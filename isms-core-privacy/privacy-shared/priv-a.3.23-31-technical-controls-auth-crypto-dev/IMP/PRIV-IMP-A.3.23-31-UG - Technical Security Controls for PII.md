<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.23-31-UG:privacy:UG:a.3.23-31 -->
**PRIV-IMP-A.3.23-31-UG — Technical Security Controls for PII — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Technical Security Controls for PII — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.3.23-31-UG |
| **Related Policy** | PRIV-POL-A.3.23-31 (Technical Security Controls for PII) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial user guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant technical or regulatory change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.3.23-31 (Technical Security Controls for PII — the governing policy)
- PRIV-IMP-A.3.23-31-TG (Technical Security Controls for PII — Technical Guide)
- ISMS-POL-A.8.24 (Use of Cryptography — cryptographic standards framework)
- ISMS-POL-A.8.25-31 (Secure Development — secure development framework)

---

## Purpose of This Guide

This guide explains **how to implement** the nine technical security controls for PII processing (A.3.23–A.3.31). It covers how to apply authentication, backup, logging, cryptography, secure development, application security, architecture, outsourced development, and test information controls specifically to PII-processing systems.

**Who this guide is for**: CISO, IT Security Team, Development/DevOps Teams, IT Architecture, DPO.

---

## Part 1 — Secure Authentication for PII Systems (A.3.23)

### 1.1 Assessing Authentication Requirements for a PII System

When a system is designated as a PII processing system (or when an existing system gains PII processing scope):

1. Identify the PII classifications handled by the system (CONFIDENTIAL / RESTRICTED / INTERNAL — per PRIV-POL-A.3.5-7)
2. Identify access types: internal access (on-premise or internal network), remote access (VPN, internet-accessible), privileged/administrative access
3. Select the authentication standard from the policy table (PRIV-POL-A.3.23-31) and confirm the specific technology from PRIV-IMP-A.3.23-31-TG
4. Configure the authentication controls and document the configuration in the PII System Authentication Register

### 1.2 Configuring MFA for PII Systems

For all RESTRICTED PII systems and all remote access to CONFIDENTIAL PII systems:

1. CISO selects an approved MFA technology from PRIV-IMP-A.3.23-31-TG
2. IT Security Team configures MFA enforcement in the identity provider (IdP) — MFA must be mandatory, not optional
3. Verify: attempt to access the PII system without the second factor — access must be denied
4. Document: MFA enforcement configuration and test result in PII System Authentication Register
5. Review: annually or on any change to the system's access architecture

**MFA exceptions**: If a technical constraint prevents MFA for a specific integration or service account, document the exception and implement compensating controls (network-level restriction, enhanced monitoring). DPO notification required for exceptions on RESTRICTED PII systems.

### 1.3 Failed Authentication Response

For all PII-processing systems, configure:
- Account lockout after failed attempts per threshold defined in PRIV-IMP-A.3.23-31-TG
- Alerts to IT Security Team on repeated failed attempts (potential brute force)
- Log all failed authentication attempts with identity, source, and timestamp (per A.3.25 logging requirements)

---

## Part 2 — Backup of PII and PII Systems (A.3.24)

### 2.1 Confirming PII Backup Coverage

The DPO confirms annually with IT Security Team that all PII data stores and systems are covered by the backup regime:

1. Generate list of all systems in scope for PII processing (from PII System Inventory in PRIV-IMP-A.3.23-31-TG)
2. Cross-reference against backup coverage reports — confirm each PII system is included
3. Confirm backup encryption is enabled for each PII backup (use the same or equivalent key management as the primary data)
4. Confirm backup access controls — who can access the backup, and are access rights reviewed?
5. Document confirmation in annual backup compliance review record

### 2.2 Annual Backup Restoration Test

PII backup restorability must be tested at minimum annually:

1. IT Security Team selects a representative PII system backup for restoration testing
2. Restore the backup to a test environment (not overwriting production)
3. Verify: data is complete, readable, and intact (no corruption)
4. For special category PII backups: test that the decryption keys are accessible and decryption is successful
5. Document: backup reference tested, date, test environment, outcome, data integrity verification method
6. Any failure: escalate to CISO and DPO; treat as a risk event; investigate root cause before relying on that backup

---

## Part 3 — Logging for PII Processing (A.3.25)

### 3.1 Configuring PII Logging

For each system identified in the PII System Inventory:

1. Confirm the required logging events from PRIV-POL-A.3.23-31 are configured and capturing (access to PII stores, bulk operations, rights fulfilment operations, admin operations, failed access)
2. Confirm log storage location is classified CONFIDENTIAL and access-controlled
3. Confirm log tamper protection: logs should be written to append-only or WORM storage where technically feasible
4. Confirm log retention meets minimum 12 months (or longer per regulatory or contractual requirement)
5. Configure alerting for anomalous events: bulk export, repeated failed access, access outside business hours, access to high-risk PII categories (special category data)

### 3.2 Periodic Log Review

The CISO (or delegated IT Security Team lead) reviews PII access logs:

| Review Type | Frequency | Focus |
|-------------|-----------|-------|
| Automated alerting | Continuous | Anomalous bulk access; failed authentication threshold exceeded; privileged access anomalies |
| Operational review | Monthly | Unusual patterns; access by departed or changed-role personnel; data export volume |
| Compliance review | Annual | Evidence of logging coverage; log integrity; log availability for potential incident investigation |
| Incident review | On incident | Specific log pull for the incident window per PRIV-POL-A.3.11-12 |

---

## Part 4 — Cryptography for PII Processing (A.3.26)

### 4.1 Confirming Encryption Coverage for PII

Annually, CISO confirms:

| Check | Method | Outcome |
|-------|--------|---------|
| Encryption at rest — PII databases | Database encryption configuration review | Confirmed / Gap |
| Encryption at rest — PII file stores | Storage encryption configuration review | Confirmed / Gap |
| Encryption in transit — PII APIs | TLS configuration review (version + cipher) | Confirmed / Gap |
| Encryption of PII backups | Backup encryption configuration review | Confirmed / Gap |
| Key management documentation | Key management procedure review | Current / Requires update |

Any gap is escalated to the CISO and DPO and treated as a risk requiring remediation.

### 4.2 Pseudonymisation and Anonymisation Decisions

When a team proposes using PII for analytics, testing, or secondary purposes:

1. The team submits a request to the DPO describing the intended use and the proposed de-identification approach
2. DPO assesses: is the proposed technique pseudonymisation (reversible) or anonymisation (irreversible)?
3. For pseudonymisation: PII continues to be in scope — apply all PII controls to the pseudonymised dataset; maintain the re-identification key under access control
4. For anonymisation: DPO confirms that re-identification is not reasonably possible given the available data — if confirmed, GDPR/FADP no longer apply to that dataset. Document the confirmation.
5. Do not treat data as anonymised without explicit DPO confirmation — this is a legal determination, not a technical one

### 4.3 Key Management

Cryptographic keys protecting PII:
- Are stored in a dedicated key management system (KMS) or hardware security module (HSM) — never alongside the PII they protect
- Are accessible only to authorised personnel listed in the key management access record
- Are rotated per the key rotation schedule in PRIV-IMP-A.3.23-31-TG
- Key compromise: treated as PII incident — report to DPO immediately; initiate re-encryption with new key

---

## Part 5 — Secure Development Life Cycle for PII Systems (A.3.27)

### 5.1 Privacy-by-Design Integration in Development

For any new system or significant change to a system that processes PII, development teams must:

1. **At design stage**: Identify PII processing scope — what PII will the system collect, store, or process?
2. **Data minimisation review**: Can the purpose be achieved with less PII? Remove unnecessary fields before design is finalised
3. **Privacy-by-default configuration**: Define what the default settings will be — minimum data collection; minimum retention; minimum disclosure. Document why defaults are set as they are.
4. **DPIA trigger check**: Would this processing be "likely to result in a high risk" per GDPR Article 35? If yes, DPO must conduct a DPIA before development commences (not after)
5. **Security requirements**: DPO and CISO approve PII security requirements (A.3.28) before sprint commencement
6. **Pre-deployment review**: Confirm privacy-by-design requirements are implemented before production deployment

### 5.2 Privacy-by-Design Review Checklist

Use this checklist in design review for any new or significantly changed PII-processing system:

| Check | Result |
|-------|--------|
| PII scope mapped — only necessary PII collected | Yes / No — [detail required fields] |
| Privacy-by-default settings defined and documented | Yes / No |
| DPIA trigger assessed (and DPIA conducted if required) | Yes / DPIA not required — [rationale] |
| Logging for required PII events configured in design | Yes / No |
| Encryption at rest and in transit specified | Yes / No |
| Access controls and authentication aligned to PII classification | Yes / No |
| Data retention and deletion mechanism included | Yes / No |
| DPO approval obtained | Yes / No — Date: [__] |

---

## Part 6 — Application Security Requirements for PII (A.3.28)

### 6.1 Documenting PII Security Requirements

