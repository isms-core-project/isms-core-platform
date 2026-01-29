# ISMS-POL-A.8.9-S2.2
## Configuration Management - Change Control Requirements

**Document ID**: ISMS-POL-A.8.9-S2.2  
**Title**: Change Control Requirements  
**Version**: 1.0  
**Date**: [Date] 
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]| Configuration Manager / Information Security Manager | Initial change control requirements |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: 08.01.2027  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Configuration Manager / Chief Technology Officer
- Operations Review: Change Advisory Board (CAB) Chair / IT Operations Manager

**Distribution**: CAB members, configuration management team, system administrators, DevOps engineers, application owners  
**Related Documents**: ISMS-POL-A.8.9-S1 (Definitions), ISMS-POL-A.8.9-S2.1 (Baseline Requirements), ISMS-IMP-A.8.9.2 (Change Control Assessment)

---

## 2.2.1 Purpose

This document defines **mandatory and recommended requirements** for controlling changes to IT configurations. Change control ensures that configuration modifications are:
- **Authorized** - Approved by appropriate authority before implementation
- **Documented** - Recorded with sufficient detail for audit and rollback
- **Risk-Assessed** - Evaluated for potential security and operational impact
- **Reversible** - Capable of being rolled back if unsuccessful
- **Traceable** - Linked to baselines, incidents, and business requirements

**The Anti-Pattern**: Organizations that require a 47-field change request form and 3-week approval cycle for changing a firewall rule description, then wonder why engineers make "undocumented emergency changes" at 2 AM.

**The Feynman Standard**: *"The best change control process is one that people actually follow. If your process is so bureaucratic that Shadow IT emerges, you've failed. Design for speed AND safety."*

---

## 2.2.2 Change Classification

### 2.2.2.1 Classification Framework

**MUST Requirements**:
- [Organization] MUST classify all configuration changes into one of three categories:
  - **Standard Changes** - Pre-approved, low-risk, repeatable changes
  - **Normal Changes** - Require evaluation and approval before implementation
  - **Emergency Changes** - Urgent changes implemented with expedited approval
- The classification criteria MUST be documented and communicated to all technical staff
- Each classification MUST have a defined approval authority and timeline

**SHOULD Requirements**:
- Classification criteria SHOULD consider:
  - Business impact (revenue, customer service, regulatory compliance)
  - Technical risk (potential for service disruption, data loss, security exposure)
  - Scope (number of affected systems, users, or services)
  - Reversibility (ease and speed of rollback)
- [Organization] SHOULD maintain a Standard Change Catalog listing all pre-approved changes

**MAY Requirements**:
- [Organization] MAY define additional change sub-categories (e.g., "Expedited Normal Change")
- [Organization] MAY establish different approval workflows based on asset criticality

---

### 2.2.2.2 Standard Changes

**Definition**: Pre-approved, low-risk changes that follow a documented procedure and require no additional authorization at time of execution.

**MUST Requirements**:
- Each Standard Change MUST have:
  - **Unique identifier and name**
  - **Documented procedure** - Step-by-step instructions
  - **Risk assessment** - Initial evaluation justifying pre-approval
  - **Approval record** - Evidence of CAB or equivalent pre-approval
  - **Success criteria** - How to verify the change worked
  - **Rollback procedure** - How to undo if needed
- Standard Changes MUST be reviewed at least annually to confirm they remain low-risk
- If a Standard Change fails or causes an incident, it MUST be suspended and re-evaluated

**SHOULD Requirements**:
- Standard Changes SHOULD include:
  - Estimated execution time
  - Required skill level or role
  - Dependencies and prerequisites
  - Communication requirements
- Failed Standard Changes SHOULD trigger an incident review

**Examples of Standard Changes** (typical):
- Scheduled firmware updates on network devices (following vendor-tested procedures)
- Adding user accounts following established templates
- Scaling cloud resources within predefined limits
- Deploying application updates through approved CI/CD pipelines
- Password resets following identity verification
- Certificate renewals using established processes
- Adding storage to existing volumes within capacity plans
- Enabling/disabling pre-approved firewall rules

---

### 2.2.2.3 Normal Changes

**Definition**: Changes that require risk assessment, approval, and planning before implementation.

