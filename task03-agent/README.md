# Task 03: Autonomous Multi-Tool AI Research Agent - Verification & Usage Guide

This guide explains how to start, verify, and interact with the Autonomous Multi-Tool AI Research Agent.

The runtime now uses one main supervisor agent and four parallel subagents:

- Web search scout
- PDF reader scout
- Python chart analyst
- Vector memory curator

The backend executes independent tool calls in parallel, so the SSE stream shows concurrent research, extraction, analysis, and memory updates.

---

## ⚡ Quick Start: Running the Application

To run the complete system, you must start both the backend server and the frontend dashboard.

### 1. Start the Backend API (FastAPI)
Navigate to the backend directory, activate the virtual environment, and launch the Uvicorn server:
```bash
cd task03-agent/backend
source .venv/bin/activate
# Make sure your Gemini API key is configured in your shell environment or .env file
export GEMINI_API_KEY="your-gemini-api-key"
# Start the Uvicorn server on port 8000
python -m uvicorn app.main:create_app --factory --host 127.0.0.1 --port 8000 --reload
```
*The API docs will be available at: http://127.0.0.1:8000/docs*

### 2. Start the Frontend Dashboard (React + Vite)
Open a new terminal session, navigate to the frontend directory, install dependencies, and start the Vite dev server:
```bash
cd task03-agent/frontend
npm install
npm run dev
```
*The React Dashboard will be available at: http://localhost:3000*

---

## 🧪 Running Automated Verification Tests

### 1. Run Backend Unit & Integration Tests (Pytest)
Ensure you are in the `task03-agent/backend` directory with the virtual environment activated:
```bash
cd task03-agent/backend
source .venv/bin/activate
PYTHONPATH=. pytest -v
```
This runs all 33 unit and integration tests covering:
- Configuration and environment settings (`test_config.py`)
- SSE event emitters and cost calculators (`test_cost_tracker.py` & `test_routes.py`)
- Individual agent tools: web search, PDF parser, restricted python sandbox code executor, and ChromaDB vector store (`test_tools.py`)
- PDF report styling and generator (`test_pdf_generator.py`)
- Full ReAct Agent loop, budget enforcement gates, and iteration limits (`test_agent.py`)

### 2. Run Frontend E2E & Visual Tests (Playwright)
Navigate to the frontend directory and execute the E2E verification specs:
```bash
cd task03-agent/frontend
npx playwright install
npx playwright test
```
This tests the full E2E flow including inputs, budget slider adjustments, SSE stream terminal lines rendering, base64 chart cards rendering, and report download triggers.

---

## 🔍 Manual API Verification (Using curl)

If you wish to test the APIs directly, you can run these command line checks:

### 1. Check API Health
```bash
curl -X GET http://127.0.0.1:8000/api/v1/agent/health
# Expected output: {"status":"healthy"}
```

### 2. Trigger a Research Agent Run
```bash
curl -X POST http://127.0.0.1:8000/api/v1/agent/run \
  -H "Content-Type: application/json" \
  -d '{"topic": "top 3 competitors in smartwatch segment", "max_cost_usd": 1.0}'
# Expected output: {"success":true,"run_id":"run-xxx-xxx","message":"Research run started successfully."}
```

### 3. Stream Live Reasoning Events (Replace <run_id> with the id returned above)
```bash
curl -X GET http://127.0.0.1:8000/api/v1/agent/stream/<run_id>
# This will stream SSE event packets (e.g. data: {"type": "reasoning", "data": {...}}) in real-time.
```
