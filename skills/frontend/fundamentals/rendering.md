# Rendering

Version: 1.0

---

# Goal

Understand the browser rendering pipeline, from parsing resources to displaying pixels on the screen. Learn how style calculation, layout, paint, compositing, animations, and rendering optimizations work together to create responsive user interfaces.

Rendering is the process of transforming HTML, CSS, and JavaScript into pixels.

Every frontend optimization ultimately targets one or more stages of this pipeline.

---

# When to Use

Rendering knowledge is essential for

- React
- Next.js
- animations
- performance optimization
- Core Web Vitals
- accessibility
- browser debugging
- responsive UI
- game engines
- dashboards

---

# Problem

Without understanding rendering

- pages feel slow
- animations stutter
- scrolling becomes janky
- layout shifts occur
- React rerenders become expensive
- performance optimizations become guesswork

---

# Solution

HTML

↓

DOM

↓

CSSOM

↓

Render Tree

↓

Style

↓

Layout

↓

Paint

↓

Composite

↓

Display

Understand every stage before attempting optimization.

---

# Core Principles

Parse

↓

Style

↓

Layout

↓

Paint

↓

Composite

↓

Frame

Every visible update follows this sequence.

---

# Complete Rendering Pipeline

```
HTML

↓

DOM

↓

CSS

↓

CSSOM

↓

Render Tree

↓

Style Calculation

↓

Layout

↓

Paint

↓

Compositing

↓

GPU

↓

Display
```

---

# DOM

Represents

document structure.

Generated from HTML.

---

# CSSOM

Represents

styles.

Generated from CSS.

---

# Render Tree

The browser combines

DOM

+

CSSOM

↓

Render Tree

Invisible elements

```
display: none
```

are excluded.

---

# Style Calculation

The browser determines

- computed styles
- inheritance
- cascade
- specificity
- CSS variables

Style recalculation occurs after relevant DOM or CSS changes.

---

# Layout (Reflow)

Calculates

- element position
- dimensions
- geometry

Layout affects

- width
- height
- margins
- fonts
- flex
- grid

Layout is expensive.

---

# Paint

Converts layout information into pixels.

Paint includes

- text
- borders
- gradients
- shadows
- images
- backgrounds

---

# Compositing

The GPU combines painted layers into the final frame.

Properties that commonly stay in the compositor include

- transform
- opacity

These are preferred for smooth animations.

---

# Frame Rendering

Modern displays typically refresh at

60 FPS

Frame budget

```
1000 ms

÷

60

≈

16.67 ms
```

All rendering work for a frame should ideally complete within this budget.

---

# Rendering Invalidation

Changing elements invalidates parts of the pipeline.

Example

Changing

```
color
```

↓

Paint

Changing

```
width
```

↓

Layout

↓

Paint

↓

Composite

Understanding invalidation avoids unnecessary work.

---

# Layout Thrashing

Occurs when code repeatedly alternates

Read Layout

↓

Write Layout

↓

Read Layout

↓

Write Layout

forcing synchronous recalculations.

Batch reads and writes separately.

---

# Forced Synchronous Layout

Example

Read

↓

Modify

↓

Read

↓

Modify

This blocks rendering.

Avoid layout reads immediately after writes.

---

# Layers

Some elements become independent compositor layers.

Common triggers

- transform
- opacity
- position: fixed
- will-change

Layers improve animation performance but consume GPU memory.

---

# GPU Acceleration

GPU excels at

- transforms
- opacity
- compositing

CPU handles

- layout
- style
- scripting

Choose animation properties accordingly.

---

# Animations

Prefer animating

- transform
- opacity

Avoid animating

- width
- height
- left
- top
- margin

These often trigger layout.

---

# requestAnimationFrame

Use

```
requestAnimationFrame()
```

for visual updates synchronized with the browser's rendering cycle.

Avoid using timers for animations.

---

# Idle Work

Use

```
requestIdleCallback()
```

for low-priority tasks when browser support and workload allow.

Examples

- analytics
- cleanup
- preloading

---

# Core Web Vitals

Google measures rendering quality using

## Largest Contentful Paint (LCP)

Measures

loading performance.

Target

< 2.5 s

---

## Cumulative Layout Shift (CLS)

Measures

visual stability.

Target

< 0.1

---

## Interaction to Next Paint (INP)

Measures

interaction responsiveness.

Target

