# Skill

Fundamentals

Version: 1.0

---

# Goal

Understand the fundamental principles, architecture, and lifecycle of AI agents.

This skill establishes the conceptual foundation required to design, build, and operate production-grade autonomous systems.

An AI agent is not simply an LLM—it is an intelligent software system capable of perceiving, reasoning, planning, acting, and adapting to achieve goals.

---

# When to Load

Load this skill whenever building

- AI Agents
- Autonomous Systems
- Coding Agents
- Research Assistants
- Customer Support AI
- Workflow Automation
- Multi-Agent Systems

---

# Prerequisites

- llm_basics.md
- structured_outputs.md
- prompt_builder.md

---

# Core Principles

Language Models generate text.

Agents accomplish objectives.

The difference is

```
LLM

↓

Input

↓

Prediction

↓

Output
```

versus

```
Goal

↓

Observe

↓

Reason

↓

Plan

↓

Act

↓

Learn

↓

Repeat
```

Agents operate in continuous feedback loops.

---

# Definition of an AI Agent

An AI Agent is a software system that can

- Understand goals
- Maintain state
- Plan actions
- Use external tools
- Make decisions
- Adapt to new information
- Recover from failures
- Produce measurable outcomes

The language model is only one component of the system.

---

# Agent Architecture

A production agent typically consists of

```
User

↓

Goal

↓

Planner

↓

Reasoner

↓

Tool Manager

↓

Memory

↓

Executor

↓

Evaluator

↓

Result
```

Each component should be modular and independently testable.

---

# Core Components

## Goal

Defines what success looks like.

Examples

- Write an API
- Debug production issue
- Plan a vacation
- Summarize research

---

## Planner

Breaks complex objectives into executable tasks.

Responsible for

- sequencing
- prioritization
- dependency management

---

## Reasoner

Determines

- what information is needed
- which tool to use
- when to stop
- how to respond

Reasoning should remain internal and should not be exposed unless explicitly required.

---

## Tool Manager

Provides controlled access to

- APIs
- Databases
- Search
- File Systems
- Browsers
- Code Execution

Tools extend the agent beyond the model's built-in knowledge.

---

## Memory

Stores

- conversation state
- user preferences
- project information
- previous actions
- intermediate results

Memory enables continuity across tasks.

---

## Executor

Performs

- API calls
- database operations
- file manipulation
- shell commands
- code execution

Execution should be observable and reversible where possible.

---

## Evaluator

Measures whether the objective has been achieved.

Can verify

- correctness
- completeness
- policy compliance
- output quality

Evaluation should occur before task completion.

---

# Agent Lifecycle

```
Receive Goal

↓

Understand Context

↓

Create Plan

↓

Execute Step

↓

Observe Result

↓

Update State

↓

Evaluate Progress

↓

Repeat

↓

Finish
```

This loop distinguishes agents from traditional request-response systems.

---

# Types of Agents

## Reactive Agents

Respond immediately to events.

No long-term planning.

Examples

- FAQ bots
- command interpreters

Advantages

- fast
- simple

Trade-off

Limited autonomy.

---

## Goal-Based Agents

Optimize toward a defined objective.

Examples

- coding assistants
- research agents

Most production systems fall into this category.

---

## Utility-Based Agents

Choose the action with the highest expected value.

Useful when multiple valid strategies exist.

Examples

- scheduling
- logistics
- recommendation systems

---

## Deliberative Agents

Plan extensively before acting.

Suitable for

- long-running workflows
- enterprise automation
- scientific research

Trade-off

Higher latency.

---

## Hybrid Agents

Combine planning with reactive execution.

Recommended default for production systems.

---

# Levels of Autonomy

Level 0

User performs everything.

---

Level 1

AI suggests actions.

---

Level 2

AI performs actions with approval.

---

Level 3

AI performs routine tasks autonomously.

---

Level 4

AI coordinates multiple workflows independently.

---

Level 5

Fully autonomous systems operating within defined constraints.

Higher autonomy requires stronger guardrails.

---

# Request-Driven vs Event-Driven Agents

## Request-Driven

Activated by user input.

Examples

- ChatGPT
- Claude
- Coding assistants

---

## Event-Driven

Activated by external events.

Examples

- GitHub webhook
- email arrival
- deployment failure
- monitoring alerts

Recommended for automation.

---

# Single-Agent vs Multi-Agent

## Single Agent

Advantages

- Simpler
- Lower latency
- Easier debugging

Best for

- personal assistants
- coding assistants
- customer support

---

## Multi-Agent

Advantages

- specialization
- parallelism
- scalability

