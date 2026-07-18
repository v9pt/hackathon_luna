# Design Spec: Autonomous Multi-Tool AI Research Agent Dashboard
Date: 2026-07-18

## 1. Overview
The Frontend React Dashboard provides a responsive, dark-themed user interface to interact with the Autonomous Research Agent backend. It allows users to start research runs, configure parameters (topic and budget limit), monitor real-time reasoning and tool execution logs via Server-Sent Events (SSE), track token-based costs, visualize comparisons, and download generated reports in PDF or Markdown formats.

---

## 2. UI Layout & Component Hierarchy

We propose a modern single-page dashboard featuring a dark slate palette (`bg-slate-950`, `text-slate-100`, with vibrant emerald/indigo accents).

```
+---------------------------------------------------------------------------------+
|  [Logo] Autonomous Research Agent Dashboard              [Status: Running...]   |
+---------------------------------------------------------------------------------+
|                                       |                                         |
|  LEFT PANEL: CONTROLS & COST          |  RIGHT PANEL: LIVE MONITOR              |
|                                       |                                         |
|  +---------------------------------+  |  +-----------------------------------+  |
|  | Topic Input                     |  |  | Live Terminal Logs                |  |
|  | [ Enter research topic...     ] |  |  | - [tool_call] search: "competitor"|  |
|  |                                 |  |  | - [reasoning] analyzing results...|  |
|  | Budget Slider ($0.1 - $5.0)     |  |  | - [tool_result] (collapsible)     |  |
|  | [--O---------------------] $1.0 |  |  |                                   |  |
|  |                                 |  |  |                                   |  |
|  | [ Start Research ]              |  |  |                                   |  |
|  +---------------------------------+  |  +-----------------------------------+  |
|                                       |                                         |
|  +---------------------------------+  |  +-----------------------------------+  |
|  | Budget & Cost Progress          |  |  | Export Options                    |  |
|  | Cost: $0.15 / $1.00 [======   ]  |  |  | [ Download MD ]  [ Download PDF ]  |
|  | Tokens: 12.5k In / 8.2k Out     |  |  +-----------------------------------+  |
|  +---------------------------------+  |                                         |
|                                       |                                         |
+---------------------------------------------------------------------------------+
|                                                                                 |
|  BOTTOM PANEL: RESULTS VIEW                                                     |
|  +---------------------------------------------------------------------------+  |
|  | Markdown Report (Live Rendered)                                           |  |
|  | # Wearable Technology Analysis...                                         |  |
|  | - Competitor A holds 30% market share.                                    |  |
|  |                                                                           |  |
|  | [ Market Share Comparison Chart (Base64 Rendered Image/Chart) ]            |  |
|  +---------------------------------------------------------------------------+  |
+---------------------------------------------------------------------------------+
```

### Main Sections
1. **Header Component**:
   - Title and brief description.
   - Run Status Badge: `Idle` (gray), `Running` (amber/pulsing), `Completed` (emerald), `Error` (red).
   - *ID*: `status-badge`
2. **Control Panel Component**:
   - Topic input text area. *ID*: `topic-input`
   - Budget slider ($0.1 to $5.0, default $1.0). *ID*: `budget-slider`
   - Start button. *ID*: `start-btn`
3. **Live Monitor Component**:
   - Real-time terminal with auto-scroll and interactive filters (show/hide reasoning, tool calls, results). *ID*: `terminal-logs`
   - Individual log blocks styled by type:
     - `reasoning`: Italicized text with a brain icon.
     - `tool_call`: Yellow alert box showing `tool` name and arguments.
     - `tool_result`: Collapsible green/gray terminal block. *ID*: `tool-result-<index>`
     - `error`: Red alert box with exception details.
4. **Budget & Cost Tracker**:
   - Dynamic progress bar showing cumulative cost against the budget. *ID*: `cost-progress-bar`
   - Value display for `input_tokens`, `output_tokens`, `total_usd`, `cumulative_usd`. *ID*: `cost-stats`
5. **Results Pane**:
   - Markdown viewer showing the final report. *ID*: `report-markdown`
   - Image gallery rendering base64 comparison charts sent via the `report` event. *ID*: `report-charts`
6. **Export Action Buttons**:
   - Download Markdown. *ID*: `export-md-btn`
   - Download PDF. *ID*: `export-pdf-btn`

---

## 3. Data Flow & SSE Streaming

1. **Trigger Run**:
   - User inputs a topic and sets a max cost budget.
   - User clicks `Start Research`.
   - Frontend issues a `POST` request to `http://localhost:8000/api/v1/agent/run` with the payload:
     ```json
     {
       "topic": "topic_value",
       "max_cost_usd": budget_value
     }
     ```
   - On success, retrieve `run_id`.
   - Update UI status to `Running`. Clear previous logs, cost, and report state.

2. **Establish SSE Stream**:
   - Instantiate `new EventSource("http://localhost:8000/api/v1/agent/stream/" + run_id)`.
   - Listen for message events:
     ```javascript
     eventSource.onmessage = (event) => {
       const sseEvent = JSON.parse(event.data);
       handleEvent(sseEvent);
     }
     ```
   - **Event Handlers**:
     - `reasoning`: Append text to logs state.
     - `tool_call`: Append tool execution info to logs state.
     - `tool_result`: Append results to logs state (collapsible).
     - `cost`: Update cost and token progress state.
     - `report`: Update markdown content state and extract base64 charts.
     - `error`: Display error log and transition status badge to `Error`. Close SSE stream.
     - `done`: Update run status to `Completed`. Enable PDF/Markdown export. Close SSE stream.
   - **SSE Error Handling**:
     - If the EventSource fires an error before a `done` or `error` message is received, attempt a retry once or show a connection warning.

3. **Export Reports**:
   - Clicking `Download Markdown` calls the local file download with the markdown state.
   - Clicking `Download PDF` triggers a GET request to `http://localhost:8000/api/v1/agent/report/{run_id}/pdf` and downloads the response as a PDF blob.

---

## 4. Technical Stack

- **Framework**: React 18+ with TypeScript
- **Build Tool**: Vite (creates fast dev and optimized production builds)
- **Styling**: TailwindCSS (responsive layouts, dark mode utility classes)
- **Icons**: `lucide-react` (icons for tools, brain, cost, export, etc.)
- **Markdown Rendering**: Custom styled parser or lightweight library.
- **Charts Rendering**: Render the `charts` list containing name & base64 images directly inside a CSS grid layout, allowing direct view of high-fidelity matplotlib charts generated by the backend.

---

## 5. Verification Plan

1. **Unit & Build Tests**:
   - Verify Vite compilation passes (`npm run build`).
   - Run typechecking (`tsc --noEmit`).
2. **Interactive Elements Verification**:
   - Verify all buttons, inputs, sliders, and panels have exact matching `id` tags.
3. **E2E flow test**:
   - Trigger mock run, ensure logs stream, cost updates, and download buttons trigger correct browser actions.
