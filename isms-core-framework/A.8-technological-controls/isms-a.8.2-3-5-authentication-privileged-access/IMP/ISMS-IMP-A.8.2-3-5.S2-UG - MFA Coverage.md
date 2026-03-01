<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.2-3-5.S2-UG:framework:UG:a.8.2-3-5 -->
**ISMS-IMP-A.8.2-3-5.S2-UG - MFA Coverage Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | MFA Coverage |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.2-3-5.S2-UG |
| **Related Policy** | ISMS-POL-A.8.2-3-5 (Authentication Privileged Access) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.2 (Privileged Access Rights) |
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

- ISMS-POL-A.8.2-3-5 (Authentication Privileged Access)
- ISMS-IMP-A.8.2-3-5.S1 (Authentication Inventory)
- ISMS-IMP-A.8.2-3-5.S3 (Privileged Accounts)
- ISMS-IMP-A.8.2-3-5.S4 (Privileged Monitoring)
- ISMS-IMP-A.8.2-3-5.S5 (Access Restrictions)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.2-3-5.S2-TG.

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | User MFA Enrollment | Track MFA enrollment status per user |
| 3 | MFA Coverage By Type | Analyse MFA coverage across user types and roles |
| 4 | MFA Method Analysis | Assess the security of MFA methods in use |
| 5 | MFA Gaps Priority | Prioritise gaps in MFA deployment for remediation |
| 6 | Enrollment Campaign | Track MFA enrollment campaign progress |
| 7 | Backup Method Status | Document backup authentication method availability |
| 8 | Evidence Register | Store and reference evidence supporting assessments |
| 9 | Summary Dashboard | Compliance status and key metrics overview |
| 10 | Approval Sign-Off | Management review sign-off and certification |

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.2-3-5.2 - MFA Coverage Assessment

**What This Assessment Does:**

- Tracks MFA enrollment status for ALL users (employees, contractors, vendors, service accounts)
- Measures MFA coverage by user type (privileged, standard, remote, contractors)
- Identifies MFA gaps (users without MFA, high-priority gaps)
- Monitors MFA enrollment trends over time
- Verifies compliance with NIS2 Article 21(2)(e) if applicable (mandatory MFA for essential/important entities)
- Tracks MFA method distribution (authenticator app, hardware token, SMS, biometric)

**What This Assessment Does NOT Do:**

- Inventory authentication mechanisms per system (see IMP.1 - Authentication Inventory)
- Track privileged account details (see IMP.3 - Privileged Account Inventory)
- Test MFA effectiveness (penetration testing is separate)

**Primary ISO 27001 Control:** A.8.5 - Secure Authentication

**Related Controls:**

- A.8.2 - Privileged Access Rights (MFA mandatory for privileged users)
- A.5.16 - Identity Management (user inventory foundation)

**Regulatory Drivers:**

- **NIS2 Article 21(2)(e)**: MANDATORY MFA for essential/important entities (if applicable)
- **FINMA Margin 56**: MFA for critical systems access (if Swiss financial institution)
- **DORA Article 9(3)**: Strong authentication mechanisms (if EU financial entity)
- **GDPR Article 32**: MFA as appropriate security measure

## When to Use This Assessment

**Use this assessment when:**

- Deploying MFA organisation-wide (track rollout progress)
- Monthly MFA enrollment tracking (new hires, enrollment status changes)
- Quarterly compliance reporting (MFA coverage metrics)
- Preparing for ISO 27001 certification audits
- Demonstrating NIS2 compliance (if applicable)
- Investigating authentication security incidents
- Executive reporting (MFA deployment KPIs)

**Assessment Frequency:**

- **Monthly**: MFA enrollment updates, new user onboarding, enrollment gap tracking
- **Quarterly**: Comprehensive coverage analysis, compliance reporting, trend analysis
- **Annual**: Deep assessment, MFA effectiveness testing, policy compliance verification

## Who Completes This Assessment

**Primary Responsibility:** Security Team (MFA deployment lead) + IAM Team

**Supporting Roles:**

- **IT Operations**: MFA platform administration, user enrollment support
- **HR**: User type classification (employee, contractor, temporary)
- **Managers**: Privileged user identification, approval of exceptions
- **Help Desk**: MFA troubleshooting, device replacement

**Approval Authority:** Chief Information Security Officer (CISO)

## Expected Time Investment

**Initial Assessment** (first MFA rollout):

