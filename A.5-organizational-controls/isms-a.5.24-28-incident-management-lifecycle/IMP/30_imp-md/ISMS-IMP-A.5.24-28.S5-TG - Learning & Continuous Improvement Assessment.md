**ISMS-IMP-A.5.24-28.S5-TG - Learning & Continuous Improvement Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.27

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Learning & Continuous Improvement Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S5-TG |
| **Assessment Domain** | Domain 5 - Learning & Improvement (A.5.27 Focus) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Incident Response Team Lead / CSIRT Manager |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CSIRT Manager | Initial learning & improvement assessment specification |

**Review Cycle:** Annual (or after major incident management process changes)
**Next Review Date:** [Effective Date + 12 months]

**Related Documents:**
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide)
- ISMS-IMP-A.5.24-28.S1 (Framework & Governance Assessment)
- ISMS-IMP-A.5.24-28.S2 (Detection & Classification Assessment)
- ISMS-IMP-A.5.24-28.S3 (Response Capabilities Assessment)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment)
- ISO/IEC 27002:2022 Control A.5.27
- NIST SP 800-61 Rev. 2 Section 3.4 (Post-Incident Activity)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides the technical specification for the Excel assessment workbook generation. Users completing the assessment should refer to Part I above.

---

## Instructions for Completing This Assessment

### How to Use This Document

This technical specification defines the structure, validation rules, and formulas for the Learning & Improvement Assessment Excel workbook (`ISMS-IMP-A.5.24-28.S5_Learning_Improvement_[DATE].xlsx`).

**Workbook Generation:** Python script `generate_a524_28_s5_learning_improvement.py` creates the workbook based on this specification.

**Assessment Completion Process:**

1. **Read each section** and determine if the learning/improvement practice applies to your organisation
2. **Complete the assessment** using the dropdown options and free-text fields as specified
3. **Mark Status:** [X] Compliant / [!] Partial / [N] Non-Compliant / N/A
4. **If [!] or [N]:** Complete the Gap Analysis entry with remediation plan
5. **Provide Evidence:** Document where compliance evidence can be found in the Evidence Register
6. **Review the Summary Dashboard** before submitting for approval

### Status Legend

| Symbol | Meaning | Description |
|--------|---------|-------------|
| **[X]** | **Compliant** | Fully meets policy requirements, no gaps identified |
| **[!]** | **Partial** | Some requirements met, minor gaps exist, remediation planned |
| **[N]** | **Non-Compliant** | Does not meet policy requirements, significant gaps |
| **N/A** | **Not Applicable** | This requirement does not apply (rare in this assessment) |

### Evidence Types

Acceptable evidence includes:
- PIR report documents (PDF or Word)
- RCA report documents
- Lessons learned log exports
- Playbook revision history
- Distribution confirmation records (email screenshots)
- Remediation action tracker exports
- Closure verification sign-off records
- Incident trend reports (monthly/quarterly/annual)
- KPI dashboard screenshots
- Escalation notification records

---

## Workbook Structure

### Sheet Overview (10 Sheets)

| Sheet # | Sheet Name | Purpose |
|---------|------------|---------|
| 1 | Instructions & Legend | Overview, status legend, evidence types, navigation guide |
| 2 | PIR Process | Post-Incident Review inventory, timeliness, quality scoring |
| 3 | Root Cause Analysis | RCA inventory, methodology, depth scoring, recurring causes |
| 4 | Lessons Learned | Lessons log, distribution verification, knowledge base inventory |
| 5 | Control Improvements | Remediation action register, closure verification, blocked actions |
| 6 | Trend Analysis | KPI tracking, reporting cadence verification, trend accuracy |
| 7 | Gap Analysis | Consolidated gap register auto-populated from domain sheets |
| 8 | Evidence Register | Central evidence log with auto-numbering |
| 9 | Summary Dashboard | Compliance overview, KPI summary, critical flags |
| 10 | Approval Sign-Off | Three-level approval workflow |

---

## Sheet 1: Instructions & Legend

### Layout

