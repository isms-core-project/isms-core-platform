# ISMS-IMP-A.6.6.4 — NDA Compliance Dashboard

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.6.4 |
| **Title** | NDA Compliance Dashboard |
| **Control Reference** | ISO/IEC 27001:2022 A.6.6 |
| **Control Name** | Confidentiality or Non-Disclosure Agreements |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

## PART I: USER COMPLETION GUIDE

### Assessment Overview

**Purpose**

This dashboard provides executive-level visibility into NDA program compliance, coverage metrics, and key performance indicators.

**Scope**

- Executive summary of NDA program status
- Coverage metrics by stakeholder category
- Expiration status overview
- Compliance scorecard
- KPI tracking
- Trend analysis over time

### Prerequisites

- [ ] Completed ISMS-IMP-A.6.6.1 (Template Registry)
- [ ] Completed ISMS-IMP-A.6.6.2 (Execution Tracking)
- [ ] Completed ISMS-IMP-A.6.6.3 (Review & Compliance)
- [ ] Access to metrics from underlying assessments

### Workbook Structure

| Sheet | Purpose | Key Actions |
|-------|---------|-------------|
| Instructions | Guidance | Review before starting |
| Executive_Summary | High-level overview | Enter key metrics |
| Coverage_Metrics | Coverage by category | Update coverage data |
| Expiration_Status | Expiration overview | Track expirations |
| Compliance_Scorecard | Compliance metrics | Record scores |
| KPI_Tracker | Performance indicators | Update KPIs |
| Trend_Analysis | Historical trends | Record periodic data |
| Approval_SignOff | Authorisation | Obtain approvals |

### Completion Walkthrough

**Step 1: Executive_Summary Sheet**

Populate high-level KPI boxes:

- **Overall Coverage** - Percentage of required NDAs signed
- **Active NDAs** - Total count of active NDAs
- **Expiring (30 days)** - Count expiring within 30 days
- **Open Gaps** - Count of unresolved gaps

Key messages section for management attention items.

**Step 2: Coverage_Metrics Sheet**

Update coverage by category:

| Category | Target | Measurement |
|----------|--------|-------------|
| Employees | 100% | Signed / Required |
| Contractors | 100% | Signed / Required |
| Vendors | 100% | Signed / Required |
| Partners | 100% | Signed / Required |

Status: Green (100%), Amber (90-99%), Red (<90%)

**Step 3: Expiration_Status Sheet**

Track expiration buckets:

- Expired (overdue) - Red
- Expiring <30 days - Red
- Expiring 30-60 days - Amber
- Expiring 60-90 days - Amber
- Expiring 90-180 days - Green
- Beyond 180 days - Green

**Step 4: Compliance_Scorecard Sheet**

Record compliance scores:

| Area | Target | Measure |
|------|--------|---------|
| Employee NDA coverage | 100% | % with current NDA |
| Contractor NDA coverage | 100% | % with current NDA |
| Vendor NDA coverage | 100% | % with current NDA |
| NDAs within validity | 100% | % not expired |
| Appropriate template used | 100% | % correct template |
| Secure storage compliance | 100% | % properly stored |
| Periodic review completion | 100% | Reviews done on schedule |
| Gap remediation SLA | >95% | Closed within target |

**Step 5: KPI_Tracker Sheet**

Track key performance indicators:

| KPI | Target | Description |
|-----|--------|-------------|
| Overall coverage rate | 100% | All required NDAs signed |
| Renewal completion rate | >95% | Renewed before expiry |
| New joiner completion | 100% | NDA within 5 days of start |
| Template legal currency | 100% | Templates reviewed <12 months |
| Gap remediation SLA | >95% | Gaps closed within target |

**Step 6: Trend_Analysis Sheet**

Record quarterly data:

- Total NDAs
- New signed
- Renewed
- Expired
- Coverage percentage
- Open gaps
- Reviews completed
- Overall status

### Evidence Collection

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Dashboard Reports | Exported dashboard PDFs | ISMS Evidence Library |
| Management Presentations | Slides presented to management | ISMS Evidence Library |
| KPI Data Sources | Underlying calculation data | ISMS Evidence Library |

### Common Pitfalls

❌ **MISTAKE**: Dashboard with outdated data
✅ **CORRECT**: Update monthly minimum

❌ **MISTAKE**: KPIs without targets
✅ **CORRECT**: Every KPI has defined target

❌ **MISTAKE**: No trend tracking
✅ **CORRECT**: Maintain historical data

❌ **MISTAKE**: Complex dashboard obscuring key messages
✅ **CORRECT**: Clear executive summary with priorities

❌ **MISTAKE**: Dashboard not reviewed before presentation
✅ **CORRECT**: ISM verifies accuracy before management presentation

❌ **MISTAKE**: Missing sign-off on presented dashboards
✅ **CORRECT**: Approval before management presentation

❌ **MISTAKE**: No action tracking from dashboard insights
✅ **CORRECT**: Link findings to gap register

❌ **MISTAKE**: Coverage metrics against wrong population
✅ **CORRECT**: Verify denominator is current headcount/vendor list

### Quality Checklist

- [ ] All source assessments current
- [ ] KPI values calculated correctly
- [ ] Trend data maintained
- [ ] Executive summary reflects key messages
- [ ] Status thresholds applied consistently
- [ ] Approval signatures obtained

### Review & Approval

**Presentation Cadence**:

| Frequency | Audience | Content |
|-----------|----------|---------|
| Monthly | CISO | Metrics update |
| Quarterly | Executive Management | Full dashboard |
| Annually | Board/Audit Committee | Annual summary |

---

## PART II: TECHNICAL SPECIFICATION

### Workbook Architecture

**File Details**:

- Filename: `ISMS-IMP-A.6.6.4_NDA_Compliance_Dashboard_YYYYMMDD.xlsx`
- Format: Microsoft Excel (.xlsx)
- Sheets: 8

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Status | Green, Amber, Red |
| KPI_Status | On Track, At Risk, Behind |
| Trend | Improving, Stable, Declining, Up, Down |
| Priority | Critical, High, Medium, Low |
| Yes_No | Yes, No |

### Generator Reference

**Script**: `generate_a66_4_nda_dashboard.py`

**Location**: `10-isms-scr-base/isms-a.6.6-confidentiality-nda/10_generator-master/`

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-01 -->
