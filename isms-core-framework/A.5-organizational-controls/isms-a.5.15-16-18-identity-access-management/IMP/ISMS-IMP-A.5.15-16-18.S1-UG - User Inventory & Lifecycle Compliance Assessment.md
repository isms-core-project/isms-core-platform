<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.15-16-18.S1-UG:framework:UG:a.5.15-16-18 -->
**ISMS-IMP-A.5.15-16-18.S1-UG - User Inventory & Lifecycle Compliance Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S1-UG |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.15-16-18.S1-TG.

---

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

This assessment is **completely technology-agnostic and vendor-independent**. You document YOUR identity systems (Active Directory, Microsoft Entra ID, Okta, Google Workspace, LDAP, custom systems - whatever you use), and assess lifecycle compliance against generic policy requirements.

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

- Understanding of identity systems (AD, Entra ID, Okta, LDAP)
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

- Administrator access to ALL identity systems (AD, Entra ID, Okta, Google Workspace, LDAP, custom)
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
- **Identity system admin tools** (AD Users and Computers, Entra Admin Center, Okta Admin Console, etc.)
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
3. Identify ALL identity systems in your environment (AD, Entra ID, Okta, etc.)
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

**For Microsoft Entra ID (formerly Azure AD):**
```powershell
# Microsoft Entra ID export using Microsoft Graph PowerShell SDK
Connect-MgGraph -Scopes "User.Read.All"
Get-MgUser -All |
Select-Object UserPrincipalName, DisplayName, Mail, AccountEnabled,
              CreatedDateTime, SignInActivity,
              Department, JobTitle, CompanyName |
Export-Csv -Path "EntraID_Users_Export.csv" -NoTypeInformation
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

- ✓ All identity systems queried (AD, Entra ID, Okta, LDAP, custom)
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
   - Account Source (AD, Entra ID, Okta, etc.)

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
   - Multi-system complexity (disabled in AD but not Entra ID/Okta)
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

   - Users in identity systems (AD, Entra ID, Okta) NOT in HR system = potential orphaned accounts
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

   - Identity system exports (AD, Entra ID, Okta, etc.)
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
   │   ├── EntraID_Users_Export_2026-01-22.csv
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

- Identity system exports (AD, Entra ID, Okta, etc.) - CSV/Excel
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

❌ **Mistake:** Only exporting users from Active Directory, missing Entra ID cloud-only accounts or Okta SSO accounts

✅ **Fix:** Export from ALL identity systems (AD, Entra ID, Okta, Google Workspace, LDAP, custom systems) and consolidate

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

❌ **Mistake:** User has account in both AD and Entra ID, only checking deprovisioning in AD (still active in Entra ID)

✅ **Fix:** For deprovisioning compliance, verify user disabled in ALL identity systems they have accounts in. Multi-system environments require comprehensive deprovisioning.

---

## Quality Checklist

Before submitting for approval, verify:

### User Inventory (Sheet 1)

- [ ] All identity systems queried (AD, Entra ID, Okta, Google Workspace, LDAP, custom)
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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
