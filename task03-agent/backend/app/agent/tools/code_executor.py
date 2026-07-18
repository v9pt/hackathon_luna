import base64
import io
import json
import logging
import os
import tempfile
import traceback
from contextlib import redirect_stdout
from typing import Any

import sys
from RestrictedPython import compile_restricted, safe_globals
from RestrictedPython.Guards import (
    guarded_iter_unpack_sequence,
    safe_builtins,
)
from RestrictedPython.PrintCollector import PrintCollector
from langchain_core.tools import tool

from app.models.schemas import ToolResult

logger = logging.getLogger(__name__)

_ALLOWED_MODULES = {
    "math",
    "statistics",
    "json",
    "matplotlib",
    "numpy",
    "matplotlib.pyplot",
}


class StdoutPrintCollector(PrintCollector):
    """Subclass of RestrictedPython's PrintCollector to redirect print statements to stdout."""
    def write(self, text: str) -> None:
        sys.stdout.write(text)


def _make_restricted_globals() -> dict[str, Any]:
    """Build a restricted globals dict with only whitelisted builtins."""
    restricted = safe_globals.copy()
    builtins = safe_builtins.copy()

    # Guards required by RestrictedPython for iteration / attribute access
    builtins["_getiter_"] = iter
    builtins["_getattr_"] = getattr
    builtins["_write_"] = lambda x: x
    builtins["_inplacevar_"] = lambda op, x, y: x  # noqa: ARG005
    builtins["_iter_unpack_sequence_"] = guarded_iter_unpack_sequence

    def _safe_import(name: str, *args: Any, **kwargs: Any) -> Any:
        base = name.split(".")[0]
        if base not in _ALLOWED_MODULES:
            raise ImportError(
                f"Module '{name}' is not allowed in code executor"
            )
        return __import__(name, *args, **kwargs)

    builtins["__import__"] = _safe_import
    restricted["__builtins__"] = builtins
    restricted["_print_"] = PrintCollector
    return restricted


@tool
async def code_executor(code: str) -> ToolResult:
    """Execute Python code in a safe sandbox.

    Allowed modules: ``math``, ``statistics``, ``json``, ``matplotlib``,
    ``numpy``.  To produce a chart call ``plt.savefig('chart.png')`` —
    the PNG will be returned as base64.

    Args:
        code: Valid Python code string.

    Returns:
        ToolResult with captured stdout.  If a chart was saved the output
        is JSON with ``stdout`` and ``chart_base64`` keys.
    """
    try:
        byte_code = compile_restricted(code, "<agent_code>", "exec")
    except SyntaxError as exc:
        return ToolResult(success=False, output="", error=f"Syntax error: {exc}")

    stdout_buf = io.StringIO()
    restricted_globals = _make_restricted_globals()
    restricted_globals["_print"] = PrintCollector()

    with tempfile.TemporaryDirectory() as tmpdir:
        orig_dir = os.getcwd()
        os.chdir(tmpdir)
        try:
            with redirect_stdout(stdout_buf):
                exec(byte_code, restricted_globals)  # noqa: S102
        except Exception:
            os.chdir(orig_dir)
            return ToolResult(
                success=False,
                output="",
                error=f"Runtime error: {traceback.format_exc(limit=5)}",
            )
        finally:
            if os.getcwd() != orig_dir:
                os.chdir(orig_dir)

        stdout_text = stdout_buf.getvalue()
        if "_print" in restricted_globals:
            stdout_text = stdout_text + restricted_globals["_print"]()

        # Check if a chart was produced
        chart_path = os.path.join(tmpdir, "chart.png")
        if os.path.exists(chart_path):
            with open(chart_path, "rb") as f:
                chart_b64 = base64.b64encode(f.read()).decode()
            output = json.dumps(
                {"stdout": stdout_text, "chart_base64": chart_b64}
            )
        else:
            output = stdout_text

    return ToolResult(success=True, output=output)
