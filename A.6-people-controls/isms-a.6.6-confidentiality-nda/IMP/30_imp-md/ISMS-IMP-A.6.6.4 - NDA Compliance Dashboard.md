# ISMS-IMP-A.6.6.4 — NDA Compliance Dashboard

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.6.4 |
| **Document Title** | NDA Compliance Dashboard Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.6.6: Confidentiality or Non-Disclosure Agreements |
| **Parent Policy** | ISMS-POL-A.6.6 (Confidentiality and Non-Disclosure Agreements) |
| **Version** | 1.0 |
| **Classification** | Internal |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial implementation specification for ISO 27001:2022 first certification |

---

# PART I: USER COMPLETION GUIDE

This section provides step-by-step guidance for using and maintaining the NDA Compliance Dashboard. Follow this guide to ensure effective executive visibility into NDA program status and compliance metrics.

---

## 1. Assessment Overview

### 1.1 Purpose

The NDA Compliance Dashboard provides executive-level visibility into NDA program compliance, coverage metrics, and key performance indicators. It aggregates data from the NDA management workbooks to present a consolidated view of confidentiality agreement status across the organisation.

ISO/IEC 27001:2022 Control A.6.6 states:

> *"Confidentiality or non-disclosure agreements reflecting the organisation's needs for the protection of information should be identified, documented, regularly reviewed and signed by personnel and other relevant interested parties."*

This dashboard demonstrates that the organisation is actively managing and monitoring its NDA program, providing evidence of control effectiveness for management and auditors.

### 1.2 Scope and Applicability

**This dashboard consolidates:**

| Source Workbook | Data Aggregated |
|-----------------|-----------------|
| ISMS-IMP-A.6.6.1 | Template registry status, template counts |
| ISMS-IMP-A.6.6.2 | Execution tracking, expiration status, NDA counts |
| ISMS-IMP-A.6.6.3 | Review completion, coverage analysis, gap status |

**This dashboard provides:**

| Function | Description |
|----------|-------------|
| Executive Summary | High-level KPI boxes for quick status review |
| Coverage Metrics | Detailed coverage by stakeholder category |
| Expiration Status | NDA expiration tracking and alerts |
| Compliance Scorecard | Multi-dimensional compliance assessment |
| KPI Tracker | Performance indicator tracking over time |
| Trend Analysis | Historical trend data for pattern identification |

### 1.3 Business Context

**Why Dashboard Visibility Matters:**

Effective NDA management requires ongoing monitoring and executive attention:

1. **Risk Visibility**: Executives need visibility into confidentiality protection status
2. **Compliance Evidence**: Dashboard reports demonstrate control effectiveness
3. **Resource Allocation**: Coverage gaps require management attention for resources
4. **Trend Identification**: Early identification of declining metrics enables intervention
5. **Audit Readiness**: Dashboard provides immediate audit evidence
6. **Accountability**: Metrics drive accountability for NDA compliance

**Stakeholder Value:**

| Stakeholder | Dashboard Value |
|-------------|-----------------|
| CISO | Overall NDA program health, risk visibility |
| Executive Management | Compliance status, coverage metrics |
| HR Director | Employee NDA coverage, onboarding compliance |
| Procurement Director | Vendor NDA coverage, renewal status |
| Legal Counsel | Template currency, adequacy status |
| External Auditors | Compliance evidence, control effectiveness |

### 1.4 Dashboard Outputs

The dashboard produces the following outputs:

| Output | Purpose | Audience | Frequency |
|--------|---------|----------|-----------|
| Executive Summary | High-level status | CISO, Executives | Monthly |
| Coverage Report | Detailed coverage metrics | ISM, HR, Procurement | Monthly |
| Expiration Alert | Upcoming expirations | NDA Owners | Weekly |
| Compliance Scorecard | Multi-metric assessment | CISO | Monthly |
| KPI Report | Performance tracking | ISM, Management | Quarterly |
| Trend Report | Historical analysis | CISO, Audit Committee | Quarterly |
| Annual Summary | Year-in-review | Board, Audit Committee | Annually |

---

## 2. Prerequisites

### 2.1 Required Inputs

Before using the dashboard, ensure:

| Input | Source | Required For |
|-------|--------|--------------|
| Template Registry data | ISMS-IMP-A.6.6.1 | Template status metrics |
| Execution Tracking data | ISMS-IMP-A.6.6.2 | NDA counts, expirations |
| Review & Compliance data | ISMS-IMP-A.6.6.3 | Coverage, compliance scores |
| Current HR headcount | Human Resources | Employee metrics denominator |
| Current vendor count | Procurement | Vendor metrics denominator |
| Previous dashboard | ISMS Evidence Library | Trend comparison |

### 2.2 Required Approvals

| Activity | Approver | Purpose |
|----------|----------|---------|
| Dashboard data publication | ISM | Verify accuracy |
| Executive presentation | CISO | Approve before management |
| External distribution | CISO | Control sensitive metrics |
| Process changes | ISM | Maintain consistency |

### 2.3 Required Knowledge

