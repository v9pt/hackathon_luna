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
