<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.35-36.S3-TG:framework:TG:a.5.35-36 -->
**ISMS-IMP-A.5.35-36.S3-TG - Findings and Remediation Management**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.35-36

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.35-36.S3-TG |
| **Title** | Findings and Remediation Management |
| **Control Reference** | ISO/IEC 27001:2022 A.5.35-36 |
| **Control Name** | Compliance and Review |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

# Technical Specification


> Auto-generated from `generate_a535_36_3_findings_remediation.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.35-36.S3` |
| **Output Filename** | `ISMS-IMP-A.5.35-36.S3_Findings_and_Remediation_Management_YYYYMMDD.xlsx` |
| **Workbook Title** | Findings and Remediation Management |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #808080 | 808080 | Gray (Disabled) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E2EFDA | E2EFDA | Pale Green (Success Background) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Workbook

---

## Sheet 2: Instructions

**Frozen Panes:** A4

---

## Sheet 3: Findings_Register

**Data Rows:** 100 (rows 4–103) | **Frozen Panes:** D4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Finding_ID | 14 |
| B | Source | 18 |
| C | Source_Ref | 16 |
| D | Finding_Date | 14 |
| E | Finding_Type | 16 |
| F | Severity | 14 |
| G | Control_Reference | 18 |
| H | Finding_Description | 50 |
| I | Root_Cause | 35 |
| J | Recommendation | 40 |
| K | Owner | 22 |
| L | Target_Date | 14 |
| M | Status | 16 |
| N | Days_Open | 12 |

---

## Sheet 4: Remediation_Actions

**Data Rows:** 200 (rows 4–203) | **Frozen Panes:** D4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Action_ID | 14 |
| B | Finding_Ref | 14 |
| C | Action_Description | 50 |
| D | Action_Type | 18 |
| E | Owner | 22 |
| F | Start_Date | 14 |
| G | Target_Date | 14 |
| H | Actual_Date | 14 |
| I | Status | 16 |
| J | % Complete | 12 |
| K | Verification_Method | 25 |
| L | Notes | 30 |

---

## Sheet 5: Root_Cause_Analysis

**Data Rows:** 50 (rows 4–53) | **Frozen Panes:** C4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | RCA_ID | 12 |
| B | Finding_Ref | 14 |
| C | Problem_Statement | 40 |
| D | Analysis_Method | 18 |
| E | Root_Cause_Category | 22 |
| F | Root_Cause_Description | 45 |
| G | Contributing_Factors | 35 |
| H | Systemic_Issue | 14 |
| I | Preventive_Actions | 40 |
| J | Analyst | 22 |
| K | Analysis_Date | 14 |

---

## Sheet 6: Verification_Log

**Data Rows:** 100 (rows 4–103) | **Frozen Panes:** D4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Verification_ID | 14 |
| B | Finding_Ref | 14 |
| C | Action_Ref | 14 |
| D | Verification_Date | 16 |
| E | Verifier | 22 |
| F | Verification_Method | 25 |
| G | Evidence_Reviewed | 35 |
| H | Verification_Result | 18 |
| I | Closure_Recommendation | 22 |
| J | Follow_Up_Required | 16 |
| K | Notes | 30 |

---

## Sheet 7: Trend_Analysis

**Data Rows:** 9 (rows 2–10) | **Frozen Panes:** B4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Period | 16 |
| B | Major_NCs | 12 |
| C | Minor_NCs | 12 |
| D | Observations | 14 |
| E | Total_Findings | 14 |
| F | Closed_This_Period | 16 |
| G | Open_at_Period_End | 18 |
| H | Avg_Days_to_Close | 16 |
| I | Repeat_Findings | 14 |
| J | Notes | 35 |

---

## Sheet 8: Evidence_Register

**Data Rows:** 100 (rows 4–103) | **Frozen Panes:** C4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence_ID | 15 |
| B | Evidence_Type | 22 |
| C | Description | 45 |
| D | Related_Finding | 18 |
| E | Collection_Date | 16 |
| F | Location | 40 |
| G | Collected_By | 25 |
| H | Retention_Until | 16 |

---

## Sheet 9: Approval_Signoff

**Data Rows:** 200 (rows 4–203) | **Frozen Panes:** A3

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Findings_Register!A4:A103)-COUNTBLANK(Findings_Register!B4:B103)` | Total Findings |
| — | `=COUNTIFS(Findings_Register!F4:F103,` | Open Major NCs |
| — | `=COUNTIF(Findings_Register!M4:M103,` | Findings Closed This Period |
| — | `=COUNTIF(Remediation_Actions!I4:I203,` | Actions In Progress |

---

**END OF SPECIFICATION**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