Dashboard maintainers should understand:

- NDA program components and data sources
- KPI calculation methodologies
- RAG (Red/Amber/Green) status thresholds
- Trend analysis interpretation
- Executive reporting requirements
- Audit evidence requirements

### 2.4 Access Requirements

| Role | Access Level | Capabilities |
|------|--------------|--------------|
| Dashboard Administrator | Full | All sheets, configuration |
| Information Security Manager | Full | All sheets, data entry |
| CISO | Read + Approve | View all, approve for publication |
| Executive Management | Read | Summary and metrics only |
| HR/Procurement | Read | Relevant sections only |
| Auditors | Read | All sheets for audit |

---

## 3. Workbook Structure Overview

### 3.1 Sheet Summary

The workbook contains eight sheets for comprehensive dashboard management:

| Sheet | Purpose | Primary Owner | Update Frequency |
|-------|---------|---------------|------------------|
| 1: Instructions | Usage guidance | N/A | Reference only |
| 2: Executive_Summary | High-level KPIs | ISM | Monthly |
| 3: Coverage_Metrics | Coverage by category | ISM | Monthly |
| 4: Expiration_Status | Expiration tracking | ISM | Weekly |
| 5: Compliance_Scorecard | Compliance scoring | ISM | Monthly |
| 6: KPI_Tracker | KPI tracking | ISM | Quarterly |
| 7: Trend_Analysis | Historical trends | ISM | Quarterly |
| 8: Approval_SignOff | Publication approval | CISO | Per publication |

### 3.2 Sheet Dependencies

```
Source Workbooks (A.6.6.1, A.6.6.2, A.6.6.3)
         ↓ (data aggregation)
Sheet 3: Coverage_Metrics + Sheet 4: Expiration_Status + Sheet 5: Compliance_Scorecard
         ↓ (feeds)
Sheet 2: Executive_Summary
         ↓ (historical tracking)
Sheet 6: KPI_Tracker + Sheet 7: Trend_Analysis
         ↓ (approval)
Sheet 8: Approval_SignOff
```

### 3.3 Data Flow

1. **Data Collection**: Pull data from source workbooks
2. **Metrics Calculation**: Calculate coverage, compliance scores
3. **Status Determination**: Apply RAG thresholds
4. **Summary Generation**: Populate executive summary
5. **Trend Update**: Add to historical tracking
6. **Approval**: Obtain sign-off before publication
7. **Distribution**: Publish to stakeholders

---

## 4. Completion Walkthrough

### 4.1 Sheet 2: Executive_Summary – Completion Guide

**Purpose**: Provide leadership with at-a-glance visibility into NDA program status.

**Step-by-Step Completion:**

**Step 1: Update Key Metric Boxes**

The executive summary features four key metric boxes:

**Box 1: Overall Coverage**

| Field | Source | Calculation |
|-------|--------|-------------|
| Value | Coverage_Metrics | Total signed / Total required |
| Target | Fixed | 100% |
| Status | Calculated | Green ≥100%, Amber ≥95%, Red <95% |
| Trend | vs Previous | ↑↓→ compared to last month |

**Box 2: Active NDAs**

| Field | Source | Calculation |
|-------|--------|-------------|
| Value | Execution Tracking | COUNT where Status = Active |
| Change | vs Previous | +/- from last month |
| Breakdown | By category | Employees, Vendors, Other |

**Box 3: Expiring (30 Days)**

| Field | Source | Calculation |
|-------|--------|-------------|
| Value | Expiration_Status | COUNT expiring ≤30 days |
| Status | Threshold | Green 0, Amber 1-5, Red >5 |
| Action | If Red | Urgent renewal required |

**Box 4: Open Gaps**

| Field | Source | Calculation |
|-------|--------|-------------|
| Value | Gap Register | COUNT where Status = Open |
| Critical | Gap Register | COUNT Critical + Open |
| Status | Threshold | Green 0, Amber 1-3, Red >3 |

**Step 2: Populate Summary Table**

| Metric | Target | Actual | Status | Trend |
|--------|--------|--------|--------|-------|
| Employee Coverage | 100% | [%] | [RAG] | [↑↓→] |
| Contractor Coverage | 100% | [%] | [RAG] | [↑↓→] |
| Vendor Coverage | 100% | [%] | [RAG] | [↑↓→] |
| Template Currency | 100% | [%] | [RAG] | [↑↓→] |
| Review Completion | 100% | [%] | [RAG] | [↑↓→] |
| Gap Closure SLA | >95% | [%] | [RAG] | [↑↓→] |

**Step 3: Document Key Messages**

Record 3-5 key messages for management attention:

| Message Type | Example |
|--------------|---------|
| Achievement | "Employee coverage reached 100% this month" |
| Risk | "5 vendor NDAs expiring within 30 days" |
| Action Needed | "Contractor onboarding process review required" |
| Trend | "Gap closure rate improving for third consecutive month" |

**Step 4: Record Report Period**

| Field | Entry |
|-------|-------|
| Report Period | Month and Year (e.g., January 2026) |
| Data As Of | Date data was extracted |
| Prepared By | ISM name |
| Preparation Date | Date prepared |