| Row | Content |
|-----|---------|
| 1-3 | Title block: "ISMS-IMP-A.5.24-28.S5 - Learning & Continuous Improvement Assessment" |
| 5-8 | Document info fields: Organisation, Assessment Date, Assessor Name, Assessment Period |
| 10 | Section header: "Status Legend" |
| 11-15 | Status legend table ([X] / [!] / [N] / N/A with descriptions) |
| 17 | Section header: "Evidence Types" |
| 18-28 | Evidence types list |
| 30 | Section header: "Navigation Guide" |
| 31-40 | Sheet-by-sheet completion instructions and time estimates |
| 42 | Section header: "Quality Checklist" |
| 43-57 | Pre-submission quality checklist items |

---

## Sheet 2: PIR Process

### Section A - PIR Inventory

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Incident_ID | 18 | Text | Free text |
| B | Incident_Date | 14 | Date | DD.MM.YYYY |
| C | Severity | 12 | Dropdown | Critical, High, Medium, Low |
| D | Resolution_Date | 16 | Date | DD.MM.YYYY |
| E | PIR_Status | 14 | Dropdown | Completed, Overdue, Pending, Not_Required |
| F | PIR_Completion_Date | 20 | Date | DD.MM.YYYY |
| G | Policy_SLA_Days | 16 | Number | Auto: 5 (Critical/High), 15 (Medium), 30 (Low) |
| H | Actual_Days_To_PIR | 18 | Number | Formula: business days between D and F |
| I | SLA_Met | 10 | Dropdown | Yes, No, N/A |
| J | Participants_Count | 18 | Number | Integer |
| K | Participant_Req_Met | 20 | Dropdown | Yes, No |
| L | PIR_Quality_Score | 18 | Dropdown | 1, 2, 3, 4, 5 |
| M | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 6-55 (50 rows - supports up to 50 incidents)

**Conditional Formatting:**
- Column E (PIR_Status): Green = Completed; Yellow = Pending; Red = Overdue
- Column I (SLA_Met): Green = Yes; Red = No
- Column L (PIR_Quality_Score): Green = 4-5; Yellow = 3; Red = 1-2

**Section Header Row:** Row 3 - "Section A: PIR Inventory"

### Section B - PIR Quality Scoring Criteria (Reference)

**Rows 58-68:** Static reference table showing the 1-5 quality scoring criteria. Read-only, informational.

### Section C - PIR Process Summary

**Rows 72-82:** Summary metrics with formulas

| Row | Label | Formula |
|-----|-------|---------|
| 72 | Total incidents in scope | `=COUNTA(A6:A55)` |
| 73 | PIRs completed | `=COUNTIF(E6:E55,"Completed")` |
| 74 | PIRs overdue | `=COUNTIF(E6:E55,"Overdue")` |
| 75 | PIRs pending | `=COUNTIF(E6:E55,"Pending")` |
| 76 | PIR completion rate (%) | `=COUNTIF(E6:E55,"Completed")/COUNTA(E6:E55)*100` |
| 77 | SLA compliance rate (%) | `=COUNTIF(I6:I55,"Yes")/(COUNTIF(I6:I55,"Yes")+COUNTIF(I6:I55,"No"))*100` |
| 78 | Average PIR quality score | `=AVERAGEIF(E6:E55,"Completed",L6:L55)` |
| 79 | Average days to PIR | `=AVERAGEIF(E6:E55,"Completed",H6:H55)` |

---

## Sheet 3: Root Cause Analysis

### Section A - RCA Inventory

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Incident_ID | 18 | Text | Free text (cross-ref to Sheet 2) |
| B | Severity | 12 | Dropdown | Critical, High |
| C | RCA_Status | 16 | Dropdown | Completed, Overdue, Not_Performed, In_Progress |
| D | RCA_Completion_Date | 20 | Date | DD.MM.YYYY |
| E | RCA_Methodology | 20 | Dropdown | 5_Whys, Fishbone, Fault_Tree, Timeline_Analysis, Other, None |
| F | Immediate_Cause | 40 | Text | Free text |
| G | Root_Cause | 45 | Text | Free text |
| H | Root_Cause_Depth | 18 | Dropdown | 3-Systemic, 2-Procedural, 1-Technical |
| I | Recurring_Root_Cause | 20 | Dropdown | Yes, No |
| J | Corrective_Actions_Count | 22 | Number | Integer |
| K | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 6-35 (30 rows - Critical and High incidents only)

