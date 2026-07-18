import { useEffect, useMemo, useRef, useState } from 'react';
import {
  AlertTriangle,
  ArrowUpRight,
  BarChart3,
  BrainCircuit,
  CheckCircle2,
  ChevronDown,
  ChevronRight,
  CircleDollarSign,
  Code2,
  Database,
  Download,
  FileSearch,
  Globe2,
  Loader2,
  Play,
  Radar,
  RefreshCw,
  Search,
  ShieldCheck,
  Sparkles,
  Terminal,
  TimerReset,
} from 'lucide-react';
import MarkdownRenderer from './MarkdownRenderer';
import heroImage from './assets/hero.png';
import type { ChartItem, CostSnapshot, RunStatus, SSEEvent } from './types';

type ToolResultProps = {
  tool: string;
  output: string;
  success: boolean;
  error?: string;
  index: number;
};

const toolMeta = {
  web_search: { label: 'Web Search', icon: Globe2, tone: 'cyan' },
  pdf_reader: { label: 'PDF Reader', icon: FileSearch, tone: 'violet' },
  code_executor: { label: 'Python Executor', icon: Code2, tone: 'amber' },
  vector_memory: { label: 'Vector Memory', icon: Database, tone: 'emerald' },
  store_memory: { label: 'Vector Memory', icon: Database, tone: 'emerald' },
  retrieve_memory: { label: 'Vector Memory', icon: Database, tone: 'emerald' },
};

const primaryTools = ['web_search', 'pdf_reader', 'code_executor', 'vector_memory'] as const;

const formatToolName = (tool: string) => {
  const known = toolMeta[tool as keyof typeof toolMeta];
  if (known) return known.label;
  return tool.replaceAll('_', ' ').replace(/\b\w/g, (letter) => letter.toUpperCase());
};

const formatCurrency = (value: number) => `$${value.toFixed(value >= 1 ? 2 : 5)}`;

const CollapsibleToolResult = ({ tool, output, success, error, index }: ToolResultProps) => {
  const [isOpen, setIsOpen] = useState(false);
  const KnownIcon = toolMeta[tool as keyof typeof toolMeta]?.icon ?? Search;

  return (
    <div className={`tool-result ${success ? 'tool-result-success' : 'tool-result-failed'}`}>
      <button
        id={`tool-result-${index}`}
        onClick={() => setIsOpen((open) => !open)}
        className="tool-result-toggle"
        type="button"
      >
        <span className="tool-result-title">
          <KnownIcon className="icon-sm" />
          <span>{formatToolName(tool)}</span>
          <span className={`tool-chip ${success ? 'chip-success' : 'chip-failed'}`}>
            {success ? 'Recovered output' : 'Failed'}
          </span>
        </span>
        <span className="tool-result-action">
          {isOpen ? <ChevronDown className="icon-sm" /> : <ChevronRight className="icon-sm" />}
          {isOpen ? 'Collapse' : 'Inspect'}
        </span>
      </button>
      {isOpen && (
        <div className="tool-result-body">
          {error && <div className="tool-error">Error: {error}</div>}
          <pre>{output || 'No output returned.'}</pre>
        </div>
      )}
    </div>
  );
};

const StatusBadge = ({ status }: { status: RunStatus }) => {
  return (
    <span id="status-badge" className={`status-badge status-${status}`}>
      <span className="status-dot" />
      {status}
    </span>
  );
};

const EmptyTerminal = () => (
  <div className="terminal-empty">
    <Radar className="empty-radar" />
    <span>Awaiting live reasoning stream.</span>
  </div>
);

