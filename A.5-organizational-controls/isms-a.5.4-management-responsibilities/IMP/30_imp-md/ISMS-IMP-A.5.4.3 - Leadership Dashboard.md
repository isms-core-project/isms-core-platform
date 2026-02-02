# ISMS-IMP-A.5.4.3 - Leadership Dashboard

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.3 |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

## PART I: USER COMPLETION GUIDE

### 1. Assessment Overview

#### 1.1 Purpose

This dashboard consolidates management security leadership metrics for executive reporting and ISMS management review. It aggregates data from the Management Commitment Assessment (A.5.4.1) and Compliance Oversight Tracker (A.5.4.2) into executive-friendly summaries.

#### 1.2 Scope

Dashboard reporting covers:
- Organisation-wide leadership metrics
- Department-level breakdown
- Quarter-over-quarter trends
- Action item tracking for improvement initiatives

#### 1.3 Target Audience

| Audience | Use Case |
|----------|----------|
| Executive Management | Governance oversight, resource decisions |
| CISO | ISMS management review input |
| Department Heads | Department performance tracking |
| Internal Audit | Control effectiveness evidence |

#### 1.4 Why This Matters

**The Executive Visibility Problem**: Without a consolidated dashboard, executives receive fragmented security information:
- Training data from HR
- Incident data from Security
- Access review data from IT
- No unified view of management effectiveness

**This dashboard solves that problem** by aggregating data from A.5.4.1 (Commitment Assessment), A.5.4.2 (Compliance Oversight), and A.5.4.4 (Security Culture Survey) into executive-friendly summaries.

**Business Value**:
- **Decision Support**: Executives can allocate resources to underperforming areas
- **Trend Visibility**: Quarter-over-quarter trends reveal whether interventions are working
- **Accountability**: Department-level breakdown enables targeted discussions
- **Audit Readiness**: Consolidated evidence demonstrates management oversight to auditors

**Real-World Impact**:
- Organisations with executive dashboards respond to security gaps 40% faster
- Department heads shown comparative data improve performance by 15-25%
- Trend visibility enables proactive intervention before metrics go critical

**The ISMS Copilot Connection**: During management review (ISO 27001 Clause 9.3), executives must evaluate ISMS performance. This dashboard provides the data they need:
- KPIs showing control effectiveness
- Action items requiring management decisions
- Trends indicating direction of travel

### 2. Prerequisites

Before populating this dashboard, ensure:

- [ ] ISMS-IMP-A.5.4.1 (Management Commitment) completed for current period
- [ ] ISMS-IMP-A.5.4.2 (Compliance Oversight) current through quarter-end
- [ ] ISMS-IMP-A.5.4.4 (Security Culture Survey) results available (if annual survey period)
- [ ] Prior quarter/year data available for trend analysis
- [ ] Department structure current in HR system
- [ ] Executive Management meeting date confirmed (for report delivery)
- [ ] Action item owners identified for remediation tracking

**Data Quality Verification**:

Before consolidating data, verify source workbook quality:

| Source | Verification Check | Pass Criteria |
|--------|-------------------|---------------|
| A.5.4.1 | Summary Scores sheet populated | All managers have scores |
| A.5.4.1 | Manager Inventory complete | Count matches HR system |
| A.5.4.2 | Quarterly Summary populated | Current quarter complete |
| A.5.4.2 | Escalation Triggers current | All escalations have status |
| A.5.4.4 | Executive Summary complete | Overall Culture Score calculated |
| A.5.4.4 | Response rate acceptable | ≥80% participation |

**Timing Considerations**:

| Data Source | Availability | Dashboard Update |
|-------------|--------------|------------------|
| A.5.4.1 Commitment Assessment | Semi-annual (Q2, Q4) | Update semi-annually |
| A.5.4.2 Compliance Oversight | Quarterly | Update quarterly |
| A.5.4.4 Culture Survey | Annual (Q4) | Update annually |
| Trend Analysis | Historical data | Update quarterly |
| Action Items | Continuous | Update monthly |

### 3. Workbook Structure

