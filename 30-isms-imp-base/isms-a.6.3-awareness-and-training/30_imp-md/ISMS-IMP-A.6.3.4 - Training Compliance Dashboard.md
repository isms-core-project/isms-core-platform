**ISMS-IMP-A.6.3.4 - Training Compliance Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.6.3: Information Security Awareness, Education and Training

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.3.4 |
| **Version** | 1.0 |
| **Assessment Area** | Training Program Effectiveness and Compliance Reporting |
| **Related Policy** | ISMS-POL-A.6.3, Section 3 (Roles and Responsibilities), Section 4 (Evidence Requirements) |
| **Purpose** | Consolidate training metrics, measure program effectiveness, generate compliance reports, and support audit evidence requirements |
| **Target Audience** | CISO, Information Security Officers, HR Directors, Internal Audit, Management |
| **Assessment Type** | Executive Reporting & Compliance Monitoring |
| **Review Cycle** | Monthly reporting + Quarterly management review + Annual effectiveness assessment |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Initial | Initial specification for Training Compliance Dashboard workbook | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** CISO, Information Security Officers, HR Directors, Internal Audit

---

# Assessment Overview

## What This Assessment Measures

This workbook consolidates training program data to provide executive-level compliance visibility, effectiveness measurement, and audit-ready reporting per ISMS-POL-A.6.3 requirements.

**Scope:** 5 reporting domains:
1. **Organizational Compliance** - Overall training completion and compliance status
2. **Effectiveness Metrics** - Behavioral change and risk reduction indicators
3. **Trend Analysis** - Historical performance and trajectory
4. **Risk Indicators** - Training-related security risk visibility
5. **Audit Readiness** - Evidence status and compliance gaps

**Assessment Output:** Excel workbook providing:
- Executive summary dashboard
- Compliance metrics by department, tier, and module
- Effectiveness measurements and KPIs
- Trend analysis with historical comparison
- Risk heat maps for training gaps
- Audit evidence checklist and status
- Management review input reports

## Why This Matters

**ISO 27001:2022 Requirements:**
- Clause 9.1: Monitoring, measurement, analysis and evaluation
- Clause 9.3: Management review inputs include "effectiveness of the ISMS"
- Control A.6.3: Requires evidence of competence and training effectiveness

**Business Impact:**
- **Executive Visibility:** Clear compliance status for leadership decision-making
- **Risk Prioritization:** Identify highest-risk training gaps for targeted intervention
- **Audit Efficiency:** Pre-assembled evidence reduces audit preparation time
- **Continuous Improvement:** Trend data enables program optimization
- **Resource Justification:** Metrics support training investment decisions

## Who Should Complete This Assessment

**Primary Responsibility:** Information Security Officer / Training Program Manager

**Report Consumers:**
1. **CISO** - Strategic oversight, risk decisions, resource allocation
2. **HR Director** - Organizational compliance, remediation coordination
3. **Department Managers** - Team compliance status, intervention needs
4. **Internal Audit** - Evidence verification, compliance assessment
5. **Executive Management** - ISMS performance reporting

## Connection to Policy

This workbook supports **ISMS-POL-A.6.3, Section 4 (Evidence Requirements)**:
- Section 4.1: Stage 1 Documentation Evidence
- Section 4.2: Stage 2 Operational Evidence
- Section 3.2: CISO responsibilities for program effectiveness

---

# Workbook Structure Overview

## Sheet 1: Instructions
Dashboard usage guidance and data refresh procedures

## Sheet 2: Executive_Summary
**Purpose:** High-level compliance status for leadership

**Metrics Displayed:**
- Overall completion rate (current vs. target)
- Compliance trend (3-month, 6-month, 12-month)
- Top 5 risk areas
- Remediation status summary
- Key achievements
- Required actions

**Visual Elements:**
- Compliance gauge chart
- Traffic light indicators
- Trend sparklines

## Sheet 3: Compliance_Metrics
**Purpose:** Detailed compliance breakdowns

