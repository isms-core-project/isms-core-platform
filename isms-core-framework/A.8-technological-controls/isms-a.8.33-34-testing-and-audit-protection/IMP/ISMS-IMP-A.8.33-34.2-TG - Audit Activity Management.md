<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.33-34.2-TG:framework:TG:a.8.33-34.2 -->
**ISMS-IMP-A.8.33-34.2-TG - Audit Activity Management Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of Information Systems During Audit Testing

### ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of Information Systems During Audit Testing

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.33-34.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Audit Activity Governance & System Protection |
| **Related Policy** | ISMS-POL-A.8.33-34, Section 2.2 (Audit Activity Management) |
| **Purpose** | Assess organizational compliance with audit testing governance including activity planning, tool authorization, access control, disruption mitigation, and evidence protection |
| **Target Audience** | Internal Audit, External Auditors, IT Security, Penetration Testers, Compliance Officers, IT Operations, Risk Management, Legal |
| **Assessment Type** | Process & Operational Compliance |
| **Review Cycle** | Annual (minimum) or After Major Audits |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Audit Activity Management assessment workbook | ISMS Implementation Team |

---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a83334_2_audit_activity_management.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.33-34.2` |
| **Output Filename** | `ISMS-IMP-A.8.33-34.2_Audit_Activity_Management_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Audit Activity Management Assessment |
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

## Sheet 2: Audit_Activity_Register

**Data Rows:** 50 (rows 5–54)

### Columns

| Col | Header |
|-----|--------|
| A | Audit_ID |
| B | Audit_Name |
| C | Audit_Type |
| D | Audit_Scope |
| E | Audit_Firm_Team |
| F | Lead_Auditor |
| G | Planned_Start |
| H | Planned_End |
| I | Actual_Start |
| J | Actual_End |
| K | Audit_Status |
| L | Management_Approval |
| M | Approver |
| N | Approval_Date |
| O | Systems_in_Scope |
| P | Data_Access_Required |
| Q | Testing_Type |
| R | Findings_Count |
| S | Critical_Findings |
| T | Report_Location |
| U | Follow_up_Status |
| V | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C5:C54 | `type_dv` |
| K | K5:K54 | `status_dv` |
| L | L5:L54 | `approval_dv` |
| Q | Q5:Q54 | `testing_dv` |
| U | U5:U54 | `followup_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B5:B54)` | Total Audits |
| — | `=COUNTIF(K5:K54,` | Planned Audits |
| — | `=COUNTIF(L5:L54,` | Approved Audits |
| — | `=COUNTIF(C5:C54,` | Internal Audits |
| — | `=SUM(R5:R54)` | Total Findings |
| — | `=SUM(S5:S54)` | Total Critical Findings |
| — | `=COUNTIF(U5:U54,` | Open Follow-ups |

---

## Sheet 3: Audit_Tool_Authorization

**Data Rows:** 50 (rows 5–54)

### Columns

| Col | Header |
|-----|--------|
| A | Tool_ID |
| B | Tool_Name |
| C | Tool_Version |
| D | Tool_Category |
| E | Vendor_Source |
| F | Tool_Owner |
| G | Authorization_Status |
| H | Authorization_Date |
| I | Authorized_By |
| J | Risk_Level |
| K | Authorized_Use_Cases |
| L | Restrictions |
| M | Required_Approvals |
| N | Storage_Location |
| O | Access_Restricted_To |
| P | Last_Security_Review |
| Q | Next_Review_Due |
| R | Usage_Logging_Required |
| S | License_Status |
| T | License_Expiry |
| U | Evidence_Reference |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D5:D54 | `category_dv` |
| G | G5:G54 | `auth_dv` |
| J | J5:J54 | `risk_dv` |
| R | R5:R54 | `yn_dv` |
| S | S5:S54 | `license_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B5:B54)` | Total Tools |
| — | `=COUNTIF(G5:G54,` | Authorized Tools |
| — | `=COUNTIF(J5:J54,` | High Risk Tools |
| — | `=COUNTIF(S5:S54,` | Expired Licenses |

---

