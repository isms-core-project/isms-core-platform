<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.30.1-TG:framework:TG:a.8.30.1 -->
**ISMS-IMP-A.8.30.1-TG - Vendor Assessment and Registry**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.30: Outsourced Development

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.1-TG |
| **Document Title** | Vendor Assessment and Registry Workbook Specification |
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


> Auto-generated from `generate_a830_1_vendor_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.30.1` |
| **Output Filename** | `ISMS-IMP-A.8.30.1_Vendor_Assessment_and_Registry_YYYYMMDD.xlsx` |
| **Workbook Title** | Vendor Assessment and Registry |
| **Total Sheets** | 5 (5 visible) |
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

## Sheet 2: Vendor Registry

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Vendor_ID |
| B | Vendor_Name |
| C | Registry_Status |
| D | Risk_Tier |
| E | Initial_Assessment_Date |
| F | Last_Assessment_Date |
| G | Next_Assessment_Due |
| H | ISO_27001_Certified |
| I | SOC2_Type2 |
| J | Primary_Contact |
| K | Approved_Project_Types |
| L | Approved_By |
| M | Notes |

---

## Sheet 3: Security Assessment

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Assessment_ID |
| B | Vendor_ID |
| C | Assessment_Date |
| D | Assessment_Type |
| E | Assessor |
| F | Security_Certification |
| G | Cert_Expiry_Date |
| H | SDLC_Maturity |
| I | Security_Incident_History |
| J | SAST_DAST_Tooling |
| K | Personnel_Screening |
| L | Dev_Environment_Security |
| M | Overall_Risk_Rating |
| N | Recommendation |
| O | Conditions |
| P | Evidence_Location |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D2:D100 | `type_dv` |
| F | F2:F100 | `cert_dv` |
| H | H2:H100 | `maturity_dv` |
| I | I2:I100 | `incident_dv` |
| K | K2:K100 | `screening_dv` |
| L | L2:L100 | `env_dv` |
| M | M2:M100 | `risk_dv` |
| N | N2:N100 | `rec_dv` |

---

## Sheet 4: Due Diligence

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Vendor_ID |
| B | Check_Category |
| C | Check_Item |
| D | Status |
| E | Evidence_Type |
| F | Evidence_Reference |
| G | Verified_By |
| H | Verified_Date |
| I | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D2:D100 | `status_dv` |
| E | E2:E100 | `evidence_dv` |

---

## Sheet 5: Environment Security

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Vendor_ID |
| B | Assessment_Date |
| C | MFA_Enabled |
| D | Network_Isolation |
| E | Endpoint_Security |
| F | Code_Repository |
| G | Secret_Scanning |
| H | Branch_Protection |
| I | Data_Handling |
| J | Attestation_Received |
| K | Attestation_Date |
| L | Compliance_Status |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| G | G2:G100 | `yn_dv` |
| J | J2:J100 | `yn_dv` |
| C | C2:C100 | `ynp_dv` |
| H | H2:H100 | `ynp_dv` |
| D | D2:D100 | `network_dv` |
| E | E2:E100 | `endpoint_dv` |
| F | F2:F100 | `repo_dv` |
| I | I2:I100 | `data_dv` |
| L | L2:L100 | `compliance_dv` |

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
