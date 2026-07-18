# Skill

Task Decomposition

Version: 1.0

---

# Goal

Design reliable task decomposition systems that transform complex goals into structured, executable subtasks while preserving dependencies, priorities, constraints, and opportunities for parallel execution.

Task decomposition enables agents to solve problems that are too large or complex to execute as a single step.

---

# When to Load

Load this skill whenever building

- AI Agents
- Coding Agents
- Enterprise Workflows
- Research Systems
- Multi-Agent Systems
- Long-running Automation

---

# Prerequisites

- planning.md
- reasoning.md
- state_management.md
- tool_calling.md

---

# Core Principles

Large Goal

↓

Break Down

↓

Prioritize

↓

Resolve Dependencies

↓

Execute

↓

Verify

↓

Complete

Every task should be independently executable and measurable.

---

# Responsibilities

Task Decomposition should

- Analyze goals
- Identify subtasks
- Resolve dependencies
- Enable parallel work
- Minimize coupling
- Support replanning

Task Decomposition should not

- Execute tasks
- Store memory
- Call tools directly

---

# Why Decomposition Matters

Without decomposition

- Large prompts fail
- Progress cannot be tracked
- Failures require restarting
- Parallel execution is impossible

With decomposition

- Smaller reasoning units
- Better observability
- Recovery from failures
- Easier delegation

---

# Decomposition Lifecycle

```
Goal

↓

Analyze

↓

Identify Tasks

↓

Estimate Complexity

↓

Resolve Dependencies

↓

Create Execution Plan

↓

Execute

↓

Validate

↓

Complete
```

---

# Hierarchical Decomposition

```
Build SaaS

↓

Backend

Frontend

Infrastructure

↓

Authentication

Database

API

Deployment
```

Large objectives become trees.

---

# Dependency Graph

```
Database

↓

Authentication

↓

API

↓

Frontend
```

Dependencies determine execution order.

---

# Directed Acyclic Graph (DAG)

Whenever possible represent workflows as DAGs.

Advantages

- Parallel execution
- Dependency resolution
- Easier recovery
- Better scheduling

Avoid circular dependencies.

---

# Granularity

Tasks should be

Small enough to execute

Large enough to matter

Poor example

```
Build Application
```

Better

- Design API
- Implement Authentication
- Write Tests
- Deploy Service

---

# Task Prioritization

Rank tasks using

Business Value

↓

Dependencies

↓

Risk

↓

Complexity

↓

Estimated Duration

Critical tasks should execute first.

---

# Sequential Tasks

```
Create Database

↓

Run Migrations

↓

Deploy API
```

Required when outputs depend on previous steps.

---

# Parallel Tasks

```
Frontend

+

Backend

+

Documentation

↓

Integration
```

Use parallelism whenever dependencies allow.

---

# Dynamic Replanning

If a task fails

```
Failure

↓

Analyze

↓

Modify Plan

↓

Continue
```

Never restart the entire workflow unnecessarily.

---

# Task Metadata

Every task should include

- ID
- Name
- Goal
- Description
- Owner
- Dependencies
- Priority
- Estimated Cost
- Estimated Duration
- Status
- Retry Policy

---

# Complexity Estimation

Estimate

Token Cost

↓

Execution Time

↓

Risk

↓

Tool Usage

↓

Human Approval

Use estimates for scheduling.

---

# Pattern References

## Planner Executor

Planner creates task graph.

Executor performs tasks.

See

patterns/planner_executor.md

---

## Supervisor Worker

Supervisor assigns subtasks.

Workers execute independently.

See

patterns/supervisor_worker.md

---

## Map Reduce

Large task

↓

Many workers

↓

Merge Results

See

patterns/map_reduce.md

---

## Router

Choose execution path.

See

patterns/router.md

---

# Engineering Decisions

## Linear Decomposition

Use when

Tasks depend heavily on one another.

Advantages

Simple

Predictable

Trade-off

Lower throughput.

