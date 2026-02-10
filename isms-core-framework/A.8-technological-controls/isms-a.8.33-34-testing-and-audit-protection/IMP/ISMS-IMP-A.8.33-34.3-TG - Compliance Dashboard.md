<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.33-34.3-TG:framework:TG:a.8.33-34.3 -->
**ISMS-IMP-A.8.33-34.3-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of Information Systems During Audit Testing

### ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of Information Systems During Audit Testing

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.33-34.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Compliance Dashboard & Consolidated Oversight |
| **Related Policy** | ISMS-POL-A.8.33-34 (All Sections) |
| **Purpose** | Consolidate all domain assessments into executive compliance view with scoring, gap analysis, exception tracking, and audit readiness certification |
| **Target Audience** | CISO, Executive Management, Board of Directors, Internal/External Auditors, ISO 27001 Certification Bodies, Workbook Developers |
| **Assessment Type** | Executive Dashboard & Consolidation |
| **Review Cycle** | Quarterly (synchronized with domain assessments) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial technical specification for Testing and Audit Protection Compliance Dashboard workbook | ISMS Implementation Team |

---


> Auto-generated from `generate_a83334_3_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.33-34.3` |
| **Output Filename** | `ISMS-IMP-A.8.33-34.3_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance Dashboard |
| **Total Sheets** | 10 (10 visible) |
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

## Sheet 1: Executive_Dashboard

**Data Rows:** 12 (rows 25–36)

### Columns

| Col | Header |
|-----|--------|
| A | Assessment Area |
| B | Compliance % |
| C | Status |
| D | Critical Gaps |
| E | Evidence Count |
| F | Last Updated |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C18:C20 | `status_dv` |
| E | E25:E36 | `trend_dv` |

---

## Sheet 2: Test_Data_Compliance

**Data Rows:** 45 (rows 6–50)

### Columns

| Col | Header |
|-----|--------|
| A | Metric |
| B | Target |
| C | Current |
| D | Status |
| E | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D6:D50 | `status_dv` |

---

## Sheet 3: Audit_Activity_Compliance

**Data Rows:** 65 (rows 6–70)

### Columns

| Col | Header |
|-----|--------|
| A | Metric |
| B | Target |
| C | Current |
| D | Status |
| E | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D6:D70 | `status_dv` |

---

## Sheet 4: Gap_Analysis

**Data Rows:** 50 (rows 6–55)

### Columns

| Col | Header |
|-----|--------|
| A | Gap_ID |
| B | Gap_Description |
| C | Area |
| D | Severity |
| E | Current_State |
| F | Target_State |
| G | Owner |
| H | Target_Date |
| I | Status |
| J | Evidence |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D6:D55 | `severity_dv` |
| D | D58:D107 | `severity_dv` |
| I | I6:I55 | `status_dv` |
| I | I58:I107 | `status_dv` |

---

## Sheet 5: Exception_Register

**Data Rows:** 30 (rows 5–34)

### Columns

| Col | Header |
|-----|--------|
| A | Exception_ID |
| B | Exception_Title |
| C | Policy_Requirement |
| D | Assessment_Source |
| E | Business_Justification |
| F | Risk_Assessment |
| G | Compensating_Controls |
| H | Requested_By |
| I | Request_Date |
| J | Approval_Status |
| K | Approved_By |
| L | Approval_Date |
| M | Expiration_Date |
| N | Renewal_Required |
| O | Risk_Level |
| P | Risk_Owner |
| Q | Review_Date |
| R | Next_Review |
| S | Evidence_Reference |
| T | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D5:D34 | `source_dv` |
| J | J5:J34 | `status_dv` |
| N | N5:N34 | `yn_dv` |
| O | O5:O34 | `risk_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B5:B34)` | Total Exceptions |
| — | `=COUNTIF(J5:J34,` | Approved Exceptions |
| — | `=COUNTIF(O5:O34,` | High Risk Exceptions |

---

## Sheet 6: KPIs_and_Metrics

**Data Rows:** 25 (rows 6–30)

### Columns

| Col | Header |
|-----|--------|
| A | KPI |
| B | Target |
| C | Q1 |
| D | Q2 |
| E | Q3 |
| F | Q4 |
| G | Current |
| H | Status |
| I | Trend |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| H | H6:H30 | `status_dv` |
| I | I6:I30 | `trend_dv` |

---

## Sheet 7: Remediation_Roadmap

**Data Rows:** 60 (rows 14–73)

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C14:C73 | `priority_dv` |
| D | D14:D73 | `source_dv` |
| H | H14:H73 | `status_dv` |

---

## Sheet 8: Evidence_Consolidation

**Data Rows:** 200 (rows 5–204)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_ID |
| B | Source_Assessment |
| C | Evidence_Type |
| D | Description |
| E | Location |
| F | Date_Collected |
| G | Collected_By |
| H | Verification_Status |
| I | Auditor_Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B5:B204 | `source_dv` |
| C | C5:C204 | `type_dv` |
| H | H5:H204 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(B5:B204)` | Total Evidence |
| — | `=COUNTIF(B5:B204,` | From Test Data Assessment |
| — | `=COUNTIF(H5:H204,` | Verified |

---

## Sheet 9: CISO_Certification

---

## Sheet 10: Approval_Sign_Off

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
