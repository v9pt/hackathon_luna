# Skill

Memory Integration

Version: 1.0

---

# Goal

Design reliable memory systems that enable AI agents to retain relevant information across interactions, personalize behavior, improve decision-making, and learn from previous executions.

Memory extends an agent beyond the current execution by providing continuity across sessions and workflows.

A production memory system should retrieve the right information at the right time while avoiding unnecessary context and protecting user privacy.

---

# When to Load

Load this skill whenever building

- Personal AI Assistants
- Coding Agents
- Enterprise AI
- Customer Support Agents
- Research Agents
- Multi-Agent Systems
- Long-Term Autonomous Systems

---

# Prerequisites

- state_management.md
- reasoning.md
- retrieval.md
- embeddings.md
- vector_databases.md

---

# Core Principles

Memory is

Past Experience

↓

Relevant Retrieval

↓

Current Reasoning

↓

Improved Decisions

Memory should support reasoning rather than replace it.

---

# Responsibilities

Memory Integration should

- Store experiences
- Retrieve relevant context
- Personalize behavior
- Support long-term tasks
- Learn from feedback
- Improve future reasoning

Memory Integration should not

- Store every interaction
- Replace databases
- Store secrets unnecessarily
- Override runtime state

---

# Memory vs State

| State | Memory |
|--------|---------|
| Current execution | Historical knowledge |
| Temporary | Persistent |
| Workflow-specific | Cross-workflow |
| Reset after completion | Survives sessions |
| Used for execution | Used for retrieval |

State answers

"What is happening now?"

Memory answers

"What happened before?"

---

# Memory Architecture

```
User

↓

Reasoner

↓

Memory Retriever

↓

Relevant Memories

↓

Context Builder

↓

LLM

↓

Response

↓

Memory Writer
```

Memory should remain external to the model.

---

# Memory Lifecycle

```
Observe

↓

Evaluate

↓

Store

↓

Index

↓

Retrieve

↓

Use

↓

Update

↓

Archive
```

---

# Types of Memory

## Working Memory

Temporary information required for the current reasoning cycle.

Examples

- Active variables
- Current plan
- Tool outputs

Usually implemented using runtime state.

---

## Episodic Memory

Stores experiences.

Examples

- Previous conversations
- Completed tasks
- Failures
- User interactions

Useful for reflection and adaptation.

---

## Semantic Memory

Stores factual knowledge.

Examples

- Documentation
- Company policies
- API specifications
- Product information

Typically backed by vector databases.

---

## Procedural Memory

Stores how to perform tasks.

Examples

- Workflows
- Standard Operating Procedures
- Prompt templates
- Agent playbooks

Supports consistent execution.

---

## User Memory

Stores persistent user preferences.

Examples

- Preferred coding style
- Time zone
- Language
- Notification preferences

Should always require appropriate consent.

---

# Memory Storage

Choose storage based on memory type.

Working Memory

- Runtime state
- Redis

Episodic Memory

- PostgreSQL
- MongoDB

Semantic Memory

- Vector Database

Procedural Memory

- Git Repository
- Knowledge Base

---

# Memory Retrieval

Retrieve based on

Similarity

↓

Recency

↓

Importance

↓

Permissions

↓

Current Goal

Avoid retrieving irrelevant memories.

---

# Memory Writing

Not every interaction should become memory.

Store only

- Important decisions
- User preferences
- Completed tasks
- Lessons learned
- High-value context

Avoid noisy memories.

---

# Memory Ranking

Rank memories using

Similarity Score

Recency

Importance

Frequency

Confidence

Higher-ranked memories should receive priority.

---

# Memory Consolidation

Merge related memories.

```
Multiple Events

↓

Summarize

↓

Store

↓

Archive Originals
```

Reduces storage growth.

---

# Forgetting

Not all memories should persist forever.

Forget

- Temporary data
- Expired preferences
- Outdated knowledge
- Low-value interactions

Support configurable retention policies.

---

# Memory Updates

Support

- Versioning
- Corrections
- Deletion
- User-controlled edits

Memory should evolve over time.

---

# Multi-Agent Memory

Separate

Local Memory

↓

Shared Memory

↓

Knowledge Base

Workers should not overwrite each other's memories.

---

# Pattern References

## ReAct

Retrieve memory before reasoning.

See

patterns/react.md

---

