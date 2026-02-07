**ISMS-IMP-A.8.27.4-UG - Zero Trust Implementation Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Zero Trust Implementation Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.4-UG |
| **Assessment Domain** | Domain 4 - Zero Trust Architecture |
| **Related Policy** | ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Security Architect / Zero Trust Program Lead |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect | Initial Zero Trust assessment specification |

**Review Cycle**: Annual (or after significant ZTA changes)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles)
- ISMS-IMP-A.8.27.1 (Security Architecture Review Process)
- ISMS-IMP-A.8.27.2 (Threat Modelling Methodology)
- ISMS-IMP-A.8.27.3 (Secure Architecture Pattern Catalogue)
- ISMS-POL-A.5.15-16-18 (Identity and Access Management)
- ISMS-POL-A.8.20-22 (Network Security)
- ISO/IEC 27002:2022 Control A.8.27
- NIST SP 800-207 (Zero Trust Architecture)
- NIST SP 800-207A (Zero Trust for Cloud-Native Applications)
- CISA Zero Trust Maturity Model

---

# Assessment Overview

## Purpose

This assessment evaluates [Organisation]'s **Zero Trust Architecture (ZTA) implementation and maturity**, measuring progress across the core Zero Trust pillars as mandated by ISMS-POL-A.8.27.

**What This Assessment Covers:**

- Zero Trust strategy and roadmap
- Identity pillar maturity
- Device pillar maturity
- Network pillar maturity
- Application/Workload pillar maturity
- Data pillar maturity
- Visibility and analytics maturity
- Automation and orchestration maturity

**What This Assessment Does NOT Cover:**

- Architecture review process (see ISMS-IMP-A.8.27.1)
- Threat modelling methodology (see ISMS-IMP-A.8.27.2)
- Architecture pattern catalogue (see ISMS-IMP-A.8.27.3)
- Detailed IAM implementation (see ISMS-IMP-A.5.15-16-18)

**Assessment Output:**

- Excel workbook documenting ZTA maturity across pillars
- CISA maturity model alignment scoring
- Gap analysis by pillar
- Zero Trust roadmap progress tracking
- Compliance scoring and recommendations

## Why This Matters

**ISO/IEC 27001:2022 Control A.8.27 Requirement:**
> *"Principles for engineering secure systems should be established, documented, maintained and applied to any information system development activities."*

**NIST SP 800-207 Core Tenets:**
> *"Zero Trust is a cybersecurity paradigm focused on resource protection and the premise that trust is never granted implicitly but must be continually evaluated."*

**Zero Trust Principles (ISMS-POL-A.8.27 Section 2.1):**

1. **Never Trust, Always Verify** - No implicit trust based on network location
2. **Assume Breach** - Design assuming adversaries have network access
3. **Verify Explicitly** - Access decisions based on all available data points
4. **Least Privilege Access** - JIT/JEA access, risk-based conditional access
5. **Encryption by Default** - All data encrypted in transit and at rest

**Business Impact of Inadequate Zero Trust:**

- **Lateral Movement:** Attackers move freely after initial compromise
- **Data Breaches:** Perimeter-only security insufficient
- **Compliance Risk:** Regulators increasingly expect Zero Trust
- **Cloud Security:** Traditional perimeter doesn't apply to cloud
- **Remote Work:** Distributed workforce requires Zero Trust approach

## Who Should Complete This Assessment

**Primary Responsibility:** Zero Trust Program Lead or Security Architect

**Required Knowledge:**

- [Organisation]'s Zero Trust strategy and roadmap
- Identity and access management architecture
- Network segmentation and security architecture
- Application security architecture
- Data protection and classification
- Security monitoring and analytics capabilities

**Support Roles:**

- **CISO:** Strategy ownership, resource allocation
- **Identity Team:** IAM pillar assessment
- **Network Team:** Network pillar assessment
- **Cloud Team:** Cloud workload assessment
- **Data Protection Team:** Data pillar assessment
- **Security Operations:** Visibility and analytics

## Time Estimate

**Total Assessment Time:** 12-16 hours

**Breakdown:**

- **Information Gathering:** 4-5 hours
  - Review Zero Trust strategy and roadmap
  - Collect evidence for each pillar
  - Gather metrics and maturity data
  - Interview pillar owners

- **Assessment Completion:** 5-6 hours
  - Complete pillar assessments (Identity, Device, Network, App, Data)
  - Assess visibility and analytics
  - Evaluate automation and orchestration
  - Calculate maturity scores

- **Evidence Collection:** 2-3 hours
  - Architecture diagrams
  - Configuration evidence
  - Policy documentation
  - Metrics and dashboards

- **Quality Review:** 1-2 hours
  - Gap analysis
  - Roadmap alignment
  - Stakeholder review

## Connection to Policy

