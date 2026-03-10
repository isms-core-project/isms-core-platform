<!-- ISMS-CORE:IMP:CLD-IMP-A.2-TG:cloud:TG:a.2 -->
**CLD-IMP-A.2-TG — Consent and Choice — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Consent and Choice — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-IMP-A.2-TG |
| **Related Policy** | CLD-POL-A.2 (Consent and Choice) |
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

- CLD-POL-A.2 (Consent and Choice — the governing policy)
- CLD-IMP-A.2-UG (Consent and Choice — User Guide)
- CLD-POL-A.9 (Individual Participation and Access)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for implementing [Organisation]'s data subject rights cooperation capabilities and the associated records management requirements under ISO/IEC 27018:2025 Annex A, Controls A.2 and A.2.1. It covers:

- Data subject rights technical capability matrix and service-level checklist
- Cooperation Request Log schema
- Legally Compelled Processing Record template (for A.2 events)

**Audience**: CISO, DPO, Cloud Engineering, Legal/Compliance.

---

## 1. Data Subject Rights Technical Capability Matrix

CLD-POL-A.2 requires [Organisation] to implement and maintain technical capabilities enabling PII controllers to fulfil data subject rights. This section provides the capability checklist that Cloud Engineering must implement and the CISO must verify annually.

### 1.1 Capability Requirements Per Right

| Right | ISO/GDPR Reference | Required Capability | Implementation Method | Verified (Y/N) | Verification Date |
|-------|--------------------|--------------------|-----------------------|----------------|-------------------|
| **Access** | GDPR Art. 15 | Export all PII associated with a data subject in machine-readable format | API endpoint or admin console export function returning structured JSON/CSV | | |
| **Rectification** | GDPR Art. 16 | Update or correct specific PII fields for a named data subject | Admin UI field edit or API PATCH endpoint; change logged with timestamp | | |
| **Erasure** | GDPR Art. 17 | Confirmed deletion of PII and all replicated or cached copies, including backups | Deletion API with cascade to backups; deletion confirmation record with timestamp; backup purge cycle documented | | |
| **Restriction** | GDPR Art. 18 | Flag and isolate PII from active processing without deletion | Status flag on data subject record; restricted records excluded from queries; flag auditable | | |
| **Portability** | GDPR Art. 20 | Export PII in structured, commonly used, machine-readable format | Export in JSON and/or CSV; export includes all PII categories held; file delivered via secure channel | | |
| **Objection** | GDPR Art. 21 | Suspend automated processing involving specific PII | Processing exclusion flag; automated processing pipelines check flag before including record | | |

### 1.2 Service-Level Capability Assessment Checklist

For each cloud service that processes PII on behalf of controllers, Cloud Engineering completes this checklist annually (or upon material service architecture change):

| Service Name | Access Export | Rectification | Erasure (incl. backups) | Restriction Flag | Portability Export | Objection Flag | Gaps / Remediation Plan |
|--------------|:---:|:---:|:---:|:---:|:---:|:---:|---------|
| [Service 1] | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | |
| [Service 2] | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | |
| [Add rows] | | | | | | | |

**Assessment completed by (Cloud Engineering Lead)**: _________________________ Date: _____________
**Reviewed by (CISO)**: _________________________ Date: _____________
**DPO sign-off**: _________________________ Date: _____________

### 1.3 Backup and Cache Erasure Technical Note

Erasure requests must cascade to all copies of the affected PII. Cloud Engineering documents the following for each service:

| Copy Type | Location | Deletion Method | Deletion Lag (max) | Confirmation Method |
|-----------|----------|-----------------|---------------------|---------------------|
| Primary database | [e.g., PostgreSQL prod] | Hard delete or anonymisation | Immediate | DB deletion log |
| Read replica(s) | [e.g., PostgreSQL replica] | Cascade from primary | [e.g., < 5 min] | Replication lag monitor |
| Backup snapshots | [e.g., S3 encrypted snapshots] | Overwrite on next backup cycle + explicit purge | [e.g., ≤ 30 days] | Backup system purge log |
| CDN / application cache | [e.g., Redis, Varnish] | Cache invalidation on delete | [e.g., < 1 hour] | Cache invalidation log |
| Log archives | [e.g., CloudWatch, ELK] | Redaction or truncation on next log rotation | [e.g., ≤ 90 days per retention schedule] | Log rotation audit record |

