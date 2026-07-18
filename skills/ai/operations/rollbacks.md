# Rollbacks

Version: 1.0

---

# Goal

Safely restore a previously verified production state after an unsuccessful deployment while minimizing downtime, customer impact, data inconsistency, and operational risk.

Rollback engineering ensures every production change—including models, prompts, workflows, infrastructure, and databases—can be reversed quickly, predictably, and safely.

A production AI platform should make rollbacks routine, automated, and low risk.

---

# When to Use

Rollback strategies apply whenever

- deployments fail
- latency increases
- quality regresses
- costs spike
- hallucinations increase
- safety issues appear
- infrastructure becomes unstable
- customer impact is detected

---

# Problem

Deployments can introduce

- software bugs
- prompt regressions
- model failures
- retrieval degradation
- routing mistakes
- infrastructure issues
- database inconsistencies

Without rollback

small mistakes become prolonged outages.

---

# Solution

Detect

↓

Validate

↓

Rollback

↓

Verify

↓

Recover

Recovery should be measured in minutes, not hours.

---

# Core Principles

Version Everything

↓

Deploy Safely

↓

Monitor

↓

Rollback Quickly

↓

Learn

Every production artifact should be reversible.

---

# Rollback Architecture

```
Deployment

↓

Verification

↓

Health Checks

↓

Rollback Decision

↓

Previous Stable Version

↓

Validation

↓

Production
```

---

# Components

## Version Registry

Maintain immutable versions of

- application code
- prompts
- models
- embeddings
- workflows
- configurations
- infrastructure

Every deployed artifact must be versioned.

---

## Deployment Validator

Continuously checks

- latency
- error rate
- quality
- safety
- infrastructure health

Validation determines whether rollback is necessary.

---

## Rollback Controller

Responsible for

- selecting target version
- orchestrating rollback
- validating recovery
- notifying operators

---

## Audit Log

Record

- deployment time
- rollback reason
- affected services
- operator actions
- validation results

Every rollback should be traceable.

---

# Rollback Lifecycle

Deploy

↓

Observe

↓

Validate

↓

Rollback Decision

↓

Restore

↓

Verify

↓

Close Incident

---

# Types of Rollbacks

## Code Rollback

Restore previous application release.

Commonly performed through

- Git tags
- container images
- deployment revisions

---

## Prompt Rollback

Restore previous prompt versions.

Useful when

- hallucinations increase
- formatting breaks
- safety regresses

Prompt rollbacks should be independent of application deployments.

---

## Model Rollback

Switch

New Model

↓

Previous Model

Useful when

- latency increases
- quality decreases
- provider incidents occur

---

## Workflow Rollback

Restore previous

- agent planner
- routing policy
- reflection strategy
- orchestration logic

Entire workflows should be versioned.

---

## Configuration Rollback

Restore

- environment variables
- feature flags
- routing policies
- thresholds

Configuration errors are common deployment failures.

---

## Infrastructure Rollback

Restore

- Kubernetes manifests
- Terraform state
- Helm releases
- networking configuration

Infrastructure should be managed as code.

---

## Database Rollback

Most difficult rollback.

Strategies include

- reverse migrations
- point-in-time recovery
- backup restoration
- forward fixes

Prefer backward-compatible migrations.

---

# Deployment Strategies

## Blue-Green

Blue

↓

Green

If validation fails

↓

Switch Back

Fastest rollback strategy.

Recommended.

---

## Canary

Deploy

1%

↓

5%

↓

25%

↓

100%

Rollback affects only exposed users.

Recommended default.

---

## Rolling Deployment

Update instances gradually.

Rollback replaces updated instances.

Lower infrastructure cost.

---

## Shadow Deployment

Run new version

without serving users.

Rollback unnecessary if validation fails.

Safest validation strategy.

---

# Feature Flags

Disable features

without redeployment.

Useful for

- prompts
- tools
- workflows
- routing
- experiments

Feature flags reduce rollback frequency.

---

# Automated Rollbacks

Trigger rollback when

- latency exceeds threshold
- error rate spikes
- quality drops
- safety fails
- health checks fail
- deployment validation fails

Automation minimizes recovery time.

---

# Rollback Triggers

Examples

