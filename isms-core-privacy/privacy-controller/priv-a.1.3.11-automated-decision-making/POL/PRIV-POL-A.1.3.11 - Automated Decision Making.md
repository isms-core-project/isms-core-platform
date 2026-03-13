<!-- ISMS-CORE:POLICY:PRIV-POL-A.1.3.11:privacy:POL:a.1.3.11 -->
**PRIV-POL-A.1.3.11 — Automated Decision Making**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Automated Decision Making |
| **Document Type** | Policy |
| **Document ID** | PRIV-POL-A.1.3.11 |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial policy for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Data Protection Officer (DPO)
- Secondary: Legal/Compliance Officer
- Final Authority: Executive Management

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- PRIV-POL-01 (Privacy Governance and Decision-Making Framework)
- PRIV-IMP-A.1.3.11-UG (Automated Decision Making — User Guide)
- PRIV-IMP-A.1.3.11-TG (Automated Decision Making — Technical Guide)
- PRIV-POL-A.1.3.5-10 (Data Subject Rights — sibling policy: human review right)
- PRIV-POL-A.1.3.2-4 (Transparency — sibling policy: transparency obligation for ADM)
- ISO/IEC 27701:2025 Control A.1.3.11
- ISO/IEC 27701:2025 Annex B (Implementation guidance B.1.3.11)
- GDPR Article 22 (Automated individual decision-making, including profiling); Recital 71
- CH FADP Article 21 (Automated individual decisions)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for identifying, documenting, and addressing obligations to PII principals arising from automated decision-making based solely on automated processing of PII — in accordance with ISO/IEC 27701:2025 Control A.1.3.11.

**Scope**: All processing activities where [Organisation], acting as PII Controller, makes decisions about individuals that are based solely on automated processing and that produce legal effects or similarly significant effects on those individuals; all profiling activities that feed such decisions.

**Role Applicability**: This policy applies to [Organisation] acting as **PII Controller only**. Control A.1.3.11 is controller-specific (Table A.1).

---

# Scope and Applicability

## ISO/IEC 27701:2025 Control Statement

**Control A.1.3.11 — Automated decision making**
Control A.1.3.11 requires [Organisation] to identify the obligations — including legal obligations — it holds towards PII principals in connection with decisions made solely through automated processing of their PII, and to demonstrate how those obligations are addressed.

## What This Policy Covers

- Automated decision-making activities that produce legal or similarly significant effects on data subjects
- Profiling activities that feed automated decisions
- Obligations to data subjects arising from such processing
- Demonstrability of how [Organisation] addresses those obligations

## What This Policy Does NOT Cover

- The technical implementation of ADM systems (see PRIV-IMP-A.1.3.11-TG)
- General AI/ML governance beyond privacy obligations
- Human-in-the-loop decision support systems where humans make the final decision (these are not subject to Article 22 restrictions, though transparency obligations still apply)

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 22 (right not to be subject to solely automated decision-making with significant effects; exceptions: contract, law, explicit consent — with safeguards); Article 13(2)(f) / 14(2)(g) (transparency about ADM existence, logic, significance, consequences); Recital 71 (profiling context and safeguards)
- **CH FADP**: Article 21 (right to explanation for automated decisions; right to request human review)
- **ISO/IEC 27701:2025**: Control A.1.3.11 (normative)

---

# Policy Statements

## Automated Decision Making Identification

[Organisation] SHALL identify and document all processing activities where:

- Decisions are made based solely on automated processing of PII (without meaningful human involvement), AND
- Those decisions produce legal effects or similarly significant effects on data subjects

Examples of significant effects include: denial of credit, automatic rejection of employment applications, insurance pricing, personalised pricing with material financial impact, automated exclusion from services.

**Not in scope** (though transparency obligations may still apply):
- Decision support tools where a human reviews and makes the final determination — provided the review is meaningful, i.e., the reviewer has the information and ability to override the automated output
- Automated filtering that provides options but does not make the final decision

The DPO maintains an **ADM Register** listing all in-scope automated decision-making activities.

## Obligations Identification

For each ADM activity, [Organisation] SHALL identify and document obligations to data subjects, including:

- The right not to be subject to the decision (Article 22(1)) unless an exception applies
- Applicable exceptions: necessary for contract (Article 22(2)(a)), authorised by Union/Member State law (Article 22(2)(b)), or explicit consent (Article 22(2)(c))
- Where an exception applies: safeguards required (right to obtain human intervention, right to express point of view, right to contest the decision)
- Transparency obligations: data subjects must be informed of the existence of ADM, the logic involved, and the significance and envisaged consequences

## Safeguards for In-Scope ADM

Where ADM produces significant effects and an exception to Article 22 is invoked, [Organisation] SHALL implement:

1. **Human review right**: A mechanism for data subjects to request human intervention — either (a) before the decision is acted upon, or (b) as part of contesting a decision already communicated. The reviewer must have the information and authority to override the automated output; perfunctory review does not satisfy this safeguard
2. **Point of view**: A mechanism for data subjects to express their point of view about the automated decision
3. **Contestation**: A mechanism for data subjects to contest the automated decision

These safeguards SHALL be communicated to data subjects in the privacy notice and upon the automated decision being communicated to them.

## Transparency

For each ADM activity in scope, the transparency information provided to data subjects (per PRIV-POL-A.1.3.2-4) SHALL include:

- The existence of automated decision-making
- Meaningful information about the logic involved (at a level data subjects can understand — not proprietary algorithm disclosure)
- The significance and envisaged consequences of such processing for the data subject

## Special Category PII in ADM

ADM that processes special category PII requires an Article 9(2) condition in addition to an Article 22 exception. Such processing requires explicit DPO approval and, in most cases, a DPIA (per PRIV-POL-A.1.2.6-9).

## Demonstrability

[Organisation] SHALL be able to demonstrate how it addresses its obligations for each ADM activity at any time — to supervisory authorities, data subjects, and certification auditors. The ADM Register and associated documentation (including DPIA where conducted) are the primary demonstrability evidence.

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Data Protection Officer (DPO)** | Maintains ADM Register; approves new ADM activities; reviews obligations identification; approves safeguards design; DPIAs for ADM processing |
| **Legal/Compliance** | Advises on applicable exceptions to Article 22; reviews legal basis for ADM; advises on Article 22 safeguards adequacy |
| **Development / Data Science Teams** | Identify ADM activities in systems they build; notify DPO before deploying ADM; implement human review and contestation mechanisms |
| **Product Management** | Ensure ADM activities are flagged to DPO during product design; support safeguards implementation |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| ADM Register | All ADM activities with legal basis, exception invoked, safeguards, transparency | Current + 3 years |
| DPIAs for ADM | Where ADM involves high-risk processing | Duration of ADM + 3 years |
| Safeguard Implementation Evidence | Technical records of human review mechanism, contestation process | Current + 3 years |
| Data Subject Rights Register | Requests for human review, point-of-view, or contestation | 5 years |

---

# Audit Considerations

Auditors verifying compliance with A.1.3.11 should expect to find:

- ADM Register identifying all in-scope automated decision-making activities
- For each activity: documented exception to Article 22(1) invoked and safeguards in place
- Transparency information in privacy notice covering ADM existence, logic, and consequences
- Human review, point-of-view, and contestation mechanisms operational and accessible
- DPIA conducted for high-risk ADM activities

---

<!-- QA_VERIFIED: [Date] -->
