<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.30:framework:POL:a.8.30 -->
**ISMS-POL-A.8.30 – Outsourced Development**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Outsourced Development Policy |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.30 |
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
- Secondary: Chief Technology Officer (CTO)
- Procurement: Procurement/Vendor Management
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.8.28 (Secure Coding)
- ISMS-POL-A.5.19-23 (Supplier Relationships & Cloud Services)
- ISMS-IMP-A.8.30.1-UG/TG (Vendor Assessment and Registry)
- ISMS-IMP-A.8.30.2-UG/TG (Contract Compliance)
- ISMS-IMP-A.8.30.3-UG/TG (Security Testing and Acceptance)
- ISMS-IMP-A.8.30.4-UG/TG (Monitoring and Exceptions Dashboard)
- ISO/IEC 27001:2022 Control A.8.30
- ISO/IEC 27002:2022 Control 8.30

---

## Executive Summary

This policy establishes [Organization]'s requirements for managing security in outsourced system and software development in accordance with ISO/IEC 27001:2022 Control A.8.30.

**Purpose**: Define WHAT security controls are required for outsourced development and WHO is accountable. Technical implementation details (HOW) are documented in ISMS-IMP-A.8.30 specifications.

**Scope**: All outsourced development activities including contracted development, offshore development, freelance developers, and acquired software customization.

**Business Risk Addressed**: Security vulnerabilities introduced through third-party development leading to data breaches, intellectual property theft, supply chain compromise, and regulatory non-compliance.

**Regulatory Alignment**: Per ISMS-POL-00 (Regulatory Applicability Framework):

- **Mandatory**: Swiss FADP (Art. 8), EU GDPR (Art. 32), ISO 27001:2022
- **Conditional**: FINMA, DORA (Art. 28-30 ICT third-party risk), NIS2 (Art. 21 supply chain)
- **Informational**: NIST SP 800-218 SSDF, ISO/IEC 27036 (Supplier Relationships)

---

# Control Alignment & Scope

## ISO/IEC 27001:2022 Control A.8.30

**Control Statement**:
> *The organization shall direct, monitor and review the activities related to outsourced system development.*

**Control Type**: Preventive and Detective

**Control Objective**: Ensure that information security measures required by [Organization] are effectively implemented when system and software development is outsourced to third parties.

**This Control Addresses**:

- Direction of outsourced development security requirements
- Monitoring of third-party development activities
- Review and verification of outsourced deliverables
- Contractual security requirements
- Security testing of third-party code
- Subcontractor and supply chain management

## Scope Definition

**In Scope**:

- All contracted software development (full projects, modules, components)
- Offshore and nearshore development teams
- Freelance/independent developers
- Staff augmentation with development access
- Acquired software requiring customization
- Development platform providers (where [Organization] code is hosted)
- Managed development services

**Out of Scope**:

- Commercial off-the-shelf (COTS) software without customization (see A.8.31)
- Internal development by employees (see A.8.28)
- Cloud service providers for infrastructure only (see A.5.23)
- General supplier management (see A.5.19-22)

## Document Hierarchy

| Document Type | Content | Update Frequency |
|---------------|---------|------------------|
| **This Policy (POL)** | Requirements, governance, accountability | Annual |
| **Implementation (IMP)** | Assessment procedures, workbook specs | Quarterly |
| **Reference (REF)** | Contract templates, checklists | As needed |

---

# Vendor Selection & Due Diligence

## Security Assessment Requirements

**Pre-Engagement Assessment**:

Prior to engaging any outsourced development vendor, [Organization] SHALL conduct security due diligence including:

| Assessment Area | Requirement | Evidence Required |
|-----------------|-------------|-------------------|
| **Security Certification** | ISO 27001 or SOC 2 Type II preferred | Current certificate (within 12 months) |
| **Secure Development Practices** | OWASP SAMM, Microsoft SDL, or equivalent | SDLC documentation or attestation |
| **Security Incident History** | No major breaches in past 24 months | Vendor disclosure + reference checks |
| **Technical Capabilities** | SAST/DAST/SCA tooling in use | Tool inventory and sample reports |
| **Personnel Security** | Background checks for developers | Written confirmation of screening policy |

