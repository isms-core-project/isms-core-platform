<!-- ISMS-CORE:IMP:AI-IMP-A.10.2-4-TG:ai:TG:a.10.2-4 -->
**AI-IMP-A.10.2-4-TG — Third-Party and Customer Relationships — Technical Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Third-Party and Customer Relationships — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | AI-IMP-A.10.2-4-TG |
| **Related Policy** | AI-POL-A.10.2-4 (Third-Party and Customer Relationships) |
| **Document Creator** | AI Governance Officer / Legal / Procurement Officer |
| **Document Owner** | AI Governance Officer |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **AIMS Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | AI Governance Officer | Initial technical guide for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- AI-POL-A.10.2-4 (Third-Party and Customer Relationships — governing policy)
- AI-IMP-A.10.2-4-UG (Third-Party and Customer Relationships — User Guide)

---

## Purpose of This Guide

This guide provides the **schemas, templates, and reference structures** for managing AI-related obligations in third-party and customer relationships — including the AI Third-Party Responsibility Matrix schema, the AI supplier pre-procurement assessment schema, the AI supplier monitoring register schema, and the customer AI information register schema.

**Audience**: AI Governance Officer, Legal, Procurement, Account Management.

---

## 1. AI Third-Party Responsibility Matrix Schema (A.10.2)

Maintained by the AI Governance Officer. One record per multi-party AI arrangement. Document as a separate exhibit in the relevant contract and maintain a master register.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Arrangement ID | Text | M | Unique reference |
| Arrangement Type | Enum | M | Supplier / Customer / Co-development / Partner |
| [Organisation] Role (EU AI Act) | Enum | M | Provider / Deployer / Both / Neither |
| Third Party Name | Text | M | |
| Third Party Role (EU AI Act) | Enum | M | Provider / Deployer / Distributor / Importer / Other |
| AI System(s) Covered | Text | M | |
| Contract Reference | Text | M | |
| Effective Date | Date | M | |
| **Responsibility Allocation** | | | |
| AI system specification — Responsible Party | Text | M | [Organisation] / Third party / Shared |
| Training data governance — Responsible Party | Text | M | |
| V&V — Responsible Party | Text | M | |
| AISIA — Responsible Party | Text | M | |
| Regulatory compliance (EU AI Act) — Responsible Party | Text | M | Specify: provider obligations / deployer obligations |
| Monitoring and incident response — Responsible Party | Text | M | |
| User-facing transparency — Responsible Party | Text | M | |
| Right to erasure / personal data obligations — Responsible Party | Text | M | |
| Indemnity and liability allocation | Text | M | Summary of contractual allocation |
| GDPR DPA in place? | Boolean | C | Required if personal data involved |
| GDPR DPA Reference | Text | C | |
| Notes | Text | R | Any special considerations |
| Approved By | Text | M | AI Governance Officer |
| Last Reviewed | Date | M | |

---

## 2. AI Supplier Pre-Procurement Assessment Schema (A.10.3)

