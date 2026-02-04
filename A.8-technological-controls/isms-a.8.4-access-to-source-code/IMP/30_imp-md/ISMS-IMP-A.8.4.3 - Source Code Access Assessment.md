**ISMS-IMP-A.8.4.3 - Source Code Security Compliance Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.4: Access to Source Code

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.4.3 |
| **Version** | 1.0 |
| **Assessment Area** | Source Code Security Compliance Dashboard (Aggregated) |
| **Related Policy** | ISMS-POL-A.8.4, Section 4 (Assessment and Evidence Framework) |
| **Purpose** | Aggregate data from IMP-S1 (Access Control) and IMP-S2 (Branch Protection) into comprehensive executive dashboard showing overall source code security posture |
| **Target Audience** | CISO, CTO/VP Engineering, Information Security Manager, Auditors, Executive Leadership |
| **Assessment Type** | Aggregated Dashboard & Executive Reporting |
| **Review Cycle** | Quarterly (with monthly KPI updates) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Source Code Security Compliance Dashboard | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE** (THIS PART)
  - Assessment Overview
  - Prerequisites
  - Dashboard Workflow
  - Completing Each Sheet
  - Data Integration from IMP-S1 and IMP-S2
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION** (SEPARATE FILE)
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formula Specifications for Aggregation
  - Cell Styling Reference

**Target Audiences:**

- **Part I:** Dashboard users (CISO, Security Manager, Auditors)
- **Part II:** Workbook developers (Python/Excel script maintainers)

---

# PART I: USER COMPLETION GUIDE

**Audience:** CISO, CTO/VP Engineering, Information Security Manager, Auditors

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.4.3 - Source Code Security Compliance Dashboard

#### What This Assessment Covers

This dashboard AGGREGATES data from two detailed assessments to provide executive visibility:

**Data Sources:**
1. **IMP-S1**: Repository Access Control Assessment

   - Repository inventory
   - User access permissions
   - Access reviews
   - Deprovisioning
   - Orphaned accounts

2. **IMP-S2**: Branch Protection Assessment

   - Branch protection rules
   - Pull request enforcement
   - Status checks
   - Signed commits
   - Exceptions

**Dashboard Outputs:**

- **Overall Compliance Score** (0-100%)
- **KPI Summary** (4 main areas)
- **Trend Analysis** (quarterly improvement tracking)
- **Gap Priority Matrix** (critical → low priority)
- **Action Items** (prioritized remediation tasks)
- **Executive Summary** (1-page view for leadership)

#### Key Principle

This dashboard is **NOT a new assessment** - it's an AGGREGATOR. You don't collect new data here. You IMPORT data from IMP-S1 and IMP-S2 workbooks and calculate overall compliance.

**This is NOT about:**

- Conducting new access reviews (done in IMP-S1)
- Configuring branch protection (done in IMP-S2)
- Collecting new evidence (comes from S1 and S2)

**This IS about:**

- Synthesizing S1 and S2 results
- Calculating overall compliance
- Identifying cross-cutting gaps
- Prioritizing remediation
- Executive reporting

#### What You'll Document

- **Executive Summary**: Overall compliance score, KPI dashboard, critical findings
- **Repository Overview**: Consolidated repository status across all metrics
- **Access Control Metrics**: Aggregated from IMP-S1
- **Branch Protection Metrics**: Aggregated from IMP-S2
- **Trend Analysis**: Quarterly score progression
- **Gap Priority Matrix**: All gaps ranked by severity
- **Action Items**: Remediation tasks with owners and dates
- **Evidence Summary**: Audit readiness checklist
- **Approval Sign-Off**: CISO certification

#### How This Relates to Other A.8.4 Assessments

| Assessment            | Focus                    | Relationship to A.8.4.3             |
|-----------------------|--------------------------|--------------------------------------|
| ISMS-IMP-A.8.4.1     | Access Control           | **DATA SOURCE** for access metrics   |
| ISMS-IMP-A.8.4.2     | Branch Protection        | **DATA SOURCE** for protection metrics |
| **ISMS-IMP-A.8.4.3** | **Compliance Dashboard** | **AGGREGATES S1 + S2** for executive view |

**Workflow:**
1. Complete IMP-S1 (Repository Access) → generates access compliance data
2. Complete IMP-S2 (Branch Protection) → generates protection compliance data
3. **Import S1 + S2 data into IMP-S3** → calculate overall compliance score
4. Present S3 dashboard to CISO/executive leadership

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Information Security Manager** - Owns dashboard compilation
2. **CISO** - Reviews and approves final dashboard
3. **CTO/VP Engineering** - Reviews for resource allocation decisions
4. **Compliance Team** - Uses for audit preparation
5. **Auditors** - Reviews during ISO 27001 certification

#### Required Skills

- Understanding of source code security concepts
- Ability to aggregate data from multiple workbooks
- Excel proficiency (formulas, pivot tables, charts)
- Executive communication skills
- Risk prioritization judgment

#### Time Commitment

- **Initial setup:** 4-6 hours (first time, configure formulas)
- **Quarterly updates:** 2-3 hours (import S1/S2 data, review results)
- **Monthly KPI refresh:** 1 hour (update trends)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Executive dashboard** - 1-page compliance summary
2. ✅ **Overall compliance score** - Weighted average (0-100%)
3. ✅ **KPI metrics** - 4 main scores with targets
4. ✅ **Repository overview** - Consolidated repository status
5. ✅ **Trend analysis** - 12-month compliance progression
6. ✅ **Gap priority matrix** - Critical → low priority gaps
7. ✅ **Action items** - Remediation tasks with owners
8. ✅ **Evidence summary** - Audit readiness checklist
9. ✅ **Executive report** - 1-page summary for leadership
10. ✅ **CISO sign-off** - Final approval certification

---

## Prerequisites

### Information You'll Need

Before starting this dashboard, ensure you have:

#### 1. Completed Assessments

- ✅ **IMP-S1 completed** - Repository Access Control Assessment
  - File: `ISMS-IMP-A.8.4.1_Repository_Access_YYYYMMDD.xlsx`
  - Status: Approved by CISO
  - Contains: Repository inventory, user access matrix, access reviews, deprovisioning logs

- ✅ **IMP-S2 completed** - Branch Protection Assessment
  - File: `ISMS-IMP-A.8.4.2_Branch_Protection_YYYYMMDD.xlsx`
  - Status: Approved by CISO
  - Contains: Branch inventory, protection details, PR configuration, status checks

**CRITICAL:** S1 and S2 must be COMPLETED and APPROVED before starting S3. This dashboard aggregates their data.

#### 2. Historical Data (for trend analysis)

- **Previous quarter dashboards** (if available)
- **12-month compliance score history** (if available)
- **Remediation completion records**

