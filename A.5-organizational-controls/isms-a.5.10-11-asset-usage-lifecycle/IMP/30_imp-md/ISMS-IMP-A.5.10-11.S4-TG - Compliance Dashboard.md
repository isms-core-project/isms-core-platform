**ISMS-IMP-A.5.10-11.S4-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.10-11

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.S4-TG |
| **Title** | Asset Usage Lifecycle Compliance Dashboard |
| **Control Reference** | ISO/IEC 27001:2022 A.5.10-11 |
| **Control Name** | Asset Usage Lifecycle |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

## Table of Contents

**PART I: USER COMPLETION GUIDE**
1. [Assessment Overview](#assessment-overview)
2. [Control Requirements](#control-requirements)
3. [Prerequisites](#prerequisites)
4. [Key Terminology](#key-terminology)
5. [Dashboard Architecture](#dashboard-architecture)
6. [Key Performance Indicators](#key-performance-indicators)
7. [Data Aggregation Framework](#data-aggregation-framework)
8. [Workbook Structure](#workbook-structure)
9. [Completion Walkthrough](#completion-walkthrough)
10. [Gap Management Framework](#gap-management-framework)
11. [Remediation Management](#remediation-management)
12. [Trend Analysis Framework](#trend-analysis-framework)
13. [Reporting and Export](#reporting-and-export)
14. [Evidence Collection](#evidence-collection)
15. [Common Pitfalls](#common-pitfalls)
16. [Quality Checklist](#quality-checklist)
17. [Review & Approval](#review-approval)

**PART II: TECHNICAL SPECIFICATION**
1. [Workbook Architecture](#workbook-architecture)
2. [Sheet Specifications](#sheet-specifications)
3. [Data Validations](#data-validations)
4. [Conditional Formatting Rules](#conditional-formatting-rules)
5. [Formula Specifications](#formula-specifications)
6. [Chart Specifications](#chart-specifications)
7. [Generator Reference](#generator-reference)

---

# Technical Specification

### Workbook Architecture

**File Details**

| Attribute | Value |
|-----------|-------|
| Filename | `ISMS-IMP-A.5.10-11.S4_Asset_Usage_Lifecycle_Compliance_Dashboard_YYYYMMDD.xlsx` |
| Format | Microsoft Excel (.xlsx) |
| Total Sheets | 8 |
| Target Rows | Compliance: 19-20 each; Gaps: 50+; Remediation: 100+; Trends: 8 |

**Sheet Overview**

| Sheet Name | Purpose | Row Count |
|------------|---------|-----------|
| Instructions | Guidance and metadata | 35 |
| Executive_Summary | KPIs and key findings | 30 |
| A510_Compliance | A.5.10 compliance scoring | 19 requirements |
| A511_Compliance | A.5.11 compliance scoring | 20 requirements |
| Gap_Register | Consolidated gap tracking | Dynamic (50+) |
| Remediation_Tracker | Action tracking | Dynamic (100+) |
| Trend_Analysis | Historical compliance | 8 quarters |
| Approval_SignOff | Dashboard approvals | 10 |

### Sheet Specifications

#### Instructions Sheet

**Metadata Section (Rows 1-20)**

| Row | Content |
|-----|---------|
| 1 | Document title (merged A1:F1) |
| 3-15 | Metadata table (Field/Value pairs) |
| 17-35 | Instructions and guidance text |

**Metadata Fields**

| Field | Cell | Content |
|-------|------|---------|
| Dashboard Title | B3 | Asset Usage Lifecycle Compliance Dashboard |
| Document ID | B4 | ISMS-IMP-A.5.10-11.S4 |
| Control Reference | B5 | A.5.10-11 |
| Reporting Period Start | B6 | Date (user input) |
| Reporting Period End | B7 | Date (user input) |
| Compiled By | B8 | Text (user input) |
| Compilation Date | B9 | Date (user input) |
| Version | B10 | 1.0 |

#### Executive_Summary Sheet

**KPI Boxes (Rows 3-5)**

| Location | Content | Style |
|----------|---------|-------|
| A3:B5 (merged) | Overall Compliance % | Large font, centered, conditional colour |
| D3:E5 (merged) | A.5.10 Compliance % | Large font, centered, conditional colour |
| G3:H5 (merged) | A.5.11 Compliance % | Large font, centered, conditional colour |

**Key Metrics Table (Rows 8-16)**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Metric | 35 | Pre-populated metrics |
| B | Value | 18 | User input |
| C | Target | 12 | Pre-populated targets |
| D | Status | 14 | Data validation |
| E | Control | 12 | Pre-populated (A.5.10/A.5.11/Both) |

**Pre-populated Metrics**

| Metric | Target | Control |
|--------|--------|---------|
| AUP Policy Completeness | 100% | A.5.10 |
| Asset Categories Covered | 100% | A.5.10 |
| User Acknowledgment Rate | 100% | A.5.10 |
| Usage Rules Documented | 100% | Both |
| Return Process Requirements | 100% | A.5.11 |
| Offboarding Completion Rate | 100% | A.5.11 |
| Access Revocation SLA | 95% | A.5.11 |

**Key Findings Table (Rows 19-28)**

| Column | Header | Width |
|--------|--------|-------|
| A-C | Finding/Recommendation | 60 (merged) |
| D | Priority | 14 |
| E | Owner | 20 |
| F | Due Date | 14 |

#### A510_Compliance Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Compliance_Area | 25 | Pre-populated areas |
| B | Requirement | 45 | Pre-populated requirements |
| C | Status | 16 | Data validation |
| D | Score | 12 | User input (0, 0.5, 1) |
| E | Max_Score | 12 | Pre-populated (1) |
| F | Evidence_Ref | 18 | User input |
| G | Last_Assessed | 14 | Date field |
| H | Assessor | 20 | User input |
| I | Gap_Notes | 35 | User input |
| J | Remediation_Ref | 16 | Link to Remediation_Tracker |

**Pre-populated Requirements (19)**

| Area | Requirement |
|------|-------------|
| Policy Framework | AUP document exists and is approved |
| Policy Framework | AUP is published and accessible to all users |
| Policy Framework | AUP covers all required topics |
| Asset Coverage | Physical assets (devices) covered |
| Asset Coverage | Digital assets (accounts, data) covered |
| Asset Coverage | Information assets (documents, IP) covered |
| User Awareness | New user acknowledgment process exists |
| User Awareness | Annual re-acknowledgment required |
| User Awareness | Security awareness training includes AUP |
| Enforcement | Violation reporting mechanism exists |
| Enforcement | Disciplinary process for violations defined |
| Enforcement | Violations are consistently addressed |
| Monitoring | Compliance monitoring process exists |
| Monitoring | Monitoring results are reported |
| Third Parties | Contractors covered by AUP requirements |
| Third Parties | Third-party agreements include AUP reference |
| Review | AUP reviewed at least annually |
| Review | Changes approved through governance process |
| Review | Review triggered by significant changes |

**Summary Row (Row 22)**

- Total Score: `=SUM(D2:D20)`
- Max Score: `=SUM(E2:E20)`
- Percentage: `=D22/E22*100`

#### A511_Compliance Sheet

Same structure as A510_Compliance with 20 requirements:

**Pre-populated Requirements (20)**

| Area | Requirement |
|------|-------------|
| Process Documentation | Offboarding procedure documented |
| Process Documentation | Procedure is published and accessible |
| Asset Return | Asset inventory linked to employees |
| Asset Return | Return checklist exists per asset type |
| Asset Return | Return verification process exists |
| Access Revocation | Network access revocation procedure |
| Access Revocation | Application access revocation procedure |
| Access Revocation | Physical access revocation procedure |
| Access Revocation | Revocation SLA defined (24 hours) |
| Data Security | Data wipe procedure documented |
| Data Security | Wipe verification/certification process |
| Knowledge Transfer | Knowledge transfer requirements defined |
| Knowledge Transfer | Critical role handover documented |
| Verification | Offboarding completion sign-off exists |
| Verification | HR confirmation process exists |
| Remote Workers | Remote asset return process exists |
| Remote Workers | Shipping/logistics procedure documented |
| Contractors | Contractor offboarding process exists |
| Contractors | Contract end triggers access review |
| Escalation | Escalation process for incomplete returns |

#### Gap_Register Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Gap_ID | 12 | Auto-generated (GAP-001) |
| B | Control | 12 | Data validation |
| C | Source_Assessment | 20 | Data validation |
| D | Gap_Description | 45 | User input |
| E | Gap_Type | 18 | Data validation |
| F | Severity | 14 | Data validation |
| G | Risk_Rating | 14 | User input |
| H | Identified_Date | 14 | Date field |
| I | Owner | 22 | User input |
| J | Target_Date | 14 | Date field |
| K | Status | 16 | Data validation |
| L | Remediation_Ref | 16 | Link to Remediation_Tracker |
| M | Closure_Date | 14 | Date field |
| N | Notes | 30 | User input |

**Summary Metrics (Bottom section)**

| Metric | Formula |
|--------|---------|
| Total Gaps | `=COUNTA(A2:A200)` |
| Open Gaps | `=COUNTIF(K:K,"Open")` |
| In Progress | `=COUNTIF(K:K,"In Progress")` |
| Closed | `=COUNTIF(K:K,"Closed")` |
| Critical/High | `=COUNTIFS(F:F,"Critical")+COUNTIFS(F:F,"High")` |

#### Remediation_Tracker Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Remediation_ID | 14 | Auto-generated (REM-001) |
| B | Gap_Ref | 14 | Link to Gap_Register |
| C | Action_Description | 45 | User input |
| D | Control | 12 | Data validation |
| E | Priority | 12 | Data validation |
| F | Owner | 22 | User input |
| G | Assigned_Date | 14 | Date field |
| H | Start_Date | 14 | Date field |
| I | Target_Date | 14 | Date field |
| J | Status | 16 | Data validation |
| K | % Complete | 12 | User input (0-100) |
| L | Completion_Date | 14 | Date field |
| M | Verification | 25 | User input |
| N | Notes | 30 | User input |

**Summary Metrics**

| Metric | Formula |
|--------|---------|
| Total Actions | `=COUNTA(A2:A200)` |
| Not Started | `=COUNTIF(J:J,"Not Started")` |
| In Progress | `=COUNTIF(J:J,"In Progress")` |
| Completed | `=COUNTIF(J:J,"Completed")` |
| Overdue | `=COUNTIFS(I:I,"<"&TODAY(),J:J,"<>Completed",J:J,"<>Cancelled")` |

#### Trend_Analysis Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Assessment_Period | 18 | Pre-populated (Q1 2025, etc.) |
| B | A510_Score | 14 | User input (percentage) |
| C | A510_Change | 14 | Formula |
| D | A511_Score | 14 | User input (percentage) |
| E | A511_Change | 14 | Formula |
| F | Overall_Score | 14 | Formula |
| G | Overall_Change | 14 | Formula |
| H | Open_Gaps | 14 | User input |
| I | Critical_High | 14 | User input |
| J | Notes | 40 | User input |

**Pre-populated Periods**

| Row | Period |
|-----|--------|
| 2 | Q1 2025 |
| 3 | Q2 2025 |
| 4 | Q3 2025 |
| 5 | Q4 2025 |
| 6 | Q1 2026 |
| 7 | Q2 2026 |
| 8 | Q3 2026 |
| 9 | Q4 2026 |

**Change Formulas**

```
A510_Change: =IF(B2="","",IF(B1="","N/A",B2-B1))
A511_Change: =IF(D2="","",IF(D1="","N/A",D2-D1))
Overall_Score: =IF(OR(B2="",D2=""),"",(B2+D2)/2)
Overall_Change: =IF(F2="","",IF(F1="","N/A",F2-F1))
```

#### Approval_SignOff Sheet

**Approval Table**

| Row | Role | Name | Signature | Date | Comments |
|-----|------|------|-----------|------|----------|
| 2 | Compiler | | | | |
| 3 | Information Security Manager | | | | |
| 4 | CISO | | | | |

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Compliance Status | Compliant, Partial, Non-Compliant, Not Assessed |
| KPI Status | On Track, At Risk, Behind |
| Finding Priority | Critical, High, Medium, Low |
| Control | A.5.10, A.5.11, Both |
| Source_Assessment | ISMS-IMP-A.5.10-11.S1, ISMS-IMP-A.5.10-11.S2, ISMS-IMP-A.5.10-11.S3, Internal Audit, Incident |
| Gap_Type | Policy Gap, Process Gap, Technical Gap, Documentation Gap, Training Gap |
| Gap Severity | Critical, High, Medium, Low |
| Gap Status | Open, In Progress, Remediated, Accepted, Closed |
| Remediation Priority | Critical, High, Medium, Low |
| Remediation Status | Not Started, In Progress, On Hold, Completed, Cancelled |

### Conditional Formatting Rules

**Executive_Summary KPI Boxes**

| Condition | Format |
|-----------|--------|
| Score ≥ 90% | Green fill |
| Score 75-89% | Yellow fill |
| Score 60-74% | Orange fill |
| Score < 60% | Red fill |

**KPI Status Column**

| Value | Format |
|-------|--------|
| On Track | Green text |
| At Risk | Yellow fill |
| Behind | Red fill |

**Compliance Sheets (Status Column)**

| Value | Format |
|-------|--------|
| Compliant | Green fill |
| Partial | Yellow fill |
| Non-Compliant | Red fill |
| Not Assessed | Grey fill |

**Gap_Register Sheet**

| Condition | Format | Column |
|-----------|--------|--------|
| Severity = "Critical" | Red fill | F |
| Severity = "High" | Orange fill | F |
| Status = "Open" AND Target_Date < TODAY() | Red border | Row |
| Status = "Closed" | Green fill | K |

**Remediation_Tracker Sheet**

| Condition | Format | Column |
|-----------|--------|--------|
| Priority = "Critical" | Red fill | E |
| Target_Date < TODAY() AND Status <> "Completed" | Red fill | I |
| Status = "Completed" | Green fill | J |
| % Complete = 100 | Green fill | K |

**Trend_Analysis Sheet**

| Condition | Format | Column |
|-----------|--------|--------|
| Change > 0 | Green text, ↑ | C, E, G |
| Change < 0 | Red text, ↓ | C, E, G |
| Change = 0 | Grey text, → | C, E, G |

### Formula Specifications

**Executive Summary Overall Compliance**

```
=ROUND((A510_Score + A511_Score) / 2, 1)
```

**A510 Compliance Total**

```
=ROUND(SUM(D2:D20) / SUM(E2:E20) * 100, 1)
```

**Gap Register - Overdue Count**

```
=COUNTIFS(K:K,"Open",J:J,"<"&TODAY())+COUNTIFS(K:K,"In Progress",J:J,"<"&TODAY())
```

**Remediation Tracker - SLA Compliance**

```
=COUNTIFS(J:J,"Completed",L:L,"<="&I:I) / COUNTIF(J:J,"Completed") * 100
```

**Trend Change**

```
=IF(B3="","",B3-B2)
```

**Risk Score**

```
=COUNTIF(F:F,"Critical")*4 + COUNTIF(F:F,"High")*3 + COUNTIF(F:F,"Medium")*2 + COUNTIF(F:F,"Low")*1
```

### Chart Specifications

**Trend Chart (Optional)**

| Attribute | Specification |
|-----------|---------------|
| Type | Line chart |
| X-axis | Assessment_Period |
| Y-axis | Compliance % (0-100) |
| Series 1 | A510_Score (blue line) |
| Series 2 | A511_Score (green line) |
| Series 3 | Overall_Score (black line) |
| Location | Trend_Analysis sheet, cells L2:T15 |

**Gap Severity Pie Chart (Optional)**

| Attribute | Specification |
|-----------|---------------|
| Type | Pie chart |
| Data | Count by severity |
| Colours | Critical=Red, High=Orange, Medium=Yellow, Low=Green |
| Location | Gap_Register sheet, cells P2:V12 |

### Generator Reference

**Script**: `generate_a510_11_4_compliance_dashboard.py`

**Location**: `10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/10_generator-master/`

**Dependencies**:
- openpyxl
- datetime
- logging

**Output**: `../90_workbooks/ISMS-IMP-A.5.10-11.S4_Asset_Usage_Lifecycle_Compliance_Dashboard_YYYYMMDD.xlsx`

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