Trade-off

Higher coordination complexity.

---

# Agent Decision Loop

Every decision should answer

Do I have enough information?

↓

Should I retrieve more context?

↓

Do I need a tool?

↓

Can I answer safely?

↓

Have I achieved the goal?

Never execute unnecessary actions.

---

# Production Design Principles

Agents should

- Minimize tool usage
- Validate every tool output
- Persist important state
- Recover gracefully
- Support interruption
- Support retries
- Remain deterministic where possible
- Log every important decision
- Respect security boundaries

---

# Failure Modes

Common failures include

- infinite reasoning loops
- repeated tool calls
- stale memory
- hallucinated actions
- unauthorized execution
- missing context
- goal drift
- state corruption

Every failure mode should have mitigation strategies.

---

# Engineering Decisions

## Stateless Agents

Use when

- chat applications
- FAQs
- simple assistants

Advantages

- simple
- scalable

Trade-off

No continuity.

---

## Stateful Agents

Use when

- coding assistants
- enterprise workflows
- research projects

Recommended default.

---

## Hybrid Architecture

Planner

+

Memory

+

Tool Calling

+

Reflection

Recommended for nearly all production agents.

---

# Performance Considerations

Optimize

Planning latency

↓

Reasoning latency

↓

Tool execution time

↓

Memory retrieval

↓

Total task completion time

Measure each stage independently.

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Single agent | Simple | Limited specialization |
| Multi-agent | Parallel execution | Coordination overhead |
| Stateless | Scalable | No continuity |
| Stateful | Personalized | Higher complexity |
| Reactive | Fast | Limited planning |
| Deliberative | Better decisions | Higher latency |

---

# Security

Enforce

- authentication
- authorization
- least privilege
- tool permissions
- audit logging
- rate limiting
- tenant isolation

Agents should never possess unrestricted capabilities.

---

# Observability

Track

Goal completion

↓

Planning time

↓

Reasoning failures

↓

Tool failures

↓

Retry count

↓

Execution latency

↓

Memory retrieval latency

↓

Task completion rate

---

# Metrics

Monitor

Task Success Rate

Goal Completion Time

Average Tool Calls

Retry Rate

Planning Latency

Execution Latency

Failure Rate

Human Intervention Rate

Cost Per Task

---

# Common Failures

- Acting without planning
- Tool overuse
- Goal drift
- Infinite loops
- Ignoring failures
- Missing state persistence
- No evaluation phase
- Weak security boundaries

---

# Best Practices

- Plan before acting.
- Keep tools modular.
- Evaluate before completing.
- Persist meaningful state.
- Support interruption.
- Design for recovery.
- Separate reasoning from execution.
- Continuously measure performance.

---

# Anti-Patterns

❌ Using an LLM as the entire agent

❌ Hardcoding workflows

❌ Unlimited tool access

❌ No retry policy

❌ No memory management

❌ No evaluation

❌ No observability

❌ Infinite autonomous loops

---

# Real-World Production Examples

## GitHub Copilot

- Goal-based coding assistant.
- Retrieves repository context.
- Suggests code rather than executing changes autonomously.

---

## Claude Code

- Stateful coding agent.
- Uses tools for filesystem operations and terminal execution.
- Maintains task context across multi-step workflows.

---

## OpenHands

- Autonomous software engineering agent.
- Plans, writes, tests, and iterates on code changes.

---

## Devin

- Long-running software engineering agent.
- Executes multi-step tasks with planning, debugging, and evaluation.

---

## Cursor

- Hybrid coding assistant combining chat, repository context, tool use, and code editing.

---

# Testing

Verify

Goal understanding

Planning

Tool selection

State persistence

Failure recovery

Cancellation

Security boundaries

Evaluation

Human approval flows

---

# Review Checklist

□ Goal representation defined

□ Agent architecture documented

□ Planning implemented

□ Tool management isolated

□ Memory strategy selected

□ Evaluation integrated

□ Metrics configured

□ Security reviewed

□ Observability enabled

□ Tests passing

---

# Related Skills

- agent_architecture.md
- planning.md
- reasoning.md
- tool_calling.md
- state_management.md
- memory_integration.md

---

# Definition of Done

An AI agent implementation is production-ready only if

✓ Goals are explicit and measurable

✓ Planning precedes execution

✓ Tool usage is controlled and observable

✓ State is managed consistently

✓ Evaluation validates task completion

✓ Failures are recoverable

✓ Security boundaries are enforced

✓ Performance metrics are continuously monitored

✓ Human oversight is supported where required

✓ The agent reliably achieves its intended objectives under production workloads