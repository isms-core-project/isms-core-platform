**ISMS-IMP-A.7.10.4-UG - Storage Media Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.10: Storage Media

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.10.4-UG |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Compliance Dashboard & KPIs |
| **Related Policy** | ISMS-POL-A.7.10, Section 4 (Governance & Compliance) |
| **Purpose** | Consolidate storage media compliance data from assessments A.7.10.1-3, provide executive overview, track KPIs, and manage remediation roadmap |
| **Target Audience** | CISO, IT Management, Executive Leadership, Compliance Officers, Internal Audit |
| **Assessment Type** | Consolidated Dashboard & Executive Reporting |
| **Review Cycle** | Quarterly (minimum) or Monthly for Active Remediation |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Storage Media Compliance Dashboard | ISMS Implementation Team |

---

**Audience:** CISO, IT Directors, Executive Leadership, Compliance Officers, Internal Auditors

---

# Assessment Overview

## What This Dashboard Provides

This compliance dashboard **consolidates data from A.7.10.1-3 assessments** to provide:

1. **Executive Summary** - Overall media compliance posture at a glance
2. **Domain Summaries** - Status from each assessment area
3. **Gap Analysis** - Consolidated view of compliance gaps across all domains
4. **Risk Register** - Prioritised risks with ownership and remediation
5. **Remediation Roadmap** - Timeline and milestones for gap closure
6. **KPI Dashboard** - Key performance indicators and trends
7. **Evidence Index** - Master list of all compliance evidence

**Dashboard Output:** Single workbook providing executive visibility into storage media compliance, enabling informed decision-making on remediation priorities and resource allocation.

## Why This Matters

**ISO 27001:2022 Control A.7.10 Governance:**
> *"Storage media should be managed through their life cycle of acquisition, use, transportation and disposal in accordance with the organisation's classification scheme and handling requirements."*

**Executive Accountability:**
- Board-level visibility into media security posture
- Risk-based prioritisation of remediation
- Evidence of management oversight
- Audit-ready compliance documentation

**Business Impact:**
- **Strategic Planning:** Data-driven resource allocation
- **Audit Readiness:** Comprehensive evidence package
- **Risk Management:** Prioritised risk treatment
- **Continuous Improvement:** Trend tracking and benchmarking

## Who Should Use This Dashboard

**Primary Users:**
- **CISO:** Overall accountability for media security
- **IT Director:** Operational responsibility for media controls
- **CRO/Risk Officer:** Risk oversight and acceptance

**Support Users:**
- **Compliance Officers:** Regulatory alignment verification
- **Internal Audit:** Control testing and verification
- **Executive Management:** Governance oversight

## Prerequisites

Before using this dashboard, ensure:

- [ ] **A.7.10.1 Assessment** (Storage Media Inventory) completed
- [ ] **A.7.10.2 Assessment** (Media Handling Procedures) completed
- [ ] **A.7.10.3 Assessment** (Media Lifecycle Tracking) completed
- [ ] Normalized assessment files in same directory (if using external links)
- [ ] Access to update remediation status

---

# Dashboard Structure

## Sheet Overview

| Sheet # | Sheet Name | Purpose | Update Frequency |
|---------|------------|---------|------------------|
| 1 | Instructions & Legend | Dashboard guidance | Read-only |
| 2 | Executive Summary | High-level compliance overview | Quarterly |
| 3 | Domain 1 Summary | Inventory assessment highlights | Per A.7.10.1 update |
| 4 | Domain 2 Summary | Handling procedures highlights | Per A.7.10.2 update |
| 5 | Domain 3 Summary | Lifecycle tracking highlights | Per A.7.10.3 update |
| 6 | Consolidated Gap Analysis | All gaps across domains | Quarterly |
| 7 | Risk Register | Prioritised risk tracking | Monthly |
| 8 | Remediation Roadmap | Timeline and milestones | Monthly |
| 9 | Evidence Master Index | All evidence references | Per assessment update |
| 10 | KPI Dashboard | Performance metrics and trends | Monthly |
| 11 | CISO Approval | Executive sign-off | Quarterly |

---

# Using the Dashboard

## Step 1: Review Executive Summary (Sheet 2)

