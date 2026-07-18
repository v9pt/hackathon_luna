# Evaluation Pipelines

Version: 1.0

---

# Goal

Continuously measure, validate, and improve AI system quality before and after deployment using automated and human evaluation workflows.

Evaluation pipelines provide repeatable, objective measurements that prevent quality regressions, validate new models, prompts, workflows, and retrieval systems, and ensure production AI systems meet defined performance standards.

A production evaluation pipeline should detect regressions before users experience them.

---

# When to Use

Evaluation pipelines apply whenever

- prompts change
- models change
- agent workflows change
- retrieval logic changes
- tools change
- datasets evolve
- deployments occur
- quality must be measured

---

# Problem

Traditional software answers

"Did the code pass the tests?"

AI systems require additional questions

- Is the answer correct?
- Is retrieval improving?
- Did hallucinations increase?
- Did latency increase?
- Did cost increase?
- Are users happier?

Without evaluation

quality slowly degrades.

---

# Solution

Evaluate continuously.

```
Code

↓

Build

↓

Deploy Candidate

↓

Evaluation Pipeline

↓

Quality Report

↓

Approve

↓

Production
```

Evaluation becomes a mandatory deployment gate.

---

# Core Principles

Collect

↓

Evaluate

↓

Analyze

↓

Compare

↓

Approve

↓

Deploy

Quality should always be measurable.

---

# Evaluation Architecture

```
Model

↓

Evaluation Runner

↓

Benchmark Dataset

↓

Metrics

↓

Reports

↓

Quality Gate

↓

Deployment
```

---

# Components

## Benchmark Dataset

Contains

- representative prompts
- expected outputs
- edge cases
- adversarial cases
- production scenarios

Datasets should evolve continuously.

---

## Evaluation Runner

Responsible for

- executing prompts
- running workflows
- collecting outputs
- calculating metrics

---

## Judge

Evaluates responses.

Can be

- rule based
- human
- LLM-as-a-Judge
- hybrid

---

## Metrics Engine

Computes

- accuracy
- latency
- cost
- safety
- retrieval quality
- hallucination rate

---

## Quality Gate

Determines

Pass

or

Fail

before deployment.

---

# Evaluation Lifecycle

Dataset

↓

Execution

↓

Judging

↓

Metrics

↓

Comparison

↓

Approval

↓

Deployment

---

# Offline Evaluation

Run before deployment.

Advantages

- reproducible
- inexpensive
- deterministic

Recommended for CI/CD.

---

# Online Evaluation

Run in production.

Examples

- A/B tests
- shadow deployments
- user feedback

Useful for validating real-world behavior.

---

# Human Evaluation

Experts evaluate

- correctness
- helpfulness
- completeness
- tone
- safety

Most accurate.

Most expensive.

---

# Automated Evaluation

Evaluate

- exact match
- semantic similarity
- execution success
- structured outputs
- retrieval correctness

Fast.

Scalable.

---

# LLM-as-a-Judge

A second model evaluates responses.

Useful for

- reasoning
- writing quality
- summarization
- conversational AI

Human calibration remains important.

---

# Golden Datasets

Curated benchmark examples.

Should include

- common cases
- difficult cases
- failures
- edge cases
- adversarial prompts

Never evaluate using only easy examples.

---

# Regression Testing

Compare

Old Version

↓

New Version

↓

Metric Difference

↓

Pass/Fail

Every deployment should run regression evaluations.

---

# Prompt Evaluation

Measure

- correctness
- consistency
- token usage
- latency
- safety

Treat prompts like production code.

---

# RAG Evaluation

Evaluate

- retrieval precision
- retrieval recall
- context relevance
- citation accuracy
- answer correctness

Separate retrieval quality from generation quality.

---

# Agent Evaluation

Measure

- task completion
- planning quality
- tool selection
- retries
- reflection effectiveness
- execution efficiency

Entire workflows should be evaluated.

---

# Safety Evaluation

Test

