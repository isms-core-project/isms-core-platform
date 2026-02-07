**ISMS-IMP-A.8.17-S1-TG - Time Source Configuration & Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Time Source Infrastructure & Configuration |
| **Related Policy** | ISMS-POL-A.8.17 (Clock Synchronization Policy - Section 2.1, 2.2) |
| **Purpose** | Document authoritative time sources and internal NTP infrastructure, assess compliance with policy requirements |
| **Target Audience** | Network Engineers, System Administrators, Security Engineers, ISMS Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original Date] | Initial technical specification for time source configuration | Network Operations Manager |


---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, technical implementers


> Auto-generated from `generate_a817_1_time_sources.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.17.1` |
| **Output Filename** | `ISMS-IMP-A.8.17.1_Time_Sources_YYYYMMDD.xlsx` |
| **Total Sheets** | 5 (5 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.17: Clock Synchronization |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Time_Sources

**Data Rows:** 99 (rows 2–100) | **Frozen Panes:** A2

### Columns

| Col | Header |
|-----|--------|
| A | Source Name [*] |
| B | Type [*] |
| C | IP/Hostname [*] |
| D | Stratum [*] |
| E | Geographic Location |
| F | Provider |
| G | Availability SLA |
| H | Last Verified [*] |
| I | Status |
| J | Notes |

---

## Sheet 3: Internal_NTP_Servers

**Data Rows:** 99 (rows 2–100) | **Frozen Panes:** A2

### Columns

| Col | Header |
|-----|--------|
| A | Server Name [*] |
| B | IP Address [*] |
| C | Stratum [*] |
| D | Upstream Sources [*] |
| E | Location/Datacenter [*] |
| F | Redundancy Group |
| G | Peer Servers |
| H | Monitoring Status |
| I | Last Health Check [*] |
| J | Status |
| K | Notes |

---

## Sheet 4: Hierarchy

**Data Rows:** 99 (rows 2–100)

---

## Sheet 5: Compliance_Summary

**Data Rows:** 99 (rows 2–100)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Time_Sources!A2:A100)` | External Time Sources (Stratum 0/1) |
| — | `=COUNTA(Internal_NTP_Servers!A2:A100)` | Internal NTP Servers (Stratum 2) |
| — | `=COUNTIF(Time_Sources!I2:I100,\` | Active External Sources |
| — | `=COUNTIF(Internal_NTP_Servers!H2:H100,\` | Monitored Internal Servers |
| — | `=IF(B5<2,\` | Insufficient External Sources |
| — | `=IF(B6<2,\` | Insufficient Internal Servers |
| — | `=IF(B8<B6,\` | Unmonitored Servers |

---

**END OF SPECIFICATION**

---

*"Time is what keeps everything from happening at once."*
— Ray Cummings

<!-- QA_VERIFIED: 2026-02-06 -->
