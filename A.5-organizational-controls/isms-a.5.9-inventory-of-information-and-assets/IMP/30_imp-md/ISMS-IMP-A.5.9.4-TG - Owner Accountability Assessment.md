**ISMS-IMP-A.5.9.4-TG - Owner Accountability Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Asset Ownership Assignment & Accountability Verification |
| **Related Policy** | ISMS-POL-A.5.9, Section 2.4 (Ownership and Accountability), Section 4 (Roles and Responsibilities) |
| **Purpose** | Verify asset ownership is assigned, acknowledged, and understood; validate owner accountability and performance |
| **Target Audience** | Security Team, Asset Owners, Management, HR, Compliance Officers |
| **Assessment Type** | Ownership Verification & Accountability Audit |
| **Review Cycle** | Quarterly or After Significant Ownership Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial assessment specification following consolidated policy structure | ISMS Implementation Team |


---
# Technical Specification
**Audience:** Workbook developers (Python/Excel script maintainers)


> Auto-generated from `generate_a59_4_owner_accountability.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.9.4` |
| **Total Sheets** | 9 (9 visible) |
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

## Sheet 2: Ownership_Coverage

**Data Rows:** 5 (rows 4–8)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset Category | 25 |
| B | Total Assets | 15 |
| C | Assets with Owner | 18 |
| D | Assets without Owner | 18 |
| E | Coverage % | 15 |
| F | Target % | 12 |
| G | Gap | 12 |
| H | Status | 18 |
| I | Unique Owners Count | 18 |
| J | Avg Assets per Owner | 18 |
| K | Evidence ID | 15 |
| L | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| E4:E8 | equal 100 |  |
| E4:E8 | between 95 |  |
| E4:E8 | lessThan 95 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=B{row}-C{row}` |  |
| EN | `=IFERROR(C{row}/B{row}*100,0)` |  |
| GN | `=E{row}-100` |  |
| HN | `=IF(E{row}=100,` |  |
| JN | `=IFERROR(B{row}/I{row},0)` |  |
| BN | `=SUM(B4:B8)` |  |
| BN | `=SUM(C4:C8)` |  |
| BN | `=SUM(D4:D8)` |  |
| BN | `=IFERROR(B{summary_row-2}/B{summary_row-3}*100,0)` |  |
| BN | `=B{summary_row-2}-100` |  |
| BN | `=IF(B{summary_row-3}=100,` |  |

---

## Sheet 3: Owner_Acknowledgment

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Owner Name | 25 |
| B | Owner Email | 30 |
| C | Department | 20 |
| D | Assets Count | 15 |
| E | Email Sent Date | 18 |
| F | Reminder 1 (Day 7) | 18 |
| G | Reminder 2 (Day 14) | 18 |
| H | Reminder 3 (Day 21) | 18 |
| I | Escalation (Day 28) | 18 |
| J | Response Date | 18 |
| K | Days to Respond | 15 |
| L | Attestation Status | 20 |
| M | Next Action | 25 |
| N | Evidence ID | 15 |
| O | Notes | 30 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| KN | `=IF(AND(E{row}<>` |  |
| BN | `=COUNTA(A4:A{row-31})` |  |
| BN | `=COUNTIFS(L4:L{row-31},` |  |
| BN | `=IFERROR(B{summary_row-1}/B{summary_row-2}*100,0)` |  |
| BN | `=B{summary_row-2}-95` |  |
| BN | `=IFERROR(AVERAGE(K4:K{row-31}),0)` |  |
| BN | `=IF(B{summary_row-4}>=95,` |  |

---

## Sheet 4: Owner_Awareness

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Owner Name | 25 |
| B | Assets Assigned | 15 |
| C | Assets Identified by Owner | 22 |
| D | Awareness % | 15 |
| E | Target % | 12 |
| F | Gap | 12 |
| G | Status | 18 |
| H | Verification Method | 30 |
| I | Verification Date | 18 |
| J | Evidence ID | 15 |
| K | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| D4:DN | equal 100 |  |
| D4:DN | between 95 |  |
| D4:DN | lessThan 95 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=IFERROR(C{row}/B{row}*100,0)` |  |
| FN | `=D{row}-100` |  |
| GN | `=IF(D{row}=100,` |  |
| BN | `=IFERROR(AVERAGE(D4:D{row-31}),0)` |  |
| BN | `=B{summary_row-2}-100` |  |
| BN | `=IF(B{summary_row-3}=100,` |  |

---

## Sheet 5: Owner_Performance

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Owner Name | 25 |
| B | Assets Count | 15 |
| C | Reviews Due | 15 |
| D | Reviews Completed | 18 |
| E | Review Compliance % | 18 |
| F | Avg Response Time (Days) | 22 |
| G | Target Response (Days) | 20 |
| H | Responsiveness % | 18 |
| I | Performance Score | 18 |
| J | Target | 12 |
| K | Status | 18 |
| L | Evidence ID | 15 |
| M | Notes | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| I4:IN | greaterThanOrEqual 80 |  |
| I4:IN | between 75 |  |
| I4:IN | lessThan 75 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IFERROR(D{row}/C{row}*100,0)` |  |
| HN | `=IF(F{row}=` |  |
| IN | `=IF(OR(E{row}=` |  |
| KN | `=IF(I{row}=` |  |
| BN | `=IFERROR(AVERAGE(I4:I{row-31}),0)` |  |
| BN | `=B{summary_row-2}-80` |  |
| BN | `=IF(B{summary_row-3}>=80,` |  |

---

## Sheet 6: Accountability_Metrics

**Data Rows:** 4 (rows 4–7)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=B{row}*{weight}/100` |  |
| FN | `=B{row}-{target}/100` |  |
| GN | `=IF(B{row}>={target}/100,` |  |
| BN | `=SUM(D4:D7)` |  |
| BN | `=B{overall_row-2}-0.94` |  |
| BN | `=IF(B{overall_row-3}>=0.94,` |  |
| AN | `=A{4+i}` |  |
| BN | `=B{4+i}` |  |
| CN | `=G{4+i}` |  |

---

## Sheet 7: Evidence_Register

**Data Rows:** 97 (rows 4–100)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 15 |
| B | Accountability Domain | 25 |
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

## Sheet 8: Summary_Dashboard

---

## Sheet 9: Approval_Signoff

**Data Rows:** 4 (rows 2–5)

---

**END OF SPECIFICATION**

---

*"We are all agreed that your theory is crazy. The question which divides us is whether it is crazy enough."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
