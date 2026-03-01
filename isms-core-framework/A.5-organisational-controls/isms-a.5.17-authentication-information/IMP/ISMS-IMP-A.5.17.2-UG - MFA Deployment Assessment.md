<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.17.2-UG:framework:UG:a.5.17.2 -->
**ISMS-IMP-A.5.17.2-UG - MFA Deployment Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.17: Authentication Information

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | MFA Deployment Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.17.2-UG |
| **Related Policy** | ISMS-POL-A.5.17 (Authentication Information) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.17 (Authentication Information) |
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

- ISMS-POL-A.5.17 (Authentication Information)
- ISMS-IMP-A.5.17.1 (Password Policy Implementation Guide)
- ISMS-IMP-A.5.17.3 (Authentication Management Procedures)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.17.2-TG.

---

### Workbook at a Glance

This workbook contains the following 9 sheets:

| Sheet | Purpose |
|-------|---------|
| **Instructions & Legend** | Assessment guidance, rating definitions, and field descriptions |
| **Allocation Process** | Credential allocation procedures and approval workflows |
| **Change Management** | Credential change and reset procedures and controls |
| **Recovery Process** | Credential recovery and emergency access procedures |
| **Revocation Process** | Credential revocation procedures for leavers and incidents |
| **Audit Log Requirements** | Audit logging requirements for credential lifecycle events |
| **Evidence Register** | Tracking of supporting evidence for audit purposes |
| **Summary Dashboard** | Compliance overview auto-populated from your input data |
| **Approval Sign-Off** | Stakeholder sign-off and approval workflow |

---

## Assessment Overview

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
| **Compliance** | Meets ISO 27001, NIST, PCI DSS v4.0.1, FINMA requirements |
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

## Control Requirements

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

## Prerequisites

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

## Completion Walkthrough

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

For Microsoft Entra ID (formerly Azure AD):
1. Navigate to Microsoft Entra ID (formerly Azure AD) > Security > Authentication methods > User registration details
2. Export registration details report
3. Navigate to Microsoft Entra ID (formerly Azure AD) > Security > MFA > Per-user MFA
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
| Action | Specific steps | Federate legacy payroll to Microsoft Entra ID (formerly Azure AD) |
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

## Evidence Collection

### Evidence Requirements

| Evidence Type | Source | Retention |
|---------------|--------|-----------|
| This assessment workbook | Generated | 7 years |
| IdP MFA configuration | Microsoft Entra ID (formerly Azure AD)/Okta | 3 years |
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

## Common Pitfalls

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

## Quality Checklist

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

## Review and Approval

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

**END OF USER GUIDE**

---

*"One lock is never enough."*
— Traditional locksmith saying

<!-- QA_VERIFIED: 2026-03-01 -->
