# Skill

Document Ingestion

Version: 1.0

---

# Goal

Build reliable, scalable, secure, and observable document ingestion pipelines for Retrieval-Augmented Generation (RAG) systems.

Document ingestion transforms raw user documents into structured knowledge that can later be parsed, chunked, embedded, indexed, and retrieved.

Ingestion should be asynchronous, fault-tolerant, idempotent, and provider-independent.

---

# When to Load

Load this skill whenever

- Building RAG systems
- Uploading documents
- Knowledge base applications
- Enterprise search
- AI assistants
- Multi-tenant SaaS
- Document indexing
- OCR pipelines

---

# Prerequisites

- llm_basics.md
- rag/README.md

---

# Core Principle

Uploading a document is **not indexing a document**.

Document processing should always happen in background workers.

```
Upload

↓

Validate

↓

Store Original

↓

Queue Processing

↓

Parse

↓

Chunk

↓

Embed

↓

Index

↓

Ready
```

Never perform the entire pipeline inside an HTTP request.

---

# Responsibilities

The ingestion service is responsible for

- Receiving uploads
- Validating files
- Detecting MIME types
- Deduplicating documents
- Extracting metadata
- Storing originals
- Queueing background jobs
- Tracking processing status
- Recording audit logs

It is **not responsible** for parsing, embeddings, or retrieval.

---

# Architecture

```
                Client

                   │

                   ▼

          Upload API

                   │

      Validate Request

                   │

      Store Original File

                   │

      Generate Document ID

                   │

      Save Metadata

                   │

        Queue Job

                   │

        Return 202 Accepted

                   │

        Background Workers
```

The upload endpoint should return quickly.

---
# Engineering Decisions

## Synchronous Ingestion

Use when

- Small files
- Internal tools
- Low traffic

Advantages

- Simple
- Easy debugging

Trade-off

Poor scalability.

---

## Asynchronous Ingestion

Use when

- Enterprise RAG
- Large uploads
- Connectors
- Bulk imports

Recommended default.

---

## Queue-Based Processing

Use when

- High throughput
- Distributed workers
- OCR
- Large PDFs

Trade-off

Higher infrastructure complexity.

# Real-World Production Examples

## Notion AI

Processes uploaded pages asynchronously and indexes workspace content.

---

## Microsoft Copilot

Indexes Microsoft 365 documents while preserving permissions.

---

## Google Vertex AI Search

Separates ingestion from retrieval using managed indexing pipelines.

---

## Perplexity

Continuously refreshes web indexes instead of relying on static uploads.
# Document Lifecycle

```
Uploaded

↓

Queued

↓

Parsing

↓

Chunking

↓

Embedding

↓

Indexed

↓

Available

↓

Archived

↓

Deleted
```

Track every state transition.

---

# Supported Formats

Minimum support

- PDF
- DOCX
- TXT
- Markdown
- HTML
- CSV
- JSON

Optional

- PowerPoint
- Excel
- Images (OCR)
- Email (.eml)
- EPUB

Use adapters for each format.

---

# File Validation

Validate

- File size
- MIME type
- Extension
- Encoding
- Corruption
- Malware
- Password protection
- Empty files

Reject invalid uploads immediately.

---

# Security

Always

- Scan uploads
- Validate MIME types
- Limit maximum size
- Authenticate uploads
- Authorize ownership
- Encrypt storage
- Sanitize filenames

Never trust

- File extensions
- Client MIME headers
- Original filenames

---
# Observability

Track

Processing latency

↓

Failure rate

↓

Throughput

↓

Average document size

↓

Success rate

↓

Retry count

↓

Storage growth

↓

Processing cost
# Metrics

Monitor

Average Processing Time

Documents Processed

Failure Rate

Retry Rate

Average Chunk Size

Average Embedding Time

Indexing Throughput

Storage Usage

# Storage

Store

Original File

↓

Immutable Object Storage

Examples

- S3
- Azure Blob
- Google Cloud Storage
- MinIO

Never overwrite uploaded files.

---

# Naming Strategy

Avoid

resume.pdf

Good

```
tenant/document_uuid/version.pdf
```

Never depend on original filenames.

---

# Metadata

Every document should store

- Document ID
- Tenant ID
- Workspace
- Owner
- Source
- Upload Time
- File Type
- Size
- Language
- Checksum
- Version
- Processing Status
- Embedding Version
- Tags

Metadata is essential for filtering and governance.

---

# Checksums

Generate

SHA-256

or

SHA-512

Use checksums for

- Deduplication
- Integrity verification
- Version comparison

---

# Deduplication

Before processing

Compare

Checksum

↓

Already Exists?

↓

Reuse Existing

↓

Otherwise Process

