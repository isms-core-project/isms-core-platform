**ISMS-IMP-A.7.12-13.S4-TG - Infrastructure Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.7.12 & A.7.13: Cabling Security and Equipment Maintenance

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.12-13.S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Compliance Dashboard - Cabling Security and Equipment Maintenance |
| **Related Policy** | ISMS-POL-A.7.12-13 (Full Policy) |
| **Purpose** | Provide consolidated compliance view across cabling security and equipment maintenance domains |
| **Target Audience** | CISO, IT Management, Compliance Officers, Internal Audit, External Auditors |
| **Assessment Type** | Executive Summary and Compliance Dashboard |
| **Review Cycle** | Quarterly or On-Demand |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Infrastructure Compliance Dashboard | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.12-13.S4-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.12-13.S4_Compliance_Dashboard_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a712_4_compliance_dashboard.py)

**Sheet Count:** 6 worksheets

**Styling:** Navy blue headers, colour-coded status indicators, charts

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type |
|---------|------------|---------|------|
| 1 | Executive Summary | High-level compliance overview | Dashboard |
| 2 | Cabling Security | A.7.12 domain compliance | Formula-driven |
| 3 | Equipment Maintenance | A.7.13 domain compliance | Formula-driven |
| 4 | Gap Register | All gaps with remediation status | Data Entry |
| 5 | Trend Analysis | Historical compliance data | Data Entry + Charts |
| 6 | Audit Evidence | Evidence pack summary | Reference |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Executive Summary

**Purpose:** One-page executive view of infrastructure compliance

**Structure:**

**Section A: Overall Compliance (Rows 1-10)**

| Row | Content | Style |
|-----|---------|-------|
| 1 | Header: "A.7.12-13 Infrastructure Compliance Dashboard" | Navy blue |
| 3 | Assessment Period | Input |
| 5 | Overall Compliance Score | Large number, colour-coded |
| 6 | Status: Excellent/Good/Acceptable/Non-Compliant | Text |
| 8 | Cabling Security Score (40%) | Medium number |
| 9 | Equipment Maintenance Score (60%) | Medium number |

**Section B: Domain Summary (Rows 12-25)**

| Row | Content |
|-----|---------|
| 12 | Header: "Domain Breakdown" |
| 14-17 | Cabling: Pathways, Protection, Access, Documentation |
| 19-22 | Maintenance: Schedule, Programme, Personnel, Security |

**Section C: Key Indicators (Rows 27-40)**

| Row | Content |
|-----|---------|
| 27 | Header: "Key Risk Indicators" |
| 29 | Critical Overdue Count |
| 30 | Unprotected Cabling % |
| 31 | Remote Access Gaps |
| 33 | Header: "Gap Summary" |
| 34 | Open Gaps (Critical/High/Medium/Low) |
| 36 | Oldest Open Gap (days) |

**Section D: Charts (Columns F-L)**

- Compliance gauge chart
- Domain comparison bar chart
- 6-month trend line chart

### Sheet 2: Cabling Security

**Purpose:** Detailed A.7.12 compliance breakdown

**Structure:**

**Section A: Score Summary (Rows 1-15)**

| Metric | Weight | Score | Status |
|--------|--------|-------|--------|
| Cable Pathways | 30% | Formula | Colour |
| Physical Protection | 25% | Formula | Colour |
| Access Controls | 25% | Formula | Colour |
| Documentation | 20% | Formula | Colour |
| **Domain Score** | 100% | **Weighted** | **Colour** |

**Section B: Detailed Metrics (Rows 17-40)**

- Pathways: Total, Compliant, Partial, Non-Compliant
- Protection: Total areas, Protected, Partially protected, Unprotected
- Access: Total locations, Secured, Partial, Unsecured
- Documentation: Total docs, Current, Outdated, Missing

**Section C: Gap List (Rows 42+)**

- List of non-compliant items from S1

**External Links:**

```excel
=COUNTIF('[ISMS-IMP-A.7.12-13.S1_Cabling_Security.xlsx]Cable Pathways'!L:L,"✅ Compliant")
```

### Sheet 3: Equipment Maintenance

**Purpose:** Detailed A.7.13 compliance breakdown

**Structure:**

**Section A: Score Summary**

