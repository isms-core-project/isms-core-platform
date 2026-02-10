<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.28.3-TG:framework:TG:a.8.28.3 -->
**ISMS-IMP-A.8.28.3-TG - Code Review & Testing Assessment Specification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.28.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Code Review & Security Testing |
| **Related Policy** | ISMS-POL-A.8.28 Section 2.3 (Code Review & Testing Requirements), Annex B (Code Review Checklist) |
| **Purpose** | Evaluate effectiveness of code review practices and security testing activities throughout SDLC, focusing on whether security is genuinely evaluated before production |
| **Target Audience** | Application Security Team, QA Managers, Security Champions, Development Team Leads, Test Engineers, Auditors |
| **Assessment Type** | Process & Technical |
| **Review Cycle** | Quarterly or After Security Incidents Revealing Review/Testing Gaps |
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

---

# Technical Specification


> Auto-generated from `generate_a828_3_code_review_testing.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.28.3` |
| **Output Filename** | `ISMS-IMP-A.8.28.3_Code_Review_and_Security_Testing_Processes_YYYYMMDD.xlsx` |
| **Workbook Title** | Code Review and Security Testing Processes |
| **Total Sheets** | 13 (13 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
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

## Sheet 2: Code_Review_Process

---

## Sheet 3: Security_Champion_Review

---

## Sheet 4: Unit_Integration_Testing

---

## Sheet 5: API_Application_Testing

---

## Sheet 6: External_Testing_Validation

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

*"You can't encrypt your way out of a fundamentally insecure design."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