**MUST Requirements**:
- All Normal Changes MUST follow a documented change request process
- Each Normal Change request MUST include:
  - **Change description** - What is being changed and why
  - **Business justification** - Why this change is needed
  - **Implementation plan** - How and when the change will be executed
  - **Risk assessment** - Potential impacts and mitigation measures
  - **Rollback plan** - How to undo the change if unsuccessful
  - **Testing approach** - How the change will be validated
  - **Communication plan** - Who needs to be informed and when
- Normal Changes MUST be approved by the Change Advisory Board (CAB) or designated authority
- Approval MUST be documented and retained for audit purposes

**SHOULD Requirements**:
- Normal Change requests SHOULD include:
  - **Configuration Item (CI) references** - Links to CMDB entries
  - **Baseline references** - Current and target states
  - **Related incidents or problems** - If change is remediation
  - **Resource requirements** - Personnel, time, tools
  - **Maintenance window requirements** - If service interruption is needed
  - **Success metrics** - Measurable outcomes
- CAB meetings SHOULD occur at a regular cadence (weekly or bi-weekly for most organizations)
- CAB decisions SHOULD be based on risk-balanced evaluation, not pure risk avoidance

**MAY Requirements**:
- [Organization] MAY delegate approval authority for low-complexity Normal Changes to specific roles (e.g., "Infrastructure Change Manager")
- CAB MAY defer changes requiring additional information or risk assessment
- [Organization] MAY implement automated change request workflows

---

### 2.2.2.4 Emergency Changes

**Definition**: Urgent changes required to resolve critical incidents or security vulnerabilities, implemented with expedited approval.

**MUST Requirements**:
- Emergency Changes MUST be justified by one of the following:
  - **Critical incident resolution** - Service outage affecting business operations
  - **Security vulnerability remediation** - Active exploit or imminent threat
  - **Regulatory compliance urgency** - Mandatory deadline approaching
  - **Data integrity threat** - Risk of data loss or corruption
- Emergency Changes MUST be approved by at least one senior authority (e.g., CTO, CISO, IT Director)
- Approval MAY be verbal or via rapid communication channels (phone, instant messaging) but MUST be documented immediately after
- All Emergency Changes MUST undergo **post-implementation review** within 5 business days
- The post-review MUST evaluate:
  - Whether the emergency justification was valid
  - Whether the change achieved its objective
  - Whether proper procedures were followed given the urgency
  - Lessons learned and process improvements

**SHOULD Requirements**:
- Emergency Changes SHOULD still include:
  - Basic risk assessment (even if rapid)
  - Implementation plan (even if abbreviated)
  - Rollback plan (critical even under pressure)
- Post-implementation review SHOULD involve CAB or equivalent body
- If Emergency Changes become frequent (>10% of total changes), [Organization] SHOULD investigate root causes

**MAY Requirements**:
- [Organization] MAY establish an "Emergency Change On-Call" rotation
- [Organization] MAY define additional approval requirements for Emergency Changes affecting critical systems

**The Reality Check**: *Emergency changes will happen. The goal is not to eliminate them but to ensure they're actually emergencies and that we learn from them.*

---

## 2.2.3 Change Request Process

### 2.2.3.1 Request Submission

**MUST Requirements**:
- [Organization] MUST provide a documented method for submitting change requests
- The submission mechanism MUST capture all mandatory fields defined in Section 2.2.2.3
- Change requests MUST be assigned a unique identifier upon submission
- Requesters MUST receive acknowledgment of submission (automated or manual)

**SHOULD Requirements**:
- [Organization] SHOULD provide a change request template or form
- The submission system SHOULD integrate with the CMDB to auto-populate asset details
- Requesters SHOULD be able to track the status of their requests

**MAY Requirements**:
- [Organization] MAY implement a change request portal or ticketing system
- The system MAY provide request templates for common change types

---

### 2.2.3.2 Risk Assessment and Impact Analysis

**MUST Requirements**:
- All Normal and Emergency Changes MUST undergo risk assessment before approval
- The risk assessment MUST evaluate:
  - **Technical risk** - Potential for system failure, service disruption, or data loss
  - **Security risk** - Potential for security vulnerabilities or exposure
  - **Business impact** - Effect on users, customers, revenue, or compliance
  - **Dependencies** - Impact on related systems or services
- Risk assessment MUST assign a risk level (e.g., Critical, High, Medium, Low)
- High and Critical risk changes MUST include additional scrutiny and mitigation measures

