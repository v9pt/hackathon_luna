# Skill

Backend Testing Engineering

Version: 1.0

---

# Goal

Build backend systems that are provably correct through automated testing.

Testing is not optional.

Every production feature must be testable.

---

# Testing Philosophy

Never test implementation.

Test behavior.

Good tests survive refactoring.

Bad tests fail after harmless code changes.

Write tests that describe expected outcomes.

---

# Testing Pyramid

Always prioritize

Unit Tests

↓

Integration Tests

↓

End-to-End Tests

Avoid relying only on E2E tests.

---

# Coverage Goal

Target

90%+

Critical modules

95%+

Authentication

Payments

AI

Permissions

Background Jobs

---

# Test Structure

Follow

Arrange

Act

Assert

Example

Arrange

Create user

↓

Act

Call endpoint

↓

Assert

Verify response

Verify database

Verify side effects

---

# Unit Tests

Test

Services

Utilities

Validators

Repositories (mocked)

AI Prompt Builders

Permissions

Business Rules

Never depend on databases.

Never depend on APIs.

Never depend on the internet.

---

# Integration Tests

Test

API

Database

Authentication

Middleware

Caching

Repositories

Dependency Injection

Real interactions.

Mock external services only.

---

# End-to-End Tests

Verify

Authentication

User Flow

Complete API

Database

Background Jobs

File Uploads

Use sparingly.

---

# API Testing

Every endpoint should test

Success

Validation Errors

Authentication Failure

Authorization Failure

404

409

422

500

Rate Limits

Timeouts

Large Payloads

---

# Validation Testing

Verify

Missing Fields

Wrong Types

Invalid UUID

Invalid Email

Empty String

Long String

Boundary Values

Enums

Unexpected Fields

---

# Authentication Testing

Verify

Invalid Password

Expired JWT

Malformed JWT

Revoked JWT

Missing JWT

Wrong Role

Refresh Token

Logout

Password Reset

Email Verification

---

# Authorization Testing

Check

Guest

User

Admin

Owner

Organization

Never assume authorization works.

---

# Repository Testing

Test

Create

Read

Update

Delete

Transactions

Indexes

Relationships

Constraints

---

# AI Testing

Test

Prompt Formatting

Structured Output

Fallback Models

Retries

Tool Calls

RAG Retrieval

Context Size

Hallucination Detection

Token Limits

Latency

Never trust AI outputs.

---

# Error Testing

Verify

Database Offline

Redis Offline

External API Failure

Timeout

Invalid Configuration

Missing Environment Variables

Unexpected Exceptions

---

# Performance Testing

Measure

Latency

Memory

CPU

Concurrent Requests

Database Queries

Response Time

Cold Start

---

# Load Testing

Scenarios

100 Users

500 Users

1000 Users

Burst Traffic

Slow Database

Slow AI Provider

---

# Security Testing

Verify

SQL Injection

NoSQL Injection

XSS

CSRF

SSRF

Command Injection

Rate Limits

JWT Tampering

Privilege Escalation

Prompt Injection

---

# Mocking

Mock

External APIs

Payments

Email

SMS

LLM Providers

Storage

Never mock

Business Logic

Validation

Permissions

---

# Fixtures

Use fixtures for

Users

Admin

JWT

Database

Products

Files

Organizations

Keep fixtures reusable.

---

# Naming

Good

test_create_user_success()

test_login_invalid_password()

test_admin_can_delete_user()

Bad

test1()

test_login2()

run_test()

---

# Assertions

Always verify

Status Code

Response Body

Database State

Logs (if required)

Events

Background Jobs

Side Effects

Never assert only the status code.

---

# Common Mistakes

❌ Testing implementation

❌ No edge cases

❌ Huge test files

❌ Duplicate fixtures

❌ Shared mutable state

❌ Hidden dependencies

❌ Network calls

❌ Random failures

---

# Test Folder

tests/

    unit/

    integration/

    api/

    ai/

    performance/

    security/

    fixtures/

    helpers/

---

# Pytest

Prefer

Fixtures

Parametrize

Markers

Factories

Avoid

Global State

Shared Variables

Sleep()

---

# Continuous Testing

Every Pull Request should

Run Unit Tests

↓

Run Integration Tests

↓

Run Security Checks

↓

Run Coverage

↓

Run Lint

↓

Run Type Check

↓

Deploy

Never merge without passing tests.

---

# Review Checklist

□ Happy Path

□ Edge Cases

□ Invalid Input

□ Authentication

□ Authorization

□ Error Handling

□ Database State

□ Background Tasks

□ Logging

□ AI Output Validation

□ Security

□ Performance

---

# Definition of Done

Testing is complete only if

✓ Unit Tests Pass

✓ Integration Tests Pass

✓ Coverage Target Achieved

✓ Security Tests Pass

✓ Performance Acceptable

✓ Edge Cases Covered

✓ CI Passes