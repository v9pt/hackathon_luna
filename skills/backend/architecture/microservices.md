# Skill

Microservices Engineering

Version: 1.0

---

# Goal

Design scalable, resilient, loosely coupled backend systems using microservice architecture.

Microservices are an organizational architecture.

Not a scalability hack.

Do not build microservices unless there is a clear need.

---

# When to Use

Use microservices when

Multiple teams

Independent deployments

Different scaling requirements

Different technology stacks

Independent business domains

Long-term product evolution

Avoid microservices for

Hackathons

Small startups

MVPs

Single-developer projects

Simple CRUD apps

Start with a modular monolith.

Extract services only when necessary.

---

# Architecture

                   API Gateway
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
 Auth Service      User Service      AI Service
        │                │                │
        └──────┐         │         ┌──────┘
               ▼         ▼         ▼
          Message Bus / Event Broker
               │
        ┌──────┼──────────────┐
        ▼      ▼              ▼
 Worker      Notification     Analytics

Each service owns its business capability.

---

# Service Principles

Each service should own

Business Logic

Database

API

Deployment

Monitoring

Documentation

Testing

Never allow another service to modify your database.

---

# Bounded Contexts

Split services by business domains.

Good

Authentication

Billing

Users

Orders

AI

Notifications

Search

Analytics

Bad

Utils Service

Database Service

Common Service

Everything Service

---

# Database Per Service

Each service owns its own database.

Good

Auth → PostgreSQL

AI → MongoDB

Analytics → ClickHouse

Search → Qdrant

Never share database tables across services.

---

# Communication

Prefer

REST

gRPC

Events

Queues

Streams

Choose

REST

Simple request/response

gRPC

Low latency

Events

Loose coupling

Streaming

Real-time

---

# API Gateway

Responsibilities

Authentication

Rate Limiting

Routing

Load Balancing

Caching

Logging

Metrics

Never place business logic inside the gateway.

---

# Event-Driven Design

Publish events.

Examples

UserCreated

PaymentCompleted

DocumentIndexed

EmbeddingGenerated

EmailSent

Services react independently.

---

# Message Brokers

Preferred

Kafka

RabbitMQ

Redis Streams

NATS

Google Pub/Sub

AWS SQS/SNS

Choose based on reliability requirements.

---

# Synchronous Communication

Use when

Immediate response required

Authentication

Profile lookup

Configuration

Avoid long dependency chains.

---

# Asynchronous Communication

Use when

Emails

Notifications

Embeddings

OCR

Analytics

AI Evaluation

Search Indexing

Background processing improves resilience.

---

# Service Discovery

Support

DNS

Consul

Kubernetes

Eureka

Cloud discovery

Never hardcode service IPs.

---

# Resilience

Implement

Timeouts

Retries

Circuit Breakers

Bulkheads

Fallbacks

Graceful Degradation

Never assume another service is always available.

---

# Circuit Breaker

Closed

↓

Open

↓

Half Open

Protect downstream services.

---

# Retry Strategy

Retry only

Transient failures

Timeouts

Network issues

Rate limits

Do not retry validation errors.

---

# Idempotency

Every command should safely retry.

Examples

Payment

Webhook

Embedding

Notification

Avoid duplicate side effects.

---

# Data Consistency

Prefer

Eventual Consistency

Use

Saga Pattern

Outbox Pattern

Compensation

Avoid distributed transactions.

---

# Observability

Every service exports

Logs

Metrics

Traces

Health Checks

Version

Request IDs

Correlation IDs

Use OpenTelemetry.

---

# Monitoring

Track

Latency

Availability

Error Rate

Queue Length

Retry Count

CPU

Memory

Database Health

Worker Health

---

# Security

Mutual TLS

JWT

OAuth2

API Keys

Network Policies

Least Privilege

Encrypt service communication.

---

# Deployment

Deploy independently.

Version independently.

Scale independently.

Rollback independently.

Never require all services to deploy together.

---

# AI Services

Recommended split

Gateway

↓

RAG API

↓

Embedding Service

↓

Inference Service

↓

Evaluation Service

↓

Background Worker

↓

Vector Database

Allows independent scaling.

---

# Scaling

Scale only what is needed.

Examples

High AI traffic

↓

Scale AI workers

High authentication

↓

Scale auth service

Avoid scaling everything together.

---

# Testing

Test

Service Contracts

API Compatibility

Retries

Timeouts

Events

Failure Recovery

Message Ordering

Consumer Groups

---

# Local Development

Use

Docker Compose

Mock services

Seed data

Health checks

Feature flags

Develop services independently.

---

# Common Mistakes

❌ Too many services

❌ Shared database

❌ Tight coupling

❌ No monitoring

❌ No retries

❌ No health checks

❌ Chatty APIs

❌ Synchronous chains

❌ No contracts

---

# Review Checklist

□ Bounded contexts defined

□ Database per service

□ API contracts documented

□ Retries configured

□ Circuit breakers enabled

□ Events documented

□ Observability configured

□ Tests written

---

# Definition of Done

Microservice architecture is complete only if

✓ Loosely coupled

✓ Independently deployable

✓ Observable

✓ Resilient

✓ Secure

✓ Tested

✓ Scalable

✓ Production ready