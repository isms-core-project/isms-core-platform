# ISMS-IMP-A.5.15-16-18-S1: Access Control Governance
## Implementation Guide for Strategic Access Control Framework

**Document ID**: ISMS-IMP-A.5.15-16-18-S1  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Active

---

## Document Purpose

This implementation guide provides **step-by-step procedures** for establishing access control governance in accordance with ISO/IEC 27001:2022 Control A.5.15. It translates policy requirements from **ISMS-POL-A.5.15-16-18-S2** into actionable implementation steps.

**Target Audience**: Security team, CISO, IAM team leads, policy writers

**Prerequisites**:
- Read ISMS-POL-A.5.15-16-18-S2 (Access Control Policy requirements)
- Executive sponsorship secured
- Stakeholder alignment (HR, IT, Legal, Business)

---

## 1. Access Control Policy Development

### 1.1 Policy Development Process

**Objective**: Create organization's access control policy document implementing A.5.15 requirements.

**Step 1: Assemble Policy Development Team**
- **CISO** (lead and sponsor)
- **IAM Manager** (technical requirements)
- **HR Representative** (employee lifecycle integration)
- **Legal/Compliance** (regulatory requirements)
- **IT Operations Manager** (provisioning practicality)
- **Business Representatives** (business justification framework)

**Estimated Effort**: 1 person assigned, 2-3 weeks coordination

---

**Step 2: Document Current State**

Before writing policy, understand current access control practices:

```
Current State Assessment Checklist:
☐ How are access requests submitted today? (Email? Ticket system? Verbal?)
☐ Who approves access requests? (Managers? IT? System owners?)
☐ How long does provisioning take? (Hours? Days? Weeks?)
☐ How are access reviews conducted? (Manual? Automated? Not at all?)
☐ How are accounts deprovisioned? (HR notifies IT? Automated?)
☐ Are there documented exceptions to standard process?
☐ What identity systems exist? (AD, Azure AD, Okta, custom?)
☐ What user types exist? (Employees, contractors, vendors, service accounts?)
```

**Tool**: Use spreadsheet to document findings
- System/Application → Current Access Process → Approver → SLA
- Identify gaps vs. A.5.15 requirements

**Estimated Effort**: 1 week interviews + documentation

---

**Step 3: Define Access Control Principles**

Translate A.5.15 requirements into organizational principles:

**Template: Access Control Principles Section**

```markdown
## Access Control Principles

[Organization] implements the following access control principles:

### 1. Least Privilege
Users are granted the minimum access required to perform their job functions.
- Access is role-based (not individual-based)
- Additional access requires business justification
- Administrative privileges granted only when necessary

### 2. Need-to-Know
Access to information is restricted to those with a business need.
- Data owners define who needs access
- Access to sensitive data (PII, financial, IP) requires additional approval
- Access to customer data limited to customer-facing roles

### 3. Segregation of Duties (SoD)
Conflicting duties are separated to prevent fraud or error.
- Same person cannot request AND approve access
- Developers do not have production admin access
- Finance roles (request, approve, pay) are separated
- SoD matrix defines all conflicts (see Appendix A)

### 4. Default Deny
No access is granted unless explicitly approved.
- New users start with zero access
- Access must be requested and approved
- Expired access is automatically removed

### 5. Defense in Depth
Multiple layers of access control protect critical assets.
- Network segmentation limits lateral movement
- Application-level access controls enforce least privilege
- Data encryption provides additional protection
```

**Review Point**: Security team reviews, CISO approves principles

---

**Step 4: Define Access Classification Framework**

Create classification scheme for users, systems, and data:

**User Type Classification**

| User Type | Definition | Access Approval | Review Frequency |
|-----------|------------|-----------------|------------------|
| Employee | Internal staff (permanent, full-time/part-time) | Manager | Annual |
| Contractor | Time-bound external workers | Manager + Sponsor | Quarterly |
| Vendor | Third-party service providers | Vendor Manager | Quarterly |
| Partner | Business partners with system access | Partner Manager | Semi-annual |
| Customer | External users (customer portals) | Self-service | N/A (built-in roles) |
| Service Account | Non-human accounts (apps, systems) | System Owner | Annual |
| Emergency Account | Break-glass accounts | CISO | After each use |

**System Criticality Classification**

| Criticality | Definition | Approval Required | Access Review |
|-------------|------------|-------------------|---------------|
| Critical | Business-critical, revenue-impacting | Manager + System Owner + Security | Quarterly |
| High | Important but not critical | Manager + System Owner | Semi-annual |
| Medium | Standard business systems | Manager | Annual |
| Low | Non-critical, low-risk systems | Self-service with justification | Biennial |

**Data Sensitivity Classification** (reference ISMS-POL-A.5.12 if exists)

| Sensitivity | Examples | Access Restrictions |
|-------------|----------|---------------------|
| Restricted | PII, financial records, trade secrets | Approval: Manager + Data Owner + Security |
| Confidential | Internal-only business data | Approval: Manager + Data Owner |
| Internal | General business information | Approval: Manager |
| Public | Public-facing information | No restrictions |

**Customization Note**: Adapt classifications to [Organization]'s risk appetite and industry

**Estimated Effort**: 3-5 days drafting, 1 week stakeholder review

---

**Step 5: Document Business Justification Framework**

Define WHAT constitutes valid business justification:

**Business Justification Requirements**

Access requests must include:
1. **Why access is needed** - Job function or project requirement
2. **What data/systems** - Specific systems and access level
3. **How long needed** - Permanent (role-based) or temporary (project-based)
4. **Who approved** - Manager and/or system owner

**Examples of Valid Justifications**:
- ✅ "User is new Finance Analyst, requires read access to ERP for reporting duties"
- ✅ "User joining Project Phoenix, requires write access to project SharePoint for 6 months"
- ✅ "User promoted to IT Manager, requires admin access to Active Directory"

**Examples of Invalid Justifications**:
- ❌ "User needs access" (too vague)
- ❌ "Same access as Jane Doe" (no business reason)
- ❌ "Boss said so" (no documented approval)

**Rejection Criteria**:
- No clear business need
- Access level exceeds job requirements (violates least privilege)
- Requestor is not user's manager or system owner
- Creates SoD violation without exception approval

