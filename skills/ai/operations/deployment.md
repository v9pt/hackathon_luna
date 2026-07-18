# Deployment

Version: 1.0

---

# Goal

Deploy AI systems safely, reproducibly, and reliably across development, staging, and production environments.

Deployment encompasses far more than publishing code. It includes model serving, infrastructure provisioning, configuration management, rollout strategies, monitoring readiness, rollback capability, and operational safety.

A production deployment process should minimize downtime, maximize reproducibility, and enable rapid recovery from failures.

---

# When to Use

Deployment practices apply whenever

- launching a new AI application
- releasing a new model
- updating prompts
- deploying agent workflows
- changing infrastructure
- modifying retrieval pipelines
- introducing new tools
- scaling production services

---

# Problem

AI applications are composed of many moving parts

- frontend
- backend
- LLM providers
- vector databases
- Redis
- databases
- object storage
- observability
- authentication
- agent orchestration

Deploying them manually introduces

- configuration drift
- inconsistent environments
- downtime
- rollback difficulties
- production instability

---

# Solution

Treat deployment as an automated, reproducible engineering workflow.

Every deployment should be

- automated
- versioned
- observable
- reversible
- repeatable

---

# Core Principles

Build

↓

Test

↓

Package

↓

Deploy

↓

Validate

↓

Monitor

↓

Rollback (if necessary)

---

# Deployment Architecture

```
Developer

↓

Git

↓

CI Pipeline

↓

Tests

↓

Artifact

↓

Container Registry

↓

CD Pipeline

↓

Staging

↓

Validation

↓

Production

↓

Monitoring
```

---

# Components

## Source Control

Stores

- application code
- prompts
- infrastructure
- workflows
- configuration

Git should remain the single source of truth.

---

## Continuous Integration (CI)

Responsible for

- linting
- unit testing
- security scanning
- artifact generation

Deployment should never bypass CI.

---

## Artifact Registry

Stores immutable

- Docker images
- models
- prompt packages
- workflow bundles

Artifacts should never be rebuilt after testing.

---

## Continuous Deployment (CD)

Responsible for

- provisioning infrastructure
- deploying artifacts
- configuration updates
- rollout strategies
- validation

---

## Runtime Platform

Examples

- Kubernetes
- ECS
- Cloud Run
- Azure Container Apps
- Nomad
- Serverless Functions

Choose based on workload characteristics.

---

# Deployment Environments

## Development

Purpose

Rapid iteration.

Characteristics

- local execution
- debugging
- mock services

---

## Staging

Purpose

Production simulation.

Characteristics

- realistic traffic
- production-like infrastructure
- validation testing

---

## Production

Purpose

Serve real users.

Requirements

- monitoring
- autoscaling
- backups
- redundancy
- alerting

---

# Deployment Pipeline

Code

↓

CI

↓

Tests

↓

Security Scan

↓

Container Build

↓

Artifact Registry

↓

CD

↓

Staging

↓

Smoke Tests

↓

Production

↓

Health Verification

---

# Infrastructure as Code

Provision infrastructure using

- Terraform
- Pulumi
- AWS CDK
- Crossplane

Infrastructure should be version controlled.

---

# Configuration Management

Separate

- code
- secrets
- environment variables
- runtime configuration

Never hardcode configuration.

---

# Secrets Management

Store secrets in

- AWS Secrets Manager
- Azure Key Vault
- Google Secret Manager
- HashiCorp Vault

Never commit secrets.

---

# Model Deployment

Deploy

- model versions
- embeddings
- prompt templates
- evaluation datasets

Version every AI asset independently.

---

# Prompt Deployment

Treat prompts like code.

Every prompt should have

- version
- changelog
- owner
- evaluation history

---

# Agent Deployment

Deploy

- workflow graphs
- routing rules
- tool registries
- memory configuration
- safety policies

Avoid changing production agents without validation.

---

# Database Migrations

Apply

Schema Migration

↓

Validation

↓

Application Deployment

↓

Cleanup

Prefer backward-compatible migrations.

---

# Deployment Strategies

## Recreate

Old version stops.

New version starts.

Simple but causes downtime.

---

## Rolling Deployment

Replace instances gradually.

Recommended default.

---

## Blue–Green Deployment

