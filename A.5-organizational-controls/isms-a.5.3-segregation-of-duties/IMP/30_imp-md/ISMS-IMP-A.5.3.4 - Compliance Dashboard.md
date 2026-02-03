# ISMS-IMP-A.5.3.4 - Compliance Dashboard

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.3.4 |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.3 Segregation of Duties |
| **Parent Policy** | ISMS-POL-A.5.3 - Segregation of Duties |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Workbook Structure](#14-workbook-structure)
   - [1.5 Completion Walkthrough](#15-completion-walkthrough)
   - [1.6 Dashboard Refresh Process](#16-dashboard-refresh-process)
   - [1.7 Evidence Collection](#17-evidence-collection)
   - [1.8 Common Pitfalls](#18-common-pitfalls)
   - [1.9 Quality Checklist](#19-quality-checklist)
   - [1.10 Review and Approval](#110-review-and-approval)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Technical Details](#21-workbook-technical-details)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Conditional Formatting](#23-conditional-formatting)
   - [2.4 Formulas](#24-formulas)
   - [2.5 Integration Points](#25-integration-points)
   - [2.6 Related Documents](#26-related-documents)

---

# PART I: USER COMPLETION GUIDE

---

## 1.1 Assessment Overview

### Purpose

This workbook provides an executive-level dashboard consolidating all segregation of duties metrics from ISMS-IMP-A.5.3.1, A.5.3.2, and A.5.3.3. It enables management oversight, trend analysis, and audit-ready reporting of SoD compliance status.

The dashboard serves multiple purposes:
- **Executive Visibility**: Single-view summary of SoD compliance posture
- **Trend Analysis**: Track compliance improvement over time
- **KPI Tracking**: Monitor key performance indicators for SoD programme
- **Audit Readiness**: Provide consolidated evidence for Stage 2 audits
- **Management Reporting**: Support ISMS management review inputs

### Scope

The Compliance Dashboard aggregates data from:

| Source | Metrics Consolidated |
|--------|---------------------|
| A.5.3.1 SoD Matrix | Total roles, conflicts identified, resolution status |
| A.5.3.2 Conflict Analysis | Impact scores, prioritisation status, control effectiveness |
| A.5.3.3 Role-Function Mapping | Function coverage, validation status, permission drift |

**Dashboard Consumers:**

| Audience | Primary Interest | Frequency |
|----------|------------------|-----------|
| Executive Management | Overall compliance status, risk posture | Quarterly |
| CISO | Detailed metrics, trend analysis | Monthly |
| Internal Audit | Evidence completeness, control effectiveness | Per audit |
| Process Owners | Department-specific status | Monthly |
| External Auditors | Audit evidence, historical trends | Per audit |

### Business Value

A well-maintained compliance dashboard delivers:

| Value Area | Benefit |
|------------|---------|
| **Executive Visibility** | Clear risk posture for decision-making |
| **Trend Tracking** | Demonstrate continuous improvement |
| **Audit Efficiency** | Consolidated evidence reduces preparation time |
| **Resource Justification** | Data-driven security investment requests |
| **Early Warning** | Identify deteriorating compliance before audits |
| **Accountability** | Clear metrics for performance management |

### Dashboard Frequency

| Activity | Frequency | Responsibility |
|----------|-----------|----------------|
| Full Dashboard Refresh | Monthly | Dashboard Owner |
| Executive Summary Update | Monthly | CISO |
| Trend Analysis Update | Quarterly | Dashboard Owner |
| Remediation Progress Update | Weekly | Remediation Owners |
| Exception Monitoring | Monthly | Dashboard Owner |
| Audit Evidence Compilation | Per audit | ISMS Administrator |

---

## 1.2 Control Requirements

### ISO 27001:2022 Control A.5.3

Per ISO/IEC 27001:2022 Control A.5.3:

> *"Conflicting duties and conflicting areas of responsibility should be segregated."*

**Control Type:** Preventive
**Security Properties:** Confidentiality, Integrity, Availability
**Cybersecurity Concepts:** Protect
**Operational Capabilities:** Governance, Identity and Access Management

This dashboard demonstrates ongoing compliance monitoring and continuous improvement of segregation controls.

### What Auditors Look For

ISO 27001 auditors examining compliance dashboards will verify:

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Ongoing Monitoring** | Regular dashboard updates |
| **Trend Data** | Historical compliance tracking |
| **Management Attention** | Evidence of review and action |
| **Completeness** | Coverage of all A.5.3 components |
| **Accuracy** | Data matches source workbooks |
| **Timeliness** | Current data, not stale metrics |

### Why This Matters

**The Visibility Problem:**
Without a consolidated dashboard:
- Executives don't know the organisation's SoD risk posture
- Progress on remediation isn't visible
- Trend data is scattered across multiple workbooks
- Audit preparation requires extensive data compilation

**Stage 2 Audit Value:**
Auditors specifically look for evidence of ongoing monitoring. This dashboard provides:
- Current compliance status at a glance
- Historical trend demonstrating improvement
- KPI tracking showing management attention
- Evidence of exception monitoring and escalation

**Management Review Input:**
ISO 27001 requires management review of ISMS effectiveness. This dashboard provides:
- SoD programme performance metrics
- Resource allocation recommendations
- Risk-based prioritisation support
- Continuous improvement evidence

---

## 1.3 Prerequisites

### Required Data Sources

Before generating the dashboard, ensure:

- [ ] ISMS-IMP-A.5.3.1 SoD Matrix Assessment completed
- [ ] ISMS-IMP-A.5.3.2 Conflict Analysis completed
- [ ] ISMS-IMP-A.5.3.3 Role-Function Mapping completed
- [ ] Prior period dashboard (for trend comparison)

### Data Refresh Schedule

| Data Element | Source | Refresh Frequency |
|--------------|--------|-------------------|
| Conflict counts | A.5.3.1 Gap_Analysis | Monthly |
| Remediation status | A.5.3.1 Remediation_Tracker | Weekly |
| Impact scores | A.5.3.2 Impact_Assessment | Quarterly |
| Exception status | A.5.3.1 Exception_Register | Monthly |
| Validation status | A.5.3.3 Validation_Status | Quarterly |

### Required Personnel

| Role | Responsibility | Time Commitment |
|------|----------------|-----------------|
| **Dashboard Owner** | Maintain dashboard, refresh data | 2-4 hours monthly |
| **CISO** | Review and approve | 1-2 hours monthly |
| **Remediation Owners** | Update progress | 30 min weekly |
| **ISMS Administrator** | Validate data sources | 1-2 hours monthly |

### Prerequisite Checklist

Before proceeding, verify:

- [ ] All source workbooks current and approved
- [ ] Data refresh schedule understood
- [ ] Prior period data available (if not baseline)
- [ ] Distribution list current
- [ ] Archive location accessible

---

## 1.4 Workbook Structure

| Sheet | Purpose | Update Frequency |
|-------|---------|------------------|
| **Executive_Dashboard** | High-level summary for leadership | Monthly |
| **KPI_Scorecard** | Detailed KPI tracking | Monthly |
| **Conflict_Status** | Current conflict breakdown | Monthly |
| **Remediation_Progress** | Remediation tracking | Weekly |
| **Exception_Monitoring** | Active exceptions tracking | Monthly |
| **Trend_Analysis** | Historical trends | Quarterly |
| **Department_View** | Per-department metrics | Monthly |
| **Audit_Evidence** | Evidence compilation | Per audit |
| **Data_Sources** | Source data references | Each refresh |

### Sheet Dependencies

```
Data_Sources (Reference) <---- Source workbooks
       |
       v
Conflict_Status (Step 1) <---- Import conflict data
       |
       v
Remediation_Progress (Step 2) <---- Import remediation data
       |
       v
Exception_Monitoring (Step 3) <---- Import exception data
       |
       v
KPI_Scorecard (Step 4) <---- Calculate metrics
       |
       v
Trend_Analysis (Step 5) <---- Update trends
       |
       v
Department_View (Step 6) <---- Calculate by department
       |
       v
Executive_Dashboard (Step 7) <---- Summarise for executives
       |
       v
Audit_Evidence (Final) <---- Compile evidence
```

### Sheet-by-Sheet Summary

#### 1. Executive_Dashboard Sheet

High-level summary containing:
- Traffic light status indicators
- Key metrics summary
- Executive summary narrative
- Quick trend chart
- Recommended actions

#### 2. KPI_Scorecard Sheet

Detailed KPI tracking containing:
- KPI definitions and targets
- Quarterly performance
- Year-to-date status
- Trend indicators
- Target comparisons

#### 3. Conflict_Status Sheet

Current conflict breakdown containing:
- Conflict counts by type
- Conflict counts by process
- Status distribution
- Aging analysis
- Department breakdown

#### 4. Remediation_Progress Sheet

Remediation tracking containing:
- Active remediations
- Overdue items
- Burndown tracking
- Escalation status
- Owner performance

#### 5. Exception_Monitoring Sheet

Active exceptions tracking containing:
- Exception inventory
- Expiry tracking
- Compensating control status
- Review schedule
- Effectiveness ratings

#### 6. Trend_Analysis Sheet

Historical trends containing:
- Quarterly trend data
- Resolution rates
- Mean time to resolution
- Compliance percentages
- Trend indicators

#### 7. Department_View Sheet

Per-department metrics containing:
- Department compliance scores
- Department conflict counts
- Department exception counts
- Department-specific trends

#### 8. Audit_Evidence Sheet

Evidence compilation containing:
- Evidence inventory
- Location references
- Status indicators
- Audit trail

#### 9. Data_Sources Sheet

Source data references containing:
- Source workbook references
- Last refresh dates
- Responsible parties
- Refresh frequencies

---

## 1.5 Completion Walkthrough

### Step 1: Update Executive Dashboard

**Time allocation:** 30-60 minutes

**Purpose:** Provide leadership with at-a-glance compliance status.

**Key Metrics:**

| Metric | Description | Target |
|--------|-------------|--------|
| **Overall Compliance Score** | % of roles without conflicts | >95% |
| **Critical Conflicts Open** | Count of X-type conflicts unresolved | 0 |
| **Remediation On Track** | % of remediations meeting timeline | >90% |
| **Exceptions Active** | Count of approved exceptions | <5 |
| **Days Since Last Assessment** | Currency indicator | <90 |

**Traffic Light Status:**

| Metric | Green | Yellow | Red |
|--------|:-----:|:------:|:---:|
| Compliance Score | >95% | 85-95% | <85% |
| Critical Conflicts | 0 | 1-2 | >2 |
| Remediation On Track | >90% | 70-90% | <70% |
| Active Exceptions | <5 | 5-10 | >10 |

**Executive Summary Template:**
```
As of [Date], the organisation's SoD compliance status is [GREEN/YELLOW/RED].

Key Highlights:
- [X] roles assessed across [Y] systems
- [Z] conflicts identified, [W] resolved, [V] in remediation
- [N] critical conflicts requiring immediate attention
- Overall compliance improved [X]% from prior quarter

Recommended Actions:
1. [Priority action 1]
2. [Priority action 2]
3. [Priority action 3]
```

**Worked Example - Executive Summary:**
```
As of 03.02.2026, the organisation's SoD compliance status is YELLOW.

Key Highlights:
- 150 roles assessed across 12 systems
- 25 conflicts identified, 18 resolved, 5 in remediation, 2 accepted
- 1 critical conflict requiring immediate attention (Developer-Deployer)
- Overall compliance improved 8% from prior quarter (87% to 95%)

Recommended Actions:
1. Resolve critical Developer-Deployer conflict by 10.02.2026
2. Complete quarterly exception review by end of month
3. Implement automated SoD checking in HR onboarding process
```

### Step 2: Complete KPI Scorecard

**Time allocation:** 30-60 minutes

**Purpose:** Track detailed key performance indicators for SoD programme.

**KPI Definitions:**

| KPI | Formula | Target | Measurement |
|-----|---------|--------|-------------|
| **Conflict Identification Rate** | Conflicts identified / Total role combinations | N/A (baseline) | Quarterly |
| **Resolution Rate** | Conflicts resolved / Conflicts identified | >80% annually | Monthly |
| **Mean Time to Resolution** | Avg days from identification to resolution | <90 days | Monthly |
| **Exception Ratio** | Exceptions / Total conflicts | <20% | Quarterly |
| **Control Effectiveness** | Conflicts prevented by controls / Total conflicts | >70% | Quarterly |
| **Validation Coverage** | Roles validated / Total roles | 100% | Annually |
| **Drift Detection Rate** | Permission changes detected / Actual changes | >95% | Monthly |

**KPI Tracking Table:**

| KPI | Target | Q1 | Q2 | Q3 | Q4 | YTD | Trend |
|-----|:------:|:--:|:--:|:--:|:--:|:---:|:-----:|
| Resolution Rate | >80% | - | - | - | - | - | - |
| MTTR (days) | <90 | - | - | - | - | - | - |
| Exception Ratio | <20% | - | - | - | - | - | - |
| Control Effectiveness | >70% | - | - | - | - | - | - |
| Validation Coverage | 100% | - | - | - | - | - | - |

**Worked Example - KPI Scorecard:**

| KPI | Target | Q1 | Q2 | Q3 | Q4 | YTD | Trend |
|-----|:------:|:--:|:--:|:--:|:--:|:---:|:-----:|
| Resolution Rate | >80% | 65% | 72% | 78% | 85% | 75% | Up |
| MTTR (days) | <90 | 120 | 95 | 82 | 68 | 91 | Down |
| Exception Ratio | <20% | 28% | 24% | 20% | 16% | 22% | Down |
| Control Effectiveness | >70% | 55% | 62% | 68% | 75% | 65% | Up |
| Validation Coverage | 100% | 85% | 92% | 98% | 100% | 100% | Up |

### Step 3: Update Conflict Status

**Time allocation:** 30-60 minutes

**Purpose:** Provide detailed breakdown of current conflict state.

**Conflict Summary by Type:**

| Conflict Type | Total | Open | Mitigated | Resolved | Accepted |
|:-------------:|:-----:|:----:|:---------:|:--------:|:--------:|
| X (Hard) | - | - | - | - | - |
| C (Conditional) | - | - | - | - | - |
| M (Monitor) | - | - | - | - | - |
| **Total** | - | - | - | - | - |

**Conflict Summary by Process:**

| Process Domain | Total Conflicts | Critical | High | Medium | Low |
|----------------|:---------------:|:--------:|:----:|:------:|:---:|
| Financial | - | - | - | - | - |
| IT Operations | - | - | - | - | - |
| HR | - | - | - | - | - |
| Procurement | - | - | - | - | - |
| Security | - | - | - | - | - |
| Change Management | - | - | - | - | - |

**Conflict Aging Analysis:**

| Age Bucket | Count | % of Total |
|------------|:-----:|:----------:|
| <30 days | - | - |
| 30-60 days | - | - |
| 60-90 days | - | - |
| >90 days | - | - |

**Worked Example - Conflict Status:**

| Conflict Type | Total | Open | Mitigated | Resolved | Accepted |
|:-------------:|:-----:|:----:|:---------:|:--------:|:--------:|
| X (Hard) | 5 | 1 | 0 | 3 | 1 |
| C (Conditional) | 12 | 2 | 4 | 5 | 1 |
| M (Monitor) | 8 | 2 | 3 | 3 | 0 |
| **Total** | 25 | 5 | 7 | 11 | 2 |

### Step 4: Track Remediation Progress

**Time allocation:** 30-60 minutes

**Purpose:** Monitor progress of conflict resolution activities.

**Remediation Summary:**

| Status | Count | % |
|--------|:-----:|:--:|
| Not Started | - | - |
| In Progress | - | - |
| Completed | - | - |
| Cancelled | - | - |
| Overdue | - | - |

**Overdue Remediations (requiring escalation):**

| Remediation_ID | Gap_ID | Owner | Target_Date | Days_Overdue | Escalation_Status |
|----------------|--------|-------|-------------|:------------:|-------------------|
| - | - | - | - | - | - |

**Remediation Burndown:**

Track weekly/monthly progress toward zero open remediations:

| Period | Open at Start | New | Completed | Open at End | Target |
|--------|:-------------:|:---:|:---------:|:-----------:|:------:|
| Week 1 | - | - | - | - | - |
| Week 2 | - | - | - | - | - |
| ... | - | - | - | - | - |

**Worked Example - Remediation Progress:**

| Status | Count | % |
|--------|:-----:|:--:|
| Not Started | 2 | 15% |
| In Progress | 3 | 23% |
| Completed | 7 | 54% |
| Cancelled | 1 | 8% |
| Overdue | 0 | 0% |

### Step 5: Monitor Exceptions

**Time allocation:** 30-60 minutes

**Purpose:** Track active exceptions and compensating control effectiveness.

**Exception Summary:**

| Exception_ID | Gap_ID | Justification | Compensating_Controls | Expiry | Last_Review | Status |
|--------------|--------|---------------|----------------------|--------|-------------|--------|
| - | - | - | - | - | - | - |

**Exception Metrics:**

| Metric | Value |
|--------|:-----:|
| Total Active Exceptions | - |
| Exceptions Expiring <30 days | - |
| Exceptions Reviewed This Quarter | - |
| Compensating Control Failures | - |

**Compensating Control Effectiveness:**

For each exception, track whether compensating controls are working:

| Exception_ID | Control | Evidence Collected | Issues Detected | Effectiveness |
|--------------|---------|:------------------:|:---------------:|:-------------:|
| EXC-001 | Weekly log review | Yes/No | 0 | Effective |
| EXC-002 | Quarterly audit | Yes/No | 2 | Needs Improvement |

**Worked Example - Exception Monitoring:**

| Exception_ID | Gap_ID | Justification | Expiry | Control_Effective | Status |
|--------------|--------|---------------|--------|:-----------------:|--------|
| EXC-2026-001 | GAP-2026-002 | Finance team of 3 | 10.05.2026 | Yes | Active |
| EXC-2026-002 | GAP-2026-004 | Emergency access | Per incident | Yes | Active |

### Step 6: Analyse Trends

**Time allocation:** 30-60 minutes

**Purpose:** Track historical patterns to demonstrate continuous improvement.

**Quarterly Trend Data:**

| Quarter | Total Conflicts | Critical | Resolved | MTTR | Compliance % |
|---------|:---------------:|:--------:|:--------:|:----:|:------------:|
| 2025-Q1 | - | - | - | - | - |
| 2025-Q2 | - | - | - | - | - |
| 2025-Q3 | - | - | - | - | - |
| 2025-Q4 | - | - | - | - | - |
| 2026-Q1 | - | - | - | - | - |

**Trend Analysis Questions:**

1. Is the number of conflicts decreasing over time?
2. Are critical conflicts being addressed faster?
3. Is the exception count stable or growing?
4. Are compensating controls remaining effective?
5. Is validation coverage improving?

**Worked Example - Trend Analysis:**

| Quarter | Total Conflicts | Critical | Resolved | MTTR | Compliance % |
|---------|:---------------:|:--------:|:--------:|:----:|:------------:|
| 2025-Q1 | 35 | 8 | 15 | 120 | 78% |
| 2025-Q2 | 32 | 6 | 20 | 95 | 82% |
| 2025-Q3 | 28 | 4 | 24 | 82 | 88% |
| 2025-Q4 | 25 | 2 | 22 | 68 | 92% |
| 2026-Q1 | 22 | 1 | 18 | 55 | 95% |

### Step 7: Generate Department View

**Time allocation:** 30-60 minutes

**Purpose:** Provide department-specific metrics for process owners.

**Department Summary Template:**

| Metric | Engineering | Finance | HR | IT | Sales |
|--------|:-----------:|:-------:|:--:|:--:|:-----:|
| Total Roles | - | - | - | - | - |
| Conflicts Identified | - | - | - | - | - |
| Conflicts Resolved | - | - | - | - | - |
| Active Exceptions | - | - | - | - | - |
| Compliance % | - | - | - | - | - |

**Worked Example - Department View:**

| Metric | Engineering | Finance | HR | IT | Sales |
|--------|:-----------:|:-------:|:--:|:--:|:-----:|
| Total Roles | 25 | 35 | 15 | 45 | 30 |
| Conflicts Identified | 3 | 8 | 2 | 10 | 2 |
| Conflicts Resolved | 2 | 6 | 2 | 7 | 1 |
| Active Exceptions | 0 | 1 | 0 | 1 | 0 |
| Compliance % | 96% | 91% | 100% | 93% | 97% |

### Step 8: Compile Audit Evidence

**Time allocation:** 30-60 minutes

**Purpose:** Prepare consolidated evidence package for audits.

**Evidence Checklist:**

| Evidence Item | Location | Date | Status |
|---------------|----------|------|--------|
| SoD Matrix (current) | A.5.3.1 | - | Ready |
| Gap Analysis | A.5.3.1 | - | Ready |
| Conflict Analysis | A.5.3.2 | - | Ready |
| Role-Function Mapping | A.5.3.3 | - | Ready |
| Exception Approvals | Evidence folder | - | Ready |
| Compensating Control Evidence | Evidence folder | - | Ready |
| Historical Dashboards | Archive | - | Ready |
| Management Review Minutes | ISMS Records | - | Ready |

---

## 1.6 Dashboard Refresh Process

### Monthly Refresh Checklist

- [ ] Export latest data from A.5.3.1 (Remediation_Tracker, Gap_Analysis)
- [ ] Update conflict counts and status breakdown
- [ ] Refresh remediation burndown
- [ ] Update exception monitoring
- [ ] Recalculate KPIs
- [ ] Update Executive Dashboard traffic lights
- [ ] Update executive summary narrative
- [ ] Archive previous month's dashboard
- [ ] Distribute to stakeholders
- [ ] Log refresh in Data_Sources sheet

### Quarterly Refresh Checklist

- [ ] All monthly items plus:
- [ ] Update trend analysis with new quarter
- [ ] Refresh impact scores from A.5.3.2
- [ ] Validate role mappings from A.5.3.3
- [ ] Review and update KPI targets
- [ ] Prepare management review input
- [ ] Document improvement recommendations
- [ ] Update year-to-date calculations
- [ ] Review exception expiry dates

### Data Validation Steps

Before publishing refresh:

1. **Source Data Validation**
   - Verify source workbooks are current
   - Check last modified dates
   - Confirm approval status

2. **Calculation Validation**
   - Spot-check KPI calculations
   - Verify totals match source data
   - Confirm formula integrity

3. **Presentation Validation**
   - Verify traffic lights show correct status
   - Check for formula errors
   - Confirm print areas correct

---

## 1.7 Evidence Collection

### Evidence Requirements

| Evidence Type | Source | Retention |
|---------------|--------|-----------|
| Compliance Dashboard Workbook | Generated | 7 years |
| Source workbook snapshots | A.5.3.1, A.5.3.2, A.5.3.3 | 7 years |
| Management review presentations | Dashboard extracts | 7 years |
| Distribution records | Email/SharePoint | 3 years |
| Trend analysis reports | Quarterly updates | 7 years |
| Audit evidence packages | Compiled | Per audit + 7 years |

### Evidence Storage

**Primary Location:** `[SharePoint/Evidence Library]/A.5.3/Dashboard/[Year]/`

**Folder Structure:**
```
A.5.3/
|-- Dashboard/
|   |-- 2026/
|   |   |-- Monthly/
|   |   |   |-- ISMS-IMP-A.5.3.4_Compliance_Dashboard_202601.xlsx
|   |   |   |-- ISMS-IMP-A.5.3.4_Compliance_Dashboard_202602.xlsx
|   |   |   |-- ...
|   |   |-- Quarterly/
|   |   |   |-- Q1-2026-Trend-Analysis.pdf
|   |   |   |-- Q1-2026-Management-Review-Input.pptx
|   |   |-- Audit-Evidence/
|   |   |   |-- Stage2-Audit-Evidence-Package.zip
|   |   |   |-- Surveillance-Audit-2026.zip
|   |   |-- Distribution-Records/
|   |   |   |-- Dashboard-Distribution-Log-2026.xlsx
```

**Naming Convention:**
```
ISMS-IMP-A.5.3.4_Compliance_Dashboard_YYYYMM.xlsx
```

---

## 1.8 Common Pitfalls

Avoid these common mistakes when maintaining the Compliance Dashboard:

### Data Accuracy Pitfalls

❌ **MISTAKE**: Creating a dashboard that's never updated
✅ **CORRECT**: Establish a regular refresh schedule and assign clear ownership; stale dashboards lose credibility and audit value

❌ **MISTAKE**: Not validating source data before dashboard update
✅ **CORRECT**: Verify source workbooks are current before consolidating; dashboards built on stale data are misleading

❌ **MISTAKE**: Manual data entry instead of linking to sources
✅ **CORRECT**: Link to source workbooks where possible; manual entry introduces errors and creates maintenance burden

❌ **MISTAKE**: Not reconciling dashboard totals to source data
✅ **CORRECT**: Verify dashboard totals match source workbook totals; discrepancies indicate data integrity issues

### Presentation Pitfalls

❌ **MISTAKE**: Focusing only on current status without trends
✅ **CORRECT**: Always include historical comparison to show improvement; auditors want to see continuous improvement

❌ **MISTAKE**: Showing raw numbers without context
✅ **CORRECT**: Include targets, thresholds, and traffic light indicators; numbers without context are hard to interpret

❌ **MISTAKE**: Making the dashboard too detailed for executive audience
✅ **CORRECT**: Executive view should be summary; detail available in drill-down sheets; overwhelmed executives don't engage

❌ **MISTAKE**: Using inconsistent metrics between periods
✅ **CORRECT**: Maintain consistent metric definitions; changing definitions makes trend analysis meaningless

### Process Pitfalls

❌ **MISTAKE**: Not archiving previous versions
✅ **CORRECT**: Maintain historical dashboards for audit trail and trend analysis; archives demonstrate continuous monitoring

❌ **MISTAKE**: Using dashboard for detailed operational management
✅ **CORRECT**: Dashboard is for monitoring and reporting; use source workbooks for operations; mixing purposes creates confusion

❌ **MISTAKE**: Not connecting dashboard findings to actions
✅ **CORRECT**: Every red/yellow status should have documented remediation action; dashboard without action is just reporting

❌ **MISTAKE**: Distributing without CISO review
✅ **CORRECT**: CISO should review and approve before distribution; ensures accuracy and appropriate messaging

### Exception Monitoring Pitfalls

❌ **MISTAKE**: Ignoring compensating control monitoring
✅ **CORRECT**: Actively track whether exception compensating controls are working; exceptions without effective controls are unacceptable risk

❌ **MISTAKE**: Not tracking exception expiry dates
✅ **CORRECT**: Monitor exceptions expiring in next 30 days; expired exceptions without renewal are compliance failures

❌ **MISTAKE**: Assuming compensating controls are effective without evidence
✅ **CORRECT**: Collect and review compensating control evidence; "we're doing it" is not sufficient without proof

❌ **MISTAKE**: Not escalating failed compensating controls
✅ **CORRECT**: Failed compensating controls require immediate escalation; the exception is no longer valid without working controls

### Audit Readiness Pitfalls

❌ **MISTAKE**: Not preparing audit-ready evidence packages
✅ **CORRECT**: Proactively compile evidence, don't wait for audit requests; last-minute compilation leads to missing evidence

❌ **MISTAKE**: Dashboard not traceable to source evidence
✅ **CORRECT**: Maintain clear links from dashboard metrics to source workbooks; auditors will follow the trail

❌ **MISTAKE**: Historical dashboards not available
✅ **CORRECT**: Archive all dashboard versions; auditors may request historical data for trend verification

❌ **MISTAKE**: Management review inputs not documented
✅ **CORRECT**: Document how dashboard data feeds management review; this demonstrates governance integration

---

## 1.9 Quality Checklist

Before distributing the dashboard, verify all items:

### Data Accuracy Checks

- [ ] Source data timestamps verified (current within expected refresh cycle)
- [ ] Calculations spot-checked for accuracy
- [ ] KPIs match detailed data (no discrepancies)
- [ ] Traffic light thresholds correctly applied
- [ ] Totals reconcile to source workbooks
- [ ] Prior period data unchanged (unless correction)

### Completeness Checks

- [ ] All sheets updated
- [ ] Trend data includes current period
- [ ] Exception monitoring complete
- [ ] Department view covers all departments
- [ ] All KPIs have values (no blanks)
- [ ] Executive summary current

### Presentation Checks

- [ ] Executive summary narrative updated
- [ ] Traffic lights correctly colored
- [ ] No formula errors or #REF! values
- [ ] Print areas configured correctly
- [ ] Charts and graphs current
- [ ] Version number/date updated

### Process Checks

- [ ] Previous version archived
- [ ] Data_Sources sheet updated with refresh date
- [ ] CISO review completed
- [ ] Distribution list current
- [ ] File naming convention followed
- [ ] Evidence folder updated

### Audit Readiness Checks

- [ ] Audit Evidence sheet current
- [ ] All evidence items have locations
- [ ] Evidence status verified
- [ ] Historical dashboards accessible
- [ ] Source workbooks accessible

---

## 1.10 Review and Approval

### Dashboard Review Workflow

| Step | Role | Responsibility | Timeline |
|------|------|----------------|----------|
| 1 | Dashboard Owner | Complete refresh, validate data | By deadline |
| 2 | ISMS Administrator | Verify source data accuracy | 2 business days |
| 3 | CISO | Review and approve | 2 business days |
| 4 | Executive Management | Receive and review | Next management meeting |

### Approval Workflow

```
Dashboard Owner Completes Refresh
        │
        ▼
Data Validation (Quality Checklist)
        │
        ▼
ISMS Administrator Verifies ─────► Return for Corrections
        │                                │
        ▼                                │
CISO Review and Approval ────────────────┘
        │
        ▼
   Dashboard Approved
        │
        ▼
   Distribute to Stakeholders
        │
        ▼
   Archive and Log
```

### Post-Approval Actions

Upon approval:

1. Distribute to stakeholders per distribution list
2. Archive approved version in ISMS Evidence Library
3. Log distribution in Data_Sources sheet
4. Schedule next refresh
5. Update related reporting (management review, audit prep)
6. Communicate any escalation items

---

# PART II: TECHNICAL SPECIFICATION

---

## 2.1 Workbook Technical Details

### File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.3.4_Compliance_Dashboard_YYYYMMDD.xlsx` |
| Generator | `generate_a53_4_compliance_dashboard.py` |
| Sheets | 9 |
| Protected | Formula cells only |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Executive_Dashboard | Summary | 50 | 8 |
| 2 | KPI_Scorecard | KPI tracking | 20 | 9 |
| 3 | Conflict_Status | Conflict detail | 50 | 7 |
| 4 | Remediation_Progress | Remediation | 100+ | 7 |
| 5 | Exception_Monitoring | Exceptions | 50+ | 9 |
| 6 | Trend_Analysis | Trends | 20 | 8 |
| 7 | Department_View | By department | 20 | 7 |
| 8 | Audit_Evidence | Evidence | 30 | 6 |
| 9 | Data_Sources | Sources | 15 | 6 |

---

## 2.2 Sheet Specifications

### Sheet 1: Executive_Dashboard

| Row | Content | Purpose |
|-----|---------|---------|
| 1-2 | Title and date | Header |
| 4-10 | Traffic light summary (5 metrics) | At-a-glance status |
| 12-20 | Key statistics | Summary numbers |
| 22-30 | Executive summary narrative | Context and recommendations |
| 32-40 | Quick trend chart | Visual trend |

### Sheet 2: KPI_Scorecard

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | KPI_Name | 30 | Text | Pre-populated |
| B | Target | 12 | Number | None |
| C | Q1 | 10 | Number | None |
| D | Q2 | 10 | Number | None |
| E | Q3 | 10 | Number | None |
| F | Q4 | 10 | Number | None |
| G | YTD | 10 | Formula | Average of Q1-Q4 |
| H | Status | 12 | Formula | Based on Target |
| I | Trend | 10 | Formula | Compare to prior period |

### Sheet 3: Conflict_Status

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Category | 20 | Text | Pre-populated |
| B | Total | 10 | Number | None |
| C | Open | 10 | Number | None |
| D | Mitigated | 12 | Number | None |
| E | Resolved | 12 | Number | None |
| F | Accepted | 12 | Number | None |
| G | % Resolved | 12 | Formula | `=E/(B-F)*100` |

### Sheet 4: Remediation_Progress

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Remediation_ID | 15 | Text | None |
| B | Gap_ID | 15 | Text | None |
| C | Owner | 25 | Text | None |
| D | Target_Date | 15 | Date | None |
| E | Status | 15 | List | Not Started, In Progress, Completed, Cancelled, Overdue |
| F | Days_Remaining | 15 | Formula | `=D-TODAY()` |
| G | Escalation_Status | 20 | Text | None |

### Sheet 5: Exception_Monitoring

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Exception_ID | 15 | Text | None |
| B | Gap_ID | 15 | Text | None |
| C | Justification | 35 | Text | None |
| D | Compensating_Controls | 40 | Text | None |
| E | Expiry_Date | 15 | Date | None |
| F | Days_Until_Expiry | 18 | Formula | `=E-TODAY()` |
| G | Last_Review | 15 | Date | None |
| H | Control_Effective | 15 | List | Yes, No, Partial |
| I | Status | 12 | List | Active, Expired, Revoked |

### Sheet 6: Trend_Analysis

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Period | 12 | Text | e.g., 2026-Q1 |
| B | Total_Conflicts | 15 | Number | None |
| C | Critical_Conflicts | 18 | Number | None |
| D | Resolved_Count | 15 | Number | None |
| E | MTTR_Days | 12 | Number | None |
| F | Compliance_Pct | 15 | Number | None |
| G | Exceptions_Active | 18 | Number | None |
| H | Trend_vs_Prior | 15 | Formula | Compare to prior row |

### Sheet 7: Department_View

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Department | 20 | Text | None |
| B | Total_Roles | 12 | Number | None |
| C | Conflicts_Identified | 20 | Number | None |
| D | Conflicts_Resolved | 18 | Number | None |
| E | Active_Exceptions | 18 | Number | None |
| F | Compliance_Pct | 15 | Formula | `=(B-C+D)/B*100` |
| G | Status | 12 | Formula | Traffic light based on F |

### Sheet 8: Audit_Evidence

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Evidence_Item | 35 | Text | None |
| B | Document_ID | 20 | Text | None |
| C | Location | 50 | Text | None |
| D | Date | 15 | Date | None |
| E | Status | 15 | List | Ready, In Progress, Missing |
| F | Notes | 40 | Text | None |

### Sheet 9: Data_Sources

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Source_Name | 25 | Text | Pre-populated |
| B | Document_ID | 20 | Text | None |
| C | File_Location | 50 | Text | None |
| D | Last_Refresh | 15 | Date | None |
| E | Refresh_Frequency | 15 | List | Daily, Weekly, Monthly, Quarterly |
| F | Responsible_Party | 25 | Text | None |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Executive_Dashboard | Status cells | ="GREEN" | Green fill (#C6EFCE) |
| Executive_Dashboard | Status cells | ="YELLOW" | Yellow fill (#FFEB9C) |
| Executive_Dashboard | Status cells | ="RED" | Red fill (#FFC7CE), Bold |
| KPI_Scorecard | H:H | ="On Target" | Green fill (#C6EFCE) |
| KPI_Scorecard | H:H | ="At Risk" | Yellow fill (#FFEB9C) |
| KPI_Scorecard | H:H | ="Below Target" | Red fill (#FFC7CE) |
| Remediation_Progress | E:E | ="Overdue" | Red fill (#FFC7CE), Bold |
| Remediation_Progress | E:E | ="Completed" | Green fill (#C6EFCE) |
| Remediation_Progress | F:F | <0 | Red fill (#FFC7CE) |
| Exception_Monitoring | F:F | <30 | Orange fill (#FABF8F) |
| Exception_Monitoring | F:F | <0 | Red fill (#FFC7CE) |
| Exception_Monitoring | H:H | ="No" | Red fill (#FFC7CE) |
| Exception_Monitoring | H:H | ="Yes" | Green fill (#C6EFCE) |
| Department_View | G:G | ="GREEN" | Green fill (#C6EFCE) |
| Department_View | G:G | ="YELLOW" | Yellow fill (#FFEB9C) |
| Department_View | G:G | ="RED" | Red fill (#FFC7CE) |
| Audit_Evidence | E:E | ="Missing" | Red fill (#FFC7CE) |
| Audit_Evidence | E:E | ="Ready" | Green fill (#C6EFCE) |

---

## 2.4 Formulas

**Compliance Score (Executive_Dashboard):**
```
=(Total_Roles - Open_Conflicts + Resolved_Conflicts) / Total_Roles * 100
```

**Days Remaining (Remediation_Progress, Column F):**
```
=IF(D{row}="","",D{row}-TODAY())
```

**Days Until Expiry (Exception_Monitoring, Column F):**
```
=IF(E{row}="","",E{row}-TODAY())
```

**Department Compliance % (Department_View, Column F):**
```
=IF(B{row}=0,"N/A",(B{row}-C{row}+D{row})/B{row}*100)
```

**Department Status (Department_View, Column G):**
```
=IF(F{row}="N/A","N/A",IF(F{row}>=95,"GREEN",IF(F{row}>=85,"YELLOW","RED")))
```

**KPI Status (KPI_Scorecard, Column H):**
```
=IF(G{row}>=B{row},"On Target",IF(G{row}>=B{row}*0.8,"At Risk","Below Target"))
```

**KPI Trend (KPI_Scorecard, Column I):**
```
=IF(G{row}>G{row-1},"Up",IF(G{row}<G{row-1},"Down","Flat"))
```

**Resolution Rate (Conflict_Status, Column G):**
```
=IF(B{row}-F{row}=0,"N/A",E{row}/(B{row}-F{row})*100)
```

---

## 2.5 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| ISMS-IMP-A.5.3.1 | Conflict and remediation data | A.5.3.1 -> Dashboard |
| ISMS-IMP-A.5.3.2 | Impact and prioritisation data | A.5.3.2 -> Dashboard |
| ISMS-IMP-A.5.3.3 | Validation status data | A.5.3.3 -> Dashboard |
| Management Review | ISMS performance input | Dashboard -> Management Review |
| GRC Platform | Compliance metrics | Bidirectional |
| Executive Reporting | Summary metrics | Dashboard -> Reports |

---

## 2.6 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.3 | Segregation of Duties | Parent policy |
| ISMS-IMP-A.5.3.1 | SoD Matrix Assessment | Primary data source |
| ISMS-IMP-A.5.3.2 | Conflict Analysis | Impact data source |
| ISMS-IMP-A.5.3.3 | Role-Function Mapping | Validation data source |
| ISMS Management Review | Management Review Records | Consumer of dashboard |

---

**END OF SPECIFICATION**

---

*"You can't manage what you don't measure."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-03 -->
