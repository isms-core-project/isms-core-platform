**ISMS-IMP-A.5.5-6.S2-TG - Special Interest Groups Register**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.6: Contact with Special Interest Groups

## Implementation Guide for ISO 27001:2022 Control A.5.6: Contact with Special Interest Groups

**Document ID:** ISMS-IMP-A.5.5-6.S2-TG
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


> Auto-generated from `generate_a55_6_2_special_interest_groups.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.5-6.S2` |
| **Output Filename** | `ISMS-IMP-A.5.5-6.S2_Special_Interest_Groups_Register_YYYYMMDD.xlsx` |
| **Workbook Title** | Special Interest Groups Register |
| **Total Sheets** | 8 (8 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls A.5.5 & A.5.6: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Groups_Registry

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Group_ID |
| B | Group_Name |
| C | Group_Type |
| D | Focus_Area |
| E | Geographic_Scope |
| F | Website |
| G | Primary_Contact |
| H | Contact_Email |
| I | Internal_Owner |
| J | Owner_Department |
| K | Membership_Status |
| L | Member_Since |
| M | Membership_Level |
| N | Annual_Cost |
| O | Value_Rating |
| P | Last_Engagement |
| Q | Next_Review |
| R | Strategic_Priority |
| S | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C100 | `type_dv` |
| D | D2:D100 | `focus_dv` |
| E | E2:E100 | `scope_dv` |
| K | K2:K100 | `status_dv` |
| M | M2:M100 | `level_dv` |
| O | O2:O100 | `value_dv` |
| R | R2:R100 | `priority_dv` |

---

## Sheet 3: Membership_Details

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Group_ID |
| B | Group_Name |
| C | Membership_Start |
| D | Membership_End |
| E | Membership_Type |
| F | Access_Level |
| G | Portal_Credentials |
| H | Mailing_Lists_Subscribed |
| I | Events_Access |
| J | Intel_Feed_Access |
| K | Publication_Access |
| L | Voting_Rights |
| M | Annual_Fee |
| N | Billing_Contact |
| O | Contract_Reference |
| P | Benefits_Summary |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E100 | `type_dv` |
| F | F2:F100 | `access_dv` |
| I | I2:I100 | `yn_dv` |
| J | J2:J100 | `yn_dv` |
| K | K2:K100 | `yn_dv` |
| L | L2:L100 | `yn_dv` |

---

## Sheet 4: Engagement_Log

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Engagement_ID |
| B | Group_ID |
| C | Group_Name |
| D | Date |
| E | Engagement_Type |
| F | Description |
| G | Our_Representative |
| H | Key_Topics |
| I | Outcomes |
| J | Action_Items |
| K | Follow_Up_Date |
| L | Evidence_Reference |
| M | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E200 | `type_dv` |

---

## Sheet 5: Intelligence_Received

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Intel_ID |
| B | Group_ID |
| C | Group_Name |
| D | Date_Received |
| E | Intel_Type |
| F | Classification |
| G | Title |
| H | Summary |
| I | Relevance_To_Org |
| J | Action_Taken |
| K | Distributed_To |
| L | Distribution_Date |
| M | Evidence_Location |
| N | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E200 | `type_dv` |
| F | F2:F200 | `class_dv` |
| I | I2:I200 | `relevance_dv` |

---

## Sheet 6: Contribution_Log

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Contribution_ID |
| B | Group_ID |
| C | Group_Name |
| D | Date |
| E | Contribution_Type |
| F | Title |
| G | Description |
| H | Contributor |
| I | Approval_Status |
| J | Approved_By |
| K | Classification_Check |
| L | Publication_Status |
| M | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E100 | `type_dv` |
| I | I2:I100 | `approval_dv` |
| K | K2:K100 | `class_dv` |
| L | L2:L100 | `pub_dv` |

---

## Sheet 7: Evidence_Register

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_ID |
| B | Evidence_Type |
| C | Description |
| D | Related_Group_ID |
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
| F | Registry_Complete |
| G | Memberships_Active |
| H | Value_Assessed |
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

*"If you want to go fast, go alone. If you want to go far, go together."*
— African Proverb

<!-- QA_VERIFIED: 2026-02-06 -->
