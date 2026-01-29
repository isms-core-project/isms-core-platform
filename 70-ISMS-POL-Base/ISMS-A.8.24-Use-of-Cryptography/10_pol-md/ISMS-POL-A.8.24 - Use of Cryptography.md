# ISMS-POL-A.8.24 — Use of Cryptography

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Use of Cryptography |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.24 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.24-1 (Data Transmission Assessment)
- ISMS-IMP-A.8.24-2 (Data Storage Assessment)
- ISMS-IMP-A.8.24-3 (Authentication Assessment)
- ISMS-IMP-A.8.24-4 (Key Management Assessment)
- ISMS-IMP-A.8.24-5 (Compliance Summary Dashboard)
- ISMS-CTX-A.8.24 (Cryptographic Landscape Reference - Technical Context)
- ISMS-REF-A.5.23 (Cloud Service Provider Registry)
- ISO/IEC 27001:2022 Control A.8.24

---

## Executive Summary

This policy establishes [Organization]'s requirements for cryptographic controls to protect the confidentiality, integrity, authenticity, and non-repudiation of information in accordance with ISO/IEC 27001:2022 Control A.8.24.

**Scope**: This policy applies to all information assets classified as Internal, Confidential, or Restricted; all cryptographic implementations including encryption, digital signatures, and key management; and all organizational personnel, contractors, and third parties processing organizational information.

**Purpose**: Define organizational requirements for cryptographic control implementation and governance. This policy establishes WHAT cryptographic protection is required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8.24 suite.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS, HIPAA, SOX, DORA, NIS2, FINMA) apply where [Organization]'s business activities trigger applicability.

**Key Changes in Version 2.0**:
- Corrected regulatory tier assignments per ISMS-POL-00 (HIPAA and SOX moved to Tier 2 - Conditional Applicability)
- Removed technical annexes (algorithm tables, cloud deployment guidance) - now referenced from ISMS-CTX-A.8.24 and ISMS-IMP-A.8.24-2
- Streamlined policy to core requirements with clear references to implementation guidance
- Strengthened separation between policy (WHAT/WHO) and implementation (HOW)

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.24

**ISO/IEC 27001:2022 Annex A.8.24 - Use of Cryptography**

> *A policy on the use of cryptographic controls for protection of information should be developed and implemented.*

**Control Objective**: Establish organizational policy for cryptographic controls protecting information confidentiality, integrity, authenticity, and non-repudiation throughout the information lifecycle.

**This Policy Addresses**:
- Cryptographic requirements based on data classification and organizational risk appetite
- Data transmission encryption requirements (TLS, VPN, email, protocols)
- Data storage encryption requirements (databases, files, backups, removable media)
- Authentication requirements (certificates, digital signatures, PKI)
- Key management requirements (generation, storage, rotation, destruction)
- Organizational roles and responsibilities for cryptographic governance
- Exception and incident management frameworks
- Integration with [Organization]'s risk assessment and treatment processes

### 1.2 What This Policy Does

This policy:
- **Defines** cryptographic control requirements aligned with data classification and regulatory obligations
- **Establishes** governance framework for cryptographic decision-making and accountability
- **Specifies** mandatory cryptographic protections for data in transit and at rest
- **References** applicable regulatory requirements per ISMS-POL-00
- **Identifies** organizational roles and responsibilities for cryptographic controls

### 1.3 What This Policy Does NOT Do

