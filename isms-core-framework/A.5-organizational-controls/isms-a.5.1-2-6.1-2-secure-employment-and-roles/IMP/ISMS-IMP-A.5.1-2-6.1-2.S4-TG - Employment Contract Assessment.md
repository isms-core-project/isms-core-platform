<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.1-2-6.1-2.S4-TG:framework:TG:a.5.1-2-6.1-2 -->
**ISMS-IMP-A.5.1-2-6.1-2.S4-TG - Employment Contract Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.2: Terms and Conditions of Employment

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Employment Contract Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S4-TG |
| **Related Policy** | ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.2 (Terms and Conditions of Employment) |
| **Linked Control** | ISO/IEC 27001:2022 Annex A.6.5 (Responsibilities at Termination or Change of Employment) |
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
- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) — Section 7 (Employment Contract Requirements)
- ISMS-IMP-A.5.1-2-6.1-2.S1 (Policy Framework Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S2 (Roles & Responsibilities Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S3 (Screening & Vetting Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S5 (Governance Compliance Dashboard)
- Swiss Code of Obligations (OR) — Articles 328, 328b, 730a
- Swiss Federal Data Protection Act (FADP / nDSG) — Articles 6, 19
- ISMS-POL-A.8.12 (Data Leakage Prevention) — Annex A (monitoring transparency in employment contracts)

**Note on Linked Controls**: This assessment covers both A.6.2 (what security obligations are IN the contract) and A.6.5 (that post-employment obligations are specified and enforced). These are assessed together because A.6.5 obligations (confidentiality surviving termination, IP assignment, device return) must be contractually established by A.6.2.

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers


> Auto-generated from `generate_a5_1_2_6_1_2_s4_employment_contract.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.1-2-6.1-2.S4` |
| **Output Filename** | `ISMS-IMP-A.5.1-2-6.1-2.S4_Employment_Contract_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Employment Contract Assessment |
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

**Data Rows:** 5 (rows 32–36)

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
| C38 | `=SUM(D32:D36)` |  |

---

## Sheet 2: Contract_Template_Assessment

**Purpose:** Verify contract templates are complete and current.

**Data Rows:** 50 (rows 5–54) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Template_ID | 15 |
| B | Template_Name | 35 |
| C | Template_Type | 20 |
| D | Personnel_Category | 20 |
| E | Current_Version | 12 |
| F | Version_Date | 12 |
| G | Last_Review_Date | 12 |
| H | Next_Review_Date | 12 |
| I | Security_Clauses_Count | 15 |
| J | Required_Clauses_Met | 15 |
| K | Legal_Review_Date | 12 |
| L | Legal_Approved | 15 |
| M | Compliance_Status | 15 |
| N | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C5:C54 | `type_dv` |
| D | D5:D54 | `category_dv` |
| J | J5:J54 | `yn_dv` |
| L | L5:L54 | `yn_dv` |

---

## Sheet 3: Required_Clause_Registry

**Purpose:** Master list of required security clauses and template coverage.

**Data Rows:** 50 (rows 5–54) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Clause_ID | 15 |
| B | Clause_Category | 20 |
| C | Clause_Title | 35 |
| D | Clause_Description | 50 |
| E | ISO_27001_Reference | 20 |
| F | Legal_Requirement | 20 |
| G | Mandatory_For | 25 |
| H | Coverage_Status | 15 |
| I | Templates_With_Clause | 25 |
| J | Gap_If_Missing | 40 |
| K | Last_Verified | 12 |
| L | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B5:B54 | `category_dv` |
| H | H5:H54 | `coverage_dv` |

---

## Sheet 4: Personnel_Contract_Compliance

**Purpose:** Per-person contract status verification.

**Data Rows:** 200 (rows 5–204) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Employee_ID | 15 |
| B | Employee_Name | 25 |
| C | Department | 20 |
| D | Role_Title | 25 |
| E | Employment_Type | 15 |
| F | Start_Date | 12 |
| G | Contract_Template_Used | 20 |
| H | Contract_Signed | 15 |
| I | Contract_Date | 12 |
| J | Contract_On_File | 15 |
| K | All_Clauses_Present | 15 |
| L | Screening_Complete | 15 |
| M | Background_Check_Date | 12 |
| N | Compliance_Status | 15 |
| O | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E5:E204 | `emp_type_dv` |
| H | H5:H204 | `yn_dv` |
| J | J5:J204 | `yn_dv` |
| K | K5:K204 | `yn_dv` |
| L | L5:L204 | `yn_dv` |

---

## Sheet 5: Confidentiality_NDA_Tracking

**Purpose:** NDA / confidentiality status per individual.

**Data Rows:** 200 (rows 5–204) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Employee_ID | 15 |
| B | Employee_Name | 25 |
| C | Department | 20 |
| D | NDA_Type | 20 |
| E | NDA_Version | 12 |
| F | Date_Signed | 12 |
| G | Expiration_Date | 12 |
| H | Covers_IP | 15 |
| I | Covers_Trade_Secrets | 15 |
| J | Covers_Post_Employment | 15 |
| K | NDA_Status | 15 |
| L | Renewal_Required | 15 |
| M | Document_Location | 30 |
| N | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D5:D204 | `nda_type_dv` |
| H | H5:H204 | `yn_dv` |
| I | I5:I204 | `yn_dv` |
| J | J5:J204 | `yn_dv` |
| L | L5:L204 | `renewal_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(ROW()-4<=COUNTA(Personnel_Contract_Compliance!$A:$A)-4,INDEX(Personnel_Contr` |  |
| BN | `=IF(A{row}<>` |  |

---

## Sheet 6: Post_Employment_Obligations

**Purpose:** Track individuals with ongoing post-employment obligations.

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Former_Employee_ID | 15 |
| B | Former_Employee_Name | 25 |
| C | Former_Department | 20 |
| D | Former_Role | 25 |
| E | Termination_Date | 12 |
| F | Termination_Type | 15 |
| G | Confidentiality_End_Date | 15 |
| H | Non_Compete_End_Date | 15 |
| I | Non_Solicit_End_Date | 15 |
| J | IP_Assignment_Perpetual | 15 |
| K | Assets_Returned | 15 |
| L | Exit_Interview_Complete | 15 |
| M | Obligation_Status | 15 |
| N | Monitoring_Required | 15 |
| O | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| F | F5:F104 | `term_type_dv` |
| J | J5:J104 | `yn_dv` |
| K | K5:K104 | `yn_dv` |
| L | L5:L104 | `yn_dv` |
| N | N5:N104 | `yn_dv` |

---

## Sheet 7: Contractor_Agreement_Assessment

**Purpose:** Third-party and contractor agreement verification.

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Contractor_ID | 15 |
| B | Contractor_Name | 25 |
| C | Company_Name | 25 |
| D | Contract_Type | 20 |
| E | Services_Provided | 30 |
| F | Contract_Start | 12 |
| G | Contract_End | 12 |
| H | NDA_In_Place | 15 |
| I | Security_Clauses_Present | 15 |
| J | Data_Access_Level | 15 |
| K | Background_Check | 15 |
| L | Compliance_Status | 15 |
| M | Sponsor_Manager | 25 |
| N | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D5:D104 | `contract_type_dv` |
| H | H5:H104 | `yn_dv` |
| I | I5:I104 | `yn_dv` |
| K | K5:K104 | `yn_dv` |
| J | J5:J104 | `access_dv` |

---

## Sheet 8: Gap_Analysis

**Purpose:** Consolidated gaps from all assessment domains.

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap_ID | 12 |
| B | Source_Sheet | 25 |
| C | Affected_Entity | 25 |
| D | Gap_Category | 20 |
| E | Gap_Description | 50 |
| F | Risk_Level | 15 |
| G | Impact_Assessment | 40 |
| H | Affected_Personnel_Count | 15 |
| I | Remediation_Action | 50 |
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
| B | B5:B104 | `source_sheet_dv` |
| D | D5:D104 | `category_dv` |
| F | F5:F104 | `risk_level_dv` |
| L | L5:L104 | `effort_dv` |
| N | N5:N104 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{row}<>` |  |

---

## Sheet 9: Evidence_Register

**Purpose:** Supporting evidence documentation.

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence_ID | 12 |
| B | Evidence_Type | 25 |
| C | Description | 40 |
| D | Related_Entity_ID | 20 |
| E | Related_Assessment_Sheet | 25 |
| F | File_Location | 40 |
| G | Date_Collected | 12 |
| H | Collected_By | 25 |
| I | Verification_Status | 15 |
| J | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B5:B104 | `evidence_type_dv` |
| E | E5:E104 | `sheet_dv` |
| I | I5:I104 | `verification_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{row}<>` |  |

---

## Sheet 10: Approval_Sign_Off

**Purpose:** Three-level approval workflow.

---

**END OF SPECIFICATION**

---

*"A verbal contract isn't worth the paper it's written on."*
— Samuel Goldwyn

<!-- QA_VERIFIED: 2026-02-06 -->
