**ISMS-IMP-A.5.35-36.S4-TG - Compliance and Review Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.35-36

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.35-36.S4-TG |
| **Title** | Compliance and Review Dashboard |
| **Control Reference** | ISO/IEC 27001:2022 A.5.35-36 |
| **Control Name** | Compliance and Review |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

# Technical Specification

### Workbook Architecture

**File Details**:

- Filename: `ISMS-IMP-A.5.35-36.S4_Compliance_and_Review_Dashboard_YYYYMMDD.xlsx`
- Format: Microsoft Excel (.xlsx)
- Sheets: 8

### Sheet Specifications

#### Executive_Summary Sheet

**KPI Boxes** (merged cells for visual impact):
- Overall ISMS Status (cells A3:B5)
- Compliance Score (cells D3:E5)
- Open Critical Findings (cells G3:H5)

**Key Metrics Table**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Metric | 35 | Pre-populated metrics |
| B | Value | 14 | User input |
| C | Target | 14 | Pre-populated targets |
| D | Status | 12 | Data validation |
| E | Trend | 12 | Data validation |

**Key Messages Table**:

| Column | Header | Width |
|--------|--------|-------|
| A-C | Message | 60 (merged) |
| D | Priority | 14 |
| E | Owner | 20 |
| F | Action Required | 14 |

#### Review_Status Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Review_ID | 14 | Link to ISMS-IMP-A.5.35-36.S1 |
| B | Review_Type | 18 | User input |
| C | Planned_Date | 14 | Date field |
| D | Actual_Date | 14 | Date field |
| E | Status | 14 | Data validation |
| F | Reviewer | 22 | User input |
| G | Overall_Opinion | 18 | Data validation |
| H | Findings_Critical | 12 | Numeric |
| I | Findings_High | 12 | Numeric |
| J | Findings_Total | 12 | Numeric |
| K | Report_Issued | 10 | Data validation |
| L | Actions_Agreed | 10 | Data validation |
| M | Notes | 30 | User input |

#### Compliance_Status Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Compliance_Area | 30 | User input |
| B | Last_Assessment | 14 | Date field |
| C | Next_Assessment | 14 | Date field |
| D | Compliance_Score | 14 | Percentage |
| E | Status | 16 | Data validation |
| F | Trend | 12 | Data validation |
| G | Open_NonCompliance | 14 | Numeric |
| H | Key_Issues | 40 | User input |
| I | Owner | 22 | User input |
| J | Notes | 30 | User input |

#### Findings_Overview Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Period | 14 | User input |
| B | Total_Open | 12 | Numeric |
| C | Critical_Open | 12 | Numeric |
| D | High_Open | 12 | Numeric |
| E | Medium_Open | 12 | Numeric |
| F | Low_Open | 12 | Numeric |
| G | Closed_This_Period | 14 | Numeric |
| H | Opened_This_Period | 14 | Numeric |
| I | Overdue | 12 | Numeric |
| J | Overdue_Critical | 12 | Numeric |
| K | Overdue_High | 12 | Numeric |
| L | Avg_Age_Days | 12 | Numeric |
| M | Oldest_Finding | 14 | Numeric |
| N | MTTR_Critical | 12 | Numeric |
| O | MTTR_High | 12 | Numeric |

#### KPI_Scorecard Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | KPI_ID | 10 | Unique identifier |
| B | KPI_Name | 40 | KPI description |
| C | Target | 14 | Target value |
| D | Current_Value | 14 | Actual value |
| E | Prior_Period | 14 | Previous period |
| F | Trend | 12 | Data validation |
| G | Status | 12 | Data validation |
| H | Owner | 22 | User input |
| I | Notes | 30 | User input |

#### Trend_Analysis Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Period | 12 | Pre-populated (Q1 2025, etc.) |
| B | Period_End_Date | 14 | Date field |
| C | Reviews_Completed | 14 | Numeric |
| D | Reviews_Planned | 14 | Numeric |
| E | Compliance_Score | 14 | Percentage |
| F | Score_Change | 12 | Numeric (formula) |
| G | Open_Findings_Total | 14 | Numeric |
| H | Open_Critical | 12 | Numeric |
| I | Open_High | 12 | Numeric |
| J | Closed_in_Period | 14 | Numeric |
| K | MTTR_Critical | 12 | Numeric |
| L | MTTR_High | 12 | Numeric |
| M | Overall_Status | 12 | Data validation |
| N | Notes | 40 | User input |

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Overall_Status | Green, Amber, Red |
| KPI_Status | On Track, At Risk, Behind |
| Trend | Improving, Stable, Declining |
| Review_Status | Scheduled, In Progress, Completed, Overdue |
| Review_Opinion | Effective, Partially Effective, Ineffective |
| Compliance_Status | Compliant, Partial, Non-Compliant |
| Yes_No | Yes, No |
| Trend_Direction | Up, Down, Stable |

### Generator Reference

**Script**: `generate_a535_36_4_compliance_dashboard.py`

**Location**: `10-isms-scr-base/isms-a.5.35-36-compliance-review/10_generator-master/`

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
