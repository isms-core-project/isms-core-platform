**ISMS-IMP-A.7.6-7-14-S1-TG - Secure Areas Working Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.6: Working in Secure Areas

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.6-7-14-S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Secure Areas - Working Procedures, Access Controls, Personnel Conduct |
| **Related Policy** | ISMS-POL-A.7.6-7-14, Section 2.1 (Working in Secure Areas) |
| **Purpose** | Document secure area definitions, assess working procedures against policy requirements, track personnel compliance and third-party access |
| **Target Audience** | Facilities Management, Security Operations, IT Operations, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Procedural |
| **Review Cycle** | Quarterly or After Major Facility Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Secure Areas Working assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.6-7-14-S1-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.6.S1_Secure_Areas_Working_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a76_1_secure_areas.py)

**Sheet Count:** 8 worksheets

**Data Capacity:** 100 data rows per assessment sheet (Sheets 2-5)

**Styling:** Navy blue headers, yellow input cells, conditional formatting for compliance status

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Assessment metadata and status legend | Read-only Reference | ~30 rows |
| 2 | Secure Area Register | Secure area inventory and characteristics | Data Entry | 100 data rows |
| 3 | Working Procedures | Procedure compliance assessment | Data Entry | 50 data rows |
| 4 | Third-Party Access | Visitor and contractor access tracking | Data Entry | 100 data rows |
| 5 | Incidents | Security incident log (last 12 months) | Data Entry | 100 data rows |
| 6 | Summary Dashboard | Automated compliance scoring and metrics | Formula-driven | ~40 rows |
| 7 | Evidence Register | Supporting evidence documentation | Data Entry | 100 data rows |
| 8 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata, status legend, and completion instructions

**Structure:**

**Row 1:** Header
- Merged cells A1:G1
- Text: "ISMS-IMP-A.7.6.S1 - Secure Areas Working Assessment\nISO/IEC 27001:2022 - Control A.7.6: Working in Secure Areas"
- Style: Navy blue background, white bold text, 14pt, centre-aligned

**Rows 3-11:** Document Information Table
- Column A: Labels
- Column B: Values (pre-filled for read-only fields, blank yellow for user input)
- User input fields (yellow): Assessment Date, Completed By, Organisation

**Rows 13-17:** Status Legend
- Colour-coded status definitions

**Rows 19-30:** Completion Instructions
- Brief workflow summary
- Reference to Part I User Guide

### Sheet 2: Secure Area Register

**Purpose:** Document all defined secure areas and assess characteristics

**Header Row (Row 3):**
- Style: Grey background, bold text, centre-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Secure Area ID | Text | 15 | None |
| B | Secure Area Name | Text | 30 | None |
| C | Location | Text | 25 | None |
| D | Classification | Dropdown | 20 | Tier 1 - Critical / Tier 2 - Standard |
| E | Access Control Type | Dropdown | 20 | Badge + PIN / Biometric / Badge Only / Mantrap |
| F | Authorised Personnel | Number | 15 | Integer >0 |
| G | Last Access Review | Date | 15 | Date |
| H | Emergency Procedures Posted | Dropdown | 15 | Yes / No |
| I | Recording Controls | Dropdown | 18 | Prohibited / Authorised Only / No Restriction |
| J | Unsupervised Working | Dropdown | 18 | Prohibited / Restricted / Allowed |
| K | Compliance Status | Formula | 18 | Auto-calculated |
| L | Notes | Text | 50 | None |

**Data Rows:** Rows 4-103 (100 data rows)

### Sheet 3: Working Procedures

**Purpose:** Assess compliance with working procedure requirements

**Columns:**

| Col | Field Name | Type | Width |
|-----|------------|------|-------|
| A | Requirement ID | Text | 15 |
| B | Requirement Description | Text | 50 |
| C | Implementation Status | Dropdown | 20 |
| D | Evidence | Text | 40 |
| E | Compliance Status | Formula | 18 |
| F | Notes | Text | 50 |

