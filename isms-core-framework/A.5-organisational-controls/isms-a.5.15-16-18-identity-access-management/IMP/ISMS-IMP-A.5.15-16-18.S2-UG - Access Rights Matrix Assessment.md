<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.15-16-18.S2-UG:framework:UG:a.5.15-16-18 -->
**ISMS-IMP-A.5.15-16-18.S2-UG - Access Rights Matrix Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Access Rights Matrix Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.15-16-18.S2-UG |
| **Related Policy** | ISMS-POL-A.5.15-16-18 (Identity Access Management) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.15 (Access Annex) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.5.15-16-18 (Identity Access Management)
- ISMS-IMP-A.5.15-16-18.S1 (User Inventory & Lifecycle Compliance Assessment)
- ISMS-IMP-A.5.15-16-18.S3 (Access Review Results Assessment)
- ISMS-IMP-A.5.15-16-18.S4 (Role Definition & SoD Compliance Assessment)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.15-16-18.S2-TG.

---

### Workbook at a Glance

This workbook contains the following 11 sheets:

| Sheet | Purpose |
|-------|---------|
| **Instructions & Legend** | Assessment guidance, rating definitions, and field descriptions |
| **Access Matrix** | Current state access rights mapped by system, role, and user |
| **Role Assignments** | Mapping of users to roles across all assessed systems |
| **Group Memberships** | Group and distribution list membership records |
| **Privileged Access** | Inventory and assessment of privileged and administrative accounts |
| **Access Documentation** | Documentation quality and completeness assessment |
| **Coverage Analysis** | Coverage metrics for access rights documentation |
| **Gap Analysis** | Identified gaps and remediation action tracking |
| **Summary Dashboard** | Compliance overview auto-populated from your input data |
| **Evidence Register** | Tracking of supporting evidence for audit purposes |
| **Approval Sign-Off** | Stakeholder sign-off and approval workflow |

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.15-16-18.S2 - Access Rights Matrix Assessment

#### What This Assessment Covers

This assessment documents your COMPLETE ACCESS RIGHTS MATRIX - the mapping of WHO has access to WHAT and WHY. This answers:

- Which users have access to which systems/applications/data?
- What level of access does each user have? (Read, Write, Admin, Privileged)
- What is the business justification for each access grant?
- When was access granted, by whom, and with whose approval?
- Which access is via group membership vs. direct assignment?
- Which access is time-bound (contractors, temporary access)?
- How sensitive is the data being accessed (Restricted, Confidential, Internal, Public)?
- Which users have privileged/administrative access?

#### Key Principle

This assessment is **completely technology-agnostic and vendor-independent**. You document YOUR access architecture (whatever systems you use - on-premises, cloud, SaaS, custom - whatever), and verify access rights against policy requirements.

#### What You'll Document

- **Access Rights Matrix**: User-to-system-to-access-level mapping
  - User ID → System/Application → Access Level (Read, Write, Admin, Privileged)
  - Group memberships granting access
  - Role assignments granting access
  - Direct access assignments (not via group/role)

- **Access Documentation**:
  - Business justification (why was access granted?)
  - Approval date and approver (who approved this access?)
  - Last review date (when was this access last verified?)
  - Access expiration date (for time-bound access)

- **Access Classification**:
  - Data sensitivity (what level of sensitive data can user access?)
  - Privileged access flag (is this admin/root/elevated access?)
  - Segregation of duties conflicts (does this access violate SoD requirements?)

- **Gap Analysis**:
  - Access without business justification (documented but no reason)
  - Access never reviewed (granted but never verified)
  - Excessive access (user has more than needed for job function)
  - Undocumented access (access exists but not in access matrix)

#### How This Relates to Other A.5.15-16-18 Assessments

| Assessment | Focus | Relationship to A.5.15-16-18.2 |
|------------|-------|--------------------------------|
| ISMS-IMP-A.5.15-16-18.S1 | User Inventory & Lifecycle | Provides user list (.2 uses this as baseline) |
| **ISMS-IMP-A.5.15-16-18.S2** | **Access Rights Matrix** | **WHAT access do users have** |
| ISMS-IMP-A.5.15-16-18.S3 | Access Review Results | Uses access matrix (.2) to determine WHAT to review |
| ISMS-IMP-A.5.15-16-18.S4 | Role & SoD Compliance | Uses access via roles (from .2) to detect SoD violations |
This assessment (A.5.15-16-18.2) provides the **foundational access rights mapping** used by access review and SoD detection!

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **System Owners** - Define who should have access to their systems
2. **IAM Team** - Extract access data from identity and application systems
3. **IT Operations** - Understand technical access configurations
4. **Security Team** - Assess privileged access and data sensitivity
5. **Managers** - Verify their direct reports have appropriate access

