**ISMS-IMP-A.6.6.2-TG - NDA Execution and Tracking**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.6

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.6.2-TG |
| **Title** | NDA Execution and Tracking |
| **Control Reference** | ISO/IEC 27001:2022 A.6.6 |
| **Control Name** | Confidentiality or Non-Disclosure Agreements |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |
| **Framework Version** | 1.0 |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.6.6.2-UG.

---

# Technical Specification


> Auto-generated from `generate_a66_2_nda_execution_tracking.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.6.6.2` |
| **Output Filename** | `ISMS-IMP-A.6.6.2_NDA_Execution_and_Tracking_YYYYMMDD.xlsx` |
| **Workbook Title** | NDA Execution and Tracking |
| **Total Sheets** | 8 (8 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Workbook

---

## Sheet 2: Instructions

---

## Sheet 3: Active_Ndas

**Data Rows:** 198 (rows 3–200) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | NDA_ID | 14 |
| B | Template_Ref | 14 |
| C | NDA_Title | 35 |
| D | Counterparty | 30 |
| E | Counterparty_Type | 18 |
| F | Execution_Date | 14 |
| G | Effective_Date | 14 |
| H | Expiration_Date | 14 |
| I | Post_Term_Period | 16 |
| J | Post_Term_Expiry | 16 |
| K | Signatories_Count | 14 |
| L | Storage_Location | 30 |
| M | Status | 14 |
| N | Notes | 30 |

---

## Sheet 4: Signatory_Register

**Data Rows:** 498 (rows 3–500) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Signatory_ID | 14 |
| B | NDA_Ref | 14 |
| C | Signatory_Name | 25 |
| D | Signatory_Type | 18 |
| E | Organisation | 25 |
| F | Role_Title | 25 |
| G | Email | 30 |
| H | Signature_Date | 14 |
| I | Signature_Method | 16 |
| J | Termination_Date | 14 |
| K | Status | 14 |
| L | Notes | 30 |

---

## Sheet 5: Expiration_Monitor

**Data Rows:** 98 (rows 3–100) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | NDA_ID | 14 |
| B | Counterparty | 30 |
| C | Expiration_Date | 14 |
| D | Days_Until_Expiry | 16 |
| E | Alert_Status | 14 |
| F | Renewal_Required | 14 |
| G | Renewal_Owner | 20 |
| H | Renewal_Started | 14 |
| I | Action_Required | 30 |
| J | Notes | 30 |

---

## Sheet 6: Renewal_Tracking

**Data Rows:** 98 (rows 3–100) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Renewal_ID | 14 |
| B | Original_NDA | 14 |
| C | Counterparty | 25 |
| D | Original_Expiry | 14 |
| E | Renewal_Initiated | 14 |
| F | New_Terms_Required | 16 |
| G | Legal_Review | 14 |
| H | Counterparty_Agreed | 16 |
| I | New_NDA_ID | 14 |
| J | New_Expiry | 14 |
| K | Status | 14 |
| L | Notes | 30 |

---

## Sheet 7: Evidence_Register

**Data Rows:** 98 (rows 3–100) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence_ID | 14 |
| B | NDA_Ref | 14 |
| C | Evidence_Type | 22 |
| D | Description | 40 |
| E | Storage_Location | 35 |
| F | Collected_Date | 14 |
| G | Collected_By | 20 |
| H | Retention_Until | 14 |

---

## Sheet 8: Approval

**Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Approval_Type | 25 |
| B | Approver_Role | 25 |
| C | Approver_Name | 25 |
| D | Signature | 20 |
| E | Date | 14 |
| F | Comments | 35 |

---

**END OF SPECIFICATION**

---

*"A verbal contract isn't worth the paper it's written on."*
— Samuel Goldwyn

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-02-06 -->
