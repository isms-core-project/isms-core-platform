# ISMS-IMP-A.8.4-S1
## Repository Access Control Implementation
### Excel Workbook Layout Specification

**Document ID**: ISMS-IMP-A.8.4-S1  
**Assessment Area**: Repository Access Control and Compliance  
**Related Policy**: ISMS-POL-A.8.4-S2 (Source Code Access Control Policy)  
**Purpose**: Document repository inventory, access permissions, and access control compliance in a technology-independent manner

**Key Principle**: This assessment is **technology-agnostic**. Organizations document THEIR specific repository platforms (GitHub, GitLab, Bitbucket, Azure DevOps, self-hosted, etc.) and verify access controls against generic requirements.

---

## Implementation Overview

### Objectives

This implementation guide provides:
1. Step-by-step procedures for repository access control implementation
2. Excel workbook specification for documenting and assessing access compliance
3. Platform-specific guidance (GitHub, GitLab, Bitbucket, Azure DevOps)
4. Evidence collection requirements for audits

### Scope

- Repository inventory management
- User access provisioning and deprovisioning
- Access request and approval workflows
- Quarterly access reviews
- Access compliance assessment

---

## Section 1: Access Request and Approval Workflow

### 1.1 Access Request Process

**Step 1: Requestor Initiates Access Request**

The requestor (developer, contractor, auditor, etc.) submits an access request containing:

- **Requestor Information**:
  - Full name
  - Role/job title
  - Department/team
  - Employment type (employee, contractor, auditor)
  
- **Repository Information**:
  - Repository name(s)
  - Repository classification (production, internal tools, open source, archived)
  - Business justification for access
  
- **Access Level Requested**:
  - Read: View-only access
  - Write/Contributor: Clone, push, create branches, submit pull requests
  - Admin: Repository configuration, access management
  
- **Access Duration**:
  - Permanent (standard for employees)
  - Time-bound (standard for contractors, auditors)
  - Expected end date (for time-bound access)

**Request Submission Methods**:
- IT ticketing system (ServiceNow, Jira Service Management, etc.)
- Email to repository owner with standard template
- Access request form (Google Forms, Microsoft Forms, custom web form)
- Repository platform built-in request system (if available)

**Step 2: Repository Owner Reviews Request**

Repository owner or delegate reviews the access request:

- **Verification Checks**:
  - Requestor has legitimate business need
  - Access level is appropriate (least privilege)
  - Requestor's role justifies the requested access
  - No existing access or access level is correct
  - Request does not grant excessive permissions
  
- **Additional Approvals Required**:
  - Write access or higher: Development team lead approval
  - Admin access to production repositories: CISO or delegate approval
  - External contractor access: Contracting manager approval + NDA verification
  - Auditor access: Legal/compliance approval + time-bound restriction

**Step 3: Access Approval or Denial**

Repository owner makes decision:

- **If Approved**:
  - Document approval with timestamp and approver name
  - Forward to IT operations or DevOps for provisioning
  - Set access expiration date (if time-bound)
  - Retain approval record for audit (minimum 3 years)
  
- **If Denied**:
  - Document denial reason
  - Communicate denial to requestor
  - Suggest alternative (reduced access level, different repository, etc.)
  - Retain denial record

**Step 4: Access Provisioning**

IT operations or DevOps team provisions access:

- **Platform-Specific Provisioning**: (See Section 2 for detailed procedures)
  - Add user to repository with specified access level
  - Configure access expiration if time-bound
  - Verify access is granted correctly
  
- **Provisioning Timeframe**: Within 24 hours of approval during business hours
  
- **Provisioning Documentation**:
  - Log timestamp of access grant
  - Document user, repository, access level
  - Link to approval ticket/email

**Step 5: Access Confirmation**

Confirm access grant:

- Notify requestor that access has been granted
- Provide repository URL and access instructions
- Remind of security policies (no secrets in code, branch protection, etc.)
- Inform of access review schedule (quarterly)

### 1.2 Emergency Access Requests

For incident response or production emergencies:

**Emergency Process**:
1. Requestor clearly marks request as EMERGENCY
2. Repository owner or on-call manager approves verbally
3. Access is provisioned immediately (target: <1 hour)
4. Post-facto documentation completed within 48 hours:
   - Emergency justification
   - Written approval from repository owner
   - Access review (was emergency access appropriate?)
   - Access removal if temporary emergency need

---

## Section 2: Platform-Specific Access Provisioning

### 2.1 GitHub Access Provisioning

**Organization-Level Access**:
1. Navigate to Organization → Settings → Member privileges
2. Verify organization requires 2FA for all members
3. Add user to organization (if not already member)

**Repository-Level Access**:
1. Navigate to Repository → Settings → Collaborators and teams
2. Click "Add people" or "Add teams"
3. Search for user by username
4. Select access level:
   - **Read**: Can view and clone repository
   - **Triage**: Read + manage issues and PRs
   - **Write**: Read + push commits, create branches
   - **Maintain**: Write + manage repository settings (not recommended for standard developers)
   - **Admin**: Full repository control including deletion
5. Click "Add [username] to [repository]"
6. Verify user appears in collaborators list

**Time-Bound Access** (GitHub Enterprise):
- Use GitHub CLI or API to set access expiration
- Schedule automated access removal using cron job or GitHub Actions
- Document expiration date in access tracking spreadsheet

**Verification**:
- User receives invitation email
- User accepts invitation
- User appears in repository access list
- Access level is correct

### 2.2 GitLab Access Provisioning

**Project-Level Access**:
1. Navigate to Project → Settings → Members
2. Click "Invite members"
3. Enter username or email
4. Select role:
   - **Guest**: View-only (issues and wiki)
   - **Reporter**: Read repository code
   - **Developer**: Clone, push, create branches, submit merge requests
   - **Maintainer**: Manage project settings, protect branches
   - **Owner**: Full project control (rarely granted)
5. Set access expiration date (if time-bound)
6. Click "Invite"

**Group-Level Access** (for multiple projects):
1. Navigate to Group → Settings → Members
2. Add user to group with appropriate role
3. User inherits access to all projects in group
4. Set expiration if needed

**Verification**:
- User receives invitation email
- User appears in project members list
- Role is correct
- Expiration date is set (if applicable)

### 2.3 Bitbucket Access Provisioning

**Repository-Level Access** (Bitbucket Cloud):
1. Navigate to Repository → Repository settings → User and group access
2. Click "Add members"
3. Enter username or email
4. Select permission:
   - **Read**: View-only access
   - **Write**: Clone, push, create branches
   - **Admin**: Full repository control
5. Click "Add"

**Workspace-Level Access** (for multiple repositories):
1. Navigate to Workspace settings → User groups
2. Create or select group
3. Add user to group
4. Assign group to repositories with appropriate permission

**Time-Bound Access**:
- Bitbucket does not have native expiration
- Implement manual calendar reminder or automated script
- Document expiration in access tracking system

**Verification**:
- User appears in repository access list
- Permission level is correct

### 2.4 Azure DevOps Access Provisioning

**Project-Level Access**:
1. Navigate to Project Settings → Permissions
2. Click "Add" → "Add users"
3. Enter user email or select from Azure AD
4. Assign to security group:
   - **Readers**: View-only access
   - **Contributors**: Clone, push, create branches, create PRs
   - **Build Administrators**: Manage build pipelines
   - **Project Administrators**: Full project control
5. Click "Save changes"

**Repository-Specific Access**:
1. Navigate to Project Settings → Repositories → [Repository name] → Security
2. Add user or group
3. Set permissions:
   - Read: Allow
   - Contribute: Allow/Deny
   - Force push: Deny
   - Manage permissions: Deny
4. Save

**Time-Bound Access**:
- Azure DevOps does not have native expiration
- Implement automated PowerShell script for access review and removal
- Document expiration in tracking system

**Verification**:
- User can access project
- Repository appears in user's repository list
- Permissions are correct

---

## Section 3: Access Deprovisioning Procedures

### 3.1 Automated Deprovisioning (Ideal State)

