<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.4.6-10-TG:privacy:TG:a.1.4.6-10 -->
**PRIV-IMP-A.1.4.6-10-TG — PII Lifecycle, Retention and Disposal — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | PII Lifecycle, Retention and Disposal — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.1.4.6-10-TG |
| **Related Policy** | PRIV-POL-A.1.4.6-10 (PII Lifecycle, Retention and Disposal) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.1.4.6-10 (PII Lifecycle, Retention and Disposal — the governing policy)
- PRIV-IMP-A.1.4.6-10-UG (PII Lifecycle, Retention and Disposal — User Guide)
- PRIV-IMP-A.1.2.6-9-TG (Privacy Governance and Records — RoPA schema with retention fields)
- PRIV-IMP-A.3.20-22-TG (Physical Media — disposal methods for physical media)

---

## Purpose of This Guide

This guide provides the **technical structures, register schemas, and templates** for PII lifecycle, retention, and disposal management. It covers:

- PII Retention Schedule schema
- Disposal Log schema
- Temporary File Register schema
- Legal Hold Register schema
- Disposal Execution Reference (disposal methods by data location and classification)
- PII Transmission Log schema

**Audience**: DPO, IT Security Team, Legal/Compliance.

---

## 1. PII Retention Schedule

The authoritative reference for retention periods across all PII processing activities. Maintained by the DPO. Part of the RoPA and referenced in privacy notices.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Schedule ID | Text | Unique reference (e.g., RET-001) |
| Processing Activity | Text | Name or RoPA reference of the processing activity |
| PII Category | Text | Category of PII subject to this retention rule |
| Retention Period | Text | Duration (e.g., "7 years", "1 year post-contract", "Duration of employment + 6 years") |
| Trigger Date | Text | When the retention period starts (e.g., "Date of contract termination", "Date of last transaction") |
| Absolute Expiry Calculation | Text | How the expiry date is calculated from the trigger (for system implementation) |
| Legal/Regulatory Basis | Text | Specific law, regulation, or contractual provision requiring this period (or "Processing purpose — no external requirement") |
| Disposal Method | Enum | Deletion / Anonymisation / Physical Destruction / Cryptographic Erasure |
| Disposal Executor | Text | Role responsible for executing disposal (e.g., "IT Security Team") |
| Systems Affected | Text | Systems holding this PII (for disposal scope) |
| Backup Retention | Text | Aligned backup retention period and approach |
| Legal Hold Status | Enum | No Hold / Active Hold / Hold Lifted (date) |
| Last Reviewed | Date | Date this entry was last confirmed as current |
| Notes | Text | Exceptions, special circumstances, linked legal holds |

### Sample Entries

| PII Category | Retention Period | Trigger | Legal Basis | Disposal Method |
|-------------|-----------------|---------|-------------|----------------|
| Customer transaction records | 7 years | Date of transaction | Tax law (specify) | Deletion |
| Customer account data (inactive) | 3 years post-inactivity | Date of last login / last transaction | Business operational need (fraud detection, re-engagement) | Deletion |
| Employee HR records — full file | 6 years | Date of employment termination | Employment law (specify) | Deletion / physical destruction |
| Employee payroll records | 7 years | End of tax year in which payment made | Tax law (specify) | Deletion / physical destruction |
| Marketing consent records | 3 years post-withdrawal | Date of consent withdrawal | GDPR accountability (Art. 5(2)) | Deletion |
| CCTV recordings | 30 days | Date of recording | Processing purpose | Automatic overwrite |
| Support ticket records | 3 years | Date of ticket closure | Business operational need | Deletion |

---

## 2. Disposal Log

Records all PII disposal actions. Maintained by the IT Security Team; copy to DPO. Classified RESTRICTED.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Disposal ID | Text | Unique reference (e.g., DISP-2026-001) |
| Trigger Type | Enum | Schedule / Erasure Request / Consent Withdrawal / Legal Hold Lifted / Purpose Cessation / Other |
| DSR Reference (if applicable) | Text | Linked Data Subject Rights Register entry (if triggered by DSR) |
| Processing Activity / RoPA Ref | Text | The processing activity whose PII is being disposed |
| PII Category | Text | Category of PII disposed |
| Systems / Storage Locations | Text | All systems and locations where disposal was executed |
| Disposal Method | Enum | SQL Deletion / File Deletion / Cryptographic Erasure / Physical Shredding / Overwrite / Anonymisation in-place |
| Records Affected (approx.) | Number | Approximate count of records or data volume disposed |
| Disposal Date | Date | Date disposal was executed |
| Executed By | Text | Role and name of person who executed disposal |
| DPO Authorisation | Text | Name of DPO confirming disposal was appropriate; date authorised |
| Backup Disposal Status | Enum | Completed / Scheduled (date) / Not Applicable |
| Backup Disposal Date | Date | Date backup disposal completed (if applicable) |
| Third Parties Notified | Boolean | Yes / No / Not Applicable |
| Verification Method | Text | How disposal was verified (e.g., DB query confirming record count = 0; file hash confirmation; witness) |
| Notes | Text | Exceptional circumstances, partial disposal with reason |

---

## 3. Temporary File Register