This assessment implements **ISMS-POL-A.8.27, Section 2.1 (Zero Trust Architecture Principles)** which mandates:

**Never Trust, Always Verify:**

- No implicit trust based on network location, device ownership, or previous authentication
- Every access request authenticated and authorised regardless of source
- Trust continuously evaluated

**Assume Breach:**

- Design systems assuming adversaries may have network access
- Internal network traffic treated as potentially hostile
- Lateral movement restricted through segmentation

**Verify Explicitly:**

- Access decisions based on:
  - User identity and authentication strength
  - Device health and compliance status
  - Data sensitivity and classification
  - Access context (location, time, behaviour)
  - Request anomaly detection

**Least Privilege Access:**

- Just-in-time (JIT) access for elevated privileges
- Just-enough-access (JEA) for all access grants
- Risk-based conditional access policies
- Continuous access evaluation

**Encryption by Default:**

- All data in transit encrypted (TLS 1.2+ minimum)
- All data at rest encrypted for CONFIDENTIAL+ classification
- Internal service-to-service communication encrypted

---

# Prerequisites

## Required Access

| System/Resource | Purpose | Who Can Provide |
|-----------------|---------|-----------------|
| Zero Trust strategy docs | Strategy and roadmap | CISO Office |
| IAM architecture docs | Identity pillar | Identity Team |
| Network architecture docs | Network pillar | Network Team |
| Application security docs | Workload pillar | Security Engineering |
| Data protection docs | Data pillar | Data Protection |
| SIEM/Analytics | Visibility pillar | Security Operations |

## Pre-Assessment Checklist

✅ Zero Trust strategy reviewed
✅ Pillar owners identified and scheduled
✅ Architecture documentation compiled
✅ Maturity baseline (if exists) available
✅ Assessment timeframe communicated

---

# Completion Walkthrough

## Step 1: Review Instructions and CISA Maturity Model

**Navigate to the Instructions sheet**

Understand the CISA Zero Trust Maturity Model levels:

| Level | Description |
|-------|-------------|
| **Traditional** | Perimeter-based security, implicit trust within network |
| **Initial** | Basic ZT capabilities, some explicit verification |
| **Advanced** | Comprehensive ZT, automated policy enforcement |
| **Optimal** | Full ZT, continuous verification, dynamic policies |

## Step 2: Assess Zero Trust Strategy

**Navigate to the Strategy sheet**

Assess strategic elements:

| Element | Assessment Questions |
|---------|---------------------|
| **Executive Sponsorship** | Is ZT endorsed at executive level? |
| **Strategy Document** | Is ZT strategy documented? |
| **Roadmap** | Is multi-year roadmap defined? |
| **Governance** | Is ZT governance established? |
| **Investment** | Is budget allocated? |
| **Metrics** | Are success metrics defined? |
| **Communication** | Is strategy communicated? |
| **Training** | Is ZT training provided? |

## Step 3: Assess Identity Pillar

**Navigate to the Identity sheet**

Assess identity capabilities against CISA maturity levels:

| Capability | Traditional | Initial | Advanced | Optimal |
|------------|-------------|---------|----------|---------|
| **Authentication** | Passwords | MFA some users | MFA all users | Phishing-resistant MFA |
| **Authorisation** | Static groups | RBAC | ABAC | Dynamic, risk-based |
| **Identity Lifecycle** | Manual | Automated provisioning | JIT access | Continuous verification |
| **Privileged Access** | Standing privileges | PAM basic | JIT/JEA | Zero standing privilege |
| **Federation** | None | Basic SAML | Modern protocols | Decentralised identity |

## Step 4: Assess Device Pillar

**Navigate to the Device sheet**

Assess device capabilities:

| Capability | Traditional | Initial | Advanced | Optimal |
|------------|-------------|---------|----------|---------|
| **Inventory** | Partial | Complete inventory | Real-time inventory | Auto-discovery |
| **Compliance** | None | Compliance checks | Continuous compliance | Real-time posture |
| **Access Control** | Network-based | Device certificates | Device health gates | Context-aware |
| **Threat Protection** | Antivirus | EDR | XDR | Autonomous response |

## Step 5: Assess Network Pillar

**Navigate to the Network sheet**

Assess network capabilities:

| Capability | Traditional | Initial | Advanced | Optimal |
|------------|-------------|---------|----------|---------|
| **Segmentation** | Perimeter only | VLANs | Micro-segmentation | App-level micro-seg |
| **Traffic Encryption** | VPN | TLS for external | TLS everywhere | mTLS |
| **Access Control** | Firewall rules | ZTNA basic | ZTNA comprehensive | SDP |
| **Monitoring** | Perimeter logs | Network flow | Full packet inspection | ML-based analysis |

## Step 6: Assess Workload Pillar

