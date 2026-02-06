**ISMS-IMP-A.5.12-13.S1-TG - Classification Scheme Definition**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.12: Classification of Information

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.12-13.S1-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.12 Classification of Information |
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
| Filename | `ISMS-IMP-A.5.12-13.S1_Classification_Scheme_Definition_YYYYMMDD.xlsx` |
| Generator | `generate_a512_13_1_classification_scheme.py` |
| Sheets | 7 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 8 |
| 2 | Classification_Levels | Level definitions | 20 | 10 |
| 3 | Handling_Requirements | Per-level controls | 30 | 5 |
| 4 | CIA_Matrix | CIA requirements | 30 | 5 |
| 5 | Regulatory_Mapping | Legal alignment | 30 | 7 |
| 6 | Evidence_Register | Audit evidence | 30 | 8 |
| 7 | Approval_SignOff | Authorisation | 20 | 6 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

| Row | Content | Purpose |
|-----|---------|---------|
| 1 | Title (merged A1:H1) | Document identification |
| 3-10 | Purpose and principles | Methodology guidance |
| 12-20 | Standard classification levels | Quick reference |
| 22-30 | How to use instructions | Step-by-step guidance |
| 32-40 | Key stakeholders | Role descriptions |

### Sheet 2: Classification_Levels

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Level_ID | 10 | Text | L1, L2, L3, L4 |
| B | Level_Name | 15 | Text | Required |
| C | Display_Label | 18 | Text | Visual format |
| D | Color_Code | 12 | Text | Hex colour |
| E | Description | 45 | Text | Required |
| F | Impact_if_Disclosed | 45 | Text | Required |
| G | Examples | 50 | Text | Required |
| H | Default_Retention | 15 | Text | None |
| I | Review_Frequency | 15 | List | Annual, Biennial, Triennial |
| J | Owner_Approval_Required | 20 | List | Yes - Executive, Yes - Manager, Yes - Owner, No |

### Sheet 3: Handling_Requirements

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Requirement_Category | 25 | Text | Pre-populated |
| B | RESTRICTED | 25 | Text | Input |
| C | CONFIDENTIAL | 25 | Text | Input |
| D | INTERNAL | 25 | Text | Input |
| E | PUBLIC | 25 | Text | Input |

**Pre-populated Categories:**
- Access Control (Need-to-know basis, Access approval, Access logging, Access review frequency)
- Storage (Encryption at rest, Storage location, Personal device storage, Cloud storage)
- Transmission (Encryption in transit, Email transmission, External sharing)
- Physical Handling (Printing, Clean desk, Secure disposal)
- Labelling (Document marking, Metadata tagging, Visual indicators)

### Sheet 4: CIA_Matrix

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Level | 15 | Text | Pre-populated |
| B | Access_Control | 25 | Text | Input |
| C | Encryption | 25 | Text | Input |
| D | Impact | 25 | Text | Input |
| E | Monitoring | 20 | Text | Input |

**Sections:**
- Confidentiality Requirements (rows 5-9)
- Integrity Requirements (rows 13-17)
- Availability Requirements (rows 21-25)

### Sheet 5: Regulatory_Mapping

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Regulation | 18 | Text | Input |
| B | Requirement | 25 | Text | Input |
| C | Data_Types_Covered | 25 | Text | Input |
| D | Min_Classification | 18 | List | RESTRICTED, CONFIDENTIAL, INTERNAL, PUBLIC |
| E | Special_Handling | 30 | Text | Input |
| F | Retention | 18 | Text | Input |
| G | Status | 18 | List | Compliant, Partial, Non-Compliant, N/A |

### Sheet 6: Evidence_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Evidence_ID | 15 | Text | None |
| B | Description | 40 | Text | None |
| C | Evidence_Type | 20 | List | Policy document, Procedure, Configuration, Screenshot, Training record, Audit report, Other |
| D | Related_Requirement | 25 | Text | None |
| E | Location | 30 | Text | None |
| F | Collected_Date | 15 | Date | None |
| G | Collected_By | 15 | Text | None |
| H | Verification_Status | 18 | List | Verified, Pending Review, Not Verified, Expired |

### Sheet 7: Approval_SignOff

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
| Classification_Levels | B:B | ="RESTRICTED" | Red fill (#FF6B6B), White bold text |
| Classification_Levels | B:B | ="CONFIDENTIAL" | Orange fill (#FFA94D), Bold |
| Classification_Levels | B:B | ="INTERNAL" | Green fill (#69DB7C), Bold |
| Classification_Levels | B:B | ="PUBLIC" | Blue fill (#74C0FC), Bold |
| Handling_Requirements | B:B | Category headers (uppercase) | Bold |
| Regulatory_Mapping | G:G | ="Compliant" | Green fill (#C6EFCE) |
| Regulatory_Mapping | G:G | ="Partial" | Yellow fill (#FFEB9C) |
| Regulatory_Mapping | G:G | ="Non-Compliant" | Red fill (#FFC7CE) |
| Evidence_Register | H:H | ="Verified" | Green fill (#C6EFCE) |
| Evidence_Register | H:H | ="Pending Review" | Yellow fill (#FFEB9C) |
| Evidence_Register | H:H | ="Not Verified" | Red fill (#FFC7CE) |
| Approval_SignOff | E:E | ="Approved" | Green fill (#C6EFCE) |
| Approval_SignOff | E:E | ="Rejected" | Red fill (#FFC7CE) |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| ISMS-POL-A.5.12-13 | Policy requirements | Policy -> This workbook |
| Asset Inventory (A.5.9) | Information types | A.5.9 -> Examples/coverage |
| Regulatory Register | Compliance requirements | ISMS-POL-00 -> Regulatory_Mapping |
| A.5.12-13.2 Workbook | Labelling procedures | This workbook -> Labelling |
| A.5.12-13.3 Workbook | Asset classification | This workbook -> Asset inventory |
| A.5.12-13.4 Workbook | Compliance monitoring | This workbook -> Compliance |
| DLP Tools | Classification enforcement | This workbook -> DLP configuration |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.12-13 | Information Classification and Labelling | Parent policy |
| ISMS-IMP-A.5.12-13.S2 | Labelling Procedures and Standards | Labelling implementation |
| ISMS-IMP-A.5.12-13.S3 | Asset Classification Inventory | Asset tracking |
| ISMS-IMP-A.5.12-13.S4 | Compliance Dashboard | Compliance monitoring |
| ISMS-IMP-A.5.12-13.S5 | Consolidation Dashboard | Executive view |
| ISMS-POL-A.5.9 | Inventory of Information and Assets | Asset source |
| ISMS-POL-A.8.12 | Data Leakage Prevention | DLP enforcement |
| ISMS-POL-A.8.24 | Use of Cryptography | Encryption requirements |

---

**END OF SPECIFICATION**

---

*"Information is the oil of the 21st century, and analytics is the combustion engine."*
— Peter Sondergaard

<!-- QA_VERIFIED: 2026-02-06 -->