---

## Tree-Based Decomposition

Use when

Large hierarchical goals.

Recommended for software projects.

---

## DAG Execution

Use when

Dependencies exist but parallel execution is possible.

Recommended default.

---

## Dynamic Decomposition

Use when

Requirements change during execution.

Useful for autonomous agents.

---

# Runtime Architecture

```
Goal

↓

Task Analyzer

↓

Task Graph

↓

Scheduler

↓

Workers

↓

Results

↓

Verification
```

---

# Performance Considerations

Optimize

Task generation

↓

Dependency resolution

↓

Parallelism

↓

Scheduling

↓

Failure recovery

↓

Resource utilization

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Linear | Simple | Slow |
| Tree | Organized | More planning |
| DAG | Parallel | Higher complexity |
| Dynamic | Flexible | Continuous replanning |

---

# Security

Protect against

- Unauthorized task execution
- Invalid dependencies
- Infinite task generation
- Circular workflows
- Privilege escalation

Validate every generated task.

---

# Observability

Track

Task creation

↓

Queue time

↓

Execution time

↓

Retries

↓

Failures

↓

Completion rate

↓

Dependency resolution

---

# Metrics

Monitor

Tasks Per Goal

Average Task Duration

Parallelism Ratio

Dependency Resolution Time

Task Success Rate

Retry Rate

Workflow Completion Rate

Scheduling Efficiency

---

# Common Failures

- Tasks too large
- Tasks too small
- Circular dependencies
- Poor prioritization
- Duplicate work
- Ignoring dependencies
- No replanning

---

# Best Practices

- Keep tasks independently executable.
- Prefer DAGs over rigid sequences.
- Track dependencies explicitly.
- Estimate task complexity.
- Enable replanning.
- Validate task graphs.
- Use metadata for scheduling.
- Measure decomposition quality.

---

# Anti-Patterns

❌ Giant monolithic tasks

❌ Circular dependencies

❌ Hidden task relationships

❌ No prioritization

❌ Duplicate subtasks

❌ Static plans for dynamic environments

❌ Ignoring execution costs

---

# Real-World Production Examples

## Claude Code

- Breaks software requests into search, edit, test, and verification phases.
- Replans tasks when tests fail.

---

## Devin

- Constructs long-horizon task plans.
- Continuously updates task graphs based on execution results.

---

## OpenHands

- Splits coding work into repository analysis, implementation, testing, and validation.
- Supports iterative task refinement.

---

## LangGraph

- Represents workflows as graphs with explicit dependencies.
- Enables resumable execution through graph checkpoints.

---

## Apache Airflow

- Uses DAGs to schedule and execute dependent tasks.
- Prevents circular dependencies and tracks execution state.

---

# Testing

Verify

Task generation

Dependency resolution

Priority ordering

Parallel execution

Failure recovery

Dynamic replanning

Metadata validation

Workflow completion

---

# Review Checklist

□ Goals decompose into executable tasks

□ Dependencies are explicit

□ DAG validation implemented

□ Parallel execution supported

□ Priorities assigned

□ Metadata complete

□ Replanning supported

□ Metrics configured

□ Observability enabled

□ Tests passing

---

# Related Skills

- workflows.md
- delegation.md
- orchestration.md
- multi_agent_systems.md
- state_management.md
- planning.md
- patterns/planner_executor.md
- patterns/supervisor_worker.md
- patterns/map_reduce.md
- patterns/router.md

---

# Definition of Done

A task decomposition system is production-ready only if

✓ Complex goals are transformed into executable subtasks

✓ Dependencies are explicitly modeled

✓ DAGs support safe parallel execution

✓ Tasks include sufficient metadata for scheduling

✓ Dynamic replanning handles changing conditions

✓ Failure recovery avoids unnecessary restarts

✓ Decomposition quality is measurable

✓ Observability tracks task progress

✓ Security validates task generation

✓ Large objectives can be completed reliably through structured execution