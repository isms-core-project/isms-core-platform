**ISMS-IMP-A.8.4.3-TG - Source Code Security Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.4: Access to Source Code

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.4.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Source Code Security Compliance Dashboard (Aggregated) |
| **Related Policy** | ISMS-POL-A.8.4, Section 4 (Assessment and Evidence Framework) |
| **Purpose** | Aggregate data from IMP-S1 (Access Control) and IMP-S2 (Branch Protection) into comprehensive executive dashboard showing overall source code security posture |
| **Target Audience** | CISO, CTO/VP Engineering, Information Security Manager, Auditors, Executive Leadership |
| **Assessment Type** | Aggregated Dashboard & Executive Reporting |
| **Review Cycle** | Quarterly (with monthly KPI updates) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Source Code Security Compliance Dashboard | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.4.3-UG.

---

# Technical Specification

**Audience:** Python/Excel Script Maintainers, Assessment Workbook Developers

---

## Instructions for Workbook Development

### Workbook Generation

**Primary Script:** `generate_a84_3_compliance_dashboard.py`

**Purpose:** Generate Excel workbook (`ISMS-IMP-A.8.4.3_Compliance_Dashboard_YYYYMMDD.xlsx`) that aggregates data from S1 (Repository Access) and S2 (Branch Protection) into executive dashboard.

**Key Functions:**

- `create_workbook()`: Initialize workbook and sheets
- `setup_styles()`: Cell styles, executive dashboard styling
- `create_executive_summary()`: 1-page dashboard with charts
- `import_s1_data()`: Link to S1 workbook compliance scores
- `import_s2_data()`: Link to S2 workbook compliance scores
- `calculate_overall_score()`: Aggregate S1 + S2 into overall compliance
- `create_trend_analysis()`: Historical score tracking
- `create_gap_matrix()`: Consolidated gap prioritization
- `create_action_items()`: Remediation task tracking

**File Naming:** `ISMS-IMP-A.8.4.3_Compliance_Dashboard_YYYYMMDD.xlsx`

**Critical Design Pattern:**
This workbook LINKS to S1 and S2 workbooks using Excel external references. Formulas reference:

- `[ISMS-IMP-A.8.4.1_Repository_Access_YYYYMMDD.xlsx]Compliance_Scoring`
- `[ISMS-IMP-A.8.4.2_Branch_Protection_YYYYMMDD.xlsx]Compliance_Scoring`

---

## Workbook Structure Overview

### Sheet List (11 Sheets Total)

| Sheet # | Sheet Name | Purpose | Rows | Columns | Entry Type |
|---------|------------|---------|------|---------|------------|
| 1 | Executive_Summary | 1-page dashboard | ~40 | A-F | Formula + Chart |
| 2 | Repository_Overview | Consolidated repo status | Variable | A-G | Linked data |
| 3 | Access_Control_Metrics | S1 detailed metrics | ~30 | A-D | Linked from S1 |
| 4 | Branch_Protection_Metrics | S2 detailed metrics | ~30 | A-D | Linked from S2 |
| 5 | Secret_Management_Metrics | Secret scanning & rotation | ~30 | A-D | Linked data |
| 6 | Third_Party_Access | External access summary | Variable | A-F | Aggregated |
| 7 | Trend_Analysis | 12-month history | 12 rows | A-F | Historical data |
| 8 | Gap_Priority_Matrix | Consolidated gaps | Variable | A-H | Aggregated |
| 9 | Action_Items | Remediation tracking | Variable | A-H | User input |
| 10 | Evidence_Summary | Audit readiness | ~30 | A-C | Checklist |
| 11 | Approval_Sign_Off | CISO certification | ~40 | A-B | User input |

---

## Sheet 1: Executive_Summary

### Purpose
1-page executive dashboard for CISO/leadership.

### Layout Structure

