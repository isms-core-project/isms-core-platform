<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.9.2-TG:framework:TG:a.5.9.2 -->
**ISMS-IMP-A.5.9.2-TG - Inventory Maintenance**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Inventory Structure & Maintenance Procedures |
| **Related Policy** | ISMS-POL-A.5.9, Section 2.2 (Asset Categorization), Section 2.3 (Mandatory Inventory Attributes), Section 2.5 (Inventory Quality Standards), Section 2.6 (Integration Requirements) |
| **Purpose** | Document inventory structure, update procedures, integration mechanisms, and maintenance workflows |
| **Target Audience** | Security Team, IT Operations, System Owners, Information Owners, CMDB Administrators, Integration Engineers |
| **Assessment Type** | Operational & Technical |
| **Review Cycle** | Quarterly or After Inventory Structure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial assessment specification following consolidated policy structure | ISMS Implementation Team |


---
# Technical Specification
**Audience:** Workbook developers (Python/Excel script maintainers)


> Auto-generated from `generate_a59_2_inventory_maintenance.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.9.2` |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.9: Inventory of Information and Assets |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | header_bg | Dark Blue (Headers) |
| #006100 | green_dark | Dark Green (Pass) |
| #2E75B5 | 2E75B5 | Custom |
| #4472C4 | section_bg | Medium Blue (Sub-headers) |
| #9C0006 | red_dark | Dark Red (Error) |
| #9C5700 | yellow_dark | Custom |
| #C6EFCE | green_light | Light Green (Compliant/Pass) |
| #D8E4F8 | D8E4F8 | Pale Blue (Sub-section) |
| #D9D9D9 | gray_light | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FFC7CE | red_light | Light Red (Non-Compliant/Fail) |
| #FFEB9C | yellow_light | Light Yellow/Amber (Partial) |
| #FFF2CC | FFF2CC | Cream (Input Alt) |

## Sheet 1: Instructions

**Data Rows:** 4 (rows 5–8)

---

## Sheet 2: Inventory_Structure

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | System Component | 30 |
| B | Technology/Platform | 25 |
| C | Purpose | 40 |
| D | Data Stored | 40 |
| E | Owner | 20 |
| F | Backup Frequency | 20 |
| G | Availability | 15 |
| H | Documentation | 30 |
| I | Last Review | 15 |
| J | Status | 15 |
| K | Evidence ID | 15 |
| L | Notes | 30 |

---

## Sheet 3: Update_Triggers

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Update Trigger Event | 35 |
| B | Trigger Source | 25 |
| C | Workflow Documented? | 20 |
| D | Automation Level | 20 |
| E | Target SLA (Days) | 15 |
| F | Actual Avg Time (Days) | 18 |
| G | SLA Compliance % | 16 |
| H | Compliance Status | 18 |
| I | Responsible Party | 25 |
| J | Procedure Location | 35 |
| K | Last Review | 15 |
| L | Evidence ID | 15 |
| M | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| G4:GN | greaterThanOrEqual 95 |  |
| G4:GN | between 80 |  |
| G4:GN | lessThan 80 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| GN | `=IF(F{row}=` |  |
| HN | `=IF(G{row}=` |  |
| BN | `=COUNTA(A4:A{row-1})` |  |
| BN | `=COUNTIF(C4:C{row-1},` |  |
| BN | `=IFERROR(B{summary_row-1}/B{summary_row-2}*100,0)` |  |
| BN | `=COUNTIF(D4:D{row-1},` |  |
| BN | `=IFERROR(AVERAGE(G4:G{row-1}),0)` |  |

---

## Sheet 4: Integration_Architecture

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Source System | 30 |
| B | Integration Type | 25 |
| C | Data Flow | 30 |
| D | Frequency | 20 |
| E | Status | 15 |
| F | Last Successful Run | 18 |
| G | Success Rate % | 15 |
| H | Health Status | 18 |
| I | Owner | 20 |
| J | Documentation | 35 |
| K | Monitoring | 25 |
| L | Evidence ID | 15 |
| M | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| G4:GN | greaterThanOrEqual 98 |  |
| G4:GN | between 90 |  |
| G4:GN | lessThan 90 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| HN | `=IF(G{row}=` |  |
| BN | `=COUNTA(A4:A{row-6})` |  |
| BN | `=COUNTIF(E4:E{row-6},` |  |
| BN | `=COUNTIF(H4:H{row-6},` |  |
| BN | `=IFERROR(B{summary_row-1}/B{summary_row-2}*100,0)` |  |
| BN | `=IFERROR(AVERAGE(G4:G{row-6}),0)` |  |

---

## Sheet 5: Quality_Control

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Quality Control Process | 35 |
| B | Frequency | 20 |
| C | Documented? | 15 |
| D | Last Performed | 18 |
| E | Responsible Party | 25 |
| F | Issues Found (Last Run) | 25 |
| G | Issues Resolved | 20 |
| H | Effectiveness % | 18 |
| I | Status | 18 |
| J | Evidence ID | 15 |
| K | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| H4:HN | greaterThanOrEqual 90 |  |
| H4:HN | between 70 |  |
| H4:HN | lessThan 70 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| HN | `=IF(OR(F{row}=` |  |
| IN | `=IF(H{row}=` |  |
| BN | `=COUNTA(A4:A{row-1})` |  |
| BN | `=COUNTIF(C4:C{row-1},` |  |
| BN | `=IFERROR(B{summary_row-1}/B{summary_row-2}*100,0)` |  |
| BN | `=IFERROR(AVERAGE(H4:H{row-1}),0)` |  |

---

## Sheet 6: Maintenance_Metrics

**Data Rows:** 4 (rows 5–8)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=B{row}-VALUE(LEFT(C{row},LEN(C{row})-1))/100` |  |
| EN | `=IF(B{row}>=VALUE(LEFT(C{row},LEN(C{row})-1))/100,` |  |
| BN | `=AVERAGE(B5:B8)` |  |
| BN | `=B{overall_row-2}-0.95` |  |
| AN | `=A{5+i}` |  |
| BN | `=B{5+i}` |  |
| CN | `=E{5+i}` |  |

---

## Sheet 7: Evidence_Register

**Data Rows:** 97 (rows 4–100)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 15 |
| B | Maintenance Area | 30 |
| C | Evidence Type | 30 |
| D | Evidence Description | 50 |
| E | Evidence Location | 40 |
| F | Collection Date | 15 |
| G | Collected By | 25 |
| H | Validity Period | 20 |
| I | Review Date | 15 |
| J | Reviewed By | 25 |
| K | Review Status | 20 |
| L | Retention End Date | 18 |
| M | Related Assessment | 25 |
| N | Notes | 40 |

---

## Sheet 8: Summary_Dashboard

---

## Sheet 9: Approval_Signoff

**Data Rows:** 4 (rows 2–5)

---

**END OF SPECIFICATION**

---

*"Truth and clarity are complementary."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
