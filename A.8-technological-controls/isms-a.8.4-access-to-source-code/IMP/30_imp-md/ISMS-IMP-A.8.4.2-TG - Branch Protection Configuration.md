**ISMS-IMP-A.8.4.2-TG - Branch Protection Configuration**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.4: Access to Source Code

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.4.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Branch Protection and Code Review Compliance |
| **Related Policy** | ISMS-POL-A.8.4, Section 2.4 (Branch Protection and Code Review) |
| **Purpose** | Document and assess branch protection configurations across all repository platforms to enforce code review and prevent unauthorized code changes |
| **Target Audience** | Repository Owners, DevOps Engineers, Security Team, Development Team Leads, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Branch Protection assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.4.2-UG.

---

# Technical Specification

**Audience:** Python/Excel Script Maintainers, Assessment Workbook Developers

---

## Instructions for Workbook Development

### Workbook Generation

**Primary Script:** `generate_a84_2_branch_protection.py`

**Purpose:** Generate Excel workbook (`ISMS-IMP-A.8.4.2_Branch_Protection_YYYYMMDD.xlsx`) with pre-configured sheets, data validation, conditional formatting, and formulas.

**Key Functions:**

- `create_workbook()`: Initialize workbook and sheets
- `setup_styles()`: Cell styles, fonts, fills, borders
- `create_branch_protection_sheets()`: Generate assessment sheets
- `create_compliance_formulas()`: Compliance calculations
- `create_evidence_register()`: Evidence tracking
- `create_approval_signoff()`: Approval workflow

**File Naming:** `ISMS-IMP-A.8.4.2_Branch_Protection_YYYYMMDD.xlsx`

---

## Workbook Structure Overview

### Sheet List (10 Sheets Total)

| Sheet # | Sheet Name | Purpose | Rows | Columns | Entry Type |
|---------|------------|---------|------|---------|------------|
| 1 | Instructions_Legend | User guide | ~50 | A-B | Read-only |
| 2 | Repository_Branch_Inventory | Branch inventory | Variable | A-H | User input |
| 3 | Branch_Protection_Details | Protection rules | Variable | A-M | User input |
| 4 | Pull_Request_Configuration | PR settings | Variable | A-H | User input |
| 5 | Status_Check_Verification | CI/CD checks | Variable | A-I | User input |
| 6 | Signed_Commits_Audit | GPG adoption | Variable | A-F | User input |
| 7 | Exception_Management | Exception tracking | Variable | A-H | User input |
| 8 | Compliance_Scoring | Automated metrics | ~50 | A-D | Formula |
| 9 | Gap_Analysis | Gap remediation | Variable | A-S | User input |
| 10 | Evidence_Register | Evidence docs | Variable | A-P | User input |
| 11 | Approval_Sign_Off | Final approval | ~40 | A-B | User input |

---

## Sheet 2: Repository_Branch_Inventory

### Purpose
Document all branches requiring protection.

### Column Definitions

| Col | Field Name | Width | Type | Validation | Description |
|-----|------------|-------|------|------------|-------------|
| A | Repository Name | 30 | Text | From IMP-S1 | Repository being assessed |
| B | Repository Platform | 20 | Dropdown | GitHub Cloud, GitHub Enterprise, GitLab SaaS, GitLab Self-Hosted, Bitbucket Cloud, Bitbucket Server, Azure DevOps | Hosting platform |
| C | Repository Classification | 20 | Dropdown | 🔴 Production, 🟡 Internal Tools, 🟢 Open Source, ⚪ Archived | From IMP-S1 |
| D | Branch Name | 25 | Text | None | Exact branch name (main, release/v1.0) |
| E | Branch Type | 18 | Dropdown | Main, Release, Development, Feature, Hotfix | Branch category |
| F | Protection Required | 18 | Dropdown | ✅ Yes, ❌ No, ➖ N/A | Per policy requirements |
| G | Protection Configured | 20 | Dropdown | ✅ Yes, ❌ No, ⚠️ Partial | Current platform status |
| H | Status | 18 | Formula | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant | Compliance status |

