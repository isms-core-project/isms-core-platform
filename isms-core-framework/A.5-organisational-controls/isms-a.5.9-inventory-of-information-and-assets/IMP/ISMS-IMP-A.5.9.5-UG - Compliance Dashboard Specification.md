<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.9.5-UG:framework:UG:a.5.9.5 -->
**ISMS-IMP-A.5.9.5-UG - Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.5-UG |
| **Version** | 1.0 |
| **Assessment Area** | Executive Compliance Dashboard & Consolidated Metrics |
| **Related Policy** | ISMS-POL-A.5.9, Section 3 (Assessment Methodology), Requirement A.5.9-R9 (Reporting) |
| **Purpose** | Consolidate all A.5.9 assessment data into executive dashboard for management reporting and compliance tracking |
| **Target Audience** | CISO, Information Security Manager, Executive Management, Auditors, Board of Directors |
| **Assessment Type** | Consolidation & Executive Reporting |
| **Review Cycle** | Quarterly (after all 4 assessments completed) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial dashboard specification consolidating 4 assessment workbooks | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.9.5-TG.

---

**Audience:** CISO, Information Security Manager, Executive Management, Auditors

---

## Dashboard Overview

### What This Dashboard Consolidates

This dashboard is the **EXECUTIVE VIEW** of Control A.5.9 compliance. It consolidates data from **4 assessment workbooks**:

| Assessment | What It Measures | Key Metrics |
|------------|------------------|-------------|
| **IMP-A.5.9-1: Asset Discovery** | Do we know what assets exist? | Discovery completeness (5 domains), Gap counts, Coverage % |
| **IMP-A.5.9-2: Inventory Maintenance** | Is inventory kept current? | Update timeliness, Integration health, Data quality |
| **IMP-A.5.9-3: Quality & Compliance** | Is inventory data accurate? | Quality score (5 dimensions), Policy compliance |
| **IMP-A.5.9-4: Owner Accountability** | Are owners engaged? | Accountability score (4 dimensions), Attestation rate |

**Dashboard Output**: Single consolidated view showing:

- **Overall A.5.9 Compliance Score** (aggregated)
- **Traffic-light status** by assessment area
- **Trending** (quarter-over-quarter improvement)
- **Top priorities** for remediation
- **Executive summary** for Board/CISO

### Why This Matters

This dashboard fulfills:

- **ISO/IEC 27001:2022 Control A.5.9**: Management oversight of asset inventory
- **ISMS-POL-A.5.9, Requirement A.5.9-R9**: [Organization] SHALL report inventory metrics to management
- **Executive Reporting**: Single-page compliance status for CISO/Board
- **Audit Readiness**: Consolidated evidence of A.5.9 compliance
- **Continuous Improvement**: Trend analysis, gap prioritization

**From Implementer Perspective**: Provides clear priorities for improvement efforts.

**From Auditor Perspective**: Demonstrates systematic compliance monitoring and management oversight.

### Dashboard Philosophy

**"One Dashboard to Rule Them All"**

Instead of presenting 4 separate workbooks to management (overwhelming!), this dashboard:

- **Aggregates** key metrics from all 4 assessments
- **Simplifies** to traffic-light indicators (✅/⚠️/❌)
- **Prioritizes** remediation actions by impact
- **Trends** quarter-over-quarter to show improvement
- **Communicates** in business language, not technical jargon

**Dashboard Audience**:

- **Board of Directors**: One-page summary, overall compliance score
- **CISO**: Detailed metrics, remediation priorities
- **Audit Committee**: Compliance evidence, trend analysis
- **External Auditors**: Consolidated compliance proof

---

## Prerequisites

### What You Need Before Starting

**1. Completed Assessments** (ALL 4 REQUIRED):

- ✅ **IMP-A.5.9-1**: Asset Discovery assessment workbook
- ✅ **IMP-A.5.9-2**: Inventory Maintenance assessment workbook
- ✅ **IMP-A.5.9-3**: Quality & Compliance assessment workbook
- ✅ **IMP-A.5.9-4**: Owner Accountability assessment workbook

