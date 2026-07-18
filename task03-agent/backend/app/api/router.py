import asyncio
import logging
import uuid
from typing import Any, AsyncGenerator, Dict

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response, StreamingResponse

from app.agent.graph import run_agent
from app.models.schemas import AgentRunRequest, SSEEvent
from app.utils.pdf_generator import generate_pdf

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1")

# In-memory stores (single-process; fine for assessment/demo)
_reports: Dict[str, str] = {}
_runs: Dict[str, AgentRunRequest] = {}


@router.post("/agent/run")
async def start_run(body: AgentRunRequest) -> Dict[str, Any]:
    """Create a new agent run, validate input, and return the run details."""
    try:
        if not body.topic or not body.topic.strip():
            raise HTTPException(status_code=400, detail="Topic cannot be empty")
        
        run_id = str(uuid.uuid4())
        _runs[run_id] = body
        logger.info("Started run %s for topic: %s", run_id, body.topic)
        return {
            "success": True,
            "run_id": run_id,
            "message": "Research run started successfully.",
        }
    except Exception as exc:
        logger.error("Failed to start run: %s", exc)
        if isinstance(exc, HTTPException):
            raise exc
        raise HTTPException(status_code=500, detail=f"Failed to start run: {str(exc)}")


async def _event_stream(run_id: str) -> AsyncGenerator[str, None]:
    request = _runs.get(run_id)
    if not request:
        yield SSEEvent(
            type="error",
            data={"message": f"Run ID {run_id} not found"},
            run_id=run_id,
        ).to_sse_line()
        return

    try:
        async for event in run_agent(run_id, request.topic, request.max_cost_usd):
            if event.type == "report":
                _reports[run_id] = event.data.get("markdown", "")
            yield event.to_sse_line()
            await asyncio.sleep(0)  # Yield control for async streaming
    except Exception as exc:
        logger.error("Error in stream for run %s: %s", run_id, exc)
        yield SSEEvent(
            type="error",
            data={"message": f"Stream error: {str(exc)}"},
            run_id=run_id,
        ).to_sse_line()


@router.get("/agent/stream/{run_id}")
async def stream_run(run_id: str) -> StreamingResponse:
    """SSE endpoint — streams reasoning, tool calls, cost, and report."""
    if run_id not in _runs:
        raise HTTPException(status_code=404, detail=f"Run {run_id} not found")
        
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
async def get_report(run_id: str) -> Dict[str, str]:
    """Return the finished Markdown report as JSON."""
    markdown = _reports.get(run_id)
    if markdown is None:
        raise HTTPException(
            status_code=404, detail="Report not found or run not complete"
        )
    return {"markdown": markdown}


@router.get("/agent/report/{run_id}/markdown")
async def get_report_markdown(run_id: str) -> Response:
    """Return the finished report as a downloadable Markdown file."""
    markdown = _reports.get(run_id)
    if markdown is None:
        raise HTTPException(
            status_code=404, detail="Report not found or run not complete"
        )
    return Response(
        content=markdown,
        media_type="text/markdown",
        headers={
            "Content-Disposition": f"attachment; filename=report-{run_id[:8]}.md"
        },
    )


@router.get("/agent/report/{run_id}/pdf")
async def get_report_pdf(run_id: str) -> Response:
    """Return the finished report as a downloadable PDF."""
    markdown = _reports.get(run_id)
    if markdown is None:
        raise HTTPException(
            status_code=404, detail="Report not found or run not complete"
        )
    
    try:
        pdf_data = generate_pdf(markdown)
        return Response(
            content=pdf_data,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f"attachment; filename=report-{run_id[:8]}.pdf"
            },
        )
    except Exception as exc:
        logger.error("Failed to generate PDF for run %s: %s", run_id, exc)
        raise HTTPException(status_code=500, detail=f"PDF generation failed: {str(exc)}")
