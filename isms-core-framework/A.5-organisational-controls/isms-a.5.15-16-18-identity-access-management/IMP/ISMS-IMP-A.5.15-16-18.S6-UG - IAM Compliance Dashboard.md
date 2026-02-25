<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.15-16-18.S6-UG:framework:UG:a.5.15-16-18 -->
**ISMS-IMP-A.5.15-16-18.S6-UG - IAM Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Controls A.5.15, A.5.16, A.5.18: Identity and Access Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S6-UG |
| **Version** | 1.0 |
| **Assessment Area** | IAM Governance Compliance Dashboard - Consolidated Metrics |
| **Related Policy** | ISMS-POL-A.5.15-16-18 (All Sections) |
| **Purpose** | Provide consolidated executive dashboard for IAM compliance across all assessment domains (S1-S5), enabling governance oversight, audit readiness, and continuous improvement tracking |
| **Target Audience** | CISO, Security Management, Internal Audit, Executive Leadership, Board/Audit Committee, External Auditors |
| **Assessment Type** | Executive Dashboard & Governance Reporting |
| **Review Cycle** | Monthly (metric refresh), Quarterly (executive review), Annually (comprehensive audit) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for IAM Compliance Dashboard - consolidates S1-S5 metrics | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.15-16-18.S6-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.15-16-18.S6 - IAM Compliance Dashboard

#### What This Assessment Covers

This dashboard CONSOLIDATES all IAM compliance metrics from the five assessment domains into a single executive view. It answers:

- **What is our overall IAM compliance posture?** (Composite score across all domains)
- **Where are we strong?** (Domains meeting or exceeding targets)
- **Where are we weak?** (Domains requiring immediate attention)
- **What gaps require remediation?** (Consolidated gap register across all assessments)
- **What evidence do we have?** (Audit-ready evidence summary)
- **What is our maturity trajectory?** (Trend analysis over time)
- **Are we ready for audit?** (Certification readiness assessment)

#### Data Sources - The S1-S5 Assessments

| Source Assessment | What It Provides to S6 Dashboard |
|-------------------|----------------------------------|
| **S1: User Inventory & Lifecycle** | User counts, provisioning SLA compliance, deprovisioning timeliness, orphaned accounts |
| **S2: Access Rights Matrix** | Access documentation completeness, privileged access counts, excessive access findings |
| **S3: Access Review Results** | Access review completion rates, review findings, attestation status |
| **S4: Role Definition & SoD** | RBAC adoption rate, SoD violations, role compliance metrics |
| **S5: Lifecycle Compliance** | Joiner/mover/leaver SLA compliance, HR integration status, contractor expiration |

#### Key Principle

This dashboard does NOT generate new data - it **aggregates and visualises** data from S1-S5 assessments. If source assessments are incomplete or inaccurate, the dashboard will reflect those deficiencies.

#### What You Will Document

- **Executive Summary**: Overall IAM compliance score, maturity level, key findings
- **Domain Compliance Scores**: Individual scores for each assessment domain (S1-S5)
- **Gap Analysis Consolidation**: All gaps from S1-S5 in prioritised register
- **KPI Tracking**: Key performance indicators with targets, actuals, and trends
- **Evidence Summary**: Consolidated evidence register for audit readiness
- **Remediation Progress**: Gap closure tracking across all domains
- **Trend Analysis**: Month-over-month and quarter-over-quarter improvement tracking
- **Certification Readiness**: ISO 27001 audit readiness assessment

#### How This Relates to Other A.5.15-16-18 Assessments

| Assessment | Focus | Relationship to S6 Dashboard |
|------------|-------|------------------------------|
| S1 | User Inventory & Lifecycle | S6 pulls lifecycle compliance metrics |
| S2 | Access Rights Matrix | S6 pulls access documentation scores |
| S3 | Access Review Results | S6 pulls review completion rates |
| S4 | Role Definition & SoD | S6 pulls RBAC and SoD metrics |
| S5 | Lifecycle Compliance | S6 pulls detailed JML event compliance |
| **S6** | **IAM Compliance Dashboard** | **CONSOLIDATES all S1-S5 metrics** |

This assessment (S6) is the **capstone dashboard** that provides the executive view across all IAM assessment domains.

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **IAM Manager** - Consolidates data from S1-S5 assessments, prepares dashboard
2. **Security Manager** - Reviews dashboard, validates metrics, approves findings
3. **CISO** - Executive sponsor, uses dashboard for governance reporting
4. **Internal Audit** - Uses dashboard for audit planning and evidence review
5. **Executive Leadership** - Receives quarterly dashboard reports

