**ISMS-IMP-A.8.2-3-5.S2-TG - MFA Coverage Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.2-3-5.S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Multi-Factor Authentication Coverage |
| **Related Policy** | ISMS-POL-A.8.2-3-5 (Section 2.1.2 - MFA Requirements) |
| **Purpose** | Track MFA enrollment and coverage across all user types to verify MFA deployment meets organizational and regulatory requirements (including NIS2 Article 21(2)(e) where applicable) |
| **Target Audience** | Security Team, IT Operations, IAM Team, CISO, Compliance Team |
| **Assessment Type** | User Enrollment & Coverage Analysis |
| **Review Cycle** | Monthly enrollment tracking, Quarterly comprehensive coverage analysis |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial assessment specification for MFA coverage tracking | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.2-3-5.S2-UG.

---

# Technical Specification

# Excel Workbook Structure

## Workbook Overview

**Filename:** `ISMS-IMP-A.8.2-3-5.2_MFA_Coverage_YYYYMMDD.xlsx`

**Sheet Structure:**

| Sheet # | Sheet Name | Purpose | Rows | Completion Method |
|---------|-----------|---------|------|-------------------|
| 1 | Instructions_Legend | User guide and reference | ~50 | Pre-populated |
| 2 | User_MFA_Enrollment | Individual user MFA status | 1003 | User completes (or auto-import) |
| 3 | MFA_Coverage_By_Type | MFA coverage metrics by user type | ~30 | Auto-calculated |
| 4 | MFA_Method_Analysis | MFA method breakdown and security analysis | ~50 | User completes |
| 5 | Enrollment_Timeline | Month-over-month progress tracking | ~15 | User completes (historical) |
| 6 | MFA_Gaps_Priority | Users without MFA with remediation priority | 503 | Auto-populated from Sheet 2 |
| 7 | Enrollment_Campaign | Campaign scheduling and delivery tracking | ~30 | User completes |
| 8 | Backup_Method_Status | Backup authentication method coverage | ~25 | User completes |
| 9 | Evidence_Register | Evidence tracking | 53 | User completes |
| 10 | Approval_Sign_Off | Three-level approval workflow | ~25 | User completes |

**Total Workbook:** 10 sheets, ~1,800 rows of structured data collection

## Color Coding & Conditional Formatting

**MFA Enrollment Status Colors:**

- 🟢 **Green (Enrolled)**: RGB(198, 239, 206) - User has MFA enrolled and active
- 🔴 **Red (Not Enrolled)**: RGB(255, 199, 206) - User does not have MFA
- 🟡 **Yellow (Exempt)**: RGB(255, 235, 156) - User exempt from MFA (documented exception)

**Gap Priority Colors:**

- 🔴 **Critical**: RGB(255, 0, 0) - Privileged user without MFA
- 🟠 **High**: RGB(255, 153, 0) - Remote access or confidential data without MFA
- 🟡 **Medium**: RGB(255, 255, 0) - Standard user without MFA
- 🟢 **Low**: RGB(146, 208, 80) - Service account or documented exception

**MFA Method Quality Colors:**

- 🟢 **Green (Phishing-Resistant)**: FIDO2, WebAuthn
- 🟡 **Yellow (Good)**: Authenticator App, Hardware Token
- 🟠 **Orange (Acceptable)**: Push Notification
- 🔴 **Red (Weak)**: SMS, Voice

---

# Sheet 2: User MFA Enrollment (Primary Data Collection)

## Purpose

Individual user MFA enrollment status tracking.

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | User ID | 15 | Text | Free text | Unique user identifier (username, employee ID) |
| B | User Principal Name | 25 | Text | Free text | Email address / UPN |
| C | Display Name | 22 | Text | Free text | Full name (First Last) |
| D | User Type | 15 | Dropdown | Employee, Contractor, Vendor, Service Account | User classification |
| E | Department | 18 | Text | Free text | User's department/business unit |
| F | Privileged User | 15 | Dropdown | Yes, No | Has admin rights anywhere? |
| G | Remote Access User | 18 | Dropdown | Yes, No | VPN or external access? |
| H | Confidential Data Access | 20 | Dropdown | Yes, No | Access to restricted data? |
| I | Manager | 20 | Text | Free text | User's direct manager |
| J | MFA Enrolled | 15 | Dropdown | Yes, No, Exempt | MFA enrollment status |
| K | MFA Method | 20 | Dropdown | Authenticator App, Hardware Token, FIDO2, SMS, Biometric, Push, Other | Primary MFA method |
| L | MFA Method Tier | 15 | Formula | Auto: Tier 1-4 | MFA method quality (phishing-resistant = Tier 1) |
| M | Backup Method Registered | 18 | Dropdown | Yes, No, N/A | Second MFA method registered? |
| N | Enrollment Date | 15 | Date | DD.MM.YYYY | When MFA was enrolled |
| O | Last MFA Authentication | 18 | Date | DD.MM.YYYY | Date of last MFA auth |
| P | MFA Exemption Reason | 25 | Text | Free text | If exempt, why? |
| Q | MFA Requirement | 15 | Formula | Auto: Required, Optional, N/A | Is MFA required for this user? |
| R | Compliance Status | 18 | Formula | Auto: Compliant, Non-Compliant, Exempt | Compliance with MFA policy |

