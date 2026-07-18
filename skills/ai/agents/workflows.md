# Skill

Workflows

Version: 1.0

---

# Goal

Design reliable, repeatable, and observable workflows that coordinate planning, reasoning, tools, state, and memory into structured execution pipelines.

A workflow defines **what work should happen**, **in what order**, and **under what conditions**.

Production workflows should be deterministic where possible and adaptive where necessary.

---

# When to Load

Load this skill whenever building

- AI Agents
- Enterprise Automation
- Coding Agents
- Business Processes
- Research Pipelines
- Multi-Step Workflows
- Multi-Agent Systems

---

# Prerequisites

- planning.md
- reasoning.md
- tool_calling.md
- state_management.md
- task_decomposition.md

---

# Core Principles

Goal

↓

Workflow

↓

Tasks

↓

Execution

↓

Verification

↓

Completion

A workflow should describe the process, not the implementation.

---

# Responsibilities

Workflow systems should

- Define execution order
- Coordinate tasks
- Track progress
- Handle failures
- Trigger retries
- Support checkpoints
- Enable human approval

Workflow systems should not

- Perform reasoning
- Store long-term memory
- Execute business logic directly

---

# Workflow Lifecycle

```
Goal

↓

Planning

↓

Task Generation

↓

Scheduling

↓

Execution

↓

Verification

↓

Completion
```

Every workflow should have a clear beginning and end.

---

# Workflow Components

Every workflow contains

- Goal
- Tasks
- Dependencies
- Conditions
- Inputs
- Outputs
- State
- Error Handling
- Completion Criteria

---

# Workflow Types

## Sequential

```
Task A

↓

Task B

↓

Task C
```

Best for dependent tasks.

---

## Parallel

```
Task A

+

Task B

+

Task C

↓

Merge
```

Best when tasks are independent.

---

## Conditional

```
Validate

↓

Success?

↓

Yes → Continue

No → Retry
```

Useful for validation pipelines.

---

## Loop

```
Execute

↓

Evaluate

↓

Complete?

↓

No

↓

Repeat
```

Useful for iterative refinement.

---

## Event Driven

```
Event

↓

Workflow

↓

Completion
```

Triggered by external systems.

---

# Workflow Graph

Represent workflows as DAGs whenever possible.

```
Plan

↓

Backend

Frontend

↓

Testing

↓

Deployment
```

Avoid cyclic execution.

---

# Scheduling

Schedule tasks using

Dependencies

↓

Priority

↓

Resource Availability

↓

Estimated Cost

↓

Deadlines

Schedulers should maximize throughput while respecting dependencies.

---

# Checkpoints

Checkpoint after

- Task completion
- Human approval
- Tool execution
- External API calls

Enable resumable workflows.

---

# Human Approval

Support approval gates before

- Production deployment
- Payments
- Data deletion
- Infrastructure changes

Humans should remain in control of high-impact decisions.

---

# Retry Strategy

Retry only

- Transient failures
- Timeouts
- Temporary provider errors

Do not retry

- Invalid input
- Authorization failures
- Business rule violations

---

# Workflow Recovery

Recover by

Checkpoint

↓

Restore State

↓

Resume Execution

↓

Verify Results

Avoid restarting completed work.

---

# Workflow Metadata

Every workflow should include

- Workflow ID
- Goal
- Owner
- Status
- Priority
- Tasks
- Dependencies
- Start Time
- End Time
- Retry Policy
- Checkpoints

---

# Pattern References

## Planner Executor

Planner creates workflow.

Executor performs tasks.

See

patterns/planner_executor.md

---

## Supervisor Worker

Supervisor assigns workflow stages.

Workers execute independently.

See

patterns/supervisor_worker.md

---

## Router

Select execution path.

See

patterns/router.md

---

## Map Reduce

Parallel execution

↓

Aggregation

See

patterns/map_reduce.md

---

## ReAct

Reason

↓

Execute

↓

Observe

↓

Continue

See

patterns/react.md

---

# Engineering Decisions

## Sequential Workflow

Use when

Tasks have strict dependencies.

