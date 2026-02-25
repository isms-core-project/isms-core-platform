<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.1-2-6.1-2.S3-TG:framework:TG:a.5.1-2-6.1-2 -->
**ISMS-IMP-A.5.1-2-6.1-2.S3-TG - Screening & Vetting Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.1: Screening

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Screening & Vetting Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S3-TG |
| **Related Policy** | ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.1 (Screening) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO / Chief Human Resources Officer (CHRO) — joint ownership |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:
- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) — Section 6 (Screening & Vetting Requirements)
- ISMS-IMP-A.5.1-2-6.1-2.S1 (Policy Framework Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S2 (Roles & Responsibilities Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S4 (Employment Contract Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S5 (Governance Compliance Dashboard)
- Swiss Federal Data Protection Act (FADP / nDSG) — Articles 4, 6, 7, 22, 25
- Swiss Code of Obligations (OR) — Article 328b

**Note on Naming Convention**: The ".S" designation indicates this implementation is part of a **stacked control framework** (A.5.1 + A.5.2 + A.6.1 + A.6.2). Despite unified implementation, each control maintains distinct requirements for Statement of Applicability purposes.

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a5_1_2_6_1_2_s3_screening_vetting.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.1-2-6.1-2.S3` |
| **Output Filename** | `ISMS-IMP-A.5.1-2-6.1-2.S3_Screening_Vetting_Assessment_Workbook_YYYYMMDD.xlsx` |
| **Workbook Title** | Screening Vetting Assessment Workbook |
| **Total Sheets** | 10 (10 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #92D050 | 92D050 | Green (Complete) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #DCE6F1 | DCE6F1 | Pale Blue (Info) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFFF00 | FFFF00 | Yellow (Warning) |

## Sheet 1: Dashboard

**Purpose:** Auto-calculated metrics pulling from other sheets.

**Data Rows:** 6 (rows 32–37)

### Columns

| Col | Header |
|-----|--------|
| A | Domain |
| B | Weight |
| C | Score (%) |
| D | Weighted Score |
| E | Status |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=IF(B{0}>=C{0},` |  |
| EN | `=IF(C{row_num}>=0.9,` |  |
| C38 | `=SUM(D32:D37)` |  |

---

## Sheet 2: Screening_Process_Assessment

**Purpose:** Screening process documentation verification.

**Data Rows:** 40 (rows 5–44) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Process_ID | 15 |
| B | Process_Name | 35 |
| C | Process_Owner | 25 |
| D | Documented | 12 |
| E | Document_Location | 35 |
| F | Last_Review_Date | 15 |
| G | Process_Implemented | 15 |
| H | Implementation_Evidence | 35 |
| I | Compliance_Status | 15 |
| J | Provider_Governed | 12 |
| K | Gap_Description | 40 |
| L | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D5:D44 | `documented_dv` |
| G | G5:G44 | `implemented_dv` |
| I | I5:I44 | `compliance_dv` |
| J | J5:J44 | `provider_dv` |

---

## Sheet 3: Screening_Level_Matrix

**Purpose:** Role tier to screening level mapping.

**Data Rows:** 26 (rows 5–30) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Role_Tier | 15 |
| B | Role_Category | 30 |
| C | Example_Roles | 40 |
| D | Required_Screening_Level | 20 |
| E | Identity_Check | 12 |
| F | Employment_History | 12 |
| G | Criminal_Check | 12 |
| H | Credit_Check | 12 |
| I | Mapping_Documented | 12 |
| J | Gap_Description | 40 |
| K | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D5:D30 | `screening_level_dv` |
| E | E5:H30 | `yes_no_req_dv` |
| I | I5:I30 | `documented_dv` |

---

## Sheet 4: Personnel_Screening_Registry

**Purpose:** Master registry: all personnel screening status.

**Data Rows:** 250 (rows 5–254) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Employee_ID | 15 |
| B | Full_Name | 25 |
| C | Department | 20 |
| D | Job_Title | 25 |
| E | Role_Tier | 12 |
| F | Employment_Type | 15 |
| G | Start_Date | 12 |
| H | Required_Screening_Level | 15 |
| I | Actual_Screening_Level | 15 |
| J | Screening_Complete | 12 |
| K | Screening_Date | 12 |
| L | Screening_Expiry | 12 |
| M | Screening_Provider | 20 |
| N | Consent_Obtained | 12 |
| O | Consent_Date | 12 |
| P | Screening_Status | 15 |
| Q | Gap_Identified | 15 |
| R | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E5:E254 | `tier_dv` |
| F | F5:F254 | `emp_type_dv` |
| H | H5:I254 | `screening_level_dv` |
| J | J5:J254 | `complete_dv` |
| N | N5:N254 | `consent_dv` |

---

## Sheet 5: Screening_Compliance_Verif

**Purpose:** Per-person compliance gap identification.

**Data Rows:** 250 (rows 5–254) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Employee_ID | 15 |
| B | Full_Name | 25 |
| C | Role_Tier | 12 |
| D | Identity_Verified | 12 |
| E | Employment_History_Checked | 12 |
| F | Education_Verified | 12 |
| G | Criminal_Check_Complete | 12 |
| H | Credit_Check_Complete | 12 |
| I | References_Checked | 12 |
| J | Right_to_Work_Verified | 12 |
| K | All_Required_Checks_Complete | 15 |
| L | Screening_Level_Appropriate | 15 |
| M | Compliance_Status | 15 |
| N | Gap_Description | 40 |
| O | Evidence_Reference | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D5:J254 | `check_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(ROW()-4<=COUNTA(Personnel_Screening_Registry!$A:$A)-4,INDEX(Personnel_Screen` |  |
| BN | `=IF(A{row}<>` |  |

---

## Sheet 6: Continuous_Screening_Assessment

**Purpose:** Re-screening schedule and compliance.

**Data Rows:** 250 (rows 5–254) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Employee_ID | 15 |
| B | Full_Name | 25 |
| C | Role_Tier | 12 |
| D | Initial_Screening_Date | 15 |
| E | Re_Screening_Interval | 15 |
| F | Last_Re_Screening_Date | 15 |
| G | Next_Re_Screening_Due | 15 |
| H | Re_Screening_Status | 15 |
| I | Trigger_Event_Occurred | 15 |
| J | Trigger_Event_Details | 30 |
| K | Continuous_Monitoring_Active | 15 |
| L | Compliance_Status | 15 |
| M | Gap_Description | 40 |
| N | Evidence_Reference | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E5:E254 | `interval_dv` |
| I | I5:I254 | `trigger_dv` |
| K | K5:K254 | `monitoring_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(ROW()-4<=COUNTA(Personnel_Screening_Registry!$A:$A)-4,INDEX(Personnel_Screen` |  |
| BN | `=IF(A{row}<>` |  |

---

## Sheet 7: Legal_Compliance_Review

**Purpose:** FADP/GDPR screening legality verification.

**Data Rows:** 40 (rows 5–44) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Requirement_ID | 15 |
| B | Requirement_Category | 25 |
| C | Requirement_Description | 50 |
| D | Applicable_Regulation | 20 |
| E | Implementation_Status | 15 |
| F | Implementation_Evidence | 35 |
| G | Last_Review_Date | 15 |
| H | Responsible_Party | 25 |
| I | Compliance_Status | 15 |
| J | Gap_Description | 40 |
| K | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E5:E44 | `implementation_dv` |
| I | I5:I44 | `compliance_dv` |

---

## Sheet 8: Gap_Analysis

**Purpose:** Consolidated gaps from all assessment domains.

**Data Rows:** 150 (rows 5–154) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap_ID | 12 |
| B | Source_Sheet | 25 |
| C | Employee_ID | 15 |
| D | Gap_Category | 20 |
| E | Gap_Description | 40 |
| F | Risk_Level | 12 |
| G | Impact_Assessment | 35 |
| H | Affected_Stakeholders | 25 |
| I | Remediation_Action | 40 |
| J | Responsible_Party | 25 |
| K | Target_Completion_Date | 15 |
| L | Estimated_Effort | 15 |
| M | Dependencies | 30 |
| N | Status | 15 |
| O | Completion_Evidence | 30 |
| P | Risk_Acceptance | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B5:B154 | `source_dv` |
| D | D5:D154 | `category_dv` |
| F | F5:F154 | `risk_level_dv` |
| L | L5:L154 | `effort_dv` |
| N | N5:N154 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{row}=` |  |

---

## Sheet 9: Evidence_Register

**Purpose:** Supporting evidence documentation.

**Data Rows:** 200 (rows 5–204) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence_ID | 12 |
| B | Evidence_Type | 25 |
| C | Description | 40 |
| D | Related_Employee_ID | 15 |
| E | Related_Assessment_Sheet | 25 |
| F | File_Location | 40 |
| G | Date_Collected | 12 |
| H | Collected_By | 25 |
| I | Verification_Status | 15 |
| J | Retention_Date | 12 |
| K | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B5:B204 | `evidence_type_dv` |
| E | E5:E204 | `sheet_dv` |
| I | I5:I204 | `verification_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{row}=` |  |

---

## Sheet 10: Approval_Sign_Off

**Purpose:** Three-level approval workflow.

---

**END OF SPECIFICATION**

---

*"Trust is earned through verification."*
— Security Maxim

<!-- QA_VERIFIED: 2026-02-06 -->
