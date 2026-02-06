**ISMS-IMP-A.8.31.2-TG - Environment Access Control Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.31: Separation of Development, Test and Production Environments

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.31.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Environment Access Control & Production Access Restrictions |
| **Related Policy** | ISMS-POL-A.8.31, Section 2.2 (Environment Access Control Requirements) |
| **Purpose** | Document access control implementation, verify production access restrictions (zero developer access), and assess compliance with environment-specific access requirements |
| **Target Audience** | IAM Administrators, IT Operations, Security Engineers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Access Control Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Environment Access Control assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.31.2-UG.

---

# Technical Specification

## Workbook Structure

### Overview

The Environment Access Control Assessment workbook consists of 10 sheets:

1. **Instructions_Legend** - Metadata, instructions, status legend
2. **User_Environment_Access_Matrix** - All users with environment access and user → environment access mapping
3. **Developer_Production_Access** - CRITICAL: Zero developer production access check
4. **Production_Credential_Audit** - Production credential verification and PAM vault compliance
5. **Cross_Environment_Access_Log** - Tracking of cross-environment access requests and approvals
6. **Break_Glass_Access_Log** - Emergency access procedures and usage tracking
7. **MFA_Enforcement** - Multi-factor authentication compliance
8. **Access_Compliance_Scorecard** - Audit logging, access reviews, and compliance scoring
9. **Evidence_Register** - Supporting documentation inventory
10. **Approval_Sign_Off** - Multi-level approval workflow and signatures

---

## Sheet 1: Instructions & Legend

### Header Section

- **Row 1 (Merged A1:G1):** Title
  - Text: "ISMS-IMP-A.8.31.2 — Environment Access Control Assessment"
  - Style: Dark blue header (003366), white text, bold, centered, 40px height
  
- **Row 2 (Merged A2:G2):** Subtitle
  - Text: "ISO/IEC 27001:2022 - Control A.8.31: Separation of Development, Test and Production Environments"
  - Style: Medium blue header (4472C4), white text, centered, 30px height

### Document Information Block (Rows 4-12)

| Row | Column A (Label) | Column B (Value) | Column B Style |
|-----|------------------|------------------|----------------|
| 4 | Document ID: | ISMS-IMP-A.8.31.2 | Plain text |
| 5 | Assessment Area: | Environment Access Control & Production Restrictions | Plain text |
| 6 | Related Policy: | ISMS-POL-A.8.31, Section 2.2 | Plain text |
| 7 | Version: | 1.0 | Plain text |
| 8 | Assessment Date: | [USER INPUT] | Yellow fill (FFEB9C), bold |
| 9 | Completed By: | [USER INPUT] | Yellow fill (FFEB9C), bold |
| 10 | Organization: | [USER INPUT] | Yellow fill (FFEB9C), bold |
| 11 | Review Cycle: | Quarterly | Plain text |

**Column A:** Bold labels  
**Column B:** User input cells (rows 8-10) with yellow fill

### How to Use This Workbook (Rows 14-25)

- **Row 14:** "How to Use This Workbook" (bold, underlined)
- **Rows 15-25:** Numbered instructions (1-11)

```
1. PREREQUISITE: Complete ISMS-IMP-A.8.31.1 (Environment Architecture) FIRST
2. Export environment list from A.8.31.1, Sheet 2 (needed for access matrix)
3. Complete User_Inventory for ALL users (human + service accounts, including terminated)
4. Build Access_Matrix (user → environment access mapping)
5. Complete Production_Access_Verification (CRITICAL: verify zero developer access)
6. Verify MFA_Enforcement (mandatory for production)
7. Document BreakGlass_Emergency_Access (emergency procedures and usage)
8. Verify Access_Monitoring (audit logging, access reviews)
9. Complete Gap_Analysis for all non-compliance areas
10. Collect Evidence (IAM exports, audit logs, screenshots)
11. Obtain three-level approval (IAM Admin → Security → Executive)
```

### Critical Compliance Requirement (Rows 27-30)

- **Row 27:** "CRITICAL COMPLIANCE REQUIREMENT" (bold, red text, yellow background)
- **Row 28:** "ZERO DEVELOPER ACCESS TO PRODUCTION (except documented break-glass emergencies)"
- **Row 29:** "Developer production access = MAJOR AUDIT FINDING"
- **Row 30:** "Target: 0 developers with production access"

### Status Legend (Rows 32-38)

| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Compliant | Fully compliant with policy requirement | Green (C6EFCE) |
| ⚠️ | Partial | Partially compliant or compensating controls | Yellow (FFEB9C) |
| ❌ | Non-Compliant | Not compliant, remediation required | Red (FFC7CE) |
| 🔴 | MAJOR VIOLATION | Developer production access (immediate remediation) | Dark Red (8B0000) |
| 📋 | Planned | Remediation planned with target date | Blue (B4C7E7) |
| N/A | Not Applicable | Requirement not applicable | Gray (D9D9D9) |

### Acceptable Evidence (Rows 40-54)

- **Row 40:** "Acceptable Evidence (Examples)" (bold, underlined)
- **Rows 41-54:** Bulleted list with checkmarks

