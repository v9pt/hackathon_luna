# Pattern

Router

Version: 1.0

---

# Goal

Direct requests, tasks, or events to the most appropriate model, agent, tool, workflow, or service based on structured routing policies.

The Router pattern separates decision-making from execution, enabling AI systems to scale efficiently while optimizing cost, latency, quality, and resource utilization.

A production router should consistently choose the best execution path while remaining observable, configurable, and fault tolerant.

---

# When to Use

Use this pattern whenever

- Multiple agents exist
- Multiple LLMs are available
- Multiple tools perform similar tasks
- Different workflows handle different requests
- Cost optimization matters
- Latency optimization matters
- Enterprise AI platforms

---

# Problem

Without routing

Every request reaches every component.

Problems include

- unnecessary tool calls
- increased latency
- higher cost
- duplicated work
- poor scalability
- overloaded workers

---

# Solution

Insert a routing layer.

```
Request

↓

Router

↓

Best Destination

↓

Execution

↓

Response
```

Only one or the appropriate set of execution paths should receive the request.

---

# Core Principles

Classify

↓

Route

↓

Execute

↓

Validate

↓

Respond

Routing should remain independent of execution.

---

# Architecture

```
User Request
      │
      ▼
   Router
      │
 ┌────┼────┐
 ▼    ▼    ▼
Agent Tool Model
      │
      ▼
Execution
```

---

# Components

## Request Classifier

Determines

- intent
- domain
- complexity
- priority

---

## Routing Engine

Selects

- worker
- model
- tool
- workflow

based on routing policies.

---

## Execution Target

Receives the routed request.

---

## Validator

Confirms

- routing correctness
- execution success
- policy compliance

---

# Routing Lifecycle

Receive Request

↓

Classify

↓

Evaluate Rules

↓

Select Destination

↓

Execute

↓

Validate

↓

Complete

---

# Routing Strategies

## Rule-Based Routing

Examples

IF coding

↓

Backend Agent

Simple

Deterministic

Easy to debug.

---

## Intent Routing

Identify user intent

↓

Select workflow

Useful for assistants.

---

## Capability Routing

Choose destination based on

- supported tools
- knowledge
- permissions

Recommended default.

---

## Semantic Routing

Compare embeddings.

Route toward closest semantic match.

Useful for RAG.

---

## LLM Router

LLM decides

- agent
- workflow
- tool

Useful when rules become too complex.

Trade-off

Higher latency and cost.

---

## Hybrid Router

Rules

↓

Semantic

↓

LLM

↓

Fallback

Recommended for production.

---

# Cost-Aware Routing

Choose

Fast Model

↓

Large Model

↓

Expert Model

↓

Human

Only escalate when necessary.

---

# Latency Optimization

Prefer

Nearby services

↓

Cached results

↓

Fast models

↓

Parallel routing

Latency should influence routing decisions.

---

# Fallback Routing

If destination fails

Retry

↓

Alternative Agent

↓

Alternative Model

↓

Alternative Workflow

↓

Human Escalation

Avoid single points of failure.

---

# Multi-Destination Routing

Some requests require

Research Agent

+

Backend Agent

+

QA Agent

↓

Aggregation

Useful for complex workflows.

---

# Pattern References

## Supervisor Worker

Supervisor uses routing to select workers.

---

## Planner Executor

Planner routes execution tasks.

---

## ReAct

Reasoning determines routing decisions.

---

# Engineering Decisions

## Static Router

Simple systems

Hackathons

---

## Dynamic Router

Enterprise AI

Recommended.

---

## Centralized Router

Easy to monitor.

Trade-off

Single bottleneck.

---

## Distributed Router

Large-scale systems.

Higher resilience.

Higher complexity.

---

# Runtime Architecture

```
Request

↓

Classifier

↓

Routing Engine

↓

Destination

↓

Execution

↓

Validation
```

---

# Performance

Optimize

classification latency

↓

routing accuracy

↓

execution cost

↓

fallback time

↓

cache utilization

↓

throughput

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Rule-Based | Predictable | Less flexible |
| Semantic | Intelligent | Embedding cost |
| LLM Router | Adaptive | Higher latency |
| Hybrid | Balanced | More infrastructure |

---

# Common Failures

- incorrect routing
- routing loops
- overloaded destinations
- poor fallback
- conflicting rules
- stale routing policies

---

# Best Practices

- Separate routing from execution.
- Version routing rules.
- Monitor routing accuracy.
- Keep fallbacks available.
- Optimize for cost and latency.
- Validate routing decisions.
- Measure destination performance.
- Prefer capability-based routing.

---

# Anti-Patterns

❌ Hardcoding execution targets

❌ Routing everything to the largest model

❌ No fallback

❌ Circular routing

❌ Ignoring latency

❌ Ignoring costs

❌ Hidden routing logic

---

# Comparison

| Pattern | Best For | Weakness |
|----------|----------|----------|
| Planner–Executor | Workflow planning | Limited routing |
| ReAct | Tool reasoning | Single execution path |
| Supervisor–Worker | Multi-agent coordination | Needs routing |
| Router | Intelligent dispatch | Doesn't coordinate execution |
| Map–Reduce | Massive parallel work | Limited decision logic |

---

# Real-World Examples

## OpenAI Agents SDK

Routes requests between models, tools, and structured function calls while enforcing policies.

---

## Google ADK

Uses routing layers to dispatch work across modular agents with different capabilities.

---

## LangGraph

Routes execution between graph nodes based on workflow state and conditional edges.

---

## CrewAI

Manager agents dynamically assign work to specialists based on role and capability.

---

## Enterprise AI Gateways

Route requests according to

- cost
- latency
- region
- compliance
- model availability

---

# Related Skills

- orchestration.md
- delegation.md
- communication_protocols.md
- workflows.md

---

# Related Patterns

- planner_executor.md
- supervisor_worker.md
- react.md
- map_reduce.md

---

# Definition of Done

A Router implementation is production-ready only if

✓ Requests are classified before execution

✓ Routing policies are explicit and versioned

✓ Destinations are selected using objective criteria

✓ Cost and latency influence routing decisions

✓ Fallbacks handle unavailable destinations

✓ Routing decisions are observable and measurable

✓ Policies remain independent of execution logic

✓ Routing scales across agents, models, and workflows

✓ Security policies are enforced before dispatch

✓ The system consistently routes requests to the most appropriate execution path