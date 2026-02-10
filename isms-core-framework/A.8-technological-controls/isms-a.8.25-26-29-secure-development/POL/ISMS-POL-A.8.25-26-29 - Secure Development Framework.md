<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.25-26-29:framework:GOV-POL:a.8.25-26-29 -->
**ISMS-POL-A.8.25-26-29 – Secure Development Framework**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Secure Development Framework |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.25-26-29 |
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
| 1.0 | [Date to be set] | CISO / Application Security Lead | Initial consolidated secure development framework |

**Review Cycle**: Annual (or upon significant SDLC methodology changes, regulatory updates, or major security incidents)

---

# Executive Summary

This policy establishes [Organization]'s Secure Development Framework, implementing ISO/IEC 27001:2022 Controls A.8.26 (Application Security Requirements), A.8.25 (Secure Development Lifecycle), and A.8.29 (Security Testing in Development and Acceptance) as a unified security framework.

**Purpose**: Define organizational requirements for secure software development throughout the software development lifecycle (SDLC). This policy establishes WHAT security practices are required, WHEN they must be applied, and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8 (UG/TG variants).25-26-29 Implementation Guides.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG (data protection by design), EU GDPR Article 25 (data protection by design and default), and ISO/IEC 27001:2022.

---

# Scope

## In Scope

**Applications**:

- All internally developed applications (web, mobile, desktop, embedded, APIs)
- Acquired applications requiring customization or integration
- Infrastructure-as-Code (IaC) and configuration management code

**Development Activities**:

- New application development
- Application enhancements and security patches
- Application modernization and cloud migration

**Development Models**:

- Internal development teams
- Outsourced development (contractors, offshore teams)
- Hybrid development models

**SDLC Methodologies**:

- Waterfall, Agile/Scrum, DevOps/DevSecOps
- Continuous delivery and continuous deployment (CI/CD)

## Out of Scope

- Commercial Off-The-Shelf (COTS) software without customization (covered by vendor security assessment)
- Production vulnerability management post-deployment (covered by ISMS-POL-A.8.8)
- Operational security monitoring (covered by ISMS-POL-A.8.15-16)

---

# ISO/IEC 27001:2022 Control Statements

**A.8.26 - Application Security Requirements**
> *Information security requirements should be identified, specified and approved when developing or acquiring applications.*

**A.8.25 - Secure Development Lifecycle**
> *Rules for the secure development of software and systems should be established and applied.*

**A.8.29 - Security Testing in Development and Acceptance**
> *Security testing processes should be defined and implemented in the development life cycle.*

---

# Policy Statements

## Application Risk Classification (A.8.26)

[Organization] SHALL classify all applications by risk level to determine appropriate security requirements.

**High-Risk Applications** meet ANY of these criteria:

- Processes Confidential or Restricted data
- Handles personally identifiable information (PII) subject to GDPR, FADP
- Internet-facing or accessible by external parties
- Critical business function or financial transaction processing
- Payment card information (PCI DSS v4.0.1 scope)

**Medium-Risk Applications** meet ANY of these criteria:

- Processes Internal Use data
- Limited PII exposure (names, email addresses only)
- Internal-only access
- Important but not critical business function

**Low-Risk Applications** meet ALL of these criteria:

- Processes only Public data
- No PII, no sensitive business data
- Non-critical business function

## Security Requirements Specification (A.8.26)

[Organization] SHALL specify security requirements for all applications based on risk classification.

**Mandatory Requirements by Risk Level**:

| Requirement | High-Risk | Medium-Risk | Low-Risk |
|-------------|-----------|-------------|----------|
| Security Requirements Specification | Mandatory | Mandatory | Basic checklist |
| Threat Modeling | Mandatory | Recommended | Optional |
| Security Architecture Review | Mandatory | Recommended | Optional |
| Requirements Traceability | Mandatory | Recommended | Optional |

**Security Requirements SHALL address**:

