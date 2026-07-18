# SHARED ENGINEERING RULES

These rules apply to every engineer in the organization.

CEO

Architect

Research

Backend

Frontend

AI

QA

Every engineer must follow these standards.

---

# PRIMARY GOAL

Build production-quality software.

Not demos.

Not prototypes.

Not proof of concepts.

Assume every project may eventually reach production.

---

# THINK BEFORE CODING

Never immediately generate code.

First understand

• Business Problem

• User Goal

• Constraints

• Edge Cases

• Success Criteria

If requirements are unclear

Ask questions.

Never guess.

---

# CODE QUALITY

Write code that another engineer can understand in six months.

Prioritize

Readability

Maintainability

Testability

Simplicity

Avoid clever code.

---

# SINGLE RESPONSIBILITY

Every

Function

Class

Hook

Component

Module

Service

should have exactly one responsibility.

---

# FILE SIZE

Prefer

Components

<200 lines

Services

<300 lines

Functions

<40 lines

If larger

Refactor.

---

# NAMING

Names must describe intent.

Good

UserRepository

EmailService

GenerateInvoice

Bad

temp

data

obj

newData

abc

Never abbreviate unnecessarily.

---

# TYPE SAFETY

Always use

TypeScript

Python Type Hints

Interfaces

Schemas

Enums

Avoid

any

dynamic typing

magic values

---

# VALIDATION

Validate

Every API Input

Every Form

Every Query Parameter

Every Environment Variable

Never trust user input.

---

# ERROR HANDLING

Never silently fail.

Always

Catch

Log

Return meaningful errors

Recover when possible

Never expose internal stack traces.

---

# LOGGING

Log

Requests

Failures

Retries

Latency

Database Errors

Authentication Events

Never log

Passwords

JWT

Secrets

API Keys

Personal Data

---

# SECURITY

Never hardcode

Secrets

Passwords

API Keys

Tokens

Use

Environment Variables

Validate inputs.

Escape outputs.

Use least privilege.

---

# PERFORMANCE

Always think about

Caching

Pagination

Memoization

Lazy Loading

Background Jobs

Compression

Indexes

Measure before optimizing.

---

# TESTING

Every feature requires

Happy Path

Failure Path

Edge Cases

Validation Tests

Security Tests

Unit Tests

Integration Tests when appropriate.

---

# DOCUMENTATION

Every feature should explain

Why

Tradeoffs

Assumptions

Risks

Future improvements

Not just

What.

---

# GIT

One feature

One commit

Clear commit messages

Small PRs

Never mix unrelated changes.

---

# ACCESSIBILITY

Every interface must support

Keyboard Navigation

Screen Readers

Focus Indicators

Semantic HTML

Color Contrast

Responsive Design

---

# RESPONSIVENESS

Support

Mobile

Tablet

Desktop

Large Displays

Avoid fixed dimensions.

---

# AI GENERATED CODE

Never trust generated code.

Review

Improve

Test

Optimize

Document

---

# DEPENDENCIES

Before installing a package

Ask

Is it maintained?

Is it necessary?

Is there a native solution?

Does it increase bundle size?

Avoid dependency bloat.

---

# ARCHITECTURE

Prefer

Feature-based architecture

Reusable components

Dependency Injection

Composition

Loose coupling

Avoid

God classes

Circular dependencies

Deep nesting

Duplicated logic

---

# COMMUNICATION

Explain decisions.

Mention assumptions.

Mention risks.

Mention alternatives.

Never simply output code.

---

# DEFINITION OF DONE

A task is complete only if

✓ Requirements satisfied

✓ Code reviewed

✓ Typed

✓ Tested

✓ Accessible

✓ Responsive

✓ Secure

✓ Logged

✓ Documented

✓ Production ready

---

# ESCALATION

Escalate to Architect when

Architecture changes

Database changes

Authentication changes

Technology changes

Major dependencies

Escalate to CEO when

Requirements change

Timeline changes

Scope changes

Project risks

Never make major architectural decisions independently.

---

# OUTPUT FORMAT

Every response should end with

## Summary

## Files Changed

## Tests

## Risks

## Future Improvements