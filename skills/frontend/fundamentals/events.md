# Events

Version: 1.0

---

# Goal

Understand the browser event system, including event propagation, event listeners, delegation, pointer events, keyboard events, custom events, asynchronous execution, accessibility, and framework abstractions.

The event system is how browsers communicate user interaction to applications.

Modern frontend applications depend on efficient event handling for responsiveness, accessibility, and scalability.

---

# When to Use

Event knowledge is required for

- user interaction
- forms
- drag and drop
- React
- Vue
- Angular
- accessibility
- keyboard navigation
- touch interfaces
- animations
- realtime applications

---

# Problem

Without understanding events

- interactions become inconsistent
- memory leaks occur
- event listeners multiply unnecessarily
- accessibility suffers
- scrolling becomes janky
- applications become difficult to debug

---

# Solution

User Action

↓

Browser Event

↓

Event Dispatch

↓

Propagation

↓

JavaScript Handler

↓

UI Update

Treat events as a structured communication system rather than isolated callbacks.

---

# Core Principles

Dispatch

↓

Capture

↓

Target

↓

Bubble

↓

Default Action

↓

Rendering

---

# Event Lifecycle

```
User Input

↓

Browser

↓

Event Object

↓

Capture Phase

↓

Target Phase

↓

Bubble Phase

↓

Default Action
```

---

# Event Object

Every event contains information including

- type
- target
- currentTarget
- timestamp
- defaultPrevented
- propagation state

The event object describes what happened.

---

# Event Phases

```
Window

↓

Document

↓

HTML

↓

Body

↓

Target

↓

Body

↓

HTML

↓

Document

↓

Window
```

Capture flows downward.

Bubble flows upward.

---

# Capture Phase

Occurs before reaching the target.

Useful for

- global monitoring
- analytics
- advanced event routing

---

# Target Phase

The event reaches the originating element.

Application logic commonly executes here.

---

# Bubble Phase

The event propagates back up the DOM tree.

Most event listeners operate during bubbling.

---

# Event Propagation

Events travel through the DOM unless propagation is stopped.

Methods

- stopPropagation()
- stopImmediatePropagation()

Use sparingly.

---

# Default Actions

Examples

- clicking links
- submitting forms
- scrolling
- text selection

Prevent only when necessary.

```
preventDefault()
```

---

# Event Delegation

Instead of

```
1000 Buttons

↓

1000 Listeners
```

Use

```
Parent

↓

One Listener

↓

Event Target
```

Benefits

- lower memory usage
- dynamic content support
- improved scalability

---

# Common Event Types

Mouse

- click
- dblclick
- mousedown
- mouseup
- mousemove

Keyboard

- keydown
- keyup

Pointer

- pointerdown
- pointermove
- pointerup

Touch

- touchstart
- touchmove
- touchend

Forms

- input
- change
- submit
- focus
- blur

Clipboard

- copy
- cut
- paste

Window

- resize
- scroll
- load
- beforeunload

---

# Pointer Events

Modern applications should generally prefer Pointer Events.

Advantages

- mouse
- touch
- stylus

through one unified API.

---

# Keyboard Events

Accessible applications support

- Tab
- Enter
- Escape
- Arrow Keys
- Space

Never rely solely on mouse interaction.

---

# Focus Events

Focus management is essential for

- accessibility
- dialogs
- forms
- keyboard navigation

Always provide visible focus indicators.

---

# Passive Event Listeners

Example

```
passive: true
```

Useful for

- scroll
- touchmove
- wheel

Allows smoother scrolling because the browser knows the handler will not call `preventDefault()`.

---

# Custom Events

Applications can dispatch their own events.

Useful for

- reusable components
- plugins
- loosely coupled modules

---

# Event Loop Interaction

Events enter

```
Browser

↓

Task Queue

↓

Call Stack

↓

Handler

↓

Rendering
```

Long-running handlers delay rendering.

---

# React Synthetic Events

React wraps browser events in a consistent API.

Benefits

- cross-browser consistency
- unified behavior

Modern React delegates most events at the root container.

---

# Memory Management

Remove listeners when no longer needed.

Common leaks

- detached DOM nodes
- global listeners
- timers
- closures

---

# Accessibility

Support

- keyboard navigation
- focus order
- semantic controls

A button should respond equally well to keyboard and pointer input.

---

# Performance

Optimize by

- delegating events
- avoiding unnecessary listeners
- keeping handlers short
- using passive listeners where appropriate
- throttling high-frequency events

---

# High-Frequency Events

Examples

- scroll
- resize
- pointermove
- mousemove

Throttle or debounce expensive work.

---

# Debouncing

Wait until activity stops.

Useful for

- search inputs
- resize
- autocomplete

---

# Throttling

Limit execution frequency.

Useful for

- scrolling
- dragging
- animations
- pointer tracking

---

# Engineering Decisions

## Event Delegation

Recommended for lists and dynamic interfaces.

---

## Pointer Events

Preferred over separate mouse and touch APIs.

---

## Passive Listeners

Recommended for scroll performance.

---

## Keyboard Support

Required for interactive controls.

---

# Runtime Architecture

```
User

↓

Browser

↓

Event Queue

↓

Propagation

↓

Handler

↓

DOM Update

↓

Rendering
```

---

# Performance

Optimize

listener count

↓

handler duration

↓

event delegation

↓

rendering

↓

memory usage

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Event Delegation | Efficient and scalable | Requires understanding bubbling |
| Direct Listeners | Simpler for isolated elements | Higher memory usage |
| Passive Listeners | Better scrolling performance | Cannot prevent default behavior |
| Custom Events | Loose coupling | Additional architecture complexity |

---

# Common Failures

- thousands of listeners
- forgotten cleanup
- blocking handlers
- unnecessary preventDefault()
- inaccessible keyboard interactions
- excessive scroll processing

---

# Best Practices

- Prefer delegation for dynamic content.
- Keep handlers short.
- Clean up listeners.
- Support keyboard interaction.
- Use passive listeners for scrolling.
- Throttle expensive events.
- Avoid unnecessary propagation blocking.

---

# Anti-Patterns

❌ Attaching listeners to every list item

❌ Long synchronous event handlers

❌ Ignoring keyboard users

❌ Calling stopPropagation() without justification

❌ Forgetting to remove global listeners

❌ Expensive work inside scroll handlers

---

# Real-World Examples

## React

Uses a synthetic event system layered over native browser events, providing a consistent API while integrating event handling with its rendering lifecycle.

---

## Google Maps

Processes high-frequency pointer events using throttling and GPU-accelerated rendering to maintain smooth interactions.

---

## GitHub

Uses event delegation for menus, navigation, and dynamic content, reducing the number of event listeners attached to the DOM.

---

## Chrome

Dispatches events through the capture, target, and bubble phases while coordinating execution with the event loop and rendering pipeline.

---

# Related Skills

- javascript.md
- browser.md
- dom.md
- rendering.md
- accessibility.md
- react.md

---

# Definition of Done

An engineer understands browser events when they can

✓ Explain the complete event lifecycle from dispatch to rendering

✓ Distinguish capture, target, and bubble phases

✓ Use event delegation to build scalable interfaces

✓ Optimize high-frequency events with throttling and debouncing

✓ Manage keyboard, pointer, and focus interactions accessibly

✓ Prevent memory leaks by cleaning up event listeners

✓ Explain the relationship between events, the event loop, and rendering

✓ Understand React's synthetic event system

✓ Build responsive interfaces that remain performant under heavy interaction

✓ Treat events as the browser's communication layer between users and applications