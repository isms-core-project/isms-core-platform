**ISMS-IMP-A.5.4.2-UG - Compliance Oversight Tracker**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.4: Management Responsibilities

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.2-UG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

### 1. Assessment Overview

#### 1.1 Purpose

This workbook tracks how managers ensure their teams comply with information security requirements. It monitors training oversight, policy violation handling, and access review participation with escalation triggers for underperforming areas.

#### 1.2 Scope

Tracks compliance oversight activities for:
- All managers with direct reports
- Quarterly metrics by department
- Escalation triggers for threshold breaches

#### 1.3 Control Requirement

Per ISO/IEC 27001:2022 Control A.5.4: *"Management should require all personnel to apply information security in accordance with the established information security policy."*

This workbook operationalises management oversight of that requirement by tracking three critical compliance dimensions:
1. **Training Oversight** - Are managers ensuring their teams complete required security training?
2. **Policy Violation Response** - How effectively do managers address security policy violations?
3. **Access Review Participation** - Are managers fulfilling their access certification responsibilities?

#### 1.4 Why This Matters

**The Management Accountability Gap**: Many organisations have strong security policies but weak management enforcement. This creates an "accountability gap" where:
- Policies exist but aren't consistently applied
- Training is assigned but not followed up
- Violations occur but aren't addressed
- Access reviews are scheduled but not completed thoroughly

**This workbook closes that gap** by providing objective, measurable evidence of management oversight activities. When an auditor asks "How do you know managers are enforcing security policies?", this workbook provides the answer.

**Real-World Impact**:
- A department with 60% training completion has 3x more security incidents than one with 95% completion
- Managers who don't respond to violations within 15 days see repeat offence rates double
- Incomplete access reviews leave 15-20% of inappropriate access undetected

**The ISMS Copilot Connection**: During Stage 2 audits, auditors will ask for evidence of management oversight effectiveness. This workbook provides:
- Trend data showing compliance improvement (or decline) over time
- Escalation records proving the organisation acts on non-compliance
- Correlation between training gaps and violation patterns

### 2. Prerequisites

Before beginning this assessment, ensure access to:

- [ ] Learning Management System (LMS) training reports
- [ ] Security incident/violation register
- [ ] Access review completion records
- [ ] Manager contact information
- [ ] Prior quarter data (for trend analysis)
- [ ] HR system manager hierarchy (to verify manager list is current)
- [ ] Department head contact list (for escalations)

**Verification Steps**:

1. **LMS Access Verification**: Export a test report covering the previous month. Verify the report includes:
   - Manager identification (name/ID)
   - Team member training assignments
   - Completion status with dates
   - Overdue items highlighted

2. **Violation Register Format**: Confirm the incident register includes manager attribution. If violations are logged without manager identification, coordinate with incident management to add this field.

3. **Access Review Calendar**: Obtain the current year's access review schedule. Confirm which reviews have occurred and which are upcoming. Note any managers who were absent and require delegate assignments.

4. **Baseline Data**: If this is the first assessment cycle, establish baselines by:
   - Recording current training completion rates as "starting point"
   - Documenting any open violations as "inherited"
   - Marking prior access reviews as "historical reference"

### 3. Workbook Structure

| Sheet | Purpose | Update Frequency |
|-------|---------|------------------|
| **Instructions** | Guidance and escalation thresholds | Reference |
| **Training Oversight** | Track team training completion | Monthly |
| **Policy Violations** | Log violations and manager response | As occurred |
| **Access Reviews** | Record access review participation | Per review cycle |
| **Escalation Triggers** | Monitor thresholds and log escalations | Continuous |
| **Quarterly Summary** | Aggregate metrics for reporting | Quarterly |

### 4. Escalation Triggers

**Per ISMS Copilot Audit Requirements:**

| Metric | Threshold | Condition | Escalation Action |
|--------|:---------:|-----------|-------------------|
| Training Completion Rate | 90% | Below | Escalate to CISO |
| Policy Violations | 5 | Above | Manager performance review |
| Manager Response Time | 15 days | Above | Escalate to Department Head |

When thresholds are breached:
1. Log the escalation in the Escalation Triggers sheet
2. Notify the appropriate authority
3. Track resolution and document outcome
4. Review root cause to prevent recurrence

