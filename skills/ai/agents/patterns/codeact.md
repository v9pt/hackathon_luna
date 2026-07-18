# Pattern

CodeAct

Version: 1.0

---

# Goal

Enable AI agents to solve complex tasks by generating, executing, observing, debugging, and refining executable code rather than relying solely on natural language reasoning.

The CodeAct pattern treats code as the primary medium for reasoning and action, allowing agents to leverage programming languages, interpreters, operating systems, and development tools as extensions of their cognitive process.

A production CodeAct system should produce safe, deterministic, observable, and recoverable execution while continuously improving through runtime feedback.

---

# When to Use

Use this pattern whenever

- Software engineering tasks
- Repository modification
- API integration
- Automation
- Data processing
- Infrastructure management
- Tool-heavy workflows
- Long-running engineering tasks
- Continuous debugging

---

# Problem

Traditional LLM agents

Reason

↓

Tool

↓

Reason

↓

Tool

are constrained by

- token limits
- natural language ambiguity
- repetitive reasoning
- limited computational capability

Many engineering problems are easier to solve through executable code.

---

# Solution

Treat generated code as executable reasoning.

```
Goal

↓

Plan

↓

Generate Code

↓

Execute

↓

Observe

↓

Debug

↓

Refine

↓

Complete
```

The interpreter becomes part of the reasoning loop.

---

# Core Principles

Reason

↓

Generate Code

↓

Execute

↓

Observe

↓

Improve

↓

Repeat

Execution should validate reasoning whenever possible.

---

# Architecture

```
Goal
 │
 ▼
Planner
 │
 ▼
Code Generator
 │
 ▼
Execution Environment
 │
 ▼
Observations
 │
 ▼
Debugger
 │
 ▼
Updated Plan
```

---

# Components

## Planner

Responsible for

- understanding objectives
- decomposing tasks
- selecting tools
- defining execution strategy

---

## Code Generator

Responsible for

- writing executable code
- creating scripts
- generating tests
- invoking APIs

---

## Execution Environment

Provides

- interpreter
- shell
- compiler
- filesystem
- APIs
- containers
- package managers

Execution environments should be isolated.

---

## Observation Engine

Collects

- stdout
- stderr
- exit codes
- test failures
- logs
- artifacts
- runtime metrics

---

## Debugger

Responsible for

- analyzing failures
- identifying root causes
- modifying code
- determining retry strategy

---

## Validator

Confirms

- correctness
- test success
- policy compliance
- task completion

---

# Execution Lifecycle

Goal

↓

Planning

↓

Generate Code

↓

Execute

↓

Observe

↓

Debug

↓

Refine

↓

Validate

↓

Complete

---

# Execution Modes

## Single Execution

Generate

↓

Run

↓

Finish

Suitable for deterministic automation.

---

## Iterative Execution

Generate

↓

Execute

↓

Observe

↓

Improve

↓

Repeat

Recommended default.

---

## Interactive Execution

Generate

↓

User Feedback

↓

Modify

↓

Execute

Useful for pair programming.

---

# Code Generation

Generated code should

- be modular
- be typed where appropriate
- include error handling
- be observable
- be testable

Avoid one-off scripts unless explicitly requested.

---

# Runtime Feedback

Collect

- exceptions
- compiler errors
- failing tests
- benchmark results
- performance metrics
- static analysis warnings

Feedback should directly influence the next iteration.

---

# Debugging Loop

Failure

↓

Diagnosis

↓

Code Modification

↓

Execution

↓

Validation

↓

Complete

Avoid repeating identical fixes.

---

# Environment Management

Support

- virtual environments
- containers
- isolated workspaces
- dependency installation
- reproducible builds

Environment state should be versioned when possible.

---

# Tool Integration

Common tools include

- Git
- Docker
- Kubernetes
- SQL
- Browsers
- REST APIs
- Build systems
- Package managers
- CI/CD systems

The execution environment should expose tools through well-defined interfaces.

---

# State Management

Maintain

- repository state
- execution history
- generated artifacts
- checkpoints
- environment configuration

Support resumable execution.