**Conditional Formatting:**
- Column C (RCA_Status): Green = Completed; Yellow = In_Progress; Red = Not_Performed / Overdue
- Column H (Root_Cause_Depth): Green = 3-Systemic; Yellow = 2-Procedural; Red = 1-Technical
- Column I (Recurring_Root_Cause): Red = Yes (flags systemic risk)

### Section B - RCA Quality Assessment

**Rows 40-75:** One block per RCA (up to 30 entries), each containing 4 Yes/No questions.

| Row Offset | Question | Validation |
|------------|----------|------------|
| +0 | RCA Reference (auto from Section A) | Auto |
| +1 | Root cause clearly distinguishable from immediate cause? | Yes, No |
| +2 | Root cause explains WHY immediate cause was possible? | Yes, No |
| +3 | Corrective actions linked to root cause (not symptoms)? | Yes, No |
| +4 | RCA reviewed by someone other than incident owner? | Yes, No |

### Section C - Recurring Root Cause Analysis

**Header Row:** Row 80 (after Section B ends)

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Root_Cause_Statement | 45 | Text | Free text |
| B | Occurrences | 14 | Number | Integer |
| C | First_Occurrence | 18 | Date | DD.MM.YYYY |
| D | Latest_Occurrence | 18 | Date | DD.MM.YYYY |
| E | Corrective_Action_Status | 24 | Dropdown | In_Progress, Completed, Not_Started |
| F | Risk_Register_Updated | 22 | Dropdown | Yes, No |
| G | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 10 rows for recurring root causes

---

## Sheet 4: Lessons Learned

### Section A - Lessons Learned Log

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | PIR_Reference | 18 | Text | Free text |
| B | Lesson_ID | 16 | Text | Auto: ="LL-"&TEXT(ROW()-5,"000") |
| C | Lesson_Category | 20 | Dropdown | Detection, Response, Communication, Governance, Technology, Training, Process, Other |
| D | Lesson_Summary | 50 | Text | Free text |
| E | Applicable_Teams | 30 | Text | Free text (comma-separated) |
| F | Distribution_Date | 18 | Date | DD.MM.YYYY |
| G | Distribution_Method | 24 | Dropdown | Email, Team_Meeting, KB_Update, Training, Multiple, None |
| H | Distribution_SLA_Met | 18 | Dropdown | Yes, No |
| I | Playbook_Update_Required | 22 | Dropdown | Yes, No |
| J | Playbook_Updated | 18 | Dropdown | Yes, No, N/A |
| K | Playbook_Update_Date | 20 | Date | DD.MM.YYYY |
| L | Playbook_SLA_Met | 18 | Dropdown | Yes, No, N/A |
| M | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 6-55 (50 rows)

**Conditional Formatting:**
- Column H (Distribution_SLA_Met): Green = Yes; Red = No
- Column J (Playbook_Updated): Green = Yes; Yellow = N/A; Red = No (when I = Yes)
- Column L (Playbook_SLA_Met): Green = Yes; Yellow = N/A; Red = No

### Section B - Knowledge Base Inventory

**Header Row:** Row 60

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | KB_Item | 38 | Text | Pre-filled item list (see Section 4.3) |
| B | Status | 16 | Dropdown | Exists, Outdated, Missing |
| C | Last_Updated | 16 | Date | DD.MM.YYYY |
| D | Next_Review_Due | 18 | Date | DD.MM.YYYY |
| E | Gap_Identified | 16 | Dropdown | Yes, No |
| F | Gap_Description | 40 | Text | Free text (required if E = Yes) |
| G | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 8 pre-filled items (as listed in Section 4.3 of Part I)

**Conditional Formatting:**
- Column B (Status): Green = Exists; Yellow = Outdated; Red = Missing
- Column E (Gap_Identified): Red = Yes

