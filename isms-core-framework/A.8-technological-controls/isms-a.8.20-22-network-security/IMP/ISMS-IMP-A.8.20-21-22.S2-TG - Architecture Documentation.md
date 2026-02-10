<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.20-21-22.S2-TG:framework:TG:a.8.20-21-22 -->
**ISMS-IMP-A.8.20-21-22.S2-TG - Network Architecture Documentation**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.20-21-22-S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Network Topology & Architecture Documentation |
| **Related Policy** | ISMS-POL-A.8.20-21-22, Section 2.1 (Network Infrastructure Security - A.8.20), Section 2.3 (Network Segmentation - A.8.22), Section 4.2 (Implementation Resources) |
| **Purpose** | Define standards and procedures for creating, maintaining, and validating network architecture documentation including topology diagrams, security zones, and trust boundaries |
| **Target Audience** | Network Architects, Network Engineers, Security Engineers, IT Operations, System Administrators, Auditors |
| **Assessment Type** | Technical Documentation & Architecture Validation |
| **Review Cycle** | Quarterly or After Major Network Architecture Changes |
| **Total Sheets** | 9 |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guidance for network architecture documentation | ISMS Implementation Team |

---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a820_2_device_security_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.20-21-22.S2` |
| **Output Filename** | `ISMS-IMP-A.8.20-21-22.S2_Network_Device_Security_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Network Device Security Assessment |
| **Total Sheets** | 16 (16 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls A.8.20, A.8.21, A.8.22: Network Security |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #002060 | 002060 | Custom |
| #003366 | 003366 | Dark Blue (Headers) |
| #006100 | 006100 | Dark Green (Pass) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #7F7F7F | 7F7F7F | Custom |
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

## Sheet 3: Device_Hardening_Assessment

**Data Rows:** 5 (rows 1–5) | **Frozen Panes:** F4

### Columns

| Col | Header |
|-----|--------|
| A | Device ID |
| B | Device Type |
| C | Hostname |
| D | Primary IP |
| E | Criticality |

---

## Sheet 4: Hardening_Baseline_Reference

---

## Sheet 5: Gap_Summary

**Data Rows:** 10 (rows 2–11) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | Device ID |
| C | Device Type |
| D | Hostname |
| E | Hardening Requirement |
| F | Current State |
| G | Gap Severity |
| H | Remediation Plan |
| I | Owner |
| J | Status |
| K | Target Date |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| GN:GN | equal  |  |
| GN:GN | equal  |  |
| GN:GN | equal  |  |
| GN:GN | equal  |  |

---

## Sheet 6: Compliance_Scoring

---

## Sheet 7: Compliance Status Distribution

---

## Sheet 8: Device_Type_Compliance

---

## Sheet 9: Average Compliance Score by Device Type

---

## Sheet 10: Compliance Score (%)

---

## Sheet 11: Device Type

---

## Sheet 12: Top_Gaps_Analysis

---

## Sheet 13: Most Common Hardening Failures

---

## Sheet 14: Failure Count

---

## Sheet 15: Requirement

---

## Sheet 16: Remediation_Roadmap

**Data Rows:** 7 (rows 2–8) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Priority |
| B | Severity |
| C | Gap Description |
| D | Affected Devices |
| E | Remediation Action |
| F | Owner |
| G | Target Date |
| H | Status |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| BN:BN | equal  |  |
| BN:BN | equal  |  |
| BN:BN | equal  |  |
| BN:BN | equal  |  |

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `HARDENING_REQUIREMENTS` | Default Credentials Disabled, Strong Password Policy, Multi-Factor Authentication (MFA), Unnecess... |

---

**END OF SPECIFICATION**

---

*"In attempting to construct such machines we should not be irreverently usurping His power of creating souls, any more than we are in the procreation of children."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
