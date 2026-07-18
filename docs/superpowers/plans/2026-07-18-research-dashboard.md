# Autonomous Research Agent Dashboard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the frontend React/Vite/TS dashboard for the Autonomous Research Agent under `task03-agent/frontend/` that triggers research runs, streams reasoning logs, displays cost progress, renders markdown reports with base64 charts, and supports downloading exports.

**Architecture:** A single-page dashboard with Tailwind CSS. State is managed locally using React hooks. Real-time updates are pushed via an `EventSource` (SSE) stream, updating terminal logs, cost progress, and results asynchronously.

**Tech Stack:** React 18+, Vite, TypeScript, TailwindCSS, Lucide-react (icons).

## Global Constraints
- Target directory: `/Users/zaif/Desktop/NEW/task03-agent/frontend/`
- Target backend URL: `http://localhost:8000` (FastAPI backend)
- Theme: Dark-themed responsive dashboard using slate/gray Tailwind classes.
- Playwright Interactive element IDs must match:
  - `topic-input`: Text input/area for the topic.
  - `budget-slider`: Range slider for budget.
  - `start-btn`: Trigger research button.
  - `terminal-logs`: Terminal container.
  - `cost-progress-bar`: Cost tracker progress bar container.
  - `cost-stats`: Text container showing numeric costs.
  - `report-markdown`: Markdown rendering container.
  - `report-charts`: Chart gallery container.
  - `export-md-btn`: Markdown download button.
  - `export-pdf-btn`: PDF download button.
  - `status-badge`: Run status display.

---

## Tasks

### Task 1: Initialize Project & Setup Scaffolding

**Files:**
- Create: `task03-agent/frontend/` (via Vite initialization)
- Modify: `task03-agent/frontend/package.json`, `task03-agent/frontend/vite.config.ts`, `task03-agent/frontend/tailwind.config.js`

**Interfaces:**
- Consumes: None
- Produces: Base Vite + React + TS build pipeline with Tailwind CSS ready.

- [ ] **Step 1: Scaffold React TS Vite project**
  Run: `npx -y create-vite@latest frontend --template react-ts` from directory `/Users/zaif/Desktop/NEW/task03-agent/`
  Expected: Scaffolds Vite project under `task03-agent/frontend/`.

- [ ] **Step 2: Install dependencies**
  Run: `npm install -D tailwindcss postcss autoprefixer && npx tailwindcss init -p && npm install lucide-react` from `task03-agent/frontend/`
  Expected: Installs Tailwind CSS and Lucide icons.

- [ ] **Step 3: Configure Tailwind CSS**
  Update `tailwind.config.js` with content:
  ```javascript
  /** @type {import('tailwindcss').Config} */
  export default {
    content: [
      "./index.html",
      "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
      extend: {},
    },
    plugins: [],
  }
  ```

- [ ] **Step 4: Update global styles**
  Replace `src/index.css` content with Tailwind directives:
  ```css
  @tailwind base;
  @tailwind components;
  @tailwind utilities;

  body {
    background-color: #020617; /* bg-slate-950 */
    color: #f8fafc; /* text-slate-50 */
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
  }
  ```

- [ ] **Step 5: Verify build works**
  Run: `npm run build` inside `task03-agent/frontend/`
  Expected: Compile successfully.

- [ ] **Step 6: Commit**
  Run: `git add . && git commit -m "feat: initialize frontend project scaffolding with tailwind"`

---

### Task 2: Core Components & State Design

**Files:**
- Modify: `task03-agent/frontend/src/App.tsx`
- Create: `task03-agent/frontend/src/types.ts`

**Interfaces:**
- Consumes: Initial setup
- Produces: Type structures for SSEEvents and layout shell.

- [ ] **Step 1: Create type definitions**
  Create `task03-agent/frontend/src/types.ts` with following content:
  ```typescript
  export type RunStatus = 'idle' | 'running' | 'completed' | 'error';

  export interface SSEEvent {
    type: 'reasoning' | 'tool_call' | 'tool_result' | 'cost' | 'report' | 'error' | 'done';
    data: any;
    run_id: string;
  }

  export interface CostSnapshot {
    input_tokens: number;
    output_tokens: number;
    total_tokens: number;
    total_usd: number;
    cumulative_usd: number;
  }

  export interface ChartItem {
    name: string;
    base64: string;
  }
  ```