### 4.2 Sheet 3: Coverage_Metrics – Completion Guide

**Purpose**: Provide detailed NDA coverage analysis by stakeholder category.

**Step-by-Step Completion:**

**Step 1: Update Category Data**

For each stakeholder category:

| Field | Source | Entry |
|-------|--------|-------|
| Category | Fixed | Employee, Contractor, Vendor, etc. |
| Total Population | HR/Procurement | Current count |
| NDA Required | Policy | How many require NDA |
| NDA Signed | Execution Tracking | Current signed count |
| Coverage Rate | Calculated | Signed / Required |

**Step 2: Calculate Gap Details**

| Field | Calculation |
|-------|-------------|
| Gap Count | Required - Signed |
| Expired Count | COUNT expired in category |
| Pending Renewal | COUNT expiring ≤90 days |

**Step 3: Apply Status**

| Coverage Rate | Status | Colour |
|---------------|--------|--------|
| 100% | On Target | Green |
| 95-99% | Near Target | Amber |
| 90-94% | Below Target | Orange |
| <90% | Critical | Red |

**Step 4: Document Actions**

For categories not at 100%:

| Field | Entry |
|-------|-------|
| Root Cause | Why coverage is below target |
| Action Required | Specific remediation action |
| Owner | Who is responsible |
| Target Date | When to achieve target |

**Category Detail Tables:**

**Employees:**

| Sub-Category | Total | Required | Signed | Rate | Status |
|--------------|-------|----------|--------|------|--------|
| Permanent FT | [n] | [n] | [n] | [%] | [RAG] |
| Permanent PT | [n] | [n] | [n] | [%] | [RAG] |
| Fixed Term | [n] | [n] | [n] | [%] | [RAG] |
| **Total Employees** | [n] | [n] | [n] | [%] | [RAG] |

**Contractors:**

| Sub-Category | Total | Required | Signed | Rate | Status |
|--------------|-------|----------|--------|------|--------|
| Individual | [n] | [n] | [n] | [%] | [RAG] |
| Agency | [n] | [n] | [n] | [%] | [RAG] |
| **Total Contractors** | [n] | [n] | [n] | [%] | [RAG] |

**Vendors:**

| Sub-Category | Total | Required | Signed | Rate | Status |
|--------------|-------|----------|--------|------|--------|
| IT Vendors | [n] | [n] | [n] | [%] | [RAG] |
| Service Providers | [n] | [n] | [n] | [%] | [RAG] |
| Consultants | [n] | [n] | [n] | [%] | [RAG] |
| **Total Vendors** | [n] | [n] | [n] | [%] | [RAG] |

### 4.3 Sheet 4: Expiration_Status – Completion Guide

**Purpose**: Track NDA expirations to enable proactive renewal management.

**Step-by-Step Completion:**

**Step 1: Categorise by Expiration Bucket**

Pull from ISMS-IMP-A.6.6.2 and categorise:

| Bucket | Definition | Status | Priority |
|--------|------------|--------|----------|
| Expired | Past expiry date | Red | Immediate |
| <30 Days | Expiring within 30 days | Red | Urgent |
| 30-60 Days | Expiring 30-60 days | Amber | High |
| 60-90 Days | Expiring 60-90 days | Amber | Medium |
| 90-180 Days | Expiring 90-180 days | Green | Plan |
| >180 Days | Expiring beyond 180 days | Green | Monitor |
| Perpetual | No expiry | Green | N/A |

**Step 2: Populate Summary**

| Expiration Bucket | Count | % of Total | Status |
|-------------------|-------|------------|--------|
| Expired | [n] | [%] | Red |
| <30 Days | [n] | [%] | Red |
| 30-60 Days | [n] | [%] | Amber |
| 60-90 Days | [n] | [%] | Amber |
| 90-180 Days | [n] | [%] | Green |
| >180 Days | [n] | [%] | Green |
| Perpetual | [n] | [%] | Green |
| **Total** | [n] | 100% | - |

**Step 3: List Critical Expirations**

For Expired and <30 Days categories, list details:

| NDA_ID | Counterparty | Category | Expiry Date | Days | Owner | Action Status |
|--------|--------------|----------|-------------|------|-------|---------------|
| [ID] | [Name] | [Cat] | [Date] | [-X] | [Name] | [Status] |

**Step 4: Track Renewal Progress**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Expired NDAs | [n] | 0 | [RAG] |
| Renewal rate (30 day) | [%] | 100% | [RAG] |
| Renewal rate (90 day) | [%] | >95% | [RAG] |
| Average renewal lead time | [days] | >45 | [RAG] |

### 4.4 Sheet 5: Compliance_Scorecard – Completion Guide

**Purpose**: Provide multi-dimensional compliance assessment of NDA program.

**Step-by-Step Completion:**

**Step 1: Define Scoring Areas**

