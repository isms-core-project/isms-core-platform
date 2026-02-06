**ISMS-IMP-A.6.3.1-TG - Training Needs Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.3: Information Security Awareness, Education and Training

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.3.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Training Needs Analysis and Audience Classification |
| **Related Policy** | ISMS-POL-A.6.3, Section 2.2 (Training Audience Classification) |
| **Purpose** | Assess training needs by role classification, identify training gaps, and determine appropriate training requirements for all personnel |
| **Target Audience** | HR Training Coordinators, Information Security Officers, Department Managers, Compliance Officers, Auditors |
| **Assessment Type** | Process & Organizational Assessment |
| **Review Cycle** | Annual (minimum) + upon significant organizational changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Initial | Initial specification for Training Needs Assessment workbook | ISMS Implementation Team |

---

# Technical Specification
**Audience:** Generator Script Developers

---

# Excel Workbook Technical Specification

## Workbook Metadata

```python
DOCUMENT_ID = "ISMS-IMP-A.6.3.1"
WORKBOOK_NAME = "Training Needs Assessment"
CONTROL_ID = "A.6.3"
CONTROL_NAME = "Information Security Awareness, Education and Training"
```

## Sheet Specifications

### Sheet 1: Instructions

**Purpose:** User guidance and assessment overview

**Content Sections:**
1. Assessment Purpose
2. Scope and Applicability
3. Completion Workflow
4. Key Definitions
5. Support Contacts

**Formatting:**
- Header: Bold, centered, larger font
- Sections: Clear headings with explanatory text
- Workflow: Numbered steps with descriptions
- Freeze top row

### Sheet 2: Role_Inventory

**Column Specification:**

| Column | Header | Width | Type | Validation | Required |
|--------|--------|-------|------|------------|----------|
| A | Role_ID | 12 | Text | Unique, format "XXX-000" | Yes |
| B | Role_Title | 30 | Text | None | Yes |
| C | Department | 20 | Text | None | Yes |
| D | Employment_Type | 15 | Dropdown | Employee, Contractor, Temp, Third-Party | Yes |
| E | Personnel_Count | 12 | Integer | ≥1 | Yes |
| F | Role_Description | 50 | Text | None | Yes |
| G | Primary_Systems | 40 | Text | None | Yes |
| H | Highest_Data_Classification | 15 | Dropdown | Public, Internal, Confidential, Restricted | Yes |
| I | External_Facing | 10 | Dropdown | Yes, No | Yes |
| J | Technical_Role | 10 | Dropdown | Yes, No | Yes |
| K | Management_Role | 10 | Dropdown | Yes, No | Yes |
| L | Notes | 40 | Text | None | No |

**Formatting:**
- Header row: Bold, frozen, filter-enabled
- Alternating row colors
- Data validation dropdowns where specified
- Conditional formatting: Restricted data = orange highlight

### Sheet 3: Tier_Classification

**Column Specification:**

| Column | Header | Width | Type | Validation | Required |
|--------|--------|-------|------|------------|----------|
| A | Role_ID | 12 | Reference | Must match Role_Inventory | Yes |
| B | Role_Title | 30 | Lookup | =VLOOKUP(A,Role_Inventory,2) | Auto |
| C | System_Access_Score | 18 | Integer | 1-5 | Yes |
| D | Data_Handling_Score | 18 | Integer | 1-5 | Yes |
| E | Technical_Depth_Score | 18 | Integer | 1-5 | Yes |
| F | External_Exposure_Score | 20 | Integer | 1-5 | Yes |
| G | Regulatory_Scope_Score | 18 | Integer | 1-5 | Yes |
| H | Total_Score | 12 | Formula | =SUM(C:G) | Auto |
| I | Assigned_Tier | 12 | Formula/Override | Tier 1-7 | Yes |
| J | Classification_Justification | 50 | Text | None | Yes |
| K | Approved_By | 25 | Text | None | Yes |
| L | Approval_Date | 12 | Date | None | Yes |

