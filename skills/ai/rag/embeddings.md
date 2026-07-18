# Skill

Embeddings

Version: 1.0

---

# Goal

Design high-quality semantic representations of information that maximize retrieval accuracy while remaining provider-independent, scalable, and observable.

Embeddings are numerical representations of meaning.

Good embeddings make retrieval possible.

Poor embeddings make even the best LLM useless.

---

# When to Load

Load this skill whenever

- Building RAG
- Semantic Search
- Enterprise Search
- Knowledge Bases
- Recommendation Systems
- Similarity Search
- Multi-Agent Memory

---

# Prerequisites

- chunking.md

---

# Core Principle

Embeddings represent semantic meaning.

They do NOT represent

Formatting

Grammar

Exact wording

Instead they represent

Meaning

Concepts

Relationships

Intent

Similarity

---

# Embedding Pipeline

```
Chunk

↓

Preprocessing

↓

Embedding Model

↓

Vector

↓

Vector Database

↓

Similarity Search
```

---

# Architecture

```
Chunk

↓

Embedding Service

↓

Provider Adapter

↓

Embedding Model

↓

Vector Database

↓

Retriever
```

Never generate embeddings inside API routes.

---
# Engineering Decisions

## OpenAI Embeddings

Use when

Highest quality

General-purpose retrieval

Trade-off

API cost.

---

## Voyage AI

Use when

Production semantic search

Long-context retrieval

High multilingual quality.

---

## BGE Models

Use when

Self-hosting

Cost optimization

Offline deployments.

---

## E5 Models

Use when

Instruction-aware retrieval

Enterprise RAG.

---

## Hybrid Dense + Sparse

Recommended default for enterprise search.

Balances semantic understanding and keyword matching.
# Real-World Production Examples

## OpenAI

Uses dense embeddings for semantic retrieval.

---

## Microsoft Copilot

Combines embeddings with permission-aware retrieval.

---

## Perplexity

Uses embeddings alongside keyword retrieval and reranking.

---

## GitHub Copilot

Embeds source code using code-aware representations instead of generic text embeddings.
# Responsibilities

Embedding systems should

Generate vectors

Version vectors

Track metadata

Support multiple providers

Monitor latency

Monitor cost

Support re-indexing

They should not

Retrieve documents

Generate responses

Construct prompts

---

# Embedding Models

Examples

OpenAI

Voyage AI

Jina AI

BAAI

Cohere

Sentence Transformers

Ollama

E5

BGE

Nomic

Use abstraction.

Never couple business logic to one provider.

---

# Dense Embeddings

Most modern RAG systems use

Dense vectors.

Advantages

Semantic understanding

Language understanding

Robust retrieval

High recall

Preferred for production.

---

# Sparse Embeddings

Represent

Keywords

Exact matching

Token frequency

Useful for

Hybrid Search

Enterprise Search

---

# Hybrid Embeddings

Combine

Dense

+

Sparse

↓

Better Retrieval

Often outperform dense-only systems.

---

# Vector Dimensions

Every embedding model produces vectors of fixed size.

Examples

384

768

1024

1536

3072

Higher dimensions

↓

Higher storage

↓

Potentially better representation

Do not compare vectors from different models.

---

# Embedding Versioning

Every vector must store

Embedding Model

↓

Embedding Version

↓

Creation Date

↓

Chunk Version

↓

Document Version

Never mix vectors from different embedding models.

---

# Normalization

Many embedding models require

Vector normalization.

Normalize consistently.

Do not mix normalized and non-normalized vectors.

---

# Similarity Metrics

Common metrics

Cosine Similarity

Dot Product

Euclidean Distance

Choose the metric recommended by the embedding model.

---

# Preprocessing

Before embedding

Normalize Unicode

↓

Remove noise

↓

Preserve structure

↓

Validate language

↓

Generate embedding

Avoid embedding corrupted text.

---

# What Should Be Embedded

Embed

Paragraphs

Sections

API Docs

Code

Tables

Policies

Knowledge Articles

Do not embed

Navigation

Headers

Footers

Duplicate content

Boilerplate