**Objective:** Understand overall compliance posture

**Key Metrics:**
- **Overall Compliance %:** Weighted average across all domains
- **Critical Gaps:** Count of high-severity issues
- **Remediation Progress:** % of planned actions completed
- **Trend Indicator:** Improvement/decline vs. previous period

**Traffic Light Status:**
- **Green (>80%):** Satisfactory compliance
- **Amber (60-80%):** Improvement needed
- **Red (<60%):** Significant gaps requiring attention

**Detailed Executive Summary Elements:**

**Compliance Score Calculation:**
- Domain 1 (Inventory): 35% weight
- Domain 2 (Handling): 35% weight
- Domain 3 (Lifecycle): 30% weight
- Overall = Weighted average of domain scores

**Trend Analysis Components:**
- Current period score
- Previous period score
- Change percentage
- Trend direction indicator

**Executive Attention Items:**
- Critical gaps requiring immediate action
- Overdue remediation items
- Upcoming compliance deadlines
- Resource constraints identified

## Step 2: Review Domain Summaries (Sheets 3-5)

**Objective:** Understand status within each assessment area

**For each domain:**
- Key findings summary
- Compliance percentage
- Critical gaps identified
- Evidence coverage
- Next assessment date

**Domain 1: Storage Media Inventory (Sheet 3)**
- Total media items tracked
- Registration compliance rate
- Encryption coverage for CONFIDENTIAL
- Custodian assignment rate
- Overdue media returns

**Domain 2: Media Handling Procedures (Sheet 4)**
- Access control compliance
- Transportation security status
- Chain of custody adherence
- Incident response readiness
- Training completion rate

**Domain 3: Media Lifecycle Tracking (Sheet 5)**
- Disposal compliance rate
- Certificate collection rate
- Vendor certification status
- Re-use verification rate
- Environmental compliance

## Step 3: Review Consolidated Gap Analysis (Sheet 6)

**Objective:** Prioritise remediation efforts

**Gap Categories:**
- **Policy Gaps:** Missing or inadequate policies
- **Procedure Gaps:** Undocumented or incomplete procedures
- **Technical Gaps:** Missing controls or tools
- **People Gaps:** Training, awareness, accountability

**Priority Matrix:**

| Risk Level | Timeline | Escalation |
|------------|----------|------------|
| Critical | 30 days | CISO + Executive |
| High | 90 days | CISO |
| Medium | 180 days | IT Director |
| Low | 365 days | IT Operations |

**Gap Analysis Process:**

1. **Extract gaps** from each domain assessment
2. **Assign unique ID** (GAP-001, GAP-002, etc.)
3. **Categorise by type** (Policy/Procedure/Technical/People)
4. **Assess risk level** using impact/likelihood matrix
5. **Assign owner** for remediation
6. **Set target date** based on risk level
7. **Link to evidence** of gap and remediation

**Gap Consolidation Checklist:**
- All domain gaps captured
- No duplicate entries
- Consistent risk assessment
- Owners assigned to all gaps
- Target dates realistic

## Step 4: Update Risk Register (Sheet 7)

**Objective:** Track risk treatment decisions

**For each identified risk:**
1. Assign unique Risk ID
2. Document risk description
3. Assess impact and likelihood
4. Calculate risk score
5. Assign risk owner
6. Select treatment option (Mitigate/Accept/Transfer/Avoid)
7. Document treatment plan
8. Track treatment status

**Risk Assessment Matrix:**

| Likelihood / Impact | Negligible (1) | Minor (2) | Moderate (3) | Significant (4) | Severe (5) |
|---------------------|----------------|-----------|--------------|-----------------|------------|
| Almost Certain (5) | 5 | 10 | 15 | 20 | 25 |
| Likely (4) | 4 | 8 | 12 | 16 | 20 |
| Possible (3) | 3 | 6 | 9 | 12 | 15 |
| Unlikely (2) | 2 | 4 | 6 | 8 | 10 |
| Rare (1) | 1 | 2 | 3 | 4 | 5 |

**Risk Rating Thresholds:**
- Critical: Score 20-25
- High: Score 12-19
- Medium: Score 6-11
- Low: Score 1-5

