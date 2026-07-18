# CSS

Version: 1.0

---

# Goal

Understand CSS as the browser's styling, layout, rendering, and visual presentation engine, enabling engineers to build responsive, accessible, performant, and maintainable user interfaces.

CSS is not merely about appearance—it controls how documents are laid out, rendered, animated, and adapted across devices and user preferences.

Every modern frontend framework ultimately relies on CSS.

---

# When to Use

CSS applies whenever

- styling HTML
- designing layouts
- creating responsive interfaces
- building design systems
- implementing themes
- optimizing rendering performance
- animating interfaces
- supporting accessibility

---

# Problem

Poor CSS leads to

- broken layouts
- inconsistent UI
- difficult maintenance
- slow rendering
- accessibility issues
- excessive specificity
- visual regressions

Large applications require CSS architecture rather than isolated styles.

---

# Solution

Structure

↓

Cascade

↓

Layout

↓

Responsive Design

↓

Performance

↓

Maintainability

CSS should describe presentation while remaining predictable and scalable.

---

# Core Principles

Cascade

↓

Inheritance

↓

Layout

↓

Responsiveness

↓

Performance

↓

Maintainability

Understand how browsers calculate styles before writing CSS.

---

# CSS Rendering Pipeline

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

Layout

↓

Paint

↓

Composite
```

CSS participates directly in browser rendering.

---

# CSSOM

The browser converts stylesheets into the

CSS Object Model.

```
CSS

↓

Parser

↓

CSSOM

↓

Render Tree
```

The DOM and CSSOM combine to create the Render Tree.

---

# The Cascade

Style priority is determined by

Origin

↓

Importance

↓

Specificity

↓

Source Order

Understanding the cascade eliminates most CSS bugs.

---

# Specificity

Priority increases approximately as

Element

↓

Class

↓

Attribute

↓

Pseudo-class

↓

ID

↓

Inline Style

Avoid relying on high specificity.

---

# Inheritance

Some properties inherit automatically

Examples

- color
- font-family
- line-height

Others do not

- margin
- padding
- border
- width
- height

Understanding inheritance reduces redundant CSS.

---

# Box Model

Every element consists of

```
Margin

↓

Border

↓

Padding

↓

Content
```

Use

```css
box-sizing: border-box;
```

for predictable sizing.

---

# Display Types

Common display values

- block
- inline
- inline-block
- flex
- grid
- none

Display determines formatting behavior.

---

# Positioning

Types

- static
- relative
- absolute
- fixed
- sticky

Choose the simplest positioning model possible.

---

# Flexbox

Designed for

- one-dimensional layouts
- alignment
- spacing
- navigation
- toolbars
- forms

Best for distributing items along a single axis.

---

# Grid

Designed for

- two-dimensional layouts
- dashboards
- application shells
- galleries
- responsive grids

Grid controls both rows and columns.

---

# Responsive Design

Adapt layouts using

- media queries
- flexible units
- fluid typography
- responsive images
- container queries

Design for varying screen sizes rather than fixed resolutions.

---

# Container Queries

Instead of viewport size

Respond to

Container Size

↓

Component Layout

Container queries improve reusable component design.

---

# Units

Prefer

- rem
- em
- %
- fr
- vw
- vh

Avoid excessive fixed pixel values.

---

# Custom Properties

Example

```css
:root {
    --primary: #2563eb;
}
```

Benefits

- theming
- consistency
- runtime updates
- design systems

---

# Typography

Control

- font-family
- font-size
- line-height
- letter-spacing
- font-weight

Readable typography improves usability.

---

# Color Systems

Organize colors using design tokens

```
Primary

↓

Secondary

↓

Success

↓

Warning

↓

Danger

↓

