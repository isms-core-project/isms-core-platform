# ISMS-POL-A.8.9-S3
## Configuration Management - Roles and Responsibilities

**Document ID**: ISMS-POL-A.8.9-S3  
**Title**: Roles and Responsibilities  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Configuration Manager / CISO | Initial roles and responsibilities definition |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Date + 1 year]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Executive Review: Chief Information Officer (CIO) / Chief Technology Officer (CTO)
- HR Review: Human Resources Manager (for role definitions)

**Distribution**: All technical staff, management, HR  
**Related Documents**: ISMS-POL-A.8.9 (Master Policy), ISMS-POL-A.8.9-S2 (Requirements), ISMS-POL-A.8.9-S4 (Governance)

---

## 3.1 Purpose

This document defines the **roles, responsibilities, and accountability structure** for configuration management within [Organization]. Clear role definitions ensure:
- **Accountability** - Everyone knows who is responsible for what
- **Authority** - Decision-making authority is properly delegated
- **Collaboration** - Interfaces between roles are well-defined
- **Compliance** - Audit requirements for segregation of duties are met
- **Efficiency** - Work doesn't fall through gaps or duplicate unnecessarily

**The Anti-Pattern**: Organizations with a 20-page RACI matrix where every task has 15 people "consulted" and nobody is actually "accountable." When everyone is responsible, nobody is responsible.

**The Feynman Standard**: *"The test of good role definition is simple: When something goes wrong, can you answer 'Who is accountable?' in under 5 seconds? If not, your RACI matrix is decoration."*

---

## 3.2 Role Definition Principles

**MUST Requirements**:
- All roles involved in configuration management MUST have documented responsibilities
- Each critical activity MUST have a clearly identified accountable party
- Role definitions MUST consider:
  - **Separation of duties** - No single person controls all aspects of critical processes
  - **Span of control** - Roles have manageable scope
  - **Escalation paths** - Clear hierarchy for decision-making
  - **Succession planning** - Backup or deputy assignments for critical roles

**SHOULD Requirements**:
- Role definitions SHOULD use the RACI framework:
  - **R**esponsible - Does the work
  - **A**ccountable - Ultimately answerable for the outcome (only one A per activity)
  - **C**onsulted - Provides input before action
  - **I**nformed - Notified after action
- [Organization] SHOULD document role interfaces and handoff points
- Role definitions SHOULD be reviewed annually and updated as organizational structure evolves

---

## 3.3 Executive Ownership

### 3.3.1 Chief Information Security Officer (CISO)

**Accountabilities**:
- Overall accountability for configuration management program effectiveness
- Approval authority for configuration management policies and standards
- Approval authority for high-risk configuration deviations and exceptions
- Escalation point for unresolved configuration security incidents
- Executive reporting on configuration security posture

**Responsibilities**:
- Define security requirements for configuration management
- Approve security hardening standards
- Review and approve critical change requests (as CAB member or delegate)
- Ensure adequate resources for configuration security activities
- Report configuration security metrics to executive leadership and board

**Authority**:
- Approve or reject high-risk configuration changes
- Mandate security hardening requirements
- Impose compensating controls for configuration deviations
- Escalate configuration security issues to CEO/Board

**Typical Delegation**:
- Day-to-day operations delegated to Configuration Manager and Security Operations Manager
- Technical decisions delegated to Security Architect and subject matter experts

---

### 3.3.2 Chief Information Officer (CIO) / Chief Technology Officer (CTO)

**Accountabilities**:
- Overall accountability for IT operations including configuration management execution
- Approval authority for configuration management budget and resources
- Approval authority for technology selection (CMDB, monitoring tools, change management systems)
- Business alignment of configuration management practices

**Responsibilities**:
- Ensure configuration management integration with IT service management (ITSM)
- Approve configuration baselines for major platforms
- Chair or delegate Change Advisory Board (CAB) leadership
- Resource allocation for configuration management team
- Balance security requirements with operational needs