**Risk-Based Assessment Depth**:

| Project Classification | Assessment Depth | Approver |
|------------------------|------------------|----------|
| **Critical** (production systems, sensitive data) | Full security questionnaire + on-site/remote audit + reference checks | CISO |
| **High** (internal systems, business data) | Security questionnaire + reference checks | IT Security Manager |
| **Standard** (non-sensitive, low-risk) | Security questionnaire + certification verification | Procurement + Security Review |

**Verification**: Due diligence records retained in vendor management system; assessment results documented in Workbook 1.

## Approved Vendor Registry

[Organization] SHALL maintain an approved vendor registry for outsourced development:

- Vendors assessed and approved before engagement
- Registry includes: vendor name, assessment date, risk tier, approved project types, renewal date
- Annual reassessment required for active vendors
- Removal from registry upon contract termination, security incident, or failed reassessment

**Verification**: Approved vendor registry maintained by Procurement with Security input; quarterly review of active vendors.

---

# Contractual Security Requirements

## Mandatory Contract Clauses

All outsourced development contracts SHALL include the following security requirements:

**Security Standards Compliance**:

- Adherence to [Organization]'s secure coding standards (ISMS-POL-A.8.28)
- Compliance with [Organization]'s security policies and procedures
- Use of approved development tools and environments
- Security training completion requirements

**Intellectual Property and Code Protection**:

- Clear ownership of developed code and documentation
- Source code escrow arrangements for critical projects
- Protection of [Organization]'s proprietary information
- Non-disclosure and confidentiality obligations

**Security Verification Rights**:

- Right to audit development processes and security controls
- Right to conduct security testing of deliverables
- Right to request security certifications and attestations
- Right to access security incident information

**Incident Notification**:

- Notification of security incidents within 24 hours
- Notification of suspected data breaches immediately
- Cooperation with incident investigation
- Post-incident remediation requirements

**Subcontractor Management**:

- Prior written approval required for subcontractors
- Flow-down of security requirements to subcontractors
- [Organization] right to reject subcontractors
- Subcontractor audit rights

## Vulnerability Remediation SLAs

Contracts SHALL specify vulnerability remediation timeframes aligned with ISMS-POL-A.8.28:

| Severity | CVSS Score | Remediation SLA |
|----------|------------|-----------------|
| **Critical** | 9.0-10.0 | 7 days |
| **High** | 7.0-8.9 | 30 days |
| **Medium** | 4.0-6.9 | 90 days |
| **Low** | 0.1-3.9 | Next release or 180 days |

**SLA Enforcement**:

- SLA compliance tracked in project management system
- Repeated SLA failures escalated to vendor management and CISO
- Chronic non-compliance may result in contract review or termination
- SLA exceptions require documented risk acceptance (CISO approval for Critical/High)

**Verification**: Contract templates maintained by Legal with Security input; compliance tracked in Workbook 2.

## Termination and Transition

Contracts SHALL address security requirements for termination:

- Return or secure destruction of [Organization] data
- Revocation of all access credentials within 24 hours
- Transfer of documentation and source code
- Knowledge transfer period for critical projects
- Post-termination confidentiality obligations
- Certification of data destruction

---

# Secure Development Requirements

## Development Standards

Outsourced developers SHALL comply with [Organization]'s secure coding standards per ISMS-POL-A.8.28:

**Mandatory Requirements**:

- Input validation for all user and external input
- Output encoding appropriate to context
- Secure authentication and session management
- Server-side authorization enforcement
- Use of approved cryptographic methods
- Secure error handling (no sensitive data in logs)
- No hardcoded secrets in source code

**Prohibited Practices**:

- Hardcoded credentials, API keys, or secrets
- Deprecated or insecure functions
- SQL query construction via string concatenation
- Disabled security controls
- Committing secrets to version control
- Ignoring security tool findings without exception

**Verification**: Secure coding compliance verified via code review and security testing; findings documented in Workbook 3.

## Development Environment Security

Outsourced development environments SHALL meet minimum security requirements:

| Requirement | Description |
|-------------|-------------|
| **Access Control** | MFA required for all development systems; least privilege access |
| **Network Security** | Development environment isolated or secured; no direct production access |
| **Endpoint Security** | Developer workstations with current security software |
| **Code Repository** | Branch protection, code review enforcement, secret scanning |
| **Data Handling** | No production data in development without masking/anonymization |

**Verification**: Environment security requirements documented in Workbook 1; vendor attestation required.

## Third-Party Developer Training

Prior to accessing [Organization] systems or code, outsourced developers SHALL:

- Complete [Organization]'s secure coding awareness training (or equivalent)
- Acknowledge [Organization]'s security policies and acceptable use requirements
- Demonstrate understanding of project-specific security requirements

**Training Verification**:

- Training completion tracked in vendor onboarding checklist **and recorded in [HR/Vendor Management System]**
- **Access requests cross-checked against training records before approval** (system-enforced where feasible, procedural review for manual access provisioning)
- Annual refresher required for long-term engagements
- Training records retained for audit

**Verification**: Training completion confirmed before access granted; records in Workbook 4.

---

# Security Verification & Testing

## Code Review Requirements

All outsourced code SHALL be subject to security review before acceptance:

| Review Type | Requirement | Reviewer |
|-------------|-------------|----------|
| **Peer Review** | All code changes reviewed before merge | Internal developer (minimum 1) |
| **Security Review** | Security-sensitive changes reviewed by security team | Application Security Team |
| **Architecture Review** | New components or significant changes | Security Architect |

**Review Criteria** (per ISMS-REF-A.8.28):

- Input validation and output encoding
- Authentication and authorization logic
- Cryptographic implementations
- Error handling and logging
- Third-party component usage

**Verification**: Code review records retained in version control system; review statistics in Workbook 3.

## Security Testing Requirements

Outsourced deliverables SHALL undergo security testing before production deployment:

**Automated Testing**:

- SAST (Static Application Security Testing): Run on all code before acceptance
- SCA (Software Composition Analysis): Scan all third-party dependencies
- Secret scanning: Verify no secrets in codebase

**Manual Testing**:

- DAST (Dynamic Application Security Testing): Run on staging environment
- Penetration testing: Required for Critical projects before go-live

**Testing Responsibility**:

| Test Type | Primary Responsibility | Verification |
|-----------|------------------------|--------------|
| SAST | Vendor (with [Organization] tool access) or [Organization] | Scan reports reviewed |
| SCA | Vendor or [Organization] | SBOM and vulnerability report |
| DAST | [Organization] Application Security | Test report documented |
| Penetration Test | [Organization] or approved third-party | Findings remediated before go-live |

**Acceptance Criteria**:

- No Critical or High vulnerabilities (or documented exception with compensating controls)
- All security requirements verified
- Security test reports documented and retained

**Verification**: Test results documented in Workbook 3; acceptance sign-off required.

## Software Bill of Materials (SBOM)

For all outsourced development, [Organization] SHALL receive:

- Complete SBOM listing all third-party components
- Component versions and licenses
- Known vulnerability status at time of delivery
- Update plan for components with known vulnerabilities

**SBOM Format**: CycloneDX or SPDX format preferred; spreadsheet acceptable for simple projects.

**Verification**: SBOM reviewed and retained with project documentation; tracked in Workbook 3.

---

# Monitoring & Oversight

## Active Oversight Requirements

[Organization] SHALL maintain active involvement in outsourced development (not passive monitoring):

**Directing**:

- Clear security requirements communicated at project initiation
- Security checkpoints defined in project milestones
- Regular security guidance and clarification

**Monitoring**:

- Regular status updates on security activities
- Access to vendor's security testing results
- Participation in security-related discussions
- Alert monitoring for security incidents

**Reviewing**:

- Security deliverables reviewed at each milestone
- Final security review before acceptance
- Lessons learned captured for future projects

## Monitoring Frequency

