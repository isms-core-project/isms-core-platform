<!-- ISMS-CORE:IMP:AI-IMP-A.2.2-4-TG:ai:TG:a.2.2-4 -->
**AI-IMP-A.2.2-4-TG — AI Policy Framework — Technical Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI Policy Framework — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | AI-IMP-A.2.2-4-TG |
| **Related Policy** | AI-POL-A.2.2-4 (AI Policy Framework) |
| **Document Creator** | AI Governance Officer |
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

- AI-POL-A.2.2-4 (AI Policy Framework — governing policy)
- AI-IMP-A.2.2-4-UG (AI Policy Framework — User Guide)

---

## Purpose of This Guide

This guide provides the **document structures, templates, and schemas** for the AI policy framework — including the AIMS policy document template, the AIMS document register schema, and the Responsible AI Principles Statement template. It is the technical companion to the AI-IMP-A.2.2-4-UG process guide.

**Audience**: AI Governance Officer, document control function, compliance staff.

---

## 1. AIMS Policy Document Template

All AIMS policy documents (AI-POL-xx series) shall use the following structure. The template ensures consistency across all policies and provides the minimum content required for ISO 42001:2023 compliance.

---

```
<!-- ISMS-CORE:POLICY:[DOCUMENT-ID]:[product]:[type]:[control-ref] -->
**[DOCUMENT-ID] — [Document Title]**

---

## Document Control

| Field | Value |
|-------|-------|
| Document Title | [Full title] |
| Document Type | Policy |
| Document ID | [AI-POL-Ax.x-x or AI-POL-0x] |
| Document Creator | [Role(s)] |
| Document Owner | [Role — typically CEO or AI Governance Officer] |
| Approved By | [Executive Management / AI Governance Officer] |
| Created Date | [Date to be set] |
| Version | 1.0 |
| Version Date | [Date to be set] |
| Classification | Internal |
| Status | Draft |
| AIMS Product Version | 1.0 |

**Version History**: [Table: Version / Date / Author / Changes]

**Review Cycle**: [Annual / triggered by specific events]
**Next Review Date**: [Effective Date + X months]

**Approval Chain**:
- Primary: [Role]
- Secondary: [Role]
- Compliance: [Role]
- Final Authority: [Executive Management / CEO]

**Related Documents**: [Cross-references]

---

## Executive Summary
[2–4 paragraphs: what this policy covers; scope; purpose; combined control rationale if applicable]

---

## Scope and Applicability

### ISO/IEC 42001:2023 Control Statements
[Verbatim control text for each control addressed]

### What This Policy Covers
[Bullet list of what is in scope]

### What This Policy Does NOT Cover
[Explicit exclusions with cross-references]

### Regulatory Framework
[Tier 1 / Tier 2 / Tier 3 per AI-POL-00]

---

## Policy Statements: [Control Area 1]
[Policy requirements — SHALL statements]

---

## Policy Statements: [Control Area 2]
[Policy requirements — SHALL statements]

[Repeat per control group addressed]

---

## Roles and Responsibilities
[Table: Role / Responsibilities]

---

## Evidence Requirements
[Table: Evidence / Description / Retention]

---

## Audit Considerations
[Bullet list of what auditors should expect to find]

---

<!-- QA_VERIFIED: [YYYY-MM-DD] -->
```

---

## 2. AIMS Document Register Schema

The AI Governance Officer maintains an AIMS Document Register. The register tracks all policy documents, implementation guides, and key AIMS records. Minimum fields:

| Field | Type | Description |
|-------|------|-------------|
| Document ID | Text | e.g., AI-POL-A.2.2-4 |
| Document Title | Text | Full document title |
| Document Type | Enum | Policy / IMP-UG / IMP-TG / SCR / Template |
| Control Reference | Text | ISO 42001:2023 control(s) addressed |
| Version | Text | Current version number |
| Status | Enum | Draft / Under Review / Approved / Superseded |
| Owner | Text | Document owner role |
| Approver | Text | Approver role |
| Approval Date | Date | Date of current version approval |
| Next Review Date | Date | Scheduled review date |
| File Location | URL/Path | Location of current version |
| Related Documents | Text | Comma-separated related document IDs |
| Notes | Text | Any notes on scope, exclusions, or open items |

