<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.34.4-TG:framework:TG:a.5.34.4 -->
**ISMS-IMP-A.5.34.4-TG - Technical and Organizational Measures (TOMs) Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.34.4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Technical and Organizational Measures (TOMs) Assessment per GDPR Article 32 |
| **Related Policy** | ISMS-POL-A.5.34, Section 2.4 (Technical and Organizational Measures) |
| **Purpose** | Guide users through systematic evaluation of 20 GDPR Article 32 security measures, calculate compliance scoring, and identify gaps in pseudonymization, encryption, availability, and resilience controls |
| **Target Audience** | DPO/Privacy Officers, CISO, IT Security Teams, System Administrators, Cloud Architects, Compliance Officers, Auditors |
| **Assessment Type** | Technical Security Assessment |
| **Review Cycle** | Quarterly or after security architecture changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for TOMs assessment workbook | ISMS Implementation Team |

---


---
# Technical Specification


> Auto-generated from `generate_a5344_toms_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.34.4` |
| **Output Filename** | `ISMS-IMP-A.5.34.4_Technical_and_Organizational_Measures_(TOMs)_YYYYMMDD.xlsx` |
| **Workbook Title** | Technical and Organizational Measures (TOMs) |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | COLOR_HEADER | Dark Blue (Headers) |
| #BDD7EE | COLOR_PLANNED | Light Blue (Alt) |
| #C6EFCE | COLOR_IMPLEMENTED | Light Green (Compliant/Pass) |
| #D6DCE4 | COLOR_INSTRUCTION | Silver (Neutral) |
| #F2F2F2 | COLOR_CALCULATED | Very Light Gray (Protected/Alternating) |
| #FFC7CE | COLOR_CRITICAL | Light Red (Non-Compliant/Fail) |
| #FFD966 | COLOR_HIGH | Gold/Yellow (Highlight) |
| #FFEB9C | COLOR_MEDIUM | Light Yellow/Amber (Partial) |

## Sheet 1: 1. Instructions

**Data Rows:** 3 (rows 3–5)

---

## Sheet 2: 2. TOM Control Inventory

**Data Rows:** 20 (rows 2–21)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | TOM ID | 8 |
| B | TOM Category | 35 |
| C | TOM Type | 15 |
| D | Implementation Status | 20 |
| E | Implementation Date | 15 |
| F | Description of Implementation | 80 |
| G | Evidence Reference | 20 |
| H | Effectiveness Rating | 20 |
| I | Last Test Date | 15 |
| J | Gaps Identified | 60 |
| K | Risk Level | 15 |
| L | Remediation Plan | 60 |
| M | Remediation Owner | 25 |
| N | Target Completion Date | 15 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| D2:D21 | equal  |  |
| D2:D21 | equal  |  |
| D2:D21 | equal  |  |
| K2:K21 | equal  |  |
| K2:K21 | equal  |  |

---

## Sheet 3: 3. Technical Measures Detail

---

## Sheet 4: 4. Organizational Measures Detail

---

## Sheet 5: 5. Evidence Repository

**Data Rows:** 499 (rows 2–500)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 15 |
| B | TOM ID | 12 |
| C | Evidence Type | 35 |
| D | Description | 50 |
| E | File Location | 60 |
| F | Evidence Date | 15 |
| G | Verification Status | 20 |
| H | Verified By | 25 |
| I | Notes | 50 |

---

## Sheet 6: 6. Gap Analysis & Risk

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 10 |
| B | TOM ID | 12 |
| C | Gap Description | 60 |
| D | Likelihood | 15 |
| E | Impact | 15 |
| F | Overall Risk | 15 |
| G | Risk Score | 10 |
| H | Remediation Priority | 20 |
| I | Residual Risk | 20 |
| J | Acceptance Justification | 50 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| F2:F200 | equal  |  |
| F2:F200 | equal  |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| FN | `=IF(AND(D{row}=` |  |
| GN | `=IF(F{row}=` |  |

---

## Sheet 7: 7. Remediation Action Plan

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Action ID | 12 |
| B | TOM ID | 12 |
| C | Gap Description | 50 |
| D | Proposed Solution | 60 |
| E | Owner | 25 |
| F | Start Date | 12 |
| G | Target Date | 12 |
| H | Status | 20 |
| I | % Complete | 10 |
| J | Completion Date | 12 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| H2:H200 | equal  |  |
| H2:H200 | equal  |  |

---

## Sheet 8: 8. Compliance Dashboard

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| BN | greaterThanOrEqual 0.9 |  |
| BN | between 0.7 |  |
| BN | lessThan 0.7 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIF(` | Implemented |
| — | `=COUNTA(` | Total Gaps |

---

## Sheet 9: Header_Row

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `ACTION_STATUS` | Not Started, In Progress, Blocked, Complete, Cancelled |
| `EFFECTIVENESS` | Effective, Partially Effective, Ineffective, Not Tested |
| `IMPACT` | Critical, High, Medium, Low |
| `IMPL_STATUS` | Implemented, Partially Implemented, Planned, Not Implemented |
| `LIKELIHOOD` | High, Medium, Low |
| `RISK_LEVELS` | Critical, High, Medium, Low, N/A |

---

**END OF SPECIFICATION**

---

*"Even for the physicist the description in plain language will be a criterion of the degree of understanding that has been reached."*
— Werner Heisenberg

<!-- QA_VERIFIED: 2026-02-06 -->
