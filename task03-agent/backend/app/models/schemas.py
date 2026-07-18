from typing import Any, Literal, Optional

from pydantic import BaseModel


class ToolResult(BaseModel):
    """Standardised return type for all agent tools."""

    success: bool
    output: str
    error: Optional[str] = None


class CostSnapshot(BaseModel):
    """Cumulative token-usage and cost snapshot."""

    input_tokens: int
    output_tokens: int
    total_tokens: int
    total_usd: float


class SSEEvent(BaseModel):
    """Server-Sent Event payload sent to the frontend."""

    type: Literal[
        "reasoning",
        "tool_call",
        "tool_result",
        "cost",
        "report",
        "error",
        "done",
    ]
    data: dict[str, Any]
    run_id: str

    def to_sse_line(self) -> str:
        """Serialise to the SSE wire format: ``data: {...}\\n\\n``."""
        return f"data: {self.model_dump_json()}\n\n"


class AgentRunRequest(BaseModel):
    """Body of ``POST /api/v1/agent/run``."""

    topic: str = "wearable technology competitive landscape top 5 competitors"
    max_cost_usd: float = 1.0
