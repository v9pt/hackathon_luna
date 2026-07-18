# Skill

Document Chunking

Version: 1.0

---

# Goal

Split documents into semantically meaningful, retrievable chunks while preserving context, maximizing retrieval quality, and minimizing hallucinations.

Chunking is the most important preprocessing step in Retrieval-Augmented Generation.

Poor chunking cannot be fixed by better embeddings or larger LLMs.

---

# When to Load

Load this skill whenever

- Building RAG
- Enterprise Search
- AI Chatbots
- Semantic Search
- Document QA
- Knowledge Bases

---

# Prerequisites

- ingestion.md
- parsing.md

---

# Core Principle

Never split text by characters alone.

Split by meaning.

Bad chunking destroys context.

Good chunking preserves meaning.

---
# Engineering Decisions

## Fixed-Length Chunking

Use when

Simple documentation

Small projects

Trade-off

Breaks semantic boundaries.

---

## Recursive Chunking

Recommended default.

Balances semantic structure and chunk size.

---

## Semantic Chunking

Use when

Research

Enterprise search

Long-form documentation

Trade-off

Higher embedding cost.

---

## Parent-Child Chunking

Use when

Large documents

Manuals

Books

Best for hierarchical retrieval.
# Real-World Production Examples

## LangChain

Uses RecursiveCharacterTextSplitter as the default splitter.

---

## LlamaIndex

Supports hierarchical chunking and node relationships.

---

## Anthropic Context Engineering

Emphasizes semantic coherence over fixed token counts.

---

## Enterprise Knowledge Bases

Often combine parent-child chunking with metadata filters.

# Chunking Pipeline

```
Parsed Document

↓

Clean Text

↓

Identify Structure

↓

Split Logically

↓

Apply Token Limits

↓

Add Overlap

↓

Generate Metadata

↓

Ready for Embeddings
```

---

# What Makes a Good Chunk?

Every chunk should

Represent one idea

Contain sufficient context

Be independently understandable

Remain within token limits

Avoid duplication

Support semantic retrieval

---

# Chunking Objectives

Maximize

Semantic coherence

↓

Retrieval precision

↓

Context quality

↓

Embedding quality

↓

Generation quality

Never optimize only for chunk size.

---

# Chunk Characteristics

A chunk should

Contain

One topic

One concept

One procedure

One API

One section

Avoid mixing unrelated topics.

---

# Chunk Size

General recommendation

300–800 tokens

Smaller

Extraction

Classification

Larger

Technical documentation

Research papers

Books

Tune based on evaluation.

---

# Chunk Overlap

Overlap preserves context.

Typical overlap

50–150 tokens

Without overlap

Information may be lost.

Too much overlap

Creates duplicate retrieval.

---

# Example

Without overlap

Chunk A

"The deployment requires Docker."

Chunk B

"Kubernetes should be configured..."

The relationship is lost.

With overlap

Chunk A

"...Docker."

Chunk B

"Docker.
Kubernetes should be configured..."

Context remains.

---

# Fixed Size Chunking

Split by

Characters

Words

Tokens

Advantages

Simple

Fast

Predictable

Disadvantages

Breaks semantics

Poor retrieval

Use only as a fallback.

---

# Recursive Chunking

Preferred default.

Algorithm

Large Section

↓

Paragraph

↓

Sentence

↓

Phrase

↓

Token Limit

Maintains natural boundaries.

---

# Semantic Chunking

Split based on meaning.

Examples

Topic changes

Heading changes

Concept changes

Advantages

Best retrieval quality

Disadvantages

More computation

Preferred for production.

---

# Hierarchical Chunking

Structure

Document

↓

Chapter

↓

Section

↓

Subsection

↓

Paragraph

↓

Chunk

Preserves hierarchy.

Useful for enterprise search.

---

# Parent-Child Chunking

Store

Parent

↓

Child

Retrieve

Child

↓

Expand

↓

Parent

Useful for

Large documents

Policies

Manuals

Books

---

# Sliding Window Chunking

Window

↓

Move

↓

Overlap

↓

Repeat

Useful for

Sequential information

Logs

Conversations

Books

---

# Markdown-Aware Chunking

