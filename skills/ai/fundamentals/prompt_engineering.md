# Skill

Prompt Engineering

Version: 1.0

---

# Goal

Design reliable, maintainable, testable, and production-ready prompts that consistently produce high-quality outputs.

Prompt engineering is a software engineering discipline.

It is not prompt hacking.

Treat prompts as production code.

---

# When to Load

Load this skill whenever

- Building AI applications
- Creating AI assistants
- Designing RAG systems
- Building agents
- Implementing tool calling
- Creating workflows
- Optimizing model quality

---

# Prerequisites

- llm_basics.md

---

# Core Principle

A prompt is an interface between your application and an LLM.

Good prompts reduce

- Hallucinations
- Cost
- Latency
- Ambiguity

while increasing

- Reliability
- Consistency
- Accuracy
- Maintainability

---

# Prompt Architecture

A production prompt should contain

System Role

↓

Objective

↓

Context

↓

Constraints

↓

Tools (if available)

↓

Output Format

↓

Examples

↓

User Input

Never mix all instructions into one paragraph.

---

# Prompt Hierarchy

Models generally prioritize

1. System Prompt

↓

2. Developer Instructions

↓

3. User Prompt

↓

4. Retrieved Context

↓

5. Conversation History

Design prompts with this hierarchy in mind.

---

# Prompt Components

## System Prompt

Defines

Identity

Responsibilities

Behavior

Restrictions

Tone

Never include task-specific information here.

---

## Context

Provide only information required for the current task.

Good

Relevant documentation

Retrieved chunks

API schemas

Business rules

Bad

Entire database

Full chat history

Large irrelevant files

---

## Constraints

Explicitly define boundaries.

Examples

Never invent facts.

Do not answer outside supplied context.

Return JSON only.

Never expose internal reasoning.

Ask for clarification if required information is missing.

Constraints improve consistency.

---

## Output Format

Always define the expected output.

Preferred

JSON

Markdown

XML

Tables

Schemas

Avoid

Free-form responses

Ambiguous formatting

---

## Examples

Use few-shot examples only when

Output format is complex

Reasoning style matters

Classification labels require consistency

Do not overuse examples.

---

# Prompt Design Principles

Prompts should be

Specific

Modular

Deterministic

Reusable

Version Controlled

Easy to Evaluate

Provider Agnostic

---

# Prompt Patterns

## Zero-Shot

Provide only instructions.

Best for

Simple tasks

---

## One-Shot

Provide one example.

Useful when

Output style matters.

---

## Few-Shot

Provide multiple examples.

Useful for

Classification

Extraction

Formatting

Avoid unnecessary examples.

---

## Role Prompting

Assign a role.

Example

"You are a Senior Backend Engineer."

Roles improve consistency when aligned with the task.

---

## Constraint Prompting

Clearly define limitations.

Examples

Never fabricate information.

Return valid JSON.

Do not explain your reasoning.

---

## Step-Based Prompting

Break complex tasks into ordered steps.

Useful for

Planning

Analysis

Debugging

Multi-stage workflows

---

## Retrieval-Augmented Prompting

Inject retrieved knowledge into the prompt.

Never rely on model memory for proprietary information.

---

## Tool-Aware Prompting

Inform the model about available tools.

Describe

Capabilities

Limitations

Expected usage

Avoid describing implementation details.

---

# Prompt Templates

Separate prompts from application code.

Preferred structure

prompts/

summarization.md

classification.md

coding.md

review.md

retrieval.md

analysis.md

Store prompts as versioned assets.

---

# Prompt Versioning

Every production prompt should have

Version

Author

Date

Purpose

Expected Output

Evaluation Results

Treat prompts like APIs.

---

# Prompt Testing

Test prompts against

Typical inputs

Edge cases

Invalid inputs

Long inputs

Missing context

Prompt injection attempts

Regression datasets

Never deploy untested prompts.

---

# Prompt Evaluation

Measure

Accuracy

Consistency

Latency

Cost

Hallucination Rate

Format Validity

Task Success Rate

Prompt quality should be measurable.

---

# Prompt Chaining

Break large workflows into smaller prompts.

Example

Analyze

↓

Plan

↓

Generate

↓

Validate

↓

Refine

Smaller prompts are easier to debug.

---

# Context Engineering

Provide

Relevant

Current

Minimal

Verified

context.

Avoid

Duplicate information

Conflicting information

Excessive context

Irrelevant documents

Context quality matters more than quantity.

---

# Prompt Injection Defense

Never trust user input.

Protect against

Instruction overrides

Hidden prompts

Malicious URLs

Tool abuse

Prompt leakage

Validate all external inputs.

---

# Common Prompt Structures

## Classification

Task

↓

Labels

↓

Examples

↓

Input

↓

Output

---

## Extraction

Schema

↓

Rules

↓

Input

↓

JSON Output

---

## Summarization

Objective

↓

Audience

↓

Length

↓

Context

↓

Output

---

## Code Generation

Requirements

↓

Constraints

↓

Architecture

↓

Output Format

↓

Code

---

# Production Best Practices

- Keep prompts concise.
- Use explicit constraints.
- Define output schemas.
- Separate prompts from code.
- Version every prompt.
- Evaluate prompt quality continuously.
- Prefer structured outputs.
- Minimize token usage.
- Use retrieval instead of large prompts.

---

# Anti-Patterns

❌ Giant prompts

❌ Hidden business logic

❌ Prompt duplication

❌ Hardcoded prompts

❌ Unstructured outputs

❌ Conflicting instructions

❌ Prompt concatenation throughout the codebase

❌ No version control

❌ No evaluation

---

# Metrics

Track

- Prompt Success Rate
- Hallucination Rate
- JSON Validity
- Cost
- Latency
- User Satisfaction
- Evaluation Score

---

# Testing

Verify

- Prompt correctness
- Schema compliance
- Output consistency
- Injection resistance
- Provider compatibility
- Regression performance

---

# Review Checklist

□ Prompt has a single responsibility

□ Instructions are explicit

□ Constraints are defined

□ Context is minimal

□ Output format specified

□ Prompt is versioned

□ Evaluation exists

□ Injection risks addressed

□ Stored outside application code

---

# Related Skills

- llm_basics.md
- structured_outputs.md
- model_selection.md
- prompt_templates.md
- guardrails.md
- evaluation.md
- tool_calling.md

---

# Definition of Done

A production prompt is complete only if

✓ Purpose is clearly defined

✓ Constraints are explicit

✓ Output format is deterministic

✓ Prompt is versioned

✓ Evaluation is implemented

✓ Injection risks are mitigated

✓ Stored separately from application code

✓ Tested across representative datasets

✓ Provider independent

✓ Maintainable