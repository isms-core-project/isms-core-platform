**ISMS-IMP-A.8.27.1-TG - Security Architecture Review Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Security Architecture Review Process |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.1-TG |
| **Assessment Domain** | Domain 1 - Architecture Review Governance |
| **Related Policy** | ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Security Architect / Enterprise Architect |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect | Initial architecture review assessment specification |

**Review Cycle**: Annual (or after major architecture changes)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles)
- ISMS-IMP-A.8.27.2 (Threat Modelling Methodology)
- ISMS-IMP-A.8.27.3 (Secure Architecture Pattern Catalogue)
- ISMS-IMP-A.8.27.4 (Zero Trust Implementation Assessment)
- ISMS-POL-A.8.25-26-29 (Secure Development Framework)
- ISO/IEC 27002:2022 Control A.8.27
- NIST SP 800-160 Vol. 1 Rev. 1 (Engineering Trustworthy Secure Systems)
- INCOSE Systems Engineering Handbook, 5th Edition (2023)

---

# Technical Specification

# Excel Workbook Specification

## Workbook Overview

| Property | Value |
|----------|-------|
| **Filename** | ISMS-IMP-A.8.27.1_Security_Architecture_Review_Process_YYYYMMDD.xlsx |
| **Sheets** | 9 |
| **Purpose** | Security architecture review process assessment |
| **Generator** | generate_a827_1_architecture_review.py |

## Sheet Specifications

### Sheet 1: Instructions

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Instructions |
| **Purpose** | User guidance and reference |
| **Protection** | Read-only (protected) |

**Content Sections:**

1. Document header with ISMS branding
2. Assessment purpose and scope
3. Completion instructions
4. Rating scale definitions
5. Evidence requirements
6. Contact information
7. Version and date information

### Sheet 2: Governance

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Governance |
| **Purpose** | Architecture review governance assessment |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gov-ID | 10 | Auto | GOV-001 format |
| B | Category | 20 | Dropdown | Policy/Procedures/Roles/Authority/Exceptions |
| C | Requirement | 40 | Text | Required |
| D | Status | 15 | Dropdown | Implemented/Partial/Not Implemented/N/A |
| E | Evidence | 40 | Text | Required if Implemented |
| F | Gap | 40 | Text | Required if Not Implemented |
| G | Owner | 20 | Text | Required |
| H | Notes | 30 | Text | Optional |

**Pre-populated Rows:** 15 governance requirements from ISMS-POL-A.8.27

### Sheet 3: Process

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Process |
| **Purpose** | Review process assessment |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Proc-ID | 10 | Auto | PROC-001 format |
| B | Phase | 15 | Dropdown | Trigger/Planning/Execution/Documentation/Approval/Follow-up |
| C | Activity | 40 | Text | Required |
| D | Documented | 12 | Dropdown | Yes/Partial/No |
| E | Implemented | 12 | Dropdown | Yes/Partial/No |
| F | Evidence | 30 | Text | Required |
| G | Effectiveness | 12 | Dropdown | 1/2/3/4/5 |
| H | Notes | 30 | Text | Optional |

**Pre-populated Rows:** 25 process activities

### Sheet 4: Templates

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Templates |
| **Purpose** | Documentation templates assessment |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Temp-ID | 10 | Auto | TEMP-001 format |
| B | Template | 35 | Text | Required |
| C | Version | 10 | Text | Version format |
| D | Last Updated | 12 | Date | Date validation |
| E | Completeness | 12 | Dropdown | 1/2/3/4/5 |
| F | Usability | 12 | Dropdown | 1/2/3/4/5 |
| G | Gaps | 35 | Text | Optional |
| H | Notes | 25 | Text | Optional |

**Pre-populated Rows:** 8 expected templates

### Sheet 5: Integration

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Integration |
| **Purpose** | SDLC integration assessment |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Int-ID | 10 | Auto | INT-001 format |
| B | Integration | 30 | Text | Required |
| C | Trigger | 35 | Text | Required |
| D | Automated | 12 | Dropdown | Yes/Partial/No |
| E | Tracked | 12 | Dropdown | Yes/Partial/No |
| F | Enforced | 12 | Dropdown | Yes/Partial/No |
| G | Evidence | 30 | Text | Required |
| H | Notes | 25 | Text | Optional |