**Total Columns:** 18 (A-R)

## Data Validation Rules

**User Type (Column D):**
```
List: Employee, Contractor, Vendor, Service Account
```

**Privileged User / Remote Access / Confidential Data (Columns F, G, H):**
```
List: Yes, No
```

**MFA Enrolled (Column J):**
```
List: Yes, No, Exempt
```

**MFA Method (Column K):**
```
List: Authenticator App (TOTP), Hardware Token (FIDO2), Hardware Token (TOTP), 
SMS, Voice, Biometric, Push Notification, Other
```

**Backup Method Registered (Column M):**
```
List: Yes, No, N/A
```

## MFA Method Tier Calculation (Column L)

**Formula Logic:**
```excel
=IF(K5="Hardware Token (FIDO2)", "Tier 1 - Phishing-Resistant",
  IF(OR(K5="Authenticator App (TOTP)", K5="Hardware Token (TOTP)"), "Tier 2 - Good",
    IF(K5="Push Notification", "Tier 3 - Acceptable",
      IF(OR(K5="SMS", K5="Voice"), "Tier 4 - Weak", 
        "Unknown"))))
```

**MFA Method Tiers** (per ISMS-POL-A.8.2-3-5 Section 2.1.2):

- **Tier 1 - Phishing-Resistant**: FIDO2, WebAuthn (hardware tokens with public key crypto)
- **Tier 2 - Good**: TOTP (Authenticator app, TOTP hardware token)
- **Tier 3 - Acceptable**: Push notifications (can be phished but better than SMS)
- **Tier 4 - Weak**: SMS, Voice (vulnerable to SIM swapping, interception)

## MFA Requirement Calculation (Column Q)

**Formula Logic:**
```excel
=IF(F5="Yes", "Required - Privileged",
  IF(G5="Yes", "Required - Remote Access",
    IF(H5="Yes", "Required - Confidential Data",
      IF(D5="Service Account", "Optional",
        "Required - Standard"))))
```

**MFA Requirements** (per ISMS-POL-A.8.2-3-5):

- Privileged users: MANDATORY
- Remote access users: MANDATORY
- Confidential data access: MANDATORY
- Standard users: MANDATORY (if NIS2 applicable) or RECOMMENDED
- Service accounts: Optional (use compensating controls)

## Compliance Status Calculation (Column R)

**Formula Logic:**
```excel
=IF(J5="Exempt", "Exempt",
  IF(J5="Yes", "Compliant",
    IF(Q5="Optional", "N/A - Optional",
      "Non-Compliant")))
```

**Conditional Formatting:**

- Compliant → Green
- Non-Compliant → Red
- Exempt → Yellow
- N/A → Gray

## Data Rows

**Header Row:** Row 4
**Data Rows:** Rows 5-1003 (1000 users)
**Freeze Panes:** Row 5 (freeze header)

---

# Sheet 3: Coverage by User Type

## Purpose

Calculate MFA coverage percentages by user type for executive reporting.

## Metric Calculations

**Privileged Users:**
```excel
Total Privileged Users: 
  =COUNTIF('User MFA Enrollment'!F:F,"Yes")

Privileged Users with MFA: 
  =COUNTIFS('User MFA Enrollment'!F:F,"Yes",'User MFA Enrollment'!J:J,"Yes")

Privileged User MFA Coverage: 
  =Privileged_with_MFA / Total_Privileged * 100

Target: 100%
```

**Remote Access Users:**
```excel
Total Remote Users: 
  =COUNTIF('User MFA Enrollment'!G:G,"Yes")

Remote Users with MFA: 
  =COUNTIFS('User MFA Enrollment'!G:G,"Yes",'User MFA Enrollment'!J:J,"Yes")

Remote User MFA Coverage: 
  =Remote_with_MFA / Total_Remote * 100

Target: 100%
```

**Confidential Data Access Users:**
```excel
Total Confidential Access: 
  =COUNTIF('User MFA Enrollment'!H:H,"Yes")

Confidential Access with MFA: 
  =COUNTIFS('User MFA Enrollment'!H:H,"Yes",'User MFA Enrollment'!J:J,"Yes")

Confidential Access MFA Coverage: 
  =Confidential_with_MFA / Total_Confidential * 100

Target: 100%
```

