# ISMS-IMP-A.5.15-16-18.S2 - Access Rights Matrix Assessment
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Control A.5.18: Access Rights

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S2 |
| **Version** | 1.0 |
| **Assessment Area** | Access Rights Matrix & Documentation |
| **Related Policy** | ISMS-POL-A.5.15-16-18, Section 2.3 (Access Rights Management Requirements - A.5.18) |
| **Purpose** | Document complete access rights matrix mapping users to systems/applications/data, assess access documentation completeness, and verify business justification in a technology-agnostic manner |
| **Target Audience** | IAM Team, System Owners, IT Operations, Security Team, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Monthly (access rights updates), Quarterly (comprehensive access audit) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Access Rights Matrix assessment workbook | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE** (THIS DOCUMENT)
  - Assessment Overview
  - Prerequisites
  - Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION** (SEPARATE DOCUMENT)
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formula Logic
  - Conditional Formatting Rules
  - Integration Points

---

# PART I: USER COMPLETION GUIDE

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
| ISMS-IMP-A.5.15-16-18.S5 | IAM Governance Dashboard | Uses access metrics from .2 for compliance dashboard |

This assessment (A.5.15-16-18.2) provides the **foundational access rights mapping** used by access review and SoD detection!

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **System Owners** - Define who should have access to their systems
2. **IAM Team** - Extract access data from identity and application systems
3. **IT Operations** - Understand technical access configurations
4. **Security Team** - Assess privileged access and data sensitivity
5. **Managers** - Verify their direct reports have appropriate access

#### Required Skills

- Understanding of access control systems (AD groups, Azure AD roles, application permissions)
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
- Group memberships (AD groups, Azure AD groups, application groups)
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
- **Identity system admin tools** (AD, Azure AD, Okta for group membership exports)
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
- A.5.15-16-18.5 (IAM Governance Dashboard) - Consolidates access metrics

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
9. CALCULATE COMPLETENESS SCORE (Sheet 6)
   ↓
10. IDENTIFY GAPS (Sheet 7)
    ↓
11. REGISTER EVIDENCE (Sheet 8)
    ↓
12. REVIEW & APPROVE (Sheet 9)
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
   - Infrastructure systems (AD, Azure AD, Okta, LDAP)
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

