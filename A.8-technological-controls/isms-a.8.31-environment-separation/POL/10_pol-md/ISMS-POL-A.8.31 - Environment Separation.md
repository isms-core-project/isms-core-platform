**ISMS-POL-A.8.31 - Separation of Development, Test and Production Environments**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Separation of Development, Test and Production Environments |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.31 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / IT Operations | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

---

# Executive Summary

This policy establishes [Organization]'s requirements for separating development, test, and production environments to reduce risks associated with unauthorized changes and data exposure in accordance with ISO/IEC 27001:2022 Control A.8.31.

**Purpose**: Define organizational requirements for environment separation, establishing WHAT separation is required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8.31.

**Core Principles**:

- Production environments SHALL be protected from development and testing activities
- Production data SHALL NOT be used in development or testing environments
- Changes SHALL flow through defined promotion paths before reaching production
- Developer access to production SHALL be restricted to emergency situations only

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including ISO/IEC 27001:2022, Swiss FADP, EU GDPR, and sector-specific requirements where applicable.

---

# Scope

## In Scope

This policy applies to:

**Environment Types**:

- Development environments (active code development, experimentation)
- Testing/QA environments (quality assurance, integration testing, UAT)
- Staging/Pre-production environments (final validation before production)
- Production environments (live business operations)

**Technology Scope**:

- All information systems and applications operated by [Organization]
- On-premises, cloud, hybrid, and container-based infrastructure
- Internal and customer-facing systems
- Third-party managed systems processing organizational data

**Personnel**:

- All employees, contractors, and third parties with access to organizational systems

## Out of Scope

This policy does NOT apply to:

- Single-user isolated research environments not connected to organizational networks
- Temporary proof-of-concept systems with no organizational data
- Vendor demonstration systems managed entirely by vendors

Once research or proof-of-concept systems transition to organizational use, they SHALL comply with this policy.

---

# Policy Statements

## Environment Architecture Requirements

[Organization] SHALL maintain separated environments with the following characteristics:

**3.1.1 Minimum Environment Tiers**

- Organizations SHALL maintain at minimum three environment tiers: Development, Testing/QA, and Production
- Each environment tier SHALL have defined purpose, infrastructure resources, data handling restrictions, and access controls
- Environment naming SHALL clearly distinguish environment type to prevent confusion

**3.1.2 Network Separation**

- Environments SHALL be isolated through network segmentation
- Inter-environment traffic SHALL be blocked by default (deny-all)
- Controlled promotion paths SHALL be the only permitted cross-environment connectivity
- Production environments SHALL NOT have direct network connectivity to development environments

**3.1.3 Infrastructure Separation**

- Compute, storage, and database resources SHALL be separated per environment
- Production and non-production workloads SHALL NOT share infrastructure resources
- Credentials and secrets SHALL be unique per environment

**3.1.4 Configuration Management**

- Environment configurations SHALL be managed as code and version controlled
- Staging environments SHALL mirror production configuration
- Configuration changes SHALL follow the same promotion path as application code

**3.1.4.1 Configuration Validation**

- Environment configurations SHALL be stored in version-controlled repository with access control
- Configuration changes SHALL follow the same promotion workflow as application code (Section 3.4.1)
- Staging configuration SHALL be validated against production configuration before each production deployment
- Configuration drift detection SHALL be performed weekly with violations reported to IT Operations Manager

## Environment Access Control Requirements

**3.2.1 Role-Based Access**

- Access to each environment SHALL follow least privilege principles
- Access rights SHALL be defined per role and environment tier
- Developers SHALL have full access to development environments only
- Operations team SHALL have primary access to production environments

**3.2.2 Production Access Restrictions**

- Developers SHALL NOT have standing access to production infrastructure
- Production access SHALL require privileged access management controls
- Multi-factor authentication SHALL be required for all production access
- Production access sessions SHALL be logged and monitored

**3.2.3 Emergency Access (Break-Glass)**

