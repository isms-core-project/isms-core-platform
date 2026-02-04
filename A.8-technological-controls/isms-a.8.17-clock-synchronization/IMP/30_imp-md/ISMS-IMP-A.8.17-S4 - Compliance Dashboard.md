**ISMS-IMP-A.8.17-S4 — Compliance Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S4 |
| **Version** | 1.0 |
| **Assessment Area** | Clock Synchronization Compliance Dashboard |
| **Related Policy** | ISMS-POL-A.8.17 (Clock Synchronization Policy) |
| **Purpose** | Provide executive dashboard aggregating S1-S3 findings, showing overall clock synchronization compliance status and metrics |
| **Target Audience** | CISO, Executive Management, ISMS Officers, Auditors, Risk Managers |
| **Assessment Type** | Executive Reporting & Compliance Tracking |
| **Review Cycle** | Monthly or As Required |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original Date] | Initial technical specification for compliance dashboard | ISMS Officer |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE** (Sections 1-8)
  - How to complete the Compliance Dashboard workbook
  - Prerequisites, workflow, field-by-field guidance
  - Evidence collection, quality checks, and approval process

- **PART II: TECHNICAL SPECIFICATION** (Sections 9-onwards)
  - Section A: Implementation Guidance (metric calculations, aggregation logic)
  - Section B: Assessment Workbook Specification (Excel workbook structure, formulas, validation rules)

---

# PART I: USER COMPLETION GUIDE

**Audience:** ISMS Officers, Security Managers, Compliance Officers preparing executive dashboards

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.17-S4 - Compliance Dashboard

**What This Assessment Covers:**

This dashboard aggregates findings from S1 (Time Source Configuration), S2 (Synchronization Verification), and S3 (Exception Management) into an executive-level view of clock synchronization compliance. Think of this as the "single pane of glass" for A.8.17 compliance. This assessment answers critical questions:

- **What is our overall compliance score?** (Percentage of systems meeting requirements)
- **Is our NTP infrastructure healthy?** (Time sources and servers operational)
- **How many systems are synchronized?** (From S2 verification results)
- **How many exceptions do we have?** (From S3 exception register)
- **What gaps need attention?** (Aggregated remediation tracking)

**Key Principle:** "Executive visibility enables accountability." Leadership needs clear, actionable metrics to understand clock synchronization posture without diving into technical details. This dashboard provides that visibility.

Think of this as the "executive scorecard" for time synchronization - similar to how a financial dashboard shows revenue and expenses at a glance, this shows synchronization compliance and risks at a glance.

## What You'll Document

**Workbook Sheets You'll Complete:**

1. **Instructions** - Dashboard guidance and navigation

   - Purpose and scope
   - Data sources (S1, S2, S3)
   - Metric definitions
   - Update procedures

2. **Executive_Summary** - Overall compliance score and status

   - Compliance percentage (big number)
   - Trend over time (improving/declining)
   - Key highlights and concerns
   - Risk rating (Green/Yellow/Red)

3. **Infrastructure_Health** - NTP infrastructure health metrics

   - External time source status (from S1)
   - Internal NTP server status (from S1)
   - Source redundancy compliance
   - Monitoring coverage

4. **System_Compliance** - System-level sync compliance

   - Total systems in scope
   - Systems compliant (from S2)
   - Systems non-compliant (from S2)
   - Systems with exceptions (from S3)
   - Compliance by category/department

5. **Gaps_Action_Items** - Remediation tracking

   - Open gaps from S1, S2, S3
   - Priority and severity
   - Responsible parties
   - Target dates and status

## How This Relates to Other A.8.17 Assessments

| Assessment | Focus | Input to S4 Dashboard |
|------------|-------|----------------------|
| ISMS-IMP-A.8.17-S1 | Time Source Infrastructure | Infrastructure health metrics, source/server counts |
| ISMS-IMP-A.8.17-S2 | System Synchronization Verification | System compliance counts, non-compliant system list |
| ISMS-IMP-A.8.17-S3 | Exception Management | Exception counts, exception categories |
| **ISMS-IMP-A.8.17-S4** | **Compliance Dashboard** | **THIS assessment - aggregates S1-S3 into executive view** |

**Assessment Flow:**
1. **A.8.17-S1:** "We have 2 external sources and 4 internal NTP servers"
2. **A.8.17-S2:** "1,200 of 1,234 systems are synchronized correctly"
3. **A.8.17-S3:** "34 non-compliant systems have 3 approved exceptions + 31 pending remediation"
4. **A.8.17-S4 (THIS):** "Overall compliance: 97.5% (1,200 compliant + 3 exceptions = 1,203 of 1,234)"

You MUST complete S1, S2, and S3 first - this dashboard consolidates their findings.

## Who Should Complete This Assessment

**Primary Stakeholders:**

1. **ISMS Officer** - Primary owner of compliance dashboard
2. **Security Analyst** - Aggregates data from S1, S2, S3 assessments
3. **Compliance Officer** - Reviews metrics against policy requirements
4. **CISO** - Consumer of dashboard for executive reporting
5. **Audit Team** - Uses dashboard for compliance evidence

**Required Skills:**

- **Data Aggregation** - Can combine findings from multiple assessments
- **Metric Calculation** - Understands compliance percentage calculations
- **Executive Communication** - Can present technical data in business terms
- **Trend Analysis** - Can identify patterns over time