### Section C - Knowledge Base Governance

**Rows 75-82:** 4 Yes/No questions with notes fields. Static layout.

---

## Sheet 5: Control Improvements

### Section A - Remediation Action Register

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Action_ID | 16 | Text | Auto: ="RA-"&TEXT(ROW()-5,"000") |
| B | Source_Incident_ID | 20 | Text | Free text |
| C | Source_PIR_ID | 16 | Text | Free text |
| D | Action_Description | 45 | Text | Free text |
| E | Priority | 12 | Dropdown | Critical, High, Medium, Low |
| F | Owner | 26 | Text | Free text |
| G | Department | 22 | Text | Free text |
| H | Target_Date | 14 | Date | DD.MM.YYYY |
| I | Status | 16 | Dropdown | Not_Started, In_Progress, Completed, Blocked, Cancelled |
| J | Completion_Date | 18 | Date | DD.MM.YYYY |
| K | Overdue | 10 | Text | Formula: =IF(AND(I5<>"Completed",J5<>"",H5<TODAY()),"Yes","No") |
| L | Escalation_Triggered | 20 | Dropdown | Yes, No, N/A |
| M | Closure_Verified_By | 24 | Text | Free text |
| N | Closure_Verification_Date | 24 | Date | DD.MM.YYYY |
| O | Closure_Verified | 16 | Dropdown | Yes, No, N/A |
| P | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 6-75 (70 rows)

**Conditional Formatting:**
- Column E (Priority): Red = Critical; Orange = High; Yellow = Medium; Green = Low
- Column I (Status): Green = Completed; Blue = In_Progress; Grey = Not_Started; Red = Blocked
- Column K (Overdue): Red = Yes
- Column O (Closure_Verified): Green = Yes; Red = No (when status = Completed)

### Section B - Action Summary Metrics

**Rows 80-96:** Summary formulas

| Row | Label | Formula |
|-----|-------|---------|
| 80 | Total actions | `=COUNTA(A6:A75)` |
| 81 | Not Started | `=COUNTIF(I6:I75,"Not_Started")` |
| 82 | In Progress | `=COUNTIF(I6:I75,"In_Progress")` |
| 83 | Completed | `=COUNTIF(I6:I75,"Completed")` |
| 84 | Blocked | `=COUNTIF(I6:I75,"Blocked")` |
| 85 | Cancelled | `=COUNTIF(I6:I75,"Cancelled")` |
| 86 | Closure rate (all) | `=COUNTIF(I6:I75,"Completed")/COUNTA(I6:I75)*100` |
| 87 | Closure rate (Critical) | `=COUNTIFS(E6:E75,"Critical",I6:I75,"Completed")/COUNTIF(E6:E75,"Critical")*100` |
| 88 | Closure rate (High) | `=COUNTIFS(E6:E75,"High",I6:I75,"Completed")/COUNTIF(E6:E75,"High")*100` |
| 89 | Overdue Critical | `=COUNTIFS(E6:E75,"Critical",K6:K75,"Yes")` |
| 90 | Overdue High | `=COUNTIFS(E6:E75,"High",K6:K75,"Yes")` |
| 91 | Self-verified (non-compliant) | `=COUNTIF(O6:O75,"Yes")` where M = F (owner = verifier) - flag for manual review |
| 92 | Actions without owner | `=COUNTBLANK(F6:F75)` (where A is not blank) |
| 93 | Actions without target date | `=COUNTBLANK(H6:H75)` (where A is not blank) |

### Section C - Blocked Actions Analysis

**Header Row:** Row 100

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Action_ID | 16 | Text | Cross-ref to Section A |
| B | Block_Reason | 28 | Dropdown | Budget, Resource, Technical_Dependency, Governance, Other |
| C | Block_Since_Date | 18 | Date | DD.MM.YYYY |
| D | Escalation_Path | 34 | Text | Free text |
| E | Expected_Unblock_Date | 22 | Date | DD.MM.YYYY |
| F | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 10 rows

---

## Sheet 6: Trend Analysis

