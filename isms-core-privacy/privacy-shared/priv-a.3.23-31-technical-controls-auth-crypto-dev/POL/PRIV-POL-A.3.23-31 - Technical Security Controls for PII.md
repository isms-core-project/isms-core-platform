<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.23-31:privacy:POL:a.3.23-31 -->
**PRIV-POL-A.3.23-31 — Technical Security Controls for PII**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Technical Security Controls for PII |
| **Document Type** | Policy |
| **Document ID** | PRIV-POL-A.3.23-31 |
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
- Technical: Development Lead / IT Architecture
- Final Authority: Executive Management

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- PRIV-POL-01 (Privacy Governance and Decision-Making Framework)
- PRIV-IMP-A.3.23-31-UG (Technical Security Controls for PII — User Guide)
- PRIV-IMP-A.3.23-31-TG (Technical Security Controls for PII — Technical Guide)
- ISMS-POL-A.8.2 (Privileged Access Rights — ISMS parallel)
- ISMS-POL-A.8.5 (Secure Authentication — ISMS parallel)
- ISMS-POL-A.8.13 (Information Backup — ISMS parallel)
- ISMS-POL-A.8.15-16 (Logging and Monitoring — ISMS parallel)
- ISMS-POL-A.8.24 (Use of Cryptography — ISMS parallel)
- ISMS-POL-A.8.25-31 (Secure Development — ISMS parallel)
- ISO/IEC 27701:2025 Controls A.3.23 through A.3.31
- ISO/IEC 27701:2025 Annex B (Implementation guidance B.3.23 through B.3.31)
- GDPR Article 25 (Privacy by design and by default); Article 32 (Security of processing)
- CH FADP Article 7 (Technical and organisational measures)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for technical security controls as they apply to the processing of Personally Identifiable Information (PII), covering authentication, backup, logging, cryptography, secure development, application security, system architecture, outsourced development, and test information — in accordance with ISO/IEC 27701:2025 Controls A.3.23 through A.3.31.

**Scope**: All technical controls implemented for systems, applications, and infrastructure that process PII; all software and system development activities that involve PII processing; all test environments that use or simulate PII.

**Purpose**: Define organisational requirements for nine technical control areas that protect PII at the system and development level. This policy establishes **WHAT** technical requirements apply to PII-processing systems, **WHO** holds accountability, and **WHEN** reviews and verifications occur. Implementation procedures (**HOW**) are documented in PRIV-IMP-A.3.23-31-UG and PRIV-IMP-A.3.23-31-TG.

**Role Applicability**: This policy applies to the organisation acting as **both PII Controller and PII Processor**. Controls A.3.23–A.3.31 are shared controls (Table A.3) and apply regardless of processing role.

**Combined Control Rationale**: A.3.23–A.3.31 constitute the technical assurance layer for PII processing. They extend and specialise the ISMS technical control framework for PII contexts — ensuring that every significant technical control domain (authentication, backup, logging, cryptography, development, architecture, outsourcing, testing) explicitly addresses PII. GDPR Article 25 (privacy by design and by default) and Article 32 (appropriate technical measures) provide the regulatory foundation for this group as a whole.

---

# Scope and Applicability

## ISO/IEC 27701:2025 Control Statements

**Control A.3.23 — Secure authentication**
Control A.3.23 requires [Organisation] to implement secure authentication technologies and procedures for PII processing systems, calibrated to the access restrictions applicable to each system or dataset.

**Control A.3.24 — Information backup**
Control A.3.24 requires [Organisation] to maintain backup copies of PII and of the software and systems involved in PII processing, and to test those backups regularly.

**Control A.3.25 — Logging**
Control A.3.25 requires [Organisation] to produce, store, protect, and analyse logs that capture activities, exceptions, faults, and other relevant events related to PII processing.

**Control A.3.26 — Use of cryptography**
Control A.3.26 requires [Organisation] to define and implement rules for the effective use of cryptography in PII processing contexts, including cryptographic key management.

**Control A.3.27 — Secure development life cycle**
Control A.3.27 requires [Organisation] to establish and apply rules for the secure development of software and systems that are involved in PII processing.

**Control A.3.28 — Application security requirements**
Control A.3.28 requires [Organisation] to identify, specify, and approve information security requirements related to PII processing when developing or acquiring applications.

