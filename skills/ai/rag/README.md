# RAG Engineering Skill Library

Version: 1.0

---

# Purpose

This library contains reusable engineering knowledge for building production-grade Retrieval-Augmented Generation (RAG) systems.

RAG is not a single API endpoint.

It is a distributed pipeline that combines document processing, information retrieval, prompt engineering, and LLM inference to generate accurate, context-aware responses.

Each skill in this directory focuses on one stage of the pipeline.

Load only the skills required for the current task.

---

# Engineering Philosophy

Production RAG systems should be

Reliable

Scalable

Observable

Secure

Provider Agnostic

Cost Efficient

Low Latency

Highly Accurate

Continuously Evaluated

Every stage should be independently testable and replaceable.

---

# RAG Pipeline

```
User Upload
      │
      ▼
Document Ingestion
      │
      ▼
Parsing
      │
      ▼
Cleaning & Normalization
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
      │
      ▼
Vector Storage
      │
      ▼
Retrieval
      │
      ▼
Re-ranking
      │
      ▼
Prompt Construction
      │
      ▼
LLM Generation
      │
      ▼
Evaluation
      │
      ▼
Streaming Response
```

Never combine multiple stages into a single service.

---

# Skill Overview

## Document Processing

Responsible for transforming raw files into searchable knowledge.

- ingestion.md
- parsing.md
- chunking.md

---

## Knowledge Representation

Transforms text into searchable vectors.

- embeddings.md
- vector_databases.md

---

## Information Retrieval

Finds the most relevant context.

- retrieval.md
- hybrid_search.md
- reranking.md

---

## Context Construction

Builds high-quality prompts for the language model.

- prompt_builder.md

---

## Memory

Maintains conversation context.

- memory.md

---

## Evaluation

Measures quality continuously.

- evaluation.md

---

## Safety

Protects against hallucinations and prompt injection.

- guardrails.md

---

## User Experience

Delivers responses efficiently.

- streaming.md

---

# Learning Order

Follow this order when learning RAG engineering.

```
Ingestion

↓

Parsing

↓

Chunking

↓

Embeddings

↓

Vector Databases

↓

Retrieval

↓

Hybrid Search

↓

Re-ranking

↓

Prompt Builder

↓

Memory

↓

Evaluation

↓

Guardrails

↓

Streaming
```

Each concept builds upon the previous one.

---

# Skill Routing Guide

## Build a Document Chatbot

Load

- ingestion
- parsing
- chunking
- embeddings
- retrieval
- prompt_builder

---

## Enterprise Knowledge Base

Load

- ingestion
- parsing
- chunking
- vector_databases
- retrieval
- hybrid_search
- reranking
- evaluation

---

## AI Research Assistant

Load

- retrieval
- prompt_builder
- memory
- evaluation
- guardrails

---

## Multi-Tenant SaaS

Load

- ingestion
- vector_databases
- retrieval
- guardrails
- evaluation

---

## Large Document Search

Load

- parsing
- chunking
- embeddings
- hybrid_search
- reranking

---

## Conversational RAG

Load

- retrieval
- prompt_builder
- memory
- streaming

---

# Engineering Workflow

Every RAG feature should follow this sequence.

```
Understand Documents

↓

Design Pipeline

↓

Implement Ingestion

↓

Parse Documents

↓

Chunk Content

↓

Generate Embeddings

↓

Store Vectors

↓

Retrieve Context

↓

Re-rank Results

↓

Construct Prompt

↓

Generate Response

↓

Evaluate Quality

↓

Deploy

↓

Monitor

↓

Continuously Improve
```

Never optimize prompts before retrieval quality.

---

# Design Principles

## Separation of Concerns

Each stage should own exactly one responsibility.

Never combine

- Parsing
- Embedding
- Retrieval
- Prompt Construction

inside the same module.

---

## Provider Independence

Support multiple

Embedding Models

LLM Providers

Vector Databases

Avoid vendor lock-in.

---

## Retrieval First

Good retrieval is more valuable than larger language models.

Improve

Chunking

Metadata

Filtering

Re-ranking

before changing LLMs.

---

## Metadata Matters

Every chunk should contain metadata.

Examples

- Document ID
- Chunk ID
- Page
- Source
- Language
- Owner
- Workspace
- Timestamp
- Embedding Version
- Tags

Metadata enables filtering and traceability.

---

## Evaluation First

Every RAG system should measure

Retrieval Quality

Answer Relevance

Faithfulness

Latency

Cost

Hallucination Rate

Evaluation is mandatory.

---

# Recommended Technology

## Parsing

- PyMuPDF
- Unstructured
- pdfplumber
- Apache Tika

---

## OCR

- Tesseract
- PaddleOCR

---

## Embeddings

- OpenAI
- Voyage AI
- Jina AI
- BAAI
- Ollama

---

## Vector Databases

- Qdrant
- pgvector
- Pinecone
- Weaviate
- Milvus

---

## Retrieval

- Dense Search
- Hybrid Search
- Metadata Filtering
- MMR
- Re-ranking

---

## Evaluation

- Ragas
- DeepEval
- LangSmith

---

# Skill Dependencies

```
Ingestion

↓

Parsing

↓

Chunking

↓

Embeddings

↓

Vector Database

↓

Retrieval

↓

Hybrid Search

↓

Re-ranking

↓

Prompt Builder

↓

Memory

↓

Evaluation

↓

Guardrails

↓

Streaming
```

Later skills assume mastery of earlier stages.

---

# Engineering Standards

Every RAG implementation should

Separate every pipeline stage

Version embeddings

Track metadata

Support provider abstraction

Measure retrieval quality

Log latency

Protect against prompt injection

Support streaming

Support background processing

Be fully testable

---

# Common Mistakes

❌ Sending entire documents to the LLM

❌ Huge chunks

❌ No overlap

❌ No metadata

❌ Poor retrieval

❌ No re-ranking

❌ Prompt concatenation

❌ No evaluation

❌ Blind trust in LLM output

❌ Provider lock-in

---

# Definition of Done

A RAG system is production-ready only if

✓ Documents are validated

✓ Parsing is reliable

✓ Chunking is optimized

✓ Embeddings are versioned

✓ Retrieval is accurate

✓ Re-ranking improves relevance

✓ Prompt construction is modular

✓ Memory is managed

✓ Evaluation is continuous

✓ Guardrails are implemented

✓ Streaming is supported

✓ Observability is configured

---

# Future Skills

This library can be expanded with

- Graph RAG
- Agentic RAG
- Knowledge Graphs
- Multi-Modal RAG
- Adaptive Retrieval
- Semantic Caching
- Federated Search
- Long Context Optimization
- Citation Generation
- Query Planning

---

# Objective

This library exists to help engineers build reliable, scalable, secure, and production-ready Retrieval-Augmented Generation systems using modular engineering practices instead of monolithic AI pipelines.