### Data Validation

**Column B (Repository Platform):**
```
Values: GitHub Cloud, GitHub Enterprise, GitLab SaaS, GitLab Self-Hosted, Bitbucket Cloud, Bitbucket Server, Azure DevOps, AWS CodeCommit, Other
Allow blank: No
```

**Column C (Repository Classification):**
```
Values: 🔴 Production, 🟡 Internal Tools, 🟢 Open Source, ⚪ Archived
Allow blank: No
```

**Column E (Branch Type):**
```
Values: Main, Release, Development, Feature, Hotfix
Allow blank: No
```

**Column F (Protection Required):**
```
Values: ✅ Yes, ❌ No, ➖ N/A
Allow blank: No
```

**Column G (Protection Configured):**
```
Values: ✅ Yes, ❌ No, ⚠️ Partial
Allow blank: No
```

### Formulas

**Column H (Status):**
```excel
=IF(F4="✅ Yes",
  IF(G4="✅ Yes", "✅ Compliant",
    IF(G4="⚠️ Partial", "⚠️ Partial", "❌ Non-Compliant")),
  "➖ N/A")
```

### Conditional Formatting

**Column C (Classification):**

- 🔴 Production: Red fill (#FFC7CE)
- 🟡 Internal Tools: Yellow fill (#FFEB9C)
- 🟢 Open Source: Green fill (#C6EFCE)
- ⚪ Archived: Gray fill (#D9D9D9)

**Column H (Status):**

- ✅ Compliant: Green background
- ⚠️ Partial: Yellow background
- ❌ Non-Compliant: Red background

---

## Sheet 3: Branch_Protection_Details

### Purpose
Document specific protection rules per branch.

### Column Definitions

| Col | Field Name | Width | Type | Validation | Description |
|-----|------------|-------|------|------------|-------------|
| A | Repository Name | 30 | Text | From Sheet 2 | Repository name |
| B | Branch Name | 25 | Text | From Sheet 2 | Branch name |
| C | Direct Commits Blocked | 20 | Dropdown | ✅ Yes, ❌ No | PR required enforcement |
| D | Pull Request Required | 20 | Dropdown | ✅ Yes, ❌ No | Same as Column C |
| E | Required Approvals | 12 | Number | 0-5 | Minimum reviewer count |
| F | Dismiss Stale Reviews | 20 | Dropdown | ✅ Yes, ❌ No | Invalidate old approvals |
| G | Code Owner Review | 20 | Dropdown | ✅ Yes, ❌ No, ➖ N/A | CODEOWNERS enforcement |
| H | Status Checks Required | 20 | Dropdown | ✅ Yes, ❌ No, ⚠️ Partial | CI/CD enforcement |
| I | Status Check List | 40 | Text | None | Comma-separated checks |
| J | Signed Commits | 20 | Dropdown | ✅ Yes, ❌ No, ➖ N/A | GPG requirement |
| K | Linear History | 18 | Dropdown | ✅ Yes, ❌ No | Merge commit prevention |
| L | Compliance Score | 12 | Formula | Percentage | % rules configured |
| M | Status | 18 | Formula | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant | Overall status |

### Data Validation

**Columns C, D, F, K:**
```
Values: ✅ Yes, ❌ No
Allow blank: No
```

**Columns G, J:**
```
Values: ✅ Yes, ❌ No, ➖ N/A
Allow blank: No
```

**Column H:**
```
Values: ✅ Yes, ❌ No, ⚠️ Partial
Allow blank: No
```

**Column E (Required Approvals):**
```
Type: Whole number
Minimum: 0
Maximum: 5
Allow blank: No
```

### Formulas

**Column L (Compliance Score) - Production Code:**
```excel
=IF(C4="", "",
  (IF(C4="✅ Yes",1,0) +
   IF(D4="✅ Yes",1,0) +
   IF(E4>=2,1,IF(E4>=1,0.5,0)) +
   IF(F4="✅ Yes",1,0) +
   IF(H4="✅ Yes",1,IF(H4="⚠️ Partial",0.5,0))
  ) / 5 * 100)
```

**Column M (Status):**
```excel
=IF(L4="", "",
  IF(L4=100, "✅ Compliant",
    IF(L4>=50, "⚠️ Partial", "❌ Non-Compliant")))
```

### Conditional Formatting

**Column E (Required Approvals):**

- ≥2: Green background (production standard)
- 1: Yellow background (internal tools standard)
- 0: Red background (non-compliant)

**Column L (Compliance Score):**

- 100%: Green background
- 50-99%: Yellow background
- <50%: Red background

**Column M (Status):**

- ✅ Compliant: Green background
- ⚠️ Partial: Yellow background
- ❌ Non-Compliant: Red background

---

## Sheet 4: Pull_Request_Configuration

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Repository Name | 30 | Text | From Sheet 2 |
| B | Minimum Reviewers | 12 | Number | 0-5 |
| C | Code Owner Review | 20 | Dropdown | ✅ Required, ⚠️ Optional, ❌ No |
| D | Dismiss Stale Approvals | 20 | Dropdown | ✅ Yes, ❌ No |
| E | Restrict Dismiss | 20 | Dropdown | ✅ Yes, ❌ No |
| F | Conversation Resolution | 20 | Dropdown | ✅ Required, ⚠️ Optional, ❌ No |
| G | Self-Approval Blocked | 20 | Dropdown | ✅ Yes, ❌ No |
| H | Compliance Status | 18 | Formula | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |

### Formulas

**Column H (Compliance Status):**
```excel
=IF(B4>=1,
  IF(AND(D4="✅ Yes", G4="✅ Yes"), "✅ Compliant",
    IF(OR(D4="✅ Yes", G4="✅ Yes"), "⚠️ Partial", "❌ Non-Compliant")),
  "❌ Non-Compliant")
```

---

## Sheet 5: Status_Check_Verification

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Repository Name | 30 | Text | From Sheet 2 |
| B | Status Checks Configured | 22 | Dropdown | ✅ Yes, ❌ No |
| C | Build Check | 18 | Dropdown | ✅ Configured, ❌ Missing |
| D | Test Check | 18 | Dropdown | ✅ Configured, ❌ Missing |
| E | Lint Check | 18 | Dropdown | ✅ Configured, ❌ Missing |
| F | Security Check | 18 | Dropdown | ✅ Configured, ❌ Missing |
| G | All Checks Must Pass | 20 | Dropdown | ✅ Yes, ❌ No |
| H | Up-to-Date Before Merge | 22 | Dropdown | ✅ Yes, ❌ No |
| I | Compliance Status | 18 | Formula | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |

### Formulas

**Column I (Compliance Status):**
```excel
=IF(B4="✅ Yes",
  IF(AND(C4="✅ Configured", D4="✅ Configured", G4="✅ Yes"),
    "✅ Compliant",
    IF(OR(C4="✅ Configured", D4="✅ Configured"), "⚠️ Partial", "❌ Non-Compliant")),
  "❌ Non-Compliant")
```

---

## Sheet 6: Signed_Commits_Audit

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Repository Name | 30 | Text | From Sheet 2 |
| B | Signed Commits Required | 22 | Dropdown | ✅ Yes, ❌ No, ➖ N/A |
| C | % Commits Signed (Last 30d) | 22 | Number | 0-100% |
| D | GPG Infrastructure | 20 | Dropdown | ✅ Implemented, ⚠️ Partial, ❌ Missing |
| E | Developer Training | 20 | Dropdown | ✅ Completed, ⚠️ In Progress, ❌ Not Started |
| F | Compliance Status | 18 | Formula | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |

### Formulas

**Column F (Compliance Status):**
```excel
=IF(B4="✅ Yes",
  IF(C4>=80, "✅ Compliant",
    IF(C4>=50, "⚠️ Partial", "❌ Non-Compliant")),
  IF(B4="➖ N/A", "➖ N/A", "✅ Compliant"))
```

### Conditional Formatting

**Column C (% Commits Signed):**

- ≥80%: Green background
- 50-79%: Yellow background
- <50%: Red background

---

## Sheet 7: Exception_Management

### Column Definitions

| Col | Field Name | Width | Type | Validation |
|-----|------------|-------|------|------------|
| A | Exception ID | 15 | Text | Format: EXC-001 |
| B | Repository/Branch | 30 | Text | "repo / branch" |
| C | Exception Reason | 40 | Text | Justification |
| D | Granted By | 25 | Text | Approver name |
| E | Grant Date | 15 | Date | Date format |
| F | Expiration Date | 15 | Date | Date format |
| G | Review Date | 15 | Date | Date format |
| H | Status | 15 | Formula | 🟢 Active, 🔴 Expired, ⚪ Revoked |

### Formulas

**Column H (Status):**
```excel
=IF(F4<TODAY(), "🔴 Expired",
  IF(F4="", "⚪ Revoked", "🟢 Active"))
```

### Conditional Formatting

**Column H (Status):**

- 🔴 Expired: Red background (CRITICAL)
- 🟢 Active: Green background
- ⚪ Revoked: Gray background

**Column F (Expiration Date):**
```
=F4<TODAY()
Format: Red fill (expired)
```

---

## Sheet 8: Compliance_Scoring

### Purpose
Calculate overall branch protection compliance (automated).

### Metrics Calculated

**Row 5: Branch Protection Configuration Rate**
```excel
Cell B5: =COUNTIF(Repository_Branch_Inventory!H:H,"✅ Compliant")/
         COUNTIF(Repository_Branch_Inventory!F:F,"✅ Yes")*100
Target C5: 100%
Status D5: =IF(B5>=100,"🟢","🔴")
```

**Row 8: Pull Request Enforcement Rate**
```excel
Cell B8: =COUNTIF(Branch_Protection_Details!D:D,"✅ Yes")/
         COUNTA(Branch_Protection_Details!A:A)*100
Target C8: ≥95%
Status D8: =IF(B8>=95,"🟢",IF(B8>=80,"🟡","🔴"))
```

**Row 11: Status Check Compliance Rate**
```excel
Cell B11: =COUNTIF(Status_Check_Verification!I:I,"✅ Compliant")/
          COUNTIF(Status_Check_Verification!B:B,"✅ Yes")*100
Target C11: 100%
Status D11: =IF(B11>=100,"🟢","🔴")
```

**Row 14: Signed Commit Adoption Rate**
```excel
Cell B14: =AVERAGE(Signed_Commits_Audit!C:C)
Target C14: ≥80%
Status D14: =IF(B14>=80,"🟢",IF(B14>=50,"🟡","🔴"))
```

**Row 17: Overall Branch Protection Score**
```excel
Cell B17: =(B5*0.40)+(B8*0.30)+(B11*0.20)+(B14*0.10)
Target C17: ≥85%
```

**Row 20: Risk Categorization**
```excel
Cell B20: =IF(B17>=85,"🟢 Low Risk",
              IF(B17>=70,"🟡 Medium Risk","🔴 High Risk"))
```

### Conditional Formatting

**Column B (Current Score):**

- ≥Target: Green background
- <Target: Red background

**Row 20 (Risk Level):**

- 🟢 Low Risk: Green background
- 🟡 Medium Risk: Yellow background
- 🔴 High Risk: Red background

---

## Sheet 9: Gap_Analysis

### Structure

Same as IMP-S1 Gap_Analysis with standard columns:

- Gap ID, Gap Category, Gap Description
- Policy Requirement, Current State, Desired State
- Risk Level, Impact, Affected Repos
- Root Cause, Remediation Plan
- Responsible Party, Target Date, Estimated Effort
- Status, Actual Completion, Verification Method, Verification Date
- Notes

**Reference IMP-S1 PART II for detailed specifications**

---

## Sheet 10: Evidence_Register

### Structure

Same as IMP-S1 Evidence_Register with standard columns:

- Evidence ID, Evidence Type, Description
- Related Requirement, Evidence Date, Evidence Source
- File Name, File Location
- Collected By, Collection Date, Format
- Retention Period, Retention End, Auditor Reviewed
- Auditor Comments, Notes

**Reference IMP-S1 PART II for detailed specifications**

---

## Sheet 11: Approval_Sign_Off

### Structure

Same as IMP-S1 Approval_Sign_Off:

- Assessment Summary (links to Compliance_Scoring)
- Assessment Completed By
- Repository Owner Approvals (3-5 blocks)
- Information Security Manager Review
- CISO Approval
- Next Review Date (+90 days)

**Reference IMP-S1 PART II for detailed specifications**

---

## Cell Styling Reference

### Header Styles

**Main Header (Row 1):**

- Font: Calibri 14pt bold white
- Fill: #003366 (dark blue)
- Alignment: Center
- Height: 40px

**Subheader (Row 2):**

- Font: Calibri 11pt bold white
- Fill: #4472C4 (medium blue)
- Alignment: Center
- Height: 30px

**Column Header (Row 3):**

- Font: Calibri 10pt bold black
- Fill: #D9D9D9 (light gray)
- Alignment: Center, text wrap
- Border: Thin black

### Input Cell Styles

**User Input:**

- Fill: #FFFFCC (light yellow)
- Border: Thin gray
- Font: Calibri 10pt

**Formula (Read-only):**

- Fill: #E7F3FF (light blue)
- Protection: Locked
- Font: Calibri 10pt

### Status Colors

**Green (Compliant):**

- Fill: #C6EFCE
- Text: #006100

**Yellow (Partial/Warning):**

- Fill: #FFEB9C
- Text: #9C6500

**Red (Non-Compliant):**

- Fill: #FFC7CE
- Text: #9C0006

**Blue (In Progress):**

- Fill: #B4C7E7
- Text: #002060

**Gray (N/A):**

- Fill: #D9D9D9
- Text: #404040

---

## Freeze Panes

**All Assessment Sheets (2-10):**

- Freeze at **A4** (headers visible when scrolling)

**Approval Sheet (11):**

- Freeze at **A3**

---

## Cell Protection

**Protected:**

- Header rows (1-3)
- Formula cells (Compliance_Scoring)
- Instructions sheet

**Unprotected:**

- User input cells (light yellow)
- Data entry rows (4+)

**Sheet Protection:**

- Allow: Select unlocked, format cells, insert rows, delete rows, sort, filter
- Disallow: Edit locked cells, modify formulas

---

## Quality Assurance

### Validation Script

**Script:** `excel_sanity_check_a84_2.py`

**Checks:**
1. All 11 sheets exist
2. Column counts match specification
3. Data validation configured
4. Conditional formatting applied
5. Formulas syntactically correct
6. Freeze panes configured
7. Cell protection enabled
8. Styling consistent

**Usage:**
```bash
python excel_sanity_check_a84_2.py ISMS-IMP-A.8.4.2_Branch_Protection_20260125.xlsx
```

---

## Version Control

**Filename:** `ISMS-IMP-A.8.4.2_Branch_Protection_YYYYMMDD.xlsx`

**Change Log:**

- v1.0: Initial workbook structure

---

**END OF SPECIFICATION**

---

*"Secret sharing allows us to distribute trust among multiple parties, eliminating single points of failure."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
