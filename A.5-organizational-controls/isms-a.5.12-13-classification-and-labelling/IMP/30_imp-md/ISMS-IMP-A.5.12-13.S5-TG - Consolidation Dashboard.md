**ISMS-IMP-A.5.12-13.S5-TG - Consolidation Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.12-13: Classification and Labelling

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.12-13.S5-TG |
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
| Filename | `ISMS-IMP-A.5.12-13.S5_Consolidation_Dashboard_YYYYMMDD.xlsx` |
| Generator | `generate_a512_13_5_consolidation_dashboard.py` |
| Sheets | 12 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Dashboard guidance | 30 | 1 |
| 2 | Executive_Summary | High-level view | 25 | 8 |
| 3 | Domain_Overview | Per-domain status | 30 | 5 |
| 4 | Classification_Compliance | Scheme status | 15 | 8 |
| 5 | Labelling_Compliance | Labelling status | 20 | 8 |
| 6 | Inventory_Compliance | Asset coverage | 15 | 8 |
| 7 | Cross_Domain_Gaps | Cross-cutting gaps | 20 | 10 |
| 8 | Remediation_Tracker | All remediation | 20 | 11 |
| 9 | KPI_Summary | Consolidated KPIs | 15 | 6 |
| 10 | Evidence_Index | Evidence links | 20 | 8 |
| 11 | Trend_Dashboard | Historical trends | 15 | 8 |
| 12 | Approval_SignOff | Executive approval | 15 | 5 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

| Row | Content | Purpose |
|-----|---------|---------|
| 1 | Title | Document identification |
| 3-6 | Purpose | Dashboard purpose |
| 8-12 | Source workbooks | Reference list |
| 14-18 | Compliance scoring | Scoring methodology |
| 20-22 | Generated info | Date and control reference |

### Sheet 2: Executive_Summary

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Domain / Metric | 35 | Text | Pre-populated |
| B | Workbook | 35 | Text | Pre-populated |
| C | Status | 18 | List | Compliant, Partial, Non-Compliant |
| D | Score % | 12 | Percent | Input |
| E | Critical Gaps | 15 | Number | Input |
| F | Last Updated | 15 | Date | Input |

**Sections:**
- Reporting Period (rows 3-5)
- Overall Compliance Status (rows 6-11)
- Key Metrics (rows 14-18)

### Sheet 3: Domain_Overview

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Requirement | 40 | Text | Pre-populated |
| B | Status | 18 | List | Complete, In Progress, Not Started, N/A |
| C | Evidence_Ref | 15 | Text | Input |
| D | Gap_Description | 35 | Text | Input |
| E | Remediation | 35 | Text | Input |

**Sections:**
- Domain 1: Classification Scheme (rows 3-8)
- Domain 2: Labelling Standards (rows 10-15)
- Domain 3: Asset Inventory (rows 17-22)

### Sheet 4: Classification_Compliance

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Classification_Level | 20 | Text | Pre-populated |
| B | Definition_Status | 18 | List | Complete, Partial, Missing |
| C | Handling_Rules | 18 | List | Complete, Partial, Missing |
| D | Examples_Documented | 20 | List | Yes, No |
| E | Training_Available | 18 | List | Yes, No |
| F | Compliance_Status | 18 | List | Compliant, Partial, Non-Compliant |
| G | Gap_Notes | 30 | Text | Input |
| H | Owner | 20 | Text | Input |

### Sheet 5: Labelling_Compliance

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Asset_Type | 18 | Text | Pre-populated |
| B | Digital_Label_Standard | 22 | List | Defined, Partial, Not Defined |
| C | Physical_Label_Standard | 22 | List | Defined, Partial, Not Defined, N/A |
| D | Automation_Status | 18 | List | Deployed, Partial, Not Deployed, N/A |
| E | Compliance_Status | 18 | List | Compliant, Partial, Non-Compliant |
| F | Gap_Notes | 30 | Text | Input |
| G | Remediation | 25 | Text | Input |
| H | Owner | 18 | Text | Input |

### Sheet 6: Inventory_Compliance

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Asset_Category | 22 | Text | Pre-populated |
| B | Total_Assets | 14 | Number | Input |
| C | Classified | 14 | Number | Input |
| D | Labelled | 14 | Number | Input |
| E | Percent_Complete | 12 | Percent | Formula |
| F | Compliance_Status | 18 | List | Compliant, Partial, Non-Compliant |
| G | Gap_Notes | 30 | Text | Input |
| H | Owner | 18 | Text | Input |

### Sheet 7: Cross_Domain_Gaps

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Gap_ID | 10 | Text | Auto-generated |
| B | Source_Domain | 22 | List | A.5.12-13.1, A.5.12-13.2, A.5.12-13.3, A.5.12-13.4, Cross-Domain |
| C | Gap_Description | 40 | Text | Input |
| D | Risk_Rating | 12 | List | Critical, High, Medium, Low |
| E | Priority | 10 | List | Critical, High, Medium, Low |
| F | Affected_Controls | 18 | Text | Input |
| G | Root_Cause | 30 | Text | Input |
| H | Remediation_Action | 35 | Text | Input |
| I | Owner | 18 | Text | Input |
| J | Target_Date | 15 | Date | Input |