**Risk Treatment Options:**
- **Mitigate:** Implement controls to reduce risk
- **Accept:** Acknowledge and monitor (requires CISO approval)
- **Transfer:** Insurance or contractual transfer
- **Avoid:** Eliminate the activity causing risk

## Step 5: Manage Remediation Roadmap (Sheet 8)

**Objective:** Plan and track remediation activities

**For each remediation action:**
1. Link to gap/risk
2. Define specific action
3. Assign owner
4. Set target date
5. Estimate resources/budget
6. Track progress (%)
7. Update status

**Milestone Tracking:**
- Quick wins (30 days)
- Short-term improvements (90 days)
- Medium-term initiatives (180 days)
- Long-term programmes (365 days)

**Remediation Action Types:**

**Policy Updates:**
- Draft policy revision
- Review and approval cycle
- Communication and training
- Effectiveness verification

**Procedure Implementation:**
- Procedure documentation
- Pilot implementation
- Full rollout
- Compliance verification

**Technical Controls:**
- Requirements definition
- Solution selection/procurement
- Implementation and testing
- Operational handover

**Training and Awareness:**
- Training material development
- Delivery schedule
- Completion tracking
- Effectiveness assessment

**Roadmap Reporting:**
- Actions on track count
- Actions delayed count
- Actions completed count
- Overall progress percentage

## Step 6: Verify Evidence Index (Sheet 9)

**Objective:** Ensure complete audit trail

**Evidence Categories:**
- Policy and procedure documents
- Assessment workbooks
- Certificates of destruction
- Training records
- Audit reports
- System configurations

**Evidence Requirements:**
- Unique identifier
- Related control/gap
- Location/link
- Date collected
- Retention period
- Owner

**Evidence Management Best Practices:**

**Naming Convention:**
```
EV-[Domain]-[Seq]-[Type]-[Description]
Example: EV-D1-001-CERT-Encryption_Certificate
```

**Storage Requirements:**
- Centralised evidence repository
- Access controls appropriate for classification
- Backup and recovery provisions
- Retention schedule compliance

**Evidence Quality Criteria:**
- Dated and timestamped
- Authored or attributed
- Relevant to control/gap
- Complete (not partial)
- Authentic (original or certified copy)

## Step 7: Monitor KPI Dashboard (Sheet 10)

**Objective:** Track performance trends

**Key Performance Indicators:**

| KPI | Target | Measurement |
|-----|--------|-------------|
| Registered media % | 100% | Asset inventory |
| Encrypted CONFIDENTIAL media % | 100% | Encryption reports |
| Authorised removable media % | 100% | Registry vs. detected |
| Media disposal with certificate % | 100% | Certificate tracking |
| Chain of custody compliance % | 100% | Transfer documentation |
| Media loss incidents | 0 | Incident records |
| Overdue media returns | <3 | Asset tracking |
| Media audit completion % | 100% | Audit records |

**KPI Categories:**

**Inventory KPIs:**
- Registration rate
- Encryption compliance
- Custodian assignment
- Location accuracy

**Handling KPIs:**
- Chain of custody adherence
- Approved courier usage
- Access control compliance
- Training completion

**Lifecycle KPIs:**
- Disposal certificate rate
- Vendor compliance
- Re-use verification
- Environmental compliance

**Trend Indicators:**
- Improving (green arrow up)
- Stable (yellow dash)
- Declining (red arrow down)

**KPI Reporting Schedule:**
- Monthly data collection
- Quarterly trend analysis
- Annual benchmarking

## Step 8: Executive Approval (Sheet 11)

**Objective:** Formalise governance review

**Quarterly Review Includes:**
1. Overall compliance status acknowledgment
2. Risk acceptance for residual gaps
3. Remediation plan approval
4. Resource allocation confirmation
5. Executive signature

**Approval Workflow:**

**Pre-Meeting Preparation:**
- Dashboard updated with current data
- Significant changes highlighted
- Risk acceptance requests documented
- Resource requirements summarised

**Meeting Agenda:**
- Compliance status review (15 min)
- Critical gaps discussion (15 min)
- Risk acceptance decisions (15 min)
- Resource requests (10 min)
- Sign-off (5 min)