### 5. Completion Walkthrough

#### Step 1: Training Oversight (Monthly)

For each manager, record:
1. **Team_Size**: Number of direct reports
2. **Training_Required**: Number of training modules required
3. **Training_Completed**: Number completed across team
4. **Completion_Rate**: Auto-calculated (target: ≥90%)
5. **Overdue_Count**: Personnel with overdue training
6. **Follow_Up_Actions**: What manager is doing about overdue items
7. **Last_Review_Date**: When manager last reviewed training status

#### Step 2: Policy Violations (As Occurred)

When a policy violation involves a manager's team:
1. Assign **Violation_ID** (format: VIO-YYYY-NNN)
2. Record **Date_Reported** and manager details
3. Select **Violation_Type** and **Severity**
4. Document **Manager_Response** action taken
5. Track to **Resolution**
6. Capture **Lessons_Learned** for trend analysis

**Response Time Target**: Manager acknowledgment within 2 business days

#### Step 3: Access Reviews (Per Cycle)

For each access review cycle:
1. Record **Review_ID** and **Review_Period**
2. Document manager's **System_Scope** (what they reviewed)
3. Count **Accounts_Reviewed** and **Changes_Requested**
4. Mark **Review_Completed** (Yes/No/Partial)
5. Add notes on any issues or delays

#### Step 4: Escalation Triggers (Continuous)

When a threshold is breached:
1. Generate **Escalation_ID** (format: ESC-YYYY-NNN)
2. Record the **Metric_Triggered** and **Actual_Value**
3. Identify **Escalated_To** (CISO, Department Head, HR)
4. Track **Resolution** status
5. Document **Resolution_Date** when closed

#### Step 5: Quarterly Summary

Aggregate all data quarterly:
1. Calculate **Training_Compliance_Rate** (target: ≥90%)
2. Count **Violations_Handled**
3. Calculate **Avg_Response_Days** (target: ≤15 days)
4. Verify **Access_Reviews_Completed** (target: 100%)
5. Assign **Overall_Rating**: Exceeds, Meets, Below, N/A

### 6. Worked Examples

#### Example A: High-Performing Manager (Sarah Chen, Engineering)

**Training Oversight Entry**:
| Field | Value | Notes |
|-------|-------|-------|
| Manager_ID | MGR-0042 | |
| Manager_Name | Sarah Chen | |
| Department | Engineering | |
| Team_Size | 12 | |
| Training_Required | 36 | 3 modules × 12 team members |
| Training_Completed | 35 | 1 person on parental leave |
| Completion_Rate | 97.2% | ✅ Above 90% threshold |
| Overdue_Count | 1 | |
| Follow_Up_Actions | Scheduled completion for returning employee in Week 2 | |
| Last_Review_Date | 15-Jan-2026 | Reviews weekly |

**Why Sarah Scores Well**:
- Proactively tracks training status
- Has documented follow-up plan for exceptions
- Reviews regularly (not waiting until quarter-end)
- Completion rate well above threshold

**Quarterly Summary Rating**: **Exceeds** (97.2% training, 0 violations, 100% access reviews)

---

#### Example B: At-Risk Manager (James Wilson, Sales)

**Training Oversight Entry**:
| Field | Value | Notes |
|-------|-------|-------|
| Manager_ID | MGR-0078 | |
| Manager_Name | James Wilson | |
| Department | Sales | |
| Team_Size | 8 | |
| Training_Required | 24 | 3 modules × 8 team members |
| Training_Completed | 18 | Several overdue >30 days |
| Completion_Rate | 75% | ⚠️ Below 90% threshold |
| Overdue_Count | 6 | |
| Follow_Up_Actions | "Will remind team next week" | Vague, no specific plan |
| Last_Review_Date | 01-Nov-2025 | >2 months since last review |

**Policy Violations (Q4)**:
| Violation_ID | Date | Type | Severity | Response | Days |
|--------------|------|------|----------|----------|------|
| VIO-2026-023 | 10-Jan | Password sharing | High | Coaching | 18 |
| VIO-2026-031 | 22-Jan | Unencrypted data transfer | Medium | No Action | - |

