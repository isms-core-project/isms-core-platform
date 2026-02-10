<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.5-6.S1-TG:framework:TG:a.5.5-6 -->
**ISMS-IMP-A.5.5-6.S1-TG - Authority Contacts Register**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.5: Contact with Authorities

## Implementation Guide for ISO 27001:2022 Control A.5.5: Contact with Authorities

**Document ID:** ISMS-IMP-A.5.5-6.S1-TG
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


> Auto-generated from `generate_a55_6_1_authority_contacts.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.5-6.S1` |
| **Output Filename** | `ISMS-IMP-A.5.5-6.S1_Authority_Contacts_Register_YYYYMMDD.xlsx` |
| **Workbook Title** | Authority Contacts Register |
| **Total Sheets** | 7 (7 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls A.5.5 & A.5.6: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #D6DCE4 | D6DCE4 | Silver (Neutral) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Authority_Registry

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Contact_ID |
| B | Authority_Name |
| C | Authority_Type |
| D | Jurisdiction |
| E | Primary_Contact_Name |
| F | Primary_Contact_Title |
| G | Primary_Phone |
| H | Primary_Email |
| I | Secondary_Contact_Name |
| J | Secondary_Phone |
| K | Website |
| L | Physical_Address |
| M | Internal_Owner |
| N | Owner_Department |
| O | Relationship_Status |
| P | Last_Contact_Date |
| Q | Next_Review_Date |
| R | Escalation_Trigger |
| S | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C100 | `type_dv` |
| D | D2:D100 | `jurisdiction_dv` |
| O | O2:O100 | `status_dv` |

---

## Sheet 3: Contact_Types

### Columns

| Col | Header |
|-----|--------|
| A | Type_Code |
| B | Authority_Type |
| C | Description |
| D | Typical_Scenarios |
| E | Mandatory_Contact |
| F | Response_SLA |
| G | Escalation_Path |
| H | Required_Information |
| I | Example_Authorities |

---

## Sheet 4: Communication_Log

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Log_ID |
| B | Contact_ID |
| C | Authority_Name |
| D | Communication_Date |
| E | Communication_Type |
| F | Direction |
| G | Subject |
| H | Summary |
| I | Our_Representative |
| J | Authority_Representative |
| K | Outcome |
| L | Follow_Up_Required |
| M | Follow_Up_Date |
| N | Evidence_Reference |
| O | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E200 | `type_dv` |
| F | F2:F200 | `direction_dv` |
| L | L2:L200 | `followup_dv` |

---

## Sheet 5: Verification_Register

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Verification_ID |
| B | Contact_ID |
| C | Authority_Name |
| D | Verification_Date |
| E | Verified_By |
| F | Verification_Method |
| G | Contact_Details_Correct |
| H | Escalation_Path_Tested |
| I | Website_Accessible |
| J | Relationship_Active |
| K | Issues_Found |
| L | Actions_Required |
| M | Next_Verification |
| N | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| F | F2:F100 | `method_dv` |
| G | G2:G100 | `yn_dv` |
| H | H2:H100 | `yn_dv` |
| I | I2:I100 | `yn_dv` |
| J | J2:J100 | `yn_dv` |

---

## Sheet 6: Evidence_Register

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_ID |
| B | Evidence_Type |
| C | Description |
| D | Related_Contact_ID |
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

## Sheet 7: Approval_SignOff

**Data Rows:** 19 (rows 2–20)

### Columns

| Col | Header |
|-----|--------|
| A | Approval_ID |
| B | Review_Period |
| C | Review_Date |
| D | Reviewer_Name |
| E | Reviewer_Role |
| F | Registry_Complete |
| G | Contacts_Verified |
| H | Communication_Log_Current |
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

*"In a crisis, the first thing you need is a number you can call."*
— Unknown

<!-- QA_VERIFIED: 2026-02-06 -->