**You DON'T need deep technical knowledge!** The S1, S2, S3 assessments capture technical details. This dashboard translates those details into executive metrics.

## Time Commitment

- **Initial setup (first time):** 2-4 hours
  - 1 hour: Gather data from S1, S2, S3 assessments
  - 1 hour: Populate dashboard sheets
  - 30 minutes: Calculate compliance metrics
  - 30 minutes: Prepare executive summary narrative
  - 30 minutes: Review and validate calculations

- **Monthly updates:** 1-2 hours
  - 30 minutes: Refresh data from S1, S2, S3
  - 30 minutes: Update compliance metrics
  - 30 minutes: Update trend analysis
  - 30 minutes: Prepare executive summary highlights

**Pro Tip:** Link dashboard cells directly to S1, S2, S3 workbooks where possible. This enables automatic updates when source assessments are refreshed.

## Expected Outputs

Upon completion, you will have:

1. **Overall compliance score** - Single percentage for executive reporting
2. **Infrastructure health status** - Green/Yellow/Red for NTP infrastructure
3. **System compliance breakdown** - Compliant, non-compliant, exception counts
4. **Trend visualization** - Compliance over time (improving/declining)
5. **Risk rating** - Executive-friendly risk assessment
6. **Gap summary** - Aggregated view of open remediation items
7. **Action items** - Priority items requiring executive attention
8. **Audit-ready report** - Dashboard suitable for auditor review

**What This Looks Like for Audit:**

When an auditor asks: *"What is your overall clock synchronization compliance posture?"*

You hand them this dashboard and say:

> "Our overall compliance is 97.5%. We have 1,234 systems in scope: 1,200 are fully compliant, 3 have approved exceptions with compensating controls, and 31 are pending remediation with target completion in Q2. Our NTP infrastructure is healthy with redundant time sources and 100% monitoring coverage."

**Auditor reaction:** "This demonstrates mature compliance tracking with clear visibility into remediation progress. Excellent."

---

# Prerequisites

## Required Information

Before starting, gather the following:

**From S1 (Time Source Configuration):**

- [ ] **External time source count** (minimum 2 required)
- [ ] **Primary source count** (Stratum 0/1 sources)
- [ ] **Internal NTP server count** (minimum 2 required)
- [ ] **Monitoring coverage percentage** (target: 100%)
- [ ] **S1 gaps and remediation status**

**From S2 (Synchronization Verification):**

- [ ] **Total systems in scope**
- [ ] **Systems verified compliant**
- [ ] **Systems non-compliant** (requiring remediation or exception)
- [ ] **S2 gaps and remediation status**

**From S3 (Exception Management):**

- [ ] **Active exception count**
- [ ] **Pending exception requests**
- [ ] **Exception categories breakdown**
- [ ] **Upcoming expirations**

**Historical Data:**

- [ ] **Previous compliance scores** (for trend analysis)
- [ ] **Previous dashboard dates** (for period comparison)

## Required Tools

**For Data Collection:**

- Access to S1, S2, S3 assessment workbooks
- Or: Database/CMDB with compliance data

**For Dashboard Creation:**

- Microsoft Excel (or compatible spreadsheet)
- This workbook template

**For Visualization:**

- Optional: Power BI, Tableau, or similar for advanced visualization
- Built-in Excel charts sufficient for basic dashboard

## Policy Requirements to Review

Before starting, familiarize yourself with key policy requirements from **ISMS-POL-A.8.17**:

**Infrastructure Requirements:**

- REQ-817-001: Minimum 2 external authoritative time sources
- REQ-817-005: Minimum 2 internal NTP servers
- REQ-817-008: 100% monitoring with alerting for NTP infrastructure

**System Compliance Requirements:**

- REQ-817-009: All systems must synchronize to approved time sources
- REQ-817-010: Maximum acceptable drift (varies by system class)

**Exception Requirements:**

- REQ-817-017: Formal exception process for non-compliant systems
- REQ-817-019: Compensating controls required for all exceptions

The dashboard should show compliance against these requirements.

---

# Assessment Workflow

## Recommended Completion Order

**STEP 1:** Gather source data

- Export key metrics from S1 workbook
- Export compliance counts from S2 workbook
- Export exception counts from S3 workbook

**STEP 2:** Populate Infrastructure_Health sheet

- Enter external source status from S1
- Enter internal server status from S1
- Calculate redundancy compliance
- Calculate monitoring coverage

**STEP 3:** Populate System_Compliance sheet

- Enter total systems in scope
- Enter compliant system count
- Enter non-compliant system count
- Enter exception count
- Calculate overall compliance percentage

**STEP 4:** Populate Gaps_Action_Items sheet

- List open gaps from S1, S2, S3
- Assign priority and severity
- Document responsible parties and target dates
- Track remediation status

**STEP 5:** Complete Executive_Summary sheet

- Calculate overall compliance score
- Determine risk rating (Green/Yellow/Red)
- Write executive narrative
- Highlight key concerns and achievements

**STEP 6:** Update trend analysis

- Record current period metrics
- Compare to previous periods
- Identify improvement or decline

**STEP 7:** Review and validate

- Verify calculations are correct
- Cross-check totals against source workbooks
- Ensure narrative matches data

