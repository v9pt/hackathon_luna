import json
import logging

import chromadb
from langchain_core.tools import tool

from app.models.schemas import ToolResult

logger = logging.getLogger(__name__)

# Module-level ChromaDB client (in-process, ephemeral)
_chroma_client = chromadb.Client()


def _get_collection(run_id: str) -> chromadb.Collection:
    """Get or create a ChromaDB collection for this run."""
    safe_name = f"run_{run_id.replace('-', '_')}"
    return _chroma_client.get_or_create_collection(
        name=safe_name,
        metadata={"hnsw:space": "cosine"},
    )


@tool
async def store_memory(
    run_id: str, text: str, metadata: str = "{}"
) -> ToolResult:
    """Store a text chunk in vector memory for the current agent run.

    Args:
        run_id: Unique identifier for this research run.
        text: Text content to store (research findings, facts, quotes).
        metadata: JSON string of metadata, e.g.
                  ``'{"source": "web", "competitor": "Apple"}'``.

    Returns:
        ToolResult indicating success or failure.
    """
    try:
        collection = _get_collection(run_id)
        meta = json.loads(metadata) if metadata else {}
        if not meta:
            meta = {"source": "default"}
        doc_id = f"{run_id}-{collection.count()}"
        collection.add(documents=[text], metadatas=[meta], ids=[doc_id])
        return ToolResult(success=True, output=f"Stored document {doc_id}")
    except Exception as exc:
        logger.warning("store_memory failed: %s", exc)
        return ToolResult(success=False, output="", error=str(exc))


@tool
async def retrieve_memory(
    run_id: str, query: str, k: int = 5
) -> ToolResult:
    """Retrieve the *k* most semantically similar documents from memory.

    Args:
        run_id: Unique identifier for this research run.
        query: Query string to search for similar facts.
        k: Number of results to return (default 5).

    Returns:
        ToolResult with a JSON array of matching text chunks.
    """
    try:
        collection = _get_collection(run_id)
        if collection.count() == 0:
            return ToolResult(success=True, output="[]")
        results = collection.query(
            query_texts=[query], n_results=min(k, collection.count())
        )
        docs = results.get("documents", [[]])[0]
        return ToolResult(success=True, output=json.dumps(docs))
    except Exception as exc:
        logger.warning("retrieve_memory failed: %s", exc)
        return ToolResult(success=False, output="[]", error=str(exc))


async def add_facts(run_id: str, facts: list[str]) -> ToolResult:
    """Helper function to store multiple facts in vector memory."""
    try:
        collection = _get_collection(run_id)
        for i, fact in enumerate(facts):
            doc_id = f"{run_id}-{collection.count()}-{i}"
            collection.add(documents=[fact], metadatas=[{"source": "add_facts"}], ids=[doc_id])
        return ToolResult(success=True, output=f"Stored {len(facts)} facts")
    except Exception as exc:
        logger.warning("add_facts failed: %s", exc)
        return ToolResult(success=False, output="", error=str(exc))


async def query_facts(run_id: str, query: str, n_results: int = 5) -> ToolResult:
    """Helper function to query semantically similar facts from memory."""
    return await retrieve_memory.ainvoke({"run_id": run_id, "query": query, "k": n_results})

