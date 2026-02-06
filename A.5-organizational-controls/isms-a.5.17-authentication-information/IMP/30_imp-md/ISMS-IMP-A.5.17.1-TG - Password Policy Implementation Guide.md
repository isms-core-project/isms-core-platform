**ISMS-IMP-A.5.17.1-TG - Password Policy Implementation Guide**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.17: Authentication Information

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.17.1-TG |
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
| Filename | `ISMS-IMP-A.5.17.1_Password_Policy_Implementation_YYYYMMDD.xlsx` |
| Generator | `generate_a517_1_password_policy.py` |
| Sheets | 8 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 8 |
| 2 | System_Inventory | System catalogue | 200+ | 10 |
| 3 | Policy_Requirements | Requirements reference | 20 | 6 |
| 4 | Compliance_Assessment | Per-system assessment | 200+ | 15 |
| 5 | Gap_Analysis | Non-compliance findings | 50+ | 12 |
| 6 | Remediation_Tracker | Fix tracking | 50+ | 10 |
| 7 | Exception_Register | Exceptions | 20+ | 12 |
| 8 | Approval_SignOff | Authorisation | 15 | 5 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

| Row | Content | Purpose |
|-----|---------|---------|
| 1 | Title (merged A1:H1) | Document identification |
| 3-10 | Document Information table | Metadata reference |
| 12-25 | Assessment methodology | Step-by-step guidance |
| 27-40 | Password requirement reference | Quick lookup |
| 42-50 | Evidence requirements | Audit preparation |

### Sheet 2: System_Inventory

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | System_ID | 12 | Text | Required |
| B | System_Name | 30 | Text | Required |
| C | System_Type | 20 | List | Identity Provider, Enterprise App, Infrastructure, Cloud Platform, Database, Other |
| D | Criticality | 12 | List | Critical, High, Medium, Low |
| E | Auth_Method | 20 | List | Password Only, Password + MFA, Certificate, Federated |
| F | Federated | 10 | List | Yes, No, N/A |
| G | Owner | 25 | Text | None |
| H | Department | 20 | Text | None |
| I | Assessment_Status | 15 | List | Pending, In Progress, Completed, N/A |
| J | Notes | 40 | Text | None |

### Sheet 3: Policy_Requirements

| Column | Header | Width | Type | Content |
|:------:|--------|:-----:|------|---------|
| A | Requirement | 25 | Text | Pre-populated |
| B | Standard_Systems | 20 | Text | Pre-populated |
| C | Privileged_Systems | 20 | Text | Pre-populated |
| D | Service_Accounts | 20 | Text | Pre-populated |
| E | Source | 25 | Text | Policy reference |
| F | Notes | 40 | Text | Implementation guidance |

### Sheet 4: Compliance_Assessment

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | System_ID | 12 | Text | From System_Inventory |
| B | System_Name | 25 | Text | Auto-populated |
| C | Min_Length_Required | 12 | Number | From Policy |
| D | Min_Length_Actual | 12 | Number | Input |
| E | Min_Length_Compliant | 12 | Formula | Auto-calculated |
| F | Complexity_Required | 15 | Text | From Policy |
| G | Complexity_Actual | 15 | Text | Input |
| H | Complexity_Compliant | 12 | Formula | Auto-calculated |
| I | Max_Age_Required | 12 | Number | From Policy |
| J | Max_Age_Actual | 12 | Number | Input |
| K | Max_Age_Compliant | 12 | Formula | Auto-calculated |
| L | History_Required | 12 | Number | From Policy |
| M | History_Actual | 12 | Number | Input |
| N | History_Compliant | 12 | Formula | Auto-calculated |
| O | Overall_Compliant | 12 | Formula | Auto-calculated |

### Sheet 5: Gap_Analysis

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Gap_ID | 18 | Text | Auto-generated |
| B | System_ID | 12 | Text | From Assessment |
| C | System_Name | 25 | Text | Auto-populated |
| D | Requirement | 20 | Text | Which requirement |
| E | Required_Value | 15 | Text | Policy value |
| F | Actual_Value | 15 | Text | Current setting |
| G | Variance | 15 | Text | Difference |
| H | Risk_Level | 12 | List | Critical, High, Medium, Low |
| I | Identified_Date | 15 | Date | Auto-populated |
| J | Status | 15 | List | Open, Remediated, Exception |
| K | Remediation_ID | 18 | Text | Link to tracker |
| L | Notes | 40 | Text | None |

