<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.27.2-TG:framework:TG:a.8.27.2 -->
**ISMS-IMP-A.8.27.2-TG - Threat Modelling Methodology**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Threat Modelling Methodology |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.2-TG |
| **Assessment Domain** | Domain 2 - Threat Analysis and Modelling |
| **Related Policy** | ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Security Architect / Threat Modelling Lead |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect | Initial threat modelling assessment specification |

**Review Cycle**: Annual (or after methodology changes)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles)
- ISMS-IMP-A.8.27.1 (Security Architecture Review Process)
- ISMS-IMP-A.8.27.3 (Secure Architecture Pattern Catalogue)
- ISMS-IMP-A.8.27.4 (Zero Trust Implementation Assessment)
- ISMS-POL-A.5.7 (Threat Intelligence)
- ISO/IEC 27002:2022 Control A.8.27
- MITRE ATT&CK Framework
- STRIDE Methodology (Microsoft)
- PASTA Threat Modelling Framework

---

# Technical Specification


> Auto-generated from `generate_a827_2_threat_modelling.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.27.2` |
| **Output Filename** | `ISMS-IMP-A.8.27.2_Threat_Modelling_Methodology_YYYYMMDD.xlsx` |
| **Workbook Title** | Threat Modelling Methodology |
| **Total Sheets** | 10 (10 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #1F4E79 | header_bg | Custom |
| #2E75B6 | subheader_bg | Custom |
| #E2EFDA | input_cell | Pale Green (Success Background) |
| #FFF2CC | formula_cell | Cream (Input Alt) |

## Sheet 1: Instructions

---

## Sheet 2: Methodology

**Data Rows:** 8 (rows 1–8)

### Columns

| Col | Header |
|-----|--------|
| A | Meth-ID |
| B | Category |
| C | Requirement |
| D | Adopted |
| E | Documented |
| F | Effective |
| G | Evidence |
| H | Gaps |

---

## Sheet 3: Mitre_Attack

**Data Rows:** 7 (rows 1–7)

### Columns

| Col | Header |
|-----|--------|
| A | ATT-ID |
| B | Tactic |
| C | Technique |
| D | Relevance |
| E | Covered |
| F | DetectionMap |
| G | Gap |

---

## Sheet 4: Threat_Catalogue

**Data Rows:** 8 (rows 1–8)

### Columns

| Col | Header |
|-----|--------|
| A | Threat-ID |
| B | Category |
| C | ThreatActor |
| D | Motivation |
| E | Capability |
| F | ATT&CK_Ref |
| G | Likelihood |
| H | Countermeasures |

---

## Sheet 5: Tools

**Data Rows:** 8 (rows 1–8)

### Columns

| Col | Header |
|-----|--------|
| A | Tool-ID |
| B | Tool |
| C | Purpose |
| D | Licensed |
| E | Users |
| F | Integration |
| G | Effectiveness |
| H | Gaps |

---

## Sheet 6: Competency

**Data Rows:** 8 (rows 1–8)

### Columns

| Col | Header |
|-----|--------|
| A | Comp-ID |
| B | Role |
| C | Competency |
| D | Required |
| E | Training |
| F | Certified |
| G | Target |
| H | Gap |

---

## Sheet 7: Samples

**Data Rows:** 10 (rows 4–13)

### Columns

| Col | Header |
|-----|--------|
| A | Sample-ID |
| B | System |
| C | Date |
| D | Author |
| E | Methodology |
| F | Completeness |
| G | Quality |
| H | ATT&CK_Mapped |
| I | Findings |
| J | Mitigated |

---

## Sheet 8: Compliance

**Data Rows:** 7 (rows 1–7)

### Columns

| Col | Header |
|-----|--------|
| A | Comp-ID |
| B | Requirement |
| C | Source |
| D | Compliant |
| E | Evidence |
| F | Score |
| G | Notes |

---

## Sheet 9: Gap_Register

**Data Rows:** 20 (rows 4–23)

### Columns

| Col | Header |
|-----|--------|
| A | Gap-ID |
| B | Source |
| C | Description |
| D | Risk |
| E | Remediation |
| F | Owner |
| G | Due Date |
| H | Status |
| I | Closure Date |
| J | Notes |

---

## Sheet 10: Dashboard

---

**END OF SPECIFICATION**

---

*"If you know the enemy and know yourself, you need not fear the result of a hundred battles."*
— Sun Tzu, The Art of War

<!-- QA_VERIFIED: [Date] -->
