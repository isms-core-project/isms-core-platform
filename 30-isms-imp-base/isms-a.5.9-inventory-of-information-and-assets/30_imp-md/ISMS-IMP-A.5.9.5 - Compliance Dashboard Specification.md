**ISMS-IMP-A.5.9.5 - Compliance Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.5 |
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

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE** (This Document)
  - Dashboard Overview
  - Prerequisites
  - Dashboard Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION** (Separate Document)
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formula Definitions
  - Python Script Implementation (Dashboard Consolidation)


**Target Audiences:**

- **Part I:** Dashboard users (CISO, Management, Auditors)
- **Part II:** Dashboard developers (Python/Excel script maintainers)


---

# PART I: USER COMPLETION GUIDE

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

**END OF ISMS-IMP-A.5.9.5 PART I - USER COMPLETION GUIDE**

# PART II: TECHNICAL SPECIFICATION

**Audience:** Dashboard developers (Python/Excel script maintainers)

---

## Document Overview

### Purpose of Technical Specification

This section provides complete technical specifications for developers creating or maintaining the Python script that consolidates all 4 assessment workbooks into the executive compliance dashboard.

**Python Script**: `generate_assessment_5_compliance_dashboard.py`

**Input Files** (4 CSV exports):

- `A59_1_Discovery_Metrics_YYYYMMDD.csv`
- `A59_2_Maintenance_Metrics_YYYYMMDD.csv`
- `A59_3_Quality_Metrics_YYYYMMDD.csv`
- `A59_4_Accountability_Metrics_YYYYMMDD.csv`


**Generated Workbook**: `ISMS_A_5_9_Compliance_Dashboard_QX_YYYY.xlsx`

**Key Design Principles**:
1. **Automated Consolidation**: CSV import, not manual data entry
2. **Executive Focus**: Dashboard clarity over technical detail
3. **Audit Trail**: Preserve data lineage from assessments to dashboard
4. **Trending Capability**: Support quarter-over-quarter comparison
5. **Error Handling**: Graceful failure if CSVs malformed or missing

---

## Excel Workbook Structure

### Workbook Metadata

**Workbook Properties**:

- **Title**: ISMS A.5.9 Compliance Dashboard
- **Subject**: ISO/IEC 27001:2022 Control A.5.9 - Executive Reporting
- **Author**: [Organization] ISMS Implementation Team
- **Company**: [Organization]
- **Created**: [Generation Date]
- **Version**: 1.0


### Sheet Summary

| Sheet # | Sheet Name | Purpose | Data Source | User Input | Protection |
|---------|-----------|---------|-------------|------------|-----------|
| 1 | Executive Summary | One-page dashboard | Auto-calc from 2-6 | Executive narrative | Partial |
| 2 | Compliance Scorecard | All 4 assessment scores | Auto-calc from 3-6 | Trending manual | Partial |
| 3 | Discovery Metrics | IMP-A.5.9-1 data | CSV import | None | Full |
| 4 | Maintenance Metrics | IMP-A.5.9-2 data | CSV import | None | Full |
| 5 | Quality Metrics | IMP-A.5.9-3 data | CSV import | None | Full |
| 6 | Accountability Metrics | IMP-A.5.9-4 data | CSV import | None | Full |
| 7 | Trending Analysis | Quarter-over-quarter | Manual + auto-calc | Historical data | Partial |
| 8 | Action Register | Remediation priorities | Compiled from 3-6 | Status updates | Partial |

---

## Global Styling Standards

Same as IMP-A.5.9-1/2/3/4 (refer to those documents for color palette).

---

## CSV Import Specifications

### CSV File Format Requirements

**General Requirements**:

- **Encoding**: UTF-8 with BOM
- **Delimiter**: Comma (`,`)
- **Line Ending**: CRLF (`\r\n`) or LF (`\n`)
- **Header Row**: Required (first row)
- **Data Rows**: Starting from row 2


### CSV 1: Discovery Metrics (from IMP-A.5.9-1)

**Filename Pattern**: `A59_1_Discovery_Metrics_YYYYMMDD.csv`