**Standard Users:**
```excel
Total Standard Users: 
  =COUNTIFS('User MFA Enrollment'!F:F,"No",'User MFA Enrollment'!G:G,"No",
            'User MFA Enrollment'!H:H,"No",'User MFA Enrollment'!D:D,"Employee")

Standard Users with MFA: 
  =COUNTIFS('User MFA Enrollment'!F:F,"No",'User MFA Enrollment'!G:G,"No",
            'User MFA Enrollment'!H:H,"No",'User MFA Enrollment'!D:D,"Employee",
            'User MFA Enrollment'!J:J,"Yes")

Standard User MFA Coverage: 
  =Standard_with_MFA / Total_Standard * 100

Target: 95% (or 100% if NIS2 applicable)
```

**Overall:**
```excel
Total Users: 
  =COUNTA('User MFA Enrollment'!A5:A1003)

Total Users with MFA: 
  =COUNTIF('User MFA Enrollment'!J:J,"Yes")

Overall MFA Coverage: 
  =Total_with_MFA / Total_Users * 100

Target: 95-100%
```

## Layout

```
+-----------------------------------------------+
| MFA COVERAGE BY USER TYPE                     |
+-----------------------------------------------+
| User Type           | Total | With MFA | % |
|---------------------|-------|----------|-----|
| Privileged Users    |   50  |    48    | 96% | 🟡
| Remote Access       |  120  |   115    | 96% | 🟡
| Confidential Data   |   80  |    78    | 98% | 🟢
| Standard Users      |  650  |   520    | 80% | 🟠
| Contractors         |  100  |    85    | 85% | 🟢
+-----------------------------------------------+
| OVERALL             | 1000  |   846    | 85% | 🟢
+-----------------------------------------------+
```

---

# Sheet 4: MFA Gap Analysis

## Purpose

Identify all users without MFA with prioritized remediation plan.

## Auto-Population Logic

This sheet auto-populates from Sheet 2 - only users with `MFA Enrolled = No`:

```excel
=FILTER('User MFA Enrollment'!A:R, 
        'User MFA Enrollment'!J:J="No")
```

## Additional Columns

| Col | Header | Width | Type | Description |
|-----|--------|-------|------|-------------|
| S | Gap Priority | 15 | Formula | Auto: Critical, High, Medium, Low |
| T | Reason for No MFA | 25 | Dropdown | Never Enrolled, Lost Device, Technical Issue, Refused, Other |
| U | Remediation Owner | 20 | Text | Person responsible for enrollment |
| V | Target Enrollment Date | 18 | Date | Deadline for MFA enrollment |
| W | Remediation Status | 18 | Dropdown | Not Started, In Progress, Blocked, Completed |
| X | Blocking Issue | 25 | Text | If blocked, why? |

## Gap Priority Calculation (Column S)

**Formula Logic:**
```excel
=IF(F5="Yes", "Critical - Privileged User",
  IF(OR(G5="Yes", H5="Yes"), "High - Remote or Confidential",
    IF(D5="Employee", "Medium - Standard User",
      "Low - Service Account")))
```

**Conditional Formatting:**

- Critical → Red background
- High → Orange background
- Medium → Yellow background
- Low → Green background

---

# Sheet 5: MFA Method Distribution

## Purpose

Show breakdown of MFA methods in use (quality analysis).

## Calculations

```excel
Authenticator App: 
  =COUNTIF('User MFA Enrollment'!K:K,"Authenticator App (TOTP)")

Hardware Token (FIDO2): 
  =COUNTIF('User MFA Enrollment'!K:K,"Hardware Token (FIDO2)")

Hardware Token (TOTP): 
  =COUNTIF('User MFA Enrollment'!K:K,"Hardware Token (TOTP)")

SMS: 
  =COUNTIF('User MFA Enrollment'!K:K,"SMS")

Push Notification: 
  =COUNTIF('User MFA Enrollment'!K:K,"Push Notification")

Biometric: 
  =COUNTIF('User MFA Enrollment'!K:K,"Biometric")

Other: 
  =COUNTIF('User MFA Enrollment'!K:K,"Other")
```

## Quality Score

```excel
Phishing-Resistant Methods: 
  =COUNTIF('User MFA Enrollment'!L:L,"Tier 1 - Phishing-Resistant")

Good Methods: 
  =COUNTIF('User MFA Enrollment'!L:L,"Tier 2 - Good")

Acceptable Methods: 
  =COUNTIF('User MFA Enrollment'!L:L,"Tier 3 - Acceptable")

Weak Methods: 
  =COUNTIF('User MFA Enrollment'!L:L,"Tier 4 - Weak")

Overall MFA Quality Score: 
  =(Phishing_Resistant*100 + Good*80 + Acceptable*60 + Weak*40) / Total_MFA_Users
```

---

# Sheet 6: Enrollment Trend

## Purpose

Track MFA enrollment progress month-over-month.