- User data export from identity provider: 30-60 minutes
- MFA enrollment status collection: 1-2 hours
- Workbook completion: 1-2 hours
- Gap analysis: 30-60 minutes
- **Total**: 3-6 hours

**Monthly Updates** (ongoing enrollment tracking):

- User data refresh: 15-30 minutes
- Enrollment status update: 30-45 minutes
- Gap analysis update: 15-30 minutes
- **Total**: 1-2 hours per month

**Quarterly Comprehensive Review**:

- Full enrollment validation: 1-2 hours
- Trend analysis: 30-60 minutes
- Compliance reporting: 1 hour
- **Total**: 3-4 hours per quarter

---

# Prerequisites

## Required Information

Before starting the assessment, gather the following information:

**User Inventory:**

- [ ] Complete user list from identity provider (Entra ID, Okta, Active Directory)
- [ ] User type classification (employee, contractor, vendor, service account)
- [ ] User role classification (privileged, standard, remote access, confidential data access)
- [ ] User manager/department information

**MFA Enrollment Data:**

- [ ] MFA enrollment status per user (enrolled, not enrolled, exempt)
- [ ] MFA method per user (authenticator app, hardware token, SMS, biometric, push notification)
- [ ] MFA enrollment date per user
- [ ] Backup MFA method registered (yes/no)

**MFA Platform Details:**

- [ ] MFA platform in use (Azure MFA, Okta MFA, Duo, Google Authenticator, etc.)
- [ ] MFA methods supported (TOTP, FIDO2, SMS, biometric, etc.)
- [ ] MFA enforcement policies (who is required to have MFA)

**Regulatory Requirements:**

- [ ] NIS2 applicability status (essential entity, important entity, not applicable)
- [ ] FINMA applicability (Swiss financial institution license holder)
- [ ] DORA applicability (EU financial entity)

## Required Access

**System Access Needed:**

- [ ] Read access to identity provider (Entra ID, Okta admin console)
- [ ] Read access to MFA platform (MFA enrollment reports)
- [ ] Read access to HR system (user type, manager, department)
- [ ] Optional: SIEM access (MFA authentication logs for usage analysis)

**People Access Needed:**

- [ ] HR team (for user classification verification)
- [ ] Managers (for privileged user identification)
- [ ] Help Desk (for MFA enrollment support statistics)

## Required Tools

**Software:**

- [ ] Microsoft Excel 2016 or later
- [ ] Python 3.8+ (if using automated workbook generation)
- [ ] PowerShell / Azure CLI / Okta API (for automated data collection)

**Identity Provider Reports:**

- [ ] Entra ID: "MFA Registration Details" report
- [ ] Okta: "MFA Enrollment Report"
- [ ] Google Workspace: "2-Step Verification Enrollment"

---

# Assessment Workflow

## Assessment Process Overview

```
1. PREPARE
   → Export user list from identity provider
   → Export MFA enrollment status
   → Classify users by type and role
   → Generate workbook (Python script or Excel template)

2. COLLECT DATA
   → Sheet 1: User MFA Enrollment Status

      - User ID, Name, Type, Role, MFA Enrolled, MFA Method

   → Sheet 2: MFA Coverage by User Type

      - Privileged users, Standard users, Remote access, Contractors

   → Sheet 3: MFA Gap Analysis

      - Users without MFA, High-priority gaps, Remediation timeline

3. ANALYZE & SCORE
   → Calculate MFA coverage percentages
   → Identify critical gaps (privileged users without MFA)
   → Track enrollment trends (month-over-month)

4. COLLECT EVIDENCE
   → Screenshot MFA enrollment reports
   → Export identity provider MFA data
   → Document MFA enforcement policies

5. REVIEW & APPROVE
   → Security Team review (data accuracy)
   → IAM Team validation (enrollment status correct)
   → CISO approval (coverage targets met)

6. REMEDIATE GAPS
   → Enroll users without MFA
   → Address MFA exemptions
   → Track remediation progress
```

## Step-by-Step Completion Guide

**Step 1: Export User Data**

**Entra ID (Microsoft Graph PowerShell):**
```powershell
# Connect to Microsoft Graph with required scopes
Connect-MgGraph -Scopes "User.Read.All", "UserAuthenticationMethod.Read.All"

# Export all users with MFA status
Get-MgUser -All | ForEach-Object {
    $methods = Get-MgUserAuthenticationMethod -UserId $_.Id
    [PSCustomObject]@{
        UserPrincipalName = $_.UserPrincipalName
        DisplayName = $_.DisplayName
        MFAMethods = ($methods | Measure-Object).Count
        MFAEnabled = ($methods | Measure-Object).Count -gt 1
    }
} | Export-Csv -Path "EntraID_MFA_Status.csv" -NoTypeInformation
```