**Required Columns**:
| Column | Type | Description |
|--------|------|-------------|
| Discovery_Domain | Text | Domain name (Info Assets, IT Infra, Apps, Physical, Personnel) |
| Target | Number (%) | Target completeness |
| Actual | Number (%) | Actual completeness |
| Gap | Number (%) | Gap vs. target |
| Status | Text | Compliance status (✅/⚠️/❌) |

**Sample CSV**:
```csv
Discovery_Domain,Target,Actual,Gap,Status
Information Assets,95,94,-1,⚠️
IT Infrastructure,98,98,0,✅
Applications,90,92,+2,✅
Physical Assets,90,91,+1,✅
Personnel Assets,100,100,0,✅
Overall Discovery Score,95,96,+1,✅
```

### CSV 2: Maintenance Metrics (from IMP-A.5.9-2)

**Filename Pattern**: `A59_2_Maintenance_Metrics_YYYYMMDD.csv`

**Required Columns**:
| Column | Type | Description |
|--------|------|-------------|
| Metric_Category | Text | Category (Update Timeliness, Integration Health, Data Quality, Review Compliance) |
| Target | Number (%) | Target |
| Actual | Number (%) | Current achievement |
| Gap | Number (%) | Gap |
| Status | Text | Compliance status |

**Sample CSV**:
```csv
Metric_Category,Target,Actual,Gap,Status
Update Timeliness,95,89,-6,⚠️
Integration Health,98,96,-2,⚠️
Data Quality,95,87,-8,⚠️
Review Compliance,95,73,-22,❌
Overall Maintenance Score,95,88,-7,⚠️
```

### CSV 3: Quality Metrics (from IMP-A.5.9-3)

**Filename Pattern**: `A59_3_Quality_Metrics_YYYYMMDD.csv`

**Required Columns**:
| Column | Type | Description |
|--------|------|-------------|
| Quality_Dimension | Text | Dimension (Accuracy, Completeness, Currency, Consistency, Policy Compliance) |
| Weight | Number (%) | Weighting |
| Target | Number (%) | Target score |
| Actual | Number (%) | Actual score |
| Gap | Number (%) | Gap |
| Status | Text | Compliance status |

**Sample CSV**:
```csv
Quality_Dimension,Weight,Target,Actual,Gap,Status
Accuracy,30,95,96,+1,✅
Completeness,25,100,94,-6,⚠️
Currency,20,100,92,-8,⚠️
Consistency,15,99,98.5,-0.5,✅
Policy Compliance,10,100,89,-11,⚠️
Overall Quality Score,100,97,94.2,-2.8,⚠️
```

### CSV 4: Accountability Metrics (from IMP-A.5.9-4)

**Filename Pattern**: `A59_4_Accountability_Metrics_YYYYMMDD.csv`

**Required Columns**:
| Column | Type | Description |
|--------|------|-------------|
| Accountability_Dimension | Text | Dimension (Coverage, Acknowledgment, Awareness, Performance) |
| Weight | Number (%) | Weighting |
| Target | Number (%) | Target score |
| Actual | Number (%) | Actual score |
| Gap | Number (%) | Gap |
| Status | Text | Compliance status |

**Sample CSV**:
```csv
Accountability_Dimension,Weight,Target,Actual,Gap,Status
Coverage,30,100,98,-2,⚠️
Acknowledgment,25,95,89,-6,⚠️
Awareness,20,100,85,-15,❌
Performance,25,80,76,-4,⚠️
Overall Accountability Score,100,94,88.1,-5.9,⚠️
```

---

## Sheet 1: Executive Summary - Complete Specification

### Purpose

One-page executive dashboard.

### Layout Structure

**Section A: Header & Overall Score** (Rows 1-12)
**Section B: Assessment Breakdown** (Rows 14-22)
**Section C: Top Priorities** (Rows 24-32)
**Section D: Executive Narrative** (Rows 34-45)
**Section E: Key Metrics** (Rows 47-58)
**Section F: Audit Readiness** (Rows 60-68)

### Section A: Header & Overall Score

