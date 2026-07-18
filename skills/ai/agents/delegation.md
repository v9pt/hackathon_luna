# Skill

Delegation

Version: 1.0

---

# Goal

Design reliable delegation systems that assign work to the most appropriate agent, worker, or execution unit while maximizing parallelism, minimizing duplication, and ensuring accountability.

Delegation enables AI systems to solve complex problems by distributing work across specialized components.

A production delegation system should assign responsibility intelligently while maintaining coordination and observability.

---

# When to Load

Load this skill whenever building

- Multi-Agent Systems
- Coding Agents
- Enterprise AI
- Research Agents
- Workflow Engines
- Distributed Automation

---

# Prerequisites

- planning.md
- task_decomposition.md
- workflows.md
- state_management.md

---

# Core Principles

Goal

↓

Decompose

↓

Assign

↓

Execute

↓

Verify

↓

Aggregate

↓

Complete

Delegation assigns responsibility.

Execution performs the work.

---

# Responsibilities

Delegation systems should

- Select the appropriate worker
- Balance workload
- Track ownership
- Prevent duplicate work
- Support parallel execution
- Reassign failed work
- Aggregate results

Delegation systems should not

- Perform reasoning
- Execute tools directly
- Store long-term memory

---

# Delegation Lifecycle

```
Goal

↓

Task Analysis

↓

Worker Selection

↓

Assignment

↓

Execution

↓

Monitoring

↓

Verification

↓

Aggregation
```

Every delegated task should have a clear owner.

---

# Delegation Model

```
Planner

↓

Supervisor

↓

Worker A

Worker B

Worker C

↓

Results

↓

Merge

↓

Final Output
```

Ownership should always be explicit.

---

# Worker Selection

Select workers using

Capability

↓

Availability

↓

Current Load

↓

Estimated Cost

↓

Reliability

↓

Permissions

Always assign work to the most suitable worker.

---

# Task Ownership

Every task should have

- Owner
- Priority
- Deadline
- Status
- Dependencies
- Retry Policy

No task should have multiple owners unless explicitly coordinated.

---

# Delegation Strategies

## Capability-Based

Assign work based on expertise.

Example

- Backend Agent
- Frontend Agent
- QA Agent

Recommended default.

---

## Load-Based

Assign work to the least busy worker.

Useful for high-throughput systems.

---

## Cost-Based

Choose the lowest-cost worker capable of completing the task.

Useful for LLM routing.

---

## Priority-Based

Critical work receives the highest priority.

Useful for production incidents.

---

## Geographic

Assign work based on region.

Examples

- US Data
- EU Compliance
- APAC Infrastructure

Useful for enterprise deployments.

---

# Static Delegation

Assignments are predefined.

Advantages

- Predictable
- Simple

Trade-off

Less adaptive.

---

# Dynamic Delegation

Assignments are determined at runtime.

Advantages

- Flexible
- Adaptive
- Resource aware

Recommended for autonomous systems.

---

# Parallel Delegation

```
Research

+

Implementation

+

Testing

↓

Integration
```

Independent work should execute concurrently.

---

# Sequential Delegation

```
Architecture

↓

Development

↓

Testing

↓

Deployment
```

Required when dependencies exist.

---

# Delegation Constraints

Respect

Permissions

↓

Dependencies

↓

Budget

↓

Deadlines

↓

Tool Availability

↓

Compliance

Delegation should never violate system constraints.

---

# Workload Balancing

Monitor

Tasks per Worker

↓

Execution Time

↓

Failure Rate

↓

Queue Length

↓

Resource Usage

Prevent worker starvation.

---

# Failure Recovery

If a worker fails

```
Detect

↓

Retry

↓

Reassign

↓

Verify

↓

Continue
```

Delegation should be resilient.

---

# Result Aggregation

Merge outputs using

Validation

↓

Deduplication

↓

Conflict Resolution

↓

Ranking

↓

Summary

Aggregation should preserve correctness.

---

# Pattern References

## Supervisor Worker

Supervisor assigns work.

Workers execute.

Supervisor validates results.

See

patterns/supervisor_worker.md

---

## Planner Executor

Planner creates assignments.

Executors perform work.

See

patterns/planner_executor.md

---

## Router

Route tasks to specialized workers.

See

patterns/router.md

---

## Map Reduce

Distribute

↓

