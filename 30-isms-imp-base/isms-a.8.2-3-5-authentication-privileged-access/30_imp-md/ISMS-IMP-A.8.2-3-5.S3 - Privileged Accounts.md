# ISMS-IMP-A.8.2-3-5.3 - Privileged Account Inventory
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.2-3-5.S3 |
| **Version** | 1.0 |
| **Assessment Area** | Privileged Account Inventory & Admin Tiering |
| **Related Policy** | ISMS-POL-A.8.2-3-5 (Section 2.2 - Privileged Access Rights) |
| **Purpose** | Comprehensive inventory of all privileged accounts with Admin Tiering Model classification, PAM coverage tracking, and tier isolation verification to prevent lateral movement and credential theft |
| **Target Audience** | Security Team, IT Operations, System Owners, IAM Team, CISO |
| **Assessment Type** | Privileged Account Inventory & Configuration Analysis |
| **Review Cycle** | Monthly inventory updates, Quarterly comprehensive review |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial assessment specification for privileged account inventory with Admin Tiering Model | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Understanding Admin Tiering Model (CRITICAL)
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Column Definitions
  - Formulas & Calculations
  - Python Script Integration

---

# PART I: USER COMPLETION GUIDE

## 1. Assessment Overview

### 1.1 Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.2-3-5.3 - Privileged Account Inventory

**What This Assessment Does:**
- Inventories ALL privileged accounts (named, shared, service, break-glass)
- Classifies privileged accounts by Admin Tier (Tier 0, Tier 1, Tier 2)
- Tracks PAM (Privileged Access Management) coverage per account
- Verifies tier isolation compliance (Tier 0 accounts never log into Tier 1/2 systems)
- Identifies privileged accounts without MFA (critical security gap)
- Documents privileged account ownership and business justification
- Tracks privileged credential rotation schedules

**What This Assessment Does NOT Do:**
- Track individual user MFA enrollment (see IMP.2 - MFA Coverage)
- Inventory authentication mechanisms (see IMP.1 - Authentication Inventory)
- Monitor real-time privileged access activity (see IMP.4 - Privileged Monitoring)

**Primary ISO 27001 Control:** A.8.2 - Privileged Access Rights

**Related Controls:**
- A.8.5 - Secure Authentication (MFA for privileged accounts)
- A.5.18 - Access Rights (privileged access as special category)
- A.8.16 - Monitoring Activities (privileged access monitoring)

**Why Admin Tiering Matters:**
The Admin Tiering Model (Tier 0/1/2) is the MOST CRITICAL architectural control for preventing lateral movement in case of credential compromise. Without tier isolation, an attacker who compromises a single workstation can steal Domain Admin credentials and compromise the entire Active Directory domain. This assessment ensures tier isolation is properly implemented.

### 1.2 When to Use This Assessment

**Use this assessment when:**
- Establishing privileged access inventory baseline (first certification)
- Monthly privileged account updates (new admins, role changes, leavers)
- Quarterly privileged access reviews (access justification, owner validation)
- Preparing for ISO 27001 certification audits
- Investigating privileged access security incidents
- Deploying PAM solutions (track PAM coverage)
- Implementing Admin Tiering Model (tier classification and isolation)

**Assessment Frequency:**
- **Monthly**: Privileged account inventory updates, new admin accounts, leaver processing
- **Quarterly**: Comprehensive review, access justification validation, tier isolation verification
- **Annual**: Deep assessment, penetration testing (privilege escalation), full compliance validation

### 1.3 Who Completes This Assessment

**Primary Responsibility:** Security Team (privileged access security lead) + IAM Team

**Supporting Roles:**
- **IT Operations**: Identify system administrators, provide admin group memberships
- **System Owners**: Identify application administrators for owned systems
- **Database Team**: Identify database administrators (DBAs)
- **Network Team**: Identify network administrators
- **Cloud Team**: Identify cloud administrators (Azure, AWS, GCP)
- **Security Operations**: Identify security tool administrators (SIEM, PAM, backup)

**Approval Authority:** Chief Information Security Officer (CISO)

### 1.4 Expected Time Investment

**Initial Assessment** (establishing baseline):
- Privileged account discovery: 4-6 hours (depends on environment complexity)
- Admin tier classification: 2-4 hours
- PAM coverage assessment: 2-3 hours
- Workbook completion: 2-3 hours
- Evidence collection: 2-3 hours
- **Total**: 12-19 hours (spread over 1-2 weeks)

**Monthly Updates**:
- New privileged accounts: 30-60 minutes
- Leaver processing: 15-30 minutes
- Workbook updates: 15-30 minutes
- **Total**: 1-2 hours per month

**Quarterly Comprehensive Review**:
- Full inventory validation: 3-4 hours
- Tier isolation verification: 2-3 hours
- Access justification review: 2-3 hours
- Evidence update: 1-2 hours
- **Total**: 8-12 hours per quarter

---

## 2. Prerequisites

### 2.1 Required Information

Before starting the assessment, gather the following information:

**Privileged Account Discovery:**
- [ ] Active Directory group memberships (Domain Admins, Enterprise Admins, Schema Admins, local Administrators)
- [ ] Azure AD privileged roles (Global Administrator, Privileged Role Administrator, etc.)
- [ ] AWS IAM privileged users (AdministratorAccess policy, root account users)
- [ ] GCP IAM privileged users (Owner, Editor at organization/project level)
- [ ] Okta Super Admins and privileged roles
- [ ] System-specific administrator accounts (application admins, DBAs, network admins)

**Admin Tiering Classification:**
- [ ] List of Tier 0 systems (domain controllers, Azure AD tenant, PKI, PAM, SIEM, backup servers)
- [ ] List of Tier 1 systems (application servers, database servers, cloud subscriptions)
- [ ] List of Tier 2 systems (workstations, VDI, user endpoints)

**PAM Solution Details:**
- [ ] PAM solution in use (CyberArk, BeyondTrust, Azure PIM, native controls)
- [ ] Accounts vaulted in PAM
- [ ] Session recording status per account