**Okta:**
```bash
# Use Okta API to get MFA enrollment
curl -X GET "https://your-domain.okta.com/api/v1/users?limit=200" \
  -H "Authorisation: SSWS your-api-token" \
  -H "Accept: application/json" | jq '.[] | {id, profile, mfa}'
```

**Google Workspace:**

- Admin Console → Reports → User Reports
- Select "2-Step Verification" enrollment report
- Export to CSV

**Step 2: Generate Workbook**

Option A - Automated (Recommended):
```bash
python3 generate_a8235_2_mfa_coverage.py --input EntraID_MFA_Status.csv
```
This creates: `ISMS-IMP-A.8.2-3-5.2_MFA_Coverage_YYYYMMDD.xlsx`

Option B - Manual:

- Use Excel template (provided in ISMS repository)
- Import user data manually
- Save as: `ISMS-IMP-A.8.2-3-5.2_MFA_Coverage_[DATE].xlsx`

**Step 3: Complete Sheet 1 - User MFA Enrollment Status**

For each user:

1. **User Identification** (Columns A-E):

   - User ID: Unique identifier (username, employee ID)
   - User Principal Name: Email/UPN
   - Display Name: Full name
   - User Type: Employee, Contractor, Vendor, Service Account
   - Department: User's department/business unit

2. **User Role Classification** (Columns F-I):

   - Privileged User: Yes/No (admin rights anywhere?)
   - Remote Access User: Yes/No (VPN, remote desktop?)
   - Confidential Data Access: Yes/No (access to restricted data?)
   - Manager: User's direct manager

3. **MFA Enrollment Status** (Columns J-O):

   - MFA Enrolled: Yes, No, Exempt
   - MFA Method: Authenticator App, Hardware Token, SMS, Biometric, Push, Other
   - Backup Method Registered: Yes/No
   - Enrollment Date: When MFA was enrolled (DD.MM.YYYY)
   - Last MFA Authentication: Date of last successful MFA auth
   - MFA Exemption Reason: If exempt, why? (documented exception)

4. **Compliance Assessment** (Columns P-Q):

   - MFA Requirement: Required, Optional, N/A (auto-calculated based on user role)
   - Compliance Status: Compliant, Non-Compliant, Exempt (auto-calculated)

**Step 4: Complete Sheet 2 - MFA Coverage by User Type**

This sheet auto-calculates from Sheet 1:

**Privileged Users:**

- Total privileged users
- Privileged users with MFA
- MFA coverage percentage
- Privileged users without MFA (critical gap)

**Standard Users:**

- Total standard users
- Standard users with MFA
- MFA coverage percentage

**Remote Access Users:**

- Total remote access users
- Remote access users with MFA
- MFA coverage percentage

**Contractors/Vendors:**

- Total contractors/vendors
- Contractors with MFA
- MFA coverage percentage

**Overall:**

- Total users
- Total users with MFA
- Overall MFA coverage percentage

**Step 5: Complete Sheet 3 - MFA Gap Analysis**

For each user WITHOUT MFA:

1. **Gap Identification** (Columns A-E):

   - User ID (from Sheet 1)
   - User Name
   - User Type
   - User Role (Privileged, Remote, Confidential Data)
   - Gap Priority: Critical, High, Medium, Low (auto-calculated)

2. **Gap Remediation** (Columns F-I):

   - Reason for No MFA: Never enrolled, Lost device, Technical issue, Refused, Other
   - Remediation Owner: Person responsible for enrolling user
   - Target Enrollment Date: Deadline for MFA enrollment
   - Remediation Status: Not Started, In Progress, Blocked, Completed

**Gap Priority Rules:**

- **Critical**: Privileged user without MFA
- **High**: Remote access user without MFA OR Confidential data access without MFA
- **Medium**: Standard employee without MFA
- **Low**: Service account or documented exception

**Step 6: Complete Sheet 5 - Enrollment Campaign**

For tracking MFA enrollment communications:

1. **Campaign Planning** (Columns A-C):
   - Campaign ID: Unique identifier (CAMPAIGN-2026-Q1)
   - Campaign Name: MFA Q1 Rollout, Privileged User MFA Push, etc.
   - Target Audience: All Users, Privileged Users, Remote Users, Contractors