**Control A.3.29 — Secure system architecture and engineering principles**
Control A.3.29 requires [Organisation] to establish, document, maintain, and apply principles for engineering secure systems in the context of PII processing, across all information system development activities.

**Control A.3.30 — Outsourced development**
Control A.3.30 requires [Organisation] to direct, monitor, and review activities related to the outsourced development of systems used for PII processing.

**Control A.3.31 — Test information**
Control A.3.31 requires [Organisation] to appropriately select, protect, and manage test information used in the context of PII processing systems.

## What This Policy Covers

All nine controls listed above, applied to:

- Systems and applications that process PII as part of their primary function
- Infrastructure and platforms that host or connect to PII processing systems
- Software and systems developed or acquired for PII processing purposes
- Test environments used during development, QA, or integration of PII-processing systems

## What This Policy Does NOT Cover

- ISMS-wide technical controls (see ISMS-POL-A.8.x for full technical controls framework)
- Access rights governance (see PRIV-POL-A.3.8-10)
- Endpoint device management (see PRIV-POL-A.3.20-22)
- Processor agreement requirements (see PRIV-POL-A.2.2.2-7)

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 25 (privacy by design and by default — technical controls as design requirement); Article 32 (pseudonymisation, encryption, availability restoration, regular testing of TOMs)
- **CH FADP**: Article 7 (technical measures proportionate to risk)
- **ISO/IEC 27701:2025**: Controls A.3.23–A.3.31 (normative)

**Tier 2: Conditional Applicability** (per PRIV-POL-00):

- **ISO/IEC 27018:2025**: Annex A — cloud PII processing technical controls where applicable

**Tier 3: Informational Reference** (per PRIV-POL-00):

- **ISO/IEC 27002:2022**: Implementation guidance for controls 8.5 (authentication), 8.13 (backup), 8.15–16 (logging), 8.24 (cryptography), 8.25–8.31 (secure development)
- **ISO/IEC 27701:2025 Annex B**: B.3.23 through B.3.31

For complete regulatory categorisation, refer to PRIV-POL-00.

---

# Policy Statements

## A.3.23 — Secure Authentication for PII Processing

[Organisation] SHALL implement secure authentication technologies and procedures for access to PII processing systems, based on the access restrictions defined for each PII dataset and system.

### Authentication Requirements for PII Systems

| PII Sensitivity | Minimum Authentication Requirement |
|----------------|-------------------------------------|
| CONFIDENTIAL PII | Multi-factor authentication (MFA) for remote access; strong password policy for internal access |
| RESTRICTED PII (special category) | MFA required for ALL access (internal and remote) |
| Administrative / privileged access to PII | MFA required; separate privileged credential from standard identity |

Authentication standards and approved MFA technologies are defined in PRIV-IMP-A.3.23-31-TG, consistent with ISMS-POL-A.8.5.

### Authentication Procedure Requirements

- Authentication procedures SHALL enforce access restrictions aligned to the access rights defined in PRIV-POL-A.3.8-10
- Failed authentication attempts to PII systems SHALL be logged and trigger lockout per the thresholds defined in PRIV-IMP-A.3.23-31-TG
- Authentication credentials for PII systems SHALL be unique per individual; shared credentials are prohibited for PII system access

---

## A.3.24 — Backup of PII and Related Systems

[Organisation] SHALL maintain backup copies of PII and of the software and systems related to PII processing, and shall regularly test the integrity and restorability of those backups.

### PII Backup Requirements

- All PII processed by [Organisation] SHALL be covered by a backup regime with documented recovery point objectives (RPO) aligned to the PII processing criticality and regulatory requirements
- Backups containing PII SHALL be subject to the same classification and access controls as the primary PII (CONFIDENTIAL or RESTRICTED as applicable)
- Backup copies containing PII SHALL be encrypted with the same standard as the primary data
- Offsite or cloud backup copies containing PII SHALL be subject to equivalent security controls to primary storage, including access restrictions and encryption in transit and at rest

### Backup Testing

- Backup restoration SHALL be tested at minimum annually to confirm that PII is recoverable and complete
- Test restoration outcomes SHALL be documented, including data integrity verification
- Restoration test failures involving PII SHALL be treated as a risk event and escalated to the CISO and DPO

