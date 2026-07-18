# Skill

FastAPI Engineering

Version: 1.0

---

# Goal

Build production-ready FastAPI applications that are scalable, modular, secure, observable, and easy to maintain.

Never build a "main.py" application containing all business logic.

---

# Design Philosophy

FastAPI should act as the transport layer.

Business logic should never live inside routes.

Routes should remain thin.

Services should contain business logic.

Repositories should handle persistence.

Schemas should validate data.

---

# Preferred Architecture

```

app/
│
├── api/
│ ├── v1/
│ │ ├── auth.py
│ │ ├── users.py
│ │ ├── ai.py
│ │ └── health.py
│
├── services/
│
├── repositories/
│
├── models/
│
├── schemas/
│
├── middleware/
│
├── dependencies/
│
├── core/
│
├── utils/
│
├── db/
│
├── workers/
│
├── tests/
│
└── main.py

```

---

# Folder Responsibilities

api/

Receive requests only.

Never contain business logic.

---

services/

Business logic.

Validation.

Transactions.

AI orchestration.

External APIs.

---

repositories/

Database only.

CRUD.

Queries.

Aggregation.

No business logic.

---

schemas/

Pydantic models.

Validation.

Serialization.

Response models.

---

models/

ORM models.

Database entities.

Relationships.

Indexes.

---

middleware/

Authentication.

Logging.

Rate Limiting.

Request IDs.

CORS.

---

core/

Settings.

Configuration.

Security.

Constants.

---

utils/

Small reusable helpers.

No business logic.

---

# Dependency Injection

Always use Depends()

Never instantiate services inside routes.

Good

```

@router.get("/users")
async def get_users(
service: UserService = Depends(get_user_service)
):

```

Bad

```

service = UserService()

```

---

# Async

Prefer async everywhere.

Use

async def

await

Async DB drivers

httpx.AsyncClient

Motor

SQLAlchemy Async

Never block the event loop.

Avoid

requests

time.sleep()

blocking file operations

---

# Pydantic

Always create

Request Models

Response Models

Internal Models

Example

```

CreateUserRequest

CreateUserResponse

UserDTO

```

Never return ORM models directly.

---

# Validation

Validate

Email

Password

UUID

Dates

Enums

Ranges

Strings

Lists

Never trust incoming data.

---

# Response Format

Prefer consistent responses.

```

{
"success": true,
"data": {},
"message": "User created"
}

```

Errors

```

{
"success": false,
"error": {
"code": "USER_NOT_FOUND",
"message": "User not found"
}
}

```

---

# Exception Handling

Create

Global Exception Handler

Validation Handler

Database Handler

Authentication Handler

Never repeat try/except inside every endpoint.

---

# Authentication

Support

JWT

OAuth2

API Keys

Bearer Tokens

Refresh Tokens

Use middleware or dependencies.

---

# Database

Prefer

SQLAlchemy Async

or

Motor

Never write SQL inside routes.

Always use repositories.

---

# AI Endpoints

Separate AI logic.

Example

```

AIService

↓

PromptBuilder

↓

Retriever

↓

LLMProvider

↓

ResponseFormatter

```

Never call OpenAI or Gemini directly inside routes.

---

# Background Tasks

Use

BackgroundTasks

Celery

RQ

Arq

For

Emails

AI jobs

PDFs

Exports

Never block HTTP requests.

---

# Middleware

Recommended

Logging

Authentication

CORS

Request ID

Compression

Rate Limiting

Timing

---

# Health Checks

Always include

/health

/ready

/live

Useful for Docker and Kubernetes.

---

# Pagination

Never return massive datasets.

Support

limit

offset

cursor

sorting

filtering

---

# Versioning

Use

/api/v1

/api/v2

Never break old clients.

---

# File Upload

Validate

Mime Type

Extension

Size

Store outside application root.

Generate random filenames.

---

# Configuration

Use

BaseSettings

Environment Variables

.env

Never hardcode

URLs

Keys

Secrets

Ports

---

# Logging

Log

Requests

Responses

Latency

Errors

External APIs

AI Calls

Never log secrets.

---

# Testing

Use

pytest

httpx

TestClient

Cover

Success

Validation

Errors

Authentication

Authorization

Edge Cases

---

# Docker

Use

python:3.12-slim

Multi-stage builds

Non-root user

Health check

Pinned dependencies

---

# Performance

Use

Connection Pooling

Redis Cache

Pagination

Compression

Async

Background Tasks

Indexes

Measure before optimizing.

---

# Common Mistakes

❌ Business logic inside routes

❌ Blocking code

❌ Returning ORM models

❌ Missing validation

❌ Missing response models

❌ Global mutable state

❌ Hardcoded secrets

❌ Missing async

❌ Huge main.py

---

# FastAPI Checklist

□ Thin routes

□ Service layer

□ Repository layer

□ Pydantic validation

□ Dependency injection

□ Async everywhere

□ Error handlers

□ Logging

□ JWT auth

□ Health checks

□ Tests

□ Docker support

□ Swagger documented

□ Production ready

---

# Definition of Done

FastAPI implementation is complete only if

✓ Modular

✓ Async

✓ Typed

✓ Secure

✓ Tested

✓ Documented

✓ Dockerized

✓ Scalable

✓ Observable