- Authentication and authorization controls
- Input validation and output encoding
- Cryptography (data in transit and at rest)
- Session management
- Error handling and logging
- API security (where applicable)
- Data protection and privacy requirements

**Threat Modeling Methodology**:
High-Risk applications SHALL use a structured threat modeling methodology (e.g., STRIDE, PASTA, or Attack Trees). Threat modeling templates and guidance are provided in **ISMS-IMP-A.8.25-26-29-S1 (Security Requirements Process)**.

## Secure Development Lifecycle Integration (A.8.25)

[Organization] SHALL integrate security activities into all SDLC phases.

**Security Gates by Phase**:

| Phase | Security Gate | Approval Authority |
|-------|---------------|-------------------|
| Requirements | Security requirements approved | Security Architect |
| Design | Architecture approved, threat model complete | Security Architect (CISO for High-Risk) |
| Development | Security defects below threshold | Development Manager |
| Testing | Security testing passed | Security Architect |
| Deployment | Production security validated | CISO (High-Risk), Security Architect (Medium) |

**Mandatory Security Activities**:

- Apply secure coding standards (per ISMS-POL-A.8.28)
- Conduct code review (peer review for all code, security review for high-risk code)
- Deploy security tools (SAST, SCA, secret scanning)
- Track and remediate security defects
- Complete developer security training

## Security Testing Requirements (A.8.29)

[Organization] SHALL implement security testing based on application risk classification.

**Required Testing by Risk Level**:

| Testing Type | High-Risk | Medium-Risk | Low-Risk |
|--------------|-----------|-------------|----------|
| SAST (Static Analysis) | Per commit/daily | Per commit/daily | Weekly |
| SCA (Dependency Scanning) | Daily/continuous | Daily/continuous | Weekly |
| DAST (Dynamic Testing) | Per deployment/weekly | Monthly | Optional |
| Penetration Testing | Annually + major releases | Every 2 years | Optional |
| Security Acceptance Testing | Per deployment | Per deployment | Basic checklist |

**Tool Selection and Maintenance**:
Security testing tools SHALL be selected based on criteria documented in **ISMS-REF-A.8.25-26-29 (Security Testing Tools Reference)**, including coverage of required vulnerability classes, integration with CI/CD pipelines, and vendor support. Current toolset is maintained in [Security Tools Register].

**Software Bill of Materials (SBOM)**:
- High-Risk applications SHALL maintain an SBOM in CycloneDX or SPDX format
- SBOMs SHALL be generated automatically during build process and stored in [SBOM Repository]
- SBOMs SHALL be updated upon dependency changes and reviewed quarterly for known vulnerabilities

## Vulnerability Remediation Requirements (A.8.29)

[Organization] SHALL remediate security vulnerabilities within defined timeframes.

**Remediation Service Level Agreements**:

| Severity | CVSS Score | Remediation SLA | Deployment Impact |
|----------|------------|-----------------|-------------------|
| Critical | 9.0-10.0 | 7 days | Block deployment if unresolved |
| High | 7.0-8.9 | 30 days | Block deployment if overdue |
| Medium | 4.0-6.9 | 90 days | Track as technical debt |
| Low | 0.1-3.9 | 180 days | Plan for next major release |

## Failure Mode Management

[Organization] SHALL define procedures for handling security control failures and exceptions.

**Security Gate Bypass**:
- Emergency deployments bypassing security gates require CISO approval + retrospective security validation within 72 hours
- Bypassed gates SHALL be logged in [Release Management System] with justification and remediation timeline

**SLA Overrun Escalation**:
- Vulnerabilities exceeding remediation SLA SHALL be escalated:
  - **Critical (7 days)**: Automatic escalation to CISO + Application Owner + Risk Committee
  - **High (30 days)**: Escalation to CISO + Application Owner
  - **Medium (90 days)**: Escalation to Security Architect + Development Manager
- Overdue vulnerabilities SHALL block subsequent deployments until remediated or exception approved

