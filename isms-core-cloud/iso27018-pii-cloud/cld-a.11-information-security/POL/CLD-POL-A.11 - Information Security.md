<!-- ISMS-CORE:POLICY:CLD-POL-A.11:cloud:POL:a.11 -->
**CLD-POL-A.11 — Information Security**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Public Cloud PII Processor — Information Security |
| **Document Type** | Policy |
| **Document ID** | CLD-POL-A.11 |
| **Document Creator** | CISO / Cloud Security Manager |
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
| 1.0 | [Date to be set] | CISO / Cloud Security Manager | Initial policy for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant infrastructure, technology, or regulatory change)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: CISO / Cloud Security Manager
- Secondary: Data Protection Officer (DPO)
- Final Authority: Executive Management

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- ISMS-POL-A.5.34 (Privacy and Protection of PII)
- ISMS-POL-A.5.15-16-18 (Identity and Access Management)
- ISMS-POL-A.5.19-23 (Supplier and Third-Party Relationships)
- ISMS-POL-A.8.10 (Information Deletion)
- ISMS-POL-A.8.24 (Use of Cryptography)
- CLD-POL-A.1 (General)
- CLD-POL-A.5 (Data Minimisation — temporary file erasure)
- CLD-POL-A.8 (Openness, Transparency — sub-processor disclosure)
- CLD-POL-A.10 (Accountability — breach notification)
- ISO/IEC 27018:2025 Annex A, Section A.11 and Controls A.11.1–A.11.13
- ISO/IEC 27701:2025 Annex A.3 (Information security controls — A.3.3 through A.3.31, applicable to both controllers and processors and implemented through this policy)
- ISO/IEC 27002:2022 Controls 6.2 (terms and conditions), 8.11 (data masking), 8.12 (data leakage), 8.24 (cryptography)
- GDPR Article 28(3)(c) (processor implements appropriate technical and organisational measures per Article 32); Article 32 (security of processing)
- CH FADP Article 9 (processor engagement and associated data security obligations)

---

## Executive Summary

This policy establishes [Organisation]'s information security requirements for the protection of PII in public cloud environments — the most comprehensive section of the ISO/IEC 27018:2025 Annex A control set, covering 13 controls across confidentiality, physical media security, access management, encryption, audit logging, sub-processor management, and storage remanence.

**Scope**: All systems, personnel, processes, and sub-processors involved in processing PII on behalf of PII controllers within [Organisation]'s public cloud services.

**Control Coverage**: This policy addresses ISO/IEC 27018:2025 Controls A.11.1 through A.11.13.

---

# Scope and Applicability

## ISO/IEC 27018:2025 Control Statements

**A.11.1 — Confidentiality or non-disclosure agreements**: Personnel with PII access bound by documented NDA obligations surviving termination.

**A.11.2 — Restriction of the creation of hardcopy material**: Printing of PII restricted to documented legitimate purposes; printed PII handled securely.

**A.11.3 — Control and logging of data restoration**: Backup restoration of PII is a controlled, logged operation; logs protected and reviewed.

**A.11.4 — Protecting data on storage media leaving the premises**: Physical media containing PII encrypted or destroyed before leaving controlled environment.

**A.11.5 — Use of unencrypted portable storage media and devices**: Unencrypted portable devices prohibited for PII; loss/theft treated as PII incident.

**A.11.6 — Encryption of PII transmitted over public data-transmission networks**: PII in transit encrypted with TLS 1.2 minimum, 1.3 preferred; HTTPS enforced.

**A.11.7 — Secure disposal of hardcopy materials**: Hardcopy PII disposed of by cross-cut shredding or equivalent; disposal documented.

**A.11.8 — Unique use of user IDs**: Each individual with PII access assigned a unique identifier; no shared accounts.

**A.11.9 — User ID management**: User ID lifecycle managed; deactivated promptly on termination or role change; dormant accounts reviewed.

**A.11.10 — Records of authorized users**: Up-to-date records of all authorised PII system users; reviewed at least quarterly; available to controller.

**A.11.11 — Contract measures**: Processor–controller agreements include scope, security, breach notification, rights assistance, audit, sub-processor approval, return/deletion, jurisdiction.