#### 3. Organizational Information

- **Executive priorities** (what matters most to CISO/CTO)
- **Upcoming audits** (audit readiness requirements)
- **Budget/resource constraints** (for remediation prioritization)

### Tools You'll Use

- **Excel or compatible spreadsheet application**
- **Previous quarter S1 and S2 workbooks** (for trend analysis)
- **Presentation software** (PowerPoint/Google Slides - for executive summary)

### Skills Assessment

**Before you begin, ensure you can:**

- [ ] Access completed S1 and S2 workbooks
- [ ] Extract compliance scores from S1 and S2
- [ ] Calculate weighted averages
- [ ] Create executive summaries
- [ ] Prioritize gaps by severity

**If you answered NO to any item**, get help from:

- Information Security Manager (for score interpretation)
- Excel support (for formula assistance)
- CISO office (for prioritization guidance)

---

## Dashboard Workflow

### Overview of Process

```
Step 1: Import S1 Data (Access Control)
  ↓
Step 2: Import S2 Data (Branch Protection)
  ↓
Step 3: Calculate Overall Compliance Score
  ↓
Step 4: Generate Repository Overview
  ↓
Step 5: Create Trend Analysis
  ↓
Step 6: Build Gap Priority Matrix
  ↓
Step 7: Compile Action Items
  ↓
Step 8: Assess Audit Readiness
  ↓
Step 9: Generate Executive Summary
  ↓
Step 10: Obtain CISO Approval
```

### Detailed Workflow

#### Step 1: Import S1 Data - Access Control (30 minutes)

**What to do:**
1. Open completed `ISMS-IMP-A.8.4.1_Repository_Access_[Date].xlsx`
2. Navigate to Sheet: Compliance_Scoring
3. Extract key metrics:

   - Repository Inventory Completeness (target: 100%)
   - Access Control Compliance (target: 100%)
   - Appropriate Access Rate (target: ≥95%)
   - Orphaned Account Rate (target: 0%)
   - Access Review Completion (target: 100%)
   - Deprovisioning SLA Compliance (target: ≥95%)
   - **Overall Repository Access Score** (target: ≥85%)

4. Copy to IMP-S3 Sheet: Access_Control_Metrics

**Outputs:**

- Repository Access Score (0-100%)
- 6 component metrics
- Compliance status (✅/⚠️/❌)

#### Step 2: Import S2 Data - Branch Protection (30 minutes)

**What to do:**
1. Open completed `ISMS-IMP-A.8.4.2_Branch_Protection_[Date].xlsx`
2. Navigate to Sheet: Compliance_Scoring
3. Extract key metrics:

   - Branch Protection Configuration Rate (target: 100%)
   - Pull Request Enforcement Rate (target: ≥95%)
   - Status Check Compliance Rate (target: 100%)
   - Signed Commit Adoption Rate (target: ≥80%)
   - **Overall Branch Protection Score** (target: ≥85%)

4. Copy to IMP-S3 Sheet: Branch_Protection_Metrics

**Outputs:**

- Branch Protection Score (0-100%)
- 4 component metrics
- Compliance status (✅/⚠️/❌)

#### Step 3: Calculate Overall Compliance Score (automated)

**What happens:**
Dashboard automatically calculates:

```
Overall Source Code Security Score =
  (Repository Access Score × 50%) +
  (Branch Protection Score × 50%)

Target: ≥85%
```

**Weighted Components:**

- **Repository Access** (50%):
  - Inventory completeness
  - Access control
  - Appropriate access
  - Reviews
  - Deprovisioning
  
- **Branch Protection** (50%):
  - Protection configuration
  - PR enforcement
  - Status checks
  - Signed commits

**What you do:**

- Review calculated score
- Understand drivers (which component is low?)
- Assess risk level (🟢 Green ≥85%, 🟡 Yellow 70-84%, 🔴 Red <70%)

#### Step 4: Generate Repository Overview (1 hour)

**What to do:**
1. Consolidate repository data from S1 and S2
2. For each repository, document:

   - Repository name
   - Platform (GitHub, GitLab, etc.)
   - Classification (Production, Internal Tools, etc.)
   - Access control status (from S1)
   - Branch protection status (from S2)
   - Overall security score (average of S1 + S2)

3. Create summary statistics:

   - Repositories by platform
   - Repositories by classification
   - Compliant repositories (%)
   - Non-compliant repositories (count)

**Outputs:**

- Repository_Overview sheet populated
- Summary statistics calculated
- Visual dashboard (chart showing compliance by classification)

#### Step 5: Create Trend Analysis (30 minutes)

**What to do:**
1. Retrieve previous quarter scores (if available)
2. Plot 12-month trend:

   - Overall Compliance Score
   - Repository Access Score
   - Branch Protection Score

3. Calculate quarter-over-quarter change:

   - **Improving** ↗: Score increased ≥5%
   - **Stable** →: Score change within ±5%
   - **Declining** ↘: Score decreased ≥5%

4. Document in Sheet: Trend_Analysis

**Outputs:**

- 12-month score history
- Trend direction (↗/→/↘)
- Improvement/decline analysis

#### Step 6: Build Gap Priority Matrix (1 hour)

**What to do:**
1. Extract all gaps from S1 Gap_Analysis sheet
2. Extract all gaps from S2 Gap_Analysis sheet
3. Consolidate and re-prioritize:

   - 🔴 **Critical**: Production access control failures, no branch protection
   - 🟠 **High**: Internal tools non-compliance, missing status checks
   - 🟡 **Medium**: Partial compliance, missing documentation
   - 🟢 **Low**: Optimization opportunities

4. Rank by:

   - Risk level
   - Number of repositories affected
   - Remediation effort

5. Document in Sheet: Gap_Priority_Matrix

**Critical Gaps** (🔴 - immediate action required):

- Former employees with production repository access
- Production repositories with no branch protection
- No code review enforcement (0 required approvals)
- Critical secrets exposed in code

**High Gaps** (🟠 - remediate within 30 days):

- Access reviews >90 days overdue
- Branch protection partial (missing status checks)
- Service accounts not documented
- Contractor access without end dates

**Medium Gaps** (🟡 - remediate within 90 days):

- Missing access justifications
- Stale approval dismissal not configured
- Signed commit adoption <80%
- Internal tools without protection

**Low Gaps** (🟢 - continuous improvement):

- Optimization of access request workflow
- Enhanced monitoring
- Additional CI/CD checks
- Documentation improvements

#### Step 7: Compile Action Items (30 minutes)