Before development begins (or before procurement decision for acquired software):

1. Development/architecture team documents the PII security requirements for the application — use the PII Application Security Requirements template in PRIV-IMP-A.3.23-31-TG
2. DPO reviews requirements for completeness (does the template cover: authentication, access control, encryption, logging, retention/deletion)
3. CISO reviews for security architecture alignment
4. Both DPO and CISO sign off before development commences
5. Requirements incorporated into the development specification and acceptance criteria

For **acquired applications**: security requirements must be in the procurement RFP/RFI. Vendor assessment covers: authentication capabilities, encryption support, audit logging, data deletion, and security certifications held.

---

## Part 7 — Secure Architecture Principles for PII (A.3.29)

### 7.1 Applying PII Architecture Principles

IT Architecture applies the six PII architecture principles from PRIV-POL-A.3.23-31 in design reviews:

| Principle | Design Review Question |
|-----------|----------------------|
| Minimum exposure | Does PII flow through any components that don't need to see it? Can it be reduced? |
| Least privilege in architecture | Does each service/component access only the PII required for its function? |
| Data segregation | Are PII from different purposes or different sensitivity levels logically separated? |
| Auditability | Will the architecture produce the required PII access logs without additional work? |
| Restorability | Does the architecture support the RPO/RTO for PII recovery (backup, failover)? |
| Pseudonymisation pathway | Is there a technical pathway to pseudonymise or anonymise PII for secondary use? |

IT Architecture documents the review outcome and any residual deviations (with DPO and CISO agreement) in the design record.

---

## Part 8 — Outsourced Development of PII Systems (A.3.30)

### 8.1 Engaging an Outsourced Development Partner for PII Systems

Before an outsourced development partner accesses any PII-capable system or environment:

1. Categorise the partner per PRIV-POL-A.3.8-10 supplier categorisation (typically PII-Adjacent Supplier or PII Processor depending on the engagement scope)
2. Ensure a signed agreement is in place covering: PII security obligations; no use of real PII in development/test without DPO approval; incident notification; confidentiality survival; deletion on termination
3. Communicate the PII security requirements for the project (A.3.28) to the partner before work commences
4. Include PII security requirements in acceptance testing criteria — development not accepted until PII controls confirmed working
5. Conduct or require a security review of developed code before production deployment

### 8.2 Monitoring Outsourced Development

During the engagement:
- Require the partner to report any PII incident immediately
- Reserve the right to audit or review development artefacts for PII compliance
- Include PII compliance as a criteria in project phase sign-off

---

## Part 9 — Test Information Related to PII (A.3.31)

### 9.1 Default: Synthetic or Anonymised Test Data

Development and QA teams must use synthetic or anonymised test data for PII-processing system testing. The default process:

1. Request test data from the data engineering or IT Security Team
2. Receive synthetically generated dataset with realistic structure but no real PII (generated by approved tools — see PRIV-IMP-A.3.23-31-TG)
3. If synthetic data is insufficient for the specific test: request anonymised extract — DPO confirms irreversible anonymisation before releasing

### 9.2 Exception Process: Real PII in Testing

Where the team believes real PII is operationally necessary for a specific test:

1. Submit a written request to the DPO: what PII is needed, why synthetic data is insufficient, which specific test, how long the PII will be in the test environment
2. DPO approves or rejects — approval is time-limited to the specific test (not open-ended)
3. Apply production-equivalent access controls and encryption to the test environment during the period
4. Log all access to the real PII in the test environment
5. On test completion: delete all real PII from the test environment; confirm and document deletion
6. If DPO approval is not obtained: do not proceed with real PII

---

## Evidence Checklist

- [ ] PII System Authentication Register — all PII systems registered with authentication standard confirmed
- [ ] Annual backup coverage review — all PII systems confirmed in backup; encryption confirmed
- [ ] Annual backup restoration test record — PII integrity verified
- [ ] PII logging configuration — required events logging confirmed for all in-scope systems
- [ ] Encryption coverage confirmation — at rest and in transit for all CONFIDENTIAL/RESTRICTED PII
- [ ] Pseudonymisation/anonymisation decisions — DPO confirmation on file for any anonymisation
- [ ] Privacy-by-design review checklists — for all new or significantly changed PII systems
- [ ] PII Application Security Requirements documents — approved by DPO and CISO
- [ ] PII architecture design review records
- [ ] Outsourced development PII agreements — with required clauses confirmed
- [ ] Test data usage records — synthetic/anonymised data standard; DPO approvals for any real PII use; deletion confirmations

---

<!-- QA_VERIFIED: [Date] -->