| Project Classification | Status Updates | Security Reviews | Full Audit |
|------------------------|----------------|------------------|------------|
| **Critical** | Weekly | At each milestone + final | Annual (or project end) |
| **High** | Bi-weekly | At major milestones + final | On-demand |
| **Standard** | Monthly | Final acceptance | On-demand |

**Verification**: Monitoring activities logged in project management system; summary in Workbook 2.

## Issue Escalation

Security issues identified during monitoring SHALL be escalated:

| Issue Severity | Escalation Path | Timeline |
|----------------|-----------------|----------|
| **Critical** (active vulnerability, breach) | Project Manager → CISO → Executive | Immediate |
| **High** (security requirement not met) | Project Manager → IT Security Manager | Within 24 hours |
| **Medium** (deviation from standards) | Project Manager → Security Lead | Within 5 business days |
| **Low** (minor observation) | Logged for project review | Next status meeting |

---

# Subcontractor Management

## Subcontractor Requirements

Outsourced development vendors SHALL NOT engage subcontractors without:

- Prior written approval from [Organization]
- Subcontractor security assessment (proportionate to risk)
- Flow-down of all security requirements to subcontractor, including:
  - Secure coding standards (per ISMS-POL-A.8.28)
  - Security testing requirements (per ISMS-POL-A.8.29)
  - **SBOM delivery requirements (covering subcontractor components)**
  - Vulnerability remediation SLAs (per Section 5.2)
- Direct audit rights over subcontractor (or vendor-conducted audit)
- Confidentiality and IP protection obligations

## Subcontractor Approval Process

**Approval Requirements**:

| Subcontractor Scope | Approval Authority | Assessment Required |
|---------------------|-------------------|---------------------|
| Access to [Organization] systems/data | CISO | Full security questionnaire |
| Development without direct access | IT Security Manager | Abbreviated questionnaire + vendor attestation |
| Limited/specialized tasks | Project Manager + Security | Vendor attestation of security requirements flow-down |

**Verification**: Subcontractor approvals documented in project records; tracked in Workbook 4.

---

# Roles and Responsibilities

## Executive Management

- Approve outsourced development security policy
- Allocate budget for security assessments and testing
- Review high-risk vendor engagements
- Escalation point for critical security issues

## Chief Information Security Officer (CISO)

- Overall accountability for outsourced development security
- Approve high-risk vendor engagements
- Approve security exceptions
- Review security metrics and vendor performance
- Escalation for security incidents involving vendors

## IT Security Manager

- Day-to-day oversight of vendor security compliance
- Conduct or coordinate vendor security assessments
- Review security testing results
- Approve standard-risk vendor engagements
- Manage vendor security incident response

## Application Security Team

- Define secure development requirements
- Conduct security testing of deliverables
- Review security-sensitive code changes
- Provide security guidance to project teams
- Maintain security testing tools and procedures

## Procurement/Vendor Management

- Maintain approved vendor registry
- Ensure contracts include required security clauses
- Coordinate vendor assessments with Security
- Manage vendor performance including security metrics
- Coordinate vendor offboarding

## Project Managers

- Ensure security requirements included in project scope
- Monitor vendor compliance with security requirements
- Escalate security issues appropriately
- Ensure security milestones are met
- Coordinate security reviews and testing

## Development Team Leads

- Review outsourced code before acceptance
- Verify security testing completed
- Ensure integration with internal security practices
- Report security concerns to Security team

---

# Governance and Compliance

## Policy Compliance Monitoring

**Continuous Monitoring**:

- Vendor security assessment status tracked
- Contract security clause compliance verified
- Security testing results reviewed

**Periodic Assessment**:

- Quarterly: Active vendor security status review
- Annual: Full vendor security reassessment
- Annual: Policy effectiveness review

## Non-Compliance Handling

**Vendor Non-Compliance**:

| Severity | Response | Escalation |
|----------|----------|------------|
| **Critical** (active security breach, major violation) | Immediate suspension of access; incident response | CISO, Executive, Legal |
| **High** (significant security gap) | Remediation plan required within 5 days; enhanced monitoring | IT Security Manager, Project Sponsor |
| **Medium** (deviation from requirements) | Documented warning; remediation within 30 days | Project Manager, Security Lead |
| **Low** (minor observation) | Noted for next review | Project Manager |

