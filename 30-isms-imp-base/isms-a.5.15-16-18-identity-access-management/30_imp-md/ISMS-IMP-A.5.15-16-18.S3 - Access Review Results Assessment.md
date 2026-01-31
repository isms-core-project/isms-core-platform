# ISMS-IMP-A.5.15-16-18.S3 - Access Review Results Assessment
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Controls A.5.15 & A.5.18: Access Control & Access Rights

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S3 |
| **Version** | 1.0 |
| **Assessment Area** | Access Review Results & Recertification Compliance |
| **Related Policy** | ISMS-POL-A.5.15-16-18, Section 2.3.4 (Access Review and Recertification Requirements) |
| **Purpose** | Document access review execution, track review completion rates, assess reviewer accountability, and verify access removal for findings in a technology-agnostic manner |
| **Target Audience** | Managers, System Owners, Security Team, IAM Team, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Quarterly (review cycle completion), Monthly (tracking progress) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Access Review Results assessment workbook | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE** (THIS DOCUMENT)
  - Assessment Overview
  - Prerequisites
  - Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION** (SEPARATE DOCUMENT)
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formula Logic
  - Conditional Formatting Rules
  - Integration Points

---

# PART I: USER COMPLETION GUIDE

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.15-16-18.S3 - Access Review Results Assessment

#### What This Assessment Covers

This assessment documents your ACCESS REVIEW EXECUTION and tracks compliance with access recertification requirements. This answers:

- Are access reviews being conducted per policy? (quarterly for critical, annually for standard)
- Which users' access was reviewed? (review scope and coverage)
- Which reviewers completed their reviews? (manager accountability)
- What were the review findings? (access confirmed, removed, or justified with exceptions)
- Were access removal findings remediated? (within 5 business days per policy)
- Are there overdue reviews? (reviews not completed by deadline)
- What is the overall access review completion rate?

#### Key Principle

This assessment is **completely technology-agnostic and process-independent**. Whether you conduct reviews via automated tools (Sailpoint, Saviynt), spreadsheets, or manual manager sign-offs, this assessment captures RESULTS and COMPLIANCE regardless of methodology.

#### What You'll Document

- **Review Scope Definition**: Which systems/users included in each review cycle
  - Review period (Q1 2026, H1 2026, Annual 2025, etc.)
  - Systems in scope (critical quarterly, standard annually)
  - Users in scope (all active users, contractors, privileged access)

- **Review Execution Tracking**:
  - Reviewer assignments (which managers, which system owners)
  - Review completion status (completed, in progress, overdue)
  - Review completion dates (when did reviewer sign off?)
  - Review findings (access confirmed, access removed, access justified)

- **Access Removal Verification**:
  - Access removal requests (from review findings)
  - Removal execution (was access actually removed?)
  - Removal timeliness (within 5 business days per policy?)
  - Removal evidence (audit logs, screenshots)

- **Reviewer Accountability**:
  - Review completion rate by reviewer (manager, system owner)
  - Overdue reviews by reviewer
  - Unresponsive reviewers requiring escalation

- **Gap Analysis**:
  - Reviews not completed (overdue by >30 days)
  - Access removal not executed (findings not remediated)
  - Reviewers consistently missing deadlines (accountability issue)

#### How This Relates to Other A.5.15-16-18 Assessments

| Assessment | Focus | Relationship to A.5.15-16-18.3 |
|------------|-------|--------------------------------|
| ISMS-IMP-A.5.15-16-18.S1 | User Inventory & Lifecycle | Provides user list (.3 uses this for review scope) |
| ISMS-IMP-A.5.15-16-18.S2 | Access Rights Matrix | Provides WHAT access to review (.3 reviews access from .2) |
| **ISMS-IMP-A.5.15-16-18.S3** | **Access Review Results** | **DID we review access and WHAT were findings** |
| ISMS-IMP-A.5.15-16-18.S4 | Role & SoD Compliance | Uses review results to validate role accuracy |
| ISMS-IMP-A.5.15-16-18.S5 | IAM Governance Dashboard | Uses review metrics from .3 for compliance dashboard |

This assessment (A.5.15-16-18.3) verifies that access reviews are **actually happening** and **findings are remediated**!

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Security Team** - Coordinate review cycles, track completion, escalate overdue reviews
2. **Managers** - Review their direct reports' access, sign off on appropriateness
3. **System Owners** - Review access to systems they own, verify business need
4. **IAM Team** - Execute access removal findings, provide review data
5. **HR Team** - Coordinate manager reviews, escalate unresponsive managers

#### Required Skills

- Understanding of access review process
- Access to review tool (Sailpoint, Saviynt, spreadsheets, etc.)
- Project management (tracking review completion across many reviewers)
- Basic understanding of ISO 27001 Controls A.5.15 and A.5.18

#### Time Commitment

- **Initial assessment:** 8-12 hours (document review scope, track completion, analyze findings)
- **Quarterly updates:** 10-15 hours per review cycle (coordinate reviews, track progress, analyze results)
- **Monthly monitoring:** 2-3 hours (track overdue reviews, escalate to managers)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Review scope documentation** - Which systems/users reviewed in each cycle
2. ✅ **Review completion tracking** - Reviewer assignments, completion dates, status
3. ✅ **Review findings summary** - Access confirmed, removed, justified (counts and percentages)
4. ✅ **Access removal verification** - Removal requests executed and verified
5. ✅ **Reviewer accountability metrics** - Completion rates by manager/system owner
6. ✅ **Overdue review tracking** - Reviews not completed, escalation status
7. ✅ **Access review compliance rate** - Overall completion percentage
8. ✅ **Evidence register** - Review sign-offs, removal confirmations, escalations
9. ✅ **Approved assessment** - Three-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Review Scope Definition (from Policy)

- ISMS-POL-A.5.15-16-18, Section 2.3.4 (Access Review and Recertification)
  - Review frequency requirements (quarterly for critical, annually for standard)
  - Review scope (all users, all systems, all groups)
  - Reviewer accountability (managers, system owners, security)

#### 2. Access Data (from IMP.2)

- ISMS-IMP-A.5.15-16-18.S2 Sheet 3 (Access Rights Matrix)
- User-to-system access mapping (what access should be reviewed?)
- Group memberships (which groups grant access?)

#### 3. User Inventory (from IMP.1)