#### Required Skills

- Understanding of all five IAM assessment domains (S1-S5)
- Data consolidation and analysis skills
- Executive reporting and visualisation
- Understanding of ISO 27001 certification requirements
- Risk assessment and prioritisation

#### Time Commitment

- **Initial dashboard creation:** 8-10 hours (consolidate S1-S5 data, build metrics, create visualisations)
- **Monthly refresh:** 2-4 hours (update metrics from latest S1-S5 assessments)
- **Quarterly executive report:** 4-6 hours (trend analysis, executive summary, presentation)

### Expected Outputs

Upon completion, you will have:

1. **Executive Summary** - One-page IAM compliance overview with composite score
2. **Domain Compliance Scores** - Individual scores for S1-S5 with status indicators
3. **Consolidated Gap Register** - All gaps from S1-S5 in prioritised list
4. **KPI Dashboard** - Key metrics with targets, actuals, trends, and RAG status
5. **Evidence Summary** - Audit-ready evidence catalogue with completeness assessment
6. **Trend Analysis** - Historical compliance trajectory (improving, stable, declining)
7. **Certification Readiness** - ISO 27001 audit readiness checklist
8. **Approved Dashboard** - Three-level approval workflow completed

---

## Prerequisites

### Information You Will Need

Before starting this assessment, ensure:

#### 1. Completed S1-S5 Assessments

All source assessments must be completed and current:

- **S1: User Inventory & Lifecycle** (within 30 days)
- **S2: Access Rights Matrix** (within 30 days)
- **S3: Access Review Results** (within 30 days)
- **S4: Role Definition & SoD** (within 30 days)
- **S5: Lifecycle Compliance** (within 30 days)

**CRITICAL:** S6 dashboard is only as good as its source data. Stale or incomplete S1-S5 assessments = inaccurate dashboard.

#### 2. Metrics from Each Assessment

From each source assessment, extract:

| Assessment | Required Metrics |
|------------|------------------|
| **S1** | Total users, active/disabled counts, provisioning on-time %, deprovisioning on-time %, orphaned account count |
| **S2** | Total access grants, documentation completeness %, privileged access count, excessive access count |
| **S3** | Access reviews scheduled, reviews completed %, findings count, attestation completion % |
| **S4** | RBAC adoption %, SoD violations count, role compliance score |
| **S5** | Joiner SLA compliance %, leaver SLA compliance %, mover SLA compliance %, contractor expiration compliance % |

#### 3. Gap Analysis Data

From each source assessment, extract gap analysis data:

- Gap ID, description, risk level, owner, due date, status
- Consolidate into single gap register

#### 4. Evidence Register Data

From each source assessment, extract evidence register:

- Evidence ID, requirement, type, location, completeness
- Consolidate into single evidence catalogue

#### 5. Historical Data (for Trend Analysis)

If available, gather previous dashboard data:

- Previous month's composite score
- Previous quarter's domain scores
- Historical gap closure rates

### Required Tools

- **Microsoft Excel** (2016 or later) for dashboard completion
- **Completed S1-S5 workbooks** for data extraction
- **Evidence folder** with S1-S5 supporting documentation
- **Historical dashboards** (if available) for trend analysis

### Dependencies

**CRITICAL DEPENDENCY:**

- **ISMS-IMP-A.5.15-16-18.S1 through S5** MUST be completed first
- S6 dashboard consolidates data from all five assessments
- Missing assessments = incomplete dashboard

**Outputs FROM this dashboard feed INTO:**

- CISO governance reports
- Audit committee presentations
- ISO 27001 certification evidence
- Risk management reporting

---

## Workflow

### High-Level Process

```
1. PREPARE (Verify S1-S5 completed)
   |
2. EXTRACT METRICS (From each S1-S5 assessment)
   |
3. BUILD EXECUTIVE SUMMARY (Sheet 2)
   |
4. POPULATE DOMAIN SCORES (Sheet 3)
   |
5. CONSOLIDATE GAPS (Sheet 4)
   |
6. POPULATE KPIs (Sheet 5)
   |
7. CONSOLIDATE EVIDENCE (Sheet 6)
   |
8. CALCULATE TRENDS (Sheet 7) - if historical data available
   |
9. ASSESS CERTIFICATION READINESS (Sheet 8)
   |
10. REVIEW & APPROVE (Sheet 9)
```

### Detailed Workflow

#### Phase 1: Preparation (1-2 hours)

**Objective:** Verify all source assessments are complete and current

