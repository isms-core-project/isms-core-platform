# ISMS-IMP-A.5.17.2 - MFA Deployment Assessment

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.17.2 |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.17 Authentication Information |
| **Parent Policy** | ISMS-POL-A.5.17 - Authentication Information |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Workbook Structure](#14-workbook-structure)
   - [1.5 Completion Walkthrough](#15-completion-walkthrough)
   - [1.6 Evidence Collection](#16-evidence-collection)
   - [1.7 Common Pitfalls](#17-common-pitfalls)
   - [1.8 Quality Checklist](#18-quality-checklist)
   - [1.9 Review and Approval](#19-review-and-approval)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Technical Details](#21-workbook-technical-details)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Conditional Formatting](#23-conditional-formatting)
   - [2.4 Integration Points](#24-integration-points)
   - [2.5 Related Documents](#25-related-documents)

---

# PART I: USER COMPLETION GUIDE

---

## 1.1 Assessment Overview

### Purpose

This workbook provides a comprehensive Multi-Factor Authentication (MFA) Deployment Assessment framework that inventories MFA requirements across systems, tracks MFA enrollment status, and ensures coverage aligns with policy requirements.

The assessment serves multiple purposes:
- **Coverage Mapping**: Identify all systems requiring MFA and current deployment state
- **Enrollment Tracking**: Monitor user MFA registration and compliance rates
- **Method Verification**: Ensure approved MFA methods are in use
- **Gap Identification**: Identify systems and users lacking required MFA protection
- **Evidence**: Provide Stage 2 audit evidence of MFA implementation effectiveness

### Scope

The MFA Deployment Assessment covers:

| Access Category | MFA Requirement | Examples |
|-----------------|-----------------|----------|
| **Privileged Access** | Mandatory (no exceptions) | Admin consoles, PAM, infrastructure |
| **Remote Access** | Mandatory | VPN, remote desktop, cloud access |
| **CONFIDENTIAL Systems** | Mandatory | Systems processing CONFIDENTIAL data |
| **Internet-Facing** | Mandatory | Customer portals, external services |
| **Standard Internal** | Risk-based | Internal apps per IdP conditional access policy |
| **Service Accounts** | Certificate/token preferred | Non-interactive access |

**Approved MFA Methods (per ISMS-POL-A.5.17):**

| Method | Approval Status | Use Case |
|--------|-----------------|----------|
| Hardware security keys (FIDO2) | Approved - Preferred | Privileged access, high-risk users |
| Authenticator apps (TOTP) | Approved | General workforce |
| Push notifications | Approved with fatigue controls | General workforce |
| Biometric (device-bound) | Approved | Device unlock, Windows Hello |
| SMS/Voice OTP | Not approved (new) | Legacy only with exception |
| Email OTP | Not approved | N/A |
| Security questions | Prohibited | N/A |

**Exclusions:**
- Service accounts using certificate authentication (no MFA required)
- Air-gapped systems with physical access controls only
- Local emergency accounts (covered by break-glass procedures)

### Business Value

| Value Area | Benefit |
|------------|---------|
| **Breach Prevention** | MFA blocks 99.9% of credential-based attacks |
| **Compliance** | Meets ISO 27001, NIST, PCI DSS, FINMA requirements |
| **Cyber Insurance** | MFA is prerequisite for most cyber insurance policies |
| **Zero Trust** | Foundation for Zero Trust architecture |
| **User Trust** | Demonstrates security commitment to customers |

### Assessment Frequency

| Assessment Type | Frequency | Trigger Events |
|-----------------|-----------|----------------|
| Full Coverage Assessment | Annual | New systems, M&A, policy changes |
| Enrollment Status | Monthly | User onboarding cycles |
| Method Compliance | Quarterly | New MFA methods, deprecation |
| Conditional Access Review | Quarterly | Policy changes, audit findings |
| Ad-hoc Assessment | As needed | Security incidents, audit requests |

---

## 1.2 Control Requirements

### ISO 27001:2022 Control A.5.17

Per ISO/IEC 27001:2022 Control A.5.17:

> *"Allocation and management of authentication information should be controlled by a management process, including advising personnel on appropriate handling of authentication information."*

Multi-factor authentication is a critical implementation of this control, providing defense-in-depth for authentication.

**Control Type:** Preventive
**Security Properties:** Confidentiality, Integrity
**Cybersecurity Concepts:** Protect
**Operational Capabilities:** Identity and Access Management

### MFA Requirements (from ISMS-POL-A.5.17)

| Access Type | MFA Requirement | Approved Methods |
|-------------|-----------------|------------------|
| Privileged Access | Mandatory - No exceptions | Hardware keys, Authenticator apps |
| Remote Access | Mandatory | Hardware keys, Authenticator apps, Push |
| CONFIDENTIAL Data | Mandatory | Hardware keys, Authenticator apps, Push |
| Internet-Facing | Mandatory | Hardware keys, Authenticator apps, Push |
| Standard Internal | Risk-based per IdP policy | Authenticator apps, Push, Biometric |

### What Auditors Look For

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Policy Coverage** | MFA requirements documented in ISMS-POL-A.5.17 |
| **System Coverage** | Inventory of systems with MFA status |
| **User Enrollment** | Enrollment rates and exceptions |
| **Method Compliance** | Evidence approved methods are used |
| **Conditional Access** | IdP policies enforcing MFA |
| **Exceptions** | Documented exceptions with compensating controls |
| **Monitoring** | Evidence of MFA bypass attempts and response |

---

## 1.3 Prerequisites

### Required Access

| System | Purpose | Access Level Needed |
|--------|---------|---------------------|
| Identity Provider | MFA configuration, enrollment reports | Admin or security reader |
| Conditional Access | Policy review | Security reader |
| User Directory | User population | Read access |
| PAM Solution | Privileged account MFA status | Audit access |
| Application Portfolio | System MFA support | Read access |

### Required Documents

- [ ] ISMS-POL-A.5.17 - Authentication Information (approved)
- [ ] Asset inventory with system classification
- [ ] User population by department/role
- [ ] Current conditional access policies
- [ ] Prior MFA assessments (if applicable)
- [ ] MFA exception register entries

### Required Personnel

| Role | Responsibility | Time Commitment |
|------|----------------|-----------------|
| **Assessment Lead** | Coordinate assessment, document findings | 6-10 hours |
| **IAM Administrator** | Provide enrollment reports, policy exports | 4-6 hours |
| **Application Owners** | Confirm MFA support per application | 1-2 hours each |
| **Security Operations** | Provide bypass/failure monitoring evidence | 2-4 hours |
| **Internal Audit** | Independent validation | 4 hours |

---

## 1.4 Workbook Structure

### Sheet Overview

| Sheet | Purpose | Assessor Action |
|-------|---------|-----------------|
| **Instructions** | Guidance and methodology | Read before starting |
| **System_MFA_Inventory** | Systems requiring MFA | Populate with MFA status |
| **User_Enrollment** | User MFA registration status | Import from IdP |
| **Method_Analysis** | MFA methods in use | Document method distribution |
| **Conditional_Access** | IdP policies enforcing MFA | Document active policies |
| **Gap_Analysis** | Coverage gaps | Review and validate |
| **Remediation_Tracker** | Actions to address gaps | Plan and track |
| **Exception_Register** | Systems/users without MFA | Document with controls |
| **Approval_SignOff** | Assessment authorisation | Obtain signatures |

### Data Flow

```
Asset Inventory (A.5.9)          IdP Reports
        │                              │
        ▼                              ▼
System_MFA_Inventory ◄─────────► User_Enrollment
        │                              │
        ▼                              ▼
        └──────────► Method_Analysis ◄─┘
                           │
                           ▼
                   Conditional_Access
                           │
                           ▼
                     Gap_Analysis
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
        Remediation_Tracker   Exception_Register
                 │                   │
                 └─────────┬─────────┘
                           ▼
                   Approval_SignOff
```

---

## 1.5 Completion Walkthrough

### Step 1: Inventory Systems Requiring MFA

**Time allocation:** 2-3 hours

**Purpose:** Create a complete list of systems and their MFA requirements based on access category.

**Fields to Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| System_ID | From asset inventory | SYS-0042 |
| System_Name | Descriptive name | Azure Portal |
| Access_Category | Per policy classification | Privileged Access |
| MFA_Requirement | Required/Risk-Based/Not Required | Required |
| MFA_Enabled | Current state | Yes |
| MFA_Method | Method(s) in use | FIDO2, Authenticator |
| Enforcement | How enforced | Conditional Access |
| Owner | System owner | Cloud Team |
| Assessment_Status | Review state | Completed |

**Categorisation Rules:**

| System Characteristic | Access Category | MFA Requirement |
|-----------------------|-----------------|-----------------|
| Admin/management console | Privileged Access | Mandatory |
| Remote access (VPN, RDP) | Remote Access | Mandatory |
| Processes CONFIDENTIAL data | CONFIDENTIAL Systems | Mandatory |
| Internet-accessible | Internet-Facing | Mandatory |
| Internal corporate app | Standard Internal | Risk-based |
| Internal read-only tool | Standard Internal | Risk-based |

**Worked Example - System MFA Inventory:**

| System_ID | System_Name | Access_Category | MFA_Requirement | MFA_Enabled | MFA_Method |
|-----------|-------------|-----------------|-----------------|-------------|------------|
| SYS-0001 | Azure Portal | Privileged Access | Required | Yes | FIDO2, Authenticator |
| SYS-0002 | VPN Gateway | Remote Access | Required | Yes | Authenticator, Push |
| SYS-0003 | SAP ERP | CONFIDENTIAL | Required | Yes | Authenticator |
| SYS-0004 | Customer Portal | Internet-Facing | Required | Yes | Authenticator, Push |
| SYS-0005 | HR Intranet | Standard Internal | Risk-based | Yes | Authenticator |
| SYS-0006 | Print Server | Standard Internal | Risk-based | No | N/A |

### Step 2: Assess User Enrollment Status

**Time allocation:** 2-3 hours

**Purpose:** Determine MFA enrollment rates across the user population.

**Data Collection from IdP:**

For Azure AD:
1. Navigate to Azure AD > Security > Authentication methods > User registration details
2. Export registration details report
3. Navigate to Azure AD > Security > MFA > Per-user MFA
4. Export MFA status report

For Okta:
1. Navigate to Reports > System Log > Factor enrollment
2. Export factor enrollment status
3. Navigate to Security > Multifactor > Factor enrollment
4. Export enrollment summary

**Enrollment Status Categories:**

| Status | Definition | Action Required |
|--------|------------|-----------------|
| Enrolled - Active | MFA registered and used | None |
| Enrolled - Inactive | Registered but not used recently | Monitor |
| Not Enrolled - Required | Should have MFA but doesn't | Remediation |
| Not Enrolled - Exempt | Exception approved | Document |
| Not Applicable | Service account, no MFA required | Verify |

**Enrollment Analysis Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| User_ID | Employee ID or UPN | john.smith@org.com |
| Department | Organisational unit | Finance |
| Role_Category | User classification | Standard User |
| MFA_Required | Based on role/access | Yes |
| Enrollment_Status | Current state | Enrolled - Active |
| Method_Registered | MFA method(s) | Authenticator App |
| Last_MFA_Used | Date last authenticated | 03.02.2026 |
| Compliant | Meets requirements | Yes |

**Enrollment Metrics to Calculate:**

| Metric | Formula | Target |
|--------|---------|--------|
| Overall Enrollment Rate | (Enrolled / Required) × 100 | 100% |
| Privileged User Enrollment | (Enrolled Privileged / Total Privileged) × 100 | 100% |
| Active Usage Rate | (Used in 30 days / Enrolled) × 100 | >95% |
| Approved Method Rate | (Using approved / Enrolled) × 100 | 100% |

### Step 3: Analyze MFA Methods in Use

**Time allocation:** 1-2 hours

**Purpose:** Verify only approved MFA methods are deployed and identify deprecated methods.

**Method Distribution Analysis:**

| MFA Method | Approval Status | User Count | Percentage | Action |
|------------|-----------------|------------|------------|--------|
| FIDO2 Hardware Key | Approved - Preferred | 45 | 5% | Expand |
| Microsoft Authenticator | Approved | 720 | 80% | Maintain |
| Google Authenticator | Approved | 85 | 9% | Maintain |
| Push Notifications | Approved (with controls) | 650 | 72% | Verify fatigue controls |
| SMS OTP | Not Approved (new) | 35 | 4% | Migrate |
| Phone Call | Not Approved | 12 | 1% | Migrate |

**Method Risk Assessment:**

| Method | Phishing Resistance | Deployment Complexity | User Experience | Overall Rating |
|--------|---------------------|----------------------|-----------------|----------------|
| FIDO2 | High | Medium | Good | Excellent |
| Authenticator TOTP | Medium | Low | Good | Good |
| Push (with controls) | Medium | Low | Excellent | Good |
| Biometric (device) | High | Low | Excellent | Excellent |
| SMS OTP | Low | Low | Good | Poor |
| Phone Call | Low | Low | Fair | Poor |

### Step 4: Review Conditional Access Policies

**Time allocation:** 2-3 hours

**Purpose:** Document IdP policies that enforce MFA requirements.

**Policy Documentation Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Policy_ID | Identifier | CA-MFA-001 |
| Policy_Name | Descriptive name | Require MFA for Admin Portals |
| Scope_Users | Who it applies to | All administrators |
| Scope_Apps | Applications covered | Azure Portal, M365 Admin |
| Conditions | When triggered | Always |
| MFA_Requirement | Grant control | Require MFA |
| Status | Enabled/Disabled | Enabled |
| Last_Modified | Change date | 01.01.2026 |

**Required Policies per ISMS-POL-A.5.17:**

| Policy Coverage | Target Applications | Target Users | Expected |
|-----------------|---------------------|--------------|----------|
| Privileged Access | Admin portals, PAM | Administrators | MFA always |
| Remote Access | VPN, Remote Desktop | All remote users | MFA always |
| CONFIDENTIAL Systems | Apps with CONFIDENTIAL data | Users accessing | MFA always |
| Internet-Facing | External portals | External users | MFA always |
| Risky Sign-In | All applications | All users | MFA when risk detected |

**Worked Example - Conditional Access Inventory:**

| Policy_ID | Policy_Name | Scope_Apps | Scope_Users | MFA_Requirement |
|-----------|-------------|------------|-------------|-----------------|
| CA-MFA-001 | Admin Portal MFA | Azure Portal, AWS Console | Global Admins | Always |
| CA-MFA-002 | Remote Access MFA | VPN, RDP Gateway | All Users | Always |
| CA-MFA-003 | CONFIDENTIAL App MFA | SAP, HR System | App Users | Always |
| CA-MFA-004 | External Access MFA | Customer Portal | External Users | Always |
| CA-MFA-005 | Risky Sign-In MFA | All Cloud Apps | All Users | Medium+ Risk |

### Step 5: Identify and Document Gaps

**Time allocation:** 2-3 hours

**Purpose:** Consolidate all MFA coverage gaps for remediation or exception.

**Gap Categories:**

| Gap Type | Description | Example |
|----------|-------------|---------|
| System Gap | Required system lacks MFA | Legacy app without MFA support |
| User Gap | Required user not enrolled | New hire pending enrollment |
| Method Gap | User using deprecated method | User on SMS OTP |
| Policy Gap | No conditional access policy | App not covered by policy |
| Enforcement Gap | Policy exists but not enforcing | Policy in report-only mode |

**Gap Record Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Gap_ID | Unique identifier | GAP-MFA-2026-001 |
| Gap_Type | Category | System Gap |
| System_ID | Affected system | SYS-0099 |
| User_ID | Affected user (if applicable) | - |
| Description | Gap details | Legacy payroll lacks MFA support |
| Risk_Level | Impact assessment | High |
| Identified_Date | Discovery date | 03.02.2026 |
| Status | Current state | Open |

### Step 6: Create Remediation Plans

**Time allocation:** 2-3 hours

**Purpose:** Document actions to close identified gaps.

**Remediation Options by Gap Type:**

| Gap Type | Remediation Options |
|----------|---------------------|
| System Gap | Enable MFA, federate to IdP, replace system, exception with controls |
| User Gap | Enrollment campaign, forced registration, exception with justification |
| Method Gap | Migration campaign, disable deprecated method, grace period |
| Policy Gap | Create conditional access policy, update existing policy |
| Enforcement Gap | Enable policy, remove report-only mode |

**Remediation Plan Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Remediation_ID | Unique identifier | REM-MFA-2026-001 |
| Gap_ID | Related gap | GAP-MFA-2026-001 |
| Action | Specific steps | Federate legacy payroll to Azure AD |
| Owner | Responsible person | Application Owner |
| Target_Date | Deadline | 31.03.2026 |
| Status | Progress | In Progress |
| Completion_Date | When closed | - |
| Evidence_Ref | Proof of completion | - |

### Step 7: Document Exceptions

**Time allocation:** 1-2 hours

**Purpose:** For gaps that cannot be remediated, document exceptions with compensating controls.

**Exception Requirements:**

| System Category | Exception Allowed | Approval Required | Max Duration |
|-----------------|-------------------|-------------------|--------------|
| Privileged Access | No | N/A | N/A |
| Remote Access | No | N/A | N/A |
| CONFIDENTIAL | CISO only | CISO + Executive | 90 days |
| Internet-Facing | CISO only | CISO + Executive | 90 days |
| Standard Internal | Yes | CISO | 6 months |

**Required Compensating Controls for MFA Exceptions:**

| Control | Description | Evidence |
|---------|-------------|----------|
| Enhanced monitoring | All authentication logged and reviewed | SIEM alerts configured |
| IP restriction | Access limited to known locations | Firewall/proxy rules |
| Session limits | Reduced session duration | Application config |
| Additional approval | Manager approval for access | Workflow configured |
| Network segmentation | System isolated from sensitive data | Network diagram |

---

## 1.6 Evidence Collection

### Evidence Requirements

| Evidence Type | Source | Retention |
|---------------|--------|-----------|
| This assessment workbook | Generated | 7 years |
| IdP MFA configuration | Azure AD/Okta | 3 years |
| Enrollment reports | IdP exports | 3 years |
| Conditional access policies | IdP exports | 3 years |
| Method distribution reports | IdP reports | 3 years |
| Exception approvals | Email/workflow | Duration + 2 years |
| Remediation evidence | Change tickets | 3 years |

### Evidence Storage

**Primary Location:** `[SharePoint/Evidence Library]/A.5.17/MFA-Deployment/[Year]/`

**Folder Structure:**
```
A.5.17/
|-- MFA-Deployment/
|   |-- 2026/
|   |   |-- Assessment-Workbooks/
|   |   |   |-- ISMS-IMP-A.5.17.2_MFA_Deployment_20260203.xlsx
|   |   |-- Evidence/
|   |   |   |-- Enrollment-Reports/
|   |   |   |   |-- AzureAD-MFA-Enrollment-20260203.xlsx
|   |   |   |   |-- MFA-Registration-Details-20260203.pdf
|   |   |   |-- Conditional-Access/
|   |   |   |   |-- CA-Policy-Export-20260203.json
|   |   |   |   |-- CA-Policy-Screenshots/
|   |   |   |-- Method-Analysis/
|   |   |   |   |-- MFA-Method-Distribution-20260203.xlsx
|   |   |   |-- Exceptions/
|   |   |   |   |-- EXC-MFA-2026-001-Approval.pdf
|   |   |   |-- Approvals/
|   |   |   |   |-- CISO-SignOff-20260203.pdf
```

---

## 1.7 Common Pitfalls

Avoid these common mistakes when completing the MFA Deployment assessment:

### Coverage Assessment Pitfalls

❌ **MISTAKE**: Only checking cloud applications, missing on-premises systems
✅ **CORRECT**: Include VPN, on-premises applications, infrastructure management interfaces

❌ **MISTAKE**: Assuming federated apps automatically have MFA
✅ **CORRECT**: Verify conditional access policies actually require MFA for each application

❌ **MISTAKE**: Excluding service accounts from assessment
✅ **CORRECT**: Document all non-interactive accounts and verify alternative controls (certificates, managed identities)

### Enrollment Analysis Pitfalls

❌ **MISTAKE**: Counting users with MFA registered but never used
✅ **CORRECT**: Verify active usage - registration alone is insufficient

❌ **MISTAKE**: Including terminated users in enrollment calculations
✅ **CORRECT**: Filter to active users only for accurate enrollment rates

❌ **MISTAKE**: Not distinguishing between required and optional MFA users
✅ **CORRECT**: Segment analysis by access category and requirement level

### Method Compliance Pitfalls

❌ **MISTAKE**: Accepting SMS OTP as compliant for new deployments
✅ **CORRECT**: SMS is not approved for new enrollments per policy

❌ **MISTAKE**: Not checking for push notification fatigue controls
✅ **CORRECT**: Verify number matching or geographic context is enabled

❌ **MISTAKE**: Allowing backup methods that bypass primary MFA
✅ **CORRECT**: Ensure backup methods meet minimum security requirements

### Evidence Quality Pitfalls

❌ **MISTAKE**: Screenshots of policy names without policy details
✅ **CORRECT**: Export full policy configuration showing scope and controls

❌ **MISTAKE**: Enrollment percentages without user counts
✅ **CORRECT**: Include absolute numbers: "95% enrolled (950 of 1000 required users)"

---

## 1.8 Quality Checklist

Before submitting the assessment, verify:

### Coverage Checks

- [ ] All systems requiring MFA are inventoried
- [ ] Each system has MFA status documented
- [ ] User enrollment report covers all required users
- [ ] Conditional access policies documented for all required scenarios
- [ ] Service accounts documented with alternative controls

### Compliance Checks

- [ ] Privileged access has 100% MFA coverage
- [ ] Remote access has 100% MFA coverage
- [ ] CONFIDENTIAL systems have MFA coverage
- [ ] All MFA methods in use are approved methods
- [ ] Users on deprecated methods have migration plans

### Evidence Quality Checks

- [ ] IdP configuration exports are current (within 30 days)
- [ ] Enrollment reports include user counts and percentages
- [ ] Conditional access policies fully documented
- [ ] All gaps have remediation plans or exceptions
- [ ] Exceptions have documented compensating controls

### Documentation Accuracy Checks

- [ ] Access categories match ISMS-POL-A.5.17 definitions
- [ ] Enrollment metrics are calculated correctly
- [ ] Gap descriptions are specific and actionable
- [ ] Remediation timelines are realistic

---

## 1.9 Review and Approval

### Review Workflow

```
Assessment Lead Completes
        │
        ▼
Self-Review (Quality Checklist)
        │
        ▼
IAM Administrator Validates ──────► Return for Corrections
        │                                 │
        ▼                                 │
IT Security Review ───────────────► Return for Corrections
        │                                 │
        ▼                                 │
Internal Audit Validation ────────► Return for Corrections
        │                                 │
        ▼                                 │
CISO Final Approval ──────────────────────┘
        │
        ▼
   Assessment Complete
```

### Approval Signatures

1. **Assessment Lead Certification:**
   - Confirms methodology was followed
   - Confirms evidence accuracy
   - Date and signature

2. **IAM Administrator Validation:**
   - Confirms enrollment data accuracy
   - Confirms conditional access review complete
   - Date and signature

3. **CISO Approval:**
   - Approves overall MFA posture
   - Authorises exceptions (if any)
   - Date and signature

---

# PART II: TECHNICAL SPECIFICATION

---

## 2.1 Workbook Technical Details

### File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.17.2_MFA_Deployment_Assessment_YYYYMMDD.xlsx` |
| Generator | `generate_a517_2_mfa_deployment.py` |
| Sheets | 9 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 8 |
| 2 | System_MFA_Inventory | System MFA status | 200+ | 12 |
| 3 | User_Enrollment | User MFA status | 1000+ | 10 |
| 4 | Method_Analysis | MFA method distribution | 20 | 8 |
| 5 | Conditional_Access | IdP policies | 30+ | 10 |
| 6 | Gap_Analysis | Coverage gaps | 50+ | 10 |
| 7 | Remediation_Tracker | Fix tracking | 50+ | 10 |
| 8 | Exception_Register | Exceptions | 20+ | 12 |
| 9 | Approval_SignOff | Authorisation | 15 | 5 |

---

## 2.2 Sheet Specifications

### Sheet 2: System_MFA_Inventory

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | System_ID | 12 | Text | Required |
| B | System_Name | 30 | Text | Required |
| C | Access_Category | 20 | List | Privileged Access, Remote Access, CONFIDENTIAL, Internet-Facing, Standard Internal |
| D | MFA_Requirement | 15 | List | Required, Risk-Based, Not Required |
| E | MFA_Enabled | 10 | List | Yes, No, Partial |
| F | MFA_Method | 25 | Text | None |
| G | Enforcement | 20 | List | Conditional Access, Application Native, Manual, None |
| H | Compliant | 10 | Formula | Auto-calculated |
| I | Owner | 25 | Text | None |
| J | Last_Assessed | 15 | Date | None |
| K | Evidence_Ref | 25 | Text | None |
| L | Notes | 40 | Text | None |

### Sheet 3: User_Enrollment

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | User_ID | 30 | Text | Required |
| B | Display_Name | 25 | Text | None |
| C | Department | 20 | Text | None |
| D | Role_Category | 20 | List | Administrator, Privileged User, Standard User, External User |
| E | MFA_Required | 10 | List | Yes, No |
| F | Enrollment_Status | 20 | List | Enrolled - Active, Enrolled - Inactive, Not Enrolled - Required, Not Enrolled - Exempt |
| G | Method_Registered | 25 | Text | None |
| H | Last_MFA_Used | 15 | Date | None |
| I | Compliant | 10 | Formula | Auto-calculated |
| J | Notes | 40 | Text | None |

### Sheet 4: Method_Analysis

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | MFA_Method | 25 | Text | Pre-populated |
| B | Approval_Status | 20 | List | Approved - Preferred, Approved, Approved (with controls), Not Approved (legacy), Prohibited |
| C | User_Count | 12 | Number | Input |
| D | Percentage | 12 | Formula | Auto-calculated |
| E | Phishing_Resistant | 10 | List | Yes, No |
| F | Migration_Required | 10 | List | Yes, No |
| G | Migration_Deadline | 15 | Date | None |
| H | Notes | 40 | Text | None |

### Sheet 5: Conditional_Access

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Policy_ID | 15 | Text | None |
| B | Policy_Name | 35 | Text | None |
| C | Status | 12 | List | Enabled, Report-Only, Disabled |
| D | Scope_Users | 30 | Text | None |
| E | Scope_Apps | 30 | Text | None |
| F | Conditions | 30 | Text | None |
| G | MFA_Requirement | 20 | List | Require MFA, Require Compliant Device, Block, Allow |
| H | Last_Modified | 15 | Date | None |
| I | Evidence_Ref | 25 | Text | None |
| J | Notes | 40 | Text | None |

### Sheet 6: Gap_Analysis

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Gap_ID | 18 | Text | None |
| B | Gap_Type | 15 | List | System Gap, User Gap, Method Gap, Policy Gap, Enforcement Gap |
| C | System_ID | 12 | Text | None |
| D | User_ID | 30 | Text | None |
| E | Description | 50 | Text | None |
| F | Risk_Level | 12 | List | Critical, High, Medium, Low |
| G | Identified_Date | 15 | Date | None |
| H | Status | 15 | List | Open, Remediation Planned, Remediated, Exception |
| I | Remediation_ID | 18 | Text | None |
| J | Notes | 40 | Text | None |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| System_MFA_Inventory | D:D | ="Required" | Bold |
| System_MFA_Inventory | E:E | ="No" | Red fill (#FFC7CE) |
| System_MFA_Inventory | H:H | ="No" | Red fill (#FFC7CE), Bold |
| User_Enrollment | F:F | ="Not Enrolled - Required" | Red fill (#FFC7CE) |
| User_Enrollment | I:I | ="No" | Red fill (#FFC7CE) |
| Method_Analysis | B:B | ="Not Approved (legacy)" | Orange fill (#FABF8F) |
| Method_Analysis | B:B | ="Prohibited" | Red fill (#FFC7CE), Bold |
| Conditional_Access | C:C | ="Disabled" | Red fill (#FFC7CE) |
| Conditional_Access | C:C | ="Report-Only" | Yellow fill (#FFEB9C) |
| Gap_Analysis | F:F | ="Critical" | Red fill (#FFC7CE), Bold |
| Gap_Analysis | H:H | ="Open" | Red fill (#FFC7CE) |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| Azure AD / Entra ID | Enrollment reports, CA policies | IdP -> This workbook |
| Okta | Factor enrollment, policies | IdP -> This workbook |
| Asset Inventory (A.5.9) | System list | A.5.9 -> System_MFA_Inventory |
| A.5.17.1 Workbook | Password compliance | Bidirectional |
| A.5.17.3 Workbook | Credential lifecycle | Bidirectional |
| PAM Solution | Privileged account MFA | PAM -> User_Enrollment |
| SIEM | MFA bypass monitoring | SIEM -> Evidence |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.17 | Authentication Information | Parent policy |
| ISMS-IMP-A.5.17.1 | Password Policy Implementation | Password controls |
| ISMS-IMP-A.5.17.3 | Authentication Management Procedures | Credential lifecycle |
| ISMS-POL-A.8.2-3-5 | Authentication & Privileged Access | Privileged MFA |
| ISMS-IMP-A.5.15-16-18 | IAM Assessment | Identity management |

---

**END OF SPECIFICATION**

---

*"There are only two types of companies: those that have been hacked, and those that will be."*
— Robert Mueller

<!-- QA_VERIFIED: 2026-02-04 -->
