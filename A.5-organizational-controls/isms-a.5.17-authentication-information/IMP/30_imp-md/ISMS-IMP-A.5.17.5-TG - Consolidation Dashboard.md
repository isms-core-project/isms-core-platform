**ISMS-IMP-A.5.17.5-TG - Consolidation Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.17

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.17.5-TG |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.17 (Authentication Information) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.17 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.17 (Authentication Information Policy)
- ISMS-IMP-A.5.17.1 (Password Policy Implementation Guide)
- ISMS-IMP-A.5.17.2 (MFA Deployment Assessment)
- ISMS-IMP-A.5.17.3 (Authentication Management Procedures)
- ISMS-IMP-A.5.17.4 (Compliance and Audit Dashboard)

---

# Technical Specification


> Auto-generated from `generate_a517_5_consolidation_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.17.5` |
| **Output Filename** | `ISMS-IMP-A.5.17.5_Consolidation_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Consolidation Dashboard |
| **Total Sheets** | 12 (12 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #002060 | 002060 | Custom |
| #1F4E79 | 1F4E79 | Custom |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Executive_Summary

### Columns

| Col | Header |
|-----|--------|
| A | Domain |
| B | Workbook |
| C | Status |
| D | Score % |
| E | Critical Gaps |
| F | Last Updated |

---

## Sheet 3: Domain_Overview

**Data Rows:** 4 (rows 2–5)

### Columns

| Col | Header |
|-----|--------|
| A | Requirement |
| B | Status |
| C | Evidence Ref |
| D | Gap Description |
| E | Remediation |

---

## Sheet 4: Policy_Compliance

**Data Rows:** 6 (rows 3–8)

### Columns

| Col | Header |
|-----|--------|
| A | Policy_Element |
| B | Requirement |
| C | Implementation_Status |
| D | Evidence_Ref |
| E | Last_Review |
| F | Compliance_Status |
| G | Gap_Notes |
| H | Owner |

---

## Sheet 5: Lifecycle_Compliance

**Data Rows:** 7 (rows 2–8)

### Columns

| Col | Header |
|-----|--------|
| A | Lifecycle_Phase |
| B | Process_Defined |
| C | Automation_Status |
| D | Audit_Trail |
| E | SLA_Compliance |
| F | Compliance_Status |
| G | Gap_Notes |
| H | Owner |

---

## Sheet 6: System_Compliance

**Data Rows:** 7 (rows 2–8)

### Columns

| Col | Header |
|-----|--------|
| A | System_Name |
| B | Auth_Method |
| C | MFA_Enabled |
| D | Storage_Security |
| E | Last_Assessed |
| F | Compliance_Status |
| G | Gap_Notes |
| H | Owner |

---

## Sheet 7: Cross_Domain_Gaps

**Data Rows:** 15 (rows 4–18)

### Columns

| Col | Header |
|-----|--------|
| A | Gap_ID |
| B | Source_Domain |
| C | Gap_Description |
| D | Risk_Rating |
| E | Priority |
| F | Affected_Controls |
| G | Root_Cause |
| H | Remediation_Action |
| I | Owner |
| J | Target_Date |

---

## Sheet 8: Remediation_Tracker

**Data Rows:** 15 (rows 4–18)

### Columns

| Col | Header |
|-----|--------|
| A | Action_ID |
| B | Related_Gap |
| C | Source_Domain |
| D | Action_Description |
| E | Priority |
| F | Owner |
| G | Start_Date |
| H | Target_Date |
| I | Status |
| J | Progress_% |
| K | Notes |

---

## Sheet 9: KPI_Summary

### Columns

| Col | Header |
|-----|--------|
| A | KPI |
| B | Target |
| C | Current |
| D | Previous |
| E | Trend |
| F | Status |

---

## Sheet 10: Evidence_Index

**Data Rows:** 15 (rows 4–18)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_ID |
| B | Source_Workbook |
| C | Source_Sheet |
| D | Evidence_Type |
| E | Evidence_Description |
| F | Location/Reference |
| G | Date_Captured |
| H | Validation_Status |

---

## Sheet 11: Trend_Dashboard

**Data Rows:** 7 (rows 2–8)

### Columns

| Col | Header |
|-----|--------|
| A | Period |
| B | Policy % |
| C | Lifecycle % |
| D | Systems % |
| E | Overall % |
| F | MFA Adoption |
| G | Incidents |
| H | Notes |

---

## Sheet 12: Approval_SignOff

**Data Rows:** 4 (rows 2–5)

### Columns

| Col | Header |
|-----|--------|
| A | Role |
| B | Name |
| C | Date |
| D | Signature |
| E | Comments |

---

**END OF SPECIFICATION**

---

*"Identity is the new perimeter."*
— John Kindervag

<!-- QA_VERIFIED: 2026-02-06 -->
