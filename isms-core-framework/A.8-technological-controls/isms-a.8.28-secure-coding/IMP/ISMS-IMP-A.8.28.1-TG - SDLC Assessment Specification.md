<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.28.1-TG:framework:TG:a.8.28.1 -->
**ISMS-IMP-A.8.28.1-TG - SDLC Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.28.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Secure Development Lifecycle (SDLC) Integration |
| **Related Policy** | ISMS-POL-A.8.28 Section 2.1 (Pre-Development Requirements), Section 3.1 (Roles & Responsibilities) |
| **Purpose** | Evaluate integration of security practices into SDLC, focusing on pre-development activities and process-level controls that prevent vulnerabilities |
| **Target Audience** | Application Security Lead, Development Managers, Security Architects, Project Managers, Auditors |
| **Assessment Type** | Process & Organizational |
| **Review Cycle** | Quarterly or After Major SDLC Changes |
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

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.28.1-UG.

---

---


> Auto-generated from `generate_a828_1_sdlc_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.28.1` |
| **Output Filename** | `ISMS-IMP-A.8.28.1_Secure_Development_Lifecycle_Integration_YYYYMMDD.xlsx` |
| **Workbook Title** | Secure Development Lifecycle Integration |
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

## Sheet 2: Security_Requirements_Design

---

## Sheet 3: Development_Environment

---

## Sheet 4: Build_Deployment_Pipeline

---

## Sheet 5: Security_Testing_Integration

---

## Sheet 6: Release_Change_Management

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

**Purpose:** Each domain sheet follows the same structure:

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

**Purpose:** Assessment isn't complete until it's reviewed and approved.

**Data Rows:** 6 (rows 30–35)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| B6 | `=Instructions!B8` |  |
| B7 | `=Instructions!B9` |  |
| B8 | `=Instructions!B10` |  |
| B9 | `=Summary_Dashboard!C7` |  |
| B10 | `=Summary_Dashboard!D7` |  |
| B15 | `=Summary_Dashboard!B19` |  |
| B16 | `=Summary_Dashboard!B20` |  |
| B17 | `=Summary_Dashboard!B21` |  |
| B18 | `=Summary_Dashboard!B22` |  |
| B19 | `=Summary_Dashboard!B23` |  |

---

## Sheet 13: Base_Validations

---

**END OF SPECIFICATION**

---

*"Security is a process, not a product. It's also not a destination but a journey."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