**HR System Integration**:
1. HR system triggers "termination event" or "role change event"
2. Identity management system (Okta, Azure AD, etc.) receives event
3. IAM system automatically disables accounts:
   - Corporate SSO access to repository platforms
   - Direct repository platform accounts (if not SSO-integrated)
4. IAM system logs deprovisioning action
5. Verification report generated daily showing deprovisioned accounts

**Automation Implementation**:
- Use identity provider (IdP) lifecycle management
- Configure repository platform SCIM provisioning (if supported)
- Implement webhook from HR system to IAM system
- Schedule daily sync to catch any missed deprovisions

### 3.2 Manual Deprovisioning (Fallback Process)

**Trigger Events**:
- Employment termination
- Role change (access no longer needed)
- Contract expiration (contractors)
- Access review identifies unnecessary access
- Security incident involving account

**Deprovisioning Checklist**:

1. **Receive Notification**:
   - HR sends termination notification
   - Manager confirms last working day
   - IT receives deprovisioning request

2. **Identify Repository Access**:
   - Query repository platforms for user's access
   - Generate list of repositories user can access
   - Identify access level for each repository

3. **Remove Access** (per platform):
   - **GitHub**: Repository → Settings → Collaborators → Remove user
   - **GitLab**: Project → Members → Remove member
   - **Bitbucket**: Repository settings → User and group access → Remove
   - **Azure DevOps**: Project Settings → Permissions → Remove user from groups

4. **Verify Removal**:
   - User no longer appears in repository collaborator lists
   - User cannot access repositories (test if possible)
   - Document verification timestamp

5. **Document Deprovisioning**:
   - Log user, repositories, removal date, actor
   - Retain for audit (3 years minimum)

**Deprovisioning Timeline**: Within 24 hours of termination notification

### 3.3 Contractor Access Expiration

**Automatic Expiration** (if platform supports):
- GitHub Enterprise: Use API to set expiration dates
- GitLab: Built-in expiration date feature
- Bitbucket: Manual tracking required
- Azure DevOps: Manual tracking required

**Manual Expiration Tracking**:
1. Maintain contractor access inventory with expiration dates
2. Set calendar reminders 7 days before expiration
3. Contact contracting manager to confirm renewal or expiration
4. If not renewed, remove access on expiration date
5. Document removal

**Expired Access Remediation**:
- Weekly report of contractor access past expiration date
- Immediate removal of expired access
- Investigation if access was not removed timely

---

## Section 4: Quarterly Access Reviews

### 4.1 Access Review Schedule

**Review Frequency**: Quarterly for all repositories

**Review Timeline**:
- Q1 review: January (covers Q4 previous year)
- Q2 review: April (covers Q1 current year)
- Q3 review: July (covers Q2 current year)
- Q4 review: October (covers Q3 current year)

**Repository Prioritization**:
1. Production code repositories (highest priority)
2. Customer-facing applications
3. Internal tools with sensitive data access
4. Infrastructure-as-Code repositories
5. Other repositories

### 4.2 Access Review Procedure

**Step 1: Generate Access Report**

Repository owner or designated reviewer:
1. Export current access list from repository platform
2. Include: username, access level, last access date (if available), role/team
3. Compare against previous quarter's access list
4. Identify changes (new users, removed users, access level changes)

**Step 2: Verify Business Need**

For each user with access:
1. Confirm user still requires access (current role, current projects)
2. Verify access level is appropriate (not excessive)
3. Check if user has accessed repository recently (if last access data available)
4. Identify orphaned accounts (former employees still listed)
5. Identify excessive access (users with access to many repositories unnecessarily)

**Step 3: Document Findings**

Create access review report:
- **Appropriate Access**: User requires access, access level correct
- **Excessive Access**: User has higher access level than needed (e.g., admin when write would suffice)
- **Unnecessary Access**: User no longer needs access (role change, project completed)
- **Orphaned Account**: Former employee still has access
- **Contractor Expired**: Contractor access past contract end date

**Step 4: Remediate Findings**

- **Excessive Access**: Reduce access level within 14 days
- **Unnecessary Access**: Remove access within 14 days
- **Orphaned Account**: Remove immediately (within 24 hours)
- **Contractor Expired**: Remove immediately (within 24 hours)