**Account Ownership:**
- [ ] Privileged account owners (who owns each admin account)
- [ ] Business justification for privileged access
- [ ] Manager approvals for privileged access

### 2.2 Required Access

**System Access Needed:**
- [ ] Active Directory admin access (read group memberships, user properties)
- [ ] Azure AD Global Reader (read privileged role assignments)
- [ ] AWS IAM read access (list users, policies, roles)
- [ ] GCP IAM read access (list principals and bindings)
- [ ] PAM solution admin access (view vaulted accounts, session recordings)
- [ ] System owner access (identify application administrators)

**People Access Needed:**
- [ ] IT Operations managers (identify admin team members)
- [ ] System owners (identify system-specific administrators)
- [ ] DBAs and database team leads
- [ ] Network team leads
- [ ] Cloud team leads

### 2.3 Required Tools

**Software:**
- [ ] Microsoft Excel 2016 or later
- [ ] Python 3.8+ (if using automated workbook generation)
- [ ] PowerShell (for AD/Azure AD queries)
- [ ] Azure CLI / AWS CLI / GCP gcloud (for cloud privileged access queries)

**Scripts:**
- [ ] Active Directory privileged group enumeration script
- [ ] Azure AD privileged role assignment script
- [ ] Cloud IAM privileged user enumeration scripts

---

## 3. Understanding Admin Tiering Model (CRITICAL SECTION)

### 3.1 What is Admin Tiering?

The **Admin Tiering Model** (also called **Tiered Administration Model**) is a security architecture that segregates privileged accounts into three tiers based on the scope and criticality of systems they manage. This prevents **lateral movement** and **credential theft** during security incidents.

**Core Principle:** 
- Tier 0 accounts SHALL NEVER log into Tier 1 or Tier 2 systems
- Tier 1 accounts SHALL NEVER log into Tier 2 systems
- Violation of tier isolation = CRITICAL SECURITY INCIDENT

### 3.2 Tier Definitions

**Tier 0 - Domain/Enterprise/Critical Infrastructure**

**Scope:** Controls that can access or modify EVERYTHING in the organization

**Examples:**
- **Active Directory**: Domain Admins, Enterprise Admins, Schema Admins, BUILTIN\Administrators on domain controllers
- **Azure AD**: Global Administrator, Privileged Role Administrator, Cloud Application Administrator (can reset Global Admin passwords)
- **AWS**: Root account users, users with AdministratorAccess at organization level
- **GCP**: Organization Owners, Folder/Project Owners at organization level
- **PKI**: Certificate Authority administrators, enterprise PKI admins
- **Security Infrastructure**: PAM administrators, SIEM administrators, backup administrators (can restore domain controllers)
- **Identity Providers**: Okta Super Administrators, Google Workspace Super Admins

**Why Tier 0:**
- Can compromise ANY system in the organization
- If Tier 0 credentials stolen, attacker has full domain control
- Requires STRONGEST security controls

**Tier 0 Requirements:**
- ✅ Hardware MFA MANDATORY (FIDO2, YubiKey - NO SMS, NO authenticator app)
- ✅ Dedicated Privileged Access Workstations (PAWs) MANDATORY
- ✅ Session recording MANDATORY
- ✅ Network isolation (PAWs cannot browse internet, cannot access email)
- ✅ No daily work with Tier 0 accounts (admin tasks ONLY)

---

**Tier 1 - Server/Application Infrastructure**

**Scope:** Manages servers and applications but cannot directly access Tier 0 infrastructure

**Examples:**
- **Server Administrators**: Windows Server local admins, Linux sudo users (non-DC servers)
- **Database Administrators**: SQL Server SA, Oracle DBA, PostgreSQL superuser, MongoDB admin
- **Application Administrators**: SAP administrators, ERP admins, CRM admins
- **Cloud Infrastructure**: Azure subscription Owners/Contributors, AWS account admins, GCP project Owners
- **Virtualization**: VMware administrators, Hyper-V administrators
- **Middleware**: Application server admins (Tomcat, IIS, Apache administrators)

**Why Tier 1:**
- Can manage critical business applications and data
- Cannot directly compromise Tier 0 (domain controllers, PKI, etc.)
- If credentials stolen, blast radius limited to servers/applications

**Tier 1 Requirements:**
- ✅ MFA MANDATORY (authenticator app or hardware token)
- ✅ Dedicated admin workstations RECOMMENDED (separate VM or physical workstation)
- ✅ Session recording RECOMMENDED
- ✅ Separate admin accounts from user accounts (john.doe.admin ≠ john.doe)

---

**Tier 2 - Workstation/Endpoint**

**Scope:** Manages user endpoints only, cannot access servers or Tier 0/1 infrastructure