**Why James Triggers Escalation**:
1. Training completion (75%) is below 90% threshold → **Escalate to CISO**
2. Response time (18 days) exceeds 15-day threshold → **Escalate to Department Head**
3. "No Action" on violation is unacceptable → **Immediate review required**
4. Vague follow-up actions suggest disengagement
5. >2 months without reviewing training status

**Escalation Triggers Entry**:
| Escalation_ID | Date | Metric_Triggered | Actual_Value | Escalated_To |
|---------------|------|------------------|--------------|--------------|
| ESC-2026-008 | 25-Jan | Training Completion Rate | 75% | CISO |
| ESC-2026-009 | 28-Jan | Manager Response Time | 18 days | Department Head (Sales) |

**Quarterly Summary Rating**: **Below** (75% training, 2 violations with poor response, escalation required)

---

#### Example C: Interpreting Access Review Data

**Good Access Review Record**:
| Review_ID | Manager | System_Scope | Accounts | Changes | Completed |
|-----------|---------|--------------|:--------:|:-------:|-----------|
| AR-2026-Q1-015 | Maria Santos | CRM + Marketing Platform | 45 | 7 | Yes |

**Interpretation**: Maria reviewed 45 accounts, identified 7 requiring changes (15.5% change rate). A 10-20% change rate is typical for thorough reviews. 0% change rate may indicate rubber-stamping.

**Concerning Access Review Record**:
| Review_ID | Manager | System_Scope | Accounts | Changes | Completed |
|-----------|---------|--------------|:--------:|:-------:|-----------|
| AR-2026-Q1-022 | Tom Harris | Finance Systems (SAP, Treasury) | 28 | 0 | Partial |

**Interpretation**: Tom reviewed 28 accounts in sensitive finance systems but requested zero changes, and review is marked "Partial". This requires follow-up:
- Was the review thorough or perfunctory?
- Why "Partial" status? Which systems incomplete?
- Zero changes on finance systems is unusual (staff turnover, role changes typically require adjustments)

### 7. Escalation Workflow Details

#### Escalation Level 1: Training Compliance (<90%)

**Trigger**: Any manager with training completion rate below 90%

**Immediate Actions**:
1. Log in Escalation Triggers sheet (same day)
2. Email notification to CISO with:
   - Manager name and department
   - Current completion rate
   - Number of overdue training items
   - Gap analysis (what training is missing)
3. CC manager's department head

**Resolution Path**:
1. CISO reviews within 3 business days
2. Meeting scheduled with manager within 5 business days
3. Remediation plan with specific completion dates required
4. Follow-up check at 2-week and 4-week marks
5. Close escalation when ≥90% achieved

**If Unresolved After 30 Days**:
- Escalate to HR for inclusion in performance review
- Document in manager's personnel file (if organisation policy allows)
- Consider temporary restriction of manager's system access

---

#### Escalation Level 2: Policy Violations (>5 per quarter)

**Trigger**: Any manager with more than 5 policy violations in their team per quarter

**Immediate Actions**:
1. Log in Escalation Triggers sheet
2. Compile violation summary report
3. Analyse patterns:
   - Are violations concentrated in specific employees?
   - Common violation types (suggests training gap)?
   - Timing patterns (end of month, after-hours)?

**Resolution Path**:
1. Meeting with manager and department head
2. Root cause analysis required
3. Targeted intervention plan (training, process change, personnel action)
4. Weekly tracking until violations trend downward
5. Close escalation when violations <3 for subsequent quarter

---

#### Escalation Level 3: Response Time (>15 days)

**Trigger**: Manager takes longer than 15 business days to respond to reported violation

**Immediate Actions**:
1. Log in Escalation Triggers sheet
2. Notify Department Head directly
3. Document impact of delayed response (potential continued risk exposure)

**Resolution Path**:
1. Department Head contacts manager within 2 business days
2. Manager must provide response action within 5 business days of escalation
3. Coaching on expected response times
4. Close escalation when response received

**Repeat Offenders**: Managers with 3+ response time escalations in 12 months require HR involvement.

### 8. Evidence Collection

| Data Type | Source | Retention |
|-----------|--------|-----------|
| Training completion | LMS exports | 3 years |
| Violation records | Incident register | 7 years |
| Access review logs | IAM system | 3 years |
| Escalation records | This workbook | 3 years |
| Manager communications | Email/tickets | 3 years |

