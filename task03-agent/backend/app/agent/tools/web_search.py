import asyncio
import logging
from typing import Any

import httpx
from langchain_core.tools import tool

from app.config import get_settings
from app.models.schemas import ToolResult

logger = logging.getLogger(__name__)

_MAX_RETRIES = 3


async def _gemini_search(query: str) -> dict[str, Any]:
    """Call Gemini REST API directly with google_search grounding enabled."""
    settings = get_settings()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{settings.gemini_model_name}:generateContent?key={settings.google_api_key if hasattr(settings, 'google_api_key') else settings.gemini_api_key}"
    
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": f"Search the web and summarize findings for: {query}"}]}],
        "tools": [{"google_search": {}}]
    }
    
    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(url, json=data, headers=headers)
        resp.raise_for_status()
        return resp.json()


@tool
async def web_search(query: str) -> ToolResult:
    """Search the web using Gemini's built-in Google Search grounding.

    Args:
        query: The search query string.

    Returns:
        ToolResult with grounded text and source URLs.
    """
    # Rate-limit delay before calling Gemini (free tier: 5 req/min)
    from app.config import get_settings as _get_settings
    delay = _get_settings().gemini_request_delay
    if delay > 0:
        await asyncio.sleep(delay)

    for attempt in range(_MAX_RETRIES):
        try:
            res = await _gemini_search(query)
            
            # Extract grounded text
            candidates = res.get("candidates", [])
            if not candidates:
                raise ValueError("No candidates returned from search endpoint")
                
            parts = candidates[0].get("content", {}).get("parts", [])
            content = parts[0].get("text", "") if parts else ""
            
            # Extract citation URLs if available
            urls: list[str] = []
            metadata = candidates[0].get("groundingMetadata", {})
            chunks = metadata.get("groundingChunks", [])
            for chunk in chunks:
                web = chunk.get("web", {})
                uri = web.get("uri")
                if uri:
                    urls.append(uri)

            output = content
            if urls:
                output += "\n\nSources:\n" + "\n".join(f"- {u}" for u in urls)

            return ToolResult(success=True, output=output)

        except Exception as exc:
            logger.warning("web_search attempt %d failed: %s", attempt + 1, exc)
            if attempt < _MAX_RETRIES - 1:
                # Use longer backoff for rate limits (429): 15s, 30s
                is_rate_limit = "429" in str(exc) or "quota" in str(exc).lower()
                backoff = (15 * (attempt + 1)) if is_rate_limit else (2 ** attempt)
                logger.info("web_search backing off %ds (rate_limit=%s)", backoff, is_rate_limit)
                await asyncio.sleep(backoff)

    return ToolResult(
        success=False,
        output="",
        error=f"web_search failed after {_MAX_RETRIES} retries",
    )

