# Backend Engineering Skill Library

Version: 1.0

---

# Purpose

This directory contains reusable engineering knowledge for designing, building, testing, deploying, and operating production-grade backend systems.

Each document represents a focused engineering capability.

Load only the skills relevant to the current task instead of loading the entire library.

---

# Engineering Philosophy

Backend systems should be

Reliable

Secure

Scalable

Observable

Maintainable

Testable

Production Ready

Every implementation should follow the Engineering Constitution and Shared Rules before applying these skills.

---

# Skill Categories

## Fundamentals

Core engineering principles that should be applied to almost every backend task.

security.md

testing.md

logging.md

performance.md

---

## Frameworks

Framework-specific implementation knowledge.

fastapi.md

Future

express.md

nestjs.md

springboot.md

django.md

---

## Databases

Database design, optimization, and persistence.

postgresql.md

mongodb.md

redis.md

---

## Infrastructure

Deployment and runtime environment.

docker.md

deployment.md

---

## Architecture

Higher-level backend patterns.

background_jobs.md

websockets.md

rag_api.md

microservices.md

---

## Cross-Cutting

authentication.md

Applies to almost every backend application.

---

# Skill Routing Guide

This section determines which skills should be loaded for different engineering tasks.

---

## Building a CRUD API

Load

authentication

security

fastapi

postgresql or mongodb

testing

logging

performance

---

## Authentication System

Load

authentication

security

fastapi

redis

testing

logging

deployment

---

## AI Chatbot Backend

Load

fastapi

mongodb

redis

rag_api

background_jobs

websockets

logging

performance

deployment

---

## RAG Application

Load

rag_api

mongodb or postgresql

redis

background_jobs

fastapi

logging

performance

testing

deployment

---

## File Upload Service

Load

fastapi

security

background_jobs

logging

performance

testing

---

## Notification Service

Load

background_jobs

redis

fastapi

logging

deployment

---

## WebSocket Application

Load

websockets

redis

fastapi

logging

performance

testing

---

## Background Worker

Load

background_jobs

redis

logging

performance

deployment

---

## Analytics API

Load

postgresql

performance

logging

testing

deployment

---

## High Traffic API

Load

performance

redis

logging

docker

deployment

testing

---

## Multi-Service System

Load

microservices

docker

deployment

logging

performance

authentication

---

# Recommended Engineering Workflow

Every backend task should follow this sequence.

Understand Requirements

↓

Select Required Skills

↓

Design Architecture

↓

Implement Feature

↓

Secure Implementation

↓

Write Tests

↓

Measure Performance

↓

Add Logging

↓

Deploy

↓

Monitor

Never skip engineering steps.

---

# Decision Matrix

Need authentication?

↓

authentication.md

Need FastAPI?

↓

fastapi.md

Need PostgreSQL?

↓

postgresql.md

Need MongoDB?

↓

mongodb.md

Need Redis?

↓

redis.md

Need Docker?

↓

docker.md

Need Deployment?

↓

deployment.md

Need Async Workers?

↓

background_jobs.md

Need Live Updates?

↓

websockets.md

Need AI Retrieval?

↓

rag_api.md

Need Distributed Architecture?

↓

microservices.md

Need Performance Optimization?

↓

performance.md

Need Security?

↓

security.md

Need Testing?

↓

testing.md

Need Observability?

↓

logging.md

---

# Skill Dependencies

authentication

↓

security

↓

fastapi

↓

database

↓

logging

↓

testing

↓

performance

↓

docker

↓

deployment

Higher-level architecture skills build on these foundations.

---

# Engineering Standards

Every backend implementation must

Validate all inputs

Handle errors gracefully

Protect sensitive data

Log important events

Support monitoring

Be testable

Be type-safe

Use dependency injection

Avoid duplicated logic

Separate business logic from transport logic

Follow SOLID principles where appropriate

---

# Backend Technology Stack

Preferred Framework

FastAPI

Preferred Databases

PostgreSQL

MongoDB

Redis

Preferred Container Platform

Docker

Preferred Queue

Redis

Arq

Celery

Preferred Testing

pytest

httpx

Preferred Observability

OpenTelemetry

Structured Logging

Prometheus

Grafana

---

# Definition of Done

A backend feature is complete only if

✓ Requirements implemented

✓ Security reviewed

✓ Authentication applied (if required)

✓ Database optimized

✓ Tests passing

✓ Logging added

✓ Performance reviewed

✓ Docker compatible

✓ Deployment ready

✓ Documentation updated

---

# Future Skills

The backend library is expected to expand with

GraphQL

gRPC

Kafka

RabbitMQ

ElasticSearch

ClickHouse

Kubernetes

Terraform

Serverless

Feature Flags

API Gateway

Service Mesh

Workflow Engines

Event Sourcing

CQRS

---

# Maintenance

Update skills whenever

A better engineering pattern is adopted

A framework changes significantly

A security recommendation changes

A new production incident reveals a better approach

Deprecated practices should be removed rather than accumulated.

---

# Objective

This library exists to help engineers consistently build production-grade backend systems using proven engineering practices instead of ad hoc solutions.