```
✓ IAM policy exports (AWS IAM, Azure RBAC, GCP IAM)
✓ User → group/role assignment exports
✓ Active Directory user lists with group memberships
✓ Production access restriction configurations
✓ MFA enforcement policy configurations
✓ MFA enrollment status per user
✓ Break-glass emergency access procedures
✓ Break-glass usage logs (last 90 days)
✓ Audit log configurations (CloudTrail, Azure Monitor, AD audit logs)
✓ Access review records (production access reviews)
✓ Access monitoring dashboards (SIEM alerts)
✓ Terminated user access verification (should be zero)
✓ Developer production access count (should be zero)
✓ Compliance violation remediation plans
```

---

## Sheet 2: User_Inventory

### Purpose
Document all users with access to ANY environment (human users + service accounts, including terminated users).

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:H1):** "USER INVENTORY"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:H2):** "Document ALL users with environment access - include human users, service accounts, and TERMINATED users"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | User ID / Username | 20 | Text |
| B | Full Name | 25 | Text |
| C | Job Title / Role | 25 | Dropdown |
| D | Department | 20 | Text |
| E | Account Type | 18 | Dropdown |
| F | Employment Status | 18 | Dropdown |
| G | Termination Date | 15 | Date |
| H | Notes | 40 | Text |

**Row 4 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column C: Job Title / Role**

- Developer
- Senior Developer
- Lead Developer
- QA Engineer / Tester
- DevOps Engineer
- Operations Engineer
- System Administrator
- Security Analyst
- Database Administrator
- Business Analyst
- Manager
- Service Account
- Other

**Column E: Account Type**

- Human (regular employee)
- Human (contractor)
- Service Account
- Break-Glass Account
- Shared Account (discouraged)

**Column F: Employment Status**

- Active
- Inactive (leave of absence)
- Terminated
- Contractor (active)
- Contractor (ended)

### Sample Data (Rows 5-10)

| User ID | Full Name | Job Title | Department | Account Type | Status | Termination Date | Notes |
|---------|-----------|-----------|------------|--------------|--------|------------------|-------|
| jdoe | John Doe | Senior Developer | Engineering | Human (employee) | Active | N/A | Full-stack developer |
| jsmith | Jane Smith | Operations Engineer | IT Operations | Human (employee) | Active | N/A | Production ops lead |
| tchen | Tom Chen | QA Engineer | Quality Assurance | Human (employee) | Active | N/A | Test automation |
| svc_backup | Backup Service | Service Account | IT Operations | Service Account | Active | N/A | Automated backup system |
| breakglass_001 | Emergency Access 001 | Break-Glass Account | Security | Break-Glass Account | Active | N/A | Emergency production access |
| bjones | Bob Jones | Developer | Engineering | Human (employee) | Terminated | 2023-12-15 | ⚠️ VERIFY ACCESS REMOVED |

### User Input Rows (11+)

Yellow-filled cells (FFEB9C) for user data entry.

**Critical Notes:**

- Include ALL users (active + terminated + service accounts)
- Terminated users should have ZERO access (verify in access matrix)
- Service accounts must be documented (non-human identities)
- Break-glass accounts tracked separately

---

## Sheet 3: Access_Matrix

### Purpose
Document user → environment access mapping (who can access which environments).

### Header Section (Rows 1-3)

- **Row 1 (Merged A1:J1):** "USER → ENVIRONMENT ACCESS MATRIX"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:J2):** "For each user, document access to EACH environment - verify via IAM system (do NOT assume)"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

- **Row 3:** "CRITICAL: Production column should show ZERO developers"
  - Style: Red background (FFC7CE), dark text, bold, centered, 25px height

### Column Headers (Row 5)

**Dynamic columns based on environments from A.8.31.1:**

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | User ID | 20 | Dropdown (from Sheet 2) |
| B | Full Name | 25 | Text (auto-populated from Sheet 2) |
| C | Job Title | 25 | Text (auto-populated from Sheet 2) |
| D | Development Access | 20 | Dropdown |
| E | Testing Access | 20 | Dropdown |
| F | Staging Access | 20 | Dropdown |
| G | Production Access | 20 | Dropdown |
| H | Production Access Justified? | 25 | Dropdown |
| I | Access Verification Method | 30 | Text |
| J | Last Verified Date | 15 | Date |

**NOTE**: Columns D-G are DYNAMIC based on environments from A.8.31.1, Sheet 2. Above shows standard 4-environment setup.

**Row 5 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

**Column G (Production Access) Special Formatting:**

- Header: Dark red background (8B0000), white text
- Cells with "Admin" or "Read-Write": Red fill (FFC7CE) - triggers production access verification

### Data Validation (Dropdowns)

**Columns D-G: Environment Access Level**

- ❌ None (no access)
- Read-Only
- Read-Write
- Admin (full control)
- Via Break-Glass Only

**Column H: Production Access Justified? (only if Column G ≠ None)**

- ✅ Yes (Operations/Support role)
- ❌ No (Developer role - VIOLATION)
- ⚠️ Break-Glass Only
- N/A (no production access)

### Sample Data (Rows 6-11)

