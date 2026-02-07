**ISMS-IMP-A.5.10-11.S3-TG - Asset Return and Offboarding Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.11

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.S3-TG |
| **Title** | Asset Return and Offboarding Assessment |
| **Control Reference** | ISO/IEC 27001:2022 A.5.11 |
| **Control Name** | Return of Assets |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.10-11.S3-UG.

---

# Technical Specification


> Auto-generated from `generate_a510_11_3_asset_return_offboarding.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.10-11.S3` |
| **Output Filename** | `ISMS-IMP-A.5.10-11.S3_Asset_Return_and_Offboarding_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Asset Return and Offboarding Assessment |
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

## Sheet 2: Return_Process

---

## Sheet 3: Asset_Checklist

---

## Sheet 4: Offboarding_Tracking

---

## Sheet 5: Access_Revocation

---

## Sheet 6: Evidence_Register

---

## Sheet 7: Approval_SignOff

---

## Sheet 8: Approval_Signoff

**Data Rows:** 200 (rows 4–203) | **Frozen Panes:** A3

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Return_Process!A4:A31)-COUNTBLANK(Return_Process!B4:B31)` | Process Requirements Assessed |
| — | `=COUNTIF(Return_Process!D4:D31,` | Process Requirements Implemented |
| — | `=COUNTA(Offboarding_Tracking!A4:A103)-COUNTBLANK(Offboarding_Tracking!B4:B103)` | Offboardings Tracked |
| — | `=COUNTIF(Offboarding_Tracking!I4:I103,` | Offboardings Complete |
| — | `=COUNTA(Access_Revocation!A4:A203)-COUNTBLANK(Access_Revocation!B4:B203)` | Access Revocations Verified |

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
