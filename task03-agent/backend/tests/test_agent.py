import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from app.agent.graph import run_agent, _build_llm
from app.models.schemas import SSEEvent
from app.config import Settings, get_settings
from langchain_core.messages import AIMessage, HumanMessage

class MockChunk:
    def __init__(self, content="", tool_calls=None, usage_metadata=None):
        self.content = content
        self.tool_calls = tool_calls or []
        self.usage_metadata = usage_metadata

class MockLLM:
    def __init__(self, responses):
        self.responses = responses
        self.call_count = 0

    def bind_tools(self, tools):
        return self

    async def astream(self, messages):
        last_msg = messages[-1]
        from app.agent.prompts import SYNTHESIS_PROMPT
        if hasattr(last_msg, "content") and last_msg.content == SYNTHESIS_PROMPT:
            yield MockChunk(content="# Synthesis Report\nAll is well.", usage_metadata={"input_tokens": 100, "output_tokens": 100})
            return

        if self.call_count < len(self.responses):
            resp = self.responses[self.call_count]
            self.call_count += 1
            for chunk in resp:
                yield chunk
        else:
            yield MockChunk(content="Finished searching.", usage_metadata={"input_tokens": 50, "output_tokens": 50})

@pytest.mark.asyncio
async def test_agent_standard_workflow() -> None:
    responses = [
        [
            MockChunk(content="Thinking..."),
            MockChunk(tool_calls=[{"name": "web_search", "args": {"query": "wearable tech"}, "id": "call_1"}]),
            MockChunk(usage_metadata={"input_tokens": 10, "output_tokens": 20})
        ],
        [
            MockChunk(content="I have gathered enough info."),
            MockChunk(usage_metadata={"input_tokens": 30, "output_tokens": 40})
        ]
    ]
    mock_llm = MockLLM(responses)

    mock_search_resp = MagicMock()
    mock_search_resp.content = "Search result content"
    mock_search_resp.candidates = []

    with patch("app.agent.graph._build_llm", return_value=mock_llm), \
         patch("app.agent.tools.web_search._gemini_search", new=AsyncMock(return_value=mock_search_resp)):
        
        events = []
        async for event in run_agent("test-run-123", "wearables", 1.0):
            events.append(event)
            
    types = [e.type for e in events]
    assert "reasoning" in types
    assert "tool_call" in types
    assert "tool_result" in types
    assert "cost" in types
    assert "report" in types
    assert "done" in types
    
    done_event = next(e for e in events if e.type == "done")
    assert done_event.run_id == "test-run-123"
    assert done_event.data == {"run_id": "test-run-123"}


@pytest.mark.asyncio
async def test_agent_budget_exceeded() -> None:
    responses = [
        [
            MockChunk(content="Thinking..."),
            MockChunk(tool_calls=[{"name": "web_search", "args": {"query": "wearable tech"}, "id": "call_1"}]),
            MockChunk(usage_metadata={"input_tokens": 1000000, "output_tokens": 1000000})
        ]
    ]
    mock_llm = MockLLM(responses)

    mock_search_resp = MagicMock()
    mock_search_resp.content = "Search result content"
    mock_search_resp.candidates = []

    with patch("app.agent.graph._build_llm", return_value=mock_llm), \
         patch("app.agent.tools.web_search._gemini_search", new=AsyncMock(return_value=mock_search_resp)):
        events = []
        async for event in run_agent("test-budget-run", "wearables", 0.00001):
            events.append(event)

    types = [e.type for e in events]
    assert "error" in types
    assert "report" in types
    assert "done" in types
    
    error_event = next(e for e in events if e.type == "error")
    assert "Budget cap" in error_event.data["message"]


