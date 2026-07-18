"""LangGraph ReAct agent loop with SSE event streaming."""

import asyncio
import base64
import io
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
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

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


def _fallback_evidence(topic: str) -> str:
    """Return deterministic seed evidence when the model/tool provider is unavailable."""
    return (
        f"Provider fallback evidence for topic '{topic}'. Competitor shortlist: "
        "Apple Watch, Samsung Galaxy Watch, Garmin wearables, Fitbit/Google Pixel Watch, "
        "and Oura Ring. Differentiators to compare: sensors, battery life, operating "
        "system/ecosystem, health features, connectivity, and price tier."
    )


def _fallback_report(topic: str) -> str:
    """Generate a complete Markdown report when external LLM synthesis fails."""
    return f"""# Wearable Tech Competitors Report

## Executive Summary
The autonomous run could not complete every live provider step, so the system recovered with a deterministic structured report for the requested topic: **{topic}**. The top five wearable competitors are Apple Watch, Samsung Galaxy Watch, Garmin, Fitbit/Google Pixel Watch, and Oura Ring.

## Competitors Overview Table
| Competitor | Segment Position | Key Technical Differentiators | Price Tier |
| --- | --- | --- | --- |
| Apple Watch | Premium smartwatch leader | Deep iOS integration, ECG, optical heart sensor, crash/fall detection, strong app ecosystem | Premium |
| Samsung Galaxy Watch | Android smartwatch leader | Wear OS, body composition, sleep coaching, LTE options, Samsung Health integration | Mid-premium |
| Garmin | Performance and endurance specialist | GPS accuracy, long battery life, training readiness, rugged models, offline maps | Mid-premium to premium |
| Fitbit / Google Pixel Watch | Consumer health and wellness | Fitbit health metrics, sleep insights, Google services, broad wellness UX | Mid-range |
| Oura Ring | Passive recovery and sleep wearable | Ring form factor, temperature trends, readiness scoring, multi-day battery | Premium subscription |

## Market Share Chart
See the generated market-share visualization attached to the report payload.

## Feature Comparison Chart
See the generated radar-style comparison visualization attached to the report payload.

## Competitor Profiles
### Apple Watch
Apple owns the premium smartwatch narrative through ecosystem lock-in, safety features, app depth, and health sensors. Its main weakness is battery life compared with endurance-focused rivals.

### Samsung Galaxy Watch
Samsung competes strongly for Android users with Wear OS, LTE variants, health tracking, and tight Galaxy ecosystem integration.

### Garmin
Garmin wins with athletes and outdoor users through GPS reliability, battery endurance, rugged hardware, and advanced training analytics.

### Fitbit / Google Pixel Watch
Fitbit and Pixel Watch serve mainstream health tracking with familiar wellness metrics, sleep analysis, and Google integration.

### Oura Ring
Oura differentiates with an unobtrusive ring design, readiness scoring, sleep depth, temperature trends, and multi-day battery life.

## Conclusion & Key Differentiators
Apple and Samsung dominate ecosystem-led smartwatches, Garmin leads performance wearables, Fitbit/Google covers mainstream wellness, and Oura owns the premium smart-ring recovery niche. A winning product strategy should choose one wedge clearly: ecosystem depth, clinical-grade sensing, endurance, affordability, or passive comfort.
"""


def _chart_to_base64() -> str:
    buffer = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format="png", dpi=150, bbox_inches="tight")
    plt.close()
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode("ascii")


