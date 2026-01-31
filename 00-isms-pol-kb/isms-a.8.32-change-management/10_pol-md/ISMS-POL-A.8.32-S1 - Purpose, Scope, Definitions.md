# ISMS-POL-A.8.32-S1
## Change Management - Purpose, Scope, Definitions

**Document ID**: ISMS-POL-A.8.32-S1  
**Title**: Change Management - Purpose, Scope, Definitions  
**Version**: 1.0  
**Date**: [Date] 
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]| Information Security Manager | Initial foundational document |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Change Manager / IT Operations Manager
- Compliance Review: Legal/Compliance Officer

**Distribution**: Change Manager, CAB members, IT operations, security team, policy administrators  
**Related Documents**: ISMS-POL-A.8.32 (Master), ISO/IEC 27001:2022 A.8.32

---

## 1.1 Purpose

### 1.1.1 Policy Objective

This document establishes the purpose, scope, and key definitions for the organization's Change Management policy framework, implementing ISO/IEC 27001:2022 Annex A Control 8.32 (Change Management).

The policy framework aims to:

- **Protect** information security during changes to information processing facilities and systems
- **Prevent** system failures, security vulnerabilities, data integrity issues, and availability disruptions
- **Ensure** proper planning, assessment, authorization, testing, and documentation of all changes
- **Enable** business agility through controlled and repeatable change processes
- **Comply** with legal, regulatory, and contractual obligations regarding change control
- **Support** continuous improvement through lessons learned and failure analysis

### 1.1.2 Control Alignment

This policy implements ISO/IEC 27001:2022 Annex A.8.32:

> **A.8.32 Change Management**  
> *Changes to information processing facilities and information systems should be subject to change management procedures.*

**ISO/IEC 27002:2022 Guidance:**
> *Poor control over changes to information processing facilities and information systems is a common cause of system or security failures.*

The control recognizes that uncontrolled changes expose organizations to risks including:
- System outages and availability disruptions
- Security vulnerabilities introduced through inadequate testing
- Data integrity violations through configuration errors
- Compliance failures through undocumented changes
- Operational disruptions through inadequate communication
- Inability to recover through lack of rollback procedures

### 1.1.3 Risk Management Context

Change management serves as a **preventive and detective control** within the organization's layered security architecture. While changes are necessary for business operations and continuous improvement, they also represent significant risk events that require careful management.

**Key Risk Scenarios Addressed:**
- **Unauthorized changes:** Direct-to-production modifications bypassing approval
- **Inadequate testing:** Changes deployed without proper validation
- **Failed changes:** Implementation errors causing outages or security issues
- **Undocumented changes:** Configuration drift and inability to troubleshoot
- **Emergency changes:** Rushed implementations under pressure without proper controls
- **Environment confusion:** Production changes tested in development (or vice versa)

**Risk Mitigation Strategy:**
The organization recognizes that change management must balance **security and control** with **business agility and innovation**. Overly bureaucratic change processes can impede legitimate business activities and encourage shadow IT, while insufficient change controls expose the organization to unacceptable operational and security risks.

This framework implements **risk-based change control** where the level of rigor is proportional to the risk and impact of the change.

---

## 1.2 Scope

### 1.2.1 In Scope

This policy framework applies to:

**Information Processing Facilities:**
- Physical servers (on-premises data centers, colocation facilities)
- Virtual infrastructure (hypervisors, virtual machines, containers)
- Network infrastructure (routers, switches, firewalls, load balancers)
- Storage systems (SAN, NAS, object storage, backup systems)
- Cloud infrastructure (IaaS, PaaS resources in public/private/hybrid clouds)
- Security infrastructure (SIEM, IDS/IPS, endpoint protection, authentication systems)
- Monitoring and management systems (logging, metrics, orchestration)
- Telecommunications systems (voice, video, unified communications)
- Physical facilities affecting IT systems (power, cooling, cabling)

