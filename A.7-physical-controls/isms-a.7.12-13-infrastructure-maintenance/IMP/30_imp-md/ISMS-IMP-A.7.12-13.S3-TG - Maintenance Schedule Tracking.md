**ISMS-IMP-A.7.12-13.S3-TG - Maintenance Schedule Tracking**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.13: Equipment Maintenance

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.12-13.S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Maintenance Schedule Tracking - Preventive Maintenance Planning, Schedule Compliance, Overdue Tracking |
| **Related Policy** | ISMS-POL-A.7.12-13, Section 2.2.1 (Maintenance Programme) |
| **Purpose** | Track preventive maintenance schedules, monitor compliance, identify overdue items, and ensure equipment reliability |
| **Target Audience** | IT Operations, Facilities Management, System Administrators, Asset Managers, Compliance Officers |
| **Assessment Type** | Operational Tracking |
| **Review Cycle** | Monthly Review, Quarterly Full Assessment |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Maintenance Schedule Tracking workbook | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a712_3_maintenance_schedule.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.7.12-13.S3` |
| **Output Filename** | `ISMS-IMP-A.7.12-13.S3_Maintenance_Schedule_Tracking_YYYYMMDD.xlsx` |
| **Workbook Title** | Maintenance Schedule Tracking |
| **Total Sheets** | 14 (14 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #808080 | 808080 | Gray (Disabled) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Equipment Schedule

---

## Sheet 3: Overdue Tracking

---

## Sheet 4: Upcoming Maintenance

---

## Sheet 5: Dashboard

---

## Sheet 6: Maintenance Log

---

## Sheet 7: Evidence Register

---

## Sheet 8: Instructions

---

## Sheet 9: Equipment_Schedule

**Data Rows:** 200 (rows 4–203)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Equipment ID | 15 |
| B | Equipment Type | 18 |
| C | Equipment Description | 35 |
| D | Location | 25 |
| E | Criticality | 18 |
| F | Maintenance Type | 22 |
| G | Frequency | 15 |
| H | Responsible Party | 20 |
| I | Last Completed | 15 |
| J | Next Due | 15 |
| K | Status | 15 |
| L | Days Until/Overdue | 18 |
| M | Record Ref | 18 |
| N | Notes | 40 |

---

## Sheet 10: Overdue_Tracking

**Data Rows:** 50 (rows 4–53)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Equipment ID | 15 |
| B | Equipment Description | 35 |
| C | Maintenance Type | 22 |
| D | Original Due Date | 18 |
| E | Days Overdue | 15 |
| F | Reason for Delay | 25 |
| G | Estimated Completion | 18 |
| H | Escalated | 12 |
| I | Escalated To | 20 |
| J | Compensating Control | 35 |
| K | Resolution Notes | 40 |

---

## Sheet 11: Upcoming_Maintenance

**Data Rows:** 30 (rows 7–36)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Equipment ID | 15 |
| B | Equipment Description | 35 |
| C | Maintenance Type | 22 |
| D | Due Date | 15 |
| E | Days Until Due | 15 |
| F | Scheduled Date | 15 |
| G | Assigned To | 20 |
| H | Vendor Booked | 15 |

---

## Sheet 12: Dashboard

**Data Rows:** 200 (rows 4–203)

### Columns

| Col | Header |
|-----|--------|
| A | Criticality |
| B | Total |
| C | Current |
| D | Due Soon |
| E | Overdue |
| F | % Current |

---

## Sheet 13: Maintenance_Log

**Data Rows:** 500 (rows 4–503)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Equipment ID | 15 |
| B | Maintenance Type | 22 |
| C | Scheduled Date | 15 |
| D | Actual Completion | 18 |
| E | Performed By | 25 |
| F | Record Reference | 20 |
| G | Findings/Notes | 40 |
| H | Follow-up Required | 18 |
| I | Follow-up Notes | 40 |

---

## Sheet 14: Evidence_Register

**Data Rows:** 100 (rows 4–103)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 12 |
| B | Evidence Type | 20 |
| C | Description | 40 |
| D | Related Equipment/Item | 25 |
| E | File Name | 30 |
| F | File Location | 45 |
| G | Collection Date | 15 |
| H | Collected By | 20 |
| I | Retention Period | 15 |
| J | Notes | 40 |

---

**END OF SPECIFICATION**

---

*"An ounce of prevention is worth a pound of cure."*
— Benjamin Franklin

<!-- QA_VERIFIED: 2026-02-06 -->