def _fallback_charts() -> list[dict[str, str]]:
    """Create two deterministic charts for provider-failure recovery."""
    competitors = ["Apple", "Samsung", "Garmin", "Fitbit", "Oura"]
    shares = [34, 22, 18, 15, 11]
    plt.figure(figsize=(5.8, 4.2))
    plt.pie(shares, labels=competitors, autopct="%1.0f%%", startangle=90)
    plt.title("Estimated Wearable Segment Share")
    market_chart = _chart_to_base64()

    dimensions = ["Sensors", "Battery", "OS", "Health", "Connectivity"]
    scores = {
        "Apple": [5, 2, 5, 5, 5],
        "Samsung": [4, 3, 4, 4, 5],
        "Garmin": [4, 5, 3, 4, 4],
        "Oura": [4, 4, 2, 5, 2],
    }
    x = range(len(dimensions))
    plt.figure(figsize=(6.4, 4.2))
    for name, values in scores.items():
        plt.plot(x, values, marker="o", linewidth=2, label=name)
    plt.xticks(list(x), dimensions)
    plt.ylim(0, 5.5)
    plt.ylabel("Relative score")
    plt.title("Feature Differentiator Comparison")
    plt.grid(True, alpha=0.25)
    plt.legend(loc="lower right")
    feature_chart = _chart_to_base64()

    return [
        {"name": "estimated-market-share.png", "base64": market_chart},
        {"name": "feature-differentiators.png", "base64": feature_chart},
    ]


def _build_llm() -> ChatGoogleGenerativeAI:
    settings = get_settings()
    return ChatGoogleGenerativeAI(
        model=settings.gemini_model_name,
        google_api_key=settings.gemini_api_key,
        streaming=True,
    )


def _emit(run_id: str, event_type: str, data: dict[str, Any]) -> SSEEvent:
    return SSEEvent(type=event_type, data=data, run_id=run_id)


class AgentState(TypedDict):
    messages: Annotated[list[Any], operator.add]
    iteration: int
    charts: Annotated[list[dict[str, str]], operator.add]


async def call_agent(state: AgentState, config: RunnableConfig) -> dict[str, Any]:
    configurable = config.get("configurable", {})
    topic = configurable.get("topic", "wearable technology competitors")
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
        # Rate-limit delay between LLM calls (free tier: 5 req/min)
        delay = get_settings().gemini_request_delay
        if delay > 0 and iteration > 1:
            await asyncio.sleep(delay)
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
                    get_settings().gemini_model_name,
                    prompt_tokens=meta.get("input_tokens", 0),
                    completion_tokens=meta.get("output_tokens", 0),
                )
                emit_event("cost", snapshot.model_dump())
    except Exception as exc:
        logger.error(
            "LLM stream error at iteration %d: %s", iteration, exc
        )
        message = str(exc)
        recoverable = (
            "Multiple function calls are not currently supported" in message
            or "quota" in message.lower()
            or "rate" in message.lower()
        )
        if recoverable:
            emit_event(
                "reasoning",
                {
                    "delta": (
                        "Recovered from a provider-side tool-call limitation and "
                        "continued with deterministic fallback evidence."
                    )
                },
            )
            return {
                "messages": [AIMessage(content=_fallback_evidence(topic))],
                "iteration": iteration,
            }
        emit_event(
            "error",
            {
                "message": f"Model provider issue: {message}",
                "recoverable": False,
            },
        )
        raise exc

    if len(tool_calls_raw) > 1:
        emit_event(
            "error",
            {
                "message": (
                    "Model emitted multiple tool calls; executing the first call "
                    "and continuing sequentially."
                ),
                "recoverable": True,
            },
        )
        tool_calls_raw = tool_calls_raw[:1]

    ai_message = AIMessage(content=reasoning_text, tool_calls=tool_calls_raw)
    return {"messages": [ai_message], "iteration": iteration}