| Area | Weight | Target | Description |
|------|--------|--------|-------------|
| Employee NDA Coverage | 15% | 100% | % employees with current NDA |
| Contractor NDA Coverage | 15% | 100% | % contractors with current NDA |
| Vendor NDA Coverage | 15% | 100% | % vendors with current NDA |
| NDAs Within Validity | 15% | 100% | % not expired |
| Appropriate Template | 10% | 100% | % using correct template |
| Secure Storage | 10% | 100% | % properly stored |
| Periodic Review | 10% | 100% | Reviews completed on schedule |
| Gap Remediation SLA | 10% | >95% | Gaps closed within target |

**Step 2: Calculate Individual Scores**

For each area:

| Field | Calculation |
|-------|-------------|
| Actual | Current metric value |
| Score | (Actual / Target) × 100, capped at 100 |
| Weighted Score | Score × Weight |
| Status | Green ≥100%, Amber ≥90%, Red <90% |

**Step 3: Calculate Overall Score**

```
Overall Score = Σ (Weighted Scores)
```

**Step 4: Apply Overall Status**

| Score Range | Status | Colour | Action |
|-------------|--------|--------|--------|
| ≥95% | Excellent | Green | Maintain |
| 90-94% | Good | Green | Monitor |
| 80-89% | Acceptable | Amber | Improve |
| 70-79% | Needs Improvement | Orange | Action Plan |
| <70% | Critical | Red | Urgent Remediation |

**Step 5: Document Score Breakdown**

| Compliance Area | Target | Actual | Score | Weight | Weighted | Status |
|-----------------|--------|--------|-------|--------|----------|--------|
| Employee Coverage | 100% | [%] | [/100] | 15% | [/15] | [RAG] |
| Contractor Coverage | 100% | [%] | [/100] | 15% | [/15] | [RAG] |
| Vendor Coverage | 100% | [%] | [/100] | 15% | [/15] | [RAG] |
| Within Validity | 100% | [%] | [/100] | 15% | [/15] | [RAG] |
| Template Correct | 100% | [%] | [/100] | 10% | [/10] | [RAG] |
| Secure Storage | 100% | [%] | [/100] | 10% | [/10] | [RAG] |
| Periodic Review | 100% | [%] | [/100] | 10% | [/10] | [RAG] |
| Gap SLA | >95% | [%] | [/100] | 10% | [/10] | [RAG] |
| **OVERALL** | - | - | - | 100% | **[/100]** | [RAG] |

### 4.5 Sheet 6: KPI_Tracker – Completion Guide

**Purpose**: Track key performance indicators over time for trend analysis.

**Step-by-Step Completion:**

**Step 1: Define KPIs**

| KPI ID | KPI Name | Target | Measurement | Frequency |
|--------|----------|--------|-------------|-----------|
| KPI-01 | Overall Coverage Rate | 100% | Signed / Required | Monthly |
| KPI-02 | Renewal Completion Rate | >95% | Renewed before expiry / Due | Monthly |
| KPI-03 | New Joiner Completion | 100% | NDA within 5 days | Monthly |
| KPI-04 | Template Legal Currency | 100% | Templates reviewed <12 months | Monthly |
| KPI-05 | Gap Remediation SLA | >95% | Closed within target / Total | Monthly |
| KPI-06 | Compliance Score | >90% | From scorecard | Monthly |
| KPI-07 | Zero Expired NDAs | Yes | Expired count = 0 | Weekly |
| KPI-08 | Review Completion | 100% | Reviews on schedule | Quarterly |

**Step 2: Record Monthly Values**

For each KPI, record:

| Field | Entry |
|-------|-------|
| Period | Month/Quarter |
| Value | Actual measurement |
| Target | Target value |
| Variance | Value - Target |
| Status | Green/Amber/Red |
| Commentary | Notable observations |

**Step 3: Track Status Over Time**

| KPI | Target | Jan | Feb | Mar | Apr | May | Jun | Trend |
|-----|--------|-----|-----|-----|-----|-----|-----|-------|
| KPI-01 | 100% | [%] | [%] | [%] | [%] | [%] | [%] | [↑↓→] |
| KPI-02 | >95% | [%] | [%] | [%] | [%] | [%] | [%] | [↑↓→] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Step 4: Calculate KPI Status**

| Status | Definition | Colour |
|--------|------------|--------|
| On Track | Meets or exceeds target | Green |
| At Risk | Within 5% of target | Amber |
| Behind | More than 5% below target | Red |

**Step 5: Determine Trend**

| Trend | Definition | Symbol |
|-------|------------|--------|
| Improving | Better than previous 3 periods average | ↑ |
| Stable | Within 2% of previous 3 periods average | → |
| Declining | Worse than previous 3 periods average | ↓ |

### 4.6 Sheet 7: Trend_Analysis – Completion Guide

**Purpose**: Maintain historical data for pattern identification and reporting.

**Step-by-Step Completion:**

**Step 1: Record Quarterly Metrics**

At quarter end, record:

| Metric | Q1 | Q2 | Q3 | Q4 | YoY Change |
|--------|----|----|----|----|------------|
| Total NDAs | [n] | [n] | [n] | [n] | [+/-%] |
| New Signed | [n] | [n] | [n] | [n] | [+/-%] |
| Renewed | [n] | [n] | [n] | [n] | [+/-%] |
| Expired | [n] | [n] | [n] | [n] | [+/-%] |
| Coverage % | [%] | [%] | [%] | [%] | [+/- pp] |
| Open Gaps | [n] | [n] | [n] | [n] | [+/-%] |
| Reviews Done | [n] | [n] | [n] | [n] | [%] |
| Compliance Score | [n] | [n] | [n] | [n] | [+/-] |

**Step 2: Generate Trend Charts**

Create visualisations for:
- Coverage trend over time
- NDA counts by category
- Gap trends
- Compliance score trend
- Expiration distribution

**Step 3: Identify Patterns**

Document significant patterns:

| Pattern Type | Observation | Implication | Recommended Action |
|--------------|-------------|-------------|-------------------|
| Seasonal | Higher expirations in Q4 | Renewal burden | Spread anniversary dates |
| Growth | Increasing vendor count | Coverage challenge | Automate vendor NDA |
| Improvement | Declining gaps | Process effectiveness | Maintain current approach |
| Concern | Rising expired count | Process failure | Root cause analysis |

**Step 4: Year-Over-Year Comparison**

| Metric | Prior Year | Current Year | Change | Status |
|--------|------------|--------------|--------|--------|
| Total NDAs | [n] | [n] | [+/-%] | [↑↓→] |
| Coverage Rate | [%] | [%] | [+/- pp] | [↑↓→] |
| Expired at Period End | [n] | [n] | [+/-%] | [↑↓→] |
| Compliance Score | [n] | [n] | [+/-] | [↑↓→] |

### 4.7 Sheet 8: Approval_SignOff – Completion Guide

**Purpose**: Obtain formal approval before publishing dashboard to stakeholders.

**Step-by-Step Completion:**

**Step 1: Document Dashboard Details**

| Field | Entry |
|-------|-------|
| Dashboard Period | Month/Quarter |
| Data As Of Date | Date data extracted |
| Prepared By | ISM name |
| Preparation Date | Date prepared |
| Distribution | Who will receive |

**Step 2: Pre-Publication Checklist**

- [ ] All source data current
- [ ] Calculations verified
- [ ] RAG status correctly applied
- [ ] Trend data updated
- [ ] Key messages appropriate
- [ ] No sensitive data inappropriately included
- [ ] Format suitable for audience

**Step 3: Obtain Approvals**

| Approver | Role | Scope | Date | Signature |
|----------|------|-------|------|-----------|
| [Name] | ISM | Data accuracy | [Date] | [Sig] |
| [Name] | CISO | Publication approval | [Date] | [Sig] |

**Step 4: Record Distribution**

| Date | Recipient | Format | Delivery Method |
|------|-----------|--------|-----------------|
| [Date] | Executive Management | PDF | Email |
| [Date] | HR Director | Excel | SharePoint |
| [Date] | Audit Committee | PDF | Board portal |

---

## 5. Evidence Collection

### 5.1 Evidence Requirements

Evidence must be maintained for all dashboard activities:

| Evidence Category | Retention Period | Storage Location |
|-------------------|------------------|------------------|
| Published dashboards | 7 years | ISMS Evidence Library |
| Approval records | 7 years | ISMS Evidence Library |
| Source data snapshots | 3 years | ISMS Evidence Library |
| Trend data | 7 years | ISMS Evidence Library |
| Presentation materials | 3 years | ISMS Evidence Library |

### 5.2 Evidence Folder Structure

```
ISMS-Evidence-Library/
└── NDA-Management/
    └── A.6.6-Confidentiality-NDAs/
        └── Dashboards/
            └── [YYYY]/
                ├── Monthly/
                │   └── [YYYY-MM]-Dashboard.pdf
                ├── Quarterly/
                │   └── [YYYY-QN]-Dashboard.pdf
                └── Approvals/
                    └── [YYYY-MM]-Approval.pdf
```

### 5.3 Evidence for Audit

During ISO 27001 audit, be prepared to demonstrate:

| Auditor Request | Evidence to Provide |
|-----------------|---------------------|
| "Show me NDA program status" | Current executive summary |
| "What is your NDA coverage?" | Coverage metrics with source data |
| "How do you track expirations?" | Expiration status sheet |
| "How do you measure compliance?" | Compliance scorecard methodology |
| "Show me trend over time" | Trend analysis with historical data |
| "Who approves dashboard publication?" | Approval records |

---

## 6. Common Pitfalls

### 6.1 Data Quality Errors

❌ **MISTAKE: Dashboard with outdated data**
Dashboard must be updated at defined frequency. Outdated data misleads stakeholders.

❌ **MISTAKE: Coverage metrics against wrong population**
Verify denominator is current headcount/vendor list. Wrong denominator produces incorrect coverage.

❌ **MISTAKE: Inconsistent calculation methodology**
Use same calculation method each period. Methodology changes break trend analysis.

❌ **MISTAKE: Not validating source data**
Verify source workbooks are current and accurate before aggregating.

