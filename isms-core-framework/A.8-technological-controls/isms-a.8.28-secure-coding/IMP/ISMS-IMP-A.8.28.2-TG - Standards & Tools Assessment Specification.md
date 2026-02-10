<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.28.2-TG:framework:TG:a.8.28.2 -->
**ISMS-IMP-A.8.28.2-TG - Standards & Tools Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.28.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Secure Coding Standards & Security Tool Implementation |
| **Related Policy** | ISMS-POL-A.8.28 Section 2.2 (Secure Coding Standards), Section 2.3 (Code Review & Testing) |
| **Purpose** | Evaluate implementation and effectiveness of secure coding standards and security tools - deployment AND actual security improvement |
| **Target Audience** | Application Security Team, Security Architects, Development Managers, DevOps Engineers, Tool Administrators, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Tool Changes |
| **Date** | [Date] |

**Version History**:

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [Date] | Initial assessment specification |

**Approvers**:

- Application Security Lead (Technical Review)
- Development Manager / Engineering Lead (Engineering Perspective)
- QA Manager / Test Lead (Testing Validation)
- CISO / Security Director (Executive Approval)

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.28.2-UG.

---

# Technical Specification
**Audience:** Workbook developers (Python/Excel script maintainers)


> Auto-generated from `generate_a828_2_standards_tools.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.28.2` |
| **Output Filename** | `ISMS-IMP-A.8.28.2_Coding_Standards_and_Development_Tool_Security_YYYYMMDD.xlsx` |
| **Workbook Title** | Coding Standards and Development Tool Security |
| **Total Sheets** | 13 (13 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #70AD47 | 70AD47 | Medium Green (On Track) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FF6666 | FF6666 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Coding_Standards_Adoption

---

## Sheet 3: SAST_SCA_Tools

---

## Sheet 4: DAST_Security_Testing_Tools

---

## Sheet 5: IDE_Plugins_Linters

---

## Sheet 6: Tool_Effectiveness_Metrics

---

## Sheet 7: Summary_Dashboard

---

## Sheet 8: Evidence_Register

---

## Sheet 9: Gap_Analysis

---

## Sheet 10: Approval_Sign_Off

---

## Sheet 11: Domain

**Frozen Panes:** A3

### Columns

| Col | Header |
|-----|--------|
| A | ID |
| B | Requirement |
| C | Implementation Status |
| D | Evidence Reference |
| E | Comments |
| F | Compliance |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| FN | `=IF(C{row}=` |  |

---

## Sheet 12: Approval

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| B6 | `=Instructions!B8` |  |
| B7 | `=Instructions!B9` |  |
| B8 | `=Summary_Dashboard!C7` |  |

---

## Sheet 13: Base_Validations

---

**END OF SPECIFICATION**

---

*"The purpose of computing is insight, not numbers."*
— Ron Rivest, after Richard Hamming

<!-- QA_VERIFIED: 2026-02-06 -->
