**ISMS-IMP-A.8.27.5-UG - SSE Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Secure Systems Engineering Compliance Dashboard |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.5-UG |
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


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
