<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.37.4-UG:framework:UG:a.5.37.4 -->
**ISMS-IMP-A.5.37.4-UG - Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.37: Documented Operating Procedures

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.4-UG |
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

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.37.4-TG.

---

## Dashboard Overview

### Purpose

The Compliance Dashboard consolidates procedure management metrics from the A.5.37.1-3 workbooks into executive-ready visualisations. It provides real-time visibility into:

- **Procedure Documentation Status**: Coverage and completeness of documented procedures
- **Quality Scores**: Aggregate quality ratings across the procedure inventory
- **Review Compliance**: Currency of procedures against review schedules
- **Gap Remediation Progress**: Status of identified gaps and remediation activities
- **Change Activity Trends**: Volume and velocity of procedure changes

This dashboard serves as the primary management reporting tool for documented operating procedures, providing the metrics needed for ISMS management reviews and audit evidence.

### Scope

The dashboard aggregates data from:
- **A.5.37.1 Procedure Inventory Assessment**: Procedure counts, coverage, approval status
- **A.5.37.2 Procedure Quality Assessment**: Quality scores, dimension ratings, gaps
- **A.5.37.3 Procedure Review and Update Tracking**: Review status, change requests, escalations

### Audience and Use Cases

| Audience | Primary Use |
|----------|-------------|
| **CISO** | Executive summary, risk visibility, management review input |
| **ISM** | Operational monitoring, trend analysis, resource planning |
| **Department Heads** | Category performance, gap ownership, compliance status |
| **Auditors** | Compliance evidence, control effectiveness assessment |
| **Process Owners** | Individual procedure status, action items |

### Dashboard Refresh Frequency

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Data refresh from source workbooks | Weekly | ISM or delegate |
| Trend data update | Monthly | ISM |
| Executive summary refresh | Monthly (before management review) | ISM |
| Full dashboard validation | Quarterly | ISM |

---

## Control Requirements

### ISO 27001:2022 A.5.37 Dashboard Requirements

While A.5.37 focuses on documented procedures, the ISMS requires monitoring and measurement (Clause 9.1). The dashboard supports:

| ISO Requirement | Dashboard Support |
|-----------------|-------------------|
| **9.1 Monitoring and measurement** | KPIs for procedure documentation and quality |
| **9.2 Internal audit** | Evidence of control effectiveness |
| **9.3 Management review** | Performance metrics for executive review |
| **10.1 Continual improvement** | Trend analysis for improvement opportunities |

### Key Metrics Framework

| Metric Category | What It Measures | Why It Matters |
|-----------------|------------------|----------------|
| **Coverage** | Procedures documented vs required | Ensures no gaps in operational guidance |
| **Currency** | Procedures reviewed within cycle | Ensures procedures reflect current practice |
| **Quality** | Procedures meeting quality standards | Ensures procedures are usable and effective |
| **Gaps** | Open issues and remediation status | Shows active improvement efforts |
| **Change Velocity** | Rate of procedure updates | Indicates organisational agility and maturity |

### Compliance Thresholds

| Metric | Target | Warning | Critical |
|--------|:------:|:-------:|:--------:|
| Overall Compliance Score | ≥95% | 80-94% | <80% |
| Procedures Approved | 100% | 90-99% | <90% |
| Reviews Current | ≥95% | 80-94% | <80% |
| Average Quality Score | ≥4.0 | 3.0-3.9 | <3.0 |
| Open Critical Gaps | 0 | 1-2 | >2 |
| Overdue Reviews | 0 | 1-5 | >5 |

---

## Prerequisites

### Required Source Workbooks

Before populating the dashboard, ensure the following are complete and current:

| Source Workbook | Key Data | Required Sheets |
|-----------------|----------|-----------------|
| **A.5.37.1 Procedure Inventory** | Procedure list, approval status, categories | Procedure_Inventory, Category_Summary |
| **A.5.37.2 Quality Assessment** | Quality scores, dimension ratings, gaps | Quality_Scores, Gap_Analysis, Dimension_Summary |
| **A.5.37.3 Review Tracking** | Review status, change requests, escalations | Review_Schedule, Change_Requests, Metrics_Summary |

### Data Currency Requirements

| Source | Maximum Age | Refresh Before |
|--------|-------------|----------------|
| Procedure Inventory | 7 days | Dashboard refresh |
| Quality Assessment | 7 days | Dashboard refresh |
| Review Tracking | 7 days | Dashboard refresh |

### Access Requirements

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| **Source Workbooks** | Read | Pull data for dashboard |
| **Dashboard Workbook** | Edit | Update dashboard data |
| **Report Distribution** | Send | Distribute reports |
| **Evidence Repository** | Write | Store dashboard snapshots |