**Information Systems:**
- Business applications (ERP, CRM, financial systems, HR systems)
- Custom-developed software (internally developed applications)
- Databases and data warehouses (RDBMS, NoSQL, data lakes)
- Middleware and integration platforms (message queues, ESB, API gateways)
- Operating systems (Windows, Linux, Unix, mainframe)
- Security systems (IAM, PAM, encryption, DLP)
- Development tools and CI/CD pipelines (version control, build systems, deployment automation)
- Office productivity systems (email, collaboration, document management)
- Website and web applications (public-facing and internal)

**Change Types:**
- **Hardware changes:** Server installations, network equipment upgrades, storage expansions
- **Software changes:** Application updates, OS patches, security updates, new software installations
- **Configuration changes:** Parameter modifications, rule updates, policy changes
- **Infrastructure changes:** Network topology, virtualization, cloud resources
- **Data changes:** Database schema modifications, data migrations, master data updates
- **Process changes:** Workflow modifications, integration changes, automation updates
- **Documentation changes:** Operating procedures, configuration documentation, runbooks

**All Environments:**
- Development (Dev)
- Testing / Quality Assurance (Test/QA)
- Staging / Pre-Production (where applicable)
- Production (Prod)
- Disaster Recovery (DR)
- Transitions between environments (promotion/deployment)

### 1.2.2 Out of Scope

The following are explicitly **out of scope** for this change management framework:

**Business Process Changes:**
- Organizational restructuring (unless affecting IT systems)
- Business policy changes (unless affecting IT system configurations)
- Human resource changes (hiring, terminations, role changes)
  - *Exception: Changes to system access/privileges follow this framework*

**Content Changes:**
- Website content updates (text, images, marketing materials)
- Document content modifications in content management systems
- Email/communication content
  - *Exception: Changes to website functionality or CMS configuration follow this framework*

**Routine Operations:**
- Daily backups (scheduled, automated)
- Log rotation and archival (automated processes)
- Monitoring alert acknowledgments
- Routine maintenance tasks (pre-approved as standard changes)

**User Activities:**
- User-initiated self-service actions (password resets via approved self-service portal)
- User preference configurations within applications
- Personal file storage and sharing (within approved limits)

**External Service Provider Changes:**
- Changes managed entirely by SaaS providers (behind the scenes)
- Cloud provider infrastructure changes (outside customer control)
  - *Exception: Changes to customer-controlled configurations follow this framework*

**Exclusion Rationale:** These exclusions represent activities that either:
1. Do not materially affect information security
2. Are managed through separate governance processes
3. Are fully automated with adequate controls
4. Are outside the organization's control

Any changes falling into gray areas SHALL be escalated to the Change Manager for classification.

### 1.2.3 Applicability by Change Size and Risk

**Change Categorization:**
All in-scope changes are classified into one of three categories based on risk assessment:

1. **Standard Changes:** Low risk, pre-approved, may be self-service
2. **Normal Changes:** Medium to high risk, require CAB review and approval
3. **Emergency Changes:** Urgent, fast-track approval, mandatory post-review

*See ISMS-POL-A.8.32-S2.2 (Change Classification Requirements) for detailed criteria.*

**Risk-Based Scope Application:**
- **Low-risk standard changes:** Streamlined process, minimal documentation
- **High-risk normal changes:** Full change management rigor, comprehensive testing
- **Emergency changes:** Accelerated approval, enhanced post-implementation review

---

## 1.3 Definitions

### 1.3.1 Core Change Management Terms

**Change:**
A modification to any information processing facility or information system that could impact information security, availability, integrity, or confidentiality. Includes additions, modifications, deletions, and temporary changes.

**Change Request (CR):**
A formal proposal to implement a change, documented in the organization's ITSM system with sufficient detail for impact assessment, risk evaluation, and approval decision.

**Change Management:**
The process of controlling changes to information processing facilities and information systems through formal procedures covering planning, assessment, authorization, testing, implementation, and documentation.

**Change Advisory Board (CAB):**
A group of stakeholders responsible for reviewing and approving normal changes based on business justification, technical assessment, risk evaluation, and resource availability.

**Emergency CAB (E-CAB):**
A subset of CAB members available for urgent decisions on emergency changes, typically including Change Manager, senior technical authority, and security representative.

