**ISMS-IMP-A.8.32.5 - Compliance Summary Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.32.5 |
| **Version** | 1.0 |
| **Assessment Area** | Compliance Dashboard & Consolidation |
| **Related Policy** | ISMS-POL-A.8.32 (All Sections) |
| **Purpose** | Consolidate all domain assessments into executive compliance view with scoring, gap analysis, and audit readiness certification |
| **Target Audience** | CISO, Executive Management, Board of Directors, Internal/External Auditors, ISO 27001 Certification Bodies, Workbook Developers |
| **Assessment Type** | Executive Dashboard & Consolidation |
| **Review Cycle** | Quarterly (synchronized with domain assessments) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial technical specification for Change Management Compliance Dashboard workbook | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Dashboard Overview
  - Prerequisites (Critical: Requires Assessments 1-4)
  - Dashboard Generation Workflow
  - Understanding Dashboard Sections
  - Executive Reporting
  - Compliance Scoring Methodology
  - Gap Prioritization
  - CISO Certification Process
  - Quality Checklist

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formulas & Calculations
  - Dashboard Design
  - Integration with Source Workbooks


**Target Audiences:**

- **Part I:** Dashboard users (CISO, Executive Management, Auditors)
- **Part II:** Workbook developers (Python/Excel script maintainers)


---

# PART I: USER COMPLETION GUIDE

**Audience:** CISO, Executive Management, Board of Directors, Auditors

---

## Dashboard Overview

### What This Dashboard Provides

This is the **MASTER DASHBOARD** that consolidates all four domain assessments (IMP-A.8.32.1 through IMP-A.8.32.4) into a single executive compliance view.

**Key Difference from Other Assessments:**

- IMP-A.8.32.1-4: Data entry assessments (you complete them)
- IMP-A.8.32.5: **Consolidation dashboard** (reads FROM other assessments)


This dashboard does NOT require new data entry - it pulls data from completed assessments and presents it for executive decision-making.

### What You'll See

**Executive Summary:**

- Overall change management compliance percentage
- Compliance by domain (Process, Classification, Environment, Testing)
- Trend analysis (improving, stable, declining)
- Audit readiness assessment


**Gap Analysis:**

- Critical gaps requiring immediate attention
- High-priority issues with remediation plans
- Risk exposure from non-compliance


**Risk Register:**

- Change management risks identified
- Risk severity and mitigation status
- Risk acceptance tracking


**Remediation Roadmap:**

- Gap closure timeline
- Responsible parties
- Progress tracking


**KPIs & Metrics:**

- Change volume trends
- Change success rate
- Emergency change percentage
- Testing coverage
- Audit readiness indicators


**Evidence Register:**

- Evidence completeness across all domains
- Audit trail availability


**CISO Certification:**

- Formal attestation of compliance status
- Risk acceptance for identified gaps
- Audit readiness declaration


---

## Prerequisites

### CRITICAL: Complete Source Assessments First

**This dashboard REQUIRES all four source assessments to be completed:**

**Required Source Workbooks:**

- [ ] ? ISMS-IMP-A.8.32.1 - Change Process Assessment (COMPLETED)
- [ ] ? ISMS-IMP-A.8.32.2 - Change Types & Categories (COMPLETED)
- [ ] ? ISMS-IMP-A.8.32.3 - Environment Separation (COMPLETED)
- [ ] ? ISMS-IMP-A.8.32.4 - Testing & Validation (COMPLETED)


**Verification Checklist:**

- [ ] All source workbooks have "Final" status (not Draft)
- [ ] All source workbooks approved by domain owners
- [ ] All source workbooks dated within last quarter
- [ ] Source workbooks in same directory as dashboard


**If Source Assessments Not Complete:**
You cannot generate meaningful dashboard. Complete assessments 1-4 first, then return to dashboard generation.

### Before Starting Dashboard

**Required:**

- [ ] All 4 source assessments completed and approved
- [ ] Source workbook files accessible
- [ ] Python dashboard generation script available
- [ ] Understand dashboard interpretation (read this guide)


**Recommended:**

- [ ] Review source assessments for critical gaps
- [ ] Prepare executive briefing materials
- [ ] Schedule CISO certification review
- [ ] Identify stakeholders for dashboard distribution


### Who Uses This Dashboard

**Primary Users:**

- **CISO:** Overall compliance oversight, risk acceptance, certification
- **Executive Management:** Strategic decision-making, investment prioritization
- **Board of Directors:** Governance oversight, risk exposure understanding


**Secondary Users:**

- **Internal Audit:** Audit planning, control assessment
- **External Auditors:** ISO 27001 certification, compliance verification
- **Compliance Officers:** Regulatory compliance tracking


**Contributors:**

- **Change Manager:** Provide context for findings, remediation plans
- **Domain Assessment Owners:** Validate data accuracy


---

## Dashboard Generation Workflow

### Step-by-Step Process

**Step 1: Verify Prerequisites (Day 1)**

- Confirm all 4 source assessments completed
- Verify all source workbooks have "Final" status
- Check all approvals obtained
- Ensure files in correct directory


**Step 2: Generate Dashboard (Day 1)**

- Run Python dashboard generation script
- Script reads from source workbooks
- Dashboard workbook created with formulas
- Verify dashboard calculations accurate


**Step 3: Validate Data Integrity (Day 2)**

- Review Executive Dashboard sheet for accuracy
- Verify compliance percentages match source data
- Check gap analysis completeness
- Validate risk register consolidation


**Step 4: Gap Analysis Review (Day 3)**

- Review critical gaps identified
- Assess gap severity and business impact
- Identify quick wins vs long-term remediation
- Prioritize gaps for remediation


**Step 5: Risk Assessment (Day 4)**

- Review change management risks
- Assess risk severity (likelihood x impact)
- Identify risk mitigation strategies
- Document risk acceptance decisions


**Step 6: Remediation Planning (Day 5)**

- Develop remediation roadmap
- Assign gap owners
- Set target closure dates
- Estimate resource requirements


**Step 7: Executive Summary Preparation (Days 6-7)**

- Prepare executive briefing deck
- Highlight key findings and recommendations
- Document investment needs
- Prepare audit readiness statement


**Step 8: CISO Review & Certification (Days 8-10)**

- CISO reviews complete dashboard
- CISO certifies compliance status
- CISO accepts residual risks
- CISO signs audit readiness declaration


**Step 9: Executive Presentation (Days 11-12)**

- Present dashboard to executive leadership
- Discuss critical gaps and remediation
- Obtain investment approvals
- Document executive decisions


**Step 10: Dashboard Distribution (Day 13)**

- Distribute dashboard to stakeholders
- File in document repository
- Schedule next quarterly review
- Set reminders for gap remediation milestones


**Total Duration:** 2-3 weeks from source completion to executive presentation

---

## Understanding Dashboard Sections

### Sheet 1: Executive_Dashboard

**What it shows:**

- Overall compliance percentage across all domains
- Compliance by domain (Process, Classification, Environment, Testing)
- Critical gaps count
- Audit readiness status


**How to interpret:**