**Steps:**

1. Locate all S1-S5 assessment workbooks
2. Verify each assessment is:
   - Completed (all sheets populated)
   - Approved (three-level sign-off completed)
   - Current (within 30 days)
3. Create working folder for S6 dashboard
4. Download S6 dashboard template (generated workbook)

**Deliverable:** All S1-S5 workbooks ready for data extraction

**Quality Check:**

- All five assessments (S1-S5) located and accessible
- Each assessment has approval sign-off completed
- Assessment dates within acceptable range (30 days)
- No critical gaps blocking dashboard creation

---

#### Phase 2: Extract Metrics from Source Assessments (2-3 hours)

**Objective:** Gather key metrics from each S1-S5 assessment

**Steps:**

**From S1 (User Inventory & Lifecycle):**

1. Open S1 workbook Sheet 7 (Lifecycle_Metrics)
2. Extract:
   - Total user count (from Sheet 2)
   - Active user count
   - Disabled user count
   - Provisioning on-time rate (%)
   - Deprovisioning on-time rate (%)
   - Orphaned account count (from Sheet 6)
   - Overall S1 compliance score

**From S2 (Access Rights Matrix):**

1. Open S2 workbook Sheet 6 (Compliance Dashboard)
2. Extract:
   - Total access grants documented
   - Access documentation completeness (%)
   - Privileged access count
   - Excessive access count
   - Group-based vs. direct access ratio
   - Overall S2 compliance score

**From S3 (Access Review Results):**

1. Open S3 workbook Sheet 6 (Review Metrics)
2. Extract:
   - Reviews scheduled for period
   - Reviews completed (%)
   - Access confirmed (%)
   - Access revoked (%)
   - Findings requiring remediation
   - Overall S3 compliance score

**From S4 (Role Definition & SoD):**

1. Open S4 workbook Sheet 6 (SoD Dashboard)
2. Extract:
   - RBAC adoption rate (%)
   - Total roles defined
   - SoD violations detected
   - SoD violations remediated
   - Role certification status
   - Overall S4 compliance score

**From S5 (Lifecycle Compliance):**

1. Open S5 workbook Sheet 7 (Timeliness_Metrics)
2. Extract:
   - Joiner on-time provisioning (%)
   - Mover access update (%)
   - Leaver on-time deprovisioning (%)
   - Contractor expiration compliance (%)
   - Orphaned account remediation (%)
   - Overall S5 compliance score

**Deliverable:** Metrics spreadsheet with all extracted values

**Quality Check:**

- All metrics extracted from current assessments
- No missing values (if metric unavailable, note as "N/A" with explanation)
- Metrics align with assessment dates (consistent reporting period)
- Calculations verified (spot check source → extracted value)

---

#### Phase 3: Build Executive Summary (1 hour)

**Objective:** Complete Sheet 2 - Executive Summary

**Steps:**

1. **Calculate Composite IAM Compliance Score:**
   ```
   Composite Score =
     (S1 Score × 20%) +
     (S2 Score × 20%) +
     (S3 Score × 20%) +
     (S4 Score × 20%) +
     (S5 Score × 20%)
   ```

   Alternatively, weight based on risk:
   ```
   Composite Score =
     (S1 Score × 15%) +   // User inventory
     (S2 Score × 25%) +   // Access rights (higher weight - audit focus)
     (S3 Score × 20%) +   // Access review
     (S4 Score × 15%) +   // RBAC/SoD
     (S5 Score × 25%)     // Lifecycle (higher weight - security critical)
   ```

2. **Determine Maturity Level:**
   - **Optimised (90-100%)**: Best-in-class IAM, continuous improvement
   - **Managed (75-89%)**: Strong controls, minor gaps
   - **Defined (60-74%)**: Documented processes, significant gaps
   - **Developing (40-59%)**: Basic controls, major gaps
   - **Initial (<40%)**: Ad-hoc processes, critical gaps

3. **Summarise Key Findings:**
   - Top 3 strengths (highest scoring areas)
   - Top 3 weaknesses (lowest scoring areas)
   - Critical gaps requiring immediate action
   - Audit readiness status

4. **Document Recommendations:**
   - Priority 1 actions (critical/high risk)
   - Priority 2 actions (medium risk)
   - Strategic improvements (long-term)

**Deliverable:** Complete Sheet 2 with executive summary

**Quality Check:**

- Composite score calculated correctly
- Maturity level assignment accurate
- Key findings reflect actual assessment data
- Recommendations are actionable and prioritised

---

#### Phase 4: Populate Domain Compliance Scores (1 hour)

