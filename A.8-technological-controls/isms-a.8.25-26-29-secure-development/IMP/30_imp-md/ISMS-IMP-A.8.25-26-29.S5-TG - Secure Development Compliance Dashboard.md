**ISMS-IMP-A.8.25-26-29.S5-TG - Secure Development Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.25: Secure Development Life Cycle

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.25-26-29-S5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Secure Development Compliance Dashboard (A.8.25, A.8.26, A.8.29 Combined) |
| **Related Policy** | ISMS-POL-A.8.25-26-29 All Sections |
| **Purpose** | Executive dashboard aggregating security requirements (A.8.26), SDLC security activities (A.8.25), security testing (A.8.29), and vulnerability remediation metrics into unified compliance view |
| **Target Audience** | CISO, Security Leadership, Development Executives, Auditors, Compliance Officers |
| **Assessment Type** | Portfolio-level or application-level executive summary |
| **Review Cycle** | Quarterly for portfolio view, Monthly for critical applications |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial dashboard specification | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.25-26-29.S5-UG.

---

# Technical Specification

---

**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

# Workbook Overview

## Workbook Metadata

**Filename Format:** `ISMS-A825-26-29-Dashboard-[Portfolio or APP-ID]-[YYYYMMDD].xlsx`

**Examples:**

- `ISMS-A825-26-29-Dashboard-Portfolio-20260123.xlsx` (portfolio view)
- `ISMS-A825-26-29-Dashboard-APP-CUST-20260123.xlsx` (application view)

**Total Sheets:** 8

**Excel Version:** Excel 2016+ (Office 365 recommended)

**File Size Estimate:** 200KB - 1MB

**Python Script:** `generate_a825_26_29_5_compliance_dashboard.py`

## Workbook Structure Summary

| Sheet # | Sheet Name | Purpose | Data Source | Complexity |
|---------|------------|---------|-------------|------------|
| 1 | Executive Summary | One-page overview | IMP-S1,S2,S3,S4 | High |
| 2 | Control Compliance | A.8.25/26/29 scores | IMP-S1,S2,S3,S4 | Medium |
| 3 | Maturity Assessment | Maturity level 1-5 | Calculated from scores | Medium |
| 4 | Trend Analysis | Quarterly progress | Historical dashboards | Low |
| 5 | Recommendations | Action plan | Gap analysis | Low |

---

# Common Structure Elements

## Standard Colors

**Headers:** `RGB(0, 51, 102)` Dark Blue, White text, 14pt Bold
**Metrics (Large):** `RGB(68, 114, 196)` Blue, 24pt Bold (for Executive Summary scores)
**Input Cells:** `RGB(255, 255, 204)` Light Yellow
**Auto-Calculated:** `RGB(217, 217, 217)` Light Gray

**Status Colors:**

- ✅ Compliant (≥70%): `RGB(198, 239, 206)` Light Green
- ⚠️ Partial (50-69%): `RGB(255, 235, 156)` Light Yellow
- ❌ Non-Compliant (<50%): `RGB(255, 199, 206)` Light Red

**Maturity Levels:**

- Level 5: `RGB(0, 176, 80)` Dark Green
- Level 4: `RGB(146, 208, 80)` Light Green
- Level 3: `RGB(255, 192, 0)` Orange
- Level 2: `RGB(255, 153, 0)` Dark Orange
- Level 1: `RGB(192, 0, 0)` Red

## Data Validation

**Status Dropdown:**
```excel
List: ✅ Compliant,⚠️ Partial,❌ Non-Compliant
```

**Trend Dropdown:**
```excel
List: ↑ Improving,→ Stable,↓ Degrading
```

**Priority Dropdown:**
```excel
List: P1 (Immediate),P2 (High),P3 (Medium),P4 (Low)
```

**Effort Dropdown:**
```excel
List: Low,Medium,High
```

---

# Sheet 1: Executive Summary

## Structure

**This sheet should fit on ONE PAGE (portrait orientation)**

### Section A: Dashboard Header (Rows 1-5)

**Merged Cells:** A1:G5 (Large header block)

| Row | Content | Format |
|-----|---------|--------|
| 1-2 | "SECURE DEVELOPMENT COMPLIANCE DASHBOARD" | 18pt Bold, Centered |
| 3 | Assessment Date: [Date] | 12pt |
| 4 | Reporting Period: [Period] | 12pt |
| 5 | Scope: [Portfolio/Application] | 12pt |

