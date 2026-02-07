**ISMS-IMP-A.5.17.3-TG - Authentication Management Procedures**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.17: Authentication Information

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.17.3-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.17 Authentication Information |
| **Parent Policy** | ISMS-POL-A.5.17 - Authentication Information |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.17.3-UG.

---

# Technical Specification


> Auto-generated from `generate_a517_3_password_system_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.17.3` |
| **Output Filename** | `ISMS-IMP-A.5.17.3_Password_System_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Password System Assessment |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

**Frozen Panes:** A3

---

## Sheet 2: System_Inventory

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | System Name |
| B | System Type |
| C | Vendor |
| D | Version |
| E | User Count |
| F | Auth Method |
| G | SSO Integrated |
| H | MFA Enabled |
| I | Owner |
| J | Criticality |

---

## Sheet 3: Security_Assessment

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | System Name |
| B | Control Area |
| C | Requirement |
| D | Expected State |
| E | Actual State |
| F | Status |
| G | Gap Description |
| H | Priority |
| I | Notes |

---

## Sheet 4: Storage_Assessment

**Data Rows:** 8 (rows 1–8) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | System/Application |
| B | Storage Mechanism |
| C | Hashing Algorithm |
| D | Salting |
| E | Key Protection |
| F | Encryption at Rest |
| G | Status |
| H | Notes |

---

## Sheet 5: Integration_Assessment

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Application |
| B | SSO Protocol |
| C | Identity Provider |
| D | MFA Pass-through |
| E | Session Timeout |
| F | Token Encryption |
| G | Provisioning |
| H | Status |
| I | Notes |

---

## Sheet 6: Gap_Analysis

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | System/Area |
| C | Gap Description |
| D | Risk Level |
| E | Remediation Plan |
| F | Owner |
| G | Target Date |
| H | Status |
| I | Notes |

---

## Sheet 7: Evidence_Register

**Data Rows:** 8 (rows 1–8) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Evidence Type |
| C | Description |
| D | Related Assessment |
| E | Location/Link |
| F | Date Collected |
| G | Collected By |
| H | Status |

---

## Sheet 8: Approval_SignOff

**Data Rows:** 4 (rows 2–5) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Role |
| B | Name |
| C | Signature |
| D | Date |
| E | Status |
| F | Comments |

---

## Sheet 9: Header_Row

---

**END OF SPECIFICATION**

---

*"A chain is only as strong as its weakest link."*
— Thomas Reid

<!-- QA_VERIFIED: 2026-02-06 -->
