**ISMS-IMP-A.5.1-2-6.1-2.S5-TG - Governance Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.1, A.5.2, A.6.1, A.6.2: Stacked Control Consolidation

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Governance Compliance Dashboard |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S5-TG |
| **Related Policy** | ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.1, A.5.2, A.6.1, A.6.2 (Stacked Control Consolidation) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle:** Quarterly (aligned with source assessments)
**Next Review Date:** [Effective Date + 90 days]

**Source Assessments (MANDATORY prerequisites — all must be approved before this dashboard is populated):**
- ISMS-IMP-A.5.1-2-6.1-2.S1 — Policy Framework Assessment (Control A.5.1)
- ISMS-IMP-A.5.1-2-6.1-2.S2 — Roles & Responsibilities Assessment (Control A.5.2)
- ISMS-IMP-A.5.1-2-6.1-2.S3 — Screening & Vetting Assessment (Control A.6.1)
- ISMS-IMP-A.5.1-2-6.1-2.S4 — Employment Contract Assessment (Controls A.6.2, A.6.5)

**Related Documents:**
- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles)
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.8.12 (Data Leakage Prevention) — monitoring transparency context
- Swiss Federal Data Protection Act (FADP / nDSG) — Articles 6, 19, 22
- ISO/IEC 27001:2022 Clause 9.3 (Management Review)

---

# Technical Specification
**Audience:** Workbook Developers (Python/Excel script maintainers)


