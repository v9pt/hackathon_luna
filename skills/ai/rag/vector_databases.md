# Skill

Vector Databases

Version: 1.0

---

# Goal

Design scalable, high-performance vector storage systems capable of storing, indexing, filtering, and retrieving embeddings for Retrieval-Augmented Generation (RAG) applications.

A vector database is responsible for efficient similarity search over high-dimensional embeddings while supporting metadata filtering, multi-tenancy, scalability, and observability.

---

# When to Load

Load this skill whenever

- Building RAG systems
- Semantic Search
- Enterprise Search
- AI Memory
- Recommendation Systems
- Similarity Search
- Knowledge Bases

---

# Prerequisites

- embeddings.md

---

# Core Principles

A vector database should

Store vectors efficiently

↓

Support Approximate Nearest Neighbor (ANN) search

↓

Filter by metadata

↓

Scale horizontally

↓

Remain provider independent

↓

Support high-throughput retrieval

Never treat a vector database like a relational database.

---

# Responsibilities

A vector database should

- Store embeddings
- Store metadata
- Perform similarity search
- Filter results
- Manage indexes
- Handle replication
- Support backups
- Support collection management

It should **not**

- Generate embeddings
- Construct prompts
- Generate LLM responses
- Perform reranking

---

# High-Level Architecture

```
Document

↓

Chunk

↓

Embedding Model

↓

Vector

↓

Vector Database

↓

Retriever

↓

Reranker

↓

Prompt Builder

↓

LLM
```

---

# Vector Database Components

Every vector database contains

Collections

↓

Vectors

↓

Metadata

↓

Indexes

↓

Search Engine

↓

Storage Layer

---

# Collections

Collections group related vectors.

Examples

Customer Knowledge Base

Engineering Docs

Policies

Legal Documents

Product Manuals

Avoid placing unrelated knowledge into the same collection.

---

# Namespaces

Namespaces isolate data inside collections.

Useful for

Multi-tenancy

Organizations

Projects

Departments

Development vs Production

---

# Metadata (Payload)

Each vector should include metadata such as

- document_id
- chunk_id
- page
- section
- source
- language
- owner
- tenant
- tags
- created_at
- embedding_version

Never store vectors without metadata.

---

# Similarity Search

The most common similarity metrics are

## Cosine Similarity

Most widely used.

Measures angular similarity.

Recommended for most embedding models.

---

## Dot Product

Fast.

Useful when embeddings are normalized.

---

## Euclidean Distance

Measures geometric distance.

Less common for production RAG.

---

# Exact vs Approximate Search

## Exact Search

Advantages

- Perfect accuracy

Disadvantages

- Slow
- Doesn't scale

Useful only for small datasets.

---

## Approximate Nearest Neighbor (ANN)

Advantages

- Extremely fast
- Scalable
- Production ready

Disadvantages

- Slight reduction in accuracy

Preferred for nearly all production systems.

---

# ANN Index Types

## HNSW (Hierarchical Navigable Small World)

Characteristics

- Excellent recall
- Very low latency
- Memory intensive

Best for

Most production RAG systems.

---

## IVF (Inverted File Index)

Characteristics

- Lower memory usage
- Fast on very large datasets

Trade-off

Slightly lower recall than HNSW.

---

## DiskANN

Characteristics

- Optimized for SSD storage
- Handles billions of vectors

Used for

Very large enterprise deployments.

---

## Flat Index

Characteristics

- Exact search
- No approximation

Useful for

Testing

Small datasets

Evaluation

---

# Filtering

Search should support filtering by metadata.

Examples

```
department = Engineering

language = English

created_after = 2026-01-01

owner = Alice
```

Filtering improves relevance and security.

---

# Hybrid Queries

Modern systems combine

Metadata Filters

+

Vector Search

↓

Higher quality retrieval

Example

Find engineering documents related to Docker created after January.

---

# Multi-Tenancy

Always isolate tenants.

```
Tenant

↓

Collection

↓

Namespace

↓

Vectors
```

Never allow cross-tenant searches.

---

# Index Maintenance

Indexes require

Optimization

Compaction

Monitoring

Rebuilding

Versioning

Monitor index health continuously.

---

# Sharding

Split collections across multiple nodes.

