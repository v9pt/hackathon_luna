# Security Operations

Version: 1.0

---

# Goal

Protect AI systems, models, prompts, agents, infrastructure, data, and users from malicious activity while maintaining availability, integrity, confidentiality, and operational resilience throughout the AI lifecycle.

Security Operations (SecOps) combines traditional cybersecurity, cloud security, application security, and AI-specific defenses into a continuous operational capability.

A production AI platform should continuously detect, prevent, respond to, and recover from security threats.

---

# When to Use

Security Operations applies whenever

- production AI systems exist
- customer data is processed
- LLMs are deployed
- RAG systems exist
- agents execute tools
- APIs are exposed
- enterprise customers are served
- regulated data is handled

---

# Problem

AI systems introduce both traditional and AI-specific attack surfaces.

Examples

- prompt injection
- indirect prompt injection
- jailbreaks
- tool abuse
- model theft
- data exfiltration
- supply chain attacks
- API abuse
- credential compromise
- adversarial inputs
- poisoned retrieval data
- malicious MCP servers

Without operational security

- confidential information leaks
- models behave unpredictably
- attackers gain persistence
- customer trust is lost
- compliance obligations are violated

---

# Solution

Prevent

↓

Detect

↓

Contain

↓

Respond

↓

Recover

↓

Improve

Security should be continuous rather than reactive.

---

# Core Principles

Least Privilege

↓

Defense in Depth

↓

Zero Trust

↓

Continuous Monitoring

↓

Rapid Response

↓

Continuous Improvement

Assume compromise and minimize blast radius.

---

# Security Operations Lifecycle

```
Identify

↓

Protect

↓

Detect

↓

Respond

↓

Recover

↓

Review

↓

Improve
```

---

# Security Architecture

```
Users

↓

Identity & Access

↓

API Gateway

↓

Authentication

↓

LLM Gateway

↓

Agents

↓

Tools

↓

Infrastructure

↓

Monitoring

↓

SOC
```

---

# Identity and Access Management

Protect

- users
- developers
- services
- agents
- administrators

Implement

- RBAC
- ABAC
- MFA
- SSO
- Just-In-Time access

Least privilege should be enforced everywhere.

---

# Secrets Management

Never store secrets in

- prompts
- source code
- repositories
- logs

Use

- Vault
- AWS Secrets Manager
- Azure Key Vault
- GCP Secret Manager

Rotate secrets regularly.

---

# Network Security

Protect

- APIs
- databases
- inference endpoints
- vector stores
- internal services

Implement

- TLS
- WAF
- network segmentation
- private networking
- rate limiting

---

# Zero Trust

Never trust

- users
- agents
- APIs
- providers
- internal services

Continuously verify identity and authorization.

---

# Threat Modeling

Assess threats against

- models
- prompts
- agents
- RAG
- APIs
- infrastructure
- third-party integrations

Threat modeling should occur before deployment.

---

# AI-Specific Threats

## Prompt Injection

Attackers manipulate prompts to override intended instructions.

Mitigations

- prompt isolation
- input validation
- output filtering
- instruction hierarchy

---

## Indirect Prompt Injection

Malicious instructions hidden inside

- web pages
- PDFs
- emails
- retrieved documents

Mitigations

- content sanitization
- retrieval filtering
- trust boundaries
- source validation

---

## Jailbreaks

Attempts to bypass safety mechanisms.

Mitigations

- adversarial testing
- output moderation
- layered safety systems
- policy enforcement

---

## Tool Abuse

Agents misuse

- APIs
- file systems
- email
- shell access

Mitigations

- capability restrictions
- scoped permissions
- approval workflows
- execution sandboxes

---

## RAG Poisoning

Attackers insert malicious documents into knowledge bases.

Mitigations

- document validation
- source trust scoring
- signed content
- retrieval monitoring

---

## Embedding Poisoning

Manipulate embeddings to influence retrieval.

Mitigations

- embedding validation
- anomaly detection
- periodic re-indexing

---

## Model Theft

Unauthorized extraction of model capabilities.

Mitigations

- rate limits
- watermarking
- API monitoring
- behavioral analysis

---

## Adversarial Inputs

Inputs crafted to produce incorrect predictions.

Mitigations

- adversarial testing
- confidence thresholds
- anomaly detection

---

# OWASP Top 10 for LLM Applications

Protect against

- Prompt Injection
- Insecure Output Handling
- Training Data Poisoning
- Model Denial of Service
- Supply Chain Vulnerabilities
- Sensitive Information Disclosure
- Excessive Agency
- System Prompt Leakage
- Vector and Embedding Weaknesses
- Misinformation

Security reviews should include these categories.

---

# Supply Chain Security

Secure