**Sections:**
- **By Department:** Completion rate, overdue count, average score
- **By Training Tier:** Tier 1-7 compliance status
- **By Module:** Individual module completion and pass rates
- **By Employment Type:** Full-time, contractor, third-party
- **By Time Period:** Monthly, quarterly, annual views

**Columns:**
- Category
- Total_Population
- Training_Required
- Completed
- Completion_Rate
- On_Time_Rate
- Average_Score
- Overdue_Count
- Remediation_Active
- Compliance_Status

## Sheet 4: Effectiveness_Metrics
**Purpose:** Measure training impact on security behavior

**Columns:**
- Metric_Category
- Metric_Name
- Baseline_Value
- Current_Value
- Target_Value
- Trend_Direction
- Period_Comparison
- Data_Source
- Notes

**Key Metrics:**
- Phishing simulation click rate (trend)
- Phishing report rate (trend)
- Security incident rate (training-related)
- Policy violation rate
- Assessment pass rates (first attempt vs. retake)
- Time to complete training
- Knowledge retention (re-assessment scores)

## Sheet 5: Trend_Analysis
**Purpose:** Historical performance tracking

**Columns:**
- Period (Month/Quarter)
- Completion_Rate
- On_Time_Rate
- Average_Score
- Phishing_Click_Rate
- Phishing_Report_Rate
- Incident_Count
- Remediation_Count
- Compliance_Score

**Visual Elements:**
- Line charts for key metrics over time
- Comparison to previous year same period
- Trend indicators (improving/stable/declining)

## Sheet 6: Risk_Heatmap
**Purpose:** Visual risk identification for training gaps

**Dimensions:**
- Rows: Departments or Roles
- Columns: Risk factors (Overdue training, Failed assessments, Phishing failures, Incident history)

**Risk Scoring:**
- Critical (Red): Multiple risk factors, significant gaps
- High (Orange): Single major risk factor or multiple moderate
- Medium (Yellow): Moderate risk factors
- Low (Green): Compliant, no significant risks

**Columns:**
- Entity (Department/Role)
- Overdue_Risk_Score
- Assessment_Risk_Score
- Simulation_Risk_Score
- Incident_Risk_Score
- Combined_Risk_Level
- Priority_Rank
- Recommended_Action

## Sheet 7: Audit_Evidence
**Purpose:** Evidence checklist for audit readiness

**Sections:**
- **Stage 1 Documentation Evidence:**
  - Training policy approved
  - Curriculum documented
  - Roles assigned
  - Procedures documented

- **Stage 2 Operational Evidence:**
  - Completion records available
  - Assessment results documented
  - Simulation results tracked
  - Remediation records maintained
  - Effectiveness metrics collected

**Columns:**
- Evidence_Category
- Evidence_Item
- Required_For
- Status (Available/Partial/Missing)
- Location
- Last_Updated
- Responsible_Party
- Notes

## Sheet 8: Management_Review_Input
**Purpose:** Prepared input for management review meetings

**Sections:**
- Training program status summary
- Effectiveness assessment
- Non-conformities and corrective actions
- Resource requirements
- Recommendations for improvement
- Changes affecting training program

**Format:** Narrative sections with supporting metrics

## Sheet 9: KPI_Definitions
**Purpose:** Reference for all metrics and KPIs

**Columns:**
- KPI_ID
- KPI_Name
- Definition
- Calculation_Method
- Data_Source
- Target_Value
- Measurement_Frequency
- Owner
- Reporting_Level

## Sheet 10: Data_Sources
**Purpose:** Document data inputs and refresh procedures

**Columns:**
- Data_Element
- Source_System
- Source_Sheet (from A.6.3.1-3)
- Refresh_Frequency
- Last_Refresh
- Responsible_Party
- Validation_Method

## Sheet 11: Evidence_Register
Supporting documentation references

## Sheet 12: Dashboard
Visual summary with charts

## Sheet 13: Approval_Sign_Off
Formal review and attestation

---

# Dashboard Usage Guide

## Intended Audiences and Use Cases