Respect

#

##

###

Lists

Tables

Code blocks

Never split inside headings.

---

# HTML Chunking

Preserve

Heading hierarchy

Paragraphs

Lists

Tables

Sections

Ignore navigation bars.

---

# Code Chunking

Split

File

↓

Class

↓

Function

↓

Method

↓

Block

Never split inside a function.

---

# API Documentation

Chunk by

Endpoint

↓

Request

↓

Response

↓

Examples

↓

Errors

Avoid mixing endpoints.

---

# Table Chunking

Small tables

Keep together.

Large tables

Split by logical sections.

Preserve

Headers

Rows

Relationships

---

# Conversation Chunking

Messages

↓

Turns

↓

Topics

↓

Sessions

Avoid splitting user/assistant pairs.

---

# Metadata

Every chunk should include

Document ID

Chunk ID

Parent ID

Section

Page

Heading

Language

Source

Embedding Version

Timestamp

Metadata improves retrieval.

---

# Chunk IDs

Every chunk requires

Stable

Unique

Immutable

identifier.

Never regenerate IDs unnecessarily.

---

# Language Awareness

Chunk according to language rules.

Chinese

Japanese

Arabic

Hindi

English

Different languages require different tokenization.

---

# Multi-Modal Chunking

Support

Text

Images

Tables

Captions

OCR

Code

Treat each modality appropriately.

---

# Token Awareness

Always chunk using tokenizer length.

Do not estimate by characters.

Different models tokenize differently.

---

# Adaptive Chunking

Adjust chunk size based on

Document type

Language

Heading depth

Paragraph length

Target model

Adaptive chunking often outperforms static chunk sizes.

---

# Chunk Quality

Good chunks

Independent

Focused

Context-rich

Small enough

Large enough

Bad chunks

Random

Mixed topics

Incomplete

Tiny

Massive

---

# Evaluation

Measure

Retrieval Accuracy

Precision@K

Recall@K

MRR

Context Recall

Faithfulness

Chunk size should be determined by evaluation.

---

# Observability

Track

Chunks per document

Average size

Overlap

Retrieval success

Embedding latency

Chunk failures

---

# Best Practices

- Prefer semantic chunking.
- Preserve headings.
- Preserve tables.
- Preserve code blocks.
- Use token-aware splitting.
- Include overlap.
- Generate metadata.
- Evaluate continuously.
- Version chunking strategy.

---

# Anti-Patterns

❌ Splitting by characters

❌ No overlap

❌ Huge chunks

❌ Tiny chunks

❌ Mixing topics

❌ Losing headings

❌ Breaking code blocks

❌ Ignoring tables

❌ No metadata

---

# Metrics

Track

- Average Chunk Size
- Overlap Size
- Chunks per Document
- Retrieval Precision
- Recall@K
- MRR
- Context Recall
- Hallucination Rate

---

# Testing

Verify

- Large documents
- Small documents
- Code repositories
- PDFs
- HTML
- Markdown
- Tables
- Images
- OCR output

---

# Review Checklist

□ Semantic chunking used

□ Token-aware splitting

□ Overlap configured

□ Metadata generated

□ Headings preserved

□ Tables preserved

□ Code preserved

□ Chunk IDs generated

□ Strategy versioned

□ Retrieval evaluated

---

# Related Skills

- parsing.md
- embeddings.md
- retrieval.md
- reranking.md
- prompt_builder.md

---
# Trade-offs

| Choice | Advantages | Disadvantages |
|---------|------------|---------------|
| Simpler implementation | Faster development | Lower retrieval quality |
| More metadata | Better filtering | Larger storage |
| Larger chunks | More context | Lower precision |
| Smaller chunks | Higher precision | More retrieval operations |
| Rich pipelines | Better quality | Higher latency |

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

# Definition of Done

A chunking strategy is production-ready only if

✓ Chunks are semantically coherent

✓ Token-aware splitting is used

✓ Overlap preserves context

✓ Metadata is attached

✓ Structure is preserved

✓ Chunk IDs are stable

✓ Strategy is versioned

✓ Retrieval quality is measured

✓ Evaluation validates chunk size

✓ Pipeline scales to large document collections