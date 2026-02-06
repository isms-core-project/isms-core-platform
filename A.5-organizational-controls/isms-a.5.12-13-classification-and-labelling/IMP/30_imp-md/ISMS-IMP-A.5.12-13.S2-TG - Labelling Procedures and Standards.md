**ISMS-IMP-A.5.12-13.S2-TG - Labelling Procedures and Standards**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.13: Labelling of Information

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.12-13.S2-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.13 Labelling of Information |
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
| Filename | `ISMS-IMP-A.5.12-13.S2_Labelling_Procedures_and_Standards_YYYYMMDD.xlsx` |
| Generator | `generate_a512_13_2_labelling_procedures.py` |
| Sheets | 7 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 40 | 8 |
| 2 | Labelling_Standards | Visual formats | 20 | 9 |
| 3 | Digital_Labelling | Electronic labelling | 30 | 7 |
| 4 | Physical_Labelling | Paper and media | 30 | 7 |
| 5 | Automation_Tools | Tool inventory | 20 | 8 |
| 6 | Evidence_Register | Audit evidence | 30 | 8 |
| 7 | Approval_SignOff | Authorisation | 20 | 6 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

| Row | Content | Purpose |
|-----|---------|---------|
| 1 | Title (merged A1:H1) | Document identification |
| 3-10 | Purpose and principles | Methodology guidance |
| 12-20 | Labelling methods overview | Quick reference |
| 22-30 | How to use instructions | Step-by-step guidance |

### Sheet 2: Labelling_Standards

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Classification_Level | 18 | Text | Pre-populated |
| B | Display_Text | 18 | Text | Input |
| C | Color_Hex | 12 | Text | Hex format |
| D | Header_Format | 30 | Text | Input |
| E | Footer_Format | 40 | Text | Input |
| F | Watermark_Text | 25 | Text | Input |
| G | Banner_Style | 25 | Text | Input |
| H | Icon_Symbol | 20 | Text | Input |
| I | Font_Requirements | 25 | Text | Input |

### Sheet 3: Digital_Labelling

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Asset_Type | 25 | Text | Pre-populated |
| B | Labelling_Method | 35 | Text | Input |
| C | Metadata_Fields | 40 | Text | Input |
| D | Automation | 30 | Text | Input |
| E | Validation | 20 | Text | Input |
| F | Responsibility | 18 | Text | Input |
| G | Implementation_Status | 18 | List | Implemented, In Progress, Not Implemented, N/A |

### Sheet 4: Physical_Labelling

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Asset_Type | 20 | Text | Pre-populated |
| B | Labelling_Method | 35 | Text | Input |
| C | Label_Location | 30 | Text | Input |
| D | Label_Format | 40 | Text | Input |
| E | Durability | 20 | Text | Input |
| F | Responsible_Party | 20 | Text | Input |
| G | Implementation_Status | 18 | List | Implemented, In Progress, Not Implemented, N/A |

### Sheet 5: Automation_Tools

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Tool_Name | 35 | Text | Input |
| B | Vendor | 15 | Text | Input |
| C | Scope_Coverage | 25 | Text | Input |
| D | Key_Features | 45 | Text | Input |
| E | Integration_Points | 30 | Text | Input |
| F | Licence_Type | 18 | Text | Input |
| G | Implementation_Status | 20 | List | Deployed, Pilot, Evaluating, Not Implemented, Planned |
| H | Owner | 15 | Text | Input |

### Sheet 6: Evidence_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Evidence_ID | 15 | Text | None |
| B | Description | 40 | Text | None |
| C | Evidence_Type | 22 | List | Procedure document, Configuration screenshot, Label sample, Training record, Tool export, Audit report, Other |
| D | Related_Procedure | 25 | Text | None |
| E | Location | 30 | Text | None |
| F | Collected_Date | 15 | Date | None |
| G | Collected_By | 15 | Text | None |
| H | Verification_Status | 18 | List | Verified, Pending Review, Not Verified, Expired |

### Sheet 7: Approval_SignOff

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Role | 30 | Text | Pre-populated |
| B | Name | 25 | Text | Input |
| C | Signature | 20 | Text | Input |
| D | Date | 15 | Date | Input |
| E | Decision | 22 | List | Approved, Approved with conditions, Rejected, Pending |
| F | Comments | 30 | Text | Input |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Labelling_Standards | A:A | ="RESTRICTED" | Red fill (#FF6B6B), White bold |
| Labelling_Standards | A:A | ="CONFIDENTIAL" | Orange fill (#FFA94D) |
| Labelling_Standards | A:A | ="INTERNAL" | Green fill (#69DB7C) |
| Labelling_Standards | A:A | ="PUBLIC" | Blue fill (#74C0FC) |
| Digital_Labelling | G:G | ="Implemented" | Green fill (#C6EFCE) |
| Digital_Labelling | G:G | ="In Progress" | Yellow fill (#FFEB9C) |
| Digital_Labelling | G:G | ="Not Implemented" | Red fill (#FFC7CE) |
| Physical_Labelling | G:G | ="Implemented" | Green fill (#C6EFCE) |
| Physical_Labelling | G:G | ="Not Implemented" | Red fill (#FFC7CE) |
| Automation_Tools | G:G | ="Deployed" | Green fill (#C6EFCE) |
| Automation_Tools | G:G | ="Pilot" | Yellow fill (#FFEB9C) |
| Automation_Tools | G:G | ="Not Implemented" | Red fill (#FFC7CE) |
| Evidence_Register | H:H | ="Verified" | Green fill (#C6EFCE) |
| Evidence_Register | H:H | ="Not Verified" | Red fill (#FFC7CE) |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| A.5.12-13.1 Workbook | Classification scheme | A.5.12-13.1 -> Labelling_Standards |
| Microsoft Purview | Sensitivity labels | This workbook -> MIP configuration |
| Email System | Transport rules | This workbook -> Exchange rules |
| DLP Solution | Label-based policies | This workbook -> DLP rules |
| Document Management | Metadata standards | This workbook -> DMS configuration |
| A.5.12-13.3 Workbook | Asset classification | Bidirectional |
| A.5.12-13.4 Workbook | Compliance monitoring | This workbook -> Compliance |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.12-13 | Information Classification and Labelling | Parent policy |
| ISMS-IMP-A.5.12-13.S1 | Classification Scheme Definition | Classification scheme |
| ISMS-IMP-A.5.12-13.S3 | Asset Classification Inventory | Asset tracking |
| ISMS-IMP-A.5.12-13.S4 | Compliance Dashboard | Compliance monitoring |
| ISMS-IMP-A.5.12-13.S5 | Consolidation Dashboard | Executive view |
| ISMS-POL-A.8.12 | Data Leakage Prevention | DLP integration |

---

**END OF SPECIFICATION**

---

*"The single biggest problem in communication is the illusion that it has taken place."*
— George Bernard Shaw

<!-- QA_VERIFIED: 2026-02-06 -->
