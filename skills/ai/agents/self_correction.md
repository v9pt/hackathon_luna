# Skill

Self Correction

Version: 1.0

---

# Goal

Design reliable self-correction systems that enable AI agents to identify, repair, and validate mistakes autonomously while minimizing repeated failures and preventing infinite correction loops.

Self-correction transforms evaluation into improvement.

A production self-correction system should improve output quality through evidence-based iteration while respecting safety limits and execution budgets.

---

# When to Load

Load this skill whenever building

- Coding Agents
- Autonomous AI Systems
- Enterprise Workflows
- Research Agents
- Multi-Agent Systems
- Long-running Automation

---

# Prerequisites

- reflection.md
- reasoning.md
- workflows.md
- tool_calling.md

---

# Core Principles

Execute

↓

Validate

↓

Identify Error

↓

Correct

↓

Verify

↓

Continue

Correction should always be evidence-driven.

---

# Responsibilities

Self-correction systems should

- Detect failures
- Diagnose root causes
- Generate corrections
- Validate fixes
- Learn from repeated failures
- Escalate when correction fails

Self-correction systems should not

- Retry indefinitely
- Ignore validation
- Rewrite unrelated work
- Override security constraints

---

# Why Self-Correction Matters

Without self-correction

- Small mistakes become larger failures
- Human intervention increases
- Agents repeat the same errors
- Long-running workflows fail

With self-correction

- Higher autonomy
- Better reliability
- Lower operational cost
- Improved task completion

---

# Self-Correction Lifecycle

```
Execute

↓

Validate

↓

Detect Failure

↓

Diagnose

↓

Generate Fix

↓

Verify

↓

Success?

↓

Continue

or

Escalate
```

---

# Error Categories

## Reasoning Errors

Examples

- Incorrect assumptions
- Invalid logic
- Wrong task ordering

Correction

Replan

---

## Tool Errors

Examples

- Wrong tool selected
- Invalid parameters
- Failed API calls

Correction

Retry

Alternative tool

---

## Code Errors

Examples

- Compilation failures
- Test failures
- Runtime exceptions

Correction

Generate patch

Run tests again

---

## Workflow Errors

Examples

- Invalid dependency
- Missing checkpoint
- Incorrect execution order

Correction

Rebuild workflow

Resume execution

---

## Data Errors

Examples

- Missing input
- Invalid schema
- Corrupted data

Correction

Validate

Request additional information

---

# Root Cause Analysis

Identify

Symptom

↓

Evidence

↓

Possible Causes

↓

Most Likely Cause

↓

Correction Strategy

Avoid correcting symptoms without understanding causes.

---

# Correction Strategies

## Retry

Useful for

- Temporary network failures
- Provider overload
- Timeout

---

## Regenerate

Useful for

- Low-quality outputs
- Incorrect reasoning
- Hallucinations

---

## Replan

Useful for

- Invalid task decomposition
- Dependency failures
- Goal changes

---

## Alternative Tool

Useful when

Current tool repeatedly fails.

---

## Human Escalation

Use when

Repeated failures occur

or

High-risk actions require approval.

---

# Validation Before Correction

Always verify

Is the error real?

↓

Is correction necessary?

↓

Can it be corrected safely?

↓

Will correction affect other tasks?

Never modify validated work unnecessarily.

---

# Verification After Correction

Every correction should be validated.

Examples

- Unit tests
- Integration tests
- Schema validation
- Static analysis
- Human approval

Correction without verification is incomplete.

---

# Retry Limits

Define maximum retries.

Example

```
Attempt 1

↓

Attempt 2

↓

Attempt 3

↓

Escalate
```

Never allow infinite correction loops.

---

# Learning From Failures

Record

Failure

↓

Root Cause

↓

Successful Fix

↓

Future Recommendation

Past corrections improve future execution.

---

# Pattern References

## Reflexion

Reflect

↓

Improve

↓

Retry

See

patterns/reflexion.md

---

## ReAct

Observe

↓

Reason

↓

Act

↓

Repeat

See

patterns/react.md

---

