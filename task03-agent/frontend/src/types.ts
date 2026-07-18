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
  cumulative_usd?: number;
}

export interface ChartItem {
  name: string;
  base64: string;
}