**Objective:** Complete Sheet 3 - Domain Compliance Scores

**Steps:**

1. For each domain (S1-S5), document:
   - Domain name and description
   - Individual compliance score (from source assessment)
   - Target score (organisational target, typically 85%+)
   - Gap to target (Target - Actual)
   - Status (Compliant, Warning, Non-Compliant)
   - Key metrics contributing to score
   - Summary of findings
   - Remediation status

2. **Assign status based on score:**
   - **Compliant** (green): Score >= 85%
   - **Warning** (yellow): Score 60-84%
   - **Non-Compliant** (red): Score < 60%

3. **Document trend vs. previous period:**
   - Improving (up arrow)
   - Stable (horizontal arrow)
   - Declining (down arrow)

**Deliverable:** Complete Sheet 3 with all domain scores

**Quality Check:**

- All five domains (S1-S5) documented
- Scores match source assessments exactly
- Status assignments reflect actual scores
- Trends accurate (if historical data available)

---

#### Phase 5: Consolidate Gap Analysis (1-2 hours)

**Objective:** Complete Sheet 4 - Consolidated Gap Register

**Steps:**

1. **Extract gaps from each source assessment:**
   - S1 Sheet 8 (Gap_Analysis)
   - S2 Sheet 8 (Gap_Analysis)
   - S3 Sheet 7 (Gap_Analysis)
   - S4 Sheet 7 (Gap_Analysis)
   - S5 Sheet 9 (Gap_Analysis)

2. **For each gap, document:**
   - Gap ID (unique across all assessments)
   - Source assessment (S1, S2, S3, S4, or S5)
   - Category (Provisioning, Access Rights, Access Review, RBAC, Lifecycle, etc.)
   - Description
   - Risk level (Critical, High, Medium, Low)
   - Affected users/items
   - Root cause
   - Remediation plan
   - Owner
   - Due date
   - Status (Open, In Progress, Closed)

3. **Prioritise gaps:**
   - Sort by risk level (Critical first, then High, Medium, Low)
   - Within risk level, sort by due date (nearest first)

4. **Calculate gap metrics:**
   - Total gaps identified
   - Critical gaps count
   - High gaps count
   - Gaps closed this period
   - Gap closure rate (%)
   - Average days to close

**Deliverable:** Complete Sheet 4 with consolidated gap register

**Quality Check:**

- All gaps from S1-S5 included
- No duplicate gaps
- Risk levels assigned consistently
- Owners assigned for all gaps
- Due dates realistic

---

#### Phase 6: Populate KPI Dashboard (1 hour)

**Objective:** Complete Sheet 5 - KPI Dashboard

**Steps:**

1. **Document each KPI:**

| KPI | Target | Actual | Status | Gap | Source |
|-----|--------|--------|--------|-----|--------|
| User Inventory Completeness | 100% | [from S1] | | | S1 |
| Provisioning On-Time Rate | >= 95% | [from S1/S5] | | | S1/S5 |
| Deprovisioning On-Time Rate | >= 98% | [from S1/S5] | | | S1/S5 |
| Orphaned Account Count | <= 1% | [from S1] | | | S1 |
| Access Documentation Completeness | >= 90% | [from S2] | | | S2 |
| Privileged Access Review | 100% | [from S2/S3] | | | S2/S3 |
| Access Review Completion | >= 95% | [from S3] | | | S3 |
| RBAC Adoption Rate | >= 80% | [from S4] | | | S4 |
| SoD Violations Open | 0 | [from S4] | | | S4 |
| Contractor Expiration Compliance | 100% | [from S5] | | | S5 |

2. **Assign status:**
   - **Compliant** (green): Actual meets or exceeds target
   - **Warning** (yellow): Actual within 10% of target
   - **Non-Compliant** (red): Actual more than 10% below target

3. **Calculate gap:**
   - Gap = Target - Actual (positive = below target, negative = exceeding target)

**Deliverable:** Complete Sheet 5 with KPI dashboard

**Quality Check:**

- All KPIs populated
- Targets reflect organisational policy
- Actuals match source assessments
- Status assignments accurate
- Source assessment documented for each KPI

---

#### Phase 7: Consolidate Evidence Register (1 hour)

**Objective:** Complete Sheet 6 - Evidence Summary

**Steps:**

1. **Extract evidence from each source assessment:**
   - S1 Sheet 9 (Evidence_Register)
   - S2 Sheet 9 (Evidence_Register)
   - S3 Sheet 8 (Evidence_Register)
   - S4 Sheet 8 (Evidence_Register)
   - S5 Sheet 10 (Evidence_Register)

