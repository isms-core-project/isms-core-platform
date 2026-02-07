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


---
# Technical Specification
**Audience:** Python/Excel Script Maintainers, Assessment Workbook Developers


> Auto-generated from `generate_a84_2_branch_protection.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.4.2` |
| **Output Filename** | `ISMS-IMP-A.8.4.2_Branch_Protection_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Branch Protection Assessment |
| **Total Sheets** | 19 (19 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: Repository_Branch_Inventory

---

## Sheet 3: Branch_Protection_Details

---

## Sheet 4: Pull_Request_Configuration

---

## Sheet 5: Status_Check_Verification

---

## Sheet 6: Signed_Commits_Audit

---

## Sheet 7: Exception_Management

---

## Sheet 8: Compliance_Scoring

---

## Sheet 9: Gap_Analysis

---

## Sheet 10: Evidence_Register

---

## Sheet 11: Approval_Sign_Off

---

## Sheet 12: Base_Validations

---

## Sheet 13: Instructions

---

## Sheet 14: Branch_Inventory

**Data Rows:** 496 (rows 5–500)

### Columns

| Col | Header |
|-----|--------|
| A | Repository Name |
| B | Repository Platform |
| C | Repository Classification |
| D | Branch Name |
| E | Branch Type |
| F | Protection Required |
| G | Protection Configured |
| H | Status |

---

## Sheet 15: Protection_Details

**Data Rows:** 496 (rows 5–500)

### Columns

| Col | Header |
|-----|--------|
| A | Repository Name |
| B | Branch Name |
| C | Direct Commits Blocked |
| D | Pull Request Required |
| E | Required Approvals |
| F | Dismiss Stale Reviews |
| G | Code Owner Review |
| H | Status Checks Required |
| I | Status Check List |
| J | Signed Commits Required |
| K | Linear History |
| L | Compliance Score (%) |
| M | Status |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| LN | `=((COUNTIF(C{row}:K{row},` |  |

---

## Sheet 16: Pr_Configuration

**Data Rows:** 496 (rows 5–500)

### Columns

| Col | Header |
|-----|--------|
| A | Repository Name |
| B | Minimum Reviewers |
| C | Code Owner Review |
| D | Dismiss Stale Approvals |
| E | Restrict Dismiss |
| F | Conversation Resolution |
| G | Self-Approval Blocked |
| H | Compliance Status |

---

## Sheet 17: Status_Check

**Data Rows:** 496 (rows 5–500)

### Columns

| Col | Header |
|-----|--------|
| A | Repository Name |
| B | Status Checks Configured |
| C | Build Check |
| D | Test Check |
| E | Lint Check |
| F | Security Check |
| G | All Checks Must Pass |
| H | Up-to-Date Before Merge |
| I | Compliance Status |

---

## Sheet 18: Signed_Commits

**Data Rows:** 496 (rows 5–500)

### Columns

| Col | Header |
|-----|--------|
| A | Repository Name |
| B | Signed Commits Required |
| C | % Commits Signed (30 days) |
| D | GPG Infrastructure |
| E | Developer Training |
| F | Compliance Status |

---

## Sheet 19: Approval_Signoff

---

**END OF SPECIFICATION**

---

*"Secret sharing allows us to distribute trust among multiple parties, eliminating single points of failure."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
