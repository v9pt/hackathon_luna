# Rate Limiting

Version: 1.0

---

# Goal

Protect AI systems from overload, abuse, cascading failures, and uncontrolled resource consumption by controlling request rates, concurrency, and resource allocation.

Rate limiting ensures fair resource usage, predictable latency, operational stability, and cost control while maintaining a high-quality user experience.

A production rate limiting system should maximize availability while preventing individual users, services, or workflows from monopolizing shared resources.

---

# When to Use

Rate limiting applies whenever

- public APIs exist
- LLM providers enforce quotas
- GPUs are shared
- multi-tenant systems exist
- external APIs are consumed
- abuse is possible
- costs must be controlled
- infrastructure has finite capacity

---

# Problem

Without rate limiting

- abusive clients consume resources
- retry storms overload services
- GPUs become saturated
- LLM provider quotas are exceeded
- latency increases
- cascading failures occur
- infrastructure costs explode

A single client should never be able to destabilize the entire platform.

---

# Solution

Control

Requests

↓

Concurrency

↓

Resource Usage

↓

Backpressure

↓

Recovery

↓

Stable System

Protection should occur before overload happens.

---

# Core Principles

Protect

↓

Prioritize

↓

Throttle

↓

Recover

↓

Scale

Every request competes for limited resources.

---

# Architecture

```
Client

↓

API Gateway

↓

Rate Limiter

↓

Admission Control

↓

Queue

↓

AI Services

↓

LLMs
```

---

# Components

## Request Counter

Tracks

- requests
- users
- organizations
- IPs
- API keys

Provides the foundation for rate limiting.

---

## Quota Manager

Enforces limits such as

- requests/minute
- requests/day
- tokens/day
- workflow executions
- concurrent sessions

---

## Concurrency Controller

Limits

- simultaneous requests
- concurrent agents
- parallel workflows
- active GPU jobs

Concurrency control protects expensive resources.

---

## Admission Controller

Determines

Accept

Delay

Reject

based on system health and capacity.

---

## Queue

Buffers accepted requests.

Useful during temporary traffic spikes.

Queues smooth demand rather than dropping every burst.

---

# Request Lifecycle

Client

↓

Authentication

↓

Quota Check

↓

Rate Limit Check

↓

Admission

↓

Execution

↓

Response

---

# Algorithms

## Fixed Window

Example

100 requests

per minute

Simple.

May allow bursts at window boundaries.

---

## Sliding Window

Calculates limits continuously.

Provides smoother enforcement.

Recommended for most APIs.

---

## Token Bucket

Bucket contains tokens.

Each request consumes one.

Tokens refill over time.

Supports controlled bursts.

Recommended default.

---

## Leaky Bucket

Requests enter queue.

Processed at constant rate.

Excellent for smoothing traffic.

---

## Concurrency Limits

Restrict

simultaneous execution

rather than request frequency.

Especially useful for GPU inference.

---

# AI-Specific Limits

Examples

Requests/minute

Tokens/minute

Tokens/day

Embeddings/minute

Agent executions/hour

Workflow executions/day

Concurrent tool calls

Concurrent GPU jobs

---

# Multi-Tenant Isolation

Separate limits for

- free users
- premium users
- enterprise customers
- internal services

Higher-tier customers should not be affected by abusive lower-tier traffic.

---

# Burst Handling

Allow temporary spikes while preventing sustained overload.

Techniques

- token buckets
- queues
- burst quotas

---

# Backpressure

When capacity is limited

Clients should

- wait
- retry later
- reduce request rate

Backpressure prevents cascading failures.

---

# Retry Strategy

Retries should use

Exponential Backoff

+

Jitter

Avoid synchronized retry storms.

---

# Circuit Breakers

If downstream services fail repeatedly

Open Circuit

↓

Reject Requests

↓

Recovery Period

↓

Half-Open

↓

Resume

Circuit breakers protect dependencies.

---

# Load Shedding

Discard

low-priority requests

before high-priority workloads are affected.

Recommended during overload.

---

