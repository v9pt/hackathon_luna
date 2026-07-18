# Skill

Backend Security Engineering

Version: 1.0

---

# Goal

Design backend systems that are secure by default.

Security is not a feature.

Security is a requirement.

Every API, database, background job and AI endpoint must follow these rules.

---

# Security Principles

Always follow

Least Privilege

↓

Defense in Depth

↓

Fail Secure

↓

Zero Trust

↓

Input Validation

↓

Output Encoding

↓

Audit Logging

Never trust

User Input

Headers

Cookies

JWT Claims

Query Parameters

Uploaded Files

Third-party APIs

AI Outputs

Everything is considered untrusted.

---

# Authentication

Supported

JWT

OAuth2

Session

API Keys

Passkeys

Magic Links

Always

Expire tokens

Rotate refresh tokens

Hash passwords

Invalidate revoked sessions

Never

Store plaintext passwords

Store JWTs inside localStorage unless explicitly required

Reuse refresh tokens forever

---

# Authorization

Authentication != Authorization

Authentication

Who are you?

Authorization

Can you perform this action?

Always check ownership.

Never trust frontend role checks.

Implement middleware or policy-based authorization.

Support

RBAC

ABAC

Ownership

Organization-based permissions

---

# Password Storage

Preferred

Argon2id

Fallback

bcrypt (cost 12+)

Never use

MD5

SHA1

SHA256

Base64

Plain text

Passwords must never be recoverable.

---

# Environment Variables

Secrets belong only inside

.env

Vault

Secret Manager

Kubernetes Secrets

Never commit

API Keys

JWT Secrets

Database Passwords

Private Keys

OAuth Secrets

SMTP Passwords

OpenAI Keys

Gemini Keys

Mongo URI

---

# Input Validation

Validate

Body

Headers

Cookies

Params

Query

Files

AI Tool Inputs

Prefer

Pydantic

Zod

Joi

Class Validator

Reject unknown fields unless explicitly allowed.

---

# SQL Injection

Always

Parameterized Queries

ORM

Prepared Statements

Never

String concatenation

Dynamic SQL

Unsafe interpolation

Bad

SELECT * FROM users WHERE id = ${id}

Good

SELECT * FROM users WHERE id = ?

---

# NoSQL Injection

Never trust Mongo queries.

Whitelist operators.

Reject

$where

$regex (unsafe)

$ne

$gt

when not expected.

---

# XSS

Escape HTML.

Sanitize Markdown.

Never trust user-generated HTML.

Enable CSP.

Avoid dangerouslySetInnerHTML.

---

# CSRF

If using cookies

Enable

SameSite

CSRF Token

Origin Validation

Secure Cookies

HttpOnly

---

# CORS

Never use

*

in production.

Whitelist origins.

Allow only required methods.

Allow only required headers.

---

# Rate Limiting

Protect

Login

Register

Password Reset

OTP

AI Endpoints

File Upload

Search

Webhook

Recommended

5 requests/minute (auth)

60 requests/minute (API)

Use Redis if possible.

---

# File Upload Security

Validate

Extension

Mime Type

Magic Bytes

File Size

Virus Scan Hook

Random Filename

Never trust filenames.

Store outside web root.

---

# API Security

Every endpoint must define

Authentication

Authorization

Validation

Rate Limit

Audit Logging

Errors

Version

Never expose admin endpoints publicly.

---

# Logging

Log

Authentication

Failures

Permission Denied

Token Refresh

Password Reset

Critical Actions

Never log

Passwords

Tokens

Secrets

Cookies

PII

---

# Error Messages

Users should see

"Invalid credentials."

Never

"Password incorrect."

Never reveal

Email exists

Username exists

Internal errors

Database schema

Stack traces

---

# HTTP Headers

Enable

Content-Security-Policy

X-Frame-Options

Referrer-Policy

Permissions-Policy

X-Content-Type-Options

Strict-Transport-Security

---

# Encryption

HTTPS only.

TLS 1.2+

Encrypt

Sensitive files

Tokens at rest

Backups

Secrets

---

# AI Security

Validate prompts.

Detect prompt injection.

Limit tool access.

Never expose system prompts.

Never allow unrestricted filesystem access.

Never execute AI-generated code without review.

---

# Webhooks

Verify signatures.

Reject expired timestamps.

Prevent replay attacks.

---

# JWT

Short-lived Access Token

15 minutes

Refresh Token

7-30 days

Rotate refresh tokens.

Blacklist revoked refresh tokens.

Never put sensitive data inside JWT payload.

---

# Database

Least privilege database user.

Indexes.

Encrypted backups.

Connection pooling.

Parameterized queries.

No root accounts.

---

# Docker

Run as non-root.

Read-only filesystem where possible.

Minimal base images.

Pin versions.

Scan images.

---

# Monitoring

Alert on

Failed Logins

500 Errors

Rate Limit Abuse

Privilege Escalation

Database Failures

Large AI Usage

---

# Security Review Checklist

□ Authentication implemented

□ Authorization implemented

□ Validation complete

□ Rate limiting enabled

□ Password hashing correct

□ Secrets externalized

□ SQL injection protected

□ XSS protected

□ CSRF protected

□ CORS configured

□ File uploads secured

□ Logs sanitized

□ HTTPS enforced

□ Security headers enabled

□ Error messages safe

□ JWT rotation implemented

□ Tests written

---

# Common Vulnerabilities

Always review against

OWASP Top 10

Broken Access Control

Cryptographic Failures

Injection

Insecure Design

Security Misconfiguration

Vulnerable Components

Authentication Failures

Integrity Failures

Logging Failures

SSRF

---

# Definition of Done

Security work is complete only if

✓ OWASP reviewed

✓ Secrets externalized

✓ Validation complete

✓ Authorization complete

✓ Logs sanitized

✓ Tests pass

✓ Security review passes