| Audience | Primary Use | Key Sheets | Frequency |
|----------|-------------|------------|-----------|
| **CISO** | Strategic oversight, risk decisions | Executive_Summary, Risk_Heatmap | Weekly review |
| **ISO** | Program management, compliance monitoring | All sheets | Daily/Weekly |
| **HR Director** | Organizational compliance, intervention planning | Compliance_Metrics, Overdue alerts | Weekly |
| **Department Managers** | Team compliance, remediation | Compliance_Metrics (filtered) | Weekly |
| **Internal Audit** | Evidence verification, compliance assessment | Audit_Evidence, all data sheets | Quarterly/As needed |
| **Executive Committee** | ISMS performance reporting | Executive_Summary, Management_Review_Input | Quarterly |

## Dashboard Interpretation Guide

### Executive Summary Traffic Lights

| Indicator | Green | Yellow | Red |
|-----------|-------|--------|-----|
| **Completion Rate** | ≥95% | 85-94% | <85% |
| **On-Time Rate** | ≥90% | 80-89% | <80% |
| **Phishing Click Rate** | ≤5% | 6-15% | >15% |
| **Phishing Report Rate** | ≥70% | 50-69% | <50% |
| **Remediation Success** | ≥95% | 85-94% | <85% |

### Risk Heatmap Interpretation

**Combined Risk Levels:**
- **Critical (Red):** Immediate action required. Department has multiple significant risk factors. Escalate to CISO.
- **High (Orange):** Priority attention needed. Schedule intervention within 30 days.
- **Medium (Yellow):** Monitor closely. Include in regular management review.
- **Low (Green):** Compliant. Continue normal operations.

**Risk Factor Scoring:**

| Score | Overdue Training | Assessment Failures | Simulation Failures | Incident History |
|-------|------------------|---------------------|---------------------|------------------|
| 0 | 0% overdue | <5% fail rate | <5% click rate | No incidents |
| 1 | 1-5% overdue | 5-10% fail rate | 5-10% click rate | 1 minor incident |
| 2 | 6-15% overdue | 11-20% fail rate | 11-20% click rate | 2-3 incidents |
| 3 | >15% overdue | >20% fail rate | >20% click rate | 4+ or 1 major |

### Trend Analysis Guidance

**Positive Trends (Improving):**
- Completion rate increasing
- Click rate decreasing
- Report rate increasing
- Average scores improving

**Negative Trends (Require Attention):**
- Any metric declining for 2+ consecutive periods
- Sudden changes (>10% movement in single period)
- Divergence between departments (one falling behind)

---

# Reporting Procedures

## Monthly Compliance Report

**Generated By:** Information Security Officer
**Due:** By 5th business day of following month
**Distribution:** CISO, HR Director, Department Managers

**Report Contents:**
1. **Executive Summary** (1 page)
   - Overall compliance status (traffic lights)
   - Key metrics vs. targets
   - Critical issues requiring attention
   - Achievements and improvements

2. **Compliance Detail** (by department)
   - Completion rates
   - Overdue training count
   - Remediation cases

3. **Action Items**
   - Departments requiring intervention
   - Escalated cases
   - Recommended actions

**Process:**
1. Refresh data from source workbooks (A.6.3.1-3)
2. Update all calculated metrics
3. Generate Executive_Summary export
4. Prepare narrative summary
5. Distribute via secure email

## Quarterly Effectiveness Report

**Generated By:** Information Security Officer with Training Manager
**Due:** Within 10 business days of quarter end
**Distribution:** CISO, Security Committee, HR Leadership

**Report Contents:**
1. **Effectiveness Analysis**
   - Behavioral metrics trends
   - Simulation campaign results analysis
   - Knowledge retention assessment
   - Correlation with incident data

2. **Program Assessment**
   - What's working
   - Areas for improvement
   - Resource needs

3. **Recommendations**
   - Program adjustments
   - Content updates needed
   - Budget/resource requests

