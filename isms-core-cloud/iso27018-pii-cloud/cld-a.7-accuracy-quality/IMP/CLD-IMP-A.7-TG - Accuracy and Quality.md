<!-- ISMS-CORE:IMP:CLD-IMP-A.7-TG:cloud:TG:a.7 -->
**CLD-IMP-A.7-TG — Accuracy and Quality — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Accuracy and Quality — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-IMP-A.7-TG |
| **Related Policy** | CLD-POL-A.7 (Accuracy and Quality) |
| **Document Creator** | CISO / Data Protection Officer (DPO) |
| **Document Owner** | CISO / Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial technical guide for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant regulatory change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-POL-A.7 (Accuracy and Quality — the governing policy)
- CLD-IMP-A.7-UG (Accuracy and Quality — User Guide)
- CLD-POL-A.9 (Individual Participation and Access)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for accuracy and data quality management. It covers:

- Rectification Request Log schema
- Data correction propagation checklist (all tiers)
- Audit trail schema for PII modifications
- Quality Check Log schema

**Audience**: CISO, DPO, Cloud Engineering, Cloud Service Delivery.

---

## 1. Rectification Request Log Schema

Maintained by Cloud Service Delivery. One entry per rectification request received from a PII controller.

| Field | Type | Description |
|-------|------|-------------|
| Request ID | Text | Unique reference (e.g., RECT-2026-001) |
| Date Received | Date | Date request was submitted by controller |
| Controller Name | Text | Name of PII controller submitting the request |
| Controller Contact | Text | Name and email of the authorised controller contact |
| Request Type | Enum | Correction / Deletion / Suppression |
| Affected Record Identifier(s) | Text | Record ID(s), account reference(s), or equivalent controller-provided identifier |
| PII Field(s) Affected | Text | Field names or data categories to be corrected |
| Current Value (if known) | Text | Existing value(s) — captured for audit trail |
| Corrected Value | Text | New value(s) specified by controller (for corrections) |
| Reason for Request | Text | Source of the rectification need (e.g., data subject request, internal discovery) |
| Clarification Required | Boolean | Yes / No — and if Yes, nature of clarification sought |
| Clarification Resolved Date | Date | Date clarification received from controller |
| Assigned to (Cloud Engineering) | Text | Engineer responsible for implementing correction |
| Primary Store Updated | Date | Date and time correction applied to primary data store |
| Propagation Completed | Date | Date correction confirmed across all replicated tiers |
| Controller Confirmation Sent | Date | Date written completion confirmation sent to controller |
| Status | Enum | Received / In Progress / Completed / Closed |
| Notes | Text | Complications, partial completions, escalations |

---

## 2. Data Correction Propagation Checklist

Completed by Cloud Engineering for each rectification. Attached to the Rectification Request Log entry.

**Request ID**: _______________
**Controller**: _______________
**Correction Summary**: _______________

| Tier | Action Required | Completed | Timestamp | Confirmed By |
|------|----------------|-----------|-----------|-------------|
| Primary data store | Direct write via standard write path | [ ] Yes / [ ] N/A | | |
| Read replicas | Confirm replication propagation — verify corrected value present in all read replicas | [ ] Yes / [ ] N/A | | |
| Application cache | Invalidate cache entries for affected record(s); confirm cache serves corrected value on next read | [ ] Yes / [ ] N/A | | |
| CDN / edge cache | Purge cached responses containing affected PII field(s), if applicable | [ ] Yes / [ ] N/A | | |
| Message queue / event stream | If correction event must be propagated downstream via event stream: publish correction event; confirm consumer acknowledgement | [ ] Yes / [ ] N/A | | |
| Scheduled backup | Add correction note to backup manifest for next cycle; or apply out-of-band correction if deadline requires | [ ] Yes / [ ] N/A | | |
| Archive / cold storage | DPO reviewed — correction required in archive? If yes: out-of-band correction applied | [ ] Yes / [ ] N/A | | |
| Sub-processor data copies | If sub-processor holds a copy of the affected PII: sub-processor notified and correction confirmed | [ ] Yes / [ ] N/A | | |

**All tiers confirmed complete**: [ ] Yes
**Cloud Engineering sign-off**: _________________________ Date: _____________
**CISO review (for material corrections)**: _________________________ Date: _____________

---

## 3. Audit Trail Schema — PII Modifications

All modifications to PII in [Organisation]'s cloud systems — whether from rectification requests, processing operations, or automated pipeline actions — SHALL be recorded in an immutable audit trail. Maintained by Cloud Engineering. Access: CISO, DPO, Legal/Compliance.

| Field | Type | Description |
|-------|------|-------------|
| Event ID | Text | Unique event reference (e.g., AUD-2026-000001) |
| Timestamp | Datetime | UTC timestamp of the modification event |
| Record Identifier | Text | Identifier of the modified record |
| PII Field Modified | Text | Field name(s) modified |
| Pre-Modification Value | Text | Value before modification (encrypted at rest) |
| Post-Modification Value | Text | Value after modification (encrypted at rest) |
| Modification Type | Enum | Rectification / Deletion / Suppression / Processing Transformation / System Operation |
| Initiated By | Enum | Controller / Cloud Engineering / Automated Pipeline / Sub-processor |
| Operator Identity | Text | User account or service account that executed the modification |
| Rectification Request Ref | Text | Linked Rectification Request Log entry (if applicable) |
| Controller | Text | PII controller whose data was modified |
| Immutability Confirmed | Boolean | Yes — audit log is append-only; no modification or deletion of this entry is permitted |

**Retention**: Audit trail records are retained for the duration of the controller's service contract plus 5 years.

---

## 4. Quality Check Log Schema

One entry per quality check run. Maintained by Cloud Engineering; reviewed by CISO quarterly.

| Field | Type | Description |
|-------|------|-------------|
| Check ID | Text | Unique reference (e.g., QC-2026-Q1-001) |
| Check Type | Enum | Data Completeness / Replication Consistency / Backup Integrity |
| Date Executed | Date | Date check was run |
| Service / Data Store | Text | Service component and data store checked |
| Controller (if scoped) | Text | Controller name, or "All" if cross-controller check |
| Method | Text | Query, hash comparison, restore test — describe the method used |
| Records in Scope (approx.) | Text | Approximate number of records or volume checked |
| Outcome | Enum | Pass / Pass with findings / Fail |
| Findings | Text | Description of any completeness gaps, inconsistencies, or backup failures found |
| Material Issue? | Boolean | Yes / No — material issue requires controller notification |
| Controller Notification Sent | Date | Date controller was notified (if material issue) |
| Remediation Action | Text | Action taken or planned; owner and deadline |
| Reviewed By (CISO) | Text | CISO name and review date |

---

<!-- QA_VERIFIED: [Date] -->
