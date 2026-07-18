# Skill

Multi-Agent Systems

Version: 1.0

---

# Goal

Design scalable, fault-tolerant, and collaborative AI systems composed of multiple specialized agents that cooperate to solve complex problems more efficiently than a single agent.

A multi-agent system distributes intelligence across specialized workers while coordinating planning, communication, execution, and validation.

A production multi-agent system should maximize specialization, reliability, scalability, and observability.

---

# When to Load

Load this skill whenever building

- Enterprise AI
- Coding Agents
- Research Platforms
- Autonomous Organizations
- Workflow Engines
- AI Operating Systems
- Large Automation Systems

---

# Prerequisites

- orchestration.md
- delegation.md
- communication_protocols.md
- workflows.md
- state_management.md
- memory_integration.md

---

# Core Principles

Goal

↓

Planner

↓

Specialized Agents

↓

Coordination

↓

Verification

↓

Aggregation

↓

Completion

No single agent should perform every task.

---

# Responsibilities

Multi-agent systems should

- Divide work
- Assign specialists
- Coordinate execution
- Share information
- Resolve conflicts
- Aggregate results
- Recover from failures

Multi-agent systems should not

- Duplicate work
- Hide responsibilities
- Share unrestricted access
- Create circular dependencies

---

# Why Multi-Agent Systems

Single agents eventually become bottlenecks.

Problems include

- Context limits
- Tool overload
- Slow execution
- Poor specialization
- Difficult debugging

Multi-agent systems solve these by distributing responsibility.

---

# Multi-Agent Lifecycle

```
Goal

↓

Planning

↓

Task Decomposition

↓

Delegation

↓

Communication

↓

Execution

↓

Aggregation

↓

Validation

↓

Completion
```

---

# Agent Roles

Typical specialist agents

- Planner
- Researcher
- Backend Engineer
- Frontend Engineer
- QA Engineer
- Security Reviewer
- Documentation Writer
- Deployment Engineer

Each agent should have a clearly defined responsibility.

---

# Agent Topologies

## Supervisor Worker

```
Supervisor

↓

Worker A

Worker B

Worker C

↓

Merge
```

Recommended default.

---

## Hierarchical

```
CEO

↓

Engineering Manager

↓

Backend

Frontend

QA
```

Best for enterprise organizations.

---

## Peer-to-Peer

```
Agent A

↔

Agent B

↔

Agent C
```

Useful for collaborative research.

---

## Swarm

Many agents collaborate without a permanent leader.

Useful for exploration and optimization.

Trade-off

Higher coordination complexity.

---

## Hub and Spoke

```
Coordinator

↓

All Workers
```

Simple centralized communication.

---

## Hybrid

Combine multiple topologies.

Recommended for production systems.

---

# Agent Specialization

Specialize by

Domain

↓

Capability

↓

Tools

↓

Knowledge

↓

Permissions

Avoid general-purpose workers whenever possible.

---

# Coordination Strategies

Support

Centralized

Distributed

Event Driven

Hierarchical

Collaborative

Choose based on workload.

---

# Shared Knowledge

Agents may share

Knowledge Base

↓

Vector Store

↓

Workflow State

↓

Messages

↓

Artifacts

Avoid sharing unnecessary context.

---

# Conflict Resolution

When agents disagree

Validate

↓

Rank Evidence

↓

Majority Decision

↓

Supervisor Decision

↓

Human Approval

Never merge conflicting outputs blindly.

---

# Failure Handling

If an agent fails

Detect

↓

Retry

↓

Reassign

↓

Alternative Agent

↓

Escalate

↓

Continue

Failure should remain isolated.

---

# Scalability

Scale by

Adding workers

↓

Task partitioning

↓

Parallel execution

↓

Load balancing

↓

Distributed orchestration

---

# Resource Isolation

Each agent should have

Own Context

Own Permissions

Own Memory View

Own Tool Access

Least privilege improves safety.

---

# Pattern References

## Supervisor Worker

See

patterns/supervisor_worker.md

---

## Planner Executor

See

patterns/planner_executor.md

---

## Router

See

patterns/router.md

---

## Map Reduce

See

patterns/map_reduce.md

---

## ReAct

See

patterns/react.md

---

# Engineering Decisions

## Single Supervisor

Use when

Small systems

Hackathons

Simple automation

---

## Hierarchical Teams

Use when

Enterprise software

Large engineering teams