| User ID | Full Name | Job Title | Development | Testing | Staging | Production | Prod Justified? | Verification | Last Verified |
|---------|-----------|-----------|-------------|---------|---------|------------|----------------|--------------|---------------|
| jdoe | John Doe | Senior Developer | Admin | Read-Write | Read-Only | ❌ None | N/A | AWS IAM policy review | 2024-01-20 |
| jsmith | Jane Smith | Operations Engineer | Read-Only | Read-Only | Admin | Admin (via PAM) | ✅ Yes (Operations) | AWS IAM policy review | 2024-01-20 |
| tchen | Tom Chen | QA Engineer | Read-Only | Admin | Read-Only | ❌ None | N/A | AWS IAM policy review | 2024-01-20 |
| svc_backup | Backup Service | Service Account | Read-Only | Read-Only | Read-Only | Read-Only | ✅ Yes (Backup) | AWS IAM policy review | 2024-01-20 |
| bjones | Bob Jones | Developer (TERMINATED) | ❌ VIOLATION: Read-Write | ❌ VIOLATION: Read-Only | ❌ None | ❌ None | N/A | AWS IAM user list | 2024-01-20 |

### Conditional Formatting Rules

**Production Access Column (Column G):**

- If value = "Admin" or "Read-Write" → Red fill (FFC7CE)
- If value = "Read-Only" AND Job Title contains "Developer" → Red fill (FFC7CE)
- If value = "❌ None" → Green fill (C6EFCE)

**Terminated Users:**

- If Employment Status (from Sheet 2) = "Terminated" AND any access column ≠ "❌ None" → Red fill (FFC7CE)

### Critical Verification

**After completing matrix:**
1. Filter Production Access column for any value except "❌ None"
2. For each user with production access, verify Job Title is Operations/Support
3. Count developers with production access → **TARGET: 0**

---

## Sheet 4: Production_Access_Verification

### Purpose
Verify zero developer production access (CRITICAL COMPLIANCE CHECK).

### Header Section (Rows 1-3)

- **Row 1 (Merged A1:H1):** "PRODUCTION ACCESS VERIFICATION"
  - Style: Dark red (8B0000), white text, bold, centered, 40px height
  
- **Row 2 (Merged A2:H2):** "CRITICAL: Zero developer access to production (except break-glass emergencies)"
  - Style: Light red (FFC7CE), dark text, bold, centered, 30px height

- **Row 3 (Merged A3:H3):** "List ALL users with production access - verify each is Operations/Support role"
  - Style: Light red (FFC7CE), dark text, centered, 25px height

### Summary Metrics (Rows 5-10)

| Row | Metric | Value Formula | Color Code |
|-----|--------|---------------|------------|
| 5 | **Total Users with Production Access:** | =COUNTA(A12:A1000)-1 | Bold |
| 6 | **Operations/Support Users (Compliant):** | =COUNTIF(F12:F1000,"✅ Yes") | Green if >0 |
| 7 | **Developers with Production Access:** | =COUNTIF(F12:F1000,"❌ No") | Red if >0 |
| 8 | **TARGET - Developers with Prod Access:** | 0 | Green |
| 9 | **ACTUAL - Developers with Prod Access:** | =COUNTIF(F12:F1000,"❌ No") | Red if >0, Green if =0 |
| 10 | **Compliance Status:** | =IF(COUNTIF(F12:F1000,"❌ No")=0,"✅ COMPLIANT","🔴 MAJOR VIOLATION") | Conditional |

### Column Headers (Row 12)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | User ID | 20 | Dropdown (from Sheet 2) |
| B | Full Name | 25 | Text (auto-populated) |
| C | Job Title | 25 | Text (auto-populated) |
| D | Production Access Level | 20 | Dropdown (from Sheet 3) |
| E | Access Method | 30 | Text |
| F | Operations/Support Role? | 22 | Dropdown |
| G | Compliance Status | 18 | Dropdown |
| H | Evidence | 35 | Text |

**Row 12 Style:** Dark red header (8B0000), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column D: Production Access Level**

- Admin (full control)
- Read-Write
- Read-Only
- Via Break-Glass Only

**Column F: Operations/Support Role?**

- ✅ Yes (Operations, SysAdmin, DBA, Security, Monitoring)
- ❌ No (Developer, QA, Business Analyst) - VIOLATION
- ⚠️ Service Account (acceptable if documented)

**Column G: Compliance Status**

- ✅ Compliant (Operations/Support role)
- 🔴 MAJOR VIOLATION (Developer with production access)
- ⚠️ Service Account (acceptable)
- ⚠️ Break-Glass Only (acceptable if monitored)

### Sample Data (Rows 13-17)

| User ID | Full Name | Job Title | Prod Access | Access Method | Ops/Support? | Compliance | Evidence |
|---------|-----------|-----------|-------------|---------------|--------------|------------|----------|
| jsmith | Jane Smith | Operations Engineer | Admin (via PAM) | AWS IAM role: ProdOpsAccess | ✅ Yes | ✅ Compliant | aws-iam-prod-policy.json |
| svc_monitoring | Monitoring Service | Service Account | Read-Only | AWS IAM role: MonitoringReadOnly | ⚠️ Service Account | ⚠️ Service Account | aws-iam-monitoring-policy.json |
| svc_backup | Backup Service | Service Account | Read-Only | AWS IAM role: BackupService | ⚠️ Service Account | ⚠️ Service Account | aws-iam-backup-policy.json |
| jdoe | John Doe | Senior Developer | Read-Only | AWS IAM role: DevReadOnly | ❌ No | 🔴 MAJOR VIOLATION | FINDING: Developer has production access |

### Critical Alerts

**If any row has Compliance Status = "🔴 MAJOR VIOLATION":**

- Entire row highlighted in red (FFC7CE)
- Alert icon in Summary Metrics (Row 9)
- Gap automatically created in Sheet 8 (Gap Analysis)