export default function App() {
  const [topic, setTopic] = useState('wearable technology competitive landscape top 5 competitors');
  const [budget, setBudget] = useState(1.0);
  const [runId, setRunId] = useState<string | null>(null);
  const [status, setStatus] = useState<RunStatus>('idle');
  const [logs, setLogs] = useState<SSEEvent[]>([]);
  const [cost, setCost] = useState<CostSnapshot>({
    input_tokens: 0,
    output_tokens: 0,
    total_tokens: 0,
    total_usd: 0,
    cumulative_usd: 0,
  });
  const [reportMarkdown, setReportMarkdown] = useState('');
  const [charts, setCharts] = useState<ChartItem[]>([]);
  const [errorMsg, setErrorMsg] = useState('');

  const terminalEndRef = useRef<HTMLDivElement | null>(null);
  const eventSourceRef = useRef<EventSource | null>(null);

  useEffect(() => {
    terminalEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [logs]);

  useEffect(() => {
    return () => {
      eventSourceRef.current?.close();
    };
  }, []);

  const activeCost = cost.cumulative_usd ?? cost.total_usd;
  const totalTokens = cost.total_tokens || cost.input_tokens + cost.output_tokens;
  const budgetPercent = Math.min(100, budget > 0 ? (activeCost / budget) * 100 : 0);

  const runSummary = useMemo(() => {
    const reasoning = logs.filter((log) => log.type === 'reasoning').length;
    const toolCalls = logs.filter((log) => log.type === 'tool_call').length;
    const toolResults = logs.filter((log) => log.type === 'tool_result');
    const failures = toolResults.filter((log) => log.data?.success === false).length + (errorMsg ? 1 : 0);
    return { reasoning, toolCalls, toolResults: toolResults.length, failures };
  }, [errorMsg, logs]);

  const toolHealth = useMemo(() => {
    return primaryTools.map((tool) => {
      const meta = toolMeta[tool];
      const aliases = tool === 'vector_memory' ? ['vector_memory', 'store_memory', 'retrieve_memory'] : [tool];
      const calls = logs.filter((log) => log.type === 'tool_call' && aliases.includes(log.data?.tool)).length;
      const results = logs.filter((log) => log.type === 'tool_result' && aliases.includes(log.data?.tool));
      const failed = results.some((log) => log.data?.success === false);
      const complete = results.some((log) => log.data?.success === true);
      return { tool, ...meta, calls, failed, complete };
    });
  }, [logs]);

  const connectSSE = (id: string) => {
    eventSourceRef.current?.close();
    const eventSource = new EventSource(`http://localhost:8000/api/v1/agent/stream/${id}`);
    eventSourceRef.current = eventSource;

    eventSource.onmessage = (event) => {
      try {
        const payload: SSEEvent = JSON.parse(event.data);
        setLogs((prev) => [...prev, payload]);

        if (payload.type === 'cost') {
          setCost(payload.data);
        } else if (payload.type === 'report') {
          if (payload.data.markdown) setReportMarkdown(payload.data.markdown);
          if (payload.data.charts) setCharts(payload.data.charts);
        } else if (payload.type === 'error') {
          if (payload.data.recoverable) {
            console.warn('Recoverable agent event', payload.data.message);
          } else {
            setStatus('error');
            setErrorMsg(payload.data.message || 'An error occurred during execution.');
            eventSource.close();
          }
        } else if (payload.type === 'done') {
          setStatus('completed');
          eventSource.close();
        }
      } catch (err) {
        console.error('Failed to parse SSE event data', err);
      }
    };

    eventSource.onerror = () => {
      eventSource.close();
      setStatus((current) => {
        if (current === 'running') {
          setErrorMsg('SSE stream connection was disconnected before the agent completed.');
          return 'error';
        }
        return current;
      });
    };
  };

  const startResearch = async () => {
    if (!topic.trim()) {
      setErrorMsg('Enter a research topic before starting a run.');
      return;
    }

    setStatus('running');
    setLogs([]);
    setReportMarkdown('');
    setCharts([]);
    setErrorMsg('');
    setCost({
      input_tokens: 0,
      output_tokens: 0,
      total_tokens: 0,
      total_usd: 0,
      cumulative_usd: 0,
    });

    try {
      const res = await fetch('http://localhost:8000/api/v1/agent/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          topic,
          max_cost_usd: budget,
        }),
      });

      if (!res.ok) {
        throw new Error(`Failed to start run: server returned ${res.status}`);
      }

      const data = await res.json();
      setRunId(data.run_id);
      connectSSE(data.run_id);
    } catch (e: unknown) {
      const message = e instanceof Error ? e.message : 'Request failed';
      setStatus('error');
      setErrorMsg(message);
    }
  };

  const downloadMarkdown = () => {
    if (!reportMarkdown) return;
    const blob = new Blob([reportMarkdown], { type: 'text/markdown;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `research-report-${runId ? runId.substring(0, 8) : 'export'}.md`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  };

  const downloadPDF = async () => {
    if (!runId) return;
    try {
      const res = await fetch(`http://localhost:8000/api/v1/agent/report/${runId}/pdf`);
      if (!res.ok) {
        throw new Error('Failed to download PDF. Server returned an error.');
      }
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `research-report-${runId.substring(0, 8)}.pdf`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : 'Unknown export error';
      setErrorMsg(`PDF export failed: ${message}`);
    }
  };

  const renderLog = (log: SSEEvent, index: number) => {
    if (log.type === 'reasoning') {
      return (
        <div key={index} className="terminal-line terminal-reasoning">
          <BrainCircuit className="icon-sm" />
          <span>{log.data.text ?? log.data.delta}</span>
        </div>
      );
    }

    if (log.type === 'tool_call') {
      const KnownIcon = toolMeta[log.data.tool as keyof typeof toolMeta]?.icon ?? Search;
      return (
        <div key={index} className="terminal-line terminal-tool-call">
          <KnownIcon className="icon-sm" />
          <span>
            <strong>{formatToolName(log.data.tool)}</strong> requested with{' '}
            <code>{JSON.stringify(log.data.args)}</code>
          </span>
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

    if (log.type === 'cost') {
      return (
        <div key={index} className="terminal-line terminal-cost">
          <CircleDollarSign className="icon-sm" />
          <span>
            Cost checkpoint: {formatCurrency(log.data.cumulative_usd ?? log.data.total_usd)} across{' '}
            {(log.data.total_tokens || 0).toLocaleString()} tokens
          </span>
        </div>
      );
    }

    if (log.type === 'report') {
      return (
        <div key={index} className="terminal-line terminal-report">
          <BarChart3 className="icon-sm" />
          <span>Structured report and chart payload received.</span>
        </div>
      );
    }

    if (log.type === 'error') {
      return (
        <div key={index} className="terminal-line terminal-error">
          <AlertTriangle className="icon-sm" />
          <span>{log.data.message}</span>
        </div>
      );
    }

    return null;
  };

  return (
    <div className="app-shell">
      <header className="topbar">
        <div className="brand-lockup">
          <div className="brand-mark">
            <Sparkles className="brand-icon" />
          </div>
          <div>
            <h1>Autonomous Research Agent</h1>
            <p>Task 03 competitive intelligence console</p>
          </div>
        </div>
        <div className="topbar-actions">
          <div className="run-id-pill">{runId ? `Run ${runId.substring(0, 8)}` : 'No active run'}</div>
          <StatusBadge status={status} />
        </div>
      </header>

      <main className="dashboard">
        <section className="hero-panel">
          <div className="hero-copy">
            <div className="eyebrow">
              <ShieldCheck className="icon-sm" />
              Failure-aware multi-tool agent
            </div>
            <h2>Find the wearable market leaders, prove the differentiators, and ship the report.</h2>
            <p>
              Live reasoning, tool recovery, token spend, charts, and export controls are visible in one
              operator-grade workspace.
            </p>
          </div>
          <div className="hero-visual" aria-hidden="true">
            <img src={heroImage} alt="" />
            <div className="hero-metric hero-metric-one">
              <span>Tools</span>
              <strong>4</strong>
            </div>
            <div className="hero-metric hero-metric-two">
              <span>Stream</span>
              <strong>SSE</strong>
            </div>
          </div>
        </section>

        <section className="control-panel">
          <div className="section-heading">
            <div>
              <span className="section-kicker">Research Configuration</span>
              <h2>Mission brief</h2>
            </div>
            <Play className="section-icon" />
          </div>

          <label htmlFor="topic-input" className="field-label">
            Research topic
          </label>
          <textarea
            id="topic-input"
            rows={4}
            value={topic}
            onChange={(event) => setTopic(event.target.value)}
            disabled={status === 'running'}
            placeholder="Describe the competitive research objective..."
          />

          <div className="budget-row">
            <label htmlFor="budget-slider" className="field-label">
              Max budget limit
            </label>
            <span>{formatCurrency(budget)} USD</span>
          </div>
          <input
            id="budget-slider"
            type="range"
            min="0.10"
            max="5.00"
            step="0.05"
            value={budget}
            onChange={(event) => setBudget(parseFloat(event.target.value))}
            disabled={status === 'running'}
          />

          <button
            id="start-btn"
            onClick={startResearch}
            disabled={status === 'running'}
            className="primary-action"
            type="button"
          >
            {status === 'running' ? (
              <>
                <RefreshCw className="icon-md spinning" />
                Researching
              </>
            ) : (
              <>
                <Play className="icon-md fill-icon" />
                Start Research Run
              </>
            )}
          </button>
        </section>

        <section className="cost-panel">
          <div className="section-heading">
            <div>
              <span className="section-kicker">Budget & Tokens Monitor</span>
              <h2>Spend control</h2>
            </div>
            <CircleDollarSign className="section-icon green" />
          </div>

          <div className="cost-orbit">
            <div className="cost-value">{formatCurrency(activeCost)}</div>
            <div className="cost-label">of {formatCurrency(budget)} budget</div>
            <div className="cost-ring" style={{ '--progress': `${budgetPercent}%` } as React.CSSProperties} />
          </div>

          <div id="cost-progress-bar" className="progress-track">
            <div className="progress-fill" style={{ width: `${budgetPercent}%` }} />
          </div>

          <div id="cost-stats" className="metric-grid">
            <div className="metric-card">
              <span>Input Tokens</span>
              <strong>{cost.input_tokens.toLocaleString()}</strong>
            </div>
            <div className="metric-card">
              <span>Output Tokens</span>
              <strong>{cost.output_tokens.toLocaleString()}</strong>
            </div>
            <div className="metric-card metric-wide">
              <span>Total Combined Tokens</span>
              <strong>{totalTokens.toLocaleString()}</strong>
            </div>
          </div>
        </section>

        <section className="tool-panel">
          <div className="section-heading compact">
            <div>
              <span className="section-kicker">Tool Stack</span>
              <h2>Recovery surface</h2>
            </div>
          </div>
          <div className="tool-grid">
            {toolHealth.map((tool) => {
              const Icon = tool.icon;
              return (
                <div key={tool.tool} className={`tool-card tool-${tool.tone}`}>
                  <Icon className="icon-md" />
                  <div>
                    <strong>{tool.label}</strong>
                    <span>
                      {tool.complete
                        ? 'Validated'
                        : tool.failed
                          ? 'Needs recovery'
                          : tool.calls > 0
                            ? 'In flight'
                            : 'Ready'}
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        </section>

        <section className="terminal-panel">
          <div className="section-heading">
            <div>
              <span className="section-kicker">Live Terminal Monitor</span>
              <h2>Reasoning stream</h2>
            </div>
            <Terminal className="section-icon" />
          </div>

          <div className="run-stats">
            <div>
              <span>Reasoning</span>
              <strong>{runSummary.reasoning}</strong>
            </div>
            <div>
              <span>Tool Calls</span>
              <strong>{runSummary.toolCalls}</strong>
            </div>
            <div>
              <span>Results</span>
              <strong>{runSummary.toolResults}</strong>
            </div>
            <div>
              <span>Failures</span>
              <strong>{runSummary.failures}</strong>
            </div>
          </div>

          <div id="terminal-logs" className="terminal-window">
            {logs.length === 0 ? <EmptyTerminal /> : logs.map(renderLog)}
            {status === 'running' && (
              <div className="terminal-line terminal-running">
                <Loader2 className="icon-sm spinning" />
                <span>Executing LangGraph node...</span>
              </div>
            )}
            {status === 'completed' && (
              <div className="terminal-line terminal-complete">
                <CheckCircle2 className="icon-sm" />
                <span>Agent completed successfully.</span>
              </div>
            )}
            <div ref={terminalEndRef} />
          </div>

          {errorMsg && (
            <div className="error-banner">
              <AlertTriangle className="icon-md" />
              <div>
                <strong>Run Failure</strong>
                <p>{errorMsg}</p>
              </div>
            </div>
          )}
        </section>

        <section className="insights-panel">
          <div className="insights-header">
            <div>
              <span className="section-kicker">Synthesized Competitive Insights</span>
              <h2>Structured report workspace</h2>
            </div>
            <div className="export-actions">
              <button id="export-md-btn" onClick={downloadMarkdown} disabled={!reportMarkdown} type="button">
                <Download className="icon-sm" />
                Export MD
              </button>
              <button id="export-pdf-btn" onClick={downloadPDF} disabled={status !== 'completed'} type="button">
                <Download className="icon-sm" />
                Export PDF
              </button>
            </div>
          </div>

          <div className="results-grid">
            <div id="report-markdown" className="report-surface">
              <MarkdownRenderer content={reportMarkdown} />
            </div>

            <aside className="chart-panel">
              <div className="chart-heading">
                <div>
                  <span>Matplotlib Visualizations</span>
                  <strong>{charts.length} charts</strong>
                </div>
                <ArrowUpRight className="icon-sm" />
              </div>
              <div id="report-charts" className="chart-list">
                {charts.length === 0 ? (
                  <div className="chart-empty">
                    <BarChart3 className="icon-lg" />
                    <span>Charts will appear when the report payload streams in.</span>
                  </div>
                ) : (
                  charts.map((chart, cIdx) => (
                    <figure key={`${chart.name}-${cIdx}`} className="chart-card">
                      <figcaption>{chart.name}</figcaption>
                      <img src={`data:image/png;base64,${chart.base64}`} alt={chart.name} />
                    </figure>
                  ))
                )}
              </div>
            </aside>
          </div>
        </section>

        <section className="readiness-strip">
          <div>
            <TimerReset className="icon-md" />
            <span>Real-time stream</span>
          </div>
          <div>
            <ShieldCheck className="icon-md" />
            <span>Tool failure recovery visible</span>
          </div>
          <div>
            <CircleDollarSign className="icon-md" />
            <span>Cumulative cost tracked</span>
          </div>
          <div>
            <Download className="icon-md" />
            <span>Markdown and PDF exports</span>
          </div>
        </section>
      </main>
    </div>
  );
}
