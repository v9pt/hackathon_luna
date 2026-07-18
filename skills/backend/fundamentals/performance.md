# Skill

Backend Performance Engineering

Version: 1.0

---

# Goal

Build backend systems that remain fast, scalable, and efficient under increasing load.

Performance is a feature.

Measure first.

Optimize second.

Never optimize blindly.

---

# Performance Philosophy

Correctness

↓

Reliability

↓

Performance

↓

Optimization

Never sacrifice correctness for speed.

---

# Performance Metrics

Always monitor

Latency

↓

Throughput

↓

CPU

↓

Memory

↓

Disk I/O

↓

Network I/O

↓

Database Time

↓

Cache Hit Rate

↓

Queue Time

↓

Error Rate

---

# Latency Goals

API

<100ms preferred

<300ms acceptable

Database

<20ms

Cache

<5ms

LLM Calls

Track separately

Never compare AI latency with CRUD endpoints.

---

# Measure Before Optimizing

Profile

Benchmark

Trace

Monitor

Never guess performance bottlenecks.

---

# Profiling

Use

py-spy

cProfile

Scalene

OpenTelemetry

Profilers before optimization.

---

# API Optimization

Prefer

Async

Pagination

Compression

Caching

Connection Pooling

Streaming

Avoid

Blocking code

Large payloads

Repeated serialization

---

# Database Optimization

Always

Create indexes

Avoid N+1 queries

Batch operations

Select required columns

Use pagination

Review query plans

Use EXPLAIN ANALYZE.

---

# Query Optimization

Good

SELECT id,name

Bad

SELECT *

Never fetch unnecessary data.

---

# Connection Pooling

Pool

Database

Redis

HTTP Clients

MongoDB

Reuse connections.

Never create one connection per request.

---

# Redis

Cache

Configuration

Sessions

User Profiles

AI Responses

Search Results

Prompt Results

Conversation Metadata

Monitor hit ratio.

Target

90%+

---

# Async

Prefer

async def

await

httpx.AsyncClient

Motor

SQLAlchemy Async

Avoid

requests

time.sleep()

Blocking filesystem operations

---

# Parallelism

Use

asyncio.gather()

Task Groups

Worker Queues

Parallelize independent work.

Never parallelize dependent work.

---

# Batch Processing

Prefer

Bulk Inserts

Bulk Updates

Batch Embeddings

Batch Emails

Batch Notifications

Avoid

One request per item.

---

# Pagination

Never return unlimited results.

Support

Limit

Offset

Cursor

Infinite Scroll

---

# Background Processing

Move expensive work to

Celery

Arq

RQ

BackgroundTasks

Examples

Emails

Reports

Embeddings

LLM Calls

OCR

Image Processing

---

# Streaming

Use streaming for

LLM Responses

Large Files

CSV Export

Logs

WebSockets

Reduce perceived latency.

---

# Compression

Enable

Gzip

Brotli

Compress

JSON

HTML

CSS

JavaScript

Avoid compressing already compressed files.

---

# Serialization

Prefer

orjson

Pydantic v2

Avoid expensive serialization loops.

---

# File Uploads

Stream uploads.

Avoid loading large files into memory.

Validate early.

---

# AI Performance

Optimize

Prompt Size

Context Window

Retrieval

Embedding Cache

Prompt Cache

Model Selection

Fallback Models

Tool Calls

Token Usage

Track

Latency

Cost

Token Count

Retries

---

# Memory

Watch

Memory Leaks

Large Objects

Unused Variables

Caches

Worker Memory

Release unused resources.

---

# CPU

Monitor

Serialization

Image Processing

Embedding Generation

OCR

PDF Parsing

Offload heavy work.

---

# Network

Reduce

Round Trips

Payload Size

Repeated Requests

Combine related requests.

---

# Docker

Optimize

Small Images

Health Checks

Resource Limits

Build Cache

Multi-stage Builds

---

# Load Testing

Test

100 Users

500 Users

1000 Users

Burst Traffic

AI Spikes

Slow Database

Slow LLM

Worker Failures

---

# Benchmarking

Measure

Cold Start

Warm Requests

Average

P95

P99

Never optimize averages only.

---

# Monitoring

Track

Latency

Throughput

CPU

Memory

Queue Size

Redis Hit Ratio

Database Queries

External APIs

AI Cost

---

# Common Bottlenecks

Database

Redis Misses

Large JSON

Repeated Queries

Large Responses

Blocking Code

Slow LLM

Slow OCR

Poor Indexes

Missing Cache

---

# Anti-Patterns

❌ SELECT *

❌ Blocking requests

❌ No pagination

❌ No indexes

❌ Repeated API calls

❌ Duplicate embeddings

❌ Huge payloads

❌ Loading entire files

❌ Synchronous I/O

---

# Performance Checklist

□ Async APIs

□ Database indexed

□ Redis enabled

□ Connection pooling

□ Pagination

□ Compression

□ Background jobs

□ Profiling completed

□ Benchmarks recorded

□ Monitoring enabled

---

# Definition of Done

Performance work is complete only if

✓ Profiled

✓ Benchmarked

✓ Indexed

✓ Cached

✓ Async

✓ Monitored

✓ Scalable

✓ Production ready