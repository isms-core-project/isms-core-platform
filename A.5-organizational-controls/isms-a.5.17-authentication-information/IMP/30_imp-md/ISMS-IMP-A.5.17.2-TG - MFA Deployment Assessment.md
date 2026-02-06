**ISMS-IMP-A.5.17.2-TG - MFA Deployment Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.17: Authentication Information

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.17.2-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.17 Authentication Information |
| **Parent Policy** | ISMS-POL-A.5.17 - Authentication Information |
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
| Filename | `ISMS-IMP-A.5.17.2_MFA_Deployment_Assessment_YYYYMMDD.xlsx` |
| Generator | `generate_a517_2_mfa_deployment.py` |
| Sheets | 9 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 8 |
| 2 | System_MFA_Inventory | System MFA status | 200+ | 12 |
| 3 | User_Enrollment | User MFA status | 1000+ | 10 |
| 4 | Method_Analysis | MFA method distribution | 20 | 8 |
| 5 | Conditional_Access | IdP policies | 30+ | 10 |
| 6 | Gap_Analysis | Coverage gaps | 50+ | 10 |
| 7 | Remediation_Tracker | Fix tracking | 50+ | 10 |
| 8 | Exception_Register | Exceptions | 20+ | 12 |
| 9 | Approval_SignOff | Authorisation | 15 | 5 |

---

## 2.2 Sheet Specifications

### Sheet 2: System_MFA_Inventory

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | System_ID | 12 | Text | Required |
| B | System_Name | 30 | Text | Required |
| C | Access_Category | 20 | List | Privileged Access, Remote Access, CONFIDENTIAL, Internet-Facing, Standard Internal |
| D | MFA_Requirement | 15 | List | Required, Risk-Based, Not Required |
| E | MFA_Enabled | 10 | List | Yes, No, Partial |
| F | MFA_Method | 25 | Text | None |
| G | Enforcement | 20 | List | Conditional Access, Application Native, Manual, None |
| H | Compliant | 10 | Formula | Auto-calculated |
| I | Owner | 25 | Text | None |
| J | Last_Assessed | 15 | Date | None |
| K | Evidence_Ref | 25 | Text | None |
| L | Notes | 40 | Text | None |

### Sheet 3: User_Enrollment

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | User_ID | 30 | Text | Required |
| B | Display_Name | 25 | Text | None |
| C | Department | 20 | Text | None |
| D | Role_Category | 20 | List | Administrator, Privileged User, Standard User, External User |
| E | MFA_Required | 10 | List | Yes, No |
| F | Enrollment_Status | 20 | List | Enrolled - Active, Enrolled - Inactive, Not Enrolled - Required, Not Enrolled - Exempt |
| G | Method_Registered | 25 | Text | None |
| H | Last_MFA_Used | 15 | Date | None |
| I | Compliant | 10 | Formula | Auto-calculated |
| J | Notes | 40 | Text | None |

### Sheet 4: Method_Analysis

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | MFA_Method | 25 | Text | Pre-populated |
| B | Approval_Status | 20 | List | Approved - Preferred, Approved, Approved (with controls), Not Approved (legacy), Prohibited |
| C | User_Count | 12 | Number | Input |
| D | Percentage | 12 | Formula | Auto-calculated |
| E | Phishing_Resistant | 10 | List | Yes, No |
| F | Migration_Required | 10 | List | Yes, No |
| G | Migration_Deadline | 15 | Date | None |
| H | Notes | 40 | Text | None |

### Sheet 5: Conditional_Access

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Policy_ID | 15 | Text | None |
| B | Policy_Name | 35 | Text | None |
| C | Status | 12 | List | Enabled, Report-Only, Disabled |
| D | Scope_Users | 30 | Text | None |
| E | Scope_Apps | 30 | Text | None |
| F | Conditions | 30 | Text | None |
| G | MFA_Requirement | 20 | List | Require MFA, Require Compliant Device, Block, Allow |
| H | Last_Modified | 15 | Date | None |
| I | Evidence_Ref | 25 | Text | None |
| J | Notes | 40 | Text | None |

### Sheet 6: Gap_Analysis

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Gap_ID | 18 | Text | None |
| B | Gap_Type | 15 | List | System Gap, User Gap, Method Gap, Policy Gap, Enforcement Gap |
| C | System_ID | 12 | Text | None |
| D | User_ID | 30 | Text | None |
| E | Description | 50 | Text | None |
| F | Risk_Level | 12 | List | Critical, High, Medium, Low |
| G | Identified_Date | 15 | Date | None |
| H | Status | 15 | List | Open, Remediation Planned, Remediated, Exception |
| I | Remediation_ID | 18 | Text | None |
| J | Notes | 40 | Text | None |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| System_MFA_Inventory | D:D | ="Required" | Bold |
| System_MFA_Inventory | E:E | ="No" | Red fill (#FFC7CE) |
| System_MFA_Inventory | H:H | ="No" | Red fill (#FFC7CE), Bold |
| User_Enrollment | F:F | ="Not Enrolled - Required" | Red fill (#FFC7CE) |
| User_Enrollment | I:I | ="No" | Red fill (#FFC7CE) |
| Method_Analysis | B:B | ="Not Approved (legacy)" | Orange fill (#FABF8F) |
| Method_Analysis | B:B | ="Prohibited" | Red fill (#FFC7CE), Bold |
| Conditional_Access | C:C | ="Disabled" | Red fill (#FFC7CE) |
| Conditional_Access | C:C | ="Report-Only" | Yellow fill (#FFEB9C) |
| Gap_Analysis | F:F | ="Critical" | Red fill (#FFC7CE), Bold |
| Gap_Analysis | H:H | ="Open" | Red fill (#FFC7CE) |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| Azure AD / Entra ID | Enrollment reports, CA policies | IdP -> This workbook |
| Okta | Factor enrollment, policies | IdP -> This workbook |
| Asset Inventory (A.5.9) | System list | A.5.9 -> System_MFA_Inventory |
| A.5.17.1 Workbook | Password compliance | Bidirectional |
| A.5.17.3 Workbook | Credential lifecycle | Bidirectional |
| PAM Solution | Privileged account MFA | PAM -> User_Enrollment |
| SIEM | MFA bypass monitoring | SIEM -> Evidence |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.17 | Authentication Information | Parent policy |
| ISMS-IMP-A.5.17.1 | Password Policy Implementation | Password controls |
| ISMS-IMP-A.5.17.3 | Authentication Management Procedures | Credential lifecycle |
| ISMS-POL-A.8.2-3-5 | Authentication & Privileged Access | Privileged MFA |
| ISMS-IMP-A.5.15-16-18 | IAM Assessment | Identity management |

---

**END OF SPECIFICATION**

---

*"There are only two types of companies: those that have been hacked, and those that will be."*
— Robert Mueller

<!-- QA_VERIFIED: 2026-02-06 -->
