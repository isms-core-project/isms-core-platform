**ISMS-IMP-A.5.29.1-TG - Security Controls During Disruption Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.29

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.29.1-TG |
| **Title** | Security Controls During Disruption Assessment |
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

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.29.1-UG.

---

# Technical Specification


> Auto-generated from `generate_a529_1_security_controls_disruption.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.29.1` |
| **Output Filename** | `ISMS-IMP-A.5.29.1_Security_Controls_During_Disruption_YYYYMMDD.xlsx` |
| **Workbook Title** | Security Controls During Disruption |
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
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Security_Control_Inventory

---

## Sheet 3: Minimum_Baseline

---

## Sheet 4: Security_Posture_Levels

---

## Sheet 5: Compensating_Controls

---

## Sheet 6: BCDR_Security_Review

---

## Sheet 7: Evidence_Register

---

## Sheet 8: Approval_SignOff

---

## Sheet 9: Bcdr_Security_Review

**Data Rows:** 30 (rows 4–33) | **Frozen Panes:** C4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Plan_ID | 15 |
| B | Plan_Name | 35 |
| C | Plan_Type | 20 |
| D | Plan_Owner | 25 |
| E | Security_Section_Present | 18 |
| F | CISO_Review_Date | 16 |
| G | CISO_Approval_Status | 18 |
| H | Gaps_Identified | 40 |
| I | Remediation_Due_Date | 18 |
| J | Remediation_Status | 18 |
| K | Next_Review_Due | 16 |

---

## Sheet 10: Approval_Signoff

**Data Rows:** 100 (rows 4–103) | **Frozen Panes:** A3

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Security_Control_Inventory!A4:A103)-COUNTBLANK(Security_Control_Inventor` | Total Security Controls |
| — | `=COUNTIF(Security_Control_Inventory!F4:F103,` | Non-Negotiable Controls |
| — | `=COUNTIF(BCDR_Security_Review!G4:G33,` | BC/DR Plans Reviewed |
| — | `=COUNTIF(Compensating_Controls!I4:I33,` | Compensating Controls Tested |
| — | `=COUNTIF(BCDR_Security_Review!J4:J33,` | Open Remediation Items |

---

**END OF SPECIFICATION**

---

*"Plans are worthless, but planning is everything."*
— Dwight D. Eisenhower

<!-- QA_VERIFIED: 2026-02-06 -->