**Examples:**
- **Desktop Support**: Help desk with local admin rights on workstations
- **Endpoint Management**: MDM administrators (Intune, Jamf, SCCM workstation admins)
- **VDI Administrators**: VDI user desktop administrators (not VDI infrastructure - that's Tier 1)
- **Workstation Imaging**: Technicians who deploy workstation images

**Why Tier 2:**
- Lowest privilege tier
- Can only manage user workstations
- Cannot access servers, applications, or Tier 0 infrastructure
- If credentials stolen, attacker limited to workstation access

**Tier 2 Requirements:**
- ✅ MFA MANDATORY (authenticator app)
- ✅ Standard workstations (no dedicated admin workstations required)
- ✅ Standard logging and monitoring

### 3.3 Tier Isolation Rules (NON-NEGOTIABLE)

**CRITICAL RULE 1: Tier 0 accounts SHALL NEVER log into Tier 1 or Tier 2 systems**

❌ **VIOLATION EXAMPLE:**
- Domain Admin account (Tier 0) used to RDP into file server (Tier 1)
- Why violation: File server could be compromised, malware steals Domain Admin credentials cached in memory
- Result: Attacker now has Domain Admin, can compromise entire AD domain

✅ **CORRECT APPROACH:**
- Use separate Tier 1 admin account to manage file server
- Tier 0 Domain Admin account used ONLY on Tier 0 systems (domain controllers, PAWs)

---

**CRITICAL RULE 2: Tier 1 accounts SHALL NEVER log into Tier 2 systems**

❌ **VIOLATION EXAMPLE:**
- SQL Server DBA account (Tier 1) used to log into user workstation to help user
- Why violation: Workstation could be compromised, DBA credentials stolen
- Result: Attacker has database admin access, can access all business data

✅ **CORRECT APPROACH:**
- Use separate Tier 2 account for workstation support
- Tier 1 DBA account used ONLY on database servers

---

**CRITICAL RULE 3: Each admin has SEPARATE accounts per tier**

**Correct Account Structure:**
```
User: John Doe

john.doe                  → Standard user account (email, Office 365, daily work)
john.doe.tier2            → Tier 2 admin (workstation support)
john.doe.tier1            → Tier 1 admin (server management)
john.doe.tier0            → Tier 0 admin (domain controller management)

DIFFERENT PASSWORDS FOR EACH ACCOUNT
```

**Why separate accounts:**
- If john.doe account compromised (phishing email), Tier 0 credentials NOT exposed
- Each tier account has different password (compromise of one doesn't compromise others)
- Clear audit trail (Tier 0 account activity easily monitored)

### 3.4 Tier Isolation Verification

**How to verify tier isolation:**

1. **Check logon events**: Tier 0 accounts should ONLY log into Tier 0 systems
2. **Review authentication logs**: Look for cross-tier authentication (Tier 0 → Tier 1/2)
3. **Alert on violations**: SIEM alert on Tier 0 account logging into non-Tier 0 system
4. **Regular audits**: Quarterly review of tier isolation compliance

**Enforcement Mechanisms:**
- **Group Policy**: Deny logon to Tier 1/2 systems for Tier 0 accounts
- **Azure AD Conditional Access**: Block Tier 0 accounts from non-Tier 0 resources
- **PAM Solution**: Enforce tier-based access (CyberArk, BeyondTrust tier policies)
- **Network Segmentation**: Tier 0 PAWs cannot reach Tier 1/2 networks

---

## 4. Assessment Workflow

### 4.1 Assessment Process Overview

```
1. PREPARE
   → Gather privileged account lists (AD groups, Azure roles, cloud IAM)
   → Identify Tier 0, Tier 1, Tier 2 systems
   → Generate workbook (Python script or Excel template)

2. DISCOVER PRIVILEGED ACCOUNTS
   → Sheet 1: Privileged Account Inventory
      - Named accounts (john.doe.admin)
      - Shared accounts (root, Administrator, sa)
      - Service accounts with privileges
      - Break-glass accounts
   → Classify by tier (Tier 0, Tier 1, Tier 2, N/A)

3. ASSESS PAM COVERAGE
   → Which accounts are vaulted in PAM?
   → Which accounts have session recording?
   → Which accounts have password rotation?

4. VERIFY TIER ISOLATION
   → Check: Do Tier 0 accounts only access Tier 0 systems?
   → Identify tier isolation violations (critical incidents)

5. COLLECT EVIDENCE
   → AD group membership exports
   → Azure AD privileged role assignments
   → PAM coverage reports
   → Tier isolation verification logs

6. REVIEW & APPROVE
   → Security Team review (inventory completeness)
   → System Owner validation (confirm admins for their systems)
   → CISO approval (privileged access governance)

7. REMEDIATE GAPS
   → Enroll privileged accounts in PAM
   → Implement tier isolation (separate accounts per tier)
   → Enable MFA for privileged accounts without MFA
```

### 4.2 Step-by-Step Completion Guide

**Step 1: Discover Privileged Accounts**

**Active Directory Privileged Groups:**
```powershell
# Get Domain Admins
Get-ADGroupMember -Identity "Domain Admins" | Select Name, SamAccountName

# Get Enterprise Admins
Get-ADGroupMember -Identity "Enterprise Admins" | Select Name, SamAccountName

# Get Schema Admins
Get-ADGroupMember -Identity "Schema Admins" | Select Name, SamAccountName

# Get local Administrators on domain controllers
```

**Azure AD Privileged Roles:**
```powershell
# Connect to Azure AD
Connect-AzureAD

# Get Global Administrators
Get-AzureADDirectoryRole | Where-Object {$_.DisplayName -eq "Global Administrator"} | 
  Get-AzureADDirectoryRoleMember | Select DisplayName, UserPrincipalName

# Get all privileged role assignments
Get-AzureADDirectoryRole | ForEach-Object {
  $role = $_
  Get-AzureADDirectoryRoleMember -ObjectId $role.ObjectId | Select @{N='Role';E={$role.DisplayName}}, DisplayName, UserPrincipalName
}
```

**AWS IAM Privileged Users:**
```bash
# List users with AdministratorAccess policy
aws iam list-policies --scope Local --query 'Policies[?PolicyName==`AdministratorAccess`].Arn' --output text | 
  xargs -I {} aws iam list-entities-for-policy --policy-arn {}
```

**Step 2: Generate Workbook**

Option A - Automated (Recommended):
```bash
python3 generate_a8235_3_privileged_accounts.py
```
This creates: `ISMS-IMP-A.8.2-3-5.3_Privileged_Accounts_YYYYMMDD.xlsx`

Option B - Manual:
- Use Excel template
- Save as: `ISMS-IMP-A.8.2-3-5.3_Privileged_Accounts_[DATE].xlsx`

**Step 3: Complete Sheet 1 - Privileged Account Inventory**

For each privileged account:

1. **Account Identification** (Columns A-E):
   - Account ID: Unique identifier (username, SamAccountName)
   - Account Name: Display name or description
   - Account Type: Named, Shared, Service, Break-Glass
   - Platform: Windows AD, Azure AD, Linux, AWS, GCP, Application
   - Account Owner: Person responsible (for named accounts) or team (for shared)

2. **Privileged Role** (Columns F-H):
   - Privileged Role: Domain Admin, Server Admin, DBA, Network Admin, Cloud Admin, Security Admin, Application Admin
   - Role Description: Brief description of privileges
   - Systems/Applications: Where this account has privileges

3. **Admin Tier Classification** (Columns I-J):
   - Admin Tier: Tier 0, Tier 1, Tier 2, N/A (THIS IS CRITICAL)
   - Tier Justification: Why this tier? (e.g., "Domain Admin = Tier 0", "SQL DBA = Tier 1")

4. **PAM Coverage** (Columns K-N):
   - PAM Vaulted: Yes, No (is password stored in PAM?)
   - Session Recording: Yes, No (are sessions recorded?)
   - Password Rotation: Yes, No, N/A (automated rotation?)
   - Rotation Frequency: Daily, Weekly, Monthly, Quarterly, Manual

5. **Security Controls** (Columns O-Q):
   - MFA Enrolled: Yes, No (does account have MFA?)
   - MFA Method: Hardware Token, Authenticator App, etc.
   - Dedicated Workstation: Yes, No, N/A (PAW for Tier 0?)

6. **Access Governance** (Columns R-U):
   - Business Justification: Why does this account need privileges?
   - Manager Approval: Manager who approved privileged access
   - Last Access Review: Date of last access review
   - Compliance Status: Compliant, Partial, Non-Compliant

**Step 4: Complete Sheet 2 - Privileged User Summary**

This sheet auto-calculates from Sheet 1:

**By User:**
For each person who owns privileged accounts:
- User Name
- Privileged Accounts Owned (count)
- Tier 0 Access (Yes/No)
- Tier 1 Access (Yes/No)
- Tier 2 Access (Yes/No)
- Multiple Tier Access (Yes/No - flag for review)

**Step 5: Complete Sheet 3 - Tier Isolation Compliance**

**Tier 0 Accounts:**
- Total Tier 0 accounts
- Tier 0 accounts with dedicated PAWs (%)
- Tier 0 accounts with hardware MFA (%)
- Tier 0 accounts with session recording (%)

**Tier Isolation Violations:**
- Tier 0 accounts that logged into Tier 1/2 systems (count - should be 0)
- Tier 1 accounts that logged into Tier 2 systems (count - should be 0)
- Cross-tier violation events (log analysis)

**Step 6: Complete Sheet 4 - PAM Coverage**

**Overall:**
- Total privileged accounts: [count]
- Accounts in PAM vault: [count] ([%])
- Accounts with session recording: [count] ([%])
- Accounts with automated rotation: [count] ([%])

**By Account Type:**
- Named accounts: [count] → PAM coverage [%]
- Shared accounts: [count] → PAM coverage [%]
- Service accounts: [count] → PAM coverage [%]
- Break-glass accounts: [count] → PAM coverage [%]

**Step 7: Collect Evidence**

Required evidence:

- **AD Group Membership Export**: CSV export of Domain Admins, Enterprise Admins, etc.
- **Azure AD Privileged Role Assignments**: Screenshot or CSV export
- **PAM Coverage Report**: Screenshot from PAM solution showing vaulted accounts
- **Tier Isolation Verification**: SIEM query results showing Tier 0 logon events
- **MFA Enrollment for Privileged Users**: Cross-reference with IMP.2

Store evidence in: `/evidence/privileged-access/[date]/`

**Step 8: Complete Evidence Register (Sheet 5)**

Document all collected evidence with links.

**Step 9: Approval & Sign-Off (Sheet 6)**

Three-level approval process.

---

## 5. Evidence Collection Guidelines

### 5.1 Required Evidence Types

**For Privileged Account Inventory:**

1. **Active Directory Evidence**:
   - `Get-ADGroupMember` export for privileged groups (Domain Admins, etc.)
   - Screenshot of AD group memberships
   - Export dated with timestamp

2. **Azure AD Evidence**:
   - Privileged role assignment report
   - Screenshot of Global Administrator role members
   - PIM (Privileged Identity Management) configuration

3. **Cloud IAM Evidence**:
   - AWS IAM policy attachments (users with AdministratorAccess)
   - GCP IAM bindings (organization/project Owners)
   - Cloud provider privileged access reports

4. **PAM Solution Evidence**:
   - Screenshot of vaulted accounts
   - Session recording configuration
   - Password rotation schedule

5. **Tier Isolation Evidence**:
   - SIEM query: Tier 0 account logon events (should only be Tier 0 systems)
   - GPO or Conditional Access policy enforcing tier isolation
   - Tier violation alerts (if any)

### 5.2 Evidence Storage

**Structure:**
```
/evidence/privileged-access/
├── 2026-01-22/
│   ├── ad-domain-admins-export.csv
│   ├── azure-ad-global-admins-screenshot.png
│   ├── pam-coverage-report.pdf
│   ├── tier-isolation-siem-query.png
│   └── privileged-account-mfa-status.csv
├── tier-isolation-policies/
│   ├── gpo-tier0-logon-restrictions.xml
│   └── azure-conditional-access-tier0.json
└── access-reviews/
    └── 2026-Q1-privileged-access-review.xlsx
```

### 5.3 Evidence Quality Checklist

For each piece of evidence:
- [ ] Timestamp visible
- [ ] Source clearly identified
- [ ] Account names NOT redacted (needed for audit)
- [ ] Passwords redacted (if applicable)
- [ ] Linked in Evidence Register

---

## 6. Common Pitfalls & How to Avoid Them

### Pitfall 1: Not Understanding Tier 0

**Problem**: Misclassifying accounts (e.g., calling backup admin "Tier 1" when it's actually Tier 0)

**Solution**:
- **Rule**: Can this account restore a domain controller? → Tier 0
- **Rule**: Can this account modify enterprise-wide security policy? → Tier 0
- Backup admins = Tier 0 (can restore DCs)
- PKI admins = Tier 0 (can issue certificates for any system)
- PAM admins = Tier 0 (can access any vaulted credential)

### Pitfall 2: Missing Service Accounts with Privileges

**Problem**: Only inventorying interactive user accounts, missing service accounts with elevated privileges

**Solution**:
- Check: Which service accounts are Domain Admins?
- Check: Which service accounts have local admin rights?
- Check: Which service accounts have database SA/DBA rights?
- Service accounts with privileges = privileged accounts (inventory them)

### Pitfall 3: Not Separating Admin Accounts from User Accounts

**Problem**: Admins using same account for daily work (email, web browsing) and administration

**Solution**:
- Enforce separate accounts: john.doe (daily work), john.doe.admin (admin tasks)
- NO admin work from user account
- NO daily work from admin account

### Pitfall 4: Allowing Tier 0 Accounts to Browse Internet

**Problem**: Tier 0 admin account used on workstation with internet access

**Solution**:
- Tier 0 accounts used ONLY on PAWs (Privileged Access Workstations)
- PAWs have NO internet access, NO email
- PAWs are dedicated, hardened, isolated workstations

### Pitfall 5: Shared Admin Accounts Without PAM

**Problem**: Shared "Administrator" or "root" account used by multiple admins without vaulting

**Solution**:
- ALL shared admin accounts MUST be vaulted in PAM
- PAM manages password (admins check out password, use it, check in - password rotates)
- Session recording MANDATORY for shared accounts

### Pitfall 6: Break-Glass Accounts Not Tested

**Problem**: Emergency break-glass account exists but password is unknown/expired/doesn't work

**Solution**:
- Test break-glass accounts quarterly
- Verify password works
- Verify account has intended privileges
- After test, rotate password and re-seal

### Pitfall 7: Not Tracking "Multiple Tier Access"

**Problem**: Admin has Tier 0, Tier 1, AND Tier 2 access (violates principle of least privilege)

**Solution**:
- Flag users with multiple tier access (Sheet 2)
- Question: Why does this person need access to multiple tiers?
- Remediate: Remove unnecessary tier access

### Pitfall 8: Cloud Admins Not Classified

**Problem**: Azure Global Administrator or AWS root user not recognized as Tier 0

**Solution**:
- Azure Global Administrator = Tier 0 (can do anything in Azure AD tenant)
- AWS root account users = Tier 0
- GCP Organization Owner = Tier 0
- Cloud global admins have SAME risk as Domain Admins

### Pitfall 9: Assuming PAM Means Tier Isolation

**Problem**: Thinking PAM solution automatically enforces tier isolation

**Solution**:
- PAM vaulting ≠ Tier isolation
- PAM is ONE control (password vaulting, session recording)
- Tier isolation requires separate accounts, separate workstations, GPO/Conditional Access enforcement
- PAM + Tier Isolation = defense in depth

### Pitfall 10: Not Celebrating Small Wins

**Problem**: Privileged access security is long-term effort, team gets discouraged

**Solution**:
- Celebrate: "100% of Domain Admins now have MFA!"
- Celebrate: "All Tier 0 accounts now vaulted in PAM!"
- Celebrate: "Zero tier isolation violations this quarter!"
- Track progress month-over-month

---

## 7. Quality Checklist

Before submitting assessment for approval, verify:

### 7.1 Completeness

- [ ] All privileged accounts inventoried (AD, Azure AD, cloud IAM, applications, databases)
- [ ] All privileged accounts classified by tier (Tier 0, Tier 1, Tier 2)
- [ ] All account types covered (named, shared, service, break-glass)
- [ ] PAM coverage documented for all accounts
- [ ] MFA status documented for all accounts

### 7.2 Accuracy

- [ ] Tier classifications reviewed (Tier 0 = can access anything, validated)
- [ ] Privileged role descriptions accurate
- [ ] Account ownership validated with system owners
- [ ] PAM coverage verified against PAM solution
- [ ] MFA status cross-referenced with IMP.2

### 7.3 Tier Isolation

- [ ] Tier 0 accounts identified and flagged
- [ ] Tier 0 accounts have dedicated PAWs (or planned)
- [ ] Tier isolation violations identified (if any)
- [ ] Users with multiple tier access flagged for review

### 7.4 Evidence Quality

- [ ] AD group membership exports collected
- [ ] Azure AD role assignments documented
- [ ] PAM coverage reports collected
- [ ] Tier isolation verification evidence collected
- [ ] Evidence dated and linked

### 7.5 Compliance

- [ ] Privileged accounts without MFA identified as CRITICAL gaps
- [ ] Privileged accounts without PAM vaulting identified
- [ ] Tier isolation non-compliance identified
- [ ] Remediation timeline defined

---

## 8. Interpreting Results

### 8.1 Understanding Privileged Access Scores

**PAM Coverage:**
- **100%**: All privileged accounts vaulted (ideal state)
- **90-99%**: Nearly complete coverage, document exceptions
- **80-89%**: Good progress, prioritize remaining gaps
- **<80%**: Insufficient PAM coverage (high risk)

**Tier 0 Security Score:**
- **100%**: All Tier 0 controls implemented (PAWs, hardware MFA, session recording, tier isolation)
- **75-99%**: Most controls in place, some gaps
- **<75%**: CRITICAL RISK - Tier 0 not adequately protected

**Tier Isolation Compliance:**
- **Zero violations**: Excellent - Tier isolation enforced
- **1-5 violations/quarter**: Acceptable - Investigate and remediate
- **>5 violations/quarter**: CRITICAL - Tier isolation not enforced, architectural issue

### 8.2 Gap Prioritization

**Priority 1 - CRITICAL (Immediate Action - Within 7 Days):**
- Tier 0 accounts without hardware MFA
- Tier 0 accounts without PAM vaulting
- Tier 0 accounts without dedicated PAWs
- Tier isolation violations (Tier 0 account logging into Tier 1/2)
- Shared privileged accounts without PAM vaulting

**Priority 2 - HIGH (Within 30 Days):**
- Tier 1 privileged accounts without MFA
- Privileged accounts without PAM vaulting (Tier 1)
- Tier 1 accounts without session recording
- Privileged accounts with no access review in >1 year

**Priority 3 - MEDIUM (Within 90 Days):**
- Tier 2 accounts without MFA
- Service accounts without automated password rotation
- Privileged accounts with no documented business justification

**Priority 4 - LOW (Ongoing Improvement):**
- Optimization of PAM workflows
- Enhanced session recording analytics
- Privileged access training improvements

---

## 9. Review & Approval Process

### 9.1 Approval Workflow

**Level 1 - Preparer (Security Team)**:
- Discover and inventory privileged accounts
- Classify by admin tier
- Assess PAM coverage
- Collect evidence
- Submit for review

**Level 2 - Reviewer (Senior Security / IAM Lead)**:
- Validate tier classifications
- Verify PAM coverage data
- Check tier isolation compliance
- Confirm evidence completeness
- Approve and forward to CISO

**Level 3 - Approver (CISO)**:
- Review privileged access metrics
- Validate Tier 0 security controls
- Approve tier isolation strategy
- Sign off on assessment
- Present to Executive Management (if required)

### 9.2 Approval Criteria

Assessment is approved when:
- [ ] All privileged accounts inventoried
- [ ] Admin tier classifications documented
- [ ] PAM coverage assessed
- [ ] Tier isolation compliance verified
- [ ] Critical gaps identified and prioritized
- [ ] Remediation timeline defined

### 9.3 Post-Approval Actions

After CISO approval:
1. **Communicate Gaps**: Notify privileged users of security gaps (MFA missing, PAM enrollment needed)
2. **Escalate Critical**: Tier 0 gaps escalated immediately
3. **Track Remediation**: Move gaps to Dashboard (IMP.6)
4. **Schedule Next Review**: Monthly updates, quarterly comprehensive review

---

# PART II: TECHNICAL SPECIFICATION

## 1. Excel Workbook Structure

### 1.1 Workbook Overview

**Filename:** `ISMS-IMP-A.8.2-3-5.3_Privileged_Accounts_YYYYMMDD.xlsx`

**Sheet Structure:**

| Sheet # | Sheet Name | Purpose | Rows | Completion Method |
|---------|-----------|---------|------|-------------------|
| 1 | Instructions & Legend | User guide and Admin Tiering reference | ~80 | Pre-populated |
| 2 | Privileged Account Inventory | All privileged accounts with tier classification | 503 | User completes |
| 3 | Privileged User Summary | Users who own privileged accounts | 203 | Auto-calculated |
| 4 | Tier Isolation Compliance | Tier 0/1/2 security metrics | ~40 | Auto-calculated |
| 5 | PAM Coverage Analysis | PAM vaulting and session recording coverage | ~30 | Auto-calculated |
| 6 | Evidence Register | Evidence tracking | 53 | User completes |
| 7 | Approval & Sign-Off | Three-level approval | ~25 | User completes |

**Total Workbook:** 7 sheets, ~950 rows of structured data collection

### 1.2 Color Coding & Conditional Formatting

**Admin Tier Colors:**
- 🔴 **Red (Tier 0)**: RGB(255, 0, 0) - Highest privilege, strictest controls
- 🟠 **Orange (Tier 1)**: RGB(255, 153, 0) - Server/application privileges
- 🟡 **Yellow (Tier 2)**: RGB(255, 255, 0) - Workstation privileges
- ⚫ **Gray (N/A)**: RGB(217, 217, 217) - Not tiered

**Compliance Status Colors:**
- 🟢 **Green (Compliant)**: RGB(198, 239, 206) - Meets all requirements
- 🟡 **Yellow (Partial)**: RGB(255, 235, 156) - Meets some requirements
- 🔴 **Red (Non-Compliant)**: RGB(255, 199, 206) - Does not meet requirements

---

## 2. Sheet 2: Privileged Account Inventory (Primary Data Collection)

### 2.1 Purpose

Comprehensive inventory of ALL privileged accounts with Admin Tiering classification.

### 2.2 Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Account ID | 20 | Text | Free text | Unique identifier (SamAccountName, UPN, username) |
| B | Account Name | 25 | Text | Free text | Display name or description |
| C | Account Type | 15 | Dropdown | Named, Shared, Service, Break-Glass | Account classification |
| D | Platform | 18 | Dropdown | Windows AD, Azure AD, Linux, AWS, GCP, Azure, Okta, Application, Database, Network | Where account exists |
| E | Account Owner | 22 | Text | Free text | Person responsible (named) or team (shared/service) |
| F | Privileged Role | 20 | Dropdown | Domain Admin, Enterprise Admin, Server Admin, DBA, Network Admin, Cloud Admin, Security Admin, Application Admin, Other | Type of privilege |
| G | Role Description | 30 | Text | Free text | Brief description of privileges |
| H | Systems/Applications | 30 | Text | Free text | Where this account has privileges |
| I | **Admin Tier** | 12 | Dropdown | **Tier 0, Tier 1, Tier 2, N/A** | **CRITICAL: Tier classification** |
| J | Tier Justification | 30 | Text | Free text | Why this tier? (e.g., "Domain Admin = Tier 0") |
| K | PAM Vaulted | 12 | Dropdown | Yes, No | Is password in PAM vault? |
| L | Session Recording | 15 | Dropdown | Yes, No, N/A | Are sessions recorded? |
| M | Password Rotation | 18 | Dropdown | Yes, No, N/A | Automated rotation? |
| N | Rotation Frequency | 18 | Dropdown | After Each Use, Daily, Weekly, Monthly, Quarterly, Manual | How often? |
| O | MFA Enrolled | 12 | Dropdown | Yes, No | MFA on this account? |
| P | MFA Method | 18 | Dropdown | Hardware Token (FIDO2), Authenticator App, SMS, Other | MFA type |
| Q | Dedicated Workstation | 18 | Dropdown | Yes (PAW), Yes (Dedicated VM), No, N/A | Admin workstation? |
| R | Business Justification | 30 | Text | Free text | Why does this account need privileges? |
| S | Manager Approval | 20 | Text | Free text | Manager who approved |
| T | Last Access Review | 15 | Date | DD.MM.YYYY | Date of last review |
| U | Compliance Status | 18 | Formula | Auto: Compliant, Partial, Non-Compliant | Meets policy? |

**Total Columns:** 21 (A-U)

### 2.3 Data Validation Rules

**Account Type (Column C):**
```
List: Named, Shared, Service, Break-Glass
```

**Platform (Column D):**
```
List: Windows Active Directory, Azure AD, Linux, AWS IAM, GCP IAM, Azure, 
Okta, Application-Specific, Database, Network Device, Other
```

**Privileged Role (Column F):**
```
List: Domain Admin, Enterprise Admin, Schema Admin, Server Admin (Windows), 
Server Admin (Linux), Database Administrator, Network Admin, 
Cloud Admin (Azure), Cloud Admin (AWS), Cloud Admin (GCP), 
Security Admin, Application Admin, Backup Admin, PKI Admin, Other
```

**Admin Tier (Column I) - CRITICAL:**
```
List: Tier 0, Tier 1, Tier 2, N/A
```

**PAM Vaulted / Session Recording (Columns K, L):**
```
List: Yes, No, N/A
```

**Password Rotation (Column M):**
```
List: Yes, No, N/A
```

**Rotation Frequency (Column N):**
```
List: After Each Use, Daily, Weekly, Monthly, Quarterly, Manual, N/A
```

**MFA Enrolled (Column O):**
```
List: Yes, No
```

**MFA Method (Column P):**
```
List: Hardware Token (FIDO2), Hardware Token (TOTP), Authenticator App (TOTP), 
Push Notification, SMS, Biometric, Certificate, None
```

**Dedicated Workstation (Column Q):**
```
List: Yes (PAW), Yes (Dedicated VM), Yes (Jump Server), No, N/A
```

### 2.4 Compliance Status Calculation (Column U)

**Formula Logic:**
```excel
=IF(I5="Tier 0",
    IF(AND(O5="Yes", P5="Hardware Token (FIDO2)", K5="Yes", L5="Yes", Q5="Yes (PAW)"),
        "Compliant",
        "Non-Compliant"),
    IF(I5="Tier 1",
        IF(AND(O5="Yes", K5="Yes"),
            IF(L5="Yes", "Compliant", "Partial"),
            "Non-Compliant"),
        IF(I5="Tier 2",
            IF(O5="Yes", "Compliant", "Non-Compliant"),
            "N/A")))
```

**Compliance Requirements:**

**Tier 0:**
- MFA = Yes (REQUIRED)
- MFA Method = Hardware Token FIDO2 (REQUIRED)
- PAM Vaulted = Yes (REQUIRED)
- Session Recording = Yes (REQUIRED)
- Dedicated Workstation = Yes (PAW) (REQUIRED)

**Tier 1:**
- MFA = Yes (REQUIRED)
- PAM Vaulted = Yes (REQUIRED)
- Session Recording = Yes (RECOMMENDED - Partial if missing)

**Tier 2:**
- MFA = Yes (REQUIRED)

**Conditional Formatting:**
- Compliant → Green
- Partial → Yellow
- Non-Compliant → Red
- N/A → Gray

### 2.5 Admin Tier Color Coding (Column I)

**Conditional Formatting:**
- Tier 0 → Red background (RGB 255, 0, 0), White text
- Tier 1 → Orange background (RGB 255, 153, 0), Black text
- Tier 2 → Yellow background (RGB 255, 255, 0), Black text
- N/A → Gray background

---

## 3. Sheet 3: Privileged User Summary

### 3.1 Purpose

Summary of privileged access per user (who has what tier access).

### 3.2 Auto-Calculation Logic

For each unique owner in Sheet 2:

```excel
Owner Name: =UNIQUE('Privileged Account Inventory'!E:E)

Privileged Accounts Owned: 
  =COUNTIF('Privileged Account Inventory'!E:E, Owner_Name)

Tier 0 Access: 
  =IF(COUNTIFS('Privileged Account Inventory'!E:E, Owner_Name, 
               'Privileged Account Inventory'!I:I, "Tier 0")>0, "Yes", "No")

Tier 1 Access: 
  =IF(COUNTIFS('Privileged Account Inventory'!E:E, Owner_Name, 
               'Privileged Account Inventory'!I:I, "Tier 1")>0, "Yes", "No")

Tier 2 Access: 
  =IF(COUNTIFS('Privileged Account Inventory'!E:E, Owner_Name, 
               'Privileged Account Inventory'!I:I, "Tier 2")>0, "Yes", "No")

Multiple Tier Access: 
  =IF(COUNTIF([Tier 0 Access], [Tier 1 Access], [Tier 2 Access], "Yes")>1, 
      "Yes - Review Required", "No")
```

**Flag for Review:**
- Users with Tier 0 AND Tier 1/2 access (potential tier isolation risk)
- Users with >5 privileged accounts (excessive privilege)

---

## 4. Sheet 4: Tier Isolation Compliance

### 4.1 Purpose

Measure tier isolation implementation and compliance.

### 4.2 Metrics Calculated

**Tier 0 Security Controls:**
```excel
Total Tier 0 Accounts: 
  =COUNTIF('Privileged Account Inventory'!I:I, "Tier 0")

Tier 0 with Hardware MFA: 
  =COUNTIFS('Privileged Account Inventory'!I:I, "Tier 0",
            'Privileged Account Inventory'!P:P, "Hardware Token (FIDO2)")

Tier 0 with PAWs: 
  =COUNTIFS('Privileged Account Inventory'!I:I, "Tier 0",
            'Privileged Account Inventory'!Q:Q, "Yes (PAW)")

Tier 0 with Session Recording: 
  =COUNTIFS('Privileged Account Inventory'!I:I, "Tier 0",
            'Privileged Account Inventory'!L:L, "Yes")

Tier 0 Security Score: 
  =(Tier0_HW_MFA / Total_Tier0 + Tier0_PAWs / Total_Tier0 + 
    Tier0_SessionRec / Total_Tier0) / 3 * 100
```

**Tier Isolation Violations:**
```excel
Users with Multiple Tier Access: 
  =COUNTIF('Privileged User Summary'!F:F, "Yes - Review Required")

Tier 0 Accounts Without PAWs: 
  =COUNTIFS('Privileged Account Inventory'!I:I, "Tier 0",
            'Privileged Account Inventory'!Q:Q, "No")

[Manual Entry] Cross-Tier Logon Events (from SIEM): [Count]
```

---

## 5. Sheet 5: PAM Coverage Analysis

### 5.1 Purpose

Measure PAM solution adoption and session recording coverage.

### 5.2 Metrics Calculated

**Overall PAM Coverage:**
```excel
Total Privileged Accounts: 
  =COUNTA('Privileged Account Inventory'!A5:A503)

Accounts in PAM Vault: 
  =COUNTIF('Privileged Account Inventory'!K:K, "Yes")

PAM Coverage %: 
  =Accounts_PAM / Total_Accounts * 100

Accounts with Session Recording: 
  =COUNTIF('Privileged Account Inventory'!L:L, "Yes")

Session Recording Coverage %: 
  =Accounts_SessionRec / Total_Accounts * 100
```

**PAM Coverage by Account Type:**
```excel
Named Accounts Total: 
  =COUNTIF('Privileged Account Inventory'!C:C, "Named")

Named Accounts in PAM: 
  =COUNTIFS('Privileged Account Inventory'!C:C, "Named",
            'Privileged Account Inventory'!K:K, "Yes")

Named Account PAM Coverage %: 
  =Named_PAM / Named_Total * 100

[Repeat for Shared, Service, Break-Glass]
```

**PAM Coverage by Tier:**
```excel
Tier 0 Accounts in PAM: 
  =COUNTIFS('Privileged Account Inventory'!I:I, "Tier 0",
            'Privileged Account Inventory'!K:K, "Yes")

Tier 0 PAM Coverage %: 
  =Tier0_PAM / Total_Tier0 * 100

[Repeat for Tier 1, Tier 2]
```

---

## 6. Sheet 6: Evidence Register

### 6.1 Column Structure

| Col | Header | Width | Type | Description |
|-----|--------|-------|------|-------------|
| A | Evidence ID | 15 | Text | EV-A8235-3-001 |
| B | Evidence Type | 20 | Dropdown | Group Membership, Role Assignment, PAM Report, SIEM Query, Policy Document |
| C | Description | 30 | Text | Brief description |
| D | File Location | 30 | Text | Path to evidence file |
| E | Collection Date | 15 | Date | When collected |
| F | Collected By | 18 | Text | Person who collected |

---

## 7. Sheet 7: Approval & Sign-Off

### 7.1 Three-Level Approval

**Level 1 - Preparer (Security Team):**
- Name, Title, Date, Signature

**Level 2 - Reviewer (IAM Lead / Senior Security Engineer):**
- Name, Title, Date, Signature

**Level 3 - Approver (CISO):**
- Name, Title, Date, Signature

---

## 8. Python Script Integration

### 8.1 Script Purpose

Automated generation of privileged account inventory workbook.

**Script:** `generate_a8235_3_privileged_accounts.py`

### 8.2 Script Features

- Creates all 7 sheets with proper structure
- Applies data validation rules (dropdowns, tier classifications)
- Implements conditional formatting (tier colors, compliance colors)
- Adds formulas for compliance calculations
- Generates privileged user summary
- Calculates tier isolation metrics
- Sets column widths and freeze panes

### 8.3 Running the Script

```bash
# Basic usage
python3 generate_a8235_3_privileged_accounts.py

# With custom date
python3 generate_a8235_3_privileged_accounts.py --date 2026-01-22

# Custom output path
python3 generate_a8235_3_privileged_accounts.py --output /path/to/file.xlsx
```

### 8.4 Script Customization Points

Marked with `# CUSTOMIZE:` in script:
- Admin tier definitions (organizational tier model)
- Privileged role categories (additional role types)
- Compliance criteria (different tier requirements)
- PAM solution integration (CyberArk, BeyondTrust API)

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

## Document Assembly & Quality Checks

**Complete Document Structure:**
```
ISMS-IMP-A.8.2-3-5.3 - Privileged Account Inventory v1.0

├── Document Control (Metadata, Version History)
│
├── PART I: USER COMPLETION GUIDE (~700 lines)
│   ├── 1. Assessment Overview
│   ├── 2. Prerequisites
│   ├── 3. Understanding Admin Tiering Model (CRITICAL)
│   ├── 4. Assessment Workflow
│   ├── 5. Evidence Collection
│   ├── 6. Common Pitfalls (10 pitfalls)
│   ├── 7. Quality Checklist
│   ├── 8. Interpreting Results
│   └── 9. Review & Approval
│
└── PART II: TECHNICAL SPECIFICATION (~350 lines)
    ├── 1. Workbook Structure
    ├── 2. Sheet 2: Privileged Account Inventory
    ├── 3. Sheet 3: Privileged User Summary
    ├── 4. Sheet 4: Tier Isolation Compliance
    ├── 5. Sheet 5: PAM Coverage Analysis
    ├── 6. Sheet 6: Evidence Register
    ├── 7. Sheet 7: Approval & Sign-Off
    └── 8. Python Script Integration
```

**Quality Checks Before Finalizing:**
- [ ] Admin Tiering Model thoroughly explained
- [ ] Tier 0/1/2 definitions clear with examples
- [ ] Tier isolation rules emphasized (NON-NEGOTIABLE)
- [ ] PAM requirements clearly documented
- [ ] Cross-references correct (policy, other IMPs)
- [ ] No placeholder text
- [ ] Technical specification matches Python script

---

**END OF ISMS-IMP-A.8.2-3-5.3**

*Privileged accounts are the keys to the kingdom. Inventory them. Tier them. Protect them.*

*Admin Tiering prevents lateral movement. Tier isolation is NON-NEGOTIABLE.*

*Remember: Tier 0 accounts SHALL NEVER log into Tier 1 or Tier 2 systems. No exceptions.*
