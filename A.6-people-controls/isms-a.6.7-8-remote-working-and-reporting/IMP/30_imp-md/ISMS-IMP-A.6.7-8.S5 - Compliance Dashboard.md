**ISMS-IMP-A.6.7-8.S5 - Remote Working and Event Reporting Compliance Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S5 |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Compliance Metrics and Executive Reporting |
| **Related Policy** | ISMS-POL-A.6.7-8 (All Sections) |
| **Purpose** | Consolidate compliance data from S1-S4 assessments into executive dashboard |
| **Target Audience** | CISO, IT Security Manager, Executive Management, Auditors |
| **Assessment Type** | Consolidation Dashboard |
| **Review Cycle** | Quarterly (or as S1-S4 are updated) |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for compliance dashboard | ISMS Implementation Team |

---

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Dashboard Overview
  - Prerequisites
  - Data Import Workflow
  - Sheet-by-Sheet Guidance
  - Metric Interpretation
  - Reporting Use Cases
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Workbook Structure
  - Data Import Specifications
  - Formula Specifications
  - Visualization Specifications
  - Styling Reference

**Target Audiences:**

- **Part I:** Dashboard users (CISO, IT Security Manager, Executive Management)
- **Part II:** Workbook developers (Python/Excel script maintainers)

---

# PART I: USER COMPLETION GUIDE

**Audience:** CISO, IT Security Manager, Executive Management, Auditors

---

## 1. Dashboard Overview

### 1.1 Purpose

This compliance dashboard consolidates metrics from the four component assessments (S1-S4) to provide:
- Executive-level visibility into remote working and event reporting compliance
- Trend tracking across assessment periods
- Gap prioritization and remediation tracking
- Audit-ready compliance evidence
- Integration with Statement of Applicability (SoA) reporting

### 1.2 Scope

This dashboard consolidates:
- **S1 Metrics**: Remote work authorization compliance
- **S2 Metrics**: Technical controls (VPN, MFA, encryption) compliance
- **S3 Metrics**: Endpoint and physical security compliance
- **S4 Metrics**: Event reporting mechanisms effectiveness

### 1.3 Key Metrics

| Metric | Source | Target |
|--------|--------|--------|
| Authorization Compliance Rate | S1 | ≥95% |
| VPN/MFA Coverage | S2 | 100% |
| Encryption Compliance | S2, S3 | 100% |
| Endpoint Protection Coverage | S3 | ≥98% |
| Patch Compliance Rate | S3 | ≥95% |
| Reporting Channel Accessibility | S4 | 100% |
| Response SLA Compliance | S4 | ≥90% |
| Overall Control Compliance | All | ≥90% |

### 1.4 Target Audience

- **Primary Users**: CISO, IT Security Manager
- **Executive Consumers**: Executive Management, Board
- **Auditors**: Internal and External Auditors
- **Operational Users**: IT Security Team

### 1.5 Update Frequency

| Trigger | Frequency |
|---------|-----------|
| Scheduled Update | Quarterly |
| Post-Assessment Update | After any S1-S4 assessment |
| Management Review | Before management review meetings |
| Audit Preparation | Before Stage 1/Stage 2 audits |

## 2. Prerequisites

Before updating this dashboard, ensure:

| Prerequisite | Status | Notes |
|--------------|--------|-------|
| S1 Assessment completed | ☐ | Remote Work Authorization |
| S2 Assessment completed | ☐ | Technical Controls |
| S3 Assessment completed | ☐ | Endpoint & Physical Security |
| S4 Assessment completed | ☐ | Event Reporting |
| S1-S4 workbooks accessible | ☐ | For data import |
| Previous dashboard version | ☐ | For trend comparison |

