# ISMS-POL-A.8.12-S3
## Data Leakage Prevention - Roles and Responsibilities

**Document ID**: ISMS-POL-A.8.12-S3  
**Title**: Roles and Responsibilities  
**Version**: 1.0  
**Date**: 2025-01-03  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-03 | Information Security Manager / HR | Initial RACI definition for DLP |

**Review Cycle**: Annual (or upon significant organizational restructuring)  
**Next Review Date**: 2026-01-03  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- HR Approval: Human Resources Director (for role alignment with employment practices)
- Management Approval: IT Director / CIO (for resource commitment)

**Distribution**: All stakeholders with defined roles, management, HR  
**Related Documents**: Organizational Chart, Job Descriptions, ISMS-POL-A.8.12 (Master), ISMS-POL-A.5.24-28 (Incident Management)

---

## 1. Purpose and Scope

This document defines **roles and responsibilities** for Data Leakage Prevention (DLP) implementation, operation, governance, and incident response. Clear accountability ensures effective policy enforcement, rapid incident response, and continuous improvement.

**Key Principle**: Responsibilities are assigned to **roles**, not specific individuals. Role assignments may change as the organization evolves, but responsibilities remain consistent.

**In Scope**: All roles involved in DLP lifecycle (policy definition, technology deployment, monitoring, incident response, user compliance)  
**Primary Stakeholders**: All organizational personnel  
**Implementation Evidence**: ISMS-IMP-A.8.12 (all assessment workbooks demonstrate role execution)

---

## 2. Responsibility Model

### 2.1 RACI Framework

This policy uses the **RACI model** to clarify responsibilities:

- **R - Responsible**: Performs the work, executes the task
- **A - Accountable**: Ultimately answerable, has approval authority (only ONE per task)
- **C - Consulted**: Provides input, must be consulted before action
- **I - Informed**: Kept informed, notified of outcomes

### 2.2 Separation of Duties

Where appropriate, responsibilities are separated to ensure checks and balances:

- **Policy definition** (what should be done) separated from **implementation** (how it's done)
- **Approval authority** separated from **requestor** (no self-approval for exceptions)
- **Monitoring** separated from **system administration** (detect unauthorized changes)
- **Investigation** separated from **disciplinary action** (objectivity in employee matters)

Organizations MAY combine roles in small organizations where separation is impractical, but SHALL document combined roles and implement compensating controls (e.g., external audit reviews).

---

## 3. Executive Roles

### 3.1 Chief Information Security Officer (CISO)

**Primary Accountability**: Overall DLP program success

**Responsibilities:**

**Policy Governance:**
- Establishing and maintaining DLP policy framework
- Approving policy changes and updates
- Ensuring policy alignment with organizational risk appetite
- Reviewing policy effectiveness annually

**Risk Management:**
- Defining acceptable risk levels for data leakage
- Approving high-risk exceptions (Critical/High incidents per S2.4)
- Accepting residual risks (coverage gaps, limitations)
- Escalating significant risks to Executive Management

**Strategic Decisions:**
- Approving DLP technology selection and procurement
- Allocating budget and resources for DLP program
- Defining phased deployment strategy (S2.2 - Channel Protection)
- Approving DLP roadmap and improvement initiatives

**Incident Response:**
- Serving as escalation point for Critical DLP incidents
- Approving incident response procedures
- Reviewing post-incident analyses and lessons learned
- Authorizing breach notifications (with Legal/DPO)

**Compliance:**
- Ensuring DLP controls meet ISO 27001:2022 Control A.8.12
- Ensuring compliance with FADP/GDPR employee monitoring requirements
- Supporting internal and external audits
- Approving audit remediation plans

### 3.2 Chief Information Officer (CIO) / IT Director

**Primary Accountability**: Technology infrastructure support for DLP

**Responsibilities:**

- Approving DLP technology procurement and deployment
- Ensuring IT infrastructure supports DLP requirements (network bandwidth, storage capacity, endpoint coverage)
- Coordinating DLP integration with existing systems (SIEM, email gateway, endpoint security)
- Allocating IT Operations resources for DLP deployment and maintenance
- Approving DLP-related infrastructure changes (network architecture, cloud services)

### 3.3 Data Protection Officer (DPO)

**Primary Accountability**: Employee monitoring compliance and privacy protection

**Responsibilities:**

**Privacy Compliance:**
- Conducting Data Protection Impact Assessment (DPIA) for DLP deployment
- Ensuring lawful basis for employee monitoring (FADP Article 26, GDPR Article 5)
- Verifying proportionality of DLP monitoring (Swiss Employment Law Article 328b CO)
- Reviewing employee notification and transparency requirements

**Data Subject Rights:**
- Handling data subject access requests (employees requesting DLP logs about them)
- Advising on employee privacy rights during DLP investigations
- Ensuring data minimization in DLP logging (S2.3)
- Reviewing log retention policies for FADP/GDPR compliance

**Breach Notification:**
- Determining if DLP incidents require breach notification (FADP Article 24, GDPR Article 33-34)
- Coordinating with Legal on notification timeline and content
- Notifying FDPIC (Swiss) or DPA (EU) within required timelines
- Documenting breach notification decisions for audit purposes

**Works Council Coordination** (where applicable):
- Consulting with works council on DLP monitoring practices
- Negotiating acceptable monitoring practices (co-determination rights)
- Documenting agreements and employee consent

### 3.4 Executive Management / Board

**Primary Accountability**: Strategic approval and risk acceptance

**Responsibilities:**

- Approving DLP program strategy and budget
- Accepting residual risks for coverage gaps (unprotected channels, false negative rates)
- Escalation point for Critical incidents with reputational/regulatory/legal impact
- Approving major policy changes affecting employee privacy or business operations
- Reviewing DLP effectiveness in quarterly/annual security reports

---

## 4. Operational Roles

### 4.1 Information Security Officer (ISO) / Security Manager

**Primary Accountability**: DLP policy ownership and enforcement

**Responsibilities:**

**Policy Ownership:**
- Developing and maintaining DLP policy documents (S1-S5)
- Coordinating policy reviews (annual, triggered)
- Updating policies based on lessons learned and regulatory changes

**Enforcement:**
- Monitoring DLP policy compliance
- Managing exception process (reviewing requests, recommending approval/denial)
- Escalating policy violations to appropriate authorities (HR, Legal, CISO)

**Assessment Coordination:**
- Coordinating quarterly DLP assessments (ISMS-IMP-A.8.12.1-5)
- Reviewing assessment results and identifying gaps
- Developing remediation plans for identified gaps
- Tracking remediation progress

**Metrics and Reporting:**
- Generating DLP effectiveness metrics (coverage %, false positive rate, incident counts)
- Reporting to CISO and management (monthly operational, quarterly strategic)
- Supporting audit activities (evidence collection, documentation)

### 4.2 Security Engineering

**Primary Accountability**: DLP technology implementation and tuning

**Responsibilities:**

**Technology Deployment:**
- Developing Python assessment generators (ISMS-IMP-A.8.12.1-5 Excel workbooks)
- Developing validation and sanity-check scripts
- Testing DLP solutions before production deployment
- Integrating DLP with SIEM, SOC tools, incident management systems

**Rule Development:**
- Translating data classification requirements (S2.1) into DLP detection rules
- Developing detection patterns (regex, fingerprints, keywords, ML models)
- Tuning DLP rules to reduce false positives (target <10% FP rate)
- Testing new rules in monitor-only mode before enforcement

**Technical Support:**
- Providing Tier 3 technical support for complex DLP issues
- Troubleshooting DLP performance or integration problems
- Optimizing DLP system performance (latency, storage, scalability)
- Researching new DLP capabilities and recommending enhancements

### 4.3 IT Operations

**Primary Accountability**: DLP system operation and maintenance

**Responsibilities:**

**System Administration:**
- Operating DLP solutions (network, endpoint, cloud, email)
- Deploying DLP agents to endpoints (laptops, desktops, servers)
- Configuring DLP policies and rules (based on Security Engineering specifications)
- Maintaining DLP system uptime and performance

**Rule Deployment:**
- Deploying approved DLP rules to production
- Implementing policy exceptions (authorized by ISO/CISO)
- Rolling back problematic rules if excessive false positives occur

**Monitoring:**
- Monitoring DLP system health (uptime, performance, agent status)
- First-level triage of DLP alerts (validate vs. false positive)
- Escalating security incidents to SOC/Security Team
- Maintaining DLP infrastructure (patching, updates, capacity planning)

### 4.4 Security Operations Center (SOC)

**Primary Accountability**: DLP alert monitoring and incident triage

**Responsibilities:**

**Alert Monitoring:**
- Monitoring SIEM for DLP alerts (real-time, 24x7 for Critical/High alerts)
- Triaging alerts per severity (Critical: 15 min, High: 1 hour, Medium: 4 hours per S2.3)
- Validating alerts (true positive vs. false positive)

**Incident Management:**
- Classifying DLP incidents by severity (Critical/High/Medium/Low per S2.4)
- Conducting initial investigation (user context, data sensitivity, business impact)
- Escalating High/Critical incidents to Incident Response team
- Handling Medium/Low incidents within SOC (user education, manager notification)

**Continuous Improvement:**
- Reporting false positive patterns to Security Engineering (for tuning)
- Contributing to lessons learned and post-incident reviews
- Recommending policy adjustments based on operational experience

### 4.5 Incident Response Team

**Primary Accountability**: DLP incident investigation and remediation

**Responsibilities:**

**Investigation:**
- Conducting forensic investigation of High/Critical DLP incidents
- Determining root cause (malicious, negligent, policy gap, control gap)
- Preserving evidence (DLP logs, endpoint forensics, email audit)
- Interviewing users (with HR/Legal support where appropriate)

**Containment:**
- Executing containment actions (disable accounts, isolate endpoints, block external access)
- Coordinating with IT Operations on technical containment
- Notifying stakeholders (Data Owners, Legal, DPO, HR, Executive Management)

**Remediation:**
- Implementing remediation plans (policy updates, training, technology fixes)
- Tracking remediation to completion
- Verifying gap closure through testing
- Documenting lessons learned

**Breach Notification Support:**
- Supporting DPO/Legal in breach notification process
- Providing technical details for notification (scope, data categories, affected individuals)
- Coordinating with external parties (law enforcement, cyber insurance, forensic firms)

---

## 5. Data and System Owner Roles

### 5.1 Data Owners

**Primary Accountability**: Data classification and access authorization

**Responsibilities:**

**Data Classification:**
- Classifying data within their domain (Public, Internal, Confidential, Restricted per S2.1)
- Defining DLP protection requirements for their data
- Reviewing and updating classifications based on business value changes
- Approving or denying DLP exceptions for their data

**Risk Assessment:**
- Assessing business impact of data leakage incidents
- Determining if breach notification is required (with DPO/Legal)
- Participating in incident investigations involving their data
- Approving compensating controls for DLP exceptions

**Continuous Improvement:**
- Providing feedback on DLP false positives affecting legitimate business workflows
- Recommending DLP policy adjustments for business efficiency
- Participating in post-incident reviews

### 5.2 System Owners

**Primary Accountability**: DLP implementation within their systems

**Responsibilities:**

**Implementation:**
- Implementing DLP controls within their systems (applications, databases, cloud services)
- Providing evidence for DLP assessments (ISMS-IMP-A.8.12.1-5)
- Configuring system-specific DLP settings (database export controls, API rate limits)
- Testing DLP integration with their systems

**Maintenance:**
- Maintaining DLP agent deployment on endpoints they manage
- Updating system configurations to support DLP requirements
- Troubleshooting system-specific DLP issues
- Participating in DLP testing and validation

---

## 6. Supporting Roles

### 6.1 Human Resources (HR)

**Primary Accountability**: Employee awareness and policy violations

**Responsibilities:**

**Policy Integration:**
- Integrating DLP policy into employment contracts and handbook
- Including DLP awareness in new hire onboarding
- Ensuring Acceptable Use Policy (AUP) acknowledgment from all employees

**Training:**
- Coordinating DLP security awareness training (annual, new hires)
- Tracking training completion rates
- Conducting targeted training for users with repeated violations

**Violation Handling:**
- Investigating alleged DLP policy violations (with Security Team)
- Determining appropriate disciplinary actions (warning, suspension, termination)
- Ensuring consistent enforcement across organization
- Documenting violations and disciplinary actions
- Protecting employee privacy rights during investigations

**Privacy Compliance:**
- Ensuring DLP monitoring practices comply with employment law
- Consulting with works council (where required)
- Handling employee concerns about DLP monitoring

### 6.2 Legal and Compliance

**Primary Accountability**: Legal and regulatory compliance

**Responsibilities:**

**Legal Review:**
- Reviewing DLP policies for legal compliance (employment law, data protection, telecommunications)
- Advising on FADP/GDPR employee monitoring requirements
- Reviewing employee notification and consent requirements
- Assessing cross-border data transfer implications (DLP logs)

**Incident Support:**
- Advising on legal implications of DLP incidents
- Coordinating breach notification (with DPO)
- Managing legal hold on evidence for litigation
- Liaising with law enforcement when appropriate (computer fraud, espionage)

**Contract Review:**
- Reviewing DLP vendor contracts and data processing agreements
- Ensuring contractual DLP obligations are met (customer contracts requiring DLP)
- Negotiating SLAs and liability terms

### 6.3 IT Support / Help Desk

**Primary Accountability**: User support for DLP issues

**Responsibilities:**

- First-level support for users blocked by DLP (explain policy, provide alternatives)
- Intake of DLP exception requests (forward to Security Team)
- Escalating technical DLP issues to IT Operations
- Educating users on DLP policy during support interactions
- Reporting false positive patterns to Security Team

### 6.4 Internal Audit

**Primary Accountability**: Independent compliance verification

**Responsibilities:**

**Audit Execution:**
- Conducting periodic audits of DLP controls (annual or as scheduled)
- Verifying policy compliance (are requirements being met?)
- Testing control effectiveness (is DLP actually preventing data leakage?)
- Reviewing exception management process (are exceptions justified and properly approved?)

**Reporting:**
- Reporting audit findings to CISO and Executive Management
- Providing independent assessment of DLP maturity
- Recommending improvements based on audit findings
- Tracking remediation progress for audit findings

**Risk Assessment Support:**
- Including DLP in enterprise risk assessments
- Evaluating residual risks from DLP limitations
- Reporting DLP risks to Board/Audit Committee

---

## 7. User Responsibilities

### 7.1 All Employees

**Primary Accountability**: Policy compliance

**Responsibilities:**

**Policy Adherence:**
- Complying with DLP policy and Acceptable Use Policy (AUP)
- Handling sensitive data according to classification level (S2.1)
- Using approved channels for data transfers (no personal email, USB, cloud)
- Reporting suspected data leakage or policy violations

**Security Awareness:**
- Completing annual DLP security awareness training
- Understanding what data is protected and why
- Understanding that data transfers are monitored (transparency requirement)
- Acknowledging no expectation of privacy on organizational networks

**Exception Requests:**
- Requesting exceptions through proper channels (not bypassing DLP)
- Providing business justification for exception requests
- Accepting responsibility for data handled under exceptions

**Incident Reporting:**
- Reporting false positives (legitimate business activity blocked)
- Reporting DLP issues (performance, usability)
- Cooperating with incident investigations

**Consequences:**
- Understanding that policy violations may result in disciplinary action (warning, suspension, termination)
- Accepting that DLP monitoring is for security and compliance purposes

### 7.2 Privileged Users (Administrators, Developers, Executives)

**Primary Accountability**: Enhanced responsibility due to elevated access

**Additional Responsibilities:**

- Heightened awareness of DLP monitoring (access to sensitive data = higher scrutiny)
- Role-modeling secure data handling practices
- Providing strong business justification for exceptions (elevated access = elevated risk)
- Enhanced DLP monitoring (stricter alerting thresholds)
- Accepting more restrictive DLP controls (e.g., USB blocking for all admins)

### 7.3 Contractors and Third Parties

**Primary Accountability**: Contractual DLP obligations

**Responsibilities:**

- Complying with organizational DLP policy per contract terms
- Adhering to Acceptable Use Policy (AUP)
- Reporting DLP incidents involving organizational data
- Accepting DLP monitoring for systems they access
- Notifying organization of data breaches involving organizational data

---

## 8. RACI Matrix Summary

| Activity | CISO | ISO/SM | Sec Eng | IT Ops | SOC | IR Team | Data Owner | HR | Legal | DPO | Users |
|----------|------|--------|---------|--------|-----|---------|------------|-------|-------|-----|-------|
| **Policy Definition** | A | R | C | C | I | I | C | C | C | C | I |
| **DLP Technology Selection** | A | R | C | C | I | I | I | I | C | I | I |
| **Rule Development** | I | C | A/R | C | C | I | C | I | I | I | I |
| **Rule Deployment** | I | C | C | A/R | I | I | I | I | I | I | I |
| **Agent Deployment** | I | C | C | A/R | I | I | I | I | I | I | I |
| **Alert Monitoring** | I | C | I | C | A/R | C | I | I | I | I | I |
| **Incident Triage** | I | C | I | C | A/R | C | I | I | I | I | I |
| **Incident Investigation** | C | C | C | C | C | A/R | C | C | C | C | R |
| **Incident Containment** | C | C | C | R | R | A | C | C | C | C | I |
| **Breach Notification** | A | C | I | I | I | R | C | C | R | R | I |
| **Exception Request** | I | C | I | I | I | I | C | I | I | I | A/R |
| **Exception Approval (Low)** | I | A/R | C | I | I | I | C | I | I | I | I |
| **Exception Approval (High)** | A | R | C | I | I | I | C | C | C | C | I |
| **False Positive Tuning** | I | C | A/R | C | C | C | I | I | I | I | R |
| **Policy Violation Enforcement** | C | C | I | I | C | C | C | A/R | C | C | - |
| **User Training** | C | C | I | I | I | I | C | A/R | I | C | R |
| **Policy Review** | A | R | C | C | C | C | C | C | C | C | I |
| **Audit Compliance** | A | R | C | C | C | C | C | C | C | C | I |

**Legend**: A = Accountable, R = Responsible, C = Consulted, I = Informed, - = Not involved

---

## 9. Role Transitions and Handovers

### 9.1 Personnel Changes

When personnel change roles affecting DLP responsibilities:

**Departing Personnel:**
- Document current state of DLP responsibilities (in-progress projects, pending decisions)
- Transfer knowledge to successor (DLP configurations, exception rationales, incident context)
- Complete handover checklist
- Revoke access to DLP management systems (principle of least privilege)

**New Personnel:**
- Receive role-specific DLP training
- Obtain necessary access to DLP systems and tools
- Review DLP documentation and exception register
- Shadow predecessor where possible (overlap period)

### 9.2 Organizational Changes

When organizational structure changes (mergers, acquisitions, reorganizations):

- Review and update role assignments
- Ensure no responsibilities are orphaned (all RACI entries have assigned roles)
- Document any role consolidations and compensating controls
- Communicate changes to all stakeholders
- Update this policy section (S3) as needed

---

## 10. Accountability and Escalation

### 10.1 Performance Accountability

Role performance is measured through:

**Security Metrics:**
- DLP incident response times (SLA compliance per S2.4)
- False positive management (tuning effectiveness per S2.3)
- Policy compliance (exception adherence, audit findings)
- Incident outcomes (effective remediation, recurrence prevention)

**Operational Metrics:**
- DLP system uptime and performance
- User satisfaction (support responsiveness, training effectiveness)
- Continuous improvement contributions (lessons learned, policy updates)

### 10.2 Escalation Paths

**Technical Escalation:**
- IT Operations → Security Engineering → CISO
- Vendor support → IT Operations → Security Engineering → CISO

**Policy/Risk Escalation:**
- ISO/Security Team → CISO → Executive Management
- Business Unit Manager → CISO → Executive Management

**Incident Escalation (per S2.4):**
- SOC → Incident Response Team → CISO → Executive Management → Board (if Critical with reputational/regulatory/legal impact)
- Timeline: Critical incidents escalated to CISO within 1 hour, to Executive Management within 4 hours

**Exception Escalation:**
- Low risk (routine business need): ISO/Security Team approval
- Medium risk (confidential data, approved business partners): CISO approval
- High risk (restricted data, unapproved destinations): CISO + Legal/DPO approval + Executive Management notification

**Privacy/Legal Escalation:**
- Employee concerns about monitoring → HR → DPO → Legal → CISO
- Breach notification required → DPO → Legal → CISO → Executive Management

---

## 11. Integration with DLP Framework

This roles and responsibilities document (S3) integrates with:

- **S1 (Purpose, Scope, Definitions)**: Defines what roles are responsible for
- **S2 (Requirements)**: Assigns accountability for each requirement domain
- **S2.3 (Monitoring & Detection)**: SOC, Security Team, IT Operations roles
- **S2.4 (Incident Response)**: Incident Response, HR, Legal, DPO roles
- **S4 (Policy Governance)**: CISO, ISO policy review and update responsibilities
- **S5 (Annexes)**: Operational procedures executed by assigned roles

---

## 12. References

### 12.1 Internal Policy Documents

- **ISMS-POL-A.8.12** - Master DLP Policy
- **ISMS-POL-A.8.12-S2** - DLP Requirements Overview
- **ISMS-POL-A.8.12-S2.4** - Incident Response & Remediation
- **ISMS-POL-A.5.24-28** - Organizational Incident Management
- **Organizational Chart** - Current role assignments
- **Job Descriptions** - Detailed role specifications

### 12.2 Regulatory References

- **ISO/IEC 27001:2022** - Control A.8.12 (Data Leakage Prevention), Control 5.2 (Roles and Responsibilities)
- **Swiss FADP** - Article 26 (Employee data processing)
- **EU GDPR** - Article 5 (Lawfulness, fairness, transparency)

---

**END OF DOCUMENT**

*"Responsibility without authority is frustration. Authority without responsibility is tyranny. This RACI matrix provides both."*  
*— The Wisdom of Organizational Design*