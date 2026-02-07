**ISMS-IMP-A.5.10-11.S1-TG - Acceptable Use Policy Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.10: Acceptable Use of Information and Other Associated Assets

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.S1-TG |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.10: Acceptable Use of Information and Other Associated Assets |
| **Parent Policy** | ISMS-POL-A.5.10-11 Asset Usage Lifecycle Policy |
| **Related IMPs** | ISMS-IMP-A.5.10-11.S2, ISMS-IMP-A.5.10-11.S3, ISMS-IMP-A.5.10-11.S4 |
| **Version** | 1.0 |
| **Classification** | Internal Use |
| **Owner** | Information Security Manager |
| **Last Review** | [Date to be set] |
| **Framework Version** | 1.0 |
| **Assessment Type** | Policy Completeness and Effectiveness Assessment |

---

## Control Requirement

> "Rules for the acceptable use of information and other associated assets should be identified, documented and implemented."
>
> — ISO/IEC 27001:2022, Annex A Control 5.10

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.10-11.S1-UG.

---

# Technical Specification


> Auto-generated from `generate_a510_11_1_acceptable_use_policy.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.10-11.S1` |
| **Output Filename** | `ISMS-IMP-A.5.10-11.S1_Acceptable_Use_Policy_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Acceptable Use Policy Assessment |
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

## Sheet 2: Policy_Assessment

---

## Sheet 3: Asset_Coverage

---

## Sheet 4: Awareness_Tracking

---

## Sheet 5: Communication_Matrix

---

## Sheet 6: Evidence_Register

---

## Sheet 7: Approval_SignOff

---

## Sheet 8: Approval_Signoff

**Data Rows:** 30 (rows 4–33) | **Frozen Panes:** A3

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Policy_Assessment!A4:A33)-COUNTBLANK(Policy_Assessment!B4:B33)` | Total Policy Requirements Assessed |
| — | `=COUNTIF(Policy_Assessment!D4:D33,` | Requirements Addressed |

---

**END OF SPECIFICATION**

---

*"Security is not a product, but a process."*
— Bruce Schneier

<!-- QA_VERIFIED: 2026-02-06 -->
