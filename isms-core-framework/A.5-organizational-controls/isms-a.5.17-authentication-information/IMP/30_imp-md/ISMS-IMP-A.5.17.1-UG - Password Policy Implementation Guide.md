**ISMS-IMP-A.5.17.1-UG - Password Policy Implementation Guide**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.17: Authentication Information

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.17.1-UG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.17 Authentication Information |
| **Parent Policy** | ISMS-POL-A.5.17 - Authentication Information |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.17.1-TG.

---

---

## Assessment Overview

### Purpose

This workbook provides a comprehensive Password Policy Implementation assessment framework that verifies password controls across all systems, documents configuration compliance, and tracks remediation for non-compliant systems.

The assessment serves multiple purposes:
- **Inventory**: Catalogue all systems requiring password authentication
- **Compliance Verification**: Confirm password configurations meet policy requirements
- **Gap Identification**: Identify systems with non-compliant password settings
- **Risk Management**: Prioritise remediation based on system criticality
- **Evidence**: Provide Stage 2 audit evidence of operational password controls

### Scope

The Password Policy Implementation Assessment covers:

| System Category | Examples | Password Requirements |
|-----------------|----------|----------------------|
| **Identity Providers** | Microsoft Entra ID (formerly Azure AD), Okta, on-premises AD | Central policy enforcement |
| **Enterprise Applications** | ERP, CRM, HRIS | Federated or local compliance |
| **Infrastructure** | Servers, network devices, databases | Service account and admin passwords |
| **Cloud Platforms** | AWS, Azure, GCP console access | IAM policy compliance |
| **Privileged Access** | PAM vault, break-glass accounts | Enhanced requirements per A.8.2-3-5 |
| **Service Accounts** | Batch jobs, integrations, APIs | Non-interactive password management |

**Inclusions:**
- All systems in the asset inventory (ISMS-POL-A.5.9) requiring password authentication
- Both user-interactive and service account passwords
- Local accounts on systems with federated identity
- Emergency/break-glass accounts

**Exclusions:**
- Systems using exclusively certificate-based authentication (covered by A.8.24)
- API keys and tokens (covered by ISMS-POL-A.8.24)
- Physical access PINs (covered by A.7.1-2-3)

### Business Value

| Value Area | Benefit |
|------------|---------|
| **Security Posture** | Consistent password strength reduces credential compromise risk by 70% |
| **Compliance** | Meets ISO 27001, PCI DSS v4.0.1, FINMA password requirements |
| **Operational Efficiency** | Centralised policy reduces password reset tickets |
| **Audit Readiness** | Documented evidence accelerates certification |
| **Risk Reduction** | Weak password elimination closes common attack vector |

### Assessment Frequency

| Assessment Type | Frequency | Trigger Events |
|-----------------|-----------|----------------|
| Full System Inventory | Annual | New systems, M&A activity |
| Configuration Compliance | Quarterly | Policy changes, audit findings |
| New System Assessment | Per deployment | System onboarding |
| Exception Review | Quarterly | Exception expiry, risk changes |
| Ad-hoc Review | As needed | Security incidents, audit requests |

---

## Control Requirements

### ISO 27001:2022 Control A.5.17

Per ISO/IEC 27001:2022 Control A.5.17:

> *"Allocation and management of authentication information should be controlled by a management process, including advising personnel on appropriate handling of authentication information."*

**Control Type:** Preventive
**Security Properties:** Confidentiality, Integrity
**Cybersecurity Concepts:** Protect, Identify
**Operational Capabilities:** Identity and Access Management

### Password Policy Requirements (from ISMS-POL-A.5.17)

| Requirement | Standard Systems | Privileged/Critical | Service Accounts |
|-------------|------------------|---------------------|------------------|
| **Minimum Length** | 12 characters | 16 characters | 24 characters |
| **Complexity** | 3 of 4 character types | 4 of 4 character types | Generated random |
| **Maximum Age** | 365 days | 90 days | Per event triggers |
| **History** | 12 passwords | 24 passwords | N/A |
| **Lockout Threshold** | 5 attempts | 3 attempts | N/A |
| **Lockout Duration** | 15 minutes | 30 minutes | N/A |

### What Auditors Look For

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Policy Existence** | Documented password policy in ISMS-POL-A.5.17 |
| **Technical Enforcement** | Configuration screenshots/exports from IdP and systems |
| **Coverage** | Inventory showing all systems assessed |
| **Exceptions** | Documented exceptions with compensating controls |
| **Monitoring** | Evidence of compliance tracking and remediation |
| **Training** | User awareness of password handling requirements |

---

## Prerequisites

### Required Access

