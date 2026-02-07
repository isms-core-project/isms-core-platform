**ISMS-IMP-A.8.20-21-22.S1-TG - Network Discovery Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.20-21-22-S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Network Asset Discovery & Inventory |
| **Related Policy** | ISMS-POL-A.8.20-21-22, Section 2.1 (Network Infrastructure Security - A.8.20), Section 2.2 (Network Services Security - A.8.21), Section 2.3 (Network Segmentation - A.8.22) |
| **Purpose** | Provide systematic methodology for discovering and inventorying network infrastructure, services, and segments to support compliance assessment |
| **Target Audience** | Network Administrators, Security Engineers, ISMS Implementation Teams, Infrastructure Teams, Auditors |
| **Assessment Type** | Technical Discovery & Inventory |
| **Review Cycle** | Annually or After Major Network Changes |
| **Total Sheets** | 9 |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guidance for network discovery process | ISMS Implementation Team |

---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a820_1_infrastructure_inventory.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.20-21-22.S1` |
| **Workbook Title** | Network Infrastructure Inventory |
| **Total Sheets** | 13 (13 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls A.8.20, A.8.21, A.8.22: Network Security |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #002060 | 002060 | Custom |
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #92D050 | 92D050 | Green (Complete) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFFF00 | FFFF00 | Yellow (Warning) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Data_Validations

---

## Sheet 2: Instructions & Legend

---

## Sheet 3: Device_Inventory

**Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Device ID |
| B | Device Type |
| C | Make/Model |
| D | Hostname |
| E | Primary IP |
| F | Management IP |
| G | Location |
| H | Security Zone |
| I | Purpose |
| J | Criticality |
| K | Owner |
| L | Last Discovered |
| M | Discovery Method |
| N | Firmware Version |
| O | Serial Number |
| P | Compliance Status |
| Q | Status |
| R | Notes |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| JN:JN | equal  |  |
| JN:JN | equal  |  |
| JN:JN | equal  |  |
| JN:JN | equal  |  |
| QN:QN | equal  |  |
| QN:QN | equal  |  |
| QN:QN | equal  |  |

---

## Sheet 4: Device_Criticality_Matrix

---

## Sheet 5: Device_Type_Summary

---

## Sheet 6: Device Distribution by Type

---

## Sheet 7: Device Count by Criticality

---

## Sheet 8: Count

---

## Sheet 9: Criticality

---

## Sheet 10: Discovery_Metadata

**Data Rows:** 5 (rows 1–5)

---

## Sheet 11: Gap_Analysis

**Data Rows:** 9 (rows 2–10) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | Gap Type |
| C | Device/Location |
| D | Description |
| E | Severity |
| F | Impact |
| G | Remediation Plan |
| H | Owner |
| I | Status |
| J | Target Date |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| EN:EN | equal  |  |
| EN:EN | equal  |  |
| EN:EN | equal  |  |
| EN:EN | equal  |  |

---

## Sheet 12: Evidence_Register

**Data Rows:** 7 (rows 2–8) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Evidence Type |
| C | Description |
| D | File Location |
| E | Collection Date |
| F | Collected By |
| G | Status |
| H | Notes |

---

## Sheet 13: Validation_Rules

---

**END OF SPECIFICATION**

---

*"The idea behind digital computers may be explained by saying that these machines are intended to carry out any operations which could be done by a human computer."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
