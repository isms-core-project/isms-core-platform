**ISMS-IMP-A.5.17.3-TG - Authentication Management Procedures**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.17: Authentication Information

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.17.3-TG |
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
| Filename | `ISMS-IMP-A.5.17.3_Auth_Management_Procedures_YYYYMMDD.xlsx` |
| Generator | `generate_a517_3_auth_procedures.py` |
| Sheets | 9 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 8 |
| 2 | Procedure_Inventory | Procedure catalogue | 50+ | 10 |
| 3 | Lifecycle_Assessment | Per-phase evaluation | 30+ | 12 |
| 4 | Identity_Verification | Verification methods | 20+ | 10 |
| 5 | Communication_Security | Delivery assessment | 20+ | 8 |
| 6 | Audit_Trail_Review | Logging verification | 30+ | 10 |
| 7 | Gap_Analysis | Findings | 30+ | 12 |
| 8 | Remediation_Tracker | Actions | 30+ | 10 |
| 9 | Approval_SignOff | Authorisation | 15 | 5 |

---

## 2.2 Sheet Specifications

### Sheet 2: Procedure_Inventory

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Procedure_ID | 18 | Text | Required |
| B | Procedure_Name | 35 | Text | Required |
| C | Lifecycle_Phase | 20 | List | Initial Allocation, Ongoing Use, Password Change, Password Reset, Credential Recovery, Revocation, Shared Credentials |
| D | Account_Types | 25 | Text | None |
| E | Document_Location | 40 | Text | None |
| F | Owner | 25 | Text | None |
| G | Last_Updated | 15 | Date | None |
| H | Next_Review | 15 | Date | None |
| I | Review_Status | 15 | List | Current, Review Needed, Outdated |
| J | Notes | 40 | Text | None |

### Sheet 3: Lifecycle_Assessment

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Lifecycle_Phase | 20 | Text | Pre-populated |
| B | Requirement | 40 | Text | Pre-populated from policy |
| C | Procedure_Exists | 12 | List | Yes, No, Partial |
| D | Procedure_ID | 18 | Text | From Procedure_Inventory |
| E | Technically_Enforced | 12 | List | Yes, No, Partial |
| F | Evidence_Reviewed | 12 | List | Yes, No |
| G | Compliant | 12 | Formula | Auto-calculated |
| H | Finding_Summary | 50 | Text | None |
| I | Gap_ID | 18 | Text | If non-compliant |
| J | Evidence_Ref | 30 | Text | None |
| K | Assessor | 20 | Text | None |
| L | Assessment_Date | 15 | Date | None |

### Sheet 4: Identity_Verification

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Scenario | 30 | Text | Pre-populated |
| B | Account_Type | 20 | List | Standard, Privileged, External, Service |
| C | Required_Factors | 15 | Number | From policy |
| D | Actual_Factors | 15 | Number | Input |
| E | Methods_Used | 40 | Text | None |
| F | Prohibited_Methods | 30 | Text | None |
| G | Supervisor_Required | 12 | List | Yes, No, N/A |
| H | Compliant | 12 | Formula | Auto-calculated |
| I | Evidence_Ref | 30 | Text | None |
| J | Notes | 40 | Text | None |

### Sheet 5: Communication_Security

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Credential_Type | 25 | Text | Pre-populated |
| B | Delivery_Method | 30 | Text | Input |
| C | Encryption | 12 | List | Yes, No, N/A |
| D | Time_Limited | 12 | List | Yes, No, N/A |
| E | Forced_Change | 12 | List | Yes, No, N/A |
| F | Audit_Logged | 12 | List | Yes, No |
| G | Compliant | 12 | Formula | Auto-calculated |
| H | Notes | 40 | Text | None |

### Sheet 6: Audit_Trail_Review

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Event_Category | 25 | Text | Pre-populated |
| B | Specific_Events | 40 | Text | Pre-populated |
| C | Logged | 12 | List | Yes, No, Partial |
| D | Log_Source | 25 | Text | None |
| E | Retention_Required | 15 | Text | From policy |
| F | Retention_Actual | 15 | Text | Input |
| G | Sample_Reviewed | 12 | List | Yes, No |
| H | Compliant | 12 | Formula | Auto-calculated |
| I | Evidence_Ref | 30 | Text | None |
| J | Notes | 40 | Text | None |