```python
def create_header_section(ws):
    # Title
    ws.merge_cells('A1:P1')
    ws['A1'] = "CONTROL A.5.9 - COMPLIANCE DASHBOARD"
    ws['A1'].font = Font(size=18, bold=True, color='003366')
    ws['A1'].alignment = Alignment(horizontal='center')
    ws.row_dimensions[1].height = 35
    
    # Subtitle
    ws.merge_cells('A2:P2')
    ws['A2'] = "Asset Inventory Management - Executive Summary"
    ws['A2'].font = Font(size=12, color='666666')
    ws['A2'].alignment = Alignment(horizontal='center')
    
    # Assessment Quarter
    ws['A4'] = "Assessment Quarter:"
    ws['B4'] = f"Q{current_quarter} {current_year}"  # User configurable
    ws['A4'].font = Font(bold=True)
    
    ws['A5'] = "Assessment Date:"
    ws['B5'] = datetime.now().strftime('%d.%m.%Y')
    ws['A5'].font = Font(bold=True)
    
    # OVERALL COMPLIANCE SCORE (Large, prominent)
    ws.merge_cells('A7:D10')
    ws['A7'] = "OVERALL COMPLIANCE"
    ws['A7'].font = Font(size=14, bold=True, color='003366')
    ws['A7'].alignment = Alignment(horizontal='center', vertical='top')
    
    ws.merge_cells('A11:D11')
    # Formula: Weighted average of 4 assessments
    ws['A11'] = "=('Discovery Metrics'!B7*0.25)+('Maintenance Metrics'!B6*0.20)+('Quality Metrics'!B8*0.35)+('Accountability Metrics'!B7*0.20)"
    ws['A11'].number_format = '0.0"%"'
    ws['A11'].font = Font(size=36, bold=True)
    ws['A11'].alignment = Alignment(horizontal='center')
    
    # Compliance Status (Conditional)
    ws.merge_cells('A12:D12')
    ws['A12'] = '=IF(A11>=90,"✅ Compliant",IF(A11>=75,"⚠️ At Risk","❌ Non-Compliant"))'
    ws['A12'].font = Font(size=14, bold=True)
    ws['A12'].alignment = Alignment(horizontal='center')
    
    # Conditional formatting for A11 (overall score)
    # Green: ≥90%, Yellow: 75-89%, Red: <75%
    # (add conditional formatting rules)
```

### Section B: Assessment Breakdown

```python
def create_assessment_breakdown(ws, row_start=14):
    # Table header
    ws[f'A{row_start}'] = "ASSESSMENT BREAKDOWN"
    ws[f'A{row_start}'].font = Font(size=12, bold=True, color='003366')
    
    row = row_start + 2
    
    # Column headers
    headers = ['Assessment', 'Weight', 'Target', 'Actual', 'Gap', 'Status']
    for col_num, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_num, value=header)
        cell.font = Font(bold=True, color='FFFFFF')
        cell.fill = PatternFill(start_color='003366', fill_type='solid')
        cell.alignment = Alignment(horizontal='center')
    
    row += 1
    
    # Assessment rows (formulas pull from metric sheets)
    assessments = [
        ('Discovery', 25, '=\'Discovery Metrics\'!B7'),
        ('Maintenance', 20, '=\'Maintenance Metrics\'!B6'),
        ('Quality', 35, '=\'Quality Metrics\'!B8'),
        ('Accountability', 20, '=\'Accountability Metrics\'!B7')
    ]
    
    for assessment, weight, actual_formula in assessments:
        ws[f'A{row}'] = assessment
        ws[f'B{row}'] = weight
        ws[f'B{row}'].number_format = '0"%"'
        
        # Target (pull from respective metric sheet or use config)
        ws[f'C{row}'] = get_target_for_assessment(assessment)  # e.g., 95, 95, 97, 94
        ws[f'C{row}'].number_format = '0"%"'
        
        # Actual (formula to metric sheet)
        ws[f'D{row}'] = actual_formula
        ws[f'D{row}'].number_format = '0.0"%"'
        
        # Gap
        ws[f'E{row}'] = f'=D{row}-C{row}'
        ws[f'E{row}'].number_format = '0.0"%"'
        
        # Status (conditional)
        ws[f'F{row}'] = f'=IF(D{row}>=C{row},"✅",IF(D{row}>=C{row}-10,"⚠️","❌"))'
        ws[f'F{row}'].alignment = Alignment(horizontal='center')
        
        row += 1
    
    # Overall row (bold, larger font)
    ws[f'A{row}'] = "OVERALL"
    ws[f'A{row}'].font = Font(bold=True, size=12)
    ws[f'B{row}'] = 100
    ws[f'B{row}'].number_format = '0"%"'
    ws[f'C{row}'] = 95  # Overall target (configurable)
    ws[f'C{row}'].number_format = '0"%"'
    ws[f'D{row}'] = '=A11'  # Link to overall score
    ws[f'D{row}'].number_format = '0.0"%"'
    ws[f'D{row}'].font = Font(bold=True, size=12)
    ws[f'E{row}'] = f'=D{row}-C{row}'
    ws[f'E{row}'].number_format = '0.0"%"'
    ws[f'E{row}'].font = Font(bold=True)
    ws[f'F{row}'] = '=F12'  # Link to overall status
    ws[f'F{row}'].alignment = Alignment(horizontal='center')
    ws[f'F{row}'].font = Font(bold=True, size=12)
```

