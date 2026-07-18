import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import fitz  # PyMuPDF
import pytest

from app.agent.tools.code_executor import code_executor
from app.agent.tools.pdf_reader import pdf_reader
from app.agent.tools.vector_memory import (
    retrieve_memory,
    store_memory,
    add_facts,
    query_facts,
)
from app.agent.tools.web_search import web_search
from app.models.schemas import ToolResult


# ───────────────────────────── web_search ──────────────────────────────


class TestWebSearch:
    @pytest.mark.asyncio
    async def test_returns_tool_result_on_success(self) -> None:
        mock_response = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {
                                "text": "Apple Watch Series 9 features advanced health sensors..."
                            }
                        ]
                    },
                    "groundingMetadata": {
                        "groundingChunks": [
                            {
                                "web": {
                                    "uri": "https://apple.com/watch",
                                    "title": "Apple Watch",
                                }
                            }
                        ]
                    }
                }
            ]
        }

        with patch(
            "app.agent.tools.web_search._gemini_search",
            new=AsyncMock(return_value=mock_response),
        ):
            result = await web_search.ainvoke(
                {"query": "Apple Watch Series 9 health sensors"}
            )

        assert isinstance(result, ToolResult)
        assert result.success is True
        assert "Apple Watch" in result.output

    @pytest.mark.asyncio
    async def test_returns_failure_on_api_error(self) -> None:
        with patch(
            "app.agent.tools.web_search._gemini_search",
            new=AsyncMock(side_effect=Exception("API error")),
        ):
            result = await web_search.ainvoke({"query": "any query"})

        assert result.success is False
        assert result.error is not None


# ──────────────────────────── pdf_reader ───────────────────────────────


class TestPdfReader:
    @pytest.mark.asyncio
    async def test_extracts_text(self) -> None:
        doc = fitz.open()
        page = doc.new_page()
        page.insert_text((72, 72), "Hello from PDF page 1")
        pdf_bytes = doc.write()
        doc.close()

        mock_resp = AsyncMock()
        mock_resp.content = pdf_bytes
        mock_resp.raise_for_status = MagicMock()

        mock_client_instance = MagicMock()
        mock_client_instance.get = AsyncMock(return_value=mock_resp)

        with patch("app.agent.tools.pdf_reader.httpx.AsyncClient") as mock_cls:
            mock_cls.return_value.__aenter__ = AsyncMock(
                return_value=mock_client_instance
            )
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=False)

            result = await pdf_reader.ainvoke(
                {"url": "http://example.com/test.pdf"}
            )

        assert result.success is True
        assert "Hello from PDF" in result.output

    @pytest.mark.asyncio
    async def test_fails_on_bad_url(self) -> None:
        mock_resp = AsyncMock()
        mock_resp.raise_for_status = MagicMock(
            side_effect=Exception("404 Not Found")
        )

        mock_client_instance = MagicMock()
        mock_client_instance.get = AsyncMock(return_value=mock_resp)

        with patch("app.agent.tools.pdf_reader.httpx.AsyncClient") as mock_cls:
            mock_cls.return_value.__aenter__ = AsyncMock(
                return_value=mock_client_instance
            )
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=False)

            result = await pdf_reader.ainvoke(
                {"url": "http://example.com/missing.pdf"}
            )

        assert result.success is False
        assert result.error is not None


# ────────────────────────── code_executor ──────────────────────────────


class TestCodeExecutor:
    @pytest.mark.asyncio
    async def test_runs_simple_code(self) -> None:
        result = await code_executor.ainvoke(
            {"code": "result = 2 + 2\nprint(result)"}
        )
        assert result.success is True
        assert "4" in result.output

    @pytest.mark.asyncio
    async def test_catches_syntax_error(self) -> None:
        result = await code_executor.ainvoke({"code": "def broken(:"})
        assert result.success is False
        assert result.error is not None

    @pytest.mark.asyncio
    async def test_blocks_file_access(self) -> None:
        result = await code_executor.ainvoke(
            {"code": "open('/etc/passwd').read()"}
        )
        assert result.success is False


# ────────────────────────── vector_memory ──────────────────────────────


class TestVectorMemory:
    @pytest.fixture(autouse=True)
    def mock_chroma(self) -> None:
        class DummyEmbeddingFunction:
            def __call__(self, input: list[str]) -> list[list[float]]:
                return [[0.0] * 384 for _ in input]
        
        from app.agent.tools import vector_memory
        
        def mock_get_collection(run_id: str):
            safe_name = f"run_{run_id.replace('-', '_')}"
            return vector_memory._chroma_client.get_or_create_collection(
                name=safe_name,
                metadata={"hnsw:space": "cosine"},
                embedding_function=DummyEmbeddingFunction(),
            )
            
        with patch("app.agent.tools.vector_memory._get_collection", side_effect=mock_get_collection):
            yield

    @pytest.mark.asyncio
    async def test_store_and_retrieve(self) -> None:
        run_id = f"test_{uuid.uuid4().hex[:8]}"
        store_result = await store_memory.ainvoke(
            {
                "run_id": run_id,
                "text": "Apple Watch has advanced ECG sensor",
                "metadata": '{"source": "web"}',
            }
        )
        assert store_result.success is True

        retrieve_result = await retrieve_memory.ainvoke(
            {"run_id": run_id, "query": "Apple Watch ECG", "k": 1}
        )
        assert retrieve_result.success is True
        assert "Apple Watch" in retrieve_result.output

    @pytest.mark.asyncio
    async def test_returns_empty_on_unknown_run(self) -> None:
        result = await retrieve_memory.ainvoke(
            {"run_id": "nonexistent_run_id", "query": "anything", "k": 3}
        )
        assert result.success is True

    @pytest.mark.asyncio
    async def test_add_and_query_facts(self) -> None:
        run_id = f"test_{uuid.uuid4().hex[:8]}"
        facts = ["Fact 1: Wearables market is growing", "Fact 2: Apple is the leader"]
        store_result = await add_facts(run_id, facts)
        assert store_result.success is True

        query_result = await query_facts(run_id, "Apple leader", n_results=1)
        assert query_result.success is True
        assert "Apple is the leader" in query_result.output
