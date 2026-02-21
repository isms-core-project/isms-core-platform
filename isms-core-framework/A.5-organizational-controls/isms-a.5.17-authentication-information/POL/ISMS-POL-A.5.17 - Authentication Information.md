<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.17:framework:POL:a.5.17 -->
**ISMS-POL-A.5.17 — Authentication Information**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Authentication Information |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.17 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.15-16-18 (Identity & Access Management)
- ISMS-POL-A.8.2-3-5 (Authentication & Privileged Access)
- ISMS-POL-A.8.24 (Use of Cryptography)
- ISMS-IMP-A.5.17.1-UG/TG (Password Policy Implementation Guide)
- ISMS-IMP-A.5.17.2-UG/TG (MFA Deployment Assessment)
- ISMS-IMP-A.5.17.3-UG/TG (Authentication Management Procedures)
- ISMS-IMP-A.5.17.4-UG/TG (Compliance and Audit Dashboard)
- ISMS-IMP-A.5.17.5-UG/TG (Consolidation Dashboard)
- ISO/IEC 27001:2022 Control A.5.17

---

## Executive Summary

This policy establishes [Organization]'s requirements for the management and protection of authentication information to prevent unauthorized access to information systems and data.

**Scope**: This policy applies to all authentication information including passwords, PINs, cryptographic keys, tokens, biometric templates, and other authentication secrets used to access [Organization]'s systems and data.

**Purpose**: Define organizational requirements for authentication information management. This policy establishes WHAT authentication controls are required and WHO is responsible. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.17 (UG/TG variants).

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, PCI DSS v4.0.1, NIS2, DORA) apply where [Organization]'s business activities trigger applicability.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Control A.5.17**

**ISO/IEC 27001:2022 Annex A.5.17 - Authentication Information**

Authentication information is issued, managed, protected, and revoked through defined lifecycle processes. Personnel are instructed on secure handling and must follow documented requirements for confidentiality and reporting of compromise.

**Control Objectives**:

- Ensure authentication information is securely allocated through verified processes
- Protect authentication information throughout its lifecycle
- Prevent unauthorized access through credential compromise
- Maintain accountability for authentication credential usage

**Control Type**: Preventive
**Control Category**: Organizational

**This Policy Addresses**:

- Authentication information allocation and distribution
- Password requirements and complexity standards
- Multi-factor authentication requirements
- Protection and handling of authentication secrets
- Password reset and recovery procedures

## What This Policy Does

This policy:

- **Defines** requirements for secure allocation of authentication information
- **Establishes** password complexity and lifecycle standards
- **Specifies** multi-factor authentication requirements by access type
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Specify authentication mechanism technical implementation** (see ISMS-POL-A.8.2-3-5 and ISMS-IMP-A.5.17)
- **Define privileged access management procedures** (see ISMS-POL-A.8.2-3-5)
- **Provide cryptographic key management infrastructure details** (see ISMS-POL-A.8.24)
- **Detail identity lifecycle management** (see ISMS-POL-A.5.15-16-18)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite technology or platform changes
- Flexibility for different authentication solutions
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- All authentication information (passwords, PINs, tokens, keys, biometrics)
- All information systems, applications, network devices, cloud services, and databases
- All personnel (employees, contractors, third parties) with system access
- All authentication processes (allocation, management, reset, revocation)

**Out of Scope**:

- Personal accounts unrelated to organizational systems
- Authentication mechanism design and engineering (covered by A.8.5)
- Cryptographic key management lifecycle (key generation standards, cryptographic parameters, HSM/KMS controls, enterprise PKI operations) - governed by ISMS-POL-A.8.24