< 200 ms

---

# Reducing LCP

Improve by

- optimizing images
- preloading critical assets
- reducing server latency
- minimizing render-blocking resources
- streaming HTML

---

# Reducing CLS

Prevent layout shifts by

- reserving image dimensions
- reserving ad space
- avoiding late font swaps
- avoiding unexpected DOM insertion

---

# Improving INP

Reduce

- long tasks
- synchronous JavaScript
- excessive rerenders
- heavy event handlers

---

# Render Blocking

Resources that delay rendering

- CSS
- synchronous JavaScript

Optimize loading strategy.

---

# Lazy Loading

Delay non-critical resources

Examples

- images
- videos
- components
- routes

Improves initial rendering.

---

# React Rendering

React rendering consists of

State Change

↓

Virtual DOM

↓

Diff

↓

Commit

↓

DOM Update

↓

Browser Rendering Pipeline

React does not replace browser rendering.

It minimizes DOM changes before the browser renders.

---

# Hydration

Server-rendered HTML

↓

Browser

↓

JavaScript

↓

Hydration

↓

Interactive UI

Hydration attaches behavior without rebuilding the page.

---

# Streaming Rendering

Modern frameworks stream HTML progressively.

Benefits

- faster perceived loading
- earlier interaction
- improved LCP

---

# Engineering Decisions

## GPU-Friendly Animations

Preferred.

---

## Batch DOM Updates

Recommended.

---

## Avoid Layout Thrashing

Always.

---

## Minimize Repaints

Recommended.

---

## Lazy Loading

Load only what is necessary.

---

# Runtime Architecture

```
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

↓

GPU

↓

Display
```

---

# Performance

Optimize

DOM complexity

↓

style recalculation

↓

layout

↓

paint

↓

GPU compositing

↓

JavaScript execution

↓

network loading

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| GPU animations | Smooth performance | Increased GPU memory usage |
| Many compositor layers | Faster animations | Higher memory consumption |
| Lazy loading | Faster initial load | Additional loading logic |
| Streaming rendering | Better perceived performance | More complex implementation |

---

# Common Failures

- layout thrashing
- excessive paints
- long JavaScript tasks
- large render trees
- blocking CSS
- synchronous rendering
- oversized images
- unnecessary rerenders

---

# Best Practices

- Keep the DOM small.
- Animate transforms and opacity.
- Batch DOM mutations.
- Avoid forced synchronous layouts.
- Optimize Core Web Vitals.
- Measure before optimizing.
- Use browser profiling tools.
- Stream and lazy load where appropriate.

---

# Anti-Patterns

❌ Animating layout properties

❌ Reading layout repeatedly during writes

❌ Large synchronous rendering tasks

❌ Blocking rendering with unnecessary scripts

❌ Ignoring Core Web Vitals

❌ Excessive repaint regions

❌ Unbounded component rerenders

---

# Real-World Examples

## React

Uses a Virtual DOM to calculate the minimal set of changes before updating the real DOM, reducing unnecessary rendering work while still relying on the browser's rendering pipeline.

---

## Chrome Rendering Engine

Builds the Render Tree, performs style calculation, layout, painting, and GPU compositing for every visible frame.

---

## Next.js

Improves perceived rendering performance through server-side rendering, streaming, selective hydration, and route-level code splitting.

---

## Google Search

Optimizes Largest Contentful Paint and Cumulative Layout Shift by prioritizing critical content and reserving layout space for dynamic elements.

---

## Figma

Maintains a highly interactive interface by minimizing layout work, batching updates, and leveraging GPU compositing for smooth panning and zooming.

---

# Related Skills

- browser.md
- dom.md
- css.md
- javascript.md
- performance.md
- react.md
- nextjs.md

---

# Definition of Done

An engineer understands browser rendering when they can

✓ Explain the complete rendering pipeline from HTML to pixels

✓ Distinguish style calculation, layout, paint, and compositing

✓ Identify which CSS and DOM changes invalidate each rendering stage

✓ Prevent layout thrashing and forced synchronous layouts

✓ Optimize animations using GPU-friendly properties

✓ Improve Core Web Vitals including LCP, CLS, and INP

✓ Explain how React integrates with the browser's rendering process

✓ Profile rendering performance using browser developer tools

✓ Design interfaces that remain responsive under heavy workloads

✓ Treat rendering as the central performance model for modern frontend engineering