---

## Sheet 5: MFA_Enforcement

### Purpose
Verify MFA (Multi-Factor Authentication) is MANDATORY for production access.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:H1):** "MFA ENFORCEMENT VERIFICATION"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:H2):** "Verify MFA is MANDATORY (not optional) for ALL production access"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### MFA Policy Summary (Rows 4-8)

| Row | Attribute | Value | Notes |
|-----|-------|-------|-------|
| 4 | **MFA Required for Production?** | [USER INPUT: Yes/No] | Yellow cell |
| 5 | **MFA Policy Type:** | [USER INPUT: Mandatory/Optional/Recommended] | Yellow cell |
| 6 | **MFA Enforcement Method:** | [USER INPUT: IAM Policy/Conditional Access/Other] | Yellow cell |
| 7 | **MFA Bypass Possible?** | [USER INPUT: Yes/No/Unknown] | Yellow cell (Red if Yes) |
| 8 | **MFA Policy Evidence:** | [USER INPUT: File location] | Yellow cell |

### Column Headers (Row 10)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | User ID | 20 | Dropdown (from Sheet 4 - production users only) |
| B | Full Name | 25 | Text |
| C | Job Title | 25 | Text |
| D | MFA Enrolled? | 18 | Dropdown |
| E | MFA Device Type | 25 | Dropdown |
| F | MFA Required or Optional? | 22 | Dropdown |
| G | MFA Bypass Possible? | 20 | Dropdown |
| H | Compliance Status | 18 | Dropdown |
| I | Evidence | 30 | Text |

**Row 10 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column D: MFA Enrolled?**

- ✅ Yes (enrolled and active)
- ❌ No (not enrolled) - VIOLATION
- ⚠️ Pending (enrollment in progress)
- N/A (service account - alternative auth)

**Column E: MFA Device Type**

- Authenticator App (Google Authenticator, Microsoft Authenticator)
- Hardware Token (YubiKey, RSA SecurID)
- SMS (discouraged - phishing risk)
- Biometric (fingerprint, face recognition)
- API Key (service accounts only)
- N/A

**Column F: MFA Required or Optional?**

- ✅ Required (mandatory - cannot bypass)
- ⚠️ Optional (user can choose - VIOLATION)
- ⚠️ Recommended (not enforced - VIOLATION)
- N/A

**Column G: MFA Bypass Possible?**

- ❌ No (bypass blocked - correct)
- ⚠️ Yes (bypass allowed - VIOLATION)
- ⚠️ Unknown (needs testing)
- N/A

**Column H: Compliance Status**

- ✅ Compliant (MFA enrolled + required + no bypass)
- ❌ Non-Compliant (MFA not enrolled or optional or bypass possible)
- ⚠️ Service Account (alternative auth acceptable)
- 📋 Remediation Planned

### Sample Data (Rows 11-15)

| User ID | Full Name | Job Title | MFA Enrolled? | MFA Device | Required? | Bypass? | Compliance | Evidence |
|---------|-----------|-----------|---------------|------------|-----------|---------|------------|----------|
| jsmith | Jane Smith | Operations Engineer | ✅ Yes | Authenticator App | ✅ Required | ❌ No | ✅ Compliant | aws-mfa-enrollment.json |
| svc_monitoring | Monitoring Service | Service Account | N/A | API Key (rotated monthly) | N/A | N/A | ⚠️ Service Account | aws-api-key-rotation.log |
| jdoe | John Doe | Senior Developer | ❌ No | N/A | ⚠️ Optional | ⚠️ Yes | ❌ Non-Compliant | FINDING: Developer with prod access (from Sheet 4) |

### Critical Requirements

**For compliance:**

- [ ] MFA policy = "Mandatory" (not "Optional")
- [ ] MFA bypass = "No" (cannot be bypassed)
- [ ] All production users enrolled (except service accounts with alternative auth)

---

## Sheet 6: BreakGlass_Emergency_Access

### Purpose
Document break-glass emergency access procedures and usage tracking.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:H1):** "BREAK-GLASS EMERGENCY ACCESS"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:H2):** "Document emergency access procedures - usage should be RARE (monthly usage = process problem)"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Break-Glass Policy Summary (Rows 4-10)

| Row | Attribute | Value | Notes |
|-----|-------|-------|-------|
| 4 | **Break-Glass Procedure Documented?** | [USER INPUT: Yes/No] | Yellow cell |
| 5 | **Activation Approval Required?** | [USER INPUT: Yes/No/Who] | Yellow cell |
| 6 | **Time Limit (auto-revoke)?** | [USER INPUT: Hours] | Yellow cell |
| 7 | **Post-Incident Review Mandatory?** | [USER INPUT: Yes/No] | Yellow cell |
| 8 | **Break-Glass Usage (Last 90 days):** | [CALCULATED] | Auto-count from usage log |
| 9 | **Usage Frequency Assessment:** | [CALCULATED: Rare/Occasional/Frequent] | Green/Yellow/Red |
| 10 | **Break-Glass Procedure Document:** | [USER INPUT: File location] | Yellow cell |

### Break-Glass Accounts (Rows 12+)

**Column Headers (Row 12):**

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Account ID | 20 | Text |
| B | Account Purpose | 30 | Text |
| C | Authorized Approvers | 30 | Text (comma-separated) |
| D | Time Limit (hours) | 15 | Number |
| E | Auto-Revoke? | 15 | Dropdown |
| F | Last Used Date | 15 | Date |
| G | Usage Count (90 days) | 15 | Number |
| H | Status | 15 | Dropdown |

