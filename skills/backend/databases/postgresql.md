# Skill

PostgreSQL Engineering

Version: 1.0

---

# Goal

Design scalable, normalized, performant PostgreSQL databases suitable for production.

Never treat PostgreSQL as just "storage."

It is an application component.

---

# Design Philosophy

Good schema

↓

Good indexes

↓

Good queries

↓

Good performance

Never optimize SQL before designing data correctly.

---

# Preferred Stack

PostgreSQL 16+

SQLAlchemy Async

Alembic

asyncpg

Pydantic

Docker

---

# Schema Design

Prefer

Normalized tables

Foreign keys

Unique constraints

Indexes

NOT NULL

CHECK constraints

Avoid

Duplicate data

Huge JSON columns

Unbounded TEXT everywhere

Nullable fields without reason

---

# Naming Convention

Tables

snake_case

users

orders

chat_messages

Columns

created_at

updated_at

user_id

Never abbreviate.

---

# Primary Keys

Prefer

UUID

or BIGSERIAL

Never expose sequential IDs publicly if enumeration is a concern.

---

# Relationships

Support

One-to-One

One-to-Many

Many-to-Many

Always define

ON DELETE behavior

Indexes

Constraints

---

# Migrations

Always use

Alembic

Never edit production tables manually.

Every schema change requires

Migration

Rollback strategy

Documentation

---

# Indexing

Index

Foreign Keys

Search columns

JOIN columns

Sorting columns

Frequently filtered columns

Avoid over-indexing.

Indexes improve reads but slow writes.

---

# Query Rules

Prefer

SELECT explicit columns

LIMIT

OFFSET or Cursor Pagination

Parameterized Queries

Avoid

SELECT *

N+1 queries

Unbounded scans

Dynamic SQL

---

# Transactions

Use transactions for

Payments

Authentication

Inventory

Multi-table writes

Money movement

Never leave partial writes.

---

# Constraints

Always use

PRIMARY KEY

FOREIGN KEY

UNIQUE

CHECK

NOT NULL

Let PostgreSQL enforce correctness.

---

# Pagination

Prefer Cursor Pagination

Fallback

LIMIT/OFFSET

Never return entire tables.

---

# Soft Deletes

Preferred

deleted_at timestamp

Instead of hard delete when auditability matters.

---

# Full Text Search

Prefer

GIN Index

tsvector

tsquery

Before introducing Elasticsearch.

---

# JSON

Use JSONB only for

Flexible metadata

AI responses

Configuration

Do not replace relational modeling with JSONB.

---

# Performance

Monitor

Slow queries

Locks

Connection pool

Index usage

Execution plans

Use EXPLAIN ANALYZE before optimizing.

---

# Connection Pooling

Use

PgBouncer

or SQLAlchemy Pool

Never create a new DB connection per request.

---

# Security

Least privilege DB users

Parameterized queries

Encrypted connections

No root access

Rotate credentials

---

# Backup Strategy

Daily backups

Point-in-time recovery

Restore testing

Backup verification

---

# Testing

Test

CRUD

Constraints

Transactions

Indexes

Rollback

Migration

Performance

---

# Common Mistakes

❌ SELECT *

❌ Missing indexes

❌ String concatenation SQL

❌ Huge transactions

❌ Duplicate data

❌ Missing foreign keys

❌ No migrations

---

# Review Checklist

□ Schema normalized

□ Indexes reviewed

□ Constraints added

□ Queries parameterized

□ Transactions used

□ Alembic migration created

□ Tests written

□ Performance reviewed

---

# Definition of Done

✓ Normalized schema

✓ Indexed

✓ Secure

✓ Tested

✓ Migration included

✓ Production ready