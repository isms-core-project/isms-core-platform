**ISMS-IMP-A.8.15.3-TG - Log Protection & Retention Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Log Protection, Integrity, Access Control & Retention Compliance |
| **Related Policy** | ISMS-POL-A.8.15, Section 2.2 (Log Protection & Integrity), Section 2.3 (Log Retention & Storage), Section 2.5 (Privacy & Data Protection) |
| **Purpose** | Verify log integrity protection mechanisms, validate access controls, assess retention compliance, evaluate privacy controls |
| **Target Audience** | Information Security Team, SOC, IT Operations, Data Protection Officer (DPO), Legal/Compliance, Storage Team, Auditors, Workbook Developers |
| **Assessment Type** | Security & Compliance |
| **Review Cycle** | Semi-annual (full assessment), Quarterly (retention compliance check) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial technical specification | ISMS Implementation Team |


---
# Technical Specification
**Audience:** Workbook Developers (Python/Excel script maintainers)


> Auto-generated from `generate_a815_3_log_protection_retention.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.15.3` |
| **Output Filename** | `ISMS-IMP-A.8.15.3_Log_Protection_Retention_YYYYMMDD.xlsx` |
| **Total Sheets** | 30 (30 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.15: Logging |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #4472C4 | end_color | Medium Blue (Sub-headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: Access Control Assessment

---

## Sheet 3: Integrity Protection

---

## Sheet 4: Secure Transmission

---

## Sheet 5: Retention Period Compliance

---

## Sheet 6: Storage Tier Implementation

---

## Sheet 7: Log Backup & Recovery

---

## Sheet 8: Disposal Procedures

---

## Sheet 9: Separation of Duties

---

## Sheet 10: Legal Hold Management

---

## Sheet 11: Privacy Impact Assessment

---

## Sheet 12: Gap Analysis

---

## Sheet 13: Evidence Register

---

## Sheet 14: Summary Dashboard

---

## Sheet 15: Approval & Sign-Off

---

## Sheet 16: Instructions

**Frozen Panes:** A3

---

## Sheet 17: Access_Control

**Purpose:** "Security is a process, not a product." - Bruce Schneier

**Data Rows:** 92 (rows 9–100) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Log Source / SIEM Component | 30 |
| B | Access Control Type | 20 |
| C | Authentication Required | 18 |
| D | Authorization Model | 20 |
| E | Read Access Controlled | 18 |
| F | Write Access Prevented | 20 |
| G | Delete Access Controlled | 20 |
| H | Admin Separation | 20 |
| I | Access Logged (Meta) | 20 |
| J | MFA Required for Admin | 20 |
| K | Last Access Review | 18 |
| L | Review Frequency | 20 |
| M | Non-Compliance Issues | 40 |
| N | Compliance Score | 15 |
| O | Remediation Required | 18 |
| P | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B9:B100 | `access_type_dv` |
| C | C9:C100 | `yes_no_dv` |
| O | O9:O100 | `yes_no_dv` |
| D | D9:D100 | `auth_model_dv` |
| E | E9:E100 | `read_dv` |
| F | F9:F100 | `write_dv` |
| G | G9:G100 | `delete_dv` |
| H | H9:H100 | `admin_sep_dv` |
| I | I9:I100 | `logged_dv` |
| J | J9:J100 | `mfa_dv` |
| L | L9:L100 | `frequency_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| NN | `=IF(A{data_row}=` |  |

---

## Sheet 18: Integrity_Protection

**Data Rows:** 92 (rows 9–100) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Log Source / Storage | 30 |
| B | Log Criticality | 18 |
| C | Write-Once Storage (WORM) | 20 |
| D | WORM Technology | 25 |
| E | Cryptographic Hashing | 20 |
| F | Hash Algorithm | 18 |
| G | Hash Storage Location | 25 |
| H | Digital Signatures | 18 |
| I | File Sealing | 18 |
| J | Integrity Check Frequency | 20 |
| K | Last Integrity Check | 18 |
| L | Tampering Detected | 18 |
| M | Backup Protected | 18 |
| N | Compliance with Policy | 20 |
| O | Gap Description | 40 |
| P | Remediation Plan | 40 |
| Q | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B9:B100 | `criticality_dv` |
| C | C9:C100 | `yes_no_dv` |
| E | E9:E100 | `yes_no_dv` |
| H | H9:H100 | `yes_no_dv` |
| I | I9:I100 | `yes_no_dv` |
| M | M9:M100 | `yes_no_dv` |
| D | D9:D100 | `worm_tech_dv` |
| F | F9:F100 | `hash_algo_dv` |
| J | J9:J100 | `frequency_dv` |
| L | L9:L100 | `tampering_dv` |

---

## Sheet 19: Secure_Transmission

**Data Rows:** 192 (rows 9–200) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Source System | 30 |
| B | Destination (SIEM) | 25 |
| C | Transport Protocol | 20 |
| D | Encryption in Transit | 18 |
| E | TLS Version | 15 |
| F | Certificate Validation | 20 |
| G | Network Segment | 20 |
| H | Firewall Protection | 18 |
| I | Source Authentication | 20 |
| J | Vulnerability Risk | 18 |
| K | Compliance Status | 18 |
| L | Remediation Required | 18 |
| M | Target Date | 15 |
| N | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C9:C200 | `protocol_dv` |
| D | D9:D200 | `encryption_dv` |
| E | E9:E200 | `tls_version_dv` |
| F | F9:F200 | `cert_val_dv` |
| G | G9:G200 | `network_dv` |
| H | H9:H200 | `yes_no_dv` |
| L | L9:L200 | `yes_no_dv` |
| I | I9:I200 | `auth_dv` |
| J | J9:J200 | `risk_dv` |

---

## Sheet 20: Retention_Period

**Data Rows:** 92 (rows 9–100) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Log Source / Type | 30 |
| B | Log Category | 20 |
| C | Regulatory Requirement | 25 |
| D | Policy Retention (months) | 20 |
| E | Hot Storage Period (months) | 22 |
| F | Warm Storage Period (months) | 22 |
| G | Cold Storage Period (years) | 20 |
| H | Total Retention (months) | 20 |
| I | Meets Policy Requirement | 20 |
| J | Retention Gap (months) | 20 |
| K | Over-Retention (months) | 20 |
| L | Automated Disposal | 18 |
| M | Last Disposal Date | 18 |
| N | Legal Hold Capability | 18 |
| O | Compliance Status | 18 |
| P | Remediation Action | 40 |
| Q | Target Date | 15 |
| R | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B9:B100 | `category_dv` |
| C | C9:C100 | `regulatory_dv` |
| L | L9:L100 | `yes_no_dv` |
| N | N9:N100 | `yes_no_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| HN | `=IF(A{data_row}=` |  |
| JN | `=IF(I{data_row}=` |  |
| KN | `=IF(H{data_row}<=D{data_row}*1.5,0,H{data_row}-D{data_row})` |  |

---

## Sheet 21: Storage_Tier

**Data Rows:** 22 (rows 9–30) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Storage Tier | 20 |
| B | Technology | 25 |
| C | Capacity (TB) | 15 |
| D | Used (TB) | 15 |
| E | % Used | 12 |
| F | Retention Period | 20 |
| G | Access Performance | 20 |
| H | Encryption at Rest | 18 |
| I | Encryption Method | 20 |
| J | Geographic Location | 25 |
| K | Redundancy | 20 |
| L | Backup Implemented | 18 |
| M | Meets Policy Requirements | 20 |
| N | Issues | 40 |
| O | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| A | A9:A30 | `tier_dv` |
| B | B9:B30 | `tech_dv` |
| G | G9:G30 | `performance_dv` |
| H | H9:H30 | `yes_no_dv` |
| L | L9:L30 | `yes_no_dv` |
| M | M9:M30 | `yes_no_dv` |
| I | I9:I30 | `encryption_dv` |
| K | K9:K30 | `redundancy_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IF(C{data_row}=0,0,D{data_row}/C{data_row})` |  |

---

## Sheet 22: Backup_Recovery

**Purpose:** "Hope is not a strategy." - Ancient Sysadmin Proverb

**Data Rows:** 17 (rows 9–25) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Backup Scope | 30 |
| B | Backup Frequency | 20 |
| C | Backup Technology | 25 |
| D | Backup Location | 30 |
| E | Backup Encrypted | 18 |
| F | Encryption Algorithm | 20 |
| G | Backup Integrity Verified | 20 |
| H | Last Backup Date | 18 |
| I | Last Restore Test Date | 18 |
| J | Restore Test Frequency | 20 |
| K | Last Restore Success | 18 |
| L | RTO (Recovery Time) | 20 |
| M | RPO (Recovery Point) | 20 |
| N | Backup Retention Period | 20 |
| O | Compliance Status | 18 |
| P | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| A | A9:A25 | `scope_dv` |
| B | B9:B25 | `frequency_dv` |
| D | D9:D25 | `location_dv` |
| E | E9:E25 | `yes_no_dv` |
| K | K9:K25 | `yes_no_dv` |
| F | F9:F25 | `encryption_dv` |
| G | G9:G25 | `verified_dv` |
| J | J9:J25 | `test_freq_dv` |

---

## Sheet 23: Disposal_Procedures

**Data Rows:** 42 (rows 9–50) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Log Type / Source | 30 |
| B | Retention Period Expired | 20 |
| C | Automated Disposal | 18 |
| D | Disposal Method | 25 |
| E | Disposal Approval Required | 22 |
| F | Legal Hold Check | 18 |
| G | Disposal Logged | 18 |
| H | Last Disposal Date | 18 |
| I | Volume Disposed (GB) | 20 |
| J | Disposal Verification | 20 |
| K | Compliance with Policy | 20 |
| L | Issues | 40 |
| M | Remediation | 40 |
| N | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C9:C50 | `automated_dv` |
| D | D9:D50 | `method_dv` |
| E | E9:E50 | `approval_dv` |
| F | F9:F50 | `legal_hold_dv` |
| G | G9:G50 | `logged_dv` |
| J | J9:J50 | `verified_dv` |

---

## Sheet 24: Separation_Of_Duties

**Data Rows:** 42 (rows 9–50) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | System / Component | 30 |
| B | System Administrator(s) | 30 |
| C | Log Administrator(s) | 30 |
| D | Roles Separated | 18 |
| E | Sys Admin Can Modify Logs | 25 |
| F | Compensating Controls | 40 |
| G | Break-Glass Procedure | 20 |
| H | Break-Glass Usage Logged | 22 |
| I | Independent Review | 20 |
| J | Last Review Date | 18 |
| K | Violations Detected | 18 |
| L | Compliance Status | 18 |
| M | Remediation Plan | 40 |
| N | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D9:D50 | `separated_dv` |
| E | E9:E50 | `modify_dv` |
| G | G9:G50 | `breakglass_dv` |
| H | H9:H50 | `yes_no_dv` |
| I | I9:I50 | `yes_no_dv` |
| K | K9:K50 | `violations_dv` |

---

## Sheet 25: Legal_Hold

**Data Rows:** 22 (rows 9–30) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Hold ID | 15 |
| B | Hold Name / Matter | 30 |
| C | Initiation Date | 15 |
| D | Initiated By | 25 |
| E | Scope Description | 40 |
| F | Systems/Sources Affected | 30 |
| G | Date Range | 20 |
| H | Hold Status | 15 |
| I | Review Date | 15 |
| J | Disposal Prevented | 18 |
| K | Release Date | 15 |
| L | Release Authorized By | 25 |
| M | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| H | H9:H30 | `status_dv` |
| J | J9:J30 | `prevented_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{data_row}<>` |  |

---

## Sheet 26: Privacy_Impact

**Frozen Panes:** A6

### Columns

| Col | Header |
|-----|--------|
| A | Log Category |
| B | PII/Sensitive Data Present |
| C | Data Types |
| D | Minimization Applied |
| E | Justification |
| F | Retention Period |
| G | GDPR Article |
| H | Compliance Status |
| I | Review Date |
| J | Owner |
| K | Notes |

---

## Sheet 27: Evidence_Register

**Data Rows:** 95 (rows 6–100) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 12 |
| B | Assessment Sheet | 24 |
| C | Evidence Type | 20 |
| D | Evidence Title | 35 |
| E | Description | 40 |
| F | File Location/Link | 35 |
| G | Date Collected | 14 |
| H | Collected By | 18 |
| I | Retention Period | 15 |
| J | Review Date | 14 |
| K | Status | 12 |
| L | Notes | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C6:C100 | `type_dv` |
| B | B6:B100 | `sheet_dv` |
| K | K6:K100 | `status_dv` |

---

## Sheet 28: Gap_Analysis

**Data Rows:** 92 (rows 9–100) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 12 |
| B | Gap Category | 25 |
| C | Description | 50 |
| D | Affected Systems | 30 |
| E | Policy Requirement | 30 |
| F | Risk Level | 15 |
| G | Remediation Action | 50 |
| H | Owner | 25 |
| I | Target Date | 15 |
| J | Budget Required | 15 |
| K | Status | 15 |
| L | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B9:B100 | `category_dv` |
| F | F9:F100 | `risk_dv` |
| J | J9:J100 | `budget_dv` |
| K | K9:K100 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{data_row}<>` |  |

---

## Sheet 29: Summary_Dashboard

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIF(` | Access Controls Compliant |
| DN | `=IF(B{row}>0,\` |  |
| BN | `=COUNTIFS(\` |  |
| EN | `=IF((B{row}+C{row}+D{row})=0,0,B{row}/(B{row}+C{row}+D{row}))` |  |
| NN | `=SUM({col}{row-4}:{col}{row-1})` |  |
| EN | `=SUMPRODUCT((\` |  |

---

## Sheet 30: Approval_Signoff

---

**END OF SPECIFICATION**

---

*"Information is not knowledge. The only source of knowledge is experience."*
- Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
