<!-- ISMS-CORE:POLICY:CLD-POL-A.10:cloud:POL:a.10 -->
**CLD-POL-A.10 — Accountability**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Public Cloud PII Processor — Accountability |
| **Document Type** | Policy |
| **Document ID** | CLD-POL-A.10 |
| **Document Creator** | Data Protection Officer (DPO) / CISO |
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
| 1.0 | [Date to be set] | DPO / CISO | Initial policy for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant regulatory or service model change)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Data Protection Officer (DPO)
- Secondary: CISO / Cloud Security Manager
- Final Authority: Executive Management (GL)

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle — parent incident policy)
- ISMS-POL-A.5.34 (Privacy and Protection of PII)
- ISMS-POL-A.5.33 (Protection of Records)
- CLD-POL-A.1 (General)
- CLD-POL-A.6 (Use, Retention and Disclosure Limitation)
- CLD-POL-A.11 (Information Security)
- ISO/IEC 27018:2025 Annex A, Section A.10 and Controls A.10.1–A.10.3
- ISO/IEC 27701:2025 Controls A.2.3.15–A.2.3.17 (processor — accountability)
- GDPR Article 33 (notification to supervisory authority — 72 hours); Article 34 (communication to data subjects); Article 28(3)(f) (processor assists with breach notification); Article 28(3)(g) (processor provides compliance information)
- CH FADP Article 24 (data breach notification to FDPIC)

---

## Executive Summary

This policy establishes [Organisation]'s requirements as a public cloud PII processor with regard to accountability — specifically breach notification to PII controllers, retention of administrative security documentation, and procedures for the return, transfer, and disposal of PII upon contract termination — in accordance with ISO/IEC 27018:2025 Annex A, Section A.10 and Controls A.10.1, A.10.2, and A.10.3.

**Scope**: All PII processing performed by [Organisation] on behalf of PII controllers, including end-of-contract obligations.

**Combined Control Rationale**: A.10.1–A.10.3 establish the three pillars of processor accountability: (1) telling the controller promptly when things go wrong (A.10.1), (2) keeping evidence of security commitments for as long as needed (A.10.2), and (3) ensuring PII does not remain in [Organisation]'s systems after it is no longer needed (A.10.3).

---

# Scope and Applicability

## ISO/IEC 27018:2025 Control Statements

**Section A.10 — Accountability (principle)**
> *The cloud service provider shall maintain records of all PII processing activities including categories of PII, purposes, recipients, retention periods, and security measures. These records shall be made available to the PII controller and competent supervisory authorities upon request.*

**Control A.10.1 — Notification of a data breach involving PII**
> *The public cloud PII processor shall notify the PII controller of confirmed or suspected PII security incidents without undue delay, and within a timeframe enabling the controller to fulfil any regulatory breach notification obligations (e.g. 72-hour GDPR notification). Notifications shall include the nature of the breach, categories and approximate number of data subjects affected, categories of PII concerned, likely consequences, and measures taken or proposed.*

**Control A.10.2 — Retention period for administrative security policies and guidelines**
> *The public cloud PII processor shall retain administrative security policies, guidelines, and related PII processing documentation for a period sufficient to demonstrate compliance with applicable obligations. Minimum retention periods shall be defined. Version history of policies shall be maintained to support retrospective audit and incident investigation.*

**Control A.10.3 — PII return, transfer and disposal**
> *Upon termination of the service agreement, the public cloud PII processor shall return all PII to the PII controller in a documented, machine-readable format, or securely dispose of it as instructed. Where disposal is chosen, certification of secure destruction shall be provided. Copies retained in backups or replicated systems shall be disposed of within a defined timeframe. The processor shall confirm completion of return or disposal in writing.*

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 28(3)(f) (processor assists controller with breach notifications and security obligations); Article 33 (controller must notify supervisory authority within 72 hours — processor must notify controller in time for this); Article 34 (controller communicates to data subjects for high-risk breaches); Article 28(3)(g) (processor provides all information necessary to demonstrate compliance)
- **CH FADP**: Article 24 (breach notification to FDPIC — as quickly as possible); Article 9 (processor accountability obligations)
- **ISO/IEC 27018:2025**: Controls A.10.1, A.10.2, A.10.3

---

# Policy Statements: Breach Notification (A.10.1)

## Notification Obligation

[Organisation] SHALL notify the relevant PII controller of any confirmed or reasonably suspected PII security incident **without undue delay**, and in any case within **24 hours** of detection. This timeframe ensures the controller has sufficient time to fulfil its own 72-hour GDPR supervisory authority notification obligation.

## Notification Content

Breach notifications to PII controllers SHALL include the following information, to the extent available at the time of notification:

| Element | Description |
|---------|-------------|
| **Nature of the breach** | Type of incident (unauthorised access, accidental disclosure, ransomware, data loss, etc.) |
| **Categories of PII** | Types of personal data affected (identity, contact, financial, health, etc.) |
| **Approximate number of data subjects** | Estimated number of individuals whose PII may be affected |
| **Likely consequences** | Probable impact on data subjects |
| **Measures taken** | Containment and remediation steps implemented or proposed |
| **Incident reference** | [Organisation] internal incident reference number |
| **Contact point** | DPO or security contact for the controller to direct follow-up queries |