| Sheet | Purpose | Update Frequency |
|-------|---------|------------------|
| **Instructions** | Guidance and data sources | Reference |
| **Executive Summary** | High-level KPIs for leadership | Quarterly |
| **By Department** | Department-level metrics | Quarterly |
| **Trend Analysis** | Quarter-over-quarter trends | Quarterly |
| **Action Items** | Improvement actions tracking | Continuous |

### 4. Completion Walkthrough

#### Step 1: Executive Summary

Populate key metrics from source workbooks:

| Metric | Source | Target |
|--------|--------|--------|
| Overall Commitment Score | A.5.4.1 Summary average | ≥70% min, ≥85% target |
| Managers Assessed | A.5.4.1 Manager Inventory count | 100% of managers |
| Managers Meeting Target | A.5.4.1 Summary (≥70% scores) | 100% |
| Training Oversight Compliance | A.5.4.2 Training Oversight average | ≥90% min, ≥95% target |
| Access Reviews Completed | A.5.4.2 Access Reviews (Yes count) | 100% |
| Avg Policy Violation Response | A.5.4.2 Policy Violations average | ≤5 days min, ≤3 days target |

Set **Overall Status** based on:
- **EXCEEDS**: All metrics at or above target
- **MEETS**: All metrics at or above minimum
- **BELOW**: Any metric below minimum

#### Step 2: By Department

For each department, aggregate:
1. **Manager_Count**: Number of managers in department
2. **Avg_Commitment_Score**: Mean from A.5.4.1
3. **Training_Compliance**: Mean from A.5.4.2 Training Oversight
4. **Violations_Handled**: Count from A.5.4.2 Policy Violations
5. **Access_Reviews**: Completion percentage from A.5.4.2
6. **Status**: Exceeds/Meets/Below/N/A
7. **Notes**: Key observations or concerns

#### Step 3: Trend Analysis

Track six key metrics across quarters:

| Metric | Q1 | Q2 | Q3 | Q4 | YoY Change | Trend |
|--------|:--:|:--:|:--:|:--:|:----------:|:-----:|
| Overall Commitment Score (%) | | | | | | |
| Managers at Target (%) | | | | | | |
| Training Oversight (%) | | | | | | |
| Access Review Completion (%) | | | | | | |
| Violation Response Time (days) | | | | | | |
| Security Culture Survey Score | | | | | | |

Set **Trend** as: Improving, Stable, or Declining

#### Step 4: Action Items

Track improvement actions:
1. Generate **Action_ID** (format: MGT-YYYY-NNN)
2. Document the **Finding** that triggered the action
3. Define **Action_Required** (specific, measurable)
4. Assign **Owner** with accountability
5. Set realistic **Due_Date**
6. Update **Status**: Open, In Progress, Completed, Overdue, Cancelled
7. Record **Completion_Date** and **Evidence** when closed

### 5. Worked Examples

#### Example A: Executive Summary - High-Performing Organisation

| Key Metric | Current | Minimum | Target | Status |
|------------|:-------:|:-------:|:------:|--------|
| Overall Commitment Score | 82% | 70% | 85% | ✅ MEETS |
| Managers Assessed | 45/45 | 100% | 100% | ✅ MEETS |
| Managers Meeting Target | 42/45 | 100% | 100% | ⚠️ BELOW |
| Training Oversight Compliance | 93% | 90% | 95% | ✅ MEETS |
| Access Reviews Completed | 100% | 100% | 100% | ✅ MEETS |
| Avg Policy Violation Response | 4 days | ≤5 days | ≤3 days | ⚠️ MEETS MIN |

**Overall Status**: **MEETS** (all metrics at or above minimum)

**Key Insights**:
- 3 managers below commitment target require attention
- Training oversight strong but policy response could improve
- Recommend focus on response time for next quarter

---

#### Example B: Department Breakdown - Identifying Outliers