**Exception Expiration**:
- Expired exceptions SHALL trigger automatic revocation of deployment approval
- Applications with expired exceptions SHALL be removed from production or moved to remediation queue within 14 days

**Failure Tracking**:
- All failures (bypassed gates, SLA overruns, exception expirations) SHALL be logged in [Gap Register / Risk Register] with remediation status

## Outsourced Development Requirements (A.8.25)

[Organization] SHALL apply secure development requirements to outsourced and third-party development.

**Contractual Requirements**:

- Security requirements and secure coding standards compliance
- Security testing requirements (SAST, DAST, SCA)
- Vulnerability remediation SLAs
- Security incident notification requirements
- Code review and security architecture review rights

**Verification of Contractor Compliance**:
[Organization] SHALL verify contractor adherence to secure development requirements through:
- **Quarterly reporting**: Contractors SHALL submit security testing reports (SAST/DAST/SCA results, remediation status) to Application Security Lead
- **Access to contractor tools**: [Organization] SHALL maintain read-only access to contractor SAST/DAST platforms or receive exported reports
- **Periodic audits**: High-Risk outsourced projects SHALL undergo security review by [Organization] Security Architects at major milestones (design approval, pre-production)
- **Contractual audit rights**: Contracts SHALL include [Organization] right to audit contractor security practices upon 30-day notice

## Developer Security Training (A.8.25)

[Organization] SHALL provide security training for all developers.

**Training Requirements**:

| Training Type | Audience | Frequency | Duration |
|---------------|----------|-----------|----------|
| Initial Security Training | All Developers | Before production code | 4 hours minimum |
| Annual Refresher | All Developers | Annually | 2 hours minimum |
| Security Champion Training | Security Champions | Initial + Annual | 8 hours + 4 hours |

---

# Roles and Responsibilities

## Governance

| Role | Responsibility |
|------|----------------|
| **CEO** | Ultimate accountability for secure development framework; approves policy; allocates resources |
| **CISO** | Overall accountability for framework implementation; policy governance; escalation authority |
| **Application Security Lead** | Framework implementation ownership; security tool program; training program oversight |

## Security Team

| Role | Responsibility |
|------|----------------|
| **Security Architects** | Security requirements review; architecture review; threat modeling; security design guidance |
| **Security Analysts** | Assessment execution; vulnerability triage; security testing; metrics reporting |
| **Penetration Testers** | Penetration testing execution; vulnerability validation; security testing methodology |

## Development Organization

| Role | Responsibility |
|------|----------------|
| **Development Manager** | SDLC security integration; training support; code review enforcement; defect remediation oversight |
| **Security Champions** | Security advocacy within teams; security code review; secure coding mentorship |
| **Developers** | Security requirements implementation; secure coding adherence; vulnerability remediation |
| **Solution Architects** | Security architecture design; threat modeling participation; technical security decisions |

## Quality Assurance

| Role | Responsibility |
|------|----------------|
| **QA Manager** | Security testing integration; security acceptance testing coordination |
| **QA Engineers** | Security test case execution; DAST operation; security defect reporting |

## DevOps

| Role | Responsibility |
|------|----------------|
| **DevOps Lead** | Security tool integration into CI/CD; security gate implementation |
| **DevOps Engineers** | CI/CD security automation; production security configuration |

## Application Management

| Role | Responsibility |
|------|----------------|
| **Product Manager / Application Owner** | Application risk classification; security requirements initiation; exception requests |

---

# Governance and Compliance

## Assessment and Verification

[Organization] SHALL verify secure development control effectiveness through structured assessment.

**Assessment Frequency**:

| Scope | Frequency |
|-------|-----------|
| Comprehensive framework assessment | Annually |
| High-Risk applications verification | Quarterly |
| Medium-Risk applications verification | Semi-annually |
| Low-Risk applications verification | Annually |
| Triggered assessment (incidents, audit findings) | Within 30 days |