**Sample Data (Rows 13-15):**

| Account ID | Purpose | Authorized Approvers | Time Limit | Auto-Revoke | Last Used | Usage Count | Status |
|------------|---------|---------------------|------------|-------------|-----------|-------------|--------|
| breakglass_dev_001 | Emergency production fix (developers) | CISO, IT Ops Manager | 4 hours | ✅ Yes | 2024-01-10 | 1 | ✅ Active |
| breakglass_ops_001 | Emergency operations access | CISO | 8 hours | ✅ Yes | Never used | 0 | ✅ Active |

### Break-Glass Usage Log (Last 90 Days)

**Column Headers (Row 20):**

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Date/Time | 18 | DateTime |
| B | User (who activated) | 20 | Text |
| C | Break-Glass Account Used | 25 | Text |
| D | Duration (hours) | 15 | Number |
| E | Purpose / Incident | 40 | Text |
| F | Incident Ticket | 15 | Text |
| G | Post-Review Completed? | 20 | Dropdown |
| H | Review Date | 15 | Date |

**Sample Data (Rows 21-22):**

| Date/Time | User | Account | Duration | Purpose | Incident | Post-Review? | Review Date |
|-----------|------|---------|----------|---------|----------|--------------|-------------|
| 2024-01-10 14:23 | jdoe | breakglass_dev_001 | 2 hours | Critical production bug fix (payment API down) | INC-2024-001 | ✅ Yes | 2024-01-12 |

### Usage Frequency Assessment

**Formula for Row 9:**
```
=IF(H8=0,"✅ Rare (none)",IF(H8<=3,"✅ Rare (acceptable)",IF(H8<=10,"⚠️ Occasional (review needed)","❌ Frequent (process issue)")))
```

**Interpretation:**

- 0 uses: ✅ Rare (perfect - none needed)
- 1-3 uses: ✅ Rare (acceptable for emergencies)
- 4-10 uses: ⚠️ Occasional (review why so frequent)
- 11+ uses: ❌ Frequent (becoming routine - process issue)

---

## Sheet 7: Access_Monitoring

### Purpose
Verify audit logging and access review processes.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:I1):** "ACCESS MONITORING & AUDIT LOGGING"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:I2):** "Verify audit logging enabled, logs monitored, and access reviews performed regularly"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Environment | 18 | Dropdown (from A.8.31.1 Sheet 2) |
| B | Logging Enabled? | 18 | Dropdown |
| C | Events Logged | 40 | Text |
| D | Retention Period (days) | 18 | Number |
| E | Logs Monitored? | 18 | Dropdown |
| F | Monitoring Method | 30 | Text |
| G | Alerts Configured? | 18 | Dropdown |
| H | Access Review Frequency | 22 | Dropdown |
| I | Compliance Status | 18 | Dropdown |
| J | Evidence | 30 | Text |

**Row 4 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column B: Logging Enabled?**

- ✅ Yes (full logging)
- ⚠️ Partial (some events only)
- ❌ No (not enabled) - VIOLATION

**Column E: Logs Monitored?**

- ✅ Yes (automated + manual review)
- ⚠️ Partial (manual review only)
- ❌ No (collection only, no review) - VIOLATION

**Column G: Alerts Configured?**

- ✅ Yes (unauthorized access → alert)
- ⚠️ Partial (some alerts only)
- ❌ No (no alerts) - VIOLATION

**Column H: Access Review Frequency**

- Daily (production recommended)
- Weekly
- Monthly
- Quarterly
- ❌ None (no reviews) - VIOLATION

**Column I: Compliance Status**

- ✅ Compliant (logging + monitoring + alerts + reviews)
- ⚠️ Partial (missing some requirements)
- ❌ Non-Compliant (critical gaps)

### Sample Data (Rows 5-8)

| Environment | Logging? | Events | Retention | Monitored? | Method | Alerts? | Review Freq | Compliance | Evidence |
|-------------|----------|--------|-----------|------------|--------|---------|-------------|------------|----------|
| Production | ✅ Yes | Login, permission changes, resource access, failed attempts | 365 days | ✅ Yes | SIEM (Splunk) | ✅ Yes | Weekly | ✅ Compliant | cloudtrail-config.json |
| Staging | ✅ Yes | Login, permission changes | 90 days | ⚠️ Partial | Manual review | ❌ No | Monthly | ⚠️ Partial | cloudtrail-config.json |
| Testing | ✅ Yes | Login attempts only | 30 days | ❌ No | None | ❌ No | Quarterly | ⚠️ Partial | cloudtrail-config.json |
| Development | ⚠️ Partial | Login only | 7 days | ❌ No | None | ❌ No | None | ❌ Non-Compliant | FINDING: Inadequate logging |

### Critical Requirements (Production)

**Minimum requirements for production:**

- ✅ Logging enabled (full event logging)
- ✅ Retention ≥ 90 days (regulatory requirement)
- ✅ Logs monitored (automated + manual)
- ✅ Alerts configured (unauthorized access)
- ✅ Access reviews (minimum monthly, recommended weekly)

---

## Sheet 8: Gap_Analysis