**Process:**
1. Compile quarterly data
2. Perform trend analysis
3. Correlate with incident/violation data
4. Draft recommendations
5. Present to CISO for review
6. Present to Security Committee

## Annual Program Review

**Generated By:** Training Manager with ISO
**Due:** Within 30 days of year end
**Distribution:** CISO, Executive Management, Board (summary)

**Report Contents:**
1. **Year in Review**
   - All KPIs vs. annual targets
   - Significant achievements
   - Challenges encountered

2. **Program Effectiveness**
   - Overall behavioral impact assessment
   - ROI analysis (if measurable)
   - Benchmark comparison (industry if available)

3. **Next Year Planning**
   - Recommended targets
   - Program changes
   - Budget requirements
   - New initiatives

## Ad-Hoc Audit Response

**Process:**
1. Receive evidence request from auditor
2. Identify relevant data in Audit_Evidence sheet
3. Extract requested records from source workbooks
4. Prepare evidence package with:
   - Cover sheet explaining contents
   - Extracted data (sanitized if needed)
   - Supporting documentation
5. Log evidence provision in Evidence_Register

---

# Evidence Collection

## Dashboard-Generated Evidence

This workbook automatically generates audit evidence:

| Report | Evidence Value | Retention |
|--------|---------------|-----------|
| Monthly Compliance Report | Demonstrates ongoing monitoring (Cl.9.1) | 3 years |
| Quarterly Effectiveness Report | Demonstrates effectiveness evaluation (Cl.9.1) | 3 years |
| Annual Program Review | Demonstrates continual improvement (Cl.10.1) | 5 years |
| Management Review Input | Supports management review (Cl.9.3) | 5 years |

## Evidence Storage

**Location:** ISMS Evidence Library / A.6.3 Training / Dashboard_Reports / [Year] /

**Naming Convention:**
- `ISMS-A.6.3.4_Monthly_Compliance_[YYYY-MM].pdf`
- `ISMS-A.6.3.4_Quarterly_Effectiveness_[YYYY-QX].pdf`
- `ISMS-A.6.3.4_Annual_Review_[YYYY].pdf`

**Archive Schedule:**
- Monthly reports: Archive after 3 years, delete after 5 years
- Quarterly reports: Archive after 3 years, delete after 5 years
- Annual reports: Archive after 5 years, delete after 7 years

---

# Common Pitfalls

## ❌ MISTAKE #1: Presenting Data Without Context

**The Problem:** Showing metrics without explaining what they mean or what action is needed.

**Why It Matters:** Executives can't act on data they don't understand. Reports become ignored.

**The Fix:**
- Always include interpretation guidance
- Highlight what changed and why it matters
- Include specific recommended actions
- Use traffic lights for quick understanding

## ❌ MISTAKE #2: Stale Data

**The Problem:** Dashboard shows outdated information; decisions made on old data.

**Why It Matters:** Wrong decisions. Loss of credibility. Compliance gaps undetected.

**The Fix:**
- Document refresh schedule for each data source
- Display "Last Updated" prominently
- Automate refreshes where possible
- Flag when data is >7 days old

## ❌ MISTAKE #3: Vanity Metrics

**The Problem:** Reporting metrics that look good but don't indicate actual security improvement.

**Why It Matters:** False sense of progress. Resources invested without return. Real risks hidden.

**The Fix:**
- Focus on behavioral and outcome metrics
- Track correlation between training and incidents
- Include leading AND lagging indicators
- Be honest about what metrics actually measure

## ❌ MISTAKE #4: One-Size-Fits-All Reporting

**The Problem:** Same report for CISO, department managers, and auditors.

**Why It Matters:** Too detailed for executives, not detailed enough for operations, wrong format for audit.

**The Fix:**
- Tailor reports to audience
- Executive summary for leadership
- Detailed breakdowns for operational managers
- Evidence packages for audit

## ❌ MISTAKE #5: No Historical Comparison

**The Problem:** Showing only current status without trend or comparison.

**Why It Matters:** Can't tell if improving or declining. No context for "good" or "bad."