### Section B: Overall Compliance Score (Rows 7-12)

**Merged Cells:** A7:D12 (Large score display)

**Content:**
```
Secure Development Compliance
        85%
   Level 3: Defined
```

**Format:**

- "85%" → 36pt Bold, Blue
- "Level 3: Defined" → 14pt Bold

**Formula for Overall Score (Cell B9):**
```excel
=AVERAGE(Sheet2!B10, Sheet2!B20, Sheet2!B30, Sheet2!B40)
```
*Average of A.8.26, A.8.25, A.8.29, Remediation scores from Sheet 2*

**Formula for Maturity Level (Cell B11):**
```excel
=IF(B9>=95,"Level 5: Optimizing",IF(B9>=85,"Level 4: Quantitatively Managed",IF(B9>=70,"Level 3: Defined",IF(B9>=50,"Level 2: Managed","Level 1: Initial"))))
```

### Section C: Control Compliance Summary (Rows 7-12, Columns F-G)

**Table:**

| Control | Score | Status |
|---------|-------|--------|
| A.8.26 - Security Requirements | =Sheet2!B10 | Formula |
| A.8.25 - Secure Development Lifecycle | =Sheet2!B20 | Formula |
| A.8.29 - Security Testing | =Sheet2!B30 | Formula |
| Vulnerability Remediation | =Sheet2!B40 | Formula |

**Status Formula (Cell G8):**
```excel
=IF(F8>=70,"✅ Compliant",IF(F8>=50,"⚠️ Partial","❌ Non-Compliant"))
```

### Section D: Key Metrics At-a-Glance (Rows 14-22)

**Table:**

| Metric | Value | Trend |
|--------|-------|-------|
| Applications Assessed | User input | - |
| High-Risk Applications | User input | - |
| Security Requirements Coverage | =Sheet2!B6 | User selects |
| SDLC Security Maturity | =Sheet2!B16 | User selects |
| Security Testing Coverage | =Sheet2!B26 | User selects |
| Open Critical Vulnerabilities | User input | User selects |
| SLA Compliance Rate | =Sheet2!B36 | User selects |

### Section E: Critical Gaps (Rows 24-30)

**Table:** User inputs top 3 gaps manually

| # | Gap | Impact | Priority |
|---|-----|--------|----------|
| 1 | [Description] | [Impact] | Dropdown: Priority |
| 2 | [Description] | [Impact] | Dropdown: Priority |
| 3 | [Description] | [Impact] | Dropdown: Priority |

### Section F: Executive Recommendation (Rows 32-35)

**Merged Cells:** A32:G35

**Content:** User writes 2-3 sentence summary recommendation

---

# Sheet 2: Control Compliance

## Structure

**4 Main Sections (one per control/metric):**

### Section A: ISO 27001:2022 Control A.8.26 - Application Security Requirements (Rows 5-12)

**Table:**

| Row | Sub-Metric | Score Source | Weight | Weighted Score |
|-----|-----------|--------------|--------|----------------|
| 6 | Security Requirements Specification | User input from IMP-S1 | 30% | =B6*C6 |
| 7 | Threat Modeling Completion | User input from IMP-S1 | 25% | =B7*C7 |
| 8 | Security Architecture Review | User input from IMP-S1 | 25% | =B8*C8 |
| 9 | Requirements Traceability | User input from IMP-S1 | 20% | =B9*C9 |
| 10 | **Overall A.8.26 Score** | **=SUM(D6:D9)** | **100%** | - |

**Gap Summary (Rows 11-12):** User documents gap counts

### Section B: ISO 27001:2022 Control A.8.25 - Secure Development Lifecycle (Rows 14-22)

**Table:**

| Row | Sub-Metric | Score Source | Weight | Weighted Score |
|-----|-----------|--------------|--------|----------------|
| 15 | SDLC Phase Security Activities | User input from IMP-S2 | 25% | =B15*C15 |
| 16 | Secure Coding Standards | User input from IMP-S2 | 20% | =B16*C16 |
| 17 | Code Review Execution | User input from IMP-S2 | 20% | =B17*C17 |
| 18 | Security Tools Deployment | User input from IMP-S2 | 20% | =B18*C18 |
| 19 | Developer Training | User input from IMP-S2 | 15% | =B19*C19 |
| 20 | **Overall A.8.25 Score** | **=SUM(D15:D19)** | **100%** | - |

