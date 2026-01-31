# ISMS-POL-A.8.24 – Use of Cryptography
## Comprehensive Policy & Implementation Framework (Master Document)

---

**Document ID**: ISMS-POL-A.8.24  
**Title**: Use of Cryptography Policy (Master Document)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Information Security Manager | Initial policy framework |

**Review Cycle**: Quarterly (or upon significant organizational/regulatory/cryptographic landscape changes)  
**Next Review Date**: [Approval Date + 3 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO) or IT Director
- Compliance: Legal/Compliance Officer (for regulatory alignment)
- Final Authority: Executive Management / Board (for strategic approval)

**Distribution**: All employees, contractors, third-party service providers with access to organizational systems  
**Related Standards**: ISO/IEC 27001:2022 Control A.8.24, ISMS-POL-00 (Regulatory Applicability Framework), NIST SP 800-57, FIPS 140-2/140-3, Swiss FADP, EU GDPR, PCI DSS, HIPAA

---

## Executive Summary

This document serves as the **master index** for the organization's cryptography control framework, implementing ISO/IEC 27001:2022 Control A.8.24.

**Purpose**: Define mandatory requirements for the use of cryptographic controls to protect the confidentiality, integrity, and authenticity of information processed, stored, or transmitted by the organization.

**Scope**: All information assets classified as Internal, Confidential, or Restricted; all cryptographic implementations including encryption, hashing, digital signatures, and key management; all employees, contractors, and third parties with access to organizational information.

**Framework Components**:
- **Policy Layer:** Governance documents defining requirements (13 documents, ~337 KB)
- **Assessment Layer:** Technical evaluation specifications (8 markdown specs, ~249 KB)
- **Implementation Layer:** Automated Excel workbook generators (5 Python scripts, ~371 KB)
- **Validation Layer:** Quality assurance and checking tools (8 Python scripts, ~143 KB)
- **Utility Layer:** Supporting scripts and tools (5 Python/Bash scripts, ~56 KB)
- **Integration Layer:** Executive dashboard with consolidated oversight

**Approach:** This framework uses a **system engineering methodology** rather than traditional paperwork-based compliance. All assessments are generated via Python scripts to ensure consistency, repeatability, and maintainability. A comprehensive validation suite ensures Excel workbooks are error-free and audit-ready.

**Maturity Achievement**: This framework has achieved **Level 4 (Quantitatively Managed)** maturity with automated assessment generation, quantitative compliance metrics, and quality validation suite.

---

## Control Alignment

**ISO/IEC 27001:2022 Annex A.8.24 - Use of Cryptography**

> *A policy on the use of cryptographic controls for protection of information should be developed and implemented.*

**ISO/IEC 27002:2022 Control 8.24 - Use of Cryptography**

This policy framework provides the organizational governance, requirements, roles, and procedures necessary to fulfill Control 8.24 objectives and ensure cryptographic controls protect the confidentiality, authenticity, and integrity of information across the Information Security Management System (ISMS).

**Control Objective**: Define and implement cryptographic controls to protect sensitive information throughout its lifecycle (transmission, storage, processing) using approved algorithms, secure key management, and risk-based protection levels.

**Control Implementation**: This framework addresses:
- Selection of appropriate cryptographic algorithms and key lengths
- Secure key generation, storage, distribution, and destruction
- Encryption for data at rest and data in transit
- Digital signatures and authentication mechanisms
- Certificate lifecycle management
- Cryptographic incident response
- Compliance with legal, regulatory, and contractual requirements

---

## 1. Framework Structure

### 1.1 Purpose

Define mandatory requirements for the use of cryptographic controls to protect the confidentiality, integrity, and authenticity of information processed, stored, or transmitted by the organization.

### 1.2 Scope

This framework applies to:
- All information assets classified as **Internal, Confidential, or Restricted**
- All systems, applications, networks, and services processing organizational data
- All cryptographic implementations including encryption, hashing, digital signatures, and key management
- All employees, contractors, and third parties with access to organizational information
- All cloud services, third-party providers, and outsourced operations handling organizational data

### 1.3 Users

This framework is binding for:
- **Employees** – Must comply with all cryptographic requirements
- **External service providers** – Must meet contractual cryptographic obligations
- **Management** – Accountable for cryptographic control effectiveness within their domains
- **System owners** – Responsible for implementation within their domains
- **Development teams** – Implement cryptography in applications per standards
- **Auditors and regulators** – May review for compliance verification

---

## 2. Regulatory Framework

This control implements requirements from regulations categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

The categorization below (Mandatory, Conditional, Informational) follows the methodology defined in POL-00. For complete regulatory applicability determination and assessment processes, refer to ISMS-POL-00.

### 2.1 Mandatory Compliance

| Regulation/Standard | Applicability | Key Cryptography Requirements |
|---------------------|---------------|-------------------------------|
| **Swiss FADP (nDSG)** | All operations | Article 8 - Appropriate technical and organizational measures including encryption where necessary |
| **EU GDPR** | Where processing EU resident data | Article 32 - Encryption of personal data, pseudonymization as security measure |
| **ISO/IEC 27001:2022** | Certification scope | Control A.8.24 implementation, documented cryptography policy, evidence of controls |

### 2.2 Sector-Specific Regulations (Conditional)

| Framework | Applicability | Cryptography Requirements |
|-----------|---------------|---------------------------|
| **PCI DSS v4.0** | Payment card processing | Strong cryptography for cardholder data transmission (TLS 1.2+), encryption at rest (AES-256), key management (dual control, split knowledge), cryptoperiod limits |
| **HIPAA Security Rule** | Healthcare data (US) | Encryption of ePHI at rest and in transit (§164.312(a)(2)(iv)), encryption as addressable specification, risk-based implementation |
| **SOX (Sarbanes-Oxley)** | Financial reporting | Encryption of financial data, cryptographic audit trail protection, key management for data integrity |
| **DORA** (Digital Operational Resilience Act) | EU financial services entities | ICT system encryption requirements, secure key management, crypto agility for resilience |
| **NIS2** (Network and Information Security Directive 2) | Essential/important entities (EU) | Encryption as cybersecurity risk management measure, secure authentication |
| **FINMA** | Swiss financial services | Encryption requirements for client data, secure communication channels |

**Note**: Sector-specific regulations apply only where organization operates in regulated industry or handles regulated data types. Organizations subject to multiple regulations must comply with the most stringent requirements.

### 2.3 Informational Reference / Best Practice

| Framework | Usage | Notes |
|-----------|-------|-------|
| **NIST SP 800-57** | Key management guidance | Recommendation for Key Management (Parts 1-3) |
| **NIST SP 800-175B** | Secure communications | Guide to Secure Group Communications |
| **NIST SP 800-38 Series** | Block cipher modes | Recommendation for Block Cipher Modes of Operation |
| **NIST SP 800-90A** | Random number generation | Recommendation for Random Number Generation Using Deterministic RBGs |
| **FIPS 140-2/140-3** | Cryptographic module standards | HSM/TPM compliance validation, module testing |
| **BSI TR-02102** | German crypto recommendations | Algorithm selection, key lengths, protocol configuration |
| **ANSSI** | French crypto guidance | Approved algorithms and parameters (RGS - Référentiel Général de Sécurité) |
| **OWASP** | Application security | Cryptographic Storage Cheat Sheet, Transport Layer Protection, Password Storage |
| **CSA (Cloud Security Alliance)** | Cloud cryptography | Cloud Controls Matrix - encryption requirements |

These frameworks inform cryptographic implementation practices but do not constitute mandatory compliance requirements unless explicitly required by contract or regulation.

### 2.4 Export Control Considerations

**Cryptography Export Regulations**:

| Regulation | Scope | Impact |
|-----------|-------|--------|
| **Wassenaar Arrangement** | International export controls | Export controls on cryptographic technology and "dual-use" items |
| **EU Dual-Use Regulation** (EU 2021/821) | EU member states | Controls on encryption products >56-bit symmetric, licensing requirements |
| **US EAR** (Export Administration Regulations) | US jurisdiction | ECCN 5A002/5D002 for encryption, license exceptions available |
| **US ITAR** | Military/defense items | Strict controls, registration requirements |

**Organizational Responsibilities**:
- Verify export compliance when deploying cryptographic solutions internationally
- Document export license exceptions (e.g., mass market encryption, publicly available encryption)
- Consult Legal/Compliance before cross-border cryptographic deployments
- Maintain records of cryptographic product exports

**Common License Exceptions**:
- **TSU** (Technology and Software Unrestricted): Publicly available encryption
- **ENC** (Encryption Commodities, Software, and Technology): Mass market encryption
- Organizations typically qualify for ENC exception but must document applicability

### 2.5 US Federal Requirements

References to United States federal frameworks and regulations (including, but not limited to, FISMA, FIPS, FedRAMP, NIST cybersecurity requirements) apply **only** where the organization:

- Acts as contractor, subcontractor, or service provider to US federal agencies
- Provides services to customers subject to such regulations (e.g., FedRAMP cloud services)
- Has explicit contractual obligations requiring such compliance

In all other cases, NIST references are provided for **informational and technical guidance purposes only** and do not constitute mandatory compliance requirements. NIST SP 800-series publications are recognized as cryptographic best practices globally and are used for technical alignment regardless of regulatory jurisdiction.

---

## 3. Policy Documents

The cryptography policy framework consists of the following modular documents:

### 3.1 Core Policy Documents

| Document ID | Title | Lines | Purpose |
|-------------|-------|-------|---------|
| **ISMS-POL-A.8.24** | Master Policy Framework (This Document) | ~1,313 | Overview, index, framework structure |
| **ISMS-POL-A.8.24-S1** | Purpose, Scope, Definitions | ~250 | Foundation, terminology, cryptographic concepts |
| **ISMS-POL-A.8.24-S2.1** | Use of Cryptographic Controls | ~200 | Algorithm selection, approved standards |
| **ISMS-POL-A.8.24-S2.2** | Data Transmission | ~250 | TLS, VPN, email encryption, API security |
| **ISMS-POL-A.8.24-S2.3** | Data Storage | ~300 | FDE, TDE, cloud encryption, backups |
| **ISMS-POL-A.8.24-S2.4** | Authentication | ~300 | Password hashing, MFA, certificates, SSO |
| **ISMS-POL-A.8.24-S2.5** | Compliance Requirements | ~250 | Legal, regulatory, contractual obligations |
| **ISMS-POL-A.8.24-S3** | Roles & Responsibilities | ~250 | RACI matrix, stakeholder duties |
| **ISMS-POL-A.8.24-S4** | Policy Governance | ~300 | Review, approval, change management |

### 3.2 Supporting Documents (Technical Annexes)

| Document ID | Title | Lines | Purpose |
|-------------|-------|-------|---------|
| **ISMS-POL-A.8.24-S5.A** | Approved Cryptographic Standards | ~400 | Algorithms, key lengths, protocols, deprecation schedule |
| **ISMS-POL-A.8.24-S5.B** | Exception Request Form Template | ~150 | Standardized exception documentation |
| **ISMS-POL-A.8.24-S5.C** | Incident Response for Cryptographic Events | ~350 | Compromised keys, expired certificates, weak crypto detection |
| **ISMS-POL-A.8.24-S5.D** | Quick Reference Guide | ~150 | One-pager for developers and system owners |

**Total Policy Layer:** 13 documents, approximately 3,463 lines

**Design Philosophy**: Each document is independently versionable to enable granular change management, targeted stakeholder reviews, and clear audit trails. Cryptographic standards (S5.A) are updated more frequently than policy framework.

### 3.3 Document Hierarchy

```
ISMS-POL-A.8.24 (Master) ← You are here
├── S1 (Purpose, Scope, Definitions)
├── S2 (Requirements Overview)
│   ├── S2.1 (Use of Cryptographic Controls)
│   ├── S2.2 (Data Transmission)
│   ├── S2.3 (Data Storage)
│   ├── S2.4 (Authentication)
│   └── S2.5 (Compliance Requirements)
├── S3 (Roles & Responsibilities)
├── S4 (Policy Governance)
└── S5 (Annexes)
    ├── S5.A (Approved Cryptographic Standards)
    ├── S5.B (Exception Request Form)
    ├── S5.C (Incident Response Procedures)
    └── S5.D (Quick Reference Guide)

Implementation Layer (Separate Documents):
├── ISMS-IMP-A.8.24.1 (Data Transmission Assessment)
├── ISMS-IMP-A.8.24.2 (Data Storage Assessment)
├── ISMS-IMP-A.8.24.3 (Authentication Assessment)
├── ISMS-IMP-A.8.24.4 (Key Management Assessment)
└── ISMS-IMP-A.8.24.5 (Compliance Summary Dashboard)
```