**The Fix:**
- Always include trend data (month-over-month, quarter-over-quarter)
- Compare to previous year same period
- Show progress toward targets
- Highlight significant changes

## ❌ MISTAKE #6: Ignoring Low-Risk Areas

**The Problem:** Only focusing on red/critical items, ignoring green areas that might be degrading.

**Why It Matters:** Green areas can turn yellow, yellow can turn red. Early intervention is cheaper.

**The Fix:**
- Monitor all areas, not just problems
- Track direction of change (stable, improving, declining)
- Celebrate sustained compliance (reinforces good behavior)
- Set threshold for early warning (before red)

## ❌ MISTAKE #7: Incomplete Audit Evidence Tracking

**The Problem:** Audit_Evidence sheet not maintained; scrambling when auditors arrive.

**Why It Matters:** Audit preparation is stressful and time-consuming. Missing evidence = findings.

**The Fix:**
- Update Audit_Evidence sheet monthly
- Verify evidence locations are accurate
- Pre-stage evidence for common audit requests
- Conduct mock audit evidence review quarterly

## ❌ MISTAKE #8: Not Linking to Business Impact

**The Problem:** Security metrics not connected to business language or outcomes.

**Why It Matters:** Business leaders don't understand security jargon. Budget requests ignored.

**The Fix:**
- Translate to business impact where possible
- Show cost of incidents (when training gaps contributed)
- Express risk in terms executives understand
- Connect to strategic objectives

## ❌ MISTAKE #9: Manual Dashboard Updates

**The Problem:** Manually updating dashboard from multiple source workbooks, introducing errors.

**Why It Matters:** Errors in reporting. Time-consuming. Inconsistent updates.

**The Fix:**
- Use formulas to pull from source sheets
- Establish data validation checks
- Document refresh procedures
- Consider automation tools for larger organizations

## ❌ MISTAKE #10: No Action Follow-Through

**The Problem:** Dashboard identifies issues but no tracking of resolution.

**Why It Matters:** Same issues appear month after month. Dashboard becomes ignored.

**The Fix:**
- Every critical/high risk item gets assigned owner
- Track action items to resolution
- Report on closure rate
- Escalate unresolved items

---

# Quality Checklist

## Data Quality Checks

- [ ] All source data refreshed within expected timeframe
- [ ] "Last Updated" dates accurate
- [ ] No #REF! or #VALUE! errors in formulas
- [ ] Totals reconcile with source workbooks
- [ ] Personnel count matches HR headcount

## Metric Accuracy Checks

- [ ] Completion rate calculation verified (spot check)
- [ ] Traffic light thresholds applied correctly
- [ ] Risk scores calculate correctly
- [ ] Trend direction indicators accurate
- [ ] KPI values match definitions

## Report Quality Checks

- [ ] Executive summary reflects data accurately
- [ ] All charts render correctly
- [ ] No stale data (>7 days old)
- [ ] Narrative sections updated
- [ ] Action items are specific and actionable

## Audit Readiness Checks

- [ ] Audit_Evidence sheet current
- [ ] All evidence locations verified accessible
- [ ] Evidence retention periods appropriate
- [ ] Gap items have remediation plans

---

# Review & Approval

## Monthly Attestation

**Completed By:** Information Security Officer
**Review Points:**
- Data refresh verified
- Metrics calculated correctly
- Report generated and distributed
- Critical issues escalated

**Approved By:** CISO (for reports to executive)

## Quarterly Effectiveness Review

**Presented To:** Security Committee / CISO
**Includes:**
- Quarterly effectiveness report
- Trend analysis
- Recommendations

**Documentation:**
- Meeting minutes with decisions
- Approved report stored as evidence

## Annual Program Review

**Presented To:** Executive Management
**Includes:**
- Annual program review
- Next year targets and budget
- Program improvement recommendations

**Approval Required:**
- CISO approval of report content
- Executive approval of next year targets/budget

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Generator Script Developers

---

# Excel Workbook Technical Specification