**STEP 8:** Obtain approval

- ISMS Officer review
- CISO sign-off for executive distribution

## Data Sources

**Where to find information for this dashboard:**

**S1 Assessment:**

- Time_Sources sheet: Count of external sources
- Internal_NTP_Servers sheet: Count of internal servers, monitoring status
- Compliance_Summary sheet: Infrastructure compliance metrics

**S2 Assessment:**

- System_Inventory sheet: Total systems in scope
- Verification_Results sheet: Compliant/non-compliant counts
- Compliance_Summary sheet: System compliance metrics

**S3 Assessment:**

- Active_Exceptions sheet: Count of active exceptions
- Summary_Dashboard sheet: Exception metrics
- Gaps table: Open remediation items

---

# Sheet-by-Sheet Completion Guidance

## Sheet: Instructions

**Purpose:** Provide dashboard usage instructions and metric definitions.

**THIS SHEET IS PRE-POPULATED** - No user input required.

**Content Includes:**

- Dashboard purpose and scope
- Data source descriptions (S1, S2, S3)
- Metric definitions and calculations
- Update frequency guidance
- Contact information for questions

---

## Sheet: Executive_Summary (Overall Compliance Score and Status)

**Purpose:** Provide single-page executive view of clock synchronization compliance.

**Layout:**

**Section 1: Overall Compliance Score**

| Element | Description | Guidance |
|---------|-------------|----------|
| **Compliance Score** | Large percentage display | = (Compliant Systems + Exception Systems) / Total Systems |
| **Score Trend** | Arrow indicator | Up (improving), Down (declining), Flat (stable) |
| **Risk Rating** | Green/Yellow/Red status | Based on compliance thresholds |

**Risk Rating Thresholds:**

| Compliance Percentage | Risk Rating | Color |
|-----------------------|-------------|-------|
| ≥95% | Low Risk | Green |
| 80-94% | Medium Risk | Yellow |
| <80% | High Risk | Red |

**Section 2: Key Metrics Summary**

| Metric | Value | Source |
|--------|-------|--------|
| **Total Systems in Scope** | [Number] | S2 System_Inventory |
| **Compliant Systems** | [Number] | S2 Verification_Results |
| **Non-Compliant Systems** | [Number] | S2 Verification_Results |
| **Systems with Exceptions** | [Number] | S3 Active_Exceptions |
| **Pending Remediation** | [Number] | = Non-Compliant - Exceptions |
| **Infrastructure Status** | Green/Yellow/Red | Infrastructure_Health sheet |

**Section 3: Executive Narrative**

Free-form text area for executive summary. Include:

- Current compliance status summary
- Key achievements since last report
- Top concerns requiring attention
- Recommended actions for leadership

**Example Narrative:**

> **Clock Synchronization Compliance Summary - January 2026**
>
> Overall compliance is 97.5%, up from 95.2% last quarter. Key achievements include remediation of 15 legacy systems and deployment of GPS receivers for air-gapped OT environments.
>
> **Key Concerns:**
> - 31 systems pending remediation (target: Q2 2026)
> - 2 exception renewals due in February
>
> **Recommended Actions:**
> - Approve budget for remaining legacy system upgrades
> - Schedule exception renewal reviews

**Section 4: Compliance Trend**

Chart showing compliance percentage over time (6-12 months).

| Period | Compliance % | Notes |
|--------|--------------|-------|
| Jan 2026 | 97.5% | Current |
| Oct 2025 | 95.2% | Q3 assessment |
| Jul 2025 | 92.1% | Q2 assessment |
| Apr 2025 | 88.5% | Q1 assessment |
| Jan 2025 | 85.0% | Initial baseline |

---

## Sheet: Infrastructure_Health (NTP Infrastructure Health Metrics)

**Purpose:** Show health status of time source infrastructure from S1 assessment.

**Section 1: External Time Sources**

| Metric | Requirement | Actual | Status |
|--------|-------------|--------|--------|
| **External Source Count** | ≥2 | [From S1] | Pass/Fail |
| **Primary Sources (Stratum 0/1)** | ≥2 | [From S1] | Pass/Fail |
| **Sources Active** | 100% | [From S1] | Pass/Fail |

**Section 2: Internal NTP Servers**

| Metric | Requirement | Actual | Status |
|--------|-------------|--------|--------|
| **Internal Server Count** | ≥2 | [From S1] | Pass/Fail |
| **Servers at Stratum 2** | 100% | [From S1] | Pass/Fail |
| **Servers Active** | 100% | [From S1] | Pass/Fail |

**Section 3: Monitoring Coverage**

| Metric | Requirement | Actual | Status |
|--------|-------------|--------|--------|
| **Monitoring with Alerting** | 100% | [From S1] | Pass/Fail |
| **Last Health Check < 30 days** | 100% | [From S1] | Pass/Fail |

**Section 4: Infrastructure Summary**

| Component | Status | Details |
|-----------|--------|---------|
| External Time Sources | Green/Yellow/Red | [Summary] |
| Internal NTP Servers | Green/Yellow/Red | [Summary] |
| Monitoring | Green/Yellow/Red | [Summary] |
| **Overall Infrastructure** | Green/Yellow/Red | [Aggregate] |

**Infrastructure Status Criteria:**

