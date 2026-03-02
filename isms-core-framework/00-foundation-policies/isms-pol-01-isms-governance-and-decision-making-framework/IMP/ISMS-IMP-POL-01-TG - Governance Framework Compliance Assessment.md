<!-- ISMS-CORE:IMP:ISMS-IMP-POL-01-TG:framework:TG:00 -->
**ISMS-IMP-POL-01-TG — Governance Framework Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Clause 5.3: Roles, Responsibilities and Authorities

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Governance Framework Compliance Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-POL-01-TG |
| **Related Policy** | ISMS-POL-01 (ISMS Governance and Decision-Making Framework) |
| **Control Reference** | ISO/IEC 27001:2022 Clause 5.3 (Roles, responsibilities and authorities) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- ISMS-POL-01 (ISMS Governance and Decision-Making Framework)
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-POL-01-UG (Governance Framework Compliance Assessment — User Guide)
- ISMS-INS-POL-01 (Implementation Guide)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

> Auto-generated from `ISMS-SCR-CHK-POL-01.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 generate_tg_from_scr.py --single .../SCR/ISMS-SCR-CHK-POL-01.py`

**Document ID:** `ISMS-CHK-POL-01`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-CHK-POL-01` |
| **Workbook Title** | Governance Framework Compliance Assessment |
| **Total Sheets** | 9 (9 visible) |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #808080 | 808080 | Gray (Disabled) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

**Frozen Panes:** A4

---

## Sheet 2: Domain 1 - Authority

**Data Rows:** 4 (rows 5–8) | **Frozen Panes:** A4

### Requirements

| ID | Requirement |
|----|-------------|
| GOV-01 | Technical control implementations approved by CISO (verify POL approval signatures) |
| GOV-02 | Regulatory applicability determinations approved by Legal/Compliance (verify POL-00 Section 8 approvals) |
| GOV-03 | Risk acceptance decisions approved by Executive Management (verify Risk Acceptance Register signatures) |
| GOV-04 | Competence requirements verified for all decision-makers (verify Section 2.3 criteria: CISO, Legal, DPO, Executive Management) |

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Req_ID | 12 |
| B | Requirement | 60 |
| C | Compliance_Status | 18 |
| D | Evidence_Reference | 35 |
| E | Owner | 20 |
| F | Verified_Date | 15 |
| G | Notes | 30 |

### Data Validations

| Column | Range | Options |
|--------|-------|---------|
| C | C5:C8 | Compliant, Partial, Non-Compliant, N/A |

---

## Sheet 3: Domain 2 - Applicability

**Data Rows:** 4 (rows 5–8) | **Frozen Panes:** A4

### Requirements

| ID | Requirement |
|----|-------------|
| GOV-05 | POL-00 quarterly monitoring completed (verify 4 quarters have logs with Legal/Compliance + CISO signatures) |
| GOV-06 | Triggered assessments documented (verify business changes assessed per POL-00 Section 5) |
| GOV-07 | SoA justifications complete (verify all 93 controls documented with implementation status and rationale) |
| GOV-08 | Challenge Protocol followed if invoked (verify Section 3.3 execution if applicable) |

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Req_ID | 12 |
| B | Requirement | 60 |
| C | Compliance_Status | 18 |
| D | Evidence_Reference | 35 |
| E | Owner | 20 |
| F | Verified_Date | 15 |
| G | Notes | 30 |

### Data Validations

| Column | Range | Options |
|--------|-------|---------|
| C | C5:C8 | Compliant, Partial, Non-Compliant, N/A |

---

## Sheet 4: Domain 3 - Exceptions

**Data Rows:** 4 (rows 5–8) | **Frozen Panes:** A4

### Requirements

| ID | Requirement |
|----|-------------|
| GOV-09 | Exceptions follow 5-step process (verify Exception Register entries complete Steps 1–5) |
| GOV-10 | Residual risk assessed for all exceptions (verify Step 2 risk assessments with likelihood/impact/residual risk) |
| GOV-11 | Risk acceptances approved by Executive Management (verify Step 4 approvals: Alternative Control = CISO, Risk Acceptance = Executive Management) |
| GOV-12 | Exception volume within targets (Total <5%, Risk acceptances <3%, Deferred <2%, Overdue >90 days = 0) |

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Req_ID | 12 |
| B | Requirement | 60 |
| C | Compliance_Status | 18 |
| D | Evidence_Reference | 35 |
| E | Owner | 20 |
| F | Verified_Date | 15 |
| G | Notes | 30 |

### Data Validations

| Column | Range | Options |
|--------|-------|---------|
| C | C5:C8 | Compliant, Partial, Non-Compliant, N/A |

---

## Sheet 5: Domain 4 - Change Mgmt

**Data Rows:** 4 (rows 5–8) | **Frozen Panes:** A4

### Requirements

| ID | Requirement |
|----|-------------|
| GOV-13 | Compliance criteria changes documented (verify ISMS Change Log entries with trigger, affected controls, rationale, approval) |
| GOV-14 | Changes follow 6-step process (verify Steps 1–6: Identify, Assess impact, Propose, Approve, Implement, Verify) |
| GOV-15 | Reassessments completed within 90 days (verify Gap Register: completion rate >95%, overdue items = 0) |
| GOV-16 | Changes verified by internal audit (verify Step 6: internal audit reports covering changed controls) |

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Req_ID | 12 |
| B | Requirement | 60 |
| C | Compliance_Status | 18 |
| D | Evidence_Reference | 35 |
| E | Owner | 20 |
| F | Verified_Date | 15 |
| G | Notes | 30 |

### Data Validations

| Column | Range | Options |
|--------|-------|---------|
| C | C5:C8 | Compliant, Partial, Non-Compliant, N/A |

---

## Sheet 6: Domain 5 - Governance Review

**Data Rows:** 4 (rows 5–8) | **Frozen Panes:** A4

### Requirements

| ID | Requirement |
|----|-------------|
| GOV-17 | Annual governance review completed (verify Section 6.1 meeting minutes with Executive Management attendance) |
| GOV-18 | Review covers all 6 required topics (Authority boundaries, Applicability framework, Exception handling, Change management, Auditor feedback, Governance efficiency) |
| GOV-19 | Continual improvement actions documented (verify actions assigned with owners, due dates, and status tracking) |
| GOV-20 | Lessons learned register maintained (verify Section 6.2 register has: Date, Event, Lesson, Action, Status, Verified) |

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Req_ID | 12 |
| B | Requirement | 60 |
| C | Compliance_Status | 18 |
| D | Evidence_Reference | 35 |
| E | Owner | 20 |
| F | Verified_Date | 15 |
| G | Notes | 30 |

### Data Validations

| Column | Range | Options |
|--------|-------|---------|
| C | C5:C8 | Compliant, Partial, Non-Compliant, N/A |

---

## Sheet 7: Evidence Register

**Data Rows:** 100 (rows 6–105) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 15 |
| B | Evidence Title | 40 |
| C | Evidence Type | 20 |
| D | Description | 50 |
| E | Source / Location | 35 |
| F | Date Collected | 15 |
| G | Collected By | 20 |
| H | Status | 15 |

### Data Validations

| Column | Range | Options |
|--------|-------|---------|
| C | C6:C105 | Document, Screenshot, Log, Report, Certificate, Interview, Observation, Other |
| H | H6:H105 | Compliant, Partial, Non-Compliant, N/A |

---

## Sheet 8: Summary Dashboard

**Data Rows:** 5 domains (rows 2–7) | **Frozen Panes:** A6

### Columns

| Col | Header |
|-----|--------|
| A | Assessment Domain |
| B | Total Requirements |
| C | Compliant |
| D | Partially Compliant |
| E | Non-Compliant |
| F | N/A |
| G | Compliance % |

### Domain Mapping

| Row | Domain | Requirements |
|-----|--------|-------------|
| 2 | Domain 1 - Authority Boundaries | GOV-01 to GOV-04 |
| 3 | Domain 2 - Applicability Decisions | GOV-05 to GOV-08 |
| 4 | Domain 3 - Exception Handling | GOV-09 to GOV-12 |
| 5 | Domain 4 - Change Management | GOV-13 to GOV-16 |
| 6 | Domain 5 - Governance Review | GOV-17 to GOV-20 |

---

## Sheet 9: Approval Sign-Off

**Data Rows:** 5 (rows 1–5) | **Frozen Panes:** A3

---

**END OF SPECIFICATION**

---

<!-- QA_VERIFIED: 2026-03-02 -->
