# Skill

Reranking

Version: 1.0

---

# Goal

Improve retrieval quality by reordering retrieved candidates using more accurate relevance models before passing context to the language model.

Reranking is the final quality gate between retrieval and generation.

Instead of retrieving *more* documents, reranking retrieves *better* documents.

---

# When to Load

Load this skill whenever building

- Production RAG
- Enterprise Search
- AI Chatbots
- AI Coding Assistants
- Legal Search
- Medical Search
- Research Assistants

---

# Prerequisites

- retrieval.md
- hybrid_search.md

---

# Core Principles

Initial retrieval prioritizes speed.

↓

Reranking prioritizes accuracy.

↓

LLM generation prioritizes reasoning.

Each stage has a different optimization objective.

---

# Responsibilities

A reranker should

- Score relevance
- Reorder retrieved chunks
- Remove noisy results
- Improve precision
- Preserve diversity

It should not

- Retrieve new documents
- Generate answers
- Modify source documents

---

# Retrieval Architecture

```
User Query

↓

Retriever

↓

Top-50 Candidates

↓

Reranker

↓

Top-5 Results

↓

Prompt Builder

↓

LLM
```

Retrieval finds candidates.

Reranking finds the best candidates.

---

# Why Reranking?

Vector similarity measures semantic closeness.

It does not fully understand

Context

↓

Intent

↓

Relationships

↓

Importance

A reranker performs a deeper comparison between

Query

+

Document

to determine true relevance.

---

# Multi-Stage Retrieval

Production systems typically use

```
Query

↓

Dense Search

↓

BM25

↓

Fusion

↓

Top-100

↓

Cross Encoder

↓

Top-10

↓

Prompt Builder

↓

LLM
```

Never rerank an entire corpus.

---

# Candidate Selection

Always rerank a limited candidate set.

Typical values

Top-20

Top-50

Top-100

The larger the candidate pool

↓

Higher recall

↓

Higher latency

---

# Cross Encoder

The gold standard for reranking.

Architecture

```
Query

+

Document

↓

Transformer

↓

Relevance Score
```

Advantages

Highest accuracy

Deep understanding

Best for production

Disadvantages

Slower

Higher compute cost

---

# Bi-Encoder

Embeds query and document independently.

Advantages

Fast

Scalable

Low latency

Disadvantages

Lower ranking quality

Use for retrieval, not reranking.

---

# Late Interaction Models

Examples

ColBERT

Characteristics

- Better than bi-encoders
- Faster than cross-encoders
- Token-level matching
- Higher memory usage

Suitable for very large search systems.

---

# Popular Rerankers

Commercial

- Cohere Rerank
- Voyage AI Rerank
- Jina AI Reranker

Open Source

- BGE Reranker
- CrossEncoder (Sentence Transformers)
- ColBERT

Choose based on latency, quality, and deployment needs.

---

# Scoring

Each candidate receives

```
Query

+

Chunk

↓

Relevance Score
```

Candidates are sorted by score.

Only the highest-ranked chunks proceed.

---

# Context Compression

After reranking

Remove

Duplicate chunks

↓

Low-confidence chunks

↓

Redundant context

↓

Irrelevant sections

Smaller context often produces better answers.

---

# Diversity

Do not return

Five nearly identical chunks.

Instead

Relevant

+

Different

+

Complementary

information.

MMR can be applied before or after reranking.

---

# Engineering Decisions

## Skip Reranking

When

Small datasets

Internal prototypes

Low latency requirements

Simple FAQs

Trade-off

Lower answer quality.

---

## Use Cross Encoder

When

Enterprise search

Customer support

Legal AI

Medical AI

Research assistants

Recommended default.

---

## Use ColBERT

When

Very large corpora

Millions of documents

Interactive search

Higher infrastructure complexity is acceptable.

---

## Use Hosted APIs

When

Small teams

Fast iteration

Minimal infrastructure

Examples

Cohere

Voyage AI

Jina AI

Trade-off

Vendor dependency

Per-request cost

---

## Self-Host Rerankers

When

Sensitive data

Compliance

Cost optimization

Offline deployments

Examples

BGE

CrossEncoder

ColBERT

Trade-off

Infrastructure management

---

# Performance Considerations

Monitor

Candidate count

↓

Inference latency

↓

GPU utilization

↓

Memory usage

↓

Recall

↓

Precision

Avoid reranking unnecessarily large candidate sets.

---

# Cost Optimization

Reduce costs by

- Lowering Top-K before reranking
- Batch inference
- Caching popular queries
- Using smaller rerankers for simple queries
- Applying reranking conditionally

---

# Dynamic Reranking

Not every query needs reranking.

Example

Exact product ID

↓

Keyword match

↓

Skip reranker

Complex natural language

↓

Apply reranker

Adaptive pipelines reduce latency.

---

# Security

Enforce

Authorization

Tenant isolation

Metadata filtering

Audit logging

Never rerank unauthorized documents.

---

# Observability

Track

Rerank latency

Candidate count

Precision@K

GPU utilization

Cache hit rate

Model version

Inference failures

---

# Metrics

Measure

Precision@5

Precision@10

MRR

NDCG

Latency

GPU usage

Cost per query

Rerank success rate

Evaluation should compare

Retriever alone

vs

Retriever + Reranker

---

# Common Failures

- Reranking entire collections
- Candidate pool too small
- Candidate pool too large
- Ignoring metadata filters
- Duplicate context
- No batching
- High latency
- Model version drift

---

# Best Practices

- Retrieve broadly, rerank narrowly.
- Keep candidate pools between 20–100.
- Use cross-encoders for quality-critical applications.
- Benchmark rerankers before adoption.
- Batch inference whenever possible.
- Continuously evaluate precision improvements.
- Cache common reranked queries.

---

# Trade-offs

| Approach | Quality | Latency | Cost | Scale |
|----------|---------|---------|------|------|
| No Reranker | Low | Very Low | Low | Excellent |
| Cross Encoder | Excellent | Medium | Medium | Good |
| Hosted API | Excellent | Medium | High | Excellent |
| ColBERT | Very Good | Low | Medium | Excellent |

---

# Testing

Verify

- Candidate ordering
- Duplicate removal
- Cross-encoder scoring
- Hosted provider fallback
- Batch inference
- Multi-tenant isolation
- Latency budgets
- Precision improvements

---

# Review Checklist

□ Candidate pool configured

□ Reranker selected

□ Batch inference enabled

□ Latency measured

□ Precision benchmarked

□ Duplicate removal verified

□ Security enforced

□ Metrics configured

□ Cost analyzed

□ Tests passing

---

# Related Skills

- retrieval.md
- hybrid_search.md
- prompt_builder.md
- evaluation.md

---

# Definition of Done

A reranking system is production-ready only if

✓ Candidate retrieval precedes reranking

✓ Cross-encoder or equivalent model is selected appropriately

✓ Precision improvements are validated against retrieval-only baselines

✓ Candidate pool size is optimized through evaluation

✓ Latency stays within service-level objectives

✓ Security and tenant isolation are enforced

✓ Metrics and observability are configured

✓ Costs are monitored

✓ Batch inference is implemented

✓ End-to-end retrieval quality is continuously evaluated