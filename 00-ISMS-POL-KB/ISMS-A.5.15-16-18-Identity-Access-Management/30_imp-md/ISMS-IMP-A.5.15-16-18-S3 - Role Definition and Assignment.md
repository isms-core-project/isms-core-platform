# ISMS-IMP-A.5.15-16-18-S3: Role Definition and Assignment
## Implementation Guide for RBAC Framework

**Document ID**: ISMS-IMP-A.5.15-16-18-S3  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: IAM Manager / Security Team  
**Status**: Active

---

## Document Purpose

This implementation guide provides **step-by-step procedures** for implementing role-based access control (RBAC) in accordance with ISO/IEC 27001:2022 Controls A.5.15 and A.5.18. It covers role catalog development, role assignment procedures, group management, and RBAC adoption.

**Target Audience**: IAM team, security team, business analysts, system owners

**Prerequisites**:
- Access control governance established (IMP-S1)
- User type classification implemented
- System criticality classification completed
- Identity systems operational

---

## 1. RBAC Fundamentals

### 1.1 What is Role-Based Access Control?

**RBAC Definition**: Access control approach where permissions are assigned to roles rather than individual users.

**Traditional Approach (Direct Access)**:
```
User Alice → Finance System (Read/Write access)
User Bob → Finance System (Read/Write access)  
User Carol → Finance System (Read/Write access)

Problem: Must provision each user individually
```

**RBAC Approach**:
```
Role: Finance Analyst → Finance System (Read/Write access)

User Alice → Finance Analyst role
User Bob → Finance Analyst role
User Carol → Finance Analyst role

Benefit: Provision role once, assign users to role
```

**RBAC Benefits**:
- **Consistency**: All users in same role have same access
- **Efficiency**: Provision role once, not per user
- **Scalability**: Easy to add/remove users from roles
- **Auditability**: Clear mapping of role → access → users
- **Compliance**: Easier to demonstrate access control

---

### 1.2 RBAC vs Direct Access

| Aspect | Direct Access | RBAC |
|--------|--------------|------|
| **Provisioning** | Per user | Per role (once) |
| **Consistency** | Varies by user | Standardized by role |
| **Audit** | User-by-user review | Role-based review |
| **Scalability** | Manual per user | Automatic via role assignment |
| **Example** | Alice gets CRM Read/Write | Alice assigned "Sales Rep" role → gets CRM Read/Write |

**Recommendation**: Migrate from direct access to RBAC over time.

---

## 2. Role Catalog Development

### 2.1 Role Identification

**Objective**: Identify standard roles based on job functions.

**Step 1: Business Analysis**

**Interview Questions** (for department heads):
1. What are the distinct job functions in your department?
2. What systems/data does each job function need access to?
3. Are there different levels within the same job function? (junior, senior)
4. What access do new hires in each role typically need?

**Example Interview** (Sales Department):

**Q**: What job functions exist in Sales?  
**A**: Sales Representative, Sales Manager, Sales Operations

**Q**: What systems does each role need?  
**A**:
- Sales Rep: CRM (Read/Write customer records), Sales folder (Read/Write)
- Sales Manager: CRM (Read/Write + manager view), Sales folder (Read/Write/Delete), Commission system (Read)
- Sales Operations: CRM (Admin), Sales folder (Admin), Commission system (Read/Write)

**Output**: List of roles per department

---

**Step 2: Role Consolidation**

**Identify Common Roles Across Departments**:
- Standard User (all employees)
- Department-Specific Roles (Finance Analyst, Sales Rep, HR Generalist)
- Cross-Functional Roles (Project Manager, Executive)
- Technical Roles (Developer, System Administrator, Security Analyst)

**Example Role List** (50-person company):