### Section C: Top Priorities

```python
def create_top_priorities(ws, row_start=24):
    ws[f'A{row_start}'] = "TOP 3 PRIORITIES THIS QUARTER"
    ws[f'A{row_start}'].font = Font(size=12, bold=True, color='003366')
    
    row = row_start + 2
    
    # Headers
    headers = ['Priority', 'Gap Description', 'Severity', 'Owner', 'Target Date', 'Status']
    for col_num, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_num, value=header)
        cell.font = Font(bold=True)
    
    row += 1
    
    # Priority 1-3 rows (user fills these, or pulled from Action Register sheet)
    # These can be manually entered or auto-populated from top of Action Register
    for priority_num in range(1, 4):
        ws[f'A{row}'] = priority_num
        ws[f'A{row}'].alignment = Alignment(horizontal='center')
        ws[f'A{row}'].font = Font(bold=True)
        
        # Gap description - user enters or formula from Action Register
        ws[f'B{row}'] = f'=IF(\'Action Register\'!B{priority_num+2}<>"",\'Action Register\'!B{priority_num+2},"[To be determined]")'
        ws[f'B{row}'].alignment = Alignment(horizontal='left', wrap_text=True)
        
        # Severity
        ws[f'C{row}'] = f'=IF(\'Action Register\'!D{priority_num+2}<>"",\'Action Register\'!D{priority_num+2},"")'
        
        # Owner
        ws[f'D{row}'] = f'=IF(\'Action Register\'!H{priority_num+2}<>"",\'Action Register\'!H{priority_num+2},"")'
        
        # Target Date
        ws[f'E{row}'] = f'=IF(\'Action Register\'!I{priority_num+2}<>"",\'Action Register\'!I{priority_num+2},"")'
        ws[f'E{row}'].number_format = 'DD.MM.YYYY'
        
        # Status
        ws[f'F{row}'] = f'=IF(\'Action Register\'!J{priority_num+2}<>"",\'Action Register\'!J{priority_num+2},"")'
        
        row += 1
```

### Section D: Executive Narrative

```python
def create_executive_narrative_section(ws, row_start=34):
    ws[f'A{row_start}'] = "EXECUTIVE NARRATIVE"
    ws[f'A{row_start}'].font = Font(size=12, bold=True, color='003366')
    
    row = row_start + 2
    
    # Merged cell for narrative (user enters 2-3 paragraphs)
    ws.merge_cells(f'A{row}:P{row+8}')
    ws[f'A{row}'] = """[User enters executive narrative here - 2-3 paragraphs]

Template:

- Paragraph 1: Current state summary (overall score, comparison to target)
- Paragraph 2: Key achievements this quarter (specific accomplishments, quantified improvements)
- Paragraph 3: Critical gaps and recommended actions (specific gaps, proposed remediation, resource needs)

"""
    ws[f'A{row}'].alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
    ws[f'A{row}'].font = Font(size=11)
    ws.row_dimensions[row].height = 150
    
    # User replaces template with actual narrative
    ws[f'A{row}'].protection = Protection(locked=False)  # Unlocked for editing
```

### Section E: Key Metrics