**Assessment Methodology**:
Assessment procedures are documented in **ISMS-IMP-A.8.25-26-29-S5 (Secure Development Assessment)**. Assessments SHALL include:
- Review of application risk classification currency (verify classification remains accurate)
- Evidence sampling (SAST/DAST/SCA reports, penetration test reports, security gate approvals)
- Remediation SLA compliance verification (check overdue vulnerabilities)
- Security training completion verification (confirm developers/security champions trained)
- Exception review (verify active exceptions are still justified and compensating controls are effective)

## Evidence Collection and Retention

[Organization] SHALL maintain verifiable evidence of secure development control implementation.

**Evidence Types and Storage**:

| Control Activity | Evidence Type | Storage Location | Retention Period |
|------------------|---------------|------------------|------------------|
| Application risk classification | Risk assessment records | [GRC Platform / Risk Register] | Lifecycle of application + 3 years |
| SAST execution | Tool execution logs, findings reports | [SAST Platform - e.g., GitHub Security/Snyk/SonarQube] | 2 years |
| DAST execution | Scan reports, validated findings | [DAST Platform / Security Testing Repository] | 2 years |
| SCA execution | Dependency scan reports, SBOM updates | [SCA Platform / SBOM Repository] | 2 years |
| Penetration testing | Test reports, remediation verification | [Security Team Document Repository] | 5 years |
| Security gate approvals | Approval records (architecture review, deployment sign-off) | [Release Management System / Jira] | 3 years |
| Vulnerability remediation | Remediation tickets with SLA tracking | [Issue Tracking System / Jira Security] | 3 years |
| Security training completion | Training records | [HR System / LMS] | Lifecycle of employment + 3 years |
| Exception approvals | Exception requests, approvals, review records | [GRC Platform / Exception Register] | Duration of exception + 3 years |

**Evidence Validation**:
- Security Architects SHALL review SAST/DAST/SCA findings monthly to validate remediation progress and triage false positives
- Application Security Lead SHALL conduct quarterly evidence sampling audits to verify evidence completeness and accuracy

## Gap Remediation and Tracking

[Organization] SHALL maintain a centralized gap register for secure development control deficiencies.

**Gap Identification Sources**:
- Quarterly/semi-annual/annual assessments (per Assessment Frequency table)
- Security testing findings (SAST/DAST/SCA/penetration tests)
- Security gate failures or SLA overruns
- Audit findings (internal/external)
- Security incidents related to application vulnerabilities

**Gap Register Requirements**:

| Field | Description |
|-------|-------------|
| Gap ID | Unique identifier |
| Control ID | ISO 27001 control(s) affected (A.8.25, A.8.26, A.8.29) |
| Application | Affected application(s) |
| Description | Specific deficiency identified |
| Risk Rating | High/Medium/Low (based on application risk classification) |
| Owner | Assigned remediation owner (Development Manager / Security Architect) |
| Due Date | Remediation deadline (per SLA or exception timeline) |
| Status | Open / In Progress / Closed / Exception Approved |
| Closure Evidence | Reference to verification evidence (test report, code review, deployment confirmation) |

**Gap Closure Verification**:
- Security Architects SHALL verify gap closure before marking status as "Closed"
- Application Security Lead SHALL review monthly gap register to track overdue items and escalate high-risk gaps

**Gap Register Location**: [GRC Platform / Jira Security / SharePoint Gap Register]

## Exception Management

**Exception Request Requirements**:

- Documented business or technical justification
- Risk assessment and residual risk evaluation
- Proposed compensating controls
- Timeline for achieving full compliance

**Approval Authority**:

| Application Risk | Approval Authority |
|------------------|-------------------|
| Low-Risk | Security Architect |
| Medium-Risk | CISO |
| High-Risk | CISO + Risk Committee (for high-impact risks) |

## Policy Review

**Review Triggers**:

- Annual scheduled review
- Regulatory changes affecting secure development
- Major security incidents
- Significant SDLC methodology or technology changes
- Audit findings requiring policy updates

