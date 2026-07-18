"""LangGraph ReAct agent loop with SSE event streaming."""

import asyncio
import json
import logging
import operator
from typing import Any, AsyncGenerator, Annotated, TypedDict

from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)
from langchain_core.runnables import RunnableConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END

from app.agent.cost_tracker import CostTracker
from app.agent.prompts import SYNTHESIS_PROMPT, SYSTEM_PROMPT
from app.agent.tools.code_executor import code_executor
from app.agent.tools.pdf_reader import pdf_reader
from app.agent.tools.vector_memory import retrieve_memory, store_memory
from app.agent.tools.web_search import web_search
from app.config import get_settings
from app.models.schemas import SSEEvent, ToolResult

logger = logging.getLogger(__name__)

_TOOLS = [web_search, pdf_reader, code_executor, store_memory, retrieve_memory]
_TOOL_MAP = {t.name: t for t in _TOOLS}
_MODEL = "gemini-2.0-flash"


def _build_llm() -> ChatGoogleGenerativeAI:
    settings = get_settings()
    return ChatGoogleGenerativeAI(
        model=_MODEL,
        google_api_key=settings.gemini_api_key,
        streaming=True,
    )


def _emit(run_id: str, event_type: str, data: dict[str, Any]) -> SSEEvent:
    return SSEEvent(type=event_type, data=data, run_id=run_id)


class AgentState(TypedDict):
    messages: Annotated[list[Any], operator.add]
    iteration: int


async def call_agent(state: AgentState, config: RunnableConfig) -> dict[str, Any]:
    configurable = config.get("configurable", {})
    run_id = configurable.get("run_id")
    max_cost_usd = configurable.get("max_cost_usd", 1.0)
    tracker: CostTracker = configurable.get("tracker")
    emit_event = configurable.get("emit_event")

    iteration = state.get("iteration", 0) + 1

    # Check budget
    if tracker.is_over_budget(max_cost_usd):
        emit_event(
            "error",
            {
                "message": f"Budget cap ${max_cost_usd} reached. Proceeding to synthesis.",
                "recoverable": True,
            },
        )
        return {"messages": [], "iteration": iteration}

    llm = _build_llm()
    llm_with_tools = llm.bind_tools(_TOOLS)

    reasoning_text = ""
    tool_calls_raw = []

    try:
        async for chunk in llm_with_tools.astream(state["messages"]):
            if hasattr(chunk, "content") and chunk.content:
                delta = chunk.content if isinstance(chunk.content, str) else ""
                if delta:
                    reasoning_text += delta
                    emit_event("reasoning", {"delta": delta})

            if hasattr(chunk, "tool_calls") and chunk.tool_calls:
                tool_calls_raw.extend(chunk.tool_calls)

            # Record cost from usage metadata if available
            if hasattr(chunk, "usage_metadata") and chunk.usage_metadata:
                meta = chunk.usage_metadata
                snapshot = tracker.record(
                    _MODEL,
                    prompt_tokens=meta.get("input_tokens", 0),
                    completion_tokens=meta.get("output_tokens", 0),
                )
                emit_event("cost", snapshot.model_dump())
    except Exception as exc:
        logger.error(
            "LLM stream error at iteration %d: %s", iteration, exc
        )
        emit_event(
            "error",
            {"message": str(exc), "recoverable": False},
        )
        raise exc

    ai_message = AIMessage(content=reasoning_text, tool_calls=tool_calls_raw)
    return {"messages": [ai_message], "iteration": iteration}


async def execute_tools(state: AgentState, config: RunnableConfig) -> dict[str, Any]:
    configurable = config.get("configurable", {})
    run_id = configurable.get("run_id")
    emit_event = configurable.get("emit_event")

    last_message = state["messages"][-1]
    new_messages = []

    if not isinstance(last_message, AIMessage) or not last_message.tool_calls:
        return {"messages": []}

    for tc in last_message.tool_calls:
        tool_name = tc.get("name", "")
        tool_args = dict(tc.get("args", {}))
        tool_id = tc.get("id", f"call_{state.get('iteration', 0)}")

        # Inject correct run_id for memory tools defensively
        if tool_name in ("store_memory", "retrieve_memory"):
            if "run_id" not in tool_args or not tool_args["run_id"]:
                tool_args["run_id"] = run_id

        emit_event(
            "tool_call", {"tool": tool_name, "input": tool_args}
        )

        tool_fn = _TOOL_MAP.get(tool_name)
        if tool_fn is None:
            result = ToolResult(
                success=False,
                output="",
                error=f"Unknown tool: {tool_name}",
            )
        else:
            try:
                result = await tool_fn.ainvoke(tool_args)
            except Exception as exc:
                logger.warning("Tool %s raised: %s", tool_name, exc)
                result = ToolResult(
                    success=False, output="", error=str(exc)
                )

        if not result.success:
            emit_event(
                "error",
                {
                    "message": f"{tool_name} failed: {result.error}",
                    "recoverable": True,
                },
            )

        emit_event(
            "tool_result",
            {
                "tool": tool_name,
                "success": result.success,
                "output": result.output[:2000],  # Truncate for SSE
            },
        )

        new_messages.append(
            ToolMessage(content=result.output, tool_call_id=tool_id)
        )

    return {"messages": new_messages}