### Sheet 7: Gap_Analysis

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Gap_ID | 18 | Text | None |
| B | Gap_Type | 20 | List | Missing Procedure, Inadequate Procedure, Non-Compliance, Outdated Procedure, Missing Audit Trail |
| C | Lifecycle_Phase | 20 | Text | None |
| D | Description | 50 | Text | None |
| E | Current_State | 35 | Text | None |
| F | Required_State | 35 | Text | None |
| G | Risk_Level | 12 | List | Critical, High, Medium, Low |
| H | Identified_Date | 15 | Date | None |
| I | Status | 15 | List | Open, Remediation Planned, Remediated, Accepted |
| J | Remediation_ID | 18 | Text | None |
| K | Evidence_Ref | 30 | Text | None |
| L | Notes | 40 | Text | None |

### Sheet 8: Remediation_Tracker

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Remediation_ID | 18 | Text | None |
| B | Gap_ID | 18 | Text | From Gap_Analysis |
| C | Action | 50 | Text | None |
| D | Owner | 25 | Text | None |
| E | Target_Date | 15 | Date | None |
| F | Status | 15 | List | Not Started, In Progress, Completed, Blocked |
| G | Completion_Date | 15 | Date | None |
| H | Evidence_Ref | 30 | Text | None |
| I | Verified_By | 20 | Text | None |
| J | Notes | 40 | Text | None |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Procedure_Inventory | I:I | ="Outdated" | Red fill (#FFC7CE) |
| Procedure_Inventory | I:I | ="Review Needed" | Yellow fill (#FFEB9C) |
| Lifecycle_Assessment | C:C | ="No" | Red fill (#FFC7CE) |
| Lifecycle_Assessment | G:G | ="No" | Red fill (#FFC7CE), Bold |
| Identity_Verification | H:H | ="No" | Red fill (#FFC7CE) |
| Communication_Security | G:G | ="No" | Red fill (#FFC7CE) |
| Audit_Trail_Review | C:C | ="No" | Red fill (#FFC7CE) |
| Audit_Trail_Review | H:H | ="No" | Red fill (#FFC7CE) |
| Gap_Analysis | G:G | ="Critical" | Red fill (#FFC7CE), Bold |
| Gap_Analysis | G:G | ="High" | Orange fill (#FABF8F) |
| Gap_Analysis | I:I | ="Open" | Red fill (#FFC7CE) |
| Gap_Analysis | I:I | ="Remediated" | Green fill (#C6EFCE) |
| Remediation_Tracker | F:F | ="Completed" | Green fill (#C6EFCE) |
| Remediation_Tracker | F:F | ="Blocked" | Red fill (#FFC7CE) |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| Service Desk (ITSM) | Reset/recovery tickets | ITSM -> Evidence |
| Identity Provider | Configuration, logs | IdP -> Assessment |
| HR System | Onboarding/offboarding triggers | HR -> Revocation verification |
| PAM Solution | Shared credential management | PAM -> Assessment |
| Training Platform (LMS) | Completion records | LMS -> Evidence |
| A.5.17.1 Workbook | Password configuration | Bidirectional |
| A.5.17.2 Workbook | MFA procedures | Bidirectional |
| A.6.4-5 Assessment | Employment exit integration | Reference |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.17 | Authentication Information | Parent policy |
| ISMS-IMP-A.5.17.1 | Password Policy Implementation | Technical config |
| ISMS-IMP-A.5.17.2 | MFA Deployment Assessment | MFA procedures |
| ISMS-POL-A.8.2-3-5 | Authentication & Privileged Access | Privileged procedures |
| ISMS-POL-A.6.4-5 | Employment Exit | Revocation integration |
| ISMS-IMP-A.5.15-16-18 | IAM Assessment | Access management |

---

**END OF SPECIFICATION**

---

*"A chain is only as strong as its weakest link."*
— Thomas Reid

<!-- QA_VERIFIED: 2026-02-06 -->