**Evidence Storage**: `[SharePoint/Evidence Library]/A.5.4/Compliance-Oversight/[Year]/[Quarter]/`

### 7. Common Pitfalls

❌ **MISTAKE**: Waiting until quarter-end to update training data
✅ **CORRECT**: Update Training Oversight sheet monthly

❌ **MISTAKE**: Not logging violations handled informally
✅ **CORRECT**: Document ALL violations, including coaching conversations

❌ **MISTAKE**: Ignoring escalation triggers hoping metrics improve
✅ **CORRECT**: Escalate immediately when thresholds are breached

❌ **MISTAKE**: Recording only the final outcome of violations
✅ **CORRECT**: Document the full timeline from report to resolution

❌ **MISTAKE**: Skipping access reviews for managers on leave
✅ **CORRECT**: Assign delegate or reschedule; document exception

❌ **MISTAKE**: Using inconsistent violation severity classifications
✅ **CORRECT**: Apply severity criteria consistently (Critical/High/Medium/Low)

❌ **MISTAKE**: Not correlating violations with training gaps
✅ **CORRECT**: Analyse whether training deficiencies contributed to violations

❌ **MISTAKE**: Failing to close escalations formally
✅ **CORRECT**: Document Resolution_Date and outcome for all escalations

❌ **MISTAKE**: Accepting "I'll handle it" as a manager response to violations
✅ **CORRECT**: Require specific documented actions (coaching session, written warning, training assignment)

❌ **MISTAKE**: Treating all violations equally regardless of severity
✅ **CORRECT**: Apply proportionate responses - Critical violations require immediate action, Low violations may be addressed in regular 1:1s

### 9. Trend Analysis

#### Quarterly Trend Indicators

After 2+ quarters of data, analyse trends to identify systemic issues:

**Improving Trend Indicators** (Good Signs):
- Training completion rates increasing quarter-over-quarter
- Average response time to violations decreasing
- Fewer escalations triggered each quarter
- Higher percentage of violations resulting in "Resolved" status

**Concerning Trend Indicators** (Requires Intervention):
- Consistent underperformance by same managers
- Violation types clustering (e.g., repeated password issues suggest training gap)
- Escalation closure times increasing (suggests process fatigue)
- Access review change rates near 0% (suggests rubber-stamping)

#### Cross-Reference Analysis

Compare Compliance Oversight data with other A.5.4 assessments:

| If You See... | Cross-Reference With... | Likely Root Cause |
|---------------|-------------------------|-------------------|
| High violation rates | A.5.4.1 Security Leadership score | Low management visibility/support |
| Poor training completion | A.5.4.4 Culture Survey | Perceived lack of training relevance |
| Delayed responses | A.5.4.1 Resource Allocation score | Manager capacity/workload issues |
| Repeated escalations | A.5.4.3 Dashboard trends | Department-specific culture issues |

#### Department Comparison

Create quarterly department comparison to identify outliers:

| Department | Training % | Violations | Avg Response | Access Reviews | Status |
|------------|:----------:|:----------:|:------------:|:--------------:|--------|
| Engineering | 97% | 1 | 3 days | 100% | ✅ |
| Sales | 75% | 4 | 18 days | 75% | ⚠️ |
| Finance | 92% | 2 | 8 days | 100% | ✅ |
| Marketing | 88% | 3 | 12 days | 100% | ⚠️ |

**Investigation Priority**: Sales department requires immediate attention across all metrics.

### 10. Quality Checklist

Before quarterly reporting:

- [ ] Training Oversight updated for all managers
- [ ] All violations logged with complete details
- [ ] Access review participation recorded
- [ ] Escalation triggers reviewed and documented
- [ ] Quarterly Summary calculated accurately
- [ ] Managers below target have documented improvement plans
- [ ] Evidence files organised in SharePoint
- [ ] Workbook saved with correct naming convention
- [ ] Trend analysis completed (if Q2 or later)
- [ ] Department comparison chart updated
- [ ] All escalations have documented resolution or status update

### 11. Review and Approval

| Role | Responsibility | Frequency |
|------|----------------|-----------|
| IS Analyst | Update all sheets | Monthly |
| Security Manager | Validate data accuracy | Monthly |
| CISO | Review escalations; approve quarterly summary | Quarterly |
| Department Heads | Address escalations in their departments | As needed |

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
