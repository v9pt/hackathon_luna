# Skill

Document Parsing

Version: 1.0

---

# Goal

Extract clean, structured, semantically meaningful information from raw documents while preserving the original document's logical structure.

Parsing transforms raw files into normalized text suitable for chunking and embedding.

Poor parsing leads to poor retrieval, poor context, and hallucinations.

---

# When to Load

Load this skill whenever

- Building RAG systems
- Enterprise Search
- AI Knowledge Bases
- OCR Pipelines
- Document Intelligence
- Semantic Search
- Search Indexing

---

# Prerequisites

- ingestion.md

---

# Core Principle

Documents are more than plain text.

They contain

Titles

↓

Headings

↓

Paragraphs

↓

Lists

↓

Tables

↓

Images

↓

Captions

↓

Footnotes

↓

Code Blocks

↓

Metadata

Every parser should preserve document structure.

---

# Parsing Pipeline

```
Document

↓

Detect Format

↓

Extract Content

↓

Extract Metadata

↓

Preserve Layout

↓

Normalize Text

↓

Remove Noise

↓

Semantic Cleanup

↓

Structured Output
```

---

# Responsibilities

A parser should

- Detect file format
- Extract readable text
- Preserve hierarchy
- Extract metadata
- Detect language
- Preserve formatting
- Remove boilerplate
- Handle encoding issues
- Prepare for chunking

A parser should **not**

- Generate embeddings
- Chunk documents
- Retrieve information

---

# Architecture

```
Upload

↓

Parser Router

↓

PDF Parser

DOCX Parser

HTML Parser

Markdown Parser

OCR Parser

↓

Normalizer

↓

Structured Document
```

Use specialized parsers instead of one generic parser.

---
# Engineering Decisions

## Native PDF Parsing

Use when

Digital PDFs.

Fastest option.

---

## OCR Parsing

Use when

Scanned PDFs

Invoices

Images

Trade-off

Higher latency.

---

## Layout-Aware Parsing

Use when

Research papers

Financial reports

Manuals

Recommended for enterprise RAG.

---

## Markdown Conversion

Use when

Developer documentation

Knowledge bases

API docs

Produces high-quality chunks.
# Real-World Production Examples

## GitHub Copilot

Parses repositories while preserving directory structure.

---

## ChatGPT File Uploads

Parses PDFs, spreadsheets, presentations and text before retrieval.

---

## Adobe PDF Services

Preserves layout, tables and reading order during extraction.

---

## Unstructured.io

Routes documents through specialized parsers depending on file type.

# Supported Formats

Minimum

- PDF
- DOCX
- TXT
- Markdown
- HTML
- CSV
- JSON

Advanced

- PPTX
- XLSX
- EPUB
- XML
- Email
- Images

---

# PDF Parsing

Preserve

- Page order
- Headings
- Paragraphs
- Lists
- Tables
- Images
- Captions
- References

Avoid extracting pages as one giant block.

---

# OCR

OCR is required for

- Scanned PDFs
- Photos
- Receipts
- Contracts
- Whiteboards
- Handwritten notes (where supported)

Preferred

- PaddleOCR
- Tesseract
- Azure OCR
- Google Vision
- AWS Textract

---

# Layout Preservation

Maintain

Document

↓

Sections

↓

Subsections

↓

Paragraphs

↓

Lists

↓

Tables

↓

Figures

↓

Footnotes

Never flatten everything into plain text.

---

# Table Extraction

Tables should remain tables.

Avoid

```
Name Age City
John 20 Delhi
```

Prefer

```
| Name | Age | City |
|------|-----|------|
| John | 20 | Delhi |
```

or structured JSON.

---

# Code Blocks

Preserve

Programming Language

↓

Indentation

↓

Formatting

↓

Line Breaks

Never destroy code formatting.

---

# Images

Extract

- Alt text
- Captions
- Figure Numbers
- OCR Text (optional)

Images should become metadata.

---

# Hyperlinks

Preserve

Anchor Text

↓

URL

↓

Context

Useful for enterprise search.

---

# Metadata Extraction

