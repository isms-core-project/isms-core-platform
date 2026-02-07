**ISMS-IMP-A.5.5-6.S3-TG - External Communication Procedures**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.5.5 & A.5.6: Communication Procedures

## Implementation Guide for ISO 27001:2022 Controls A.5.5 & A.5.6: Communication Procedures

**Document ID:** ISMS-IMP-A.5.5-6.S3-TG
**Version:** 1.0
**Classification:** Internal Use
**Owner:** CISO
**Last Review:** [Date to be set]
**Next Review:** [Date to be set]

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | ISMS Team | Initial release |

---

# Technical Specification


> Auto-generated from `generate_a55_6_3_communication_procedures.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.5-6.S3` |
| **Output Filename** | `ISMS-IMP-A.5.5-6.S3_External_Communication_Procedures_YYYYMMDD.xlsx` |
| **Workbook Title** | External Communication Procedures |
| **Total Sheets** | 8 (8 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls A.5.5 & A.5.6: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Communication_Scenarios

**Data Rows:** 49 (rows 2–50)

### Columns

| Col | Header |
|-----|--------|
| A | Scenario_ID |
| B | Scenario_Name |
| C | Scenario_Category |
| D | Trigger_Event |
| E | Primary_Authority |
| F | Secondary_Authority |
| G | SIG_Contact |
| H | Response_Time |
| I | Approval_Level |
| J | Internal_Escalation_First |
| K | Documentation_Required |
| L | Template_Reference |
| M | Procedure_Steps |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C50 | `category_dv` |
| I | I2:I50 | `approval_dv` |
| J | J2:J50 | `yn_dv` |

---

## Sheet 3: Notification_Requirements

### Columns

| Col | Header |
|-----|--------|
| A | Requirement_ID |
| B | Regulation |
| C | Notification_Type |
| D | Authority |
| E | Trigger_Condition |
| F | Time_Limit |
| G | Required_Information |
| H | Format |
| I | Penalty_for_Non_Compliance |
| J | Internal_Owner |
| K | Procedure_Reference |
| L | Last_Review_Date |
| M | Notes |

---

## Sheet 4: Escalation_Matrix

### Columns

| Col | Header |
|-----|--------|
| A | Level |
| B | Scenario_Type |
| C | First_Contact |
| D | Escalation_1 |
| E | Escalation_2 |
| F | Escalation_3 |
| G | Time_to_Escalate |
| H | External_Contact_Approval |
| I | Notes |

---

## Sheet 5: Approval_Workflow

**Data Rows:** 29 (rows 2–30)

### Columns

| Col | Header |
|-----|--------|
| A | Workflow_ID |
| B | Communication_Type |
| C | Recipient_Type |
| D | Required_Approvers |
| E | Approval_Sequence |
| F | Max_Approval_Time |
| G | Delegate_When_Absent |
| H | Documentation_Required |
| I | Post_Communication_Actions |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E30 | `sequence_dv` |

---

## Sheet 6: Communication_Templates

**Data Rows:** 29 (rows 2–30)

### Columns

| Col | Header |
|-----|--------|
| A | Template_ID |
| B | Template_Name |
| C | Purpose |
| D | Recipient_Type |
| E | Required_Sections |
| F | Classification |
| G | Review_Date |
| H | Owner |
| I | Storage_Location |
| J | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| F | F2:F30 | `class_dv` |

---

## Sheet 7: Evidence_Register

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_ID |
| B | Evidence_Type |
| C | Description |
| D | Related_Procedure |
| E | Date_Created |
| F | Created_By |
| G | Storage_Location |
| H | Retention_Period |
| I | Review_Date |
| J | Status |
| K | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B2:B100 | `type_dv` |
| J | J2:J100 | `status_dv` |

---

## Sheet 8: Approval_SignOff

**Data Rows:** 19 (rows 2–20)

### Columns

| Col | Header |
|-----|--------|
| A | Approval_ID |
| B | Review_Period |
| C | Review_Date |
| D | Reviewer_Name |
| E | Reviewer_Role |
| F | Procedures_Complete |
| G | Templates_Current |
| H | Training_Complete |
| I | Approval_Status |
| J | Signature_Date |
| K | Next_Review_Date |
| L | Comments |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E20 | `role_dv` |
| F | F2:F20 | `yn_dv` |
| G | G2:G20 | `yn_dv` |
| H | H2:H20 | `yn_dv` |
| I | I2:I20 | `status_dv` |

---

**END OF SPECIFICATION**

---

*"The single biggest problem in communication is the illusion that it has taken place."*
— George Bernard Shaw

<!-- QA_VERIFIED: 2026-02-06 -->
