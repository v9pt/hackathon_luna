"""FastAPI routes — POST /run, GET /stream/{id}, GET /report/{id}[/pdf]."""

import asyncio
import io
import uuid
from typing import AsyncGenerator

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response, StreamingResponse

from app.agent.graph import run_agent
from app.models.schemas import AgentRunRequest, SSEEvent

router = APIRouter(prefix="/api/v1")

# In-memory stores (single-process; fine for demo / assessment)
_reports: dict[str, str] = {}
_runs: dict[str, AgentRunRequest] = {}


@router.post("/agent/run")
async def start_run(body: AgentRunRequest) -> dict[str, str]:
    """Create a new agent run and return its ``run_id``."""
    run_id = str(uuid.uuid4())
    _runs[run_id] = body
    return {"run_id": run_id}


async def _event_stream(run_id: str) -> AsyncGenerator[str, None]:
    request = _runs.get(run_id)
    if not request:
        yield SSEEvent(
            type="error",
            data={"message": "run_id not found"},
            run_id=run_id,
        ).to_sse_line()
        return

    async for event in run_agent(run_id, request.topic, request.max_cost_usd):
        if event.type == "report":
            _reports[run_id] = event.data.get("markdown", "")
        yield event.to_sse_line()
        await asyncio.sleep(0)  # Yield control for true streaming


@router.get("/agent/stream/{run_id}")
async def stream_run(run_id: str) -> StreamingResponse:
    """SSE endpoint — streams reasoning, tool calls, cost, and report."""
    return StreamingResponse(
        _event_stream(run_id),
        media_type="text/event-stream",
        headers={
            "X-Accel-Buffering": "no",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )


@router.get("/agent/report/{run_id}")
async def get_report(run_id: str) -> dict[str, str]:
    """Return the finished Markdown report."""
    markdown = _reports.get(run_id)
    if markdown is None:
        raise HTTPException(
            status_code=404, detail="Report not found or run not complete"
        )
    return {"markdown": markdown}


@router.get("/agent/report/{run_id}/pdf")
async def get_report_pdf(run_id: str) -> Response:
    """Return the finished report as a downloadable PDF."""
    markdown = _reports.get(run_id)
    if markdown is None:
        raise HTTPException(status_code=404, detail="Report not found")

    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story: list = []
    for line in markdown.split("\n"):
        if line.startswith("# "):
            story.append(Paragraph(line[2:], styles["h1"]))
        elif line.startswith("## "):
            story.append(Paragraph(line[3:], styles["h2"]))
        elif line.strip():
            story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 6))
    doc.build(story)

    return Response(
        content=buffer.getvalue(),
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=report-{run_id[:8]}.pdf"
        },
    )


@router.get("/agent/report/{run_id}/markdown")
async def get_report_markdown(run_id: str) -> Response:
    """Return the finished report as a downloadable Markdown file."""
    markdown = _reports.get(run_id)
    if markdown is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return Response(
        content=markdown,
        media_type="text/markdown",
        headers={
            "Content-Disposition": f"attachment; filename=report-{run_id[:8]}.md"
        },
    )