**Section 1: Header (Rows 1-5)**
```
Row 1: "SOURCE CODE SECURITY COMPLIANCE DASHBOARD"
Row 2: "Assessment Period: [Date]"
Row 3: [Blank]
Row 4: "OVERALL COMPLIANCE SCORE"
Row 5: [Large Score Display - Cell C5]
```

**Section 2: Risk Indicator (Rows 7-9)**
```
Row 7: "Risk Level:"
Row 8: [Traffic Light Display - Cell C8]
Row 9: "Trend: [Arrow] [+/- %]"
```

**Section 3: KPI Summary Table (Rows 11-16)**
```
| Metric                 | Current | Target | Status |
|------------------------|---------|--------|--------|
| Repository Access      | [Link]  | ≥85%   | [Icon] |
| Branch Protection      | [Link]  | ≥85%   | [Icon] |
```

**Section 4: Critical Findings (Rows 18-24)**
```
Row 18: "CRITICAL FINDINGS:"
Row 19-24: Bullet list of top 5 issues
```

**Section 5: Top Action Items (Rows 26-32)**
```
Row 26: "TOP 5 ACTION ITEMS:"
Row 27: [Table header]
Row 28-32: Top 5 actions from Action_Items sheet
```

**Section 6: Audit Readiness (Rows 34-37)**
```
Row 34: "AUDIT READINESS:"
Row 35: [Status indicator]
Row 36: [Readiness score]
Row 37: [Recommendation]
```

### Key Formulas

**Cell C5 (Overall Compliance Score):**
```excel
=(Access_Control_Metrics!B3 * 0.50) + (Branch_Protection_Metrics!B3 * 0.50)
```

**Cell C8 (Risk Level):**
```excel
=IF(C5>=85, "🟢 Low Risk",
    IF(C5>=70, "🟡 Medium Risk", "🔴 High Risk"))
```

**Cell C9 (Trend):**
```excel
=IF(Trend_Analysis!E12>5, "↗ Improving",
    IF(Trend_Analysis!E12<-5, "↘ Declining", "→ Stable"))
& " (" & TEXT(Trend_Analysis!E12, "+0%;-0%") & ")"
```

### Charts

**Chart 1: Overall Score Gauge (near Cell C5)**

- Type: Doughnut chart (gauge style)
- Data: Overall score vs. 100%
- Colors: Green (score), Gray (remaining)

**Chart 2: KPI Trend (Rows 11-16)**

- Type: Sparkline charts in Column E
- Data: Last 4 quarters for each KPI
- Shows trend direction visually

### Conditional Formatting

**Cell C5 (Overall Score):**

- ≥85%: Green fill, large font (18pt bold)
- 70-84%: Yellow fill, large font
- <70%: Red fill, large font

**Cell C8 (Risk Level):**

- 🟢 Low Risk: Green background
- 🟡 Medium Risk: Yellow background
- 🔴 High Risk: Red background

---

## Sheet 2: Repository_Overview

### Purpose
Consolidated view of all repositories with access + protection status.

### Column Definitions

| Col | Field Name | Width | Type | Formula/Link |
|-----|------------|-------|------|--------------|
| A | Repository Name | 30 | Linked | From S1 Repository_Inventory |
| B | Platform | 20 | Linked | From S1 Repository_Inventory |
| C | Classification | 20 | Linked | From S1 Repository_Inventory |
| D | Access Control Status | 18 | Linked | From S1 User_Access_Matrix analysis |
| E | Branch Protection Status | 20 | Linked | From S2 Branch_Protection_Details |
| F | Overall Security Score | 15 | Formula | =(D + E)/2 (if both numeric) |
| G | Status | 18 | Formula | =IF(AND(D="✅",E="✅"),"✅ Compliant","⚠️ Needs Work") |

### Summary Statistics (Below Data)

