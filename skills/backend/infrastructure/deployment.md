# Skill

Deployment Engineering

Version: 1.0

---

# Goal

Deploy backend applications safely, consistently, and repeatably across development, staging, and production.

Deployment is an engineering process.

Not a manual task.

Every deployment should be reproducible.

---

# Deployment Philosophy

Code

↓

Build

↓

Test

↓

Package

↓

Scan

↓

Deploy

↓

Monitor

↓

Rollback (if required)

Never deploy directly from your local machine.

---

# Environments

Always separate

Development

↓

Testing

↓

Staging

↓

Production

Each environment should have

Separate Database

Separate Secrets

Separate Storage

Separate Cache

Separate Monitoring

Never share production resources.

---

# Configuration

Use

Environment Variables

Secret Managers

Configuration Files

Never hardcode

Passwords

API Keys

Database URLs

JWT Secrets

Cloud Credentials

---

# Environment Variables

Typical variables

APP_ENV

PORT

DATABASE_URL

REDIS_URL

MONGO_URI

JWT_SECRET

OPENAI_API_KEY

GEMINI_API_KEY

LOG_LEVEL

CORS_ORIGINS

---

# Secrets

Store using

GitHub Secrets

AWS Secrets Manager

Azure Key Vault

Google Secret Manager

Docker Secrets

Hashicorp Vault

Never store secrets in Git.

---

# CI/CD Pipeline

Recommended workflow

Code Push

↓

Lint

↓

Type Check

↓

Unit Tests

↓

Integration Tests

↓

Security Scan

↓

Build Docker Image

↓

Push Registry

↓

Deploy

↓

Smoke Tests

↓

Production

Every deployment should be automated.

---

# Branch Strategy

main

Production

develop

Integration

feature/*

Feature branches

hotfix/*

Production fixes

release/*

Release preparation

Never develop directly on main.

---

# Versioning

Follow Semantic Versioning

Major.Minor.Patch

Example

1.4.2

Tag releases in Git.

Never deploy anonymous builds.

---

# Database Migrations

Deployment order

Backup

↓

Migration

↓

Deploy API

↓

Health Check

↓

Traffic

Never modify schemas manually.

Always support rollback.

---

# Docker

Every deployment should use

Pinned image versions

Health checks

Non-root user

Resource limits

Multi-stage builds

---

# Reverse Proxy

Recommended

Nginx

Traefik

Cloud Load Balancer

Responsibilities

HTTPS

Compression

Rate Limiting

Routing

Caching

Headers

---

# HTTPS

Always use HTTPS.

Enable

TLS 1.2+

HSTS

Secure Cookies

Redirect HTTP → HTTPS

---

# Scaling

Support

Horizontal Scaling

Stateless APIs

Redis Sessions

External File Storage

Load Balancers

Never rely on local filesystem.

---

# Health Checks

Expose

/health

/ready

/live

Health checks should verify

Database

Redis

External APIs (optional)

Configuration

---

# Rollback Strategy

Every deployment must support rollback.

Rollback if

Critical Errors

Database Failure

Health Check Failure

High Error Rate

Performance Regression

Never deploy without a rollback plan.

---

# Zero Downtime

Prefer

Blue/Green Deployment

Rolling Deployment

Canary Deployment

Avoid downtime during updates.

---

# Logging

Deployment logs should include

Version

Environment

Build Number

Commit SHA

Deployment Time

Operator

Never log secrets.

---

# Monitoring

Track

CPU

Memory

Disk

Latency

500 Errors

Queue Length

Database Connections

Redis

External APIs

LLM Usage

---

# Alerts

Notify on

Deployment Failure

Health Check Failure

High Error Rate

Database Down

Redis Down

Memory Exhaustion

Queue Backlog

SSL Expiration

---

# Backup

Backup before

Schema Changes

Major Releases

Infrastructure Changes

Test restore procedures regularly.

---

# Infrastructure as Code

Prefer

Terraform

Pulumi

AWS CDK

Bicep

CloudFormation

Avoid manual infrastructure changes.

---

# Cloud Providers

Common platforms

AWS

Azure

Google Cloud

Railway

Render

Fly.io

DigitalOcean

Vercel (Frontend)

Backend deployments should remain cloud-agnostic where possible.

---

# AI Deployments

Separate

API

Worker

LLM Gateway

Redis

Vector Database

Embedding Pipeline

Background Jobs

Do not run all AI services in a single container.

---

# Release Checklist

Before deployment

□ Tests passing

□ Lint passing

□ Type checks passing

□ Security scan passing

□ Docker image built

□ Secrets configured

□ Database migration reviewed

□ Monitoring enabled

□ Alerts configured

□ Rollback verified

---

# Post Deployment Validation

Verify

Health endpoints

Authentication

Database connectivity

Redis connectivity

Background jobs

External APIs

LLM providers

Critical user flows

Error rate

Latency

---

# Common Mistakes

❌ Deploying from local machine

❌ Manual database changes

❌ Hardcoded secrets

❌ No rollback

❌ No health checks

❌ No monitoring

❌ No backups

❌ Deploying untested code

---

# Review Checklist

□ CI/CD configured

□ Version tagged

□ Health checks

□ Monitoring enabled

□ Rollback available

□ Secrets externalized

□ Logs available

□ Deployment documented

---

# Definition of Done

Deployment is complete only if

✓ Automated

✓ Versioned

✓ Secure

✓ Monitored

✓ Rollback supported

✓ Zero-downtime capable

✓ Production ready