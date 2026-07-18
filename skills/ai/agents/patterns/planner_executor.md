# Pattern

Planner → Executor

Version: 1.0

---

# Goal

Separate planning from execution by assigning one component to determine **what should be done** and another component to perform **how it should be done**.

This separation improves modularity, reliability, observability, and maintainability while enabling dynamic replanning and specialized execution.

Planner–Executor is one of the most widely used architectural patterns in modern AI systems, including coding agents, workflow engines, robotics, and autonomous task automation.

---

# When to Use

Use this pattern when

- Tasks require multiple steps
- Planning is more expensive than execution
- Specialized executors exist
- Workflows may change dynamically
- Failures require replanning
- Parallel execution is beneficial

---

# Problem

A single autonomous agent must both

- understand goals
- create plans
- execute tools
- recover failures
- verify outputs

This mixes responsibilities and makes systems

- difficult to debug
- hard to scale
- difficult to observe
- difficult to test

---

# Solution

Separate responsibilities.

Planner

↓

Execution Plan

↓

Executor

↓

Results

↓

Planner (optional replanning)

The planner never executes work.

The executor never creates long-term strategy.

---

# Core Principles

Planning and execution should evolve independently.

Execution should follow an explicit plan.

Planning should remain adaptable based on execution feedback.

---

# Architecture

```text
User Goal
     │
     ▼
 Planner
     │
     ▼
 Task Graph
     │
     ▼
 Executor(s)
     │
     ▼
 Validation
     │
     ▼
 Success / Replan
```

---

# Components

## Planner

Responsible for

- understanding objectives
- decomposing tasks
- dependency analysis
- prioritization
- scheduling
- replanning

Planner should not

- execute tools
- modify files
- access infrastructure directly

---

## Executor

Responsible for

- running tools
- editing code
- querying databases
- calling APIs
- executing shell commands

Executor should not

- redesign workflows
- reprioritize objectives

---

## Validator

Verifies

- correctness
- tests
- policy compliance
- completion

Validation provides objective feedback.

---

# Execution Lifecycle

Goal

↓

Planner

↓

Task Graph

↓

Executor

↓

Validation

↓

Complete

or

↓

Replan

---

# Planning Strategies

Static Planning

Plan once.

Execute completely.

Useful for deterministic workflows.

---

Dynamic Planning

Continuously improve the plan.

Recommended default.

---

Hierarchical Planning

Large goals

↓

Sub-goals

↓

Tasks

↓

Actions

Useful for enterprise systems.

---

# Replanning

Replanning may occur when

- execution fails
- new information appears
- requirements change
- dependencies fail
- validation fails

Only the planner should modify the plan.

---

# Parallel Execution

Planner identifies independent tasks.

Executors perform them concurrently.

Results are merged before validation.

---

# Failure Recovery

If execution fails

Detect

↓

Diagnose

↓

Replan

↓

Retry

↓

Validate

↓

Continue

Failures should not require rebuilding the entire workflow.

---

# Advantages

- Separation of concerns
- Better scalability
- Easier testing
- Improved observability
- Dynamic adaptation
- Supports specialization

---

# Disadvantages

- More infrastructure
- Additional coordination
- Planner latency
- Higher orchestration complexity

---

# Engineering Decisions

## Static Planner

Simple systems

Small workflows

---

## Adaptive Planner

Enterprise AI

Coding agents

Research systems

Recommended.

---

## Centralized Planner

Single authority.

Easy to debug.

---

## Distributed Planning

Multiple planners cooperate.

Higher scalability.

Higher complexity.

---

# Runtime Architecture

```text
Goal
   │
   ▼
 Planner
   │
   ▼
 Task Queue
   │
   ▼
 Executors
   │
   ▼
 Validator
   │
   ▼
 Complete
```

---

# Performance

Optimize

- planning latency
- executor utilization
- replanning frequency
- queue efficiency
- validation overhead

---

# Common Failures

- planner generates unrealistic tasks
- executor modifies plan
- missing validation
- overplanning
- excessive replanning
- hidden dependencies

---

# Best Practices

- Keep planner stateless where possible.
- Keep executors specialized.
- Validate after execution.
- Support replanning.
- Log planning decisions.
- Version execution plans.
- Measure planner quality.

---

# Anti-Patterns

❌ Planner executes tools

❌ Executor changes objectives

❌ No validation

❌ Massive monolithic plans

❌ Hidden dependencies

❌ Infinite replanning

---

# Real-World Examples

## Claude Code

Planner analyzes repository, determines implementation strategy, then execution components edit files, run tests, and validate outcomes.

---

## OpenHands

Planner decomposes repository tasks while executors modify code, run commands, and validate fixes iteratively.

---

## LangGraph

Represents planning as graph construction and execution as node traversal with checkpointing and resumability.

---

## Temporal

Separates durable workflow definitions from executable activities, enabling retries and recovery.

---

## CrewAI

Manager agents create plans while worker agents execute assigned tasks independently.

---

# Related Skills

- planning.md
- workflows.md
- orchestration.md
- delegation.md
- task_decomposition.md
- self_correction.md

---

# Definition of Done

A Planner–Executor implementation is production-ready only if

✓ Planning and execution are fully separated

✓ Execution follows explicit plans

✓ Validation occurs after execution

✓ Replanning is supported

✓ Parallel execution is possible

✓ Planner decisions are observable

✓ Failures trigger controlled recovery

✓ Executors remain specialized

✓ Responsibilities remain clearly separated

✓ Complex goals can be executed reliably at production scale