**Change Manager:**
Role responsible for overall change management process governance, CAB coordination, change prioritization, and ensuring change management procedures are followed.

**Change Owner:**
Individual or team proposing the change, responsible for providing change details, business justification, risk assessment, and implementing approved changes.

**Change Implementer:**
Technical personnel responsible for executing the approved change according to the implementation plan.

**Change Approver:**
Authority level with decision-making power to approve changes based on risk and impact (may be Change Manager, CAB, E-CAB, or designated technical authority).

### 1.3.2 Change Types

**Standard Change:**
A pre-approved, low-risk change following a documented procedure with well-understood impact and rollback. Standard changes do not require individual CAB approval but must still be logged and tracked.

*Examples:*
- Password resets (via approved self-service mechanism)
- Standard workstation software installations (from approved catalog)
- Routine monthly security patches (following established schedule)
- SSL/TLS certificate renewals (automated or following documented procedure)

**Normal Change:**
A change requiring formal assessment, CAB review, approval, and comprehensive testing before implementation. Represents the majority of changes to production systems.

*Examples:*
- Application version upgrades
- Infrastructure configuration changes
- New system deployments
- Database schema modifications
- Network topology changes

**Emergency Change:**
An urgent change required to resolve a critical incident, security vulnerability, or business disruption. Follows accelerated approval process with mandatory post-implementation review.

*Examples:*
- Critical security patches (zero-day vulnerability, active exploitation)
- Incident remediation (restore service after outage)
- Emergency fixes (resolve critical business-impacting issue)
- Security incident response (contain/remediate active breach)

*See ISMS-POL-A.8.32-S2.2 and ISMS-POL-A.8.32-S2.4 for detailed change classification criteria and emergency change procedures.*

### 1.3.3 Change States

**Requested:**
Change request submitted, awaiting initial review and scheduling for assessment.

**Assessing:**
Change under evaluation for impact, risk, resources, and dependencies. Technical assessment in progress.

**Scheduled:**
Change approved by CAB, scheduled for implementation with confirmed date/time and resources.

**Implementing:**
Change in progress, implementation plan being executed.

**Review:**
Change completed, under post-implementation review to verify success and document lessons learned.

**Closed:**
Change successfully implemented and reviewed, all documentation complete, ticket closed.

**Rejected:**
Change request denied by CAB or appropriate authority with documented justification.

**Cancelled:**
Change request withdrawn by requestor or cancelled due to changing business requirements.

**Failed:**
Change implementation unsuccessful, rollback executed, requiring problem analysis.

### 1.3.4 Environment Definitions

**Development Environment (Dev):**
Environment for software development, coding, initial unit testing, and experimentation. Not connected to production systems or data.

**Testing Environment (Test / QA):**
Environment for integration testing, quality assurance, user acceptance testing (UAT), and security testing. Simulates production but uses synthetic or anonymized data (see ISO 27001:2022 Control 8.33).

**Staging Environment (Stage / Pre-Prod):**
Optional environment that mirrors production configuration as closely as possible for final validation before production deployment. May use production-like data (anonymized).

**Production Environment (Prod):**
Live operational environment serving business functions and customers. Contains real data and requires maximum protection and change control.

**Disaster Recovery Environment (DR):**
Backup environment for business continuity purposes. Changes to DR environment follow same controls as production.

### 1.3.5 Change Risk Terms

**Impact:**
The scope and severity of consequences if the change fails or causes issues. Measured in terms of affected users, systems, business processes, and potential financial/reputational damage.

**Impact Levels:**
- **Low:** Single user/system, no business impact, easily reversible
- **Medium:** Multiple users/systems, minor business impact, rollback possible
- **High:** Department/major system, significant business impact, complex rollback
- **Critical:** Organization-wide, severe business/security impact, difficult/impossible rollback

**Likelihood:**
The probability that the change will fail, cause issues, or have unintended consequences. Based on change complexity, environment stability, testing adequacy, and implementer experience.