| Role Name | Department | Job Functions | User Count (approx) |
|-----------|------------|---------------|-------------------|
| **Standard User** | All | Email, calendar, intranet | All (50) |
| **Finance Analyst** | Finance | Accounting, AP/AR | 5 |
| **Finance Manager** | Finance | Financial reporting, approvals | 1 |
| **Sales Representative** | Sales | Customer management, deals | 15 |
| **Sales Manager** | Sales | Team management, forecasting | 2 |
| **HR Generalist** | HR | Employee records, recruiting | 2 |
| **Software Developer** | Engineering | Code, development tools | 10 |
| **Engineering Manager** | Engineering | Code review, project management | 2 |
| **IT Administrator** | IT | System administration | 2 |
| **Security Analyst** | Security | Security monitoring, incident response | 1 |
| **Executive** | Leadership | All systems (read-only for visibility) | 5 |

**Total Roles Defined**: 11 roles

**Rule of Thumb**: 
- Small company (10-50 employees): 5-15 roles
- Medium company (50-200 employees): 15-30 roles
- Large company (200+ employees): 30-50 roles

---

### 2.2 Role Description Documentation

**Objective**: Document each role with clear description and purpose.

**Role Documentation Template**:

```markdown
## Role: [Role Name]

**Role ID**: [Unique identifier, e.g., ROLE-001]  
**Department**: [Department or "Cross-functional"]  
**Description**: [1-2 sentence description of role purpose]  
**Job Functions**: [Bullet list of job functions this role performs]  
**Typical Job Titles**: [Examples: "Sales Representative", "Account Executive"]  
**User Count**: [Approximate number of users in this role]  
**Owner**: [Person responsible for role definition, typically department head]  
**Last Reviewed**: [Date role definition was last reviewed]  
**Status**: [Active | Under Review | Deprecated]

### Access Granted by This Role

**Systems/Applications**:
1. [System Name] - [Access Level: Read | Write | Admin]
   - Justification: [Why this role needs this access]
   
2. [System Name] - [Access Level]
   - Justification: [...]

**Data/Folders**:
1. [Folder/Dataset Name] - [Access Level]
   - Justification: [...]

**Groups**:
1. [Group Name] - [Purpose of group]

### Assignment Criteria

Users are assigned this role when:
- [ ] Job title matches: [List of job titles]
- [ ] Department is: [Department name]
- [ ] Manager approval: [Required | Not required]
- [ ] Special justification: [Any special circumstances]

### Review Process

- **Review Frequency**: [Quarterly | Semi-annual | Annual]
- **Reviewer**: [Role owner, department head]
- **Review Checks**: 
  - [ ] Access mappings still accurate
  - [ ] No excessive access (least privilege)
  - [ ] Users assigned to role still appropriate
```

---

**Example Role Documentation**:

```markdown
## Role: Sales Representative

**Role ID**: ROLE-SALES-REP  
**Department**: Sales  
**Description**: Manages customer relationships, creates opportunities, closes deals  
**Job Functions**: 
- Customer relationship management
- Opportunity tracking
- Quote generation
- Order entry  
**Typical Job Titles**: Sales Representative, Account Executive, Business Development Representative  
**User Count**: 15  
**Owner**: VP Sales  
**Last Reviewed**: 2026-01-01  
**Status**: Active

### Access Granted by This Role

**Systems/Applications**:
1. CRM (Salesforce) - Read/Write
   - Justification: Core job function - manage customers, opportunities, deals
   
2. Sales Portal - Read
   - Justification: Access product information, pricing
   
3. Email & Calendar - Read/Write
   - Justification: Standard communication tools

**Data/Folders**:
1. Sales Shared Folder - Read/Write
   - Justification: Access sales collateral, templates, shared documents

**Groups**:
1. Sales Team Distribution List
   - Purpose: Email distribution for sales team communications

### Assignment Criteria

Users are assigned this role when:
- [x] Job title matches: Sales Representative, Account Executive
- [x] Department is: Sales
- [x] Manager approval: Required (Sales Manager)
- [ ] Special justification: None

### Review Process

- **Review Frequency**: Annual
- **Reviewer**: VP Sales
- **Review Checks**: 
  - [ ] CRM access level appropriate (Read/Write, not Admin)
  - [ ] No access to systems outside sales function
  - [ ] Users still in sales role
```

