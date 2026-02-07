**ISMS-IMP-A.5.30-8.13-14-S2-TG - Backup Implementation**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.13: Information Backup

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.30-8.13-14-S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Backup Implementation & Recovery Capability |
| **Related Policy** | ISMS-POL-A.5.30-8.13-14, Section 2.1 (Information Backup Requirements) |
| **Related Assessment** | ISMS-IMP-A.5.30-8.13-14-S1 (BIA - provides RPO requirements) |
| **Purpose** | Implement backup solutions aligned with BIA-determined RPO requirements, establish backup schedules, configure retention policies, implement backup monitoring, document recovery procedures |
| **Target Audience** | Backup Administrator, Storage Team, Database Administrators, System Administrators, IT Operations, BC/DR Coordinator |
| **Assessment Type** | Technical Implementation |
| **Review Cycle** | Quarterly (backup configuration) + After Major System Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial backup implementation methodology | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a530_2_redundancy_analysis.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.30.S2` |
| **Output Filename** | `ISMS-IMP-A.5.30.S2_Redundancy_Analysis_YYYYMMDD.xlsx` |
| **Workbook Title** | Redundancy Analysis & SPOF Assessment |
| **Total Sheets** | 8 (8 visible) |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: Summary

---

## Sheet 3: Redundancy_Inventory

**Data Rows:** 108 (rows 5–112) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | System Name |
| B | Criticality Tier |
| C | RTO Requirement (hours) |
| D | Redundancy Status |
| E | Architecture Type |
| F | Failover Type |
| G | Geographic Redundancy |
| H | Last Failover Test |
| I | Test Result |
| J | Notes |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(A5:A112)` | Total Systems: |
| — | `=COUNTIF(D5:D112,` | Systems with Redundancy: |
| — | `=IF(B115>0,B116/B115,0)` | Redundancy Coverage %: |
| — | `=COUNTIFS(B5:B112,` | Critical Systems (RTO < 4h): |
| — | `=IF(B118>0,B119/B118,1)` | Critical Coverage %: |

---

## Sheet 4: SPOF_Register

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | SPOF ID |
| B | System Affected |
| C | SPOF Component |
| D | SPOF Type |
| E | Risk Level |
| F | Mitigation Status |
| G | Mitigation Plan |
| H | Owner |
| I | Target Date |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B5:B104)` | Total SPOFs Identified: |
| — | `=COUNTIF(F5:F104,` | SPOFs Mitigated: |
| — | `=COUNTIFS(E5:E104,` | Critical Open SPOFs: |
| — | `=IF(B108>0,B109/B108,0)` | Mitigation Rate: |

---

## Sheet 5: RTO_Compliance

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | System Name |
| B | Criticality Tier |
| C | RTO Requirement (hours) |
| D | Actual Failover Time (hours) |
| E | RTO Compliant |
| F | Gap (hours) |
| G | Notes |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IF(AND(ISNUMBER(C{row}),ISNUMBER(D{row})),IF(D{row}<=C{row},` |  |

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
| — | `=COUNTA(Evidence_Register!A5:A104)` | Evidence Items: |

---

## Sheet 8: Base_Validations

---

**END OF SPECIFICATION**

---

*"A person who never made a mistake never tried anything new."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