---

## 4. Assessment & Implementation Documents

### 4.1 Assessment Specifications (Markdown)

The framework includes **5 comprehensive assessment specifications** defining the structure and requirements for Excel workbook generation:

| Document ID | Title | Sheets | Checklist Items | Purpose |
|-------------|-------|--------|-----------------|---------|
| **ISMS-IMP-A.8.24.1** | Data Transmission Assessment | 16 | 186 items | 13 transmission types (HTTPS, VPN, SSH, etc.) |
| **ISMS-IMP-A.8.24.2** | Data Storage Assessment | 11 | 124 items | 7 storage types (endpoints, servers, databases, cloud, backups) |
| **ISMS-IMP-A.8.24.3** | Authentication Assessment | 9 | 96 items | 5 authentication methods (passwords, MFA, certificates, SSO) |
| **ISMS-IMP-A.8.24.4** | Key Management Assessment | 9 | 85 items | 5 lifecycle stages (generation, storage, rotation, backup, certificates) |
| **ISMS-IMP-A.8.24.5** | Compliance Summary Dashboard | 9 | 25+ KPIs | Consolidates all 4 assessments, executive metrics |

**Additional Specifications:**
| Document | Purpose |
|----------|---------|
| **ISMS-IMP-A.8.24 - Use of Cryptography Assessment Suite.md** | Master assessment suite overview and instructions |
| **ISMS-IMP-A.8.24.1 - Excel Template Specification.md** | Detailed workbook structure for Data Transmission (reference spec) |
| **generate_excel_workbooks.md** | Quick reference for script usage and validation |

**Total Assessment Specifications:** 8 markdown documents

### 4.2 Generated Excel Workbooks

When Python generators are executed, they produce:

| Workbook | Sheets | Purpose | Users |
|----------|--------|---------|-------|
| **ISMS-IMP-A.8.24.1_Data_Transmission_YYYYMMDD.xlsx** | 16 | TLS, VPN, email encryption, API security assessment | IT Ops, Security, DevOps |
| **ISMS-IMP-A.8.24.2_Data_Storage_YYYYMMDD.xlsx** | 11 | FDE, TDE, cloud encryption, backup encryption assessment | IT Ops, Security, DBAs |
| **ISMS-IMP-A.8.24.3_Authentication_YYYYMMDD.xlsx** | 9 | Password security, MFA, certificates, SSO assessment | IT Ops, Security, IAM |
| **ISMS-IMP-A.8.24.4_Key_Management_YYYYMMDD.xlsx** | 9 | Key lifecycle, HSM/KMS, rotation, certificate management | Security, IT Ops |
| **ISMS-IMP-A.8.24.5_Compliance_Dashboard_YYYYMMDD.xlsx** | 9 | KPIs, gap analysis, risk register, remediation roadmap | CISO, Management |

**Total Generated Output:** 54 sheets across 5 workbooks

### 4.3 Assessment Domains Explained

**Domain 1 - Data Transmission**:
- What transmission protocols are used? (HTTPS, SFTP, VPN, SSH, RDP, email)
- What TLS versions and cipher suites? (TLS 1.3 preferred, TLS 1.2 minimum, TLS 1.0/1.1 prohibited)
- What VPN protocols? (IKEv2, WireGuard, OpenVPN with strong crypto)
- What is certificate management? (CA hierarchy, expiry tracking, revocation)
- 13 transmission types assessed across 16 sheets

**Domain 2 - Data Storage**:
- What storage is encrypted? (Endpoints, servers, databases, cloud, backups)
- What encryption methods? (FDE: BitLocker/FileVault, TDE: SQL TDE/Oracle TDE, cloud: S3 SSE/Azure SSE)
- Where are encryption keys stored? (HSM, KMS, TPM - not with encrypted data)
- What is backup encryption status? (All backups encrypted, keys offline)
- 7 storage types assessed across 11 sheets

**Domain 3 - Authentication**:
- How are passwords protected? (bcrypt, scrypt, Argon2, PBKDF2 - not plaintext, not MD5)
- What is MFA coverage? (100% privileged, 100% remote access, 90%+ sensitive data)
- What certificate-based authentication? (TLS client certs, smart cards, PKI)
- What SSO/Federation? (SAML, OAuth 2.0, OpenID Connect)
- 5 authentication methods assessed across 9 sheets

**Domain 4 - Key Management**:
- How are keys generated? (CSRNG - cryptographically secure RNG)
- Where are keys stored? (HSM, cloud KMS, TPM - with access controls)
- What is rotation schedule? (Encryption keys: annual, signing keys: biennial, session keys: hourly/daily)
- How is key backup/recovery tested? (Documented procedures, tested quarterly)
- What is certificate lifecycle? (Issuance, renewal 30 days before expiry, revocation process)
- 5 lifecycle stages assessed across 9 sheets

**Domain 5 - Compliance Dashboard**:
- What is overall cryptographic maturity? (Level 1-5, current status, target)
- What are key performance indicators? (50+ KPIs: % compliance, weak crypto count, expired certs, MFA coverage)
- What gaps exist? (Weak algorithms, missing encryption, key management issues)
- What is remediation roadmap? (Prioritized improvements, timelines, budget, ownership)
- Executive summary with traffic light indicators

### 4.4 Assessment Workflow

```
┌────────────────────────────────────────────────────────────┐
│ PHASE 1: GENERATION (Day 1)                               │
│ • Run 5 Python generator scripts                          │
│ • Output: 5 Excel workbooks with 54 sheets total          │
│ • Validation: Run excel_sanity_check.py on each           │
│ • Quality: Run style_object_checker.py on each            │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ PHASE 2: ASSESSMENT (Weeks 1-3)                           │
│ • Technical SMEs complete assigned workbooks               │
│ • IT Operations: Data Transmission + Data Storage         │
│ • Security Engineering: Authentication + Key Management   │
│ • Provide evidence (configs, certs, scan results)         │
│ • Document gaps and exceptions                            │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ PHASE 3: NORMALIZATION (Day 15)                           │
│ • Run normalize_assessment_files.py                        │
│ • Clean up filename chaos from review process              │
│ • Create audit trail manifest                              │
│ • Verify completeness (no missing workbooks)               │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ PHASE 4: DASHBOARD (Day 16)                               │
│ • Generate compliance summary dashboard                    │
│ • Link to normalized assessment files                      │
│ • Auto-populate KPIs and compliance metrics                │
│ • Complete gap analysis and remediation roadmap            │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ PHASE 5: EXECUTIVE REVIEW (Week 4)                        │
│ • CISO reviews dashboard and gap analysis                  │
│ • Approve remediation roadmap and budget                   │
│ • Sign off on assessment package                           │
│ • Deliver to auditors (internal/external/regulatory)       │
└────────────────────────────────────────────────────────────┘
```

---

## 5. Automation Scripts

### 5.1 Assessment Generator Scripts

| Script | Output | Lines | Purpose |
|--------|--------|-------|---------|
| `generate_a824_1_data_transmission.py` | ISMS-IMP-A.8.24.1 | ~1,800 | Data transmission assessment workbook (16 sheets) |
| `generate_a824_2_data_storage.py` | ISMS-IMP-A.8.24.2 | ~1,500 | Data storage assessment workbook (11 sheets) |
| `generate_a824_3_authentication.py` | ISMS-IMP-A.8.24.3 | ~1,400 | Authentication assessment workbook (9 sheets) |
| `generate_a824_4_key_management.py` | ISMS-IMP-A.8.24.4 | ~1,300 | Key management assessment workbook (9 sheets) |
| `generate_a824_5_compliance_dashboard.py` | ISMS-IMP-A.8.24.5 | ~1,000 | Compliance summary dashboard (9 sheets) |

**Total Generator Code:** ~7,000 lines across 5 Python scripts

### 5.2 Validation Scripts (Quality Assurance)

| Script | Purpose | Lines |
|--------|---------|-------|
| `excel_sanity_check.py` | Generic workbook validator - auto-detects all 5 assessment types | ~800 |
| `excel_sanity_check_a824_1.py` | Specialized validator for Data Transmission (16-sheet structure) | ~500 |
| `excel_sanity_check_a824_2.py` | Specialized validator for Data Storage (11-sheet structure) | ~600 |
| `excel_sanity_check_a824_3.py` | Specialized validator for Authentication (9-sheet structure) | ~700 |
| `excel_sanity_check_a824_4.py` | Specialized validator for Key Management (9-sheet structure) | ~700 |
| `excel_sanity_check_a824_5.py` | Specialized validator for Compliance Dashboard (KPI validation) | ~800 |
| `style_object_checker.py` | Detects shared Border/Font/Fill objects (prevents Excel repair warnings) | ~600 |
| `style_object_patcher.py` | Auto-fixes shared style object issues in generator scripts | ~600 |

**Total Validation Code:** ~5,300 lines across 8 Python scripts

**Validation Benefits:**
- Prevents Excel "file is corrupted" errors
- Ensures workbook structure consistency
- Validates formula correctness
- Checks data validation dropdowns
- Verifies sheet naming conventions
- Detects shared style objects (openpyxl issue)

### 5.3 Supporting Utility Scripts

| Script | Purpose | Lines |
|--------|---------|-------|
| `normalize_assessment_files.py` | Normalizes filenames and creates audit manifest | ~700 |
| `isms_doc_reviewer.py` | Comprehensive document inventory and review checklist generator | ~800 |
| `isms_md_to_docx.py` | Converts ISMS markdown to Word format for stakeholders | ~300 |
| `markdown_to_docx.py` | Generic markdown to DOCX converter | ~250 |
| `md2docx.sh` | Bash wrapper for quick markdown conversion | ~50 |

**Total Utility Code:** ~2,100 lines across 5 scripts

### 5.4 Complete Automation Inventory

**Total Automation Framework:**
- **18 Python scripts** (~14,400 lines total)
- **1 Bash script** (~50 lines)
- **13 Policy documents** (markdown source)
- **8 Assessment specifications** (markdown source)
- **5 Generated Excel workbooks** (54 sheets, produced on-demand)

**Script Quality Standards:**
- PEP 8 compliant Python code
- Error handling and graceful failures
- Comprehensive commenting (explain WHY, not just WHAT)
- Modular functions for reusability
- Validation of inputs and outputs
- Version control integration (Git)

---

## 6. Key Policy Requirements

### 6.1 Use of Cryptographic Controls

**Mandatory Requirements:**
- Cryptographic controls **MUST** be used to protect information based on its classification and risk level
- Only approved algorithms and key lengths **SHALL** be used (see ISMS-POL-A.8.24-S5.A)
- Proprietary or deprecated cryptographic mechanisms **MUST NOT** be used
- Weak algorithms **MUST** be phased out within 90 days of discovery or public disclosure

**Approved Cryptographic Standards (Summary):**
- **Symmetric Encryption:** AES-256, AES-128 (where AES-256 not feasible), ChaCha20-Poly1305
- **Asymmetric Encryption:** RSA ≥3072 bits (RSA-4096 for long-term), ECDH P-256/P-384/P-521, Ed25519/Ed448
- **Hashing:** SHA-256, SHA-384, SHA-512, SHA-3 family
- **Password Hashing:** bcrypt (work factor ≥12), scrypt, Argon2id, PBKDF2-SHA256 (≥100,000 iterations)
- **Transport Security:** TLS 1.3 (preferred), TLS 1.2 (minimum acceptable)
- **Message Authentication:** HMAC-SHA256, HMAC-SHA384, HMAC-SHA512

**Prohibited Algorithms (MUST NOT be used):**
- **Encryption:** DES, 3DES, RC4, RC2, Blowfish
- **Hashing:** MD5, SHA-1, MD4, MD2
- **Asymmetric:** RSA <2048 bits, DSA <2048 bits
- **Protocols:** SSL v2/v3, TLS 1.0, TLS 1.1

**Deprecation Schedule** (detailed in ISMS-POL-A.8.24-S5.A):
- **TLS 1.2:** Acceptable until 2030, migrate to TLS 1.3 when feasible
- **RSA-2048:** Acceptable until 2030, migrate to RSA-3072+ or ECDH
- **SHA-256:** No current deprecation, monitor NIST guidance for post-quantum transition

### 6.2 Data Transmission

**Requirements:**
- Data transmitted over untrusted networks **MUST** be protected using strong encryption
- Minimum TLS 1.2 for all external communications (TLS 1.3 **SHOULD** be implemented where supported)
- Insecure protocols (HTTP, FTP, Telnet, unencrypted SMTP) **SHALL NOT** be used unless explicitly approved by exception
- VPN connections **MUST** use IKEv2 with AES-256-GCM or WireGuard
- Email containing confidential/restricted data **MUST** use S/MIME or PGP, or transmitted via TLS-protected webmail

