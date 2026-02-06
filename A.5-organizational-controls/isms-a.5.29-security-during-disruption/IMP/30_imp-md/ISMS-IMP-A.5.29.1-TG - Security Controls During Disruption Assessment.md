**ISMS-IMP-A.5.29.1-TG - Security Controls During Disruption Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.29

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.29.1-TG |
| **Title** | Security Controls During Disruption Assessment |
| **Control Reference** | ISO/IEC 27001:2022 A.5.29 |
| **Control Name** | Information Security During Disruption |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Chief Information Security Officer (CISO) |
| **Classification** | Internal |
| **Framework Version** | 1.0 |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Disruption Categories](#14-disruption-categories)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 Security Control Classification](#17-security-control-classification)
   - [1.8 Evidence Collection](#18-evidence-collection)
   - [1.9 Common Pitfalls](#19-common-pitfalls)
   - [1.10 Quality Checklist](#110-quality-checklist)
   - [1.11 Review and Approval](#111-review-and-approval)
   - [1.12 Integration with Other Controls](#112-integration-with-other-controls)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Architecture](#21-workbook-architecture)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Data Validations](#23-data-validations)
   - [2.4 Conditional Formatting](#24-conditional-formatting)
   - [2.5 Formula Specifications](#25-formula-specifications)
   - [2.6 Cell Styling Standards](#26-cell-styling-standards)
   - [2.7 Generator Script Reference](#27-generator-script-reference)

---

# Technical Specification

---

## 2.1 Workbook Architecture

### File Naming Convention

```
ISMS-IMP-A.5.29.1_Security_Controls_During_Disruption_YYYYMMDD.xlsx
```

### Sheet Tab Order

1. Instructions
2. Security_Control_Inventory
3. Minimum_Baseline
4. Security_Posture_Levels
5. Compensating_Controls
6. BCDR_Security_Review
7. Evidence_Register
8. Approval_SignOff

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

| Row | Content |
|-----|---------|
| 1 | Header: "ISMS-IMP-A.5.29.1 - Security Controls During Disruption Assessment" |
| 3-12 | Document information (ID, version, date, etc.) |
| 14+ | How to use this workbook |

### Sheet 2: Security_Control_Inventory

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Control_ID | 15 | Text | Required |
| B | Control_Name | 35 | Text | Required |
| C | Control_Category | 20 | List | Access Control, Data Encryption, Logging, Network Security, Backup Protection, Endpoint Security, Physical Security, Other |
| D | ISO_Reference | 15 | Text | Optional |
| E | Normal_Status | 15 | List | Operational, Partial, Not Applicable |
| F | Disruption_Classification | 20 | List | Non-Negotiable, Degradable, Deferrable, Not Applicable |
| G | Recovery_Priority | 15 | List | Critical, High, Medium, Low |
| H | Compensating_Control_ID | 15 | Text | Reference to Compensating_Controls |
| I | Owner | 25 | Text | Required |
| J | Last_Review_Date | 15 | Date | Required |
| K | Notes | 40 | Text | Optional |

### Sheet 3: Minimum_Baseline

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Control_ID | 15 | Text | From Security_Control_Inventory |
| B | Control_Name | 35 | Text | Auto-populate |
| C | Category | 20 | Text | Auto-populate |
| D | Minimum_Requirement | 40 | Text | Required |
| E | Rationale | 40 | Text | Required |
| F | Never_Acceptable_Actions | 40 | Text | Required |
| G | Approval_Status | 15 | List | Pending, Approved, Rejected |
| H | Approved_By | 25 | Text | Required if Approved |
| I | Approval_Date | 15 | Date | Required if Approved |

### Sheet 4: Security_Posture_Levels

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Posture_Level | 15 | List | Normal, Elevated, Degraded, Emergency, Recovery |
| B | Description | 40 | Text | Required |
| C | Trigger_Conditions | 40 | Text | Required |
| D | Control_Status | 30 | Text | Required |
| E | Monitoring_Enhancement | 30 | Text | Required |
| F | Transition_To | 20 | Text | Next level options |
| G | Transition_Authority | 25 | Text | Required |
| H | Documentation_Required | 30 | Text | Required |
| I | Example_Scenario | 40 | Text | Required |

### Sheet 5: Compensating_Controls

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Compensating_ID | 15 | Text | Required |
| B | Primary_Control_ID | 15 | Text | From Security_Control_Inventory |
| C | Primary_Control_Name | 30 | Text | Auto-populate |
| D | Compensating_Measure | 40 | Text | Required |
| E | Effectiveness | 15 | List | Full, Partial, Minimal |
| F | Implementation_Requirements | 40 | Text | Required |
| G | Activation_Trigger | 30 | Text | Required |
| H | Duration_Limit | 20 | Text | Required |
| I | Test_Status | 15 | List | Tested, Untested, Failed |
| J | Last_Test_Date | 15 | Date | Required if Tested |
| K | Test_Results | 40 | Text | Required if Tested |

### Sheet 6: BCDR_Security_Review

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Plan_ID | 15 | Text | Required |
| B | Plan_Name | 35 | Text | Required |
| C | Plan_Type | 20 | List | BCP, DRP, Crisis Management, IT Recovery, Other |
| D | Plan_Owner | 25 | Text | Required |
| E | Security_Section_Present | 12 | List | Yes, No, Partial |
| F | CISO_Review_Date | 15 | Date | Required |
| G | CISO_Approval_Status | 15 | List | Approved, Rejected, Pending |
| H | Gaps_Identified | 40 | Text | Optional |
| I | Remediation_Due_Date | 15 | Date | Required if gaps |
| J | Remediation_Status | 15 | List | Open, In Progress, Closed |
| K | Next_Review_Due | 15 | Date | Required |

### Sheet 7: Evidence_Register

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Evidence_ID | 15 | Text | Required |
| B | Evidence_Type | 20 | List | Document, Approval, Test Result, Configuration, Screenshot, Attestation |
| C | Description | 40 | Text | Required |
| D | Related_Section | 25 | Text | Reference to sheet/row |
| E | Collection_Date | 15 | Date | Required |
| F | Location | 40 | Text | URL/path to evidence |
| G | Collected_By | 25 | Text | Required |
| H | Valid_Until | 15 | Date | Optional |

### Sheet 8: Approval_SignOff

| Section | Content |
|---------|---------|
| Assessment Summary | Auto-calculated metrics |
| Assessment Completed By | Name, Role, Department, Email, Date |
| Reviewed By | Security Manager review and sign-off |
| Approved By | CISO approval and sign-off |

---

## 2.3 Data Validations

### Control Category Validation
```
Access Control, Data Encryption, Logging, Network Security, Backup Protection, Endpoint Security, Physical Security, Other
```

### Disruption Classification Validation
```
Non-Negotiable, Degradable, Deferrable, Not Applicable
```

### Security Posture Level Validation
```
Normal, Elevated, Degraded, Emergency, Recovery
```

### Approval Status Validation
```
Pending, Approved, Rejected
```

### Priority Validation
```
Critical, High, Medium, Low
```

---

## 2.4 Conditional Formatting

### Security_Control_Inventory Sheet

| Condition | Formatting |
|-----------|------------|
| Disruption_Classification = "Non-Negotiable" | Bold text, light blue fill |
| Disruption_Classification = "Degradable" | Yellow fill |
| Disruption_Classification = "Deferrable" | Light grey fill |
| Last_Review_Date > 365 days ago | Red text |

### BCDR_Security_Review Sheet

| Condition | Formatting |
|-----------|------------|
| CISO_Approval_Status = "Approved" | Green fill |
| CISO_Approval_Status = "Rejected" | Red fill |
| CISO_Approval_Status = "Pending" | Yellow fill |
| Remediation_Status = "Open" | Red text |
| Remediation_Status = "Closed" | Green text |

---

## 2.5 Formula Specifications

### Approval_SignOff Summary Formulas

```excel
# Total Security Controls
=COUNTA(Security_Control_Inventory!A4:A103)-COUNTBLANK(Security_Control_Inventory!B4:B103)

# Non-Negotiable Controls
=COUNTIF(Security_Control_Inventory!F4:F103,"Non-Negotiable")

# BC/DR Plans Reviewed
=COUNTIF(BCDR_Security_Review!G4:G53,"Approved")

# Open Remediation Items
=COUNTIF(BCDR_Security_Review!J4:J53,"Open")

# Compensating Controls Tested
=COUNTIF(Compensating_Controls!I4:I53,"Tested")
```

---

## 2.6 Cell Styling Standards

### Header Styling
- **Font**: Calibri 14pt Bold White
- **Fill**: Navy Blue (#003366)
- **Alignment**: Centre, Middle, Wrap Text
- **Row Height**: 30-40

### Column Header Styling
- **Font**: Calibri 10pt Bold
- **Fill**: Light Grey (#D9D9D9)
- **Alignment**: Centre, Middle, Wrap Text
- **Border**: Thin black all sides

### Input Cell Styling
- **Fill**: Light Yellow (#FFFFCC)
- **Border**: Thin black all sides
- **Alignment**: Left, Middle, Wrap Text

### Formula Cell Styling
- **Fill**: Light Green (#E2EFDA)
- **Border**: Thin black all sides

---

## 2.7 Generator Script Reference

**Script Name**: `generate_a529_1_security_controls_disruption.py`

**Location**: `10-isms-scr-base/isms-a.5.29-security-during-disruption/10_generator-master/`

**Output**: `ISMS-IMP-A.5.29.1_Security_Controls_During_Disruption_YYYYMMDD.xlsx`

**Dependencies**:
- openpyxl
- logging
- datetime

---

**END OF SPECIFICATION**

---

*"Plans are worthless, but planning is everything."*
— Dwight D. Eisenhower

<!-- QA_VERIFIED: 2026-02-06 -->