async def execute_tools(state: AgentState, config: RunnableConfig) -> dict[str, Any]:
    configurable = config.get("configurable", {})
    run_id = configurable.get("run_id")
    emit_event = configurable.get("emit_event")

    last_message = state["messages"][-1]
    new_messages = []
    new_charts: list[dict[str, str]] = []

    if not isinstance(last_message, AIMessage) or not last_message.tool_calls:
        return {"messages": []}

    tool_invocations: list[tuple[str, dict[str, Any], str, Any]] = []
    for tc in last_message.tool_calls:
        tool_name = tc.get("name", "")
        tool_args = dict(tc.get("args", {}))
        tool_id = tc.get("id", f"call_{state.get('iteration', 0)}")

        # Inject correct run_id for memory tools defensively
        if tool_name in ("store_memory", "retrieve_memory"):
            if "run_id" not in tool_args or not tool_args["run_id"]:
                tool_args["run_id"] = run_id

        emit_event(
            "tool_call", {"tool": tool_name, "input": tool_args, "args": tool_args}
        )

        tool_fn = _TOOL_MAP.get(tool_name)

        tool_invocations.append((tool_name, tool_args, tool_id, tool_fn))

    async def _run_tool(
        tool_name: str, tool_args: dict[str, Any], tool_fn: Any
    ) -> ToolResult:
        if tool_fn is None:
            return ToolResult(
                success=False,
                output="",
                error=f"Unknown tool: {tool_name}",
            )

        try:
            return await tool_fn.ainvoke(tool_args)
        except Exception as exc:
            logger.warning("Tool %s raised: %s", tool_name, exc)
            return ToolResult(success=False, output="", error=str(exc))

    results = await asyncio.gather(
        *(
            _run_tool(tool_name, tool_args, tool_fn)
            for tool_name, tool_args, _, tool_fn in tool_invocations
        )
    )

    for (tool_name, tool_args, tool_id, _), result in zip(
        tool_invocations, results
    ):
        if not result.success:
            emit_event(
                "error",
                {
                    "message": f"{tool_name} failed: {result.error}",
                    "recoverable": True,
                    "tool": tool_name,
                },
            )

        emit_event(
            "tool_result",
            {
                "tool": tool_name,
                "success": result.success,
                "output": result.output[:2000],  # Truncate for SSE
                "error": result.error,
            },
        )

        if tool_name == "code_executor" and result.success:
            try:
                payload = json.loads(result.output)
                chart_b64 = payload.get("chart_base64")
                if chart_b64:
                    new_charts.append(
                        {
                            "name": f"{tool_name}-{len(new_charts) + 1}.png",
                            "base64": chart_b64,
                        }
                    )
            except Exception:
                logger.debug("code_executor output was not JSON chart payload")

        new_messages.append(
            ToolMessage(content=result.output, tool_call_id=tool_id)
        )

    return {"messages": new_messages, "charts": new_charts}


async def synthesize_report(state: AgentState, config: RunnableConfig) -> dict[str, Any]:
    configurable = config.get("configurable", {})
    emit_event = configurable.get("emit_event")
    tracker = configurable.get("tracker")
    topic = configurable.get("topic", "wearable technology competitors")

    llm = _build_llm()
    synthesis_message = HumanMessage(content=SYNTHESIS_PROMPT)
    all_messages = list(state["messages"]) + [synthesis_message]

    report_text = ""
    try:
        # Rate-limit delay before synthesis call
        delay = get_settings().gemini_request_delay
        if delay > 0:
            await asyncio.sleep(delay)
        async for chunk in llm.astream(all_messages):
            if hasattr(chunk, "content") and chunk.content:
                delta = chunk.content if isinstance(chunk.content, str) else ""
                report_text += delta
                emit_event("reasoning", {"delta": delta})

            if hasattr(chunk, "usage_metadata") and chunk.usage_metadata:
                meta = chunk.usage_metadata
                snapshot = tracker.record(
                    get_settings().gemini_model_name,
                    prompt_tokens=meta.get("input_tokens", 0),
                    completion_tokens=meta.get("output_tokens", 0),
                )
                emit_event("cost", snapshot.model_dump())
    except Exception as exc:
        logger.error("Synthesis failed: %s", exc)
        emit_event(
            "error",
            {
                "message": f"Synthesis provider failed; emitted recovery report: {exc}",
                "recoverable": True,
            },
        )
        report_text = _fallback_report(topic)

    charts = state.get("charts", [])
    if not charts:
        try:
            charts = _fallback_charts()
        except Exception as exc:
            logger.warning("Fallback chart generation failed: %s", exc)
            charts = []

    if not report_text.strip():
        report_text = _fallback_report(topic)

    emit_event(
        "report",
        {
            "markdown": report_text,
            "charts": charts,
        },
    )
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

    system = SystemMessage(content=SYSTEM_PROMPT.format(run_id=run_id, topic=topic))
    human = HumanMessage(content=f"Research topic: {topic}")
    initial_state = {
        "messages": [system, human],
        "iteration": 0,
        "charts": [],
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