**What to do:**
1. For each gap, create action item:

   - Action ID (ACT-001, ACT-002, etc.)
   - Description (what needs to be done)
   - Gap reference (which gap this addresses)
   - Responsible party (who will do it)
   - Target completion date
   - Status (🔴 Open, 🟡 In Progress, 🟢 Completed)
   - Days overdue (if past target date)

2. Sort by priority (Critical → Low)
3. Document in Sheet: Action_Items

**Action Item Examples:**

- ACT-001: Remove access for 3 former employees in production repos (Critical, IT Ops, 2026-02-01)
- ACT-002: Enable branch protection on backend-api repository (Critical, DevOps, 2026-02-05)
- ACT-003: Complete Q4 access review for 15 overdue repositories (High, Repository Owners, 2026-02-15)
- ACT-004: Configure CodeQL security checks on all production repos (High, Security Team, 2026-03-01)

#### Step 8: Assess Audit Readiness (30 minutes)

**What to do:**
1. Check evidence completeness:

   - S1 evidence register complete? (✅/❌)
   - S2 evidence register complete? (✅/❌)
   - Supporting screenshots collected? (✅/❌)
   - Approval sign-offs obtained? (✅/❌)

2. Calculate audit readiness score:

   - Documentation completeness (%)
   - Evidence availability (%)
   - Compliance score (%)
   - Gap remediation status (%)

3. Document in Sheet: Evidence_Summary

**Audit Readiness Criteria:**

- ✅ **Ready**: Overall score ≥85%, all critical gaps remediated, evidence complete
- ⚠️ **Needs Work**: Score 70-84%, some critical gaps remain, evidence mostly complete
- ❌ **Not Ready**: Score <70%, multiple critical gaps, evidence incomplete

#### Step 9: Generate Executive Summary (1 hour)

**What to do:**
1. Create 1-page executive summary in Sheet: Executive_Summary
2. Include:

   - **Overall Compliance Score** (large, prominent)
   - **Risk Level** (🟢/🟡/🔴 with explanation)
   - **Trend** (↗/→/↘ with quarter-over-quarter change)
   - **KPI Summary** (4 main scores in table)
   - **Critical Findings** (top 3-5 issues)
   - **Action Items** (top 5 by priority)
   - **Audit Readiness** (Ready/Needs Work/Not Ready)

3. Add visual elements:

   - Gauge chart showing overall score
   - Trend line chart (12 months)
   - Gap priority pie chart

**Executive Summary Template:**
```
SOURCE CODE SECURITY COMPLIANCE DASHBOARD
Assessment Period: Q4 2025
Assessment Date: 2025-12-31

┌─────────────────────────────────────────┐
│  OVERALL COMPLIANCE SCORE: 87%          │
│  Risk Level: 🟢 Low Risk (Target: ≥85%) │
│  Trend: ↗ Improving (+7% from Q3)       │
└─────────────────────────────────────────┘

KPI SUMMARY:
┌────────────────────────┬─────────┬────────┬────────┐
│ Metric                 │ Current │ Target │ Status │
├────────────────────────┼─────────┼────────┼────────┤
│ Repository Access      │   89%   │  ≥85%  │   ✅   │
│ Branch Protection      │   85%   │  ≥85%  │   ✅   │
└────────────────────────┴─────────┴────────┴────────┘

CRITICAL FINDINGS:
1. 2 former employees still have production access (Critical)
2. 5 production repositories missing branch protection (Critical)
3. 12 access reviews overdue >90 days (High)

TOP 5 ACTION ITEMS:
1. Remove terminated employee access (Due: 2026-02-01)
2. Enable branch protection on 5 repos (Due: 2026-02-05)
3. Complete overdue access reviews (Due: 2026-02-15)
4. Configure CodeQL on production repos (Due: 2026-03-01)
5. Update contractor end dates (Due: 2026-03-15)

AUDIT READINESS: ⚠️ Needs Work

- Overall score: ✅ 87% (target ≥85%)
- Critical gaps: ⚠️ 2 remain (target: 0)
- Evidence: ✅ Complete
- Recommendation: Remediate 2 critical gaps before audit

```

#### Step 10: Obtain CISO Approval (1-3 days elapsed)

**What to do:**
1. Present dashboard to Information Security Manager (review)
2. Address any feedback
3. Present to CISO for approval
4. If score <70% (High Risk):

   - CISO may require immediate remediation before approval
   - Weekly status meetings until score ≥70%

5. Once approved, file dashboard as official record
6. Schedule next quarterly assessment

---

## Completing Each Sheet

### Sheet 1: Executive_Summary

**Purpose:** 1-page view for CISO/executive leadership.

**What to include:**

- Overall Compliance Score (large, prominent number)
- Risk Level with visual indicator (🟢/🟡/🔴)
- Trend direction with chart (↗/→/↘)
- KPI Summary table (4 main scores)
- Critical findings (top 3-5)
- Action items (top 5 by priority)
- Audit readiness assessment

**Layout:**

- Row 1-5: Title, date, overall score (visual gauge)
- Row 7-12: KPI summary table
- Row 14-20: Critical findings (bullet list)
- Row 22-28: Top 5 action items (table)
- Row 30-35: Audit readiness summary

**Visual Elements:**

- Gauge chart for overall score (0-100%)
- Traffic light (🟢/🟡/🔴) for risk level
- Trend arrow (↗/→/↘)
- Small sparkline charts for KPIs

---

### Sheet 2: Repository_Overview

**Purpose:** Consolidated view of all repositories.

**Columns:**

- A: Repository Name
- B: Platform (GitHub, GitLab, etc.)
- C: Classification (Production, Internal Tools, etc.)
- D: Access Control Status (from S1 - ✅/⚠️/❌)
- E: Branch Protection Status (from S2 - ✅/⚠️/❌)
- F: Overall Security Score (average of access + protection)
- G: Status (✅ Compliant if both D and E are ✅)

**Summary Statistics** (below data):

- Total repositories
- Repositories by platform (GitHub: X, GitLab: Y, etc.)
- Repositories by classification (Production: X, Internal: Y, etc.)
- Compliant repositories (%)
- Non-compliant repositories (count)

---

### Sheet 3: Access_Control_Metrics

**Purpose:** Detailed access control metrics from IMP-S1.

**Data imported from S1:**

- Repository Inventory Completeness
- Access Control Compliance
- Appropriate Access Rate
- Orphaned Account Rate
- Access Review Completion
- Deprovisioning SLA Compliance
- Overall Repository Access Score

**Additional analysis:**

- Repositories with access control issues (list)
- Orphaned accounts by platform
- Overdue access reviews (count)
- Deprovisioning violations (count)

---

### Sheet 4: Branch_Protection_Metrics

**Purpose:** Detailed branch protection metrics from IMP-S2.

**Data imported from S2:**