| Metric | Weight | Score | Status |
|--------|--------|-------|--------|
| Schedule Compliance | 40% | Formula | Colour |
| Maintenance Programme | 30% | Formula | Colour |
| Personnel Verification | 15% | Formula | Colour |
| Security Controls | 15% | Formula | Colour |
| **Domain Score** | 100% | **Weighted** | **Colour** |

**Section B: Schedule Metrics**

- Total equipment in programme
- Current: X (X%)
- Due Soon: X (X%)
- Overdue: X (X%)
- Critical Overdue: X

**Section C: Overdue Detail**

- List of overdue equipment from S3
- Days overdue
- Escalation status

**External Links:**

```excel
=COUNTIF('[ISMS-IMP-A.7.12-13.S3_Maintenance_Schedule.xlsx]Equipment Schedule'!K:K,"✅ Current")
```

### Sheet 4: Gap Register

**Purpose:** Central gap tracking and remediation management

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Gap ID | Text | 12 | Auto-generate |
| B | Source | Dropdown | 15 | S1, S2, S3 |
| C | Description | Text | 50 | None |
| D | Priority | Dropdown | 12 | Critical, High, Medium, Low |
| E | Owner | Text | 20 | None |
| F | Identified Date | Date | 15 | Date |
| G | Target Date | Date | 15 | Date |
| H | Status | Dropdown | 15 | Open, In Progress, Closed, Accepted |
| I | Remediation Plan | Text | 50 | None |
| J | Evidence | Text | 30 | None |
| K | Closure Date | Date | 15 | Date |
| L | Notes | Text | 40 | None |

**Conditional Formatting:**

- Priority Critical: Red background
- Priority High: Orange background
- Status Overdue (Target Date < Today AND Status not Closed): Red text

### Sheet 5: Trend Analysis

**Purpose:** Track compliance trends over time

**Structure:**

**Section A: Monthly Data Entry (Rows 1-20)**

| Month | Overall % | Cabling % | Maintenance % | Open Gaps | Notes |
|-------|-----------|-----------|---------------|-----------|-------|
| Jan 2026 | Input | Input | Input | Input | Input |
| Feb 2026 | Input | Input | Input | Input | Input |
| ... | ... | ... | ... | ... | ... |

**Section B: Trend Charts (Rows 22+)**

- Line chart: Compliance trend (Overall, Cabling, Maintenance)
- Bar chart: Gap count trend

### Sheet 6: Audit Evidence

**Purpose:** Summary of evidence for audit

**Structure:**

**Assessment Evidence:**

| Assessment | File Name | Location | Last Updated | Status |
|------------|-----------|----------|--------------|--------|
| S1 - Cabling | ISMS-IMP-A.7.12-13.S1_*.xlsx | [Path] | [Date] | Current/Outdated |
| S2 - Maintenance | ISMS-IMP-A.7.12-13.S2_*.xlsx | [Path] | [Date] | Current/Outdated |
| S3 - Schedule | ISMS-IMP-A.7.12-13.S3_*.xlsx | [Path] | [Date] | Current/Outdated |

**Supporting Evidence:**

- Evidence registers from S1, S2, S3
- Gap closure evidence
- Approval documentation

---

## External Workbook Links

### Link Configuration

**Source Files Must Be Named:**

- ISMS-IMP-A.7.12-13.S1_Cabling_Security.xlsx
- ISMS-IMP-A.7.12-13.S2_Equipment_Maintenance.xlsx
- ISMS-IMP-A.7.12-13.S3_Maintenance_Schedule.xlsx

**Location:**

All files should be in same directory as dashboard for links to work.

**Link Formulas:**

```excel
' Cabling Pathways Compliant
=[ISMS-IMP-A.7.12-13.S1_Cabling_Security.xlsx]'Summary Dashboard'!B5

' Maintenance Schedule Compliance
=[ISMS-IMP-A.7.12-13.S3_Maintenance_Schedule.xlsx]Dashboard!B3

' Equipment Overdue Count
=[ISMS-IMP-A.7.12-13.S3_Maintenance_Schedule.xlsx]Dashboard!B7
```

**Link Update:**

- Open dashboard, click "Update Links" when prompted
- Or: Data → Edit Links → Update Values

---

## Cell Styling Reference

### Colour Palette

**Headers:**

- Primary: #003366 (Navy blue)
- Section: #4472C4 (Medium blue)