Two identical environments.

Switch traffic instantly.

Excellent rollback capability.

---

## Canary Deployment

Deploy to a small percentage of users first.

Increase traffic gradually.

Recommended for AI systems.

---

## Shadow Deployment

Run new version alongside production without serving users.

Compare outputs before release.

Ideal for model upgrades.

---

# Health Checks

Validate

- API availability
- database connectivity
- vector database
- Redis
- model access
- tool registry
- workflow engine

Health checks should block unhealthy deployments.

---

# Validation

Verify

- latency
- accuracy
- evaluation metrics
- error rate
- cost
- safety policies

Deployment is incomplete until validation succeeds.

---

# Rollback

Rollback should restore

- code
- prompts
- models
- workflows
- infrastructure

Rollback should require one action.

---

# Multi-Region Deployment

Deploy across

Region A

+

Region B

+

Region C

Support regional failover.

---

# Edge Deployment

Useful for

- low latency
- privacy
- offline inference
- regional compliance

---

# Engineering Decisions

## Container-Based Deployment

Recommended default.

Portable and reproducible.

---

## Kubernetes

Recommended for large-scale AI systems.

Supports autoscaling, service discovery, and rolling updates.

---

## Serverless

Useful for

- lightweight APIs
- intermittent workloads

Higher cold-start latency.

---

## Hybrid Deployment

Mix

- serverless
- containers
- GPUs
- batch workers

Recommended for enterprise AI.

---

# Runtime Architecture

```
Users

↓

Load Balancer

↓

API Gateway

↓

AI Service

↓

Redis

↓

Database

↓

Vector DB

↓

LLM Provider

↓

Monitoring

↓

Alerting
```

---

# Performance

Optimize

deployment frequency

↓

deployment duration

↓

rollback speed

↓

startup latency

↓

container size

↓

GPU utilization

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Rolling | No downtime | Slower rollout |
| Blue–Green | Instant rollback | Higher infrastructure cost |
| Canary | Low deployment risk | Operational complexity |
| Shadow | Excellent validation | Double compute cost |
| Serverless | Minimal operations | Cold starts |

---

# Common Failures

- configuration drift
- failed migrations
- missing secrets
- incompatible model versions
- unhealthy containers
- broken workflows
- partial rollouts

---

# Best Practices

- Automate deployments.
- Version every AI asset.
- Use immutable artifacts.
- Validate before promotion.
- Deploy gradually.
- Monitor immediately after release.
- Make rollbacks trivial.
- Test disaster recovery regularly.

---

# Anti-Patterns

❌ Manual production deployments

❌ Deploying without monitoring

❌ Hardcoded secrets

❌ Mutable production environments

❌ Rebuilding artifacts after testing

❌ Skipping staging

❌ No rollback strategy

---

# Real-World Examples

## OpenAI

Deploys new models through staged rollouts, extensive evaluations, traffic gating, monitoring, and rollback capabilities before broad availability.

---

## Anthropic

Uses gradual releases, continuous safety evaluation, infrastructure monitoring, and operational controls to introduce new Claude model versions with minimal disruption.

---

## GitHub Copilot

Deploys backend services, model routing logic, and prompt updates independently while monitoring latency, acceptance rates, and error metrics.

---

## LangSmith Deployments

Supports versioned prompts, evaluation workflows, experiment tracking, and deployment validation before production rollout.

---

## Enterprise AI Platforms

Deploy APIs, agent workflows, vector databases, retrieval pipelines, and observability infrastructure through Infrastructure as Code and CI/CD automation.

---

# Related Skills

- monitoring.md
- observability.md
- scaling.md
- reliability.md
- rollbacks.md
- security_operations.md

---

# Definition of Done

An AI deployment process is production-ready only if

✓ Infrastructure is provisioned through code

✓ All AI assets are versioned independently

✓ CI validates code, prompts, and workflows before deployment

✓ CD automates promotion across environments

✓ Deployments use safe rollout strategies such as rolling or canary releases

✓ Health checks block unhealthy releases

✓ Monitoring begins immediately after deployment

✓ Rollbacks restore the complete production state with minimal downtime

✓ Secrets and configuration are managed securely outside application code

✓ The deployment process is reproducible, observable, automated, and recoverable