- dependencies
- models
- containers
- datasets
- plugins
- MCP servers
- CI/CD pipelines

Generate

SBOMs

and verify artifact integrity.

---

# Runtime Protection

Continuously monitor

- API traffic
- prompts
- outputs
- agent actions
- infrastructure
- user behavior

Use anomaly detection for abnormal activity.

---

# Vulnerability Management

Continuously

- scan dependencies
- patch systems
- review configurations
- rotate secrets
- verify containers

Security debt should be actively managed.

---

# Security Monitoring

Monitor

- authentication failures
- privilege escalation
- prompt injection attempts
- unusual token usage
- abnormal agent behavior
- provider anomalies
- data exfiltration

Integrate with SIEM platforms.

---

# Security Incident Response

Respond to

- compromised credentials
- prompt leakage
- provider compromise
- ransomware
- malicious prompts
- model abuse
- infrastructure attacks

Security incidents follow dedicated runbooks.

---

# Logging

Maintain immutable logs for

- authentication
- deployments
- prompt changes
- model changes
- administrative actions
- tool execution
- agent decisions

Logs support investigations.

---

# Engineering Decisions

## Centralized Security Operations Center (SOC)

Recommended for enterprise organizations.

Provides unified monitoring and response.

---

## Security Champions

Embed security expertise within engineering teams.

Improves secure development practices.

---

## Automated Detection

Recommended.

Reduces response time.

---

## Human Approval

Required for

- privileged actions
- destructive operations
- production credential changes

---

# Runtime Architecture

```
Identity

↓

Gateway

↓

Authorization

↓

LLM

↓

Agents

↓

Tools

↓

Monitoring

↓

SIEM

↓

SOC
```

---

# Performance

Optimize

threat detection

↓

incident response

↓

false positive reduction

↓

attack prevention

↓

system resilience

↓

operational visibility

---

# Trade-offs

| Decision | Advantages | Disadvantages |
|----------|------------|---------------|
| Zero Trust | Strong security | Operational complexity |
| Broad permissions | Easier development | Increased risk |
| Automated detection | Faster response | Possible false positives |
| Human approval | Better oversight | Slower operations |

---

# Common Failures

- hardcoded secrets
- excessive permissions
- missing audit logs
- unvalidated retrieval content
- unsecured agent tools
- ignored dependency updates
- weak authentication

---

# Best Practices

- Enforce least privilege.
- Rotate secrets regularly.
- Validate retrieved content.
- Sandbox agent execution.
- Monitor continuously.
- Conduct regular penetration testing.
- Threat model every major AI system.
- Follow OWASP guidance for LLM applications.

---

# Anti-Patterns

❌ Trusting all retrieved content

❌ Allowing unrestricted tool access

❌ Storing secrets in prompts

❌ Ignoring prompt injection

❌ No runtime monitoring

❌ Manual security reviews only

❌ Treating AI as traditional software security

---

# Real-World Examples

## OpenAI

Implements layered safety systems, staged deployments, operational monitoring, red teaming, and continuous security improvements to protect production AI services.

---

## Anthropic

Combines constitutional safety techniques, adversarial testing, operational monitoring, and secure deployment practices to reduce misuse and improve robustness.

---

## Microsoft

Applies Zero Trust architecture, enterprise identity management, Defender security tooling, and Responsible AI governance across AI services.

---

## Google

Integrates BeyondCorp Zero Trust principles, supply chain security, threat intelligence, and secure cloud infrastructure into production AI deployments.

---

## OWASP

Publishes the OWASP Top 10 for LLM Applications, providing practical guidance for mitigating AI-specific security risks.

---

# Related Skills

- governance.md
- compliance.md
- incident_response.md
- reliability.md
- deployment.md
- testing_ai_systems.md

---

# Definition of Done

A production AI Security Operations capability is complete only if

✓ Identity, authentication, and authorization enforce least privilege across all users, services, and agents

✓ Secrets are securely managed and rotated without exposure in code or prompts

✓ AI-specific threats—including prompt injection, jailbreaks, RAG poisoning, tool abuse, and model theft—are actively mitigated

✓ Infrastructure, models, prompts, and dependencies are continuously monitored for security events

✓ Supply chain security verifies the integrity of software, models, datasets, and external integrations

✓ Security incidents follow documented response procedures with forensic-quality audit logs

✓ Runtime monitoring detects anomalous agent behavior, prompt misuse, and potential data exfiltration

✓ Regular threat modeling, penetration testing, and red-team exercises validate security controls

✓ Compliance requirements are supported through logging, evidence collection, and operational governance

✓ Security becomes an integrated engineering discipline that continuously protects AI systems throughout their entire lifecycle while enabling safe, reliable, and trustworthy operation