### Purpose
Document all access control non-compliance areas, risk severity, and remediation plans.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:J1):** "GAP ANALYSIS & REMEDIATION PLANNING"
  - Style: Dark red (8B0000), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:J2):** "Document ALL access control gaps - prioritize by risk (developer production access = HIGH)"
  - Style: Light red (FFC7CE), dark text, bold, centered, 25px height

### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Gap ID | 10 | Text |
| B | Gap Description | 45 | Text |
| C | Policy Requirement Violated | 35 | Text |
| D | Risk Severity | 15 | Dropdown |
| E | Current Risk | 35 | Text |
| F | Proposed Remediation | 45 | Text |
| G | Estimated Effort (hours) | 15 | Number |
| H | Target Completion Date | 18 | Date |
| I | Assigned Owner | 20 | Text |
| J | Status | 15 | Dropdown |

**Row 4 Style:** Dark red header (8B0000), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column D: Risk Severity**

- 🔴 High (developer production access, MFA not mandatory, terminated user access)
- 🟡 Medium (audit logging gaps, excessive break-glass usage)
- 🟢 Low (documentation gaps, manual processes)
- ⚪ Info (awareness, no remediation)

**Column J: Status**

- 📋 Identified (not started)
- 🔄 In Progress (remediation underway)
- ✅ Remediated (completed, verified)
- ⏸️ On Hold (dependencies or approvals)
- ❌ Risk Accepted (executive decision)

### Sample Data (Rows 5-10)

| Gap ID | Description | Policy Violated | Severity | Current Risk | Remediation | Effort | Target Date | Owner | Status |
|--------|-------------|-----------------|----------|--------------|-------------|--------|-------------|-------|--------|
| GAP-001 | 1 developer (jdoe) has production read-only access | ISMS-POL-A.8.31, Section 2.2 | 🔴 High | Developer can view production data | Revoke production access, provide staging read-only instead | 2h | 2024-01-25 | IAM Admin | 🔄 In Progress |
| GAP-002 | Terminated user (bjones) still has dev/test access | ISMS-POL-A.8.31, Section 2.2 | 🔴 High | Former employee unauthorized access | Disable account immediately, review offboarding checklist | 1h | 2024-01-25 | IAM Admin | 📋 Identified |
| GAP-003 | MFA optional for production access (not mandatory) | ISMS-POL-A.8.31, Section 2.2 | 🔴 High | Production access without MFA possible | Change policy to mandatory, enforce via IAM policy | 8h | 2024-02-01 | Security Eng | 📋 Identified |
| GAP-004 | Break-glass used 12 times in last 90 days (frequent) | ISMS-POL-A.8.31, Section 2.5 | 🟡 Medium | Emergency access becoming routine | Implement read-only production troubleshooting access | 16h | 2024-03-15 | DevOps Lead | 📋 Identified |
| GAP-005 | Development environment audit logs only retained 7 days | ISMS-POL-A.8.31, Section 2.2 | 🟢 Low | Limited audit trail for dev environment | Increase retention to 90 days | 2h | 2024-04-30 | Security Eng | 📋 Identified |

### Gap Prioritization Matrix

| Severity | Examples | Remediation Timeline |
|----------|----------|---------------------|
| 🔴 High | Developer production access, terminated user access, MFA not mandatory | Immediate (within 30 days) |
| 🟡 Medium | Audit logging gaps, excessive break-glass usage, weak monitoring | Within 90 days |
| 🟢 Low | Documentation gaps, manual access reviews, short log retention | Within 180 days |

---

## Sheet 9: Evidence_Register

### Purpose
Central registry of all supporting evidence for audit traceability.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:H1):** "EVIDENCE REGISTER"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:H2):** "Document ALL supporting evidence - IAM exports, audit logs, screenshots, access review records"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Evidence ID | 12 | Text |
| B | Evidence Type | 20 | Dropdown |
| C | Description | 50 | Text |
| D | File Name | 35 | Text |
| E | Date Collected | 15 | Date |
| F | Related Requirement | 30 | Text |
| G | Related Sheet | 15 | Dropdown |
| H | File Location | 40 | Text |

**Row 4 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column B: Evidence Type**

- IAM Policy Export
- User List Export
- Access Assignment Export
- Screenshot
- Audit Log Export
- Access Review Record
- Break-Glass Procedure
- MFA Configuration
- Approval Record
- Other

**Column G: Related Sheet**

- Sheet 2: User_Inventory
- Sheet 3: Access_Matrix
- Sheet 4: Production_Access_Verification
- Sheet 5: MFA_Enforcement
- Sheet 6: BreakGlass_Emergency_Access
- Sheet 7: Access_Monitoring
- Sheet 8: Gap_Analysis
- Multiple Sheets

### Sample Data (Rows 5-15)

