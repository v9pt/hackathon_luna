# Compliance

Version: 1.0

---

# Goal

Establish and maintain organizational processes, technical controls, documentation, and evidence that demonstrate AI systems comply with applicable laws, regulations, industry standards, contractual obligations, and internal policies.

Compliance engineering ensures AI systems remain legally, operationally, and ethically deployable throughout their lifecycle.

A production AI platform should make compliance a continuous engineering process rather than a periodic audit activity.

---

# When to Use

Compliance applies whenever

- production AI systems exist
- customer data is processed
- regulated industries are served
- enterprise customers require certifications
- legal obligations exist
- audits occur
- international deployments exist
- contractual security requirements exist

---

# Problem

AI systems introduce regulatory challenges involving

- personal data
- automated decision making
- transparency
- fairness
- explainability
- security
- retention
- cross-border transfers

Without compliance

- legal penalties increase
- customer trust declines
- enterprise sales become difficult
- deployments may be prohibited

---

# Solution

Identify Requirements

↓

Implement Controls

↓

Collect Evidence

↓

Audit

↓

Improve

Compliance should be integrated into engineering workflows from the beginning.

---

# Core Principles

Understand Requirements

↓

Implement Controls

↓

Document

↓

Verify

↓

Monitor

↓

Improve

Compliance is continuous, not annual.

---

# Compliance Lifecycle

```
Requirements

↓

Risk Assessment

↓

Control Design

↓

Implementation

↓

Evidence Collection

↓

Audit

↓

Continuous Monitoring

↓

Improvement
```

---

# Compliance Architecture

```
Policies

↓

Engineering Controls

↓

Operational Processes

↓

Evidence Collection

↓

Monitoring

↓

Audits

↓

Continuous Improvement
```

---

# Regulatory Frameworks

## EU AI Act

Focuses on

- risk classification
- prohibited AI
- transparency
- human oversight
- documentation
- post-market monitoring

Risk-based compliance.

---

## GDPR

Protects

- personal data
- privacy
- consent
- data portability
- deletion rights
- lawful processing

Critical for European users.

---

## HIPAA

Applicable for healthcare AI.

Protects

- protected health information
- access controls
- audit logs
- encryption

---

## PCI DSS

Relevant for payment systems.

Protects

- payment data
- authentication
- network security
- logging

---

## SOC 2

Focuses on

- security
- availability
- confidentiality
- processing integrity
- privacy

Widely required for enterprise SaaS.

---

## ISO 27001

Information Security Management System.

Covers

- governance
- risk management
- security controls
- continuous improvement

---

## ISO/IEC 42001

AI Management System standard.

Addresses

- AI governance
- lifecycle management
- accountability
- risk management

Designed specifically for AI organizations.

---

## NIST AI Risk Management Framework

Provides guidance for

- governance
- mapping
- measurement
- management

Widely adopted internationally.

---

# Organizational Controls

Maintain

- security policies
- AI governance policies
- acceptable use policies
- incident procedures
- change management
- vendor management

Policies establish organizational expectations.

---

# Technical Controls

Implement

- encryption
- authentication
- authorization
- audit logging
- access control
- monitoring
- data retention
- backups

Controls demonstrate compliance.

---

# Privacy Controls

Protect

- personal information
- customer prompts
- uploaded documents
- embeddings
- logs

Apply

- minimization
- anonymization
- pseudonymization
- retention limits

---

# Data Classification

Classify

Public

↓

Internal

↓

Confidential

↓

Restricted

AI systems should process data according to classification policies.

---

# Data Retention

Define

- retention periods
- deletion procedures
- archival policies
- legal hold processes

Retention should follow legal requirements.

---

# Cross-Border Data Transfers

Document

- storage locations
- processing locations
- regional restrictions
- transfer mechanisms

International deployments require careful governance.

---

# Audit Logging

Record

- deployments
- prompt changes
- model changes
- approvals
- authentication
- administrative actions
- incidents

Audit logs should be immutable.

---

# Evidence Collection

Collect