## Reflexion

Store lessons after execution.

See

patterns/reflexion.md

---

## Planner Executor

Planner retrieves memory.

Executor updates experiences.

See

patterns/planner_executor.md

---

# Engineering Decisions

## Vector Database

Use when

Semantic retrieval is required.

Recommended default.

---

## Relational Database

Use when

Structured historical records are needed.

---

## Hybrid Memory

Combine

Relational Database

+

Vector Database

+

Object Storage

Recommended for enterprise systems.

---

# Runtime Architecture

```
Reasoner

↓

Memory Retriever

↓

Vector Search

↓

Rank Memories

↓

Context Builder

↓

LLM

↓

Memory Writer
```

---

# Performance Considerations

Optimize

Embedding latency

↓

Retrieval latency

↓

Ranking quality

↓

Memory size

↓

Context length

↓

Storage cost

Avoid retrieving unnecessary memories.

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Store everything | High recall | High cost and noise |
| Selective storage | Cleaner retrieval | Risk of missing context |
| Vector search | Semantic retrieval | Embedding overhead |
| Relational storage | Structured queries | Weak semantic search |
| Hybrid memory | Flexible | Higher complexity |

---

# Security

Protect

- Personal information
- User preferences
- Proprietary knowledge
- API credentials
- Sensitive conversations

Support

- Encryption
- Access control
- Audit logging
- User deletion requests

Memory systems must respect privacy regulations.

---

# Observability

Track

Memory writes

↓

Retrieval latency

↓

Retrieval quality

↓

Memory growth

↓

Storage utilization

↓

Recall accuracy

---

# Metrics

Monitor

Memory Hit Rate

Retrieval Latency

Average Context Size

Memory Growth

Embedding Cost

Recall Accuracy

Storage Cost

Memory Write Frequency

---

# Common Failures

- Remembering everything
- Retrieving irrelevant memories
- Mixing state and memory
- Duplicate memories
- Outdated knowledge
- Ignoring permissions
- Context overload

---

# Best Practices

- Store only high-value information.
- Retrieve based on relevance.
- Separate state from memory.
- Version memory records.
- Periodically consolidate memories.
- Respect user privacy.
- Measure retrieval quality.
- Allow users to edit or delete memories.

---

# Anti-Patterns

❌ Unlimited memory growth

❌ Using prompts as storage

❌ Mixing runtime state with memory

❌ Retrieving every memory

❌ Ignoring user consent

❌ Duplicate storage

❌ No retention policy

---

# Real-World Production Examples

## ChatGPT

- Maintains optional persistent user memories separately from conversation context.
- Retrieves relevant preferences without exposing unrelated information.

---

## Claude

- Uses conversation context effectively while relying on external systems for persistent knowledge.
- Separates execution context from long-term information.

---

## GitHub Copilot

- Retrieves repository context rather than memorizing code.
- Uses semantic search to provide relevant suggestions.

---

## LangGraph

- Integrates checkpoints with external memory stores.
- Supports long-running workflows that combine execution state and memory retrieval.

---

## Enterprise Knowledge Assistants

- Combine relational databases, vector search, and document repositories.
- Retrieve only information relevant to the current task.

---

# Testing

Verify

Memory writes

Memory retrieval

Ranking quality

Retention policies

Permission enforcement

Memory updates

Deletion requests

Context relevance

---

# Review Checklist

□ Memory types defined

□ State separated from memory

□ Retrieval strategy implemented

□ Memory ranking configured

□ Retention policy documented

□ Privacy controls enforced

□ Metrics configured

□ Observability enabled

□ Tests passing

---

# Related Skills

- state_management.md
- retrieval.md
- embeddings.md
- vector_databases.md
- reflection.md
- self_correction.md
- patterns/reflexion.md
- patterns/planner_executor.md
- patterns/react.md

---

# Definition of Done

A memory integration system is production-ready only if

✓ Runtime state and long-term memory are clearly separated

✓ Memory retrieval is relevant and efficient

✓ Storage supports multiple memory types

✓ Ranking prioritizes useful information

✓ Privacy and permissions are enforced

✓ Retention and deletion policies are implemented

✓ Memory improves reasoning without overwhelming context

✓ Retrieval quality is measurable

✓ Observability supports debugging and optimization

✓ The agent reliably benefits from past experience while maintaining user trust