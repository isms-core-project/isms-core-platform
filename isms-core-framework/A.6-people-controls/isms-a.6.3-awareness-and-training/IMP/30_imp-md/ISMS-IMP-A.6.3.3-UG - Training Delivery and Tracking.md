**ISMS-IMP-A.6.3.3-UG - Training Delivery and Tracking**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.6.3: Information Security Awareness, Education and Training

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.3.3-UG |
| **Version** | 1.0 |
| **Assessment Area** | Training Completion Tracking and Effectiveness Measurement |
| **Related Policy** | ISMS-POL-A.6.3, Section 2.5 (Delivery Requirements), Section 2.6 (Competency Assessment) |
| **Purpose** | Track training completion, measure assessment results, manage remediation, and verify competency across all personnel |
| **Target Audience** | HR Training Administrators, LMS Administrators, Department Managers, Information Security Officers |
| **Assessment Type** | Operational Tracking & Compliance Monitoring |
| **Review Cycle** | Continuous tracking + Monthly reporting + Quarterly analysis |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Initial | Initial specification for Training Delivery and Tracking workbook | ISMS Implementation Team |

---

**Audience:** HR Training Administrators, LMS Administrators, Department Managers

---

# Assessment Overview

## What This Assessment Measures

This workbook tracks training delivery, completion status, assessment results, and remediation activities to ensure all personnel complete required training and demonstrate required competencies per ISMS-POL-A.6.3.

**Scope:** 5 tracking domains:
1. **Completion Tracking** - Who has completed what training
2. **Assessment Results** - Test scores and competency verification
3. **Simulation Results** - Phishing and behavioral testing outcomes
4. **Remediation Tracking** - Failed assessments and corrective actions
5. **Compliance Status** - Overall compliance by department/role

**Assessment Output:** Excel workbook documenting:
- Individual training completion records
- Assessment scores and pass/fail status
- Simulation campaign results
- Remediation cases and outcomes
- Department and organizational compliance metrics
- Overdue training alerts

## Why This Matters

**Regulatory Requirements:**
- ISO 27001:2022 Clause 7.2(d): "retain appropriate documented information as evidence of competence"
- GDPR Art. 32: Evidence that appropriate technical and organizational measures are in place
- Most regulatory frameworks require training completion records as audit evidence

**Business Impact:**
- **Audit Evidence:** Documented completion records demonstrate compliance
- **Risk Visibility:** Identify departments/roles with training gaps
- **Intervention Timing:** Early identification of non-compliance enables proactive remediation
- **Effectiveness Measurement:** Assessment data validates training quality

## Who Should Complete This Assessment

**Primary Responsibility:** HR Training Administrator / LMS Administrator

**Process:** This is an ongoing operational workbook, not a one-time assessment:
- Training completions recorded as they occur (often automated from LMS)
- Assessment results recorded upon completion
- Simulation results imported after each campaign
- Monthly compliance reports generated
- Quarterly trend analysis performed

## Connection to Policy

This workbook tracks compliance with **ISMS-POL-A.6.3, Sections 2.5-2.6**:
- Section 2.5.2: Training timing and frequency requirements
- Section 2.6: Competency assessment requirements

---

# Operational Procedures

## Daily Operations

**LMS Administrator Tasks:**
1. **Import New Hires:** Add new personnel to Personnel_Register within 1 business day of start
2. **Assign Training:** Ensure onboarding training assigned based on tier classification
3. **Monitor Completions:** Review completion imports from LMS
4. **Update Status:** Mark terminated employees as inactive

## Weekly Operations

**Training Administrator Tasks:**
1. **Overdue Report Review:**
   - Generate overdue alerts (Sheet 8)
   - Send reminder notifications for training due within 7 days
   - Send escalation notifications for overdue >7 days

2. **Remediation Follow-Up:**
   - Check remediation completion status
   - Escalate unresolved remediation cases
   - Update remediation outcomes

**Report Distribution:**
| Report | Recipients | Day |
|--------|------------|-----|
| Overdue Summary | Department Managers | Monday |
| Critical Overdue (>30 days) | CISO | Friday |

## Monthly Operations

**Training Manager Tasks:**
1. **Compliance Summary Generation:**
   - Update Compliance_Summary (Sheet 7) metrics
   - Calculate department compliance rates
   - Identify trends and patterns

2. **Management Reporting:**
   - Generate monthly training compliance report
   - Distribute to department heads
   - Present to security governance meeting

