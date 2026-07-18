# Skill

Reflection

Version: 1.0

---

# Goal

Design reliable reflection systems that enable AI agents to evaluate their own work, identify mistakes, measure progress toward goals, and improve future decisions before continuing execution.

Reflection provides an internal feedback loop that improves quality, robustness, and reliability.

A production reflection system should continuously assess execution without becoming trapped in endless self-analysis.

---

# When to Load

Load this skill whenever building

- Coding Agents
- Autonomous Agents
- Enterprise AI
- Research Systems
- Long-running Workflows
- Multi-Agent Systems

---

# Prerequisites

- reasoning.md
- workflows.md
- state_management.md
- task_decomposition.md

---

# Core Principles

Plan

↓

Execute

↓

Reflect

↓

Improve

↓

Continue

Reflection should improve execution rather than replace it.

---

# Responsibilities

Reflection systems should

- Evaluate outputs
- Detect mistakes
- Measure goal progress
- Recommend improvements
- Trigger replanning
- Decide whether execution should continue

Reflection systems should not

- Execute tools
- Rewrite history
- Replace reasoning

---

# Reflection Lifecycle

```
Execute

↓

Collect Results

↓

Evaluate

↓

Identify Issues

↓

Recommend Actions

↓

Continue or Replan
```

Reflection should occur after meaningful execution milestones.

---

# Why Reflection Matters

Without reflection

- Errors accumulate
- Bugs propagate
- Hallucinations persist
- Wrong assumptions remain hidden

With reflection

- Higher accuracy
- Better reliability
- Safer execution
- Adaptive behavior

---

# Types of Reflection

## Immediate Reflection

Occurs after each task.

Useful for

- Tool execution
- API calls
- Code edits

---

## Periodic Reflection

Occurs after multiple tasks.

Useful for

- Long workflows
- Research
- Large coding sessions

---

## Final Reflection

Occurs before completion.

Questions

- Was the goal achieved?
- Are tests passing?
- Is anything missing?

Required before task completion.

---

## Human Reflection

Allow users to review outputs before irreversible actions.

Examples

- Production deployment
- Payments
- Data deletion

---

# Reflection Questions

Every reflection cycle should answer

Did the task succeed?

↓

Was the result correct?

↓

Were tools used appropriately?

↓

Are there remaining risks?

↓

Should execution continue?

↓

Should the plan change?

---

# Reflection Signals

Evaluate

Task Success

↓

Test Results

↓

Tool Outputs

↓

User Feedback

↓

Performance Metrics

↓

Confidence

Reflection should use objective signals whenever possible.

---

# Reflection Triggers

Trigger reflection after

- Tool execution
- Task completion
- Failed validation
- Test failures
- User feedback
- Workflow milestones

Avoid reflecting after every token generation.

---

# Reflection Outcomes

Reflection may result in

Continue

Retry

Replan

Delegate

Escalate

Abort

Each outcome should have clear criteria.

---

# Confidence Assessment

Estimate confidence using

Validation Results

↓

Test Coverage

↓

Evidence

↓

Agreement Between Tools

↓

Model Confidence

Low confidence should increase verification.

---

# Pattern References

## Reflexion

Execute

↓

Reflect

↓

Retry

↓

Improve

See

patterns/reflexion.md

---

## ReAct

Observe

↓

Reason

↓

Continue

See

patterns/react.md

---

## Planner Executor

Planner evaluates execution quality before scheduling additional work.

See

patterns/planner_executor.md

---

# Engineering Decisions

## Immediate Reflection

Use when

High-risk tasks

Code generation

Financial operations

Recommended default.

---

## Periodic Reflection

Use when

Long-running workflows

Research

Large projects

---

## Final Reflection

Required before

Deployment

Task completion

Human handoff

---

## Human Review

Use when

High-impact decisions

Legal

Medical

Security

Production changes

---

# Runtime Architecture

```
Execution

↓

Reflection Engine

↓

Validation

↓

Decision

↓

Continue or Replan
```

---

# Performance Considerations

Optimize

Reflection latency

↓

Validation cost

↓

Feedback quality

↓

Token usage

↓

Decision accuracy

Reflection should improve quality without excessive overhead.

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Immediate reflection | Early error detection | Higher latency |
| Periodic reflection | Lower overhead | Errors accumulate longer |
| Final reflection | Efficient | Late discovery of issues |
| Human review | Highest confidence | Slowest execution |

---

# Security

Protect against

- Reflection loops
- Prompt injection during evaluation
- Manipulated tool outputs
- Unsafe retries
- Unauthorized workflow continuation

Reflection should never bypass security controls.

---

# Observability

Track

Reflection count

↓

Reflection latency

↓

Detected issues

↓

Retries

↓

Replans

↓

Confidence trends

↓

Quality improvements

---

# Metrics

Monitor

Reflection Frequency

Issue Detection Rate

Retry Rate

Replan Rate

Validation Success Rate

Confidence Score

Quality Improvement Rate

Task Success Rate

---

# Common Failures

- Reflecting too often
- Never reflecting
- Ignoring validation
- Infinite retry loops
- High confidence without evidence
- Repeating failed strategies

---

# Best Practices

- Reflect after meaningful milestones.
- Base reflection on evidence.
- Separate reflection from execution.
- Measure confidence objectively.
- Trigger replanning when needed.
- Limit retry attempts.
- Include human review for critical actions.
- Log reflection decisions.

---

# Anti-Patterns

❌ Infinite reflection loops

❌ Reflection without validation

❌ Ignoring failures

❌ Blind confidence

❌ No stopping condition

❌ Repeating identical retries

❌ Reflection replacing execution

---

# Real-World Production Examples

## Claude Code

- Reviews edits after execution.
- Uses test results and diagnostics to determine whether additional work is required.
- Iteratively improves code before completion.

---

## OpenHands

- Evaluates execution results after repository changes.
- Uses failures to trigger replanning.

---

## SWE-Agent

- Reviews repository state after each modification.
- Iteratively refines solutions until tests pass.

---

## Devin

- Continuously evaluates progress toward long-running goals.
- Revises plans when intermediate outcomes fail.

---

## OpenAI Codex

- Uses execution feedback to determine whether further edits are required before returning results.

---

# Testing

Verify

Reflection triggers

Validation quality

Confidence estimation

Retry logic

Replanning

Stopping conditions

Human approval

Issue detection

---

# Review Checklist

□ Reflection lifecycle defined

□ Validation integrated

□ Confidence measured

□ Retry policy configured

□ Replanning supported

□ Human review supported

□ Metrics configured

□ Observability enabled

□ Security reviewed

□ Tests passing

---

# Related Skills

- self_correction.md
- reasoning.md
- workflows.md
- orchestration.md
- patterns/reflexion.md
- patterns/react.md
- patterns/planner_executor.md

---

# Definition of Done

A reflection system is production-ready only if

✓ Reflection is triggered at meaningful execution milestones

✓ Decisions are based on objective validation signals

✓ Confidence is measurable and evidence-based

✓ Reflection can trigger retries, replanning, or escalation

✓ Human review is supported for high-impact actions

✓ Reflection decisions are observable and auditable

✓ Retry loops are bounded

✓ Security controls cannot be bypassed

✓ Reflection measurably improves execution quality

✓ Agents consistently deliver more reliable outcomes through continuous evaluation