| System | Purpose | Access Level Needed |
|--------|---------|---------------------|
| Identity Provider (Microsoft Entra ID (formerly Azure AD)/Okta/AD) | Password policy configuration | Admin or security reader |
| PAM Solution | Privileged account policies | Audit access |
| Enterprise Applications | Local password settings | Admin access per system |
| Asset Inventory | System list | Read access |
| SIEM/Audit Logs | Authentication events | Read access |

### Required Documents

- [ ] Current asset inventory (ISMS-POL-A.5.9 output)
- [ ] ISMS-POL-A.5.17 - Authentication Information (approved)
- [ ] IdP configuration documentation
- [ ] Application architecture diagrams showing authentication flows
- [ ] Prior password compliance assessments (if applicable)
- [ ] Exception register entries for password-related exceptions

### Required Personnel

| Role | Responsibility | Time Commitment |
|------|----------------|-----------------|
| **Assessment Lead** | Coordinate assessment, document findings | 8-12 hours |
| **IAM Administrator** | Provide IdP configuration evidence | 4-6 hours |
| **Application Owners** | Verify application password settings | 2-3 hours each |
| **Security Operations** | Provide monitoring/alerting evidence | 2-4 hours |
| **Internal Audit** | Independent validation | 4 hours |

---

## Completion Walkthrough

### Step 1: Populate System Inventory

**Time allocation:** 2-3 hours

**Purpose:** Create a complete list of systems requiring password authentication assessment.

**Fields to Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| System_ID | Unique identifier from asset inventory | SYS-0042 |
| System_Name | Descriptive name | Microsoft Entra ID (formerly Azure Active Directory) |
| System_Type | Category | Identity Provider |
| Criticality | Business impact rating | Critical |
| Auth_Method | Primary authentication | Password + MFA |
| Owner | System owner | IT Operations |
| Federated | Uses central IdP | Yes/No |
| Assessment_Status | Current state | Pending |

**Data Sources:**
- Asset inventory (ISMS-IMP-A.5.9 workbook)
- Application portfolio
- Infrastructure inventory
- Cloud resource lists

**Worked Example - System Inventory:**

| System_ID | System_Name | System_Type | Criticality | Auth_Method | Federated |
|-----------|-------------|-------------|-------------|-------------|-----------|
| SYS-0001 | Microsoft Entra ID (formerly Azure AD) | Identity Provider | Critical | Password + MFA | N/A |
| SYS-0002 | SAP ERP | Enterprise App | Critical | Password | Yes |
| SYS-0003 | VMware vCenter | Infrastructure | High | Password + MFA | No |
| SYS-0004 | AWS Console | Cloud Platform | Critical | Password + MFA | Yes |
| SYS-0005 | PostgreSQL Prod | Database | Critical | Password | No |

### Step 2: Assess Identity Provider Configuration

**Time allocation:** 2-3 hours

**Purpose:** Verify central identity provider enforces password policy requirements.

**Assessment Points:**

| Setting | Policy Requirement | Where to Find | Evidence |
|---------|-------------------|---------------|----------|
| Minimum length | 12 characters | Password policy settings | Screenshot |
| Complexity | 3 of 4 types | Password policy settings | Screenshot |
| Maximum age | 365 days | Password policy settings | Screenshot |
| History | 12 passwords | Password policy settings | Screenshot |
| Lockout threshold | 5 attempts | Account lockout policy | Screenshot |
| Lockout duration | 15 minutes | Account lockout policy | Screenshot |

**Microsoft Entra ID (formerly Azure AD) Example:**

1. Navigate to Microsoft Entra ID (formerly Azure AD) > Security > Authentication methods > Password protection
2. Capture settings for: Custom banned passwords, Lockout threshold, Lockout duration
3. Navigate to Microsoft Entra ID (formerly Azure AD) > Users > Password reset > Authentication methods
4. Capture password complexity and length requirements
5. Export conditional access policies affecting password requirements

**On-Premises AD Example:**

1. Open Group Policy Management
2. Navigate to Default Domain Policy > Computer Configuration > Policies > Windows Settings > Security Settings > Account Policies
3. Document Password Policy and Account Lockout Policy settings
4. Export GPO report as HTML or XML evidence

### Step 3: Assess Federated Applications

**Time allocation:** 3-4 hours

**Purpose:** Verify applications using central IdP inherit password policy.

**Assessment Points:**

| Check | Verification Method | Pass Criteria |
|-------|---------------------|---------------|
| SSO configured | Application settings | SAML/OIDC enabled |
| No local passwords | Admin verification | Local auth disabled |
| MFA enforced | Conditional access | MFA required for app |
| Session management | Application config | Appropriate timeout |

**For Each Federated Application:**

1. Confirm SSO/federation is active
2. Verify no local password authentication exists
3. Check conditional access policies include the application
4. Document session timeout settings
5. Record evidence (screenshots, config exports)

### Step 4: Assess Non-Federated Systems