2. **For each evidence item, document:**
   - Evidence ID (unique)
   - Source assessment (S1, S2, S3, S4, S5)
   - ISO 27001 requirement (A.5.15, A.5.16, A.5.18)
   - Evidence type
   - Evidence location
   - Collection date
   - Completeness (Complete, Partial, Missing)
   - Verified by

3. **Calculate evidence metrics:**
   - Total evidence items
   - Complete evidence count
   - Partial evidence count
   - Missing evidence count
   - Evidence completeness score (%)

4. **Map evidence to ISO 27001 requirements:**
   - A.5.15 (Access Control): Evidence from S2, S3
   - A.5.16 (Identity Management): Evidence from S1, S5
   - A.5.18 (Access Rights): Evidence from S2, S4

**Deliverable:** Complete Sheet 6 with evidence summary

**Quality Check:**

- All evidence from S1-S5 included
- Evidence locations verified and accessible
- Completeness assessments accurate
- ISO 27001 mapping correct
- Evidence ready for audit

---

#### Phase 8: Calculate Trends (Optional - 30 minutes)

**Objective:** Complete Sheet 7 - Trend Analysis (if historical data available)

**Steps:**

1. **If previous dashboards exist:**
   - Enter previous month's composite score
   - Enter previous quarter's composite score
   - Enter previous domain scores (S1-S5)

2. **Calculate trends:**
   - Month-over-month change (%)
   - Quarter-over-quarter change (%)
   - Trend direction (Improving, Stable, Declining)

3. **Project trajectory:**
   - At current improvement rate, when will target be achieved?
   - Are we on track for certification timeline?

**Deliverable:** Complete Sheet 7 with trend analysis

**Quality Check:**

- Historical data accurate (matches previous dashboards)
- Trend calculations correct
- Trajectory projections realistic

---

#### Phase 9: Assess Certification Readiness (30 minutes)

**Objective:** Complete Sheet 8 - Certification Readiness

**Steps:**

1. **For each ISO 27001 requirement, assess:**

| Requirement | Control | Evidence Status | Gap Status | Readiness |
|-------------|---------|-----------------|------------|-----------|
| A.5.15 | Access Control | [from S2, S3] | | |
| A.5.16 | Identity Management | [from S1, S5] | | |
| A.5.18 | Access Rights | [from S2, S4] | | |

2. **Determine overall certification readiness:**
   - **Ready**: All controls compliant, evidence complete, no critical gaps
   - **Mostly Ready**: Minor gaps, evidence mostly complete
   - **Not Ready**: Significant gaps, evidence incomplete

3. **Document audit blockers:**
   - Critical gaps that would result in non-conformity
   - Missing evidence that auditor would flag
   - Process gaps requiring documentation

**Deliverable:** Complete Sheet 8 with certification readiness assessment

**Quality Check:**

- All relevant controls assessed
- Readiness status reflects actual evidence and gap status
- Audit blockers clearly identified
- Remediation timeline realistic for certification date

---

#### Phase 10: Review & Approval (1-2 hours)

**Objective:** Three-level approval process (Sheet 9)

**Steps:**

**Step 1: Self-Review** (Dashboard Creator)

- Verify all sheets complete
- Check calculations and formulas
- Validate data matches source assessments
- Ensure evidence register is accurate

**Step 2: Security Manager Review**

- Review overall compliance posture
- Validate gap prioritisation
- Confirm remediation plans are adequate
- Approve or request changes

**Step 3: CISO Approval**

- Review executive summary
- Confirm certification readiness assessment
- Accept risk for outstanding gaps (if applicable)
- Final approval for governance reporting

**Deliverable:** Approved dashboard ready for distribution

**Quality Check:**

- All three approval levels completed
- Review comments addressed
- Dashboard suitable for executive distribution
- Evidence audit-ready

---

## Evidence Collection

### What Evidence to Collect

**For Executive Summary (Sheet 2):**

- Composite score calculation methodology
- Maturity assessment criteria
- Previous period comparisons (if available)

**For Domain Scores (Sheet 3):**

- Source S1-S5 workbooks (archived with date)
- Score calculation worksheets
- Variance explanations

**For Gap Register (Sheet 4):**

- Source gap analysis sheets from S1-S5
- Remediation project plans
- Gap closure evidence

**For KPI Dashboard (Sheet 5):**

- KPI source data extracts
- Target approval documentation
- Historical KPI tracking

**For Evidence Summary (Sheet 6):**