Where information is not fully available at the time of the initial notification, [Organisation] SHALL provide the information as it becomes available in phased updates, without further undue delay.

## Escalation and Coordination

[Organisation]'s breach response process for PII incidents:

1. **Detection** — Security Operations or Cloud Engineering detects potential PII incident
2. **Triage** (within 2 hours) — CISO determines whether PII is involved; activates PII breach response if confirmed or suspected
3. **Initial notification** (within 24 hours of detection) — DPO notifies affected PII controller(s) with available information
4. **Investigation** — Parallel containment and forensic investigation; phased controller updates as facts emerge
5. **Closure** — Root cause analysis and remediation confirmed; final incident report provided to controller

---

# Policy Statements: Document Retention (A.10.2)

## Retention Schedule

[Organisation] SHALL retain the following administrative documentation for the defined minimum periods:

| Document Type | Minimum Retention |
|---------------|-------------------|
| CLD-POL-A.X cloud security policies (all versions) | 5 years from version supersession |
| Sub-processor agreements and registers | Duration of engagement + 5 years |
| PII processing records (records of processing activities) | Duration of processing + 5 years |
| Breach notification records and incident reports | 5 years from incident closure |
| PII disclosure records (CLD-POL-A.6.2 register) | 5 years from disclosure |
| Data return / disposal confirmations (A.10.3) | 5 years from completion |
| Security assessment and audit reports | 5 years |
| Controller service agreements | Duration of agreement + 5 years |

## Version History

All CLD-POL-A.X policy documents SHALL maintain a version history capturing document version, date, author, and summary of changes. Previous versions SHALL be retained in accordance with the retention schedule above.

---

# Policy Statements: PII Return, Transfer and Disposal (A.10.3)

## End-of-Contract Obligation

Upon termination or expiry of a cloud service agreement under which [Organisation] processes PII, [Organisation] SHALL, as instructed by the PII controller:

**Option A — Return**: Return all PII to the PII controller in a structured, machine-readable format (JSON, CSV, or standard database export as agreed), within the timeframe specified in the service agreement or, absent such specification, within **30 calendar days** of termination.

**Option B — Disposal**: Securely destroy all PII (including primary stores, backups, replicated copies, and any sub-processor copies) using methods that prevent recovery, within **30 calendar days** of termination. [Organisation] SHALL provide the PII controller with a **written certificate of destruction** confirming completion, the disposal method used, and the scope of data destroyed.

## Backup and Replicated Copies

Where PII exists in backup or replicated copies at the time of contract termination, [Organisation] SHALL:

- Include backup copies in the return or disposal process
- Define in the service agreement the maximum timeframe for backup disposal (accounting for backup rotation cycles)
- Confirm in writing when backup disposal is complete

## Confirmation Record

[Organisation] SHALL provide the PII controller with written confirmation of completed return or disposal, including:

- Date of return delivery or disposal completion
- Scope of PII returned or disposed of (categories, approximate volume)
- Disposal method (where disposal was chosen)
- Confirmation that sub-processor PII has also been returned or disposed of

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Data Protection Officer (DPO)** | Owns breach notification process; ensures controller notifications are issued within 24 hours; manages documentation retention schedule; oversees end-of-contract PII return/disposal process |
| **CISO / Cloud Security Manager** | Leads technical breach response (containment, investigation); confirms PII scope of incidents; implements secure disposal for end-of-contract obligations |
| **Legal/Compliance Officer** | Advises on notification obligations under GDPR and FADP; reviews service agreement return/disposal clauses; maintains retention schedule compliance |
| **Cloud Engineering** | Implements secure disposal mechanisms; generates data exports for return; confirms backup purge completion |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Breach Notification Records | All notifications sent to PII controllers with timestamps and content | 5 years |
| Incident Reports | Final post-incident reports for all PII security events | 5 years |
| Document Version Archive | All previous versions of CLD-POL-A.X policies | 5 years from supersession |
| End-of-Contract Confirmations | Written confirmations of PII return or disposal per contract | 5 years |
| Certificates of Destruction | Certificates confirming secure disposal with method and scope | 5 years |
| Backup Disposal Confirmations | Written confirmation that backup copies of PII have been purged | 5 years |

---

# Audit Considerations

Auditors verifying compliance with CLD-POL-A.10 should expect to find:

- A documented breach notification procedure with 24-hour controller notification requirement
- Records of all PII security incidents including notification timelines — notifications should predate any controller's 72-hour GDPR clock expiry
- Version history for all CLD-POL-A.X policy documents with retention conforming to the schedule
- End-of-contract return or disposal confirmations and certificates of destruction for all terminated agreements in the audit period

---

<!-- QA_VERIFIED: [Date] -->