Avoid embedding identical documents multiple times.

---

# Versioning

Support

Version 1

↓

Version 2

↓

Version 3

Never overwrite existing knowledge.

---

# Multi-Tenant Design

Every document belongs to

Organization

↓

Workspace

↓

User

↓

Document

Never allow cross-tenant access.

---

# Upload API

Example

```
POST /documents
```

Returns

```
202 Accepted
```

```
{
  "document_id": "...",
  "status": "queued"
}
```

Avoid synchronous indexing.

---

# Background Processing

Workers perform

Parsing

↓

Cleaning

↓

Chunking

↓

Embeddings

↓

Indexing

HTTP APIs should never block.

---

# Retry Strategy

Retry only

- Network failures
- Storage failures
- Temporary parser failures

Do not retry

- Invalid files
- Unsupported formats
- Corrupt uploads

---

# Failure Handling

Possible failures

Upload Failed

Storage Failed

Parser Failed

OCR Failed

Embedding Failed

Indexing Failed

Every failure should produce actionable logs.

---

# Idempotency

Uploading the same file twice should not produce duplicate knowledge.

Strategies

- Checksum
- Document IDs
- Version tracking

---

# Observability

Track

- Upload latency
- Queue delay
- Parse duration
- Processing duration
- Failure rate
- Retry count
- Throughput
- Storage usage

Every ingestion stage should emit metrics.

---

# Logging

Log

Upload Started

Upload Completed

Validation Failed

Queued

Processing Started

Processing Finished

Processing Failed

Never log document contents.

---

# Notifications

Optional

Notify user

When

- Processing completed
- Processing failed
- Re-index finished

Avoid polling where possible.

---

# Large Documents

Support

Chunked uploads

Resumable uploads

Streaming uploads

Multipart uploads

Avoid loading huge files entirely into memory.

---

# Batch Uploads

Support

Single

↓

Multiple

↓

Folder

↓

ZIP

↓

Cloud Connector

Design ingestion to scale horizontally.

---

# Connectors

Documents may originate from

- Google Drive
- SharePoint
- Confluence
- Notion
- GitHub
- Slack
- Dropbox
- Local Upload

Treat connectors as ingestion sources.

---

# Scheduling

Support

Manual Upload

Scheduled Sync

Webhook Trigger

Incremental Updates

Avoid full re-indexes whenever possible.

---

# Re-indexing

When

Embedding Model Changes

↓

Reprocess

↓

Re-Embed

↓

Replace Index

Version every embedding model.

---

# Compliance

Support

Retention Policies

Soft Delete

Hard Delete

Audit Logs

GDPR Delete

Enterprise systems require lifecycle management.

---

# Best Practices

- Store immutable originals.
- Use object storage.
- Queue processing.
- Validate aggressively.
- Compute checksums.
- Version everything.
- Log every stage.
- Monitor throughput.
- Design for multi-tenancy.

---

# Anti-Patterns

❌ Embedding during upload

❌ Parsing in HTTP requests

❌ Trusting file extensions

❌ No checksum

❌ No versioning

❌ Shared tenant storage

❌ Synchronous OCR

❌ Missing audit logs

❌ Silent failures

---

# Trade-offs

| Choice | Advantages | Disadvantages |
|---------|------------|---------------|
| Simpler implementation | Faster development | Lower retrieval quality |
| More metadata | Better filtering | Larger storage |
| Larger chunks | More context | Lower precision |
| Smaller chunks | Higher precision | More retrieval operations |
| Rich pipelines | Better quality | Higher latency |
# Metrics

Track

- Upload Success Rate
- Queue Time
- Parse Time
- Processing Time
- Average File Size
- Duplicate Rate
- Storage Growth
- Failure Rate

---

# Testing

Verify

- Invalid files
- Large files
- Duplicate uploads
- Concurrent uploads
- Retry logic
- Queue failures
- Multi-tenant isolation
- Malware detection
- Metadata extraction

---

# Review Checklist

□ Upload validation implemented

□ Background jobs used

□ Checksums generated

□ Metadata extracted

□ Object storage configured

□ Multi-tenancy enforced

□ Processing observable

□ Retry strategy implemented

□ Security reviewed

□ Tests written

---

# Related Skills

- parsing.md
- chunking.md
- embeddings.md
- evaluation.md
- guardrails.md

---

# Definition of Done

A document ingestion pipeline is production-ready only if

✓ Uploads are validated

✓ Originals are stored immutably

✓ Metadata is complete

✓ Checksums are generated

✓ Processing is asynchronous

✓ Multi-tenancy is enforced

✓ Retries are implemented

✓ Observability is configured

✓ Security is reviewed

✓ Tests pass

✓ Pipeline scales horizontally