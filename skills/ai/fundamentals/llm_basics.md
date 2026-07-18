# Skill

LLM Fundamentals

Version: 1.0

---

# Goal

Understand how Large Language Models (LLMs) work so that AI systems are designed using engineering principles instead of trial-and-error prompting.

An LLM is a probabilistic next-token prediction engine.

It does not think, understand, or know facts like a human.

Everything else in AI engineering builds upon this principle.

---

# When to Load

Load this skill whenever

- Building an AI application
- Designing prompts
- Selecting models
- Building agents
- Implementing RAG
- Using tool calling
- Evaluating model outputs
- Debugging AI behavior

This skill is foundational.

---

# Prerequisites

None.

This is the starting point for every AI engineer.

---

# What is an LLM?

A Large Language Model is a neural network trained to predict the next token in a sequence.

Input

↓

Tokenizer

↓

Tokens

↓

Transformer Layers

↓

Probability Distribution

↓

Next Token

↓

Repeat

The model predicts one token at a time until a stopping condition is reached.

---

# Important Principle

LLMs generate text.

They do not retrieve knowledge from a database.

They do not execute code.

They do not browse the internet.

They do not verify facts.

Those capabilities are added through

- Retrieval
- Tool Calling
- Agents
- Memory
- External APIs

---

# Tokens

Models do not read words.

They read tokens.

Examples

"Hello world"

↓

["Hello", " world"]

Longer prompts produce more tokens.

More tokens increase

- Cost
- Latency
- Context usage

Optimize prompts for token efficiency.

---

# Context Window

The context window is the maximum number of tokens a model can process.

It includes

System Prompt

+

Conversation History

+

Retrieved Context

+

User Input

+

Model Output

Everything shares the same context budget.

---

# Context Management

Never send unnecessary information.

Prefer

Relevant context

Short prompts

Filtered retrieval

Summarized memory

Avoid

Entire databases

Entire conversations

Duplicate context

Irrelevant documents

Good context engineering often improves quality more than changing models.

---

# Sampling

The model predicts probabilities for every possible next token.

Sampling determines which token is selected.

Common strategies

Greedy

Temperature

Top-K

Top-P

Production systems usually use deterministic settings whenever possible.

---

# Temperature

Controls randomness.

Lower

↓

More deterministic

Higher

↓

More creative

Typical values

0.0–0.2

Extraction

Classification

Structured outputs

0.3–0.7

General assistants

0.8–1.2

Creative writing

Use the lowest value that satisfies the task.

---

# Top-P

Limits token selection to the smallest probability mass.

Useful for balancing creativity and consistency.

Generally tune either Temperature or Top-P, not both aggressively.

---

# Hallucinations

Hallucination occurs when a model confidently generates incorrect or fabricated information.

Causes

Missing context

Poor prompts

Outdated training data

Ambiguous questions

Overly broad tasks

Reduce hallucinations with

Retrieval

Guardrails

Structured outputs

Verification

Evaluation

Never assume hallucinations can be eliminated completely.

---

# Model Knowledge

A model has

Training knowledge

+

Prompt context

It does not automatically know

Current events

Private company data

Your database

Uploaded files

User-specific information

Use RAG or tools when external knowledge is required.

---

# Reasoning Models

Some models allocate additional computation before producing an answer.

Advantages

Better planning

Better coding

Better mathematics

Improved complex reasoning

Trade-offs

Higher latency

Higher cost

Choose reasoning models only when task complexity justifies them.

---

# Inference

Inference is the process of generating outputs from a trained model.

Factors affecting inference

Model size

Hardware

Context length

Output length

Sampling strategy

Provider infrastructure

Optimize inference before changing providers.

---

# Prompt Hierarchy

Models typically prioritize instructions in this order

System Prompt

↓

Developer Instructions

↓

User Prompt

↓

Retrieved Context

↓

Conversation History

Understand this hierarchy when debugging unexpected behavior.

---

# Model Limitations

LLMs cannot

Guarantee correctness