## 3. Data Import Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1: Collect Component Workbooks                           │
│  - Obtain latest S1, S2, S3, S4 workbooks                       │
│  - Verify assessment dates are current                          │
│  - Confirm approvals are complete                               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  STEP 2: Import Dashboard Metrics                              │
│  - Extract key metrics from each workbook                       │
│  - Update Metrics_Import sheet                                  │
│  - Verify calculations are correct                              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  STEP 3: Consolidate Gaps                                       │
│  - Import open gaps from each Gap_Analysis sheet                │
│  - Update priority and status                                   │
│  - Verify owner assignments                                     │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  STEP 4: Update Trend Data                                      │
│  - Record current period metrics                                │
│  - Compare to previous periods                                  │
│  - Update trend visualizations                                  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  STEP 5: Review & Approve                                       │
│  - Technical review of data accuracy                            │
│  - Management review of findings                                │
│  - Approve for distribution                                     │
└─────────────────────────────────────────────────────────────────┘
```

## 4. Sheet-by-Sheet Completion Guide

### 4.1 Instructions Sheet

**Purpose**: Provides guidance for dashboard users.

### 4.2 Executive_Summary Sheet

**Purpose**: High-level compliance status for executive consumption.

**Content**:
- Overall compliance score (aggregate)
- Control-by-control compliance (A.6.7 and A.6.8 separately)
- Top 3 risks requiring attention
- Trend indicator (improving/stable/declining)
- Assessment period and dates

**Presentation**: Designed for presentation to executive management and board.

### 4.3 Metrics_Import Sheet

**Purpose**: Import metrics from S1-S4 component assessments.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Source Workbook | S1/S2/S3/S4 | Dropdown |
| Metric Name | Name of metric being imported | Free text |
| Metric Value | Current value | Number/Percentage |
| Target Value | Target for compliance | Number/Percentage |
| Compliant | Value meets target | Formula |
| Assessment Date | Date of source assessment | Date |
| Source Cell | Cell reference in source | Free text |
| Notes | Any adjustments or notes | Free text |

### 4.4 Control_Compliance Sheet

**Purpose**: Detailed compliance breakdown by control (A.6.7 and A.6.8).

**Structure**:
- **Section A.6.7 - Remote Working**
  - Authorization compliance
  - Technical controls compliance
  - Endpoint security compliance
  - Physical security compliance

- **Section A.6.8 - Event Reporting**
  - Reporting channel availability
  - Procedure documentation
  - Awareness coverage
  - Response effectiveness

### 4.5 Gap_Consolidation Sheet

**Purpose**: Consolidated view of all open gaps from S1-S4.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Gap ID | Original gap ID from source | Text |
| Source | S1/S2/S3/S4 | Dropdown |
| Gap Description | Description of gap | Free text |
| Risk Level | High/Medium/Low | Dropdown |
| Remediation Action | Required action | Free text |
| Owner | Responsible party | Free text |
| Target Date | Due date | Date |
| Status | Open/In Progress/Closed | Dropdown |
| Days Open | Days since identified | Calculated |
| Overdue | Is remediation overdue | Formula |

### 4.6 Trend_Analysis Sheet

**Purpose**: Track compliance metrics over time.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Period | Assessment period (Q1 2026, etc.) | Free text |
| Assessment Date | Date of assessment | Date |
| Authorization Compliance | S1 metric | Percentage |
| Technical Compliance | S2 metric | Percentage |
| Endpoint Compliance | S3 metric | Percentage |
| Reporting Compliance | S4 metric | Percentage |
| Overall Compliance | Aggregate | Percentage |
| Open Gaps | Total open gaps | Number |
| High-Risk Gaps | High priority gaps | Number |

**Visualization**: Line chart showing compliance trends over time.

### 4.7 Risk_Assessment Sheet

**Purpose**: Risk-based view of non-compliance.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Risk Area | Area of non-compliance | Free text |
| Current State | Current compliance level | Percentage |
| Gap to Target | Difference from target | Percentage |
| Impact | Business impact if exploited | Dropdown |
| Likelihood | Likelihood of exploitation | Dropdown |
| Risk Score | Impact × Likelihood | Calculated |
| Mitigation Status | Mitigation progress | Dropdown |
| Risk Owner | Accountable executive | Free text |

### 4.8 SoA_Integration Sheet

**Purpose**: Map dashboard results to Statement of Applicability.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Control ID | A.6.7 or A.6.8 | Pre-populated |
| Control Name | Control title | Pre-populated |
| Applicable | Is control applicable | Yes |
| Implementation Status | Implemented/Partial/Planned | Dropdown |
| Compliance % | Compliance percentage | Percentage |
| Evidence Reference | Link to evidence | Free text |
| Last Assessment | Date of last assessment | Date |
| Notes | SoA notes | Free text |

### 4.9 Audit_Summary Sheet

**Purpose**: Audit-ready summary for Stage 1/Stage 2 audits.

**Content**:
- Control implementation status (A.6.7, A.6.8)
- Key evidence references
- Non-conformities and status
- Improvement opportunities
- Management commitment evidence

### 4.10 Evidence_Index Sheet

**Purpose**: Master index of evidence across all S1-S4 assessments.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Evidence ID | Unique identifier | Auto-generated |
| Source Assessment | S1/S2/S3/S4 | Dropdown |
| Evidence Type | Document/Screenshot/Report/etc. | Dropdown |
| Description | What evidence demonstrates | Free text |
| Location | File/folder location | Free text |
| Audit Relevance | Stage 1/Stage 2/Both | Dropdown |
| Last Updated | When evidence was collected | Date |

### 4.11 Dashboard Sheet

**Purpose**: Visual dashboard for at-a-glance status.

**Visualizations**:
- Gauge charts for each compliance metric
- Bar chart comparing current vs. target
- Pie chart of gap distribution by severity
- Trend sparklines for key metrics
- RAG status indicators

### 4.12 Approval_Sign_Off Sheet

**Purpose**: Document formal review and approval.

**Sections**:
1. **Data Accuracy Certification**: IT Security confirms data is accurate
2. **Management Review**: CISO review and approval
3. **Distribution Authorization**: Approval for distribution
4. **Next Review Date**: Scheduled next update

## 5. Metric Interpretation

### 5.1 Compliance Thresholds

| Threshold | Status | Action |
|-----------|--------|--------|
| ≥95% | Green | Maintain, continuous improvement |
| 80-94% | Yellow | Improvement needed, track closely |
| <80% | Red | Immediate attention required |

### 5.2 Trend Indicators

| Trend | Meaning | Action |
|-------|---------|--------|
| ↑ Improving | Metrics improving over periods | Continue current approach |
| → Stable | Metrics consistent | Look for improvement opportunities |
| ↓ Declining | Metrics worsening | Investigate root cause, escalate |

### 5.3 Risk Prioritization

| Risk Score | Priority | Response Time |
|------------|----------|---------------|
| High (>15) | Critical | Immediate action |
| Medium (8-15) | High | Within 30 days |
| Low (<8) | Normal | Within 90 days |

## 6. Reporting Use Cases

### 6.1 Executive Reporting

**Frequency**: Quarterly
**Content**: Executive_Summary, Dashboard
**Audience**: Executive Management, Board
**Format**: PDF export or presentation

### 6.2 Management Review

**Frequency**: Per ISMS management review cycle
**Content**: Control_Compliance, Gap_Consolidation, Trend_Analysis
**Audience**: CISO, IT Security Manager
**Format**: Full workbook with discussion

### 6.3 Audit Support

**Frequency**: As needed for audits
**Content**: SoA_Integration, Audit_Summary, Evidence_Index
**Audience**: Internal/External Auditors
**Format**: Full workbook with evidence package

### 6.4 Operational Tracking

**Frequency**: Monthly
**Content**: Gap_Consolidation, Metrics_Import
**Audience**: IT Security Team
**Format**: Workbook for operational tracking

## 7. Quality Checklist

Before distributing dashboard, verify:

- [ ] All S1-S4 metrics imported correctly
- [ ] Calculations verified (spot-check)
- [ ] Gaps consolidated and current
- [ ] Trend data updated
- [ ] Visualizations rendering correctly
- [ ] Evidence index complete
- [ ] SoA integration accurate
- [ ] Management approval obtained

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook Developers (Python/Excel Script Maintainers)

---

## 8. Workbook Architecture

### 8.1 Sheet Structure

| Sheet Name | Purpose | Sheet Type |
|------------|---------|------------|
| Instructions | User guidance | Static |
| Executive_Summary | Executive overview | Summary |
| Metrics_Import | Data import from S1-S4 | Import |
| Control_Compliance | Detailed compliance | Analysis |
| Gap_Consolidation | Consolidated gaps | Analysis |
| Trend_Analysis | Trend tracking | Analysis |
| Risk_Assessment | Risk-based view | Analysis |
| SoA_Integration | SoA mapping | Integration |
| Audit_Summary | Audit support | Summary |
| Evidence_Index | Evidence master list | Register |
| Dashboard | Visual dashboard | Calculated |
| Approval_Sign_Off | Formal approvals | Governance |

### 8.2 Data Dependencies

```
S1 Workbook ──┐
S2 Workbook ──┼──→ Metrics_Import ──→ Control_Compliance
S3 Workbook ──┤                   └──→ Dashboard
S4 Workbook ──┘                   └──→ Executive_Summary

