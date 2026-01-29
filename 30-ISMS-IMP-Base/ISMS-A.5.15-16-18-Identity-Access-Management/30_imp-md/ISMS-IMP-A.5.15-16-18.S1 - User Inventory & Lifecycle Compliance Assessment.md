# ISMS-IMP-A.5.15-16-18.S1 - User Inventory & Lifecycle Compliance Assessment
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Control A.5.16: Identity Management

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S1 |
| **Version** | 1.0 |
| **Assessment Area** | User Inventory & Identity Lifecycle Compliance |
| **Related Policy** | ISMS-POL-A.5.15-16-18, Section 2.2 (Identity Management Requirements - A.5.16) |
| **Purpose** | Document complete user inventory across all identity systems, assess identity lifecycle compliance (joiner/mover/leaver timeliness), and identify orphaned accounts in a technology-agnostic manner |
| **Target Audience** | IAM Team, HR Team, IT Operations, Security Team, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Monthly (user inventory updates), Quarterly (comprehensive lifecycle assessment) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for User Inventory & Lifecycle assessment workbook | ISMS Implementation Team |

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

**Assessment Name:** ISMS-IMP-A.5.15-16-18.S1 - User Inventory & Lifecycle Compliance Assessment

#### What This Assessment Covers

This assessment documents your COMPLETE USER INVENTORY and assesses IDENTITY LIFECYCLE COMPLIANCE. This is the foundational "WHO has accounts?" assessment that answers:

- Who are ALL the users in your identity systems? (employees, contractors, vendors, service accounts)
- Are user accounts provisioned on time? (access ready by start date)
- Are user accounts deprovisioned on time? (access removed upon termination)
- Are there orphaned accounts? (accounts without valid business owner)
- Are there inactive accounts? (no login in 90+ days)
- What is the overall lifecycle compliance rate?

#### Key Principle

This assessment is **completely technology-agnostic and vendor-independent**. You document YOUR identity systems (Active Directory, Azure AD, Okta, Google Workspace, LDAP, custom systems - whatever you use), and assess lifecycle compliance against generic policy requirements.

#### What You'll Document

- **User Inventory**: Complete list of ALL users across ALL identity systems
  - User ID, name, email, account status (active/disabled)
  - User type (employee, contractor, vendor, service account, shared account)
  - Department, manager, location
  - Hire date, termination date (if applicable)
  - Last login date, account creation date
  - Account source (which identity system)

- **Lifecycle Compliance Metrics**:
  - Provisioning timeliness (days from hire date to account creation)
  - Deprovisioning timeliness (days from termination to account disable)
  - Orphaned account count and remediation status
  - Inactive account count and justification
  - Compliance status per user (lifecycle compliant/non-compliant)

- **Gap Analysis**:
  - Users provisioned late (missed start date SLA)
  - Users not deprovisioned (terminated but still active)
  - Orphaned accounts requiring cleanup
  - Inactive accounts requiring review

#### How This Relates to Other A.5.15-16-18 Assessments

| Assessment | Focus | Relationship to A.5.15-16-18.1 |
|------------|-------|--------------------------------|
| **ISMS-IMP-A.5.15-16-18.S1** | **User Inventory & Lifecycle** | **WHO has accounts and WHEN were they created/removed** |
| ISMS-IMP-A.5.15-16-18.S2 | Access Rights Matrix | WHAT access do users have (uses user list from .1) |
| ISMS-IMP-A.5.15-16-18.S3 | Access Review Results | HOW access is reviewed (uses user list from .1) |
| ISMS-IMP-A.5.15-16-18.S4 | Role & SoD Compliance | WHAT roles users have and SoD violations (uses user list from .1) |
| ISMS-IMP-A.5.15-16-18.S5 | IAM Governance Dashboard | Consolidated view across all assessments |

This assessment (A.5.15-16-18.1) provides the **foundational user inventory** used by all other IAM assessments!

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **IAM Team** - User account management, identity system administration
2. **HR Team** - Authoritative source for employee data, joiner/mover/leaver triggers
3. **IT Operations** - Account provisioning/deprovisioning execution
4. **Security Team** - Orphaned account detection, compliance monitoring
5. **Managers** - Verification of direct reports, data handover for leavers

#### Required Skills

- Understanding of identity systems (AD, Azure AD, Okta, LDAP)
- Access to identity system admin consoles or APIs
- Understanding of HR processes (joiner/mover/leaver)
- Data analysis skills (Excel formulas, pivot tables)
- Basic understanding of ISO 27001 Control A.5.16

#### Time Commitment

- **Initial assessment:** 12-16 hours (complete user inventory, HR data correlation, lifecycle analysis)
- **Monthly updates:** 2-4 hours (update user inventory, calculate current month metrics)
- **Quarterly comprehensive review:** 6-8 hours (deep dive lifecycle compliance, orphaned account cleanup)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete user inventory** - Every user account across all identity systems
2. ✅ **Lifecycle compliance metrics** - Provisioning/deprovisioning timeliness by user
3. ✅ **Orphaned account register** - Accounts without valid owner identified
4. ✅ **Inactive account tracking** - Accounts with no recent login flagged
5. ✅ **Compliance dashboard** - Overall lifecycle compliance rate calculated
6. ✅ **Gap analysis** - Late provisioning, missed deprovisioning, orphaned accounts prioritized
7. ✅ **Remediation plan** - Actions to improve lifecycle compliance
8. ✅ **Evidence register** - Supporting documentation for audit
9. ✅ **Approved assessment** - Three-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Identity System Access

- Administrator access to ALL identity systems (AD, Azure AD, Okta, Google Workspace, LDAP, custom)
- API access or reporting tools to extract user data
- Access to HR information system (authoritative employee data)
- Access to contractor management system (if separate from HR)

#### 2. HR Data

- Complete employee list with:
  - Employee ID, name, email, department, manager
  - Hire date, termination date (if applicable), employment status
  - Employee type (full-time, part-time, contractor, vendor)
  - Contract end dates (for contractors/vendors)

#### 3. Historical Data

- User account creation logs (last 12 months minimum for trend analysis)
- Termination notifications (HR → IT workflow records)
- Login logs (last 90 days minimum for inactive account detection)
- Previous assessment results (if available for comparison)

#### 4. Policy Requirements

- ISMS-POL-A.5.15-16-18, Section 2.2 (Identity Management Requirements - A.5.16)
  - Section 2.2.1: Identity Lifecycle Framework (joiner/mover/leaver)
  - Section 2.2.2: User Account Provisioning (timeliness requirements)
  - Section 2.2.3: User Account Deprovisioning (timeliness requirements)
  - Section 2.2.6: Orphaned Account Detection and Remediation
  - Section 2.2.7: Contractor/Vendor Identity Management

### Required Tools

- **Microsoft Excel** (2016 or later) for workbook completion
- **Identity system admin tools** (AD Users and Computers, Azure AD Portal, Okta Admin Console, etc.)
- **HR system access** (for authoritative employee data)
- **Data export tools** (PowerShell for AD, Azure CLI, Okta API, LDAP queries)
- **Screen capture tools** (for evidence screenshots)

### Dependencies

This assessment has NO dependencies - it's the first assessment in the A.5.15-16-18 series.

However, outputs from this assessment are INPUT to:
- A.5.15-16-18.2 (Access Rights Matrix) - Uses user inventory as baseline
- A.5.15-16-18.3 (Access Review Results) - Uses user list for review scope
- A.5.15-16-18.4 (Role & SoD Compliance) - Uses user list for role assignment verification
- A.5.15-16-18.5 (IAM Governance Dashboard) - Consolidates lifecycle metrics

---

## Workflow

### High-Level Process

```
1. PREPARE
   ↓
2. EXTRACT USER DATA (from identity systems)
   ↓
3. EXTRACT HR DATA (authoritative source)
   ↓
4. CONSOLIDATE USER INVENTORY (Sheet 1)
   ↓
5. CORRELATE WITH HR DATA (cross-reference)
   ↓
6. CALCULATE PROVISIONING COMPLIANCE (Sheet 2)
   ↓
7. CALCULATE DEPROVISIONING COMPLIANCE (Sheet 3)
   ↓
8. DETECT ORPHANED ACCOUNTS (Sheet 4)
   ↓
9. DETECT INACTIVE ACCOUNTS (Sheet 5)
   ↓
10. ANALYZE COMPLIANCE METRICS (Sheet 6)
    ↓
11. IDENTIFY GAPS & REMEDIATION (Sheet 7)
    ↓
12. REGISTER EVIDENCE (Sheet 8)
    ↓
13. REVIEW & APPROVE (Sheet 9)
```

### Detailed Workflow

#### Phase 1: Preparation (2-3 hours)

**Objective:** Gather information and understand requirements

**Steps:**
1. Read this entire User Guide
2. Read ISMS-POL-A.5.15-16-18, Section 2.2 (Identity Management Requirements)
3. Identify ALL identity systems in your environment (AD, Azure AD, Okta, etc.)
4. Verify access to HR system (authoritative employee data)
5. Schedule time with IAM Team and HR Team for data collection
6. Create working folder for evidence collection (screenshots, data exports)

**Deliverable:** List of all identity systems and HR system access confirmed