**Row N+5: Summary Section**
```
Total Repositories: [COUNT of Column A]
By Platform:

  - GitHub: [COUNTIF Platform = "GitHub"]
  - GitLab: [COUNTIF Platform = "GitLab"]
  - Bitbucket: [COUNTIF Platform = "Bitbucket"]

By Classification:

  - Production: [COUNTIF Classification = "🔴 Production"]
  - Internal Tools: [COUNTIF Classification = "🟡 Internal Tools"]

Compliance:

  - Compliant: [COUNTIF Status = "✅ Compliant"]
  - Non-Compliant: [COUNTIF Status != "✅ Compliant"]

```

### Linking Pattern

**To link from S1 (example for Repository Name):**
```excel
='[ISMS-IMP-A.8.4.1_Repository_Access_20251231.xlsx]Repository_Inventory'!$A4
```

**Important:** File path must be adjusted based on actual S1/S2 filenames.

---

## Sheet 3: Access_Control_Metrics

### Purpose
Import detailed access control metrics from S1 Compliance_Scoring sheet.

### Structure

**Row 3: Overall Repository Access Score**
```
Cell A3: "Overall Repository Access Score"
Cell B3: ='[S1_File.xlsx]Compliance_Scoring'!B23
Cell C3: "≥85%"
Cell D3: =IF(B3>=85,"✅ Compliant","❌ Non-Compliant")
```

**Row 5-10: Component Metrics**
```
Row 5: Repository Inventory Completeness
  B5: ='[S1_File.xlsx]Compliance_Scoring'!B5
  C5: "100%"
  D5: [Status formula]

Row 6: Access Control Compliance
  B6: ='[S1_File.xlsx]Compliance_Scoring'!B8
  
Row 7: Appropriate Access Rate
  B7: ='[S1_File.xlsx]Compliance_Scoring'!B11
  
Row 8: Orphaned Account Rate
  B8: ='[S1_File.xlsx]Compliance_Scoring'!B14
  
Row 9: Access Review Completion
  B9: ='[S1_File.xlsx]Compliance_Scoring'!B17
  
Row 10: Deprovisioning SLA Compliance
  B10: ='[S1_File.xlsx]Compliance_Scoring'!B20
```

**Row 13-20: Additional Analysis**
```
Row 13: Repositories with Access Issues
  B13: [Count from S1 data]

Row 15: Total Orphaned Accounts
  B15: [Count from S1 Deprovisioning_Log]

Row 17: Overdue Access Reviews
  B17: [Count from S1 Access_Review_Log]

Row 19: Deprovisioning Violations
  B19: [Count from S1 where timeline = "❌ No"]
```

### Conditional Formatting

**Column B (Current Values):**

- ≥Target: Green background
- <Target: Red background

**Column D (Status):**

- ✅ Compliant: Green background
- ❌ Non-Compliant: Red background

---

## Sheet 4: Branch_Protection_Metrics

### Purpose
Import detailed branch protection metrics from S2 Compliance_Scoring sheet.

### Structure

**Row 3: Overall Branch Protection Score**
```
Cell A3: "Overall Branch Protection Score"
Cell B3: ='[S2_File.xlsx]Compliance_Scoring'!B17
Cell C3: "≥85%"
Cell D3: =IF(B3>=85,"✅ Compliant","❌ Non-Compliant")
```

**Row 5-8: Component Metrics**
```
Row 5: Branch Protection Configuration Rate
  B5: ='[S2_File.xlsx]Compliance_Scoring'!B5

Row 6: Pull Request Enforcement Rate
  B6: ='[S2_File.xlsx]Compliance_Scoring'!B8

Row 7: Status Check Compliance Rate
  B7: ='[S2_File.xlsx]Compliance_Scoring'!B11

Row 8: Signed Commit Adoption Rate
  B8: ='[S2_File.xlsx]Compliance_Scoring'!B14
```

