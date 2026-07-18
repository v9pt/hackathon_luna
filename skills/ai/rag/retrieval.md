# Skill

Retrieval

Version: 1.0

---

# Goal

Retrieve the most relevant, diverse, and trustworthy pieces of information from a knowledge base for a given user query.

Retrieval is the bridge between stored knowledge and language model generation.

A Retrieval-Augmented Generation (RAG) system is only as good as its retriever.

---

# When to Load

Load this skill whenever building

- RAG systems
- Enterprise Search
- AI Assistants
- Semantic Search
- Knowledge Bases
- Internal Documentation Search
- AI Coding Assistants

---

# Prerequisites

- chunking.md
- embeddings.md
- vector_databases.md

---

# Core Principles

Retrieval should maximize

Relevance

↓

Coverage

↓

Diversity

↓

Freshness

↓

Trustworthiness

Never optimize only for similarity score.

---

# Responsibilities

A retriever should

- Transform queries
- Search vector databases
- Apply metadata filters
- Rank initial candidates
- Return relevant context

It should not

- Generate answers
- Summarize documents
- Hallucinate missing information

---

# Retrieval Pipeline

```
User Query

↓

Normalize Query

↓

Query Transformation

↓

Metadata Filters

↓

Vector Search

↓

Candidate Chunks

↓

MMR / Diversification

↓

Top-K Results

↓

Reranker

↓

Prompt Builder
```

---

# Retrieval Objectives

A good retriever should

Return relevant chunks

Avoid duplicates

Preserve diversity

Minimize irrelevant context

Support filtering

Remain fast

---

# Query Processing

Before retrieval

Normalize

↓

Remove noise

↓

Detect language

↓

Extract entities

↓

Apply filters

↓

Search

Never embed raw user input without preprocessing.

---

# Query Transformation

Users often ask vague questions.

Transform

"What about Docker?"

into

"Docker deployment architecture, containers, orchestration"

before retrieval.

Methods include

- Query expansion
- Synonym generation
- Entity extraction
- LLM-based rewriting

---

# Metadata Filtering

Apply structured filters before similarity search when possible.

Examples

```
language = "English"

department = "Engineering"

document_type = "Policy"

updated_after = "2026-01-01"
```

Filtering improves both speed and precision.

---

# Top-K Retrieval

Return the K most relevant candidates.

Typical values

K = 5

K = 10

K = 20

Choosing K

Too small

↓

Misses context

Too large

↓

Adds noise

Tune K through evaluation.

---

# Similarity Threshold

Not every result should be accepted.

Reject chunks below a minimum similarity score.

Benefits

Reduces hallucinations

Improves context quality

---

# Multi-Query Retrieval

Generate multiple search queries.

Example

User

"How do I deploy Docker?"

Queries

- Docker deployment
- Container deployment
- Docker production
- Kubernetes Docker deployment

Merge all retrieved candidates.

Improves recall.

---

# Self-Query Retrieval

Use an LLM to infer filters.

Example

User

"Show HR policies from last year."

Generated filter

```
department = HR

year = 2025
```

Then perform filtered retrieval.

Useful for enterprise search.

---

# Parent-Child Retrieval

Retrieve

Small child chunks

↓

Expand

↓

Return parent section

Benefits

High precision

Large context

Reduced fragmentation

---

# Context Compression

Sometimes retrieved chunks are too large.

Compress

↓

Remove irrelevant sentences

↓

Keep essential information

↓

Pass compact context to the LLM

Reduces token cost.

---

# Maximal Marginal Relevance (MMR)

MMR balances

Similarity

+

Diversity

Instead of returning five nearly identical chunks,

return

Relevant

Different

Complementary

information.

Preferred in production systems.

---

# Fusion Retrieval

Combine multiple retrieval methods.

Example

Dense Search

+

Keyword Search

+

Metadata Filtering

↓

Merge

↓

Deduplicate

↓

Rank

Higher recall than any individual method.

---

# Hybrid Retrieval

Hybrid retrieval combines

Dense vectors

+

Sparse search (BM25)

