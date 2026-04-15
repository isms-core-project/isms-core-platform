<!-- ISMS-CORE:IMP:AI-IMP-A.10.2-4-UG:ai:UG:a.10.2-4 -->
**AI-IMP-A.10.2-4-UG — Third-Party and Customer Relationships — User Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Third-Party and Customer Relationships — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | AI-IMP-A.10.2-4-UG |
| **Related Policy** | AI-POL-A.10.2-4 (Third-Party and Customer Relationships) |
| **Document Creator** | AI Governance Officer / Legal / Procurement Officer |
| **Document Owner** | AI Governance Officer |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **AIMS Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | AI Governance Officer | Initial user guide for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- AI-POL-A.10.2-4 (Third-Party and Customer Relationships — governing policy)
- AI-IMP-A.10.2-4-TG (Third-Party and Customer Relationships — Technical Guide)
- AI-POL-A.8.2-5 (Information for Interested Parties — customer documentation)
- PRIV-POL-00 (Privacy Regulatory Applicability — data processing agreements)
- ISO/IEC 42001:2023 Controls A.10.2–A.10.4

---

## Purpose of This Guide

This guide explains **how to manage AI-related obligations in third-party and customer relationships** — including how to allocate responsibilities with AI suppliers, how to assess and onboard AI suppliers, and how to fulfil information obligations toward customers of AI-enabled products. It is the practical companion to AI-POL-A.10.2-4.

**Who this guide is for**: Legal/Procurement, AI Governance Officer, Account Management/Customer Success, AI System Owners managing third-party AI components.

---

## Part 1 — Responsibility Allocation (A.10.2)

### 1.1 Why This Matters

Where multiple parties are involved in an AI system — a supplier providing an AI component, a customer deploying [Organisation]'s AI product, a partner co-developing an AI solution — it must be clear who is responsible for what. Without documented responsibility allocation:
- Regulatory obligations fall through the gaps
- Incidents happen without a clear response owner
- Affected individuals have no clear recourse path

### 1.2 How to Allocate Responsibilities

For every multi-party AI arrangement, the AI Governance Officer leads responsibility allocation. The process:

1. **Identify the arrangement**: Is it a supplier relationship (third party provides AI to [Organisation]) or a customer relationship (third party uses AI provided by [Organisation])? Or both?

2. **Determine EU AI Act roles**: Per AI-POL-00 role determination framework:
   - **Provider**: party that places an AI system on the market or puts it into service
   - **Deployer**: party that uses an AI system under their authority
   - **Distributor**: party that makes an AI system available but does not modify it
   Where [Organisation] modifies a third-party AI system materially, assess whether provider obligations apply.

3. **Work through the responsibility matrix**: For each of the nine responsibility domains (system specification, training data governance, V&V, AISIA, regulatory compliance, monitoring and incident response, user-facing transparency, right to erasure, indemnity and liability), determine which party holds the obligation.

4. **Document the allocation**: In the AI Third-Party Responsibility Matrix (maintained by the AI Governance Officer) and in the contract schedule.

### 1.3 Common Allocation Patterns

| Arrangement Type | Typical Allocation Pattern |
|-----------------|--------------------------|
| [Organisation] uses a foundation model API | Foundation model provider: model V&V, EU AI Act provider obligations for the model. [Organisation]: deployment governance, AISIA for the application, intended use specification, user transparency |
| [Organisation] provides AI SaaS to customers | [Organisation]: model development, V&V, technical documentation, EU AI Act provider obligations. Customer: deployer obligations, intended use within their organisation, human oversight in their context |
| Joint development partnership | Negotiated per agreement — each party's obligations must be explicitly documented; EU AI Act role assignment agreed in contract |

---

## Part 2 — AI Supplier Assessment and Management (A.10.3)

### 2.1 Who Is an "AI Supplier"?

An AI supplier is any third party providing:
- A foundation model or pre-trained model used in [Organisation]'s AI systems
- An AI development platform, MLOps tool, or annotation platform
- An AI-as-a-service API used in production
- Training data sourced from the third party
- An AI system auditing or assessment service

