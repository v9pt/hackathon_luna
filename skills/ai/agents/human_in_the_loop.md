# Skill

Human in the Loop

Version: 1.0

---

# Goal

Design AI systems that collaborate effectively with humans by introducing structured approval, review, intervention, and feedback mechanisms at appropriate stages of execution.

Human-in-the-Loop (HITL) enables autonomous systems to remain accountable, transparent, and safe while allowing humans to guide high-impact decisions.

A production AI system should know when to continue autonomously and when to request human input.

---

# When to Load

Load this skill whenever building

- Enterprise AI
- Coding Agents
- Autonomous Workflows
- Financial Systems
- Healthcare AI
- Legal AI
- Multi-Agent Systems
- High-Risk Automation

---

# Prerequisites

- workflows.md
- orchestration.md
- reflection.md
- self_correction.md

---

# Core Principles

Goal

↓

Autonomous Execution

↓

Risk Evaluation

↓

Human Review?

↓

Approve

↓

Continue

↓

Complete

Humans should supervise decisions, not every action.

---

# Responsibilities

Human-in-the-Loop systems should

- Request approvals
- Explain decisions
- Accept feedback
- Pause workflows
- Resume execution
- Escalate uncertainty
- Maintain audit trails

Human-in-the-Loop systems should not

- Replace autonomous execution
- Block low-risk work
- Ignore expert feedback

---

# Why Human Oversight Matters

Without human oversight

- Incorrect assumptions propagate
- Sensitive actions execute automatically
- Accountability is reduced
- Trust decreases

With structured oversight

- Higher confidence
- Better safety
- Regulatory compliance
- Improved user trust

---

# Human Interaction Lifecycle

```
Goal

↓

Execute

↓

Evaluate Risk

↓

Request Approval

↓

Human Decision

↓

Resume Workflow

↓

Complete
```

---

# Approval Gates

Require approval before

- Production deployments
- Database migrations
- Financial transactions
- User deletion
- Infrastructure changes
- Legal actions
- Security configuration

Routine operations should remain autonomous.

---

# Types of Human Interaction

## Approval

Human explicitly approves or rejects an action.

---

## Review

Human evaluates generated output.

Examples

- Code review
- Documentation review
- Research validation

---

## Clarification

Agent requests additional information before proceeding.

Useful when requirements are ambiguous.

---

## Override

Human replaces the agent's decision.

Override decisions should be recorded.

---

## Feedback

Human improves future execution by providing corrections.

Feedback should be reusable where appropriate.

---

# Escalation Criteria

Escalate when

- Confidence is low
- Validation fails repeatedly
- Sensitive resources are affected
- Policy conflicts exist
- Multiple correction attempts fail
- Required information is missing

---

# Confidence Thresholds

Example

High confidence

↓

Autonomous execution

Medium confidence

↓

Optional review

Low confidence

↓

Mandatory approval

Confidence thresholds should be configurable.

---

# Approval Workflow

```
Action

↓

Risk Assessment

↓

Approval Request

↓

Decision

↓

Execute

↓

Audit Log
```

---

# Explainability

Every approval request should include

- Goal
- Proposed action
- Reasoning summary
- Expected impact
- Risks
- Rollback plan

Humans should understand what they are approving.

---

# Feedback Loop

```
Execution

↓

Human Feedback

↓

Validation

↓

Memory Update

↓

Future Improvement
```

Feedback should improve future decisions without bypassing validation.

---

# Audit Logging

Record

- Who approved
- Timestamp
- Action
- Decision
- Reason
- Workflow ID
- Outcome

Audit trails support accountability and compliance.

---

# Pattern References

## Supervisor Worker

Supervisor pauses execution until approval is received.

See

patterns/supervisor_worker.md

---

## Planner Executor

Planner inserts approval checkpoints into the workflow.

See

patterns/planner_executor.md

---

## Reflexion

Reflection determines whether escalation is necessary.

See

patterns/reflexion.md

---

# Engineering Decisions

## Fully Autonomous

Use when