**SHOULD Requirements**:
- Risk assessment SHOULD be performed by qualified personnel (system owners, security team, technical leads)
- [Organization] SHOULD maintain a risk assessment matrix or rubric for consistency
- Changes with significant risk SHOULD be scheduled during maintenance windows

**MAY Requirements**:
- [Organization] MAY require peer review for High and Critical risk changes
- Risk assessment MAY include automated scanning or pre-flight checks

---

### 2.2.3.3 Approval Workflows

**MUST Requirements**:
- Each change classification MUST have a defined approval workflow:
  - **Standard Changes**: Pre-approved by CAB or equivalent (annual review)
  - **Normal Changes**: Approved by CAB, Change Manager, or delegated authority
  - **Emergency Changes**: Approved by senior technical or security authority
- Approvers MUST have the technical competence to evaluate the change
- Approval decisions MUST be documented with:
  - Approver identity and role
  - Date and time of approval
  - Any conditions or restrictions attached to approval
- Rejected changes MUST include a reason for rejection

**SHOULD Requirements**:
- CAB membership SHOULD include:
  - Change Manager (chair)
  - Security representative (CISO or delegate)
  - Operations representative (IT Ops Manager)
  - Business representative (for significant changes)
  - Technical subject matter experts (as needed)
- CAB meetings SHOULD follow a documented agenda and decision-making process
- Approvers SHOULD consider:
  - Risk assessment findings
  - Business justification
  - Timing and scheduling
  - Resource availability
  - Conflict with other changes

**MAY Requirements**:
- [Organization] MAY implement tiered approval (e.g., "Manager approval for Low risk, CAB for Medium/High")
- CAB MAY delegate specific change types to sub-groups or individual approvers

---

### 2.2.3.4 Change Scheduling and Coordination

**MUST Requirements**:
- Approved changes MUST be scheduled before implementation
- The schedule MUST consider:
  - Maintenance windows (for changes requiring downtime)
  - Blackout periods (e.g., end-of-quarter financial closes, peak business periods)
  - Resource availability (personnel, tools, environments)
  - Dependencies on other changes or releases
- Conflicting or overlapping changes MUST be identified and resolved before implementation
- Scheduled changes MUST be communicated to affected stakeholders

**SHOULD Requirements**:
- [Organization] SHOULD maintain a change calendar visible to all stakeholders
- High-risk changes SHOULD be scheduled with adequate lead time for preparation
- Changes affecting critical services SHOULD occur during pre-defined maintenance windows

**MAY Requirements**:
- [Organization] MAY implement automated scheduling tools
- Change calendar MAY integrate with incident management and monitoring systems

---

## 2.2.4 Change Implementation

### 2.2.4.1 Implementation Planning

**MUST Requirements**:
- All Normal and Emergency Changes MUST have a documented implementation plan before execution
- The implementation plan MUST include:
  - **Step-by-step procedure** - Clear, sequenced instructions
  - **Execution timeline** - Estimated duration and milestones
  - **Resource requirements** - Personnel, tools, access credentials
  - **Verification steps** - How to confirm success at each stage
  - **Rollback triggers** - Conditions that require rollback
  - **Communication checkpoints** - When to update stakeholders
- Implementers MUST follow the approved plan
- Deviations from the plan MUST be documented and justified

**SHOULD Requirements**:
- Implementation plans SHOULD be reviewed by a peer before execution
- High-risk changes SHOULD include a "dress rehearsal" in a test environment
- Plans SHOULD include contingency procedures for common failure scenarios

---

### 2.2.4.2 Rollback Procedures

**MUST Requirements**:
- All Normal and Emergency Changes MUST have a documented rollback plan
- The rollback plan MUST include:
  - **Rollback decision criteria** - When to execute rollback
  - **Rollback procedure** - Step-by-step instructions to restore previous state
  - **Rollback validation** - How to verify successful rollback
  - **Rollback authority** - Who can authorize rollback decision
- Rollback procedures MUST be tested in non-production environments where feasible
- If a change is rolled back, the incident MUST be documented and reviewed

**SHOULD Requirements**:
- Rollback plans SHOULD be executable within a defined Recovery Time Objective (RTO)
- Critical systems SHOULD have automated or semi-automated rollback capabilities
- Rollback procedures SHOULD be regularly tested as part of disaster recovery exercises

**MAY Requirements**:
- [Organization] MAY implement "blue-green deployment" or canary release strategies to enable rapid rollback
- Rollback plans MAY include data restoration procedures from backups