### Sheet 6: Remediation_Tracker

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Remediation_ID | 18 | Text | None |
| B | Gap_ID | 18 | Text | From Gap_Analysis |
| C | System_Name | 25 | Text | Auto-populated |
| D | Action | 50 | Text | None |
| E | Owner | 25 | Text | None |
| F | Target_Date | 15 | Date | None |
| G | Status | 15 | List | Not Started, In Progress, Completed, Blocked |
| H | Completion_Date | 15 | Date | None |
| I | Evidence_Ref | 30 | Text | None |
| J | Notes | 40 | Text | None |

### Sheet 7: Exception_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Exception_ID | 18 | Text | None |
| B | System_ID | 12 | Text | From System_Inventory |
| C | System_Name | 25 | Text | Auto-populated |
| D | Requirement | 20 | Text | Exempted requirement |
| E | Justification | 50 | Text | None |
| F | Compensating_Controls | 60 | Text | Required |
| G | Risk_Acceptance | 25 | Text | Approver name |
| H | Approval_Date | 15 | Date | None |
| I | Expiry_Date | 15 | Date | Max 6 months |
| J | Review_Frequency | 15 | List | Monthly, Quarterly |
| K | Last_Review | 15 | Date | None |
| L | Status | 12 | List | Active, Expired, Revoked |

### Sheet 8: Approval_SignOff

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Role | 25 | Text | Pre-populated |
| B | Name | 25 | Text | Input |
| C | Date | 15 | Date | Input |
| D | Signature | 20 | Text | Input |
| E | Comments | 50 | Text | Input |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| System_Inventory | D:D | ="Critical" | Red fill (#FFC7CE), Bold |
| System_Inventory | I:I | ="Pending" | Yellow fill (#FFEB9C) |
| System_Inventory | I:I | ="Completed" | Green fill (#C6EFCE) |
| Compliance_Assessment | E,H,K,N:E,H,K,N | ="No" | Red fill (#FFC7CE) |
| Compliance_Assessment | E,H,K,N:E,H,K,N | ="Yes" | Green fill (#C6EFCE) |
| Compliance_Assessment | O:O | ="Non-Compliant" | Red fill (#FFC7CE), Bold |
| Gap_Analysis | H:H | ="Critical" | Red fill (#FFC7CE), Bold |
| Gap_Analysis | H:H | ="High" | Orange fill (#FABF8F) |
| Gap_Analysis | J:J | ="Open" | Red fill (#FFC7CE) |
| Gap_Analysis | J:J | ="Remediated" | Green fill (#C6EFCE) |
| Remediation_Tracker | G:G | ="Completed" | Green fill (#C6EFCE) |
| Remediation_Tracker | G:G | ="Blocked" | Red fill (#FFC7CE) |
| Exception_Register | L:L | ="Active" | Yellow fill (#FFEB9C) |
| Exception_Register | L:L | ="Expired" | Red fill (#FFC7CE) |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| Asset Inventory (A.5.9) | System list | A.5.9 -> System_Inventory |
| IAM/IdP | Password policy config | IdP -> Evidence |
| PAM Solution | Service account inventory | PAM -> System_Inventory |
| A.5.17.2 Workbook | MFA coverage | Bidirectional |
| A.5.17.3 Workbook | Credential lifecycle | Bidirectional |
| Exception Register (ISMS-REG-EXCEPTIONS) | Approved exceptions | Bidirectional |
| GRC Platform | Compliance status | This workbook -> GRC |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.17 | Authentication Information | Parent policy |
| ISMS-IMP-A.5.17.2 | MFA Deployment Assessment | MFA coverage |
| ISMS-IMP-A.5.17.3 | Authentication Management Procedures | Credential lifecycle |
| ISMS-POL-A.8.2-3-5 | Authentication & Privileged Access | Privileged requirements |
| ISMS-IMP-A.5.9 | Asset Inventory | System source |
| ISMS-REG-EXCEPTIONS | Exception Register | Exception documentation |

---

**END OF SPECIFICATION**

---

*"The weakest link in security is almost always the human element."*
— Kevin Mitnick

<!-- QA_VERIFIED: 2026-02-06 -->