**Estimated Effort**: 2-3 days drafting, stakeholder review

---

**Step 6: Write Policy Document**

Combine principles, classifications, and framework into policy document.

**Policy Document Structure**:

```
1. Purpose and Scope
2. Access Control Principles (least privilege, need-to-know, SoD, etc.)
3. Access Classification (users, systems, data)
4. Roles and Responsibilities (see Section 2 below)
5. Business Justification Requirements
6. Access Request and Approval Workflow (see Section 3 below)
7. Segregation of Duties Requirements (see Section 4 below)
8. Exception Management (see Section 5 below)
9. Integration with HR Processes (see Section 6 below)
10. Compliance and Audit (see Section 7 below)
11. Policy Review and Update
12. Definitions and References
```

**Length**: 8-12 pages typically

**Estimated Effort**: 1 week drafting

---

**Step 7: Stakeholder Review and Approval**

Policy approval workflow:

```
1. Draft Review (Security Team) → 3 days
2. Stakeholder Review (HR, IT, Legal, Business) → 1 week
3. Incorporate Feedback → 3 days
4. CISO Approval → Sign-off
5. Executive Communication → Announce policy to organization
```

**Approval Template**:

```
Policy Approval Record

Policy Name: Access Control Policy
Policy ID: ISMS-POL-A.5.15
Version: 1.0
Approval Date: [Date]

Prepared By: [Name, Title] - [Date]
Reviewed By: [Name, Title] - [Date]
Approved By: [CISO Name] - [Date]

Next Review Date: [Date + 12 months]
```

**Estimated Effort**: 2 weeks for review cycle

---

### 1.2 Policy Communication and Training

**Objective**: Ensure stakeholders understand their access control responsibilities.

**Step 1: Identify Training Audiences**

| Audience | Training Focus | Format |
|----------|---------------|--------|
| All Employees | Access request process, acceptable use | 15-min online module |
| Managers | Approval responsibilities, access reviews | 30-min workshop |
| IT Operations | Provisioning procedures, SLAs | 1-hour technical training |
| System Owners | System-specific approvals, reviews | 30-min workshop |
| Security Team | Policy enforcement, exception handling | 2-hour deep dive |

**Step 2: Develop Training Materials**

**For Managers**:
- **Key Message**: "You are accountable for access approvals for your direct reports"
- **Training Topics**:
  - How to approve access requests (ticket system workflow)
  - What to look for in business justifications
  - How to conduct access reviews (quarterly/annually)
  - What to do with orphaned accounts (former direct reports)

**For IT Operations**:
- **Key Message**: "Provision access only after proper approvals"
- **Training Topics**:
  - Approval verification (check approver authority)
  - Provisioning SLAs (standard vs. sensitive access)
  - Access logging and audit trails
  - Escalation procedures (unclear approvals)

**Step 3: Communication Plan**

```
Week 1: Email announcement from CISO
  - Policy published to intranet
  - Link to training modules
  
Week 2-3: Mandatory training rollout
  - Track completion rates
  - Follow-up with non-completers
  
Week 4: Q&A sessions (office hours)
  - Security team answers questions
  
Ongoing: Policy available on intranet, referenced in onboarding
```

**Estimated Effort**: 1 week developing materials, 2 weeks rollout

---

## 2. Access Control Roles and Responsibilities

### 2.1 Define Access Control Roles

**Objective**: Assign clear responsibilities for access control activities.

**RACI Matrix for Access Control**

| Activity | Requestor | Manager | System Owner | IT Ops | Security | CISO |
|----------|-----------|---------|--------------|--------|----------|------|
| Submit access request | R | I | I | I | I | I |
| Approve access (standard) | I | A | I | I | I | I |
| Approve access (sensitive) | I | C | A | I | C | I |
| Provision access | I | I | I | R/A | C | I |
| Review access (quarterly/annual) | I | A/R | A/R | I | C | I |
| Remove access (termination) | I | I | I | R/A | C | I |
| Investigate SoD violations | I | C | C | I | A/R | I |
| Approve exceptions | I | C | C | I | R | A |

**Legend**: R = Responsible, A = Accountable, C = Consulted, I = Informed

---

### 2.2 Role Definitions

**Access Requestor**
- **Who**: Any user needing access (employee, contractor, manager on behalf of user)
- **Responsibilities**:
  - Submit access request via ticketing system
  - Provide clear business justification
  - Specify required access level (read, write, admin)
  - Specify duration (permanent or temporary)
- **Accountability**: Honest representation of access need

---

**Business Owner / Manager**
- **Who**: Direct manager of user requesting access
- **Responsibilities**:
  - Approve access requests based on job function
  - Verify business justification is valid
  - Ensure access aligns with least privilege
  - Conduct periodic access reviews for direct reports
  - Notify IT when direct reports terminate or change roles
- **Accountability**: Appropriate access for team members
- **Training Required**: Yes (approval workflow, review process)

---

**System Owner**
- **Who**: Person responsible for specific application/system
- **Responsibilities**:
  - Define access requirements for their system
  - Approve access to sensitive systems (critical/high classification)
  - Maintain list of current users with access
  - Participate in periodic access reviews
  - Report suspected unauthorized access
- **Accountability**: Security of their system
- **Training Required**: Yes (system-specific approval criteria)

---

**IT Operations / Provisioning Team**
- **Who**: IT staff who grant/remove access in systems
- **Responsibilities**:
  - Verify proper approvals before provisioning
  - Provision access within SLA
  - Document access grants in audit log
  - Remove access upon termination or role change
  - Escalate unclear or suspicious requests
- **Accountability**: Technical accuracy of access provisioning
- **Training Required**: Yes (provisioning procedures, SLAs)

---

**Security Team**
- **Who**: Information Security team members
- **Responsibilities**:
  - Maintain access control policy
  - Monitor SoD violations
  - Review exception requests
  - Conduct access audits
  - Investigate access-related incidents
  - Report compliance to CISO
- **Accountability**: Access control policy enforcement
- **Training Required**: Yes (policy deep dive, exception handling)

---

