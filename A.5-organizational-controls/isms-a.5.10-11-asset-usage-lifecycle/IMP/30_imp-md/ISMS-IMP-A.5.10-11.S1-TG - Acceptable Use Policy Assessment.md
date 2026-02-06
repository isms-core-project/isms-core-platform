**ISMS-IMP-A.5.10-11.S1-TG - Acceptable Use Policy Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.10: Acceptable Use of Information and Other Associated Assets

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.S1-TG |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.10: Acceptable Use of Information and Other Associated Assets |
| **Parent Policy** | ISMS-POL-A.5.10-11 Asset Usage Lifecycle Policy |
| **Related IMPs** | ISMS-IMP-A.5.10-11.S2, ISMS-IMP-A.5.10-11.S3, ISMS-IMP-A.5.10-11.S4 |
| **Version** | 1.0 |
| **Classification** | Internal Use |
| **Owner** | Information Security Manager |
| **Last Review** | [Date to be set] |
| **Framework Version** | 1.0 |
| **Assessment Type** | Policy Completeness and Effectiveness Assessment |

---

## Control Requirement

> "Rules for the acceptable use of information and other associated assets should be identified, documented and implemented."
>
> — ISO/IEC 27001:2022, Annex A Control 5.10

---

## Table of Contents

### PART I: USER COMPLETION GUIDE
1. [Assessment Overview](#1-assessment-overview)
2. [Control Requirements](#2-control-requirements)
3. [Prerequisites](#3-prerequisites)
4. [Policy Content Framework](#4-policy-content-framework)
5. [Asset Category Coverage](#5-asset-category-coverage)
6. [Workbook Structure](#6-workbook-structure)
7. [Completion Walkthrough](#7-completion-walkthrough)
8. [User Awareness and Acknowledgement](#8-user-awareness-and-acknowledgement)
9. [Communication Effectiveness](#9-communication-effectiveness)
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
| **Script Name** | `generate_a510_11_1_acceptable_use_policy.py` |
| **Script Location** | `10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/10_generator-master/` |
| **Output Location** | `10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/90_workbooks/` |
| **Output Filename** | `ISMS-IMP-A.5.10-11.S1_Acceptable_Use_Policy_Assessment_YYYYMMDD.xlsx` |

### 15.2 Technical Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    WORKBOOK ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    HEADER STRUCTURE                       │   │
│  │  Row 1: Title Bar (merged A1:K1)                         │   │
│  │  Row 2: Control Reference                                 │   │
│  │  Row 3: Assessment Period                                 │   │
│  │  Row 4: Generated Date                                    │   │
│  │  Row 5: Empty (separator)                                 │   │
│  │  Row 6: Column Headers                                    │   │
│  │  Row 7+: Data Rows                                        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │Instruc-  │ │Policy_   │ │Asset_    │ │Awareness_│          │
│  │tions     │ │Assessment│ │Coverage  │ │Tracking  │          │
│  │ Sheet 1  │ │ Sheet 2  │ │ Sheet 3  │ │ Sheet 4  │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                        │
│  │Communic- │ │Evidence_ │ │Approval_ │                        │
│  │ation     │ │Register  │ │SignOff   │                        │
│  │ Sheet 5  │ │ Sheet 6  │ │ Sheet 7  │                        │
│  └──────────┘ └──────────┘ └──────────┘                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 16. Sheet Specifications

### Sheet 1: Instructions

**Purpose:** Assessment guidance and metadata

**Structure:**
- Merged header row with document title
- Metadata table (assessment date, assessor, organisation)
- Quick reference guide for completion
- Colour legend for status indicators

### Sheet 2: Policy_Assessment

**Purpose:** Evaluate AUP content completeness

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Requirement_ID | 15 | Text | Auto-generated (REQ-001) |
| B | Policy_Requirement | 45 | Text | Pre-populated requirement |
| C | Category | 20 | Text | Requirement category |
| D | Addressed | 14 | List | Yes/Partial/No/N/A |
| E | Policy_Section | 20 | Text | AUP section reference |
| F | Clarity_Rating | 16 | List | Clear/Needs Improvement/Unclear |
| G | Last_Updated | 16 | Date | When requirement was last reviewed |
| H | Owner | 22 | Text | Requirement owner |
| I | Gap_Status | 16 | List | Compliant/Gap Identified/Remediation In Progress |
| J | Remediation_Notes | 35 | Text | Required improvements |
| K | Evidence_Ref | 18 | Text | Evidence reference |

**Pre-populated Requirements (20 items):**
1. Policy scope defines applicable assets
2. Policy defines acceptable business use
3. Policy explicitly prohibits unauthorized activities
4. Personal use guidelines are documented
5. Monitoring and logging disclosure included
6. Consequences of violation are stated
7. Exception request process documented
8. Intellectual property rules defined
9. Data classification handling requirements
10. Mobile device acceptable use rules
11. Remote working asset use guidelines
12. Cloud service usage rules
13. Social media usage guidelines
14. Email and messaging acceptable use
15. Internet usage guidelines
16. Password and authentication requirements
17. Physical asset protection responsibilities
18. Incident reporting obligations
19. Third-party access provisions
20. Policy acknowledgement requirement

### Sheet 3: Asset_Coverage

**Purpose:** Verify all asset categories have defined usage rules

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Asset_Category | 25 | Text | Pre-populated categories |
| B | Asset_Examples | 40 | Text | Example assets in category |
| C | Covered_In_AUP | 16 | List | Yes/Partial/No |
| D | Policy_Section | 20 | Text | AUP section reference |
| E | Usage_Rules_Defined | 18 | List | Yes/No/N/A |
| F | Handling_Rules_Defined | 18 | List | Yes/No/N/A |
| G | Gap_Notes | 35 | Text | Coverage gaps identified |
| H | Remediation_Required | 18 | List | Yes/No |
| I | Evidence_Ref | 18 | Text | Evidence reference |

**Pre-populated Categories (12 items):**
- Information Assets, Software Assets, Hardware Assets
- Network Assets, Cloud Services, Communication Tools
- Physical Media, Authentication Assets, Development Environments
- Monitoring Systems, Personal Devices (BYOD), IoT Devices

### Sheet 4: Awareness_Tracking

**Purpose:** Track user AUP acknowledgement status

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Department | 22 | Text | Department name |
| B | Total_Users | 14 | Number | Total users in department |
| C | Acknowledged | 14 | Number | Users who acknowledged |
| D | Pending | 14 | Number | Formula: =B-C |
| E | Acknowledgment_% | 16 | Percent | Formula: =C/B*100 |
| F | Last_Campaign_Date | 18 | Date | Last acknowledgement campaign |
| G | Next_Due_Date | 16 | Date | Next renewal due |
| H | Campaign_Method | 22 | List | Email/LMS/Intranet/In-Person/Onboarding |
| I | Escalation_Status | 18 | List | None Required/Reminder Sent/Manager Notified/HR Escalation |
| J | Notes | 35 | Text | Additional notes |

**Summary Row:** TOTAL row with SUM formulas for columns B, C, D and AVERAGE for column E

### Sheet 5: Communication_Matrix

**Purpose:** Assess policy communication effectiveness

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Communication_Channel | 28 | Text | Pre-populated channels |
| B | Audience | 25 | Text | Target audience |
| C | Frequency | 18 | List | Daily/Weekly/Monthly/Quarterly/Annual/Per hire/As needed |
| D | Last_Communication | 18 | Date | Last use date |
| E | Next_Scheduled | 18 | Date | Next planned use |
| F | Effectiveness_Rating | 18 | List | Highly Effective/Effective/Needs Improvement/Ineffective |
| G | Owner | 22 | Text | Channel owner |
| H | Improvement_Actions | 35 | Text | Actions to improve effectiveness |
| I | Evidence_Ref | 18 | Text | Evidence reference |

**Pre-populated Channels:**
- Onboarding Process, Intranet/SharePoint, Annual Training
- Email Announcements, Team Meetings, Security Newsletter
- Posters/Digital Signage

### Sheet 6: Evidence_Register

**Purpose:** Link supporting audit evidence

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Evidence_ID | 15 | Text | Auto-generated (EV-001) |
| B | Evidence_Type | 22 | List | Policy Document/Acknowledgment Record/Training Record/etc. |
| C | Description | 45 | Text | Evidence description |
| D | Related_Requirement | 25 | Text | Requirement(s) supported |
| E | Collection_Date | 16 | Date | When collected |
| F | Location | 40 | Text | Storage location (URL or path) |
| G | Collected_By | 25 | Text | Person who collected |
| H | Valid_Until | 16 | Date | Expiration date |

### Sheet 7: Approval_SignOff

**Purpose:** Assessment approval and sign-off

**Structure:**
- Summary metrics section (auto-calculated)
- Assessor completion section
- ISM review section
- CISO approval section

**Summary Formulas:**
- Total Requirements Assessed: `=COUNTA(Policy_Assessment!A7:A26)`
- Requirements Addressed: `=COUNTIF(Policy_Assessment!D7:D26,"Yes")`
- Partial Coverage: `=COUNTIF(Policy_Assessment!D7:D26,"Partial")`
- Gaps Identified: `=COUNTIF(Policy_Assessment!D7:D26,"No")`
- Compliance Score: `=(COUNTIF(D7:D26,"Yes")+0.5*COUNTIF(D7:D26,"Partial"))/COUNTA(A7:A26)*100`
- Overall Acknowledgement: Reference to Awareness_Tracking total

---

## 17. Data Validation Rules

### 17.1 Dropdown Lists

| Field | Valid Values |
|-------|--------------|
| **Addressed** | Yes, Partial, No, N/A |
| **Clarity_Rating** | Clear, Needs Improvement, Unclear |
| **Gap_Status** | Compliant, Gap Identified, Remediation In Progress |
| **Covered_In_AUP** | Yes, Partial, No |
| **Usage/Handling Defined** | Yes, No, N/A |
| **Remediation_Required** | Yes, No |
| **Campaign_Method** | Email, LMS, Intranet, In-Person, Onboarding |
| **Escalation_Status** | None Required, Reminder Sent, Manager Notified, HR Escalation |
| **Frequency** | Daily, Weekly, Monthly, Quarterly, Annual, Per hire, As needed, Always available |
| **Effectiveness_Rating** | Highly Effective, Effective, Needs Improvement, Ineffective |
| **Evidence_Type** | Policy Document, Acknowledgment Record, Training Record, Screenshot, Export, Attestation, Email, Meeting Minutes |
| **Approval_Decision** | Approved, Approved with conditions, Rejected |

### 17.2 Numeric Constraints

| Field | Constraint |
|-------|------------|
| Total_Users | ≥0, whole number |
| Acknowledged | ≥0, ≤Total_Users |
| Dates | Valid date format (DD.MM.YYYY) |

---

## 18. Conditional Formatting

### 18.1 Policy_Assessment Sheet

| Range | Condition | Format |
|-------|-----------|--------|
| Column D (Addressed) | "Yes" | Green fill (#90EE90) |
| Column D (Addressed) | "Partial" | Yellow fill (#FFFF00) |
| Column D (Addressed) | "No" | Red fill (#FF6B6B) |
| Column D (Addressed) | "N/A" | Grey fill (#D3D3D3) |
| Column I (Gap_Status) | "Gap Identified" | Red fill (#FF6B6B) |

### 18.2 Asset_Coverage Sheet

| Range | Condition | Format |
|-------|-----------|--------|
| Column C (Covered) | "Yes" | Green fill |
| Column C (Covered) | "Partial" | Yellow fill |
| Column C (Covered) | "No" | Red fill |
| Column H (Remediation) | "Yes" | Red fill |

### 18.3 Awareness_Tracking Sheet

| Range | Condition | Format |
|-------|-----------|--------|
| Column E (%) | ≥95% | Green fill |
| Column E (%) | 80-94% | Yellow fill |
| Column E (%) | <80% | Red fill |
| Column I (Escalation) | "HR Escalation" | Red fill |

---

## 19. Formula Specifications

### 19.1 Awareness Tracking Formulas

**Pending Users (Column D):**
```excel
=B7-C7
```

**Acknowledgement Percentage (Column E):**
```excel
=IF(B7>0,C7/B7*100,0)
```

**Total Row:**
```excel
=SUM(B7:B20)  // Total Users
=SUM(C7:C20)  // Acknowledged
=SUM(D7:D20)  // Pending
=AVERAGE(E7:E20)  // Average %
```

### 19.2 Summary Metrics (Approval Sheet)

**Compliance Score:**
```excel
=(COUNTIF(Policy_Assessment!D7:D26,"Yes")+0.5*COUNTIF(Policy_Assessment!D7:D26,"Partial"))/COUNTA(Policy_Assessment!A7:A26)*100
```

**Asset Coverage Rate:**
```excel
=COUNTIF(Asset_Coverage!C7:C18,"Yes")/COUNTA(Asset_Coverage!A7:A18)*100
```

---

## 20. Cell Styling Standards

### 20.1 Colour Palette

| Element | Colour | Hex Code | Usage |
|---------|--------|----------|-------|
| Header Background | Navy Blue | #003366 | Title rows, headers |
| Header Text | White | #FFFFFF | Header text |
| Input Cells | Light Yellow | #FFFFCC | User input fields |
| Compliant/Yes | Green | #90EE90 | Positive status |
| Partial | Yellow | #FFFF00 | Partial compliance |
| Gap/No | Red | #FF6B6B | Non-compliance |
| N/A | Grey | #D3D3D3 | Not applicable |
| Border | Grey | #D0D0D0 | Cell borders |

### 20.2 Font Standards

| Element | Font | Size | Style |
|---------|------|:----:|-------|
| Title | Calibri | 14 | Bold |
| Column Headers | Calibri | 11 | Bold |
| Data Cells | Calibri | 10 | Regular |
| Notes | Calibri | 9 | Italic |

---

## 21. Generator Script Reference

### 21.1 Script Structure

```python
# =============================================================================
# ISMS-IMP-A.5.10-11.S1 - Acceptable Use Policy Assessment Generator
# =============================================================================
# ISO 27001:2022 Control A.5.10: Acceptable Use of Information and Assets
# Generates assessment workbook for AUP completeness and effectiveness
# =============================================================================

# Document Metadata
DOCUMENT_ID = "ISMS-IMP-A.5.10-11.S1"
WORKBOOK_NAME = "Acceptable Use Policy Assessment"
CONTROL_ID = "A.5.10"
CONTROL_NAME = "Acceptable Use of Information and Other Associated Assets"

# Output Configuration
OUTPUT_FILENAME = f"{DOCUMENT_ID}_Acceptable_Use_Policy_Assessment_{GENERATED_TIMESTAMP}.xlsx"
```

### 21.2 Key Functions

| Function | Purpose |
|----------|---------|
| `create_workbook()` | Initialise workbook with standard structure |
| `create_instructions_sheet()` | Generate Instructions sheet |
| `create_policy_assessment_sheet()` | Generate Policy_Assessment with requirements |
| `create_asset_coverage_sheet()` | Generate Asset_Coverage with categories |
| `create_awareness_tracking_sheet()` | Generate Awareness_Tracking with formulas |
| `create_communication_matrix_sheet()` | Generate Communication_Matrix |
| `create_evidence_register_sheet()` | Generate Evidence_Register |
| `create_approval_sheet()` | Generate Approval_SignOff with summaries |
| `apply_data_validation()` | Add dropdown lists |
| `apply_conditional_formatting()` | Apply status-based formatting |
| `style_workbook()` | Apply consistent styling |

### 21.3 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| openpyxl | ≥3.0.0 | Excel workbook generation |
| datetime | stdlib | Date handling |
| logging | stdlib | Execution logging |

### 21.4 Execution

```bash
cd 10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/10_generator-master/
python3 generate_a510_11_1_acceptable_use_policy.py
mv ISMS-IMP-A.5.10-11.S1_*.xlsx ../90_workbooks/
```

### 21.5 Output Verification

After generation, verify:
- [ ] All 7 sheets created
- [ ] Headers styled correctly
- [ ] Pre-populated requirements present
- [ ] Data validation dropdowns functional
- [ ] Conditional formatting applied
- [ ] Formulas calculate correctly
- [ ] Column widths appropriate

---

**END OF SPECIFICATION**

---

*"Security is not a product, but a process."*
— Bruce Schneier

<!-- QA_VERIFIED: 2026-02-06 -->
