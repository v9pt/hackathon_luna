# Accessibility

Version: 1.0

---

# Goal

Understand accessibility (a11y) as the practice of designing and building web applications that are usable by everyone, including people with disabilities, across different devices, browsers, and assistive technologies.

Accessibility is not an optional feature.

It is a core quality attribute of every production application.

Good accessibility improves usability for all users.

---

# When to Use

Accessibility principles apply to

- web applications
- dashboards
- ecommerce
- SaaS platforms
- design systems
- forms
- mobile web
- PWAs
- documentation

Every user interface should be accessible by default.

---

# Problem

Poor accessibility leads to

- inaccessible navigation
- unusable forms
- poor keyboard support
- screen reader failures
- legal compliance issues
- frustrated users

Accessibility cannot be added after development.

It must be built into the engineering process.

---

# Solution

Semantic HTML

↓

Keyboard Navigation

↓

Accessible Names

↓

Focus Management

↓

Screen Readers

↓

Testing

↓

Inclusive User Experience

---

# Core Principles

Perceivable

↓

Operable

↓

Understandable

↓

Robust

These are the four WCAG principles (POUR).

---

# WCAG Overview

The Web Content Accessibility Guidelines define internationally recognized standards.

Three conformance levels

- A
- AA
- AAA

Most production systems target

AA

---

# Semantic HTML

Prefer native elements

```
<button>
<nav>
<header>
<main>
<footer>
<label>
<form>
```

instead of generic containers.

Semantic HTML provides accessibility with minimal additional work.

---

# Accessible Names

Every interactive element must have an accessible name.

Examples

- visible label
- aria-label
- aria-labelledby

Users of assistive technologies rely on these names.

---

# Forms

Every form control should include

- label
- helper text
- validation feedback
- required indicators
- error messaging

Example

```html
<label for="email">Email</label>
<input id="email" type="email">
```

Never rely on placeholders as labels.

---

# Keyboard Navigation

Every interactive element should be usable without a mouse.

Support

- Tab
- Shift + Tab
- Enter
- Space
- Escape
- Arrow Keys

Keyboard access is essential.

---

# Focus Management

Visible focus indicators should never be removed.

When dialogs, menus, or modals open

- move focus appropriately
- trap focus where necessary
- restore focus when closing

---

# Screen Readers

Common screen readers

- NVDA
- JAWS
- VoiceOver
- TalkBack

Screen readers interpret the Accessibility Tree rather than visual layout.

---

# ARIA

Accessible Rich Internet Applications (ARIA) supplement semantic HTML.

Examples

- aria-label
- aria-labelledby
- aria-describedby
- aria-expanded
- aria-live
- aria-hidden

Use ARIA only when native HTML cannot provide the required semantics.

Rule:

No ARIA is better than bad ARIA.

---

# Landmarks

Important landmarks include

- banner
- navigation
- main
- complementary
- contentinfo

These allow users to navigate quickly.

---

# Images

Meaningful images

Require

```
alt
```

Decorative images

Should use

```
alt=""
```

Never omit alt attributes.

---

# Color Contrast

Maintain sufficient contrast.

Minimum recommendation

- Normal text: 4.5:1
- Large text: 3:1

Avoid communicating information through color alone.

---

# Accessible Tables

Tables should include

- caption
- thead
- tbody
- th
- scope attributes when appropriate

Use tables only for tabular data.

---

# Live Regions

Use

```
aria-live
```

for dynamic updates

Examples

- notifications
- chat messages
- validation feedback

Avoid interrupting users unnecessarily.

---

# Motion

Respect

```
prefers-reduced-motion
```

Reduce or disable non-essential animations.

---

# Accessible Dialogs

Dialogs should

- receive focus on open
- trap keyboard focus
- close with Escape
- restore focus when dismissed

---

# Error Handling

Errors should be

- announced
- associated with fields
- descriptive
- recoverable

Users should understand how to fix problems.

---

# Accessibility Testing

Test with

- keyboard only
- screen readers
- browser accessibility tools
- automated linters
- manual testing

Automation alone cannot guarantee accessibility.

---

# Engineering Decisions

## Semantic HTML

Always preferred.

---

## Native Controls

Use before creating custom widgets.

---

## ARIA

Use only when necessary.

---

## Keyboard Support

Required for all interactive components.

---

# Runtime Architecture

```
HTML

↓

Accessibility Tree

↓

Assistive Technology

↓

User Interaction
```

The Accessibility Tree is generated from the DOM and semantic information.

---

# Performance

Accessibility improvements generally have minimal runtime cost while significantly improving usability.

Prioritize

- semantic structure
- logical focus order
- accessible names
- efficient keyboard interaction

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Native elements | Built-in accessibility | Less visual flexibility |
| Custom components | Highly customizable | Must recreate accessibility behavior |
| ARIA | Extends semantics | Easy to misuse |
| Automated testing | Fast feedback | Cannot detect every issue |

---

# Common Failures

- missing labels
- inaccessible dialogs
- hidden focus indicators
- low contrast
- keyboard traps
- missing alt text
- placeholder-only forms
- clickable divs

---

# Best Practices

- Start with semantic HTML.
- Support keyboard users.
- Maintain visible focus.
- Write descriptive labels.
- Test with screen readers.
- Respect user preferences.
- Use ARIA sparingly.
- Include accessibility reviews in every feature.

---

# Anti-Patterns

❌ Removing focus outlines

❌ Using `<div>` as a button

❌ Placeholder instead of label

❌ Missing alt attributes

❌ Keyboard-inaccessible menus

❌ Auto-playing content without controls

❌ Color-only status indicators

---

# Real-World Examples

## GOV.UK Design System

Built around accessibility-first principles, emphasizing semantic HTML, keyboard support, clear language, and progressive enhancement.

---

## GitHub

Implements keyboard navigation, accessible dialogs, semantic landmarks, and comprehensive screen reader support across a large-scale application.

---

## React Aria

Provides accessible behavior for complex UI components while preserving flexibility in styling and rendering.

---

## Chrome Accessibility Tree

Transforms the DOM into an accessibility representation consumed by screen readers and other assistive technologies.

---

# Related Skills

- html.md
- css.md
- events.md
- dom.md
- responsive_design.md
- react.md
- design_systems.md

---

# Definition of Done

An engineer understands accessibility when they can

✓ Apply the POUR principles of WCAG

✓ Build interfaces using semantic HTML before ARIA

✓ Design forms with accessible labels, validation, and error handling

✓ Support complete keyboard navigation and focus management

✓ Create accessible dialogs, menus, and interactive components

✓ Ensure sufficient color contrast and readable typography

✓ Write meaningful alternative text and accessible names

✓ Test applications with keyboard navigation, screen readers, and automated tools

✓ Integrate accessibility into the development lifecycle rather than treating it as an afterthought

✓ Treat accessibility as a fundamental aspect of software quality and inclusive engineering