### Section A - KPI Definitions and Current Values

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | KPI_ID | 10 | Text | Auto: KPI-01 through KPI-10 |
| B | KPI_Name | 38 | Text | Pre-filled (see Section 4.5) |
| C | Measurement_Unit | 18 | Dropdown | Minutes, Hours, Percentage, Count |
| D | Target_Value | 16 | Text | Free text (org-specific target) |
| E | Current_Value | 16 | Text | Free text |
| F | Met_Target | 12 | Dropdown | Yes, No, At_Risk |
| G | Trend | 14 | Dropdown | Improving, Stable, Degrading |
| H | Reporting_Period | 20 | Text | Free text (e.g., "Q4 2025") |
| I | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 6-15 (10 pre-filled KPIs as defined in Section 4.5)

**Conditional Formatting:**
- Column F (Met_Target): Green = Yes; Yellow = At_Risk; Red = No
- Column G (Trend): Green = Improving; Yellow = Stable; Red = Degrading

### Section B - Reporting Cadence Verification

**Header Row:** Row 20

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Report_Type | 32 | Text | Pre-filled: Monthly / Quarterly / Annual |
| B | Audience | 24 | Text | Pre-filled per report type |
| C | Frequency | 14 | Text | Pre-filled |
| D | Last_Report_Date | 18 | Date | DD.MM.YYYY |
| E | On_Schedule | 14 | Dropdown | Yes, No |
| F | Distributed | 14 | Dropdown | Yes, No |
| G | Distribution_List_Complete | 26 | Dropdown | Yes, No |
| H | Content_Accuracy_Verified | 26 | Dropdown | Yes, No |
| I | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 3 rows (Monthly / Quarterly / Annual)

**Conditional Formatting:**
- Columns E-H: Green = Yes; Red = No

### Section C - Trend Accuracy Spot-Check

**Header Row:** Row 28

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | KPI_Name | 38 | Text | Free text |
| B | Reported_Value | 18 | Text | Free text |
| C | Source_Verified_Value | 24 | Text | Free text |
| D | Match | 10 | Dropdown | Yes, No |
| E | Discrepancy_Notes | 40 | Text | Free text (required if D = No) |

**Data Rows:** 3 rows

**Conditional Formatting:**
- Column D (Match): Green = Yes; Red = No

### Section D - Period-over-Period Comparison

**Rows 36-42:** 4 Yes/No questions with notes fields. Static layout.

---

## Sheet 7: Gap Analysis

### Structure

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap_ID | 12 | Text | Auto: ="GAP-"&TEXT(ROW()-5,"000") |
| B | Source_Sheet | 22 | Dropdown | PIR_Process, Root_Cause_Analysis, Lessons_Learned, Control_Improvements, Trend_Analysis |
| C | Gap_Category | 26 | Dropdown | PIR_Timeliness, PIR_Quality, RCA_Completeness, RCA_Depth, Knowledge_Gap, Distribution_Failure, Remediation_Overdue, Reporting_Gap, Other |
| D | Gap_Description | 48 | Text | Free text |
| E | Priority | 12 | Dropdown | Critical, High, Medium, Low |
| F | Current_Status | 18 | Dropdown | Open, In_Progress, Resolved, Accepted |
| G | Remediation_Action | 45 | Text | Free text |
| H | Owner | 24 | Text | Free text |
| I | Target_Date | 14 | Date | DD.MM.YYYY |
| J | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 6-35 (30 rows)

**Summary Row (Row 40):**
- Total gaps: `=COUNTA(A6:A35)`
- Critical: `=COUNTIF(E6:E35,"Critical")`
- High: `=COUNTIF(E6:E35,"High")`
- Medium: `=COUNTIF(E6:E35,"Medium")`
- Low: `=COUNTIF(E6:E35,"Low")`
- Open: `=COUNTIF(F6:F35,"Open")`
- Resolved: `=COUNTIF(F6:F35,"Resolved")`

**Conditional Formatting:**
- Column E (Priority): Red = Critical; Orange = High; Yellow = Medium; Green = Low
- Column F (Current_Status): Green = Resolved; Blue = In_Progress; Grey = Open; Yellow = Accepted

