**ISMS-IMP-A.5.4.2-TG - Compliance Oversight Tracker**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.4: Management Responsibilities

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.2-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

# Technical Specification

### 12. Workbook Technical Details

#### 12.1 File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.4.2_Compliance_Oversight_Tracker_YYYYMMDD.xlsx` |
| Generator | `generate_a54_2_compliance_oversight.py` |
| Sheets | 6 |
| Protected | No |

#### 12.2 Sheet Specifications

**Sheet 1: Instructions**
- Purpose: Guidance, workflow, escalation thresholds
- Rows: ~25
- No data entry required

**Sheet 2: Training Oversight**

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Manager_ID | 12 | Text | None |
| B | Manager_Name | 25 | Text | None |
| C | Department | 20 | Text | None |
| D | Team_Size | 10 | Number | None |
| E | Training_Required | 15 | Number | None |
| F | Training_Completed | 18 | Number | None |
| G | Completion_Rate | 15 | Formula | `=IF(E{row}>0,F{row}/E{row}*100,0)` |
| H | Overdue_Count | 12 | Number | None |
| I | Follow_Up_Actions | 35 | Text | None |
| J | Last_Review_Date | 15 | Date | None |

**Sheet 3: Policy Violations**

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Violation_ID | 12 | Text | None |
| B | Date_Reported | 15 | Date | None |
| C | Manager_ID | 12 | Text | None |
| D | Manager_Name | 25 | Text | None |
| E | Employee_ID | 12 | Text | None |
| F | Violation_Type | 25 | Text | None |
| G | Severity | 10 | List | Critical, High, Medium, Low |
| H | Manager_Response | 18 | List | Coaching, Written Warning, Performance Plan, Escalated, No Action |
| I | Response_Date | 15 | Date | None |
| J | Resolution | 12 | List | Resolved, In Progress, Escalated, Pending |
| K | Lessons_Learned | 35 | Text | None |

**Sheet 4: Access Reviews**

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Review_ID | 12 | Text | None |
| B | Review_Period | 15 | Text | None |
| C | Manager_ID | 12 | Text | None |
| D | Manager_Name | 25 | Text | None |
| E | System_Scope | 25 | Text | None |
| F | Accounts_Reviewed | 18 | Number | None |
| G | Changes_Requested | 18 | Number | None |
| H | Review_Completed | 15 | List | Yes, No, Partial |
| I | Completion_Date | 15 | Date | None |
| J | Notes | 35 | Text | None |

**Sheet 5: Escalation Triggers**

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Escalation_ID | 15 | Text | None |
| B | Date | 12 | Date | None |
| C | Manager_ID | 12 | Text | None |
| D | Metric_Triggered | 25 | List | Training Completion Rate, Policy Violations, Manager Response Time |
| E | Actual_Value | 12 | Text | None |
| F | Escalated_To | 20 | Text | None |
| G | Resolution | 15 | List | Resolved, In Progress, Pending, Closed - No Action |
| H | Resolution_Date | 15 | Date | None |

**Sheet 6: Quarterly Summary**

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Manager_ID | 12 | Text | None |
| B | Manager_Name | 25 | Text | None |
| C | Quarter | 10 | List | Q1, Q2, Q3, Q4 |
| D | Training_Compliance_Rate | 22 | Percentage | None |
| E | Violations_Handled | 18 | Number | None |
| F | Avg_Response_Days | 18 | Number | None |
| G | Access_Reviews_Completed | 25 | Percentage | None |
| H | Overall_Rating | 15 | List | Exceeds, Meets, Below, N/A |
| I | Comments | 40 | Text | None |

#### 12.3 Escalation Trigger Thresholds

| Metric | Threshold | Operator | Action |
|--------|:---------:|:--------:|--------|
| Training Completion Rate | 90% | < | Escalate to CISO |
| Policy Violations | 5 | > | Manager performance review |
| Manager Response Time | 15 days | > | Escalate to Department Head |

#### 12.4 Calculation Formulas

**Training Completion Rate** (Training Oversight sheet, Column G):
```
=IF(E{row}>0, F{row}/E{row}*100, 0)
```
Where E = Training_Required, F = Training_Completed

**Escalation Flag** (Training Oversight sheet, Column K - hidden):
```
=IF(G{row}<90, "ESCALATE", "OK")
```

**Response Time Calculation** (Policy Violations sheet):
```
=IF(AND(I{row}<>"", B{row}<>""), I{row}-B{row}, "")
```
Where I = Response_Date, B = Date_Reported

**Quarterly Training Compliance** (Quarterly Summary sheet):
```
=AVERAGEIF('Training Oversight'!C:C, B{row}, 'Training Oversight'!G:G)
```
Averages completion rates for all managers in specified department