| Department | Managers | Avg Commitment | Training | Violations | Access Reviews | Status |
|------------|:--------:|:--------------:|:--------:|:----------:|:--------------:|--------|
| Engineering | 8 | 85% | 97% | 2 | 100% | ✅ Exceeds |
| Finance | 6 | 88% | 94% | 1 | 100% | ✅ Exceeds |
| Sales | 10 | 62% | 78% | 8 | 75% | ❌ Below |
| Marketing | 5 | 79% | 91% | 3 | 100% | ✅ Meets |
| Operations | 8 | 75% | 89% | 4 | 100% | ⚠️ Meets |
| IT | 8 | 83% | 95% | 2 | 100% | ✅ Exceeds |

**Analysis**:
- **Sales** is significantly underperforming across all metrics
  - Root cause investigation required
  - Consider structural issues (high turnover, new managers, workload)
- **Operations** is borderline - monitor closely next quarter
- **Engineering, Finance, IT** are strong performers - share best practices

---

#### Example C: Trend Analysis Showing Improvement

| Metric | Q1 | Q2 | Q3 | Q4 | YoY Change | Trend |
|--------|:--:|:--:|:--:|:--:|:----------:|:-----:|
| Overall Commitment Score (%) | 68 | 72 | 78 | 82 | +14 | ↑ Improving |
| Managers at Target (%) | 78 | 82 | 88 | 93 | +15 | ↑ Improving |
| Training Oversight (%) | 85 | 88 | 91 | 93 | +8 | ↑ Improving |
| Access Review Completion (%) | 92 | 95 | 98 | 100 | +8 | ↑ Improving |
| Violation Response Time (days) | 12 | 8 | 6 | 4 | -8 | ↑ Improving |
| Security Culture Survey Score | 3.2 | - | - | 3.8 | +0.6 | ↑ Improving |

**Executive Narrative**: "All metrics show positive year-over-year trends. The improvement in Violation Response Time (from 12 days to 4 days) reflects the escalation process implemented in Q2. Security Culture Survey score improved by 0.6 points, indicating the training investments are perceived positively by staff."

---

#### Example D: Trend Analysis Showing Concerns

| Metric | Q1 | Q2 | Q3 | Q4 | YoY Change | Trend |
|--------|:--:|:--:|:--:|:--:|:----------:|:-----:|
| Overall Commitment Score (%) | 82 | 78 | 74 | 70 | -12 | ↓ Declining |
| Managers at Target (%) | 95 | 90 | 85 | 78 | -17 | ↓ Declining |
| Training Oversight (%) | 94 | 91 | 88 | 84 | -10 | ↓ Declining |
| Access Review Completion (%) | 100 | 95 | 90 | 85 | -15 | ↓ Declining |
| Violation Response Time (days) | 4 | 6 | 9 | 14 | +10 | ↓ Declining |
| Security Culture Survey Score | 3.9 | - | - | 3.2 | -0.7 | ↓ Declining |

**Executive Narrative**: "All metrics show concerning year-over-year decline. The deterioration began in Q2 coinciding with the organisational restructure and 15% reduction in security team headcount. Immediate intervention recommended:
1. Review manager workload capacity
2. Reinstate security team resources
3. Simplify compliance processes where possible
4. Executive communication emphasising security priority"

---

#### Example E: Action Items Tracking

| Action_ID | Finding | Action Required | Owner | Due Date | Status |
|-----------|---------|-----------------|-------|----------|--------|
| MGT-2026-001 | Sales dept below target | Targeted management training for Sales leadership | HR Director | 28-Feb | In Progress |
| MGT-2026-002 | Response time at minimum | Implement automated violation alerts | IT Security | 15-Mar | Open |
| MGT-2026-003 | 3 managers failed commitment | Individual coaching sessions | CISO | 31-Jan | Completed |
| MGT-2026-004 | Culture survey score dropped | Investigate cause through focus groups | HR/Security | 15-Feb | In Progress |
| MGT-2026-005 | Access review completion below 100% | Delegate process for managers on leave | IAM Team | 01-Feb | Completed |

**Tracking Metrics**:
- Total Actions: 5
- Completed: 2 (40%)
- In Progress: 2 (40%)
- Open: 1 (20%)
- Overdue: 0 (0%)

### 6. Dashboard Presentation Tips

#### For Executive Management Meetings