**A.11.12 — Sub-contracted PII processing**: Sub-processors bound by equivalent obligations via binding contracts; audited periodically; processor remains accountable.

**A.11.13 — Access to data on pre-used data storage space**: Storage reallocated to new customer cryptographically erased; decommissioning procedures documented and tested.

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 28(3)(c) (processor implements appropriate technical and organisational measures per Article 32); Article 32 (security of processing — pseudonymisation, encryption, resilience, restoration, testing)
- **CH FADP**: Article 9 (processor engagement conditions and associated data security obligations)
- **ISO/IEC 27018:2025**: Controls A.11.1–A.11.13

---

# Policy Statements: Confidentiality Obligations (A.11.1)

All [Organisation] personnel and contractors with access to systems containing PII SHALL be bound by written confidentiality and non-disclosure obligations. NDAs SHALL explicitly:

- Prohibit secondary use, personal retention, or unauthorised disclosure of PII
- Survive termination of employment or engagement
- Be signed before access to any PII system is granted

NDAs are managed per ISMS-POL-A.6.3 (Confidentiality agreements). NDA coverage SHALL be verified during onboarding and departure processes.

---

# Policy Statements: Restriction of Hardcopy Material (A.11.2)

Creation of hardcopy (printed) material containing PII is **restricted**. Printing of PII requires:

- Documented business justification (e.g., regulatory requirement, audit paper trail)
- Authorisation from the relevant team lead and DPO notation for large-volume prints
- Immediate collection from printer; PII material not left unattended in shared areas

Printed PII SHALL be handled under secure-desk procedures and disposed of per §11.7 (secure hardcopy disposal). Where technically feasible, print management software or DLP controls SHALL be configured to flag or restrict print jobs containing PII; where technical enforcement is not implemented, the reliance on procedural controls SHALL be documented by the CISO with compensating monitoring identified.

---

# Policy Statements: Control and Logging of Data Restoration (A.11.3)

Restoration of PII from backup or archive is a **controlled operation** requiring:

- Documented restoration authorisation from the team lead or incident commander
- Logging of: operator identity, timestamp, backup source, scope of data restored, and authorisation reference
- Restoration logs protected against tampering (write-once or cryptographically signed)
- Quarterly review of restoration logs by CISO

Automated alerting SHALL be configured to notify the CISO of restoration events in real time, enabling detection of out-of-pattern restorations without waiting for the quarterly log review. Unplanned or unauthorised restoration attempts SHALL be treated as security events and investigated under ISMS-POL-A.5.24-28.

---

# Policy Statements: Storage Media Leaving Premises (A.11.4)

Physical storage media (drives, tapes, removable media) containing PII that leaves [Organisation]'s cloud facilities SHALL be:

- **Encrypted** using approved full-disk or volume encryption with key management per ISMS-POL-A.8.24, or
- **Physically destroyed** to a standard preventing data recovery (e.g., NIST SP 800-88 compliant destruction) before departure

Media movement SHALL be:
- Authorised by the CISO or Cloud Security Manager
- Logged in a media movement register with chain of custody documentation
- Tracked to final destination (return or destruction facility)

---

# Policy Statements: Unencrypted Portable Storage Devices (A.11.5)

The use of unencrypted portable storage media and devices for storage or transfer of PII is **prohibited**. This prohibition covers USB drives, external hard drives, laptops, tablets, and mobile phones.

Where portable devices are authorised for PII:
- Full-disk encryption meeting approved standards (AES-256 minimum) is **mandatory**
- Device encryption status SHALL be verified by IT before PII access is permitted
- Remote wipe capability SHALL be enabled for mobile devices

**Loss or theft** of any portable device potentially containing PII SHALL be reported to the CISO and DPO immediately and treated as a PII security incident under CLD-POL-A.10.1 and ISMS-POL-A.5.24-28.

---

# Policy Statements: Encryption of PII in Transit (A.11.6)

PII transmitted over public networks SHALL be encrypted. Requirements:

- **TLS 1.3 required** for all new implementations; **TLS 1.2 permitted only for existing integrations** where TLS 1.3 is not yet technically feasible, subject to a documented remediation plan and CISO approval
- **HTTPS enforced** on all web interfaces and API endpoints handling PII; HTTP redirect to HTTPS mandatory
- TLS certificates SHALL be issued by trusted certificate authorities and renewed before expiry (automated renewal preferred)
- **Unencrypted transmission** (plain HTTP, FTP, SMTP without STARTTLS) of PII is prohibited

Cipher suite configurations SHALL be reviewed annually against current best practice (e.g., BSI TR-02102, NIST SP 800-52). Weak ciphers (RC4, DES, 3DES, SSL 3.0, TLS 1.0, TLS 1.1) SHALL be disabled.

---

# Policy Statements: Secure Disposal of Hardcopy Materials (A.11.7)

Hardcopy materials containing PII SHALL be disposed of securely:

- **Individual disposal**: Cross-cut shredding to DIN 66399 Level P-5 (max 30mm² particle size) for documents containing PII or sensitive categories; P-4 is acceptable for general internal documents not containing PII
- **Bulk disposal**: Certified destruction services with certificate of destruction provided to requester
- **Disposal bins**: Locked, access-controlled bins for PII material in all work areas containing PII

Disposal SHALL be documented. Certificates of destruction SHALL be retained for 3 years.

---

# Policy Statements: Unique User IDs (A.11.8)

Each individual with access to PII systems SHALL be assigned a **unique user identifier**. Shared, generic, or role-based accounts SHALL NOT be used to access systems where PII is processed or stored.

Unique IDs ensure that all actions on PII can be attributed to a specific individual for audit and accountability purposes. Exceptions (e.g., service accounts) require CISO approval and enhanced compensating controls (privileged access management, session recording).

---

# Policy Statements: User ID Management (A.11.9)

User identifiers for PII systems SHALL be managed through a documented lifecycle:

| Lifecycle Stage | Requirement |
|-----------------|-------------|
| **Provisioning** | Requires documented authorisation from user's manager and system owner |
| **Access review** | All PII system accounts reviewed at least quarterly |
| **Role change** | Access updated within 1 business day of confirmed role change |
| **Termination** | Account deactivated within 4 hours of HR-confirmed departure |
| **Dormant accounts** | Accounts inactive for 30 days on PII-critical systems (45 days on lower-sensitivity PII systems) reviewed; suspended pending review; deleted if no business justification |

User ID lifecycle management integrates with ISMS-POL-A.5.15-16-18 (IAM).

---

# Policy Statements: Records of Authorised Users (A.11.10)

[Organisation] SHALL maintain an **Authorised User Register** for each PII system, recording:

- Individual identity and role
- Scope of access granted (read, write, admin)
- Authorisation date and authorising manager
- Last review date

The Authorised User Register SHALL be:
- Reviewed and attested by system owners at least **quarterly**
- Made available to any PII controller upon request — [Organisation] SHALL provide each controller with a **scoped extract** showing only personnel with access to that controller's PII data, not the full register across all customers
- Updated within 1 business day of any access change

---

# Policy Statements: Contract Measures (A.11.11)

Service agreements between [Organisation] and PII controllers SHALL include provisions addressing:

- Scope and documented purpose of PII processing
- Security obligations aligned with GDPR Article 32 and this policy
- Breach notification requirements (controller notification within 24 hours per CLD-POL-A.10.1)
- Data subject rights assistance obligations (per CLD-POL-A.2.1 and CLD-POL-A.9)
- Audit rights: controller (or appointed auditor) may audit [Organisation]'s compliance, exercisable with not less than 30 days' advance notice, no more than once per calendar year unless a confirmed security incident justifies additional audit, and at the controller's cost unless non-compliance is demonstrated
- Sub-processor approval requirements (per CLD-POL-A.8.1)
- PII return or deletion upon termination (per CLD-POL-A.10.3)
- Applicable law and jurisdiction

Contract terms SHALL be reviewed when regulatory requirements change materially. Legal/Compliance maintains the standard processor agreement template.

---

# Policy Statements: Sub-contracted PII Processing (A.11.12)