**Status Colours:**

- Excellent (≥90%): #C6EFCE (Light green)
- Good (75-89%): #FFEB9C (Light amber)
- Acceptable (60-74%): #FFD966 (Yellow)
- Non-Compliant (<60%): #FFC7CE (Light red)

**Priority Colours:**

- Critical: #FFC7CE (Light red)
- High: #FFE4B5 (Light orange)
- Medium: #FFFFCC (Light yellow)
- Low: #FFFFFF (White)

---

## Integration Points

### Integration with Source Assessments

| Dashboard Element | Source | Link Type |
|-------------------|--------|-----------|
| Cabling Scores | S1 Sheets 2-5 | External formula |
| Maintenance Scores | S2 Sheets 2-6 | External formula |
| Schedule Compliance | S3 Sheet 2, 5 | External formula |
| Gap Details | S1, S2, S3 Gap lists | Manual consolidation |

### Integration with ISMS

**Feeds Into:**

- Management Review reporting
- Internal Audit planning
- Risk Register (high-priority gaps)
- Corrective Action Register

**Related Controls:**

- A.7.4-5-11 (Physical Infrastructure) - Related physical controls
- A.5.9 (Asset Management) - Equipment inventory
- A.8.32 (Change Management) - Infrastructure changes

---

## Formula Reference

### Overall Compliance Calculation

**Overall Score Formula:**

```excel
=B8*0.4+B9*0.6
```
Where B8 = Cabling Security Score, B9 = Equipment Maintenance Score

**Status Determination:**

```excel
=IF(B5>=90,"Excellent",IF(B5>=75,"Good",IF(B5>=60,"Acceptable","Non-Compliant")))
```

### Cabling Security Domain Formulas

**Domain Score:**

```excel
=(PathwaysScore*0.3)+(ProtectionScore*0.25)+(AccessScore*0.25)+(DocumentationScore*0.2)
```

**Sub-Domain Scores:**

```excel
' Pathways Compliance
=IFERROR(COUNTIF('[S1]Cable Pathways'!L:L,"Compliant")/COUNTA('[S1]Cable Pathways'!A:A)*100,0)

' Protection Score
=IFERROR(COUNTIF('[S1]Physical Protection'!H:H,"Protected")/COUNTA('[S1]Physical Protection'!A:A)*100,0)

' Access Control Score
=IFERROR(COUNTIF('[S1]Access Controls'!G:G,"Secured")/COUNTA('[S1]Access Controls'!A:A)*100,0)

' Documentation Score
=IFERROR(COUNTIF('[S1]Documentation'!E:E,"Current")/COUNTA('[S1]Documentation'!A:A)*100,0)
```

### Equipment Maintenance Domain Formulas

**Domain Score:**

```excel
=(ScheduleScore*0.4)+(ProgrammeScore*0.3)+(PersonnelScore*0.15)+(SecurityScore*0.15)
```

**Sub-Domain Scores:**

```excel
' Schedule Compliance
=IFERROR('[S3]Dashboard'!B3,0)

' Programme Coverage
=IFERROR(COUNTIF('[S2]Equipment Inventory'!F:F,"In Programme")/COUNTA('[S2]Equipment Inventory'!A:A)*100,0)

' Personnel Verification
=IFERROR(COUNTIF('[S2]Personnel'!E:E,"Verified")/COUNTA('[S2]Personnel'!A:A)*100,0)

' Security Controls
=IFERROR(COUNTIF('[S2]Security Controls'!G:G,"Compliant")/COUNTA('[S2]Security Controls'!A:A)*100,0)
```

### Gap Register Formulas

**Gap Count by Priority:**

```excel
' Critical Gaps
=COUNTIF('Gap Register'!D:D,"Critical")

' High Gaps
=COUNTIF('Gap Register'!D:D,"High")

' Open Gaps Total
=COUNTIFS('Gap Register'!H:H,"<>Closed",'Gap Register'!H:H,"<>Accepted")
```

**Oldest Open Gap:**

```excel
=IFERROR(TODAY()-MIN(IF('Gap Register'!H:H<>"Closed",'Gap Register'!F:F)),0)
```
(Enter as array formula with Ctrl+Shift+Enter)

**Overdue Gap Highlighting:**

```excel
=AND(G2<TODAY(),H2<>"Closed",H2<>"Accepted")
```

