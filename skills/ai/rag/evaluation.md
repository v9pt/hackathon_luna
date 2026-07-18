# Skill

Evaluation

Version: 1.0

---

# Goal

Continuously measure, benchmark, and improve Retrieval-Augmented Generation (RAG) systems using objective metrics, automated testing, and production monitoring.

Evaluation ensures that every architectural decision is validated with evidence rather than intuition.

A production AI system should never rely solely on manual testing.

---

# When to Load

Load this skill whenever building

- RAG Systems
- AI Agents
- Chatbots
- Enterprise Search
- Coding Assistants
- Customer Support AI
- Research Assistants

---

# Prerequisites

- retrieval.md
- reranking.md
- prompt_builder.md
- memory.md

---

# Core Principles

Every AI system should answer

Is retrieval correct?

↓

Is context sufficient?

↓

Is the answer grounded?

↓

Is latency acceptable?

↓

Is cost acceptable?

↓

Has quality improved?

Evaluation is a continuous process, not a final step.

---

# Responsibilities

An evaluation system should

- Measure retrieval quality
- Measure generation quality
- Detect hallucinations
- Benchmark changes
- Monitor production
- Compare models
- Compare prompts
- Compare retrieval strategies

It should not

- Generate answers
- Replace human review
- Depend on a single metric

---

# Evaluation Architecture

```
Knowledge Base

↓

Retriever

↓

Prompt Builder

↓

LLM

↓

Generated Answer

↓

Evaluation Pipeline

↓

Metrics

↓

Dashboards

↓

Continuous Improvement
```

---

# Types of Evaluation

Production AI systems require

Offline Evaluation

↓

Online Evaluation

↓

Human Evaluation

↓

LLM-as-a-Judge

↓

Continuous Monitoring

Each answers different questions.

---

# Offline Evaluation

Run against

Golden datasets

Reference answers

Known queries

Advantages

Repeatable

Fast

Benchmark-friendly

Used before deployment.

---

# Online Evaluation

Runs in production.

Measures

Latency

Failures

User feedback

Click-through

Escalations

Real-world performance.

---

# Human Evaluation

Experts review

Correctness

Completeness

Tone

Safety

Reasoning

Still essential for high-risk domains.

---

# LLM-as-a-Judge

An LLM evaluates another model's output.

Can assess

Correctness

Grounding

Relevance

Helpfulness

Use with caution.

Validate against human reviewers.

---

# Golden Dataset

A curated benchmark.

Each example includes

Question

↓

Expected Context

↓

Expected Answer

↓

Evaluation Criteria

Golden datasets should evolve over time.

---

# Retrieval Metrics

## Recall@K

Measures

How many relevant documents were retrieved.

Higher is better.

---

## Precision@K

Measures

How many retrieved documents are actually relevant.

Higher is better.

---

## Mean Reciprocal Rank (MRR)

Measures

How early the first relevant result appears.

Higher is better.

---

## NDCG

Normalized Discounted Cumulative Gain

Measures

Ranking quality.

Considers ordering.

---

# Generation Metrics

Evaluate

Correctness

Completeness

Faithfulness

Relevance

Grounding

Conciseness

Citation quality

---

# Faithfulness

Does the answer stay grounded in retrieved context?

High faithfulness

↓

No hallucinations

↓

Evidence-backed responses

Critical for enterprise AI.

---

# Answer Relevance

Measures

Does the answer actually address the user's question?

Not

Is the answer well written?

---

# Context Precision

Measures

How much retrieved context was actually useful.

Low precision

↓

Too much irrelevant context

↓

Higher cost

↓

Lower quality

---

# Context Recall

Measures

Did retrieval provide enough information to answer correctly?

Low recall

↓

Incomplete answers

↓

Hallucinations

---

# Hallucination Detection

Detect

Unsupported claims

Invented citations

Fabricated facts

Contradictions

Missing evidence

Hallucinations should be monitored continuously.

---

# Citation Evaluation

Verify

Every factual statement

↓

Supported by retrieved sources

↓

Correct citation

↓

Correct document

↓

Correct page

---

# Latency Evaluation

Measure

Retrieval

↓

