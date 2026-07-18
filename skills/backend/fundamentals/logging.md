# Skill

Backend Logging & Observability Engineering

Version: 1.0

---

# Goal

Design backend systems that are observable, debuggable, and measurable through structured logging, tracing, and monitoring.

Logs should answer

What happened?

When?

Where?

Why?

For whom?

Never use logging only for debugging.

Logging is an operational tool.

---

# Observability Pillars

Logs

↓

Metrics

↓

Traces

Together they provide complete system visibility.

---

# Logging Principles

Logs must be

Structured

Consistent

Searchable

Actionable

Timestamped

Never log random text.

---

# Log Levels

DEBUG

Development details

INFO

Normal application events

WARNING

Unexpected but recoverable

ERROR

Request failed

CRITICAL

System failure

Never log everything as INFO.

---

# Structured Logging

Prefer JSON logs.

Good

{
  "timestamp": "...",
  "level": "INFO",
  "request_id": "...",
  "user_id": "...",
  "service": "auth",
  "message": "User authenticated"
}

Avoid

print("login success")

---

# Required Log Fields

Timestamp

Level

Service

Environment

Request ID

Correlation ID

User ID (if available)

HTTP Method

Endpoint

Status Code

Duration

Error Code

Message

---

# Request Logging

Log

Method

Path

Client IP

Duration

Status Code

Request ID

Authenticated User

Never log request bodies containing sensitive information.

---

# Response Logging

Log

Status

Response Time

Response Size

Request ID

Errors

Do not log entire responses unless debugging.

---

# Error Logging

Always include

Exception Type

Message

Stack Trace

Context

Request ID

Service

Never swallow exceptions silently.

---

# Correlation IDs

Every request must have

Request ID

Example

X-Request-ID

Every downstream service should propagate it.

This enables distributed tracing.

---

# AI Logging

Track

Model Used

Prompt Version

Latency

Tokens

Cost

Retries

Fallback Model

Tool Calls

Retrieval Time

Do not log prompts containing sensitive user data.

---

# Authentication Logging

Log

Login Success

Login Failure

Password Reset

MFA Events

Token Refresh

Logout

Permission Denied

Never log

Passwords

Tokens

Refresh Tokens

Secrets

---

# Database Logging

Monitor

Slow Queries

Connection Errors

Deadlocks

Timeouts

Migration Events

Avoid logging full SQL with sensitive values.

---

# External API Logging

Log

Provider

Endpoint

Latency

Retries

Status

Timeouts

Failures

Useful for

LLMs

Payment APIs

Email APIs

Storage

---

# Background Jobs

Log

Job ID

Queue

Worker

Retries

Execution Time

Failures

Completion

---

# Performance Logging

Measure

API Latency

Database Time

External API Time

Cache Hit Ratio

Memory Usage

CPU Usage

Queue Time

---

# Security Events

Always log

Failed Login

Rate Limit

Permission Denied

Suspicious Activity

Role Changes

Admin Actions

Secret Rotation

---

# Privacy

Never log

Passwords

Credit Cards

JWT

API Keys

Cookies

OAuth Tokens

PII unless absolutely necessary

Mask sensitive values.

---

# Retention

Development

7 Days

Staging

14 Days

Production

30–180 Days

Follow legal and compliance requirements.

---

# Log Aggregation

Recommended

Grafana Loki

ELK Stack

OpenSearch

Datadog

Splunk

Cloud Logging

Centralize logs.

Never rely on local files.

---

# Metrics

Track

Requests/sec

Latency

Error Rate

CPU

Memory

DB Connections

Cache Hit Rate

Queue Size

LLM Usage

---

# Tracing

Use

OpenTelemetry

Jaeger

Tempo

AWS X-Ray

Trace

Request

↓

API

↓

Database

↓

Redis

↓

External APIs

↓

Response

---

# Alerts

Notify on

500 Error Spike

Latency Spike

Worker Failure

Database Down

Redis Down

Memory High

Queue Backlog

Authentication Abuse

---

# Common Mistakes

❌ Using print()

❌ Logging secrets

❌ No request IDs

❌ Inconsistent formats

❌ Missing timestamps

❌ Excessive logging

❌ Ignoring log rotation

❌ No monitoring

---

# Testing

Verify

Logs generated

Levels correct

Sensitive data masked

Correlation IDs propagated

Errors logged

Alerts triggered

---

# Review Checklist

□ Structured logging

□ Request IDs

□ Correlation IDs

□ Error logs complete

□ Sensitive data masked

□ Metrics exported

□ Tracing enabled

□ Alerts configured

□ Retention defined

---

# Definition of Done

✓ Structured logs

✓ Correlation IDs

✓ Metrics available

✓ Traces available

✓ Security compliant

✓ Production ready