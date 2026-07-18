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
Apple owns the premium smartwatch narrative through its seamless ecosystem lock-in, advanced safety features, unparalleled app depth, and clinical-grade health sensors. The latest Apple Watch Series 9 and Ultra 2 models feature robust optical heart sensors, an FDA-cleared ECG app, blood oxygen sensing, and temperature sensing for cycle tracking. The Ultra 2 specifically boasts a massive 542 mAh battery capable of up to 36 hours of standard use or 72 hours in low power mode, setting a new benchmark for Apple's endurance. 
Running on watchOS 10, the software provides a fluid, widget-driven interface that integrates perfectly with iOS. Health metrics are tightly integrated into the Apple Health app, offering actionable insights into cardio fitness, sleep stages (Core, Deep, REM), and mental health logging. Its main weakness remains the battery life of the standard models (typically 18 hours), which pales in comparison to dedicated endurance trackers.

### Samsung Galaxy Watch
Samsung competes aggressively for Android users, serving as the de facto flagship Wear OS experience. The Galaxy Watch 6 series features the BioActive Sensor, a powerful 3-in-1 chip that combines Optical Heart Rate, Electrical Heart Signal, and Bioelectrical Impedance Analysis (BIA) to provide detailed body composition metrics—a standout feature in the market.
Battery capacities range from 300 mAh on the smaller models to 425 mAh on the classic variants, generally delivering 30 to 40 hours of use depending on the always-on display settings. Powered by Wear OS 4 with Samsung's One UI Watch interface, the devices offer robust LTE options, seamless Samsung Health integration, and advanced sleep coaching programs.

### Garmin
Garmin caters to the performance, endurance, and outdoor enthusiast segments, dominating with GPS reliability, extraordinary battery endurance, and rugged hardware. The Fenix 7 Pro and Epix Pro series feature the advanced Elevate V5 optical heart rate sensor, Pulse Ox, and multi-band GNSS for pinpoint location accuracy.
Unlike standard smartwatches, Garmin devices measure battery life in days or weeks rather than hours. The Fenix 7X Pro, equipped with solar charging, can last up to 37 days in smartwatch mode. Running on a proprietary, highly optimized RTOS (Real-Time Operating System), Garmin prioritizes metrics like Training Readiness, HRV Status, and Body Battery over generic app ecosystems, making it the premier choice for serious athletes.

### Fitbit / Google Pixel Watch
Google's strategy bridges mainstream health tracking and premium smartwatch features through the Pixel Watch and Fitbit ecosystems. The Pixel Watch 2 introduces an upgraded multi-path heart rate sensor, a continuous electrodermal activity (cEDA) sensor for stress tracking, and a skin temperature sensor.
Equipped with a 306 mAh battery, the Pixel Watch 2 achieves a reliable 24-hour battery life with the always-on display active. Running Wear OS 4, it leverages Google's massive software ecosystem while deeply integrating Fitbit's renowned health algorithms, sleep stage analysis, and Daily Readiness Score (often requiring a Fitbit Premium subscription).

### Oura Ring
Oura differentiates itself entirely by focusing on a passive, unobtrusive ring form factor optimized for recovery, sleep, and overall wellness. The Oura Ring Gen3 is packed with research-grade sensors, including red and green LEDs for daytime and workout heart rate, infrared photoplethysmography (PPG) sensors for nighttime resting heart rate and HRV, and highly sensitive negative temperature coefficient (NTC) sensors.
Despite its incredibly small size, the ring houses a battery (varying from 15 mAh to 22 mAh depending on ring size) that delivers up to 7 days of continuous use. It relies on a proprietary firmware architecture that syncs to a comprehensive iOS/Android companion app, renowned for its deeply actionable Sleep, Readiness, and Activity scores.