**Time allocation:** 4-6 hours

**Purpose:** Verify systems with local authentication meet password requirements.

**Common System Types and Assessment Methods:**

| System Type | Assessment Method | Evidence Required |
|-------------|-------------------|-------------------|
| Linux Servers | /etc/login.defs, PAM config | Config file exports |
| Windows Servers | Local Security Policy or GPO | GPO report or screenshot |
| Network Devices | Running config | Sanitised config export |
| Databases | Database security settings | Settings export/screenshot |
| Legacy Applications | Application configuration | Admin screenshots |

**Linux Server Example:**

```bash
# Document password aging settings
cat /etc/login.defs | grep -E "PASS_MAX_DAYS|PASS_MIN_DAYS|PASS_MIN_LEN|PASS_WARN_AGE"

# Document PAM password requirements
cat /etc/pam.d/common-password
cat /etc/security/pwquality.conf
```

**Database Example (PostgreSQL):**

```sql
-- Check password encryption
SHOW password_encryption;

-- Review pg_hba.conf for authentication methods
-- Review password validation extensions (passwordcheck)
```

### Step 5: Assess Service Accounts

**Time allocation:** 2-3 hours

**Purpose:** Verify service account password management meets enhanced requirements.

**Service Account Requirements:**

| Requirement | Standard | Evidence |
|-------------|----------|----------|
| Password length | 24+ characters | PAM/vault config |
| Generated random | Yes | Creation procedure |
| Stored in vault | Yes | PAM inventory |
| Rotation | Per event triggers | Rotation logs |
| No interactive login | Where possible | Account settings |

**Assessment Points:**

1. List all service accounts from privileged access inventory
2. Verify each is stored in approved credential vault
3. Check rotation history matches policy triggers
4. Verify interactive login is disabled where appropriate
5. Document exceptions with justification

### Step 6: Document Gaps and Plan Remediation

**Time allocation:** 2-3 hours

**Purpose:** Consolidate non-compliance findings and create remediation plans.

**Gap Record Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Gap_ID | Unique identifier | GAP-PW-2026-001 |
| System_ID | Affected system | SYS-0003 |
| System_Name | System name | VMware vCenter |
| Requirement | Policy requirement violated | Minimum length |
| Current_State | Actual configuration | 8 characters |
| Required_State | Policy requirement | 12 characters |
| Risk_Level | Impact rating | High |
| Remediation_Action | Planned fix | Update password policy |
| Owner | Responsible person | VMware Admin |
| Target_Date | Deadline | 28.02.2026 |

**Remediation Priority:**

| Risk Level | SLA | Escalation |
|------------|-----|------------|
| Critical | 7 days | CISO, Executive |
| High | 30 days | CISO |
| Medium | 60 days | IT Security Manager |
| Low | 90 days | Security Team |

### Step 7: Document Exceptions

**Time allocation:** 1-2 hours

**Purpose:** For systems that cannot meet password requirements, document exceptions with compensating controls.

**Valid Exception Scenarios:**

| Scenario | Justification | Required Compensating Controls |
|----------|---------------|--------------------------------|
| Legacy system | Vendor limitation | Network isolation, enhanced monitoring, MFA |
| Third-party SaaS | Cannot configure | Contractual requirement, SSO if possible |
| Embedded device | Hardware limitation | Network segmentation, physical security |
| OT/ICS system | Operational constraint | Air-gapped, physical access control |

**Exception Record Requirements:**

| Field | Description |
|-------|-------------|
| Exception_ID | Unique identifier |
| System_ID | Affected system |
| Requirement | Policy requirement exempted |
| Justification | Business/technical reason |
| Compensating_Controls | Alternative protections |
| Risk_Acceptance | Approver (CISO required for Critical systems) |
| Expiry_Date | Maximum 6 months |
| Review_Frequency | Quarterly minimum |

---

## Evidence Collection

### Evidence Requirements

| Evidence Type | Source | Retention |
|---------------|--------|-----------|
| This assessment workbook | Generated | 7 years |
| IdP configuration exports | Microsoft Entra ID (formerly Azure AD)/Okta/AD | 3 years |
| System configuration screenshots | Various systems | 3 years |
| GPO/policy reports | Active Directory | 3 years |
| Exception approvals | Email/workflow | Duration + 2 years |
| Remediation completion evidence | Change tickets | 3 years |
| Compliance reports | PAM/IAM tools | 3 years |

### Evidence Storage

**Primary Location:** `[SharePoint/Evidence Library]/A.5.17/Password-Policy/[Year]/`