---

## 3. Responsible AI Principles Statement Template

The AI Governance Officer publishes a Responsible AI Principles Statement for external and internal communication. This is a derived document from AI-POL-A.2.2-4 — a plain-language summary, not a new policy. Template:

---

```
[ORGANISATION] RESPONSIBLE AI PRINCIPLES

Version: [X.X] | Date: [YYYY-MM-DD]

[Organisation] is committed to the responsible development and use of artificial 
intelligence systems. Our AI management system is certified / aligned to 
ISO/IEC 42001:2023. Our AI governance is guided by five core principles:

1. HUMAN AGENCY AND OVERSIGHT
   We design AI systems to support, not replace, human judgment. For 
   consequential decisions, human review is required before action is taken.
   Users of AI systems at [Organisation] are trained that accountability for
   decisions remains with the person, not the AI.

2. FAIRNESS AND NON-DISCRIMINATION
   We assess AI systems for potential bias and discriminatory impact before
   deployment and in operation. We are committed to equitable AI outcomes
   across all groups our AI systems affect.

3. PRIVACY BY DESIGN
   Personal data is processed in AI systems only where a lawful basis exists
   and only to the extent necessary. Privacy risks are assessed before
   AI deployment.

4. ROBUSTNESS, SECURITY, AND SAFETY
   Our AI systems undergo validation and testing before deployment. We monitor
   performance in operation and respond to incidents promptly.

5. ACCOUNTABILITY AND TRANSPARENCY
   Every AI system has an accountable owner. We provide transparency 
   information to users and affected individuals. Our AI governance 
   records are available to auditors and, where required, to regulators.

For enquiries about our AI governance practices: [Contact]
```

---

## 4. AIMS Scope Statement Template

ISO 42001:2023 Clause 4 requires the scope of the AIMS to be documented. Template:

---

```
AIMS SCOPE STATEMENT
Document ID: AIMS-SCOPE-01 | Version: [X.X] | Date: [YYYY-MM-DD]

Organisation: [Organisation full legal name]

AIMS Scope:
[Organisation]'s AI Management System (AIMS) covers the following AI systems 
and activities:

[Describe: which AI systems are in scope; which business units or functions; 
which geographic locations; which products or services involving AI]

Exclusions from AIMS Scope:
[Where applicable: describe any AI systems or activities explicitly excluded, 
with justification]

AI System Portfolio (in-scope):
[List or reference the AI System Resource Register]

Applicable Standards and Regulations:
- ISO/IEC 42001:2023 (normative — certification target)
- EU AI Act (Regulation 2024/1689) — see AI-POL-00 for role determination
- GDPR — see PRIV-POL-00 for AI data processing obligations
- [Other applicable regulations per AI-POL-00]

Approved by: [AI Governance Officer] | [Date]
Reviewed by: [Executive Management] | [Date]
```

---

## 5. AI Governance Calendar Template

The AI Governance Officer maintains an annual governance calendar to ensure all required reviews, assessments, and reporting activities occur on schedule. Minimum recurring activities:

| Activity | Frequency | Responsible | Due Date |
|---------|-----------|-------------|----------|
| AIMS management review | Annual | AI Governance Officer + Executive Management | [Month] |
| AIMS internal audit | Annual | Internal audit / AI Governance Officer | [Month] |
| AI policy review cycle | Annual (per policy schedule) | AI Governance Officer | Rolling |
| AISIA reviews — High-impact | Every 6 months per system | AI System Owner | Per system schedule |
| AISIA reviews — Medium-impact | Annual per system | AI System Owner | Per system schedule |
| AISIA reviews — Low-impact | Every 3 years per system | AI System Owner | Per system schedule |
| EU AI Act compliance status review | Annual | Legal / AI Governance Officer | [Month] |
| AI System Resource Register update | On change + annual confirmation | AI System Owners | [Month] |
| Responsible AI Principles Statement review | Annual | AI Governance Officer | [Month] |
| AIMS Scope Statement review | Annual | AI Governance Officer | [Month] |
| Staff AI awareness training refresh | Annual | AI System Owners / HR | [Month] |

---

<!-- QA_VERIFIED: [2026-04-15] -->