↓

Unified ranking

Recommended for enterprise search.

---

# Freshness

Knowledge changes.

Prefer

Recent documents

↓

Current policies

↓

Latest documentation

Freshness may outweigh similarity in some domains.

---

# Confidence Scoring

Each retrieved chunk should include

Similarity score

Source

Timestamp

Metadata

Confidence estimate

Useful for downstream ranking.

---

# Multi-Tenant Retrieval

Never search across tenants.

Always apply tenant filters before retrieval.

Isolation is mandatory.

---

# Pagination

Support

Top 10

↓

Next 10

↓

Next 10

Useful for search interfaces.

---

# Caching

Cache

Frequent queries

Popular searches

Hot documents

Improves latency.

---

# Engineering Decisions

## When to Use Dense Retrieval

Use when

Semantic meaning matters

Natural language queries

Knowledge bases

Documentation

Default choice for most RAG systems.

---

## When to Use Keyword Search

Use when

Exact identifiers

Product IDs

Error codes

File names

Function names

Legal references

---

## When to Use Hybrid Retrieval

Use when

Enterprise documentation

Mixed query styles

Large corpora

High precision requirements

Recommended for production.

---

## When to Use Multi-Query

Use when

Users ask ambiguous questions

Recall is more important than latency

Research assistants

Legal search

Medical search

Trade-off

Higher token cost

Higher latency

---

## When to Use Parent-Child Retrieval

Use when

Large manuals

Books

Policies

Research papers

Long technical documents

---

# Performance Considerations

Optimize

Query latency

↓

Metadata filtering

↓

ANN search

↓

Network latency

↓

Caching

↓

Parallel retrieval

Measure end-to-end retrieval time.

---

# Security

Enforce

Authentication

Authorization

Tenant isolation

Metadata filtering

Audit logging

Never retrieve unauthorized content.

---

# Observability

Track

Query latency

Top-K size

Similarity scores

Cache hit rate

Filter usage

Failed searches

Retrieval success

---

# Metrics

Monitor

Recall@K

Precision@K

MRR

NDCG

Latency

Filter efficiency

Cache hit ratio

Query throughput

These metrics should drive optimization decisions.

---

# Testing

Verify

Dense retrieval

Metadata filtering

Hybrid search

Multi-query retrieval

Tenant isolation

Similarity thresholds

Pagination

Caching

Failure recovery

---

# Common Failures

- Returning duplicate chunks
- Ignoring metadata
- Using oversized K values
- No similarity threshold
- Cross-tenant leakage
- Poor query rewriting
- No evaluation
- High latency

---

# Best Practices

- Apply metadata filters early.
- Tune K empirically.
- Use MMR for diversity.
- Monitor Recall@K.
- Cache frequent queries.
- Support query rewriting.
- Keep retrieval provider-independent.
- Evaluate continuously.

---

# Anti-Patterns

❌ Blindly retrieving Top-100

❌ Ignoring metadata

❌ Exact search for semantic queries

❌ Dense search for error codes

❌ No tenant isolation

❌ No similarity threshold

❌ No retrieval evaluation

❌ Assuming the highest similarity is always the best answer

---

# Review Checklist

□ Query normalization implemented

□ Metadata filtering applied

□ Similarity threshold configured

□ Top-K tuned

□ MMR supported

□ Caching implemented

□ Tenant isolation verified

□ Metrics configured

□ Retrieval benchmarked

□ Tests passing

---

# Related Skills

- vector_databases.md
- hybrid_search.md
- reranking.md
- prompt_builder.md
- evaluation.md

---

# Definition of Done

A retrieval system is production-ready only if

✓ Queries are normalized

✓ Metadata filters are enforced

✓ Top-K is tuned through evaluation

✓ Similarity thresholds reduce irrelevant context

✓ Diversity is considered (MMR or equivalent)

✓ Multi-tenancy is enforced

✓ Metrics are continuously monitored

✓ Retrieval latency meets SLA targets

✓ Recall and precision are benchmarked

✓ Retrieval quality is validated before deployment