**For Azure AD Roles and Groups:**
```powershell
Connect-AzureAD
# Export group memberships
Get-AzureADGroup -All $true | ForEach-Object {
    $group = $_
    Get-AzureADGroupMember -ObjectId $group.ObjectId | ForEach-Object {
        [PSCustomObject]@{
            GroupName = $group.DisplayName
            UserPrincipalName = $_.UserPrincipalName
        }
    }
} | Export-Csv -Path "AzureAD_Group_Memberships.csv" -NoTypeInformation
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
- Normalize data format across all systems
- Map user identifiers (AD SamAccountName → Azure AD UPN → Application UserID)
- Tag each access record with source system

**Deliverable:** Consolidated access data CSV for all systems

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
   - Azure AD groups
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

**Objective:** Complete Sheet 6 - Access Rights Compliance Dashboard

**Steps:**

1. **Consolidate metrics** from Sheets 2-5:
   - Total access grants (from Sheet 2)
   - Access with complete documentation (from Sheet 4)
   - Privileged access count (from Sheet 2)
   - Access to restricted/confidential data (from Sheet 2)
   - Excessive access count (from Sheet 5)
   - Group-based access vs. direct access (from Sheets 2-3)

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

**Deliverable:** Sheet 6 with access rights compliance dashboard

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
   - Access data exports (AD groups, Azure AD roles, application access)
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
- ✓ Evidence organized in logical folder structure
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

**Deliverable:** Approved assessment ready for IAM Governance Dashboard

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
- Azure AD role assignment exports
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

**For Sheet 6 (Compliance Dashboard):**
- Trend charts (if historical data)
- Benchmark references

**For Sheet 7 (Gap Analysis):**
- Gap remediation project plans
- Resource allocation approvals

**For Sheet 8 (Evidence Register):**
- All evidence listed above, organized

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

### Compliance Dashboard (Sheet 6)
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
- [ ] Evidence organized logically
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

### A.5.15-16-18.5 - IAM Governance Compliance Dashboard
- **Uses:** Access metrics from Sheet 6
- **Consolidation:** Access rights metrics combined with lifecycle, review, role metrics
- **Dependency:** Dashboard incomplete without access rights data

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

4. **Refresh Compliance Dashboard (Sheet 6):**
   - All metrics auto-update from linked sheets

5. **Update Gap Analysis (Sheet 7):**
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

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

## Workbook Structure

### Sheet 1: Instructions_and_Legend

#### Header Section
- **Title:** "ISMS-IMP-A.5.15-16-18.S2 – Access Rights Matrix Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.5.18: Access Rights"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block (Rows 3-12)
```
Document ID:           ISMS-IMP-A.5.15-16-18.S2
Assessment Area:       Access Rights Matrix & Documentation
Related Policy:        ISMS-POL-A.5.15-16-18, Section 2.3 (A.5.18 - Access Rights)
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Assessment Period:     [USER INPUT - e.g., "Q1 2026"]
Review Cycle:          Monthly (access updates), Quarterly (comprehensive audit)
```

#### How to Use This Workbook (Rows 14-25)
1. **Sheet 1 - System Inventory:** List all systems/applications requiring access control
2. **Sheet 2 - Access Rights Matrix:** Map users to systems to access levels (the core assessment)
3. **Sheet 3 - Group and Role Mapping:** Document how access is granted (groups, roles)
4. **Sheet 4 - Access Justification Documentation:** Verify business justification for each access grant
5. **Sheet 5 - Excessive Access Analysis:** Identify users with more access than job function requires
6. **Sheet 6 - Access Rights Compliance Dashboard:** Overall metrics and compliance scoring
7. **Sheet 7 - Gap Analysis & Remediation:** Identify documentation gaps and track fixes
8. **Sheet 8 - Evidence Register:** Document all supporting evidence for audit
9. **Sheet 9 - Approval & Sign-Off:** Three-level approval workflow

#### Status Legend (Rows 27-35)
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Complete / Approved | Access fully documented with justification and approval | Green (C6EFCE) |
| ⚠️ | Partial | Access documented but missing some information (justification or approval) | Yellow (FFEB9C) |
| ❌ | Missing | Access exists but no documentation (justification, approval, review missing) | Red (FFC7CE) |
| 🚨 | CRITICAL | Privileged access without approval or access to Restricted data undocumented | Dark Red (FF0000) |
| ℹ️ | Under Review | Access documentation being collected or verified | Blue (B4C7E7) |
| N/A | Not Applicable | User does not have access to this system | Gray (D3D3D3) |

#### Access Level Legend (Rows 37-45)
| Access Level | Description | Examples |
|--------------|-------------|----------|
| **Read** | View-only access, no modification | View reports, read emails, browse files |
| **Write** | Create and modify content | Edit documents, create records, post messages |
| **Admin** | System administration, configuration | Manage settings, create users, configure workflows |
| **Privileged** | Elevated access (root, domain admin, database admin) | Domain Admin (AD), sysadmin (SQL), root (Linux) |

#### Data Sensitivity Legend (Rows 47-55)
| Sensitivity Level | Description | Examples | Access Requirements |
|-------------------|-------------|----------|---------------------|
| **Restricted** | Highest sensitivity, regulatory protection | PII/GDPR data, payment card data, trade secrets | CISO approval required |
| **Confidential** | High sensitivity, business impact if disclosed | Contracts, employee data, IP | System owner + manager approval |
| **Internal** | Moderate sensitivity, internal use only | Internal communications, operational data | Manager approval |
| **Public** | No sensitivity, publicly available | Marketing materials, published info | Standard approval |

---

## Sheet 2: System_Application_Inventory

### Purpose
Master list of ALL systems and applications requiring access control.

### Header Section (Rows 1-3)
**Row 1:** "SYSTEM / APPLICATION INVENTORY"  
**Row 2:** "Complete list of systems requiring access control governance"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | System ID | Text | Unique identifier | **USER INPUT** (SYS-001, SYS-002, etc.) | None |
| B | System Name | Text | What YOU call this system | **USER INPUT** | None |
| C | Description | Text | What does this system do? | **USER INPUT** | None |
| D | System Type | Dropdown | Category | Dropdown: Application, Database, Infrastructure, Network, Development, Cloud/SaaS, Other | None |
| E | Deployment Model | Dropdown | Where is it deployed? | Dropdown: On-Premises, Cloud SaaS, Hybrid, Container, Hosted | None |
| F | System Owner | Text | Who is accountable for access? | **USER INPUT** (name or role) | **CF:** Yellow if BLANK |
| G | System Owner Email | Text | Owner contact | **USER INPUT** | None |
| H | Criticality | Dropdown | Business impact if unavailable | Dropdown: Critical, High, Medium, Low | **CF:** Red if Critical, Yellow if High |
| I | Data Sensitivity | Dropdown | Highest sensitivity data in system | Dropdown: Restricted, Confidential, Internal, Public | **CF:** Dark Red if Restricted, Red if Confidential |
| J | User Count | Number | Approximate users with access | **USER INPUT** or calculated from Sheet 3 | None |
| K | Last Access Audit Date | Date | When was access last reviewed? | **USER INPUT** | **CF:** Red if >365 days or blank |
| L | Notes | Text | Additional context | **USER INPUT** | None |

### Summary Metrics (Top of Sheet, Rows 1-2, Columns N-S)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Systems | `=COUNTA(A:A)-1` | N1 |
| Critical Systems | `=COUNTIF(H:H,"Critical")` | O1 |
| Systems with Restricted Data | `=COUNTIF(I:I,"Restricted")` | P1 |
| Systems with Owner Assigned | `=COUNTIF(F:F,"<>")` | Q1 |
| Systems Audited <365 Days | `=COUNTIF(K:K,">"&TODAY()-365)` | R1 |
| Systems Needing Audit | `=COUNTIF(K:K,"<"&TODAY()-365)+COUNTIF(K:K,"")` | S1 |

### Data Validation (Dropdowns)

**System Type (Column D):**
- List: Application, Database, Infrastructure, Network, Development, Cloud/SaaS, Other

**Deployment Model (Column E):**
- List: On-Premises, Cloud SaaS, Hybrid, Container, Hosted

**Criticality (Column H):**
- List: Critical, High, Medium, Low

**Data Sensitivity (Column I):**
- List: Restricted, Confidential, Internal, Public

### Conditional Formatting Rules

**System Owner (Column F):**
- Rule 1: If BLANK → Fill: FFEB9C (yellow) - missing owner

**Criticality (Column H):**
- Rule 1: If "Critical" → Fill: FFC7CE (red)
- Rule 2: If "High" → Fill: FFEB9C (yellow)

**Data Sensitivity (Column I):**
- Rule 1: If "Restricted" → Fill: FF0000 (dark red)
- Rule 2: If "Confidential" → Fill: FFC7CE (red)

**Last Access Audit Date (Column K):**
- Rule 1: If BLANK OR < (TODAY()-365) → Fill: FFC7CE (red) - overdue audit

---

## Sheet 3: Access_Rights_Matrix

### Purpose
Complete mapping of users to systems to access levels - the core access rights matrix.

### Header Section (Rows 1-3)
**Row 1:** "ACCESS RIGHTS MATRIX"  
**Row 2:** "User-to-system-to-access-level mapping with documentation"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | User ID | Text | From IMP.1 user inventory | **LOOKUP** from IMP.1 Sheet 2 | None |
| B | Full Name | Text | User's name | **LOOKUP** from IMP.1 Sheet 2 | None |
| C | User Type | Text | Employee, Contractor, etc. | **LOOKUP** from IMP.1 Sheet 2 | None |
| D | Department | Text | User's department | **LOOKUP** from IMP.1 Sheet 2 | None |
| E | System ID | Text | From Sheet 2 | **LOOKUP** from Sheet 2 | None |
| F | System Name | Text | System being accessed | **LOOKUP** from Sheet 2 | None |
| G | Has Access? | Dropdown | Does user have access? | Dropdown: Yes, No | **CF:** Green if Yes, Gray if No |
| H | Access Level | Dropdown | If yes, what level? | Dropdown: Read, Write, Admin, Privileged | **CF:** Dark Red if Privileged, Red if Admin |
| I | Access Method | Dropdown | How is access granted? | Dropdown: Direct Assignment, Group Membership, Role Assignment, Combination | None |
| J | Group Name(s) | Text | If via group, which group(s)? | **USER INPUT** | **CF:** Yellow if Access Method = Group but this blank |
| K | Role Name(s) | Text | If via role, which role(s)? | **USER INPUT** | **CF:** Yellow if Access Method = Role but this blank |
| L | Access Grant Date | Date | When was access granted? | **USER INPUT** from access request or audit log | **CF:** Red if >365 days with no review |
| M | Access Granted By | Text | Who provisioned access? | **USER INPUT** (IT operations, IAM team) | None |
| N | Approver Name | Text | Who approved access? | **USER INPUT** (manager, system owner, CISO) | **CF:** Red if BLANK for Privileged or Restricted data |
| O | Approval Date | Date | When was access approved? | **USER INPUT** | **CF:** Red if BLANK for Privileged or Restricted data |
| P | Business Justification | Text | Why does user need this access? | **USER INPUT** | **CF:** Red if BLANK |
| Q | Last Review Date | Date | When was access last verified? | **USER INPUT** from access review | **CF:** Red if >365 days or blank |
| R | Reviewer Name | Text | Who last reviewed this access? | **USER INPUT** (manager, system owner) | None |
| S | Access Expiration Date | Date | For contractors, time-bound access | **USER INPUT** (blank for permanent) | **CF:** Red if past expiration + still active |
| T | Data Sensitivity Accessed | Dropdown | What sensitivity data can user access? | Dropdown from Sheet 2 System Data Sensitivity | **CF:** Dark Red if Restricted, Red if Confidential |
| U | Privileged Access Flag | Calculated | Is this privileged/admin access? | **FORMULA:** `=IF(H="Privileged","YES","NO")` | **CF:** Dark Red if YES |
| V | Documentation Completeness | Calculated | Is access fully documented? | **FORMULA:** See below | **CF:** Green if Complete, Yellow if Partial, Red if Missing |
| W | Notes | Text | Additional context | **USER INPUT** | None |

### Documentation Completeness Formula (Column V)
```excel
=IF(G="No","N/A - No Access",
  IF(AND(P<>"", N<>"", O<>"", Q<>""), "✅ Complete",
    IF(OR(P<>"", N<>""), "⚠️ Partial",
      "❌ Missing")))
