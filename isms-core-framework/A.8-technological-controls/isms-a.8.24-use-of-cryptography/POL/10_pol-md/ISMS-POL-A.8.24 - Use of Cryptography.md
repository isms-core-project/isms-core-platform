**ISMS-POL-A.8.24 — Use of Cryptography**

---

**Document Control**

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
- ISMS-IMP-A.8.24.1-UG/TG (Data Transmission Assessment)
- ISMS-IMP-A.8.24.2-UG/TG (Data Storage Assessment)
- ISMS-IMP-A.8.24.3-UG/TG (Authentication Assessment)
- ISMS-IMP-A.8.24.4-UG/TG (Key Management Assessment)
- ISMS-IMP-A.8.24.5-UG/TG (Compliance Summary Dashboard)
- ISO/IEC 27001:2022 Control A.8.24

---

## Executive Summary

This policy establishes [Organization]'s requirements for cryptographic controls to protect information confidentiality, integrity, and authenticity in accordance with ISO/IEC 27001:2022 Control A.8.24.

**Scope**: This policy applies to all information assets, systems, and personnel handling classified information (Internal, Confidential, or Restricted).

**Purpose**: Define organizational requirements for cryptographic control selection, implementation, and governance. This policy establishes WHAT cryptographic protection is required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8.24 (UG/TG variants).

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS v4.0.1, FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Control A.8.24**

**ISO/IEC 27001:2022 Annex A.8.24 - Use of Cryptography**

> *A policy on the use of cryptographic controls for protection of information should be developed and implemented.*

**Control Objective**: Establish organizational policy for cryptographic controls protecting information throughout its lifecycle.

**This Policy Addresses**:

- Cryptographic control requirements based on data classification
- Organizational roles and responsibilities for cryptographic governance
- Exception and incident management frameworks
- Integration with [Organization]'s risk assessment and treatment processes

## What This Policy Does

This policy:

- **Defines** cryptographic control requirements aligned with data classification
- **Establishes** governance framework for cryptographic decision-making
- **Specifies** accountability for cryptographic control implementation
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Specify technical implementation details** (see ISMS-IMP-A.8.24 Implementation Guides)
- **Define approved algorithms or key lengths** (see ISMS-IMP-A.8.24 Technical Standards)
- **Provide system-specific configuration procedures** (see ISMS-IMP-A.8.24 Assessment Guides)
- **Replace risk assessment** (cryptographic controls selected based on [Organization]'s risk treatment)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite evolving cryptographic standards
- Technical agility for algorithm updates without policy revision
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- All information assets classified as Internal, Confidential, or Restricted
- All systems, applications, networks, and services processing organizational information
- All cryptographic implementations (encryption, hashing, digital signatures, key management)
- All personnel (employees, contractors, third parties) with access to organizational information
- All third-party services handling organizational data

**Out of Scope**:

- Public information (no cryptographic protection required)
- Non-cryptographic security controls (covered by other ISMS policies)

## Regulatory Applicability

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
| **PCI DSS v4.0.1** | Processing payment card data | Strong cryptography for cardholder data, key management controls |
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

# Cryptographic Requirements Framework

## Data Classification-Based Requirements

[Organization] implements cryptographic controls based on data classification as defined in ISMS-POL-A.5.12 (Information Classification Policy).

**Protection Requirements by Classification**:

| Classification | Data in Transit | Data at Rest | Authentication | Key Management |
|----------------|-----------------|--------------|----------------|----------------|
| **Public** | Not required | Not required | Standard | N/A |
| **Internal** | Recommended | Recommended | Standard | Standard |
| **Confidential** | **Required** | **Required** | Strong | Enhanced |
| **Restricted** | **Required (Strong)** | **Required (Strong)** | Strong + MFA | HSM/KMS Required |

**Implementation Note**: Specific cryptographic algorithms, key lengths, and technical configurations are defined in ISMS-IMP-A.8.24 Technical Standards. [Organization] maintains technical standards separately from policy to enable cryptographic agility.

## Cryptographic Control Categories

[Organization] implements cryptographic controls in the following categories:

**Data Transmission Protection**:

- Network communications encryption (TLS/SSL with cipher suites supporting Perfect Forward Secrecy where technically feasible, VPN, wireless)
- Application-level encryption (HTTPS, SFTP, secure email)
- Database connection encryption
- API security

**Data Storage Protection**:

- Full disk encryption (mobile devices, laptops)
- Database encryption (Transparent Data Encryption, column-level)
- Backup encryption (keys stored separately from backup media and production keys per A.8.13 backup segregation requirements. Verification procedure documented in ISMS-IMP-A.8.24-2 Data Storage Assessment and ISMS-IMP-A.8.13 Backup Procedures)
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
Third-party services handling Confidential or Restricted data must demonstrate cryptographic controls equivalent to this policy. Verification occurs during vendor security assessment per ISMS-POL-A.5.19 (Supplier Security Policy).

**Verification Mechanism**: Third-party cryptographic compliance is verified through [Organization]'s vendor security assessment process, which includes questionnaire completion, evidence review, and attestation validation prior to contract execution and annually thereafter.

**Contractual Requirements by Data Classification**:

| Data Classification | Cryptographic Requirement | Evidence Required |
|---------------------|---------------------------|-------------------|
| **Internal** | Encryption in transit recommended | Self-attestation acceptable |
| **Confidential** | Encryption required (transit and rest) | SOC 2 Type II or ISO 27001 certificate |
| **Restricted** | Strong encryption required, HSM/KMS for keys | SOC 2 Type II + penetration test report, or ISO 27001 + independent attestation |

**Acceptable Third-Party Attestations**: SOC 2 Type II (Security Trust Criteria), ISO/IEC 27001 certification, CSA STAR Level 2, or equivalent independent audit. Self-attestation accepted only for Internal classification data.

**Evidence Recency Requirements**:

Third-party cryptographic attestations must cover audit period within:

- **SOC 2 Type II**: Report date within 12 months of [Organization] assessment date. Audit period ending within 18 months acceptable if vendor confirms no material changes.

- **ISO 27001 Certificate**: Certificate validity confirmed via certification body registry. Expired certificates not acceptable.

- **Penetration Test Reports**: Report date within 12 months of assessment.

**Vendor Change Notification**: Contractual requirement for vendors to notify [Organization] within 30 days of material changes to cryptographic implementations, triggering reassessment regardless of annual schedule.

**Implementation Guidance**: Detailed procedures for each category are documented in ISMS-IMP-A.8.24 Implementation Guides (Data Transmission, Data Storage, Authentication, Key Management).

## Cryptographic Agility

[Organization] systems shall be designed to support algorithm replacement without major system re-architecture.

**Requirements**:

- Cryptographic algorithms should be configurable (not hardcoded where feasible)
- Systems should support multiple algorithm versions during migration periods
- [Organization] maintains algorithm lifecycle states (Approved, Deprecated, Prohibited)
- Algorithm deprecation triggers formal migration process
- System Owners receive formal notification minimum 180 days prior to algorithm prohibition to enable migration planning. Critical systems supporting Restricted data receive 270-day advance notice.

**Deprecation Communication Process**:

1. **IT Security Team** publishes algorithm deprecation notice in ISMS-CTX-A.8.24 with timeline
2. **CISO** issues formal communication to all System Owners via [Communication Platform - email/Confluence/SharePoint] with:

   - Affected algorithm details
   - Deprecation timeline (180/270 days)
   - Migration resources (ISMS-IMP-A.8.24 guidance)
   - Acknowledgment request

3. **System Owners** acknowledge receipt within 14 days and submit migration plan within 30 days
4. **IT Security Team** tracks acknowledgments and migration plans in deprecation register

**Non-Acknowledgment Escalation**: System Owners not acknowledging within 14 days receive CISO escalation. Non-response after 30 days triggers Executive Management escalation.

**Rationale**: Cryptographic standards evolve due to cryptanalysis advances, regulatory changes, and post-quantum cryptography migration. Crypto-agile systems reduce risk and cost of algorithm transitions.

**Process**: Algorithm lifecycle management procedures are defined in ISMS-IMP-A.8.24 Technical Standards.

## Certificate Lifecycle Management

[Organization] manages TLS/SSL and other digital certificates in accordance with industry standards and certificate authority requirements.

**Requirements**:

- Public-facing TLS certificates comply with CA/Browser Forum Baseline Requirements for validity periods. As of this policy version, the maximum validity period is 398 days (per CA/Browser Forum Ballot SC31). Current validity requirements are maintained in ISMS-CTX-A.8.24 Technical Reference.
- Internal certificate validity periods are defined in ISMS-IMP-A.8.24 based on risk assessment and operational requirements.
- Certificate renewal processes appropriate to certificate lifetime (automated renewal for short-lived certificates)
- Certificate expiration monitoring and alerting
- Private key protection
- Certificate revocation capability (OCSP/CRL)

**Industry Context**: Certificate lifetime requirements change periodically due to CA/Browser Forum policy updates and browser vendor requirements. [Organization] monitors industry developments and adapts certificate management processes accordingly. Current CA/Browser Forum requirements are tracked in ISMS-CTX-A.8.24.

**Implementation**: Certificate management procedures are defined in ISMS-IMP-A.8.24 Key Management Assessment.

## Prohibited Practices

The following practices are **strictly prohibited**:

- Plaintext storage of passwords or cryptographic keys
- Use of cryptographically broken algorithms (MD5, DES, RC4 for confidentiality)
- Transmission of Confidential or Restricted data without encryption
- Storage of encryption keys alongside encrypted data without separation
- Development of custom cryptographic algorithms without cryptographic expertise
- Bypassing or disabling cryptographic controls without formal exception approval

---

# Governance & Accountability

## Roles & Responsibilities

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

## Assessment & Compliance Verification

**Assessment Approach**: [Organization] conducts cryptographic control assessments using structured methodology covering:

- Data Transmission controls
- Data Storage controls
- Authentication mechanisms
- Key Management practices

**Assessment Frequency**:

- **Initial**: Within 90 days of policy approval or new system deployment
- **Regular**: Annual minimum
- **Triggered**: After significant system changes, security incidents, or algorithm deprecations

**Continuous Monitoring**:

Between scheduled assessments, [Organization] employs automated monitoring for:

- **Prohibited Algorithm Detection**: Weekly vulnerability scans using [Tool Name - to be specified in ISMS-IMP-A.8.24] to detect MD5, DES, RC4, or other prohibited algorithms in production systems. Findings trigger immediate assessment per "Triggered Assessment" criteria above.

- **Certificate Expiration**: Automated monitoring via [Certificate Management System - to be specified] with alerts at 60 days, 30 days, and 7 days prior to expiration. Alert recipients defined in ISMS-IMP-A.8.24-4 (Key Management Assessment).

- **TLS Configuration Drift**: Monthly TLS cipher suite scans to detect configuration changes enabling weak ciphers. Deviations from approved configurations (ISMS-CTX-A.8.24) trigger compliance assessment.

**Monitoring Evidence**: Automated scan logs retained in [Security Information and Event Management (SIEM) system / Evidence Repository - to be specified] for minimum 12 months. Monitoring system operational status verified quarterly by IT Security Team.

**Note**: Specific monitoring tool selection and configuration procedures documented in ISMS-IMP-A.8.24 Implementation Guides to enable technical flexibility without policy revision.

**Significant System Changes** (triggering assessment) include:

- Major version upgrades to cryptographic libraries or TLS implementations
- Migration to new infrastructure (cloud, on-premises, hybrid changes)
- Integration of new third-party services handling Confidential/Restricted data
- Changes to key management infrastructure (HSM/KMS)
- Deployment of new applications processing Confidential/Restricted data
- Algorithm deprecation affecting systems in scope

**Assessment Tools**: [Organization] uses ISMS-IMP-A.8.24 Assessment Workbooks to systematically verify compliance, document evidence, and track remediation.

**Evidence Collection**: Assessments collect the following evidence types:

- **Configuration Evidence**: Screenshots, exports, or configuration files demonstrating cryptographic settings
- **System Reports**: Automated scan results, TLS configuration reports, cipher suite analysis
- **Certificate Inventories**: Complete listing of certificates with expiration dates and key specifications
- **Key Management Records**: Key rotation logs, access control records, HSM audit logs
- **Third-Party Attestations**: Vendor SOC 2 reports, ISO 27001 certificates, security questionnaire responses

**Evidence Sampling Methodology**:

For assessments covering multiple systems:

- **100% Coverage Required**:
  - Certificate inventories (all certificates must be tracked)
  - HSM/KMS access controls (all privileged accounts audited)
  - Prohibited algorithm detection (automated scans provide complete coverage)
  - Systems processing Restricted data (no sampling permitted)

- **Statistical Sampling Permitted**:
  - Configuration evidence for homogeneous system groups (e.g., 30 identical web servers configured from single template)
  - Sample size calculated per ISMS-IMP-A.8.24 Assessment Methodology to achieve 95% confidence level
  - Minimum sample: 10% of population or 5 systems, whichever is greater
  - Non-homogeneous systems require individual assessment

- **Risk-Based Prioritization**: Systems processing Restricted data receive enhanced scrutiny (100% coverage). Systems processing only Internal data may use sampling where automated validation is unavailable.

**Auditor Access**: Full inventory and automated scan results provided to auditors. Sample selection methodology documented in assessment workbook to demonstrate statistical validity.

**Compliance Calculation**: Compliance score = (Implemented Controls / Applicable Controls) x 100%

**Compliance Targets by Data Classification**:

| Data Classification | Minimum Compliance | Target Compliance |
|---------------------|-------------------|-------------------|
| **Internal** | 70% | 85% |
| **Confidential** | 85% | 95% |
| **Restricted** | 95% | 100% |

**Compliance Calculation Methodology**:

- **Required Controls**: Must be implemented for 100% compliance. Non-implementation constitutes policy violation requiring exception approval per Section 3.3.

- **Recommended Controls**: Included in compliance scoring. Systems implementing recommended controls receive credit toward compliance percentage; systems not implementing receive neutral score (neither credit nor violation). Recommended controls enable exceeding minimum compliance thresholds.

- **Compliance Score Formula**:
  - Required Controls Score = (Implemented Required / Total Required) x 100%
  - Recommended Controls Score = (Implemented Recommended / Total Recommended) x 100%
  - Overall Score = (Required Score x 70%) + (Recommended Score x 30%)

- **Example**: System processing Internal data:
  - All Required controls implemented (100% Required Score)
  - No Recommended controls implemented (0% Recommended Score)
  - Overall: (100% x 70%) + (0% x 30%) = 70% (meets minimum threshold)

  Same system with Recommended controls:

  - All Required controls implemented (100% Required Score)
  - All Recommended controls implemented (100% Recommended Score)
  - Overall: (100% x 70%) + (100% x 30%) = 100% (exceeds target)

**Rationale**: "Recommended" status reflects risk-based approach where encryption provides security value but organizational risk tolerance permits exceptions for Internal classification without formal approval process. Required controls address regulatory obligations (Tier 1); Recommended controls address defense-in-depth best practices (Tier 3).

**Evidence Storage**: Assessment evidence is retained in [Organization]'s ISMS evidence repository for minimum 3 years (or regulatory retention period if longer). Evidence is classified as Confidential and access-controlled.

**Non-Compliance Management**: Assessment findings are classified by severity (Critical, High, Medium, Low) with defined remediation timelines. Gaps requiring risk acceptance follow the exception process (Section 3.3).

## Exception Management

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
- **Maximum renewals**: 2 renewals permitted (36 months total maximum exception duration)
- **Third expiration**: After two renewals, exception cannot be extended. System must achieve compliance or be decommissioned. Escalation to Executive Management required.

**Renewal Limit Enforcement**:

Exception tracking system (ISMS Gap Register or equivalent) automatically flags exceptions approaching renewal limits:

- **First Renewal Alert**: 90 days before 12-month expiration
- **Second Renewal Alert**: 60 days before 24-month expiration
- **Final Expiration Notice**: 90 days before 36-month expiration with explicit statement "NO FURTHER RENEWALS PERMITTED"

System Owners receive escalating communications. At 36-month expiration, exception automatically closes and system enters non-compliance status pending remediation or decommissioning.

**Monitoring**: Active exceptions reviewed quarterly by CISO. Compensating control effectiveness verified. Exceptions revoked if risk profile changes or compensating controls fail.

**Exception Template**: ISMS-IMP-A.8.24 Exception Request Form provides standardized documentation format.

## Incident Response

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

## Policy Governance

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

# Implementation & References

## Integration with ISMS

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
- A.8.13 (Information Backup): Backup encryption key storage segregation. A.8.24 defines encryption requirements; A.8.13 defines backup procedures including key-data separation verification
- A.8.15 (Logging): Cryptographic event logging
- A.8.23 (Web Filtering): Secure communications for web traffic

**Stacked Control Integration**:

A.8.24 (Use of Cryptography) stacks with related controls to provide comprehensive protection:

| Stacked Control | Integration Point | A.8.24 Contribution |
|-----------------|-------------------|---------------------|
| **A.5.14** (Information Transfer) | Data transmission security | A.8.24 specifies encryption algorithms; A.5.14 specifies transfer procedures |
| **A.8.20** (Networks Security) | Network encryption | A.8.24 defines TLS/VPN requirements; A.8.20 defines network architecture |
| **A.8.25** (Secure Development Lifecycle) | Application cryptography | A.8.24 defines approved libraries; A.8.25 defines integration into SDLC |

Assessment of A.8.24 should reference stacked control assessments for complete coverage.

## Implementation Resources

**Implementation Document Structure** (ISMS-IMP-A.8.24 Suite):

| Document ID | Title | Purpose | Content |
|-------------|-------|---------|---------|
| **ISMS-IMP-A.8.24-1-UG/TG** | Data Transmission Assessment | Verify encryption controls for data in transit | TLS/SSL configuration, VPN settings, wireless encryption, API security, cipher suite verification |
| **ISMS-IMP-A.8.24-2-UG/TG** | Data Storage Assessment | Verify encryption controls for data at rest | Full disk encryption, database encryption, backup encryption, cloud storage encryption, key separation |
| **ISMS-IMP-A.8.24-3-UG/TG** | Authentication Assessment | Verify cryptographic authentication mechanisms | Password hashing algorithms, MFA implementation, certificate-based authentication, digital signatures |
| **ISMS-IMP-A.8.24-4-UG/TG** | Key Management Assessment | Verify key lifecycle management | Key generation, storage, distribution, rotation, backup, destruction, HSM/KMS configuration |
| **ISMS-IMP-A.8.24-5-UG/TG** | Compliance Summary Dashboard | Consolidated compliance reporting | Aggregated scores across all domains, gap analysis, regulatory mapping, remediation tracking |

**Technical Reference Document** (ISMS-CTX-A.8.24):

ISMS-CTX-A.8.24 (Cryptographic Technical Reference) is established as a non-ISMS technical reference document providing:

- Current approved cryptographic algorithms and key lengths
- TLS/SSL cipher suite configurations and version requirements
- Password hashing parameters (iterations, salt requirements)
- Certificate validity periods and CA/Browser Forum current requirements
- Algorithm deprecation schedules and migration timelines
- Post-quantum cryptography readiness guidance

**Document Control Status**: ISMS-CTX-A.8.24 is NOT subject to ISMS formal document control. This separation enables rapid technical updates without policy change management overhead.

**Governance**: IT Security Team updates ISMS-CTX-A.8.24 as cryptographic standards evolve. CISO reviews semi-annually for accuracy and completeness.

**Rationale**: Cryptographic technical standards change more frequently than policy (algorithm deprecations, new CA/Browser Forum requirements, emerging threats). Separation ensures policy stability while maintaining current technical guidance.

**Version Control & Change Management**:

While ISMS-CTX-A.8.24 is not subject to ISMS formal approval workflow, it maintains:

- **Version Numbering**: Semantic versioning (MAJOR.MINOR.PATCH)
- **Publication Location**: Single authoritative source in [ISMS Repository / Confluence / SharePoint]
- **Change Communication**: Major version changes (algorithm deprecations, cipher suite updates) communicated to all System Owners via [Communication Platform]. Minor/patch changes (clarifications, reference updates) noted in repository changelog.
- **Historical Versions**: Previous versions archived for audit trail. Current version clearly marked.

**Audit Trail**: ISMS-CTX-A.8.24 change log maintained showing date, version, changes, and IT Security Team reviewer.

**Assessment Tools**:

- Excel-based assessment workbooks with automated compliance calculations
- Evidence registers
- Gap analysis templates
- Remediation tracking

## Regulatory Mapping

This policy addresses cryptographic requirements from:

| Requirement Category | Swiss nDSG | EU GDPR | ISO 27001 | PCI DSS v4.0.1* | FINMA* | DORA/NIS2* |
|---------------------|-----------|---------|-----------|---------|--------|------------|
| Encryption at rest | Art. 8 | Art. 32 | A.8.24 | Req. 3.5 | Circ. 2023/1 | ICT Risk Mgmt |
| Encryption in transit | Art. 8 | Art. 32 | A.8.24 | Req. 4.2 | Circ. 2023/1 | Secure Comms |
| Key management | Art. 8 | Art. 32 | A.8.24 | Req. 3.6 | Circ. 2023/1 | Key Controls |
| Algorithm strength | Best Practice | Art. 32 | A.8.24 | Strong Crypto | Risk-Based | Crypto Agility |

*Conditional applicability per ISMS-POL-00

**Note**: Specific regulatory interpretation and compliance verification procedures are documented in ISMS-IMP-A.8.24 Compliance Summary Dashboard.

## Training & Awareness

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

# Definitions

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

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for use of cryptography. Implementation procedures are documented in ISMS-IMP-A.8.24 (UG/TG).*

<!-- QA_VERIFIED: 2026-02-02 -->