**The Cargo Cult Warning**: *Having a rollback plan that says "restore from last night's backup" is not a real rollback plan if your last backup was 3 days ago and takes 6 hours to restore.*

---

### 2.2.4.3 Post-Implementation Validation

**MUST Requirements**:
- All changes MUST be validated after implementation to confirm:
  - The change achieved its intended objective
  - No unintended side effects occurred
  - Services are functioning as expected
  - Security controls remain effective
- Validation results MUST be documented in the change record
- Failed changes MUST trigger rollback or remediation procedures

**SHOULD Requirements**:
- Validation SHOULD include:
  - Functional testing (does the change work as intended?)
  - Integration testing (do dependent systems still work?)
  - Security testing (are security controls still effective?)
  - Performance monitoring (has performance degraded?)
- Critical changes SHOULD include an observation period before closure

**MAY Requirements**:
- [Organization] MAY implement automated post-change validation tests
- Validation MAY include stakeholder sign-off

---

## 2.2.5 Change Communication

**MUST Requirements**:
- Changes affecting service availability or user experience MUST be communicated to affected stakeholders in advance
- Emergency Changes MUST be communicated as soon as possible, even if implementation occurs before notification
- Change notifications MUST include:
  - What is changing
  - When the change will occur
  - Expected impact (service interruption, performance impact, feature changes)
  - Who to contact for questions or issues
- Change status updates MUST be provided during implementation of High and Critical risk changes

**SHOULD Requirements**:
- [Organization] SHOULD define communication plans for different change types
- Communication SHOULD be tailored to the audience (technical teams vs. business users)
- Failed changes SHOULD be communicated with transparency about impact and resolution timeline

---

## 2.2.6 Change Recording and Documentation

**MUST Requirements**:
- All changes (Standard, Normal, Emergency) MUST be recorded in a change management system or log
- Each change record MUST include:
  - Change identification (ID, title, type)
  - Dates (requested, approved, scheduled, implemented, closed)
  - Personnel involved (requester, approver, implementer)
  - Assets affected (configuration items)
  - Approval evidence
  - Implementation results
  - Validation outcomes
- Change records MUST be retained according to [Organization]'s retention policy (minimum 2 years recommended)
- Change records MUST be available for audit and compliance reviews

**SHOULD Requirements**:
- [Organization] SHOULD use a centralized change management system or platform
- The system SHOULD integrate with CMDB, incident management, and monitoring tools
- Change records SHOULD be searchable and reportable for trend analysis

**Technology Neutrality Note**: 
Common change management platforms include ServiceNow Change Management, Jira Service Management, BMC Remedy, Ivanti, ManageEngine, Cherwell, and Microsoft System Center Service Manager. Some organizations use custom systems or manual processes (Excel/email-based). The requirement is for CAPABILITY (recording, tracking, approval workflow), not specific technology.

---

## 2.2.7 Infrastructure as Code (IaC) and Automated Configuration Management

### 2.2.7.1 IaC Change Control Integration

**MUST Requirements**:
- Configuration changes deployed via Infrastructure as Code (IaC) MUST follow the same change control principles as manual changes
- IaC repositories MUST use version control systems (e.g., Git)
- IaC changes MUST be reviewed before merging to production branches
- Production deployments from IaC MUST be traceable to approved change requests

**SHOULD Requirements**:
- [Organization] SHOULD implement branch protection on IaC repositories
- IaC changes SHOULD undergo automated testing before approval:
  - Syntax validation
  - Security scanning (e.g., for hardcoded credentials)
  - Policy compliance checks
  - Impact analysis (what will change)
- IaC deployments SHOULD be logged and correlated with change management records

**MAY Requirements**:
- [Organization] MAY classify certain IaC deployments as Standard Changes (e.g., application scaling within defined parameters)
- IaC platforms MAY integrate directly with change management systems

---

### 2.2.7.2 Automated Change Workflows

**MUST Requirements**:
- Automated configuration changes MUST be authorized through defined approval workflows
- Automation scripts or tools MUST not bypass change control requirements
- Automated changes MUST be logged and auditable
- Failure of automated changes MUST trigger alerts and remediation procedures

**SHOULD Requirements**:
- Automated deployment tools SHOULD implement:
  - Pre-deployment validation
  - Incremental rollout (canary deployments)
  - Automatic rollback on failure
  - Post-deployment verification
