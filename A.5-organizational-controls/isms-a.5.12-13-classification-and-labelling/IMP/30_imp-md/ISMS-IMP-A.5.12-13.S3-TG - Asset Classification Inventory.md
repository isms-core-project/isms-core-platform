**ISMS-IMP-A.5.12-13.S3-TG - Asset Classification Inventory**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.12-13: Classification and Labelling

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.12-13.S3-TG |
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
| Filename | `ISMS-IMP-A.5.12-13.S3_Asset_Classification_Inventory_YYYYMMDD.xlsx` |
| Generator | `generate_a512_13_3_asset_classification_inventory.py` |
| Sheets | 7 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 40 | 8 |
| 2 | Asset_Inventory | Master asset list | 500+ | 13 |
| 3 | Classification_Summary | Statistics | 40 | 7 |
| 4 | Reclassification_Log | Change tracking | 50+ | 10 |
| 5 | Gap_Analysis | Non-compliance items | 50+ | 9 |
| 6 | Evidence_Register | Audit evidence | 30 | 8 |
| 7 | Approval_SignOff | Authorisation | 20 | 6 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

| Row | Content | Purpose |
|-----|---------|---------|
| 1 | Title (merged A1:H1) | Document identification |
| 3-10 | Purpose and scope | Methodology guidance |
| 12-20 | Classification ownership | Responsibility guidance |
| 22-30 | How to use instructions | Step-by-step guidance |
| 32-40 | Review cycle guidance | Timing expectations |

### Sheet 2: Asset_Inventory

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Asset_ID | 12 | Text | Required |
| B | Asset_Name | 25 | Text | Required |
| C | Asset_Type | 15 | List | Database, Document, Document Set, Application, System, Repository, Email, Media, Other |
| D | Description | 30 | Text | None |
| E | Classification | 15 | List | RESTRICTED, CONFIDENTIAL, INTERNAL, PUBLIC |
| F | Owner | 18 | Text | Required |
| G | Custodian | 15 | Text | None |
| H | Location_System | 20 | Text | None |
| I | Labelling_Status | 15 | List | Labelled, Partial, Not Labelled, N/A |
| J | Last_Review | 12 | Date | None |
| K | Next_Review | 12 | Date | None |
| L | Regulatory_Req | 15 | Text | None |
| M | Notes | 25 | Text | None |

### Sheet 3: Classification_Summary

| Column | Header | Width | Type | Content |
|:------:|--------|:-----:|------|---------|
| A | Classification | 20 | Text | Pre-populated levels |
| B | Count | 12 | Number | Formula/Input |
| C | Percentage | 12 | Percent | Formula |
| D | Labelled | 12 | Number | Formula/Input |
| E | Unlabelled | 12 | Number | Formula/Input |
| F | Compliance_% | 12 | Percent | Formula |

**Sections:**
- Assets by Classification Level (rows 5-11)
- Assets by Type (rows 15-26)
- Assets by Department (rows 29-40)

### Sheet 4: Reclassification_Log

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Change_ID | 12 | Text | None |
| B | Asset_ID | 12 | Text | From Asset_Inventory |
| C | Asset_Name | 25 | Text | Auto-populated |
| D | Previous_Class | 15 | List | RESTRICTED, CONFIDENTIAL, INTERNAL, PUBLIC |
| E | New_Class | 15 | List | RESTRICTED, CONFIDENTIAL, INTERNAL, PUBLIC |
| F | Reason_for_Change | 25 | List | Value change, Regulatory requirement, Business need, Data lifecycle, Merger/divestiture, Error correction, Periodic review, Other |
| G | Requested_By | 18 | Text | None |
| H | Approved_By | 18 | Text | None |
| I | Change_Date | 12 | Date | None |
| J | Status | 18 | List | Complete, Pending Approval, Rejected, In Progress |

### Sheet 5: Gap_Analysis

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Gap_ID | 12 | Text | None |
| B | Asset_Area | 20 | Text | None |
| C | Gap_Type | 22 | List | Unclassified Assets, Incomplete Labelling, Misclassification, No Labelling Capability, Inconsistent Labels, Missing Metadata, Other |
| D | Description | 45 | Text | None |
| E | Risk_Level | 12 | List | Critical, High, Medium, Low |
| F | Remediation_Action | 40 | Text | None |
| G | Owner | 15 | Text | None |
| H | Due_Date | 12 | Date | None |
| I | Status | 15 | List | Resolved, In Progress, Open, Accepted |

### Sheet 6: Evidence_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Evidence_ID | 15 | Text | None |
| B | Description | 40 | Text | None |
| C | Evidence_Type | 22 | List | Inventory export, Classification report, Label screenshot, Audit finding, Training record, Policy acknowledgment, Other |
| D | Related_Asset_Gap | 20 | Text | None |
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
| Asset_Inventory | E:E | ="RESTRICTED" | Red fill (#FF6B6B), White bold |
| Asset_Inventory | E:E | ="CONFIDENTIAL" | Orange fill (#FFA94D) |
| Asset_Inventory | E:E | ="INTERNAL" | Green fill (#69DB7C) |
| Asset_Inventory | E:E | ="PUBLIC" | Blue fill (#74C0FC) |
| Asset_Inventory | I:I | ="Labelled" | Green fill (#C6EFCE) |
| Asset_Inventory | I:I | ="Not Labelled" | Red fill (#FFC7CE) |
| Asset_Inventory | I:I | ="Partial" | Yellow fill (#FFEB9C) |
| Reclassification_Log | J:J | ="Complete" | Green fill (#C6EFCE) |
| Reclassification_Log | J:J | ="Pending Approval" | Yellow fill (#FFEB9C) |
| Reclassification_Log | J:J | ="Rejected" | Red fill (#FFC7CE) |
| Gap_Analysis | E:E | ="Critical" | Red fill (#FFC7CE), Bold |
| Gap_Analysis | E:E | ="High" | Orange fill (#FABF8F) |
| Gap_Analysis | I:I | ="Open" | Red fill (#FFC7CE) |
| Gap_Analysis | I:I | ="Resolved" | Green fill (#C6EFCE) |
| Evidence_Register | H:H | ="Verified" | Green fill (#C6EFCE) |
| Evidence_Register | H:H | ="Not Verified" | Red fill (#FFC7CE) |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| Asset Inventory (A.5.9) | Asset list source | A.5.9 -> Asset_Inventory |
| A.5.12-13.1 Workbook | Classification scheme | A.5.12-13.1 -> Classification levels |
| A.5.12-13.2 Workbook | Labelling standards | A.5.12-13.2 -> Labelling_Status |
| A.5.12-13.4 Workbook | Compliance monitoring | This workbook -> Compliance metrics |
| Data Discovery Tools | Classification scan results | Tools -> Asset_Inventory |
| GRC Platform | Compliance status | This workbook -> GRC |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.12-13 | Information Classification and Labelling | Parent policy |
| ISMS-IMP-A.5.12-13.S1 | Classification Scheme Definition | Classification scheme |
| ISMS-IMP-A.5.12-13.S2 | Labelling Procedures and Standards | Labelling standards |
| ISMS-IMP-A.5.12-13.S4 | Compliance Dashboard | Compliance monitoring |
| ISMS-IMP-A.5.12-13.S5 | Consolidation Dashboard | Executive view |
| ISMS-IMP-A.5.9 | Asset Inventory | Asset source |

---

**END OF SPECIFICATION**

---

*"You can't protect what you don't know you have."*
— Security Industry Proverb

<!-- QA_VERIFIED: 2026-02-06 -->