---

## Sheet 8: Evidence Register

### Structure

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Evidence_ID | 16 | Text | Auto: ="EV-S5-"&TEXT(ROW()-5,"000") |
| B | Domain | 24 | Dropdown | PIR_Process, Root_Cause_Analysis, Lessons_Learned, Control_Improvements, Trend_Analysis |
| C | Evidence_Type | 28 | Dropdown | PIR_Report, RCA_Report, LL_Log, KB_Entry, Playbook_Revision, Distribution_Record, Action_Register, Closure_Verification, Trend_Report, Dashboard_Screenshot, Other |
| D | Description | 44 | Text | Free text |
| E | File_Name | 34 | Text | Free text |
| F | Storage_Location | 38 | Text | Free text |
| G | Date_Collected | 16 | Date | DD.MM.YYYY |
| H | Collected_By | 24 | Text | Free text |
| I | Related_Incident_ID | 20 | Text | Free text (if applicable) |
| J | Verified | 12 | Dropdown | Yes, No |

**Data Rows:** 6-55 (50 rows)

---

## Sheet 9: Summary Dashboard

### Layout

**Panel 1: Overall Compliance (Rows 3-12)**

| Row | Label | Formula |
|-----|-------|---------|
| 3 | Title | "ISMS-IMP-A.5.24-28.S5 - Summary Dashboard" |
| 5 | Assessment Period | [From PIR Process sheet - auto or manual] |
| 6 | Overall Compliance Rate | Weighted average across all 5 domains |
| 7 | Total Gaps Identified | `='Gap Analysis'!A40 total` |
| 8 | Critical Gaps | `='Gap Analysis'!E40 Critical count` |
| 9 | High Gaps | `='Gap Analysis'!E40 High count` |
| 10 | Gaps Resolved | `='Gap Analysis'!F40 Resolved count` |

**Panel 2: Domain Compliance Scores (Rows 15-24)**

| Row | Domain | Compliance Score (%) | Status |
|-----|--------|----------------------|--------|
| 16 | PIR Process | Formula based on SLA compliance + quality | [X]/[!]/[N] |
| 17 | Root Cause Analysis | Formula based on RCA completion + depth | [X]/[!]/[N] |
| 18 | Lessons Learned | Formula based on LL documentation + distribution | [X]/[!]/[N] |
| 19 | Control Improvements | Formula based on closure rate + verification | [X]/[!]/[N] |
| 20 | Trend Analysis | Formula based on reporting cadence + accuracy | [X]/[!]/[N] |

**Domain Scoring Logic:**
- **PIR Process:** (SLA compliance rate x 0.4) + (Average quality score / 5 x 0.4) + (Participant requirement met rate x 0.2)
- **Root Cause Analysis:** (RCA completion rate x 0.5) + (Average depth score / 3 x 0.3) + (Quality check pass rate x 0.2)
- **Lessons Learned:** (LL entry rate per PIR x 0.3) + (Distribution SLA rate x 0.3) + (Playbook update SLA rate x 0.2) + (KB completeness x 0.2)
- **Control Improvements:** (Closure rate x 0.4) + (Critical closure rate x 0.3) + (Verification compliance x 0.2) + (No-owner/no-date rate inverted x 0.1)
- **Trend Analysis:** (Reporting cadence compliance x 0.4) + (Accuracy spot-check pass rate x 0.3) + (Period comparison completeness x 0.3)

**Panel 3: Key Metrics (Rows 27-38)**

| Metric | Value | Source |
|--------|-------|--------|
| PIR Completion Rate | [%] | Sheet 2 Summary |
| PIR SLA Compliance Rate | [%] | Sheet 2 Summary |
| Avg PIR Quality Score | [1-5] | Sheet 2 Summary |
| RCA Completion Rate (Crit/High) | [%] | Sheet 3 |
| Recurring Root Causes | [count] | Sheet 3 Section C |
| Lessons Learned Entries | [count] | Sheet 4 |
| Playbooks Requiring Update | [count] | Sheet 4 |
| Remediation Actions - Open | [count] | Sheet 5 Summary |
| Remediation Actions - Overdue Critical | [count] | Sheet 5 Summary |
| Reporting Cadence Compliance | [count of 3 met] | Sheet 6 |