- Branch Protection Configuration Rate
- Pull Request Enforcement Rate
- Status Check Compliance Rate
- Signed Commit Adoption Rate
- Overall Branch Protection Score

**Additional analysis:**

- Repositories without branch protection (list)
- Pull request bypasses (count)
- Missing status checks (by repository)
- Signed commit adoption by repository

---

### Sheet 5: Trend_Analysis

**Purpose:** Track compliance over time (12 months).

**Columns:**

- A: Quarter (Q1 2025, Q2 2025, etc.)
- B: Overall Compliance Score
- C: Repository Access Score
- D: Branch Protection Score
- E: Change from Previous Quarter (%)
- F: Trend Direction (↗/→/↘)

**Chart:**

- Line chart showing all 3 scores over 12 months
- Target line at 85%
- Annotations for significant events

---

### Sheet 6: Gap_Priority_Matrix

**Purpose:** All gaps ranked by severity.

**Columns:**

- A: Gap ID (from S1 or S2)
- B: Gap Description
- C: Source (S1 or S2)
- D: Risk Level (🔴/🟠/🟡/🟢)
- E: Repositories Affected (count)
- F: Remediation Effort (hours/days)
- G: Priority Score (calculated: risk × repos affected ÷ effort)
- H: Status (Open/In Progress/Completed)

**Sorted by:** Priority Score (highest to lowest)

---

### Sheet 7: Action_Items

**Purpose:** Remediation tasks with tracking.

**Columns:**

- A: Action ID
- B: Description
- C: Gap Reference (which gap)
- D: Responsible Party
- E: Target Completion Date
- F: Status (🔴 Open, 🟡 In Progress, 🟢 Completed)
- G: Days Overdue (if past target date)
- H: Notes

**Sorted by:** Priority (Critical → Low), then by Target Date

---

### Sheet 8: Evidence_Summary

**Purpose:** Audit readiness checklist.

**Sections:**

**1. Documentation Completeness:**

- [ ] ISMS-POL-A.8.4 (Policy) - approved and current
- [ ] ISMS-IMP-A.8.4.1 (Access Control) - completed
- [ ] ISMS-IMP-A.8.4.2 (Branch Protection) - completed
- [ ] ISMS-IMP-A.8.4.3 (Dashboard) - this document

**2. Evidence Availability:**

- [ ] S1 Evidence Register - complete
- [ ] S2 Evidence Register - complete
- [ ] Configuration screenshots - collected
- [ ] Access review records - archived
- [ ] Deprovisioning logs - retained

**3. Compliance Metrics:**

- [ ] Overall score ≥85%
- [ ] Critical gaps remediated
- [ ] High gaps in remediation
- [ ] Evidence organized for audit

**4. Audit Readiness Score:**
```
= (Documentation % + Evidence % + Compliance % + Gap Remediation %) / 4
```

---

### Sheet 9: Approval_Sign_Off

**Purpose:** CISO certification of dashboard.

**Sections:**

**Assessment Summary:**

- Assessment Period: Q4 2025
- Assessment Date: 2025-12-31
- Overall Compliance Score: [Link to Executive_Summary]
- Risk Level: [Link to Executive_Summary]
- Audit Readiness: [Link to Evidence_Summary]

**Dashboard Compiled By:**

- Name: [Information Security Manager]
- Date: [Completion date]

**Information Security Manager Review:**

- Name:
- Date:
- Review Notes:
- Recommendation: Approve / Approve with Conditions / Reject

**CISO Approval:**

- Name:
- Date:
- Decision: Approved / Approved with Conditions / Rejected
- Conditions (if any):
- Next Review Date: [Date + 90 days]

---

## Evidence Collection

**Evidence for S3 Dashboard:**

**Primary Evidence:**

- Completed S1 workbook (approved by CISO)
- Completed S2 workbook (approved by CISO)
- Previous quarter S3 dashboards (for trend analysis)

**Supporting Evidence:**

- S1 Evidence Register (repository access evidence)
- S2 Evidence Register (branch protection evidence)
- Gap remediation completion records
- Executive presentation slides (if presented to leadership)

**Evidence Naming:**
```
ISMS-IMP-A.8.4.3_Dashboard_Q4-2025.xlsx
ISMS-IMP-A.8.4.3_Executive_Summary_Q4-2025.pdf
ISMS-IMP-A.8.4.3_CISO_Presentation_Q4-2025.pptx
```

---

## Common Pitfalls

### Pitfall 1: Creating Dashboard Without Completing S1 and S2

**Problem:** Starting S3 before S1 and S2 are done.

**Why it fails:**

- S3 has no data to aggregate
- Scores are incomplete or estimated
- Dashboard shows inaccurate compliance

**How to avoid:**

- Complete S1 FIRST (Repository Access)
- Complete S2 SECOND (Branch Protection)
- Only then create S3 Dashboard
- Verify S1 and S2 have CISO approval

---

### Pitfall 2: Manual Data Entry (Not Using Formulas)

**Problem:** Copying scores manually instead of using formulas.

**Why it's bad:**