| Status | Criteria |
|--------|----------|
| Green | All requirements met |
| Yellow | Minor gaps, non-critical |
| Red | Critical requirements not met |

---

## Sheet: System_Compliance (System-Level Sync Compliance)

**Purpose:** Show system-level synchronization compliance from S2 assessment.

**Section 1: Overall System Compliance**

| Metric | Count | Percentage |
|--------|-------|------------|
| **Total Systems in Scope** | [From S2] | 100% |
| **Compliant Systems** | [From S2] | [%] |
| **Non-Compliant Systems** | [From S2] | [%] |
| **With Approved Exceptions** | [From S3] | [%] |
| **Pending Remediation** | [Calculated] | [%] |

**Compliance Calculation:**

```
Effective Compliance % = (Compliant + Exceptions) / Total * 100

Where:
- Compliant = Systems verified synchronized in S2
- Exceptions = Active approved exceptions in S3
- Total = Total systems in scope
```

**Section 2: Compliance by System Category**

| Category | Total | Compliant | Non-Compliant | Exceptions | Compliance % |
|----------|-------|-----------|---------------|------------|--------------|
| Servers | [N] | [N] | [N] | [N] | [%] |
| Workstations | [N] | [N] | [N] | [N] | [%] |
| Network Devices | [N] | [N] | [N] | [N] | [%] |
| OT/ICS Systems | [N] | [N] | [N] | [N] | [%] |
| Cloud Resources | [N] | [N] | [N] | [N] | [%] |
| Other | [N] | [N] | [N] | [N] | [%] |

**Section 3: Compliance by Business Unit/Department**

| Department | Total | Compliant | Non-Compliant | Exceptions | Compliance % |
|------------|-------|-----------|---------------|------------|--------------|
| IT Operations | [N] | [N] | [N] | [N] | [%] |
| Manufacturing | [N] | [N] | [N] | [N] | [%] |
| Finance | [N] | [N] | [N] | [N] | [%] |
| R&D | [N] | [N] | [N] | [N] | [%] |
| Other | [N] | [N] | [N] | [N] | [%] |

**Section 4: Non-Compliant System Summary**

| Status | Count | Target Resolution |
|--------|-------|-------------------|
| **Pending Exception Request** | [N] | Per exception process |
| **Remediation In Progress** | [N] | [Target date] |
| **Remediation Planned** | [N] | [Target date] |
| **Unaddressed** | [N] | Requires immediate action |

---

## Sheet: Gaps_Action_Items (Remediation Tracking)

**Purpose:** Aggregate and track gaps from S1, S2, S3 assessments.

**Column-by-Column Guidance:**

| Column | Field Name | Required? | Guidance |
|--------|------------|-----------|----------|
| A | **Gap ID [*]** | REQUIRED | Unique identifier |
| | | | Format: GAP-A817-S[X]-[NNN] (e.g., GAP-A817-S1-001) |
| B | **Source Assessment [*]** | REQUIRED | S1, S2, or S3 |
| C | **Gap Description [*]** | REQUIRED | Clear description of gap |
| D | **Severity [*]** | REQUIRED | Critical, High, Medium, Low |
| E | **Policy Requirement** | Optional | REQ-817-XXX reference |
| F | **Impact [*]** | REQUIRED | Business/security impact |
| G | **Remediation Plan [*]** | REQUIRED | Specific action to close gap |
| H | **Responsible Party [*]** | REQUIRED | Person/team accountable |
| I | **Target Date [*]** | REQUIRED | Target completion date |
| J | **Status [*]** | REQUIRED | Open, In Progress, Completed, Deferred |
| K | **Progress Notes** | Optional | Updates on remediation progress |
| L | **Completion Date** | Optional | Actual completion date |

**Severity Definitions:**

| Severity | Definition | Target Resolution |
|----------|------------|-------------------|
| Critical | Policy violation, security risk | <7 days |
| High | Significant compliance gap | <30 days |
| Medium | Minor compliance deviation | <90 days |
| Low | Best practice enhancement | <180 days |

**Status Definitions:**

| Status | Definition |
|--------|------------|
| Open | Gap identified, not yet started |
| In Progress | Remediation underway |
| Completed | Gap resolved, verified |
| Deferred | Risk accepted, timeline extended |

**Example Gap Entries:**

| Gap ID | Source | Description | Severity | Requirement | Impact | Remediation | Responsible | Target | Status |
|--------|--------|-------------|----------|-------------|--------|-------------|-------------|--------|--------|
| GAP-A817-S1-001 | S1 | Only 1 primary Stratum 1 source configured | High | REQ-817-002 | Single point of failure for authoritative time | Add Cloudflare as second Stratum 1 source | Network Ops | 2026-02-15 | In Progress |
| GAP-A817-S2-001 | S2 | 15 legacy servers not synchronized | Medium | REQ-817-009 | Logs cannot be correlated accurately | Upgrade NTP client or replace systems | IT Ops | 2026-03-31 | In Progress |
| GAP-A817-S3-001 | S3 | Exception EXC-20260101-003 overdue for review | High | REQ-817-021 | Compensating control not verified | Complete quarterly review | ISMS Officer | 2026-01-20 | Open |

**Summary Statistics:**

