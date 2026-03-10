<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.4.6-10-UG:privacy:UG:a.1.4.6-10 -->
**PRIV-IMP-A.1.4.6-10-UG — PII Lifecycle, Retention and Disposal — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | PII Lifecycle, Retention and Disposal — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.1.4.6-10-UG |
| **Related Policy** | PRIV-POL-A.1.4.6-10 (PII Lifecycle, Retention and Disposal) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial user guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.1.4.6-10 (PII Lifecycle, Retention and Disposal — the governing policy)
- PRIV-IMP-A.1.4.6-10-TG (PII Lifecycle, Retention and Disposal — Technical Guide)
- PRIV-POL-A.1.4.2-5 (Data Minimisation — collection and processing minimisation)
- PRIV-POL-A.1.3.5-10 (Data Subject Rights — erasure requests)
- PRIV-POL-A.3.20-22 (Physical Media and Endpoint Security — physical disposal execution)

---

## Purpose of This Guide

This guide explains **how to implement** the PII lifecycle, retention, and disposal obligations of PRIV-POL-A.1.4.6-10. It covers how to build and maintain the Retention Schedule, how to operate disposal processes, how to manage temporary files, and how to ensure PII is transmitted securely.

**Who this guide is for**: DPO, Data Owners, IT Security Team, Legal/Compliance.

**Controller-only**: This guide applies only to processing activities where [Organisation] acts as PII Controller.

---

## Part 1 — Building and Maintaining the Retention Schedule (A.1.4.8)

### 1.1 What the Retention Schedule Is

The Retention Schedule is the DPO's authoritative document specifying how long each category of PII is retained, from what trigger date, and what happens at the end of the retention period. It is a regulatory compliance document — it must be accurate, current, and evidenced.

The Retention Schedule is part of the RoPA (each processing activity has a retention field) and is also maintained as a standalone reference document for operational use and audit purposes.

### 1.2 Setting Retention Periods

For each PII category or processing activity, the DPO and Data Owner establish the retention period using the following inputs:

1. **Processing purpose**: How long does the purpose require this PII? (e.g., an order requires shipping address for the duration of delivery + returns period)
2. **Contractual obligations**: Does the contract with the data subject specify a retention commitment?
3. **Legal/regulatory obligation**: Does any law require minimum or maximum retention? (e.g., tax records — 7 years; employment records — varies by jurisdiction; medical records — varies significantly)
4. **Business operational need**: Is there a documented operational need beyond the processing purpose? If so, what is the minimum period for that need?

The retention period is the **shortest** period that satisfies all applicable requirements. "We might need it" is not a valid basis for extended retention.

**Trigger date**: The retention period runs from a defined trigger, not from an arbitrary date. Common triggers:

| PII Category | Retention Trigger |
|-------------|-------------------|
| Customer account data | Date of account closure or last active transaction |
| Transaction records | Date of transaction |
| Employment records | Date of termination of employment |
| Marketing consent data | Date of consent withdrawal or last interaction |
| Support / service records | Date case is closed |
| Contract documents | Date of contract expiry or termination |

### 1.3 Annual Retention Schedule Review

The DPO reviews the Retention Schedule annually:

1. Confirm all current processing activities are reflected in the schedule
2. Check for regulatory changes affecting retention periods (consult Legal/Compliance)
3. Add entries for new processing activities commenced since last review
4. Remove or archive entries for discontinued processing activities
5. Confirm disposal processes operated as scheduled

The review is documented (date, reviewer, changes made) and retained as evidence.

---

## Part 2 — Operating PII Disposal (A.1.4.6 / A.1.4.9)

### 2.1 Routine (Schedule-Triggered) Disposal

Disposal of PII upon retention period expiry is the primary disposal mechanism. The process:

1. **Identifying expiry**: Data Owners are responsible for identifying when PII in their domain has reached its retention period. Automated expiry alerts or scheduled disposal jobs are the preferred method — manual calendar-based tracking is a fallback.
2. **Disposal authorisation**: Data Owner confirms to DPO that the retention period has been reached and no countervailing legal obligation (legal hold, active DSR, ongoing legal proceedings) prevents disposal.
3. **Execution**: IT Security Team (or Data Owner for physical records) executes the disposal using the approved method for the data classification (see PRIV-IMP-A.1.4.6-10-TG for methods).
4. **Confirmation**: IT Security Team confirms disposal completion to Data Owner and DPO. Disposal is logged in the Disposal Log (see TG).
5. **Backup alignment**: If the disposed PII is present in backups, the backup retention is aligned to the schedule — see Section 2.3.

### 2.2 Event-Triggered Disposal

Disposal may also be triggered before the scheduled retention period by:

- **Data subject erasure request**: handled per PRIV-IMP-A.1.3.5-10-UG — disposal within the one-month response window unless an exemption applies
- **Consent withdrawal**: where the only lawful basis for processing was consent and no other basis applies — processing ceases immediately, disposal follows
- **End of contract / employment**: PII no longer needed for the contractual purpose is disposed at contract end, subject to legally mandated retention of specific records
- **Purpose cessation**: where a processing activity is discontinued, all PII processed solely for that activity is disposed when the activity ends

Event-triggered disposal follows the same documentation and confirmation steps as routine disposal.

### 2.3 Backup Retention and PII Alignment

