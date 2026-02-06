**ISMS-IMP-A.5.35-36.S1-TG - Independent Review Planning and Tracking**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.35

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.35-36.S1-TG |
| **Title** | Independent Review Planning and Tracking |
| **Control Reference** | ISO/IEC 27001:2022 A.5.35 |
| **Control Name** | Independent Review of Information Security |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

# Technical Specification

### Workbook Architecture

**File Details**:

- Filename: `ISMS-IMP-A.5.35-36.S1_Independent_Review_Planning_and_Tracking_YYYYMMDD.xlsx`
- Format: Microsoft Excel (.xlsx)
- Sheets: 8

### Sheet Specifications

#### Review_Schedule Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Review_ID | 14 | Auto-format REV-YYYY-NNN |
| B | Review_Type | 18 | Data validation |
| C | Planned_Year | 12 | Year (2025, 2026, etc.) |
| D | Planned_Quarter | 12 | Data validation |
| E | Planned_Start | 14 | Date field |
| F | Planned_End | 14 | Date field |
| G | Scope_Summary | 40 | User input |
| H | Trigger | 18 | Data validation |
| I | Assigned_Reviewer | 22 | User input |
| J | Status | 14 | Data validation |
| K | Notes | 30 | User input |

#### Reviewer_Registry Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Reviewer_ID | 14 | Auto-format |
| B | Reviewer_Name | 25 | User input |
| C | Organisation | 25 | User input |
| D | Type | 20 | Data validation |
| E | Qualifications | 35 | User input |
| F | Experience_Years | 12 | Numeric |
| G | Independence_Status | 18 | Data validation |
| H | Independence_Notes | 30 | User input |
| I | Approved_Date | 14 | Date field |
| J | Last_Used | 14 | Date field |
| K | Status | 12 | Data validation |

#### Review_Scope Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Review_ID | 14 | Link to Review_Schedule |
| B | Scope_Item | 35 | User input |
| C | Control_Ref | 14 | ISO control reference |
| D | Review_Criteria | 35 | User input |
| E | Methodology | 16 | Data validation |
| F | Sample_Approach | 14 | Data validation |
| G | Key_Contacts | 25 | User input |
| H | Documentation_Required | 35 | User input |
| I | Priority | 12 | Data validation |

#### Review_Execution Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Review_ID | 14 | Link to Review_Schedule |
| B | Phase | 14 | Data validation |
| C | Activity | 35 | User input |
| D | Assigned_Reviewer | 22 | Link to Reviewer_Registry |
| E | Planned_Start | 14 | Date field |
| F | Actual_Start | 14 | Date field |
| G | Planned_End | 14 | Date field |
| H | Actual_End | 14 | Date field |
| I | Status | 14 | Data validation |
| J | Notes | 30 | User input |

#### Findings_Summary Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Review_ID | 14 | Link to Review_Schedule |
| B | Total_Findings | 12 | Numeric |
| C | Critical | 10 | Numeric |
| D | High | 10 | Numeric |
| E | Medium | 10 | Numeric |
| F | Low | 10 | Numeric |
| G | Observations | 12 | Numeric |
| H | Overall_Opinion | 20 | Data validation |
| I | Key_Strengths | 40 | User input |
| J | Key_Weaknesses | 40 | User input |
| K | Report_Date | 14 | Date field |
| L | Report_Ref | 20 | User input |

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Review_Type | Full ISMS, Partial, Specific Control, Thematic, Ad-hoc |
| Planned_Quarter | Q1, Q2, Q3, Q4 |
| Trigger | Planned Interval, Significant Change, Regulatory, Management Request, Other |
| Schedule_Status | Scheduled, In Planning, In Progress, Completed, Cancelled, Deferred |
| Reviewer_Type | Internal Auditor, External Auditor, Third-Party Consultant |
| Independence_Status | Independent, Conflict Declared, Not Independent, Pending Assessment |
| Reviewer_Status | Active, Inactive, Suspended |
| Methodology | Document Review, Interview, Testing, Observation, Combined |
| Sample_Approach | Full Coverage, Statistical Sample, Judgmental Sample |
| Priority | High, Medium, Low |
| Phase | Planning, Fieldwork, Reporting, Closure |
| Execution_Status | Not Started, In Progress, Complete, Delayed, On Hold |
| Overall_Opinion | Effective, Partially Effective, Ineffective, Unable to Conclude |

### Generator Reference

**Script**: `generate_a535_36_1_independent_review.py`

**Location**: `10-isms-scr-base/isms-a.5.35-36-compliance-review/10_generator-master/`

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