**Do**:
- Lead with headline status (Overall: MEETS/EXCEEDS/BELOW)
- Highlight 2-3 key trends (positive or negative)
- Focus discussion on action items requiring decisions
- Show comparison to previous periods

**Don't**:
- Overwhelm with raw data (executives want insights, not numbers)
- Hide negative trends (executives need truth to make decisions)
- Present without recommendations
- Skip the "So what?" analysis

**Recommended Format** (15-minute presentation):
1. **Headline** (2 min): Overall status, key metrics summary
2. **Trends** (3 min): What's improving, what's declining
3. **Spotlight** (5 min): One deep-dive on area needing attention
4. **Actions** (3 min): Status of open items, new actions proposed
5. **Decision** (2 min): Specific asks requiring executive approval

#### Handling Difficult Questions

| Question | Response Approach |
|----------|-------------------|
| "Why are we below target?" | Present root cause analysis from source workbooks |
| "When will this improve?" | Reference action plan timeline; avoid overpromising |
| "How does this compare to industry?" | Note that internal trends matter more than benchmarks |
| "What resources do you need?" | Be specific about budget/headcount asks |
| "Who is responsible?" | Focus on systemic issues, not individuals (in executive forum) |

### 7. Evidence Collection

| Dashboard Element | Evidence Required |
|-------------------|-------------------|
| Executive Summary | Source workbook screenshots, calculation methodology |
| By Department | Department roster, aggregation formulas |
| Trend Analysis | Historical workbooks, quarter-end snapshots |
| Action Items | Action completion artifacts, owner sign-off |

**Evidence Storage**: `[SharePoint/Evidence Library]/A.5.4/Leadership-Dashboard/[Year]/`

**Evidence Retention Schedule**:
| Document Type | Retention Period | Archive After |
|--------------|------------------|---------------|
| Dashboard workbooks | 5 years | 1 year |
| Source workbook exports | 3 years | Current + 2 prior years |
| Action item evidence | 5 years | Upon closure + 5 years |
| Executive presentations | 5 years | 1 year |
| Meeting minutes | 7 years | 2 years |

### 8. Common Pitfalls

❌ **MISTAKE**: Presenting dashboard without current source data
✅ **CORRECT**: Verify A.5.4.1 and A.5.4.2 are current before dashboard update

❌ **MISTAKE**: Manually entering values that should be calculated
✅ **CORRECT**: Use formulas linked to source workbooks where possible

❌ **MISTAKE**: Hiding unfavourable trends from executives
✅ **CORRECT**: Present accurate data; executives need truth to make decisions

❌ **MISTAKE**: Leaving action items without clear owners
✅ **CORRECT**: Every action must have a named, accountable owner

❌ **MISTAKE**: Not closing completed action items formally
✅ **CORRECT**: Update status, record completion date, link to evidence

❌ **MISTAKE**: Presenting raw data without context
✅ **CORRECT**: Add notes explaining significant changes or anomalies

❌ **MISTAKE**: Using inconsistent time periods across metrics
✅ **CORRECT**: Align all metrics to the same reporting period

❌ **MISTAKE**: Omitting departments with poor performance
✅ **CORRECT**: Include all departments; highlight areas needing attention

❌ **MISTAKE**: Presenting dashboard without pre-briefing the CISO
✅ **CORRECT**: Brief CISO on content before executive meeting to avoid surprises

❌ **MISTAKE**: Using different definitions of metrics across quarters
✅ **CORRECT**: Document metric definitions; apply consistently for trend validity

### 9. Quality Checklist

Before presenting to executive management:

- [ ] All source workbooks (A.5.4.1, A.5.4.2) current and complete
- [ ] Executive Summary metrics accurately calculated
- [ ] All departments represented in By Department sheet
- [ ] Trend Analysis includes prior periods for comparison
- [ ] YoY Change and Trend columns populated
- [ ] All open Action Items have owners and due dates
- [ ] Overdue actions flagged and escalated
- [ ] Dashboard saved with correct naming convention
- [ ] Executive talking points prepared for key findings

### 10. Review and Approval

