<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.10-11.S4-TG:framework:TG:a.5.10-11 -->
**ISMS-IMP-A.5.10-11.S4-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.10-11

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.S4-TG |
| **Title** | Asset Usage Lifecycle Compliance Dashboard |
| **Control Reference** | ISO/IEC 27001:2022 A.5.10-11 |
| **Control Name** | Asset Usage Lifecycle |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.10-11.S4-UG.

---

# Technical Specification


> Auto-generated from `generate_a510_11_4_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.10-11.S4` |
| **Output Filename** | `ISMS-IMP-A.5.10-11.S4_Asset_Usage_Lifecycle_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Asset Usage Lifecycle Compliance Dashboard |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
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

## Sheet 2: Executive_Summary

---

## Sheet 3: A510_Compliance

---

## Sheet 4: A511_Compliance

---

## Sheet 5: Gap_Register

---

## Sheet 6: Remediation_Tracker

---

## Sheet 7: Trend_Analysis

---

## Sheet 8: Approval_SignOff

---

## Sheet 9: Approval_Signoff

**Data Rows:** 50 (rows 4–53) | **Frozen Panes:** A3

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIF(Gap_Register!J4:J53,\` | Total Open Gaps |
| — | `=COUNTIF(Remediation_Tracker!I4:I53,` | Remediations In Progress |

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
