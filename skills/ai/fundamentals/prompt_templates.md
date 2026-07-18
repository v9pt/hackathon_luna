# Skill

Prompt Templates

Version: 1.0

---

# Goal

Design reusable, version-controlled prompt templates that are modular, maintainable, testable, and independent of application logic.

Prompt templates should be treated as reusable software assets.

Never hardcode prompts throughout the codebase.

---

# When to Load

Load this skill whenever

- Building AI applications
- Designing agents
- Building RAG
- Creating workflows
- Developing coding assistants
- Building chatbots
- Maintaining prompt libraries

---

# Prerequisites

- llm_basics.md
- prompt_engineering.md
- structured_outputs.md

---

# Core Principle

Application Code

↓

Prompt Template

↓

Variables

↓

Rendered Prompt

↓

LLM

Business logic should never contain prompt text.

---

# Why Templates

Templates provide

Consistency

Maintainability

Version Control

Reuse

Testing

Provider Independence

Scalability

---

# Repository Structure

prompts/

system/

assistant/

rag/

coding/

review/

analysis/

summarization/

classification/

translation/

evaluation/

Each template should have one responsibility.

---

# Naming Convention

Good

summarize_document.md

review_code.md

generate_tests.md

retrieve_context.md

classify_email.md

Bad

prompt1.md

new_prompt.md

latest.md

---

# Template Structure

Every prompt should include

Metadata

↓

Purpose

↓

Variables

↓

Instructions

↓

Constraints

↓

Output Format

↓

Examples (optional)

↓

Version

---

# Metadata

Every prompt should define

Name

Version

Owner

Purpose

Last Updated

Compatible Models

Expected Output

Related Skills

---

# Variables

Templates should accept explicit variables.

Example

{{user_input}}

{{context}}

{{conversation_history}}

{{language}}

{{style}}

{{tools}}

Avoid concatenating strings manually.

---

# Static vs Dynamic Content

Static

Role

Instructions

Constraints

Output Format

Dynamic

User Query

Retrieved Context

Examples

Memory

Tool Results

Separate the two.

---

# Prompt Composition

Compose prompts from reusable building blocks.

System Prompt

+

Task Template

+

Retrieved Context

+

Conversation Memory

+

User Input

↓

Final Prompt

Avoid monolithic prompts.

---

# Template Inheritance

Allow templates to extend base templates.

Example

Base Assistant

↓

Coding Assistant

↓

Python Reviewer

↓

Security Reviewer

Reuse common instructions.

---

# Prompt Library

Maintain categorized prompts.

Examples

Coding

Documentation

Summarization

Classification

Extraction

Translation

Planning

Debugging

Testing

Review

---

# Environment-Specific Prompts

Support

Development

Testing

Production

Experimentation

Different environments may require different prompts.

---

# Prompt Versioning

Every template should include

Version

Change Log

Migration Notes

Evaluation Results

Never overwrite production prompts.

---

# A/B Testing

Compare

Prompt A

↓

Evaluation

↓

Prompt B

↓

Evaluation

↓

Deploy Better Version

Measure before replacing prompts.

---

# Prompt Registry

Every application should maintain

Prompt Name

Version

Owner

Status

Evaluation Score

Supported Models

Deprecation Date

Treat prompts as deployable assets.

---

# Provider Compatibility

Avoid provider-specific syntax whenever possible.

Keep templates portable.

Application

↓

Prompt Template

↓

Provider Adapter

↓

LLM

Supports provider abstraction.

---

# Security

Never embed

Secrets

API Keys

Private Data

Credentials

Business-sensitive information

Templates should contain instructions only.

---

# Localization

Support

Language Variables

Region

Formatting

Units

Date Formats

Avoid duplicating templates for every language.

---

# Prompt Testing

Test

Rendering

Variables

Missing Variables

Long Context

Injection Resistance

Output Quality

Regression

Every template should have test cases.

---

# Prompt Lifecycle

Design

↓

Review

↓

Implement

↓

Evaluate

↓

Deploy

↓

Monitor

↓

Improve

↓

Deprecate

Prompts should evolve continuously.

---

# Documentation

Each template should document

Purpose

Variables

Expected Inputs

Expected Outputs

Compatible Models

Known Limitations

---

# Best Practices

- Store prompts outside source code.
- Use variables instead of string concatenation.
- Version every prompt.
- Keep templates focused.
- Reuse common components.
- Document all variables.
- Test prompts before deployment.
- Evaluate continuously.

---

# Anti-Patterns

❌ Hardcoded prompts

❌ Prompt duplication

❌ String concatenation

❌ No versioning

❌ Monolithic prompts

❌ Provider-specific templates

❌ No documentation

❌ No testing

---

# Metrics

Track

- Prompt Success Rate
- Evaluation Score
- Rendering Errors
- Variable Coverage
- Hallucination Rate
- Cost
- Latency

---

# Testing

Verify

- Template rendering
- Variable substitution
- Version compatibility
- Prompt quality
- Provider compatibility
- Injection resistance

---

# Review Checklist

□ Template documented

□ Variables defined

□ Version assigned

□ Prompt reusable

□ Output format documented

□ Rendering tested

□ Security reviewed

□ Evaluation completed

---

# Related Skills

- prompt_engineering.md
- structured_outputs.md
- model_selection.md
- guardrails.md
- evaluation.md

---

# Definition of Done

A prompt template is production-ready only if

✓ Stored separately from application code

✓ Variables documented

✓ Versioned

✓ Tested

✓ Evaluated

✓ Reusable

✓ Provider independent

✓ Security reviewed

✓ Maintainable