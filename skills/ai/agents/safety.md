# Skill

Safety

Version: 1.0

---

# Goal

Design AI systems that operate safely, securely, reliably, and responsibly by preventing misuse, minimizing risk, protecting users and data, and enforcing organizational policies throughout the system lifecycle.

Safety is a cross-cutting engineering concern that applies to planning, reasoning, tool usage, communication, memory, orchestration, and deployment.

A production AI system should be secure by design, not secure by accident.

---

# When to Load

Load this skill whenever building

- AI Agents
- Multi-Agent Systems
- Enterprise AI
- Coding Agents
- RAG Systems
- Autonomous Workflows
- AI Infrastructure
- Production LLM Applications

---

# Prerequisites

- tool_calling.md
- communication_protocols.md
- orchestration.md
- human_in_the_loop.md
- evaluation.md

---

# Core Principles

Identify Risk

↓

Prevent

↓

Detect

↓

Respond

↓

Recover

↓

Learn

Safety should be built into every layer of the system.

---

# Responsibilities

Safety systems should

- Protect users
- Protect data
- Protect infrastructure
- Enforce policies
- Detect misuse
- Reduce operational risk
- Support auditing

Safety systems should not

- Depend solely on prompts
- Assume trusted inputs
- Ignore failures
- Disable observability

---

# Why Safety Matters

Without safety

- Data leaks
- Prompt injection
- Unauthorized tool execution
- Compliance violations
- Infrastructure compromise
- Loss of user trust

With structured safety

- Reliable systems
- Controlled autonomy
- Regulatory compliance
- Secure deployment
- Trustworthy AI

---

# Safety Lifecycle

```
Threat Modeling

↓

Risk Assessment

↓

Preventive Controls

↓

Runtime Monitoring

↓

Incident Response

↓

Recovery

↓

Continuous Improvement
```

---

# Threat Modeling

Identify

Assets

↓

Threats

↓

Attack Surface

↓

Likelihood

↓

Impact

↓

Mitigation

Threat modeling should occur before implementation.

---

# Common Threats

## Prompt Injection

Attempts to manipulate agent behavior through malicious instructions.

Mitigation

- Input validation
- Context isolation
- Tool permission checks
- Policy enforcement

---

## Jailbreak Attempts

Attempts to bypass system rules.

Mitigation

- Policy engine
- Runtime validation
- Human escalation
- Continuous monitoring

---

## Data Leakage

Sensitive information exposed unintentionally.

Mitigation

- Data classification
- Redaction
- Encryption
- Access control

---

## Tool Abuse

Unauthorized or dangerous tool usage.

Mitigation

- Least privilege
- Tool allowlists
- Approval gates
- Execution sandbox

---

## Credential Exposure

Secrets accidentally revealed or logged.

Mitigation

- Secret managers
- Environment variables
- Log sanitization
- Credential rotation

---

# Least Privilege

Every agent should receive only

- Required tools
- Required data
- Required permissions
- Required memory

Never grant unrestricted access.

---

# Sandboxing

Run untrusted execution inside isolated environments.

Examples

- Container
- Virtual machine
- Restricted runtime
- Browser sandbox

Sandboxing limits blast radius.

---

# Policy Enforcement

Policies should govern

- Tool execution
- File access
- Network access
- Database access
- Deployment actions
- User permissions

Policy enforcement should occur before execution.

---

# Guardrails

Guardrails include

- Input validation
- Output validation
- Tool validation
- Rate limiting
- Approval checkpoints
- Runtime policy checks

Guardrails complement, not replace, model behavior.

---

# Data Protection

Protect

- Personally identifiable information
- Credentials
- API keys
- Financial records
- Proprietary code
- Customer data

Apply encryption at rest and in transit where appropriate.

---

# Logging and Auditing

Record

- Requests
- Decisions
- Tool calls
- Approvals
- Policy violations
- Security events
- Configuration changes

Logs should support incident investigation without exposing sensitive data.

---

# Incident Response

When a safety event occurs

Detect

↓

Contain

↓

Investigate

↓

Recover

↓

Review

↓

Improve

---

# Compliance

Consider requirements such as

- GDPR
- SOC 2
- ISO 27001
- HIPAA (where applicable)
- Internal organizational policies

Compliance requirements should influence system design.

---

# Pattern References

## Supervisor Worker

Supervisor enforces permissions and reviews worker actions.

See

patterns/supervisor_worker.md

---

## Planner Executor

Planner validates execution plans against safety policies.

See

patterns/planner_executor.md

