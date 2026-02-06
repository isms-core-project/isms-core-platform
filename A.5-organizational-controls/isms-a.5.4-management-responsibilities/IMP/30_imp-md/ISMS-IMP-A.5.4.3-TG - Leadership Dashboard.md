**ISMS-IMP-A.5.4.3-TG - Leadership Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.4: Management Responsibilities

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.3-TG |
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
| Filename | `ISMS-IMP-A.5.4.3_Leadership_Dashboard_YYYYMMDD.xlsx` |
| Generator | `generate_a54_3_leadership_dashboard.py` |
| Sheets | 5 |
| Protected | No |

#### 12.2 Sheet Specifications

**Sheet 1: Instructions**
- Purpose: Data sources, workflow guidance
- Rows: ~20
- No data entry required

**Sheet 2: Executive Summary**

| Row | Content | Type |
|:---:|---------|------|
| 1 | Title (merged A1:E1) | Header |
| 2 | Report Date | Text |
| 4 | Key Metric headers | Header row |
| 5-10 | Metric rows | Data + formulas |
| 12 | Overall Status | Input (MEETS/BELOW/EXCEEDS) |

**Metrics Table:**

| Column | Header | Width |
|:------:|--------|:-----:|
| A | Key Metric | 35 |
| B | Current | 15 |
| C | Minimum | 12 |
| D | Target | 12 |

**Sheet 3: By Department**

| Column | Header | Width | Type |
|:------:|--------|:-----:|------|
| A | Department | 15 | Text |
| B | Manager_Count | 15 | Number |
| C | Avg_Commitment_Score | 20 | Percentage |
| D | Training_Compliance | 18 | Percentage |
| E | Violations_Handled | 18 | Number |
| F | Access_Reviews | 15 | Percentage |
| G | Status | 10 | List (Exceeds, Meets, Below, N/A) |
| H | Notes | 30 | Text |

**Pre-populated Departments:**
Executive, Finance, IT, Operations, HR, Legal, Sales, Marketing, Engineering, Support

**Sheet 4: Trend Analysis**

| Column | Header | Width | Type |
|:------:|--------|:-----:|------|
| A | Metric | 35 | Text |
| B | Q1 | 12 | Number |
| C | Q2 | 12 | Number |
| D | Q3 | 12 | Number |
| E | Q4 | 12 | Number |
| F | YoY_Change | 12 | Formula |
| G | Trend | 15 | List (Improving, Stable, Declining) |

**Pre-populated Metrics:**
1. Overall Commitment Score (%)
2. Managers at Target (%)
3. Training Oversight (%)
4. Access Review Completion (%)
5. Violation Response Time (days)
6. Security Culture Survey Score

**Sheet 5: Action Items**

| Column | Header | Width | Type |
|:------:|--------|:-----:|------|
| A | Action_ID | 12 | Text |
| B | Finding | 35 | Text |
| C | Action_Required | 40 | Text |
| D | Owner | 20 | Text |
| E | Due_Date | 12 | Date |
| F | Status | 12 | List |
| G | Completion_Date | 15 | Date |
| H | Evidence | 30 | Text |

**Status Values:** Open, In Progress, Completed, Overdue, Cancelled

#### 12.3 Styling