**Authority**:
- Approve configuration management tooling investments
- Approve organizational structure for configuration management
- Approve IT operational policies including change management
- Escalate conflicts between security and operations to executive level

**Typical Delegation**:
- Day-to-day operations delegated to IT Operations Manager and Configuration Manager
- Technical architecture delegated to Chief Architect or Infrastructure Manager

---

## 3.4 Operational Leadership

### 3.4.1 Configuration Manager

**Accountabilities**:
- Day-to-day accountability for configuration management program execution
- Maintaining accuracy of configuration baselines and CMDB
- Configuration drift management and remediation tracking
- Reporting on configuration management metrics
- Policy compliance measurement

**Responsibilities**:
- **Baseline Management**:
  - Coordinate baseline definition for all asset types
  - Maintain baseline documentation repository
  - Schedule and track baseline reviews
  - Approve minor baseline updates (escalate major changes to CAB)
- **Change Control**:
  - Chair or co-chair Change Advisory Board (CAB)
  - Review and triage change requests
  - Coordinate change scheduling and conflict resolution
  - Track change success metrics and remediation
- **Monitoring and Compliance**:
  - Oversee configuration monitoring activities
  - Review drift detection reports
  - Coordinate remediation activities
  - Generate compliance reports for audits
- **CMDB Management**:
  - Ensure CMDB accuracy and completeness
  - Define CMDB structure and relationships
  - Coordinate CMDB updates with asset discovery and change management
- **Stakeholder Coordination**:
  - Interface with system administrators, DevOps, security team, application owners
  - Facilitate baseline approval workshops
  - Communicate policy updates and requirements

**Authority**:
- Approve standard changes
- Approve minor configuration baseline updates
- Require remediation of configuration drift within policy SLAs
- Escalate unresolved issues to CISO/CTO

**Typical Team Size**: 1-5 FTEs depending on organization size and complexity

---

### 3.4.2 Security Operations Center (SOC) Manager

**Accountabilities**:
- Accountability for configuration security monitoring and incident response
- Integration of configuration monitoring with security event monitoring (SIEM)
- Security incident escalation related to configuration drift

**Responsibilities**:
- Deploy and maintain configuration monitoring tools for security-relevant parameters
- Define alerting rules for security-critical configuration drift
- Triage configuration drift alerts for security incidents
- Coordinate response to configuration-related security events
- Provide 24/7 monitoring for critical configuration changes (if SOC is 24/7)
- Generate security-focused configuration reports

**Authority**:
- Declare security incidents based on configuration drift
- Require immediate remediation of security-critical drift
- Escalate incidents to CISO and incident response team

---

### 3.4.3 IT Operations Manager

**Accountabilities**:
- Accountability for operational execution of configuration changes
- Ensuring system administrators follow configuration management policies
- Operational stability and availability during configuration changes

**Responsibilities**:
- Assign change implementation to system administrators
- Approve maintenance windows for configuration changes
- Coordinate with Configuration Manager on change scheduling
- Monitor change implementation progress
- Escalate failed changes and operational issues
- Ensure operational teams are trained on configuration policies

**Authority**:
- Approve or defer change implementation timing based on operational capacity
- Require rollback of failed changes impacting service availability
- Assign resources to configuration remediation activities

---

## 3.5 Governance and Oversight

### 3.5.1 Change Advisory Board (CAB)

**Composition** (typical):
- **Chair**: Configuration Manager or IT Operations Manager
- **Members**:
  - Security Representative (CISO or delegate)
  - Infrastructure Representative (System Administrators Lead)
  - Application Representative (Application Development Manager)
  - Business Representative (Business Analyst or Service Owner)
  - Additional SMEs as needed (Database Administrator, Network Administrator, Cloud Architect)

**Accountabilities**:
- Collective accountability for approving normal configuration changes
- Risk assessment and impact analysis for proposed changes
- Change conflict identification and resolution