[Organisation] SHALL impose on all sub-processors, via binding contract, **obligations equivalent** to those in this policy and the full CLD-POL-A.X suite. Sub-processor contracts SHALL:

- Mirror the data protection obligations from the controller–processor agreement
- Require prior written consent from [Organisation] (and by extension, from the PII controller) before any further sub-processing
- Include audit rights for [Organisation] over sub-processor compliance
- Require breach notification to [Organisation] within 12 hours of detection (enabling [Organisation]'s 24-hour controller notification obligation under CLD-POL-A.10.1) — this 12-hour requirement is a **mandatory clause** in all sub-processor agreements; Legal/Compliance maintains the standard sub-processor agreement template
- Require PII return or disposal upon sub-processor engagement termination

[Organisation] SHALL audit sub-processors at least annually (via questionnaire, document review, or on-site audit) and remains **fully accountable** to PII controllers for sub-processor compliance failures. Sub-processor audit results SHALL be documented and available to controllers upon request.

---

# Policy Statements: Pre-used Data Storage Space (A.11.13)

[Organisation] SHALL ensure that PII cannot be accessed from storage previously allocated to another customer (**data remanence prevention**).

Before any storage is reallocated to a new customer workload:
- All prior data SHALL be **cryptographically erased** (encryption key deletion for encrypted volumes — the primary method for cloud storage) or overwritten to a standard preventing recovery
- Erasure SHALL be documented and the decommissioning record retained

Decommissioning procedures SHALL:
- Cover all storage types: block storage (EBS, volumes), object storage (bucket contents), ephemeral instance storage, and database storage
- Be tested at least **annually** by randomly sampling reallocated storage and confirming no residual data
- Apply equally to physical decommissioning of storage media (see A.11.4)

This control is the foundation of multi-tenant PII isolation. Any failure SHALL be treated as a potential PII security incident.

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO / Cloud Security Manager** | Owns this policy; ensures all 13 controls are implemented and maintained; conducts annual security review; manages media movement and sub-processor audit programme |
| **Data Protection Officer (DPO)** | Reviews policy annually for regulatory alignment; advises on contract terms (A.11.11); oversees sub-processor adequacy assessments |
| **Cloud Engineering** | Implements technical controls (encryption, TLS configuration, erasure, logging); tests decommissioning procedures |
| **IT / Identity Management** | Manages user ID lifecycle per A.11.8–A.11.10; maintains Authorised User Register; enforces access policies |
| **Legal/Compliance Officer** | Maintains standard processor agreement template; reviews sub-processor agreements; advises on jurisdiction and audit rights clauses |
| **HR** | Triggers user account deactivation on departure; manages NDA signing process on onboarding |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| NDA Records | Signed NDAs for all personnel with PII access | Duration of engagement + 5 years |
| Print Authorisation Logs | Records of authorised PII print operations | 3 years |
| Backup Restoration Logs | Logged restoration events with authorisation records | 3 years |
| Media Movement Register | Physical media movement log with chain of custody | 3 years |
| TLS / Encryption Configuration Records | Current cipher suite and TLS configuration documentation | Current + previous versions 5 years |
| Destruction Certificates | Hardcopy and media disposal certificates | 3 years |
| Authorised User Register | Quarterly-attested access records per PII system | 5 years |
| Sub-Processor Audit Records | Annual audit results for each sub-processor | 5 years |
| Storage Decommissioning Records | Records of cryptographic erasure per storage decommission event | 3 years |
| Decommissioning Test Results | Annual test results confirming no residual data in reallocated storage | 3 years |

---

# Audit Considerations

Auditors verifying compliance with CLD-POL-A.11 should expect to find:

- NDA coverage for all personnel with PII access — no exceptions
- TLS 1.2+ enforced on all PII-handling network interfaces; TLS 1.0/1.1 disabled
- Quarterly Authorised User Register attestations with prompt removal of leavers and role-changers
- Sub-processor audit reports for the audit period confirming equivalent obligations are enforced
- Storage decommissioning test results confirming no cross-tenant data remanence
- Backup restoration logs with authorisation records for all restoration events

---

<!-- QA_VERIFIED: [Date] -->