S1 Gap_Analysis ──┐
S2 Gap_Analysis ──┼──→ Gap_Consolidation ──→ Risk_Assessment
S3 Gap_Analysis ──┤
S4 Gap_Analysis ──┘

Historical Data ──→ Trend_Analysis
```

## 9. Column Specifications

### 9.1 Metrics_Import Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Source Workbook | 12 | Dropdown | S1/S2/S3/S4 |
| B | Metric Name | 40 | Text | Free text |
| C | Metric Value | 15 | Number | Percentage or number |
| D | Target Value | 15 | Number | Percentage or number |
| E | Compliant | 12 | Formula | =C>=D |
| F | Assessment Date | 15 | Date | Date format |
| G | Source Cell | 15 | Text | Cell reference |
| H | Notes | 40 | Text | Free text |

### 9.2 Gap_Consolidation Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap ID | 15 | Text | From source |
| B | Source | 8 | Dropdown | S1/S2/S3/S4 |
| C | Gap Description | 50 | Text | Free text |
| D | Risk Level | 12 | Dropdown | High/Medium/Low |
| E | Remediation Action | 50 | Text | Free text |
| F | Owner | 20 | Text | Free text |
| G | Target Date | 12 | Date | Date format |
| H | Status | 15 | Dropdown | Open/In Progress/Closed |
| I | Days Open | 12 | Formula | =TODAY()-[Created Date] |
| J | Overdue | 10 | Formula | =AND(G<TODAY(),H<>"Closed") |

## 10. Formula Specifications

### 10.1 Overall Compliance Calculation

**Weighted Average**:
```
Overall = (S1_Compliance * 0.20) + (S2_Compliance * 0.30) +
          (S3_Compliance * 0.30) + (S4_Compliance * 0.20)
