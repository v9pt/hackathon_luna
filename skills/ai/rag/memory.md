# Skill

Memory

Version: 1.0

---

# Goal

Design scalable, secure, and efficient memory systems that allow AI applications to retain, retrieve, update, and forget information across conversations and tasks.

Memory enables personalization, continuity, long-running workflows, and collaborative agents.

A production AI system should treat memory as a first-class subsystem rather than an extension of the prompt.

---

# When to Load

Load this skill whenever building

- AI Agents
- RAG Systems
- Coding Assistants
- Customer Support AI
- Research Assistants
- Multi-Agent Systems
- Personal AI Assistants

---

# Prerequisites

- retrieval.md
- prompt_builder.md

---

# Core Principles

Memory should answer four questions

What should be remembered?

↓

Where should it be stored?

↓

When should it be retrieved?

↓

When should it be forgotten?

Memory is a retrieval problem, not a prompt problem.

---

# Responsibilities

A memory system should

- Store important information
- Retrieve relevant memories
- Update memories
- Forget obsolete memories
- Support personalization
- Enable long-term continuity

It should not

- Store every conversation forever
- Replace the knowledge base
- Override system instructions

---

# Memory Architecture

```
User

↓

Conversation

↓

Memory Manager

↓

Memory Classifier

↓

Memory Store

↓

Retriever

↓

Prompt Builder

↓

LLM
```

Memory management should be independent of the LLM.

---

# Types of Memory

Production AI systems typically distinguish between

Short-Term Memory

↓

Long-Term Memory

↓

Working Memory

↓

Semantic Memory

↓

Episodic Memory

↓

Procedural Memory

Each serves a different purpose.

---

# Working Memory

Temporary context for the current reasoning task.

Examples

- Current user request
- Active tool outputs
- Intermediate reasoning
- Temporary variables

Working memory should be discarded after the task completes.

---

# Short-Term Memory

Maintains recent conversation history.

Examples

Last 10 messages

Current task

Current topic

Implementation

Sliding window

Token-limited history

Summaries

---

# Long-Term Memory

Stores durable information.

Examples

User preferences

Project information

Persistent goals

Past decisions

Useful across multiple conversations.

---

# Semantic Memory

Stores facts.

Examples

Company policy

API documentation

Project architecture

User preferences

Semantic memory is usually implemented with RAG.

---

# Episodic Memory

Stores experiences.

Examples

Last deployment failed

Previous debugging session

Earlier design decisions

Past conversations

Useful for agents.

---

# Procedural Memory

Stores how to perform tasks.

Examples

Coding standards

Deployment workflow

Testing checklist

Internal engineering practices

Often represented as playbooks.

---

# Memory Lifecycle

```
Conversation

↓

Importance Detection

↓

Classification

↓

Storage

↓

Retrieval

↓

Update

↓

Expiration
```

Not everything should become memory.

---

# Memory Classification

Evaluate each piece of information.

Questions

Is it useful later?

Is it specific?

Is it durable?

Is it private?

Should it expire?

Only store information with long-term value.

---

# Memory Importance

High Importance

Project goals

User preferences

Architecture decisions

Long-running tasks

Low Importance

Greetings

Small talk

Temporary questions

One-time clarifications

Avoid polluting memory.

---

# Storage Strategies

## Relational Database

Store

Profiles

Settings

Preferences

Configuration

---

## Vector Database

Store

Semantic memories

Past conversations

Meeting notes

Research

---

## Graph Database

Store

Relationships

Entities

Knowledge graphs

Useful for complex reasoning.

---

## Object Storage

Store

Large documents

Images

Videos

Audio

Never embed binary files directly.

---

# Memory Retrieval

Retrieve memories using

Semantic similarity

Metadata filters

Time

Importance

Recency

Task relevance

Never retrieve all memories.

---

# Memory Ranking

Rank memories using

Relevance

↓

Recency

↓

Importance

↓

Confidence

↓

User context

---

# Memory Consolidation

Merge duplicate memories.

Example

```
User prefers TypeScript.

↓

User prefers TypeScript and React.

↓

One updated memory.
```

Avoid duplicate facts.

---