Understand intent perfectly

Remember previous sessions by default

Verify facts independently

Access external systems without tools

Provide deterministic answers in every scenario

Design systems that account for these limitations.

---

# Capabilities

LLMs are excellent at

Summarization

Code generation

Classification

Extraction

Translation

Reasoning

Planning

Content generation

Question answering

Transformation

Leverage strengths instead of forcing unsuitable tasks.

---

# Weaknesses

LLMs struggle with

Precise arithmetic

Long-term memory

Up-to-date information

Strict determinism

Multi-step workflows without orchestration

Complex business rules

High-precision factual guarantees

Use external systems where appropriate.

---

# Provider Differences

Different providers optimize for different goals.

Examples

OpenAI

Balanced general-purpose performance

Anthropic

Strong reasoning and long-context understanding

Google Gemini

Large context windows and multimodal capabilities

Groq

Very low-latency inference

Ollama

Local inference and privacy

DeepSeek

Strong coding and reasoning performance

Select providers based on workload requirements, not popularity.

---

# Cost

Inference cost depends on

Input tokens

Output tokens

Model selection

Context length

Request frequency

Streaming

Monitor token usage continuously.

---

# Latency

Latency is influenced by

Prompt size

Model complexity

Reasoning effort

Network

Provider infrastructure

Output length

Reduce latency through efficient context engineering and model selection.

---

# Security

Never send

Secrets

Passwords

Private keys

Sensitive customer data

Personally identifiable information unless required and protected

Treat prompts as potentially visible to providers.

---

# AI System Architecture

A production AI application typically consists of

Application

↓

Prompt Builder

↓

Memory

↓

Retrieval

↓

Tool Calling

↓

LLM Provider

↓

Structured Output Parser

↓

Business Logic

↓

Response

Avoid coupling business logic directly to LLM responses.

---

# Engineering Principles

Design AI systems that are

Modular

Observable

Provider-agnostic

Evaluated

Secure

Version-controlled

Testable

Maintainable

Replaceable

---

# Common Misconceptions

❌ LLMs think like humans

❌ Bigger models always perform better

❌ More prompt text always improves results

❌ Hallucinations can be fully eliminated

❌ One model is best for every task

❌ AI applications only require prompt engineering

Modern AI systems combine models with retrieval, tools, memory, orchestration, and evaluation.

---

# Best Practices

- Keep prompts concise and explicit.
- Use structured outputs whenever possible.
- Retrieve only relevant context.
- Measure quality with evaluations.
- Choose models based on workload.
- Version prompts and model configurations.
- Track latency, cost, and reliability.
- Build for provider portability.

---

# Anti-Patterns

❌ Giant prompts

❌ No evaluation

❌ Provider lock-in

❌ Blind trust in model outputs

❌ Ignoring token costs

❌ Embedding business logic in prompts

❌ Mixing prompts throughout the codebase

---

# Metrics

Track

- Token Usage
- Cost per Request
- Latency
- Success Rate
- Hallucination Rate
- User Satisfaction
- Evaluation Score

---

# Testing

Verify

- Prompt correctness
- Model selection
- Output consistency
- Structured output validation
- Failure handling
- Provider fallback
- Cost and latency budgets

---

# Review Checklist

□ Appropriate model selected

□ Context optimized

□ Prompt concise

□ Temperature justified

□ Structured outputs used

□ Cost measured

□ Latency acceptable

□ Hallucination risk considered

□ Provider abstraction maintained

□ Evaluation implemented

---

# Related Skills

- prompt_engineering.md
- structured_outputs.md
- model_selection.md
- tool_calling.md
- retrieval.md
- evaluation.md

---

# Definition of Done

An AI system is production-ready only if

✓ Model choice is justified

✓ Context is optimized

✓ Outputs are validated

✓ Hallucination risks are mitigated

✓ Cost is monitored

✓ Latency meets requirements

✓ Provider abstraction exists

✓ Evaluation is continuous

✓ Architecture is modular

✓ Security requirements are satisfied