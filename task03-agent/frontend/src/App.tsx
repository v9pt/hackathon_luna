import { useState, useEffect, useRef } from 'react';
import { Play, Terminal, DollarSign, Download, AlertTriangle, Cpu, HelpCircle, RefreshCw } from 'lucide-react';
import type { RunStatus, SSEEvent, CostSnapshot, ChartItem } from './types';
import MarkdownRenderer from './MarkdownRenderer';


const CollapsibleToolResult = ({ 
  tool, 
  output, 
  success, 
  error, 
  index 
}: { 
  tool: string; 
  output: string; 
  success: boolean; 
  error?: string; 
  index: number; 
}) => {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <div className="border border-slate-800 rounded bg-slate-950/65 text-xs overflow-hidden">
      <button 
        id={`tool-result-${index}`}
        onClick={() => setIsOpen(!isOpen)}
        className="w-full px-3 py-2 text-left hover:bg-slate-850 flex justify-between items-center font-mono transition-colors"
      >
        <span className="flex items-center gap-1.5 font-bold">
          <span>🔨</span>
          <span className="text-slate-300">Tool:</span>
          <span className="text-amber-400">{tool}</span>
          <span className={success ? 'text-emerald-400' : 'text-red-400'}>
            ({success ? 'success' : 'failed'})
          </span>
        </span>
        <span className="text-slate-500 font-bold">{isOpen ? '▲ Collapse' : '▼ Expand'}</span>
      </button>
      {isOpen && (
        <div className="p-3 bg-slate-950/80 overflow-x-auto text-slate-300 font-mono border-t border-slate-800 max-h-64 leading-relaxed">
          {error && <div className="text-red-400 font-bold mb-2">Error: {error}</div>}
          <pre className="whitespace-pre-wrap">{output || 'No output returned.'}</pre>
        </div>
      )}
    </div>
  );
};

