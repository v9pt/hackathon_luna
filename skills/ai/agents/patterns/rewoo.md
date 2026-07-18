# Pattern

ReWOO (Reason Without Observation)

Version: 1.0

---

# Goal

Reduce LLM calls by separating planning from execution.

Instead of reasoning after every tool call, the agent first creates a complete execution plan containing variable bindings and tool invocations. The execution engine then carries out that plan before a final synthesis step.

A production ReWOO system should minimize reasoning overhead while maintaining correctness, reproducibility, and scalability.

---

# When to Use

Use this pattern whenever

- Tool calls dominate execution time
- Long workflows exist
- API costs matter
- Large repositories are analyzed
- Enterprise workflows execute repeatedly
- Deterministic execution is preferred

---

# Problem

ReAct performs

Reason

↓

Tool

↓

Reason

↓

Tool

↓

Reason

↓

Tool

Every tool call requires another LLM invocation.

Problems

- High token usage
- Increased latency
- Expensive execution
- Difficult reproducibility

---

# Solution

Separate planning and execution.

```
Reason Once

↓

Execution Plan

↓

Tool Execution

↓

Final Reasoning

↓

Complete
```

Reasoning becomes independent from intermediate observations.

---

# Core Principles

Plan First

↓

Execute Sequentially

↓

Collect Results

↓

Synthesize

Planning and execution should remain separate.

---

# Architecture

```
Goal
 │
 ▼
Planner
 │
 ▼
Execution Program
 │
 ▼
Executor
 │
 ▼
Results
 │
 ▼
Solver
 │
 ▼
Response
```

---

# Components

## Planner

Responsible for

- understanding objectives
- decomposing work
- generating execution programs
- assigning variables

Planner executes only once.

---

## Execution Program

Contains

- ordered tool calls
- dependencies
- variable references
- execution metadata

Execution programs should be deterministic.

---

## Executor

Responsible for

- invoking tools
- resolving variables
- handling retries
- collecting outputs

Executor does not reason.

---

## Solver

Responsible for

- combining execution results
- producing the final answer
- validating completion

---

# Execution Lifecycle

Goal

↓

Planning

↓

Execution Program

↓

Tool Execution

↓

Result Collection

↓

Final Synthesis

↓

Validation

↓

Complete

---

# Variable Binding

Instead of reasoning repeatedly

Store intermediate results.

Example

```
E1 = Search(API Docs)

E2 = Read(E1)

E3 = Summarize(E2)

Final = Generate(E3)
```

Later steps reference variables rather than requiring additional reasoning.

---

# Dependency Graph

Execution forms a Directed Acyclic Graph (DAG).

```
Search

↓

Read

↓

Extract

↓

Summarize
```

Independent branches may execute in parallel.

---

# Parallel Execution

If two variables have no dependency

```
E1

+

E2

↓

Merge

↓

Continue
```

Improves throughput.

---

# Failure Recovery

If execution fails

Retry

↓

Alternative Tool

↓

Planner Re-execution (only if necessary)

↓

Escalation

Avoid rebuilding the entire execution program unless dependencies change.

---

# Engineering Decisions

## Static Planning

Single execution program.

Best for deterministic workflows.

---

## Adaptive Replanning

Rebuild the execution plan only after major failures.

Recommended default.

---

## Variable-Based Execution

Preferred over free-form reasoning.

Improves reproducibility.

---

## DAG Execution

Recommended.

Supports parallelism and checkpointing.

---

# Runtime Architecture

```
User Goal

↓

Planner

↓

Execution Graph

↓

Executor

↓

Variable Store

↓

Solver

↓

Validator

↓

Complete
```

---

# Performance

Optimize

planning latency

↓

execution throughput

↓

parallel execution

↓

token usage

↓

retry frequency

↓

program size

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| ReAct | Highly adaptive | Many LLM calls |
| ReWOO | Lower cost | Less adaptive during execution |
| Planner + ReWOO | Efficient | Larger upfront planning |
| Dynamic Replanning | Flexible | Additional complexity |

---

# Common Failures

- poor initial planning
- invalid variable references
- dependency cycles
- stale execution plans
- unnecessary replanning
- oversized execution graphs

---

# Best Practices

- Generate explicit execution programs.
- Use variable references instead of repeated reasoning.
- Validate dependency graphs.
- Execute independent branches in parallel.
- Retry individual steps before replanning.
- Version execution programs.
- Measure planning quality.
- Keep execution deterministic.

---

# Anti-Patterns

❌ Reasoning after every tool call

❌ Hidden execution order

❌ Mutable execution plans

❌ Circular dependencies

❌ Replanning after every failure

❌ Ignoring variable reuse

❌ Non-deterministic execution

---

# Comparison

| Pattern | Strength | Weakness |
|----------|----------|----------|
| ReAct | Adaptive | Expensive |
| ReWOO | Efficient | Less adaptive |
| Reflexion | Learns from failures | Additional reflection cost |
| LLM Compiler | Optimizes workflows | More infrastructure |
| CodeAct | Code-centric execution | Narrower scope |

---

# Real-World Examples

## ReWOO (Research)

Introduces reasoning once, followed by variable-based execution and final synthesis to reduce LLM calls.

---

## LangGraph

Supports graph-based execution where planned nodes execute independently before aggregation.

---

## Enterprise AI Pipelines

Generate execution plans for document processing, retrieval, and reporting before dispatching work to workers.

---

## Large RAG Systems

Plan retrieval, reranking, filtering, and synthesis before executing retrieval operations.

---

## Coding Agents

Analyze repositories, build execution plans, execute searches, run tests, and synthesize implementation without repeated planning after every command.

---

# Related Skills

- planning.md
- orchestration.md
- task_decomposition.md
- workflows.md

---

# Related Patterns

- react.md
- planner_executor.md
- llm_compiler.md
- codeact.md
- reflexion.md

---

# Definition of Done

A ReWOO implementation is production-ready only if

✓ Planning occurs independently of execution

✓ Execution programs are explicit and versioned

✓ Variable bindings eliminate unnecessary reasoning

✓ Dependency graphs are validated before execution

✓ Independent tasks execute in parallel where possible

✓ Failures trigger targeted retries before replanning

✓ Final synthesis combines validated execution results

✓ Token usage and latency are measurably reduced compared to ReAct

✓ Execution remains observable through logs, metrics, and traces

✓ Complex workflows execute efficiently while preserving correctness and reproducibility