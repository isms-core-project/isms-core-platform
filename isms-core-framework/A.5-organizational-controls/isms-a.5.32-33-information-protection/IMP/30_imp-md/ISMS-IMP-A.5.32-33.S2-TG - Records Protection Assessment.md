**ISMS-IMP-A.5.32-33.S2-TG - Records Protection Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.33: Protection of Records

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.32-33.S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Records Identification, Classification, Protection Controls, and Integrity Verification |
| **Related Policy** | ISMS-POL-A.5.32-33, Section 2.2 (Records Protection) |
| **Purpose** | Guide users through systematic records inventory, classification, protection assessment, and integrity verification |
| **Target Audience** | Records Manager, CISO, Legal Counsel, System Owners, IT Teams, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Annual or After Significant System Changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Records Protection assessment workbook | ISMS Implementation Team |

---


---
# Technical Specification
**Audience:** Workbook Developers, Python/Excel Script Maintainers


> Auto-generated from `generate_a532_33_2_records_protection.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.32-33.S2` |
| **Output Filename** | `ISMS-IMP-A.5.32-33.S2_Records_Protection_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Records Protection Assessment |
| **Total Sheets** | 10 (10 visible) |
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

## Sheet 2: Records_Category_Inventory

**Data Rows:** 46 (rows 5–50)

### Columns

| Col | Header |
|-----|--------|
| A | Record Category ID |
| B | Category Name |
| C | Record Type |
| D | Description |
| E | Custodian Department |
| F | Storage Location |
| G | Format |
| H | Retention Requirement |
| I | Confidentiality |
| J | Integrity Requirement |
| K | Availability Requirement |
| L | Notes |

---

## Sheet 3: Protection_Controls

**Data Rows:** 46 (rows 5–50)

### Columns

| Col | Header |
|-----|--------|
| A | Record Category ID |
| B | Category Name |
| C | Confidentiality Controls |
| D | Integrity Controls |
| E | Availability Controls |
| F | Physical Controls |
| G | Control Effectiveness |
| H | Gap Description |
| I | Remediation Needed |
| J | Status |

---

## Sheet 4: Integrity_Verification

**Data Rows:** 36 (rows 5–40)

### Columns

| Col | Header |
|-----|--------|
| A | Test ID |
| B | Record Category |
| C | Integrity Mechanism |
| D | Test Date |
| E | Test Performed |
| F | Expected Result |
| G | Actual Result |
| H | Status |
| I | Issues |
| J | Remediation |

---

## Sheet 5: Access_Control_Review

**Data Rows:** 26 (rows 5–30)

### Columns

| Col | Header |
|-----|--------|
| A | System Name |
| B | Record Categories |
| C | Access Control Type |
| D | User Count |
| E | Privileged Users |
| F | Last Access Review |
| G | Access Logging |
| H | Log Retention |
| I | Issues |
| J | Remediation |
| K | Status |

---

## Sheet 6: Legal_Hold_Register

**Data Rows:** 26 (rows 5–30)

### Columns

| Col | Header |
|-----|--------|
| A | Hold ID |
| B | Matter Name |
| C | Legal Counsel |
| D | Effective Date |
| E | Record Categories |
| F | Custodians Notified |
| G | Notification Date |
| H | Release Date |
| I | Status |
| J | Notes |

---

## Sheet 7: Backup_Verification

**Data Rows:** 36 (rows 5–40)

### Columns

| Col | Header |
|-----|--------|
| A | Record Category |
| B | Backup System |
| C | Backup Frequency |
| D | Backup Location |
| E | Last Backup Date |
| F | Last Verification |
| G | Last Recovery Test |
| H | RTO Target |
| I | RTO Achieved |
| J | RPO Target |
| K | RPO Achieved |
| L | Status |
| M | Issues |

---

## Sheet 8: Gap_Analysis

**Data Rows:** 46 (rows 5–50)

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | Gap Category |
| C | Description |
| D | Related Record Category |
| E | Risk Rating |
| F | Remediation Action |
| G | Owner |
| H | Due Date |
| I | Status |
| J | Notes |

---

## Sheet 9: Evidence_Register

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

## Sheet 10: Approval

**Data Rows:** 7 (rows 14–20)

---

**END OF SPECIFICATION**

---

*"Records management is not just about what you keep, but how you keep it."*
-- Anonymous

<!-- QA_VERIFIED: 2026-02-06 -->