**CISO (Chief Information Security Officer)**
- **Who**: Executive responsible for information security
- **Responsibilities**:
  - Approve access control policy
  - Approve exceptions to policy (SoD violations, emergency access)
  - Review access audit results (quarterly)
  - Escalation point for access disputes
- **Accountability**: Overall access control effectiveness
- **Authority**: Policy waivers, risk acceptance

---

### 2.3 Role Assignment Process

**Step 1: Identify System Owners**

For each business-critical system, assign a system owner:

```
System Owner Assignment Template

System Name: [e.g., ERP (SAP)]
System Owner: [Name, Title]
Backup Owner: [Name, Title]
Criticality: [Critical / High / Medium / Low]
Data Sensitivity: [Restricted / Confidential / Internal / Public]

Approval Authority:
- Standard access: Manager approval only
- Sensitive access: Manager + System Owner approval
- Admin access: Manager + System Owner + Security approval

Review Frequency: [Quarterly / Semi-annual / Annual]
```

**Process**:
1. IT creates list of all business systems
2. Business leaders nominate system owners
3. CISO approves system owner assignments
4. System owners trained on responsibilities

**Estimated Effort**: 2 weeks (for 50-100 systems)

---

**Step 2: Document Role Assignments**

Create "Access Control Roles Register":

| Person | Role | Systems/Scope | Trained? | Appointment Date |
|--------|------|---------------|----------|------------------|
| Jane Doe | System Owner | ERP (SAP) | Yes | 2026-01-15 |
| John Smith | System Owner | CRM (Salesforce) | Yes | 2026-01-15 |
| Alice Johnson | Access Reviewer | Finance Department | Yes | 2026-01-20 |
| Bob Williams | IT Provisioner | Active Directory | Yes | 2026-01-10 |

**Maintenance**: Update quarterly, review annually

---

## 3. Access Request and Approval Workflow

### 3.1 Design Access Request Workflow

**Objective**: Implement consistent, auditable access request process.

**Step 1: Select Ticketing System**

Access requests should be tracked in ticketing system:

**Options**:
- **ServiceNow** (ITSM platform with access request module)
- **Jira Service Management** (flexible workflow, good for small-medium orgs)
- **Freshservice** (user-friendly, good for non-technical users)
- **Email + Spreadsheet** (only for very small orgs, not recommended)

**Requirements**:
- Request form with fields (user, system, access level, justification, duration)
- Approval workflow (manager → system owner → IT)
- Email notifications (requestor, approver, provisioner)
- Audit trail (who approved, when)
- Integration with identity systems (optional but recommended)

---

**Step 2: Configure Request Form**

**Access Request Form Fields**:

```
Ticket Type: Access Request

Required Fields:
☐ Requestor Name (auto-populated from login)
☐ User Needing Access (if requesting for someone else)
☐ System/Application (dropdown: all systems)
☐ Access Level (dropdown: Read / Write / Admin)
☐ Business Justification (free text, 100 char min)
☐ Duration (dropdown: Permanent / Temporary)
  ↳ If Temporary: End Date (date picker)
☐ Manager (auto-populated from HR system)
☐ Priority (dropdown: Standard / Urgent)

Optional Fields:
☐ Specific Groups/Roles (if known)
☐ Reference User (for "same access as" requests)
☐ Project Code (for project-based access)

Auto-Generated:
☐ Ticket ID (unique identifier)
☐ Submission Date/Time
☐ Requestor Email
```

---

**Step 3: Design Approval Workflow**

**Standard Access Workflow**:

```
1. User submits request
   ↓
2. Manager receives approval email
   ├─ Approve → Go to step 3
   ├─ Reject → Request closed, user notified
   └─ No response after 3 days → Escalate to manager's manager
   ↓
3. IT Operations receives provisioning task
   ├─ Provision access
   ├─ Verify access granted (test login)
   └─ Update ticket: "Provisioned on [date]"
   ↓
4. User receives "Access Granted" notification
   ↓
5. Ticket closed, archived for audit
```

**Sensitive Access Workflow** (Critical/High systems, Restricted data):

```
1. User submits request
   ↓
2. Manager receives approval email
   ├─ Approve → Go to step 3
   └─ Reject → Request closed
   ↓
3. System Owner receives approval email
   ├─ Approve → Go to step 4
   └─ Reject → Request closed, manager notified
   ↓
4. Security Team review (if Admin access)
   ├─ Approve → Go to step 5
   └─ Reject → Escalate to CISO
   ↓
5. IT Operations provisions access
   ↓
6. Ticket closed
```

---

**Step 4: Set Provisioning SLAs**

Define service level agreements for access provisioning:

| Access Type | SLA | Measurement |
|-------------|-----|-------------|
| Standard access (read/write) | 1 business day | Time from final approval to access granted |
| Sensitive access (critical systems) | 3 business days | Time from final approval to access granted |
| Admin/privileged access | 5 business days | Time from final approval to access granted (includes security review) |
| Emergency access | Same day | Time from CISO approval to access granted |
| Contractor onboarding | By contract start date | Access ready by first day of work |

**SLA Exceptions**:
- If request submitted after 3pm, next business day counts as Day 1
- Holidays not counted in business days
- Delays due to missing approvals not counted against IT

**Monitoring**: Track SLA compliance monthly, report to IT management

---

**Step 5: Implement Auto-Routing**

Configure ticket system to auto-route approvals:

**Auto-Routing Rules**:
```
IF System = "ERP (SAP)" AND Access Level = "Admin"
  THEN Route to: Manager → System Owner (Jane Doe) → Security Team
  
IF System = "CRM (Salesforce)" AND Access Level = "Read"
  THEN Route to: Manager → IT Operations
  
IF User Type = "Contractor"
  THEN Require: Sponsor field + Contract End Date
  THEN Route to: Manager → Sponsor → IT Operations
```

**Benefits**:
- Reduces routing errors
- Ensures correct approvers engaged
- Faster processing (no manual routing)

**Estimated Effort**: 1-2 weeks configuration, 1 week testing

---

### 3.2 Exception Handling Process

**Objective**: Manage requests that don't fit standard workflow.

**Step 1: Define Exception Scenarios**