| Element | Style |
|---------|-------|
| Title | Bold 14pt, centered |
| Headers | White text (#FFFFFF), Blue fill (#2F5496), Bold |
| Metric cells | Light green fill (#E2EFDA) |
| Input cells | Yellow fill (#FFFFCC) |
| All data cells | Thin black border |

### 13. Data Sources

| Dashboard Element | Source Workbook | Source Sheet |
|-------------------|-----------------|--------------|
| Overall Commitment Score | A.5.4.1 | Summary Scores (average) |
| Managers Assessed | A.5.4.1 | Manager Inventory (count) |
| Managers Meeting Target | A.5.4.1 | Summary Scores (≥70% count) |
| Training Oversight | A.5.4.2 | Training Oversight (average) |
| Access Reviews | A.5.4.2 | Access Reviews (Yes %) |
| Violation Response | A.5.4.2 | Policy Violations (avg days) |
| Culture Survey | A.5.4.4 | Executive Summary |

### 14. Calculation Formulas

**YoY Change** (Trend Analysis sheet, Column F):
```
=IF(AND(B{row}>0, E{row}>0), E{row}-B{row}, "-")
```
Where B = Q1 value, E = Q4 value

**Department Status** (By Department sheet, Column G):
```
=IF(C{row}>=85%, "Exceeds", IF(C{row}>=70%, "Meets", IF(C{row}>0, "Below", "N/A")))
```

**Overall Status Logic**:
- EXCEEDS: All 6 metrics at or above Target
- MEETS: All 6 metrics at or above Minimum
- BELOW: Any metric below Minimum

**Action Item Status Aging**:
```
=IF(E{row}<TODAY(), IF(F{row}<>"Completed", "Overdue", F{row}), F{row})
```
Automatically flags items past due date as "Overdue"

### 15. Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| A.5.4.1 Workbook | Commitment scores | Manual consolidation quarterly |
| A.5.4.2 Workbook | Training, violations, access reviews | Manual consolidation quarterly |
| A.5.4.4 Workbook | Culture survey scores | Manual consolidation annually |
| SharePoint | Evidence storage | File links in Action Items sheet |
| Calendar | Management review meetings | Dashboard timed to meeting schedule |

#### 15.1 Data Flow Diagram

```
┌──────────────────────────────────────────────────────────────────────┐
│                    A.5.4 DATA CONSOLIDATION FLOW                      │
└──────────────────────────────────────────────────────────────────────┘

┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
│ ISMS-IMP-A.5.4.1    │  │ ISMS-IMP-A.5.4.2    │  │ ISMS-IMP-A.5.4.4    │
│ Management          │  │ Compliance          │  │ Security Culture    │
│ Commitment          │  │ Oversight           │  │ Survey              │
│                     │  │                     │  │                     │
│ ─ Summary Scores    │  │ ─ Training %        │  │ ─ Overall Score     │
│ ─ Manager Count     │  │ ─ Violations        │  │ ─ Category Scores   │
│ ─ Department Data   │  │ ─ Response Time     │  │ ─ Response Rate     │
│                     │  │ ─ Access Reviews    │  │                     │
└────────┬────────────┘  └────────┬────────────┘  └────────┬────────────┘
         │                        │                        │
         │    [Semi-annual]       │    [Quarterly]         │  [Annual]
         │                        │                        │
         └────────────────────────┼────────────────────────┘
                                  │
                                  ▼
         ┌────────────────────────────────────────────────────┐
         │              ISMS-IMP-A.5.4.3                       │
         │           LEADERSHIP DASHBOARD                      │
         │                                                     │
         │  ┌──────────────────┐  ┌──────────────────┐        │
         │  │ Executive        │  │ By Department    │        │
         │  │ Summary          │  │                  │        │
         │  │ ─ 6 KPIs        │  │ ─ 10 Depts       │        │
         │  │ ─ Status        │  │ ─ 6 Metrics      │        │
         │  └──────────────────┘  └──────────────────┘        │
         │                                                     │
         │  ┌──────────────────┐  ┌──────────────────┐        │
         │  │ Trend Analysis   │  │ Action Items     │        │
         │  │ ─ 4 Quarters    │  │ ─ Finding        │        │
         │  │ ─ YoY Change    │  │ ─ Owner          │        │
         │  │ ─ Trend         │  │ ─ Status         │        │
         │  └──────────────────┘  └──────────────────┘        │
         └───────────────────────────┬────────────────────────┘
                                     │
                                     ▼
         ┌────────────────────────────────────────────────────┐
         │              EXECUTIVE MANAGEMENT                   │
         │                                                     │
         │  ─ Quarterly Management Review (ISO 27001 Cl 9.3)  │
         │  ─ Resource allocation decisions                    │
         │  ─ Action item approval                             │
         │  ─ Trend assessment and strategic direction         │
         └────────────────────────────────────────────────────┘
```

#### 15.2 Consolidation Procedures

**Executive Summary Consolidation**:

| Metric | Source | Calculation |
|--------|--------|-------------|
| Overall Commitment Score | A.5.4.1 Summary Scores | Average of all manager scores |
| Managers Assessed | A.5.4.1 Manager Inventory | Count of rows with data |
| Managers Meeting Target | A.5.4.1 Summary Scores | Count where Overall ≥70% |
| Training Oversight Compliance | A.5.4.2 Training Oversight | Average of Completion_Rate column |
| Access Reviews Completed | A.5.4.2 Access Reviews | Count "Yes" ÷ Total × 100% |
| Avg Policy Violation Response | A.5.4.2 Policy Violations | Average of (Response_Date - Date_Reported) |

**Department Consolidation**:

For each department in A.5.4.1 and A.5.4.2:
1. Filter source data by Department column
2. Calculate department averages for each metric
3. Aggregate into By Department sheet
4. Apply status logic (Exceeds/Meets/Below)
5. Add notes for any departments requiring attention

**Trend Analysis Consolidation**:

1. Retrieve current quarter data from source workbooks
2. Enter in appropriate Q column (Q1-Q4)
3. Formula calculates YoY Change automatically
4. Manually set Trend based on:
   - Improving: YoY Change positive by >5% or >0.3 points
   - Stable: YoY Change within ±5% or ±0.3 points
   - Declining: YoY Change negative by >5% or >0.3 points

#### 15.3 Timing and Dependencies

```
QUARTERLY DASHBOARD UPDATE TIMELINE
────────────────────────────────────────────────────────────────────────

Quarter End (Day 0)
       │
       ▼
┌──────────────────────────────────────────────────────────────────────┐
│ Day 1-3: Source Data Freeze                                          │
│ ─ A.5.4.1 finalised (if assessment quarter)                         │
│ ─ A.5.4.2 monthly data closed out                                   │
│ ─ A.5.4.4 results available (Q4 only)                               │
└──────────────────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────────────────┐
│ Day 4-5: Dashboard Data Consolidation                                │
│ ─ Security Analyst compiles from source workbooks                   │
│ ─ Executive Summary metrics calculated                              │
│ ─ By Department breakdown completed                                  │
│ ─ Trend Analysis updated                                            │
│ ─ Action Items reviewed (status, new items)                         │
└──────────────────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────────────────┐
│ Day 6-7: Validation and Quality Check                                │
│ ─ Security Manager reviews for accuracy                             │
│ ─ Cross-check against source workbooks                              │
│ ─ Flag any anomalies or data quality issues                         │
└──────────────────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────────────────┐
│ Day 8-10: CISO Review and Approval                                   │
│ ─ CISO reviews dashboard content                                    │
│ ─ Executive narrative drafted                                        │
│ ─ Presentation materials prepared                                    │
│ ─ Dashboard approved for management review                          │
└──────────────────────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────────────────────────────┐
│ Management Review Meeting (per ISMS Calendar)                        │
│ ─ Dashboard presented to Executive Management                        │
│ ─ Trends discussed and decisions made                                │
│ ─ Action items assigned for follow-up                               │
│ ─ Meeting minutes documented                                         │
└──────────────────────────────────────────────────────────────────────┘
```

#### 15.4 Management Review Integration

This dashboard provides input to ISO 27001 Clause 9.3 Management Review:

| Management Review Input | Dashboard Source |
|------------------------|------------------|
| Status of actions from previous reviews | Action Items sheet (prior quarter items) |
| Changes in external and internal issues | Trend Analysis (declining metrics indicate changes) |
| Information on security performance | Executive Summary (all 6 KPIs) |
| Results of risk assessments | By Department (highlights risk areas) |
| Opportunities for improvement | Action Items (proposed new actions) |

**Meeting Agenda Integration**:

```
MANAGEMENT REVIEW AGENDA - ISMS PERFORMANCE
─────────────────────────────────────────────
1. Review of prior action items                    → Action Items sheet
2. Security leadership metrics overview            → Executive Summary
3. Department performance analysis                 → By Department
4. Trend assessment and direction                 → Trend Analysis
5. New action items and decisions                  → Discussion outcomes
6. Resource allocation (if needed)                → Based on findings
```

### 16. Glossary of Terms

| Term | Definition |
|------|------------|
| **Overall Commitment Score** | Weighted average of manager security leadership scores from A.5.4.1 |
| **Managers Meeting Target** | Count of managers with Overall Commitment Score ≥70% |
| **Training Oversight Compliance** | Percentage of required training completed across manager teams |
| **Access Review Completion** | Percentage of scheduled access reviews fully completed |
| **Avg Policy Violation Response** | Mean number of business days from violation report to manager response |
| **Security Culture Survey Score** | Organisation-wide average from annual culture survey (scale 1.0-5.0) |
| **YoY Change** | Year-over-year change (Current Q4 minus Prior Q4) |
| **Trend** | Direction indicator: Improving (↑), Stable (→), Declining (↓) |

### 17. Automation Opportunities

| Process | Current State | Automation Potential | Priority |
|---------|---------------|---------------------|----------|
| Data consolidation | Manual copy/paste from source workbooks | Power Query links to source workbooks | High |
| Executive Summary calculation | Manual entry | Formulas linked to source workbooks | High |
| Department breakdown | Manual filtering and averaging | PivotTable with source workbook links | Medium |
| Trend graphing | Manual chart creation | Auto-updating charts with data ranges | Medium |
| Action item reminders | Manual tracking | Automated email alerts for due dates | Medium |
| Status indicators | Manual colour coding | Conditional formatting (already implemented) | Done |
| Meeting scheduling | Manual calendar invite | Recurring calendar with dashboard link | Low |

**Recommended Implementation Sequence**:
1. **Phase 1** (High priority): Power Query data connections to source workbooks
2. **Phase 2** (Medium priority): Auto-updating charts for trend visualisation
3. **Phase 3** (Optional): Email automation for action item reminders

**Constraints**:
- Automation must maintain audit trail (who changed what, when)
- Source workbook structure changes require link updates
- Executives may prefer static snapshots for meeting discussions

### 18. Version Control

**Dashboard Version Naming**:
```
ISMS-IMP-A.5.4.3_Leadership_Dashboard_[YYYYMMDD].xlsx
```

Example: `ISMS-IMP-A.5.4.3_Leadership_Dashboard_20260131.xlsx`

**Retention Requirements**:
- Current quarter: Active working file
- Prior 3 quarters: Archive (read-only)
- Prior years: 5-year retention per ISMS evidence policy

**Change Log** (maintain in Instructions sheet):

| Date | Changed By | Description |
|------|------------|-------------|
| 2026-01-31 | [Name] | Q4 2025 data consolidated |
| 2025-10-15 | [Name] | Q3 2025 data consolidated |
| ... | ... | ... |

### 19. Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.4 | Management Responsibilities | Parent policy |
| ISMS-IMP-A.5.4.1 | Management Commitment Assessment | Data source |
| ISMS-IMP-A.5.4.2 | Compliance Oversight Tracker | Data source |
| ISMS-IMP-A.5.4.4 | Security Culture Survey | Data source |
| ISMS-POL-A.5.35-36 | Compliance and Review | Management review input |

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