- **90-100%**: Fully compliant - ready for audit
- **70-89%**: Substantially compliant - minor gaps, audit-ready with caveats
- **50-69%**: Partially compliant - significant gaps, remediation required before audit
- **<50%**: Non-compliant - major deficiencies, not audit-ready


**Key Questions to Ask:**

- Which domain has lowest compliance? (Focus remediation there)
- Are we trending up or down from last quarter?
- Are critical gaps decreasing?


### Sheet 2: Gap_Analysis

**What it shows:**

- All gaps identified across 4 assessments
- Gap severity (Critical, High, Medium, Low)
- Gap status (Open, In Progress, Closed)
- Assigned owners and target dates


**How to interpret:**

- **Critical gaps:** Must remediate before audit (typically <30 days)
- **High gaps:** Should remediate soon (30-90 days)
- **Medium gaps:** Plan remediation (90-180 days)
- **Low gaps:** Continuous improvement (>180 days)


**Key Questions to Ask:**

- How many critical gaps? (Target: zero before audit)
- Are gaps being closed or accumulating?
- Do we have resources assigned to gap remediation?


### Sheet 3: Risk_Register

**What it shows:**

- Change management risks identified
- Risk level (Critical, High, Medium, Low)
- Risk mitigation status
- Risk acceptance records


**How to interpret:**

- Risks WITH mitigation = acceptable residual risk
- Risks WITHOUT mitigation = unacceptable exposure
- Accepted risks = CISO formally accepted residual risk


**Key Questions to Ask:**

- What's our highest risk? (Focus mitigation there)
- Have all high risks been formally accepted or mitigated?
- Are risk mitigations actually implemented?


### Sheet 4: Remediation_Roadmap

**What it shows:**

- Timeline for gap closure
- Milestones and dependencies
- Resource requirements
- Progress tracking


**How to interpret:**

- Roadmap shows path to full compliance
- Dates should be realistic (not "next month" for everything)
- Resources must be allocated (not just "TBD")


**Key Questions to Ask:**

- Is roadmap realistic given our resources?
- Are dependencies identified and managed?
- What's blocking progress on overdue items?


### Sheet 5: KPIs_Metrics

**What it shows:**

- Key performance indicators for change management
- Trends over time (quarterly comparison)
- Target vs actual performance
- Leading and lagging indicators


**Key Metrics:**

- **Change Volume:** Total changes per quarter
- **Change Success Rate:** % changes successful (target: >95%)
- **Emergency Change %:** % emergency changes (target: <5%)
- **Testing Coverage:** % changes tested before prod (target: >90%)
- **PIR Completion Rate:** % changes with PIR (target: >90% for emergency)
- **Compliance %:** Overall compliance (target: >90%)


**How to interpret:**

- Green: Meeting targets
- Yellow: Close to target, watch closely
- Red: Missing targets, action required


**Key Questions to Ask:**

- Are we improving over time?
- Which metrics are declining? (Investigate root cause)
- Do we have right targets set?


### Sheet 6: Evidence_Register

**What it shows:**

- Evidence availability across all domains
- Evidence completeness percentage
- Evidence location and accessibility


**How to interpret:**

- 100% evidence = audit-ready
- <90% evidence = audit risk


**Key Questions to Ask:**

- Is all evidence accessible to auditors?
- Is evidence current (<6 months old)?
- Do we have evidence for critical controls?


### Sheet 7: Audit_Readiness

**What it shows:**

- Audit readiness assessment
- Requirements met vs outstanding
- Evidence completeness
- CISO certification status


**How to interpret:**

- **Audit Ready:** All criteria met, evidence complete, CISO certified
- **Audit Ready with Caveats:** Minor gaps documented and accepted
- **Not Audit Ready:** Critical gaps or missing evidence


**Key Questions to Ask:**

- What's blocking audit readiness?
- When will we be ready?
- What investments needed to achieve readiness?


### Sheet 8: CISO_Certification

**What it shows:**

- CISO formal attestation of compliance
- Risk acceptance for identified gaps
- Audit readiness declaration
- Certification date and signature


**How to interpret:**

- CISO certification is FORMAL statement to auditors/board
- CISO accepts accountability for residual risks
- Certification should only be given when CISO confident in compliance


**Key Questions to Ask:**

- Is CISO comfortable certifying?
- What risks is CISO accepting?
- What conditions apply to certification?


---

## Compliance Scoring Methodology

### How Compliance is Calculated

**Overall Compliance Percentage:**
```
Overall % = (Sum of all compliant items / Total assessable items) x 100
```

**Weighting by Domain:**
All domains weighted equally (25% each):

- Process (IMP-A.8.32.1): 25%
- Classification (IMP-A.8.32.2): 25%
- Environment (IMP-A.8.32.3): 25%
- Testing (IMP-A.8.32.4): 25%


**Status Scoring:**

- ? Fully Compliant: 100 points
- ? Partially Compliant: 50 points
- ? Non-Compliant: 0 points
- ? Planned: 25 points (partial credit for documented plan)
- N/A: Excluded from calculation


### Compliance Levels

| Level | Score Range | Interpretation | Audit Readiness |
|-------|-------------|----------------|-----------------|
| **Fully Compliant** | 90-100% | All requirements met, minor findings only | ? Ready |
| **Substantially Compliant** | 70-89% | Most requirements met, some gaps | ? Ready with caveats |
| **Partially Compliant** | 50-69% | Significant gaps, remediation required | ? Not ready |
| **Non-Compliant** | <50% | Major deficiencies, extensive remediation | ? Not ready |

---

## Gap Prioritization

### Gap Severity Matrix

**Critical Gaps** (Immediate attention required):

- Control completely missing (e.g., no test environment)
- Regulatory compliance violation (e.g., prod data in test unmasked)
- High security risk (e.g., developers can deploy to prod)
- Audit showstopper (e.g., no change records)


**High Gaps** (Remediate soon):

- Significant control weakness (e.g., no CAB)
- Incomplete procedures (e.g., no rollback procedures)
- Recurring failures (e.g., high emergency change %)
- Evidence gaps for key controls


**Medium Gaps** (Plan remediation):

- Process inefficiency (e.g., manual change management)
- Documentation gaps (e.g., no standard change catalog)
- Tool limitations (e.g., no automation)
- Training needs


**Low Gaps** (Continuous improvement):

- Process optimization opportunities
- Enhanced reporting
- Advanced automation
- Best practice adoption


### Prioritization Framework

**Step 1: Assess Impact**

- What's the risk if we don't fix this?
- Does this violate policy/regulations?
- Could this cause audit finding?


**Step 2: Assess Effort**

- How much effort to remediate? (days/weeks/months)
- What resources required? (people, budget, tools)
- Any dependencies?


**Step 3: Calculate Priority**

- High Impact + Low Effort = Quick Win (do immediately)
- High Impact + High Effort = Strategic Initiative (plan carefully)
- Low Impact + Low Effort = Easy Improvement (do when time permits)
- Low Impact + High Effort = Defer (may not be worth it)


---

## CISO Certification Process

### What CISO Certification Means

CISO certification is **FORMAL STATEMENT** to:

- Executive management: Change management controls are effective
- Board of Directors: Risk is appropriately managed
- Auditors: Organization ready for audit
- Regulators: Compliance requirements met


**CISO certifies:**
1. Assessment data is accurate
2. Identified gaps are understood and risk-accepted
3. Remediation plans are realistic and resourced
4. Residual risk is acceptable
5. Organization is (or is not) audit-ready

### When CISO Should NOT Certify

**Do NOT certify if:**

- Critical gaps without remediation plans
- Inaccurate or incomplete assessment data
- Unacceptable residual risk
- Missing evidence for key controls
- Not confident in audit readiness


**Instead:** Document reasons for non-certification, remediation requirements, timeline to certification

### Certification Process

**Step 1: Pre-Certification Review**

- CISO reviews complete dashboard
- Validates data accuracy with domain owners
- Reviews all critical gaps
- Assesses audit readiness


**Step 2: Risk Acceptance**

- CISO formally accepts residual risks
- Documents risk acceptance rationale
- Sets conditions for acceptance


**Step 3: Formal Certification**

- CISO signs certification statement
- Includes any caveats or conditions
- Sets certification validity period (typically 1 quarter)


**Step 4: Communication**

- Communicate certification to stakeholders
- File certification in governance records
- Schedule recertification (quarterly)


---

## Quality Checklist

### Before CISO Certification

**Data Integrity:**

- [ ] All source assessments have "Final" status
- [ ] All domain owners approved their assessments
- [ ] Dashboard formulas calculate correctly
- [ ] No obvious data errors or inconsistencies


**Gap Analysis:**

- [ ] All gaps documented with severity
- [ ] Gap owners assigned
- [ ] Target remediation dates set
- [ ] Critical gaps have remediation plans


**Risk Assessment:**

- [ ] All risks documented
- [ ] Risk severity assessed
- [ ] Mitigation strategies identified
- [ ] Risk acceptance documented where applicable


**Evidence:**

- [ ] Evidence completeness validated
- [ ] Evidence accessible to auditors
- [ ] Evidence current (<6 months)


**Remediation Roadmap:**

- [ ] Roadmap realistic and achievable
- [ ] Resources allocated
- [ ] Dependencies identified
- [ ] Progress tracking mechanisms in place


**KPIs:**

- [ ] Metrics tracked and trended
- [ ] Targets defined
- [ ] Performance against targets analyzed
- [ ] Declining metrics investigated


**Audit Readiness:**

- [ ] Audit readiness criteria assessed
- [ ] Compliance level determined
- [ ] Readiness statement prepared
- [ ] Any blockers documented


---

## Continuous Improvement

### Using Dashboard for Decision-Making

**Quarterly Review Cycle:**
1. Generate dashboard from updated source assessments
2. Compare to previous quarter (trending)
3. Celebrate improvements (gaps closed, compliance increased)
4. Address declining metrics (why getting worse?)
5. Adjust remediation plans based on progress
6. Recertify or document why not ready

**Investment Decisions:**

- Use gap analysis to justify budget requests
- Prioritize investments based on risk and impact
- Track ROI on change management improvements


**Strategic Planning:**

- Dashboard informs annual planning
- Identifies capability gaps
- Guides tool investment decisions
- Supports maturity roadmap


---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel dashboard workbook generation and maintenance. Users completing the dashboard should refer to Part I above.

---

# ISMS-IMP-A.8.32.5 - Compliance Summary Dashboard
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.32.5  
**Assessment Area:** Compliance Summary Dashboard (Consolidated Oversight)  
**Related Policy:** ISMS-POL-A.8.32 (Change Management)  
**Purpose:** Consolidate compliance data from all four A.8.32 assessment workbooks into executive-level dashboard

**CRITICAL DESIGN PRINCIPLE:** This dashboard uses **Excel external workbook references** to pull live data from normalized source workbooks. Dashboard does NOT duplicate data entry?EUR"it aggregates and visualizes data from the 4 assessment workbooks.

---

## Source Workbooks

This dashboard consolidates data from these four normalized assessment workbooks:

1. **ISMS-IMP-A.8.32.1.xlsx** - Change Process Assessment
2. **ISMS-IMP-A.8.32.2.xlsx** - Change Types & Categories Assessment  
3. **ISMS-IMP-A.8.32.3.xlsx** - Environment Separation Assessment
4. **ISMS-IMP-A.8.32.4.xlsx** - Testing & Validation Assessment

**Normalization Workflow:**
1. Generate assessment workbooks with dated filenames (Scripts 1-4)
2. Run `normalize_assessment_files_a832.py` to create normalized copies

# ISMS-IMP-A.8.32.5 - Compliance Summary Dashboard
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.32.5  
**Assessment Area:** Compliance Summary Dashboard (Consolidated Oversight)  
**Related Policy:** ISMS-POL-A.8.32 (Change Management)  
**Purpose:** Consolidate compliance data from all four A.8.32 assessment workbooks into executive-level dashboard

**CRITICAL DESIGN PRINCIPLE:** This dashboard uses **Excel external workbook references** to pull live data from normalized source workbooks. Dashboard does NOT duplicate data entry—it aggregates and visualizes data from the 4 assessment workbooks.

---

## Source Workbooks

This dashboard consolidates data from these four normalized assessment workbooks:

1. **ISMS-IMP-A.8.32.1.xlsx** - Change Process Assessment
2. **ISMS-IMP-A.8.32.2.xlsx** - Change Types & Categories Assessment  
3. **ISMS-IMP-A.8.32.3.xlsx** - Environment Separation Assessment
4. **ISMS-IMP-A.8.32.4.xlsx** - Testing & Validation Assessment

**Normalization Workflow:**
1. Generate assessment workbooks with dated filenames (Scripts 1-4)
2. Run `normalize_assessment_files_a832.py` to create normalized copies
3. Generate this dashboard workbook (Script 5)
4. Place dashboard in same directory as normalized files
5. Open dashboard → Excel prompts "Update Links" → Auto-populates with current data

**External Reference Format:**
```
='[ISMS-IMP-A.8.32.1.xlsx]Summary_Dashboard'!B5
=COUNTIF('[ISMS-IMP-A.8.32.2.xlsx]Standard_Changes_Catalog'!G10:G60,"✅ Approved")
='[ISMS-IMP-A.8.32.3.xlsx]Summary_Dashboard'!F6
```

---

## Workbook Structure

### Sheet 1: Executive_Dashboard

#### Header Section

- **Title:** "ISMS-IMP-A.8.32.5 – Change Management Compliance Summary Dashboard"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.32: Change Management - Executive Overview"
- **Styling:** Dark blue header (003366), white text, centered, 50px height


#### Document Information Block (Rows 3-13)
```
Document Information            [Section Header]

Document ID:           ISMS-IMP-A.8.32.5
Report Type:           Compliance Summary Dashboard
Related Policy:        ISMS-POL-A.8.32 (Change Management)
Version:               1.0
Report Date:           [USER INPUT - yellow cell]
Reporting Period:      [USER INPUT - yellow cell]
Prepared By:           [USER INPUT - yellow cell]
Organization:          [Organization]
Review Cycle:          Quarterly
Last Updated:          [Formula: =TODAY(), gray cell, DD.MM.YYYY format]
```

