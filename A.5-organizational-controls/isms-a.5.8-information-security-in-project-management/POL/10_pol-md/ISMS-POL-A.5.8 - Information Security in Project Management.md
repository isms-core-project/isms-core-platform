**ISMS-POL-A.5.8 - Information Security in Project Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Security in Project Management |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.8 |
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
| 1.0 | [Date to be set] | CISO | Initial policy framework |

**Review Cycle**: Annual
**Next Review Date**: [Date to be set]

---

# Executive Summary

This policy establishes [Organization]'s requirements for integrating information security into project management to ensure security risks are systematically addressed throughout the project lifecycle in accordance with ISO/IEC 27001:2022 Control A.5.8.

**Purpose**: Define organizational requirements for information security integration into project management processes. This policy establishes WHAT security activities are required at each project phase and WHO is accountable for security outcomes.

**Scope**: This policy applies to all projects undertaken by [Organization], regardless of project type, methodology, complexity, size, duration, or organizational scope, including projects managed by internal teams, external vendors, or hybrid structures.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG (Art. 8), EU GDPR (Art. 25), and ISO/IEC 27001:2022. Conditional sector-specific requirements (NIS2, DORA, FINMA) apply where [Organization]'s business activities trigger applicability.

---

# Scope and Applicability

## ISO/IEC 27001:2022 Control A.5.8

> *Information security should be integrated into project management.*

**Control Objective**: Ensure information security risks associated with projects and project deliverables are systematically identified, assessed, and treated throughout the project lifecycle.

## In Scope

This policy applies to:

- **IT projects**: Software development, system implementation, infrastructure deployment
- **Business projects**: Process redesign, organizational change, merger/acquisition activities
- **Infrastructure projects**: Data center construction, facility modifications, equipment installation
- **Compliance projects**: Regulatory implementation, audit remediation, certification programs
- Projects of all sizes and durations
- Projects regardless of management methodology (Agile, Waterfall, hybrid)
- Projects managed by internal teams, external vendors, or hybrid teams
- All project phases: Initiation, planning, execution, monitoring/control, closure


## Out of Scope

- Routine operational activities not constituting a project (business-as-usual maintenance)
- Emergency incident response activities (covered under A.5.24-27 Incident Management)
- Minor changes managed through change control process (covered under A.8.32 Change Management)


## Regulatory Requirements

**Tier 1 - Mandatory Compliance**:

- Swiss nDSG (Art. 8): Appropriate technical and organizational measures
- EU GDPR (Art. 25, 32): Data protection by design and by default
- ISO/IEC 27001:2022: Control A.5.8 information security in project management


**Tier 2 - Conditional Applicability** (per ISMS-POL-00):

- NIS2, DORA, FINMA Circular 2008/21, PCI DSS v4.0 - apply when business conditions trigger applicability


---

# Policy Statements

## Project Security Integration Principles

[Organization] SHALL integrate information security into all projects based on the following principles:

| Principle | Requirement | Application Example |
|-----------|-------------|---------------------|
| **Early Integration** | Security SHALL be considered from project initiation, not added retrospectively | Project charter includes security classification; security resources allocated in project budget before planning phase |
| **Proportionality** | Security effort SHALL be proportional to project risk classification | Low Risk internal tool receives checklist validation (2 hours); High Risk customer portal receives penetration testing (40 hours) |
| **Lifecycle Coverage** | Security activities SHALL occur at all project phases | Security review at each phase gate; security requirements in planning, testing in execution, handover at closure |
| **Risk-Based** | Security decisions SHALL be based on risk assessment | Security controls selected based on threat modeling and data classification, not generic checklists |
| **Traceable Requirements** | Security requirements SHALL be documented and tracked to implementation | Security Requirements Register links each requirement to design element, test case, and deployment evidence |
| **Lessons Learned** | Project security experiences SHALL feed continuous improvement | Post-project security review identifies control gaps; findings update security requirements templates |

## Project Classification Requirement

All projects SHALL be classified based on information security impact to determine proportional security requirements.

**Classification Factors and Decision Matrix**:

Projects SHALL be classified based on the highest applicable factor:

| Factor | High Risk | Medium Risk | Low Risk |
|--------|-----------|-------------|----------|
| **Data Sensitivity** | Critical/Confidential data (PII, payment data, IP, confidential business information per A.5.12) | Internal data (non-public business data, employee records) | Public data (marketing content, published documentation) |
| **System Criticality** | RTO < 4 hours, revenue-generating system, customer-facing service | RTO 4-24 hours, business-important but not revenue-critical | RTO > 24 hours, operational support system |
| **Regulatory Scope** | GDPR/PCI DSS/FINMA directly applicable | Swiss nDSG applicable | No regulated data processing |
| **External Exposure** | Internet-facing or accessible to external parties (customers, partners, public) | Controlled external access (VPN, dedicated connection) | Internal-only access |
| **Technical Complexity** | New architecture pattern, novel integrations, custom security controls | Standard architecture with moderate customization | Standard deployment, proven architecture |
| **Third-Party Involvement** | Critical function outsourced (hosting, authentication, payment processing) | Vendor-managed components (SaaS integration, managed services) | Fully internal development and hosting |

**Classification Logic**: If **any factor** meets High Risk criteria → classify as **High Risk**. If **any factor** meets Medium Risk criteria (and no High Risk factors) → classify as **Medium Risk**. If **all factors** meet Low Risk criteria → classify as **Low Risk**.

**Classification Documentation**: Classification determination and rationale SHALL be documented in project charter and approved per approval authority below.

**Classification Levels**:

| Classification | Description | Approval Authority |
|----------------|-------------|-------------------|
| **High Risk** | Critical information security impact | CISO approval required |
| **Medium Risk** | Moderate information security impact | Information Security Officer approval |
| **Low Risk** | Minimal information security impact | Project Manager self-classifies with InfoSec review |

Classification SHALL be reviewed at each phase gate and updated if scope, data sensitivity, or external exposure changes materially.

## Phase Gate Security Requirements

[Organization] SHALL integrate security reviews into project governance at the following phase gates:

| Phase Gate | Security Criteria Required |
|------------|---------------------------|
| **Project Approval** | Security classification determined; Initial security risks identified; Security budget allocated |
| **Planning Approval** | Security requirements documented and approved; Security resources committed |
| **Execution Checkpoint** | Security testing conducted; Critical findings remediated |
| **Deployment Approval** | All Critical/High findings remediated or accepted; Security handover documentation complete |
| **Project Closure** | Residual risks formally accepted; Lessons learned documented; Assets registered |

Projects SHALL NOT proceed to the next phase until security criteria for the current phase are met or formally accepted by the appropriate authority.

## Security Requirements Identification

Security requirements for project deliverables SHALL be identified systematically using the following process:

**Requirement Identification Process**:

1. **Applicability Assessment**: Project Manager, with InfoSec Officer support, reviews each security requirement category against project scope:
   - Application security (A.8.25-28): Applicable if project includes software development or custom code
   - Data protection (A.8.24, GDPR/nDSG): Applicable based on data classification per A.5.12
   - Access control (A.5.15-18): Applicable for all projects (minimum: access control policy compliance)
   - Infrastructure security (A.8.20-22): Applicable if project affects network architecture or deploys infrastructure
   - Third-party security (A.5.19-22): Applicable if project involves external vendors or cloud services
   - Regulatory requirements (ISMS-POL-00): Applicable based on Tier 1/2 analysis

2. **Requirement Scoping**: For applicable categories, specific requirements are selected based on:
   - Data classification (Critical/Confidential/Internal/Public per A.5.12)
   - System criticality (RTO/RPO requirements per A.5.29-30)
   - Threat profile (per A.5.7 threat intelligence and project-specific threat modeling)
   - Regulatory obligations (per ISMS-POL-00 Tier 1/2 mandatory requirements)

3. **Documentation**: Applicable requirements SHALL be documented in:
   - **Medium/High Risk projects**: Security Requirements Register (formal tracking tool)
   - **Low Risk projects**: Project Risk Register (security requirements as risk mitigation items)

4. **Approval**: Requirements SHALL be reviewed and approved by:
   - **High Risk projects**: CISO approval before project execution phase
   - **Medium Risk projects**: InfoSec Officer approval before project execution phase
   - **Low Risk projects**: InfoSec Officer confirmation of requirement completeness

**Detailed requirement identification procedures, category-specific checklists, and Security Requirements Register template are provided in ISMS-IMP-A.5.8.**

## Security Testing Requirement

All projects SHALL include security testing proportional to project classification, with testing scope determined as follows:

**Security Testing Requirements by Classification**:

- **High Risk Projects**:
  - **Mandatory**: External penetration testing (OWASP methodology or equivalent), automated vulnerability scanning (weekly during development + final pre-deployment scan), security code review for custom code (minimum 20% coverage of authentication, authorization, data protection, and cryptographic functions)
  - **Testing Criteria**: Penetration testing SHALL be performed by independent third party (not project team). All Critical findings and ≥80% of High findings SHALL be remediated before deployment.

- **Medium Risk Projects**:
  - **Mandatory**: Automated vulnerability scanning (final pre-deployment scan), functional security testing of authentication, authorization, data validation, and error handling
  - **Conditional**: Penetration testing required if project is internet-facing OR processes regulated data (GDPR/PCI DSS)
  - **Testing Criteria**: All Critical findings and ≥70% of High findings SHALL be remediated before deployment.

- **Low Risk Projects**:
  - **Mandatory**: Security validation against security requirements checklist (minimum: A.5.15-18 access control verification, A.8.24 encryption verification if applicable)
  - **Optional**: Automated vulnerability scanning (recommended but not required)
  - **Testing Criteria**: Critical findings SHALL be remediated before deployment.

**Testing Sufficiency Documentation**: For Medium/High Risk projects, testing adequacy SHALL be documented in security assessment report and approved by InfoSec Officer (Medium) or CISO (High) before deployment authorization. If remediation target is not achieved, residual risk SHALL be formally accepted per Exception Management section.

**Testing evidence (scan reports, penetration test reports, code review findings) SHALL be archived per A.5.33 and provided in security handover documentation.**

## Security Handover Requirement

At project closure, security handover documentation SHALL be provided to operations and validated as complete before project closure authorisation.

**Security Handover Completeness Criteria**:

Security handover SHALL include the following documentation, delivered to operational owner and confirmed complete via handover checklist:

1. **Security Architecture Documentation**:
   - System security design (trust boundaries, authentication/authorisation model, encryption implementation)
   - Data flow diagrams showing data classification and protection controls
   - Network architecture (firewall rules, network segmentation, external access points)
   - Integration security (API authentication, third-party service dependencies)

2. **Operational Security Procedures**:
   - Monitoring requirements (security log sources, alert thresholds, SIEM integration)
   - Log retention requirements (per A.8.15, regulatory retention periods)
   - Backup and recovery procedures (per A.8.13, including security-specific restoration testing)
   - Incident response escalation (security incident types, escalation paths, contact information)
   - Security patch management (update frequency, testing requirements, rollback procedures)

3. **Accepted Residual Risks**:
   - Formal risk acceptance records with approval signatures (per risk classification authority)
   - Compensating controls (if applicable)
   - Risk re-assessment timeline (for time-limited acceptances)

4. **Security Testing Evidence**:
   - Final vulnerability scan report (dated within 7 days of deployment)
   - Penetration test report (if applicable per Security Testing Requirement)
   - Remediation records for Critical/High findings (or risk acceptance for unresolved findings)

**Handover Validation Process**: Operations SHALL confirm handover completeness via signed Security Handover Checklist (template in ISMS-IMP-A.5.8) before Project Manager requests project closure authorisation. Incomplete handover documentation blocks project closure until gaps are resolved or explicitly accepted by operational owner and CISO (for High Risk projects).

**Handover documentation is archived per A.5.33 records management requirements and maintained as operational baseline documentation for system lifecycle.**

---

# Roles and Responsibilities

## Executive Management

**Accountability**: Overall organizational security, including project security integration.

**Responsibilities**:

- Approve this policy and ensure organizational resources for implementation
- Review high-risk project security status in management reviews
- Accept residual risks for critical projects


## Chief Information Security Officer (CISO)

**Accountability**: Information security program implementation, including project security oversight.

**Responsibilities**:

- Approve and maintain this policy
- Approve High Risk project classifications
- Accept residual security risks for High Risk projects
- Provide security resources for project support
- Monitor project security metrics and report to Executive Management
- Approve exceptions to security requirements


**Authority**: Halt or delay projects with unacceptable security risks; mandate additional security controls.

## Information Security Officer / Security Team

**Accountability**: Operational security guidance and risk assessment support.

**Responsibilities**:

- Support project teams in security risk assessment and requirements identification
- Review and approve Medium Risk project classifications
- Review security requirements and provide technical guidance
- Conduct or commission security testing
- Maintain security requirements templates and checklists


**Authority**: Escalate security concerns to CISO; recommend project delays for unmitigated risks.

## Project Manager

**Accountability**: Overall project success, including security requirements implementation.

**Responsibilities**:

- Classify project security risk level (with InfoSec Officer support)
- Ensure security activities are planned and budgeted
- Execute security activities at each project phase
- Maintain project security risk register
- Escalate security risks and issues
- Document security aspects in project closure and handover


**Authority**: Allocate project resources to security activities; request security support from InfoSec team.

## Business Owner / Product Owner

**Accountability**: Business requirements, including security needs of project deliverables.

**Responsibilities**:

- Define business security requirements
- Participate in security risk assessment
- Approve security requirements as part of project scope
- Accept residual security risks for owned systems/services


## Technical Lead / Solution Architect

**Accountability**: Technical design and implementation, including security architecture.

**Responsibilities**:

- Design security controls into solution architecture
- Implement security requirements per specifications
- Support threat modeling and security architecture reviews
- Address security findings from testing or reviews


## Third-Party Vendors / Contractors

**Accountability**: Security of vendor-delivered components and services per contract.

**Responsibilities**:

- Comply with [Organization]'s security requirements in contracts
- Participate in security assessments and provide required evidence
- Report security incidents or vulnerabilities to [Organization]


## RACI Matrix for Project Security Activities

| Activity | PM | InfoSec | CISO | Business Owner | Tech Lead |
|----------|----|---------| -----|----------------|-----------|
| Project classification | R | A | I | C | C |
| Security requirements identification | R | A | I | C | C |
| Security architecture design | C | C | I | I | R/A |
| Security testing execution | R | C | I | I | R |
| Residual risk acceptance | I | C | A (High) | A (Medium/Low) | I |
| Security handover review | R | A | I | C | C |

R = Responsible (does the work), A = Accountable (final decision), C = Consulted (provides input), I = Informed (kept updated)

---

# Governance and Exception Management

## Security Review Authority

| Project Classification | Review Authority |
|------------------------|------------------|
| Low Risk | Project Manager self-assessment |
| Medium Risk | Information Security Officer review required |
| High Risk | CISO approval required |

## Escalation

Security concerns SHALL be escalated within:

- 2 business days for High Risk projects
- 5 business days for Medium Risk projects

**Escalation Path**: Project Manager -> Information Security Officer -> CISO -> Executive Management

**Escalation Triggers**:

Security concerns requiring escalation include:

- **Mandatory Escalation**:
  - Critical security findings that cannot be remediated before deployment deadline
  - Security requirements that conflict with business objectives (requiring risk acceptance)
  - Third-party vendor unable to meet security requirements
  - Data breach or security incident affecting project deliverables
  - Regulatory compliance concerns identified during project execution

- **Discretionary Escalation**:
  - Security architecture decisions with significant long-term implications
  - Budget constraints affecting security control implementation
  - Timeline pressure requiring security testing shortcuts

Routine security guidance (requirement interpretation, control selection, testing procedures) SHALL be managed via InfoSec Officer support without escalation unless decision authority exceeds project team scope.

## Exception Management

Exceptions to security requirements SHALL be:

- Documented with business justification and compensating controls
- Approved by appropriate authority based on project classification
- Time-limited and tracked in the Security Exception Register
- Reviewed quarterly by CISO


## Policy Review

This policy SHALL be reviewed:

- Annually (minimum) by CISO
- Upon major project failures with security root causes
- Upon regulatory changes affecting project security
- Upon significant organizational changes


---

# Compliance and Monitoring

## Compliance Requirements

| Requirement | Compliance Measure |
|-------------|-------------------|
| Project classification | All projects classified within 5 business days of initiation |
| Security requirements | Documented for all Medium/High Risk projects before execution |
| Security testing | Completed before deployment for all projects |
| Residual risk acceptance | Formally documented before project closure |
| Lessons learned | Captured for all Medium/High Risk projects |

## Monitoring and Metrics

[Organization] SHALL track project security metrics including:

- Projects by security classification
- Projects with completed security assessments
- Security findings by severity and remediation status
- Security exceptions granted

**Metrics Reporting Requirements**:

- **Monthly CISO Report**: Detailed metrics dashboard including:
  - Projects by classification and security status (on track / at risk / overdue)
  - Open security findings by severity and age
  - Security exceptions granted vs. remediated
  - Security testing completion rates
  - Action Required: CISO reviews for trends requiring intervention (e.g., >20% High Risk projects with overdue security assessments)

- **Quarterly Executive Report**: Executive summary including:
  - Total projects and high-risk project count
  - Critical security findings and remediation status
  - Security exceptions requiring executive awareness
  - Significant security incidents affecting projects
  - Action Required: Executive Management accepts residual risks for critical projects

Metrics are maintained in GRC Platform / Project Dashboard and accessible to authorised personnel per A.5.15-18 access control.

## Non-Compliance

Non-compliance with this policy may result in:

- Project delays until security requirements are met
- Escalation to Executive Management
- Disciplinary action per [Organization]'s HR policies


---

# Related Documents

## ISMS Documents

| Document ID | Document Title |
|-------------|----------------|
| ISMS-POL-00 | Regulatory Applicability Framework |
| ISMS-IMP-A.5.8 | Information Security in Project Management - Implementation Guide |
| ISMS-POL-A.5.15-18 | Identity and Access Management |
| ISMS-POL-A.5.19-22 | Supplier Relationship Security |
| ISMS-POL-A.8.24 | Use of Cryptography |
| ISMS-POL-A.8.25-28 | Secure Development Lifecycle |
| ISMS-POL-A.8.32 | Change Management |

## External References

| Reference | Description |
|-----------|-------------|
| ISO/IEC 27001:2022 | Information security management systems - Requirements |
| ISO/IEC 27002:2022 | Information security controls - Guidance |
| ISO 21500:2021 | Project, Programme and Portfolio Management |
| NIST SP 800-64 | Security Considerations in System Development Life Cycle |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:

- ✅ This policy document (ISMS-POL-A.5.8 v1.0)
- ✅ Approval signatures from CISO, CIO, Executive Management
- ✅ Project classification framework defined (Section 2.2)
- ✅ Phase gate security requirements documented (Section 2.3)
- ✅ Security requirements categories specified (Section 2.4)
- ✅ Security testing requirements by classification (Section 2.5)
- ✅ Security handover requirements documented (Section 2.6)
- ✅ Roles and responsibilities assigned (Section 3)
- ✅ Governance and exception procedures defined (Section 4)
- ✅ Integration with related controls documented (Section 6)


**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Project classification approvals showing security risk classification determinations (High/Medium/Low)
- Security requirements registers for Medium/High Risk projects
- Phase gate approval records with security criteria verification
- Security testing reports (penetration tests, vulnerability scans, code reviews) by project classification
- Security findings and remediation tracking to closure
- Security handover documentation packages
- Residual risk acceptance records with appropriate approvals
- Lessons learned documentation for Medium/High Risk projects
- Security exception register with approvals and time limits
- Project security metrics dashboards showing trends
- Training records for project managers on security requirements
- Security assessment workbook outputs (from ISMS-IMP-A.5.8)

## Clarification on Compliance Evidence

This policy establishes information security integration requirements for project management governance. It does NOT establish:

- **Specific technical security controls** (addressed in technical control policies A.8.x)
- **Project management methodology** (organizational choice - Agile, Waterfall, hybrid)
- **Vendor selection criteria** (addressed in A.5.19-22 Supplier Relationship Security)
- **Application security testing techniques** (addressed in A.8.25-28 Secure Development Lifecycle)

The boundary is: POL-A.5.8 defines WHAT security activities must occur at each project phase and WHO approves → ISMS-IMP-A.5.8 provides HOW to assess security requirements and track compliance → Technical controls (A.8.x) define specific security capabilities required.

---

# Approval Record

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Chief Information Security Officer (CISO)** | [Name] | | [Date to be set] |
| **Chief Information Officer (CIO)** | [Name] | | [Date to be set] |
| **Chief Operating Officer (COO)** | [Name] | | [Date to be set] |
| **Legal/Compliance Officer** | [Name] | | [Date to be set] |
| **Executive Management** | [Name] | | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for information security integration into project management. Implementation procedures, assessment templates, and detailed guidance are documented in ISMS-IMP-A.5.8.*

<!-- QA_VERIFIED: 2026-02-02 -->