2. **Campaign Execution** (Columns D-H):
   - Launch Date: When campaign started
   - Delivery Methods: Email, All Hands Meeting, Department Meeting, Training Session
   - Messages Sent: Number of communications
   - Enrollment Support: Help desk contact, training videos, documentation links
   - Campaign Status: Planning, In Progress, Completed

3. **Campaign Metrics** (Columns I-K):
   - Users Targeted: Count
   - Users Enrolled During Campaign: Count
   - Campaign Enrollment %: Percentage from target audience

**Step 7: Complete Sheet 6 - Backup Method Status**

For tracking secondary MFA methods:

1. **User Backup Methods** (Columns A-E):
   - User ID: From Sheet 2
   - User Name: Display name
   - Primary MFA Method: Authenticator App, Hardware Token, etc.
   - Backup Method Registered: Yes, No (does user have secondary method?)
   - Backup Method Type: Authenticator App, Recovery Codes, Secondary Device

2. **Backup Coverage Analysis** (Columns F-H):
   - Last Backup Validation: Date backup method was tested
   - Recovery Code Status: Saved, Not Saved, Lost/Regenerated
   - Compliance: Compliant (backup exists), Non-Compliant (no backup)

3. **Metrics Summary**:
   - Users with Backup Methods: Count and %
   - Recovery Code Distribution: Users with printed/saved codes

**Step 8: Review Calculated Metrics**

The workbook automatically calculates:

- **Overall MFA Coverage**: % of all users with MFA
- **Privileged User MFA Coverage**: % of privileged users with MFA (target: 100%)
- **Remote Access MFA Coverage**: % of remote users with MFA (target: 100%)
- **MFA Method Distribution**: Breakdown by method (authenticator app, hardware token, etc.)
- **Enrollment Trend**: Month-over-month MFA enrollment progress
- **Backup Method Coverage**: % of MFA users with secondary authentication method

**Step 9: Collect Evidence**

Required evidence:

- **Identity Provider MFA Report**: Screenshot or CSV export showing MFA enrollment
- **MFA Enforcement Policy**: Screenshot of conditional access policies (Azure) or MFA policies (Okta)
- **Enrollment Campaign Documentation**: Communications to users, training materials
- **Exception Approvals**: CISO-approved exceptions for MFA exemptions
- **Backup Method Report**: Backup method registration status

Store evidence in: `/evidence/mfa/[date]/`

**Step 10: Complete Evidence Register (Sheet 9)**

Document all collected evidence:

- Evidence ID, Type, Description, Location, Collection Date

**Step 11: Approval & Sign-Off (Sheet 10)**

Three-level approval process:
1. **Preparer**: Security team member who completed assessment
2. **Reviewer**: IAM team lead or senior security engineer
3. **Approver**: CISO (final authority)

---

---

# Evidence Collection Guidelines

## Required Evidence Types

**For Overall MFA Deployment:**

1. **MFA Enrollment Report**:

   - Screenshot from identity provider showing MFA enrollment status
   - Export CSV with user MFA data
   - Date/time stamp visible

2. **MFA Enforcement Policies**:

   - Entra ID Conditional Access policies (if Azure)
   - Okta MFA policies (if Okta)
   - Screenshot showing which users/groups require MFA

3. **MFA Method Distribution**:

   - Report showing breakdown by MFA method
   - Authenticator app usage, hardware token usage, SMS usage, etc.

4. **Enrollment Campaign Documentation**:

   - Email communications to users
   - Training materials (how to enroll in MFA)
   - Help desk tickets related to MFA enrollment

## Evidence Storage

**Structure:**
```
/evidence/mfa/
├── 2026-01-22/
│   ├── azure-ad-mfa-enrollment-report.csv
│   ├── azure-ad-mfa-enforcement-policy.png
│   ├── mfa-method-distribution-report.pdf
│   └── mfa-enrollment-email-to-users.pdf
├── 2026-02-22/
│   └── [monthly evidence]
└── exception-approvals/
    ├── service-account-mfa-exemption-ciso-approval.pdf
    └── legacy-system-mfa-exemption.pdf
```

## Evidence Quality Checklist

For each piece of evidence:

- [ ] Date/time stamp visible
- [ ] Source clearly identified (Entra ID, Okta, etc.)
- [ ] Data matches workbook entries
- [ ] Redacted appropriately (no passwords or secrets)
- [ ] Linked in Evidence Register

---

# Common Pitfalls & How to Avoid Them

## Pitfall 1: Confusing MFA Capable vs. MFA Enrolled

**Problem**: Identity provider shows user as "MFA capable" but not actually enrolled