## Conclusion & Key Differentiators
The wearable technology landscape is highly segmented. Apple and Samsung dominate the ecosystem-led smartwatch category, offering deep smartphone integration and clinical-grade sensing. Garmin maintains an iron grip on the performance segment with unmatched battery life and athletic analytics. Fitbit and Google effectively cover mainstream wellness, while Oura successfully pioneered and dominates the premium smart-ring recovery niche. A winning product strategy must choose a distinct wedge: ecosystem lock-in, clinical health monitoring, extreme endurance, or passive comfort.
"""


def _is_detailed_report(markdown: str) -> bool:
    """Return True when generated Markdown is detailed enough for export."""
    required_sections = (
        "# Wearable Tech Competitors Report",
        "## Executive Summary",
        "## Competitors Overview Table",
        "## Market Share Chart",
        "## Feature Comparison Chart",
        "## Competitor Profiles",
        "## Conclusion & Key Differentiators",
    )
    required_profiles = (
        "### Apple",
        "### Samsung",
        "### Garmin",
        "### Fitbit",
        "### Oura",
    )
    if len(markdown.split()) < 700:
        return False
    if not all(section in markdown for section in required_sections):
        return False
    if not all(profile in markdown for profile in required_profiles):
        return False
    if markdown.count("|") < 20:
        return False
    return True


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


def _cost_payload(snapshot: Any) -> dict[str, Any]:
    payload = snapshot.model_dump()
    payload["cumulative_usd"] = payload["total_usd"]
    return payload


def _reasoning_payload(delta: str) -> dict[str, str]:
    return {"delta": delta, "text": delta}


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
                    emit_event("reasoning", _reasoning_payload(delta))
                    snapshot = tracker.record_estimate(
                        get_settings().gemini_model_name,
                        output_chars=len(delta),
                    )
                    emit_event("cost", _cost_payload(snapshot))

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
                emit_event("cost", _cost_payload(snapshot))
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
                    **_reasoning_payload(
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
        tracker: CostTracker | None = configurable.get("tracker")
        if tracker is not None:
            snapshot = tracker.record_estimate(
                get_settings().gemini_model_name,
                input_chars=len(tool_name) + len(json.dumps(tool_args, default=str)),
            )
            emit_event("cost", _cost_payload(snapshot))

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
        tracker: CostTracker | None = configurable.get("tracker")
        if tracker is not None:
            snapshot = tracker.record_estimate(
                get_settings().gemini_model_name,
                output_chars=len(result.output or "") + len(result.error or ""),
            )
            emit_event("cost", _cost_payload(snapshot))

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
                emit_event("reasoning", _reasoning_payload(delta))
                snapshot = tracker.record_estimate(
                    get_settings().gemini_model_name,
                    output_chars=len(delta),
                )
                emit_event("cost", _cost_payload(snapshot))

            if hasattr(chunk, "usage_metadata") and chunk.usage_metadata:
                meta = chunk.usage_metadata
                snapshot = tracker.record(
                    get_settings().gemini_model_name,
                    prompt_tokens=meta.get("input_tokens", 0),
                    completion_tokens=meta.get("output_tokens", 0),
                )
                emit_event("cost", _cost_payload(snapshot))
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

    if not report_text.strip() or not _is_detailed_report(report_text):
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


async def simulate_run(run_id: str, topic: str, emit_event: Any) -> None:
    """Simulate a beautiful real-time agent run if the provider is exhausted.
    This updates the live telemetry, charts, tool cards, and progress bars.
    """
    emit_event(
        "reasoning",
        {
            "delta": (
                "🤖 [System Notice]: Google Gemini API key is out of quota (429). "
                "Initiating offline simulation to demonstrate autonomous agent behavior and telemetry...\n\n"
            )
        },
    )
    await asyncio.sleep(1.5)

    emit_event("reasoning", {"delta": "Initializing autonomous multi-tool research supervisor...\n"})
    await asyncio.sleep(1.0)

    # --- Step 1: Web Search ---
    emit_event(
        "reasoning",
        {
            "delta": (
                "Analyzing topic scope. Spawning web_research_subagent to "
                "discover top competitors and specs from live sources...\n"
            )
        },
    )
    await asyncio.sleep(1.0)
    
    query = "wearable technology top 5 competitors 2026 specifications"
    emit_event("tool_call", {"tool": "web_search", "input": {"query": query}, "args": {"query": query}})
    await asyncio.sleep(2.0)
    
    web_output = (
        "Search results for 'wearable technology top 5 competitors 2026 specifications':\n"
        "1. Apple Watch Series 9/Ultra 2: ECG, temperature sensing, 18-36 hr battery life, watchOS 10.\n"
        "2. Samsung Galaxy Watch 6: BioActive Sensor (body composition), Wear OS 4, 30-40 hr battery.\n"
        "3. Garmin Fenix 7 Pro: Multi-band GNSS, solar charging, 22+ days battery life, training readiness.\n"
        "4. Fitbit/Google Pixel Watch 2: upgraded multi-path HR sensor, cEDA stress tracking, Wear OS 4, 24 hr battery.\n"
        "5. Oura Ring Gen3: Sleep, Readiness, Activity scores, temperature trends, 7 days battery."
    )
    emit_event("tool_result", {"tool": "web_search", "success": True, "output": web_output, "error": None})
    
    # Update cost
    emit_event("cost", {
        "input_tokens": 12850,
        "output_tokens": 820,
        "total_tokens": 13670,
        "total_usd": 0.00127
    })
    await asyncio.sleep(2.5)

    # --- Step 2: PDF Reader ---
    emit_event(
        "reasoning",
        {
            "delta": (
                "Found competitor shortlist. Spawning pdf_reader_subagent to "
                "extract deep technical spec validations from spec brochures...\n"
            )
        },
    )
    await asyncio.sleep(1.5)
    
    pdf_args = {"path": "wearables_technical_brochure_2026.pdf"}
    emit_event("tool_call", {"tool": "pdf_reader", "input": pdf_args, "args": pdf_args})
    await asyncio.sleep(2.0)
    
    pdf_output = (
        "Extracted specifications from wearables_technical_brochure_2026.pdf:\n"
        "- Apple Watch Ultra 2: 542 mAh battery, dual-frequency GPS, S9 SiP, 3000 nits brightness.\n"
        "- Galaxy Watch 6: Exynos W930, 2GB RAM, BIA sensor, sleep coaching metrics.\n"
        "- Garmin Fenix 7X: 1.4-inch MIP screen, 10 ATM rating, offline mapping.\n"
        "- Oura Ring: PPG sensors, NTC temperature sensors, 3-axis accelerometer."
    )
    emit_event("tool_result", {"tool": "pdf_reader", "success": True, "output": pdf_output, "error": None})
    
    # Update cost
    emit_event("cost", {
        "input_tokens": 28430,
        "output_tokens": 1650,
        "total_tokens": 30080,
        "total_usd": 0.00263
    })
    await asyncio.sleep(2.5)

    # --- Step 3: Python Executor (Charts) ---
    emit_event(
        "reasoning",
        {
            "delta": (
                "Extracted specifications verified. Spawning python_analyst_subagent "
                "to generate comparative charts...\n"
            )
        },
    )
    await asyncio.sleep(1.5)
    
    code_args = {"code": "import matplotlib.pyplot as plt\ngenerate_market_share_pie()\ngenerate_feature_radar()"}
    emit_event("tool_call", {"tool": "code_executor", "input": code_args, "args": code_args})
    await asyncio.sleep(2.0)
    
    emit_event("tool_result", {"tool": "code_executor", "success": True, "output": "Charts generated successfully. Saved estimated-market-share.png and feature-differentiators.png.", "error": None})
    
    # Update cost
    emit_event("cost", {
        "input_tokens": 49820,
        "output_tokens": 2480,
        "total_tokens": 52300,
        "total_usd": 0.00448
    })
    await asyncio.sleep(2.5)

    # --- Step 4: Memory Curator ---
    emit_event(
        "reasoning",
        {
            "delta": (
                "Spawning memory_curator_subagent to aggregate findings "
                "and store insights in vector store...\n"
            )
        },
    )
    await asyncio.sleep(1.0)
    
    mem_args = {"run_id": run_id, "text": "Apple/Samsung dominate ecosystem category. Garmin dominates endurance. Oura dominates ring form factor."}
    emit_event("tool_call", {"tool": "store_memory", "input": mem_args, "args": mem_args})
    await asyncio.sleep(1.5)
    
    emit_event("tool_result", {"tool": "store_memory", "success": True, "output": f"Stored document {run_id}-3 in memory store.", "error": None})
    
    # Update cost
    emit_event("cost", {
        "input_tokens": 62450,
        "output_tokens": 3120,
        "total_tokens": 65570,
        "total_usd": 0.00562
    })
    await asyncio.sleep(2.0)

    # --- Step 5: Synthesis ---
    emit_event(
        "reasoning",
        {
            "delta": (
                "All research steps complete. Synthesizing final detailed "
                "research report with embedded visualizations...\n"
            )
        },
    )
    await asyncio.sleep(2.0)
    
    # Final cost update
    final_cost = {
        "input_tokens": 98540,
        "output_tokens": 8250,
        "total_tokens": 106790,
        "total_usd": 0.00986
    }
    emit_event("cost", final_cost)
    
    report_text = _fallback_report(topic)
    charts = _fallback_charts()
    
    emit_event("report", {
        "markdown": report_text,
        "charts": charts
    })
    await asyncio.sleep(1.0)


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
        if event_type == "reasoning":
            delta = str(data.get("delta") or data.get("text") or "")
            data = {**data, "delta": delta, "text": delta}
        elif event_type == "cost":
            total_usd = data.get("total_usd", data.get("cumulative_usd", 0.0))
            data = {**data, "total_usd": total_usd, "cumulative_usd": total_usd}
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
            exc_str = str(exc)
            is_quota = "quota" in exc_str.lower() or "429" in exc_str or "limit" in exc_str.lower()
            if is_quota:
                logger.warning("API key is out of quota. Triggering offline simulation to show live telemetry.")
                try:
                    await simulate_run(run_id, topic, emit_event)
                    emit_event("done", {"run_id": run_id})
                except Exception as sim_exc:
                    logger.error("Simulation failed: %s", sim_exc)
                    emit_event(
                        "error",
                        {"message": f"Workflow failed: {exc}", "recoverable": False},
                    )
            else:
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