```

**Logic:**
- No Access → N/A
- Has justification + approver + approval date + last review → Complete
- Has some documentation but not all → Partial
- No documentation → Missing

### Summary Metrics (Top of Sheet, Rows 1-2, Columns Y-AH)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Access Grants | `=COUNTIF(G:G,"Yes")` | Y1 |
| Privileged Access Grants | `=COUNTIF(U:U,"YES")` | Z1 |
| Access to Restricted Data | `=COUNTIF(T:T,"Restricted")` | AA1 |
| Access to Confidential Data | `=COUNTIF(T:T,"Confidential")` | AB1 |
| Fully Documented Access | `=COUNTIF(V:V,"✅ Complete")` | AC1 |
| Partially Documented | `=COUNTIF(V:V,"⚠️ Partial")` | AD1 |
| Missing Documentation | `=COUNTIF(V:V,"❌ Missing")` | AE1 |
| Documentation Completeness Rate | `=AC1/(AC1+AD1+AE1)` (format as %) | AF1 |

### Data Validation (Dropdowns)

**Has Access (Column G):**
- List: Yes, No

**Access Level (Column H):**
- List: Read, Write, Admin, Privileged

**Access Method (Column I):**
- List: Direct Assignment, Group Membership, Role Assignment, Combination

**Data Sensitivity Accessed (Column T):**
- List: Restricted, Confidential, Internal, Public

### Conditional Formatting Rules

**Has Access (Column G):**
- Rule 1: If "Yes" → Fill: C6EFCE (green)
- Rule 2: If "No" → Fill: D3D3D3 (gray)

**Access Level (Column H):**
- Rule 1: If "Privileged" → Fill: FF0000 (dark red) - highest sensitivity
- Rule 2: If "Admin" → Fill: FFC7CE (red)

**Group Name (Column J):**
- Rule 1: If BLANK AND Access Method contains "Group" → Fill: FFEB9C (yellow) - inconsistent

**Role Name (Column K):**
- Rule 1: If BLANK AND Access Method contains "Role" → Fill: FFEB9C (yellow) - inconsistent

**Access Grant Date (Column L):**
- Rule 1: If (TODAY() - L) > 365 AND Q is BLANK → Fill: FFC7CE (red) - old access never reviewed

**Approver Name (Column N):**
- Rule 1: If BLANK AND (H="Privileged" OR T="Restricted") → Fill: FF0000 (dark red) - CRITICAL

**Approval Date (Column O):**
- Rule 1: If BLANK AND (H="Privileged" OR T="Restricted") → Fill: FF0000 (dark red) - CRITICAL

**Business Justification (Column P):**
- Rule 1: If BLANK AND G="Yes" → Fill: FFC7CE (red) - missing justification

**Last Review Date (Column Q):**
- Rule 1: If BLANK OR < (TODAY()-365) → Fill: FFC7CE (red) - overdue review

**Access Expiration Date (Column S):**
- Rule 1: If < TODAY() AND G="Yes" → Fill: FF0000 (dark red) - expired access still active

**Data Sensitivity Accessed (Column T):**
- Rule 1: If "Restricted" → Fill: FF0000 (dark red)
- Rule 2: If "Confidential" → Fill: FFC7CE (red)

**Privileged Access Flag (Column U):**
- Rule 1: If "YES" → Fill: FF0000 (dark red)

**Documentation Completeness (Column V):**
- Rule 1: If "✅ Complete" → Fill: C6EFCE (green)
- Rule 2: If "⚠️ Partial" → Fill: FFEB9C (yellow)
- Rule 3: If "❌ Missing" → Fill: FFC7CE (red)

---

## Sheet 4: Group_and_Role_Mapping

### Purpose
Document how access is granted via groups and roles.

### Header Section (Rows 1-3)
**Row 1:** "GROUP AND ROLE MAPPING"  
**Row 2:** "Document groups and roles that grant access to systems"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | Group/Role ID | Text | Unique identifier | **USER INPUT** (GRP-001, ROLE-001) | None |
| B | Group/Role Name | Text | Name | **USER INPUT** (e.g., "Finance-ERP-Users", "IT-Admins") | None |
| C | Type | Dropdown | Group or Role? | Dropdown: AD Group, Azure AD Group, Application Group, RBAC Role, Other | None |
| D | Purpose | Text | What does this grant access to? | **USER INPUT** | **CF:** Red if BLANK |
| E | System(s) Accessed | Text | Which systems? | **USER INPUT** (comma-separated if multiple) | None |
| F | Access Level Granted | Dropdown | What level? | Dropdown: Read, Write, Admin, Privileged | **CF:** Dark Red if Privileged, Red if Admin |
| G | Group/Role Owner | Text | Who is accountable? | **USER INPUT** | **CF:** Yellow if BLANK |
| H | Owner Email | Text | Owner contact | **USER INPUT** | None |
| I | Member Count | Number | How many users? | **USER INPUT** or calculated | None |
| J | Last Membership Review Date | Date | When was membership verified? | **USER INPUT** | **CF:** Red if >365 days or blank |
| K | Review Frequency | Dropdown | How often reviewed? | Dropdown: Monthly, Quarterly, Semi-Annual, Annual | None |
| L | Notes | Text | Additional context | **USER INPUT** | None |

### Summary Metrics (Top of Sheet, Rows 1-2, Columns N-R)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Groups/Roles | `=COUNTA(A:A)-1` | N1 |
| Privileged Groups/Roles | `=COUNTIF(F:F,"Privileged")` | O1 |
| Groups with Owner | `=COUNTIF(G:G,"<>")` | P1 |
| Groups Reviewed <365 Days | `=COUNTIF(J:J,">"&TODAY()-365)` | Q1 |
| Groups Needing Review | `=COUNTIF(J:J,"<"&TODAY()-365)+COUNTIF(J:J,"")` | R1 |

### Data Validation (Dropdowns)

**Type (Column C):**
- List: AD Group, Azure AD Group, Application Group, RBAC Role, Other

**Access Level Granted (Column F):**
- List: Read, Write, Admin, Privileged

**Review Frequency (Column K):**
- List: Monthly, Quarterly, Semi-Annual, Annual

### Conditional Formatting Rules

**Purpose (Column D):**
- Rule 1: If BLANK → Fill: FFC7CE (red) - undocumented purpose

**Access Level Granted (Column F):**
- Rule 1: If "Privileged" → Fill: FF0000 (dark red)
- Rule 2: If "Admin" → Fill: FFC7CE (red)

**Group/Role Owner (Column G):**
- Rule 1: If BLANK → Fill: FFEB9C (yellow) - missing owner

**Last Membership Review Date (Column J):**
- Rule 1: If BLANK OR < (TODAY()-365) → Fill: FFC7CE (red) - overdue review

---

## Sheet 5: Access_Justification_Documentation

### Purpose
Assess business justification completeness for all access grants.

### Header Section (Rows 1-3)
**Row 1:** "ACCESS JUSTIFICATION DOCUMENTATION ANALYSIS"  
**Row 2:** "Verify every access grant has documented business justification"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | User ID | Text | From Sheet 3 | **LOOKUP** from Sheet 3 (filter: Has Access = Yes) | None |
| B | Full Name | Text | User's name | **LOOKUP** from Sheet 3 | None |
| C | System Name | Text | System accessed | **LOOKUP** from Sheet 3 | None |
| D | Access Level | Text | Read, Write, Admin, Privileged | **LOOKUP** from Sheet 3 | **CF:** Dark Red if Privileged |
| E | Business Justification | Text | From Sheet 3 | **LOOKUP** from Sheet 3, Column P | **CF:** Red if BLANK |
| F | Justification Source | Dropdown | Where is justification documented? | Dropdown: Access Request Ticket, Manager Approval Email, HR Job Description, System Owner Approval, Not Documented | **CF:** Red if "Not Documented" |
| G | Source Reference | Text | Ticket ID, email date, document link | **USER INPUT** | **CF:** Yellow if BLANK and Source ≠ "Not Documented" |
| H | Approver Name | Text | From Sheet 3 | **LOOKUP** from Sheet 3, Column N | **CF:** Red if BLANK |
| I | Approval Date | Date | From Sheet 3 | **LOOKUP** from Sheet 3, Column O | **CF:** Red if BLANK |
| J | Last Review Date | Date | From Sheet 3 | **LOOKUP** from Sheet 3, Column Q | **CF:** Red if BLANK or >365 days |
| K | Documentation Status | Calculated | Complete/Partial/Missing | **FORMULA:** `=IF(AND(E<>"",H<>"",I<>"",J<>""),"✅ Complete",IF(OR(E<>"",H<>""),"⚠️ Partial","❌ Missing"))` | **CF:** Green/Yellow/Red |
| L | Priority for Remediation | Calculated | Based on access level and gaps | **FORMULA:** See below | **CF:** Dark Red if Critical, Red if High |
| M | Notes | Text | Remediation actions | **USER INPUT** | None |

### Priority for Remediation Formula (Column L)
```excel
=IF(K="✅ Complete","N/A - Complete",
  IF(AND(D="Privileged",K="❌ Missing"),"🚨 CRITICAL",
    IF(D="Privileged","High",
      IF(D="Admin","High",
        IF(K="❌ Missing","Medium","Low")))))