- Error-prone (typos, copy-paste mistakes)
- Not dynamic (doesn't update if S1/S2 change)
- Breaks traceability

**How to avoid:**

- Use Excel formulas to link to S1 and S2 workbooks
- Example: `='[ISMS-IMP-A.8.4.1_Repository_Access_20251231.xlsx]Compliance_Scoring'!B23`
- Dashboard auto-updates when S1/S2 change

---

### Pitfall 3: Focusing Only on Overall Score

**Problem:** Only looking at aggregate 87% score, ignoring components.

**Why it's insufficient:**

- High score can hide critical gaps in specific areas
- Example: 90% access control + 80% branch protection = 85% overall (looks good)
- But 80% branch protection might include "0% of production repos protected" (CRITICAL)

**How to avoid:**

- Review ALL component scores
- Identify which specific metric is low
- Read Gap_Priority_Matrix for details
- Don't declare victory based on aggregate score alone

---

### Pitfall 4: Not Tracking Trends

**Problem:** Only looking at current quarter, ignoring trend.

**Example:**

- Q3: 92% → Q4: 87% = **Declining** ↘ (even though 87% is "compliant")
- This indicates worsening, requires investigation

**How to avoid:**

- Always populate Trend_Analysis sheet
- Compare quarter-over-quarter
- Investigate declines (why did score drop?)
- Celebrate improvements (share wins)

---

### Pitfall 5: Gaps Without Action Items

**Problem:** Documenting 15 gaps, creating 3 action items.

**Reality:**

- Every gap needs remediation plan
- Every gap needs owner
- Every gap needs target date

**How to avoid:**

- 1 gap = 1 action item (minimum)
- Large gaps may need multiple action items
- Track progress on ALL gaps, not just critical

---

### Pitfall 6: Presenting Raw Data to Executives

**Problem:** Sending 50-page S1+S2 workbooks to CISO.

**Why it fails:**

- Executives need summary, not details
- CISO doesn't have time to read 50 pages
- Key points get lost in data

**How to succeed:**

- Create 1-page Executive_Summary sheet
- Present KEY findings only (top 3-5 issues)
- Use visuals (charts, traffic lights)
- Save details for backup slides

---

### Pitfall 7: Audit Readiness Assumption

**Problem:** Assuming "87% compliant = audit ready."

**Reality Check:**

- 87% overall score = GOOD
- But if 2 critical gaps remain = NOT audit ready
- Auditor samples 10 repos, finds 1 critical gap = audit finding

**How to avoid:**

- Remediate ALL critical gaps before audit
- Review Evidence_Summary checklist
- Conduct mock audit (spot-check repositories)
- Don't schedule audit with open critical gaps

---

### Pitfall 8: Stale Dashboard

**Problem:** Creating dashboard in January, not updating until April.

**Why it's bad:**

- Compliance status changes (new gaps appear)
- Score becomes outdated
- Dashboard loses credibility

**How to avoid:**

- Monthly KPI refresh (update key scores)
- Quarterly comprehensive update (full S1+S2 refresh)
- Continuous gap tracking (update Action_Items as remediated)

---

### Pitfall 9: No Executive Engagement

**Problem:** Creating dashboard, filing it, never presenting to CISO.

**Missed opportunity:**

- CISO doesn't know compliance status
- Gaps don't get prioritized
- Resources not allocated
- Remediation stalls

**How to succeed:**

- Schedule quarterly CISO review
- Present 1-page executive summary
- Discuss critical findings
- Request resources for remediation
- Get buy-in for action items

---

### Pitfall 10: Treating Dashboard as "Done"

**Problem:** Dashboard approved, filed, forgotten until next quarter.

**Reality:**

- Dashboard is START of remediation, not END
- Action items need tracking
- Gaps need closure
- Continuous monitoring required

**How to avoid:**

- Weekly action item status updates
- Monthly gap remediation reviews
- Continuous monitoring (don't wait for quarter)
- Celebrate wins (share gap closure)

---

## Quality Checklist

Before submitting dashboard for CISO approval:

### Data Integrity

- [ ] S1 workbook completed and approved
- [ ] S2 workbook completed and approved
- [ ] All scores imported correctly (formulas, not manual)
- [ ] Overall compliance score calculated correctly
- [ ] Trend analysis includes historical data
- [ ] Gap priority matrix includes ALL gaps from S1 and S2

### Completeness

- [ ] Executive_Summary sheet populated
- [ ] Repository_Overview sheet complete
- [ ] Access_Control_Metrics populated from S1
- [ ] Branch_Protection_Metrics populated from S2
- [ ] Trend_Analysis shows 12-month history
- [ ] Gap_Priority_Matrix ranks all gaps
- [ ] Action_Items created for all gaps
- [ ] Evidence_Summary checklist complete
- [ ] Approval_Sign_Off ready for signatures

### Accuracy

- [ ] Overall score matches calculation (spot-check)
- [ ] Component scores match S1 and S2 (verify)
- [ ] Repository counts consistent across sheets
- [ ] Gap counts match S1 + S2 gap totals
- [ ] Action item count ≥ gap count

### Executive Readiness

- [ ] 1-page executive summary created
- [ ] Visual elements included (charts, gauges)
- [ ] Critical findings highlighted (top 3-5)
- [ ] Action items prioritized
- [ ] Audit readiness assessed

### Presentation Quality

- [ ] Dashboard is visually clear
- [ ] Charts are readable
- [ ] Color coding consistent (🟢/🟡/🔴)
- [ ] No typos or formatting errors
- [ ] Professional appearance

---

## Review & Approval

**Submission Process:**

1. **Information Security Manager Review** (1-2 days)

   - Verify data accuracy
   - Review prioritization
   - Confirm evidence completeness

2. **CISO Presentation** (1 hour meeting)

   - Present 1-page executive summary
   - Discuss critical findings
   - Review action items
   - Request resource allocation
   - Obtain approval

3. **Post-Approval Actions**

   - File dashboard as official record
   - Communicate results to stakeholders
   - Initiate action item tracking
   - Schedule monthly reviews

**Approval Criteria:**

- Dashboard accurately reflects S1 and S2 data
- Gap prioritization is appropriate
- Action items have owners and dates
- Audit readiness assessed realistically
- Executive summary is clear and actionable

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Python/Excel Script Maintainers, Assessment Workbook Developers

---

## Instructions for Workbook Development

### Workbook Generation

**Primary Script:** `generate_a84_3_compliance_dashboard.py`

**Purpose:** Generate Excel workbook (`ISMS-IMP-A.8.4.3_Compliance_Dashboard_YYYYMMDD.xlsx`) that aggregates data from S1 (Repository Access) and S2 (Branch Protection) into executive dashboard.

**Key Functions:**

- `create_workbook()`: Initialize workbook and sheets
- `setup_styles()`: Cell styles, executive dashboard styling
- `create_executive_summary()`: 1-page dashboard with charts
- `import_s1_data()`: Link to S1 workbook compliance scores
- `import_s2_data()`: Link to S2 workbook compliance scores
- `calculate_overall_score()`: Aggregate S1 + S2 into overall compliance
- `create_trend_analysis()`: Historical score tracking
- `create_gap_matrix()`: Consolidated gap prioritization
- `create_action_items()`: Remediation task tracking

**File Naming:** `ISMS-IMP-A.8.4.3_Compliance_Dashboard_YYYYMMDD.xlsx`

**Critical Design Pattern:**
This workbook LINKS to S1 and S2 workbooks using Excel external references. Formulas reference:

- `[ISMS-IMP-A.8.4.1_Repository_Access_YYYYMMDD.xlsx]Compliance_Scoring`
- `[ISMS-IMP-A.8.4.2_Branch_Protection_YYYYMMDD.xlsx]Compliance_Scoring`

---

## Workbook Structure Overview

### Sheet List (11 Sheets Total)

| Sheet # | Sheet Name | Purpose | Rows | Columns | Entry Type |
|---------|------------|---------|------|---------|------------|
| 1 | Executive_Summary | 1-page dashboard | ~40 | A-F | Formula + Chart |
| 2 | Repository_Overview | Consolidated repo status | Variable | A-G | Linked data |
| 3 | Access_Control_Metrics | S1 detailed metrics | ~30 | A-D | Linked from S1 |
| 4 | Branch_Protection_Metrics | S2 detailed metrics | ~30 | A-D | Linked from S2 |
| 5 | Secret_Management_Metrics | Secret scanning & rotation | ~30 | A-D | Linked data |
| 6 | Third_Party_Access | External access summary | Variable | A-F | Aggregated |
| 7 | Trend_Analysis | 12-month history | 12 rows | A-F | Historical data |
| 8 | Gap_Priority_Matrix | Consolidated gaps | Variable | A-H | Aggregated |
| 9 | Action_Items | Remediation tracking | Variable | A-H | User input |
| 10 | Evidence_Summary | Audit readiness | ~30 | A-C | Checklist |
| 11 | Approval_Sign_Off | CISO certification | ~40 | A-B | User input |

---

## Sheet 1: Executive_Summary

### Purpose
1-page executive dashboard for CISO/leadership.

### Layout Structure

**Section 1: Header (Rows 1-5)**
```
Row 1: "SOURCE CODE SECURITY COMPLIANCE DASHBOARD"
Row 2: "Assessment Period: [Date]"
Row 3: [Blank]
Row 4: "OVERALL COMPLIANCE SCORE"
Row 5: [Large Score Display - Cell C5]
```

**Section 2: Risk Indicator (Rows 7-9)**
```
Row 7: "Risk Level:"
Row 8: [Traffic Light Display - Cell C8]
Row 9: "Trend: [Arrow] [+/- %]"
```

**Section 3: KPI Summary Table (Rows 11-16)**
```
| Metric                 | Current | Target | Status |
|------------------------|---------|--------|--------|
| Repository Access      | [Link]  | ≥85%   | [Icon] |
| Branch Protection      | [Link]  | ≥85%   | [Icon] |
```

**Section 4: Critical Findings (Rows 18-24)**
```
Row 18: "CRITICAL FINDINGS:"
Row 19-24: Bullet list of top 5 issues
```

**Section 5: Top Action Items (Rows 26-32)**
```
Row 26: "TOP 5 ACTION ITEMS:"
Row 27: [Table header]
Row 28-32: Top 5 actions from Action_Items sheet
```

**Section 6: Audit Readiness (Rows 34-37)**
```
Row 34: "AUDIT READINESS:"
Row 35: [Status indicator]
Row 36: [Readiness score]
Row 37: [Recommendation]
```

### Key Formulas

**Cell C5 (Overall Compliance Score):**
```excel
=(Access_Control_Metrics!B3 * 0.50) + (Branch_Protection_Metrics!B3 * 0.50)
```

**Cell C8 (Risk Level):**
```excel
=IF(C5>=85, "🟢 Low Risk",
    IF(C5>=70, "🟡 Medium Risk", "🔴 High Risk"))
```

**Cell C9 (Trend):**
```excel
=IF(Trend_Analysis!E12>5, "↗ Improving",
    IF(Trend_Analysis!E12<-5, "↘ Declining", "→ Stable"))
& " (" & TEXT(Trend_Analysis!E12, "+0%;-0%") & ")"
```

### Charts

**Chart 1: Overall Score Gauge (near Cell C5)**

- Type: Doughnut chart (gauge style)
- Data: Overall score vs. 100%
- Colors: Green (score), Gray (remaining)

**Chart 2: KPI Trend (Rows 11-16)**

- Type: Sparkline charts in Column E
- Data: Last 4 quarters for each KPI
- Shows trend direction visually

### Conditional Formatting

**Cell C5 (Overall Score):**

- ≥85%: Green fill, large font (18pt bold)
- 70-84%: Yellow fill, large font
- <70%: Red fill, large font

**Cell C8 (Risk Level):**

- 🟢 Low Risk: Green background
- 🟡 Medium Risk: Yellow background
- 🔴 High Risk: Red background

---

## Sheet 2: Repository_Overview

### Purpose
Consolidated view of all repositories with access + protection status.

### Column Definitions

| Col | Field Name | Width | Type | Formula/Link |
|-----|------------|-------|------|--------------|
| A | Repository Name | 30 | Linked | From S1 Repository_Inventory |
| B | Platform | 20 | Linked | From S1 Repository_Inventory |
| C | Classification | 20 | Linked | From S1 Repository_Inventory |
| D | Access Control Status | 18 | Linked | From S1 User_Access_Matrix analysis |
| E | Branch Protection Status | 20 | Linked | From S2 Branch_Protection_Details |
| F | Overall Security Score | 15 | Formula | =(D + E)/2 (if both numeric) |
| G | Status | 18 | Formula | =IF(AND(D="✅",E="✅"),"✅ Compliant","⚠️ Needs Work") |

### Summary Statistics (Below Data)

**Row N+5: Summary Section**
```
Total Repositories: [COUNT of Column A]
By Platform:

  - GitHub: [COUNTIF Platform = "GitHub"]
  - GitLab: [COUNTIF Platform = "GitLab"]
  - Bitbucket: [COUNTIF Platform = "Bitbucket"]

By Classification:

  - Production: [COUNTIF Classification = "🔴 Production"]
  - Internal Tools: [COUNTIF Classification = "🟡 Internal Tools"]

Compliance:

  - Compliant: [COUNTIF Status = "✅ Compliant"]
  - Non-Compliant: [COUNTIF Status != "✅ Compliant"]

```

### Linking Pattern

**To link from S1 (example for Repository Name):**
```excel
='[ISMS-IMP-A.8.4.1_Repository_Access_20251231.xlsx]Repository_Inventory'!$A4
```

**Important:** File path must be adjusted based on actual S1/S2 filenames.

---

## Sheet 3: Access_Control_Metrics

### Purpose
Import detailed access control metrics from S1 Compliance_Scoring sheet.

### Structure

**Row 3: Overall Repository Access Score**
```
Cell A3: "Overall Repository Access Score"
Cell B3: ='[S1_File.xlsx]Compliance_Scoring'!B23
Cell C3: "≥85%"
Cell D3: =IF(B3>=85,"✅ Compliant","❌ Non-Compliant")
```

**Row 5-10: Component Metrics**
```
Row 5: Repository Inventory Completeness
  B5: ='[S1_File.xlsx]Compliance_Scoring'!B5
  C5: "100%"
  D5: [Status formula]

Row 6: Access Control Compliance
  B6: ='[S1_File.xlsx]Compliance_Scoring'!B8
  
Row 7: Appropriate Access Rate
  B7: ='[S1_File.xlsx]Compliance_Scoring'!B11
  
Row 8: Orphaned Account Rate
  B8: ='[S1_File.xlsx]Compliance_Scoring'!B14
  
Row 9: Access Review Completion
  B9: ='[S1_File.xlsx]Compliance_Scoring'!B17
  
Row 10: Deprovisioning SLA Compliance
  B10: ='[S1_File.xlsx]Compliance_Scoring'!B20
```

**Row 13-20: Additional Analysis**
```
Row 13: Repositories with Access Issues
  B13: [Count from S1 data]

Row 15: Total Orphaned Accounts
  B15: [Count from S1 Deprovisioning_Log]

Row 17: Overdue Access Reviews
  B17: [Count from S1 Access_Review_Log]

Row 19: Deprovisioning Violations
  B19: [Count from S1 where timeline = "❌ No"]
```

### Conditional Formatting

**Column B (Current Values):**

- ≥Target: Green background
- <Target: Red background

**Column D (Status):**

- ✅ Compliant: Green background
- ❌ Non-Compliant: Red background

---

## Sheet 4: Branch_Protection_Metrics

### Purpose
Import detailed branch protection metrics from S2 Compliance_Scoring sheet.

### Structure

**Row 3: Overall Branch Protection Score**
```
Cell A3: "Overall Branch Protection Score"
Cell B3: ='[S2_File.xlsx]Compliance_Scoring'!B17
Cell C3: "≥85%"
Cell D3: =IF(B3>=85,"✅ Compliant","❌ Non-Compliant")
```

**Row 5-8: Component Metrics**
```
Row 5: Branch Protection Configuration Rate
  B5: ='[S2_File.xlsx]Compliance_Scoring'!B5

Row 6: Pull Request Enforcement Rate
  B6: ='[S2_File.xlsx]Compliance_Scoring'!B8

Row 7: Status Check Compliance Rate
  B7: ='[S2_File.xlsx]Compliance_Scoring'!B11

Row 8: Signed Commit Adoption Rate
  B8: ='[S2_File.xlsx]Compliance_Scoring'!B14
```

**Row 11-18: Additional Analysis**
```
Row 11: Repositories Without Branch Protection
  B11: [Count from S2 where Protection = "❌ No"]

Row 13: Pull Request Bypasses
  B13: [Count from S2 where PR Required = "❌ No"]

Row 15: Missing Status Checks
  B15: [Count from S2 where Status Checks = "❌ No"]

Row 17: Signed Commit Adoption
  B17: [Average from S2 Signed_Commits_Audit]
```

---

## Sheet 5: Trend_Analysis

### Purpose
Track compliance scores over time (12 months).

### Column Definitions

| Col | Field Name | Width | Type | Description |
|-----|------------|-------|------|-------------|
| A | Quarter | 15 | Text | Q1 2025, Q2 2025, etc. |
| B | Overall Score | 15 | Number | Historical overall compliance |
| C | Repository Access | 18 | Number | Historical S1 score |
| D | Branch Protection | 18 | Number | Historical S2 score |
| E | Change from Previous | 18 | Formula | =(B4-B3)/B3*100 |
| F | Trend Direction | 15 | Formula | =IF(E4>5,"↗",IF(E4<-5,"↘","→")) |

### Data Population

**Manual Entry for Historical Data:**

- Rows 4-15: Previous 12 quarters (oldest to newest)
- Current quarter data: Linked from Access_Control_Metrics and Branch_Protection_Metrics

**Current Quarter (Row 15 - example):**
```
Cell A15: "Q4 2025"
Cell B15: =Executive_Summary!C5
Cell C15: =Access_Control_Metrics!B3
Cell D15: =Branch_Protection_Metrics!B3
Cell E15: =(B15-B14)/B14*100
Cell F15: =IF(E15>5,"↗",IF(E15<-5,"↘","→"))
```

### Chart

**Line Chart (Below data, Rows 17-30)**

- X-axis: Quarter (Column A)
- Y-axis: Scores (Columns B, C, D)
- Series 1: Overall Score (blue line)
- Series 2: Repository Access (green line)
- Series 3: Branch Protection (orange line)
- Horizontal line at 85% (target)

---

## Sheet 6: Gap_Priority_Matrix

### Purpose
Consolidate all gaps from S1 and S2, ranked by priority.

### Column Definitions

| Col | Field Name | Width | Type | Description |
|-----|------------|-------|------|-------------|
| A | Gap ID | 15 | Text | GAP-001, GAP-002 (from S1/S2) |
| B | Gap Description | 40 | Text | From S1 or S2 Gap_Analysis |
| C | Source | 10 | Text | "S1" or "S2" |
| D | Risk Level | 15 | Dropdown | 🔴 Critical, 🟠 High, 🟡 Medium, 🟢 Low |
| E | Repos Affected | 12 | Number | Count of repositories |
| F | Remediation Effort | 18 | Text | Hours/days estimate |
| G | Priority Score | 12 | Formula | =(RISK_NUM*E)/EFFORT_NUM |
| H | Status | 18 | Dropdown | 🔴 Open, 🟡 In Progress, 🟢 Completed |

### Data Import

**From S1 Gap_Analysis:**
```
Import all rows where Status != "🟢 Completed"
Prefix Gap ID with "S1-" (e.g., S1-GAP-001)
Set Source = "S1"
```

**From S2 Gap_Analysis:**
```
Import all rows where Status != "🟢 Completed"
Prefix Gap ID with "S2-" (e.g., S2-GAP-001)
Set Source = "S2"
```

### Formulas

**Column G (Priority Score):**
```excel
=LET(
  risk_weight, SWITCH(D4, "🔴 Critical", 10, "🟠 High", 5, "🟡 Medium", 2, "🟢 Low", 1, 0),
  effort_days, SWITCH(F4, "1-2 hours", 0.25, "1 day", 1, "1 week", 5, "2-4 weeks", 15, ">1 month", 30, 1),
  (risk_weight * E4) / effort_days
)
```

Higher score = Higher priority (high risk × many repos ÷ low effort)

### Sorting

**Primary Sort:** Column D (Risk Level) - Critical → High → Medium → Low  
**Secondary Sort:** Column G (Priority Score) - Descending

### Conditional Formatting

**Column D (Risk Level):**

- 🔴 Critical: Red background
- 🟠 High: Orange background
- 🟡 Medium: Yellow background
- 🟢 Low: Green background

**Column H (Status):**

- 🔴 Open: Red background
- 🟡 In Progress: Yellow background
- 🟢 Completed: Green background

---

## Sheet 7: Action_Items

### Purpose
Track remediation tasks derived from gaps.

### Column Definitions

| Col | Field Name | Width | Type | Description |
|-----|------------|-------|------|-------------|
| A | Action ID | 15 | Text | ACT-001, ACT-002, etc. |
| B | Description | 40 | Text | What needs to be done |
| C | Gap Reference | 15 | Text | Which gap (from Sheet 6) |
| D | Responsible Party | 25 | Text | Who will do it |
| E | Target Date | 15 | Date | When it should be done |
| F | Status | 18 | Dropdown | 🔴 Open, 🟡 In Progress, 🟢 Completed |
| G | Days Overdue | 12 | Formula | =IF(F4<>"🟢 Completed",MAX(0,TODAY()-E4),"") |
| H | Notes | 30 | Text | Additional info |

### Formulas

**Column G (Days Overdue):**
```excel
=IF(F4="🟢 Completed", "",
   IF(E4<TODAY(), TODAY()-E4, ""))
```

Shows blank if completed or not yet due.

### Conditional Formatting

**Column E (Target Date):**
```
=AND(E4<TODAY(), F4<>"🟢 Completed")
Format: Red fill (overdue)
```

**Column G (Days Overdue):**

- >30 days: Red fill (critical delay)
- 15-30 days: Orange fill (attention needed)
- 1-14 days: Yellow fill (monitor)

### Sorting

**Primary Sort:** Column F (Status) - Open → In Progress → Completed  
**Secondary Sort:** Column E (Target Date) - Earliest first

---

## Sheet 8: Evidence_Summary

### Purpose
Audit readiness checklist.

### Structure

**Section 1: Documentation Completeness (Rows 4-10)**
```
Row 4: "DOCUMENTATION COMPLETENESS"
Row 6:  [✅/❌] ISMS-POL-A.8.4 (Policy) - approved
Row 7:  [✅/❌] ISMS-IMP-A.8.4.1 (Access) - completed
Row 8:  [✅/❌] ISMS-IMP-A.8.4.2 (Protection) - completed
Row 9:  [✅/❌] ISMS-IMP-A.8.4.3 (Dashboard) - this document
Row 10: Completeness Score: [COUNTIF(✅) / 4 * 100%]
```

**Section 2: Evidence Availability (Rows 12-18)**
```
Row 12: "EVIDENCE AVAILABILITY"
Row 14: [✅/❌] S1 Evidence Register - complete
Row 15: [✅/❌] S2 Evidence Register - complete
Row 16: [✅/❌] Configuration screenshots - collected
Row 17: [✅/❌] Evidence organized for audit
Row 18: Availability Score: [COUNTIF(✅) / 4 * 100%]
```

**Section 3: Compliance Metrics (Rows 20-26)**
```
Row 20: "COMPLIANCE METRICS"
Row 22: [✅/❌] Overall score ≥85%
Row 23: [✅/❌] Critical gaps remediated
Row 24: [✅/❌] High gaps in remediation
Row 25: [✅/❌] Evidence complete
Row 26: Compliance Score: [COUNTIF(✅) / 4 * 100%]
```

**Section 4: Overall Audit Readiness (Rows 28-32)**
```
Row 28: "OVERALL AUDIT READINESS"
Row 30: Readiness Score: [(Row 10 + Row 18 + Row 26) / 3]
Row 31: Status: [IF ≥85%, "✅ Ready", IF ≥70%, "⚠️ Needs Work", "❌ Not Ready"]
Row 32: Recommendation: [Text based on status]
```

### Formulas

**Cell C30 (Readiness Score):**
```excel
=(C10+C18+C26)/3
```

**Cell C31 (Status):**
```excel
=IF(C30>=85, "✅ Ready for Audit",
    IF(C30>=70, "⚠️ Needs Work", "❌ Not Ready"))
```

**Cell C32 (Recommendation):**
```excel
=IF(C31="✅ Ready for Audit", "Proceed with audit scheduling",
    IF(C31="⚠️ Needs Work", "Complete missing items before audit",
        "Significant remediation required"))
```

---

## Sheet 9: Approval_Sign_Off

### Purpose
CISO certification of dashboard.

### Structure

Same as IMP-S1 and IMP-S2 Approval sheets:

- Assessment Summary (with links to Executive_Summary)
- Dashboard Compiled By
- Information Security Manager Review
- CISO Approval
- Next Review Date (+90 days)

**Reference IMP-S1 PART II for detailed approval sheet specification.**

---

## Cell Styling Reference

### Executive Summary Styling

**Overall Score (Cell C5):**

- Font: Calibri 36pt bold
- Alignment: Center
- Border: Thick black box
- Fill: Conditional (green/yellow/red)

**Section Headers:**

- Font: Calibri 14pt bold
- Fill: #003366 (dark blue)
- Text: White

**KPI Table:**

- Header row: #4472C4 (medium blue), white text
- Data rows: Alternating white and light gray

### Standard Styling

**Headers:** Same as IMP-S1 and IMP-S2  
**Input Cells:** Light yellow (#FFFFCC)  
**Formula Cells:** Light blue (#E7F3FF)  
**Status Colors:** Green/Yellow/Red standard palette

---

## Integration Points

### External Workbook Links

**Critical:** This workbook depends on external links to S1 and S2 workbooks.

**Link Syntax:**
```excel
='[ISMS-IMP-A.8.4.1_Repository_Access_20251231.xlsx]Compliance_Scoring'!B23
='[ISMS-IMP-A.8.4.2_Branch_Protection_20251231.xlsx]Compliance_Scoring'!B17
```

**Link Management:**

- Links must be updated when S1/S2 filenames change
- Excel → Data → Edit Links → Update Source
- Or use VBA/Python to update links automatically

**For Python Script:**
```python
# Update external links programmatically
import openpyxl

wb = openpyxl.load_workbook('Dashboard.xlsx')
# Update external references
# Update sheet formulas with new S1/S2 filenames
```

---

## Quality Assurance

### Validation Script

**Script:** `excel_sanity_check_a84_3.py`

**Checks:**
1. All 9 sheets exist
2. External links to S1 and S2 workbooks exist
3. Overall score formula calculates correctly
4. Trend analysis has historical data
5. Gap matrix aggregates from S1 and S2
6. Charts render correctly
7. Conditional formatting applied

**Usage:**
```bash
python excel_sanity_check_a84_3.py ISMS-IMP-A.8.4.3_Compliance_Dashboard_20260125.xlsx \
  --s1-file ISMS-IMP-A.8.4.1_Repository_Access_20251231.xlsx \
  --s2-file ISMS-IMP-A.8.4.2_Branch_Protection_20251231.xlsx
```

---

## Version Control

**Filename:** `ISMS-IMP-A.8.4.3_Compliance_Dashboard_YYYYMMDD.xlsx`

**Quarterly Versioning:**

- Q1 2025: `_20250331.xlsx`
- Q2 2025: `_20250630.xlsx`
- Q3 2025: `_20250930.xlsx`
- Q4 2025: `_20251231.xlsx`

**Change Log:**

- v1.0: Initial dashboard structure (2026-01-25)

---

**END OF SPECIFICATION**

---

*"The strength of a cryptographic system is measured by its ability to resist the best known attacks."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-01-31 -->
