<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.34.6-TG:framework:TG:a.5.34.6 -->
**ISMS-IMP-A.5.34.6-TG - Cross-Border Data Transfer Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.34.6-TG |
| **Version** | 1.0 |
| **Assessment Area** | Cross-Border Data Transfer Assessment and GDPR Chapter V Compliance |
| **Related Policy** | ISMS-POL-A.5.34, Section 2.6 (Cross-Border Transfers) |
| **Purpose** | Guide users through transfer inventory, Transfer Impact Assessments (TIAs), and compliance with GDPR Chapter V (Articles 44-50) and post-Schrems II requirements |
| **Target Audience** | DPO/Privacy Officers, Legal Counsel, Procurement Teams, IT/Cloud Teams, Third-Party Risk Management, Compliance Officers, Auditors |
| **Assessment Type** | Legal & Technical Compliance |
| **Review Cycle** | Quarterly or upon new international transfers |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Cross-Border Transfer assessment workbook | ISMS Implementation Team |
---


---
# Technical Specification


> Auto-generated from `generate_a5346_cross_border_transfer_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.34.6` |
| **Output Filename** | `ISMS-IMP-A.5.34.6_Cross-Border_Transfer_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Cross-Border Transfer Assessment |
| **Total Sheets** | 8 (8 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Sheet 1: Instructions

**Data Rows:** 3 (rows 1–3)

---

## Sheet 2: Transfer Register

**Data Rows:** 999 (rows 2–1000)

### Columns

| Col | Header |
|-----|--------|
| A | Transfer ID |
| B | Status |
| C | Transfer Name |
| D | Source System |
| E | Destination System |
| F | Destination Country |
| G | Adequacy Status |
| H | Transfer Mechanism |
| I | SCC Version |
| J | SCC Date |
| K | DPF Cert? |
| L | TIA Required? |
| M | TIA ID |
| N | PII Categories |
| O | Transfer Volume |
| P | Transfer Frequency |
| Q | Purpose |
| R | Legal Basis (Art.6) |
| S | Last Updated |
| T | Notes |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| A2 | `=TEXT(ROW()-1,` |  |

---

## Sheet 3: TIA Register

**Data Rows:** 999 (rows 2–1000)

### Columns

| Col | Header |
|-----|--------|
| A | TIA ID |
| B | Transfer ID |
| C | Status |
| D | Destination Country |
| E | Assessment Date |
| F | Assessor |
| G | Surveillance Laws |
| H | Gov Access Risk |
| I | Risk Justification |
| J | Supplementary Measures |
| K | Residual Risk |
| L | TIA Conclusion |
| M | DPO Approval |
| N | Next Review Date |
| O | Notes |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| A2 | `=TEXT(ROW()-1,` |  |

---

## Sheet 4: Processor Tracker

**Data Rows:** 999 (rows 2–1000)

### Columns

| Col | Header |
|-----|--------|
| A | Processor ID |
| B | Transfer ID |
| C | Processor Name |
| D | Processor Location |
| E | DPA Exists? |
| F | DPA Date |
| G | SCCs Included? |
| H | SCC Version |
| I | SCC Date |
| J | Subprocessors? |
| K | Compliance Status |
| L | Gap Description |
| M | Remediation Action |
| N | Owner |
| O | Deadline |
| P | Notes |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| A2 | `=TEXT(ROW()-1,` |  |

---

## Sheet 5: Evidence Repository

**Data Rows:** 999 (rows 2–1000)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Transfer ID |
| C | TIA ID |
| D | Evidence Type |
| E | Description |
| F | Document Name |
| G | File Location |
| H | Upload Date |
| I | Owner |
| J | Status |
| K | Notes |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| A2 | `=TEXT(ROW()-1,` |  |

---

## Sheet 6: Gap Analysis

**Data Rows:** 999 (rows 2–1000)

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | Transfer ID |
| C | Gap Type |
| D | Description |
| E | Risk Level |
| F | Affected Data Subjects |
| G | Discovery Date |
| H | Remediation Action |
| I | Owner |
| J | Target Date |
| K | Status |
| L | Notes |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| E2:E1000 | equal  | Fill: light_red |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| A2 | `=TEXT(ROW()-1,` |  |

---

## Sheet 7: Dashboard

**Data Rows:** 3 (rows 1–3)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(` | Total Transfers |
| — | `=COUNTIF(` | TIAs Required |

---

## Sheet 8: Approvals

**Data Rows:** 999 (rows 2–1000)

### Columns

| Col | Header |
|-----|--------|
| A | Approval ID |
| B | Approval Type |
| C | Transfer/TIA ID |
| D | Description |
| E | Approver Name |
| F | Approver Role |
| G | Approval Date |
| H | Status |
| I | Notes |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| A2 | `=TEXT(ROW()-1,` |  |

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `EU_ADEQUACY_COUNTRIES` | Andorra, Argentina, Canada (Commercial), Faroe Islands, Guernsey, Israel, Isle of Man, Japan, Jer... |
| `RISK_LEVELS` | Low, Medium, High, Critical |
| `STATUS_OPTIONS` | Not Started, In Progress, Complete, Validated |

---

**END OF SPECIFICATION**

---

*"The problems of language here are really serious. We wish to speak in some way about the structure of the atoms. But we cannot speak about atoms in ordinary language."*
— Werner Heisenberg

<!-- QA_VERIFIED: 2026-02-06 -->
