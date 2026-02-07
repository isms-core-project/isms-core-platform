**ISMS-IMP-A.8.30.2-TG - Contract Compliance**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.30: Outsourced Development

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.2-TG |
| **Document Title** | Contract Compliance Workbook Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.30: Outsourced Development |
| **Parent Policy** | ISMS-POL-A.8.30 (Outsourced Development) |
| **Version** | 1.0 |
| **Classification** | Internal |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial implementation specification for ISO 27001:2022 first certification |

---

# Technical Specification


> Auto-generated from `generate_a830_2_contract_compliance.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.30.2` |
| **Output Filename** | `ISMS-IMP-A.8.30.2_Contract_Compliance_YYYYMMDD.xlsx` |
| **Workbook Title** | Contract Compliance |
| **Total Sheets** | 6 (6 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #D6DCE4 | D6DCE4 | Silver (Neutral) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Contract Inventory

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Contract_ID |
| B | Vendor_ID |
| C | Contract_Name |
| D | Contract_Type |
| E | Start_Date |
| F | End_Date |
| G | Project_Classification |
| H | Contract_Value_CHF |
| I | Primary_Contact |
| J | Legal_Review_Date |
| K | Security_Review_Date |
| L | Status |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D2:D100 | `type_dv` |
| G | G2:G100 | `class_dv` |
| L | L2:L100 | `status_dv` |

---

## Sheet 3: Security Clauses

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Contract_ID |
| B | Clause_Category |
| C | Clause_Description |
| D | Included |
| E | Clause_Reference |
| F | Modification_Notes |
| G | Reviewed_By |
| H | Review_Date |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D2:D100 | `included_dv` |

---

## Sheet 4: SLA Compliance

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | SLA_ID |
| B | Contract_ID |
| C | Vulnerability_ID |
| D | Severity |
| E | Discovery_Date |
| F | SLA_Days |
| G | SLA_Due_Date |
| H | Remediation_Date |
| I | SLA_Met |
| J | Exception_Approved |
| K | Exception_Approver |
| L | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D2:D100 | `severity_dv` |
| F | F2:F100 | `sla_days_dv` |
| I | I2:I100 | `met_dv` |
| J | J2:J100 | `exception_dv` |

---

## Sheet 5: Subcontractor Approvals

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Approval_ID |
| B | Contract_ID |
| C | Primary_Vendor_ID |
| D | Subcontractor_Name |
| E | Subcontractor_Scope |
| F | Access_Level |
| G | Assessment_Level |
| H | Risk_Classification |
| I | Approval_Status |
| J | Approved_By |
| K | Approval_Date |
| L | Expiry_Date |
| M | Flow_Down_Verified |
| N | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| F | F2:F100 | `access_dv` |
| G | G2:G100 | `assess_dv` |
| H | H2:H100 | `risk_dv` |
| I | I2:I100 | `status_dv` |
| M | M2:M100 | `yn_dv` |

---

## Sheet 6: Termination Checklist

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Contract_ID |
| B | Termination_Type |
| C | Termination_Date |
| D | Check_Item |
| E | Status |
| F | Completion_Date |
| G | Verified_By |
| H | Evidence_Reference |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B2:B100 | `type_dv` |
| E | E2:E100 | `status_dv` |

---

**END OF SPECIFICATION**

---

*"A verbal contract isn't worth the paper it's written on."*
— Samuel Goldwyn

<!-- QA_VERIFIED: 2026-02-06 -->