Reranking

↓

Prompt Building

↓

LLM

↓

Streaming

↓

Total Response Time

Optimize bottlenecks.

---

# Cost Evaluation

Monitor

Embedding cost

↓

Inference cost

↓

Reranking cost

↓

Storage cost

↓

Cost per request

↓

Monthly spend

Quality improvements should justify additional cost.

---

# A/B Testing

Compare

Prompt A

↓

Prompt B

or

Retriever A

↓

Retriever B

Use statistically significant traffic.

---

# Regression Testing

Every deployment should verify

Retrieval quality

Prompt quality

Memory behavior

Latency

Safety

Avoid quality regressions.

---

# Engineering Decisions

## Use RAGAs

When

Evaluating RAG pipelines

Measures

Faithfulness

Context Precision

Context Recall

Answer Relevance

Recommended for most RAG systems.

---

## Use DeepEval

When

Testing AI applications

Supports

Hallucination detection

Prompt evaluation

Custom metrics

Recommended for AI agents.

---

## Use LangSmith

When

Tracing

Debugging

Prompt comparisons

Workflow evaluation

Useful for LangChain ecosystems.

---

## Build Custom Evaluators

When

Domain-specific requirements exist

Examples

Finance

Healthcare

Legal

Enterprise policies

---

# Continuous Evaluation

Evaluation should run

Every deployment

↓

Nightly benchmarks

↓

Production monitoring

↓

Canary releases

↓

Major model updates

Never evaluate only once.

---

# Benchmarking

Benchmark

Embedding models

Retrievers

Rerankers

Prompt templates

LLMs

Memory strategies

Keep historical results.

---

# Observability

Track

Latency

Errors

Recall

Precision

Faithfulness

Hallucinations

User feedback

Cost

Token usage

---

# Metrics Dashboard

Monitor

Recall@10

Precision@10

MRR

Faithfulness

Answer Relevance

Hallucination Rate

Average Latency

Average Cost

User Satisfaction

Production dashboards should update continuously.

---

# Performance Considerations

Evaluation pipelines should

Run asynchronously

Cache repeated evaluations

Sample production traffic

Avoid increasing user latency.

---

# Security

Protect

Evaluation datasets

User conversations

Sensitive documents

Prompt logs

Evaluation systems should follow the same security standards as production systems.

---

# Common Failures

- No golden dataset
- Measuring only latency
- Ignoring hallucinations
- Comparing prompts without benchmarks
- Manual evaluation only
- No regression testing
- No production monitoring
- Optimizing for one metric

---

# Best Practices

- Build a representative golden dataset.
- Measure retrieval and generation separately.
- Track trends over time.
- Benchmark before every release.
- Use multiple evaluation metrics.
- Combine automated and human evaluation.
- Store historical benchmark results.
- Treat evaluation as part of CI/CD.

---

# Anti-Patterns

❌ Judging quality from a few manual tests

❌ Measuring only BLEU or ROUGE

❌ Ignoring retrieval metrics

❌ No regression tests

❌ Evaluating only after deployment

❌ Optimizing prompts without benchmarks

❌ Assuming newer models are always better

---

# Testing

Verify

Golden dataset execution

Metric correctness

Hallucination detection

Prompt comparisons

Regression suite

Cost reporting

Latency reporting

Dashboard updates

---

# Review Checklist

□ Golden dataset created

□ Retrieval metrics configured

□ Generation metrics configured

□ Hallucination detection enabled

□ Benchmark suite automated

□ Regression tests integrated

□ Dashboards configured

□ Cost monitored

□ Human review process defined

□ Historical results stored

---

# Related Skills

- retrieval.md
- reranking.md
- prompt_builder.md
- memory.md
- guardrails.md

---

# Definition of Done

An evaluation system is production-ready only if

✓ Golden datasets exist

✓ Retrieval quality is measured

✓ Generation quality is measured

✓ Hallucinations are monitored

✓ Automated regression testing is integrated

✓ Production metrics are continuously collected

✓ Dashboards visualize trends over time

✓ Cost and latency are tracked

✓ Human evaluation complements automated evaluation

✓ Every significant system change is benchmarked before release