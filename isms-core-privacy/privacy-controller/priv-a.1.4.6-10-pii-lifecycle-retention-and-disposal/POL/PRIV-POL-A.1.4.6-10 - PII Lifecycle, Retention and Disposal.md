<!-- ISMS-CORE:POLICY:PRIV-POL-A.1.4.6-10:privacy:POL:a.1.4.6-10 -->
**PRIV-POL-A.1.4.6-10 — PII Lifecycle, Retention and Disposal**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | PII Lifecycle, Retention and Disposal |
| **Document Type** | Policy |
| **Document ID** | PRIV-POL-A.1.4.6-10 |
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
- PRIV-IMP-A.1.4.6-10-UG (PII Lifecycle, Retention and Disposal — User Guide)
- PRIV-IMP-A.1.4.6-10-TG (PII Lifecycle, Retention and Disposal — Technical Guide)
- PRIV-POL-A.1.4.2-5 (Data Minimisation — sibling policy)
- PRIV-POL-A.3.20-22 (Physical Media and Endpoint Security — disposal execution)
- ISO/IEC 27701:2025 Controls A.1.4.6, A.1.4.7, A.1.4.8, A.1.4.9, A.1.4.10
- ISO/IEC 27701:2025 Annex B (Implementation guidance B.1.4.6 through B.1.4.10)
- GDPR Article 5(1)(e) (storage limitation principle); Article 17 (erasure); Article 32 (security of transmission)
- CH FADP Article 6(4) (storage limitation); Article 7 (technical security measures)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for PII de-identification and deletion at end of processing, management of temporary files, PII retention limits, disposal procedures, and transmission controls — in accordance with ISO/IEC 27701:2025 Controls A.1.4.6 through A.1.4.10.

**Scope**: All PII held by [Organisation] as PII Controller from the point where the processing purpose is fulfilled through to confirmed disposal; all temporary files generated during PII processing; all transmission of PII over data networks.

**Role Applicability**: This policy applies to [Organisation] acting as **PII Controller only**. Controls A.1.4.6–A.1.4.10 are controller-specific (Table A.1) within the Privacy by Design and Privacy by Default objective group.

---

# Scope and Applicability

## ISO/IEC 27701:2025 Control Statements

**Control A.1.4.6 — PII de-identification and deletion at the end of processing**
Control A.1.4.6 requires [Organisation] to delete PII or render it non-identifiable as soon as it is no longer needed for the purpose for which it was processed.

**Control A.1.4.7 — Temporary files**
Control A.1.4.7 requires [Organisation] to dispose of temporary files created during PII processing within a defined, documented period, using documented procedures.

**Control A.1.4.8 — Retention**
Control A.1.4.8 requires [Organisation] not to retain PII for longer than is necessary for the purposes for which it is processed.

**Control A.1.4.9 — Disposal**
Control A.1.4.9 requires [Organisation] to have documented policies, procedures, and mechanisms for the disposal of PII.

**Control A.1.4.10 — PII transmission controls**
Control A.1.4.10 requires [Organisation] to apply appropriate controls to PII transmitted over data networks, designed to ensure that data reaches its intended destination.

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 5(1)(e) (storage limitation — not retained longer than necessary; longer retention for archiving/research with appropriate safeguards); Article 17 (erasure — upon purpose end, consent withdrawal, or successful erasure request); Article 32(1)(a) (pseudonymisation and encryption as security measures, including in transit)
- **CH FADP**: Article 6(4) (retention — only as long as necessary); Article 7 (transmission security)
- **ISO/IEC 27701:2025**: Controls A.1.4.6–A.1.4.10 (normative)

---

# Policy Statements

## A.1.4.6 — De-identification and Deletion at End of Processing

When PII is no longer necessary for the identified processing purpose(s), [Organisation] SHALL either:

- **Delete** the PII (irreversible destruction), OR
- **De-identify** the PII to a form that does not permit identification or re-identification of PII principals (anonymisation — confirmed by DPO per PRIV-POL-A.1.4.2-5)

This obligation applies **as soon as** the purpose is no longer served. It applies to all copies of PII: primary databases, backups, archives, processing logs, and temporary copies.

### Retention for Countervailing Legal Obligation

Where a legal obligation requires retention beyond the processing purpose (e.g., tax records, employment records, legal hold), retention SHALL be:

- Limited to the legally required period
- Restricted to the minimum scope necessary (where possible, other fields not required by the legal obligation shall be deleted)
- Clearly recorded in the Retention Schedule with the legal provision reference

---

## A.1.4.7 — Temporary Files

[Organisation] SHALL ensure that temporary files created as a result of PII processing are disposed of within a documented, specified period.

### Temporary File Types and Disposal Periods

| Temporary File Type | Maximum Retention | Disposal Method |
|--------------------|------------------|-----------------|
| Processing cache files (session data, intermediate results) | 24 hours after session end or processing completion | Automatic purge |
| Export files generated for data subject access requests | 72 hours after transmission to data subject | Secure deletion |
| Batch processing staging files | 48 hours after batch completion | Secure deletion |
| Debugging / error log files containing PII | 30 days | Automated rotation with secure deletion |
| Temporary development copies with real PII | Immediately after use (per PRIV-POL-A.3.23-31 test data requirements) | DPO-approved secure deletion with confirmation |

Specific disposal periods for additional temporary file types are documented in PRIV-IMP-A.1.4.6-10-TG. Automated purge mechanisms are preferred over manual deletion.

---

## A.1.4.8 — Retention