#### Overall Compliance Summary (Rows 15-22)

**Section Header:** "OVERALL COMPLIANCE SUMMARY"

| Assessment Area | Compliance % | Status | Critical Gaps | Evidence Count | Last Updated |
|-----------------|--------------|--------|---------------|----------------|--------------|
| Change Process (IMP-A.8.32.1) | Formula: ='[ISMS-IMP-A.8.32.1.xlsx]Summary_Dashboard'!F5 | Formula: ='[ISMS-IMP-A.8.32.1.xlsx]Summary_Dashboard'!G5 | Formula: =COUNTIF('[ISMS-IMP-A.8.32.1.xlsx]Summary_Dashboard'!A25:A30,"❌") | Formula: =COUNTA('[ISMS-IMP-A.8.32.1.xlsx]Evidence_Register'!A5:A104) | Formula: ='[ISMS-IMP-A.8.32.1.xlsx]Instructions & Legend'!B6 |
| Change Types & Categories (IMP-A.8.32.2) | Formula from A.8.32.2 | Formula | Formula | Formula | Formula |
| Environment Separation (IMP-A.8.32.3) | Formula from A.8.32.3 | Formula | Formula | Formula | Formula |
| Testing & Validation (IMP-A.8.32.4) | Formula from A.8.32.4 | Formula | Formula | Formula | Formula |
| **OVERALL AVERAGE** | Formula: =AVERAGE(B17:B20) | Conditional: ✅/⚠️/❌ based on average | Formula: =SUM(D17:D20) | Formula: =SUM(E17:E20) | Formula: =MAX(F17:F20) |

**Conditional Formatting:**

- Compliance % cell: Green if ≥85%, Yellow if 70-84%, Red if <70%
- Status cell: Auto-populate based on compliance %


#### Key Performance Indicators (Rows 24-35)

**Section Header:** "KEY PERFORMANCE INDICATORS"

| KPI | Target | Current | Status | Trend | Notes |
|-----|--------|---------|--------|-------|-------|
| Overall Change Management Compliance | ≥85% | Formula: =B21 | Formula: Auto ✅/⚠️/❌ | [User can add ↑/→/↓] | Text |
| Standard Changes Catalog Size | ≥30 changes | Formula: =COUNTA('[ISMS-IMP-A.8.32.2.xlsx]Standard_Changes_Catalog'!A5:A54)-4 | Formula | Text | Text |
| Standard Changes as % of Total | ≥60% | Formula from A.8.32.2 dashboard | Formula | Text | Text |
| Emergency Changes Rate | <5% | Formula from A.8.32.2 dashboard | Formula | Text | Text |
| Change Success Rate (First Attempt) | ≥95% | [User Input - yellow] | Formula | Text | Text |
| Average Change Lead Time (Days) | <7 days | [User Input - yellow] | Formula | Text | Text |
| Environment Separation Compliance | 100% | Formula from A.8.32.3 dashboard | Formula | Text | Text |
| Production Data in Non-Prod (Violations) | 0 instances | Formula from A.8.32.3 dashboard | Formula | Text | Text |
| Security Testing Coverage (Control 8.29) | 100% releases | Formula from A.8.32.4 dashboard | Formula | Text | Text |
| Rollback Success Rate | ≥98% | Formula from A.8.32.4 dashboard | Formula | Text | Text |
| Test Automation Rate | ≥70% | Formula from A.8.32.4 dashboard | Formula | Text | Text |

#### Control Compliance Mapping (Rows 37-50)

**Section Header:** "ISO 27001:2022 CONTROL COMPLIANCE MAPPING"

| ISO Control | Requirement | Assessment Source | Compliance | Status | Evidence | Notes |
|-------------|-------------|-------------------|------------|--------|----------|-------|
| 8.31 - Environment Separation | Dev/Test/Prod separated | IMP-A.8.32.3 | Formula from A.8.32.3 | Auto status | Link to sheet | Text |
| 8.32 - Change Planning | Changes planned & approved | IMP-A.8.32.1 | Formula from A.8.32.1 | Auto status | Link to sheet | Text |
| 8.32 - Change Impact | Impact assessment required | IMP-A.8.32.2 | Formula from A.8.32.2 | Auto status | Link to sheet | Text |
| 8.32 - Change Authorization | Proper authorization | IMP-A.8.32.1 | Formula from A.8.32.1 | Auto status | Link to sheet | Text |
| 8.32 - Change Communication | Stakeholder notification | IMP-A.8.32.1 | Formula from A.8.32.1 | Auto status | Link to sheet | Text |
| 8.32 - Change Testing | Testing before production | IMP-A.8.32.4 | Formula from A.8.32.4 | Auto status | Link to sheet | Text |
| 8.32 - UAT Required | User acceptance testing | IMP-A.8.32.4 | Formula from A.8.32.4 | Auto status | Link to sheet | Text |
| 8.32 - Rollback Procedures | Rollback capability | IMP-A.8.32.4 | Formula from A.8.32.4 | Auto status | Link to sheet | Text |
| 8.32 - Post-Impl Validation | Production validation | IMP-A.8.32.4 | Formula from A.8.32.4 | Auto status | Link to sheet | Text |
| 8.32 - Change Records | Documentation maintained | IMP-A.8.32.1 | Formula from A.8.32.1 | Auto status | Link to sheet | Text |
| 8.33 - Test Data | Production data protection | IMP-A.8.32.3 | Formula from A.8.32.3 | Auto status | Link to sheet | Text |
| 8.29 - Security Testing | Security testing integrated | IMP-A.8.32.4 | Formula from A.8.32.4 | Auto status | Link to sheet | Text |

#### Critical Findings Summary (Rows 52-58)

**Section Header (RED):** "CRITICAL FINDINGS REQUIRING IMMEDIATE ATTENTION"

| Assessment | Critical Finding | Severity | Assigned To | Target Date | Status |
|------------|------------------|----------|-------------|-------------|--------|
| Auto-populate from A.8.32.1-4 dashboards | Text | Critical/High/Medium | Text | Date DD.MM.YYYY | ✅/⚠️/❌/📋 |

