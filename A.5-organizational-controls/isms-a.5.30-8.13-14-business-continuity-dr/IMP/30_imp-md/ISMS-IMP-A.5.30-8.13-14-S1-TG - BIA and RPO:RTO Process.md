**ISMS-IMP-A.5.30-8.13-14-S1-TG - BIA and RPO/RTO Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.13: Information Backup

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.30-8.13-14-S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Business Impact Analysis & Recovery Requirements Definition |
| **Related Policy** | ISMS-POL-A.5.30-8.13-14, Section 2.3.1 (Business Impact Analysis Requirements) |
| **Purpose** | Define systematic methodology for conducting BIA, determining system criticality, establishing RPO/RTO requirements, documenting recovery priorities |
| **Target Audience** | BC/DR Coordinator, Business Process Owners, System Owners, IT Management, Executive Management, Risk Management, Compliance Officers |
| **Assessment Type** | Business & Technical |
| **Review Cycle** | Annual or After Major Business/System Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial methodology for BIA and RPO/RTO determination | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a530_1_backup_inventory.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.30.S1` |
| **Output Filename** | `ISMS-IMP-A.5.30.S1_Backup_Inventory_YYYYMMDD.xlsx` |
| **Workbook Title** | Backup Inventory & Coverage Assessment |
| **Total Sheets** | 8 (8 visible) |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #808080 | 808080 | Gray (Disabled) |
| #B4C7E7 | B4C7E7 | Light Blue (Planned/Info) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: Summary

---

## Sheet 3: Backup_Inventory

**Data Rows:** 110 (rows 5–114) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | System Name |
| B | Criticality Tier |
| C | Backup Status |
| D | Backup Solution |
| E | Backup Frequency |
| F | Last Backup Date |
| G | Offsite Backup |
| H | Immutable Backup |
| I | Last Test Date |
| J | Test Result |
| K | Notes |

---

## Sheet 4: RPO_Compliance

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | System Name |
| B | Criticality Tier |
| C | RPO Requirement (hours) |
| D | Backup Frequency (hours) |
| E | RPO Compliant |
| F | Gap (hours) |
| G | Notes |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IF(AND(ISNUMBER(C{row}),ISNUMBER(D{row})),IF(D{row}<=C{row},` |  |

---

## Sheet 5: 3-2-1-1-0_Compliance

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | System Name |
| B | Criticality |
| C | 3 Copies |
| D | 2 Media Types |
| E | 1 Offsite |
| F | 1 Immutable |
| G | 0 Errors (Tested) |
| H | Total Score (0-5) |
| I | Compliance Status |
| J | Notes |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| HN | `=(IF(C{row}=` |  |
| IN | `=IF(H{row}=` |  |

---

## Sheet 6: Evidence_Register

**Data Rows:** 100 (rows 1–100) | **Frozen Panes:** A5

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

## Sheet 7: Approval_Sign_Off

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A3

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Evidence_Register!A5:A104)` | Evidence Items Collected: |

---

## Sheet 8: Base_Validations

---

**END OF SPECIFICATION**

---

*"The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
