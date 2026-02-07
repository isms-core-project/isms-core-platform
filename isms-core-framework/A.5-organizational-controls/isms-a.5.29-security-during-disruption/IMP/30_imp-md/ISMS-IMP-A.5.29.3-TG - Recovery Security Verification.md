**ISMS-IMP-A.5.29.3-TG - Recovery Security Verification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.29

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.29.3-TG |
| **Title** | Recovery Security Verification |
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

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.29.3-UG.

---

# Technical Specification


> Auto-generated from `generate_a529_3_recovery_verification.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.29.3` |
| **Output Filename** | `ISMS-IMP-A.5.29.3_Recovery_Security_Verification_YYYYMMDD.xlsx` |
| **Workbook Title** | Recovery Security Verification |
| **Total Sheets** | 10 (10 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #808080 | 808080 | Gray (Disabled) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Recovery_Checklist

---

## Sheet 3: Emergency_Access_Closure

---

## Sheet 4: Control_Validation

---

## Sheet 5: Anomaly_Detection

---

## Sheet 6: Security_Debt_Closure

---

## Sheet 7: Lessons_Learned

---

## Sheet 8: Evidence_Register

---

## Sheet 9: Approval_SignOff

---

## Sheet 10: Approval_Signoff

**Data Rows:** 50 (rows 4–53) | **Frozen Panes:** A3

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIF(Recovery_Checklist!F4:F33,` | Recovery Checklist Items Complete |
| — | `=COUNTIF(Emergency_Access_Closure!M4:M23,` | Emergency Access Accounts Verified |
| — | `=COUNTIF(Control_Validation!E4:E53,` | Controls Validated |
| — | `=COUNTIF(Anomaly_Detection!H4:H53,` | Open Anomalies |
| — | `=COUNTIF(Security_Debt_Closure!L4:L33,` | Security Debt Closed |
| — | `=COUNTIF(Lessons_Learned!J4:J23,` | Lessons Learned Actions Open |

---

**END OF SPECIFICATION**

---

*"Security is not a product, but a process."*
— Bruce Schneier

<!-- QA_VERIFIED: 2026-02-06 -->
