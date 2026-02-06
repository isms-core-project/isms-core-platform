**ISMS-IMP-A.5.12-13.S4-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.12-13: Classification and Labelling

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.12-13.S4-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.12-13 Classification and Labelling |
| **Parent Policy** | ISMS-POL-A.5.12-13 - Information Classification and Labelling |
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
   - [1.6 Evidence Collection](#16-evidence-collection)
   - [1.7 Common Pitfalls](#17-common-pitfalls)
   - [1.8 Quality Checklist](#18-quality-checklist)
   - [1.9 Review and Approval](#19-review-and-approval)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Technical Details](#21-workbook-technical-details)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Conditional Formatting](#23-conditional-formatting)
   - [2.4 Integration Points](#24-integration-points)
   - [2.5 Related Documents](#25-related-documents)

---

# Technical Specification

---

## 2.1 Workbook Technical Details

### File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.12-13.S4_Compliance_Dashboard_YYYYMMDD.xlsx` |
| Generator | `generate_a512_13_4_compliance_dashboard.py` |
| Sheets | 8 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Executive_Summary | High-level status | 30 | 8 |
| 2 | Compliance_Metrics | Detailed KPIs | 30 | 9 |
| 3 | Control_Assessment | A.5.12/A.5.13 eval | 30 | 6 |
| 4 | Maturity_Assessment | Maturity scoring | 30 | 6 |
| 5 | Risk_Register | Risk tracking | 30 | 10 |
| 6 | Remediation_Tracker | Action tracking | 40 | 9 |
| 7 | Evidence_Register | Audit evidence | 30 | 8 |
| 8 | Approval_SignOff | Authorisation | 20 | 6 |

---

## 2.2 Sheet Specifications

### Sheet 1: Executive_Summary

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Status_Item / Metric | 35 | Text | Pre-populated |
| B | Status / Value | 20 | Text/Number | Input |
| C | Target | 15 | Text | Pre-populated |
| D | Status | 18 | List | Complete, In Progress, Not Started, N/A |

**Sections:**
- Overall Compliance Status (rows 5-10)
- Key Metrics (rows 14-20)
- Assessment Period (rows 23-27)

### Sheet 2: Compliance_Metrics

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Metric_ID | 12 | Text | None |
| B | Metric_Name | 22 | Text | None |
| C | Description | 35 | Text | None |
| D | Measurement_Method | 22 | Text | None |
| E | Target | 12 | Text | None |
| F | Current | 12 | Number/% | Input |
| G | Trend | 12 | List | Improving, Stable, Declining, New |
| H | Owner | 12 | Text | None |
| I | Status | 15 | List | On Target, At Risk, Below Target, N/A |

### Sheet 3: Control_Assessment

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Requirement | 45 | Text | Pre-populated |
| B | Implementation | 30 | Text | Input |
| C | Evidence | 25 | Text | Input |
| D | Gap | 25 | Text | Input |
| E | Score | 18 | List | 5 - Optimised, 4 - Managed, 3 - Defined, 2 - Developing, 1 - Initial, 0 - Non-existent |
| F | Status | 15 | List | Compliant, Partial, Non-Compliant, N/A |

**Sections:**
- A.5.12: Classification of Information (rows 5-11)
- A.5.13: Labelling of Information (rows 15-21)

### Sheet 4: Maturity_Assessment

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Domain | 25 | Text | Pre-populated |
| B | Current_Level | 18 | List | 5 - Optimised, 4 - Managed, 3 - Defined, 2 - Developing, 1 - Initial, 0 - Non-existent |
| C | Target_Level | 18 | List | Same as above |
| D | Gap | 10 | Formula | Auto-calculated |
| E | Priority | 12 | List | Critical, High, Medium, Low, N/A |
| F | Notes | 35 | Text | Input |

### Sheet 5: Risk_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Risk_ID | 12 | Text | None |
| B | Risk_Description | 35 | Text | None |
| C | Risk_Category | 15 | Text | None |
| D | Likelihood | 18 | List | 5 - Almost Certain, 4 - Likely, 3 - Possible, 2 - Unlikely, 1 - Rare |
| E | Impact | 18 | List | 5 - Catastrophic, 4 - Major, 3 - Moderate, 2 - Minor, 1 - Insignificant |
| F | Risk_Score | 12 | Formula | Auto-calculated |
| G | Mitigation | 30 | Text | None |
| H | Owner | 12 | Text | None |
| I | Status | 15 | List | Mitigated, In Progress, Open, Accepted, Transferred |
| J | Review_Date | 12 | Date | None |

### Sheet 6: Remediation_Tracker

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Action_ID | 12 | Text | None |
| B | Description | 40 | Text | None |
| C | Source | 18 | List | Audit Finding, Risk Assessment, Gap Analysis, Incident, Self-Assessment, Regulatory, Other |
| D | Priority | 12 | List | Critical, High, Medium, Low |
| E | Owner | 15 | Text | None |
| F | Due_Date | 12 | Date | None |
| G | Progress | 12 | List | 0%, 25%, 50%, 75%, 100% |
| H | Status | 15 | List | Complete, In Progress, Not Started, On Hold, Cancelled |
| I | Notes | 30 | Text | None |

### Sheet 7: Evidence_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Evidence_ID | 15 | Text | None |
| B | Description | 40 | Text | None |
| C | Evidence_Type | 20 | List | Policy document, Procedure, Configuration, Screenshot, Training record, Audit report, Assessment, Metrics report, Other |
| D | Related_Control | 15 | List | A.5.12, A.5.13, Both |
| E | Location | 30 | Text | None |
| F | Collected_Date | 15 | Date | None |
| G | Collected_By | 15 | Text | None |
| H | Verification_Status | 18 | List | Verified, Pending Review, Not Verified, Expired |

### Sheet 8: Approval_SignOff

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Role | 35 | Text | Pre-populated |
| B | Name | 25 | Text | Input |
| C | Signature | 20 | Text | Input |
| D | Date | 15 | Date | Input |
| E | Decision | 22 | List | Approved, Approved with conditions, Rejected, Pending |
| F | Comments | 30 | Text | Input |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Executive_Summary | D:D | ="Complete" | Green fill (#C6EFCE) |
| Executive_Summary | D:D | ="In Progress" | Yellow fill (#FFEB9C) |
| Executive_Summary | D:D | ="Not Started" | Red fill (#FFC7CE) |
| Compliance_Metrics | I:I | ="On Target" | Green fill (#C6EFCE) |
| Compliance_Metrics | I:I | ="At Risk" | Yellow fill (#FFEB9C) |
| Compliance_Metrics | I:I | ="Below Target" | Red fill (#FFC7CE) |
| Compliance_Metrics | G:G | ="Improving" | Green text |
| Compliance_Metrics | G:G | ="Declining" | Red text |
| Control_Assessment | F:F | ="Compliant" | Green fill (#C6EFCE) |
| Control_Assessment | F:F | ="Partial" | Yellow fill (#FFEB9C) |
| Control_Assessment | F:F | ="Non-Compliant" | Red fill (#FFC7CE) |
| Maturity_Assessment | D:D | >0 | Red fill (#FFC7CE) |
| Maturity_Assessment | D:D | =0 | Green fill (#C6EFCE) |
| Risk_Register | I:I | ="Open" | Red fill (#FFC7CE) |
| Risk_Register | I:I | ="In Progress" | Yellow fill (#FFEB9C) |
| Risk_Register | I:I | ="Mitigated" | Green fill (#C6EFCE) |
| Remediation_Tracker | H:H | ="Complete" | Green fill (#C6EFCE) |
| Remediation_Tracker | H:H | ="Not Started" | Red fill (#FFC7CE) |
| Remediation_Tracker | H:H | ="In Progress" | Yellow fill (#FFEB9C) |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| A.5.12-13.1 Workbook | Scheme compliance | A.5.12-13.1 -> Control_Assessment |
| A.5.12-13.2 Workbook | Labelling compliance | A.5.12-13.2 -> Control_Assessment |
| A.5.12-13.3 Workbook | Inventory metrics | A.5.12-13.3 -> Compliance_Metrics |
| A.5.12-13.5 Workbook | Consolidation | This workbook -> A.5.12-13.5 |
| GRC Platform | Compliance data | Bidirectional |
| Risk Register | Risk data | ISMS-REG-RISK -> Risk_Register |
| Training System | Completion rates | LMS -> Compliance_Metrics |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.12-13 | Information Classification and Labelling | Parent policy |
| ISMS-IMP-A.5.12-13.S1 | Classification Scheme Definition | Scheme source |
| ISMS-IMP-A.5.12-13.S2 | Labelling Procedures and Standards | Labelling source |
| ISMS-IMP-A.5.12-13.S3 | Asset Classification Inventory | Inventory source |
| ISMS-IMP-A.5.12-13.S5 | Consolidation Dashboard | Executive consolidation |
| ISMS-REG-RISK | Risk Register | Risk integration |

---

**END OF SPECIFICATION**

---

*"Without data, you're just another person with an opinion."*
— W. Edwards Deming

<!-- QA_VERIFIED: 2026-02-06 -->