```

Weights reflect relative importance:
- S1 (Authorization): 20%
- S2 (Technical): 30%
- S3 (Endpoint/Physical): 30%
- S4 (Event Reporting): 20%

### 10.2 Control-Level Compliance

**A.6.7 Compliance**:
```
= AVERAGE(S1_Compliance, S2_Compliance, S3_Compliance)
```

**A.6.8 Compliance**:
```
= S4_Compliance
```

### 10.3 Gap Metrics

**Open Gaps by Severity**:
```
High: =COUNTIFS(Gap_Consolidation!D:D,"High",Gap_Consolidation!H:H,"<>Closed")
Medium: =COUNTIFS(Gap_Consolidation!D:D,"Medium",Gap_Consolidation!H:H,"<>Closed")
Low: =COUNTIFS(Gap_Consolidation!D:D,"Low",Gap_Consolidation!H:H,"<>Closed")
```

**Overdue Gaps**:
```
=COUNTIF(Gap_Consolidation!J:J,TRUE)
```

## 11. Visualization Specifications

### 11.1 Gauge Charts

**Compliance Gauges**:
- Red zone: 0-79%
- Yellow zone: 80-94%
- Green zone: 95-100%
- Needle position based on current value

### 11.2 Trend Chart

**Line Chart Configuration**:
- X-axis: Assessment periods
- Y-axis: Compliance percentage (0-100%)
- Series: Overall, S1, S2, S3, S4
- Target line at 95%

### 11.3 Gap Distribution

**Pie Chart**:
- Segments: High, Medium, Low (by count)
- Colors: Red, Yellow, Green

## 12. Pre-Populated Content

### 12.1 Metrics to Import

| Source | Metric | Target |
|--------|--------|--------|
| S1 | Authorization Compliance Rate | ≥95% |
| S1 | Policy Framework Score | ≥90% |
| S2 | VPN Compliance Score | 100% |
| S2 | MFA Coverage | 100% |
| S2 | MFA Enforcement Rate | ≥98% |
| S2 | Encryption Compliance | 100% |
| S3 | Encryption Status | 100% |
| S3 | Endpoint Protection Coverage | ≥98% |
| S3 | Patch Compliance Rate | ≥95% |
| S3 | Physical Security Compliance | ≥90% |
| S4 | Channel Accessibility | 100% |
| S4 | Response SLA Compliance | ≥90% |
| S4 | Awareness Coverage | ≥95% |

### 12.2 SoA Mapping

| Control | Name | Assessment Source |
|---------|------|-------------------|
| A.6.7 | Remote Working | S1, S2, S3 |
| A.6.8 | Information Security Event Reporting | S4 |

---

## END OF SPECIFICATION

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-01-31 -->
