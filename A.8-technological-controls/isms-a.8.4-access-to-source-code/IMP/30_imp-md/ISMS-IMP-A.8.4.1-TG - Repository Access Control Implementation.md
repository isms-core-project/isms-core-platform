**ISMS-IMP-A.8.4.1-TG - Repository Access Control Implementation**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.4: Access to Source Code

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.4.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Repository Access Control and Compliance |
| **Related Policy** | ISMS-POL-A.8.4, Section 2.1 (Repository Access Management), Section 2.2 (Repository Classification), Section 2.3 (Role-Based Access Control) |
| **Purpose** | Document repository inventory, access permissions, and access control compliance in a technology-independent manner |
| **Target Audience** | Repository Owners, Development Team Leads, Information Security Team, IT Operations, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Repository Access Control assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.4.1-UG.

---

# Technical Specification

**Audience:** Python/Excel Script Maintainers, Assessment Workbook Developers

---

## Instructions for Workbook Development

### Workbook Generation

**Primary Script:** `generate_a84_1_repository_access.py`

**Purpose:** Generate Excel workbook (`ISMS-IMP-A.8.4.1_Repository_Access_YYYYMMDD.xlsx`) with pre-configured sheets, data validation, conditional formatting, and formulas based on this specification.

**Key Functions:**

- `create_workbook()`: Initialize workbook and sheets
- `setup_styles()`: Define cell styles, fonts, fills, borders
- `get_repository_columns()`: Return standard column definitions for repository sheets
- `create_data_validation()`: Apply dropdown lists and data validation rules
- `create_conditional_formatting()`: Apply color-coding based on cell values
- `create_formulas()`: Insert formulas for automated calculations
- `create_assessment_sheet()`: Generic sheet generator with validation
- `create_compliance_scoring()`: Compliance metrics and dashboard
- `create_evidence_register()`: Evidence tracking sheet
- `create_approval_signoff()`: Approval workflow sheet

**Script Customization Points** (marked with `# CUSTOMIZE:` in script):

- Sheet names (if organizational naming differs)
- Dropdown options (if additional statuses needed)
- Data validation rules (if custom compliance criteria)
- Conditional formatting thresholds (if different color coding)
- Formula references (if sheet structure changes)

### Workbook File Naming Convention

**Format:** `ISMS-IMP-A.8.4.1_Repository_Access_YYYYMMDD.xlsx`

**Examples:**

- `ISMS-IMP-A.8.4.1_Repository_Access_20260125.xlsx`
- `ISMS-IMP-A.8.4.1_Repository_Access_20260401.xlsx`

**Version in Filename:** Date represents assessment completion date

### Excel Compatibility

**Minimum Version:** Microsoft Excel 2016 or Excel 365  
**Compatible Applications:** LibreOffice Calc 7.0+, Google Sheets (with limitations on conditional formatting)  
**File Format:** `.xlsx` (Office Open XML)

**Features Used:**

- Data validation (dropdown lists)
- Conditional formatting (color-coding)
- Formulas (COUNTIF, SUMIF, VLOOKUP, etc.)
- Named ranges (for formula readability)
- Freeze panes (for navigation)
- Cell protection (protect formulas, allow data entry)

---

## Workbook Structure Overview

### Sheet List (11 Sheets Total)

| Sheet # | Sheet Name | Purpose | Rows | Columns | Entry Type |
|---------|------------|---------|------|---------|------------|
| 1 | Instructions_Legend | User guide and legend | ~50 | A-B | Read-only |
| 2 | Repository_Inventory | List all repositories | Variable | A-N | User input |
| 3 | User_Access_Matrix | User-to-repository access | Variable | A-Q | User input |
| 4 | Access_Request_Log | Access approval tracking | Variable | A-M | User input |
| 5 | Access_Review_Log | Quarterly review tracking | Variable | A-N | User input |
| 6 | Deprovisioning_Log | Access removal tracking | Variable | A-O | User input |
| 7 | Third_Party_Access | Contractor/auditor access | Variable | A-P | User input |
| 8 | Service_Accounts | Automation account tracking | Variable | A-P | User input |
| 9 | Compliance_Scoring | Automated compliance metrics | ~50 | A-D | Formula-based |
| 10 | Gap_Analysis | Gap tracking and remediation | Variable | A-S | User input |
| 11 | Evidence_Register | Evidence documentation | Variable | A-P | User input |
| 12 | Approval_Sign_Off | Final approval workflow | ~40 | A-B | User input |