**Row 11-18: Additional Analysis**
```
Row 11: Repositories Without Branch Protection
  B11: [Count from S2 where Protection = "❌ No"]

Row 13: Pull Request Bypasses
  B13: [Count from S2 where PR Required = "❌ No"]

Row 15: Missing Status Checks
  B15: [Count from S2 where Status Checks = "❌ No"]

Row 17: Signed Commit Adoption
  B17: [Average from S2 Signed_Commits_Audit]
```

---

## Sheet 5: Trend_Analysis

### Purpose
Track compliance scores over time (12 months).

### Column Definitions

| Col | Field Name | Width | Type | Description |
|-----|------------|-------|------|-------------|
| A | Quarter | 15 | Text | Q1 2025, Q2 2025, etc. |
| B | Overall Score | 15 | Number | Historical overall compliance |
| C | Repository Access | 18 | Number | Historical S1 score |
| D | Branch Protection | 18 | Number | Historical S2 score |
| E | Change from Previous | 18 | Formula | =(B4-B3)/B3*100 |
| F | Trend Direction | 15 | Formula | =IF(E4>5,"↗",IF(E4<-5,"↘","→")) |

### Data Population

**Manual Entry for Historical Data:**

- Rows 4-15: Previous 12 quarters (oldest to newest)
- Current quarter data: Linked from Access_Control_Metrics and Branch_Protection_Metrics

**Current Quarter (Row 15 - example):**
```
Cell A15: "Q4 2025"
Cell B15: =Executive_Summary!C5
Cell C15: =Access_Control_Metrics!B3
Cell D15: =Branch_Protection_Metrics!B3
Cell E15: =(B15-B14)/B14*100
Cell F15: =IF(E15>5,"↗",IF(E15<-5,"↘","→"))
```

### Chart

**Line Chart (Below data, Rows 17-30)**

- X-axis: Quarter (Column A)
- Y-axis: Scores (Columns B, C, D)
- Series 1: Overall Score (blue line)
- Series 2: Repository Access (green line)
- Series 3: Branch Protection (orange line)
- Horizontal line at 85% (target)

---

## Sheet 6: Gap_Priority_Matrix

### Purpose
Consolidate all gaps from S1 and S2, ranked by priority.

### Column Definitions

| Col | Field Name | Width | Type | Description |
|-----|------------|-------|------|-------------|
| A | Gap ID | 15 | Text | GAP-001, GAP-002 (from S1/S2) |
| B | Gap Description | 40 | Text | From S1 or S2 Gap_Analysis |
| C | Source | 10 | Text | "S1" or "S2" |
| D | Risk Level | 15 | Dropdown | 🔴 Critical, 🟠 High, 🟡 Medium, 🟢 Low |
| E | Repos Affected | 12 | Number | Count of repositories |
| F | Remediation Effort | 18 | Text | Hours/days estimate |
| G | Priority Score | 12 | Formula | =(RISK_NUM*E)/EFFORT_NUM |
| H | Status | 18 | Dropdown | 🔴 Open, 🟡 In Progress, 🟢 Completed |

### Data Import

**From S1 Gap_Analysis:**
```
Import all rows where Status != "🟢 Completed"
Prefix Gap ID with "S1-" (e.g., S1-GAP-001)
Set Source = "S1"
```

**From S2 Gap_Analysis:**
```
Import all rows where Status != "🟢 Completed"
Prefix Gap ID with "S2-" (e.g., S2-GAP-001)
Set Source = "S2"
```

### Formulas

**Column G (Priority Score):**
```excel
=LET(
  risk_weight, SWITCH(D4, "🔴 Critical", 10, "🟠 High", 5, "🟡 Medium", 2, "🟢 Low", 1, 0),
  effort_days, SWITCH(F4, "1-2 hours", 0.25, "1 day", 1, "1 week", 5, "2-4 weeks", 15, ">1 month", 30, 1),
  (risk_weight * E4) / effort_days
)
```

Higher score = Higher priority (high risk × many repos ÷ low effort)

### Sorting