**Tier Assignment Formula (Column I):**
```excel
=IF(AND(Management_Role="Yes",H>=12),"Tier 7",
  IF(H<=7,"Tier 1",
    IF(H<=11,"Tier 2",
      IF(H<=15,"Tier 3",
        IF(H<=19,"Tier 4",
          IF(H<=22,"Tier 5","Tier 6"))))))
```

**Scoring Criteria (embedded in sheet or separate reference):**

### Sheet 4: Training_Requirements

**Column Specification:**

| Column | Header | Width | Type | Required |
|--------|--------|-------|------|----------|
| A | Tier | 10 | Dropdown | Yes |
| B | Training_Topic | 40 | Text | Yes |
| C | Topic_Category | 20 | Dropdown | Yes |
| D | Mandatory | 10 | Dropdown | Yes |
| E | Frequency | 15 | Dropdown | Yes |
| F | Delivery_Requirement | 20 | Dropdown | Yes |
| G | Assessment_Required | 15 | Dropdown | Yes |
| H | Regulatory_Driver | 30 | Text | No |
| I | Policy_Reference | 25 | Text | Yes |
| J | Notes | 40 | Text | No |

**Dropdown Values:**

- Tier: Tier 1, Tier 2, Tier 3, Tier 4, Tier 5, Tier 6, Tier 7
- Topic_Category: Baseline Awareness, Data Protection, Technical Security, Privileged Access, Specialized, Governance
- Mandatory: Yes, No
- Frequency: Onboarding, Annual, Bi-Annual, Quarterly, As Needed, Upon Change
- Delivery_Requirement: Any, eLearning, Instructor-Led, Workshop, Simulation
- Assessment_Required: Yes, No

**Pre-populated Data (from POL-A.6.3 Sections 2.3-2.4):**

[Include 40-60 rows of pre-populated training requirements mapped to tiers]

### Sheet 5: Gap_Analysis

**Column Specification:**

| Column | Header | Width | Type | Required |
|--------|--------|-------|------|----------|
| A | Role_ID | 12 | Reference | Yes |
| B | Role_Title | 30 | Lookup | Auto |
| C | Assigned_Tier | 12 | Lookup | Auto |
| D | Training_Topic | 40 | Reference | Yes |
| E | Required_By | 15 | Lookup | Auto |
| F | Current_Status | 15 | Dropdown | Yes |
| G | Gap_Description | 50 | Text | If gap |
| H | Priority | 10 | Dropdown | Yes |
| I | Remediation_Action | 50 | Text | If gap |
| J | Target_Date | 12 | Date | If gap |
| K | Owner | 25 | Text | If gap |
| L | Status_Update | 30 | Text | No |

**Dropdown Values:**

- Current_Status: Completed, Partial, Not Started, Not Available
- Priority: Critical, High, Medium, Low

**Conditional Formatting:**
- Not Started + Critical: Red fill
- Not Started + High: Orange fill
- Partial: Yellow fill
- Completed: Green fill

### Sheet 6: Evidence_Register

**Column Specification:**

| Column | Header | Width | Type | Required |
|--------|--------|-------|------|----------|
| A | Evidence_ID | 12 | Text | Yes |
| B | Category | 20 | Dropdown | Yes |
| C | Description | 50 | Text | Yes |
| D | Source | 30 | Text | Yes |
| E | Date_Obtained | 12 | Date | Yes |
| F | Location_Reference | 40 | Text | Yes |
| G | Retention_Period | 15 | Text | No |
| H | Notes | 40 | Text | No |

**Dropdown Values:**

- Category: Organizational Data, System Access, Training Records, Policy Documents, Approvals, Other

### Sheet 7: Dashboard

**Metrics to Display:**

**Summary Section:**
- Assessment Date
- Assessor Name
- Review Period
- Next Review Date

**Role Metrics:**
- Total Roles Assessed
- Total Personnel Covered
- Roles by Tier (pie chart)
- Personnel by Tier (bar chart)

**Gap Metrics:**
- Total Gaps Identified
- Gaps by Priority (Critical/High/Medium/Low)
- Gap by Tier (heatmap)
- Remediation Progress (% complete)