export default function App() {
  const [topic, setTopic] = useState("wearable technology competitive landscape top 5 competitors");
  const [budget, setBudget] = useState(1.0);
  const [runId, setRunId] = useState<string | null>(null);
  const [status, setStatus] = useState<RunStatus>('idle');
  const [logs, setLogs] = useState<SSEEvent[]>([]);
  const [cost, setCost] = useState<CostSnapshot>({ 
    input_tokens: 0, 
    output_tokens: 0, 
    total_tokens: 0, 
    total_usd: 0, 
    cumulative_usd: 0 
  });
  const [reportMarkdown, setReportMarkdown] = useState<string>("");
  const [charts, setCharts] = useState<ChartItem[]>([]);
  const [errorMsg, setErrorMsg] = useState<string>("");

  const terminalEndRef = useRef<HTMLDivElement | null>(null);

  // Auto scroll terminal logs
  useEffect(() => {
    if (terminalEndRef.current) {
      terminalEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [logs]);

  const startResearch = async () => {
    if (!topic.trim()) {
      alert("Please enter a research topic.");
      return;
    }

    setStatus('running');
    setLogs([]);
    setReportMarkdown("");
    setCharts([]);
    setErrorMsg("");
    setCost({ 
      input_tokens: 0, 
      output_tokens: 0, 
      total_tokens: 0, 
      total_usd: 0, 
      cumulative_usd: 0 
    });

    try {
      const res = await fetch("http://localhost:8000/api/v1/agent/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          topic, 
          max_cost_usd: budget 
        })
      });
      
      if (!res.ok) {
        throw new Error(`Failed to start run: Server returned ${res.status}`);
      }
      
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
        
        // Append to logs
        setLogs(prev => [...prev, payload]);

        // Process based on type
        if (payload.type === 'cost') {
          setCost(payload.data);
        } else if (payload.type === 'report') {
          if (payload.data.markdown) {
            setReportMarkdown(payload.data.markdown);
          }
          if (payload.data.charts) {
            setCharts(payload.data.charts);
          }
        } else if (payload.type === 'error') {
          setStatus('error');
          setErrorMsg(payload.data.message || 'An error occurred during execution.');
          eventSource.close();
        } else if (payload.type === 'done') {
          setStatus('completed');
          eventSource.close();
        }
      } catch (err) {
        console.error("Failed to parse SSE event data", err);
      }
    };

    eventSource.onerror = (err) => {
      console.error("SSE connection error", err);
      eventSource.close();
      // If we are currently running, transition to error state
      setStatus(prev => {
        if (prev === 'running') {
          setErrorMsg("SSE stream connection was disconnected prematurely.");
          return 'error';
        }
        return prev;
      });
    };
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
        throw new Error("Failed to download PDF. Server returned error.");
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
    } catch (err: any) {
      console.error("Error exporting PDF:", err);
      alert("Error exporting PDF: " + err.message);
    }
  };

  const activeCost = cost.cumulative_usd !== undefined ? cost.cumulative_usd : cost.total_usd;

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col antialiased">
      {/* Header */}
      <header className="border-b border-slate-900 bg-slate-900/40 backdrop-blur px-6 py-4 flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center font-bold text-white text-lg tracking-wider">
            AI
          </div>
          <div>
            <h1 className="text-base font-bold tracking-tight text-white">Autonomous Research Agent</h1>
            <p className="text-[10px] text-slate-400">LangGraph-backed Competitive Intelligence</p>
          </div>
        </div>
        
        <div>
          <span 
            id="status-badge" 
            className={`px-3 py-1.5 rounded-full text-[10px] font-bold uppercase tracking-wider transition-all duration-300 ${
              status === 'idle' ? 'bg-slate-800/80 text-slate-400 border border-slate-700/50' :
              status === 'running' ? 'bg-amber-500/15 text-amber-400 border border-amber-500/30 animate-pulse' :
              status === 'completed' ? 'bg-emerald-500/15 text-emerald-400 border border-emerald-500/30' :
              'bg-red-500/15 text-red-400 border border-red-500/30'
            }`}
          >
            {status}
          </span>
        </div>
      </header>

      {/* Main Grid */}
      <main className="flex-1 p-6 max-w-7xl w-full mx-auto grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        {/* Left Column (Controls & Cost) */}
        <div className="lg:col-span-5 space-y-6 flex flex-col">
          
          {/* Controls Panel */}
          <div className="bg-slate-900/60 border border-slate-900 rounded-xl p-5 space-y-4 shadow-sm">
            <h2 className="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
              <Play className="w-4 h-4 text-indigo-500" /> Research Configuration
            </h2>
            
            <div className="space-y-1.5">
              <label htmlFor="topic-input" className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">
                Research Topic
              </label>
              <textarea
                id="topic-input"
                rows={3}
                className="w-full bg-slate-950 border border-slate-850 rounded-lg p-3 text-xs leading-relaxed focus:outline-none focus:ring-1 focus:ring-indigo-500 text-slate-200 resize-none transition-all"
                value={topic}
                onChange={(e) => setTopic(e.target.value)}
                disabled={status === 'running'}
                placeholder="Describe your research topic in detail..."
              />
            </div>
            
            <div className="space-y-2">
              <div className="flex justify-between items-center text-[10px] font-bold text-slate-500 uppercase tracking-wider">
                <span>Max Budget Limit</span>
                <span className="text-xs font-semibold text-indigo-400 font-mono">${budget.toFixed(2)} USD</span>
              </div>
              <input
                id="budget-slider"
                type="range"
                min="0.10"
                max="5.00"
                step="0.05"
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
              className="w-full bg-indigo-600 hover:bg-indigo-500 active:bg-indigo-700 disabled:bg-slate-900 disabled:text-slate-600 disabled:border-slate-800/50 disabled:cursor-not-allowed text-white font-semibold py-2.5 rounded-lg transition-all text-xs flex items-center justify-center gap-2 border border-indigo-500/20 shadow-md"
            >
              {status === 'running' ? (
                <>
                  <RefreshCw className="w-3.5 h-3.5 animate-spin" />
                  <span>Researching...</span>
                </>
              ) : (
                <>
                  <Play className="w-3.5 h-3.5 fill-current" />
                  <span>Start Research Run</span>
                </>
              )}
            </button>
          </div>

          {/* Budget & Cost Tracker */}
          <div className="bg-slate-900/60 border border-slate-900 rounded-xl p-5 space-y-4 shadow-sm flex-1 flex flex-col justify-between">
            <div className="space-y-4">
              <h2 className="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
                <DollarSign className="w-4 h-4 text-emerald-500" /> Budget & Tokens Monitor
              </h2>
              
              <div className="space-y-2">
                <div className="flex justify-between text-[11px] font-semibold text-slate-400">
                  <span>Cumulative Cost</span>
                  <span className="font-bold text-emerald-400 font-mono">
                    ${activeCost.toFixed(5)} / ${budget.toFixed(2)}
                  </span>
                </div>
                
                <div 
                  id="cost-progress-bar" 
                  className="w-full bg-slate-950 h-3.5 rounded-full overflow-hidden border border-slate-900 p-0.5"
                >
                  <div 
                    className="bg-emerald-500 h-full rounded-full transition-all duration-300 shadow-[0_0_8px_rgba(16,185,129,0.4)]"
                    style={{ width: `${Math.min(100, (activeCost / budget) * 100)}%` }}
                  />
                </div>
              </div>
            </div>

            <div id="cost-stats" className="grid grid-cols-2 gap-3 mt-4">
              <div className="bg-slate-950/80 p-3 rounded-lg border border-slate-900">
                <span className="text-[9px] text-slate-500 block uppercase font-bold tracking-wider">Input Tokens</span>
                <span className="text-sm font-bold font-mono text-slate-200">{cost.input_tokens.toLocaleString()}</span>
              </div>
              <div className="bg-slate-950/80 p-3 rounded-lg border border-slate-900">
                <span className="text-[9px] text-slate-500 block uppercase font-bold tracking-wider">Output Tokens</span>
                <span className="text-sm font-bold font-mono text-slate-200">{cost.output_tokens.toLocaleString()}</span>
              </div>
              <div className="bg-slate-950/80 p-3 rounded-lg border border-slate-900 col-span-2 flex justify-between items-center">
                <span className="text-[9px] text-slate-500 uppercase font-bold tracking-wider">Total Combined Tokens</span>
                <span className="text-xs font-bold font-mono text-slate-200">
                  {cost.total_tokens ? cost.total_tokens.toLocaleString() : (cost.input_tokens + cost.output_tokens).toLocaleString()}
                </span>
              </div>
            </div>
          </div>
        </div>

        {/* Right Column (Live Monitor) */}
        <div className="lg:col-span-7 flex flex-col min-h-[450px]">
          <div className="bg-slate-900/60 border border-slate-900 rounded-xl p-5 flex flex-col flex-1 shadow-sm">
            <h2 className="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2 mb-3">
              <Terminal className="w-4 h-4 text-indigo-400" /> Live Terminal Monitor
            </h2>
            
            <div 
              id="terminal-logs"
              className="flex-1 bg-slate-950 border border-slate-900 rounded-lg p-4 font-mono text-xs overflow-y-auto space-y-3 max-h-[400px] min-h-[250px] shadow-inner"
            >
              {logs.length === 0 ? (
                <div className="text-slate-600 italic text-center py-10 flex flex-col items-center justify-center gap-2">
                  <Cpu className="w-8 h-8 text-slate-800 animate-pulse" />
                  <span>Terminal idle. Trigger a research run to stream events.</span>
                </div>
              ) : (
                logs.map((log, index) => {
                  if (log.type === 'reasoning') {
                    return (
                      <div key={index} className="text-slate-400 flex items-start gap-1.5 leading-relaxed">
                        <span className="text-indigo-400 font-bold">💡</span>
                        <span className="italic">{log.data.text}</span>
                      </div>
                    );
                  }
                  if (log.type === 'tool_call') {
                    return (
                      <div key={index} className="text-amber-400/90 leading-relaxed">
                        <span className="text-amber-500 font-bold">⚡ Call:</span>{' '}
                        <span className="font-bold">{log.data.tool}</span>({JSON.stringify(log.data.args)})
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
                    return (
                      <div key={index} className="text-red-400 font-bold border-l-2 border-red-500 pl-2 py-0.5">
                        ❌ {log.data.message}
                      </div>
                    );
                  }
                  return null;
                })
              )}
              
              {status === 'running' && (
                <div className="text-indigo-400 animate-pulse font-bold flex items-center gap-1.5">
                  <span className="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-ping" />
                  <span>Executing agent graph node...</span>
                </div>
              )}
              
              {status === 'completed' && (
                <div className="text-emerald-400 font-bold flex items-center gap-1.5">
                  <span>✔</span>
                  <span>Agent finished execution successfully.</span>
                </div>
              )}
              
              <div ref={terminalEndRef} />
            </div>
            
            {/* Error Message Banner */}
            {errorMsg && (
              <div className="bg-red-500/10 border border-red-500/20 text-red-400 p-4 rounded-lg flex items-start gap-3 mt-4 text-xs leading-relaxed">
                <AlertTriangle className="w-4 h-4 flex-shrink-0 mt-0.5 text-red-500" />
                <div>
                  <span className="font-bold block text-red-300">Run Failure</span>
                  <p className="mt-1">{errorMsg}</p>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Bottom Results Panel (Markdown Report + Base64 Charts) */}
        <div className="lg:col-span-12 bg-slate-900/60 border border-slate-900 rounded-xl p-5 space-y-6 shadow-sm">
          
          {/* Action Export Bar */}
          <div className="flex justify-between items-center border-b border-slate-900 pb-4">
            <div>
              <h2 className="text-sm font-bold text-slate-200 uppercase tracking-wider">
                📊 Synthesized Competitive Insights
              </h2>
              <p className="text-[10px] text-slate-400 mt-0.5">Compiled real-time from vector and web searches</p>
            </div>
            
            <div className="flex gap-2">
              <button
                id="export-md-btn"
                onClick={downloadMarkdown}
                disabled={!reportMarkdown}
                className="bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:hover:bg-slate-800 text-xs px-3.5 py-2 rounded-lg border border-slate-700 flex items-center gap-2 transition-colors font-bold text-slate-200"
              >
                <Download className="w-3.5 h-3.5" />
                <span>Export MD</span>
              </button>
              
              <button
                id="export-pdf-btn"
                onClick={downloadPDF}
                disabled={status !== 'completed'}
                className="bg-indigo-600 hover:bg-indigo-500 active:bg-indigo-700 disabled:opacity-40 disabled:hover:bg-indigo-600 text-xs px-3.5 py-2 rounded-lg flex items-center gap-2 transition-colors font-bold text-white shadow"
              >
                <Download className="w-3.5 h-3.5" />
                <span>Export PDF</span>
              </button>
            </div>
          </div>

          <div className="grid grid-cols-1 xl:grid-cols-12 gap-6">
            
            {/* Markdown Viewer */}
            <div 
              id="report-markdown" 
              className="xl:col-span-8 bg-slate-950 border border-slate-900 rounded-lg p-5 max-h-[600px] overflow-y-auto shadow-inner"
            >
              <MarkdownRenderer content={reportMarkdown} />
            </div>
            
            {/* Charts Viewer */}
            <div className="xl:col-span-4 space-y-4">
              <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider">
                Matplotlib Visualizations
              </h3>
              
              <div 
                id="report-charts" 
                className="space-y-4 bg-slate-950 border border-slate-900 rounded-lg p-4 max-h-[600px] overflow-y-auto shadow-inner"
              >
                {charts.length === 0 ? (
                  <div className="text-slate-600 text-xs italic text-center py-20 flex flex-col items-center gap-2">
                    <HelpCircle className="w-6 h-6 text-slate-800" />
                    <span>No generated charts available yet.</span>
                  </div>
                ) : (
                  charts.map((chart, cIdx) => (
                    <div key={cIdx} className="space-y-2 border border-slate-850 p-3 rounded-lg bg-slate-900/40">
                      <div className="text-[10px] font-bold text-slate-400 font-mono truncate">
                        📈 {chart.name}
                      </div>
                      <img 
                        src={`data:image/png;base64,${chart.base64}`} 
                        alt={chart.name} 
                        className="w-full h-auto rounded border border-slate-900 bg-white" 
                      />
                    </div>
                  ))
                )}
              </div>
            </div>

          </div>
        </div>

      </main>

      {/* Footer */}
      <footer className="border-t border-slate-900 bg-slate-950 py-4 text-center text-[10px] text-slate-500 font-semibold uppercase tracking-wider mt-auto">
        Autonomous AI Research Agent • Task 03 Dashboard
      </footer>
    </div>
  );
}