**Pre-populated Rows:** 8 integration points

### Sheet 6: Metrics

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Metrics |
| **Purpose** | Review effectiveness metrics |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Met-ID | 10 | Auto | MET-001 format |
| B | Metric | 35 | Text | Required |
| C | Period | 15 | Text | Required |
| D | Target | 12 | Percentage | 0-100% |
| E | Actual | 12 | Percentage | 0-100% |
| F | Trend | 10 | Dropdown | Up/Down/Stable |
| G | Action | 35 | Text | Required if Actual < Target |
| H | Notes | 25 | Text | Optional |

**Pre-populated Rows:** 10 recommended metrics

### Sheet 7: Compliance

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Compliance |
| **Purpose** | Policy compliance scoring |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Comp-ID | 10 | Auto | COMP-001 format |
| B | Requirement | 40 | Text | Required |
| C | Source | 20 | Text | Policy reference |
| D | Compliant | 12 | Dropdown | Yes/Partial/No |
| E | Evidence | 35 | Text | Required |
| F | Score | 10 | Formula | =IF(D="Yes",100,IF(D="Partial",50,0)) |
| G | Notes | 25 | Text | Optional |

**Pre-populated Rows:** 20 compliance requirements from ISMS-POL-A.8.27

### Sheet 8: GapRegister

| Property | Specification |
|----------|---------------|
| **Sheet Name** | GapRegister |
| **Purpose** | Gap tracking and remediation |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap-ID | 10 | Auto | GAP-001 format |
| B | Source | 15 | Dropdown | Sheet names |
| C | Description | 40 | Text | Required |
| D | Risk | 10 | Dropdown | High/Medium/Low |
| E | Remediation | 40 | Text | Required |
| F | Owner | 20 | Text | Required |
| G | Due Date | 12 | Date | Future date |
| H | Status | 12 | Dropdown | Open/In Progress/Closed |
| I | Closure Date | 12 | Date | Date validation |
| J | Notes | 25 | Text | Optional |

### Sheet 9: Dashboard

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Dashboard |
| **Purpose** | Summary and status view |
| **Protection** | Read-only (formulas only) |

**Dashboard Elements:**

1. **Overall Compliance Score:** Average of Compliance sheet scores
2. **Category Scores:** Governance, Process, Templates, Integration, Metrics
3. **Gap Summary:** Count by risk level (High/Medium/Low)
4. **Status Summary:** Open/In Progress/Closed gaps
5. **Trend Chart:** Placeholder for compliance trend
6. **Key Metrics:** Top 5 metrics with status indicators

## Styling Specifications

### Colour Palette

| Element | Colour Code | Usage |
|---------|-------------|-------|
| Header Background | #1F4E79 | Sheet headers |
| Header Text | #FFFFFF | Header text |
| Subheader Background | #2E75B6 | Section subheaders |
| Input Cell | #E2EFDA | User input cells |
| Formula Cell | #FFF2CC | Calculated cells |
| Compliant | #C6EFCE | Yes/Implemented status |
| Partial | #FFEB9C | Partial status |
| Non-Compliant | #FFC7CE | No/Not Implemented status |
| High Risk | #FF0000 | High risk gaps |
| Medium Risk | #FFA500 | Medium risk gaps |
| Low Risk | #FFFF00 | Low risk gaps |

### Font Standards

| Element | Font | Size | Style |
|---------|------|------|-------|
| Headers | Calibri | 14 | Bold |
| Subheaders | Calibri | 12 | Bold |
| Body Text | Calibri | 11 | Regular |
| Notes | Calibri | 10 | Italic |

### Cell Formatting

- All cells with borders (thin, black)
- Headers with bottom border (medium)
- Alternating row shading for readability (optional)
- Frozen panes for headers on all data sheets
- Column auto-filter enabled on data sheets