#### Required Skills

- Understanding of access control systems (AD groups, Entra ID roles, application permissions)
- Access to application admin consoles or reporting tools
- Data classification knowledge (what's Restricted vs. Confidential vs. Internal)
- Understanding of segregation of duties requirements
- Basic understanding of ISO 27001 Control A.5.18

#### Time Commitment

- **Initial assessment:** 20-30 hours (extract access data from all systems, build access matrix, document justifications)
- **Monthly updates:** 4-6 hours (update access grants, remove leavers, update group memberships)
- **Quarterly comprehensive review:** 10-12 hours (verify all access, update justifications, assess gaps)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete access rights matrix** - Every user's access to every system documented
2. ✅ **Access classification** - Privileged access flagged, data sensitivity tagged
3. ✅ **Business justification documentation** - Why each access was granted
4. ✅ **Group/role mapping** - Which access is via groups, which is direct
5. ✅ **Time-bound access tracking** - Contractor/temporary access with expiration dates
6. ✅ **Access documentation completeness score** - % access with justification, approval, review
7. ✅ **Excessive access analysis** - Users with more access than job function requires
8. ✅ **Evidence register** - Supporting documentation for audit
9. ✅ **Approved assessment** - Three-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. User Inventory (from IMP.1)

- Complete user list from ISMS-IMP-A.5.15-16-18.S1 Sheet 2 (User_Inventory_Master_List)
- User ID, name, email, user type, department, manager
- This provides the baseline "WHO" for the access matrix

#### 2. System/Application Inventory

- Complete list of systems and applications requiring access control
- System name, description, criticality (Critical, High, Medium, Low)
- Data sensitivity (what level of sensitive data does system contain?)
- System owner (who is accountable for access to this system?)

#### 3. Access Data Exports

For EACH system/application:

- User access lists (who has access, what level)
- Group memberships (AD groups, Entra ID groups, application groups)
- Role assignments (if RBAC implemented)
- Direct access assignments (users with access not via group/role)
- Administrative/privileged access (admin, root, elevated access)

#### 4. Access Documentation

- Access request tickets (from ticketing system)
- Access approval records (manager approvals, system owner approvals)
- Business justification documentation (why access was granted)
- Access review records (when was access last verified?)

#### 5. Policy Requirements

- ISMS-POL-A.5.15-16-18, Section 2.3 (Access Rights Management Requirements - A.5.18)
  - Section 2.3.1: Access Rights Assignment
  - Section 2.3.2: Role Definition and RBAC
  - Section 2.3.3: Group Membership Management
  - Section 2.3.8: Access Rights Documentation

### Required Tools

- **Microsoft Excel** (2016 or later) for workbook completion
- **Identity system admin tools** (AD, Entra ID, Okta for group membership exports)
- **Application admin consoles** (for application-specific access)
- **Ticketing system access** (for access request and approval records)
- **Screen capture tools** (for evidence screenshots)

### Dependencies

**CRITICAL DEPENDENCY:**

- **ISMS-IMP-A.5.15-16-18.S1** (User Inventory) MUST be completed first
- This assessment uses the user list from IMP.1 as baseline

**Outputs FROM this assessment feed INTO:**

- A.5.15-16-18.3 (Access Review Results) - Uses access matrix to define review scope
- A.5.15-16-18.4 (Role & SoD Compliance) - Uses access data to detect SoD violations

---

## Workflow

### High-Level Process

```
1. PREPARE
   ↓
2. BUILD SYSTEM INVENTORY (what systems exist?)
   ↓
3. EXTRACT ACCESS DATA (from each system)
   ↓
4. BUILD ACCESS RIGHTS MATRIX (Sheet 2)
   ↓
5. CLASSIFY ACCESS (privileged, data sensitivity)
   ↓
6. DOCUMENT GROUP/ROLE ACCESS (Sheet 3)
   ↓
7. DOCUMENT JUSTIFICATIONS (Sheet 4)
   ↓
8. IDENTIFY EXCESSIVE ACCESS (Sheet 5)
   ↓
9. CALCULATE COMPLETENESS SCORE (Summary Dashboard)
   ↓
10. IDENTIFY GAPS (Gap Analysis)
    ↓
11. REGISTER EVIDENCE (Evidence Register)
    ↓
12. REVIEW & APPROVE (Approval Sign-Off)
```

### Detailed Workflow

#### Phase 1: Preparation (2-3 hours)

**Objective:** Gather information and understand requirements

**Steps:**
1. Read this entire User Guide
2. Read ISMS-POL-A.5.15-16-18, Section 2.3 (Access Rights Management)
3. Obtain user inventory from IMP.1 (ISMS-IMP-A.5.15-16-18.S1 Sheet 2)
4. Identify ALL systems and applications requiring access control
5. Schedule time with System Owners and IAM Team for data collection
6. Create working folder for evidence collection

**Deliverable:** List of all systems/applications and data collection plan

**Quality Check:**

- ✓ User inventory from IMP.1 available and current
- ✓ All systems identified (don't miss cloud applications, SaaS tools)
- ✓ System owners identified and available
- ✓ Policy requirements reviewed and understood

---

#### Phase 2: Build System/Application Inventory (3-4 hours)

**Objective:** Complete Sheet 1 - System Inventory

**Steps:**

1. **List ALL Systems and Applications**:

   - On-premises applications (ERP, CRM, HR, Finance, custom apps)
   - Cloud/SaaS applications (Microsoft 365, Salesforce, Workday, etc.)
   - Databases (SQL Server, Oracle, MySQL, MongoDB)
   - Infrastructure systems (AD, Entra ID, Okta, LDAP)
   - Network devices (firewalls, switches, routers if they have user access)
   - Development tools (GitLab, Jenkins, development environments)

2. **For EACH system, document**:

   - System ID (unique identifier, e.g., SYS-001)
   - System Name (what YOU call it)
   - Description (what does this system do?)
   - System Type (Application, Database, Infrastructure, Network, Development, Other)
   - Deployment Model (On-Premises, Cloud SaaS, Hybrid)
   - System Owner (who is accountable for access to this system?)
   - Criticality (Critical, High, Medium, Low - business impact if unavailable)
   - Data Sensitivity (Restricted, Confidential, Internal, Public - highest sensitivity data in system)

3. **Verify completeness**:

   - Cross-check with asset inventory
   - Ask IT Operations: "What systems do users log into?"
   - Ask System Owners: "What applications do your teams use?"
   - Check cloud service subscriptions

**Deliverable:** Complete Sheet 1 with all systems/applications

**Quality Check:**

- ✓ All systems identified (on-premises + cloud + SaaS)
- ✓ No "Unknown" or "TBD" values
- ✓ System owners assigned and verified
- ✓ Criticality reflects actual business impact
- ✓ Data sensitivity accurately categorized

---

#### Phase 3: Extract Access Data from Each System (10-15 hours)

**Objective:** Export access data from EVERY system

**Steps:**

**For Active Directory Groups:**
```powershell
# Export all groups and members
Get-ADGroup -Filter * -Properties Members | ForEach-Object {
    $group = $_
    $group.Members | ForEach-Object {
        [PSCustomObject]@{
            GroupName = $group.Name
            UserDN = $_
        }
    }
} | Export-Csv -Path "AD_Group_Memberships.csv" -NoTypeInformation
```

**For Entra ID Roles and Groups:**
```powershell
# Using Microsoft Graph PowerShell SDK
Connect-MgGraph -Scopes "Group.Read.All", "GroupMember.Read.All"
Get-MgGroup -All | ForEach-Object {
    $group = $_
    Get-MgGroupMember -GroupId $group.Id | ForEach-Object {
        [PSCustomObject]@{
            GroupName = $group.DisplayName
            UserPrincipalName = $_.AdditionalProperties.userPrincipalName
        }
    }
} | Export-Csv -Path "EntraID_Group_Memberships.csv" -NoTypeInformation
```

**For Application-Specific Access:**

- **SaaS Applications** (Salesforce, Workday, etc.):
  - Use admin console → Users → Export to CSV
  - OR use application API (Salesforce API, Workday API)
- **Databases** (SQL Server, Oracle, MySQL):
  - Query system tables for user permissions
  - Example SQL: `SELECT * FROM sys.database_permissions`
- **Custom Applications**:
  - Work with application owners to export user access data
  - May require custom scripts or database queries

**For Each System, Export:**

- User ID → Access Level (Read, Write, Admin, Privileged)
- Group memberships (if access is via group)
- Role assignments (if access is via role)
- Direct permissions (if access is not via group/role)

**Consolidation Step:**

- Map user identifiers (AD SamAccountName → Entra ID UPN → Application UserID)
- Tag each access record with source system

**Deliverable:** Collected access data for all systems

**Quality Check:**

- ✓ All systems queried for access data
- ✓ Access levels categorized consistently (Read, Write, Admin, Privileged)
- ✓ Group/role access identified (not just direct access)
- ✓ User identifiers mapped across systems
- ✓ Source system tagged for each access record

---

#### Phase 4: Build Access Rights Matrix (6-8 hours)

**Objective:** Complete Sheet 2 - Access Rights Matrix

**Steps:**

1. **Import user list** from IMP.1 (baseline "WHO")
2. **Import system list** from Sheet 1 (baseline "WHAT")
3. **For EACH user-system pair, document**:

   - Does user have access? (Yes/No)
   - If yes, what access level? (Read, Write, Admin, Privileged)
   - How is access granted? (Direct, Group Membership, Role Assignment)
   - Which group(s) grant access? (if via group)
   - Which role(s) grant access? (if via role)
   - When was access granted? (from access request ticket or audit log)
   - Who approved access? (from access request approval)
   - Business justification (why was access granted?)
   - Last review date (when was this access last verified?)
   - Access expiration date (for contractors, time-bound access)

4. **Classify access**:

   - **Privileged Access Flag**: Is this admin/root/elevated access? (Yes/No)
   - **Data Sensitivity**: What sensitivity level can user access via this system? (Restricted/Confidential/Internal/Public)
   - **SoD Conflict**: Does this access violate segregation of duties? (flagged later in IMP.4)

5. **Calculate derived fields**:

   - Days since access granted (Today - Access Grant Date)
   - Days since last review (Today - Last Review Date)
   - Access documentation completeness (justification + approval + review = complete)

**Deliverable:** Complete Sheet 2 with access rights matrix

**Quality Check:**

- ✓ All users from IMP.1 included in matrix
- ✓ All systems from Sheet 1 included in matrix
- ✓ Access levels categorized consistently
- ✓ Group/role access documented (not just "Yes - has access")
- ✓ Privileged access flagged
- ✓ Data sensitivity tagged
- ✓ Documentation fields populated where available

---

#### Phase 5: Document Group and Role Access (3-4 hours)

**Objective:** Complete Sheet 3 - Group and Role Mapping

**Steps:**

1. **List ALL groups** that grant access:

   - Active Directory groups
   - Entra ID groups
   - Application-specific groups (Salesforce profiles, Workday security groups, etc.)

2. **For EACH group, document**:

   - Group ID (unique identifier)
   - Group Name
   - Group Purpose (what does this group grant access to?)
   - Systems/Applications Accessed (via this group)
   - Access Level Granted (what level of access does group membership give?)
   - Group Owner (who is accountable for membership?)
   - Member Count (how many users in this group?)
   - Last Membership Review Date (when was membership last verified?)

3. **List ALL roles** that grant access (if RBAC implemented):

   - Role ID, Role Name
   - Systems/Applications Accessed (via this role)
   - Access Level Granted
   - Users Assigned to Role (count)
   - Role Last Reviewed Date

4. **Cross-reference with Sheet 2**:

   - Verify all groups mentioned in Sheet 2 are documented in Sheet 3
   - Verify all roles mentioned in Sheet 2 are documented in Sheet 3

**Deliverable:** Complete Sheet 3 with group and role mapping

**Quality Check:**

- ✓ All groups granting access documented
- ✓ Group owners identified
- ✓ Member counts accurate
- ✓ Access granted by group clearly documented
- ✓ Roles documented (if RBAC implemented)
- ✓ Cross-references to Sheet 2 verified

---

#### Phase 6: Document Business Justifications (2-3 hours)

**Objective:** Complete Sheet 4 - Access Justification Documentation

**Steps:**

1. **For EACH access grant in Sheet 2, verify business justification**:

   - Why does this user need this access?
   - What business function requires this access?
   - Job role requirement (e.g., "Finance Analyst role requires access to ERP for reporting")
   - Project requirement (e.g., "Temporary access for Q1 audit project")
   - Manager approval (e.g., "Manager John Doe approved access on 2025-01-15")

2. **Collect justification documentation**:

   - Access request tickets (from ServiceNow, Jira, etc.)
   - Manager approval emails
   - HR system job descriptions (job role → required access mapping)
   - Project charters (project team → required access)

3. **Categorize justification completeness**:

   - **✅ Complete**: Justification documented, approver identified, approval date recorded
   - **⚠️ Partial**: Justification exists but missing approver or date
   - **❌ Missing**: No justification documented

4. **Calculate metrics**:

   - Total access grants
   - Access with complete justification (count, percentage)
   - Access with partial justification (count, percentage)
   - Access with missing justification (count, percentage)
   - **Documentation Completeness Score** = (Complete / Total) × 100%

**Deliverable:** Sheet 4 with justification documentation analysis

**Quality Check:**

- ✓ All access grants from Sheet 2 assessed for justification
- ✓ Justification sources documented (ticket ID, email, approval record)
- ✓ Completeness categorization accurate
- ✓ Missing justifications flagged for remediation
- ✓ Documentation completeness score calculated

---

#### Phase 7: Identify Excessive Access (3-4 hours)

**Objective:** Complete Sheet 5 - Excessive Access Analysis

**Steps:**

1. **Define "required access" baseline**:

   - For each job role/function, define required access
   - Example: "Finance Analyst" role requires:
     - ERP (Read-only for reporting)
     - BI Tool (Write for dashboard creation)
     - Email/Collaboration (Standard access)
   - Document this as "role-to-access mapping"

2. **Compare actual access vs. required access**:

   - For EACH user, compare their actual access (from Sheet 2) to their required access (based on job role)
   - Identify excess access:
     - Access to systems not required for job function
     - Higher access level than required (e.g., Write when only Read needed)
     - Multiple system access when only one required (e.g., access to both Test and Prod when only Test needed)

3. **Categorize excessive access**:

   - **Legitimate Excess**: Documented reason (e.g., "Also supporting Project X", "Backup for Manager")
   - **Questionable Excess**: No clear reason, requires manager review
   - **Privilege Creep**: User accumulated access from previous roles, never removed

4. **Calculate metrics**:

   - Total users assessed
   - Users with excess access (count, percentage)
   - Users with legitimate excess (justified)
   - Users with questionable excess (no justification, requires review)
   - Systems most commonly over-granted (which systems have most excessive access?)

**Deliverable:** Sheet 5 with excessive access analysis

**Quality Check:**

- ✓ Job role → required access mapping defined
- ✓ All users compared against required access baseline
- ✓ Excessive access accurately identified
- ✓ Legitimate excess access has documented justification
- ✓ Questionable excess flagged for manager review

---

#### Phase 8: Calculate Documentation Completeness Score (1-2 hours)

**Objective:** Calculate access rights documentation completeness and record findings in the Summary Dashboard

**Steps:**

1. **Collect metrics** from assessment sheets:

   - Total access grants (from Access Matrix sheet)
   - Access with complete documentation (from Access Documentation sheet)
   - Privileged access count (from Privileged Access sheet)
   - Access to restricted/confidential data (from Access Matrix sheet)
   - Excessive access count (from Coverage Analysis sheet)
   - Group-based access vs. direct access (from Role Assignments and Group Memberships sheets)

2. **Calculate overall access rights documentation score**:
   ```
   Documentation Score =
     (Justification Completeness × 40%) +
     (Approval Documentation × 30%) +
     (Review Currency × 20%) +
     (Access Accuracy × 10%)
   ```

3. **Benchmark against industry standards**:

   - **Excellent (90-100%)**: Best-in-class access documentation
   - **Good (75-89%)**: Strong documentation, minor gaps
   - **Fair (60-74%)**: Acceptable but significant documentation gaps
   - **Poor (<60%)**: Major documentation deficiencies, audit risk

4. **Document findings**:

   - Strengths (areas of compliance)
   - Weaknesses (areas of non-compliance)
   - Root causes (why is documentation incomplete?)
   - Recommendations (how to improve)

**Deliverable:** Documentation completeness score recorded in Gap Analysis and tracked in Summary Dashboards

**Quality Check:**

- ✓ All metrics calculated correctly
- ✓ Overall documentation score formula applied correctly
- ✓ Benchmark categories accurate
- ✓ Findings documented clearly

---

#### Phase 9: Identify Gaps and Remediation Plan (2-3 hours)

**Objective:** Complete Sheet 7 - Gap Analysis & Remediation Plan

**Steps:**

1. **Identify all gaps** from previous sheets:

   - **Access without justification** (from Sheet 4)
   - **Access never reviewed** (from Sheet 2)
   - **Excessive access** (from Sheet 5)
   - **Undocumented group/role access** (from Sheet 3)
   - **Privileged access without approval** (from Sheet 2)

2. **Prioritize gaps by risk**:

   - **Critical** (P1):
     - Privileged access without justification/approval
     - Access to Restricted data without documented approval
     - Excessive access to critical systems
   - **High** (P2):
     - Access to Confidential data without justification
     - Access never reviewed (>365 days)
     - Undocumented group memberships granting access
   - **Medium** (P3):
     - Access to Internal data without recent review
     - Partial documentation (justification but no approver)
   - **Low** (P4):
     - Access to Public data without full documentation
     - Minor documentation gaps

3. **Create remediation actions**:

| Gap ID | Gap Description | Priority | Action | Owner | Target Date | Status |
|--------|----------------|----------|--------|-------|-------------|--------|
| GAP-001 | 15 users with privileged access, no approval documented | Critical | Obtain retroactive CISO approval or remove access | Security Team | 14 days | Open |
| GAP-002 | 50 users with access never reviewed (>365 days) | High | Trigger access review for all users | Managers | 30 days | Open |
| GAP-003 | 25 users with excessive access to ERP | Medium | Manager review, remove excess access | Finance Manager | 45 days | Open |

4. **Track remediation progress**:

   - Action completion status (Open, In Progress, Completed)
   - Percent complete (0%, 25%, 50%, 75%, 100%)
   - Notes on progress or blockers

**Deliverable:** Sheet 7 with gap analysis and remediation plan

**Quality Check:**

- ✓ All gaps identified from previous sheets
- ✓ Prioritization reflects actual risk
- ✓ Remediation actions specific and actionable
- ✓ Owners assigned for each action
- ✓ Target dates realistic but urgent for critical gaps

---

#### Phase 10: Register Evidence (1 hour)

**Objective:** Complete Sheet 8 - Evidence Register

**Steps:**

1. **List all evidence collected**:

   - Access data exports (AD groups, Entra ID roles, application access)
   - Access request tickets (examples)
   - Manager approval emails (examples)
   - System owner confirmations (who should have access)
   - Screenshots (access matrices, group memberships)
   - Policy documents (ISMS-POL-A.5.15-16-18, Section 2.3)

2. **For EACH piece of evidence, document**:

   - Evidence ID (EVID-001, EVID-002, etc.)
   - Evidence Type (Data Export, Screenshot, Approval Email, Policy Document, etc.)
   - Description (what is this evidence?)
   - Related Sheet/Row (where is this evidence referenced?)
   - Location/Path (file path, URL, ticket system)
   - Date Collected (when was this evidence captured?)
   - Collected By (who gathered this evidence?)
   - Verification Status (Verified, Pending, Not Verified)

3. **Organize evidence** in logical folder structure

4. **Verify evidence quality**:

   - All evidence recent (< 30 days old for access data)
   - Evidence accessible to auditors
   - Evidence clearly labeled

**Deliverable:** Sheet 8 with complete evidence register

**Quality Check:**

- ✓ All evidence collected and documented
- ✓ Evidence organised in logical folder structure
- ✓ Evidence IDs cross-referenced to assessment sheets
- ✓ All evidence verified as accurate and current

---

#### Phase 11: Review & Approval (2-3 hours)

**Objective:** Three-level approval process (Sheet 9 - Approval & Sign-Off)

**Steps:**

**Step 1: Self-Review** (Assessment Completer)

- Run through Quality Checklist
- Verify all sheets complete
- Check formulas calculating correctly
- Validate data accuracy
- Ensure evidence collected

**Step 2: System Owner Review**

- Review access to THEIR systems (is it accurate?)
- Verify business justifications (are they valid?)
- Confirm group/role memberships (correct?)
- Approve or request changes

**Step 3: CISO / Security Manager Review**

- Review overall documentation completeness (acceptable?)
- Assess critical gaps (privileged access without approval = unacceptable)
- Verify remediation plans have adequate resources
- Final approval

**Deliverable:** Approved assessment ready for management review

**Quality Check:**

- ✓ All three approval levels completed
- ✓ All review comments addressed
- ✓ Critical gaps have immediate remediation actions
- ✓ Evidence is audit-ready

---

## Evidence Collection

### What Evidence to Collect

**For Sheet 1 (System Inventory):**

- System architecture diagrams
- Asset inventory exports
- System owner assignments
- Data classification documentation

**For Sheet 2 (Access Rights Matrix):**

- AD group membership exports
- Entra ID role assignment exports
- Application access reports
- Database user permission queries
- Privileged access lists

**For Sheet 3 (Group/Role Mapping):**

- Group purpose documentation
- Group owner assignments
- Role catalog (if RBAC implemented)

**For Sheet 4 (Access Justification):**

- Access request tickets (ServiceNow, Jira)
- Manager approval emails
- HR job descriptions (role → access mapping)
- System owner approvals

**For Sheet 5 (Excessive Access):**

- Job role → required access mapping
- Manager justifications for excess access
- Privilege creep analysis reports

**For Gap Analysis:**

- Gap remediation project plans
- Resource allocation approvals

**For Sheet 8 (Evidence Register):**

- All evidence listed above, organised

**For Sheet 9 (Approval):**

- Approval sign-offs
- System owner confirmations

### How to Organize Evidence

**Folder Structure:**
```
ISMS-A.5.15-16-18.2_Evidence_YYYYMMDD/
├── 01_System_Inventory/
├── 02_Access_Data_Exports/
├── 03_Group_Role_Exports/
├── 04_Access_Requests_Approvals/
├── 05_Screenshots/
├── 06_Job_Role_Mappings/
├── 07_Policy_Documents/
└── 08_Approval_Records/
```

### Evidence Retention

- **Minimum retention:** 3 years (ISO 27001 certification cycle)
- **Recommended retention:** 5 years (trend analysis, improvement tracking)
- **Storage location:** Secure document management system
- **Access:** IAM Team, Security Team, Internal Audit, External Auditors

---

## Common Pitfalls

### Pitfall 1: Incomplete System Inventory

❌ **Mistake:** Only documenting major applications (ERP, CRM), missing cloud/SaaS tools

✅ **Fix:** Include ALL systems with user access: on-premises, cloud, SaaS, databases, infrastructure. Ask: "What systems do users log into?"

---

### Pitfall 2: Access Level Inconsistency

❌ **Mistake:** Different terminology for access levels across systems (View, Contributor, Editor, Modify, Update)

✅ **Fix:** Normalize to standard levels: Read, Write, Admin, Privileged. Document mapping (e.g., "Contributor" in SharePoint = "Write" in access matrix).

---

### Pitfall 3: Group Access Not Documented

❌ **Mistake:** Documenting only direct access assignments, missing access via group membership

✅ **Fix:** Always document HOW access is granted: Direct, Group Membership (specify group), or Role Assignment (specify role).

---

### Pitfall 4: No Business Justification

❌ **Mistake:** Access matrix shows WHO has WHAT, but no documentation of WHY

✅ **Fix:** For EVERY access grant, document business justification. If unknown, flag as gap requiring remediation.

---

### Pitfall 5: Stale Access Data

❌ **Mistake:** Using access exports from 6 months ago

✅ **Fix:** Use recent access data (< 30 days). Access changes frequently (new hires, leavers, role changes).

---

### Pitfall 6: Privileged Access Not Flagged

❌ **Mistake:** Admin/root/elevated access not differentiated from standard access

✅ **Fix:** Flag ALL privileged access explicitly. Privileged access requires special handling (CISO approval, enhanced monitoring).

---

### Pitfall 7: Missing Data Sensitivity Classification

❌ **Mistake:** Access matrix doesn't indicate WHAT data user can access (sensitivity level)

✅ **Fix:** Tag each system with data sensitivity (Restricted, Confidential, Internal, Public). Access to Restricted/Confidential data requires documented approval.

---

### Pitfall 8: Excessive Access Not Identified

❌ **Mistake:** Documenting access as-is, not identifying users with more access than required

✅ **Fix:** Define "required access" baseline for each job role, compare actual vs. required, flag excessive access.

---

### Pitfall 9: Contractor/Temporary Access Not Time-Bound

❌ **Mistake:** Contractor access documented same as employee access (no expiration date)

✅ **Fix:** For contractors and temporary access, document expiration date. Access should auto-revoke on contract end.

---

### Pitfall 10: No Access Review Date

❌ **Mistake:** Access documented but no record of when it was last verified

✅ **Fix:** Document last review date for each access grant. Access never reviewed (>365 days) = gap requiring remediation.

---

## Quality Checklist

Before submitting for approval, verify:

### System Inventory (Sheet 1)

- [ ] All systems with user access included (on-premises + cloud + SaaS)
- [ ] System owners identified and verified
- [ ] Criticality reflects actual business impact
- [ ] Data sensitivity accurately categorized
- [ ] No "Unknown" or "TBD" values

### Access Rights Matrix (Sheet 2)

- [ ] All users from IMP.1 included
- [ ] All systems from Sheet 1 included
- [ ] Access levels categorized consistently (Read, Write, Admin, Privileged)
- [ ] Group/role access documented (not just "Yes")
- [ ] Privileged access flagged
- [ ] Data sensitivity tagged
- [ ] Access grant dates documented (where available)
- [ ] Approvers documented (where available)

### Group/Role Mapping (Sheet 3)

- [ ] All groups granting access documented
- [ ] Group owners assigned
- [ ] Member counts accurate
- [ ] Access granted by group clearly documented
- [ ] Roles documented (if RBAC implemented)
- [ ] Cross-references to Sheet 2 verified

### Access Justification (Sheet 4)

- [ ] All access grants assessed for justification
- [ ] Justification sources documented (ticket ID, email, approval)
- [ ] Completeness categorization accurate
- [ ] Missing justifications flagged
- [ ] Documentation completeness score calculated

### Excessive Access Analysis (Sheet 5)

- [ ] Job role → required access mapping defined
- [ ] All users compared against baseline
- [ ] Excessive access accurately identified
- [ ] Legitimate excess has justification
- [ ] Questionable excess flagged for review

### Summary Dashboard

- [ ] All metrics pulled from correct sheets
- [ ] Overall documentation score calculated correctly
- [ ] Benchmark category accurate
- [ ] Findings clearly documented

### Gap Analysis (Sheet 7)

- [ ] All gaps identified from previous sheets
- [ ] Prioritization reflects actual risk
- [ ] Remediation actions specific and actionable
- [ ] Owners assigned
- [ ] Target dates realistic

### Evidence Register (Sheet 8)

- [ ] All evidence collected and listed
- [ ] Evidence organised logically
- [ ] Evidence IDs cross-referenced
- [ ] All evidence verified

### Approval (Sheet 9)

- [ ] Self-review completed
- [ ] System Owner review completed
- [ ] CISO review completed
- [ ] All comments addressed

---

## Review & Approval

### Review Process

**Step 1: Self-Review** (Assessment Completer)

- **Focus:** Completeness, accuracy, data quality
- **Time:** 2-3 hours
- **Turnaround:** Same day

**Step 2: System Owner Review**

- **Focus:** Access to their systems is accurate and justified
- **Review Criteria:**
  - Is access list complete (no missing users)?
  - Is access list accurate (no inappropriate access)?
  - Are justifications valid?
  - Are group/role memberships correct?
- **Decision:** Approve / Request Changes
- **Time:** 2-3 hours per system owner
- **Turnaround:** 1 week (coordinating multiple system owners)

**Step 3: CISO / Security Manager Review**

- **Focus:** Overall documentation completeness, privileged access governance, gap remediation
- **Review Criteria:**
  - Documentation completeness acceptable? (target >85%)
  - Privileged access properly documented and approved?
  - Critical gaps have immediate remediation?
  - Risk acceptance for gaps that cannot be immediately remediated?
- **Decision:** Final Approval / Approve with Conditions / Reject
- **Time:** 2-3 hours
- **Turnaround:** 3-5 business days

### Approval Timeline

```
Day 1:       Assessment completed, self-review, submitted to System Owners
Day 2-7:     System Owner reviews (multiple owners, coordinated)
Day 8:       All System Owner approvals collected
Day 9-11:    CISO review
Day 12:      CISO final approval
Day 13:      Assessment marked "Final", ready for dashboard
```

**Total timeline:** ~2 weeks from start to final approval

---

## Integration with Other Assessments

This assessment (A.5.15-16-18.2) feeds into:

### A.5.15-16-18.3 - Access Review Results Assessment

- **Uses:** Access rights matrix from Sheet 2 as review scope
- **Mapping:** Which users' access was reviewed, confirmed, or removed
- **Dependency:** Cannot conduct access review without knowing WHAT access exists

### A.5.15-16-18.4 - Role Definition & SoD Compliance Assessment

- **Uses:** Access via roles (from Sheets 2-3) to detect SoD violations
- **Mapping:** User → Roles → SoD conflicts
- **Dependency:** SoD detection requires knowing which users have which roles

---

## Continuous Improvement

### Monthly Updates

1. **Update Access Rights Matrix (Sheet 2):**

   - Add new access grants (from current month access requests)
   - Remove access for leavers (from IMP.1 deprovisioning)
   - Update group memberships (changes during month)

2. **Update Group/Role Mapping (Sheet 3):**

   - New groups created
   - Group ownership changes
   - Member count updates

3. **Update Justification Documentation (Sheet 4):**

   - Collect justifications for new access grants
   - Update documentation completeness score

4. **Update Gap Analysis (Sheet 7):**

   - Close resolved gaps
   - Add new gaps identified
   - Update remediation progress

**Time Commitment:** 4-6 hours per month

### Quarterly Comprehensive Review

1. **Verify Access Accuracy:**

   - Sample 10% of access grants, verify still accurate
   - Identify access that should have been removed but wasn't

2. **Excessive Access Cleanup Campaign:**

   - Manager review of all excessive access
   - Remove access no longer needed

3. **Documentation Improvement:**

   - Retroactive justification collection for undocumented access
   - Target: Increase documentation completeness to >90%

4. **System Owner Validation:**

   - Each system owner verifies access to their system

**Time Commitment:** 10-12 hours per quarter

---

**END OF USER GUIDE**

---

*"Least privilege is not a limitation; it is a liberation from risk."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