## Sheet 4: Audit_Access_Tracking

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Access_ID |
| B | Auditor_Name |
| C | Auditor_Organization |
| D | Associated_Audit |
| E | Access_Type |
| F | Systems_Accessed |
| G | Data_Classification_Accessed |
| H | Access_Requested_Date |
| I | Access_Start_Date |
| J | Access_End_Date |
| K | Actual_Revocation_Date |
| L | Access_Status |
| M | Approval_Status |
| N | Approver |
| O | Approval_Date |
| P | Access_Logging_Enabled |
| Q | NDA_Signed |
| R | NDA_Reference |
| S | Supervision_Required |
| T | Supervisor |
| U | Multi_Factor_Auth_Required |
| V | Revocation_Confirmation |
| W | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E5:E104 | `access_type_dv` |
| G | G5:G104 | `classification_dv` |
| L | L5:L104 | `status_dv` |
| M | M5:M104 | `approval_dv` |
| P | P5:P104 | `ynp_dv` |
| Q | Q5:Q104 | `yn_dv` |
| S | S5:S104 | `yn_dv` |
| U | U5:U104 | `yn_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B5:B104)` | Total Access Grants |
| — | `=COUNTIF(L5:L104,` | Active Access |
| — | `=COUNTIF(M5:M104,` | Approved Access |
| — | `=COUNTIF(E5:E104,` | Read-Only Access |
| — | `=COUNTIF(G5:G104,` | Restricted Data Access |
| — | `=COUNTIF(Q5:Q104,` | NDA Coverage (Yes) |
| — | `=COUNTIF(P5:P104,` | Access Logging (Yes) |
| — | `=COUNTIF(U5:U104,` | MFA Required (Yes) |

---

## Sheet 5: Disruption_Mitigation_Plans

**Data Rows:** 50 (rows 5–54)

### Columns

| Col | Header |
|-----|--------|
| A | System_ID |
| B | System_Name |
| C | System_Criticality |
| D | Business_Owner |
| E | Technical_Owner |
| F | Associated_Audits |
| G | Primary_Mitigation_Strategy |
| H | Testing_Restrictions |
| I | Permitted_Testing_Window |
| J | Maximum_Test_Duration |
| K | Backup_Required_Before_Test |
| L | Recovery_Point_Objective |
| M | Recovery_Time_Objective |
| N | Rollback_Procedure_Location |
| O | Rollback_Last_Tested |
| P | Escalation_Contact |
| Q | Escalation_Phone |
| R | Secondary_Contact |
| S | Monitoring_Enhancement |
| T | Incident_Response_Plan |
| U | Last_Mitigation_Review |
| V | Review_Due_Date |
| W | Evidence_Reference |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C5:C54 | `criticality_dv` |
| G | G5:G54 | `strategy_dv` |
| K | K5:K54 | `backup_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B5:B54)` | Total Systems |
| — | `=COUNTIF(C5:C54,` | Critical Systems |
| — | `=COUNTA(N5:N54)` | With Rollback Procedure |
| — | `=COUNTIF(K5:K54,` | Backup Required |

---

## Sheet 6: Audit_Evidence_Protection

**Data Rows:** 30 (rows 5–34)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_Category_ID |
| B | Evidence_Category |
| C | Evidence_Description |
| D | Sensitivity_Classification |
| E | Example_Documents |
| F | Primary_Storage_Location |
| G | Backup_Location |
| H | Encryption_at_Rest |
| I | Encryption_in_Transit |
| J | Access_Control_Type |
| K | Authorized_Accessors |
| L | Retention_Period |
| M | Retention_Start_Event |
| N | Destruction_Method |
| O | Destruction_Approval |
| P | Chain_of_Custody_Required |
| Q | Chain_of_Custody_Process |
| R | Legal_Hold_Applicable |
| S | Legal_Hold_Contact |
| T | Integrity_Verification |
| U | Last_Access_Review |
| V | Evidence_Owner |
| W | Evidence_Reference |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D5:D34 | `classification_dv` |
| H | H5:H34 | `enc_rest_dv` |
| I | I5:I34 | `enc_transit_dv` |
| J | J5:J34 | `access_dv` |
| L | L5:L34 | `retention_dv` |
| N | N5:N34 | `destruction_dv` |
| P | P5:P34 | `yn_dv` |
| R | R5:R34 | `legal_dv` |
| T | T5:T34 | `integrity_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B5:B34)` | Total Evidence Categories |
| — | `=COUNTIF(D5:D34,` | Restricted Categories |
| — | `=COUNTIF(H5:H34,` | Encryption at Rest (AES-256) |
| — | `=COUNTIF(I5:I34,` | Encryption in Transit (TLS 1.3) |
| — | `=COUNTIF(P5:P34,` | Chain of Custody Required |
| — | `=COUNTIF(R5:R34,` | Legal Hold Applicable |

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
| — | `=COUNTIF(E5:E104,` | Evidence by Area - Audit Activity |

---

## Sheet 9: Approval_Sign_Off

---

**END OF SPECIFICATION**

---

*"The purpose of an audit is to improve, not to prove."*

<!-- QA_VERIFIED: 2026-02-06 -->
