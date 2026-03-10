<!-- ISMS-CORE:IMP:CLD-IMP-A.7-UG:cloud:UG:a.7 -->
**CLD-IMP-A.7-UG — Accuracy and Quality — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Accuracy and Quality — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-IMP-A.7-UG |
| **Related Policy** | CLD-POL-A.7 (Accuracy and Quality) |
| **Document Creator** | CISO / Data Protection Officer (DPO) |
| **Document Owner** | CISO / Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial user guide for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant service architecture change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-POL-A.7 (Accuracy and Quality — the governing policy)
- CLD-IMP-A.7-TG (Accuracy and Quality — Technical Guide)
- CLD-POL-A.2 (Consent and Choice — data subject rights cooperation)
- CLD-POL-A.9 (Individual Participation and Access — controller tools for subject access)
- CLD-POL-A.6 (Use, Retention and Disclosure Limitation — retention and deletion)

---

## Purpose of This Guide

This guide explains how [Organisation] fulfils its accuracy and data quality obligations as a public cloud PII processor. It covers how cloud service delivery handles PII rectification requests raised by controllers, the technical procedures for implementing corrections, and how corrections are propagated across replicated data stores.

**Who this guide is for**: Cloud Service Delivery, Cloud Engineering, DPO.

**Cloud processor context**: This guide applies to [Organisation] acting as a public cloud PII processor under ISO/IEC 27018:2025. [Organisation] does not originate PII — accuracy of source data remains the PII controller's responsibility. [Organisation]'s obligations are to preserve accuracy, not degrade it through processing, and to provide the technical means for controllers to correct PII held in cloud storage.

---

## Part 1 — How Cloud Service Delivery Handles Controller Rectification Requests

### 1.1 Receiving a Rectification Request

PII controllers submit rectification requests when they need to correct, update, or delete PII stored by [Organisation] on their behalf. Requests may arise from:

- A data subject exercising their right to rectification (GDPR Article 16)
- The controller identifying an internal data quality issue
- A third-party notification of inaccurate PII

Rectification requests SHALL be submitted by the controller to the Cloud Service Delivery contact designated in the service agreement. All requests are logged in the Rectification Request Log (see CLD-IMP-A.7-TG) upon receipt.

### 1.2 Assessing the Request

Cloud Service Delivery reviews the request to confirm:

1. The request identifies the affected records with sufficient specificity (record ID, account reference, or equivalent)
2. The correction requested is within the scope of PII [Organisation] holds for the controller
3. The request is submitted by an authorised contact under the service agreement

Where a request is ambiguous or incomplete, Cloud Service Delivery contacts the controller for clarification within 2 business days.

### 1.3 Escalating to Cloud Engineering

Cloud Service Delivery passes confirmed requests to Cloud Engineering with the following details:

- Affected record identifier(s)
- PII field(s) to be corrected and the corrected value(s)
- Whether the request is a correction (update value), deletion (remove field or record), or suppression (retain but flag as disputed)
- Deadline — [Organisation] SHALL complete PII rectification within a timeframe that allows the controller to fulfil its own data subject rights obligations (standard SLA: 5 business days from confirmed request; expedited where controller provides a tighter deadline)

---

## Part 2 — Technical Procedures for Implementing Rectification

### 2.1 Applying the Correction

Cloud Engineering applies the correction to the **primary data store** for the affected service. The correction is applied using the standard write path (same API/database layer used for normal data operations) to ensure that integrity controls and audit logging are triggered.

Before applying the correction:

- Cloud Engineering confirms the record identifier matches the controller's specification
- A pre-correction snapshot of the affected record is captured and retained in the Audit Trail (see CLD-IMP-A.7-TG)

After applying the correction:

- Cloud Engineering confirms the corrected value is written correctly
- The Rectification Request Log is updated with correction timestamp and operator identity

### 2.2 Propagating Corrections Across Replicated Data

PII stored in cloud services may be replicated across multiple tiers. Cloud Engineering SHALL propagate corrections to all replicated copies in the following order:

| Tier | Propagation Method | Target Completion |
|------|--------------------|-------------------|
| Primary data store | Direct write — applied first | Immediate |
| Read replicas | Replication lag — correction propagates automatically via replication stream | Within replication SLA (typically seconds to minutes) |
| Caches | Cache invalidation — entry evicted and refreshed from corrected primary | Within cache TTL or immediate invalidation if PII risk |
| Backup copies | Flag applied — correction noted in backup manifest; applied at next scheduled backup cycle | Within next backup cycle |
| Archive copies | DPO reviews whether archive copy requires correction; if so, Cloud Engineering applies out-of-band correction | Within 30 days or controller-specified deadline |

Where replication is asynchronous and a completion guarantee is required (e.g., GDPR rectification deadline), Cloud Engineering performs a forced synchronisation and confirms propagation before reporting completion.

### 2.3 Confirming Completion to the Controller

Cloud Service Delivery sends a written confirmation to the controller once correction is propagated across all tiers listed above. The confirmation includes:

- Record identifier(s) corrected
- Field(s) updated and confirmation of new value (where the controller requested confirmation)
- Propagation confirmation across each data tier
- Date and time of completion

This confirmation record is retained in the Rectification Request Log.

---

## Part 3 — Quality Checks and Processing-Induced Inaccuracy

### 3.1 Scheduled Quality Checks

Cloud Engineering runs the following quality checks quarterly:

| Check Type | Scope | Method | Output |
|-----------|-------|--------|--------|
| Data completeness | All PII data stores | Query for records with missing mandatory fields | Quality Check Log entry; material gaps reported to controller |
| Replication consistency | Primary vs. read replicas | Hash comparison of record counts and field-level spot checks | Consistency confirmation or discrepancy report |
| Backup integrity | All scheduled backups | Restore sample to isolated test environment; verify record count and field completeness | Backup Integrity Log entry |

Results are recorded in the Quality Check Log and reviewed by the CISO quarterly. Any material data quality issue (completeness gap, replication discrepancy, or backup failure) is reported to the affected PII controller without undue delay.

### 3.2 Transformation Operations and Processing-Induced Inaccuracy

Where [Organisation] performs data transformation or enrichment operations on controller PII:

1. Cloud Engineering documents the transformation logic prior to implementation and obtains DPO confirmation that it does not modify PII in a way that could introduce inaccuracy
2. All transformations are reversible or logged, enabling the original value to be recovered
3. If a processing operation produces output that indicates potential inaccuracy in the source data (e.g., a validation rule flags an unexpected pattern), Cloud Service Delivery alerts the controller within 2 business days

Unauthorised transformation of PII (i.e., modification not specified in the controller's processing instructions) is prohibited. Cloud Engineering configurations SHALL enforce this at the service level.

---

## Evidence Checklist

- [ ] Rectification Request Log — all requests received, dated, and tracked to completion
- [ ] Correction propagation confirmations — written confirmations sent to controllers, retained
- [ ] Audit trail records — pre- and post-correction snapshots per rectification event
- [ ] Quality Check Logs — quarterly, covering completeness, consistency, and backup verification
- [ ] Material data quality incident records — controller notifications and resolution evidence
- [ ] Backup integrity verification records — sample restore results per scheduled backup cycle

---

<!-- QA_VERIFIED: [Date] -->
