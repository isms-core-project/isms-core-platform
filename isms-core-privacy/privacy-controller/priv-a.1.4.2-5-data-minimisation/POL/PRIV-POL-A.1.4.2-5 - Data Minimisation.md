<!-- ISMS-CORE:POLICY:PRIV-POL-A.1.4.2-5:privacy:POL:a.1.4.2-5 -->
**PRIV-POL-A.1.4.2-5 — Data Minimisation**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Data Minimisation |
| **Document Type** | Policy |
| **Document ID** | PRIV-POL-A.1.4.2-5 |
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
- PRIV-IMP-A.1.4.2-5-UG (Data Minimisation — User Guide)
- PRIV-IMP-A.1.4.2-5-TG (Data Minimisation — Technical Guide)
- PRIV-POL-A.1.4.6-10 (PII Lifecycle, Retention and Disposal — sibling policy)
- PRIV-POL-A.3.23-31 (Technical Controls for PII — pseudonymisation and anonymisation)
- ISO/IEC 27701:2025 Controls A.1.4.2, A.1.4.3, A.1.4.4, A.1.4.5
- ISO/IEC 27701:2025 Annex B (Implementation guidance B.1.4.2 through B.1.4.5)
- GDPR Article 5(1)(b) (purpose limitation); Article 5(1)(c) (data minimisation); Article 5(1)(d) (accuracy)
- CH FADP Article 6(2) (proportionality principle)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for limiting PII collection, limiting PII processing, ensuring PII accuracy and quality, and defining data minimisation objectives and mechanisms — in accordance with ISO/IEC 27701:2025 Controls A.1.4.2, A.1.4.3, A.1.4.4, and A.1.4.5.

**Scope**: All PII collected and processed by [Organisation] as PII Controller; all systems and processes involved in PII collection or processing; all personnel who design or operate PII processing activities.

**Role Applicability**: This policy applies to [Organisation] acting as **PII Controller only**. Controls A.1.4.2–A.1.4.5 are controller-specific (Table A.1) within the Privacy by Design and Privacy by Default objective group.

**Combined Control Rationale**: A.1.4.2–A.1.4.5 operationalise the data minimisation and accuracy principles of GDPR Article 5. Limiting collection (A.1.4.2) restricts what is gathered; limiting processing (A.1.4.3) restricts what is done with it; accuracy (A.1.4.4) ensures what is held is correct; minimisation objectives (A.1.4.5) create the institutional commitment and mechanisms to sustain these disciplines.

---

# Scope and Applicability

## ISO/IEC 27701:2025 Control Statements

**Control A.1.4.2 — Limit collection**
Control A.1.4.2 requires [Organisation] to collect only the PII that is relevant, proportional, and necessary for the identified processing purpose — no more.

**Control A.1.4.3 — Limit processing**
Control A.1.4.3 requires [Organisation] to limit the processing of PII to what is adequate, relevant, and necessary for the identified purposes, and not to process PII beyond those bounds.

**Control A.1.4.4 — Accuracy and quality**
Control A.1.4.4 requires [Organisation] to ensure that PII is as accurate, complete, and up to date as the processing purpose demands, and to maintain that standard throughout the PII lifecycle.

**Control A.1.4.5 — PII minimisation objectives**
Control A.1.4.5 requires [Organisation] to define and document its data minimisation objectives, along with the mechanisms — such as de-identification — it uses to achieve them.

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 5(1)(b) (purpose limitation — no further incompatible processing); Article 5(1)(c) (data minimisation — adequate, relevant, limited to what is necessary); Article 5(1)(d) (accuracy — kept up to date, inaccurate data erased or rectified without delay); Article 25(1) (privacy by design — data minimisation a design requirement)
- **CH FADP**: Article 6(2) (proportionality — processing limited to what is necessary for the purpose)
- **ISO/IEC 27701:2025**: Controls A.1.4.2–A.1.4.5 (normative)

---

# Policy Statements

## A.1.4.2 — Limit Collection

[Organisation] SHALL limit the collection of PII to the minimum that is relevant, proportional, and necessary for the identified purposes.

### Collection Minimisation Requirements

- PII fields collected in any form (online, physical, telephone, third-party import) SHALL be reviewed and justified before collection commences
- Each data field collected SHALL be traceable to a specific documented purpose; fields without a documented purpose SHALL NOT be collected
- New data collection points (forms, APIs, integrations) require DPO review of the fields to be collected before deployment
- Collection of PII that is not necessary for a documented purpose is not permitted, regardless of potential future utility; data minimisation shall be the default at the design stage (privacy by design per GDPR Article 25)

