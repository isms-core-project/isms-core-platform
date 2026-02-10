<!-- ISMS-CORE:IMP:ISMS-IMP-A.6.3.4-UG:framework:UG:a.6.3.4 -->
**ISMS-IMP-A.6.3.4-UG - Training Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.6.3: Information Security Awareness, Education and Training

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.3.4-UG |
| **Version** | 1.0 |
| **Assessment Area** | Training Program Effectiveness and Compliance Reporting |
| **Related Policy** | ISMS-POL-A.6.3, Section 3 (Roles and Responsibilities), Section 4 (Evidence Requirements) |
| **Purpose** | Consolidate training metrics, measure program effectiveness, generate compliance reports, and support audit evidence requirements |
| **Target Audience** | CISO, Information Security Officers, HR Directors, Internal Audit, Management |
| **Assessment Type** | Executive Reporting & Compliance Monitoring |
| **Review Cycle** | Monthly reporting + Quarterly management review + Annual effectiveness assessment |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Initial | Initial specification for Training Compliance Dashboard workbook | ISMS Implementation Team |

---

**Audience:** CISO, Information Security Officers, HR Directors, Internal Audit

---

# Assessment Overview

## What This Assessment Measures

This workbook consolidates training program data to provide executive-level compliance visibility, effectiveness measurement, and audit-ready reporting per ISMS-POL-A.6.3 requirements.

**Scope:** 5 reporting domains:
1. **Organizational Compliance** - Overall training completion and compliance status
2. **Effectiveness Metrics** - Behavioral change and risk reduction indicators
3. **Trend Analysis** - Historical performance and trajectory
4. **Risk Indicators** - Training-related security risk visibility
5. **Audit Readiness** - Evidence status and compliance gaps

**Assessment Output:** Excel workbook providing:
- Executive summary dashboard
- Compliance metrics by department, tier, and module
- Effectiveness measurements and KPIs
- Trend analysis with historical comparison
- Risk heat maps for training gaps
- Audit evidence checklist and status
- Management review input reports

## Why This Matters

**ISO 27001:2022 Requirements:**
- Clause 9.1: Monitoring, measurement, analysis and evaluation
- Clause 9.3: Management review inputs include "effectiveness of the ISMS"
- Control A.6.3: Requires evidence of competence and training effectiveness

**Business Impact:**
- **Executive Visibility:** Clear compliance status for leadership decision-making
- **Risk Prioritization:** Identify highest-risk training gaps for targeted intervention
- **Audit Efficiency:** Pre-assembled evidence reduces audit preparation time
- **Continuous Improvement:** Trend data enables program optimization
- **Resource Justification:** Metrics support training investment decisions

## Who Should Complete This Assessment

**Primary Responsibility:** Information Security Officer / Training Program Manager

**Report Consumers:**
1. **CISO** - Strategic oversight, risk decisions, resource allocation
2. **HR Director** - Organizational compliance, remediation coordination
3. **Department Managers** - Team compliance status, intervention needs
4. **Internal Audit** - Evidence verification, compliance assessment
5. **Executive Management** - ISMS performance reporting

## Connection to Policy

This workbook supports **ISMS-POL-A.6.3, Section 4 (Evidence Requirements)**:
- Section 4.1: Stage 1 Documentation Evidence
- Section 4.2: Stage 2 Operational Evidence
- Section 3.2: CISO responsibilities for program effectiveness

---

# Dashboard Usage Guide

## Intended Audiences and Use Cases

| Audience | Primary Use | Key Sheets | Frequency |
|----------|-------------|------------|-----------|
| **CISO** | Strategic oversight, risk decisions | Executive_Summary, Risk_Heatmap | Weekly review |
| **ISO** | Program management, compliance monitoring | All sheets | Daily/Weekly |
| **HR Director** | Organizational compliance, intervention planning | Compliance_Metrics, Overdue alerts | Weekly |
| **Department Managers** | Team compliance, remediation | Compliance_Metrics (filtered) | Weekly |
| **Internal Audit** | Evidence verification, compliance assessment | Audit_Evidence, all data sheets | Quarterly/As needed |
| **Executive Committee** | ISMS performance reporting | Executive_Summary, Management_Review_Input | Quarterly |

## Dashboard Interpretation Guide

### Executive Summary Traffic Lights

| Indicator | Green | Yellow | Red |
|-----------|-------|--------|-----|
| **Completion Rate** | ≥95% | 85-94% | <85% |
| **On-Time Rate** | ≥90% | 80-89% | <80% |
| **Phishing Click Rate** | ≤5% | 6-15% | >15% |
| **Phishing Report Rate** | ≥70% | 50-69% | <50% |
| **Remediation Success** | ≥95% | 85-94% | <85% |

### Risk Heatmap Interpretation

**Combined Risk Levels:**
- **Critical (Red):** Immediate action required. Department has multiple significant risk factors. Escalate to CISO.
- **High (Orange):** Priority attention needed. Schedule intervention within 30 days.
- **Medium (Yellow):** Monitor closely. Include in regular management review.
- **Low (Green):** Compliant. Continue normal operations.