**CRITICAL**: All 4 assessments must be completed for the same quarter. Cannot consolidate Q1 discovery with Q2 maintenance!

**2. Access to Assessment Workbooks**:

- File paths to all 4 workbooks
- Read access to consolidated data sheets
- Previous quarter dashboard (if exists, for trending)

**3. Personnel**:

- **Information Security Manager**: Prepares dashboard, compiles metrics
- **CISO**: Reviews dashboard, approves presentation to Board
- **Executive Management**: Receives dashboard, approves remediation priorities
- **Auditors** (if applicable): Reviews dashboard for compliance verification

**4. Time Allocation**:

- **Dashboard Generation**: 2-4 hours (mostly automated via Python script)
- **Executive Summary Preparation**: 2-3 hours (narrative, priorities, trending analysis)
- **Management Review**: 1 hour
- **Total**: ~1 working day

---

## Dashboard Workflow

### Step-by-Step Process

```
Phase 1: Data Collection (Day 1 Morning)
├─ Verify all 4 assessment workbooks completed
├─ Check assessment dates (same quarter?)
├─ Export CSV from each assessment (metrics sheets)
└─ Validate data completeness

Phase 2: Dashboard Generation (Day 1 Afternoon)
├─ Run Python consolidation script
├─ Import CSV files from 4 assessments
├─ Auto-calculate aggregated metrics
├─ Generate traffic-light indicators
└─ Calculate quarter-over-quarter trends

Phase 3: Executive Summary (Day 1 End of Day)
├─ Write narrative summary (1-2 pages)
├─ Identify top 5 priorities
├─ Analyze trends vs. previous quarter
├─ Prepare recommendations
└─ Compile evidence links

Phase 4: Review & Approval (Day 2)
├─ Information Security Manager self-review
├─ CISO review and approval
├─ Prepare Board presentation (if quarterly Board meeting)
├─ Archive dashboard and assessments
└─ Plan Q+1 assessment cycle
```

**Timeline**: 1-2 working days (after all 4 assessments completed)

---

## Completing Each Sheet

### Sheet Structure (Aligned with Generator - 8 Sheets)