> Auto-generated from `generate_a5_1_2_6_1_2_s5_governance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.1-2-6.1-2.S5` |
| **Output Filename** | `ISMS-IMP-A.5.1-2-6.1-2.S5_Governance_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Governance Compliance Dashboard |
| **Total Sheets** | 11 (11 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #7030A0 | 7030A0 | Purple (Exception) |
| #92D050 | 92D050 | Green (Complete) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #DCE6F1 | DCE6F1 | Pale Blue (Info) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFFF00 | FFFF00 | Yellow (Warning) |

## Sheet 1: Instructions_Legend

**Purpose:** Navigation guide, color coding, dropdown reference.

**Data Rows:** 3 (rows 5–7)

### Columns

| Col | Header |
|-----|--------|
| A | # |
| B | Sheet Name |
| C | Description |

---

## Sheet 2: Executive_Summary

**Purpose:** Board-facing single-page summary with weighted compliance score.

**Data Rows:** 4 (rows 14–17)

### Columns

| Col | Header |
|-----|--------|
| A | Domain |
| B | Weight |
| C | Raw Score |
| D | Weighted Score |
| E | Status |
| F | Source Workbook |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| E6 | `=ROUND((Policy_Summary!B20*0.35)+(Roles_Summary!B20*0.25)+(Screening_Summary!B20` |  |
| I6 | `=IF(Screening_Summary!B22=` |  |
| EN | `=IF(C{i}>=0.9,` |  |
| D18 | `=SUM(D14:D17)` |  |
| DN | `=IF(B{i}>=VALUE(SUBSTITUTE(C{i},` |  |

---

## Sheet 3: Maturity_Assessment

**Purpose:** 5-level maturity model + trend analysis.

**Data Rows:** 5 (rows 33–37)

### Columns

| Col | Header |
|-----|--------|
| A | Domain |
| B | Control |
| C | Current Level |
| D | Target Level |
| E | Gap |
| F | Trend |
| G | Priority |
| H | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C17:D20 | `level_dv` |
| F | F17:F20 | `trend_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IF(AND(C{i}<>` |  |
| GN | `=IF(E{i}=` |  |
| B25 | `=AVERAGE(C17:C20)` |  |
| B26 | `=AVERAGE(D17:D20)` |  |
| B27 | `=B26-B25` |  |
| FN | `=IF(B{row}<>` |  |

---

## Sheet 4: Policy_Summary

**Purpose:** S1 (A.5.1) domain metrics from Policy Framework Assessment.

### Columns

| Col | Header |
|-----|--------|
| A | Domain |
| B | Weight |
| C | Score |
| D | Status |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=IF(C{i}=` |  |
| B24 | `=B20` | Link to overall score |

---

## Sheet 5: Roles_Summary

**Purpose:** S2 (A.5.2) domain metrics from Roles & Responsibilities Assessment.

### Columns

| Col | Header |
|-----|--------|
| A | Domain |
| B | Weight |
| C | Score |
| D | Status |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=IF(C{i}=` |  |

---

## Sheet 6: Screening_Summary

**Purpose:** S3 (A.6.1) domain metrics + FADP indicator.

**Data Rows:** 6 (rows 24–29)

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B24:B29 | `fadp_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| B24 | `=B10/(B9)*100` | This links to the screening rate |

---

## Sheet 7: Contract_Summary

**Purpose:** S4 (A.6.2/A.6.5) domain metrics + NDA focal point.

### Columns

| Col | Header |
|-----|--------|
| A | Domain |
| B | Weight |
| C | Score |
| D | Status |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=IF(C{i}=` |  |

---

## Sheet 8: Gap_Analysis

**Purpose:** Consolidated gaps with cross-domain flags.

**Data Rows:** 100 (rows 11–110) | **Frozen Panes:** A12

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap_ID | 12 |
| B | Source_Workbook | 15 |
| C | Primary_Control | 12 |
| D | Gap_Title | 30 |
| E | Gap_Description | 40 |
| F | Risk_Level | 12 |
| G | Affected_Domains | 20 |
| H | Cross_Domain_Flag | 15 |
| I | Remediation_Action | 35 |
| J | Owner | 20 |
| K | Target_Date | 12 |
| L | Status | 15 |
| M | FADP_Relevant | 12 |
| N | Notes | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B12:B110 | `source_dv` |
| C | C12:C110 | `control_dv` |
| F | F12:F110 | `risk_dv` |
| L | L12:L110 | `status_dv` |
| M | M12:M110 | `fadp_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| B50 | `=COUNTIF(H11:H110,` |  |
| B51 | `=B50` |  |
| AN | `=IF(D{row}<>` |  |
| HN | `=IF(G{row}=` |  |

---

## Sheet 9: Evidence_Register

**Purpose:** Consolidated evidence index from all S1-S4 workbooks.

**Data Rows:** 150 (rows 5–154) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence_ID | 12 |
| B | Source_Workbook | 15 |
| C | Evidence_Type | 20 |
| D | Description | 40 |
| E | Related_Control | 12 |
| F | Related_Gap_ID | 12 |
| G | File_Location | 40 |
| H | Date_Collected | 12 |
| I | Collected_By | 20 |
| J | Verification_Status | 15 |
| K | Notes | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B5:B154 | `source_dv` |
| C | C5:C154 | `evidence_type_dv` |
| E | E5:E154 | `control_dv` |
| J | J5:J154 | `verification_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(D{row}<>` |  |

---

## Sheet 10: Action_Items

**Purpose:** Remediation tracker linked to Gap_Analysis.

**Data Rows:** 100 (rows 10–109) | **Frozen Panes:** A11

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Action_ID | 12 |
| B | Related_Gap_ID | 12 |
| C | Action_Description | 40 |
| D | Priority | 12 |
| E | Owner | 20 |
| F | Target_Date | 12 |
| G | Status | 15 |
| H | Progress_% | 12 |
| I | Last_Update | 12 |
| J | Update_Notes | 30 |
| K | Blocking_Issues | 30 |
| L | Escalation_Required | 15 |
| M | Escalation_To | 20 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D11:D109 | `priority_dv` |
| G | G11:G109 | `status_dv` |
| L | L11:L109 | `escalation_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{row}<>` |  |

---

## Sheet 11: Approval_Sign_Off

**Purpose:** Three-level governance certification with FADP acknowledgment.

**Data Rows:** 3 (rows 53–55)

---

**END OF SPECIFICATION**

---

*"Governance is the art of making decisions that stick."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