**Risk Factor Scoring:**

| Score | Overdue Training | Assessment Failures | Simulation Failures | Incident History |
|-------|------------------|---------------------|---------------------|------------------|
| 0 | 0% overdue | <5% fail rate | <5% click rate | No incidents |
| 1 | 1-5% overdue | 5-10% fail rate | 5-10% click rate | 1 minor incident |
| 2 | 6-15% overdue | 11-20% fail rate | 11-20% click rate | 2-3 incidents |
| 3 | >15% overdue | >20% fail rate | >20% click rate | 4+ or 1 major |

### Trend Analysis Guidance

**Positive Trends (Improving):**
- Completion rate increasing
- Click rate decreasing
- Report rate increasing
- Average scores improving

**Negative Trends (Require Attention):**
- Any metric declining for 2+ consecutive periods
- Sudden changes (>10% movement in single period)
- Divergence between departments (one falling behind)

---

# Reporting Procedures

## Monthly Compliance Report

**Generated By:** Information Security Officer
**Due:** By 5th business day of following month
**Distribution:** CISO, HR Director, Department Managers

**Report Contents:**
1. **Executive Summary** (1 page)
   - Overall compliance status (traffic lights)
   - Key metrics vs. targets
   - Critical issues requiring attention
   - Achievements and improvements

2. **Compliance Detail** (by department)
   - Completion rates
   - Overdue training count
   - Remediation cases

3. **Action Items**
   - Departments requiring intervention
   - Escalated cases
   - Recommended actions

**Process:**
1. Refresh data from source workbooks (A.6.3.1-3)
2. Update all calculated metrics
3. Generate Executive_Summary export
4. Prepare narrative summary
5. Distribute via secure email

## Quarterly Effectiveness Report

**Generated By:** Information Security Officer with Training Manager
**Due:** Within 10 business days of quarter end
**Distribution:** CISO, Security Committee, HR Leadership

**Report Contents:**
1. **Effectiveness Analysis**
   - Behavioral metrics trends
   - Simulation campaign results analysis
   - Knowledge retention assessment
   - Correlation with incident data

2. **Program Assessment**
   - What's working
   - Areas for improvement
   - Resource needs

3. **Recommendations**
   - Program adjustments
   - Content updates needed
   - Budget/resource requests

**Process:**
1. Compile quarterly data
2. Perform trend analysis
3. Correlate with incident/violation data
4. Draft recommendations
5. Present to CISO for review
6. Present to Security Committee

## Annual Program Review

**Generated By:** Training Manager with ISO
**Due:** Within 30 days of year end
**Distribution:** CISO, Executive Management, Board (summary)

**Report Contents:**
1. **Year in Review**
   - All KPIs vs. annual targets
   - Significant achievements
   - Challenges encountered

2. **Program Effectiveness**
   - Overall behavioral impact assessment
   - ROI analysis (if measurable)
   - Benchmark comparison (industry if available)

3. **Next Year Planning**
   - Recommended targets
   - Program changes
   - Budget requirements
   - New initiatives

## Ad-Hoc Audit Response

**Process:**
1. Receive evidence request from auditor
2. Identify relevant data in Audit_Evidence sheet
3. Extract requested records from source workbooks
4. Prepare evidence package with:
   - Cover sheet explaining contents
   - Extracted data (sanitized if needed)
   - Supporting documentation
5. Log evidence provision in Evidence_Register

---

# Evidence Collection

## Dashboard-Generated Evidence

This workbook automatically generates audit evidence:

| Report | Evidence Value | Retention |
|--------|---------------|-----------|
| Monthly Compliance Report | Demonstrates ongoing monitoring (Cl.9.1) | 3 years |
| Quarterly Effectiveness Report | Demonstrates effectiveness evaluation (Cl.9.1) | 3 years |
| Annual Program Review | Demonstrates continual improvement (Cl.10.1) | 5 years |
| Management Review Input | Supports management review (Cl.9.3) | 5 years |

## Evidence Storage

**Location:** ISMS Evidence Library / A.6.3 Training / Dashboard_Reports / [Year] /

**Naming Convention:**
- `ISMS-A.6.3.4_Monthly_Compliance_[YYYY-MM].pdf`
- `ISMS-A.6.3.4_Quarterly_Effectiveness_[YYYY-QX].pdf`
- `ISMS-A.6.3.4_Annual_Review_[YYYY].pdf`

**Archive Schedule:**
- Monthly reports: Archive after 3 years, delete after 5 years
- Quarterly reports: Archive after 3 years, delete after 5 years
- Annual reports: Archive after 5 years, delete after 7 years

---

# Common Pitfalls

## ❌ MISTAKE #1: Presenting Data Without Context

**The Problem:** Showing metrics without explaining what they mean or what action is needed.

**Why It Matters:** Executives can't act on data they don't understand. Reports become ignored.

**The Fix:**
- Always include interpretation guidance
- Highlight what changed and why it matters
- Include specific recommended actions
- Use traffic lights for quick understanding

## ❌ MISTAKE #2: Stale Data

**The Problem:** Dashboard shows outdated information; decisions made on old data.

