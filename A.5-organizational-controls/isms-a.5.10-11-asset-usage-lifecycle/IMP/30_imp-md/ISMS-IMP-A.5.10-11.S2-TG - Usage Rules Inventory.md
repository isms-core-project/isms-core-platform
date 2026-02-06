**ISMS-IMP-A.5.10-11.S2-TG - Usage Rules Inventory**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.10: Acceptable Use of Information and Other Associated Assets

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.S2-TG |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.10: Acceptable Use of Information and Other Associated Assets |
| **Parent Policy** | ISMS-POL-A.5.10-11 Asset Usage Lifecycle Policy |
| **Related IMPs** | ISMS-IMP-A.5.10-11.S1, ISMS-IMP-A.5.10-11.S3, ISMS-IMP-A.5.10-11.S4 |
| **Version** | 1.0 |
| **Classification** | Internal Use |
| **Owner** | Information Security Manager |
| **Last Review** | [Date to be set] |
| **Framework Version** | 1.0 |
| **Assessment Type** | Usage Rules Documentation and Inventory |

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
4. [Rule Classification Framework](#4-rule-classification-framework)
5. [Asset Category Rules](#5-asset-category-rules)
6. [Workbook Structure](#6-workbook-structure)
7. [Completion Walkthrough](#7-completion-walkthrough)
8. [Handling Requirements by Classification](#8-handling-requirements-by-classification)
9. [Enforcement and Monitoring](#9-enforcement-and-monitoring)
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
| **Script Name** | `generate_a510_11_2_usage_rules_inventory.py` |
| **Script Location** | `10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/10_generator-master/` |
| **Output Location** | `10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/90_workbooks/` |
| **Output Filename** | `ISMS-IMP-A.5.10-11.S2_Usage_Rules_Inventory_YYYYMMDD.xlsx` |

### 15.2 Technical Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    WORKBOOK ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │Instruc-  │ │Usage_    │ │Permitted_│ │Prohibited│          │
│  │tions     │ │Rules     │ │Activities│ │Activities│          │
│  │ Sheet 1  │ │ Sheet 2  │ │ Sheet 3  │ │ Sheet 4  │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                        │
│  │Handling_ │ │Evidence_ │ │Approval_ │                        │
│  │Requiremts│ │Register  │ │SignOff   │                        │
│  │ Sheet 5  │ │ Sheet 6  │ │ Sheet 7  │                        │
│  └──────────┘ └──────────┘ └──────────┘                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 16. Sheet Specifications

### Sheet 1: Instructions

**Purpose:** Document guidance and metadata

**Structure:**
- Title header with document ID
- Metadata table (date, author, organisation)
- Completion guidance
- Colour legend for classifications

### Sheet 2: Usage_Rules

**Purpose:** Master inventory of all usage rules

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Rule_ID | 14 | Text | UR-001, UR-002, etc. |
| B | Asset_Category | 25 | List | Asset category dropdown |
| C | Rule_Description | 50 | Text | Clear rule statement |
| D | Classification | 20 | List | Permitted/Permitted with Conditions/Prohibited |
| E | Applies_To | 22 | Text | ALL/EMP/CON/TMP/3P/PRV |
| F | Enforcement_Method | 22 | Text | How compliance verified |
| G | Monitoring_Required | 16 | List | Yes/No |
| H | Exception_Process | 18 | Text | Exception request method |
| I | Policy_Reference | 20 | Text | AUP section reference |
| J | Last_Updated | 14 | Date | Last review date |
| K | Owner | 22 | Text | Rule owner |
| L | Notes | 30 | Text | Additional notes |

**Pre-populated Rules (15 items):**
- Laptop full-disk encryption required
- VPN required for remote access
- Password sharing prohibited
- Confidential data encryption in transit
- Personal device connection restrictions
- Software installation approval required
- Email usage for business communications
- Personal use limits during breaks
- USB storage device restrictions
- Cloud service approval requirements
- Social media guidelines
- Mobile device security requirements
- Network resource usage limits
- Physical asset care requirements
- Incident reporting obligations

### Sheet 3: Permitted_Activities

**Purpose:** Document allowed activities with conditions

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Activity_ID | 14 | Text | PA-001, PA-002, etc. |
| B | Asset_Category | 22 | List | Asset category |
| C | Permitted_Activity | 45 | Text | What is allowed |
| D | Conditions | 35 | Text | Restrictions or requirements |
| E | Approval_Required | 16 | List | Yes/No |
| F | Approver_Role | 22 | Text | Who approves |
| G | Time_Restrictions | 20 | Text | When allowed |
| H | Location_Restrictions | 22 | Text | Where allowed |
| I | Documentation_Required | 20 | List | Yes/No |
| J | Notes | 30 | Text | Additional notes |

### Sheet 4: Prohibited_Activities

**Purpose:** Document forbidden actions with consequences

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Prohibition_ID | 14 | Text | PH-001, PH-002, etc. |
| B | Asset_Category | 22 | List | Asset category |
| C | Prohibited_Activity | 45 | Text | What is forbidden |
| D | Reason | 35 | Text | Why prohibited (risk basis) |
| E | Risk_Level | 14 | List | Critical/High/Medium/Low |
| F | Detection_Method | 25 | Text | How violation detected |
| G | Consequence | 25 | Text | What happens if violated |
| H | Exception_Possible | 16 | List | Yes/No |
| I | Related_Control | 18 | Text | ISO control reference |
| J | Notes | 30 | Text | Additional notes |

**Pre-populated Prohibitions (8 items):**
- Sharing login credentials (Critical)
- Bypassing security controls (Critical)
- Connecting unauthorised devices (High)
- Sending restricted data externally (Critical)
- Installing unapproved software (Medium)
- Using personal email for business (High)
- Disabling security software (Critical)
- Storing data on personal devices (High)

### Sheet 5: Handling_Requirements

**Purpose:** Asset handling by classification

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Handling_ID | 14 | Text | HR-001, HR-002, etc. |
| B | Asset_Category | 22 | List | Asset category |
| C | Data_Classification | 18 | List | Public/Internal/Confidential/Restricted |
| D | Storage_Requirement | 30 | Text | Where/how to store |
| E | Transmission_Requirement | 30 | Text | How to transmit |
| F | Disposal_Requirement | 30 | Text | How to dispose |
| G | Access_Restriction | 25 | Text | Who can access |
| H | Labelling_Required | 16 | List | Yes/No/N/A |
| I | Encryption_Required | 16 | List | Yes/No/N/A |
| J | Retention_Period | 18 | Text | How long to keep |
| K | Notes | 30 | Text | Additional notes |

### Sheet 6: Evidence_Register

**Purpose:** Link supporting evidence

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Evidence_ID | 15 | Text | EV-001, etc. |
| B | Evidence_Type | 22 | List | Dropdown |
| C | Description | 45 | Text | Description |
| D | Related_Rules | 25 | Text | Rule IDs supported |
| E | Collection_Date | 16 | Date | When collected |
| F | Location | 40 | Text | Storage path |
| G | Collected_By | 25 | Text | Person |
| H | Valid_Until | 16 | Date | Expiration |

### Sheet 7: Approval_SignOff

**Purpose:** Inventory approval

**Structure:**
- Summary metrics
- Author completion section
- Stakeholder review sections
- CISO approval section

---

## 17. Data Validation Rules

### 17.1 Dropdown Lists

| Field | Valid Values |
|-------|--------------|
| **Asset_Category** | Information Assets, Software Assets, Hardware Assets, Network Assets, Cloud Services, Communication Tools, Physical Media, Authentication Assets, Development Assets, Personal Devices, IoT Devices |
| **Classification** | Permitted, Permitted with Conditions, Prohibited, Not Applicable |
| **Risk_Level** | Critical, High, Medium, Low |
| **Data_Classification** | Public, Internal, Confidential, Restricted |
| **Yes/No** | Yes, No |
| **Evidence_Type** | Policy Document, Legal Review, Technical Configuration, Sign-off Record, Exception Record |

---

## 18. Conditional Formatting

### 18.1 Usage_Rules Sheet

| Range | Condition | Format |
|-------|-----------|--------|
| Column D (Classification) | "Permitted" | Green fill |
| Column D (Classification) | "Permitted with Conditions" | Yellow fill |
| Column D (Classification) | "Prohibited" | Red fill |

### 18.2 Prohibited_Activities Sheet

| Range | Condition | Format |
|-------|-----------|--------|
| Column E (Risk_Level) | "Critical" | Red fill, white bold text |
| Column E (Risk_Level) | "High" | Orange fill |
| Column E (Risk_Level) | "Medium" | Yellow fill |
| Column E (Risk_Level) | "Low" | Green fill |

### 18.3 Handling_Requirements Sheet

| Range | Condition | Format |
|-------|-----------|--------|
| Column C (Classification) | "Restricted" | Red fill |
| Column C (Classification) | "Confidential" | Orange fill |
| Column C (Classification) | "Internal" | Yellow fill |
| Column C (Classification) | "Public" | Green fill |

---

## 19. Formula Specifications

### 19.1 Summary Counts (Approval Sheet)

**Total Rules:**
```excel
=COUNTA(Usage_Rules!A7:A100)
```

**Prohibited Count:**
```excel
=COUNTIF(Usage_Rules!D7:D100,"Prohibited")
```

**Critical Prohibitions:**
```excel
=COUNTIF(Prohibited_Activities!E7:E50,"Critical")
```

---

## 20. Cell Styling Standards

### 20.1 Colour Palette

| Element | Colour | Hex Code | Usage |
|---------|--------|----------|-------|
| Header | Navy Blue | #003366 | Headers |
| Permitted | Green | #90EE90 | Permitted status |
| Conditional | Yellow | #FFFF00 | Permitted with conditions |
| Prohibited | Red | #FF6B6B | Prohibited status |
| Critical | Dark Red | #8B0000 | Critical risk |
| Border | Grey | #D0D0D0 | Cell borders |

### 20.2 Font Standards

| Element | Font | Size | Style |
|---------|------|:----:|-------|
| Title | Calibri | 14 | Bold |
| Headers | Calibri | 11 | Bold |
| Data | Calibri | 10 | Regular |

---

## 21. Generator Script Reference

### 21.1 Script Structure

```python
# =============================================================================
# ISMS-IMP-A.5.10-11.S2 - Usage Rules Inventory Generator
# =============================================================================
# ISO 27001:2022 Control A.5.10: Acceptable Use of Information and Assets
# Generates comprehensive usage rules inventory workbook
# =============================================================================

DOCUMENT_ID = "ISMS-IMP-A.5.10-11.S2"
WORKBOOK_NAME = "Usage Rules Inventory"
CONTROL_ID = "A.5.10"

OUTPUT_FILENAME = f"{DOCUMENT_ID}_Usage_Rules_Inventory_{GENERATED_TIMESTAMP}.xlsx"
```

### 21.2 Execution

```bash
cd 10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/10_generator-master/
python3 generate_a510_11_2_usage_rules_inventory.py
mv ISMS-IMP-A.5.10-11.S2_*.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"The best security policy is the one that people actually follow."*
— Unknown

<!-- QA_VERIFIED: 2026-02-06 -->
