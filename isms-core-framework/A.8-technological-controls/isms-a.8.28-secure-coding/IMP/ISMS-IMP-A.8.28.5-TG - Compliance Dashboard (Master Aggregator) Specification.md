<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.28.5-TG:framework:TG:a.8.28.5 -->
**ISMS-IMP-A.8.28.5-TG - Compliance Dashboard (Master Aggregator) Specification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.28.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Compliance Dashboard & Master Aggregator |
| **Related Policy** | ISMS-POL-A.8.28 (All Sections) - Control A.8.28 Master Policy |
| **Purpose** | Aggregate compliance data from all four operational assessments (SDLC, Tools, Review/Testing, Supply Chain) to provide executive-level visibility and unified compliance tracking |
| **Target Audience** | CISO, CTO, Board of Directors, Audit Committee, Application Security Leadership, Risk Management, Auditors |
| **Assessment Type** | Consolidation & Reporting |
| **Review Cycle** | Quarterly (Aligned with Board Reporting Cycles) |
| **Date** | [Date]|

**Version History**:

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [Date] | Initial dashboard specification |

**Approvers**:

- Application Security Lead (Technical Review)
- Chief Information Security Officer (Executive Approval)
- Chief Technology Officer (Stakeholder Review)

**Related Documents**:

- ISMS-POL-A.8.28 - Secure Coding Policy (Master Policy)
- ISMS-IMP-A.8.28.1 - SDLC Assessment
- ISMS-IMP-A.8.28.2 - Standards & Tools Assessment
- ISMS-IMP-A.8.28.3 - Code Review & Testing Assessment
- ISMS-IMP-A.8.28.4 - Third-Party & OSS Assessment

---

# Technical Specification


> Auto-generated from `generate_a828_5_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.28.5` |
| **Output Filename** | `ISMS-IMP-A.8.28.5_Compliance_Summary_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance Summary Dashboard |
| **Total Sheets** | 18 (18 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #0000FF | 0000FF | Custom |
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #808080 | 808080 | Gray (Disabled) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Executive Dashboard

---

## Sheet 2: Gap Analysis

---

## Sheet 3: Risk Register

---

## Sheet 4: Remediation Roadmap

---

## Sheet 5: KPIs & Metrics

---

## Sheet 6: Evidence Register

---

## Sheet 7: Action Items & Follow-up

---

## Sheet 8: Audit & Compliance Log

---

## Sheet 9: Approval Sign-Off

---

## Sheet 10: Executive_Dashboard

**Data Rows:** 200 (rows 8–207) | **Frozen Panes:** A4

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIFS(` | Critical Gaps |
| — | `=COUNTIF(` | Remediation Progress |
| — | `=IF(C21>=95%,\` | Overall Compliance Status: |
| — | `=IF(C21>=90%,\` | Security Posture: |
| — | `=SUM(` | Total Estimated Remediation Budget: |

---

## Sheet 11: Gap_Analysis

**Data Rows:** 200 (rows 12–211) | **Frozen Panes:** A12

---

## Sheet 12: Risk_Register

**Data Rows:** 100 (rows 20–119) | **Frozen Panes:** A20

---

## Sheet 13: Remediation_Roadmap

**Data Rows:** 200 (rows 37–236) | **Frozen Panes:** A37

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(E37:E236)` | Total Remediation Items |
| — | `=COUNTIF(H37:H236,` | Completed |
| — | `=COUNTIFS(M37:M236,` | Overdue |
| — | `=SUM(R37:R236)` | Total Budget Required |
| — | `=SUM(T37:T236)` | Budget Utilized |

---

## Sheet 14: Kpis_Metrics

**Data Rows:** 200 (rows 12–211) | **Frozen Panes:** A4

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIFS(\` | Critical Risks - Open |
| — | `=SUM(\` | Residual Risk Exposure |
| — | `=COUNTIF(\` | Risks Accepted (No Remediation) |

---

## Sheet 15: Evidence_Register

**Data Rows:** 500 (rows 17–516) | **Frozen Panes:** A17

---

## Sheet 16: Action_Items

**Data Rows:** 200 (rows 22–221) | **Frozen Panes:** A22

---

## Sheet 17: Audit_Log

**Data Rows:** 100 (rows 19–118) | **Frozen Panes:** A19

---

## Sheet 18: Approval_Signoff

**Frozen Panes:** A3

---

**END OF SPECIFICATION**

---

*"Cryptographic systems should be designed to minimize the damage that can occur when they fail."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