**Why It Matters:** Wrong decisions. Loss of credibility. Compliance gaps undetected.

**The Fix:**
- Document refresh schedule for each data source
- Display "Last Updated" prominently
- Automate refreshes where possible
- Flag when data is >7 days old

## ❌ MISTAKE #3: Vanity Metrics

**The Problem:** Reporting metrics that look good but don't indicate actual security improvement.

**Why It Matters:** False sense of progress. Resources invested without return. Real risks hidden.

**The Fix:**
- Focus on behavioral and outcome metrics
- Track correlation between training and incidents
- Include leading AND lagging indicators
- Be honest about what metrics actually measure

## ❌ MISTAKE #4: One-Size-Fits-All Reporting

**The Problem:** Same report for CISO, department managers, and auditors.

**Why It Matters:** Too detailed for executives, not detailed enough for operations, wrong format for audit.

**The Fix:**
- Tailor reports to audience
- Executive summary for leadership
- Detailed breakdowns for operational managers
- Evidence packages for audit

## ❌ MISTAKE #5: No Historical Comparison

**The Problem:** Showing only current status without trend or comparison.

**Why It Matters:** Can't tell if improving or declining. No context for "good" or "bad."

**The Fix:**
- Always include trend data (month-over-month, quarter-over-quarter)
- Compare to previous year same period
- Show progress toward targets
- Highlight significant changes

## ❌ MISTAKE #6: Ignoring Low-Risk Areas

**The Problem:** Only focusing on red/critical items, ignoring green areas that might be degrading.

**Why It Matters:** Green areas can turn yellow, yellow can turn red. Early intervention is cheaper.

**The Fix:**
- Monitor all areas, not just problems
- Track direction of change (stable, improving, declining)
- Celebrate sustained compliance (reinforces good behavior)
- Set threshold for early warning (before red)

## ❌ MISTAKE #7: Incomplete Audit Evidence Tracking

**The Problem:** Audit_Evidence sheet not maintained; scrambling when auditors arrive.

**Why It Matters:** Audit preparation is stressful and time-consuming. Missing evidence = findings.

**The Fix:**
- Update Audit_Evidence sheet monthly
- Verify evidence locations are accurate
- Pre-stage evidence for common audit requests
- Conduct mock audit evidence review quarterly

## ❌ MISTAKE #8: Not Linking to Business Impact

**The Problem:** Security metrics not connected to business language or outcomes.

**Why It Matters:** Business leaders don't understand security jargon. Budget requests ignored.

**The Fix:**
- Translate to business impact where possible
- Show cost of incidents (when training gaps contributed)
- Express risk in terms executives understand
- Connect to strategic objectives

## ❌ MISTAKE #9: Manual Dashboard Updates

**The Problem:** Manually updating dashboard from multiple source workbooks, introducing errors.

**Why It Matters:** Errors in reporting. Time-consuming. Inconsistent updates.

**The Fix:**
- Use formulas to pull from source sheets
- Establish data validation checks
- Document refresh procedures
- Consider automation tools for larger organizations

## ❌ MISTAKE #10: No Action Follow-Through

**The Problem:** Dashboard identifies issues but no tracking of resolution.

**Why It Matters:** Same issues appear month after month. Dashboard becomes ignored.

**The Fix:**
- Every critical/high risk item gets assigned owner
- Track action items to resolution
- Report on closure rate
- Escalate unresolved items

---

# Quality Checklist

## Data Quality Checks

- [ ] All source data refreshed within expected timeframe
- [ ] "Last Updated" dates accurate
- [ ] No #REF! or #VALUE! errors in formulas
- [ ] Totals reconcile with source workbooks
- [ ] Personnel count matches HR headcount

## Metric Accuracy Checks

- [ ] Completion rate calculation verified (spot check)
- [ ] Traffic light thresholds applied correctly
- [ ] Risk scores calculate correctly
- [ ] Trend direction indicators accurate
- [ ] KPI values match definitions

## Report Quality Checks

- [ ] Executive summary reflects data accurately
- [ ] All charts render correctly
- [ ] No stale data (>7 days old)
- [ ] Narrative sections updated
- [ ] Action items are specific and actionable

## Audit Readiness Checks

- [ ] Audit_Evidence sheet current
- [ ] All evidence locations verified accessible
- [ ] Evidence retention periods appropriate
- [ ] Gap items have remediation plans

---

# Review & Approval

## Monthly Attestation

**Completed By:** Information Security Officer
**Review Points:**
- Data refresh verified
- Metrics calculated correctly
- Report generated and distributed
- Critical issues escalated

**Approved By:** CISO (for reports to executive)

## Quarterly Effectiveness Review

**Presented To:** Security Committee / CISO
**Includes:**
- Quarterly effectiveness report
- Trend analysis
- Recommendations

**Documentation:**
- Meeting minutes with decisions
- Approved report stored as evidence

## Annual Program Review

**Presented To:** Executive Management
**Includes:**
- Annual program review
- Next year targets and budget
- Program improvement recommendations

**Approval Required:**
- CISO approval of report content
- Executive approval of next year targets/budget

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
