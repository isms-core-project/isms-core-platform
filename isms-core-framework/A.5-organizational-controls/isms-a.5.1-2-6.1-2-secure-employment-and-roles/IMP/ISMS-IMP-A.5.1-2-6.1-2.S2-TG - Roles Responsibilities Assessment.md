<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.1-2-6.1-2.S2-TG:framework:TG:a.5.1-2-6.1-2 -->
**ISMS-IMP-A.5.1-2-6.1-2.S2-TG - Roles & Responsibilities Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.2: Information Security Roles and Responsibilities

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Roles & Responsibilities Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S2-TG |
| **Related Policy** | ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.2 (Information Security Roles and Responsibilities) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
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
- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) - Section 5 (Roles & Responsibilities Requirements)
- ISMS-IMP-A.5.1-2-6.1-2.S1 (Policy Framework Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S3 (Screening & Vetting Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S4 (Employment Contract Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S5 (Governance Compliance Dashboard)

**Note on Naming Convention**: The ".S" designation indicates this implementation is part of a **stacked control framework** (A.5.1 + A.5.2 + A.6.1 + A.6.2). Despite unified implementation, each control maintains distinct requirements for Statement of Applicability purposes.

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a5_1_2_6_1_2_s2_roles_responsibilities.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.1-2-6.1-2.S2` |
| **Output Filename** | `ISMS-IMP-A.5.1-2-6.1-2.S2_Roles_Responsibilities_Assessment_Workbook_YYYYMMDD.xlsx` |
| **Workbook Title** | Roles Responsibilities Assessment Workbook |
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

## Sheet 2: Role_Inventory

**Purpose:** Master list of all security roles with metadata.

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Role_ID | 15 |
| B | Role_Title | 30 |
| C | Role_Category | 20 |
| D | Role_Type | 15 |
| E | Department | 20 |
| F | Reports_To | 25 |
| G | Security_Clearance_Required | 15 |
| H | ISO_Control_Mapping | 20 |
| I | Role_Created_Date | 12 |
| J | Last_Review_Date | 12 |
| K | Role_Status | 15 |
| L | Criticality | 15 |
| M | Backup_Required | 15 |
| N | Backup_Role_ID | 15 |
| O | Role_Description | 50 |
| P | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C5:C104 | `category_dv` |
| D | D5:D104 | `type_dv` |
| G | G5:G104 | `clearance_dv` |
| K | K5:K104 | `status_dv` |
| L | L5:L104 | `crit_dv` |
| M | M5:M104 | `backup_dv` |

---

## Sheet 3: Role_Definition_Assessment

**Purpose:** Verify role definition completeness for each security role.

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Role_ID | 15 |
| B | Role_Title | 30 |
| C | Role_Category | 20 |
| D | Responsibilities_Documented | 15 |
| E | Authority_Level_Defined | 15 |
| F | Reporting_Lines_Clear | 15 |
| G | Competency_Requirements | 15 |
| H | Training_Requirements | 15 |
| I | Access_Requirements | 15 |
| J | Accountability_Defined | 15 |
| K | Segregation_of_Duties | 15 |
| L | Definition_Documentation | 20 |
| M | Definition_Compliance_Rating | 20 |
| N | Gap_Description | 40 |
| O | Evidence_Reference | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| K | K5:K104 | `sod_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(ROW()-4<=COUNTA(Role_Inventory!$A:$A)-4,INDEX(Role_Inventory!$A:$A,ROW()-3),` |  |
| BN | `=IF(A{row}<>` |  |

---

## Sheet 4: RACI_Matrix_Assessment

**Purpose:** RACI matrix completeness and accuracy verification.

**Data Rows:** 150 (rows 25–174) | **Frozen Panes:** A26

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Activity_ID | 15 |
| B | Security_Activity | 40 |
| C | Activity_Category | 20 |
| D | Responsible_Role | 25 |
| E | Accountable_Role | 25 |
| F | Consulted_Roles | 30 |
| G | Informed_Roles | 30 |
| H | Responsible_Assigned | 12 |
| I | Accountable_Assigned | 12 |
| J | Multiple_Accountables | 12 |
| K | RACI_Documented | 12 |
| L | RACI_Score | 12 |
| M | RACI_Status | 15 |
| N | RACI_Conflict | 15 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C26:C175 | `category_dv` |
| K | K26:K175 | `documented_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| HN | `=IF(D{row}<>` |  |
| IN | `=IF(E{row}<>` |  |
| JN | `=IF(ISERROR(FIND(` |  |
| MN | `=IF(B{row}=` |  |
| NN | `=IF(J{row}=` |  |

---

## Sheet 5: Role_Assignment_Verification

**Purpose:** Current role holders and vacancy tracking.

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Role_ID | 15 |
| B | Role_Title | 30 |
| C | Role_Category | 20 |
| D | Current_Holder_Name | 25 |
| E | Current_Holder_Employee_ID | 15 |
| F | Assignment_Date | 12 |
| G | Assignment_Documentation | 15 |
| H | Formal_Acceptance | 15 |
| I | Background_Check_Status | 15 |
| J | Assignment_Status | 15 |
| K | Backup_Holder_Name | 25 |
| L | Backup_Assignment_Status | 15 |
| M | Last_Verification_Date | 12 |
| N | Gap_Description | 40 |
| O | Evidence_Reference | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| G | G5:G104 | `doc_status_dv` |
| H | H5:H104 | `acceptance_dv` |
| I | I5:I104 | `bg_check_dv` |
| L | L5:L104 | `backup_status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(ROW()-4<=COUNTA(Role_Inventory!$A:$A)-4,INDEX(Role_Inventory!$A:$A,ROW()-3),` |  |
| BN | `=IF(A{row}<>` |  |

---

## Sheet 6: Training_Assessment

**Purpose:** Role-specific training completion tracking.

**Data Rows:** 100 (rows 25–124) | **Frozen Panes:** A26

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Role_ID | 15 |
| B | Role_Title | 30 |
| C | Role_Holder_Name | 25 |
| D | Required_Training_1 | 25 |
| E | Training_1_Status | 12 |
| F | Training_1_Date | 12 |
| G | Required_Training_2 | 25 |
| H | Training_2_Status | 12 |
| I | Training_2_Date | 12 |
| J | Required_Training_3 | 25 |
| K | Training_3_Status | 12 |
| L | Training_Expiry_Status | 15 |
| M | Training_Records_Available | 12 |
| N | Training_Compliance_Rating | 20 |
| O | Gap_Description | 40 |
| P | Evidence_Reference | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| L | L26:L125 | `expiry_dv` |
| M | M26:M125 | `records_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(ROW()-25<=COUNTA(Role_Assignment_Verification!$A:$A)-4,INDEX(Role_Assignment` |  |
| BN | `=IF(A{row}<>` |  |

---

## Sheet 7: Access_Alignment_Review

**Purpose:** Role-based access vs. role definition alignment verification.

**Data Rows:** 100 (rows 25–124) | **Frozen Panes:** A26

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Role_ID | 15 |
| B | Role_Title | 30 |
| C | Role_Holder_Name | 25 |
| D | Defined_Access_Level | 20 |
| E | Actual_Access_Level | 20 |
| F | Systems_Access_Defined | 30 |
| G | Systems_Access_Actual | 30 |
| H | Excess_Privileges | 12 |
| I | Missing_Access | 12 |
| J | Access_Review_Date | 12 |
| K | SoD_Conflict | 12 |
| L | Access_Documentation | 12 |
| M | Access_Alignment_Status | 15 |
| N | Gap_Description | 40 |
| O | Evidence_Reference | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| L | L26:L125 | `doc_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(ROW()-25<=COUNTA(Role_Assignment_Verification!$A:$A)-4,INDEX(Role_Assignment` |  |
| BN | `=IF(A{row}<>` |  |

---

## Sheet 8: Gap_Analysis

**Purpose:** Consolidated gaps from all assessment domains.

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap_ID | 12 |
| B | Role_ID | 15 |
| C | Role_Title | 30 |
| D | Gap_Category | 20 |
| E | Gap_Description | 40 |
| F | Risk_Level | 15 |
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
| D | D5:D104 | `gap_category_dv` |
| F | F5:F104 | `risk_level_dv` |
| L | L5:L104 | `effort_dv` |
| N | N5:N104 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(ROW()<=4,` |  |

---

## Sheet 9: Evidence_Register

**Purpose:** Supporting evidence documentation.

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence_ID | 12 |
| B | Evidence_Type | 20 |
| C | Description | 40 |
| D | Related_Role_ID | 15 |
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
| AN | `=IF(ROW()<=4,` |  |

---

## Sheet 10: Approval_Sign_Off

**Purpose:** Three-level approval workflow.

---

**END OF SPECIFICATION**

---

*"The price of greatness is responsibility."*
— Winston Churchill

<!-- QA_VERIFIED: 2026-02-06 -->