This table must be completed per service and reviewed whenever service architecture changes.

---

## 2. Cooperation Request Log Schema

The Cooperation Request Log records all controller cooperation requests for data subject rights assistance, as well as any escalations arising from out-of-scope processing requests. Maintained by Cloud Service Delivery; reviewed quarterly by the DPO.

| Field | Type | Description |
|-------|------|-------------|
| `request_id` | String (unique) | Internal reference: `CRQ-YYYY-NNN` |
| `agreement_id` | String | Reference to the Processor Agreement Register |
| `controller_name` | String | Legal name of the requesting PII controller |
| `request_type` | Enum | Data subject right: Access / Rectification / Erasure / Restriction / Portability / Objection / Out-of-scope processing escalation |
| `data_subject_reference` | String | Internal reference for the data subject (do not record name — use controller-supplied identifier) |
| `date_received` | Date | Date request was received by Cloud Service Delivery |
| `date_acknowledged` | Date | Date acknowledgement was sent to controller |
| `controller_deadline` | Date | Deadline provided by the controller for regulatory compliance |
| `assigned_to` | String | Name of Cloud Service Delivery team member assigned |
| `pii_categories_affected` | Text | PII categories involved in the request |
| `service_name` | String | Cloud service in scope for this request |
| `technical_action_required` | Text | Technical actions required to fulfil the request |
| `technical_constraint_identified` | Boolean | Whether a technical constraint was identified |
| `constraint_description` | Text | Description of constraint and revised timeline (if applicable) |
| `dpo_escalated` | Boolean | Whether the DPO was consulted |
| `dpo_instruction` | Text | DPO's instruction or assessment (if escalated) |
| `date_completed` | Date | Date fulfilment was completed |
| `outcome` | Enum | Fulfilled / Partially fulfilled / Unable to fulfil / Rejected — with reason |
| `confirmation_sent_to_controller` | Boolean | Whether written confirmation was sent |
| `confirmation_date` | Date | Date confirmation was sent |
| `notes` | Text | Free-text field for exceptions or follow-up actions |

---

## 3. Legally Compelled Processing Record Template (A.2 Events)

This record is completed for any event where [Organisation] processes PII beyond controller instructions due to a legal requirement under CLD-POL-A.2. See also the parallel template in CLD-IMP-A.1-TG, Section 4 (which covers A.1-context legally compelled processing). Both templates should be cross-referenced when an event engages both policies.

---

**LEGALLY COMPELLED PROCESSING RECORD — A.2 EVENT**
**Record ID**: [LCP2-YYYY-NNN]
**Date Demand Received**: [Date]
**Agreement ID(s) affected**: [Reference(s) to Processor Agreement Register]

**1. Demand Details**

| Field | Detail |
|-------|--------|
| Issuing authority / legislation | [Name of authority or statute] |
| Demand type | [e.g., Law enforcement order / Court order / Regulatory requirement] |
| Jurisdiction | [Country / court / regulatory body] |
| Reference number (if available) | [Demand or order reference] |
| Date of demand | [Date] |
| PII categories demanded | [List] |
| Volume / scope of PII demanded | [e.g., All records for user ID XYZ; records from date range A–B] |

**2. Legal/Compliance Review**

| Field | Detail |
|-------|--------|
| Reviewed by (Legal/Compliance) | [Name] |
| Review date | [Date] |
| Demand assessed as legally valid | Yes / No / Challenged — [Notes] |
| Challenge outcome (if applicable) | [Outcome and date] |
| Minimum necessary PII scope confirmed | [Description of minimum scope] |

**3. Controller Notification**

| Field | Detail |
|-------|--------|
| Notification permitted before processing | Yes / No |
| If yes — controller notified on | [Date] |
| Notification method | [Secure email / Registered letter / Other] |
| Controller response (if any) | [Description] |
| If notification prohibited — legal basis | [Statute / order reference] |
| Prohibition lapse date (if known) | [Date or "Unknown"] |
| Post-lapse notification date | [Complete when notification made] |

**4. Processing Execution and Outcome**

| Field | Detail |
|-------|--------|
| Processing start date | [Date] |
| Processing end date | [Date] |
| PII actually disclosed / processed | [Describe — should match minimum necessary scope] |
| Deviation from minimum necessary scope | None / [Description and justification] |

**DPO sign-off**: _________________________ Date: _____________

---

<!-- QA_VERIFIED: [Date] -->
