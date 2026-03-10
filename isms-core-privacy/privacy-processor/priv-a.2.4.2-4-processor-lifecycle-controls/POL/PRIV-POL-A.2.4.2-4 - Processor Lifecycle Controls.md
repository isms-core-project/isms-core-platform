<!-- ISMS-CORE:POLICY:PRIV-POL-A.2.4.2-4:privacy:POL:a.2.4.2-4 -->
**PRIV-POL-A.2.4.2-4 — Processor Lifecycle Controls**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Processor Lifecycle Controls |
| **Document Type** | Policy |
| **Document ID** | PRIV-POL-A.2.4.2-4 |
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
- Secondary: Chief Information Security Officer (CISO)
- Final Authority: Executive Management (GL)

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- PRIV-POL-01 (Privacy Governance and Decision-Making Framework)
- PRIV-IMP-A.2.4.2-4-UG (Processor Lifecycle Controls — User Guide)
- PRIV-IMP-A.2.4.2-4-TG (Processor Lifecycle Controls — Technical Guide)
- PRIV-POL-A.2.2.2-7 (Processor Agreements — foundational processor policy)
- PRIV-POL-A.1.4.6-10 (Controller PII Lifecycle — the controller-side counterpart for temporary files and retention)
- PRIV-POL-A.3.5-7 (Information Classification and Transfer — transmission rules)
- ISO/IEC 27701:2025 Controls A.2.4.2, A.2.4.3, A.2.4.4
- ISO/IEC 27701:2025 Annex B (Implementation guidance B.2.4.2 through B.2.4.4)
- GDPR Article 28(3)(g) (return or deletion at service end); Article 32(1)(a) (encryption and transmission security)
- CH FADP Article 9 (processor must take equivalent security measures)

---

## Executive Summary

This policy establishes [Organisation]'s requirements when acting as PII Processor for the disposal of temporary files, the secure return/transfer/disposal of customer PII at end of service, and transmission controls for PII — in accordance with ISO/IEC 27701:2025 Controls A.2.4.2, A.2.4.3, and A.2.4.4.

**Scope**: All temporary files created during processing of customer PII; all end-of-service handling of customer PII; all transmission of PII over data networks on behalf of customers.

**Role Applicability**: This policy applies to [Organisation] acting as **PII Processor only**. Controls A.2.4.2–A.2.4.4 are processor-specific (Table A.2).

---

# Scope and Applicability

## ISO/IEC 27701:2025 Control Statements

**Control A.2.4.2 — Temporary files**
> *The organization shall ensure that temporary files created as a result of the processing of PII are disposed of (e.g. erased or destroyed) following documented procedures within a specified, documented period.*

**Control A.2.4.3 — Return, transfer or disposal of PII**
> *The organization shall be able to return, transfer or dispose of PII in a secure manner. It shall also make its policy available to the customer.*

**Control A.2.4.4 — PII transmission controls**
> *The organization shall subject PII transmitted over a data-transmission network to appropriate controls, which are designed to ensure that the data reaches its intended destination.*

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 28(3)(g) (processor shall, at the controller's choice, delete or return PII at service end and delete copies unless required by law); Article 32(1)(a) (pseudonymisation, encryption, and transmission security)
- **CH FADP**: Article 9 (security measures equivalent to controller requirements)
- **ISO/IEC 27701:2025**: Controls A.2.4.2–A.2.4.4 (normative)

---

# Policy Statements

## A.2.4.2 — Temporary Files (Processor)

[Organisation] SHALL ensure that temporary files created as a result of PII processing on behalf of customers are disposed of within documented, specified periods.

Temporary file disposal requirements for processor activities are consistent with the general temporary file policy in PRIV-POL-A.1.4.6-10 (A.1.4.7), applied to customer PII contexts:

- Processing cache and staging files: disposed within 48 hours of processing completion
- Error/exception logs containing customer PII: disposed within 30 days (automated rotation)
- Export files generated for customer delivery: disposed within 72 hours after confirmed delivery to customer

Specific periods are documented in PRIV-IMP-A.2.4.2-4-TG. Automated purge mechanisms are preferred.

---

## A.2.4.3 — Return, Transfer or Disposal of Customer PII

When a customer contract ends or a customer requests return or deletion of their PII, [Organisation] SHALL be able to:

- **Return** the PII to the customer in a structured, agreed format
- **Transfer** the PII to another processor designated by the customer
- **Dispose** of the PII securely using approved erasure methods

[Organisation] SHALL choose between these options according to the customer's documented instruction. In the absence of a specific customer instruction at contract end, [Organisation] SHALL request instructions and follow the default specified in the processor agreement.

### Disposal Standards

PII disposal at contract end follows the methods defined in PRIV-POL-A.1.4.6-10 (A.1.4.9):

- Database records: SQL DELETE or equivalent; or cryptographic erasure for encrypted stores
- File system: cryptographic erasure or approved overwrite
- Backup media: aligned to backup retention schedule; expired backups purged per schedule; or out-of-cycle deletion upon customer instruction with confirmation

Disposal SHALL be confirmed in writing to the customer within the timeframe specified in the processor agreement (typically within 30 days of service end).

### Policy Availability

[Organisation] SHALL make its return, transfer, and disposal policy available to customers on request and, where contractually required, as part of the processor agreement documentation.

---

## A.2.4.4 — PII Transmission Controls (Processor)

[Organisation] SHALL subject PII transmitted on behalf of customers over data-transmission networks to appropriate controls to ensure it reaches its intended destination.

Transmission controls are consistent with PRIV-POL-A.3.5-7 (transfer rules) and PRIV-POL-A.3.23-31 (cryptographic controls):

- All PII transmitted over networks SHALL be encrypted in transit (minimum TLS 1.2; TLS 1.3 preferred)
- CONFIDENTIAL and RESTRICTED PII transmissions SHALL use approved secure transfer methods
- Delivery confirmation or receipt acknowledgment SHALL be obtained for RESTRICTED PII transmissions to third parties
- Transmission logs for PII carried over networks are maintained per PRIV-POL-A.3.25 (logging)

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Data Protection Officer (DPO)** | Manages end-of-service PII return/disposal process; confirms completion to customers; maintains disposal records |
| **CISO / IT Security Team** | Implements temporary file purge mechanisms; executes disposal; configures TLS enforcement; provides disposal confirmation |
| **Customer Success** | Coordinates with customers on preferred return/disposal option at contract end; tracks disposal completion |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Temporary File Purge Records | Automated/manual purge confirmation for customer PII temp files | 3 years |
| End-of-Service Disposal Records | Written confirmation of PII return/transfer/disposal per customer | 5 years |
| Customer PII Disposal Confirmation | Written confirmation sent to customers at contract end | 5 years |
| Transmission Encryption Configuration | TLS configuration records for customer PII transmission | Current + 3 years |

---

# Audit Considerations

- Temporary file disposal periods documented and automated mechanisms in place
- End-of-service PII handling: evidence of return, transfer, or disposal per customer instruction
- Written disposal confirmation provided to customers within contracted timeframe
- TLS enforcement for PII transmission (configuration evidence)
- Return/disposal policy available to customers

---

<!-- QA_VERIFIED: [Date] -->
