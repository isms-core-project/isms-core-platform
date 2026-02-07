**ISMS-IMP-A.8.2-3-5.S3-TG - Privileged Account Inventory**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.2-3-5.S3-TG |
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

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.2-3-5.S3-UG.

---

# Technical Specification

# Excel Workbook Structure

## Workbook Overview

**Filename:** `ISMS-IMP-A.8.2-3-5.3_Privileged_Accounts_YYYYMMDD.xlsx`

**Sheet Structure:**

| Sheet # | Sheet Name | Purpose | Rows | Completion Method |
|---------|-----------|---------|------|-------------------|
| 1 | Instructions_Legend | User guide and Admin Tiering reference | ~80 | Pre-populated |
| 2 | Privileged_Account_Inventory | All privileged accounts with tier classification | 503 | User completes |
| 3 | Admin_Tiering_Matrix | Tier 0/1/2 definitions and security requirements | ~50 | Pre-populated |
| 4 | Privileged_User_Roster | Users who own privileged accounts | 203 | Auto-calculated |
| 5 | PAM_Vault_Coverage | PAM vaulting and credential management coverage | ~30 | Auto-calculated |
| 6 | MFA_Hardware_Tokens | Hardware token distribution for privileged users | ~50 | User completes |
| 7 | Credential_Rotation_Status | Credential rotation compliance tracking | ~40 | User completes |
| 8 | Access_Review_Results | Quarterly access review audit trail | ~60 | User completes |
| 9 | Tier_Isolation_Compliance | Tier 0/1/2 isolation and baseline verification | ~40 | Auto-calculated |
| 10 | Evidence_Register | Evidence tracking | 53 | User completes |
| 11 | Approval_Sign_Off | Three-level approval workflow | ~25 | User completes |

**Total Workbook:** 11 sheets, ~1,100 rows of structured data collection

## Color Coding & Conditional Formatting

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

# Sheet 2: Privileged Account Inventory (Primary Data Collection)

## Purpose

Comprehensive inventory of ALL privileged accounts with Admin Tiering classification.

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Account ID | 20 | Text | Free text | Unique identifier (SamAccountName, UPN, username) |
| B | Account Name | 25 | Text | Free text | Display name or description |
| C | Account Type | 15 | Dropdown | Named, Shared, Service, Break-Glass | Account classification |
| D | Platform | 18 | Dropdown | Windows AD, Entra ID, Linux, AWS, GCP, Azure, Okta, Application, Database, Network | Where account exists |
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

## Data Validation Rules

**Account Type (Column C):**
```
List: Named, Shared, Service, Break-Glass
```

**Platform (Column D):**
```
List: Windows Active Directory, Entra ID, Linux, AWS IAM, GCP IAM, Azure, 
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

## Compliance Status Calculation (Column U)

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

## Admin Tier Color Coding (Column I)

**Conditional Formatting:**

- Tier 0 → Red background (RGB 255, 0, 0), White text
- Tier 1 → Orange background (RGB 255, 153, 0), Black text
- Tier 2 → Yellow background (RGB 255, 255, 0), Black text
- N/A → Gray background

---

# Sheet 3: Privileged User Summary

## Purpose

Summary of privileged access per user (who has what tier access).

## Auto-Calculation Logic

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

# Sheet 4: Tier Isolation Compliance

## Purpose

Measure tier isolation implementation and compliance.

## Metrics Calculated

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

# Sheet 5: PAM Coverage Analysis

## Purpose

Measure PAM solution adoption and session recording coverage.

## Metrics Calculated

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

# Sheet 6: Evidence Register

## Column Structure

| Col | Header | Width | Type | Description |
|-----|--------|-------|------|-------------|
| A | Evidence ID | 15 | Text | EV-A8235-3-001 |
| B | Evidence Type | 20 | Dropdown | Group Membership, Role Assignment, PAM Report, SIEM Query, Policy Document |
| C | Description | 30 | Text | Brief description |
| D | File Location | 30 | Text | Path to evidence file |
| E | Collection Date | 15 | Date | When collected |
| F | Collected By | 18 | Text | Person who collected |

---

# Sheet 7: Approval & Sign-Off

## Three-Level Approval

**Level 1 - Preparer (Security Team):**

- Name, Title, Date, Signature

**Level 2 - Reviewer (IAM Lead / Senior Security Engineer):**

- Name, Title, Date, Signature

**Level 3 - Approver (CISO):**

- Name, Title, Date, Signature

---

# Python Script Integration

## Script Purpose

Automated generation of privileged account inventory workbook.

**Script:** `generate_a8235_3_privileged_accounts.py`

## Script Features

- Creates all 7 sheets with proper structure
- Applies data validation rules (dropdowns, tier classifications)
- Implements conditional formatting (tier colors, compliance colors)
- Adds formulas for compliance calculations
- Generates privileged user summary
- Calculates tier isolation metrics
- Sets column widths and freeze panes

## Running the Script

```bash
# Basic usage
python3 generate_a8235_3_privileged_accounts.py

# With custom date
python3 generate_a8235_3_privileged_accounts.py --date 2026-01-22

# Custom output path
python3 generate_a8235_3_privileged_accounts.py --output /path/to/file.xlsx
```

## Script Customization Points

Marked with `# CUSTOMIZE:` in script:

- Admin tier definitions (organizational tier model)
- Privileged role categories (additional role types)
- Compliance criteria (different tier requirements)
- PAM solution integration (CyberArk, BeyondTrust API)

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Document Assembly & Quality Checks

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

---

**END OF SPECIFICATION**

---

*"I believe that at the end of the century the use of words and general educated opinion will have altered so much that one will be able to speak of machines thinking without expecting to be contradicted."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