**Solution**:

- Entra ID: "Capable" means user CAN register, not that they HAVE registered
- Check "Registered" status, not "Capable" status
- Verify: Has user completed MFA registration? Has user authenticated with MFA at least once?

## Pitfall 2: Not Tracking Backup MFA Methods

**Problem**: User enrolled in MFA but no backup method (single point of failure)

**Solution**:

- Track backup method registration in Column M (Sheet 1)
- Best practice: Every user should have 2+ MFA methods registered
- Common backup: Authenticator app + hardware token OR Authenticator app + recovery codes

## Pitfall 3: Assuming All Privileged Users Are Known

**Problem**: Missing privileged users (not tracked in IAM system)

**Solution**:

- Cross-reference with IMP.3 (Privileged Account Inventory)
- Check group memberships (Domain Admins, Enterprise Admins, local admins)
- Ask system owners: "Who has admin rights to your system?"

## Pitfall 4: SMS as Primary MFA Method

**Problem**: SMS is weakest MFA method (SIM swapping attacks, interception)

**Solution**:

- Flag users with SMS as primary method
- Encourage migration to authenticator app or hardware token
- SMS acceptable as backup method ONLY

## Pitfall 5: Not Tracking MFA Exemptions

**Problem**: Users exempt from MFA with no documentation

**Solution**:

- Every MFA exemption requires CISO approval
- Document reason in Column O (Sheet 1)
- Review exemptions quarterly (are they still necessary?)

## Pitfall 6: Service Accounts Without MFA

**Problem**: Service accounts authenticate without MFA

**Solution**:

- Service accounts typically cannot use interactive MFA
- Compensating controls:
  - Certificate-based authentication (mTLS)
  - API keys with short expiration
  - Network restriction (service account can only auth from specific IPs)
  - Enhanced monitoring (alert on service account usage from unexpected location)

## Pitfall 7: Not Celebrating Progress

**Problem**: MFA rollout is a multi-month effort, team morale suffers

**Solution**:

- Track month-over-month improvement (e.g., "MFA coverage increased from 45% to 72% this quarter!")
- Celebrate milestones (80% coverage, 90% coverage, 100% privileged user coverage)
- Share success stories (security incidents prevented by MFA)

## Pitfall 8: Forgetting NIS2 Compliance

**Problem**: Organisation is NIS2 essential/important entity but MFA deployment not prioritized

**Solution**:

- NIS2 Article 21(2)(e) MANDATES MFA for essential/important entities
- This is not optional - regulatory requirement
- Document NIS2 applicability in assessment
- Present MFA coverage as NIS2 compliance metric

## Pitfall 9: MFA Fatigue

**Problem**: Users complain about excessive MFA prompts

**Solution**:

- Use "remember MFA on trusted devices" (30-90 days)
- Deploy risk-based MFA (only challenge on unusual login)
- Use push notifications (easier than typing codes)
- User training (explain why MFA is worth the inconvenience)

## Pitfall 10: Not Testing MFA Effectiveness

**Problem**: MFA enrolled but never actually used

**Solution**:

- Track "Last MFA Authentication" (Column N, Sheet 1)
- Users with MFA enrolled but never authenticated = suspicious
- Test: Force MFA challenge, verify user can complete

---

# Quality Checklist

Before submitting assessment for approval, verify:

## Completeness

- [ ] All users inventoried (employees, contractors, vendors, service accounts)
- [ ] User type and role correctly classified
- [ ] MFA enrollment status documented for every user
- [ ] MFA method documented for enrolled users
- [ ] Backup MFA method status tracked
- [ ] All gaps identified with remediation plan

## Accuracy

- [ ] MFA enrollment data validated against identity provider
- [ ] Privileged user classification validated with IMP.3
- [ ] User type classification validated with HR
- [ ] MFA exemptions have documented CISO approval
- [ ] Calculated metrics reviewed (make sense?)

## Evidence Quality

- [ ] Identity provider MFA report collected
- [ ] MFA enforcement policies documented
- [ ] Exception approvals collected
- [ ] Evidence dated and linked in Evidence Register

## Compliance

- [ ] Privileged users without MFA identified as CRITICAL gaps
- [ ] Remote access users without MFA identified as HIGH gaps
- [ ] MFA coverage targets defined (e.g., 100% privileged, 95% overall)
- [ ] NIS2 compliance status documented (if applicable)
- [ ] Remediation timeline defined for all gaps

## Professional Presentation

