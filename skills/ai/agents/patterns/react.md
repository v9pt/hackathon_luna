# Pattern

ReAct (Reason + Act)

Version: 1.0

---

# Goal

Enable AI agents to iteratively reason about a problem, perform actions using tools or external systems, observe the results, and continue reasoning until the objective is achieved.

Rather than producing a single response, ReAct alternates between thinking and acting, allowing the agent to adapt based on real-world feedback.

ReAct is one of the foundational execution patterns for modern AI agents.

---

# When to Use

Use this pattern whenever

- External tools are required
- Information is incomplete
- Tasks require multiple steps
- Intermediate observations influence future decisions
- Dynamic environments are involved
- Verification is necessary

---

# Problem

Traditional prompting follows

Input

↓

Reason

↓

Output

This assumes all required knowledge already exists.

In reality, many tasks require

- searching
- reading files
- querying databases
- browsing documentation
- executing code
- validating results

Static reasoning cannot adapt once new information appears.

---

# Solution

Alternate reasoning and action.

```
Reason

↓

Act

↓

Observe

↓

Reason

↓

Act

↓

Observe

↓

Complete
```

Each observation becomes part of the next reasoning step.

---

# Core Principles

Reasoning guides actions.

Actions produce observations.

Observations improve reasoning.

Continue until objective completion.

---

# Architecture

```
Goal
 │
 ▼
Reason
 │
 ▼
Action
 │
 ▼
Tool
 │
 ▼
Observation
 │
 ▼
Reason
 │
 ▼
Repeat
```

---

# Components

## Reasoner

Responsible for

- understanding objectives
- selecting next action
- interpreting observations
- deciding completion

Should not directly manipulate external systems.

---

## Action Executor

Responsible for

- tool invocation
- API requests
- shell execution
- database operations
- file editing

Should execute only approved actions.

---

## Observation Processor

Responsible for

- parsing results
- extracting evidence
- detecting failures
- updating execution context

Observations should be structured whenever possible.

---

# Execution Lifecycle

Goal

↓

Reason

↓

Action

↓

Observation

↓

Reason

↓

Action

↓

Observation

↓

Validation

↓

Complete

---

# Action Types

Examples

- Search
- Read
- Write
- Execute
- Query
- Retrieve
- Compute
- Generate
- Validate

Actions should be deterministic whenever possible.

---

# Observation Types

Examples

- Tool output
- Test results
- API responses
- Error messages
- Retrieved documents
- User feedback

Observations become evidence for subsequent reasoning.

---

# Stopping Conditions

Terminate when

- Goal achieved
- Validation succeeds
- Confidence threshold reached
- Budget exhausted
- Human approval required
- Safety policy blocks execution

Avoid infinite execution loops.

---

# Error Handling

If an action fails

Observe failure

↓

Reason

↓

Choose

Retry

Alternative tool

Replan

Escalate

↓

Continue

Failures should influence subsequent reasoning.

---

# Tool Selection

The reasoner should evaluate

- Required capability
- Tool availability
- Cost
- Latency
- Permissions
- Reliability

Choose the simplest tool that satisfies the objective.

---

# Memory Integration

Maintain

- Goal
- Completed actions
- Observations
- Pending tasks
- Tool history

Avoid repeatedly performing identical actions.

---

# Pattern Variants

## Basic ReAct

Reason

↓

Act

↓

Observe

↓

Repeat

Suitable for small workflows.

---

## ReAct with Reflection

Reason

↓

Act

↓

Observe

↓

Reflect

↓

Improve

↓

Continue

Useful for coding agents.

---

## ReAct with Planner

Planner

↓

ReAct Executor

↓

Validation

Recommended for enterprise systems.

---

## Multi-Agent ReAct

Supervisor

↓

Worker ReAct Loops

↓

Aggregation

Useful for distributed execution.

---

# Engineering Decisions

## Free-form Reasoning

Flexible.

Harder to validate.

---

## Structured Reasoning

Recommended.

Produces machine-readable intermediate state.

---

## Single Tool Per Step

Simple.

Easy to debug.

Recommended default.

---

## Parallel Actions

Useful when actions are independent.

Requires orchestration.

---

# Runtime Architecture

```
User Goal
     │
     ▼
Reasoner
     │
     ▼
Action Selector
     │
     ▼
Tool Runtime
     │
     ▼
Observation
     │
     ▼
Reasoner
```

---

# Performance

Optimize

- reasoning latency
- tool latency
- observation parsing
- duplicate actions
- loop count
- token usage

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Basic ReAct | Simple | Limited planning |
| Structured ReAct | Reliable | More implementation effort |
| Planner + ReAct | Scalable | Higher orchestration complexity |
| Parallel ReAct | Faster | Coordination overhead |

---

# Common Failures

- Infinite loops
- Repeating failed actions
- Ignoring observations
- Selecting incorrect tools
- Hallucinating tool results
- Missing stopping conditions

---

# Best Practices

- Keep reasoning explicit.
- Validate every observation.
- Prefer structured tool outputs.
- Log every action.
- Avoid repeated failures.
- Support replanning.
- Enforce execution budgets.
- Use objective stopping conditions.

---

# Anti-Patterns

❌ Acting without reasoning

❌ Ignoring observations

❌ Hallucinating tool responses

❌ Infinite loops

❌ Hidden intermediate state

❌ Excessive tool usage

❌ No validation

---

# Comparison

| Pattern | Strength | Weakness |
|----------|----------|----------|
| ReAct | Flexible | Higher token usage |
| ReWOO | Efficient | Less adaptive |
| Reflexion | Self-improving | Additional latency |
| CodeAct | Code-centric | Specialized domain |
| LLM Compiler | Optimized execution | More complex planning |

---

# Real-World Examples

## Claude Code

Uses iterative reasoning to inspect repositories, edit files, execute tests, observe failures, and refine subsequent actions until the implementation is complete.

---

## OpenAI Codex

Alternates between planning code edits, executing commands, interpreting outputs, and refining future actions based on execution results.

---

## OpenHands

Continuously reasons over repository state, invokes tools, evaluates outputs, and updates execution strategy throughout a task.

---

## LangGraph

Implements ReAct as graph nodes connected by observations and state transitions, enabling checkpointing and resumable execution.

---

## Cursor

Uses reasoning to determine edits, applies changes, observes compiler or test feedback, and iteratively improves code.

---

# Related Skills

- reasoning.md
- tool_calling.md
- reflection.md
- self_correction.md
- planning.md
- orchestration.md

---

# Related Patterns

- planner_executor.md
- reflexion.md
- rewoo.md
- codeact.md
- llm_compiler.md

---

# Definition of Done

A ReAct implementation is production-ready only if

✓ Reasoning and actions alternate through explicit iterations

✓ Tool invocations are based on structured reasoning

✓ Observations are validated before influencing future decisions

✓ Memory prevents redundant actions

✓ Error handling supports retries, replanning, and escalation

✓ Stopping conditions prevent infinite loops

✓ Execution remains observable through logs and metrics

✓ Tool usage respects permissions and policies

✓ Validation confirms objective completion

✓ The agent reliably adapts its behavior using evidence gathered during execution