**Update Authority**:

- Minor updates (clarifications, references): CISO approval
- Major updates (scope, requirements changes): Full approval chain

---

# Regulatory Framework

## Mandatory Compliance (Tier 1)

**ISO/IEC 27001:2022**

- Controls: A.8.25, A.8.26, A.8.29
- Requirements: Documented policies, procedures, evidence of implementation

**Swiss Federal Data Protection Act (FADP/nDSG)**

- Article 8: Technical and organizational measures for data protection
- Article 26: Security by design and by default

**EU General Data Protection Regulation (GDPR)**

- Article 25: Data protection by design and by default
- Article 32: Security of processing

## Conditional Compliance (Tier 2)

Sector-specific requirements apply where [Organization]'s business activities trigger applicability:

| Regulation | Applicability Trigger | Key Requirements |
|------------|----------------------|------------------|
| DORA | EU financial entity | ICT risk management, resilience testing |
| NIS2 | Essential/important entity | Cybersecurity risk management |
| FINMA Circular 2023/1 | Swiss financial institution | Security for financial applications |
| PCI DSS v4.0.1 | Payment card processing | Requirement 6: Secure development |

**Refer to ISMS-POL-00 (Regulatory Applicability Framework) for complete regulatory categorization.**

---

# Related Documents

## Policies

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-00 | Regulatory Applicability Framework | Regulatory tier classification |
| ISMS-POL-A.8.28 | Secure Coding | Secure coding standards |
| ISMS-POL-A.8.4 | Access to Source Code | Repository security |
| ISMS-POL-A.8.31 | Separation of Environments | Dev/test/prod isolation |
| ISMS-POL-A.8.32 | Change Management | Security sign-off in releases |
| ISMS-POL-A.8.8 | Vulnerability Management | Production vulnerabilities |

## Implementation Guides

| Document ID | Title | Content |
|-------------|-------|---------|
| ISMS-IMP-A.8.25-26-29-S1 | Security Requirements Process | Requirements elicitation, threat modeling |
| ISMS-IMP-A.8.25-26-29-S2 | SDLC Security Integration | Security activities by phase |
| ISMS-IMP-A.8.25-26-29-S3 | Secure Coding Practices | Code review, tool deployment |
| ISMS-IMP-A.8.25-26-29-S4 | Security Testing Implementation | SAST/DAST/SCA configuration |
| ISMS-IMP-A.8.25-26-29-S5 | Secure Development Assessment | Assessment methodology, compliance |

## Reference Materials

| Document ID | Title | Content |
|-------------|-------|---------|
| ISMS-REF-A.8.25-26-29 | Security Testing Tools Reference | Tool comparison, selection criteria |
| ISMS-CTX-A.8.25-26-29 | SDLC Security Evolution | Industry context, awareness |

---

# Definitions

| Term | Definition |
|------|------------|
| **Application** | Software system developed, acquired, or integrated by [Organization] |
| **DAST** | Dynamic Application Security Testing - analyzes running applications |
| **Penetration Testing** | Manual security testing by qualified professionals |
| **SAST** | Static Application Security Testing - analyzes source code |
| **SCA** | Software Composition Analysis - identifies dependency vulnerabilities |
| **SDLC** | Software Development Lifecycle |
| **Security Champion** | Developer with specialized security training serving as team security contact |
| **Threat Modeling** | Structured approach to identify security threats in application design |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Application Security Lead** | [Name] | [Date to be set] |
| **Development Manager** | [Name] | [Date to be set] |
| **Legal/Compliance Officer** | [Name] | [Date to be set] |
| **Chief Executive Officer (CEO)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for secure software development. Implementation procedures (HOW) are documented in ISMS-IMP-A.8 (UG/TG).25-26-29 Implementation Guides. Technical tool guidance is provided in ISMS-REF-A.8.25-26-29.*

<!-- QA_VERIFIED: 2026-02-02 -->
