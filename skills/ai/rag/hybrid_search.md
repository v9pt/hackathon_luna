# Skill

Hybrid Search

Version: 1.0

---

# Goal

Combine semantic search and lexical search to maximize retrieval quality across diverse query types while maintaining low latency and high precision.

Hybrid search is the default retrieval strategy for most production Retrieval-Augmented Generation (RAG) systems.

---

# When to Load

Load this skill whenever building

- Enterprise Search
- Production RAG
- AI Knowledge Bases
- AI Coding Assistants
- Documentation Search
- Customer Support AI
- Internal Search Platforms

---

# Prerequisites

- retrieval.md
- vector_databases.md

---

# Core Principles

No single retrieval method is universally optimal.

Semantic Search

+

Lexical Search

+

Metadata Filters

↓

Higher Recall

↓

Higher Precision

↓

Better User Experience

Hybrid search should be the default unless evaluation proves otherwise.

---

# Why Hybrid Search?

Dense embeddings understand meaning.

Example

Query

```
How do I deploy containers?
```

Semantic search can retrieve

```
Docker Deployment Guide
```

even if the word *container* never appears.

---

Lexical search understands exact words.

Example

Query

```
ERR_CONNECTION_RESET
```

A dense embedding may fail.

BM25 retrieves the exact documentation immediately.

---

Together they solve each other's weaknesses.

---

# Architecture

```
                User Query

                     │

         ┌───────────┴───────────┐

         ▼                       ▼

Semantic Search            BM25 Search

         ▼                       ▼

 Semantic Results       Lexical Results

          \                 /

           \               /

            ▼             ▼

            Fusion Engine

                  │

                  ▼

            Re-ranked Results

                  │

                  ▼

            Prompt Builder
```

---

# Components

Hybrid search consists of

Semantic Retrieval

↓

Lexical Retrieval

↓

Metadata Filtering

↓

Fusion

↓

Ranking

↓

Top-K Selection

---

# Semantic Search

Uses

Embeddings

↓

Vector Database

↓

Similarity Search

Advantages

- Understands intent
- Handles paraphrases
- Supports natural language

Weaknesses

- Misses exact identifiers
- Misses product codes
- Misses rare terminology

---

# Lexical Search

Uses

BM25

TF-IDF

Keyword Matching

Advantages

- Exact matches
- Fast
- Reliable for identifiers

Weaknesses

- No semantic understanding
- Poor synonym handling

---

# Metadata Filtering

Apply filters before ranking.

Examples

department = Engineering

language = English

created_after = 2026

author = Alice

Hybrid search should always support metadata constraints.

---

# Fusion

Fusion combines multiple ranked result lists.

Goal

Produce one better ranking.

---

# Reciprocal Rank Fusion (RRF)

Most widely used fusion algorithm.

Formula

```
Score = Σ 1 / (k + rank)
```

Advantages

- Simple
- Stable
- No score normalization
- Works across retrieval methods

Recommended default.

---

# Weighted Score Fusion

Example

```
0.7 × Semantic

+

0.3 × BM25
```

Useful when one signal is more reliable.

Requires score normalization.

---

# Borda Count

Ranks results by voting.

Simple.

Rarely used in modern RAG systems.

---

# Learning-to-Rank

Machine learning model combines

Semantic Score

Lexical Score

Freshness

Popularity

Metadata

User History

Highest quality

Most complex.

---

# Score Normalization

Different retrieval systems produce different score ranges.

Normalize scores before weighted fusion.

Common techniques

- Min-Max
- Z-score
- Softmax

RRF does not require normalization.

---

# Query Types

## Semantic Questions

Example

```
How can I secure APIs?
```

Dense search dominates.

---

## Exact Identifiers

Example

```
HTTP_401

ERR_404

SKU-18372
```

Lexical search dominates.

---

## Mixed Queries

Example

```
Docker deployment error 503
```

Hybrid search performs best.

---

# Engineering Decisions

## Use Dense Search Only

When

Small datasets

Conversational assistants

Research prototypes

Low operational complexity

---

## Use BM25 Only

When

Legal citations

Product IDs

Source code identifiers

Error codes

File names

---

## Use Hybrid Search

When

Enterprise documentation

Customer support

Internal knowledge

Developer documentation

Code search

Production RAG

Recommended default.

---

# Implementation Patterns

## Pattern 1

Semantic

↓

BM25

↓

RRF

↓

Top-K

Simple and effective.

---

## Pattern 2

Semantic

↓

BM25

↓

Metadata Filter

↓

Cross Encoder

↓

Prompt

Highest quality.

---

## Pattern 3

Semantic

↓

BM25

↓

Fusion

↓

MMR

↓

Prompt

Improves diversity.

---

# Freshness

Sometimes

Recent documents

should outrank

Highly similar but outdated documents.

Include freshness as a ranking feature.

---

# Diversity

Avoid

Five nearly identical chunks.

Prefer

Relevant

+

Different

+

Complementary

information.

Use MMR after fusion.

---

# Performance Considerations

Parallelize

Semantic Search

BM25 Search

Fusion

Do not execute sequentially.

---

# Scaling

Large systems should

Shard indexes

Cache hot queries

Cache BM25 indexes

Optimize vector indexes

Use asynchronous retrieval

---

# Security

Apply authorization before fusion.

Never fuse results across tenants.

Always filter unauthorized documents first.

---

# Observability

Track

Semantic latency

Lexical latency

Fusion latency

Recall@K

Precision@K

Search throughput

Cache hit rate

---

# Metrics

Measure

Recall@10

Recall@20

Precision@10

MRR

NDCG

Latency

Fusion Quality

Result Diversity

---

# Common Failures

- Overweighting BM25
- Ignoring semantic search
- No metadata filtering
- No score normalization
- Sequential retrieval
- Duplicate chunks
- Cross-tenant retrieval
- Large Top-K values

---

# Best Practices

- Use RRF as the default fusion algorithm.
- Execute dense and sparse searches in parallel.
- Apply metadata filters early.
- Tune weights using evaluation, not intuition.
- Evaluate hybrid search against dense-only baselines.
- Measure latency and retrieval quality together.

---

# Anti-Patterns

❌ Dense search only for enterprise systems

❌ Keyword search only

❌ Sequential retrieval

❌ Ignoring metadata

❌ Fixed fusion weights without evaluation

❌ Returning duplicate chunks

❌ No diversity optimization

---

# Testing

Verify

Dense retrieval

BM25 retrieval

Fusion correctness

Metadata filtering

Latency

Recall

Duplicate removal

Multi-tenant isolation

---

# Review Checklist

□ Dense retrieval implemented

□ BM25 configured

□ Fusion algorithm selected

□ Metadata filtering enabled

□ Parallel execution implemented

□ Duplicate removal verified

□ Metrics configured

□ Security reviewed

□ Benchmarks completed

---

# Related Skills

- retrieval.md
- reranking.md
- prompt_builder.md
- evaluation.md

---

# Definition of Done

A hybrid search implementation is production-ready only if

✓ Dense and lexical retrieval run in parallel

✓ Metadata filtering is enforced

✓ Fusion improves retrieval quality

✓ Duplicate results are removed

✓ Latency meets system SLAs

✓ Recall and precision outperform dense-only retrieval

✓ Security is enforced

✓ Metrics are continuously monitored

✓ Benchmarks validate the chosen fusion strategy

✓ Hybrid search remains provider-independent