**Step 5: Complete Review Documentation**

Document:
- Review date
- Reviewer name and role
- Repositories reviewed
- Total users reviewed
- Findings count by category
- Remediation actions taken
- Remediation completion date
- Next review date

**Step 6: Submit Review Results**

- Submit review completion report to Information Security Manager
- Include findings and remediation evidence
- Update access review tracking dashboard

### 4.3 Access Review Automation

**Automation Opportunities**:
- Automated access report generation from repository platforms
- Comparison against HR system for orphaned account detection
- Automated notifications to repository owners when review due
- Dashboard showing review completion status

**Tools**:
- GitHub API for access reports
- GitLab API for project member exports
- Python scripts for cross-referencing with HR data
- Excel/Google Sheets for review tracking

---

## Section 5: Excel Workbook Specification

### Workbook Structure

**Sheet 1: Instructions & Legend**

#### Header Section
- **Title**: "ISMS-IMP-A.8.4.1 – Repository Access Control Assessment"
- **Subtitle**: "ISO/IEC 27001:2022 - Control A.8.4: Access to Source Code"
- **Styling**: Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```
Document ID:           ISMS-IMP-A.8.4.1
Assessment Area:       Repository Access Control
Related Policy:        ISMS-POL-A.8.4-S2
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

#### How to Use This Workbook
1. Complete the Repository_Inventory sheet for ALL source code repositories
2. Fill in the User_Access_Matrix sheet showing who has access to what
3. Document all access requests and approvals in Access_Approval_Records
4. Track quarterly access reviews in Access_Review_Log
5. The Compliance_Scoring sheet automatically calculates compliance metrics
6. Document gaps in Gap_Analysis with remediation plans
7. Maintain Evidence_Register for audit traceability
8. Obtain final approval and sign-off

#### Status Legend
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Appropriate | Access is justified and appropriate | Green (C6EFCE) |
| ⚠️ | Excessive | User has higher access than needed | Yellow (FFEB9C) |
| ❌ | Orphaned | Former employee still has access | Red (FFC7CE) |
| 📅 | Expired | Contractor access past contract end | Red (FFC7CE) |
| ✔️ | Remediated | Finding has been addressed | Blue (B4C7E7) |

#### Acceptable Evidence
- ✓ Repository platform access reports (exports from GitHub, GitLab, etc.)
- ✓ Access request tickets and approval emails
- ✓ NDA signature records for personnel with code access
- ✓ Contractor contracts showing access periods
- ✓ Access review completion reports
- ✓ Deprovisioning logs showing timely access removal
- ✓ User-to-repository access matrix
- ✓ HR termination records correlated with access removal

---

**Sheet 2: Repository_Inventory**

### Purpose
Complete inventory of all source code repositories across all platforms.

### Header Section
**Row 1**: "REPOSITORY INVENTORY"  
**Row 2**: "Document all source code repositories regardless of platform"

### Column Definitions

| Column | Field Name | Type | Description |
|--------|-----------|------|-------------|
| A | Repository Name | Text | Full repository name |
| B | Repository URL | Text | Complete URL to repository |
| C | Repository Platform | Dropdown | GitHub, GitLab, Bitbucket, Azure DevOps, Self-Hosted Git, Perforce, SVN, Other |
| D | Repository Classification | Dropdown | Production Code, Internal Tools, Open Source, Archived/Deprecated |
| E | Repository Owner | Text | Name of person responsible for repository |
| F | Repository Owner Email | Email | Contact email |
| G | Business Purpose | Text | What is this repository used for? |
| H | Primary Programming Language | Dropdown | Python, Java, JavaScript, C#, Go, Ruby, PHP, TypeScript, C++, Other |
| I | Last Commit Date | Date | Date of most recent code commit |
| J | Active/Inactive Status | Dropdown | Active, Archived, Deprecated, Planned |
| K | Total Contributors | Number | Count of users with write access |
| L | Total Commits (Lifetime) | Number | Total commit count |
| M | Repository Creation Date | Date | When was repository created? |
| N | Criticality | Dropdown | Critical, High, Medium, Low |
| O | Contains Production Code | Dropdown | Yes, No |
| P | Contains Sensitive Data | Dropdown | Yes, No, Unknown |
| Q | Branch Protection Enabled | Dropdown | ✅ Yes, ❌ No, ⚠️ Partial |
| R | Secret Scanning Enabled | Dropdown | ✅ Yes, ❌ No |
| S | Last Access Review Date | Date | Most recent quarterly review |
| T | Notes | Text | Additional information |

### Data Validation
- Repository Platform: List of common platforms
- Repository Classification: Fixed list per policy
- Active/Inactive Status: Fixed status list
- Criticality: Fixed risk levels
- Yes/No fields: Standardized with emoji indicators

### Conditional Formatting
- Repository Classification:
  - Production Code: Red background
  - Internal Tools: Yellow background
  - Open Source: Blue background
  - Archived: Gray background
- Last Access Review Date:
  - >90 days ago: Red (overdue)
  - 60-90 days ago: Yellow (due soon)
  - <60 days: Green (current)

---

**Sheet 3: User_Access_Matrix**

### Purpose
Document which users have access to which repositories and at what level.

### Header Section
**Row 1**: "USER ACCESS MATRIX"  
**Row 2**: "Document all user access to repositories"

### Column Definitions

| Column | Field Name | Type | Description |
|--------|-----------|------|-------------|
| A | User Name | Text | Full name of user |
| B | User Email | Email | Corporate email |
| C | User Role | Dropdown | Developer, Security Team, Auditor, External Contractor, Repository Admin, Service Account |
| D | Employment Type | Dropdown | Employee, Contractor, Auditor, Automated System |
| E | Department/Team | Text | Organizational unit |
| F | Repository Name | Text | Repository user has access to |
| G | Repository Platform | Dropdown | GitHub, GitLab, Bitbucket, Azure DevOps, Other |
| H | Access Level | Dropdown | Read, Write/Contribute, Admin |
| I | Access Granted Date | Date | When was access first granted? |
| J | Access Approved By | Text | Who approved the access? |
| K | Business Justification | Text | Why does user need access? |
| L | Contract End Date | Date | For contractors - when does contract end? |
| M | Access Expiration Date | Date | For time-bound access |
| N | Last Access Date | Date | When did user last interact with repository? |
| O | Access Status | Dropdown | ✅ Appropriate, ⚠️ Excessive, ❌ Orphaned, 📅 Expired, ✔️ Remediated |
| P | Last Review Date | Date | Most recent access review |
| Q | Reviewer Comments | Text | Comments from access review |
| R | Remediation Required | Dropdown | Yes, No |
| S | Remediation Due Date | Date | When must remediation be completed? |
| T | Notes | Text | Additional information |

### Formulas
- Access Status (automated):
  - If User Email not in HR active list → ❌ Orphaned
  - If Contract End Date < Today → 📅 Expired
  - If Access Level = Admin and Role ≠ Repository Admin → ⚠️ Excessive
  - Else → ✅ Appropriate

### Conditional Formatting
- Access Status:
  - ✅ Appropriate: Green
  - ⚠️ Excessive: Yellow
  - ❌ Orphaned: Red
  - 📅 Expired: Red
- Last Access Date:
  - >180 days: Red (inactive user)
  - 90-180 days: Yellow (rarely used)
  - <90 days: Green (active)

---

**Sheet 4: Access_Approval_Records**

### Purpose
Document all access request approvals for audit trail.

### Column Definitions

| Column | Field Name | Type | Description |
|--------|-----------|------|-------------|
| A | Request Date | Date | When was access requested? |
| B | Request ID | Text | Ticket number or reference |
| C | Requestor Name | Text | Who requested access? |
| D | Requestor Email | Email | Requestor contact |
| E | Repository Name | Text | Repository access requested for |
| F | Access Level Requested | Dropdown | Read, Write, Admin |
| G | Business Justification | Text | Why is access needed? |
| H | Expected Duration | Dropdown | Permanent, Time-Bound |
| I | Expected End Date | Date | For time-bound access |
| J | Repository Owner | Text | Who reviewed the request? |
| K | Owner Approval | Dropdown | ✅ Approved, ❌ Denied, ⏳ Pending |
| L | Approval Date | Date | When was decision made? |
| M | Additional Approver | Text | For admin access (CISO, etc.) |
| N | Additional Approval | Dropdown | ✅ Approved, ❌ Denied, ➖ N/A |
| O | Provisioning Date | Date | When was access actually granted? |
| P | Provisioned By | Text | Who granted the access? |
| Q | Denial Reason | Text | If denied, why? |
| R | Notes | Text | Additional information |

### Metrics (Calculated)
- Total requests this quarter
- Approval rate (% approved)
- Average time to provision (Provisioning Date - Approval Date)
- Pending requests (for follow-up)

---

**Sheet 5: Access_Review_Log**

### Purpose
Track quarterly access reviews for all repositories.

### Column Definitions

| Column | Field Name | Type | Description |
|--------|-----------|------|-------------|
| A | Review Date | Date | When was review conducted? |
| B | Review Quarter | Text | Q1 2026, Q2 2026, etc. |
| C | Reviewer Name | Text | Who conducted the review? |
| D | Reviewer Role | Text | Repository owner, security manager, etc. |
| E | Repositories Reviewed | Number | Count of repositories |
| F | Repository Names | Text | List of repositories (or "See detail sheet") |
| G | Total Users Reviewed | Number | Count of users with access |
| H | Appropriate Access Found | Number | Count of appropriate access |
| I | Excessive Access Found | Number | Count of excessive access |
| J | Unnecessary Access Found | Number | Count of unnecessary access |
| K | Orphaned Accounts Found | Number | Former employees |
| L | Contractor Expired Found | Number | Contractors past contract end |
| M | Total Findings | Number | Sum of all finding types |
| N | Remediation Completed | Number | Count of findings addressed |
| O | Remediation Pending | Number | Count of findings not yet addressed |
| P | Review Completion Date | Date | When was review finalized? |
| Q | Days to Complete | Number | Review Date to Completion Date |
| R | Next Review Due Date | Date | Review Date + 90 days |
| S | Compliance Status | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |
| T | Notes | Text | Reviewer comments |

### Conditional Formatting
- Compliance Status: Green/Yellow/Red by status
- Remediation Pending: Red if >0
- Next Review Due Date: Red if <today (overdue)

---

**Sheet 6: Deprovisioning_Log**

### Purpose
Track access removal for audit trail.

### Column Definitions

| Column | Field Name | Type | Description |
|--------|-----------|------|-------------|
| A | User Name | Text | Who lost access? |
| B | User Email | Email | User contact |
| C | Deprovisioning Event | Dropdown | Termination, Role Change, Contract End, Access Review, Security Incident |
| D | Event Date | Date | Termination date, contract end, etc. |
| E | Notification Received Date | Date | When was IT notified? |
| F | Repository Name | Text | Repository access removed from |
| G | Previous Access Level | Dropdown | Read, Write, Admin |
| H | Access Removed Date | Date | When was access actually removed? |
| I | Hours to Deprovision | Number | Event Date to Removed Date (hours) |
| J | Removed By | Text | Who removed the access? |
| K | Removal Method | Dropdown | Automated, Manual |
| L | Verification Method | Dropdown | Platform Check, Login Test, API Query |
| M | Verification Date | Date | When was removal confirmed? |
| N | Compliant Timeline | Dropdown | ✅ Yes (<24 hours), ❌ No (>24 hours) |
| O | Delay Reason | Text | If >24 hours, why? |
| P | Notes | Text | Additional information |

### Metrics (Calculated)
- Average time to deprovision (target: <24 hours)
- % deprovisioned within SLA (<24 hours)
- Total deprovisions this quarter
- Automated vs manual deprovisioning rate

---

**Sheet 7: Compliance_Scoring**

### Purpose
Calculate compliance metrics based on assessment data.

### Metrics Calculated

#### Repository Inventory Compliance
```
Formula: (Repositories in inventory / Total repositories in platform) × 100%
Target: 100%
Data Source: Compare Repository_Inventory sheet against platform exports
```

#### Access Control Compliance
```
Formula: (Repositories with access control / Total repositories) × 100%
Target: 100%
Data Source: Repository_Inventory sheet, Column Q (Branch Protection)
```

#### Appropriate Access Rate
```
Formula: (Appropriate access grants / Total access grants) × 100%
Target: ≥95%
Data Source: User_Access_Matrix sheet, Column O (Access Status)
Count: ✅ Appropriate / Total rows
```

#### Orphaned Account Rate
```
Formula: (Orphaned accounts / Total users with access) × 100%
Target: 0%
Data Source: User_Access_Matrix sheet, Column O (Access Status)
Count: ❌ Orphaned / Total users
```

#### Access Review Completion Rate
```
Formula: (Reviews completed on time / Total reviews due) × 100%
Target: 100%
Data Source: Access_Review_Log sheet
Count: Reviews with Completion Date ≤ Review Date + 30 days
```

#### Deprovisioning SLA Compliance
```
Formula: (Deprovisions within 24 hours / Total deprovisions) × 100%
Target: ≥95%
Data Source: Deprovisioning_Log sheet, Column N (Compliant Timeline)
Count: ✅ Yes / Total deprovisions
```

#### Overall Repository Access Compliance Score
```
Formula: 
  (Repository Inventory Compliance × 15%) +
  (Access Control Compliance × 20%) +
  (Appropriate Access Rate × 25%) +
  ((100% - Orphaned Account Rate) × 15%) +
  (Access Review Completion Rate × 15%) +
  (Deprovisioning SLA Compliance × 10%)

