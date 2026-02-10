<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.32.1-TG:framework:TG:a.8.32.1 -->
**ISMS-IMP-A.8.32.1-TG - Change Process Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.32.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Change Process Workflow & Management Procedures |
| **Related Policy** | ISMS-POL-A.8.32, Section 2.1 (Change Process Requirements) |
| **Purpose** | Document change management processes, assess procedural capabilities against policy requirements, and identify gaps in a technology-agnostic manner |
| **Target Audience** | Change Manager, CAB Members, IT Operations, System Owners, Compliance Officers, Auditors, Workbook Developers |
| **Assessment Type** | Process & Procedural |
| **Review Cycle** | Quarterly or After Major Process Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial assessment specification for Change Process workbook | ISMS Implementation Team |


---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a832_1_change_process.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.32.1` |
| **Output Filename** | `ISMS-IMP-A.8.32.1_Change_Process_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Change Process Assessment |
| **Total Sheets** | 19 (19 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #B4C7E7 | B4C7E7 | Light Blue (Planned/Info) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E0E0E0 | E0E0E0 | Custom |
| #F5F5F5 | F5F5F5 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFD966 | FFD966 | Gold/Yellow (Highlight) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: Change_Process_Workflow

---

## Sheet 3: Approval_Authority_Matrix

---

## Sheet 4: CAB_Operations

---

## Sheet 5: Communication

---

## Sheet 6: Documentation_Records

---

## Sheet 7: Tool_Capabilities

---

## Sheet 8: Metrics_KPIs

---

## Sheet 9: Evidence_Register

---

## Sheet 10: Summary_Dashboard

---

## Sheet 11: Approval_Sign_Off

---

## Sheet 12: Instructions

**Frozen Panes:** A4

---

## Sheet 13: Cab_Operations

**Frozen Panes:** A6

### Columns

| Col | Header |
|-----|--------|
| A | Role |
| B | Name |
| C | Department |
| D | Authority Level |
| E | Mandatory/Optional |
| F | Delegate |
| G | Contact |
| H | Status |

---

## Sheet 14: Communication_Procedures

**Frozen Panes:** A6

---

## Sheet 15: Documentation_Requirements

**Frozen Panes:** A6

---

## Sheet 16: Change_Management_Tools

**Frozen Panes:** A6

---

## Sheet 17: Metrics_Kpis

**Frozen Panes:** A6

### Columns

| Col | Header |
|-----|--------|
| A | Metric Name |
| B | Description |
| C | Target |
| D | Current Value |
| E | Frequency |
| F | Data Source |
| G | Owner |
| H | Status |

---

## Sheet 18: Approval_Signoff

**Frozen Panes:** A3

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=TODAY()+90` |  |

---

## Sheet 19: Base_Validations

---

**END OF SPECIFICATION**

---

*"The enemy knows the system. Security through obscurity is not security at all."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