**Access Review Completion Percentage** (Quarterly Summary sheet):
```
=COUNTIF('Access Reviews'!H:H, "Yes") / COUNTA('Access Reviews'!H:H) * 100
```

#### 12.5 Conditional Formatting Rules

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Training Oversight | G:G | <90 | Red fill (#FFC7CE), Bold |
| Training Oversight | G:G | ≥90 AND <95 | Yellow fill (#FFEB9C) |
| Training Oversight | G:G | ≥95 | Green fill (#C6EFCE) |
| Policy Violations | G:G | ="Critical" | Red fill (#FFC7CE), Bold |
| Policy Violations | G:G | ="High" | Orange fill (#FABF8F) |
| Escalation Triggers | G:G | ="Pending" | Yellow fill (#FFEB9C) |
| Escalation Triggers | G:G | ="Resolved" | Green fill (#C6EFCE) |
| Quarterly Summary | H:H | ="Below" | Red fill (#FFC7CE), Bold |
| Quarterly Summary | H:H | ="Exceeds" | Green fill (#C6EFCE) |

#### 12.6 Data Validation Lists

**Violation Severity** (Policy Violations, Column G):
- Critical
- High
- Medium
- Low

**Manager Response** (Policy Violations, Column H):
- Coaching
- Written Warning
- Performance Plan
- Escalated
- No Action

**Resolution Status** (Policy Violations, Column J):
- Resolved
- In Progress
- Escalated
- Pending

**Review Completion** (Access Reviews, Column H):
- Yes
- No
- Partial

**Overall Rating** (Quarterly Summary, Column H):
- Exceeds
- Meets
- Below
- N/A

#### 12.7 Styling

| Element | Style |
|---------|-------|
| Title | Bold 14pt, centered, merged across columns |
| Headers | White text (#FFFFFF), Blue fill (#2F5496), Bold, Centered |
| Input cells | Yellow fill (#FFFFCC) |
| Formula cells | Light grey fill (#F2F2F2) |
| All cells | Thin black border |
| Threshold exceeded | Red fill (#FFC7CE) |
| Target met | Green fill (#C6EFCE) |

#### 12.8 Print Settings

| Setting | Value |
|---------|-------|
| Orientation | Landscape |
| Fit to | 1 page wide × automatic pages tall |
| Header | `ISMS-IMP-A.5.4.2 Compliance Oversight - [Date]` |
| Footer | `Page &[Page] of &[Pages] | Confidential` |
| Print Area | Exclude hidden columns |
| Repeat Rows | Row 1 (headers) |

### 13. Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| LMS | Training completion exports | LMS → Training Oversight sheet (monthly) |
| Incident Management | Violation records | Incident register → Policy Violations sheet (as occurred) |
| IAM System | Access review records | IAM system → Access Reviews sheet (per cycle) |
| HR System | Manager hierarchy, performance tracking | HR → Manager list validation (monthly) |
| Email/Calendar | Escalation notifications | Escalation Triggers → Email alert (immediate) |
| A.5.4.1 Workbook | Commitment assessment correlation | Cross-reference for root cause analysis |
| A.5.4.3 Dashboard | Aggregated metrics | This workbook → Dashboard KPIs (quarterly) |
| A.5.4.4 Survey | Culture survey correlation | Compare violations with culture scores |

#### 13.1 Data Flow Diagram

```
┌─────────────────┐
│  LMS Reports    │
│  (Monthly)      │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────┐
│           ISMS-IMP-A.5.4.2 Compliance Oversight         │
│  ┌──────────────────┐  ┌──────────────────────────┐    │
│  │ Training Oversight│  │ Policy Violations        │    │
│  │ (Monthly update) │  │ (Event-driven)           │    │
│  └────────┬─────────┘  └────────────┬─────────────┘    │
│           │                         │                   │
│  ┌────────┴─────────┐  ┌────────────┴─────────────┐    │
│  │ Access Reviews   │  │ Escalation Triggers      │    │
│  │ (Per cycle)      │  │ (Continuous)             │    │
│  └────────┬─────────┘  └────────────┬─────────────┘    │
│           │                         │                   │
│           └────────────┬────────────┘                   │
│                        ▼                                │
│           ┌──────────────────────┐                     │
│           │ Quarterly Summary    │                     │
│           └──────────┬───────────┘                     │
└──────────────────────┼──────────────────────────────────┘
                       │
                       ▼
         ┌─────────────────────────┐
         │ A.5.4.3 Leadership      │
         │ Dashboard               │
         └─────────────────────────┘
```

#### 13.2 LMS Integration Specification

**Required Export Fields**:
| LMS Field | Maps To | Format |
|-----------|---------|--------|
| Manager_Employee_ID | Manager_ID | Text (MGR-XXXX) |
| Manager_Name | Manager_Name | Text |
| Department | Department | Text |
| Direct_Reports_Count | Team_Size | Integer |
| Required_Courses_Total | Training_Required | Integer |
| Completed_Courses_Total | Training_Completed | Integer |
| Overdue_Count | Overdue_Count | Integer |
| Last_Access_Date | Last_Review_Date | Date (DD-MMM-YYYY) |

**Export Frequency**: Monthly (first week of month)
**Export Format**: CSV or XLSX
**Automation**: If LMS supports scheduled exports, configure automatic delivery to Security team

#### 13.3 Incident Management Integration

**When a security violation is logged**:
1. Incident management system captures: Date, Description, Employee involved, Severity
2. Security analyst adds: Manager attribution (lookup from HR system)
3. Entry created in Policy Violations sheet
4. Manager notified within 24 hours
5. Response tracked until resolution

**Field Mapping**:
| Incident Field | Violations Field | Notes |
|----------------|------------------|-------|
| Incident_ID | Violation_ID | Prefix changed (INC → VIO) |
| Date_Reported | Date_Reported | Direct copy |
| Employee_ID | Employee_ID | Direct copy |
| Employee_Manager | Manager_ID, Manager_Name | HR lookup |
| Category | Violation_Type | Map to standardised types |
| Priority | Severity | Map: P1→Critical, P2→High, P3→Medium, P4→Low |

### 14. Automation Opportunities

| Process | Current State | Automation Potential |
|---------|---------------|---------------------|
| LMS data entry | Manual export/import | API integration for real-time sync |
| Escalation notifications | Manual email | Automated alerts when thresholds breached |
| Quarterly Summary | Manual calculation | Dashboard with auto-refresh |
| Trend analysis | Manual charting | Power BI/Tableau integration |
| Manager reminders | Manual follow-up | Automated reminder emails at Day 7, 14 |

**Recommended Automation Priority**:
1. Escalation notifications (high impact, low effort)
2. LMS sync (medium impact, medium effort)
3. Dashboard integration (high impact, medium effort)

### 15. Audit Preparation

#### 15.1 Stage 2 Audit Evidence Requirements

When auditors review management compliance oversight, prepare:

**Documentation Evidence**:
- This workbook (current quarter + previous 2 quarters minimum)
- Escalation notification emails (sample of 3-5)
- Remediation plans for managers below threshold
- Quarterly summary reports presented to management

**Demonstration Requests** (be prepared to show):
1. How training completion data is sourced from LMS
2. How violations are attributed to managers
3. How escalation process works in practice
4. How quarterly summaries feed into Leadership Dashboard

**Common Audit Questions**:

| Question | Evidence to Provide |
|----------|---------------------|
| "How do you ensure managers complete training oversight?" | Training Oversight sheet with completion rates, follow-up actions |
| "What happens when a manager doesn't respond to violations?" | Escalation Triggers sheet with specific examples |
| "How do you verify access reviews are thorough?" | Access Reviews sheet showing change rates, "Partial" follow-ups |
| "Show me trend data over multiple quarters" | Quarterly Summary sheets for past 4 quarters |

#### 15.2 Pre-Audit Checklist

Two weeks before scheduled audit:

- [ ] All sheets updated through current month
- [ ] No blank required fields in any sheet
- [ ] All escalations have documented resolution or active status
- [ ] Quarterly Summary matches source data (spot check)
- [ ] Evidence files accessible in SharePoint
- [ ] Prior quarter workbooks available for trend comparison
- [ ] Responsible staff available during audit window
- [ ] Sample escalation emails exported and organised

#### 15.3 Common Audit Findings (Avoid These)

| Finding | Root Cause | Prevention |
|---------|------------|------------|
| Incomplete training data | LMS export not configured correctly | Monthly verification of export completeness |
| Missing violation responses | Informal handling not documented | Require documentation of ALL violations |
| Escalations not closed | Process fatigue | Weekly escalation review meeting |
| Inconsistent severity ratings | No calibration | Quarterly severity calibration session |
| No trend analysis | Only current data maintained | Retain 8 quarters of historical data |

### 16. Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.4 | Management Responsibilities | Parent policy |
| ISMS-IMP-A.5.4.1 | Management Commitment Assessment | Commitment scoring |
| ISMS-IMP-A.5.4.3 | Leadership Dashboard | Consolidation |
| ISMS-IMP-A.6.3 | Awareness and Training | Training data source |
| ISMS-IMP-A.5.15-16-18 | IAM Assessment | Access review source |

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Russian proverb (popularised by Ronald Reagan)

<!-- QA_VERIFIED: 2026-02-06 -->