### Trend Analysis Formulas

**Month-over-Month Change:**

```excel
=B3-B2
```

**Trend Direction:**

```excel
=IF(B3>B2,"↑",IF(B3<B2,"↓","→"))
```

**Rolling 3-Month Average:**

```excel
=AVERAGE(B2:B4)
```

---

## Conditional Formatting Specifications

### Executive Summary Score Colours

**Overall Score (Cell B5):**

| Score Range | Background | Font Colour |
|-------------|------------|-------------|
| ≥90 | #C6EFCE (Light green) | #006100 (Dark green) |
| 75-89 | #FFEB9C (Light amber) | #9C6500 (Dark amber) |
| 60-74 | #FFD966 (Yellow) | #9C5700 (Brown) |
| <60 | #FFC7CE (Light red) | #9C0006 (Dark red) |

**Domain Scores (Cells B8, B9):**

Apply same colour rules as Overall Score.

### Gap Register Formatting

**Priority Column (D):**

| Priority | Background |
|----------|------------|
| Critical | #FFC7CE (Light red) |
| High | #FFE4B5 (Light orange) |
| Medium | #FFFFCC (Light yellow) |
| Low | #FFFFFF (White) |

**Overdue Gap Row:**

```
Condition: =AND($G2<TODAY(),$H2<>"Closed",$H2<>"Accepted")
Format: Red italic font, light red background
```

### Trend Chart Formatting

**Compliance Line Chart:**

| Series | Colour | Line Width |
|--------|--------|------------|
| Overall | #003366 (Navy) | 2.5pt |
| Cabling | #4472C4 (Blue) | 1.5pt |
| Maintenance | #70AD47 (Green) | 1.5pt |

**Target Line:**

| Element | Colour | Style |
|---------|--------|-------|
| 90% Target | #FF0000 (Red) | Dashed |

---

## Data Validation Rules

### Gap Register Validations

**Source Field (Column B):**

```
Type: List
Source: S1,S2,S3
Allow blank: No
Error: Source must be S1, S2, or S3
```

**Priority Field (Column D):**

```
Type: List
Source: Critical,High,Medium,Low
Allow blank: No
Error: Select valid priority level
```

**Status Field (Column H):**

```
Type: List
Source: Open,In Progress,Closed,Accepted
Allow blank: No
Error: Select valid status
```

**Date Fields (Columns F, G, K):**

```
Type: Date
Operator: Greater than or equal to
Formula: =DATE(2020,1,1)
Error: Enter valid date in DD.MM.YYYY format
```

### Trend Analysis Validations

**Compliance Percentage Fields:**

```
Type: Decimal
Operator: Between
Minimum: 0
Maximum: 100
Error: Compliance must be between 0 and 100%
```

**Gap Count Fields:**

```
Type: Whole number
Operator: Greater than or equal to
Formula: 0
Error: Gap count must be zero or positive
```

---

## Print Settings

### Executive Summary Print Area

- Range: A1:L45
- Orientation: Landscape
- Fit to: 1 page wide by 1 page tall
- Margins: Normal
- Include gridlines: No
- Include headers: Yes (page numbers)

### Gap Register Print Area

- Range: A1:L (all rows with data)
- Orientation: Landscape
- Fit to: 1 page wide
- Repeat rows at top: Row 1 (headers)
- Include gridlines: Yes

### Trend Analysis Print Area

- Range: A1:F25 (data) + Charts
- Orientation: Portrait
- Fit to: 1 page wide by 2 pages tall
- Include charts: Yes

---

## Error Handling

### External Link Errors

**When Source Files Not Found:**

- Formulas display #REF! error
- Status shows "Link Error" text via IFERROR wrapper
- Manual intervention required to reconnect links

**IFERROR Wrapper Pattern:**

```excel
=IFERROR('[S1]Sheet'!Cell,"Link Error - Check Source File")
```

### Division by Zero Prevention

**All Percentage Calculations:**

```excel
=IFERROR(numerator/denominator*100,0)
```
Returns 0 if denominator is zero.

### Missing Data Handling

**When Source Data Not Available:**

- Use "N/A" text for display
- Exclude from calculations using IFERROR
- Flag in Notes for investigation

---

**END OF SPECIFICATION**

---

*"You cannot improve what you cannot measure."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
