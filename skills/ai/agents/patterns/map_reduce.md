# Pattern

Map → Reduce

Version: 1.0

---

# Goal

Execute many independent tasks in parallel and combine their outputs into a single validated result.

The Map–Reduce pattern decomposes large workloads into independent units that can execute concurrently before aggregating their outputs through a deterministic reduction stage.

A production Map–Reduce system should maximize parallelism while ensuring correctness, scalability, fault tolerance, and reproducibility.

---

# When to Use

Use this pattern whenever

- Thousands of documents must be processed
- Large repositories require analysis
- Independent subtasks exist
- Data can be partitioned
- Parallel execution improves throughput
- Results require aggregation

---

# Problem

Sequential execution

```
Task1

↓

Task2

↓

Task3

↓

Task4
```

becomes increasingly slow as workload grows.

Problems include

- poor scalability
- idle compute resources
- long execution time
- expensive sequential workflows

---

# Solution

Split

↓

Execute Independently

↓

Merge

↓

Validate

```
Input

↓

Map

↓

Worker 1

Worker 2

Worker 3

Worker N

↓

Reduce

↓

Result
```

---

# Core Principles

Partition

↓

Parallelize

↓

Aggregate

↓

Validate

Every mapped task should be independent.

---

# Architecture

```
Input
 │
 ▼
Partitioner
 │
 ▼
Map Workers
 │
 ▼
Intermediate Results
 │
 ▼
Reducer
 │
 ▼
Validator
 │
 ▼
Output
```

---

# Components

## Partitioner

Responsible for

- splitting work
- balancing partitions
- preserving metadata

---

## Mapper

Responsible for

- processing one partition
- producing structured output
- remaining independent

Mappers should not communicate directly.

---

## Intermediate Store

Stores

- partial outputs
- metadata
- execution status

---

## Reducer

Responsible for

- merging outputs
- resolving duplicates
- ordering results
- producing final output

---

## Validator

Verifies

- completeness
- correctness
- consistency
- policy compliance

---

# Execution Lifecycle

Input

↓

Partition

↓

Parallel Mapping

↓

Intermediate Results

↓

Reduce

↓

Validation

↓

Complete

---

# Partition Strategies

## Equal Size

Split evenly.

Useful for uniform workloads.

---

## Semantic

Split by

- document
- repository
- topic
- customer
- project

Recommended for AI systems.

---

## Dynamic

Generate partitions during execution.

Useful for unknown workloads.

---

# Mapping

Each mapper should

- receive one partition
- process independently
- emit deterministic outputs
- report status

Avoid shared mutable state.

---

# Reduction

Reducer may

- merge summaries
- rank answers
- remove duplicates
- compute statistics
- combine code changes

Reduction should be deterministic.

---

# Hierarchical Reduction

Large workloads may require

```
Workers

↓

Local Reducers

↓

Regional Reducers

↓

Global Reducer
```

Useful for distributed systems.

---

# Streaming Reduction

Reducer processes outputs as they arrive.

Useful for

- long-running workflows
- real-time analytics
- streaming pipelines

---

# Fault Tolerance

If a mapper fails

Detect

↓

Retry

↓

Reassign

↓

Continue

Only failed partitions should rerun.

---

# Load Balancing

Balance using

- partition size
- execution time
- worker capacity
- historical latency

Avoid uneven workloads.

---

# Pattern References

## Supervisor Worker

Supervisor coordinates mappers.

---

## Router

Routes partitions to workers.

---

## Planner Executor

Planner creates partition strategy.

---

# Engineering Decisions

## Static Partitioning

Simple

Predictable

Suitable for small datasets.

---

## Dynamic Partitioning

Recommended.

Adapts to workload changes.

---

## Tree Reduction

Recommended for large outputs.

Reduces bottlenecks.

---

## Streaming Reduction

Recommended for continuous systems.

---

# Runtime Architecture

```
Input

↓

Partitioner

↓

Task Queue

↓

Worker Pool

↓

Intermediate Store

↓

Reducer

↓

Validator

↓

Output
```

---

# Performance

Optimize

partition balance

↓

worker utilization

↓

network transfer

↓

aggregation latency

↓

retry frequency

↓

memory usage

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Static partitions | Simple | Uneven workload |
| Dynamic partitions | Better utilization | Scheduler complexity |
| Single reducer | Easy | Bottleneck |
| Hierarchical reducer | Scalable | More infrastructure |
| Streaming reducer | Low latency | Stateful execution |

---

# Common Failures

- uneven partitions
- reducer bottleneck
- duplicate outputs
- missing partitions
- worker starvation
- inconsistent aggregation

---

# Best Practices

- Keep partitions independent.
- Balance workloads dynamically.
- Emit structured outputs.
- Validate intermediate results.
- Retry only failed partitions.
- Use hierarchical reduction for large workloads.
- Monitor worker utilization.
- Make reduction deterministic.

---

# Anti-Patterns

❌ Shared mutable state

❌ Sequential mapping

❌ Monolithic reducers

❌ Ignoring failed partitions

❌ Non-deterministic aggregation

❌ Excessive synchronization

❌ Uneven partition sizes

---

# Comparison

| Pattern | Best For | Weakness |
|----------|----------|----------|
| Planner–Executor | Workflow planning | Limited parallelism |
| ReAct | Iterative reasoning | Sequential loop |
| Supervisor–Worker | Specialized collaboration | Coordination overhead |
| Router | Intelligent dispatch | Doesn't aggregate |
| Map–Reduce | Massive parallel execution | Limited iterative reasoning |

---

# Real-World Examples

## Google MapReduce

Processes massive datasets by distributing work across thousands of machines before aggregating results.

---

## Apache Spark

Uses distributed map and reduce operations for scalable data processing with in-memory execution.

---

## Ray

Schedules parallel tasks across worker nodes and aggregates results efficiently for AI and data workloads.

---

## LangGraph

Fans out independent graph branches and combines outputs through aggregation nodes with checkpoint support.

---

## Large RAG Pipelines

Split millions of documents into chunks, process embeddings in parallel, then merge metadata into vector indexes.

---

## Repository Analysis

Analyze thousands of source files concurrently, aggregate findings into architecture summaries or refactoring plans.

---

# Related Skills

- workflows.md
- orchestration.md
- delegation.md
- task_decomposition.md

---

# Related Patterns

- planner_executor.md
- supervisor_worker.md
- router.md
- react.md

---

# Definition of Done

A Map–Reduce implementation is production-ready only if

✓ Workloads are partitioned into independent tasks

✓ Mapping executes safely in parallel

✓ Intermediate results are structured and traceable

✓ Reduction deterministically combines outputs

✓ Failed partitions can be retried independently

✓ Load balancing maximizes worker utilization

✓ Aggregation scales without becoming a bottleneck

✓ Execution is observable through metrics and logs

✓ Validation confirms the completeness and correctness of the final result

✓ The system reliably processes large-scale workloads with high throughput and fault tolerance