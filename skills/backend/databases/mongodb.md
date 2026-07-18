# Skill

MongoDB Engineering

Version: 1.0

---

# Goal

Design scalable, maintainable, and performant MongoDB databases suitable for production AI applications.

MongoDB is a document database.

Do not use it like a SQL database.

Do not use it as a dumping ground for arbitrary JSON.

---

# Design Philosophy

Design documents around

Access Patterns

↓

Business Requirements

↓

Performance

↓

Scalability

Never model data first.

Model queries first.

---

# Preferred Stack

MongoDB 7+

Motor (Async)

PyMongo

Pydantic

FastAPI

Docker

Mongo Express (Development)

---

# Collection Design

Collections represent

Entities

Examples

users

messages

conversations

documents

embeddings

workflows

tasks

logs

Avoid creating dozens of tiny collections.

---

# Document Design

A document should represent one logical object.

Good

Conversation

↓

Messages

↓

Metadata

Avoid

Massive deeply nested objects

Huge arrays

Duplicate information

---

# Embedding vs Referencing

Embed when

Small

Read together

Rarely updated

Example

Address

Settings

Preferences

Reference when

Large

Shared

Frequently updated

Many-to-many

Example

Users

Organizations

Projects

Permissions

---

# Document Size

MongoDB Limit

16 MB

Never approach this limit.

Split data before reaching it.

Especially

Chat History

AI Context

Logs

File Metadata

---

# IDs

Use

ObjectId

or UUID

Never expose internal IDs directly without validation.

---

# Validation

Always validate with

Pydantic

Mongo Schema Validation

FastAPI Request Models

Never trust client payloads.

---

# Indexing

Always index

email

username

conversation_id

user_id

created_at

updated_at

organization_id

status

Frequently searched fields

Review indexes regularly.

Unused indexes waste memory.

---

# Compound Indexes

Prefer

(user_id, created_at)

(status, updated_at)

(organization_id, role)

Design indexes around real queries.

---

# TTL Indexes

Use for

OTP

Sessions

Temporary Tokens

Cache

Logs

AI Temporary State

Never manually delete expiring data.

---

# Query Rules

Always

Limit()

Project()

Sort()

Paginate()

Avoid

Collection scans

Regex without indexes

Loading unnecessary fields

---

# Aggregation

Use aggregation for

Analytics

Dashboards

Statistics

Grouping

Filtering

Summaries

Avoid multiple database calls when one pipeline is sufficient.

---

# Pagination

Prefer

Cursor Pagination

Avoid

skip() on very large datasets.

---

# Relationships

MongoDB has no joins by default.

Use

Embedding

or

References

Never over-normalize.

Never over-denormalize.

---

# Transactions

Use transactions only when required.

Examples

Financial operations

Multiple collections

Inventory

Authentication

Avoid unnecessary transactions.

---

# AI Data

Ideal for

Conversation History

Prompt History

Context Memory

Embeddings Metadata

Agent State

Retrieval Metadata

Workflow Logs

Tool Execution History

Do not store vectors directly unless using MongoDB Vector Search.

---

# Vector Search

Prefer

MongoDB Atlas Vector Search

Store

Embeddings

Metadata

Source

Chunk IDs

Document IDs

Distance Metric

---

# File Metadata

Store

Filename

Mime Type

Owner

Size

Hash

Created Date

Storage Location

Do not store large binary files inside MongoDB.

Use

S3

Cloud Storage

GridFS (only if necessary)

---

# Security

Authentication enabled

Role-based users

TLS

Least privilege

Network restrictions

Never expose MongoDB publicly.

---

# Connection Management

Reuse clients.

Singleton connection.

Never create a new MongoClient per request.

---

# Performance

Monitor

Slow queries

Collection scans

Index usage

Memory

Connections

Aggregation cost

Use explain() before optimizing.

---

# Backup Strategy

Daily backup

Point-in-time recovery

Replica Set

Restore testing

---

# Testing

Test

CRUD

Indexes

Validation

Aggregation

Transactions

Pagination

Performance

Security

---

# Common Mistakes

❌ Huge documents

❌ No indexes

❌ Creating MongoClient repeatedly

❌ Collection scans

❌ Storing files directly

❌ Duplicating excessive data

❌ Ignoring validation

❌ skip() on millions of records

---

# AI Best Practices

Separate

Conversation

↓

Messages

↓

Embeddings

↓

Documents

↓

Users

↓

Agent State

Avoid putting an entire chatbot into one document.

---

# Review Checklist

□ Collections designed

□ Access patterns identified

□ Indexes created

□ Validation enabled

□ Pagination implemented

□ Aggregation reviewed

□ Security configured

□ Tests written

□ Performance reviewed

---

# Definition of Done

✓ Collections designed

✓ Indexed

✓ Validated

✓ Secure

✓ Tested

✓ Scalable

✓ Production ready