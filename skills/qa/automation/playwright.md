# Playwright

Version: 1.0

---

# Goal

Design and implement best-in-class Playwright solutions to maximize efficiency, performance, correctness, and user experience in production-grade systems.

Playwright is a key pillar in building robust, scalable applications.

---

# When to Use

Use this skill whenever:
- Designing systems that require Playwright
- Optimizing or refactoring existing Playwright implementations
- Establishing best practices and standards for Playwright
- Preemptively guarding against common pitfalls related to Playwright

---

# Problem

Without a structured and disciplined approach to Playwright:
- Systems suffer from performance bottlenecks
- Maintenance and extensibility overheads spike
- Bugs, memory leaks, or operational instability occur
- Developer velocity slows due to tech debt

---

# Solution

Establish a systematic, well-documented, and fully verified pattern for Playwright:
- Design for scalability and clean boundaries from day one
- Keep modules focused, decoupled, and easy to test
- Leverage modern tools and industry standards
- Verify behaviors comprehensively using automated test suites

---

# Core Principles

Understand the Lifecycle

↓

Design with Clean Abstractions

↓

Implement Defensively

↓

Verify Behaviors

↓

Optimize Responsibly

---

# Architecture & Flow

```text
Input / Event
      │
      ▼
Processing / Playwright Layer
      │
      ▼
Output / Update State
```

---

# Best Practices

- Enforce strict boundaries between layers
- Prefer simple, readable logic over premature optimizations
- Write modular, unit-testable components
- Handle edge cases, timeouts, and failures gracefully
- Log errors clearly with actionable diagnostics

---

# Common Failures

- Tight coupling with implementation details
- Lack of proper error handling or fallback modes
- Excessive complexity or over-engineering
- Missing test coverage for key boundaries
- Performance regressions due to unoptimized loops or requests

---

# Related Skills

- testing.md
- performance.md
- deployment.md

---

# Definition of Done

✓ The Playwright implementation functions correctly across all target scenarios
✓ Code is fully tested (unit, integration, and edge cases)
✓ Performance metrics remain within acceptable thresholds
✓ Error-handling patterns and fallbacks are implemented
✓ The solution is documented, clear, and ready for production deployment
