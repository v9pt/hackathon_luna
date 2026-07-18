# Skill

Reasoning

Version: 1.0

---

# Goal

Design reliable reasoning systems that enable AI agents to analyze problems, make decisions, choose tools, evaluate outcomes, and adapt their execution strategy.

Reasoning is the decision-making engine of an AI agent.

A production agent should reason deliberately, efficiently, and safely before executing actions.

---

# When to Load

Load this skill whenever building

- AI Agents
- Coding Agents
- Research Assistants
- Autonomous Workflows
- Multi-Agent Systems
- Enterprise AI

---

# Prerequisites

- fundamentals.md
- planning.md
- prompt_builder.md

---

# Core Principles

Reasoning transforms

Information

↓

Understanding

↓

Decision

↓

Action

↓

Evaluation

The objective is not to think longer.

The objective is to think better.

---

# Responsibilities

A reasoning engine should

- Analyze goals
- Select tools
- Decide execution order
- Evaluate uncertainty
- Choose strategies
- Detect failures
- Trigger replanning

It should not

- Execute tools
- Store long-term memory
- Manage infrastructure

---

# Reasoning Pipeline

```
Goal

↓

Context

↓

Reasoning

↓

Decision

↓

Action

↓

Observation

↓

Reflection

↓

Next Decision
```

Reasoning is iterative.

---

# Types of Reasoning

Production agents combine multiple reasoning strategies.

Examples

- Reactive
- Deliberative
- Deductive
- Inductive
- Abductive
- Tool-Assisted
- Reflective

---

# Reactive Reasoning

Immediate response.

```
Input

↓

Decision

↓

Action
```

Advantages

- Fast
- Low latency

Trade-off

Poor long-term planning.

---

# Deliberative Reasoning

Analyze before acting.

```
Goal

↓

Think

↓

Evaluate

↓

Execute
```

Recommended for complex tasks.

---

# Deductive Reasoning

General rule

↓

Specific conclusion

Example

```
All authenticated users can deploy.

Alice is authenticated.

↓

Alice can deploy.
```

Useful for policy engines.

---

# Inductive Reasoning

Specific observations

↓

General pattern

Useful for

- analytics
- monitoring
- recommendations

---

# Abductive Reasoning

Infer the most likely explanation.

Example

```
Tests fail.

↓

Dependency update is probably responsible.
```

Useful for debugging.

---

# Tool-Assisted Reasoning

The agent reasons about

- whether a tool is required
- which tool to use
- when to stop using tools

Never call tools automatically.

---

# Reflection

Reason

↓

Execute

↓

Evaluate

↓

Improve

Reflection improves future decisions.

---

# Chain of Thought

Break reasoning into intermediate logical steps.

Benefits

- Better planning
- Better decomposition
- Better debugging

Trade-off

Higher token usage.

Implementation should remain internal unless explicitly required.

---

# ReAct Pattern

Reason

↓

Act

↓

Observe

↓

Reason

↓

Repeat

Excellent for

- tool usage
- search
- coding
- research

Recommended default.

---

# ReWOO

Reason once.

Generate an execution plan.

Execute without repeated reasoning.

Advantages

- Fewer LLM calls
- Lower cost
- Higher throughput

Trade-off

Less adaptive.

---

# Tree of Thoughts

Explore multiple reasoning branches.

```
Goal

↓

Idea A

Idea B

Idea C

↓

Best Branch

↓

Solution
```

Useful for

- optimization
- difficult reasoning
- planning

Trade-off

High compute cost.

---

# Graph of Thoughts

Generalizes Tree of Thoughts.

Allows

- branching
- merging
- revisiting ideas

Best for

- research
- scientific workflows
- enterprise planning

---

# Self-Consistency

Generate multiple reasoning paths.

Choose the most consistent result.

Useful when

Correctness is more important than latency.

---

# Reflexion

Execute

↓

Evaluate

↓

Learn

↓

Retry

Recommended for

- coding agents
- debugging
- autonomous systems

---

# LLM Compiler

Separate

Planning

↓

Scheduling

↓

Execution

↓

Verification

Reduces repeated reasoning.

Useful for long workflows.

---

# CodeAct

Reason

↓

Execute Code

↓

Observe

↓

Continue

Ideal for coding agents.

---

# Decision Loop

Every reasoning cycle should answer

Do I understand the goal?

↓

Do I need more information?

↓

Should I retrieve context?

↓

Should I use a tool?

↓

Can I answer safely?

↓

Should I continue?

---

# Uncertainty Handling

If confidence is low

Retrieve

↓

Ask User

↓

Use Tool

↓

Escalate

↓

Stop

Never hallucinate certainty.

---