---

# Safety

Code execution should enforce

- sandboxing
- least privilege
- resource limits
- network restrictions
- filesystem permissions
- secret isolation

Never execute arbitrary code without policy validation.

---

# Pattern References

## ReAct

Code execution replaces many tool calls.

---

## Reflexion

Execution feedback guides future code generation.

---

## LLM Compiler

Compiled execution graphs can generate executable programs.

---

## Supervisor–Worker

Specialized workers execute independent code tasks.

---

# Engineering Decisions

## Local Execution

Fast

Recommended for development.

---

## Container Execution

Recommended default.

Provides isolation and reproducibility.

---

## Remote Execution

Useful for enterprise infrastructure.

Higher operational complexity.

---

## Distributed Execution

Suitable for large-scale automation.

---

# Runtime Architecture

```
Goal

↓

Planner

↓

Code Generator

↓

Sandbox

↓

Execution

↓

Debugger

↓

Validator

↓

Artifacts
```

---

# Performance

Optimize

code generation latency

↓

execution time

↓

test duration

↓

retry count

↓

resource utilization

↓

artifact reuse

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Local execution | Fast | Limited isolation |
| Containers | Safe | Startup overhead |
| Remote execution | Scalable | Network latency |
| Distributed execution | Massive scale | Operational complexity |

---

# Common Failures

- infinite execution loops
- dependency conflicts
- environment drift
- flaky tests
- unsafe code execution
- missing permissions
- repeated debugging cycles

---

# Best Practices

- Execute code in isolated environments.
- Generate tests alongside implementation.
- Validate every execution.
- Store execution artifacts.
- Keep execution deterministic.
- Use checkpoints for long workflows.
- Capture logs automatically.
- Prefer incremental modifications over rewrites.

---

# Anti-Patterns

❌ Executing code without validation

❌ Running with unrestricted permissions

❌ Ignoring runtime feedback

❌ Rewriting entire projects after small failures

❌ Hidden environment dependencies

❌ No testing before completion

❌ Treating generated code as inherently correct

---

# Comparison

| Pattern | Strength | Weakness |
|----------|----------|----------|
| ReAct | Flexible reasoning | Many LLM calls |
| ReWOO | Efficient planning | Limited runtime adaptation |
| Reflexion | Learns from failures | Reflection overhead |
| LLM Compiler | Optimized execution graphs | Higher implementation complexity |
| CodeAct | Direct executable reasoning | Requires secure execution environments |

---

# Real-World Examples

## Claude Code

Uses executable code, shell commands, Git operations, and test execution as the primary mechanism for solving software engineering tasks, iteratively refining implementations based on runtime feedback.

---

## OpenAI Codex

Generates and executes code within controlled environments, validating solutions through tests and execution results before presenting them.

---

## OpenHands

Operates inside a development workspace, modifying repositories, executing commands, running tests, and iteratively improving implementations through observation and debugging.

---

## SWE-Agent

Navigates repositories, edits source code, executes test suites, analyzes failures, and repeats until issues are resolved.

---

## Devin

Combines planning, coding, debugging, environment management, and validation into autonomous software engineering workflows that can span hours or days.

---

# Related Skills

- tool_calling.md
- state_management.md
- reflection.md
- self_correction.md
- orchestration.md
- workflows.md

---

# Related Patterns

- react.md
- reflexion.md
- rewoo.md
- llm_compiler.md
- supervisor_worker.md

---

# Definition of Done

A CodeAct implementation is production-ready only if

✓ Code generation is driven by explicit plans

✓ Execution occurs inside isolated, reproducible environments

✓ Runtime observations directly influence subsequent iterations

✓ Debugging is evidence-based rather than speculative

✓ Tests validate all meaningful code changes

✓ Execution artifacts, logs, and checkpoints are persisted

✓ Safety controls enforce sandboxing, permissions, and resource limits

✓ The system can resume from intermediate checkpoints after failures

✓ Code quality is continuously evaluated through automated validation

✓ The agent reliably solves engineering tasks by combining planning, executable code, runtime feedback, and iterative refinement