---

## Reflexion

Reflection identifies unsafe outcomes before completion.

See

patterns/reflexion.md

---

# Engineering Decisions

## Fail Closed

Reject execution when safety cannot be verified.

Recommended default.

---

## Defense in Depth

Use multiple independent controls.

Recommended for production.

---

## Zero Trust

Assume every input, user, and component requires verification.

Recommended for enterprise systems.

---

## Human Approval

Require explicit approval for high-impact operations.

Use for

- Production deployments
- Financial actions
- Destructive commands

---

# Runtime Architecture

```
User

↓

Input Validation

↓

Policy Engine

↓

Planner

↓

Orchestrator

↓

Tool Runtime

↓

Output Validation

↓

Audit Log

↓

Response
```

---

# Performance Considerations

Optimize

Policy evaluation

↓

Validation latency

↓

Audit overhead

↓

Encryption cost

↓

Sandbox startup

↓

Monitoring efficiency

Safety controls should minimize unnecessary performance impact while preserving security.

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Strict policies | Higher security | Lower flexibility |
| Human approval | Reduced risk | Slower workflows |
| Sandboxing | Strong isolation | Additional overhead |
| Least privilege | Smaller attack surface | More configuration |

---

# Security

Protect against

- Prompt injection
- Jailbreak attempts
- Tool misuse
- Unauthorized access
- Data leakage
- Credential exposure
- Denial-of-service
- Supply chain attacks

Security should be continuously monitored and updated.

---

# Observability

Track

Policy evaluations

↓

Denied actions

↓

Tool executions

↓

Approval requests

↓

Security alerts

↓

Audit events

↓

Incident resolution

---

# Metrics

Monitor

Policy Violation Rate

Blocked Requests

Prompt Injection Detection Rate

Unauthorized Access Attempts

Approval Rate

Incident Response Time

Mean Time to Recovery

False Positive Rate

False Negative Rate

---

# Common Failures

- Overly permissive tools
- Missing audit logs
- Exposed secrets
- Weak access controls
- Unvalidated inputs
- Incomplete threat modeling
- Ignored policy violations

---

# Best Practices

- Apply least privilege.
- Separate duties.
- Encrypt sensitive data.
- Validate every input and output.
- Maintain comprehensive audit logs.
- Perform regular threat modeling.
- Review permissions periodically.
- Test safety controls continuously.

---

# Anti-Patterns

❌ Trusting all prompts

❌ Hardcoding credentials

❌ Running tools without validation

❌ Unlimited permissions

❌ Ignoring audit logs

❌ No incident response plan

❌ Assuming one guardrail is sufficient

---

# Real-World Production Examples

## Anthropic

- Uses layered safety techniques including constitutional principles, evaluation, and policy enforcement to reduce harmful outputs.

---

## OpenAI

- Combines system-level safeguards, policy enforcement, tool restrictions, and continuous monitoring for production deployments.

---

## GitHub Copilot

- Limits execution authority, keeps developers responsible for applying changes, and integrates with secure development workflows.

---

## Enterprise AI Platforms

- Combine identity management, approval workflows, audit logging, and least-privilege access to satisfy organizational security requirements.

---

## Cloud Infrastructure

- Uses IAM, encryption, network isolation, logging, monitoring, and secret management to secure AI services.

---

# Testing

Verify

Threat modeling

Policy enforcement

Prompt injection resistance

Tool permissions

Secret handling

Audit logging

Incident response

Recovery

Compliance checks

---

# Review Checklist

□ Threat model completed

□ Policy engine implemented

□ Least privilege enforced

□ Guardrails configured

□ Secrets managed securely

□ Audit logging enabled

□ Incident response documented

□ Metrics configured

□ Compliance requirements reviewed

□ Tests passing

---

# Related Skills

- evaluation.md
- human_in_the_loop.md
- orchestration.md
- communication_protocols.md
- tool_calling.md
- patterns/planner_executor.md
- patterns/supervisor_worker.md
- patterns/reflexion.md

---

# Definition of Done

A production AI system is safety-ready only if

✓ Threats have been identified and mitigated

✓ Policies govern tool access and execution

✓ Inputs and outputs are validated

✓ Agents operate with least privilege

✓ Sensitive data is protected throughout its lifecycle

✓ Audit logs provide complete accountability

✓ Human approval is required for high-risk actions

✓ Security incidents can be detected, investigated, and recovered from

✓ Compliance requirements are addressed where applicable

✓ Safety is continuously monitored, tested, and improved throughout the system lifecycle