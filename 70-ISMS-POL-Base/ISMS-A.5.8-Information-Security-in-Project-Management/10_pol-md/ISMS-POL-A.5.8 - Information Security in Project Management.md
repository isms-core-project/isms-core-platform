# ISMS-POL-A.5.8 – Information Security in Project Management

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Information Security in Project Management |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.8 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [Date] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial policy framework (3 assessment domains) |

**Review Cycle**: Annual  
**Next Review Date**: 28.01.2027  

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO) / Chief Operating Officer (COO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.5.8 (Implementation Guidance Suite - 3 assessment workbooks)
- ISO/IEC 27001:2022 Control A.5.8
- ISO 21500:2021 (Project, Programme and Portfolio Management - Context and Concepts)
- ISO 21502:2020 (Project Management Guidance)

---

## Executive Summary

This policy establishes [Organization]'s requirements for integrating information security into project management to ensure security risks are systematically addressed throughout the project lifecycle in accordance with ISO/IEC 27001:2022 Control A.5.8.

**Scope**: This policy applies to all projects undertaken by [Organization], regardless of project type (IT, infrastructure, business process, facilities), methodology (Waterfall, Agile, hybrid), complexity, size, duration, or organizational scope. This includes projects managed by internal teams, external vendors, or hybrid project structures.

**Purpose**: Define organizational requirements for information security integration into project management processes. This policy establishes WHAT security activities are required at each project phase and WHO is accountable for security outcomes. Implementation procedures (HOW to execute security activities) are documented separately in ISMS-IMP-A.5.8.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG (Art. 8 - appropriate measures), EU GDPR (Art. 25 - data protection by design and default), and ISO/IEC 27001:2022. Conditional sector-specific requirements (NIS2, DORA, FINMA) apply where [Organization]'s business activities trigger applicability.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control A.5.8

**ISO/IEC 27001:2022 Annex A.5.8 - Information Security in Project Management**

> *Information security should be integrated into project management.*

**Control Objective**: Ensure information security risks associated with projects and project deliverables are systematically identified, assessed, and treated throughout the project lifecycle, preventing security being treated as an afterthought or omitted entirely.

**This Policy Addresses**:
- Integration of information security into project management methodology
- Information security risk assessment requirements at project phases
- Security requirements identification and documentation for project deliverables
- Roles and responsibilities for project security activities
- Project classification framework based on information security impact
- Security activities across project lifecycle (initiation, planning, execution, monitoring, closure)
- Governance and oversight of project security risks
- Integration with [Organization]'s risk assessment and treatment processes

### 1.2 What This Policy Does

This policy:
- **Defines** requirements for integrating information security into all projects
- **Establishes** project classification framework based on information security risk
- **Specifies** mandatory security activities at each project phase
- **Assigns** accountability for project security outcomes
- **References** applicable regulatory requirements per ISMS-POL-00
- **Integrates** project security with enterprise risk management framework

### 1.3 What This Policy Does NOT Do

This policy does NOT:
- **Specify project management methodology** (Agile, Waterfall, PRINCE2 selection based on project needs)
- **Define detailed security assessment procedures** (see ISMS-IMP-A.5.8 Implementation Guides)
- **Provide security requirements templates** (see ISMS-IMP-A.5.8.2 Security Requirements Register)
- **Define project governance structure** (uses [Organization]'s existing project governance)
- **Replace specialized security policies** (secure development A.8.25-28, supplier management A.5.19-22)
- **Specify project management tools** (tool selection based on [Organization]'s preferences)

**Rationale**: Separating policy requirements from implementation guidance enables:
- Policy stability despite evolving project methodologies and tooling
- Methodology flexibility (works with any project management approach)
- Clear distinction between governance (policy) and execution (implementation)
- Proportional security effort based on project risk classification
- Integration with existing project management practices without mandating specific frameworks

### 1.4 Scope

**This policy applies to**:
- All projects undertaken by [Organization], including:
  - **IT projects**: Software development, system implementation, infrastructure deployment
  - **Business projects**: Process redesign, organizational change, merger/acquisition activities
  - **Infrastructure projects**: Data center construction, facility modifications, equipment installation
  - **Compliance projects**: Regulatory implementation, audit remediation, certification programs
- Projects of all sizes and durations (1-week initiatives to multi-year programs)
- Projects regardless of management methodology (Agile, Waterfall, hybrid, custom)
- Projects managed by:
  - Internal project teams
  - External vendors or contractors
  - Hybrid internal-external teams
  - Third-party managed projects on behalf of [Organization]
- Project phases: Initiation, planning, execution, monitoring/control, closure
- All project deliverables that process, store, or transmit organizational information

**Out of Scope**:
- Routine operational activities not constituting a "project" (business-as-usual maintenance)
- Emergency incident response activities (covered under A.5.24-27 Incident Management)
- Minor changes managed through change control process (covered under A.8.32 Change Management)
- Personal or educational projects not involving organizational information assets

**Definition of "Project"**: For this policy, a project is a temporary endeavor with defined start/end dates, specific objectives, and producing unique deliverables. Organizations apply proportional security requirements based on project classification (see Section 2.2).

### 1.5 Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**. 

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG** | All Swiss operations | Art. 8 - Appropriate technical and organizational measures (includes security in system design) |
| **EU GDPR** | When processing EU personal data | Art. 25 - Data protection by design and by default; Art. 32 - Security measures |
| **ISO/IEC 27001:2022** | Certification scope | Control A.5.8 - Information security integrated into project management |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Project Security Requirements |
|-----------|-------------------|-------------------------------|
| **NIS2** | Essential/important entity (EU) | Art. 21(2) - Cybersecurity risk management measures, including in ICT development and acquisition |
| **DORA** | EU financial services entity | Art. 6(8) - ICT project and change management with risk assessment and testing |
| **FINMA Circular 2008/21** | Swiss regulated financial institution | Margin no. 56-58 - Project management with information security requirements and risk assessment |
| **PCI DSS v4.0** | Processing payment card data | Requirement 6.3 - Secure systems and software development lifecycle |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- ISO 21500:2021 - Project management guidance (context and concepts)
- ISO 21502:2020 - Project management guidance (implementation principles)
- NIST SP 800-64 Rev. 2 - Security Considerations in the System Development Life Cycle
- PMBOK® Guide (Project Management Body of Knowledge)
- PRINCE2® (Projects IN Controlled Environments)

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment per ISMS-POL-00. The most stringent requirements apply where multiple regulations overlap.

---

## 2. Requirements Framework

### 2.1 Project Security Integration Principles

[Organization]'s approach to project security integration is based on the following principles:

| Principle | Requirement | Implementation |
|-----------|-------------|----------------|
| **Early Integration** | Security considered from project initiation, not added retrospectively | Security risk assessment during project approval process |
| **Proportionality** | Security effort proportional to project risk and complexity | Project classification framework determines security requirements |
| **Lifecycle Coverage** | Security activities at all project phases | Phase-gate security reviews from initiation through closure |
| **Risk-Based** | Security decisions based on risk assessment, not checkbox compliance | Project-specific risk assessment informs security controls |
| **Traceable Requirements** | Security requirements documented and tracked to implementation/test | Requirements register with verification evidence |
| **Lessons Learned** | Project security experiences feed continuous improvement | Post-project reviews inform policy and procedure updates |

### 2.2 Project Classification Framework

[Organization] classifies projects based on information security impact to determine proportional security requirements.

**Classification Criteria**:

| Factor | Description | Risk Indicators |
|--------|-------------|-----------------|
| **Data Sensitivity** | Classification of information processed/stored by project deliverables | Restricted or Confidential data = High risk |
| **System Criticality** | Business impact if project deliverable fails or is compromised | Revenue-generating or customer-facing systems = High risk |
| **Regulatory Scope** | Applicability of regulatory requirements (GDPR, PCI DSS, FINMA, etc.) | Regulated data or processes = High risk |
| **External Exposure** | Internet-facing or accessible to external parties | Public internet exposure = Higher risk |
| **Complexity** | Technical complexity, number of integrations, architectural novelty | High complexity or novel technology = Higher risk |
| **Third-Party Involvement** | External vendors, contractors, or outsourced components | Significant third-party involvement = Additional controls required |

**Project Risk Classification**:

| Classification | Risk Level | Security Requirements | Examples |
|----------------|------------|----------------------|----------|
| **High Risk** | Critical information security impact | Comprehensive security assessment, dedicated security resources, CISO approval, detailed documentation | New customer-facing application processing payment data; Cloud migration of Confidential data; Integration with external partners handling Restricted information |
| **Medium Risk** | Moderate information security impact | Standard security assessment, security requirements documented, InfoSec review at key phases | Internal application development; Infrastructure upgrade affecting multiple systems; Third-party SaaS implementation |
| **Low Risk** | Minimal information security impact | Lightweight security checklist, self-assessment acceptable | Internal tool deployment (Public/Internal data only); Hardware refresh (no data migration); Process documentation projects |

**Classification Authority**: Project classification is determined jointly by Project Manager and Information Security Officer during project initiation. CISO reviews and approves High Risk project classifications.

**Classification Review**: Project classification is reviewed at each phase gate and updated if scope, data sensitivity, or external exposure changes materially.

### 2.3 Security Activities Across Project Lifecycle

**Mandatory security activities** are required at each project phase, with depth/rigor proportional to project classification.

#### 2.3.1 Project Initiation Phase

**Objective**: Identify information security risks early and establish security baseline.

**Required Activities**:

| Activity | High Risk Projects | Medium Risk Projects | Low Risk Projects |
|----------|-------------------|---------------------|-------------------|
| **Initial Risk Identification** | Formal risk workshop with Security Officer | Risk assessment questionnaire | Self-assessment checklist |
| **Project Classification** | CISO approval required | InfoSec Officer approval | PM self-classifies with InfoSec review |
| **Security Stakeholder Identification** | Dedicated Security Coordinator assigned | InfoSec Officer as stakeholder | InfoSec available for consultation |
| **High-Level Security Requirements** | Documented in project charter | Listed in project scope | Noted in project plan |
| **Budget/Resource Allocation** | Dedicated security budget line item | Security testing included in budget | Security activities in general PM time |

**Deliverables**: 
- Project classification determination (all projects)
- Initial security risk register (High/Medium projects)
- Security stakeholder matrix (High projects)

**Phase Gate Criterion**: Project cannot proceed to Planning phase without approved security classification and initial risk identification.

#### 2.3.2 Project Planning Phase

**Objective**: Define comprehensive security requirements and plan security activities.

**Required Activities**:

| Activity | High Risk Projects | Medium Risk Projects | Low Risk Projects |
|----------|-------------------|---------------------|-------------------|
| **Detailed Security Requirements** | Full requirements specification (see Section 2.4) | Key security requirements documented | High-level security considerations |
| **Threat Modeling** | Formal threat modeling workshop | Lightweight threat assessment | Standard threats considered |
| **Security Architecture Review** | Security Architect reviews design | InfoSec Officer reviews architecture | Standard architecture patterns used |
| **Security Test Planning** | Dedicated security test plan | Security testing integrated in test plan | Basic security checks in testing |
| **Vendor Security Assessment** | Comprehensive vendor security review | Standard vendor questionnaire | Vendor security terms in contract |
| **Data Protection Impact Assessment (DPIA)** | If processing Restricted personal data | If processing Confidential personal data | Not typically required |

**Deliverables**: 
- Security requirements register (all Medium/High projects)
- Security test plan (all Medium/High projects)
- Threat model (High projects)
- Security architecture documentation (High projects)

**Phase Gate Criterion**: Security requirements documented and approved by appropriate authority before execution phase begins.

#### 2.3.3 Project Execution Phase

**Objective**: Implement security controls and verify effectiveness through testing.

**Required Activities**:

| Activity | High Risk Projects | Medium Risk Projects | Low Risk Projects |
|----------|-------------------|---------------------|-------------------|
| **Security Control Implementation** | Implement per detailed requirements | Implement per documented requirements | Implement basic security controls |
| **Security Testing** | Penetration testing, vulnerability scanning, code review | Vulnerability scanning, functional security testing | Basic security validation |
| **Configuration Review** | Security configuration audit | Configuration checklist review | Standard secure configuration applied |
| **Documentation** | Security documentation complete (admin guides, security features) | Security setup documented | Basic operational documentation |
| **Security Training** | Administrator and user security training | User awareness for security features | Standard security awareness sufficient |

**Deliverables**: 
- Implemented security controls (all projects)
- Security test results (all Medium/High projects)
- Security configuration documentation (all Medium/High projects)
- Remediation evidence for identified vulnerabilities (all projects)

**Phase Gate Criterion**: Critical and High severity security findings remediated before production deployment. Medium/Low findings have approved remediation plan.

#### 2.3.4 Project Monitoring and Control Phase

**Objective**: Monitor security risks and control effectiveness throughout project execution.

**Required Activities**:

| Activity | High Risk Projects | Medium Risk Projects | Low Risk Projects |
|----------|-------------------|---------------------|-------------------|
| **Security Risk Monitoring** | Weekly security risk review | Bi-weekly or milestone reviews | Ad-hoc as issues arise |
| **Change Security Impact Assessment** | All changes assessed for security impact | Significant changes assessed | Major changes assessed |
| **Security Testing Updates** | Regression testing after security-relevant changes | Re-test after major changes | Re-test if security concerns |
| **Security Metrics Tracking** | Formal security KPIs tracked (vulnerabilities, coverage) | Basic security metrics (open findings) | Issues tracked in project management tool |

**Deliverables**: 
- Updated security risk register (High/Medium projects, ongoing)
- Security metrics dashboard (High projects)
- Change impact assessments (all projects, as needed)

**Continuous Activity**: Security risk monitoring is continuous throughout execution phase, not a one-time gate.

#### 2.3.5 Project Closure Phase

**Objective**: Ensure secure handover to operations and capture lessons learned.

**Required Activities**:

| Activity | High Risk Projects | Medium Risk Projects | Low Risk Projects |
|----------|-------------------|---------------------|-------------------|
| **Security Handover Documentation** | Comprehensive security documentation package | Security runbook and known issues | Basic security notes |
| **Operational Security Review** | Operations team trained, security procedures documented | Handover meeting with security topics | Standard operational handover |
| **Residual Risk Acceptance** | Formal risk acceptance by asset owner and CISO | Risk acceptance by asset owner | Risks noted in handover |
| **Asset Registration** | Assets registered in ISMS asset inventory (A.5.9) | Assets registered in inventory | Assets registered |
| **Security Lessons Learned** | Formal security review meeting | Security lessons documented | Security notes in project closure |
| **Closure Approval** | CISO sign-off for High Risk projects | InfoSec Officer sign-off | PM closure includes security checklist |

**Deliverables**: 
- Security handover documentation (all Medium/High projects)
- Accepted residual risks (all projects with open findings)
- Lessons learned documentation (all Medium/High projects)
- Updated asset inventory (all projects)

**Phase Gate Criterion**: Security handover complete and residual risks formally accepted before project closure approved.

### 2.4 Security Requirements Identification

Security requirements for project deliverables SHALL be identified systematically and documented in the project Security Requirements Register (see ISMS-IMP-A.5.8.2).

**Security Requirements Categories**:

#### 2.4.1 Application Security Requirements (A.8.26)

For software development or system implementation projects:

- Secure coding standards and practices
- Input validation and output encoding
- Authentication and authorization mechanisms
- Session management and secure state handling
- Cryptographic requirements (encryption, hashing, key management per A.8.24)
- Secure error handling and logging
- API security (authentication, rate limiting, input validation)
- Security testing requirements (SAST, DAST, penetration testing)

**Source**: OWASP Top 10, OWASP ASVS, secure development lifecycle (A.8.25-28)

#### 2.4.2 Data Protection Requirements

For projects processing, storing, or transmitting organizational data:

- Data classification requirements (per [Organization]'s data classification scheme)
- Encryption requirements (in transit per A.8.24, at rest for Confidential/Restricted data)
- Data retention and deletion requirements (per A.8.10, A.8.11)
- Data backup and recovery requirements (per A.8.13-14)
- Data minimization and purpose limitation (GDPR Art. 5 compliance)
- Data subject rights implementation (access, rectification, erasure per GDPR)
- Cross-border data transfer controls (if applicable)

**Source**: ISMS-POL-A.8.24 (Cryptography), ISMS-POL-A.8.10 (Deletion), GDPR/nDSG requirements

#### 2.4.3 Access Control and Authentication Requirements

For projects creating or modifying systems with user access:

- Authentication mechanism requirements (password, MFA, SSO per A.8.5)
- Authorization model (RBAC, ABAC, least privilege per A.5.15)
- Privileged access management requirements (for administrative functions per A.8.2)
- Account lifecycle requirements (provisioning, deprovisioning per A.5.16)
- Access logging and monitoring requirements (per A.8.16)

**Source**: ISMS-POL-A.5.15-16-18 (IAM), authentication standards (NIST SP 800-63B)

#### 2.4.4 Infrastructure and Network Security Requirements

For projects deploying infrastructure or modifying network architecture:

- Network segmentation requirements (separate environments, DMZ, internal per A.8.20-22)
- Firewall and access control list requirements
- Secure configuration requirements (per A.8.9)
- Patch management requirements (per A.8.8)
- Web filtering requirements (if internet-facing per A.8.23)
- DLP requirements (for sensitive data egress per A.8.12)
- Monitoring and logging requirements (per A.8.16)

**Source**: ISMS-POL-A.8.20-22 (Network Security), infrastructure security standards

#### 2.4.5 Third-Party and Integration Security Requirements

For projects involving external vendors or system integrations:

- Vendor security assessment requirements (per A.5.19-22)
- Contractual security obligations (SLA, liability, data protection)
- API security requirements (authentication, authorization, rate limiting)
- Data sharing and segregation requirements
- Third-party access controls and monitoring
- Service level agreements for security (incident response times, patching SLAs)

**Source**: ISMS-POL-A.5.19-22 (Supplier Management), integration security standards

#### 2.4.6 Compliance and Regulatory Requirements

For projects subject to regulatory obligations:

- Regulatory applicability assessment (per ISMS-POL-00 and A.5.31)
- Specific regulatory controls required (GDPR, PCI DSS, HIPAA, FINMA, etc.)
- Audit trail and evidence retention requirements
- Regulatory reporting or notification requirements
- Certification or attestation requirements (ISO 27001, SOC 2, etc.)
- Privacy requirements (consent, privacy notices, data subject rights)

**Source**: ISMS-POL-00 (Regulatory Framework), ISMS-POL-A.5.31 (Legal Requirements)

**Requirements Documentation**: All identified security requirements SHALL be documented in the Security Requirements Register with:
- Unique requirement ID
- Requirement description (clear, testable)
- Requirement source (policy, regulation, threat model, risk assessment)
- Priority (Must Have / Should Have / Nice to Have)
- Implementation status (Not Started / In Progress / Implemented / Verified)
- Verification method (testing approach, evidence required)
- Traceability (links to design, implementation, test results)

---

## 3. Roles and Responsibilities

### 3.1 Executive Management

**Accountability**: Overall organizational security, including project security integration.

**Responsibilities**:
- Approve this policy and ensure organizational resources for implementation
- Review high-risk project security status in management reviews
- Accept residual risks for critical projects that cannot fully meet security requirements
- Ensure project management methodology includes information security requirements

**Authority**: Final approval for risk acceptance decisions on critical projects.

### 3.2 Chief Information Security Officer (CISO)

**Accountability**: Information security program implementation, including project security oversight.

**Responsibilities**:
- Approve and maintain this policy
- Approve High Risk project classifications
- Review and approve security requirements for High Risk projects
- Accept residual security risks for High Risk projects (with Executive Management for critical risks)
- Provide security resources (Security Architects, Security Officers) for project support
- Monitor project security metrics and report to Executive Management
- Conduct or commission security reviews of critical projects
- Approve exceptions to security requirements

**Authority**: Halt or delay projects with unacceptable security risks; Mandate additional security controls for high-risk projects.

### 3.3 Information Security Officer / Security Team

**Accountability**: Operational security guidance and risk assessment support.

**Responsibilities**:
- Support project teams in security risk assessment and requirements identification
- Review and approve Medium Risk project classifications
- Review security requirements and provide technical guidance
- Conduct or commission security testing (vulnerability scans, penetration tests)
- Review security architecture and design for Medium/High Risk projects
- Document lessons learned and recommend policy/procedure improvements
- Maintain security requirements templates and checklists
- Provide security training to project teams

**Authority**: Escalate security concerns to CISO; Recommend project delays for unmitigated risks.

### 3.4 Project Manager

**Accountability**: Overall project success, including security requirements implementation.

**Responsibilities**:
- Classify project security risk level (with InfoSec Officer support)
- Ensure security activities are planned and budgeted at project initiation
- Execute security activities at each project phase per this policy
- Maintain project security risk register
- Escalate security risks and issues to appropriate authorities
- Ensure security testing is conducted and findings remediated
- Document security aspects in project closure and handover
- Incorporate security lessons learned into future projects

**Authority**: Allocate project resources to security activities; Request security support from InfoSec team.

**Note**: For High Risk projects, a dedicated **Project Security Coordinator** may be assigned to support the Project Manager with security-specific activities.

### 3.5 Business Owner / Product Owner

**Accountability**: Business requirements, including security needs of project deliverables.

**Responsibilities**:
- Define business security requirements (confidentiality, integrity, availability needs)
- Participate in security risk assessment (identify business impact)
- Approve security requirements as part of overall project scope
- Accept residual security risks for owned systems/services
- Ensure operational security procedures post-deployment
- Allocate operational budget for ongoing security (patching, monitoring, updates)

**Authority**: Approve project security requirements; Accept residual risks for owned assets (Medium Risk projects).

### 3.6 Technical Lead / Solution Architect

**Accountability**: Technical design and implementation, including security architecture.

**Responsibilities**:
- Design security controls into solution architecture
- Implement security requirements per specifications
- Support threat modeling and security architecture reviews
- Ensure secure configuration of systems and applications
- Conduct security testing (unit tests, integration tests)
- Document security configuration and operational procedures
- Address security findings from testing or reviews

**Authority**: Recommend technical security approaches; Escalate security implementation challenges.

### 3.7 Project Steering Committee / Governance Board

**Accountability**: Project oversight and strategic decision-making.

**Responsibilities**:
- Review security risks as part of phase gate approvals
- Approve project continuation despite identified security risks (with documented rationale)
- Escalate unacceptable security risks to Executive Management
- Ensure adequate project resources allocated to security activities

**Authority**: Approve or reject phase gate progression based on security status; Request additional security reviews or controls.

### 3.8 Third-Party Vendors / Contractors

**Accountability**: Security of vendor-delivered components and services per contract.

**Responsibilities**:
- Comply with [Organization]'s security requirements in contracts
- Participate in security assessments and provide required evidence
- Implement security controls per specifications
- Report security incidents or vulnerabilities to [Organization]
- Support security testing and remediation activities
- Provide security documentation for delivered solutions

**Authority**: As defined in contract or statement of work.

---

## 4. Governance, Review, and Documentation

### 4.1 Project Security Governance

#### 4.1.1 Phase Gate Reviews

[Organization] integrates security reviews into existing project governance and phase gate processes:

**Gate 0 (Project Approval)**:
- Security classification determined
- Initial security risks identified
- Security budget allocated

**Gate 1 (Planning Approval)**:
- Security requirements documented and approved
- Security resources identified and committed
- Security test plan approved

**Gate 2 (Execution Checkpoint)**:
- Security testing conducted
- Critical findings remediated
- Security architecture reviewed (High Risk projects)

**Gate 3 (Deployment Approval)**:
- All Critical/High findings remediated or accepted
- Security handover documentation complete
- Operational security procedures defined

**Gate 4 (Project Closure)**:
- Residual risks formally accepted
- Lessons learned documented
- Assets registered in ISMS inventory

**Security Review Authority**: 
- Low Risk: Project Manager self-assessment
- Medium Risk: Information Security Officer review required
- High Risk: CISO approval required

**Gate Approval**: Projects SHALL NOT proceed to next phase until security criteria for current phase are met or formally accepted by appropriate authority.

#### 4.1.2 Escalation Procedures

**Escalation Triggers**:
- Critical or High security vulnerabilities identified during testing
- Project scope changes materially increase security risk (reclassification needed)
- Security budget or resources insufficient to meet requirements
- Proposed workarounds or exceptions to security requirements
- Disagreement between Project Manager and InfoSec Officer on security approach
- External security incidents affecting similar technologies/architectures

**Escalation Path**:
1. **Project Manager → Information Security Officer** (technical security concerns)
2. **Information Security Officer → CISO** (risk acceptance needed, policy exceptions)
3. **CISO → Executive Management** (critical risks, significant resource needs, policy changes)

**Escalation Timeline**: Security concerns SHALL be escalated within 2 business days of identification for High Risk projects, 5 business days for Medium Risk projects.

#### 4.1.3 Exception Management

**Exception Request Process**:
1. Project Manager documents exception request (requirement to be waived, business justification, compensating controls)
2. Information Security Officer assesses risk impact and recommends approval/rejection
3. Appropriate authority approves/rejects:
   - Low Risk projects: Information Security Officer
   - Medium Risk projects: CISO
   - High Risk projects: CISO + Executive Management

**Exception Documentation**:
- Exception description and justification
- Risk assessment (likelihood, impact, residual risk)
- Compensating controls (if applicable)
- Time limit (temporary exceptions expire and require renewal)
- Approval signatures and date

**Exception Tracking**: All exceptions tracked in Security Exception Register and reviewed quarterly by CISO.

### 4.2 Documentation Requirements

#### 4.2.1 Mandatory Project Security Documentation

| Project Classification | Required Documentation |
|------------------------|------------------------|
| **High Risk** | • Project Security Plan<br>• Detailed Security Risk Register<br>• Security Requirements Register<br>• Threat Model<br>• Security Architecture Documentation<br>• Security Test Plan and Results<br>• Security Handover Package<br>• Lessons Learned Report |
| **Medium Risk** | • Security Risk Register (integrated in project risk register)<br>• Security Requirements Register<br>• Security Test Results<br>• Security Handover Documentation<br>• Lessons Learned (security section) |
| **Low Risk** | • Security Checklist (completed)<br>• Basic security test results<br>• Security handover notes |

**Documentation Storage**: All project security documentation SHALL be stored in [Organization]'s project repository with appropriate access controls and retained per [Organization]'s records retention policy.

#### 4.2.2 Security Requirements Register

The Security Requirements Register is the authoritative source for project security requirements. Minimum content:

- **Requirement Identification**: Unique ID, description, source (policy/regulation/threat/risk)
- **Categorization**: Requirement type (application/data/access/infrastructure/compliance)
- **Prioritization**: Must Have / Should Have / Nice to Have
- **Implementation Status**: Not Started / In Progress / Implemented / Verified
- **Verification**: Test method, test results, evidence location
- **Traceability**: Links to design documents, implementation artifacts, test cases

**Maintenance**: Requirements register is living document, updated throughout project lifecycle. Changes to requirements require impact assessment and appropriate approval.

#### 4.2.3 Security Risk Register

Project security risks SHALL be documented in the Project Risk Register with:

- **Risk Identification**: Unique ID, description, threat source, vulnerability
- **Risk Analysis**: Likelihood, impact, risk level (using [Organization]'s risk methodology)
- **Risk Treatment**: Mitigate / Accept / Transfer / Avoid + treatment plan
- **Risk Owner**: Individual accountable for risk management
- **Status**: Open / In Progress / Closed / Accepted
- **Monitoring**: Review frequency, current status, trend

**Integration**: Project security risks feed into [Organization]'s enterprise risk register for High Risk projects or when risks exceed project-level risk appetite.

#### 4.2.4 Security Handover Documentation

At project closure, security handover documentation SHALL include:

- **Security Architecture**: Design decisions, security controls implemented, configuration notes
- **Security Configuration**: Hardening applied, security settings, secure defaults
- **Security Procedures**: Operational security tasks, monitoring, patching, backup verification
- **Known Security Issues**: Accepted residual risks, workarounds, future enhancements
- **Security Contacts**: Vendor security contacts, escalation procedures, incident reporting
- **Security Testing Evidence**: Test results, penetration test reports, remediation evidence
- **Compliance Artifacts**: Evidence for regulatory requirements, audit trails

**Audience**: Operations team, system administrators, security monitoring team, future maintainers.

### 4.3 Review and Continuous Improvement

#### 4.3.1 Policy Review

This policy SHALL be reviewed:
- **Annually** (minimum) by CISO with input from PMO and Security team
- **Triggered by**: Major project failures with security root causes, regulatory changes affecting project security, significant organizational changes (M&A, new business lines)

**Review Criteria**:
- Policy effectiveness (are projects consistently meeting security requirements?)
- Usability (can project teams reasonably comply without excessive overhead?)
- Regulatory alignment (does policy address current compliance obligations?)
- Lessons learned integration (are common project security gaps addressed in policy?)

**Review Authority**: CISO recommends updates, Executive Management approves.

#### 4.3.2 Lessons Learned Process

[Organization] systematically captures and applies project security lessons learned:

**Post-Project Security Review** (mandatory for High/Medium Risk projects):
- Review conducted within 30 days of project closure
- Participants: Project Manager, InfoSec Officer, key project team members
- Topics: What worked well? What didn't? What would we do differently? What should be standardized?
- Output: Lessons Learned Report with actionable recommendations

**Lessons Learned Application**:
- **Process Improvements**: Update ISMS-IMP-A.5.8 procedures based on lessons learned
- **Template Updates**: Improve checklists, requirement templates, risk assessment guides
- **Training**: Incorporate lessons into project manager security training
- **Policy Updates**: Recommend policy changes for systemic issues
- **Best Practices**: Document successful approaches for reuse

**Sharing**: Lessons learned (sanitized for confidentiality) shared with project management community quarterly.

#### 4.3.3 Security Metrics and Reporting

[Organization] tracks the following project security metrics:

**Project Security Metrics**:
- Number/percentage of projects by security classification (High/Medium/Low)
- Percentage of projects with completed security assessments (by phase)
- Number of security findings by severity (Critical/High/Medium/Low) and remediation status
- Average time to remediate security findings
- Percentage of projects with accepted residual risks
- Security exceptions granted (number, type, duration)

**Portfolio Security Metrics**:
- Trend: Are projects getting better at security over time?
- Common gaps: What security requirements are frequently missed?
- Methodology effectiveness: Which project methodologies have better security outcomes?

**Reporting Frequency**:
- **Monthly**: CISO dashboard (High Risk project status, critical open findings)
- **Quarterly**: Executive Management report (portfolio security trends, lessons learned)
- **Annually**: Board reporting (project security program effectiveness, major improvements)

---

## 5. Integration with Other Controls

This policy integrates with [Organization]'s Information Security Management System as follows:

### 5.1 Integration with ISMS Core

**Risk Assessment** (ISO 27001 Clause 6.1):
- Project security risks are identified and assessed per this policy
- Project risks feed into enterprise risk register when exceeding project-level risk appetite
- Risk treatment decisions determine which security controls are implemented in projects
- Residual project risks tracked in [Organization]'s risk register

**Statement of Applicability** (ISO 27001 Clause 6.1.3):
- Control A.5.8 applicability justified in [Organization]'s SoA
- Implementation status tracked through project security assessments
- Control effectiveness measured through project security metrics and audit findings

**This policy supports the following SoA entry**:

| Control | Status | Justification | Implementation |
|---------|--------|---------------|----------------|
| **A.5.8 - Information Security in Project Management** | ☑ Applicable | [Organization] undertakes projects that create/modify information systems and processes; systematic security integration prevents security being treated as afterthought | Section 2 (Requirements), ISMS-IMP-A.5.8 (Assessment Suite) |

### 5.2 Related Control Integration Points

**Strong Integration** (referenced extensively in project security activities):

- **A.5.31** (Legal, Statutory, Regulatory and Contractual Requirements): Project security requirements include applicable regulatory obligations per ISMS-POL-00
- **A.8.25-28** (Secure Development Lifecycle): Software development projects implement secure SDLC per secure development policies
- **A.5.19-22** (Information Security in Supplier Relationships): Projects involving third-party vendors follow supplier security assessment per supplier management policies
- **A.8.32** (Change Management): Project deliverables enter production through formal change control process
- **A.5.9** (Inventory of Information and Other Associated Assets): Project deliverables registered in asset inventory during project closure

**Moderate Integration** (relevant for specific project types):

- **A.8.8** (Management of Technical Vulnerabilities): Security testing in projects includes vulnerability assessment
- **A.8.9** (Configuration Management): Infrastructure projects implement secure configuration per configuration management policy
- **A.8.24** (Use of Cryptography): Projects handling Confidential/Restricted data implement encryption per cryptography policy
- **A.5.15-18** (Identity and Access Management): Projects creating user-facing systems implement access controls per IAM policy
- **A.8.2** (Privileged Access Rights): Projects implement privileged access management for administrative functions

**Contextual Integration** (applies when specific project scenarios occur):

- **A.5.24-27** (Incident Management): Security incidents during projects managed per incident response procedures
- **A.8.13-14** (Backup, Redundancy): Projects affecting critical systems ensure backup/recovery capability
- **A.8.23** (Web Filtering): Projects deploying internet access implement web filtering requirements
- **A.8.12** (Data Leakage Prevention): Projects handling sensitive data implement DLP controls
- **A.8.11** (Data Masking): Projects with test environments implement data masking for production data

### 5.3 Project Management Methodology Integration

This policy integrates with [Organization]'s project management methodology regardless of framework:

**Waterfall/Traditional Projects**:
- Security activities aligned with sequential phases (Initiation → Planning → Execution → Closure)
- Phase gate reviews include security checkpoints
- Security requirements documented in requirements specification
- Security testing in dedicated test phase

**Agile/Iterative Projects**:
- Security requirements in product backlog (user stories with security acceptance criteria)
- Security activities in Definition of Done (code review, testing, documentation)
- Security risks reviewed in sprint planning and retrospectives
- Incremental security testing (per sprint or release)
- Security architecture reviewed at epic or major release level

**Hybrid/Custom Projects**:
- Security principles applied (early integration, risk-based, traceable requirements)
- Security activities adapted to project governance structure
- Flexibility in documentation (proportional to project risk and complexity)

**Key Principle**: Security integration is methodology-agnostic. This policy defines WHAT security activities are required; project teams determine HOW to integrate them into their chosen methodology.

---

## Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:
- ✅ This policy document (ISMS-POL-A.5.8 v1.0)
- ✅ Approval signatures from CISO, Executive Management, relevant stakeholders
- ✅ Project classification framework defined (Section 2.2)
- ✅ Security activities by phase documented (Section 2.3)
- ✅ Security requirements categories specified (Section 2.4)
- ✅ Roles and responsibilities assigned (Section 3)
- ✅ Governance and escalation procedures defined (Section 4)

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:
- Project security assessments completed per ISMS-IMP-A.5.8 (sample of High/Medium/Low projects)
- Project classification determinations with approval signatures
- Security risk registers for active projects (at appropriate phase gates)
- Security requirements registers for Medium/High Risk projects
- Security test results and remediation evidence
- Phase gate review records showing security approvals
- Residual risk acceptance documentation
- Security handover documentation for completed projects
- Lessons learned reports with security sections
- Project security metrics dashboard (quarterly/annual reports)
- Security exception register (if exceptions granted)

**Clarification on Compliance Evidence**:
This policy establishes project security requirements (HOW security is integrated into projects). It does NOT establish:
- **Project-specific security controls** (determined by individual project risk assessments and requirements)
- **General security controls** (addressed in Annex A control-specific policies like A.8.24, A.5.15-18, etc.)
- **Project management methodology** (organizational project governance, separate from ISMS)

The boundary is: POL-A.5.8 defines security integration requirements → Projects implement security per their risk classification → Project assessments verify integration → Control-specific policies define technical requirements.

---

## Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Chief Operating Officer (COO) / PMO Director** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for information security integration into project management. Implementation procedures, assessment templates, and detailed guidance are documented in ISMS-IMP-A.5.8.*