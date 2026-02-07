**ISMS-IMP-A.5.30-8.13-14-S5-TG - BC/DR Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.13: Information Backup

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.30-8.13-14-S5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Overall BC/DR Capability Assessment |
| **Related Policy** | ISMS-POL-A.5.30-8.13-14 (All Sections) |
| **Related Assessments** | IMP-S1 (BIA), IMP-S2 (Backup), IMP-S3 (Redundancy), IMP-S4 (Testing) |
| **Purpose** | Consolidate BC/DR metrics, calculate maturity score, provide executive dashboard |
| **Target Audience** | Executive Management, CISO, BC/DR Coordinator, Internal Auditors, External Auditors |
| **Assessment Type** | Comprehensive Evaluation |
| **Review Cycle** | Quarterly (Dashboard Update) + Annual (Comprehensive Assessment) |
| **Date** | [Date] |

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a530_5_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.30.S5` |
| **Output Filename** | `ISMS-IMP-A.5.30.S5_BC/DR_Consolidated_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | BC/DR Consolidated Dashboard |
| **Total Sheets** | 7 (7 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #808080 | 808080 | Gray (Disabled) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #DDEBF7 | DDEBF7 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Executive_Dashboard

---

## Sheet 3: Detailed_Metrics

---

## Sheet 4: Gap_Summary

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Source Assessment |
| B | Gap/Issue Type |
| C | System/Area |
| D | Priority |
| E | Description |
| F | Status |

---

## Sheet 5: Evidence_Checklist

### Columns

| Col | Header |
|-----|--------|
| A | Control |
| B | Assessment Workbook |
| C | Evidence Count |
| D | Min Required |
| E | Status |

---

## Sheet 6: Approval_Sign_Off

---

## Sheet 7: Base_Validations

---

**END OF SPECIFICATION**

---

*"The only source of knowledge is experience."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