- Emergency developer access to production SHALL be permitted only during declared incidents
- Break-glass access SHALL require approval from Incident Commander and CISO
- Break-glass access SHALL be time-limited (maximum 8 hours, renewable with re-approval) and purpose-limited
- Post-incident review SHALL be mandatory for all break-glass activations

**3.2.3.1 Break-Glass Documentation Requirements**

Break-glass activations SHALL be logged with:

- Incident identifier (from incident management system) and declared severity level
- Requesting developer name, role, and manager
- Approving Incident Commander and CISO names with approval timestamps
- Access duration (granted, used, expired) and systems/applications accessed
- Actions performed during break-glass session (from session recording or activity log)
- Post-incident review outcome (completed within 7 days of incident closure)
- Lessons learned and process improvements identified

Break-glass logs SHALL be:

- Maintained in Privileged Access Management (PAM) system with automated retention
- Reviewed monthly by Information Security Manager for patterns and policy compliance
- Included in quarterly CISO dashboard with trend analysis (frequency, duration, justification categories)

**3.2.4 Access Reviews**

- Production environment access SHALL be reviewed quarterly
- Staging environment access SHALL be reviewed semi-annually
- Development/test environment access SHALL be reviewed annually
- Terminated employee access SHALL be revoked within 24 hours

## Data Handling Requirements

**3.3.1 Production Data Prohibition**

- Production data SHALL NOT be copied to development or test environments
- Production database backups SHALL NOT be restored in non-production environments
- Production credentials SHALL NOT be used in non-production environments

**3.3.2 Approved Data for Non-Production**

- Synthetic data (generated, not derived from production) SHALL be preferred
- Anonymized data MAY be used with Data Protection Officer approval
- Anonymization SHALL be irreversible (not pseudonymization or encryption)
- Anonymized data SHALL be deleted within 30 days of project completion

**3.3.2.1 Anonymization Validation Process**

Before DPO approves anonymized data for non-production use:

- Data Protection Officer SHALL test anonymization effectiveness using re-identification attempts
- Validation SHALL assess risk of re-identification through:
  - Direct identifier removal verification
  - Quasi-identifier combination analysis (k-anonymity assessment where k ≥ 5)
  - Linkage attack simulation using publicly available datasets
- Results SHALL be documented in Data Handling Register (ISMS-IMP-A.8.31-S2)
- Anonymization procedures SHALL be reviewed and approved by CISO and DPO before first use
- Failed validation SHALL result in rejection or additional anonymization measures

**3.3.3 Data Classification Enforcement**

- Confidential and Restricted data classifications SHALL be prohibited in development and test environments
- Automated scanning SHALL detect prohibited data in non-production environments
- Violations SHALL be remediated within 7 days of detection

**3.3.3.1 Automated Data Scanning**

- Non-production environments SHALL be scanned weekly for production data patterns
- Scanning SHALL cover databases, file systems, log files, and container images
- Scanning tools and detection patterns SHALL be defined in ISMS-IMP-A.8.31-S2
- Violations SHALL trigger alerts to Information Security Manager within 24 hours
- Scanning coverage and effectiveness SHALL be verified during quarterly self-assessments

## Environment Promotion Requirements

**3.4.1 Mandatory Promotion Path**

- Changes SHALL follow the standard promotion path: Development -> Testing -> Staging -> Production
- Direct deployment to production SHALL be prohibited except for approved emergency fixes
- Skipping environment tiers SHALL require documented exception and CISO approval

**3.4.2 Approval Requirements**

- Production deployments SHALL require Change Advisory Board approval per ISMS-POL-A.8.32 (Change Management)
- CAB composition and approval authority are defined in ISMS-POL-A.8.32
- Production deployments SHALL occur only during approved change windows
- Rollback plans SHALL be documented and available before production deployment
- Emergency changes MAY bypass CAB approval with post-implementation review within 48 hours

**3.4.3 Rollback Capability**

- Previous versions SHALL be retained for rollback purposes
- Rollback procedures SHALL be documented and tested periodically
- Operations team SHALL be authorized to execute rollbacks without additional approval during incidents

## Production Support Requirements

**3.5.1 Monitoring Access**