Documents all categories of temporary files created from PII processing, with disposal periods and mechanism. Reviewed annually by IT Security Team and DPO.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Temp File ID | Text | Unique reference (e.g., TMP-001) |
| File Type / Description | Text | What the temporary file is (e.g., "SAR export ZIP file") |
| Created By / Process | Text | System or process that creates this file type |
| Storage Location | Text | Where the file is stored |
| PII Categories Contained | Text | What PII may be in this file |
| Maximum Retention Period | Text | Documented maximum retention after creation or purpose completion |
| Disposal Mechanism | Enum | Automated TTL / Scheduled Job / Manual / Overwrite |
| Disposal Configured | Boolean | Yes / No |
| Configuration Reference | Text | System or job that implements the automated disposal |
| Last Verified | Date | Date disposal mechanism was last confirmed as operational |
| Notes | Text | Exceptions, manual oversight requirements |

### Reference Table: Standard Temporary File Disposal Periods

| File Type | Maximum Retention | Preferred Disposal Method |
|-----------|------------------|--------------------------|
| Session cache / session store | 24 hours post-session end | TTL in session store (Redis/Memcached) |
| DSR export packages | 72 hours post-transmission | Scheduled deletion job |
| Batch processing staging tables | 48 hours post-batch completion | Post-batch cleanup job |
| Error / debug logs with PII | 30 days | Log rotation with secure deletion |
| Development copies of production PII | Immediately after use | Manual deletion with DPO confirmation |
| API response cache (if PII-bearing) | Per API TTL, max 1 hour | Cache eviction policy |

---

## 4. Legal Hold Register

Tracks active legal holds preventing scheduled disposal. Maintained by the DPO in coordination with Legal/Compliance. Classified RESTRICTED.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Hold ID | Text | Unique reference (e.g., HOLD-001) |
| Hold Instructed By | Text | Role/person from Legal/Compliance instructing the hold |
| Date Hold Commenced | Date | Date disposal was suspended |
| PII Scope | Text | Categories of PII and systems affected by the hold |
| Reason | Text | Nature of the proceeding or obligation requiring the hold (without disclosing privileged content) |
| Systems Affected | Text | Systems where disposal is suspended |
| Retention Schedule Entries Affected | Text | RET-xxx references |
| Date Hold Lifted | Date | Date Legal/Compliance confirmed hold is lifted (blank if active) |
| Post-Hold Disposal Deadline | Date | Date by which disposal must be executed after hold is lifted |
| Disposal Executed | Boolean | Yes / No |
| Disposal Date | Date | Date disposal was completed after hold lifted |
| Notes | Text | Communications, extensions, partial lifts |

---

## 5. Disposal Execution Reference

### Electronic Data Disposal Methods by Classification

| Classification | System Type | Required Method | Verification |
|---------------|-------------|-----------------|-------------|
| INTERNAL | Database | SQL DELETE / table truncation | Row count = 0 query |
| INTERNAL | File system | Standard file deletion + recycle bin empty | File absent on check |
| CONFIDENTIAL | Database | SQL DELETE | Row count = 0 query + log review |
| CONFIDENTIAL | File system | Cryptographic erasure (if encrypted) or DoD 5220.22-M overwrite | Hash verification or log |
| CONFIDENTIAL | Cloud storage | Provider deletion API + deletion confirmation | Provider confirmation log |
| RESTRICTED | Database | SQL DELETE + audit log purge of sensitive fields | Row count = 0 + DBA witness |
| RESTRICTED | File system | Cryptographic erasure (encryption key destruction) or 3-pass overwrite | Certificate of destruction |
| RESTRICTED | Cloud storage | Provider deletion API + written confirmation | Signed provider confirmation |

### Physical Document Disposal

| Classification | Method | Witness Required |
|---------------|--------|-----------------|
| INTERNAL | Standard cross-cut shredding | No |
| CONFIDENTIAL | Cross-cut shredding (DIN 66399 P-4 minimum) | No |
| RESTRICTED | Cross-cut shredding (DIN 66399 P-5 minimum) OR certified third-party destruction | Yes — signed disposal certificate |

### Backup Disposal

| Scenario | Approach |
|----------|----------|
| Backup within retention window | No action — backup will be naturally overwritten per backup cycle |
| Backup past retention window | Overwrite at next full backup cycle (document expected date) |
| Backup containing DSR erasure target | Document the delayed deletion; notify data subject if they enquire; execute on next backup overwrite |
| Backup media at end-of-life | Physical destruction per classification standard above |

---

## 6. PII Transmission Log

Records PII transmissions to external parties for CONFIDENTIAL and RESTRICTED PII. Maintained by IT Security Team. Classified RESTRICTED.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Transmission ID | Text | Unique reference (e.g., TRANS-2026-001) |
| Date / Time | DateTime | Date and time of transmission |
| Sender | Text | Role / system initiating the transmission |
| Recipient | Text | Receiving party name and role |
| Recipient Type | Enum | Processor / Third Party Controller / Data Subject / Regulatory Authority / Other |
| PII Categories Transmitted | Text | Categories of PII in the transmission |
| Classification | Enum | CONFIDENTIAL / RESTRICTED |
| Transmission Method | Enum | SFTP / HTTPS API / Encrypted Email / Portal / Physical (courier) / Other |
| Encryption Confirmed | Boolean | Yes / No |
| Delivery Confirmed | Boolean | Yes / No |
| Delivery Confirmation Reference | Text | Log entry, acknowledgment email reference, or signed receipt |
| Purpose / Context | Text | Why the transmission occurred (e.g., "Processor agreement data transfer", "SAR response") |
| Linked DSR or Agreement | Text | Reference to DSR or processor agreement if applicable |
| Notes | Text | Exceptions, failed deliveries, resends |

---

<!-- QA_VERIFIED: [Date] -->