- [ ] **Step 2: Construct basic dashboard UI shell in App.tsx**
  Replace `task03-agent/frontend/src/App.tsx` with code setting up state hook variables:
  ```tsx
  import React, { useState } from 'react';
  import { Play, Shield, Terminal, DollarSign, Download, AlertTriangle, CheckCircle, HelpCircle } from 'lucide-react';
  import { RunStatus, SSEEvent, CostSnapshot, ChartItem } from './types';

  export default function App() {
    const [topic, setTopic] = useState("wearable technology competitive landscape top 5 competitors");
    const [budget, setBudget] = useState(1.0);
    const [runId, setRunId] = useState<string | null>(null);
    const [status, setStatus] = useState<RunStatus>('idle');
    const [logs, setLogs] = useState<SSEEvent[]>([]);
    const [cost, setCost] = useState<CostSnapshot>({ input_tokens: 0, output_tokens: 0, total_tokens: 0, total_usd: 0, cumulative_usd: 0 });
    const [reportMarkdown, setReportMarkdown] = useState<string>("");
    const [charts, setCharts] = useState<ChartItem[]>([]);
    const [errorMsg, setErrorMsg] = useState<string>("");

    return (
      <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
        <header className="border-b border-slate-800 bg-slate-900/50 backdrop-blur px-6 py-4 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center font-bold text-lg">A</div>
            <h1 className="text-xl font-bold tracking-tight">Autonomous Research Agent</h1>
          </div>
          <div>
            <span id="status-badge" className={`px-3 py-1.5 rounded-full text-xs font-semibold uppercase tracking-wider ${
              status === 'idle' ? 'bg-slate-800 text-slate-400' :
              status === 'running' ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30 animate-pulse' :
              status === 'completed' ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' :
              'bg-red-500/20 text-red-400 border border-red-500/30'
            }`}>
              {status}
            </span>
          </div>
        </header>
        {/* Skeleton content layout to be filled in subsequent steps */}
        <main className="flex-1 p-6 grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="space-y-6">
             {/* Left Column content: Control Panel & Budget Progress */}
          </div>
          <div className="space-y-6 flex flex-col">
             {/* Right Column: Terminal Logs & Outputs */}
          </div>
        </main>
      </div>
    );
  }
  ```

- [ ] **Step 3: Compile and verify**
  Run: `npm run build` in `task03-agent/frontend/`
  Expected: Builds without errors.

- [ ] **Step 4: Commit**
  Run: `git add . && git commit -m "feat: design types and basic shell layout in App.tsx"`

---

### Task 3: API Integration & EventSource Log Stream

**Files:**
- Modify: `task03-agent/frontend/src/App.tsx`

**Interfaces:**
- Consumes: Backend REST and SSE Endpoints (POST `/api/v1/agent/run`, GET `/api/v1/agent/stream/{run_id}`)
- Produces: Functioning triggers and real-time log ingestion.