- Read-only monitoring access SHALL be provided to enable troubleshooting without production access
- Sensitive data SHALL be redacted from logs accessible to non-operations personnel
- Credentials SHALL NOT be included in logs

**3.5.2 Remote Troubleshooting**

- Troubleshooting procedures SHALL enable issue resolution without developer production access
- Runbooks SHALL be maintained for common operational scenarios
- Screen sharing MAY be used with operations team controlling production systems

**3.5.3 Incident Response Integration**

- Environment separation requirements SHALL be integrated with incident response procedures
- Tiered escalation SHALL be followed before granting emergency production access
- Break-glass usage SHALL be tracked and trended for continuous improvement

---

# Roles and Responsibilities

## Governance Roles

| Role | Responsibilities |
|------|------------------|
| **CISO** | Policy owner; approves exceptions; reviews compliance quarterly |
| **IT Operations Manager** | Production environment security; production access approval; PAM management |
| **Development Manager** | Development/test environment management; promotion workflow implementation |
| **Information Security Manager** | Compliance assessments; policy violation investigations; policy maintenance |
| **Data Protection Officer** | Anonymization approval; data handling compliance; re-identification testing |

## Operational Roles

| Role | Responsibilities |
|------|------------------|
| **System Owners** | Environment architecture definition; compliance documentation; exception reporting |
| **Developers** | Use assigned environments only; follow data handling requirements; use promotion workflows |
| **QA Team** | Testing in appropriate environments; test data management; report data violations |
| **Operations Team** | Production access management; production deployments; incident response |
| **Security Team** | Access log monitoring; violation investigation; security assessments |

---

# Compliance and Enforcement

## Assessment Requirements

| Assessment Type | Frequency | Responsible Party |
|-----------------|-----------|-------------------|
| Self-Assessment | Quarterly | System Owners, IT Operations |
| Security Assessment | Semi-Annual | Information Security Team |
| Internal Audit | Annual | Internal Audit |
| External Audit | Annual | External Auditor (ISO 27001) |
| Continuous Monitoring | Ongoing | Security Operations |

**4.1 Assessment Methodology**

Assessments SHALL verify environment separation compliance through:

**4.1.1 Technical Controls Validation**

- Network segmentation: Test that cross-environment traffic is blocked (quarterly)
- Access enforcement: Verify developer production access is prohibited (quarterly)
- Data scanning: Review automated scan results for production data in non-production (quarterly)
- Configuration consistency: Validate staging mirrors production (quarterly)

**4.1.2 Process Controls Validation**

- Promotion workflow: Audit last 30 days of production deployments for approval compliance (quarterly)
- Break-glass usage: Review post-incident documentation for all activations (quarterly)
- Access reviews: Verify completion and findings resolution (quarterly for production, semi-annually for staging)
- Exception management: Verify active exceptions are still justified and compensating controls are effective (quarterly)

**4.1.3 Evidence Validation**

- Documentation currency: Verify architecture docs reflect current state (semi-annually)
- Log completeness: Validate required logs are being generated and retained (quarterly)
- Training records: Verify relevant personnel completed environment separation training (annually)

Assessment results SHALL be documented in Compliance Assessment Register (ISMS-IMP-A.8.31-S3) with:

- Assessment date and assessor
- Controls assessed and findings identified
- Risk rating for each finding (Critical/High/Medium/Low per ISMS-POL-00)
- Remediation actions assigned with target closure dates
- Follow-up validation results

## Evidence Requirements

[Organization] SHALL maintain evidence of compliance including:

- Environment architecture documentation
- Access control matrices per environment
- Promotion workflow documentation
- Access review records
- Break-glass activation logs and post-incident reviews
- Data handling procedure documentation
- Compliance assessment reports

## Non-Compliance

Violations of this policy may result in:

- Immediate access revocation
- Disciplinary action per HR policies
- Incident reporting to regulatory authorities where required
- Corrective action tracking in the risk register

---

# Exception Management

## Exception Criteria

Exceptions MAY be approved only for:

- Legacy systems scheduled for decommission within 12 months
- Technical limitations where separation is not feasible (with documented justification)
- Temporary exceptions during migration or transformation projects

