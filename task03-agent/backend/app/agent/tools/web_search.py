import asyncio
import logging
from typing import Any

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import get_settings
from app.models.schemas import ToolResult

logger = logging.getLogger(__name__)

_GOOGLE_SEARCH_TOOL = {"google_search": {}}
_MAX_RETRIES = 3


async def _gemini_search(query: str) -> Any:
    """Call Gemini with google_search grounding enabled."""
    settings = get_settings()
    llm = ChatGoogleGenerativeAI(
        model=settings.gemini_model_name,
        google_api_key=settings.gemini_api_key,
    )
    llm_with_search = llm.bind_tools([_GOOGLE_SEARCH_TOOL])
    return await llm_with_search.ainvoke(
        f"Search the web and summarize findings for: {query}"
    )


@tool
async def web_search(query: str) -> ToolResult:
    """Search the web using Gemini's built-in Google Search grounding.

    Args:
        query: The search query string.

    Returns:
        ToolResult with grounded text and source URLs.
    """
    for attempt in range(_MAX_RETRIES):
        try:
            response = await _gemini_search(query)
            # Extract grounded text
            content = (
                response.content if hasattr(response, "content") else str(response)
            )
            # Extract citation URLs if available
            urls: list[str] = []
            try:
                chunks = (
                    response.candidates[0].grounding_metadata.grounding_chunks
                )
                urls = [c.web.uri for c in chunks if hasattr(c, "web")]
            except (AttributeError, IndexError):
                pass

            output = content
            if urls:
                output += "\n\nSources:\n" + "\n".join(f"- {u}" for u in urls)

            return ToolResult(success=True, output=output)

        except Exception as exc:
            logger.warning("web_search attempt %d failed: %s", attempt + 1, exc)
            if attempt < _MAX_RETRIES - 1:
                await asyncio.sleep(2**attempt)

    return ToolResult(
        success=False,
        output="",
        error=f"web_search failed after {_MAX_RETRIES} retries",
    )
