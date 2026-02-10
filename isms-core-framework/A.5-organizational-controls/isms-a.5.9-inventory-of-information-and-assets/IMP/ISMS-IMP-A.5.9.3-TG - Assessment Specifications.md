<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.9.3-TG:framework:TG:a.5.9.3 -->
**ISMS-IMP-A.5.9.3-TG - Quality & Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Inventory Quality & Policy Compliance Verification |
| **Related Policy** | ISMS-POL-A.5.9, Section 2.3 (Mandatory Attributes), Section 2.5 (Quality Standards), Section 3 (Assessment Methodology) |
| **Purpose** | Verify inventory data quality (accuracy, completeness, currency) and compliance with policy requirements |
| **Target Audience** | Security Team, Quality Assurance, CMDB Administrators, Auditors |
| **Assessment Type** | Quality Verification & Compliance Audit |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial assessment specification following consolidated policy structure | ISMS Implementation Team |


---
# Technical Specification
**Audience:** Workbook developers (Python/Excel script maintainers)


> Auto-generated from `generate_a59_3_quality_compliance.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.9.3` |
| **Total Sheets** | 10 (10 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.9: Inventory of Information and Assets |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | header_bg | Dark Blue (Headers) |
| #006100 | green_dark | Dark Green (Pass) |
| #2E75B5 | 2E75B5 | Custom |
| #4472C4 | section_bg | Medium Blue (Sub-headers) |
| #9C0006 | red_dark | Dark Red (Error) |
| #9C5700 | yellow_dark | Custom |
| #C6EFCE | green_light | Light Green (Compliant/Pass) |
| #D8E4F8 | D8E4F8 | Pale Blue (Sub-section) |
| #D9D9D9 | gray_light | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FFC7CE | red_light | Light Red (Non-Compliant/Fail) |
| #FFEB9C | yellow_light | Light Yellow/Amber (Partial) |
| #FFF2CC | FFF2CC | Cream (Input Alt) |

## Sheet 1: Instructions

**Data Rows:** 4 (rows 5–8)

---

## Sheet 2: Accuracy_Sampling

**Data Rows:** 97 (rows 4–100)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Sample ID | 15 |
| B | Asset Category | 25 |
| C | Asset ID (Inventory) | 25 |
| D | Attribute Verified | 30 |
| E | Inventory Value | 30 |
| F | Ground Truth Value | 30 |
| G | Match? | 12 |
| H | Discrepancy Type | 25 |
| I | Verification Method | 30 |
| J | Verified By | 20 |
| K | Verification Date | 18 |
| L | Corrected? | 15 |
| M | Evidence ID | 15 |
| N | Notes | 30 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=COUNTA(A4:A{row-51})` |  |
| BN | `=COUNTIF(G4:G{row-51},` |  |
| BN | `=IFERROR(B{summary_row-1}/B{summary_row-2}*100,0)` |  |
| BN | `=B{summary_row-2}-98` |  |
| BN | `=IF(B{summary_row-3}>=98,` |  |

---

## Sheet 3: Completeness

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset Category | 25 |
| B | Mandatory Field | 30 |
| C | Total Assets | 15 |
| D | Assets with Field Populated | 20 |
| E | Completeness % | 16 |
| F | Target % | 12 |
| G | Gap | 12 |
| H | Status | 18 |
| I | Missing Count | 15 |
| J | Evidence ID | 15 |
| K | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| E4:EN | greaterThanOrEqual 95 |  |
| E4:EN | between 90 |  |
| E4:EN | lessThan 90 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IFERROR(D{row}/C{row}*100,0)` |  |
| GN | `=E{row}-{target}` |  |
| HN | `=IF(E{row}>={target},` |  |
| IN | `=C{row}-D{row}` |  |
| BN | `=IFERROR(AVERAGE(E4:E{row-1}),0)` |  |
| BN | `=B{summary_row-2}-95` |  |
| BN | `=IF(B{summary_row-3}>=95,` |  |

---

## Sheet 4: Currency

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset Category | 25 |
| B | Currency Metric | 30 |
| C | Total Assets | 15 |
| D | Assets Meeting Currency Target | 22 |
| E | Currency % | 15 |
| F | Target % | 12 |
| G | Gap | 12 |
| H | Status | 18 |
| I | Stale Assets Count | 18 |
| J | Evidence ID | 15 |
| K | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| E4:EN | greaterThanOrEqual 90 |  |
| E4:EN | between 85 |  |
| E4:EN | lessThan 85 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IFERROR(D{row}/C{row}*100,0)` |  |
| GN | `=E{row}-{target}` |  |
| HN | `=IF(E{row}>={target},` |  |
| IN | `=C{row}-D{row}` |  |
| BN | `=IFERROR(AVERAGE(E4:E{row-1}),0)` |  |
| BN | `=B{summary_row-2}-90` |  |
| BN | `=IF(B{summary_row-3}>=90,` |  |

---

## Sheet 5: Consistency

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Consistency Check | 35 |
| B | System A | 25 |
| C | System B | 25 |
| D | Records in A | 15 |
| E | Records in B | 15 |
| F | Matches | 15 |
| G | Consistency % | 16 |
| H | Target % | 12 |
| I | Gap | 12 |
| J | Status | 18 |
| K | Evidence ID | 15 |
| L | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| G4:GN | greaterThanOrEqual 95 |  |
| G4:GN | between 90 |  |
| G4:GN | lessThan 90 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| GN | `=IFERROR(F{row}/MAX(D{row},E{row})*100,0)` |  |
| IN | `=G{row}-{target}` |  |
| JN | `=IF(G{row}>={target},` |  |
| BN | `=IFERROR(AVERAGE(G4:G{row-1}),0)` |  |
| BN | `=B{summary_row-2}-95` |  |
| BN | `=IF(B{summary_row-3}>=95,` |  |

---

## Sheet 6: Policy_Compliance

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Policy Requirement | 50 |
| B | SHALL Requirement | 50 |
| C | Compliant Assets | 18 |
| D | Total Assets | 15 |
| E | Compliance % | 16 |
| F | Target | 12 |
| G | Gap | 12 |
| H | Status | 18 |
| I | Evidence ID | 15 |
| J | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| E4:EN | equal 100 |  |
| E4:EN | between 95 |  |
| E4:EN | lessThan 95 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IFERROR(C{row}/D{row}*100,0)` |  |
| GN | `=E{row}-{target}` |  |
| HN | `=IF(E{row}={target},` |  |
| BN | `=IFERROR(AVERAGE(E4:E{row-1}),0)` |  |
| BN | `=B{summary_row-2}-100` |  |
| BN | `=IF(B{summary_row-3}=100,` |  |

---

## Sheet 7: Quality_Metrics

**Data Rows:** 5 (rows 4–8)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=B{row}*{weight}/100` |  |
| FN | `=B{row}-{target}/100` |  |
| GN | `=IF(B{row}>={target}/100,` |  |
| BN | `=SUM(D4:D8)` |  |
| BN | `=B{overall_row-2}-0.97` |  |
| BN | `=IF(B{overall_row-3}>=0.97,` |  |
| AN | `=A{4+i}` |  |
| BN | `=B{4+i}` |  |
| CN | `=G{4+i}` |  |

---

## Sheet 8: Evidence_Register

**Data Rows:** 97 (rows 4–100)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 15 |
| B | Quality Dimension | 25 |
| C | Evidence Type | 30 |
| D | Evidence Description | 50 |
| E | Evidence Location | 40 |
| F | Collection Date | 15 |
| G | Collected By | 25 |
| H | Validity Period | 20 |
| I | Review Date | 15 |
| J | Reviewed By | 25 |
| K | Review Status | 20 |
| L | Retention End Date | 18 |
| M | Related Assessment | 25 |
| N | Notes | 40 |

---

## Sheet 9: Summary_Dashboard

---

## Sheet 10: Approval_Signoff

**Data Rows:** 4 (rows 2–5)

---

**END OF SPECIFICATION**

---

*"When it comes to atoms, language can be used only as in poetry."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
