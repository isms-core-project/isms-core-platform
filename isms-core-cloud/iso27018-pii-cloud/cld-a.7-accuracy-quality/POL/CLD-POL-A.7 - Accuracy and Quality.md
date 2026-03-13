<!-- ISMS-CORE:POLICY:CLD-POL-A.7:cloud:POL:a.7 -->
**CLD-POL-A.7 — Accuracy and Quality**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Public Cloud PII Processor — Accuracy and Quality |
| **Document Type** | Policy |
| **Document ID** | CLD-POL-A.7 |
| **Document Creator** | CISO / Data Protection Officer (DPO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial policy for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant service architecture change)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: CISO / Cloud Security Manager
- Secondary: Data Protection Officer (DPO)
- Final Authority: Executive Management

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- ISMS-POL-A.5.34 (Privacy and Protection of PII)
- CLD-POL-A.2 (Consent and Choice — data subject rights cooperation)
- CLD-POL-A.6 (Use, Retention and Disclosure Limitation)
- CLD-POL-A.9 (Individual Participation and Access)
- ISO/IEC 27018:2025 Annex A, Section A.7 (Accuracy and Quality — principle)
- ISO/IEC 27701:2025 Controls A.2.3.10 (processor — accuracy)
- GDPR Article 5(1)(d) (accuracy principle); Article 16 (right to rectification); Article 28(3)(e) (processor assists with data subject rights)
- CH FADP Article 6(4) (accuracy); Article 9(2)(c) (processor cooperation on data subject requests)

---

## Executive Summary

This policy establishes [Organisation]'s requirements as a public cloud PII processor with regard to accuracy and quality — specifically the obligation to maintain the integrity of PII stored in cloud systems, to provide mechanisms for PII controllers to correct, update, or delete inaccurate PII, and to avoid introducing data quality degradation through processing operations — in accordance with ISO/IEC 27018:2025 Annex A, Section A.7.

**Scope**: All PII stored or processed by [Organisation] on behalf of PII controllers.

**Principle Note**: ISO/IEC 27018:2025 Annex A, Section A.7 is a principle-level section with no additional sub-controls beyond the main body of the standard. This policy implements the principle as an operational commitment. The primary accountability for PII accuracy rests with the PII controller; [Organisation]'s role is to preserve and not degrade accuracy, and to provide tools for the controller to maintain it.

---

# Scope and Applicability

## ISO/IEC 27018:2025 — Section A.7

**Section A.7 — Accuracy and quality (principle)**
> *The cloud service provider shall implement controls to maintain the accuracy and completeness of PII. Mechanisms shall be provided to allow the PII controller to correct, update, or delete inaccurate PII. Quality checks shall be performed on PII stored or processed.*

## What This Policy Does NOT Cover

- Verifying the accuracy of PII provided to [Organisation] by the PII controller — accuracy of source data is the controller's responsibility
- Data quality standards for the controller's own processing — these are the controller's obligations under GDPR Article 5(1)(d)

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 5(1)(d) (accuracy — PII must be accurate and, where necessary, kept up to date; inaccurate PII must be erased or rectified without delay); Article 16 (right to rectification — the controller must be able to exercise this right, requiring processor cooperation); Article 28(3)(e) (processor assists controller with data subject rights obligations)
- **CH FADP**: Article 6(4) (accuracy and correction obligations); Article 9(2)(c) (processor cooperation with controller on data subject requests)
- **ISO/IEC 27018:2025**: Section A.7 principle

---

# Policy Statements: Accuracy and Quality (A.7)

## Data Integrity Preservation

[Organisation] SHALL implement technical controls ensuring that PII stored in cloud systems is not degraded, corrupted, or altered through processing operations except as authorised by the PII controller. Specifically:

- Storage systems SHALL implement integrity checking (e.g., checksums, cryptographic hashes) for PII data stores to detect unauthorised or accidental modification
- Transformation operations performed on PII during processing SHALL be reversible or logged, ensuring the original data can be verified or restored
- Backup and replication operations SHALL preserve PII accuracy and completeness without data loss

## Mechanisms for Controller Correction

[Organisation] SHALL provide PII controllers with technical capabilities to correct, update, and delete PII within cloud storage. These mechanisms SHALL:

- Allow field-level correction or full record update for structured PII data stores
- Propagate corrections to replicated copies (backups, read replicas, caches) within a reasonable timeframe — and in any case within the timeframe required for the controller to fulfil data subject rights obligations
- Generate a confirmation record when corrections are completed, including which records were modified and the timestamp

## Quality Checks

[Organisation] SHALL implement the following quality controls for PII data stores:

- **Data completeness checks**: Identify and flag records with missing mandatory fields that may indicate data corruption or incomplete transfer
- **Data consistency checks**: Verify PII consistency across replicated or distributed data stores to detect replication errors
- **Backup integrity verification**: Periodically restore and verify backup PII data to confirm backup integrity

Quality check results SHALL be logged and reviewed quarterly by the Cloud Engineering team. Material data quality issues SHALL be reported to the PII controller without undue delay.

## Processing-Induced Inaccuracy

Where [Organisation] performs data transformation, enrichment, or processing operations on PII on behalf of a controller, [Organisation] SHALL:

- Document the transformation logic and its effect on PII accuracy
- Obtain controller authorisation for any transformation that modifies PII attributes
- Alert the controller if a processing operation produces results that indicate potential inaccuracy in the source data

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO / Cloud Security Manager** | Owns integrity controls for PII data stores; ensures correction mechanisms are functional; oversees quality check programme |
| **Cloud Engineering** | Implements integrity checking, correction mechanisms, and quality check processes; investigates and resolves data quality issues |
| **Data Protection Officer (DPO)** | Advises on accuracy obligations under GDPR and FADP; reviews controller-facing capability documentation; monitors data quality incident escalations |
| **Cloud Service Delivery** | Communicates controller-reported accuracy issues to Cloud Engineering; tracks resolution and confirms completion to controller |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Integrity Check Configuration Records | Technical documentation of integrity checking mechanisms per data store | Current + 3 years |
| Correction Mechanism Documentation | Description of PII correction, update, and deletion tools available to controllers per service | Current + previous versions for 3 years |
| Quality Check Logs | Quarterly quality check results including completeness, consistency, and backup verification | 3 years |
| Data Quality Incident Records | Records of material data quality issues, controller notifications, and resolution | Duration of contract + 3 years |

---

# Audit Considerations

Auditors verifying compliance with CLD-POL-A.7 should expect to find:

- Technical documentation confirming integrity checking is implemented for PII data stores
- Evidence that PII controllers have access to correction, update, and deletion mechanisms within cloud services
- Quality check logs covering the audit period with documented review
- Any data quality incidents reported to controllers with resolution evidence

---

<!-- QA_VERIFIED: [Date] -->
