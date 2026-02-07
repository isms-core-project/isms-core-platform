**ISMS-IMP-A.6.6.3-TG - NDA Review and Compliance**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.6: Confidentiality or Non-Disclosure Agreements

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.6.3-TG |
| **Document Title** | NDA Review and Compliance Workbook Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.6.6: Confidentiality or Non-Disclosure Agreements |
| **Parent Policy** | ISMS-POL-A.6.6 (Confidentiality and Non-Disclosure Agreements) |
| **Version** | 1.0 |
| **Classification** | Internal |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial implementation specification for ISO 27001:2022 first certification |

---

# Technical Specification


> Auto-generated from `generate_a66_3_nda_review_compliance.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.6.6.3` |
| **Output Filename** | `ISMS-IMP-A.6.6.3_NDA_Review_and_Compliance_YYYYMMDD.xlsx` |
| **Workbook Title** | NDA Review and Compliance |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Workbook

---

## Sheet 2: Instructions

---

## Sheet 3: Periodic_Review

**Data Rows:** 48 (rows 3–50) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Review_ID | 14 |
| B | Review_Type | 20 |
| C | Review_Scope | 30 |
| D | Planned_Date | 14 |
| E | Actual_Date | 14 |
| F | Reviewer | 22 |
| G | Findings_Count | 14 |
| H | Gaps_Identified | 14 |
| I | Status | 14 |
| J | Next_Review | 14 |
| K | Notes | 35 |

---

## Sheet 4: Template_Adequacy

**Data Rows:** 48 (rows 3–50) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Template_ID | 14 |
| B | Template_Name | 30 |
| C | Last_Legal_Review | 16 |
| D | Regulatory_Current | 16 |
| E | Covers_All_Info_Types | 18 |
| F | Post_Term_Adequate | 16 |
| G | Remedies_Adequate | 16 |
| H | Jurisdiction_Correct | 16 |
| I | Overall_Adequacy | 16 |
| J | Score | 10 |
| K | Action_Required | 30 |
| L | Notes | 30 |

---

## Sheet 5: Coverage_Analysis

**Data Rows:** 18 (rows 3–20) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Stakeholder_Category | 22 |
| B | Total_Count | 12 |
| C | NDA_Required | 12 |
| D | NDA_Signed | 12 |
| E | Coverage_Rate | 14 |
| F | Expired_NDAs | 12 |
| G | Missing_NDAs | 12 |
| H | Gap_Status | 14 |
| I | Remediation_Owner | 20 |
| J | Notes | 35 |

---

## Sheet 6: Compliance_Check

**Data Rows:** 98 (rows 3–100) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | NDA_ID | 14 |
| B | Counterparty | 25 |
| C | Correctly_Executed | 16 |
| D | Within_Validity | 14 |
| E | Appropriate_Template | 18 |
| F | All_Parties_Signed | 16 |
| G | Securely_Stored | 14 |
| H | Overall_Compliance | 16 |
| I | Issues_Found | 35 |
| J | Action_Required | 30 |
| K | Status | 14 |

---

## Sheet 7: Gap_Register

**Data Rows:** 48 (rows 3–50) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap_ID | 12 |
| B | Gap_Type | 18 |
| C | Description | 45 |
| D | Affected_Area | 22 |
| E | Severity | 12 |
| F | Identified_Date | 14 |
| G | Owner | 20 |
| H | Remediation_Action | 40 |
| I | Target_Date | 14 |
| J | Status | 14 |
| K | Closure_Date | 14 |
| L | Notes | 30 |

---

## Sheet 8: Evidence_Register

**Data Rows:** 48 (rows 3–50) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence_ID | 14 |
| B | Review_Ref | 14 |
| C | Evidence_Type | 22 |
| D | Description | 40 |
| E | Storage_Location | 35 |
| F | Collected_Date | 14 |
| G | Collected_By | 20 |
| H | Retention_Until | 14 |

---

## Sheet 9: Approval

**Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Approval_Type | 25 |
| B | Approver_Role | 25 |
| C | Approver_Name | 25 |
| D | Signature | 20 |
| E | Date | 14 |
| F | Comments | 35 |

---

**END OF SPECIFICATION**

---

*"In God we trust; all others must bring data."*
— W. Edwards Deming

<!-- QA_VERIFIED: 2026-02-06 -->