This policy does NOT:
- **Specify technical implementation details** (see ISMS-IMP-A.8.24 Implementation Guides)
- **Define specific cryptographic algorithms or parameters** (see ISMS-CTX-A.8.24 Cryptographic Landscape Reference)
- **Provide system-specific configuration procedures** (see ISMS-IMP-A.8.24 Assessment Guides)
- **Select cryptographic technologies or vendors** (technology selection based on [Organization]'s risk assessment)
- **Replace risk assessment** (cryptographic controls selected based on [Organization]'s risk treatment)
- **Define detailed incident response procedures** (integrated with organizational incident response)
- **Establish exception request workflows** (exception management framework defined in Section 4)

**Rationale**: Separating policy requirements from implementation guidance enables:
- Policy stability despite evolving cryptographic landscape and algorithm deprecations
- Technical agility for algorithm updates and technology changes without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Focused audit scope (auditors audit policy compliance, not technical implementation details)

**Document Structure**:
- **ISMS-POL-A.8.24** (THIS DOCUMENT): Policy requirements (WHAT and WHO)
- **ISMS-IMP-A.8.24-1 through IMP-5**: Implementation guidance (HOW)
- **ISMS-CTX-A.8.24**: Technical reference for algorithms, cipher suites, industry standards (non-ISMS informational document)

### 1.4 Scope

**This policy applies to**:
- All information assets classified as Internal, Confidential, or Restricted per [Organization]'s data classification scheme
- All systems, applications, networks, and services processing, storing, or transmitting organizational information
- All cryptographic implementations including encryption (symmetric and asymmetric), hashing, digital signatures, and key management
- All organizational personnel (employees, contractors, temporary staff) with access to organizational information
- All third-party service providers, cloud services, and outsourced operations handling organizational data
- All deployment models (on-premises infrastructure, hybrid environments, cloud services)

**Out of Scope**:
- Public information (unclassified data requiring no cryptographic protection)
- Consumer-grade encryption for personal use (unless processing organizational data)
- Cryptographic research and development (covered under separate R&D policies)
- Product-embedded cryptography where [Organization] has no configuration control (assessed during procurement)

### 1.5 Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**. 

**Tier 1: Mandatory Compliance**

[Organization] MUST comply with these regulations based on jurisdiction and business operations:

**Swiss Federal Data Protection Act (nDSG/FADP)**
- **Applicability**: All operations in Switzerland
- **Key Requirements**: Art. 8 (Appropriate technical and organizational measures including encryption)
- **ISMS Impact**: Data protection by design, encryption of personal data, data breach notification

**EU General Data Protection Regulation (GDPR)**
- **Applicability**: When processing personal data of EU residents
- **Key Requirements**: Art. 32 (Security of processing - encryption and pseudonymization)
- **ISMS Impact**: Technical and organizational measures (TOMs), encryption requirements, data breach response

**ISO/IEC 27001:2022**
- **Applicability**: Required for ISO 27001 certification
- **Key Requirements**: Control A.8.24 (Use of Cryptography) - establish and implement cryptographic policy
- **ISMS Impact**: This policy document fulfills Control A.8.24 policy requirement

**Tier 2: Conditional Applicability**

These regulations apply ONLY when specific conditions are met. [Organization] must assess applicability based on business activities:

**PCI DSS (Payment Card Industry Data Security Standard)** [If processing payment card data]
- **Applicability Trigger**: Processing, storing, or transmitting payment card data
- **Key Requirements**: 
  - Requirement 3.4: Render PAN unreadable (encryption, truncation, hashing)
  - Requirement 3.5: Protect cryptographic keys
  - Requirement 4.1: Encrypt transmission of cardholder data over open, public networks
- **ISMS Impact**: Cardholder data encryption (at rest and in transit), key management procedures
- **Applicability Assessment**: See ISMS-POL-00 Section 4.1

**HIPAA (Health Insurance Portability and Accountability Act)** [If processing US healthcare data]
- **Applicability Trigger**: Processing Protected Health Information (PHI) of US persons
- **Key Requirements** (Addressable Safeguards):
  - 45 CFR § 164.312(a)(2)(iv): Encryption and decryption (addressable - risk assessment required)
  - 45 CFR § 164.312(e)(2)(ii): Encryption of ePHI in transit (addressable - risk assessment required)
- **ISMS Impact**: Risk-based encryption decisions for PHI, documented risk assessments where encryption not implemented
- **Note**: HIPAA encryption requirements are "addressable" not "required" - risk assessment determines implementation
- **Applicability Assessment**: See ISMS-POL-00 Section 4.2

**SOX (Sarbanes-Oxley Act)** [If US publicly traded company]
- **Applicability Trigger**: [Organization] is publicly traded company subject to US securities regulations
- **Key Requirements**: Section 404 (Internal controls over financial reporting - ITGC requirements)
- **ISMS Impact**: IT General Controls (ITGC) for financial data integrity, access controls, audit trails
- **Note**: SOX does not mandate specific cryptographic controls but requires appropriate safeguards for financial data integrity
- **Applicability Assessment**: See ISMS-POL-00 Section 4.6

**DORA (Digital Operational Resilience Act)** [If EU financial services entity]
- **Applicability Trigger**: EU financial entity (credit institutions, investment firms, payment institutions, etc.)
- **Key Requirements**: Art. 9, 10 (ICT risk management framework including encryption)
- **ISMS Impact**: ICT risk management, encryption for financial data, third-party risk management
- **Applicability Assessment**: See ISMS-POL-00 Section 4.4

**NIS2 (Network and Information Security Directive)** [If essential/important entity in EU]
- **Applicability Trigger**: Designated as essential or important entity under NIS2 scope
- **Key Requirements**: Art. 21 (Cybersecurity risk management measures including encryption)
- **ISMS Impact**: Cybersecurity measures, incident handling, supply chain security
- **Applicability Assessment**: See ISMS-POL-00 Section 4.5

**FINMA (Swiss Financial Market Supervisory Authority)** [If Swiss-regulated financial institution]
- **Applicability Trigger**: [Organization] is supervised by FINMA (banks, insurance, securities dealers, etc.)
- **Key Requirements**: FINMA Circular 2008/21 (Operational Risks in Banks - IT security requirements)
- **ISMS Impact**: Information security framework, encryption requirements, outsourcing controls
- **Applicability Assessment**: See ISMS-POL-00 Section 4.7

**Tier 3: Informational Reference / Best Practice Alignment**

These frameworks provide technical guidance and are used for implementation decisions but do NOT constitute mandatory compliance requirements unless contractually specified:

**NIST (National Institute of Standards and Technology) Publications**
- NIST SP 800-52 Rev. 2: Guidelines for TLS Implementations
- NIST SP 800-57 Part 1 Rev. 5: Key Management Recommendations
- NIST SP 800-131A Rev. 2: Transitioning the Use of Cryptographic Algorithms
- NIST SP 800-175B Rev. 1: Guideline for Using Cryptographic Standards

**BSI (Bundesamt für Sicherheit in der Informationstechnik) - German Federal Office for Information Security**
- BSI TR-02102-1: Cryptographic Mechanisms - Recommendations and Key Lengths
- BSI TR-02102-2: Use of TLS
- BSI TR-02102-4: Use of Secure Shell (SSH)

**Other Technical Standards**
- CIS Controls (Center for Internet Security)
- OWASP (Open Web Application Security Project) - Application security best practices
- ISO/IEC 18033: Encryption Algorithms

**United States Federal Requirements**

References to US federal frameworks (FISMA, FIPS, FedRAMP, NIST cybersecurity requirements) apply ONLY where [Organization] has explicit US federal contractual obligations.

**US Federal Frameworks Classification**:
- **FISMA (Federal Information Security Management Act)**: Mandatory ONLY for US federal agencies and federal contractors
- **FIPS 140-2/140-3 (Federal Information Processing Standards)**: Cryptographic module validation required ONLY for US federal systems
- **FedRAMP (Federal Risk and Authorization Management Program)**: Applicable ONLY when providing cloud services to US federal agencies

**Applicability Determination**: Per ISMS-POL-00 Section 5 (US Federal Requirements), these frameworks are informational reference unless:
1. [Organization] has explicit US federal government contracts requiring compliance, OR
2. Customer contracts specifically mandate FIPS 140-2/3 validated cryptographic modules

**Default Classification**: Tier 3 (Informational Reference) unless contractually required, in which case treated as Tier 1 (Mandatory) for specific systems/services covered by contract.

**For Complete Regulatory Framework**: See ISMS-POL-00 (Regulatory Applicability Framework) for detailed categorization, applicability triggers, and assessment methodology.

### 1.6 Integration with Risk Management

Cryptographic control selection and implementation are integrated with [Organization]'s risk management process (ISO/IEC 27001:2022 Clause 6).

**Risk Assessment Inputs**:
- Data classification and sensitivity assessment
- Threat modeling (data in transit, data at rest, authentication)
- Regulatory applicability determination (per ISMS-POL-00)
- Business impact analysis (confidentiality, integrity, availability)
- Technical feasibility and operational constraints

**Risk Treatment Outputs**:
- Cryptographic control selection (encryption, hashing, digital signatures)
- Algorithm and key length decisions (referenced from ISMS-CTX-A.8.24)
- Key management approach (HSM, cloud KMS, software-based)
- Exception and compensating control approvals

**Continuous Improvement**:
- Algorithm deprecation monitoring (NIST, BSI, CA/Browser Forum)
- Cryptographic agility planning (transition to post-quantum cryptography)
- Periodic reassessment of cryptographic controls (quarterly minimum)

---

## 2. Roles and Responsibilities

### 2.1 Governance Structure

Cryptographic control governance follows [Organization]'s ISMS governance framework with clear accountability for policy, implementation, and operational management.

**Decision Authority Hierarchy**:
1. **Executive Management**: Approves cryptographic policy and accepts residual risks
2. **CISO**: Owns cryptographic policy, approves exceptions, manages cryptographic risk
3. **CIO**: Implements cryptographic controls, allocates resources, manages operations
4. **System Owners**: Responsible for cryptographic control implementation in their systems
5. **Security Team**: Provides technical expertise, monitors compliance, manages incidents

### 2.2 Cryptographic Control Roles

**Chief Information Security Officer (CISO)**

**Accountabilities**:
- Owns and maintains this cryptographic policy
- Approves cryptographic control exceptions and compensating controls
- Reviews cryptographic risk assessments and treatment decisions
- Monitors regulatory changes affecting cryptographic requirements
- Reports cryptographic compliance status to Executive Management

**Authorities**:
- Mandate cryptographic control implementation for systems processing Confidential/Restricted data
- Approve or reject exception requests
- Require remediation of non-compliant cryptographic implementations
- Escalate unresolved cryptographic risks to Executive Management

**Responsibilities**:
- Annual policy review and update
- Cryptographic algorithm deprecation monitoring
- Exception approval within 10 business days
- Quarterly cryptographic compliance reporting

---

**Chief Information Officer (CIO)**

**Accountabilities**:
- Implements cryptographic controls in [Organization]'s infrastructure
- Provides resources (budget, personnel, tools) for cryptographic implementation
- Ensures operational readiness of cryptographic systems (key management, certificate lifecycle)
- Manages cryptographic technology selection and vendor relationships

**Authorities**:
- Select cryptographic technologies and vendors (within policy constraints)
- Allocate budget for cryptographic infrastructure (HSM, KMS, certificates)
- Approve technical implementation approaches
- Manage cryptographic operations team

**Responsibilities**:
- Implement policy-mandated cryptographic controls
- Maintain cryptographic infrastructure availability and performance
- Coordinate with CISO on cryptographic risk treatment
- Execute approved exception remediation plans

---

**System Owners (Application Owners, Database Owners, Infrastructure Owners)**

**Accountabilities**:
- Implement cryptographic controls for systems under their ownership
- Maintain compliance with cryptographic policy requirements
- Document cryptographic implementation (algorithms, key management, configurations)
- Report cryptographic compliance status via assessment workbooks

**Authorities**:
- Select specific cryptographic implementations (within policy and technical standards)
- Request exceptions for systems with unique constraints
- Define system-specific cryptographic requirements (beyond policy minimums)

**Responsibilities**:
- Complete ISMS-IMP-A.8.24 assessment workbooks quarterly
- Maintain evidence of cryptographic control implementation
- Remediate identified cryptographic gaps within approved timelines
- Coordinate with Security Team for cryptographic incident response

---

**Security Team (Security Engineers, Security Architects)**

**Accountabilities**:
- Provides cryptographic technical expertise and guidance
- Monitors cryptographic control compliance across [Organization]
- Manages cryptographic incidents (compromised keys, algorithm vulnerabilities)
- Maintains ISMS-CTX-A.8.24 (Cryptographic Landscape Reference)

**Authorities**:
- Recommend cryptographic technologies and configurations
- Review and validate cryptographic implementations
- Escalate non-compliance to CISO
- Declare cryptographic incidents

**Responsibilities**:
- Support System Owners with cryptographic implementation guidance
- Monitor algorithm deprecation announcements (NIST, BSI, CA/Browser Forum)
- Update ISMS-CTX-A.8.24 as industry standards evolve
- Conduct cryptographic control assessments and audits
- Respond to cryptographic security incidents

---

**Legal/Compliance Officer**

**Accountabilities**:
- Monitors regulatory changes affecting cryptographic requirements
- Assesses cryptographic compliance with applicable regulations
- Supports exception approval process (regulatory impact assessment)

**Authorities**:
- Flag regulatory non-compliance to CISO and Executive Management
- Recommend policy updates for regulatory alignment
- Require cryptographic controls for contractual obligations

**Responsibilities**:
- Update ISMS-POL-00 (Regulatory Applicability Framework) for cryptographic regulations
- Review exception requests for regulatory impact
- Support internal and external audits on cryptographic compliance

---

**Third-Party Service Providers (Cloud Providers, Managed Service Providers, SaaS Vendors)**

**Accountabilities**:
- Implement cryptographic controls per contractual requirements
- Provide evidence of cryptographic implementation (SOC 2, ISO 27001 certificates)
- Notify [Organization] of cryptographic incidents or algorithm deprecations affecting services

**Authorities**:
- Manage cryptographic infrastructure within their service boundaries
- Select cryptographic implementations (subject to [Organization] approval for Restricted data)

**Responsibilities**:
- Maintain encryption of [Organization] data at rest and in transit
- Provide access to key management interfaces (customer-managed keys)
- Report cryptographic compliance status via attestations or audits
- Coordinate with [Organization] for cryptographic incident response

**Evaluation**: See ISMS-REF-A.5.23 (Cloud Service Provider Registry) for cryptographic requirements in vendor contracts.

### 2.3 Accountability Matrix

| Role | Policy Ownership | Exception Approval | Implementation | Monitoring | Incident Response |
|------|------------------|-------------------|----------------|------------|-------------------|
| **Executive Management** | Approve | Final Authority | Fund | Review Reports | Informed |
| **CISO** | Own | Primary Approval | Define Requirements | Oversight | Coordinate |
| **CIO** | Support | Recommend | Execute | Operational | Support |
| **System Owners** | Comply | Request | Implement | Report Status | Execute |
| **Security Team** | Support | Recommend | Advise | Monitor | Lead Technical Response |
| **Legal/Compliance** | Regulatory Input | Regulatory Review | N/A | Compliance Audit | Legal Support |

---

## 3. Policy Requirements

### 3.1 Data Classification and Cryptographic Requirements

Cryptographic control requirements are determined by data classification per [Organization]'s data classification scheme.

**Data Classification Mapping**:

| Data Classification | Confidentiality Impact | Example Data Types | Cryptographic Requirements |
|---------------------|----------------------|-------------------|---------------------------|
| **Restricted** | Critical - Severe damage if disclosed | Trade secrets, financial records, patient data, cryptographic keys | MANDATORY encryption (transit AND rest), customer-managed keys, AES-256 minimum |
| **Confidential** | High - Significant damage if disclosed | Employee data, customer contracts, internal financial data | MANDATORY encryption (transit AND rest), AES-128/256 acceptable |
| **Internal** | Moderate - Limited damage if disclosed | Internal documentation, operational procedures, project plans | RECOMMENDED encryption based on risk assessment |
| **Public** | None - Intended for public disclosure | Marketing materials, public website content, press releases | OPTIONAL - No cryptographic requirements |

**Key Principle**: Higher data classification → Stronger cryptographic controls and key management requirements.

### 3.2 Data Transmission Encryption Requirements

**Objective**: Protect data confidentiality and integrity during transmission across networks.

**Policy Requirements by Data Classification**:

**Restricted Data Transmission**:
- MANDATORY TLS 1.2 minimum (TLS 1.3 preferred) for all network transmission
- MANDATORY VPN or equivalent encryption for remote access
- MANDATORY end-to-end encryption for email containing Restricted data (S/MIME or PGP)
- MANDATORY digital signatures for authentication and non-repudiation where required
- PROHIBITED unencrypted transmission under any circumstances

**Confidential Data Transmission**:
- MANDATORY TLS 1.2 minimum for web services and APIs
- MANDATORY encryption for file transfer (SFTP, FTPS, or HTTPS)
- MANDATORY VPN for remote access to Confidential data
- RECOMMENDED email encryption (S/MIME or PGP)
- PROHIBITED unencrypted transmission over public networks

**Internal Data Transmission**:
- MANDATORY TLS 1.2 minimum for web services exposing Internal data over public networks
- RECOMMENDED encryption for file transfer
- RECOMMENDED VPN for remote access
- Unencrypted transmission acceptable within secured internal networks (risk assessment required)

**Public Data Transmission**:
- RECOMMENDED HTTPS for integrity and authentication (not required for confidentiality)
- No mandatory encryption requirements

**Protocol-Specific Requirements**:

| Protocol/Service | Minimum Encryption | Acceptable Use | Prohibited Use |
|------------------|-------------------|----------------|----------------|
| **HTTPS/TLS** | TLS 1.2 (TLS 1.3 preferred) | All web services, APIs, internal applications | TLS 1.0, TLS 1.1, SSL v2/v3 |
| **Email** | TLS 1.2 (transport), S/MIME/PGP (end-to-end) | All email transmission | Unencrypted SMTP for Restricted data |
| **File Transfer** | SFTP, FTPS, or HTTPS | All file transfers containing organizational data | FTP (unencrypted), HTTP file transfer |
| **VPN** | IPsec or TLS-based VPN (OpenVPN, WireGuard) | All remote access to organizational networks | PPTP, L2TP without IPsec |
| **SSH** | SSH-2 with RSA-2048+ or Ed25519 keys | Server administration, secure shell access | SSH-1, password-only authentication |
| **RDP** | RDP with TLS 1.2, NLA (Network Level Authentication) | Remote desktop access | Unencrypted RDP, RDP over public networks without VPN |
| **Database** | TLS 1.2 for client-server connections | All database connections over networks | Unencrypted database protocols (MySQL, PostgreSQL, MSSQL without TLS) |
| **Wireless** | WPA3 (WPA2-Enterprise acceptable) | Organizational WiFi networks | WEP, WPA, WPA2-Personal, open networks |

**Implementation Guidance**: See ISMS-IMP-A.8.24-1 (Data Transmission Assessment) for detailed configuration procedures, cipher suite selection, certificate management, and compliance verification.

**Technical Reference**: See ISMS-CTX-A.8.24 (Cryptographic Landscape Reference) for algorithm status, TLS cipher suites, and industry standards evolution.

### 3.3 Data Storage Encryption Requirements

**Objective**: Protect data confidentiality at rest against unauthorized access, theft, or loss.

**Policy Requirements by Data Classification**:

**Restricted Data Storage**:
- MANDATORY full disk encryption (FDE) or volume encryption for all storage (mobile devices, laptops, servers)
- MANDATORY database Transparent Data Encryption (TDE) or equivalent
- MANDATORY file-level or application-level encryption for cloud storage
- MANDATORY customer-managed keys (CMEK) or customer-held keys (HYOK) for cloud storage
- MANDATORY backup encryption with separate key storage
- MANDATORY AES-256 minimum encryption algorithm
- MANDATORY key escrow and recovery procedures

**Confidential Data Storage**:
- MANDATORY encryption for mobile devices and laptops (BitLocker, FileVault, LUKS)
- MANDATORY database TDE or column-level encryption
- MANDATORY encryption for cloud storage (customer-managed keys preferred)
- MANDATORY backup encryption
- AES-128 or AES-256 acceptable
- MANDATORY key escrow for business-owned devices

**Internal Data Storage**:
- RECOMMENDED encryption for mobile devices and laptops
- RECOMMENDED database encryption for sensitive Internal data
- RECOMMENDED encryption for cloud storage
- Risk assessment determines encryption requirements
- Encryption REQUIRED for portable storage (USB drives, external disks)

**Public Data Storage**:
- OPTIONAL - No encryption requirements
- May use encryption for integrity protection or operational consistency

**Storage Type-Specific Requirements**:

| Storage Type | Restricted Data | Confidential Data | Internal Data |
|--------------|----------------|------------------|---------------|
| **Mobile Devices** | MANDATORY FDE (iOS, Android encryption) | MANDATORY FDE | RECOMMENDED |
| **Laptops/Workstations** | MANDATORY (BitLocker, FileVault, LUKS) | MANDATORY | RECOMMENDED |
| **Servers** | MANDATORY (volume/disk encryption) | MANDATORY | Risk-based |
| **Databases** | MANDATORY (TDE, column-level, field-level) | MANDATORY (TDE minimum) | Risk-based |
| **Cloud Storage** | MANDATORY (CMEK/HYOK) | MANDATORY (CMEK preferred) | RECOMMENDED |
| **Backups** | MANDATORY (AES-256) | MANDATORY | RECOMMENDED |
| **Removable Media** | MANDATORY (BitLocker To Go, encrypted devices) | MANDATORY | MANDATORY |

**Cloud Deployment Encryption Requirements**:

**On-Premises Deployment**:
- [Organization] controls all encryption infrastructure (HSM, KMS)
- Full device/volume encryption for servers and storage
- Database TDE enabled for all databases containing Confidential/Restricted data

**Hybrid Deployment**:
- Encryption required in both on-premises and cloud environments
- Key synchronization or separate key management per environment
- Cross-environment data transfer requires encryption in transit

**Cloud Deployment**:
- Cloud provider encryption-at-rest enabled for all storage services
- Customer-managed keys (CMEK/BYOK) REQUIRED for Restricted data
- Customer-managed keys (CMEK/BYOK) PREFERRED for Confidential data
- Cloud-service-managed keys (CSEK/PMK) acceptable for Internal data with risk acceptance
- Customer-held keys (HYOK) REQUIRED for Restricted data with regulatory key custody requirements

**Implementation Guidance**: See ISMS-IMP-A.8.24-2 (Data Storage Assessment) for:
- Detailed encryption configuration procedures
- Cloud encryption architecture patterns (Section 5.8)
- Key management model selection (PMK/CMEK/HYOK)
- Deployment model considerations (on-premises, hybrid, cloud)
- Platform-specific guidance (BitLocker, FileVault, LUKS, TDE, Cloud KMS)

**Technical Reference**: See ISMS-CTX-A.8.24 for encryption algorithms, key lengths, and maturity status.

### 3.4 Authentication and Digital Signature Requirements

**Objective**: Ensure authenticity, non-repudiation, and integrity through cryptographic authentication mechanisms.

**Password-Based Authentication**:
- Passwords MUST be hashed using approved algorithms (see ISMS-CTX-A.8.24 for current recommendations)
- Password storage MUST NOT use reversible encryption
- PROHIBITED: Plain text storage, weak hashing (MD5, SHA-1 for password hashing), symmetric encryption of passwords

**Multi-Factor Authentication (MFA)**:
- MANDATORY for all access to Restricted data
- MANDATORY for all administrative/privileged access
- RECOMMENDED for access to Confidential data
- MFA mechanisms: Time-based OTP (TOTP), hardware tokens, biometrics, certificate-based authentication

**Digital Certificates and PKI**:
- Public TLS certificates MUST be issued by trusted Certificate Authority (CA)
- Internal PKI certificates for internal services acceptable with proper CA hierarchy
- Certificate validity periods aligned with CA/Browser Forum requirements (public certificates) or organizational policy (internal certificates)
- Certificate lifecycle management REQUIRED (issuance, renewal, revocation)

**Digital Signatures**:
- REQUIRED for code signing (software releases, scripts)
- REQUIRED for document signing where legal non-repudiation needed
- REQUIRED for email authentication (S/MIME, PGP) for Restricted data
- Signature algorithms per ISMS-CTX-A.8.24 current recommendations

**Biometric Authentication**:
- Acceptable as MFA factor (combined with password/PIN)
- Biometric data MUST be stored as cryptographic hash or template (not raw biometric)
- PROHIBITED: Reversible storage of biometric data

**Implementation Guidance**: See ISMS-IMP-A.8.24-3 (Authentication Assessment) for:
- Password hashing algorithm selection and configuration
- MFA implementation procedures
- Certificate lifecycle management
- Digital signature procedures
- Biometric authentication requirements

**Technical Reference**: See ISMS-CTX-A.8.24 for hash functions, signature algorithms, and key lengths.

### 3.5 Key Management Requirements

**Objective**: Protect cryptographic keys throughout their lifecycle to prevent unauthorized access, compromise, or loss.

**Key Generation**:
- Cryptographic keys MUST be generated using cryptographically secure random number generators (CSPRNG)
- Key generation MUST occur in secure environment (HSM, TPM, or trusted key management system)
- Weak or predictable key generation PROHIBITED

**Key Storage**:
- **Restricted Data Keys**: MUST be stored in Hardware Security Module (HSM) or equivalent tamper-resistant device
- **Confidential Data Keys**: MUST be stored in HSM, Trusted Platform Module (TPM), or cloud KMS with customer-managed keys
- **Internal Data Keys**: MAY be stored in software-based key management system with appropriate access controls
- PROHIBITED: Plaintext key storage, hardcoded keys in application code, keys in version control systems

**Key Rotation**:
- **Encryption Keys**: Rotation frequency based on data classification and risk assessment (annual minimum for Restricted data)
- **TLS Certificates**: Per certificate validity period (public certificates per CA/Browser Forum requirements)
- **SSH Keys**: Annual rotation minimum for administrative access keys
- **API Keys/Tokens**: 90-day rotation recommended, 180-day maximum for Confidential data access

**Key Escrow and Recovery**:
- MANDATORY for business-owned device encryption keys (BitLocker, FileVault recovery keys)
- MANDATORY for data encryption keys protecting Restricted/Confidential data
- Escrow system MUST have access controls and audit logging
- Key recovery procedures MUST be tested annually

**Key Destruction**:
- Keys MUST be securely destroyed when no longer needed
- Cryptographic erasure or physical destruction of key material
- Destruction MUST be logged and verifiable
- Retention aligned with data retention policies and legal requirements

**Key Separation**:
- Encryption keys MUST be stored separately from encrypted data
- Key management systems MUST NOT be co-located with application servers
- Multi-party control (split knowledge, dual control) REQUIRED for Restricted data key access

**Implementation Guidance**: See ISMS-IMP-A.8.24-4 (Key Management Assessment) for:
- Key lifecycle procedures (generation, storage, rotation, destruction)
- HSM/KMS selection and configuration
- Key escrow and recovery procedures
- Cloud key management (AWS KMS, Azure Key Vault, GCP KMS)
- Key rotation schedules and automation

**Technical Reference**: See ISMS-CTX-A.8.24 for key length recommendations and algorithm lifecycle.

### 3.6 Cryptographic Agility

**Objective**: Enable [Organization] to adapt to evolving cryptographic landscape, algorithm deprecations, and emerging threats (including post-quantum cryptography).

**Algorithm Lifecycle Monitoring**:
- Security Team MUST monitor algorithm deprecation announcements from authoritative sources:
  - NIST (National Institute of Standards and Technology)
  - BSI (Bundesamt für Sicherheit in der Informationstechnik)
  - CA/Browser Forum (for TLS certificates)
  - IETF (Internet Engineering Task Force)
  - Browser vendors (Chrome, Firefox, Safari, Edge root programs)

**Deprecation Response**:
- When algorithm deprecation announced: Risk assessment within 30 days
- Migration planning required for deprecated algorithms affecting Confidential/Restricted data
- Migration execution timeline based on deprecation severity and organizational risk

**Post-Quantum Cryptography Readiness**:
- Monitor NIST post-quantum cryptography standardization progress
- Assess organizational systems for post-quantum migration requirements
- Plan for hybrid cryptography during transition period (classical + post-quantum)

**Cryptographic Inventory**:
- Maintain inventory of cryptographic implementations (algorithms, key lengths, systems)
- Quarterly review of cryptographic inventory for deprecated algorithms
- Assessment workbooks (ISMS-IMP-A.8.24-1 through IMP-4) document current cryptographic status

**Technical Reference**: ISMS-CTX-A.8.24 (Cryptographic Landscape Reference) documents:
- Algorithm lifecycle status (Modern, Legacy, Deprecated, Obsolete)
- Industry standards evolution
- Post-quantum cryptography status
- Certificate validity trends

**Note**: ISMS-CTX-A.8.24 is a non-ISMS technical reference document maintained by Security Team. Updates to CTX do NOT require policy revision.

---

## 4. Exception Management

### 4.1 Exception Policy

Cryptographic policy requirements are mandatory for systems processing Internal, Confidential, or Restricted data. Exceptions may be granted only when:
- Technical constraints prevent policy-compliant implementation, AND
- Compensating controls reduce risk to acceptable levels, AND
- Exception is documented, approved, and time-limited

**Prohibited Exceptions**:
- Exceptions that violate mandatory regulatory requirements (Tier 1 per ISMS-POL-00)
- Exceptions for Restricted data without compensating controls
- Permanent exceptions without periodic review
- Exceptions based solely on cost or convenience

**Exception Principles**:
- Exceptions are temporary measures, not permanent solutions
- Remediation planning is mandatory for all approved exceptions
- Exceptions expire and require renewal (maximum 12 months)
- Exception inventory maintained and reviewed quarterly

### 4.2 Exception Request Process

**Step 1: Exception Request Submission**

System Owner submits exception request documenting:
- System/application/service requiring exception
- Specific policy requirement(s) that cannot be met
- Data classification of affected data
- Technical or business justification for exception
- Proposed compensating controls
- Risk assessment (likelihood and impact of not implementing policy requirement)
- Remediation plan with target completion date
- Budget and resource requirements for remediation

**Exception Request Template**: Available from Security Team

**Step 2: Security Team Review**

Security Team reviews exception request within 5 business days:
- Validates technical justification
- Assesses proposed compensating controls
- Evaluates risk assessment
- Recommends approval, conditional approval, or rejection
- Escalates to CISO with recommendation

**Step 3: CISO Approval Decision**

CISO approves or rejects exception within 10 business days:
- **Approved**: Exception granted with conditions, expiration date, and review schedule
- **Conditional Approval**: Exception granted pending specific conditions (e.g., additional compensating controls)
- **Rejected**: Exception denied, policy-compliant implementation required

**Step 4: Exception Documentation**

Approved exceptions documented in Exception Register:
- Exception ID (unique identifier)
- Approval date and expiration date
- System/service covered by exception
- Specific policy requirements waived
- Compensating controls implemented
- Risk acceptance (residual risk documented)
- Remediation plan and milestones
- Review schedule (quarterly minimum)

**Step 5: Exception Monitoring**

Security Team monitors exception status:
- Quarterly review of compensating control effectiveness
- Remediation progress tracking
- Exception expiration alerts (60 days before expiration)
- Annual exception report to Executive Management

### 4.3 Compensating Controls

When policy-compliant cryptographic controls cannot be implemented, compensating controls reduce risk to acceptable levels.

**Acceptable Compensating Controls (Examples)**:
- **Network segmentation**: Isolate non-compliant systems in restricted network segments with enhanced monitoring
- **Enhanced access controls**: Multi-factor authentication, privileged access management, just-in-time access
- **Data minimization**: Reduce data classification (e.g., anonymization, pseudonymization) to lower encryption requirements
- **Application-level encryption**: Encrypt sensitive fields at application layer if database TDE unavailable
- **Physical security**: Enhanced physical security for systems with unencrypted storage (locked facilities, biometric access)
- **Monitoring and alerting**: Enhanced security monitoring, SIEM correlation, anomaly detection
- **Time-limited access**: Restrict access to non-compliant systems to specific time windows with logging

**Unacceptable Compensating Controls**:
- Policy acknowledgment or user training alone (does not reduce technical risk)
- Antivirus or endpoint protection (does not replace encryption)
- Backup-only encryption (does not protect primary data)
- Obscurity or obfuscation (not cryptographically secure)

**Compensating Control Assessment**:
- Security Team validates compensating controls provide equivalent risk reduction
- Compensating controls must be verifiable and auditable
- Annual review of compensating control effectiveness

### 4.4 Exception Review and Renewal

**Quarterly Exception Review**:
- Security Team reviews all active exceptions
- Validates compensating controls remain effective
- Tracks remediation progress against milestones
- Escalates overdue remediation to CISO

**Exception Expiration and Renewal**:
- Exceptions expire after 12 months maximum
- Renewal requires updated exception request (same approval process)
- Renewal NOT automatic - requires re-justification
- Repeated renewals trigger escalation to Executive Management

**Exception Closure**:
- Exception closed when policy-compliant implementation completed
- Exception closed when system/service decommissioned
- Closure documented in Exception Register
- Lessons learned captured for future implementations

### 4.5 Exception Reporting

**Quarterly Report to CISO**:
- Active exceptions count and risk summary
- Overdue remediation items
- New exceptions requested/approved/rejected
- Exception trends and patterns

**Annual Report to Executive Management**:
- Exception inventory and risk profile
- Remediation completion rate
- Systemic issues requiring policy or resource changes
- Recommendations for exception reduction

---

## 5. Assessment and Compliance

### 5.1 Compliance Verification Methodology

[Organization] verifies cryptographic policy compliance through structured assessment process using ISMS-IMP-A.8.24 assessment workbooks.

**Assessment Framework**:
- **IMP-A.8.24-1**: Data Transmission Assessment (HTTPS/TLS, Email, File Transfer, VPN, SSH, RDP, APIs, Database, Wireless, Cloud)
- **IMP-A.8.24-2**: Data Storage Assessment (Mobile Devices, Laptops, Servers, Databases, Cloud Storage, Backups, Removable Media)
- **IMP-A.8.24-3**: Authentication Assessment (Password Hashing, MFA, Certificates, Digital Signatures, Biometrics)
- **IMP-A.8.24-4**: Key Management Assessment (Key Generation, Storage, Rotation, Escrow, Destruction)
- **IMP-A.8.24-5**: Compliance Summary Dashboard (Consolidated view across all assessments)

**Assessment Frequency**:
- **Quarterly**: All systems processing Confidential or Restricted data
- **Annually**: All systems processing Internal data
- **Triggered**: After major infrastructure changes, security incidents, or regulatory updates

### 5.2 Assessment Process

**Step 1: Assessment Planning** (Security Team + System Owners)
- Identify systems and services in scope
- Assign assessment responsibilities by system/service area
- Distribute assessment workbooks (Excel templates generated via Python scripts)
- Schedule assessment completion deadline (typically 30 days)

**Step 2: Data Collection** (System Owners)
- Complete assessment workbooks for assigned systems
- Document current cryptographic implementation status
- Identify compliance gaps (✅ Compliant / ⚠️ Partial / ❌ Non-Compliant)
- Collect evidence (configuration screenshots, reports, certificates)
- Document exceptions and compensating controls

**Step 3: Gap Analysis** (System Owners + Security Team)
- Review identified gaps against policy requirements
- Assess gap severity (High/Medium/Low based on data classification and risk)
- Validate compensating controls if applicable
- Develop remediation plans for non-compliant items

**Step 4: Remediation Planning** (System Owners)
- Document remediation actions required
- Assign responsible persons and target completion dates
- Identify budget and resource requirements
- Prioritize remediation based on risk (High priority: Restricted data gaps)

**Step 5: Dashboard Consolidation** (Security Team)
- Consolidate assessment workbooks into ISMS-IMP-A.8.24-5 Dashboard
- Calculate overall compliance percentage
- Identify top gaps requiring immediate attention
- Generate executive summary for CISO

**Step 6: Review and Approval** (CISO)
- Review consolidated dashboard and gap analysis
- Approve remediation plans and timelines
- Escalate critical gaps to Executive Management if needed
- Track remediation progress through quarterly reviews

### 5.3 Compliance Scoring

**Compliance Calculation**:
```
Compliance % = (Compliant Items / Total Applicable Items) × 100

Where:
- Compliant Items: Items marked ✅ Compliant
- Total Applicable Items: All items excluding N/A (Not Applicable)
- Partial (⚠️) and Non-Compliant (❌) count as non-compliant
```

**Compliance Targets**:
- **Mature ISMS**: ≥90% overall compliance
- **New ISMS**: ≥70% compliance in first year, ≥85% by year two, ≥90% by year three
- **Restricted Data Systems**: ≥95% compliance (higher bar for highest sensitivity)
- **Confidential Data Systems**: ≥90% compliance
- **Internal Data Systems**: ≥80% compliance

**Compliance Status Definitions**:
- **✅ Compliant**: Fully meets policy requirements, no gaps identified
- **⚠️ Partial**: Some requirements met, minor gaps exist, remediation planned
- **❌ Non-Compliant**: Does not meet policy requirements, significant gaps, immediate remediation required
- **N/A**: Not applicable to this system/service (excluded from compliance calculation)

### 5.4 Evidence Requirements

**Assessment Evidence Types**:
- Configuration files and screenshots (TLS settings, encryption settings, certificate configurations)
- System reports (BitLocker status, MDM encryption reports, database TDE status)
- Cloud provider configurations (KMS settings, S3 encryption policies, encryption-at-rest verification)
- Certificate inventories (TLS certificates, code signing certificates, expiration tracking)
- Key management documentation (key rotation logs, escrow verification, HSM/KMS configurations)
- Audit logs (cryptographic operations, key access, certificate lifecycle events)
- Vendor attestations (SOC 2 reports, ISO 27001 certificates for cloud/SaaS providers)

**Evidence Storage**:
- Evidence files stored in [Organization]'s evidence repository
- Evidence naming convention: `EV-[IMP-Section]-[System]-[Date]-[Type].[ext]`
- Evidence retention: Audit cycle + 1 year minimum
- Evidence access control: Restricted to Security Team, System Owners, and Auditors
- Evidence sanitization: Remove sensitive data (encryption keys, passwords) before storage

**Evidence Traceability**:
- Each assessment workbook references evidence file locations
- Evidence Register maintained in IMP-A.8.24 documents
- Evidence linked to specific policy requirements for audit trail

### 5.5 Incident Response

**Cryptographic Incidents** include:
- Compromised cryptographic keys (encryption keys, signing keys, TLS private keys)
- Algorithm vulnerabilities (e.g., POODLE, BEAST, Heartbleed)
- Certificate compromise or unauthorized issuance
- Cryptographic implementation flaws (weak random number generation, implementation bugs)
- Unauthorized key access or key management system breach
- Loss of key escrow/recovery capability

**Incident Response Process**:
1. **Detection**: Security Team identifies cryptographic incident or receives report
2. **Classification**: Assess incident severity based on data classification and scope
3. **Containment**: Revoke compromised keys/certificates, disable affected cryptographic implementations
4. **Eradication**: Replace compromised keys, patch vulnerable implementations, update configurations
5. **Recovery**: Restore cryptographic controls, verify integrity of encrypted data
6. **Lessons Learned**: Document incident, update procedures, improve detection capabilities

**Incident Reporting**:
- All cryptographic incidents reported to CISO within 24 hours
- High-severity incidents (Restricted data exposure risk) escalated to Executive Management immediately
- Regulatory breach notification if incident affects personal data (GDPR Art. 33, nDSG Art. 24)

**Post-Incident Actions**:
- Root cause analysis for all cryptographic incidents
- Assessment of affected systems (determine scope of compromise)
- Remediation plan to prevent recurrence
- Update cryptographic inventory and risk assessment
- Consider policy updates if incident reveals systemic gaps

### 5.6 Continuous Improvement

**Quarterly Cryptographic Review** (Security Team + CISO):
- Review assessment results and compliance trends
- Analyze exception requests and remediation progress
- Monitor algorithm deprecation announcements
- Update ISMS-CTX-A.8.24 (Cryptographic Landscape Reference) as needed
- Identify systemic issues and improvement opportunities

**Annual Policy Review** (CISO + Legal/Compliance):
- Comprehensive policy review against current regulatory landscape
- Update ISMS-POL-A.8.24 for regulatory changes (reference ISMS-POL-00 updates)
- Review cryptographic technology trends and emerging threats
- Assess post-quantum cryptography readiness
- Validate policy remains aligned with organizational risk appetite

**Metrics and KPIs**:
- Overall cryptographic compliance percentage (quarterly trend)
- Mean time to remediate cryptographic gaps (by severity)
- Exception count and age (active exceptions aging analysis)
- Incident count and type (cryptographic incident trends)
- Certificate expiration management (certificates expiring in next 30/60/90 days)
- Algorithm deprecation response time (time from announcement to migration completion)

**Benchmarking and Maturity Assessment**:
- Compare cryptographic maturity against industry standards (CIS Controls, NIST CSF)
- Assess cryptographic capability maturity (ad-hoc → managed → optimized)
- Identify maturity gaps and improvement roadmap
- Align cryptographic improvements with ISMS continuous improvement (ISO 27001 Clause 10)

---

## 6. Related Documents and References

### 6.1 Internal ISMS Documents

**Policy Framework**:
- ISMS-POL-00: Regulatory Applicability Framework (defines Tier 1/2/3 categorization)
- ISO/IEC 27001:2022 Clause 6: Risk Management (cryptographic control selection)
- [Organization] Data Classification Policy (defines Restricted/Confidential/Internal/Public)

**Implementation Guidance (ISMS-IMP-A.8.24 Suite)**:
- ISMS-IMP-A.8.24-1: Data Transmission Assessment (detailed procedures for TLS, VPN, email, protocols)
- ISMS-IMP-A.8.24-2: Data Storage Assessment (encryption-at-rest, cloud encryption, deployment models)
- ISMS-IMP-A.8.24-3: Authentication Assessment (password hashing, MFA, certificates, digital signatures)
- ISMS-IMP-A.8.24-4: Key Management Assessment (key lifecycle, HSM/KMS, rotation, escrow)
- ISMS-IMP-A.8.24-5: Compliance Summary Dashboard (consolidated compliance reporting)

**Technical Reference (Non-ISMS)**:
- ISMS-CTX-A.8.24: Cryptographic Landscape Reference (algorithm tables, cipher suites, key lengths, industry standards)

**Cloud Service Management**:
- ISMS-REF-A.5.23: Cloud Service Provider Registry (cryptographic requirements in vendor evaluation)

### 6.2 External Standards and Frameworks

**Regulatory References** (per ISMS-POL-00):
- Swiss Federal Data Protection Act (nDSG/FADP) - SR 235.1
- EU GDPR - Regulation (EU) 2016/679
- ISO/IEC 27001:2022 - Control A.8.24
- PCI DSS - Payment Card Industry Data Security Standard (if applicable)
- HIPAA - 45 CFR Part 164 (if applicable)
- DORA - Regulation (EU) 2022/2554 (if applicable)
- NIS2 - Directive (EU) 2022/2555 (if applicable)

**Technical Standards** (Informational Reference):
- NIST SP 800-52 Rev. 2: Guidelines for TLS Implementations
- NIST SP 800-57 Part 1 Rev. 5: Recommendation for Key Management
- NIST SP 800-131A Rev. 2: Transitioning the Use of Cryptographic Algorithms
- BSI TR-02102-1: Cryptographic Mechanisms - Recommendations and Key Lengths
- BSI TR-02102-2: Use of Transport Layer Security (TLS)
- IETF RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3
- CA/Browser Forum Baseline Requirements for TLS Certificates

### 6.3 Document Hierarchy
```
ISMS Cryptographic Control Framework

┌─────────────────────────────────────────────────────────────┐
│  ISMS-POL-A.8.24 (THIS DOCUMENT)                           │
│  Policy Requirements (WHAT and WHO)                         │
│  - Data classification-based requirements                   │
│  - Roles and responsibilities                               │
│  - Exception management                                     │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┴───────────────────┬─────────────────────┐
        ▼                                       ▼                     ▼
┌──────────────────┐                 ┌──────────────────┐  ┌──────────────────┐
│  ISMS-IMP-A.8.24 │                 │ ISMS-CTX-A.8.24  │  │  ISMS-POL-00     │
│  Implementation  │                 │ Technical Context │  │  Regulatory      │
│  Guidance (HOW)  │                 │ (Non-ISMS)       │  │  Framework       │
│                  │                 │                  │  │                  │
│  - IMP-1: Data   │                 │ - Algorithm      │  │  - Tier 1/2/3    │
│    Transmission  │                 │   Tables         │  │    Categories    │
│  - IMP-2: Data   │                 │ - Cipher Suites  │  │  - Applicability │
│    Storage       │                 │ - Key Lengths    │  │    Triggers      │
│  - IMP-3: Auth   │                 │ - Industry       │  │                  │
│  - IMP-4: Keys   │                 │   Standards      │  │                  │
│  - IMP-5: Dashboard                │                  │  │                  │
└──────────────────┘                 └──────────────────┘  └──────────────────┘
        │
        ▼
┌──────────────────────────────────────────────────────────────┐
│  Assessment Workbooks (Excel)                                │
│  - Generated via Python scripts                              │
│  - Quarterly compliance verification                         │
│  - Evidence collection and gap analysis                      │
└──────────────────────────────────────────────────────────────┘
```

---

## 7. Policy Maintenance

### 7.1 Review Schedule

**Annual Review** (CISO + Legal/Compliance):
- Comprehensive policy review
- Regulatory landscape assessment (reference ISMS-POL-00 updates)
- Cryptographic technology evolution assessment
- Risk appetite alignment verification
- Executive Management approval of policy updates

**Quarterly Review** (CISO + Security Team):
- Monitor regulatory changes affecting cryptographic requirements
- Review exception inventory and remediation progress
- Assess algorithm deprecation impact
- Update ISMS-POL-00 reference if regulatory tiers change

**Triggered Review**:
- Major regulatory change (new Tier 1 mandatory requirement)
- Significant algorithm deprecation (e.g., TLS 1.2 deprecation announcement)
- Cryptographic incident revealing policy gap
- Organizational changes (merger, acquisition, new service offerings)
- Failed audit findings related to cryptographic policy

### 7.2 Update Process

**Minor Updates** (e.g., clarifications, reference updates):
- CISO approval sufficient
- Update version to X.Y (minor version increment)
- Communicate to System Owners and Security Team
- No re-approval by Executive Management required

**Major Updates** (e.g., new requirements, scope changes, regulatory additions):
- CISO drafts update
- Legal/Compliance review for regulatory impact
- CIO review for operational impact
- Executive Management approval required
- Update version to X.0 (major version increment)
- Communication to all stakeholders
- Training update if significant changes

### 7.3 Communication and Training

**Policy Distribution**:
- Policy portal (primary publication location)
- Email notification to all System Owners upon approval/update
- Security Team briefing on policy changes
- CISO briefing to Executive Management

**Training Requirements**:
- Annual security awareness training includes cryptographic policy overview
- Role-specific training for System Owners (assessment workbook completion)
- Technical training for Security Team (cryptographic implementation guidance)
- New hire onboarding includes cryptographic policy acknowledgment

---

## Approval Record

| Role | Name | Date | Signature |
|------|------|------|-----------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] | __________ |
| **Chief Information Officer (CIO)** | [Name] | [Date] | __________ |
| **Legal/Compliance Officer** | [Name] | [Date] | __________ |
| **Executive Management (GL)** | [Name] | [Date] | __________ |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes cryptographic control requirements. Implementation procedures are documented in ISMS-IMP-A.8.24 suite. Technical reference is available in ISMS-CTX-A.8.24.*