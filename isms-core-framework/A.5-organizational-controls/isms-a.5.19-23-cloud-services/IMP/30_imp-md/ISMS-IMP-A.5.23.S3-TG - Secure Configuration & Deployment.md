**ISMS-IMP-A.5.23.S3-TG - Secure Configuration & Deployment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Secure Configuration & Deployment |
| **Related Policy** | ISMS-POL-A.5.19-23-S5 (Cloud Services Security - Sections 5, 9) |
| **Purpose** | Assess and document secure configuration of cloud services across identity, data protection, network, logging, backup, and jurisdictional risk controls |
| **Target Audience** | IT Operations, Cloud Operations, DevOps Engineers, Cloud Security Engineers, Platform Engineering |
| **Assessment Type** | Technical Configuration Assessment |
| **Review Cycle** | Quarterly (with continuous monitoring) |
| **Date** | [Date to be set] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial Excel workbook specification | ISMS Implementation Team |

---


> Auto-generated from `generate_reg_a523_3_secure_config.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.23.S3` |
| **Output Filename** | `ISMS-IMP-A.5.23.S3_Secure_Configuration_&_Deployment_YYYYMMDD.xlsx` |
| **Workbook Title** | Secure Configuration & Deployment |
| **Total Sheets** | 23 (23 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #FF0000 | color | Red (Critical/Alert) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | end_color | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: 2. Configuration Baseline

---

## Sheet 3: 3. Access Control Setup

---

## Sheet 4: 4. Network Security

---

## Sheet 5: 5. Encryption Configuration

---

## Sheet 6: 6. Deployment Checklist

---

## Sheet 7: 7. Jurisdictional Risk

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Assessment_ID | 14 |
| B | Cloud_Service_Name | 25 |
| C | Provider_Name | 22 |
| D | Provider_HQ_Country | 18 |
| E | Provider_HQ_Jurisdiction | 20 |
| F | US_Parent_Company | 14 |
| G | CLOUD_Act_Applicability | 20 |
| H | Data_Processing_Locations | 25 |
| I | EU_Data_Boundary_Available | 18 |
| J | Customer_Managed_Keys | 16 |
| K | Legal_Challenge_Commitment | 18 |
| L | Adequacy_Decision_Status | 18 |
| M | Transfer_Mechanism | 16 |
| N | Risk_Level | 14 |
| O | Risk_Accepted_By | 18 |
| P | Risk_Acceptance_Date | 16 |
| Q | Compensating_Controls | 28 |
| R | Review_Date | 14 |
| S | Evidence_Reference | 20 |
| T | Notes | 30 |

---

## Sheet 8: 8. Summary Dashboard

---

## Sheet 9: 9. Evidence Register

---

## Sheet 10: 10. Approval Sign-Of

---

## Sheet 11: Instructions

**Frozen Panes:** A4

---

## Sheet 12: 2_Configuration_Baseline

---

## Sheet 13: 3_Access_Control

---

## Sheet 14: 4_Network_Security

---

## Sheet 15: 5_Encryption_Config

---

## Sheet 16: 6_Deployment_Checklist

---

## Sheet 17: 7_Jurisdictional_Risk

**Data Rows:** 25 (rows 6–30) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Assessment_ID | 14 |
| B | Cloud_Service_Name | 25 |
| C | Provider_Name | 22 |
| D | Provider_HQ_Country | 18 |
| E | Provider_HQ_Jurisdiction | 20 |
| F | US_Parent_Company | 14 |
| G | CLOUD_Act_Applicability | 20 |
| H | Data_Processing_Locations | 25 |
| I | EU_Data_Boundary_Available | 18 |
| J | Customer_Managed_Keys | 16 |
| K | Legal_Challenge_Commitment | 18 |
| L | Adequacy_Decision_Status | 18 |
| M | Transfer_Mechanism | 16 |
| N | Risk_Level | 14 |
| O | Risk_Accepted_By | 18 |
| P | Risk_Acceptance_Date | 16 |
| Q | Compensating_Controls | 28 |
| R | Review_Date | 14 |
| S | Evidence_Reference | 20 |
| T | Notes | 30 |

---

## Sheet 18: 8_Summary_Dashboard

**Data Rows:** 26 (rows 5–30) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Configuration Area |
| B | Total Items |
| C | {...} Compliant |
| D | {...} Partial |
| E | {...} Non-Compliant |
| F | N/A |
| G | Compliance % |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIF(` | US-HQ Providers (CLOUD Act Scope) |
| — | `=COUNTIFS(` | CLOUD Act Mitigated |

---

## Sheet 19: 9_Evidence_Register

**Data Rows:** 37 (rows 4–40) | **Frozen Panes:** A4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 18 |
| B | Cloud Service Name | 25 |
| C | Configuration Area | 22 |
| D | Evidence Type | 25 |
| E | Description | 35 |
| F | File Location | 35 |
| G | Capture Date | 16 |
| H | Captured By | 18 |
| I | Status | 14 |

---

## Sheet 20: 10_Approval_Signoff

**Frozen Panes:** A3

---

## Sheet 21: Base_Validations

---

## Sheet 22: Regulatory_Validations

---

## Sheet 23: Config_Assessment

**Data Rows:** 26 (rows 5–30)

---

**END OF SPECIFICATION**

---

*"Know how to solve every problem that has been solved."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