Recommended default.

---

## Peer Network

Use when

Collaborative reasoning

Research

Scientific discovery

---

## Swarm

Use when

Large search spaces

Optimization

Simulation

Trade-off

Higher communication cost.

---

# Runtime Architecture

```
User

↓

Planner

↓

Orchestrator

↓

Supervisor

↓

Worker Pool

↓

Communication Layer

↓

Shared State

↓

Aggregation

↓

Validation

↓

Response
```

---

# Performance Considerations

Optimize

Agent startup

↓

Communication latency

↓

Parallel execution

↓

Aggregation

↓

Synchronization

↓

Resource utilization

↓

Context size

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Single Agent | Simple | Doesn't scale |
| Supervisor Worker | Organized | Coordinator bottleneck |
| Hierarchical | Scalable | More management |
| Peer Network | Flexible | Coordination complexity |
| Swarm | Massive parallelism | High communication cost |

---

# Security

Protect against

- Unauthorized delegation
- Agent impersonation
- Context leakage
- Excessive permissions
- Malicious workers
- Cross-agent prompt injection

Each agent should receive only the information and permissions required for its role.

---

# Observability

Track

Agent utilization

↓

Delegation decisions

↓

Communication latency

↓

Task completion

↓

Failures

↓

Retries

↓

Aggregation quality

↓

Resource usage

---

# Metrics

Monitor

Task Success Rate

Agent Utilization

Delegation Accuracy

Communication Latency

Workflow Completion Time

Parallelism Ratio

Failure Recovery Rate

Aggregation Accuracy

Cost Per Workflow

---

# Common Failures

- Duplicate work
- Poor specialization
- Communication bottlenecks
- Circular delegation
- Context leakage
- Worker starvation
- Supervisor overload

---

# Best Practices

- Build specialized agents.
- Delegate based on capability.
- Use structured communication.
- Minimize shared context.
- Validate aggregated results.
- Monitor coordination quality.
- Keep responsibilities explicit.
- Design for failure recovery.

---

# Anti-Patterns

❌ One agent doing everything

❌ Unlimited context sharing

❌ Circular delegation

❌ Shared mutable memory

❌ Hidden ownership

❌ No aggregation validation

❌ Excessive communication

---

# Real-World Production Examples

## Claude Code

- Organizes complex software engineering work into specialized execution phases.
- Coordinates planning, editing, testing, and validation through structured workflows.

---

## OpenHands

- Separates repository exploration, implementation, testing, and verification.
- Uses specialized execution stages with iterative feedback.

---

## CrewAI

- Coordinates role-based agents through structured task delegation and collaboration.
- Supports hierarchical and collaborative execution models.

---

## AutoGen

- Enables conversational collaboration between multiple specialized agents.
- Uses structured messaging to coordinate planning and execution.

---

## LangGraph

- Represents multi-agent workflows as graph-based execution pipelines.
- Supports durable state, checkpoints, and coordinated execution.

---

## Google Agent Development Kit (ADK)

- Encourages modular, reusable agent components with standardized interfaces.
- Supports scalable orchestration across heterogeneous agent teams.

---

# Testing

Verify

Agent coordination

Delegation

Communication

Failure isolation

Aggregation

Conflict resolution

Load balancing

Security boundaries

Recovery

Scalability

---

# Review Checklist

□ Agent roles defined

□ Topology selected

□ Communication protocol implemented

□ Delegation strategy configured

□ Conflict resolution documented

□ Failure recovery implemented

□ Metrics configured

□ Observability enabled

□ Security reviewed

□ Tests passing

---

# Related Skills

- human_in_the_loop.md
- evaluation.md
- safety.md
- orchestration.md
- communication_protocols.md
- delegation.md
- workflows.md
- patterns/supervisor_worker.md
- patterns/planner_executor.md
- patterns/router.md
- patterns/map_reduce.md
- patterns/react.md

---

# Definition of Done

A multi-agent system is production-ready only if

✓ Agent responsibilities are clearly defined

✓ Appropriate topology is selected for the workload

✓ Delegation matches agent capabilities

✓ Communication uses structured, versioned protocols

✓ Shared state and knowledge are managed safely

✓ Failures remain isolated and recoverable

✓ Aggregated results are validated before completion

✓ Security enforces least privilege across agents

✓ Observability provides end-to-end visibility into coordination

✓ The system reliably solves complex objectives through coordinated specialization at production scale