Execute

↓

Merge

See

patterns/map_reduce.md

---

# Engineering Decisions

## Single Worker

Use when

Small workflows

Simple automation

Low overhead

---

## Specialized Workers

Use when

Different expertise is required.

Recommended default.

---

## Dynamic Delegation

Use when

Workload changes frequently.

Supports autonomous systems.

---

## Hierarchical Delegation

Use when

Large organizations

Complex workflows

Many workers

Recommended for enterprise AI.

---

# Runtime Architecture

```
Planner

↓

Supervisor

↓

Task Queue

↓

Worker Pool

↓

Aggregation

↓

Verification

↓

Completion
```

---

# Performance Considerations

Optimize

Assignment latency

↓

Worker utilization

↓

Queue time

↓

Parallel execution

↓

Aggregation latency

↓

Task completion

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Static delegation | Predictable | Inflexible |
| Dynamic delegation | Adaptive | More runtime logic |
| Specialized workers | Higher quality | More coordination |
| General workers | Simpler | Lower expertise |
| Parallel delegation | Faster | Synchronization overhead |

---

# Security

Protect against

- Unauthorized task assignment
- Privilege escalation
- Duplicate execution
- Worker impersonation
- Cross-tenant delegation
- Sensitive data leakage

Workers should receive only the information required for their task.

---

# Observability

Track

Task assignments

↓

Worker utilization

↓

Queue length

↓

Execution time

↓

Failures

↓

Reassignments

↓

Aggregation quality

---

# Metrics

Monitor

Assignment Latency

Worker Utilization

Queue Time

Task Success Rate

Worker Failure Rate

Reassignment Rate

Aggregation Latency

Parallelism Ratio

Cost Per Task

---

# Common Failures

- Wrong worker selection
- Duplicate ownership
- Worker overload
- Poor balancing
- Missing reassignment
- Bottleneck supervisors
- No aggregation validation

---

# Best Practices

- Assign one owner per task.
- Prefer specialized workers.
- Balance workload continuously.
- Support dynamic reassignment.
- Validate aggregated results.
- Monitor worker health.
- Delegate only necessary context.
- Keep delegation observable.

---

# Anti-Patterns

❌ One agent performs everything

❌ Multiple owners without coordination

❌ Blind round-robin assignment

❌ Ignoring worker capabilities

❌ No reassignment strategy

❌ Supervisor executing worker tasks

❌ Unlimited task fan-out

---

# Real-World Production Examples

## Claude Code

- Delegates repository analysis, code editing, testing, and validation to specialized execution phases.
- Coordinates results before presenting changes.

---

## OpenHands

- Separates repository exploration, implementation, testing, and verification into distinct responsibilities.
- Reassigns work when execution fails.

---

## AutoGen

- Enables specialized conversational agents to collaborate through explicit task delegation.
- Supports hierarchical coordination patterns.

---

## CrewAI

- Assigns responsibilities to role-based agents with defined goals and capabilities.
- Coordinates execution through task ownership.

---

## Google ADK

- Supports modular agent composition with clear responsibility boundaries.
- Encourages reusable specialist agents.

---

# Testing

Verify

Worker selection

Capability matching

Load balancing

Task ownership

Parallel execution

Sequential execution

Failure reassignment

Aggregation

Permission enforcement

---

# Review Checklist

□ Delegation model defined

□ Worker capabilities documented

□ Ownership assigned

□ Load balancing implemented

□ Failure recovery supported

□ Aggregation validated

□ Metrics configured

□ Observability enabled

□ Security reviewed

□ Tests passing

---

# Related Skills

- orchestration.md
- communication_protocols.md
- multi_agent_systems.md
- workflows.md
- task_decomposition.md
- patterns/supervisor_worker.md
- patterns/planner_executor.md
- patterns/router.md
- patterns/map_reduce.md

---

# Definition of Done

A delegation system is production-ready only if

✓ Every task has a single accountable owner

✓ Worker selection is capability-aware

✓ Dynamic reassignment handles failures

✓ Parallel and sequential delegation are supported

✓ Results are validated before aggregation

✓ Workloads remain balanced across workers

✓ Delegation decisions are observable and measurable

✓ Security enforces least-privilege information sharing

✓ Worker responsibilities remain modular and reusable

✓ Complex objectives are completed reliably through coordinated specialization