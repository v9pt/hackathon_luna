# Skill

Evaluation

Version: 1.0

---

# Goal

Design comprehensive evaluation systems that measure the quality, reliability, efficiency, robustness, and business impact of AI agents throughout development and production.

Evaluation provides objective evidence that an AI system meets its intended requirements and continues to perform reliably over time.

A production evaluation framework should detect regressions, quantify improvements, and guide continuous optimization.

---

# When to Load

Load this skill whenever building

- AI Agents
- Multi-Agent Systems
- RAG Applications
- Coding Agents
- Enterprise AI
- Autonomous Workflows
- Production LLM Systems

---

# Prerequisites

- reflection.md
- self_correction.md
- human_in_the_loop.md
- orchestration.md

---

# Core Principles

Design

↓

Measure

↓

Analyze

↓

Improve

↓

Validate

↓

Deploy

↓

Monitor

↓

Repeat

Evaluation is a continuous process, not a one-time event.

---

# Responsibilities

Evaluation systems should

- Measure quality
- Detect regressions
- Benchmark performance
- Compare versions
- Monitor production
- Guide improvements

Evaluation systems should not

- Depend solely on manual review
- Ignore production metrics
- Optimize only one metric

---

# Why Evaluation Matters

Without evaluation

- Improvements are subjective
- Regressions go unnoticed
- Models drift over time
- Performance claims cannot be verified

With structured evaluation

- Reliable releases
- Objective decision making
- Continuous improvement
- Higher user trust

---

# Evaluation Lifecycle

```
Define Objectives

↓

Build Dataset

↓

Execute Evaluation

↓

Analyze Results

↓

Identify Improvements

↓

Implement Changes

↓

Re-evaluate

↓

Deploy
```

---

# Types of Evaluation

## Offline Evaluation

Uses predefined datasets.

Examples

- Benchmark suites
- Test repositories
- Golden datasets

Best for

Development and regression testing.

---

## Online Evaluation

Measures real production usage.

Examples

- User feedback
- Success rates
- Latency
- Cost

Best for

Monitoring deployed systems.

---

## Human Evaluation

Experts assess

- Correctness
- Helpfulness
- Clarity
- Safety

Required for subjective tasks.

---

## Automated Evaluation

Uses objective metrics

Examples

- Unit tests
- Exact match
- BLEU
- ROUGE
- Pass@k
- Precision
- Recall

Recommended whenever possible.

---

# Evaluation Dimensions

Measure

Correctness

↓

Reliability

↓

Latency

↓

Cost

↓

Robustness

↓

Safety

↓

User Satisfaction

↓

Business Impact

---

# Benchmark Datasets

Evaluation datasets should be

- Representative
- Versioned
- Diverse
- Reproducible
- Continuously updated

Avoid evaluating only on training examples.

---

# Regression Testing

Every release should verify

- Existing functionality
- Previous bug fixes
- Performance baselines
- Safety requirements

Never deploy without regression testing.

---

# A/B Testing

Compare

System A

↓

System B

↓

Metrics

↓

Decision

Useful for incremental improvements.

---

# Production Monitoring

Track

Success Rate

↓

Latency

↓

Token Usage

↓

Failures

↓

Retries

↓

Escalations

↓

User Feedback

↓

Business KPIs

Evaluation continues after deployment.

---

# Error Analysis

For every failure determine

What failed?

↓

Why?

↓

How often?

↓

Can it be fixed?

↓

How will improvement be verified?

---

# Pattern References

## Reflexion

Evaluate generated output before improvement.

See

patterns/reflexion.md

---

## Planner Executor

Measure planning quality and execution success.

See

patterns/planner_executor.md

---

## Supervisor Worker

Evaluate worker performance individually and collectively.

See

patterns/supervisor_worker.md

---

# Engineering Decisions

## Manual Evaluation

Use when

- Subjective quality
- Small datasets
- UX assessment

---

## Automated Evaluation

Use when