## Planner Executor

Planner adjusts future execution based on corrected outcomes.

See

patterns/planner_executor.md

---

# Engineering Decisions

## Automatic Correction

Use when

- Low-risk changes
- Deterministic validation
- Strong confidence

Recommended default.

---

## Human-Assisted Correction

Use when

- Production deployments
- Financial operations
- Legal decisions
- Sensitive infrastructure

---

## Progressive Correction

Apply the smallest safe correction first.

Avoid large rewrites.

---

## Rollback

Support rollback when corrections introduce regressions.

Required for production systems.

---

# Runtime Architecture

```
Execution

↓

Validator

↓

Failure Detector

↓

Correction Engine

↓

Verification

↓

Continue

or

Escalate
```

---

# Performance Considerations

Optimize

Detection latency

↓

Correction quality

↓

Validation time

↓

Retry count

↓

Recovery time

↓

Execution cost

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Automatic correction | Fast | May introduce regressions |
| Human review | High confidence | Slower |
| Progressive fixes | Lower risk | More iterations |
| Large rewrites | Comprehensive | Higher regression risk |

---

# Security

Protect against

- Unsafe corrections
- Privilege escalation
- Prompt injection during correction
- Infinite retry loops
- Unauthorized modifications

Corrections should respect existing security policies.

---

# Observability

Track

Failure detection

↓

Correction attempts

↓

Validation results

↓

Retry count

↓

Rollback events

↓

Escalations

↓

Success rate

---

# Metrics

Monitor

Correction Success Rate

Retry Count

Rollback Rate

Escalation Rate

Regression Rate

Validation Success Rate

Recovery Time

Cost Per Correction

---

# Common Failures

- Infinite retries
- Repeating identical fixes
- Ignoring validation
- Overcorrecting
- Hidden regressions
- Wrong root cause analysis

---

# Best Practices

- Correct only verified failures.
- Diagnose before fixing.
- Validate every correction.
- Prefer incremental fixes.
- Limit retries.
- Record successful corrections.
- Support rollback.
- Escalate when necessary.

---

# Anti-Patterns

❌ Blind retries

❌ Infinite correction loops

❌ Ignoring validation

❌ Massive rewrites for minor bugs

❌ No rollback strategy

❌ Correcting symptoms instead of causes

❌ Hiding failed corrections

---

# Real-World Production Examples

## Claude Code

- Revises code after compiler or test failures.
- Uses validation feedback before applying further edits.
- Stops when objective success criteria are met.

---

## OpenHands

- Iteratively fixes repository issues.
- Uses execution results to guide subsequent corrections.
- Replans when simple fixes fail.

---

## SWE-Agent

- Applies code patches.
- Runs automated tests.
- Repeats only when new evidence suggests improvement.

---

## Devin

- Diagnoses failed tasks.
- Generates corrective actions.
- Continues execution without restarting the entire workflow.

---

## Cursor

- Refines generated edits based on diagnostics.
- Revalidates changes before presenting them to the developer.

---

# Testing

Verify

Failure detection

Root cause analysis

Correction generation

Validation

Retry limits

Rollback

Escalation

Regression prevention

---

# Review Checklist

□ Failure detection implemented

□ Root cause analysis supported

□ Correction strategies defined

□ Validation integrated

□ Retry limits configured

□ Rollback supported

□ Escalation implemented

□ Metrics configured

□ Observability enabled

□ Tests passing

---

# Related Skills

- orchestration.md
- reflection.md
- workflows.md
- reasoning.md
- patterns/reflexion.md
- patterns/react.md
- patterns/planner_executor.md

---

# Definition of Done

A self-correction system is production-ready only if

✓ Failures are detected through objective validation

✓ Root causes are analyzed before correction

✓ Corrections are verified before acceptance

✓ Retry loops are bounded

✓ Rollback protects against regressions

✓ Escalation handles unresolvable failures

✓ Corrections improve future execution

✓ Security policies remain enforced

✓ Metrics measure correction effectiveness

✓ Agents consistently recover from failures without unnecessary human intervention