**Likelihood Levels:**
- **Low:** Simple change, well-tested, experienced implementer, stable environment
- **Medium:** Moderate complexity, some unknowns, adequate testing
- **High:** Complex change, many dependencies, limited testing, new technology

**Risk:**
Combination of impact and likelihood, calculated using risk matrix (Impact × Likelihood). Determines required approval authority and rigor of change management process.

*See ISMS-POL-A.8.32-S5.C (Risk Assessment Matrix) for detailed risk classification methodology.*

**Rollback:**
Process of reverting a change to restore the previous state if the change fails or causes issues. Rollback procedures should be defined before change implementation.

**Backout:**
Similar to rollback but may involve alternative recovery steps rather than pure reversion. Used when simple rollback is not feasible.

### 1.3.6 Testing Terms

**Unit Testing:**
Developer testing of individual components in isolation, performed in development environment.

**Integration Testing:**
Testing of interactions between multiple components, performed in test environment.

**User Acceptance Testing (UAT):**
Business user validation that change meets requirements and works as expected, performed in test/staging environment.

**Regression Testing:**
Testing to ensure change does not adversely impact existing functionality.

**Security Testing:**
Validation that change does not introduce security vulnerabilities. Aligns with ISO 27001:2022 Control 8.29 (Security Testing in Development).

**Production Validation Testing:**
Post-implementation testing in production to verify change success (often called "smoke testing" or "sanity testing").

### 1.3.7 Additional Terms

**Change Window:**
Scheduled time period during which changes to production systems are permitted. Often aligned with low-usage periods to minimize business impact.

**Freeze Period / Blackout Window:**
Time period during which changes to production systems are prohibited (except emergency changes) due to high business criticality (e.g., financial close, peak business periods).

**Change Collision:**
Situation where multiple changes to the same system or dependent systems are scheduled simultaneously, creating conflict risk.

**Post-Implementation Review (PIR):**
Formal review after change implementation to verify success, document lessons learned, and identify process improvements.

**Configuration Item (CI):**
A component of IT infrastructure or systems tracked in configuration management database (CMDB). Changes typically target specific CIs.

**Configuration Management Database (CMDB):**
Repository of configuration items and their relationships, dependencies, and change history. Supports impact assessment for changes.

---

## 1.4 Regulatory and Standards Context

### 1.4.1 ISO/IEC 27001:2022 Requirements

**Control A.8.32 mandates change management procedures addressing:**

a) **Planning and impact assessment:** Analysis of potential impacts, dependencies, risks  
b) **Authorization:** Formal approval based on risk and business justification  
c) **Communication:** Notification to affected stakeholders with appropriate timing  
d) **Testing and acceptance:** Pre-deployment validation with defined success criteria  
e) **Implementation:** Controlled deployment with defined procedures  
f) **Emergency and contingency:** Rollback procedures and emergency change process  
g) **Record keeping:** Complete change history and audit trail  
h) **Documentation updates:** Operational procedures updated to reflect changes (Control 5.37)  
i) **Continuity plan updates:** ICT continuity plans updated for infrastructure changes (Control 5.30)

*See ISMS-POL-A.8.32-S2 (Requirements Overview) for detailed requirement specifications.*

### 1.4.2 Swiss Federal Data Protection Act (FADP)

**Relevance to Change Management:**

Changes to information processing facilities and systems that handle personal data must maintain data protection controls throughout the change lifecycle.

**Key Considerations:**
- Changes SHALL NOT introduce vulnerabilities allowing unauthorized personal data access
- Data protection impact assessments (DPIA) required for changes affecting personal data processing
- Change management records may be required for data protection compliance audits
- Changes affecting data processing must maintain technical and organizational measures per Art. 8 FADP

### 1.4.3 EU GDPR (Where Applicable)

**Relevance to Change Management:**

Organizations processing EU personal data must ensure changes to processing systems maintain GDPR Article 32 security requirements (security of processing).

**Key Considerations:**
- Changes must maintain appropriate technical measures (encryption, pseudonymization, etc.)
- Changes affecting data processing may require DPIA (Article 35)
- Change management forms part of demonstrable accountability (Article 5(2))
- Data protection by design and default (Article 25) applies to system changes