Target: ≥85%
```

### Scoring Dashboard

| Metric | Current Score | Target | Status |
|--------|--------------|--------|---------|
| Repository Inventory | [Formula] | 100% | [🟢/🟡/🔴] |
| Access Control | [Formula] | 100% | [🟢/🟡/🔴] |
| Appropriate Access | [Formula] | ≥95% | [🟢/🟡/🔴] |
| Orphaned Accounts | [Formula] | 0% | [🟢/🟡/🔴] |
| Review Completion | [Formula] | 100% | [🟢/🟡/🔴] |
| Deprovisioning SLA | [Formula] | ≥95% | [🟢/🟡/🔴] |
| **OVERALL SCORE** | **[Formula]** | **≥85%** | **[🟢/🟡/🔴]** |

### Risk Categorization
- 🟢 Low Risk: Score ≥85%
- 🟡 Medium Risk: Score 70-84%
- 🔴 High Risk: Score <70%

---

**Sheet 8: Gap_Analysis**

### Purpose
Document identified gaps and remediation plans.

### Column Definitions

| Column | Field Name | Type | Description |
|--------|-----------|------|-------------|
| A | Gap ID | Text | Unique identifier (GAP-001, GAP-002, etc.) |
| B | Gap Category | Dropdown | Access Control, Inventory, Reviews, Deprovisioning, Documentation |
| C | Gap Description | Text | What is the gap? |
| D | Policy Requirement | Text | Which policy requirement is not met? |
| E | Current State | Text | What is happening now? |
| F | Desired State | Text | What should be happening? |
| G | Risk Level | Dropdown | 🔴 Critical, 🟠 High, 🟡 Medium, 🟢 Low |
| H | Impact | Text | What is the impact of this gap? |
| I | Affected Repositories | Text | Which repositories are affected? |
| J | Root Cause | Text | Why does this gap exist? |
| K | Remediation Plan | Text | How will gap be closed? |
| L | Responsible Party | Text | Who will fix it? |
| M | Target Completion Date | Date | When will gap be closed? |
| N | Estimated Effort | Dropdown | 1-2 hours, 1 day, 1 week, 2-4 weeks, >1 month |
| O | Status | Dropdown | 🔴 Open, 🟡 In Progress, 🟢 Completed, ⚪ Deferred |
| P | Actual Completion Date | Date | When was gap actually closed? |
| Q | Verification Method | Text | How was closure verified? |
| R | Verification Date | Date | When was verification completed? |
| S | Notes | Text | Additional information |

### Conditional Formatting
- Risk Level: Color-coded (red/orange/yellow/green)
- Status: Color-coded
- Target Completion Date: Red if overdue

---

**Sheet 9: Evidence_Register**

### Purpose
Track evidence collected for audit purposes.

### Column Definitions

| Column | Field Name | Type | Description |
|--------|-----------|------|-------------|
| A | Evidence ID | Text | Unique identifier (EV-001, EV-002, etc.) |
| B | Evidence Type | Dropdown | Access Report, Approval Record, Review Report, Deprovisioning Log, Configuration Screenshot, Other |
| C | Evidence Description | Text | What is this evidence? |
| D | Related Requirement | Text | Which policy requirement does this support? |
| E | Evidence Date | Date | When was evidence created? |
| F | Evidence Source | Text | Where did evidence come from? (GitHub export, ticket system, etc.) |
| G | File Name | Text | Name of evidence file |
| H | File Location | Text | Where is file stored? (SharePoint, drive, etc.) |
| I | Collected By | Text | Who collected the evidence? |
| J | Collection Date | Date | When was evidence collected? |
| K | Evidence Format | Dropdown | Excel, PDF, CSV, Screenshot, Email, JSON, Other |
| L | Retention Period | Text | How long must evidence be retained? |
| M | Retention End Date | Date | When can evidence be purged? |
| N | Auditor Reviewed | Dropdown | ✅ Yes, ❌ No, ⏳ Pending |
| O | Auditor Comments | Text | Auditor notes |
| P | Notes | Text | Additional information |

### Evidence Categories
- Access reports (user-to-repository matrix exports)
- Approval records (tickets, emails)
- Review completion reports (quarterly reviews)
- Deprovisioning logs (access removal records)
- Configuration screenshots (branch protection, MFA enforcement)
- Training records (developer security training)
- NDA signatures (confidentiality agreements)

---

**Sheet 10: Approval_Sign_Off**

### Purpose
Final approval and sign-off for assessment completion.

### Sign-Off Section

```
ASSESSMENT COMPLETION CERTIFICATION

