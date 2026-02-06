**ISMS-IMP-A.8.27.5-TG - SSE Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Secure Systems Engineering Compliance Dashboard |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.5-TG |
| **Assessment Domain** | Domain 5 - Consolidated Dashboard |
| **Related Policy** | ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Security Architect |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect | Initial dashboard specification |

**Review Cycle**: Quarterly (aligned with ISMS reporting)
**Next Review Date**: [Effective Date + 3 months]

**Related Documents**:

- ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles)
- ISMS-IMP-A.8.27.1 (Security Architecture Review Process)
- ISMS-IMP-A.8.27.2 (Threat Modelling Methodology)
- ISMS-IMP-A.8.27.3 (Secure Architecture Pattern Catalogue)
- ISMS-IMP-A.8.27.4 (Zero Trust Implementation Assessment)

---

# Technical Specification

# Excel Workbook Specification

## Workbook Overview

| Property | Value |
|----------|-------|
| **Filename** | ISMS-IMP-A.8.27.5_SSE_Compliance_Dashboard_YYYYMMDD.xlsx |
| **Sheets** | 8 |
| **Purpose** | Consolidated SSE dashboard |
| **Generator** | generate_a827_5_dashboard.py |

## Sheet Specifications

### Sheet 1: Instructions

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Instructions |
| **Purpose** | Dashboard guidance |
| **Protection** | Read-only |

### Sheet 2: ExecutiveSummary

| Property | Specification |
|----------|---------------|
| **Sheet Name** | ExecutiveSummary |
| **Purpose** | High-level SSE status |

**Layout:**

Row 1-2: Title and date
Row 4-6: Overall SSE Score (large display)
Row 8-12: Domain status table (RAG)
Row 14-18: Key metrics
Row 20-25: Critical gaps summary
Row 27-30: Next steps and actions

### Sheet 3: DomainScores

| Property | Specification |
|----------|---------------|
| **Sheet Name** | DomainScores |
| **Purpose** | Compliance by domain |

**Column Definitions:**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Domain | 15 | Text |
| B | Name | 40 | Text |
| C | Assessment Date | 15 | Date |
| D | Compliance Score | 15 | Percentage |
| E | Gap Count | 12 | Number |
| F | High Risk Gaps | 12 | Number |
| G | Status | 10 | RAG |
| H | Trend | 10 | Arrow |
| I | Next Assessment | 15 | Date |

**Pre-populated Rows:**

| Domain | Name |
|--------|------|
| A.8.27.1 | Security Architecture Review Process |
| A.8.27.2 | Threat Modelling Methodology |
| A.8.27.3 | Secure Architecture Pattern Catalogue |
| A.8.27.4 | Zero Trust Implementation |

### Sheet 4: ZeroTrustRadar

| Property | Specification |
|----------|---------------|
| **Sheet Name** | ZeroTrustRadar |
| **Purpose** | ZT pillar maturity data |

**Column Definitions:**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Pillar | 15 | Text |
| B | Current Level | 15 | Dropdown |
| C | Current Score | 12 | Number (1-4) |
| D | Target Level | 15 | Dropdown |
| E | Target Score | 12 | Number (1-4) |
| F | Gap | 10 | Formula |
| G | Priority | 10 | Dropdown |

**Pre-populated Pillars:**

Identity, Device, Network, Workload, Data, Visibility, Automation

### Sheet 5: GapConsolidation

| Property | Specification |
|----------|---------------|
| **Sheet Name** | GapConsolidation |
| **Purpose** | All SSE gaps |

**Column Definitions:**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Gap-ID | 10 | Auto |
| B | Source Domain | 12 | Dropdown |
| C | Description | 45 | Text |
| D | Risk | 10 | Dropdown |
| E | Remediation | 40 | Text |
| F | Owner | 20 | Text |
| G | Due Date | 12 | Date |
| H | Status | 12 | Dropdown |
| I | Days Open | 10 | Formula |
| J | Overdue | 10 | Formula |

### Sheet 6: TrendAnalysis

| Property | Specification |
|----------|---------------|
| **Sheet Name** | TrendAnalysis |
| **Purpose** | Historical trends |

**Column Definitions:**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Period | 12 | Text |
| B | Overall Score | 12 | Percentage |
| C | Domain 1 | 12 | Percentage |
| D | Domain 2 | 12 | Percentage |
| E | Domain 3 | 12 | Percentage |
| F | Domain 4 | 12 | Percentage |
| G | Open Gaps | 10 | Number |
| H | High Gaps Closed | 15 | Number |

### Sheet 7: AuditEvidence

| Property | Specification |
|----------|---------------|
| **Sheet Name** | AuditEvidence |
| **Purpose** | Evidence inventory |

**Column Definitions:**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Evidence-ID | 12 | Auto |
| B | Domain | 12 | Dropdown |
| C | Description | 45 | Text |
| D | Location | 40 | Text |
| E | Date | 12 | Date |
| F | Status | 12 | Dropdown |
| G | Audit Use | 15 | Dropdown |

### Sheet 8: ActionTracker

| Property | Specification |
|----------|---------------|
| **Sheet Name** | ActionTracker |
| **Purpose** | Remediation tracking |

**Column Definitions:**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Action-ID | 10 | Auto |
| B | Gap-ID | 10 | Text |
| C | Action | 45 | Text |
| D | Owner | 20 | Text |
| E | Due Date | 12 | Date |
| F | Status | 15 | Dropdown |
| G | Completion Date | 15 | Date |
| H | Evidence | 35 | Text |

## Formulas

### Overall SSE Score

```excel
=AVERAGE(DomainScores!D4:D7)
```

Or weighted:

```excel
=(DomainScores!D4*0.25)+(DomainScores!D5*0.25)+(DomainScores!D6*0.20)+(DomainScores!D7*0.30)
```

### Days Open

```excel
=IF(H2="Closed","",TODAY()-G2)
```

### Overdue Flag

```excel
=IF(AND(H2<>"Closed",G2<TODAY()),"OVERDUE","")
```

### ZT Gap Calculation

```excel
=E2-C2
```

## Styling

Use standard ISMS colour palette with additional RAG indicators:

| Status | Colour |
|--------|--------|
| Green (≥80%) | #2ECC71 |
| Amber (60-79%) | #F39C12 |
| Red (<60%) | #E74C3C |

---

# Generator Script Reference

| Property | Value |
|----------|-------|
| **Script Name** | generate_a827_5_dashboard.py |
| **Location** | 10-isms-scr-base/isms-a.8.27-secure-systems-engineering/10_generator-master/ |
| **Output** | ISMS-IMP-A.8.27.5_SSE_Compliance_Dashboard_YYYYMMDD.xlsx |

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed. What gets reported gets improved."*
— Peter Drucker

<!-- QA_VERIFIED: [Date] -->
