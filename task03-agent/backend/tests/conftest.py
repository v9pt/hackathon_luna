import pytest
from unittest.mock import MagicMock, patch

from app.models.schemas import CostSnapshot, ToolResult


@pytest.fixture(autouse=True)
def mock_chroma_embeddings():
    with patch("chromadb.utils.embedding_functions.ONNXMiniLM_L6_V2") as mock_class:
        mock_instance = MagicMock()
        mock_instance.side_effect = lambda texts: [[0.1] * 384 for _ in texts]
        mock_class.return_value = mock_instance
        yield mock_instance


@pytest.fixture
def ok_tool_result() -> ToolResult:
    return ToolResult(success=True, output="sample output")


@pytest.fixture
def fail_tool_result() -> ToolResult:
    return ToolResult(success=False, output="", error="connection refused")


@pytest.fixture
def cost_snapshot() -> CostSnapshot:
    return CostSnapshot(
        input_tokens=100,
        output_tokens=50,
        total_tokens=150,
        total_usd=0.00002,
    )