| Evidence ID | Type | Description | File Name | Date | Related Requirement | Sheet | Location |
|-------------|------|-------------|-----------|------|---------------------|-------|----------|
| EVD-001 | IAM Policy Export | AWS IAM production role policy | aws-iam-prod-policy-2024-01.json | 2024-01-20 | ISMS-POL-A.8.31, Section 2.2 | Sheet 4 | ./evidence/EVD-001/ |
| EVD-002 | User List Export | Complete AWS IAM user list | aws-iam-users-2024-01.json | 2024-01-20 | ISMS-POL-A.8.31, Section 2.2 | Sheet 2 | ./evidence/EVD-002/ |
| EVD-003 | Access Assignment Export | IAM role → user assignments | aws-iam-role-assignments-2024-01.csv | 2024-01-20 | ISMS-POL-A.8.31, Section 2.2 | Sheet 3 | ./evidence/EVD-003/ |
| EVD-004 | Screenshot | MFA enforcement policy configuration | mfa-policy-screenshot-2024-01.png | 2024-01-21 | ISMS-POL-A.8.31, Section 2.2 | Sheet 5 | ./evidence/EVD-004/ |
| EVD-005 | Break-Glass Procedure | Emergency access procedure document | breakglass-procedure-v1.2.pdf | 2024-01-22 | ISMS-POL-A.8.31, Section 2.5 | Sheet 6 | ./evidence/EVD-005/ |
| EVD-006 | Audit Log Export | Production access audit log (90 days) | cloudtrail-prod-access-2024-01.csv | 2024-01-22 | ISMS-POL-A.8.31, Section 2.2 | Sheet 7 | ./evidence/EVD-006/ |
| EVD-007 | Access Review Record | Production access review (January 2024) | prod-access-review-2024-01.xlsx | 2024-01-25 | ISMS-POL-A.8.31, Section 2.2 | Sheet 7 | ./evidence/EVD-007/ |
| EVD-008 | User List Export | Active Directory user list with groups | ad-users-groups-2024-01.csv | 2024-01-20 | ISMS-POL-A.8.31, Section 2.2 | Sheet 2, 3 | ./evidence/EVD-008/ |
| EVD-009 | MFA Configuration | Azure Conditional Access MFA policy | azure-ca-mfa-policy-2024-01.json | 2024-01-21 | ISMS-POL-A.8.31, Section 2.2 | Sheet 5 | ./evidence/EVD-009/ |
| EVD-010 | Approval Record | Access control assessment approval | assessment-approval-2024-01.pdf | 2024-01-28 | ISO 27001 audit requirement | Multiple | ./evidence/EVD-010/ |

### Evidence Organization

**Folder Structure:**
```
evidence/
├── EVD-001-aws-iam-prod-policy-2024-01.json
├── EVD-002-aws-iam-users-2024-01.json
├── EVD-003-aws-iam-role-assignments-2024-01.csv
├── EVD-004-mfa-policy-screenshot-2024-01.png
├── EVD-005-breakglass-procedure-v1.2.pdf
├── EVD-006-cloudtrail-prod-access-2024-01.csv
├── EVD-007-prod-access-review-2024-01.xlsx
├── EVD-008-ad-users-groups-2024-01.csv
├── EVD-009-azure-ca-mfa-policy-2024-01.json
└── EVD-010-assessment-approval-2024-01.pdf
```

**File Naming Convention:**
`[Evidence-ID]-[description]-[YYYY-MM].[extension]`

---

## Sheet 10: Approval_Sign_Off

### Purpose
Multi-level approval workflow and formal sign-off for the assessment.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:F1):** "APPROVAL & SIGN-OFF"
  - Style: Dark blue (003366), white text, bold, centered, 35px height

- **Row 2 (Merged A2:F2):** "Formal approval workflow - Assessment requires three-level approval before finalization"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Assessment Summary (Rows 4-11)

| Row | Attribute | Value |
|-----|-----------|-------|
| 4 | Assessment ID: | ISMS-IMP-A.8.31.2 |
| 5 | Assessment Name: | Environment Access Control Assessment |
| 6 | Assessment Date: | [From Sheet 1] |
| 7 | Completed By: | [From Sheet 1] |
| 8 | Total Users Assessed: | [Count from Sheet 2] |
| 9 | Developers with Production Access: | [Count from Sheet 3 - TARGET: 0] |
| 10 | Total Gaps Identified: | [Count from Sheet 8] |
| 11 | Overall Compliance Status: | [Summary status] |

### Critical Compliance Check (Rows 13-16)

**Row 13:** "CRITICAL COMPLIANCE VERIFICATION" (bold, red background)

| Check | Target | Actual | Status |
|-------|--------|--------|--------|
| Developer Production Access Count | 0 | [From Sheet 3] | [✅ if 0, 🔴 MAJOR VIOLATION if >0] |
| MFA Enforcement for Production | 100% | [From Sheet 7] | [✅/⚠️/❌] |
| Terminated Users with Access | 0 | [Calculated] | [✅ if 0, 🔴 VIOLATION if >0] |

### Approval Workflow (Rows 18-31)

**Level 1: Technical Review (Rows 20-23)**

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Reviewer Role | 25 | Text |
| B | Reviewer Name | 25 | Text (user input) |
| C | Review Date | 15 | Date (user input) |
| D | Decision | 15 | Dropdown |
| E | Comments | 50 | Text (user input) |
| F | Signature | 20 | Text (user input) |

**Dropdown for Decision:**
- Approved
- Approved with Comments
- Request Changes
- Rejected

**Level 1 Reviewers:**
| Role | Name | Date | Decision | Comments | Signature |
|------|------|------|----------|----------|-----------|
| IAM Administrator | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |
| Identity Management Lead | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |

**Level 2: Security Review (Rows 25-27)**

| Role | Name | Date | Decision | Comments | Signature |
|------|------|------|----------|----------|-----------|
| Information Security Manager | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |
| CISO | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |

**Level 3: Executive Approval (Rows 29-31)**

