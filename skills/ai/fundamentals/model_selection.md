# Skill

Model Selection

Version: 1.0

---

# Goal

Select the most appropriate AI model for a given workload by balancing quality, latency, cost, context window, reasoning ability, and operational constraints.

Model selection is an engineering decision.

Not a popularity contest.

---

# When to Load

Load this skill whenever

- Building AI applications
- Designing agent workflows
- Building RAG
- Creating chatbots
- Designing multi-agent systems
- Optimizing inference cost
- Reducing latency
- Choosing AI providers

---

# Prerequisites

- llm_basics.md
- prompt_engineering.md
- structured_outputs.md

---

# Core Principle

Choose the smallest, fastest, and cheapest model that reliably solves the problem.

Avoid overengineering.

---

# Selection Factors

Evaluate models based on

Reasoning Ability

↓

Accuracy

↓

Latency

↓

Cost

↓

Context Window

↓

Tool Calling

↓

Structured Outputs

↓

Multimodal Support

↓

Reliability

↓

Availability

Never choose a model based on benchmarks alone.

---

# Model Categories

## General Models

Balanced performance.

Best for

Chat

Summarization

Translation

Code Generation

Classification

---

## Reasoning Models

Designed for

Planning

Complex coding

Math

Logic

Multi-step reasoning

Trade-off

Higher latency

Higher cost

---

## Small Models

Advantages

Fast

Cheap

Low latency

High throughput

Use for

Classification

Extraction

Routing

Simple chat

Moderation

---

## Large Models

Advantages

Better reasoning

Better creativity

Longer context

More robust

Use only when task complexity requires it.

---

# Model Capability Matrix

Evaluate every candidate for

- Coding
- Reasoning
- Math
- Long Context
- Tool Calling
- Structured Outputs
- Vision
- Audio
- Cost
- Latency

Maintain an internal comparison table for your organization.

---

# Context Window

Larger context windows are useful for

Large documents

Long conversations

Legal

Research

Enterprise search

Avoid paying for large context if unnecessary.

---

# Latency

Latency depends on

Model size

Reasoning effort

Provider infrastructure

Prompt length

Output length

Network

Low-latency workloads include

Autocomplete

Customer support

Voice assistants

Interactive coding

---

# Cost

Inference cost depends on

Input tokens

Output tokens

Model pricing

Reasoning mode

Retries

Streaming

Monitor cost continuously.

---

# Reasoning vs Standard Models

Use reasoning models for

Architecture

Debugging

Planning

Algorithms

Research

Use standard models for

Extraction

Formatting

Summaries

Classification

Simple Q&A

Do not waste reasoning models on trivial tasks.

---

# Multimodal Support

Some models support

Images

PDFs

Video

Audio

Screenshots

Select multimodal models only when required.

---

# Tool Calling

Choose models that natively support

Function Calling

Structured Outputs

JSON Mode

Tool Invocation

These features improve reliability.

---

# Provider Comparison

Examples

OpenAI

General-purpose, strong ecosystem.

Anthropic

Excellent reasoning, coding, long-context tasks.

Gemini

Strong multimodal capabilities and very large context windows.

Groq

Optimized for low-latency inference.

Ollama

Local deployment, privacy, offline use.

DeepSeek

Strong coding and reasoning at competitive cost.

Model capabilities evolve rapidly; validate against current documentation before deployment.

---

# Routing Strategy

One application may use multiple models.

Example

User Request

↓

Router

↓

Simple Task?

↓

Small Model

↓

Complex Task?

↓

Reasoning Model

↓

Vision?

↓

Multimodal Model

↓

Coding?

↓

Code-Optimized Model

Use routing to reduce cost.

---

# Fallback Strategy

Implement

Primary Model

↓

Secondary Model

↓

Local Model

↓

Graceful Failure

Never rely on a single provider.

---

# Hybrid AI Systems

Combine specialized models.

Example

Classification

↓

Small Model

↓

Retrieval

↓

Embedding Model

↓

Reasoning

↓

Large Model

↓

Formatting

↓

Small Model

Optimize every stage independently.

---

# Embedding Models

Embedding models are not chat models.

Select embedding models based on

Retrieval quality

Latency

Cost

Language support

Dimensionality

Maintain version compatibility with stored vectors.

---

# Local vs Cloud

Cloud

Pros

Latest models

Scalability

Managed infrastructure

Cons

Network dependency

Cost

Data residency concerns

---

Local

Pros

Privacy

Offline support

Predictable cost

Cons

Hardware requirements

Maintenance

Potentially lower capability

Choose based on business requirements.

---

# Fine-Tuned Models

Consider fine-tuning only when

Prompt engineering is insufficient

Large labeled datasets exist

Consistent task repetition

Performance gains justify maintenance

Do not fine-tune prematurely.

---

# Evaluation Before Adoption

Test models using

Accuracy

Latency

Cost

Hallucination rate

Tool reliability

JSON validity

User satisfaction

Select based on measured performance.

---

# Provider Abstraction

Never couple business logic to one provider.

Application

↓

Provider Interface

↓

OpenAI

Anthropic

Gemini

Ollama

DeepSeek

This simplifies migration and resilience.

---

# Security

Review

Data handling

Retention policies

Regional availability

Compliance

Rate limits

Supported authentication

Ensure provider choices align with organizational requirements.

---

# Best Practices

- Benchmark models on your own tasks.
- Separate chat, embedding, and reasoning models.
- Implement routing.
- Measure latency and cost.
- Keep provider interfaces abstract.
- Periodically re-evaluate model choices.

---

# Anti-Patterns

❌ One model for everything

❌ Choosing the newest model by default

❌ Ignoring latency

❌ Ignoring token pricing

❌ No fallback provider

❌ No evaluation

❌ Vendor lock-in

---

# Metrics

Track

- Accuracy
- Cost per Request
- Latency
- Throughput
- Tool Success Rate
- JSON Validity
- Hallucination Rate
- User Satisfaction

---

# Testing

Verify

- Provider compatibility
- Routing logic
- Fallback behavior
- Cost budgets
- Latency budgets
- Structured output support
- Tool calling support

---

# Review Checklist

□ Model choice justified

□ Cost evaluated

□ Latency acceptable

□ Context window appropriate

□ Tool support verified

□ Structured outputs supported

□ Provider abstraction implemented

□ Fallback configured

□ Benchmarked on real workloads

---

# Related Skills

- llm_basics.md
- prompt_engineering.md
- structured_outputs.md
- provider_abstraction.md
- latency.md
- cost_optimization.md

---

# Definition of Done

A model selection strategy is production-ready only if

✓ Workloads are classified

✓ Models are benchmarked

✓ Cost is monitored

✓ Latency targets are met

✓ Provider abstraction exists

✓ Fallback providers are configured

✓ Selection rationale is documented

✓ Periodic re-evaluation is planned