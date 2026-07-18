# Caching

Version: 1.0

---

# Goal

Reduce latency, infrastructure load, and operational cost by reusing previously computed results across AI applications.

Caching avoids unnecessary computation by storing reusable outputs at multiple layers of the AI stack, including prompts, embeddings, retrieval results, model responses, agent workflows, and infrastructure resources.

A production caching strategy should maximize cache usefulness while preserving correctness, freshness, and consistency.

---

# When to Use

Caching applies whenever

- repeated prompts occur
- retrieval results are reused
- embeddings are deterministic
- expensive tool calls exist
- model inference is costly
- workflows repeat
- latency requirements are strict
- infrastructure costs matter

---

# Problem

AI systems repeatedly perform expensive operations

- LLM inference
- embedding generation
- vector retrieval
- API requests
- tool execution
- database queries

Without caching

- latency increases
- costs increase
- infrastructure scales unnecessarily
- users wait longer

---

# Solution

Reuse previously computed results whenever possible.

```
Request

↓

Cache Lookup

↓

Cache Hit

↓

Immediate Response

or

↓

Cache Miss

↓

Execute

↓

Store

↓

Respond
```

---

# Core Principles

Lookup

↓

Reuse

↓

Store

↓

Expire

↓

Refresh

Only deterministic or safely reusable results should be cached.

---

# Caching Architecture

```
Client

↓

API

↓

Cache Layer

↓

AI Services

↓

Database

↓

LLM
```

---

# Components

## Cache Store

Stores

- responses
- embeddings
- retrieval results
- prompt templates
- workflow state

Examples

- Redis
- Memcached
- CDN
- Local Memory

---

## Cache Manager

Responsible for

- lookup
- insertion
- expiration
- invalidation
- eviction

---

## Cache Keys

Keys should uniquely identify

- prompt
- model
- version
- parameters
- user context

Poor cache keys reduce effectiveness.

---

# Caching Lifecycle

Request

↓

Lookup

↓

Hit?

↓

Yes → Return

↓

No

↓

Compute

↓

Store

↓

Return

---

# Cache Types

## Response Cache

Stores completed LLM responses.

Useful for

- FAQs
- documentation
- customer support
- repeated requests

---

## Prompt Cache

Stores rendered prompt templates.

Useful when prompt construction is expensive.

---

## Embedding Cache

Stores generated embeddings.

Useful because embeddings are deterministic.

Recommended default.

---

## Retrieval Cache

Stores

- vector search results
- metadata
- reranked documents

Useful for repeated semantic queries.

---

## Tool Cache

Stores

- weather data
- exchange rates
- API responses
- search results

Only cache data with acceptable freshness windows.

---

## Workflow Cache

Stores intermediate workflow outputs.

Useful for

- long-running agents
- planners
- multi-step pipelines

---

## Session Cache

Stores temporary user state.

Useful for

- conversations
- memory
- authentication

---

# Semantic Caching

Instead of exact string matching

Compare

Embedding

↓

Similarity

↓

Threshold

↓

Reuse

Useful for AI applications where similar prompts should reuse results.

---

# KV Cache

Large language models internally cache attention key/value tensors during autoregressive generation.

Benefits

- lower inference latency
- reduced computation
- faster streaming

Primarily an inference optimization implemented by model serving systems.

---

# Cache Invalidation

Invalidate when

- data changes
- model changes
- prompt changes
- user permissions change
- workflow changes

Cache invalidation should be automatic whenever possible.

---

# Expiration Policies

Examples

TTL

Sliding Expiration

Absolute Expiration

Version-Based Expiration

Choose based on data volatility.

---

# Eviction Policies

Common policies

LRU

Least Recently Used

---

LFU

Least Frequently Used

---

FIFO

First In First Out

---

Random

Simplest implementation.

LRU is generally the recommended default.

---

# Distributed Caching

Useful for

- Kubernetes
- multiple API servers
- globally distributed AI systems

Common technologies

