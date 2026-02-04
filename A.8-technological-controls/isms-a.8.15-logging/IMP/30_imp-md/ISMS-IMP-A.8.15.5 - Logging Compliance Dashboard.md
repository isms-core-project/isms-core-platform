**ISMS-IMP-A.8.15.5 - Compliance Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.5 |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Compliance Dashboard & Gap Prioritization |
| **Related Policy** | ISMS-POL-A.8.15 (All Sections) |
| **Purpose** | Consolidate assessments A.8.15.1, .2, .3, .4 into executive dashboard; track overall compliance; prioritize cross-domain gaps; monitor trends |
| **Target Audience** | CISO, Senior Management, Board of Directors, Information Security Manager, Compliance Team, Internal Audit, External Auditors, Workbook Developers |
| **Assessment Type** | Consolidation & Executive Reporting |
| **Review Cycle** | Quarterly (consolidation after all sub-assessments complete), Annual (formal presentation to Board) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial dashboard specification | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Dashboard Overview
  - Prerequisites
  - Data Consolidation Workflow
  - Dashboard Sections
  - Gap Prioritization Methodology
  - Trend Analysis
  - Executive Presentation
  - Evidence Collection

- **PART II: TECHNICAL SPECIFICATION**
  - Workbook Structure Overview
  - Sheet-by-Sheet Specifications
  - External Workbook References
  - Formula Definitions
  - Cell Styling Reference
  - Python Script Usage Notes

**Target Audiences:**

- **Part I:** Executive stakeholders (CISO, Board), InfoSec Manager, Compliance Team
- **Part II:** Workbook developers (Python/Excel script maintainers)

---

# PART I: USER COMPLETION GUIDE

**Audience:** CISO, Senior Management, InfoSec Manager, Compliance Team

---

# Dashboard Overview

## What This Dashboard Provides

This dashboard consolidates FOUR detailed assessments into a single executive view:

**Source Assessments**:
1. **IMP-A.8.15.1**: Log Source Inventory (what systems are logging)
2. **IMP-A.8.15.2**: Log Collection & Centralization (logs flowing to SIEM)
3. **IMP-A.8.15.3**: Log Protection & Retention (logs protected and retained)
4. **IMP-A.8.15.4**: Log Analysis & Review (logs analyzed and reviewed)

**Dashboard Outputs**:

- **Overall Compliance Score**: Single percentage (0-100%) representing Control A.8.15 compliance
- **Compliance by Domain**: Scores for each of the 4 assessment areas
- **Gap Summary**: Total gaps across all domains, prioritized by risk
- **Trend Analysis**: Compliance improvement/degradation over time (if multiple assessment cycles)
- **Remediation Tracking**: Status of gap remediation efforts
- **Executive Findings**: 1-page summary for Board/Senior Management

## Why This Matters

**For CISO/Senior Management**:

- Single view of logging compliance posture
- Risk-based gap prioritization (where to invest resources)
- Proof of continuous improvement (trend tracking)
- Board reporting (executive summary ready for presentation)

**For InfoSec Manager**:

- Holistic view across all logging domains
- Cross-domain gap analysis (identify systemic issues)
- Resource allocation prioritization
- Audit readiness (consolidated evidence)

**For Compliance/Audit**:

- Objective evidence of Control A.8.15 implementation
- Traceability (Control -> Policy -> Assessments -> Evidence)
- Gap tracking and closure verification
- Trend analysis (continuous monitoring)

## Dashboard Philosophy

**"One Number" Principle**:

- Board wants ONE number: "Are we compliant with logging requirements?"
- Overall Compliance Score provides that number
- Details available on-demand (drill-down capability)

**Risk-Based Prioritization**:

- Not all gaps are equal
- Dashboard prioritizes gaps by: Impact x Likelihood x Detectability / Remediation Effort
- Focus resources on highest-priority gaps

**Trend Tracking**:

- Compliance is not point-in-time
- Track trends over multiple assessment cycles
- Demonstrate continuous improvement

---

# Prerequisites

## Required Completed Assessments

**CRITICAL**: All FOUR sub-assessments MUST be completed before dashboard consolidation:

[X] **IMP-A.8.15.1** - Log Source Inventory Assessment  
[X] **IMP-A.8.15.2** - Log Collection & Centralization Assessment  
[X] **IMP-A.8.15.3** - Log Protection & Retention Assessment  
[X] **IMP-A.8.15.4** - Log Analysis & Review Assessment  

**If any assessment incomplete**:

- Dashboard will show partial data
- Overall Compliance Score will be incomplete
- Gap analysis will miss entire domains
- **Recommendation**: Complete all assessments before dashboard consolidation

## Required Access

**Assessment Workbooks**:

- Read access to all 4 completed assessment workbooks
- Workbooks must be in accessible location (network drive, SharePoint, OneDrive)
- File paths needed for external workbook references

**Historical Data** (if trend analysis desired):

- Previous assessment cycles (if available)
- Previous dashboard workbooks (for comparison)

## Required Personnel

**Primary Responsibility**:

- **Information Security Manager**: Owns dashboard consolidation, presents to CISO

**Supporting Input**:

- **CISO**: Reviews dashboard, provides strategic direction on gaps
- **Compliance Manager**: Validates compliance interpretation, regulatory mapping
- **Internal Audit**: Reviews for audit readiness