**Responsibilities**:
- Review normal change requests submitted for approval
- Evaluate business justification, technical risk, and implementation plan
- Approve, reject, or defer change requests
- Recommend mitigation measures for high-risk changes
- Review emergency change post-implementation reports
- Review change management metrics and trends
- Recommend process improvements

**Authority**:
- Approve or reject normal change requests
- Require additional information or risk assessment before decision
- Impose conditions on change approval (e.g., additional testing, rollback plan enhancement)
- Escalate high-risk changes to executive leadership (CISO/CTO)

**Meeting Cadence**: Weekly or bi-weekly (typical for most organizations)

**Decision-Making**: Consensus-based or chair has tiebreaker authority

---

### 3.5.2 Internal Audit

**Responsibilities**:
- Conduct periodic audits of configuration management processes
- Verify compliance with policies and standards
- Test effectiveness of controls (baseline accuracy, change authorization, monitoring)
- Review exception management
- Report audit findings to management and audit committee
- Follow up on remediation of audit findings

**Authority**:
- Access to all configuration management records and systems
- Interview personnel involved in configuration management
- Report non-compliance to executive management and audit committee
- Recommend corrective actions

**Independence**: Internal Audit must be independent of IT operations and security operations

---

## 3.6 Technical Execution Roles

### 3.6.1 System Administrators

**Responsibilities**:
- **Baseline Implementation**:
  - Build systems according to approved configuration baselines
  - Deploy golden images where available
  - Validate configuration compliance after deployment
- **Change Implementation**:
  - Execute approved configuration changes according to change plans
  - Document change implementation steps and outcomes
  - Validate change success and perform rollback if needed
  - Update configuration documentation after changes
- **Monitoring and Remediation**:
  - Review configuration drift alerts for systems under their management
  - Investigate root cause of drift
  - Remediate unauthorized drift within policy SLAs
  - Request baseline updates for authorized drift (approved changes)
- **Documentation**:
  - Maintain system documentation including as-built configurations
  - Update CMDB with configuration changes
  - Provide evidence for audit and compliance

**Authority**:
- Implement approved changes within defined scope
- Execute standard changes without additional approval
- Request emergency changes when justified
- Propose baseline updates based on operational experience

**Skills Required**: Platform-specific technical expertise, change implementation experience, security awareness

---

### 3.6.2 DevOps Engineers / Platform Engineers

**Responsibilities**:
- **Infrastructure as Code (IaC)**:
  - Develop and maintain IaC templates (Terraform, CloudFormation, ARM templates)
  - Integrate configuration security scanning into CI/CD pipelines
  - Version control of IaC configurations
  - Test IaC deployments in non-production environments
- **Automation**:
  - Automate configuration deployments and updates
  - Develop automated compliance checking scripts
  - Implement automated remediation for specific drift types (where safe)
- **Baseline Development**:
  - Collaborate with Configuration Manager to define baselines for cloud and containerized environments
  - Create golden images and container base images
- **Change Management**:
  - Submit change requests for infrastructure modifications
  - Coordinate deployments with IT Operations

**Authority**:
- Develop IaC templates according to baselines
- Deploy to non-production environments (subject to change control for production)
- Recommend automation opportunities

**Skills Required**: Scripting/programming, cloud platforms, container orchestration, CI/CD tools, security automation

---

### 3.6.3 Application Owners

**Responsibilities**:
- Define application-specific configuration requirements
- Participate in baseline development for application platforms
- Submit change requests for application configuration changes
- Validate application functionality after configuration changes
- Coordinate with system administrators on application dependencies

**Authority**:
- Approve application configuration changes impacting business functionality
- Define application-specific security requirements (in collaboration with Security team)
- Escalate application issues related to configuration changes

---

### 3.6.4 Asset Owners

