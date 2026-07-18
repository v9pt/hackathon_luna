import type { ReactNode } from 'react';


interface MarkdownProps {
  content: string;
}

export default function MarkdownRenderer({ content }: MarkdownProps) {
  if (!content) {
    return <div className="text-slate-500 italic">No report content generated yet.</div>;
  }

  // Parse inline styles like **bold**, *italic*, and `code`
  const renderTextWithInlineFormatting = (text: string) => {
    // Matches **bold**, *italic*, and `code`


    // Matches **bold**, *italic*, and `code`
    const regex = /(\*\*.*?\*\*|\*.*?\*|`.*?`)/g;
    const matches = text.split(regex);

    return matches.map((part, index) => {
      if (part.startsWith('**') && part.endsWith('**')) {
        return <strong key={index} className="font-bold text-white">{part.slice(2, -2)}</strong>;
      }
      if (part.startsWith('*') && part.endsWith('*')) {
        return <em key={index} className="italic text-slate-300">{part.slice(1, -1)}</em>;
      }
      if (part.startsWith('`') && part.endsWith('`')) {
        return (
          <code key={index} className="bg-slate-900 border border-slate-800 text-pink-400 px-1.5 py-0.5 rounded font-mono text-xs">
            {part.slice(1, -1)}
          </code>
        );
      }
      return part;
    });
  };

  const lines = content.split('\n');
  const renderedElements: ReactNode[] = [];


  let isInsideCodeBlock = false;
  let codeBlockLanguage = '';
  let codeBlockLines: string[] = [];

  let isInsideTable = false;
  let tableRows: string[][] = [];

  const flushCodeBlock = (key: string | number) => {
    const codeText = codeBlockLines.join('\n');
    renderedElements.push(
      <div key={`code-${key}`} className="my-4 border border-slate-800 rounded-lg overflow-hidden font-mono text-xs bg-slate-950">
        {codeBlockLanguage && (
          <div className="bg-slate-900 px-4 py-1.5 text-[10px] text-slate-500 font-semibold border-b border-slate-800 uppercase tracking-wider">
            {codeBlockLanguage}
          </div>
        )}
        <pre className="p-4 overflow-x-auto text-emerald-400 leading-relaxed">{codeText}</pre>
      </div>
    );
    codeBlockLines = [];
    isInsideCodeBlock = false;
    codeBlockLanguage = '';
  };

  const flushTable = (key: string | number) => {
    if (tableRows.length === 0) return;
    
    // Check if the second row is a separator (e.g. |---|---|)
    let headerRow: string[] | null = null;
    let dataRows: string[][] = [];
    
    if (tableRows.length > 1 && tableRows[1].every(cell => cell.includes('-') && cell.replace(/-/g, '').length === 0)) {
      headerRow = tableRows[0];
      dataRows = tableRows.slice(2);
    } else {
      dataRows = tableRows;
    }

    renderedElements.push(
      <div key={`table-${key}`} className="overflow-x-auto my-4 border border-slate-800 rounded-lg shadow-sm">
        <table className="min-w-full divide-y divide-slate-800 bg-slate-950/20">
          {headerRow && (
            <thead className="bg-slate-900">
              <tr>
                {headerRow.map((cell, idx) => (
                  <th key={idx} className="px-4 py-2.5 text-left text-xs font-bold text-slate-400 uppercase tracking-wider border-b border-slate-800">
                    {renderTextWithInlineFormatting(cell)}
                  </th>
                ))}
              </tr>
            </thead>
          )}
          <tbody className="divide-y divide-slate-850">
            {dataRows.map((row, rIdx) => (
              <tr key={rIdx} className="hover:bg-slate-900/30">
                {row.map((cell, cIdx) => (
                  <td key={cIdx} className="px-4 py-2.5 text-xs text-slate-300 font-medium">
                    {renderTextWithInlineFormatting(cell)}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );

    tableRows = [];
    isInsideTable = false;
  };

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();

    // 1. Handle Code Blocks
    if (trimmed.startsWith('```')) {
      if (isInsideCodeBlock) {
        flushCodeBlock(i);
      } else {
        isInsideCodeBlock = true;
        codeBlockLanguage = trimmed.slice(3).trim();
      }
      continue;
    }

    if (isInsideCodeBlock) {
      codeBlockLines.push(line);
      continue;
    }

    // 2. Handle Tables
    if (trimmed.startsWith('|') && trimmed.endsWith('|')) {
      if (!isInsideTable) {
        isInsideTable = true;
        tableRows = [];
      }
      // Split by pipe and remove empty first/last elements
      const cells = line.split('|').map(c => c.trim());
      cells.shift();
      cells.pop();
      tableRows.push(cells);
      continue;
    } else {
      if (isInsideTable) {
        flushTable(i);
      }
    }

    // 3. Headers
    if (trimmed.startsWith('# ')) {
      renderedElements.push(
        <h1 key={i} className="text-xl font-bold text-white border-b border-slate-800 pb-2 mt-6 mb-4 flex items-center gap-2">
          {renderTextWithInlineFormatting(trimmed.substring(2))}
        </h1>
      );
      continue;
    }
    if (trimmed.startsWith('## ')) {
      renderedElements.push(
        <h2 key={i} className="text-lg font-bold text-slate-100 mt-5 mb-3 flex items-center gap-2">
          {renderTextWithInlineFormatting(trimmed.substring(3))}
        </h2>
      );
      continue;
    }
    if (trimmed.startsWith('### ')) {
      renderedElements.push(
        <h3 key={i} className="text-base font-bold text-slate-200 mt-4 mb-2">
          {renderTextWithInlineFormatting(trimmed.substring(4))}
        </h3>
      );
      continue;
    }

    // 4. Bullet lists
    if (trimmed.startsWith('- ') || trimmed.startsWith('* ')) {
      renderedElements.push(
        <li key={i} className="ml-5 list-disc text-xs text-slate-300 my-1.5 leading-relaxed">
          {renderTextWithInlineFormatting(trimmed.substring(2))}
        </li>
      );
      continue;
    }

    // 5. Numbered lists
    const numberListMatch = trimmed.match(/^(\d+)\.\s(.*)/);
    if (numberListMatch) {
      renderedElements.push(
        <li key={i} className="ml-5 list-decimal text-xs text-slate-300 my-1.5 leading-relaxed">
          {renderTextWithInlineFormatting(numberListMatch[2])}
        </li>
      );
      continue;
    }

    // 6. Paragraphs / empty lines
    if (trimmed === '') {
      renderedElements.push(<div key={i} className="h-2" />);
    } else {
      renderedElements.push(
        <p key={i} className="text-xs text-slate-300 leading-relaxed my-2">
          {renderTextWithInlineFormatting(line)}
        </p>
      );
    }
  }

  // Flush remaining table or code block at end of file
  if (isInsideTable) flushTable('end');
  if (isInsideCodeBlock) flushCodeBlock('end');

  return <div className="space-y-0.5">{renderedElements}</div>;
}
