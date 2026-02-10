<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.30-8.13-14-S3-TG:framework:TG:a.5.30-8.13-14-s3 -->
**ISMS-IMP-A.5.30-8.13-14-S3-TG - Redundancy Implementation**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.13: Information Backup

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.30-8.13-14-S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Redundancy & High Availability Implementation |
| **Related Policy** | ISMS-POL-A.5.30-8.13-14, Section 2.2 (Redundancy Requirements) |
| **Related Assessment** | ISMS-IMP-A.5.30-8.13-14-S1 (BIA - provides RTO requirements) |
| **Purpose** | Implement redundancy and high availability aligned with BIA-determined RTO requirements, eliminate single points of failure, configure failover capabilities |
| **Target Audience** | Infrastructure Team, Network Team, Database Administrators, Cloud Architects, System Administrators, BC/DR Coordinator |
| **Assessment Type** | Technical Implementation |
| **Review Cycle** | Quarterly (redundancy configuration) + After Major System Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial redundancy implementation methodology | ISMS Implementation Team |


---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a530_3_rpo_rto_compliance.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.30.S3` |
| **Output Filename** | `ISMS-IMP-A.5.30.S3_RPO_RTO_Compliance_YYYYMMDD.xlsx` |
| **Workbook Title** | RPO/RTO Compliance Matrix |
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
| — | `=COUNTA(System_Inventory!A5:A114)` | Total Systems Assessed: |
| — | `=COUNTIF(Compliance_Matrix!E5:E114,` | Systems with Full Compliance (RPO & RTO): |
| — | `=IF(B5>0,B6/B5,0)` | Overall Compliance Rate: |
| — | `=COUNTIF(System_Inventory!C5:C114,` | Tier 1 - Critical Systems: |
| — | `=SUMPRODUCT((System_Inventory!C5:C114=` | Tier 1 - Full Compliance: |
| — | `=IF(B13>0,B14/B13,0)` | Tier 1 - Compliance Rate: |
| — | `=IF(B17>0,B18/B17,0)` | Tier 2 - Compliance Rate: |
| — | `=COUNTA(Gap_Analysis!A5:A114)` | Total Gaps Identified: |
| — | `=COUNTIF(Gap_Analysis!F5:F114,` | 🔴 Critical Priority Gaps: |
| — | `=COUNTIF(Gap_Analysis!H5:H114,` | Open Gaps (🔴): |
| — | `=IFERROR(AVERAGE(Gap_Analysis!E5:E114),0)` | Average Risk Score: |
| — | `=COUNTA(Evidence_Register!A5:A104)` | Evidence Items Collected: |
| — | `=COUNTIF(Evidence_Register!H5:H104,` | Verified Evidence: |
| — | `=IF(B40>=B42,` | Evidence Compliance: |
| — | `=IF(Approval_Sign_Off!B27<>` | Level 1 - Assessor Completed: |
| — | `=IF(Approval_Sign_Off!B38<>` | Level 2 - ISO Review: |
| — | `=IF(Approval_Sign_Off!B50<>` | Level 3 - CISO Approval: |

---

## Sheet 3: System_Inventory

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | System Name |
| B | Business Process |
| C | Criticality Tier |
| D | MTPD (hours) |
| E | RPO Requirement (hours) |
| F | RTO Requirement (hours) |
| G | Business Justification |

---

## Sheet 4: Capability_Assessment

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | System Name |
| B | Backup Frequency (hours) |
| C | Restore Time Tested (hours) |
| D | Failover Time Tested (hours) |
| E | RPO Capability (hours) |
| F | RTO Capability (hours) |
| G | Test Notes / Observations |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IF(ISNUMBER(B{current_row}),B{current_row},` |  |
| FN | `=IF(AND(ISNUMBER(C{current_row}),ISNUMBER(D{current_row})),MIN(C{current_row},D{` |  |

---

## Sheet 5: Compliance_Matrix

**Data Rows:** 110 (rows 5–114) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | System Name |
| B | Criticality |
| C | RPO: Req vs Cap |
| D | RTO: Req vs Cap |
| E | Overall Compliance |
| F | Priority |
| G | Gap Summary |
| H | Next Action Required |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=System_Inventory!A{current_row}` |  |
| BN | `=System_Inventory!C{current_row}` |  |

---

## Sheet 6: Gap_Analysis

**Data Rows:** 110 (rows 5–114) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | System |
| C | Gap Type |
| D | Gap Description |
| E | Risk Score (1-10) |
| F | Priority |
| G | Remediation Plan |
| H | Status |

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

*"We cannot solve our problems with the same thinking we used when we created them."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
