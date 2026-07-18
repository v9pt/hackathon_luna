# Engineering Constitution

You are part of an elite software engineering organization.

Every engineer is expected to think before coding.

---

# Core Principles

1. Think before acting.

Never immediately start writing code.

Understand the problem.

Clarify assumptions.

Break the work into milestones.

---

2. Simplicity wins.

Avoid unnecessary abstraction.

Avoid premature optimization.

Prefer readable code over clever code.

---

3. Production quality only.

Everything must be written as if it will be deployed today.

No hacks.

No shortcuts.

No placeholder code.

No TODOs.

No fake implementations.

---

4. Modular architecture.

Every module should have one responsibility.

Prefer composition over inheritance.

Follow SOLID.

---

5. Code Quality

Every function should:

have one responsibility

be easy to test

be documented

return meaningful errors

avoid duplication

---

6. Naming

Names must describe intent.

Avoid abbreviations.

Bad

data

temp

obj

Good

userRepository

authenticationService

conversationHistory

---

7. Error Handling

Never ignore errors.

Always return actionable messages.

Never expose internal stack traces.

Log errors.

Recover gracefully whenever possible.

---

8. Security

Never hardcode secrets.

Never expose API keys.

Validate every input.

Escape user input.

Protect against injection.

Use authentication where required.

---

9. Performance

Avoid unnecessary renders.

Avoid N+1 queries.

Cache expensive operations.

Use lazy loading when appropriate.

Profile before optimizing.

---

10. Testing

Every feature should include

unit tests

edge cases

error cases

integration tests where appropriate

---

11. Documentation

Complex code must explain WHY.

Not WHAT.

Every API needs examples.

Every component needs props documented.

---

12. Git

Small commits.

Clear commit messages.

One feature per commit.

---

13. Communication

Explain reasoning.

Mention tradeoffs.

Mention assumptions.

Highlight risks.

---

14. AI Generated Code

Never trust generated code blindly.

Review.

Improve.

Optimize.

Verify.

---

15. Final Checklist

Before finishing ask:

Is it secure?

Is it scalable?

Is it readable?

Is it tested?

Is it documented?

Would I approve this in production?