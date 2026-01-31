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
- ISMS-IMP-A.8.24 (Implementation Guidance Suite)
- ISO/IEC 27001:2022 Control A.8.24

---

## Executive Summary

This policy establishes [Organization]'s requirements for cryptographic controls to protect information confidentiality, integrity, and authenticity in accordance with ISO/IEC 27001:2022 Control A.8.24.

**Scope**: This policy applies to all information assets, systems, and personnel handling classified information (Internal, Confidential, or Restricted).

**Purpose**: Define organizational requirements for cryptographic control selection, implementation, and governance. This policy establishes WHAT cryptographic protection is required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8.24.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS, FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.24

**ISO/IEC 27001:2022 Annex A.8.24 - Use of Cryptography**

> *A policy on the use of cryptographic controls for protection of information should be developed and implemented.*

**Control Objective**: Establish organizational policy for cryptographic controls protecting information throughout its lifecycle.

**This Policy Addresses**:
- Cryptographic control requirements based on data classification
- Organizational roles and responsibilities for cryptographic governance
- Exception and incident management frameworks
- Integration with [Organization]'s risk assessment and treatment processes

### 1.2 What This Policy Does

This policy:
- **Defines** cryptographic control requirements aligned with data classification
- **Establishes** governance framework for cryptographic decision-making
- **Specifies** accountability for cryptographic control implementation
- **References** applicable regulatory requirements per ISMS-POL-00

### 1.3 What This Policy Does NOT Do