async def synthesize_report(state: AgentState, config: RunnableConfig) -> dict[str, Any]:
    configurable = config.get("configurable", {})
    emit_event = configurable.get("emit_event")
    tracker = configurable.get("tracker")

    llm = _build_llm()
    synthesis_message = HumanMessage(content=SYNTHESIS_PROMPT)
    all_messages = list(state["messages"]) + [synthesis_message]

    report_text = ""
    try:
        async for chunk in llm.astream(all_messages):
            if hasattr(chunk, "content") and chunk.content:
                delta = chunk.content if isinstance(chunk.content, str) else ""
                report_text += delta
                emit_event("reasoning", {"delta": delta})

            if hasattr(chunk, "usage_metadata") and chunk.usage_metadata:
                meta = chunk.usage_metadata
                snapshot = tracker.record(
                    _MODEL,
                    prompt_tokens=meta.get("input_tokens", 0),
                    completion_tokens=meta.get("output_tokens", 0),
                )
                emit_event("cost", snapshot.model_dump())
    except Exception as exc:
        logger.error("Synthesis failed: %s", exc)
        emit_event(
            "error",
            {"message": f"Synthesis error: {exc}", "recoverable": False},
        )
        raise exc

    emit_event("report", {"markdown": report_text})
    return {"messages": [AIMessage(content=report_text)]}


def should_continue(state: AgentState, config: RunnableConfig) -> str:
    configurable = config.get("configurable", {})
    max_cost_usd = configurable.get("max_cost_usd", 1.0)
    tracker: CostTracker = configurable.get("tracker")
    settings = configurable.get("settings")
    emit_event = configurable.get("emit_event")

    iteration = state.get("iteration", 0)

    if iteration >= settings.max_iterations:
        if emit_event:
            emit_event(
                "error",
                {
                    "message": f"Iteration limit {settings.max_iterations} reached. Proceeding to synthesis.",
                    "recoverable": True,
                },
            )
        return "synthesize"

    if tracker.is_over_budget(max_cost_usd):
        if emit_event:
            emit_event(
                "error",
                {
                    "message": f"Budget cap ${max_cost_usd} reached. Proceeding to synthesis.",
                    "recoverable": True,
                },
            )
        return "synthesize"

    messages = state.get("messages", [])
    if not messages:
        return "synthesize"

    last_message = messages[-1]

    if not isinstance(last_message, AIMessage) or not last_message.tool_calls:
        return "synthesize"

    return "tools"


# Compile the StateGraph workflow
workflow = StateGraph(AgentState)
workflow.add_node("agent", call_agent)
workflow.add_node("tools", execute_tools)
workflow.add_node("synthesize", synthesize_report)

workflow.add_edge(START, "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "synthesize": "synthesize",
    },
)
workflow.add_edge("tools", "agent")
workflow.add_edge("synthesize", END)

graph = workflow.compile()


async def run_agent(
    run_id: str,
    topic: str,
    max_cost_usd: float,
) -> AsyncGenerator[SSEEvent, None]:
    """Run the research agent and yield SSEEvent objects as they occur.

    The caller is responsible for serialising and sending these to the
    SSE stream.
    """
    settings = get_settings()
    tracker = CostTracker()
    event_queue: asyncio.Queue[SSEEvent | None] = asyncio.Queue()

    def emit_event(event_type: str, data: dict[str, Any]) -> None:
        event_queue.put_nowait(
            SSEEvent(type=event_type, data=data, run_id=run_id)
        )

    system = SystemMessage(content=SYSTEM_PROMPT.format(run_id=run_id))
    human = HumanMessage(content=f"Research topic: {topic}")
    initial_state = {
        "messages": [system, human],
        "iteration": 0,
    }

    config = {
        "configurable": {
            "run_id": run_id,
            "topic": topic,
            "max_cost_usd": max_cost_usd,
            "tracker": tracker,
            "emit_event": emit_event,
            "settings": settings,
        }
    }

    async def run_workflow() -> None:
        try:
            await graph.ainvoke(initial_state, config)
            emit_event("done", {"run_id": run_id})
        except Exception as exc:
            logger.error("Workflow run failed: %s", exc, exc_info=True)
            # Make sure we emit error if we haven't completed gracefully
            emit_event(
                "error",
                {"message": f"Workflow failed: {exc}", "recoverable": False},
            )
        finally:
            event_queue.put_nowait(None)

    task = asyncio.create_task(run_workflow())

    while True:
        event = await event_queue.get()
        if event is None:
            break
        yield event

    await task