Common exceptions:
1. **Emergency Access** - User needs immediate access (system outage, security incident)
2. **SoD Violation** - User needs access that conflicts with existing role
3. **Shared Account** - Team needs shared account (discouraged but sometimes necessary)
4. **Extended Access** - Contractor needs access beyond contract end date
5. **Guest Access** - External party needs temporary access (auditors, consultants)

---

**Step 2: Exception Approval Workflow**

**Emergency Access**:
```
1. User submits emergency access request
   ↓
2. IT Manager or CISO approval (phone/email approval acceptable)
   ↓
3. Access granted immediately
   ↓
4. After-the-fact documentation required within 24 hours:
   - Business justification
   - Manager confirmation
   - Security review
   ↓
5. Emergency access reviewed weekly (CISO receives report)
```

**SoD Violation Exception**:
```
1. User submits access request
   ↓
2. System detects SoD violation (user already has conflicting role)
   ↓
3. Automatic escalation to Security Team
   ↓
4. Security Team reviews:
   ├─ Can be mitigated? (remove one role, use different approach)
   │  └─ Recommend alternative, reject request
   └─ Cannot be mitigated? (business requirement)
      └─ Escalate to CISO with compensating controls proposal
   ↓
5. CISO approves with compensating controls:
   - Enhanced monitoring (all actions logged)
   - Secondary approval for sensitive transactions
   - Quarterly review of user's activity
   ↓
6. Access granted, exception documented, quarterly review scheduled
```

---

**Step 3: Document Exceptions**

**Exception Register**:

| Exception ID | User | Exception Type | Justification | Approver | Approval Date | Compensating Controls | Review Date |
|--------------|------|----------------|---------------|----------|---------------|----------------------|-------------|
| EXC-001 | Alice Johnson | SoD Violation (AP Clerk + AP Approver) | Small team, no other qualified person | CISO | 2026-01-15 | Manager reviews all Alice's approvals | 2026-04-15 |
| EXC-002 | Bob Williams | Shared Account (shared-finance-team) | Legacy system, no individual accounts | CISO | 2026-01-10 | All logins logged, monthly review | 2026-02-10 |

**Review Frequency**: Quarterly (all exceptions reviewed)

**Expiration**: Exceptions expire annually, must be re-approved

---

## 4. Segregation of Duties (SoD) Matrix

### 4.1 Develop SoD Matrix

**Objective**: Define conflicting roles to prevent fraud or error.

**Step 1: Identify Critical Business Processes**

Focus on processes where SoD prevents fraud:
- **Financial**: Accounts Payable, Accounts Receivable, Payroll, Purchasing
- **IT**: Development vs. Production, Access Provisioning vs. Approval
- **HR**: Employee Data Entry vs. Payroll Processing
- **Compliance**: Audit vs. Implementation

---

**Step 2: Define Conflicting Roles**

**SoD Matrix Template**:

| Process Area | Role A | Role B | Conflict Type | Risk if Combined | Mitigation |
|--------------|--------|--------|---------------|------------------|------------|
| Accounts Payable | AP Clerk (enter invoices) | AP Approver (approve payments) | Request + Approve | Fraudulent payments | Separate users, or manager review |
| Purchasing | Purchase Requisitioner | Purchase Approver | Request + Approve | Unauthorized purchases | Separate users, spending limits |
| Access Management | Access Requestor | Access Approver | Request + Approve | Unauthorized access | Manager approval required |
| IT Development | Developer (write code) | Production Admin (deploy code) | Create + Execute | Unauthorized changes | Change approval board |
| Payroll | HR Data Entry (employee info) | Payroll Processor (calculate pay) | Data Entry + Processing | Fraudulent payroll | Manager review of payroll changes |
| Audit | Auditor (test controls) | Process Owner (implement controls) | Assess + Implement | Biased audit results | Independent audit team |

**Customization**: [Organization] adds industry-specific SoD requirements (e.g., trading firms separate front-office and back-office)

---

**Step 3: Implement SoD Checks**

**Automated SoD Detection** (if using identity management platform):

```
SoD Rule Configuration

Rule 1: Accounts Payable Segregation
  IF User in group "AP-Clerks"
  AND User requests group "AP-Approvers"
  THEN Trigger SoD violation workflow
  
Rule 2: Development vs. Production
  IF User has role "Developer"
  AND User requests role "Production-Admin"
  THEN Trigger SoD violation workflow
  
Rule 3: Access Request Self-Approval
  IF User = Manager
  AND User requests access for self
  THEN Require Manager's Manager approval
```

**Manual SoD Detection** (if no automation):
- Periodic review (quarterly) of user role assignments
- Cross-reference users against SoD matrix
- Flag violations for review

---

**Step 4: SoD Violation Remediation**

When SoD violation detected:

```
Remediation Workflow

1. Security Team notifies user's manager and user
   ↓
2. Manager decides:
   ├─ Remove one conflicting role (user doesn't need both)
   │  └─ IT removes access, ticket closed
   ├─ Business justification (user needs both roles)
   │  ├─ Propose compensating controls
   │  └─ Escalate to CISO for exception approval
   └─ Dispute (not actually a violation)
      └─ Security Team re-evaluates SoD matrix
   ↓
3. If approved: Document exception, implement compensating controls
   ↓
4. If rejected: Remove one role, notify user and manager
```

**Compensating Controls Examples**:
- Manager reviews all conflicting transactions monthly
- All conflicting actions logged and audited quarterly
- Secondary approval required for sensitive transactions
- User's activity monitored by Security Team

---

### 4.2 SoD Monitoring and Reporting

**Monitoring Frequency**: Monthly automated scan, quarterly manual review

**SoD Violation Report Template**:

```
SoD Violation Report - January 2026

Total Users Reviewed: 500
SoD Violations Detected: 8
Approved Exceptions: 3
Violations Remediated: 4
Violations Pending Resolution: 1

Details:

Violation #1:
- User: Alice Johnson
- Conflicting Roles: AP-Clerk + AP-Approver
- Status: Approved Exception (EXC-001)
- Compensating Control: Manager reviews all Alice's approvals
- Next Review: 2026-04-15

Violation #2:
- User: Bob Williams
- Conflicting Roles: Developer + Production-Admin
- Status: Remediated on 2026-01-20 (removed Production-Admin role)

[...]

Escalations:
- Violation #8: Charlie Davis (Finance Manager + Payroll Processor)
  - Pending CISO review for exception approval
  - Proposed compensating control: Independent payroll audit
```