### 1.4.4 Industry-Specific Regulations

**Financial Services:**
- FINMA regulations may require specific change management controls
- SOX compliance requirements for financial systems (if applicable)
- Payment card industry (PCI DSS) change control requirements (if applicable)

**Healthcare:**
- Swiss medical device regulations for software affecting medical systems
- HIPAA requirements (if handling US health data)

**Critical Infrastructure:**
- Additional change control requirements may apply to critical infrastructure operators

*Organizations must document specific regulatory requirements in change management procedures based on their industry and operational context. See ISMS-POL-00 (Regulatory Applicability Framework) for comprehensive regulatory categorization.*

### 1.4.5 ITIL 4 Alignment (Informational)

This framework aligns with ITIL 4 Change Enablement practice where applicable:

**ITIL 4 Concepts Referenced:**
- Change models (standard, normal, emergency)
- Change authority levels
- Change Advisory Board (CAB)
- Post-implementation review (PIR)

**Important Clarification:**
ITIL 4 is used as **informational reference and best practice alignment** only. This organization is implementing ISO/IEC 27001:2022 compliance, not ITIL 4 certification. Where ITIL terminology aids clarity, it is referenced, but ITIL is not mandatory for this framework.

---

## 1.5 Integration with Other Controls

### 1.5.1 Direct Dependencies

**This change management framework directly integrates with:**

**Control 5.30 (ICT Continuity Planning):**
- Major infrastructure changes require updates to continuity plans
- Change management ensures continuity plans remain current
- DR environment changes follow same controls as production

**Control 5.37 (Documented Operating Procedures):**
- Changes require operational documentation updates
- Change closure criteria include documentation completeness
- Runbooks and procedures updated to reflect implemented changes

**Control 8.29 (Security Testing in Development):**
- Security testing required before production deployment
- Security test results documented as part of change approval
- Security vulnerabilities must be remediated before deployment

**Control 8.31 (Separation of Development, Test, Production):**
- Environment separation enforced through change promotion process
- Unauthorized direct production changes prohibited
- Clear boundaries between Dev, Test, Prod environments

**Control 8.33 (Test Information):**
- Production data in test environments requires special handling
- Data masking/anonymization requirements for test environments
- Change management procedures protect production data confidentiality

**Control 8.19 (Installation of Software on Operational Systems):**
- Software installation changes follow formal change management
- Security validation before software deployment
- Licensing and compliance verification

### 1.5.2 Supporting Controls

Change management supports effectiveness of:

- **Access Control (Chapter 5):** Changes to access rights follow change management
- **Cryptography (8.24):** Changes to encryption implementations controlled
- **Secure Configuration (8.9):** Configuration changes formally managed
- **Logging (8.15):** Changes to logging infrastructure tracked
- **Monitoring (8.16):** Changes to monitoring systems controlled
- **Vulnerability Management (8.8):** Patching follows change management procedures

---

## 1.6 Document Maintenance

### 1.6.1 Review Triggers

This document SHALL be reviewed when:

**Scheduled:**
- Annual review (aligned with master policy review cycle)
- Internal audit findings
- External audit recommendations

**Triggered:**
- ISO/IEC 27001 standard updates affecting Control 8.32
- Regulatory changes affecting change management requirements
- Organizational changes (mergers, acquisitions, major restructuring)
- Technology changes (new change management tools, DevOps transformation)
- Major change management incidents requiring process updates

### 1.6.2 Change Authority

**Changes to this document require:**
- Primary approval: CISO
- Technical review: Change Manager
- Compliance review: Legal/Compliance Officer (for regulatory changes)
- Stakeholder consultation: IT Operations, CAB, Security Team

**Version Control:**
- Major version (X.0): Scope changes, new requirements, regulatory updates
- Minor version (X.Y): Clarifications, examples, non-material updates

---

**END OF SECTION 1**

*"I learned very early the difference between knowing the name of something and knowing something."  
— Richard Feynman*

*Knowing the definition of "change management" doesn't mean you have change management. Evidence and measurement are what matter.* 🎯