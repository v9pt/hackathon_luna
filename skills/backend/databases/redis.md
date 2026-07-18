# Skill

Redis Engineering

Version: 1.0

---

# Goal

Design high-performance backend systems using Redis for caching, sessions, messaging, distributed coordination, and temporary state.

Redis is an in-memory data store.

It is not a replacement for PostgreSQL or MongoDB.

Use Redis for speed, not permanent storage.

---

# Design Philosophy

Persistent Data

↓

PostgreSQL / MongoDB

↓

Frequently Accessed Data

↓

Redis Cache

↓

Client

Redis should reduce latency and database load.

Never make Redis the source of truth unless the application is explicitly designed that way.

---

# Preferred Stack

Redis 7+

redis-py (asyncio)

FastAPI

Celery

RQ

Docker

RedisInsight

---

# Primary Use Cases

Use Redis for

Caching

Rate Limiting

Sessions

JWT Blacklists

OTP Storage

Queues

Distributed Locks

Pub/Sub

WebSockets

Feature Flags

Temporary AI State

Conversation Context

Task Progress

---

# Data Structures

Choose the correct structure.

String

Simple values

JWT blacklist

OTP

Counters

Hash

Objects

User sessions

Settings

List

Queues

Recent messages

Streams

Event pipelines

Pub/Sub

Notifications

Set

Unique values

Permissions

Tags

Online users

Sorted Set

Leaderboards

Scheduling

Priority queues

Ranking

Bitmap

Feature toggles

Bloom Filter

Duplicate detection

HyperLogLog

Approximate counting

---

# Caching

Cache only

Frequently requested

Expensive to compute

Rarely changing

Examples

User profiles

Configuration

AI prompts

Search results

Analytics

API responses

Never cache

Sensitive data

Financial transactions

Authorization decisions

---

# Cache Keys

Use descriptive keys.

Good

user:123

conversation:456

project:12

feature_flags

session:abc123

Avoid

cache1

temp

data

Use namespaces.

---

# TTL

Always define expiration.

Examples

OTP

5 minutes

Session

30 minutes

Cache

5–60 minutes

AI Context

15 minutes

Never leave temporary keys without TTL.

---

# Cache Strategies

Cache Aside

Application reads database.

Stores result in Redis.

Recommended default.

Write Through

Update database and cache together.

Write Behind

Write cache first.

Persist asynchronously.

Read Through

Redis automatically loads missing values.

Choose based on consistency requirements.

---

# Cache Invalidation

Prefer

Explicit invalidation

Versioned keys

Short TTL

Never assume cached data is always correct.

Invalidation is one of the hardest problems.

---

# Sessions

Store

Session ID

User ID

Expiration

Permissions

Last Activity

Always expire sessions.

---

# Rate Limiting

Implement

Sliding Window

Token Bucket

Fixed Window

Leaky Bucket

Protect

Login

Register

Password Reset

AI APIs

Search

File Upload

Public APIs

---

# Distributed Locks

Use for

Scheduled Jobs

Cron Tasks

Payment Processing

Inventory

Background Workers

Prevent duplicate execution.

---

# Pub/Sub

Use for

Notifications

Live dashboards

Chat

WebSockets

AI progress updates

Avoid using Pub/Sub for guaranteed delivery.

---

# Streams

Preferred for

Task queues

Event processing

Agent workflows

Message replay

Audit events

Streams provide persistence unlike Pub/Sub.

---

# AI Use Cases

Store

Conversation State

Prompt Cache

Embedding Cache

LLM Response Cache

Tool Results

Rate Limits

Agent Memory

Workflow Progress

Temporary Retrieval Results

Never store long-term memory only in Redis.

---

# Background Jobs

Redis can broker

Celery

RQ

BullMQ

Arq

Store

Task Status

Retries

Queue Length

Execution Metadata

---

# Performance

Monitor

Memory

Evictions

Key Count

Hit Ratio

Latency

CPU

Slow Commands

Blocked Clients

Aim for

Cache Hit Ratio

>90%

---

# Persistence

Redis supports

RDB

AOF

Hybrid

Choose based on

Recovery needs

Performance

Business requirements

---

# High Availability

Use

Redis Sentinel

Redis Cluster

Replication

Failover

Avoid single-node production deployments.

---

# Security

Enable authentication.

Use ACLs.

Restrict network access.

Use TLS.

Disable dangerous commands when possible.

Never expose Redis publicly.

---

# Common Mistakes

❌ No TTL

❌ Storing permanent data

❌ Huge values

❌ Large key scans

❌ KEYS * in production

❌ Ignoring memory limits

❌ Cache stampede

❌ Missing invalidation

---

# Monitoring

Track

Cache Hit Rate

Memory Usage

Evictions

Expired Keys

Replication Lag

Queue Size

Command Latency

Blocked Clients

---

# Testing

Test

Cache Miss

Cache Hit

Expiration

Invalidation

Rate Limits

Pub/Sub

Locks

Streams

Worker Failures

---

# Review Checklist

□ TTL defined

□ Keys namespaced

□ Cache strategy chosen

□ Invalidation implemented

□ Rate limiting tested

□ Sessions expire

□ Security enabled

□ Monitoring configured

□ Tests written

---

# Definition of Done

✓ Cache strategy documented

✓ TTL implemented

✓ Security configured

✓ Performance reviewed

✓ Monitoring enabled

✓ Tested

✓ Production ready