# Skill

State Management

Version: 1.0

---

# Goal

Design reliable, persistent, and recoverable runtime state systems that enable AI agents to execute long-running workflows, recover from failures, coordinate tools, and maintain execution context.

State Management is responsible for **what the agent is doing right now**.

It is not responsible for long-term memory or knowledge retrieval.

---

# When to Load

Load this skill whenever building

- AI Agents
- Coding Agents
- Workflow Engines
- Multi-Step Automation
- Long Running Tasks
- Multi-Agent Systems

---

# Prerequisites

- planning.md
- reasoning.md
- tool_calling.md

---

# Core Principles

State represents

Current Progress

↓

Execution Context

↓

Intermediate Results

↓

Active Tasks

↓

Workflow Status

State should always be recoverable.

---

# Responsibilities

State Management should

- Track execution
- Store intermediate results
- Resume interrupted workflows
- Coordinate components
- Maintain checkpoints
- Synchronize parallel tasks

State Management should not

- Store user preferences
- Store long-term memory
- Replace databases

---

# State Lifecycle

```
Initialize

↓

Update

↓

Checkpoint

↓

Recover

↓

Complete

↓

Archive

↓

Delete
```

Every workflow follows this lifecycle.

---

# Types of State

## Session State

Temporary state for one interaction.

Examples

- Current prompt
- Active tool
- Open files
- Current branch

Discarded after completion.

---

## Workflow State

Tracks execution of a long-running task.

Examples

- Current step
- Completed tasks
- Pending tasks
- Failures

Can survive restarts.

---

## Execution State

Tracks runtime execution.

Examples

- Tool outputs
- Variables
- API responses
- Temporary artifacts

Usually short-lived.

---

## Shared State

Accessible by multiple agents.

Examples

- Task queue
- Blackboard
- Shared document
- Coordination messages

Requires synchronization.

---

# State Architecture

```
Planner

↓

Workflow State

↓

Executor

↓

Tool Outputs

↓

Checkpoint

↓

Recovery

↓

Continue
```

State should be external to the LLM.

---

# State Model

Every state object should contain

- Workflow ID
- Session ID
- Current Goal
- Active Step
- Status
- Variables
- Tool Results
- Checkpoints
- Metadata
- Timestamps

Keep state serializable.

---

# State Transitions

```
Pending

↓

Running

↓

Waiting

↓

Completed

↓

Failed

↓

Cancelled
```

Transitions should be explicit and auditable.

---

# Checkpointing

Persist execution at meaningful boundaries.

Examples

- Before tool execution
- After tool execution
- Before user approval
- Before external API calls

Checkpointing enables recovery.

---

# Recovery

Recover from

- Process crash
- Network failure
- Timeout
- User disconnect
- Deployment restart

Resume from the latest checkpoint.

---

# State Persistence

Choose storage based on workflow duration.

Short-lived

- Redis
- In-memory cache

Long-lived

- PostgreSQL
- DynamoDB
- MongoDB

Shared

- Distributed cache
- Event store

---

# State Synchronization

When multiple workers modify state

Use

- Optimistic locking
- Version numbers
- Atomic updates
- Distributed locks

Prevent race conditions.

---

# Event Sourcing

Instead of storing only current state

Store

```
Event

↓

Event

↓

Event

↓

Current State
```

Advantages

- Auditability
- Replay
- Debugging

Trade-off

Higher storage cost.

---

# State Versioning

Support

- Schema evolution
- Migration
- Rollback
- Compatibility

Never break existing workflows.

---

# Pattern References

## Planner Executor

Planner updates workflow state.

Executor updates execution state.

See

patterns/planner_executor.md

---

## Supervisor Worker

Supervisor owns shared state.

Workers own local state.

See

patterns/supervisor_worker.md

---

## Map Reduce

Workers maintain isolated state.

Reducer merges results.

See

patterns/map_reduce.md

---

# Engineering Decisions