General IT suppliers who do not specifically provide AI components are managed under ISMS supplier management controls, not this process.

### 2.2 Pre-Procurement Assessment Process

Before engaging a new AI supplier:

| Step | Action | Who |
|------|--------|-----|
| 1 | AI System Owner identifies need for third-party AI component | AI System Owner |
| 2 | Procurement Officer notifies AI Governance Officer | Procurement |
| 3 | AI Governance Officer initiates pre-procurement assessment | AI Governance Officer |
| 4 | Assessment conducted across all required dimensions (see AI-IMP-A.10.2-4-TG for assessment schema) | AI Governance Officer + Procurement + CISO + DPO (if personal data) |
| 5 | Assessment outcome documented | AI Governance Officer |
| 6 | If assessment passes: Procurement proceeds to contract | Procurement |
| 7 | Contract includes AI-specific provisions (Section 2.3) | Legal |
| 8 | Supplier record added to AI System Resource Register | AI System Owner |
| 9 | Responsibility allocation documented in AI Third-Party Responsibility Matrix | AI Governance Officer |

### 2.3 Contractual Minimums for AI Suppliers

Every AI supplier contract must include:

| Provision | Key Points |
|-----------|-----------|
| **Responsible AI obligations** | Supplier must maintain responsible AI practices consistent with [Organisation]'s requirements |
| **Intended use limitations** | AI system may only be used for documented intended purposes; restrictions on downstream use |
| **Incident notification** | Supplier notifies [Organisation] within 24 hours of any serious AI incident and within 72 hours of any other material AI incident affecting [Organisation]'s use |
| **Audit rights** | [Organisation] (and regulators where required) may audit supplier's AI governance upon reasonable notice |
| **Data governance** | Training data, operational data, output data responsibilities clearly allocated; GDPR DPA where personal data involved |
| **EU AI Act compliance** | Where supplier's product is subject to EU AI Act, supplier maintains compliance and notifies [Organisation] of material compliance changes |
| **Change notification** | Supplier provides advance notice of material changes to AI system (model updates, training data changes, architecture changes) |
| **Exit and portability** | Transition provisions; data return or deletion; transition assistance |

If Legal cannot obtain a required provision, the gap is escalated to the AI Governance Officer and AI Risk Owner before contracting proceeds.

### 2.4 Ongoing Supplier Monitoring

AI suppliers are not set-and-forget. Ongoing monitoring includes:
- Periodic review proportionate to dependency and impact classification
- Triggered reviews: material incident / EU AI Act compliance change / significant model update / regulatory change
- Annual review at minimum for all significant AI suppliers

---

## Part 3 — Customer Obligations (A.10.4)

### 3.1 When A.10.4 Applies

A.10.4 applies when [Organisation] is in the **AI provider** role — delivering AI-enabled products or services to external customers. If [Organisation] is acting solely as an internal AI deployer, A.10.4 applies to internal business units treated as internal customers.

### 3.2 What Customers Must Receive

For each AI-enabled product or service delivered to customers, the Account Management/Customer Success team (with AI Governance Officer and Legal support) ensures customers receive:

| Information Category | When Provided |
|--------------------|--------------|
| AI system description (what AI does in this product) | At onboarding; in product documentation |
| Intended use | In contract and documentation |
| Limitations | In documentation; in onboarding |
| Customer responsibilities (human oversight obligations) | In contract; in training |
| Incident reporting (how to report to [Organisation]) | In documentation; in onboarding |
| Updates and material changes | Before each material AI system change |
| Data handling (how customer data is used in AI) | In contract; in privacy notice |

### 3.3 Customer Contract Provisions

Account Management must ensure customer contracts include:
- Intended use clause (customer's permitted uses defined; prohibition on out-of-scope use)
- Responsibility allocation (who holds deployer obligations under EU AI Act)
- Incident notification in both directions
- Prohibition on harmful use
- Limitation of liability where harm arises from customer's misuse

If a customer pushes back on these provisions, escalate to Legal and AI Governance Officer before agreeing to remove them.

---

<!-- QA_VERIFIED: 2026-04-15 -->
