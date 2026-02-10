<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.33-34.1-TG:framework:TG:a.8.33-34.1 -->
**ISMS-IMP-A.8.33-34.1-TG - Test Data Protection Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of Information Systems During Audit Testing

### ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of Information Systems During Audit Testing

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.33-34.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Test Data Governance & Protection |
| **Related Policy** | ISMS-POL-A.8.33-34, Section 2.1 (Test Data Protection) |
| **Purpose** | Assess organizational compliance with test data protection requirements including inventory, masking, anonymization, and environment registry management |
| **Target Audience** | Test Managers, Development Teams, Security Officers, Data Protection Officers, QA Teams, Compliance Officers, IT Operations, Auditors |
| **Assessment Type** | Process & Operational Compliance |
| **Review Cycle** | Semi-Annual (minimum) or After Major System Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Test Data Protection assessment workbook | ISMS Implementation Team |

---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a83334_1_test_data_protection.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.33-34.1` |
| **Output Filename** | `ISMS-IMP-A.8.33-34.1_Test_Data_Protection_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Test Data Protection Assessment |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D6DCE4 | D6DCE4 | Silver (Neutral) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions_and_Legend

---

## Sheet 2: Test_Data_Inventory

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Data_Set_ID |
| B | Data_Set_Name |
| C | Source_System |
| D | Target_Environment |
| E | Data_Classification |
| F | Contains_PII |
| G | PII_Categories |
| H | Data_Volume |
| I | Authorization_Status |
| J | Data_Owner |
| K | Authorizer |
| L | Authorization_Date |
| M | Last_Copy_Date |
| N | Refresh_Frequency |
| O | Masking_Required |
| P | Masking_Status |
| Q | Business_Justification |
| R | Expiration_Date |
| S | Evidence_Reference |
| T | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E5:E104 | `classification_dv` |
| F | F5:F104 | `pii_dv` |
| O | O5:O104 | `pii_dv` |
| I | I5:I104 | `auth_status_dv` |
| N | N5:N104 | `refresh_dv` |
| P | P5:P104 | `masking_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B5:B104)` | Total Data Sets |
| — | `=COUNTIF(I5:I104,` | Authorized Data Sets |
| — | `=COUNTIF(F5:F104,` | Data Sets with PII |
| — | `=COUNTIFS(F5:F104,` | Fully Masked PII Sets |

---

## Sheet 3: Data_Masking_Assessment

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Data_Set_ID |
| B | Data_Set_Name |
| C | Target_Environment |
| D | Contains_PII |
| E | Masking_Status |
| F | Primary_Masking_Technique |
| G | Masking_Tool |
| H | Masking_Effectiveness_Score |
| I | PII_Fields_Identified |
| J | PII_Fields_Masked |
| K | PII_Fields_Unmasked |
| L | Masking_Verification_Date |
| M | Verification_Method |
| N | Re_identification_Risk |
| O | Masking_Gap_Severity |
| P | Remediation_Owner |
| Q | Remediation_Target_Date |
| R | Remediation_Status |
| S | Exception_Approved |
| T | Exception_Justification |
| U | Evidence_Reference |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D5:D104 | `pii_dv` |
| S | S5:S104 | `pii_dv` |
| E | E5:E104 | `masking_dv` |
| F | F5:F104 | `technique_dv` |
| H | H5:H104 | `score_dv` |
| M | M5:M104 | `verify_dv` |
| N | N5:N104 | `risk_dv` |
| O | O5:O104 | `severity_dv` |
| R | R5:R104 | `status_dv` |

---

## Sheet 4: Test_Environment_Registry

**Data Rows:** 50 (rows 5–54)

### Columns

