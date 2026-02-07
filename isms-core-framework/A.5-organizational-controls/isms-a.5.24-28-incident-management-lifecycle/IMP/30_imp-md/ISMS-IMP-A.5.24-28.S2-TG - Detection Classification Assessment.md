**ISMS-IMP-A.5.24-28.S2-TG - Incident Detection & Classification Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.24: Information Security Incident Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Incident Detection & Classification Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S2-TG |
| **Assessment Domain** | Domain 2 - Detection & Classification (A.5.25 Focus) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | SOC Manager / Detection Engineering Lead |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | SOC Manager | Initial detection & classification assessment specification |

**Review Cycle**: Annual (or after major detection capability changes)  
**Next Review Date**: [Effective Date + 12 months]  

**Related Documents**: 

- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide, Section 1: Incident Classification Taxonomy)
- ISMS-IMP-A.5.24-28.S1 (Framework & Governance Assessment)
- ISMS-IMP-A.5.24-28.S3 (Response Capabilities Assessment)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment)
- ISMS-IMP-A.5.24-28.S5 (Learning & Improvement Assessment)
- ISMS-IMP-A.8.16 (Security Monitoring Assessment)
- ISO/IEC 27002:2022 Control A.5.25
- NIST SP 800-61 Rev. 2 Section 3.2 (Detection and Analysis)

---

# Technical Specification


> Auto-generated from `generate_a524_28_s2_detection_classification.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.24-28.S2` |
| **Output Filename** | `ISMS-IMP-A.5.24-28.S2_Detection_&_Classification_YYYYMMDD.xlsx` |
| **Workbook Title** | Detection & Classification |
| **Total Sheets** | 17 (17 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D8E4F8 | D8E4F8 | Pale Blue (Sub-section) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFD9B3 | FFD9B3 | Custom |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: Detection Mechanisms

---

## Sheet 3: Alert Handling

---

## Sheet 4: Classification & Severity

---

## Sheet 5: Detection Effectiveness

---

## Sheet 6: Gap Analysis

---

## Sheet 7: Evidence Register

---

## Sheet 8: Dashboard

---

## Sheet 9: Approval Sign-Off

---

## Sheet 10: Instructions

**Frozen Panes:** A3

---

## Sheet 11: Detection_Mechanisms

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Question_ID |
| B | Section |
| C | Question |
| D | Answer |
| E | Evidence_Reference |
| F | Comments |
| G | Gap_Identified |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| GN | `=IF(OR(D{row}=` |  |

---

## Sheet 12: Alert_Handling

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Question_ID |
| B | Section |
| C | Question |
| D | Answer |
| E | Evidence_Reference |
| F | Comments |
| G | Gap_Identified |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| GN | `=IF(OR(D{row}=` |  |

---

## Sheet 13: Classification_Severity

**Data Rows:** 8 (rows 76–83) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Question_ID |
| B | Section |
| C | Question |
| D | Answer |
| E | Evidence_Reference |
| F | Comments |
| G | Gap_Identified |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| GN | `=IF(OR(D{row}=` |  |

---

## Sheet 14: Detection_Effectiveness

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Question_ID |
| B | Section |
| C | Question |
| D | Answer |
| E | Evidence_Reference |
| F | Comments |
| G | Gap_Identified |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| GN | `=IF(OR(D{row}=` |  |

---

## Sheet 15: Gap_Analysis

**Data Rows:** 9 (rows 2–10) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Gap_ID |
| B | Section |
| C | Gap_Description |
| D | Risk_Level |
| E | Current_State |
| F | Target_State |
| G | Remediation |
| H | Owner |
| I | Target_Date |
| J | Status |

---

## Sheet 16: Evidence_Register

**Data Rows:** 7 (rows 2–8) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_ID |
| B | Evidence_Type |
| C | Description |
| D | Related_Section |
| E | Storage_Location |
| F | Date_Collected |
| G | Collected_By |
| H | Verification |

---

## Sheet 17: Approval_Signoff

**Frozen Panes:** A3

---

**END OF SPECIFICATION**

---

*"The first principle is that you must not fool yourself — and you are the easiest person to fool."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