- All evidence items referenced
- Evidence index/catalogue
- Evidence storage location documentation

**For Trend Analysis (Sheet 7):**

- Previous dashboard versions
- Historical metric tracking
- Improvement initiative documentation

**For Certification Readiness (Sheet 8):**

- ISO 27001 control mapping
- Audit preparation checklist
- Previous audit findings (if any)

### How to Organise Evidence

**Folder Structure:**
```
ISMS-A.5.15-16-18.S6_Dashboard_YYYYMMDD/
+-- 01_Source_Assessments/
|   +-- S1_User_Inventory_YYYYMMDD.xlsx
|   +-- S2_Access_Rights_YYYYMMDD.xlsx
|   +-- S3_Access_Review_YYYYMMDD.xlsx
|   +-- S4_Role_SoD_YYYYMMDD.xlsx
|   +-- S5_Lifecycle_YYYYMMDD.xlsx
+-- 02_Extracted_Metrics/
+-- 03_Gap_Remediation/
+-- 04_Historical_Dashboards/
+-- 05_Approval_Records/
+-- S6_IAM_Dashboard_YYYYMMDD.xlsx
```

### Evidence Retention

- **Minimum retention:** 3 years (ISO 27001 certification cycle)
- **Recommended retention:** 5 years (trend analysis, improvement tracking)
- **Storage location:** Secure document management system (SharePoint, Confluence, or equivalent)
- **Access:** CISO, Security Management, Internal Audit, External Auditors

---

## Common Pitfalls

### Pitfall 1: Stale Source Assessments

**Mistake:** Using S1-S5 assessments that are several months old, resulting in inaccurate dashboard

**Fix:** Ensure all source assessments are within 30 days of dashboard creation. If assessments are stale, refresh them before building the dashboard. Document assessment dates prominently on the dashboard.

---

### Pitfall 2: Inconsistent Metric Definitions

**Mistake:** Metrics calculated differently across S1-S5 assessments (e.g., "compliance rate" means different things)

**Fix:** Establish standard metric definitions documented in the Instructions sheet. When extracting metrics, verify calculation methodology is consistent. Flag and explain any variations.

---

### Pitfall 3: Missing Historical Data

**Mistake:** Unable to show trends because previous dashboards were not retained

**Fix:** Implement dashboard archival process - save each monthly dashboard with date suffix. Create historical metrics tracking sheet for continuity even if full dashboards are not available.

---

### Pitfall 4: Gap Duplication

**Mistake:** Same gap appears multiple times in consolidated register (e.g., "orphaned accounts" appears in both S1 and S5)

**Fix:** When consolidating gaps, identify duplicates that span assessments. Consolidate into single gap entry with notation of which assessments identified it. Avoid double-counting in gap metrics.

---

### Pitfall 5: Unrealistic Targets

**Mistake:** Setting KPI targets that are unachievable (e.g., 100% compliance for first assessment)

**Fix:** Set initial targets based on current capability, then establish improvement trajectory. Year 1 target might be 75%, Year 2 target 85%, Year 3 target 95%. Document target rationale.

---

### Pitfall 6: Evidence Not Accessible

**Mistake:** Evidence register references files that auditors cannot access (broken links, restricted folders)

**Fix:** Verify all evidence locations before dashboard approval. Test access from auditor perspective. Store evidence in accessible, organised folder structure with clear naming conventions.

---

### Pitfall 7: Ignoring Low-Scoring Domains

**Mistake:** Focusing executive summary on strengths while minimising weaknesses

**Fix:** Present balanced view - acknowledge strengths but ensure weaknesses are clearly communicated with remediation plans. Executives need accurate picture to support remediation resourcing.

---

### Pitfall 8: No Remediation Ownership

**Mistake:** Gaps identified but no owners assigned, resulting in no progress between assessments

**Fix:** Every gap MUST have an owner and due date. Track ownership changes. Escalate gaps with owners who consistently miss due dates. Report gap ownership coverage as dashboard metric.

---

### Pitfall 9: Dashboard Too Complex for Executives

**Mistake:** Dashboard contains excessive technical detail that obscures key messages

**Fix:** Executive Summary (Sheet 2) should be understandable by non-technical executives in 5 minutes. Use RAG (Red/Amber/Green) status consistently. Reserve technical detail for supporting sheets.

---

### Pitfall 10: Certification Readiness Overly Optimistic

**Mistake:** Marking organisation as "Ready" for audit when significant gaps remain

