# Skill

Streaming

Version: 1.0

---

# Goal

Deliver language model responses incrementally while maintaining low latency, reliability, observability, and a seamless user experience.

Streaming allows users to begin consuming responses before generation has completed.

A production streaming system should optimize perceived latency without compromising correctness.

---

# When to Load

Load this skill whenever building

- AI Chat Applications
- RAG Systems
- Coding Assistants
- Voice Assistants
- Customer Support AI
- Multi-Agent Systems

---

# Prerequisites

- prompt_builder.md
- guardrails.md

---

# Core Principles

Streaming optimizes

Time-To-First-Token

↓

User Experience

↓

Responsiveness

↓

Perceived Performance

Streaming should never change answer quality.

---

# Responsibilities

A streaming system should

- Stream tokens
- Handle cancellation
- Handle retries
- Buffer partial output
- Preserve citations
- Track latency
- Recover gracefully

It should not

- Modify retrieval
- Skip safety checks
- Ignore client disconnects

---

# Streaming Architecture

```
User

↓

API Gateway

↓

Prompt Builder

↓

LLM

↓

Streaming Engine

↓

Transport Layer

↓

Client
```

Streaming is a transport concern, not an LLM concern.

---

# Streaming Pipeline

```
User Query

↓

Retrieval

↓

Prompt Assembly

↓

LLM Starts

↓

First Token

↓

Incremental Tokens

↓

Final Token

↓

Completion Metadata
```

---

# Transport Options

## Server-Sent Events (SSE)

Characteristics

- One-way communication
- Simple HTTP
- Excellent browser support
- Low overhead

Best for

Chat applications

Recommended default.

---

## WebSockets

Characteristics

- Bidirectional
- Persistent connection
- Higher complexity

Best for

Collaborative applications

Voice

Real-time agents

---

## HTTP Chunked Responses

Useful for

Simple deployments

CLI applications

Streaming APIs

---

# Time-To-First-Token (TTFT)

Definition

Time between

User request

↓

First generated token

Goal

Minimize TTFT.

Users perceive systems with low TTFT as faster.

---

# Token Streaming

```
Hello

↓

Hello,

↓

Hello, how

↓

Hello, how can

↓

...
```

Never wait for the full response unless required.

---

# Buffering

Small buffers

↓

Lower latency

↓

Higher network overhead

Large buffers

↓

Higher latency

↓

Lower overhead

Tune buffer sizes based on deployment.

---

# Cancellation

Support

Browser close

↓

Stop button

↓

Timeout

↓

Client disconnect

↓

Server shutdown

Terminate generation immediately when appropriate.

---

# Backpressure

Clients may consume tokens slower than they are generated.

Strategies

Queue

↓

Throttle

↓

Pause

↓

Drop connection

Prevent memory growth.

---

# Retry Strategy

Retry

Network interruptions

Temporary provider failures

Gateway errors

Do not retry

Completed generations

Client cancellations

Invalid prompts

---

# Partial Responses

Maintain

Current text

↓

Current citations

↓

Generation state

↓

Completion status

Never lose partially generated work unexpectedly.

---

# Streaming Citations

Do not delay citations until the end.

Possible strategies

Inline

```
Docker uses containers [1]
```

Deferred

```
Response...

Sources:
[1]
```

Incremental

Stream citations as supporting evidence becomes available.

---

# Tool Calls

Streaming agents may pause generation to execute tools.

Example

```
Generate

↓

Call Search API

↓

Resume Streaming

↓

Finish Response
```

The client should be aware of intermediate states.

---

# Structured Outputs

When generating JSON

Avoid streaming invalid fragments.

Strategies

- Buffer until valid
- Stream JSON events
- Stream line-delimited JSON (NDJSON)

Maintain parser compatibility.

---

# Multi-Agent Streaming

Coordinator

↓

Worker A

Worker B

Worker C

↓

Aggregator

↓

Client

Stream progress as work completes.

---

# Engineering Decisions

## SSE

Use when

Chat applications

RAG

Documentation assistants

Customer support

Recommended default.

---

## WebSockets

Use when

Real-time collaboration

Voice AI

Shared workspaces

Interactive coding

Trade-off

Higher operational complexity.

---

## Buffered Streaming

Use when

Structured outputs

Large JSON responses

Strict formatting requirements

---

## Immediate Token Streaming

Use when

Conversational AI

Research assistants

General-purpose chat

Best user experience.

---

# Error Handling

Handle

Provider timeout

↓

Network interruption

↓

Gateway failure

↓

Token generation error

↓

Client disconnect

Communicate errors gracefully.

---

# Performance Considerations

Optimize

TTFT

↓

Tokens/sec

↓

Serialization

↓

Network latency

↓

Compression

↓

Connection reuse

Streaming performance should be measured independently from model latency.

---

# Security

Protect

Authentication

Authorization

Rate limiting

Connection limits

Sensitive tokens

Terminate unauthorized streams immediately.

---

# Observability

Track

Time-To-First-Token

Generation latency

Tokens per second

Average stream duration

Cancellation rate

Connection failures

Provider latency

Streaming errors

---

# Metrics

Monitor

TTFT

Average Tokens/sec

P50 Stream Duration

P95 Stream Duration

Cancellation Rate

Reconnect Rate

Dropped Connections

Provider Errors

Average Response Size

---

# Common Failures

- Buffering the entire response
- Ignoring client disconnects
- Missing cancellation support
- Streaming invalid JSON
- High TTFT
- Lost citations
- Memory leaks
- No timeout handling

---

# Best Practices

- Optimize TTFT.
- Prefer SSE for standard chat applications.
- Handle cancellation immediately.
- Stream citations when practical.
- Monitor tokens per second.
- Support graceful retries.
- Separate transport from generation logic.
- Keep streaming provider-independent.

---

# Anti-Patterns

❌ Waiting for the complete response before sending data

❌ Ignoring disconnects

❌ Mixing transport and business logic

❌ Streaming malformed structured outputs

❌ No timeout policies

❌ No connection limits

❌ No observability

---

# Real-World Production Examples

## ChatGPT

- Streams tokens immediately after generation begins.
- Supports interruption during response generation.
- Optimizes for low Time-To-First-Token.

---

## GitHub Copilot

- Streams code suggestions incrementally.
- Cancels generation when user continues typing.
- Prioritizes responsiveness over full completion.

---

## Perplexity AI

- Streams generated answers while progressively incorporating citations.
- Balances answer generation with evidence presentation.

---

## Claude

- Streams conversational responses while preserving formatting and structured output.
- Handles long generations efficiently through incremental delivery.

---

# Testing

Verify

SSE connections

WebSocket connections

Cancellation

Retries

Timeouts

Streaming JSON

Citation streaming

Client disconnects

Load testing

---

# Review Checklist

□ Streaming transport selected

□ TTFT measured

□ Cancellation supported

□ Retry strategy implemented

□ Buffer sizes tuned

□ Metrics configured

□ Security reviewed

□ Observability enabled

□ Load tested

□ Tests passing

---

# Related Skills

- prompt_builder.md
- guardrails.md
- evaluation.md

---

# Definition of Done

A streaming implementation is production-ready only if

✓ Time-To-First-Token meets latency objectives

✓ Tokens are streamed incrementally

✓ Cancellation is supported

✓ Client disconnects are handled gracefully

✓ Structured outputs remain valid

✓ Security controls are enforced

✓ Streaming metrics are continuously monitored

✓ Performance is benchmarked under load

✓ Error recovery is implemented

✓ User experience remains responsive under production traffic