---

## A.3.25 — Logging for PII Processing

[Organisation] SHALL produce, store, protect, and analyse logs that record activities, exceptions, faults, and other relevant events related to PII processing.

### PII Logging Requirements

The following events relating to PII processing SHALL be logged:

- Access to PII data stores (read, write, export) by authenticated users
- Failed access attempts to PII systems
- Bulk data operations involving PII (export, deletion, pseudonymisation, anonymisation)
- Changes to access rights for PII systems (grant, revoke, modify)
- Privileged operations on PII processing systems
- Data subject rights fulfilment operations (access, erasure, restriction, portability)
- System and application errors or exceptions in PII processing components

### Log Protection

Logs containing PII processing activity SHALL be:

- Protected against modification and deletion (tamper-evident storage)
- Classified at minimum CONFIDENTIAL
- Accessible only to authorised personnel (IT Security Team, CISO, DPO for privacy investigation purposes)
- Retained for minimum 12 months as an operational floor, with a minimum of 3 years for logs that may be required as evidence of GDPR accountability compliance (e.g., access logs for data subject rights fulfilment, bulk deletion and anonymisation operations, and privileged access to PII systems). The CISO and DPO shall agree specific retention periods per log category in PRIV-IMP-A.3.23-31-TG, taking into account applicable regulatory requirements and contractual obligations

### Log Analysis

Logs SHALL be reviewed:

- On an exception basis (alerts for anomalous PII access patterns)
- As part of periodic compliance review (PRIV-POL-A.3.13-16)
- In response to a privacy incident (PRIV-POL-A.3.11-12)
- As part of access rights review (PRIV-POL-A.3.8-10)

Log analysis standards and tools are defined in PRIV-IMP-A.3.23-31-TG, consistent with ISMS-POL-A.8.15-16.

---

## A.3.26 — Cryptography for PII Processing

[Organisation] SHALL define and implement rules for the effective use of cryptography related to PII processing, including cryptographic key management.

### Cryptographic Requirements for PII

- **Encryption at rest**: All CONFIDENTIAL and RESTRICTED PII stored in databases, files, or on media SHALL be encrypted at rest using an approved algorithm (minimum AES-256 or equivalent per ISMS-POL-A.8.24)
- **Encryption in transit**: All PII transmitted across networks SHALL be encrypted in transit using current TLS standards (minimum TLS 1.2; TLS 1.3 preferred)
- **Pseudonymisation**: Where PII is used for analytics, testing, research, or secondary purposes, pseudonymisation SHALL be applied to reduce re-identification risk where technically feasible
- **Anonymisation**: Where irreversible anonymisation is applied, the result is no longer PII subject to GDPR — but anonymisation must be robust: the DPO shall confirm, using a documented methodology, that re-identification is not reasonably possible by any means reasonably likely to be used, considering the risks of singling out (isolating an individual in a dataset), linkability (linking records across datasets to identify an individual), and inference (deriving attributes about an individual from remaining data). Anonymisation that does not withstand this assessment shall be treated as pseudonymisation, and the underlying data continues to be PII

### Key Management for PII Encryption

- Cryptographic keys protecting PII SHALL be managed separately from the PII they protect
- Key access SHALL be restricted to authorised personnel with documented operational need
- Key rotation SHALL occur at intervals defined in PRIV-IMP-A.3.23-31-TG
- Key compromise or loss involving PII-protecting keys SHALL be treated as a PII security incident per PRIV-POL-A.3.11-12

Full cryptographic standards are defined in ISMS-POL-A.8.24; this section establishes the PII-specific requirements that operate within that framework.

---

## A.3.27 — Secure Development Life Cycle for PII Systems

[Organisation] SHALL establish and apply rules for secure development of software and systems related to PII processing.

### PII in Secure Development

The secure development rules for systems involving PII processing SHALL include:

- **Privacy by Design**: Privacy and PII protection requirements SHALL be considered from the earliest design stage of any system intended to process PII; retrofitting privacy controls is not an acceptable approach
- **Privacy by Default**: System defaults SHALL minimise PII collection and processing; the most privacy-protective settings SHALL be the default, not requiring individual configuration by end users
- **PII data minimisation in design**: Systems SHALL be designed to collect and process only the minimum PII necessary for the stated purpose; excess field collection SHALL be identified and removed during design review
- **Separation of PII concerns**: Where technically feasible, PII SHALL be isolated from non-PII data in system design (separate databases, separate processing paths)

### GDPR Article 25 Compliance

Systems involving PII processing SHALL be documented as privacy-by-design compliant before production deployment. The DPIA process (PRIV-POL-A.1.2.6-9) SHALL be triggered for high-risk processing systems during the design phase, not after deployment.

---

## A.3.28 — Application Security Requirements for PII

[Organisation] SHALL identify, specify, and approve information security requirements related to PII processing when developing or acquiring applications.

### PII Security Requirements in Development and Acquisition

For any application that processes PII (whether developed in-house or acquired):

- PII security requirements SHALL be documented before development begins or before procurement decision
- Requirements SHALL address at minimum: authentication, access control, encryption at rest and in transit, logging, and data retention/deletion
- Requirements SHALL be approved by the DPO (for privacy requirements) and CISO (for security requirements) before commencement
- For acquired applications: security requirements SHALL be included in procurement specifications; vendor security assessment SHALL address PII processing controls

### Security Requirements Review

PII application security requirements SHALL be reviewed:

- At each major version release or significant change
- Upon changes to applicable regulatory requirements
- Following a security incident involving the application

---

## A.3.29 — Secure Architecture and Engineering Principles for PII

[Organisation] SHALL establish, document, maintain, and apply principles for engineering secure systems related to PII processing.

### PII Architecture Principles

The following principles SHALL be applied to system architecture involving PII:

1. **Minimum exposure**: PII shall flow through the minimum number of system components necessary; unnecessary exposure of PII to intermediate systems or logs shall be avoided
2. **Least privilege in architecture**: System components shall access only the PII they require; service-to-service access to PII shall be scoped and authenticated
3. **Data segregation**: Where feasible, PII from different processing purposes or different data subjects shall be logically segregated
4. **Auditability**: Systems processing PII shall be designed to produce the logs required by A.3.25 without additional instrumentation
5. **Restorability**: Architecture shall support the backup and recovery requirements of A.3.24 for PII
6. **Anonymisation and pseudonymisation pathways**: Architecture shall include technical mechanisms to pseudonymise or anonymise PII for secondary use cases without requiring access to primary PII stores

These principles extend and specialise the ISMS secure engineering principles in ISMS-POL-A.8.27.

---

## A.3.30 — Outsourced Development of PII Processing Systems

[Organisation] SHALL direct, monitor, and review activities related to outsourced development of PII processing systems.

### Requirements for Outsourced Development

Where development of systems that process PII is outsourced to a third party:

- The development partner SHALL be treated as a PII processor or PII-adjacent supplier per PRIV-POL-A.3.8-10 (supplier categorisation)
- An agreement covering PII security obligations SHALL be in place before development access to PII (or PII-capable systems) is granted
- PII security requirements (A.3.28) SHALL be communicated and agreed before development commences
- Security and privacy requirements SHALL be included in acceptance testing before deployment
- [Organisation] SHALL retain the right to review development artefacts (code, design documents) for PII compliance
- The development partner SHALL report any PII incident discovered during development immediately

### PII in Outsourced Development Environments

- Development partners SHALL NOT use real PII in development or test environments without explicit DPO approval
- Where real PII must be used (e.g., for reproducible defect investigation), approval SHALL be time-limited and documented; the PII SHALL be deleted after the specific investigation concludes

---

## A.3.31 — Test Information Related to PII

[Organisation] SHALL appropriately select, protect, and manage test information related to PII processing.

### Prohibition on Real PII in Test Environments

Real PII SHALL NOT be used in test environments as a default practice. Test environments SHALL use:

- Synthetically generated data that resembles PII in structure but contains no real personal data, OR
- Irreversibly anonymised data from real PII datasets (DPO confirmation of anonymisation required)

### Exception: Use of Real PII in Testing

Where use of real PII in testing is operationally necessary (e.g., to reproduce a specific data defect), the following SHALL apply:

