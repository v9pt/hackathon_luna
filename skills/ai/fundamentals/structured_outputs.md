# Skill

Structured Outputs

Version: 1.0

---

# Goal

Design AI systems that produce deterministic, machine-readable outputs using schemas instead of unpredictable natural language.

Structured outputs improve

- Reliability
- Validation
- Automation
- Integration
- Safety
- Maintainability

Every AI application that interacts with software should prefer structured outputs.

---

# When to Load

Load this skill whenever

- Building AI APIs
- Tool Calling
- Function Calling
- RAG
- Agents
- Workflow Automation
- Data Extraction
- Classification
- Code Generation

---

# Prerequisites

- llm_basics.md
- prompt_engineering.md

---

# Core Principle

Never parse natural language when the model can generate structured data.

Prefer

Application

↓

LLM

↓

Validated Schema

↓

Business Logic

Instead of

Application

↓

LLM

↓

Regex

↓

String Parsing

↓

Hope it works

---

# Why Structured Outputs

Natural language changes.

Schemas do not.

Good

```json
{
  "priority":"high",
  "completed":true
}
```

Bad

"The task seems pretty important and yes, it has been completed."

---

# Benefits

Structured outputs provide

Consistency

Validation

Strong typing

Easy debugging

Automation

Provider portability

Reduced hallucinations

Simpler testing

---

# Common Formats

Preferred

JSON

Pydantic Models

JSON Schema

Typed Objects

Enums

Arrays

Objects

Avoid

Free-form text

Regex parsing

CSV generation

Markdown tables for APIs

---

# Schema Design Principles

Schemas should be

Small

Explicit

Typed

Validated

Documented

Versioned

Stable

---

# Example Schema

Task

↓

title

description

priority

status

deadline

owner

tags

Avoid unnecessary fields.

---

# Strong Typing

Prefer

priority

HIGH

MEDIUM

LOW

Instead of

"Very Important"

"Urgent"

"Kind of High"

Enums reduce ambiguity.

---

# Required vs Optional

Every field should clearly indicate

Required

Optional

Nullable

Avoid ambiguous schemas.

---

# Nested Objects

Good

User

↓

Profile

↓

Address

↓

Preferences

Design schemas to reflect real business entities.

---

# Arrays

Use arrays only for collections.

Good

tags

documents

citations

actions

Avoid comma-separated strings.

---

# Validation

Always validate outputs before using them.

Validation should check

Required fields

Data types

Enum values

Ranges

Formats

Business rules

Never trust model output blindly.

---

# Pydantic

Preferred validation library for Python.

Application

↓

LLM

↓

Pydantic Validation

↓

Business Logic

Reject invalid responses.

---

# JSON Schema

Define

Types

Constraints

Enums

Descriptions

Required fields

JSON Schema improves provider interoperability.

---

# Error Handling

Handle

Missing fields

Wrong types

Invalid JSON

Extra fields

Malformed objects

Retry or repair invalid outputs.

---

# Output Repair

If validation fails

Validate

↓

Repair Prompt

↓

Retry

↓

Validate Again

Do not immediately fail the request.

---

# Function Calling

Structured outputs pair naturally with function calling.

Model

↓

Arguments

↓

Validation

↓

Tool Execution

↓

Structured Response

---

# Tool Calling

Every tool should define

Input Schema

Output Schema

Error Schema

Avoid untyped tool interfaces.

---

# RAG Outputs

Return

Answer

Sources

Confidence

Citations

Reasoning Summary (optional)

Do not return only plain text.

---

# Agent Outputs

Agent responses should include

Thought Summary

Selected Tool

Arguments

Result

Status

Next Action

Internal reasoning should not be exposed unless explicitly required.

---

# Versioning

Every schema should include

Version

Breaking changes

Migration notes

Treat schemas like APIs.

---

# Security

Reject

Unexpected fields

Code injection

Executable content

Unsafe HTML

Validate before persistence.

---

# Testing

Verify

Schema validity

Edge cases

Missing fields

Malformed JSON

Large outputs

Provider compatibility

Regression datasets

---

# Best Practices

- Define schemas before writing prompts.
- Keep schemas minimal.
- Use enums whenever possible.
- Validate every response.
- Reject malformed outputs.
- Separate schema definitions from prompts.
- Version schemas.
- Prefer provider-native structured output features.

---

# Anti-Patterns

❌ Parsing paragraphs

❌ Regex extraction

❌ Dynamic field names

❌ Mixed data types

❌ Unvalidated JSON

❌ Huge schemas

❌ Optional everything

❌ Business logic inside prompts

---

# Metrics

Track

- Validation Success Rate
- JSON Validity
- Retry Rate
- Repair Rate
- Schema Coverage
- Latency
- Cost

---

# Testing

Verify

- Valid JSON
- Required fields
- Enum correctness
- Provider compatibility
- Retry behavior
- Validation performance

---

# Review Checklist

□ Schema defined

□ Types explicit

□ Enums used

□ Validation implemented

□ Error handling present

□ Output repair implemented

□ Versioned

□ Tested

---

# Related Skills

- llm_basics.md
- prompt_engineering.md
- tool_calling.md
- function_calling.md
- evaluation.md
- provider_abstraction.md

---

# Definition of Done

Structured outputs are production-ready only if

✓ Schema is documented

✓ Validation is implemented

✓ Invalid outputs are handled

✓ Retry strategy exists

✓ Types are explicit

✓ Business logic never depends on free-form text

✓ Tests cover edge cases

✓ Versioning is maintained