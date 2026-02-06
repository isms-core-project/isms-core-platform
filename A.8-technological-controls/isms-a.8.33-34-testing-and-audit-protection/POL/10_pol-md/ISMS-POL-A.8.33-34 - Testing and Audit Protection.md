**ISMS-POL-A.8.33-34 - Testing and Audit Protection**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Testing and Audit Protection |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.33-34 |
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
| 1.0 | [Date to be set] | CISO | Initial consolidated policy for ISO 27001:2022 certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO) / IT Operations Manager
- Privacy: Data Protection Officer (DPO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (CEO)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.8.11 (Data Masking)
- ISMS-POL-A.8.31 (Environment Separation)
- ISMS-IMP-A.8.33-34.1-UG (Test Data Protection - User Guide)
- ISMS-IMP-A.8.33-34.1-TG (Test Data Protection - Technical Specification)
- ISMS-IMP-A.8.33-34.2-UG (Audit Activity Management - User Guide)
- ISMS-IMP-A.8.33-34.2-TG (Audit Activity Management - Technical Specification)
- ISMS-IMP-A.8.33-34.3-UG (Compliance Dashboard - User Guide)
- ISMS-IMP-A.8.33-34.3-TG (Compliance Dashboard - Technical Specification)
- ISO/IEC 27001:2022 Controls A.8.33 and A.8.34

---

# Executive Summary

This policy establishes [Organization]'s requirements for protecting test information and safeguarding information systems during audit testing in accordance with ISO/IEC 27001:2022 Controls A.8.33 and A.8.34.

**Scope**: This policy applies to all test data selection and protection activities, all audit and security testing activities, all environments where testing occurs, and all personnel involved in testing and audit activities.

**Purpose**: Define organizational requirements for test data protection and audit testing controls, establishing WHAT protections are required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8.33-34.

**Core Principles**:

- Test data SHALL NOT contain unprotected production PII or sensitive data
- Production data used in testing SHALL be masked or anonymized
- Test environments SHALL be isolated from production systems
- Audit testing SHALL be planned to minimize operational disruption
- Audit tools and logs SHALL be protected and controlled

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022, with conditional sector-specific requirements (PCI DSS, HIPAA, FINMA) where applicable.

---

# Scope

## In Scope

This policy applies to:

**Control A.8.33 - Test Information**:

- All test data used in development, QA, staging, and training environments
- Production data copies used for testing purposes
- Synthetic and generated test data
- Test databases and data repositories
- User acceptance testing (UAT) data
- Performance and load testing datasets
- Security testing data

**Control A.8.34 - Audit Testing**:

- Internal security audits and assessments
- External certification audits (ISO 27001)
- Penetration testing and vulnerability assessments
- Technical compliance scanning
- Third-party security assessments
- Regulatory compliance audits

**Environments**:

- Development environments
- Testing/QA environments
- Staging/Pre-production environments
- Training and demonstration environments
- Sandbox and experimental environments

**Personnel**:

- All employees involved in testing activities
- Development and QA teams
- Internal and external auditors
- Penetration testing teams
- Third-party assessors and consultants

## Out of Scope

This policy does NOT apply to:

- Production environment operations (covered by operational policies)
- Routine monitoring activities (covered by A.8.16)
- Data masking technique specifications (covered by A.8.11)
- Environment architecture requirements (covered by A.8.31)

---

# Policy Statements - Control A.8.33: Test Information

## Test Data Selection Requirements

**REQ-TEST-001: No Live Data Default**

[Organization] SHALL NOT use operational (live) production data containing PII or sensitive information for testing unless explicitly approved and protected.

**Preferred Data Sources** (in order of preference):
1. Synthetic data - artificially generated, no relation to real data
2. Anonymized data - irreversibly de-identified production data
3. Masked/pseudonymized data - protected production data (requires approval)

**Rationale**: Unprotected production data in test environments creates data breach risk, regulatory non-compliance, and unauthorized access exposure.

---

**REQ-TEST-002: Test Data Classification**

Test data SHALL be classified according to [Organization]'s data classification scheme:

- **Synthetic data** (no production data source): Classified as Public or Internal based on business context
- **Production-derived data** (masked, anonymized, or pseudonymized): Inherits production data classification until masking validation confirms non-reversibility, then MAY be downgraded with Data Owner approval
- **Direct production copies** (during refresh process): Classified as Restricted until masking is applied
- Classification determines protection requirements and access controls
- Data Owner approval required for Confidential or Restricted test data

---

## Data Protection Requirements

**REQ-TEST-003: Production Data Masking**

When production data is required for testing, [Organization] SHALL apply data masking per ISMS-POL-A.8.11:

- PII SHALL be masked, anonymized, or replaced with synthetic values
- Financial data (account numbers, payment cards) SHALL be masked
- Credentials and secrets SHALL be replaced with test values
- Health information SHALL be de-identified per applicable regulations

**Masking Validation**: Masked data SHALL be validated to confirm:

- Original sensitive values are not recoverable through pattern matching, dictionary attacks, or re-identification techniques
- Data format preserved for application compatibility
- Referential integrity maintained across datasets

**Validation Testing Requirements**:

- Validation testing SHALL include: (1) Comparison against production data samples to detect pattern similarities, (2) Statistical analysis to confirm distribution differences from production, (3) Verification that no plaintext PII exists in test database exports
- Validation results SHALL be documented and approved by Information Security Manager before test environment use
- Validation procedures are documented in ISMS-IMP-A.8.33-34.1

---

**REQ-TEST-004: Test Data Isolation**

Test data SHALL be isolated from production:

- Test databases SHALL be logically or physically separated from production
- No direct access paths between test and production data stores
- Test data exports SHALL be controlled and logged
- Data refresh procedures SHALL include re-masking

---

## Test Environment Requirements

**REQ-TEST-005: Environment Separation**

[Organization] SHALL maintain separated test environments per ISMS-POL-A.8.31:

- Development, testing, and production environments SHALL be separated
- Network segmentation SHALL prevent unauthorized cross-environment access
- Separate credentials SHALL be required for each environment
- Clear environment identification SHALL prevent confusion

---

**REQ-TEST-006: Access Controls**

Access to test environments containing sensitive data SHALL:

- Follow least privilege principles
- Require explicit authorization based on job function
- Be reviewed at least annually
- Be revoked upon role change or termination

---

## Test Data Lifecycle

**REQ-TEST-007: Data Retention**

Test data containing masked production data SHALL:

- Be retained only for the duration of testing requirements
- Be deleted within 30 days of project completion

For continuous testing environments where "project completion" is not clearly defined:

- Test data retention SHALL be reviewed quarterly
- Test data older than 90 days without documented active usage SHALL be deleted unless:
  - Data Owner provides written approval with business justification
  - Exception is documented in exception register with expiration date (maximum 12 months)
- Automated retention monitoring SHALL flag data exceeding thresholds for review

Test data SHALL:

- Follow documented retention and deletion procedures
- Be included in data deletion verification

---

**REQ-TEST-008: Test Data Refresh**

When test data is refreshed from production:

- Masking SHALL be applied before data is accessible in test environment
- Refresh procedures SHALL be documented and approved
- Refresh activities SHALL be logged for audit purposes
- Data Owner approval required for scheduled refreshes

---

# Policy Statements - Control A.8.34: Audit Testing

## Audit Planning Requirements

**REQ-AUDIT-001: Pre-Audit Agreement**

[Organization] SHALL establish formal agreement before any audit testing:

- Scope of systems and information to be tested
- Testing methodologies and tools to be used
- Timing and duration of testing activities
- Escalation procedures for issues discovered
- Confidentiality requirements for audit findings

**Agreement Parties**: Management and auditor/assessor SHALL jointly approve testing scope and methods before testing begins.

---

**REQ-AUDIT-002: Timing and Scheduling**

Audit testing activities SHALL be scheduled to minimize operational impact:

- Critical business periods SHALL be avoided (unless specifically testing resilience)
- Testing windows SHALL be coordinated with IT Operations
- Stakeholders SHALL be notified of planned testing activities
- Emergency testing SHALL follow expedited approval process

---

## Access Control Requirements

**REQ-AUDIT-003: Auditor Access**

Access granted to auditors and assessors SHALL:

- Be limited to scope agreed in pre-audit agreement
- Default to read-only access for information and software
- Require MFA for access to sensitive systems
- Be time-limited to the audit duration
- Be logged and monitored throughout the engagement

---

**REQ-AUDIT-004: Device Security**

Devices used by auditors to access [Organization]'s systems SHALL:

- Meet [Organization]'s minimum security requirements
- Have current endpoint protection and patching
- Not introduce malware or unauthorized software
- Be verified before access is granted

---

## Testing Controls

**REQ-AUDIT-005: Testing Boundaries**

Audit testing activities SHALL:

- Remain within agreed scope boundaries
- Not access systems or data outside defined scope
- Stop immediately if unintended impact occurs
- Be suspended if critical issues are discovered affecting operations

---

**REQ-AUDIT-006: Penetration Testing Controls**

Penetration testing and active security testing SHALL:

- Be authorized in writing by appropriate management
- Be conducted in isolated or non-production environments where possible
- Include rollback and recovery procedures
- Have IT Operations on standby during active testing
- Follow agreed rules of engagement

---

## Data and Log Protection

**REQ-AUDIT-007: Audit Data Handling**

Data accessed or collected during audits SHALL:

- Be protected according to its classification
- Not be retained longer than necessary for audit purposes
- Be securely deleted after audit completion
- Be subject to confidentiality agreements

---

**REQ-AUDIT-008: Audit Log Protection**

Logs generated during audit activities SHALL:

- Be protected from unauthorized modification or deletion
- Be retained per [Organization]'s log retention policy
- Be available for review if audit findings are questioned
- Be included in security monitoring during testing period

---

## Incident Response During Audits

**REQ-AUDIT-009: Incident Handling**

If audit testing causes unintended impact:

- Testing SHALL be suspended immediately
- IT Operations SHALL be notified for containment
- Root cause SHALL be documented
- Resumption requires explicit approval from IT Operations Manager

---

**REQ-AUDIT-010: Vulnerability Discovery**

Vulnerabilities discovered during audit testing SHALL:

- Be reported to Security Team immediately if critical
- Be documented in audit findings
- Be handled per [Organization]'s vulnerability management process
- Not be exploited beyond scope necessary for verification

---

# Roles and Responsibilities

## Governance Roles

| Role | Responsibilities |
|------|------------------|
| **CISO** | Policy owner; approves audit testing scope; reviews compliance; authorizes penetration testing |
| **IT Operations Manager** | Production protection; audit scheduling; incident response during testing |
| **Data Protection Officer** | Test data privacy compliance; anonymization approval; regulatory alignment |
| **Information Security Manager** | Audit coordination; testing standards; policy maintenance |
| **Internal Audit** | Audit planning; engagement management; findings reporting |

## Operational Roles

| Role | Responsibilities |
|------|------------------|
| **Data Owners** | Test data authorization; masking approval; data classification decisions |
| **Development Manager** | Test environment management; test data procedures; developer compliance |
| **QA Manager** | Test data quality; testing process compliance; UAT oversight |
| **Security Team** | Audit tool management; penetration testing coordination; vulnerability handling |
| **External Auditors** | Compliance with access restrictions; confidentiality; scope adherence |

---

# Compliance and Enforcement

## Assessment Requirements

| Assessment Type | Frequency | Responsible Party |
|-----------------|-----------|-------------------|
| Test Data Inventory | Quarterly | Development/QA Managers |
| Test Environment Review | Semi-Annual | IT Operations, Security Team |
| Audit Procedure Review | Annual | Internal Audit, CISO |
| Compliance Assessment | Annual | Information Security Manager |

## Verification Mechanisms

[Organization] verifies compliance through:

- Automated scanning for sensitive data in test environments
- Access log reviews for test environment access
- Audit engagement documentation reviews
- Test data masking effectiveness validation
- Pre-audit checklist completion verification

## Evidence Requirements

[Organization] SHALL maintain evidence including:

- Test data handling procedures and approvals
- Data masking verification records
- Audit engagement agreements and scope documents
- Auditor access logs and activity records
- Penetration testing authorization and rules of engagement
- Incident reports from testing activities

## Non-Compliance

Violations of this policy may result in:

- Immediate suspension of testing activities
- Access revocation for non-compliant personnel
- Disciplinary action per HR policies
- Contract termination for third-party violators
- Incident reporting where regulatory breach occurs

---

# Exception Management

## Exception Criteria

Exceptions MAY be approved only for:

- Legacy systems requiring production data for specific debugging
- Regulatory requirements mandating specific testing approaches
- Technical limitations preventing standard masking approaches

## Exception Process

1. **Request**: Requestor documents business justification, risk assessment, and compensating controls
2. **Review**: Security Team validates technical necessity and evaluates compensating controls
3. **Approval**: CISO (test data) or IT Operations Manager (audit timing) approves with conditions
4. **Tracking**: Exception tracked with expiration date and review schedule
5. **Monitoring**: Compensating controls verified throughout exception period

## Compensating Controls

When exceptions are approved, compensating controls SHALL include:

- Enhanced access logging and monitoring
- Reduced data retention periods
- Additional access restrictions
- Increased oversight and review frequency

---

# Regulatory Alignment

## Mandatory Compliance

| Regulation | Test Information (A.8.33) | Audit Testing (A.8.34) |
|------------|---------------------------|------------------------|
| **Swiss nDSG** | Art. 8 - Data protection by design; personal data minimization in testing | Art. 8 - Appropriate technical measures during processing |
| **EU GDPR** | Art. 5(1)(c) - Data minimization; Art. 25 - Privacy by design; Art. 32 - Pseudonymization | Art. 32 - Security of processing; testing as security measure |
| **ISO 27001:2022** | Control A.8.33 - Test information selection and protection | Control A.8.34 - Audit testing planning and system protection |

## Conditional Applicability

| Regulation | Trigger | Key Requirements |
|------------|---------|------------------|
| **PCI DSS** | Payment card processing | Req. 3.4 - Test data masking; Req. 11 - Security testing requirements |
| **HIPAA** | US healthcare data | De-identification standards for test data |
| **FINMA** | Swiss financial services | Risk-based testing controls; outsourcing security |

---

# Related Documents

## ISMS Framework Documents

| Document ID | Title |
|-------------|-------|
| ISMS-POL-00 | Regulatory Applicability Framework |
| ISMS-POL-A.8.11 | Data Masking |
| ISMS-POL-A.8.31 | Environment Separation |
| ISMS-POL-A.8.32 | Change Management |
| ISMS-POL-A.5.15-16-18 | Identity and Access Management |

## Implementation Documents

| Document ID | Title |
|-------------|-------|
| ISMS-IMP-A.8.33-34.1-UG | Test Data Protection - User Guide |
| ISMS-IMP-A.8.33-34.1-TG | Test Data Protection - Technical Specification |
| ISMS-IMP-A.8.33-34.2-UG | Audit Activity Management - User Guide |
| ISMS-IMP-A.8.33-34.2-TG | Audit Activity Management - Technical Specification |
| ISMS-IMP-A.8.33-34.3-UG | Compliance Dashboard - User Guide |
| ISMS-IMP-A.8.33-34.3-TG | Compliance Dashboard - Technical Specification |

## External Standards

- ISO/IEC 27001:2022 - Controls A.8.33, A.8.34
- ISO/IEC 27002:2022 - Implementation guidance for A.8.33, A.8.34
- NIST SP 800-53 Rev. 5 - SA-11 (Developer Testing), AU-11 (Audit Record Retention)

---

# Definitions

| Term | Definition |
|------|------------|
| **Anonymization** | Irreversible process removing all identifying information such that re-identification is not possible |
| **Audit Testing** | Systematic examination of systems, controls, and processes to verify compliance and effectiveness |
| **Data Masking** | Process of obscuring original data with modified content while maintaining format and usability |
| **Penetration Testing** | Authorized simulated attack on systems to identify security vulnerabilities |
| **Production Data** | Live operational data from business systems containing real information |
| **Pseudonymization** | Replacement of identifiers with pseudonyms; re-identifiable with separate key |
| **Synthetic Data** | Artificially generated data containing no real personal or business information |
| **Test Environment** | Non-production system used for development, testing, or training purposes |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:

- ✅ This policy document (ISMS-POL-A.8.33-34 v1.0)
- ✅ Approval signatures from CISO, CIO, Executive Management
- ✅ Test data handling requirements defined
- ✅ Audit protection requirements documented
- ✅ Penetration testing requirements specified
- ✅ Roles and responsibilities assigned

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Test data handling procedures and approvals
- Data masking verification records
- Audit engagement agreements and scope documents
- Auditor access logs and activity records
- Penetration testing authorization and rules of engagement
- Incident reports from testing activities

---

# Approval Record

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Chief Information Security Officer (CISO)** | [Name] | | [Date to be set] |
| **Chief Information Officer (CIO)** | [Name] | | [Date to be set] |
| **IT Operations Manager** | [Name] | | [Date to be set] |
| **Data Protection Officer (DPO)** | [Name] | | [Date to be set] |
| **Internal Audit Manager** | [Name] | | [Date to be set] |
| **Legal/Compliance Officer** | [Name] | | [Date to be set] |
| **Chief Executive Officer (CEO)** | [Name] | | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for testing and audit protection. Implementation procedures are documented in ISMS-IMP-A.8.33-34.1-UG/TG, .2-UG/TG, and .3-UG/TG.*

<!-- QA_VERIFIED: 2026-02-02 -->