**Quality Check:**
- ✓ All identity systems identified (don't miss cloud identity, LDAP, custom systems)
- ✓ HR system access confirmed
- ✓ Policy requirements reviewed and understood
- ✓ Working folder created and accessible

---

#### Phase 2: Extract User Data from Identity Systems (4-6 hours)

**Objective:** Export complete user list from EVERY identity system

**Steps:**

**For Active Directory:**
```powershell
# PowerShell example for AD export
Get-ADUser -Filter * -Properties * | 
Select-Object SamAccountName, GivenName, Surname, EmailAddress, 
              Enabled, whenCreated, lastLogonTimestamp, Department, 
              Manager, EmployeeID, EmployeeType |
Export-Csv -Path "AD_Users_Export.csv" -NoTypeInformation
```

**For Azure AD:**
```powershell
# Azure AD export
Connect-AzureAD
Get-AzureADUser -All $true | 
Select-Object UserPrincipalName, DisplayName, Mail, AccountEnabled, 
              CreatedDateTime, RefreshTokensValidFromDateTime, 
              Department, JobTitle, CompanyName |
Export-Csv -Path "AzureAD_Users_Export.csv" -NoTypeInformation
```

**For Okta:**
- Use Okta Admin Console → Directory → People → Export to CSV
- OR use Okta API for automated export

**For Google Workspace:**
- Use Admin Console → Directory → Users → Download users
- OR use Google Admin SDK API

**For LDAP (OpenLDAP, FreeIPA, etc.):**
```bash
# LDAP query example
ldapsearch -x -LLL -b "ou=users,dc=example,dc=com" "(objectClass=person)" \
  uid cn mail accountStatus createTimestamp loginTimestamp |
  > ldap_users_export.ldif
```

**Consolidation Step:**
- Combine exports from all identity systems into single CSV
- Normalize column names (UserID, Name, Email, Status, CreatedDate, LastLogin, Source)
- Remove duplicates (same user in multiple systems)
- Tag each user with source system

**Deliverable:** Consolidated user export CSV with ALL users from ALL identity systems

**Quality Check:**
- ✓ All identity systems queried (AD, Azure AD, Okta, LDAP, custom)
- ✓ Export includes ALL users (active + disabled)
- ✓ Export includes required attributes (name, email, status, dates)
- ✓ Duplicates identified and tagged
- ✓ Source system tagged for each user

---

#### Phase 3: Extract HR Data (2-3 hours)

**Objective:** Export authoritative employee data from HR system

**Steps:**
1. **Request HR Data Export** from HR Team or HR system admin
2. **Required Fields**:
   - Employee ID (primary key)
   - First Name, Last Name, Email
   - Department, Manager Name/Email
   - Hire Date
   - Termination Date (if applicable)
   - Employment Status (Active, Terminated, Leave of Absence)
   - Employee Type (Employee, Contractor, Vendor)
   - Contract End Date (for contractors)

3. **Verify Data Quality**:
   - No missing hire dates
   - Termination dates accurate (terminated employees marked correctly)
   - Manager names/emails correct
   - Employee types categorized correctly

**Deliverable:** HR data export CSV with authoritative employee information

**Quality Check:**
- ✓ HR data includes ALL current employees
- ✓ HR data includes recent terminations (last 90 days minimum)
- ✓ Hire dates present for all employees
- ✓ Termination dates present for terminated employees
- ✓ Manager information accurate
- ✓ Contractor contract end dates present

---

#### Phase 4: Consolidate User Inventory (3-4 hours)

**Objective:** Complete Sheet 1 - User Inventory Master List

**Steps:**
1. **Import identity system data** into Sheet 1
2. **For EACH user, document**:
   - User ID (primary account identifier)
   - Full Name
   - Email Address
   - Account Status (Active, Disabled, Locked)
   - User Type (Employee, Contractor, Vendor, Service Account, Shared Account)
   - Department, Manager
   - Hire Date (from HR system)
   - Termination Date (from HR system, if applicable)
   - Account Created Date (from identity system)
   - Last Login Date (from identity system logs)
   - Account Source (AD, Azure AD, Okta, etc.)

3. **Cross-reference with HR data**:
   - Match users by email or Employee ID
   - Import hire date and termination date from HR
   - Flag users in identity systems NOT in HR (orphaned accounts)
   - Flag users in HR but NOT in identity systems (provisioning gap)

4. **Calculate derived fields**:
   - Days Since Last Login (Today - Last Login Date)
   - Account Age (Today - Account Created Date)
   - Employment Status (Active, Terminated, Unknown)

**Deliverable:** Complete Sheet 1 with consolidated user inventory

**Quality Check:**
- ✓ All users from all identity systems included
- ✓ All active employees from HR system included
- ✓ No duplicate users (same person listed twice)
- ✓ Account status accurately reflects current state
- ✓ User type correctly categorized
- ✓ Hire dates and termination dates populated where available
- ✓ Last login dates recent (within last 90 days for active users)

---

#### Phase 5: Calculate Provisioning Compliance (2-3 hours)

**Objective:** Complete Sheet 2 - Provisioning Timeliness Analysis

**Steps:**
1. **Filter to NEW HIRES** (users hired in assessment period, e.g., last quarter)
2. **For EACH new hire, calculate**:
   - Hire Date (from HR)
   - Account Created Date (from identity system)
   - Provisioning Delay (Days) = Account Created Date - Hire Date
   - Target SLA (typically 0 days - access ready by start date)
   - Compliance Status:
     - ✅ **On-Time** (≤0 days delay - account ready by/before start date)
     - ⚠️ **Late** (1-5 days delay - minor SLA miss)
     - ❌ **Very Late** (>5 days delay - significant SLA miss)

3. **Calculate metrics**:
   - Total new hires in period
   - On-time provisioning count (≤0 days delay)
   - Late provisioning count (1-5 days)
   - Very late provisioning count (>5 days)
   - **Provisioning Compliance Rate** = (On-Time / Total) × 100%
   - Average provisioning delay (days)
   - Maximum provisioning delay (worst case)

4. **Identify causes** of late provisioning:
   - HR notification delay (HR didn't notify IT on time)
   - IAM Team capacity (backlog of provisioning requests)
   - Technical issues (identity system downtime, sync failures)
   - Manager approval delay (manager didn't approve access request on time)

**Deliverable:** Sheet 2 with provisioning timeliness analysis

**Quality Check:**
- ✓ All new hires in assessment period included
- ✓ Provisioning delay calculated correctly (Account Created - Hire Date)
- ✓ Compliance status accurate (on-time, late, very late)
- ✓ Metrics calculated correctly
- ✓ Causes of delays identified and documented

---

#### Phase 6: Calculate Deprovisioning Compliance (2-3 hours)

**Objective:** Complete Sheet 3 - Deprovisioning Timeliness Analysis

**Steps:**
1. **Filter to TERMINATED USERS** (users terminated in assessment period)
2. **For EACH terminated user, calculate**:
   - Termination Date (from HR)
   - Account Disabled Date (from identity system)
   - Deprovisioning Delay (Days) = Account Disabled Date - Termination Date
   - Target SLA:
     - Termination for cause: 0 days (same day, ideally within 1 hour)
     - Voluntary resignation: 0 days (same business day)
     - Contractor end date: 0 days (scheduled on contract end date)
   - Compliance Status:
     - ✅ **On-Time** (0 days delay - disabled on termination date)
     - ⚠️ **Late** (1-7 days delay - minor risk window)
     - ❌ **Very Late** (>7 days delay - significant security risk)
     - 🚨 **CRITICAL** (>30 days delay or still active - major vulnerability)

3. **Calculate metrics**:
   - Total terminations in period
   - On-time deprovisioning count (0 days delay)
   - Late deprovisioning count (1-7 days)
   - Very late deprovisioning count (>7 days)
   - Critical deprovisioning count (>30 days or still active)
   - **Deprovisioning Compliance Rate** = (On-Time / Total) × 100%
   - Average deprovisioning delay (days)
   - Maximum deprovisioning delay (worst case)

4. **Identify causes** of late deprovisioning:
   - HR notification failure (IT not notified of termination)
   - Weekend/holiday delays (termination on Friday, disabled on Monday)
   - IAM Team capacity (backlog during busy periods)
   - Multi-system complexity (disabled in AD but not Azure AD/Okta)
   - Manager request delay (manager requested delayed disable for handover)

**Deliverable:** Sheet 3 with deprovisioning timeliness analysis

**Quality Check:**
- ✓ All terminations in assessment period included
- ✓ Deprovisioning delay calculated correctly (Disabled Date - Termination Date)
- ✓ Compliance status reflects risk (critical for >30 days)
- ✓ Metrics calculated correctly
- ✓ Causes of delays identified
- ✓ CRITICAL cases flagged for immediate remediation

---

#### Phase 7: Detect Orphaned Accounts (2-3 hours)

**Objective:** Complete Sheet 4 - Orphaned Account Detection

**Steps:**
1. **Cross-reference identity systems with HR data**:
   - Users in identity systems (AD, Azure AD, Okta) NOT in HR system = potential orphaned accounts
   - Filter out legitimate non-HR accounts (service accounts, shared accounts, vendor accounts with valid sponsor)

2. **For EACH potential orphaned account, investigate**:
   - Who is the user? (name, email, department from identity system)
   - When was account created?
   - When was last login? (if never logged in, likely orphaned at creation)
   - What access does this account have? (cross-reference with access rights matrix)
   - Is this a service account? (check account type, naming convention)
   - Is this a vendor account with valid sponsor? (check vendor management system)
   - Is this a former employee whose termination was not processed? (check with HR)

3. **Categorize orphaned accounts**:
   - **Confirmed Orphaned** - Former employee, contractor ended, no valid owner
   - **Service Account** - Non-human account, valid owner documented
   - **Vendor Account** - Third-party access, valid sponsor documented
   - **Pending Investigation** - Need more info to determine status

4. **Calculate metrics**:
   - Total users in identity systems
   - Users matched to HR system (current employees)
   - Orphaned account count (not in HR, not service/vendor)
   - Orphaned account remediation status:
     - ✅ **Remediated** (account disabled/deleted)
     - 🔄 **In Progress** (under investigation or scheduled for removal)
     - ❌ **Outstanding** (identified but not yet addressed)

5. **Create remediation plan**:
   - Prioritize by risk (privileged orphaned accounts = highest priority)
   - Assign ownership (who will investigate/remediate)
   - Set target completion date (typically 30 days maximum)

**Deliverable:** Sheet 4 with orphaned account register and remediation plan

**Quality Check:**
- ✓ All users in identity systems cross-referenced with HR
- ✓ Service accounts excluded (not orphaned, legitimate non-human accounts)
- ✓ Vendor accounts with valid sponsors excluded
- ✓ Confirmed orphaned accounts accurately identified
- ✓ Investigation status documented for each
- ✓ Remediation plan has owners and target dates

---

#### Phase 8: Detect Inactive Accounts (1-2 hours)

**Objective:** Complete Sheet 5 - Inactive Account Detection

**Steps:**
1. **Filter users with no recent login** (Last Login > 90 days ago OR never logged in)
2. **For EACH inactive account, document**:
   - User ID, Name, Email
   - Account Status (Active, Disabled)
   - Last Login Date (or "Never" if never logged in)
   - Days Since Last Login
   - User Type (Employee, Contractor, Service Account)
   - Account Created Date
   - Justification (why is this account inactive but still active?)

3. **Categorize inactive accounts**:
   - **Legitimate Inactive**:
     - Employee on leave of absence (maternity, sabbatical, long-term sick)
     - Seasonal worker (not currently working but will return)
     - Service account (only used periodically, e.g., monthly batch job)
   - **Questionable Inactive**:
     - Employee who should be active but hasn't logged in (check with manager)
     - Contractor whose contract may have ended (verify with HR/Procurement)
     - Account created but never used (provisioned but user never onboarded?)
   - **Orphaned (via inactivity)**:
     - Former employee whose termination was not processed (overlap with orphaned account detection)

4. **Calculate metrics**:
   - Total active accounts
   - Inactive account count (>90 days no login)
   - Never-logged-in account count
   - Inactive accounts with justification (documented reason)
   - Inactive accounts without justification (require review)

5. **Create review plan**:
   - Accounts inactive >180 days → High priority review (likely orphaned or should be disabled)
   - Accounts inactive 90-180 days → Medium priority review
   - Never-logged-in accounts → Immediate review (why created if never used?)

**Deliverable:** Sheet 5 with inactive account register

**Quality Check:**
- ✓ Last login dates accurate (from identity system logs)
- ✓ Days since last login calculated correctly
- ✓ Legitimate inactive accounts documented with justification (leave of absence, seasonal, etc.)
- ✓ Questionable inactive accounts flagged for manager review
- ✓ Never-logged-in accounts highlighted (high priority investigation)

---

#### Phase 9: Analyze Compliance Metrics (1-2 hours)

**Objective:** Complete Sheet 6 - Lifecycle Compliance Dashboard

**Steps:**
1. **Consolidate metrics** from Sheets 2-5:
   - **Provisioning Compliance Rate** (from Sheet 2)
   - **Deprovisioning Compliance Rate** (from Sheet 3)
   - **Orphaned Account Count** (from Sheet 4)
   - **Inactive Account Count** (from Sheet 5)

2. **Calculate overall IAM lifecycle maturity score**:
   ```
   Lifecycle Maturity Score = 
     (Provisioning Compliance × 25%) + 
     (Deprovisioning Compliance × 40%) + 
     (100% - Orphaned Account %) × 20%) + 
     (100% - Inactive Account %) × 15%)
   ```
   *Note: Deprovisioning weighted highest due to security risk*

3. **Benchmark against industry standards**:
   - **Excellent (90-100%)**: Best-in-class lifecycle management
   - **Good (75-89%)**: Strong lifecycle controls, minor improvements needed
   - **Fair (60-74%)**: Acceptable but significant gaps exist
   - **Poor (<60%)**: Major lifecycle deficiencies, high security risk

4. **Trend analysis** (if historical data available):
   - Compare current quarter vs. previous quarter
   - Provisioning compliance trend (improving/declining?)
   - Deprovisioning compliance trend
   - Orphaned account trend (cleanup effective?)

5. **Document findings**:
   - Strengths (areas of compliance)
   - Weaknesses (areas of non-compliance)
   - Root causes (why are we non-compliant?)
   - Recommendations (how to improve)

**Deliverable:** Sheet 6 with compliance dashboard and analysis

**Quality Check:**
- ✓ All metrics calculated correctly
- ✓ Overall maturity score formula applied correctly
- ✓ Benchmark categories accurate
- ✓ Trend analysis meaningful (comparing equivalent time periods)
- ✓ Findings documented clearly

---

#### Phase 10: Identify Gaps & Remediation Plan (2-3 hours)

**Objective:** Complete Sheet 7 - Gap Analysis & Remediation Plan

**Steps:**
1. **Identify all gaps** from previous sheets:
   - **Provisioning Gaps** (late provisioning, users missed)
   - **Deprovisioning Gaps** (late deprovisioning, still-active terminated users)
   - **Orphaned Account Gaps** (accounts without valid owner)
   - **Inactive Account Gaps** (accounts inactive >90 days without justification)

2. **Prioritize gaps by risk**:
   - **Critical** (P1):
     - Terminated employees still active (>7 days post-termination)
     - Orphaned privileged accounts (admin, root, elevated access)
     - Never-logged-in accounts with privileged access
   - **High** (P2):
     - Terminated employees still active (1-7 days post-termination)
     - Orphaned standard accounts
     - Inactive accounts >180 days
   - **Medium** (P3):
     - Late provisioning (1-5 days)
     - Inactive accounts 90-180 days
   - **Low** (P4):
     - Late provisioning (<1 day)
     - Service accounts with infrequent use (justified)

3. **Create remediation actions**:

| Gap ID | Gap Description | Priority | Action | Owner | Target Date | Status |
|--------|----------------|----------|--------|-------|-------------|--------|
| GAP-001 | 5 terminated users still active (>30 days) | Critical | Disable accounts immediately, investigate why not disabled | IAM Team | Today | Open |
| GAP-002 | 12 orphaned accounts detected | High | Investigate ownership, disable if confirmed orphaned | Security Team | 14 days | In Progress |
| GAP-003 | 45 users inactive >90 days | Medium | Manager review, disable if no justification | Managers | 30 days | Open |
| GAP-004 | Provisioning SLA missed 15% of time | Medium | Automate HR→IT workflow, reduce manual delays | IAM Team | 60 days | Planned |
| GAP-005 | Deprovisioning SLA missed 20% of time | High | Improve HR termination notification process | HR + IT | 30 days | In Progress |

4. **Track remediation progress**:
   - Action completion status (Open, In Progress, Completed)
   - Percent complete (0%, 25%, 50%, 75%, 100%)
   - Notes on progress or blockers

**Deliverable:** Sheet 7 with gap analysis and remediation plan

**Quality Check:**
- ✓ All gaps identified from previous sheets
- ✓ Prioritization reflects actual risk (deprovisioning > provisioning)
- ✓ Remediation actions are specific and actionable
- ✓ Owners assigned for each action
- ✓ Target dates are realistic but urgent for critical gaps
- ✓ Status tracking in place

---

#### Phase 11: Register Evidence (1 hour)

**Objective:** Complete Sheet 8 - Evidence Register

**Steps:**
1. **List all evidence collected**:
   - Identity system exports (AD, Azure AD, Okta, etc.)
   - HR system export
   - Login logs (for inactive account detection)
   - Screenshots (identity system dashboards, user counts)
   - Policy documents (ISMS-POL-A.5.15-16-18, Section 2.2)
   - HR termination notification records (examples)
   - Orphaned account investigation notes
   - Manager approvals for inactive account exceptions

2. **For EACH piece of evidence, document**:
   - Evidence ID (EVID-001, EVID-002, etc.)
   - Evidence Type (Data Export, Screenshot, Policy Document, Email, Meeting Notes, etc.)
   - Description (what is this evidence?)
   - Related Sheet/Row (where is this evidence referenced?)
   - Location/Path (file path, URL, document management system location)
   - Date Collected (when was this evidence captured?)
   - Collected By (who gathered this evidence?)
   - Verification Status (Verified, Pending, Not Verified)

3. **Organize evidence** in logical folder structure:
   ```
   Evidence/
   ├── Identity_System_Exports/
   │   ├── AD_Users_Export_2026-01-22.csv
   │   ├── AzureAD_Users_Export_2026-01-22.csv
   │   └── Okta_Users_Export_2026-01-22.json
   ├── HR_Data/
   │   └── HR_Employee_List_2026-01-22.csv
   ├── Login_Logs/
   │   └── Last_Login_Report_2026-01-22.xlsx
   ├── Screenshots/
   │   ├── AD_User_Count_2026-01-22.png
   │   └── Orphaned_Account_Example_2026-01-22.png
   ├── Policy_Documents/
   │   └── ISMS-POL-A.5.15-16-18.md
   └── Approvals/
       └── Manager_Approval_Inactive_Accounts.pdf
   ```

4. **Verify evidence quality**:
   - All evidence recent (< 30 days old for most items)
   - Evidence accessible to auditors
   - Evidence clearly labeled and organized
   - Evidence demonstrates compliance (or non-compliance with remediation plan)

**Deliverable:** Sheet 8 with complete evidence register

**Quality Check:**
- ✓ All evidence collected and documented
- ✓ Evidence organized in logical folder structure
- ✓ Evidence IDs cross-referenced to assessment sheets
- ✓ All evidence verified as accurate and current
- ✓ Evidence accessible for audit

---

#### Phase 12: Review & Approval (2-3 hours)

**Objective:** Three-level approval process (Sheet 9 - Approval & Sign-Off)

**Steps:**

**Step 1: Self-Review (Assessment Completer)**
- Run through Quality Checklist (see section below)
- Verify all sheets complete
- Check all formulas calculating correctly
- Validate data accuracy (spot-check random users)
- Ensure evidence collected and accessible
- Complete "Assessment Completed By" section in Sheet 9

**Step 2: IAM Team Lead Review**
- Review user inventory completeness (all identity systems included?)
- Verify lifecycle calculations accurate (provisioning/deprovisioning delays)
- Check orphaned account detection logic (false positives?)
- Validate inactive account thresholds (90 days appropriate?)
- Review gap analysis and remediation plan (prioritization correct?)
- Approve or request changes
- Complete "Reviewed By (IAM Team Lead)" section in Sheet 9

**Step 3: Security Team / CISO Review**
- Review overall lifecycle compliance rate (acceptable?)
- Assess critical gaps (terminated users still active = unacceptable)
- Verify remediation plans have adequate resources and timelines
- Approve gap priorities (deprovisioning delays = higher priority)
- Accept residual risk (if any gaps cannot be immediately remediated)
- Final approval
- Complete "Approved By (CISO)" section in Sheet 9

**Approval Timeline:** 
- Self-review: Same day
- IAM Team Lead review: 2-3 business days
- CISO review: 2-3 business days
- Total: ~1 week from submission to final approval

**Deliverable:** Approved assessment ready for IAM Governance Dashboard (A.5.15-16-18.5)

**Quality Check:**
- ✓ All three approval levels completed
- ✓ All review comments addressed
- ✓ Critical gaps have immediate remediation actions
- ✓ Evidence is audit-ready
- ✓ Assessment status set to "Final"

---

## Evidence Collection

### What Evidence to Collect

**For Sheet 1 (User Inventory):**
- Identity system exports (AD, Azure AD, Okta, etc.) - CSV/Excel
- HR system export - CSV/Excel
- Screenshots of user counts from admin consoles
- Network diagrams showing identity system architecture

**For Sheet 2 (Provisioning Compliance):**
- HR new hire notifications (example emails or tickets)
- IAM team provisioning logs (timestamped)
- Screenshots of account creation audit logs
- Manager access approval examples

**For Sheet 3 (Deprovisioning Compliance):**
- HR termination notifications (example emails or tickets)
- IAM team deprovisioning logs (timestamped)
- Screenshots of account disable audit logs
- Examples of delayed deprovisioning and root causes

**For Sheet 4 (Orphaned Accounts):**
- Cross-reference report (users in identity systems not in HR)
- Orphaned account investigation notes
- Screenshots of orphaned account details (last login, access rights)
- Remediation evidence (disabled account confirmation)

**For Sheet 5 (Inactive Accounts):**
- Login log reports (last 90 days)
- Never-logged-in user report
- Manager justifications for legitimate inactive accounts (email approvals)
- Screenshots of inactive account details

**For Sheet 6 (Compliance Dashboard):**
- Trend charts (if historical data available)
- Comparison with previous assessment
- Benchmark references (industry standards for lifecycle compliance)

**For Sheet 7 (Gap Analysis):**
- Gap remediation project plans
- Resource allocation approvals
- Target date commitments from owners
- Progress updates on in-flight remediation

**For Sheet 8 (Evidence Register):**
- All evidence listed above, organized and accessible

**For Sheet 9 (Approval):**
- Approval emails or sign-off forms
- Meeting minutes from review sessions
- CISO acceptance of risk for unresolved gaps

### How to Organize Evidence

**Folder Structure:**
```
ISMS-A.5.15-16-18.1_Evidence_YYYYMMDD/
├── 01_Identity_System_Exports/
├── 02_HR_Data/
├── 03_Login_Logs/
├── 04_Screenshots/
├── 05_Audit_Logs/
├── 06_Approvals/
├── 07_Policy_Documents/
└── 08_Remediation_Plans/
```

**File Naming Convention:**
```
EVID-###_Description_YYYYMMDD.ext

Examples:
EVID-001_AD_Users_Export_20260122.csv
EVID-002_HR_Employee_List_20260122.xlsx
EVID-003_Orphaned_Account_Screenshot_20260122.png
EVID-004_Deprovisioning_Delay_Root_Cause_Analysis_20260122.pdf
```

### Evidence Retention

- **Minimum retention:** 3 years (to cover full ISO 27001 certification cycle)
- **Recommended retention:** 5 years (for trend analysis and long-term improvement tracking)
- **Storage location:** Secure document management system with access controls
- **Access:** IAM Team, Security Team, Internal Audit, External Auditors (read-only)

---

## Common Pitfalls

### Pitfall 1: Incomplete User Inventory

❌ **Mistake:** Only exporting users from Active Directory, missing Azure AD cloud-only accounts or Okta SSO accounts

✅ **Fix:** Export from ALL identity systems (AD, Azure AD, Okta, Google Workspace, LDAP, custom systems) and consolidate

---

### Pitfall 2: Missing HR Data Cross-Reference

❌ **Mistake:** Assessing lifecycle compliance without HR data (hire dates, termination dates)

✅ **Fix:** Work with HR to get authoritative employee data export. Cannot calculate provisioning/deprovisioning timeliness without it.

---

### Pitfall 3: Incorrect Lifecycle Delay Calculation

❌ **Mistake:** Calculating provisioning delay as (Today - Account Created Date) instead of (Account Created Date - Hire Date)

✅ **Fix:** 
- **Provisioning Delay** = Account Created Date - Hire Date (negative = early provisioning, 0 = on-time, positive = late)
- **Deprovisioning Delay** = Account Disabled Date - Termination Date (0 = on-time, positive = late)

---

### Pitfall 4: Service Accounts Counted as Orphaned Accounts

❌ **Mistake:** Flagging all non-HR accounts as orphaned, including legitimate service accounts

✅ **Fix:** Exclude service accounts (identified by naming convention, account type, or manual categorization) from orphaned account detection. Service accounts are NOT orphaned; they're intentionally non-human.

---

### Pitfall 5: Ignoring Contractors and Vendors

❌ **Mistake:** Only assessing employee lifecycle, ignoring contractors and vendors

✅ **Fix:** Include contractors and vendors in assessment. They have different lifecycle requirements (time-bound access, contract end dates) but still require compliance assessment.

---

### Pitfall 6: No Remediation Plan for Critical Gaps

❌ **Mistake:** Identifying terminated users still active (critical gap) but no immediate remediation action

✅ **Fix:** Critical gaps (especially deprovisioning delays >7 days) require IMMEDIATE remediation. "Owner: IAM Team, Target Date: Today, Action: Disable accounts now, investigate why not disabled later."

---

### Pitfall 7: Stale Login Data

❌ **Mistake:** Using login logs from 6 months ago to identify inactive accounts

✅ **Fix:** Use recent login logs (last 90 days maximum). Inactive account detection requires current data.

---

### Pitfall 8: Overly Optimistic Compliance Scoring

❌ **Mistake:** Marking provisioning as "on-time" when account created 1 day before hire date (should be on or before hire date, but 1 day before is cutting it close and may indicate process risk)

✅ **Fix:** Be honest in compliance assessment. The goal is to identify and fix gaps, not to inflate compliance scores.

---

### Pitfall 9: No Trend Analysis

❌ **Mistake:** Only assessing current quarter, no comparison with previous quarters

✅ **Fix:** If historical data available, compare current quarter with previous quarter. Is lifecycle compliance improving or declining? This shows whether remediation actions are effective.

---

### Pitfall 10: Forgetting Multi-System Users

❌ **Mistake:** User has account in both AD and Azure AD, only checking deprovisioning in AD (still active in Azure AD)

✅ **Fix:** For deprovisioning compliance, verify user disabled in ALL identity systems they have accounts in. Multi-system environments require comprehensive deprovisioning.

---

## Quality Checklist

Before submitting for approval, verify:

### User Inventory (Sheet 1)
- [ ] All identity systems queried (AD, Azure AD, Okta, Google Workspace, LDAP, custom)
- [ ] All users included (active + disabled, not just active)
- [ ] User types correctly categorized (Employee, Contractor, Vendor, Service Account, Shared)
- [ ] HR data cross-referenced (hire dates, termination dates populated where available)
- [ ] Last login dates accurate (from recent login logs, not stale data)
- [ ] No "Unknown" or "TBD" values
- [ ] Source system tagged for each user
- [ ] Duplicates identified and handled (same user in multiple systems)

### Provisioning Compliance (Sheet 2)
- [ ] All new hires in assessment period included
- [ ] Hire dates accurate (from HR system)
- [ ] Account created dates accurate (from identity system audit logs)
- [ ] Provisioning delay calculated correctly (Account Created - Hire Date)
- [ ] Compliance status reflects SLA (on-time = ≤0 days, late = 1-5 days, very late = >5 days)
- [ ] Provisioning compliance rate calculated correctly
- [ ] Causes of delays identified and documented
- [ ] Late provisioning cases have remediation actions

### Deprovisioning Compliance (Sheet 3)
- [ ] All terminations in assessment period included
- [ ] Termination dates accurate (from HR system)
- [ ] Account disabled dates accurate (from identity system audit logs)
- [ ] Deprovisioning delay calculated correctly (Disabled Date - Termination Date)
- [ ] Critical cases flagged (>30 days or still active after termination)
- [ ] Deprovisioning compliance rate calculated correctly
- [ ] Causes of delays identified
- [ ] CRITICAL cases have immediate remediation actions (disable today)
- [ ] Multi-system users verified (disabled in ALL identity systems)

### Orphaned Accounts (Sheet 4)
- [ ] All identity system users cross-referenced with HR data
- [ ] Service accounts excluded from orphaned account count (not orphaned, legitimate)
- [ ] Vendor accounts with valid sponsors excluded
- [ ] Confirmed orphaned accounts accurately identified
- [ ] Investigation status documented for each orphaned account
- [ ] Remediation plan has owners and target dates
- [ ] Privileged orphaned accounts prioritized (highest risk)

### Inactive Accounts (Sheet 5)
- [ ] Last login data recent (from logs within last 90 days)
- [ ] Inactive threshold applied consistently (>90 days no login)
- [ ] Never-logged-in accounts identified
- [ ] Legitimate inactive accounts have justification (leave of absence, seasonal, service account)
- [ ] Questionable inactive accounts flagged for manager review
- [ ] Inactive account count excludes legitimately inactive (e.g., service accounts with periodic use)

### Compliance Dashboard (Sheet 6)
- [ ] All metrics pulled from correct sheets (provisioning from Sheet 2, deprovisioning from Sheet 3, etc.)
- [ ] Overall maturity score calculated correctly (weighted formula)
- [ ] Benchmark category accurate (Excellent/Good/Fair/Poor)
- [ ] Trend analysis meaningful (if historical data available)
- [ ] Findings clearly documented (strengths, weaknesses, root causes, recommendations)

### Gap Analysis (Sheet 7)
- [ ] All gaps identified from previous sheets
- [ ] Prioritization reflects actual risk (Critical = terminated users still active, orphaned privileged accounts)
- [ ] Remediation actions specific and actionable (not vague "improve process")
- [ ] Owners assigned for each action
- [ ] Target dates realistic but urgent for critical gaps
- [ ] Status tracking in place (Open, In Progress, Completed)

### Evidence Register (Sheet 8)
- [ ] All evidence collected and listed
- [ ] Evidence organized in logical folder structure
- [ ] Evidence IDs cross-referenced to assessment sheets
- [ ] All evidence verified as accurate and current
- [ ] Evidence accessible for audit (file paths correct, permissions set)
- [ ] Evidence recent (< 30 days old for most items)

### Approval (Sheet 9)
- [ ] Self-review completed (assessment completer sign-off)
- [ ] IAM Team Lead review completed (technical accuracy verified)
- [ ] CISO review completed (gaps accepted, remediation approved)
- [ ] All review comments addressed
- [ ] Assessment status set to "Final"

---

## Review & Approval

### Review Process

**Step 1: Self-Review** (Assessment Completer)
- Run through entire Quality Checklist above
- Verify all sheets complete and accurate
- Check formulas calculating correctly
- Validate data accuracy (spot-check random users against source systems)
- Ensure evidence collected and accessible
- **Time Commitment:** 2-3 hours

**Step 2: IAM Team Lead Review**
- **Focus:** Technical accuracy, data quality, lifecycle calculations
- **Review Criteria:**
  - User inventory complete (all identity systems included?)
  - Provisioning/deprovisioning delays calculated correctly?
  - Orphaned account detection logic sound (false positives minimized?)
  - Inactive account thresholds appropriate (90 days reasonable for your org?)
  - Gap analysis accurate (missing any major gaps?)
  - Remediation plan realistic (owners have capacity, timelines achievable?)
- **Decision:** Approve / Approve with Conditions / Reject (send back for corrections)
- **Time Commitment:** 3-5 hours
- **Turnaround:** 2-3 business days

**Step 3: Security Team / CISO Review**
- **Focus:** Compliance level, risk acceptance, resource allocation for remediation
- **Review Criteria:**
  - Overall lifecycle compliance rate acceptable? (target >85%)
  - Critical gaps identified and prioritized correctly?
  - Remediation plans have adequate resources and timelines?
  - Deprovisioning delays addressed urgently? (security risk priority)
  - Risk acceptance for gaps that cannot be immediately remediated?
- **Decision:** Final Approval / Approve with Conditions / Reject
- **Time Commitment:** 2-3 hours
- **Turnaround:** 2-3 business days

### If Assessment Rejected

Common reasons for rejection:
- **Incomplete data:** Missing identity systems, incomplete HR data cross-reference
- **Calculation errors:** Provisioning/deprovisioning delays calculated incorrectly
- **Insufficient evidence:** Claims not backed by evidence
- **No remediation plan:** Gaps identified but no actions assigned
- **Unrealistic timelines:** Critical gaps with 90-day remediation (should be immediate)

**Corrective Action:**
1. Address review comments
2. Update affected sheets
3. Revalidate calculations
4. Collect missing evidence
5. Update version/date in Document Control
6. Resubmit with change summary

### Approval Timeline

```
Day 1:       Assessment completed, self-review done, submitted to IAM Team Lead
Day 2-4:     IAM Team Lead review
Day 5:       IAM Team Lead approves (or sends back for corrections)
Day 6-8:     CISO review
Day 9:       CISO final approval
Day 10:      Assessment marked "Final", ready for IAM Governance Dashboard
```

**Total timeline:** ~2 weeks from start to final approval

---

## Integration with Other Assessments

This assessment (A.5.15-16-18.1) feeds into:

### A.5.15-16-18.2 - Access Rights Matrix Assessment
- **Uses:** User inventory from Sheet 1 as baseline
- **Mapping:** User ID → Systems/Applications → Access Level
- **Dependency:** Cannot assess access rights without knowing WHO the users are

### A.5.15-16-18.3 - Access Review Results Assessment
- **Uses:** User list from Sheet 1 as review scope
- **Mapping:** Which users' access was reviewed, which was confirmed/removed
- **Dependency:** Access reviews verify appropriateness of users' access (needs user list)

### A.5.15-16-18.4 - Role Definition & SoD Compliance Assessment
- **Uses:** User list from Sheet 1 for role assignment verification
- **Mapping:** User ID → Roles → SoD Violations
- **Dependency:** SoD assessment requires knowing which users exist and what roles they have

### A.5.15-16-18.5 - IAM Governance Compliance Dashboard
- **Uses:** Lifecycle compliance metrics from Sheet 6
- **Consolidation:** Combines metrics from all 5 IAM assessments into executive dashboard
- **Dependency:** Dashboard cannot be complete without lifecycle compliance data

---

## Continuous Improvement

### Monthly Updates

For ongoing assessments (not initial assessment):
1. **Update user inventory** (Sheet 1) - add new hires, remove terminated users, update status
2. **Calculate current month metrics** (Sheets 2-3) - provisioning/deprovisioning for current month
3. **Scan for new orphaned accounts** (Sheet 4) - monthly cross-reference
4. **Update inactive account list** (Sheet 5) - monthly login log analysis
5. **Update compliance dashboard** (Sheet 6) - recalculate metrics
6. **Track remediation progress** (Sheet 7) - update gap closure status

**Time Commitment:** 2-4 hours per month (after initial assessment complete)

### Quarterly Comprehensive Review

1. **Deep dive lifecycle analysis** - analyze trends, identify systemic issues
2. **Orphaned account cleanup campaign** - intensive investigation and remediation
3. **Process improvement** - address root causes of provisioning/deprovisioning delays
4. **Benchmark review** - compare against previous quarter, assess improvement

**Time Commitment:** 6-8 hours per quarter

### Annual Strategic Review

1. **Year-over-year comparison** - how much has lifecycle compliance improved?
2. **Technology assessment** - are current identity systems adequate? Need upgrades?
3. **Automation opportunities** - can we automate more of joiner/mover/leaver?
4. **Policy updates** - do lifecycle SLAs need adjustment?

**Time Commitment:** 1-2 days annually

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

## Workbook Structure

### Sheet 1: Instructions_and_Legend

#### Header Section
- **Title:** "ISMS-IMP-A.5.15-16-18.S1 – User Inventory & Lifecycle Compliance Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.5.16: Identity Management"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block (Rows 3-12)
```
Document ID:           ISMS-IMP-A.5.15-16-18.S1
Assessment Area:       User Inventory & Identity Lifecycle Compliance
Related Policy:        ISMS-POL-A.5.15-16-18, Section 2.2 (A.5.16 - Identity Management)
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Assessment Period:     [USER INPUT - e.g., "Q1 2026", "January 2026"]
Review Cycle:          Monthly (user inventory), Quarterly (comprehensive lifecycle review)
```

#### How to Use This Workbook (Rows 14-30)
1. **Sheet 1 - User Inventory Master List:** Export users from ALL identity systems (AD, Azure AD, Okta, etc.), consolidate into single list, cross-reference with HR data
2. **Sheet 2 - Provisioning Timeliness:** Analyze new hires, calculate days from hire date to account creation, assess compliance with SLA (≤0 days)
3. **Sheet 3 - Deprovisioning Timeliness:** Analyze terminations, calculate days from termination to account disable, assess compliance with SLA (0 days)
4. **Sheet 4 - Orphaned Account Detection:** Cross-reference identity systems with HR, identify accounts without valid business owner, track remediation
5. **Sheet 5 - Inactive Account Detection:** Identify users with no login >90 days, categorize as legitimate/questionable, create review plan
6. **Sheet 6 - Lifecycle Compliance Dashboard:** Consolidate metrics from Sheets 2-5, calculate overall maturity score, benchmark performance
7. **Sheet 7 - Gap Analysis & Remediation:** Identify all gaps (late provisioning, late deprovisioning, orphaned accounts, inactive accounts), prioritize by risk, create remediation plan
8. **Sheet 8 - Evidence Register:** Document all evidence collected (identity system exports, HR data, login logs, screenshots, approvals)
9. **Sheet 9 - Approval & Sign-Off:** Three-level approval workflow (Self-Review → IAM Team Lead → CISO)

#### Status Legend (Rows 32-40)
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | On-Time / Compliant | Lifecycle SLA met (provisioning ≤0 days, deprovisioning 0 days) | Green (C6EFCE) |
| ⚠️ | Late / Partial | Minor SLA miss (provisioning 1-5 days, deprovisioning 1-7 days) | Yellow (FFEB9C) |
| ❌ | Very Late / Non-Compliant | Significant SLA miss (provisioning >5 days, deprovisioning >7 days) | Red (FFC7CE) |
| 🚨 | CRITICAL | Critical security risk (deprovisioning >30 days or terminated user still active) | Dark Red (FF0000) |
| ℹ️ | Under Investigation | Status being investigated (orphaned account verification, inactive account review) | Blue (B4C7E7) |
| N/A | Not Applicable | Does not apply to this user type (e.g., service accounts don't have hire dates) | Gray (D3D3D3) |

#### User Type Legend (Rows 42-50)
| User Type | Description | Lifecycle Characteristics |
|-----------|-------------|--------------------------|
| **Employee** | Full-time/part-time staff with employment contract | Joiner process, no expiration date, leaver on termination |
| **Contractor** | Temporary workers with defined contract end date | Joiner process, mandatory expiration date, leaver on contract end |
| **Vendor** | Third-party service providers requiring system access | Requires internal sponsor, time-bound access, quarterly review |
| **Service Account** | Non-human accounts for applications/systems | No hire/termination dates, requires documented owner, password rotation |
| **Shared Account** | Accounts used by multiple individuals (discouraged) | Requires CISO approval, enhanced logging, quarterly review |
| **Emergency** | Break-glass accounts for disaster scenarios | Dormant, usage triggers alert, quarterly verification |

#### Acceptable Evidence (Rows 52-70)
- ✓ Identity system exports (AD, Azure AD, Okta, Google Workspace, LDAP) - CSV/JSON
- ✓ HR system export (employee list with hire/termination dates)
- ✓ Login logs (last 90 days minimum for inactive account detection)
- ✓ Screenshots from identity system admin consoles (user counts, audit logs)
- ✓ HR termination notification examples (emails, tickets)
- ✓ IAM team provisioning/deprovisioning logs (timestamped actions)
- ✓ Account creation audit logs (AD "whenCreated", Azure AD "CreatedDateTime")
- ✓ Account disable audit logs (AD "accountDisabled", Azure AD "AccountEnabled=False")
- ✓ Orphaned account investigation notes (ownership verification attempts)
- ✓ Manager approvals for inactive account exceptions (email confirmations)
- ✓ Service account owner documentation (application owner, technical lead)
- ✓ Contractor sponsor verification (internal sponsor, contract end dates)
- ✓ Policy documents (ISMS-POL-A.5.15-16-18, Section 2.2)
- ✓ Gap remediation project plans and progress reports
- ✓ Approval sign-offs (Self-Review, IAM Team Lead, CISO)

---

## Sheet 2: User_Inventory_Master_List

### Purpose
Complete inventory of ALL users across ALL identity systems, cross-referenced with HR data.

### Header Section (Rows 1-3)
**Row 1:** "USER INVENTORY MASTER LIST"  
**Row 2:** "Complete list of all users from all identity systems, cross-referenced with HR data"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | User ID | Text | Primary account identifier (SamAccountName, UPN, UID) | **USER INPUT** from identity system export | None |
| B | Full Name | Text | User's full name | **USER INPUT** from identity system | None |
| C | Email Address | Text | Primary email address | **USER INPUT** from identity system | None |
| D | Account Status | Dropdown | Current account status | Dropdown: Active, Disabled, Locked, Deleted | **CF:** Green if Active, Red if Disabled/Deleted |
| E | User Type | Dropdown | User categorization | Dropdown: Employee, Contractor, Vendor, Service Account, Shared Account, Emergency | **CF:** Yellow if Shared/Emergency |
| F | Department | Text | Organizational department | **USER INPUT** from HR or identity system | None |
| G | Manager Name | Text | Direct manager's name | **USER INPUT** from HR or identity system | None |
| H | Manager Email | Text | Direct manager's email | **USER INPUT** from HR | None |
| I | Location | Text | Physical location/office | **USER INPUT** from HR | None |
| J | Hire Date | Date | Employee hire date (from HR) | **USER INPUT** from HR system | **CF:** Missing hire date = Yellow (for employees) |
| K | Termination Date | Date | Employee termination date (from HR) | **USER INPUT** from HR system (blank if active) | **CF:** Red if terminated + account still active |
| L | Contract End Date | Date | Contractor contract end date | **USER INPUT** from HR/Procurement | **CF:** Red if past contract end + still active |
| M | Account Created Date | Date | When account was created | **USER INPUT** from identity system (AD whenCreated, Azure AD CreatedDateTime) | None |
| N | Last Login Date | Date | Last successful authentication | **USER INPUT** from login logs | **CF:** Red if >90 days and account active |
| O | Account Source | Text | Which identity system (AD, Azure AD, Okta, etc.) | **USER INPUT** | None |
| P | Employment Status | Calculated | Current employment status | **FORMULA:** `=IF(K<>"", "Terminated", IF(J<>"", "Active", "Unknown"))` | **CF:** Red if Terminated, Green if Active |
| Q | Days Since Last Login | Calculated | Days between today and last login | **FORMULA:** `=IF(N<>"", TODAY()-N, "Never")` | **CF:** Red if >90, Yellow if 60-90, Green if <60 |
| R | Account Age (Days) | Calculated | Days since account created | **FORMULA:** `=IF(M<>"", TODAY()-M, "")` | None |
| S | Provisioning Delay (Days) | Calculated | Days from hire to account creation | **FORMULA:** `=IF(AND(J<>"",M<>""), M-J, "N/A")` | **CF:** Green if ≤0, Yellow if 1-5, Red if >5 |
| T | Deprovisioning Delay (Days) | Calculated | Days from termination to account disable | **FORMULA:** `=IF(AND(K<>"",D="Disabled"), [DisableDate]-K, IF(AND(K<>"",D="Active"), TODAY()-K, "N/A"))` *Note: Disable date may need manual entry or separate audit log import* | **CF:** Green if 0, Yellow if 1-7, Red if >7, DARK RED if >30 |
| U | Orphaned Account Flag | Calculated | Is this an orphaned account? | **FORMULA:** `=IF(AND(P="Unknown", E="Employee"), "YES - Investigate", IF(AND(P="Terminated", D="Active", Q>90), "YES - Former Employee", "NO"))` | **CF:** Red if YES |
| V | Inactive Account Flag | Calculated | Is this an inactive account? | **FORMULA:** `=IF(AND(D="Active", Q>90), "YES - Review Required", "NO")` | **CF:** Yellow if YES |
| W | Compliance Status | Calculated | Overall lifecycle compliance | **FORMULA:** Complex - see below | **CF:** Green if Compliant, Yellow if Partial, Red if Non-Compliant |
| X | Notes | Text | Free-text notes | **USER INPUT** | None |

### Compliance Status Formula (Column W)
```excel
=IF(E="Service Account", "N/A - Service Account",
  IF(E="Shared Account", "N/A - Shared Account",
    IF(P="Terminated",
      IF(D="Disabled", "Compliant - Deprovisioned", "❌ NON-COMPLIANT - Still Active"),
      IF(AND(S<=0, V="NO"), "✅ Compliant", 
        IF(OR(S>5, Q>90), "❌ Non-Compliant",
          "⚠️ Partial Compliance")))))
```

**Logic:**
- Service accounts and shared accounts → N/A (different lifecycle)
- Terminated users:
  - If disabled → Compliant
  - If still active → NON-COMPLIANT (critical)
- Active users:
  - If provisioned on-time (≤0 days) AND not inactive → Compliant
  - If provisioned very late (>5 days) OR inactive (>90 days) → Non-Compliant
  - Otherwise → Partial Compliance

### Summary Metrics (Top of Sheet, Rows 1-2, Columns AA-AH)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Users | `=COUNTA(A:A)-1` (subtract header) | AA1 |
| Active Users | `=COUNTIF(D:D,"Active")` | AB1 |
| Disabled Users | `=COUNTIF(D:D,"Disabled")` | AC1 |
| Employees | `=COUNTIF(E:E,"Employee")` | AD1 |
| Contractors | `=COUNTIF(E:E,"Contractor")` | AE1 |
| Service Accounts | `=COUNTIF(E:E,"Service Account")` | AF1 |
| Orphaned Accounts | `=COUNTIF(U:U,"YES*")` | AG1 |
| Inactive Accounts | `=COUNTIF(V:V,"YES*")` | AH1 |

### Data Validation (Dropdowns)

**Account Status (Column D):**
- List: Active, Disabled, Locked, Deleted

**User Type (Column E):**
- List: Employee, Contractor, Vendor, Service Account, Shared Account, Emergency

### Conditional Formatting Rules

**Account Status (Column D):**
- Rule 1: If "Active" → Fill: C6EFCE (green)
- Rule 2: If "Disabled" OR "Deleted" → Fill: FFC7CE (red)
- Rule 3: If "Locked" → Fill: FFEB9C (yellow)

**User Type (Column E):**
- Rule 1: If "Shared Account" OR "Emergency" → Fill: FFEB9C (yellow) - requires special handling

**Hire Date (Column J):**
- Rule 1: If BLANK AND User Type = "Employee" → Fill: FFEB9C (yellow) - missing data

**Termination Date (Column K):**
- Rule 1: If NOT BLANK AND Account Status = "Active" → Fill: FF0000 (dark red) - CRITICAL

**Last Login Date (Column N):**
- Rule 1: If (TODAY() - N) > 90 AND Account Status = "Active" → Fill: FFC7CE (red)

**Days Since Last Login (Column Q):**
- Rule 1: If >90 → Fill: FFC7CE (red)
- Rule 2: If 60-90 → Fill: FFEB9C (yellow)
- Rule 3: If <60 → Fill: C6EFCE (green)

**Provisioning Delay (Column S):**
- Rule 1: If ≤0 → Fill: C6EFCE (green) - on-time or early
- Rule 2: If 1-5 → Fill: FFEB9C (yellow) - late but minor
- Rule 3: If >5 → Fill: FFC7CE (red) - very late

**Deprovisioning Delay (Column T):**
- Rule 1: If 0 → Fill: C6EFCE (green) - on-time
- Rule 2: If 1-7 → Fill: FFEB9C (yellow) - late but acceptable
- Rule 3: If 8-30 → Fill: FFC7CE (red) - very late
- Rule 4: If >30 → Fill: FF0000 (dark red) - CRITICAL

**Orphaned Account Flag (Column U):**
- Rule 1: If "YES*" → Fill: FFC7CE (red)

**Inactive Account Flag (Column V):**
- Rule 1: If "YES*" → Fill: FFEB9C (yellow)

**Compliance Status (Column W):**
- Rule 1: If "✅ Compliant" → Fill: C6EFCE (green)
- Rule 2: If "⚠️ Partial" → Fill: FFEB9C (yellow)
- Rule 3: If "❌ Non-Compliant" → Fill: FFC7CE (red)
- Rule 4: If "N/A" → Fill: D3D3D3 (gray)

### Notes on Data Import

**From Active Directory (PowerShell):**
```powershell
Get-ADUser -Filter * -Properties * | 
Select-Object SamAccountName, GivenName, Surname, EmailAddress, 
              Enabled, whenCreated, lastLogonTimestamp, Department, 
              Manager, EmployeeID, EmployeeType |
Export-Csv -Path "AD_Users_Export.csv" -NoTypeInformation
```

**From Azure AD (PowerShell):**
```powershell
Connect-AzureAD
Get-AzureADUser -All $true | 
Select-Object UserPrincipalName, DisplayName, Mail, AccountEnabled, 
              CreatedDateTime, RefreshTokensValidFromDateTime, 
              Department, JobTitle, CompanyName |
Export-Csv -Path "AzureAD_Users_Export.csv" -NoTypeInformation
```

**From HR System:**
- Export should include: Employee ID, First Name, Last Name, Email, Department, Manager, Hire Date, Termination Date, Employment Status, Employee Type
- Use VLOOKUP or Power Query to merge HR data into user inventory based on Email or Employee ID

---

## Sheet 3: Provisioning_Timeliness_Analysis

### Purpose
Assess provisioning compliance for new hires - how quickly are accounts created after hire date?

### Header Section (Rows 1-3)
**Row 1:** "PROVISIONING TIMELINESS ANALYSIS"  
**Row 2:** "New hire account provisioning compliance assessment"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | User ID | Text | Link to User Inventory | **LOOKUP** from Sheet 2 (filter: hired in assessment period) | None |
| B | Full Name | Text | User's name | **LOOKUP** from Sheet 2 | None |
| C | User Type | Text | Employee or Contractor | **LOOKUP** from Sheet 2 | None |
| D | Hire Date | Date | From HR system | **LOOKUP** from Sheet 2, Column J | None |
| E | Account Created Date | Date | From identity system | **LOOKUP** from Sheet 2, Column M | None |
| F | Provisioning Delay (Days) | Calculated | Account Created - Hire Date | **FORMULA:** `=E-D` | **CF:** Green if ≤0, Yellow if 1-5, Red if >5 |
| G | Target SLA (Days) | Static | Policy requirement | **VALUE:** 0 (access ready by start date) | None |
| H | SLA Met? | Calculated | Did we meet SLA? | **FORMULA:** `=IF(F<=G, "✅ Yes", "❌ No")` | **CF:** Green if Yes, Red if No |
| I | Compliance Status | Calculated | On-Time / Late / Very Late | **FORMULA:** `=IF(F<=0, "✅ On-Time", IF(F<=5, "⚠️ Late", "❌ Very Late"))` | **CF:** Green/Yellow/Red |
| J | Delay Reason | Dropdown | Why was provisioning late? | Dropdown: HR Notification Delay, IAM Team Backlog, Technical Issue, Manager Approval Delay, Other | None |
| K | Notes | Text | Additional context | **USER INPUT** | None |

### Filter Criteria for This Sheet
- **Include:** Users with Hire Date in assessment period (e.g., Q1 2026)
- **Exclude:** Service accounts (no hire date), users hired before assessment period

### Summary Metrics (Top of Sheet, Rows 1-2, Columns M-S)

| Metric | Formula | Cell |
|--------|---------|------|
| Total New Hires | `=COUNTA(A:A)-1` | M1 |
| On-Time Provisioning | `=COUNTIF(I:I,"✅ On-Time")` | N1 |
| Late Provisioning | `=COUNTIF(I:I,"⚠️ Late")` | O1 |
| Very Late Provisioning | `=COUNTIF(I:I,"❌ Very Late")` | P1 |
| Provisioning Compliance Rate | `=N1/M1` (format as percentage) | Q1 |
| Average Delay (Days) | `=AVERAGE(F:F)` | R1 |
| Maximum Delay (Days) | `=MAX(F:F)` | S1 |

### Conditional Formatting Rules

**Provisioning Delay (Column F):**
- Rule 1: If ≤0 → Fill: C6EFCE (green)
- Rule 2: If 1-5 → Fill: FFEB9C (yellow)
- Rule 3: If >5 → Fill: FFC7CE (red)

**SLA Met (Column H):**
- Rule 1: If "✅ Yes" → Fill: C6EFCE (green)
- Rule 2: If "❌ No" → Fill: FFC7CE (red)

**Compliance Status (Column I):**
- Rule 1: If "✅ On-Time" → Fill: C6EFCE (green)
- Rule 2: If "⚠️ Late" → Fill: FFEB9C (yellow)
- Rule 3: If "❌ Very Late" → Fill: FFC7CE (red)

### Data Validation (Dropdowns)

**Delay Reason (Column J):**
- List: HR Notification Delay, IAM Team Backlog, Technical Issue, Manager Approval Delay, Weekend/Holiday, Other

---

## Sheet 4: Deprovisioning_Timeliness_Analysis

### Purpose
Assess deprovisioning compliance for terminated users - how quickly are accounts disabled after termination?

### Header Section (Rows 1-3)
**Row 1:** "DEPROVISIONING TIMELINESS ANALYSIS"  
**Row 2:** "Terminated user account deprovisioning compliance assessment"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | User ID | Text | Link to User Inventory | **LOOKUP** from Sheet 2 (filter: terminated in assessment period) | None |
| B | Full Name | Text | User's name | **LOOKUP** from Sheet 2 | None |
| C | User Type | Text | Employee or Contractor | **LOOKUP** from Sheet 2 | None |
| D | Termination Date | Date | From HR system | **LOOKUP** from Sheet 2, Column K | None |
| E | Account Disabled Date | Date | When was account disabled? | **USER INPUT** from audit logs OR **LOOKUP** if available | None |
| F | Account Current Status | Text | Is account still active? | **LOOKUP** from Sheet 2, Column D | **CF:** RED if Active (critical issue) |
| G | Deprovisioning Delay (Days) | Calculated | Disabled Date - Termination Date | **FORMULA:** `=IF(F="Active", TODAY()-D, E-D)` | **CF:** Green if 0, Yellow if 1-7, Red if 8-30, DARK RED if >30 |
| H | Target SLA (Days) | Static | Policy requirement | **VALUE:** 0 (same day) | None |
| I | SLA Met? | Calculated | Did we meet SLA? | **FORMULA:** `=IF(G<=H, "✅ Yes", "❌ No")` | **CF:** Green if Yes, Red if No |
| J | Compliance Status | Calculated | On-Time / Late / Very Late / CRITICAL | **FORMULA:** `=IF(F="Active", "🚨 CRITICAL - Still Active", IF(G=0, "✅ On-Time", IF(G<=7, "⚠️ Late", IF(G<=30, "❌ Very Late", "🚨 CRITICAL"))))` | **CF:** Green/Yellow/Red/Dark Red |
| K | Termination Type | Dropdown | Cause of termination | Dropdown: Voluntary Resignation, Termination for Cause, Contract End, Other | None |
| L | Delay Reason | Dropdown | Why was deprovisioning late? | Dropdown: HR Notification Failure, Weekend/Holiday, IAM Team Backlog, Multi-System Complexity, Manager Delay Request, Other | None |
| M | All Systems Disabled? | Dropdown | Was user disabled in ALL identity systems? | Dropdown: Yes - All Systems, No - Partial (specify in notes), Unknown | **CF:** Red if No |
| N | Notes | Text | Additional context | **USER INPUT** | None |

### Filter Criteria for This Sheet
- **Include:** Users with Termination Date in assessment period (e.g., Q1 2026)
- **Exclude:** Active employees (no termination date)

### Summary Metrics (Top of Sheet, Rows 1-2, Columns P-W)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Terminations | `=COUNTA(A:A)-1` | P1 |
| On-Time Deprovisioning | `=COUNTIF(J:J,"✅ On-Time")` | Q1 |
| Late Deprovisioning | `=COUNTIF(J:J,"⚠️ Late")` | R1 |
| Very Late Deprovisioning | `=COUNTIF(J:J,"❌ Very Late")` | S1 |
| CRITICAL Deprovisioning | `=COUNTIF(J:J,"🚨 CRITICAL*")` | T1 |
| Deprovisioning Compliance Rate | `=Q1/P1` (format as percentage) | U1 |
| Average Delay (Days) | `=AVERAGE(G:G)` | V1 |
| Maximum Delay (Days) | `=MAX(G:G)` | W1 |

### Conditional Formatting Rules

**Account Current Status (Column F):**
- Rule 1: If "Active" → Fill: FF0000 (dark red) - CRITICAL SECURITY ISSUE

**Deprovisioning Delay (Column G):**
- Rule 1: If 0 → Fill: C6EFCE (green)
- Rule 2: If 1-7 → Fill: FFEB9C (yellow)
- Rule 3: If 8-30 → Fill: FFC7CE (red)
- Rule 4: If >30 → Fill: FF0000 (dark red) - CRITICAL

**SLA Met (Column I):**
- Rule 1: If "✅ Yes" → Fill: C6EFCE (green)
- Rule 2: If "❌ No" → Fill: FFC7CE (red)

**Compliance Status (Column J):**
- Rule 1: If "✅ On-Time" → Fill: C6EFCE (green)
- Rule 2: If "⚠️ Late" → Fill: FFEB9C (yellow)
- Rule 3: If "❌ Very Late" → Fill: FFC7CE (red)
- Rule 4: If "🚨 CRITICAL" → Fill: FF0000 (dark red)

**All Systems Disabled (Column M):**
- Rule 1: If "No - Partial" → Fill: FFC7CE (red) - user still active in some systems

### Data Validation (Dropdowns)

**Termination Type (Column K):**
- List: Voluntary Resignation, Termination for Cause, Contract End, Layoff, Retirement, Other

**Delay Reason (Column L):**
- List: HR Notification Failure, Weekend/Holiday, IAM Team Backlog, Multi-System Complexity, Manager Delay Request, Technical Issue, Other

**All Systems Disabled (Column M):**
- List: Yes - All Systems, No - Partial (specify in notes), Unknown

---

## Sheet 5: Orphaned_Account_Detection

### Purpose
Identify accounts without valid business owner (former employees, contractors whose contracts ended, etc.)

### Header Section (Rows 1-3)
**Row 1:** "ORPHANED ACCOUNT DETECTION & REMEDIATION"  
**Row 2:** "Accounts without valid business owner requiring investigation and cleanup"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | User ID | Text | Link to User Inventory | **LOOKUP** from Sheet 2 (filter: Orphaned Account Flag = YES) | None |
| B | Full Name | Text | User's name | **LOOKUP** from Sheet 2 | None |
| C | Email Address | Text | Email from identity system | **LOOKUP** from Sheet 2 | None |
| D | Account Status | Text | Active or Disabled | **LOOKUP** from Sheet 2, Column D | **CF:** Red if Active |
| E | User Type | Text | What type was this account? | **LOOKUP** from Sheet 2, Column E | None |
| F | Account Created Date | Date | When was account created? | **LOOKUP** from Sheet 2, Column M | None |
| G | Last Login Date | Date | Last authentication | **LOOKUP** from Sheet 2, Column N | None |
| H | Days Since Last Login | Calculated | Today - Last Login | **LOOKUP** from Sheet 2, Column Q | **CF:** Red if >90 |
| I | Account Source | Text | Which identity system | **LOOKUP** from Sheet 2, Column O | None |
| J | Orphaned Reason | Dropdown | Why is this orphaned? | Dropdown: Former Employee (not in HR), Contractor Ended, No HR Record, Service Account (Unknown Owner), Other | None |
| K | Investigation Status | Dropdown | Investigation progress | Dropdown: Not Started, In Progress, Owner Identified, Confirmed Orphaned, False Positive | **CF:** Yellow if In Progress, Green if Owner Identified |
| L | Investigation Notes | Text | What did we find? | **USER INPUT** | None |
| M | Privileged Access? | Dropdown | Does this account have admin/elevated access? | Dropdown: Yes - Admin/Root, Yes - Elevated, No - Standard, Unknown | **CF:** DARK RED if Yes AND Active |
| N | Remediation Action | Dropdown | What action to take? | Dropdown: Disable Immediately, Delete After 30 Days, Re-Assign Owner, Retain (with justification), Under Review | **CF:** Red if Active account without action |
| O | Remediation Owner | Text | Who is responsible? | **USER INPUT** | None |
| P | Target Remediation Date | Date | When will this be resolved? | **USER INPUT** | **CF:** Red if past due |
| Q | Remediation Status | Dropdown | Progress | Dropdown: Open, In Progress, Completed, Closed | **CF:** Green if Completed/Closed |
| R | Remediation Notes | Text | What was done? | **USER INPUT** | None |

### Filter Criteria for This Sheet
- **Include:** Users with Orphaned Account Flag = "YES*" from Sheet 2
- **Automatic Detection Logic (from Sheet 2):**
  - User in identity system NOT in HR system (Employment Status = "Unknown")
  - Terminated user still active >90 days after termination
  - Contractor past contract end date

### Summary Metrics (Top of Sheet, Rows 1-2, Columns T-Z)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Orphaned Accounts | `=COUNTA(A:A)-1` | T1 |
| Active Orphaned Accounts | `=COUNTIF(D:D,"Active")` | U1 |
| Privileged Orphaned Accounts | `=COUNTIF(M:M,"Yes*")` | V1 |
| Remediation Completed | `=COUNTIF(Q:Q,"Completed")+COUNTIF(Q:Q,"Closed")` | W1 |
| Remediation In Progress | `=COUNTIF(Q:Q,"In Progress")` | X1 |
| Remediation Outstanding | `=COUNTIF(Q:Q,"Open")` | Y1 |
| Remediation Rate | `=W1/T1` (format as percentage) | Z1 |

### Conditional Formatting Rules

**Account Status (Column D):**
- Rule 1: If "Active" → Fill: FFC7CE (red) - orphaned account should be disabled

**Days Since Last Login (Column H):**
- Rule 1: If >90 → Fill: FFC7CE (red)

**Investigation Status (Column K):**
- Rule 1: If "In Progress" → Fill: FFEB9C (yellow)
- Rule 2: If "Owner Identified" → Fill: C6EFCE (green)
- Rule 3: If "Confirmed Orphaned" → Fill: FFC7CE (red)

**Privileged Access (Column M):**
- Rule 1: If "Yes*" AND Account Status = "Active" → Fill: FF0000 (dark red) - CRITICAL

**Remediation Action (Column N):**
- Rule 1: If BLANK AND Account Status = "Active" → Fill: FFC7CE (red) - no action assigned

**Target Remediation Date (Column P):**
- Rule 1: If < TODAY() AND Remediation Status ≠ "Completed" → Fill: FFC7CE (red) - overdue

**Remediation Status (Column Q):**
- Rule 1: If "Completed" OR "Closed" → Fill: C6EFCE (green)
- Rule 2: If "In Progress" → Fill: FFEB9C (yellow)
- Rule 3: If "Open" → Fill: FFC7CE (red)

### Data Validation (Dropdowns)

**Orphaned Reason (Column J):**
- List: Former Employee (not in HR), Contractor Ended, No HR Record, Service Account (Unknown Owner), Vendor (No Sponsor), Other

**Investigation Status (Column K):**
- List: Not Started, In Progress, Owner Identified, Confirmed Orphaned, False Positive

**Privileged Access (Column M):**
- List: Yes - Admin/Root, Yes - Elevated, No - Standard, Unknown

**Remediation Action (Column N):**
- List: Disable Immediately, Delete After 30 Days, Re-Assign Owner, Retain (with justification), Under Review

**Remediation Status (Column Q):**
- List: Open, In Progress, Completed, Closed

---

## Sheet 6: Inactive_Account_Detection

### Purpose
Identify accounts with no login activity >90 days, categorize as legitimate or questionable.

### Header Section (Rows 1-3)
**Row 1:** "INACTIVE ACCOUNT DETECTION & REVIEW"  
**Row 2:** "Accounts with no login activity >90 days requiring justification or remediation"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | User ID | Text | Link to User Inventory | **LOOKUP** from Sheet 2 (filter: Inactive Account Flag = YES) | None |
| B | Full Name | Text | User's name | **LOOKUP** from Sheet 2 | None |
| C | Email Address | Text | Email | **LOOKUP** from Sheet 2 | None |
| D | Account Status | Text | Active or Disabled | **LOOKUP** from Sheet 2, Column D | None |
| E | User Type | Text | Employee, Contractor, etc. | **LOOKUP** from Sheet 2, Column E | None |
| F | Account Created Date | Date | When account created | **LOOKUP** from Sheet 2, Column M | None |
| G | Last Login Date | Date | Last successful login | **LOOKUP** from Sheet 2, Column N | **CF:** Red if blank (never logged in) |
| H | Days Since Last Login | Calculated | Today - Last Login | **LOOKUP** from Sheet 2, Column Q | **CF:** Red if >180, Yellow if 90-180 |
| I | Never Logged In? | Calculated | Account created but never used? | **FORMULA:** `=IF(G="", "YES - Never Used", "NO")` | **CF:** Red if YES |
| J | Inactive Category | Dropdown | Why is this inactive? | Dropdown: Leave of Absence, Seasonal Worker, Service Account (Periodic Use), Questionable - Verify with Manager, Likely Orphaned, Other | **CF:** Yellow if Questionable, Red if Likely Orphaned |
| K | Justification | Text | Why is this legitimately inactive? | **USER INPUT** (e.g., "Maternity leave until June 2026", "Batch job runs monthly") | **CF:** Red if BLANK and Category = Questionable |
| L | Manager Approval | Dropdown | Did manager approve continued access? | Dropdown: Yes - Approved, No - Remove Access, Pending Review, N/A | **CF:** Red if No |
| M | Review Priority | Calculated | Urgency of review | **FORMULA:** `=IF(H>180, "High", IF(H>90, "Medium", "Low"))` | **CF:** Red if High, Yellow if Medium |
| N | Action Required | Dropdown | What should be done? | Dropdown: No Action (Justified), Disable Account, Manager Review, Delete Account, Under Investigation | **CF:** Red if Disable/Delete |
| O | Action Owner | Text | Who is responsible? | **USER INPUT** | None |
| P | Target Action Date | Date | When will this be resolved? | **USER INPUT** | **CF:** Red if past due |
| Q | Action Status | Dropdown | Progress | Dropdown: Open, In Progress, Completed, Closed | **CF:** Green if Completed/Closed |
| R | Notes | Text | Additional context | **USER INPUT** | None |

### Filter Criteria for This Sheet
- **Include:** Users with Inactive Account Flag = "YES*" from Sheet 2
- **Automatic Detection Logic (from Sheet 2):**
  - Account Status = "Active" AND Days Since Last Login > 90
  - OR Last Login Date = blank (never logged in)

### Summary Metrics (Top of Sheet, Rows 1-2, Columns T-Z)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Inactive Accounts | `=COUNTA(A:A)-1` | T1 |
| Never Logged In | `=COUNTIF(I:I,"YES*")` | U1 |
| Inactive >180 Days | `=COUNTIF(H:H,">180")` | V1 |
| Legitimate Inactive | `=COUNTIF(J:J,"Leave of Absence")+COUNTIF(J:J,"Seasonal Worker")+COUNTIF(J:J,"Service Account*")` | W1 |
| Questionable Inactive | `=COUNTIF(J:J,"Questionable*")+COUNTIF(J:J,"Likely Orphaned")` | X1 |
| Manager Approved | `=COUNTIF(L:L,"Yes - Approved")` | Y1 |
| Require Action | `=COUNTIF(N:N,"Disable Account")+COUNTIF(N:N,"Delete Account")` | Z1 |

### Conditional Formatting Rules

**Last Login Date (Column G):**
- Rule 1: If BLANK → Fill: FFC7CE (red) - never logged in

**Days Since Last Login (Column H):**
- Rule 1: If >180 → Fill: FFC7CE (red)
- Rule 2: If 90-180 → Fill: FFEB9C (yellow)

**Never Logged In (Column I):**
- Rule 1: If "YES*" → Fill: FFC7CE (red)

**Inactive Category (Column J):**
- Rule 1: If "Questionable*" → Fill: FFEB9C (yellow)
- Rule 2: If "Likely Orphaned" → Fill: FFC7CE (red)

**Justification (Column K):**
- Rule 1: If BLANK AND Inactive Category = "Questionable*" → Fill: FFC7CE (red)

**Manager Approval (Column L):**
- Rule 1: If "No - Remove Access" → Fill: FFC7CE (red)
- Rule 2: If "Yes - Approved" → Fill: C6EFCE (green)

**Review Priority (Column M):**
- Rule 1: If "High" → Fill: FFC7CE (red)
- Rule 2: If "Medium" → Fill: FFEB9C (yellow)
- Rule 3: If "Low" → Fill: C6EFCE (green)

**Action Required (Column N):**
- Rule 1: If "Disable Account" OR "Delete Account" → Fill: FFC7CE (red)

**Target Action Date (Column P):**
- Rule 1: If < TODAY() AND Action Status ≠ "Completed" → Fill: FFC7CE (red)

**Action Status (Column Q):**
- Rule 1: If "Completed" OR "Closed" → Fill: C6EFCE (green)
- Rule 2: If "In Progress" → Fill: FFEB9C (yellow)
- Rule 3: If "Open" → Fill: FFC7CE (red)

### Data Validation (Dropdowns)

**Inactive Category (Column J):**
- List: Leave of Absence, Seasonal Worker, Service Account (Periodic Use), Questionable - Verify with Manager, Likely Orphaned, Other

**Manager Approval (Column L):**
- List: Yes - Approved, No - Remove Access, Pending Review, N/A

**Action Required (Column N):**
- List: No Action (Justified), Disable Account, Manager Review, Delete Account, Under Investigation

**Action Status (Column Q):**
- List: Open, In Progress, Completed, Closed

---

## Sheet 7: Lifecycle_Compliance_Dashboard

### Purpose
Consolidated lifecycle compliance metrics and overall maturity scoring.

### Header Section (Rows 1-3)
**Row 1:** "IDENTITY LIFECYCLE COMPLIANCE DASHBOARD"  
**Row 2:** "Consolidated metrics from provisioning, deprovisioning, orphaned accounts, and inactive accounts"  
**Row 3:** Section headers

### Dashboard Layout (Rows 5+)

#### Section 1: Overall Compliance Summary (Rows 5-15)

| Metric | Value (Formula) | Target | Status | Cell Reference |
|--------|----------------|--------|--------|----------------|
| **Total Users** | `=Sheet2!AA1` | N/A | N/A | B5 |
| **Active Users** | `=Sheet2!AB1` | N/A | N/A | B6 |
| **Employees** | `=Sheet2!AD1` | N/A | N/A | B7 |
| **Contractors** | `=Sheet2!AE1` | N/A | N/A | B8 |
| **Service Accounts** | `=Sheet2!AF1` | N/A | N/A | B9 |
| **Orphaned Accounts** | `=Sheet2!AG1` | 0 | `=IF(B10=0,"✅",IF(B10<=5,"⚠️","❌"))` | B10 |
| **Inactive Accounts** | `=Sheet2!AH1` | <5% of active | `=IF(B11/B6<0.05,"✅",IF(B11/B6<0.10,"⚠️","❌"))` | B11 |

#### Section 2: Provisioning Compliance (Rows 17-25)

| Metric | Value (Formula) | Target | Status | Cell Reference |
|--------|----------------|--------|--------|----------------|
| **New Hires (Period)** | `=Sheet3!M1` | N/A | N/A | B17 |
| **On-Time Provisioning** | `=Sheet3!N1` | All | N/A | B18 |
| **Late Provisioning** | `=Sheet3!O1` | 0 | N/A | B19 |
| **Very Late Provisioning** | `=Sheet3!P1` | 0 | N/A | B20 |
| **Provisioning Compliance Rate** | `=Sheet3!Q1` (format as %) | ≥85% | `=IF(B21>=0.85,"✅",IF(B21>=0.70,"⚠️","❌"))` | B21 |
| **Average Delay (Days)** | `=Sheet3!R1` | ≤1 | `=IF(B22<=1,"✅",IF(B22<=3,"⚠️","❌"))` | B22 |
| **Maximum Delay (Days)** | `=Sheet3!S1` | ≤3 | `=IF(B23<=3,"✅",IF(B23<=7,"⚠️","❌"))` | B23 |

#### Section 3: Deprovisioning Compliance (Rows 27-35)

| Metric | Value (Formula) | Target | Status | Cell Reference |
|--------|----------------|--------|--------|----------------|
| **Terminations (Period)** | `=Sheet4!P1` | N/A | N/A | B27 |
| **On-Time Deprovisioning** | `=Sheet4!Q1` | All | N/A | B28 |
| **Late Deprovisioning** | `=Sheet4!R1` | 0 | N/A | B29 |
| **Very Late Deprovisioning** | `=Sheet4!S1` | 0 | N/A | B30 |
| **CRITICAL Deprovisioning** | `=Sheet4!T1` | 0 | `=IF(B31=0,"✅","🚨 CRITICAL")` | B31 |
| **Deprovisioning Compliance Rate** | `=Sheet4!U1` (format as %) | ≥90% | `=IF(B32>=0.90,"✅",IF(B32>=0.75,"⚠️","❌"))` | B32 |
| **Average Delay (Days)** | `=Sheet4!V1` | 0 | `=IF(B33=0,"✅",IF(B33<=3,"⚠️","❌"))` | B33 |
| **Maximum Delay (Days)** | `=Sheet4!W1` | ≤1 | `=IF(B34<=1,"✅",IF(B34<=7,"⚠️","❌"))` | B34 |

#### Section 4: Orphaned Account Metrics (Rows 37-43)

| Metric | Value (Formula) | Target | Status | Cell Reference |
|--------|----------------|--------|--------|----------------|
| **Total Orphaned Accounts** | `=Sheet5!T1` | 0 | `=IF(B37=0,"✅",IF(B37<=5,"⚠️","❌"))` | B37 |
| **Active Orphaned Accounts** | `=Sheet5!U1` | 0 | `=IF(B38=0,"✅","❌")` | B38 |
| **Privileged Orphaned Accounts** | `=Sheet5!V1` | 0 | `=IF(B39=0,"✅","🚨 CRITICAL")` | B39 |
| **Remediation Completed** | `=Sheet5!W1` | All | N/A | B40 |
| **Remediation Rate** | `=Sheet5!Z1` (format as %) | 100% | `=IF(B41=1,"✅",IF(B41>=0.80,"⚠️","❌"))` | B41 |

#### Section 5: Inactive Account Metrics (Rows 45-51)

| Metric | Value (Formula) | Target | Status | Cell Reference |
|--------|----------------|--------|--------|----------------|
| **Total Inactive Accounts** | `=Sheet6!T1` | <5% active | `=IF(B45/B6<0.05,"✅",IF(B45/B6<0.10,"⚠️","❌"))` | B45 |
| **Never Logged In** | `=Sheet6!U1` | 0 | `=IF(B46=0,"✅",IF(B46<=3,"⚠️","❌"))` | B46 |
| **Inactive >180 Days** | `=Sheet6!V1` | 0 | `=IF(B47=0,"✅",IF(B47<=5,"⚠️","❌"))` | B47 |
| **Legitimate Inactive** | `=Sheet6!W1` | N/A | N/A | B48 |
| **Questionable Inactive** | `=Sheet6!X1` | 0 | `=IF(B49=0,"✅","⚠️")` | B49 |

#### Section 6: Overall Lifecycle Maturity Score (Rows 53-65)

**Weighted Calculation:**
```
Lifecycle Maturity Score = 
  (Provisioning Compliance × 25%) + 
  (Deprovisioning Compliance × 40%) + 
  ((1 - Orphaned Account %) × 20%) + 
  ((1 - Inactive Account %) × 15%)
```

| Component | Weight | Score | Weighted Score | Cell |
|-----------|--------|-------|----------------|------|
| Provisioning Compliance | 25% | `=B21` | `=B21*0.25` | D54 |
| Deprovisioning Compliance | 40% | `=B32` | `=B32*0.40` | D55 |
| Orphaned Account Score | 20% | `=1-(B37/B5)` | `=(1-(B37/B5))*0.20` | D56 |
| Inactive Account Score | 15% | `=1-(B45/B6)` | `=(1-(B45/B6))*0.15` | D57 |
| **Total Maturity Score** | **100%** | N/A | `=SUM(D54:D57)` | **D58** |

**Benchmark Categories:**

| Score Range | Maturity Level | Description | Cell |
|-------------|----------------|-------------|------|
| 90-100% | ✅ **Excellent** | Best-in-class lifecycle management | B60 |
| 75-89% | ⚠️ **Good** | Strong lifecycle controls, minor improvements needed | B61 |
| 60-74% | ⚠️ **Fair** | Acceptable but significant gaps exist | B62 |
| <60% | ❌ **Poor** | Major lifecycle deficiencies, high security risk | B63 |

**Current Maturity Level:**
```excel
=IF(D58>=0.90, "✅ Excellent", 
  IF(D58>=0.75, "⚠️ Good", 
    IF(D58>=0.60, "⚠️ Fair", "❌ Poor")))
```

### Conditional Formatting Rules

**Status Columns (All sections):**
- Rule 1: If "✅" → Fill: C6EFCE (green)
- Rule 2: If "⚠️" → Fill: FFEB9C (yellow)
- Rule 3: If "❌" → Fill: FFC7CE (red)
- Rule 4: If "🚨 CRITICAL" → Fill: FF0000 (dark red)

**Maturity Score (D58):**
- Rule 1: If ≥0.90 → Fill: C6EFCE (green)
- Rule 2: If 0.75-0.89 → Fill: FFEB9C (yellow)
- Rule 3: If 0.60-0.74 → Fill: FFEB9C (yellow)
- Rule 4: If <0.60 → Fill: FFC7CE (red)

---

## Sheet 8: Gap_Analysis_and_Remediation

### Purpose
Consolidated gap identification and remediation tracking across all lifecycle areas.

### Header Section (Rows 1-3)
**Row 1:** "GAP ANALYSIS & REMEDIATION ROADMAP"  
**Row 2:** "Identify all lifecycle deficiencies and track remediation progress"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | Gap ID | Text | Unique identifier | **USER INPUT** (e.g., GAP-001, GAP-002) | None |
| B | Gap Type | Dropdown | Category of gap | Dropdown: Provisioning Delay, Deprovisioning Delay, Orphaned Account, Inactive Account, Process Issue, Technical Issue, Other | None |
| C | Gap Description | Text | What is the gap? | **USER INPUT** (e.g., "5 terminated users still active >30 days") | None |
| D | Affected Users/Count | Text/Number | How many users affected? | **USER INPUT** or **LOOKUP** from other sheets | None |
| E | Source Sheet | Dropdown | Where was this identified? | Dropdown: Sheet 3 (Provisioning), Sheet 4 (Deprovisioning), Sheet 5 (Orphaned), Sheet 6 (Inactive), Sheet 7 (Dashboard), Other | None |
| F | Risk Level | Dropdown | Severity of gap | Dropdown: Critical, High, Medium, Low | **CF:** Dark Red if Critical, Red if High, Yellow if Medium |
| G | Business Impact | Text | What's the risk/impact? | **USER INPUT** (e.g., "Security risk - ex-employee data access") | None |
| H | Root Cause | Text | Why did this happen? | **USER INPUT** (e.g., "HR termination notification not sent to IT") | None |
| I | Remediation Plan | Text | What action will fix this? | **USER INPUT** (e.g., "Disable accounts immediately, implement automated HR-IT workflow") | None |
| J | Remediation Owner | Text | Who is responsible? | **USER INPUT** (name or role) | **CF:** Yellow if BLANK |
| K | Target Date | Date | When will this be resolved? | **USER INPUT** | **CF:** Red if past due and not completed |
| L | Status | Dropdown | Current progress | Dropdown: Open, In Progress, Blocked, Completed, Closed | **CF:** Green if Completed/Closed, Red if Blocked |
| M | % Complete | Number | Progress percentage | **USER INPUT** (0-100) | **CF:** Data bars (green) |
| N | Budget Required | Dropdown | Does this need budget? | Dropdown: Yes, No, TBD | None |
| O | Estimated Cost | Currency | If yes, how much? | **USER INPUT** (optional) | None |
| P | Progress Notes | Text | Latest updates | **USER INPUT** | None |
| Q | Date Closed | Date | When was gap resolved? | **USER INPUT** | None |

### Pre-Populated Gap Examples (Rows 4+)

Assessment script should auto-populate gaps based on other sheets:

**Auto-Generated Gaps:**
1. **From Sheet 4 (Deprovisioning):** If any users have Compliance Status = "🚨 CRITICAL - Still Active"
   - Gap Type: Deprovisioning Delay
   - Risk Level: Critical
   - Affected Users: [Count from Sheet 4]
   
2. **From Sheet 5 (Orphaned):** If Privileged Orphaned Accounts > 0
   - Gap Type: Orphaned Account
   - Risk Level: Critical
   - Affected Users: [Count from Sheet 5]

3. **From Sheet 3 (Provisioning):** If Provisioning Compliance Rate < 85%
   - Gap Type: Provisioning Delay
   - Risk Level: High
   - Affected Users: [Count of late provisioning]

4. **From Sheet 6 (Inactive):** If Never Logged In > 0
   - Gap Type: Inactive Account
   - Risk Level: Medium
   - Affected Users: [Count from Sheet 6]

### Summary Metrics (Top of Sheet, Rows 1-2, Columns S-X)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Gaps | `=COUNTA(A:A)-1` | S1 |
| Critical Gaps | `=COUNTIF(F:F,"Critical")` | T1 |
| High Gaps | `=COUNTIF(F:F,"High")` | U1 |
| Medium Gaps | `=COUNTIF(F:F,"Medium")` | V1 |
| Low Gaps | `=COUNTIF(F:F,"Low")` | W1 |
| Gaps Closed | `=COUNTIF(L:L,"Closed")+COUNTIF(L:L,"Completed")` | X1 |
| Resolution Rate | `=X1/S1` (format as percentage) | Y1 |

### Conditional Formatting Rules

**Risk Level (Column F):**
- Rule 1: If "Critical" → Fill: FF0000 (dark red)
- Rule 2: If "High" → Fill: FFC7CE (red)
- Rule 3: If "Medium" → Fill: FFEB9C (yellow)
- Rule 4: If "Low" → Fill: C6EFCE (green)

**Remediation Owner (Column J):**
- Rule 1: If BLANK → Fill: FFEB9C (yellow) - no owner assigned

**Target Date (Column K):**
- Rule 1: If < TODAY() AND Status ≠ "Completed" AND Status ≠ "Closed" → Fill: FFC7CE (red)

**Status (Column L):**
- Rule 1: If "Completed" OR "Closed" → Fill: C6EFCE (green)
- Rule 2: If "In Progress" → Fill: FFEB9C (yellow)
- Rule 3: If "Blocked" → Fill: FFC7CE (red)
- Rule 4: If "Open" → Fill: D3D3D3 (gray)

**% Complete (Column M):**
- Data bars: Green gradient (0% = no fill, 100% = full green)

### Data Validation (Dropdowns)

**Gap Type (Column B):**
- List: Provisioning Delay, Deprovisioning Delay, Orphaned Account, Inactive Account, Process Issue, Technical Issue, Documentation Gap, Other

**Source Sheet (Column E):**
- List: Sheet 3 (Provisioning), Sheet 4 (Deprovisioning), Sheet 5 (Orphaned), Sheet 6 (Inactive), Sheet 7 (Dashboard), Multiple Sheets, Other

**Risk Level (Column F):**
- List: Critical, High, Medium, Low

**Status (Column L):**
- List: Open, In Progress, Blocked, Completed, Closed

**Budget Required (Column N):**
- List: Yes, No, TBD

---

## Sheet 9: Evidence_Register

### Purpose
Centralized evidence repository linking to all supporting documentation.

### Header Section (Rows 1-3)
**Row 1:** "EVIDENCE REGISTER"  
**Row 2:** "Document all evidence supporting this assessment for audit traceability"  
**Row 3:** Column headers

### Column Definitions (Rows 3-103, 100 rows for evidence)

| Column | Header | Type | Description | Conditional Formatting |
|--------|--------|------|-------------|----------------------|
| A | Evidence ID | Text | Unique identifier (EVID-001, EVID-002, etc.) | None |
| B | Evidence Type | Dropdown | Category of evidence | None |
| C | Description | Text | What is this evidence? | None |
| D | Related Sheet/Row | Text | Where is this evidence referenced? | None |
| E | Location/Path | Text | File path or URL | None |
| F | Date Collected | Date | When was evidence captured? | **CF:** Red if >90 days old |
| G | Collected By | Text | Who gathered this evidence? | None |
| H | Verification Status | Dropdown | Has evidence been verified? | **CF:** Green if Verified, Yellow if Pending |

### Data Validation (Dropdowns)

**Evidence Type (Column B):**
- List: Identity System Export, HR Data Export, Login Logs, Screenshot, Audit Log, Policy Document, Email/Approval, Meeting Notes, Configuration File, Report, Contract/License, Other

**Verification Status (Column H):**
- List: Verified, Pending Verification, Not Verified, N/A

### Conditional Formatting Rules

**Date Collected (Column F):**
- Rule 1: If (TODAY() - F) > 90 → Fill: FFC7CE (red) - evidence may be stale

**Verification Status (Column H):**
- Rule 1: If "Verified" → Fill: C6EFCE (green)
- Rule 2: If "Pending Verification" → Fill: FFEB9C (yellow)
- Rule 3: If "Not Verified" → Fill: FFC7CE (red)

### Pre-Populated Evidence Examples

**Core Evidence (Auto-populated by assessment script):**
1. EVID-001 | Identity System Export | AD Users Export | Sheet 2 (User Inventory) | [path] | [date] | [user] | Verified
2. EVID-002 | Identity System Export | Azure AD Users Export | Sheet 2 (User Inventory) | [path] | [date] | [user] | Verified
3. EVID-003 | HR Data Export | Employee List with Hire/Term Dates | Sheet 2 (User Inventory) | [path] | [date] | [user] | Verified
4. EVID-004 | Login Logs | Last 90 Days Login Activity | Sheet 2, 6 (Inactive Accounts) | [path] | [date] | [user] | Verified
5. EVID-005 | Screenshot | AD User Count Screenshot | Sheet 2 | [path] | [date] | [user] | Verified
6. EVID-006 | Policy Document | ISMS-POL-A.5.15-16-18 | All Sheets | [path] | [date] | [user] | Verified

---

## Sheet 10: Approval_and_Sign_Off

### Purpose
Formal three-level approval workflow for completed assessment.

### Assessment Summary Section (Rows 3-12)
```
Assessment Document:              ISMS-IMP-A.5.15-16-18.S1 - User Inventory & Lifecycle Compliance
Assessment Period:                [USER INPUT - e.g., Q1 2026]
Total Users Assessed:             [Formula: =Sheet2!AA1]
Total Active Users:               [Formula: =Sheet2!AB1]
Orphaned Accounts Detected:       [Formula: =Sheet2!AG1]
Inactive Accounts Detected:       [Formula: =Sheet2!AH1]
Provisioning Compliance Rate:     [Formula: =Sheet7!B21]
Deprovisioning Compliance Rate:   [Formula: =Sheet7!B32]
Overall Lifecycle Maturity Score: [Formula: =Sheet7!D58]
Critical Gaps:                    [Formula: =Sheet8!T1]
Assessment Status:                [Dropdown: Draft, Final, Requires Remediation, Re-assessment Required]
```

### Assessment Completed By (Rows 14-22)
```
Name:                [USER INPUT]
Role/Title:          [USER INPUT]
Department:          [USER INPUT - e.g., IAM Team, IT Operations]
Email:               [USER INPUT]
Date Completed:      [USER INPUT - date picker]
Signature/Initials:  [USER INPUT]
Completion Notes:    [Text area - merged cells, 3 rows]
```

### Reviewed By - IAM Team Lead (Rows 24-32)
```
Name:                     [USER INPUT]
Role/Title:               IAM Team Lead
Date Reviewed:            [USER INPUT - date picker]
Review Notes:             [Text area - merged cells, 3 rows]
Technical Accuracy:       [Dropdown: Verified, Issues Found (see notes), Not Reviewed]
Data Quality:             [Dropdown: High Quality, Acceptable, Issues Found (see notes)]
Recommendation:           [Dropdown: Approve, Approve with Conditions, Reject - Require Rework]
Conditions/Comments:      [Text area - merged cells, 2 rows]
```

### Approved By - CISO or Security Manager (Rows 34-42)
```
Name:                     [USER INPUT]
Role/Title:               CISO / Security Manager
Date Approved:            [USER INPUT - date picker]
Approval Decision:        [Dropdown: Approved, Approved with Conditions, Rejected]
Risk Acceptance:          [Text area - "I accept residual risks documented in Gap Analysis (Sheet 8)"]
Conditions/Comments:      [Text area - merged cells, 3 rows]
Final Approval:           [Checkbox or Dropdown: Yes - Final, No - See conditions]
```

### Next Review Details (Rows 44-50)
```
Next Review Type:         [Dropdown: Monthly Update, Quarterly Comprehensive, Annual Strategic]
Next Review Date:         [Date - auto-calculate based on review type: Monthly = +1 month, Quarterly = +3 months]
Review Responsible:       [USER INPUT - typically IAM Team Lead]
Special Considerations:   [Text area - merged cells, 2 rows]
Continuous Improvement:   [Text area - "What should we improve for next assessment cycle?"]
```

### Data Validation (Dropdowns)

**Assessment Status:**
- List: Draft, Final, Requires Remediation, Re-assessment Required

**Technical Accuracy:**
- List: Verified, Issues Found (see notes), Not Reviewed

**Data Quality:**
- List: High Quality, Acceptable, Issues Found (see notes)

**Recommendation (IAM Team Lead):**
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
- **Main Header:** Font: Calibri 14pt bold white, Fill: 003366 (dark blue), Alignment: centered/wrapped, Height: 40px
- **Subheader:** Font: Calibri 11pt bold white, Fill: 4472C4 (blue), Alignment: centered/wrapped
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (gray), Alignment: centered/wrapped, Border: thin all sides
- **Section Header (within sheet):** Font: Calibri 12pt bold, Fill: E7E6E6 (light gray), Alignment: left, Border: medium bottom

### Input Cell Styles
- **Fill:** FFFFCC (light yellow) - indicates user should fill in
- **Alignment:** Left for text, center for dropdowns, right for numbers
- **Border:** Thin black on all sides
- **Protection:** Unlocked (allow editing)

### Formula/Calculated Cell Styles
- **Fill:** White (FFFFFF) or light gray (F2F2F2) for read-only calculated fields
- **Alignment:** Right for numbers, left for text
- **Border:** Thin gray on all sides
- **Protection:** Locked (prevent editing)

### Status Fill Colors (Conditional Formatting)
- **✅ Compliant / On-Time / Verified:** C6EFCE (green)
- **⚠️ Partial / Late / Pending:** FFEB9C (yellow)
- **❌ Non-Compliant / Very Late / Issues:** FFC7CE (red)
- **🚨 CRITICAL:** FF0000 (dark red) - for critical security issues
- **ℹ️ Under Investigation / In Progress:** B4C7E7 (blue)
- **N/A / Not Applicable:** D3D3D3 (gray)

### Data Bars (Progress Indicators)
- **Color:** Green (63BE7B)
- **Direction:** Left-to-right
- **Min Value:** 0
- **Max Value:** 100
- **Show Bar Only:** No (show value and bar)

---

## Freeze Panes

Apply freeze panes for easier navigation:

- **Sheet 2 (User Inventory):** Freeze at A4 (column headers visible when scrolling down)
- **Sheet 3 (Provisioning):** Freeze at A4
- **Sheet 4 (Deprovisioning):** Freeze at A4
- **Sheet 5 (Orphaned):** Freeze at A4
- **Sheet 6 (Inactive):** Freeze at A4
- **Sheet 7 (Dashboard):** Freeze at A5 (section headers visible)
- **Sheet 8 (Gap Analysis):** Freeze at A4
- **Sheet 9 (Evidence):** Freeze at A4
- **Sheet 10 (Approval):** Freeze at A3

---

## File Naming Convention

**Format:** `ISMS-IMP-A.5.15-16-18.S1_User_Inventory_Lifecycle_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.5.15-16-18.S1_User_Inventory_Lifecycle_20260122.xlsx`

**Version Control:**
- Date in filename indicates assessment date or data snapshot date
- Monthly assessments → New file each month
- Quarterly comprehensive → Major version in filename (e.g., `..._Q1-2026.xlsx`)

---

## Monthly Review Cycle

1. **Update User Inventory (Sheet 2):**
   - Re-export users from all identity systems
   - Re-export HR data
   - Update last login dates
   - Recalculate all formulas

2. **Refresh Provisioning Analysis (Sheet 3):**
   - Filter to current month new hires
   - Calculate current month compliance

3. **Refresh Deprovisioning Analysis (Sheet 4):**
   - Filter to current month terminations
   - Calculate current month compliance
   - **CRITICAL:** Check for any terminated users still active >30 days

4. **Update Orphaned Accounts (Sheet 5):**
   - Run cross-reference (identity systems vs. HR)
   - Update remediation status

5. **Update Inactive Accounts (Sheet 6):**
   - Recalculate days since last login
   - Update inactive account list

6. **Refresh Dashboard (Sheet 7):**
   - All metrics auto-update from linked sheets
   - Review maturity score trend

7. **Update Gap Analysis (Sheet 8):**
   - Close resolved gaps
   - Add new gaps identified in current month
   - Update remediation progress

8. **Add New Evidence (Sheet 9):**
   - Document current month exports and data sources

9. **Update Approval (Sheet 10):**
   - IAM Team Lead monthly review
   - CISO sign-off if significant changes or critical gaps

---

## Quarterly Comprehensive Review Cycle

1. **Deep Dive Analysis:**
   - Analyze trends over last 3 months
   - Identify systemic issues (e.g., provisioning always late by 2 days → process issue)
   - Root cause analysis for recurring gaps

2. **Orphaned Account Cleanup Campaign:**
   - Intensive investigation of all orphaned accounts
   - Target: Close 100% of orphaned accounts identified >90 days ago

3. **Process Improvement:**
   - Review provisioning/deprovisioning procedures
   - Identify automation opportunities
   - Update documentation if processes changed

4. **Benchmark Review:**
   - Compare Q1 vs. Q2 vs. Q3 vs. Q4
   - Are we improving? (maturity score trend)
   - What changed? (staffing, technology, process)

5. **CISO Review and Approval:**
   - Present quarterly summary to CISO
   - Review critical gaps and remediation plans
   - Allocate budget/resources for improvements

---

## Integration Points

### Related Assessments (Other A.5.15-16-18 Workbooks)

**A.5.15-16-18.2 - Access Rights Matrix Assessment:**
- **Input FROM this workbook:** User inventory (Sheet 2) provides baseline user list
- **Usage:** Access rights assessment maps users (from .1) to systems/applications to access levels

**A.5.15-16-18.3 - Access Review Results Assessment:**
- **Input FROM this workbook:** Active user list (Sheet 2) defines review scope
- **Usage:** Access review verifies which users' access was reviewed and confirmed/removed

**A.5.15-16-18.4 - Role Definition & SoD Compliance Assessment:**
- **Input FROM this workbook:** User list (Sheet 2) for role assignment verification
- **Usage:** Role compliance assessment verifies users are assigned to appropriate roles, detects SoD violations

**A.5.15-16-18.5 - IAM Governance Compliance Dashboard:**
- **Input FROM this workbook:** Lifecycle compliance metrics (Sheet 7)
- **Usage:** Dashboard consolidates lifecycle metrics with access rights, reviews, and role compliance into executive summary

### Related ISMS Documents

- **ISMS-POL-A.5.15-16-18:** Identity & Access Management Policy (defines requirements being assessed)
- **Risk Register:** Link orphaned/inactive account gaps to IAM risk items
- **Incident Management:** Link account compromise incidents to lifecycle gaps
- **Change Management:** Link identity system changes to assessment updates
- **Asset Inventory:** Ensure identity systems are tracked as assets

### HR System Integration

- **Joiner Event Triggers:** HR system notifies IAM Team of new hires → provisioning
- **Leaver Event Triggers:** HR system notifies IAM Team of terminations → deprovisioning
- **Mover Event Triggers:** HR system notifies IAM Team of role changes → access review

### Audit Trail

- All evidence referenced in Evidence Register (Sheet 9)
- Gap remediation linked to project management system
- Lifecycle SLA compliance tracked monthly for trend analysis
- Approval sign-off (Sheet 10) maintains complete audit trail for certification

---

**END OF TECHNICAL SPECIFICATION**

*"The first principle is that you must not fool yourself – and you are the easiest person to fool."*  
– Richard Feynman

**ISMS Maturity Indicator:** If you can honestly populate this assessment workbook without inflating compliance scores or hiding critical gaps, you understand that lifecycle compliance is not about documentation – it's about systematically managing the complete identity lifecycle to prevent unauthorized access. ✅