**Repeated Non-Compliance**: Vendors with repeated non-compliance issues may be:

- Subject to enhanced monitoring
- Restricted to lower-risk projects
- Removed from approved vendor registry
- Subject to contract termination

## Exception Management

- All exceptions require documented business justification
- Risk assessment and compensating controls mandatory
- Approval authority based on risk level (Security Lead for Medium, CISO for High/Critical)
- Exceptions tracked in central register (Workbook 4)
- Maximum duration: 90 days (renewable with re-approval)

**Compensating Controls Adequacy Criteria**:

- **Effectiveness**: Control mitigates the specific risk (not generic security)
- **Reliability**: Control operates continuously with alerting on failure
- **Verifiability**: Control operation can be tested and monitored
- **Scope**: Control covers all affected systems/data flows

**Exceptions require documented risk assessment** quantifying residual risk with and without proposed compensating controls. Risk assessment SHALL be prepared by project team and validated by IT Security Manager before approval authority review.

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:

- ✅ This policy document (ISMS-POL-A.8.30 v1.0)
- ✅ Approval signatures from CISO, CIO, Executive Management
- ✅ Vendor security requirements documented
- ✅ Contract security clauses defined
- ✅ Security testing requirements specified
- ✅ Roles and responsibilities assigned
- ✅ Assessment workbook references documented (ISMS-IMP-A.8.30)

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Approved vendor registry with assessment records
- Contract templates with security clauses
- Vendor security assessment reports
- Security testing results for outsourced deliverables
- Code review records
- Subcontractor approval records
- Exception and incident records
- Training completion records

**Assessment Workbooks** (ISMS-IMP-A.8.30 Suite):
- ISMS-IMP-A.8.30.1: Vendor Assessment & Registry
- ISMS-IMP-A.8.30.2: Contract Compliance
- ISMS-IMP-A.8.30.3: Security Testing & Acceptance
- ISMS-IMP-A.8.30.4: Monitoring & Exceptions Dashboard

**Evidence Retention:**
- Vendor assessment records: Duration of relationship + 3 years
- Contract documents: Duration of contract + 7 years
- Security testing results: 5 years (aligned with DORA Art. 28(6) where applicable) or project lifecycle + 3 years
- Code review records: Project lifecycle + 2 years
- Incident records: 5 years

---

# Integration with Related Controls

## Related ISMS Controls

| Control | Integration |
|---------|-------------|
| **A.5.19** (Supplier Security) | Vendor risk assessment framework feeds A.8.30 |
| **A.5.20** (Supplier Agreements) | Contract security clauses from A.8.30 |
| **A.5.21** (ICT Supply Chain) | SBOM and subcontractor requirements align |
| **A.5.22** (Supplier Monitoring) | Ongoing vendor monitoring per A.8.30 |
| **A.8.25** (Secure Architecture) | Architecture requirements apply to outsourced systems |
| **A.8.28** (Secure Coding) | Secure coding standards apply to third parties |
| **A.8.29** (Security Testing) | Testing requirements for outsourced deliverables |
| **A.8.31** (Development Environment) | Environment security requirements for vendors |

## Regulatory Mapping

| Requirement | Swiss FADP | EU GDPR | ISO 27001 | DORA* |
|-------------|-----------|---------|-----------|-------|
| Vendor security assessment | Art. 8 | Art. 28, 32 | A.8.30 | Art. 28 |
| Contract security requirements | Art. 8 | Art. 28 | A.5.20 | Art. 30 |
| Security testing | Art. 8 | Art. 32 | A.8.29 | Art. 24-25 |
| Subcontractor management | Art. 8 | Art. 28(4) | A.5.21 | Art. 29 |

*DORA applicable where [Organization] is classified as financial entity.

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Technology Officer (CTO)** | [Name] | [Date] |
| **Procurement Manager** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for outsourced development security. Implementation procedures, assessment methodologies, and workbook specifications are documented in ISMS-IMP-A.8.30.1-4 (UG/TG).*

<!-- QA_VERIFIED: 2026-02-02 -->