### 6.2 Presentation Errors

❌ **MISTAKE: Complex dashboard obscuring key messages**
Keep executive summary clear and focused. Details in supporting sheets.

❌ **MISTAKE: No context for metrics**
Always include target and trend. Numbers without context are meaningless.

❌ **MISTAKE: Inconsistent RAG thresholds**
Apply same thresholds consistently. Document threshold definitions.

❌ **MISTAKE: Missing action items for Red status**
Red status without action plan shows lack of response. Always include remediation.

### 6.3 Process Errors

❌ **MISTAKE: Dashboard not reviewed before presentation**
ISM and CISO must verify accuracy before management presentation.

❌ **MISTAKE: Missing sign-off on published dashboards**
Approval must be documented before distribution.

❌ **MISTAKE: No action tracking from dashboard insights**
Findings must link to gap register or action tracking. Dashboard is not just reporting.

❌ **MISTAKE: Not maintaining historical data**
Trend analysis requires consistent historical data. Don't overwrite previous periods.

---

## 7. Quality Checklist

### 7.1 Pre-Publication Checklist

Before publishing dashboard:

- [ ] All source assessments current (within reporting period)
- [ ] KPI values calculated correctly
- [ ] Coverage denominators verified against current data
- [ ] Trend data updated with new period
- [ ] RAG status thresholds applied consistently
- [ ] Executive summary reflects key messages
- [ ] All Red items have documented actions
- [ ] Approval signatures obtained

### 7.2 Monthly Update Checklist

Monthly dashboard activities:

- [ ] Source workbook data refreshed
- [ ] Coverage metrics recalculated
- [ ] Expiration status updated
- [ ] Compliance scorecard recalculated
- [ ] KPI tracker updated
- [ ] Executive summary key messages reviewed
- [ ] Trend data point added
- [ ] Previous month archived

### 7.3 Quarterly Checklist

Additional quarterly activities:

- [ ] Trend analysis narrative updated
- [ ] Year-over-year comparison updated
- [ ] KPI performance review conducted
- [ ] Process improvement opportunities identified
- [ ] Quarterly report to management prepared
- [ ] Historical data verified

---

## 8. Review and Approval

### 8.1 Publication Authority

| Dashboard Type | Preparer | Approver | Distribution |
|----------------|----------|----------|--------------|
| Monthly Operations | ISM | ISM | IT Security Team |
| Monthly Executive | ISM | CISO | Executive Management |
| Quarterly Summary | ISM | CISO | Management + Board |
| Annual Report | ISM | CISO + Executive | Board, Audit Committee |

### 8.2 Presentation Cadence

| Frequency | Audience | Content | Format |
|-----------|----------|---------|--------|
| Weekly | IT Security | Expiration alerts | Email/Dashboard |
| Monthly | CISO | Full dashboard | Meeting + PDF |
| Quarterly | Executive Management | Executive summary + trends | Presentation |
| Annually | Board/Audit Committee | Annual summary | Formal report |

### 8.3 Escalation Triggers

| Trigger | Escalation Path | Timing |
|---------|-----------------|--------|
| Coverage < 90% any category | ISM → CISO → Executive | Immediate |
| Expired NDAs > 0 | ISM → Category Owner | Within 24 hours |
| Compliance Score < 80% | ISM → CISO | Within 48 hours |
| Critical gaps > 0 | ISM → CISO → Executive | Immediate |

---

# PART II: TECHNICAL SPECIFICATION

This section provides technical details for the NDA Compliance Dashboard workbook implementation.

---

## 9. Workbook Technical Structure

### 9.1 Workbook Properties

| Property | Value |
|----------|-------|
| File Format | .xlsx (Excel 2016+) |
| Sheet Protection | Structure protected, cells unlocked for input |
| Workbook Protection | Structure only |
| File Naming | ISMS-IMP-A.6.6.4_NDA_Compliance_Dashboard_YYYYMMDD.xlsx |

### 9.2 Sheet Configuration

