# Skill

Communication Protocols

Version: 1.0

---

# Goal

Design reliable communication systems that enable agents, services, tools, and workflows to exchange information safely, efficiently, and consistently.

Communication protocols define how messages are created, transmitted, validated, processed, and acknowledged.

A production communication system should prioritize reliability, interoperability, and observability over raw speed.

---

# When to Load

Load this skill whenever building

- Multi-Agent Systems
- Distributed AI
- Enterprise AI
- Workflow Engines
- Tool Platforms
- Event-Driven Systems
- Agent Networks

---

# Prerequisites

- orchestration.md
- delegation.md
- state_management.md
- workflows.md

---

# Core Principles

Sender

↓

Serialize

↓

Transmit

↓

Receive

↓

Validate

↓

Process

↓

Acknowledge

Communication should always be explicit.

---

# Responsibilities

Communication systems should

- Exchange messages
- Validate schemas
- Preserve ordering when required
- Support retries
- Handle failures
- Enable interoperability
- Track message lifecycle

Communication systems should not

- Perform reasoning
- Execute workflows
- Store long-term memory

---

# Communication Lifecycle

```
Create Message

↓

Serialize

↓

Transmit

↓

Receive

↓

Validate

↓

Process

↓

Acknowledge

↓

Archive
```

---

# Communication Models

## Request Response

```
Agent

↓

Request

↓

Worker

↓

Response
```

Simple and deterministic.

---

## Publish Subscribe

```
Publisher

↓

Event Bus

↓

Subscriber A

Subscriber B

Subscriber C
```

Supports loose coupling.

---

## Event Driven

```
Event

↓

Listener

↓

Workflow
```

Ideal for distributed systems.

---

## Broadcast

One sender.

Many receivers.

Useful for notifications.

---

## Streaming

Continuous communication.

Examples

- Token streaming
- Live monitoring
- Sensor data

---

# Message Structure

Every message should include

- ID
- Sender
- Receiver
- Timestamp
- Type
- Payload
- Version
- Correlation ID
- Priority

Messages should be immutable after sending.

---

# Serialization

Supported formats

- JSON
- Protocol Buffers
- MessagePack
- Avro

Prefer schema-driven serialization.

---

# Message Validation

Validate

Schema

↓

Authentication

↓

Authorization

↓

Business Rules

↓

Integrity

Reject malformed messages.

---

# Correlation IDs

Every workflow should generate

Workflow ID

↓

Request ID

↓

Message ID

↓

Trace ID

Enables distributed tracing.

---

# Delivery Guarantees

Support

At Most Once

At Least Once

Exactly Once (when feasible)

Choose based on workload requirements.

---

# Ordering

Some workflows require strict ordering.

Others allow unordered parallel processing.

Ordering should be configurable.

---

# Reliability

Support

Retries

↓

Acknowledgements

↓

Dead Letter Queues

↓

Replay

↓

Timeouts

Messages should never disappear silently.

---

# Event Bus

Responsibilities

- Routing
- Fan-out
- Buffering
- Retry
- Replay
- Backpressure

Avoid direct coupling between agents.

---

# Shared State vs Messages

Messages

- Temporary
- Immutable
- Event-driven

Shared State

- Persistent
- Mutable
- Coordinated

Prefer messages unless shared state is required.

---

# Pattern References

## Supervisor Worker

Supervisor communicates through structured task messages.

See

patterns/supervisor_worker.md

---

## Planner Executor

Planner issues execution instructions.

Executors return structured results.

See

patterns/planner_executor.md

---

## Router

Routes incoming messages.

See

patterns/router.md

---

## Map Reduce

Workers communicate intermediate results.

Reducer aggregates outputs.

See

patterns/map_reduce.md

---

# Engineering Decisions

## REST

Use when

Simple APIs

Synchronous communication

---

## gRPC

Use when

Low latency

Typed contracts

Internal services

---

## Message Queue

Use when

Background processing

Reliable delivery

Asynchronous workflows

