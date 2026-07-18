# DOM (Document Object Model)

Version: 1.0

---

# Goal

Understand the Document Object Model (DOM) as the browser's live, in-memory representation of an HTML document. Learn how it is created, manipulated, observed, rendered, and optimized in modern frontend applications.

The DOM is not HTML.

HTML is parsed once.

The DOM is a dynamic object tree that changes throughout the lifetime of a webpage.

Every frontend framework ultimately interacts with the DOM.

---

# When to Use

DOM knowledge is required for

- browser applications
- React
- Vue
- Angular
- Next.js
- event handling
- animations
- accessibility
- rendering optimization
- debugging

Understanding the DOM is essential for frontend engineering.

---

# Problem

Without understanding the DOM

- UI updates become inefficient
- rendering slows
- unnecessary reflows occur
- memory leaks increase
- event handling becomes inconsistent
- framework behavior appears "magical"

---

# Solution

HTML

↓

Parser

↓

DOM

↓

JavaScript

↓

Rendering

↓

User Interface

Treat the DOM as a mutable object graph rather than static markup.

---

# Core Principles

Tree Structure

↓

Nodes

↓

Traversal

↓

Mutation

↓

Rendering

↓

Optimization

---

# DOM Creation

```
HTML

↓

Tokenizer

↓

Parser

↓

DOM Tree
```

The parser creates a node for every HTML element.

---

# DOM Tree

```
Document

↓

HTML

├── Head

└── Body
    ├── Header
    ├── Main
    └── Footer
```

Every element becomes a node.

---

# Node Types

Common node types

- Document
- Element
- Text
- Comment
- Attribute
- DocumentFragment

Everything in the DOM inherits from `Node`.

---

# Relationships

Every node has

- parent
- children
- siblings

Example

```
Parent

├── Child

├── Child

└── Child
```

---

# Traversal

Common traversal methods

- parentNode
- children
- firstElementChild
- lastElementChild
- nextElementSibling
- previousElementSibling

Traversal allows efficient navigation through the tree.

---

# Selecting Elements

Preferred APIs

```javascript
document.querySelector()
document.querySelectorAll()
```

Other methods

- getElementById
- getElementsByClassName
- getElementsByTagName

Prefer CSS selector-based APIs for flexibility.

---

# DOM Manipulation

Common operations

- createElement
- append
- prepend
- remove
- replaceWith
- cloneNode

Manipulate nodes rather than rebuilding large sections unnecessarily.

---

# Attributes vs Properties

Attributes

- HTML source values

Properties

- live JavaScript values

Example

```html
<input value="Hello">
```

Changing the property does not always change the original attribute.

---

# DocumentFragment

Use

```
DocumentFragment
```

to batch multiple DOM insertions.

Benefits

- fewer reflows
- improved performance

---

# Layout and Reflow

DOM changes may trigger

Style

↓

Layout

↓

Paint

↓

Composite

Frequent layout calculations reduce performance.

---

# Reflow

Occurs when geometry changes

Examples

- width
- height
- font-size
- display

Reflow is expensive.

---

# Repaint

Occurs when appearance changes without affecting layout

Examples

- color
- background
- visibility

Generally cheaper than reflow.

---

# Event System

Events propagate through the DOM.

```
Capture

↓

Target

↓

Bubble
```

Understanding propagation is essential for scalable event handling.

---

# Event Delegation

Instead of attaching many listeners

```
Parent

↓

Single Listener

↓

Children
```

Benefits

- lower memory usage
- better performance
- easier maintenance

---

# MutationObserver

Observe DOM changes efficiently.

Use for

- widgets
- analytics
- dynamic content
- browser extensions

Avoid polling.

---

# Shadow DOM

Provides encapsulation.

```
Host

↓

Shadow Root

↓

Private DOM
```

Used by

- Web Components
- design systems
- reusable UI libraries

---

# Virtual DOM

Libraries like React maintain

```
Virtual DOM

↓

Diff

↓

Minimal DOM Updates
```

The Virtual DOM is not the browser DOM.

It is an optimization layer.

---

# Real DOM vs Virtual DOM

| Real DOM | Virtual DOM |
|----------|-------------|
| Browser implementation | JavaScript representation |
| Expensive updates | Cheap comparisons |
| Live tree | Temporary tree |
| Used for rendering | Used for diffing |

---

# Accessibility Tree

The browser derives an Accessibility Tree from the DOM.

Semantic HTML improves

- screen readers
- keyboard navigation
- assistive technologies

---

# Memory

Detached DOM nodes can remain in memory if references persist.

Common causes

- forgotten event listeners
- global variables
- closures
- caches

Always clean up unused nodes.

---

# Engineering Decisions

## Event Delegation

Preferred for dynamic lists.

---

## DocumentFragment

Use for batch insertions.

---

## querySelector

Preferred over older APIs for most use cases.

---

## Minimize DOM Mutations

Batch updates whenever possible.

---

# Runtime Architecture

```
HTML

↓

DOM

↓

JavaScript

↓

DOM Mutation

↓

Style

↓

Layout

↓

Paint

↓

Composite
```

---

# Performance

Optimize

DOM size

↓

DOM depth

↓

layout frequency

↓

paint operations

↓

memory usage

↓

event listeners

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Event Delegation | Efficient | Requires propagation awareness |
| Direct DOM Updates | Simple | Can become expensive at scale |
| Virtual DOM | Efficient diffing | Additional abstraction layer |
| Shadow DOM | Encapsulation | More complex debugging |

---

# Common Failures

- deeply nested DOM trees
- excessive DOM mutations
- forced synchronous layouts
- detached DOM nodes
- too many event listeners
- querying the DOM repeatedly inside loops

---

# Best Practices

- Keep the DOM shallow.
- Batch updates.
- Use event delegation.
- Cache frequently accessed elements.
- Minimize layout-triggering operations.
- Remove unused listeners.
- Profile using DevTools.

---

# Anti-Patterns

❌ Rebuilding large DOM trees unnecessarily

❌ Querying the DOM repeatedly inside animation loops

❌ Thousands of event listeners on similar elements

❌ Ignoring cleanup for removed nodes

❌ Modifying layout properties repeatedly inside loops

---

# Real-World Examples

## React

Maintains a Virtual DOM, computes differences between renders, and applies only the minimal required changes to the browser DOM.

---

## Vue

Uses a reactive rendering system that updates the DOM efficiently based on dependency tracking.

---

## Chrome

Represents every HTML document as a DOM tree, combining it with the CSSOM to generate the Render Tree for layout and painting.

---

## Web Components

Use the Shadow DOM to encapsulate markup, styles, and behavior, preventing conflicts with the surrounding page.

---

## GitHub

Uses event delegation and incremental DOM updates to efficiently handle large, interactive interfaces without excessive listener registration.

---

# Related Skills

- html.md
- css.md
- javascript.md
- browser.md
- rendering.md
- events.md
- react.md
- performance.md

---

# Definition of Done

An engineer understands the DOM when they can

✓ Explain how HTML is parsed into a DOM tree

✓ Traverse and manipulate DOM nodes efficiently

✓ Distinguish attributes from properties

✓ Understand the relationship between DOM mutations and rendering

✓ Use event propagation and delegation effectively

✓ Optimize DOM updates to reduce layout and paint costs

✓ Explain the purpose of MutationObserver and Shadow DOM

✓ Compare the real DOM with Virtual DOM implementations

✓ Prevent memory leaks caused by detached nodes and event listeners

✓ Treat the DOM as the browser's live object model rather than static HTML