```python
def create_key_metrics(ws, row_start=47):
    ws[f'A{row_start}'] = "KEY METRICS AT A GLANCE"
    ws[f'A{row_start}'].font = Font(size=12, bold=True, color='003366')
    
    row = row_start + 2
    
    metrics = [
        ('Total Assets Inventoried', '=\'Discovery Metrics\'!B2', 'From Discovery'),
        ('Asset Categories Covered', '5 of 5', 'Fixed'),
        ('Ownership Coverage', '=\'Accountability Metrics\'!D3', 'From Accountability'),
        ('Data Quality Score', '=\'Quality Metrics\'!D8', 'From Quality'),
        ('Critical Assets at Risk', '[Manual Entry]', 'From assessments'),
        ('High Priority Gaps', '=COUNTIF(\'Action Register\'!D:D,"Critical")+COUNTIF(\'Action Register\'!D:D,"High")', 'From Action Register')
    ]
    
    for metric_name, formula_or_value, source in metrics:
        ws[f'A{row}'] = metric_name
        ws[f'A{row}'].font = Font(bold=True)
        
        if formula_or_value.startswith('='):
            ws[f'B{row}'] = formula_or_value
        else:
            ws[f'B{row}'] = formula_or_value
        
        ws[f'B{row}'].font = Font(size=11)
        row += 1
```

### Section F: Audit Readiness

```python
def create_audit_readiness(ws, row_start=60):
    ws[f'A{row_start}'] = "AUDIT READINESS"
    ws[f'A{row_start}'].font = Font(size=12, bold=True, color='003366')
    
    row = row_start + 2
    
    # ISO Control Status
    ws[f'A{row}'] = "ISO/IEC 27001:2022 Control A.5.9:"
    ws[f'A{row}'].font = Font(bold=True)
    ws[f'B{row}'] = '=F12'  # Link to overall compliance status
    ws[f'B{row}'].alignment = Alignment(horizontal='center')
    ws[f'B{row}'].font = Font(bold=True, size=12)
    row += 1
    
    # Evidence Completeness
    ws[f'A{row}'] = "Evidence Completeness:"
    ws[f'A{row}'].font = Font(bold=True)
    ws[f'B{row}'] = '[Manual: % of evidence collected]'  # User enters
    ws[f'B{row}'].protection = Protection(locked=False)
    row += 1
    
    # Last Audit Finding
    ws[f'A{row}'] = "Last Audit Findings:"
    ws[f'A{row}'].font = Font(bold=True)
    ws[f'B{row}'] = '[Manual: Open/Closed/N/A]'
    ws[f'B{row}'].protection = Protection(locked=False)
    row += 1
    
    # Next Audit Preparation
    ws[f'A{row}'] = "Next Audit Preparation:"
    ws[f'A{row}'].font = Font(bold=True)
    ws[f'B{row}'] = '[Manual: On Track/At Risk/Behind]'
    ws[f'B{row}'].protection = Protection(locked=False)
```

---

## Sheet 2: Compliance Scorecard - Complete Specification

### Purpose

Detailed breakdown of all 4 assessments.

### Table Structure

**Table 1: Assessment Summary** (Rows 3-12)

Columns: Assessment | Weight | Target | Actual | Gap | Status | Trend

**Table 2: Dimension Details** (Rows 15+)

For each assessment, show sub-dimensions:

```python
def create_scorecard_sheet(ws):
    # Table 1: Assessment Summary
    create_assessment_summary_table(ws, row_start=3)
    
    # Table 2: Discovery Breakdown
    create_discovery_breakdown(ws, row_start=15)
    
    # Table 3: Maintenance Breakdown
    create_maintenance_breakdown(ws, row_start=25)
    
    # Table 4: Quality Breakdown
    create_quality_breakdown(ws, row_start=35)
    
    # Table 5: Accountability Breakdown
    create_accountability_breakdown(ws, row_start=50)
    
    # Traffic Light Summary
    create_traffic_light_summary(ws, row_start=65)
```

Formulas pull directly from Sheets 3-6 (imported CSV data).

---

## Sheets 3-6: CSV Import Sheets - Specification

### Sheet 3: Discovery Metrics

**Import Source**: `A59_1_Discovery_Metrics_YYYYMMDD.csv`

**Layout**:

- Row 1: Headers
- Rows 2+: Data from CSV


**Python Implementation**:

```python
def import_discovery_metrics(ws, csv_filepath):
    """Import Discovery CSV into Sheet 3"""
    import csv
    
    with open(csv_filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row_num, row_data in enumerate(reader, start=1):
            for col_num, cell_value in enumerate(row_data, start=1):
                cell = ws.cell(row=row_num, column=col_num)
                
                # Try to convert to number if possible
                try:
                    cell.value = float(cell_value)
                except ValueError:
                    cell.value = cell_value
                
                # Header formatting
                if row_num == 1:
                    cell.font = Font(bold=True, color='FFFFFF')
                    cell.fill = PatternFill(start_color='003366', fill_type='solid')
                    cell.alignment = Alignment(horizontal='center')
    
    # Protect sheet (read-only, imported data)
    ws.protection.sheet = True
```

### Sheets 4-6: Same Pattern

Same CSV import logic for Maintenance, Quality, and Accountability metrics.

---

## Sheet 7: Trending Analysis - Specification

### Purpose

Quarter-over-quarter comparison.

### Table Structure

**Historical Data Table** (manual entry for past quarters):

| Quarter | Overall | Discovery | Maintenance | Quality | Accountability |
|---------|---------|-----------|-------------|---------|----------------|
| Q4 2025 | 89.1% | 93% | 84% | 91% | 85% |
| Q1 2026 | 92.8% (formula) | 96% (formula) | 89% (formula) | 94.2% (formula) | 88.1% (formula) |
| Q2 2026 | (future) | (future) | (future) | (future) | (future) |

**Formulas for Current Quarter**:
```python
# Overall Score for current quarter
ws['B5'] = '=\'Executive Summary\'!A11'

# Discovery Score for current quarter
ws['C5'] = '=\'Discovery Metrics\'!B7'

# etc.
```

**Trend Calculation**:
```python
# Improvement Rate
ws['G5'] = '=(B5-B4)/B4*100'  # % change vs. previous quarter
ws['G5'].number_format = '0.0"%"'

# Trend Direction
ws['H5'] = '=IF(G5>1,"↗️ Improved",IF(G5<-1,"↘️ Degraded","→ Stable"))'
```

**Forecast** (simple linear projection):
```python
# Projected Q+1
ws['B6'] = '=B5+(B5-B4)'  # Linear: Current + (Current - Previous)
```

---

## Sheet 8: Action Register - Specification

### Purpose

Consolidated gaps from all 4 assessments with prioritization.

### Column Structure

| Col | Header | Width | Source |
|-----|--------|-------|--------|
| A | Priority | 10 | Auto-ranked |
| B | Gap Description | 50 | From assessments |
| C | Source Assessment | 20 | Discovery/Maintenance/Quality/Accountability |
| D | Severity | 15 | From assessment |
| E | Impact | 15 | Manual entry |
| F | Effort | 15 | Manual entry |
| G | Priority Score | 12 | Auto-calculated |
| H | Owner | 25 | From assessment or assigned |
| I | Target Date | 15 | From assessment or set |
| J | Status | 15 | Dropdown |
| K | % Complete | 10 | Manual |
| L | Evidence | 30 | Link |
| M | Notes | 30 | Free text |

### Priority Calculation

```python
def calculate_priority_score(severity, impact, effort):
    """
    Priority Score = (Severity_Points + Impact_Points) × (Effort_Inverse) + Audit_Relevance
    
    Severity: Critical=10, High=7, Medium=4, Low=2
    Impact: High=8, Medium=5, Low=2
    Effort: High=3/10, Medium=5/10, Low=8/10 (inverse: lower effort = higher priority)
    Audit_Relevance: +8 for SHALL requirements, +3 for SHOULD, 0 for operational
    """
    
    severity_points = {'Critical': 10, 'High': 7, 'Medium': 4, 'Low': 2}
    impact_points = {'High': 8, 'Medium': 5, 'Low': 2}
    effort_inverse = {'High': 3, 'Medium': 5, 'Low': 8}
    
    score = (severity_points[severity] + impact_points[impact]) * (effort_inverse[effort] / 10)
    
    # Add audit relevance (heuristic: if severity is Critical or High, likely audit-relevant)
    if severity in ['Critical', 'High']:
        score += 8
    
    return score

# In Excel formula:
ws['G3'] = '''=
  (IF(D3="Critical",10,IF(D3="High",7,IF(D3="Medium",4,2))) +
   IF(E3="High",8,IF(E3="Medium",5,2))) *
  (IF(F3="High",0.3,IF(F3="Medium",0.5,0.8))) +
  IF(OR(D3="Critical",D3="High"),8,0)
'''
```