| Col | Header |
|-----|--------|
| A | Environment_ID |
| B | Environment_Name |
| C | Environment_Type |
| D | Infrastructure_Type |
| E | Environment_Owner |
| F | Business_Unit |
| G | Highest_Data_Classification |
| H | Contains_Production_Data |
| I | Access_Control_Type |
| J | Network_Isolation |
| K | Encryption_at_Rest |
| L | Encryption_in_Transit |
| M | Logging_Enabled |
| N | Patch_Management |
| O | Security_Control_Status |
| P | Last_Security_Review |
| Q | Next_Review_Due |
| R | Data_Masking_Enforced |
| S | Environment_URL_Location |
| T | Support_Contact |
| U | Evidence_Reference |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C5:C54 | `env_type_dv` |
| D | D5:D54 | `infra_type_dv` |
| G | G5:G54 | `classification_dv` |
| H | H5:H54 | `yn_dv` |
| I | I5:I54 | `access_dv` |
| J | J5:J54 | `isolation_dv` |
| K | K5:K54 | `ynp_dv` |
| L | L5:L54 | `ynp_dv` |
| M | M5:M54 | `ynp_dv` |
| R | R5:R54 | `ynp_dv` |
| N | N5:N54 | `patch_dv` |
| O | O5:O54 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B5:B54)` | Total Environments |
| — | `=COUNTIF(C5:C54,` | Development Environments |
| — | `=COUNTIF(H5:H54,` | Environments with Prod Data |
| — | `=COUNTIF(O5:O54,` | Security Compliant |
| — | `=COUNTIF(J5:J54,` | Full Network Isolation |

---

## Sheet 5: Data_Refresh_Schedule

**Data Rows:** 50 (rows 5–54)

### Columns

| Col | Header |
|-----|--------|
| A | Refresh_ID |
| B | Target_Environment |
| C | Data_Sources |
| D | Refresh_Frequency |
| E | Refresh_Method |
| F | Last_Refresh_Date |
| G | Next_Scheduled_Refresh |
| H | Authorization_Status |
| I | Authorizer |
| J | Authorization_Date |
| K | Masking_Applied_at_Refresh |
| L | Masking_Tool |
| M | Data_Volume |
| N | Refresh_Duration |
| O | Refresh_Window |
| P | Retention_Period |
| Q | Auto_Purge_Enabled |
| R | Refresh_Owner |
| S | Refresh_Log_Location |
| T | Evidence_Reference |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D5:D54 | `freq_dv` |
| E | E5:E54 | `method_dv` |
| H | H5:H54 | `auth_dv` |
| K | K5:K54 | `masking_dv` |
| Q | Q5:Q54 | `yn_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B5:B54)` | Total Refresh Schedules |
| — | `=COUNTIF(H5:H54,` | Authorized Refreshes |
| — | `=COUNTIF(D5:D54,` | Daily Refreshes |
| — | `=COUNTIF(K5:K54,` | Masking Automated |
| — | `=COUNTIF(Q5:Q54,` | Auto-Purge Enabled |

---

## Sheet 6: Compliance_Verification

**Data Rows:** 50 (rows 5–54)

### Columns

| Col | Header |
|-----|--------|
| A | Requirement_ID |
| B | Requirement_Source |
| C | Requirement_Reference |
| D | Requirement_Description |
| E | Applicable_Data_Sets |
| F | Applicable_Environments |
| G | Compliance_Status |
| H | Last_Verification_Date |
| I | Verification_Method |
| J | Verifier |
| K | Findings |
| L | Finding_Severity |
| M | Remediation_Required |
| N | Remediation_Owner |
| O | Remediation_Target_Date |
| P | Remediation_Status |
| Q | Next_Verification_Due |
| R | Evidence_Reference |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B5:B54 | `source_dv` |
| G | G5:G54 | `status_dv` |
| I | I5:I54 | `method_dv` |
| L | L5:L54 | `severity_dv` |
| M | M5:M54 | `yn_dv` |
| P | P5:P54 | `rem_status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B5:B54)` | Total Requirements |
| — | `=COUNTIF(G5:G54,` | Compliant |
| — | `=COUNTIF(L5:L54,` | Critical Findings |

---

## Sheet 7: Summary_Dashboard

**Data Rows:** 9 (rows 7–15)

### Columns

| Col | Header |
|-----|--------|
| A | Metric |
| B | Value |
| C | Target |
| D | Status |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D7:D15 | `status_dv` |

---

## Sheet 8: Evidence_Register

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_ID |
| B | Evidence_Type |
| C | Evidence_Title |
| D | Description |
| E | Related_Assessment_Area |
| F | Related_Finding_Control |
| G | Document_Location |
| H | Date_Collected |
| I | Collected_By |
| J | Verification_Status |
| K | Verified_By |
| L | Verification_Date |
| M | Retention_Period |
| N | Expiration_Date |
| O | Confidentiality |
| P | Auditor_Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B5:B104 | `type_dv` |
| E | E5:E104 | `area_dv` |
| J | J5:J104 | `status_dv` |
| M | M5:M104 | `retention_dv` |
| O | O5:O104 | `conf_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B5:B104)` | Total Evidence Entries |
| — | `=COUNTIF(J5:J104,` | Verified Evidence |
| — | `=COUNTIF(E5:E104,` | Evidence by Area - Inventory |

---

## Sheet 9: Approval_Sign_Off

---

**END OF SPECIFICATION**

---

*"The best time to discover a data protection flaw is during testing, not after a breach."*

<!-- QA_VERIFIED: 2026-02-06 -->
