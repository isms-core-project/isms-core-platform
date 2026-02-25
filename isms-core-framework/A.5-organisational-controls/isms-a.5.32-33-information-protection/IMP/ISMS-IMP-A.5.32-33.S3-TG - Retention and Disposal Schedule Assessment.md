<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.32-33.S3-TG:framework:TG:a.5.32-33 -->
**ISMS-IMP-A.5.32-33.S3-TG - Retention and Disposal Schedule Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.33: Protection of Records

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.32-33.S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Records Retention Requirements, Disposal Schedule, Secure Destruction Verification |
| **Related Policy** | ISMS-POL-A.5.32-33, Section 2.2 (Retention Requirements, Records Disposal) |
| **Purpose** | Guide users through defining retention periods, managing disposal schedules, and verifying secure destruction |
| **Target Audience** | Records Manager, Legal Counsel, CISO, IT Operations, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Annual or After Regulatory Changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Retention and Disposal assessment workbook | ISMS Implementation Team |

---


---
# Technical Specification
**Audience:** Workbook Developers, Python/Excel Script Maintainers


> Auto-generated from `generate_a532_33_3_retention_disposal.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.32-33.S3` |
| **Output Filename** | `ISMS-IMP-A.5.32-33.S3_Retention_Disposal_Schedule_YYYYMMDD.xlsx` |
| **Workbook Title** | Retention Disposal Schedule |
| **Total Sheets** | 11 (11 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #1F4E79 | 1F4E79 | Custom |
| #2E75B6 | 2E75B6 | Custom |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D6DCE4 | D6DCE4 | Silver (Neutral) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Retention_Schedule

**Data Rows:** 46 (rows 5–50)

### Columns

| Col | Header |
|-----|--------|
| A | Record Category ID |
| B | Category Name |
| C | Retention Period |
| D | Retention Basis |
| E | Basis Detail |
| F | Retention Trigger |
| G | Grace Period |
| H | Review Cycle |
| I | Last Review |
| J | Next Review |
| K | Notes |

---

## Sheet 3: Regulatory_Mapping

**Data Rows:** 22 (rows 8–29)

### Columns

| Col | Header |
|-----|--------|
| A | Regulation ID |
| B | Regulation Name |
| C | Section/Article |
| D | Record Types Affected |
| E | Required Retention |
| F | Retention Trigger |
| G | Penalty for Non-Compliance |
| H | Last Review |
| I | Reviewer |
| J | Notes |

---

## Sheet 4: Disposal_Queue

**Data Rows:** 46 (rows 5–50)

### Columns

| Col | Header |
|-----|--------|
| A | Queue ID |
| B | Record Category |
| C | Retention End Date |
| D | Volume - Physical |
| E | Volume - Electronic |
| F | Legal Hold Status |
| G | Disposal Priority |
| H | Target Disposal Date |
| I | Assigned To |
| J | Status |
| K | Notes |

---

## Sheet 5: Disposal_Method_Matrix

### Columns

| Col | Header |
|-----|--------|
| A | Classification |
| B | Physical - Paper |
| C | Physical - Media |
| D | Electronic - On-Prem |
| E | Electronic - Cloud |
| F | Verification Required |
| G | Approved Vendors |
| H | Special Handling |

---

## Sheet 6: Destruction_Verification

**Data Rows:** 56 (rows 5–60)

### Columns

| Col | Header |
|-----|--------|
| A | Destruction ID |
| B | Record Category |
| C | Volume |
| D | Destruction Date |
| E | Method Used |
| F | Performed By |
| G | Witness |
| H | Certificate Reference |
| I | Storage Location |
| J | Verification Status |

---

## Sheet 7: Exception_Register

**Data Rows:** 36 (rows 5–40)

### Columns

| Col | Header |
|-----|--------|
| A | Exception ID |
| B | Exception Type |
| C | Record Category |
| D | Original Retention |
| E | New Retention |
| F | Reason |
| G | Requested By |
| H | Approved By |
| I | Approval Date |
| J | Expiration |
| K | Status |

---

## Sheet 8: Compliance_Dashboard

**Data Rows:** 21 (rows 5–25)

### Columns

| Col | Header |
|-----|--------|
| A | Metric ID |
| B | Metric Name |
| C | Description |
| D | Target |
| E | Current Value |
| F | Trend |
| G | Status |
| H | Owner |
| I | Last Updated |

---

## Sheet 9: Gap_Analysis

**Data Rows:** 36 (rows 5–40)

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | Gap Category |
| C | Description |
| D | Related Item |
| E | Risk Rating |
| F | Remediation Action |
| G | Owner |
| H | Due Date |
| I | Status |

---

## Sheet 10: Evidence_Register

**Data Rows:** 46 (rows 5–50)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Description |
| C | Evidence Type |
| D | Related Item |
| E | Storage Location |
| F | Collected Date |
| G | Collected By |
| H | Verification Status |

---

## Sheet 11: Approval

**Data Rows:** 7 (rows 14–20)

---

**END OF SPECIFICATION**

---

*"The cost of storage is not just dollars - it is also risk."*
-- Anonymous Records Manager

<!-- QA_VERIFIED: 2026-02-06 -->