## Exception Process

1. **Request**: System Owner documents justification, risk assessment, compensating controls, and remediation plan
2. **Review**: Information Security Manager validates justification and compensating controls
3. **Approval**: CISO approves or denies with optional additional controls
4. **Tracking**: Exception tracked in risk register with expiration date
5. **Re-approval**: Exceptions expire and require re-approval per defined duration

## Compensating Controls

When exceptions are approved, compensating controls SHALL include one or more of:

- Enhanced access logging and monitoring
- Mandatory code review for all changes
- Read-only access restrictions
- Data masking requirements
- Increased change management rigor
- More frequent security assessments

---

# Related Documents

## ISMS Framework Documents

| Document ID | Title |
|-------------|-------|
| ISMS-POL-00 | Regulatory Applicability Framework |
| ISMS-POL-A.8.25-26-29 | Secure Development Framework |
| ISMS-POL-A.8.32 | Change Management |
| ISMS-POL-A.5.15-16-18 | Identity and Access Management |
| ISMS-POL-A.8.2-3-5 | Authentication and Privileged Access Management |

## Implementation Documents

| Document ID | Title |
|-------------|-------|
| ISMS-IMP-A.8.31-S1 | Environment Architecture Implementation |
| ISMS-IMP-A.8.31-S2 | Environment Access Control Implementation |
| ISMS-IMP-A.8.31-S3 | Environment Separation Assessment & Dashboard |

## Reference Documents

| Document ID | Title |
|-------------|-------|
| ISMS-REF-A.8.31-Environment-Architecture-Patterns | Environment Architecture Patterns |
| ISMS-REF-A.8.31-CICD-Pipeline-Integration | CI/CD Pipeline Integration |

## External Standards

- ISO/IEC 27001:2022 - Control A.8.31
- ISO/IEC 27002:2022 - Implementation guidance for A.8.31
- NIST SP 800-53 Rev. 5 - CM-7 (Least Functionality), SA-11 (Developer Testing)

---

# Definitions

| Term | Definition |
|------|------------|
| **Anonymization** | Irreversible process of removing personal data such that individuals cannot be re-identified |
| **Break-Glass Access** | Emergency procedure allowing developers temporary production access during declared incidents |
| **Environment** | Distinct set of infrastructure resources serving a specific SDLC purpose |
| **Privileged Access Management (PAM)** | System for managing and securing privileged credentials |
| **Production Environment** | Live operational environment serving real users with real business data |
| **Promotion** | Process of moving changes from one environment to another through defined workflow |
| **Pseudonymization** | Reversible process replacing identifiers with pseudonyms (still considered personal data) |
| **Staging Environment** | Pre-production environment mirroring production for final validation |
| **Synthetic Data** | Artificially generated data containing no real personal information |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:

- ✅ This policy document (ISMS-POL-A.8.31 v1.0)
- ✅ Approval signatures from CISO, CIO, Executive Management
- ✅ Environment separation requirements defined
- ✅ Production access restrictions documented
- ✅ Data handling requirements specified
- ✅ Roles and responsibilities assigned
- ✅ Assessment requirements documented

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Environment architecture documentation
- Access control matrices per environment
- Promotion workflow documentation
- Access review records
- Break-glass activation logs and post-incident reviews
- Data handling procedure documentation
- Compliance assessment reports

---

# Approval Record

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Chief Information Security Officer (CISO)** | [Name] | | [Date to be set] |
| **Chief Information Officer (CIO)** | [Name] | | [Date to be set] |
| **IT Operations Manager** | [Name] | | [Date to be set] |
| **Development Manager** | [Name] | | [Date to be set] |
| **Data Protection Officer (DPO)** | [Name] | | [Date to be set] |
| **Legal/Compliance Officer** | [Name] | | [Date to be set] |
| **Chief Executive Officer (CEO)** | [Name] | | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for separation of development, test and production environments. Implementation procedures are documented in ISMS-IMP-A.8.31-S1, S2, and S3.*

<!-- QA_VERIFIED: 2026-02-02 -->