## Column Structure

| Col | Header | Width | Type | Description |
|-----|--------|-------|------|-------------|
| A | Month | 12 | Date | Month (MMM YYYY) |
| B | Total Users | 12 | Number | Total users in organization |
| C | Users with MFA | 15 | Number | Users with MFA enrolled |
| D | MFA Coverage % | 15 | Formula | (C / B) * 100 |
| E | New Enrollments | 15 | Number | Users enrolled this month |
| F | Target Coverage % | 15 | Number | Target for this month |

## User Completes

User manually enters historical data for trend analysis:

- January 2026: 1000 users, 700 with MFA (70%)
- February 2026: 1010 users, 800 with MFA (79%)
- March 2026: 1020 users, 900 with MFA (88%)

---

# Sheet 7: Evidence Register

## Column Structure

| Col | Header | Width | Type | Description |
|-----|--------|-------|------|-------------|
| A | Evidence ID | 15 | Text | EV-A8235-2-001 |
| B | Evidence Type | 20 | Dropdown | Screenshot, Export, Policy, Communication, Report |
| C | Description | 30 | Text | Brief description |
| D | File Location | 30 | Text | Path to evidence file |
| E | Collection Date | 15 | Date | When collected |
| F | Collected By | 18 | Text | Person who collected |

---

# Sheet 8: Approval & Sign-Off

## Three-Level Approval

**Level 1 - Preparer:**

- Name, Title, Date, Signature

**Level 2 - Reviewer (IAM Lead):**

- Name, Title, Date, Signature

**Level 3 - Approver (CISO):**

- Name, Title, Date, Signature

---

# Python Script Integration

## Script Purpose

Automated generation of MFA coverage workbook with user data import from identity provider.

**Script:** `generate_a8235_2_mfa_coverage.py`

## Script Features

- Imports user data from CSV (Entra ID, Okta, Google export)
- Creates all 8 sheets with proper structure
- Applies data validation rules (dropdowns)
- Implements conditional formatting (color coding)
- Adds formulas for coverage calculations
- Generates MFA gap analysis automatically
- Sets column widths and freeze panes

## Running the Script

```bash
# With user data import
python3 generate_a8235_2_mfa_coverage.py --input azure-ad-mfa-export.csv

# With custom date
python3 generate_a8235_2_mfa_coverage.py --input users.csv --date 2026-01-22

# Custom output path
python3 generate_a8235_2_mfa_coverage.py --input users.csv --output /path/to/file.xlsx
```

## Input CSV Format

Expected columns in input CSV:

- UserPrincipalName (required)
- DisplayName (required)
- MFAStatus (required: "Enabled", "Disabled", "Enforced")
- MFAMethod (optional: "Authenticator App", "SMS", etc.)
- UserType (optional: "Employee", "Contractor", etc.)

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Document Assembly & Quality Checks

**Complete Document Structure:**
```
ISMS-IMP-A.8.2-3-5.2 - MFA Coverage Assessment v1.0

├── Document Control (Metadata, Version History)
│
├── PART I: USER COMPLETION GUIDE (~600 lines)
│   ├── 1. Assessment Overview
│   ├── 2. Prerequisites
│   ├── 3. Assessment Workflow
│   ├── 4. Evidence Collection
│   ├── 5. Common Pitfalls (10 pitfalls)
│   ├── 6. Quality Checklist
│   ├── 7. Interpreting Results
│   └── 8. Review & Approval
│
└── PART II: TECHNICAL SPECIFICATION (~400 lines)
    ├── 1. Workbook Structure
    ├── 2. Sheet 2: User MFA Enrollment
    ├── 3. Sheet 3: Coverage by User Type
    ├── 4. Sheet 4: MFA Gap Analysis
    ├── 5. Sheet 5: MFA Method Distribution
    ├── 6. Sheet 6: Enrollment Trend
    ├── 7. Sheet 7: Evidence Register
    ├── 8. Sheet 8: Approval & Sign-Off
    └── 9. Python Script Integration
```

**Quality Checks Before Finalizing:**

- [ ] All sections complete and accurate
- [ ] NIS2 Article 21(2)(e) compliance clearly addressed
- [ ] MFA method tier system explained (phishing-resistant vs. weak)
- [ ] Cross-references correct (sheet numbers, policy references)
- [ ] No placeholder text
- [ ] Dates in DD.MM.YYYY format
- [ ] Technical specification matches Python script
- [ ] User guide provides clear, actionable guidance

---

**END OF ISMS-IMP-A.8.2-3-5.2**

*MFA is your first line of defense. Deploy it properly. Track it rigorously.*

*NIS2 makes MFA mandatory. FINMA recommends it. GDPR expects it. Get it done.*

---

**END OF SPECIFICATION**

---

*"Programming is a skill best acquired by practice and example rather than from books."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