**Folder Structure:**
```
A.5.17/
|-- Password-Policy/
|   |-- 2026/
|   |   |-- Assessment-Workbooks/
|   |   |   |-- ISMS-IMP-A.5.17.1_Password_Policy_20260203.xlsx
|   |   |-- Evidence/
|   |   |   |-- IdP-Configuration/
|   |   |   |   |-- AzureAD-Password-Policy-20260203.pdf
|   |   |   |   |-- AD-GPO-Report-20260203.html
|   |   |   |-- System-Assessments/
|   |   |   |   |-- SYS-0001-AzureAD/
|   |   |   |   |-- SYS-0003-vCenter/
|   |   |   |   |-- SYS-0005-PostgreSQL/
|   |   |   |-- Exceptions/
|   |   |   |   |-- EXC-PW-2026-001-Approval.pdf
|   |   |   |-- Remediation/
|   |   |   |   |-- GAP-PW-2026-001-Closure.pdf
|   |   |   |-- Approvals/
|   |   |   |   |-- CISO-SignOff-20260203.pdf
```

**Naming Convention:**
```
EVD-A.5.17.1_[SystemID]_[EvidenceType]_[YYYYMMDD].[ext]
```

---

## Common Pitfalls

Avoid these common mistakes when completing the Password Policy assessment:

### Inventory Completeness Pitfalls

❌ **MISTAKE**: Only assessing enterprise applications, missing infrastructure systems
✅ **CORRECT**: Include all systems: network devices, databases, hypervisors, storage arrays, and OT systems

❌ **MISTAKE**: Assuming federated applications have no local accounts
✅ **CORRECT**: Verify no local admin or emergency accounts exist with separate passwords

❌ **MISTAKE**: Forgetting service accounts and non-interactive accounts
✅ **CORRECT**: Include all service accounts, batch job accounts, and API accounts in scope

### Configuration Assessment Pitfalls

❌ **MISTAKE**: Accepting verbal confirmation of password settings
✅ **CORRECT**: Always capture configuration evidence (screenshots, exports, config files)

❌ **MISTAKE**: Checking only default/global password policy
✅ **CORRECT**: Verify no override policies exist for specific user groups or OUs

❌ **MISTAKE**: Assuming cloud platforms inherit on-premises settings
✅ **CORRECT**: Assess each cloud platform's IAM password policy independently

### Evidence Quality Pitfalls

❌ **MISTAKE**: Screenshots without timestamps or system identification
✅ **CORRECT**: Include system name, date, and assessor in all evidence

❌ **MISTAKE**: Storing passwords or sensitive credentials in evidence
✅ **CORRECT**: Redact any visible passwords; document settings only

❌ **MISTAKE**: Generic "compliant" without specific configuration values
✅ **CORRECT**: Document actual values: "Minimum length: 12 (meets requirement of 12)"

### Exception Handling Pitfalls

❌ **MISTAKE**: Approving exceptions without compensating controls
✅ **CORRECT**: Every exception requires documented compensating controls

❌ **MISTAKE**: Permanent exceptions for temporary limitations
✅ **CORRECT**: All exceptions expire within 6 months and require renewal

---

## Quality Checklist

Before submitting the assessment, verify:

### Completeness Checks

- [ ] All systems from asset inventory are assessed or explicitly excluded with rationale
- [ ] Identity provider(s) configuration fully documented
- [ ] Each federated application verified for SSO and no local passwords
- [ ] Each non-federated system has configuration evidence
- [ ] Service accounts documented with storage and rotation evidence
- [ ] All gaps have remediation plans with owners and dates
- [ ] All exceptions have compensating controls and approvals

### Evidence Quality Checks

- [ ] All screenshots include system name and date
- [ ] Configuration exports are complete and current
- [ ] No sensitive credentials visible in evidence
- [ ] Evidence naming follows convention
- [ ] Evidence stored in correct folder structure

### Documentation Accuracy Checks

- [ ] System inventory matches asset register
- [ ] Policy requirements match ISMS-POL-A.5.17
- [ ] Gap descriptions accurately reflect non-compliance
- [ ] Remediation actions are specific and actionable
- [ ] Exception justifications are valid business/technical reasons

### Approval Readiness Checks

- [ ] All mandatory fields completed
- [ ] No pending items blocking approval
- [ ] Internal review completed
- [ ] Evidence package ready for audit

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
        │
        ▼
   Upload to ISMS Evidence Library
```

### Approval Signatures

The Approval_SignOff sheet requires:

1. **Assessment Lead Certification:**
   - Confirms methodology was followed
   - Confirms all systems assessed
   - Date and signature

2. **IAM Administrator Validation:**
   - Confirms IdP configuration accuracy
   - Confirms federated application list complete
   - Date and signature

3. **IT Security Review:**
   - Confirms gap analysis accuracy
   - Confirms remediation plans appropriate
   - Date and signature

4. **CISO Approval:**
   - Approves overall assessment
   - Authorises exceptions (if any)
   - Date and signature

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
