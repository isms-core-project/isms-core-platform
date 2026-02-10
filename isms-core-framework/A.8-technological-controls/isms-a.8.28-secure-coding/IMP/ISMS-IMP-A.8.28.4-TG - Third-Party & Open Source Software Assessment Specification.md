<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.28.4-TG:framework:TG:a.8.28.4 -->
**ISMS-IMP-A.8.28.4-TG - Third-Party & Open Source Software Assessment Specification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.28.4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Third-Party Dependencies & Open Source Software Management |
| **Related Policy** | ISMS-POL-A.8.28 Section 2.4 (Third-Party & OSS Management), Section 3 (Roles & Responsibilities) |
| **Purpose** | Evaluate supply chain security practices for third-party dependencies, open source software, vendor security, and license compliance |
| **Target Audience** | Application Security Team, Engineering Managers, Software Architects, Legal/Compliance Team, Procurement Team, Auditors |
| **Assessment Type** | Process, Technical & Legal |
| **Review Cycle** | Annually or After Major Supply Chain Security Incidents |
| **Date** | [Date] |

**Version History**:

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [Date] | Initial assessment specification |

**Approvers**:

- Application Security Lead (Technical Review)
- Chief Information Security Officer (Final Approval)
- Legal Counsel (License Compliance Review)

**Related Documents**:

- ISMS-POL-A.8.28 - Secure Coding Policy (Master Policy)
- ISMS-POL-A.8.28-S2.4 - Third-Party & Open Source Software Management  
- ISMS-IMP-A.8.28.1 - SDLC Assessment
- ISMS-IMP-A.8.28.2 - Standards & Tools Assessment

---

# Technical Specification


> Auto-generated from `generate_a828_4_third_party_oss.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.28.4` |
| **Output Filename** | `ISMS-IMP-A.8.28.4_Third-Party_Code_and_Open_Source_Component_Security_YYYYMMDD.xlsx` |
| **Workbook Title** | Third-Party Code and Open Source Component Security |
| **Total Sheets** | 8 (8 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #70AD47 | 70AD47 | Medium Green (On Track) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FF6666 | FF6666 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: ISMS Control A.8.28.4 - Third-Party & OSS Assessment

**Purpose:** Initialize workbook with proper metadata.

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | A | 8 |
| B | B | 55 |
| C | C | 22 |
| D | D | 35 |
| E | E | 40 |
| F | F | 12 |

---

## Sheet 2: Data_Validations

---

## Sheet 3: Instructions

**Purpose:** This sheet provides:

---

## Sheet 4: Domain_Assessment

### Columns

| Col | Header |
|-----|--------|
| A | ID |
| B | Requirement |
| C | Implementation Status |
| D | Evidence Reference |
| E | Comments |
| F | ✓ |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| FN:FN | equal  |  |
| FN:FN | equal  |  |
| FN:FN | equal  |  |
| FN:FN | equal  |  |

---

## Sheet 5: Summary_Dashboard

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Domain |
| B | Total |
| C | Impl. |
| D | Partial |
| E | Not Impl. |
| F | N/A |
| G | Compliance % |
| H | Status |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| CN | `=COUNTIF({sheet_name}!C4:C21,` |  |
| GN | `=IF((B{current_row}-F{current_row})=0,0,(C{current_row}+D{current_row}*0.5)/(B{c` |  |
| HN | `=IF(G{current_row}>=0.8,` |  |
| BN | `=SUM(B{domain_start_row}:B{domain_end_row})` |  |
| CN | `=SUM(C{domain_start_row}:C{domain_end_row})` |  |
| DN | `=SUM(D{domain_start_row}:D{domain_end_row})` |  |
| EN | `=SUM(E{domain_start_row}:E{domain_end_row})` |  |
| FN | `=SUM(F{domain_start_row}:F{domain_end_row})` |  |
| HN | `=IF(G{current_row}>=0.7,` |  |
| — | `=COUNTA(Evidence_Register!D2:D200)/COUNTA(Evidence_Register!A2:A200)` | Evidence Completeness: |

---

## Sheet 6: Evidence_Register

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 10 |
| B |  | 40 |
| C |  | 15 |
| D |  | 35 |
| E |  | 12 |
| F |  | 20 |
| G |  | 15 |
| H |  | 20 |
| I |  | 12 |
| J |  | 30 |

---

## Sheet 7: Gap_Analysis

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A |  | 10 |
| B |  | 25 |
| C |  | 10 |
| D |  | 35 |
| E |  | 30 |
| F |  | 30 |
| G |  | 12 |
| H |  | 35 |
| I |  | 20 |
| J |  | 12 |
| K |  | 15 |
| L |  | 12 |
| M |  | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| JN:JN | lessThan TODAY() |  |

---

## Sheet 8: Approval_Sign_Off

---

**END OF SPECIFICATION**

---

*"Complexity is the enemy of security."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
