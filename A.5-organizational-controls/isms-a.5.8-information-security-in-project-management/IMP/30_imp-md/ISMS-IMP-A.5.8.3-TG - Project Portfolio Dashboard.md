**ISMS-IMP-A.5.8.3-TG - Project Portfolio Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.8: Information Security in Project Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.8.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Project Portfolio Security Status & Executive Visibility |
| **Related Policy** | ISMS-POL-A.5.8 (All Sections - Portfolio-Wide View) |
| **Purpose** | Consolidated executive dashboard aggregating security status across all organizational projects, providing portfolio-wide visibility, trend analysis, gap identification, and lessons learned synthesis for strategic decision-making |
| **Target Audience** | CISO, Executive Management, PMO Director, Board of Directors, Internal Auditors, External Auditors |
| **Assessment Type** | Consolidated Dashboard & Portfolio Analysis (Layer 2 - consolidates multiple A.5.8.1 assessments) |
| **Review Cycle** | Quarterly (minimum) or After Major Project Milestones |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Initial | Initial specification for Project Portfolio Dashboard workbook | ISMS Implementation Team |

---
# Technical Specification
**Audience:** Workbook Developers, Data Analysts, Python/Power BI Developers


> Auto-generated from `generate_a58_3_portfolio_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.8.3` |
| **Output Filename** | `ISMS-IMP-A.5.8.3_Portfolio_Dashboard_YYYYMMDD.xlsx` |
| **Total Sheets** | 12 (12 visible) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.8 |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #305496 | 305496 | Custom |
| #B4C7E7 | B4C7E7 | Light Blue (Planned/Info) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFF00 | FFFF00 | Yellow (Warning) |

## Sheet 1: Workbook

---

## Sheet 2: Instructions

---

## Sheet 3: Project_Data

**Data Rows:** 16 (rows 1–16) | **Frozen Panes:** A{...}

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Project Name | 25 |
| B | Classification | 12 |
| C | PM | 20 |
| D | Business Owner | 20 |
| E | Phase | 15 |
| F | Compliance % | 12 |
| G | Initiation % | 10 |
| H | Planning % | 10 |
| I | Execution % | 10 |
| J | Monitoring % | 10 |
| K | Closure % | 10 |
| L | Critical Gaps | 10 |
| M | High Findings | 10 |
| N | Deploy Date | 12 |
| O | Last Assessment | 12 |
| P | Notes | 30 |

---

## Sheet 4: Executive_Summary

**Data Rows:** 50 (rows 4–53)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=(SUMPRODUCT(` |  |
| — | `=COUNTA(` | Total Projects: |
| — | `=COUNTIF(` | High Risk Projects: |
| — | `=SUM(` | Total Critical Gaps: |

---

## Sheet 5: Project_Status

### Columns

| Col | Header |
|-----|--------|
| A | Project |
| B | Classification |
| C | Phase |
| D | Compliance % |
| E | Critical Gaps |
| F | Status |
| G | Owner |
| H | Notes |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| FN | `=IF(D{row}>=0.85,\` |  |

---

## Sheet 6: Gap_Analysis

**Data Rows:** 5 (rows 1–5)

### Columns

| Col | Header |
|-----|--------|
| A | Gap Category |
| B | Description |
| C | Frequency |
| D | Impact |
| E | Recommended Action |

---

## Sheet 7: Trend_Analysis

**Data Rows:** 6 (rows 1–6)

### Columns

| Col | Header |
|-----|--------|
| A | Quarter |
| B | Total Projects |
| C | Avg Compliance % |
| D | High Risk Avg |
| E | Medium Risk Avg |
| F | Low Risk Avg |

---

## Sheet 8: Risk_Prioritization

**Data Rows:** 6 (rows 1–6)

### Columns

| Col | Header |
|-----|--------|
| A | Priority |
| B | Project Name |
| C | Classification |
| D | Compliance % |
| E | Critical Gaps |
| F | Action Required |

---

## Sheet 9: Lessons_Learned

**Data Rows:** 4 (rows 1–4)

### Columns

| Col | Header |
|-----|--------|
| A | Project |
| B | Lesson Learned |
| C | Category |
| D | Recommendation |

---

## Sheet 10: Regulatory_Compliance

**Data Rows:** 4 (rows 2–5)

### Columns

| Col | Header |
|-----|--------|
| A | Regulation |
| B | Applicable Projects |
| C | Compliance Rate |
| D | Gaps |
| E | Status |

---

## Sheet 11: Resources_Budget

**Data Rows:** 5 (rows 1–5)

### Columns

| Col | Header |
|-----|--------|
| A | Project |
| B | Security Budget (CHF) |
| C | Actual Spend (CHF) |
| D | % of Total Budget |
| E | Resource FTE |

---

## Sheet 12: Charts

---

**END OF SPECIFICATION**

---

*"A physicist is just an atom's way of looking at itself."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