---

## Dashboard Views

### Executive Summary View

High-level metrics designed for quick review by senior management:

| Element | Content | Update Frequency |
|---------|---------|------------------|
| **Overall Compliance Score** | Single percentage summarising overall status | Weekly |
| **Traffic Light Indicators** | Green/Yellow/Red for each major metric | Weekly |
| **Critical Issues Count** | Number of items requiring executive attention | Weekly |
| **Trend Arrows** | Direction of change from previous period | Monthly |
| **Period Summary** | Brief narrative of key changes | Monthly |

### Category Performance View

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

### Quality Deep-Dive View

Detailed quality analysis:

| Element | Content |
|---------|---------|
| **Rating Distribution** | Count and percentage by rating (Excellent/Good/Adequate/Needs Improvement/Poor) |
| **Dimension Breakdown** | Average scores for each quality dimension |
| **Category Comparison** | Quality scores compared across categories |
| **Improvement Trends** | Quality score changes over time |

### Review Compliance View

Procedure currency status:

| Element | Content |
|---------|---------|
| **Status Distribution** | Count by Current/Due Soon/Overdue |
| **Criticality Breakdown** | Review status by procedure criticality |
| **Overdue List** | Top 10 most overdue procedures |
| **Upcoming Reviews** | Reviews due in next 30 days |

### Gap Remediation View

Gap management status:

| Element | Content |
|---------|---------|
| **Gap Status Summary** | Open/In Progress/Closed counts |
| **Severity Distribution** | Gaps by Critical/High/Medium/Low |
| **Aging Analysis** | Average age of open gaps |
| **Closure Trend** | Gap closure rate over time |
| **Overdue Gaps** | Gaps past remediation target date |

### Change Activity View

Procedure change metrics:

| Element | Content |
|---------|---------|
| **CR Volume Trend** | Change requests over time |
| **Category Breakdown** | CRs by Administrative/Minor/Major/Emergency |
| **Cycle Time Metrics** | Average time from submission to implementation |
| **Approval Rate** | Approved vs rejected change requests |

---

## Key Performance Indicators

### Primary KPIs

| KPI | Definition | Formula | Target |
|-----|------------|---------|:------:|
| **Overall Compliance Score** | Weighted composite of all metrics | See formula below | ≥95% |
| **Procedure Coverage** | Procedures documented vs required | (Documented/Required) × 100 | 100% |
| **Approval Rate** | Procedures with valid approval | (Approved/Total) × 100 | 100% |
| **Review Currency** | Procedures reviewed within cycle | (Current/Total) × 100 | ≥95% |
| **Average Quality Score** | Mean quality score across inventory | SUM(Scores)/COUNT(Procedures) | ≥4.0 |
| **Open Gap Count** | Total open gaps | COUNT(Status="Open") | 0 |

### Overall Compliance Score Formula

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

### Secondary KPIs

| KPI | Definition | Target |
|-----|------------|:------:|
| CR Approval Rate | Change requests approved vs total | Track trend |
| CR Cycle Time (Minor) | Days from submission to implementation | ≤5 days |
| CR Cycle Time (Major) | Days from submission to implementation | ≤14 days |
| Communication Acknowledgement | Acknowledgement rate for notifications | ≥90% |
| Training Completion | Training completion for major changes | 100% |
| Zero L3 Escalations | Count of L3 escalations | 0 |

### Trend Indicators

| Indicator | Meaning |
|-----------|---------|
| ↑ Improving | Current period better than previous |
| → Stable | No significant change |
| ↓ Declining | Current period worse than previous |

Trend calculation: Compare current period to previous period (month-over-month or quarter-over-quarter).

---

## Completion Walkthrough

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

## Data Refresh Process

### Manual Refresh Procedure

1. **Open Source Workbooks**: Open all three source workbooks (read-only)
2. **Open Dashboard Workbook**: Open the dashboard for editing
3. **Check Links**: Excel > Data > Edit Links > Check status
4. **Update Links**: Click "Update Values" for each linked workbook
5. **Refresh Pivot Tables**: Right-click each pivot > Refresh
6. **Verify Calculations**: Spot-check key metrics against source
7. **Update Timestamp**: Update Last_Refreshed date in Data_Sources sheet
8. **Save Dashboard**: Save and close

### Automated Refresh (If Configured)

| Setting | Value |
|---------|-------|
| Refresh Schedule | Daily at 06:00 |
| Trigger | Source workbook modification |
| Notification | Email on completion or error |
| Log Location | [System path] |

### Troubleshooting Data Issues

