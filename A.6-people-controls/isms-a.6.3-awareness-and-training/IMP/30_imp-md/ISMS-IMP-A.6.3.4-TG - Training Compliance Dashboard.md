**ISMS-IMP-A.6.3.4-TG - Training Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.3: Information Security Awareness, Education and Training

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.3.4-TG |
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

# Technical Specification
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

<!-- QA_VERIFIED: 2026-02-06 -->