- SLO violation
- error budget exhaustion
- evaluation regression
- failed smoke tests
- customer impact
- infrastructure instability

---

# Rollback Validation

After rollback verify

- service health
- latency
- correctness
- safety
- traffic recovery
- business metrics

Never assume rollback succeeded.

---

# State Reconciliation

Some deployments modify

- databases
- caches
- queues
- object storage

Rollback should restore system consistency.

---

# Prompt Versioning

Every prompt should include

- version
- author
- deployment date
- evaluation results

Rollback becomes trivial.

---

# Model Versioning

Track

- provider
- model
- configuration
- hyperparameters
- deployment history

Support rapid provider switching.

---

# Deployment Verification

Verify

- APIs
- agent execution
- retrieval
- tool integrations
- inference
- authentication

Verification should occur automatically.

---

# Rollback Metrics

Measure

- rollback frequency
- rollback duration
- recovery success
- deployment success
- false rollbacks
- incident duration

---

# Engineering Decisions

## Manual Rollback

Useful for

- high-risk deployments

Slower response.

---

## Automated Rollback

Recommended default.

Fast recovery.

Requires reliable monitoring.

---

## Blue-Green

Fastest rollback.

Higher infrastructure cost.

---

## Canary

Recommended for AI deployments.

Balances safety and operational cost.

---

# Runtime Architecture

```
CI/CD

↓

Deployment

↓

Monitoring

↓

Validation

↓

Rollback Controller

↓

Stable Version

↓

Production
```

---

# Performance

Optimize

rollback duration

↓

validation speed

↓

deployment confidence

↓

recovery automation

↓

downtime

↓

customer impact

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Manual rollback | Human oversight | Slow |
| Automated rollback | Fast recovery | Possible false positives |
| Blue-Green | Instant rollback | Higher infrastructure cost |
| Canary | Lower deployment risk | Longer rollout |
| Shadow | Safest validation | Double infrastructure usage |

---

# Common Failures

- unversioned prompts
- irreversible database migrations
- manual deployment recovery
- rollback without validation
- stale feature flags
- inconsistent configurations
- missing deployment history

---

# Best Practices

- Version every deployable artifact.
- Keep database migrations backward compatible.
- Automate rollback decisions where appropriate.
- Validate after every rollback.
- Use feature flags to reduce deployments.
- Prefer canary or blue-green deployments.
- Record every rollback event.
- Practice rollback drills regularly.

---

# Anti-Patterns

❌ Deploying without rollback plans

❌ Irreversible schema migrations

❌ Manual production recovery

❌ Unversioned prompts

❌ Rollback without monitoring

❌ Long rollback procedures

❌ Treating rollback as an emergency-only process

---

# Real-World Examples

## Google

Uses progressive rollouts, automated health checks, and rapid rollback mechanisms across large-scale production services to minimize deployment risk.

---

## OpenAI

Combines staged deployments, operational monitoring, and version-controlled infrastructure to safely introduce and, when necessary, revert changes to production AI systems.

---

## Anthropic

Employs phased releases, automated validation, and deployment safeguards that allow operational teams to halt or reverse changes if quality or safety degrades.

---

## Kubernetes

Supports rolling updates, deployment revisions, and rollback commands, enabling infrastructure teams to restore previous application versions quickly.

---

## Enterprise AI Platforms

Version prompts, models, retrieval pipelines, workflows, feature flags, and infrastructure independently, allowing targeted rollbacks without reverting the entire platform.

---

# Related Skills

- deployment.md
- reliability.md
- monitoring.md
- observability.md
- prompt_versioning.md
- model_versioning.md
- incident_response.md

---

# Definition of Done

A production AI rollback strategy is complete only if

✓ Every deployable artifact is independently versioned

✓ Rollback procedures are automated where appropriate

✓ Canary, blue-green, or equivalent deployment strategies minimize rollback risk

✓ Prompts, models, workflows, infrastructure, and configurations can be restored independently

✓ Database migrations support safe recovery through backward compatibility or recovery plans

✓ Rollback triggers are based on measurable operational signals

✓ Every rollback is automatically validated before normal traffic resumes

✓ Rollback events are fully audited and documented

✓ Recovery time objectives are consistently achieved

✓ Engineers can restore a known-good production state quickly, safely, and predictably with minimal customer impact