| Issue | Possible Cause | Resolution |
|-------|----------------|------------|
| #REF! errors | Source file moved/renamed | Update file path in Data_Sources |
| #VALUE! errors | Data type mismatch | Check source data format |
| Stale data | Links not refreshed | Force refresh of external links |
| Missing data | New procedures not included | Update source workbook ranges |
| Incorrect totals | Formula range incomplete | Extend formula ranges |

---

## Reporting and Export

### Standard Reports

| Report | Content | Frequency | Distribution |
|--------|---------|-----------|--------------|
| **Executive Summary** | Sheet 1 as PDF | Monthly | CISO, Management |
| **Category Report** | Sheet 2 as PDF | Quarterly | Department Heads |
| **Gap Status Report** | Sheet 5 as PDF | Weekly | ISM, Gap Owners |
| **Audit Evidence Package** | All sheets as PDF | On request | Auditors |

### Export Procedure

1. Select sheet to export
2. File > Print > Save as PDF
3. Name file: `ISMS-A.5.37.4_[ReportName]_YYYYMMDD.pdf`
4. Store in: ISMS Evidence Library/A.5.37/Dashboard Reports/
5. Distribute via secure email or SharePoint

### Management Review Input

For ISMS Management Review (ISO 27001 Clause 9.3), provide:

| Input Item | Dashboard Source |
|------------|------------------|
| Performance of information security processes | Overall Compliance Score, KPIs |
| Status of corrective actions | Gap Tracking sheet |
| Changes affecting the ISMS | Change Activity trends |
| Opportunities for improvement | Gap analysis, quality scores |

---

## Evidence Collection

### Evidence Requirements

| Evidence Type | Format | Retention |
|---------------|--------|-----------|
| **Dashboard Snapshots** | PDF export of Executive_Dashboard | 3 years |
| **Trend Data** | Excel snapshot of Trend_History | Permanent |
| **Management Reports** | PDF exports per distribution | 3 years |
| **Audit Evidence Packages** | Complete PDF bundle | Per audit cycle |

### Evidence Storage

| Evidence Type | Storage Location | Naming Convention |
|---------------|------------------|-------------------|
| Monthly snapshots | ISMS Evidence Library/A.5.37/Dashboard/ | A.5.37.4_Dashboard_YYYYMM.pdf |
| Quarterly reports | ISMS Evidence Library/A.5.37/Reports/ | A.5.37.4_QtrReport_YYYYQN.pdf |
| Audit packages | ISMS Evidence Library/Audits/[Year]/ | A.5.37_AuditEvidence_YYYYMMDD.pdf |

### Audit Evidence Checklist

For auditors requesting evidence of A.5.37 compliance:

- [ ] Current Executive Dashboard showing compliance score ≥95%
- [ ] Category Analysis showing all categories meeting targets
- [ ] Review Status showing ≤5% overdue reviews
- [ ] Gap Tracking showing gap remediation progress
- [ ] Trend History showing improvement or stability over 12 months
- [ ] Management review meeting minutes referencing dashboard metrics

---

## Common Pitfalls

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

## Quality Checklist

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

## Review and Approval

### Dashboard Review Workflow

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

### Approval Authorities

| Dashboard Activity | Owner | Reviewer |
|--------------------|-------|----------|
| Weekly refresh | ISM or delegate | Self-check |
| Monthly report | ISM | CISO (optional) |
| Audit evidence package | ISM | CISO |
| Methodology changes | ISM | CISO approval required |

### Sign-off Record

| Activity | Name | Date |
|----------|------|------|
| Dashboard Refresh Completed | | |
| Quality Check Passed | | |
| Distribution Authorised | | |

---

## Related Controls

### Primary Dependencies

| Control | Relationship | Integration |
|---------|--------------|-------------|
| **A.5.37.1** | Procedure Inventory | Source of procedure counts and categories |
| **A.5.37.2** | Quality Assessment | Source of quality scores and gaps |
| **A.5.37.3** | Review Tracking | Source of review status and change metrics |
| **A.5.1** | Information Security Policy | Policy framework governance |

### Downstream Consumers

| Consumer | What They Use |
|----------|---------------|
| **Management Review** | Overall compliance score, trend data |
| **Internal Audit** | Full dashboard as control evidence |
| **Risk Management** | Gap data for risk assessment |
| **Improvement Planning** | Trend analysis for improvement priorities |

### Related ISMS Dashboards

| Dashboard | Relationship |
|-----------|--------------|
| **ISMS Master Dashboard** | A.5.37.4 feeds overall compliance score |
| **Control Effectiveness Dashboard** | A.5.37.4 provides procedure control data |
| **Gap Register Dashboard** | A.5.37.4 contributes procedure gaps |

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
