# HTML

Version: 1.0

---

# Goal

Understand HTML as the structural language of the Web that defines document semantics, accessibility, browser parsing, SEO, and the foundation upon which CSS, JavaScript, and modern frontend frameworks operate.

HTML is not a programming language.

It is the document model every browser understands.

Every frontend framework ultimately produces HTML.

---

# When to Use

HTML is used for

- web pages
- web applications
- emails
- documentation
- dashboards
- landing pages
- forms
- embedded applications

Every browser begins by parsing HTML.

---

# Problem

Without proper HTML

- accessibility suffers
- SEO decreases
- browser rendering slows
- JavaScript becomes harder
- maintainability declines
- screen readers fail
- forms become unreliable

Modern frameworks cannot compensate for poor document structure.

---

# Solution

Design documents using semantic structure.

HTML should communicate

- meaning
- hierarchy
- relationships
- intent

before styling or interactivity.

---

# Core Principles

Structure

↓

Semantics

↓

Accessibility

↓

Performance

↓

Maintainability

HTML describes content—not appearance.

---

# Browser Architecture

```
Request

↓

HTML

↓

Parser

↓

DOM

↓

CSSOM

↓

Render Tree

↓

Layout

↓

Paint

↓

Composite
```

Everything begins with HTML.

---

# HTML Document

```
<!DOCTYPE html>

↓

<html>

↓

<head>

↓

<body>

↓

Elements

↓

DOM
```

The browser converts every element into DOM nodes.

---

# HTML Parsing

The browser

Downloads HTML

↓

Parses tokens

↓

Creates DOM Nodes

↓

Executes blocking scripts

↓

Continues parsing

↓

Completes DOM

Understanding parsing explains rendering performance.

---

# DOM Generation

Example

```html
<body>
    <h1>Hello</h1>
    <p>World</p>
</body>
```

becomes

```
Document

↓

HTML

↓

Body

↓

H1

↓

P
```

JavaScript interacts with this tree.

---

# Semantic HTML

Prefer

```
<header>
<nav>
<main>
<section>
<article>
<aside>
<footer>
```

instead of

```
<div>
<div>
<div>
```

Semantics improve

- accessibility
- SEO
- maintainability
- readability

---

# Document Outline

Example

```
h1

↓

h2

↓

h3
```

Avoid skipping heading levels.

Headings communicate hierarchy.

---

# Common Semantic Elements

Document

- html
- head
- body

Content

- main
- section
- article
- aside

Navigation

- nav

Media

- figure
- figcaption

Lists

- ul
- ol
- li

Text

- p
- strong
- em
- blockquote

Forms

- form
- label
- input
- textarea
- button

Tables

- table
- thead
- tbody
- tr
- td
- th

Each has semantic meaning.

---

# Accessibility

Semantic HTML provides

- landmarks
- navigation
- labels
- keyboard support
- screen reader context

Use native elements before ARIA.

Example

Prefer

```html
<button>
```

instead of

```html
<div onclick="">
```

---

# Forms

Good forms include

- labels
- validation
- autocomplete
- correct input types
- required fields

Example

```html
<input type="email">
```

instead of

```html
<input type="text">
```

Native controls improve usability.

---

# Metadata

The head contains

- title
- description
- viewport
- charset
- icons
- Open Graph
- canonical URLs

Metadata affects

- SEO
- sharing
- browser behavior

---

# Structured Data

Use

JSON-LD

for

- products
- articles
- organizations
- events
- recipes

Structured data improves search engine understanding.

---

# Images

Every image should include

- alt text
- width
- height
- loading strategy

Example

```html
<img
  src=""
  alt=""
  loading="lazy">
```

---

# Links

Use descriptive links.

Good

```
Read React Documentation
```

Poor

```
Click Here
```

Links should describe destinations.

---

# Tables

Use tables only for tabular data.

Never for page layout.

Always include

- thead
- tbody
- th

---

# Performance

Optimize HTML by

- minimizing DOM depth
- lazy loading media
- preloading critical resources
- avoiding unnecessary wrappers
- reducing blocking scripts

Smaller DOMs render faster.

---

# SEO

Semantic HTML improves

- indexing
- crawling
- snippets
- accessibility

Search engines understand structured documents.

---

# Security

Avoid

- inline JavaScript
- inline event handlers
- unsafe HTML injection

Always sanitize user-generated HTML.

---

# Engineering Decisions

## Semantic Elements

Recommended.

Improves accessibility.

---

## Native Controls

Preferred over custom implementations.

---

## Minimal DOM

Recommended.

Improves rendering performance.

---

## Progressive Enhancement

HTML should function before JavaScript loads.

---

# Runtime Architecture

```
HTML

↓

Parser

↓

DOM

↓

CSS

↓

JavaScript

↓

Interactive UI
```

---

# Performance

Optimize

DOM size

↓

semantic correctness

↓

parser efficiency

↓

resource loading

↓

accessibility

↓

SEO

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Semantic HTML | Accessibility, SEO | Requires planning |
| Generic divs | Flexible | Poor semantics |
| Native forms | Reliable | Less customization |
| Custom components | Flexible UI | Higher maintenance |

---

# Common Failures

- div-only layouts
- missing labels
- missing alt attributes
- multiple h1 elements without structure
- tables for layout
- inline JavaScript
- deeply nested DOM trees

---

# Best Practices

- Use semantic elements.
- Prefer native controls.
- Minimize DOM complexity.
- Label every form field.
- Provide alternative text.
- Structure headings logically.
- Include essential metadata.
- Keep HTML clean and readable.

---

# Anti-Patterns

❌ Using `<div>` for everything

❌ Missing form labels

❌ Using tables for layout

❌ Inline styles

❌ Inline event handlers

❌ Empty alt attributes for meaningful images

❌ Skipping heading hierarchy

---

# Real-World Examples

## Wikipedia

Highly semantic HTML enables excellent accessibility, fast rendering, and strong SEO despite minimal styling.

---

## GOV.UK Design System

Uses native HTML elements wherever possible, prioritizing accessibility, progressive enhancement, and long-term maintainability.

---

## GitHub

Employs semantic HTML landmarks, accessible forms, descriptive navigation, and well-structured documents to support millions of users.

---

## Next.js

Regardless of React components, every page ultimately renders semantic HTML that browsers parse into the DOM.

---

## React

JSX compiles into HTML element creation. Understanding HTML semantics remains essential even when using component frameworks.

---

# Related Skills

- css.md
- javascript.md
- browser.md
- dom.md
- rendering.md
- accessibility.md
- web_standards.md

---

# Definition of Done

An engineer understands HTML when they can

✓ Structure documents using semantic elements

✓ Build accessible forms and navigation

✓ Create SEO-friendly pages with proper metadata

✓ Understand how browsers parse HTML into the DOM

✓ Optimize HTML for rendering performance

✓ Use native elements before custom implementations

✓ Design clean, maintainable document structures

✓ Integrate HTML effectively with CSS and JavaScript

✓ Apply progressive enhancement principles

✓ Treat HTML as the structural foundation of every modern web application