**Primary Sort:** Column D (Risk Level) - Critical → High → Medium → Low  
**Secondary Sort:** Column G (Priority Score) - Descending

### Conditional Formatting

**Column D (Risk Level):**

- 🔴 Critical: Red background
- 🟠 High: Orange background
- 🟡 Medium: Yellow background
- 🟢 Low: Green background

**Column H (Status):**

- 🔴 Open: Red background
- 🟡 In Progress: Yellow background
- 🟢 Completed: Green background

---

## Sheet 7: Action_Items

### Purpose
Track remediation tasks derived from gaps.

### Column Definitions

| Col | Field Name | Width | Type | Description |
|-----|------------|-------|------|-------------|
| A | Action ID | 15 | Text | ACT-001, ACT-002, etc. |
| B | Description | 40 | Text | What needs to be done |
| C | Gap Reference | 15 | Text | Which gap (from Sheet 6) |
| D | Responsible Party | 25 | Text | Who will do it |
| E | Target Date | 15 | Date | When it should be done |
| F | Status | 18 | Dropdown | 🔴 Open, 🟡 In Progress, 🟢 Completed |
| G | Days Overdue | 12 | Formula | =IF(F4<>"🟢 Completed",MAX(0,TODAY()-E4),"") |
| H | Notes | 30 | Text | Additional info |

### Formulas

**Column G (Days Overdue):**
```excel
=IF(F4="🟢 Completed", "",
   IF(E4<TODAY(), TODAY()-E4, ""))
```

Shows blank if completed or not yet due.

### Conditional Formatting

**Column E (Target Date):**
```
=AND(E4<TODAY(), F4<>"🟢 Completed")
Format: Red fill (overdue)
```

**Column G (Days Overdue):**

- >30 days: Red fill (critical delay)
- 15-30 days: Orange fill (attention needed)
- 1-14 days: Yellow fill (monitor)

### Sorting

**Primary Sort:** Column F (Status) - Open → In Progress → Completed  
**Secondary Sort:** Column E (Target Date) - Earliest first

---

## Sheet 8: Evidence_Summary

### Purpose
Audit readiness checklist.

### Structure

**Section 1: Documentation Completeness (Rows 4-10)**
```
Row 4: "DOCUMENTATION COMPLETENESS"
Row 6:  [✅/❌] ISMS-POL-A.8.4 (Policy) - approved
Row 7:  [✅/❌] ISMS-IMP-A.8.4.1 (Access) - completed
Row 8:  [✅/❌] ISMS-IMP-A.8.4.2 (Protection) - completed
Row 9:  [✅/❌] ISMS-IMP-A.8.4.3 (Dashboard) - this document
Row 10: Completeness Score: [COUNTIF(✅) / 4 * 100%]
```

**Section 2: Evidence Availability (Rows 12-18)**
```
Row 12: "EVIDENCE AVAILABILITY"
Row 14: [✅/❌] S1 Evidence Register - complete
Row 15: [✅/❌] S2 Evidence Register - complete
Row 16: [✅/❌] Configuration screenshots - collected
Row 17: [✅/❌] Evidence organized for audit
Row 18: Availability Score: [COUNTIF(✅) / 4 * 100%]
```

**Section 3: Compliance Metrics (Rows 20-26)**
```
Row 20: "COMPLIANCE METRICS"
Row 22: [✅/❌] Overall score ≥85%
Row 23: [✅/❌] Critical gaps remediated
Row 24: [✅/❌] High gaps in remediation
Row 25: [✅/❌] Evidence complete
Row 26: Compliance Score: [COUNTIF(✅) / 4 * 100%]
```

**Section 4: Overall Audit Readiness (Rows 28-32)**
```
Row 28: "OVERALL AUDIT READINESS"
Row 30: Readiness Score: [(Row 10 + Row 18 + Row 26) / 3]
Row 31: Status: [IF ≥85%, "✅ Ready", IF ≥70%, "⚠️ Needs Work", "❌ Not Ready"]
Row 32: Recommendation: [Text based on status]
```