| Status | Count | Percentage |
|--------|-------|------------|
| Open | [N] | [%] |
| In Progress | [N] | [%] |
| Completed (this period) | [N] | [%] |
| Deferred | [N] | [%] |
| **Total Gaps** | [N] | 100% |

**Severity Distribution:**

| Severity | Open | In Progress | Completed | Deferred |
|----------|------|-------------|-----------|----------|
| Critical | [N] | [N] | [N] | [N] |
| High | [N] | [N] | [N] | [N] |
| Medium | [N] | [N] | [N] | [N] |
| Low | [N] | [N] | [N] | [N] |

---

# Evidence Collection

## Required Evidence Types

**Dashboard Source Data:**

- [ ] **S1 Assessment workbook** - Latest version with dates
- [ ] **S2 Assessment workbook** - Latest version with dates
- [ ] **S3 Assessment workbook** - Latest version with dates

**Validation Evidence:**

- [ ] **Calculation verification** - Spot-check compliance percentages
- [ ] **Cross-reference validation** - Totals match source workbooks

**Approval Evidence:**

- [ ] **ISMS Officer sign-off** - Review and approval record
- [ ] **CISO acknowledgment** - For executive distribution

## Evidence Naming Convention

```
Evidence Type: ISMS-A817-S4-[TYPE]-[DATE].ext

Examples:
ISMS-A817-S4-Dashboard-20260131.xlsx       (Completed dashboard)
ISMS-A817-S4-Source-S1-20260131.xlsx       (S1 source data)
ISMS-A817-S4-Source-S2-20260131.xlsx       (S2 source data)
ISMS-A817-S4-Source-S3-20260131.xlsx       (S3 source data)
ISMS-A817-S4-Approval-20260131.pdf         (Approval record)
```

## Where to Store Evidence

**Options:**
1. **ISMS document repository** - Centralized ISMS file storage
2. **Network share** - `\\fileserver\ISMS\Evidence\A.8.17\S4\`
3. **Document management** - SharePoint, Confluence, etc.

**Recommendation:** Store dashboard with source workbooks for audit trail.

---

# Common Pitfalls & How to Avoid Them

## Inconsistent Data Sources

**MISTAKE:**
Using different versions of S1, S2, S3 workbooks that don't reflect same time period.

**WHY IT'S WRONG:**
Metrics won't reconcile; compliance percentage may be incorrect.

**HOW TO AVOID:**
- Use dated versions of all source workbooks
- Document source workbook versions in Instructions sheet
- Refresh all sources together

## Double-Counting Exceptions

**MISTAKE:**
Counting exception systems in both "Compliant" and "Exceptions" categories.

**WHY IT'S WRONG:**
Inflates compliance percentage; totals don't add up.

**HOW TO AVOID:**
- Exception systems should NOT be in "Compliant" count
- Formula: Effective Compliance = (Compliant + Exceptions) / Total
- Total should equal: Compliant + Non-Compliant (where Non-Compliant includes Exceptions + Pending Remediation)

## Stale Data

**MISTAKE:**
Presenting dashboard with data from 3+ months ago.

**WHY IT'S WRONG:**
Executive decisions based on outdated information; audit risk.

**HOW TO AVOID:**
- Update monthly minimum
- Display "Last Updated" prominently
- Set calendar reminder for monthly refresh

## Missing Narrative Context

**MISTAKE:**
Presenting numbers without explanation or context.

**WHY IT'S WRONG:**
Executives can't interpret raw numbers; miss important trends.

**HOW TO AVOID:**
- Always include Executive_Summary narrative
- Explain significant changes from previous period
- Highlight items requiring executive attention

## Gap List Not Actionable

**MISTAKE:**
Listing gaps without responsible parties or target dates.

**WHY IT'S WRONG:**
Gaps won't be remediated without accountability.

**HOW TO AVOID:**
- Every gap must have assigned responsible party
- Every gap must have target date
- Review overdue gaps monthly

---

# Quality Checklist

Before distributing dashboard, verify:

**Data Accuracy:**

- [ ] Source workbook versions documented
- [ ] All S1, S2, S3 data from same assessment period
- [ ] Compliance calculation verified (spot-check)
- [ ] Totals reconcile across sheets

**Completeness:**

- [ ] Executive_Summary narrative completed
- [ ] All sections of Infrastructure_Health populated
- [ ] System_Compliance breakdown by category
- [ ] Gaps_Action_Items includes all open gaps

**Presentation:**

- [ ] Risk ratings (Green/Yellow/Red) applied consistently
- [ ] Trend chart updated with current period
- [ ] "Last Updated" date is current
- [ ] No spelling errors in narrative

**Actionability:**

- [ ] Key concerns clearly highlighted
- [ ] All gaps have responsible parties and dates
- [ ] Recommended actions for executive attention
- [ ] Upcoming expirations flagged

---

# Review & Approval Process

## Internal Review

**Step 1: Self-Review**

- Use Quality Checklist above
- Verify calculations against source workbooks
- Read narrative aloud for clarity

**Step 2: Peer Review** (Recommended)

- Another ISMS team member reviews for accuracy
- Focus on: Do numbers make sense? Is narrative clear?

**Step 3: ISMS Officer Review** (Required)

- ISMS Officer validates methodology and accuracy
- Approves for executive distribution

## Formal Approval

**Level 1: ISMS Officer**

- **Reviews:** Data accuracy, calculation methodology, completeness
- **Approves:** Dashboard ready for executive review

**Level 2: CISO** (for executive distribution)

- **Reviews:** Executive summary, risk ratings, recommended actions
- **Approves:** Dashboard suitable for leadership and audit presentation

## Distribution

**After approval:**
1. **Distribute to CISO** for executive reporting
2. **File in ISMS repository** with date-stamped version
3. **Provide to audit** when requested
4. **Schedule next update** (set calendar reminder)

**Distribution List (typical):**

- CISO (primary consumer)
- Executive Management (as needed)
- IT Security Team
- Audit/Compliance Team
- Risk Management

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook developers, Python script maintainers, technical implementers

**Note:** This section provides technical specifications for compliance dashboard workbook structure. Users completing the assessment should refer to Part I above.

---

# Implementation Requirement Mapping

**This section maps dashboard metrics to policy requirements for traceability.**

## Dashboard Metrics to Policy Mapping

| Dashboard Metric | Policy Requirement(s) | Source Assessment |
|-----------------|----------------------|-------------------|
| External Source Count | REQ-817-001, REQ-817-002 | S1 |
| Internal Server Count | REQ-817-005, REQ-817-006 | S1 |
| Monitoring Coverage | REQ-817-008 | S1 |
| System Compliance % | REQ-817-009, REQ-817-010 | S2 |
| Exception Count | REQ-817-017, REQ-817-019 | S3 |
| Gap Remediation | All REQ-817-xxx | S1, S2, S3 |

---

# SECTION A: Implementation Guidance

## Introduction

This section provides technical guidance for creating and maintaining the compliance dashboard, including metric calculations, data aggregation, and visualization best practices.

**Purpose:** Enable ISMS Officers to create consistent, accurate compliance dashboards that aggregate findings from S1, S2, S3 assessments.

**Scope:** Executive-level reporting on clock synchronization compliance.

**Related Documents:**

- ISMS-POL-A.8.17 (Clock Synchronization Policy)
- ISMS-IMP-A.8.17-S1 (Time Source Configuration)
- ISMS-IMP-A.8.17-S2 (Synchronization Verification)
- ISMS-IMP-A.8.17-S3 (Exception Management)

---

## Compliance Calculation Methodology

### Overall Compliance Score

**Formula:**

```
Overall Compliance % = ((Compliant Systems + Systems with Approved Exceptions) / Total Systems in Scope) × 100
```

**Components:**

| Component | Source | Description |
|-----------|--------|-------------|
| Compliant Systems | S2 Verification_Results | Systems verified as synchronized to approved time sources |
| Systems with Approved Exceptions | S3 Active_Exceptions | Systems with approved exceptions and compensating controls |
| Total Systems in Scope | S2 System_Inventory | All systems subject to clock synchronization policy |

**Example Calculation:**

```
Total Systems: 1,234
Compliant Systems: 1,200
Approved Exceptions: 3

