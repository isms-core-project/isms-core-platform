<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.35-36.S4-UG:framework:UG:a.5.35-36 -->
**ISMS-IMP-A.5.35-36.S4-UG - Compliance and Review Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.35-36

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.35-36.S4-UG |
| **Title** | Compliance and Review Dashboard |
| **Control Reference** | ISO/IEC 27001:2022 A.5.35-36 |
| **Control Name** | Compliance and Review |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

### Assessment Overview

**Purpose**

This dashboard workbook provides consolidated compliance monitoring for both A.5.35 (Independent Review) and A.5.36 (Compliance Verification) controls. It aggregates metrics from the other assessment workbooks to provide executive-level visibility into ISMS compliance and review status.

**Scope**

This dashboard covers:
- Executive summary of ISMS compliance status
- Independent review tracking and outcomes
- Policy and control compliance overview
- Findings metrics and aging analysis
- Key performance indicators
- Trend analysis over time

**What This Dashboard Covers**

| Domain | Dashboard Focus |
|--------|-----------------|
| Executive Summary | High-level compliance overview |
| Review Status | Independent review tracking |
| Compliance Status | Policy/control compliance metrics |
| Findings Overview | Findings metrics and aging |
| KPI Scorecard | Key performance indicators |
| Trends | Historical compliance tracking |

**Control Requirements**

ISO 27001:2022 Controls A.5.35 and A.5.36 together address the complete compliance and review lifecycle. This dashboard tracks compliance with both controls in a unified view, supporting management reporting and continuous improvement.

### Prerequisites

Before completing this dashboard:

- [ ] Completed ISMS-IMP-A.5.35-36.S1 (Independent Review Planning & Tracking)
- [ ] Completed ISMS-IMP-A.5.35-36.S2 (Compliance Assessment)
- [ ] Completed ISMS-IMP-A.5.35-36.S3 (Findings & Remediation Management)
- [ ] Access to compliance metrics from underlying assessments
- [ ] Finding and remediation status from responsible parties

### Completion Walkthrough

**Step 1: Executive_Summary Sheet**

Populate the executive overview section:

1. **Reporting_Period** - Period covered (e.g., Q1 2026)
2. **Report_Date** - Date dashboard prepared
3. **Prepared_By** - Person preparing dashboard
4. **Overall_ISMS_Status** - Green / Amber / Red
5. **Overall_Compliance_Score** - Percentage
6. **Independent_Review_Status** - On Track / Delayed / Completed
7. **Critical_Findings_Open** - Count of open Critical findings
8. **High_Findings_Open** - Count of open High findings
9. **Overdue_Actions** - Count of overdue remediation actions
10. **Key_Message_1** - First key message for management
11. **Key_Message_2** - Second key message
12. **Key_Message_3** - Third key message
13. **Priority_Actions** - Actions requiring management attention
14. **Next_Steps** - Planned activities for next period

**Status Thresholds**:

| Status | Criteria |
|--------|----------|
| Green | Compliance >90%, no Critical findings open, <5% overdue |
| Amber | Compliance 70-90%, or High findings open, or 5-15% overdue |
| Red | Compliance <70%, or Critical findings open, or >15% overdue |

**Step 2: Review_Status Sheet**

Track independent review status:

1. **Review_ID** - Link to ISMS-IMP-A.5.35-36.S1
2. **Review_Type** - Type of review
3. **Planned_Date** - Originally scheduled date
4. **Actual_Date** - When conducted (if complete)
5. **Status** - Scheduled / In Progress / Completed / Overdue
6. **Reviewer** - Who conducted the review
7. **Overall_Opinion** - Effective / Partially Effective / Ineffective
8. **Findings_Critical** - Count of Critical findings
9. **Findings_High** - Count of High findings
10. **Findings_Total** - Total findings count
11. **Report_Issued** - Yes / No
12. **Actions_Agreed** - Yes / No
13. **Notes** - Key observations

**Review Summary Metrics**:

| Metric | Calculation | Target |
|--------|-------------|--------|
| Review Completion Rate | Completed / Scheduled | 100% |
| Reviews On Schedule | On-time / Total | >95% |
| Positive Opinions | Effective / Total | >80% |

**Step 3: Compliance_Status Sheet**

Track compliance by area:

1. **Compliance_Area** - Policy or control category
2. **Last_Assessment** - Date of last assessment
3. **Next_Assessment** - Date of next planned assessment
4. **Compliance_Score** - Percentage score
5. **Status** - Compliant / Partial / Non-Compliant
6. **Trend** - Improving / Stable / Declining
7. **Open_NonCompliance** - Count of open NC items
8. **Key_Issues** - Summary of main issues
9. **Owner** - Accountable person
10. **Notes** - Additional observations

**Compliance Areas** (typical list):

| Area | Focus |
|------|-------|
| Information Security Policy | ISMS-POL-01 compliance |
| Access Control | A.5.15-18 compliance |
| Asset Management | A.5.9-11 compliance |
| Cryptography | A.8.24 compliance |
| Operations Security | A.8.x operational controls |
| Incident Management | A.5.24-28 compliance |
| Compliance | A.5.31-36 compliance |
| [Add all applicable areas] | |

**Step 4: Findings_Overview Sheet**

Analyse findings metrics:

1. **Period** - Reporting period
2. **Total_Open** - Total open findings
3. **Critical_Open** - Open Critical count
4. **High_Open** - Open High count
5. **Medium_Open** - Open Medium count
6. **Low_Open** - Open Low count
7. **Closed_This_Period** - Closed during period
8. **Opened_This_Period** - New findings identified
9. **Overdue** - Past target resolution date
10. **Overdue_Critical** - Overdue Critical findings
11. **Overdue_High** - Overdue High findings
12. **Avg_Age_Days** - Average age of open findings
13. **Oldest_Finding** - Age of oldest open finding
14. **MTTR_Critical** - Mean time to resolve Critical
15. **MTTR_High** - Mean time to resolve High

**Aging Analysis Buckets**:

| Age Bucket | Definition |
|------------|------------|
| 0-30 days | Newly identified |
| 31-60 days | Active remediation |
| 61-90 days | Extended remediation |
| 91+ days | Long-standing (escalate) |

**Step 5: KPI_Scorecard Sheet**

Track key performance indicators:

1. **KPI_ID** - Unique identifier
2. **KPI_Name** - KPI description
3. **Target** - Target value
4. **Current_Value** - Actual value
5. **Prior_Period** - Previous period value
6. **Trend** - Up / Down / Stable
7. **Status** - On Track / At Risk / Behind
8. **Owner** - Accountable person
9. **Notes** - Commentary

**Core KPIs**:

| KPI | Target | Measurement |
|-----|--------|-------------|
| Independent review completion | 100% | Scheduled vs. completed |
| Compliance assessment completion | 100% | Scheduled vs. completed |
| Overall compliance score | >90% | Average compliance score |
| Finding closure rate | >90% | Closed on time vs. total |
| Critical finding MTTR | <30 days | Mean time to remediate |
| High finding MTTR | <60 days | Mean time to remediate |
| Overdue findings | <5% | Overdue vs. total open |
| Review opinion positive | >80% | Effective opinions vs. total |

**Step 6: Trend_Analysis Sheet**

Record compliance trends over time:

1. **Period** - Quarter/Year (e.g., Q1 2026)
2. **Period_End_Date** - End date of period
3. **Reviews_Completed** - Count of reviews completed
4. **Reviews_Planned** - Count planned for period
5. **Compliance_Score** - Overall compliance percentage
6. **Score_Change** - Change from prior period
7. **Open_Findings_Total** - Total open at period end
8. **Open_Critical** - Open Critical at period end
9. **Open_High** - Open High at period end
10. **Closed_in_Period** - Findings closed during period
11. **MTTR_Critical** - Critical MTTR for period
12. **MTTR_High** - High MTTR for period
13. **Overall_Status** - Green / Amber / Red
14. **Notes** - Period commentary

**Trend Requirements**:

- Maintain at least 8 quarters of history
- Show clear trends (improving/declining)
- Highlight significant changes
- Identify seasonal patterns

**Step 7: Approval_SignOff Sheet**

Obtain dashboard approval:

1. **Report_Period** - Period covered
2. **Prepared_By** - Preparer name
3. **Prepared_Date** - Date prepared
4. **Reviewed_By** - ISM name
5. **Review_Date** - Date reviewed
6. **Approved_By** - CISO name
7. **Approval_Date** - Date approved
8. **Presented_To** - Management group presented to
9. **Presentation_Date** - Date of presentation
10. **Comments** - Any conditions or follow-ups

### Evidence Collection

**Required Evidence**:

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Underlying Assessments | Completed ISMS-IMP-A.5.35-36.S1-3 | ISMS Evidence Library |
| Dashboard Reports | Generated dashboard exports | ISMS Evidence Library |
| KPI Calculations | Working data for KPIs | ISMS Evidence Library |
| Management Presentations | Executive summaries presented | ISMS Evidence Library |
| Meeting Minutes | Management review discussions | ISMS Evidence Library |

### Common Pitfalls

❌ **MISTAKE**: Using outdated data from underlying assessments
✅ **CORRECT**: Ensure all source assessments are current before updating dashboard

❌ **MISTAKE**: Not tracking trends over time
✅ **CORRECT**: Maintain historical data to show compliance trajectory

❌ **MISTAKE**: KPIs without clear targets
✅ **CORRECT**: Every KPI must have a defined target

❌ **MISTAKE**: Dashboard not reviewed before management presentation
✅ **CORRECT**: ISM reviews for accuracy before CISO presentation

❌ **MISTAKE**: Ignoring negative trends
✅ **CORRECT**: Highlight deteriorating metrics with action plans

❌ **MISTAKE**: Complex dashboard that obscures key messages
✅ **CORRECT**: Clear, focused executive summary with priorities

❌ **MISTAKE**: No drill-down capability to source data
✅ **CORRECT**: Maintain links to underlying assessments

❌ **MISTAKE**: Missing sign-off on management-presented dashboards
✅ **CORRECT**: All dashboards presented to management should be approved

### Quality Checklist

Before presenting:

- [ ] All source assessments are current (within 30 days)
- [ ] KPI values calculated correctly
- [ ] All metrics linked to source data
- [ ] Trends include at least 4 data points
- [ ] Executive summary reflects key messages
- [ ] Status thresholds applied consistently
- [ ] Overdue items escalated appropriately
- [ ] Approval signatures obtained

### Review & Approval

**Review Workflow**:

1. Assessor compiles dashboard from source assessments
2. ISM verifies accuracy and completeness
3. CISO reviews for management presentation
4. Executive Management receives quarterly briefing

**Presentation Cadence**:

| Frequency | Audience | Content |
|-----------|----------|---------|
| Monthly | CISO | Metrics update, issues |
| Quarterly | Executive Management | Full dashboard, trends |
| Annually | Board/Audit Committee | Annual summary, outlook |

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