# Memory Updating

Memory should evolve.

Old

```
Uses GPT-4
```

New

```
Uses GPT-5
```

Update instead of duplicating.

---

# Forgetting

Not every memory should be permanent.

Forget

Expired tasks

Old preferences

Completed workflows

Temporary information

Support

TTL

Expiration dates

Manual deletion

---

# Multi-Agent Memory

Multiple agents should share

Project knowledge

↓

Documents

↓

Architecture

↓

Tasks

↓

User preferences

Agent-specific reasoning should remain isolated.

---

# User Profiles

Maintain structured profiles.

Examples

Preferred language

Preferred IDE

Preferred framework

Communication style

Current project

Profiles should be editable.

---

# Session Memory

Store

Current session state

Temporary variables

Open tasks

Discard after session ends unless promoted.

---

# Memory Retrieval Pipeline

```
User Query

↓

Memory Search

↓

Ranking

↓

Deduplication

↓

Prompt Builder

↓

LLM
```

Memory retrieval should happen before prompt assembly.

---

# Engineering Decisions

## Sliding Window

Use when

Simple chatbots

Low complexity

Short conversations

Advantages

Fast

Simple

Trade-off

Loses long-term context.

---

## Summary Memory

Use when

Long conversations

Customer support

Research assistants

Advantages

Compact

Lower token usage

Trade-off

May omit details.

---

## Vector Memory

Use when

Semantic retrieval

Knowledge assistants

Coding agents

Recommended default for long-term memory.

---

## Graph Memory

Use when

Entity relationships matter.

Examples

Knowledge graphs

Research assistants

Enterprise search

Trade-off

Higher complexity.

---

# Performance Considerations

Monitor

Memory retrieval latency

Memory growth

Storage cost

Embedding cost

Cache hit rate

Memory should not dominate response latency.

---

# Security

Encrypt stored memories.

Enforce

Authentication

Authorization

Tenant isolation

Audit logging

Support user deletion requests.

Never expose another user's memory.

---

# Privacy

Support

Consent

Retention policies

GDPR deletion

Selective forgetting

Memory export

Privacy must be designed into the system.

---

# Observability

Track

Memory retrieval time

Memory updates

Memory deletions

Storage growth

Recall rate

Retrieval quality

---

# Metrics

Monitor

Memory Hit Rate

Average Retrieval Time

Duplicate Memory Rate

Memory Size

Storage Growth

Retention Rate

Expired Memory Count

---

# Common Failures

- Storing every message
- Duplicate memories
- No expiration
- Cross-user leakage
- Poor retrieval
- Missing updates
- Infinite memory growth
- No deletion policy

---

# Best Practices

- Store only durable information.
- Separate memory types.
- Retrieve only relevant memories.
- Version memories when needed.
- Support forgetting.
- Monitor memory growth.
- Respect user privacy.
- Keep memory provider-independent.

---

# Anti-Patterns

❌ Infinite chat history

❌ No memory classification

❌ Duplicate facts

❌ Hardcoded user profiles

❌ No deletion support

❌ No tenant isolation

❌ Mixing memory with prompt templates

❌ Treating memory as a database dump

---

# Testing

Verify

Memory storage

Memory retrieval

Ranking

Expiration

Updates

Deletion

Multi-user isolation

Long conversations

Vector retrieval

---

# Review Checklist

□ Memory types defined

□ Storage strategy selected

□ Retrieval implemented

□ Ranking configured

□ Forgetting policy implemented

□ Privacy reviewed

□ Metrics configured

□ Security enforced

□ Multi-tenant support verified

□ Tests passing

---

# Related Skills

- prompt_builder.md
- retrieval.md
- evaluation.md
- guardrails.md

---

# Definition of Done

A memory system is production-ready only if

✓ Memory types are clearly separated

✓ Durable information is classified before storage

✓ Retrieval is relevance-driven

✓ Memory updates replace stale facts

✓ Forgetting policies are implemented

✓ Privacy and deletion requirements are supported

✓ Multi-tenant isolation is enforced

✓ Memory retrieval latency is monitored

✓ Storage growth is controlled

✓ End-to-end memory quality is continuously evaluated