import pytest
from app.agent.cost_tracker import CostTracker


class TestCostTracker:
    """Tests for the CostTracker accumulator."""

    def test_record_accumulates_tokens(self) -> None:
        tracker = CostTracker()
        tracker.record("gemini-2.0-flash", prompt_tokens=1000, completion_tokens=200)
        tracker.record("gemini-2.0-flash", prompt_tokens=500, completion_tokens=100)

        snapshot = tracker.get_total()
        assert snapshot.input_tokens == 1500
        assert snapshot.output_tokens == 300
        assert snapshot.total_tokens == 1800

    def test_cost_calculated_correctly(self) -> None:
        tracker = CostTracker()
        # 1M input @ $0.075, 1M output @ $0.30 → $0.375
        tracker.record(
            "gemini-2.0-flash",
            prompt_tokens=1_000_000,
            completion_tokens=1_000_000,
        )
        snapshot = tracker.get_total()
        assert abs(snapshot.total_usd - 0.375) < 0.001

    def test_is_over_budget_false_when_under(self) -> None:
        tracker = CostTracker()
        tracker.record("gemini-2.0-flash", prompt_tokens=100, completion_tokens=50)
        assert tracker.is_over_budget(max_usd=1.0) is False

    def test_is_over_budget_true_when_over(self) -> None:
        tracker = CostTracker()
        tracker.record(
            "gemini-2.0-flash",
            prompt_tokens=10_000_000,
            completion_tokens=1_000_000,
        )
        assert tracker.is_over_budget(max_usd=1.0) is True

    def test_unknown_model_uses_zero_cost(self) -> None:
        tracker = CostTracker()
        tracker.record("unknown-model", prompt_tokens=1000, completion_tokens=1000)
        snapshot = tracker.get_total()
        assert snapshot.total_usd == 0.0