## Workbook Metadata

```python
DOCUMENT_ID = "ISMS-IMP-A.6.3.4"
WORKBOOK_NAME = "Training_Compliance_Dashboard"
CONTROL_ID = "A.6.3"
CONTROL_NAME = "Information Security Awareness, Education and Training"
```

## Sheet Specifications

### Sheet 2: Executive_Summary

**Layout:** Dashboard format with summary cards and charts

**Summary Cards:**
| Row | Metric | Formula Concept |
|-----|--------|-----------------|
| 1 | Overall Compliance Rate | =Completed/Required |
| 2 | Current Month Completion | =Month completions count |
| 3 | Overdue Training Count | =COUNTIF(Status="Overdue") |
| 4 | Average Assessment Score | =AVERAGE(Scores) |
| 5 | Active Remediation Cases | =COUNTIF(Remediation="In Progress") |
| 6 | Phishing Click Rate | =Clicked/Sent |

**Traffic Light Logic:**
- Green: ≥95% compliance, <5% click rate
- Yellow: 85-94% compliance, 5-15% click rate
- Red: <85% compliance, >15% click rate

### Sheet 3: Compliance_Metrics

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Category | 20 | Text |
| B | Total_Population | 15 | Integer |
| C | Training_Required | 15 | Integer |
| D | Completed | 12 | Integer |
| E | Completion_Rate | 15 | Percentage (Formula) |
| F | On_Time_Rate | 15 | Percentage (Formula) |
| G | Average_Score | 15 | Percentage |
| H | Overdue_Count | 12 | Integer |
| I | Remediation_Active | 15 | Integer |
| J | Compliance_Status | 15 | Formula (Green/Yellow/Red) |

**Completion Rate Formula:**
```excel
=IF(C2>0, D2/C2, "N/A")
```

**Compliance Status Formula:**
```excel
=IF(E2>=0.95,"Green",IF(E2>=0.85,"Yellow","Red"))
```

**Conditional Formatting:**
- Completion_Rate <85%: Red background
- Completion_Rate 85-94%: Yellow background
- Completion_Rate ≥95%: Green background
- Overdue_Count >10: Bold red text

### Sheet 4: Effectiveness_Metrics

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Metric_Category | 20 | Dropdown |
| B | Metric_Name | 30 | Text |
| C | Baseline_Value | 15 | Number/Percentage |
| D | Current_Value | 15 | Number/Percentage |
| E | Target_Value | 15 | Number/Percentage |
| F | Trend_Direction | 15 | Formula |
| G | Period_Comparison | 18 | Text |
| H | Data_Source | 25 | Text |
| I | Notes | 40 | Text |

**Trend Direction Formula:**
```excel
=IF(D2>C2, IF(A2="Risk Metric", "↑ Worsening", "↑ Improving"), IF(D2<C2, IF(A2="Risk Metric", "↓ Improving", "↓ Declining"), "→ Stable"))
```

**Pre-Populated Metrics:**

```python
EFFECTIVENESS_METRICS = [
    ("Behavior", "Phishing Click Rate", None, None, "≤5%", "IMP-A.6.3.3 Simulation_Results"),
    ("Behavior", "Phishing Report Rate", None, None, "≥70%", "IMP-A.6.3.3 Simulation_Results"),
    ("Behavior", "Credential Submission Rate", None, None, "≤1%", "IMP-A.6.3.3 Simulation_Results"),
    ("Knowledge", "First-Attempt Pass Rate", None, None, "≥85%", "IMP-A.6.3.3 Assessment_Results"),
    ("Knowledge", "Average Assessment Score", None, None, "≥80%", "IMP-A.6.3.3 Assessment_Results"),
    ("Knowledge", "Remediation Success Rate", None, None, "≥95%", "IMP-A.6.3.3 Remediation_Tracking"),
    ("Compliance", "On-Time Completion Rate", None, None, "≥90%", "IMP-A.6.3.3 Completion_Tracking"),
    ("Compliance", "Annual Training Completion", None, None, "100%", "IMP-A.6.3.3 Completion_Tracking"),
    ("Risk", "Training-Related Incidents", None, None, "Decreasing", "Incident Management System"),
    ("Risk", "Policy Violations (Training Gap)", None, None, "Decreasing", "Policy Violation Log"),
]
```

