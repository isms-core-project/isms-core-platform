**ISMS-IMP-A.6.4-5.S4-UG - Employment Exit Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.6.4, A.6.5

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.4-5.S4-UG |
| **Title** | Employment Exit Compliance Dashboard |
| **Control Reference** | ISO/IEC 27001:2022 A.6.4, A.6.5 |
| **Control Name** | Disciplinary Process / Responsibilities After Termination |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Chief Information Security Officer (CISO) |
| **Classification** | Internal |
| **Framework Version** | 1.0 |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Dashboard Metrics](#14-dashboard-metrics)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 KPI Definitions](#17-kpi-definitions)
   - [1.8 Trend Analysis](#18-trend-analysis)
   - [1.9 Evidence Collection](#19-evidence-collection)
   - [1.10 Common Pitfalls](#110-common-pitfalls)
   - [1.11 Quality Checklist](#111-quality-checklist)
   - [1.12 Review and Approval](#112-review-and-approval)
   - [1.13 Related Controls](#113-related-controls)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Architecture](#21-workbook-architecture)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Data Validations](#23-data-validations)
   - [2.4 Conditional Formatting](#24-conditional-formatting)
   - [2.5 Formula Specifications](#25-formula-specifications)
   - [2.6 Cell Styling Standards](#26-cell-styling-standards)
   - [2.7 Generator Script Reference](#27-generator-script-reference)

---

---

## 1.1 Assessment Overview

### Purpose

This workbook provides executive-level visibility into the organisation's employment exit and disciplinary process compliance. It consolidates data from the other A.6.4-5 workbooks to deliver actionable metrics and trend analysis. It serves as the operational tool for:

- **Executive Reporting**: High-level KPIs for management review
- **Compliance Monitoring**: Real-time visibility into process compliance
- **Trend Analysis**: Historical trends in exits, disciplinary actions, and SLA compliance
- **Risk Identification**: Highlighting areas requiring attention
- **Audit Preparation**: Consolidated evidence for ISO 27001 audits
- **Continuous Improvement**: Data-driven improvement opportunities

The dashboard aggregates data from:
- ISMS-IMP-A.6.4-5.S1: Disciplinary Process Assessment
- ISMS-IMP-A.6.4-5.S2: Employment Exit Assessment
- ISMS-IMP-A.6.4-5.S3: Post-Employment Obligations

### Scope

**In Scope:**
- Executive summary metrics
- Access revocation SLA compliance
- Asset recovery rates
- Exit process completion rates
- Disciplinary case metrics
- Post-employment obligation tracking
- Orphaned account metrics
- Trend analysis (12-month rolling)
- Comparative analysis by exit type
- Exception and escalation tracking

**Out of Scope:**
- Detailed process documentation (covered in source workbooks)
- Individual case management
- Operational procedures

### Business Value

| Value Area | Benefit |
|------------|---------|
| **Visibility** | Management awareness of exit process health |
| **Compliance** | Evidence of continuous monitoring |
| **Accountability** | Clear metrics drive performance |
| **Audit Readiness** | Consolidated evidence for auditors |
| **Risk Management** | Early identification of issues |
| **Improvement** | Data-driven process enhancement |

### Reporting Frequency

| Report | Frequency | Audience |
|--------|-----------|----------|
| Executive Dashboard | Monthly | Executive Management |
| Detailed Metrics | Monthly | CISO, HR Director |
| Trend Analysis | Quarterly | Management Review |
| Audit Summary | Pre-audit | External Auditors |

---

## 1.2 Control Requirements

### ISO 27001:2022 Control A.6.4 and A.6.5

This dashboard supports demonstration of effective implementation of both controls through continuous monitoring and measurement.

**Measurement Requirements:**
- Process effectiveness tracking
- SLA compliance monitoring
- Exception management
- Trend identification
- Continuous improvement evidence

### What Auditors Look For

| Audit Focus | Dashboard Evidence |
|-------------|-------------------|
| **Process Effectiveness** | KPI achievement rates |
| **Timeliness** | Access revocation SLA compliance |
| **Completeness** | Exit checklist completion rates |
| **Monitoring** | Orphaned account detection |
| **Improvement** | Trend analysis and corrective actions |

---

## 1.3 Prerequisites

### Data Sources Required

| Source | Data Required | Update Frequency |
|--------|---------------|------------------|
| Exit_Tracker (A.6.4-5.2) | Exit dates, status, completion | Ongoing |
| Access_Revocation (A.6.4-5.2) | Revocation dates, SLA compliance | Ongoing |
| Asset_Recovery (A.6.4-5.2) | Asset return status | Ongoing |
| Leaver_Reconciliation (A.6.4-5.2) | Orphaned account counts | Monthly |
| Case_Tracker (A.6.4-5.1) | Disciplinary case metrics | Ongoing |
| Active_Obligations (A.6.4-5.3) | Obligation status | Ongoing |
| Acknowledgement_Log (A.6.4-5.3) | Exit acknowledgement rates | Ongoing |

### Prerequisite Checklist

- [ ] Source workbooks (A.6.4-5.1, .2, .3) populated
- [ ] Data refresh process established
- [ ] Reporting period defined
- [ ] KPI targets approved by management
- [ ] Trend baseline established

---

## 1.4 Dashboard Metrics

### Executive Summary KPIs

| KPI | Target | Measurement |
|-----|--------|-------------|
| **Exit Process Completion Rate** | 100% | Exits fully completed / Total exits |
| **Access Revocation SLA Compliance** | 100% | Revocations within SLA / Total revocations |
| **Asset Recovery Rate** | >95% | Assets recovered / Assets assigned |
| **Orphaned Account Rate** | 0 | Active accounts for terminated staff |
| **Exit Interview Completion** | 100% | Exit interviews conducted / Voluntary exits |
| **Acknowledgement Rate** | 100% | Signed acknowledgements / Total exits |
| **Disciplinary Case Closure** | >90% in 30 days | Cases closed within 30 days / Total cases |
| **Active Obligation Compliance** | 100% | No enforcement actions |

### Category-Specific Metrics

#### Access Revocation Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Same-Day Revocation Rate | Revoked same day / Total | 100% (involuntary) |
| End-of-Day Revocation Rate | Revoked by end of last day / Total | 100% (voluntary) |
| Third-Party Notification Rate | Notified within 48h / Total with third-party access | 100% |
| Privileged Access Revocation | Privileged revoked within 1h / Total privileged | 100% |

#### Asset Recovery Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Computing Device Recovery | Devices returned / Devices assigned | >98% |
| Mobile Device Recovery | Mobile returned / Mobile assigned | >95% |
| Access Badge Recovery | Badges returned / Badges issued | >99% |
| Data Wiping Verification | Wiping verified / Devices recovered | 100% |

#### Disciplinary Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Cases per 100 Employees | (Total cases / Headcount) x 100 | <5% |
| Average Case Duration | Sum(closure date - report date) / Cases | <30 days |
| Appeal Rate | Appeals / Decisions | <10% |
| Repeat Violation Rate | Second+ violations / Total violations | <20% |

#### Post-Employment Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Active Obligations Count | Count of active post-employment obligations | Informational |
| Expiring Next 90 Days | Obligations expiring in 90 days | Informational |
| Enforcement Actions | Active enforcement cases | 0 |
| Acknowledgement Refusal Rate | Refusals / Total exits | <1% |

---

## 1.5 Workbook Structure

### Sheet Overview

| Sheet | Purpose | Primary User | Update Frequency |
|-------|---------|--------------|------------------|
| **Executive_Dashboard** | High-level KPI summary | Executive Management | Monthly |
| **Exit_Metrics** | Detailed exit process metrics | HR, IT | Monthly |
| **Access_Revocation_Metrics** | Access revocation compliance | IAM Team | Monthly |
| **Asset_Metrics** | Asset recovery tracking | IT Operations | Monthly |
| **Disciplinary_Metrics** | Disciplinary case analysis | HR, CISO | Monthly |
| **Obligation_Metrics** | Post-employment tracking | Legal, ISM | Monthly |
| **Trend_Analysis** | Historical trend data | ISM | Monthly |
| **Data_Sources** | Source data references | ISM | Per update |
| **Instructions** | Guidance | All users | As needed |

---

## 1.6 Completion Walkthrough

### Step 1: Update Data_Sources Sheet

**Time estimate:** 30-60 minutes

Link to or import data from source workbooks:

#### Column A: Data_Source

- **Options:** A.6.4-5.1, A.6.4-5.2, A.6.4-5.3

#### Column B: Source_Sheet

- **Format:** Sheet name from source workbook

#### Column C: Last_Updated

- **Format:** DD.MM.YYYY

#### Column D: Records_Count

- **Format:** Number of records

#### Column E: Update_Method

- **Options:** Manual, Linked, Automated

#### Column F: Update_By

- **Format:** Person responsible

### Step 2: Update Exit_Metrics Sheet

**Time estimate:** 30 minutes

Enter monthly exit statistics:

#### Column A: Period

- **Format:** YYYY-MM

#### Column B: Total_Exits

- Count of exits in period

#### Column C: Voluntary

- Count of voluntary exits

#### Column D: Involuntary

- Count of involuntary exits

#### Column E: Contractors

- Count of contractor exits

#### Column F: Fully_Complete

- Count with all steps complete

#### Column G: Completion_Rate

- **Formula:** =F2/B2

#### Column H: Outstanding_Items

- Count with items outstanding

### Step 3: Update Access_Revocation_Metrics Sheet

**Time estimate:** 30 minutes

Enter access revocation compliance data:

#### Column A: Period

- **Format:** YYYY-MM

#### Column B: Total_Revocations

- Count of access revocations required

#### Column C: Within_SLA

- Count revoked within SLA

#### Column D: SLA_Compliance

- **Formula:** =C2/B2

#### Column E: Avg_Revocation_Hours

- Average hours from last day to revocation

#### Column F: Same_Day_Rate

- Percentage revoked same day (involuntary)

#### Column G: Privileged_Compliance

- Percentage of privileged access revoked within 1 hour

#### Column H: Third_Party_Notified

- Third-party notification compliance rate

### Step 4: Update Asset_Metrics Sheet

**Time estimate:** 30 minutes

Enter asset recovery data:

#### Column A: Period

- **Format:** YYYY-MM

#### Column B: Assets_Due

- Total assets expected to be returned

#### Column C: Assets_Returned

- Total assets actually returned

#### Column D: Recovery_Rate

- **Formula:** =C2/B2

#### Column E: Outstanding_30Days

- Assets outstanding >30 days

#### Column F: Data_Wiping_Verified

- Count of devices with verified wiping

#### Column G: Wiping_Rate

- **Formula:** =F2/C2

### Step 5: Update Disciplinary_Metrics Sheet

**Time estimate:** 30 minutes

Enter disciplinary case statistics:

#### Column A: Period

- **Format:** YYYY-MM

#### Column B: Cases_Opened

- New cases in period

#### Column C: Cases_Closed

- Cases closed in period

#### Column D: Avg_Duration_Days

- Average days to close

#### Column E: By_Severity

- Breakdown by severity level

#### Column F: Appeals_Filed

- Number of appeals

#### Column G: Terminations

- Cases resulting in termination

### Step 6: Update Obligation_Metrics Sheet

**Time estimate:** 30 minutes

Enter post-employment obligation data:

#### Column A: Period

- **Format:** YYYY-MM

#### Column B: Total_Active

- Total active obligations

#### Column C: New_This_Period

- New obligations added

#### Column D: Expired_This_Period

- Obligations that expired

#### Column E: Expiring_90Days

- Expiring in next 90 days

#### Column F: Enforcement_Active

- Active enforcement cases

#### Column G: Acknowledgement_Rate

- Percentage with signed acknowledgement

### Step 7: Update Trend_Analysis Sheet

**Time estimate:** 1 hour (initial setup)

Maintain 12-month rolling trend data:

#### Rows: One per month (rolling 12)

#### Columns: Key metrics for trending

- Exit completion rate trend
- Access revocation SLA trend
- Asset recovery rate trend
- Orphaned account trend
- Disciplinary case trend

### Step 8: Review Executive_Dashboard Sheet

**Time estimate:** 15 minutes

Verify all KPIs are calculating correctly:

- Check formula references to data sheets
- Verify RAG status indicators
- Review trend arrows
- Confirm period is correct

---

## 1.7 KPI Definitions

### Exit Process Completion Rate

**Definition:** Percentage of employment exits that have all required steps completed.

**Formula:**
```
Exit Process Completion Rate = (Exits with all steps complete / Total exits) x 100
```

**Target:** 100%

**Components:**
- Access revocation complete
- Assets returned
- Exit interview conducted
- Acknowledgement signed
- Knowledge transfer complete (where applicable)

**RAG Status:**
| Status | Threshold |
|--------|-----------|
| Green | ≥98% |
| Amber | 90-97% |
| Red | <90% |

### Access Revocation SLA Compliance

**Definition:** Percentage of access revocations completed within defined SLAs.

**Formula:**
```
SLA Compliance = (Revocations within SLA / Total revocations) x 100
```

**Target:** 100%

**SLA by Exit Type:**
| Exit Type | SLA |
|-----------|-----|
| Immediate Dismissal | 1 hour |
| Involuntary Termination | Same business day |
| Voluntary Resignation | End of last working day |
| Contract End | Contract end date |

**RAG Status:**
| Status | Threshold |
|--------|-----------|
| Green | 100% |
| Amber | 95-99% |
| Red | <95% |

### Orphaned Account Rate

**Definition:** Number of active user accounts belonging to terminated employees.

**Formula:**
```
Orphaned Account Rate = Active accounts for leavers / Total terminations
```

**Target:** 0

**Detection Method:** Monthly reconciliation of HR termination records against active account lists.

**RAG Status:**
| Status | Threshold |
|--------|-----------|
| Green | 0 |
| Amber | 1-2 |
| Red | >2 |

### Asset Recovery Rate

**Definition:** Percentage of assigned assets recovered from departing personnel.

**Formula:**
```
Asset Recovery Rate = (Assets returned / Assets assigned to leavers) x 100
```

**Target:** >95%

**RAG Status:**
| Status | Threshold |
|--------|-----------|
| Green | ≥95% |
| Amber | 85-94% |
| Red | <85% |

---

## 1.8 Trend Analysis

### Trend Indicators

| Indicator | Meaning |
|-----------|---------|
| ↑ Green Arrow | Improving trend (positive) |
| ↓ Red Arrow | Declining trend (negative) |
| → Yellow Arrow | Stable (no significant change) |

### Trend Calculation

**Month-over-Month Change:**
```
Change = ((Current Month - Previous Month) / Previous Month) x 100
```

**Rolling Average (3-month):**
```
Rolling Avg = (Month 1 + Month 2 + Month 3) / 3
```

### Trend Thresholds

| Metric | Improving | Stable | Declining |
|--------|-----------|--------|-----------|
| Completion Rate | >1% increase | ±1% | >1% decrease |
| SLA Compliance | Any increase | No change | Any decrease |
| Asset Recovery | >2% increase | ±2% | >2% decrease |
| Orphaned Accounts | Decrease | 0 | Any increase |

### Seasonality Considerations

| Period | Expected Impact |
|--------|-----------------|
| Q1 (Jan-Mar) | Higher voluntary exits (new year moves) |
| Q2 (Apr-Jun) | Normal |
| Q3 (Jul-Sep) | Lower exits (vacation period) |
| Q4 (Oct-Dec) | Lower voluntary exits (year-end retention) |

---

## 1.9 Evidence Collection

### Evidence Requirements

| Evidence Type | Description | Retention |
|---------------|-------------|-----------|
| **Monthly Dashboard Reports** | PDF exports of dashboard | 3 years |
| **Trend Analysis** | Historical trend data | 3 years |
| **KPI Achievement Records** | Target vs. actual | 3 years |
| **Management Review Minutes** | Minutes referencing dashboard | 3 years |
| **Completed Workbook** | This assessment | 3 cycles |

### Evidence Storage

**Naming Convention:**
```
EVD-A.6.4-5.4_[EvidenceType]_[YYYYMM].[ext]
```

**Examples:**
- `EVD-A.6.4-5.4_Dashboard_202602.pdf`
- `EVD-A.6.4-5.4_TrendAnalysis_2026Q1.xlsx`

---

## 1.10 Common Pitfalls

### Data Quality Pitfalls

**MISTAKE**: Dashboard data not updated regularly
**CORRECT**: Establish monthly update schedule; assign responsibility; automate where possible; verify data freshness before reporting

**MISTAKE**: Inconsistent data definitions across sources
**CORRECT**: Define clear data definitions; ensure source workbooks use consistent terminology; document data transformations; validate calculations

**MISTAKE**: Missing historical data for trends
**CORRECT**: Maintain 12-month rolling data minimum; backfill gaps where possible; document any data gaps in notes; establish baseline before trending

**MISTAKE**: Manual data entry errors
**CORRECT**: Use formulas and links where possible; implement validation checks; review data before publishing; use data validation dropdowns

### Metric Definition Pitfalls

**MISTAKE**: Unclear KPI definitions
**CORRECT**: Document precise formulas and data sources; ensure consistent interpretation; train users on metric meaning; include definitions in dashboard

**MISTAKE**: Inappropriate targets
**CORRECT**: Set realistic, achievable targets; review and adjust annually; benchmark against industry where possible; get management buy-in on targets

**MISTAKE**: Too many metrics causing confusion
**CORRECT**: Focus on actionable KPIs (5-7 maximum for executive dashboard); provide detail in subsidiary sheets; prioritise by business impact

**MISTAKE**: Metrics that can be gamed
**CORRECT**: Use multiple complementary metrics; validate unusual results; audit underlying data; focus on outcomes not just compliance

### Reporting Pitfalls

**MISTAKE**: Dashboard not reviewed by management
**CORRECT**: Include in management review agenda; require sign-off; highlight significant changes; make reporting valuable through insights

**MISTAKE**: No action taken on poor results
**CORRECT**: Define escalation for amber/red metrics; assign owners for improvement actions; track action completion; report on remediation

**MISTAKE**: RAG status thresholds too lenient
**CORRECT**: Set thresholds that drive action; review thresholds annually; benchmark against best practice; align with risk appetite

**MISTAKE**: Trends misinterpreted
**CORRECT**: Consider seasonality; use rolling averages to smooth volatility; look at context not just numbers; document explanations for anomalies

---

## 1.11 Quality Checklist

### Data Quality Checks

- [ ] All source data updated to current period
- [ ] Data sources documented and verified
- [ ] Formulas validated and calculating correctly
- [ ] No data gaps in trend analysis
- [ ] Outliers investigated and explained

### Metric Checks

- [ ] All KPIs displaying correctly
- [ ] RAG status indicators accurate
- [ ] Trend arrows calculated correctly
- [ ] Targets current and approved
- [ ] Period labels correct

### Reporting Checks

- [ ] Executive summary complete
- [ ] Key insights highlighted
- [ ] Actions documented for poor performance
- [ ] Comparison to prior period included
- [ ] Ready for management review

### Evidence Checks

- [ ] Dashboard exported as PDF
- [ ] Stored in ISMS Evidence Library
- [ ] Naming convention followed
- [ ] Management review documented

---

## 1.12 Review and Approval

### Monthly Review Process

1. **Data Update** (ISM) - Update all data sheets
2. **Validation** (ISM) - Verify calculations and RAG status
3. **Analysis** (ISM) - Document insights and issues
4. **Review** (HR Director, IAM Manager) - Validate data accuracy
5. **Approval** (CISO) - Sign-off for management reporting

### Management Review Inclusion

Dashboard should be included in:
- Monthly ISMS management review
- Quarterly executive security briefing
- Annual ISMS management review (ISO 27001 Clause 9.3)
- Pre-audit preparation

---

## 1.13 Related Controls

| Control | Dashboard Integration |
|---------|----------------------|
| **A.5.15-18** IAM | Access revocation metrics |
| **A.6.3** Training | Training completion as mitigation |
| **A.6.6** NDAs | Obligation tracking |
| **A.8.1** User Endpoints | Asset recovery metrics |

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
