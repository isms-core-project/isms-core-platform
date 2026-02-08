**ISMS-IMP-A.6.7-8.S5-UG - Remote Working and Event Reporting Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S5-UG |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.6.7-8.S5-TG.

---

**Audience:** CISO, IT Security Manager, Executive Management, Auditors

---

## Dashboard Overview

### Purpose

This compliance dashboard consolidates metrics from the four component assessments (S1-S4) to provide:
- Executive-level visibility into remote working and event reporting compliance
- Trend tracking across assessment periods
- Gap prioritization and remediation tracking
- Audit-ready compliance evidence
- Integration with Statement of Applicability (SoA) reporting

### Scope

This dashboard consolidates:
- **S1 Metrics**: Remote work authorization compliance
- **S2 Metrics**: Technical controls (VPN, MFA, encryption) compliance
- **S3 Metrics**: Endpoint and physical security compliance
- **S4 Metrics**: Event reporting mechanisms effectiveness

### Key Metrics

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

### Target Audience

- **Primary Users**: CISO, IT Security Manager
- **Executive Consumers**: Executive Management, Board
- **Auditors**: Internal and External Auditors
- **Operational Users**: IT Security Team

### Update Frequency

| Trigger | Frequency |
|---------|-----------|
| Scheduled Update | Quarterly |
| Post-Assessment Update | After any S1-S4 assessment |
| Management Review | Before management review meetings |
| Audit Preparation | Before Stage 1/Stage 2 audits |

## Prerequisites

Before updating this dashboard, ensure:

| Prerequisite | Status | Notes |
|--------------|--------|-------|
| S1 Assessment completed | ☐ | Remote Work Authorization |
| S2 Assessment completed | ☐ | Technical Controls |
| S3 Assessment completed | ☐ | Endpoint & Physical Security |
| S4 Assessment completed | ☐ | Event Reporting |
| S1-S4 workbooks accessible | ☐ | For data import |
| Previous dashboard version | ☐ | For trend comparison |

## Data Import Workflow

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

## Sheet-by-Sheet Completion Guide

### Instructions Sheet

**Purpose**: Provides guidance for dashboard users.

### Executive_Summary Sheet

**Purpose**: High-level compliance status for executive consumption.

**Content**:
- Overall compliance score (aggregate)
- Control-by-control compliance (A.6.7 and A.6.8 separately)
- Top 3 risks requiring attention
- Trend indicator (improving/stable/declining)
- Assessment period and dates

**Presentation**: Designed for presentation to executive management and board.

### Metrics_Import Sheet

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

### Control_Compliance Sheet

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

### Gap_Consolidation Sheet

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

### Trend_Analysis Sheet

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

### Risk_Assessment Sheet

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

### SoA_Integration Sheet

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

### Audit_Summary Sheet

**Purpose**: Audit-ready summary for Stage 1/Stage 2 audits.

**Content**:
- Control implementation status (A.6.7, A.6.8)
- Key evidence references
- Non-conformities and status
- Improvement opportunities
- Management commitment evidence

### Evidence_Index Sheet

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

### Dashboard Sheet

**Purpose**: Visual dashboard for at-a-glance status.

**Visualizations**:
- Gauge charts for each compliance metric
- Bar chart comparing current vs. target
- Pie chart of gap distribution by severity
- Trend sparklines for key metrics
- RAG status indicators

### Approval_Sign_Off Sheet

**Purpose**: Document formal review and approval.

**Sections**:
1. **Data Accuracy Certification**: IT Security confirms data is accurate
2. **Management Review**: CISO review and approval
3. **Distribution Authorization**: Approval for distribution
4. **Next Review Date**: Scheduled next update

## Metric Interpretation

### Compliance Thresholds

| Threshold | Status | Action |
|-----------|--------|--------|
| ≥95% | Green | Maintain, continuous improvement |
| 80-94% | Yellow | Improvement needed, track closely |
| <80% | Red | Immediate attention required |

### Trend Indicators

| Trend | Meaning | Action |
|-------|---------|--------|
| ↑ Improving | Metrics improving over periods | Continue current approach |
| → Stable | Metrics consistent | Look for improvement opportunities |
| ↓ Declining | Metrics worsening | Investigate root cause, escalate |

### Risk Prioritization

| Risk Score | Priority | Response Time |
|------------|----------|---------------|
| High (>15) | Critical | Immediate action |
| Medium (8-15) | High | Within 30 days |
| Low (<8) | Normal | Within 90 days |

## Reporting Use Cases

### Executive Reporting

**Frequency**: Quarterly
**Content**: Executive_Summary, Dashboard
**Audience**: Executive Management, Board
**Format**: PDF export or presentation

### Management Review

**Frequency**: Per ISMS management review cycle
**Content**: Control_Compliance, Gap_Consolidation, Trend_Analysis
**Audience**: CISO, IT Security Manager
**Format**: Full workbook with discussion

### Audit Support

**Frequency**: As needed for audits
**Content**: SoA_Integration, Audit_Summary, Evidence_Index
**Audience**: Internal/External Auditors
**Format**: Full workbook with evidence package

### Operational Tracking

**Frequency**: Monthly
**Content**: Gap_Consolidation, Metrics_Import
**Audience**: IT Security Team
**Format**: Workbook for operational tracking

## Quality Checklist

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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