### Sheet 8: Remediation_Tracker

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Action_ID | 10 | Text | None |
| B | Related_Gap | 12 | Text | None |
| C | Source_Domain | 20 | List | A.5.12-13.1, A.5.12-13.2, A.5.12-13.3, A.5.12-13.4, Cross-Domain |
| D | Action_Description | 40 | Text | None |
| E | Priority | 10 | List | Critical, High, Medium, Low |
| F | Owner | 18 | Text | None |
| G | Start_Date | 12 | Date | None |
| H | Target_Date | 12 | Date | None |
| I | Status | 12 | List | Not Started, In Progress, Complete, On Hold |
| J | Progress_% | 10 | List | 0%, 25%, 50%, 75%, 100% |
| K | Notes | 30 | Text | None |

### Sheet 9: KPI_Summary

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | KPI | 42 | Text | Pre-populated |
| B | Target | 15 | Text | Pre-populated |
| C | Current | 12 | Text/Number | Input |
| D | Previous | 12 | Text/Number | Input |
| E | Trend | 10 | List | ↑, →, ↓ |
| F | Status | 15 | List | On Target, At Risk, Below Target |

### Sheet 10: Evidence_Index

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Evidence_ID | 12 | Text | None |
| B | Source_Workbook | 25 | List | A.5.12-13.1, A.5.12-13.2, A.5.12-13.3, A.5.12-13.4 |
| C | Source_Sheet | 22 | Text | None |
| D | Evidence_Type | 18 | Text | None |
| E | Evidence_Description | 40 | Text | None |
| F | Location_Reference | 30 | Text | None |
| G | Date_Captured | 15 | Date | None |
| H | Validation_Status | 18 | List | Validated, Pending, Not Validated |

### Sheet 11: Trend_Dashboard

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Period | 12 | Text | Pre-populated |
| B | Classification_% | 16 | Percent | Input |
| C | Labelling_% | 14 | Percent | Input |
| D | Inventory_% | 14 | Percent | Input |
| E | Overall_% | 12 | Percent | Formula |
| F | Critical_Gaps | 15 | Number | Input |
| G | Remediation_Rate | 18 | Percent | Input |
| H | Notes | 35 | Text | Input |

### Sheet 12: Approval_SignOff

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Role | 30 | Text | Pre-populated |
| B | Name | 25 | Text | Input |
| C | Date | 15 | Date | Input |
| D | Signature | 20 | Text | Input |
| E | Comments | 40 | Text | Input |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Executive_Summary | C:C | ="Compliant" | Green fill (#C6EFCE) |
| Executive_Summary | C:C | ="Partial" | Yellow fill (#FFEB9C) |
| Executive_Summary | C:C | ="Non-Compliant" | Red fill (#FFC7CE) |
| Domain_Overview | B:B | ="Complete" | Green fill (#C6EFCE) |
| Domain_Overview | B:B | ="In Progress" | Yellow fill (#FFEB9C) |
| Domain_Overview | B:B | ="Not Started" | Red fill (#FFC7CE) |
| Classification_Compliance | F:F | ="Compliant" | Green fill (#C6EFCE) |
| Classification_Compliance | F:F | ="Non-Compliant" | Red fill (#FFC7CE) |
| Labelling_Compliance | E:E | ="Compliant" | Green fill (#C6EFCE) |
| Labelling_Compliance | E:E | ="Non-Compliant" | Red fill (#FFC7CE) |
| Inventory_Compliance | F:F | ="Compliant" | Green fill (#C6EFCE) |
| Inventory_Compliance | F:F | ="Non-Compliant" | Red fill (#FFC7CE) |
| Cross_Domain_Gaps | D:D | ="Critical" | Red fill (#FFC7CE), Bold |
| Cross_Domain_Gaps | D:D | ="High" | Orange fill (#FABF8F) |
| Remediation_Tracker | I:I | ="Complete" | Green fill (#C6EFCE) |
| Remediation_Tracker | I:I | ="Not Started" | Red fill (#FFC7CE) |
| KPI_Summary | F:F | ="On Target" | Green fill (#C6EFCE) |
| KPI_Summary | F:F | ="Below Target" | Red fill (#FFC7CE) |
| KPI_Summary | E:E | ="↑" | Green text |
| KPI_Summary | E:E | ="↓" | Red text |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| A.5.12-13.1 Workbook | Classification scheme data | A.5.12-13.1 -> Classification_Compliance |
| A.5.12-13.2 Workbook | Labelling data | A.5.12-13.2 -> Labelling_Compliance |
| A.5.12-13.3 Workbook | Inventory data | A.5.12-13.3 -> Inventory_Compliance |
| A.5.12-13.4 Workbook | Metrics and remediation | A.5.12-13.4 -> KPI_Summary, Remediation |
| GRC Platform | Compliance reporting | This workbook -> GRC |
| Executive Reporting | Management dashboards | This workbook -> Board reports |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.12-13 | Information Classification and Labelling | Parent policy |
| ISMS-IMP-A.5.12-13.S1 | Classification Scheme Definition | Source workbook |
| ISMS-IMP-A.5.12-13.S2 | Labelling Procedures and Standards | Source workbook |
| ISMS-IMP-A.5.12-13.S3 | Asset Classification Inventory | Source workbook |
| ISMS-IMP-A.5.12-13.S4 | Compliance Dashboard | Source workbook |

---

**END OF SPECIFICATION**

---

*"The whole is greater than the sum of its parts."*
— Aristotle

<!-- QA_VERIFIED: 2026-02-06 -->