**Compliance Score:**
- Formula: (Completed Requirements / Total Requirements) × 100
- Target: ≥90%

### Sheet 8: Approval_Sign_Off

**Layout:**

```
ASSESSMENT APPROVAL RECORD

Assessment Details:
- Document ID: ISMS-IMP-A.6.3.1
- Assessment Period: [Date Range]
- Total Roles Assessed: [Auto from Dashboard]
- Total Gaps Identified: [Auto from Dashboard]

Approval Chain:

1. Assessor
   Name: _______________
   Title: _______________
   Date: _______________
   Signature: _______________

2. HR Director
   Name: _______________
   Title: _______________
   Date: _______________
   Signature: _______________

3. Information Security Officer
   Name: _______________
   Title: _______________
   Date: _______________
   Signature: _______________

4. CISO (Final Approval)
   Name: _______________
   Title: _______________
   Date: _______________
   Signature: _______________

Approval Notes:
[Free text area]
```

---

## Generator Script Requirements

### Required Libraries

```python
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.chart import PieChart, BarChart, Reference
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule, ColorScaleRule
from datetime import datetime
import logging
```

### Generator Script Pattern

Follow standardized generator pattern per ISMS-Control-Implementation-Instructions v3.0:

```python
# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.6.3.1"
WORKBOOK_NAME = "Training_Needs_Assessment"
CONTROL_ID = "A.6.3"
CONTROL_NAME = "Information Security Awareness, Education and Training"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")

OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME}_{GENERATED_TIMESTAMP}.xlsx"
```

### Pre-populated Training Requirements Data

Include reference data for Sheet 4 (Training_Requirements) based on POL-A.6.3:

```python
TRAINING_REQUIREMENTS = [
    # Tier 1 - All Personnel
    ("Tier 1", "Information Security Policy Overview", "Baseline Awareness", "Yes", "Onboarding", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.3.1"),
    ("Tier 1", "Acceptable Use Policy", "Baseline Awareness", "Yes", "Annual", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.3.2"),
    ("Tier 1", "Data Classification and Handling", "Baseline Awareness", "Yes", "Annual", "Any", "Yes", "GDPR Art.32", "POL-A.6.3 §2.3.3"),
    ("Tier 1", "Password and Authentication Security", "Baseline Awareness", "Yes", "Annual", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.3.4"),
    ("Tier 1", "Phishing and Social Engineering Awareness", "Baseline Awareness", "Yes", "Annual", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.3.5"),
    ("Tier 1", "Security Incident Reporting", "Baseline Awareness", "Yes", "Onboarding", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.3.6"),
    ("Tier 1", "Physical Security Awareness", "Baseline Awareness", "Yes", "Annual", "Any", "No", "ISO 27001", "POL-A.6.3 §2.3.7"),
    ("Tier 1", "Remote Working Security", "Baseline Awareness", "Yes", "Annual", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.3.8"),

    # Tier 3 - Data Handlers (includes Tier 1-2)
    ("Tier 3", "Privacy and Data Protection (GDPR/nDSG)", "Data Protection", "Yes", "Annual", "Any", "Yes", "GDPR Art.29", "POL-A.6.3 §2.4.1"),
    ("Tier 3", "Data Subject Rights", "Data Protection", "Yes", "Annual", "Any", "Yes", "GDPR", "POL-A.6.3 §2.4.1"),
    ("Tier 3", "Data Retention and Deletion", "Data Protection", "Yes", "Annual", "Any", "No", "GDPR Art.17", "POL-A.6.3 §2.4.1"),
    ("Tier 3", "Cross-Border Data Transfer", "Data Protection", "Yes", "Annual", "Any", "No", "GDPR Ch.V", "POL-A.6.3 §2.4.1"),

    # Tier 4 - Technical Staff
    ("Tier 4", "Secure Coding Practices", "Technical Security", "Yes", "Annual", "Any", "Yes", "OWASP", "POL-A.6.3 §2.4.2"),
    ("Tier 4", "OWASP Top 10", "Technical Security", "Yes", "Annual", "Any", "Yes", "OWASP", "POL-A.6.3 §2.4.2"),
    ("Tier 4", "Secure Configuration Management", "Technical Security", "Yes", "Annual", "Any", "No", "CIS", "POL-A.6.3 §2.4.2"),
    ("Tier 4", "Vulnerability Management", "Technical Security", "Yes", "Annual", "Any", "No", "ISO 27001", "POL-A.6.3 §2.4.2"),

    # Tier 5 - Privileged Users
    ("Tier 5", "Privileged Access Management", "Privileged Access", "Yes", "Annual", "Instructor-Led", "Yes", "ISO 27001", "POL-A.6.3 §2.4.3"),
    ("Tier 5", "Incident Response Procedures", "Privileged Access", "Yes", "Annual", "Workshop", "Yes", "ISO 27001", "POL-A.6.3 §2.4.3"),
    ("Tier 5", "Insider Threat Awareness", "Privileged Access", "Yes", "Annual", "Any", "No", "ISO 27001", "POL-A.6.3 §2.4.3"),

    # Tier 6 - Security Roles
    ("Tier 6", "Risk Assessment and Management", "Specialized", "Yes", "Annual", "Any", "Yes", "ISO 27005", "POL-A.6.3 §2.4.4"),
    ("Tier 6", "Security Operations", "Specialized", "Yes", "Annual", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.4.4"),
    ("Tier 6", "Incident Response and Forensics", "Specialized", "Yes", "Annual", "Workshop", "Yes", "ISO 27001", "POL-A.6.3 §2.4.4"),
    ("Tier 6", "Security Architecture", "Specialized", "Yes", "Annual", "Any", "No", "TOGAF", "POL-A.6.3 §2.4.4"),

    # Tier 7 - Management
    ("Tier 7", "Information Security Governance", "Governance", "Yes", "Annual", "Any", "No", "ISO 27001", "POL-A.6.3 §2.4.5"),
    ("Tier 7", "Risk Management for Executives", "Governance", "Yes", "Annual", "Any", "No", "ISO 31000", "POL-A.6.3 §2.4.5"),
    ("Tier 7", "Incident Management - Executive Role", "Governance", "Yes", "Annual", "Any", "No", "ISO 27001", "POL-A.6.3 §2.4.5"),
]
```

---

## Validation Rules Summary

| Sheet | Validation | Rule |
|-------|------------|------|
| Role_Inventory | Role_ID | Unique, non-empty |
| Role_Inventory | Personnel_Count | Integer ≥ 1 |
| Role_Inventory | Data_Classification | Dropdown only |
| Tier_Classification | Scores | Integer 1-5 |
| Tier_Classification | Assigned_Tier | Must match calculated or justified |
| Gap_Analysis | Current_Status | Dropdown only |
| Gap_Analysis | Remediation fields | Required if gap exists |
| Evidence_Register | Evidence_ID | Unique, non-empty |
| Approval_Sign_Off | All fields | Required for final approval |

---

## QA Checklist

Before generating workbook:

- [ ] All 8 sheets created with correct names
- [ ] Column widths set per specification
- [ ] Data validation dropdowns functional
- [ ] Formulas calculate correctly
- [ ] Conditional formatting applied
- [ ] Header rows frozen
- [ ] Filters enabled on data sheets
- [ ] Dashboard charts render correctly
- [ ] Pre-populated data included (Training_Requirements)
- [ ] Document control metadata accurate
- [ ] Print areas defined for approval sheet

---

# Document Control

**Document ID:** ISMS-IMP-A.6.3.1
**Version:** 1.0
**Classification:** Internal
**Status:** Draft

**Review and Approval:**

| Role | Responsibility |
|------|----------------|
| **Document Owner** | CISO |
| **Technical Review** | Information Security Officer |
| **Business Review** | HR Director |
| **Approval Authority** | CISO |

---

**END OF SPECIFICATION**

---

*"An equation for me has no meaning unless it expresses a thought of God."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
