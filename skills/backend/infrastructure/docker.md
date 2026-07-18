# Skill

Docker Engineering

Version: 1.0

---

# Goal

Package applications into secure, reproducible, portable containers that can run consistently across development, testing, and production.

Containers should be

Portable

Small

Secure

Observable

Fast

Never build Docker images only for local development.

Build production-ready images first.

---

# Design Philosophy

Source Code

↓

Dockerfile

↓

Docker Image

↓

Container

↓

Docker Compose

↓

Deployment

A container should contain one primary responsibility.

---

# Preferred Stack

Docker 27+

Docker Compose V2

BuildKit

Multi-stage Builds

Docker Scout

Trivy

---

# Image Selection

Prefer official images.

Examples

python:3.12-slim

node:22-alpine

postgres:16

redis:7

mongo:7

Avoid

latest

Unmaintained images

Huge base images

---

# Dockerfile Principles

Keep images

Small

Deterministic

Repeatable

Secure

Always

Pin versions

Use .dockerignore

Reduce layers

Remove unnecessary files

Never copy secrets.

---

# Multi-stage Builds

Use

Builder Stage

↓

Production Stage

Builder installs dependencies.

Production contains only runtime artifacts.

Benefits

Smaller images

Better security

Faster deployments

---

# Layer Optimization

Copy dependency files first.

Example

requirements.txt

package.json

poetry.lock

Then install dependencies.

Copy source code last.

Maximize layer caching.

---

# Python Containers

Use

python:3.12-slim

Create virtual environment if required.

Disable .pyc generation.

Enable unbuffered output.

Prefer

uv

or

pip with pinned versions.

---

# Node Containers

Install dependencies before source.

Use npm ci.

Avoid npm install in production.

Build separately.

Copy only build artifacts.

---

# Environment Variables

Store configuration in

.env

Secrets Manager

Docker Secrets

Never hardcode

API Keys

Passwords

JWT Secrets

Database URLs

---

# Secrets

Use

Docker Secrets

Vault

Cloud Secret Manager

Never bake secrets into images.

Never commit .env files.

---

# Non-root User

Always run containers as non-root.

Example

appuser

Avoid running as root.

---

# File System

Use read-only filesystem when possible.

Mount writable volumes only where required.

Limit permissions.

---

# Volumes

Use for

Database storage

Uploads

Logs

Configuration

Never store persistent data inside containers.

Containers are ephemeral.

---

# Networking

Use custom bridge networks.

Communicate via service names.

Example

backend

postgres

redis

mongo

Avoid exposing unnecessary ports.

---

# Docker Compose

Separate services.

Example

frontend

backend

postgres

redis

mongo

nginx

worker

Keep compose files readable.

---

# Health Checks

Every service should define

Health Check

Readiness

Liveness

Example

/health

Docker should restart unhealthy containers.

---

# Logging

Write logs to stdout/stderr.

Do not write application logs into container files.

Use centralized logging.

---

# Security

Run as non-root

Minimal base image

Pinned versions

No secrets

Read-only filesystem

Drop Linux capabilities

Enable image scanning

---

# Image Scanning

Scan images using

Trivy

Docker Scout

Grype

Resolve

Critical

High

Medium vulnerabilities before release.

---

# Resource Limits

Define

CPU

Memory

Restart Policy

Health Checks

Avoid unlimited containers.

---

# Build Performance

Enable BuildKit.

Cache dependencies.

Minimize COPY operations.

Remove unused packages.

---

# CI/CD

Pipeline

Lint

↓

Tests

↓

Build Image

↓

Security Scan

↓

Push Registry

↓

Deploy

Never deploy untested images.

---

# Registry

Use

Docker Hub

GitHub Container Registry

AWS ECR

Azure ACR

Google Artifact Registry

Version images.

Example

backend:1.0.0

backend:latest

backend:dev

---

# Container Lifecycle

Container starts

↓

Health Check

↓

Ready

↓

Serve Requests

↓

Graceful Shutdown

↓

Cleanup

Always handle SIGTERM.

---

# AI Workloads

Separate

API

Worker

Vector DB

Redis

LLM Gateway

Do not combine everything into one container.

---

# Monitoring

Track

CPU

Memory

Restarts

Health Status

Image Version

Disk Usage

Network Usage

Container Count

---

# Common Mistakes

❌ Using latest tag

❌ Running as root

❌ Huge images

❌ Secrets inside images

❌ No .dockerignore

❌ No health checks

❌ Multiple unrelated processes

❌ Writing persistent data inside containers

---

# Recommended Project Structure

Dockerfile

docker-compose.yml

docker-compose.dev.yml

.dockerignore

.env.example

scripts/

deploy/

---

# Testing

Verify

Image builds

Container starts

Health checks pass

Dependencies connect

Volumes mount

Environment loads

Graceful shutdown

---

# Review Checklist

□ Multi-stage build

□ Small base image

□ Non-root user

□ Health checks

□ Secrets externalized

□ Volumes configured

□ Resource limits

□ Image scanned

□ Tests pass

---

# Definition of Done

✓ Image optimized

✓ Secure

✓ Small

✓ Health checks enabled

✓ Deployable

✓ Tested

✓ Production ready