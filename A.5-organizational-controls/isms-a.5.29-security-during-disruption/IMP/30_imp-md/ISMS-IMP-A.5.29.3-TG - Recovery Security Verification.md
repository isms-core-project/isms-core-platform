**ISMS-IMP-A.5.29.3-TG - Recovery Security Verification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.29

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.29.3-TG |
| **Title** | Recovery Security Verification |
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
   - [1.4 Recovery Phases](#14-recovery-phases)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 Security Validation Activities](#17-security-validation-activities)
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
ISMS-IMP-A.5.29.3_Recovery_Security_Verification_YYYYMMDD.xlsx
```

### Sheet Tab Order

1. Instructions
2. Recovery_Checklist
3. Emergency_Access_Closure
4. Control_Validation
5. Anomaly_Detection
6. Security_Debt_Closure
7. Lessons_Learned
8. Evidence_Register
9. Approval_SignOff

---

## 2.2 Sheet Specifications

### Sheet 2: Recovery_Checklist

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Checklist_ID | 12 | Text | Required |
| B | Phase | 15 | List | Immediate, Short-term, Medium-term, Long-term |
| C | Activity | 40 | Text | Required |
| D | Responsible_Party | 25 | Text | Required |
| E | Target_Completion | 20 | Text | Required |
| F | Status | 12 | List | Not Started, In Progress, Complete, N/A |
| G | Completion_Date | 15 | Date | If Complete |
| H | Completed_By | 25 | Text | If Complete |
| I | Evidence_Reference | 20 | Text | If Complete |
| J | Notes | 40 | Text | Optional |

### Sheet 3: Emergency_Access_Closure

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Account_ID | 15 | Text | From ISMS-IMP-A.5.29.2 |
| B | Account_Name | 25 | Text | Required |
| C | Activation_Date | 15 | Date | Required |
| D | Deactivation_Date | 15 | Date | Required |
| E | Deactivated_By | 25 | Text | Required |
| F | Credential_Rotated | 10 | List | Yes, No |
| G | Rotation_Date | 15 | Date | If rotated |
| H | Usage_Reviewed | 10 | List | Yes, No |
| I | Review_Date | 15 | Date | If reviewed |
| J | Anomalies_Found | 10 | List | Yes, No |
| K | Anomaly_Details | 40 | Text | If anomalies found |
| L | CISO_Notified | 10 | List | Yes, No |
| M | Verification_Status | 12 | List | Pending, Verified |

### Sheet 4: Control_Validation

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Control_ID | 15 | Text | From ISMS-IMP-A.5.29.1 |
| B | Control_Name | 30 | Text | Required |
| C | Category | 20 | Text | Required |
| D | Pre_Disruption_Status | 15 | Text | Required |
| E | Current_Status | 15 | List | Operational, Partial, Not Operational |
| F | Validation_Method | 25 | Text | Required |
| G | Validation_Date | 15 | Date | Required |
| H | Validated_By | 25 | Text | Required |
| I | Gaps_Identified | 40 | Text | If not operational |
| J | Remediation_Required | 10 | List | Yes, No |
| K | Remediation_Date | 15 | Date | If required |
| L | Remediation_Status | 12 | List | Open, Closed |

### Sheet 5: Anomaly_Detection

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Anomaly_ID | 12 | Text | Required |
| B | Detection_Source | 25 | List | SIEM, Log Review, User Report, Automated Alert, Manual Analysis |
| C | Detection_Date | 15 | Date | Required |
| D | Anomaly_Type | 25 | List | Authentication, Access, Network, Data, Configuration, Other |
| E | Description | 50 | Text | Required |
| F | Severity | 12 | List | Critical, High, Medium, Low, Informational |
| G | Related_Timeframe | 25 | Text | During disruption period |
| H | Investigation_Status | 15 | List | Open, Investigating, Closed - False Positive, Closed - Confirmed |
| I | Investigator | 25 | Text | Required |
| J | Findings | 50 | Text | Investigation results |
| K | Actions_Taken | 40 | Text | Remediation actions |
| L | Escalated | 10 | List | Yes, No |
| M | Escalated_To | 25 | Text | If escalated |

### Sheet 6: Security_Debt_Closure

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Debt_ID | 15 | Text | From ISMS-IMP-A.5.29.2 |
| B | Debt_Type | 20 | Text | Required |
| C | Description | 40 | Text | Required |
| D | Created_Date | 15 | Date | Required |
| E | Original_Target | 15 | Date | Required |
| F | Remediation_Action | 40 | Text | Required |
| G | Action_Date | 15 | Date | Required |
| H | Action_By | 25 | Text | Required |
| I | Verification_Method | 30 | Text | Required |
| J | Verification_Date | 15 | Date | Required |
| K | Verified_By | 25 | Text | Required |
| L | Closure_Status | 12 | List | Pending, Verified, Closed |
| M | Evidence_Reference | 20 | Text | If Closed |

### Sheet 7: Lessons_Learned

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Finding_ID | 12 | Text | Required |
| B | Category | 20 | List | Planning, Controls, Personnel, Communication, Tools, Process, Other |
| C | Finding_Description | 50 | Text | Required |
| D | Impact | 40 | Text | Required |
| E | Root_Cause | 40 | Text | Required |
| F | Recommendation | 50 | Text | Required |
| G | Action_Type | 20 | List | Policy Update, Procedure Update, Training, Tool Enhancement, Process Change |
| H | Action_Owner | 25 | Text | Required |
| I | Target_Date | 15 | Date | Required |
| J | Status | 12 | List | Open, In Progress, Closed |
| K | Completion_Date | 15 | Date | If Closed |
| L | Evidence_Reference | 20 | Text | If Closed |

---

## 2.3 Data Validations

### Phase Validation
```
Immediate, Short-term, Medium-term, Long-term
```

### Status Validation
```
Not Started, In Progress, Complete, N/A
```

### Anomaly Type Validation
```
Authentication, Access, Network, Data, Configuration, Other
```

### Investigation Status Validation
```
Open, Investigating, Closed - False Positive, Closed - Confirmed
```

### Action Type Validation
```
Policy Update, Procedure Update, Training, Tool Enhancement, Process Change
```

---

## 2.4 Conditional Formatting

### Recovery_Checklist Sheet

| Condition | Formatting |
|-----------|------------|
| Phase = "Immediate" and Status != "Complete" | Red fill |
| Status = "Complete" | Green fill |
| Status = "In Progress" | Yellow fill |

### Anomaly_Detection Sheet

| Condition | Formatting |
|-----------|------------|
| Severity = "Critical" | Bold red text |
| Severity = "High" | Bold orange text |
| Investigation_Status = "Closed - Confirmed" | Red fill |
| Investigation_Status = "Closed - False Positive" | Grey fill |

### Security_Debt_Closure Sheet

| Condition | Formatting |
|-----------|------------|
| Closure_Status = "Closed" | Green fill |
| Closure_Status = "Pending" | Yellow fill |

---

## 2.5 Formula Specifications

### Approval_SignOff Summary Formulas

```excel
# Immediate Phase Completion
=COUNTIF(Recovery_Checklist!B:B,"Immediate")-COUNTIF(Recovery_Checklist!F:F,"Complete")

# All Controls Validated
=COUNTIF(Control_Validation!E4:E103,"Operational")

# Open Anomalies
=COUNTIF(Anomaly_Detection!H4:H103,"Open")+COUNTIF(Anomaly_Detection!H4:H103,"Investigating")

# Security Debt Closed
=COUNTIF(Security_Debt_Closure!L4:L53,"Closed")

# Lessons Learned Actions Open
=COUNTIF(Lessons_Learned!J4:J53,"Open")+COUNTIF(Lessons_Learned!J4:J53,"In Progress")
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

### Completion Cell Styling
- **Fill**: Light Green (#C6EFCE)
- **Border**: Thin black all sides

---

## 2.7 Generator Script Reference

**Script Name**: `generate_a529_3_recovery_verification.py`

**Location**: `10-isms-scr-base/isms-a.5.29-security-during-disruption/10_generator-master/`

**Output**: `ISMS-IMP-A.5.29.3_Recovery_Security_Verification_YYYYMMDD.xlsx`

**Dependencies**:
- openpyxl
- logging
- datetime

---

**END OF SPECIFICATION**

---

*"Security is not a product, but a process."*
— Bruce Schneier

<!-- QA_VERIFIED: 2026-02-06 -->
