# Skill

WebSockets & Real-Time Systems Engineering

Version: 1.0

---

# Goal

Build scalable, low-latency, real-time applications using WebSockets while maintaining reliability, security, and performance.

Use WebSockets only when real-time communication provides clear value.

---

# Communication Model

Traditional

Client

↓

HTTP Request

↓

HTTP Response

Real-Time

Client

⇅

WebSocket Connection

↓

Bidirectional Communication

Persistent connections reduce repeated HTTP overhead.

---

# When to Use WebSockets

Ideal for

AI Chat

LLM Streaming

Notifications

Collaborative Editing

Live Dashboards

Progress Updates

Presence Systems

Gaming

IoT

Stock Prices

Do not use WebSockets for simple CRUD APIs.

---

# Preferred Stack

FastAPI

Redis Pub/Sub

Redis Streams

NGINX

OpenTelemetry

Docker

---

# Connection Lifecycle

Client Connects

↓

Authentication

↓

Connection Registered

↓

Heartbeat

↓

Bidirectional Messaging

↓

Disconnect

↓

Cleanup

Always clean stale connections.

---

# Authentication

Authenticate during connection.

Support

JWT

OAuth

API Keys

Cookies

Never trust unauthenticated WebSocket clients.

---

# Authorization

Verify

User

Organization

Room

Permissions

Subscription

Never allow clients to subscribe to arbitrary channels.

---

# Connection Manager

Maintain

Connection ID

User ID

Organization ID

Session

Last Activity

Subscriptions

Never store connection state only in memory if multiple servers exist.

---

# Horizontal Scaling

Use Redis Pub/Sub or Redis Streams.

Server A

↓

Redis

↓

Server B

↓

Connected Clients

Avoid single-instance WebSocket architectures.

---

# Message Format

Prefer JSON.

Example

{
  "type": "chat.message",
  "conversation_id": "...",
  "timestamp": "...",
  "payload": {}
}

Avoid sending raw strings.

---

# Message Types

Connect

Disconnect

Heartbeat

Chat

Progress

Notification

Typing

Presence

Error

Ack

Version messages when protocols evolve.

---

# AI Streaming

Stream

Tokens

Partial Responses

Tool Progress

Retrieval Status

Model Switching

Completion

Never wait for the entire LLM response before sending.

---

# Heartbeats

Use

Ping

↓

Pong

Detect dead connections.

Close inactive sessions.

---

# Reconnection

Support

Automatic reconnect

Backoff

Resume session

Duplicate detection

Handle temporary network failures gracefully.

---

# Rate Limiting

Protect

Connections

Messages

Uploads

Subscriptions

Prevent abuse.

---

# Backpressure

Handle slow clients.

Strategies

Drop

Buffer

Disconnect

Throttle

Never let one slow client block others.

---

# Rooms / Channels

Organize communication using

Conversation

Workspace

Organization

Project

Topic

Avoid global broadcasts.

---

# Presence

Track

Online

Offline

Idle

Typing

Editing

Store ephemeral presence in Redis.

---

# Notifications

Support

Targeted

Broadcast

Room

Organization

Priority

Never broadcast unnecessarily.

---

# File Transfer

Do not send large files over WebSockets.

Use

Object Storage

↓

Signed URL

↓

Notify over WebSocket

---

# Security

Validate every message.

Limit payload size.

Encrypt via TLS.

Authenticate.

Authorize.

Log abuse.

---

# Error Handling

Handle

Malformed JSON

Unknown Events

Permission Denied

Timeout

Disconnected Client

Retry

Rate Limit

Never crash the connection manager.

---

# Logging

Log

Connection

Disconnection

Authentication

Errors

Latency

Reconnects

Dropped Messages

---

# Monitoring

Track

Active Connections

Messages/sec

Latency

Reconnect Rate

Dropped Messages

Memory

CPU

Queue Size

---

# Scaling

Support

Load Balancers

Sticky Sessions (if required)

Redis

Multiple Workers

Stateless Servers

---

# AI Use Cases

Streaming LLM

Agent Progress

Retrieval Updates

Tool Execution

OCR Progress

Background Job Updates

Voice Streaming

Collaborative Prompt Editing

---

# Testing

Verify

Authentication

Authorization

Reconnect

Heartbeat

Streaming

Large Messages

Concurrency

Multiple Clients

Rate Limits

Failure Recovery

---

# Common Mistakes

❌ No authentication

❌ No heartbeat

❌ No reconnect

❌ In-memory connection state only

❌ Broadcasting everything

❌ Sending huge payloads

❌ No cleanup

❌ Missing rate limits

---

# Review Checklist

□ Auth implemented

□ Authorization checked

□ Heartbeats enabled

□ Redis configured

□ Reconnect supported

□ Logging enabled

□ Monitoring configured

□ Tests written

---

# Definition of Done

✓ Secure

✓ Scalable

✓ Observable

✓ Tested

✓ Production ready