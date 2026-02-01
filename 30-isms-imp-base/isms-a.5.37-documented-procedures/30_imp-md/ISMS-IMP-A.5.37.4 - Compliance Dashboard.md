# ISMS-IMP-A.5.37.4 - Compliance Dashboard

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.4 |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.37: Documented Operating Procedures |
| **Version** | 1.0 |
| **Classification** | Internal Use |
| **Owner** | Information Security Manager |
| **Last Review** | [Date to be set] |

---

## Control Requirement

> "Operating procedures for information processing facilities should be documented and made available to personnel who need them."
>
> — ISO/IEC 27001:2022, Annex A Control 5.37

---

# PART I: USER GUIDE

## 1. Purpose

This dashboard consolidates procedure management metrics from A.5.37.1-3 workbooks into executive-ready visualisations. It provides real-time visibility into procedure documentation status, quality scores, review compliance, and gap remediation progress.

## 2. Dashboard Views

### 2.1 Executive Summary

| Metric | Description | Target |
|--------|-------------|--------|
| **Overall Compliance** | % of procedures meeting all requirements | >95% |
| **Review Currency** | % of procedures reviewed within cycle | >95% |
| **Average Quality Score** | Mean quality score across all procedures | ≥4.0 |
| **Open Gaps** | Count of unresolved procedure gaps | 0 |
| **Overdue Reviews** | Procedures past review due date | 0 |

### 2.2 Category Breakdown

| Category | Metrics Tracked |
|----------|-----------------|
| **System Operations** | Count, compliance %, quality average |
| **Security Operations** | Count, compliance %, quality average |
| **Facility Operations** | Count, compliance %, quality average |
| **Change Management** | Count, compliance %, quality average |
| **Recovery Operations** | Count, compliance %, quality average |
| **User Management** | Count, compliance %, quality average |

### 2.3 Trend Analysis

| Period View | Data Points |
|-------------|-------------|
| **Monthly** | Last 12 months rolling |
| **Quarterly** | Last 8 quarters |
| **Annual** | Year-over-year comparison |

## 3. Using This Dashboard

### Step 1: Data Refresh
- Update data links from source workbooks
- Verify calculation accuracy
- Refresh pivot tables and charts

### Step 2: Analysis
- Review executive summary metrics
- Identify categories below target
- Drill down into specific procedures

### Step 3: Reporting
- Export summary for management review
- Generate audit evidence package
- Update risk register if needed

---

# PART II: TECHNICAL SPECIFICATION

## 4. Workbook Structure

### Sheet 1: Executive_Dashboard
**Purpose:** High-level metrics and KPIs

| Cell/Range | Content | Data Source |
|------------|---------|-------------|
| B3 | Total Procedures | COUNT(Inventory) |
| B4 | Approved % | COUNTIF(Approved)/Total |
| B5 | Current % | COUNTIF(Current)/Total |
| B6 | Avg Quality Score | AVERAGE(Quality_Assessment!J:J) |
| B7 | Open Gaps | COUNTIF(Gap_Analysis!H:H,"Open") |
| B8 | Overdue Reviews | COUNTIF(Review_Schedule!H:H,"OVERDUE") |
| D3:D8 | Targets | Static values |
| F3:F8 | Status | Formula (Met/Not Met) |

**Visual Elements:**
- Gauge chart: Overall Compliance %
- Traffic light indicators per metric
- Trend sparklines (last 6 periods)

### Sheet 2: Category_Analysis
**Purpose:** Breakdown by procedure category

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Category | Text | Procedure category |
| B | Total_Count | Number | Procedures in category |
| C | Documented | Number | With documentation |
| D | Approved | Number | With approval |
| E | Current | Number | Review current |
| F | Compliance_% | Number | Overall compliance |
| G | Avg_Quality | Number | Average quality score |
| H | Open_Gaps | Number | Gaps for category |
| I | Status | Text | Traffic light status |

### Sheet 3: Review_Status
**Purpose:** Review compliance tracking

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Status | Text | OVERDUE/DUE SOON/CURRENT |
| B | Count | Number | Procedures in status |
| C | Percentage | Number | % of total |
| D | Critical_Count | Number | Critical procedures |
| E | High_Count | Number | High criticality |
| F | Medium_Count | Number | Medium criticality |
| G | Low_Count | Number | Low criticality |

**Visual Elements:**
- Stacked bar chart by criticality
- Pie chart: Status distribution
- List: Top 10 overdue procedures

### Sheet 4: Quality_Overview
**Purpose:** Quality assessment summary

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Rating | Text | Excellent/Good/Adequate/Poor |
| B | Count | Number | Procedures with rating |
| C | Percentage | Number | % of assessed |
| D | Avg_Clarity | Number | Average dimension score |
| E | Avg_Completeness | Number | Average dimension score |
| F | Avg_Accuracy | Number | Average dimension score |
| G | Avg_Usability | Number | Average dimension score |
| H | Avg_Maintainability | Number | Average dimension score |

**Visual Elements:**
- Radar chart: Dimension scores
- Bar chart: Rating distribution
- Trend line: Quality over time

### Sheet 5: Gap_Tracking
**Purpose:** Gap remediation status

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Severity | Text | Critical/High/Medium/Low |
| B | Open | Number | Open gaps |
| C | In_Progress | Number | Being addressed |
| D | Closed | Number | Resolved |
| E | Total | Number | All gaps |
| F | Closure_Rate | Number | % closed |
| G | Avg_Days_Open | Number | Average age |
| H | Overdue | Number | Past target date |