- [ ] **Step 1: Add run triggers and SSE listener in App.tsx**
  Implement the full state updater logic.
  Code update details:
  ```typescript
  const startResearch = async () => {
    if (!topic.trim()) return;
    setStatus('running');
    setLogs([]);
    setReportMarkdown("");
    setCharts([]);
    setErrorMsg("");
    setCost({ input_tokens: 0, output_tokens: 0, total_tokens: 0, total_usd: 0, cumulative_usd: 0 });

    try {
      const res = await fetch("http://localhost:8000/api/v1/agent/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic, max_cost_usd: budget })
      });
      if (!res.ok) throw new Error("Failed to start run");
      const data = await res.json();
      setRunId(data.run_id);
      connectSSE(data.run_id);
    } catch (e: any) {
      setStatus('error');
      setErrorMsg(e.message || "Request failed");
    }
  };

  const connectSSE = (id: string) => {
    const eventSource = new EventSource(`http://localhost:8000/api/v1/agent/stream/${id}`);
    
    eventSource.onmessage = (event) => {
      try {
        const payload: SSEEvent = JSON.parse(event.data);
        setLogs(prev => [...prev, payload]);

        if (payload.type === 'cost') {
          setCost(payload.data);
        } else if (payload.type === 'report') {
          if (payload.data.markdown) setReportMarkdown(payload.data.markdown);
          if (payload.data.charts) setCharts(payload.data.charts);
        } else if (payload.type === 'error') {
          setStatus('error');
          setErrorMsg(payload.data.message || 'An error occurred');
          eventSource.close();
        } else if (payload.type === 'done') {
          setStatus('completed');
          eventSource.close();
        }
      } catch (err) {
        console.error("Failed to parse event", err);
      }
    };

    eventSource.onerror = (err) => {
      console.error("SSE error", err);
      eventSource.close();
      setStatus(prev => prev === 'running' ? 'error' : prev);
    };
  };
  ```

- [ ] **Step 2: Add full Control Panel UI in App.tsx**
  Ensure elements have correct IDs:
  ```tsx
  {/* Control Panel */}
  <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 space-y-4">
    <h2 className="text-lg font-semibold flex items-center gap-2"><Play className="w-5 h-5 text-indigo-500" /> Research Settings</h2>
    <div className="space-y-2">
      <label className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Research Topic</label>
      <textarea
        id="topic-input"
        rows={3}
        className="w-full bg-slate-950 border border-slate-800 rounded-lg p-3 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 text-slate-100"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        disabled={status === 'running'}
      />
    </div>
    <div className="space-y-2">
      <div className="flex justify-between items-center">
        <label className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Max Cost Budget</label>
        <span className="text-sm font-semibold text-indigo-400">${budget.toFixed(2)}</span>
      </div>
      <input
        id="budget-slider"
        type="range"
        min="0.1"
        max="5.0"
        step="0.1"
        className="w-full h-1 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-indigo-500"
        value={budget}
        onChange={(e) => setBudget(parseFloat(e.target.value))}
        disabled={status === 'running'}
      />
    </div>
    <button
      id="start-btn"
      onClick={startResearch}
      disabled={status === 'running'}
      className="w-full bg-indigo-600 hover:bg-indigo-700 disabled:bg-slate-800 disabled:text-slate-500 text-white font-semibold py-2.5 rounded-lg transition-colors flex items-center justify-center gap-2"
    >
      {status === 'running' ? 'Researching...' : 'Start Research'}
    </button>
  </div>
  ```

- [ ] **Step 3: Compile check**
  Run: `npm run build` inside `task03-agent/frontend/`
  Expected: Builds correctly.

- [ ] **Step 4: Commit**
  Run: `git add . && git commit -m "feat: implement SSE client connections and settings panel UI"`

---

### Task 4: Real-time Terminal Log Display & Progress Tracker

**Files:**
- Modify: `task03-agent/frontend/src/App.tsx`

**Interfaces:**
- Consumes: `logs` and `cost` states.
- Produces: Collapsible tool results and budget meters.

- [ ] **Step 1: Add Budget & Cost progress UI**
  Make progress bar reflect `cumulative_usd` vs `max_cost_usd`:
  ```tsx
  {/* Cost Progress */}
  <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 space-y-4">
    <h2 className="text-lg font-semibold flex items-center gap-2"><DollarSign className="w-5 h-5 text-emerald-500" /> Usage & Budget</h2>
    <div className="space-y-2">
      <div className="flex justify-between text-sm">
        <span className="text-slate-400">Total Spent</span>
        <span className="font-semibold text-emerald-400">${cost.cumulative_usd ? cost.cumulative_usd.toFixed(5) : cost.total_usd.toFixed(5)} / ${budget.toFixed(2)}</span>
      </div>
      <div id="cost-progress-bar" className="w-full bg-slate-950 h-3 rounded-full overflow-hidden border border-slate-800">
        <div 
          className="bg-emerald-500 h-full rounded-full transition-all duration-300"
          style={{ width: `${Math.min(100, ((cost.cumulative_usd || cost.total_usd) / budget) * 100)}%` }}
        />
      </div>
    </div>
    <div id="cost-stats" className="grid grid-cols-2 gap-4 pt-2">
      <div className="bg-slate-950 p-3 rounded-lg border border-slate-800/50">
        <span className="text-xs text-slate-500 block uppercase">Input Tokens</span>
        <span className="text-base font-bold">{cost.input_tokens.toLocaleString()}</span>
      </div>
      <div className="bg-slate-950 p-3 rounded-lg border border-slate-800/50">
        <span className="text-xs text-slate-500 block uppercase">Output Tokens</span>
        <span className="text-base font-bold">{cost.output_tokens.toLocaleString()}</span>
      </div>
    </div>
  </div>
  ```

- [ ] **Step 2: Add Live Terminal View**
  Ensure it handles collapsible logs for `tool_result` events.
  Add helper sub-component inside `App.tsx` or inline. Let's create an inline collapsible wrapper for tool results:
  ```tsx
  const CollapsibleToolResult = ({ tool, output, success, error, index }: { tool: string, output: string, success: boolean, error?: string, index: number }) => {
    const [isOpen, setIsOpen] = useState(false);
    return (
      <div className="border border-slate-800 rounded bg-slate-950/60 text-xs overflow-hidden">
        <button 
          id={`tool-result-${index}`}
          onClick={() => setIsOpen(!isOpen)}
          className="w-full px-3 py-2 text-left hover:bg-slate-800/50 flex justify-between items-center font-mono text-emerald-400"
        >
          <span>🔨 {tool} result ({success ? 'success' : 'failed'})</span>
          <span>{isOpen ? '▲ Collapse' : '▼ Expand'}</span>
        </button>
        {isOpen && (
          <pre className="p-3 bg-slate-950 overflow-x-auto text-slate-300 font-mono border-t border-slate-800 max-h-60">
            {error ? `Error: ${error}\n` : ''}
            {output}
          </pre>
        )}
      </div>
    );
  };
  ```
  Now, place the Terminal Monitor UI inside `App.tsx`:
  ```tsx
  {/* Terminal Log */}
  <div className="flex-1 bg-slate-900 border border-slate-800 rounded-xl p-5 flex flex-col min-h-[400px]">
    <h2 className="text-lg font-semibold flex items-center gap-2 mb-3"><Terminal className="w-5 h-5 text-indigo-400" /> Live Terminal Logs</h2>
    <div 
      id="terminal-logs"
      className="flex-1 bg-slate-950 border border-slate-800 rounded-lg p-4 font-mono text-xs overflow-y-auto space-y-3 max-h-[500px]"
    >
      {logs.map((log, index) => {
        if (log.type === 'reasoning') {
          return <div key={index} className="text-slate-400 italic">💡 {log.data.text}</div>;
        }
        if (log.type === 'tool_call') {
          return (
            <div key={index} className="text-amber-400">
              ⚡ Call: <span className="font-bold">{log.data.tool}</span>({JSON.stringify(log.data.args)})
            </div>
          );
        }
        if (log.type === 'tool_result') {
          return (
            <CollapsibleToolResult 
              key={index}
              index={index}
              tool={log.data.tool}
              output={log.data.output}
              success={log.data.success}
              error={log.data.error}
            />
          );
        }
        if (log.type === 'error') {
          return <div key={index} className="text-red-500 font-bold border-l-2 border-red-500 pl-2">❌ {log.data.message}</div>;
        }
        return null;
      })}
      {status === 'running' && <div className="text-indigo-400 animate-pulse font-bold">● Running agent execution graph...</div>}
      {status === 'completed' && <div className="text-emerald-400 font-bold">✔ Research execution complete.</div>}
    </div>
  </div>
  ```

- [ ] **Step 3: Verify and Build**
  Run: `npm run build` in `task03-agent/frontend/`
  Expected: PASS

- [ ] **Step 4: Commit**
  Run: `git add . && git commit -m "feat: complete Live Terminal and Cost Progress components"`

---

### Task 5: Report Rendering & Export Options

**Files:**
- Modify: `task03-agent/frontend/src/App.tsx`
- Create: `task03-agent/frontend/src/MarkdownRenderer.tsx`

**Interfaces:**
- Consumes: `reportMarkdown` and `charts` states, backend GET `/api/v1/agent/report/{run_id}/pdf`
- Produces: Rendered reports, custom tables/charts, and file downloads.

- [ ] **Step 1: Implement custom lightweight markdown renderer**
  Instead of installing complex markdown dependencies, write a lightweight but reliable custom Markdown component `task03-agent/frontend/src/MarkdownRenderer.tsx` that supports headings, bullet points, numbered lists, and tables:
  ```tsx
  import React from 'react';

  interface MarkdownProps {
    content: string;
  }

  export default function MarkdownRenderer({ content }: MarkdownProps) {
    if (!content) return <div className="text-slate-500 italic">No report content generated yet.</div>;

    const parseLine = (line: string, index: number) => {
      const trimmed = line.trim();
      
      // Headers
      if (trimmed.startsWith('# ')) {
        return <h1 key={index} className="text-2xl font-bold text-white border-b border-slate-800 pb-2 mt-6 mb-4">{trimmed.substring(2)}</h1>;
      }
      if (trimmed.startsWith('## ')) {
        return <h2 key={index} className="text-xl font-bold text-slate-100 mt-5 mb-3">{trimmed.substring(3)}</h2>;
      }
      if (trimmed.startsWith('### ')) {
        return <h3 key={index} className="text-lg font-bold text-slate-200 mt-4 mb-2">{trimmed.substring(4)}</h3>;
      }

      // Lists
      if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {
        return <li key={index} className="ml-5 list-disc text-sm text-slate-300 my-1">{trimmed.substring(2)}</li>;
      }

      // Table parsing (simple pipe-separated rows)
      if (trimmed.startsWith('|') && trimmed.endsWith('|')) {
        const cells = trimmed.split('|').map(c => c.trim()).filter((_, idx, arr) => idx > 0 && idx < arr.length - 1);
        const isHeader = line.includes('---') || (index > 0 && content.split('\n')[index + 1]?.includes('---'));
        
        if (isHeader) {
          if (trimmed.includes('---')) return null; // skip separators
          return (
            <tr key={index} className="bg-slate-900 border-b border-slate-800">
              {cells.map((cell, cIdx) => (
                <th key={cIdx} className="px-4 py-2 text-left text-xs font-bold text-slate-400 uppercase tracking-wider">{cell}</th>
              ))}
            </tr>
          );
        }
        return (
          <tr key={index} className="border-b border-slate-850 hover:bg-slate-900/30">
            {cells.map((cell, cIdx) => (
              <td key={cIdx} className="px-4 py-2 text-sm text-slate-300">{cell}</td>
            ))}
          </tr>
        );
      }

      // Default paragraphs
      if (trimmed === '') return <div key={index} className="h-2" />;
      return <p key={index} className="text-sm text-slate-300 leading-relaxed my-2">{trimmed}</p>;
    };

    const lines = content.split('\n');
    let insideTable = false;
    const renderedElements: React.ReactNode[] = [];
    let currentTableRows: React.ReactNode[] = [];

    lines.forEach((line, idx) => {
      const isTableRow = line.trim().startsWith('|') && line.trim().endsWith('|');
      
      if (isTableRow) {
        if (!insideTable) {
          insideTable = true;
          currentTableRows = [];
        }
        const row = parseLine(line, idx);
        if (row) currentTableRows.push(row);
      } else {
        if (insideTable) {
          insideTable = false;
          renderedElements.push(
            <div key={`table-${idx}`} className="overflow-x-auto my-4 border border-slate-800 rounded-lg">
              <table className="min-w-full divide-y divide-slate-800 bg-slate-950/20">
                <tbody>{currentTableRows}</tbody>
              </table>
            </div>
          );
        }
        renderedElements.push(parseLine(line, idx));
      }
    });

    if (insideTable) {
      renderedElements.push(
        <div key="table-end" className="overflow-x-auto my-4 border border-slate-800 rounded-lg">
          <table className="min-w-full divide-y divide-slate-800 bg-slate-950/20">
            <tbody>{currentTableRows}</tbody>
          </table>
        </div>
      );
    }

    return <div className="space-y-1">{renderedElements}</div>;
  }
  ```

- [ ] **Step 2: Add Results Pane & Export Panel**
  Integrate `MarkdownRenderer` and render Base64 charts.
  Implement the PDF and Markdown export download logic inside `App.tsx`:
  ```tsx
  import MarkdownRenderer from './MarkdownRenderer';

  // Export buttons triggers
  const downloadMarkdown = () => {
    if (!reportMarkdown) return;
    const blob = new Blob([reportMarkdown], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `research-report-${runId ? runId.substring(0, 8) : 'export'}.md`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const downloadPDF = async () => {
    if (!runId) return;
    try {
      const res = await fetch(`http://localhost:8000/api/v1/agent/report/${runId}/pdf`);
      if (!res.ok) throw new Error("Failed to download PDF");
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `research-report-${runId.substring(0, 8)}.pdf`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (err: any) {
      console.error(err);
      alert("Error downloading PDF: " + err.message);
    }
  };
  ```
  Now, include the visual components in layout (bottom of the page or in a split layout):
  ```tsx
  {/* Bottom Results Section */}
  <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 space-y-6 mt-6 col-span-1 lg:col-span-2">
    <div className="flex justify-between items-center border-b border-slate-800 pb-3">
      <h2 className="text-xl font-bold flex items-center gap-2">📊 Research Results</h2>
      <div className="flex gap-2">
        <button
          id="export-md-btn"
          onClick={downloadMarkdown}
          disabled={!reportMarkdown}
          className="bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:hover:bg-slate-800 text-xs px-3 py-1.5 rounded border border-slate-750 flex items-center gap-1.5 transition-colors font-semibold"
        >
          <Download className="w-3.5 h-3.5" /> Export MD
        </button>
        <button
          id="export-pdf-btn"
          onClick={downloadPDF}
          disabled={status !== 'completed'}
          className="bg-indigo-600 hover:bg-indigo-700 disabled:opacity-40 disabled:hover:bg-indigo-600 text-xs px-3 py-1.5 rounded flex items-center gap-1.5 transition-colors font-semibold text-white"
        >
          <Download className="w-3.5 h-3.5" /> Export PDF
        </button>
      </div>
    </div>

    <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
      {/* Markdown Text */}
      <div id="report-markdown" className="xl:col-span-2 bg-slate-950 border border-slate-800 rounded-lg p-5 max-h-[600px] overflow-y-auto">
        <MarkdownRenderer content={reportMarkdown} />
      </div>
      
      {/* Charts Panel */}
      <div className="space-y-4">
        <h3 className="text-sm font-semibold text-slate-400 uppercase tracking-wider">Comparison Charts</h3>
        <div id="report-charts" className="space-y-4 bg-slate-950 border border-slate-800 rounded-lg p-4 max-h-[600px] overflow-y-auto">
          {charts.length === 0 ? (
            <div className="text-slate-500 text-xs italic text-center py-10">No charts generated for this run.</div>
          ) : (
            charts.map((chart, cIdx) => (
              <div key={cIdx} className="space-y-2 border border-slate-800 p-2.5 rounded bg-slate-900/40">
                <div className="text-xs font-semibold text-slate-300 font-mono truncate">{chart.name}</div>
                <img 
                  src={`data:image/png;base64,${chart.base64}`} 
                  alt={chart.name} 
                  className="w-full h-auto rounded border border-slate-800 bg-white" 
                />
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  </div>
  ```

- [ ] **Step 3: Compile check**
  Run: `npm run build` in `task03-agent/frontend/`
  Expected: PASS

- [ ] **Step 4: Commit**
  Run: `git add . && git commit -m "feat: add markdown parser, image base64 chart view, and PDF/MD export actions"`

---

### Task 6: Final Integration, Styling & Build Run

**Files:**
- Modify: `task03-agent/frontend/src/App.tsx`
- Modify: `task03-agent/frontend/index.html`

**Interfaces:**
- Consumes: Full codebase
- Produces: Production ready optimized bundle.

- [ ] **Step 1: Check full `App.tsx` file for alignment and missing styles**
  Complete any UI additions (e.g. handle loading states, display error message banners).
  ```tsx
  {errorMsg && (
    <div className="bg-red-500/10 border border-red-500/25 text-red-400 p-4 rounded-lg flex items-start gap-3 mt-4">
      <AlertTriangle className="w-5 h-5 flex-shrink-0 mt-0.5" />
      <div>
        <span className="font-bold">Error executing research run:</span>
        <p className="text-sm mt-1">{errorMsg}</p>
      </div>
    </div>
  )}
  ```

- [ ] **Step 2: Update HTML title**
  Change the title in `index.html` to `AI Research Agent Dashboard`.

- [ ] **Step 3: Run final project build**
  Run: `npm run build` inside `task03-agent/frontend/`
  Expected: Successfully builds without any TypeScript compiler errors or Vite warnings.
