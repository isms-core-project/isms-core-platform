# ISMS-IMP-A.5.37.4 - Compliance Dashboard

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.4 |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.37: Documented Operating Procedures |
| **Parent Policy** | ISMS-POL-A.5.37 Documented Operating Procedures Policy |
| **Related IMPs** | ISMS-IMP-A.5.37.1, ISMS-IMP-A.5.37.2, ISMS-IMP-A.5.37.3 |
| **Version** | 1.0 |
| **Classification** | Internal Use |
| **Owner** | Information Security Manager |
| **Last Review** | [Date to be set] |
| **Framework Version** | 1.0 |
| **Assessment Type** | Management Dashboard and Reporting |

---

## Control Requirement

> "Operating procedures for information processing facilities should be documented and made available to personnel who need them."
>
> — ISO/IEC 27001:2022, Annex A Control 5.37

---

## Table of Contents

### PART I: USER COMPLETION GUIDE
1. [Dashboard Overview](#1-dashboard-overview)
2. [Control Requirements](#2-control-requirements)
3. [Prerequisites](#3-prerequisites)
4. [Dashboard Views](#4-dashboard-views)
5. [Key Performance Indicators](#5-key-performance-indicators)
6. [Workbook Structure](#6-workbook-structure)
7. [Completion Walkthrough](#7-completion-walkthrough)
8. [Data Refresh Process](#8-data-refresh-process)
9. [Reporting and Export](#9-reporting-and-export)
10. [Evidence Collection](#10-evidence-collection)
11. [Common Pitfalls](#11-common-pitfalls)
12. [Quality Checklist](#12-quality-checklist)
13. [Review and Approval](#13-review-and-approval)
14. [Related Controls](#14-related-controls)

### PART II: TECHNICAL SPECIFICATION
15. [Workbook Architecture](#15-workbook-architecture)
16. [Sheet Specifications](#16-sheet-specifications)
17. [Data Validation Rules](#17-data-validation-rules)
18. [Conditional Formatting](#18-conditional-formatting)
19. [Formula Specifications](#19-formula-specifications)
20. [Chart Specifications](#20-chart-specifications)
21. [Cell Styling Standards](#21-cell-styling-standards)
22. [Generator Script Reference](#22-generator-script-reference)

---

# PART I: USER COMPLETION GUIDE

## 1. Dashboard Overview

### 1.1 Purpose

The Compliance Dashboard consolidates procedure management metrics from the A.5.37.1-3 workbooks into executive-ready visualisations. It provides real-time visibility into:

- **Procedure Documentation Status**: Coverage and completeness of documented procedures
- **Quality Scores**: Aggregate quality ratings across the procedure inventory
- **Review Compliance**: Currency of procedures against review schedules
- **Gap Remediation Progress**: Status of identified gaps and remediation activities
- **Change Activity Trends**: Volume and velocity of procedure changes

This dashboard serves as the primary management reporting tool for documented operating procedures, providing the metrics needed for ISMS management reviews and audit evidence.

### 1.2 Scope

The dashboard aggregates data from:
- **A.5.37.1 Procedure Inventory Assessment**: Procedure counts, coverage, approval status
- **A.5.37.2 Procedure Quality Assessment**: Quality scores, dimension ratings, gaps
- **A.5.37.3 Procedure Review and Update Tracking**: Review status, change requests, escalations

### 1.3 Audience and Use Cases

| Audience | Primary Use |
|----------|-------------|
| **CISO** | Executive summary, risk visibility, management review input |
| **ISM** | Operational monitoring, trend analysis, resource planning |
| **Department Heads** | Category performance, gap ownership, compliance status |
| **Auditors** | Compliance evidence, control effectiveness assessment |
| **Process Owners** | Individual procedure status, action items |

### 1.4 Dashboard Refresh Frequency

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Data refresh from source workbooks | Weekly | ISM or delegate |
| Trend data update | Monthly | ISM |
| Executive summary refresh | Monthly (before management review) | ISM |
| Full dashboard validation | Quarterly | ISM |

---

## 2. Control Requirements

### 2.1 ISO 27001:2022 A.5.37 Dashboard Requirements

While A.5.37 focuses on documented procedures, the ISMS requires monitoring and measurement (Clause 9.1). The dashboard supports:

| ISO Requirement | Dashboard Support |
|-----------------|-------------------|
| **9.1 Monitoring and measurement** | KPIs for procedure documentation and quality |
| **9.2 Internal audit** | Evidence of control effectiveness |
| **9.3 Management review** | Performance metrics for executive review |
| **10.1 Continual improvement** | Trend analysis for improvement opportunities |

### 2.2 Key Metrics Framework

| Metric Category | What It Measures | Why It Matters |
|-----------------|------------------|----------------|
| **Coverage** | Procedures documented vs required | Ensures no gaps in operational guidance |
| **Currency** | Procedures reviewed within cycle | Ensures procedures reflect current practice |
| **Quality** | Procedures meeting quality standards | Ensures procedures are usable and effective |
| **Gaps** | Open issues and remediation status | Shows active improvement efforts |
| **Change Velocity** | Rate of procedure updates | Indicates organisational agility and maturity |

### 2.3 Compliance Thresholds

| Metric | Target | Warning | Critical |
|--------|:------:|:-------:|:--------:|
| Overall Compliance Score | ≥95% | 80-94% | <80% |
| Procedures Approved | 100% | 90-99% | <90% |
| Reviews Current | ≥95% | 80-94% | <80% |
| Average Quality Score | ≥4.0 | 3.0-3.9 | <3.0 |
| Open Critical Gaps | 0 | 1-2 | >2 |
| Overdue Reviews | 0 | 1-5 | >5 |

---

## 3. Prerequisites

### 3.1 Required Source Workbooks

Before populating the dashboard, ensure the following are complete and current:

| Source Workbook | Key Data | Required Sheets |
|-----------------|----------|-----------------|
| **A.5.37.1 Procedure Inventory** | Procedure list, approval status, categories | Procedure_Inventory, Category_Summary |
| **A.5.37.2 Quality Assessment** | Quality scores, dimension ratings, gaps | Quality_Scores, Gap_Analysis, Dimension_Summary |
| **A.5.37.3 Review Tracking** | Review status, change requests, escalations | Review_Schedule, Change_Requests, Metrics_Summary |

### 3.2 Data Currency Requirements

| Source | Maximum Age | Refresh Before |
|--------|-------------|----------------|
| Procedure Inventory | 7 days | Dashboard refresh |
| Quality Assessment | 7 days | Dashboard refresh |
| Review Tracking | 7 days | Dashboard refresh |

### 3.3 Access Requirements

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| **Source Workbooks** | Read | Pull data for dashboard |
| **Dashboard Workbook** | Edit | Update dashboard data |
| **Report Distribution** | Send | Distribute reports |
| **Evidence Repository** | Write | Store dashboard snapshots |

---

## 4. Dashboard Views

### 4.1 Executive Summary View

High-level metrics designed for quick review by senior management:

| Element | Content | Update Frequency |
|---------|---------|------------------|
| **Overall Compliance Score** | Single percentage summarising overall status | Weekly |
| **Traffic Light Indicators** | Green/Yellow/Red for each major metric | Weekly |
| **Critical Issues Count** | Number of items requiring executive attention | Weekly |
| **Trend Arrows** | Direction of change from previous period | Monthly |
| **Period Summary** | Brief narrative of key changes | Monthly |

### 4.2 Category Performance View

Breakdown of metrics by procedure category:

| Category | Metrics Displayed |
|----------|-------------------|
| **System Operations** | Count, coverage %, approval %, quality avg, open gaps |
| **Security Operations** | Count, coverage %, approval %, quality avg, open gaps |
| **Facility Operations** | Count, coverage %, approval %, quality avg, open gaps |
| **Change Management** | Count, coverage %, approval %, quality avg, open gaps |
| **Recovery Operations** | Count, coverage %, approval %, quality avg, open gaps |
| **User Management** | Count, coverage %, approval %, quality avg, open gaps |
| **IT Operations** | Count, coverage %, approval %, quality avg, open gaps |
| **Network Operations** | Count, coverage %, approval %, quality avg, open gaps |

### 4.3 Quality Deep-Dive View

Detailed quality analysis:

| Element | Content |
|---------|---------|
| **Rating Distribution** | Count and percentage by rating (Excellent/Good/Adequate/Needs Improvement/Poor) |
| **Dimension Breakdown** | Average scores for each quality dimension |
| **Category Comparison** | Quality scores compared across categories |
| **Improvement Trends** | Quality score changes over time |

### 4.4 Review Compliance View

Procedure currency status:

| Element | Content |
|---------|---------|
| **Status Distribution** | Count by Current/Due Soon/Overdue |
| **Criticality Breakdown** | Review status by procedure criticality |
| **Overdue List** | Top 10 most overdue procedures |
| **Upcoming Reviews** | Reviews due in next 30 days |

### 4.5 Gap Remediation View

Gap management status:

| Element | Content |
|---------|---------|
| **Gap Status Summary** | Open/In Progress/Closed counts |
| **Severity Distribution** | Gaps by Critical/High/Medium/Low |
| **Aging Analysis** | Average age of open gaps |
| **Closure Trend** | Gap closure rate over time |
| **Overdue Gaps** | Gaps past remediation target date |

### 4.6 Change Activity View

Procedure change metrics:

| Element | Content |
|---------|---------|
| **CR Volume Trend** | Change requests over time |
| **Category Breakdown** | CRs by Administrative/Minor/Major/Emergency |
| **Cycle Time Metrics** | Average time from submission to implementation |
| **Approval Rate** | Approved vs rejected change requests |

---

## 5. Key Performance Indicators

### 5.1 Primary KPIs

| KPI | Definition | Formula | Target |
|-----|------------|---------|:------:|
| **Overall Compliance Score** | Weighted composite of all metrics | See formula below | ≥95% |
| **Procedure Coverage** | Procedures documented vs required | (Documented/Required) × 100 | 100% |
| **Approval Rate** | Procedures with valid approval | (Approved/Total) × 100 | 100% |
| **Review Currency** | Procedures reviewed within cycle | (Current/Total) × 100 | ≥95% |
| **Average Quality Score** | Mean quality score across inventory | SUM(Scores)/COUNT(Procedures) | ≥4.0 |
| **Open Gap Count** | Total open gaps | COUNT(Status="Open") | 0 |

### 5.2 Overall Compliance Score Formula

The Overall Compliance Score is a weighted composite:

```
Overall Compliance Score =
    (Approval Rate × 0.25) +
    (Review Currency × 0.25) +
    ((Average Quality Score / 5) × 100 × 0.25) +
    ((1 - (Open Gaps / Total Procedures)) × 100 × 0.25)
```

| Component | Weight | Rationale |
|-----------|:------:|-----------|
| Approval Rate | 25% | Ensures governance oversight |
| Review Currency | 25% | Ensures procedures are current |
| Quality Score | 25% | Ensures procedures are effective |
| Gap Remediation | 25% | Ensures continuous improvement |

### 5.3 Secondary KPIs

| KPI | Definition | Target |
|-----|------------|:------:|
| CR Approval Rate | Change requests approved vs total | Track trend |
| CR Cycle Time (Minor) | Days from submission to implementation | ≤5 days |
| CR Cycle Time (Major) | Days from submission to implementation | ≤14 days |
| Communication Acknowledgement | Acknowledgement rate for notifications | ≥90% |
| Training Completion | Training completion for major changes | 100% |
| Zero L3 Escalations | Count of L3 escalations | 0 |

### 5.4 Trend Indicators

| Indicator | Meaning |
|-----------|---------|
| ↑ Improving | Current period better than previous |
| → Stable | No significant change |
| ↓ Declining | Current period worse than previous |

Trend calculation: Compare current period to previous period (month-over-month or quarter-over-quarter).

---

## 6. Workbook Structure

### 6.1 Sheet Overview

| Sheet # | Sheet Name | Purpose | Primary Users |
|:-------:|------------|---------|---------------|
| 1 | Executive_Dashboard | High-level summary with KPIs | CISO, Management |
| 2 | Category_Analysis | Performance by procedure category | Department Heads, ISM |
| 3 | Review_Status | Review compliance tracking | ISM, Procedure Owners |
| 4 | Quality_Overview | Quality assessment summary | ISM, Quality team |
| 5 | Gap_Tracking | Gap remediation status | ISM, Process Owners |
| 6 | Change_Activity | Change request metrics | ISM, Change Management |
| 7 | Trend_History | Historical trend data | ISM, Auditors |
| 8 | Data_Sources | Source workbook links | ISM (technical) |
| 9 | Instructions | User guidance | All users |

### 6.2 Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      DASHBOARD DATA FLOW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SOURCE WORKBOOKS                                               │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐    │
│  │ A.5.37.1       │  │ A.5.37.2       │  │ A.5.37.3       │    │
│  │ Inventory      │  │ Quality        │  │ Review         │    │
│  └───────┬────────┘  └───────┬────────┘  └───────┬────────┘    │
│          │                   │                   │              │
│          ▼                   ▼                   ▼              │
│  ┌────────────────────────────────────────────────────────┐    │
│  │                    Data_Sources Sheet                   │    │
│  │              (External references/links)                │    │
│  └─────────────────────────┬──────────────────────────────┘    │
│                            │                                    │
│          ┌─────────────────┼─────────────────┐                 │
│          ▼                 ▼                 ▼                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ Category_    │  │ Quality_     │  │ Review_      │         │
│  │ Analysis     │  │ Overview     │  │ Status       │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│          │                 │                 │                 │
│          ▼                 ▼                 ▼                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ Gap_         │  │ Change_      │  │ Trend_       │         │
│  │ Tracking     │  │ Activity     │  │ History      │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│          │                 │                 │                 │
│          └─────────────────┼─────────────────┘                 │
│                            ▼                                    │
│                  ┌──────────────────┐                          │
│                  │ Executive_       │                          │
│                  │ Dashboard        │                          │
│                  └──────────────────┘                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Completion Walkthrough

### Step 1: Verify Source Data Currency

**Objective:** Ensure source workbooks are current before refresh

**Actions:**
1. Open each source workbook (A.5.37.1, A.5.37.2, A.5.37.3)
2. Check "Last Updated" date in each
3. If older than 7 days, update source workbook first
4. Note any data issues or pending updates

**Verification Checklist:**
- [ ] A.5.37.1 Inventory updated within 7 days
- [ ] A.5.37.2 Quality Assessment updated within 7 days
- [ ] A.5.37.3 Review Tracking updated within 7 days
- [ ] No pending data corrections in source workbooks

### Step 2: Refresh Data Sources (Sheet 8)

**Objective:** Update all external data links

**Actions:**
1. Navigate to Data_Sources sheet
2. Update Last_Updated column for each source
3. If using Excel links, refresh external data
4. If manual, copy latest summary data from sources
5. Verify data connection status (Connected/Error)

**Data Points to Capture:**

| Source | Data Elements |
|--------|---------------|
| **A.5.37.1** | Total procedures, by category, approval status |
| **A.5.37.2** | Quality scores, dimension averages, gap counts |
| **A.5.37.3** | Review status counts, CR counts, escalation counts |

### Step 3: Update Category Analysis (Sheet 2)

**Objective:** Refresh category-level performance data

**Actions:**
1. Update procedure counts per category
2. Calculate compliance percentages
3. Update quality averages per category
4. Identify categories below target
5. Apply conditional formatting

**Data to Capture per Category:**

| Field | Source |
|-------|--------|
| Total_Count | A.5.37.1 |
| Documented | A.5.37.1 |
| Approved | A.5.37.1 |
| Current (Reviews) | A.5.37.3 |
| Compliance_% | Calculated |
| Avg_Quality | A.5.37.2 |
| Open_Gaps | A.5.37.2 |

### Step 4: Update Review Status (Sheet 3)

**Objective:** Refresh review compliance data

**Actions:**
1. Update status counts (Current/Due Soon/Overdue)
2. Update criticality breakdown
3. Refresh overdue procedure list
4. Update upcoming review list
5. Calculate review currency percentage

### Step 5: Update Quality Overview (Sheet 4)

**Objective:** Refresh quality metrics

**Actions:**
1. Update rating distribution
2. Update dimension average scores
3. Refresh quality trends
4. Update comparison charts

### Step 6: Update Gap Tracking (Sheet 5)

**Objective:** Refresh gap remediation data

**Actions:**
1. Update gap status summary
2. Update severity distribution
3. Calculate average gap age
4. Update closure trend
5. Identify overdue gaps

### Step 7: Update Change Activity (Sheet 6)

**Objective:** Refresh change management metrics

**Actions:**
1. Update CR volume for current period
2. Update category breakdown
3. Calculate cycle time metrics
4. Update approval rate

### Step 8: Update Trend History (Sheet 7)

**Objective:** Capture current period for trend analysis

**Actions:**
1. Add new row for current period
2. Capture all key metrics
3. Verify trend calculations
4. Add period notes if significant events

### Step 9: Update Executive Dashboard (Sheet 1)

**Objective:** Refresh executive summary view

**Actions:**
1. Verify all calculated metrics update correctly
2. Update traffic light indicators
3. Update trend arrows
4. Update period summary narrative
5. Review overall compliance score

### Step 10: Validate and Export

**Objective:** Final quality check and report distribution

**Actions:**
1. Validate all metrics against source data
2. Check for calculation errors
3. Export executive summary PDF
4. Store snapshot in evidence repository
5. Distribute reports to stakeholders

---

## 8. Data Refresh Process

### 8.1 Manual Refresh Procedure

1. **Open Source Workbooks**: Open all three source workbooks (read-only)
2. **Open Dashboard Workbook**: Open the dashboard for editing
3. **Check Links**: Excel > Data > Edit Links > Check status
4. **Update Links**: Click "Update Values" for each linked workbook
5. **Refresh Pivot Tables**: Right-click each pivot > Refresh
6. **Verify Calculations**: Spot-check key metrics against source
7. **Update Timestamp**: Update Last_Refreshed date in Data_Sources sheet
8. **Save Dashboard**: Save and close

### 8.2 Automated Refresh (If Configured)

| Setting | Value |
|---------|-------|
| Refresh Schedule | Daily at 06:00 |
| Trigger | Source workbook modification |
| Notification | Email on completion or error |
| Log Location | [System path] |

### 8.3 Troubleshooting Data Issues

| Issue | Possible Cause | Resolution |
|-------|----------------|------------|
| #REF! errors | Source file moved/renamed | Update file path in Data_Sources |
| #VALUE! errors | Data type mismatch | Check source data format |
| Stale data | Links not refreshed | Force refresh of external links |
| Missing data | New procedures not included | Update source workbook ranges |
| Incorrect totals | Formula range incomplete | Extend formula ranges |

---

## 9. Reporting and Export

### 9.1 Standard Reports

| Report | Content | Frequency | Distribution |
|--------|---------|-----------|--------------|
| **Executive Summary** | Sheet 1 as PDF | Monthly | CISO, Management |
| **Category Report** | Sheet 2 as PDF | Quarterly | Department Heads |
| **Gap Status Report** | Sheet 5 as PDF | Weekly | ISM, Gap Owners |
| **Audit Evidence Package** | All sheets as PDF | On request | Auditors |

### 9.2 Export Procedure

1. Select sheet to export
2. File > Print > Save as PDF
3. Name file: `ISMS-A.5.37.4_[ReportName]_YYYYMMDD.pdf`
4. Store in: ISMS Evidence Library/A.5.37/Dashboard Reports/
5. Distribute via secure email or SharePoint

### 9.3 Management Review Input

For ISMS Management Review (ISO 27001 Clause 9.3), provide:

| Input Item | Dashboard Source |
|------------|------------------|
| Performance of information security processes | Overall Compliance Score, KPIs |
| Status of corrective actions | Gap Tracking sheet |
| Changes affecting the ISMS | Change Activity trends |
| Opportunities for improvement | Gap analysis, quality scores |

---

## 10. Evidence Collection

### 10.1 Evidence Requirements

| Evidence Type | Format | Retention |
|---------------|--------|-----------|
| **Dashboard Snapshots** | PDF export of Executive_Dashboard | 3 years |
| **Trend Data** | Excel snapshot of Trend_History | Permanent |
| **Management Reports** | PDF exports per distribution | 3 years |
| **Audit Evidence Packages** | Complete PDF bundle | Per audit cycle |

### 10.2 Evidence Storage

| Evidence Type | Storage Location | Naming Convention |
|---------------|------------------|-------------------|
| Monthly snapshots | ISMS Evidence Library/A.5.37/Dashboard/ | A.5.37.4_Dashboard_YYYYMM.pdf |
| Quarterly reports | ISMS Evidence Library/A.5.37/Reports/ | A.5.37.4_QtrReport_YYYYQN.pdf |
| Audit packages | ISMS Evidence Library/Audits/[Year]/ | A.5.37_AuditEvidence_YYYYMMDD.pdf |

### 10.3 Audit Evidence Checklist

For auditors requesting evidence of A.5.37 compliance:

- [ ] Current Executive Dashboard showing compliance score ≥95%
- [ ] Category Analysis showing all categories meeting targets
- [ ] Review Status showing ≤5% overdue reviews
- [ ] Gap Tracking showing gap remediation progress
- [ ] Trend History showing improvement or stability over 12 months
- [ ] Management review meeting minutes referencing dashboard metrics

---

## 11. Common Pitfalls

### Dashboard Design Pitfalls

❌ **MISTAKE:** Creating a dashboard with too many metrics, overwhelming users
✅ **CORRECT:** Focus on the 5-7 key metrics that drive decisions; provide drill-down for detail

❌ **MISTAKE:** Using inconsistent colour coding across different views
✅ **CORRECT:** Apply consistent traffic light logic: Green = target met, Yellow = warning, Red = critical

❌ **MISTAKE:** Displaying raw numbers without context (e.g., "15 gaps")
✅ **CORRECT:** Show numbers with trend and target (e.g., "15 gaps ↓ from 18, target: 0")

❌ **MISTAKE:** Creating charts that are visually appealing but hard to interpret
✅ **CORRECT:** Prioritise clarity over aesthetics; every chart should answer a specific question

### Data Quality Pitfalls

❌ **MISTAKE:** Refreshing dashboard without verifying source data currency
✅ **CORRECT:** Always check source workbook "Last Updated" dates before refresh

❌ **MISTAKE:** Manual entry of data that could be linked/calculated
✅ **CORRECT:** Use formulas and links wherever possible to prevent transcription errors

❌ **MISTAKE:** Not documenting data sources and calculation methodologies
✅ **CORRECT:** Maintain Data_Sources sheet with clear documentation of each data element

❌ **MISTAKE:** Ignoring data validation errors or #REF! issues
✅ **CORRECT:** Treat any calculation error as critical—investigate and fix before distribution

### Reporting Pitfalls

❌ **MISTAKE:** Distributing dashboard without narrative context
✅ **CORRECT:** Include brief summary of key changes, issues requiring attention, and action items

❌ **MISTAKE:** Sending different versions to different stakeholders without version control
✅ **CORRECT:** Use single source of truth; if filtered views needed, use same base data

❌ **MISTAKE:** Not archiving dashboard snapshots as evidence
✅ **CORRECT:** Save PDF snapshot monthly to evidence repository before any updates

❌ **MISTAKE:** Waiting until management review to identify critical issues
✅ **CORRECT:** Set up alerts for critical thresholds; escalate immediately, don't wait for scheduled reports

### Interpretation Pitfalls

❌ **MISTAKE:** Celebrating "100% compliance" without examining the data quality
✅ **CORRECT:** Validate that high scores reflect genuine compliance, not gaming or incomplete data

❌ **MISTAKE:** Focusing only on negative indicators (gaps, overdue items)
✅ **CORRECT:** Also highlight improvements and successes to maintain stakeholder engagement

❌ **MISTAKE:** Treating all categories/procedures as equally important
✅ **CORRECT:** Weight or prioritise based on criticality; one gap in critical procedure > ten in low-priority

❌ **MISTAKE:** Comparing metrics across periods without accounting for scope changes
✅ **CORRECT:** Note when procedure inventory changes significantly; rebase trends if needed

---

## 12. Quality Checklist

### Pre-Distribution Checklist

#### Data Integrity
- [ ] All source workbooks updated within the last 7 days
- [ ] External data links refreshed successfully
- [ ] No #REF!, #VALUE!, or #DIV/0! errors visible
- [ ] Spot-check: Dashboard totals match source workbook totals
- [ ] Last_Refreshed timestamp updated

#### Metric Accuracy
- [ ] Overall Compliance Score calculated correctly
- [ ] Category counts sum to total procedure count
- [ ] Review status counts sum to total procedure count
- [ ] Gap counts match source workbook
- [ ] Trend arrows reflect actual direction of change

#### Visual Quality
- [ ] Traffic light indicators correct (Green/Yellow/Red)
- [ ] Charts render correctly without display issues
- [ ] All labels and titles visible and correct
- [ ] Print preview shows complete content (no cut-off)
- [ ] Conditional formatting applied consistently

#### Documentation
- [ ] Period summary narrative updated (if monthly report)
- [ ] Any significant changes noted
- [ ] Data_Sources sheet current
- [ ] Version/date in footer updated

#### Distribution
- [ ] Correct recipients identified
- [ ] PDF export readable and complete
- [ ] Evidence copy archived
- [ ] Distribution method appropriate for classification

---

## 13. Review and Approval

### 13.1 Dashboard Review Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    DASHBOARD REVIEW WORKFLOW                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────────┐   │
│  │ ISM Updates  │      │ QA Check     │      │ Distribution │   │
│  │ Dashboard    │─────▶│ & Validation │─────▶│ to Stake-    │   │
│  │              │      │              │      │ holders      │   │
│  └──────────────┘      └──────────────┘      └──────────────┘   │
│        │                      │                      │          │
│        ▼                      ▼                      ▼          │
│  Data Refresh          Error Check            Evidence         │
│  Completed             Passed                 Archived          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 13.2 Approval Authorities

| Dashboard Activity | Owner | Reviewer |
|--------------------|-------|----------|
| Weekly refresh | ISM or delegate | Self-check |
| Monthly report | ISM | CISO (optional) |
| Audit evidence package | ISM | CISO |
| Methodology changes | ISM | CISO approval required |

### 13.3 Sign-off Record

| Activity | Name | Date |
|----------|------|------|
| Dashboard Refresh Completed | | |
| Quality Check Passed | | |
| Distribution Authorised | | |

---

## 14. Related Controls

### 14.1 Primary Dependencies

| Control | Relationship | Integration |
|---------|--------------|-------------|
| **A.5.37.1** | Procedure Inventory | Source of procedure counts and categories |
| **A.5.37.2** | Quality Assessment | Source of quality scores and gaps |
| **A.5.37.3** | Review Tracking | Source of review status and change metrics |
| **A.5.1** | Information Security Policy | Policy framework governance |

### 14.2 Downstream Consumers

| Consumer | What They Use |
|----------|---------------|
| **Management Review** | Overall compliance score, trend data |
| **Internal Audit** | Full dashboard as control evidence |
| **Risk Management** | Gap data for risk assessment |
| **Improvement Planning** | Trend analysis for improvement priorities |

### 14.3 Related ISMS Dashboards

| Dashboard | Relationship |
|-----------|--------------|
| **ISMS Master Dashboard** | A.5.37.4 feeds overall compliance score |
| **Control Effectiveness Dashboard** | A.5.37.4 provides procedure control data |
| **Gap Register Dashboard** | A.5.37.4 contributes procedure gaps |

---

# PART II: TECHNICAL SPECIFICATION

## 15. Workbook Architecture

### 15.1 Generator Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a537_4_compliance_dashboard.py` |
| **Script Location** | `10-isms-scr-base/isms-a.5.37-documented-procedures/10_generator-master/` |
| **Output Location** | `10-isms-scr-base/isms-a.5.37-documented-procedures/90_workbooks/` |
| **Output Filename** | `ISMS-IMP-A.5.37.4_Compliance_Dashboard_YYYYMMDD.xlsx` |

### 15.2 Technical Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    WORKBOOK ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    HEADER STRUCTURE                       │   │
│  │  Row 1: Dashboard Title Bar (merged A1:H1)               │   │
│  │  Row 2: Report Period                                     │   │
│  │  Row 3: Last Refreshed Date                               │   │
│  │  Row 4: Empty (separator)                                 │   │
│  │  Row 5+: Dashboard Content                                │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │Executive │ │Category  │ │Review    │ │Quality   │          │
│  │Dashboard │ │Analysis  │ │Status    │ │Overview  │          │
│  │ Sheet 1  │ │ Sheet 2  │ │ Sheet 3  │ │ Sheet 4  │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │Gap       │ │Change    │ │Trend     │ │Data      │          │
│  │Tracking  │ │Activity  │ │History   │ │Sources   │          │
│  │ Sheet 5  │ │ Sheet 6  │ │ Sheet 7  │ │ Sheet 8  │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│                                                                 │
│  ┌──────────┐                                                   │
│  │Instruc-  │                                                   │
│  │tions     │                                                   │
│  │ Sheet 9  │                                                   │
│  └──────────┘                                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 16. Sheet Specifications

### Sheet 1: Executive_Dashboard

**Purpose:** High-level KPIs and compliance summary

**Layout:**

| Section | Location | Content |
|---------|----------|---------|
| Title Block | A1:H3 | Dashboard title, period, refresh date |
| Overall Score | B5:C8 | Compliance score gauge |
| KPI Cards | D5:H8 | Individual KPI values with traffic lights |
| Trend Summary | B10:H12 | Sparklines and trend arrows |
| Critical Issues | B14:H20 | List of items requiring attention |
| Period Notes | B22:H25 | Narrative summary |

**Key Cells:**

| Cell | Content | Formula/Value |
|------|---------|---------------|
| C6 | Overall Compliance Score | Composite formula |
| D6 | Approval Rate | From Data_Sources |
| E6 | Review Currency | From Data_Sources |
| F6 | Avg Quality Score | From Data_Sources |
| G6 | Open Gaps | From Data_Sources |
| H6 | Overdue Reviews | From Data_Sources |

### Sheet 2: Category_Analysis

**Purpose:** Performance breakdown by procedure category

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Category | 25 | Text | Procedure category name |
| B | Total_Count | 12 | Number | Total procedures |
| C | Documented | 12 | Number | With documentation |
| D | Approved | 12 | Number | With approval |
| E | Current | 12 | Number | Review current |
| F | Compliance_% | 12 | Percent | Overall compliance |
| G | Avg_Quality | 12 | Number | Average quality score |
| H | Open_Gaps | 12 | Number | Open gaps |
| I | Status | 10 | Text | Traffic light |

### Sheet 3: Review_Status

**Purpose:** Review compliance summary

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Status | 15 | Text | OVERDUE/DUE SOON/CURRENT |
| B | Count | 10 | Number | Procedures in status |
| C | Percentage | 10 | Percent | % of total |
| D | Critical_Count | 12 | Number | Critical procedures |
| E | High_Count | 12 | Number | High criticality |
| F | Medium_Count | 12 | Number | Medium criticality |
| G | Low_Count | 12 | Number | Low criticality |

**Additional Sections:**
- Top 10 Overdue List (rows 15-25)
- Upcoming Reviews 30-Day List (rows 30-45)

### Sheet 4: Quality_Overview

**Purpose:** Quality assessment summary

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Rating | 20 | Text | Excellent/Good/Adequate/Needs Improvement/Poor |
| B | Count | 10 | Number | Procedures with rating |
| C | Percentage | 10 | Percent | % of assessed |
| D | Avg_Clarity | 12 | Number | Clarity dimension |
| E | Avg_Completeness | 12 | Number | Completeness dimension |
| F | Avg_Accuracy | 12 | Number | Accuracy dimension |
| G | Avg_Usability | 12 | Number | Usability dimension |
| H | Avg_Maintainability | 12 | Number | Maintainability dimension |

### Sheet 5: Gap_Tracking

**Purpose:** Gap remediation status

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Severity | 12 | Text | Critical/High/Medium/Low |
| B | Open | 10 | Number | Open gaps |
| C | In_Progress | 10 | Number | Being addressed |
| D | Closed | 10 | Number | Resolved |
| E | Total | 10 | Number | All gaps |
| F | Closure_Rate | 12 | Percent | % closed |
| G | Avg_Days_Open | 12 | Number | Average age |
| H | Overdue | 10 | Number | Past target date |

### Sheet 6: Change_Activity

**Purpose:** Change request metrics

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Period | 12 | Text | Month/Quarter |
| B | Submitted | 10 | Number | CRs submitted |
| C | Approved | 10 | Number | CRs approved |
| D | Rejected | 10 | Number | CRs rejected |
| E | Implemented | 10 | Number | CRs completed |
| F | Approval_Rate | 12 | Percent | % approved |
| G | Avg_Cycle_Time | 12 | Number | Days to implement |
| H | Emergency_Count | 10 | Number | Emergency changes |

### Sheet 7: Trend_History

**Purpose:** Historical trend data for analysis

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Period | 12 | Text | YYYY-MM or YYYY-QN |
| B | Total_Procedures | 12 | Number | Count at period |
| C | Compliance_% | 12 | Percent | Overall compliance |
| D | Avg_Quality | 12 | Number | Quality score |
| E | Open_Gaps | 12 | Number | Gap count |
| F | Overdue_Reviews | 12 | Number | Overdue count |
| G | CR_Volume | 12 | Number | Change requests |
| H | Notes | 40 | Text | Period notes |

### Sheet 8: Data_Sources

**Purpose:** Document and track source workbook links

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Source_Workbook | 30 | Text | Source file name |
| B | Sheet | 20 | Text | Source sheet |
| C | Data_Range | 20 | Text | Range reference |
| D | Last_Updated | 15 | Date | Last refresh |
| E | Refresh_Method | 15 | Text | Manual/Auto/Link |
| F | Status | 15 | Text | Connected/Error/Stale |

### Sheet 9: Instructions

**Purpose:** User guidance for dashboard

Static content including:
- Dashboard navigation guide
- Metric definitions
- Data refresh procedures
- Troubleshooting guide
- Report distribution list
- Contact information

---

## 17. Data Validation Rules

### 17.1 Dropdown Lists

| Field | Valid Values |
|-------|--------------|
| **Rating** | Excellent, Good, Adequate, Needs Improvement, Poor |
| **Status** | OVERDUE, DUE SOON, CURRENT |
| **Severity** | Critical, High, Medium, Low |
| **Refresh_Method** | Manual, Auto, Link |
| **Connection_Status** | Connected, Error, Stale |

### 17.2 Numeric Constraints

| Field | Constraint |
|-------|------------|
| Counts | ≥0, whole numbers |
| Percentages | 0-100 |
| Quality Scores | 0.0-5.0 |
| Days | ≥0 |

---

## 18. Conditional Formatting

### 18.1 Traffic Light Rules

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| Overall Compliance | ≥95% | 80-94% | <80% |
| Approval Rate | =100% | 90-99% | <90% |
| Review Currency | ≥95% | 80-94% | <80% |
| Quality Score | ≥4.0 | 3.0-3.9 | <3.0 |
| Open Gaps | 0 | 1-5 | >5 |
| Overdue Reviews | 0 | 1-5 | >5 |

### 18.2 Colour Codes

| Condition | Fill Colour | Text Colour |
|-----------|-------------|-------------|
| Target Met (Green) | #90EE90 | #006400 |
| Warning (Yellow) | #FFFF00 | #8B8000 |
| Critical (Red) | #FF0000 | #FFFFFF |
| Neutral | #FFFFFF | #000000 |

### 18.3 Trend Arrow Formatting

| Trend | Symbol | Colour |
|-------|:------:|--------|
| Improving | ↑ | Green (#008000) |
| Stable | → | Black (#000000) |
| Declining | ↓ | Red (#FF0000) |

---

## 19. Formula Specifications

### 19.1 Overall Compliance Score

```excel
=((D6/100)*0.25)+((E6/100)*0.25)+((F6/5)*0.25)+((1-(G6/B6))*0.25)*100
```

Where:
- D6 = Approval Rate %
- E6 = Review Currency %
- F6 = Average Quality Score (0-5)
- G6 = Open Gaps
- B6 = Total Procedures

### 19.2 Category Compliance

```excel
=SUMPRODUCT((Inventory!$C:$C=A2)*(Inventory!$K:$K="Approved")*(Review!$H:$H<>"OVERDUE"))/
 COUNTIF(Inventory!$C:$C,A2)*100
```

### 19.3 Quality Trend Direction

```excel
=IF(Trend_History!D2>Trend_History!D3,"↑",IF(Trend_History!D2<Trend_History!D3,"↓","→"))
```

### 19.4 Gap Closure Rate

```excel
=D2/(B2+C2+D2)*100
```

Where: B2=Open, C2=In Progress, D2=Closed

### 19.5 Average Days Open

```excel
=AVERAGEIFS(Gap_Analysis!J:J,Gap_Analysis!H:H,"Open")
```

### 19.6 Review Currency Rate

```excel
=COUNTIF(Review_Schedule!$H:$H,"CURRENT")/COUNTA(Review_Schedule!$A:$A)*100
```

---

## 20. Chart Specifications

### 20.1 Compliance Gauge Chart (Executive Dashboard)

| Property | Value |
|----------|-------|
| Type | Doughnut chart (half) |
| Data | [Compliance %, 100-Compliance %] |
| Colours | [Traffic light colour, Light grey] |
| Centre Label | Percentage value, 24pt bold |
| Legend | None |
| Size | 200x150 pixels |

### 20.2 Category Performance Bar Chart

| Property | Value |
|----------|-------|
| Type | Clustered horizontal bar |
| Categories | Procedure categories |
| Values | Compliance % |
| Reference Line | 95% target |
| Colours | Traffic light by value |
| Legend | None |
| Size | 400x300 pixels |

### 20.3 Quality Radar Chart

| Property | Value |
|----------|-------|
| Type | Radar (filled) |
| Axes | 5 quality dimensions |
| Series | Current period, Previous period |
| Scale | 0-5 |
| Colours | Blue (current), Grey (previous) |
| Legend | Bottom |
| Size | 300x300 pixels |

### 20.4 Gap Burn-Down Chart

| Property | Value |
|----------|-------|
| Type | Line with area |
| X-Axis | Time periods (12 months) |
| Y-Axis | Open gap count |
| Trend Line | Linear forecast |
| Colours | Blue area, red trend line |
| Legend | None |
| Size | 400x250 pixels |

### 20.5 CR Volume Trend Chart

| Property | Value |
|----------|-------|
| Type | Stacked column |
| X-Axis | Periods (12 months) |
| Y-Axis | CR count |
| Series | Submitted, Approved, Implemented |
| Colours | Blue, Green, Grey |
| Legend | Bottom |
| Size | 400x250 pixels |

---

## 21. Cell Styling Standards

### 21.1 Colour Palette

| Element | Colour | Hex Code | Usage |
|---------|--------|----------|-------|
| Header Background | Dark Blue | #1F4E79 | Dashboard headers |
| Header Text | White | #FFFFFF | Header text |
| KPI Card Background | Light Blue | #DEEBF7 | Metric cards |
| Success | Green | #90EE90 | Target met indicators |
| Warning | Yellow | #FFFF00 | Warning indicators |
| Critical | Red | #FF0000 | Critical indicators |
| Chart Background | White | #FFFFFF | Chart areas |
| Border | Grey | #D0D0D0 | Cell borders |

### 21.2 Font Standards

| Element | Font | Size | Style |
|---------|------|:----:|-------|
| Dashboard Title | Calibri | 20 | Bold |
| KPI Values | Calibri | 24 | Bold |
| KPI Labels | Calibri | 11 | Regular |
| Section Headers | Calibri | 14 | Bold |
| Data Cells | Calibri | 10 | Regular |
| Trend Arrows | Calibri | 14 | Bold |

### 21.3 Number Formats

| Data Type | Format | Example |
|-----------|--------|---------|
| Percentage | 0% | 95% |
| Quality Score | 0.0 | 4.2 |
| Count | 0 | 42 |
| Date | DD.MM.YYYY | 03.02.2026 |
| Period | YYYY-MM | 2026-02 |

---

## 22. Generator Script Reference

### 22.1 Script Structure

```python
# =============================================================================
# ISMS-IMP-A.5.37.4 - Compliance Dashboard Generator
# =============================================================================
# ISO 27001:2022 Control A.5.37: Documented Operating Procedures
# Generates executive dashboard consolidating A.5.37.1-3 metrics
# =============================================================================

# Document Metadata
DOCUMENT_ID = "ISMS-IMP-A.5.37.4"
WORKBOOK_NAME = "Compliance Dashboard"
CONTROL_ID = "A.5.37"
CONTROL_NAME = "Documented Operating Procedures"

# Output Configuration
OUTPUT_FILENAME = f"{DOCUMENT_ID}_Compliance_Dashboard_{GENERATED_TIMESTAMP}.xlsx"
```

### 22.2 Key Functions

| Function | Purpose |
|----------|---------|
| `create_workbook()` | Initialise workbook with standard structure |
| `create_executive_dashboard()` | Generate Sheet 1 with KPIs and charts |
| `create_category_analysis()` | Generate Sheet 2 with category breakdown |
| `create_review_status()` | Generate Sheet 3 with review metrics |
| `create_quality_overview()` | Generate Sheet 4 with quality data |
| `create_gap_tracking()` | Generate Sheet 5 with gap metrics |
| `create_change_activity()` | Generate Sheet 6 with CR metrics |
| `create_trend_history()` | Generate Sheet 7 with trend data |
| `create_data_sources()` | Generate Sheet 8 with source links |
| `create_instructions()` | Generate Sheet 9 with user guide |
| `create_charts()` | Add visual elements to dashboard |
| `apply_conditional_formatting()` | Apply traffic light rules |
| `apply_formulas()` | Add calculated fields |
| `style_workbook()` | Apply consistent styling |

### 22.3 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| openpyxl | ≥3.0.0 | Excel workbook generation |
| openpyxl.chart | ≥3.0.0 | Chart creation |
| datetime | stdlib | Date handling |
| logging | stdlib | Execution logging |

### 22.4 Execution

```bash
cd 10-isms-scr-base/isms-a.5.37-documented-procedures/10_generator-master/
python3 generate_a537_4_compliance_dashboard.py
mv ISMS-IMP-A.5.37.4_*.xlsx ../90_workbooks/
```

### 22.5 Output Verification

After generation, verify:
- [ ] All 9 sheets created
- [ ] Executive Dashboard layout correct
- [ ] Charts render properly
- [ ] Conditional formatting applied
- [ ] Formulas calculate correctly
- [ ] Print area configured for each sheet
- [ ] Headers/footers set for printing

---

**END OF SPECIFICATION**

---

*"You can't manage what you can't measure."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-03 -->
