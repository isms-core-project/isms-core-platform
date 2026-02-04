**ISMS-IMP-A.8.27.5 — SSE Compliance Dashboard**
**Consolidated Assessment Dashboard Specification**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Secure Systems Engineering Compliance Dashboard |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.5 |
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

# PART I: USER COMPLETION GUIDE

# Dashboard Overview

## Purpose

This dashboard consolidates assessment data from all four A.8.27 assessment domains into a unified executive view for:

- **CISO Reporting:** Quarterly security posture reporting
- **Audit Readiness:** Evidence of SSE implementation for ISO 27001 audits
- **Trend Analysis:** Track SSE maturity improvements over time
- **Gap Prioritisation:** Consolidated view of all SSE-related gaps
- **Executive Communication:** High-level SSE status for leadership

## Data Sources

This dashboard consolidates data from:

| Source Workbook | Key Metrics |
|-----------------|-------------|
| **A.8.27.1** Architecture Review | Review coverage, timeliness, finding closure |
| **A.8.27.2** Threat Modelling | Methodology adoption, ATT&CK coverage, competency |
| **A.8.27.3** Pattern Catalogue | Pattern adoption, documentation quality, deviations |
| **A.8.27.4** Zero Trust | Pillar maturity scores, ZT compliance |

## Update Frequency

| Component | Update Frequency |
|-----------|------------------|
| Compliance Scores | Quarterly (after domain assessments) |
| Gap Register | Monthly (or when new gaps identified) |
| Trend Data | Quarterly |
| Zero Trust Maturity | Annual (or after major ZT initiatives) |

## Who Maintains This Dashboard

**Primary:** Security Architect or ISMS Manager

**Responsibilities:**
- Consolidate data from domain assessments quarterly
- Update trend charts with historical data
- Maintain gap register and track remediation
- Present to CISO and Executive Management

---

# Workbook Structure

## Sheet Overview

| Sheet | Purpose | Update Frequency |
|-------|---------|------------------|
| **Instructions** | Dashboard guidance | Read-only |
| **ExecutiveSummary** | High-level SSE status | Quarterly |
| **DomainScores** | Compliance by domain | Quarterly |
| **ZeroTrustRadar** | ZT pillar maturity | Annual |
| **GapConsolidation** | All SSE gaps | Monthly |
| **TrendAnalysis** | Historical trends | Quarterly |
| **AuditEvidence** | Evidence inventory | Before audits |
| **ActionTracker** | Remediation tracking | Monthly |

## Sheet Descriptions

### ExecutiveSummary Sheet

Single-page executive view:

| Section | Content |
|---------|---------|
| **Overall SSE Score** | Weighted average across domains |
| **Domain Status** | RAG status for each domain |
| **Key Metrics** | Top 5 KPIs |
| **Critical Gaps** | High-priority gaps requiring attention |
| **Trend Indicator** | Improving/Stable/Declining |
| **Next Steps** | Priority actions for next quarter |

### DomainScores Sheet

Detailed compliance by domain:

| Column | Description |
|--------|-------------|
| Domain | Assessment domain (A.8.27.1-4) |
| Assessment Date | Date of last assessment |
| Compliance Score | Overall compliance percentage |
| Gap Count | Number of open gaps |
| High Risk Gaps | Count of high-risk gaps |
| Status | RAG status |
| Trend | Up/Down/Stable |
| Next Assessment | Scheduled date |

### ZeroTrustRadar Sheet

Zero Trust maturity visualisation data:

| Column | Description |
|--------|-------------|
| Pillar | ZT pillar (Identity, Device, Network, etc.) |
| Current Level | Current maturity (Traditional/Initial/Advanced/Optimal) |
| Current Score | Numeric score (1-4) |
| Target Level | Target maturity |
| Target Score | Target numeric score |
| Gap | Difference between target and current |
| Priority | Implementation priority |

### GapConsolidation Sheet

Consolidated gap register from all domains:

| Column | Description |
|--------|-------------|
| Gap-ID | Unique gap identifier |
| Source Domain | Which assessment identified (1-4) |
| Description | Gap description |
| Risk | High/Medium/Low |
| Remediation | Planned remediation |
| Owner | Responsible party |
| Due Date | Target completion |
| Status | Open/In Progress/Closed |
| Days Open | Calculated days since identification |
| Overdue | Flag if past due date |

### TrendAnalysis Sheet

Historical trend data:

| Column | Description |
|--------|-------------|
| Period | Quarter (Q1 2026, etc.) |
| Overall Score | Consolidated SSE score |
| Domain 1 Score | Architecture Review score |
| Domain 2 Score | Threat Modelling score |
| Domain 3 Score | Pattern Catalogue score |
| Domain 4 Score | Zero Trust score |
| Open Gaps | Total open gaps |
| High Gaps Closed | High-risk gaps remediated |

### AuditEvidence Sheet

Evidence inventory for audits:

| Column | Description |
|--------|-------------|
| Evidence-ID | Unique evidence identifier |
| Domain | Related domain |
| Description | Evidence description |
| Location | Storage location/link |
| Date | Evidence date |
| Status | Available/Pending/Missing |
| Audit Use | Stage 1/Stage 2/Both |

### ActionTracker Sheet

Remediation action tracking:

| Column | Description |
|--------|-------------|
| Action-ID | Unique action identifier |
| Gap-ID | Related gap |
| Action | Specific action required |
| Owner | Responsible party |
| Due Date | Target completion |
| Status | Not Started/In Progress/Completed |
| Completion Date | Actual completion date |
| Evidence | Evidence of completion |

---

# Completion Walkthrough

## Initial Setup

1. **Complete Domain Assessments:** Ensure all 4 domain assessments (A.8.27.1-4) are completed
2. **Open Dashboard Workbook:** Open this consolidated dashboard
3. **Import Domain Scores:** Transfer compliance scores from each domain workbook
4. **Consolidate Gaps:** Copy all open gaps from domain gap registers
5. **Calculate Overall Score:** Verify formula calculations

## Quarterly Update Process

1. **Refresh Domain Assessments:** Update each domain workbook with current status
2. **Transfer Scores:** Update DomainScores sheet with latest compliance percentages
3. **Update Gaps:** Add new gaps, update status of existing gaps, close resolved gaps
4. **Record Trend Data:** Add new row to TrendAnalysis with current period data
5. **Update Executive Summary:** Refresh high-level status and key messages
6. **Review with CISO:** Present dashboard for quarterly review

## Annual ZT Update

1. **Complete A.8.27.4 Assessment:** Full Zero Trust maturity assessment
2. **Update ZeroTrustRadar:** Transfer pillar scores to radar data sheet
3. **Adjust Targets:** Review and update ZT maturity targets if needed
4. **Document Progress:** Note significant ZT achievements

---

# Evidence Collection

## Dashboard Evidence

| Evidence | Purpose | Storage |
|----------|---------|---------|
| Quarterly Dashboard Exports | Audit trail of SSE status | ISMS Evidence Library |
| Trend Charts | Demonstrate improvement | ISMS Evidence Library |
| Gap Closure Records | Remediation evidence | ISMS Evidence Library |
| CISO Review Minutes | Governance evidence | ISMS Evidence Library |

---

# Common Pitfalls

❌ **MISTAKE:** Dashboard not updated after domain assessments
✅ **CORRECT:** Update dashboard within 5 days of completing domain assessments

❌ **MISTAKE:** Gaps tracked in dashboard only, not domain workbooks
✅ **CORRECT:** Gaps should exist in source domain and be consolidated to dashboard

❌ **MISTAKE:** Historical trend data not maintained
✅ **CORRECT:** Always add new period data to TrendAnalysis before overwriting

❌ **MISTAKE:** Overall score manually entered instead of calculated
✅ **CORRECT:** Use formula to calculate weighted average from domain scores

❌ **MISTAKE:** Dashboard reviewed but actions not tracked
✅ **CORRECT:** All identified actions must be logged in ActionTracker

❌ **MISTAKE:** Evidence inventory not maintained between audits
✅ **CORRECT:** Update AuditEvidence continuously, not just before audits

---

# PART II: TECHNICAL SPECIFICATION

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