**Post-Meeting Actions:**
- Meeting minutes documented
- Approval sheet updated
- Action items assigned
- Next review scheduled

---

# Common Pitfalls

## Dashboard Data Staleness

**❌ MISTAKE:** Dashboard not updated when source assessments change

**Why This Fails:**
- Executive decisions based on outdated data
- Gaps may worsen undetected
- Audit findings for poor monitoring

**✅ Prevention:**
- Quarterly minimum refresh cycle
- Automated data links where possible
- Dashboard owner assigned

## Incomplete Gap Consolidation

**❌ MISTAKE:** Gaps from some assessments not transferred to consolidated view

**Why This Fails:**
- Incomplete risk picture
- Some gaps escape remediation
- Inconsistent reporting

**✅ Prevention:**
- Systematic gap extraction process
- Cross-reference checklist
- Validation before executive review

## No Risk Owner Assignment

**❌ MISTAKE:** Risks in register without assigned owners

**Why This Fails:**
- No accountability for treatment
- Remediation stalls
- Audit finding for governance gap

**✅ Prevention:**
- Mandatory owner field
- Owner confirmation process
- Escalation for unassigned risks

## Remediation Tracking Abandonment

**❌ MISTAKE:** Roadmap created but not maintained

**Why This Fails:**
- Progress invisible
- Deadlines missed
- Continuous improvement fails

**✅ Prevention:**
- Monthly status updates required
- Automated deadline reminders
- Management review of progress

## KPI Targets Not Realistic

**❌ MISTAKE:** Setting 100% targets without baseline

**Why This Fails:**
- Demoralising when targets missed
- No recognition of improvement
- Gaming behaviour possible

**✅ Prevention:**
- Establish baseline before targets
- Set progressive improvement targets
- Celebrate milestone achievements

## Evidence Not Linked

**❌ MISTAKE:** Evidence exists but not referenced in dashboard

**Why This Fails:**
- Auditors cannot verify claims
- Evidence may be lost or forgotten
- Duplication of evidence gathering

**✅ Prevention:**
- Mandatory evidence reference for each claim
- Central evidence repository
- Regular evidence verification

## No Trend Analysis

**❌ MISTAKE:** Point-in-time metrics without historical comparison

**Why This Fails:**
- Cannot demonstrate improvement
- Recurring issues not identified
- Investment justification weak

**✅ Prevention:**
- Archive previous dashboard versions
- Include trend charts
- Period-over-period commentary

## Executive Disengagement

**❌ MISTAKE:** Dashboard produced but not reviewed at executive level

**Why This Fails:**
- Governance oversight missing
- Resource requests unsupported
- Accountability unclear

**✅ Prevention:**
- Calendar executive review quarterly
- Dashboard on management committee agenda
- Sign-off requirement enforced

## Risk Scores Not Calibrated

**❌ MISTAKE:** Inconsistent risk scoring across different gaps

**Why This Fails:**
- Prioritisation unreliable
- Resources misallocated
- Audit questions on methodology

**✅ Prevention:**
- Documented scoring methodology
- Calibration workshops
- Peer review of high/critical scores

## Remediation Dependencies Ignored

**❌ MISTAKE:** Actions planned without considering dependencies

**Why This Fails:**
- Blocked actions cannot proceed
- Critical path not identified
- Delays cascade through roadmap

**✅ Prevention:**
- Map dependencies explicitly
- Identify critical path
- Prioritise enabling actions

## KPI Gaming

**❌ MISTAKE:** Metrics improved by changing measurement rather than control

**Why This Fails:**
- False sense of security
- Underlying issues persist
- Trust in reporting damaged

**✅ Prevention:**
- Consistent measurement definitions
- Independent verification of metrics
- Focus on outcomes not just numbers

## Gap Closure Without Verification

**❌ MISTAKE:** Marking gaps as closed without verifying remediation

**Why This Fails:**
- Gaps may reopen
- Controls not actually effective
- Audit finding for inadequate closure

**✅ Prevention:**
- Verification step before closure
- Evidence of effective remediation
- Post-implementation review

## Evidence Repository Inaccessible

**❌ MISTAKE:** Evidence stored but auditors cannot access

**Why This Fails:**
- Audit delays
- Evidence validity questioned
- Compliance cannot be demonstrated

