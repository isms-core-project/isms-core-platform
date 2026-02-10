<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.32.5-UG:framework:UG:a.8.32.5 -->
**ISMS-IMP-A.8.32.5-UG - Compliance Summary Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.32.5-UG |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.32.5-TG.

---



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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
