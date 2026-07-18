import logging
from typing import Optional

import fitz  # PyMuPDF
import httpx
from langchain_core.tools import tool

from app.models.schemas import ToolResult

logger = logging.getLogger(__name__)


@tool
async def pdf_reader(url: str, page_range: Optional[str] = None) -> ToolResult:
    """Download a PDF from a URL and extract its text content.

    Args:
        url: Direct URL to a PDF file.
        page_range: Optional page range like ``"1-3"`` (1-indexed, inclusive).
                    If omitted, all pages are extracted.

    Returns:
        ToolResult with extracted text.  On failure, ``success=False``
        with an error message.
    """
    try:
        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
            resp = await client.get(url)
            resp.raise_for_status()
            pdf_bytes = resp.content

        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        start_page, end_page = 0, len(doc) - 1
        if page_range:
            parts = page_range.split("-")
            start_page = max(0, int(parts[0]) - 1)
            end_page = (
                min(len(doc) - 1, int(parts[1]) - 1)
                if len(parts) > 1
                else start_page
            )

        pages_text: list[str] = []
        for page_num in range(start_page, end_page + 1):
            page = doc[page_num]
            pages_text.append(f"[Page {page_num + 1}]\n{page.get_text()}")

        doc.close()
        return ToolResult(success=True, output="\n\n".join(pages_text))

    except Exception as exc:
        logger.warning("pdf_reader failed for %s: %s", url, exc)
        return ToolResult(success=False, output="", error=f"PDF read failed: {exc}")