One assessment per AI supplier engagement. Completed before contracting.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Assessment ID | Text | M | |
| Supplier Name | Text | M | |
| AI Component / Service | Text | M | What is being procured |
| Assessment Date | Date | M | |
| Assessed By | Text | M | AI Governance Officer + other reviewers |
| Dependency Level | Enum | M | Critical / Significant / Standard |
| Impact Classification of Supported System(s) | Enum | M | Low / Medium / High |
| **Responsible AI Practices** | | | |
| Documented AI governance practices? | Enum | M | Yes / Partial / No / Unknown |
| ISO 42001 certification? | Boolean | M | Yes / No / In progress |
| EU AI Act conformity (if applicable)? | Enum | C | CE marked / Assessment in progress / Not yet / Not applicable |
| Public AI ethics commitments? | Enum | R | Yes / No |
| Responsible AI Evidence Summary | Text | M | |
| **EU AI Act Classification** | | | |
| AI component subject to EU AI Act? | Boolean | M | |
| Risk category if applicable | Enum | C | High-risk / Limited-risk / Minimal / GPAI |
| Conformity evidence reviewed? | Boolean | C | |
| EU AI Act Notes | Text | C | |
| **Data Governance** | | | |
| [Organisation] data processed by supplier's AI? | Boolean | M | |
| Data processing jurisdiction | Text | C | If Yes: where |
| Data governance practices — adequate? | Enum | C | Yes / Adequate / Concerns / No |
| Data Governance Notes | Text | C | |
| **Security** | | | |
| Security controls documented? | Enum | M | Yes / Partial / No |
| CVE/vulnerability management process? | Boolean | M | |
| Security assessment / certification held? | Text | R | e.g., SOC 2 Type II, ISO 27001 |
| Security Notes | Text | M | |
| **Incident Response** | | | |
| Incident response procedures for AI systems? | Boolean | M | |
| Notification obligation to customers documented? | Boolean | M | |
| Incident Response Notes | Text | M | |
| **Financial and Operational Resilience** | | | |
| Single-vendor dependency risk? | Boolean | M | |
| Business continuity plan available? | Boolean | R | |
| Resilience Notes | Text | R | |
| **Sub-suppliers / Fourth Parties** | | | |
| Key AI sub-components from fourth parties? | Text | R | Identify significant fourth-party AI dependencies |
| Fourth-party governance approach | Text | R | |
| **Assessment Outcome** | | | |
| Overall Assessment Result | Enum | M | Approved / Approved with conditions / Rejected |
| Conditions (if applicable) | Text | C | Contractual conditions required |
| Open Risks | Text | C | Known residual risks |
| Approved By | Text | M | AI Governance Officer |

---

## 3. AI Supplier Monitoring Register Schema (A.10.3)

Per-supplier monitoring records. Reviewed periodically (minimum annual) and on trigger events.

| Field | Type | Description |
|-------|------|-------------|
| Supplier ID | Text | |
| Supplier Name | Text | |
| AI Component / Service | Text | |
| Last Assessment Date | Date | |
| Next Scheduled Review | Date | |
| Dependency Level | Enum | Critical / Significant / Standard |
| **Review Events** | | |
| Review Date | Date | |
| Review Type | Enum | Scheduled / Post-incident / Model update / Regulatory change / Other |
| Triggered By | Text | |
| Review Findings | Text | |
| Action Required? | Boolean | |
| Action Description | Text | |
| Action Owner | Text | |
| Action Due Date | Date | |
| Action Status | Enum | Open / Complete |
| Review Approved By | Text | AI Governance Officer |

---

## 4. Customer AI Information Register Schema (A.10.4)

Per-customer (or per-product) register of AI information provided. Maintained by Account Management / AI Governance Officer.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Customer Name / Product | Text | M | |
| AI System(s) in Product/Service | Text | M | List of AI systems delivered to this customer |
| AI System Documentation Provided | Boolean | M | Is user documentation per A.8.2 provided? |
| Documentation Reference | Text | M | |
| Intended Use Communicated | Boolean | M | |
| Customer Responsibilities Communicated | Boolean | M | |
| Incident Reporting Process Communicated | Boolean | M | |
| Responsibility Allocation Documented | Boolean | M | Reference to AI Third-Party Responsibility Matrix |
| Contract AI Provisions Complete | Boolean | M | All mandatory contract provisions per AI-POL-A.10.2-4 in place |
| Contract Reference | Text | M | |
| Last Material AI Change Notified | Date | R | Date of most recent change notification to customer |
| Customer Training Provided? | Boolean | R | If required for responsible use |
| Data Handling Statement Provided | Boolean | M | How customer data is used in AI |
| Last Reviewed | Date | M | |

---

<!-- QA_VERIFIED: 2026-04-15 -->
