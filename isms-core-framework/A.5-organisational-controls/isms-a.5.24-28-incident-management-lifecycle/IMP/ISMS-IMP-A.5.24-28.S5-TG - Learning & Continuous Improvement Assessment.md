<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.24-28.S5-TG:framework:TG:a.5.24-28 -->
**ISMS-IMP-A.5.24-28.S5-TG - Learning & Continuous Improvement Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.27

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Learning & Continuous Improvement Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S5-TG |
| **Assessment Domain** | Domain 5 - Learning & Improvement (A.5.27 Focus) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Incident Response Team Lead / CSIRT Manager |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CSIRT Manager | Initial learning & improvement assessment specification |

**Review Cycle:** Annual (or after major incident management process changes)
**Next Review Date:** [Effective Date + 12 months]

**Related Documents:**
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide)
- ISMS-IMP-A.5.24-28.S1 (Framework & Governance Assessment)
- ISMS-IMP-A.5.24-28.S2 (Detection & Classification Assessment)
- ISMS-IMP-A.5.24-28.S3 (Response Capabilities Assessment)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment)
- ISO/IEC 27002:2022 Control A.5.27
- NIST SP 800-61 Rev. 2 Section 3.4 (Post-Incident Activity)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a524_28_s5_learning_improvement.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.24-28.S5` |
| **Output Filename** | `ISMS-IMP-A.5.24-28.S5_Learning_Improvement_YYYYMMDD.xlsx` |
| **Workbook Title** | Learning & Continuous Improvement |
| **Total Sheets** | 20 (20 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9E2F3 | D9E2F3 | Custom |
| #E2EFDA | E2EFDA | Pale Green (Success Background) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFF99 | FFFF99 | Custom |

## Sheet 1: Instructions & Legend

---

## Sheet 2: PIR Process

---

## Sheet 3: Root Cause Analysis

---

## Sheet 4: Lessons Learned

---

## Sheet 5: Control Improvements

---

## Sheet 6: Trend Analysis

---

## Sheet 7: Gap Analysis

---

## Sheet 8: Evidence Register

---

## Sheet 9: Summary Dashboard

---

## Sheet 10: Approval Sign-Off

---

## Sheet 11: Instructions

---

## Sheet 12: Pir_Process

**Data Rows:** 50 (rows 6–55)

### Columns

| Col | Header |
|-----|--------|
| A | Incident_ID |
| B | Incident_Date |
| C | Severity |
| D | Resolution_Date |
| E | PIR_Status |
| F | PIR_Completion_Date |
| G | SLA_Days |
| H | Actual_Days |
| I | SLA_Met |
| J | Participants_Met |
| K | Quality_Score |
| L | Evidence_Ref |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(A6:A55)` | Total incidents in period |
| — | `=COUNTIF(E6:E55,` | PIRs completed |
| — | `=IF(B` | SLA compliance rate (%) |

---

## Sheet 13: Rca

**Data Rows:** 30 (rows 6–35)

### Columns

| Col | Header |
|-----|--------|
| A | Incident_ID |
| B | Severity |
| C | RCA_Status |
| D | RCA_Date |
| E | Methodology |
| F | Root_Cause_Summary |
| G | Depth_Score |
| H | Recurring |
| I | Evidence_Ref |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(A6:A35)` | Critical/High incidents in period |
| — | `=COUNTIF(C6:C35,` | RCAs completed |
| — | `=COUNTIF(G6:G35,` | Systemic depth RCAs |
| — | `=COUNTIF(H6:H35,` | Recurring root causes |

---

## Sheet 14: Lessons_Learned

**Data Rows:** 50 (rows 6–55)

### Columns

| Col | Header |
|-----|--------|
| A | PIR_ID |
| B | LL_Entry_Date |
| C | Lesson_Summary |
| D | Distribution_Date |
| E | SLA_Met |
| F | Playbook_Update |
| G | Playbook_Date |
| H | Evidence_Ref |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(A6:A55)` | Total lessons learned entries |
| — | `=IF(COUNTA(A6:A55)>0,COUNTIF(E6:E55,` | Distribution SLA met (%) |
| — | `=COUNTIF(F6:F55,` | Playbook updates completed |
| — | `=COUNTIF(E60:E74,` | KB items current |
| — | `=COUNTIFS(E60:E74,` | KB items outdated/missing |

---

## Sheet 15: Control_Improvements

**Data Rows:** 70 (rows 6–75)

### Columns

| Col | Header |
|-----|--------|
| A | Action_ID |
| B | Source_Incident |
| C | Action_Description |
| D | Priority |
| E | Owner |
| F | Target_Date |
| G | Status |
| H | Completion_Date |
| I | Verified_By |
| J | Escalated |
| K | Evidence_Ref |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(A6:A75)` | Total actions |
| — | `=COUNTIF(G6:G75,` | Actions completed |
| — | `=IF(COUNTA(A6:A75)>0,COUNTIF(G6:G75,` | Closure rate (%) |
| — | `=COUNTIFS(D6:D75,` | Critical actions open |
| — | `=COUNTIFS(F6:F75,` | Overdue actions |

---

## Sheet 16: Trend_Analysis

**Data Rows:** 8 (rows 6–13)

---

## Sheet 17: Gap_Analysis

**Data Rows:** 30 (rows 6–35)

### Columns

| Col | Header |
|-----|--------|
| A | Gap_ID |
| B | Source_Sheet |
| C | Gap_Description |
| D | Severity |
| E | Owner |
| F | Target_Date |
| G | Remediation_Plan |
| H | Status |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=COUNTA(A6:A35)` |  |
| DN | `=COUNTIF(D6:D35,` |  |

---

## Sheet 18: Evidence_Register

**Data Rows:** 50 (rows 6–55)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_ID |
| B | Related_Sheet |
| C | Evidence_Type |
| D | Description |
| E | File_Location |
| F | Collection_Date |
| G | Collected_By |

---

## Sheet 19: Summary_Dashboard

**Data Rows:** 5 (rows 10–14)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| B6 | `=AVERAGE(B10:B14)` |  |

---

## Sheet 20: Approval_Signoff

---

**END OF SPECIFICATION**

---

*"The idea is to try to give all the information to help others to judge the value of your contribution."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