- Written approval from the DPO before real PII is copied to the test environment
- Scope limited to the minimum PII needed, for the minimum duration required
- Test environment SHALL apply the same access controls and encryption as the production environment
- Real PII SHALL be deleted from the test environment immediately after the specific test concludes; deletion SHALL be confirmed and documented
- All access to real PII in the test environment SHALL be logged

### Test Data Management

Synthetic and anonymised test data sets used for PII processing system testing SHALL be:

- Documented in the test data inventory (owner, format, currency, purpose)
- Protected against accidental replacement with real PII
- Reviewed periodically to ensure they remain representative for testing purposes

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Responsibilities for A.3.23–A.3.31 |
|------|-------------------------------------|
| **Data Protection Officer (DPO)** | Approves PII security requirements for new systems (A.3.28); confirms anonymisation decisions (A.3.26); approves DPIA for new PII-processing systems (A.3.27); approves use of real PII in testing (A.3.31); reviews outsourced development PII compliance (A.3.30) |
| **CISO** | Defines authentication standards (A.3.23); sets backup standards (A.3.24); manages logging infrastructure (A.3.25); maintains cryptographic standards (A.3.26); owns secure development framework (A.3.27–A.3.30) |
| **IT Security Team** | Implements authentication, backup, logging, and encryption controls; monitors logs for PII access anomalies; manages key management infrastructure |
| **Development / DevOps Teams** | Applies privacy-by-design and secure development rules; implements PII security requirements in code; uses only approved test data (no real PII without DPO approval) |
| **IT Architecture** | Maintains secure architecture principles for PII; reviews new system designs for PII architecture compliance |
| **Procurement / Legal** | Ensures outsourced development contracts include PII security obligations |

---

# Evidence Requirements

The following evidence demonstrates operation of this policy:

| Evidence | Description | Retention |
|---------|-------------|-----------|
| PII System Authentication Configuration | MFA enforcement records and access restriction configurations for PII systems | Current + 3 years |
| Backup Test Records | Annual restoration test outcomes for PII backups | 3 years |
| PII Access Logs | Activity logs for PII data store and system access | Minimum 12 months; longer per regulatory or contractual requirement |
| Cryptographic Standards Documentation | Approved algorithms, key management procedures, key rotation records | Current + 3 years |
| Privacy-by-Design Assessments | Design review records confirming PbD compliance for PII-processing systems | Duration of system operation + 3 years |
| PII Security Requirements Documents | Approved security requirements for developed or acquired PII applications | Duration of application operation + 3 years |
| Real PII Test Approval Records | DPO approvals for use of real PII in test environments, with deletion confirmations | 3 years |
| Outsourced Development PII Agreements | Agreements with development partners covering PII security obligations | Duration of agreement + 3 years |

---

# Audit Considerations

Auditors verifying compliance with A.3.23–A.3.31 should expect to find:

**For A.3.23 (Authentication)**: MFA configuration evidence for CONFIDENTIAL/RESTRICTED PII systems; access restriction alignment with defined access rights; failed login logging.

**For A.3.24 (Backup)**: Backup policy covering PII; encryption of backups; annual restoration test records with PII integrity verification.

**For A.3.25 (Logging)**: Defined PII events being logged; tamper-evident log storage; access controls on logs; evidence of log analysis for anomaly detection.

**For A.3.26 (Cryptography)**: Encryption at rest for CONFIDENTIAL/RESTRICTED PII; TLS enforcement for PII in transit; key management documentation; pseudonymisation usage evidence.

**For A.3.27 (Secure development)**: Privacy-by-design evidence in system design records; DPIA triggering for high-risk systems; data minimisation review in design.

**For A.3.28 (Application security requirements)**: Documented and DPO/CISO-approved PII security requirements for in-scope applications; security requirements in procurement specifications.

**For A.3.29 (Architecture principles)**: Documented PII architecture principles; design review evidence applying the principles to new systems.

**For A.3.30 (Outsourced development)**: Outsourced development agreements with PII security clauses; no real PII in outsourced development environments without DPO approval.

**For A.3.31 (Test information)**: Default use of synthetic or anonymised test data; DPO approval records for any use of real PII in testing; deletion confirmations for real PII after testing.

---

<!-- QA_VERIFIED: [Date] -->
