**ISMS-IMP-A.5.14.2-TG - Channel Security Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.14

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.14.2-TG |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.14 (Information Transfer) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.14 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.14 (Information Transfer Policy)
- ISMS-IMP-A.5.14.1 (Transfer Rules and Procedures)
- ISMS-IMP-A.5.14.4 (Compliance Monitoring Dashboard)
- ISMS-POL-A.8.24 (Use of Cryptography)
- ISMS-POL-A.8.12 (Data Leakage Prevention)

---

# Technical Specification


> Auto-generated from `generate_a514_2_channel_security_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.14.2` |
| **Output Filename** | `ISMS-IMP-A.5.14.2_Channel_Security_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Channel Security Assessment |
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

## Sheet 2: Email_Assessment

**Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Control Area |
| B | Security Requirement |
| C | Expected Configuration |
| D | Actual Configuration |
| E | Status |
| F | Evidence |
| G | Gap Description |
| H | Remediation |
| I | Priority |

---

## Sheet 3: Cloud_Services

**Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Service |
| B | Control Area |
| C | Requirement |
| D | Configuration |
| E | Status |
| F | Evidence |
| G | Gap |
| H | Remediation |
| I | Priority |

---

## Sheet 4: File_Transfer

**Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | System Type |
| B | Control |
| C | Requirement |
| D | Current State |
| E | Status |
| F | Evidence |
| G | Gap |
| H | Remediation |
| I | Priority |

---

## Sheet 5: Physical_Channels

**Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Channel |
| B | Control Area |
| C | Requirement |
| D | Current Practice |
| E | Status |
| F | Evidence |
| G | Gap |
| H | Remediation |
| I | Priority |

---

## Sheet 6: Risk_Assessment

**Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Channel |
| B | Threat Scenario |
| C | Likelihood |
| D | Impact |
| E | Inherent Risk |
| F | Current Controls |
| G | Control Effectiveness |
| H | Residual Risk |
| I | Treatment |
| J | Owner |

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

**Data Rows:** 5 (rows 2–6) | **Frozen Panes:** A4

---

## Sheet 9: Header_Row

---

**END OF SPECIFICATION**

---

*"Security is always excessive until it's not enough."*
— Robbie Sinclair

<!-- QA_VERIFIED: 2026-02-06 -->
