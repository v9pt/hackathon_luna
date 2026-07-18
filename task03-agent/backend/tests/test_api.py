import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from httpx import ASGITransport, AsyncClient

from app.main import create_app
from app.models.schemas import SSEEvent
from app.api.router import _reports, _runs

app = create_app()

@pytest.fixture(autouse=True)
def clean_in_memory_stores():
    """Clear internal dictionary state between test runs."""
    _reports.clear()
    _runs.clear()
    yield

class TestApi:
    """Tests for the REST / SSE endpoints and error cases."""

    @pytest.mark.asyncio
    async def test_health_check(self) -> None:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            resp = await client.get("/health")
        assert resp.status_code == 200
        assert resp.json() == {"status": "ok"}

    @pytest.mark.asyncio
    async def test_start_run_success(self) -> None:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            resp = await client.post(
                "/api/v1/agent/run",
                json={"topic": "wearable market trends 2026", "max_cost_usd": 0.5}
            )
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] is True
        assert "run_id" in data
        run_id = data["run_id"]
        assert run_id in _runs
        assert _runs[run_id].topic == "wearable market trends 2026"
        assert _runs[run_id].max_cost_usd == 0.5

    @pytest.mark.asyncio
    async def test_start_run_invalid_payload(self) -> None:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            # Topic must not be empty
            resp = await client.post(
                "/api/v1/agent/run",
                json={"topic": "", "max_cost_usd": 1.0}
            )
        assert resp.status_code == 400
        assert "cannot be empty" in resp.json()["detail"]

    @pytest.mark.asyncio
    async def test_stream_nonexistent_run(self) -> None:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            resp = await client.get("/api/v1/agent/stream/fake-run-id")
        assert resp.status_code == 404
        assert "not found" in resp.json()["detail"]

    @pytest.mark.asyncio
    async def test_stream_existing_run_success(self) -> None:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            # Seed the run
            await client.post(
                "/api/v1/agent/run",
                json={"topic": "wearables"}
            )
            # Find the actual run_id created
            actual_run_id = list(_runs.keys())[0]

            # Mock run_agent generator
            async def mock_run_agent(r_id, topic, cost):
                yield SSEEvent(type="reasoning", data={"delta": "Thinking"}, run_id=r_id)
                yield SSEEvent(type="report", data={"markdown": "# Market Report"}, run_id=r_id)
                yield SSEEvent(type="done", data={"run_id": r_id}, run_id=r_id)

            with patch("app.api.router.run_agent", side_effect=mock_run_agent):
                async with client.stream("GET", f"/api/v1/agent/stream/{actual_run_id}") as stream_resp:
                    assert stream_resp.status_code == 200
                    assert "text/event-stream" in stream_resp.headers["content-type"]
                    lines = [line async for line in stream_resp.aiter_lines() if line]
            
            assert len(lines) == 3
            assert any("reasoning" in line for line in lines)
            assert any("report" in line for line in lines)
            assert any("done" in line for line in lines)

            # Assert the report was saved in-memory
            assert actual_run_id in _reports
            assert _reports[actual_run_id] == "# Market Report"

    @pytest.mark.asyncio
    async def test_get_report_endpoints(self) -> None:
        run_id = "test-report-run-id"
        
        # Test 404s before reports exist
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            resp_md_404 = await client.get(f"/api/v1/agent/report/{run_id}")
            assert resp_md_404.status_code == 404

            resp_pdf_404 = await client.get(f"/api/v1/agent/report/{run_id}/pdf")
            assert resp_pdf_404.status_code == 404

            resp_md_file_404 = await client.get(f"/api/v1/agent/report/{run_id}/markdown")
            assert resp_md_file_404.status_code == 404

        # Seed reports
        _reports[run_id] = "# Wearables Analysis\n\n- Apple\n- Garmin"

        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            # 1. JSON Report endpoint
            resp_md = await client.get(f"/api/v1/agent/report/{run_id}")
            assert resp_md.status_code == 200
            assert "markdown" in resp_md.json()
            assert "Wearables Analysis" in resp_md.json()["markdown"]

            # 2. PDF Download endpoint
            resp_pdf = await client.get(f"/api/v1/agent/report/{run_id}/pdf")
            assert resp_pdf.status_code == 200
            assert resp_pdf.headers["content-type"] == "application/pdf"
            assert "attachment" in resp_pdf.headers["content-disposition"]
            assert resp_pdf.headers["content-disposition"].endswith(".pdf")
            assert len(resp_pdf.content) > 0

            # 3. Markdown Download endpoint
            resp_md_file = await client.get(f"/api/v1/agent/report/{run_id}/markdown")
            assert resp_md_file.status_code == 200
            assert resp_md_file.headers["content-type"].startswith("text/markdown")
            assert "attachment" in resp_md_file.headers["content-disposition"]
            assert resp_md_file.headers["content-disposition"].endswith(".md")
            assert resp_md_file.text == _reports[run_id]