- Low-risk tasks
- Deterministic validation
- Internal automation

---

## Approval-Based

Use when

High-impact decisions require explicit authorization.

Recommended default.

---

## Advisory Mode

Agent recommends actions.

Human executes them.

Useful for regulated industries.

---

## Collaborative Mode

Human and AI iterate together.

Recommended for software engineering and research.

---

# Runtime Architecture

```
Planner

↓

Risk Engine

↓

Approval Gateway

↓

Human Reviewer

↓

Workflow Resume

↓

Completion
```

---

# Performance Considerations

Optimize

Approval latency

↓

Workflow pause duration

↓

Feedback quality

↓

Review efficiency

↓

Escalation accuracy

Avoid unnecessary interruptions.

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Full autonomy | Fast | Higher risk |
| Mandatory approval | Safe | Slower |
| Advisory mode | High trust | Less automation |
| Collaborative mode | Flexible | More coordination |

---

# Security

Protect against

- Unauthorized approvals
- Approval spoofing
- Missing audit trails
- Privilege escalation
- Social engineering
- Replay attacks

Require strong authentication for approvers.

---

# Observability

Track

Approval requests

↓

Approval latency

↓

Approval outcomes

↓

Escalations

↓

Rejected actions

↓

Workflow pauses

↓

Feedback quality

---

# Metrics

Monitor

Approval Rate

Average Approval Time

Escalation Rate

Override Rate

Feedback Acceptance Rate

Workflow Pause Time

False Escalation Rate

Task Completion Rate

---

# Common Failures

- Too many approval requests
- Missing approval gates
- Poor explanations
- Ignoring expert feedback
- No audit logs
- Approval bottlenecks

---

# Best Practices

- Automate low-risk work.
- Escalate only when necessary.
- Explain every approval request.
- Keep audit logs complete.
- Allow overrides.
- Learn from human feedback.
- Make approval policies configurable.
- Measure approval efficiency.

---

# Anti-Patterns

❌ Asking for approval on every action

❌ Autonomous execution of critical operations

❌ Missing audit trails

❌ Ignoring user feedback

❌ Hidden decision making

❌ No rollback strategy

❌ Approval without explanation

---

# Real-World Production Examples

## Claude Code

- Requests confirmation before executing potentially destructive commands.
- Encourages review before applying significant repository changes.

---

## GitHub Copilot

- Suggests code while leaving acceptance to the developer.
- Keeps the human responsible for final changes.

---

## Cursor

- Allows developers to review edits before they are applied.
- Supports iterative collaboration between AI and human.

---

## OpenAI Codex

- Integrates execution with developer review and validation.
- Uses objective feedback to guide subsequent actions.

---

## Enterprise Approval Systems

- Require managerial approval for production deployments, financial actions, and infrastructure changes.
- Maintain complete audit trails for compliance.

---

# Testing

Verify

Approval gates

Escalation logic

Feedback handling

Workflow resumption

Audit logging

Override handling

Authentication

Authorization

---

# Review Checklist

□ Approval policy defined

□ Risk thresholds configured

□ Escalation implemented

□ Explainability supported

□ Audit logging enabled

□ Feedback integrated

□ Metrics configured

□ Observability enabled

□ Security reviewed

□ Tests passing

---

# Related Skills

- evaluation.md
- safety.md
- orchestration.md
- reflection.md
- self_correction.md
- patterns/planner_executor.md
- patterns/supervisor_worker.md
- patterns/reflexion.md

---

# Definition of Done

A Human-in-the-Loop system is production-ready only if

✓ High-risk actions require appropriate human approval

✓ Approval requests clearly explain intent, risks, and expected outcomes

✓ Workflow execution pauses and resumes safely

✓ Feedback improves future execution without bypassing validation

✓ Audit logs provide complete accountability

✓ Escalation thresholds are configurable

✓ Low-risk work remains autonomous

✓ Security protects the approval process

✓ Human collaboration improves overall system quality

✓ AI and humans work together efficiently while maintaining safety and trust