## Data Validation

### Dropdown Lists

Create named ranges for dropdown validation:

| Name | Values |
|------|--------|
| StatusList | Implemented, Partial, Not Implemented, N/A |
| YesNoPartial | Yes, Partial, No |
| RatingScale | 1, 2, 3, 4, 5 |
| RiskLevel | High, Medium, Low |
| GapStatus | Open, In Progress, Closed |
| TrendList | Up, Down, Stable |
| ProcessPhase | Trigger, Planning, Execution, Documentation, Approval, Follow-up |
| GovCategory | Policy, Procedures, Roles, Authority, Exceptions |

### Input Validation Rules

- Date fields: Valid date format, not in past for due dates
- Percentage fields: 0-100%
- Required fields: Cannot be blank
- Conditional: Evidence required when status is "Implemented"

## Formulas

### Compliance Score Calculation

```excel
# Individual requirement score
=IF(D2="Yes",100,IF(D2="Partial",50,0))

# Overall compliance score
=AVERAGE(F:F)
```

### Gap Summary Counts

```excel
# High risk gaps
=COUNTIF(GapRegister!D:D,"High")

# Open gaps
=COUNTIF(GapRegister!H:H,"Open")
```

### Category Scores

```excel
# Governance compliance
=AVERAGEIF(Compliance!C:C,"*GOV*",Compliance!F:F)
```

---

# Generator Script Reference

## Script Information

| Property | Value |
|----------|-------|
| **Script Name** | generate_a827_1_architecture_review.py |
| **Location** | 10-isms-scr-base/isms-a.8.27-secure-systems-engineering/10_generator-master/ |
| **Output** | ISMS-IMP-A.8.27.1_Security_Architecture_Review_Process_YYYYMMDD.xlsx |

## Script Structure

```python
# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.8.27.1"
WORKBOOK_NAME = "Security Architecture Review Process"
CONTROL_ID = "A.8.27"
CONTROL_NAME = "Secure System Architecture and Engineering Principles"
```

## Pre-populated Data

The generator should pre-populate the following:

**Governance Requirements (15 rows):**

1. Architecture review policy documented
2. Review procedures defined
3. Reviewer roles and responsibilities defined
4. Approval authority documented
5. Exception process established
6. Review scope criteria defined
7. Mandatory review triggers documented
8. Review timeline requirements specified
9. Documentation standards defined
10. Quality review process established
11. Training requirements specified
12. Escalation procedures documented
13. Integration with SDLC defined
14. Metrics and reporting requirements
15. Continuous improvement process

**Process Activities (25 rows):**

Organised by phase: Trigger (5), Planning (4), Execution (6), Documentation (4), Approval (3), Follow-up (3)

**Templates (8 rows):**

1. Security Architecture Document (SAD)
2. Threat Model Template
3. Architecture Review Checklist
4. Security Requirements Template
5. Risk Assessment Template
6. Architecture Decision Record (ADR)
7. Exception Request Form
8. Review Completion Report

**Integration Points (8 rows):**

1. Project initiation
2. Architecture design phase
3. Pre-development gate
4. Pre-production release
5. Major change requests
6. Third-party integration
7. Cloud service adoption
8. Post-incident architecture review

**Metrics (10 rows):**

1. Review coverage (% applicable projects reviewed)
2. Review timeliness (days from trigger to completion)
3. Finding closure rate (% high findings closed before release)
4. Bypass rate (% projects bypassing review)
5. Rework rate (% requiring re-review)
6. Template compliance (% using approved templates)
7. Documentation completeness (average documentation score)
8. Stakeholder satisfaction (survey score)
9. Time to approval (days from submission to approval)
10. Finding recurrence (% findings repeating)

**Compliance Requirements (20 rows):**

Mapped from ISMS-POL-A.8.27 Sections 2.2 and 4

---

**END OF SPECIFICATION**

---

*"Architecture is the foundation; security architecture is the foundation's foundation."*
— Gene Kim

<!-- QA_VERIFIED: [Date] -->