### Sheet Dependencies

```
Repository_Inventory (Sheet 1)
        ↓
User_Access_Matrix (Sheet 2) → references Repository_Inventory
        ↓
Access_Request_Log (Sheet 3) → references User_Access_Matrix
        ↓
Access_Review_Log (Sheet 4) → references Repository_Inventory
        ↓
Deprovisioning_Log (Sheet 5) → references User_Access_Matrix
        ↓
Third_Party_Access (Sheet 6) → references Repository_Inventory
        ↓
Service_Accounts (Sheet 7) → references Repository_Inventory
        ↓
Compliance_Scoring (Sheet 8) → aggregates from all above sheets
        ↓
Gap_Analysis (Sheet 9) → references Compliance_Scoring
        ↓
Evidence_Register (Sheet 10) → references all sheets
        ↓
Approval_Sign_Off (Sheet 11) → references Compliance_Scoring
```

---

## Common Column Structure Patterns

### Standard Status Dropdown

Used in multiple sheets for consistency:

**Status Values:**

- ✅ Compliant / Appropriate / Active / Complete
- âš ï¸ Partial / Excessive / Warning
- ⌠Non-Compliant / Orphaned / Inactive / Overdue
- ðŸ•' Expired / In Progress / Pending
- N/A

**Conditional Formatting:**