**✅ Prevention:**
- Clear access procedures for auditors
- Read access for appropriate roles
- Location documented in index

## No Risk Acceptance Documentation

**❌ MISTAKE:** Risks accepted verbally without documentation

**Why This Fails:**
- No audit trail of decisions
- Accountability unclear
- Re-litigation of decisions

**✅ Prevention:**
- Formal risk acceptance form
- Signature required
- Retention with risk register

## Metrics Not Actionable

**❌ MISTAKE:** KPIs reported but no response to declining trends

**Why This Fails:**
- Reporting without management
- Issues escalate unaddressed
- Dashboard becomes "wallpaper"

**✅ Prevention:**
- Trigger thresholds defined
- Action required when threshold breached
- Escalation path documented

## Quarterly Review Skipped

**❌ MISTAKE:** Executive review postponed or cancelled

**Why This Fails:**
- Governance gap
- Decisions delayed
- Compliance posture unknown

**✅ Prevention:**
- Protected calendar time
- Deputy attendance if principal unavailable
- Written review if meeting impossible

## Domain Assessment Timing Misaligned

**❌ MISTAKE:** Domain assessments completed at different times with large gaps

**Why This Fails:**
- Consolidated view inconsistent
- Comparisons unreliable
- Overall picture distorted

**✅ Prevention:**
- Coordinate assessment timing
- Rolling assessment window (e.g., 30 days)
- Note assessment dates on dashboard

## No Continuous Improvement Loop

**❌ MISTAKE:** Same issues appearing repeatedly without process improvement

**Why This Fails:**
- Root causes not addressed
- Resources wasted on repeat issues
- Maturity stagnates

**✅ Prevention:**
- Root cause analysis for recurring gaps
- Process improvement actions tracked
- Lessons learned incorporated

---

# Quality Checklist

Before executive presentation, verify:

## Data Quality

- [ ] Source assessments current (within 90 days)
- [ ] All domains represented
- [ ] Metrics calculated correctly
- [ ] External links functioning (if applicable)
- [ ] Data extraction verified against source
- [ ] Calculation formulas audited

## Completeness

- [ ] Executive Summary populated
- [ ] All domain summaries complete
- [ ] Gap analysis consolidated
- [ ] Risk register current
- [ ] Remediation roadmap updated
- [ ] Evidence index complete
- [ ] KPI dashboard populated

## Accuracy

- [ ] Compliance percentages validated
- [ ] Gap counts reconciled to source
- [ ] Risk scores correctly calculated
- [ ] Remediation progress accurate
- [ ] Trend indicators correct
- [ ] Evidence references verified
- [ ] Owner assignments current

## Governance

- [ ] Previous actions reviewed
- [ ] New risks identified and assessed
- [ ] Remediation progress documented
- [ ] Executive approval section prepared
- [ ] Meeting agenda distributed
- [ ] Prior meeting actions tracked

## Presentation Quality

- [ ] Dashboard formatting consistent
- [ ] Charts and graphs clear
- [ ] Executive summary concise
- [ ] Key messages highlighted
- [ ] Recommendations prioritised
- [ ] Resource requests documented

## Evidence Readiness

- [ ] All evidence accessible
- [ ] Evidence index current
- [ ] Evidence retention appropriate
- [ ] Audit trail complete
- [ ] Sensitive evidence protected
- [ ] Evidence backup verified

## Stakeholder Preparation

- [ ] CISO briefing completed
- [ ] IT Director input obtained
- [ ] Compliance Officer review complete
- [ ] Finance input on resource requests
- [ ] HR input on training status

---

# Review & Approval

## Approval Workflow

**Quarterly Executive Review Process:**

**Week 1-2: Preparation**
- Domain assessments updated
- Gap analysis consolidated
- Risk register reviewed
- KPIs calculated
- Dashboard compiled

**Week 3: Review**
- Technical review by ISMS team
- Management review by CISO/IT Director
- Finance review of resource requests

**Week 4: Executive Approval**
- Executive presentation
- Risk acceptance decisions
- Resource allocation approval
- Sign-off obtained

**Post-Approval:**
- Dashboard archived
- Actions communicated
- Next cycle planned

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