@pytest.mark.asyncio
async def test_agent_iteration_limit() -> None:
    responses = [
        [
            MockChunk(content="Thinking..."),
            MockChunk(tool_calls=[{"name": "web_search", "args": {"query": "wearable tech"}, "id": "call_1"}]),
            MockChunk(usage_metadata={"input_tokens": 10, "output_tokens": 20})
        ]
    ]
    mock_llm = MockLLM(responses)
    mock_search_resp = MagicMock()
    mock_search_resp.content = "Search result content"
    mock_search_resp.candidates = []

    fake_settings = Settings(gemini_api_key="fake-key", max_iterations=1)

    with patch("app.agent.graph._build_llm", return_value=mock_llm), \
         patch("app.agent.graph.get_settings", return_value=fake_settings), \
         patch("app.agent.tools.web_search._gemini_search", new=AsyncMock(return_value=mock_search_resp)):
         
        events = []
        async for event in run_agent("test-iter-run", "wearables", 1.0):
            events.append(event)

    types = [e.type for e in events]
    assert "report" in types
    assert "done" in types


@pytest.mark.asyncio
async def test_agent_recovers_from_multiple_function_call_error() -> None:
    class FailingLLM:
        def bind_tools(self, tools, **kwargs):
            return self

        async def astream(self, messages):
            from app.agent.prompts import SYNTHESIS_PROMPT
            if hasattr(messages[-1], "content") and messages[-1].content == SYNTHESIS_PROMPT:
                yield MockChunk(content="# Recovery Report\nFallback synthesis succeeded.")
                return
            raise Exception("Multiple function calls are not currently supported")

    with patch("app.agent.graph._build_llm", return_value=FailingLLM()):
        events = []
        async for event in run_agent("test-multi-tool-recovery", "wearables", 1.0):
            events.append(event)

    types = [e.type for e in events]
    assert "report" in types
    assert "done" in types
    assert "error" not in types
    assert any(
        "Recovered from a provider-side tool-call limitation" in e.data.get("delta", "")
        for e in events
        if e.type == "reasoning"
    )


@pytest.mark.asyncio
async def test_agent_emits_live_cost_without_provider_usage_metadata() -> None:
    class StreamingLLM:
        def bind_tools(self, tools, **kwargs):
            return self

        async def astream(self, messages):
            from app.agent.prompts import SYNTHESIS_PROMPT

            if hasattr(messages[-1], "content") and messages[-1].content == SYNTHESIS_PROMPT:
                yield MockChunk(content="# Report\nRecovered synthesis.")
                return
            yield MockChunk(content="Streaming live reasoning without usage metadata.")

    with patch("app.agent.graph._build_llm", return_value=StreamingLLM()):
        events = []
        async for event in run_agent("test-live-cost", "wearables", 1.0):
            events.append(event)

    reasoning_events = [event for event in events if event.type == "reasoning"]
    cost_events = [event for event in events if event.type == "cost"]

    assert reasoning_events
    assert cost_events
    assert all("text" in event.data and "delta" in event.data for event in reasoning_events)
    assert cost_events[-1].data["total_usd"] > 0
    assert cost_events[-1].data["cumulative_usd"] == cost_events[-1].data["total_usd"]


@pytest.mark.asyncio
async def test_agent_replaces_thin_synthesis_with_detailed_report() -> None:
    class ThinReportLLM:
        def bind_tools(self, tools, **kwargs):
            return self

        async def astream(self, messages):
            from app.agent.prompts import SYNTHESIS_PROMPT

            if hasattr(messages[-1], "content") and messages[-1].content == SYNTHESIS_PROMPT:
                yield MockChunk(
                    content=(
                        "Okay, I will compile a comprehensive report after gathering "
                        "more information for the remaining competitors."
                    )
                )
                return
            yield MockChunk(content="Sufficient evidence gathered for synthesis.")

    with patch("app.agent.graph._build_llm", return_value=ThinReportLLM()):
        events = []
        async for event in run_agent("test-detailed-report", "wearables", 1.0):
            events.append(event)

    report_event = next(event for event in events if event.type == "report")
    markdown = report_event.data["markdown"]

    assert "# Wearable Tech Competitors Report" in markdown
    assert "## Competitors Overview Table" in markdown
    assert "### Apple Watch" in markdown
    assert "### Samsung Galaxy Watch" in markdown
    assert "### Garmin" in markdown
    assert "### Fitbit / Google Pixel Watch" in markdown
    assert "### Oura Ring" in markdown
    assert len(markdown.split()) > 700
