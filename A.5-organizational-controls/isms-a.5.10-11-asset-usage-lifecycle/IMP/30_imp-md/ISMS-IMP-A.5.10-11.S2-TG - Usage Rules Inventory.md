**ISMS-IMP-A.5.10-11.S2-TG - Usage Rules Inventory**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.10: Acceptable Use of Information and Other Associated Assets

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.S2-TG |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.10: Acceptable Use of Information and Other Associated Assets |
| **Parent Policy** | ISMS-POL-A.5.10-11 Asset Usage Lifecycle Policy |
| **Related IMPs** | ISMS-IMP-A.5.10-11.S1, ISMS-IMP-A.5.10-11.S3, ISMS-IMP-A.5.10-11.S4 |
| **Version** | 1.0 |
| **Classification** | Internal Use |
| **Owner** | Information Security Manager |
| **Last Review** | [Date to be set] |
| **Framework Version** | 1.0 |
| **Assessment Type** | Usage Rules Documentation and Inventory |

---

## Control Requirement

> "Rules for the acceptable use of information and other associated assets should be identified, documented and implemented."
>
> — ISO/IEC 27001:2022, Annex A Control 5.10

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.10-11.S2-UG.

---

# Technical Specification


> Auto-generated from `generate_a510_11_2_usage_rules_inventory.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.10-11.S2` |
| **Output Filename** | `ISMS-IMP-A.5.10-11.S2_Usage_Rules_Inventory_YYYYMMDD.xlsx` |
| **Workbook Title** | Usage Rules Inventory |
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

## Sheet 1: Instructions

---

## Sheet 2: Usage_Rules

---

## Sheet 3: Permitted_Activities

---

## Sheet 4: Prohibited_Activities

---

## Sheet 5: Handling_Requirements

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
| — | `=COUNTA(Usage_Rules!A4:A68)-COUNTBLANK(Usage_Rules!B4:B68)` | Total Usage Rules Documented |
| — | `=COUNTA(Permitted_Activities!A4:A103)-COUNTBLANK(Permitted_Activities!B4:B103)` | Permitted Activities Documented |
| — | `=COUNTA(Prohibited_Activities!A4:A61)-COUNTBLANK(Prohibited_Activities!B4:B61)` | Prohibited Activities Documented |
| — | `=COUNTA(Handling_Requirements!A4:A53)-COUNTBLANK(Handling_Requirements!B4:B53)` | Handling Requirements Defined |

---

**END OF SPECIFICATION**

---

*"The best security policy is the one that people actually follow."*
— Unknown

<!-- QA_VERIFIED: 2026-02-06 -->