Backups are frequently overlooked in PII disposal. PII in backups is still PII and subject to the same retention obligations:

- The IT Security Team must confirm which backup sets contain PII from each processing activity
- Backup retention schedules must be aligned to PII retention periods — backups must not be retained longer than the underlying PII retention period without a documented exception
- Where immediate deletion from backups is technically impractical (e.g., incremental backup chains), the DPO documents the approach: most commonly, the backup is scheduled for deletion at the next full backup cycle, and the delayed deletion is documented in the Disposal Log
- If a data subject requests erasure and PII is in backups, the delayed backup deletion approach is documented and communicated to the data subject if they enquire

### 2.4 Disposal Conflicts and Legal Holds

Where disposal is due but a conflict arises (e.g., active legal proceedings, regulatory investigation, legal hold instruction from Legal/Compliance), disposal is suspended:

1. Legal/Compliance notifies DPO of the legal hold, identifying the PII and systems affected
2. DPO records the hold in the Retention Schedule — the record is annotated "Legal hold — disposal suspended pending Legal/Compliance clearance" with date and authority
3. Disposal recommences when Legal/Compliance confirms the hold is lifted
4. Data Owner and IT Security Team execute disposal within 30 days of hold clearance

---

## Part 3 — Temporary File Disposal (A.1.4.7)

### 3.1 What Are Temporary Files

Temporary files created as a result of PII processing include:

- Session cache files (user session data, intermediate processing results)
- Export files generated for data subject access requests or reporting
- Batch processing staging tables or files
- Debugging and error log files that captured PII
- Development or testing copies of production data

These files are not part of the primary PII record but contain PII and must be disposed of within the documented period.

### 3.2 Temporary File Disposal in Practice

**Automated disposal (preferred)**: The IT Security Team configures automated purge mechanisms for each temporary file type — session stores with TTL (time-to-live), export file deletion jobs, log rotation with secure deletion. Automated disposal is confirmed in system configuration documentation.

**Manual disposal**: Where automated disposal is not technically feasible, the Data Owner or IT Security Team schedules and documents manual deletion. Manual disposal is logged.

**Development copies**: Temporary copies of production PII in development environments are subject to immediate deletion after use — see PRIV-POL-A.3.23-31 and the test data policy. Development teams must not create production PII copies without DPO approval and must confirm deletion immediately after use.

The maximum retention periods for each temporary file type are specified in PRIV-POL-A.1.4.6-10 (Table: Temporary File Types and Disposal Periods) and detailed in PRIV-IMP-A.1.4.6-10-TG.

---

## Part 4 — PII Transmission Controls (A.1.4.10)

### 4.1 Transmission Encryption

All PII transmitted over networks must be encrypted. The IT Security Team is responsible for confirming and maintaining encryption standards:

- **Internal network transmission**: All PII transmitted between internal systems uses TLS 1.2 minimum (TLS 1.3 preferred) or equivalent application-layer encryption
- **External transmission to data subjects**: HTTPS enforced for all web-delivered content; email transmission of CONFIDENTIAL/RESTRICTED PII uses end-to-end encryption or password-protected attachments (password communicated via separate channel)
- **External transmission to processors/third parties**: Approved secure transfer methods (SFTP, HTTPS API, encrypted file transfer); unencrypted email for CONFIDENTIAL/RESTRICTED PII is prohibited
- **Cloud-to-cloud transfers**: Encryption in transit via API with TLS; confirmation of provider TLS standard in processor agreement

TLS configuration standards and cipher suite requirements are specified in PRIV-IMP-A.3.23-31-TG.

### 4.2 Delivery Confirmation for Restricted PII

For RESTRICTED PII (special category) transmitted externally, delivery confirmation is required:

1. SFTP or secure portal transmission: server logs confirm receipt by authorised recipient
2. Email with encrypted attachment: request read receipt or explicit acknowledgment reply from recipient
3. API transfer: HTTP 200/201 response logged as delivery confirmation
4. Physical courier for paper RESTRICTED documents: signed delivery receipt

Delivery confirmations for RESTRICTED PII are retained in the transmission log (see TG).

### 4.3 Identifying Prohibited Transmissions

The following transmission methods are prohibited for CONFIDENTIAL or RESTRICTED PII:

- Unencrypted email (plain text) to external recipients
- Unencrypted FTP
- Consumer file-sharing services not approved by IT Security (e.g., personal Dropbox, WeTransfer)
- Sending PII via instant messaging platforms not approved as secure by IT Security
- Verbal disclosure of RESTRICTED PII over a recorded or monitored channel where confidentiality cannot be assured

Personnel who are unsure whether a proposed transmission method is approved must check with IT Security or the DPO before sending.

---

## Evidence Checklist

- [ ] PII Retention Schedule — all processing activities covered; trigger dates defined; legal basis for each period documented
- [ ] Disposal Logs — dated, method-confirmed records for all disposal actions
- [ ] Annual Retention Schedule Review — documented review with changes noted
- [ ] Temporary file disposal confirmation — automated purge configuration or manual deletion logs
- [ ] Legal hold register — active holds documented with authority and date
- [ ] Backup retention alignment — backup schedules align to PII retention periods
- [ ] TLS configuration evidence — encryption in transit confirmed for PII-carrying systems
- [ ] Delivery confirmation records — for RESTRICTED PII transfers

---

<!-- QA_VERIFIED: [Date] -->
