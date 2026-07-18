# Skill

Prompt Builder

Version: 1.0

---

# Goal

Construct reliable, deterministic, and token-efficient prompts that maximize answer quality while minimizing hallucinations.

The Prompt Builder is responsible for assembling the final context that will be sent to the LLM.

It is not responsible for retrieving knowledge or generating responses.

---

# When to Load

Load this skill whenever building

- RAG systems
- AI Assistants
- Enterprise Search
- AI Coding Agents
- Customer Support AI
- Research Assistants

---

# Prerequisites

- retrieval.md
- reranking.md

---

# Core Principles

The quality of an answer depends on

Retrieved Context

+

Prompt Structure

+

Instructions

+

Conversation History

↓

LLM Response

The Prompt Builder controls all of these inputs.

---

# Responsibilities

The Prompt Builder should

- Assemble retrieved context
- Manage token budgets
- Inject citations
- Preserve conversation history
- Apply system instructions
- Structure prompts consistently
- Support multiple providers

It should not

- Retrieve documents
- Generate embeddings
- Perform reranking

---

# Prompt Pipeline

```
User Query

↓

Conversation Memory

↓

Retrieved Context

↓

System Instructions

↓

Developer Instructions

↓

User Prompt

↓

Prompt Builder

↓

Final Prompt

↓

LLM
```

---

# Prompt Hierarchy

Every prompt has four logical layers.

1. System Prompt

Defines the AI's role and global behavior.

---

2. Developer Prompt

Application-specific instructions.

Examples

Formatting

Policies

Guardrails

Output schemas

---

3. User Prompt

The actual user request.

---

4. Retrieved Context

Knowledge retrieved from RAG.

Never allow retrieved context to override system instructions.

---

# Prompt Structure

Recommended order

```
System

↓

Developer Instructions

↓

Conversation History

↓

Retrieved Context

↓

User Question

↓

Output Instructions
```

Keep the structure consistent across requests.

---

# Context Window Management

LLMs have finite context windows.

The Prompt Builder must allocate tokens for

System Prompt

Conversation History

Retrieved Context

User Input

Expected Output

Never exceed the model's context limit.

---

# Token Budgeting

Example

Context Window = 128K

Reserve

System Prompt = 2K

Conversation = 10K

Retrieved Context = 30K

User Input = 2K

Response = 20K

Remaining = Safety Buffer

Always leave headroom.

---

# Context Ordering

Not all retrieved chunks are equally important.

Order

Most Relevant

↓

Supporting Evidence

↓

Background Information

↓

Additional References

The strongest evidence should appear first.

---

# Context Compression

Retrieved chunks may exceed token limits.

Compress by

Removing duplicates

Removing boilerplate

Keeping only relevant paragraphs

Summarizing low-priority sections

Do not truncate arbitrarily.

---

# Citation Injection

Attach source metadata to each chunk.

Example

```
[Source: Engineering Handbook, Page 42]

Docker containers should...
```

Benefits

Traceability

Debugging

User trust

---

# Source Attribution

Maintain

Document ID

Page Number

Section

URL

Author

Timestamp

This enables answer citations and auditing.

---

# Conversation History

Maintain only relevant history.

Avoid replaying the entire conversation.

Strategies

- Sliding Window
- Summary Memory
- Semantic Memory

Older conversations should be summarized when appropriate.

---

# Prompt Templates

Store prompts as reusable templates.

Example

```
System

Developer

Context

Question

Output Format
```

Version templates independently from application code.

---

# Structured Output

When possible, require structured responses.

Examples

JSON

XML

Markdown

Tables

Schemas reduce parsing errors.

---

# Provider Abstraction

Different providers have different APIs.

The Prompt Builder should expose one internal format and translate it to

- OpenAI
- Anthropic
- Gemini
- Ollama
- Azure OpenAI

Application logic should remain provider-independent.

---

# Hallucination Mitigation

Include explicit instructions such as

- Answer only using the provided context.
- If the answer is unavailable, state that you don't know.
- Do not invent sources.
- Cite supporting evidence.

Prompt design should encourage grounded responses, but cannot guarantee them.

---

# Few-Shot Examples

Use examples only when they consistently improve task performance.

Examples consume context.

Avoid excessive few-shot prompting in RAG.

---

# Context Deduplication

Retrieved chunks may overlap.

Remove

Duplicate paragraphs

Repeated headers

Repeated tables

Repeated code

Avoid wasting context window.

---

# Long Context Handling

For large knowledge bases

Retrieve

↓

Compress

↓

Rank

↓

Assemble

↓

Validate Token Budget

↓

Generate Prompt

Do not send every retrieved chunk.

---

# Engineering Decisions

## Large Context Windows

Use when

Large manuals

Research papers

Books

Trade-off

Higher cost

Higher latency

---

## Small Context Windows

Use when

Customer support

FAQ systems

Simple assistants

Lower cost

Lower latency

---

## Prompt Templates

Use when

Multiple applications

Multi-agent systems

Shared prompt libraries

Always recommended.

---

## Dynamic Prompt Assembly

Use when

Retrieved context changes every request

Most RAG systems

Recommended default.

---

# Performance Considerations

Optimize

Prompt assembly time

Token count

Serialization

Compression

Provider formatting

Prompt building should contribute minimal latency.

---

# Security

Never include

Secrets

Credentials

Private API keys

Sensitive internal metadata

Apply redaction before prompt assembly.

---

# Observability

Track

Prompt size

Token count

Compression ratio

Assembly latency

Citation count

Template version

Prompt failures

---

# Metrics

Monitor

Average Prompt Tokens

Average Context Tokens

Compression Ratio

Assembly Latency

Prompt Failure Rate

Citation Coverage

Hallucination Rate

---

# Common Failures

- Context exceeds token limit
- Duplicate chunks
- Missing citations
- Incorrect prompt ordering
- Old conversation dominates context
- Prompt injection through retrieved text
- Inconsistent templates

---

# Best Practices

- Use reusable templates.
- Reserve token headroom.
- Order context by relevance.
- Compress intelligently.
- Attach citations.
- Separate system and user instructions.
- Version prompt templates.
- Measure token usage continuously.

---

# Anti-Patterns

❌ Dumping every retrieved chunk into the prompt

❌ No token budgeting

❌ Mixing system and user instructions

❌ Ignoring conversation history

❌ Missing citations

❌ No prompt versioning

❌ Hardcoded prompts throughout the codebase

---

# Testing

Verify

Prompt assembly

Token budgeting

Citation injection

Template rendering

Conversation handling

Provider compatibility

Structured output

Compression

---

# Review Checklist

□ Prompt template defined

□ Token budget enforced

□ Context ordered by relevance

□ Citations injected

□ Conversation memory integrated

□ Prompt versioned

□ Structured output supported

□ Security reviewed

□ Metrics configured

□ Tests passing

---

# Related Skills

- retrieval.md
- reranking.md
- memory.md
- guardrails.md
- evaluation.md

---

# Definition of Done

A Prompt Builder is production-ready only if

✓ Prompt templates are reusable and versioned

✓ Token budgets are enforced

✓ Retrieved context is ordered and deduplicated

✓ Citations are preserved

✓ Conversation history is managed efficiently

✓ Structured outputs are supported

✓ Provider abstraction is implemented

✓ Prompt assembly latency is monitored

✓ Security reviews are complete

✓ End-to-end prompt quality is continuously evaluated