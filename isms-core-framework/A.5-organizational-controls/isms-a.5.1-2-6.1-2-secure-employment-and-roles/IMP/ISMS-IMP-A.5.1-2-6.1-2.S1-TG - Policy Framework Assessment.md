<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.1-2-6.1-2.S1-TG:framework:TG:a.5.1-2-6.1-2 -->
**ISMS-IMP-A.5.1-2-6.1-2.S1-TG - Policy Framework Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.1: Policies for Information Security

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Policy Framework Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S1-TG |
| **Related Policy** | ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.1 (Policies for Information Security) |
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

- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) - Section 4 (Policy Framework Requirements)
- ISMS-IMP-A.5.1-2-6.1-2.S2 (Roles & Responsibilities Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S3 (Screening & Vetting Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S4 (Employment Contract Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S5 (Governance Compliance Dashboard)

**Note on Naming Convention**: The ".S" designation indicates this implementation is part of a **stacked control framework** (A.5.1 + A.5.2 + A.6.1 + A.6.2). Despite unified implementation, each control maintains distinct requirements for Statement of Applicability purposes.

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a5_1_2_6_1_2_s1_policy_framework.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.1-2-6.1-2.S1` |
| **Output Filename** | `ISMS-IMP-A.5.1-2-6.1-2.S1_Policy_Framework_Assessment_Workbook_YYYYMMDD.xlsx` |
| **Workbook Title** | Policy Framework Assessment Workbook |
| **Total Sheets** | 11 (11 visible) |
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

## Sheet 2: Policy_Inventory

**Purpose:** Master policy inventory with full metadata.

**Data Rows:** 150 (rows 5–154) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Policy_ID | 20 |
| B | Policy_Title | 35 |
| C | Policy_Hierarchy_Tier | 15 |
| D | ISO_Control_Mapping | 20 |
| E | Policy_Owner | 25 |
| F | Policy_Approver | 25 |
| G | Current_Version | 12 |
| H | Version_Date | 12 |
| I | Approval_Date | 12 |
| J | Last_Review_Date | 12 |
| K | Next_Review_Date | 12 |
| L | Review_Frequency | 15 |
| M | Policy_Status | 15 |
| N | Policy_Classification | 15 |
| O | Acknowledgment_Required | 15 |
| P | Acknowledgment_Rate | 12 |
| Q | Repository_Location | 40 |
| R | Related_Documents | 30 |
| S | Gap_Identified | 15 |
| T | Notes | 40 |

---

## Sheet 3: Lifecycle_Compliance

**Purpose:** Verify policy lifecycle stages (creation, approval, review, update).

**Data Rows:** 150 (rows 5–154) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Policy_ID | 20 |
| B | Policy_Title | 35 |
| C | Creation_Process_Followed | 20 |
| D | Approval_Valid | 15 |
| E | Approval_Documentation | 20 |
| F | Publication_Status | 20 |
| G | Review_Schedule_Defined | 20 |
| H | Review_Status | 20 |
| I | Last_Review_Evidence | 20 |
| J | Version_Control_Practice | 15 |
| K | Sunset_Process | 15 |
| L | Lifecycle_Compliance_Rating | 20 |
| M | Gap_Description | 40 |
| N | Evidence_Reference | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C5:C154 | `creation_dv` |
| D | D5:D154 | `approval_valid_dv` |
| E | E5:E154 | `approval_doc_dv` |
| F | F5:F154 | `pub_status_dv` |
| G | G5:G154 | `review_schedule_dv` |
| I | I5:I154 | `review_evidence_dv` |
| J | J5:J154 | `version_control_dv` |
| K | K5:K154 | `sunset_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(ROW()-4<=COUNTA(Policy_Inventory!$A:$A)-4,INDEX(Policy_Inventory!$A:$A,ROW()` |  |
| BN | `=IF(A{row}<>` |  |

---

## Sheet 4: Governance_Assessment

**Purpose:** Ownership, accountability, approval authority verification.

**Data Rows:** 150 (rows 5–154) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Policy_ID | 20 |
| B | Policy_Title | 35 |
| C | Policy_Hierarchy_Tier | 15 |
| D | Owner_Assigned | 15 |
| E | Owner_Name_Role | 25 |
| F | Owner_Accountability_Clear | 15 |
| G | Approver_Assigned | 15 |
| H | Approver_Name_Role | 25 |
| I | Approval_Authority_Appropriate | 20 |
| J | RACI_Defined | 15 |
| K | Governance_Documentation | 20 |
| L | Escalation_Path_Clear | 15 |
| M | Governance_Compliance_Rating | 20 |
| N | Gap_Description | 40 |
| O | Evidence_Reference | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| F | F5:F154 | `owner_account_dv` |
| I | I5:I154 | `approval_auth_dv` |
| J | J5:J154 | `raci_dv` |
| K | K5:K154 | `gov_doc_dv` |
| L | L5:L154 | `escalation_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(ROW()-4<=COUNTA(Policy_Inventory!$A:$A)-4,INDEX(Policy_Inventory!$A:$A,ROW()` |  |
| BN | `=IF(A{row}<>` |  |
| DN | `=IF(A{row}=` |  |

---

## Sheet 5: Classification_Review

**Purpose:** Policy classification appropriateness and access control verification.

**Data Rows:** 150 (rows 5–154) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Policy_ID | 20 |
| B | Policy_Title | 35 |
| C | Current_Classification | 15 |
| D | Classification_Appropriate | 20 |
| E | Content_Sensitivity_Assessment | 15 |
| F | Access_Controls_Implemented | 20 |
| G | Distribution_Restrictions | 20 |
| H | Classification_Marking | 15 |
| I | Classification_Review_Date | 15 |
| J | Classification_Compliance_Rating | 20 |
| K | Gap_Description | 40 |
| L | Evidence_Reference | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D5:D154 | `class_approp_dv` |
| E | E5:E154 | `sensitivity_dv` |
| F | F5:F154 | `access_controls_dv` |
| G | G5:G154 | `distribution_dv` |
| H | H5:H154 | `marking_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(ROW()-4<=COUNTA(Policy_Inventory!$A:$A)-4,INDEX(Policy_Inventory!$A:$A,ROW()` |  |
| BN | `=IF(A{row}<>` |  |

---

## Sheet 6: Communication_Tracking

**Purpose:** Policy publication, acknowledgment, and training integration.

**Data Rows:** 150 (rows 5–154) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Policy_ID | 20 |
| B | Policy_Title | 35 |
| C | Acknowledgment_Required | 15 |
| D | Target_Audience | 20 |
| E | Publication_Date | 12 |
| F | Publication_Method | 30 |
| G | Accessibility_Verified | 15 |
| H | Acknowledgment_Mechanism | 20 |
| I | Acknowledgment_Rate | 12 |
| J | Acknowledgment_Timeframe | 15 |
| K | Non_Acknowledgment_Follow_Up | 20 |
| L | Training_Integration | 15 |
| M | User_Feedback_Mechanism | 15 |
| N | Communication_Compliance_Rating | 20 |
| O | Gap_Description | 40 |
| P | Evidence_Reference | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| G | G5:G154 | `accessibility_dv` |
| H | H5:H154 | `ack_mech_dv` |
| J | J5:J154 | `ack_time_dv` |
| K | K5:K154 | `followup_dv` |
| L | L5:L154 | `training_dv` |
| M | M5:M154 | `feedback_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(ROW()-4<=COUNTA(Policy_Inventory!$A:$A)-4,INDEX(Policy_Inventory!$A:$A,ROW()` |  |
| BN | `=IF(A{row}<>` |  |
| IN | `=IF(A{row}=` |  |

---

## Sheet 7: Repository_Assessment

**Purpose:** Policy repository structure, organization, and accessibility (repository-wide).

---

## Sheet 8: Gap_Analysis

**Purpose:** Consolidated gaps from all assessment domains.

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap_ID | 12 |
| B | Policy_ID | 20 |
| C | Policy_Title | 35 |
| D | Gap_Category | 15 |
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
| D | Related_Policy_ID | 20 |
| E | Related_Assessment_Sheet | 20 |
| F | File_Location | 40 |
| G | Date_Collected | 12 |
| H | Collected_By | 25 |
| I | Verification_Status | 15 |
| J | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B5:B104 | `evidence_type_dv` |
| I | I5:I104 | `verification_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(ROW()<=4,` |  |

---

## Sheet 10: Action_Items

**Purpose:** Remediation tracking (auto-populated from Gap_Analysis).

**Data Rows:** 50 (rows 5–54) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Action_ID | 12 |
| B | Related_Gap_ID | 12 |
| C | Action_Description | 40 |
| D | Priority | 15 |
| E | Owner | 25 |
| F | Target_Date | 15 |
| G | Status | 15 |
| H | Progress_% | 12 |
| I | Last_Update_Date | 12 |
| J | Last_Update_Notes | 35 |
| K | Blocking_Issues | 35 |
| L | Escalation_Required | 15 |
| M | Escalation_To | 25 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| L | L5:L54 | `escalation_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(Gap_Analysis!A{row}=` |  |
| BN | `=Gap_Analysis!A{row}` |  |
| CN | `=IF(Gap_Analysis!I{row}<>` |  |
| DN | `=IF(Gap_Analysis!F{row}<>` |  |
| EN | `=IF(Gap_Analysis!J{row}<>` |  |
| FN | `=IF(Gap_Analysis!K{row}<>` |  |
| GN | `=IF(Gap_Analysis!N{row}<>` |  |

---

## Sheet 11: Approval_Sign_Off

**Purpose:** Three-level approval workflow.

---

**END OF SPECIFICATION**

---

*"Policy is the architecture of accountability."*
— Anonymous

<!-- QA_VERIFIED: 2026-02-06 -->