- ISMS-IMP-A.5.15-16-18.S1 Sheet 2 (User Inventory Master List)
- Active users (who should be in review scope?)
- User managers (who should review each user's access?)

#### 4. Review Execution Data

- Review tool exports (Sailpoint, Saviynt review results)
- OR spreadsheet-based review results (if manual process)
- Reviewer sign-offs (manager approvals, system owner confirmations)
- Review findings (access confirmed, access to remove, exceptions)

#### 5. Access Removal Evidence

- Access removal tickets (ServiceNow, Jira tickets for removal requests)
- Removal execution confirmation (audit logs showing access disabled)
- Removal timeliness (date removal requested vs. date executed)

### Required Tools

- **Microsoft Excel** (2016 or later) for workbook completion
- **Access review tool** (if automated: Sailpoint, Saviynt, etc.)
- **Ticketing system** (for access removal request tracking)
- **Identity system admin tools** (to verify access removal)
- **Screen capture tools** (for evidence screenshots)

### Dependencies

**CRITICAL DEPENDENCIES:**
- **ISMS-IMP-A.5.15-16-18.S2** (Access Rights Matrix) MUST be completed first
  - This assessment reviews the access documented in IMP.2
- **ISMS-IMP-A.5.15-16-18.S1** (User Inventory) provides user and manager data

**Outputs FROM this assessment feed INTO:**
- A.5.15-16-18.4 (Role & SoD Compliance) - Review findings inform role accuracy
- A.5.15-16-18.5 (IAM Governance Dashboard) - Review metrics consolidated

---

## Workflow

### High-Level Process

```
1. PREPARE
   ↓
2. DEFINE REVIEW SCOPE (which systems/users to review)
   ↓
3. ASSIGN REVIEWERS (managers, system owners)
   ↓
4. EXECUTE REVIEWS (reviewers certify access)
   ↓
5. TRACK COMPLETION (who completed, who is overdue?)
   ↓
6. COLLECT FINDINGS (access confirmed, removed, justified)
   ↓
7. EXECUTE ACCESS REMOVAL (remediate findings)
   ↓
8. VERIFY REMOVAL (confirm access actually disabled)
   ↓
9. CALCULATE COMPLETION RATE (Sheet 6)
   ↓
10. IDENTIFY GAPS (overdue reviews, unexecuted removals)
    ↓
11. REGISTER EVIDENCE (Sheet 8)
    ↓
12. REVIEW & APPROVE (Sheet 9)
```

### Detailed Workflow

#### Phase 1: Preparation (2-3 hours)

**Objective:** Plan review cycle

**Steps:**
1. Read this entire User Guide
2. Read ISMS-POL-A.5.15-16-18, Section 2.3.4 (Access Review Requirements)
3. Determine review period (Q1 2026, H1 2026, Annual 2025, etc.)
4. Identify systems in scope based on criticality:
   - Critical systems → Quarterly review required
   - High systems → Semi-annual review required
   - Standard systems → Annual review required
5. Obtain access data from IMP.2 (what access will be reviewed?)
6. Obtain user and manager data from IMP.1
7. Schedule review cycle launch date

**Deliverable:** Review cycle plan with scope, systems, timeline

**Quality Check:**
- ✓ Review frequency aligns with policy (quarterly for critical, etc.)
- ✓ All in-scope systems identified
- ✓ Access data from IMP.2 current (<30 days old)
- ✓ Manager data from IMP.1 accurate

---

#### Phase 2: Define Review Scope (2-3 hours)

**Objective:** Complete Sheet 1 - Review Scope Definition

**Steps:**

1. **Document Review Cycle Details**:
   - Review Period (Q1 2026, H1 2026, Annual 2025)
   - Review Type (Quarterly, Semi-Annual, Annual)
   - Review Start Date (when reviews launched)
   - Review Due Date (when reviews must be completed)
   - Review Coordinator (Security Team member managing cycle)

2. **List Systems in Scope**:
   - System ID, System Name (from IMP.2 Sheet 2)
   - System Criticality (Critical, High, Standard)
   - Review Frequency (Quarterly, Semi-Annual, Annual)
   - System Owner (primary reviewer for this system)
   - User Count (how many users have access to this system?)
   - Review Status (Not Started, In Progress, Completed, Overdue)

3. **List Users in Scope**:
   - User ID, Full Name (from IMP.1 Sheet 2)
   - User Type (Employee, Contractor, Service Account)
   - Manager (primary reviewer for this user)
   - System Access Count (how many systems does user access?)
   - Privileged Access Flag (if user has privileged access to ANY system)

4. **Calculate Scope Metrics**:
   - Total systems in scope
   - Total users in scope
   - Total access grants to review (users × systems)
   - Critical/High/Standard system breakdown

**Deliverable:** Complete Sheet 1 with review scope

**Quality Check:**
- ✓ All critical systems included (quarterly review)
- ✓ All active users included (from IMP.1)
- ✓ System owners and managers identified
- ✓ Scope metrics calculated correctly

---

#### Phase 3: Assign Reviewers (1-2 hours)

**Objective:** Complete Sheet 2 - Reviewer Assignments

**Steps:**

1. **Identify Reviewers**:
   - **Managers**: Review their direct reports' access
   - **System Owners**: Review access to systems they own
   - **Security Team**: Review privileged access

2. **For EACH reviewer, document**:
   - Reviewer Name, Email
   - Reviewer Type (Manager, System Owner, Security Team)
   - Review Scope (which users or systems to review?)
   - User Count (how many users to review?) OR System Count (how many systems?)
   - Review Due Date (typically review cycle due date)
   - Review Tool/Method (Sailpoint, spreadsheet, manual sign-off)

3. **Send Review Assignments**:
   - Email reviewers with:
     - What to review (users or systems)
     - How to review (tool link, spreadsheet, instructions)
     - Due date
     - Escalation contact (Security Team)

**Deliverable:** Sheet 2 with reviewer assignments

**Quality Check:**
- ✓ All users assigned to a manager reviewer
- ✓ All systems assigned to a system owner reviewer
- ✓ Reviewers notified of assignment
- ✓ Due dates set (typically 30 days from review launch)

---

#### Phase 4: Execute Reviews (Ongoing, 30 days)

**Objective:** Reviewers complete access certifications

**Steps:**

**For Managers (reviewing direct reports' access)**:
1. Review each direct report's access (systems, applications, groups)
2. For each access grant, decide:
   - **Confirm**: Access is appropriate for job function (no action)
   - **Remove**: Access is no longer needed (submit removal request)
   - **Justify**: Access appears excessive but has business reason (document exception)
3. Sign off on review (digital signature, approval in tool)

**For System Owners (reviewing access to their systems)**:
1. Review all users with access to their system
2. Verify business need for each user
3. Identify inappropriate access (users who shouldn't have access)
4. Submit removal requests or confirm access is appropriate
5. Sign off on review

**For Security Team (reviewing privileged access)**:
1. Review all users with privileged/admin access
2. Verify technical necessity (does user need admin rights?)
3. Verify CISO approval documented (per policy)
4. Identify excessive privileged access
5. Escalate to CISO for exceptions or removals

**This Phase is Iterative:**
- Reviews happen over 30-day period
- Security Team tracks completion (Phase 5)
- Reminders sent to reviewers at 15 days, 7 days, 1 day before due date
- Escalations for overdue reviews (Phase 10)

**Deliverable:** Reviewer sign-offs, access removal requests

**Quality Check:**
- ✓ Reviewers understand what to review
- ✓ Reviewers know how to submit findings (confirm, remove, justify)
- ✓ Removal requests captured (ticketing system or spreadsheet)
- ✓ Sign-offs documented (approval timestamp, digital signature)

---

#### Phase 5: Track Review Completion (Ongoing, updated daily/weekly)

**Objective:** Complete Sheet 3 - Review Completion Tracking

**Steps:**

1. **Update Review Status Daily**:
   - Which reviewers have completed?
   - Which reviewers are in progress?
   - Which reviewers have not started?
   - Which reviewers are overdue (past due date)?

2. **For EACH reviewer, track**:
   - Review Assigned Date
   - Review Started Date (when reviewer first accessed review data)
   - Review Completed Date (when reviewer signed off)
   - Review Status (Not Started, In Progress, Completed, Overdue)
   - Days to Complete (Completed Date - Assigned Date)
   - Users Reviewed (count)
   - Findings Submitted (access confirmed, removed, justified counts)

3. **Calculate Completion Metrics**:
   - Total reviewers assigned
   - Reviewers completed (count, percentage)
   - Reviewers in progress (count, percentage)
   - Reviewers overdue (count, percentage)
   - Average days to complete
   - Completion rate trend (if historical data available)

4. **Send Reminders**:
   - 15 days before due date: First reminder
   - 7 days before due date: Second reminder
   - 1 day before due date: Final reminder
   - After due date: Escalation to manager's manager or CISO

**Deliverable:** Sheet 3 with daily/weekly completion tracking

**Quality Check:**
- ✓ Status updated regularly (at least weekly)
- ✓ Completion dates accurate
- ✓ Overdue reviewers flagged
- ✓ Reminders sent per schedule

---

#### Phase 6: Collect Review Findings (After review cycle ends)

**Objective:** Complete Sheet 4 - Review Findings Summary

**Steps:**

1. **Consolidate All Review Findings**:
   - Extract findings from review tool (Sailpoint, Saviynt)
   - OR collect findings from spreadsheet reviews
   - OR gather manager sign-off forms

2. **Categorize Findings**:
   - **Access Confirmed**: Reviewer certified access is appropriate (no action)
   - **Access to Remove**: Reviewer identified inappropriate access (removal request)
   - **Access Justified**: Reviewer documented exception (access appears excessive but has business reason)
   - **No Response**: Reviewer did not complete review (escalation needed)

3. **For EACH finding, document**:
   - Review Period
   - User ID, System ID
   - Access Level (what access was reviewed?)
   - Reviewer Name (who reviewed this access?)
   - Review Date (when was review completed?)
   - Finding (Confirmed, Remove, Justified, No Response)
   - Finding Notes (reviewer comments, justification text)
   - Removal Request ID (if finding = Remove, ticket ID)

4. **Calculate Finding Metrics**:
   - Total access grants reviewed
   - Access confirmed (count, percentage)
   - Access removal requests (count, percentage)
   - Access justified with exceptions (count, percentage)
   - No response (count, percentage)
   - **Access Removal Rate** = (Access Removal Requests / Total Reviewed) × 100%

**Deliverable:** Sheet 4 with complete review findings

**Quality Check:**
- ✓ All completed reviews have findings documented
- ✓ Removal requests captured with ticket IDs
- ✓ Justifications documented for exceptions
- ✓ Finding metrics calculated correctly

---

#### Phase 7: Execute Access Removal (Immediately after findings, within 5 business days)

**Objective:** Remediate access removal findings

**Steps:**

1. **Create Removal Requests** (if not already done):
   - For each "Access to Remove" finding, create ticket
   - Ticket includes: User ID, System ID, Access to Remove, Business Justification (why removing), Requestor (reviewer name)
   - Assign to IT Operations or IAM Team

2. **Execute Removals**:
   - IT Operations removes access per ticket
   - Document removal execution date
   - Capture evidence (audit log showing access disabled, screenshot)

3. **Verify Removals**:
   - Security Team spot-checks sample of removals
   - Verify access actually disabled (not just ticket closed)
   - Identify removals not executed (findings ignored)

4. **Track Removal Timeliness**:
   - Days from finding to removal = Removal Executed Date - Review Date
   - Policy requirement: ≤5 business days
   - Categorize: On-time (≤5 days), Late (6-10 days), Very Late (>10 days)

**Deliverable:** Access removal execution and verification

**Quality Check:**
- ✓ All removal findings have tickets created
- ✓ Removals executed within 5 business days (policy SLA)
- ✓ Removal evidence captured (audit logs)
- ✓ Verification completed for sample (spot-check 10%)

---

#### Phase 8: Verify Access Removal (1-2 hours)

**Objective:** Complete Sheet 5 - Access Removal Verification

**Steps:**

1. **For EACH access removal request, document**:
   - Removal Request ID (ticket ID)
   - User ID, System ID
   - Access Removed (what was removed?)
   - Review Date (when finding submitted)
   - Removal Requested Date (when ticket created)
   - Removal Executed Date (when access actually disabled)
   - Removal Delay (Days) = Executed Date - Review Date
   - Removal SLA Met? (≤5 business days = Yes, >5 days = No)
   - Removal Verified? (spot-check confirmed access disabled)
   - Evidence Location (audit log path, screenshot filename)

2. **Calculate Removal Metrics**:
   - Total removal requests
   - Removals executed (count, percentage)
   - Removals on-time (≤5 days) (count, percentage)
   - Removals late (6-10 days) (count, percentage)
   - Removals very late (>10 days) (count, percentage)
   - Removals not executed (count, percentage)
   - **Removal Compliance Rate** = (On-Time Removals / Total Requests) × 100%

3. **Identify Removal Gaps**:
   - Removals not executed (findings ignored)
   - Removals executed late (>5 days)
   - Removals not verified (no evidence)

**Deliverable:** Sheet 5 with removal verification

**Quality Check:**
- ✓ All removal requests tracked
- ✓ Execution dates documented
- ✓ Removal timeliness calculated correctly
- ✓ Evidence collected for sample

---

#### Phase 9: Calculate Access Review Compliance Rate (1-2 hours)

**Objective:** Complete Sheet 6 - Access Review Compliance Dashboard

**Steps:**

1. **Consolidate Metrics** from Sheets 1-5:
   - Review completion rate (from Sheet 3)
   - Access removal rate (from Sheet 4)
   - Removal compliance rate (from Sheet 5)
   - Reviewer accountability (from Sheet 3)

2. **Calculate Overall Access Review Compliance Score**:
   ```
   Review Compliance Score = 
     (Review Completion Rate × 50%) + 
     (Removal Execution Rate × 30%) + 
     (Removal Timeliness × 20%)
   ```

3. **Benchmark Against Industry Standards**:
   - **Excellent (90-100%)**: Best-in-class review execution
   - **Good (75-89%)**: Strong review compliance, minor gaps
   - **Fair (60-74%)**: Acceptable but significant gaps
   - **Poor (<60%)**: Major review deficiencies, audit risk

4. **Document Findings**:
   - Strengths (areas of compliance)
   - Weaknesses (areas of non-compliance)
   - Root causes (why are reviews incomplete or late?)
   - Recommendations (how to improve)

**Deliverable:** Sheet 6 with access review compliance dashboard

**Quality Check:**
- ✓ All metrics pulled from correct sheets
- ✓ Overall compliance score calculated correctly
- ✓ Benchmark category accurate
- ✓ Findings documented clearly

---

#### Phase 10: Identify Gaps and Remediation Plan (2-3 hours)

**Objective:** Complete Sheet 7 - Gap Analysis & Remediation

**Steps:**

1. **Identify All Gaps**:
   - **Reviews not completed** (overdue by >30 days)
   - **Access removal not executed** (findings ignored)
   - **Reviewers consistently late** (accountability issue)
   - **Removal timeliness missed** (executed >5 days)

2. **Prioritize Gaps by Risk**:
   - **Critical** (P1):
     - Privileged access reviews not completed (security risk)
     - Access removal findings not executed (inappropriate access still active)
   - **High** (P2):
     - Critical system reviews not completed (quarterly requirement missed)
     - Removal executed very late (>10 days)
   - **Medium** (P3):
     - Standard system reviews not completed (annual requirement missed)
     - Removal executed late (6-10 days)
   - **Low** (P4):
     - Low-priority system reviews delayed
     - Reviewer late but completed within grace period

3. **Create Remediation Actions**:

| Gap ID | Gap Description | Priority | Action | Owner | Target Date | Status |
|--------|----------------|----------|--------|-------|-------------|--------|
| GAP-001 | 5 managers did not complete Q1 2026 review (overdue >30 days) | High | Escalate to CISO, mandate completion | Security Team | 14 days | Open |
| GAP-002 | 15 access removal findings not executed | Critical | IT Operations must execute immediately | IT Ops Manager | 7 days | Open |
| GAP-003 | 20% of removals executed late (>5 days) | Medium | Improve IT Ops process, assign dedicated resource | IAM Team | 30 days | Open |

4. **Track Remediation Progress**:
   - Action completion status
   - Percent complete
   - Notes on progress or blockers

**Deliverable:** Sheet 7 with gap analysis and remediation plan

**Quality Check:**
- ✓ All gaps identified
- ✓ Prioritization reflects actual risk
- ✓ Remediation actions specific and actionable
- ✓ Owners assigned
- ✓ Target dates realistic

---

#### Phase 11: Register Evidence (1 hour)

**Objective:** Complete Sheet 8 - Evidence Register

**Steps:**

1. **List All Evidence Collected**:
   - Review scope documentation
   - Reviewer assignments and notifications
   - Review completion sign-offs (approvals, timestamps)
   - Review findings reports (from review tool or spreadsheets)
   - Access removal tickets
   - Removal execution evidence (audit logs, screenshots)
   - Escalation emails (for overdue reviews)

2. **For EACH piece of evidence, document**:
   - Evidence ID, Type, Description
   - Related Sheet/Row
   - Location/Path
   - Date Collected, Collected By
   - Verification Status

3. **Organize Evidence**

4. **Verify Evidence Quality**:
   - All evidence recent and relevant
   - Evidence accessible for audit
   - Evidence clearly labeled

**Deliverable:** Sheet 8 with complete evidence register

**Quality Check:**
- ✓ All evidence collected and documented
- ✓ Evidence organized logically
- ✓ Evidence IDs cross-referenced
- ✓ All evidence verified

---

#### Phase 12: Review & Approval (2-3 hours)

**Objective:** Three-level approval (Sheet 9 - Approval & Sign-Off)

**Steps:**

**Step 1: Self-Review** (Assessment Completer - Security Team)
- Verify all sheets complete
- Check metrics calculated correctly
- Validate completion rates accurate
- Ensure evidence collected

**Step 2: IAM Team Lead Review**
- Review access removal execution (was it done correctly?)
- Verify removal timeliness calculations
- Check overdue review escalations
- Approve or request changes

**Step 3: CISO Review**
- Review overall compliance rate (acceptable?)
- Assess critical gaps (incomplete privileged access reviews = unacceptable)
- Verify remediation plans adequate
- Final approval

**Deliverable:** Approved assessment ready for IAM Governance Dashboard

**Quality Check:**
- ✓ All three approval levels completed
- ✓ All review comments addressed
- ✓ Critical gaps have immediate remediation
- ✓ Evidence audit-ready

---

## Evidence Collection

### What Evidence to Collect

**For Sheet 1 (Review Scope):**
- Review cycle announcement (email launching reviews)
- System criticality documentation
- Policy requirements (quarterly for critical, etc.)

**For Sheet 2 (Reviewer Assignments):**
- Reviewer notification emails
- Review tool assignment screenshots
- Manager list from HR

**For Sheet 3 (Review Completion Tracking):**
- Review tool completion reports
- Reviewer sign-off forms (if manual)
- Reminder emails sent
- Escalation emails for overdue reviews

**For Sheet 4 (Review Findings):**
- Review tool findings export
- Manager approval forms
- Access removal request tickets
- Exception justification documentation

**For Sheet 5 (Access Removal Verification):**
- Access removal tickets (ServiceNow, Jira)
- Audit logs (AD account disabled, Azure AD access removed)
- Screenshots of removal execution
- Spot-check verification results

**For Sheet 6 (Compliance Dashboard):**
- Trend charts (if historical data)
- Benchmark references

**For Sheet 7 (Gap Analysis):**
- Gap remediation plans
- Escalation records

**For Sheet 8 (Evidence Register):**
- All evidence listed above

**For Sheet 9 (Approval):**
- Approval sign-offs

### Evidence Retention

- **Minimum retention:** 3 years (ISO 27001 certification cycle)
- **Recommended retention:** 5 years (trend analysis)
- **Storage location:** Secure document management system

---

## Common Pitfalls

### Pitfall 1: Review Scope Incomplete

❌ **Mistake:** Only reviewing critical systems, missing standard systems due for annual review

✅ **Fix:** Check policy requirements, include ALL systems based on review frequency (quarterly, semi-annual, annual)

---

### Pitfall 2: Reviewers Not Prepared

❌ **Mistake:** Launching reviews without training reviewers on what/how to review

✅ **Fix:** Provide clear instructions, examples, and review tool training before launch

---

### Pitfall 3: No Tracking of Review Progress

❌ **Mistake:** Waiting until due date to check completion, discovering 50% incomplete

✅ **Fix:** Track completion daily/weekly, send reminders at 15/7/1 days before due date

---

### Pitfall 4: Access Removal Findings Not Executed

❌ **Mistake:** Reviewers submit removal requests, but IT Operations doesn't execute

✅ **Fix:** Assign clear ownership (IT Ops), track removal execution, escalate if not done within 5 days

---

### Pitfall 5: No Removal Verification

❌ **Mistake:** Assuming access removed because ticket closed, not actually verifying

✅ **Fix:** Spot-check sample of removals (10%), verify access actually disabled in audit logs

---

### Pitfall 6: Overdue Reviews Not Escalated

❌ **Mistake:** Reviewers miss deadline, no consequence, reviews never completed

✅ **Fix:** Escalate overdue reviews to reviewer's manager, CISO if necessary

---

### Pitfall 7: Review Findings Not Categorized

❌ **Mistake:** Reviewers just say "reviewed" without documenting confirmed/remove/justify

✅ **Fix:** Require structured findings (Confirm, Remove, Justify with documentation)

---

### Pitfall 8: Stale Review Data

❌ **Mistake:** Reviewing access from 6 months ago (users have since left, access changed)

✅ **Fix:** Use current access data from IMP.2 (<30 days old)

---

### Pitfall 9: No Reviewer Accountability

❌ **Mistake:** Reviews optional, no consequence for non-completion

✅ **Fix:** Manager performance reviews tied to access review completion, CISO escalation

---

### Pitfall 10: Review Cycle Too Short

❌ **Mistake:** Giving reviewers 5 days to review 100 users

✅ **Fix:** Realistic timelines (30 days minimum for comprehensive review)

---

## Quality Checklist

Before submitting for approval, verify:

### Review Scope (Sheet 1)
- [ ] All systems included based on criticality and review frequency
- [ ] All active users included from IMP.1
- [ ] System owners and managers identified
- [ ] Scope metrics calculated correctly

### Reviewer Assignments (Sheet 2)
- [ ] All users assigned to manager reviewer
- [ ] All systems assigned to system owner reviewer
- [ ] Reviewers notified
- [ ] Due dates set

### Review Completion Tracking (Sheet 3)
- [ ] Status updated regularly (at least weekly)
- [ ] Completion dates accurate
- [ ] Overdue reviewers flagged
- [ ] Reminders sent per schedule

### Review Findings (Sheet 4)
- [ ] All completed reviews have findings
- [ ] Removal requests captured with ticket IDs
- [ ] Justifications documented
- [ ] Finding metrics calculated correctly

### Access Removal Verification (Sheet 5)
- [ ] All removal requests tracked
- [ ] Execution dates documented
- [ ] Removal timeliness calculated correctly
- [ ] Evidence collected for sample

### Compliance Dashboard (Sheet 6)
- [ ] All metrics pulled from correct sheets
- [ ] Overall compliance score calculated correctly
- [ ] Benchmark category accurate
- [ ] Findings documented clearly

### Gap Analysis (Sheet 7)
- [ ] All gaps identified
- [ ] Prioritization reflects risk
- [ ] Remediation actions actionable
- [ ] Owners assigned
- [ ] Target dates realistic

### Evidence Register (Sheet 8)
- [ ] All evidence collected and listed
- [ ] Evidence organized
- [ ] Evidence IDs cross-referenced
- [ ] All evidence verified

### Approval (Sheet 9)
- [ ] Self-review completed
- [ ] IAM Team Lead review completed
- [ ] CISO review completed
- [ ] All comments addressed

---

## Review & Approval

### Review Process

**Step 1: Self-Review** (Security Team - Review Coordinator)
- **Focus:** Completeness, accuracy, metrics
- **Time:** 2-3 hours
- **Turnaround:** Same day

**Step 2: IAM Team Lead Review**
- **Focus:** Access removal execution, timeliness compliance
- **Review Criteria:**
  - Were removal findings executed?
  - Was removal timeliness met (≤5 days)?
  - Are overdue reviews properly escalated?
- **Decision:** Approve / Request Changes
- **Time:** 2-3 hours
- **Turnaround:** 2-3 business days

**Step 3: CISO Review**
- **Focus:** Overall review compliance, critical gaps
- **Review Criteria:**
  - Review completion rate acceptable? (target >90%)
  - Critical gaps addressed? (privileged access reviews complete?)
  - Remediation plans adequate?
- **Decision:** Final Approval / Approve with Conditions / Reject
- **Time:** 2-3 hours
- **Turnaround:** 3-5 business days

### Approval Timeline

```
Day 1:       Assessment completed, self-review, submitted to IAM Team Lead
Day 2-4:     IAM Team Lead review
Day 5:       IAM Team Lead approves
Day 6-10:    CISO review
Day 11:      CISO final approval
Day 12:      Assessment marked "Final"
```

**Total timeline:** ~2 weeks

---

## Integration with Other Assessments

This assessment (A.5.15-16-18.3) feeds into:

### A.5.15-16-18.2 - Access Rights Matrix Assessment
- **Uses:** Access matrix (Sheet 3) as review scope

### A.5.15-16-18.4 - Role Definition & SoD Compliance Assessment
- **Uses:** Review findings inform role accuracy

### A.5.15-16-18.5 - IAM Governance Compliance Dashboard
- **Uses:** Review metrics from Sheet 6

---

## Continuous Improvement

### Quarterly Review Cycle

Each quarter:
1. **Plan Review Cycle** (define scope, assign reviewers)
2. **Execute Reviews** (30-day window)
3. **Track Completion** (daily/weekly monitoring)
4. **Collect Findings** (after cycle ends)
5. **Execute Removals** (within 5 business days)
6. **Analyze Results** (compliance dashboard)
7. **Identify Improvements** (what can be better next quarter?)

**Time Commitment:** 10-15 hours per quarter

### Annual Strategic Review

1. **Year-over-year comparison** (is review compliance improving?)
2. **Technology assessment** (should we implement automated review tool?)
3. **Process improvement** (reduce reviewer burden, increase compliance)

**Time Commitment:** 1-2 days annually

---

# PART II: TECHNICAL SPECIFICATION

## Workbook Structure

### Sheet 1: Instructions_and_Legend

#### Header Section
- **Title:** "ISMS-IMP-A.5.15-16-18.S3 – Access Review Results Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Controls A.5.15 & A.5.18: Access Control & Access Rights"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block (Rows 3-12)
```
Document ID:           ISMS-IMP-A.5.15-16-18.S3
Assessment Area:       Access Review Results & Recertification Compliance
Related Policy:        ISMS-POL-A.5.15-16-18, Section 2.3.4 (Access Review Requirements)
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Period:         [USER INPUT - e.g., "Q1 2026", "H1 2026", "Annual 2025"]
Review Cycle:          Quarterly (critical systems), Semi-Annual (high), Annual (standard)
```

#### How to Use This Workbook (Rows 14-24)
1. **Sheet 1 - Review Scope Definition:** Define which systems/users to review in this cycle
2. **Sheet 2 - Reviewer Assignments:** Assign reviewers (managers, system owners)
3. **Sheet 3 - Review Completion Tracking:** Track who completed, who is overdue (daily/weekly updates)
4. **Sheet 4 - Review Findings Summary:** Document review results (confirmed, remove, justify)
5. **Sheet 5 - Access Removal Verification:** Track removal execution and timeliness
6. **Sheet 6 - Access Review Compliance Dashboard:** Overall metrics and compliance scoring
7. **Sheet 7 - Gap Analysis & Remediation:** Identify gaps (overdue reviews, unexecuted removals)
8. **Sheet 8 - Evidence Register:** Document all supporting evidence
9. **Sheet 9 - Approval & Sign-Off:** Three-level approval workflow

#### Status Legend (Rows 26-34)
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Completed / On-Time | Review completed on time, removal executed ≤5 days | Green (C6EFCE) |
| ⚠️ | In Progress / Late | Review in progress or removal executed 6-10 days | Yellow (FFEB9C) |
| ❌ | Overdue / Very Late | Review not completed or removal executed >10 days | Red (FFC7CE) |
| 🚨 | CRITICAL | Privileged access review not completed or removal not executed | Dark Red (FF0000) |
| ℹ️ | Not Started | Review not yet started | Blue (B4C7E7) |
| N/A | Not Applicable | Not in scope for this review cycle | Gray (D3D3D3) |

---

## Sheet 2: Review_Scope_Definition

### Purpose
Define which systems and users are in scope for this review cycle.

### Header Section (Rows 1-3)
**Row 1:** "ACCESS REVIEW SCOPE DEFINITION"  
**Row 2:** "Systems and users in scope for this review cycle"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | Review Period | Static | Review cycle identifier | **USER INPUT** (e.g., "Q1 2026") | None |
| B | Review Type | Dropdown | Cycle type | Dropdown: Quarterly, Semi-Annual, Annual, Ad-hoc | None |
| C | Review Start Date | Date | When reviews launched | **USER INPUT** | None |
| D | Review Due Date | Date | When reviews must be completed | **USER INPUT** | None |
| E | Review Coordinator | Text | Who is managing this cycle? | **USER INPUT** (Security Team member) | None |
| F | System ID | Text | From IMP.2 Sheet 2 | **LOOKUP** from IMP.2 | None |
| G | System Name | Text | System being reviewed | **LOOKUP** from IMP.2 | None |
| H | System Criticality | Text | Critical, High, Standard | **LOOKUP** from IMP.2 | **CF:** Red if Critical |
| I | Required Review Frequency | Dropdown | Per policy | Dropdown: Quarterly, Semi-Annual, Annual | None |
| J | In Scope This Cycle? | Dropdown | Include in this review? | Dropdown: Yes, No, Deferred | **CF:** Green if Yes |
| K | System Owner | Text | Primary reviewer | **LOOKUP** from IMP.2 | None |
| L | User Count | Number | Users with access | **LOOKUP** from IMP.2 or calculated from access matrix | None |
| M | Last Review Date | Date | When was last review? | **USER INPUT** or from previous cycle | **CF:** Red if >365 days and Required Frequency = Annual |
| N | Notes | Text | Why in/out of scope | **USER INPUT** | None |

### Summary Metrics (Top of Sheet, Rows 1-2, Columns P-U)

| Metric | Formula | Cell |
|--------|---------|------|
| Systems in Scope | `=COUNTIF(J:J,"Yes")` | P1 |
| Critical Systems | `=COUNTIFS(J:J,"Yes",H:H,"Critical")` | Q1 |
| High Systems | `=COUNTIFS(J:J,"Yes",H:H,"High")` | R1 |
| Standard Systems | `=COUNTIFS(J:J,"Yes",H:H,"Standard")` | S1 |
| Total Users to Review | `=SUMIF(J:J,"Yes",L:L)` | T1 |
| Systems Overdue Review | `=COUNTIFS(M:M,"<"&TODAY()-365,I:I,"Annual")` | U1 |

### Data Validation (Dropdowns)

**Review Type (Column B):**
- List: Quarterly, Semi-Annual, Annual, Ad-hoc

**Required Review Frequency (Column I):**
- List: Quarterly, Semi-Annual, Annual

**In Scope This Cycle (Column J):**
- List: Yes, No, Deferred

### Conditional Formatting Rules

**System Criticality (Column H):**
- Rule 1: If "Critical" → Fill: FFC7CE (red)

**In Scope This Cycle (Column J):**
- Rule 1: If "Yes" → Fill: C6EFCE (green)

**Last Review Date (Column M):**
- Rule 1: If < (TODAY()-365) AND Required Frequency = "Annual" → Fill: FFC7CE (red)
- Rule 2: If < (TODAY()-180) AND Required Frequency = "Semi-Annual" → Fill: FFC7CE (red)
- Rule 3: If < (TODAY()-90) AND Required Frequency = "Quarterly" → Fill: FFC7CE (red)

---

## Sheet 3: Reviewer_Assignments

### Purpose
Assign reviewers and track notification.

### Header Section (Rows 1-3)
**Row 1:** "REVIEWER ASSIGNMENTS"  
**Row 2:** "Manager and system owner assignments for access review"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | Reviewer Name | Text | Who is reviewing? | **USER INPUT** (manager or system owner name) | None |
| B | Reviewer Email | Text | Contact | **USER INPUT** | None |
| C | Reviewer Type | Dropdown | Category | Dropdown: Manager (Direct Reports), System Owner, Security Team (Privileged Access), Other | None |
| D | Review Scope | Text | What to review? | **USER INPUT** (e.g., "Direct reports in Finance", "ERP System access") | None |
| E | User Count | Number | How many users to review? | **USER INPUT** or calculated | None |
| F | System Count | Number | How many systems to review? | **USER INPUT** or calculated | None |
| G | Review Assigned Date | Date | When notified? | **USER INPUT** (review launch date) | None |
| H | Review Due Date | Date | When due? | **USER INPUT** (typically +30 days from assigned) | None |
| I | Review Tool/Method | Dropdown | How to review? | Dropdown: Sailpoint, Saviynt, Spreadsheet, Manual Sign-Off, Other | None |
| J | Assignment Notification Sent? | Dropdown | Reviewer notified? | Dropdown: Yes, No, Pending | **CF:** Yellow if No or Pending |
| K | Notification Date | Date | When notified? | **USER INPUT** | None |
| L | Notes | Text | Special instructions | **USER INPUT** | None |

### Summary Metrics (Top of Sheet, Rows 1-2, Columns N-Q)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Reviewers | `=COUNTA(A:A)-1` | N1 |
| Managers | `=COUNTIF(C:C,"Manager*")` | O1 |
| System Owners | `=COUNTIF(C:C,"System Owner")` | P1 |
| Notifications Sent | `=COUNTIF(J:J,"Yes")` | Q1 |

### Data Validation (Dropdowns)

**Reviewer Type (Column C):**
- List: Manager (Direct Reports), System Owner, Security Team (Privileged Access), Other

**Review Tool/Method (Column I):**
- List: Sailpoint, Saviynt, Spreadsheet, Manual Sign-Off, Other

**Assignment Notification Sent (Column J):**
- List: Yes, No, Pending

### Conditional Formatting Rules

**Assignment Notification Sent (Column J):**
- Rule 1: If "No" OR "Pending" → Fill: FFEB9C (yellow)

---

## Sheet 4: Review_Completion_Tracking

### Purpose
Track who completed reviews, who is in progress, who is overdue.

### Header Section (Rows 1-3)
**Row 1:** "REVIEW COMPLETION TRACKING"  
**Row 2:** "Daily/weekly updates on review progress"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | Reviewer Name | Text | From Sheet 3 | **LOOKUP** from Sheet 3 | None |
| B | Reviewer Type | Text | Manager, System Owner, etc. | **LOOKUP** from Sheet 3 | None |
| C | Review Scope | Text | What reviewing? | **LOOKUP** from Sheet 3 | None |
| D | Review Assigned Date | Date | From Sheet 3 | **LOOKUP** from Sheet 3 | None |
| E | Review Due Date | Date | From Sheet 3 | **LOOKUP** from Sheet 3 | None |
| F | Review Started Date | Date | When first accessed review data? | **USER INPUT** | None |
| G | Review Completed Date | Date | When signed off? | **USER INPUT** | None |
| H | Review Status | Calculated | Current status | **FORMULA:** See below | **CF:** Green/Yellow/Red/Dark Red |
| I | Days to Complete | Calculated | Time taken | **FORMULA:** `=IF(G<>"",G-D,"")` | None |
| J | Days Since Assigned | Calculated | How long pending? | **FORMULA:** `=IF(G="",TODAY()-D,G-D)` | **CF:** Red if >30 |
| K | Users Reviewed | Number | Count | **USER INPUT** from findings | None |
| L | Findings Submitted? | Dropdown | Findings received? | Dropdown: Yes, No, Partial | **CF:** Green if Yes, Red if No |
| M | Reminder 1 Sent | Date | 15 days before due | **USER INPUT** | None |
| N | Reminder 2 Sent | Date | 7 days before due | **USER INPUT** | None |
| O | Reminder 3 Sent | Date | 1 day before due | **USER INPUT** | None |
| P | Escalation Date | Date | If overdue, when escalated? | **USER INPUT** | **CF:** Yellow if Status = Overdue and this blank |
| Q | Escalated To | Text | Who escalated to? | **USER INPUT** (reviewer's manager, CISO) | None |
| R | Notes | Text | Additional context | **USER INPUT** | None |

### Review Status Formula (Column H)
```excel
=IF(G<>"","✅ Completed",
  IF(F<>"","⚠️ In Progress",
    IF(TODAY()>E,"❌ Overdue",
      "ℹ️ Not Started")))
```

**Logic:**
- Completed Date exists → Completed
- Started but not completed → In Progress
- Past due date and not completed → Overdue
- Not started → Not Started

### Summary Metrics (Top of Sheet, Rows 1-2, Columns T-Z)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Reviewers | `=COUNTA(A:A)-1` | T1 |
| Completed | `=COUNTIF(H:H,"✅ Completed")` | U1 |
| In Progress | `=COUNTIF(H:H,"⚠️ In Progress")` | V1 |
| Not Started | `=COUNTIF(H:H,"ℹ️ Not Started")` | W1 |
| Overdue | `=COUNTIF(H:H,"❌ Overdue")` | X1 |
| Completion Rate | `=U1/T1` (format as %) | Y1 |
| Average Days to Complete | `=AVERAGE(I:I)` | Z1 |

### Data Validation (Dropdowns)

**Findings Submitted (Column L):**
- List: Yes, No, Partial

### Conditional Formatting Rules

**Review Status (Column H):**
- Rule 1: If "✅ Completed" → Fill: C6EFCE (green)
- Rule 2: If "⚠️ In Progress" → Fill: FFEB9C (yellow)
- Rule 3: If "❌ Overdue" → Fill: FFC7CE (red)
- Rule 4: If "ℹ️ Not Started" → Fill: B4C7E7 (blue)

**Days Since Assigned (Column J):**
- Rule 1: If >30 AND Review Status ≠ "Completed" → Fill: FFC7CE (red)

**Findings Submitted (Column L):**
- Rule 1: If "Yes" → Fill: C6EFCE (green)
- Rule 2: If "No" AND Review Status = "Completed" → Fill: FFC7CE (red) - inconsistent

**Escalation Date (Column P):**
- Rule 1: If BLANK AND Review Status = "❌ Overdue" → Fill: FFEB9C (yellow)

---

## Sheet 5: Review_Findings_Summary

### Purpose
Document access review findings (confirmed, remove, justify).

### Header Section (Rows 1-3)
**Row 1:** "REVIEW FINDINGS SUMMARY"  
**Row 2:** "Consolidated review results from all reviewers"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | Review Period | Text | From Sheet 2 | **LOOKUP** from Sheet 2 | None |
| B | User ID | Text | From IMP.2 access matrix | **USER INPUT** from review results | None |
| C | Full Name | Text | User's name | **LOOKUP** from IMP.1 | None |
| D | System ID | Text | System accessed | **USER INPUT** from review results | None |
| E | System Name | Text | System name | **LOOKUP** from IMP.2 | None |
| F | Access Level | Text | What access reviewed? | **USER INPUT** (Read, Write, Admin, Privileged) | **CF:** Dark Red if Privileged |
| G | Reviewer Name | Text | Who reviewed? | **USER INPUT** | None |
| H | Reviewer Type | Text | Manager or System Owner | **LOOKUP** from Sheet 3 | None |
| I | Review Date | Date | When reviewed? | **USER INPUT** | None |
| J | Finding | Dropdown | Review decision | Dropdown: Access Confirmed, Access to Remove, Access Justified (Exception), No Response | **CF:** Green if Confirmed, Red if Remove |
| K | Finding Notes | Text | Reviewer comments | **USER INPUT** | **CF:** Yellow if Finding = Justified and this blank |
| L | Removal Request ID | Text | If remove, ticket ID | **USER INPUT** (ticket system ID) | **CF:** Yellow if Finding = Remove and this blank |
| M | Exception Justification | Text | If justified, why? | **USER INPUT** | **CF:** Yellow if Finding = Justified and this blank |
| N | Exception Approver | Text | Who approved exception? | **USER INPUT** (manager, system owner, CISO) | None |
| O | Notes | Text | Additional context | **USER INPUT** | None |

### Summary Metrics (Top of Sheet, Rows 1-2, Columns Q-W)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Access Grants Reviewed | `=COUNTA(A:A)-1` | Q1 |
| Access Confirmed | `=COUNTIF(J:J,"Access Confirmed")` | R1 |
| Access to Remove | `=COUNTIF(J:J,"Access to Remove")` | S1 |
| Access Justified | `=COUNTIF(J:J,"Access Justified*")` | T1 |
| No Response | `=COUNTIF(J:J,"No Response")` | U1 |
| Confirmation Rate | `=R1/Q1` (format as %) | V1 |
| Removal Rate | `=S1/Q1` (format as %) | W1 |

### Data Validation (Dropdowns)

**Finding (Column J):**
- List: Access Confirmed, Access to Remove, Access Justified (Exception), No Response

### Conditional Formatting Rules

**Access Level (Column F):**
- Rule 1: If "Privileged" → Fill: FF0000 (dark red)

**Finding (Column J):**
- Rule 1: If "Access Confirmed" → Fill: C6EFCE (green)
- Rule 2: If "Access to Remove" → Fill: FFC7CE (red)
- Rule 3: If "Access Justified*" → Fill: FFEB9C (yellow)
- Rule 4: If "No Response" → Fill: D3D3D3 (gray)

**Finding Notes (Column K):**
- Rule 1: If BLANK AND Finding = "Access Justified*" → Fill: FFEB9C (yellow)

**Removal Request ID (Column L):**
- Rule 1: If BLANK AND Finding = "Access to Remove" → Fill: FFEB9C (yellow)

**Exception Justification (Column M):**
- Rule 1: If BLANK AND Finding = "Access Justified*" → Fill: FFEB9C (yellow)

---

## Sheet 6: Access_Removal_Verification

### Purpose
Track access removal execution and timeliness.

### Header Section (Rows 1-3)
**Row 1:** "ACCESS REMOVAL VERIFICATION"  
**Row 2:** "Track removal execution and timeliness for review findings"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | Removal Request ID | Text | From Sheet 5 | **LOOKUP** from Sheet 5 where Finding = "Access to Remove" | None |
| B | User ID | Text | User whose access removing | **LOOKUP** from Sheet 5 | None |
| C | Full Name | Text | User's name | **LOOKUP** from IMP.1 | None |
| D | System ID | Text | System | **LOOKUP** from Sheet 5 | None |
| E | System Name | Text | System name | **LOOKUP** from IMP.2 | None |
| F | Access to Remove | Text | What access? | **LOOKUP** from Sheet 5 (Access Level) | None |
| G | Review Date | Date | When finding submitted? | **LOOKUP** from Sheet 5, Column I | None |
| H | Removal Requested Date | Date | When ticket created? | **USER INPUT** | None |
| I | Removal Executed Date | Date | When access disabled? | **USER INPUT** from audit log or ticket close date | None |
| J | Removal Delay (Days) | Calculated | Days from review to removal | **FORMULA:** `=IF(I<>"",I-G,"")` | **CF:** Green if ≤5, Yellow if 6-10, Red if >10 |
| K | Target SLA (Days) | Static | Policy requirement | **VALUE:** 5 (business days) | None |
| L | SLA Met? | Calculated | Within 5 days? | **FORMULA:** `=IF(J<="","",IF(J<=K,"✅ Yes","❌ No"))` | **CF:** Green if Yes, Red if No |
| M | Removal Status | Dropdown | Current state | Dropdown: Executed, In Progress, Not Started, Blocked | **CF:** Green if Executed, Red if Not Started/Blocked |
| N | Removal Verified? | Dropdown | Spot-check confirmation | Dropdown: Yes - Verified, No - Not Verified, Pending | **CF:** Green if Verified |
| O | Evidence Location | Text | Audit log path, screenshot filename | **USER INPUT** | **CF:** Yellow if BLANK and Verified = Yes |
| P | Executed By | Text | Who removed access? | **USER INPUT** (IT Operations, IAM Team) | None |
| Q | Notes | Text | Issues, blockers | **USER INPUT** | None |

### Removal Delay Formula (Column J)
```excel
=IF(I<>"", I-G, "")
```

### SLA Met Formula (Column L)
```excel
=IF(J="", "",
  IF(J<=K, "✅ Yes", "❌ No"))
```

### Summary Metrics (Top of Sheet, Rows 1-2, Columns S-Y)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Removal Requests | `=COUNTA(A:A)-1` | S1 |
| Removals Executed | `=COUNTIF(M:M,"Executed")` | T1 |
| Removals On-Time (≤5 days) | `=COUNTIF(L:L,"✅ Yes")` | U1 |
| Removals Late (6-10 days) | `=COUNTIFS(J:J,">5",J:J,"<=10")` | V1 |
| Removals Very Late (>10 days) | `=COUNTIF(J:J,">10")` | W1 |
| Removals Not Executed | `=COUNTIFS(M:M,"<>Executed",M:M,"<>")` | X1 |
| Removal Compliance Rate | `=U1/T1` (format as %) | Y1 |

### Data Validation (Dropdowns)

**Removal Status (Column M):**
- List: Executed, In Progress, Not Started, Blocked

**Removal Verified (Column N):**
- List: Yes - Verified, No - Not Verified, Pending

### Conditional Formatting Rules

**Removal Delay (Column J):**
- Rule 1: If ≤5 → Fill: C6EFCE (green)
- Rule 2: If 6-10 → Fill: FFEB9C (yellow)
- Rule 3: If >10 → Fill: FFC7CE (red)

**SLA Met (Column L):**
- Rule 1: If "✅ Yes" → Fill: C6EFCE (green)
- Rule 2: If "❌ No" → Fill: FFC7CE (red)

**Removal Status (Column M):**
- Rule 1: If "Executed" → Fill: C6EFCE (green)
- Rule 2: If "In Progress" → Fill: FFEB9C (yellow)
- Rule 3: If "Not Started" OR "Blocked" → Fill: FFC7CE (red)

**Removal Verified (Column N):**
- Rule 1: If "Yes - Verified" → Fill: C6EFCE (green)
- Rule 2: If "Pending" → Fill: FFEB9C (yellow)

**Evidence Location (Column O):**
- Rule 1: If BLANK AND Removal Verified = "Yes - Verified" → Fill: FFEB9C (yellow)

---

## Sheet 7: Access_Review_Compliance_Dashboard

### Purpose
Consolidated review metrics and overall compliance scoring.

### Header Section (Rows 1-3)
**Row 1:** "ACCESS REVIEW COMPLIANCE DASHBOARD"  
**Row 2:** "Overall access review execution and compliance metrics"  
**Row 3:** Section headers

### Dashboard Layout (Rows 5+)

#### Section 1: Review Completion Summary (Rows 5-13)

| Metric | Value (Formula) | Target | Status | Cell Reference |
|--------|----------------|--------|--------|----------------|
| **Review Period** | `=Sheet2!A4` (first row value) | N/A | N/A | B5 |
| **Systems in Scope** | `=Sheet2!P1` | N/A | N/A | B6 |
| **Users in Scope** | `=Sheet2!T1` | N/A | N/A | B7 |
| **Reviewers Assigned** | `=Sheet4!T1` | N/A | N/A | B8 |
| **Reviews Completed** | `=Sheet4!U1` | All | N/A | B9 |
| **Reviews Overdue** | `=Sheet4!X1` | 0 | `=IF(B10=0,"✅",IF(B10<=3,"⚠️","❌"))` | B10 |
| **Review Completion Rate** | `=Sheet4!Y1` (format as %) | ≥90% | `=IF(B11>=0.90,"✅",IF(B11>=0.75,"⚠️","❌"))` | B11 |

#### Section 2: Review Findings Summary (Rows 15-23)

| Metric | Value (Formula) | Target | Status | Cell Reference |
|--------|----------------|--------|--------|----------------|
| **Access Grants Reviewed** | `=Sheet5!Q1` | All in scope | N/A | B15 |
| **Access Confirmed** | `=Sheet5!R1` | Majority | N/A | B16 |
| **Access to Remove** | `=Sheet5!S1` | Expected findings | N/A | B17 |
| **Access Justified** | `=Sheet5!T1` | Minimal exceptions | N/A | B18 |
| **No Response** | `=Sheet5!U1` | 0 | `=IF(B19=0,"✅",IF(B19<=10,"⚠️","❌"))` | B19 |
| **Confirmation Rate** | `=Sheet5!V1` (format as %) | Variable | N/A | B20 |
| **Removal Rate** | `=Sheet5!W1` (format as %) | Variable | N/A | B21 |

#### Section 3: Access Removal Execution (Rows 25-33)

| Metric | Value (Formula) | Target | Status | Cell Reference |
|--------|----------------|--------|--------|----------------|
| **Removal Requests** | `=Sheet6!S1` | N/A | N/A | B25 |
| **Removals Executed** | `=Sheet6!T1` | 100% | `=IF(B26=B25,"✅",IF(B26/B25>=0.90,"⚠️","❌"))` | B26 |
| **Removals On-Time (≤5 days)** | `=Sheet6!U1` | ≥90% | N/A | B27 |
| **Removals Late (6-10 days)** | `=Sheet6!V1` | <5% | N/A | B28 |
| **Removals Very Late (>10 days)** | `=Sheet6!W1` | 0 | `=IF(B29=0,"✅","❌")` | B29 |
| **Removals Not Executed** | `=Sheet6!X1` | 0 | `=IF(B30=0,"✅","🚨 CRITICAL")` | B30 |
| **Removal Compliance Rate** | `=Sheet6!Y1` (format as %) | ≥90% | `=IF(B31>=0.90,"✅",IF(B31>=0.75,"⚠️","❌"))` | B31 |

#### Section 4: Overall Access Review Compliance Score (Rows 35-45)

**Weighted Calculation:**
```
Review Compliance Score = 
  (Review Completion Rate × 50%) + 
  (Removal Execution Rate × 30%) + 
  (Removal Timeliness × 20%)
```

| Component | Weight | Score | Weighted Score | Cell |
|-----------|--------|-------|----------------|------|
| Review Completion | 50% | `=B11` | `=B11*0.50` | D36 |
| Removal Execution | 30% | `=B26/B25` | `=(B26/B25)*0.30` | D37 |
| Removal Timeliness | 20% | `=B31` | `=B31*0.20` | D38 |
| **Total Compliance Score** | **100%** | N/A | `=SUM(D36:D38)` | **D39** |

**Benchmark Categories:**

| Score Range | Maturity Level | Description | Cell |
|-------------|----------------|-------------|------|
| 90-100% | ✅ **Excellent** | Best-in-class review execution | B41 |
| 75-89% | ⚠️ **Good** | Strong review compliance, minor gaps | B42 |
| 60-74% | ⚠️ **Fair** | Acceptable but significant gaps | B43 |
| <60% | ❌ **Poor** | Major review deficiencies, audit risk | B44 |

**Current Maturity Level:**
```excel
=IF(D39>=0.90, "✅ Excellent", 
  IF(D39>=0.75, "⚠️ Good", 
    IF(D39>=0.60, "⚠️ Fair", "❌ Poor")))
```

### Conditional Formatting Rules

**Status Columns (All sections):**
- Rule 1: If "✅" → Fill: C6EFCE (green)
- Rule 2: If "⚠️" → Fill: FFEB9C (yellow)
- Rule 3: If "❌" → Fill: FFC7CE (red)
- Rule 4: If "🚨 CRITICAL" → Fill: FF0000 (dark red)

**Compliance Score (D39):**
- Rule 1: If ≥0.90 → Fill: C6EFCE (green)
- Rule 2: If 0.75-0.89 → Fill: FFEB9C (yellow)
- Rule 3: If 0.60-0.74 → Fill: FFEB9C (yellow)
- Rule 4: If <0.60 → Fill: FFC7CE (red)

---

## Sheet 8: Gap_Analysis_and_Remediation

### Purpose
Identify gaps (overdue reviews, unexecuted removals) and track remediation.

### Header Section (Rows 1-3)
**Row 1:** "GAP ANALYSIS & REMEDIATION ROADMAP"  
**Row 2:** "Identify access review deficiencies and track remediation"  
**Row 3:** Column headers

### Column Definitions (Rows 3+)

| Column | Header | Type | Description | Formula/Source | Conditional Formatting |
|--------|--------|------|-------------|----------------|----------------------|
| A | Gap ID | Text | Unique identifier | **USER INPUT** (GAP-001) | None |
| B | Gap Type | Dropdown | Category | Dropdown: Review Not Completed, Removal Not Executed, Removal Executed Late, Reviewer Unresponsive, Process Issue, Other | None |
| C | Gap Description | Text | What is the gap? | **USER INPUT** | None |
| D | Affected Users/Count | Text/Number | How many affected? | **USER INPUT** | None |
| E | Source Sheet | Dropdown | Where identified? | Dropdown: Sheet 4 (Completion), Sheet 6 (Removal), Other | None |
| F | Risk Level | Dropdown | Severity | Dropdown: Critical, High, Medium, Low | **CF:** Dark Red if Critical, Red if High |
| G | Business Impact | Text | What's the risk? | **USER INPUT** | None |
| H | Root Cause | Text | Why happened? | **USER INPUT** | None |
| I | Remediation Plan | Text | What action? | **USER INPUT** | None |
| J | Remediation Owner | Text | Who responsible? | **USER INPUT** | **CF:** Yellow if BLANK |
| K | Target Date | Date | When resolved? | **USER INPUT** | **CF:** Red if past due |
| L | Status | Dropdown | Progress | Dropdown: Open, In Progress, Blocked, Completed, Closed | **CF:** Green if Completed/Closed |
| M | % Complete | Number | Progress | **USER INPUT** (0-100) | **CF:** Data bars |
| N | Notes | Text | Updates | **USER INPUT** | None |

### Summary Metrics (Top of Sheet, Rows 1-2, Columns P-U)

| Metric | Formula | Cell |
|--------|---------|------|
| Total Gaps | `=COUNTA(A:A)-1` | P1 |
| Critical Gaps | `=COUNTIF(F:F,"Critical")` | Q1 |
| High Gaps | `=COUNTIF(F:F,"High")` | R1 |
| Medium Gaps | `=COUNTIF(F:F,"Medium")` | S1 |
| Gaps Closed | `=COUNTIF(L:L,"Closed")+COUNTIF(L:L,"Completed")` | T1 |
| Resolution Rate | `=T1/P1` (format as %) | U1 |

### Data Validation (Dropdowns)

**Gap Type (Column B):**
- List: Review Not Completed, Removal Not Executed, Removal Executed Late, Reviewer Unresponsive, No Response from Reviewer, Process Issue, Other

**Source Sheet (Column E):**
- List: Sheet 4 (Completion), Sheet 5 (Findings), Sheet 6 (Removal), Multiple, Other

**Risk Level (Column F):**
- List: Critical, High, Medium, Low

**Status (Column L):**
- List: Open, In Progress, Blocked, Completed, Closed

### Conditional Formatting Rules

**Risk Level (Column F):**
- Rule 1: If "Critical" → Fill: FF0000 (dark red)
- Rule 2: If "High" → Fill: FFC7CE (red)
- Rule 3: If "Medium" → Fill: FFEB9C (yellow)

**Remediation Owner (Column J):**
- Rule 1: If BLANK → Fill: FFEB9C (yellow)

**Target Date (Column K):**
- Rule 1: If < TODAY() AND Status ≠ "Completed" AND Status ≠ "Closed" → Fill: FFC7CE (red)

**Status (Column L):**
- Rule 1: If "Completed" OR "Closed" → Fill: C6EFCE (green)
- Rule 2: If "In Progress" → Fill: FFEB9C (yellow)
- Rule 3: If "Blocked" → Fill: FFC7CE (red)

**% Complete (Column M):**
- Data bars: Green gradient

---

## Sheet 9: Evidence_Register

### Purpose
Document all supporting evidence.

### Header Section (Rows 1-3)
**Row 1:** "EVIDENCE REGISTER"  
**Row 2:** "Document all evidence supporting this assessment"  
**Row 3:** Column headers

### Column Definitions (Rows 3-103, 100 rows)

| Column | Header | Type | Description | Conditional Formatting |
|--------|--------|------|-------------|----------------------|
| A | Evidence ID | Text | Unique identifier | None |
| B | Evidence Type | Dropdown | Category | None |
| C | Description | Text | What is this? | None |
| D | Related Sheet/Row | Text | Where referenced? | None |
| E | Location/Path | Text | File path or URL | None |
| F | Date Collected | Date | When captured? | **CF:** Red if >90 days |
| G | Collected By | Text | Who gathered? | None |
| H | Verification Status | Dropdown | Verified? | **CF:** Green if Verified, Yellow if Pending |

### Data Validation (Dropdowns)

**Evidence Type (Column B):**
- List: Review Scope Document, Reviewer Assignment, Review Completion Sign-Off, Review Findings Report, Access Removal Ticket, Removal Audit Log, Escalation Email, Policy Document, Meeting Notes, Other

**Verification Status (Column H):**
- List: Verified, Pending Verification, Not Verified, N/A

### Conditional Formatting Rules

**Date Collected (Column F):**
- Rule 1: If (TODAY() - F) > 90 → Fill: FFC7CE (red)

**Verification Status (Column H):**
- Rule 1: If "Verified" → Fill: C6EFCE (green)
- Rule 2: If "Pending Verification" → Fill: FFEB9C (yellow)

---

## Sheet 10: Approval_and_Sign_Off

### Purpose
Three-level approval workflow.

### Assessment Summary Section (Rows 3-14)
```
Assessment Document:              ISMS-IMP-A.5.15-16-18.S3 - Access Review Results
Review Period:                    [Formula: =Sheet2!A4]
Systems Reviewed:                 [Formula: =Sheet7!B6]
Review Completion Rate:           [Formula: =Sheet7!B11]
Access Grants Reviewed:           [Formula: =Sheet7!B15]
Access Removal Requests:          [Formula: =Sheet7!B25]
Removal Compliance Rate:          [Formula: =Sheet7!B31]
Overall Review Compliance Score:  [Formula: =Sheet7!D39]
Critical Gaps:                    [Formula: =Sheet8!Q1]
Assessment Status:                [Dropdown: Draft, Final, Requires Remediation]
```

### Assessment Completed By (Rows 16-23)
```
Name:                [USER INPUT]
Role/Title:          [USER INPUT - Security Team, Review Coordinator]
Department:          [USER INPUT]
Email:               [USER INPUT]
Date Completed:      [USER INPUT]
Signature/Initials:  [USER INPUT]
Completion Notes:    [Text area]
```

### Reviewed By - IAM Team Lead (Rows 25-33)
```
Name:                     [USER INPUT]
Role/Title:               IAM Team Lead
Date Reviewed:            [USER INPUT]
Review Notes:             [Text area]
Removal Execution:        [Dropdown: Verified, Issues Found, Not Reviewed]
Removal Timeliness:       [Dropdown: Compliant, Issues Found, Not Reviewed]
Recommendation:           [Dropdown: Approve, Approve with Conditions, Reject]
Conditions/Comments:      [Text area]
```

### Approved By - CISO (Rows 35-43)
```
Name:                     [USER INPUT]
Role/Title:               CISO
Date Approved:            [USER INPUT]
Approval Decision:        [Dropdown: Approved, Approved with Conditions, Rejected]
Risk Acceptance:          [Text area]
Conditions/Comments:      [Text area]
Final Approval:           [Dropdown: Yes - Final, No - See conditions]
```

### Next Review Details (Rows 45-51)
```
Next Review Type:         [Dropdown: Quarterly, Semi-Annual, Annual]
Next Review Date:         [Date - auto-calculate based on type]
Review Coordinator:       [USER INPUT]
Special Considerations:   [Text area]
```

---

## Cell Styling Reference

(Same as previous IMPs - consistent styling)

---

## Freeze Panes

- All sheets: Freeze at A4

---

## File Naming Convention

**Format:** `ISMS-IMP-A.5.15-16-18.S3_Access_Review_Results_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.5.15-16-18.S3_Access_Review_Results_Q1-2026.xlsx`

---

## Quarterly Review Cycle

1. **Define Scope** (Sheet 2)
2. **Assign Reviewers** (Sheet 3)
3. **Track Completion** (Sheet 4) - daily/weekly updates
4. **Collect Findings** (Sheet 5)
5. **Execute Removals** (Sheet 6)
6. **Calculate Compliance** (Sheet 7)
7. **Identify Gaps** (Sheet 8)
8. **Register Evidence** (Sheet 9)
9. **Obtain Approval** (Sheet 10)

**Time:** 10-15 hours per quarter

---

## Integration Points

**A.5.15-16-18.2 - Access Rights Matrix:**
- **Input FROM IMP.2:** Access matrix defines WHAT to review

**A.5.15-16-18.1 - User Inventory:**
- **Input FROM IMP.1:** User and manager data

**A.5.15-16-18.5 - IAM Governance Dashboard:**
- **Input FROM this workbook:** Review metrics (Sheet 7)

---

**END OF TECHNICAL SPECIFICATION**

*"The first principle is that you must not fool yourself – and you are the easiest person to fool."*  
– Richard Feynman

**ISMS Maturity Indicator:** If you can systematically review access, track completion, remediate findings within 5 days, and hold reviewers accountable for non-completion, you understand that access review is not a checkbox exercise – it's an ongoing verification that access remains appropriate. ✅