**Fix:** Be conservative in readiness assessment. If ANY critical gaps remain open, status is "Not Ready". If evidence is incomplete for ANY control, status is "Not Ready". Auditors will find gaps; better to find them first.

---

### Pitfall 11: Inconsistent RAG Status Thresholds

**Mistake:** Different thresholds for Red/Amber/Green across different sheets

**Fix:** Document RAG thresholds in Instructions sheet and apply consistently:
- Green (Compliant): >= 85% or meets target
- Amber (Warning): 60-84% or within 10% of target
- Red (Non-Compliant): < 60% or more than 10% below target

---

### Pitfall 12: No Approval Trail

**Mistake:** Dashboard distributed without formal approval, questions arise about accuracy

**Fix:** Always complete three-level approval before distribution. Archive approved version with approval sheet visible. Reference approval in distribution communications.

---

### Pitfall 13: Metrics Without Context

**Mistake:** Presenting metrics (e.g., "85% compliance") without explaining what this means

**Fix:** For each metric, provide context: What does 85% mean? Is this good or bad relative to target? What would 100% require? What is the trend? Context enables decision-making.

---

### Pitfall 14: Trend Analysis Without Baseline

**Mistake:** Claiming "improvement" without documented baseline to compare against

**Fix:** First dashboard establishes baseline. Document baseline prominently. All subsequent dashboards compare against baseline AND previous period. No baseline = no trend claims.

---

### Pitfall 15: Ignoring Contractor/External User Metrics

**Mistake:** Dashboard focuses on employees, underrepresenting contractor/vendor access risks

**Fix:** Include contractor metrics explicitly: contractor count, expiration compliance, sponsor accountability. Contractors often pose higher risk due to temporary relationships and external employer loyalty.

---

### Pitfall 16: Dashboard as Point-in-Time Only

**Mistake:** Dashboard treated as snapshot without continuous improvement tracking

**Fix:** Dashboard should drive action. Include remediation progress tracking. Measure gap closure rate. Report on improvement initiatives. Static dashboard = compliance theatre.

---

## Quality Checklist

Before submitting for approval, verify:

### Prerequisites

- [ ] All S1-S5 assessments completed and approved
- [ ] All S1-S5 assessments current (within 30 days)
- [ ] Source assessment workbooks accessible
- [ ] Historical dashboards available (if this is not the first dashboard)
- [ ] Evidence folder structure created

### Executive Summary (Sheet 2)

- [ ] Composite score calculated correctly (verify formula)
- [ ] Maturity level assignment accurate for score
- [ ] Key findings reflect actual assessment data
- [ ] Strengths AND weaknesses documented
- [ ] Recommendations prioritised by risk
- [ ] Executive summary understandable by non-technical readers

### Domain Compliance Scores (Sheet 3)

- [ ] All five domains (S1-S5) documented
- [ ] Individual scores match source assessments exactly
- [ ] Targets documented and justified
- [ ] Status (RAG) assignments correct for scores
- [ ] Trends documented (if historical data available)
- [ ] Key findings summarised for each domain

### Consolidated Gap Register (Sheet 4)

- [ ] All gaps from S1-S5 included
- [ ] No duplicate gaps
- [ ] Risk levels assigned consistently
- [ ] All gaps have owners
- [ ] All gaps have due dates
- [ ] Status updated for previously identified gaps
- [ ] Gap metrics calculated correctly

### KPI Dashboard (Sheet 5)

- [ ] All KPIs populated
- [ ] Targets reflect organisational policy/risk tolerance
- [ ] Actuals match source assessments
- [ ] Status (RAG) assignments accurate
- [ ] Source assessment documented for each KPI
- [ ] Trend indicators correct (if historical data available)

### Evidence Summary (Sheet 6)

- [ ] All evidence from S1-S5 included
- [ ] Evidence locations verified and accessible
- [ ] Completeness assessments accurate (Complete, Partial, Missing)
- [ ] ISO 27001 requirement mapping correct
- [ ] Evidence summary metrics calculated
- [ ] Evidence ready for auditor access

### Trend Analysis (Sheet 7) - If Applicable

- [ ] Historical data accurate
- [ ] Trend calculations correct
- [ ] Trajectory projections realistic
- [ ] Improvement initiatives documented

### Certification Readiness (Sheet 8)

- [ ] All relevant ISO 27001 controls assessed
- [ ] Evidence status reflects actual availability
- [ ] Gap status reflects current state
- [ ] Readiness determination conservative (when in doubt, "Not Ready")
- [ ] Audit blockers clearly identified
- [ ] Remediation timeline realistic for certification date