[Organisation] SHALL NOT retain PII for longer than is necessary for the purposes for which it is processed.

### Retention Schedule

The DPO maintains a **PII Retention Schedule** that specifies:

- PII category or processing activity
- Retention period (from defined trigger date: e.g., end of contract, last active use, date of collection)
- Legal or regulatory basis for the retention period (where applicable)
- Disposal method upon expiry

The Retention Schedule is published internally and forms part of the RoPA. It is reviewed at minimum annually and upon changes to regulatory requirements or processing activities.

### Legal Holds

Where Legal/Compliance identifies a legal hold requirement, PII subject to the hold SHALL be retained regardless of its scheduled disposal date. Legal holds SHALL be:

- Authorised in writing by Legal/Compliance or Executive Management
- Documented in the Retention Schedule with the hold basis and expected end date
- Reviewed at minimum quarterly; lifted promptly once the hold basis no longer applies
- Applied narrowly to the minimum scope of PII necessary

Legal holds that are not formally reviewed and lifted become a source of unlawful retention. The DPO monitors all active legal holds.

### Retention Principles

- Retention periods SHALL be based on documented need (legal, contractual, or operational) — not on the principle of "keeping just in case"
- Where multiple regulatory obligations create different retention requirements for the same data, the longest mandatory period applies for the legally required scope; excess data shall be deleted at the earliest applicable period
- Backups containing PII SHALL be subject to the same retention limits as primary data — backup retention schedules SHALL align with PII retention periods or have a documented exception with compensating controls

---

## A.1.4.9 — Disposal

[Organisation] SHALL have documented policies, procedures, and mechanisms for the disposal of PII.

### Disposal Requirements

PII disposal SHALL be:

- **Irreversible**: Disposed PII cannot be recovered by routine technical means
- **Documented**: Each disposal action is logged (what was disposed, when, by whom, method)
- **Verified**: Where technically feasible, disposal is confirmed by automated or manual verification
- **Compliant with classification handling**: RESTRICTED PII disposal uses the most stringent method per PRIV-POL-A.3.20-22

### Disposal Methods

| Data Location | Disposal Method |
|--------------|----------------|
| Database records | SQL DELETE or equivalent; or anonymisation in-place where deletion creates data integrity issues (with DPO approval) |
| File system (electronic) | Cryptographic erasure (if encrypted) or approved overwrite standard |
| Backup media | Overwrite per backup cycle aligned to retention schedule; or physical destruction for expired backup media |
| Physical documents | Cross-cut shredding (CONFIDENTIAL), cross-cut + witness (RESTRICTED) |
| Cloud storage | Deletion via approved API/console; confirmation of deletion from provider where available |

Disposal procedures are detailed in PRIV-IMP-A.1.4.6-10-TG.

### Disposal Triggers

PII disposal SHALL be triggered by:

- Expiry of the retention period per the Retention Schedule
- Cessation of the processing purpose (when no countervailing legal obligation applies)
- Data subject erasure request (per PRIV-POL-A.1.3.5-10) — within the required response timeframe
- Consent withdrawal (for consent-based processing where no other basis applies)
- End of contract or employment (for applicable PII categories)

---

## A.1.4.10 — PII Transmission Controls

[Organisation] SHALL subject PII transmitted over data-transmission networks to appropriate controls to ensure that data reaches its intended destination.

### Transmission Control Requirements

- All PII transmitted over networks SHALL be encrypted in transit using current TLS standards (minimum TLS 1.2; TLS 1.3 preferred)
- PII transmitted to external parties SHALL use approved secure transfer methods per PRIV-POL-A.3.5-7 (transfer rules)
- Unencrypted transmission of CONFIDENTIAL or RESTRICTED PII over public networks is prohibited
- Delivery confirmation or receipt acknowledgment SHALL be obtained for transfers of RESTRICTED PII (special category)
- Transmission logs SHALL be maintained for CONFIDENTIAL and RESTRICTED PII transfers per PRIV-POL-A.3.25 (logging)

Technical transmission standards are specified in PRIV-IMP-A.1.4.6-10-TG, consistent with PRIV-POL-A.3.23-31.

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Data Protection Officer (DPO)** | Owns Retention Schedule; approves disposal exceptions; confirms anonymisation; monitors disposal compliance; responds to erasure requests involving retention conflicts |
| **Data Owner** | Initiates disposal upon retention period expiry in their domain; escalates disposal conflicts to DPO |
| **IT Security Team** | Implements automated disposal mechanisms; executes backup retention alignment; maintains disposal logs; configures transmission encryption |
| **Legal/Compliance** | Advises on legal hold requirements; identifies legally mandated retention periods |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| PII Retention Schedule | Documented retention periods per PII category, with legal basis | Current + 3 years |
| Disposal Logs | Records of PII disposal actions with date, method, and scope | 5 years |
| Temporary File Purge Confirmation | Automated or manual confirmation of temporary file disposal | 3 years from the date of purge |
| Transmission Encryption Configuration | TLS configuration records for PII-carrying systems | Current + 3 years |
| Retention Schedule Review Records | Annual review evidence | 3 years from the date of the review |

---

# Audit Considerations

- Retention Schedule with documented periods and legal basis for all PII categories
- Evidence of disposal actions within scheduled periods
- No PII retained beyond the documented retention period without a documented legal basis
- Temporary file purge mechanisms configured and verified
- TLS enforcement for PII in transit (configuration evidence)
- Disposal logs showing method and timing

---

<!-- QA_VERIFIED: [Date] -->