### Sheet 6: Risk_Heatmap

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Entity | 25 | Text |
| B | Overdue_Risk_Score | 18 | Integer (0-3) |
| C | Assessment_Risk_Score | 18 | Integer (0-3) |
| D | Simulation_Risk_Score | 18 | Integer (0-3) |
| E | Incident_Risk_Score | 18 | Integer (0-3) |
| F | Combined_Risk_Level | 18 | Formula |
| G | Priority_Rank | 12 | Formula |
| H | Recommended_Action | 40 | Text |

**Risk Score Definitions:**
- 0: No risk indicators
- 1: Low (minor gaps, <5% overdue)
- 2: Medium (moderate gaps, 5-15% overdue)
- 3: High (significant gaps, >15% overdue or critical failures)

**Combined Risk Formula:**
```excel
=IF(SUM(B2:E2)>=8,"Critical",IF(SUM(B2:E2)>=5,"High",IF(SUM(B2:E2)>=2,"Medium","Low")))
```

**Conditional Formatting:**
- Risk scores 3: Red cell
- Risk scores 2: Orange cell
- Risk scores 1: Yellow cell
- Risk scores 0: Green cell
- Combined "Critical": Bold red background
- Combined "High": Orange background

### Sheet 7: Audit_Evidence

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Evidence_Category | 20 | Dropdown |
| B | Evidence_Item | 40 | Text |
| C | Required_For | 20 | Text |
| D | Status | 15 | Dropdown |
| E | Location | 35 | Text |
| F | Last_Updated | 12 | Date |
| G | Responsible_Party | 25 | Text |
| H | Notes | 40 | Text |

**Pre-Populated Evidence Items:**

```python
AUDIT_EVIDENCE = [
    # Stage 1 - Documentation
    ("Stage 1", "Training Policy (ISMS-POL-A.6.3)", "ISO 27001 A.6.3", None, None, "CISO"),
    ("Stage 1", "Training Needs Assessment (IMP-A.6.3.1)", "ISO 27001 A.6.3", None, None, "ISO/Training Manager"),
    ("Stage 1", "Training Curriculum Catalog (IMP-A.6.3.2)", "ISO 27001 A.6.3", None, None, "Training Manager"),
    ("Stage 1", "Role-to-Training Matrix", "ISO 27001 A.6.3", None, None, "HR/Security"),
    ("Stage 1", "Training Delivery Standards", "ISO 27001 A.6.3", None, None, "Training Manager"),

    # Stage 2 - Operational
    ("Stage 2", "Training Completion Records", "ISO 27001 Cl.7.2(d)", None, None, "HR/LMS Admin"),
    ("Stage 2", "Assessment Results and Scores", "ISO 27001 Cl.7.2(d)", None, None, "LMS Admin"),
    ("Stage 2", "Phishing Simulation Results", "ISO 27001 A.6.3", None, None, "Security Team"),
    ("Stage 2", "Remediation Tracking Records", "ISO 27001 A.6.3", None, None, "HR/Security"),
    ("Stage 2", "Compliance Reports (Monthly)", "ISO 27001 Cl.9.1", None, None, "ISO"),
    ("Stage 2", "Effectiveness Metrics (Quarterly)", "ISO 27001 Cl.9.1", None, None, "ISO"),
    ("Stage 2", "Management Review Minutes", "ISO 27001 Cl.9.3", None, None, "CISO"),
    ("Stage 2", "Training Program Review Records", "ISO 27001 Cl.10.1", None, None, "Training Manager"),
]
```