| Role | Responsibility | Timing |
|------|----------------|--------|
| Security Analyst | Compile and validate data | Q+5 business days |
| Security Manager | Review accuracy and completeness | Q+7 business days |
| CISO | Approve for management review | Q+10 business days |
| Executive Management | Review in management review meeting | Per ISMS calendar |

### 11. Audit Preparation

#### Stage 2 Audit Evidence Requirements

When auditors review management leadership, prepare:

**Documentation Evidence**:
- Current dashboard workbook plus 3 prior quarters
- Source workbooks (A.5.4.1, A.5.4.2, A.5.4.4)
- Executive meeting minutes showing dashboard review
- Action item closure evidence

**Demonstration Requests** (be prepared to show):
1. How data flows from source workbooks to dashboard
2. How department breakdown is calculated
3. How trend analysis informs decisions
4. How action items are tracked to closure

**Common Audit Questions**:

| Question | Evidence to Provide |
|----------|---------------------|
| "How do executives review security performance?" | Meeting minutes, dashboard presentation materials |
| "Show me how you track improvement actions" | Action Items sheet with evidence links |
| "What happens when a department underperforms?" | Trend Analysis + corresponding action items |
| "How frequently is this updated?" | Workbook file dates showing quarterly updates |

---

## PART II: TECHNICAL SPECIFICATION

### 12. Workbook Technical Details

#### 12.1 File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.4.3_Leadership_Dashboard_YYYYMMDD.xlsx` |
| Generator | `generate_a54_3_leadership_dashboard.py` |
| Sheets | 5 |
| Protected | No |

#### 12.2 Sheet Specifications

**Sheet 1: Instructions**
- Purpose: Data sources, workflow guidance
- Rows: ~20
- No data entry required

**Sheet 2: Executive Summary**

| Row | Content | Type |
|:---:|---------|------|
| 1 | Title (merged A1:E1) | Header |
| 2 | Report Date | Text |
| 4 | Key Metric headers | Header row |
| 5-10 | Metric rows | Data + formulas |
| 12 | Overall Status | Input (MEETS/BELOW/EXCEEDS) |

**Metrics Table:**

| Column | Header | Width |
|:------:|--------|:-----:|
| A | Key Metric | 35 |
| B | Current | 15 |
| C | Minimum | 12 |
| D | Target | 12 |

**Sheet 3: By Department**

| Column | Header | Width | Type |
|:------:|--------|:-----:|------|
| A | Department | 15 | Text |
| B | Manager_Count | 15 | Number |
| C | Avg_Commitment_Score | 20 | Percentage |
| D | Training_Compliance | 18 | Percentage |
| E | Violations_Handled | 18 | Number |
| F | Access_Reviews | 15 | Percentage |
| G | Status | 10 | List (Exceeds, Meets, Below, N/A) |
| H | Notes | 30 | Text |

**Pre-populated Departments:**
Executive, Finance, IT, Operations, HR, Legal, Sales, Marketing, Engineering, Support

**Sheet 4: Trend Analysis**

| Column | Header | Width | Type |
|:------:|--------|:-----:|------|
| A | Metric | 35 | Text |
| B | Q1 | 12 | Number |
| C | Q2 | 12 | Number |
| D | Q3 | 12 | Number |
| E | Q4 | 12 | Number |
| F | YoY_Change | 12 | Formula |
| G | Trend | 15 | List (Improving, Stable, Declining) |

**Pre-populated Metrics:**
1. Overall Commitment Score (%)
2. Managers at Target (%)
3. Training Oversight (%)
4. Access Review Completion (%)
5. Violation Response Time (days)
6. Security Culture Survey Score

**Sheet 5: Action Items**

| Column | Header | Width | Type |
|:------:|--------|:-----:|------|
| A | Action_ID | 12 | Text |
| B | Finding | 35 | Text |
| C | Action_Required | 40 | Text |
| D | Owner | 20 | Text |
| E | Due_Date | 12 | Date |
| F | Status | 12 | List |
| G | Completion_Date | 15 | Date |
| H | Evidence | 30 | Text |

**Status Values:** Open, In Progress, Completed, Overdue, Cancelled