**Assessment Coverage (13 Transmission Types):**
1. External HTTPS/TLS connections (public websites, APIs)
2. Internal HTTPS/TLS connections (intranet, internal services)
3. Email encryption (S/MIME, PGP, TLS transport)
4. Digital signatures (document signing, code signing)
5. File transfer protocols (SFTP, FTPS - not FTP)
6. VPN implementations (IKEv2, WireGuard, OpenVPN)
7. SSH remote access (key-based auth preferred)
8. RDP remote desktop (with NLA, TLS encryption)
9. API security (REST, GraphQL with OAuth 2.0, TLS)
10. Database connections (TLS/SSL for remote connections)
11. Wireless networks (WPA3, WPA2-Enterprise minimum)
12. Cloud transmission security (AWS, Azure, GCP encryption in transit)
13. IoT/embedded communications (TLS, DTLS for constrained devices)

### 6.3 Data Storage

**Requirements:**
- Confidential and restricted data **MUST** be encrypted at rest
- Encryption keys **MUST** be stored and protected separately from encrypted data
- Database encryption (TDE) **REQUIRED** for databases containing confidential/restricted data
- Full disk encryption (FDE) **REQUIRED** for all endpoints (laptops, desktops, mobile devices) and servers
- Backup encryption **REQUIRED** for all backup media (tapes, disks, cloud backups)
- Cloud storage encryption **REQUIRED** (server-side encryption minimum, client-side for restricted data)

**Assessment Coverage (7 Storage Types):**
1. Mobile devices (smartphones, tablets) - iOS FileVault, Android FBE
2. Laptops & workstations - BitLocker, FileVault, LUKS
3. Servers (physical, virtual) - BitLocker, dm-crypt, native hypervisor encryption
4. Databases (TDE, column-level) - SQL Server TDE, Oracle TDE, PostgreSQL pgcrypto, application-layer encryption
5. Cloud storage - S3 SSE-KMS, Azure SSE, GCP CMEK
6. Backups - Encrypted full/incremental/differential, keys offline
7. Removable media - USB drives, external disks (BitLocker To Go, VeraCrypt)

### 6.4 Authentication

**Requirements:**
- Cryptographic mechanisms **SHALL** be used to protect authentication credentials
- Passwords **MUST NOT** be stored in plaintext or reversibly encrypted
- Password hashing **MUST** use bcrypt (work factor ≥12), scrypt, Argon2id, or PBKDF2-SHA256 (≥100,000 iterations)
- Multi-factor authentication (MFA) **REQUIRED** for:
  - Privileged accounts (100% coverage)
  - Remote access (100% coverage - VPN, SSH, RDP, web admin panels)
  - Access to confidential/restricted data (≥90% coverage)
- Certificate-based authentication **SHOULD** be implemented for service accounts and API access

**Assessment Coverage (5 Authentication Methods):**
1. Password security (hashing algorithm, work factor, complexity, rotation, breach monitoring)
2. Multi-factor authentication (coverage %, methods: TOTP, FIDO2, SMS, push notification)
3. Certificate-based authentication (TLS client certs, smart cards, PKI infrastructure)
4. Service account security (API keys, OAuth client credentials, certificate auth, key rotation)
5. SSO & Federation (SAML 2.0, OAuth 2.0, OpenID Connect, assertion encryption)

### 6.5 Key Management

**Requirements:**
- Cryptographic keys **MUST** be generated using cryptographically secure random number generators (CSRNG)
- Production keys **MUST** be stored in Hardware Security Module (HSM), cloud Key Management Service (KMS), or Trusted Platform Module (TPM)
- Key rotation **REQUIRED** according to defined schedules:
  - Encryption keys: Annually minimum (more frequently for high-risk data)
  - Signing keys: Biennially minimum
  - Session keys: Hourly/daily (TLS session keys)
  - Certificates: Before expiration (30-day renewal window)
- Key backup and recovery procedures **MUST** be documented and tested quarterly
- Dual control and split knowledge **REQUIRED** for master keys and CA private keys

**Assessment Coverage (5 Key Lifecycle Stages):**
1. Key generation (CSRNG validation, algorithm parameters, entropy sources)
2. Key storage (HSM vs. KMS vs. TPM, access controls, audit logging)
3. Key rotation (automated schedules, rotation testing, key versioning)
4. Key backup & recovery (offline backups, recovery testing, RTO/RPO targets)
5. Certificate management (CA hierarchy, issuance process, renewal automation, revocation, OCSP/CRL)

### 6.6 Compliance Requirements

**Legal & Regulatory:**
- Cryptographic implementations **MUST** comply with applicable legal, regulatory, and contractual requirements
- Export control regulations **MUST** be considered for cross-border cryptographic deployments
- Data residency requirements **MUST** be met for regulated data (GDPR, FADP, country-specific laws)
- Lawful interception requirements **MUST** be documented where applicable (telecommunications, financial services)

**Exception Management:**
- Deviations from policy **MUST** be documented and approved via formal exception process (ISMS-POL-A.8.24-S5.B)
- Exceptions are time-limited (maximum 12 months, preferably 6 months)
- Exceptions **MUST** have risk assessment and compensating controls documented
- Exception renewals require re-justification and risk re-assessment
- CISO approval required for all cryptographic exceptions

---

## 7. Roles & Responsibilities

### 7.1 Executive Roles

| Role | Responsibilities |
|------|------------------|
| **CISO** | Overall accountability for cryptographic control program, policy approval, exception sign-off, budget approval for remediation, quarterly executive review |
| **CIO** | Technology infrastructure support, cryptographic solution procurement, integration oversight |
| **Legal/Compliance Officer** | Regulatory interpretation, export control compliance, lawful interception requirements |
| **Executive Management** | Strategic approval, risk acceptance for cryptographic gaps, budget allocation |

### 7.2 Operational Roles

| Role | Responsibilities |
|------|------------------|
| **Information Security Officer (ISO)** | Policy ownership and maintenance, enforcement and compliance monitoring, exception process management, coordination of quarterly assessments |
| **Security Engineering** | Assessment tool development and maintenance, generator script updates and testing, validation script maintenance, technical cryptographic guidance and standards updates, dashboard generation and linking |
| **IT Operations / DevOps** | Secure implementation of cryptographic controls, configuration management (TLS, FDE, TDE), key rotation execution, incident response participation, certificate renewal |
| **Database Administrators (DBAs)** | Database encryption (TDE) implementation, database connection encryption, encrypted backup verification |
| **System Owners** | Ensure cryptographic compliance within their systems, complete quarterly assessments with evidence, implement approved remediation plans, maintain system-specific crypto documentation |
| **Development Teams** | Implement cryptography in applications per approved standards, follow secure coding standards (OWASP), participate in security code reviews, address crypto-related security findings, use approved cryptographic libraries |

### 7.3 Supporting Roles

| Role | Responsibilities |
|------|------------------|
| **Internal Audit** | Compliance verification, audit evidence review, gap identification, remediation tracking |
| **Procurement** | Vendor cryptographic capability assessment, contractual cryptographic requirements, export control documentation |
| **Identity & Access Management (IAM)** | MFA deployment and management, certificate lifecycle for user authentication, SSO/Federation implementation |
| **Cloud Architects** | Cloud encryption design, KMS integration, cloud-specific cryptographic controls |

### 7.4 User Responsibilities

| Role | Responsibilities |
|------|------------------|
| **All Employees** | Adherence to cryptographic policy requirements, reporting of cryptographic weaknesses (weak passwords, expired certificates), participation in security awareness training, secure handling of credentials and certificates |
| **Privileged Users** | Enhanced scrutiny for cryptographic implementations, MFA compliance (100% requirement), secure key management for privileged access |

---

## 8. Assessment Methodology

### 8.1 System Engineering Approach

This framework employs a **system engineering methodology** rather than traditional checkbox compliance:

**Traditional Approach (Avoided):**
```
Auditor: "Do you encrypt data?"
Organization: "Yes, we have TLS enabled"
Auditor: [checks box]
Reality: Unknown TLS version, cipher suites, certificate expiry, or key management practices
```

**System Engineering Approach (Implemented):**
```
1. Run Python generator → produces standardized Excel workbook with 54 sheets
2. Technical SMEs complete assessment with evidence:
   - TLS scan results (SSL Labs, testssl.sh)
   - Certificate inventory with expiry dates
   - FDE status reports (BitLocker, FileVault)
   - Database TDE configuration screenshots
   - HSM/KMS access logs
3. Validation scripts check for errors/issues (missing evidence, incomplete responses)
4. Normalization creates audit-ready filenames (consistent format)
5. Dashboard auto-aggregates compliance metrics from 4 assessment workbooks
6. Quantitative results: "87.3% compliant, 23 gaps identified:
   - 5 systems using TLS 1.1 (deprecated)
   - 8 databases without TDE
   - 10 expired certificates"
```

**Benefits:**
- ✅ **Repeatable:** Scripts generate identical structure quarterly (no human error in template creation)
- ✅ **Quantitative:** Compliance % calculated mathematically (not subjective estimates)
- ✅ **Evidence-based:** Every "Yes" requires artifact (screenshot, config file, scan result)
- ✅ **Traceable:** Complete audit trail from finding to remediation (workbook → gap → plan → closure)
- ✅ **Transparent:** Dashboard shows real status, not aspirational goals
- ✅ **Maintainable:** Update assessments → dashboard auto-refreshes (Excel formulas link files)
- ✅ **Auditable:** Normalized files + manifest = complete audit trail
- ✅ **Quality-Assured:** Validation scripts prevent Excel repair warnings (openpyxl style object issue)

### 8.2 Vendor-Agnostic Design

**Policy Layer** (ISMS-POL-A.8.24): Defines *what* must be accomplished using generic cryptographic capability requirements. No specific vendors, products, or cloud providers mentioned.

**Implementation Layer** (ISMS-IMP-A.8.24): Defines *how* requirements are met in organizational context. Vendor-specific guidance provided as examples (BitLocker, FileVault, AWS KMS, Azure Key Vault), not mandates.

**Benefits:**
- Policy remains stable across technology changes (no policy update when migrating from one HSM to another)
- Organizations can use any cryptographic solutions that meet requirements
- Audit focuses on capability outcomes (Is data encrypted? Are keys rotated?) not vendor selection
- Implementation flexibility without policy revision
- Reduces vendor lock-in risk

**Example:**
- **Generic Requirement** (Policy): "Organizations SHALL encrypt databases containing confidential or restricted data using transparent data encryption (TDE) or equivalent database-level encryption"
- **Vendor-Specific Implementation** (Examples): SQL Server TDE, Oracle Advanced Security TDE, PostgreSQL pgcrypto, MySQL InnoDB encryption, MongoDB field-level encryption

### 8.3 Assessment Cycle

**Frequency:** Quarterly (or upon significant change to cryptographic landscape)

**Quarterly Cycle:**
1. **Week 1:** Generate assessment workbooks using Python scripts, distribute to IT Operations and Security Engineering
2. **Weeks 2-3:** Teams complete assessments:
   - IT Operations: Data Transmission (16 sheets) + Data Storage (11 sheets)
   - Security Engineering: Authentication (9 sheets) + Key Management (9 sheets)
   - Provide evidence: TLS scan results, certificate inventory, FDE reports, TDE configs, HSM logs
   - Document gaps: Weak ciphers, expired certificates, missing encryption, inadequate key rotation
3. **Week 4:** Security review:
   - Validate completeness (all yellow cells filled, evidence provided)
   - Run validation scripts (excel_sanity_check.py on all 4 workbooks)
   - Identify gaps and exceptions
   - Prioritize remediation (critical: expired certs, weak crypto; high: missing TDE; medium: old TLS versions)
4. **Week 5:** Dashboard generation:
   - Run compliance dashboard generator
   - Link normalized files (ensure formulas reference correct workbook paths)
   - Auto-populate KPIs (% compliant, gap count, risk scores)
   - Generate remediation roadmap (gaps → owners → timelines → budget)
5. **Week 6:** Executive review:
   - CISO reviews dashboard (traffic light view: red/yellow/green by domain)
   - Approve remediation plan (timeline, budget, resource allocation)
   - Sign off on assessment package (workbooks + dashboard + manifest)
   - Deliver to auditors (internal, external, PCI QSA, HIPAA assessor)