---

### 2.3 Role-to-Access Mapping

**Objective**: Document exactly what access each role grants.

**Role Access Matrix Template**:

| System/Application | Access Level | Granted by Role | Justification |
|-------------------|--------------|-----------------|---------------|
| CRM | Read/Write | Sales Representative | Core job function |
| CRM | Admin | Sales Operations | System administration |
| Finance System | Read | Finance Analyst | Transaction review |
| Finance System | Write | Finance Manager | Transaction approval |
| HR System | Read/Write | HR Generalist | Employee record management |
| Email | Read/Write | Standard User | All employees need email |

**Consolidated Role Access Matrix** (Excel/database):
- Rows: Roles
- Columns: Systems
- Cells: Access Level (blank = no access)

**Example**:

| Role | CRM | Finance | HR | Email | Intranet |
|------|-----|---------|----|----|----------|
| **Sales Rep** | Read/Write | - | - | Read/Write | Read |
| **Finance Analyst** | Read | Read/Write | - | Read/Write | Read |
| **HR Generalist** | Read | - | Read/Write | Read/Write | Read |
| **IT Admin** | Admin | Admin | Admin | Read/Write | Admin |
| **Standard User** | - | - | - | Read/Write | Read |

**Purpose**: 
- Visualize access granted by roles
- Identify excessive access (role has access it doesn't need)
- Identify gaps (role missing access it needs)

---

## 3. RBAC Implementation

### 3.1 Create Roles in Identity System

**Objective**: Create role definitions in identity systems (AD, Azure AD, Okta).

**Implementation varies by identity system**:

---

**Option A: Active Directory Groups (On-Premises)**

**Approach**: Use AD groups to represent roles.

**Step 1: Create AD Groups for Roles**
```powershell
# Create AD group for role
New-ADGroup -Name "ROLE-Sales-Representative" `
  -GroupScope Global `
  -GroupCategory Security `
  -Description "Sales Representative role - grants CRM access" `
  -Path "OU=Roles,DC=company,DC=com"

# Create AD group for each role
New-ADGroup -Name "ROLE-Finance-Analyst" -GroupScope Global -GroupCategory Security -Path "OU=Roles,DC=company,DC=com"
New-ADGroup -Name "ROLE-HR-Generalist" -GroupScope Global -GroupCategory Security -Path "OU=Roles,DC=company,DC=com"
# ... etc for all roles
```

**Step 2: Grant Group Access to Systems**
```powershell
# Example: Grant CRM access to Sales Rep role group
# This varies by application - some use AD groups directly, others sync from AD

# Add group to application ACL (example for file share)
$Acl = Get-Acl "\\fileserver\sales"
$Permission = "COMPANY\ROLE-Sales-Representative","FullControl","Allow"
$AccessRule = New-Object System.Security.AccessControl.FileSystemAccessRule $Permission
$Acl.SetAccessRule($AccessRule)
Set-Acl "\\fileserver\sales" $Acl
```

**Step 3: Add Users to Role Groups**
```powershell
# Add user to role group
Add-ADGroupMember -Identity "ROLE-Sales-Representative" -Members "alice.smith"

# Bulk add users (from CSV)
Import-Csv users.csv | ForEach-Object {
  Add-ADGroupMember -Identity $_.Role -Members $_.Username
}
```

---

**Option B: Azure AD Groups (Cloud)**

**Approach**: Use Azure AD groups to represent roles.

**Step 1: Create Azure AD Groups**
```powershell
# Connect to Azure AD
Connect-AzureAD

# Create Azure AD group for role
New-AzureADGroup -DisplayName "ROLE-Sales-Representative" `
  -MailEnabled $false `
  -SecurityEnabled $true `
  -MailNickName "SalesRepRole" `
  -Description "Sales Representative role"
```

**Step 2: Assign Group to Applications**
- Azure Portal → Enterprise Applications → [App] → Users and groups → Add user/group
- Assign "ROLE-Sales-Representative" group to Salesforce (example)

**Step 3: Add Users to Groups**
```powershell
# Get user object ID
$user = Get-AzureADUser -SearchString "alice.smith@company.com"

# Get group object ID  
$group = Get-AzureADGroup -SearchString "ROLE-Sales-Representative"

# Add user to group
Add-AzureADGroupMember -ObjectId $group.ObjectId -RefObjectId $user.ObjectId
```

---

**Option C: Okta Groups (Cloud Identity Platform)**

**Approach**: Use Okta groups to represent roles.

**Step 1: Create Okta Groups** (via Admin Console)
- Admin Console → Directory → Groups → Add Group
- Name: "ROLE-Sales-Representative"
- Description: "Sales Representative role"

**Step 2: Assign Group to Applications**
- Admin Console → Applications → [App] → Assignments → Assign to Groups
- Select "ROLE-Sales-Representative" group

**Step 3: Add Users to Groups**
- Admin Console → Directory → People → [User] → Groups → Edit
- Add user to "ROLE-Sales-Representative" group

---

### 3.2 Role Assignment Procedures

**Objective**: Define how users are assigned to roles.

**Assignment Triggers**:
1. **New Hire**: Assign role based on job title (automated)
2. **Role Change**: Assign new role, remove old role (automated or manual)
3. **Special Request**: User requests additional role (approval workflow)

---

**Procedure 1: Automatic Role Assignment (New Hire)**

**Trigger**: New employee record in HR system

**Process**:
```
HR System: New employee added (Job Title = "Sales Representative")
  ↓
IAM System: Detects new employee
  ↓
IAM System: Looks up job title → role mapping
  ↓
IAM System: Job Title "Sales Representative" maps to "ROLE-Sales-Representative"
  ↓
IAM System: Assigns user to "ROLE-Sales-Representative" group
  ↓
User gains access automatically (CRM, Sales folder, etc.)
```

**Job Title → Role Mapping Table**:

| Job Title (in HR) | Role (in IAM) |
|-------------------|---------------|
| Sales Representative | ROLE-Sales-Representative |
| Account Executive | ROLE-Sales-Representative |
| Sales Manager | ROLE-Sales-Manager |
| Financial Analyst | ROLE-Finance-Analyst |
| Finance Manager | ROLE-Finance-Manager |
| HR Generalist | ROLE-HR-Generalist |
| Software Developer | ROLE-Software-Developer |
| IT Administrator | ROLE-IT-Administrator |

**Implementation** (pseudo-code):
```python
def assign_role_on_hire(employee):
  job_title = employee.job_title
  role = lookup_role_for_job_title(job_title)
  
  if role:
    assign_user_to_role(employee.username, role)
    log(f"Assigned {employee.username} to {role} based on job title {job_title}")
  else:
    send_alert(f"No role mapping for job title: {job_title}. Manual assignment needed.")
```

---

**Procedure 2: Manual Role Assignment (Special Request)**

**Trigger**: User requests access that's not part of their default role

**Process**:
```
User submits access request (ServiceNow ticket)
  ↓
Ticket routes to manager for approval
  ↓
Manager approves: "User needs temporary access to Finance reports for project"
  ↓
IAM team reviews: Should we assign Finance role or grant direct access?
  ↓
Decision: Assign to existing role (if access aligns with role definition)
  OR: Grant direct access (if temporary/special need)
  ↓
IAM provisions access
```

**Decision Criteria** (Role vs Direct Access):

| Scenario | Solution | Rationale |
|----------|----------|-----------|
| User permanently needs access that aligns with existing role | Assign to role | Standardized, easier to manage |
| User temporarily needs access (project-based, <3 months) | Direct access (time-bound) | Temporary, doesn't justify role change |
| User needs access that doesn't fit any existing role | Create new role OR direct access | Evaluate if others will need same access |

---

### 3.3 Role Hierarchy (Advanced)

**Objective**: Define parent-child role relationships for inheritance.

**Role Hierarchy Concept**:
```
Role: Standard User (base permissions: email, intranet)
  ├─> Role: Sales Representative (inherits Standard User + CRM access)
  │     └─> Role: Sales Manager (inherits Sales Rep + manager-level access)
  ├─> Role: Finance Analyst (inherits Standard User + Finance system access)
  │     └─> Role: Finance Manager (inherits Finance Analyst + approval rights)
  └─> Role: Developer (inherits Standard User + dev tools access)
        └─> Role: Engineering Manager (inherits Developer + project management tools)
```

**Benefits**:
- **Consistency**: All roles inherit base permissions (email, intranet)
- **Efficiency**: Don't need to redefine base permissions for each role
- **Clarity**: Clear progression from base → specialist → manager

**Implementation** (varies by system):
- **Active Directory**: Nested groups (Standard User group contains all role groups)
- **Azure AD**: Nested groups
- **Okta**: Role-based rules (less hierarchical, more flat)

**Example** (AD nested groups):
```
Group: ROLE-Standard-User (contains all employees)
  Member of: ROLE-Sales-Representative (Sales Reps)
    Member of: ROLE-Sales-Manager (Sales Managers)
```

**Result**: Sales Manager inherits permissions from Sales Representative AND Standard User.

**Caution**: Nested groups can become complex. Use sparingly (max 2-3 levels).

---

## 4. Group Management

### 4.1 Group Purpose and Ownership

**Objective**: Every group has documented purpose and assigned owner.

**Group Types**:
1. **Role Groups**: Represent roles (RBAC) - grants application access
2. **Distribution Lists**: Email distribution (no access control)
3. **Security Groups**: Grant access to specific resources (file shares, applications)
4. **Project Groups**: Temporary groups for projects

---

**Group Documentation Template**:

```markdown
## Group: [Group Name]

**Group ID**: [Unique identifier]  
**Type**: [Role Group | Distribution List | Security Group | Project Group]  
**Purpose**: [1-2 sentence description of group purpose]  
**Owner**: [Person responsible for group, typically department head or project manager]  
**Created Date**: [Date group was created]  
**Expiration Date**: [Date group should be deleted - for project groups only]  
**Status**: [Active | Under Review | Deprecated]

### Membership Criteria

Users are added to this group when:
- [ ] [Criterion 1]
- [ ] [Criterion 2]

### Membership Approval

- **Approval Required**: [Yes | No]
- **Approver**: [Group owner, manager, self-service]

### Access Granted

This group grants access to:
1. [Resource 1] - [Access level]
2. [Resource 2] - [Access level]

### Review Process

- **Review Frequency**: [Quarterly | Annual]
- **Reviewer**: [Group owner]
```

---

**Example Group Documentation**:

```markdown
## Group: Sales Team Distribution List

**Group ID**: DL-Sales-Team  
**Type**: Distribution List  
**Purpose**: Email distribution for sales team communications  
**Owner**: VP Sales (jane.doe@company.com)  
**Created Date**: 2023-05-01  
**Expiration Date**: N/A (permanent)  
**Status**: Active

### Membership Criteria

Users are added to this group when:
- [x] User is assigned to Sales department
- [x] User role is Sales Representative or Sales Manager

### Membership Approval

- **Approval Required**: No (automatic based on department)
- **Approver**: N/A (automatic)

### Access Granted

This group does NOT grant system access (distribution list only).

### Review Process

- **Review Frequency**: Annual
- **Reviewer**: VP Sales
```

---

### 4.2 Group Membership Management

**Objective**: Control who can be added to groups and how.

**Membership Approval Workflows**:

| Group Type | Approval Required? | Approver | Example |
|------------|-------------------|----------|---------|
| **Role Group** | Yes (automatic) | Manager | User assigned Sales Rep role → Manager approves role → Automatic group add |
| **Distribution List (department)** | No | N/A | User joins Sales dept → Automatic add to Sales DL |
| **Security Group (sensitive)** | Yes (manual) | Group Owner | User requests finance folder access → Finance Manager approves |
| **Project Group** | Yes | Project Manager | User requests project folder access → PM approves |

---

**Procedure 1: Automatic Group Membership** (based on department/role)

**Example**: Sales Team distribution list
```python
# Pseudo-code: Auto-add to distribution list based on department
def on_user_update(user):
  if user.department == "Sales":
    add_to_group(user, "DL-Sales-Team")
  else:
    remove_from_group(user, "DL-Sales-Team")
```

---

**Procedure 2: Approval-Based Group Membership** (sensitive groups)

**Process**:
```
User requests to join group (ticket or self-service portal)
  ↓
Request routes to Group Owner
  ↓
Group Owner reviews: Is this user appropriate for this group?
  ↓
If approved: User added to group
If rejected: User notified, request closed
```

---

### 4.3 Nested Group Strategy

**Objective**: Use nested groups to simplify management (use sparingly).

**Nested Groups Example**:
```
Group: All-Employees (all users)
  └─> Contains: ROLE-Standard-User
        ├─> Contains: ROLE-Sales-Representative
        │     └─> Contains: ROLE-Sales-Manager
        └─> Contains: ROLE-Finance-Analyst
              └─> Contains: ROLE-Finance-Manager
```

**Result**: 
- All employees automatically get "All-Employees" group access (email, intranet)
- Sales Reps get "All-Employees" + "Standard User" + "Sales Rep" access
- Sales Managers get all of the above + "Sales Manager" access

**When to Use Nested Groups**:
- ✅ Role hierarchy (Sales Rep → Sales Manager)
- ✅ Base permissions (Standard User → Specialized roles)
- ❌ Complex nesting (max 2-3 levels, beyond that becomes unmanageable)
- ❌ Cross-functional groups (can create unexpected access)

---

## 5. RBAC Adoption and Migration

### 5.1 Migration Strategy

**Objective**: Transition from direct access to role-based access over time.

**Current State** (Direct Access):
- 50 users each individually assigned to systems
- No standard roles
- Inconsistent access (some users have more access than others in same job)
- Manual provisioning for each user

**Target State** (RBAC):
- 11 roles defined
- Users assigned to roles based on job function
- Consistent access (all users in same role have same access)
- Automated provisioning (assign user to role → access granted)

---

**Migration Phases**:

**Phase 1: Role Definition (Weeks 1-4)**
- Identify roles (business analysis)
- Document roles (role catalog)
- Map roles to access (role access matrix)
- Create roles in identity system (AD groups, Azure AD groups)

**Phase 2: Pilot (Weeks 5-8)**
- Select pilot department (e.g., Sales - 15 users)
- Assign pilot users to roles
- Verify access (users have correct access via roles)
- Collect feedback (any issues? missing access? excessive access?)
- Refine role definitions

**Phase 3: Phased Rollout (Weeks 9-20)**
- **Week 9-12**: Finance department (5 users)
- **Week 13-16**: HR department (2 users)
- **Week 17-20**: Engineering department (10 users)
- Each phase: Assign users → Verify → Refine

**Phase 4: Final Migration (Weeks 21-24)**
- Migrate remaining users (IT, Leadership)
- Remove direct access assignments (transition to role-only)
- Document exceptions (users with direct access not via role)

**Phase 5: Steady State (Ongoing)**
- New hires automatically assigned to roles
- Access changes via role assignment (not direct access)
- Annual role review and optimization

---

### 5.2 Rollback Plan

**What if RBAC migration causes issues?**

**Scenario**: Users assigned to role lose access they need for their job.

**Rollback Steps**:
1. Immediately restore direct access (re-grant individual permissions)
2. Investigate root cause (why did role not grant correct access?)
3. Fix role definition (add missing permissions to role)
4. Re-test with pilot users
5. Resume migration once role is correct

**Contingency**: Maintain direct access assignments during migration for 30 days (grace period).

---

### 5.3 RBAC Adoption Metrics

**Objective**: Track progress toward full RBAC adoption.

**Key Metrics**:

| Metric | Calculation | Target | Current |
|--------|-------------|--------|---------|
| **RBAC Adoption Rate** | (Users with roles / Total users) × 100 | 100% | 60% |
| **Role Coverage** | (Access via roles / Total access) × 100 | 80%+ | 45% |
| **Direct Access Count** | # users with direct access (not via role) | <20% | 55% |
| **Role Count** | # active roles defined | 10-20 | 11 |
| **Orphaned Roles** | # roles with zero users | 0 | 1 |

**Dashboard Example**:
```
RBAC Adoption Dashboard - January 2026

Users with Roles: 30 / 50 (60%)
Access via Roles: 45% (Target: 80%)
Direct Access: 20 users (40%) - Target: <10 users (<20%)

Migration Progress:
✅ Sales (15 users) - 100% migrated
✅ Finance (5 users) - 100% migrated
⏳ HR (2 users) - 50% migrated
⏳ Engineering (10 users) - 0% migrated
```

---

## 6. Role Review and Maintenance

### 6.1 Annual Role Review

**Objective**: Verify role definitions are still accurate and appropriate.

**Review Process** (Annual):

**Step 1: Review Role Catalog**
- For each role: Is role still needed? (Yes/No)
- If no users assigned to role: Deprecate role

**Step 2: Review Access Mappings**
- For each role: Does role grant appropriate access?
- **Too much access?** (excessive privileges) → Remove unnecessary access
- **Too little access?** (users frequently request additional access) → Add missing access
- **Inconsistent?** (some users in role have more access than others) → Standardize

**Step 3: Review Users Assigned to Roles**
- For each user: Is user still in correct role?
- User changed job functions → Reassign to different role
- User has multiple roles → Verify all roles are still needed

**Step 4: Document Review**
- Update role definitions (access mappings, descriptions)
- Update role access matrix
- Communicate changes to stakeholders (users affected by role changes)

**Timeline**: 2-4 weeks annually

---

### 6.2 Role Cleanup

**Objective**: Remove obsolete roles and consolidate similar roles.

**Obsolete Role Identification**:
- Zero users assigned (role not used)
- Role grants same access as another role (duplicate)
- Role purpose no longer exists (e.g., "Project X Team" after project ends)

**Role Consolidation Example**:

**Before**:
- Role: "Sales Representative - West Region" (8 users)
- Role: "Sales Representative - East Region" (7 users)
- Problem: Both roles grant same access, only difference is region

**After**:
- Role: "Sales Representative" (15 users)
- Region tracked in user attribute (not separate role)
- Result: 1 role instead of 2, easier to manage

---

### 6.3 Role Change Management

**Objective**: Control changes to role definitions.

**Change Request Process**:

```
User/Manager identifies need to change role (add/remove access)
  ↓
Submit role change request (ticket)
  ↓
IAM team reviews: Impact assessment
  - How many users affected?
  - What access will change?
  - Any security implications?
  ↓
Role Owner (department head) approves change
  ↓
IAM implements change
  - Update role definition
  - Update access mappings in systems
  - Test with sample user
  ↓
Notify users affected by change
  - "Your [Role] access has been updated to include [New Access]"
  ↓
Document change (role version history)
```

**Change Documentation**:

| Change Date | Role | Change Description | Approver | Users Affected |
|-------------|------|-------------------|----------|----------------|
| 2026-01-15 | Sales Representative | Added Sales Portal (Read) access | VP Sales | 15 |
| 2026-02-01 | Finance Analyst | Removed Admin access to Finance System (least privilege) | CFO | 5 |

---

## 7. Common Pitfalls and Solutions

### 7.1 Pitfall: Too Many Roles

**Problem**: 50 roles defined for 50-person company (1 role per user = no benefit of RBAC)

**Consequence**: 
- Management overhead (maintain 50 roles)
- Defeats purpose of RBAC (no standardization, no efficiency)

**Solution**:
- ✅ Aim for 10-20 roles for 50-person company
- ✅ Consolidate similar roles (Sales Rep West/East → Sales Rep)
- ✅ Use role hierarchy (Standard User → Sales Rep → Sales Manager)
- ✅ Accept some variation (some users may need direct access for edge cases)

---

### 7.2 Pitfall: Roles Too Granular

**Problem**: Separate role for every minor access difference

**Example**:
- Role: "Sales Rep with CRM + Email"
- Role: "Sales Rep with CRM + Email + Sales Portal"
- Role: "Sales Rep with CRM + Email + Sales Portal + Commission System"

**Consequence**: Too many roles, no standardization

**Solution**:
- ✅ Define roles based on job function, not systems
- ✅ Role should grant standard access for job function
- ✅ Special needs handled via direct access (exception, not separate role)

---

### 7.3 Pitfall: Role Definitions Drift Over Time

**Problem**: Role defined correctly initially, but access mappings change without updating role definition

**Example**:
- Role: "Sales Rep" defined in 2023 (grants CRM + Sales folder)
- 2024: Organization adopts new sales portal, Sales Reps need access
- Problem: Access granted directly to users, not added to "Sales Rep" role
- Result: New hires don't get sales portal access (role missing it)

**Solution**:
- ✅ Annual role review (verify role grants correct access)
- ✅ Change management process (update role when access requirements change)
- ✅ Monitor new hire feedback ("I need access to X, but my role doesn't grant it")

---

### 7.4 Pitfall: No Role Owner

**Problem**: Roles defined, but nobody responsible for maintaining them

**Consequence**: Role definitions become outdated, inaccurate

**Solution**:
- ✅ Assign role owner for each role (typically department head)
- ✅ Role owner responsible for:
  - Defining role access requirements
  - Approving changes to role
  - Annual role review
  - Verifying users assigned to role are appropriate

---

## 8. Success Criteria

**How to Know RBAC is Working**:

✅ **RBAC Adoption**:
- 80%+ of users assigned to roles (not direct access)
- 80%+ of access granted via roles (not direct access)
- New hires automatically assigned to roles (no manual provisioning)

✅ **Consistency**:
- All users in same role have same access
- No more "User A has access but User B doesn't (same job)"

✅ **Efficiency**:
- Time to provision new hire: <1 day (automatic via role assignment)
- Time to change user access: <1 day (reassign role, not reprovision individual systems)

✅ **Auditability**:
- Clear mapping: User → Role → Access
- Role definitions documented and up-to-date
- Access reviews easier (review role, not individual users)

✅ **Compliance**:
- Auditors can verify access control by reviewing roles (not individual users)
- Segregation of duties enforced at role level
- Least privilege demonstrated (roles grant minimum access needed)

---

## 9. Next Steps

### 9.1 After Implementing RBAC

1. ✅ **RBAC framework established** (this implementation guide completed)
   
2. ➡️ **Next**: Implement access reviews (IMP-S4)
   - Role-based access reviews (review role, not individual users)
   - Manager access certification
   - Quarterly/annual review cycles
   
3. ➡️ **Then**: Implement IAM assessment (IMP-S5)
   - Generate role compliance workbook
   - Measure RBAC adoption rate
   - Track direct access vs. role-based access
   - Present dashboard to CISO

---

## Document Approval

**Prepared By**: [Name], [Title] - [Date]  
**Reviewed By**: [Name], [Title] - [Date]  
**Approved By**: [Name], CISO - [Date]

**Next Review Date**: [Date + 12 months]

**Version History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial implementation guide for RBAC |

---

**END OF IMPLEMENTATION GUIDE S3 - ROLE DEFINITION AND ASSIGNMENT**

**Next Document**: ISMS-IMP-A.5.15-16-18-S4_Access_Review_Process.md