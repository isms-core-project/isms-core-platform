**ISMS-IMP-A.8.17-S2-TG - Synchronization Verification Process & Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | System-Level Time Synchronization Status & Drift Measurement |
| **Related Policy** | ISMS-POL-A.8.17 (Clock Synchronization Policy - Section 2.3, 2.4) |
| **Purpose** | Verify all systems are actively synchronized to approved time sources, measure time drift, identify synchronization failures |
| **Target Audience** | System Administrators, Network Engineers, Security Engineers, ISMS Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Monthly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original Date] | Initial technical specification for synchronization verification procedures | Network Operations Manager |


---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, technical implementers


> Auto-generated from `generate_a817_2_sync_status.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.17.2` |
| **Output Filename** | `ISMS-IMP-A.8.17.2_Sync_Status_YYYYMMDD.xlsx` |
| **Total Sheets** | 5 (5 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.17: Clock Synchronization |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: System_Inventory

**Data Rows:** 999 (rows 2–1000) | **Frozen Panes:** A2

### Columns

| Col | Header |
|-----|--------|
| A | System Name [*] |
| B | Asset ID |
| C | Type [*] |
| D | OS/Platform |
| E | Criticality |
| F | NTP Server(s) Configured [*] |
| G | Sync Status [*] |
| H | Stratum |
| I | Current Drift (ms) [*] |
| J | Last Sync Time |
| K | Last Verified [*] |
| L | Compliance |
| M | Notes |

---

## Sheet 3: Drift_Analysis

**Data Rows:** 999 (rows 2–1000)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(System_Inventory!A2:A1000)` | Total Systems Assessed |
| — | `=COUNTIF(System_Inventory!G2:G1000,` | Systems Synchronized |
| — | `=COUNTIFS(System_Inventory!I2:I1000,` | ≤ 10ms (High-Precision) |

---

## Sheet 4: Gaps_Failures

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | System Name |
| B | Type |
| C | Criticality |
| D | Sync Status |
| E | Drift (ms) |
| F | Issue Category |
| G | Remediation Action |
| H | Target Date |

---

## Sheet 5: Compliance_Summary

**Data Rows:** 999 (rows 2–1000)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(System_Inventory!A2:A1000)` | Total Systems Assessed |
| — | `=COUNTIF(System_Inventory!G2:G1000,` | Systems Synchronized |
| — | `=COUNTIF(System_Inventory!L2:L1000,` | Systems Within Threshold |
| — | `=COUNTIF(System_Inventory!E2:E1000,` | 🔴 Critical |

---

**END OF SPECIFICATION**

---

*"The only reason for time is so that everything doesn't happen at once."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
