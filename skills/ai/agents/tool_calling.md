# Skill

Tool Calling

Version: 1.0

---

# Goal

Design reliable, secure, and scalable tool execution systems that enable AI agents to interact with external systems, retrieve information, execute actions, and accomplish real-world tasks.

Tool calling transforms a language model from a conversational system into an autonomous software system.

A production agent should treat every tool invocation as a controlled software operation rather than an LLM capability.

---

# When to Load

Load this skill whenever building

- AI Agents
- Coding Assistants
- Enterprise Automation
- Browser Agents
- Research Agents
- RAG Systems
- Workflow Engines
- Multi-Agent Systems

---

# Prerequisites

- reasoning.md
- planning.md
- agent_architecture.md
- structured_outputs.md

---

# Core Principles

LLMs generate decisions.

Tools execute actions.

```
Reason

↓

Choose Tool

↓

Validate

↓

Execute

↓

Observe

↓

Continue
```

The LLM should decide **what** to do.

The runtime should decide **how** to do it safely.

---

# Responsibilities

A Tool Runtime should

- Discover tools
- Validate inputs
- Enforce permissions
- Execute tools
- Handle retries
- Validate outputs
- Log executions
- Return structured results

A Tool Runtime should not

- Perform reasoning
- Store business logic
- Manage long-term memory

---

# Tool Architecture

```
User

↓

Planner

↓

Reasoner

↓

Tool Selector

↓

Tool Registry

↓

Permission Manager

↓

Executor

↓

Tool

↓

Validator

↓

Observation

↓

Reasoner
```

Reasoning and execution should remain separate.

---

# Tool Lifecycle

```
Need Identified

↓

Select Tool

↓

Validate Input

↓

Permission Check

↓

Execute

↓

Validate Output

↓

Observe Result

↓

Continue Reasoning
```

Every tool invocation follows this lifecycle.

---

# Tool Registry

Maintain a centralized registry.

Every tool should expose

- Name
- Description
- Version
- Category
- Input Schema
- Output Schema
- Timeout
- Retry Policy
- Permissions
- Cost
- Rate Limits

The registry should be provider-independent.

---

# Tool Discovery

Agents should discover tools dynamically.

Selection criteria

- Capability
- Availability
- Permissions
- Cost
- Latency
- Reliability

Avoid hardcoded tool lists.

---

# Tool Selection

The agent should determine

Do I need a tool?

↓

Which tool?

↓

One tool?

↓

Multiple tools?

↓

Parallel?

↓

Sequential?

↓

Stop?

Selecting the wrong tool is often worse than using none.

---

# Tool Interface Contract

Every production tool should implement

Name

Description

Version

Input Schema

Output Schema

Authentication

Authorization

Timeout

Retry Policy

Rate Limits

Error Types

Observability Hooks

Documentation

Example Usage

Stable interfaces simplify orchestration.

---

# Structured Inputs

Inputs should be schema-validated.

Examples

JSON Schema

Pydantic

Zod

Protocol Buffers

Reject invalid requests before execution.

---

# Structured Outputs

Tools should return structured data.

Example

```
{
  "status": "success",
  "data": {},
  "metadata": {},
  "execution_time": 210
}
```

Avoid parsing natural language whenever possible.

---

# Tool Validation

Validate

Input

↓

Schema

↓

Permissions

↓

Availability

↓

Execution

↓

Output

↓

Business Rules

Never trust tool outputs blindly.

---

# Authentication

Support

API Keys

OAuth

JWT

Service Accounts

MCP Authentication

Never expose credentials to the LLM.

---

# Authorization

Verify

User

↓

Role

↓

Workspace

↓

Resource

↓

Operation

Tool execution should always enforce least privilege.

---

# Permission Model

Separate permissions by

Read

Write

Execute

Delete

Admin

Never expose unrestricted tools.

---

# Idempotency

Some tools should safely retry.

Examples

GET requests

Search

Document retrieval

Avoid retrying non-idempotent operations unless explicitly supported.

---

# Retries

Retry

Temporary failures

↓

Network issues

↓

Provider overload

↓

Timeouts

Do not retry

Validation failures

Authentication failures

Permission errors

---

# Timeouts

Every tool should define

Connection Timeout

Execution Timeout

Overall Timeout

Never allow infinite execution.

---

# Circuit Breakers

Repeated failures should trigger

Open Circuit

↓

Temporary Block

↓

Health Check

↓

Recovery

Protect dependent systems.

---

# Rate Limiting

Apply limits by

User

Workspace

Organization

Tool

IP

Provider

Prevent abuse and runaway agents.

---

# Caching

Cache

Search

Retrieval

Configuration

Metadata

Avoid caching mutable operations.

---

# Sequential Tool Calls

```
Search

↓

Read File

↓

Generate Summary
```

Required when dependencies exist.

---

# Parallel Tool Calls

```
GitHub

+

Slack

+

Jira

↓

Merge Results
```

Use when operations are independent.

---

# Tool Chaining

One tool's output becomes another tool's input.

```
Search

↓

Read

↓

Summarize

↓

Store
```

Validate every intermediate result.

---

# Dynamic Tool Selection

Instead of

```
Always Search
```

Prefer

```
Need Information?

↓

Yes

↓

Search

↓

Continue

↓

No

↓

Answer
```

Minimize unnecessary tool usage.

---

# Tool Versioning

Support

Semantic Versioning

Backward Compatibility

Deprecation

Migration