**Distribution**: CISO (monthly), Audit Committee (quarterly)

---

## 5. Integration with HR Processes

### 5.1 Onboarding Integration (Joiner Process)

**Objective**: Automate access provisioning for new hires.

**Step 1: Map HR-to-IAM Integration Points**

```
HR System (Authoritative Source)
  ↓ (API or file export)
Identity Management System (Active Directory, Azure AD, Okta)
  ↓ (Provisioning workflow)
Business Applications (email, intranet, role-based access)
```

**Integration Scenarios**:

**Scenario A: API Integration** (best practice)
- HR system has API (e.g., Workday, SAP SuccessFactors)
- Identity system calls HR API daily
- New hire detected → Trigger provisioning workflow

**Scenario B: File Export** (common for legacy HR systems)
- HR system exports employee list (CSV) daily
- Identity system imports file, detects new hires
- Manual verification (HR confirms new hires)

**Scenario C: Manual Process** (small organizations)
- HR emails IT when new hire starts
- IT manually creates accounts
- Not recommended (error-prone, not scalable)

---

**Step 2: Define Onboarding Workflow**

```
New Hire Onboarding - Access Provisioning

Week -1 (Before Start Date):
☐ HR enters new hire in HR system (name, title, department, start date, manager)
☐ Manager receives "New Hire Access" email
  - Review default access for [Job Title]
  - Request additional access if needed
  - Confirm access requirements by [Start Date - 3 days]

Day -3 (Three Days Before Start):
☐ IT creates user account (email, AD/Azure AD, network access)
☐ IT provisions default access (based on job title/department)
  - Example: All employees get email, intranet, HR portal
  - Finance employees get read access to ERP
  - Developers get access to development environments
☐ IT sends welcome email with login credentials (to personal email)

Day 1 (Start Date):
☐ New hire logs in (account active)
☐ Manager confirms access is working
☐ If additional access needed: Submit access requests (standard workflow)

Week 1:
☐ Security Team reviews new hire access (compliance check)
☐ Confirm access aligns with job function
```

**Access Provisioning SLA**: Access ready by start date (no exceptions)

---

**Step 3: Define Default Access by Role**

**Default Access Matrix**:

| Job Title / Department | Default Access |
|------------------------|----------------|
| All Employees | Email, Intranet, HR Portal (self-service), O365 (basic) |
| Finance (any role) | ERP (read), Finance SharePoint, Expense System |
| HR | HRIS (read/write per role), Recruiting System, Benefits Portal |
| IT | Ticketing System, Monitoring Dashboards, Knowledge Base |
| Sales | CRM (Salesforce), Sales Portal, Commission Tracking |
| Engineering | Code Repository (GitHub), Development Environments, Jira |
| Marketing | CMS, Marketing Automation (HubSpot), Analytics |

**Customization**: [Organization] defines role-based access based on job analysis

**Maintenance**: Review default access matrix annually, update as roles change

---

### 5.2 Offboarding Integration (Leaver Process)

**Objective**: Ensure access is removed promptly when employees terminate.

**Step 1: Define Offboarding Trigger**

**Termination Detection**:
- HR updates employee status in HR system (status = "Terminated", termination date set)
- Identity system detects status change (daily sync)
- Offboarding workflow triggered automatically

**Voluntary vs. Involuntary**:
- **Involuntary termination**: Disable access immediately (within 1 hour)
- **Voluntary resignation**: Disable access on last working day (end of day)

---

**Step 2: Define Offboarding Workflow**

```
Employee Offboarding - Access Removal

Involuntary Termination (Immediate):

Hour 0:
☐ HR updates termination status in HR system
☐ HR notifies IT via phone/email (urgent)

Hour 1:
☐ IT disables user account immediately (AD/Azure AD)
☐ IT disables email (forward to manager)
☐ IT disables VPN access
☐ IT disables physical access (revoke badge)

Hour 2-4:
☐ IT removes user from all groups (application access)
☐ IT resets user passwords (prevent re-access)
☐ IT notifies Security Team (in case of malicious activity)

Day 1-7:
☐ IT archives user's email (export to PST, store securely)
☐ IT archives user's files (OneDrive, network drives)
☐ Manager receives "Data Handover" email (review ex-employee's files)

Day 30:
☐ IT reviews account for complete removal
☐ Service accounts owned by user reassigned
☐ Distribution lists updated (remove user)

Day 90:
☐ Account deleted (if no retention requirement)
☐ All access removal verified (audit log check)

---

Voluntary Resignation (Scheduled):

Week -2 (Two Weeks Before Last Day):
☐ HR updates termination date in HR system
☐ Manager notified (prepare for knowledge transfer)

Last Working Day (5pm):
☐ IT disables account (user cannot log in after hours)
☐ IT forwards email to manager (temporary, 30 days)

Day 1-7 (After Last Day):
☐ Same as involuntary termination (archive, handover, removal)
```

**Access Removal SLA**:
- Involuntary: Within 1 hour
- Voluntary: End of last working day

---

**Step 3: Data Handover Process**

When employee leaves, manager must handle data handover:

```
Manager Data Handover Checklist

☐ Review ex-employee's email (important threads?)
  - Forward critical emails to yourself or team
  - Set up auto-reply ("X no longer with company, contact Y")
  
☐ Review ex-employee's files (network drives, OneDrive)
  - Identify critical files (project documentation, customer data)
  - Transfer ownership to yourself or team member
  
☐ Update distribution lists
  - Remove ex-employee from team email aliases
  - Update external contact lists
  
☐ Reassign tasks (Jira, Asana, project management tools)
  - Reassign open tickets to team members
  - Update project assignments
  
☐ Transfer ownership of service accounts (if applicable)
  - If ex-employee was owner of service accounts, reassign owner
  - Update documentation
  
☐ Notify external parties (customers, partners)
  - Inform key contacts of employee departure
  - Provide new point of contact
```

**Timeline**: Manager has 7 days to complete handover

---

### 5.3 Role Change Integration (Mover Process)

**Objective**: Update access when employees change roles.