#### 12.3 Styling

| Element | Style |
|---------|-------|
| Title | Bold 14pt, centered |
| Headers | White text (#FFFFFF), Blue fill (#2F5496), Bold |
| Metric cells | Light green fill (#E2EFDA) |
| Input cells | Yellow fill (#FFFFCC) |
| All data cells | Thin black border |

### 13. Data Sources

| Dashboard Element | Source Workbook | Source Sheet |
|-------------------|-----------------|--------------|
| Overall Commitment Score | A.5.4.1 | Summary Scores (average) |
| Managers Assessed | A.5.4.1 | Manager Inventory (count) |
| Managers Meeting Target | A.5.4.1 | Summary Scores (≥70% count) |
| Training Oversight | A.5.4.2 | Training Oversight (average) |
| Access Reviews | A.5.4.2 | Access Reviews (Yes %) |
| Violation Response | A.5.4.2 | Policy Violations (avg days) |
| Culture Survey | A.5.4.4 | Executive Summary |

### 14. Calculation Formulas

**YoY Change** (Trend Analysis sheet, Column F):
```
=IF(AND(B{row}>0, E{row}>0), E{row}-B{row}, "-")
```
Where B = Q1 value, E = Q4 value

**Department Status** (By Department sheet, Column G):
```
=IF(C{row}>=85%, "Exceeds", IF(C{row}>=70%, "Meets", IF(C{row}>0, "Below", "N/A")))
```

**Overall Status Logic**:
- EXCEEDS: All 6 metrics at or above Target
- MEETS: All 6 metrics at or above Minimum
- BELOW: Any metric below Minimum

**Action Item Status Aging**:
```
=IF(E{row}<TODAY(), IF(F{row}<>"Completed", "Overdue", F{row}), F{row})
```
Automatically flags items past due date as "Overdue"

### 15. Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| A.5.4.1 Workbook | Commitment scores | Manual consolidation quarterly |
| A.5.4.2 Workbook | Training, violations, access reviews | Manual consolidation quarterly |
| A.5.4.4 Workbook | Culture survey scores | Manual consolidation annually |
| SharePoint | Evidence storage | File links in Action Items sheet |
| Calendar | Management review meetings | Dashboard timed to meeting schedule |

#### 15.1 Data Flow Diagram

```
┌──────────────────────────────────────────────────────────────────────┐
│                    A.5.4 DATA CONSOLIDATION FLOW                      │
└──────────────────────────────────────────────────────────────────────┘

┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
│ ISMS-IMP-A.5.4.1    │  │ ISMS-IMP-A.5.4.2    │  │ ISMS-IMP-A.5.4.4    │
│ Management          │  │ Compliance          │  │ Security Culture    │
│ Commitment          │  │ Oversight           │  │ Survey              │
│                     │  │                     │  │                     │
│ ─ Summary Scores    │  │ ─ Training %        │  │ ─ Overall Score     │
│ ─ Manager Count     │  │ ─ Violations        │  │ ─ Category Scores   │
│ ─ Department Data   │  │ ─ Response Time     │  │ ─ Response Rate     │
│                     │  │ ─ Access Reviews    │  │                     │
└────────┬────────────┘  └────────┬────────────┘  └────────┬────────────┘
         │                        │                        │
         │    [Semi-annual]       │    [Quarterly]         │  [Annual]
         │                        │                        │
         └────────────────────────┼────────────────────────┘
                                  │
                                  ▼
         ┌────────────────────────────────────────────────────┐
         │              ISMS-IMP-A.5.4.3                       │
         │           LEADERSHIP DASHBOARD                      │
         │                                                     │
         │  ┌──────────────────┐  ┌──────────────────┐        │
         │  │ Executive        │  │ By Department    │        │
         │  │ Summary          │  │                  │        │
         │  │ ─ 6 KPIs        │  │ ─ 10 Depts       │        │
         │  │ ─ Status        │  │ ─ 6 Metrics      │        │
         │  └──────────────────┘  └──────────────────┘        │
         │                                                     │
         │  ┌──────────────────┐  ┌──────────────────┐        │
         │  │ Trend Analysis   │  │ Action Items     │        │
         │  │ ─ 4 Quarters    │  │ ─ Finding        │        │
         │  │ ─ YoY Change    │  │ ─ Owner          │        │
         │  │ ─ Trend         │  │ ─ Status         │        │
         │  └──────────────────┘  └──────────────────┘        │
         └───────────────────────────┬────────────────────────┘
                                     │
                                     ▼
         ┌────────────────────────────────────────────────────┐
         │              EXECUTIVE MANAGEMENT                   │
         │                                                     │
         │  ─ Quarterly Management Review (ISO 27001 Cl 9.3)  │
         │  ─ Resource allocation decisions                    │
         │  ─ Action item approval                             │
         │  ─ Trend assessment and strategic direction         │
         └────────────────────────────────────────────────────┘
```

#### 15.2 Consolidation Procedures

**Executive Summary Consolidation**:

| Metric | Source | Calculation |
|--------|--------|-------------|
| Overall Commitment Score | A.5.4.1 Summary Scores | Average of all manager scores |
| Managers Assessed | A.5.4.1 Manager Inventory | Count of rows with data |
| Managers Meeting Target | A.5.4.1 Summary Scores | Count where Overall ≥70% |
| Training Oversight Compliance | A.5.4.2 Training Oversight | Average of Completion_Rate column |
| Access Reviews Completed | A.5.4.2 Access Reviews | Count "Yes" ÷ Total × 100% |
| Avg Policy Violation Response | A.5.4.2 Policy Violations | Average of (Response_Date - Date_Reported) |

**Department Consolidation**:

For each department in A.5.4.1 and A.5.4.2:
1. Filter source data by Department column
2. Calculate department averages for each metric
3. Aggregate into By Department sheet
4. Apply status logic (Exceeds/Meets/Below)
5. Add notes for any departments requiring attention

**Trend Analysis Consolidation**:

1. Retrieve current quarter data from source workbooks
2. Enter in appropriate Q column (Q1-Q4)
3. Formula calculates YoY Change automatically
4. Manually set Trend based on:
   - Improving: YoY Change positive by >5% or >0.3 points
   - Stable: YoY Change within ±5% or ±0.3 points
   - Declining: YoY Change negative by >5% or >0.3 points

#### 15.3 Timing and Dependencies

```
QUARTERLY DASHBOARD UPDATE TIMELINE
────────────────────────────────────────────────────────────────────────

Quarter End (Day 0)
       │
       ▼
┌──────────────────────────────────────────────────────────────────────┐
│ Day 1-3: Source Data Freeze                                          │
│ ─ A.5.4.1 finalised (if assessment quarter)                         │
│ ─ A.5.4.2 monthly data closed out                                   │
│ ─ A.5.4.4 results available (Q4 only)                               │
└──────────────────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────────────────┐
│ Day 4-5: Dashboard Data Consolidation                                │
│ ─ Security Analyst compiles from source workbooks                   │
│ ─ Executive Summary metrics calculated                              │
│ ─ By Department breakdown completed                                  │
│ ─ Trend Analysis updated                                            │
│ ─ Action Items reviewed (status, new items)                         │
└──────────────────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────────────────┐
│ Day 6-7: Validation and Quality Check                                │
│ ─ Security Manager reviews for accuracy                             │
│ ─ Cross-check against source workbooks                              │
│ ─ Flag any anomalies or data quality issues                         │
└──────────────────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────────────────┐
│ Day 8-10: CISO Review and Approval                                   │
│ ─ CISO reviews dashboard content                                    │
│ ─ Executive narrative drafted                                        │
│ ─ Presentation materials prepared                                    │
│ ─ Dashboard approved for management review                          │
└──────────────────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────────────────┐
│ Management Review Meeting (per ISMS Calendar)                        │
│ ─ Dashboard presented to Executive Management                        │
│ ─ Trends discussed and decisions made                                │
│ ─ Action items assigned for follow-up                               │
│ ─ Meeting minutes documented                                         │
└──────────────────────────────────────────────────────────────────────┘
```

#### 15.4 Management Review Integration

This dashboard provides input to ISO 27001 Clause 9.3 Management Review:

| Management Review Input | Dashboard Source |
|------------------------|------------------|
| Status of actions from previous reviews | Action Items sheet (prior quarter items) |
| Changes in external and internal issues | Trend Analysis (declining metrics indicate changes) |
| Information on security performance | Executive Summary (all 6 KPIs) |
| Results of risk assessments | By Department (highlights risk areas) |
| Opportunities for improvement | Action Items (proposed new actions) |

**Meeting Agenda Integration**:

```
MANAGEMENT REVIEW AGENDA - ISMS PERFORMANCE
─────────────────────────────────────────────
1. Review of prior action items                    → Action Items sheet
2. Security leadership metrics overview            → Executive Summary
3. Department performance analysis                 → By Department
4. Trend assessment and direction                 → Trend Analysis
5. New action items and decisions                  → Discussion outcomes
6. Resource allocation (if needed)                → Based on findings
```

### 16. Glossary of Terms

| Term | Definition |
|------|------------|
| **Overall Commitment Score** | Weighted average of manager security leadership scores from A.5.4.1 |
| **Managers Meeting Target** | Count of managers with Overall Commitment Score ≥70% |
| **Training Oversight Compliance** | Percentage of required training completed across manager teams |
| **Access Review Completion** | Percentage of scheduled access reviews fully completed |
| **Avg Policy Violation Response** | Mean number of business days from violation report to manager response |
| **Security Culture Survey Score** | Organisation-wide average from annual culture survey (scale 1.0-5.0) |
| **YoY Change** | Year-over-year change (Current Q4 minus Prior Q4) |
| **Trend** | Direction indicator: Improving (↑), Stable (→), Declining (↓) |

### 17. Automation Opportunities

| Process | Current State | Automation Potential | Priority |
|---------|---------------|---------------------|----------|
| Data consolidation | Manual copy/paste from source workbooks | Power Query links to source workbooks | High |
| Executive Summary calculation | Manual entry | Formulas linked to source workbooks | High |
| Department breakdown | Manual filtering and averaging | PivotTable with source workbook links | Medium |
| Trend graphing | Manual chart creation | Auto-updating charts with data ranges | Medium |
| Action item reminders | Manual tracking | Automated email alerts for due dates | Medium |
| Status indicators | Manual colour coding | Conditional formatting (already implemented) | Done |
| Meeting scheduling | Manual calendar invite | Recurring calendar with dashboard link | Low |

**Recommended Implementation Sequence**:
1. **Phase 1** (High priority): Power Query data connections to source workbooks
2. **Phase 2** (Medium priority): Auto-updating charts for trend visualisation
3. **Phase 3** (Optional): Email automation for action item reminders

**Constraints**:
- Automation must maintain audit trail (who changed what, when)
- Source workbook structure changes require link updates
- Executives may prefer static snapshots for meeting discussions

### 18. Version Control

**Dashboard Version Naming**:
```
ISMS-IMP-A.5.4.3_Leadership_Dashboard_[YYYYMMDD].xlsx
```

Example: `ISMS-IMP-A.5.4.3_Leadership_Dashboard_20260131.xlsx`

**Retention Requirements**:
- Current quarter: Active working file
- Prior 3 quarters: Archive (read-only)
- Prior years: 5-year retention per ISMS evidence policy

**Change Log** (maintain in Instructions sheet):

| Date | Changed By | Description |
|------|------------|-------------|
| 2026-01-31 | [Name] | Q4 2025 data consolidated |
| 2025-10-15 | [Name] | Q3 2025 data consolidated |
| ... | ... | ... |

### 19. Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.4 | Management Responsibilities | Parent policy |
| ISMS-IMP-A.5.4.1 | Management Commitment Assessment | Data source |
| ISMS-IMP-A.5.4.2 | Compliance Oversight Tracker | Data source |
| ISMS-IMP-A.5.4.4 | Security Culture Survey | Data source |
| ISMS-POL-A.5.35-36 | Compliance and Review | Management review input |

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-02 -->