Overall Compliance = (1,200 + 3) / 1,234 × 100 = 97.5%
```

**Important Notes:**

- Systems with approved exceptions count toward compliance (they have compensating controls)
- Systems pending exception approval do NOT count toward compliance
- Systems pending remediation do NOT count toward compliance

### Infrastructure Health Score

**Formula:**

```
Infrastructure Health = (Metrics Met / Total Metrics) × 100
```

**Metrics Evaluated:**

| Metric | Requirement | Weight |
|--------|-------------|--------|
| External Sources ≥ 2 | REQ-817-001 | Critical |
| Primary Sources ≥ 2 | REQ-817-002 | Critical |
| Internal Servers ≥ 2 | REQ-817-005 | Critical |
| All Servers Stratum 2/3 | REQ-817-006 | High |
| All Servers Monitored with Alerting | REQ-817-008 | Critical |
| All Sources/Servers Active | Operational | High |

**Status Determination:**

| Health Score | Status |
|--------------|--------|
| 100% | Green |
| 80-99% | Yellow (minor gaps) |
| <80% | Red (critical gaps) |

---

## Data Aggregation Logic

### From S1 (Time Source Configuration)

**Metrics to Extract:**

```excel
External Source Count = COUNTA(S1_Time_Sources!A2:A100)
Primary Sources (Stratum 0/1) = COUNTIFS(S1_Time_Sources!D2:D100,"<=1")
Internal Server Count = COUNTA(S1_Internal_NTP_Servers!A2:A100)
Servers with Alerting = COUNTIF(S1_Internal_NTP_Servers!H2:H100,"*Monitored with Alerting*")
Active Sources = COUNTIF(S1_Time_Sources!I2:I100,"*Active*")
Active Servers = COUNTIF(S1_Internal_NTP_Servers!J2:J100,"*Active*")
```

### From S2 (Synchronization Verification)

**Metrics to Extract:**

```excel
Total Systems = COUNTA(S2_System_Inventory!A2:A5000)
Compliant Systems = COUNTIF(S2_Verification_Results!F2:F5000,"Compliant")
Non-Compliant Systems = COUNTIF(S2_Verification_Results!F2:F5000,"Non-Compliant")
```

### From S3 (Exception Management)

**Metrics to Extract:**

```excel
Active Exceptions = COUNTA(S3_Active_Exceptions!A2:A100)
Pending Requests = COUNTIF(S3_Exception_Requests!P2:P100,"<>Approved")
Expiring Soon = COUNTIFS(S3_Active_Exceptions!J2:J100,"<="&TODAY()+30,S3_Active_Exceptions!J2:J100,">="&TODAY())
```

---

## Visualization Guidelines

### Compliance Score Display

**Design:**

- Large font (36-48pt) for percentage
- Color-coded background (Green/Yellow/Red)
- Trend arrow (up/down/flat)

**Example:**

```
┌─────────────────────┐
│    COMPLIANCE       │
│                     │
│      97.5%  ↑       │
│                     │
│  [GREEN BACKGROUND] │
└─────────────────────┘
```

### Trend Chart

**Type:** Line chart

**X-Axis:** Time periods (monthly or quarterly)

**Y-Axis:** Compliance percentage (0-100%)

**Guidelines:**

- Show 6-12 months of data
- Include target line (e.g., 95%)
- Annotate significant events

### Status Indicators

**Green/Yellow/Red Indicators:**

Use consistent colors across dashboard:

- Green: RGB(0, 176, 80) or Hex #00B050
- Yellow: RGB(255, 192, 0) or Hex #FFC000
- Red: RGB(255, 0, 0) or Hex #FF0000

---

# SECTION B: Assessment Workbook Specification

## Workbook Overview

**Filename:** ISMS-IMP-A.8.17-S4_Compliance_Dashboard_[YYYYMMDD].xlsx

**Generated By:** `generate_a817_s4_compliance_dashboard.py`

**Purpose:** Executive dashboard aggregating S1-S3 compliance findings

**Sheets:**
1. **Instructions** - Dashboard guidance
2. **Executive_Summary** - Overall compliance score and status
3. **Infrastructure_Health** - NTP infrastructure health metrics
4. **System_Compliance** - System-level sync compliance
5. **Gaps_Action_Items** - Remediation tracking

**Total Sheets:** 5

---

## Common Styling Definitions

**Header Style:**

- Font: Bold, White (FFFFFF), Size 11
- Fill: Dark Blue (366092)
- Alignment: Center, Vertical Center, Wrap Text
- Border: Thin borders all sides

**Title Style:**

- Font: Bold, Size 14, Dark Blue (366092)
- Alignment: Left, Vertical Center

**Big Number Style (Compliance Score):**

- Font: Bold, Size 36, Color based on threshold
- Alignment: Center, Vertical Center

**Status Green:**

- Fill: RGB(0, 176, 80)
- Font: White, Bold

**Status Yellow:**

- Fill: RGB(255, 192, 0)
- Font: Black, Bold

**Status Red:**

- Fill: RGB(255, 0, 0)
- Font: White, Bold

---

## Sheet 1: Instructions

**Purpose:** Provide dashboard usage instructions and metric definitions.

**Layout:**

**Row 1-2:** Title Block

- A1: "ISMS A.8.17-S4 - Compliance Dashboard" (Font: Bold 16, Dark Blue, Merged A1:F1)
- A2: "Version 1.0 | [Last Updated Date]" (Font: Italic 10, Merged A2:F2)

**Row 4-5:** Document Metadata

- A4: "Document ID:" (Bold) | B4: "ISMS-IMP-A.8.17-S4" (Bold, Dark Blue)
- A5: "Title:" (Bold) | B5: "Clock Synchronization Compliance Dashboard"

**Row 7+:** Instructions Content

- Purpose statement
- Data source descriptions (S1, S2, S3)
- Metric definitions
- Update frequency guidance
- Risk rating definitions
- Contact information

**Column Widths:**

- A: 20
- B: 80
- C-F: 15 each

---

## Sheet 2: Executive_Summary

**Purpose:** Single-page executive view of compliance status.

**Layout:**

**Section 1: Compliance Score (Rows 1-8)**

| Cell | Content | Format |
|------|---------|--------|
| A1:D1 | "Clock Synchronization Compliance Dashboard" | Title, merged |
| A2:D2 | "Last Updated: [Date]" | Subtitle, merged |
| B4:C6 | [Compliance %] | Big Number, 36pt, color-coded, merged |
| D4:D6 | [Trend Arrow] | Arrow icon |
| A8 | "Risk Rating:" | Label |
| B8 | [Green/Yellow/Red] | Status indicator |

**Section 2: Key Metrics (Rows 10-18)**

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 10 | "KEY METRICS" (Header) | | |
| 11 | "Metric" | "Value" | "Status" |
| 12 | "Total Systems in Scope" | [Number] | |
| 13 | "Compliant Systems" | [Number] | |
| 14 | "Non-Compliant Systems" | [Number] | |
| 15 | "Systems with Exceptions" | [Number] | |
| 16 | "Pending Remediation" | [Number] | Warning if >0 |
| 17 | "Infrastructure Status" | [Green/Yellow/Red] | |

**Section 3: Executive Summary Narrative (Rows 20-30)**

| Row | Content |
|-----|---------|
| 20 | "EXECUTIVE SUMMARY" (Header) |
| 21-30 | Free-form text area for narrative |

**Section 4: Trend Chart (Rows 32-45)**

Embedded line chart showing compliance trend over time.

---

## Sheet 3: Infrastructure_Health

**Purpose:** Show NTP infrastructure health from S1 assessment.

**Layout:**

**Section 1: External Time Sources (Rows 1-10)**

| Row | Column A | Column B | Column C | Column D |
|-----|----------|----------|----------|----------|
| 1 | "EXTERNAL TIME SOURCES" (Header, merged A1:D1) | | | |
| 2 | "Metric" | "Requirement" | "Actual" | "Status" |
| 3 | "External Source Count" | "≥2" | [Formula] | [Pass/Fail] |
| 4 | "Primary Sources (Stratum 0/1)" | "≥2" | [Formula] | [Pass/Fail] |
| 5 | "Sources Active" | "100%" | [Formula] | [Pass/Fail] |

**Section 2: Internal NTP Servers (Rows 12-20)**

Similar structure.

**Section 3: Monitoring (Rows 22-28)**

Similar structure.

**Section 4: Overall Infrastructure Status (Rows 30-35)**

Summary with overall Green/Yellow/Red status.

---

## Sheet 4: System_Compliance

**Purpose:** Show system-level compliance from S2 assessment.

**Layout:**

**Section 1: Overall Compliance (Rows 1-12)**

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 1 | "SYSTEM COMPLIANCE OVERVIEW" (Header) | | |
| 2 | "Metric" | "Count" | "Percentage" |
| 3 | "Total Systems in Scope" | [Number] | "100%" |
| 4 | "Compliant Systems" | [Number] | [Formula] |
| 5 | "Non-Compliant Systems" | [Number] | [Formula] |
| 6 | "With Approved Exceptions" | [Number] | [Formula] |
| 7 | "Pending Remediation" | [Number] | [Formula] |
| 9 | "EFFECTIVE COMPLIANCE" | [Number] | [Formula] |

**Section 2: By Category (Rows 14-25)**

Table with categories: Servers, Workstations, Network Devices, OT/ICS, Cloud, Other.

**Section 3: By Department (Rows 27-40)**

Table with department breakdown.

**Section 4: Non-Compliant Summary (Rows 42-50)**

Breakdown of non-compliant systems by status.

---

## Sheet 5: Gaps_Action_Items

**Purpose:** Track remediation of gaps from S1, S2, S3.

**Headers (Row 1):**

| Column | Header | Width |
|--------|--------|-------|
| A | Gap ID | 18 |
| B | Source Assessment | 12 |
| C | Gap Description | 40 |
| D | Severity | 12 |
| E | Policy Requirement | 15 |
| F | Impact | 30 |
| G | Remediation Plan | 40 |
| H | Responsible Party | 20 |
| I | Target Date | 12 |
| J | Status | 15 |
| K | Progress Notes | 35 |
| L | Completion Date | 12 |

**Data Validation:**

**Column B (Source Assessment):**

- Type: List
- Formula: `"S1,S2,S3"`

**Column D (Severity):**

- Type: List
- Formula: `"Critical,High,Medium,Low"`

**Column J (Status):**

- Type: List
- Formula: `"Open,In Progress,Completed,Deferred"`

**Conditional Formatting:**

- Severity = "Critical": Red fill
- Severity = "High": Orange fill
- Status = "Completed": Green fill, strikethrough text
- Target Date < TODAY() AND Status <> "Completed": Red text (overdue)

**Summary Section (Rows 50+):**

Status distribution and severity distribution tables.

---

## Python Script Reference

**Script File:** `generate_a817_s4_compliance_dashboard.py`

**Script Location:** `10-isms-scr-base/isms-a.8.17-clock-synchronization/10_generator-master/`

**Key Functions:**

- `create_styles()` - Defines all styling
- `create_instructions_sheet()` - Generates Instructions sheet
- `create_executive_summary_sheet()` - Generates Executive_Summary sheet
- `create_infrastructure_health_sheet()` - Generates Infrastructure_Health sheet
- `create_system_compliance_sheet()` - Generates System_Compliance sheet
- `create_gaps_action_items_sheet()` - Generates Gaps_Action_Items sheet
- `main()` - Orchestrates workbook generation

**To regenerate workbook:**

```bash
cd 10-isms-scr-base/isms-a.8.17-clock-synchronization/10_generator-master
python3 generate_a817_s4_compliance_dashboard.py
mv *.xlsx ../90_workbooks/
```

**Output:** Excel workbook ready for user completion per Part I User Guide.

---

## Linking to Source Workbooks

**For automated updates, link cells to source workbooks:**

**Example Formulas (assuming workbooks in same folder):**

```excel
' External Source Count (from S1)
='[ISMS-IMP-A.8.17-S1_Time_Source_Configuration.xlsx]Time_Sources'!$A$1:COUNTA($A:$A)-1

' Compliant Systems (from S2)
='[ISMS-IMP-A.8.17-S2_Synchronization_Verification.xlsx]Summary'!$B$5

' Active Exceptions (from S3)
='[ISMS-IMP-A.8.17-S3_Exception_Management.xlsx]Summary_Dashboard'!$B$5
```

**Best Practice:**

- Store all A.8.17 workbooks in same folder for easy linking
- Update all workbooks together to maintain consistency
- Document linked workbook locations in Instructions sheet

---

**END OF SPECIFICATION**

---

*"Time is the wisest counselor of all."*
— Pericles

<!-- QA_VERIFIED: 2026-02-01 -->