Advantages

Simple

Predictable

---

## Parallel Workflow

Use when

Tasks are independent.

Improves throughput.

---

## Event Driven Workflow

Use when

External systems trigger execution.

Examples

GitHub

Slack

Webhook

Kafka

---

## DAG Workflow

Recommended default.

Supports

- Parallelism
- Recovery
- Scheduling
- Scalability

---

# Runtime Architecture

```
Goal

↓

Planner

↓

Workflow Graph

↓

Scheduler

↓

Executor

↓

Verification

↓

Completion
```

---

# Performance Considerations

Optimize

Workflow startup

↓

Scheduling latency

↓

Parallel execution

↓

Checkpoint overhead

↓

Recovery time

↓

Completion latency

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Sequential | Simple | Slow |
| Parallel | Fast | Synchronization |
| Event Driven | Responsive | More infrastructure |
| DAG | Flexible | More planning |

---

# Security

Protect against

- Unauthorized workflow execution
- Invalid task injection
- Infinite execution
- Privilege escalation
- Sensitive data exposure

Validate every workflow before execution.

---

# Observability

Track

Workflow creation

↓

Task execution

↓

Retries

↓

Checkpoint creation

↓

Completion

↓

Failures

↓

Recovery

---

# Metrics

Monitor

Workflow Success Rate

Average Completion Time

Task Throughput

Retry Rate

Checkpoint Frequency

Recovery Time

Parallelism Ratio

Resource Utilization

---

# Common Failures

- Missing dependencies
- Circular workflows
- No checkpoints
- Infinite retries
- Poor scheduling
- Unclear completion criteria
- No human approval gates

---

# Best Practices

- Keep workflows modular.
- Prefer DAGs over rigid sequences.
- Separate planning from execution.
- Support resumable execution.
- Add checkpoints strategically.
- Measure workflow performance.
- Validate before execution.
- Keep workflows observable.

---

# Anti-Patterns

❌ Monolithic workflows

❌ Hidden dependencies

❌ No retry policy

❌ No recovery strategy

❌ Infinite loops

❌ Hardcoded execution order

❌ Mixing workflow logic with business logic

---

# Real-World Production Examples

## LangGraph

- Represents workflows as directed graphs.
- Persists checkpoints between nodes.
- Supports resumable execution.

---

## Temporal

- Executes durable workflows.
- Retries failed activities automatically.
- Maintains workflow history for recovery.

---

## Prefect

- Orchestrates data and AI pipelines.
- Tracks task state and dependencies.
- Provides workflow observability.

---

## Claude Code

- Executes workflows through planning, editing, testing, and verification stages.
- Adapts workflows dynamically when failures occur.

---

## GitHub Actions

- Defines workflows using declarative YAML.
- Supports parallel jobs, conditions, retries, and approvals.

---

# Testing

Verify

Workflow creation

Dependency resolution

Scheduling

Parallel execution

Retry policies

Checkpoint recovery

Completion criteria

Failure handling

Human approval gates

---

# Review Checklist

□ Workflow lifecycle defined

□ DAG validated

□ Dependencies explicit

□ Retry policy configured

□ Checkpoints implemented

□ Recovery supported

□ Metrics configured

□ Observability enabled

□ Human approval supported

□ Tests passing

---

# Related Skills

- orchestration.md
- delegation.md
- communication_protocols.md
- multi_agent_systems.md
- planning.md
- state_management.md
- patterns/planner_executor.md
- patterns/react.md
- patterns/router.md
- patterns/supervisor_worker.md
- patterns/map_reduce.md

---

# Definition of Done

A workflow system is production-ready only if

✓ Workflows are represented as structured execution graphs

✓ Dependencies and execution order are explicit

✓ Parallel and sequential execution are supported

✓ Checkpoints enable recovery from failures

✓ Retry and error handling strategies are implemented

✓ Human approval gates exist for high-impact operations

✓ Workflow execution is observable and measurable

✓ Security validates every workflow before execution

✓ Workflow logic is separated from business logic

✓ Complex objectives can be executed reliably through repeatable, resumable workflows