## In-Memory State

Use when

- Hackathons
- Simple chatbots
- Short workflows

Advantages

Fast

Simple

Trade-off

Lost on restart.

---

## Redis

Use when

- Session state
- Temporary execution
- Distributed workers

Recommended for runtime state.

---

## Database Persistence

Use when

- Enterprise workflows
- Long-running tasks
- Auditing

Recommended default.

---

## Event Sourcing

Use when

- Compliance
- Replay
- Debugging

Trade-off

Higher implementation complexity.

---

# Runtime Architecture

```
Planner

↓

State Store

↓

Executor

↓

Checkpoint

↓

Recovery Manager

↓

Continue
```

---

# Performance Considerations

Optimize

State reads

↓

State writes

↓

Checkpoint latency

↓

Recovery time

↓

Serialization

↓

Synchronization

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| In-memory | Fast | Not durable |
| Redis | Low latency | Additional infrastructure |
| Database | Durable | Higher latency |
| Event sourcing | Replayable | More storage |
| Shared state | Collaboration | Synchronization overhead |

---

# Security

Protect

- Session data
- Workflow state
- Execution artifacts
- Secrets
- Access tokens

Encrypt sensitive state at rest and in transit.

---

# Observability

Track

State updates

↓

Checkpoint frequency

↓

Recovery count

↓

Synchronization conflicts

↓

Workflow completion

↓

Execution latency

---

# Metrics

Monitor

State Read Latency

State Write Latency

Checkpoint Time

Recovery Success Rate

Workflow Completion Rate

Conflict Rate

State Size

Storage Growth

---

# Common Failures

- Losing state after restart
- Shared mutable state
- Race conditions
- Missing checkpoints
- Corrupted state
- Infinite retries
- Version incompatibility

---

# Best Practices

- Keep state external to the LLM.
- Checkpoint frequently.
- Separate workflow and session state.
- Make state serializable.
- Support recovery by design.
- Track state transitions.
- Version schemas.
- Audit important changes.

---

# Anti-Patterns

❌ Keeping all state in prompts

❌ Global mutable variables

❌ No recovery strategy

❌ No checkpointing

❌ Shared state without synchronization

❌ Mixing memory with runtime state

❌ Ignoring schema evolution

---

# Real-World Production Examples

## LangGraph

- Persists graph execution state.
- Supports resumable workflows.
- Stores checkpoints between nodes.

---

## Claude Code

- Maintains task context across filesystem operations.
- Tracks execution progress through multi-step edits.

---

## OpenHands

- Persists execution state while running coding tasks.
- Resumes work after tool failures.

---

## Temporal

- Uses durable workflow state.
- Automatically retries failed activities.
- Recovers long-running workflows after crashes.

---

## Prefect

- Tracks task state transitions.
- Persists execution metadata for orchestration.

---

# Testing

Verify

State persistence

Checkpoint recovery

Concurrent updates

Version migrations

Serialization

Recovery after restart

Distributed synchronization

Workflow resumption

---

# Review Checklist

□ State model defined

□ Workflow state separated

□ Session state separated

□ Checkpointing implemented

□ Recovery supported

□ Synchronization configured

□ Metrics enabled

□ Security reviewed

□ Observability implemented

□ Tests passing

---

# Related Skills

- memory_integration.md
- orchestration.md
- workflows.md
- delegation.md
- patterns/planner_executor.md
- patterns/supervisor_worker.md
- patterns/map_reduce.md

---

# Definition of Done

A state management system is production-ready only if

✓ Runtime state is externalized from the LLM

✓ Session, workflow, and execution state are clearly separated

✓ Checkpoints enable reliable recovery

✓ State transitions are explicit and auditable

✓ Concurrent updates are synchronized safely

✓ State schemas support versioning

✓ Recovery works after failures and restarts

✓ Performance is monitored continuously

✓ Security protects sensitive execution state

✓ Long-running workflows can resume without losing progress