- Deterministic outputs
- Regression testing
- Continuous Integration

Recommended default.

---

## Hybrid Evaluation

Combine automated metrics with expert review.

Recommended for production AI.

---

# Runtime Architecture

```
System

↓

Evaluation Pipeline

↓

Metrics Engine

↓

Analysis

↓

Reporting

↓

Improvement
```

---

# Performance Considerations

Optimize

Evaluation speed

↓

Dataset coverage

↓

Metric accuracy

↓

Evaluation cost

↓

Reporting latency

↓

Reproducibility

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Human review | High quality | Expensive |
| Automated evaluation | Fast | Limited for subjective tasks |
| Offline benchmarks | Repeatable | May not reflect production |
| Online evaluation | Real-world | More difficult to control |

---

# Security

Protect against

- Benchmark leakage
- Data poisoning
- Metric manipulation
- Evaluation bias
- Unauthorized dataset access

Evaluation data should follow the same security policies as production data.

---

# Observability

Track

Evaluation runs

↓

Metric trends

↓

Regression failures

↓

Dataset versions

↓

Latency

↓

Costs

↓

User feedback

↓

Release quality

---

# Metrics

Monitor

Task Success Rate

Accuracy

Precision

Recall

F1 Score

Pass@k

Latency

Token Usage

Cost Per Task

Failure Rate

Retry Rate

Escalation Rate

User Satisfaction

Business Success Rate

---

# Common Failures

- Small evaluation datasets
- Optimizing one metric only
- Ignoring production behavior
- Benchmark overfitting
- Missing regression tests
- Poor dataset diversity

---

# Best Practices

- Define measurable objectives.
- Version evaluation datasets.
- Combine offline and online evaluation.
- Measure latency and cost.
- Analyze failures systematically.
- Track regressions continuously.
- Include human evaluation where needed.
- Monitor production metrics after deployment.

---

# Anti-Patterns

❌ Evaluating only once

❌ Using only synthetic datasets

❌ Ignoring user feedback

❌ Optimizing only accuracy

❌ No regression testing

❌ Unversioned benchmarks

❌ Deploying without validation

---

# Real-World Production Examples

## OpenAI

- Evaluates models using automated benchmarks, human preference testing, and production monitoring before deployment.

---

## Anthropic

- Combines constitutional evaluations, safety testing, benchmark suites, and human review to assess model quality.

---

## GitHub Copilot

- Measures code acceptance rates, developer productivity, latency, and suggestion quality using offline benchmarks and production telemetry.

---

## Cursor

- Continuously evaluates edit quality, execution success, latency, and developer feedback to improve coding workflows.

---

## LangSmith

- Provides experiment tracking, dataset management, regression testing, and production evaluation for LLM applications.

---

# Testing

Verify

Offline benchmarks

Regression tests

Human review

Latency measurements

Cost tracking

Production monitoring

A/B testing

Metric reporting

---

# Review Checklist

□ Evaluation objectives defined

□ Benchmark datasets versioned

□ Offline evaluation implemented

□ Online monitoring enabled

□ Human review process documented

□ Regression testing configured

□ Metrics dashboard available

□ Failure analysis process established

□ Security reviewed

□ Tests passing

---

# Related Skills

- safety.md
- human_in_the_loop.md
- reflection.md
- self_correction.md
- orchestration.md
- patterns/reflexion.md
- patterns/planner_executor.md
- patterns/supervisor_worker.md

---

# Definition of Done

A production evaluation framework is complete only if

✓ Objectives are measurable and documented

✓ Representative benchmark datasets are versioned

✓ Offline and online evaluations complement each other

✓ Human evaluation is included where automation is insufficient

✓ Regression testing prevents quality degradation

✓ Latency, cost, and reliability are measured alongside correctness

✓ Production monitoring continuously tracks real-world performance

✓ Failures are analyzed and converted into improvements

✓ Evaluation results guide deployment decisions

✓ The AI system demonstrates consistent, measurable quality over time