**Visual Elements:**
- Waterfall chart: Gap lifecycle
- Heat map: Severity vs Age
- Burn-down chart: Gap remediation

### Sheet 6: Change_Activity
**Purpose:** Change request metrics

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Period | Text | Month/Quarter |
| B | Submitted | Number | CRs submitted |
| C | Approved | Number | CRs approved |
| D | Rejected | Number | CRs rejected |
| E | Implemented | Number | CRs completed |
| F | Approval_Rate | Number | % approved |
| G | Avg_Cycle_Time | Number | Days to implement |
| H | Emergency_Count | Number | Emergency changes |

**Visual Elements:**
- Line chart: CR volume trend
- Bar chart: Approval vs Rejection
- KPI card: Average cycle time

### Sheet 7: Trend_History
**Purpose:** Historical trend data

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Period | Text | Assessment period |
| B | Total_Procedures | Number | Count at period |
| C | Compliance_% | Number | Overall compliance |
| D | Avg_Quality | Number | Quality score |
| E | Open_Gaps | Number | Gap count |
| F | Overdue_Reviews | Number | Overdue count |
| G | CR_Volume | Number | Change requests |
| H | Notes | Text | Period notes |

### Sheet 8: Data_Sources
**Purpose:** Links to source workbooks

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Source_Workbook | Text | Source file name |
| B | Sheet | Text | Source sheet |
| C | Data_Range | Text | Range reference |
| D | Last_Updated | Date | Last refresh |
| E | Refresh_Method | Text | Manual/Auto |
| F | Status | Text | Connected/Error |

### Sheet 9: Instructions
**Purpose:** Dashboard user guide

Static content including:
- Data refresh procedures
- Metric definitions
- Interpretation guidance
- Export instructions

## 5. Key Formulas

### Overall Compliance Score
```excel
=(COUNTIF(Inventory!K:K,"Approved")/COUNTA(Inventory!A:A))*0.25+
 (COUNTIF(Review!H:H,"CURRENT")/COUNTA(Review!A:A))*0.25+
 (AVERAGEIF(Quality!J:J,">0")/5)*0.25+
 ((1-COUNTIF(Gap!H:H,"Open")/COUNTA(Gap!A:A)))*0.25
```

### Category Compliance
```excel
=SUMPRODUCT((Inventory!C:C=A2)*(Inventory!K:K="Approved")*(Review!H:H<>"OVERDUE"))/
 COUNTIF(Inventory!C:C,A2)*100
```

### Quality Trend Direction
```excel
=IF(H2>H3,"↑ Improving",IF(H2<H3,"↓ Declining","→ Stable"))
```

### Gap Ageing
```excel
=AVERAGEIFS(TODAY()-Gap!E:E,Gap!H:H,"Open")
```

### Review Currency Rate
```excel
=COUNTIF(Review!H:H,"CURRENT")/COUNTA(Review!A:A)*100
```

## 6. Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| Compliance % | ≥95% | Green fill |
| Compliance % | 80-94% | Yellow fill |
| Compliance % | <80% | Red fill |
| Quality Score | ≥4.0 | Green fill |
| Quality Score | 3.0-3.9 | Yellow fill |
| Quality Score | <3.0 | Red fill |
| Gap Count | 0 | Green fill |
| Gap Count | 1-5 | Yellow fill |
| Gap Count | >5 | Red fill |
| Trend | ↑ | Green text |
| Trend | ↓ | Red text |

## 7. Chart Specifications

### Compliance Gauge (Executive Dashboard)
- Type: Doughnut chart (semi-circle)
- Data: Compliance %, 100-Compliance %
- Colours: Green/Grey
- Centre label: Percentage value

### Category Performance (Category Analysis)
- Type: Clustered bar chart
- X-axis: Categories
- Y-axis: Compliance %
- Reference line: 95% target

### Quality Radar (Quality Overview)
- Type: Radar chart
- Axes: 5 quality dimensions
- Series: Current period, Previous period
- Scale: 0-5

### Gap Burn-down (Gap Tracking)
- Type: Line chart with area
- X-axis: Time periods
- Y-axis: Open gap count
- Trend line: Linear forecast

## 8. Data Refresh Process

### Manual Refresh
1. Open all source workbooks
2. Update external data links
3. Refresh all pivot tables
4. Verify calculation accuracy
5. Update Last_Refreshed timestamp

### Automated Refresh (if implemented)
- Schedule: Daily at 06:00
- Trigger: Source workbook save
- Notification: Email on error

## 9. Integration Points

### Upstream Dependencies
- A.5.37.1 Procedure Inventory Assessment
- A.5.37.2 Procedure Quality Assessment
- A.5.37.3 Procedure Review and Update Tracking

### Downstream Consumers
- Management review reports
- Audit evidence packages
- Risk register updates
- ISMS performance metrics

## 10. Output Reports

| Report | Frequency | Audience |
|--------|-----------|----------|
| Executive Summary | Monthly | CISO, Management |
| Category Detail | Quarterly | Department Heads |
| Gap Status | Weekly | ISM, Process Owners |
| Audit Package | On-demand | Auditors |

## 11. Access Control

| Role | Access Level |
|------|--------------|
| CISO | Full access, export |
| ISM | Full access, edit |
| Department Heads | View category data |
| Auditors | Read-only, export |
| Process Owners | View assigned procedures |

---

**END OF SPECIFICATION**

---

*"You can't manage what you can't measure."*
— Peter Drucker

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-02-01 -->