Per industry best practices for compliance dashboards (see [Hicomply](https://www.hicomply.com/hub/iso-27001-asset-register-how-to-build-your-asset-inventory), [isms.online](https://www.isms.online/nis-2/implementing-guidance/asset-management/12-4/)), this dashboard provides:
- **Single source of truth** for A.5.9 compliance posture
- **Real-time compliance monitoring** from 4 sub-assessments
- **Granular metrics** for operational tracking

| Sheet | Name | Purpose |
|-------|------|---------|
| 1 | Executive_Summary | Overall A.5.9 compliance score and executive overview |
| 2 | Compliance_Scorecard | Detailed scoring by assessment area |
| 3 | Discovery_Metrics | Metrics from A.5.9.1 Asset Discovery |
| 4 | Maintenance_Metrics | Metrics from A.5.9.2 Inventory Maintenance |
| 5 | Quality_Metrics | Metrics from A.5.9.3 Quality Compliance |
| 6 | Accountability_Metrics | Metrics from A.5.9.4 Owner Accountability |
| 7 | Trending_Analysis | Quarter-over-quarter trends |
| 8 | Action_Register | Remediation tracking |

---

### Sheet 1: Executive_Summary

**Purpose**: One-page overview for Board/CISO.

**What This Sheet Contains** (mostly auto-populated):

- Overall A.5.9 compliance score (single number!)
- Compliance status by assessment area (4 traffic lights)
- Top 5 priorities for remediation
- Quarter-over-quarter trend
- Key achievements and concerns

**Column Definitions**:

| Section | Content | How Populated |
|---------|---------|---------------|
| **Overall Compliance** | Single aggregated score (0-100%) | Auto-calculated from 4 assessments |
| **Assessment Breakdown** | 4 assessment areas with scores | Auto-imported from CSV exports |
| **Traffic Light Status** | ✅ / ⚠️ / ❌ per assessment | Auto-calculated based on thresholds |
| **Trend** | Improved / Stable / Degraded | Manual entry (compare to last quarter) |
| **Top Priorities** | 5 highest-impact remediation actions | Manual entry based on gap analysis |
| **Executive Narrative** | 2-3 paragraph summary | Manual entry by Information Security Manager |

**How to Complete**:

**Step 1: Review Auto-Populated Metrics**

The Python script auto-populates:

- Overall Compliance Score: Weighted average of 4 assessments
- Assessment scores: Imported from each workbook
- Traffic lights: Green (≥90%), Yellow (75-89%), Red (<75%)

**Step 2: Add Trend Analysis**

Compare to previous quarter:
```
Q4 2025 Overall Score: 86%
Q1 2026 Overall Score: 89%
Trend: Improved (+3%)
```

Document in "Trend vs. Last Quarter" section.

**Step 3: Identify Top 5 Priorities**

Review gap analysis from all 4 assessments, prioritize by:
1. **Impact**: Critical gaps > High > Medium > Low
2. **Effort**: Quick wins (low effort, high impact) first
3. **Policy Compliance**: SHALL requirements before SHOULD

**Example Top 5**:
1. **CRITICAL**: 24 information assets missing data classification (A.5.9-3, Completeness gap) - **Target: 30 days**
2. **HIGH**: Owner attestation rate 89% (target 95%) - 15 owners not responding (A.5.9-4) - **Target: 2 weeks**
3. **HIGH**: Currency compliance 92% for critical assets (target 100%) - 8% stale records (A.5.9-3) - **Target: 1 week**
4. **MEDIUM**: Procurement integration missing (A.5.9-2, Integration gap) - **Target: Q2 2026**
5. **MEDIUM**: Discovery completeness 94% for applications (target 95%) - Shadow IT detection needed (A.5.9-1) - **Target: Q2 2026**

**Step 4: Write Executive Narrative**

Template:
```
EXECUTIVE SUMMARY - CONTROL A.5.9 COMPLIANCE
Quarter: Q1 2026
Overall Compliance: 89% (⚠️ At Risk - Improvement Needed)

SUMMARY:
[Organization]'s asset inventory management achieved 89% compliance with ISO 27001:2022 
Control A.5.9 requirements in Q1 2026, an improvement of 3% from Q4 2025 (86%). While 
progress is being made, we have not yet reached the target of 95% compliance.

KEY ACHIEVEMENTS:

- Asset discovery completeness increased from 91% to 94% (+3%)
- Quality & Compliance score improved from 91% to 94% (+3%)
- Owner accountability initiatives launched (attestation campaign)

KEY CONCERNS:

- Data quality gaps: 24 information assets missing classification (CRITICAL)
- Owner engagement: 11% of owners not responding to attestation requests
- Maintenance: Procurement integration not yet implemented

REMEDIATION:
Top 5 priorities identified with assigned owners and target dates. Critical gaps 
(data classification) targeted for completion within 30 days. Management approval 
requested for remediation resource allocation.

TREND:
Positive trajectory. With focused remediation efforts on top 5 priorities, we 
project 95% compliance by Q2 2026.

RECOMMENDATION:
Approve top 5 remediation priorities and resource allocation. Schedule follow-up 
review in 60 days to assess progress.
```

---

### Sheet 3: Assessment Scorecard

**Purpose**: Detailed scores for each of the 4 assessments.

**What This Sheet Contains** (auto-populated):

- Discovery score and breakdown
- Maintenance score and breakdown
- Quality score and breakdown (5 dimensions)
- Accountability score and breakdown (4 dimensions)
- Weighting of each assessment toward overall score

**Column Definitions**:

| Column | Purpose | How Populated |
|--------|---------|---------------|
| **Assessment** | Assessment name | Fixed: Discovery / Maintenance / Quality / Accountability |
| **Weight** | Contribution to overall score | Fixed: 25% / 20% / 30% / 25% |
| **Target Score** | Policy requirement | Fixed: 95% / 95% / 97% / 94% |
| **Actual Score** | Current achievement | Auto-imported from CSV |
| **Gap vs. Target** | Shortfall | Auto-calculated |
| **Status** | Traffic light | Auto-calculated |
| **Sub-Metrics** | Breakdown (domains/dimensions) | Auto-imported from CSV |
| **Trend** | vs. Last Quarter | Manual entry |
| **Key Issues** | Main gaps | Manual summary |

**How to Complete**:

**Step 1: Verify Auto-Imported Scores**

Check that CSV imports completed successfully:

- Discovery: Overall completeness % (from A59_1_Discovery_Metrics.csv)
- Maintenance: Overall maintenance effectiveness (from A59_2_Maintenance_Metrics.csv)
- Quality: Overall quality score (from A59_3_Quality_Metrics.csv)
- Accountability: Overall accountability score (from A59_4_Accountability_Metrics.csv)

**Step 2: Add Trend Indicators**

For each assessment, compare to last quarter:
```
Discovery Q4 2025: 91%
Discovery Q1 2026: 94%
Trend: Improved (+3%)
```

**Step 3: Summarize Key Issues**

For each assessment with status ⚠️ or ❌, summarize main gaps:

**Discovery Key Issues**:

- "Application discovery 94% (target 95%) - shadow IT detection gaps"
- "Personnel asset discovery 100% ✅"

**Maintenance Key Issues**:

- "Update SLA compliance 89% (target 95%) - SaaS app onboarding delays"
- "Procurement integration missing"

**Quality Key Issues**:

- "Completeness dimension 94% (target 100%) - 24 assets missing classification"
- "Currency dimension 92% (target 100%) - 8% critical assets stale"

**Accountability Key Issues**:

- "Owner acknowledgment 89% (target 95%) - 15 owners not responding"
- "Owner performance 76% (target 80%) - 3 poor performers identified"

---

### Sheet 4: Trending Analysis

**Purpose**: Quarter-over-quarter trend visualization and analysis.

**What This Sheet Contains**:

- Historical scores (current + previous 3 quarters)
- Trend lines (improving/degrading)
- Rate of improvement
- Projection to target

**Column Definitions**:

| Column | Purpose | How Populated |
|--------|---------|---------------|
| **Quarter** | Time period | Fixed: Q4 2025, Q1 2026, Q2 2026, Q3 2026 |
| **Overall Score** | Aggregated compliance | Auto-calculated for current, manual for past |
| **Discovery Score** | Discovery assessment | Auto-imported (current), manual (past) |
| **Maintenance Score** | Maintenance assessment | Auto-imported (current), manual (past) |
| **Quality Score** | Quality assessment | Auto-imported (current), manual (past) |
| **Accountability Score** | Accountability assessment | Auto-imported (current), manual (past) |
| **Improvement Rate** | % change vs. previous quarter | Auto-calculated |
| **Projection** | Estimated next quarter score | Formula-based |

**How to Complete**:

**Step 1: Enter Historical Data**

Manually enter scores from previous quarters' dashboards:

| Quarter | Overall | Discovery | Maintenance | Quality | Accountability |
|---------|---------|-----------|-------------|---------|----------------|
| Q4 2025 | 86% | 91% | 85% | 91% | 80% |
| Q1 2026 | 89% | 94% | 88% | 94% | 84% |
| Q2 2026 | (projected) | (projected) | (projected) | (projected) | (projected) |
| Q3 2026 | (future) | (future) | (future) | (future) | (future) |

**Step 2: Review Auto-Calculated Trends**

Sheet auto-calculates:

- Improvement rate: (Q1 - Q4) / Q4 × 100% = (89-86)/86 = +3.5%
- Projection Q2: Q1 + (Q1 - Q4) = 89% + 3% = 92% (linear projection)

**Step 3: Add Narrative**

Document significant trends:

- "Consistent improvement across all 4 assessments (+3-4% each)"
- "Quality assessment showing fastest improvement (+3%)"
- "Accountability lagging (+4%) - needs focused attention"
- "At current rate, 95% target achievable by Q2 2026"

---

### Sheet 5: Gap Analysis & Remediation

**Purpose**: Consolidated view of ALL gaps across 4 assessments with prioritization.

**What This Sheet Contains**:

- All gaps from all 4 assessments
- Prioritized by severity × effort
- Assigned ownership for remediation
- Target completion dates
- Status tracking

**Column Definitions**:

| Column | Purpose | How Populated |
|--------|---------|---------------|
| **Gap ID** | Unique identifier | Format: GAP-NNN |
| **Source Assessment** | Which assessment identified gap | Discovery / Maintenance / Quality / Accountability |
| **Gap Description** | What's the gap | From assessment workbook |
| **Severity** | Impact | Critical / High / Medium / Low |
| **Effort** | Remediation effort | High / Medium / Low |
| **Priority** | Severity × Effort matrix | Auto-calculated |
| **Remediation Plan** | How to fix | From assessment workbook |
| **Responsible Party** | Who will fix | Assigned |
| **Target Date** | Completion deadline | From assessment workbook |
| **Status** | Current state | Dropdown: Not Started / In Progress / Complete / Blocked |
| **% Complete** | Progress | 0-100% |
| **Evidence** | Proof of remediation | Link to evidence |
| **Notes** | Additional context | Free text |

**How to Complete**:

**Step 1: Consolidate Gaps from All 4 Assessments**

Extract gaps from:

- **A59_1 (Discovery)**: Asset categories <95% completeness
- **A59_2 (Maintenance)**: Update procedures not documented, integrations missing
- **A59_3 (Quality)**: Mandatory attributes missing, consistency check failures
- **A59_4 (Accountability)**: Unowned assets, owners without attestation

**Step 2: Prioritize Using Severity × Effort Matrix**

| Severity → Effort ↓ | Critical | High | Medium | Low |
|---------------------|----------|------|--------|-----|
| **Low** | Priority 1 | Priority 2 | Priority 3 | Priority 5 |
| **Medium** | Priority 2 | Priority 3 | Priority 4 | Priority 6 |
| **High** | Priority 4 | Priority 5 | Priority 6 | Priority 7 |

**Priority 1-2**: Quick wins (high impact, low effort) - do these first!
**Priority 3-4**: Important but require effort - plan carefully
**Priority 5-7**: Nice to have - defer if resources limited

**Example Gap Entries**:

**GAP-001 (Priority 1 - Quick Win)**:

- **Source**: Quality (A59_3)
- **Description**: 24 information assets missing Data Classification
- **Severity**: Critical (policy SHALL requirement)
- **Effort**: Low (email owners, request classification)
- **Priority**: 1
- **Remediation**: "Email campaign to 24 asset owners, request classification within 2 weeks"
- **Responsible**: Information Security Manager
- **Target Date**: 05.02.2026 (2 weeks)
- **Status**: In Progress
- **% Complete**: 40% (10 of 24 owners responded)

**GAP-002 (Priority 2)**:

- **Source**: Accountability (A59_4)
- **Description**: 15 owners (11%) not responding to attestation requests
- **Severity**: High (ownership acknowledgment required)
- **Effort**: Low (send reminders, escalate to managers)
- **Priority**: 2
- **Remediation**: "Send 3rd reminder, escalate to department managers for non-responders"
- **Target Date**: 12.02.2026
- **Status**: In Progress

**GAP-015 (Priority 4 - Longer-term)**:

- **Source**: Maintenance (A59_2)
- **Description**: Procurement system integration missing
- **Severity**: Medium (improves automation but not critical)
- **Effort**: High (API development, testing, deployment)
- **Priority**: 4
- **Remediation**: "Develop API integration to SAP procurement, auto-create inventory records for capital asset purchases"
- **Responsible**: IT Integration Team
- **Target Date**: Q2 2026 (3 months)
- **Status**: Not Started

**Step 3: Track Progress**

Update status monthly:

- Not Started → In Progress: Work begins
- In Progress → % Complete: Track progress (25%, 50%, 75%)
- % Complete 100% → Complete: Verification evidence collected
- Blocked: Escalate to management (resource constraints, dependencies)

---

### Sheet 6: Compliance Evidence Matrix

**Purpose**: Map compliance to each policy SHALL requirement with evidence links.

**What This Sheet Contains**:

- All 9 SHALL requirements from ISMS-POL-A.5.9
- Evidence from 4 assessments supporting compliance
- Compliance status per requirement
- Audit-ready evidence trail

**Column Definitions**:

| Column | Purpose | How Populated |
|--------|---------|---------------|
| **Requirement ID** | Policy requirement code | Fixed: A.5.9-R1 through A.5.9-R9 |
| **Requirement Text** | SHALL statement | Fixed from policy |
| **Primary Evidence** | Which assessment verifies | Assessment name + sheet |
| **Compliance Status** | Met/Partially Met/Not Met | From assessment |
| **Compliance %** | If quantifiable | From assessment |
| **Supporting Evidence** | Additional proof | Links to evidence files |
| **Gap Description** | If not 100% | From assessment |
| **Remediation Plan** | How to close gap | From Gap Analysis sheet |
| **Target Date** | When to close | From Gap Analysis sheet |

**How to Complete**:

**Step 1: Map Requirements to Assessments**

| Requirement | Primary Assessment | Evidence Location |
|-------------|-------------------|-------------------|
| **R1**: Maintain inventory | Discovery (A59_1) | Sheet 2-6 (all domains documented) |
| **R2**: Categorize assets | Discovery (A59_1) | Sheet 2-6 (5 categories) |
| **R3**: Document mandatory attributes | Quality (A59_3) | Sheet 3 (Completeness Assessment) |
| **R4**: Assign ownership | Accountability (A59_4) | Sheet 2 (Ownership Coverage) |
| **R5**: Review and update on schedule | Maintenance (A59_2) | Sheet 3 (Update Triggers & Workflows) |
| **R6**: Integrate with other ISMS processes | Maintenance (A59_2) | Sheet 4 (Integration Architecture) |
| **R7**: Protect inventory with access controls | Maintenance (A59_2) | Sheet 2 (Inventory Structure, Access Controls) |
| **R8**: Conduct periodic quality assessments | Quality (A59_3) | This entire assessment! |
| **R9**: Report metrics to management | Dashboard (A59_5) | This dashboard! |

**Step 2: Document Compliance Status**

For each requirement:

- **100% compliant**: ✅ Met
- **90-99% compliant**: ⚠️ Partially Met (document gap)
- **<90% compliant**: ❌ Not Met (urgent remediation)

**Example**:

**Requirement A.5.9-R3**: Document mandatory attributes

- **Primary Evidence**: Quality Assessment (A59_3), Sheet 3 (Completeness)
- **Compliance Status**: ⚠️ Partially Met
- **Compliance %**: 94%
- **Supporting Evidence**: 
  - QUAL-010: Completeness query results
  - QUAL-031: Attribute population analysis
- **Gap Description**: "24 information assets (6%) missing Data Classification attribute"
- **Remediation Plan**: "GAP-001: Email campaign to owners, 2-week deadline"
- **Target Date**: 05.02.2026

---

### Sheet 7: Executive Presentation (One-Page)

**Purpose**: Printable one-page summary for Board presentation.

**What This Sheet Contains**:

- Single-page visual dashboard
- Charts: Overall score gauge, assessment breakdown, trend line
- Key numbers: Overall score, top 3 priorities, trend
- Designed for printing/PDF export

**Layout**:

```
┌────────────────────────────────────────────────────────────────┐
│  CONTROL A.5.9 - ASSET INVENTORY COMPLIANCE DASHBOARD         │
│  Quarter: Q1 2026              Date: 22.01.2026                │
└────────────────────────────────────────────────────────────────┘

┌─────────────────┐   ┌──────────────────────────────────────┐
│ OVERALL SCORE   │   │  ASSESSMENT BREAKDOWN                │
│                 │   │                                      │
│      89%        │   │  Discovery:        94%  ⚠️           │
│   ⚠️ At Risk    │   │  Maintenance:      88%  ⚠️           │
│                 │   │  Quality:          94%  ⚠️           │
│  Target: 95%    │   │  Accountability:   84%  ⚠️           │
│  Gap: -6%       │   │                                      │
└─────────────────┘   └──────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│  TREND (Last 4 Quarters)                                       │
│                                                                │
│  [Line chart showing Q4→Q1 improvement from 86% to 89%]       │
│                                                                │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│  TOP 3 PRIORITIES                                              │
│                                                                │
│  1. [CRITICAL] 24 assets missing classification (30 days)     │
│  2. [HIGH] Owner attestations - 15 non-responders (2 weeks)   │
│  3. [HIGH] 8% critical assets stale data (1 week)             │
│                                                                │
└────────────────────────────────────────────────────────────────┘

RECOMMENDATION: Approve remediation resource allocation. 
                95% compliance projected by Q2 2026.
```

This sheet is designed for:

- CISO to present to Board
- Printing as PDF for distribution
- Executive review in < 5 minutes

---

### Sheet 8: Evidence Register

**Purpose**: Consolidated evidence from all 4 assessments.

**Column Definitions**: Same as previous evidence registers, with:

- Evidence from all 4 assessment workbooks
- Dashboard-specific evidence (executive presentations, Board meeting minutes)

**Evidence ID format**: `DASH-NNN`

---

## Evidence Collection

### What Evidence to Collect

**From Assessment Workbooks**:

- All 4 completed assessment workbooks (.xlsx files)
- CSV exports from each assessment
- Evidence registers from each assessment

**Dashboard-Specific Evidence**:

- Generated dashboard workbook
- Executive summary (PDF)
- Board presentation slides (if created)
- Management approval of remediation priorities
- Board meeting minutes (showing dashboard presentation)

### Evidence Organization

```
/evidence/
├── 2026-Q1/
│   ├── assessments/
│   │   ├── ISMS_A_5_9_Asset_Discovery_Assessment_20260115.xlsx
│   │   ├── ISMS_A_5_9_Inventory_Maintenance_Assessment_20260118.xlsx
│   │   ├── ISMS_A_5_9_Quality_Compliance_Assessment_20260120.xlsx
│   │   └── ISMS_A_5_9_Owner_Accountability_Assessment_20260122.xlsx
│   ├── csv-exports/
│   │   ├── A59_1_Discovery_Metrics_20260115.csv
│   │   ├── A59_2_Maintenance_Metrics_20260118.csv
│   │   ├── A59_3_Quality_Metrics_20260120.csv
│   │   └── A59_4_Accountability_Metrics_20260122.csv
│   ├── dashboard/
│   │   ├── ISMS_A_5_9_Compliance_Dashboard_Q1_2026.xlsx
│   │   ├── Executive_Summary_Q1_2026.pdf
│   │   └── Board_Presentation_Q1_2026.pptx
│   └── approvals/
│       ├── CISO_Approval_Email_Q1_2026.pdf
│       └── Board_Meeting_Minutes_Q1_2026.pdf
└── 2026-Q2/
    └── [same structure]
```

---

## Common Pitfalls

### Pitfall 1: Consolidating Assessments from Different Quarters

**Problem**: Using Q1 discovery with Q2 maintenance data.

**Why It Fails**: Metrics not comparable, trend analysis invalid.

**Solution**: All 4 assessments must be from SAME quarter. If one assessment delayed, delay dashboard.

### Pitfall 2: No Trend Analysis

**Problem**: Only showing current quarter, no historical comparison.

**Why It Fails**: Can't demonstrate improvement, can't identify degrading areas.

**Solution**: Maintain historical dashboard data, trend at least 2-4 quarters.

### Pitfall 3: Too Much Detail for Executives

**Problem**: Presenting 100+ pages of assessment detail to Board.

**Why It Fails**: Information overload, executives lose interest.

**Solution**: Dashboard = Executive Summary (1 page) + detailed backup (for questions only).

### Pitfall 4: No Prioritization of Gaps

**Problem**: Listing 50 gaps without prioritization.

**Why It Fails**: Management doesn't know where to focus resources.

**Solution**: Priority matrix (severity × effort), identify top 3-5 priorities only.

### Pitfall 5: Dashboard Without Action

**Problem**: Presenting dashboard but not requesting management decisions.

**Why It Fails**: Dashboard becomes "FYI" document, no remediation happens.

**Solution**: Always include recommendations and request approvals (resource allocation, priority sign-off).

### Pitfall 6: One-Time Dashboard, Never Repeated

**Problem**: Creating dashboard once, never updating.

**Why It Fails**: Can't track improvement, compliance degrades over time.

**Solution**: Quarterly dashboard (minimum), aligned with assessment cycle.

### Pitfall 7: Not Celebrating Successes

**Problem**: Only focusing on gaps and problems.

**Why It Fails**: Team demotivated, "never good enough" feeling.

**Solution**: Highlight achievements, improved scores, closed gaps in executive summary.

---

## Quality Checklist

Before presenting dashboard, verify:

### Data Collection Checks

- [ ] All 4 assessment workbooks completed for same quarter
- [ ] CSV exports generated from each assessment
- [ ] CSV import into dashboard successful (no errors)
- [ ] All scores auto-calculated correctly
- [ ] Previous quarter data entered for trending

### Calculation Checks

- [ ] Overall compliance score = weighted average of 4 assessments
- [ ] Traffic light logic correct (Green ≥90%, Yellow 75-89%, Red <75%)
- [ ] Gap vs. Target calculations correct
- [ ] Trend calculations correct (current vs. previous quarter)
- [ ] Priority matrix applied correctly

### Executive Summary Checks

- [ ] Narrative concise (2-3 paragraphs maximum)
- [ ] Top priorities identified (3-5 maximum, not 20!)
- [ ] Priorities have assigned owners and target dates
- [ ] Trend analysis included
- [ ] Recommendations clear and actionable

### Evidence Checks

- [ ] All 4 assessment workbooks archived
- [ ] CSV exports stored
- [ ] Dashboard workbook finalized
- [ ] Executive summary PDF generated
- [ ] Evidence register complete

### Presentation Checks

- [ ] One-page summary suitable for printing
- [ ] Charts and visuals clear and readable
- [ ] No jargon (business language, not IT jargon)
- [ ] Key numbers highlighted (overall score, trend, top priorities)
- [ ] Recommendations prominently displayed

---

## Review & Approval

### Review Process

**Step 1: Self-Review** (Information Security Manager)

- Complete quality checklist above
- Verify all calculations
- Check narrative clarity
- Prepare presentation materials

**Step 2: CISO Review**

- Review overall compliance score and trend
- Assess gap priorities and remediation plans
- Approve resource allocation requests
- Approve presentation to Board/Executive Management

**Step 3: Executive Management Presentation**

- Present one-page summary
- Discuss top priorities
- Request approval for remediation plans
- Answer questions (detailed backup available)

**Step 4: Board Presentation** (if quarterly Board meeting)

- CISO presents dashboard to Board/Audit Committee
- Board reviews compliance status
- Board approves strategic priorities

**Step 5: Archival**

- Archive dashboard and all 4 assessments
- Store evidence per retention policy
- Document approvals and decisions
- Plan next quarter assessment cycle

### Approval Criteria

**Approve Dashboard** if:

- ✅ All 4 assessments completed and consolidated
- ✅ Calculations verified and accurate
- ✅ Executive summary clear and concise
- ✅ Priorities identified with owners and dates
- ✅ Evidence complete

**Return for Revision** if:

- ⚠️ Data quality issues (assessment data inconsistent)
- ⚠️ Incomplete prioritization (no clear top priorities)
- ⚠️ Unclear narrative (jargon, too technical)

**Management Decisions Required**:

- Approve top 3-5 remediation priorities
- Allocate resources for remediation
- Set expectations for Q+1 target (95% compliance?)
- Escalate critical gaps to Executive Management if needed

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
