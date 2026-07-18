from dataclasses import dataclass, field

from app.models.schemas import CostSnapshot

# Prices per 1 million tokens (USD) — Gemini pricing as of 2024-07
_PRICE_PER_1M: dict[str, dict[str, float]] = {
    "gemini-3.5-flash": {"input": 0.075, "output": 0.30},
    "gemini-2.5-flash": {"input": 0.075, "output": 0.30},
    "gemini-2.0-flash": {"input": 0.075, "output": 0.30},
    "gemini-2.0-flash-exp": {"input": 0.075, "output": 0.30},
    "gemini-1.5-flash": {"input": 0.075, "output": 0.30},
    "gemini-1.5-pro": {"input": 1.25, "output": 5.00},
}


@dataclass
class CostTracker:
    """Accumulates token usage and USD cost across LLM calls."""

    _input_tokens: int = field(default=0, init=False)
    _output_tokens: int = field(default=0, init=False)
    _total_usd: float = field(default=0.0, init=False)

    def record(
        self, model: str, prompt_tokens: int, completion_tokens: int
    ) -> CostSnapshot:
        """Record token usage for one LLM call and return updated snapshot."""
        self._input_tokens += prompt_tokens
        self._output_tokens += completion_tokens

        pricing = _PRICE_PER_1M.get(model, {"input": 0.0, "output": 0.0})
        call_usd = (
            prompt_tokens / 1_000_000 * pricing["input"]
            + completion_tokens / 1_000_000 * pricing["output"]
        )
        self._total_usd += call_usd
        return self.get_total()

    def record_estimate(
        self, model: str, input_chars: int = 0, output_chars: int = 0
    ) -> CostSnapshot:
        """Record a conservative live estimate when provider usage is delayed.

        Gemini streaming does not guarantee usage metadata on every chunk. The
        UI still needs monotonic spend telemetry while reasoning and tool work
        are happening, so this method estimates tokens from character volume.
        """
        prompt_tokens = max(0, input_chars // 4)
        completion_tokens = max(0, output_chars // 4)
        if input_chars > 0 and prompt_tokens == 0:
            prompt_tokens = 1
        if output_chars > 0 and completion_tokens == 0:
            completion_tokens = 1
        return self.record(model, prompt_tokens, completion_tokens)

    def get_total(self) -> CostSnapshot:
        """Return current cumulative snapshot."""
        return CostSnapshot(
            input_tokens=self._input_tokens,
            output_tokens=self._output_tokens,
            total_tokens=self._input_tokens + self._output_tokens,
            total_usd=round(self._total_usd, 6),
        )

    def is_over_budget(self, max_usd: float) -> bool:
        """Check whether cumulative spend has reached the cap."""
        return self._total_usd >= max_usd
