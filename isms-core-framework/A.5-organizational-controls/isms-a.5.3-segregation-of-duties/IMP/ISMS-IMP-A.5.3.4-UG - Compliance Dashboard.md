<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.3.4-UG:framework:UG:a.5.3.4 -->
**ISMS-IMP-A.5.3.4-UG - Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.3: Policies for Segregation of Duties

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.3.4-UG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.3 Segregation of Duties |
| **Parent Policy** | ISMS-POL-A.5.3 - Segregation of Duties |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.3.4-TG.

---

## Assessment Overview

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

## Control Requirements

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

## Prerequisites

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

## Completion Walkthrough

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

## Dashboard Refresh Process

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

## Evidence Collection

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

## Common Pitfalls

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

## Quality Checklist

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

## Review and Approval

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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