### Auto-Ranking

```python
# Sort Action Register by Priority Score (descending)
# Column A (Priority) is rank after sort
# This can be done manually via Excel sort, or programmatically
```

---

## Python Consolidation Script - Complete Template

```python
"""
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR YOUR ORGANIZATION

Compliance Dashboard Consolidation Script
ISO/IEC 27001:2022 Control A.5.9

This script consolidates 4 assessment CSVs into executive dashboard workbook.

IMPORTANT: This is a SAMPLE script. Customize for your organization:
1. CSV file paths (adjust to your directory structure)
2. Assessment weights (verify 25%/20%/35%/20% is correct for you)
3. Target scores (verify 95%/95%/97%/94% matches your policy)
4. Action prioritization logic (adjust severity/impact/effort scoring)

Author: ISMS Implementation Team
Date: [Date]
Version: 1.0
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, Protection
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from datetime import datetime
import csv
import os
import sys

# CUSTOMIZE: Configuration
CONFIG = {
    'input_dir': './csv-exports/',
    'output_dir': './dashboards/',
    'workbook_name': f'ISMS_A_5_9_Compliance_Dashboard_Q1_{datetime.now().year}.xlsx',
    
    # Assessment weights (must sum to 100%)
    'weights': {
        'Discovery': 25,
        'Maintenance': 20,
        'Quality': 35,
        'Accountability': 20
    },
    
    # Target scores
    'targets': {
        'Discovery': 95,
        'Maintenance': 95,
        'Quality': 97,
        'Accountability': 94,
        'Overall': 95
    },
    
    # CSV filenames (adjust YYYYMMDD to your generation dates)
    'csv_files': {
        'Discovery': 'A59_1_Discovery_Metrics_20260115.csv',
        'Maintenance': 'A59_2_Maintenance_Metrics_20260118.csv',
        'Quality': 'A59_3_Quality_Metrics_20260120.csv',
        'Accountability': 'A59_4_Accountability_Metrics_20260122.csv'
    },
    
    'sheets': [
        'Executive Summary',
        'Compliance Scorecard',
        'Discovery Metrics',
        'Maintenance Metrics',
        'Quality Metrics',
        'Accountability Metrics',
        'Trending Analysis',
        'Action Register'
    ]
}


def main():
    """Main execution function"""
    
    print("=" * 70)
    print("ISMS A.5.9 COMPLIANCE DASHBOARD CONSOLIDATION")
    print("=" * 70)
    print()
    
    # Step 1: Validate all CSV files exist
    print("[1/6] Validating CSV files...")
    csv_paths = validate_csv_files()
    if not csv_paths:
        print("❌ ERROR: Missing CSV files. Cannot proceed.")
        sys.exit(1)
    print("  ✓ All 4 CSV files found")
    print()
    
    # Step 2: Create workbook structure
    print("[2/6] Creating dashboard workbook...")
    wb = create_workbook_structure()
    print("  ✓ Workbook created with 8 sheets")
    print()
    
    # Step 3: Import CSV data into sheets 3-6
    print("[3/6] Importing assessment data...")
    import_assessment_data(wb, csv_paths)
    print("  ✓ All assessment data imported")
    print()
    
    # Step 4: Generate executive summary
    print("[4/6] Generating Executive Summary...")
    create_executive_summary(wb['Executive Summary'])
    print("  ✓ Executive Summary generated")
    print()
    
    # Step 5: Generate scorecard
    print("[5/6] Generating Compliance Scorecard...")
    create_compliance_scorecard(wb['Compliance Scorecard'])
    print("  ✓ Scorecard generated")
    print()
    
    # Step 6: Generate action register template
    print("[6/6] Creating Action Register template...")
    create_action_register(wb['Action Register'])
    print("  ✓ Action Register created")
    print()
    
    # Save workbook
    output_path = os.path.join(CONFIG['output_dir'], CONFIG['workbook_name'])
    os.makedirs(CONFIG['output_dir'], exist_ok=True)
    wb.save(output_path)
    
    print("=" * 70)
    print(f"✓ DASHBOARD GENERATED SUCCESSFULLY!")
    print(f"  Location: {output_path}")
    print(f"  Size: {os.path.getsize(output_path) / 1024:.1f} KB")
    print()
    print("NEXT STEPS:")
    print("  1. Review imported data in Sheets 3-6")
    print("  2. Complete Executive Narrative in Sheet 1")
    print("  3. Populate Action Register in Sheet 8")
    print("  4. Review with CISO and distribute")
    print("=" * 70)


def validate_csv_files():
    """Validate all required CSV files exist"""
    csv_paths = {}
    all_exist = True
    
    for assessment, filename in CONFIG['csv_files'].items():
        filepath = os.path.join(CONFIG['input_dir'], filename)
        if os.path.exists(filepath):
            csv_paths[assessment] = filepath
            print(f"  ✓ {assessment}: {filename}")
        else:
            print(f"  ❌ {assessment}: {filename} NOT FOUND")
            all_exist = False
    
    return csv_paths if all_exist else None


def create_workbook_structure():
    """Create workbook with all sheets"""
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    
    for sheet_name in CONFIG['sheets']:
        wb.create_sheet(title=sheet_name)
    
    # Set workbook properties
    wb.properties.title = "ISMS A.5.9 Compliance Dashboard"
    wb.properties.subject = "ISO/IEC 27001:2022 Control A.5.9"
    wb.properties.creator = "[Organization] ISMS Team"
    wb.properties.created = datetime.now()
    
    return wb


def import_assessment_data(wb, csv_paths):
    """Import CSV data into sheets 3-6"""
    
    sheet_mapping = {
        'Discovery': 'Discovery Metrics',
        'Maintenance': 'Maintenance Metrics',
        'Quality': 'Quality Metrics',
        'Accountability': 'Accountability Metrics'
    }
    
    for assessment, sheet_name in sheet_mapping.items():
        ws = wb[sheet_name]
        csv_path = csv_paths[assessment]
        
        with open(csv_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            for row_num, row_data in enumerate(reader, start=1):
                for col_num, cell_value in enumerate(row_data, start=1):
                    cell = ws.cell(row=row_num, column=col_num)
                    
                    # Try numeric conversion
                    try:
                        if cell_value.endswith('%'):
                            cell.value = float(cell_value.rstrip('%')) / 100
                            cell.number_format = '0.0"%"'
                        else:
                            cell.value = float(cell_value)
                    except (ValueError, AttributeError):
                        cell.value = cell_value
                    
                    # Header formatting
                    if row_num == 1:
                        cell.font = Font(bold=True, color='FFFFFF')
                        cell.fill = PatternFill(start_color='003366', fill_type='solid')
                        cell.alignment = Alignment(horizontal='center')
        
        # Protect sheet
        ws.protection.sheet = True
        print(f"  ✓ Imported {assessment} metrics")


def create_executive_summary(ws):
    """Generate Executive Summary sheet"""
    # Implementation as per specification above
    # (create_header_section, create_assessment_breakdown, etc.)
    pass


def create_compliance_scorecard(ws):
    """Generate Compliance Scorecard sheet"""
    # Implementation as per specification
    pass


def create_action_register(ws):
    """Create Action Register template"""
    # Implementation as per specification
    pass


if __name__ == '__main__':
    main()
```

---

## Integration Testing

### Test Procedure

1. **Generate Test CSVs** from sample assessment workbooks
2. **Run consolidation script**
3. **Verify imported data** matches source CSVs
4. **Check formulas** calculate correctly
5. **Test conditional formatting** (traffic lights work)
6. **Manual review** executive summary for completeness

### Expected Outputs

- Dashboard workbook generated without errors
- All 4 CSV files imported successfully
- Overall compliance score calculated correctly
- Traffic light indicators display properly
- Action register populated with sample data


---

**END OF SPECIFICATION**

---

*"The optimist thinks this is the best of all possible worlds. The pessimist fears it is true."*
— J. Robert Oppenheimer

*Where bamboo antennas actually work.* 🎋