| Role | Name | Date | Decision | Comments | Signature |
|------|------|------|----------|----------|-----------|
| CTO / VP Engineering | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |

### Approval Status Summary (Rows 33-36)

| Metric | Value | Status |
|--------|-------|--------|
| Level 1 (Technical) Status | [Auto-calculated] | [✅/⚠️/❌] |
| Level 2 (Security) Status | [Auto-calculated] | [✅/⚠️/❌] |
| Level 3 (Executive) Status | [Auto-calculated] | [✅/⚠️/❌] |
| **Overall Approval Status** | [Auto-calculated] | [✅ Approved / ⚠️ Pending / ❌ Not Approved] |

### Conditional Approval Notes (Rows 38-44)

**Row 38:** "Conditional Approval Notes" (bold, underlined)

**Rows 39-44:** User input text area (yellow fill)
- Document any conditions attached to approval
- Document required follow-up actions for developer production access (if any violations)
- Document timeline for MFA enforcement completion
- Document terminated user access remediation

### Next Assessment Date (Rows 46-48)

| Attribute | Value |
|-----------|-------|
| Next Scheduled Assessment: | [User Input: Date] |
| Assessment Frequency: | Quarterly |
| Trigger-Based Review: | After joiner/mover/leaver events, access control changes |

---

## Cell Styling Reference

### Color Codes

| Style | Background | Font Color | Usage |
|-------|------------|------------|-------|
| Header (dark blue) | #003366 | White (#FFFFFF) | Sheet titles, major headers |
| Header (medium blue) | #4472C4 | White (#FFFFFF) | Column headers |
| Header (dark red) | #8B0000 | White (#FFFFFF) | Critical sheets (Production Access, Gaps) |
| Subheader (light blue) | #B4C7E7 | Dark (#000000) | Sheet instructions |
| Subheader (light red) | #FFC7CE | Dark (#000000) | Critical requirement warnings |
| User Input | #FFEB9C (yellow) | Dark (#000000) | Cells user must complete |
| Compliant | #C6EFCE (green) | Dark (#000000) | ✅ status |
| Partial | #FFEB9C (yellow) | Dark (#000000) | ⚠️ status |
| Non-Compliant | #FFC7CE (red) | Dark (#000000) | ❌ status |
| MAJOR VIOLATION | #8B0000 (dark red) | White (#FFFFFF) | 🔴 status (developer prod access) |
| Planned | #B4C7E7 (blue) | Dark (#000000) | 📋 status |
| Read-Only | #D9D9D9 (gray) | Dark (#000000) | Calculated or locked cells |

### Font Styles

| Element | Font | Size | Weight | Alignment |
|---------|------|------|--------|-----------|
| Sheet Title (Row 1) | Calibri | 18pt | Bold | Center |
| Subtitle (Row 2) | Calibri | 12pt | Regular | Center |
| Critical Warning (Row 3) | Calibri | 11pt | Bold | Center |
| Column Headers | Calibri | 11pt | Bold | Center |
| Data Cells | Calibri | 10pt | Regular | Left |
| User Input | Calibri | 10pt | Bold | Left |
| Summary Metrics | Calibri | 11pt | Bold | Left |

### Conditional Formatting Rules

**Sheet 3: Access_Matrix**

- Production Access column: Red fill if ≠ "❌ None" AND Job Title contains "Developer"
- Terminated users: Red fill if any access ≠ "❌ None"

**Sheet 4: Production_Access_Verification**

- Row 9 (Actual Developer Count): Red if >0, Green if =0
- Any row with "🔴 MAJOR VIOLATION": Entire row red fill

**Sheet 6: BreakGlass_Emergency_Access**

- Row 9 (Usage Frequency): Green if "Rare", Yellow if "Occasional", Red if "Frequent"

---

## Integration Points

### Input from Other Assessments

**From ISMS-IMP-A.8.31.1 (Environment Architecture):**

- Sheet 2: Environment_Inventory → Environment list
- Required for Access_Matrix (columns D-G are dynamic based on environments)

### Output to Other Assessments

**To ISMS-IMP-A.8.31.3 (Compliance Dashboard):**

- Sheet 4: Developer production access count (critical metric)
- Sheet 8: All gap data (for consolidated compliance scoring)
- Sheet 4, 5, 6, 7: Compliance status (for overall compliance score)

### Output to Python Scripts

**generate_a831_2_environment_access.py** generates this workbook:

- Creates all 9 sheets with proper structure
- Applies cell styling and conditional formatting
- Includes data validation and sample data
- Exports to `.xlsx` format

---

## Workbook Metadata

**File Name:** `A831-2-Environment-Access-Control-Assessment-YYYY-MM-DD.xlsx`

**Properties:**

- Title: ISMS-IMP-A.8.31.2 - Environment Access Control Assessment
- Subject: ISO/IEC 27001:2022 Control A.8.31
- Author: [Organization] ISMS Team
- Comments: Technology-agnostic environment access control assessment - ZERO DEVELOPER PRODUCTION ACCESS
- Keywords: ISO27001, A.8.31, access control, production access, IAM, RBAC, MFA

**Protection:**

- Sheet structure protected (prevent accidental deletion)
- User input cells unlocked (yellow cells editable)
- Formula cells locked (summary metrics, conditional formatting)
- Header rows locked

---

**END OF SPECIFICATION**

---

*"We should be careful to get out of an experience only the wisdom that is in it."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
