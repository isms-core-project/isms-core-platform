**ISMS-IMP-A.5.24-28.S1-TG - Incident Management Framework Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.24: Information Security Incident Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Incident Management Framework Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S1-TG |
| **Assessment Domain** | Domain 1 - Framework & Governance (A.5.24 Focus) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Incident Response Team Lead / CSIRT Manager |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CSIRT Manager | Initial framework assessment specification |

**Review Cycle**: Annual (or after major incident management changes)  
**Next Review Date**: [Effective Date + 12 months]  

**Related Documents**: 

- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide)
- ISMS-IMP-A.5.24-28.S2 (Detection & Classification Assessment)
- ISMS-IMP-A.5.24-28.S3 (Response Capabilities Assessment)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment)
- ISMS-IMP-A.5.24-28.S5 (Learning & Improvement Assessment)
- ISO/IEC 27002:2022 Control A.5.24
- NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide)

---

# Technical Specification


> Auto-generated from `generate_a524_28_s1_framework_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.24-28.S1` |
| **Output Filename** | `ISMS-IMP-A.5.24-28.S1_Incident_Management_Framework_YYYYMMDD.xlsx` |
| **Workbook Title** | Incident Management Framework |
| **Total Sheets** | 19 (19 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D8E4F8 | D8E4F8 | Pale Blue (Sub-section) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFD9B3 | FFD9B3 | Custom |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: Governance Assessment

---

## Sheet 3: Organizational Structure

---

## Sheet 4: Training & Competency

---

## Sheet 5: Tools & Technology

---

## Sheet 6: Integration Assessment

---

## Sheet 7: Gap Analysis

---

## Sheet 8: Evidence Register

---

## Sheet 9: Dashboard

---

## Sheet 10: Approval Sign-Off

---

## Sheet 11: Instructions

**Frozen Panes:** A3

---

## Sheet 12: Governance_Assessment

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

## Sheet 13: Organizational_Structure

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

## Sheet 14: Training_Competency

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

## Sheet 15: Tools_Technology

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

## Sheet 16: Integration_Assessment

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

## Sheet 17: Gap_Analysis

**Data Rows:** 60 (rows 5–64) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Gap_ID |
| B | Assessment_Section |
| C | Gap_Description |
| D | Risk_Level |
| E | Current_State |
| F | Target_State |
| G | Remediation_Action |
| H | Owner |
| I | Target_Date |
| J | Status |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=COUNTA(A5:A64)` |  |
| BN | `=COUNTIF(D5:D64, ` |  |
| BN | `=COUNTIF(J5:J64, ` |  |

---

## Sheet 18: Evidence_Register

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
| H | Verification_Status |

---

## Sheet 19: Approval_Signoff

**Frozen Panes:** A3

---

**END OF SPECIFICATION**

---

*"I beg to introduce myself to you as a clerk in the Accounts Department... I have no university education... but I have been employing my spare time in mathematics."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