### Section C: ISO 27001:2022 Control A.8.29 - Security Testing (Rows 24-32)

**Table:**

| Row | Sub-Metric | Score Source | Weight | Weighted Score |
|-----|-----------|--------------|--------|----------------|
| 25 | SAST Execution Coverage | User input from IMP-S3 | 25% | =B25*C25 |
| 26 | DAST Execution Coverage | User input from IMP-S3 | 25% | =B26*C26 |
| 27 | SCA Execution Coverage | User input from IMP-S3 | 20% | =B27*C27 |
| 28 | Penetration Testing | User input from IMP-S3 | 20% | =B28*C28 |
| 29 | Security Acceptance Testing | User input from IMP-S3 | 10% | =B29*C29 |
| 30 | **Overall A.8.29 Score** | **=SUM(D25:D29)** | **100%** | - |

### Section D: Vulnerability Remediation (Rows 34-42)

**Table:**

| Row | Sub-Metric | Score Source | Weight | Weighted Score |
|-----|-----------|--------------|--------|----------------|
| 35 | SLA Compliance Rate | User input from IMP-S4 | 40% | =B35*C35 |
| 36 | Overdue Vulnerabilities (inverse) | User input from IMP-S4 | 30% | =B36*C36 |
| 37 | Avg Remediation Time vs SLA | User input from IMP-S4 | 20% | =B37*C37 |
| 38 | Technical Debt Management | User input from IMP-S4 | 10% | =B38*C38 |
| 40 | **Overall Remediation Score** | **=SUM(D35:D38)** | **100%** | - |

## Conditional Formatting

**Cells B10, B20, B30, B40** (Overall Scores):

- If ≥70% → Green background
- If 50-69% → Yellow background
- If <50% → Red background

---

# Sheet 3: Maturity Assessment

## Structure

**4 Maturity Dimensions (one per control/metric):**

### Dimension A: Requirements Management Maturity (Rows 5-12)

**Table:**

| Level | Criteria | Score Range | Status |
|-------|----------|-------------|--------|
| Level 5 | Continuous improvement | ≥95% | Formula |
| Level 4 | Requirements validated | 85-94% | Formula |
| Level 3 | Comprehensive requirements | 70-84% | Formula |
| Level 2 | Basic requirements | 50-69% | Formula |
| Level 1 | No formal requirements | <50% | Formula |

**Current Level (Row 12):** Formula based on Sheet2!B10

**Formula for Status (Cell D6):**
```excel
=IF(AND(Sheet2!$B$10>=95),"← Current","")
```
*Repeat for each level with appropriate ranges*

**Current Level Formula (Cell B12):**
```excel
=IF(Sheet2!B10>=95,5,IF(Sheet2!B10>=85,4,IF(Sheet2!B10>=70,3,IF(Sheet2!B10>=50,2,1))))
```

### Dimension B: SDLC Security Maturity (Rows 14-21)

*Same structure as Dimension A, references Sheet2!B20*

### Dimension C: Security Testing Maturity (Rows 23-30)

*Same structure, references Sheet2!B30*

### Dimension D: Vulnerability Management Maturity (Rows 32-39)

*Same structure, references Sheet2!B40*

### Overall Maturity Level (Rows 41-45)

**Formula (Cell B42):**
```excel
=ROUND(AVERAGE(B12,B21,B30,B39),0)
```
*Average of all dimension levels, rounded to integer*

**Display (Cell B43):**
```excel
="Level " & B42 & ": " & IF(B42=5,"Optimizing",IF(B42=4,"Quantitatively Managed",IF(B42=3,"Defined",IF(B42=2,"Managed","Initial"))))
```

## Conditional Formatting

**Cell B42** (Overall Maturity Level):

- If 5 → Dark Green background
- If 4 → Light Green background
- If 3 → Orange background
- If 2 → Dark Orange background
- If 1 → Red background

---

# Sheet 4: Trend Analysis

## Structure

**Quarterly Trend Table (Rows 5-15):**

