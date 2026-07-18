# Pattern

Reflexion

Version: 1.0

---

# Goal

Enable AI agents to improve task performance through structured self-evaluation, reflection, and iterative refinement without requiring model retraining.

The Reflexion pattern extends iterative execution by incorporating a deliberate critique phase that identifies mistakes, updates working knowledge, and guides future decisions.

A production Reflexion system should improve quality while preventing repetitive failures and uncontrolled execution loops.

---

# When to Use

Use this pattern whenever

- Tasks involve uncertainty
- Code generation requires validation
- Tool execution may fail
- Long-running workflows exist
- Quality improves through iteration
- Learning from previous attempts is valuable

---

# Problem

Traditional ReAct executes

Reason

↓

Act

↓

Observe

↓

Repeat

If the same mistake occurs repeatedly, the agent has no structured mechanism to improve beyond reacting to observations.

Problems include

- repeated failures
- inefficient retries
- poor adaptation
- low success rate
- excessive token usage

---

# Solution

Introduce a structured reflection phase.

```
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

Repeat
```

Reflection transforms observations into actionable improvements.

---

# Core Principles

Execute

↓

Observe

↓

Critique

↓

Learn

↓

Improve

Reflection should produce concrete changes, not generic comments.

---

# Architecture

```
Goal
 │
 ▼
Reasoner
 │
 ▼
Action
 │
 ▼
Observation
 │
 ▼
Reflection Engine
 │
 ▼
Updated Context
 │
 ▼
Reasoner
```

---

# Components

## Reasoner

Responsible for

- selecting actions
- interpreting context
- deciding next steps

---

## Executor

Responsible for

- tool execution
- code generation
- API calls
- workflow execution

---

## Observation Engine

Collects

- tool outputs
- test results
- logs
- errors
- retrieved knowledge

---

## Reflection Engine

Responsible for

- identifying failures
- explaining root causes
- proposing improvements
- updating working memory

---

## Validator

Confirms

- correctness
- task completion
- policy compliance

---

# Execution Lifecycle

Goal

↓

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

Validate

↓

Complete

---

# Reflection Triggers

Reflect after

- failed execution
- failed tests
- unexpected observations
- low confidence
- repeated retries
- human feedback
- policy violations

Reflection should not occur after every trivial action.

---

# Reflection Questions

Examples

- What went wrong?
- Why did it happen?
- What assumptions failed?
- Which evidence contradicts my reasoning?
- What should change next?
- Can another strategy work better?

---

# Reflection Outputs

Generate

- root cause
- confidence score
- improvement plan
- memory update
- retry recommendation

Reflection outputs should be structured.

---

# Memory Integration

Store

- successful strategies
- failed approaches
- useful observations
- execution history

Avoid repeating previously unsuccessful actions.

---

# Confidence Estimation

Estimate

High

↓

Continue

Medium

↓

Reflect briefly

Low

↓

Deep reflection

↓

Possible human escalation

---

# Failure Recovery

Failure

↓

Observation

↓

Reflection

↓

Replan

↓

Retry

↓

Validation

↓

Complete

Reflection should influence future decisions.

---

# Reflection Granularity

## Step-Level

Reflect after each significant action.

Useful for debugging.

---

## Task-Level

Reflect after completing an entire task.

Recommended default.

---

## Workflow-Level

Reflect after an entire workflow finishes.

Useful for long-running automation.

---

# Pattern References

## ReAct

Provides execution loop.

Reflexion extends ReAct with learning.

---

## Planner–Executor

Planner incorporates reflection into future plans.

---

## Supervisor–Worker

Supervisor evaluates worker performance and adapts future delegation.

---

# Engineering Decisions

## Lightweight Reflection

Short critiques.

Fast.

Suitable for production.

---

## Deep Reflection

Comprehensive analysis.

Useful for difficult reasoning tasks.

Higher latency.

---

## Continuous Reflection

Reflection after every step.

Useful for research.

Expensive.

---

## Event-Driven Reflection

Reflect only after significant events.

Recommended default.

---

# Runtime Architecture

```
Goal

↓

Reasoner

↓

Executor

↓

Observation

↓

Reflection Engine

↓

Memory Update

↓

Reasoner
```

---

# Performance

Optimize

reflection latency

↓

memory quality

↓

retry count

↓

token usage

↓

improvement rate

↓

validation cost

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Lightweight reflection | Fast | Less insight |
| Deep reflection | Better quality | Higher latency |
| Continuous reflection | Maximum learning | Expensive |
| Event-driven reflection | Balanced | Trigger tuning required |

---

# Common Failures

- generic reflections
- repeating identical critiques
- no memory updates
- reflecting too often
- reflecting too rarely
- incorrect root cause analysis

---

# Best Practices

- Base reflections on evidence.
- Generate actionable improvements.
- Store useful lessons.
- Prevent repeated failures.
- Trigger reflection selectively.
- Validate improvements objectively.
- Measure reflection effectiveness.
- Keep critiques concise.

---

# Anti-Patterns

❌ Reflecting without observations

❌ Generic self-praise

❌ Ignoring failed attempts

❌ Infinite reflection loops

❌ Updating memory without validation

❌ Treating reflection as reasoning

❌ No measurable improvements

---

# Comparison

| Pattern | Strength | Weakness |
|----------|----------|----------|
| ReAct | Fast iterative execution | No explicit learning |
| Reflexion | Learns from mistakes | Additional latency |
| ReWOO | Efficient planning | Less adaptive |
| CodeAct | Code execution | Narrower domain |
| LLM Compiler | Optimized workflows | More planning overhead |

---

# Real-World Examples

## Reflexion (Research)

Introduces verbal self-feedback that improves future iterations without updating model weights.

---

## Claude Code

Uses compiler errors, test failures, and execution feedback to revise implementations before continuing.

---

## OpenHands

Analyzes execution failures, adjusts implementation strategy, and retries using updated context.

---

## Devin

Reviews completed work, diagnoses failures, and adapts future execution plans within long-running tasks.

---

## SWE-Agent

Uses execution results and test outcomes to guide iterative improvements until objectives are met.

---

# Related Skills

- reflection.md
- self_correction.md
- reasoning.md
- evaluation.md

---

# Related Patterns

- react.md
- planner_executor.md
- supervisor_worker.md
- rewoo.md
- codeact.md

---

# Definition of Done

A Reflexion implementation is production-ready only if

✓ Reflection is triggered by meaningful execution events

✓ Critiques are evidence-based and actionable

✓ Memory captures validated lessons

✓ Future reasoning incorporates reflection outcomes

✓ Reflection reduces repeated failures over time

✓ Validation confirms measurable improvements

✓ Reflection remains bounded to prevent unnecessary overhead

✓ Execution history is observable through logs and metrics

✓ Human escalation is supported for persistent failures

✓ The agent consistently improves its performance through structured self-evaluation rather than blind retries