- [Organization] SHOULD define which changes can be fully automated vs. requiring human approval

**MAY Requirements**:
- [Organization] MAY implement "self-service" change capabilities for authorized users (e.g., developers deploying to non-production environments)
- Automated workflows MAY include compliance and security checks as gates

---

## 2.2.8 Change Performance Metrics

**SHOULD Requirements**:
- [Organization] SHOULD track and report change management metrics including:
  - **Change success rate** - Percentage of changes completed without rollback or incidents
  - **Rollback rate** - Percentage of changes requiring rollback
  - **Emergency change rate** - Percentage of emergency changes vs. total
  - **Average approval time** - Time from request to approval
  - **Average implementation time** - Time from approval to completion
  - **CAB attendance rate** - Participation in change approval meetings
  - **Backlog** - Number of pending change requests
- Metrics SHOULD be reviewed regularly (monthly or quarterly) to identify improvement opportunities
- Poor metrics (e.g., high rollback rate) SHOULD trigger root cause analysis

**MAY Requirements**:
- [Organization] MAY establish target thresholds for key metrics
- Metrics MAY be incorporated into team performance objectives

**Sample Target Metrics** (typical industry benchmarks):
- Change Success Rate: ≥95%
- Rollback Rate: <5%
- Emergency Changes: <10% of total changes
- Average Approval Time (Normal Changes): 3-5 business days
- CAB Attendance: ≥80% of voting members

---

## 2.2.9 Integration with Related Processes

### 2.2.9.1 Incident Management Integration

**MUST Requirements**:
- Failed changes that cause incidents MUST be recorded in the incident management system
- Change records MUST be linked to related incident records
- Incident resolution that requires configuration changes MUST follow change control procedures (or be documented as Emergency Changes)

---

### 2.2.9.2 Problem Management Integration

**SHOULD Requirements**:
- Changes implemented as problem resolution SHOULD reference the problem record
- Recurring change failures SHOULD trigger problem management investigation
- Known errors identified through problem management SHOULD inform change risk assessments

---

### 2.2.9.3 Configuration Baseline Integration

**MUST Requirements**:
- Changes MUST update configuration baselines upon successful implementation
- Baseline documentation MUST reflect the current state, not an outdated ideal state
- Changes that deviate from established baselines MUST be documented and justified

---

## 2.2.10 Compliance and Audit Considerations

**MUST Requirements**:
- Change management processes MUST provide evidence for:
  - Authorization and approval of changes
  - Risk assessment and mitigation
  - Implementation procedures and results
  - Validation and testing outcomes
  - Rollback capability
- Audit trails MUST be tamper-evident or immutable
- [Organization] MUST be able to demonstrate compliance with this policy during audits

**SHOULD Requirements**:
- Change management reports SHOULD be generated for internal and external audits
- [Organization] SHOULD conduct periodic internal audits of change control compliance

---

## 2.2.11 Exceptions and Deviations

**MUST Requirements**:
- Any deviation from this policy MUST be documented and approved by the CISO or designated authority
- Emergency bypasses of normal change control MUST be documented and reviewed post-implementation
- Exceptions MUST not compromise security or regulatory compliance

**SHOULD Requirements**:
- Exception requests SHOULD include:
  - Business justification
  - Risk assessment
  - Compensating controls
  - Expiration date
- Exceptions SHOULD be reviewed periodically for continued validity

---

## 2.2.12 The Reality of Change Control

**Feynman's Final Word**: 

*"Good change control is invisible. When it works, people barely notice it—changes happen smoothly, rollbacks are rare, and incidents decrease. Bad change control is obvious—it creates bottlenecks, encourages shadow IT, and paradoxically increases risk by making people avoid the process entirely.*

*The goal is not perfect change control (impossible) but effective change control (achievable). Measure success not by how many fields your change form has, but by whether your change success rate is >95% and your engineers actually follow the process."*

---

**END OF DOCUMENT**

**Cross-References**:
- ISMS-POL-A.8.9-S1: Purpose, Scope, Definitions
- ISMS-POL-A.8.9-S2: Requirements Overview
- ISMS-POL-A.8.9-S2.1: Baseline Configuration Requirements
- ISMS-POL-A.8.9-S2.3: Configuration Monitoring Requirements (next)
- ISMS-POL-A.8.9-S5.B: Change Request Form Template
- ISMS-IMP-A.8.9.2: Change Control Assessment Specification

---