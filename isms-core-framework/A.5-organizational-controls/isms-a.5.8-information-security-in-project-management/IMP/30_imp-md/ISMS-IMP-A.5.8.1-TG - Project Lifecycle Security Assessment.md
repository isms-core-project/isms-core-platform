**ISMS-IMP-A.5.8.1-TG - Project Lifecycle Security Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.8: Information Security in Project Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.8.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Project Lifecycle Security Integration |
| **Related Policy** | ISMS-POL-A.5.8, Section 2.3 (Security Activities Across Project Lifecycle) |
| **Purpose** | Assess integration of information security activities across all project phases (Initiation → Planning → Execution → Monitoring → Closure) with phase-by-phase compliance verification and gate review documentation |
| **Target Audience** | Project Managers, Project Security Coordinators, PMO Staff, Information Security Officers, Project Steering Committees, Auditors |
| **Assessment Type** | Process & Procedural Compliance |
| **Review Cycle** | Per Project Phase (at each gate review) + Annual Post-Project Review for lessons learned |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Initial | Initial specification for Project Lifecycle Security Assessment workbook | ISMS Implementation Team |

---
# Technical Specification
**Audience:** Workbook Developers (Python/Excel script maintainers)


> Auto-generated from `generate_a58_1_project_lifecycle_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.8.1` |
| **Output Filename** | `ISMS-IMP-A.5.8.1_Project_Lifecycle_Assessment_YYYYMMDD.xlsx` |
| **Total Sheets** | 16 (16 visible) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.8 |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #305496 | 305496 | Custom |
| #808080 | 808080 | Gray (Disabled) |
| #B4C7E7 | B4C7E7 | Light Blue (Planned/Info) |
| #D9E1F2 | D9E1F2 | Custom |
| #E2EFDA | E2EFDA | Pale Green (Success Background) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFF00 | FFFF00 | Yellow (Warning) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: 2. Project Classification

---

## Sheet 3: 3. Initiation Phase

---

## Sheet 4: 4. Planning Phase

---

## Sheet 5: 5. Execution Phase

---

## Sheet 6: 6. Monitoring Phase

---

## Sheet 7: 7. Closure Phase

---

## Sheet 8: 8. Compliance Dashboard

---

## Sheet 9: 9. Evidence Register

---

## Sheet 10: 10. Sign-Off

---

## Sheet 11: Instructions

---

## Sheet 12: Classification

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=SUM(E{factor_start_row}:E{factor_start_row+5})` |  |
| BN | `=IF(E{row-1}>=15,` |  |

---

## Sheet 13: Phase

**Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Activity |
| B | Status |
| C | Completion Date |
| D | Evidence Link |
| E | Notes |

---

## Sheet 14: Dashboard

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=TODAY()` |  |
| BN | `=COUNTIF({sheet_ref}!B{start_row}:B{end_row},` |  |
| BN | `=AVERAGE(B{row-5}:B{row-1})` |  |

---

## Sheet 15: Evidence_Register

**Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Phase |
| C | Description |
| D | Location/Path |
| E | Date Collected |
| F | Status |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=TEXT(ROW()-3,\` |  |

---

## Sheet 16: Signoff

### Columns

| Col | Header |
|-----|--------|
| A | Role |
| B | Name |
| C | Signature |
| D | Date |
| E | Decision |

---

**END OF SPECIFICATION**

---

*"Everything we call real is made of things that cannot be regarded as real."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
