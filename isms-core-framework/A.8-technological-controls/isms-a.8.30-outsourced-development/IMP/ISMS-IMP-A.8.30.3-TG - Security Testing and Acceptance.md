<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.30.3-TG:framework:TG:a.8.30.3 -->
**ISMS-IMP-A.8.30.3-TG - Security Testing and Acceptance**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.30: Outsourced Development

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.3-TG |
| **Document Title** | Security Testing and Acceptance Workbook Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.30: Outsourced Development |
| **Parent Policy** | ISMS-POL-A.8.30 (Outsourced Development) |
| **Version** | 1.0 |
| **Classification** | Internal |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial implementation specification for ISO 27001:2022 first certification |

---

# Technical Specification


> Auto-generated from `generate_a830_3_security_testing.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.30.3` |
| **Output Filename** | `ISMS-IMP-A.8.30.3_Security_Testing_and_Acceptance_YYYYMMDD.xlsx` |
| **Workbook Title** | Security Testing and Acceptance |
| **Total Sheets** | 6 (6 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #D6DCE4 | D6DCE4 | Silver (Neutral) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Deliverable Inventory

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Deliverable_ID |
| B | Contract_ID |
| C | Vendor_ID |
| D | Deliverable_Name |
| E | Deliverable_Type |
| F | Project_Classification |
| G | Planned_Delivery |
| H | Actual_Delivery |
| I | Code_Review_Status |
| J | Security_Test_Status |
| K | SBOM_Received |
| L | Acceptance_Status |
| M | Acceptance_Date |
| N | Accepted_By |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E100 | `type_dv` |
| F | F2:F100 | `class_dv` |
| I | I2:I100 | `review_dv` |
| J | J2:J100 | `test_dv` |
| K | K2:K100 | `sbom_dv` |
| L | L2:L100 | `accept_dv` |

---

## Sheet 3: Code Review Tracking

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Review_ID |
| B | Deliverable_ID |
| C | Review_Type |
| D | Review_Date |
| E | Reviewer |
| F | Reviewer_Role |
| G | Files_Reviewed |
| H | Security_Findings |
| I | Critical_Findings |
| J | High_Findings |
| K | Medium_Findings |
| L | Low_Findings |
| M | Review_Result |
| N | Findings_Reference |
| O | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C100 | `type_dv` |
| F | F2:F100 | `role_dv` |
| M | M2:M100 | `result_dv` |

---

## Sheet 4: Security Testing

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Test_ID |
| B | Deliverable_ID |
| C | Test_Type |
| D | Test_Tool |
| E | Test_Date |
| F | Tester |
| G | Scope |
| H | Total_Findings |
| I | Critical_Findings |
| J | High_Findings |
| K | Medium_Findings |
| L | Low_Findings |
| M | False_Positives |
| N | Findings_Remediated |
| O | Findings_Outstanding |
| P | Report_Reference |
| Q | Retest_Required |
| R | Retest_Date |
| S | Retest_Status |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C100 | `type_dv` |
| Q | Q2:Q100 | `retest_dv` |
| S | S2:S100 | `retest_status_dv` |

---

## Sheet 5: SBOM Management

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | SBOM_ID |
| B | Deliverable_ID |
| C | SBOM_Format |
| D | SBOM_Date |
| E | Total_Components |
| F | Direct_Dependencies |
| G | Transitive_Dependencies |
| H | Known_Vulnerabilities |
| I | Critical_Vulns |
| J | High_Vulns |
| K | License_Issues |
| L | Outdated_Components |
| M | Review_Status |
| N | Reviewed_By |
| O | Review_Date |
| P | SBOM_Reference |
| Q | Action_Plan |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C100 | `format_dv` |
| M | M2:M100 | `status_dv` |

---

## Sheet 6: Acceptance Sign-off

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Acceptance_ID |
| B | Deliverable_ID |
| C | Criteria_Category |
| D | Acceptance_Criteria |
| E | Status |
| F | Evidence_Reference |
| G | Verified_By |
| H | Verification_Date |
| I | Waiver_Reason |
| J | Waiver_Approver |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C100 | `category_dv` |
| E | E2:E100 | `status_dv` |

---

**END OF SPECIFICATION**

---

*"Quality is not an act, it is a habit."*
— Aristotle

<!-- QA_VERIFIED: 2026-02-06 -->