[10 rows for critical findings - auto-populate from source workbooks' Summary_Dashboard sheets]

**Column Widths:**

- A: 40, B: 18, C: 12, D: 18, E: 15, F: 15, G: 30


---

## Sheet 2: Gap_Analysis

### Purpose
Aggregate all gaps identified across the 4 assessment workbooks.

### Header Section
**Row 1:** "CONSOLIDATED GAP ANALYSIS"  
**Row 2:** "Gaps identified across all Change Management assessments"

### Gaps by Assessment Area (Rows 4-80)

**Section 1: Change Process Gaps (Rows 4-23)**

Header: "CHANGE PROCESS GAPS (IMP-A.8.32.1)"

| Gap ID | Gap Description | Assessment Area | Impact | Priority | Current State | Target State | Remediation Action | Owner | Target Date | Status | Evidence |
|--------|-----------------|-----------------|--------|----------|---------------|--------------|-------------------|-------|-------------|--------|----------|
| Formula: Auto-generate from A.8.32.1 | Formula: Pull from A.8.32.1 | Text | Formula | Formula | Formula | Text | Text | Text | Date | Formula | Text |

**[20 rows - Reference gaps from ISMS-IMP-A.8.32.1.xlsx Summary_Dashboard or specific sheets]**

**Section 2: Change Types & Categories Gaps (Rows 25-44)**

Header: "CHANGE TYPES & CATEGORIES GAPS (IMP-A.8.32.2)"

[20 rows - Same structure as above, pulling from A.8.32.2]

**Section 3: Environment Separation Gaps (Rows 46-65)**

Header: "ENVIRONMENT SEPARATION GAPS (IMP-A.8.32.3)"

[20 rows - Same structure, pulling from A.8.32.3]

**Section 4: Testing & Validation Gaps (Rows 67-86)**

Header: "TESTING & VALIDATION GAPS (IMP-A.8.32.4)"

[20 rows - Same structure, pulling from A.8.32.4]

### Gap Statistics (Rows 88-100)

**Section Header:** "GAP ANALYSIS STATISTICS"

| Metric | Count | Percentage | Notes |
|--------|-------|------------|-------|
| Total Gaps Identified | Formula: Count all non-empty gaps | 100% | Text |
| Critical Priority Gaps | Formula: COUNTIF priority="Critical" | Formula: % of total | Text |
| High Priority Gaps | Formula: COUNTIF priority="High" | Formula: % | Text |
| Medium Priority Gaps | Formula: COUNTIF priority="Medium" | Formula: % | Text |
| Low Priority Gaps | Formula: COUNTIF priority="Low" | Formula: % | Text |
| Gaps by Status - Open | Formula: COUNTIF status="❌" | Formula: % | Text |
| Gaps by Status - In Progress | Formula: COUNTIF status="⚠️" | Formula: % | Text |
| Gaps by Status - Closed | Formula: COUNTIF status="✅" | Formula: % | Text |
| Overdue Gaps | Formula: Target date < TODAY() AND status ≠ "✅" | Formula: % | Text |

**Column Widths:**

- A: 12, B: 40, C: 25, D: 15, E: 15, F: 25, G: 25, H: 25, I: 20, J: 15, K: 15, L: 25


---

## Sheet 3: Risk_Register

### Purpose
Consolidated risk register for change management risks.

### Header Section
**Row 1:** "CHANGE MANAGEMENT RISK REGISTER"  
**Row 2:** "Consolidated risk assessment across all change management areas"

### Risk Categories (Rows 4-8)

| Risk Category | Definition | Example |
|---------------|------------|---------|
| Process Risk | Risk due to inadequate change process | Unauthorized changes, missing approvals |
| Technical Risk | Risk from technical failures | Failed deployments, system outages |
| Environmental Risk | Risk from inadequate separation | Prod data in dev, unauthorized access |
| Testing Risk | Risk from insufficient testing | Defects in production, rollback failures |

### Risk Assessment Matrix (Rows 10-65)

**Section Header:** "IDENTIFIED RISKS"

| Risk ID | Risk Description | Category | Likelihood (1-5) | Impact (1-5) | Risk Score | Risk Level | Source Assessment | Mitigation Strategy | Responsible | Status | Last Review |
|---------|------------------|----------|------------------|--------------|------------|------------|-------------------|-------------------|-------------|--------|-------------|
| R-001 | Formula/User: Pull from source workbooks | Process/Technical/Environmental/Testing | Formula or User | Formula or User | Formula: Likelihood Ã- Impact | Formula: Critical(20-25)/High(15-19)/Medium(8-14)/Low(1-7) | IMP-A.8.32.X | Text | Text | ✅/⚠️/❌/📋 | Date DD.MM.YYYY |

**[50 rows for risk tracking]**

### Risk Statistics (Rows 67-80)

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Risks | Formula: COUNT non-empty | 100% |
| Critical Risks (Score 20-25) | Formula: COUNTIF | % |
| High Risks (Score 15-19) | Formula: COUNTIF | % |
| Medium Risks (Score 8-14) | Formula: COUNTIF | % |
| Low Risks (Score 1-7) | Formula: COUNTIF | % |
| Risks by Category - Process | Formula | % |
| Risks by Category - Technical | Formula | % |
| Risks by Category - Environmental | Formula | % |
| Risks by Category - Testing | Formula | % |
| Mitigated Risks | Formula: status="✅" | % |
| Risks Requiring Action | Formula: status≠"✅" | % |

**Column Widths:**

- A: 12, B: 40, C: 18, D: 12, E: 12, F: 12, G: 15, H: 20, I: 35, J: 20, K: 15, L: 15


---

## Sheet 4: Remediation_Roadmap

### Purpose
Structured remediation plan with timeline.

### Header Section
**Row 1:** "REMEDIATION ROADMAP"  
**Row 2:** "Structured plan to address identified gaps and risks"

### Remediation Timeline Overview (Rows 4-10)

| Phase | Timeline | Focus Areas | Expected Outcome |
|-------|----------|-------------|------------------|
| Phase 1 - Critical (0-30 days) | [User Input] | Critical gaps and risks | Text |
| Phase 2 - High Priority (31-90 days) | [User Input] | High priority items | Text |
| Phase 3 - Medium Priority (91-180 days) | [User Input] | Medium priority items | Text |
| Phase 4 - Continuous Improvement (Ongoing) | [User Input] | Low priority and enhancements | Text |

### Remediation Actions (Rows 12-70)

**Section Header:** "REMEDIATION ACTION PLAN"

| Action ID | Description | Priority | Related Gap/Risk | Source | Owner | Start Date | Target Date | Status | Progress % | Dependencies | Notes |
|-----------|-------------|----------|------------------|--------|-------|------------|-------------|--------|------------|--------------|-------|
| RA-001 | Text (auto-populate from gaps) | Critical/High/Medium/Low | Link to Gap ID | IMP-A.8.32.X | Text | Date DD.MM.YYYY | Date DD.MM.YYYY | ✅/⚠️/❌/📋 | Formula or User: 0-100% | Text | Text |

**[60 rows for remediation actions]**

### Remediation Progress Summary (Rows 72-85)

| Metric | Count | Percentage | Target | Status |
|--------|-------|------------|--------|--------|
| Total Remediation Actions | Formula | 100% | N/A | N/A |
| Completed Actions | Formula: status="✅" | % | Text | Auto |
| In Progress Actions | Formula: status="⚠️" | % | Text | Auto |
| Not Started Actions | Formula: status="❌" | % | Text | Auto |
| Planned Actions | Formula: status="📋" | % | Text | Auto |
| Overdue Actions | Formula: Target date < TODAY() AND status≠"✅" | % | <10% | Auto |
| Critical Actions Remaining | Formula | % | 0% | Auto |
| High Priority Actions Remaining | Formula | % | Text | Auto |
| Average Progress % | Formula: AVERAGE of all progress | N/A | ≥70% | Auto |
| On-Time Completion Rate | Formula | % | ≥90% | Auto |

**Column Widths:**

- A: 12, B: 40, C: 15, D: 15, E: 15, F: 20, G: 12, H: 12, I: 12, J: 12, K: 25, L: 30


---

## Sheet 5: KPIs_and_Metrics

### Purpose
Detailed KPI tracking with historical trends.

### Header Section
**Row 1:** "KEY PERFORMANCE INDICATORS & METRICS"  
**Row 2:** "Detailed tracking of change management performance metrics"

### Change Management KPIs (Rows 4-30)

**Section Header:** "CHANGE MANAGEMENT PERFORMANCE METRICS"

| KPI Category | KPI Name | Target | Current | Last Period | Trend | Status | Data Source | Notes |
|--------------|----------|--------|---------|-------------|-------|--------|-------------|-------|
| **Process Efficiency** | | | | | | | | |
| Change Success Rate (First Attempt) | Text | ≥95% | [User Input] | [User Input] | ↑/→/↓ | Auto | User tracking | Text |
| Average Change Lead Time | Text | <7 days | [User Input] | [User Input] | Trend | Auto | User tracking | Text |
| Change Approval Cycle Time | Text | <2 days | [User Input] | [User Input] | Trend | Auto | User tracking | Text |
| CAB Meeting Frequency | Text | Weekly | [User Input] | [User Input] | Trend | Auto | User tracking | Text |
| **Change Classification** | | | | | | | | |
| Standard Changes (%) | Text | ≥60% | Formula from A.8.32.2 | [User Input] | Trend | Auto | IMP-A.8.32.2 | Text |
| Normal Changes (%) | Text | 30-40% | Formula from A.8.32.2 | [User Input] | Trend | Auto | IMP-A.8.32.2 | Text |
| Emergency Changes (%) | Text | <5% | Formula from A.8.32.2 | [User Input] | Trend | Auto | IMP-A.8.32.2 | Text |
| Standard Changes Catalog Size | Text | ≥30 | Formula from A.8.32.2 | [User Input] | Trend | Auto | IMP-A.8.32.2 | Text |
| **Environment Separation** | | | | | | | | |
| Environment Isolation Compliance | Text | 100% | Formula from A.8.32.3 | [User Input] | Trend | Auto | IMP-A.8.32.3 | Text |
| Production Data in Non-Prod | Text | 0 instances | Formula from A.8.32.3 | [User Input] | Trend | Auto | IMP-A.8.32.3 | Text |
| Developer Access to Production | Text | 0% | Formula from A.8.32.3 | [User Input] | Trend | Auto | IMP-A.8.32.3 | Text |
| Data Anonymization Effectiveness | Text | >95% | Formula from A.8.32.3 | [User Input] | Trend | Auto | IMP-A.8.32.3 | Text |
| **Testing & Validation** | | | | | | | | |
| Test Automation Rate | Text | ≥70% | Formula from A.8.32.4 | [User Input] | Trend | Auto | IMP-A.8.32.4 | Text |
| Code Coverage | Text | ≥80% | Formula from A.8.32.4 | [User Input] | Trend | Auto | IMP-A.8.32.4 | Text |
| Security Testing Coverage | Text | 100% releases | Formula from A.8.32.4 | [User Input] | Trend | Auto | IMP-A.8.32.4 | Text |
| UAT Sign-Off Rate | Text | 100% | Formula from A.8.32.4 | [User Input] | Trend | Auto | IMP-A.8.32.4 | Text |
| Rollback Testing Rate | Text | 100% | Formula from A.8.32.4 | [User Input] | Trend | Auto | IMP-A.8.32.4 | Text |
| Rollback Success Rate | Text | ≥98% | Formula from A.8.32.4 | [User Input] | Trend | Auto | IMP-A.8.32.4 | Text |
| Production Validation Rate | Text | 100% | Formula from A.8.32.4 | [User Input] | Trend | Auto | IMP-A.8.32.4 | Text |
| Defects Escaped to Production | Text | <2/quarter | [User Input] | [User Input] | Trend | Auto | User tracking | Text |
| **Compliance & Audit** | | | | | | | | |
| Overall Compliance Rate | Text | ≥85% | Formula: Average from Executive_Dashboard | [User Input] | Trend | Auto | Dashboard | Text |
| Critical Findings Open | Text | 0 | Formula from Executive_Dashboard | [User Input] | Trend | Auto | Dashboard | Text |
| Evidence Documentation Rate | Text | 100% | Formula: Evidence count / Required | [User Input] | Trend | Auto | Evidence sheets | Text |
| Audit Readiness Score | Text | ≥85% | Formula from dashboards | [User Input] | Trend | Auto | All assessments | Text |

### Historical Trend Data (Rows 32-50)

**Section Header:** "HISTORICAL TREND DATA (Optional - User Maintained)"

| Period | Overall Compliance % | Emergency Changes % | Test Automation % | Rollback Success % | Critical Findings | Notes |
|--------|---------------------|---------------------|-------------------|-------------------|-------------------|-------|
| Q1 2026 | [User Input] | [User Input] | [User Input] | [User Input] | [User Input] | Text |

**[20 rows for historical tracking - User maintains this manually]**

**Column Widths:**

- A: 25, B: 35, C: 15, D: 15, E: 15, F: 10, G: 12, H: 25, I: 30


---

## Sheet 6: Evidence_Consolidation

### Purpose
Consolidated evidence register from all 4 assessment workbooks.

### Header Section
**Row 1:** "CONSOLIDATED EVIDENCE REGISTER"  
**Row 2:** "Evidence from all Change Management assessments (400 entries)"

### Evidence Inventory (Rows 4-403, 400 rows)

**Section Header:** "EVIDENCE ENTRIES FROM ALL ASSESSMENTS"

| Evidence ID | Source Assessment | Evidence Type | Description | Location/Path | Date Collected | Collected By | Verification Status | Auditor Notes |
|-------------|-------------------|---------------|-------------|---------------|----------------|--------------|-------------------|---------------|
| Formula: Auto-reference from A.8.32.1 | IMP-A.8.32.1 | Formula: Link | Formula: Link | Formula: Link | Formula: Link | Formula: Link | Formula: Link | Formula: Link |

**Structure:**

- Rows 5-104: Evidence from IMP-A.8.32.1 (100 entries)
- Rows 105-204: Evidence from IMP-A.8.32.2 (100 entries)
- Rows 205-304: Evidence from IMP-A.8.32.3 (100 entries)
- Rows 305-404: Evidence from IMP-A.8.32.4 (100 entries)


**Formula Pattern for each section:**
```
Row 5: ='[ISMS-IMP-A.8.32.1.xlsx]Evidence_Register'!A5
Row 6: ='[ISMS-IMP-A.8.32.1.xlsx]Evidence_Register'!A6
...
Row 104: ='[ISMS-IMP-A.8.32.1.xlsx]Evidence_Register'!A104
```

### Evidence Statistics (Rows 406-420)

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Evidence Entries | Formula: COUNT non-empty | 100% |
| Evidence from Change Process (A.8.32.1) | Formula | % |
| Evidence from Change Types (A.8.32.2) | Formula | % |
| Evidence from Environment Sep (A.8.32.3) | Formula | % |
| Evidence from Testing (A.8.32.4) | Formula | % |
| Verified Evidence | Formula: status="✅ Verified" | % |
| Pending Verification | Formula: status="⚠️ Pending" | % |
| Not Verified | Formula: status="❌ Not Verified" | % |
| Evidence by Type - Process Docs | Formula: COUNTIF | % |
| Evidence by Type - Technical Configs | Formula | % |
| Evidence by Type - Test Results | Formula | % |
| Evidence by Type - Approvals | Formula | % |

**Column Widths:**

- A: 15, B: 20, C: 20, D: 40, E: 30, F: 15, G: 20, H: 18, I: 30


---

## Sheet 7: Action_Items_and_Followup

### Purpose
Track action items and follow-up activities.

### Header Section
**Row 1:** "ACTION ITEMS & FOLLOW-UP"  
**Row 2:** "Track outstanding actions and follow-up activities"

### Action Items (Rows 4-53)

**Section Header:** "OUTSTANDING ACTION ITEMS"

| Action ID | Description | Type | Assigned To | Due Date | Status | Priority | Related Finding | Source | Progress % | Notes |
|-----------|-------------|------|-------------|----------|--------|----------|----------------|--------|------------|-------|
| ACT-001 | [User Input or auto-populate from gaps] | Remediation/Investigation/Review/Training | Text | Date DD.MM.YYYY | ✅/⚠️/❌/📋 | Critical/High/Medium/Low | Link to Gap/Risk | IMP-A.8.32.X | 0-100% | Text |

**[50 rows for action items]**

### Follow-Up Items (Rows 55-85)

**Section Header:** "SCHEDULED FOLLOW-UP ACTIVITIES"

| Follow-Up ID | Activity | Frequency | Last Completed | Next Due | Owner | Status | Notes |
|--------------|----------|-----------|----------------|----------|-------|--------|-------|
| FU-001 | Quarterly Assessment Review | Quarterly | Date DD.MM.YYYY | Formula: Last+90 days | Text | ✅/⚠️/❌ | Text |
| FU-002 | Standard Changes Catalog Review | Monthly | Date | Formula: Last+30 days | Text | Status | Text |
| FU-003 | Emergency Changes Analysis | Monthly | Date | Formula | Text | Status | Text |
| FU-004 | Environment Separation Audit | Quarterly | Date | Formula | Text | Status | Text |
| FU-005 | Test Metrics Review | Monthly | Date | Formula | Text | Status | Text |
| FU-006 | CAB Effectiveness Review | Quarterly | Date | Formula | Text | Status | Text |
| FU-007 | Risk Register Update | Monthly | Date | Formula | Text | Status | Text |
| FU-008 | Evidence Review | Quarterly | Date | Formula | Text | Status | Text |

**[30 rows total for follow-up tracking]**

### Action Items Statistics (Rows 87-100)

| Metric | Count | Percentage | Notes |
|--------|-------|------------|-------|
| Total Action Items | Formula | 100% | Text |
| Completed Actions | Formula: status="✅" | % | Text |
| In Progress Actions | Formula: status="⚠️" | % | Text |
| Not Started Actions | Formula: status="❌" | % | Text |
| Overdue Actions | Formula | % | Text |
| Critical Priority Actions Open | Formula | % | Text |
| Actions by Type - Remediation | Formula | % | Text |
| Actions by Type - Investigation | Formula | % | Text |
| Follow-Up Activities Overdue | Formula | Count | Text |

**Column Widths:**

- A: 12, B: 40, C: 18, D: 20, E: 12, F: 12, G: 15, H: 20, I: 15, J: 12, K: 30


---

## Sheet 8: Audit_and_Compliance_Log

### Purpose
Document audit activities, compliance assessments, and regulatory reviews.

### Header Section
**Row 1:** "AUDIT & COMPLIANCE LOG"  
**Row 2:** "Track audit activities and compliance assessments"

### Audit History (Rows 4-33)

**Section Header:** "AUDIT HISTORY"

| Audit ID | Audit Type | Auditor | Audit Date | Scope | Findings Count | Critical Findings | Status | Report Location | Follow-Up Required | Notes |
|----------|------------|---------|------------|-------|----------------|-------------------|--------|-----------------|-------------------|-------|
| AUD-001 | Internal/External/Regulatory | Text | Date DD.MM.YYYY | Text | Number | Number | Completed/In Progress/Scheduled | Text | ✅ Yes/❌ No | Text |

**[30 rows for audit tracking]**

### Compliance Assessments (Rows 35-64)

**Section Header:** "COMPLIANCE ASSESSMENTS"

| Assessment ID | Assessment Date | Assessed By | Assessment Type | Compliance Score | Gaps Identified | Critical Gaps | Status | Next Assessment | Notes |
|---------------|-----------------|-------------|-----------------|------------------|-----------------|---------------|--------|-----------------|-------|
| COMP-001 | Date DD.MM.YYYY | Text | Self-Assessment/Internal Audit/External Audit | Formula or User: % | Number | Number | ✅/⚠️/❌ | Date: Formula +90 days | Text |

**[30 rows for compliance assessment tracking]**

### Regulatory Reviews (Rows 66-85)

**Section Header:** "REGULATORY & COMPLIANCE REVIEWS"

| Review ID | Regulatory Framework | Review Date | Reviewer | Compliance Status | Findings | Remediation Required | Target Date | Status | Notes |
|-----------|---------------------|-------------|----------|-------------------|----------|---------------------|-------------|--------|-------|
| REG-001 | ISO 27001/GDPR/SOC2/HIPAA/etc | Date DD.MM.YYYY | Text | Compliant/Partial/Non-Compliant | Text | ✅ Yes/❌ No | Date | ✅/⚠️/❌ | Text |

**[20 rows for regulatory review tracking]**

### Audit & Compliance Statistics (Rows 87-100)

| Metric | Count | Notes |
|--------|-------|-------|
| Total Audits Conducted | Formula | Text |
| Internal Audits | Formula | Text |
| External Audits | Formula | Text |
| Regulatory Audits | Formula | Text |
| Average Audit Findings | Formula | Text |
| Critical Findings from Audits | Formula | Text |
| Closed Audit Findings | Formula | Text |
| Open Audit Findings | Formula | Text |
| Average Time to Close Findings (Days) | Formula or User | Text |
| Compliance Assessments This Year | Formula | Text |
| Overall Compliance Trend | User: Improving/Stable/Declining | Text |

**Column Widths:**

- A: 12, B: 20, C: 20, D: 12, E: 30, F: 12, G: 15, H: 25, I: 25, J: 15, K: 30


---

## Sheet 9: Approval_Sign_Off

### Purpose
Executive approval and sign-off for consolidated dashboard.

### Assessment Summary Section (Rows 3-15)
```
CONSOLIDATED DASHBOARD SUMMARY

Dashboard Document:        ISMS-IMP-A.8.32.5 - Compliance Summary Dashboard
Reporting Period:          [USER INPUT]
Scope:                     All Change Management (Controls 8.31, 8.32, 8.33, 8.29)
Overall Compliance Rate:   [Formula from Executive_Dashboard]
Critical Findings:         [Formula from Executive_Dashboard]
Assessment 1 Status:       [Formula from A.8.32.1]
Assessment 2 Status:       [Formula from A.8.32.2]
Assessment 3 Status:       [Formula from A.8.32.3]
Assessment 4 Status:       [Formula from A.8.32.4]
Total Evidence Entries:    [Formula: Sum all evidence counts]
Risk Rating:               [Formula: Based on critical findings]
Audit Readiness:           [Formula: Based on overall compliance]
Dashboard Status:          [Dropdown: ✅ Final/⚠️ Requires Action/📋 Draft/❌ Re-assessment Required]
```

### Dashboard Prepared By (Rows 17-25)
```
Name:               [USER INPUT]
Role/Title:         [USER INPUT]
Department:         [USER INPUT]
Email:              [USER INPUT]
Phone:              [USER INPUT]
Date Prepared:      [USER INPUT - date picker, format DD.MM.YYYY]
Signature:          [USER INPUT]
```

### Reviewed By - Change Manager (Rows 27-36)
```
Name:                   [USER INPUT]
Role/Title:             [USER INPUT]
Review Date:            [USER INPUT - date picker, format DD.MM.YYYY]
Review Notes:           [Text area - merged cells]
Recommendation:         [Dropdown: ✅ Approve/⚠️ Approve with Conditions/❌ Reject/📋 Require Rework]
Conditions (if any):    [Text area - merged cells]
Signature:              [USER INPUT]
```

### Approved By - CISO (Rows 38-47)
```
Name:                   [USER INPUT]
Role/Title:             [USER INPUT]
Approval Date:          [USER INPUT - date picker, format DD.MM.YYYY]
Approval Decision:      [Dropdown: ✅ Approved/⚠️ Approved with Conditions/❌ Rejected]
Conditions/Notes:       [Text area - merged cells]
Signature:              [USER INPUT]
```

### Next Review Details (Rows 49-55)
```
Next Review Date:       [Formula: Approval Date + 90 days, format DD.MM.YYYY]
Review Responsibility:  [USER INPUT]
Review Focus Areas:     [USER INPUT - merged cells]
Regulatory Compliance:  [USER INPUT - any specific regulatory deadlines]
Remediation Tracking:   [Link to Remediation_Roadmap sheet]
Assessment Frequency:   Quarterly
```

**Column Widths:**

- A: 25, B: 30, C: 20, D: 20, E: 20


---

## External Workbook Reference Summary

### Reference Pattern

**Format for external references:**
```excel
='[Normalized-Filename.xlsx]SheetName'!CellRange
```

**Examples:**
```excel
='[ISMS-IMP-A.8.32.1.xlsx]Summary_Dashboard'!B5
='[ISMS-IMP-A.8.32.2.xlsx]Standard_Changes_Catalog'!A5:A54
='[ISMS-IMP-A.8.32.3.xlsx]Production_Environment'!D15
='[ISMS-IMP-A.8.32.4.xlsx]Test_Types_Coverage'!F20
=COUNTIF('[ISMS-IMP-A.8.32.2.xlsx]Emergency_Changes'!G10:G30,"✅ Approved")
```

### Key Reference Points by Source Workbook

**A.8.32.1 (Change Process):**

- Summary_Dashboard: Compliance %, Status, Critical gaps
- Change_Process_Workflow: Process maturity scores
- Approval_Authority_Matrix: Approval compliance
- Evidence_Register: All 100 evidence entries (rows 5-104)


**A.8.32.2 (Change Types):**

- Summary_Dashboard: Compliance %, Emergency change %
- Standard_Changes_Catalog: Count of standard changes (rows 5-54)
- Emergency_Changes: Emergency change metrics
- Change_Risk_Classification: Risk scores
- Evidence_Register: All 100 evidence entries (rows 5-104)


**A.8.32.3 (Environment Separation):**

- Summary_Dashboard: Compliance %, Critical findings
- Production_Environment: Production access controls
- Production_Data_in_NonProd: Data anonymization compliance
- Evidence_Register: All 100 evidence entries (rows 5-104)


**A.8.32.4 (Testing & Validation):**

- Summary_Dashboard: Compliance %, Testing metrics
- Test_Types_Coverage: Security testing coverage (Control 8.29)
- Rollback_Procedures: Rollback success rate
- Production_Validation: Production validation rate
- Evidence_Register: All 100 evidence entries (rows 5-104)


### Formula Construction Rules

1. **Always use square brackets** around filename: `[ISMS-IMP-A.8.32.1.xlsx]`
2. **Sheet names with spaces** use single quotes: `'Summary_Dashboard'`
3. **Sheet names without spaces** don't need quotes but can have them
4. **Cell ranges** use standard Excel notation: `!B5` or `!A5:A104`
5. **Functions** work normally with external references: `=COUNTA('[file.xlsx]Sheet'!A5:A104)`
6. **String literals** in formulas need escaped quotes: `=COUNTIF('[file.xlsx]Sheet'!A5:A50,\"Critical\")`

---

## Integration & Usage Notes

### File Placement Requirements
1. **All 5 files in SAME directory:**

   - ISMS-IMP-A.8.32.1.xlsx (normalized)
   - ISMS-IMP-A.8.32.2.xlsx (normalized)
   - ISMS-IMP-A.8.32.3.xlsx (normalized)
   - ISMS-IMP-A.8.32.4.xlsx (normalized)
   - ISMS_A_8_32_5_Compliance_Dashboard_YYYYMMDD.xlsx (this dashboard)


2. **First Open Behavior:**

   - Excel prompts: "This workbook contains links to other data sources"
   - Click "Update" to pull current data from source workbooks
   - Click "Don't Update" to keep cached values


3. **Updating Data:**

   - Open dashboard → Excel prompts → Click "Update"
   - Or: Data tab → Edit Links → Update Values
   - Dashboard auto-refreshes with current assessment data


### Workflow Summary

**PHASE 1 - Assessment:**
1. Complete 4 assessment workbooks (Scripts 1-4 generate dated files)
2. Document evidence, compliance status, gaps, risks in each workbook

**PHASE 2 - Normalization:**
3. Run `normalize_assessment_files_a832.py`
4. Creates normalized copies (no dates in filenames)
5. Generates audit manifest for traceability

**PHASE 3 - Dashboard:**
6. Generate this dashboard (Script 5)
7. Place dashboard in same directory as normalized files
8. Open dashboard → Update Links → Auto-populated with current data
9. Review Executive_Dashboard, Gap_Analysis, Risk_Register
10. Populate user-input fields (KPIs, trends, action items)
11. Obtain executive approval via Approval_Sign_Off

**PHASE 4 - Continuous Monitoring:**
12. Update source assessment workbooks as changes occur
13. Open dashboard → Update Links → See refreshed data
14. Track remediation progress
15. Quarterly reviews and re-assessments

---

**END OF SPECIFICATION**

---

*"Zero-knowledge proofs are perhaps the most powerful tool we have in cryptography."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-01-31 -->
