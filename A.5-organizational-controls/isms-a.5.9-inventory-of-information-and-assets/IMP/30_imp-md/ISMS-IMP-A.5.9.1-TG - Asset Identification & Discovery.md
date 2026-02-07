**ISMS-IMP-A.5.9.1-TG - Asset Identification & Discovery**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Asset Identification & Discovery Procedures |
| **Related Policy** | ISMS-POL-A.5.9, Section 2.1 (Asset Inventory Creation), Section 2.5 (Inventory Quality Standards) |
| **Purpose** | Document asset discovery procedures, verify completeness of inventory, and identify gaps in asset identification across all categories |
| **Target Audience** | Security Team, IT Operations, System Owners, Information Owners, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Technical |
| **Review Cycle** | Quarterly or After Major Organizational Changes |
| **Date** | [Date]  |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date]  | Initial assessment specification following consolidated policy structure | ISMS Implementation Team |


---
# Technical Specification
**Audience:** Workbook developers (Python/Excel script maintainers)


> Auto-generated from `generate_a59_1_asset_discovery.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.9.1` |
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

## Sheet 2: Information_Assets

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset Subcategory | 25 |
| B | Discovery Method | 30 |
| C | Expected Count | 15 |
| D | Discovered Count | 15 |
| E | Completeness % | 15 |
| F | Compliance Status | 18 |
| G | Gaps Identified | 40 |
| H | Discovery Evidence | 30 |
| I | Next Discovery Actions | 40 |
| J | Responsible Party | 25 |
| K | Target Date | 15 |
| L | Evidence ID | 15 |
| M | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| E4:EN | greaterThanOrEqual 95 |  |
| E4:EN | between 85 |  |
| E4:EN | lessThan 85 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IFERROR(D{row}/C{row}*100,0)` |  |
| FN | `=IF(E{row}>=95,` |  |
| BN | `=SUM(C4:C{row-1})` |  |
| BN | `=SUM(D4:D{row-1})` |  |
| BN | `=IFERROR(B{summary_row-1}/B{summary_row-2}*100,0)` |  |
| BN | `=B{summary_row-2}-95` |  |

---

## Sheet 3: It_Infrastructure

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset Subcategory | 25 |
| B | Discovery Method | 30 |
| C | Expected Count | 15 |
| D | Discovered Count | 15 |
| E | Completeness % | 15 |
| F | Compliance Status | 18 |
| G | Gaps Identified | 40 |
| H | Discovery Evidence | 30 |
| I | Next Discovery Actions | 40 |
| J | Responsible Party | 25 |
| K | Target Date | 15 |
| L | Evidence ID | 15 |
| M | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| E4:EN | greaterThanOrEqual 98 |  |
| E4:EN | between 88 |  |
| E4:EN | lessThan 88 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IFERROR(D{row}/C{row}*100,0)` |  |
| FN | `=IF(E{row}>=98,` |  |
| BN | `=SUM(C4:C{row-1})` |  |
| BN | `=SUM(D4:D{row-1})` |  |
| BN | `=IFERROR(B{summary_row-1}/B{summary_row-2}*100,0)` |  |
| BN | `=B{summary_row-2}-98` |  |

---

## Sheet 4: Applications

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset Subcategory | 25 |
| B | Discovery Method | 30 |
| C | Expected Count | 15 |
| D | Discovered Count | 15 |
| E | Completeness % | 15 |
| F | Compliance Status | 18 |
| G | Gaps Identified | 40 |
| H | Discovery Evidence | 30 |
| I | Next Discovery Actions | 40 |
| J | Responsible Party | 25 |
| K | Target Date | 15 |
| L | Evidence ID | 15 |
| M | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| E4:EN | greaterThanOrEqual 90 |  |
| E4:EN | between 80 |  |
| E4:EN | lessThan 80 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IFERROR(D{row}/C{row}*100,0)` |  |
| FN | `=IF(E{row}>=90,` |  |
| BN | `=SUM(C4:C{row-1})` |  |
| BN | `=SUM(D4:D{row-1})` |  |
| BN | `=IFERROR(B{summary_row+2}/B{summary_row+1}*100,0)` |  |
| BN | `=B{summary_row+3}-90` |  |

---

## Sheet 5: Physical_Assets

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset Subcategory | 25 |
| B | Discovery Method | 30 |
| C | Expected Count | 15 |
| D | Discovered Count | 15 |
| E | Completeness % | 15 |
| F | Compliance Status | 18 |
| G | Gaps Identified | 40 |
| H | Discovery Evidence | 30 |
| I | Next Discovery Actions | 40 |
| J | Responsible Party | 25 |
| K | Target Date | 15 |
| L | Evidence ID | 15 |
| M | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| E4:EN | greaterThanOrEqual 90 |  |
| E4:EN | between 80 |  |
| E4:EN | lessThan 80 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IFERROR(D{row}/C{row}*100,0)` |  |
| FN | `=IF(E{row}>=90,` |  |
| BN | `=SUM(C4:C{row-1})` |  |
| BN | `=SUM(D4:D{row-1})` |  |
| BN | `=IFERROR(B{summary_row+2}/B{summary_row+1}*100,0)` |  |
| BN | `=B{summary_row+3}-90` |  |

---

## Sheet 6: Personnel_Assets

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset Subcategory | 25 |
| B | Discovery Method | 30 |
| C | Expected Count | 15 |
| D | Discovered Count | 15 |
| E | Completeness % | 15 |
| F | Compliance Status | 18 |
| G | Gaps Identified | 40 |
| H | Discovery Evidence | 30 |
| I | Next Discovery Actions | 40 |
| J | Responsible Party | 25 |
| K | Target Date | 15 |
| L | Evidence ID | 15 |
| M | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| E4:EN | equal 100 |  |
| E4:EN | between 90 |  |
| E4:EN | lessThan 90 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IFERROR(D{row}/C{row}*100,0)` |  |
| FN | `=IF(E{row}=100,` |  |
| BN | `=SUM(C4:C{row-1})` |  |
| BN | `=SUM(D4:D{row-1})` |  |
| BN | `=IFERROR(B{summary_row+2}/B{summary_row+1}*100,0)` |  |
| BN | `=B{summary_row+3}-100` |  |

---

## Sheet 7: Discovery_Metrics

**Data Rows:** 5 (rows 4–8)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset Category | 30 |
| B | Expected Count | 15 |
| C | Discovered Count | 15 |
| D | Completeness % | 15 |
| E | Target % | 12 |
| F | Gap vs. Target | 15 |
| G | Compliance Status | 20 |
| H | Priority | 15 |
| I | Key Gaps | 50 |
| J | Next Actions | 50 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| D4:D8 | greaterThanOrEqual 95 |  |
| D4:D8 | between 85 |  |
| D4:D8 | lessThan 85 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `={sheet_ref}!B22` | Adjust row as needed |
| CN | `={sheet_ref}!B23` | Adjust row as needed |
| DN | `=IFERROR(C{row}/B{row}*100,0)` |  |
| FN | `=D{row}-{target}` |  |
| GN | `=IF(D{row}>={target},` |  |
| HN | `=IF(F{row}<-10,` |  |
| BN | `=SUM(B4:B8)` |  |
| BN | `=SUM(C4:C8)` |  |
| BN | `=IFERROR(B{overall_row-1}/B{overall_row-2}*100,0)` |  |
| BN | `=B{overall_row-2}-95` |  |
| AN | `=A{4+i}` |  |
| BN | `=D{4+i}` |  |
| CN | `=G{4+i}` |  |

---

## Sheet 8: Evidence_Register

**Data Rows:** 97 (rows 4–100)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 15 |
| B | Asset Category | 25 |
| C | Discovery Method | 30 |
| D | Evidence Type | 30 |
| E | Evidence Description | 50 |
| F | Evidence Location | 40 |
| G | Collection Date | 15 |
| H | Collected By | 25 |
| I | Validity Period | 20 |
| J | Review Date | 15 |
| K | Reviewed By | 25 |
| L | Review Status | 20 |
| M | Retention End Date | 18 |
| N | Notes | 40 |

---

## Sheet 9: Summary_Dashboard

---

## Sheet 10: Approval_Signoff

**Data Rows:** 4 (rows 2–5)

---

**END OF SPECIFICATION**

---

*"No, no, you're not thinking; you're just being logical."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