**Step 1: Detect Role Changes**

HR system updates:
- Job title change
- Department transfer
- Manager change
- Promotion/demotion

**Integration**:
- Daily sync detects role changes
- Automatic email to old manager, new manager, and IT

---

**Step 2: Role Change Workflow**

```
Employee Role Change - Access Update

Day 0 (Role Change Effective Date):
☐ HR updates employee record (new title, department, manager)
☐ Old Manager receives notification:
  - "Employee X transferred to [Department] on [Date]"
  - "Review X's current access, revoke access no longer needed"
☐ New Manager receives notification:
  - "Employee X joined your team on [Date]"
  - "Review X's access, request additional access if needed"

Day 1-3:
☐ Old Manager reviews access, submits removal requests
  - Remove department-specific access (old team's systems)
  - Remove project-based access (if projects completed)
☐ New Manager requests new access
  - Grant default access for new role/department
  - Grant specific access based on new responsibilities

Day 7:
☐ IT completes access modifications
☐ User confirms access is correct (can access new systems, old access removed)

Day 14:
☐ Security Team reviews role change (compliance check)
☐ Confirm user has appropriate access for new role
☐ Confirm old access removed (prevent privilege creep)
```

**Access Modification SLA**: 1 business day from manager approval

---

**Step 3: Privilege Creep Prevention**

**Problem**: Users accumulate excess access over time (role changes, projects, etc.)

**Solution**:
1. **Automatic Access Review Triggered**: When user changes roles, access review triggered
2. **Compare Access vs. Role**: IT compares user's current access vs. new role's default access
3. **Flag Discrepancies**: Any access not aligned with new role = flagged for review
4. **Manager Confirms or Removes**: Manager justifies why user still needs access OR removes it

**Example**:
```
User: Alice Johnson
Role Change: Finance Analyst → HR Analyst

Current Access:
- ERP (Finance module) [Read]
- Finance SharePoint [Write]
- HR Portal [Read]
- Benefits Portal [No Access]

New Role Default Access:
- HR Portal [Write]
- Benefits Portal [Read/Write]
- HRIS [Read]

Discrepancies Flagged:
- ERP (Finance module) - NOT in new role's default access
  Manager Decision: Remove (no longer needed)
- Finance SharePoint - NOT in new role's default access
  Manager Decision: Remove (no longer needed)

Result:
- Remove: ERP, Finance SharePoint
- Add: Benefits Portal (Write), HRIS (Read)
- Modify: HR Portal (Read → Write)
```

---

## 6. Compliance and Audit Support

### 6.1 Audit Evidence Preparation

**Objective**: Provide evidence of access control policy compliance.

**Evidence Artifacts**:

1. **Access Control Policy Document**
   - Policy approved by CISO
   - Version control (current version, change log)
   - Distribution (where published, who has access)

2. **SoD Matrix**
   - Conflicting roles defined
   - Automated detection rules configured
   - Exception approval process documented

3. **Access Request Approvals** (sample 20 requests)
   - Business justification documented
   - Appropriate approver signed off
   - Provisioning within SLA
   - Audit trail (who requested, who approved, when provisioned)

4. **SoD Violation Reports**
   - Monthly reports (last 3 months)
   - All violations either approved (with exception) or remediated
   - Exception approvals signed by CISO

5. **Access Review Results** (see IMP-S4 for details)
   - Review completion rates (quarterly/annually)
   - Access removal records (inappropriate access removed)
   - Reviewer sign-offs

6. **Onboarding/Offboarding Records**
   - Provisioning timeliness (access by start date)
   - Deprovisioning timeliness (access removed within 24 hours)
   - Sample new hires (access granted on time?)
   - Sample terminations (access removed on time?)

---

### 6.2 Audit Testing Procedures

**For Auditors**: How to test A.5.15 compliance

**Test 1: Policy Existence and Approval**
```
1. Request access control policy document
2. Verify CISO signature and approval date
3. Verify policy published and accessible to stakeholders
4. Verify policy reviewed within last 12 months
```

**Test 2: Access Request Approvals**
```
1. Select random sample of 20 access requests (last quarter)
2. For each request, verify:
   ☐ Business justification documented
   ☐ Appropriate approver (manager or system owner)
   ☐ Approver has authority (is user's manager or designated approver)
   ☐ Access level matches approved access level
   ☐ Provisioning within SLA (1 business day for standard)
3. Identify exceptions: Any requests without proper approvals?
4. For exceptions: Verify exception approval by CISO
```

**Test 3: Segregation of Duties**
```
1. Request SoD matrix
2. Request current SoD violation report
3. For each violation, verify:
   ☐ Violation is approved exception (CISO signature) OR
   ☐ Violation has been remediated (access removed)
4. For approved exceptions, verify:
   ☐ Compensating controls documented
   ☐ Compensating controls implemented (check logs, reviews)
   ☐ Exception reviewed within last quarter
```

**Test 4: Onboarding Timeliness**
```
1. Select 10 new hires (last quarter)
2. For each new hire, check:
   ☐ Start date (from HR system)
   ☐ Account creation date (from identity system)
   ☐ Access provisioned by start date? (Day 0 or earlier)
3. Calculate on-time provisioning rate (target: ≥95%)
4. Investigate late provisioning (root cause, corrective action)
```

**Test 5: Offboarding Timeliness**
```
1. Select 10 terminated employees (last quarter)
2. For each termination, check:
   ☐ Termination date (from HR system)
   ☐ Account disable date (from identity system)
   ☐ Access removed within 24 hours? (target: ≤1 day)
3. Calculate on-time deprovisioning rate (target: ≥98%)
4. Verify account deletion after 90 days (if no retention requirement)
```

**Test 6: Exception Management**
```
1. Request exception register (all current exceptions)
2. For each exception:
   ☐ CISO approval documented
   ☐ Business justification clear and valid
   ☐ Compensating controls defined
   ☐ Exception reviewed within last quarter
   ☐ Exception expiration date set (annual renewal)
3. Verify no expired exceptions still active
```

---

### 6.3 Continuous Monitoring

**Objective**: Monitor access control compliance continuously (not just at audit time).

