<!-- ISMS-CORE:IMP:CLD-IMP-A.9-TG:cloud:TG:a.9 -->
**CLD-IMP-A.9-TG — Individual Participation and Access — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Individual Participation and Access — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-IMP-A.9-TG |
| **Related Policy** | CLD-POL-A.9 (Individual Participation and Access) |
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

- CLD-POL-A.9 (Individual Participation and Access — the governing policy)
- CLD-IMP-A.9-UG (Individual Participation and Access — User Guide)
- CLD-POL-A.2 (Consent and Choice — co-operation on rights at control level)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for managing data subject rights requests in [Organisation]'s role as a public cloud PII processor. It covers:

- Data Subject Rights Request Log schema
- Technical capability self-assessment checklist (per service component)
- Access response package format specification

**Audience**: CISO, DPO, Cloud Engineering, Legal/Compliance.

---

## 1. Data Subject Rights Request Log Schema

Maintain one log per contract or service deployment. Each row represents a single rights fulfilment request received from a PII controller.

| Field | Type | Description |
|-------|------|-------------|
| `request_ref` | String | [Organisation] internal reference (e.g., DSR-2026-001) |
| `controller_ref` | String | Controller's own reference number (if provided) |
| `controller_name` | String | PII controller organisation name |
| `date_received` | Date | Date request received from controller |
| `date_acknowledged` | Date | Date acknowledgement sent to controller |
| `right_type` | Enum | Access / Portability / Erasure / Restriction / Rectification / Objection |
| `data_subject_identifier` | String | Identifier provided by controller (anonymised or hashed for log storage) |
| `service_name` | String | Cloud service in scope for the request |
| `assigned_to` | String | Cloud Service Delivery contact responsible |
| `escalated_to` | String | DPO / Legal / Cloud Engineering (if escalated) |
| `escalation_reason` | String | Reason for escalation (edge case, capability gap, legal hold) |
| `date_completed` | Date | Date operation was confirmed complete |
| `backup_purge_confirmed` | Boolean | For erasure only: backup propagation confirmed |
| `backup_purge_date` | Date | For erasure only: date backup purge completed or expected |
| `outcome` | Enum | Completed / Partially Completed / Deferred / Escalated |
| `within_timeframe` | Boolean | Whether completion fell within policy timeframe |
| `confirmation_ref` | String | Reference of written completion confirmation issued to controller |
| `notes` | Text | Free text for edge cases, disputes, legal holds |

**Retention**: Duration of the relevant controller contract + 3 years.

---

## 2. Technical Capability Self-Assessment Checklist

Complete this checklist at least annually and upon any material change to service architecture. Record results in the annual capability test report. For each service component, assess whether the capability exists, is documented, and has been tested.

| Capability | Service Component | Exists | Documented | Tested | Gap Noted |
|------------|-------------------|--------|------------|--------|-----------|
| PII export (structured JSON) | Primary database | ☐ | ☐ | ☐ | |
| PII export (CSV) | Primary database | ☐ | ☐ | ☐ | |
| PII export coverage — backup stores | Backup / archive | ☐ | ☐ | ☐ | |
| PII export coverage — replicated copies | Read replicas / DR | ☐ | ☐ | ☐ | |
| PII export coverage — object storage | S3 / blob storage | ☐ | ☐ | ☐ | |
| Record-level deletion | Primary database | ☐ | ☐ | ☐ | |
| Deletion propagation to backups | Backup / archive | ☐ | ☐ | ☐ | |
| Deletion propagation to replicas | Read replicas / DR | ☐ | ☐ | ☐ | |
| Restriction flag (processing isolation) | Primary database | ☐ | ☐ | ☐ | |
| Restriction propagation to replicas | Read replicas | ☐ | ☐ | ☐ | |
| Field-level update / rectification | Primary database | ☐ | ☐ | ☐ | |
| Rectification propagation to replicas | Read replicas | ☐ | ☐ | ☐ | |
| Automated processing suspension flag | Processing pipelines | ☐ | ☐ | ☐ | |

**Assessment date**: \_\_\_\_\_\_\_\_\_\_\_\_
**Assessed by**: \_\_\_\_\_\_\_\_\_\_\_\_
**Approved by (CISO)**: \_\_\_\_\_\_\_\_\_\_\_\_

Any gap noted in column 6 SHALL be raised as a remediation item and reported to affected PII controllers if the gap reduces capability below contracted service levels.

---

## 3. Access Response Package Format Specification

When delivering a data access or portability export to a PII controller, the package SHALL conform to the following specification.

### 3.1 Delivery Method

- Delivered via the secure customer portal or encrypted file transfer (SFTP / encrypted email)
- Direct transmission to controller's designated secure endpoint (as specified in DPA)
- Not delivered by unencrypted email

### 3.2 Package Contents

| File | Format | Description |
|------|--------|-------------|
| `pii_export_[ref].json` | JSON | All PII records associated with the data subject identifier, structured by data type |
| `pii_export_[ref].csv` | CSV | Flat-file version of the same data for controller readability |
| `export_manifest_[ref].txt` | Plain text | Manifest listing all data stores searched, record counts per store, and any stores returning no data |
| `export_metadata_[ref].json` | JSON | Export metadata: request reference, data subject identifier used, export timestamp, [Organisation] service name, exporting engineer |

### 3.3 JSON Structure (pii_export)

```json
{
  "export_metadata": {
    "request_ref": "DSR-2026-001",
    "controller_ref": "CTRL-REF-XYZ",
    "export_timestamp": "2026-03-10T10:00:00Z",
    "service_name": "CloudStorageService v3",
    "data_subject_identifier_type": "account_id"
  },
  "data_stores_searched": [
    "primary_db",
    "read_replica_eu_west",
    "object_storage_bucket_pii",
    "backup_archive_20260301"
  ],
  "pii_records": {
    "identity": { ... },
    "contact": { ... },
    "activity_logs": [ ... ],
    "preferences": { ... }
  }
}
```

Field names and nesting SHALL reflect the actual data model for the service in scope. The exporting engineer SHALL validate that all PII stores are included in `data_stores_searched` before delivery.

---

## 4. Response Timeframe Reference Card

| Right Type | Policy Timeframe | Clock Start |
|------------|-----------------|-------------|
| Acknowledgement | 1 business day | Date request received |
| Access / Portability export | 5 business days | Date sufficient information received from controller |
| Rectification | 5 business days | Date sufficient information received from controller |
| Restriction (functional) | 1 business day | Date request received |
| Restriction (full propagation) | 5 business days | Date request received |
| Erasure (primary stores) | 15 business days | Date confirmed no legal hold applies |
| Erasure (backup purge confirmation) | 15 business days or per backup rotation cycle | As above |
| Automated processing suspension | 1 business day | Date request received |

Where a specific controller service agreement defines shorter timeframes, those timeframes prevail and SHALL be noted in the Data Subject Rights Request Log for that controller.

---

<!-- QA_VERIFIED: [Date] -->