- prompt injection
- jailbreaks
- toxic outputs
- PII leakage
- policy violations

Run continuously.

---

# Cost Evaluation

Track

- tokens
- API cost
- GPU hours
- retrieval cost
- execution cost

Quality improvements should justify increased cost.

---

# Latency Evaluation

Measure

- p50
- p95
- p99

for

- retrieval
- model
- workflow
- tools

---

# Continuous Evaluation

Every deployment triggers

Benchmark

↓

Evaluation

↓

Comparison

↓

Approval

↓

Production

Evaluation should be automatic.

---

# CI/CD Integration

Example

Commit

↓

Tests

↓

Evaluation Suite

↓

Regression Report

↓

Deployment Approval

Quality gates should block regressions.

---

# A/B Testing

Deploy

Version A

Version B

↓

Collect Metrics

↓

Compare

↓

Winner

Useful for prompt and model selection.

---

# Shadow Evaluation

Run new system

without serving users.

Compare outputs against production.

Ideal before major model upgrades.

---

# Engineering Decisions

## Human Evaluation

Highest quality.

Low scalability.

---

## Automated Evaluation

Highly scalable.

Recommended default.

---

## Hybrid Evaluation

Automation

+

Human Review

Recommended for production.

---

# Runtime Architecture

```
Dataset

↓

Evaluation Runner

↓

LLM

↓

Judge

↓

Metrics

↓

Dashboard

↓

Deployment Gate
```

---

# Performance

Optimize

evaluation runtime

↓

dataset coverage

↓

judge consistency

↓

cost

↓

parallel execution

↓

report generation

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Human evaluation | Highest quality | Slow |
| Automated evaluation | Fast | Limited nuance |
| LLM Judge | Scalable | Possible bias |
| Hybrid | Balanced | Operational complexity |

---

# Common Failures

- outdated benchmark datasets
- evaluation leakage
- inconsistent judging
- small sample sizes
- ignoring production feedback
- evaluating only accuracy
- missing regression tests

---

# Best Practices

- Maintain versioned benchmark datasets.
- Evaluate before every deployment.
- Separate offline and online evaluations.
- Combine automated and human judging.
- Track historical trends.
- Include adversarial cases.
- Automate regression testing.
- Use evaluation gates in CI/CD.

---

# Anti-Patterns

❌ Deploying without evaluation

❌ Measuring only accuracy

❌ Static benchmark datasets

❌ Ignoring user feedback

❌ Comparing models without identical datasets

❌ Manual evaluation for every release

❌ No regression tracking

---

# Real-World Examples

## OpenAI

Evaluates model candidates against internal benchmark suites covering capability, safety, reliability, and regression detection before broader deployment.

---

## Anthropic

Runs extensive automated and human evaluations across helpfulness, harmlessness, honesty, and safety before releasing new Claude models.

---

## LangSmith

Provides evaluation datasets, experiment tracking, LLM-as-a-Judge workflows, regression comparisons, and quality dashboards for LLM applications.

---

## GitHub Copilot

Measures code completion acceptance, correctness, latency, and developer productivity before and after model updates.

---

## Enterprise AI Platforms

Continuously evaluate prompts, models, retrieval pipelines, and agent workflows using automated benchmarks integrated into CI/CD.

---

# Related Skills

- monitoring.md
- observability.md
- testing_ai_systems.md
- experimentation.md
- deployment.md
- prompt_versioning.md

---

# Definition of Done

An AI evaluation pipeline is production-ready only if

✓ Benchmark datasets are representative and versioned

✓ Offline evaluations run automatically before deployment

✓ Online evaluations measure real-world performance

✓ Regression testing prevents quality degradation

✓ Prompt, model, RAG, and agent workflows are evaluated independently

✓ Quality gates block deployments that fail defined thresholds

✓ Human and automated evaluations complement each other

✓ Historical evaluation results support trend analysis

✓ Cost, latency, safety, and correctness are measured together

✓ Every production release is backed by objective evidence that quality has been maintained or improved