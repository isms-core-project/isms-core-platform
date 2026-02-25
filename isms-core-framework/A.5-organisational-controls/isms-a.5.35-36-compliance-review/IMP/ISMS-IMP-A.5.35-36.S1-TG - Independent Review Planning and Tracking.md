<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.35-36.S1-TG:framework:TG:a.5.35-36 -->
**ISMS-IMP-A.5.35-36.S1-TG - Independent Review Planning and Tracking**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.35

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.35-36.S1-TG |
| **Title** | Independent Review Planning and Tracking |
| **Control Reference** | ISO/IEC 27001:2022 A.5.35 |
| **Control Name** | Independent Review of Information Security |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

# Technical Specification


> Auto-generated from `generate_a535_36_1_independent_review.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.35-36.S1` |
| **Output Filename** | `ISMS-IMP-A.5.35-36.S1_Independent_Review_Planning_and_Tracking_YYYYMMDD.xlsx` |
| **Workbook Title** | Independent Review Planning and Tracking |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #808080 | 808080 | Gray (Disabled) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Review_Schedule

---

## Sheet 3: Reviewer_Registry

---

## Sheet 4: Review_Scope

---

## Sheet 5: Review_Execution

---

## Sheet 6: Findings_Summary

---

## Sheet 7: Evidence_Register

---

## Sheet 8: Approval_SignOff

---

## Sheet 9: Approval_Signoff

**Data Rows:** 24 (rows 4–27) | **Frozen Panes:** A3

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Review_Schedule!A4:A27)-COUNTBLANK(Review_Schedule!B4:B27)` | Total Reviews Scheduled |
| — | `=COUNTIF(Reviewer_Registry!J4:J23,` | Approved Reviewers |

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