---

## Event Bus

Recommended for

Enterprise multi-agent systems

---

## MCP

Use when

Standardizing communication between LLMs and external tools or services through a common protocol.

---

## A2A (Agent-to-Agent)

Use when

Independent agents need standardized peer-to-peer communication.

---

# Runtime Architecture

```
Planner

↓

Message Bus

↓

Workers

↓

Responses

↓

Aggregator

↓

Completion
```

---

# Performance Considerations

Optimize

Serialization latency

↓

Network latency

↓

Queue throughput

↓

Message size

↓

Retry overhead

↓

Processing time

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| REST | Simple | Blocking |
| gRPC | Fast | More infrastructure |
| Event Bus | Decoupled | Operational complexity |
| Queue | Reliable | Higher latency |
| Streaming | Real-time | Stateful connections |

---

# Security

Protect against

- Message spoofing
- Replay attacks
- Unauthorized publishers
- Unauthorized subscribers
- Sensitive payload leakage
- Tampering

Support

- Authentication
- Authorization
- Encryption
- Signing
- Audit logging

---

# Observability

Track

Messages Sent

↓

Messages Received

↓

Latency

↓

Retries

↓

Failures

↓

Queue Depth

↓

Consumer Lag

↓

Dead Letter Queue Size

---

# Metrics

Monitor

Message Throughput

Average Latency

Failure Rate

Retry Rate

Queue Length

Consumer Lag

Serialization Time

Delivery Success Rate

---

# Common Failures

- Lost messages
- Duplicate delivery
- Schema mismatch
- Version incompatibility
- Deadlocks
- Infinite retries
- Missing acknowledgements

---

# Best Practices

- Version every message schema.
- Prefer immutable messages.
- Include correlation IDs.
- Validate every payload.
- Design for retries.
- Monitor queue health.
- Separate communication from business logic.
- Keep protocols provider-independent.

---

# Anti-Patterns

❌ Sending unstructured text

❌ Tight coupling between agents

❌ No schema validation

❌ No retries

❌ Missing acknowledgements

❌ Hidden message formats

❌ Ignoring version compatibility

---

# Real-World Production Examples

## Model Context Protocol (MCP)

- Defines standardized communication between AI applications and external tools.
- Uses structured requests and responses to improve interoperability.

---

## Google Agent Development Kit (ADK)

- Enables communication between modular agents using structured interfaces.
- Supports reusable components and service composition.

---

## AutoGen

- Exchanges structured conversational messages between collaborating agents.
- Coordinates planning and execution through message passing.

---

## LangGraph

- Uses graph edges and state transitions to coordinate communication between nodes.
- Persists execution state across communication boundaries.

---

## Apache Kafka

- Provides durable event streaming.
- Supports high-throughput communication between distributed services.

---

# Testing

Verify

Schema validation

Serialization

Retries

Ordering

Acknowledgements

Dead Letter Queues

Version compatibility

Authentication

Authorization

---

# Review Checklist

□ Message schema defined

□ Serialization selected

□ Validation implemented

□ Correlation IDs included

□ Delivery guarantees documented

□ Retry policy configured

□ Metrics enabled

□ Observability configured

□ Security reviewed

□ Tests passing

---

# Related Skills

- multi_agent_systems.md
- orchestration.md
- delegation.md
- workflows.md
- state_management.md
- patterns/router.md
- patterns/supervisor_worker.md
- patterns/planner_executor.md
- patterns/map_reduce.md

---

# Definition of Done

A communication protocol is production-ready only if

✓ Messages follow versioned schemas

✓ Communication supports synchronous and asynchronous patterns

✓ Delivery guarantees match workload requirements

✓ Correlation IDs enable end-to-end tracing

✓ Retries and acknowledgements ensure reliability

✓ Security protects message integrity and confidentiality

✓ Communication remains observable through metrics and traces

✓ Protocols are interoperable across agents and services

✓ Failures can be recovered without message loss

✓ Distributed agents communicate reliably at production scale