**ISMS-IMP-A.5.3.4-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.3: Policies for Segregation of Duties

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.3.4-TG |
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

# Technical Specification

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

<!-- QA_VERIFIED: 2026-02-06 -->