**Columns:** A (Metric), B (Q1), C (Q2), D (Q3), E (Q4), F (Trend)

**Rows:**

| Metric | Q1 | Q2 | Q3 | Q4 | Trend |
|--------|----|----|----|----|-------|
| Overall Compliance | User input | User input | User input | User input | Formula |
| A.8.26 Score | User input | User input | User input | User input | Formula |
| A.8.25 Score | User input | User input | User input | User input | Formula |
| A.8.29 Score | User input | User input | User input | User input | Formula |
| Remediation Score | User input | User input | User input | User input | Formula |
| Open Critical Vulns | User input | User input | User input | User input | Formula |
| SLA Compliance | User input | User input | User input | User input | Formula |

**Trend Formula (Cell F6):**
```excel
=IF(E6>D6,"↑ Improving",IF(E6=D6,"→ Stable","↓ Degrading"))
```

**Year-over-Year Comparison Table (Rows 17-25):**

| Metric | Q4 Last Year | Q4 This Year | Change |
|--------|--------------|--------------|--------|
| Overall Compliance | User input | User input | =C18-B18 |
| Maturity Level | User input | User input | =C19-B19 |
| Critical Vulns | User input | User input | =C20-B20 |

**Line Chart (Rows 27-45):**

- **Chart Type:** Line chart
- **Data Range:** B5:E12 (quarterly metrics)
- **X-Axis:** Quarters
- **Y-Axis:** Scores (%)

---

# Sheet 5: Recommendations

## Structure

**Recommendations Table (Rows 5-25):**

**Columns:**

| Col | Column Name | Width | Input Type |
|-----|-------------|-------|------------|
| A | # | 5 | Auto-number (1,2,3...) |
| B | Recommendation | 40 | Text |
| C | Current State | 30 | Text |
| D | Target State | 30 | Text |
| E | Priority | 15 | Dropdown: Priority |
| F | Effort | 12 | Dropdown: Effort |
| G | Owner | 20 | Text |
| H | Target Date | 15 | Date |

**Auto-numbering Formula (Cell A6):**
```excel
=ROW()-5
```
*Adjusts automatically when rows inserted*

**Quick Wins Section (Rows 27-32):**
User manually documents 3-5 quick wins (low effort, high impact)

**Strategic Initiatives Section (Rows 34-39):**
User manually documents 3-5 strategic initiatives (high effort, high impact)

## Conditional Formatting

**Column E (Priority):**

- "P1 (Immediate)" → Red background
- "P2 (High)" → Orange background
- "P3 (Medium)" → Yellow background
- "P4 (Low)" → Green background

**Column H (Target Date):**

- If past due (< TODAY()) → Red background
- If due soon (< TODAY()+30) → Yellow background

---

# Python Script Integration Notes

## Script Name
`generate_a825_26_29_5_compliance_dashboard.py`

## Key Functions

1. **create_workbook()**: Initialize 8 sheets
2. **populate_executive_summary()**: Create one-page summary with large fonts
3. **add_formulas()**: Add all cross-sheet references and calculations
4. **add_conditional_formatting()**: Status colors, maturity levels, trend indicators
5. **create_charts()**: Add trend line chart to Sheet 4
6. **protect_sheets()**: Lock all sheets

## Critical Notes

**Cross-Sheet References:**

- Executive Summary pulls from Control Compliance sheet
- Control Compliance pulls from user input (IMP-S1,S2,S3,S4 data)
- Maturity Assessment pulls from Control Compliance
- Verify all references work when sheets reordered

**Large Fonts for Executive Summary:**

- Overall score: 36pt
- Maturity level: 14pt
- Keep Executive Summary to ONE PAGE

**Trend Chart:**

- Auto-updates when quarterly data added
- Use professional color scheme
- Show data labels

---

# Quality Assurance Checklist

- [ ] All 5 sheets present
- [ ] Executive Summary fits on one page
- [ ] All cross-sheet formulas work
- [ ] Maturity level calculation correct
- [ ] Trend chart displays properly
- [ ] Conditional formatting applies correctly
- [ ] No #REF!, #VALUE!, #DIV/0! errors
- [ ] Test with sample data from all 4 IMP workbooks

---

**END OF SPECIFICATION**

---

*"The best protection is a complete understanding of the system you are trying to protect."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
