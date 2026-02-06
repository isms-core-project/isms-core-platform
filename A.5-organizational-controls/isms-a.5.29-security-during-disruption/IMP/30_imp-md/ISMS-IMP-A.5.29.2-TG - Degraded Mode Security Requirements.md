**ISMS-IMP-A.5.29.2-TG - Degraded Mode Security Requirements**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.29

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.29.2-TG |
| **Title** | Degraded Mode Security Requirements |
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
   - [1.4 Degradation Scenarios](#14-degradation-scenarios)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 Break-Glass Procedures](#17-break-glass-procedures)
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
ISMS-IMP-A.5.29.2_Degraded_Mode_Security_Requirements_YYYYMMDD.xlsx
```

### Sheet Tab Order

1. Instructions
2. Degradation_Scenarios
3. BreakGlass_Accounts
4. BreakGlass_Activation
5. Elevated_Monitoring
6. Personnel_Availability
7. Security_Debt_Register
8. Evidence_Register
9. Approval_SignOff

---

## 2.2 Sheet Specifications

### Sheet 2: Degradation_Scenarios

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Scenario_ID | 15 | Text | Required |
| B | Scenario_Name | 30 | Text | Required |
| C | Trigger_Condition | 40 | Text | Required |
| D | Control_Affected | 25 | Text | Required |
| E | Degradation_Type | 20 | List | Temporary Bypass, Reduced Capability, Postponed, Alternative Method |
| F | Compensating_Control | 40 | Text | Required |
| G | Max_Duration | 20 | Text | Required |
| H | Renewal_Process | 30 | Text | Required |
| I | Authorisation_Required | 25 | Text | Required |
| J | Posture_Level | 15 | List | Elevated, Degraded, Emergency |
| K | Never_Acceptable | 40 | Text | Required |

### Sheet 3: BreakGlass_Accounts

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Account_ID | 15 | Text | Required |
| B | Account_Name | 25 | Text | Required |
| C | Account_Type | 20 | List | Domain Admin, System Admin, Database Admin, Network Admin, Application Admin, Other |
| D | Target_Systems | 35 | Text | Required |
| E | Scope_Permissions | 35 | Text | Required |
| F | Credential_Location | 30 | Text | Required |
| G | Activation_Authority | 25 | Text | Required |
| H | Two_Person_Required | 10 | List | Yes, No |
| I | Default_Duration | 15 | Text | Required |
| J | Logging_Enabled | 10 | List | Yes, No, Verified |
| K | Last_Rotation_Date | 15 | Date | Required |
| L | Last_Test_Date | 15 | Date | Required |
| M | Status | 12 | List | Disabled, Enabled, Unknown |

### Sheet 4: BreakGlass_Activation

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Activation_ID | 15 | Text | Required |
| B | Account_ID | 15 | Text | From BreakGlass_Accounts |
| C | Emergency_Type | 25 | Text | Required |
| D | Activation_DateTime | 20 | DateTime | Required |
| E | Authorised_By | 25 | Text | Required |
| F | Activated_By | 25 | Text | Required |
| G | Second_Person | 25 | Text | If two-person required |
| H | CISO_Notified | 10 | List | Yes, No |
| I | Expiry_DateTime | 20 | DateTime | Required |
| J | Renewed | 10 | List | Yes, No |
| K | Deactivation_DateTime | 20 | DateTime | Required |
| L | Post_Review_Completed | 10 | List | Yes, No |
| M | Issues_Found | 40 | Text | Optional |

### Sheet 5: Elevated_Monitoring

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Posture_Level | 15 | List | Elevated, Degraded, Emergency |
| B | Monitoring_Area | 25 | Text | Required |
| C | Normal_Frequency | 20 | Text | Required |
| D | Enhanced_Frequency | 20 | Text | Required |
| E | Alert_Threshold_Change | 30 | Text | Required |
| F | Manual_Review_Required | 10 | List | Yes, No |
| G | Review_Frequency | 20 | Text | If manual review |
| H | Responsible_Party | 25 | Text | Required |
| I | Implementation_Notes | 40 | Text | Optional |

### Sheet 6: Personnel_Availability

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Role_ID | 15 | Text | Required |
| B | Role_Name | 30 | Text | Required |
| C | Primary_Name | 25 | Text | Required |
| D | Primary_Phone | 20 | Text | Required |
| E | Primary_Email | 30 | Text | Required |
| F | Backup1_Name | 25 | Text | Required |
| G | Backup1_Phone | 20 | Text | Required |
| H | Backup1_Email | 30 | Text | Required |
| I | Backup2_Name | 25 | Text | Required |
| J | Backup2_Phone | 20 | Text | Required |
| K | Backup2_Email | 30 | Text | Required |
| L | Cross_Training_Status | 15 | List | Complete, Partial, None |
| M | Last_Contact_Test | 15 | Date | Required |
| N | Last_Drill_Date | 15 | Date | Required |

### Sheet 7: Security_Debt_Register

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Debt_ID | 15 | Text | Required |
| B | Debt_Type | 20 | List | Deferred Patch, Skipped Review, Delayed Scan, Config Exception, Access Exception, Other |
| C | Description | 40 | Text | Required |
| D | Disruption_Reference | 20 | Text | Optional |
| E | Created_Date | 15 | Date | Required |
| F | Owner | 25 | Text | Required |
| G | Remediation_Plan | 40 | Text | Required |
| H | Target_Date | 15 | Date | Required |
| I | Status | 15 | List | Open, In Progress, Closed |
| J | Age_Days | 10 | Formula | =TODAY()-E |
| K | Escalation_Required | 10 | Formula | =IF(J>30,"Yes","No") |
| L | Escalated_To | 25 | Text | If escalation required |
| M | Escalation_Date | 15 | Date | If escalated |
| N | Closure_Date | 15 | Date | If closed |
| O | Closure_Evidence | 30 | Text | If closed |

---

## 2.3 Data Validations

### Degradation Type Validation
```
Temporary Bypass, Reduced Capability, Postponed, Alternative Method
```

### Account Type Validation
```
Domain Admin, System Admin, Database Admin, Network Admin, Application Admin, Other
```

### Debt Type Validation
```
Deferred Patch, Skipped Review, Delayed Scan, Config Exception, Access Exception, Other
```

### Cross-Training Status Validation
```
Complete, Partial, None
```

---

## 2.4 Conditional Formatting

### BreakGlass_Accounts Sheet

| Condition | Formatting |
|-----------|------------|
| Status = "Enabled" | Red fill (should normally be disabled) |
| Last_Test_Date > 365 days ago | Yellow fill |
| Logging_Enabled != "Verified" | Orange text |

### Security_Debt_Register Sheet

| Condition | Formatting |
|-----------|------------|
| Age_Days > 90 | Red fill |
| Age_Days > 30 | Yellow fill |
| Status = "Closed" | Green fill |
| Escalation_Required = "Yes" | Bold red text |

---

## 2.5 Formula Specifications

### Security_Debt_Register Formulas

```excel
# Age Days
=IF(E4<>"",TODAY()-E4,"")

# Escalation Required
=IF(J4>30,"Yes","No")

# Executive Escalation Required (>90 days)
=IF(J4>90,"Executive","")
```

### Approval_SignOff Summary Formulas

```excel
# Total Break-Glass Accounts
=COUNTA(BreakGlass_Accounts!A4:A103)-COUNTBLANK(BreakGlass_Accounts!B4:B103)

# Accounts Tested This Year
=COUNTIF(BreakGlass_Accounts!L4:L103,">=" & DATE(YEAR(TODAY()),1,1))

# Open Security Debt Items
=COUNTIF(Security_Debt_Register!I4:I103,"Open")

# Overdue Security Debt (>30 days)
=COUNTIF(Security_Debt_Register!K4:K103,"Yes")
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

### Warning Cell Styling
- **Fill**: Light Red (#FFC7CE)
- **Font**: Bold

---

## 2.7 Generator Script Reference

**Script Name**: `generate_a529_2_degraded_mode.py`

**Location**: `10-isms-scr-base/isms-a.5.29-security-during-disruption/10_generator-master/`

**Output**: `ISMS-IMP-A.5.29.2_Degraded_Mode_Security_Requirements_YYYYMMDD.xlsx`

**Dependencies**:
- openpyxl
- logging
- datetime

---

**END OF SPECIFICATION**

---

*"In preparing for battle I have always found that plans are useless, but planning is indispensable."*
— Dwight D. Eisenhower

<!-- QA_VERIFIED: 2026-02-06 -->
