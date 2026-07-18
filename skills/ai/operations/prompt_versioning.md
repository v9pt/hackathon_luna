# Prompt Versioning

Version: 1.0

---

# Goal

Manage prompts as version-controlled production assets throughout their lifecycle, enabling safe development, testing, deployment, rollback, auditing, and continuous improvement.

Prompt versioning ensures reproducibility, governance, collaboration, and operational stability while preventing uncontrolled prompt changes from degrading production AI systems.

A production AI platform should treat prompts with the same engineering discipline applied to application code.

---

# When to Use

Prompt versioning applies whenever

- prompts exist
- prompt templates evolve
- multiple environments exist
- teams collaborate
- production deployments occur
- audits are required
- evaluations run continuously
- rollbacks must be possible

---

# Problem

Prompts directly influence

- reasoning
- output quality
- safety
- latency
- token usage
- tool selection
- structured outputs

Without versioning

- changes become untraceable
- regressions are difficult to identify
- rollback becomes unreliable
- experimentation becomes impossible
- audits cannot determine which prompt generated a response

---

# Solution

Version

↓

Evaluate

↓

Approve

↓

Deploy

↓

Monitor

↓

Rollback

Every production prompt should have a unique identity and lifecycle.

---

# Core Principles

Version

↓

Review

↓

Evaluate

↓

Deploy

↓

Observe

↓

Improve

Every prompt change should be intentional and reproducible.

---

# Prompt Lifecycle

```
Draft

↓

Review

↓

Evaluation

↓

Approval

↓

Deployment

↓

Monitoring

↓

Iteration

↓

Archive
```

---

# Architecture

```
Developer

↓

Prompt Repository

↓

Version Control

↓

Evaluation

↓

CI/CD

↓

Production

↓

Monitoring
```

---

# Prompt Components

Every prompt should include

- identifier
- semantic version
- author
- creation date
- purpose
- model compatibility
- evaluation history
- deployment history
- rollback history

---

# Version Numbers

Recommended

Major.Minor.Patch

Example

```
2.4.1
```

Major

Breaking behavioral changes

Minor

Improved instructions

Patch

Formatting or typo fixes

---

# Prompt Repository

Maintain prompts in

- Git
- dedicated prompt registry
- prompt management platform

Never edit production prompts directly.

---

# Prompt Metadata

Store

- owner
- team
- task
- supported models
- expected output format
- evaluation scores
- deployment status
- dependencies

Metadata improves governance.

---

# Prompt Templates

Separate

Static Instructions

+

Variables

↓

Rendered Prompt

Template versioning is preferable to storing rendered prompts.

---

# Environment Promotion

Prompts move through

Development

↓

Testing

↓

Staging

↓

Production

Avoid direct production editing.

---

# Prompt Reviews

Require review before deployment.

Review

- correctness
- clarity
- safety
- token efficiency
- maintainability

Treat prompts like pull requests.

---

# Evaluation Integration

Every version should be evaluated using

- benchmark datasets
- regression suites
- safety tests
- structured output validation
- latency measurements

Deployment should require passing evaluations.

---

# Deployment Strategies

Supported strategies

- blue-green
- canary
- shadow
- feature flags

Prompt deployment should be independent of application deployment.

---

# Rollback

Restore

Previous Prompt Version

↓

Re-evaluate

↓

Resume Production

Rollback should take minutes.

---

# Compatibility

Track compatibility with

- model versions
- tool definitions
- output schemas
- APIs

Prompt upgrades may require coordinated deployments.

---

# Experiment Tracking

Record

- hypothesis
- candidate prompt
- evaluation metrics
- experiment duration
- winner

Prompt improvements should be evidence-based.

---

# Audit Trail

Maintain

- deployment history
- reviewers
- approvals
- evaluation reports
- rollback history

Every production prompt should be fully traceable.

---

# Security

Protect against

- prompt injection
- unauthorized edits
- secret exposure
- unsafe instructions

Production prompts should follow access controls.

---

# Monitoring

Track

- latency
- token usage
- evaluation score
- error rate
- hallucination rate
- cost
- user satisfaction

Performance should be monitored after deployment.

---

# Engineering Decisions

## Git-Based Versioning

Recommended default.

Simple.

Widely adopted.

---

## Prompt Registry

Recommended for enterprise platforms.

Supports metadata and governance.

---

## Manual Reviews

Required for production prompts.

---

## Automated Evaluation Gates

Recommended.

Prevent regressions before deployment.

---

# Runtime Architecture

```
Developer

↓

Git Repository

↓

Evaluation Pipeline

↓

Approval

↓

Prompt Registry

↓

Production

↓

Monitoring
```

---

# Performance

Optimize

prompt clarity

↓

token efficiency

↓

evaluation coverage

↓

deployment speed

↓

rollback time

↓

maintainability

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Git only | Simple | Limited metadata |
| Prompt Registry | Better governance | Additional infrastructure |
| Manual approval | Higher quality | Slower deployments |
| Automated deployment | Faster | Requires mature testing |

---

# Common Failures

- editing prompts directly in production
- missing version numbers
- no rollback history
- poor metadata
- skipped evaluations
- unreviewed prompt changes
- incompatible model updates

---

# Best Practices

- Version every prompt.
- Separate templates from variables.
- Require reviews.
- Evaluate every version.
- Store metadata.
- Deploy progressively.
- Monitor production performance.
- Archive deprecated prompts.

---

# Anti-Patterns

❌ Editing prompts directly in production

❌ No semantic versioning

❌ Copy-pasted prompts across projects

❌ Skipping evaluations

❌ Missing deployment history

❌ No rollback mechanism

❌ Embedding secrets inside prompts

---

# Real-World Examples

## OpenAI

Treats system prompts and production configurations as managed deployment artifacts, validating changes through evaluation before rollout.

---

## Anthropic

Evaluates prompt and behavior changes alongside safety testing before production deployments.

---

## LangSmith

Supports prompt management, version comparison, experiment tracking, evaluations, and deployment history.

---

## GitHub Copilot

Continuously iterates on prompt templates while validating changes through internal evaluations before release.

---

## Enterprise AI Platforms

Store prompts in version-controlled repositories with automated testing, approval workflows, deployment pipelines, rollback support, and audit logging.

---

# Related Skills

- evaluation_pipelines.md
- testing_ai_systems.md
- experimentation.md
- rollbacks.md
- model_versioning.md
- governance.md

---

# Definition of Done

A production prompt versioning system is complete only if

✓ Every prompt has a unique version and immutable deployment history

✓ Prompt changes undergo peer review and automated evaluation

✓ Templates and runtime variables are managed independently

✓ Deployment supports staged rollouts and rapid rollback

✓ Prompt metadata captures ownership, compatibility, and evaluation results

✓ Audit logs record approvals, deployments, and rollbacks

✓ Production monitoring detects prompt regressions after deployment

✓ Prompt compatibility with models, tools, and schemas is validated

✓ Deprecated prompts remain archived for reproducibility

✓ Prompt engineering follows the same lifecycle discipline as production software engineering