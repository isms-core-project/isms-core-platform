<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.20-21-22.S5-TG:framework:TG:a.8.20-21-22 -->
**ISMS-IMP-A.8.20-21-22.S5-TG - Network Segmentation Implementation**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.20-21-22-S5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Network Segmentation Architecture & Implementation |
| **Related Policy** | ISMS-POL-A.8.20-21-22, Section 2.3 (Network Segmentation - A.8.22), Section 4.2 (Implementation Resources) |
| **Purpose** | Define systematic approach for designing, implementing, and validating network segmentation including security zones, VLANs, trust boundaries, and inter-zone traffic controls |
| **Target Audience** | Network Architects, Network Engineers, Security Engineers, Firewall Administrators, Cloud Administrators, Auditors |
| **Assessment Type** | Segmentation Architecture & Effectiveness Assessment |
| **Review Cycle** | Quarterly or After Segmentation Architecture Changes |
| **Total Sheets** | 11 |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guidance for network segmentation | ISMS Implementation Team |

---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a820_5_controls_coverage.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.20-21-22.S5` |
| **Output Filename** | `ISMS-IMP-A.8.20-21-22.S5_Network_Controls_Coverage_Matrix_YYYYMMDD.xlsx` |
| **Workbook Title** | Network Security Controls Coverage Matrix |
| **Total Sheets** | 11 (11 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls A.8.20, A.8.21, A.8.22: Network Security |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #002060 | 002060 | Custom |
| #003366 | 003366 | Dark Blue (Headers) |
| #006100 | 006100 | Dark Green (Pass) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #92D050 | 92D050 | Green (Complete) |
| #9C0006 | 9C0006 | Dark Red (Error) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFF00 | FFFF00 | Yellow (Warning) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Data_Validations

---

## Sheet 2: Instructions & Guide

---

## Sheet 3: Controls_Coverage_Matrix

**Frozen Panes:** C4

---

## Sheet 4: Zone_Control_Assessment

**Data Rows:** 11 (rows 1–11) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Zone ID |
| B | Zone Name |
| C | Risk Level |
| D | Controls Required |
| E | Controls Implemented |
| F | Control Coverage % |
| G | Effectiveness Rating |
| H | Gaps Identified |
| I | Last Assessment |
| J | Assessed By |
| K | Notes |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| GN:GN | equal  |  |
| GN:GN | equal  |  |
| GN:GN | equal  |  |

---

## Sheet 5: Device_Control_Mapping

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Device ID |
| B | Device Type |
| C | Hostname |
| D | Security Zone |
| E | Controls Provided |
| F | Control Category |
| G | Hardening Score |
| H | Effectiveness |
| I | Last Assessed |
| J | Notes |

---

## Sheet 6: Service_Control_Mapping

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Service ID |
| B | Service Type |
| C | Service Name |
| D | Controls Provided |
| E | Control Category |
| F | Security Score |
| G | Zones Served |
| H | Last Assessed |
| I | Notes |

---

## Sheet 7: Control_Effectiveness

**Data Rows:** 6 (rows 3–8)

### Columns

| Col | Header |
|-----|--------|
| A | Control Name |
| B | Control Category |
| C | Zones Covered |
| D | Total Zones |
| E | Coverage % |
| F | Effectiveness Rating |
| G | Weaknesses |
| H | Improvement Actions |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| FN:FN | equal  |  |
| FN:FN | equal  |  |

---

## Sheet 8: Coverage_Gaps

**Data Rows:** 9 (rows 2–10) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | Zone/Asset |
| C | Missing Control |
| D | Control Category |
| E | Risk |
| F | Severity |
| G | Remediation Plan |
| H | Owner |
| I | Target Date |
| J | Status |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| FN:FN | equal  |  |
| FN:FN | equal  |  |
| FN:FN | equal  |  |

---

## Sheet 9: Defense_In_Depth

**Data Rows:** 8 (rows 1–8) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Zone/Asset |
| B | Risk Level |
| C | Layer 1 Control |
| D | Layer 2 Control |
| E | Layer 3 Control |
| F | Additional Layers |
| G | Defense-in-Depth OK |
| H | Notes |

---

## Sheet 10: Compliance_Dashboard

---

## Sheet 11: Executive_Summary

---

**END OF SPECIFICATION**

---

*"The best ideas are the ones that show something unexpected, something that challenges the ordinary view."*
— John Nash

<!-- QA_VERIFIED: 2026-02-06 -->