### Sheet 4: Third-Party Access

**Purpose:** Track visitor and contractor access to secure areas

**Columns:**

| Col | Field Name | Type | Width |
|-----|------------|------|-------|
| A | Access Period | Text | 15 |
| B | Secure Area | Text | 30 |
| C | Visitor/Contractor Count | Number | 15 |
| D | Escort Compliance | Text | 15 |
| E | NDA Status | Dropdown | 15 |
| F | Time Limit Compliance | Dropdown | 18 |
| G | Equipment Inspected | Dropdown | 15 |
| H | Compliance Status | Formula | 18 |
| I | Notes | Text | 50 |

### Sheet 5: Incidents

**Purpose:** Log secure area security incidents

**Columns:**

| Col | Field Name | Type | Width |
|-----|------------|------|-------|
| A | Incident ID | Text | 18 |
| B | Incident Date | Date | 15 |
| C | Secure Area | Text | 25 |
| D | Incident Type | Dropdown | 22 |
| E | Severity | Dropdown | 12 |
| F | Description | Text | 40 |
| G | Response Time (Min) | Number | 15 |
| H | Resolution Status | Dropdown | 15 |
| I | Corrective Action | Text | 40 |
| J | Notes | Text | 50 |

### Sheet 6: Summary Dashboard

**Purpose:** Automated compliance scoring and key performance indicators

**Sections:**

- Overall Compliance Score
- Secure Area Coverage
- Working Procedure Compliance
- Third-Party Access Compliance
- Incident Metrics
- Gap Summary

### Sheet 7: Evidence Register

**Purpose:** Document all supporting evidence with audit traceability

**Columns:**

| Col | Field Name | Type | Width |
|-----|------------|------|-------|
| A | Evidence ID | Text | 12 |
| B | Evidence Type | Dropdown | 18 |
| C | Description | Text | 40 |
| D | Related Sheet/Item | Text | 25 |
| E | File Name | Text | 35 |
| F | File Location | Text | 50 |
| G | Collection Date | Date | 15 |
| H | Collected By | Text | 25 |
| I | Retention Period | Text | 18 |
| J | Notes | Text | 50 |

### Sheet 8: Approval Sign-Off

**Purpose:** Four-level approval workflow documentation

**Approval Levels:**
- Level 1: Assessor
- Level 2: Security Operations Manager
- Level 3: CISO
- Level 4: Compliance Officer

---

## Cell Styling Reference

### Colour Palette

**Headers:**
- Primary Header: #003366 (Navy blue background), #FFFFFF (White text)
- Column Header: #D9D9D9 (Light grey background), #000000 (Black text)

**Data Cells:**
- Input Cell: #FFFFCC (Light yellow background)
- Formula Cell: #FFFFFF (White background)

**Compliance Status:**
- Compliant: #C6EFCE (Light green background)
- Partial: #FFEB9C (Light amber background)
- Non-Compliant: #FFC7CE (Light red background)

---

## Integration Points

### Integration with Policy (ISMS-POL-A.7.6-7-14)

**Policy Section to Assessment Sheet Mapping:**

| Policy Section | Assessment Sheet | Assessment Focus |
|----------------|------------------|------------------|
| Section 2.1: Working in Secure Areas | Sheet 2, Sheet 3 | Secure area inventory, working procedures |
| Section 2.1: Third-Party Access | Sheet 4 | Visitor and contractor management |
| Section 3: Roles & Responsibilities | Sheet 8 | Approval workflow |

### Integration with Other Assessments

**Feeds into:**
- ISMS-IMP-A.7.6-7-14-S4 (Compliance Dashboard): Overall secure area compliance score

---

**END OF SPECIFICATION**

---

*"Security is not a product, but a process."*
— Bruce Schneier

<!-- QA_VERIFIED: 2026-02-06 -->
