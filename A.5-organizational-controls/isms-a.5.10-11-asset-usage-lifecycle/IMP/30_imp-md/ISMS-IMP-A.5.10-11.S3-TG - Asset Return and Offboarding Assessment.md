**ISMS-IMP-A.5.10-11.S3-TG - Asset Return and Offboarding Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.11

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.S3-TG |
| **Title** | Asset Return and Offboarding Assessment |
| **Control Reference** | ISO/IEC 27001:2022 A.5.11 |
| **Control Name** | Return of Assets |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

## Table of Contents

**PART I: USER COMPLETION GUIDE**
1. [Assessment Overview](#assessment-overview)
2. [Control Requirement](#control-requirement)
3. [Prerequisites](#prerequisites)
4. [Key Terminology](#key-terminology)
5. [Return Process Framework](#return-process-framework)
6. [Asset Return Requirements](#asset-return-requirements)
7. [Workbook Structure](#workbook-structure)
8. [Completion Walkthrough](#completion-walkthrough)
9. [Access Revocation Framework](#access-revocation-framework)
10. [Offboarding Scenarios](#offboarding-scenarios)
11. [Evidence Collection](#evidence-collection)
12. [Common Pitfalls](#common-pitfalls)
13. [Quality Checklist](#quality-checklist)
14. [Review & Approval](#review-approval)

**PART II: TECHNICAL SPECIFICATION**
1. [Workbook Architecture](#workbook-architecture)
2. [Sheet Specifications](#sheet-specifications)
3. [Data Validations](#data-validations)
4. [Conditional Formatting Rules](#conditional-formatting-rules)
5. [Formula Specifications](#formula-specifications)
6. [Generator Reference](#generator-reference)

---

# Technical Specification

### Workbook Architecture

**File Details**

| Attribute | Value |
|-----------|-------|
| Filename | `ISMS-IMP-A.5.10-11.S3_Asset_Return_and_Offboarding_Assessment_YYYYMMDD.xlsx` |
| Format | Microsoft Excel (.xlsx) |
| Total Sheets | 7 |
| Target Rows | Process: 18; Assets: 22; Offboarding: 50+; Revocation: 200+ |

**Sheet Overview**

| Sheet Name | Purpose | Row Count |
|------------|---------|-----------|
| Instructions | Guidance and metadata | 35 |
| Return_Process | Process requirements assessment | 18 requirements |
| Asset_Checklist | Asset return definitions | 22 asset types |
| Offboarding_Tracking | Individual departure tracking | Dynamic (50+ recommended) |
| Access_Revocation | Access removal records | Dynamic (5+ per offboarding) |
| Evidence_Register | Evidence documentation | Dynamic |
| Approval_SignOff | Assessment approvals | 10 |

### Sheet Specifications

#### Instructions Sheet

**Metadata Section (Rows 1-20)**

| Row | Content |
|-----|---------|
| 1 | Document title (merged A1:F1) |
| 3-15 | Metadata table (Field/Value pairs) |
| 17-20 | Instructions text |

**Metadata Fields**

| Field | Cell | Content |
|-------|------|---------|
| Assessment Title | B3 | Asset Return and Offboarding Assessment |
| Document ID | B4 | ISMS-IMP-A.5.10-11.S3 |
| Control Reference | B5 | A.5.11 |
| Assessment Period Start | B6 | Date (user input) |
| Assessment Period End | B7 | Date (user input) |
| Assessor Name | B8 | Text (user input) |
| Department | B9 | Text (user input) |
| Review Date | B10 | Date (user input) |
| Version | B11 | 1.0 |

#### Return_Process Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Requirement_ID | 14 | Pre-populated (PR-001 to PR-018) |
| B | Process_Requirement | 45 | Pre-populated requirements |
| C | Category | 22 | Pre-populated categories |
| D | Implemented | 14 | Data validation: Yes/Partial/No |
| E | Documented | 14 | Data validation: Yes/No |
| F | Responsible_Role | 22 | User input |
| G | SLA_Days | 12 | User input (numeric) |
| H | Automated | 14 | Data validation: Yes/No |
| I | Gap_Status | 16 | Data validation |
| J | Remediation_Notes | 35 | User input |
| K | Evidence_Ref | 18 | Evidence reference |

**Pre-populated Requirements (18)**

| ID | Requirement | Category |
|----|-------------|----------|
| PR-001 | Formal offboarding procedure documented | Documentation |
| PR-002 | HR-to-IT notification process defined | Notification |
| PR-003 | Notification SLA established (24 hours) | Notification |
| PR-004 | Asset inventory linked to personnel records | Asset Tracking |
| PR-005 | Asset list generated upon notification | Asset Tracking |
| PR-006 | Return checklist defined per asset type | Asset Return |
| PR-007 | Physical asset collection process | Asset Return |
| PR-008 | Remote worker return shipping process | Asset Return |
| PR-009 | Network access revocation procedure | Access Revocation |
| PR-010 | Application access revocation procedure | Access Revocation |
| PR-011 | Physical access revocation procedure | Access Revocation |
| PR-012 | Access revocation SLA (end of LWD) | Access Revocation |
| PR-013 | Data wipe procedure for returned devices | Data Security |
| PR-014 | Data wipe verification and certification | Data Security |
| PR-015 | Knowledge transfer requirements defined | Knowledge Transfer |
| PR-016 | Return completion sign-off process | Verification |
| PR-017 | Escalation process for incomplete returns | Escalation |
| PR-018 | Exception documentation requirements | Documentation |

**Summary Row (Row 21)**

- Compliance Score: `=SUMPRODUCT((D2:D19="Yes")*1+(D2:D19="Partial")*0.5)/18*100`
- Documentation Score: `=COUNTIF(E2:E19,"Yes")/COUNTA(E2:E19)*100`

#### Asset_Checklist Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Asset_Type | 25 | Pre-populated types |
| B | Description | 40 | Pre-populated descriptions |
| C | Category | 18 | Pre-populated categories |
| D | Return_Required | 16 | Data validation: Yes/No/Optional |
| E | Verification_Method | 25 | User input |
| F | Responsible_Team | 20 | User input |
| G | SLA_Days | 12 | User input (numeric) |
| H | Data_Wipe_Required | 16 | Data validation: Yes/No/N/A |
| I | Disposal_If_Not_Returned | 25 | User input |
| J | Notes | 30 | User input |

**Pre-populated Asset Types (22)**

| Category | Asset Types |
|----------|-------------|
| Hardware | Laptop, Desktop, Monitor, Keyboard/Mouse, Tablet |
| Mobile | Mobile Phone, Smartphone, SIM Card |
| Storage | USB Drive, External HDD, SD Card |
| Authentication | Smart Card, Hardware Token, Security Key |
| Physical Access | Access Badge, Keys, Parking Pass |
| Documents | Confidential Documents, Company Manuals, Training Materials |
| Other | Company Credit Card, Fuel Card, Company Vehicle |

#### Offboarding_Tracking Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Offboard_ID | 14 | Auto-generated (OFF-001) |
| B | Employee_Name | 25 | User input |
| C | Employee_ID | 14 | User input |
| D | Department | 20 | User input |
| E | Employee_Type | 16 | Data validation |
| F | Manager | 22 | User input |
| G | Last_Working_Day | 16 | Date field |
| H | Offboard_Reason | 18 | Data validation |
| I | Notice_Date | 14 | Date field |
| J | Assets_Assigned | 14 | User input (numeric) |
| K | Assets_Returned | 14 | User input (numeric) |
| L | Return_Status | 16 | Data validation |
| M | Access_Revoked | 14 | Data validation |
| N | Data_Wiped | 14 | Data validation |
| O | Knowledge_Transfer | 16 | Data validation |
| P | Sign_Off_Date | 14 | Date field |
| Q | HR_Confirmed | 14 | Data validation |
| R | Notes | 30 | User input |

**Summary Metrics (Bottom section)**

| Metric | Formula |
|--------|---------|
| Total Offboardings | `=COUNTA(A2:A[last])` |
| Complete Returns | `=COUNTIF(L:L,"Complete")` |
| Overdue Returns | `=COUNTIF(L:L,"Overdue")` |
| Completion Rate | `=Complete/Total*100` |

#### Access_Revocation Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Revocation_ID | 14 | Auto-generated (REV-001) |
| B | Employee_Ref | 14 | Link to Offboarding_Tracking |
| C | Employee_Name | 22 | User input |
| D | Access_Type | 18 | Data validation |
| E | System_Application | 28 | User input |
| F | Access_Level | 16 | User input |
| G | Last_Working_Day | 16 | Date field |
| H | Target_Revocation | 16 | Date field |
| I | Revocation_Date | 16 | Date field |
| J | SLA_Met | 12 | Formula: Yes/No |
| K | Revoked_By | 20 | User input |
| L | Verification_Method | 22 | Data validation |
| M | Verified_By | 20 | User input |
| N | Verification_Date | 16 | Date field |
| O | Notes | 30 | User input |

**SLA_Met Formula**

```
=IF(I2="","",IF(I2<=H2,"Yes","No"))
```

**Summary Metrics**

| Metric | Formula |
|--------|---------|
| Total Revocations | `=COUNTA(A2:A[last])` |
| SLA Met | `=COUNTIF(J:J,"Yes")` |
| SLA Missed | `=COUNTIF(J:J,"No")` |
| SLA Compliance % | `=SLA Met/Total*100` |

#### Evidence_Register Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Evidence_ID | 14 | Auto-generated (EVD-001) |
| B | Evidence_Type | 18 | Data validation |
| C | Description | 40 | User input |
| D | Related_Requirement | 16 | Link to Return_Process |
| E | Related_Offboard | 16 | Link to Offboarding_Tracking |
| F | File_Reference | 30 | User input |
| G | Date_Collected | 14 | Date field |
| H | Collected_By | 20 | User input |
| I | Storage_Location | 25 | User input |

#### Approval_SignOff Sheet

**Approval Table**

| Row | Role | Name | Signature | Date | Comments |
|-----|------|------|-----------|------|----------|
| 2 | Assessor | | | | |
| 3 | IT Manager | | | | |
| 4 | HR Manager | | | | |
| 5 | CISO | | | | |

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Implemented | Yes, Partial, No |
| Documented | Yes, No |
| Automated | Yes, No |
| Gap_Status | Gap, Compliant, Risk Accepted |
| Return_Required | Yes, No, Optional |
| Data_Wipe_Required | Yes, No, N/A |
| Employee_Type | Employee, Contractor, Consultant, Intern, Temp |
| Offboard_Reason | Resignation, Termination, Contract End, Transfer, Retirement, Other |
| Return_Status | Complete, In Progress, Pending, Overdue |
| Access_Revoked | Yes, No, Partial, N/A |
| Data_Wiped | Yes, No, Pending, N/A |
| Knowledge_Transfer | Complete, Partial, N/A |
| HR_Confirmed | Yes, No |
| Access_Type | Network, VPN, Email, Application, Database, Cloud, Physical, Admin |
| Verification_Method | AD Query, System Log, Login Attempt, Screenshot, Attestation, Certificate Check, Badge Scan |
| Evidence_Type | Document, Screenshot, Log, Form, Report, Certificate |

### Conditional Formatting Rules

**Return_Process Sheet**

| Condition | Format | Columns |
|-----------|--------|---------|
| Implemented = "No" | Red fill | D |
| Implemented = "Partial" | Yellow fill | D |
| Implemented = "Yes" | Green fill | D |
| Documented = "No" | Red text | E |
| Gap_Status = "Gap" | Red fill | I |

**Offboarding_Tracking Sheet**

| Condition | Format | Columns |
|-----------|--------|---------|
| Return_Status = "Overdue" | Red fill | L |
| Return_Status = "Complete" | Green fill | L |
| Access_Revoked = "No" | Red fill | M |
| Last_Working_Day < Today AND Return_Status <> "Complete" | Red border | Row |

**Access_Revocation Sheet**

| Condition | Format | Columns |
|-----------|--------|---------|
| SLA_Met = "No" | Red fill | J |
| SLA_Met = "Yes" | Green fill | J |
| Revocation_Date blank AND Last_Working_Day < Today | Red fill | I |

### Formula Specifications

**Return_Process Compliance Score**

```
=ROUND(SUMPRODUCT((D2:D19="Yes")*1,(D2:D19="Partial")*0.5)/18*100,1)
```

**Offboarding Completion Rate**

```
=ROUND(COUNTIF(L:L,"Complete")/COUNTA(A2:A1000)*100,1)
```

**Access Revocation SLA Compliance**

```
=ROUND(COUNTIF(J:J,"Yes")/COUNTA(J2:J1000)*100,1)
```

**Days Since Last Working Day**

```
=IF(G2="","",TODAY()-G2)
```

**Return Delta**

```
=J2-K2
```
(Assets Assigned - Assets Returned)

### Generator Reference

**Script**: `generate_a510_11_3_asset_return_offboarding.py`

**Location**: `10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/10_generator-master/`

**Dependencies**:
- openpyxl
- datetime
- logging

**Output**: `../90_workbooks/ISMS-IMP-A.5.10-11.S3_Asset_Return_and_Offboarding_Assessment_YYYYMMDD.xlsx`

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