**Monthly Monitoring**:
- SoD violation scan (automated)
- Orphaned account detection (cross-reference with HR)
- Access request SLA compliance (% provisioned on time)
- New hire provisioning timeliness (% access ready by start date)
- Termination deprovisioning timeliness (% removed within 24h)

**Quarterly Monitoring**:
- Access review completion rates (critical systems reviewed on time?)
- Exception register review (all exceptions still valid?)
- Role change access updates (privilege creep detection)

**Annual Monitoring**:
- Policy review and update (any changes needed?)
- SoD matrix update (new conflicting roles identified?)
- System owner assignments review (all systems have owners?)

**Dashboard**: Security team maintains "Access Control Compliance Dashboard"
- Overall compliance score (0-100)
- Red/yellow/green indicators per metric
- Trend analysis (improving or declining?)

---

## 7. Common Pitfalls and Solutions

### 7.1 Common Implementation Challenges

**Challenge 1: "We don't have time to approve every access request"**

**Problem**: Managers complain approval workflow slows down business

**Solutions**:
1. **Pre-Approved Access**: Default access for standard roles (auto-provisioned)
2. **Delegation**: Managers delegate approval to trusted team leads
3. **Risk-Based Approach**: Low-risk systems = self-service with justification, high-risk = full approval
4. **Batch Approvals**: Group multiple requests for same user (onboarding)

**Example**:
```
Instead of: 5 separate tickets (email, intranet, ERP, SharePoint, CRM)
Use: 1 "New Hire Onboarding" ticket with all default access
Manager approves once, all access provisioned
```

---

**Challenge 2: "IT can't provision access within SLA"**

**Problem**: IT overwhelmed with access requests, can't meet 1-day SLA

**Solutions**:
1. **Automation**: Automate provisioning for standard access (AD groups, email, etc.)
2. **Self-Service**: Users provision low-risk access themselves (with auto-approval)
3. **Staffing**: Increase IT provisioning team capacity
4. **Process Improvement**: Identify bottlenecks (approval delays? unclear requests?)

**Metrics to Track**:
- Time from request submission to manager approval
- Time from approval to provisioning
- % requests delayed due to missing information

---

**Challenge 3: "Managers don't respond to access review requests"**

**Problem**: Access reviews incomplete, managers ignore review emails

**Solutions** (see IMP-S4 for detailed review process):
1. **Executive Sponsorship**: CISO communicates importance of reviews
2. **Simplify Review**: Pre-populate review data (who has access, remove or confirm)
3. **Escalation**: Unresponsive managers escalated to their manager
4. **Consequences**: Incomplete reviews tied to performance evaluations
5. **Automate**: Use access review platform (SailPoint, Saviynt) to streamline

**Timeline**:
```
Week 1: Review requests sent
Week 2: Reminder emails sent
Week 3: Escalation to manager's manager
Week 4: Incomplete reviews reported to executive team
```

---

**Challenge 4: "SoD violations everywhere, we can't fix them all"**

**Problem**: Initial SoD scan identifies 100+ violations, overwhelming

**Solutions**:
1. **Prioritize**: Start with high-risk violations (finance, privileged access)
2. **Phase Remediation**: Fix critical violations first, others over 6-12 months
3. **Risk Acceptance**: Some violations may be accepted with compensating controls
4. **Role Redesign**: Redesign roles to avoid conflicts (split job functions)

**Phased Approach**:
```
Phase 1 (Month 1-2): Fix financial SoD violations (AP, AR, payroll)
Phase 2 (Month 3-4): Fix IT SoD violations (dev vs. prod, access provisioning)
Phase 3 (Month 5-6): Fix remaining violations or approve exceptions
```

---

**Challenge 5: "We have too many systems, can't review all access"**

**Problem**: 200+ systems, can't review all user access annually

**Solutions**:
1. **Risk-Based Reviews**: Review critical systems quarterly, low-risk systems biennially
2. **Automated Reviews**: Use access review platform to automate data collection
3. **System Rationalization**: Decommission unused systems (reduce review scope)
4. **Federated Reviews**: System owners review their own systems (not centralized)

**System Prioritization**:
```
Critical Systems (20 systems): Quarterly reviews
High-Risk Systems (50 systems): Semi-annual reviews
Standard Systems (100 systems): Annual reviews
Low-Risk Systems (30 systems): Biennial reviews
Total: 200 systems, manageable review workload
```

---

## 8. Success Metrics

### 8.1 Key Performance Indicators (KPIs)

**Measure access control governance effectiveness**:

| Metric | Target | Measurement Frequency |
|--------|--------|----------------------|
| Access requests with documented business justification | ≥95% | Monthly |
| Access provisioning within SLA (1 business day) | ≥90% | Monthly |
| New hire access ready by start date | ≥95% | Monthly |
| Terminated employee access removed within 24h | ≥98% | Monthly |
| SoD violations remediated or approved within 30 days | 100% | Monthly |
| Access review completion rate (critical systems) | ≥95% | Quarterly |
| Orphaned accounts detected and remediated | ≤1% of total accounts | Monthly |
| Exception renewals completed on time | 100% | Quarterly |
| Audit findings related to access control | ≤2 per year | Annual |

---

### 8.2 Maturity Assessment

**Assess organizational access control maturity**:

**Level 1: Initial (Ad-Hoc)**
- Access requests via email, no standard process
- Approvals not documented
- Access reviews not conducted
- Accounts not deprovisioned on time
- **Characteristics**: Reactive, inconsistent, high risk

**Level 2: Managed (Repeatable)**
- Access request process documented
- Approvals tracked in ticketing system
- Periodic access reviews conducted
- Some automation (onboarding/offboarding)
- **Characteristics**: Repeatable, some consistency, medium risk

**Level 3: Defined (Standardized)**
- Access control policy approved and published
- Automated provisioning/deprovisioning (HR integration)
- RBAC framework implemented
- Regular access reviews (quarterly/annually)
- SoD matrix defined, violations monitored
- **Characteristics**: Standardized, automated, low risk

**Level 4: Optimizing (Continuous Improvement)**
- Real-time access monitoring and alerting
- Predictive analytics (privilege creep detection)
- Self-service access portal (low-risk access)
- Continuous compliance monitoring (dashboards)
- Proactive remediation (auto-remove expired access)
- **Characteristics**: Proactive, optimized, very low risk