```

**Logic:**
- Complete documentation → N/A
- Privileged access + missing documentation → CRITICAL
- Privileged access + partial documentation → High
- Admin access → High
- Missing documentation (non-privileged) → Medium
- Partial documentation (non-privileged) → Low

### Summary Metrics (Top of Sheet, Rows 1-2, Columns O-U)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Access Grants Assessed | `=COUNTA(A:A)-1` | O1 |
| Complete Documentation | `=COUNTIF(K:K,"✅ Complete")` | P1 |
| Partial Documentation | `=COUNTIF(K:K,"⚠️ Partial")` | Q1 |
| Missing Documentation | `=COUNTIF(K:K,"❌ Missing")` | R1 |
| Justification Completeness Rate | `=P1/O1` (format as %) | S1 |
| CRITICAL Priority Gaps | `=COUNTIF(L:L,"🚨 CRITICAL")` | T1 |
| High Priority Gaps | `=COUNTIF(L:L,"High")` | U1 |

### Data Validation (Dropdowns)

**Justification Source (Column F):**
- List: Access Request Ticket, Manager Approval Email, HR Job Description, System Owner Approval, Project Charter, Not Documented

### Conditional Formatting Rules

**Access Level (Column D):**
- Rule 1: If "Privileged" → Fill: FF0000 (dark red)

**Business Justification (Column E):**
- Rule 1: If BLANK → Fill: FFC7CE (red)

**Justification Source (Column F):**
- Rule 1: If "Not Documented" → Fill: FFC7CE (red)

**Source Reference (Column G):**
- Rule 1: If BLANK AND Justification Source ≠ "Not Documented" → Fill: FFEB9C (yellow)

**Approver Name (Column H):**
- Rule 1: If BLANK → Fill: FFC7CE (red)

**Approval Date (Column I):**
- Rule 1: If BLANK → Fill: FFC7CE (red)

**Last Review Date (Column J):**
- Rule 1: If BLANK OR < (TODAY()-365) → Fill: FFC7CE (red)

**Documentation Status (Column K):**
- Rule 1: If "✅ Complete" → Fill: C6EFCE (green)
- Rule 2: If "⚠️ Partial" → Fill: FFEB9C (yellow)
- Rule 3: If "❌ Missing" → Fill: FFC7CE (red)

**Priority for Remediation (Column L):**
- Rule 1: If "🚨 CRITICAL" → Fill: FF0000 (dark red)
- Rule 2: If "High" → Fill: FFC7CE (red)
- Rule 3: If "Medium" → Fill: FFEB9C (yellow)

---

## Sheet 6: Excessive_Access_Analysis

### Purpose
Identify users with more access than job function requires.

### Header Section (Rows 1-3)
**Row 1:" "EXCESSIVE ACCESS ANALYSIS"  
**Row 2:** "Identify users with more access than required for job function"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | User ID | Text | From IMP.1 | **LOOKUP** from IMP.1 | None |
| B | Full Name | Text | User's name | **LOOKUP** from IMP.1 | None |
| C | Job Role/Function | Text | User's job title | **LOOKUP** from IMP.1 or HR | None |
| D | Department | Text | User's department | **LOOKUP** from IMP.1 | None |
| E | Required Access (Baseline) | Text | What access does this job role require? | **USER INPUT** (from job role → access mapping) | None |
| F | Actual Access | Calculated | What access does user actually have? | **FORMULA:** Concatenate from Sheet 3 where User ID matches | None |
| G | Excess Access Identified | Text | Which access is excessive? | **USER INPUT** (compare F vs. E) | **CF:** Yellow if not blank |
| H | Excess Access Type | Dropdown | Category of excessive access | Dropdown: System Not Required, Access Level Too High, Multiple Systems (should be one), Historical (previous role), Other | None |
| I | Legitimate Excess? | Dropdown | Is there valid reason? | Dropdown: Yes - Documented, No - Requires Removal, Under Review | **CF:** Red if No, Yellow if Under Review |
| J | Excess Justification | Text | If yes, why is this legitimate? | **USER INPUT** (e.g., "Also supports Project X") | **CF:** Yellow if BLANK and Legitimate Excess = Yes |
| K | Approver (for excess) | Text | Who approved this excess access? | **USER INPUT** | **CF:** Yellow if BLANK and Legitimate Excess = Yes |
| L | Manager Review Required? | Dropdown | Should manager review? | Dropdown: Yes, No, Completed | **CF:** Yellow if Yes |
| M | Action Required | Dropdown | What should be done? | Dropdown: Remove Access, Document Justification, Manager Review, No Action, Under Investigation | **CF:** Red if Remove Access |
| N | Action Owner | Text | Who is responsible? | **USER INPUT** | **CF:** Yellow if BLANK and Action ≠ No Action |
| O | Target Date | Date | When will this be resolved? | **USER INPUT** | **CF:** Red if past due |
| P | Status | Dropdown | Progress | Dropdown: Open, In Progress, Completed, Closed | **CF:** Green if Completed/Closed |
| Q | Notes | Text | Additional context | **USER INPUT** | None |

### Summary Metrics (Top of Sheet, Rows 1-2, Columns S-X)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Users Assessed | `=COUNTA(A:A)-1` | S1 |
| Users with Excess Access | `=COUNTIF(G:G,"<>")` | T1 |
| Legitimate Excess (Documented) | `=COUNTIF(I:I,"Yes - Documented")` | U1 |
| Excess Requiring Removal | `=COUNTIF(I:I,"No - Requires Removal")` | V1 |
| Excess Under Review | `=COUNTIF(I:I,"Under Review")` | W1 |
| Excessive Access Rate | `=T1/S1` (format as %) | X1 |

### Data Validation (Dropdowns)

**Excess Access Type (Column H):**
- List: System Not Required, Access Level Too High, Multiple Systems (should be one), Historical (previous role), Temporary Project (ended), Other

**Legitimate Excess (Column I):**
- List: Yes - Documented, No - Requires Removal, Under Review

**Manager Review Required (Column L):**
- List: Yes, No, Completed

**Action Required (Column M):**
- List: Remove Access, Document Justification, Manager Review, No Action, Under Investigation

**Status (Column P):**
- List: Open, In Progress, Completed, Closed

### Conditional Formatting Rules

**Excess Access Identified (Column G):**
- Rule 1: If NOT BLANK → Fill: FFEB9C (yellow) - excessive access exists

**Legitimate Excess (Column I):**
- Rule 1: If "No - Requires Removal" → Fill: FFC7CE (red)
- Rule 2: If "Under Review" → Fill: FFEB9C (yellow)

**Excess Justification (Column J):**
- Rule 1: If BLANK AND Legitimate Excess = "Yes - Documented" → Fill: FFEB9C (yellow) - inconsistent

**Manager Review Required (Column L):**
- Rule 1: If "Yes" → Fill: FFEB9C (yellow)

**Action Required (Column M):**
- Rule 1: If "Remove Access" → Fill: FFC7CE (red)

**Action Owner (Column N):**
- Rule 1: If BLANK AND Action Required ≠ "No Action" → Fill: FFEB9C (yellow)

**Target Date (Column O):**
- Rule 1: If < TODAY() AND Status ≠ "Completed" → Fill: FFC7CE (red)

**Status (Column P):**
- Rule 1: If "Completed" OR "Closed" → Fill: C6EFCE (green)
- Rule 2: If "In Progress" → Fill: FFEB9C (yellow)

---

## Sheet 7: Access_Rights_Compliance_Dashboard

### Purpose
Consolidated access rights metrics and overall compliance scoring.

### Header Section (Rows 1-3)
**Row 1:** "ACCESS RIGHTS COMPLIANCE DASHBOARD"  
**Row 2:** "Overall access documentation and compliance metrics"  
**Row 3:** Section headers

### Dashboard Layout (Rows 5+)

#### Section 1: Overall Access Summary (Rows 5-15)

| Metric | Value (Formula) | Target | Status | Cell Reference |
|--------|----------------|--------|--------|----------------|
| **Total Systems** | `=Sheet2!N1` | N/A | N/A | B5 |
| **Total Access Grants** | `=Sheet3!Y1` | N/A | N/A | B6 |
| **Privileged Access Grants** | `=Sheet3!Z1` | <5% of total | `=IF(B7/B6<0.05,"✅",IF(B7/B6<0.10,"⚠️","❌"))` | B7 |
| **Access to Restricted Data** | `=Sheet3!AA1` | Document all | N/A | B8 |
| **Access to Confidential Data** | `=Sheet3!AB1` | Document all | N/A | B9 |
| **Users with Excessive Access** | `=Sheet6!T1` | <10% of users | `=IF(B10/(Sheet3!Y1)<0.10,"✅","⚠️")` | B10 |

#### Section 2: Documentation Completeness (Rows 17-25)

| Metric | Value (Formula) | Target | Status | Cell Reference |
|--------|----------------|--------|--------|----------------|
| **Fully Documented Access** | `=Sheet3!AC1` | >85% | N/A | B17 |
| **Partially Documented** | `=Sheet3!AD1` | <10% | N/A | B18 |
| **Missing Documentation** | `=Sheet3!AE1` | <5% | N/A | B19 |
| **Documentation Completeness Rate** | `=Sheet3!AF1` (format as %) | ≥85% | `=IF(B20>=0.85,"✅",IF(B20>=0.70,"⚠️","❌"))` | B20 |
| **Justification Completeness** | `=Sheet5!S1` (format as %) | ≥90% | `=IF(B21>=0.90,"✅",IF(B21>=0.75,"⚠️","❌"))` | B21 |
| **CRITICAL Gaps** (Privileged without approval) | `=Sheet5!T1` | 0 | `=IF(B22=0,"✅","🚨 CRITICAL")` | B22 |

#### Section 3: Group and Role Governance (Rows 27-33)

| Metric | Value (Formula) | Target | Status | Cell Reference |
|--------|----------------|--------|--------|----------------|
| **Total Groups/Roles** | `=Sheet4!N1` | N/A | N/A | B27 |
| **Groups with Owner Assigned** | `=Sheet4!P1` | 100% | `=IF(B28=B27,"✅",IF(B28/B27>=0.90,"⚠️","❌"))` | B28 |
| **Groups Reviewed <365 Days** | `=Sheet4!Q1` | 100% | `=IF(B29=B27,"✅",IF(B29/B27>=0.90,"⚠️","❌"))` | B29 |
| **Privileged Groups/Roles** | `=Sheet4!O1` | Document all | N/A | B30 |

#### Section 4: Overall Access Rights Documentation Score (Rows 35-45)

**Weighted Calculation:**
```
Access Rights Documentation Score = 
  (Documentation Completeness × 40%) + 
  (Justification Completeness × 30%) + 
  (Group Governance × 20%) + 
  (Excessive Access Control × 10%)
