# Skill

Planning

Version: 1.0

---

# Goal

Design intelligent planning systems that transform high-level goals into executable, observable, and adaptable workflows.

Planning enables agents to decompose complex objectives, manage dependencies, recover from failures, and optimize execution.

A production agent should think before acting.

---

# When to Load

Load this skill whenever building

- AI Agents
- Coding Agents
- Research Agents
- Workflow Automation
- Multi-Agent Systems
- Enterprise AI

---

# Prerequisites

- fundamentals.md
- agent_architecture.md

---

# Core Principles

Planning bridges the gap between

Goal

↓

Strategy

↓

Tasks

↓

Execution

↓

Evaluation

Planning should produce actions—not answers.

---

# Responsibilities

A planner should

- Understand goals
- Break work into tasks
- Identify dependencies
- Estimate complexity
- Prioritize execution
- Adapt to failures
- Determine completion

A planner should not

- Execute tools
- Generate final responses
- Store long-term memory

---

# Planning Architecture

```
User Goal

↓

Goal Analysis

↓

Task Decomposition

↓

Dependency Graph

↓

Execution Plan

↓

Executor

↓

Evaluation

↓

Replan (if required)
```

Planning is an iterative process.

---

# Planning Levels

## Strategic Planning

Long-term objectives.

Examples

- Build an application
- Research a topic
- Deploy infrastructure

---

## Tactical Planning

Intermediate milestones.

Examples

- Build backend
- Create API
- Write tests

---

## Operational Planning

Immediate executable actions.

Examples

- Call API
- Read file
- Execute command
- Generate code

---

# Planning Lifecycle

```
Goal

↓

Analyze

↓

Decompose

↓

Prioritize

↓

Estimate

↓

Execute

↓

Observe

↓

Evaluate

↓

Replan
```

---

# Goal Analysis

Every goal should answer

What needs to be achieved?

↓

What information is missing?

↓

Which tools are required?

↓

What constraints exist?

↓

How will success be measured?

---

# Task Decomposition

Large objectives become smaller tasks.

Example

```
Build Authentication System

↓

Database Schema

↓

JWT Service

↓

Login Endpoint

↓

Middleware

↓

Tests

↓

Documentation
```

Tasks should be independently executable.

---

# Dependency Graph

Identify execution order.

```
Database

↓

Authentication

↓

API

↓

Frontend

↓

Testing
```

Independent tasks may execute in parallel.

---

# Prioritization

Rank tasks by

Criticality

↓

Dependencies

↓

Risk

↓

Estimated effort

↓

Business value

Always unblock dependent work first.

---

# Parallel Planning

Independent tasks should execute concurrently.

Example

```
Backend API

+

Frontend UI

+

Documentation

↓

Merge Results
```

Parallelism reduces total completion time.

---

# Dynamic Replanning

Plans should evolve.

Trigger replanning when

- Tool failures
- New information
- User changes goal
- Missing dependencies
- Validation failures

Never assume the original plan remains optimal.

---

# Incremental Planning

Instead of planning everything upfront

Plan

↓

Execute

↓

Observe

↓

Extend Plan

Useful for uncertain environments.

---

# Long-Horizon Planning

Large objectives require hierarchical planning.

Example

```
Launch Product

↓

Backend

↓

Frontend

↓

Infrastructure

↓

QA

↓

Deployment
```

Each milestone generates its own subplan.

---

# Constraint Handling

Consider

Deadlines

↓

Budgets

↓

Permissions

↓

Resource limits

↓

Rate limits

↓

Compliance

Plans must respect operational constraints.

---

# Engineering Decisions

## Linear Planning

Use when

Simple workflows

Short tasks

Few dependencies

Advantages

Simple

Predictable

Trade-off

Limited flexibility.

---

## Hierarchical Planning

Use when

Large software projects

Research

Enterprise automation

Recommended default.

---

## Dynamic Planning

Use when

Long-running agents

Changing requirements

Interactive systems

Trade-off

Higher computational cost.

---

## Parallel Planning

Use when

