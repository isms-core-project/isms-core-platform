**ISMS-IMP-A.5.29.4-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.29

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.29.4-TG |
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

# Technical Specification

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

<!-- QA_VERIFIED: 2026-02-06 -->