**Responsibilities**:
- Approve configuration baselines for assets under their ownership
- Business justification for configuration deviations
- Risk acceptance for configuration exceptions
- Participate in configuration audits for owned assets
- Fund configuration management activities for owned assets (in some organizational models)

**Authority**:
- Approve configuration baselines for owned assets
- Request configuration changes
- Accept residual risk for justified deviations (with CISO concurrence)

**Note**: Asset ownership is a governance concept—asset owners are typically business leaders responsible for the business value and risk of IT assets, not technical administrators.

---

## 3.7 Security and Compliance Roles

### 3.7.1 Security Architect

**Responsibilities**:
- Define security hardening standards (based on CIS, STIG, vendor guides)
- Review and approve security-relevant baselines
- Provide security guidance for complex or high-risk changes
- Evaluate security implications of configuration deviations
- Design compensating controls for justified exceptions
- Participate in CAB for security-sensitive changes

**Authority**:
- Mandate security hardening requirements
- Reject baselines or changes that create unacceptable security risk
- Escalate security concerns to CISO

---

### 3.7.2 Security Engineers / Analysts

**Responsibilities**:
- Deploy and maintain security monitoring tools (SIEM, configuration scanners)
- Configure alerting rules for security-relevant drift
- Investigate security-related configuration drift
- Conduct security assessments of configuration baselines
- Perform vulnerability scanning and compliance scanning
- Coordinate with system administrators on security remediation

**Authority**:
- Require remediation of security-critical configuration issues
- Declare security incidents based on configuration drift

---

### 3.7.3 Compliance Officer / GRC Team

**Responsibilities**:
- Map configuration management requirements to regulatory obligations
- Coordinate compliance audits and evidence collection
- Track remediation of audit findings
- Report compliance status to management and regulators
- Maintain compliance evidence repository

**Authority**:
- Request evidence and documentation for compliance audits
- Escalate compliance gaps to CISO and executive management

---

## 3.8 Supporting Roles

### 3.8.1 Network Administrators

**Responsibilities**:
- Implement network device configurations according to baselines
- Execute approved network configuration changes
- Monitor network device configuration drift
- Maintain network configuration backups
- Participate in CAB for network changes

---

### 3.8.2 Database Administrators (DBAs)

**Responsibilities**:
- Implement database configurations according to baselines
- Execute approved database configuration changes
- Monitor database configuration drift
- Maintain database configuration backups
- Participate in CAB for database changes

---

### 3.8.3 Cloud Architects / Cloud Engineers

**Responsibilities**:
- Design cloud configurations according to security baselines
- Implement cloud configuration changes
- Monitor cloud configuration drift using cloud-native tools
- Develop IaC for cloud infrastructure
- Participate in CAB for cloud infrastructure changes

---

## 3.9 RACI Matrix - Key Activities

### 3.9.1 Baseline Configuration Management

| Activity | CISO | CIO/CTO | Config Mgr | Sys Admin | DevOps | Security Arch | Asset Owner | CAB |
|----------|------|---------|------------|-----------|--------|---------------|-------------|-----|
| Define baseline standards | A | C | R | C | C | C | I | I |
| Develop specific baselines | I | I | A | R | R | C | C | I |
| Approve baselines | C | C | A | I | I | C | C | I |
| Implement baselines | I | I | C | R | R | I | I | I |
| Review baselines (periodic) | I | I | A | C | C | C | C | I |
| Update baselines | I | I | A | R | R | C | C | C |

**Legend**: R = Responsible, A = Accountable, C = Consulted, I = Informed

---

### 3.9.2 Change Control

| Activity | CISO | CIO/CTO | Config Mgr | Sys Admin | DevOps | Security Arch | CAB | IT Ops Mgr |
|----------|------|---------|------------|-----------|--------|---------------|-----|------------|
| Submit change request | I | I | I | R | R | I | I | I |
| Review change request | I | I | R | I | I | C | A | C |
| Approve standard change | I | I | A | I | I | I | I | C |
| Approve normal change | I | I | C | I | I | C | A | C |
| Approve emergency change | A/C | A/C | C | I | I | C | I | C |
| Implement change | I | I | C | R | R | I | I | C |
| Validate change success | I | I | C | R | R | I | I | C |
| Update documentation | I | I | C | R | R | I | I | I |