**Panel 4: Critical Flags (Rows 41-50)**

Auto-generated flags for immediate attention:

| Flag | Condition | Status |
|------|-----------|--------|
| Overdue Critical Remediation Actions | Count of overdue Critical actions > 0 | [R] / [G] |
| Missing Escalation for Overdue Crit/High | Overdue Crit/High action with Escalation_Triggered = No | [R] / [G] |
| Self-Verified Closures Detected | Any action where owner = closure verifier | [R] / [G] |
| RCA Not Performed for Critical Incident | Any Critical incident with RCA_Status = Not_Performed | [R] / [G] |
| PIR Overdue > 2x SLA | Any PIR where Actual_Days > 2 x Policy_SLA_Days | [R] / [G] |
| Lessons Learned Distribution Failure | Any LL entry where Distribution_SLA_Met = No | [R] / [G] |
| Reporting Gap (Missing Report) | Any reporting cadence with On_Schedule = No | [R] / [G] |
| Knowledge Base Items Missing | Any KB item with Status = Missing | [R] / [G] |

---

## Sheet 10: Approval Sign-Off

### Structure

Static layout mirroring Section 8 of Part I:

| Row | Content |
|-----|---------|
| 3-8 | Assessment Summary block (Period, Compliance Rate, Status checkbox, Key Findings) |
| 12-18 | Completed By block (Name, Role, Department, Email, Date, Signature, Certification text) |
| 22-28 | Reviewed By block (Name, Date, Signature, Review Comments, Outcome checkboxes) |
| 32-40 | Approved By block (Name, Date, Signature, Decision checkboxes, Risk Acceptance statement) |
| 44-50 | Next Review Date block (Date, Review Cycle triggers, Interim Monitoring schedule) |
| 54-65 | Distribution List (checkboxes for each role, Storage Location) |

---

## Validation Dropdowns Summary

| Dropdown Name | Values |
|---------------|--------|
| Severity | Critical, High, Medium, Low |
| PIR_Status | Completed, Overdue, Pending, Not_Required |
| SLA_Met | Yes, No, N/A |
| RCA_Status | Completed, Overdue, Not_Performed, In_Progress |
| RCA_Methodology | 5_Whys, Fishbone, Fault_Tree, Timeline_Analysis, Other, None |
| Root_Cause_Depth | 3-Systemic, 2-Procedural, 1-Technical |
| Recurring | Yes, No |
| Lesson_Category | Detection, Response, Communication, Governance, Technology, Training, Process, Other |
| Distribution_Method | Email, Team_Meeting, KB_Update, Training, Multiple, None |
| KB_Status | Exists, Outdated, Missing |
| Action_Status | Not_Started, In_Progress, Completed, Blocked, Cancelled |
| Block_Reason | Budget, Resource, Technical_Dependency, Governance, Other |
| Met_Target | Yes, No, At_Risk |
| Trend | Improving, Stable, Degrading |
| Gap_Category | PIR_Timeliness, PIR_Quality, RCA_Completeness, RCA_Depth, Knowledge_Gap, Distribution_Failure, Remediation_Overdue, Reporting_Gap, Other |
| Gap_Status | Open, In_Progress, Resolved, Accepted |
| Priority | Critical, High, Medium, Low |
| Status | [X] Compliant, [!] Partial, [N] Non-Compliant, N/A |
| Evidence_Type | PIR_Report, RCA_Report, LL_Log, KB_Entry, Playbook_Revision, Distribution_Record, Action_Register, Closure_Verification, Trend_Report, Dashboard_Screenshot, Other |

---

## Appendix: Technical Notes for Workbook Developers

### A.1 Excel Workbook Structure

**Sheet Names (10 sheets total):**
1. Instructions & Legend
2. PIR Process
3. Root Cause Analysis
4. Lessons Learned
5. Control Improvements
6. Trend Analysis
7. Gap Analysis
8. Evidence Register
9. Summary Dashboard
10. Approval Sign-Off

