<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.35-36.S2-TG:framework:TG:a.5.35-36 -->
**ISMS-IMP-A.5.35-36.S2-TG - Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.36

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.35-36.S2-TG |
| **Title** | Compliance Assessment |
| **Control Reference** | ISO/IEC 27001:2022 A.5.36 |
| **Control Name** | Compliance with Policies, Rules and Standards |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

# Technical Specification


> Auto-generated from `generate_a535_36_2_compliance_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.35-36.S2` |
| **Output Filename** | `ISMS-IMP-A.5.35-36.S2_Compliance_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance Assessment |
| **Total Sheets** | 8 (8 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #808080 | 808080 | Gray (Disabled) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Workbook

---

## Sheet 2: Instructions

**Frozen Panes:** A4

---

## Sheet 3: Policy_Compliance

**Data Rows:** 11 (rows 1–11) | **Frozen Panes:** C4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Policy_ID | 16 |
| B | Policy_Name | 40 |
| C | Policy_Version | 14 |
| D | Compliance_Status | 18 |
| E | Last_Reviewed | 14 |
| F | Assessed_By | 22 |
| G | Assessment_Date | 14 |
| H | Evidence_Ref | 18 |
| I | NonCompliance_Issues | 30 |
| J | Remediation_Status | 18 |
| K | Notes | 30 |

---

## Sheet 4: Control_Compliance

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** C4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Control_ID | 14 |
| B | Control_Name | 45 |
| C | Control_Category | 22 |
| D | Compliance_Status | 18 |
| E | Implementation_% | 14 |
| F | Last_Assessed | 14 |
| G | Assessed_By | 22 |
| H | Evidence_Ref | 18 |
| I | Gaps_Identified | 30 |
| J | Notes | 30 |

---

## Sheet 5: Department_Assessment

**Data Rows:** 12 (rows 1–12) | **Frozen Panes:** B4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Department | 25 |
| B | Manager | 22 |
| C | Assessment_Period | 16 |
| D | AUP_Compliance | 16 |
| E | Access_Control_Compliance | 20 |
| F | Incident_Reporting_Compliance | 22 |
| G | Training_Compliance | 18 |
| H | Asset_Management_Compliance | 22 |
| I | Overall_Rating | 16 |
| J | Issues_Identified | 30 |
| K | Improvement_Actions | 30 |
| L | Sign_Off_Date | 14 |

---

## Sheet 6: Noncompliance_Register

**Data Rows:** 100 (rows 4–103) | **Frozen Panes:** D4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | NC_ID | 12 |
| B | Identified_Date | 14 |
| C | Policy_Control_Ref | 20 |
| D | Department | 20 |
| E | NC_Description | 45 |
| F | Root_Cause | 30 |
| G | Severity | 14 |
| H | Remediation_Action | 35 |
| I | Owner | 22 |
| J | Target_Date | 14 |
| K | Status | 16 |
| L | Closure_Date | 14 |

---

## Sheet 7: Evidence_Register

**Data Rows:** 100 (rows 4–103) | **Frozen Panes:** C4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence_ID | 15 |
| B | Evidence_Type | 22 |
| C | Description | 45 |
| D | Related_Assessment | 20 |
| E | Collection_Date | 16 |
| F | Location | 40 |
| G | Collected_By | 25 |
| H | Valid_Until | 16 |

---

## Sheet 8: Approval_Signoff

**Data Rows:** 100 (rows 4–103) | **Frozen Panes:** A3

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Policy_Compliance!A4:A36)-COUNTBLANK(Policy_Compliance!B4:B36)` | Policies Assessed |
| — | `=COUNTIF(Policy_Compliance!D4:D36,` | Policies Compliant |
| — | `=COUNTIF(NonCompliance_Register!K4:K103,` | Open Non-Conformances |

---

**END OF SPECIFICATION**

---

*"Compliance is not about checking boxes; it's about doing the right thing."*
— Unknown

<!-- QA_VERIFIED: 2026-02-06 -->
