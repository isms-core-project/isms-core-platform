<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.15.5-UG:framework:UG:a.8.15.5 -->
**ISMS-IMP-A.8.15.5-UG - Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.5-UG |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.15.5-TG.

---

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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