3. **Data Quality Review:**
   - Verify personnel register accuracy
   - Reconcile with HR headcount
   - Clean up terminated employee records

## Quarterly Operations

**Information Security Officer Tasks:**
1. **Trend Analysis:**
   - Compare quarter-over-quarter completion rates
   - Analyze assessment score trends
   - Review simulation campaign effectiveness

2. **Program Effectiveness Review:**
   - Correlate training completion with incident data
   - Identify training that isn't driving behavior change
   - Recommend program adjustments

3. **Governance Reporting:**
   - Present compliance status to CISO/Security Committee
   - Document any systemic issues
   - Propose remediation for chronic non-compliance areas

## Simulation Campaign Operations

**Campaign Execution:**
1. **Pre-Campaign:**
   - Coordinate campaign schedule with ISO
   - Ensure simulation platform configured
   - Prepare remediation training content

2. **During Campaign:**
   - Monitor click rates in real-time (if platform supports)
   - Be prepared for increased help desk calls

3. **Post-Campaign (within 5 business days):**
   - Export results to Sheet 5 (Simulation_Results)
   - Trigger remediation workflow for failures
   - Send educational follow-up to all participants

**Remediation Workflow:**

| Trigger | Level | Action | Timeline |
|---------|-------|--------|----------|
| First click | Level 1 | Additional awareness training | Within 7 days |
| Credential submission | Level 2 | Focused training + manager notification | Within 7 days |
| Repeat failure (2+ campaigns) | Level 3 | Intensive training + HR notification | Within 14 days |

---

# Evidence Collection

## Continuous Evidence Generation

This workbook generates audit evidence through normal operations:

| Evidence Type | Source Sheet | Retention |
|---------------|--------------|-----------|
| Training completion records | Completion_Tracking | 5 years |
| Assessment scores | Assessment_Results | 5 years |
| Simulation results | Simulation_Results | 3 years |
| Remediation records | Remediation_Tracking | 5 years |
| Compliance reports | Compliance_Summary | 5 years |

## Monthly Evidence Snapshot

At month end, create snapshot:
1. Export Compliance_Summary as PDF
2. Export Overdue_Alerts as PDF
3. Generate Dashboard charts as images
4. Store in: `ISMS/Evidence/A.6.3/Tracking/[Year]/[Month]/`

## Audit Request Response

**Common Auditor Requests:**
| Request | Data Source | Report Format |
|---------|-------------|---------------|
| All training completions for period | Completion_Tracking | Filtered Excel |
| Completion rate by department | Compliance_Summary | PDF |
| Failed assessments and remediation | Remediation_Tracking | Filtered Excel |
| Simulation campaign results | Simulation_Results | PDF summary |
| Overdue training list | Overdue_Alerts | Current Excel |

---

# Common Pitfalls

## ❌ MISTAKE #1: Stale Personnel Register

**The Problem:** Personnel register doesn't reflect current workforce - includes terminated employees, missing new hires.

**Why It Matters:** Compliance metrics are wrong. Terminated employees show as "non-compliant." New employees miss required training.

**The Fix:**
- Sync with HR system weekly (automate if possible)
- Remove terminated employees within 1 week of departure
- Add new hires within 1 day of start date
- Reconcile headcount monthly

## ❌ MISTAKE #2: Not Tracking "Not Available" Status

**The Problem:** Tracking only completion, not whether training was assigned or available.

**Why It Matters:** Can't distinguish between "didn't complete" and "wasn't assigned/available."

**The Fix:**
- Use full status spectrum: Not Assigned → Assigned → In Progress → Completed/Overdue
- Track assignment date separately from due date
- Flag modules not yet available for certain tiers

## ❌ MISTAKE #3: Ignoring Simulation Non-Participants

**The Problem:** Only tracking those who received simulation email, not those who should have but were filtered/blocked.

**Why It Matters:** Incomplete simulation coverage. Some employees never tested.

**The Fix:**
- Track Email_Sent status (Yes/No/Filtered)
- Investigate filtered employees (are they on leave? email issue?)
- Report coverage rate, not just click rate

## ❌ MISTAKE #4: Inconsistent Remediation Follow-Through

**The Problem:** Remediation assigned but not tracked to completion; repeat offenders not identified.

**Why It Matters:** Failed training doesn't improve without remediation. Chronic non-compliance not addressed. Audit finding waiting to happen.

**The Fix:**
- Every remediation must have due date and owner
- Escalation at due date + 7 days
- Pattern detection: flag employees with 2+ remediation cases
- Close remediation only when verification complete