---

### 3.9.3 Configuration Monitoring and Drift Remediation

| Activity | CISO | Config Mgr | SOC Mgr | Sys Admin | Security Engineer | IT Ops Mgr |
|----------|------|------------|---------|-----------|-------------------|------------|
| Deploy monitoring tools | C | A | R | C | R | C |
| Configure monitoring rules | C | A | C | C | R | C |
| Detect configuration drift | I | C | C | I | R | I |
| Triage drift alerts | I | C | R | C | R | C |
| Investigate drift | I | C | C | R | C | C |
| Remediate drift | I | C | C | R | C | A |
| Escalate security incidents | A | C | R | I | R | I |
| Report monitoring metrics | I | A | C | I | C | C |

---

### 3.9.4 Security Hardening

| Activity | CISO | Config Mgr | Security Arch | Sys Admin | DevOps | Compliance Officer |
|----------|------|------------|---------------|-----------|--------|--------------------|
| Define hardening standards | A | C | R | C | C | C |
| Implement hardening | I | C | C | R | R | I |
| Scan for compliance | I | C | C | C | C | R |
| Remediate gaps | I | A | C | R | R | C |
| Approve deviations | A | C | C | I | I | C |
| Audit hardening | C | C | C | I | I | R |

---

## 3.10 Role Assignment and Coverage

**MUST Requirements**:
- [Organization] MUST formally assign individuals to configuration management roles
- Critical roles (Configuration Manager, CAB Chair, SOC Manager) MUST have designated backups or deputies
- Role assignments MUST be documented and communicated
- Changes to role assignments MUST be communicated to all affected parties

**SHOULD Requirements**:
- Role assignments SHOULD be documented in an HR system or organizational directory
- [Organization] SHOULD conduct succession planning for critical roles
- Backup role assignments SHOULD be tested periodically (e.g., primary on vacation, backup executes responsibilities)

---

## 3.11 Training and Competency

**MUST Requirements**:
- All personnel assigned to configuration management roles MUST receive role-specific training
- Training MUST cover:
  - Configuration management policies and procedures
  - Baseline standards and hardening requirements
  - Change control process
  - Monitoring and remediation procedures
  - Tools and systems (CMDB, change management, monitoring tools)
- Training MUST be documented and records retained

**SHOULD Requirements**:
- Training SHOULD occur:
  - Within 30 days of role assignment
  - Annually for refresher training
  - When policies or procedures change significantly
- [Organization] SHOULD track training completion and competency assessment
- Advanced training SHOULD be provided for specialized roles (Security Architect, DevOps Engineers)

---

## 3.12 Role Conflicts and Segregation of Duties

**MUST Requirements**:
- The following role combinations MUST NOT be assigned to the same individual for Critical and High criticality assets:
  - **Change Requestor + Change Approver** - Cannot approve own changes
  - **Change Implementer + Change Validator** - Independent validation required
  - **Baseline Creator + Baseline Approver** - Separation of duties for baselines
  - **Auditor + Auditee** - Internal Audit must be independent
- Role conflicts MUST be documented and approved by CISO if unavoidable (e.g., small organizations)
- Compensating controls MUST be implemented where role conflicts exist (e.g., management review, peer review, audit sampling)

**SHOULD Requirements**:
- [Organization] SHOULD maintain a segregation of duties matrix
- Role assignments SHOULD be reviewed quarterly for conflicts
- Automated tools (CMDB, change management systems) SHOULD enforce segregation where possible

**The Reality for Small Organizations**:
*Small organizations may not have enough personnel to fully separate all roles. In these cases, document the conflict, implement compensating controls (management review, audit), and plan to separate roles as the organization grows.*

