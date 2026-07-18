# Pattern

Supervisor → Worker

Version: 1.0

---

# Goal

Coordinate multiple specialized workers through a central supervisor that plans, delegates, monitors, validates, and aggregates work while maintaining overall responsibility for task completion.

The Supervisor–Worker pattern enables scalable multi-agent systems by separating coordination from execution.

A production implementation should maximize specialization, parallelism, fault tolerance, and observability.

---

# When to Use

Use this pattern whenever

- Multiple specialized agents exist
- Large goals require decomposition
- Work can execute in parallel
- Workers have different capabilities
- Tasks require coordination
- Human supervision is limited

---

# Problem

A single agent responsible for

- planning
- execution
- validation
- recovery
- communication

quickly becomes a bottleneck.

Problems include

- context overload
- slow execution
- duplicated work
- difficult debugging
- poor specialization

---

# Solution

Introduce a supervisor.

```
Goal

↓

Supervisor

↓

Worker A

Worker B

Worker C

↓

Aggregation

↓

Validation

↓

Complete
```

Workers perform execution.

Supervisor owns coordination.

---

# Core Principles

Coordinate centrally.

Execute independently.

Validate collectively.

Recover gracefully.

---

# Architecture

```
User

↓

Supervisor

↓

Task Queue

↓

Workers

↓

Results

↓

Aggregator

↓

Validator

↓

Completion
```

---

# Components

## Supervisor

Responsible for

- understanding objectives
- planning work
- selecting workers
- scheduling tasks
- monitoring execution
- validating outputs
- handling failures

Should not perform detailed execution.

---

## Workers

Responsible for

- executing assigned tasks
- using tools
- producing structured outputs
- reporting status

Should not redefine objectives.

---

## Aggregator

Responsible for

- merging outputs
- resolving conflicts
- validating completeness

---

## Validator

Responsible for

- quality assurance
- testing
- policy compliance
- completion verification

---

# Execution Lifecycle

Goal

↓

Supervisor Planning

↓

Task Assignment

↓

Worker Execution

↓

Aggregation

↓

Validation

↓

Complete

or

↓

Reassignment

---

# Delegation Strategies

## Static Assignment

Workers always perform predefined roles.

Simple and predictable.

---

## Capability-Based Assignment

Supervisor selects workers according to

- expertise
- available tools
- permissions
- workload

Recommended default.

---

## Dynamic Assignment

Workers selected at runtime using

- latency
- historical performance
- current availability
- cost

Best for enterprise systems.

---

# Worker Lifecycle

Idle

↓

Assigned

↓

Executing

↓

Reporting

↓

Completed

↓

Idle

Workers should remain stateless whenever practical.

---

# Parallel Execution

Independent tasks execute simultaneously.

Example

```
Research

+

Backend

+

Frontend

+

Testing

↓

Merge
```

Parallel execution increases throughput.

---

# Result Aggregation

Supervisor combines

- code
- documents
- reports
- analyses
- decisions

Conflicts should be resolved before validation.

---

# Failure Recovery

If a worker fails

Detect

↓

Retry

↓

Reassign

↓

Alternative Worker

↓

Escalate

↓

Continue

Failure should remain isolated.

---

# Conflict Resolution

When outputs disagree

Validate evidence

↓

Rank confidence

↓

Majority agreement

↓

Supervisor decision

↓

Human review (if required)

Never merge conflicting results automatically.

---

# Load Balancing

Distribute work according to

- worker utilization
- queue depth
- execution latency
- capability
- reliability

Avoid worker starvation.

---

# Communication

Workers communicate using

- structured messages
- task IDs
- correlation IDs
- execution status
- result schemas

Workers should avoid direct peer-to-peer communication unless explicitly designed.

---

# Engineering Decisions

## Single Supervisor

Suitable for

- hackathons
- prototypes
- small teams

---

## Hierarchical Supervisors

CEO

↓

Engineering Manager

↓

Backend Lead

↓

Developers

Recommended for enterprise-scale systems.

---

## Distributed Supervisors

Multiple supervisors coordinate large workloads.

Useful for

- cloud platforms
- AI operating systems
- very large workflows

---

# Runtime Architecture

```
Goal
 │
 ▼
Supervisor
 │
 ▼
Scheduler
 │
 ▼
Task Queue
 │
 ▼
Worker Pool
 │
 ▼
Aggregation
 │
 ▼
Validation
 │
 ▼
Complete
```

---

# Performance

Optimize

- delegation latency
- worker utilization
- aggregation overhead
- scheduling efficiency
- retry frequency
- execution throughput

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Single supervisor | Simple | Bottleneck |
| Hierarchical | Scalable | More coordination |
| Distributed | Highly scalable | Operational complexity |
| Static workers | Predictable | Less flexible |
| Dynamic workers | Adaptive | Scheduling overhead |

---

# Common Failures

- supervisor bottleneck
- duplicate assignments
- idle workers
- overloaded workers
- poor aggregation
- excessive coordination
- missing validation

---

# Best Practices

- Keep supervisors lightweight.
- Keep workers specialized.
- Delegate based on capability.
- Use structured communication.
- Validate aggregated outputs.
- Support dynamic reassignment.
- Measure worker performance.
- Isolate failures.

---

# Anti-Patterns

❌ Supervisor performing execution

❌ Workers redefining objectives

❌ Duplicate task assignments

❌ Unlimited worker permissions

❌ Hidden communication

❌ No aggregation validation

❌ Tight coupling between workers

---

# Comparison

| Pattern | Best For | Weakness |
|----------|-----------|----------|
| Planner–Executor | Structured workflows | Limited specialization |
| ReAct | Tool-driven reasoning | Single-agent focus |
| Supervisor–Worker | Multi-agent execution | Coordinator bottleneck |
| Router | Dynamic routing | Limited coordination |
| Map–Reduce | Massive parallelism | Weak iterative reasoning |

---

# Real-World Examples

## Claude Code

Coordinates repository exploration, implementation, testing, and validation through specialized execution stages while maintaining centralized control over the workflow.

---

## CrewAI

Uses manager agents to assign role-based tasks to specialized workers and aggregate results into a unified outcome.

---

## AutoGen

Supports supervisory agents coordinating conversations between specialized assistants to solve complex objectives collaboratively.

---

## LangGraph

Represents supervisors and workers as graph nodes with durable execution state, checkpoints, and resumable workflows.

---

## Google Agent Development Kit (ADK)

Encourages orchestrators that coordinate modular agents through structured interfaces and well-defined responsibilities.

---

## Devin

Separates planning, implementation, debugging, and validation into coordinated execution phases managed through centralized task orchestration.

---

# Related Skills

- delegation.md
- orchestration.md
- multi_agent_systems.md
- communication_protocols.md
- workflows.md

---

# Related Patterns

- planner_executor.md
- react.md
- router.md
- map_reduce.md
- reflexion.md

---

# Definition of Done

A Supervisor–Worker implementation is production-ready only if

✓ Responsibilities are clearly separated between supervisors and workers

✓ Delegation is based on worker capabilities and workload

✓ Parallel execution is supported for independent tasks

✓ Communication uses structured, versioned messages

✓ Aggregation validates and reconciles worker outputs

✓ Failures are isolated and recoverable through retries or reassignment

✓ Supervisor decisions are observable through logs and metrics

✓ Workers operate with least-privilege permissions

✓ Human escalation is available for unresolved conflicts

✓ Complex objectives can be completed through coordinated specialization at production scale