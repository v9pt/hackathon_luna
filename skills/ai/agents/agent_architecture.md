# Skill

Agent Architecture

Version: 1.0

---

# Goal

Design modular, scalable, observable, and maintainable AI agent systems.

Agent architecture defines how intelligence, planning, memory, tools, and execution interact to accomplish goals safely and efficiently.

A production agent should be composed of loosely coupled components rather than a single monolithic prompt.

---

# When to Load

Load this skill whenever designing

- AI Agents
- Coding Assistants
- Enterprise AI
- Autonomous Workflows
- Multi-Agent Systems
- Research Agents

---

# Prerequisites

- fundamentals.md
- prompt_builder.md
- memory.md

---

# Core Principles

Separate concerns.

Every component should have one responsibility.

```
Goal

↓

Planner

↓

Executor

↓

Evaluator

↓

Result
```

Avoid tightly coupling reasoning, execution, and memory.

---

# High-Level Architecture

```
                User
                  │
                  ▼
          Goal Interpreter
                  │
                  ▼
             Planner
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
     Memory     Retriever  State
        │         │         │
        └──────┬──┴─────────┘
               ▼
          Tool Manager
               │
        ┌──────┼────────┐
        ▼      ▼        ▼
     Search   Files    APIs
               │
               ▼
           Executor
               │
               ▼
          Evaluator
               │
               ▼
          Final Response
```

---

# Architectural Layers

## Presentation Layer

Responsible for

- Chat UI
- REST APIs
- CLI
- Voice Interfaces

Never contain business logic.

---

## Orchestration Layer

Coordinates

- Planning
- Routing
- State
- Tool execution

Acts as the brain of the application.

---

## Intelligence Layer

Contains

- LLMs
- Prompt Builder
- Reasoning
- Reflection
- Evaluation

Provider-independent whenever possible.

---

## Tool Layer

Provides controlled access to

- Databases
- APIs
- Search
- File systems
- Browsers
- Code execution

Tools should expose well-defined interfaces.

---

## Memory Layer

Stores

- Session state
- Long-term memory
- Semantic memory
- User profiles
- Agent history

Memory should be independent of prompts.

---

## Infrastructure Layer

Includes

- Queues
- Databases
- Object storage
- Logging
- Monitoring
- Authentication
- Deployment

Infrastructure should be replaceable without changing agent logic.

---

# Planner–Executor–Evaluator Pattern

Recommended default architecture.

```
Goal

↓

Planner

↓

Execution Plan

↓

Executor

↓

Evaluation

↓

Complete

or

Replan
```

Benefits

- modularity
- recoverability
- easier testing

---

# Blackboard Architecture

Shared knowledge repository used by multiple components.

```
Planner

↓

Blackboard

↑

Executor

↓

Evaluator
```

Useful for

- multi-agent systems
- collaborative workflows
- shared state

---

# Event-Driven Architecture

Agents react to events instead of requests.

Examples

- GitHub push
- Email received
- Deployment failed
- Calendar updated

Suitable for automation platforms.

---

# Actor Model

Each agent is an independent actor.

Characteristics

- isolated state
- asynchronous messaging
- fault isolation

Useful for distributed systems.

---

# Message Bus

Coordinates communication between components.

```
Planner

↓

Message Bus

↓

Workers

↓

Results

↓

Planner
```

Benefits

- decoupling
- scalability
- resilience

---

# Plugin Architecture

Extend agents without modifying core logic.

Examples

Plugins

- GitHub
- Slack
- Jira
- Notion
- Browser
- Terminal

Prefer dependency injection over hardcoded integrations.

---

# State Management

Separate

Session State

↓

Workflow State

↓

Persistent Memory

↓

Application State

Never store everything in one object.

---

# Dependency Injection

Inject

LLMs

↓

Memory

↓

Retrievers

↓

Tools

↓

Evaluators

Improves

- testing
- portability
- maintainability

---

# Sandboxing

Execute potentially dangerous operations inside isolated environments.

Examples

- Python execution
- Shell commands
- Browser automation

Never allow unrestricted execution on production hosts.

---