**Estimated Time**: 4-6 hours for initial consolidation, 2-3 hours for updates

---

# Data Consolidation Workflow

## Consolidation Steps

**Step 1: Verify Assessment Completion** (30 minutes)

- Confirm all 4 assessments approved (Level 3 sign-off)
- Verify assessment dates within acceptable range (all within same quarter recommended)
- Check for any "In Progress" or "Pending" statuses

**Step 2: External Workbook Linking** (1 hour)

- Python script automatically creates external references to 4 source workbooks
- Verify file paths correct (update if workbooks moved)
- Test links (ensure formulas pulling data correctly)

**Step 3: Compliance Score Calculation** (automated)

- Dashboard extracts compliance scores from each source assessment
- Calculates weighted average (Overall Compliance Score)
- Color codes results (Green/Yellow/Orange/Red)

**Step 4: Gap Consolidation** (1-2 hours)

- Extract all gaps from 4 source assessments
- Remove duplicates (same gap identified in multiple assessments)
- Re-prioritize using cross-domain risk scoring
- Assign remediation owners

**Step 5: Trend Analysis** (1 hour, if previous cycles available)

- Import previous cycle scores
- Calculate deltas (improvement/decline)
- Generate trend graphs

**Step 6: Executive Summary Creation** (1-2 hours)

- Write 1-page executive summary (narrative)
- Highlight key findings (top 3 strengths, top 3 gaps)
- Include recommendations (top 3 actions for CISO)

**Step 7: Review & Approval** (varies)

- InfoSec Manager self-review
- CISO review and approval
- Present to Board/Senior Management (if required)

---

# Dashboard Sections

## Section 1: Executive Summary (Sheet 2)

**Purpose**: One-page summary for CISO/Board

**Content**:

- Overall Compliance Score (large, color-coded: 85% = Green, 65% = Yellow, 40% = Red)
- Compliance by Domain (4 scores: Inventory, Collection, Protection, Analysis)
- Key Findings (narrative):
  - Top 3 Strengths (what's working well)
  - Top 3 Gaps (highest-priority issues)
  - Top 3 Recommendations (what CISO should prioritize)
- Trend (if available): Compliance score vs. previous quarter
- Assessment Date Range (when assessments performed)

**Target Audience**: CISO, Board, Senior Management (non-technical stakeholders)

**Time to Complete**: 1-2 hours (writing narrative findings/recommendations)

## Section 2: Compliance Scorecard (Sheet 3)

**Purpose**: Detailed compliance metrics by domain

**Content**:

| Domain | Compliance Score | Target | Status | Gap Count | Critical Gaps |
|--------|-----------------|--------|--------|-----------|---------------|
| A.8.15.1 - Inventory | [from IMP-A.8.15.1] | >=90% | [*] | [count] | [count] |
| A.8.15.2 - Collection | [from IMP-A.8.15.2] | >=95% | [*] | [count] | [count] |
| A.8.15.3 - Protection | [from IMP-A.8.15.3] | >=95% | [*] | [count] | [count] |
| A.8.15.4 - Analysis | [from IMP-A.8.15.4] | >=80% | [*] | [count] | [count] |
| **Overall A.8.15** | **Weighted Avg** | **>=85%** | **[*]** | **Total** | **Total** |

**Weighting** (for Overall Score):

- Inventory: 20% (foundational - know what systems exist)
- Collection: 25% (critical - logs must be centralized)
- Protection: 25% (critical - logs must be tamper-proof)
- Analysis: 30% (most important - logs must be reviewed to provide value)

**Formula**: `Overall = (0.20 x Inventory) + (0.25 x Collection) + (0.25 x Protection) + (0.30 x Analysis)`

**Target Audience**: InfoSec Manager, Compliance Team, Internal Audit

**Time to Complete**: Automated (formulas extract from source assessments)

## Section 3: Gap Consolidation & Prioritization (Sheet 4)

**Purpose**: All gaps across all domains, prioritized by risk

**Content**:

**For Each Gap** (consolidated from 4 source assessments):

- Gap ID (CONS-001, CONS-002...)
- Source Assessment (A.8.15.1, .2, .3, or .4)
- Domain (Inventory, Collection, Protection, Analysis)
- Gap Description (from source assessment)
- Policy Reference (ISMS-POL-A.8.15 section violated)
- Risk Rating (Critical, High, Medium, Low - may be re-scored for cross-domain perspective)
- Business Impact (what could go wrong)
- Remediation Plan (from source assessment)
- Responsible Party (who will fix)
- Target Completion Date
- Status (Open, In Progress, Resolved, Deferred)
- Tracking Ticket (Jira, ServiceNow, etc.)

**Gap Prioritization Logic**:
```
Priority_Score = (Impact x Likelihood x Detectability) / Remediation_Effort

Where:

- Impact: 1-5 (business impact if gap exploited)
- Likelihood: 1-5 (probability of gap being exploited)
- Detectability: 1-5 (current detection capability - inverted: 5=blind spot, 1=well-detected)
- Remediation_Effort: 1-5 (effort to fix - lower effort = higher priority)

Higher Score = Higher Priority
```

**Gap Summary by Domain**:
| Domain | Total Gaps | Critical | High | Medium | Low |
|--------|-----------|----------|------|--------|-----|
| Inventory | [count] | [count] | [count] | [count] | [count] |
| Collection | [count] | [count] | [count] | [count] | [count] |
| Protection | [count] | [count] | [count] | [count] | [count] |
| Analysis | [count] | [count] | [count] | [count] | [count] |
| **Total** | **[sum]** | **[sum]** | **[sum]** | **[sum]** | **[sum]** |

**Target Audience**: CISO, InfoSec Manager, Project Managers (gap remediation)

**Time to Complete**: 1-2 hours (consolidating gaps, removing duplicates, re-scoring)

## Section 4: Remediation Tracking (Sheet 5)

**Purpose**: Track gap closure progress

**Content**:

**For Each Remediation Initiative**:

- Initiative ID (linked to Gap ID)
- Initiative Name (brief description)
- Responsible Party (owner)
- Start Date, Target Date, Actual Completion Date
- Status (Not Started, In Progress, Blocked, Completed)
- % Complete (0-100%)
- Budget (if applicable)
- Blockers/Issues (what's preventing progress)
- Last Update Date

**Remediation Progress Summary**:

- Total Initiatives: [count]
- Completed: [count] ([%])
- In Progress: [count] ([%])
- Not Started: [count] ([%])
- Blocked: [count] ([%])
- On Track: [count] (will complete by target date)
- At Risk: [count] (may miss target date)
- Overdue: [count] (past target date, not complete)

**Burn-Down Chart** (visual):

- X-axis: Time (quarters)
- Y-axis: Open Gap Count
- Line showing gap closure trend

**Target Audience**: InfoSec Manager, Project Managers, CISO (progress monitoring)

**Time to Complete**: 1-2 hours per quarter (updating status, completion %)

## Section 5: Trend Analysis (Sheet 6)

**Purpose**: Track compliance improvement over time

**Content** (requires multiple assessment cycles):

**Compliance Score Trend**:
| Assessment Cycle | Overall Score | Inventory | Collection | Protection | Analysis | Delta |
|-----------------|---------------|-----------|------------|------------|----------|-------|
| Q1 2025 | 72% | 80% | 75% | 65% | 70% | - |
| Q2 2025 | 78% | 85% | 80% | 70% | 75% | +6% |
| Q3 2025 | 82% | 88% | 85% | 75% | 80% | +4% |
| Q4 2025 | 86% | 90% | 88% | 80% | 85% | +4% |
| **Q1 2026** | **89%** | **92%** | **90%** | **85%** | **88%** | **+3%** |

**Trend Indicators**:

- Improving: Score increasing quarter-over-quarter (^ Green)
- Stable: Score +/-2% (-> Yellow)
- Declining: Score decreasing (v Red)

**Gap Closure Trend**:
| Quarter | Gaps Opened | Gaps Closed | Net Change | Open Backlog |
|---------|-------------|-------------|------------|--------------|
| Q1 2025 | 35 | 0 | +35 | 35 |
| Q2 2025 | 8 | 12 | -4 | 31 |
| Q3 2025 | 5 | 15 | -10 | 21 |
| Q4 2025 | 3 | 10 | -7 | 14 |
| **Q1 2026** | **2** | **8** | **-6** | **8** |

**Target Audience**: CISO, Board (demonstrate continuous improvement)

**Time to Complete**: Automated (formulas compare current to previous cycles)

## Section 6: Evidence Summary (Sheet 7)

**Purpose**: Index all evidence supporting compliance assertions

**Content**:

**Evidence by Assessment**:
| Assessment | Evidence Count | Evidence Types | Last Updated |
|-----------|----------------|----------------|--------------|
| A.8.15.1 - Inventory | [count] | Screenshots, Exports, Reports | [date] |
| A.8.15.2 - Collection | [count] | Config Files, Metrics, Diagrams | [date] |
| A.8.15.3 - Protection | [count] | Test Results, Procedures, Logs | [date] |
| A.8.15.4 - Analysis | [count] | SOC Reports, Use Cases, Metrics | [date] |

**Evidence Location**:

- Assessment workbooks (embedded evidence references)
- Evidence folders (network path or SharePoint)
- Evidence retention: 7 years (per policy Section 2.3)

**Audit Readiness Check**:

- [ ] All evidence indexed in source assessments
- [ ] Evidence accessible to auditors
- [ ] Evidence current (within last 12 months)
- [ ] Evidence complete (no missing items)

**Target Audience**: Compliance Team, Internal Audit, External Auditors

**Time to Complete**: Automated (extracts evidence counts from source assessments)

---

# Gap Prioritization Methodology

## Cross-Domain Risk Scoring

**Why Re-Score Gaps?**

- Source assessments score gaps within their domain
- Dashboard re-scores gaps considering cross-domain impact
- Example: "No WORM storage" (from Protection assessment) also impacts Analysis (if logs can be deleted, investigations fail)

**Cross-Domain Impact Examples**:

**Gap: "No centralized logging for critical systems" (from Collection)**

- Collection Impact: High (logs scattered, hard to analyze)
- Protection Impact: High (local logs easily deleted)
- Analysis Impact: Critical (cannot investigate without centralized logs)
- **Cross-Domain Priority**: CRITICAL (affects 3 domains)

**Gap: "Alert false positive rate 15%" (from Analysis)**

- Collection Impact: None
- Protection Impact: None
- Analysis Impact: Medium (alert fatigue, but manageable)
- **Cross-Domain Priority**: MEDIUM (single domain only)

## Remediation Prioritization Matrix

**Quick Wins** (Low Effort, High Impact):

- Prioritize first (immediate ROI)
- Examples: Enable existing SIEM use cases, tune high-FP alerts, document procedures

**Strategic Projects** (High Effort, High Impact):

- Plan and resource (important but time-consuming)
- Examples: Deploy SOAR platform, implement WORM storage, build threat hunting program

**Fill-Ins** (Low Effort, Low Impact):

- Do when time permits (nice-to-have)
- Examples: Update documentation, minor config changes, cosmetic improvements

**Reconsider** (High Effort, Low Impact):

- Deprioritize or cancel (poor ROI)
- Examples: Custom integrations for low-value data, over-engineered solutions

---

# Executive Presentation

## One-Page Executive Summary Template

**Recommended Structure**:

---

**EXECUTIVE SUMMARY: ISO 27001 Control A.8.15 - Logging Compliance**  
**Period**: Q1 2026  
**Assessment Date**: January 2026  
**Prepared By**: [InfoSec Manager]  
**Presented To**: CISO / Board of Directors  

**OVERALL COMPLIANCE: [XX%]** [*Green/Yellow/Red]

**What We Assessed**:

- Log Source Inventory ([Organization]'s logging coverage)
- Log Collection & Centralization (SIEM effectiveness)
- Log Protection & Retention (tamper-proofing, retention compliance)
- Log Analysis & Review (SOC effectiveness, threat detection)

**Key Strengths**:
1. [Top strength from assessments]
2. [Second strength]
3. [Third strength]

**Key Gaps** (Highest Priority):
1. [Most critical gap] - **Risk**: [business impact] - **Action**: [remediation plan] - **Target**: [date]
2. [Second gap] - **Risk**: [impact] - **Action**: [plan] - **Target**: [date]
3. [Third gap] - **Risk**: [impact] - **Action**: [plan] - **Target**: [date]

**Progress Since Last Assessment**:

- Compliance improved from [XX%] to [XX%] (+X%)
- Closed [X] gaps, opened [X] new gaps
- On track to achieve >=85% compliance by [target quarter]

**Recommendations for CISO**:
1. [Top recommendation - usually highest-priority gap remediation]
2. [Second recommendation - often resource allocation or strategic investment]
3. [Third recommendation - process improvement or capability development]

**Next Steps**:

- Remediation initiatives tracked in [Jira/ServiceNow]
- Quarterly review scheduled for [next quarter]
- Full reassessment in [12 months from now]

---

## Board Presentation Tips

**Keep It Simple**:

- Board wants "Are we compliant?" (yes/no, percentage)
- Use traffic lights (Green/Yellow/Red), not detailed scores
- 5-minute presentation, 10 slides maximum

**Focus on Risk**:

- "What could go wrong?" (business impact of gaps)
- "What are we doing about it?" (remediation plans)
- "When will it be fixed?" (target dates)

**Show Progress**:

- Trend graph (compliance improving over time)
- Gap closure rate (we're making progress)
- Investment ROI (security spend effectiveness)

---

# Common Pitfalls

## Pitfall: "Averaging all scores equally"

**Problem**: Not all domains equally important

**Reality**: Analysis (30%) more important than Inventory (20%) for overall security value

**Solution**: Use weighted average (as specified in Section 4.2)

## Pitfall: "Green dashboard, but critical gaps ignored"

**Problem**: Focusing on overall score, ignoring specific critical gaps

**Reality**: 85% overall compliance looks good, but "no ransomware detection" is critical

**Solution**: Dashboard highlights critical gaps separately, regardless of overall score

## Pitfall: "Dashboard updated once, never again"

**Problem**: Dashboard becomes stale, doesn't reflect current state

**Reality**: Compliance is continuous, not point-in-time

**Solution**: Quarterly updates (minimum), track trends

---

# Quality Checklist

**Before Presenting Dashboard**:

- [ ] All 4 source assessments complete and approved
- [ ] External workbook links functional
- [ ] Compliance scores calculated correctly
- [ ] Gaps consolidated (no duplicates)
- [ ] Gap prioritization re-scored (cross-domain perspective)
- [ ] Executive summary written (1-page, narrative)
- [ ] Trend analysis complete (if previous cycles available)
- [ ] Evidence summary accurate
- [ ] CISO reviewed and approved
- [ ] Board presentation prepared (if required)

---

**END OF PART I**

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook Developers (Python/Excel script maintainers)

---

# Workbook Structure Overview

| Sheet # | Sheet Name | Purpose | User Input | Formula-Driven | Protected |
|---------|------------|---------|------------|----------------|-----------|
| 1 | Instructions | Usage guide | No | No | Yes |
| 2 | Executive_Summary | One-page summary for CISO/Board | Yes (narrative) | Yes (scores) | Partial |
| 3 | Compliance_Scorecard | Detailed scores by domain | No | Yes (external refs) | Yes |
| 4 | Gap_Consolidation | All gaps prioritized | Partial | Yes (auto-populated) | Partial |
| 5 | Remediation_Tracking | Gap closure progress | Yes | Yes (metrics) | Partial |
| 6 | Trend_Analysis | Multi-cycle comparison | No | Yes (historical data) | Yes |
| 7 | Evidence_Summary | Evidence index | No | Yes (from source assessments) | Yes |

**Total Sheets**: 7 (smaller than assessment workbooks - consolidation focus)

---

# Sheet Specifications

## Sheet 1: Instructions

**Content**:

- Dashboard purpose and scope
- How to use dashboard (navigation, interpretation)
- External workbook dependency notice
- Update frequency (quarterly recommended)
- Contact information (InfoSec Manager)

---

## Sheet 2: Executive_Summary

**Section 1: Overall Compliance** (Rows 4-10)

- Large, color-coded cell with Overall Compliance Score
- Formula: `=(0.20 x Inventory_Score) + (0.25 x Collection_Score) + (0.25 x Protection_Score) + (0.30 x Analysis_Score)`
- Conditional Formatting:
  - Green: >=85%
  - Yellow: 70-84%
  - Orange: 50-69%
  - Red: <50%

**Section 2: Compliance by Domain** (Rows 12-20)
| Domain | Score | Target | Status | Trend |
|--------|-------|--------|--------|-------|
| A.8.15.1 - Inventory | `='[IMP-A.8.15.1...xlsx]Approval_Sign_Off'!B10` | >=90% | `=IF(Score>=Target,"Y","N")` | `=IF(Score>Previous,"^","v")` |
| A.8.15.2 - Collection | `='[IMP-A.8.15.2...xlsx]Approval_Sign_Off'!B11` | >=95% | `=IF...` | `=IF...` |
| A.8.15.3 - Protection | `='[IMP-A.8.15.3...xlsx]Approval_Sign_Off'!B12` | >=95% | `=IF...` | `=IF...` |
| A.8.15.4 - Analysis | `='[IMP-A.8.15.4...xlsx]Approval_Sign_Off'!B13` | >=80% | `=IF...` | `=IF...` |

**Section 3: Key Findings** (Rows 23-45)

- **Top 3 Strengths** (user-written narrative, 2-3 sentences each)
- **Top 3 Gaps** (user-written narrative, extracted from Gap Consolidation sheet)
- **Top 3 Recommendations** (user-written narrative, actionable for CISO)

**Section 4: Assessment Metadata** (Rows 48-55)

- Assessment Period: [Q1 2026]
- Assessment Dates: [Jan 2026]
- Assessments Included: 4 (A.8.15.1, .2, .3, .4)
- Total Gaps Identified: `=COUNT(Gap_Consolidation!A:A)`
- Critical Gaps: `=COUNTIF(Gap_Consolidation!Risk,"CRITICAL")`
- Next Review Date: [Q2 2026]

---

## Sheet 3: Compliance_Scorecard

**CRITICAL: All scores use external workbook references**

**Column Structure** (10 columns):

- A: Domain (A.8.15.1, A.8.15.2, A.8.15.3, A.8.15.4, Overall)
- B: Domain Name (Inventory, Collection, Protection, Analysis, Overall Control A.8.15)
- C: Compliance Score (%) - External Reference
- D: Target (%)
- E: Status (Y/N) - Formula: `=IF(C>=D,"Y","N")`
- F: Gap Count - External Reference
- G: Critical Gaps - External Reference
- H: Last Assessment Date - External Reference
- I: Trend vs. Previous (^v->) - Formula comparing to previous cycle
- J: Notes (user-entered observations)

**External Reference Examples**:

**For A.8.15.1 (Inventory)**:
```
=  '[ISMS_A_8_15_1_Log_Source_Inventory_Assessment_YYYYMMDD.xlsx]Approval_Sign_Off'!$B$10
```

**For A.8.15.2 (Collection)**:
```
='[ISMS_A_8_15_2_Log_Collection_Centralization_Assessment_YYYYMMDD.xlsx]Approval_Sign_Off'!$B$11
```

**For A.8.15.3 (Protection)**:
```
='[ISMS_A_8_15_3_Log_Protection_Retention_Assessment_YYYYMMDD.xlsx]Approval_Sign_Off'!$B$12
```

**For A.8.15.4 (Analysis)**:
```
='[ISMS_A_8_15_4_Log_Analysis_Review_Assessment_YYYYMMDD.xlsx]Approval_Sign_Off'!$B$13
```

**Overall Score Formula**:
```
=(A.8.15.1_Score * 0.20) + (A.8.15.2_Score * 0.25) + (A.8.15.3_Score * 0.25) + (A.8.15.4_Score * 0.30)
```

**Weighting Rationale**:

- **Inventory (20%)**: Foundation - need to know what systems exist, but less critical than actual security measures
- **Collection (25%)**: Critical - logs must be centralized for analysis and protection
- **Protection (25%)**: Critical - logs must be tamper-proof to be credible evidence
- **Analysis (30%)**: Most critical - logs provide no security value if not analyzed

---

## Sheet 4: Gap_Consolidation

**Purpose**: Extract all gaps from 4 source assessments, consolidate, re-prioritize

**Column Structure** (22 columns):

- A: Gap ID (CONS-001, CONS-002...)
- B: Source Assessment (A.8.15.1, .2, .3, .4)
- C: Source Gap ID (original gap ID from source assessment)
- D: Domain (Inventory, Collection, Protection, Analysis)
- E: Gap Description (imported from source assessment)
- F: Affected System/Process (imported)
- G: Policy Reference (ISMS-POL-A.8.15 Section X.X)
- H: Original Risk Rating (from source assessment)
- I: Cross-Domain Impact Assessment:
  - Does gap affect multiple domains? (Yes/No)
  - Which domains affected? (checkboxes or dropdown)
- J: Re-Scored Risk Rating (may differ from original if cross-domain impact)
- K: Impact (1-5)
- L: Likelihood (1-5)
- M: Detectability (1-5 - inverted: 5=blind spot)
- N: Remediation Effort (1-5)
- O: Priority Score = `(K x L x M) / N`
- P: Business Impact (narrative)
- Q: Remediation Plan (from source assessment)
- R: Responsible Party
- S: Target Completion Date
- T: Status (Open, In Progress, Resolved, Deferred)
- U: Tracking Ticket (Jira, ServiceNow ID)
- V: Notes

**Gap Import Logic** (Python script):
```python
# Import gaps from A.8.15.1
import_gaps_from_workbook(
    source_wb='ISMS_A_8_15_1_..._YYYYMMDD.xlsx',
    source_sheet='Gap_Analysis',
    domain='Inventory'
)

# Import from A.8.15.2, .3, .4
# repeat for each assessment
```

**Deduplication Logic**:

- Check for duplicate gaps (same description across multiple assessments)
- If duplicate found, keep highest-severity instance, note in "Cross-Domain Impact"
- Example: "No centralized logging" appears in both Collection and Protection -> consolidate with cross-domain flag

**Re-Prioritization**:

- Gaps affecting multiple domains get higher priority score
- User can manually adjust Impact/Likelihood/Detectability if cross-domain perspective changes assessment

**Gap Summary Table** (Below main gap list):
| Domain | Total | Critical | High | Medium | Low | % Closed |
|--------|-------|----------|------|--------|-----|----------|
| Inventory | COUNT | COUNTIFS | ... | ... | ... | Closed/Total% |
| Collection | ... | ... | ... | ... | ... | ... |
| Protection | ... | ... | ... | ... | ... | ... |
| Analysis | ... | ... | ... | ... | ... | ... |
| **Total** | **SUM** | **SUM** | **SUM** | **SUM** | **SUM** | **Avg%** |

---

## Sheet 5: Remediation_Tracking

**Purpose**: Track gap remediation progress

**Column Structure** (14 columns):

- A: Initiative ID (linked to Gap ID)
- B: Initiative Name
- C: Gap(s) Addressed (may fix multiple gaps)
- D: Responsible Party (owner)
- E: Team (which team executing - SOC, IT Ops, InfoSec, etc.)
- F: Start Date
- G: Target Completion Date
- H: Actual Completion Date
- I: Status (Not Started, In Progress, Blocked, Completed)
- J: % Complete (0-100%) - user-entered
- K: Budget Allocated (if applicable)
- L: Budget Spent (if tracking costs)
- M: Blockers/Issues (what's preventing progress)
- N: Last Update Date

**Remediation Metrics** (Summary section):

- Total Initiatives: `COUNTA(A:A) - 1`
- Completed: `COUNTIF(I:I,"Completed")`
- In Progress: `COUNTIF(I:I,"In Progress")`
- Not Started: `COUNTIF(I:I,"Not Started")`
- Blocked: `COUNTIF(I:I,"Blocked")`
- % Complete (avg): `AVERAGE(J:J)`

**Status Analysis**:

- On Track: `COUNTIF` initiatives where Target Date > TODAY() AND Status != "Blocked"
- At Risk: `COUNTIF` where Target Date < TODAY() + 30 days AND Status != "Completed"
- Overdue: `COUNTIF` where Target Date < TODAY() AND Status != "Completed"

**Burn-Down Chart** (conditional on historical data):

- X-axis: Quarter (Q1, Q2, Q3, Q4)
- Y-axis: Open Gap Count
- Line showing gap count over time (should trend downward)

---

## Sheet 6: Trend_Analysis

**Purpose**: Track compliance improvement over multiple assessment cycles

**CRITICAL**: Requires multiple assessment cycles (historical data)

**Table Structure**:

| Cycle | Assessment Date | Overall Score | Inventory | Collection | Protection | Analysis | Delta | Gaps Opened | Gaps Closed | Net Gap Change | Open Backlog |
|-------|----------------|---------------|-----------|------------|------------|----------|-------|-------------|-------------|----------------|--------------|
| Q1 2025 | Jan 2025 | 72% | 80% | 75% | 65% | 70% | - | 35 | 0 | +35 | 35 |
| Q2 2025 | Apr 2025 | 78% | 85% | 80% | 70% | 75% | +6% | 8 | 12 | -4 | 31 |
| Q3 2025 | Jul 2025 | 82% | 88% | 85% | 75% | 80% | +4% | 5 | 15 | -10 | 21 |
| Q4 2025 | Oct 2025 | 86% | 90% | 88% | 80% | 85% | +4% | 3 | 10 | -7 | 14 |
| **Current** | **Jan 2026** | **89%** | **92%** | **90%** | **85%** | **88%** | **+3%** | **2** | **8** | **-6** | **8** |

**Trend Calculations**:

- Delta = Current_Score - Previous_Score
- Trend Indicator:
  - ^ (Improving): Delta > +2%
  - -> (Stable): Delta between -2% and +2%
  - v (Declining): Delta < -2%

**Trend Graphs** (recommended visualizations):
1. **Compliance Score Line Graph**: All 5 scores (Overall + 4 domains) over time
2. **Gap Count Bar Chart**: Gaps opened vs. closed per quarter
3. **Open Backlog Line Graph**: Total open gaps trending over time

**First-Time Assessment**:

- If this is the first assessment cycle, Sheet 6 will show "Insufficient data for trend analysis"
- User should enter current cycle as "Baseline"
- Future assessments will enable trend tracking

---

## Sheet 7: Evidence_Summary

**Purpose**: Index all evidence across all assessments

**Content**:

**Evidence Count by Assessment**:
| Assessment | Evidence Count | Last Updated |
|-----------|----------------|--------------|
| A.8.15.1 - Inventory | `=COUNTA('[IMP-A.8.15.1...xlsx]Evidence_Register'!A:A) - 1` | `='[...]'!H2` |
| A.8.15.2 - Collection | `=COUNTA('[IMP-A.8.15.2...xlsx]Evidence_Register'!A:A) - 1` | ... |
| A.8.15.3 - Protection | `=COUNTA('[IMP-A.8.15.3...xlsx]Evidence_Register'!A:A) - 1` | ... |
| A.8.15.4 - Analysis | `=COUNTA('[IMP-A.8.15.4...xlsx]Evidence_Register'!A:A) - 1` | ... |
| **Total** | **SUM** | **N/A** |

**Evidence Location Information**:

- Source Assessment Workbooks (paths)
- Evidence Folders (network paths or SharePoint URLs)
- Evidence Retention Period: 7 years (per ISMS-POL-A.8.15 Section 2.3)

**Audit Readiness Checklist**:

- [ ] All source assessments approved (Level 3 sign-off)
- [ ] Evidence indexed in source assessments
- [ ] Evidence accessible (file paths valid, permissions granted)
- [ ] Evidence current (within last 12 months)
- [ ] Evidence complete (no missing items flagged in assessments)

**Audit Trail**:

- Dashboard Creation Date: [auto-populated]
- Dashboard Last Updated: [auto-updated on save]
- Updated By: [user-entered]
- Next Review Date: [user-entered - typically +3 months]

---

# Integration Points

## External Workbook References

**CRITICAL**: Dashboard relies on external references to all 4 source assessments

**Source Workbooks**:
1. **ISMS_A_8_15_1_Log_Source_Inventory_Assessment_YYYYMMDD.xlsx**

   - Sheet: `Approval_Sign_Off`
   - Cells Referenced: Overall compliance score, gap count, critical gaps
   - Sheet: `Gap_Analysis`
   - Cells Referenced: All gap rows (for consolidation)

2. **ISMS_A_8_15_2_Log_Collection_Centralization_Assessment_YYYYMMDD.xlsx**

   - Sheet: `Approval_Sign_Off`
   - Cells Referenced: Overall compliance score, gap count
   - Sheet: `Gap_Analysis`
   - Cells Referenced: All gap rows

3. **ISMS_A_8_15_3_Log_Protection_Retention_Assessment_YYYYMMDD.xlsx**

   - Sheet: `Approval_Sign_Off`
   - Cells Referenced: Overall compliance score, gap count
   - Sheet: `Gap_Analysis`
   - Cells Referenced: All gap rows

4. **ISMS_A_8_15_4_Log_Analysis_Review_Assessment_YYYYMMDD.xlsx**

   - Sheet: `Approval_Sign_Off`
   - Cells Referenced: Overall compliance score, gap count
   - Sheet: `Gap_Analysis`
   - Cells Referenced: All gap rows

**File Path Configuration**:

- Python script must be customized with actual file paths
- Paths can be absolute (`C:\...`) or relative (`.\Assessments\...`)
- SharePoint URLs supported (if using Excel Online or OneDrive)

**Link Maintenance**:

- If source workbooks moved, links break -> manual update required
- Recommendation: Store all assessment workbooks in single folder
- Use relative paths for portability

---

# Python Script Usage

## Script Name
`generate_a815_5_compliance_dashboard.py`

## CRITICAL Customization Points

**Line 20-50: Source Workbook Paths**
```python
# CUSTOMIZE: Paths to source assessment workbooks
SOURCE_WORKBOOKS = {
    'A.8.15.1': 'ISMS_A_8_15_1_Log_Source_Inventory_Assessment_20260121.xlsx',
    'A.8.15.2': 'ISMS_A_8_15_2_Log_Collection_Centralization_Assessment_20260121.xlsx',
    'A.8.15.3': 'ISMS_A_8_15_3_Log_Protection_Retention_Assessment_20260121.xlsx',
    'A.8.15.4': 'ISMS_A_8_15_4_Log_Analysis_Review_Assessment_20260121.xlsx'
}

# CUSTOMIZE: Folder location (if all in same directory)
ASSESSMENT_FOLDER = './ISMS_A_8_15_Assessments/'
# Or use absolute paths, SharePoint URLs, etc.
```

**Line 100-120: Compliance Score Weighting**
```python
# CUSTOMIZE: Weighting for overall compliance score
# Default: Analysis most important (30%), Inventory least (20%)
WEIGHTS = {
    'Inventory': 0.20,
    'Collection': 0.25,
    'Protection': 0.25,
    'Analysis': 0.30
}
# Must sum to 1.0
assert sum(WEIGHTS.values()) == 1.0
```

**Line 200-250: External Reference Generation**
```python
# Generate external workbook references
def create_external_ref(workbook_name, sheet_name, cell_ref):
    """
    Creates Excel external reference formula
    Example: ='[Workbook.xlsx]Sheet'!A1
    """
    return f"='[{workbook_name}]{sheet_name}'!{cell_ref}"

# Apply to Compliance_Scorecard sheet
scorecard_sheet['C2'] = create_external_ref(
    SOURCE_WORKBOOKS['A.8.15.1'],
    'Approval_Sign_Off',
    '$B$10'  # Overall score cell in source workbook
)
```

**Line 300-400: Gap Consolidation Logic**
```python
# Import gaps from all 4 assessments
def consolidate_gaps():
    """
    Reads Gap_Analysis sheet from each source workbook
    Deduplicates, re-prioritizes, consolidates into single list
    """
    all_gaps = []
    
    for domain, wb_path in SOURCE_WORKBOOKS.items():
        source_wb = load_workbook(wb_path, data_only=True)
        gap_sheet = source_wb['Gap_Analysis']
        
        for row in gap_sheet.iter_rows(min_row=2, values_only=True):
            gap = {
                'source_assessment': domain,
                'gap_id': row[0],
                'description': row[1],
                'risk_rating': row[2],
                # ... extract all gap fields
            }
            all_gaps.append(gap)
    
    # Deduplicate (check for duplicate descriptions)
    unique_gaps = remove_duplicates(all_gaps)
    
    # Re-prioritize (cross-domain scoring)
    prioritized_gaps = re_score_gaps(unique_gaps)
    
    return prioritized_gaps
```

## Key Functions

1. `create_workbook()`: Initialize 7-sheet dashboard structure
2. `import_source_assessments()`: Validate all 4 source workbooks exist and are approved
3. `generate_external_references()`: Create all external workbook formulas
4. `consolidate_gaps()`: Import and deduplicate gaps from all sources
5. `calculate_compliance_scores()`: Weighted average of domain scores
6. `generate_trend_analysis()`: Compare to previous cycles (if historical data available)
7. `apply_conditional_formatting()`: Traffic lights, trend arrows
8. `protect_cells()`: Lock formula cells, allow user input cells

## Testing Checklist

- [ ] All 4 source workbooks exist at specified paths
- [ ] External references pulling data correctly
- [ ] Overall compliance score calculates accurately (weighted average)
- [ ] Gaps consolidated without duplicates
- [ ] Gap prioritization scores calculate correctly
- [ ] Trend analysis works (if historical data available)
- [ ] Conditional formatting triggers properly (Green/Yellow/Red)
- [ ] Executive summary narrative sections editable (not locked)
- [ ] Cell protection appropriate (formulas locked, inputs unlocked)

## Error Handling

**Missing Source Workbook**:
```python
try:
    source_wb = load_workbook(wb_path)
except FileNotFoundError:
    print(f"ERROR: Source workbook not found: {wb_path}")
    print("Dashboard cannot be generated without all 4 source assessments.")
    sys.exit(1)
```

**Broken External Reference**:

- If source workbook moved after dashboard creation, external refs show #REF! error
- User must manually update file paths in formulas, or
- Re-run Python script with updated paths

**Unapproved Source Assessment**:
```python
# Check approval status in source workbook
approval_status = source_wb['Approval_Sign_Off']['B50'].value
if approval_status != "APPROVED":
    print(f"WARNING: {wb_path} not yet approved (status: {approval_status})")
    print("Dashboard data may be preliminary/incomplete.")
```

---

# Document Assembly Complete

**Total Document Length**: ~950 lines

**Structure**:

- Part I: User Completion Guide (~550 lines)
- Part II: Technical Specification (~400 lines)

**Quality Verification**:

- [X] Consolidates all 4 assessments (A.8.15.1, .2, .3, .4)
- [X] External workbook references specified
- [X] Weighted compliance scoring (Inventory 20%, Collection 25%, Protection 25%, Analysis 30%)
- [X] Cross-domain gap prioritization methodology
- [X] Trend analysis capability (multi-cycle comparison)
- [X] Executive summary (1-page for Board/CISO)
- [X] Remediation tracking
- [X] Evidence summary/audit readiness
- [X] Generic language maintained
- [X] Consistent with IMP-A.8.15.1/.2/.3/.4 structure

---

**END OF ISMS-IMP-A.8.15.5 COMPLIANCE DASHBOARD DOCUMENT**

---

*This compliance dashboard consolidates Control A.8.15 implementation evidence across all four assessment domains (Inventory, Collection, Protection, Analysis) into a single executive view. Dashboard provides objective evidence for ISO 27001 audit validation, Board reporting, and continuous monitoring of logging compliance posture.*

**Ready for Production Use**

---

**END OF SPECIFICATION**

---

*"Sometimes it is the people no one imagines anything of who do the things that no one can imagine."*
- Alan Turing

<!-- QA_VERIFIED: 2026-02-01 -->