- Redis Cluster
- Hazelcast
- KeyDB

---

# Cache Consistency

Models

Strong Consistency

Eventual Consistency

Read-Through

Write-Through

Write-Back

Read-through caching is recommended for most AI applications.

---

# Cache Warming

Populate cache before production traffic.

Useful for

- popular prompts
- documentation
- embeddings
- retrieval indexes

Reduces cold-start latency.

---

# Multi-Level Caching

```
Browser Cache

↓

CDN

↓

Application Cache

↓

Redis

↓

Database

↓

LLM
```

Each level reduces downstream load.

---

# Cache Metrics

Measure

- hit rate
- miss rate
- eviction rate
- memory usage
- lookup latency
- cache size
- stale responses

---

# Engineering Decisions

## Local Cache

Fastest.

Limited scalability.

---

## Redis

Recommended default.

Supports distributed applications.

---

## Semantic Cache

Recommended for conversational AI.

Requires embedding comparisons.

---

## Multi-Level Cache

Recommended for enterprise systems.

Balances latency and scalability.

---

# Runtime Architecture

```
User

↓

Gateway

↓

Redis

↓

AI Service

↓

Retriever

↓

LLM

↓

Database
```

---

# Performance

Optimize

cache hit rate

↓

lookup latency

↓

memory efficiency

↓

eviction frequency

↓

serialization cost

↓

TTL selection

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Local Cache | Fast | Per-instance only |
| Redis | Distributed | Network overhead |
| Semantic Cache | Higher reuse | Embedding cost |
| Long TTL | Higher hit rate | Stale data |
| Short TTL | Fresher data | More misses |

---

# Common Failures

- poor cache keys
- stale responses
- excessive invalidation
- cache stampedes
- memory exhaustion
- inconsistent cache versions
- caching user-specific data incorrectly

---

# Best Practices

- Cache deterministic computations.
- Version cache keys.
- Monitor hit rates.
- Use Redis for distributed deployments.
- Warm important caches before releases.
- Separate user-specific and global caches.
- Apply TTLs based on data volatility.
- Instrument cache performance.

---

# Anti-Patterns

❌ Caching everything

❌ Never expiring cache entries

❌ Using mutable cache keys

❌ Ignoring cache invalidation

❌ Caching sensitive user data globally

❌ Measuring only cache size

❌ No monitoring of cache effectiveness

---

# Real-World Examples

## OpenAI

Optimizes inference through internal mechanisms such as KV caching during token generation and infrastructure-level request optimizations to improve latency and efficiency.

---

## Anthropic

Employs caching and inference optimizations within serving infrastructure to reduce latency and improve throughput for repeated workloads.

---

## LangChain / LangGraph

Support semantic caching, retrieval caching, and intermediate workflow caching to reduce repeated model calls and accelerate agent execution.

---

## Redis

Acts as the primary distributed cache for prompts, embeddings, retrieval results, session state, and workflow data across many production AI systems.

---

## Enterprise AI Platforms

Use layered caching for prompt rendering, embeddings, retrieval results, model responses, and API integrations to minimize infrastructure cost while maintaining fast response times.

---

# Related Skills

- cost_optimization.md
- scaling.md
- monitoring.md
- observability.md
- deployment.md
- reliability.md

---

# Definition of Done

A production AI caching strategy is complete only if

✓ Multiple cache layers optimize different parts of the AI stack

✓ Cache keys uniquely identify reusable computations

✓ Deterministic operations such as embeddings and retrieval results are cached appropriately

✓ Cache invalidation policies preserve correctness and freshness

✓ Expiration and eviction strategies balance performance with consistency

✓ Distributed caching supports horizontally scaled deployments

✓ Hit rate, latency, and memory utilization are continuously monitored

✓ Sensitive or user-specific data is isolated appropriately

✓ Cache warming minimizes cold-start latency for critical workloads

✓ The caching system measurably reduces latency, infrastructure load, and operating costs without compromising correctness