---

## A.1.4.3 — Limit Processing

[Organisation] SHALL limit the processing of PII to that which is adequate, relevant, and necessary for the identified purposes.

### Processing Minimisation Requirements

- Access to PII for processing SHALL be restricted to personnel and systems with a documented processing purpose (minimum necessary principle)
- Secondary processing of PII for a purpose not identified at collection requires a purpose compatibility assessment (per PRIV-POL-A.1.2.2-5) and a new lawful basis where required
- Aggregation, profiling, or analytics that go beyond the documented purpose require DPO assessment before commencement
- Where the processing purpose can be fulfilled with pseudonymised or anonymised data, the pseudonymised/anonymised version SHALL be used in preference to identifiable PII

---

## A.1.4.4 — Accuracy and Quality

[Organisation] SHALL ensure that PII held and processed is as accurate, complete, and up to date as necessary for the processing purposes, throughout the lifecycle of the PII.

### Accuracy Requirements

- Collection processes SHALL include reasonable validation measures to prevent the entry of obviously inaccurate data (e.g., date format validation, email format validation)
- PII that is known to change over time SHALL have a defined review or update mechanism
- Where inaccurate PII is identified — whether by [Organisation] or through a data subject rectification request — it SHALL be corrected without undue delay
- PII used for significant decisions (financial, health, legal) SHALL have enhanced accuracy controls, documented in PRIV-IMP-A.1.4.2-5-TG
- [Organisation] SHALL NOT retain PII that has become inaccurate for purposes where accuracy is necessary, when the inaccuracy cannot be corrected

---

## A.1.4.5 — PII Minimisation Objectives

[Organisation] SHALL define and document data minimisation objectives and the mechanisms used to meet those objectives.

### Minimisation Objectives

[Organisation]'s documented PII minimisation objectives are:

1. **Collection minimisation**: Collect only fields necessary for documented purposes — assessed at design, verified in RoPA
2. **Processing minimisation**: Process PII only for documented purposes — enforced through access controls and purpose limitation
3. **Retention minimisation**: Retain PII only as long as necessary — enforced through retention schedules per PRIV-POL-A.1.4.6-10
4. **De-identification for secondary use**: Use pseudonymised or anonymised data for analytics, testing, and research wherever possible — mechanisms per PRIV-POL-A.3.23-31
5. **Aggregation minimisation**: Avoid creating aggregates that re-identify or over-identify data subjects beyond the processing purpose

### De-identification Mechanisms

[Organisation] uses the following de-identification mechanisms (documented in detail in PRIV-IMP-A.1.4.2-5-TG):

- **Pseudonymisation**: Replace direct identifiers with pseudonyms — dataset can be re-identified with the key; classified as PII under GDPR
- **Anonymisation**: Irreversible removal of identifying information such that re-identification is not reasonably possible — confirmed by the DPO using a documented methodology (referenced in PRIV-IMP-A.1.4.2-5-TG) that assesses singling out, linkability, and inference as re-identification risk vectors; output confirmed by DPO is no longer PII

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Data Protection Officer (DPO)** | Approves new collection fields; reviews processing minimisation compliance; confirms anonymisation; maintains minimisation objectives documentation |
| **Development / Product** | Implements privacy by default (minimisation is the default); submits new collection for DPO review; implements pseudonymisation mechanisms |
| **Data Owner** | Ensures PII in their domain is accurate and current; initiates correction upon identification of inaccurate data |
| **All Personnel** | Avoid collecting PII beyond documented requirements; report suspected unnecessary collection or processing to Privacy Champion / DPO |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| RoPA — Data Fields Section | Documentation of PII fields collected per activity with purpose justification | Current + 3 years |
| Privacy by Design Review Records | DPO sign-off on new data collection points | Current + 3 years |
| Anonymisation Confirmation Records | DPO confirmation that a dataset is truly anonymised | Duration of reliance on the anonymisation determination + 3 years |
| Minimisation Objectives Document | Documented objectives and mechanisms | Current + 3 years |

---

# Audit Considerations

- RoPA with data fields traceable to specific purposes
- Evidence of DPO review before new data collection deployments
- Pseudonymisation/anonymisation mechanisms documented and used for secondary processing
- Accuracy measures in collection processes; correction procedures operational
- Minimisation objectives documented and evidenced in practice

---

<!-- QA_VERIFIED: [Date] -->