### Formulas

**Cell C30 (Readiness Score):**
```excel
=(C10+C18+C26)/3
```

**Cell C31 (Status):**
```excel
=IF(C30>=85, "✅ Ready for Audit",
    IF(C30>=70, "⚠️ Needs Work", "❌ Not Ready"))
```

**Cell C32 (Recommendation):**
```excel
=IF(C31="✅ Ready for Audit", "Proceed with audit scheduling",
    IF(C31="⚠️ Needs Work", "Complete missing items before audit",
        "Significant remediation required"))
```

---

## Sheet 9: Approval_Sign_Off

### Purpose
CISO certification of dashboard.

### Structure

Same as IMP-S1 and IMP-S2 Approval sheets:

- Assessment Summary (with links to Executive_Summary)
- Dashboard Compiled By
- Information Security Manager Review
- CISO Approval
- Next Review Date (+90 days)

**Reference IMP-S1 PART II for detailed approval sheet specification.**

---

## Cell Styling Reference

### Executive Summary Styling

**Overall Score (Cell C5):**

- Font: Calibri 36pt bold
- Alignment: Center
- Border: Thick black box
- Fill: Conditional (green/yellow/red)

**Section Headers:**

- Font: Calibri 14pt bold
- Fill: #003366 (dark blue)
- Text: White

**KPI Table:**

- Header row: #4472C4 (medium blue), white text
- Data rows: Alternating white and light gray

### Standard Styling

**Headers:** Same as IMP-S1 and IMP-S2  
**Input Cells:** Light yellow (#FFFFCC)  
**Formula Cells:** Light blue (#E7F3FF)  
**Status Colors:** Green/Yellow/Red standard palette

---

## Integration Points

### External Workbook Links

**Critical:** This workbook depends on external links to S1 and S2 workbooks.

**Link Syntax:**
```excel
='[ISMS-IMP-A.8.4.1_Repository_Access_20251231.xlsx]Compliance_Scoring'!B23
='[ISMS-IMP-A.8.4.2_Branch_Protection_20251231.xlsx]Compliance_Scoring'!B17
```

**Link Management:**

- Links must be updated when S1/S2 filenames change
- Excel → Data → Edit Links → Update Source
- Or use VBA/Python to update links automatically

**For Python Script:**
```python
# Update external links programmatically
import openpyxl

wb = openpyxl.load_workbook('Dashboard.xlsx')
# Update external references
# Update sheet formulas with new S1/S2 filenames
```

---

## Quality Assurance

### Validation Script

**Script:** `excel_sanity_check_a84_3.py`

**Checks:**
1. All 9 sheets exist
2. External links to S1 and S2 workbooks exist
3. Overall score formula calculates correctly
4. Trend analysis has historical data
5. Gap matrix aggregates from S1 and S2
6. Charts render correctly
7. Conditional formatting applied

**Usage:**
```bash
python excel_sanity_check_a84_3.py ISMS-IMP-A.8.4.3_Compliance_Dashboard_20260125.xlsx \
  --s1-file ISMS-IMP-A.8.4.1_Repository_Access_20251231.xlsx \
  --s2-file ISMS-IMP-A.8.4.2_Branch_Protection_20251231.xlsx
```

---

## Version Control

**Filename:** `ISMS-IMP-A.8.4.3_Compliance_Dashboard_YYYYMMDD.xlsx`

**Quarterly Versioning:**

- Q1 2025: `_20250331.xlsx`
- Q2 2025: `_20250630.xlsx`
- Q3 2025: `_20250930.xlsx`
- Q4 2025: `_20251231.xlsx`

**Change Log:**

- v1.0: Initial dashboard structure (2026-01-25)

---

**END OF SPECIFICATION**

---

*"The strength of a cryptographic system is measured by its ability to resist the best known attacks."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