**Scope Boundary Clarification**: This policy covers issuance, storage/handling, access control, rotation/revocation triggers, and logging for authentication secrets (including API keys and certificates used for authentication). Cryptographic key management lifecycle controls are governed by ISMS-POL-A.8.24; authentication mechanism implementation is governed by ISMS-POL-A.8.2-3-5.

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG Art. 8** | All personal data processing | Technical measures for data protection |
| **ISO/IEC 27001:2022** | Certification scope | Control A.5.17 - Authentication information |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Authentication Requirements |
|-----------|-------------------|----------------------------|
| **EU GDPR Art. 32** | Processing EU personal data | Appropriate security measures including authentication |
| **FINMA** | Swiss regulated financial institution | Enhanced authentication for financial systems |
| **PCI DSS v4.0.1** | Payment card processing | Requirement 8 - Strong authentication |
| **NIS2** | Essential/important entity (EU) | Strong authentication requirements |
| **DORA** | EU financial services entity | ICT security including authentication controls |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- NIST SP 800-63B (Digital Identity Guidelines - Authentication)
- CIS Controls v8.1 (Control 5 - Account Management, Control 6 - Access Control)
- OWASP Authentication Guidelines
- Microsoft Security Baseline recommendations

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent authentication requirements apply where multiple regulations overlap.

---

# Policy Statements

## Authentication Information Allocation

### Initial Allocation Requirements

[Organization] SHALL allocate authentication information through controlled processes:

**Identity Verification**:

- Verify user identity before issuing authentication credentials
- Use out-of-band verification for sensitive system access
- Document verification method used for audit trail

**Secure Distribution**:

| Authentication Type | Distribution Method |
|--------------------|---------------------|
| **Initial Passwords** | Secure channel, separate from username, forced change on first use |
| **Tokens/Hardware** | In-person handover with identity verification, signed receipt |
| **Certificates** | Secure certificate enrollment process, verified email |
| **API Keys** | Encrypted channel, limited validity, logged issuance |

**Temporary Authentication**:

- Temporary authentication information SHALL have maximum 24-hour validity
- Users SHALL be required to change temporary credentials on first use
- System SHALL enforce expiration of temporary credentials

### Default Credential Management

[Organization] SHALL NOT use default authentication information:

- All vendor/manufacturer default passwords SHALL be changed before production deployment
- Default accounts SHALL be disabled or renamed where technically feasible
- Default credential change verification SHALL be included in system commissioning checklist

**"Not Technically Feasible" Conditions**: Default account cannot be disabled/renamed when: (1) vendor firmware/support requires the account, (2) system lacks functionality to rename, (3) disabling breaks critical functionality. Where not feasible, mandatory compensating controls apply: unique strong password per device, network segmentation restricting access, MFA where supported, enhanced monitoring/alerting, vaulting of credentials, and documented exception in ISMS-REG-EXCEPTIONS.

## Password Requirements

### Password Complexity Standards

[Organization] SHALL enforce the following password requirements:

| Requirement | Standard Access | Privileged Access | Service Accounts |
|-------------|-----------------|-------------------|------------------|
| **Minimum Length** | 12 characters | 16 characters | 24 characters |
| **Complexity** | 3 of 4 character types | 4 of 4 character types | Complex + random |
| **History** | 12 passwords remembered | 24 passwords remembered | N/A (single use) |
| **Maximum Age** | 90 days | 60 days | 90 days or certificate-based |
| **Lockout Threshold** | 5 failed attempts | 3 failed attempts | Alert on single failure |

**Character Types**: Uppercase, lowercase, numbers, special characters.

**Password Age Justification**: Time-based rotation is supplemented by event-based rotation triggers: (1) suspected compromise, (2) shared credential discovery, (3) absence of MFA protection, (4) personnel role change affecting access scope. Where strong MFA and continuous monitoring are verified, rotation may be extended via documented exception with CISO approval. The specified intervals (60/90 days) reflect [Organization]'s risk treatment decisions balancing security with usability.

### Prohibited Password Practices

Personnel SHALL NOT:

- Share passwords with any other person (including IT support)
- Write passwords in unprotected locations
- Store passwords in plaintext files or documents
- Use the same password across multiple systems
- Use passwords based on easily guessable information (names, dates, dictionary words)
- Transmit passwords via unencrypted channels

### Password Storage

[Organization] SHALL store passwords securely:

- Passwords SHALL be stored using approved one-way cryptographic hashing with salt
- Password hashing algorithms: bcrypt, Argon2, PBKDF2 (with appropriate parameters)
- Plaintext password storage is PROHIBITED
- Password databases SHALL be protected with encryption at rest

## Multi-Factor Authentication

### MFA Requirements

[Organization] SHALL require multi-factor authentication for:

| Access Type | MFA Requirement |
|-------------|-----------------|
| **Remote Access** (VPN, cloud) | Mandatory |
| **Privileged/Admin Access** | Mandatory |
| **Critical Systems** | Mandatory |
| **Customer Data Access** | Mandatory |
| **Email (external access)** | Mandatory |
| **Standard Internal Access** | Risk-based per system tiering in ISMS-IMP-A.5.17; decisions recorded in IdP conditional access policy; coverage reviewed quarterly |

### MFA Factor Types

Acceptable authentication factors:

| Factor Category | Examples | Requirements |
|-----------------|----------|--------------|
| **Something You Know** | Password, PIN, passphrase | Per password requirements |
| **Something You Have** | Hardware token, mobile authenticator, smart card | Registered to individual user |
| **Something You Are** | Fingerprint, facial recognition | Biometric template securely stored |

MFA implementations SHALL use factors from at least two different categories.

## Authentication Information Protection

### User Responsibilities

All personnel SHALL:

- Keep authentication information confidential
- Use strong, unique passwords for each system
- Report suspected compromise immediately
- Not allow others to use their credentials
- Change passwords immediately if compromise suspected
- Use approved password managers for secure storage

### System Requirements

Systems SHALL:

- Mask password entry on screens
- Not display previously used passwords
- Encrypt authentication traffic in transit
- Log authentication events (success and failure)
- Alert on authentication anomalies
- Implement account lockout after failed attempts

### Shared Authentication Information

Shared authentication information is DISCOURAGED. Where required:

- CISO approval mandatory with documented business justification
- Storage in approved credential vault (not plaintext documents/email/chat)
- Named custodian assigned for each shared credential
- Check-out logging with user identification and timestamp
- Session recording for privileged shared accounts where technically feasible
- Individual accountability maintained through audit logging
- Quarterly review of access and usage; annual reauthorization required
- Procedures documented in ISMS-IMP-A.5.17

## Password Reset and Recovery

### Self-Service Password Reset

Where implemented, self-service password reset SHALL:

- Require MFA-based verification (authenticator push, FIDO2, hardware token) for privileged accounts, remote access, and critical systems
- Knowledge-based security questions are prohibited unless approved as an exception with documented compensating controls
- Email/SMS verification may only be used for low-risk accounts where approved in the system risk assessment and where additional monitoring is in place
- Use time-limited reset tokens (maximum 1 hour validity)
- Log all reset activities including verification method used
- Alert user of password change via registered contact
- Not reveal whether account exists

### Assisted Password Reset

Helpdesk-assisted password resets SHALL:

- Verify user identity using pre-registered information
- Generate temporary password with forced change
- Document reset request and verification method
- Communicate new password via secure channel
- Not reveal passwords to support personnel after issuance

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Authentication Responsibilities |
|------|--------------------------------|
| **Executive Management** | Approve authentication policy, provide resources for implementation |
| **CISO** | Policy ownership, MFA strategy, exception approval |
| **IT Operations** | Technical implementation, system configuration, password infrastructure |
| **IAM Team** | User provisioning, credential issuance, reset procedures |
| **Helpdesk** | Assisted password reset, identity verification |
| **System Owners** | System-specific authentication configuration, compliance verification |
| **All Personnel** | Credential protection, compliance with policy, incident reporting |

## Escalation Path

- Authentication policy questions: Personnel → IAM Team → CISO
- Exception requests: Requestor → Manager → CISO
- Authentication incident: Personnel → Security Team → CISO → Executive Management

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| Password policy compliance | Monthly | IT Operations | System configuration audit |
| MFA coverage verification | Quarterly | Security Team | Access system reports |
| Authentication log review | Monthly | Security Team | SIEM analysis reports |
| Default credential scan | Quarterly | Security Team | Vulnerability scan results |
| User awareness verification | Annual | HR | Training completion records |

**Governance Metrics**:

- MFA adoption rate (target: 100% for mandatory systems)
- Password policy compliance rate (target: >98%)
- Average password age distribution
- Failed authentication patterns
- Password reset request volume and resolution time
- Default credential findings count (target: 0)

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Authentication technology changes, security incidents, regulatory updates
- **Reviewers**: CISO, IT Operations, IAM Team
- **Approval**: Executive Management

## Exception Management

**Permitted Exceptions**:

- Legacy systems unable to meet password complexity (with documented mitigation)
- Systems incompatible with MFA (with compensating controls)
- Service accounts requiring different password policies (with enhanced monitoring)

**Exception Process**:

1. Document business justification
2. Security Team risk assessment
3. CISO approval with compensating controls
4. Time-limited approval (maximum 90 days, renewable)
5. Documentation in exception register

**Not Permissible**:

- Exceptions permitting password sharing without accountability
- Exceptions eliminating MFA for privileged access
- Exceptions allowing default credentials in production

All exceptions SHALL be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

## Corrective Action Linkage

Nonconformities related to this policy (e.g., weak password configurations, MFA gaps, credential compromise, default credential findings) SHALL be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Authentication controls selected based on [Organization]'s risk assessment
- Credential compromise threats inform password and MFA requirements
- Risk treatment plans document authentication control implementation

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Control A.5.17 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported

**Related Controls**:

| Control | Relationship |
|---------|--------------|
| **A.5.15-16-18** | IAM defines identities; A.5.17 protects their authentication |
| **A.8.2-3-5** | Privileged access requires stricter authentication |
| **A.8.24** | Cryptographic protection of authentication information |
| **A.8.12** | DLP detects credential leakage |
| **A.8.15** | Logging of authentication events |

**Stacked Control Integration**:

A.5.17 (Authentication Information) stacks with related controls to provide comprehensive protection:

| Stacked Control | Integration Point | A.5.17 Contribution |
|-----------------|-------------------|---------------------|
| **A.5.15-16-18** (IAM) | Identity lifecycle | A.5.17 protects credentials; IAM manages identities |
| **A.8.2-3-5** (Privileged Access) | Admin authentication | A.5.17 sets standards; A.8.2 enforces stricter requirements |
| **A.8.24** (Cryptography) | Password protection | A.5.17 mandates hashing; A.8.24 specifies algorithms |

Assessment of A.5.17 should reference stacked control assessments for complete coverage.

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.5.17 Suite):

| Document ID | Title | Purpose |
|-------------|-------|---------|
| **ISMS-IMP-A.5.17.1-UG/TG** | Password Policy Implementation Guide | Technical configuration procedures |
| **ISMS-IMP-A.5.17.2-UG/TG** | MFA Deployment Assessment | MFA rollout and verification |
| **ISMS-IMP-A.5.17.3-UG/TG** | Authentication Management Procedures | Operational procedures for credential lifecycle |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Required Stage 1 evidence includes:

- ✅ This policy document (ISMS-POL-A.5.17 v1.0)
- ✅ Recorded approval by CISO, CIO, Executive Management
- ✅ Evidence of communication to relevant roles
- ✅ Password complexity standards defined (Password Requirements)
- ✅ MFA requirements specified (Multi-Factor Authentication)
- ✅ Initial allocation procedures documented (Authentication Information Allocation)
- ✅ Reset/recovery procedures defined (Password Reset and Recovery)
- ✅ User responsibilities specified (Authentication Information Protection)
- ✅ Roles and responsibilities assigned (Roles and Responsibilities)

Evidence status is tracked in the ISMS Evidence Register.

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Password policy configuration exports showing complexity, history, lockout settings
- MFA deployment reports showing coverage for mandatory access types
- Authentication logs showing event logging and anomaly detection
- Password reset records with identity verification documentation
- Default credential scan results showing no default credentials
- Training completion records for authentication awareness
- Exception register with CISO approval and compensating controls
- Authentication incident reports and resolution documentation

---

# Definitions

| Term | Definition |
|------|------------|
| **Authentication Information** | Data used to prove identity, including passwords, tokens, keys, biometrics |
| **Multi-Factor Authentication (MFA)** | Authentication requiring two or more verification factors from different categories |
| **Password Hash** | One-way cryptographic representation of a password |
| **Salt** | Random data added to passwords before hashing to prevent rainbow table attacks |
| **Out-of-Band Verification** | Identity verification using a separate communication channel |
| **Brute Force Attack** | Attempt to guess credentials through systematic trial |
| **Credential Stuffing** | Attack using leaked credentials from other breaches |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Chief Information Officer (CIO)** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for authentication information management. Implementation procedures are documented in ISMS-IMP-A.5.17 (UG/TG).*

<!-- QA_VERIFIED: 2026-02-04 -->
