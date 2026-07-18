# Hackathon Submission: Task 03 Autonomous Research Agent

This repository contains one completed assessment task: **Task 03 - Autonomous Multi-Tool AI Research Agent**.

The working project is in [`task03-agent/`](./task03-agent/).

## What Was Built

Task 03 is a full-stack autonomous research system that:

- Runs a multi-tool AI research agent for competitive intelligence.
- Streams reasoning, tool calls, tool results, errors, and cost telemetry live to a frontend dashboard.
- Recovers from individual tool failures without stopping the whole run.
- Tracks cumulative token usage and estimated/provider-reported spend throughout execution.
- Generates a structured Markdown report with charts.
- Exports the final report as Markdown or PDF.

## Technologies Used

- **Frontend:** React, TypeScript, Vite, CSS
- **Backend:** Python, FastAPI, Uvicorn
- **Agent Framework:** LangGraph, LangChain
- **Model Provider:** Google Gemini
- **Streaming:** Server-Sent Events
- **Memory:** ChromaDB vector memory
- **Charts:** Matplotlib
- **PDF Export:** ReportLab
- **Testing:** Pytest, Playwright, Oxlint

## Project Structure

```text
task03-agent/
  backend/
    app/
      agent/        # LangGraph workflow, tools, prompts, cost tracking
      api/          # FastAPI routes and SSE stream endpoint
      models/       # Pydantic schemas
      utils/        # PDF generation
    tests/          # Backend unit/integration tests
  frontend/
    src/            # React dashboard
    tests/          # Playwright E2E test
```

## Setup And Run

### Backend

```bash
cd task03-agent/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GEMINI_API_KEY="your-gemini-api-key"
python -m uvicorn app.main:create_app --factory --host 127.0.0.1 --port 8000 --reload
```

Backend health check:

```bash
curl http://127.0.0.1:8000/health
```

API docs:

```text
http://127.0.0.1:8000/docs
```

### Frontend

```bash
cd task03-agent/frontend
npm install
npm run dev
```

Frontend dashboard:

```text
http://localhost:3000
```

## Render Deployment

This repository is set up for a free Render deployment with two services:

1. Backend web service from `task03-agent/backend`
2. Frontend static site from `task03-agent/frontend`

Backend settings:
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- Python version: `python-3.11.9` via `task03-agent/backend/runtime.txt`
- Required env var: `GEMINI_API_KEY`
- Optional env var: `CORS_ORIGINS=https://your-frontend.onrender.com`

Frontend settings:
- Build command: `npm install && npm run build`
- Publish directory: `dist`
- Env var: `VITE_API_BASE_URL=https://your-backend.onrender.com`

The backend keeps localhost origins for development and can also accept Render-hosted frontend domains through CORS configuration.

## Verification

Backend tests:

```bash
cd task03-agent/backend
source .venv/bin/activate
PYTHONPATH=. pytest -v
```

Frontend checks:

```bash
cd task03-agent/frontend
npm run build
npm run lint
```

Playwright E2E:

```bash
cd task03-agent/frontend
npx playwright install
npx playwright test
```

## Submission Links

- GitHub repository: `https://github.com/v9pt/hackathon_luna`
- Code walkthrough video: add public video link here
- Live demo video: add public video link here

## Known Limitations

- Runs and reports are stored in process memory, so they are not persisted after backend restart.
- Live model calls require a valid Gemini API key and available quota.
- Cost telemetry uses provider token metadata when available and conservative token estimation while streaming.
- The frontend defaults to `localhost:8000`, but can point at Render via `VITE_API_BASE_URL`.
