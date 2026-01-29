# ISMS Policy Section 5: Assessment Methodology & Evidence Framework

**Document ID**: ISMS-POL-A.5.15-16-18-S5  
**Title**: Assessment Methodology & Evidence Framework  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Part of**: ISMS-POL-A.5.15-16-18 Identity & Access Management Framework

---

## Table of Contents

1. [Assessment Approach Overview](#1-assessment-approach-overview)
2. [Workbook 1: User Inventory & Lifecycle Compliance](#2-workbook-1-user-inventory--lifecycle-compliance)
3. [Workbook 2: Access Rights Matrix](#3-workbook-2-access-rights-matrix)
4. [Workbook 3: Access Review Results](#4-workbook-3-access-review-results)
5. [Workbook 4: Role Definition & Compliance](#5-workbook-4-role-definition--compliance)
6. [Workbook 5: Lifecycle Compliance Detailed Assessment](#6-workbook-5-lifecycle-compliance-detailed-assessment)
7. [Dashboard: IAM Governance Overview](#7-dashboard-iam-governance-overview)
8. [Evidence Collection Per Control](#8-evidence-collection-per-control)
9. [Compliance Scoring Methodology](#9-compliance-scoring-methodology)
10. [Continuous Assessment Approach](#10-continuous-assessment-approach)

---

## 1. Assessment Approach Overview

### 1.1 Unified Assessment Strategy

**Why Unified Assessment for A.5.15/16/18**:

These three controls share common data sources and assessment infrastructure:
- **Shared Foundation**: All three controls rely on the same user inventory, access matrix, and identity systems
- **Interdependent Metrics**: Lifecycle compliance (A.5.16) affects access rights accuracy (A.5.18), access control policy (A.5.15) governs both
- **Efficiency**: Single assessment provides evidence for all three controls (vs. 3× separate assessments)
- **Consistency**: Unified data ensures no discrepancies between control assessments

**Assessment Architecture**:
```
┌────────────────────────────────────────────────────────────────┐
│                 DATA SOURCES (Identity Systems)                │
│  Active Directory, Azure AD, Okta, HR System, Access Requests │
└──────────────────────┬─────────────────────────────────────────┘
                       │
                       ↓
┌────────────────────────────────────────────────────────────────┐
│                  6 ASSESSMENT WORKBOOKS                        │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          │
│  │ WB1: User    │ │ WB2: Access  │ │ WB3: Access  │          │
│  │ Inventory &  │ │ Rights       │ │ Review       │          │
│  │ Lifecycle    │ │ Matrix       │ │ Results      │          │
│  └──────────────┘ └──────────────┘ └──────────────┘          │
│  ┌──────────────┐ ┌──────────────┐                            │
│  │ WB4: Role    │ │ WB5: Lifecycle│                           │
│  │ Compliance   │ │ Detailed     │                            │
│  └──────────────┘ └──────────────┘                            │
└──────────────────────┬─────────────────────────────────────────┘
                       │
                       ↓
┌────────────────────────────────────────────────────────────────┐
│             DASHBOARD: IAM Governance Overview                 │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          │
│  │ A.5.15 Score │ │ A.5.16 Score │ │ A.5.18 Score │          │
│  └──────────────┘ └──────────────┘ └──────────────┘          │
│              Overall IAM Maturity Score                        │
└────────────────────────────────────────────────────────────────┘
```

### 1.2 Assessment Workbooks Overview

**Six Workbooks Provide Comprehensive IAM Evidence**:

| Workbook | Primary Controls | Purpose | Key Metrics |
|----------|-----------------|---------|-------------|
| **WB1: User Inventory & Lifecycle** | A.5.16 | Complete user inventory, lifecycle timeliness | Provisioning %, Deprovisioning %, Orphaned accounts |
| **WB2: Access Rights Matrix** | A.5.18 | User→System→Access mapping | Access coverage, Documentation completeness |
| **WB3: Access Review Results** | A.5.15, A.5.18 | Review completion, findings | Review completion %, Removal rate |
| **WB4: Role Compliance** | A.5.15, A.5.18 | RBAC maturity, SoD compliance | RBAC adoption %, SoD violations |
| **WB5: Lifecycle Detailed** | A.5.16 | Joiner/Mover/Leaver compliance | Joiner %, Mover %, Leaver % |
| **Dashboard** | A.5.15/16/18 | Executive summary, consolidated compliance | Overall IAM maturity, Gap counts |

**Assessment Frequency**:
- **Monthly**: User inventory updates, orphaned account scans (WB1)
- **Quarterly**: Access reviews for critical systems (WB3), Role compliance checks (WB4)
- **Semi-Annual**: Access reviews for high-sensitivity systems (WB3)
- **Annual**: Comprehensive IAM assessment (all 6 workbooks generated, dashboard updated)

### 1.3 Technology-Agnostic Assessment

**Assessment Works with Any Identity Environment**:

- **Identity Systems**: Active Directory, Azure AD, Okta, Google Workspace, LDAP, custom directories
- **Access Management Platforms**: SailPoint, Saviynt, CyberArk Identity, Ping Identity, custom tools
- **HR Systems**: Workday, SAP SuccessFactors, BambooHR, ADP, custom HRIS
- **Ticketing Systems**: ServiceNow, Jira, Remedy, custom workflows

**Data Integration Approach**:
- **Option 1 - API Integration**: Scripts call identity system APIs directly (Azure AD Graph, Okta API, etc.)
- **Option 2 - CSV Export/Import**: Manual export from identity systems → import into assessment workbooks
- **Option 3 - Database Queries**: Scripts query identity database directly (if accessible)
- **Option 4 - Hybrid**: Combination of automated and manual data collection

**Flexibility**: Assessment framework adapts to [Organization]'s specific technology stack.

### 1.4 Assessment Deliverables

**For Internal Use (ISMS Team, Security, Management)**:
- Six detailed assessment workbooks (operational data, metrics, gap analysis)
- Consolidated dashboard (executive summary, KPIs, prioritized gaps)
- Gap remediation action plan (prioritized by risk)

**For External Audit**:
- Evidence register (catalog of all evidence, indexed by control)
- Sample audit logs (user provisioning, access reviews, access removals)
- Policy documents (POL-S1 through POL-S5)
- Implementation procedures (IMP-S1 through IMP-S5)
- Assessment workbook exports (Excel or PDF)

---

## 2. Workbook 1: User Inventory & Lifecycle Compliance

### 2.1 Workbook Purpose & Scope

**Primary Control Coverage**: A.5.16 (Identity Management)

**Purpose**: Provide complete, current user inventory and measure identity lifecycle process compliance.

**Assessment Questions Answered**:
- How many users does [Organization] have? (employees, contractors, vendors, service accounts)
- Are new users provisioned on time? (access ready by start date)
- Are terminated users deprovisioned on time? (access removed immediately)
- How many orphaned accounts exist? (accounts without valid business owner)
- How many inactive accounts exist? (no login in 90+ days)

### 2.2 Data Sources for WB1

**Primary Data Sources**:
1. **Identity Systems**: Active Directory, Azure AD, Okta, Google Workspace
   - User accounts (user ID, name, email, status, last login)
   - Account creation date, account disabled date
   - Account attributes (department, manager, location)

2. **HR System**: Workday, SAP SuccessFactors, BambooHR
   - Employee master data (authoritative source)
   - Hire date, termination date, job title, department, manager
   - Employment status (active, terminated, on leave)

3. **Contractor Management System**: (if separate from HR)
   - Contractor records (name, sponsor, contract dates)
   - Contract start/end dates

**Data Collection Methods**:
- **Automated**: API calls to identity systems (Azure AD Graph API, Okta API)
- **Automated**: Database queries (if direct access available)
- **Manual**: CSV exports from identity systems and HR system
- **Hybrid**: Automated for employees, manual for contractors

### 2.3 WB1 Sheet Structure

**Sheet 1: Instructions & Legend**
- How to use workbook
- Color coding explanation (Green = Compliant, Yellow = Warning, Red = Non-Compliant)
- Data sources documented
- Assessment date
- Glossary of terms

**Sheet 2: User_Inventory** (100+ sample users)
- **Columns**:
  - User_ID (unique identifier from identity system)
  - Name (first, last)
  - Email
  - User_Type (Employee, Contractor, Vendor, Service Account)
  - Department
  - Manager (manager name or ID)
  - Location (office location or remote)
  - Hire_Date (from HR system)
  - Termination_Date (from HR system, blank if active)
  - Status (Active, Disabled, Deleted)
  - Last_Login (last successful login date)
  - Account_Created_Date
  - Account_Source (AD, Azure AD, Okta, etc.)
  - In_HR_System (Y/N - cross-reference with HR data)

**Sheet 3: Employee_Lifecycle** (Employee subset)
- **Columns**:
  - User_ID
  - Name
  - Hire_Date
  - Provision_Date (when account was created)
  - Days_to_Provision (DATEDIF formula: Hire_Date to Provision_Date)
  - Provisioning_Status (On-Time if ≤0 days, Late if >0 days)
  - Termination_Date (if terminated)
  - Disable_Date (when account was disabled)
  - Days_to_Disable (DATEDIF formula: Termination_Date to Disable_Date)
  - Deprovisioning_Status (On-Time if ≤1 day, Late if >1 day)
  - Compliance_Status (Compliant / Non-Compliant)

**Sheet 4: Contractor_Lifecycle** (Contractor subset)
- **Columns**:
  - User_ID
  - Name
  - Contract_Start
  - Contract_End
  - Provision_Date
  - Disable_Date
  - Sponsor (internal employee sponsoring contractor)
  - Auto_Expiration_Configured (Y/N - is account set to auto-expire on contract end?)
  - Compliance_Status

**Sheet 5: Service_Accounts** (Non-human accounts)
- **Columns**:
  - Account_ID
  - Description (service account purpose)
  - Owner (person responsible for service account)
  - Purpose (what application/service uses this account)
  - Last_Password_Change
  - Privileged (Y/N - does account have admin privileges?)
  - Compliance_Status (has owner, password rotated within 90 days)

**Sheet 6: Orphaned_Accounts** (Detection results)
- **Columns**:
  - User_ID
  - Name
  - Last_Login (or "Never")
  - Account_Age_Days (days since account created)
  - In_HR_System (Y/N)
  - Business_Owner (if identified)
  - Orphan_Reason (Not in HR / No login in 90+ days / No valid owner)
  - Remediation_Status (Pending / Owner Identified / Disabled / Deleted)
  - Remediation_Date

**Sheet 7: Lifecycle_Metrics** (Summary statistics)
- **Provisioning Metrics**:
  - Total users provisioned (count)
  - Provisioning on-time (count, %)
  - Provisioning late (count, %, average delay in days)
- **Deprovisioning Metrics**:
  - Total users deprovisioned (count)
  - Deprovisioning on-time (count, %)
  - Deprovisioning late (count, %, average delay in days)
- **Orphaned Account Metrics**:
  - Total orphaned accounts (count)
  - Orphaned accounts remediated (count, %)
  - Orphaned accounts pending (count)

**Sheet 8: Gap_Analysis**
- **Gaps Identified**:
  - Late provisioning (users who didn't get access by start date)
  - Late deprovisioning (users not disabled immediately after termination)
  - Orphaned accounts (accounts without valid owner)
  - Inactive accounts (no login in 90+ days)
- **Columns**: Gap_ID, User_ID, Gap_Type, Severity, Description, Owner, Remediation_Plan, Target_Date, Status

**Sheet 9: Evidence_Register** (50+ evidence items)
- **Columns**: Evidence_ID, Evidence_Type, Description, Source, Date_Collected, Retention_Period, Location

**Sheet 10: Approval_Sign_Off**
- 3-level approval workflow
- Security Manager, IT Director, CISO sign-off

### 2.4 WB1 Key Formulas & Validation

**Provisioning Timeliness Formula**:
```
=DATEDIF([Hire_Date], [Provision_Date], "D")
```
- Result ≤ 0: On-Time (Green) - account ready by or before start date
- Result 1-3 days: Borderline (Yellow) - slight delay
- Result > 3 days: Late (Red) - significant delay

**Deprovisioning Timeliness Formula**:
```
=DATEDIF([Termination_Date], [Disable_Date], "D")
```
- Result ≤ 1: On-Time (Green) - disabled within 24 hours
- Result 2-7 days: Borderline (Yellow) - delayed but within week
- Result > 7 days: Late (Red) - serious security risk

**Orphaned Account Detection Logic**:
```
IF(In_HR_System = "N" OR Last_Login > 90 days, "Orphaned", "Active")
```

**Conditional Formatting**:
- Green: On-time provisioning/deprovisioning, compliant lifecycle
- Yellow: Borderline delays (1-3 days provisioning, 2-7 days deprovisioning)
- Red: Late provisioning/deprovisioning, orphaned accounts

### 2.5 WB1 Assessment Criteria (A.5.16)

**Compliance Thresholds**:
- **Provisioning On-Time Rate**: Target ≥95% (at least 95% of users provisioned on time)
- **Deprovisioning On-Time Rate**: Target ≥98% (at least 98% of terminations deprovisioned within 24h)
- **Orphaned Account Rate**: Target ≤2% (no more than 2% of accounts are orphaned)
- **Inactive Account Rate**: Target ≤5% (no more than 5% of accounts inactive 90+ days)

**A.5.16 Compliance Score Calculation**:
```
A.5.16 Score = (Provisioning % + Deprovisioning % + (100 - Orphaned %)) / 3
```
Example: (96% provisioning + 99% deprovisioning + 98% non-orphaned) / 3 = 97.7% (Excellent)

---

## 3. Workbook 2: Access Rights Matrix

### 3.1 Workbook Purpose & Scope

**Primary Control Coverage**: A.5.18 (Access Rights)

**Purpose**: Document comprehensive user-to-system-to-access-level mapping and verify access documentation completeness.

**Assessment Questions Answered**:
- Who has access to what systems? (complete access mapping)
- What access level does each user have? (read, write, admin)
- Is access properly documented? (justification, approvals)
- Is privileged access identified and tracked? (admin-level access)
- Are role assignments documented? (RBAC implementation)

### 3.2 Data Sources for WB2

**Primary Data Sources**:
1. **Identity Systems**: User-to-group mappings, role assignments
2. **Application Access Logs**: User access to applications (from app logs or access management platform)
3. **Access Request System**: ServiceNow, Jira, access management platform (approval records, justifications)
4. **Role Catalog**: Documented standard roles and their access mappings

**Data Collection Methods**:
- **Automated**: Export group memberships from AD/Azure AD/Okta
- **Automated**: Query access management platform for access grants
- **Semi-Automated**: Parse application access logs
- **Manual**: Extract approval records from ticketing system

### 3.3 WB2 Sheet Structure

**Sheet 1: Instructions & Legend**

**Sheet 2: Access_Matrix** (100 users × 20 systems = ~2000 access grants with access)
- **Columns**:
  - User_ID
  - User_Name
  - User_Type (Employee, Contractor, Vendor)
  - System_Name (ERP, CRM, File Server, Database, etc.)
  - Access_Level (Read, Write, Admin)
  - Granted_Date (when access was granted)
  - Granted_By (who provisioned access - IT staff member)
  - Business_Justification (why access was granted)
  - Approval_Date (when access was approved)
  - Approver (manager or system owner who approved)
  - Last_Review_Date (when access was last reviewed)
  - Expiration_Date (for time-bounded access, blank if permanent)
  - Status (Active, Disabled, Removed)

**Sheet 3: Role_Assignments** (100 users, ~70% have role assignments)
- **Columns**:
  - User_ID
  - User_Name
  - Role_Name (Financial Analyst, HR Admin, Developer, etc.)
  - Role_Description (brief description of role)
  - Assigned_Date (when user was assigned to role)
  - Assigned_By (who assigned role - manager or IT)
  - Role_Owner (person responsible for role definition)
  - Expiration_Date (for time-bounded roles)

**Sheet 4: Group_Memberships** (100 users × avg 5 groups = ~500 memberships)
- **Columns**:
  - User_ID
  - User_Name
  - Group_Name (AD group, Azure AD group, etc.)
  - Group_Purpose (what access the group grants)
  - Group_Owner (person responsible for group membership approval)
  - Join_Date (when user was added to group)
  - Approval_Date (if group membership was formally approved)
  - Approver (group owner or manager)

**Sheet 5: Privileged_Access** (15 privileged users - subset of Access_Matrix)
- **Columns**:
  - User_ID
  - User_Name
  - Privileged_System (system where user has admin access)
  - Privilege_Type (Domain Admin, Database Admin, Application Admin, etc.)
  - Granted_Date
  - Approval_Date
  - Approver (CISO, IT Director, or security team)
  - Review_Frequency (Quarterly for privileged access)
  - Last_Review_Date
  - Next_Review_Date (calculated: Last_Review_Date + 90 days)

**Sheet 6: Access_Documentation** (Summary of documentation completeness)
- **Metrics**:
  - Total access grants (count from Access_Matrix)
  - Access with justification (count, %)
  - Access with approval (count, %)
  - Access with recent review (reviewed in last 12 months - count, %)
  - Privileged access with quarterly review (count, %)
- **Completeness Score**: (Access with justification + Access with approval + Access with recent review) / 3

**Sheet 7: Coverage_Analysis** (System-level statistics)
- **Columns**:
  - System_Name
  - Users_With_Access (count)
  - Access_Level_Breakdown (count per level: Read, Write, Admin)
  - Average_Access_Level (numeric: Read=1, Write=2, Admin=3)
  - Privileged_Users_Count (admin-level users)
  - Documentation_Completeness (% of access grants with full documentation)

**Sheet 8: Gap_Analysis**
- **Gaps**:
  - Access without justification (no business justification documented)
  - Access without approval (no manager/system owner approval)
  - Access not reviewed (last review >12 months ago)
  - Privileged access not reviewed quarterly
  - Time-bounded access without expiration date
- **Columns**: Gap_ID, User_ID, System_Name, Gap_Type, Severity, Description, Remediation_Plan, Owner, Target_Date, Status

**Sheet 9: Evidence_Register**

**Sheet 10: Approval_Sign_Off**

### 3.4 WB2 Key Formulas & Validation

**Documentation Completeness Formula**:
```
=IF(AND(NOT(ISBLANK([Business_Justification])), NOT(ISBLANK([Approver])), [Last_Review_Date] >= TODAY()-365), "Complete", "Incomplete")
```
- Complete: Has justification, approval, reviewed in last 12 months
- Incomplete: Missing one or more documentation elements

**Privileged Access Flagging**:
```
=IF([Access_Level] = "Admin", "Privileged", "Standard")
```

**Review Currency Check**:
```
=IF([Last_Review_Date] < TODAY()-365, "Overdue", "Current")
```
- Overdue: Last review more than 12 months ago (standard access)
- For privileged access: Overdue if >90 days

**Conditional Formatting**:
- Green: Complete documentation, reviewed recently
- Yellow: Partial documentation, review approaching
- Red: Missing documentation, review overdue

### 3.5 WB2 Assessment Criteria (A.5.18)

**Compliance Thresholds**:
- **Justification Completeness**: Target ≥95% (at least 95% of access grants have documented justification)
- **Approval Documentation**: Target ≥95% (at least 95% of access grants have documented approval)
- **Review Currency**: Target ≥90% (at least 90% of access reviewed in last 12 months)
- **Privileged Access Review**: Target 100% (all privileged access reviewed quarterly)

**Partial A.5.18 Score Contribution**:
```
Access Documentation Score = (Justification % + Approval % + Review %) / 3
```
This feeds into overall A.5.18 score (combined with access review completion from WB3, RBAC adoption from WB4).

---

## 4. Workbook 3: Access Review Results

### 4.1 Workbook Purpose & Scope

**Primary Control Coverage**: A.5.15 (Access Control), A.5.18 (Access Rights)

**Purpose**: Track access review execution, measure review completion rates, document review findings and remediation.

**Assessment Questions Answered**:
- Are access reviews conducted on schedule? (review completion rate)
- Which systems have overdue reviews? (review accountability)
- What do access reviews find? (inappropriate access, justifications)
- Is inappropriate access removed promptly? (remediation timeliness)
- Are reviewers responsive? (reviewer accountability)

### 4.2 Data Sources for WB3

**Primary Data Sources**:
1. **Access Review Platform**: SailPoint, Saviynt, CyberArk Identity, custom GRC tools
2. **Access Review Schedules**: Planned review calendar (which systems, which quarters)
3. **Review Completion Reports**: From access review platform or manual tracking
4. **Ticketing System**: Access removal tickets generated from review findings

**Data Collection Methods**:
- **Automated**: Export review completion data from access review platform
- **Semi-Automated**: Compile review schedules from calendar or project plan
- **Manual**: Interview reviewers for completion status (if no automated tracking)

### 4.3 WB3 Sheet Structure

**Sheet 1: Instructions & Legend**

**Sheet 2: Review_Schedule** (20 systems × 4 quarters = 80 planned reviews)
- **Columns**:
  - Review_ID (unique identifier: SYS-Q1-2026)
  - System_Name
  - Review_Period (Q1-2026, Q2-2026, etc.)
  - Review_Frequency (Quarterly, Semi-Annual, Annual based on criticality)
  - Reviewer (manager, system owner, security team)
  - Due_Date (review completion deadline)
  - Status (Scheduled, In Progress, Completed, Overdue)

**Sheet 3: Review_Completion** (80 reviews with execution data)
- **Columns**:
  - Review_ID
  - System_Name
  - Review_Period
  - Reviewer
  - Start_Date (when review was initiated)
  - Completion_Date (when review was completed)
  - Users_Reviewed (count)
  - Access_Confirmed (count - access retained as appropriate)
  - Access_Removed (count - access removed as inappropriate)
  - Access_Justified (count - access seems excessive but justified with documentation)
  - Further_Investigation (count - access requiring additional review)
  - Review_Status (Completed, Overdue, In Progress)
  - Days_to_Complete (DATEDIF from Start_Date to Completion_Date)

**Sheet 4: Review_Findings** (60 findings across all reviews - sample)
- **Columns**:
  - Finding_ID
  - Review_ID (links to specific review)
  - User_ID
  - User_Name
  - System_Name
  - Access_Level
  - Finding_Type (Remove Access, Justify Access, Further Investigation)
  - Finding_Description (why access is inappropriate or questionable)
  - Remediation_Action (Remove, Document Justification, Investigate)
  - Remediation_Ticket (ServiceNow/Jira ticket number)
  - Remediation_Date (when action was completed)
  - Status (Open, In Progress, Closed)

**Sheet 5: Overdue_Reviews** (Subset of Review_Schedule where Status = Overdue)
- **Columns**:
  - Review_ID
  - System_Name
  - Reviewer
  - Due_Date
  - Days_Overdue (DATEDIF from Due_Date to TODAY)
  - Escalation_Status (Reminder Sent, Escalated to Manager, Escalated to CISO)
  - Escalation_Date

**Sheet 6: Reviewer_Performance** (Reviewer accountability)
- **Columns**:
  - Reviewer_Name
  - Reviews_Assigned (count)
  - Reviews_Completed (count)
  - Reviews_Overdue (count)
  - Completion_Rate (%) = (Completed / Assigned) × 100
  - Average_Time_to_Complete (days - average of Days_to_Complete for all reviews)
  - Responsiveness_Rating (Excellent ≥95%, Good 85-94%, Poor <85%)

**Sheet 7: Review_Metrics** (Summary statistics)
- **Overall Metrics**:
  - Total reviews scheduled (count)
  - Reviews completed (count, %)
  - Reviews in progress (count, %)
  - Reviews overdue (count, %)
  - Overall completion rate (%)
- **Findings Metrics**:
  - Total findings (count)
  - Access confirmed (count, %)
  - Access removed (count, %)
  - Access justified (count, %)
  - Remediation completion rate (%)

**Sheet 8: Gap_Analysis**
- **Gaps**:
  - Overdue reviews (reviews past due date)
  - Incomplete reviews (reviews started but not finished)
  - Unaddressed findings (removal tickets not executed)
  - Low reviewer responsiveness (reviewers consistently late)
- **Columns**: Gap_ID, Review_ID, Gap_Type, Severity, Description, Owner, Remediation_Plan, Target_Date, Status

**Sheet 9: Evidence_Register**

**Sheet 10: Approval_Sign_Off**

### 4.4 WB3 Key Formulas & Validation

**Review Completion Rate Formula**:
```
=COUNTIF([Status], "Completed") / COUNTA([Review_ID]) × 100
```

**Days Overdue Calculation**:
```
=IF([Status] <> "Completed", DATEDIF([Due_Date], TODAY(), "D"), 0)
```

**Remediation Rate**:
```
=(Findings Closed / Total Findings) × 100
```

**Conditional Formatting**:
- Green: Review completed on time, no overdue items
- Yellow: Review in progress (approaching due date), some overdue findings
- Red: Review overdue, many unaddressed findings

### 4.5 WB3 Assessment Criteria (A.5.15 + A.5.18)

**Compliance Thresholds**:
- **Review Completion Rate**: Target ≥95% (at least 95% of scheduled reviews completed)
- **Overdue Reviews**: Target ≤5% (no more than 5% of reviews overdue)
- **Remediation Completion**: Target ≥95% (at least 95% of findings remediated)
- **Reviewer Responsiveness**: Target ≥90% (at least 90% of reviewers complete on time)

**Partial A.5.15 and A.5.18 Score Contribution**:
```
Review Compliance Score = (Completion Rate + (100 - Overdue %) + Remediation Rate) / 3
```
This feeds into:
- A.5.15 score (access control policy enforcement via reviews)
- A.5.18 score (access rights verification via reviews)

---

## 5. Workbook 4: Role Definition & Compliance

### 5.1 Workbook Purpose & Scope

**Primary Control Coverage**: A.5.15 (Access Control - SoD), A.5.18 (Access Rights - RBAC)

**Purpose**: Assess RBAC maturity, verify role-based access adoption, detect segregation of duties violations.

**Assessment Questions Answered**:
- How mature is [Organization]'s RBAC implementation? (RBAC adoption rate)
- What percentage of users are assigned to roles vs. direct access? (RBAC coverage)
- Are role definitions accurate? (role-to-access mapping current)
- Are there segregation of duties (SoD) violations? (conflicting role assignments)
- Are roles reviewed periodically? (role maintenance)

### 5.2 Data Sources for WB4

**Primary Data Sources**:
1. **Role Catalog**: Documented standard roles (from policy or access management platform)
2. **Identity Systems**: User role assignments (from AD groups, Azure AD roles, Okta groups)
3. **SoD Matrix**: Defined conflicting role pairs (from access control policy)
4. **Access Matrix**: User access data (to validate role-to-access mapping accuracy)

**Data Collection Methods**:
- **Automated**: Export role assignments from identity systems
- **Manual**: Compile role catalog from documentation or access management platform
- **Automated**: Compare user role assignments against SoD matrix (script)

### 5.3 WB4 Sheet Structure

**Sheet 1: Instructions & Legend**

**Sheet 2: Role_Catalog** (30 standard roles defined)
- **Columns**:
  - Role_ID
  - Role_Name (Financial Analyst, HR Administrator, Developer, etc.)
  - Role_Description (job function, responsibilities)
  - Business_Owner (person responsible for role definition)
  - Systems_Included (list of systems role grants access to)
  - Access_Level_Summary (summary of access levels per system)
  - Users_Assigned (count of users assigned to role)
  - Last_Review_Date (when role definition was last reviewed)
  - Next_Review_Date (annual review - Last_Review_Date + 365 days)
  - Status (Active, Under Review, Obsolete)

**Sheet 3: Role_Assignments** (80 users assigned to roles, 20 users with direct access only)
- **Columns**:
  - User_ID
  - User_Name
  - Role_Name (or "Direct Access" if no role)
  - Assignment_Date (when user was assigned to role)
  - Assignment_Approver (manager or role owner)
  - Expiration_Date (for time-bounded roles)
  - Status (Active, Expired, Removed)

**Sheet 4: Direct_Access_Users** (20 users without role assignments - need justification)
- **Columns**:
  - User_ID
  - User_Name
  - Systems_Accessed (list of systems user has direct access to)
  - Reason_No_Role (why user doesn't fit into standard role)
  - Business_Justification (documented reason for direct access)
  - Approved_By (security team or CISO)
  - Review_Frequency (quarterly for direct access users)
  - Last_Review_Date

**Sheet 5: SoD_Matrix** (6 conflicting role pairs defined)
- **Columns**:
  - Conflict_ID
  - Role_A (first role in conflict pair)
  - Role_B (second role in conflict pair)
  - Conflict_Type (Request + Approve, Developer + Production Admin, Finance + Payroll, etc.)
  - Risk_Level (High, Medium, Low)
  - Mitigation (compensating controls - enhanced monitoring, dual approval, etc.)

**Sheet 6: SoD_Violations** (5 users with conflicting role assignments - violations detected)
- **Columns**:
  - User_ID
  - User_Name
  - Conflicting_Roles (Role_A + Role_B)
  - Conflict_Type (from SoD_Matrix)
  - Risk_Level (High, Medium, Low)
  - Detection_Date (when violation was detected)
  - Business_Justification (if violation is justified)
  - Compensating_Controls (if violation is accepted)
  - Approved_By (CISO or security manager - if violation accepted)
  - Remediation_Plan (if violation requires remediation)
  - Remediation_Date
  - Status (Open, Justified with Controls, Remediated)

**Sheet 7: RBAC_Metrics** (RBAC maturity metrics)
- **Metrics**:
  - Total users (count)
  - Users with role assignments (count, %)
  - Users with direct access only (count, %)
  - RBAC adoption rate (%) = (Users with roles / Total users) × 100
  - Role coverage (%) = (Access via roles / Total access) × 100
  - Average roles per user (count)
  - Active roles (count)
  - Obsolete roles (count)
  - SoD violations (count)
  - SoD violations remediated (count, %)

**Sheet 8: Gap_Analysis**
- **Gaps**:
  - Low RBAC adoption (below target of 80%)
  - Direct access without justification
  - Unresolved SoD violations
  - Roles not reviewed annually
  - Obsolete roles not deactivated
- **Columns**: Gap_ID, Gap_Type, Severity, Description, Owner, Remediation_Plan, Target_Date, Status

**Sheet 9: Evidence_Register**

**Sheet 10: Approval_Sign_Off**

### 5.4 WB4 Key Formulas & Validation

**RBAC Adoption Rate**:
```
=(Users with Roles / Total Users) × 100
```
Target: ≥80% (mature RBAC implementation)

**SoD Violation Detection Logic**:
```
FOR EACH User:
  FOR EACH Role Pair in SoD_Matrix:
    IF User has Role_A AND User has Role_B:
      FLAG as SoD Violation
```

**Role Review Currency**:
```
=IF([Last_Review_Date] < TODAY()-365, "Overdue", "Current")
```

**Conditional Formatting**:
- Green: High RBAC adoption, no SoD violations, roles reviewed
- Yellow: Moderate RBAC adoption, justified SoD violations
- Red: Low RBAC adoption, unresolved SoD violations, roles not reviewed

### 5.5 WB4 Assessment Criteria (A.5.15 + A.5.18)

**Compliance Thresholds**:
- **RBAC Adoption Rate**: Target ≥80% (at least 80% of users assigned to roles)
- **SoD Violation Count**: Target = 0 (zero unresolved violations)
- **Role Review Currency**: Target ≥95% (at least 95% of roles reviewed annually)
- **Direct Access Justification**: Target 100% (all direct access users have documented justification)

**Partial A.5.15 and A.5.18 Score Contribution**:
```
RBAC Compliance Score = (RBAC Adoption Rate + (100 - SoD Violation %) + Role Review %) / 3
```
This feeds into:
- A.5.15 score (SoD compliance per access control policy)
- A.5.18 score (RBAC implementation for access rights management)

---

## 6. Workbook 5: Lifecycle Compliance Detailed Assessment

### 6.1 Workbook Purpose & Scope

**Primary Control Coverage**: A.5.16 (Identity Management - detailed lifecycle process compliance)

**Purpose**: Deep dive into joiner/mover/leaver process compliance, measure timeliness for each lifecycle stage, identify process gaps.

**Assessment Questions Answered**:
- Are new hires provisioned on time? (joiner process compliance)
- Are role changes handled promptly? (mover process compliance)
- Are terminations processed immediately? (leaver process compliance)
- Is contractor lifecycle managed properly? (time-bound access, sponsorship)
- Are orphaned accounts remediated? (cleanup process)

**Note**: This workbook provides MORE DETAIL than WB1 (User Inventory). WB1 provides overall lifecycle metrics; WB5 provides granular process compliance data.

### 6.2 Data Sources for WB5

**Primary Data Sources**:
1. **HR System Events**: Hire events, termination events, role change events
2. **Identity System Logs**: Account creation logs, account disable logs, role change logs
3. **Ticketing System**: Access request tickets (provisioning workflow), access removal tickets
4. **Contractor Management**: Contract start/end dates, sponsor assignments

**Data Collection Methods**:
- **Automated**: HR system event export (hire/termination/role change)
- **Automated**: Identity system audit logs
- **Semi-Automated**: Ticketing system reports (access requests)
- **Manual**: Contractor sponsor verification

### 6.3 WB5 Sheet Structure

**Sheet 1: Instructions & Legend**

**Sheet 2: Joiner_Compliance** (40 new hires in assessment period)
- **Columns**:
  - User_ID
  - Name
  - Department
  - Job_Title
  - Hire_Date (from HR system)
  - HR_Event_Date (when HR system recorded new hire event)
  - Access_Request_Date (when access request ticket was created)
  - Approval_Date (when manager approved access request)
  - Provision_Date (when account was created and initial access granted)
  - Days_HR_to_Request (DATEDIF: HR_Event_Date to Access_Request_Date)
  - Days_Request_to_Approval (DATEDIF: Access_Request_Date to Approval_Date)
  - Days_Approval_to_Provision (DATEDIF: Approval_Date to Provision_Date)
  - Days_to_Provision (DATEDIF: Hire_Date to Provision_Date - total time)
  - Initial_Access_Complete (Y/N - did user get all required initial access?)
  - Welcome_Email_Sent (Y/N - was user notified of account creation?)
  - Compliance_Status (On-Time if Days_to_Provision ≤ 0, Late if > 0)

**Sheet 3: Mover_Compliance** (20 role changes in assessment period)
- **Columns**:
  - User_ID
  - Name
  - Old_Role
  - New_Role
  - Role_Change_Date (from HR system)
  - HR_Event_Date (when HR system recorded role change)
  - Access_Review_Trigger_Date (when access review was triggered by role change)
  - Old_Role_Access_Removed_Date (when excess access was removed)
  - New_Role_Access_Granted_Date (when new required access was granted)
  - Days_to_Remove_Old_Access (DATEDIF: Role_Change_Date to Old_Role_Access_Removed_Date)
  - Days_to_Grant_New_Access (DATEDIF: Role_Change_Date to New_Role_Access_Granted_Date)
  - Access_Review_Completed (Y/N - was access review completed after role change?)
  - Compliance_Status (On-Time if Days_to_Remove ≤ 1 AND Days_to_Grant ≤ 1, Late otherwise)

**Sheet 4: Leaver_Compliance** (30 terminations in assessment period)
- **Columns**:
  - User_ID
  - Name
  - Department
  - Termination_Date (from HR system)
  - Termination_Type (Involuntary, Voluntary Resignation, Contract End)
  - HR_Event_Date (when HR system recorded termination)
  - Disable_Date (when account was disabled)
  - Delete_Date (when account was deleted - if applicable)
  - Days_to_Disable (DATEDIF: Termination_Date to Disable_Date)
  - Data_Handover_Complete (Y/N - mailbox access, file access transferred to manager?)
  - Manager_Notified (Y/N - was manager notified of access removal?)
  - Physical_Access_Removed (Y/N - badge deactivated?)
  - Compliance_Status (On-Time if Days_to_Disable ≤ 1 for Involuntary or ≤ 0 for Voluntary, Late otherwise)

**Sheet 5: Contractor_Lifecycle** (25 contractors in assessment period)
- **Columns**:
  - User_ID
  - Name
  - Sponsor (internal employee)
  - Contract_Start
  - Contract_End
  - Provision_Date
  - Expiration_Date (date account set to auto-expire)
  - Auto_Expiration_Configured (Y/N - is auto-expiration set in identity system?)
  - Sponsor_Notified_Before_End (Y/N - was sponsor notified 7 days before contract end?)
  - Access_Removed_Date (when access was actually removed)
  - Days_to_Remove (DATEDIF: Contract_End to Access_Removed_Date)
  - Compliance_Status (On-Time if Auto_Expiration = Y AND Days_to_Remove ≤ 0, Late otherwise)

**Sheet 6: Orphaned_Account_Remediation** (15 orphaned accounts detected and remediated)
- **Columns**:
  - User_ID
  - Name
  - Detection_Date (when orphaned account was detected)
  - Detection_Method (Not in HR System, No Login 90+ Days, No Valid Owner)
  - Last_Login (or "Never")
  - Business_Owner_Contacted (Y/N - did we try to find owner?)
  - Owner_Response (Owner Confirmed Still Needed, Owner Not Reachable, No Owner Found)
  - Remediation_Action (Disabled, Deleted, Documented Exception)
  - Remediation_Date (when action was completed)
  - Days_to_Remediate (DATEDIF: Detection_Date to Remediation_Date)
  - Status (Pending, Remediated)
  - Compliance_Status (On-Time if Days_to_Remediate ≤ 30, Late if > 30)

**Sheet 7: Process_Timeliness_Metrics** (Summary timeliness statistics)
- **Joiner Metrics**:
  - Total new hires (count)
  - Joiner on-time (count, %)
  - Joiner late (count, %)
  - Average provisioning time (days)
  - Maximum provisioning delay (days)
- **Mover Metrics**:
  - Total role changes (count)
  - Mover on-time (count, %)
  - Mover late (count, %)
  - Average access modification time (days)
- **Leaver Metrics**:
  - Total terminations (count)
  - Leaver on-time (count, %)
  - Leaver late (count, %)
  - Average deprovisioning time (days)
  - Maximum deprovisioning delay (days)
- **Contractor Metrics**:
  - Total contractors (count)
  - Contractors with auto-expiration (count, %)
  - Contractors removed on time (count, %)
- **Orphaned Account Metrics**:
  - Orphaned accounts detected (count)
  - Orphaned accounts remediated (count, %)
  - Average remediation time (days)

**Sheet 8: HR_Integration_Status** (HR system integration health)
- **Metrics**:
  - HR system integration method (API, File Export, Manual)
  - Last successful sync date
  - Sync frequency (Real-Time, Daily, Weekly)
  - Sync errors detected (count)
  - Error examples (list of recent errors)
  - Data quality issues (missing hire dates, missing termination dates, etc.)

**Sheet 9: Gap_Analysis**
- **Gaps**:
  - Late provisioning (new hires not getting access by start date)
  - Late deprovisioning (terminations not processed immediately)
  - Incomplete role change handling (old access not removed, new access not granted)
  - Contractors without auto-expiration (manual removal required)
  - Orphaned accounts not remediated (detected but not cleaned up)
  - HR integration failures (sync errors preventing timely provisioning/deprovisioning)
- **Columns**: Gap_ID, User_ID, Gap_Type, Severity, Description, Root_Cause, Owner, Remediation_Plan, Target_Date, Status

**Sheet 10: Evidence_Register**

**Sheet 11: Approval_Sign_Off**

### 6.4 WB5 Key Formulas & Validation

**Joiner Timeliness**:
```
=IF(DATEDIF([Hire_Date], [Provision_Date], "D") <= 0, "On-Time", "Late")
```
Conditional Formatting:
- Green: ≤ 0 days (on time)
- Yellow: 1-3 days (slight delay)
- Red: > 3 days (significant delay)

**Leaver Timeliness**:
```
=IF([Termination_Type] = "Involuntary", 
    IF(DATEDIF([Termination_Date], [Disable_Date], "D") <= 1, "On-Time", "Late"),
    IF(DATEDIF([Termination_Date], [Disable_Date], "D") <= 0, "On-Time", "Late"))
```
- Involuntary termination: Must disable within 24h (≤1 day)
- Voluntary resignation: Disable on or before last day (≤0 days)

**Mover Timeliness**:
```
=IF(AND(Days_to_Remove_Old_Access <= 1, Days_to_Grant_New_Access <= 1), "On-Time", "Late")
```
Both old access removal AND new access grant must complete within 1 business day.

**Contractor Auto-Expiration Check**:
```
=IF([Expiration_Date] = [Contract_End], "Configured", "Not Configured")
```

### 6.5 WB5 Assessment Criteria (A.5.16)

**Compliance Thresholds**:
- **Joiner On-Time Rate**: Target ≥95% (at least 95% of new hires provisioned by start date)
- **Mover On-Time Rate**: Target ≥90% (at least 90% of role changes handled within 1 day)
- **Leaver On-Time Rate**: Target ≥98% (at least 98% of terminations deprovisioned within SLA)
- **Contractor Auto-Expiration**: Target 100% (all contractor accounts have auto-expiration configured)
- **Orphaned Account Remediation**: Target ≥90% (at least 90% of detected orphaned accounts remediated within 30 days)

**Detailed A.5.16 Score Calculation**:
```
A.5.16 Detailed Score = (Joiner % + Mover % + Leaver % + Contractor % + Orphaned Remediation %) / 5
```

**Comparison with WB1 Score**:
- WB1 provides overall lifecycle compliance (high-level)
- WB5 provides granular process compliance (detailed)
- Both should align (WB5 score should match or be very close to WB1 score for A.5.16)
- Discrepancies indicate data quality issues or methodology problems

---

## 7. Dashboard: IAM Governance Overview

### 7.1 Dashboard Purpose & Scope

**Purpose**: Provide executive summary of IAM governance maturity across all three controls (A.5.15, A.5.16, A.5.18).

**Audience**:
- **Executive Management** (CISO, CIO, CEO, Board): High-level KPIs, overall maturity
- **ISMS Team**: Gap consolidation, action planning
- **Auditors**: Compliance status per control, evidence summary

**Dashboard consolidates data from all 5 workbooks** into a single executive view.

### 7.2 Data Sources for Dashboard

**Primary Data Sources** (all from normalized workbooks):
1. **WB1 (User_Inventory.xlsx)**: User counts, lifecycle metrics, orphaned accounts
2. **WB2 (Access_Rights_Matrix.xlsx)**: Access grants, privileged access, documentation completeness
3. **WB3 (Access_Review_Results.xlsx)**: Review completion, findings, overdue reviews
4. **WB4 (Role_Compliance.xlsx)**: RBAC adoption, SoD violations
5. **WB5 (Lifecycle_Compliance.xlsx)**: Detailed joiner/mover/leaver timeliness

**Prerequisites**:
- All 5 workbooks must be generated and normalized (standard filenames)
- Workbooks must have consistent data (user IDs match across workbooks)
- Data must be current (recent assessment period)

### 7.3 Dashboard Sheet Structure

**Sheet 1: Instructions** (How to use dashboard, data sources, update frequency)

**Sheet 2: Executive_Summary** (High-level KPIs)
- **Sections**:
  
  **User Population Snapshot**:
  - Total users (from WB1)
  - Active accounts (count, %)
  - Inactive accounts (count, %)
  - Orphaned accounts (count, %)
  - Contractors (count, %)
  - Service accounts (count, %)
  
  **Overall IAM Maturity**:
  - Overall IAM Maturity Score (0-100) = (A.5.15 Score + A.5.16 Score + A.5.18 Score) / 3
  - Maturity Level (Initial, Managed, Defined, Quantitatively Managed, Optimizing)
  - Previous assessment score (if available - for trend)
  - Score change (+/-%)
  
  **Critical Gaps Summary**:
  - Total gaps identified (count across all workbooks)
  - High-severity gaps (count)
  - Medium-severity gaps (count)
  - Low-severity gaps (count)
  - Gaps in remediation (count, %)
  
  **Key Highlights**:
  - Top 3 strengths (highest-performing metrics)
  - Top 3 gaps (lowest-performing metrics or highest-risk issues)
  - Top 3 priorities (recommended immediate actions)

**Sheet 3: Compliance_Scores** (Scores per control)
- **Columns**: Control, Score (%), Status, Key Metrics, Gaps (count)
- **Rows**:
  
  **A.5.15 - Access Control**:
  - Score: (Access policy compliance + SoD compliance + Exception management + Review completion) / 4
  - Status: Excellent (≥90%), Good (80-89%), Acceptable (70-79%), Poor (<70%)
  - Key Metrics: SoD violations (count), Exception approvals (%), Review completion (%)
  - Gaps: Unresolved SoD violations, overdue reviews, exceptions without approvals
  
  **A.5.16 - Identity Management**:
  - Score: (Provisioning timeliness + Deprovisioning timeliness + Orphaned account remediation) / 3
  - Status: Excellent / Good / Acceptable / Poor
  - Key Metrics: Provisioning on-time (%), Deprovisioning on-time (%), Orphaned accounts (count)
  - Gaps: Late provisioning, late deprovisioning, unaddressed orphaned accounts
  
  **A.5.18 - Access Rights**:
  - Score: (Access documentation + Review completion + RBAC adoption + Privilege creep remediation) / 4
  - Status: Excellent / Good / Acceptable / Poor
  - Key Metrics: Justification completeness (%), Review completion (%), RBAC adoption (%)
  - Gaps: Missing documentation, overdue reviews, low RBAC adoption

**Sheet 4: WB1_User_Inventory_Summary** (Summary from Workbook 1)
- **User Inventory**:
  - Total users (by type: Employee, Contractor, Vendor, Service Account)
  - Active vs. inactive breakdown
  - Orphaned account count (% of total)
- **Lifecycle Compliance**:
  - Provisioning on-time rate (%)
  - Deprovisioning on-time rate (%)
  - Average provisioning delay (days)
  - Average deprovisioning delay (days)
- **Gaps from WB1**: Count, top 3 gaps

**Sheet 5: WB2_Access_Matrix_Summary** (Summary from Workbook 2)
- **Access Rights**:
  - Total access grants (count)
  - Privileged access grants (count, %)
  - Access by level (Read, Write, Admin - count, %)
- **Documentation**:
  - Justification completeness (%)
  - Approval documentation (%)
  - Review currency (%)
- **Gaps from WB2**: Count, top 3 gaps

**Sheet 6: WB3_Review_Summary** (Summary from Workbook 3)
- **Review Execution**:
  - Total reviews scheduled (count)
  - Reviews completed (count, %)
  - Reviews overdue (count, %)
  - Average time to complete review (days)
- **Review Findings**:
  - Access confirmed (count, %)
  - Access removed (count, %)
  - Access justified (count, %)
  - Findings remediated (count, %)
- **Gaps from WB3**: Count, top 3 gaps

**Sheet 7: WB4_Role_Summary** (Summary from Workbook 4)
- **RBAC Maturity**:
  - RBAC adoption rate (%)
  - Users with roles (count, %)
  - Users with direct access only (count, %)
  - Active roles (count)
- **SoD Compliance**:
  - SoD violations detected (count)
  - SoD violations remediated (count, %)
  - SoD violations with compensating controls (count)
- **Gaps from WB4**: Count, top 3 gaps

**Sheet 8: WB5_Lifecycle_Summary** (Summary from Workbook 5)
- **Joiner Process**:
  - New hires (count)
  - Joiner on-time rate (%)
  - Average provisioning time (days)
- **Mover Process**:
  - Role changes (count)
  - Mover on-time rate (%)
  - Average access modification time (days)
- **Leaver Process**:
  - Terminations (count)
  - Leaver on-time rate (%)
  - Average deprovisioning time (days)
- **Contractor Lifecycle**:
  - Contractors (count)
  - Auto-expiration configured (%)
- **Gaps from WB5**: Count, top 3 gaps

**Sheet 9: Gap_Consolidation** (All gaps from WB1-5 consolidated)
- **Columns**:
  - Gap_ID (unique across all workbooks: WB1-GAP-001, WB2-GAP-001, etc.)
  - Source_Workbook (WB1, WB2, WB3, WB4, WB5)
  - Control (A.5.15, A.5.16, A.5.18)
  - Gap_Type (Late Provisioning, Missing Documentation, Overdue Review, SoD Violation, etc.)
  - Severity (High, Medium, Low)
  - Description (detailed gap description)
  - Owner (person responsible for remediation)
  - Remediation_Plan (how gap will be addressed)
  - Target_Date (remediation deadline)
  - Status (Open, In Progress, Closed)
- **Total gaps**: ~60 gaps (consolidated from all workbooks)

**Sheet 10: Action_Plan** (Prioritized remediation roadmap)
- **Columns**:
  - Action_ID
  - Related_Gap_IDs (one action may address multiple gaps)
  - Action_Description (what needs to be done)
  - Priority (Critical, High, Medium, Low)
  - Owner (person responsible)
  - Target_Date (completion deadline)
  - Status (Not Started, In Progress, Completed)
  - Completion_Date
  - Verification (how completion will be verified)
- **Total actions**: ~30 prioritized actions
- **Prioritization Logic**:
  - **Critical**: High-severity gaps in A.5.16 (deprovisioning failures - security risk)
  - **High**: High-severity gaps in A.5.15/A.5.18 (SoD violations, overdue reviews)
  - **Medium**: Medium-severity gaps
  - **Low**: Low-severity gaps, process improvements

**Sheet 11: Trend_Analysis** (If historical data available)
- **Metrics Over Time**:
  - Overall IAM maturity (trend over quarters)
  - Provisioning timeliness (trend)
  - Deprovisioning timeliness (trend)
  - RBAC adoption (trend)
  - Review completion (trend)
- **Visualization**: Line charts showing progress over time

**Sheet 12: Approval_Sign_Off** (Final CISO approval of dashboard)

### 7.4 Dashboard Key Formulas & Consolidation Logic

**Overall IAM Maturity Score**:
```
=AVERAGE([A.5.15 Score], [A.5.16 Score], [A.5.18 Score])
```

**Maturity Level Mapping**:
```
=IF(IAM_Score >= 90, "Optimizing",
    IF(IAM_Score >= 80, "Quantitatively Managed",
    IF(IAM_Score >= 70, "Defined",
    IF(IAM_Score >= 60, "Managed", "Initial"))))
```

**Gap Consolidation**:
- Import Gap_Analysis sheets from WB1, WB2, WB3, WB4, WB5
- Concatenate all gaps into single list
- Deduplicate (if same gap appears in multiple workbooks)
- Assign unique Gap_IDs

**Data Validation**:
- Verify user counts match across WB1, WB2 (same user population)
- Verify access grants match between WB2 and WB3 (same access data)
- Flag discrepancies (data quality issues)

### 7.5 Dashboard Conditional Formatting

**Color Scheme**:
- **Green**: Excellent performance (≥90%), compliant, on-time
- **Yellow**: Acceptable performance (70-89%), borderline, minor gaps
- **Red**: Poor performance (<70%), non-compliant, critical gaps

**Applied to**:
- Compliance scores (per control and overall)
- Timeliness metrics (provisioning, deprovisioning, reviews)
- Gap severity (high severity = red highlight)

### 7.6 Dashboard Update Frequency

**Production Use**:
- **Monthly**: Update user inventory (WB1), orphaned account scans
- **Quarterly**: Update all workbooks, regenerate dashboard (quarterly IAM health check)
- **Annual**: Comprehensive assessment (all 6 workbooks, full dashboard refresh for external audit)

**Data Refresh Process**:
1. Regenerate WB1-5 with current data (using Python scripts)
2. Normalize workbook filenames (using normalization script)
3. Regenerate dashboard (using dashboard script - consolidates WB1-5)
4. Review dashboard for data quality (spot checks)
5. Distribute to stakeholders (CISO, ISMS team, management)

---

## 8. Evidence Collection Per Control

### 8.1 Evidence Mapping to Controls

**A.5.15 - Access Control Policy**

| Evidence Type | Description | Source Workbook | Retention |
|---------------|-------------|-----------------|-----------|
| Access control policy document | POL-S2 (A.5.15 requirements) | Policy documents | Indefinite |
| SoD matrix | Conflicting role definitions | WB4 (SoD_Matrix) | 3 years |
| SoD violation reports | Users with conflicting roles | WB4 (SoD_Violations) | 3 years |
| Exception approval records | Approved exceptions to policy | WB2, WB4 | 3 years |
| Access review completion | Review schedules and completion | WB3 (Review_Completion) | 3 years |

**A.5.16 - Identity Management**

| Evidence Type | Description | Source Workbook | Retention |
|---------------|-------------|-----------------|-----------|
| User inventory | Complete list of all users | WB1 (User_Inventory) | Current + 3 years |
| Provisioning timeliness | New hire access provisioning metrics | WB1, WB5 (Joiner_Compliance) | 3 years |
| Deprovisioning timeliness | Termination access removal metrics | WB1, WB5 (Leaver_Compliance) | 3 years |
| Orphaned account reports | Detection and remediation | WB1 (Orphaned_Accounts), WB5 | 3 years |
| Contractor lifecycle | Contract start/end, access expiration | WB1, WB5 (Contractor_Lifecycle) | 3 years |
| HR integration status | HR system sync health | WB5 (HR_Integration_Status) | 1 year |

**A.5.18 - Access Rights**

| Evidence Type | Description | Source Workbook | Retention |
|---------------|-------------|-----------------|-----------|
| Access rights matrix | User → System → Access Level | WB2 (Access_Matrix) | Current + 3 years |
| Access justification | Business justification for access | WB2 (Access_Matrix) | 3 years |
| Access approval records | Manager/owner approvals | WB2 | 3 years |
| Access review results | Review findings, removals | WB3 (Review_Findings) | 3 years |
| RBAC adoption metrics | Role assignments, direct access | WB4 (Role_Assignments) | Current + 3 years |
| Privilege creep reports | Excess access detection | WB2, WB4 | 3 years |
| Access removal logs | Access removals (terminations, reviews) | WB1, WB3 | 3 years |

### 8.2 Evidence Collection Procedures

**Monthly Evidence Collection**:
1. **User Inventory Update** (WB1):
   - Export user list from identity systems (AD, Azure AD, Okta)
   - Export employee list from HR system
   - Run user inventory script → generate WB1
   - Review for orphaned accounts (automated scan)

2. **Orphaned Account Detection**:
   - Cross-reference identity systems with HR data
   - Flag accounts not in HR system
   - Flag accounts inactive 90+ days
   - Generate remediation tasks

**Quarterly Evidence Collection**:
1. **Access Review Execution** (WB3):
   - Prepare access review data (who has access to what)
   - Distribute to reviewers (managers, system owners)
   - Track review completion
   - Run access review script → generate WB3

2. **Role Compliance Check** (WB4):
   - Export role assignments from identity systems
   - Run SoD violation detection
   - Review RBAC adoption rate
   - Run role compliance script → generate WB4

**Annual Evidence Collection**:
1. **Comprehensive IAM Assessment**:
   - Regenerate all 5 workbooks (WB1-5)
   - Normalize workbook filenames
   - Regenerate dashboard
   - Review all gaps
   - Develop annual action plan

2. **External Audit Preparation**:
   - Export evidence register from dashboard
   - Package evidence (policy documents, assessment workbooks, sample logs)
   - Prepare for auditor review

### 8.3 Evidence Retention & Storage

**Retention Periods** (per ISMS-POL-00 and regulatory requirements):
- **Current access data** (user inventory, access matrix): Current + 3 years
- **Historical assessments** (previous quarter/year workbooks): 3 years
- **Access request/removal logs**: 3 years
- **Access review records**: 3 years
- **Emergency access logs**: 7 years (security incident potential)
- **Policy documents**: Indefinite (until superseded + 3 years)

**Storage Location**:
- **Assessment workbooks**: Secure file share (access restricted to ISMS team, security, auditors)
- **Audit logs**: SIEM system or centralized log repository
- **Policy documents**: Document management system (SharePoint, Confluence, etc.)
- **Evidence packages for audit**: Dedicated audit folder (prepared on demand)

**Access Controls**:
- Evidence accessible only to authorized personnel (ISMS team, security team, internal audit, external auditors)
- Logs immutable (cannot be altered after creation)
- Evidence exports timestamped and versioned

---

## 9. Compliance Scoring Methodology

### 9.1 Control-Level Scoring

**A.5.15 - Access Control Score Calculation**:
```
A.5.15 Score = (Access Policy Compliance + SoD Compliance + Exception Management + Review Completion) / 4

Where:
- Access Policy Compliance = 100% if policy exists and is current, 0% otherwise
- SoD Compliance = (1 - (Unresolved SoD Violations / Total Users)) × 100
- Exception Management = (Exceptions with Approvals / Total Exceptions) × 100
- Review Completion = (Completed Reviews / Scheduled Reviews) × 100
```

**A.5.16 - Identity Management Score Calculation**:
```
A.5.16 Score = (Provisioning Timeliness + Deprovisioning Timeliness + Orphaned Remediation) / 3

Where:
- Provisioning Timeliness = (On-Time Provisioning / Total Provisioning) × 100
- Deprovisioning Timeliness = (On-Time Deprovisioning / Total Deprovisioning) × 100
- Orphaned Remediation = (Orphaned Remediated / Orphaned Detected) × 100
```

**A.5.18 - Access Rights Score Calculation**:
```
A.5.18 Score = (Access Documentation + Review Completion + RBAC Adoption + Removal Timeliness) / 4

Where:
- Access Documentation = (Access with Justification + Access with Approval + Access Reviewed) / 3
- Review Completion = (Completed Reviews / Scheduled Reviews) × 100
- RBAC Adoption = (Users with Roles / Total Users) × 100
- Removal Timeliness = (On-Time Removals / Total Removals) × 100
```

### 9.2 Overall IAM Maturity Score

```
Overall IAM Maturity Score = (A.5.15 Score + A.5.16 Score + A.5.18 Score) / 3
```

**Maturity Levels**:
- **90-100%**: Optimizing (Best-in-class IAM governance)
- **80-89%**: Quantitatively Managed (Strong IAM governance, minor gaps)
- **70-79%**: Defined (Documented processes, consistent execution needed)
- **60-69%**: Managed (Basic processes in place, significant gaps)
- **<60%**: Initial (Ad-hoc IAM, major governance gaps)

### 9.3 Gap Severity Scoring

**Severity Levels**:
- **High**: Security risk (orphaned admin accounts, late deprovisioning for terminations, unresolved SoD violations)
- **Medium**: Compliance risk (overdue reviews, missing documentation, low RBAC adoption)
- **Low**: Process improvement (minor delays, incomplete metadata)

**Severity Assignment Logic**:
```
IF (Gap affects A.5.16 deprovisioning OR privileged access) THEN High
ELSE IF (Gap affects A.5.15 SoD OR A.5.18 reviews) THEN Medium
ELSE Low
```

### 9.4 Trend Analysis (If Historical Data Available)

**Quarter-over-Quarter Comparison**:
- Compare current quarter score to previous quarter
- Calculate change (+/- %)
- Identify improving vs. declining metrics
- Report trends to management (are we getting better or worse?)

**Year-over-Year Comparison**:
- Compare annual assessment to previous year
- Measure long-term progress
- Validate that action plans are effective

---

## 10. Continuous Assessment Approach

### 10.1 Continuous vs. Point-in-Time Assessment

**Traditional Approach** (Point-in-Time):
- Annual IAM assessment (once per year)
- Snapshot of current state
- Gaps identified but may not be addressed until next assessment

**Continuous Approach** (Recommended):
- **Monthly**: User inventory updates, orphaned account scans
- **Quarterly**: Access reviews (critical systems), role compliance checks
- **Annual**: Comprehensive assessment (all 6 workbooks)
- **Continuous**: Automated monitoring (provisioning delays, deprovisioning failures)

**Benefits of Continuous Assessment**:
- Early detection of gaps (fix before they become critical)
- Real-time visibility into IAM health
- Reduced audit preparation burden (always audit-ready)
- Proactive remediation vs. reactive

### 10.2 Automated Monitoring & Alerting

**Automated Monitoring Opportunities**:

**1. Provisioning Delays**:
- **Monitor**: New hire events in HR system
- **Alert**: If account not created within 1 day of hire date
- **Action**: Escalate to IT operations (provision immediately)

**2. Deprovisioning Failures**:
- **Monitor**: Termination events in HR system
- **Alert**: If account not disabled within 1 hour (involuntary) or 1 day (voluntary)
- **Action**: Immediate escalation to security team (critical security risk)

**3. Orphaned Account Detection**:
- **Monitor**: Monthly cross-reference of identity systems with HR data
- **Alert**: Accounts not in HR system OR inactive 90+ days
- **Action**: Generate cleanup tickets

**4. Access Review Overdue**:
- **Monitor**: Review due dates in access review platform
- **Alert**: If review not completed by due date
- **Action**: Escalate to reviewer's manager

**5. SoD Violations**:
- **Monitor**: Role assignments in identity systems
- **Alert**: If user assigned to conflicting roles (per SoD matrix)
- **Action**: Immediate notification to security team, user's manager

**6. Privileged Access Without Quarterly Review**:
- **Monitor**: Privileged access assignments
- **Alert**: If privileged access not reviewed in 90 days
- **Action**: Trigger privileged access review

**Implementation**:
- Use SIEM, access governance platform, or custom scripts
- Integrate with ticketing system (auto-create tickets for failures)
- Integrate with alerting system (email, Slack, PagerDuty)

### 10.3 Continuous Improvement Cycle

```
┌──────────────────────────────────────────────────────────────┐
│         CONTINUOUS IAM GOVERNANCE IMPROVEMENT CYCLE          │
└──────────────────────────────────────────────────────────────┘

1. MEASURE
   - Monthly: User inventory, orphaned accounts
   - Quarterly: Access reviews, role compliance, lifecycle metrics
   - Annual: Comprehensive IAM assessment
   ↓

2. ANALYZE
   - Identify gaps (compare actual vs. target)
   - Determine root causes (why are we missing targets?)
   - Prioritize gaps (by risk and effort)
   ↓

3. PLAN
   - Develop remediation actions (specific, measurable)
   - Assign owners (accountability)
   - Set target dates (deadlines)
   ↓

4. IMPLEMENT
   - Execute remediation actions (close gaps)
   - Document changes (what was done)
   - Verify effectiveness (did it work?)
   ↓

5. REVIEW
   - Reassess IAM metrics (did scores improve?)
   - Validate gap closure (are gaps actually resolved?)
   - Adjust approach (if remediation ineffective)
   ↓

   [Return to MEASURE - continuous cycle]
```

### 10.4 Integration with ISMS Continuous Improvement

**IAM assessment feeds into broader ISMS processes**:

**1. Risk Assessment** (ISMS-A.5.9):
- Orphaned accounts = information security risk
- Late deprovisioning = access control risk
- SoD violations = fraud risk
- IAM gaps identified → risk register updated

**2. Internal Audit** (ISMS-A.5.37):
- IAM assessment provides evidence for internal audit
- Dashboard highlights areas requiring audit focus
- Evidence register expedites audit response

**3. External Audit** (ISO 27001 certification):
- Assessment workbooks provide compliance evidence
- Dashboard demonstrates systematic governance
- Gap remediation shows continuous improvement

**4. Incident Management** (ISMS-A.5.24):
- Compromised accounts detected via orphaned account scans
- Unauthorized access detected via access reviews
- IAM failures trigger security incidents

**5. Management Review** (ISO 27001 Clause 9.3):
- IAM maturity score reported to management
- Trend analysis shows improvement over time
- Gap action plan demonstrates commitment

---

## Appendix A: Assessment Workbook Cross-Reference Matrix

| Metric | Primary Source | Secondary Source | Used in Dashboard |
|--------|---------------|------------------|-------------------|
| Total Users | WB1 (User_Inventory) | WB2 (Access_Matrix) | Executive_Summary |
| Provisioning Timeliness | WB1 (Employee_Lifecycle) | WB5 (Joiner_Compliance) | WB1_Summary, WB5_Summary |
| Deprovisioning Timeliness | WB1 (Employee_Lifecycle) | WB5 (Leaver_Compliance) | WB1_Summary, WB5_Summary |
| Orphaned Accounts | WB1 (Orphaned_Accounts) | WB5 (Orphaned_Remediation) | WB1_Summary |
| Access Grants | WB2 (Access_Matrix) | - | WB2_Summary |
| Privileged Access | WB2 (Privileged_Access) | - | WB2_Summary |
| Access Documentation | WB2 (Access_Documentation) | - | WB2_Summary, Compliance_Scores |
| Review Completion | WB3 (Review_Completion) | - | WB3_Summary, Compliance_Scores |
| Review Findings | WB3 (Review_Findings) | - | WB3_Summary |
| RBAC Adoption | WB4 (Role_Assignments) | - | WB4_Summary, Compliance_Scores |
| SoD Violations | WB4 (SoD_Violations) | - | WB4_Summary, Compliance_Scores |
| Joiner Compliance | WB5 (Joiner_Compliance) | WB1 (Employee_Lifecycle) | WB5_Summary |
| Mover Compliance | WB5 (Mover_Compliance) | - | WB5_Summary |
| Leaver Compliance | WB5 (Leaver_Compliance) | WB1 (Employee_Lifecycle) | WB5_Summary |
| Contractor Lifecycle | WB5 (Contractor_Lifecycle) | WB1 (Contractor_Lifecycle) | WB5_Summary |

**Data Consistency Checks**:
- Total Users in WB1 should match Users in WB2 (same population)
- Provisioning/Deprovisioning metrics in WB1 should align with WB5 (detailed vs. summary)
- Access review data in WB3 should reference users from WB1 (consistent user IDs)
- Role assignments in WB4 should reference users from WB1 (consistent user IDs)

---

## Appendix B: Assessment Frequency Matrix

| Assessment Activity | Frequency | Owner | Deliverable |
|---------------------|-----------|-------|-------------|
| User inventory update | Monthly | IAM Team | WB1 refreshed |
| Orphaned account scan | Monthly | IAM Team | WB1 (Orphaned_Accounts) |
| Access review (critical systems) | Quarterly | System Owners | WB3 updated |
| Role compliance check | Quarterly | IAM Team | WB4 refreshed |
| RBAC adoption review | Quarterly | IAM Team | WB4 (RBAC_Metrics) |
| Lifecycle compliance analysis | Quarterly | IAM Team | WB5 refreshed |
| Dashboard update | Quarterly | ISMS Team | Dashboard regenerated |
| Comprehensive IAM assessment | Annual | ISMS Team | All 6 workbooks + Dashboard |
| External audit preparation | Annual | ISMS Team | Evidence package |

---

## Appendix C: Technology-Specific Data Collection Examples

**Active Directory (On-Premises)**:
- User inventory: `Get-ADUser -Filter *`
- Group memberships: `Get-ADGroupMember`
- Last login: `Get-ADUser -Properties LastLogonDate`
- Account status: `Get-ADUser -Properties Enabled`

**Azure Active Directory (Cloud)**:
- User inventory: Microsoft Graph API `/users`
- Role assignments: Graph API `/roleManagement/directory/roleAssignments`
- Last login: `signInActivity` property
- License assignments: Graph API `/users/{id}/licenseDetails`

**Okta (Cloud Identity Platform)**:
- User inventory: Okta API `/api/v1/users`
- Group memberships: `/api/v1/users/{id}/groups`
- App assignments: `/api/v1/apps/{id}/users`
- Last login: `lastLogin` property

**HR System (Workday, SAP SuccessFactors)**:
- Employee list: HR report export (CSV or API)
- Hire/termination dates: HR event feed
- Department/manager: Employee master data
- Job title/role: Position data

**Ticketing System (ServiceNow, Jira)**:
- Access requests: Ticket export (filtered by category)
- Approvals: Workflow state data
- Request→Provision time: Ticket open→close timestamps

---

**END OF POL-S5: Assessment Methodology & Evidence Framework**

This section provides comprehensive assessment methodology across all three controls (A.5.15, A.5.16, A.5.18), defining 6 assessment workbooks, consolidated dashboard, evidence collection procedures, compliance scoring, and continuous assessment approach.

**Next Deliverable**: Implementation guidance sections (ISMS-IMP-A.5.15-16-18-S1 through S5)