Independent tasks exist

Multiple agents available

Large workflows

Improves throughput.

---

# Planner Patterns

## Sequential Planner

Task A

↓

Task B

↓

Task C

Simple but slower.

---

## Tree Planner

Goal

↓

Subgoals

↓

Tasks

↓

Actions

Recommended for complex objectives.

---

## Graph Planner

Tasks connected by dependencies.

Supports

Parallel execution

Conditional execution

Recovery

Best for enterprise workflows.

---

# Failure Recovery

When execution fails

Retry

↓

Alternative Tool

↓

Replan

↓

Escalate

↓

Abort

Planning should never stop after one failure.

---

# Planning Metrics

Measure

Plan generation time

↓

Task completion rate

↓

Average replans

↓

Dependency violations

↓

Execution efficiency

↓

Goal completion rate

---

# Performance Considerations

Optimize

Planning latency

↓

Task granularity

↓

Parallel execution

↓

Resource utilization

↓

Replanning frequency

Balance planning cost against execution cost.

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Linear planning | Simple | No flexibility |
| Hierarchical planning | Scalable | More complexity |
| Dynamic planning | Adaptive | Higher latency |
| Parallel planning | Faster execution | Coordination overhead |

---

# Security

Validate

User permissions

↓

Tool permissions

↓

Execution limits

↓

Resource quotas

↓

Approval requirements

Planning should never authorize actions beyond policy.

---

# Observability

Track

Planning time

↓

Task graph size

↓

Replanning frequency

↓

Dependency failures

↓

Execution progress

↓

Completion status

---

# Metrics

Monitor

Planning Latency

Average Plan Size

Task Success Rate

Goal Completion Rate

Replan Frequency

Parallel Task Utilization

Average Execution Time

Cost Per Goal

---

# Common Failures

- Overplanning simple tasks
- Underplanning complex objectives
- Ignoring dependencies
- No replanning
- Infinite planning loops
- Tiny unnecessary tasks
- Missing success criteria

---

# Best Practices

- Define measurable goals.
- Keep plans modular.
- Prefer hierarchical planning.
- Support dynamic replanning.
- Execute independent tasks in parallel.
- Validate assumptions continuously.
- Measure planning quality.
- Separate planning from execution.

---

# Anti-Patterns

❌ Acting immediately without planning

❌ One massive plan for every task

❌ Ignoring dependency graphs

❌ No replanning

❌ Hardcoded workflows

❌ Planning without evaluation

❌ Unlimited autonomous execution

---

# Real-World Production Examples

## Claude Code

- Creates a plan before modifying repositories.
- Updates the plan as new information is discovered.
- Revisits completed steps when validation fails.

---

## Devin

- Generates long-horizon software engineering plans.
- Tracks progress across multiple milestones.
- Replans after failed builds or tests.

---

## OpenHands

- Breaks software tasks into executable development steps.
- Continuously validates progress through execution feedback.

---

## LangGraph

- Represents plans as executable state graphs.
- Supports branching, retries, and conditional execution.

---

# Testing

Verify

Goal decomposition

Dependency graph correctness

Parallel execution

Replanning

Constraint handling

Failure recovery

Task prioritization

Completion validation

---

# Review Checklist

□ Goal analysis implemented

□ Task decomposition completed

□ Dependency graph generated

□ Planning strategy selected

□ Replanning supported

□ Parallel execution identified

□ Metrics configured

□ Security reviewed

□ Observability enabled

□ Tests passing

---

# Related Skills

- reasoning.md
- task_decomposition.md
- orchestration.md
- workflows.md
- reflection.md

---

# Definition of Done

A planning system is production-ready only if

✓ Goals are transformed into executable plans

✓ Tasks are modular and independently executable

✓ Dependencies are explicitly modeled

✓ Dynamic replanning is supported

✓ Parallel execution opportunities are identified

✓ Constraints are enforced

✓ Planning quality is measurable

✓ Failure recovery is integrated

✓ Planning remains independent from execution

✓ The system consistently achieves complex objectives through adaptive planning