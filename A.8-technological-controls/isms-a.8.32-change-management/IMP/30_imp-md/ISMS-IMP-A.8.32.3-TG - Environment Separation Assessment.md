**ISMS-IMP-A.8.32.3-TG - Environment Separation Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.32.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Development, Test, Production Environment Separation |
| **Related Policy** | ISMS-POL-A.8.32, Section 2.3 (Testing & Validation Requirements), ISO/IEC 27001:2022 Control 8.31 |
| **Purpose** | Assess environment separation, promotion workflows, and access controls to ensure changes are properly tested before production deployment |
| **Target Audience** | Infrastructure Team, DevOps Engineers, System Administrators, Security Team, Compliance Officers, Auditors, Workbook Developers |
| **Assessment Type** | Technical & Infrastructure |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial assessment specification for Environment Separation workbook | ISMS Implementation Team |

---


> Auto-generated from `generate_a832_3_environment_separation.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.32.3` |
| **Output Filename** | `ISMS-IMP-A.8.32.3_Environment_Separation_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Environment Separation Assessment |
| **Total Sheets** | 18 (18 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #B4C7E7 | B4C7E7 | Light Blue (Planned/Info) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E0E0E0 | E0E0E0 | Custom |
| #F5F5F5 | F5F5F5 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: Environment_Inventory

---

## Sheet 3: Access_Controls

---

## Sheet 4: Promotion_Workflows

---

## Sheet 5: Data_Protection

---

## Sheet 6: Environment_Config

---

## Sheet 7: Separation_Controls

---

## Sheet 8: Evidence_Register

---

## Sheet 9: Summary_Dashboard

---

## Sheet 10: Approval_Sign_Off

---

## Sheet 11: Instructions

**Frozen Panes:** A4

---

## Sheet 12: Development_Environment

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Attribute |
| B | Value |
| C | Compliance |
| D | Evidence |
| E | Notes |

---

## Sheet 13: Test_Qa_Environment

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Attribute |
| B | Value |
| C | Compliance |
| D | Evidence |
| E | Notes |

---

## Sheet 14: Environment_Promotion_Process

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | From Environment |
| B | To Environment |
| C | Method |
| D | Approval Required? |
| E | Frequency |
| F | Notes |

---

## Sheet 15: Production_Data_In_Nonprod

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Requirement |
| B | Implemented? |
| C | Details |
| D | Compliance |
| E | Evidence |
| F | Notes |

---

## Sheet 16: Production_Environment

**Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Attribute |
| B | Value |
| C | Compliance |
| D | Evidence |
| E | Notes |

---

## Sheet 17: Approval_Signoff

**Purpose:** Formal approval workflow with 3-level sign-off.

**Frozen Panes:** A4

---

## Sheet 18: Base_Validations

---

**END OF SPECIFICATION**

---

*"When you have a clever cryptographic scheme, the job is half done. Making it work in practice is the other ninety percent."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