| Sheet | Tab Colour | Protection Level | Hidden |
|-------|------------|------------------|--------|
| Instructions | Grey (#A6A6A6) | Full protection | No |
| Executive_Summary | Dark Blue (#002060) | Full (display only) | No |
| Coverage_Metrics | Green (#70AD47) | Input cells unlocked | No |
| Expiration_Status | Orange (#ED7D31) | Input cells unlocked | No |
| Compliance_Scorecard | Purple (#7030A0) | Input cells unlocked | No |
| KPI_Tracker | Blue (#4472C4) | Input cells unlocked | No |
| Trend_Analysis | Teal (#00B0F0) | Input cells unlocked | No |
| Approval_SignOff | Gold (#FFC000) | Input cells unlocked | No |
| Validation Lists | Grey (#A6A6A6) | Full protection | Yes |

---

## 10. Sheet Specifications

### 10.1 Sheet 2: Executive_Summary – Technical Specification

**Layout Configuration:**

| Section | Position | Content |
|---------|----------|---------|
| Header | Row 1-3 | Title, Report Period |
| KPI Boxes | Row 5-8 | 4 key metric boxes |
| Summary Table | Row 10-18 | Metric summary |
| Key Messages | Row 20-25 | Management messages |
| Footer | Row 27-28 | Prepared by, Date |

**KPI Box Structure:**

```
┌─────────────────┐
│ [METRIC NAME]   │
│ [VALUE] [TREND] │
│ Target: [TARGET]│
│ Status: [RAG]   │
└─────────────────┘
```

**Data Links:**

| Metric | Source Formula |
|--------|----------------|
| Overall Coverage | =Coverage_Metrics!$E$12 |
| Active NDAs | =COUNTIF(Source!Status,"Active") |
| Expiring 30 Days | =Expiration_Status!$B$3 |
| Open Gaps | =COUNTIF(Gap_Register!Status,"Open") |

### 10.2 Sheet 3: Coverage_Metrics – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Category | 25 | Text | Fixed | Yes |
| B | Sub_Category | 20 | Text | Fixed | Yes |
| C | Total_Population | 10 | Number | Integer >= 0 | Yes |
| D | NDA_Required | 10 | Number | Integer >= 0 | Yes |
| E | NDA_Signed | 10 | Number | Integer >= 0 | Yes |
| F | Coverage_Rate | 10 | Percentage | Calculated | Auto |
| G | Gap_Count | 10 | Number | Calculated | Auto |
| H | Expired_Count | 10 | Number | Integer >= 0 | Yes |
| I | Status | 12 | List | Green,Amber,Red | Auto |
| J | Action_Required | 40 | Text | If not Green | Conditional |
| K | Owner | 20 | Text | If action needed | Conditional |
| L | Target_Date | 15 | Date | DD.MM.YYYY | Conditional |

**Formulas:**

```excel
Coverage_Rate (F2):
=IF(D2=0,0,E2/D2)

Gap_Count (G2):
=MAX(0,D2-E2)

Status (I2):
=IF(F2>=1,"Green",IF(F2>=0.95,"Amber","Red"))
```

**Conditional Formatting:**

| Condition | Format |
|-----------|--------|
| Status = "Red" | Red fill |
| Status = "Amber" | Yellow fill |
| Status = "Green" | Green fill |

### 10.3 Sheet 4: Expiration_Status – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Expiration_Bucket | 20 | Text | Fixed buckets | Yes |
| B | Count | 10 | Number | Integer >= 0 | Yes |
| C | Percentage | 10 | Percentage | Calculated | Auto |
| D | Status | 12 | List | Green,Amber,Red | Auto |
| E | Priority | 12 | List | Immediate,Urgent,High,Medium,Low | Auto |

**Bucket Definitions (Row 2-8):**

```
Row 2: Expired (Red, Immediate)
Row 3: <30 Days (Red, Urgent)
Row 4: 30-60 Days (Amber, High)
Row 5: 60-90 Days (Amber, Medium)
Row 6: 90-180 Days (Green, Low)
Row 7: >180 Days (Green, Monitor)
Row 8: Perpetual (Green, N/A)
```

**Critical Expirations List (Row 12+):**

| Column | Header | Width | Data Type | Required |
|--------|--------|-------|-----------|----------|
| A | NDA_ID | 15 | Text | Yes |
| B | Counterparty | 30 | Text | Yes |
| C | Category | 20 | Text | Yes |
| D | Expiry_Date | 15 | Date | Yes |
| E | Days_Remaining | 10 | Number | Calculated |
| F | Owner | 20 | Text | Yes |
| G | Renewal_Status | 15 | List | Yes |

### 10.4 Sheet 5: Compliance_Scorecard – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | Compliance_Area | 30 | Text | Fixed | Yes |
| B | Target | 10 | Percentage | Fixed | Yes |
| C | Actual | 10 | Percentage | Calculated | Yes |
| D | Score | 10 | Number | 0-100 | Calculated |
| E | Weight | 10 | Percentage | Fixed | Yes |
| F | Weighted_Score | 10 | Number | Calculated | Auto |
| G | Status | 12 | List | Green,Amber,Red | Auto |
| H | Trend | 10 | List | ↑,→,↓ | Yes |
| I | Notes | 40 | Text | Optional | No |

**Formulas:**

```excel
Score (D2):
=MIN(100,C2/B2*100)

Weighted_Score (F2):
=D2*E2

Overall_Score (F12):
=SUM(F2:F9)

Status (G2):
=IF(D2>=100,"Green",IF(D2>=90,"Amber","Red"))
```

### 10.5 Sheet 6: KPI_Tracker – Technical Specification

**Column Definitions:**

| Column | Header | Width | Data Type | Validation | Required |
|--------|--------|-------|-----------|------------|----------|
| A | KPI_ID | 10 | Text | Format: KPI-## | Yes |
| B | KPI_Name | 30 | Text | Name | Yes |
| C | Target | 12 | Text | Target value | Yes |
| D | Jan | 10 | Varies | By KPI | Yes |
| E | Feb | 10 | Varies | By KPI | Yes |
| F | Mar | 10 | Varies | By KPI | Yes |
| ... | ... | ... | ... | ... | ... |
| O | Dec | 10 | Varies | By KPI | Yes |
| P | YTD_Avg | 10 | Calculated | Average | Auto |
| Q | Trend | 10 | List | ↑,→,↓ | Calculated |
| R | Status | 12 | List | On Track,At Risk,Behind | Calculated |

### 10.6 Sheet 7: Trend_Analysis – Technical Specification

**Quarterly Data Table:**

| Column | Header | Width | Data Type | Required |
|--------|--------|-------|-----------|----------|
| A | Metric | 25 | Text | Yes |
| B | Q1 | 10 | Varies | Yes |
| C | Q2 | 10 | Varies | Yes |
| D | Q3 | 10 | Varies | Yes |
| E | Q4 | 10 | Varies | Yes |
| F | YoY_Change | 15 | Calculated | Auto |
| G | Trend | 10 | List | Auto |

**Year-Over-Year Table:**

| Column | Header | Width | Data Type | Required |
|--------|--------|-------|-----------|----------|
| A | Metric | 25 | Text | Yes |
| B | Prior_Year | 15 | Varies | Yes |
| C | Current_Year | 15 | Varies | Yes |
| D | Change | 15 | Calculated | Auto |
| E | Status | 12 | List | Auto |

---

## 11. Automation Requirements

### 11.1 Automated Alerts

| Trigger | Alert Type | Recipients | Timing |
|---------|------------|------------|--------|
| Coverage < 95% | Email | ISM, Category Owner | Daily |
| Expired NDA count > 0 | Email | ISM, CISO | Daily |
| Compliance Score < 80% | Email | ISM, CISO | Weekly |
| Dashboard update overdue | Email | ISM | 3 days after due |

### 11.2 Data Refresh Automation

| Data Element | Refresh Method | Frequency |
|--------------|----------------|-----------|
| Source workbook links | Manual refresh | Weekly |
| Coverage calculations | Auto-calculate | Real-time |
| Expiration counts | Manual update | Weekly |
| Compliance scores | Auto-calculate | Real-time |
| Trend data | Manual entry | Quarterly |

### 11.3 Report Generation

| Report | Format | Generation | Distribution |
|--------|--------|------------|--------------|
| Monthly Dashboard | PDF | Manual export | Email |
| Executive Summary | PowerPoint | Manual | Presentation |
| Quarterly Report | PDF | Manual | Management meeting |

---

## 12. Metrics and KPIs

### 12.1 Coverage KPIs

| KPI | Target | Threshold | Owner |
|-----|--------|-----------|-------|
| Overall Coverage | 100% | <95% critical | ISM |
| Employee Coverage | 100% | <98% warning | HR |
| Vendor Coverage | 100% | <90% critical | Procurement |
| New Joiner Completion | 100% | <95% warning | HR |

### 12.2 Compliance KPIs

| KPI | Target | Threshold | Owner |
|-----|--------|-----------|-------|
| Compliance Score | >90% | <80% critical | ISM |
| Expired NDA Count | 0 | >0 critical | ISM |
| Template Currency | 100% | <90% warning | Legal |
| Secure Storage | 100% | <95% warning | ISM |

### 12.3 Process KPIs

| KPI | Target | Threshold | Owner |
|-----|--------|-----------|-------|
| Renewal Rate | >95% | <90% warning | ISM |
| Gap Closure SLA | >95% | <90% warning | ISM |
| Review Completion | 100% | <90% warning | ISM |
| Dashboard Timeliness | 100% | Late = warning | ISM |

---

## 13. Evidence Package for ISO 27001 Audit

### 13.1 Standard Evidence Package

| Document | Purpose | Preparation |
|----------|---------|-------------|
| 12-month dashboard archive | Program monitoring evidence | Monthly PDF exports |
| Coverage trend analysis | Coverage management evidence | Sheet 7 export |
| Compliance score history | Compliance tracking | Sheet 5 history |
| KPI reports | Performance management | Sheet 6 export |
| Approval records | Governance evidence | Sheet 8 export |
| Executive presentations | Management engagement | Presentation archive |

### 13.2 Audit Preparation Checklist

- [ ] Archive current dashboard state
- [ ] Export 12-month trend data
- [ ] Compile KPI history
- [ ] Gather approval records
- [ ] Prepare coverage analysis summary
- [ ] Document methodology

---

## 14. Generator Script Reference

### 14.1 Script Location

```
10-isms-scr-base/
└── isms-a.6.6-confidentiality-nda/
    └── 10_generator-master/
        └── generate_a66_4_nda_dashboard.py
```

### 14.2 Script Execution

```bash
cd 10-isms-scr-base/isms-a.6.6-confidentiality-nda/10_generator-master
python3 generate_a66_4_nda_dashboard.py
mv *.xlsx ../90_workbooks/
```

### 14.3 Output

```
ISMS-IMP-A.6.6.4_NDA_Compliance_Dashboard_YYYYMMDD.xlsx
```

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-03 -->
