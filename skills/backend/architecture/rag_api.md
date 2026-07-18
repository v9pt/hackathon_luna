# Skill

Production RAG API Engineering

Version: 1.0

---

# Goal

Build scalable, secure, observable Retrieval-Augmented Generation (RAG) APIs that provide accurate, low-latency, context-aware responses.

RAG is a pipeline.

Not a single API endpoint.

Every stage should be independently testable and replaceable.

---

# High-Level Architecture

                Upload
                   │
                   ▼
          Document Ingestion
                   │
                   ▼
          Parsing / Extraction
                   │
                   ▼
              Chunking
                   │
                   ▼
          Embedding Generation
                   │
                   ▼
           Vector Database
                   │
                   ▼
               Retrieval
                   │
                   ▼
          Context Assembly
                   │
                   ▼
              Prompt Builder
                   │
                   ▼
               LLM Provider
                   │
                   ▼
         Response Formatter
                   │
                   ▼
            Streaming Client

Every stage should be isolated.

---

# Service Architecture

api/

services/

repositories/

retrievers/

embeddings/

chunkers/

prompts/

providers/

evaluators/

workers/

Never put retrieval logic inside API routes.

---

# API Endpoints

POST /documents/upload

POST /documents/index

DELETE /documents/{id}

POST /chat

POST /retrieve

GET /documents

GET /documents/{id}

GET /health

---

# Pipeline

1.

Receive document

↓

2.

Validate

↓

3.

Extract text

↓

4.

Normalize

↓

5.

Chunk

↓

6.

Generate embeddings

↓

7.

Store metadata

↓

8.

Store vectors

↓

9.

Ready for retrieval

Never skip validation.

---

# Document Parsing

Support

PDF

DOCX

TXT

Markdown

HTML

CSV

JSON

Images (OCR)

Validate

Encoding

Size

Mime Type

Language

---

# Chunking

Preferred

Semantic Chunking

Fallback

Recursive Character Splitter

Avoid

Huge chunks

Tiny chunks

Typical

300–800 tokens

Overlap

50–100 tokens

Optimize based on retrieval quality.

---

# Embeddings

Separate

Embedding Service

↓

Provider

↓

Model

↓

Vector Store

Never call embedding APIs directly from routes.

---

# Embedding Providers

Support abstraction for

OpenAI

Gemini

Voyage

Jina

Cohere

Sentence Transformers

Ollama

Swappable providers.

---

# Metadata

Every chunk stores

Document ID

Chunk ID

Source

Page

Title

Owner

Organization

Timestamp

Embedding Version

Language

Tags

Metadata improves filtering.

---

# Vector Database

Support

Pinecone

Qdrant

Weaviate

Milvus

MongoDB Atlas Vector

pgvector

Abstract the implementation.

---

# Retrieval

Support

Top-K

Hybrid Search

Metadata Filtering

MMR

Similarity Threshold

Query Expansion

Multi-query Retrieval

---

# Retrieval Flow

User Query

↓

Embedding

↓

Vector Search

↓

Metadata Filter

↓

Re-ranking

↓

Context Assembly

↓

Prompt Builder

Never send raw retrieval results directly to the LLM.

---

# Prompt Builder

Separate prompt construction.

System Prompt

↓

Retrieved Context

↓

Conversation Memory

↓

User Question

↓

Output Instructions

Never concatenate strings inside routes.

---

# Conversation Memory

Support

Short-term Memory

Long-term Memory

Session Memory

Summary Memory

Window Memory

Separate memory from retrieval.

---

# Caching

Cache

Embeddings

Search Results

Prompt Templates

LLM Responses

Metadata

Frequently used queries

Use Redis.

---

# Streaming

Support

Server-Sent Events

WebSockets

Chunked Responses

Never wait for the complete LLM response.

---

# AI Providers

Abstract

OpenAI

Gemini

Claude

Groq

DeepSeek

Ollama

Mistral

Avoid provider lock-in.

---

# Error Handling

Handle

Embedding Failure

Vector DB Failure

Timeout

Rate Limit

No Context Found

Provider Failure

Malformed Prompt

Retry transient failures only.

---

# Security

Authenticate

Authorize

Rate Limit

Validate uploads

Validate prompts

Protect against prompt injection

Sanitize retrieved content

Never expose internal prompts.

---

# Multi-Tenant Support

Every query should support

Organization

Workspace

User

Project

Never retrieve another tenant's documents.

---

# Background Jobs

Use workers for

Parsing

OCR

Chunking

Embeddings

Re-indexing

Cleanup

Do not block HTTP requests.

---

# Observability

Track

Retrieval Latency

Embedding Latency

LLM Latency

Token Usage

Cost

Chunk Count

Retrieval Quality

Hallucination Rate

Prompt Version

---

# Evaluation

Measure

Precision@K

Recall@K

MRR

Latency

Cost

Faithfulness

Answer Relevance

Context Recall

Track quality continuously.

---

# Logging

Log

Document Indexed

Chunks Created

Embedding Model

Vector Store

Provider

Latency

Failures

Never log confidential documents.

---

# Testing

Verify

Upload

Chunking

Embeddings

Retrieval

Filtering

Prompt Assembly

Streaming

Provider Fallback

Rate Limits

Multi-tenancy

---

# Common Mistakes

❌ Huge chunks

❌ No overlap

❌ No metadata

❌ Retrieval inside routes

❌ Provider lock-in

❌ No caching

❌ Blocking indexing

❌ Ignoring prompt injection

❌ No evaluation

---

# Review Checklist

□ Modular pipeline

□ Chunking reviewed

□ Metadata stored

□ Embeddings abstracted

□ Vector DB abstracted

□ Retrieval optimized

□ Prompt builder separated

□ Streaming enabled

□ Security implemented

□ Evaluation metrics tracked

□ Tests written

---

# Definition of Done

✓ Upload pipeline complete

✓ Chunking optimized

✓ Retrieval accurate

✓ Streaming enabled

✓ Provider abstraction implemented

✓ Evaluation included

✓ Secure

✓ Production ready