**Triggered Assessments:**
- Cryptographic algorithm deprecation (e.g., SHA-1 sunset, TLS 1.1 deprecation)
- Cryptographic incident (compromised key, certificate mis-issuance)
- Significant technology change (new cloud provider, HSM migration, certificate authority change)
- Audit finding (external audit identifies cryptographic gap)
- Regulatory change (new law requiring specific encryption, e.g., GDPR enforcement guidance)

### 8.4 Response Values

Assessment checklists use standardized response values:

| Value | Meaning | Action Required |
|-------|---------|-----------------|
| `Yes` | Fully implemented and documented | Maintain, provide evidence (scan results, configs, certs) |
| `No` | Not implemented | Remediate within 90 days or document exception with compensating controls |
| `Partial` | Partially implemented (e.g., some systems encrypted, others not) | Improvement plan required with completion timeline |
| `Planned` | Scheduled for implementation | Provide target date (must be <6 months), track as open item |
| `N/A` | Not applicable to environment | Justify why (e.g., "No mobile devices in environment", "Cloud provider handles") |

**Note:** "Maybe" or "Unknown" are not valid responses. Uncertainty must be resolved through testing (TLS scan, certificate inventory, encryption verification) or investigation before assessment completion.

---

## 9. Compliance & Audit

### 9.1 Mandatory Requirements

This policy framework demonstrates compliance with:

**Primary Standards:**
- ISO/IEC 27001:2022 Annex A Control 8.24
- ISO/IEC 27002:2022 Control 8.24 (detailed implementation guidance)
- ISO/IEC 27005:2022 - Information security risk management (cryptographic risk assessment)

**Regulatory Alignment:**
- **Swiss FADP (nDSG)**: Article 8 - Appropriate technical and organizational measures including encryption
- **EU GDPR**: Article 32 - Security of processing (encryption as appropriate technical measure)
- **PCI DSS v4.0** (where applicable): Requirements 3 (Protect stored account data), 4 (Protect cardholder data in transit)
- **HIPAA Security Rule** (where applicable): §164.312(a)(2)(iv) - Encryption and decryption (addressable)
- **SOX** (where applicable): Cryptographic protection of financial data integrity

**Technical Standards:**
- FIPS 140-2/140-3 - Cryptographic module security requirements (HSM validation)
- NIST SP 800-57 - Key management recommendations (parts 1-3)
- NIST SP 800-175B - Secure group communications
- NIST SP 800-38 Series - Block cipher modes of operation
- NIST SP 800-90A - Random number generation
- RFC 8446 - TLS 1.3 protocol specification
- RFC 5280 - X.509 certificate and CRL profile

### 9.2 Audit Evidence

Auditors should expect the following evidence:

**Policy Documentation:**
- Complete policy framework (ISMS-POL-A.8.24 and subsections S1-S5.D)
- Approval records (CISO, CIO, Legal/Compliance, Executive Management signatures)
- Distribution records (training acknowledgments, policy portal access logs, email confirmations)

**Implementation Evidence:**
- Completed assessment workbooks (5 Excel files, 54 sheets)
- Normalized filenames with audit manifest (consistency verification)
- Approved cryptographic standards list (ISMS-POL-A.8.24-S5.A with version history)
- Evidence artifacts:
  - **TLS configuration**: SSL Labs reports, testssl.sh scans, cipher suite lists, certificate chain verification
  - **Full disk encryption**: BitLocker status reports, FileVault verification, LUKS configuration, percentage of endpoints encrypted
  - **Database encryption**: TDE configuration screenshots, encryption verification queries, key storage architecture
  - **Key management**: HSM audit logs, KMS access logs, key rotation schedules, rotation execution logs
  - **MFA deployment**: Coverage reports (% users with MFA), MFA methods in use, privileged account MFA enforcement
  - **Certificate management**: Certificate inventory (issuer, expiration, SANs), renewal tracking, expiry alerts

**Operational Evidence:**
- Cryptographic incident records:
  - Compromised key incidents (detection, containment, key rotation, impact analysis)
  - Expired certificate incidents (systems affected, business impact, resolution time)
  - Weak cryptography detection (vulnerability scan findings, remediation)
- Key rotation logs:
  - Encryption key rotation (schedule, execution logs, verification)
  - Certificate renewals (old cert → new cert, overlap period, revocation of old cert)
  - Session key rotation (TLS session parameters, PFS verification)
- Exception requests with approvals:
  - Business justification (why deviation needed)
  - Risk assessment (quantitative risk score)
  - Compensating controls (alternative protections)
  - Time limit (6-12 months maximum)
  - CISO approval signature