### Approval (Sheet 9)

- [ ] Self-review completed
- [ ] Security Manager review completed
- [ ] CISO approval obtained
- [ ] All review comments addressed
- [ ] Approved version archived with date

### General Quality

- [ ] All data from current period (not stale)
- [ ] Calculations verified (spot check)
- [ ] Conditional formatting displays correctly
- [ ] File naming follows standard (ISMS-IMP-A.5.15-16-18.S6_IAM_Dashboard_YYYYMMDD.xlsx)
- [ ] Source S1-S5 workbooks archived with dashboard

---

## Review & Approval

### Review Process

**Step 1: Self-Review** (Dashboard Creator)

- **Focus:** Completeness, accuracy, data quality
- **Time:** 1-2 hours
- **Turnaround:** Same day

**Step 2: Security Manager Review**

- **Focus:** Compliance posture accuracy, gap prioritisation, remediation adequacy
- **Review Criteria:**
  - Do metrics accurately reflect source assessments?
  - Is gap prioritisation appropriate for risk?
  - Are remediation plans realistic?
  - Is certification readiness assessment accurate?
- **Decision:** Approve / Request Changes
- **Time:** 2-3 hours
- **Turnaround:** 2-3 business days

**Step 3: CISO Approval**

- **Focus:** Executive summary accuracy, governance readiness, risk acceptance
- **Review Criteria:**
  - Is executive summary accurate and balanced?
  - Are key risks clearly communicated?
  - Is certification readiness determination appropriate?
  - Any risk acceptance required for outstanding gaps?
- **Decision:** Final Approval / Approve with Conditions / Reject
- **Time:** 1-2 hours
- **Turnaround:** 2-3 business days

### Approval Timeline

```
Day 1:       Dashboard completed, self-review, submitted to Security Manager
Day 2-4:     Security Manager review
Day 5:       Security Manager approval (or changes requested)
Day 6-8:     CISO review
Day 9:       CISO final approval
Day 10:      Dashboard distributed to stakeholders
```

**Total timeline:** ~2 weeks from start to distribution

---

## Integration with Other Assessments

This dashboard (S6) consolidates data from:

### S1 - User Inventory & Lifecycle Assessment

- **Uses:** User counts, lifecycle compliance rates, orphaned accounts
- **Metrics:** Total users, provisioning SLA, deprovisioning SLA
- **Frequency:** Monthly data refresh

### S2 - Access Rights Matrix Assessment

- **Uses:** Access documentation scores, privileged access counts
- **Metrics:** Documentation completeness, excessive access
- **Frequency:** Monthly data refresh

### S3 - Access Review Results Assessment

- **Uses:** Review completion rates, attestation status
- **Metrics:** Reviews completed, findings count
- **Frequency:** Quarterly data refresh (aligned with review cycle)

### S4 - Role Definition & SoD Compliance Assessment

- **Uses:** RBAC adoption, SoD violation counts
- **Metrics:** RBAC coverage, open SoD violations
- **Frequency:** Quarterly data refresh

### S5 - Lifecycle Compliance Detailed Assessment

- **Uses:** Detailed JML event compliance, HR integration status
- **Metrics:** Joiner/mover/leaver SLA compliance, contractor expiration
- **Frequency:** Monthly data refresh

---

## Continuous Improvement

### Monthly Dashboard Refresh

1. **Verify S1-S5 assessments current** (refresh if stale)
2. **Extract updated metrics** from each assessment
3. **Update composite score** and domain scores
4. **Update gap register** (close completed gaps, add new gaps)
5. **Update KPI dashboard** with current period actuals
6. **Update evidence register** with new evidence
7. **Calculate trends** (month-over-month)
8. **Obtain approval** and distribute

**Time Commitment:** 2-4 hours per month

### Quarterly Executive Report

1. **Complete monthly refresh** (above)
2. **Prepare trend analysis** (quarter-over-quarter)
3. **Summarise remediation progress** (gaps closed, initiatives completed)
4. **Update certification readiness** assessment
5. **Prepare executive presentation** (5-10 slides)
6. **Present to executive leadership/audit committee**

**Time Commitment:** 4-6 hours per quarter

### Annual Comprehensive Review

1. **Complete all S1-S5 assessments** from scratch
2. **Build annual dashboard** with full year trend analysis
3. **Assess maturity progression** (baseline → current)
4. **Document lessons learned** and improvement opportunities
5. **Set next year targets** and improvement roadmap
6. **Present to board/audit committee**

**Time Commitment:** 20-30 hours annually (across all assessments)

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
