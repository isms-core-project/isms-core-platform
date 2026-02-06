**ISMS-IMP-A.5.37.3-TG - Procedure Review and Update Tracking**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.37: Documented Operating Procedures

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.3-TG |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.37: Documented Operating Procedures |
| **Parent Policy** | ISMS-POL-A.5.37 Documented Operating Procedures Policy |
| **Related IMPs** | ISMS-IMP-A.5.37.1, ISMS-IMP-A.5.37.2, ISMS-IMP-A.5.37.4 |
| **Version** | 1.0 |
| **Classification** | Internal Use |
| **Owner** | Information Security Manager |
| **Last Review** | [Date to be set] |
| **Framework Version** | 1.0 |
| **Assessment Type** | Periodic Review and Change Management |

---

## Control Requirement

> "Operating procedures for information processing facilities should be documented and made available to personnel who need them."
>
> — ISO/IEC 27001:2022, Annex A Control 5.37

---

## Table of Contents

### PART I: USER COMPLETION GUIDE
1. [Assessment Overview](#1-assessment-overview)
2. [Control Requirements](#2-control-requirements)
3. [Prerequisites](#3-prerequisites)
4. [Review Triggers and Cycles](#4-review-triggers-and-cycles)
5. [Change Management Framework](#5-change-management-framework)
6. [Workbook Structure](#6-workbook-structure)
7. [Completion Walkthrough](#7-completion-walkthrough)
8. [Escalation Management](#8-escalation-management)
9. [Communication Requirements](#9-communication-requirements)
10. [Evidence Collection](#10-evidence-collection)
11. [Common Pitfalls](#11-common-pitfalls)
12. [Quality Checklist](#12-quality-checklist)
13. [Review and Approval](#13-review-and-approval)
14. [Related Controls](#14-related-controls)

### PART II: TECHNICAL SPECIFICATION
15. [Workbook Architecture](#15-workbook-architecture)
16. [Sheet Specifications](#16-sheet-specifications)
17. [Data Validation Rules](#17-data-validation-rules)
18. [Conditional Formatting](#18-conditional-formatting)
19. [Formula Specifications](#19-formula-specifications)
20. [Cell Styling Standards](#20-cell-styling-standards)
21. [Generator Script Reference](#21-generator-script-reference)

---

# Technical Specification

## 15. Workbook Architecture

### 15.1 Generator Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a537_3_review_tracking.py` |
| **Script Location** | `10-isms-scr-base/isms-a.5.37-documented-procedures/10_generator-master/` |
| **Output Location** | `10-isms-scr-base/isms-a.5.37-documented-procedures/90_workbooks/` |
| **Output Filename** | `ISMS-IMP-A.5.37.3_Review_Update_Tracking_YYYYMMDD.xlsx` |

### 15.2 Technical Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    WORKBOOK ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    HEADER STRUCTURE                       │   │
│  │  Row 1: Title Bar (merged A1:N1)                         │   │
│  │  Row 2: Control Reference                                 │   │
│  │  Row 3: Assessment Period                                 │   │
│  │  Row 4: Generated Date                                    │   │
│  │  Row 5: Empty (separator)                                 │   │
│  │  Row 6: Column Headers                                    │   │
│  │  Row 7+: Data Rows                                        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │ Review   │ │ Change   │ │ Version  │ │ Comms    │          │
│  │ Schedule │ │ Requests │ │ History  │ │ Log      │          │
│  │ Sheet 1  │ │ Sheet 2  │ │ Sheet 3  │ │ Sheet 4  │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │ Overdue  │ │ Evidence │ │ Metrics  │ │ Instruc- │          │
│  │ Escalate │ │ Register │ │ Summary  │ │ tions    │          │
│  │ Sheet 5  │ │ Sheet 6  │ │ Sheet 7  │ │ Sheet 8  │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 16. Sheet Specifications

### Sheet 1: Review_Schedule

**Purpose:** Track scheduled and completed reviews for all procedures

| Column | Header | Width | Data Type | Validation | Description |
|:------:|--------|:-----:|-----------|------------|-------------|
| A | Procedure_ID | 15 | Text | From Inventory | Reference to A.5.37.1 |
| B | Procedure_Name | 35 | Text | Lookup | Auto-populated from inventory |
| C | Criticality | 12 | Text | Lookup | Critical/High/Medium/Low |
| D | Review_Cycle_Days | 12 | Number | Auto | Based on criticality (180/365/365/730) |
| E | Last_Review_Date | 15 | Date | DD.MM.YYYY | Most recent review date |
| F | Next_Review_Due | 15 | Date | Formula | =E+D |
| G | Days_Until_Due | 12 | Number | Formula | =F-TODAY() |
| H | Review_Status | 12 | Text | Formula | OVERDUE/DUE SOON/CURRENT |
| I | Assigned_Reviewer | 25 | Text | Required | Person assigned to review |
| J | Review_Started | 15 | Date | DD.MM.YYYY | When review began |
| K | Review_Completed | 15 | Date | DD.MM.YYYY | When review completed |
| L | Review_Outcome | 20 | List | Dropdown | Current/Minor/Major/Obsolete/Superseded |
| M | New_Version | 10 | Text | Conditional | Version after update |
| N | Notes | 40 | Text | Optional | Review notes |

### Sheet 2: Change_Requests

**Purpose:** Log and track procedure change requests

| Column | Header | Width | Data Type | Validation | Description |
|:------:|--------|:-----:|-----------|------------|-------------|
| A | CR_ID | 15 | Text | Auto-format | CR-YYYYMM-NNN |
| B | Procedure_ID | 15 | Text | From Inventory | Affected procedure |
| C | Request_Date | 15 | Date | DD.MM.YYYY | When submitted |
| D | Requestor | 25 | Text | Required | Person requesting change |
| E | Change_Category | 15 | List | Dropdown | Administrative/Minor/Major/Emergency |
| F | Trigger | 15 | List | Dropdown | Scheduled/System/Incident/Regulatory/Audit/Personnel |
| G | Description | 40 | Text | Required | Change description |
| H | Justification | 40 | Text | Required | Reason for change |
| I | Impact_Assessment | 40 | Text | Required (non-Admin) | Training/System/Compliance impacts |
| J | Status | 15 | List | Dropdown | Submitted/Under Review/Approved/Rejected/Implemented |
| K | Approver | 25 | Text | Conditional | Who approved |
| L | Approval_Date | 15 | Date | DD.MM.YYYY | When approved |
| M | Implementation_Date | 15 | Date | DD.MM.YYYY | When implemented |
| N | Verification | 40 | Text | Optional | Implementation verification notes |

### Sheet 3: Version_History

**Purpose:** Track version history for each procedure

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Procedure_ID | 15 | Text | Reference to procedure |
| B | Version | 10 | Text | Version number (X.Y) |
| C | Effective_Date | 15 | Date | When version became active |
| D | Supersedes | 10 | Text | Previous version number |
| E | Change_Summary | 50 | Text | Summary of changes |
| F | CR_Reference | 15 | Text | Related change request ID |
| G | Approved_By | 25 | Text | Approver name |
| H | Status | 15 | List | Active/Superseded/Archived |

### Sheet 4: Communication_Log

**Purpose:** Track procedure update communications

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Comm_ID | 15 | Text | Communication identifier (COMM-YYYYMM-NNN) |
| B | Procedure_ID | 15 | Text | Related procedure |
| C | Version | 10 | Text | Version communicated |
| D | Communication_Date | 15 | Date | When sent |
| E | Communication_Method | 15 | List | Email/Intranet/Meeting/Training/Alert |
| F | Audience | 30 | Text | Who was notified |
| G | Acknowledgement_Required | 5 | Boolean | Yes/No |
| H | Acknowledgement_Target | 8 | Number | Required acknowledgements |
| I | Acknowledgements_Received | 8 | Number | Received acknowledgements |
| J | Acknowledgement_Rate | 10 | Percent | Formula: =I/H |
| K | Training_Required | 5 | Boolean | Yes/No |
| L | Training_Completion | 10 | Percent | % completed training |

### Sheet 5: Overdue_Escalation

**Purpose:** Track escalations for overdue reviews and blocked changes

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Escalation_ID | 15 | Text | ESC-YYYYMM-NNN |
| B | Item_Type | 10 | List | Review/Change Request |
| C | Item_Reference | 15 | Text | Procedure_ID or CR_ID |
| D | Days_Overdue | 10 | Number | Days past due date |
| E | Escalation_Level | 5 | List | L1/L2/L3 |
| F | Escalated_To | 30 | Text | Escalation recipient(s) |
| G | Escalation_Date | 15 | Date | When escalated |
| H | Response_Required_By | 15 | Date | Response deadline |
| I | Status | 15 | List | Open/Acknowledged/Resolved |
| J | Resolution | 40 | Text | How resolved |
| K | Resolution_Date | 15 | Date | When resolved |

### Sheet 6: Evidence_Register

**Purpose:** Link to review and change evidence

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Evidence_ID | 15 | Text | EVD-YYYYMM-NNN |
| B | Evidence_Type | 20 | List | Review Record/Approval/Communication/Training |
| C | Related_CR | 15 | Text | Change request reference |
| D | Related_Procedure | 15 | Text | Procedure ID |
| E | Description | 40 | Text | Evidence description |
| F | Collection_Date | 15 | Date | When collected |
| G | Location | 50 | Text | Storage location/path |
| H | Verified | 5 | Boolean | Evidence verified |

### Sheet 7: Metrics_Summary

**Purpose:** KPIs and trend data for dashboard

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Metric_Name | 30 | Text | KPI name |
| B | Target | 12 | Number/% | Target value |
| C | Current_Value | 12 | Number/% | Current measurement |
| D | Status | 10 | Text | Met/Not Met |
| E | Trend | 10 | Text | ↑/↓/→ |
| F | Period | 12 | Text | Measurement period |
| G | Notes | 40 | Text | Commentary |

### Sheet 8: Instructions

**Purpose:** User guidance for review and change management

Static content including:
- Review process workflow
- Change category definitions
- Escalation matrix
- Communication templates
- Evidence requirements
- Quick reference guides

---

## 17. Data Validation Rules

### 17.1 Dropdown Lists

| Field | Valid Values |
|-------|--------------|
| **Criticality** | Critical, High, Medium, Low |
| **Change_Category** | Administrative, Minor, Major, Emergency |
| **Trigger** | Scheduled Review, System Change, Incident Related, Regulatory Change, Audit Finding, Personnel Change |
| **Review_Outcome** | Current - No Changes, Minor Updates, Major Updates, Obsolete, Superseded |
| **CR_Status** | Submitted, Under Review, Approved, Rejected, Implemented |
| **Version_Status** | Active, Superseded, Archived |
| **Communication_Method** | Email, Intranet, Meeting, Training, Alert |
| **Escalation_Level** | L1, L2, L3 |
| **Escalation_Status** | Open, Acknowledged, Resolved |
| **Evidence_Type** | Review Record, Approval, Communication, Training |

### 17.2 Required Field Rules

| Sheet | Required Fields | Condition |
|-------|-----------------|-----------|
| Review_Schedule | Procedure_ID, Assigned_Reviewer | Always |
| Review_Schedule | Review_Completed, Review_Outcome | When review done |
| Change_Requests | CR_ID through Justification | Always |
| Change_Requests | Impact_Assessment | When Category ≠ Administrative |
| Change_Requests | Approver, Approval_Date | When Status = Approved |
| Change_Requests | Implementation_Date | When Status = Implemented |
| Version_History | All except F | Always |
| Communication_Log | A through F | Always |
| Communication_Log | Acknowledgement fields | When Acknowledgement_Required = Yes |

### 17.3 Cross-Field Validations

| Validation | Rule | Error Message |
|------------|------|---------------|
| Review dates | Review_Completed ≥ Review_Started | "Completion date cannot be before start date" |
| CR dates | Implementation_Date ≥ Approval_Date | "Implementation cannot be before approval" |
| Approval required | If Status = Implemented then Approver required | "Approver required for implemented changes" |
| Version sequence | New version > Previous version | "Version must increment" |

---

## 18. Conditional Formatting

### 18.1 Review_Schedule Sheet

| Range | Condition | Format |
|-------|-----------|--------|
| Column H (Status) | "OVERDUE" | Red fill (#FF0000), white bold text |
| Column H (Status) | "DUE SOON" | Yellow fill (#FFFF00), black text |
| Column H (Status) | "CURRENT" | Green fill (#90EE90), black text |
| Column G (Days) | <0 | Red fill (#FFCCCC) |
| Column G (Days) | 0-30 | Yellow fill (#FFFFCC) |
| Column G (Days) | >30 | Green fill (#CCFFCC) |

### 18.2 Change_Requests Sheet

| Range | Condition | Format |
|-------|-----------|--------|
| Row | Status = "Rejected" | Grey strikethrough |
| Row | Status = "Implemented" | Light green fill (#E8F5E9) |
| Column E (Category) | "Emergency" | Red bold text |
| Column E (Category) | "Major" | Orange text |

### 18.3 Communication_Log Sheet

| Range | Condition | Format |
|-------|-----------|--------|
| Column J (Ack Rate) | <50% | Red fill |
| Column J (Ack Rate) | 50-79% | Yellow fill |
| Column J (Ack Rate) | ≥80% | Green fill |
| Column L (Training) | <100% when required | Yellow fill |

### 18.4 Overdue_Escalation Sheet

| Range | Condition | Format |
|-------|-----------|--------|
| Column E (Level) | "L3" | Red fill, white bold |
| Column E (Level) | "L2" | Orange fill |
| Column E (Level) | "L1" | Yellow fill |
| Column I (Status) | "Resolved" | Green fill |
| Column D (Days) | >30 | Red bold text |

---

## 19. Formula Specifications

### 19.1 Review Schedule Formulas

**Next Review Due (Column F):**
```excel
=E2+D2
```

**Days Until Due (Column G):**
```excel
=F2-TODAY()
```

**Review Status (Column H):**
```excel
=IF(G2<0,"OVERDUE",IF(G2<=30,"DUE SOON","CURRENT"))
```

**Review Cycle Days (Column D):**
```excel
=IF(C2="Critical",180,IF(C2="High",365,IF(C2="Medium",365,IF(C2="Low",730,365))))
```

### 19.2 Metrics Formulas

**Reviews On-Time Rate:**
```excel
=COUNTIFS(Review_Schedule!K:K,"<>"&"",Review_Schedule!K:K,"<="&Review_Schedule!F:F)/
 COUNTIF(Review_Schedule!K:K,"<>"&"")*100
```

**Overdue Review Count:**
```excel
=COUNTIF(Review_Schedule!H:H,"OVERDUE")
```

**Average Review Cycle Time:**
```excel
=AVERAGE(Review_Schedule!K:K-Review_Schedule!J:J)
```

**CR Cycle Time (Submission to Implementation):**
```excel
=AVERAGEIFS(Change_Requests!M:M-Change_Requests!C:C,Change_Requests!J:J,"Implemented")
```

**CR Approval Rate:**
```excel
=COUNTIF(Change_Requests!J:J,"Approved")/
 (COUNTIF(Change_Requests!J:J,"Approved")+COUNTIF(Change_Requests!J:J,"Rejected"))*100
```

**Communication Acknowledgement Average:**
```excel
=AVERAGEIF(Communication_Log!G:G,"Yes",Communication_Log!J:J)
```

**Open Escalations:**
```excel
=COUNTIF(Overdue_Escalation!I:I,"Open")
```

---

## 20. Cell Styling Standards

### 20.1 Colour Palette

| Element | Colour | Hex Code | Usage |
|---------|--------|----------|-------|
| Header Background | Dark Blue | #1F4E79 | Title rows, column headers |
| Header Text | White | #FFFFFF | Header text |
| Subheader | Medium Blue | #2E75B6 | Section headers |
| Data Row (Odd) | White | #FFFFFF | Odd data rows |
| Data Row (Even) | Light Blue | #DEEBF7 | Even data rows (zebra) |
| Overdue/Critical | Red | #FF0000 | Overdue items, L3 escalations |
| Warning | Yellow | #FFFF00 | Due soon, L1 escalations |
| Success | Green | #90EE90 | Current, resolved |
| Border | Grey | #D0D0D0 | Cell borders |

### 20.2 Font Standards

| Element | Font | Size | Style |
|---------|------|:----:|-------|
| Title | Calibri | 16 | Bold |
| Column Headers | Calibri | 11 | Bold |
| Data Cells | Calibri | 10 | Regular |
| Notes/Comments | Calibri | 9 | Italic |
| Formulas Display | Calibri | 10 | Regular |

### 20.3 Number Formats

| Data Type | Format | Example |
|-----------|--------|---------|
| Date | DD.MM.YYYY | 03.02.2026 |
| Days | 0 | 14 |
| Percentage | 0% | 95% |
| CR ID | Text | CR-202602-001 |
| Version | Text | 1.2 |

---

## 21. Generator Script Reference

### 21.1 Script Structure

```python
# =============================================================================
# ISMS-IMP-A.5.37.3 - Procedure Review and Update Tracking Generator
# =============================================================================
# ISO 27001:2022 Control A.5.37: Documented Operating Procedures
# Generates assessment workbook for review cycle and change management
# =============================================================================

# Document Metadata
DOCUMENT_ID = "ISMS-IMP-A.5.37.3"
WORKBOOK_NAME = "Review Update Tracking"
CONTROL_ID = "A.5.37"
CONTROL_NAME = "Documented Operating Procedures"

# Output Configuration
OUTPUT_FILENAME = f"{DOCUMENT_ID}_Review_Update_Tracking_{GENERATED_TIMESTAMP}.xlsx"
```

### 21.2 Key Functions

| Function | Purpose |
|----------|---------|
| `create_workbook()` | Initialise workbook with standard structure |
| `create_review_schedule_sheet()` | Generate Review_Schedule sheet |
| `create_change_requests_sheet()` | Generate Change_Requests sheet |
| `create_version_history_sheet()` | Generate Version_History sheet |
| `create_communication_log_sheet()` | Generate Communication_Log sheet |
| `create_escalation_sheet()` | Generate Overdue_Escalation sheet |
| `create_evidence_register_sheet()` | Generate Evidence_Register sheet |
| `create_metrics_summary_sheet()` | Generate Metrics_Summary sheet |
| `create_instructions_sheet()` | Generate Instructions sheet |
| `apply_data_validation()` | Add dropdown lists and validation |
| `apply_conditional_formatting()` | Apply status-based formatting |
| `apply_formulas()` | Add calculated fields |
| `style_workbook()` | Apply consistent styling |

### 21.3 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| openpyxl | ≥3.0.0 | Excel workbook generation |
| datetime | stdlib | Date handling |
| logging | stdlib | Execution logging |

### 21.4 Execution

```bash
cd 10-isms-scr-base/isms-a.5.37-documented-procedures/10_generator-master/
python3 generate_a537_3_review_tracking.py
mv ISMS-IMP-A.5.37.3_*.xlsx ../90_workbooks/
```

### 21.5 Output Verification

After generation, verify:
- [ ] All 8 sheets created
- [ ] Headers styled correctly
- [ ] Data validation dropdowns functional
- [ ] Conditional formatting applied
- [ ] Formulas calculate correctly
- [ ] Column widths appropriate
- [ ] Print area configured

---

**END OF SPECIFICATION**

---

*"The only constant in life is change."*
— Heraclitus

<!-- QA_VERIFIED: 2026-02-06 -->