- evaluation reports
- deployment records
- approvals
- access reviews
- security scans
- vulnerability reports
- penetration tests
- training records

Evidence should be continuously generated.

---

# Vendor Compliance

Evaluate vendors for

- certifications
- security
- privacy
- availability
- subcontractors
- contractual obligations

Third-party risk must be managed.

---

# Continuous Compliance

Continuously verify

- policy adherence
- configuration drift
- access reviews
- encryption
- documentation
- monitoring coverage

Compliance should never depend on manual audits alone.

---

# AI-Specific Compliance

Assess

- bias
- explainability
- transparency
- human oversight
- model documentation
- evaluation quality
- monitoring
- post-deployment surveillance

AI introduces additional regulatory requirements beyond traditional software.

---

# Engineering Decisions

## Manual Audits

Useful for

high-risk systems.

Expensive.

---

## Automated Compliance Checks

Recommended.

Reduces operational effort.

---

## Continuous Evidence Collection

Recommended for enterprise AI.

Simplifies audits.

---

## Policy-as-Code

Recommended wherever possible.

Improves consistency.

---

# Runtime Architecture

```
Engineering

↓

Policies

↓

Automated Controls

↓

Evidence Collection

↓

Monitoring

↓

Audit Repository

↓

Auditors
```

---

# Performance

Optimize

audit readiness

↓

evidence quality

↓

control coverage

↓

policy compliance

↓

risk visibility

↓

regulatory confidence

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Manual evidence collection | Flexible | High effort |
| Automated evidence collection | Scalable | Initial investment |
| Centralized compliance | Consistent | Slower updates |
| Policy-as-Code | Repeatable | Requires tooling |

---

# Common Failures

- incomplete audit logs
- undocumented model changes
- missing retention policies
- unmanaged vendor risk
- outdated documentation
- poor access reviews
- inconsistent evidence

---

# Best Practices

- Build compliance into development workflows.
- Automate evidence collection.
- Maintain current documentation.
- Review regulatory changes regularly.
- Encrypt sensitive information.
- Classify data consistently.
- Audit vendors periodically.
- Continuously monitor compliance status.

---

# Anti-Patterns

❌ Preparing for audits only when scheduled

❌ Manual evidence gathering

❌ Missing documentation

❌ Ignoring regional regulations

❌ Uncontrolled access

❌ Undefined retention policies

❌ Assuming compliance is solely a legal responsibility

---

# Real-World Examples

## Microsoft

Maintains enterprise compliance programs supporting global regulatory frameworks, integrating governance, documentation, technical controls, and continuous monitoring into AI development.

---

## Google Cloud

Provides compliance tooling, regional data controls, encryption, audit logging, and certifications that help organizations satisfy regulatory obligations.

---

## AWS

Supports customers through services aligned with major compliance frameworks, including audit logging, identity management, encryption, and infrastructure certifications.

---

## OpenAI

Publishes security and governance documentation, operational practices, and enterprise controls that support customer compliance requirements while operating AI services.

---

## Enterprise AI Platforms

Integrate governance, security, lifecycle management, documentation, automated evidence collection, and continuous monitoring to maintain ongoing compliance across multiple regulatory frameworks.

---

# Related Skills

- governance.md
- security_operations.md
- prompt_versioning.md
- model_versioning.md
- incident_response.md
- deployment.md

---

# Definition of Done

An enterprise AI compliance program is complete only if

✓ Applicable regulations and standards are identified and mapped to engineering controls

✓ Technical, operational, and organizational controls are documented and implemented

✓ Audit logs provide immutable evidence of significant operational actions

✓ Data privacy, retention, and cross-border processing requirements are enforced

✓ Continuous evidence collection supports efficient audits

✓ AI-specific risks such as bias, transparency, and human oversight are addressed

✓ Vendor compliance is regularly assessed

✓ Compliance monitoring detects deviations from required controls

✓ Documentation remains current throughout the AI lifecycle

✓ Compliance becomes an integrated engineering capability that continuously demonstrates regulatory, contractual, and organizational adherence