# Engineering Decisions

## ReAct

Use when

- coding
- RAG
- search
- APIs

Recommended default.

---

## ReWOO

Use when

Tool sequence is predictable.

Lower cost.

---

## Reflexion

Use when

Quality matters more than latency.

Recommended for software engineering.

---

## Tree of Thoughts

Use when

Searching many alternatives.

Higher compute cost.

---

## Graph of Thoughts

Use when

Complex interconnected reasoning.

Enterprise AI.

---

## LLM Compiler

Use when

Long execution pipelines.

Multi-step automation.

---

# Pattern Comparison

| Pattern | Best For | Weakness |
|----------|----------|----------|
| ReAct | General agents | Many model calls |
| ReWOO | Efficient workflows | Less adaptive |
| Reflexion | Coding | Higher latency |
| Tree of Thoughts | Optimization | Expensive |
| Graph of Thoughts | Research | Complex runtime |
| Self-Consistency | High accuracy | Multiple generations |
| CodeAct | Software engineering | Requires execution environment |
| LLM Compiler | Long workflows | Complex scheduler |

---

# Failure Recovery

If reasoning fails

Retrieve more context

↓

Alternative strategy

↓

Reflection

↓

Replan

↓

Human approval

↓

Abort

---

# Performance Considerations

Optimize

Reasoning latency

↓

Reasoning quality

↓

Token usage

↓

Tool selection

↓

Decision accuracy

Avoid unnecessary reasoning cycles.

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Reactive | Fast | Poor planning |
| Deliberative | Better decisions | Higher latency |
| ReAct | Flexible | More LLM calls |
| ReWOO | Efficient | Less adaptable |
| Reflexion | Higher quality | More expensive |

---

# Security

Protect against

- Prompt injection
- Tool abuse
- Unsafe autonomous actions
- Infinite reasoning loops
- Unauthorized decisions

Reasoning should always respect system policies.

---

# Observability

Track

Reasoning latency

↓

Reasoning iterations

↓

Tool decisions

↓

Reflection count

↓

Decision accuracy

↓

Failure rate

↓

Replans

---

# Metrics

Monitor

Reasoning Time

Average Iterations

Tool Selection Accuracy

Reflection Rate

Replan Rate

Goal Completion Rate

Token Usage

Cost Per Task

---

# Common Failures

- Acting immediately
- Infinite reasoning loops
- Choosing unnecessary tools
- Ignoring uncertainty
- Repeating failed strategies
- Hallucinated decisions
- No evaluation

---

# Best Practices

- Prefer ReAct for general agents.
- Use Reflection for coding agents.
- Separate reasoning from execution.
- Stop when confidence is sufficient.
- Measure reasoning quality.
- Minimize unnecessary model calls.
- Trigger replanning early.

---

# Anti-Patterns

❌ Thinking forever

❌ Tool spam

❌ No uncertainty handling

❌ No reflection

❌ No stopping condition

❌ Hidden architecture coupling

❌ Ignoring previous failures

---

# Real-World Production Examples

## Claude Code

- Uses iterative reasoning before filesystem and terminal operations.
- Replans after failed edits or test runs.
- Balances reasoning with execution latency.

---

## OpenAI Codex

- Reasons about repository context before editing.
- Selects tools based on task requirements.
- Uses execution feedback to refine changes.

---

## Devin

- Combines long-horizon planning with continuous reasoning.
- Revises plans after failed builds or deployments.

---

## OpenHands

- Alternates between reasoning, tool execution, and validation.
- Uses execution results to guide subsequent decisions.

---

## Cursor

- Chooses between direct code generation, repository search, and editing tools based on context.

---

# Testing

Verify

Reasoning strategy selection

Tool decisions

Reflection

Failure recovery

Uncertainty handling

Stopping conditions

Replanning

Pattern selection

---

# Review Checklist

□ Reasoning strategy selected

□ Decision loop implemented

□ Tool reasoning isolated

□ Reflection supported

□ Uncertainty handling implemented

□ Metrics configured

□ Observability enabled

□ Security reviewed

□ Failure recovery tested

□ Tests passing

---

# Related Skills

- tool_calling.md
- reflection.md
- self_correction.md
- planning.md
- orchestration.md

---

# Definition of Done

A reasoning system is production-ready only if

✓ Reasoning is separated from execution

✓ Appropriate reasoning patterns are selected

✓ Tool usage is intentional and observable

✓ Reflection improves future decisions

✓ Uncertainty is handled safely

✓ Failure recovery is integrated

✓ Reasoning quality is measurable

✓ Performance remains within acceptable limits

✓ Security constraints are enforced

✓ The agent consistently makes high-quality decisions under production workloads