### A.2 Conditional Formatting Summary

| Sheet | Column | Rule | Format |
|-------|--------|------|--------|
| PIR Process | E | Completed | Green fill |
| PIR Process | E | Overdue | Red fill |
| PIR Process | E | Pending | Yellow fill |
| PIR Process | I | Yes | Green fill |
| PIR Process | I | No | Red fill |
| PIR Process | L | 4-5 | Green fill |
| PIR Process | L | 3 | Yellow fill |
| PIR Process | L | 1-2 | Red fill |
| RCA | C | Completed | Green fill |
| RCA | C | Not_Performed / Overdue | Red fill |
| RCA | H | 3-Systemic | Green fill |
| RCA | H | 2-Procedural | Yellow fill |
| RCA | H | 1-Technical | Red fill |
| RCA | I | Yes (recurring) | Red fill |
| Lessons Learned | H | Yes | Green fill |
| Lessons Learned | H | No | Red fill |
| Control Improvements | E | Critical | Red fill |
| Control Improvements | E | High | Orange fill |
| Control Improvements | K | Yes (overdue) | Red fill |
| Control Improvements | O | No (when Completed) | Red fill |
| Trend Analysis | F | Yes | Green fill |
| Trend Analysis | F | No | Red fill |
| Trend Analysis | G | Improving | Green fill |
| Trend Analysis | G | Degrading | Red fill |
| Gap Analysis | E | Critical | Red fill |
| Gap Analysis | F | Resolved | Green fill |
| Gap Analysis | F | Open | Grey fill |

### A.3 Cell Protection

**Protected:** All formula cells, headers, static reference tables, pre-filled labels
**Unprotected (input cells):** All data entry fields (yellow fill recommended), date fields, dropdown selections, free-text fields

### A.4 Python Script Integration Points

**Script:** `generate_a524_28_s5_learning_improvement.py`

**Key Functions:**
- `create_workbook()` - Master workbook creation and sheet ordering
- `setup_styles()` - Style definitions (header, input, formula, flag)
- `create_instructions_sheet()` - Sheet 1 layout
- `create_pir_process_sheet()` - Sheet 2: inventory table + quality criteria + summary formulas
- `create_rca_sheet()` - Sheet 3: inventory + quality questions + recurring causes table
- `create_lessons_learned_sheet()` - Sheet 4: LL log + KB inventory + governance questions
- `create_control_improvements_sheet()` - Sheet 5: action register + summary metrics + blocked analysis
- `create_trend_analysis_sheet()` - Sheet 6: KPI table + reporting cadence + spot-check + comparison
- `create_gap_analysis_sheet()` - Sheet 7: consolidated gap register with summary row
- `create_evidence_register_sheet()` - Sheet 8: evidence log with auto-numbering
- `create_summary_dashboard_sheet()` - Sheet 9: 4-panel dashboard with scoring formulas and critical flags
- `create_approval_sheet()` - Sheet 10: static approval layout

**QA Script:** `excel_sanity_check_a524_28_s5.py`

### A.5 Version Control

- Filename: `ISMS-IMP-A.5.24-28.S5_Learning_Improvement_YYYYMMDD.xlsx`
- v1.0: Initial release - full 10-sheet assessment workbook

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

**Quality Checks Before Finalising:**
- [ ] All cross-references to S1-S4 documents are accurate
- [ ] Document Control version shows 1.0
- [ ] Dates in DD.MM.YYYY format throughout
- [ ] Policy SLA values match ISMS-POL-A.5.24-28 (Critical/High: 5 days, Medium: 15 days, Low: 30 days)
- [ ] All 10 KPIs in Trend Analysis are defined and targets populated
- [ ] Dashboard scoring formulas verified against domain sheet structures
- [ ] Critical Flags logic verified (conditions and cell references)
- [ ] Evidence naming convention documented and consistent
- [ ] No placeholder or template-only content remains

---

**END OF SPECIFICATION**

---

*"The idea is to try to give all the information to help others to judge the value of your contribution."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