Neutral
```

Avoid arbitrary colors throughout the codebase.

---

# Animations

Prefer

- transform
- opacity

Avoid animating

- width
- height
- top
- left

Transforms remain on the compositor thread.

---

# Browser Performance

Rendering stages

Style

↓

Layout

↓

Paint

↓

Composite

Layout and paint are expensive.

Composite is comparatively inexpensive.

---

# Responsive Images

Use

- srcset
- sizes
- picture
- lazy loading

Serve appropriate assets for each device.

---

# Accessibility

Respect user preferences

- prefers-reduced-motion
- prefers-color-scheme
- sufficient contrast
- readable font sizes
- visible focus states

Accessibility extends beyond HTML.

---

# CSS Architecture

Common methodologies

## BEM

Block

↓

Element

↓

Modifier

Predictable naming.

---

## ITCSS

Layer styles from generic to specific.

Useful for large projects.

---

## Utility-First

Examples

- Tailwind CSS

Compose interfaces using reusable utility classes.

---

## CSS Modules

Local scope.

Reduces selector conflicts.

---

# Design Systems

Centralize

- spacing
- typography
- colors
- elevation
- radii
- shadows
- breakpoints

Consistency improves maintainability.

---

# Engineering Decisions

## Flexbox

Best for

one-dimensional layouts.

---

## Grid

Best for

page layouts and dashboards.

---

## Utility CSS

Fast development.

Reduced custom CSS.

---

## Component CSS

Better encapsulation.

---

## CSS Variables

Recommended.

Enable runtime theming.

---

# Runtime Architecture

```
CSS

↓

Parser

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

↓

Display
```

---

# Performance

Optimize

style recalculation

↓

layout

↓

paint

↓

compositing

↓

bundle size

↓

maintainability

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Flexbox | Simple alignment | One-dimensional only |
| Grid | Powerful layouts | More complex |
| Utility-first | Fast development | Verbose markup |
| Component CSS | Encapsulation | More files |
| CSS Variables | Dynamic themes | Browser support considerations for legacy environments |

---

# Common Failures

- excessive specificity
- !important everywhere
- fixed-width layouts
- deep selector nesting
- duplicated styles
- inconsistent spacing
- unnecessary reflows

---

# Best Practices

- Prefer semantic layout.
- Use Flexbox and Grid appropriately.
- Keep specificity low.
- Use CSS variables.
- Design mobile-first.
- Minimize layout shifts.
- Respect accessibility preferences.
- Build reusable design tokens.

---

# Anti-Patterns

❌ Excessive `!important`

❌ Deep descendant selectors

❌ Pixel-perfect fixed layouts

❌ Inline styles for reusable components

❌ Mixing layout strategies inconsistently

❌ Animating layout properties

❌ Hardcoded colors throughout the application

---

# Real-World Examples

## Tailwind CSS

Provides a utility-first approach that emphasizes composability, consistency, and rapid UI development while reducing large custom stylesheets.

---

## GitHub

Uses a centralized design system with reusable spacing, typography, color tokens, and component primitives to maintain consistency across a large application.

---

## GOV.UK Design System

Prioritizes accessible typography, responsive layouts, and progressive enhancement through carefully structured CSS.

---

## Chrome Rendering Engine

Builds the CSSOM, combines it with the DOM into the Render Tree, then performs layout, paint, and compositing to render every page.

---

## Modern React Applications

Regardless of CSS-in-JS, CSS Modules, Tailwind, or plain CSS, every styling solution ultimately generates CSS that the browser parses and renders.

---

# Related Skills

- html.md
- javascript.md
- browser.md
- rendering.md
- responsive_design.md
- accessibility.md
- design_systems.md
- performance.md

---

# Definition of Done

An engineer understands CSS when they can

✓ Explain the cascade, specificity, and inheritance

✓ Build responsive layouts using Flexbox and Grid

✓ Understand the browser rendering pipeline from CSSOM to compositing

✓ Optimize CSS for rendering performance

✓ Design scalable CSS architectures for large applications

✓ Build accessible, responsive interfaces that respect user preferences

✓ Create reusable design systems using tokens and custom properties

✓ Minimize layout shifts, unnecessary paints, and expensive reflows

✓ Choose appropriate styling methodologies for different project sizes

✓ Treat CSS as the browser's rendering engine rather than simply a styling language