---

# Metadata

Store with every embedding

Document ID

Chunk ID

Source

Language

Owner

Workspace

Page

Section

Embedding Model

Embedding Version

Timestamp

Metadata enables filtering.

---

# Multi-Language

Choose multilingual models when

Documents span multiple languages.

Do not assume English-only embeddings.

---

# Code Embeddings

For source code

Prefer code-aware embedding models.

Chunk by

Class

↓

Function

↓

Method

↓

Block

Never embed entire repositories as one chunk.

---

# Image Embeddings

Some models support

Images

Charts

Diagrams

Screenshots

Keep image vectors separate from text vectors unless using multimodal retrieval.

---

# Re-indexing

Re-index when

Embedding model changes

↓

Chunk strategy changes

↓

Document changes

↓

Metadata changes

Always version embeddings.

---

# Batch Processing

Generate embeddings in batches.

Advantages

Lower latency

Higher throughput

Reduced cost

Avoid one request per chunk.

---

# Caching

Cache

Frequently embedded documents

↓

Previously indexed chunks

↓

Duplicate documents

Avoid regenerating identical vectors.

---

# Cost Optimization

Monitor

Token count

↓

Embedding requests

↓

Provider cost

↓

Storage cost

Embedding pipelines can become expensive at scale.

---

# Performance

Optimize

Batch size

Parallel workers

Queue length

Provider latency

Retry strategy

Measure continuously.

---
# Trade-offs

| Choice | Advantages | Disadvantages |
|---------|------------|---------------|
| Simpler implementation | Faster development | Lower retrieval quality |
| More metadata | Better filtering | Larger storage |
| Larger chunks | More context | Lower precision |
| Smaller chunks | Higher precision | More retrieval operations |
| Rich pipelines | Better quality | Higher latency |
# Security

Do not embed

Secrets

Passwords

Private Keys

Sensitive credentials

Apply redaction before embedding if necessary.

---
# Observability

Track

Processing latency

↓

Failure rate

↓

Throughput

↓

Average document size

↓

Success rate

↓

Retry count

↓

Storage growth

↓

Processing cost
# Observability

Track

Embedding Latency

Embedding Cost

Embedding Throughput

Failures

Retry Count

Provider Used

Model Version

Queue Time

---
# Metrics

Monitor

Average Processing Time

Documents Processed

Failure Rate

Retry Rate

Average Chunk Size

Average Embedding Time

Indexing Throughput

Storage Usage

# Error Handling

Handle

Provider failures

Rate limits

Timeouts

Invalid text

Oversized chunks

Retry only transient failures.

---

# Best Practices

- Use provider abstraction.
- Version every embedding.
- Batch requests.
- Attach metadata.
- Cache duplicates.
- Measure latency.
- Monitor cost.
- Keep vectors immutable.

---

# Anti-Patterns

❌ Embedding entire documents

❌ Mixing models

❌ No metadata

❌ No versioning

❌ No batching

❌ No caching

❌ Embedding headers and footers

❌ Regenerating identical vectors

---

# Metrics

Track

Embedding Latency

Embedding Cost

Vectors Created

Vectors Updated

Batch Size

Failure Rate

Cache Hit Rate

Average Queue Time

---

# Testing

Verify

Model compatibility

Vector dimensions

Normalization

Batch processing

Caching

Versioning

Retry logic

Metadata

Provider fallback

---

# Review Checklist

□ Embedding abstraction implemented

□ Provider independent

□ Versioning implemented

□ Metadata stored

□ Batch generation supported

□ Caching enabled

□ Monitoring configured

□ Security reviewed

□ Tests written

---

# Related Skills

- chunking.md
- vector_databases.md
- retrieval.md
- hybrid_search.md
- evaluation.md

---

# Definition of Done

An embedding pipeline is production-ready only if

✓ Provider abstraction exists

✓ Metadata is attached

✓ Versioning is implemented

✓ Batch processing is supported

✓ Cost is monitored

✓ Latency is measured

✓ Security is reviewed

✓ Re-indexing is supported

✓ Tests pass

✓ Pipeline scales horizontally