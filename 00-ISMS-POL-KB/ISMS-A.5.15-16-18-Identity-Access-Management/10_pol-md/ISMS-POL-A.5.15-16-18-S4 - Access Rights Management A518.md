# ISMS Policy Section 4: Access Rights Management Requirements (A.5.18)

**Document ID**: ISMS-POL-A.5.15-16-18-S4  
**Title**: Access Rights Management Requirements (ISO 27001:2022 Control A.5.18)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Part of**: ISMS-POL-A.5.15-16-18 Identity & Access Management Framework

---

## Table of Contents

1. [Control Objective & Scope](#1-control-objective--scope)
2. [Access Rights Assignment Requirements](#2-access-rights-assignment-requirements)
3. [Role-Based Access Control (RBAC) Framework](#3-role-based-access-control-rbac-framework)
4. [Group Membership Management](#4-group-membership-management)
5. [Access Review & Recertification](#5-access-review--recertification)
6. [Access Removal Requirements](#6-access-removal-requirements)
7. [Privilege Creep Detection](#7-privilege-creep-detection)
8. [Emergency Access Procedures](#8-emergency-access-procedures)
9. [Access Rights Documentation](#9-access-rights-documentation)
10. [Audit & Evidence Requirements](#10-audit--evidence-requirements)

---

## 1. Control Objective & Scope

### 1.1 ISO 27001:2022 Control A.5.18 Text

**Original (German)**:
> *Zugangsrechte zu Informationen und anderen damit verbundenen Werten müssen in Übereinstimmung mit der themenspezifischen Richtlinie und den Regeln der Organisation für die Zugangssteuerung bereitgestellt, überprüft, geändert und entfernt werden.*

**English Translation**:
> *Access rights to information and other associated assets shall be provisioned, reviewed, modified and removed in accordance with the organization's topic-specific policy and rules for access control.*

### 1.2 Control Purpose

**Why A.5.18 Matters**:

Access rights management is the **operational enforcement layer** of access control governance:
- **Without A.5.18**: Users accumulate excessive rights over time (privilege creep), orphaned access remains after role changes, no systematic verification that access aligns with business need
- **With A.5.18**: Access rights are systematically assigned, periodically reviewed, promptly removed when no longer needed, and continuously aligned with the principle of least privilege

**Key Risk Mitigations**:
- **Unauthorized access**: Users have only the access they need for their current role
- **Privilege creep**: Periodic reviews detect and remove accumulated excess rights
- **Orphaned access**: Access removed promptly when users leave or change roles
- **Compliance violations**: Systematic access review provides audit evidence
- **Insider threats**: Segregation of duties violations detected and remediated

### 1.3 Scope of A.5.18 Requirements

**Access Rights Management applies to**:
- **All user types**: Employees, contractors, vendors, partners, service accounts
- **All access types**: Application access, system access, data access, administrative privileges
- **All environments**: On-premises systems, cloud services (SaaS, IaaS, PaaS), hybrid environments
- **All access grant mechanisms**: Direct user access, role-based access, group membership, privileged access

**Integration with other controls**:
- **A.5.15 (Access Control)**: Defines the policy framework that A.5.18 enforces
- **A.5.16 (Identity Management)**: Manages user identities that A.5.18 grants rights to
- **A.8.2 (Privileged Access Rights)**: Governs privileged access as a special case of A.5.18
- **A.8.5 (Secure Authentication)**: Authenticates users whose rights are managed by A.5.18

### 1.4 Access Rights Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│              ACCESS RIGHTS LIFECYCLE (A.5.18)               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. REQUEST                                                 │
│     User/Manager submits access request                     │
│     Business justification documented                       │
│                                                             │
│  2. APPROVAL                                                │
│     Manager approves (business need)                        │
│     System owner approves (if sensitive)                    │
│     Security validates (policy compliance)                  │
│                                                             │
│  3. PROVISIONING                                            │
│     IT operations grants access                             │
│     Access documented (who, what, when, why)                │
│     User notified                                           │
│                                                             │
│  4. REVIEW (Periodic)                                       │
│     Manager/owner reviews access                            │
│     Access confirmed OR removed                             │
│     Justification documented                                │
│                                                             │
│  5. MODIFICATION                                            │
│     Role change triggers access review                      │
│     Excess access removed                                   │
│     New access granted (if needed)                          │
│                                                             │
│  6. REMOVAL                                                 │
│     Termination → Immediate removal                         │
│     No longer needed → Prompt removal                       │
│     Removal verified (audit log)                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Critical Principle**: Access rights have a lifecycle - they are **granted for a reason, reviewed periodically, and removed when no longer needed**.

---

## 2. Access Rights Assignment Requirements

### 2.1 Access Request & Approval Workflow

**REQ-A518-001: Access Request Submission**
- **Requirement**: All access requests submitted via formal request process
- **Mechanism**: Ticketing system (ServiceNow, Jira, access management platform)
- **Requestor Responsibilities**:
  - Specify exactly what access is needed (system, application, data, access level)
  - Provide business justification (why access is needed for job function)
  - Identify urgency (standard, expedited, emergency)
- **Documentation**: Request ticket captures all details
- **Audit Trail**: All requests logged and traceable

**REQ-A518-002: Business Justification Requirement**
- **Requirement**: Every access request requires documented business justification
- **Justification Elements**:
  - Job function requiring access (e.g., "Financial analyst needs read access to ERP for budget reporting")
  - Business process supported (e.g., "Monthly financial close process")
  - Duration of need (permanent for role, temporary for project)
  - Data sensitivity consideration (awareness of accessing confidential/restricted data)
- **Quality Standard**: Generic justifications rejected (e.g., "Need access to do my job" is insufficient)
- **Review**: Approver validates justification adequacy

**REQ-A518-003: Multi-Level Approval Workflow**
- **Requirement**: Approval chain based on access sensitivity and criticality
- **Approval Levels**:
  - **Level 1 - Manager Approval**: All access requests require manager approval (verifies business need)
  - **Level 2 - System Owner Approval**: High-sensitivity systems require system owner approval
  - **Level 3 - Security Approval**: Privileged access or restricted data requires security team approval
  - **Level 4 - Executive Approval**: Critical systems may require executive approval (CISO, CIO)
- **Parallel vs. Sequential**: Standard access = sequential, emergency access = parallel with post-approval review
- **Approval Documentation**: Each approver documents their decision (approve, reject, request more information)

**REQ-A518-004: Access Provisioning Execution**
- **Requirement**: Access provisioned only after all required approvals obtained
- **Provisioning Responsibilities**: IT operations or system administrators execute provisioning
- **Provisioning Actions**:
  - Grant access in target system (application, directory, database)
  - Assign user to appropriate groups/roles
  - Document provisioning completion (date, who provisioned)
  - Test access (verify user can successfully access)
- **User Notification**: User notified when access is ready (instructions, limitations, usage policy)

**REQ-A518-005: Provisioning Service Level Agreements (SLAs)**
- **Requirement**: Access provisioned within defined timeframes
- **Standard Access SLA**:
  - Low-criticality systems: Within 2 business days
  - Standard systems: Within 1 business day
  - High-criticality systems: Within 4 business hours (same day)
- **Expedited Access SLA**: Within 2 hours (requires additional approval justification)
- **Emergency Access SLA**: Same day (see Section 8 for emergency procedures)
- **SLA Measurement**: Time from final approval to provisioning completion
- **Escalation**: SLA breaches escalated to IT management

**REQ-A518-006: Access Request Documentation**
- **Requirement**: Complete documentation of access grant lifecycle
- **Mandatory Documentation**:
  - Who requested access (requestor name, user ID)
  - What access requested (system, access level, specific permissions)
  - When requested (request date/time)
  - Why access needed (business justification)
  - Who approved (manager, system owner, security - with approval dates)
  - When provisioned (provisioning completion date)
  - Who provisioned (IT operations staff member)
- **Retention**: Access request records retained for 3 years (audit evidence)
- **Accessibility**: Records accessible for audit review and access recertification

### 2.2 Access Level Classification

**REQ-A518-010: Standardized Access Levels**
- **Requirement**: Access levels standardized across [Organization] systems
- **Standard Access Levels**:
  - **Read**: View-only access (query data, generate reports)
  - **Write**: Create/modify data (add records, update fields)
  - **Admin**: System administration (manage users, configure system)
  - **Owner**: Full control (admin + ability to grant access to others)
- **Application-Specific Levels**: Applications may define additional levels (e.g., "Approver", "Auditor") aligned with standard levels
- **Documentation**: Each system's access levels documented in system access matrix

**REQ-A518-011: Least Privilege Enforcement**
- **Requirement**: Access granted at minimum level required for job function
- **Implementation**:
  - Default to Read access unless Write is justified
  - Default to Write access unless Admin is justified
  - Admin access requires specific business justification and elevated approval
- **Periodic Validation**: Access reviews verify least privilege is maintained
- **Exception Process**: Requests for elevated access beyond role norm require exception approval

**REQ-A518-012: Time-Bounded Access**
- **Requirement**: Temporary access automatically expires
- **Applicability**:
  - Project-based access (expires on project completion date)
  - Contractor access (expires on contract end date)
  - Temporary delegation (expires after specified duration)
- **Implementation**: Access provisioning system supports expiration dates
- **Extension Process**: Access extension requires new approval (not automatic)
- **Notification**: User and manager notified 7 days before expiration

---

## 3. Role-Based Access Control (RBAC) Framework

### 3.1 Role Definition Requirements

**REQ-A518-020: Role Catalog Maintenance**
- **Requirement**: [Organization] maintains a catalog of standard roles
- **Role Catalog Contents**:
  - Role name (e.g., "Financial Analyst", "HR Administrator", "Developer")
  - Role description (job function, responsibilities)
  - Role owner (person responsible for role definition accuracy)
  - Systems/applications included in role
  - Access level per system (read, write, admin)
  - Last review date
- **Catalog Format**: Centralized repository (spreadsheet, access management platform, wiki)
- **Accessibility**: Role catalog accessible to managers and users for reference

**REQ-A518-021: Role-to-Access Mapping**
- **Requirement**: Each role has documented access mapping
- **Mapping Structure**:
  ```
  Role: Financial Analyst
    ├── ERP System: Read access (view financial data)
    ├── Reporting Tool: Write access (create custom reports)
    ├── Budget Database: Read access (view budget allocations)
    └── Shared Drives: Read access (finance folder only)
  ```
- **Granularity**: Mapping specifies exact systems, applications, folders, databases
- **Access Level**: Mapping specifies access level (read, write, admin) per system
- **Justification**: Mapping includes rationale (why this role needs this access)

**REQ-A518-022: Role Ownership Assignment**
- **Requirement**: Every role has an assigned owner
- **Owner Responsibilities**:
  - Define role access requirements (what access the role needs)
  - Review role accuracy annually (update as job functions change)
  - Approve user assignments to role (verify user's job function matches role)
  - Participate in access reviews (confirm assigned users still need role)
- **Owner Qualifications**: Typically manager of users in that role or subject matter expert

**REQ-A518-023: Role Hierarchy (If Applicable)**
- **Requirement**: If role hierarchy used, relationships documented
- **Hierarchy Types**:
  - **Parent-Child Roles**: Child role inherits parent role permissions (e.g., "Senior Analyst" inherits "Analyst" + additional access)
  - **Organizational Hierarchy**: Manager role includes direct report access (e.g., "Finance Manager" includes "Financial Analyst" + additional access)
- **Documentation**: Hierarchy relationships explicitly documented (avoid implicit assumptions)
- **Review**: Hierarchy reviewed annually (ensure inheritance still appropriate)

### 3.2 Role Assignment Procedures

**REQ-A518-030: Role-Based Access Assignment**
- **Requirement**: Users assigned to roles rather than direct access (where possible)
- **Benefits**:
  - Consistency: All users in same role have same access
  - Efficiency: Assign role instead of individual permissions
  - Maintainability: Update role definition once, affects all users
  - Auditability: Easier to verify appropriate access
- **Implementation Priority**:
  - High: Roles for common job functions (majority of users)
  - Medium: Roles for specialized functions (fewer users)
  - Low: Direct access for unique one-off cases (minimal users)

**REQ-A518-031: Role Assignment Approval**
- **Requirement**: Role assignments require approval
- **Approval Process**:
  - User's manager approves role assignment (verifies job function alignment)
  - Role owner approves assignment (if different from manager)
  - Documentation: Approval captured in access request system
- **Bulk Assignments**: New hires in same role can use template with manager approval

**REQ-A518-032: Role Assignment Documentation**
- **Requirement**: All role assignments documented
- **Documentation Elements**:
  - User assigned to role
  - Role name
  - Assignment date
  - Approver (manager or role owner)
  - Effective date (when role becomes active)
  - Expiration date (for time-bounded roles, e.g., contractors)

**REQ-A518-033: Multiple Role Assignments**
- **Requirement**: Users may be assigned to multiple roles
- **Use Cases**:
  - User has multiple job functions (e.g., "Developer" + "Team Lead")
  - Temporary additional responsibilities (e.g., "Analyst" + "Project Manager" for specific project)
- **Segregation of Duties (SoD) Check**: Multiple role assignments checked for SoD violations (see REQ-A518-040)
- **Review**: Users with multiple roles reviewed more frequently (increased risk)

### 3.3 RBAC Maturity & Adoption

**REQ-A518-040: RBAC Adoption Target**
- **Requirement**: [Organization] targets high RBAC adoption rate
- **Target Metrics**:
  - **Initial Target**: ≥60% of users assigned to standard roles (vs. direct access only)
  - **Mature Target**: ≥80% of users assigned to standard roles
  - **Optimized Target**: ≥90% of users assigned to standard roles
- **Measurement**: RBAC adoption rate = (Users with roles / Total users) × 100
- **Exclusions**: Service accounts, emergency accounts excluded from adoption calculation

**REQ-A518-041: Direct Access Justification**
- **Requirement**: Direct access (not via role) requires justification
- **Valid Justifications**:
  - Unique job function (no standard role exists)
  - Temporary access (project-specific, time-bounded)
  - System limitations (system does not support role-based access)
- **Approval**: Direct access requires elevated approval (security team)
- **Review**: Direct access users reviewed more frequently (quarterly vs. annual)

**REQ-A518-042: Role Review & Maintenance**
- **Requirement**: Roles reviewed annually for accuracy
- **Review Process**:
  - Role owner reviews role definition (access still appropriate for job function?)
  - Role owner reviews assigned users (users still need this role?)
  - Access mapping updated (add/remove systems as job function evolves)
  - Obsolete roles deactivated (no longer needed)
- **Documentation**: Role review completion documented with sign-off

---

## 4. Group Membership Management

### 4.1 Group Management Requirements

**REQ-A518-050: Group Purpose Documentation**
- **Requirement**: Every group has documented purpose
- **Documentation Elements**:
  - Group name (naming convention: function-system-access, e.g., "Finance-ERP-Read")
  - Group description (what access the group grants)
  - Business purpose (why group exists)
  - Systems/applications affected (where group is used)
- **Documentation Location**: Centralized group directory (Active Directory description field, access management platform, wiki)

**REQ-A518-051: Group Ownership Assignment**
- **Requirement**: Every group has assigned owner
- **Owner Responsibilities**:
  - Approve membership additions (verify user needs group access)
  - Approve membership removals (process offboarding requests)
  - Review group membership periodically (confirm current members still need access)
  - Maintain group documentation (update purpose/description as needed)
- **Owner Identification**: Group owner documented in directory service or access management system
- **Ownership Review**: Group ownership reviewed annually (ensure owner is still appropriate)

**REQ-A518-052: Group Membership Approval**
- **Requirement**: Group membership changes require approval
- **Add Member**:
  - Requestor submits access request (include business justification)
  - Group owner approves addition
  - IT provisions membership
  - Documentation: Approval captured in access request system
- **Remove Member**:
  - Manager or group owner requests removal
  - IT executes removal
  - Documentation: Removal logged in audit trail
- **Bulk Changes**: Mass adds/removes require elevated approval (security team)

**REQ-A518-053: Nested Group Management**
- **Requirement**: Nested groups (groups within groups) managed carefully
- **Use Cases**:
  - Organizational hierarchy (Department group contains team groups)
  - Role inheritance (Manager group contains employee group + additional access)
- **Documentation**: Nested relationships explicitly documented (group hierarchy map)
- **Complexity Limit**: Maximum 3 levels of nesting (avoid overly complex hierarchies)
- **Review**: Nested groups reviewed semi-annually (ensure hierarchy still makes sense)

### 4.2 Group Types & Standards

**REQ-A518-060: Group Type Classification**
- **Requirement**: Groups classified by type and purpose
- **Group Types**:
  - **Role Groups**: Map to standard roles (e.g., "Role-FinancialAnalyst")
  - **Access Groups**: Grant access to specific systems (e.g., "ERP-ReadOnly-Users")
  - **Distribution Groups**: Email distribution only (not access control)
  - **Administrative Groups**: System administration (e.g., "Domain Admins" - highly restricted)
- **Naming Convention**: Group type prefix in name for clarity

**REQ-A518-061: Privileged Group Management**
- **Requirement**: Groups granting privileged access managed with elevated controls
- **Privileged Groups**: Domain Admins, System Administrators, Database Admins, Security Groups
- **Additional Controls**:
  - Membership changes require CISO or IT Director approval
  - Membership reviewed quarterly (vs. annual for standard groups)
  - Membership minimized (only users truly needing privileged access)
  - Audit logging for all privileged group changes
  - Justification required for membership (documented business need)

**REQ-A518-062: Group Lifecycle Management**
- **Requirement**: Groups have lifecycle (creation, active use, deactivation, deletion)
- **Creation**: New group creation requires business justification and approval
- **Active Use**: Group actively used (has members, grants access to active systems)
- **Deactivation**: Group no longer needed → membership removed, group disabled
- **Deletion**: Disabled groups deleted after 90 days (if no retention requirement)
- **Orphaned Groups**: Groups with no owner or no members flagged for review (quarterly)

---

## 5. Access Review & Recertification

### 5.1 Access Review Frequency

**REQ-A518-070: Risk-Based Review Frequency**
- **Requirement**: Access review frequency based on system criticality and data sensitivity
- **Review Frequency Matrix**:

| System Criticality | Data Sensitivity | Review Frequency |
|-------------------|------------------|------------------|
| Critical          | Restricted       | Quarterly        |
| Critical          | Confidential     | Semi-Annual      |
| High              | Restricted       | Semi-Annual      |
| High              | Confidential     | Annual           |
| Medium            | Confidential     | Annual           |
| Medium/Low        | Internal/Public  | Biennial         |

- **Rationale**: Higher risk systems reviewed more frequently
- **Privileged Access**: All privileged access reviewed quarterly (regardless of system)
- **Contractor Access**: All contractor access reviewed quarterly (time-bounded nature)

**REQ-A518-071: Comprehensive Review Scope**
- **Requirement**: Access reviews cover all users and all access
- **Review Scope**:
  - **All Users**: Employees, contractors, vendors, service accounts
  - **All Systems**: Applications, databases, file shares, cloud services
  - **All Access Types**: Direct user access, role assignments, group memberships, privileged access
- **No Exclusions**: Even "low-risk" access reviewed (at lower frequency)

**REQ-A518-072: Event-Triggered Reviews**
- **Requirement**: Certain events trigger immediate access review
- **Review Triggers**:
  - **Role Change**: User changes job function → review all access within 5 business days
  - **Department Transfer**: User moves to different department → review access within 5 business days
  - **Manager Change**: New manager reviews direct reports' access within 30 days
  - **System Criticality Change**: System upgraded to higher criticality → immediate review of all access
  - **Security Incident**: Compromised account → immediate review of affected user(s) and similar access patterns

### 5.2 Access Review Execution

**REQ-A518-080: Reviewer Accountability**
- **Requirement**: Access reviews assigned to specific accountable individuals
- **Reviewer Assignments**:
  - **Manager Reviews**: Manager reviews access for their direct reports
  - **System Owner Reviews**: System owner reviews all access to their system
  - **Security Reviews**: Security team reviews all privileged access
  - **Role Owner Reviews**: Role owner reviews all assignments to their role
- **Reviewer Responsibilities**:
  - Review access data (who has access, what level, why)
  - Determine appropriateness (does user still need this access for job function?)
  - Take action (confirm access OR request removal)
  - Document decision (justification for retention or removal)
  - Complete review by deadline (avoid overdue reviews)

**REQ-A518-081: Review Data Preparation**
- **Requirement**: Access review data prepared for reviewers
- **Data Preparation Activities**:
  - Extract current access data (from systems, directories, applications)
  - Consolidate into reviewable format (spreadsheet, access management platform)
  - Include context (user's current role, department, manager)
  - Include historical data (when access granted, by whom, original justification)
  - Pre-flag anomalies (users with excessive access, orphaned accounts, SoD violations)
- **Data Accuracy**: Review data verified accurate before sending to reviewers (spot checks)

**REQ-A518-082: Review Tool/Platform**
- **Requirement**: Access reviews conducted via formal tool or platform
- **Acceptable Tools**:
  - Access governance platform (SailPoint, Saviynt, CyberArk Identity)
  - GRC platform (ServiceNow GRC, RSA Archer)
  - Structured spreadsheets (for smaller organizations)
- **Tool Requirements**:
  - Present access data to reviewers
  - Capture reviewer decisions (approve, remove, justify)
  - Track review completion (% complete, overdue reviews)
  - Generate reports (findings, removals, completion status)
  - Maintain audit trail (who reviewed, when, what decision)

**REQ-A518-083: Reviewer Training**
- **Requirement**: Reviewers trained on access review process
- **Training Topics**:
  - What is access review and why it matters (business and compliance need)
  - Reviewer responsibilities (accountability for decisions)
  - How to use review tool/platform (navigation, decision recording)
  - Decision criteria (least privilege, need-to-know, business justification)
  - Handling exceptions (when access seems excessive but is justified)
  - Escalation process (questions, concerns, disputed access)
- **Training Frequency**: Annual training for all reviewers

**REQ-A518-084: Review Completion Tracking**
- **Requirement**: Access review completion monitored and tracked
- **Tracking Metrics**:
  - Reviews assigned (count)
  - Reviews completed (count)
  - Reviews in progress (count)
  - Reviews overdue (count, aging in days)
  - Completion rate (%) = (Completed / Assigned) × 100
- **Target**: ≥95% completion rate within review period
- **Escalation**: Overdue reviews escalated at 7 days, 14 days, 30 days

### 5.3 Review Findings & Remediation

**REQ-A518-090: Review Findings Documentation**
- **Requirement**: Access review findings documented
- **Finding Types**:
  - **Access Confirmed**: User still needs access, retained with documentation
  - **Access Removed**: User no longer needs access, removal requested
  - **Access Justified**: Access seems excessive but justified by business exception (documented)
  - **Further Investigation**: Access questionable, requires additional review before decision
- **Documentation Elements**:
  - Finding type (confirmed, removed, justified, investigate)
  - Reviewer decision (who made decision, when)
  - Justification (rationale for decision)
  - Action taken (access retained, removal ticket created)

**REQ-A518-091: Access Removal Execution**
- **Requirement**: Access removal findings executed promptly
- **Removal Process**:
  - Review finding generates removal ticket (automated or manual)
  - IT operations executes removal within 3 business days
  - Removal verified (access actually removed, user cannot access)
  - User notified (access removed, reason, contact for questions)
  - Documentation: Removal completion logged in audit trail
- **Verification**: Sample of removals verified monthly (spot checks)

**REQ-A518-092: Access Justification Documentation**
- **Requirement**: Justified exceptions documented thoroughly
- **Justification Requirements**:
  - Business need (why user requires access beyond typical role)
  - Risk acknowledgment (awareness that access is elevated)
  - Compensating controls (if applicable - additional monitoring, approval requirements)
  - Review frequency (justified exceptions reviewed more frequently)
  - Approver (exception approval by manager, system owner, or CISO)
- **Retention**: Justification documentation retained with access record

**REQ-A518-093: Unresponsive Reviewer Escalation**
- **Requirement**: Unresponsive reviewers escalated systematically
- **Escalation Path**:
  - **Day 7 Past Due**: Reminder notification to reviewer
  - **Day 14 Past Due**: Escalation to reviewer's manager
  - **Day 30 Past Due**: Escalation to CISO or IT Director
  - **Day 45 Past Due**: Default action (access flagged for removal unless urgent business need documented)
- **Accountability**: Persistent non-completion may affect performance reviews

**REQ-A518-094: Review Metrics & Reporting**
- **Requirement**: Access review metrics reported to management
- **Key Metrics**:
  - Review completion rate (%) by reviewer, by system, overall
  - Access removal rate (% of access removed as inappropriate)
  - Average time to complete review (days)
  - Overdue reviews (count, aging)
  - Reviewer responsiveness (% completing on time)
  - Findings summary (confirmed vs. removed vs. justified)
- **Reporting Frequency**: Monthly during review periods, quarterly summary to CISO

---

## 6. Access Removal Requirements

### 6.1 Access Removal Triggers

**REQ-A518-100: Termination-Triggered Removal**
- **Requirement**: Access removed immediately upon termination
- **Trigger**: HR system termination event (employee terminated, contractor contract ends)
- **Removal Timeline**:
  - **Involuntary termination**: Within 1 hour of HR notification
  - **Voluntary resignation**: End of last working day
  - **Contractor contract end**: Contract end date (automated if possible)
- **Scope**: ALL access removed (applications, systems, directories, physical access, remote access)
- **Verification**: Removal verified within 24 hours (account disabled test)

**REQ-A518-101: Role Change Triggered Removal**
- **Requirement**: Excess access removed when user changes roles
- **Trigger**: HR system role change event (job title change, department transfer)
- **Process**:
  - Identify user's previous role access (what they had)
  - Identify user's new role access (what they need)
  - Calculate difference (excess access = old access - new access)
  - Remove excess access within 1 business day
  - Grant new required access (if not already present)
- **Manager Notification**: Manager notified of role change access adjustment

**REQ-A518-102: No-Longer-Needed Removal**
- **Requirement**: Access removed when no longer needed for job function
- **Triggers**:
  - Access review finding (reviewer confirms access no longer needed)
  - User request (user proactively requests removal)
  - Manager request (manager identifies unnecessary access)
  - Project completion (project-based access no longer needed)
- **Removal Timeline**: Within 3 business days of removal decision

**REQ-A518-103: Leave of Absence Handling**
- **Requirement**: Access handled appropriately during leave of absence
- **Leave Types**:
  - **Short-term leave** (<30 days): Access retained but monitored (unused access flagged)
  - **Long-term leave** (30-90 days): Access disabled, re-enabled on return
  - **Extended leave** (>90 days): Access disabled, requires re-approval on return
- **Return Process**: Manager confirms user's return, access re-enabled (if appropriate)

### 6.2 Access Removal Execution

**REQ-A518-110: Removal Verification Procedures**
- **Requirement**: Access removal verified to ensure completion
- **Verification Methods**:
  - **Technical Verification**: Attempt login with disabled account (should fail)
  - **Audit Log Verification**: Confirm account disabled in audit logs
  - **Access Matrix Verification**: User removed from access rights matrix
  - **Group Membership Verification**: User removed from all groups
- **Verification Timeline**: Within 24 hours of removal execution
- **Escalation**: Removal failures escalated immediately (security risk)

**REQ-A518-111: Removal Audit Trail**
- **Requirement**: Access removals fully logged and auditable
- **Audit Trail Elements**:
  - User whose access was removed (user ID, name)
  - What access was removed (system, application, access level)
  - When removed (date and time)
  - Who removed (IT operations staff member)
  - Why removed (termination, role change, access review finding, etc.)
  - Verification status (removal verified successfully)
- **Retention**: Removal logs retained for 3 years

**REQ-A518-112: User Notification**
- **Requirement**: Users notified when access is removed (where appropriate)
- **Notification Scenarios**:
  - **Access review removal**: User notified (reason, contact for questions)
  - **Role change removal**: User notified (excess access removed, new access granted)
  - **Termination**: No notification (security consideration)
- **Notification Content**: What access removed, why, effective date, contact for appeals

### 6.3 Temporary Access Removal

**REQ-A518-120: Time-Bounded Access Expiration**
- **Requirement**: Temporary access automatically expires
- **Implementation**:
  - Expiration date set during provisioning (project end date, contract end date)
  - Automated expiration (system disables access on expiration date)
  - Notification: User and manager notified 7 days before expiration
- **Extension Process**: Access extension requires new approval (not automatic renewal)

**REQ-A518-121: Inactive Access Removal**
- **Requirement**: Access removed if not used within defined period
- **Inactive Access Definition**: No login/usage in 90 days
- **Process**:
  - Monthly scan for inactive access (users who haven't logged in)
  - Manager notified (confirm if access still needed)
  - If not needed: Access removed
  - If still needed: Documented justification (may indicate privilege creep)
- **Exclusions**: Service accounts, emergency accounts (different inactivity criteria)

---

## 7. Privilege Creep Detection

### 7.1 Privilege Creep Definition & Risk

**REQ-A518-130: Privilege Creep Definition**
- **Definition**: User accumulates excess access rights over time beyond current role requirements
- **Common Causes**:
  - Role changes (user moves to new role but retains old role access)
  - Project access (temporary access granted but not removed after project)
  - Access reviews not conducted (no systematic verification)
  - "Nice to have" access (user requests access "just in case" not for current need)
- **Risk**: Violates least privilege principle, increases attack surface, complicates compliance

### 7.2 Privilege Creep Detection Methodology

**REQ-A518-140: Current vs. Required Access Comparison**
- **Requirement**: Systematically compare user's current access to required access
- **Detection Process**:
  1. Identify user's current role (from HR system)
  2. Identify required access for role (from role catalog)
  3. Identify user's current access (from access rights matrix)
  4. Calculate difference: Excess Access = Current Access - Required Access
  5. Flag users with excess access (privilege creep candidates)
- **Automation**: Automated comparison (monthly) via script or access management platform
- **Threshold**: Users with >20% excess access flagged for immediate review

**REQ-A518-141: Historical Access Analysis**
- **Requirement**: Analyze user's access history for accumulation patterns
- **Analysis Approach**:
  - Compare access 6 months ago vs. today (did access increase without role change?)
  - Identify access grants without corresponding role change (ad-hoc access)
  - Flag users whose access consistently increases (accumulation pattern)
- **Risk Indicator**: Access growth without job function change suggests privilege creep

**REQ-A518-142: Peer Comparison Analysis**
- **Requirement**: Compare user's access to peers in same role
- **Comparison Approach**:
  - Identify users in same role (e.g., all "Financial Analysts")
  - Calculate median access for role (typical access level)
  - Identify outliers (users with significantly more access than peers)
- **Flagging Criteria**: User has >30% more access than role median = flagged for review

### 7.3 Privilege Creep Remediation

**REQ-A518-150: Manager Review of Excess Access**
- **Requirement**: Managers review and confirm excess access
- **Review Process**:
  - User's manager presented with excess access report (user has X access but role requires only Y)
  - Manager confirms: (a) Access still needed for job function, OR (b) Access no longer needed
  - If still needed: Documented justification (why user needs more than standard role)
  - If not needed: Access removal requested
- **Timeline**: Manager review within 10 business days of privilege creep detection

**REQ-A518-151: Excess Access Removal**
- **Requirement**: Confirmed excess access removed promptly
- **Removal Process**:
  - Manager confirms access no longer needed
  - Removal ticket created (automated from review finding)
  - IT executes removal within 3 business days
  - Verification: Removal verified via audit log
- **User Notification**: User notified of excess access removal (reason: access no longer aligned with role)

**REQ-A518-152: Exception Documentation for Retained Excess Access**
- **Requirement**: Retained excess access (manager confirms still needed) documented as exception
- **Exception Documentation**:
  - Business justification (why user needs access beyond standard role)
  - Approver (manager or CISO for significant exceptions)
  - Review frequency (exceptions reviewed quarterly vs. annual)
  - Risk acknowledgment (awareness of elevated access risk)
  - Expiration date (if time-bounded exception)

**REQ-A518-153: Privilege Creep Metrics & Reporting**
- **Requirement**: Privilege creep metrics tracked and reported
- **Key Metrics**:
  - Privilege creep detection rate (% users with excess access)
  - Average excess access (% above required role access)
  - Remediation rate (% excess access removed vs. justified)
  - Repeat offenders (users flagged multiple times)
- **Reporting**: Quarterly privilege creep report to CISO (trends, high-risk users)

---

## 8. Emergency Access Procedures

### 8.1 Emergency Access Definition & Use Cases

**REQ-A518-160: Emergency Access Definition**
- **Definition**: Access granted outside standard process to address urgent business or security need
- **Valid Use Cases**:
  - **System outage**: Production system down, immediate access needed for recovery
  - **Security incident**: Security breach, immediate access needed for investigation/remediation
  - **Business continuity**: Critical business process at risk without immediate access
  - **After-hours emergency**: Standard approvers unavailable, immediate access required
- **Invalid Use Cases**: Poor planning (forgot to request in advance), convenience (don't want to wait for approval)

### 8.2 Emergency Access Mechanisms

**REQ-A518-170: Break-Glass Account Management**
- **Requirement**: Emergency accounts ("break-glass") available for urgent access
- **Break-Glass Account Characteristics**:
  - Highly privileged (admin-level access to critical systems)
  - Stored securely (password vault, physical safe)
  - Access restricted (only CISO, IT Director, designated emergency contacts)
  - Monitored closely (all usage logged and reviewed)
- **Account Types**:
  - System break-glass (Windows Domain Admin, Linux root)
  - Application break-glass (application admin accounts)
  - Database break-glass (database DBA accounts)
- **Password Management**: Passwords rotated after each use

**REQ-A518-171: Emergency Access Request Process**
- **Requirement**: Emergency access granted via expedited process
- **Expedited Process**:
  1. User contacts IT helpdesk or on-call team (phone, emergency ticket)
  2. User provides emergency justification (what happened, why immediate access needed)
  3. On-call approver validates emergency (is this truly urgent?)
  4. IT provisions access immediately (via break-glass or elevated privileges)
  5. Access usage logged (all actions recorded)
  6. Post-access review within 24 hours (was emergency access appropriate? what was done?)
- **Parallel Approval**: Standard approvers notified simultaneously (after-the-fact awareness)

**REQ-A518-172: Emergency Access Approval Authority**
- **Requirement**: Emergency access approval authority defined
- **Approval Authority** (in order of preference):
  - **Tier 1**: CISO or IT Director (primary emergency approvers)
  - **Tier 2**: Security Manager or IT Operations Manager (if Tier 1 unavailable)
  - **Tier 3**: On-call senior engineer (if Tier 1-2 unavailable, with post-approval review)
- **After-Hours**: On-call rotation documented (who to contact for emergency access approval)

### 8.3 Emergency Access Monitoring & Review

**REQ-A518-180: Emergency Access Logging**
- **Requirement**: All emergency access usage comprehensively logged
- **Logging Requirements**:
  - Who used emergency access (user ID, name)
  - What emergency account was used (break-glass account name)
  - When used (start time, end time)
  - What actions taken (commands executed, systems accessed, data viewed/modified)
  - Why emergency access granted (emergency justification)
- **Log Protection**: Emergency access logs immutable (cannot be altered by users)

**REQ-A518-181: Post-Emergency Review**
- **Requirement**: Emergency access usage reviewed within 24 hours
- **Review Process**:
  - Security team reviews emergency access logs
  - Verify: Was emergency legitimate? (or misuse of emergency process?)
  - Verify: Were actions appropriate? (or excessive/unauthorized actions?)
  - Document: Review findings (appropriate use vs. policy violation)
  - Escalate: Policy violations escalated to CISO (disciplinary action)
- **Review Documentation**: Post-emergency review report retained for audit

**REQ-A518-182: Emergency Access Revocation**
- **Requirement**: Emergency access revoked immediately after emergency resolved
- **Revocation Process**:
  - User confirms emergency resolved (issue addressed)
  - IT revokes emergency access (elevated privileges removed)
  - Break-glass password rotated (if break-glass account was used)
  - Verification: User can no longer access with emergency credentials
- **Timeline**: Emergency access revocation within 1 hour of emergency resolution

**REQ-A518-183: Emergency Access Metrics**
- **Requirement**: Emergency access usage tracked and analyzed
- **Key Metrics**:
  - Emergency access requests (count per month)
  - Emergency access approvals vs. rejections (were emergencies legitimate?)
  - Average emergency access duration (how long was emergency access active?)
  - Repeat users (users frequently requesting emergency access - red flag)
- **Analysis**: Frequent emergency access may indicate process gaps (inadequate standard access process)

---

## 9. Access Rights Documentation

### 9.1 Access Rights Matrix

**REQ-A518-190: Comprehensive Access Rights Matrix**
- **Requirement**: [Organization] maintains comprehensive access rights matrix
- **Matrix Structure**: User → System → Access Level mapping
- **Matrix Contents**:
  - User ID, User Name, User Type (employee, contractor, etc.)
  - System/Application Name
  - Access Level (read, write, admin)
  - Granted Date (when access was granted)
  - Granted By (who provisioned access)
  - Business Justification (why access was granted)
  - Last Review Date (when access was last reviewed)
  - Expiration Date (for time-bounded access)
  - Status (active, disabled, removed)
- **Maintenance**: Matrix updated continuously (real-time or daily sync with identity systems)
- **Accessibility**: Matrix accessible to security team, auditors, system owners

**REQ-A518-191: Access Rights Matrix Updates**
- **Requirement**: Access matrix updated for all access changes
- **Update Triggers**:
  - Access granted (new row added)
  - Access removed (row marked removed or deleted)
  - Access modified (access level changed)
  - Role assignment (all role access rows added)
  - Group membership change (all group access rows added/removed)
- **Automation**: Access matrix updates automated via identity system integration

**REQ-A518-192: Access Rights Matrix Exports**
- **Requirement**: Access matrix exported for review and audit
- **Export Frequency**:
  - Monthly: For access review preparation
  - Quarterly: For access governance reporting
  - On-demand: For audit requests
- **Export Format**: Excel, CSV, or access governance platform reports

### 9.2 Business Justification Documentation

**REQ-A518-200: Justification Recording**
- **Requirement**: Business justification recorded for all access grants
- **Justification Elements**:
  - Why access is needed (job function, business process)
  - How access will be used (specific use cases)
  - Duration of need (permanent for role, temporary for project)
  - Data sensitivity awareness (user acknowledges accessing confidential/restricted data)
- **Capture Method**: Access request ticket (justification field required)
- **Retention**: Justification retained with access record (linked in access matrix)

**REQ-A518-201: Approval Documentation**
- **Requirement**: All access approvals documented
- **Approval Record Elements**:
  - Approver name and role (manager, system owner, security)
  - Approval date (when approval granted)
  - Approval method (ticket approval, email confirmation, workflow system)
  - Approval decision (approved, rejected, conditional approval)
- **Audit Trail**: Approval records retained for 3 years

**REQ-A518-202: Access Rights Inventory**
- **Requirement**: Complete inventory of access rights maintained
- **Inventory Scope**: All access grants across all systems
- **Inventory Purpose**:
  - Access governance (who has access to what)
  - Access reviews (baseline for review data)
  - Audit evidence (demonstrate access control)
  - Incident response (identify affected users during breach)
- **Update Frequency**: Real-time or daily (depending on system capabilities)

### 9.3 Time-Bounded Access Documentation

**REQ-A518-210: Expiration Date Recording**
- **Requirement**: Expiration dates documented for temporary access
- **Applicability**:
  - Contractor access (contract end date)
  - Project-based access (project completion date)
  - Temporary delegation (return date)
  - Trial access (evaluation period end)
- **Enforcement**: Access provisioning system enforces expiration (auto-disable on expiration date)
- **Extension**: Access extension requires new approval (documented separately)

**REQ-A518-211: Access Renewal Documentation**
- **Requirement**: Access renewals/extensions documented
- **Renewal Record**:
  - Original access grant date
  - Expiration date (original)
  - Renewal request date
  - Renewal approver (manager or system owner)
  - New expiration date (extended)
  - Renewal justification (why extension needed)
- **Limit**: Maximum 2 renewals (after 2 renewals, requires full re-approval process)

---

## 10. Audit & Evidence Requirements

### 10.1 Evidence Types for A.5.18

**Evidence Category 1: Access Rights Assignment Evidence**
- **EVD-A518-001**: Access request tickets (all access requests with justification and approvals)
- **EVD-A518-002**: Access provisioning logs (when access was granted, by whom)
- **EVD-A518-003**: Access rights matrix exports (user → system → access level mapping)
- **EVD-A518-004**: Role catalog (all defined roles with access mappings)
- **EVD-A518-005**: Role assignment records (users assigned to roles with approvals)

**Evidence Category 2: Access Review Evidence**
- **EVD-A518-010**: Access review schedules (planned reviews by system and frequency)
- **EVD-A518-011**: Access review completion reports (% complete, overdue reviews)
- **EVD-A518-012**: Access review findings (access confirmed, removed, justified)
- **EVD-A518-013**: Access removal audit logs (access removed based on review findings)
- **EVD-A518-014**: Reviewer sign-offs (reviewers confirming review completion)

**Evidence Category 3: Access Removal Evidence**
- **EVD-A518-020**: Termination-triggered removal logs (access removed for terminated users)
- **EVD-A518-021**: Role change access adjustment logs (excess access removed during role changes)
- **EVD-A518-022**: Access removal verification reports (removals verified successfully)
- **EVD-A518-023**: Time-bounded access expiration logs (temporary access auto-expired)

**Evidence Category 4: Privilege Creep Detection Evidence**
- **EVD-A518-030**: Privilege creep detection reports (users flagged for excess access)
- **EVD-A518-031**: Manager review results (excess access confirmed needed vs. removed)
- **EVD-A518-032**: Exception documentation (justified excess access with approvals)
- **EVD-A518-033**: Privilege creep remediation logs (excess access removed)

**Evidence Category 5: Emergency Access Evidence**
- **EVD-A518-040**: Emergency access request logs (all emergency access requests)
- **EVD-A518-041**: Break-glass account usage logs (all break-glass account actions)
- **EVD-A518-042**: Post-emergency review reports (emergency access usage reviewed)
- **EVD-A518-043**: Emergency access revocation logs (emergency access removed after use)

**Evidence Category 6: Documentation Evidence**
- **EVD-A518-050**: Group ownership assignments (all groups with designated owners)
- **EVD-A518-051**: Group membership approval records (group membership changes with approvals)
- **EVD-A518-052**: Business justification records (justifications for all access grants)
- **EVD-A518-053**: RBAC adoption metrics (% users with roles vs. direct access)

### 10.2 Evidence Collection & Retention

**REQ-A518-220: Evidence Collection Procedures**
- **Requirement**: Evidence systematically collected for audit readiness
- **Collection Methods**:
  - Automated exports (access matrix, audit logs, review reports)
  - Manual compilation (approval documents, justifications, sign-offs)
  - System reports (identity system reports, access governance platform reports)
- **Collection Frequency**:
  - Continuous: Audit logs (real-time logging)
  - Monthly: Access matrix exports, orphaned account reports
  - Quarterly: Access review completion reports, privilege creep reports
  - Annual: Comprehensive evidence package for external audit

**REQ-A518-221: Evidence Retention Period**
- **Requirement**: Access rights evidence retained per regulatory and audit requirements
- **Retention Periods**:
  - **Access request records**: 3 years (from access grant date)
  - **Access review records**: 3 years (from review completion)
  - **Access removal logs**: 3 years (from removal date)
  - **Audit logs (emergency access)**: 7 years (security incident potential)
  - **RBAC role definitions**: Indefinite (until role obsolete + 3 years)
- **Storage**: Evidence stored securely (access restricted to authorized personnel)

**REQ-A518-222: Evidence Accessibility for Audit**
- **Requirement**: Evidence accessible for internal and external audits
- **Access Methods**:
  - Auditor-provided reports (pre-generated reports for common audit requests)
  - Query access (auditors can query access management system directly)
  - Export files (evidence exported in auditor-requested formats)
- **Response Time**: Audit evidence requests fulfilled within 5 business days

### 10.3 Compliance Scoring for A.5.18

**REQ-A518-230: A.5.18 Compliance Metrics**
- **Requirement**: A.5.18 compliance measured via key metrics
- **Compliance Metrics**:

| Metric | Target | Measurement |
|--------|--------|-------------|
| RBAC Adoption Rate | ≥80% | (Users with roles / Total users) × 100 |
| Access Review Completion | ≥95% | (Reviews completed / Reviews due) × 100 |
| Access Removal Timeliness | ≥98% | (Removals within SLA / Total removals) × 100 |
| Privilege Creep Remediation | ≥90% | (Excess access remediated / Total detected) × 100 |
| Emergency Access Appropriateness | ≥95% | (Legitimate emergencies / Total emergency requests) × 100 |
| Access Justification Completeness | ≥95% | (Access with justification / Total access grants) × 100 |

**REQ-A518-231: A.5.18 Compliance Score Calculation**
- **Formula**: A.5.18 Score = Average of all compliance metrics
- **Scoring Interpretation**:
  - **90-100%**: Excellent (optimized access rights management)
  - **80-89%**: Good (mature access rights management)
  - **70-79%**: Acceptable (managed access rights, improvement needed)
  - **<70%**: Poor (significant gaps, immediate remediation required)
- **Reporting**: A.5.18 compliance score reported quarterly to CISO

### 10.4 Integration with Other Controls Evidence

**REQ-A518-240: Evidence Shared with A.5.15 (Access Control)**
- User access aligned with access control policy (policy compliance)
- Segregation of duties violations detected and remediated
- Access exceptions approved and documented

**REQ-A518-241: Evidence Shared with A.5.16 (Identity Management)**
- Access removal for terminated users (deprovisioning timeliness)
- Access adjustment for role changes (mover process compliance)
- Orphaned account access removal (lifecycle compliance)

**REQ-A518-242: Evidence Shared with A.8.2 (Privileged Access Rights)**
- Privileged access assignments (who has privileged access)
- Privileged access review completion (quarterly privileged reviews)
- Privileged access removal timeliness (immediate for terminations)

**REQ-A518-243: Evidence Shared with A.8.5 (Secure Authentication)**
- User access rights inform authentication requirements (privilege level → authentication strength)
- Break-glass account usage logs (emergency authentication events)

---

## Appendix A: Access Rights Management Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│          ACCESS RIGHTS MANAGEMENT WORKFLOW (A.5.18)             │
└─────────────────────────────────────────────────────────────────┘

1. ACCESS REQUEST
   User/Manager → Request System → Ticket Created
   ↓
   Business Justification Documented
   ↓

2. APPROVAL WORKFLOW
   Manager Approval (business need) →
   System Owner Approval (if sensitive) →
   Security Approval (if privileged)
   ↓
   All Approvals Obtained
   ↓

3. PROVISIONING
   IT Operations → Grant Access →
   Document in Access Matrix →
   Notify User
   ↓

4. PERIODIC REVIEW (Quarterly/Annual)
   Extract Access Data →
   Present to Reviewer (Manager/System Owner) →
   Reviewer Decision:
     ├─→ Confirm Access (Access Retained)
     ├─→ Remove Access (Removal Ticket)
     └─→ Justify Exception (Document Justification)
   ↓

5. ACCESS MODIFICATION
   Role Change Detected →
   Compare Old vs. New Role Access →
   Remove Excess Access →
   Grant New Required Access
   ↓

6. ACCESS REMOVAL
   Trigger (Termination/No Longer Needed) →
   IT Operations Removes Access →
   Verify Removal (Account Disabled Test) →
   Log in Audit Trail
   ↓

7. PRIVILEGE CREEP DETECTION
   Compare Current vs. Required Access →
   Flag Excess Access →
   Manager Review →
     ├─→ Justified (Document Exception)
     └─→ Not Justified (Remove Access)
   ↓

8. EMERGENCY ACCESS
   Emergency Request →
   On-Call Approval →
   Grant Break-Glass Access →
   Log All Actions →
   Post-Emergency Review (within 24h) →
   Revoke Emergency Access →
   Rotate Break-Glass Password

   ↓
   [CONTINUOUS CYCLE - Return to Periodic Review]
```

---

## Appendix B: RBAC Implementation Roadmap

**Phase 1: Role Catalog Development (Months 1-2)**
1. Identify common job functions (via HR analysis)
2. Define standard roles (20-30 roles covering 80% of users)
3. Map roles to required access (system-by-system analysis)
4. Assign role owners (business stakeholders)
5. Publish role catalog (centralized repository)

**Phase 2: RBAC Infrastructure (Months 3-4)**
1. Implement role assignment mechanism (identity system or access platform)
2. Develop role assignment approval workflow
3. Build access provisioning automation (assign role → grant all role access)
4. Create RBAC reporting (who has which roles, role coverage)

**Phase 3: User Migration to RBAC (Months 5-8)**
1. Identify users for role assignment (prioritize high-volume roles)
2. Assign users to appropriate roles (manager approval)
3. Verify role access matches user needs (pilot testing)
4. Remove direct access (where replaced by role access)
5. Monitor RBAC adoption rate (track % users with roles)

**Phase 4: RBAC Maturity (Months 9-12)**
1. Achieve target RBAC adoption (≥80%)
2. Implement role review process (annual role definition review)
3. Expand role catalog (define additional specialized roles)
4. Optimize role hierarchy (if applicable)
5. Achieve mature state (90%+ RBAC adoption, minimal direct access)

---

## Appendix C: Access Review Best Practices

**1. Pre-Review Preparation**
- Extract accurate access data (verify data quality before sending to reviewers)
- Pre-flag anomalies (highlight users with excessive access, orphaned accounts)
- Provide context (include user's role, department, manager in review data)
- Communicate expectations (train reviewers on process and accountability)

**2. Review Execution**
- Use structured tools (avoid unstructured spreadsheets if possible)
- Set clear deadlines (review period start/end dates)
- Provide reviewer support (helpdesk for questions, escalation path for issues)
- Track progress (daily completion rate monitoring)

**3. Review Quality Assurance**
- Sample reviews for quality (spot-check reviewer decisions)
- Identify "rubber stamp" reviewers (approving all access without scrutiny)
- Escalate poor-quality reviews (reviewers not taking process seriously)

**4. Post-Review Remediation**
- Execute removals promptly (don't let findings languish)
- Verify removals (ensure access actually removed)
- Document exceptions (justified retained access thoroughly documented)
- Close review cycle (formal sign-off that review is complete)

**5. Continuous Improvement**
- Analyze review findings (common themes? systems with high removal rates?)
- Simplify process (reduce reviewer burden where possible)
- Improve data quality (better access data = easier reviews)
- Automate where possible (pre-approvals for low-risk access, automated removal for orphaned accounts)

---

**END OF POL-S4: Access Rights Management Requirements (A.5.18)**

This section provides comprehensive requirements for access rights assignment, role-based access control, access reviews, privilege creep detection, emergency access, and access rights documentation, ensuring systematic enforcement of access control governance per ISO 27001:2022 Control A.5.18.

**Next Section**: ISMS-POL-A.5.15-16-18-S5 (Assessment Methodology & Evidence Framework)
