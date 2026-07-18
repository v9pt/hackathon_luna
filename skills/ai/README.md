# AI Engineering Skill Library

Version: 1.0

---

# Purpose

This library contains reusable engineering knowledge for designing, building, evaluating, deploying, and operating modern AI systems.

Unlike traditional software engineering, AI systems are probabilistic. Every implementation should prioritize reliability, observability, evaluation, safety, and maintainability.

Each document in this library represents a focused engineering capability.

Load only the skills required for the current task.

---

# Engineering Philosophy

AI systems should be

Reliable

Deterministic where possible

Observable

Secure

Cost Efficient

Low Latency

Composable

Provider Agnostic

Production Ready

Never build AI features by directly calling an LLM from application code.

Every AI system should have a well-defined architecture with clear separation between prompting, retrieval, orchestration, memory, evaluation, and model providers.

---

# Skill Categories

## Fundamentals

Core concepts required for every AI application.

- llm_basics.md
- prompt_engineering.md
- structured_outputs.md
- model_selection.md
- prompt_templates.md

---

## Retrieval-Augmented Generation (RAG)

Knowledge retrieval and context engineering.

- ingestion.md
- parsing.md
- chunking.md
- embeddings.md
- vector_databases.md
- retrieval.md
- hybrid_search.md
- reranking.md
- prompt_builder.md
- memory.md
- evaluation.md
- guardrails.md
- streaming.md

---

## Agents

Autonomous and tool-using AI systems.

- tool_calling.md
- function_calling.md
- mcp.md
- langgraph.md
- multi_agent.md
- planning.md
- reasoning.md
- agent_memory.md
- orchestration.md

---

## Operations

Operating AI systems in production.

- observability.md
- ai_security.md
- latency.md
- cost_optimization.md
- hallucinations.md
- provider_abstraction.md

---

# Learning Path

Follow this order when learning AI engineering.

LLM Basics

↓

Prompt Engineering

↓

Structured Outputs

↓

Model Selection

↓

Tool Calling

↓

Function Calling

↓

RAG

↓

Memory

↓

Agents

↓

Evaluation

↓

Observability

↓

Production Deployment

Each topic builds upon the previous one.

---

# Skill Routing Guide

## Simple AI Chatbot

Load

- llm_basics
- prompt_engineering
- model_selection

---

## AI Assistant

Load

- llm_basics
- prompt_engineering
- structured_outputs
- tool_calling
- function_calling

---

## RAG System

Load

- embeddings
- vector_databases
- retrieval
- reranking
- prompt_builder
- evaluation
- guardrails

---

## Enterprise Search

Load

- ingestion
- parsing
- chunking
- embeddings
- retrieval
- hybrid_search
- reranking

---

## AI Agent

Load

- tool_calling
- planning
- reasoning
- orchestration
- agent_memory

---

## Multi-Agent System

Load

- planning
- orchestration
- multi_agent
- mcp
- observability

---

## AI Workflow Automation

Load

- function_calling
- tool_calling
- planning
- orchestration

---

## AI Coding Assistant

Load

- prompt_engineering
- structured_outputs
- tool_calling
- reasoning
- evaluation

---

## Production AI Service

Load

- provider_abstraction
- observability
- ai_security
- latency
- cost_optimization
- evaluation

---

# AI Development Workflow

Every AI feature should follow this process.

Understand the problem

↓

Determine if AI is actually required

↓

Choose the appropriate model

↓

Design prompts

↓

Define structured outputs

↓

Add tools if necessary

↓

Add retrieval if external knowledge is needed

↓

Implement memory if conversations require context

↓

Evaluate quality

↓

Optimize latency

↓

Optimize cost

↓

Deploy

↓

Monitor

↓

Continuously evaluate

Never skip evaluation before deployment.

---

# Decision Matrix

Need external knowledge?

↓

Use Retrieval (RAG)

Need API calls?

↓

Use Tool Calling

Need deterministic outputs?

↓

Use Structured Outputs

Need long conversations?

↓

Use Memory

Need autonomous workflows?

↓

Use Agents

Need multiple specialists?

↓

Use Multi-Agent Systems

Need model portability?

↓

Use Provider Abstraction

Need production monitoring?

↓

Use Observability

Need hallucination reduction?

↓

Use RAG + Evaluation + Guardrails

---

# AI Engineering Standards

Every AI implementation should

Separate prompts from code

Version prompts

Validate model outputs

Use structured outputs whenever possible

Support multiple providers

Track token usage

Track latency

Measure cost

Measure quality

Log failures

Handle provider outages

Protect sensitive data

Support retries

Never assume model responses are correct.

---

# Evaluation Principles

Every production AI system should measure

Accuracy

Faithfulness

Relevance

Latency

Cost

Reliability

Hallucination Rate

Success Rate

User Satisfaction

Evaluation is mandatory.

---

# Technology Recommendations

Preferred Orchestration

- LangGraph

Preferred Protocol

- MCP

Preferred Embedding Models

- OpenAI
- Voyage
- Jina
- BAAI
- Ollama

Preferred Vector Databases

- Qdrant
- pgvector
- Pinecone
- Weaviate

Preferred Providers

- OpenAI
- Anthropic
- Gemini
- Groq
- Ollama
- DeepSeek

Preferred Evaluation

- Ragas
- DeepEval
- LangSmith

---

# Skill Dependencies

LLM Basics

↓

Prompt Engineering

↓

Structured Outputs

↓

Tool Calling

↓

Function Calling

↓

Retrieval

↓

Memory

↓

Planning

↓

Reasoning

↓

Agent Orchestration

↓

Evaluation

↓

Operations

Higher-level skills assume mastery of lower-level concepts.

---

# Definition of Done

An AI feature is complete only if

✓ Model selection is justified

✓ Prompts are versioned

✓ Outputs are structured

✓ Hallucination risk is addressed

✓ Evaluation is implemented

✓ Latency is acceptable

✓ Cost is measured

✓ Security is reviewed

✓ Observability is configured

✓ Provider abstraction exists

✓ Documentation is updated

---

# Future Skills

This library is expected to grow with

- Vision Models
- Speech Models
- Voice Agents
- Browser Agents
- Computer Use
- Reinforcement Learning
- Fine-Tuning
- Knowledge Graphs
- Federated AI
- On-Device AI
- AI Governance
- Synthetic Data
- AI Benchmarking

---

# Objective

This library exists to help engineers build reliable, scalable, secure, and production-ready AI systems using proven engineering practices rather than ad hoc prompting.