Extract

Title

Author

Creation Date

Modified Date

Language

Pages

Keywords

File Type

Source

Document ID

Store separately from text.

---

# Language Detection

Automatically detect

English

Hindi

Arabic

Chinese

French

Spanish

...

Store language metadata for filtering.

---

# Encoding

Normalize

UTF-8

Remove invalid characters.

Handle

- BOM
- Unicode normalization
- Mixed encodings

---

# Text Normalization

Normalize

Whitespace

↓

Quotes

↓

Hyphens

↓

Bullet Styles

↓

Line Breaks

↓

Unicode

Preserve semantics.

---

# Boilerplate Removal

Remove

Headers

Footers

Page Numbers

Repeated Watermarks

Navigation Bars

Cookie Banners

Advertisements

Keep only meaningful content.

---

# Duplicate Removal

Detect repeated

Headers

Footers

Repeated paragraphs

Duplicate pages

Do not index duplicates.

---

# Semantic Cleaning

Remove

Empty paragraphs

Broken words

Repeated punctuation

Control characters

Invisible characters

Fix

Sentence boundaries

Whitespace

Formatting

---

# Structured Output

Parser output should resemble

```
Document

Sections

Paragraphs

Tables

Figures

Metadata
```

Not one giant string.

---

# Parser Selection

PDF

↓

PDF Parser

DOCX

↓

DOCX Parser

Image

↓

OCR

HTML

↓

HTML Parser

Markdown

↓

Markdown Parser

Use adapters.

---

# Error Handling

Handle

Encrypted PDFs

Corrupt Files

Missing Fonts

Broken Encoding

Malformed HTML

OCR Failures

Unsupported Formats

Never silently fail.

---

# Observability

Track

Parse Time

Characters Extracted

Pages Parsed

OCR Usage

Failures

Warnings

Document Size

---
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

# Logging

Log

Parser Used

Processing Time

Warnings

Fallback Parser

Failures

Never log document contents.

---

# Performance

Avoid

Loading huge files into RAM.

Prefer

Streaming

Incremental parsing

Parallel page parsing

Caching

---
# Trade-offs

| Choice | Advantages | Disadvantages |
|---------|------------|---------------|
| Simpler implementation | Faster development | Lower retrieval quality |
| More metadata | Better filtering | Larger storage |
| Larger chunks | More context | Lower precision |
| Smaller chunks | Higher precision | More retrieval operations |
| Rich pipelines | Better quality | Higher latency |
# Security

Validate

- File Type
- Embedded Scripts
- Macros
- Active Content

Never execute document content.

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
# Best Practices

- Preserve hierarchy.
- Preserve tables.
- Preserve code blocks.
- Normalize text.
- Remove boilerplate.
- Store metadata.
- Detect language.
- Support OCR.
- Modular parser design.

---

# Anti-Patterns

❌ One parser for every format

❌ Flattening layout

❌ Losing headings

❌ Removing tables

❌ Ignoring metadata

❌ Embedding raw OCR output

❌ Ignoring encoding

❌ No language detection

---

# Metrics

Track

- Parse Success Rate
- OCR Accuracy
- Characters Extracted
- Parse Latency
- Metadata Completeness
- Parser Failure Rate

---

# Testing

Verify

- PDFs
- DOCX
- HTML
- Markdown
- Images
- OCR
- Corrupt files
- Large files
- Multi-language documents

---

# Review Checklist

□ Layout preserved

□ Metadata extracted

□ Tables retained

□ OCR supported

□ Boilerplate removed

□ Language detected

□ Text normalized

□ Errors handled

□ Logging implemented

□ Tests written

---

# Related Skills

- ingestion.md
- chunking.md
- embeddings.md
- retrieval.md

---

# Definition of Done

A document parser is production-ready only if

✓ Structure is preserved

✓ Metadata is extracted

✓ Text is normalized

✓ OCR is supported

✓ Tables remain structured

✓ Code blocks remain intact

✓ Boilerplate is removed

✓ Errors are handled gracefully

✓ Performance is measurable

✓ Pipeline is fully testable