# Error Recovery

Failures should trigger

Retry

↓

Fallback

↓

Replan

↓

Human Escalation

↓

Abort

Every component should fail gracefully.

---

# Scalability

Scale independently

Planner

Executor

Memory

Retriever

Workers

Avoid scaling the entire application as a single unit.

---

# Engineering Decisions

## Monolithic Agent

Use when

- prototypes
- hackathons
- small internal tools

Advantages

- simple
- fast to build

Trade-off

Hard to maintain.

---

## Modular Agent

Use when

- production systems
- enterprise AI
- long-term projects

Recommended default.

---

## Microservice Architecture

Use when

- multiple teams
- independent deployments
- high traffic

Trade-off

Higher operational complexity.

---

## Event-Driven Architecture

Use when

- automation
- monitoring
- workflow engines

Recommended for asynchronous systems.

---

# Performance Considerations

Optimize

Planning latency

↓

Tool latency

↓

Memory retrieval

↓

Message passing

↓

Execution throughput

Measure each layer independently.

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Monolith | Simple | Poor scalability |
| Modular | Flexible | More components |
| Microservices | Independent scaling | Operational overhead |
| Event-driven | Responsive | Debugging complexity |
| Actor model | Fault isolation | Message coordination |

---

# Security

Enforce

- authentication
- authorization
- least privilege
- sandboxing
- secret management
- audit logging
- tenant isolation

Architecture should assume zero trust.

---

# Observability

Track

Planning latency

↓

Tool execution

↓

Memory retrieval

↓

Message queue depth

↓

Failure rate

↓

Task completion

↓

Infrastructure health

---

# Metrics

Monitor

Task Success Rate

Planner Latency

Execution Latency

Tool Success Rate

Queue Length

Memory Retrieval Time

Average Cost

Resource Utilization

---

# Common Failures

- Monolithic design
- Tight coupling
- Shared mutable state
- No retries
- No observability
- Blocking execution
- Unrestricted tool access
- Missing dependency injection

---

# Best Practices

- Keep components independent.
- Separate orchestration from intelligence.
- Design tools as plugins.
- Scale services independently.
- Use dependency injection.
- Sandbox unsafe execution.
- Build observable systems.
- Plan for failure.

---

# Anti-Patterns

❌ One giant agent class

❌ Hardcoded providers

❌ Global mutable state

❌ Direct tool access everywhere

❌ No retry strategy

❌ Business logic inside prompts

❌ Tight coupling between planner and executor

---

# Real-World Production Examples

## OpenAI Agents SDK

- Modular agent runtime.
- Structured tool interfaces.
- Explicit handoffs between agents.

---

## LangGraph

- Graph-based orchestration.
- Stateful execution.
- Durable workflows.

---

## AutoGen

- Conversational multi-agent architecture.
- Message-driven collaboration.
- Planner/worker patterns.

---

## CrewAI

- Role-based agents coordinated by shared workflows.
- Task delegation and specialization.

---

## Claude Code

- Planner, filesystem tools, terminal execution, and memory integrated into a modular runtime rather than a single prompt.

---

# Testing

Verify

Architecture boundaries

Dependency injection

Plugin loading

State isolation

Retry behavior

Failure recovery

Security controls

Scalability

---

# Review Checklist

□ Layered architecture defined

□ Planner–Executor–Evaluator implemented

□ Tool interfaces standardized

□ State management separated

□ Dependency injection configured

□ Sandboxing enabled

□ Observability implemented

□ Metrics configured

□ Security reviewed

□ Tests passing

---

# Related Skills

- planning.md
- reasoning.md
- tool_calling.md
- orchestration.md
- state_management.md

---

# Definition of Done

A production agent architecture is complete only if

✓ Components are modular and loosely coupled

✓ Planning, execution, and evaluation are separated

✓ State is managed consistently

✓ Tools are accessed through standardized interfaces

✓ Failure recovery is implemented

✓ Security boundaries are enforced

✓ Observability covers every architectural layer

✓ Performance bottlenecks are measurable

✓ Components can scale independently

✓ The architecture supports future extension without major redesign