- ✅: Green fill (#C6EFCE), dark green text (#006100)
- âš ï¸: Yellow fill (#FFEB9C), dark yellow text (#9C6500)
- âŒ: Red fill (#FFC7CE), dark red text (#9C0006)
- ðŸ•': Blue fill (#B4C7E7), dark blue text (#002060)
- N/A: Gray fill (#D9D9D9), dark gray text (#404040)

### Standard Date Format

All date columns:

- **Format:** YYYY-MM-DD (ISO 8601)
- **Excel Format Code:** `yyyy-mm-dd`
- **Data Validation:** Date picker
- **Why:** Sortable, international standard, unambiguous

### Standard Yes/No Dropdown

Used for binary questions:

- **Values:** ✅ Yes, ⌠No
- **Conditional Formatting:**
  - ✅ Yes: Green background
  - ⌠No: Red background

---

## Sheet 1: Instructions_Legend

### Purpose
Provide user guidance and legend for status indicators.

### Structure

**Rows 1-3: Title Section**
```
Row 1: "ISMS-IMP-A.8.4.1 - REPOSITORY ACCESS CONTROL ASSESSMENT"
Row 2: "Excel Workbook for ISO 27001:2022 Control A.8.4 Compliance"
Row 3: "Version 1.0 | [Date]"
```

**Rows 5-20: Instructions**

- How to use this workbook
- Sheet-by-sheet guidance
- Where to find help
- Contact information

**Rows 22-35: Status Legend**

| Symbol | Meaning | Usage |
|--------|---------|-------|
| ✅ | Compliant / Appropriate / Active | Access is justified and appropriate |
| âš ï¸ | Excessive / Partial | Access level too high, needs review |
| ⌠| Non-Compliant / Orphaned | Former employee access, must remove |
| ðŸ•' | Expired / In Progress | Time-bound access past end date |
| 🟢 | Low Risk | Compliance score ≥85% |
| 🟡 | Medium Risk | Compliance score 70-84% |
| ðŸ"´ | High Risk / Critical | Compliance score <70% or critical gap |

**Rows 37-50: Keyboard Shortcuts, Tips, Common Errors**

### Styling

- Title: Font size 16pt, bold, dark blue (#003366)
- Instructions: Font size 10pt, regular, black
- Legend table: Bordered, alternating row colors

---

## Sheet 2: Repository_Inventory

### Purpose
Document every source code repository across all platforms.

### Header Section (Rows 1-3)

**Row 1:** "REPOSITORY INVENTORY"  
**Row 2:** "Document all source code repositories across all platforms"  
**Row 3:** Column headers

### Column Definitions

| Col | Field Name | Width | Type | Validation | Description |
|-----|------------|-------|------|------------|-------------|
| A | Repository Name | 25 | Text | None | Exact repository name from platform |
| B | Platform | 20 | Dropdown | GitHub Cloud, GitHub Enterprise, GitLab SaaS, GitLab Self-Hosted, Bitbucket Cloud, Bitbucket Server, Azure DevOps, AWS CodeCommit, Other | Hosting platform |
| C | Repository URL | 40 | Text (URL) | None | Full HTTPS URL to repository |
| D | Repository Owner | 30 | Text | None | Person accountable (Name + email) |
| E | Classification | 18 | Dropdown | ðŸ"´ Production, 🟡 Internal Tools, 🟢 Open Source, ⚪ Archived | Repository sensitivity level |
| F | Description | 40 | Text | None | Brief purpose of repository |
| G | Primary Language | 18 | Dropdown | JavaScript, Python, Java, C#, Go, Ruby, PHP, TypeScript, Kotlin, Swift, Other | Main programming language |
| H | Number of Contributors | 12 | Number | >0 | Count of unique contributors (last 12 months) |
| I | Last Commit Date | 15 | Date | Date format | When code was last changed |
| J | Active Status | 15 | Dropdown | ✅ Active, ðŸ•' Maintenance, ⌠Archived, â" Unknown | Is repository actively developed |
| K | Branch Protection | 18 | Dropdown | ✅ Yes, ⌠No, N/A | Are protected branches configured |
| L | Secret Scanning | 18 | Dropdown | ✅ Yes, ⌠No | Is automated secret detection active |
| M | Backup Status | 15 | Dropdown | ✅ Yes, ⌠No, â" Unknown | Is repository backed up |
| N | Notes | 30 | Text | None | Additional information |

### Data Validation Rules

**Column B (Platform):** Dropdown list
```
Values: GitHub Cloud, GitHub Enterprise, GitLab SaaS, GitLab Self-Hosted, Bitbucket Cloud, Bitbucket Server, Azure DevOps, AWS CodeCommit, Other
Allow blank: No
Error message: "Please select a platform from the dropdown list"
```

**Column E (Classification):** Dropdown list
```
Values: ðŸ"´ Production, 🟡 Internal Tools, 🟢 Open Source, ⚪ Archived
Allow blank: No
Error message: "Please select a classification from the dropdown list"
```

**Column G (Primary Language):** Dropdown list
```
Values: JavaScript, Python, Java, C#, Go, Ruby, PHP, TypeScript, Kotlin, Swift, Other
Allow blank: Yes
```

**Column H (Number of Contributors):** Number validation
```
Type: Whole number
Minimum: 0
Maximum: 10000
Allow blank: Yes
Error message: "Must be a number between 0 and 10000"
```

**Column I (Last Commit Date):** Date validation
```
Type: Date
Minimum: 2000-01-01
Maximum: TODAY()
Allow blank: Yes
Error message: "Must be a valid date"
```

**Columns J, K, L, M:** Dropdown lists (see column definitions for values)

### Conditional Formatting

**Column E (Classification):**

- ðŸ"´ Production: Red fill (#FFC7CE), dark red text
- 🟡 Internal Tools: Yellow fill (#FFEB9C), dark yellow text
- 🟢 Open Source: Green fill (#C6EFCE), dark green text
- ⚪ Archived: Gray fill (#D9D9D9), dark gray text

**Column J (Active Status):**

- ✅ Active: Green background
- ðŸ•' Maintenance: Yellow background
- ⌠Archived: Red background
- â" Unknown: Orange background

**Column K, L, M (Yes/No fields):**

- ✅ Yes: Green background
- ⌠No: Red background

### Freeze Panes
Freeze at **A4** (headers visible when scrolling)

### Cell Protection

- Header rows (1-3): Locked
- Data rows (4+): Unlocked (user input allowed)

---

## Sheet 3: User_Access_Matrix

### Purpose
Document WHO has access to WHICH repositories with WHAT permissions.

### Header Section (Rows 1-3)

**Row 1:** "USER ACCESS MATRIX"  
**Row 2:** "Document user-to-repository access permissions"  
**Row 3:** Column headers

### Column Definitions

| Col | Field Name | Width | Type | Validation | Description |
|-----|------------|-------|------|------------|-------------|
| A | Username | 20 | Text | None | Platform username |
| B | Full Name | 25 | Text | None | Employee legal/preferred name |
| C | Email | 30 | Email | Email format | Primary work email |
| D | Role/Title | 25 | Text | None | Job title |
| E | Department/Team | 25 | Text | None | Organizational unit |
| F | Employment Type | 20 | Dropdown | ðŸ'¤ Employee, 🤠Contractor, ðŸ" Auditor, âš™ï¸ Service Account, 🢠Third-Party | Employment relationship |
| G | Contract End Date | 15 | Date | Date format (for contractors) | When contract expires |
| H | Repository Name | 30 | Text | Must match Sheet 1 Col A | Which repository |
| I | Access Level | 15 | Dropdown | ðŸ'ï¸ Read, âœï¸ Write, ðŸ"§ Admin | Permission level |
| J | Access Grant Date | 15 | Date | Date format | When access was granted |
| K | Access Expiration | 15 | Date | Date format (if time-bound) | When access should end |
| L | Access Justification | 40 | Text | None | Why user needs access |
| M | Approval Reference | 25 | Text | None | Ticket ID or approval documentation |
| N | Last Access Date | 15 | Date | Date format (if available) | When user last accessed |
| O | Access Status | 18 | Dropdown | ✅ Appropriate, âš ï¸ Excessive, ⌠Orphaned, ðŸ•' Expired | Is access appropriate |
| P | Review Date | 15 | Date | Date format | When access was last reviewed |
| Q | Notes | 30 | Text | None | Additional context |

### Data Validation Rules

**Column F (Employment Type):**
```
Values: ðŸ'¤ Employee, 🤠Contractor, ðŸ" Auditor, âš™ï¸ Service Account, 🢠Third-Party
Allow blank: No
```

**Column H (Repository Name):** Dropdown (dynamic from Sheet 1 Column A)
```
Formula: =Repository_Inventory!$A$4:$A$1000
Allow blank: No
Error message: "Repository must exist in Repository_Inventory sheet"
```

**Column I (Access Level):**
```
Values: ðŸ'ï¸ Read, âœï¸ Write, ðŸ"§ Admin
Allow blank: No
```

**Column O (Access Status):**
```
Values: ✅ Appropriate, âš ï¸ Excessive, ⌠Orphaned, ðŸ•' Expired
Allow blank: No
```

### Conditional Formatting

**Column I (Access Level):**

- ðŸ'ï¸ Read: Green background (lowest privilege)
- âœï¸ Write: Yellow background (moderate privilege)
- ðŸ"§ Admin: Red background (highest privilege, requires strong justification)

**Column K (Access Expiration):**

- If Column K < TODAY(): Red background (expired access)
- If Column K >= TODAY() AND Column K <= TODAY()+30: Yellow background (expiring soon)

**Column O (Access Status):**

- ✅ Appropriate: Green background
- âš ï¸ Excessive: Yellow background
- ⌠Orphaned: Red background
- ðŸ•' Expired: Orange background

### Formulas

**Column P (Review Date) - Highlight if overdue:**
```
Conditional formatting rule:
=AND(P4<>"", TODAY()-P4>90)
Format: Red fill (review >90 days old)
```

### Freeze Panes
Freeze at **A4** (headers visible)

---

## Sheet 4: Access_Request_Log

### Purpose
Document access request and approval workflow compliance.

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Request ID | 15 | Text | None |
| B | Request Date | 15 | Date | Date format |
| C | Requestor | 25 | Text | None |
| D | Repository Name | 30 | Text | Dropdown from Sheet 1 |
| E | Access Level | 15 | Dropdown | Read, Write, Admin |
| F | Justification | 40 | Text | None |
| G | Approver | 25 | Text | None |
| H | Approval Date | 15 | Date | Date format |
| I | Provisioned By | 25 | Text | None |
| J | Provisioned Date | 15 | Date | Date format |
| K | Approval Reference | 25 | Text | None |
| L | Compliant Timeline | 18 | Formula | =IF((J4-H4)<=1,"✅ Yes","❌ No") |
| M | Notes | 30 | Text | None |

### Formulas

**Column L (Compliant Timeline):**
```
=IF(J4="","",IF((J4-H4)<=1,"✅ Yes","⌠No"))
```
Checks if provisioning happened within 24 hours (1 day) of approval.

### Conditional Formatting

**Column L:**

- ✅ Yes: Green background
- ⌠No: Red background

---

## Sheet 5: Access_Review_Log

### Purpose
Document quarterly access review completion.

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Review ID | 15 | Text | None |
| B | Review Period | 15 | Text | Format: Q1 2025 |
| C | Repository Name | 30 | Text | Dropdown from Sheet 1 |
| D | Repository Owner | 25 | Text | None |
| E | Review Date | 15 | Date | Date format |
| F | Users Reviewed | 12 | Number | Count |
| G | Appropriate | 12 | Number | Count |
| H | Excessive | 12 | Number | Count |
| I | Orphaned | 12 | Number | Count |
| J | Expired | 12 | Number | Count |
| K | Actions Taken | 40 | Text | None |
| L | Completion Status | 18 | Dropdown | ✅ Complete, ðŸ•' In Progress, ⌠Overdue |
| M | Next Review Due | 15 | Formula | =E4+90 |
| N | Evidence | 25 | Text | File reference |

### Formulas

**Column M (Next Review Due):**
```
=E4+90
```
Adds 90 days to review date for quarterly cycle.

### Conditional Formatting

**Column M (Next Review Due):**
```
=M4<TODAY()
Format: Red fill (review overdue)
```

**Column L (Completion Status):**

- ✅ Complete: Green background
- ðŸ•' In Progress: Yellow background
- ⌠Overdue: Red background

---

## Sheet 6: Deprovisioning_Log

### Purpose
Verify access removal when people leave.

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Termination ID | 15 | Text | None |
| B | Termination Date | 18 | Date | Date format |
| C | Employee Name | 25 | Text | None |
| D | Username | 20 | Text | None |
| E | Employment Type | 20 | Dropdown | Employee, Contractor, Auditor |
| F | Departure Reason | 20 | Dropdown | Resignation, Termination, Contract End, Retirement, Other |
| G | Repos Accessed | 15 | Number | Count |
| H | Repository List | 40 | Text | Comma-separated |
| I | Access Level | 25 | Text | Summary (Read/Write/Admin counts) |
| J | Deprov Ticket | 20 | Text | Ticket ID |
| K | Removal Date | 15 | Date | Date format |
| L | Verified By | 25 | Text | Name |
| M | Verification Date | 18 | Date | Date format |
| N | Compliant Timeline | 18 | Formula | =IF((K4-B4)<=1,"✅ Yes","❌ No") |
| O | Notes | 30 | Text | None |

### Formulas

**Column N (Compliant Timeline):**
```
=IF(K4="","",IF((K4-B4)<=1,"✅ Yes","⌠No"))
```
Checks if removal within 24 hours of termination.

### Conditional Formatting

**Column N:**

- ✅ Yes: Green background
- ⌠No: Red background (critical issue)

---

## Sheet 7: Third_Party_Access

### Purpose
Track contractor/auditor/third-party access with expiration.

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Third Party ID | 15 | Text | None |
| B | Company Name | 30 | Text | None |
| C | Individual Name | 25 | Text | None |
| D | Username | 20 | Text | None |
| E | Role/Purpose | 30 | Text | None |
| F | Contract Start | 15 | Date | Date format |
| G | Contract End | 15 | Date | Date format |
| H | Repository Name | 30 | Text | Dropdown from Sheet 1 |
| I | Access Level | 15 | Dropdown | Read, Write, Admin |
| J | NDA Signed | 15 | Dropdown | ✅ Yes, ⌠No |
| K | NDA Date | 15 | Date | Date format |
| L | NDA Location | 30 | Text | File path |
| M | Access Status | 15 | Dropdown | ✅ Active, ðŸ•' Expired, ⌠Revoked |
| N | Auto-Expire Date | 18 | Formula | =G4 (Contract End) |
| O | Last Reviewed | 15 | Date | Date format |
| P | Notes | 30 | Text | None |

### Formulas

**Column N (Auto-Expire Date):**
```
=G4
```
References Contract End Date.

### Conditional Formatting

**Column J (NDA Signed):**

- ⌠No: Red background (critical - no NDA)

**Column G (Contract End) and Column N (Auto-Expire):**
```
=G4<TODAY()
Format: Red fill (contract expired, access should be removed)
```

**Column M (Access Status):**

- ✅ Active: Green background
- ðŸ•' Expired: Orange background
- ⌠Revoked: Red background

---

## Sheet 8: Service_Accounts

### Purpose
Inventory automation accounts (CI/CD, deployment, scanners).

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Account ID | 15 | Text | None |
| B | Account Name | 25 | Text | Service account username |
| C | Account Type | 20 | Dropdown | CI/CD, Deployment, Security Scanner, Backup, Monitoring, Other |
| D | Purpose | 40 | Text | What does account do |
| E | Repository Name | 30 | Text | Dropdown from Sheet 1 |
| F | Access Level | 15 | Dropdown | Read, Write, Admin |
| G | Justification | 40 | Text | Why this access level |
| H | Owner | 25 | Text | Responsible person/team |
| I | Auth Method | 25 | Dropdown | PAT, SSH Key, OAuth App, GitHub App, Deploy Key |
| J | Token Expiration | 18 | Date | Date format |
| K | Secret Storage | 30 | Text | Where credential stored |
| L | Last Rotation | 15 | Date | Date format |
| M | Next Rotation | 15 | Formula | =L4+365 |
| N | Last Review | 15 | Date | Date format |
| O | Still Required | 15 | Dropdown | ✅ Yes, ⌠No |
| P | Notes | 30 | Text | None |

### Formulas

**Column M (Next Rotation):**
```
=L4+365
```
Annual rotation cycle.

### Conditional Formatting

**Column M (Next Rotation):**
```
=M4<TODAY()
Format: Red fill (rotation overdue)
```

**Column J (Token Expiration):**
```
=J4<TODAY()
Format: Red fill (token expired)
```

**Column O (Still Required):**

- ⌠No: Yellow background (account should be removed)

---

## Sheet 9: Compliance_Scoring

### Purpose
Calculate overall access control compliance score (automated).

### Structure

**Section 1: Metric Calculations (Rows 4-25)**

| Row | Metric | Formula | Target |
|-----|--------|---------|--------|
| 5 | Repository Inventory Completeness | =(COUNTA(Repository_Inventory!A:A)-3)/[Platform Export Count]*100% | 100% |
| 8 | Access Control Compliance | =COUNTIF(Repository_Inventory!K:K,"✅ Yes")/COUNTA(Repository_Inventory!A:A)*100% | 100% |
| 11 | Appropriate Access Rate | =COUNTIF(User_Access_Matrix!O:O,"✅ Appropriate")/COUNTA(User_Access_Matrix!O:O)*100% | ≥95% |
| 14 | Orphaned Account Rate | =COUNTIF(User_Access_Matrix!O:O,"⌠Orphaned")/COUNTA(User_Access_Matrix!A:A)*100% | 0% |
| 17 | Access Review Completion | =COUNTIF(Access_Review_Log!L:L,"✅ Complete")/COUNTA(Repository_Inventory!A:A)*100% | 100% |
| 20 | Deprovisioning SLA | =COUNTIF(Deprovisioning_Log!N:N,"✅ Yes")/COUNTA(Deprovisioning_Log!N:N)*100% | ≥95% |
| 23 | **Overall Score** | =B5*0.15+B8*0.20+B11*0.25+(100-B14)*0.15+B17*0.15+B20*0.10 | **≥85%** |

**Section 2: Scoring Dashboard (Rows 27-35)**

| Metric | Current | Target | Status |
|--------|---------|--------|---------|
| Repository Inventory | [Formula] | 100% | [IF formula] |
| Access Control | [Formula] | 100% | [IF formula] |
| Appropriate Access | [Formula] | ≥95% | [IF formula] |
| Orphaned Accounts | [Formula] | 0% | [IF formula] |
| Review Completion | [Formula] | 100% | [IF formula] |
| Deprovisioning SLA | [Formula] | ≥95% | [IF formula] |
| **OVERALL SCORE** | **[Formula]** | **≥85%** | **[IF formula]** |

**Section 3: Risk Categorization (Rows 37-42)**

```
Risk Level: [IF(B23>=85,"🟢 Low Risk",IF(B23>=70,"🟡 Medium Risk","ðŸ"´ High Risk"))]
```

### Key Formulas

**Overall Compliance Score (Cell B23):**
```
=(B5*0.15)+(B8*0.20)+(B11*0.25)+((100-B14)*0.15)+(B17*0.15)+(B20*0.10)
```

**Status Indicator (Column D - example for row 5):**
```
=IF(B5>=100,"🟢","ðŸ"´")
```

**Risk Categorization (Cell B37):**
```
=IF(B23>=85,"🟢 Low Risk",IF(B23>=70,"🟡 Medium Risk","ðŸ"´ High Risk"))
```

### Conditional Formatting

**Column B (Current Score):**

- ≥Target: Green background
- <Target: Red background

**Column D (Status):**

- 🟢: Green background
- 🟡: Yellow background
- ðŸ"´: Red background

---

## Sheet 10: Gap_Analysis

### Purpose
Document gaps and remediation plans.

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Gap ID | 12 | Text | Format: GAP-001 |
| B | Gap Category | 20 | Dropdown | Access Control, Inventory, Reviews, Deprovisioning, Documentation |
| C | Gap Description | 40 | Text | None |
| D | Policy Requirement | 30 | Text | Which requirement |
| E | Current State | 30 | Text | What is happening |
| F | Desired State | 30 | Text | What should happen |
| G | Risk Level | 15 | Dropdown | ðŸ"´ Critical, 🟠 High, 🟡 Medium, 🟢 Low |
| H | Impact | 40 | Text | What is the risk |
| I | Affected Repos | 30 | Text | Which repositories |
| J | Root Cause | 30 | Text | Why gap exists |
| K | Remediation Plan | 40 | Text | How to fix |
| L | Responsible Party | 25 | Text | Who will fix |
| M | Target Date | 15 | Date | Date format |
| N | Estimated Effort | 20 | Dropdown | 1-2 hours, 1 day, 1 week, 2-4 weeks, >1 month |
| O | Status | 18 | Dropdown | ðŸ"´ Open, 🟡 In Progress, 🟢 Completed, ⚪ Deferred |
| P | Actual Completion | 18 | Date | Date format |
| Q | Verification Method | 30 | Text | How verified |
| R | Verification Date | 18 | Date | Date format |
| S | Notes | 30 | Text | None |

### Conditional Formatting

**Column G (Risk Level):**

- ðŸ"´ Critical: Red fill
- 🟠 High: Orange fill
- 🟡 Medium: Yellow fill
- 🟢 Low: Green fill

**Column M (Target Date):**
```
=M4<TODAY()
Format: Red fill (overdue)
```

**Column O (Status):**

- ðŸ"´ Open: Red background
- 🟡 In Progress: Yellow background
- 🟢 Completed: Green background
- ⚪ Deferred: Gray background

---

## Sheet 11: Evidence_Register

### Purpose
Track evidence for audit.

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Evidence ID | 15 | Text | Format: EV-001 |
| B | Evidence Type | 25 | Dropdown | Access Report, Approval Record, Review Report, Deprovisioning Log, Screenshot, NDA, Other |
| C | Description | 40 | Text | What is this evidence |
| D | Related Requirement | 30 | Text | Policy requirement |
| E | Evidence Date | 15 | Date | Date format |
| F | Evidence Source | 25 | Text | Where it came from |
| G | File Name | 30 | Text | Filename |
| H | File Location | 40 | Text | Path or URL |
| I | Collected By | 25 | Text | Name |
| J | Collection Date | 18 | Date | Date format |
| K | Format | 15 | Dropdown | Excel, PDF, CSV, Screenshot, Email, JSON, Other |
| L | Retention Period | 15 | Text | How long to keep |
| M | Retention End | 15 | Date | Date format |
| N | Auditor Reviewed | 18 | Dropdown | ✅ Yes, ⌠No, ⳠPending |
| O | Auditor Comments | 40 | Text | Notes |
| P | Notes | 30 | Text | Additional info |

### Conditional Formatting

**Column N (Auditor Reviewed):**

- ✅ Yes: Green background
- ⌠No: Yellow background
- â³ Pending: Blue background

---

## Sheet 12: Approval_Sign_Off

### Purpose
Final approval workflow.

### Structure

**Rows 1-10: Assessment Summary**
```
Assessment Document: ISMS-IMP-A.8.4.1
Assessment Period: [User input]
Completion Date: [User input]
Overall Score: [Link to Compliance_Scoring!B23]
Risk Level: [Link to Compliance_Scoring!B37]
Status: [Dropdown: Draft/Final/Requires Remediation]
```

**Rows 12-18: Assessment Completed By**
```
Name: [User input]
Role: [User input]
Date: [User input]
Signature: [User input]
```

**Rows 20-26: Repository Owner Approvals** (3-5 blocks)
```
Name: [User input]
Date: [User input]
Signature: [User input]
```

**Rows 28-34: Information Security Manager**
```
Name: [User input]
Date: [User input]
Review Notes: [Text area]
Recommendation: [Dropdown: Approve/Approve with Conditions/Reject]
```

**Rows 36-42: CISO Approval**
```
Name: [User input]
Date: [User input]
Decision: [Dropdown: Approved/Approved with Conditions/Rejected]
Conditions: [Text area]
```

**Rows 44-46: Next Review**
```
Next Review Date: [Formula: Completion Date + 90 days]
Responsible: [User input]
Notes: [User input]
```

---

## Cell Styling Reference

### Header Styles

**Main Header (Sheet Title - Row 1):**

- Font: Calibri 14pt bold white
- Fill: Dark blue (#003366)
- Alignment: Center, vertical center
- Height: 40px

**Subheader (Row 2):**

- Font: Calibri 11pt bold white
- Fill: Medium blue (#4472C4)
- Alignment: Center, vertical center
- Height: 30px

**Column Header (Row 3):**

- Font: Calibri 10pt bold black
- Fill: Light gray (#D9D9D9)
- Alignment: Center, vertical center, text wrap
- Border: Thin black on all sides
- Height: 30px

### Input Cell Styles

**User Input Cells:**

- Fill: Light yellow (#FFFFCC)
- Alignment: Left (text), Right (numbers), Center (dates)
- Border: Thin gray on all sides
- Font: Calibri 10pt regular black

**Formula Cells (Read-only):**

- Fill: Light blue (#E7F3FF)
- Alignment: Center
- Border: Thin gray
- Font: Calibri 10pt regular black
- Protection: Locked

### Status Color Coding

**Green (Compliant/Good):**

- Fill: #C6EFCE
- Text: #006100

**Yellow (Warning/Partial):**

- Fill: #FFEB9C
- Text: #9C6500

**Red (Non-Compliant/Critical):**

- Fill: #FFC7CE
- Text: #9C0006

**Orange (Expired/Attention):**

- Fill: #FFD8B1
- Text: #C65911

**Blue (In Progress/Pending):**

- Fill: #B4C7E7
- Text: #002060

**Gray (N/A/Deferred):**

- Fill: #D9D9D9
- Text: #404040

---

## Freeze Panes Configuration

**All Assessment Sheets (Sheets 2-11):**

- Freeze at **A4** (rows 1-3 remain visible when scrolling)

**Approval Sheet (Sheet 12):**

- Freeze at **A3** (title remains visible)

---

## Cell Protection

**Protected (Locked) Cells:**

- All header rows (rows 1-3)
- Formula cells (Compliance_Scoring sheet)
- Instructions (Sheet 1)

**Unprotected (Unlocked) Cells:**

- All user input cells (light yellow background)
- Data entry rows (row 4 onwards in assessment sheets)

**Sheet Protection Settings:**

- Allow: Select unlocked cells, format cells, insert rows, delete rows, sort, filter
- Disallow: Edit locked cells, modify formulas, delete sheets
- Password: [Optional - set during script generation]

---

## Quality Assurance

### Validation Script

**Script Name:** `excel_sanity_check_a84_1.py`

**Purpose:** Validate generated workbook matches this specification.

**Checks Performed:**
1. All 12 sheets exist with correct names
2. Column counts match specification
3. Data validation dropdowns configured correctly
4. Conditional formatting ranges applied
5. Formulas present and syntactically correct
6. Freeze panes configured
7. Cell protection enabled
8. Styling consistent across sheets

**Usage:**
```bash
python excel_sanity_check_a84_1.py ISMS-IMP-A.8.4.1_Repository_Access_20260125.xlsx
```

**Output:**
```
✅ All sheets present
✅ Column structure validated
✅ Data validation configured
✅ Conditional formatting applied
✅ Formulas validated
✅ Styling consistent
🟢 Workbook passes all checks
```

---

## Version Control

### Workbook Versioning

**Filename Convention:** `ISMS-IMP-A.8.4.1_Repository_Access_YYYYMMDD.xlsx`

**Version Tracking:** Embedded in Instructions_Legend sheet

**Change Log:**

- v1.0: Initial workbook structure (2026-01-25)

---

## Backward Compatibility

**Excel Compatibility:** Excel 2016+, Excel 365

**Migration from v1.0 to v2.0** (if future versions):

- Migration script: `migrate_a84_1_v1_to_v2.py`
- Preserves user data
- Updates formulas and validation rules
- Adds new columns/sheets as needed

---

**END OF SPECIFICATION**

---

*"Cryptanalysis is like solving a puzzle where the puzzle maker actively tries to stop you."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
