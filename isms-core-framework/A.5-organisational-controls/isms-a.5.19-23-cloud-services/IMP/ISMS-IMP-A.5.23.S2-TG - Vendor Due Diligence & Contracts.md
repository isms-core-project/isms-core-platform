<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.23.S2-TG:framework:TG:a.5.23 -->
**ISMS-IMP-A.5.23.S2-TG - Vendor Due Diligence & Contracts**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Vendor Due Diligence & Contracts |
| **Related Policy** | ISMS-POL-A.5.19-23-S2 (Supplier Agreement Requirements), ISMS-POL-A.5.19-23-S5 (Cloud Services Security) |
| **Purpose** | Assess vendor security posture, contract adequacy, SLA compliance, data sovereignty, audit rights, and jurisdictional risks for all cloud service providers |
| **Target Audience** | Legal, Procurement, Security Teams, Compliance Officers, Risk Managers |
| **Assessment Type** | Vendor Due Diligence & Contract Analysis |
| **Review Cycle** | Quarterly (with annual comprehensive review) |
| **Date** | [Date to be set] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial Excel workbook specification | ISMS Implementation Team |

---


> Auto-generated from `generate_reg_a523_2_vendor_dd.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.23.S2` |
| **Output Filename** | `ISMS-IMP-A.5.23.S2_Vendor_Due_Diligence_&_Contracts_YYYYMMDD.xlsx` |
| **Workbook Title** | Vendor Due Diligence & Contracts |
| **Total Sheets** | 25 (25 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | end_color | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: 2. Security Certifications

---

## Sheet 3: 3. Contract Terms

---

## Sheet 4: 4. SLA Performance

---

## Sheet 5: 5. Data Sovereignty

---

## Sheet 6: 6. Forensics & Audit

---

## Sheet 7: 7. Jurisdictional Risk

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Assessment ID | 14 |
| B | Cloud Service Name | 25 |
| C | Provider Name | 22 |
| D | Provider HQ Country | 18 |
| E | Provider HQ Jurisdiction | 20 |
| F | US Parent Company | 14 |
| G | CLOUD Act Applicability | 20 |
| H | Data Processing Locations | 25 |
| I | EU Data Boundary Available | 18 |
| J | Customer Managed Keys | 16 |
| K | Legal Challenge Commitment | 18 |
| L | Adequacy Decision Status | 18 |
| M | Transfer Mechanism | 16 |
| N | Risk Level | 14 |
| O | Risk Accepted By | 18 |
| P | Risk Acceptance Date | 16 |
| Q | Compensating Controls | 28 |
| R | Review Date | 14 |
| S | Evidence Reference | 20 |
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

## Sheet 12: 2_Security_Certifications

---

## Sheet 13: 3_Contract_Terms

---

## Sheet 14: 4_Sla_Performance

---

## Sheet 15: 5_Data_Sovereignty

---

## Sheet 16: 6_Forensics_Audit

---

## Sheet 17: 7_Jurisdictional_Risk

**Purpose:** This sheet assesses jurisdictional risks for cloud providers, particularly

**Data Rows:** 24 (rows 7–30) | **Frozen Panes:** A6

### Columns

| Col | Header |
|-----|--------|
| A | ☐ |
| B | Requirement |
| C | Status |
| D | Evidence Type |

---

## Sheet 18: 8_Summary_Dashboard

**Data Rows:** 24 (rows 7–30) | **Frozen Panes:** A3

### Columns

| Col | Header |
|-----|--------|
| A | Assessment Area |
| B | Total Vendors |
| C | {...} Compliant |
| D | {...} Partial |
| E | {...} Non-Compliant |
| F | N/A |
| G | Compliance % |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIF(` | Restricted Data Outside Switzerland/EU |

---

## Sheet 19: 9_Evidence_Register

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 15 |
| B | Vendor Name | 25 |
| C | Evidence Type | 25 |
| D | Description | 40 |
| E | File Location / URL | 40 |
| F | Document Date | 14 |
| G | Expiry/Renewal Date | 16 |
| H | Document Owner | 20 |
| I | Status | 14 |
| J | Notes | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C5:C104 | `ev_type_dv` |
| I | I5:I104 | `status_dv` |

---

## Sheet 20: 10_Approval_Signoff

**Frozen Panes:** A3

---

## Sheet 21: Base_Validations

---

## Sheet 22: Extended_Validations_Certifications

---

## Sheet 23: Extended_Validations_Contracts

---

## Sheet 24: Jurisdictional_Validations

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Assessment ID | 14 |
| B | Cloud Service Name | 25 |
| C | Provider Name | 22 |
| D | Provider HQ Country | 18 |
| E | Provider HQ Jurisdiction | 20 |
| F | US Parent Company | 14 |
| G | CLOUD Act Applicability | 20 |
| H | Data Processing Locations | 25 |
| I | EU Data Boundary Available | 18 |
| J | Customer Managed Keys | 16 |
| K | Legal Challenge Commitment | 18 |
| L | Adequacy Decision Status | 18 |
| M | Transfer Mechanism | 16 |
| N | Risk Level | 14 |
| O | Risk Accepted By | 18 |
| P | Risk Acceptance Date | 16 |
| Q | Compensating Controls | 28 |
| R | Review Date | 14 |
| S | Evidence Reference | 20 |
| T | Notes | 30 |

---

## Sheet 25: Vendor_Assessment

**Data Rows:** 20 (rows 5–24)

### Columns

| Col | Header |
|-----|--------|
| A | ☐ |
| B | Requirement |
| C | Status |
| D | Evidence Type |

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `CLOUD_ACT_EXPOSURE` | No Exposure, Potential Exposure (US HQ), Mitigated (EU Data Boundary), Mitigated (Encryption + Ke... |
| `PROVIDER_HQ_JURISDICTION` | Switzerland, EU/EEA, United Kingdom, United States, Other Adequate Country, Non-Adequate Country |
| `RISK_LEVEL` | Low, Medium, High, Critical |
| `TRANSFER_MECHANISM` | SCCs, BCRs, Adequacy Decision, None, N/A |
| `YES_NO_PARTIAL_UNKNOWN` | Yes, No, Partial, Unknown |
| `YES_NO_PLANNED` | Yes, No, Planned |

---

**END OF SPECIFICATION**

---

*"The worthwhile problems are the ones you can really solve or help solve, the ones you can really contribute something to."*
--- Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