Benefits

Higher throughput

Higher capacity

Better scalability

---

# Replication

Maintain multiple copies of data.

Benefits

Fault tolerance

High availability

Disaster recovery

---

# Quantization

Reduces vector size.

Common techniques

Scalar Quantization

Product Quantization (PQ)

Binary Quantization

Advantages

- Lower storage
- Faster search

Trade-off

Slight reduction in accuracy.

---

# Caching

Cache

Frequently searched vectors

Popular queries

Hot metadata filters

Improves latency significantly.

---

# Re-indexing

Rebuild indexes when

Embedding model changes

↓

Chunking changes

↓

Metadata schema changes

↓

Collection restructuring

---

# Backup Strategy

Backup

Collections

Indexes

Metadata

Configurations

Embedding versions

Regularly verify backups.

---

# Migration

Support migration between providers.

Example

```
Qdrant

↓

Pinecone

↓

Weaviate
```

Never tightly couple business logic to a specific database.

---

# Engineering Decisions

## When to Use pgvector

Choose pgvector when

- Existing PostgreSQL infrastructure
- Small to medium datasets
- Strong relational queries
- Simplicity is preferred

Avoid when handling hundreds of millions of vectors.

---

## When to Use Qdrant

Choose Qdrant when

- Dedicated vector search
- Rich metadata filtering
- Open source deployment
- High performance
- Production RAG

Excellent default choice.

---

## When to Use Pinecone

Choose Pinecone when

- Fully managed infrastructure
- Minimal operational overhead
- Fast deployment
- Enterprise SaaS

Trade-off

Higher cost.

---

## When to Use Weaviate

Choose Weaviate when

- GraphQL API
- Hybrid search
- Knowledge graphs
- Rich schema support

---

## When to Use Milvus

Choose Milvus when

- Massive datasets
- Distributed infrastructure
- High throughput

Better suited for very large deployments.

---

# Performance Considerations

Monitor

Index Build Time

↓

Search Latency

↓

Insert Latency

↓

Memory Usage

↓

Recall

↓

Storage Growth

Never optimize latency alone.

Measure recall as well.

---

# Security

Implement

Authentication

Authorization

Encryption at Rest

Encryption in Transit

Audit Logging

Tenant Isolation

---

# Observability

Track

Search latency

Index size

Memory usage

Recall

Insert rate

Query throughput

Replication lag

Filter performance

---

# Metrics

Monitor

P50 Search Latency

P95 Search Latency

Recall@10

Index Size

Collection Growth

Memory Usage

CPU Usage

Search Throughput

Failed Queries

---

# Testing

Verify

Collection creation

Metadata filtering

Vector insertion

Batch insertion

Similarity search

Deletion

Backups

Recovery

Namespace isolation

Performance

---

# Common Failures

- Mixing embedding versions
- Missing metadata
- No backups
- Oversized collections
- Cross-tenant leakage
- Poor filtering
- Unoptimized indexes
- Stale embeddings

---

# Best Practices

- Use HNSW by default.
- Store rich metadata.
- Version embeddings.
- Monitor recall.
- Backup regularly.
- Isolate tenants.
- Benchmark before choosing a provider.
- Keep retrieval provider-independent.

---

# Anti-Patterns

❌ Storing vectors without metadata

❌ Using one collection for everything

❌ Mixing embedding models

❌ Ignoring index maintenance

❌ No backups

❌ Vendor lock-in

❌ No tenant isolation

❌ Measuring only latency

---

# Review Checklist

□ Collections designed

□ Metadata schema defined

□ ANN index selected

□ Multi-tenancy implemented

□ Filtering tested

□ Backups configured

□ Monitoring enabled

□ Security reviewed

□ Benchmarks completed

□ Migration strategy documented

---

# Related Skills

- embeddings.md
- retrieval.md
- hybrid_search.md
- reranking.md

---

# Definition of Done

A vector database implementation is production-ready only if

✓ Collections are well-designed

✓ Metadata is comprehensive

✓ ANN indexes are configured

✓ Multi-tenancy is enforced

✓ Recall and latency are monitored

✓ Backups are verified

✓ Security is implemented

✓ Observability is configured

✓ Migration is possible

✓ Performance benchmarks meet system requirements