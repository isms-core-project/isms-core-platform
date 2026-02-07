**ISMS-IMP-A.8.20-21-22.S6-TG - Network Security Testing**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.20-21-22-S6-TG |
| **Version** | 1.0 |
| **Assessment Area** | Network Security Controls Testing & Validation |
| **Related Policy** | ISMS-POL-A.8.20-21-22, Section 3.2 (Monitoring & Reporting), Section 3.3 (Exception Management) |
| **Purpose** | Establish comprehensive testing methodologies for validating network security controls including segmentation effectiveness, firewall rules, device hardening, and service security configurations |
| **Target Audience** | Security Engineers, Network Administrators, Penetration Testers, Compliance Officers, ISMS Auditors |
| **Assessment Type** | Security Testing & Validation Assessment |
| **Review Cycle** | Semi-Annually or After Major Security Control Changes |
| **Total Sheets** | 11 |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guidance for network security testing | ISMS Implementation Team |

---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a820_6_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.20-21-22.6` |
| **Output Filename** | `ISMS-IMP-A.8.20-21-22.6_Network_Security_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Network Security Compliance Dashboard |
| **Total Sheets** | 11 (11 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #002060 | 002060 | Custom |
| #003366 | 003366 | Dark Blue (Headers) |
| #006100 | 006100 | Dark Green (Pass) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #9C0006 | 9C0006 | Dark Red (Error) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |

## Sheet 1: Instructions

---

## Sheet 2: Executive_Summary

---

## Sheet 3: Overall_Compliance

**Data Rows:** 150 (rows 4–153)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(` | Total Network Devices |
| — | `=COUNTIF(` | Segmentation Test Pass Rate |

---

## Sheet 4: WB1_Infrastructure

**Data Rows:** 150 (rows 4–153)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(` | Total Devices Inventoried |
| — | `=COUNTIF(` | Critical Devices |

---

## Sheet 5: WB2_Device_Security

**Data Rows:** 150 (rows 4–153)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIF(` | Devices Fully Compliant (≥95%) |
| — | `=COUNTIFS(` | Devices Partially Compliant |
| — | `=SUM(` | Total Hardening Gaps |

---

## Sheet 6: WB3_Services

**Data Rows:** 100 (rows 4–103)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(` | Total Services Cataloged |
| — | `=COUNTIF(` | Critical Services |

---

## Sheet 7: WB4_Segmentation

**Data Rows:** 100 (rows 4–103)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(` | Security Zones Defined |
| — | `=COUNTIF(` | Tests Passed |

---

## Sheet 8: WB5_Controls_Coverage

**Data Rows:** 40 (rows 4–43)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(` | Zones Assessed |
| — | `=COUNTIF(` | Zones Fully Covered (100%) |

---

## Sheet 9: Gap_Consolidation

**Data Rows:** 100 (rows 4–103)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=SUM(B{row-4}:B{row-1})` |  |
| CN | `=SUM(C{row-4}:C{row-1})` |  |
| DN | `=SUM(D{row-4}:D{row-1})` |  |
| EN | `=SUM(E{row-4}:E{row-1})` |  |

---

## Sheet 10: Action_Items

---

## Sheet 11: Management_Dashboard

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `REQUIRED_WORKBOOKS` | ISMS-IMP-A.8.20-21-22.S1.xlsx, ISMS-IMP-A.8.20-21-22.S2.xlsx, ISMS-IMP-A.8.20-21-22.S3.xlsx, ISMS... |

---

**END OF SPECIFICATION**

---

*"Classes will dull your mind, destroy the potential for authentic creativity."*
— John Nash

<!-- QA_VERIFIED: 2026-02-06 -->