## ❌ MISTAKE #5: Point-in-Time Reporting Only

**The Problem:** Only reporting current status, not trends over time.

**Why It Matters:** Can't show improvement or degradation. No early warning of problems. Management doesn't see program value.

**The Fix:**
- Maintain historical data (don't delete old records)
- Generate month-over-month trend reports
- Track key metrics over time: completion rate, click rate, average score

## ❌ MISTAKE #6: No Distinction Between Training Types

**The Problem:** Treating all training equally - phishing simulation same as compliance training same as technical workshop.

**Why It Matters:** Different training types have different implications. Failed phishing simulation requires different remediation than failed compliance quiz.

**The Fix:**
- Categorize by training type in tracking
- Different escalation paths by type
- Type-specific metrics (click rate for simulations, pass rate for assessments)

## ❌ MISTAKE #7: Overdue Notifications Without Escalation

**The Problem:** Sending reminders to employees but never escalating to managers or HR.

**Why It Matters:** Some employees ignore reminders. Without escalation, chronic non-compliance continues.

**The Fix:**
- Tiered notification escalation:
  - Day 1 overdue: Employee reminder
  - Day 7 overdue: Manager notification
  - Day 14 overdue: HR notification
  - Day 30 overdue: CISO notification
- Document all escalations

## ❌ MISTAKE #8: Manual Data Entry Errors

**The Problem:** Manually entering data leads to typos, wrong IDs, duplicate entries.

**Why It Matters:** Data integrity issues. Reports inaccurate. Audit findings for data quality.

**The Fix:**
- Automate imports from LMS where possible
- Use data validation (dropdowns, reference checks)
- Regular data quality reviews (monthly)
- Duplicate detection queries

## ❌ MISTAKE #9: Not Linking Training to Access

**The Problem:** Training completion tracked but not connected to access provisioning decisions.

**Why It Matters:** Employees may have access without required training. POL-A.6.3 Section 2.5.2 requires training before access.

**The Fix:**
- Cross-reference with access management (A.5.15-18)
- Flag access without required training completion
- Consider training as prerequisite for access request approval

## ❌ MISTAKE #10: Ignoring Assessment Validity

**The Problem:** Counting training as "complete" even though assessment hasn't been passed, or counting old completions as current.

**Why It Matters:** Compliance requires demonstrated competency, not just attendance. Training expires.

**The Fix:**
- Completion requires passing assessment (where applicable)
- Track validity period based on training frequency requirement
- Auto-expire completions based on recertification requirements

---

# Quality Checklist

## Data Quality Checks

**Personnel Register:**
- [ ] All active employees present (reconcile with HR)
- [ ] No terminated employees marked as active
- [ ] Tier assignments current (sync with A.6.3.1)
- [ ] Manager assignments accurate

**Completion Tracking:**
- [ ] All required training assigned for each tier
- [ ] Due dates set correctly based on frequency
- [ ] No duplicate assignment records
- [ ] Status formulas calculating correctly

**Assessment Results:**
- [ ] Scores recorded for all completed training
- [ ] Pass/fail threshold applied correctly
- [ ] Attempt count accurate

**Simulation Results:**
- [ ] All campaign participants recorded
- [ ] Click/report times accurate (where captured)
- [ ] Remediation triggered for failures

**Remediation Tracking:**
- [ ] All failures have remediation record
- [ ] Due dates assigned
- [ ] Outcomes recorded when complete
- [ ] Escalations documented

## Report Accuracy Checks

- [ ] Compliance rates calculate correctly
- [ ] Trend data accurate (compare to previous periods)
- [ ] Dashboard charts render properly
- [ ] Overdue alerts current

## Process Checks

- [ ] Notifications being sent (check logs)
- [ ] Escalations occurring per schedule
- [ ] Monthly reports generated on time
- [ ] Evidence archived per schedule

---

# Review & Approval

## Monthly Attestation

**Completed By:** HR Training Administrator
**Review Points:**
- Data quality verified
- Compliance metrics accurate
- Overdue cases addressed or escalated
- Remediation cases progressing

**Approved By:** Information Security Officer
**Review Points:**
- Metrics align with expectations
- Escalations appropriate
- No unexplained trends

## Quarterly Governance Review

**Presented To:** CISO / Security Committee
**Includes:**
- Quarterly compliance summary
- Trend analysis
- Simulation campaign results
- Remediation effectiveness
- Recommendations

**Documentation:**
- Store approved report in evidence library
- Document any decisions/actions from review

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
