from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import create_app
from app.models.schemas import SSEEvent

app = create_app()


class TestRoutes:
    """Tests for the FastAPI REST / SSE routes."""

    @pytest.mark.asyncio
    async def test_health_endpoint(self) -> None:
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            resp = await client.get("/health")
        assert resp.status_code == 200
        assert resp.json() == {"status": "ok"}

    @pytest.mark.asyncio
    async def test_post_run_returns_run_id(self) -> None:
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            resp = await client.post(
                "/api/v1/agent/run",
                json={"topic": "wearables", "max_cost_usd": 0.5},
            )
        assert resp.status_code == 200
        body = resp.json()
        assert "run_id" in body
        assert len(body["run_id"]) > 0

    @pytest.mark.asyncio
    async def test_stream_returns_event_stream_content_type(self) -> None:
        # Seed a run_id first
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            run_resp = await client.post(
                "/api/v1/agent/run", json={"topic": "test"}
            )
            run_id = run_resp.json()["run_id"]

        async def _mock_sse_gen(
            run_id: str, topic: str, max_cost_usd: float
        ):
            yield SSEEvent(
                type="done", data={"run_id": run_id}, run_id=run_id
            )

        with patch("app.api.router.run_agent", side_effect=_mock_sse_gen):
            async with AsyncClient(
                transport=ASGITransport(app=app), base_url="http://test"
            ) as client:
                async with client.stream(
                    "GET", f"/api/v1/agent/stream/{run_id}"
                ) as resp:
                    assert resp.status_code == 200
                    assert "text/event-stream" in resp.headers["content-type"]

    @pytest.mark.asyncio
    async def test_export_endpoints(self) -> None:
        from app.api.router import _reports, _runs
        from app.models.schemas import AgentRunRequest

        run_id = "test-export-run"
        _runs[run_id] = AgentRunRequest(topic="test")
        _reports[run_id] = "# Test Report\n\nSome body text."

        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as client:
            # 1. Test markdown export
            resp = await client.get(f"/api/v1/agent/report/{run_id}/markdown")
            assert resp.status_code == 200
            assert resp.headers["content-type"].startswith("text/markdown")
            assert "attachment; filename=" in resp.headers["content-disposition"]
            assert resp.text == "# Test Report\n\nSome body text."

            # 2. Test PDF export
            resp = await client.get(f"/api/v1/agent/report/{run_id}/pdf")
            assert resp.status_code == 200
            assert resp.headers["content-type"] == "application/pdf"
            assert "attachment; filename=" in resp.headers["content-disposition"]
            assert len(resp.content) > 0

            # 3. Test nonexistent run returns 404
            resp = await client.get("/api/v1/agent/report/nonexistent/pdf")
            assert resp.status_code == 404

