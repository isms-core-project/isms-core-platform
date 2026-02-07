**ISMS-IMP-A.5.30-8.13-14-S4-TG - Recovery Testing Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.13: Information Backup

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.30-8.13-14-S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Business Continuity & Disaster Recovery Testing |
| **Related Policy** | ISMS-POL-A.5.30-8.13-14, Section 2.4 (Testing Requirements) |
| **Related Assessments** | IMP-S1 (BIA), IMP-S2 (Backup), IMP-S3 (Redundancy) |
| **Purpose** | Define comprehensive testing methodology for backup restoration, failover validation, and full DR scenario exercises |
| **Target Audience** | BC/DR Coordinator, IT Operations, System Administrators, DBAs, Management |
| **Assessment Type** | Operational Testing |
| **Review Cycle** | After Each Test + Annual Methodology Review |
| **Date** | [Date] |

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a530_4_testing_results.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.30.S4` |
| **Output Filename** | `ISMS-IMP-A.5.30.S4_Testing_Results_YYYYMMDD.xlsx` |
| **Workbook Title** | BC/DR Testing Results Tracker |
| **Total Sheets** | 9 (9 visible) |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #808080 | 808080 | Gray (Disabled) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Summary

**Data Rows:** 110 (rows 5–114)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Test_Schedule!A5:A114)` | Total Tests Scheduled: |
| — | `=COUNTIF(Test_Results_Log!F5:F114,` | Tests Completed (✅ Success): |
| — | `=IF(B5>0,(B6+B7*0.5)/B5,0)` | Test Success Rate: |
| — | `=COUNTIF(Testing_Compliance!C5:C114,` | Tier 1 - Critical Systems: |
| — | `=SUMPRODUCT((Testing_Compliance!C5:C114=` | Tier 1 - Compliant: |
| — | `=IF(B15>0,B16/B15,0)` | Tier 1 - Compliance Rate: |
| — | `=IF(B19>0,B20/B19,0)` | Tier 2 - Compliance Rate: |
| — | `=COUNTA(Issue_Remediation!A5:A114)` | Total Issues Identified: |
| — | `=COUNTIF(Issue_Remediation!E5:E114,` | 🔴 Critical Issues: |
| — | `=COUNTIF(Issue_Remediation!F5:F114,` | Open Issues (🔴): |
| — | `=COUNTA(Evidence_Register!A5:A104)` | Evidence Items Collected: |
| — | `=COUNTIF(Evidence_Register!H5:H104,` | Verified Evidence: |
| — | `=IF(B39>=B41,` | Evidence Compliance: |
| — | `=IF(Approval_Sign_Off!B26<>` | Level 1 - Assessor Completed: |
| — | `=IF(Approval_Sign_Off!B37<>` | Level 2 - ISO Review: |
| — | `=IF(Approval_Sign_Off!B49<>` | Level 3 - CISO Approval: |

---

## Sheet 3: Test_Schedule

**Data Rows:** 110 (rows 5–114) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Test ID |
| B | System Name |
| C | Test Type |
| D | Criticality |
| E | Required Frequency |
| F | Scheduled Date |
| G | Test Owner |
| H | Notes / Prerequisites |

---

## Sheet 4: Test_Results_Log

**Data Rows:** 110 (rows 5–114) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Result ID |
| B | Test ID (Schedule) |
| C | System Name |
| D | Test Type |
| E | Test Date |
| F | Result |
| G | Actual Duration (hrs) |
| H | Tested By |
| I | Issues Found |
| J | Detailed Notes |

---

## Sheet 5: Issue_Remediation

**Data Rows:** 110 (rows 5–114) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Issue ID |
| B | Related Test (Result ID) |
| C | Issue Description |
| D | Root Cause |
| E | Severity |
| F | Status |
| G | Remediation Plan |
| H | Target Resolution Date |

---

## Sheet 6: Testing_Compliance

**Data Rows:** 110 (rows 5–114) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | System Name |
| B | Test Type |
| C | Criticality |
| D | Required Frequency |
| E | Last Test Date |
| F | Days Since Last Test |
| G | Compliance Status |
| H | Next Test Due |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| FN | `=IF(E{current_row}=` |  |

---

## Sheet 7: Evidence_Register

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Evidence Type |
| C | Description |
| D | Related Sheet/Row |
| E | Location/Path |
| F | Date Collected |
| G | Collected By |
| H | Verification Status |

---

## Sheet 8: Approval_Sign_Off

**Data Rows:** 100 (rows 5–104)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Evidence_Register!A5:A104)` | Evidence Items Collected: |

---

## Sheet 9: Base_Validations

---

**END OF SPECIFICATION**

---

*"Strive not to be a success, but rather to be of value."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