- [ ] No spelling errors
- [ ] Consistent formatting (dates in DD.MM.YYYY format)
- [ ] Clear and concise notes
- [ ] User-friendly (can HR or manager understand it?)

---

# Interpreting Results

## Understanding MFA Coverage Scores

**Overall MFA Coverage:**

- **95-100%**: Excellent - Near-universal MFA deployment
- **85-94%**: Good - Strong MFA coverage, few gaps
- **70-84%**: Moderate - MFA deployment in progress, significant gaps remain
- **<70%**: Poor - Insufficient MFA coverage, major security risk

**Privileged User MFA Coverage:**

- **100%**: Target state - All privileged users have MFA (MANDATORY)
- **95-99%**: Nearly there - Document exemptions, set deadline for 100%
- **<95%**: CRITICAL RISK - Privileged users without MFA = high-value targets

**Remote Access User MFA Coverage:**

- **100%**: Target state - All remote users have MFA (MANDATORY)
- **90-99%**: Good progress - Prioritize remaining gaps
- **<90%**: HIGH RISK - Remote access without MFA = easy attack vector

**MFA Method Quality Score:**

- **Phishing-Resistant (FIDO2, WebAuthn)**: Best - 100 points
- **Authenticator App (TOTP)**: Good - 80 points
- **Hardware Token (TOTP)**: Good - 80 points
- **Push Notification**: Acceptable - 60 points
- **SMS/Voice**: Weak - 40 points (acceptable as backup only)

## Gap Prioritization

**Priority 1 - CRITICAL (Immediate Action - Within 7 Days):**

- Tier 0 privileged users without MFA (Domain Admins, Enterprise Admins, Cloud Global Admins)
- Break-glass accounts without MFA
- Security administrator accounts without MFA

**Priority 2 - HIGH (Within 30 Days):**

- Tier 1/2 privileged users without MFA (Server admins, DBAs, Application admins)
- Remote access users without MFA (VPN, external access)
- Users with access to confidential/restricted data without MFA

**Priority 3 - MEDIUM (Within 90 Days):**

- Standard employees without MFA
- Contractors without MFA
- Users with SMS as primary MFA method (encourage migration to authenticator app)

**Priority 4 - LOW (Ongoing Improvement):**

- Service accounts (evaluate compensating controls)
- Documented exceptions with CISO approval

## Regulatory Compliance Interpretation

**NIS2 Compliance** (if essential/important entity):

- Article 21(2)(e) requires "the use of multi-factor authentication"
- Target: 100% user MFA coverage (privileged and standard users)
- Exemptions must be documented with compensating controls
- MFA Coverage Score directly maps to NIS2 compliance

**FINMA Compliance** (if Swiss financial institution):

- Margin 56 requires authentication for critical systems
- MFA strongly recommended for privileged access
- Target: 100% privileged user MFA, 95%+ overall

**DORA Compliance** (if EU financial entity):

- Article 9(3) requires strong authentication mechanisms
- MFA is primary strong authentication method
- Target: 100% privileged user MFA, 90%+ overall

---

# Review & Approval Process

## Approval Workflow

**Level 1 - Preparer (Security Team)**:

- Export user and MFA data
- Complete assessment workbook
- Identify gaps and prioritize
- Collect evidence
- Submit for review

**Level 2 - Reviewer (IAM Team Lead / Senior Security Engineer)**:

- Validate user classification accuracy
- Verify MFA enrollment data against identity provider
- Check gap prioritization logic
- Confirm evidence completeness
- Approve and forward to CISO

**Level 3 - Approver (CISO)**:

- Review MFA coverage metrics
- Validate critical gaps (privileged users without MFA)
- Approve remediation priorities and timeline
- Sign off on assessment
- Present to Executive Management (if required)

## Approval Criteria

Assessment is approved when:

- [ ] All users inventoried with MFA status
- [ ] Privileged user MFA coverage documented
- [ ] Critical gaps identified and prioritized
- [ ] Remediation timeline defined for all gaps
- [ ] Evidence collected and linked
- [ ] NIS2/FINMA/DORA compliance status documented (if applicable)

## Post-Approval Actions

After CISO approval:
1. **Communicate Gaps**: Notify users without MFA (enrollment required)
2. **Escalate Critical Gaps**: Privileged users without MFA escalated to their managers
3. **Track Remediation**: Move gaps to remediation tracking (Dashboard IMP.6)
4. **Schedule Next Review**: Set calendar reminder for monthly update

---

**END OF USER GUIDE**

---

*"One factor is an assumption; two factors are a verification."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