- Certificate expiry tracking:
  - Monitoring dashboard (certs expiring in 30/60/90 days)
  - Automated renewal processes (ACME protocol, Let's Encrypt, internal CA automation)
  - Manual renewal procedures (for certificates requiring business validation)
- Vulnerability scan results:
  - Weak cipher detection (3DES, RC4, MD5, SHA-1)
  - Deprecated protocol detection (SSL v2/v3, TLS 1.0, TLS 1.1)
  - Certificate issues (expired, self-signed in production, weak signature algorithm)
  - Remediation tracking (finding → plan → verification scan)

**Effectiveness Evidence:**
- Key Performance Indicators (50+ metrics from dashboard):
  - **Data Transmission**: % systems using TLS 1.2+, % using TLS 1.3, weak cipher count, certificate expiry status
  - **Data Storage**: % endpoints with FDE, % databases with TDE, % backups encrypted, key separation verification
  - **Authentication**: % privileged accounts with MFA, % remote access with MFA, password hashing algorithm distribution
  - **Key Management**: % keys in HSM/KMS, key rotation compliance %, certificate renewal lead time, expired certificate count
  - **Overall**: Cryptographic maturity level (1-5), total gap count, critical gaps, high-priority gaps
- Compliance percentages per domain:
  - Data Transmission: X% compliant (target: 95%+)
  - Data Storage: X% compliant (target: 90%+)
  - Authentication: X% compliant (target: 95%+)
  - Key Management: X% compliant (target: 90%+)
- Gap remediation tracking:
  - Gap identification (assessment date, gap description, affected systems)
  - Remediation plan (owner, timeline, budget estimate)
  - Implementation (start date, completion date, verification method)
  - Closure evidence (post-implementation scan, configuration verification, sign-off)
- Penetration test results:
  - Crypto configuration testing (TLS downgrade attacks, weak cipher negotiation)
  - Certificate validation testing (trust chain, revocation checking)
  - Key management testing (key extraction attempts, privilege escalation)
  - Authentication bypass testing (password hash cracking resistance, MFA bypass attempts)

### 9.3 Key Performance Indicators (KPIs)

**Data Transmission KPIs (16 metrics):**

| KPI | Target | Measurement Method |
|-----|--------|-------------------|
| % External HTTPS using TLS 1.2+ | 100% | SSL Labs scan, testssl.sh |
| % External HTTPS using TLS 1.3 | ≥50% | SSL Labs scan |
| Systems with expired certificates | 0 | Certificate monitoring tool |
| Systems with weak ciphers (3DES, RC4) | 0 | Vulnerability scanner, Nessus |
| VPN connections using IKEv2/WireGuard | 100% | VPN server logs |
| Emails with S/MIME for confidential data | ≥80% | Email gateway logs |
| APIs using OAuth 2.0 + TLS | 100% | API gateway configuration |
| Database connections encrypted | 100% | Database audit logs |
| Wireless networks using WPA3/WPA2-Enterprise | 100% | Wireless controller config |
| IoT/embedded devices using TLS/DTLS | ≥90% | Network traffic analysis |
| Certificate renewal lead time (days before expiry) | ≥30 | Certificate management system |
| SSH using key-based auth (vs. password) | ≥90% | SSH server logs |
| RDP using NLA + TLS encryption | 100% | RDP server config |
| SFTP/FTPS usage (vs. unencrypted FTP) | 100% | File transfer logs |
| Cloud provider encryption in transit | 100% | Cloud config review |
| Digital signature usage for code/documents | ≥80% | Code signing logs, document signing logs |

**Data Storage KPIs (14 metrics):**

| KPI | Target | Measurement Method |
|-----|--------|-------------------|
| % Laptops with full disk encryption | 100% | Endpoint management tool (Intune, JAMF) |
| % Desktops with full disk encryption | 100% | Endpoint management tool |
| % Mobile devices with encryption | 100% | MDM (Mobile Device Management) |
| % Servers with full disk encryption | ≥95% | Server inventory + encryption audit |
| % Databases with TDE for confidential data | 100% | Database audit + data classification matrix |
| % Cloud storage with encryption at rest | 100% | Cloud config review (S3, Azure, GCP) |
| % Backups encrypted | 100% | Backup software reports |
| Encryption keys stored separately from data | 100% | Architecture review, penetration test |
| Keys in HSM/KMS/TPM (vs. file-based) | ≥90% | Key management audit |
| Removable media encryption enforcement | 100% | Group Policy, endpoint DLP logs |
| Database column-level encryption for PII | ≥80% | Database schema review |
| Application-layer encryption usage | ≥50% | Application architecture review |
| Cloud provider key management (BYOK/HYOK) | ≥30% | Cloud KMS configuration |
| Encryption performance impact | <10% | Performance benchmarks |

**Authentication KPIs (10 metrics):**

| KPI | Target | Measurement Method |
|-----|--------|-------------------|
| % Privileged accounts with MFA | 100% | IAM system reports |
| % Remote access connections with MFA | 100% | VPN logs, RDP logs, SSH logs |
| % Users accessing confidential data with MFA | ≥90% | Access control logs + data classification |
| Password hashing algorithm (bcrypt/scrypt/Argon2/PBKDF2) | 100% | Application code review, database schema |
| Passwords stored in plaintext/reversibly encrypted | 0 | Security code review, penetration test |
| % Systems using certificate-based auth for service accounts | ≥70% | Service account inventory |
| SSO/Federation using SAML 2.0/OAuth 2.0/OIDC | ≥80% | SSO platform configuration |
| MFA methods (FIDO2 > TOTP > Push > SMS) | FIDO2 ≥20% | MFA platform reports |
| Password breach monitoring (HaveIBeenPwned) | Enabled | IAM system configuration |
| Session timeout for high-privilege access | ≤15 min | Application configuration |

**Key Management KPIs (10 metrics):**

| KPI | Target | Measurement Method |
|-----|--------|-------------------|
| % Keys generated using CSRNG | 100% | Key generation audit logs |
| % Production keys in HSM/KMS | ≥90% | Key inventory + storage location |
| Encryption key rotation compliance | ≥95% | Key rotation schedule vs. execution logs |
| Certificate renewal compliance (before expiry) | 100% | Certificate management system |
| Key backup and recovery testing | Quarterly | Recovery test logs |
| Dual control for master keys | 100% | HSM access logs (m-of-n authorization) |
| Split knowledge for CA private keys | 100% | CA operational procedures |
| Key usage monitoring and alerting | Enabled | SIEM integration, HSM/KMS logs |
| Certificate revocation within SLA (<24h) | 100% | Certificate revocation logs vs. incident timestamp |
| OCSP/CRL availability | 99.9% | Certificate infrastructure monitoring |

**Overall Cryptographic Maturity KPIs:**

| KPI | Current | Target | Measurement Method |
|-----|---------|--------|-------------------|
| Cryptographic Maturity Level (1-5) | TBD | Level 4 | Assessment scoring matrix |
| Total gap count | TBD | <25 | Dashboard aggregation |
| Critical gaps (weak crypto, expired certs) | TBD | 0 | Gap prioritization |
| High-priority gaps | TBD | <10 | Gap prioritization |
| Gap remediation within SLA | TBD | ≥90% | Remediation tracking |
| Quarterly assessment completion | TBD | 100% | Assessment submission logs |
| Policy compliance attestation | TBD | 100% | Annual attestation sign-off |

### 9.4 Audit Approach

**Recommended Audit Methodology:**

1. **Document Review** (1-2 days):
   - Verify policy completeness (all sections S1-S5.D present)
   - Verify approvals (CISO signature, Legal review, Executive approval)
   - Verify distribution (training records, policy portal access)

2. **Technical Assessment** (3-5 days):
   - Review completed workbooks (5 Excel files, 54 sheets)
   - Validate evidence quality (screenshots, configs, scan results)
   - Verify evidence recency (scans <90 days old, configs current)

3. **Configuration Sampling** (2-3 days):
   - **TLS testing**: SSL Labs scans on 10 external services, testssl.sh on internal services
   - **Certificate review**: Verify 20 certificates (expiry, algorithm, trust chain)
   - **Database encryption**: Verify TDE on 5 databases with confidential data
   - **Endpoint encryption**: Sample 50 endpoints for FDE status (BitLocker, FileVault)
   - **Key management**: Review HSM/KMS access logs, verify separation from encrypted data

4. **Certificate Audit** (1 day):
   - Certificate inventory completeness (all systems accounted for)
   - Expiry tracking (no expired certs, all certs monitored)
   - Algorithm strength (RSA ≥3072, ECDSA P-256+, no SHA-1 signatures)
   - Trust chain validation (valid CA, no self-signed in production)
   - Renewal automation (ACME protocol, manual procedures documented)

5. **Vulnerability Assessment** (2 days):
   - Scan for cryptographic weaknesses:
     - Weak ciphers (3DES, RC4, MD5, SHA-1)
     - Deprecated protocols (SSL v2/v3, TLS 1.0, TLS 1.1)
     - Weak key lengths (RSA <2048, DH <2048)
     - Certificate issues (expired, self-signed, wildcard abuse)
   - Review vulnerability scan reports (Nessus, Qualys, OpenVAS)
   - Verify remediation of past findings (re-scan after fixes)

6. **Key Management Review** (1-2 days):
   - Key generation process (CSRNG verification, algorithm parameters)
   - Key storage (HSM vs. KMS vs. file-based, access controls)
   - Key rotation (schedule vs. actuals, automation vs. manual)
   - Key backup (offline backups exist, recovery tested)
   - Key destruction (secure deletion, cryptographic erasure)

7. **Interview Stakeholders** (1 day):
   - Security Engineering (assessment process, tool development)
   - IT Operations (implementation challenges, remediation plans)
   - System Owners (evidence provision, gap justification)
   - DBAs (database encryption, TDE configuration)
   - IAM team (MFA deployment, certificate management)

8. **Gap Analysis** (1 day):
   - Compare actual vs. required cryptographic controls
   - Categorize gaps (critical/high/medium/low)
   - Assess risk of gaps (likelihood × impact)
   - Review compensating controls for accepted gaps

9. **Remediation Review** (1 day):
   - Assess gap closure plans (realistic timelines, adequate budget)
   - Verify ownership assignment (named individuals, not generic roles)
   - Review prioritization logic (critical gaps first)
   - Check remediation tracking (open/in-progress/closed status)

**Sampling Strategy:**
- **Critical systems** (payment, authentication, database): 100% review
- **High-value data systems**: 50% sampling
- **Standard systems**: 25% sampling
- **Total minimum sample**: 30-50 systems across all domains

**Audit Frequency:**
- **Internal Audit**: Quarterly (cryptographic landscape changes rapidly - TLS versions, certificate expiries, algorithm deprecations)
- **External Audit**: As required by ISO 27001 certification body (annual minimum, surveillance audits semi-annual)
- **Regulatory Audit**: As required:
  - PCI DSS: Annual QSA audit + quarterly network scans
  - HIPAA: As required by covered entity/business associate assessments
  - SOX: Annual financial audit with IT general controls (ITGC) review
  - Financial regulators (FINMA, BaFin, etc.): Risk-based examination schedule
- **Self-Assessment**: Quarterly using assessment workbooks (continuous compliance monitoring)

**Audit Outputs:**
- Audit report with findings (non-conformities, observations, opportunities for improvement)
- Remediation plan with timelines (agreed corrective action plan)
- Follow-up audit schedule (verify closure of findings)

### 9.5 Reporting

**Monthly Reporting:**
- Certificate expiry status (certificates expiring in 30/60/90 days)
- Weak cryptography detection (vulnerability scan findings)
- Key rotation compliance (scheduled vs. actual)
- Incident summary (cryptographic incidents, resolution time)

**Quarterly Reporting:**
- Complete assessment dashboard (5 workbooks → consolidated KPIs)
- Compliance percentage by domain (transmission, storage, authentication, key management)
- Gap analysis with remediation roadmap (critical/high/medium/low gaps)
- Maturity assessment (Level 1-5, progress toward target)
- Exception register review (approved exceptions, upcoming renewals/expirations)

**Annual Reporting:**
- Cryptographic control effectiveness review (security incidents prevented, vulnerabilities detected/remediated)
- Policy review and updates (algorithm deprecations, new standards, regulatory changes)
- Budget and resource requirements (upcoming projects, remediation costs)
- Strategic recommendations (TLS 1.3 migration, HSM upgrade, quantum-readiness planning)

**Reporting Distribution:**
- **Monthly**: CISO, Information Security Officer, IT Operations Manager
- **Quarterly**: CISO, CIO, Executive Management, Board (summary)
- **Annual**: Board, Executive Management, Internal Audit, External Auditors

**Reporting Format:**
- Executive summary (1 page, traffic light indicators)
- Detailed metrics (dashboard spreadsheet, trend charts)
- Gap analysis (list of gaps with prioritization and timelines)
- Remediation tracking (Gantt chart, budget vs. actual)

---

## 10. Exception Management

### 10.1 Exception Process

**When Exceptions Are Permitted:**
- Technical limitations (legacy system incompatibility with modern crypto)
- Business justification (partner requires specific algorithm for compatibility)
- Cost-benefit analysis (remediation cost exceeds risk)
- Temporary workaround (during migration/transition period)

**Exception Request Requirements:**
- Formal request using ISMS-POL-A.8.24-S5.B template
- Business justification (why deviation needed, alternatives considered)
- Risk assessment (quantitative risk score: likelihood × impact)
- Compensating controls (alternative protections to reduce risk)
- Time limit (6 months preferred, 12 months maximum, no perpetual exceptions)
- System owner signature (accountability)
- CISO approval (risk acceptance authority)

**Exception Approval Workflow:**
1. System owner submits exception request to Information Security Officer
2. ISO reviews for completeness (all fields filled, risk assessment documented)
3. ISO schedules risk review meeting (system owner, ISO, Security Engineering, CISO)
4. Risk assessment presentation (current state, proposed exception, compensating controls)
5. CISO decision (approve, approve with modifications, reject)
6. If approved: Document in exception register, set expiry date, schedule review
7. If rejected: Document rationale, require remediation plan

**Exception Tracking:**
- Exception register (spreadsheet or GRC tool)
- Quarterly review of all active exceptions (ISO + CISO)
- 30-day warning before exception expiration (automated reminder)
- Renewal requires full re-justification (not automatic extension)

### 10.2 Compensating Controls

**Acceptable Compensating Controls:**

| Gap | Compensating Control Example |
|-----|------------------------------|
| Legacy system cannot use TLS 1.2 | Network segmentation (isolated VLAN), VPN tunnel for external access, IDS monitoring |
| Database cannot implement TDE | Application-layer encryption before database storage, strict database access controls, audit logging |
| No HSM for key storage | Cloud KMS with hardware-backed keys, keys stored encrypted (KEK wrapping), limited access via IAM |
| Cannot enforce MFA for specific application | IP whitelisting, geofencing, enhanced logging and monitoring, reduced session timeout |
| Certificate renewal requires manual process | Monitoring and alerting (60/30/7 day warnings), documented renewal procedure, backup personnel trained |

**Unacceptable Compensating Controls:**
- "We will be more careful" (not a technical control)
- "We monitor the logs" (unless specific automated alerting for anomalies)
- "Users are trained" (awareness does not replace technical control)

---

## 11. Non-Compliance & Enforcement

### 11.1 Violation Handling

**Severity Classification:**

| Severity | Description | Examples | Response Time |
|----------|-------------|----------|---------------|
| **Critical** | Active exploitation risk, data breach imminent | Compromised private key, expired TLS cert on production system, plaintext passwords stored | Immediate (within 24h) |
| **High** | Significant policy violation, regulatory non-compliance | Weak cipher suites enabled (3DES, RC4), no FDE on laptops, no MFA for privileged accounts | Within 7 days |
| **Medium** | Policy deviation without immediate risk | TLS 1.2 instead of TLS 1.3, key rotation overdue by <30 days, self-signed cert in non-production | Within 30 days |
| **Low** | Best practice violation, minor non-compliance | Documentation incomplete, test environment using weak crypto, advisory cipher suite present | Within 90 days |

**Violation Response Process:**
1. **Detection**: Quarterly assessment, vulnerability scan, penetration test, incident, audit finding
2. **Classification**: ISO assigns severity (critical/high/medium/low)
3. **Notification**: System owner notified within 24h (email + ticketing system)
4. **Investigation**: Root cause analysis (why violation occurred, how long existed)
5. **Remediation Plan**: System owner submits plan within:
   - Critical: 24 hours
   - High: 3 days
   - Medium: 7 days
   - Low: 14 days
6. **Implementation**: Remediation executed per plan timeline
7. **Verification**: ISO verifies remediation (re-scan, configuration review, evidence)
8. **Closure**: Documented in compliance tracking system

**Escalation:**
- Critical violations: Immediate escalation to CISO
- High violations: Escalation to CISO if remediation not completed within SLA
- Medium violations: Escalation to IT Director if repeated violations
- Low violations: Escalation to system owner's manager if ignored

### 11.2 Disciplinary Action

**For Employees:**
- First violation (unintentional): Remediation training, documented counseling
- Second violation (unintentional): Formal written warning, manager notification
- Third violation (unintentional): Performance improvement plan (PIP)
- Intentional circumvention: Immediate escalation to HR, potential termination

**For System Owners:**
- Non-response to violation notification: Escalation to manager, director
- Repeated violations on same system: Ownership reassignment
- Refusal to remediate: Executive escalation, budget freeze

**For Vendors/Third Parties:**
- Contractual violation: Formal notice, cure period (30-90 days)
- Repeated violations: Contract review, potential termination
- Critical violation: Immediate suspension of service, emergency remediation

---

## 12. Training & Awareness

**Required Training:**

| Audience | Training Topic | Frequency | Format | Duration |
|----------|---------------|-----------|--------|----------|
| **All Employees** | Cryptography awareness (why it matters, basics) | Annual | E-learning | 15 min |
| **Developers** | Secure coding - cryptography | Annual | Instructor-led | 2 hours |
| **System Administrators** | Cryptographic configuration (TLS, FDE, TDE) | Semi-annual | Hands-on lab | 4 hours |
| **Security Team** | Advanced cryptography (algorithms, attacks, trends) | Quarterly | Technical workshop | 2 hours |
| **DBAs** | Database encryption (TDE, column-level) | Annual | Vendor training | 4 hours |
| **IAM Team** | MFA deployment, certificate management | Semi-annual | Technical session | 2 hours |
| **Executive Management** | Cryptography strategy (quantum readiness, regulations) | Annual | Executive briefing | 1 hour |

**Training Content:**

**All Employees:**
- Why encryption matters (confidentiality, integrity, authenticity)
- Password security (strong passwords, password managers, no sharing)
- Phishing awareness (avoid credential compromise)
- Reporting (how to report suspicious crypto warnings, expired certificates)

**Developers:**
- Approved cryptographic libraries (don't roll your own crypto)
- Secure key management (never hardcode keys, use secret managers)
- OWASP Top 10 crypto failures (weak crypto, insecure randomness)
- Code review for cryptographic issues

**System Administrators:**
- TLS configuration (cipher suites, protocol versions, certificate installation)
- Full disk encryption (BitLocker, FileVault, LUKS deployment)
- Database encryption (TDE configuration, key management)
- Certificate lifecycle (CSR generation, installation, renewal, revocation)

**Security Team:**
- Cryptographic algorithm selection (symmetric, asymmetric, hashing)
- Attack vectors (downgrade, padding oracle, timing, side-channel)
- Post-quantum cryptography (threat timeline, migration planning)
- Regulatory requirements (GDPR Article 32, PCI DSS, HIPAA)

**Training Tracking:**
- Learning management system (LMS) records
- Completion certificates (retained 3 years)
- Quiz assessments (minimum 80% passing score)
- Refresher training for failures (re-take within 30 days)

---

## 13. Incident Response for Cryptographic Events

**Cryptographic Incident Types:**

| Incident Type | Severity | Response |
|---------------|----------|----------|
| **Compromised Private Key** | Critical | Immediate key rotation, certificate revocation, forensic analysis, notification |
| **Expired Certificate (Production)** | High | Emergency renewal, service disruption assessment, post-incident review |
| **Weak Cryptography Detected** | Medium-High | Risk assessment, remediation plan, compensating controls if needed |
| **Key Rotation Failure** | Medium | Manual rotation, root cause analysis, automation fix |
| **Certificate Mis-Issuance** | Medium-High | Revocation, re-issuance, CA trust review |
| **HSM/KMS Failure** | Critical | Failover to backup HSM, key recovery testing, vendor escalation |

**Incident Response Procedures (ISMS-POL-A.8.24-S5.C):**

**Compromised Key Response:**
1. **Containment** (within 1 hour):
   - Disable affected system/service
   - Revoke compromised certificate
   - Block key usage in HSM/KMS
2. **Assessment** (within 4 hours):
   - Determine scope (which keys, which systems, which data)
   - Identify root cause (phishing, malware, insider threat, vulnerability)
3. **Eradication** (within 24 hours):
   - Generate new key pair
   - Issue new certificate
   - Deploy new key to affected systems
4. **Recovery** (within 48 hours):
   - Re-enable services with new key
   - Verify functionality
   - Monitor for anomalies
5. **Post-Incident** (within 7 days):
   - Root cause analysis
   - Lessons learned
   - Process improvements
   - Notification (customers, regulators if required)

**Expired Certificate Response:**
1. **Emergency Renewal** (within 2 hours):
   - Generate CSR
   - Request emergency issuance from CA
   - Install renewed certificate
2. **Service Restoration** (within 4 hours):
   - Deploy renewed certificate
   - Verify TLS handshake
   - Monitor for connection errors
3. **Post-Incident Review**:
   - Why did expiry occur? (monitoring failure, process gap)
   - How to prevent recurrence? (automation, redundant alerting)
   - Update certificate inventory and monitoring

---

## 14. Policy Maintenance

### 14.1 Review Schedule

**Quarterly Review:**
- Approved cryptographic standards (S5.A) updated for:
  - Algorithm deprecations (NIST announcements, vendor advisories)
  - New algorithm recommendations (post-quantum algorithms, new TLS versions)
  - Regulatory changes (GDPR guidance, PCI DSS updates, NIST transitions)
- Assessment workbooks regenerated via scripts
- Validation suite executed on all workbooks
- Dashboard updated with latest data
- Remediation progress tracked
- KPIs reported to CISO

**Annual Review:**
- Complete policy framework (all sections S1-S5.D)
- Roles and responsibilities (organizational changes, new roles)
- Exception register (review all active exceptions, close expired)
- Training content (update for new threats, regulations, technologies)
- Incident response procedures (lessons learned integration)

**Triggered Reviews:**
- Major cryptographic incident (compromised CA, widespread key compromise)
- Algorithm deprecation (SHA-1 sunset, TLS 1.1 deprecation, 3DES prohibition)
- Regulatory change (new law requiring specific encryption, GDPR enforcement, PCI DSS v5)
- Audit finding (external audit identifies cryptographic gap requiring policy update)
- Technology change (cloud migration, HSM upgrade, new authentication system)

### 14.2 Version Control

**Major Version (X.0):**
- Structural changes (new sections added, reorganization)
- Scope modifications (new data types, new systems included)
- New regulatory requirements (GDPR, PCI DSS major version)
- Algorithm baseline change (minimum TLS version increase, minimum RSA key length increase)

**Minor Version (X.Y):**
- Content updates (clarifications, examples added)
- Algorithm additions (new approved algorithm without deprecating existing)
- Reference updates (new NIST publication, new RFC)
- Process improvements (assessment workflow refinement)

**Section Versioning:**
- S5.A (Approved Standards): Updated quarterly (most frequent changes)
- S2.X (Requirements): Updated annually or per regulatory changes
- S3, S4 (Roles, Governance): Updated per organizational changes
- S1 (Definitions): Updated rarely (only for fundamental crypto concept changes)

### 14.3 Change Management

**Standard Changes:**
1. Change proposal submitted to Information Security Officer
2. Impact assessment (affected systems, stakeholders, timelines, budget)
3. Stakeholder consultation (Security Engineering, IT Operations, Development, DBAs)
4. Draft revision prepared (tracked changes in markdown)
5. Review and approval:
   - Minor changes: ISO approval
   - Major changes: CISO + CIO + Legal approval
6. Communication plan executed:
   - Policy portal updated (with version history)
   - Training materials updated (e-learning, documentation)
   - Affected teams notified (email, team meetings, technical briefings)
7. Implementation tracking (30/60/90 day checkpoints)

**Emergency Changes:**
- Critical cryptographic vulnerability (POODLE, Heartbleed, ROBOT, Logjam)
- Immediate algorithm deprecation (CA compromise, algorithm break)
- Regulatory deadline (GDPR enforcement, PCI DSS mandate)
- Emergency approval process:
  - CISO approves change within 24 hours
  - Retrospective stakeholder review within 7 days
  - Documented justification for emergency process
  - Communication via security bulletin (immediate, all stakeholders)

**Script Updates:**
- Generator script changes tracked in Git (version control, commit history)
- Breaking changes require major version increment
- Backward compatibility maintained where possible (old workbooks still validate)
- Testing before production deployment (generate sample workbooks, run validation)

**Ad-hoc Updates:**
- Triggered by incidents, audit findings, or regulatory changes
- Emergency policy amendments possible with CISO approval
- Script hotfixes for critical bugs (validation failures, Excel corruption)
- Communication via security bulletins

### 14.4 Communication

**Policy Updates Communicated Via:**
- Policy portal (central repository, version-controlled)
- Email notifications:
  - **All employees**: Major policy changes (algorithm deprecations, new requirements)
  - **Technical staff**: All changes (algorithm updates, process changes, script updates)
  - **Management**: Strategic changes (regulatory requirements, budget impacts)
- Training updates:
  - E-learning content updated (within 30 days of policy change)
  - Instructor-led training slides updated (for next session)
  - Quick reference guides updated (S5.D)
- Technical bulletins:
  - Algorithm deprecation notices (90-day warning, 30-day reminder)
  - Certificate expiry alerts (60/30/7 day warnings)
  - Vulnerability alerts (critical crypto vulnerabilities, patches available)
- Quarterly CISO briefings to Executive Management (strategic updates, maturity progress)

---

## 15. Integration with ISMS

### 15.1 Related Controls

This cryptography framework integrates with multiple ISO 27001 controls:

| Control | Integration Point |
|---------|-------------------|
| **A.5.1** | Policies - Cryptography policy is part of ISMS policy suite |
| **A.5.9** | Inventory - Cryptographic assets (HSMs, certificates) tracked in asset inventory |
| **A.5.12** | Classification - Data classification drives encryption requirements (Confidential/Restricted → encrypt) |
| **A.5.23** | Cloud Services - Cryptographic requirements for cloud providers (encryption at rest/transit, key management) |
| **A.5.30** | Business Continuity - Key recovery in BC/DR plans, HSM failover, certificate backup |
| **A.8.10** | Information Deletion - Cryptographic erasure methods (key destruction, secure deletion) |
| **A.8.11** | Data Masking - Cryptographic techniques for data protection (tokenization, format-preserving encryption) |
| **A.8.12** | Data Leakage Prevention - Encryption complements DLP (encrypted egress channels require inspection architecture) |
| **A.8.16** | Monitoring - Crypto event logging and monitoring (key usage, certificate expiry, weak crypto detection) |
| **A.8.23** | Web Filtering - HTTPS inspection considerations (SSL/TLS decryption at proxy, privacy implications) |

### 15.2 Bidirectional Data Flows

**Cryptography → Other Controls:**
- Encrypted data → Data Classification (A.5.12): Encryption verifies proper handling of classified data
- Certificate inventory → Asset Management (A.5.9): Certificates tracked as organizational assets
- Key compromise incident → Incident Management (A.5.24-28): Cryptographic incidents trigger response process
- HSM failure → Business Continuity (A.5.30): Failover to backup HSM, key recovery from escrow
- Cloud encryption → Cloud Services (A.5.23): Verify cloud provider encryption capabilities

**Other Controls → Cryptography:**
- Data Classification (A.5.12) → Encryption requirements: Confidential/Restricted data must be encrypted
- Incident lessons learned (A.5.24-28) → Algorithm updates: Compromise drives deprecation
- Business Continuity (A.5.30) → Key backup: RTO/RPO requirements drive key recovery procedures
- Access Control (A.5.15) → Authentication: Strong authentication requires cryptographic mechanisms (MFA, certificates)
- Supplier Management (A.5.19-23) → Cloud crypto: Vendor encryption capabilities assessed during procurement

### 15.3 Risk Management Integration

**Risk Treatment:**
- Cryptographic controls as risk mitigation (encryption protects against unauthorized disclosure)
- Residual risks from crypto exceptions tracked in organizational risk register
- Risk assessment feeds remediation prioritization (critical risks → immediate remediation)

**Risk Register:**
- Cryptographic risks documented in compliance dashboard (Domain 5)
- Risk categories:
  - **Algorithm risk**: Weak/deprecated algorithms in use (3DES, SHA-1)
  - **Key management risk**: Keys not in HSM, keys not rotated, keys stored with data
  - **Certificate risk**: Expired certificates, weak signatures, lack of monitoring
  - **Implementation risk**: Misconfigured TLS, weak cipher suites, no PFS
- Risk scores drive remediation urgency and budget allocation
- Exception risks monitored quarterly and reported to CISO

---

## 16. Continuous Improvement

### 16.1 Improvement Triggers

**Framework improvements driven by:**
- **Audit findings and recommendations** (external auditor identifies gaps, process inefficiencies)
- **Security incidents and lessons learned** (compromised key reveals process gap, expired cert reveals monitoring failure)
- **New regulatory requirements** (GDPR Article 32 interpretation, PCI DSS v5 requirements)
- **Technology evolution** (new algorithms: post-quantum crypto, TLS 1.4; deprecations: TLS 1.2 sunset timeline)
- **Stakeholder feedback** (assessment too complex, evidence requirements unclear, script errors)
- **KPI trends showing gaps** (certificate expiry rate increasing, weak crypto count not decreasing)
- **Excel repair warnings** (triggers script enhancement, validation rule addition)
- **Validation failures** (triggers quality improvements, generator script fixes)

### 16.2 Improvement Process

1. **Identify improvement opportunity**:
   - Incident (compromised key, certificate outage)
   - Audit finding (control gap, documentation insufficient)
   - Feedback (stakeholder complaint, usability issue)
   - Validation failure (Excel corruption, formula error)

2. **Document current state vs. desired state**:
   - What is not working? (root cause analysis)
   - What should work? (target state definition)
   - Gap analysis (current → target)

3. **Assess impact and feasibility**:
   - Who is affected? (stakeholders, systems)
   - What is the effort? (development time, testing time)
   - What is the cost? (budget, resources)
   - What is the benefit? (risk reduction, efficiency gain)

4. **Propose changes**:
   - Policy updates (algorithm deprecation, new requirement)
   - Process improvements (assessment workflow optimization)
   - Script enhancements (new validation rules, additional sheets)
   - Validation improvements (additional checks, better error messages)

5. **Review and approve**:
   - Technical review (Security Engineering validates feasibility)
   - Stakeholder review (affected teams provide feedback)
   - Management approval:
     - Minor improvements: ISO approval
     - Major changes: CISO approval

6. **Implement changes**:
   - Update scripts (generator or validation)
   - Re-test thoroughly (generate sample workbooks, run full validation suite)
   - Re-generate workbooks (provide updated templates to stakeholders)
   - Update documentation (markdown specs, user guides)

7. **Measure effectiveness**:
   - KPIs (have metrics improved?)
   - Metrics (validation pass rate, assessment completion time)
   - Validation results (fewer Excel repair warnings, fewer errors)
   - Stakeholder feedback (surveys, interviews)

8. **Standardize**:
   - Update documentation (policy, procedures, training)
   - Commit to version control (Git with meaningful commit messages)
   - Communicate changes (policy portal, email, training updates)
   - Archive old versions (maintain version history for audit trail)

### 16.3 Maturity Assessment

**Cryptographic Maturity Levels:**

**Level 1 - Initial (Ad-hoc)**:
- Cryptography used inconsistently
- No standards or guidelines
- Manual key management
- No monitoring or compliance tracking
- Characteristics:
  - Some systems use encryption, others don't
  - Algorithms chosen arbitrarily
  - Passwords stored in plaintext or MD5
  - No certificate lifecycle management
  - Keys stored in config files

**Level 2 - Managed (Documented)**:
- Policy exists
- Some standards defined
- Partial compliance
- Basic monitoring
- Characteristics:
  - Approved algorithm list exists
  - FDE deployed on some endpoints
  - TLS enabled but version inconsistent
  - Certificate expiry monitoring (manual spreadsheet)
  - Key rotation performed manually

**Level 3 - Defined (Standardized)**:
- Comprehensive policy framework
- Standardized processes
- Good compliance (70-85%)
- Regular assessments
- Characteristics:
  - Clear requirements for all data types
  - FDE mandatory for all endpoints (enforced)
  - TLS 1.2+ standard across organization
  - Certificate monitoring automated
  - Key rotation scheduled and tracked

**Level 4 - Quantitatively Managed (Metrics-Driven)** ← **CURRENT TARGET**:
- Automated assessment generation
- Quantitative compliance metrics (50+ KPIs)
- High compliance (85-95%)
- Quality validation suite
- Self-service tooling
- Characteristics:
  - Python-generated Excel assessments (54 sheets)
  - Dashboard auto-aggregates KPIs
  - Validation scripts prevent errors
  - Normalized files for audit readiness
  - Stakeholder self-service (generate own workbooks)

**Achievement Evidence for Level 4** ✅:
- ✅ Automated assessment generation (5 Python scripts, ~7,000 lines)
- ✅ Quantitative compliance metrics (50+ KPIs auto-calculated)
- ✅ Quality validation suite (8 validation scripts, ~5,300 lines)
- ✅ Self-service tooling for stakeholders (documented scripts, repeatable process)
- ✅ Normalized audit trail (normalize_assessment_files.py, manifest generation)

**Level 5 - Optimizing (Continuous Improvement)** ← **FUTURE GOAL**:
- Auto-remediation for common issues
- Predictive analytics for compliance drift
- Self-updating generator scripts
- AI-assisted gap analysis
- Full automation end-to-end
- Characteristics:
  - Weak crypto detected → auto-remediation ticket created → assigned → tracked
  - Certificate expiring → auto-renewal triggered (ACME protocol) → verified
  - Compliance trending → predictive alerts ("you will have 15 TLS 1.2 systems in 90 days")
  - Generator scripts self-update from NIST publications
  - AI-powered gap analysis ("these 5 gaps are related to lack of HSM budget")

**Path to Level 5** (Target: Q2 2025):
- Implement ACME protocol for certificate automation
- Develop auto-remediation workflows (Ansible, Terraform)
- Build predictive analytics dashboard (machine learning on KPI trends)
- Create self-updating algorithm database (NIST API integration)
- Deploy AI-assisted risk assessment (natural language processing on gap descriptions)

---

## 17. Reference Documents

### 17.1 Internal Documents

**Policy Layer:**
- ISMS-POL-A.8.24 (this document) + Sections S1 through S5.D

**Assessment Layer:**
- ISMS-IMP-A.8.24.1 – Data Transmission Assessment (Markdown + Excel)
- ISMS-IMP-A.8.24.2 – Data Storage Assessment (Markdown + Excel)
- ISMS-IMP-A.8.24.3 – Authentication Assessment (Markdown + Excel)
- ISMS-IMP-A.8.24.4 – Key Management Assessment (Markdown + Excel)
- ISMS-IMP-A.8.24.5 – Compliance Summary Dashboard (Markdown + Excel)
- ISMS-IMP-A.8.24 - Use of Cryptography Assessment Suite (Master overview)
- ISMS-IMP-A.8.24.1 - Excel Template Specification (Reference template structure)

**Automation Layer:**
- Generator Scripts (5 Python files, ~7,000 lines total)
- Validation Scripts (8 Python files, ~5,300 lines total)
- Utility Scripts (5 Python/Bash files, ~2,100 lines total)

**Supporting ISMS Documents:**
- ISMS Information Security Policy (parent policy)
- ISMS Risk Assessment Methodology
- ISMS Asset Management Policy
- ISMS Change Management Procedure
- ISMS-POL-A.5.9 - Inventory of Information and Other Associated Assets
- ISMS-POL-A.5.12 - Classification of Information
- ISMS-POL-A.5.23 - Cloud Services Security
- ISMS-POL-A.8.10 - Information Deletion
- ISMS-POL-A.8.11 - Data Masking
- ISMS-POL-A.8.12 - Data Leakage Prevention
- ISMS-POL-A.8.16 - Monitoring Activities
- ISMS Incident Management Procedure

### 17.2 External Standards & Regulations

**International Standards:**
- ISO/IEC 27001:2022 – Information Security Management Systems
- ISO/IEC 27002:2022 – Information Security Controls (Control 8.24 detailed guidance)
- ISO/IEC 27005:2022 – Information Security Risk Management

**Cryptographic Standards:**
- **FIPS 140-2/140-3** – Security Requirements for Cryptographic Modules (HSM validation)
- **NIST SP 800-38 Series** – Recommendation for Block Cipher Modes of Operation
- **NIST SP 800-52 Rev. 2** – Guidelines for the Selection, Configuration, and Use of TLS
- **NIST SP 800-57 Part 1 Rev. 5** – Recommendation for Key Management: General
- **NIST SP 800-57 Part 2 Rev. 1** – Recommendation for Key Management: Best Practices
- **NIST SP 800-57 Part 3 Rev. 1** – Recommendation for Key Management: Application-Specific
- **NIST SP 800-90A Rev. 1** – Recommendation for Random Number Generation Using Deterministic RBGs
- **NIST SP 800-131A Rev. 2** – Transitioning the Use of Cryptographic Algorithms and Key Lengths
- **NIST SP 800-175B Rev. 1** – Guideline for Using Cryptographic Standards: Cryptographic Mechanisms
- **RFC 8446** – The Transport Layer Security (TLS) Protocol Version 1.3
- **RFC 5280** – Internet X.509 Public Key Infrastructure Certificate and CRL Profile
- **RFC 5869** – HMAC-based Extract-and-Expand Key Derivation Function (HKDF)
- **RFC 7748** – Elliptic Curves for Security (Curve25519, Curve448)
- **RFC 8032** – Edwards-Curve Digital Signature Algorithm (EdDSA)

**Regional Cryptographic Guidance:**
- **BSI TR-02102** – Cryptographic Mechanisms: Recommendations and Key Lengths (Germany - Bundesamt für Sicherheit in der Informationstechnik)
- **ANSSI RGS** – Référentiel Général de Sécurité (France - Agence nationale de la sécurité des systèmes d'information)
- **ENISA** – Algorithms, Key Size and Protocols Report (European Union Agency for Cybersecurity)
- **NCSC** – Cryptography Guidance (UK National Cyber Security Centre)

**Industry Guidelines:**
- **OWASP Cryptographic Storage Cheat Sheet**
- **OWASP Transport Layer Protection Cheat Sheet**
- **OWASP Password Storage Cheat Sheet**
- **OWASP Key Management Cheat Sheet**
- **Mozilla SSL Configuration Generator** (TLS best practices)
- **Qualys SSL Labs Best Practices**

**Regulatory:**
- **Swiss FADP (nDSG)** – Federal Act on Data Protection
- **EU GDPR** – General Data Protection Regulation (Article 32 - Security of processing)
- **PCI DSS v4.0** – Payment Card Industry Data Security Standard (Requirements 3 & 4)
- **HIPAA Security Rule** – Health Insurance Portability and Accountability Act (§164.312(a)(2)(iv))
- **SOX** – Sarbanes-Oxley Act (financial data integrity)
- **DORA** – Digital Operational Resilience Act (EU Regulation 2022/2554)
- **NIS2** – Network and Information Security Directive 2 (EU Directive 2022/2555)
- **eIDAS** – Electronic Identification and Trust Services (EU Regulation 910/2014 - qualified signatures, seals, certificates)

**Post-Quantum Cryptography:**
- **NIST PQC Project** – Post-Quantum Cryptography Standardization (CRYSTALS-Kyber, CRYSTALS-Dilithium, FALCON, SPHINCS+)
- **NSA CNSA 2.0** – Commercial National Security Algorithm Suite 2.0 (quantum-resistant timeline)
- **BSI** – Migration to Post-Quantum Cryptography
- **ANSSI** – Post-Quantum Cryptography Position Paper

**Export Control:**
- **Wassenaar Arrangement** – Export Controls for Conventional Arms and Dual-Use Goods and Technologies
- **EU Dual-Use Regulation** (EU 2021/821) – Export controls on encryption
- **US EAR** – Export Administration Regulations (ECCN 5A002/5D002)
- **US ITAR** – International Traffic in Arms Regulations

---

## 18. Glossary

| Term | Definition |
|------|------------|
| **AES** | Advanced Encryption Standard, symmetric block cipher (FIPS 197), key sizes: 128, 192, 256 bits |
| **Argon2** | Password hashing function, winner of Password Hashing Competition 2015, variants: Argon2i, Argon2d, Argon2id |
| **Asymmetric Cryptography** | Public-key cryptography using key pairs (public + private), e.g., RSA, ECDH, Ed25519 |
| **bcrypt** | Password hashing function based on Blowfish cipher, adaptive work factor (cost parameter) |
| **Certificate Authority (CA)** | Trusted entity that issues digital certificates, signs certificates with private key |
| **Certificate Revocation List (CRL)** | Published list of revoked certificates, checked during certificate validation |
| **ChaCha20-Poly1305** | Authenticated encryption algorithm, alternative to AES-GCM, widely used in TLS and VPNs |
| **Cipher Suite** | Set of algorithms for key exchange, authentication, encryption, and MAC (e.g., TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) |
| **Cryptographic Hash Function** | One-way function producing fixed-size output (digest) from arbitrary input, e.g., SHA-256 |
| **Cryptoperiod** | Time span during which a cryptographic key is authorized for use, after which key rotation required |
| **CSRNG** | Cryptographically Secure Random Number Generator, provides unpredictable random values for key generation |
| **Digital Signature** | Cryptographic technique for verifying authenticity and integrity using asymmetric cryptography |
| **Dual Control** | Security principle requiring two authorized individuals to perform sensitive operation (e.g., HSM master key access) |
| **ECDH** | Elliptic Curve Diffie-Hellman, key exchange protocol using elliptic curve cryptography |
| **ECDSA** | Elliptic Curve Digital Signature Algorithm, signature scheme using elliptic curves (e.g., P-256, P-384) |
| **Ed25519** | Edwards-curve Digital Signature Algorithm using Curve25519, fast and secure signature scheme |
| **Entropy** | Measure of randomness/unpredictability in cryptographic key generation, higher entropy = more secure |
| **Ephemeral Key** | Temporary key used for single session, discarded after use (provides Perfect Forward Secrecy) |
| **FDE** | Full Disk Encryption, encrypts entire disk volume (e.g., BitLocker, FileVault, LUKS) |
| **FIPS 140-2/140-3** | Federal Information Processing Standard for cryptographic modules, defines 4 security levels |
| **HSM** | Hardware Security Module, physical device for secure key generation, storage, and cryptographic operations |
| **HMAC** | Hash-based Message Authentication Code, provides data integrity and authenticity |
| **Initialization Vector (IV)** | Random value used with encryption algorithm to ensure identical plaintexts produce different ciphertexts |
| **IKEv2** | Internet Key Exchange version 2, protocol for establishing VPN security associations |
| **KEK** | Key Encryption Key, key used to encrypt other keys (key wrapping) |
| **Key Derivation Function (KDF)** | Function deriving cryptographic keys from passwords or master keys (e.g., PBKDF2, HKDF) |
| **Key Escrow** | Secure storage of cryptographic keys with trusted third party for recovery purposes |
| **Key Pair** | Public key + private key in asymmetric cryptography, mathematically related but computationally infeasible to derive one from other |
| **Key Rotation** | Process of replacing cryptographic keys with new keys according to schedule or after compromise |
| **Key Wrapping** | Encrypting cryptographic key with another key (KEK) for secure storage or transmission |
| **KMS** | Key Management Service, typically cloud-based key management (e.g., AWS KMS, Azure Key Vault, GCP Cloud KMS) |
| **MAC** | Message Authentication Code, cryptographic checksum for integrity and authenticity (e.g., HMAC) |
| **Master Key** | Top-level key in key hierarchy, used to encrypt other keys (KEKs, DEKs) |
| **OCSP** | Online Certificate Status Protocol, real-time certificate revocation checking (alternative to CRL) |
| **openpyxl** | Python library for reading/writing Excel 2010 xlsx/xlsm files, used in generator scripts |
| **Padding** | Data added to plaintext to reach required block size for block ciphers (e.g., PKCS#7, OAEP) |
| **PBKDF2** | Password-Based Key Derivation Function 2, derives key from password with salt and iterations |
| **Perfect Forward Secrecy (PFS)** | Property ensuring session keys not compromised if long-term key compromised (ephemeral key exchange) |
| **PKCS** | Public-Key Cryptography Standards, RSA Security standards (PKCS#1 RSA, PKCS#7 padding, PKCS#12 certificates) |
| **Post-Quantum Cryptography (PQC)** | Cryptographic algorithms resistant to quantum computer attacks (e.g., lattice-based, hash-based, CRYSTALS-Kyber) |
| **Public Key Infrastructure (PKI)** | Framework for managing digital certificates, CAs, certificate lifecycle, and trust chains |
| **Quantum Computing** | Computing using quantum mechanics (qubits, superposition), threatens current public-key cryptography |
| **Rainbow Table** | Precomputed hash table for reversing cryptographic hash functions (defeated by salting) |
| **RSA** | Rivest–Shamir–Adleman, asymmetric encryption and signature algorithm, key sizes: 2048, 3072, 4096 bits |
| **Salt** | Random value added to password before hashing to prevent rainbow table attacks and ensure unique hashes |
| **scrypt** | Password-based key derivation function, memory-hard to resist hardware attacks (GPUs, ASICs) |
| **Session Key** | Temporary symmetric key used for single communication session, typically rotated hourly/daily |
| **SHA** | Secure Hash Algorithm family, variants: SHA-1 (deprecated), SHA-256, SHA-384, SHA-512, SHA-3 |
| **Split Knowledge** | Security principle where no single person has access to complete key (key split into shares, m-of-n) |
| **S/MIME** | Secure/Multipurpose Internet Mail Extensions, standard for email encryption and digital signatures |
| **Symmetric Cryptography** | Encryption using same key for encryption and decryption, e.g., AES, ChaCha20 |
| **TDE** | Transparent Data Encryption, database-level encryption (e.g., SQL Server TDE, Oracle Advanced Security TDE) |
| **TLS** | Transport Layer Security, cryptographic protocol for secure communications, versions: 1.2 (minimum), 1.3 (preferred) |
| **TPM** | Trusted Platform Module, hardware-based security chip for key storage and cryptographic operations |
| **WireGuard** | Modern VPN protocol using state-of-the-art cryptography (ChaCha20, Curve25519), simpler than IPsec/IKEv2 |
| **X.509** | ITU-T standard for public key certificates, defines certificate format and fields (issuer, subject, validity, public key) |

---

**Additional Acronyms:**

| Acronym | Full Term |
|---------|-----------|
| **CA** | Certificate Authority |
| **CRL** | Certificate Revocation List |
| **CSR** | Certificate Signing Request |
| **DEK** | Data Encryption Key |
| **DH** | Diffie-Hellman (key exchange) |
| **DSA** | Digital Signature Algorithm |
| **ECC** | Elliptic Curve Cryptography |
| **GCM** | Galois/Counter Mode (authenticated encryption) |
| **HKDF** | HMAC-based Key Derivation Function |
| **IV** | Initialization Vector |
| **KDF** | Key Derivation Function |
| **MAC** | Message Authentication Code |
| **OCSP** | Online Certificate Status Protocol |
| **OAEP** | Optimal Asymmetric Encryption Padding |
| **PFS** | Perfect Forward Secrecy |
| **PKCS** | Public-Key Cryptography Standards |
| **PKI** | Public Key Infrastructure |
| **PQC** | Post-Quantum Cryptography |
| **RNG** | Random Number Generator |
| **SAN** | Subject Alternative Name (certificate field) |
| **TDE** | Transparent Data Encryption |

---

**Deprecated/Prohibited Terms (for reference only):**

| Term | Status | Reason |
|------|--------|--------|
| **DES** | PROHIBITED | 56-bit key length, broken by brute force (1998) |
| **3DES** | PROHIBITED | Deprecated 2023, disallowed 2024, 64-bit block size vulnerability |
| **MD5** | PROHIBITED | Collision attacks demonstrated (2004), broken for security use |
| **RC4** | PROHIBITED | Stream cipher with biases, broken in TLS (2015) |
| **SHA-1** | PROHIBITED | Collision attacks demonstrated (2017), deprecated for certificates |
| **SSL v2/v3** | PROHIBITED | Multiple vulnerabilities (POODLE, BEAST, etc.) |
| **TLS 1.0** | PROHIBITED | Deprecated 2020, disallowed 2021 (PCI DSS requirement) |
| **TLS 1.1** | PROHIBITED | Deprecated 2020, disallowed 2021 |
| **RSA-1024** | PROHIBITED | Key length insufficient, factorization feasible with modern computing |

---

**END OF GLOSSARY**

## Appendix A: Philosophy & Methodology

### A.1 Evidence Over Cryptographic Theater

> "The first principle is that you must not fool yourself—and you are the easiest person to fool."  
*— Richard Feynman

This framework prevents **cargo cult cryptography** — the practice of:
- Enabling encryption "because policy says so" without understanding protection level
- Assuming "we use HTTPS" means "our data is secure"
- Treating encryption as checkbox compliance rather than risk-based control
- Ignoring key management ("keys stored next to encrypted data")
- Never rotating keys ("if it's encrypted, it's protected forever")

**The assessment workbooks force specificity and evidence:**

- **What** algorithms are used? (AES-256? RSA-3072? Or deprecated DES/MD5?)
- **Where** is encryption deployed? (TLS? Database TDE? Endpoint FDE? Backups?)
- **How** are keys managed? (HSM? KMS? Plaintext file on server? 🚨)
- **When** are keys rotated? (Annual schedule? Never? "We lost the keys"? 🚨)
- **Proof** of effectiveness? (TLS scan results, encryption verification, key rotation logs)

If these questions cannot be answered with quantitative evidence, the organization does not have cryptographic controls — it has cryptographic **theater**.

### A.2 Cryptography Is Not Optional for Confidential Data

> "There are two types of encryption: encryption that will stop your kid sister from reading your files, and encryption that will stop major governments from reading your files."  
> — Bruce Schneier

**Encryption Maturity Levels:**

**Level 0 - No Encryption** (Unacceptable for Confidential data):
- HTTP instead of HTTPS
- Unencrypted databases
- Plaintext backups
- No full disk encryption

**Level 1 - Checkbox Encryption** (Insufficient):
- HTTPS enabled (but TLS 1.0 with weak ciphers)
- Database encryption (but keys stored in same database)
- Full disk encryption (but BitLocker with TPM-only, no PIN)
- Backups encrypted (but encryption key on same backup media)

**Level 2 - Baseline Encryption** (Minimum acceptable):
- TLS 1.2+ with strong ciphers
- Database TDE with external key management
- Full disk encryption with pre-boot authentication
- Backup encryption with offline key storage
- Annual key rotation

**Level 3 - Defense-in-Depth** (Target for Restricted data):
- TLS 1.3 with PFS
- Column-level encryption for sensitive fields
- Application-layer encryption before database
- HSM for key management
- Quarterly key rotation
- Key usage auditing

**Level 4 - Zero Trust Cryptography** (High-security environments):
- End-to-end encryption (no plaintext at rest anywhere)
- HSM with dual control and split knowledge
- Continuous key rotation (automated)
- Crypto agility (algorithm substitution ready)
- Post-quantum cryptography preparation

**This policy targets Level 2 (Baseline) minimum, Level 3 (Defense-in-Depth) for Restricted data.**

### A.3 Key Management Is Harder Than Encryption

> "Most cryptographic systems fail not because the encryption is broken, but because the keys are mismanaged."

**Key Management Failure Patterns:**

1. **Keys Stored with Encrypted Data**:
   - Database TDE enabled → encryption key in database config file
   - Encrypted backup → encryption key on backup media
   - **Result**: Encryption provides zero protection

2. **No Key Rotation**:
   - Keys generated 5 years ago, never rotated
   - Same TLS certificate since 2015
   - **Result**: Prolonged cryptoperiod increases compromise impact

3. **Lost Keys (No Recovery)**:
   - Encryption enabled, key not backed up
   - Employee leaves, takes laptop password
   - **Result**: Data loss, business disruption

4. **Too Many Key Copies (Over-Recovery)**:
   - Encryption keys on 15 USB drives "for backup"
   - Key stored in: HSM, KMS, config files, documentation, employee laptops
   - **Result**: Attack surface explosion

5. **No Key Lifecycle Management**:
   - Key generation: Weak RNG (predictable keys)
   - Key storage: Plaintext files
   - Key distribution: Emailed in cleartext
   - Key rotation: Never
   - Key destruction: "Delete file" (but still in backups)
   - **Result**: Complete key management failure

**Key Management Success Criteria:**

✅ **Generation**: CSRNG (cryptographically secure random number generator)  
✅ **Storage**: HSM, KMS, or TPM (not plaintext files)  
✅ **Distribution**: Encrypted channels, out-of-band verification  
✅ **Rotation**: Automated, scheduled (annual minimum)  
✅ **Backup**: Secure, offline, tested recovery  
✅ **Destruction**: Cryptographic erasure, documented  
✅ **Audit**: Key usage logged, access controlled

**This policy dedicates an entire assessment domain (IMP-A.8.24.4) to key management because it's that critical.**

### A.4 Deprecation Is Inevitable

> "Cryptographic algorithms age like milk, not wine."

**Algorithm Lifecycle Reality:**

- **DES** (1977): Broken by 1998 → Deprecated
- **MD5** (1991): Broken by 2004 → Deprecated
- **SHA-1** (1995): Broken by 2017 → Deprecated
- **3DES** (1998): Deprecated 2023 → Disallowed 2024
- **TLS 1.0** (1999): Deprecated 2020 → Disallowed 2021
- **TLS 1.1** (2006): Deprecated 2020 → Disallowed 2021
- **RSA-1024** (1990s): Deprecated 2010 → Disallowed 2013

**Future Deprecations (Predictable):**

- **RSA-2048**: Likely deprecated 2030-2035 (quantum computing threat)
- **TLS 1.2**: Will be deprecated when TLS 1.4+ arrives (≈2028-2030)
- **SHA-256**: May be superseded by SHA-3 or post-quantum hashes
- **Current algorithms**: Will be deprecated by quantum computers (2030s-2040s)

**Crypto Agility Requirements:**

Organizations MUST be able to:
1. **Detect** deprecated algorithms in use (inventory, scanning)
2. **Plan** algorithm replacement (90-day transition plan)
3. **Execute** algorithm substitution (without re-architecting entire system)
4. **Verify** complete deprecation removal (no stragglers)

**This is why the policy prohibits hardcoded algorithms and requires configurable cryptography.**

Cryptographic systems built in 2025 must be replaceable by 2030 without complete rewrites.

### A.5 Post-Quantum Cryptography Is Not Science Fiction

> "The threat is not immediate, but the migration timeline is long. Start planning now."

**Quantum Computing Threat Timeline:**

| Timeframe | Quantum Capability | Cryptographic Impact |
|-----------|-------------------|---------------------|
| **2025** | <100 qubits (current) | No immediate threat to production crypto |
| **2030** | ~1,000 qubits (estimate) | RSA-2048 potentially vulnerable, research attacks possible |
| **2035** | ~10,000 qubits (estimate) | RSA-2048/3072 broken, ECDH P-256 broken, symmetric crypto reduced security (AES-256 → AES-128 equivalent) |
| **2040+** | Mature quantum computers | All current public-key crypto broken |

**"Harvest Now, Decrypt Later" Threat:**

Adversaries can:
1. Capture encrypted data today (TLS sessions, encrypted backups, emails)
2. Store indefinitely (cheap storage)
3. Decrypt when quantum computers available (2030s-2040s)

**High-value data with long confidentiality requirements (20+ years) is at risk NOW.**

**NIST Post-Quantum Cryptography (PQC) Standards:**

| Algorithm | Type | Status | Use Case |
|-----------|------|--------|----------|
| **CRYSTALS-Kyber** | Key encapsulation | Standardized (FIPS 203) | TLS, VPN key exchange |
| **CRYSTALS-Dilithium** | Digital signature | Standardized (FIPS 204) | Code signing, certificates |
| **FALCON** | Digital signature | Standardized (FIPS 205) | Compact signatures (IoT) |
| **SPHINCS+** | Digital signature | Standardized | Stateless hash-based signatures |

**Migration Timeline (Recommended):**

- **2025-2026**: Inventory current cryptography, identify long-term data
- **2027-2028**: Test PQC in non-production (labs, dev environments)
- **2029-2030**: Hybrid cryptography deployment (classical + PQC)
- **2031-2035**: Full migration to PQC for all systems

**Crypto Agility Preparation:**

✅ No hardcoded algorithms (use configuration files, not source code)  
✅ Modular cryptographic libraries (OpenSSL, BoringSSL, wolfSSL with update paths)  
✅ Algorithm negotiation (TLS cipher suite negotiation, not forced algorithm)  
✅ Key management flexibility (HSM supports algorithm updates)  
✅ Testing framework (ability to test new algorithms without production risk)

**Organizations starting major cryptographic projects in 2025 should design for PQC migration from day one.**

---

**END OF MASTER DOCUMENT**

*"The best time to fix your cryptography was yesterday. The second-best time is today."*

*"The best time to think about the security of your communications was twenty years ago. The second best time is now."*  
*— Ancient Cryptographic Proverb (with apologies to Chinese philosophy)*