```

| Component | Weight | Score | Weighted Score | Cell |
|-----------|--------|-------|----------------|------|
| Documentation Completeness | 40% | `=B20` | `=B20*0.40` | D36 |
| Justification Completeness | 30% | `=B21` | `=B21*0.30` | D37 |
| Group Governance | 20% | `=B28/B27` | `=(B28/B27)*0.20` | D38 |
| Excessive Access Control | 10% | `=1-(B10/B6)` | `=(1-(B10/B6))*0.10` | D39 |
| **Total Documentation Score** | **100%** | N/A | `=SUM(D36:D39)` | **D40** |

**Benchmark Categories:**

| Score Range | Maturity Level | Description | Cell |
|-------------|----------------|-------------|------|
| 90-100% | ✅ **Excellent** | Best-in-class access documentation | B42 |
| 75-89% | ⚠️ **Good** | Strong documentation, minor gaps | B43 |
| 60-74% | ⚠️ **Fair** | Acceptable but significant documentation gaps | B44 |
| <60% | ❌ **Poor** | Major documentation deficiencies, audit risk | B45 |

**Current Maturity Level:**
```excel
=IF(D40>=0.90, "✅ Excellent", 
  IF(D40>=0.75, "⚠️ Good", 
    IF(D40>=0.60, "⚠️ Fair", "❌ Poor")))