I certify that this repository access control assessment has been completed in accordance with ISMS-POL-A.8.4 requirements and that the information documented herein is accurate to the best of my knowledge.

Assessment Period: [Quarter/Year]
Assessment Completion Date: [Date]
Overall Compliance Score: [Calculated from Compliance_Scoring sheet]

APPROVALS:

Repository Owners:
Name: ________________  Signature: ________________  Date: ______
Name: ________________  Signature: ________________  Date: ______
Name: ________________  Signature: ________________  Date: ______

Information Security Manager:
Name: ________________  Signature: ________________  Date: ______

Chief Information Security Officer (CISO):
Name: ________________  Signature: ________________  Date: ______

Next Scheduled Review: [Completion Date + 90 days]
```

---

## Section 6: Evidence Collection for Audits

### Required Evidence

**Repository Inventory Evidence**:
- Repository platform exports (GitHub org repositories, GitLab projects, etc.)
- Repository metadata (classification, owner, purpose)
- Inventory review records (quarterly updates)

**Access Control Evidence**:
- User-to-repository access matrix (exported from platforms)
- Access request tickets with approvals
- NDA signature records for all personnel with code access
- Contractor contracts showing access periods

**Access Review Evidence**:
- Quarterly access review completion reports
- Finding documentation (excessive access, orphaned accounts)
- Remediation records showing timely fixes
- Before/after access reports

**Deprovisioning Evidence**:
- HR termination records
- Access removal logs with timestamps
- Verification of access removal
- Automated deprovisioning system logs (if applicable)

**Compliance Evidence**:
- Compliance scoring calculations
- Trend analysis (improvements over time)
- Exception records (if any)
- Gap remediation completion

---

**END OF IMPLEMENTATION GUIDE**

**Related Documents**:
- ISMS-POL-A.8.4-S2 (Access Control Policy Requirements)
- ISMS-POL-A.8.4-S3 (Assessment and Evidence Framework)
- ISMS-IMP-A.8.4-S2 (Branch Protection Configuration)
- ISMS-IMP-A.8.4-S3 (Source Code Access Assessment Procedures)