This policy does NOT:
- **Specify technical implementation details** (see ISMS-IMP-A.8.24 Implementation Guides)
- **Define approved algorithms or key lengths** (see ISMS-IMP-A.8.24 Technical Standards)
- **Provide system-specific configuration procedures** (see ISMS-IMP-A.8.24 Assessment Guides)
- **Replace risk assessment** (cryptographic controls selected based on [Organization]'s risk treatment)

**Rationale**: Separating policy requirements from implementation guidance enables:
- Policy stability despite evolving cryptographic standards
- Technical agility for algorithm updates without policy revision
- Clear distinction between governance (policy) and execution (implementation)

### 1.4 Scope

**This policy applies to**:
- All information assets classified as Internal, Confidential, or Restricted
- All systems, applications, networks, and services processing organizational information
- All cryptographic implementations (encryption, hashing, digital signatures, key management)
- All personnel (employees, contractors, third parties) with access to organizational information
- All third-party services handling organizational data

**Out of Scope**:
- Public information (no cryptographic protection required)
- Non-cryptographic security controls (covered by other ISMS policies)

### 1.5 Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**. 

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG** | All Swiss operations | Art. 8 - Appropriate technical measures including encryption |
| **EU GDPR** | When processing EU personal data | Art. 32 - Encryption of personal data as security measure |
| **ISO/IEC 27001:2022** | Certification scope | Control A.8.24 - Documented policy and implementation |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Cryptographic Requirements |
|-----------|-------------------|----------------------------|
| **PCI DSS v4.0** | Processing payment card data | Strong cryptography for cardholder data, key management controls |
| **FINMA** | Swiss regulated financial institution | Encryption per FINMA Circular 2023/1 Margin 62 |
| **DORA** | EU financial services entity | ICT system encryption, crypto agility |
| **NIS2** | Essential/important entity (EU) | Encryption as cybersecurity risk management measure |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- NIST SP 800-57 (Key Management)
- BSI TR-02102 (Cryptographic Mechanisms)
- ENISA (Algorithms and Key Sizes)
- OWASP (Cryptographic Storage)

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent requirements apply where multiple regulations overlap.

---

## 2. Cryptographic Requirements Framework

### 2.1 Data Classification-Based Requirements

[Organization] implements cryptographic controls based on data classification as defined in ISMS-POL-A.5.12 (Information Classification Policy).

**Protection Requirements by Classification**:

| Classification | Data in Transit | Data at Rest | Authentication | Key Management |
|----------------|-----------------|--------------|----------------|----------------|
| **Public** | Not required | Not required | Standard | N/A |
| **Internal** | Recommended | Recommended | Standard | Standard |
| **Confidential** | **Required** | **Required** | Strong | Enhanced |
| **Restricted** | **Required (Strong)** | **Required (Strong)** | Strong + MFA | HSM/KMS Required |

**Implementation Note**: Specific cryptographic algorithms, key lengths, and technical configurations are defined in ISMS-IMP-A.8.24 Technical Standards. [Organization] maintains technical standards separately from policy to enable cryptographic agility.

### 2.2 Cryptographic Control Categories

[Organization] implements cryptographic controls in the following categories:

**Data Transmission Protection**:
- Network communications encryption (TLS/SSL with cipher suites supporting Perfect Forward Secrecy where technically feasible, VPN, wireless)
- Application-level encryption (HTTPS, SFTP, secure email)
- Database connection encryption
- API security

**Data Storage Protection**:
- Full disk encryption (mobile devices, laptops)
- Database encryption (Transparent Data Encryption, column-level)
- Backup encryption (keys stored separately from backup media and production keys)
- Cloud storage encryption
- Removable media encryption

**Authentication & Identity**:
- Password hashing (not plaintext storage)
- Multi-factor authentication mechanisms
- Digital signatures
- Certificate-based authentication

**Key Management**:
- Cryptographic key lifecycle (generation, storage, distribution, rotation, destruction)
- Key-data separation
- Hardware Security Modules (HSM) or Key Management Services (KMS) for high-security keys

**Third-Party Cryptographic Requirements**: 
Third-party services handling Confidential or Restricted data must demonstrate cryptographic controls equivalent to this policy. Verification occurs during vendor security assessment per ISMS-POL-A.5.19 (Supplier Security Policy). Contractual requirements are defined based on data classification.

**Implementation Guidance**: Detailed procedures for each category are documented in ISMS-IMP-A.8.24 Implementation Guides (Data Transmission, Data Storage, Authentication, Key Management).

### 2.3 Cryptographic Agility

[Organization] systems shall be designed to support algorithm replacement without major system re-architecture.

**Requirements**:
- Cryptographic algorithms should be configurable (not hardcoded where feasible)
- Systems should support multiple algorithm versions during migration periods
- [Organization] maintains algorithm lifecycle states (Approved, Deprecated, Prohibited)
- Algorithm deprecation triggers formal migration process
- System Owners receive formal notification minimum 180 days prior to algorithm prohibition to enable migration planning. Critical systems supporting Restricted data receive 270-day advance notice.

**Rationale**: Cryptographic standards evolve due to cryptanalysis advances, regulatory changes, and post-quantum cryptography migration. Crypto-agile systems reduce risk and cost of algorithm transitions.

**Process**: Algorithm lifecycle management procedures are defined in ISMS-IMP-A.8.24 Technical Standards.

### 2.4 Certificate Lifecycle Management

[Organization] manages TLS/SSL and other digital certificates in accordance with industry standards and certificate authority requirements.

**Requirements**:
- Public-facing TLS certificates comply with CA/Browser Forum Baseline Requirements for validity periods. Internal certificate validity periods are defined in ISMS-IMP-A.8.24 based on risk assessment and operational requirements.
- Certificate renewal processes appropriate to certificate lifetime (automated renewal for short-lived certificates)
- Certificate expiration monitoring and alerting
- Private key protection
- Certificate revocation capability (OCSP/CRL)

**Industry Context**: Certificate lifetime requirements change periodically due to CA/Browser Forum policy updates and browser vendor requirements. [Organization] monitors industry developments and adapts certificate management processes accordingly.

**Implementation**: Certificate management procedures are defined in ISMS-IMP-A.8.24 Key Management Assessment.

### 2.5 Prohibited Practices

The following practices are **strictly prohibited**:
- Plaintext storage of passwords or cryptographic keys
- Use of cryptographically broken algorithms (MD5, DES, RC4 for confidentiality)
- Transmission of Confidential or Restricted data without encryption
- Storage of encryption keys alongside encrypted data without separation
- Development of custom cryptographic algorithms without cryptographic expertise
- Bypassing or disabling cryptographic controls without formal exception approval

---

## 3. Governance & Accountability

### 3.1 Roles & Responsibilities

**Chief Information Security Officer (CISO)**:
- Policy ownership and strategic direction
- Cryptographic exception approvals (technical)
- Regulatory compliance oversight
- Algorithm deprecation authority

**Information Security Manager**:
- Day-to-day policy implementation coordination
- Technical guidance to System Owners
- Assessment program management
- Incident coordination

**System Owners**:
- Cryptographic control implementation for their systems
- Risk assessment participation
- Assessment and audit participation
- Remediation plan execution

**IT Security Team**:
- Technical implementation support
- Key management infrastructure (HSM/KMS)
- Cryptographic assessment execution
- Algorithm monitoring

**Development Teams**:
- Secure cryptographic implementation in applications
- Use of approved cryptographic libraries
- Security code review participation
- Vulnerability remediation

**Legal/Compliance**:
- Regulatory requirement interpretation
- External audit coordination
- Regulatory notification (if incidents occur)

**Key Ownership vs System Ownership**:

[Organization] distinguishes between:
- **Key Owners**: Authorize key creation and define key usage policies (governance)
- **Key Custodians**: Execute physical key management operations (HSM administration, key generation)
- **System Owners**: Operate systems using keys (do not manage keys directly)

This separation ensures accountability, segregation of duties, and clear audit trails.

### 3.2 Assessment & Compliance Verification

**Assessment Approach**: [Organization] conducts cryptographic control assessments using structured methodology covering:
- Data Transmission controls
- Data Storage controls
- Authentication mechanisms
- Key Management practices

**Assessment Frequency**:
- **Initial**: Within 90 days of policy approval or new system deployment
- **Regular**: Annual minimum
- **Triggered**: After significant system changes, security incidents, or algorithm deprecations

**Assessment Tools**: [Organization] uses ISMS-IMP-A.8.24 Assessment Workbooks to systematically verify compliance, document evidence, and track remediation.

**Non-Compliance Management**: Assessment findings are classified by severity (Critical, High, Medium, Low) with defined remediation timelines. Gaps requiring risk acceptance follow the exception process (Section 3.3).

### 3.3 Exception Management

**Exception Request Requirements**:

Exceptions to cryptographic policy requirements require:
- Documented business or technical justification
- Risk assessment (likelihood, impact, residual risk)
- Compensating controls (where feasible)
- Timeline for achieving full compliance
- Formal approval per authority matrix

**Approval Authority**:
- **Technical exceptions** (algorithm, configuration): CISO approval
- **Policy-level exceptions** (requirement waiver): Executive Management approval
- **Maximum duration**: 12 months
- **Renewal**: Requires updated risk assessment and justification

**Monitoring**: Active exceptions reviewed quarterly by CISO. Compensating control effectiveness verified. Exceptions revoked if risk profile changes or compensating controls fail.

**Exception Template**: ISMS-IMP-A.8.24 Exception Request Form provides standardized documentation format.

### 3.4 Incident Response

**Cryptographic Incidents** include:
- Key compromise or suspected compromise
- Certificate private key exposure
- Unauthorized access to encrypted data
- Discovery of prohibited algorithms in production
- Cryptographic control failures

**Severity Classification**:
- **Critical**: Confirmed compromise of production encryption keys, certificate private keys, or HSM/KMS access credentials. Response: 4 hours.
- **High**: Suspected key compromise, discovery of prohibited algorithms protecting Confidential/Restricted data, or cryptographic control failure affecting multiple systems. Response: 24 hours.
- **Medium**: Discovery of deprecated algorithms, certificate expiration causing service disruption, or isolated control failures. Response: 48 hours.
- **Low**: Policy deviations without active exploitation, minor configuration drift. Response: 72 hours.

If response timelines cannot be met, escalate to CISO (for High/Medium/Low severity) or CEO (for Critical severity) within the original timeline window.

**Response Process**:
1. **Detection & Reporting**: Immediate notification to IT Security Team
2. **Assessment**: Severity determination (Critical, High, Medium, Low)
3. **Containment**: Key rotation timeline based on severity (4 hours to 72 hours)
4. **Recovery**: New key generation, data re-encryption, system updates
5. **Post-Incident**: Root cause analysis, preventive measures, regulatory notification (if applicable)

**Detailed Procedures**: ISMS-IMP-A.8.24 Incident Response Guide provides incident classification criteria, response workflows, and regulatory notification requirements.

### 3.5 Policy Governance

**Policy Review**:
- **Frequency**: Annual minimum
- **Triggers**: Regulatory changes, major incidents, algorithm deprecations, CA/Browser Forum baseline changes, organizational changes
- **Reviewers**: CISO, IT Security Team, Legal/Compliance, selected System Owners
- **Approval**: CISO (technical), Executive Management (strategic)

**Technical Standards Review**:
- **Frequency**: Semi-annual (cryptographic landscape evolves rapidly)
- **Authority**: IT Security Team proposes updates, CISO approves
- **Note**: Technical standard updates (ISMS-IMP-A.8.24) do not require policy revision

**Policy Updates**:
- **Minor** (clarifications, references): CISO approval, 30-day communication
- **Major** (scope changes, new requirements): Full approval chain, 90-day implementation
- **Emergency** (critical vulnerabilities): CISO approval, immediate communication

**Communication**: Policy published in ISMS document repository. Changes communicated organization-wide. Training provided for significant changes.

---

## 4. Implementation & References

### 4.1 Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):
- Cryptographic controls selected based on [Organization]'s risk assessment
- Data classification determines minimum cryptographic requirements
- Risk treatment plans document cryptographic control implementation

**Statement of Applicability** (ISO 27001 Clause 6.1.3):
- Control A.8.24 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported

**Related Controls**:
- A.5.10 (Acceptable Use of Information): Defines data classification
- A.5.14 (Information Transfer): Encryption requirements for data transmission
- A.5.15 (Access Control): Integrates with key access controls
- A.8.9 (Configuration Management): Cryptographic configuration management
- A.8.15 (Logging): Cryptographic event logging
- A.8.23 (Web Filtering): Secure communications for web traffic

### 4.2 Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.8.24 Suite):
- Data Transmission Assessment: TLS/SSL, VPN, wireless, API encryption
- Data Storage Assessment: Disk, database, backup, cloud encryption
- Authentication Assessment: Password hashing, MFA, certificates
- Key Management Assessment: Key lifecycle, HSM/KMS, access controls
- Compliance Summary Dashboard: Consolidated compliance reporting

**Technical Standards**:
- Approved cryptographic algorithms and key lengths
- TLS/SSL cipher suite configurations
- Password hashing parameters
- Certificate validity and lifecycle requirements
- Algorithm deprecation schedules

**Assessment Tools**:
- Excel-based assessment workbooks with automated compliance calculations
- Evidence registers
- Gap analysis templates
- Remediation tracking

### 4.3 Regulatory Mapping

This policy addresses cryptographic requirements from:

| Requirement Category | Swiss nDSG | EU GDPR | ISO 27001 | PCI DSS* | FINMA* | DORA/NIS2* |
|---------------------|-----------|---------|-----------|---------|--------|------------|
| Encryption at rest | Art. 8 | Art. 32 | A.8.24 | Req. 3.5 | Circ. 2023/1 | ICT Risk Mgmt |
| Encryption in transit | Art. 8 | Art. 32 | A.8.24 | Req. 4.2 | Circ. 2023/1 | Secure Comms |
| Key management | Art. 8 | Art. 32 | A.8.24 | Req. 3.6 | Circ. 2023/1 | Key Controls |
| Algorithm strength | Best Practice | Art. 32 | A.8.24 | Strong Crypto | Risk-Based | Crypto Agility |

*Conditional applicability per ISMS-POL-00

**Note**: Specific regulatory interpretation and compliance verification procedures are documented in ISMS-IMP-A.8.24 Compliance Summary Dashboard.

### 4.4 Training & Awareness

**Security Awareness** (All Personnel):
- Annual training module on cryptographic controls
- Data classification and encryption requirements
- Incident reporting procedures

**Technical Training** (Developers, IT Staff):
- Secure cryptographic implementation
- Approved cryptographic libraries and APIs
- Common cryptographic vulnerabilities

**Operational Training** (IT Operations):
- Key management procedures
- Certificate lifecycle management
- Cryptographic incident response

---

## 5. Definitions

**Cryptographic Control**: Hardware or software mechanism using cryptographic algorithms to protect information confidentiality, integrity, or authenticity.

**Approved Algorithm**: Cryptographic algorithm meeting [Organization]'s security standards as defined in ISMS-IMP-A.8.24 Technical Standards.

**Key Management**: Processes for cryptographic key lifecycle including generation, storage, distribution, rotation, backup, and destruction.

**Hardware Security Module (HSM)**: Tamper-resistant hardware device for secure cryptographic key storage and operations.

**Key Management Service (KMS)**: Software or cloud service for centralized cryptographic key management.

**Crypto Agility**: Organizational capability to rapidly change cryptographic algorithms without major system re-architecture.

**Data Classification**: [Organization]'s categorization of information based on confidentiality, integrity, and availability requirements (Public, Internal, Confidential, Restricted).

**Perfect Forward Secrecy (PFS)**: Cryptographic property where compromise of long-term keys does not compromise past session keys.

**Certificate Authority (CA)**: Trusted entity issuing digital certificates for public key infrastructure.

---

## Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements. Implementation procedures are documented in ISMS-IMP-A.8.24.*