### Sheet 9: KPI_Definitions

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | KPI_ID | 12 | Text |
| B | KPI_Name | 30 | Text |
| C | Definition | 50 | Text |
| D | Calculation_Method | 40 | Text |
| E | Data_Source | 25 | Text |
| F | Target_Value | 15 | Text |
| G | Measurement_Frequency | 18 | Dropdown |
| H | Owner | 20 | Text |
| I | Reporting_Level | 18 | Dropdown |

**Pre-Populated KPIs:**

```python
KPI_DEFINITIONS = [
    ("KPI-001", "Training Completion Rate", "Percentage of required training completed", "(Completed / Required) × 100", "Completion_Tracking", "≥95%", "Monthly", "Training Manager", "Executive"),
    ("KPI-002", "On-Time Completion Rate", "Percentage completed before due date", "(On-Time / Completed) × 100", "Completion_Tracking", "≥90%", "Monthly", "Training Manager", "Executive"),
    ("KPI-003", "Assessment Pass Rate", "First-attempt pass rate", "(Passed First Attempt / Total Assessments) × 100", "Assessment_Results", "≥85%", "Monthly", "Training Manager", "Department"),
    ("KPI-004", "Phishing Click Rate", "Percentage clicking simulation links", "(Clicked / Sent) × 100", "Simulation_Results", "≤5%", "Per Campaign", "Security Team", "Executive"),
    ("KPI-005", "Phishing Report Rate", "Percentage reporting suspicious emails", "(Reported / Sent) × 100", "Simulation_Results", "≥70%", "Per Campaign", "Security Team", "Executive"),
    ("KPI-006", "Remediation Success Rate", "Percentage passing remediation training", "(Remediation Passed / Remediation Assigned) × 100", "Remediation_Tracking", "≥95%", "Monthly", "HR", "Department"),
    ("KPI-007", "Training Currency", "Percentage with current/non-expired training", "(Current / Total Required) × 100", "Completion_Tracking", "≥95%", "Monthly", "Training Manager", "Executive"),
    ("KPI-008", "Average Assessment Score", "Mean score across all assessments", "AVG(Assessment_Score)", "Assessment_Results", "≥80%", "Quarterly", "Training Manager", "Department"),
]
```

---

## Dashboard Charts Specification

### Chart 1: Compliance Gauge
- Type: Doughnut chart styled as gauge
- Value: Overall completion rate
- Bands: Red (0-85%), Yellow (85-95%), Green (95-100%)

### Chart 2: Compliance by Department
- Type: Horizontal bar chart
- Data: Department completion rates
- Color coding: By compliance status

### Chart 3: Trend Over Time
- Type: Line chart
- Series: Completion rate, Click rate, Report rate
- X-Axis: Last 12 months

### Chart 4: Risk Heatmap
- Type: Conditional formatted table
- Dimensions: Departments × Risk factors

### Chart 5: Training by Tier
- Type: Stacked bar chart
- Data: Completion status by training tier

---

## Data Integration Notes

**Data Sources (from other A.6.3 workbooks):**
- IMP-A.6.3.1: Role inventory, tier assignments
- IMP-A.6.3.2: Curriculum catalog, module specifications
- IMP-A.6.3.3: Completion tracking, assessment results, simulation results, remediation records

**Recommended Refresh Schedule:**
- Daily: Completion tracking, overdue alerts
- Weekly: Assessment results, remediation status
- Monthly: Compliance metrics, trend analysis
- Quarterly: Effectiveness metrics, risk heatmap
- Annually: Full program review, KPI targets

---

## QA Checklist

- [ ] All 13 sheets created
- [ ] Formulas calculate correctly
- [ ] Conditional formatting applied
- [ ] Dashboard charts render
- [ ] KPIs pre-populated
- [ ] Evidence checklist complete
- [ ] Data source references accurate
- [ ] Traffic light logic correct

---

# Document Control

**Document ID:** ISMS-IMP-A.6.3.4
**Version:** 1.0
**Classification:** Internal
**Status:** Draft

---

**END OF SPECIFICATION**

---

*"Highly composite numbers are like the dew-drops of heaven, which distil themselves from the universe."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-01 -->
