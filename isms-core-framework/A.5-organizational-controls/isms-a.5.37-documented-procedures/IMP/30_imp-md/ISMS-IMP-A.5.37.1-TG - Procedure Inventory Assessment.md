**ISMS-IMP-A.5.37.1-TG - Procedure Inventory Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.37

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.1-TG |
| **Title** | Procedure Inventory Assessment |
| **Control Reference** | ISO/IEC 27001:2022 A.5.37 |
| **Control Name** | Documented Operating Procedures |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |
| **Framework Version** | 1.0 |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.37.1-UG.

---

# Technical Specification


> Auto-generated from `generate_a537_1_procedure_inventory.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.37.1` |
| **Output Filename** | `ISMS-IMP-A.5.37.1_Procedure_Inventory_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Procedure Inventory Assessment |
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
| #E2EFDA | E2EFDA | Pale Green (Success Background) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Procedure_Inventory

---

## Sheet 3: Required_Procedures

---

## Sheet 4: Accessibility_Matrix

---

## Sheet 5: Gap_Analysis

---

## Sheet 6: Evidence_Register

---

## Sheet 7: Approval_SignOff

---

## Sheet 8: Approval_Signoff

**Data Rows:** 100 (rows 4–103) | **Frozen Panes:** A3

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Procedure_Inventory!A4:A103)-COUNTBLANK(Procedure_Inventory!B4:B103)` | Total Procedures Inventoried |
| — | `=COUNTIF(Procedure_Inventory!K4:K103,\` | Procedures Approved |
| — | `=COUNTIF(Gap_Analysis!H4:H53,\` | Open Gaps |

---

**END OF SPECIFICATION**

---

*"The beginning of wisdom is the definition of terms."*
— Socrates

<!-- QA_VERIFIED: 2026-02-06 -->