# Priority Scheduling

Prioritize

Enterprise

↓

Premium

↓

Internal Services

↓

Free Tier

↓

Background Jobs

Critical workloads receive resources first.

---

# Fairness

Prevent

- noisy neighbors
- resource monopolization
- starvation

Fair scheduling improves overall platform stability.

---

# Cost Protection

Rate limiting also protects

- API budgets
- GPU utilization
- LLM token quotas
- infrastructure spending

Operational cost and rate limiting are closely related.

---

# Monitoring

Track

- rejected requests
- throttled requests
- queue length
- wait time
- retry rate
- concurrent executions
- quota utilization

---

# Engineering Decisions

## Fixed Window

Simple.

Suitable for internal services.

---

## Sliding Window

Recommended for public APIs.

Balances simplicity and fairness.

---

## Token Bucket

Recommended default.

Supports bursts while preventing abuse.

---

## Leaky Bucket

Ideal for smoothing sustained traffic.

---

## Adaptive Rate Limiting

Adjust limits dynamically based on

- system load
- latency
- error rate

Recommended for enterprise AI platforms.

---

# Runtime Architecture

```
Client

↓

Gateway

↓

Authentication

↓

Rate Limiter

↓

Quota Manager

↓

Admission Controller

↓

Queue

↓

AI Services

↓

Models
```

---

# Performance

Optimize

queue latency

↓

quota lookup

↓

token refill

↓

request throughput

↓

burst handling

↓

concurrency utilization

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Fixed Window | Simple | Burst boundary issues |
| Sliding Window | Fair | Higher computation |
| Token Bucket | Flexible | Slightly more complex |
| Leaky Bucket | Smooth traffic | Increased latency |
| Adaptive Limits | Efficient | Operational complexity |

---

# Common Failures

- retry storms
- missing tenant isolation
- global rate limits only
- unlimited concurrency
- no backpressure
- poor queue sizing
- static quotas

---

# Best Practices

- Use token buckets for API requests.
- Limit concurrent GPU inference.
- Separate quotas by customer tier.
- Apply exponential backoff with jitter.
- Monitor rejection rates continuously.
- Use adaptive limits during peak traffic.
- Protect downstream dependencies with circuit breakers.
- Prioritize critical workloads.

---

# Anti-Patterns

❌ Unlimited retries

❌ Global limits for every customer

❌ Unlimited concurrency

❌ Ignoring GPU capacity

❌ No admission control

❌ No queues

❌ Static limits that never change

---

# Real-World Examples

## OpenAI

Applies request, token, and concurrency limits across API tiers while enforcing organization-specific quotas to ensure fairness and platform stability.

---

## Anthropic

Uses usage limits, tiered quotas, and concurrency controls to manage API capacity and provide predictable service quality.

---

## GitHub Copilot

Controls request rates, background inference, and IDE interactions to balance responsiveness with large-scale infrastructure constraints.

---

## Google Cloud

Provides quota management, adaptive throttling, and API rate limiting across managed AI services.

---

## Enterprise AI Platforms

Combine token buckets, adaptive rate limiting, circuit breakers, admission control, and workload prioritization to protect multi-tenant AI infrastructure from overload.

---

# Related Skills

- cost_optimization.md
- scaling.md
- reliability.md
- monitoring.md
- observability.md
- incident_response.md

---

# Definition of Done

A production AI rate limiting strategy is complete only if

✓ Requests, tokens, workflows, and concurrency are independently controlled

✓ Rate limiting algorithms balance fairness with operational efficiency

✓ Multi-tenant quotas isolate customer workloads

✓ Burst traffic is absorbed without destabilizing downstream services

✓ Retries implement exponential backoff with jitter

✓ Circuit breakers prevent cascading failures

✓ Admission control and load shedding protect critical workloads during overload

✓ Rate limiting metrics are continuously monitored and correlated with system health

✓ Cost controls and quota enforcement prevent uncontrolled resource consumption

✓ The platform remains stable, fair, and responsive even during traffic spikes, abuse, and infrastructure failures