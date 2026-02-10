<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.29.2-TG:framework:TG:a.5.29.2 -->
**ISMS-IMP-A.5.29.2-TG - Degraded Mode Security Requirements**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.29

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.29.2-TG |
| **Title** | Degraded Mode Security Requirements |
| **Control Reference** | ISO/IEC 27001:2022 A.5.29 |
| **Control Name** | Information Security During Disruption |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Chief Information Security Officer (CISO) |
| **Classification** | Internal |
| **Framework Version** | 1.0 |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.29.2-UG.

---

# Technical Specification


> Auto-generated from `generate_a529_2_degraded_mode.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.29.2` |
| **Output Filename** | `ISMS-IMP-A.5.29.2_Degraded_Mode_Security_Requirements_YYYYMMDD.xlsx` |
| **Workbook Title** | Degraded Mode Security Requirements |
| **Total Sheets** | 12 (12 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #808080 | 808080 | Gray (Disabled) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E2EFDA | E2EFDA | Pale Green (Success Background) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Degradation_Scenarios

---

## Sheet 3: BreakGlass_Accounts

---

## Sheet 4: BreakGlass_Activation

---

## Sheet 5: Elevated_Monitoring

---

## Sheet 6: Personnel_Availability

---

## Sheet 7: Security_Debt_Register

---

## Sheet 8: Evidence_Register

---

## Sheet 9: Approval_SignOff

---

## Sheet 10: Breakglass_Accounts

**Data Rows:** 20 (rows 4–23) | **Frozen Panes:** C4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Account_ID | 15 |
| B | Account_Name | 25 |
| C | Account_Type | 20 |
| D | Target_Systems | 35 |
| E | Scope_Permissions | 35 |
| F | Credential_Location | 30 |
| G | Activation_Authority | 25 |
| H | Two_Person_Required | 15 |
| I | Default_Duration | 15 |
| J | Logging_Enabled | 15 |
| K | Last_Rotation_Date | 16 |
| L | Last_Test_Date | 16 |
| M | Status | 12 |

---

## Sheet 11: Breakglass_Activation

**Data Rows:** 50 (rows 4–53) | **Frozen Panes:** C4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Activation_ID | 15 |
| B | Account_ID | 15 |
| C | Emergency_Type | 25 |
| D | Activation_DateTime | 20 |
| E | Authorised_By | 25 |
| F | Activated_By | 25 |
| G | Second_Person | 25 |
| H | CISO_Notified | 12 |
| I | Expiry_DateTime | 20 |
| J | Renewed | 10 |
| K | Deactivation_DateTime | 20 |
| L | Post_Review_Completed | 15 |
| M | Issues_Found | 40 |

---

## Sheet 12: Approval_Signoff

**Data Rows:** 50 (rows 4–53) | **Frozen Panes:** A3

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(BreakGlass_Accounts!A4:A23)-COUNTBLANK(BreakGlass_Accounts!B4:B23)` | Total Break-Glass Accounts |
| — | `=COUNTIF(BreakGlass_Accounts!L4:L23,` | Accounts Tested This Year |
| — | `=COUNTIF(Security_Debt_Register!I4:I53,` | Open Security Debt Items |
| — | `=COUNTIF(Security_Debt_Register!K4:K53,` | Overdue Security Debt (>30 days) |

---

**END OF SPECIFICATION**

---

*"In preparing for battle I have always found that plans are useless, but planning is indispensable."*
— Dwight D. Eisenhower

<!-- QA_VERIFIED: 2026-02-06 -->