**Navigate to the Workload sheet**

Assess application/workload capabilities:

| Capability | Traditional | Initial | Advanced | Optimal |
|------------|-------------|---------|----------|---------|
| **Workload Identity** | None | Service accounts | Managed identities | Workload attestation |
| **Access Control** | Network-based | API keys | OAuth/OIDC | SPIFFE/SPIRE |
| **Isolation** | Shared infra | VMs | Containers | Serverless isolation |
| **Security Testing** | Manual | SAST/DAST | DevSecOps | Continuous validation |

## Step 7: Assess Data Pillar

**Navigate to the Data sheet**

Assess data capabilities:

| Capability | Traditional | Initial | Advanced | Optimal |
|------------|-------------|---------|----------|---------|
| **Classification** | Manual, ad-hoc | Policy-based | Automated labelling | ML classification |
| **Encryption** | Selective | At rest and transit | Per-field encryption | Confidential computing |
| **Access Control** | File permissions | ABAC | Dynamic access | Data-centric security |
| **DLP** | None | Basic DLP | Content-aware DLP | AI-powered DLP |
| **Discovery** | None | Periodic scans | Continuous discovery | Real-time classification |

## Step 8: Assess Visibility Pillar

**Navigate to the Visibility sheet**

Assess visibility capabilities:

| Capability | Traditional | Initial | Advanced | Optimal |
|------------|-------------|---------|----------|---------|
| **Logging** | Perimeter logs | Centralised logging | Full telemetry | Real-time streaming |
| **Analytics** | Manual review | SIEM | UEBA | AI/ML analytics |
| **Threat Detection** | Signature-based | Behaviour rules | ML detection | Autonomous detection |
| **Investigation** | Manual | Guided investigation | Automated triage | Autonomous investigation |

## Step 9: Assess Automation Pillar

**Navigate to the Automation sheet**

Assess automation capabilities:

| Capability | Traditional | Initial | Advanced | Optimal |
|------------|-------------|---------|----------|---------|
| **Policy Automation** | Manual policies | Scripted deployment | Policy as code | Intent-based |
| **Response Automation** | Manual response | Basic playbooks | SOAR integration | Autonomous response |
| **Remediation** | Manual | Scripted remediation | Auto-remediation | Self-healing |
| **Orchestration** | Siloed tools | Basic integration | Unified platform | Zero-touch security |

## Step 10: Complete Compliance and Gap Register

Complete compliance scoring and consolidate all gaps with remediation plans.

---

# Evidence Collection

## Required Evidence

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| **Strategy Docs** | ZT strategy, roadmap | CISO Office |
| **Architecture Diagrams** | ZTA architecture | Security Architecture |
| **Policy Evidence** | Conditional access, segmentation | IT Operations |
| **Configuration** | Tool configurations | Security Engineering |
| **Metrics** | ZT dashboard, KPIs | Security Operations |
| **Audit Reports** | ZT-related audit findings | Internal Audit |

## Evidence Naming Convention

```
ISMS-IMP-A.8.27.4_[Pillar]_[Description]_YYYYMMDD.[ext]
```

---

# Common Pitfalls

❌ **MISTAKE:** Treating Zero Trust as a product purchase
✅ **CORRECT:** Zero Trust is a strategy, not a product

❌ **MISTAKE:** Starting everywhere at once
✅ **CORRECT:** Prioritise high-value assets and use cases

❌ **MISTAKE:** Ignoring user experience
✅ **CORRECT:** Balance security with usability

❌ **MISTAKE:** Forgetting legacy systems
✅ **CORRECT:** Plan for legacy system integration

❌ **MISTAKE:** No metrics for success
✅ **CORRECT:** Define and track ZT maturity metrics

❌ **MISTAKE:** Identity-only focus
✅ **CORRECT:** Address all pillars holistically

❌ **MISTAKE:** Treating assessment as one-time
✅ **CORRECT:** Continuous maturity assessment

❌ **MISTAKE:** Overestimating maturity level
✅ **CORRECT:** Be honest about current state

❌ **MISTAKE:** No executive sponsorship
✅ **CORRECT:** ZT requires executive commitment

❌ **MISTAKE:** Not aligning with NIST SP 800-207
✅ **CORRECT:** Use NIST SP 800-207 as reference architecture

---

# Quality Checklist

**Completeness:**

- [ ] Strategy assessment complete
- [ ] All pillars assessed (Identity, Device, Network, Workload, Data)
- [ ] Visibility and automation assessed
- [ ] Evidence collected for each pillar
- [ ] Compliance scored
- [ ] Gaps documented

**Evidence:**

- [ ] Strategy documentation
- [ ] Architecture diagrams per pillar
- [ ] Configuration evidence
- [ ] Metrics and dashboards

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