---

## 3.13 Performance Metrics for Roles

**SHOULD Requirements**:
- [Organization] SHOULD establish performance metrics for configuration management roles:
  - **Configuration Manager**: Baseline coverage %, drift remediation SLA compliance, change success rate
  - **SOC Manager**: Mean time to detect drift (MTTD), mean time to respond (MTTR)
  - **System Administrators**: Configuration compliance %, change success rate, documentation quality
  - **CAB**: Average change approval time, change backlog, meeting attendance
- Metrics SHOULD be reviewed regularly (monthly or quarterly)
- Poor performance SHOULD trigger process improvement or additional training

---

## 3.14 Escalation and Decision Authority

### 3.14.1 Escalation Hierarchy

**Standard Escalation Path**:
1. **Operational Issue**: System Administrator → IT Operations Manager → CIO/CTO
2. **Security Issue**: Security Engineer → SOC Manager → CISO
3. **Configuration Conflict**: Configuration Manager → CAB → CIO/CTO + CISO (jointly)
4. **High-Risk Change**: CAB → CISO + CIO/CTO → Executive Leadership
5. **Unresolved Exception**: Configuration Manager → CISO → Executive Leadership

**Emergency Escalation**:
- Security incidents bypass normal escalation (immediate CISO notification)
- Critical service outages bypass normal escalation (immediate CIO/CTO notification)

---

### 3.14.2 Decision Authority Matrix

| Decision Type | Authority | Escalation |
|---------------|-----------|------------|
| Standard Change Approval | Configuration Manager | CAB (if pattern changes) |
| Normal Change Approval | CAB | CIO/CTO + CISO (if high risk) |
| Emergency Change Approval | CIO/CTO or CISO | Executive Leadership (post-event review) |
| Baseline Approval (minor) | Configuration Manager | CAB |
| Baseline Approval (major) | CAB | CIO/CTO |
| Security Hardening Standard | Security Architect | CISO |
| Configuration Deviation (low risk) | Configuration Manager | CAB |
| Configuration Deviation (high risk) | CISO | Executive Leadership |
| Audit Finding Remediation | Accountable Role | Management (if not resolved) |

---

## 3.15 External Parties and Third-Party Roles

**SHOULD Requirements**:
- [Organization] SHOULD extend configuration management roles and responsibilities to external parties where they manage [Organization]'s IT assets:
  - Managed service providers (MSPs)
  - Cloud service providers (for customer-managed configurations)
  - Contractors and consultants
  - Outsourced IT operations
- Contractual agreements SHOULD define:
  - Baseline compliance requirements
  - Change control procedures (integration with [Organization]'s CAB)
  - Monitoring and reporting obligations
  - Incident escalation procedures
  - Audit and access rights
- External parties SHOULD have documented roles analogous to internal roles

---

## 3.16 The Reality of Roles and Responsibilities

**Feynman's Final Word**: 

*"The best RACI matrix is the one that people actually use. If your organization chart requires a 15-person approval chain for every firewall rule change, the real organization chart will involve a lot of 'emergency changes' at 2 AM and a pervasive culture of policy circumvention.*

*Good role definition balances three principles:*
*1. Accountability (someone owns the outcome)
2. Empowerment (people have authority to do their jobs)
3. Oversight (checks and balances prevent mistakes)*

*For most organizations, this means: make system administrators responsible for implementation, make CAB accountable for approval, make Security and Operations jointly consulted, and make auditors independent. Start there, then adjust based on what actually breaks."*

---

**END OF DOCUMENT**

**Cross-References**:
- ISMS-POL-A.8.9: Configuration Management (Master Policy)
- ISMS-POL-A.8.9-S1: Purpose, Scope, Definitions
- ISMS-POL-A.8.9-S2: Requirements Overview
- ISMS-POL-A.8.9-S4: Policy Governance (next)

---