**Goal**: Most organizations should aim for Level 3 (Defined) within 12-18 months

---

## 9. Tools and Templates

### 9.1 Access Control Policy Template

See **ISMS-POL-A.5.15-16-18-S2** for full policy requirements.

**Quick Start Template**:
```markdown
# Access Control Policy

## 1. Purpose
This policy defines [Organization]'s approach to controlling access to information and systems.

## 2. Scope
Applies to all users (employees, contractors, vendors) and all systems.

## 3. Access Control Principles
- Least Privilege
- Need-to-Know
- Segregation of Duties
- Default Deny
- Defense in Depth

## 4. Access Request Process
[Describe workflow: request → approval → provisioning]

## 5. Access Reviews
[Describe review frequency and process]

## 6. Segregation of Duties
[Reference SoD matrix]

## 7. Exceptions
[Describe exception approval process]

## 8. Compliance
[Describe audit requirements]
```

---

### 9.2 SoD Matrix Template

**Excel Template**: SoD_Matrix.xlsx

| Process Area | Role A | Role B | Conflict Type | Risk Level | Mitigation |
|--------------|--------|--------|---------------|------------|------------|
| Accounts Payable | AP Clerk | AP Approver | Request + Approve | High | Separate users or manager review |
| [Add more] | | | | | |

**Instructions**:
1. Identify critical business processes
2. Define conflicting roles (request + approve, create + execute, etc.)
3. Assess risk level (high, medium, low)
4. Define mitigation (separate users, compensating controls)

---

### 9.3 Access Request Form Template

**Fields**:
- Requestor Name
- User Needing Access
- System/Application
- Access Level (Read / Write / Admin)
- Business Justification (minimum 100 characters)
- Duration (Permanent / Temporary, if temporary: end date)
- Manager (auto-populated)
- Priority (Standard / Urgent)

**Approval Workflow**:
1. Manager approves
2. System Owner approves (if critical/high system)
3. IT provisions access
4. User notified

---

### 9.4 Exception Request Template

```markdown
# Access Control Exception Request

**Exception ID**: [Auto-generated]
**Requestor**: [Name]
**User**: [User needing exception]
**Exception Type**: [SoD Violation / Shared Account / Emergency Access / Other]

**Business Justification**:
[Explain why exception is necessary, why standard process doesn't work]

**Proposed Compensating Controls**:
1. [e.g., Manager reviews all conflicting transactions monthly]
2. [e.g., Enhanced logging and quarterly audit]
3. [e.g., Secondary approval required for sensitive actions]

**Duration**: [How long exception is needed]
**Review Frequency**: [Quarterly / Annually]

**Approvals**:
- Security Team Review: [Approve / Reject] - [Name, Date]
- CISO Approval: [Approve / Reject] - [Name, Date]

**Exception Granted**: [Yes / No]
**Next Review Date**: [Date]
```

---

## 10. Next Steps

### 10.1 Implementation Roadmap

**Month 1-2: Foundation**
- ☐ Assemble policy development team
- ☐ Document current state (access processes, systems, user types)
- ☐ Draft access control policy
- ☐ Identify system owners
- ☐ Develop SoD matrix (initial version)

**Month 3-4: Process Design**
- ☐ Configure access request ticketing system
- ☐ Design approval workflows (standard, sensitive, emergency)
- ☐ Define default access by role
- ☐ Integrate with HR (onboarding/offboarding automation)
- ☐ Implement SoD detection (automated or manual)

**Month 5-6: Rollout**
- ☐ Train managers (approval responsibilities)
- ☐ Train IT operations (provisioning procedures)
- ☐ Train system owners (access governance)
- ☐ Launch access request process (pilot with one department)
- ☐ Expand to all departments

**Month 7-12: Optimization**
- ☐ Monitor SLA compliance (provisioning timeliness)
- ☐ Conduct first access reviews (critical systems)
- ☐ Remediate SoD violations (phased approach)
- ☐ Automate where possible (self-service, auto-approvals)
- ☐ Report to CISO (compliance dashboard)

---

### 10.2 Success Criteria

Access control governance implementation is successful when:

✅ **Policy**: Access control policy approved by CISO, published to organization  
✅ **Process**: Access request workflow operational, all requests tracked in tickets  
✅ **Approvals**: ≥95% of access requests have documented business justification and manager approval  
✅ **Provisioning**: ≥90% of access provisioned within SLA (1 business day)  
✅ **Onboarding**: ≥95% of new hires have access ready by start date  
✅ **Offboarding**: ≥98% of terminated employees' access removed within 24 hours  
✅ **SoD**: SoD matrix defined, violations monitored monthly, all violations remediated or approved  
✅ **Reviews**: Access reviews conducted for critical systems (quarterly)  
✅ **Audit**: Audit findings ≤2 per year, no material weaknesses  

---

## 11. Document Maintenance

**Review Frequency**: Annually (or when significant changes occur)

**Triggers for Update**:
- Regulatory changes (new compliance requirements)
- Organizational changes (merger, acquisition, restructuring)
- Technology changes (new identity systems, new applications)
- Audit findings (deficiencies identified, corrective action needed)
- Business process changes (new workflows, new user types)

**Update Process**:
1. Security Team proposes updates
2. Stakeholder review (HR, IT, Legal, Business)
3. CISO approval
4. Communication to organization
5. Training (if significant changes)

---

## 12. Document Approval

**Prepared By**: [Name], [Title] - [Date]  
**Reviewed By**: [Name], [Title] - [Date]  
**Approved By**: [Name], CISO - [Date]

**Next Review Date**: [Date + 12 months]

**Version History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial implementation guide |

---

**END OF IMPLEMENTATION GUIDE S1 (Access Control Governance)**

**Related Documents**:
- ISMS-POL-A.5.15-16-18-S2 (Access Control Policy Requirements)
- ISMS-IMP-A.5.15-16-18-S2 (Identity Lifecycle Process)
- ISMS-IMP-A.5.15-16-18-S4 (Access Review Process)

**Next Implementation Guide**: ISMS-IMP-A.5.15-16-18-S2 (Identity Lifecycle Process)