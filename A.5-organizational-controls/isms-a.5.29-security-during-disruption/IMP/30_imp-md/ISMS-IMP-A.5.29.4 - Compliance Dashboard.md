# ISMS-IMP-A.5.29.4 — Compliance Dashboard

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.29.4 |
| **Title** | Compliance Dashboard |
| **Control Reference** | ISO/IEC 27001:2022 A.5.29 |
| **Control Name** | Information Security During Disruption |
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
   - [1.4 Metrics and KPIs](#14-metrics-and-kpis)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 Data Sources](#17-data-sources)
   - [1.8 Evidence Collection](#18-evidence-collection)
   - [1.9 Common Pitfalls](#19-common-pitfalls)
   - [1.10 Quality Checklist](#110-quality-checklist)
   - [1.11 Review and Approval](#111-review-and-approval)
   - [1.12 Integration with Other Controls](#112-integration-with-other-controls)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Architecture](#21-workbook-architecture)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Data Validations](#23-data-validations)
   - [2.4 Conditional Formatting](#24-conditional-formatting)
   - [2.5 Formula Specifications](#25-formula-specifications)
   - [2.6 Cell Styling Standards](#26-cell-styling-standards)
   - [2.7 Generator Script Reference](#27-generator-script-reference)

---

# PART I: USER COMPLETION GUIDE

---

## 1.1 Assessment Overview

### Purpose

This workbook provides executive-level visibility into the organisation's security-during-disruption posture. It consolidates metrics from ISMS-IMP-A.5.29.1, A.5.29.2, and A.5.29.3 into a single dashboard for:

- **Executive Summary**: High-level compliance status and key indicators
- **BC/DR Security Coverage**: Security section approval status across all plans
- **Emergency Access Readiness**: Break-glass account testing and availability
- **Security Personnel Availability**: Team availability and succession readiness
- **Security Debt Status**: Current debt items and aging analysis
- **Disruption Incident History**: Past incidents and security outcomes
- **Trend Analysis**: Historical performance and improvement tracking

The Compliance Dashboard enables CISO and Executive Management to understand at a glance whether the organisation is prepared to maintain security during disruption.

### Scope

This dashboard consolidates data from:

**Input Sources:**
- ISMS-IMP-A.5.29.1 - Security Control Inventory, BC/DR Security Reviews
- ISMS-IMP-A.5.29.2 - Break-Glass Accounts, Personnel Availability, Security Debt
- ISMS-IMP-A.5.29.3 - Recovery Verification, Lessons Learned

**Output Metrics:**
- Overall compliance score
- BC/DR plan coverage percentage
- Emergency access test status
- Security personnel availability
- Security debt aging
- Disruption incident outcomes

### Business Value

The Compliance Dashboard delivers:

| Value Area | Benefit |
|------------|---------|
| **Executive Visibility** | Clear status at a glance |
| **Risk Awareness** | Identify gaps before disruption |
| **Trend Analysis** | Track improvement over time |
| **Audit Readiness** | Pre-compiled metrics for auditors |
| **Decision Support** | Data-driven resource allocation |
| **Regulatory Evidence** | Documented governance metrics |

### Dashboard Frequency

| Activity | Frequency | Responsible Party |
|----------|-----------|-------------------|
| Dashboard Update | Monthly | Security Administrator |
| Executive Review | Quarterly | CISO |
| Full Refresh | Annual (with full assessment) | Security Team |
| Audit Preparation | Before certification audits | CISO |

---

## 1.2 Control Requirements

### ISO 27001:2022 Control A.5.29

> *"The organisation should plan how to maintain information security at an appropriate level during disruption."*

**Dashboard Focus**: This workbook demonstrates that the organisation:
- Has documented security requirements for disruption
- Maintains readiness through testing and training
- Monitors and improves security-during-disruption capability

### Governance Requirements

**1. Metrics Tracking**
- Defined KPIs for security-during-disruption readiness
- Regular measurement and reporting
- Trend analysis over time

**2. Failure Mode Detection**
- Early warning indicators for gaps
- Escalation thresholds defined
- Proactive remediation triggers

**3. Continuous Improvement**
- Lessons learned incorporated
- Metrics improve over time
- Regular assessment and adjustment

### What Auditors Look For

ISO 27001 auditors reviewing governance metrics will verify:

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Metrics Definition** | Documented KPIs and targets |
| **Regular Monitoring** | Evidence of ongoing measurement |
| **Management Review** | Evidence of executive oversight |
| **Trend Analysis** | Historical data and improvement |
| **Gap Remediation** | Actions taken on identified issues |

---

## 1.3 Prerequisites

### Before Starting This Dashboard

#### Required Access

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| ISMS-IMP-A.5.29.1 Workbook | Read | BC/DR security review data |
| ISMS-IMP-A.5.29.2 Workbook | Read | Break-glass, personnel, debt data |
| ISMS-IMP-A.5.29.3 Workbook | Read | Recovery and lessons learned data |
| ISMS Evidence Library | Read | Historical disruption records |

#### Required Information

| Information | Source | Why Needed |
|-------------|--------|------------|
| Current BC/DR plan inventory | BC Manager | Calculate coverage |
| Test schedules and results | Security Team | Verify readiness |
| Security debt register | ISMS-IMP-A.5.29.2 | Calculate debt metrics |
| Disruption incident history | Incident Management | Historical analysis |

#### Prerequisite Checklist

Before proceeding, verify:

- [ ] Access to all A.5.29 workbooks confirmed
- [ ] Historical incident data available
- [ ] Current period data entered in source workbooks
- [ ] Previous dashboard version available (for trending)

---

## 1.4 Metrics and KPIs

### Primary Metrics

| Metric | Target | Measurement | Frequency |
|--------|--------|-------------|-----------|
| **BC/DR Plans with CISO Approval** | 100% | Plans approved / Total plans | Quarterly |
| **Emergency Access Tests Completed** | 100% annually | Tests completed / Tests required | Quarterly |
| **Security Personnel Availability** | 100% reachable within 1 hour | Drill success rate | Semi-annual |
| **Security Debt Items >90 Days** | 0 | Count of aged items | Monthly |
| **Recovery Site Security Assessments** | 0 critical/high findings | Finding count | Annual |

### Secondary Metrics

| Metric | Target | Measurement | Frequency |
|--------|--------|-------------|-----------|
| **Compensating Controls Tested** | 100% | Tested / Total | Annual |
| **Security Incidents During Disruption** | Decreasing trend | Count per disruption | Per incident |
| **Security Debt Closed Within Target** | >90% | Closed on time / Total | Monthly |
| **Lessons Learned Actions Completed** | 100% | Completed / Total | Per incident |
| **Personnel Cross-Training Complete** | >80% | Trained / Required | Annual |

### Compliance Scoring

| Score Range | Status | Action Required |
|-------------|--------|-----------------|
| **90-100%** | Compliant | Maintain and improve |
| **70-89%** | Partially Compliant | Address gaps within 30 days |
| **50-69%** | Non-Compliant | Immediate remediation required |
| **<50%** | Critical | Executive escalation required |

---

## 1.5 Workbook Structure

### Sheet Overview

The workbook consists of ten sheets:

| Sheet | Purpose | Primary User | Update Frequency |
|-------|---------|--------------|------------------|
| **Executive_Dashboard** | High-level summary | Executive Management | Monthly |
| **BCDR_Security_Status** | BC/DR plan coverage | CISO | Quarterly |
| **Emergency_Access_Status** | Break-glass readiness | Security Manager | Quarterly |
| **Personnel_Status** | Team availability | CISO | Quarterly |
| **Security_Debt_Status** | Debt aging analysis | Security Manager | Monthly |
| **Disruption_History** | Past incident analysis | Security Team | Per incident |
| **Trend_Analysis** | Historical performance | CISO | Quarterly |
| **Data_Sources** | Source workbook references | Security Administrator | Monthly |
| **Instructions** | Guidance | All users | As needed |
| **Approval_SignOff** | Dashboard approval | Approvers | Monthly |

### Sheet Relationships

```
┌─────────────────────┐
│    Instructions     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Data_Sources      │ ◄── Link source workbooks
└──────────┬──────────┘
           │
     ┌─────┴─────┬─────────┬─────────┬─────────┐
     ▼           ▼         ▼         ▼         ▼
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│BCDR_    │ │Emergency│ │Personnel│ │Security_│ │Disruption
│Security │ │_Access_ │ │_Status  │ │Debt_    │ │_History │
│_Status  │ │Status   │ │         │ │Status   │ │         │
└────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘
     │           │           │           │           │
     └─────┬─────┴───────────┴───────────┴───────────┘
           │
           ▼
┌─────────────────────┐
│  Trend_Analysis     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│Executive_Dashboard  │ ◄── Summary view
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Approval_SignOff   │
└─────────────────────┘
```

---

## 1.6 Completion Walkthrough

### Step-by-Step Process

#### Step 1: Update Data Sources (30 minutes)
1. Open Data_Sources sheet
2. Verify links to source workbooks are current and accessible
3. Update file paths if workbooks have moved or been renamed
4. Confirm data refresh dates for each source
5. Document any source data issues or gaps
6. Update Link_Status column for each source
7. Note any sources requiring update before proceeding

#### Step 2: Refresh BC/DR Security Status (1 hour)
1. Import current BC/DR plan list from BC Manager
2. Update CISO approval status from ISMS-IMP-A.5.29.1
3. Verify Security_Section column is accurate for each plan
4. Update approval dates where changed
5. Calculate coverage percentage using formula
6. Identify plans needing review (overdue or pending approval)
7. Flag any plans missing security sections
8. Document gaps requiring remediation action

#### Step 3: Refresh Emergency Access Status (30 minutes)
1. Import break-glass account list from ISMS-IMP-A.5.29.2
2. Update test dates and status for each account
3. Verify current disabled/enabled status in IAM
4. Check credential rotation dates
5. Verify logging is enabled and verified
6. Calculate test completion percentage
7. Identify overdue tests (>365 days since last test)
8. Calculate individual readiness scores
9. Flag accounts with issues requiring attention

#### Step 4: Refresh Personnel Status (30 minutes)
1. Import personnel data from ISMS-IMP-A.5.29.2
2. Update contact test results with dates
3. Verify primary and backup assignments current
4. Update cross-training status
5. Record drill participation dates
6. Calculate availability percentage
7. Identify succession gaps (roles with <2 backups)
8. Flag personnel with outdated contact tests (>90 days)
9. Calculate availability scores per role

#### Step 5: Refresh Security Debt Status (30 minutes)
1. Import debt register from ISMS-IMP-A.5.29.2
2. Calculate aging metrics (0-30, 31-60, 61-90, >90 days)
3. Count items in each aging category
4. Identify items requiring escalation (>30 days)
5. Identify items requiring executive escalation (>90 days)
6. Calculate closure rate for the period
7. Update trend data with current period figures
8. Document any escalation actions taken

#### Step 6: Update Disruption History (as needed)
1. Add any new disruption incidents since last update
2. Complete all incident metadata fields
3. Record security posture level during incident
4. Document emergency access usage
5. Count security incidents during disruption
6. Record any security compromises
7. Update recovery phase completion status
8. Link to lessons learned documentation
9. Assess and record security outcome

#### Step 7: Generate Trend Analysis (30 minutes)
1. Enter current period metrics in Trend_Analysis sheet
2. Verify historical data is complete for all prior periods
3. Calculate overall score for current period
4. Determine trend direction (Improving/Stable/Declining)
5. Refresh trend charts to include current period
6. Identify areas of improvement
7. Identify areas of degradation requiring attention
8. Document significant trend changes for commentary

#### Step 8: Update Executive Dashboard (30 minutes)
1. Verify all summary formulas calculating correctly
2. Confirm overall compliance score is accurate
3. Review key metrics summary for accuracy
4. Update Current Issues and Alerts section
5. Refresh trend summary indicators
6. Add CISO commentary on significant changes
7. Highlight key messages for executive attention
8. Review colour-coding for appropriate status indication
9. Ensure dashboard presents clearly and professionally

#### Step 9: Validate and Review (30 minutes)
1. Perform data quality checks per Quality Checklist
2. Cross-check metrics against source systems
3. Verify calculations independently
4. Review presentation for clarity
5. Confirm no errors or broken references
6. Security Manager review for accuracy

#### Step 10: Obtain Approval and Archive (30 minutes)
1. Present to CISO for review and approval
2. Incorporate any feedback or corrections
3. Obtain formal CISO approval
4. Schedule executive briefing if quarterly
5. Archive approved dashboard to ISMS Evidence Library
6. Update version control and date stamp
7. Notify stakeholders of dashboard availability

---

## 1.7 Data Sources

### Source Workbook Mapping

| Dashboard Element | Source Workbook | Source Sheet | Key Fields |
|-------------------|-----------------|--------------|------------|
| BC/DR Coverage | ISMS-IMP-A.5.29.1 | BCDR_Security_Review | CISO_Approval_Status |
| Control Inventory | ISMS-IMP-A.5.29.1 | Security_Control_Inventory | All |
| Break-Glass Tests | ISMS-IMP-A.5.29.2 | BreakGlass_Accounts | Last_Test_Date |
| Personnel Availability | ISMS-IMP-A.5.29.2 | Personnel_Availability | Last_Contact_Test |
| Security Debt | ISMS-IMP-A.5.29.2 | Security_Debt_Register | Status, Age_Days |
| Recovery Status | ISMS-IMP-A.5.29.3 | Recovery_Checklist | Status |
| Lessons Learned | ISMS-IMP-A.5.29.3 | Lessons_Learned | Status |

---

## 1.8 Evidence Collection

### Evidence Requirements

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| **Monthly Dashboard** | Completed dashboard for each period | ISMS Evidence Library |
| **Trend Charts** | Historical trend visualisations | ISMS Evidence Library |
| **Executive Presentations** | Quarterly briefing materials | ISMS Evidence Library |
| **Remediation Records** | Actions taken on identified gaps | ISMS Evidence Library |

---

## 1.9 Common Pitfalls

Avoid these common mistakes when completing this dashboard:

❌ **MISTAKE: Using stale source data from outdated workbooks**
- **Impact**: Dashboard shows outdated status; false confidence in compliance
- **Prevention**: Verify source update dates before each dashboard refresh; flag stale data

❌ **MISTAKE: Broken workbook links causing formula errors**
- **Impact**: Formulas return #REF errors; incomplete metrics; unprofessional presentation
- **Prevention**: Test all links before publishing; verify file paths after any workbook move

❌ **MISTAKE: Missing historical data preventing trend analysis**
- **Impact**: Cannot calculate trends; lose ability to show improvement over time
- **Prevention**: Archive each period consistently; maintain historical data repository

❌ **MISTAKE: Optimistic or subjective scoring methodology**
- **Impact**: False confidence; audit findings when actual state differs from reported
- **Prevention**: Use objective calculation formulas; document scoring methodology

❌ **MISTAKE: No executive review of dashboard content**
- **Impact**: Dashboard not used for decisions; becomes checkbox exercise
- **Prevention**: Schedule regular briefings; obtain CISO sign-off on each dashboard

❌ **MISTAKE: Relying on manual calculations instead of formulas**
- **Impact**: Errors and inconsistency; difficult to audit calculation methodology
- **Prevention**: Use formulas where possible; document any manual inputs

❌ **MISTAKE: Presenting numbers without explanatory context**
- **Impact**: Executives cannot interpret significance; no actionable insights
- **Prevention**: Add commentary section; explain significant changes from previous period

❌ **MISTAKE: Not updating dashboard after disruption incidents**
- **Impact**: Lessons not reflected; recovery outcomes not tracked
- **Prevention**: Update after every disruption; include in incident closure checklist

❌ **MISTAKE: Ignoring trend data showing gradual degradation**
- **Impact**: Missing slow decline in compliance; issues compound over time
- **Prevention**: Review trend data quarterly; set threshold alerts for declining metrics

❌ **MISTAKE: No action taken on identified gaps**
- **Impact**: Dashboard becomes compliance theatre; same issues persist
- **Prevention**: Track remediation actions; require gap closure plan for each issue

❌ **MISTAKE: Inconsistent metric definitions across periods**
- **Impact**: Trending becomes meaningless; cannot compare periods accurately
- **Prevention**: Document metric definitions; maintain consistency in calculations

❌ **MISTAKE: Overwhelming executives with too much detail**
- **Impact**: Key messages lost; dashboard not read or acted upon
- **Prevention**: Executive summary on first page; detail in supporting sheets

❌ **MISTAKE: Not validating data before presenting to executives**
- **Impact**: Credibility loss; questions about data accuracy derail discussion
- **Prevention**: Security Manager review before CISO briefing; spot-check data sources

❌ **MISTAKE: Failing to archive previous dashboard versions**
- **Impact**: Cannot demonstrate historical governance; audit evidence gaps
- **Prevention**: Archive each period to ISMS Evidence Library with date stamp

❌ **MISTAKE: Not linking remediation actions to specific gaps**
- **Impact**: Unclear accountability; actions not tracked to completion
- **Prevention**: Maintain remediation register; link to dashboard gaps

❌ **MISTAKE: Ignoring partial compliance in scoring**
- **Impact**: Binary scoring misrepresents actual state; encourages gaming
- **Prevention**: Use graduated scoring; recognise progress towards targets

---

## 1.10 Quality Checklist

Before publishing the dashboard, verify:

### Data Quality Checks
- [ ] All source workbooks updated within last 30 days
- [ ] No broken formulas or #REF errors
- [ ] All metrics within expected ranges
- [ ] Historical data complete for trending
- [ ] Data refresh dates documented in Data_Sources sheet
- [ ] Source file paths verified and accessible
- [ ] No blank cells in required data fields

### Accuracy Checks
- [ ] BC/DR plan count matches BC Manager inventory
- [ ] Break-glass account count matches IAM records
- [ ] Personnel list matches HR records
- [ ] Security debt matches source register
- [ ] Disruption history complete and current
- [ ] Trend calculations verified against raw data
- [ ] Overall compliance score calculated correctly

### Completeness Checks
- [ ] All dashboard sheets populated
- [ ] All periods included in trend analysis
- [ ] All disruption incidents documented
- [ ] All source workbooks linked
- [ ] CISO commentary section completed
- [ ] Current issues and alerts updated

### Presentation Checks
- [ ] Executive Dashboard summarises key points clearly
- [ ] Trend charts render correctly and are readable
- [ ] Commentary explains significant changes from previous period
- [ ] Remediation actions documented for all identified gaps
- [ ] Colour-coding correctly applied (green/yellow/red)
- [ ] No visual artefacts or formatting issues

### Validation Checks
- [ ] Metrics cross-checked with source systems
- [ ] Compliance score verified by independent calculation
- [ ] Trend direction verified (improving/stable/declining)
- [ ] Alert thresholds correctly triggered
- [ ] Previous period comparison accurate

### Approval Checks
- [ ] Security Manager reviewed for accuracy
- [ ] CISO approved dashboard content
- [ ] Executive briefing scheduled (if quarterly)
- [ ] Archived to ISMS Evidence Library with date stamp
- [ ] Version control updated

---

## 1.11 Review and Approval

### Approval Workflow

```
Security Administrator Updates Data
         │
         ▼
Security Manager Reviews
         │
         ▼
CISO Approves
         │
         ▼
Executive Briefing (Quarterly)
         │
         ▼
Archive to ISMS Evidence Library
```

---

## 1.12 Integration with Other Controls

### Related ISMS Controls

| Control | Relationship |
|---------|--------------|
| **A.5.1** | ISMS governance includes disruption security metrics |
| **A.5.35-36** | Compliance monitoring includes A.5.29 metrics |
| **A.5.30** | BC/DR metrics overlap |
| **A.8.13-14** | Backup/redundancy metrics related |

### Related ISMS-IMP Documents

| Document | Relationship |
|----------|--------------|
| **ISMS-IMP-A.5.29.1** | Primary source for BC/DR coverage |
| **ISMS-IMP-A.5.29.2** | Primary source for readiness metrics |
| **ISMS-IMP-A.5.29.3** | Primary source for recovery metrics |

---

# PART II: TECHNICAL SPECIFICATION

---

## 2.1 Workbook Architecture

### File Naming Convention

```
ISMS-IMP-A.5.29.4_Compliance_Dashboard_YYYYMMDD.xlsx
```

### Sheet Tab Order

1. Executive_Dashboard
2. BCDR_Security_Status
3. Emergency_Access_Status
4. Personnel_Status
5. Security_Debt_Status
6. Disruption_History
7. Trend_Analysis
8. Data_Sources
9. Instructions
10. Approval_SignOff

---

## 2.2 Sheet Specifications

### Sheet 1: Executive_Dashboard

| Row | Content |
|-----|---------|
| 1 | Header: "A.5.29 Information Security During Disruption - Executive Dashboard" |
| 3-5 | Overall Compliance Score (large display) |
| 7-12 | Key Metrics Summary (5 primary metrics with status) |
| 14-18 | Current Issues and Alerts |
| 20-25 | Trend Summary (mini-chart or indicators) |
| 27+ | CISO Commentary |

### Sheet 2: BCDR_Security_Status

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Plan_ID | 15 | Text | Required |
| B | Plan_Name | 35 | Text | Required |
| C | Plan_Type | 20 | Text | Required |
| D | Plan_Owner | 25 | Text | Required |
| E | Security_Section | 12 | List | Yes, No, Partial |
| F | CISO_Approved | 12 | List | Yes, No, Pending |
| G | Approval_Date | 15 | Date | If approved |
| H | Next_Review | 15 | Date | Required |
| I | Review_Overdue | 10 | Formula | =IF(H<TODAY(),"Yes","No") |
| J | Status | 12 | Formula | Calculated |

### Sheet 3: Emergency_Access_Status

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Account_ID | 15 | Text | Required |
| B | Account_Name | 25 | Text | Required |
| C | Account_Type | 20 | Text | Required |
| D | Last_Test_Date | 15 | Date | Required |
| E | Test_Required_By | 15 | Date | Annual from last test |
| F | Test_Status | 15 | Formula | =IF(E<TODAY(),"Overdue","Current") |
| G | Current_Status | 12 | List | Disabled, Enabled, Unknown |
| H | Credential_Current | 12 | List | Yes, No, Unknown |
| I | Logging_Verified | 12 | List | Yes, No |
| J | Readiness_Score | 10 | Formula | Calculated |

### Sheet 4: Personnel_Status

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Role_ID | 15 | Text | Required |
| B | Role_Name | 30 | Text | Required |
| C | Primary_Assigned | 10 | List | Yes, No |
| D | Backup1_Assigned | 10 | List | Yes, No |
| E | Backup2_Assigned | 10 | List | Yes, No |
| F | Cross_Training | 12 | List | Complete, Partial, None |
| G | Last_Contact_Test | 15 | Date | Required |
| H | Contact_Test_Status | 12 | Formula | Current/Overdue |
| I | Last_Drill | 15 | Date | Required |
| J | Drill_Status | 12 | Formula | Current/Overdue |
| K | Availability_Score | 10 | Formula | Calculated |

### Sheet 5: Security_Debt_Status

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Period | 15 | Text | YYYY-MM |
| B | Total_Open_Items | 15 | Number | Required |
| C | Items_0_30_Days | 15 | Number | Required |
| D | Items_31_60_Days | 15 | Number | Required |
| E | Items_61_90_Days | 15 | Number | Required |
| F | Items_Over_90_Days | 15 | Number | Required |
| G | Items_Closed | 15 | Number | Required |
| H | Closure_Rate | 12 | Formula | Closed/(Open+Closed) |
| I | Escalations | 10 | Number | Required |
| J | Executive_Escalations | 15 | Number | Required |

### Sheet 6: Disruption_History

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Incident_ID | 15 | Text | Required |
| B | Incident_Date | 15 | Date | Required |
| C | Incident_Type | 25 | Text | Required |
| D | Duration_Hours | 15 | Number | Required |
| E | Security_Posture_Level | 15 | List | Normal, Elevated, Degraded, Emergency |
| F | Emergency_Access_Used | 10 | List | Yes, No |
| G | Security_Incidents_During | 15 | Number | Required |
| H | Security_Compromises | 10 | List | Yes, No |
| I | Recovery_Phase_Completed | 15 | List | Immediate, Short-term, Medium-term, Long-term, Not Completed |
| J | Lessons_Learned_Complete | 10 | List | Yes, No |
| K | Security_Outcome | 15 | List | No Issues, Minor Issues, Major Issues |

### Sheet 7: Trend_Analysis

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Period | 15 | Text | YYYY-QN |
| B | BCDR_Coverage_Pct | 15 | Percentage | Required |
| C | Emergency_Test_Pct | 15 | Percentage | Required |
| D | Personnel_Availability_Pct | 15 | Percentage | Required |
| E | Security_Debt_Over90 | 15 | Number | Required |
| F | Disruptions_Count | 12 | Number | Required |
| G | Security_Incidents_Count | 15 | Number | Required |
| H | Overall_Score | 12 | Percentage | Calculated |
| I | Trend | 10 | Formula | Improving/Stable/Declining |

### Sheet 8: Data_Sources

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Source_ID | 15 | Text | Required |
| B | Source_Name | 35 | Text | Required |
| C | Source_Type | 20 | List | Workbook, Database, Manual Entry |
| D | File_Path | 50 | Text | Required |
| E | Sheet_Name | 25 | Text | If workbook |
| F | Last_Updated | 15 | Date | Required |
| G | Update_Frequency | 15 | Text | Required |
| H | Data_Owner | 25 | Text | Required |
| I | Link_Status | 12 | List | Active, Broken, Not Linked |

---

## 2.3 Data Validations

### Plan Type Validation
```
BCP, DRP, Crisis Management, IT Recovery, Other
```

### Security Posture Validation
```
Normal, Elevated, Degraded, Emergency
```

### Security Outcome Validation
```
No Issues, Minor Issues, Major Issues
```

### Recovery Phase Validation
```
Immediate, Short-term, Medium-term, Long-term, Not Completed
```

---

## 2.4 Conditional Formatting

### Executive_Dashboard Sheet

| Condition | Formatting |
|-----------|------------|
| Overall Score >= 90% | Green fill |
| Overall Score 70-89% | Yellow fill |
| Overall Score 50-69% | Orange fill |
| Overall Score < 50% | Red fill |

### BCDR_Security_Status Sheet

| Condition | Formatting |
|-----------|------------|
| CISO_Approved = "Yes" | Green fill |
| CISO_Approved = "No" | Red fill |
| Review_Overdue = "Yes" | Bold red text |

### Security_Debt_Status Sheet

| Condition | Formatting |
|-----------|------------|
| Items_Over_90_Days > 0 | Red fill |
| Items_61_90_Days > 0 | Orange fill |
| Closure_Rate < 50% | Red text |

---

## 2.5 Formula Specifications

### Executive Dashboard Formulas

```excel
# Overall Compliance Score
=AVERAGE(BCDR_Coverage, Emergency_Test_Pct, Personnel_Availability_Pct,
         (100%-Debt_Score), Recovery_Score)

# BC/DR Coverage
=COUNTIF(BCDR_Security_Status!F:F,"Yes")/COUNT(BCDR_Security_Status!A:A)

# Emergency Test Completion
=COUNTIF(Emergency_Access_Status!F:F,"Current")/COUNT(Emergency_Access_Status!A:A)

# Personnel Availability
=AVERAGEIF(Personnel_Status!K:K,">0")

# Security Debt Score (Lower is better)
=Security_Debt_Status![Most Recent Items_Over_90_Days]/Total_Items

# Trend Indicator
=IF(Current>Previous,"Improving",IF(Current<Previous,"Declining","Stable"))
```

### Readiness Score Formula (Emergency Access)

```excel
# Readiness Score (0-100)
=(IF(F="Current",30,0)+IF(G="Disabled",30,0)+IF(H="Yes",20,0)+IF(I="Yes",20,0))
```

### Availability Score Formula (Personnel)

```excel
# Availability Score (0-100)
=(IF(C="Yes",25,0)+IF(D="Yes",25,0)+IF(E="Yes",15,0)+
  IF(F="Complete",15,IF(F="Partial",7,0))+
  IF(H="Current",10,0)+IF(J="Current",10,0))
```

---

## 2.6 Cell Styling Standards

### Dashboard Header Styling
- **Font**: Calibri 18pt Bold White
- **Fill**: Navy Blue (#003366)
- **Alignment**: Centre, Middle
- **Row Height**: 45

### Metric Display Styling
- **Font**: Calibri 36pt Bold (for main score)
- **Fill**: Based on conditional formatting
- **Alignment**: Centre, Middle

### Standard Header Styling
- **Font**: Calibri 14pt Bold White
- **Fill**: Navy Blue (#003366)
- **Alignment**: Centre, Middle, Wrap Text
- **Row Height**: 30

### Column Header Styling
- **Font**: Calibri 10pt Bold
- **Fill**: Light Grey (#D9D9D9)
- **Alignment**: Centre, Middle, Wrap Text
- **Border**: Thin black all sides

### Input Cell Styling
- **Fill**: Light Yellow (#FFFFCC)
- **Border**: Thin black all sides
- **Alignment**: Left, Middle, Wrap Text

### Formula Cell Styling
- **Fill**: Light Green (#E2EFDA)
- **Border**: Thin black all sides
- **Protection**: Locked

### Status Indicator Styling
- **Compliant (>=90%)**: Green fill (#C6EFCE), Dark green text (#006100)
- **Partial (70-89%)**: Yellow fill (#FFEB9C), Dark yellow text (#9C5700)
- **Non-Compliant (50-69%)**: Orange fill (#FFC7CE), Dark orange text (#9C0006)
- **Critical (<50%)**: Red fill (#FF0000), White text

### Commentary Section Styling
- **Font**: Calibri 11pt Regular
- **Fill**: White
- **Border**: Thin grey all sides
- **Alignment**: Left, Top, Wrap Text

---

## 2.7 Generator Script Reference

**Script Name**: `generate_a529_4_compliance_dashboard.py`

**Location**: `10-isms-scr-base/isms-a.5.29-security-during-disruption/10_generator-master/`

**Output**: `ISMS-IMP-A.5.29.4_Compliance_Dashboard_YYYYMMDD.xlsx`

**Dependencies**:
- openpyxl
- logging
- datetime

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-03 -->