Agents should know which version they are invoking.

---

# Error Recovery

If execution fails

Retry

↓

Alternative Tool

↓

Fallback

↓

Replan

↓

Escalate

↓

Abort

Tool failure should not crash the agent.

---

# Pattern References

## ReAct

Reason

↓

Choose Tool

↓

Execute

↓

Observe

↓

Reason Again

See

patterns/react.md

---

## Planner Executor

Planner chooses work.

Executor invokes tools.

See

patterns/planner_executor.md

---

## Supervisor Worker

Supervisor delegates

↓

Workers execute tools

↓

Results merged

See

patterns/supervisor_worker.md

---

## Router

Select best tool

↓

Execute

↓

Return

See

patterns/router.md

---

## Map Reduce

Parallel tools

↓

Aggregate

↓

Summarize

See

patterns/map_reduce.md

---

# Engineering Decisions

## Direct Tool Calling

Use when

Simple agents

One tool

Internal utilities

Advantages

Simple

Low latency

Trade-off

Limited flexibility.

---

## Registry-Based Runtime

Use when

Production agents

Enterprise AI

Recommended default.

---

## Dynamic Discovery

Use when

Plugin ecosystems

Large tool collections

MCP servers

Trade-off

Higher runtime complexity.

---

## Parallel Execution

Use when

Independent tasks

Multiple APIs

Research workflows

Improves throughput.

---

# Runtime Architecture

```
Planner

↓

Reasoner

↓

Tool Selector

↓

Registry

↓

Permission Check

↓

Executor

↓

Validation

↓

Observation

↓

Planner
```

---

# Performance Considerations

Optimize

Tool Selection Latency

↓

Execution Time

↓

Serialization

↓

Network Calls

↓

Parallelism

↓

Cache Hit Rate

Reasoning should not dominate execution time.

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Direct calls | Simple | Low scalability |
| Registry | Flexible | More infrastructure |
| Parallel tools | Faster | Synchronization complexity |
| Sequential tools | Predictable | Higher latency |
| Dynamic discovery | Extensible | More runtime overhead |

---

# Security

Enforce

Authentication

Authorization

Sandboxing

Rate limiting

Secrets management

Audit logging

Input validation

Output validation

Least privilege

Zero trust should apply to every tool invocation.

---

# Observability

Track

Tool Selection Time

↓

Execution Latency

↓

Success Rate

↓

Retry Count

↓

Timeout Rate

↓

Error Types

↓

Provider Latency

↓

Cost

---

# Metrics

Monitor

Tool Success Rate

Average Execution Time

Retry Rate

Timeout Rate

Cache Hit Rate

Average Tool Calls Per Task

Cost Per Tool

Provider Availability

Parallel Execution Efficiency

---

# Common Failures

- Calling unnecessary tools
- Ignoring permissions
- Missing retries
- Infinite tool loops
- Parsing free-form outputs
- No timeout
- Hardcoded providers
- No audit logs

---

# Best Practices

- Treat tools as software services.
- Validate every input and output.
- Keep interfaces versioned.
- Prefer structured schemas.
- Execute tools through a registry.
- Minimize tool usage.
- Log every execution.
- Monitor reliability continuously.

---

# Anti-Patterns

❌ LLM directly executes business logic

❌ Unlimited tool permissions

❌ Parsing natural language responses

❌ Hardcoded API integrations

❌ Missing retries

❌ No observability

❌ No timeout policy

❌ No validation

---

# Real-World Production Examples

## Claude Code

- Uses structured filesystem, terminal, and search tools.
- Validates execution results before continuing.
- Separates reasoning from execution.

---

## OpenAI Agents SDK

- Provides schema-based tool definitions.
- Supports structured function invocation.
- Isolates tool execution from model reasoning.

---

## GitHub Copilot

- Calls repository search and symbol lookup tools before generating edits.
- Minimizes unnecessary repository scans.

---

## Cursor

- Dynamically switches between search, edit, terminal, and code analysis tools.
- Executes only the tools required for the current task.

---

## MCP Ecosystem

- Discovers external tools through standardized servers.
- Decouples agent logic from tool implementations.

---

# Testing

Verify

Tool discovery

Schema validation

Authentication

Authorization

Permission enforcement

Retries

Timeouts

Circuit breakers

Parallel execution

Sequential execution

Tool chaining

Version compatibility

Observability

---

# Review Checklist

□ Tool registry implemented

□ Interface contracts defined

□ Structured schemas validated

□ Authentication enforced

□ Authorization enforced

□ Retry strategy configured

□ Timeouts implemented

□ Circuit breakers enabled

□ Metrics configured

□ Observability enabled

□ Pattern references documented

□ Tests passing

---

# Related Skills

- state_management.md
- memory_integration.md
- orchestration.md
- delegation.md
- workflows.md
- patterns/react.md
- patterns/planner_executor.md
- patterns/router.md
- patterns/supervisor_worker.md
- patterns/map_reduce.md

---

# Definition of Done

A tool calling system is production-ready only if

✓ Tool discovery is dynamic and provider-independent

✓ Every tool follows a standardized interface contract

✓ Input and output schemas are validated

✓ Authentication and authorization are enforced

✓ Retries, timeouts, and circuit breakers are implemented

✓ Parallel and sequential execution are supported

✓ Every invocation is observable and auditable

✓ Tool failures trigger recovery strategies

✓ Security follows least-privilege principles

✓ The runtime reliably executes external actions under production workloads