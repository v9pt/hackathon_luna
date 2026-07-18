"""FastAPI application factory."""

import os
os.environ["ANONYMIZED_TELEMETRY"] = "False"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import router


def _get_cors_origins() -> list[str]:
    """Return allowed CORS origins for local development and Render."""
    origins = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]

    configured_origins = os.getenv("CORS_ORIGINS", "")
    if configured_origins:
        origins.extend(
            origin.strip() for origin in configured_origins.split(",") if origin.strip()
        )

    frontend_origin = os.getenv("FRONTEND_ORIGIN", "").strip()
    if frontend_origin:
        origins.append(frontend_origin)

    return list(dict.fromkeys(origins))


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Autonomous Research Agent",
        description="Multi-tool AI research agent with real-time SSE streaming",
        version="1.0.0",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=_get_cors_origins(),
        allow_origin_regex=r"https://.*\.onrender\.com",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router)

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