```

### Conditional Formatting Rules

**Status Columns (All sections):**
- Rule 1: If "✅" → Fill: C6EFCE (green)
- Rule 2: If "⚠️" → Fill: FFEB9C (yellow)
- Rule 3: If "❌" → Fill: FFC7CE (red)
- Rule 4: If "🚨 CRITICAL" → Fill: FF0000 (dark red)

**Documentation Score (D40):**
- Rule 1: If ≥0.90 → Fill: C6EFCE (green)
- Rule 2: If 0.75-0.89 → Fill: FFEB9C (yellow)
- Rule 3: If 0.60-0.74 → Fill: FFEB9C (yellow)
- Rule 4: If <0.60 → Fill: FFC7CE (red)

---

## Sheet 8: Gap_Analysis_and_Remediation

### Purpose
Consolidated gap identification and remediation tracking across all access documentation areas.

### Header Section (Rows 1-3)
**Row 1:** "GAP ANALYSIS & REMEDIATION ROADMAP"  
**Row 2:** "Identify all access documentation deficiencies and track remediation progress"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | Gap ID | Text | Unique identifier | **USER INPUT** (GAP-001, GAP-002) | None |
| B | Gap Type | Dropdown | Category | Dropdown: Missing Justification, Missing Approval, Missing Review, Excessive Access, Undocumented Group, Privileged Access Gap, Other | None |
| C | Gap Description | Text | What is the gap? | **USER INPUT** | None |
| D | Affected Users/Count | Text/Number | How many affected? | **USER INPUT** or calculated | None |
| E | Source Sheet | Dropdown | Where identified? | Dropdown: Sheet 3 (Access Matrix), Sheet 4 (Groups), Sheet 5 (Justification), Sheet 6 (Excessive Access), Other | None |
| F | Risk Level | Dropdown | Severity | Dropdown: Critical, High, Medium, Low | **CF:** Dark Red if Critical, Red if High |
| G | Business Impact | Text | What's the risk? | **USER INPUT** | None |
| H | Root Cause | Text | Why did this happen? | **USER INPUT** | None |
| I | Remediation Plan | Text | What action to fix? | **USER INPUT** | None |
| J | Remediation Owner | Text | Who is responsible? | **USER INPUT** | **CF:** Yellow if BLANK |
| K | Target Date | Date | When resolved? | **USER INPUT** | **CF:** Red if past due |
| L | Status | Dropdown | Progress | Dropdown: Open, In Progress, Blocked, Completed, Closed | **CF:** Green if Completed/Closed |
| M | % Complete | Number | Progress percentage | **USER INPUT** (0-100) | **CF:** Data bars |
| N | Budget Required | Dropdown | Does this need budget? | Dropdown: Yes, No, TBD | None |
| O | Estimated Cost | Currency | If yes, how much? | **USER INPUT** | None |
| P | Progress Notes | Text | Latest updates | **USER INPUT** | None |
| Q | Date Closed | Date | When resolved? | **USER INPUT** | None |

### Summary Metrics (Top of Sheet, Rows 1-2, Columns S-X)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Gaps | `=COUNTA(A:A)-1` | S1 |
| Critical Gaps | `=COUNTIF(F:F,"Critical")` | T1 |
| High Gaps | `=COUNTIF(F:F,"High")` | U1 |
| Medium Gaps | `=COUNTIF(F:F,"Medium")` | V1 |
| Low Gaps | `=COUNTIF(F:F,"Low")` | W1 |
| Gaps Closed | `=COUNTIF(L:L,"Closed")+COUNTIF(L:L,"Completed")` | X1 |
| Resolution Rate | `=X1/S1` (format as %) | Y1 |

### Data Validation (Dropdowns)

**Gap Type (Column B):**
- List: Missing Justification, Missing Approval, Missing Review, Excessive Access, Undocumented Group, Privileged Access Gap, Documentation Incomplete, Other

**Source Sheet (Column E):**
- List: Sheet 3 (Access Matrix), Sheet 4 (Groups/Roles), Sheet 5 (Justification), Sheet 6 (Excessive Access), Multiple Sheets, Other

**Risk Level (Column F):**
- List: Critical, High, Medium, Low

**Status (Column L):**
- List: Open, In Progress, Blocked, Completed, Closed

**Budget Required (Column N):**
- List: Yes, No, TBD

### Conditional Formatting Rules

**Risk Level (Column F):**
- Rule 1: If "Critical" → Fill: FF0000 (dark red)
- Rule 2: If "High" → Fill: FFC7CE (red)
- Rule 3: If "Medium" → Fill: FFEB9C (yellow)

**Remediation Owner (Column J):**
- Rule 1: If BLANK → Fill: FFEB9C (yellow)

**Target Date (Column K):**
- Rule 1: If < TODAY() AND Status ≠ "Completed" AND Status ≠ "Closed" → Fill: FFC7CE (red)

**Status (Column L):**
- Rule 1: If "Completed" OR "Closed" → Fill: C6EFCE (green)
- Rule 2: If "In Progress" → Fill: FFEB9C (yellow)
- Rule 3: If "Blocked" → Fill: FFC7CE (red)

**% Complete (Column M):**
- Data bars: Green gradient (0% = no fill, 100% = full green)

---

## Sheet 9: Evidence_Register

### Purpose
Centralized evidence repository.

### Header Section (Rows 1-3)
**Row 1:** "EVIDENCE REGISTER"  
**Row 2:** "Document all evidence supporting this assessment"  
**Row 3:** Column headers

### Column Definitions (Rows 3-103, 100 rows for evidence)

| Column | Header | Type | Description | Conditional Formatting |
|--------|--------|------|-------------|----------------------|
| A | Evidence ID | Text | Unique identifier (EVID-001) | None |
| B | Evidence Type | Dropdown | Category | None |
| C | Description | Text | What is this evidence? | None |
| D | Related Sheet/Row | Text | Where referenced? | None |
| E | Location/Path | Text | File path or URL | None |
| F | Date Collected | Date | When captured? | **CF:** Red if >90 days old |
| G | Collected By | Text | Who gathered? | None |
| H | Verification Status | Dropdown | Verified? | **CF:** Green if Verified, Yellow if Pending |

### Data Validation (Dropdowns)

**Evidence Type (Column B):**
- List: Access Data Export, Group Membership Export, Access Request Ticket, Approval Email, Screenshot, System Owner Confirmation, HR Job Description, Policy Document, Meeting Notes, Other

**Verification Status (Column H):**
- List: Verified, Pending Verification, Not Verified, N/A

### Conditional Formatting Rules

**Date Collected (Column F):**
- Rule 1: If (TODAY() - F) > 90 → Fill: FFC7CE (red)

**Verification Status (Column H):**
- Rule 1: If "Verified" → Fill: C6EFCE (green)
- Rule 2: If "Pending Verification" → Fill: FFEB9C (yellow)
- Rule 3: If "Not Verified" → Fill: FFC7CE (red)

---

## Sheet 10: Approval_and_Sign_Off

### Purpose
Three-level approval workflow.

### Assessment Summary Section (Rows 3-14)
```
Assessment Document:              ISMS-IMP-A.5.15-16-18.S2 - Access Rights Matrix
Assessment Period:                [USER INPUT]
Total Systems Assessed:           [Formula: =Sheet2!N1]
Total Access Grants:              [Formula: =Sheet3!Y1]
Privileged Access Grants:         [Formula: =Sheet3!Z1]
Documentation Completeness Rate:  [Formula: =Sheet7!B20]
Justification Completeness Rate:  [Formula: =Sheet7!B21]
Excessive Access Count:           [Formula: =Sheet6!T1]
Overall Documentation Score:      [Formula: =Sheet7!D40]
Critical Gaps:                    [Formula: =Sheet8!T1]
Assessment Status:                [Dropdown: Draft, Final, Requires Remediation, Re-assessment Required]
```

### Assessment Completed By (Rows 16-23)
```
Name:                [USER INPUT]
Role/Title:          [USER INPUT - e.g., IAM Team, System Owners]
Department:          [USER INPUT]
Email:               [USER INPUT]
Date Completed:      [USER INPUT - date picker]
Signature/Initials:  [USER INPUT]
Completion Notes:    [Text area - merged cells]
```

### Reviewed By - System Owners (Rows 25-33)
```
Name:                     [USER INPUT - multiple system owners may sign off]
Role/Title:               System Owner
Date Reviewed:            [USER INPUT]
Systems Reviewed:         [List of systems this owner verified]
Review Notes:             [Text area]
Access Accuracy:          [Dropdown: Accurate, Issues Found (see notes), Not Reviewed]
Recommendation:           [Dropdown: Approve, Approve with Conditions, Reject - Require Rework]
Conditions/Comments:      [Text area]
```

### Approved By - CISO or Security Manager (Rows 35-43)
```
Name:                     [USER INPUT]
Role/Title:               CISO / Security Manager
Date Approved:            [USER INPUT]
Approval Decision:        [Dropdown: Approved, Approved with Conditions, Rejected]
Risk Acceptance:          [Text area - privileged access gaps, documentation gaps]
Conditions/Comments:      [Text area]
Final Approval:           [Checkbox or Dropdown: Yes - Final, No - See conditions]
```

### Next Review Details (Rows 45-51)
```
Next Review Type:         [Dropdown: Monthly Update, Quarterly Comprehensive, Annual Strategic]
Next Review Date:         [Date - auto-calculate: Monthly = +1 month, Quarterly = +3 months]
Review Responsible:       [USER INPUT - typically System Owners + IAM Team]
Special Considerations:   [Text area]
Continuous Improvement:   [Text area]
```

### Data Validation (Dropdowns)

**Assessment Status:**
- List: Draft, Final, Requires Remediation, Re-assessment Required

**Access Accuracy:**
- List: Accurate, Issues Found (see notes), Not Reviewed

**Recommendation (System Owners):**
- List: Approve, Approve with Conditions, Reject - Require Rework

**Approval Decision (CISO):**
- List: Approved, Approved with Conditions, Rejected

**Final Approval:**
- List: Yes - Final, No - See conditions

**Next Review Type:**
- List: Monthly Update, Quarterly Comprehensive, Annual Strategic

---

## Cell Styling Reference

### Header Styles
- **Main Header:** Font: Calibri 14pt bold white, Fill: 003366 (dark blue), Centered, 40px height
- **Subheader:** Font: Calibri 11pt bold white, Fill: 4472C4 (blue), Centered
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (gray), Centered, Border: thin

### Input Cell Styles
- **Fill:** FFFFCC (light yellow) - user input required
- **Alignment:** Left for text, center for dropdowns, right for numbers
- **Border:** Thin black all sides
- **Protection:** Unlocked

### Formula/Calculated Cell Styles
- **Fill:** White (FFFFFF) or light gray (F2F2F2)
- **Alignment:** Right for numbers, left for text
- **Border:** Thin gray
- **Protection:** Locked

### Status Fill Colors
- **✅ Complete / Approved:** C6EFCE (green)
- **⚠️ Partial / Pending:** FFEB9C (yellow)
- **❌ Missing / Issues:** FFC7CE (red)
- **🚨 CRITICAL:** FF0000 (dark red)
- **ℹ️ Under Review:** B4C7E7 (blue)
- **N/A:** D3D3D3 (gray)

---

## Freeze Panes

- **Sheet 2 (System Inventory):** Freeze at A4
- **Sheet 3 (Access Matrix):** Freeze at A4
- **Sheet 4 (Group/Role Mapping):** Freeze at A4
- **Sheet 5 (Justification):** Freeze at A4
- **Sheet 6 (Excessive Access):** Freeze at A4
- **Sheet 7 (Dashboard):** Freeze at A5
- **Sheet 8 (Gap Analysis):** Freeze at A4
- **Sheet 9 (Evidence):** Freeze at A4
- **Sheet 10 (Approval):** Freeze at A3

---

## File Naming Convention

**Format:** `ISMS-IMP-A.5.15-16-18.S2_Access_Rights_Matrix_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.5.15-16-18.S2_Access_Rights_Matrix_20260122.xlsx`

---

## Monthly Review Cycle

1. **Update System Inventory (Sheet 2):** Add new systems, retire old systems
2. **Update Access Matrix (Sheet 3):** Add new access grants, remove leavers' access
3. **Update Group/Role Mapping (Sheet 4):** New groups, membership changes
4. **Update Justification Documentation (Sheet 5):** Collect justifications for new access
5. **Refresh Dashboard (Sheet 7):** Auto-updates from linked sheets
6. **Update Gap Analysis (Sheet 8):** Close resolved gaps, add new gaps
7. **Add Evidence (Sheet 9):** Current month documentation
8. **System Owner Sign-Off (Sheet 10):** Monthly verification

**Time:** 4-6 hours per month

---

## Integration Points

### Related Assessments

**A.5.15-16-18.1 - User Inventory & Lifecycle:**
- **Input FROM IMP.1:** User list (baseline for access matrix)

**A.5.15-16-18.3 - Access Review Results:**
- **Input FROM this workbook:** Access matrix defines WHAT to review

**A.5.15-16-18.4 - Role & SoD Compliance:**
- **Input FROM this workbook:** Access via roles for SoD detection

**A.5.15-16-18.5 - IAM Governance Dashboard:**
- **Input FROM this workbook:** Access metrics (Sheet 7)

---

**END OF TECHNICAL SPECIFICATION**

*"The first principle is that you must not fool yourself – and you are the easiest person to fool."*  
– Richard Feynman

**ISMS Maturity Indicator:** If you can document WHAT access exists, WHO approved it, and WHY it was granted for every single access grant in your organization, you understand that access governance is not about technology – it's about systematic documentation and accountability. ✅


