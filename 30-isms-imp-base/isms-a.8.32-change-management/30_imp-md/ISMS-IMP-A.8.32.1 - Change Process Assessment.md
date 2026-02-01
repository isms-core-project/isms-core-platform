**ISMS-IMP-A.8.32.1 - Change Process Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.32.1 |
| **Version** | 1.0 |
| **Assessment Area** | Change Process Workflow & Management Procedures |
| **Related Policy** | ISMS-POL-A.8.32, Section 2.1 (Change Process Requirements) |
| **Purpose** | Document change management processes, assess procedural capabilities against policy requirements, and identify gaps in a technology-agnostic manner |
| **Target Audience** | Change Manager, CAB Members, IT Operations, System Owners, Compliance Officers, Auditors, Workbook Developers |
| **Assessment Type** | Process & Procedural |
| **Review Cycle** | Quarterly or After Major Process Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial assessment specification for Change Process workbook | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formula Definitions
  - Cell Styling Reference


**Target Audiences:**

- **Part I:** Assessment users (Change Manager, CAB Members, IT Operations, Process Owners)
- **Part II:** Workbook developers (Python/Excel script maintainers)


---

# PART I: USER COMPLETION GUIDE

**Audience:** Change Manager, CAB Members, IT Operations, Process Owners

---

## Assessment Overview

### What This Assessment Evaluates

This assessment documents HOW your organization manages changes to information systems. It evaluates the end-to-end change process from request initiation through post-implementation review, verifying that your organization has structured, controlled procedures for handling changes.

### Why This Matters

This assessment verifies [Organization]'s compliance with:

- ISO/IEC 27001:2022 Control A.8.32: Change Management
- ISMS-POL-A.8.32, Section 2.1 (Change Process Requirements)
- Nine mandatory ISO 27002:2022 change management elements:
  - (a) Planning and impact assessment
  - (b) Authorization
  - (c) Communication
  - (d) Testing and acceptance (assessed in IMP-A.8.32.4)
  - (e) Implementation
  - (f) Emergency procedures (assessed in IMP-A.8.32.2)
  - (g) Record keeping
  - (h) Documentation updates
  - (i) Continuity plan updates


Change management failures are a leading cause of IT incidents. Proper change control prevents unauthorized modifications, reduces service disruptions, and ensures changes are properly tested and documented.

### Key Principle

This assessment is **completely technology-agnostic**. You document YOUR specific change management approach (whatever tools, workflows, and procedures you use), and verify capabilities against generic policy requirements.

Whether you use ServiceNow, Jira, BMC Remedy, custom tools, or spreadsheets - this assessment evaluates whether you have proper processes, not specific technologies.

---

## Prerequisites

### Before Starting This Assessment

**Required:**

- [ ] Read ISMS-POL-A.8.32 (Change Management Policy)
- [ ] Identify Change Manager or assessment owner
- [ ] Gather change management process documentation
- [ ] Access to change management system/tools
- [ ] Sample change requests (various types: standard, normal, emergency)
- [ ] CAB meeting minutes (last 3 months)
- [ ] Approval workflow documentation


**Recommended:**

- [ ] Interview Change Manager and key CAB members
- [ ] Review change failure metrics (last quarter)
- [ ] Gather Post-Implementation Review (PIR) examples
- [ ] Review emergency change procedures
- [ ] Identify change management tool administrators


### Who Should Complete This Assessment

**Primary:** Change Manager (overall assessment owner)

**Contributors:**

- CAB Chair (approval workflows, CAB operation)
- IT Operations Manager (implementation procedures, emergency changes)
- System Owners (system-specific change procedures)
- ITSM Tool Administrator (tool capabilities, reporting)
- Compliance Officer (regulatory requirements, audit readiness)


**Reviewers:**

- CISO (risk assessment validation)
- Internal Audit (control effectiveness)


---

## Assessment Workflow

### Step-by-Step Process

**Step 1: Initial Setup (Day 1)**

- Assign assessment owner (Change Manager)
- Schedule kick-off meeting with contributors
- Distribute assessment workbook
- Review completion timeline (typically 2-3 weeks)
- Identify evidence sources


**Step 2: Change Process Documentation (Days 2-5)**

- Document end-to-end change workflow (Sheet 2: Change_Process_Workflow)
- Map process stages to your organization's actual procedures
- Identify process owners for each stage
- Document standard durations
- Identify tools/systems used at each stage


**Step 3: Approval Authority Assessment (Days 3-6)**

- Complete approval authority matrix (Sheet 3: Approval_Authority_Matrix)
- Document who approves what based on risk level
- Verify approval workflows documented
- Check for separation of duties


**Step 4: CAB Operations Assessment (Days 4-7)**

- Document CAB composition and operation (Sheet 4: CAB_Operations)
- Review meeting frequency and attendance
- Assess effectiveness of CAB reviews
- Document escalation procedures


**Step 5: Communication & Stakeholder Management (Days 5-8)**

- Document stakeholder notification procedures (Sheet 5: Communication)
- Assess communication timeliness
- Review communication templates
- Verify feedback mechanisms


**Step 6: Documentation & Record Keeping (Days 6-9)**

- Assess change record completeness (Sheet 6: Documentation_Records)
- Review record retention practices
- Verify audit trail integrity
- Check documentation update procedures


**Step 7: Tool Capability Assessment (Days 7-10)**

- Inventory change management tools (Sheet 7: Tool_Capabilities)
- Assess tool features against requirements
- Identify tool limitations or gaps
- Document integration points


**Step 8: Metrics & KPIs (Days 8-11)**

- Document tracked metrics (Sheet 8: Metrics_KPIs)
- Review change success rates
- Assess emergency change percentage
- Analyze failure trends


**Step 9: Evidence Collection (Days 9-12)**

- Compile supporting evidence (Sheet 9: Evidence_Register)
- Link evidence to requirements
- Verify evidence accessibility
- Document evidence locations


**Step 10: Summary & Dashboard Review (Days 10-13)**

- Review auto-calculated compliance scores (Sheet 10: Summary_Dashboard)
- Validate gap analysis
- Prioritize remediation actions
- Prepare executive summary


**Step 11: Quality Review (Days 11-14)**

- Self-review against quality checklist (see below)
- Peer review by CAB members
- Compliance Officer review


**Step 12: Final Approval (Days 12-15)**

- Change Manager approval
- CISO review and approval
- Document sign-off (Sheet 11: Approval_Sign_Off)


**Total Duration:** 2-3 weeks from start to final approval

---

## Completing Each Sheet

### Sheet 1: Instructions & Legend

**Pre-filled content** - No user action required. Read carefully to understand:

- Status symbols (✅/⚠️/❌/📋/N/A)
- Compliance levels (90-100%, 70-89%, 50-69%, <50%)
- Evidence expectations


### Sheet 2: Change_Process_Workflow

**What to document:**

- Your organization's actual change lifecycle stages
- Process owner for each stage
- Standard duration for each stage
- Tools/systems used
- Current status (implemented, partial, planned)


**Tips:**

- Document what you ACTUALLY do, not what you think you should do
- If you skip stages, mark as N/A and explain in notes
- If processes are informal, document that honestly - assessment identifies gaps
- Include both standard and emergency change workflows


**Common Questions:**

- **Q:** "We don't have formal CAB meetings, just email approvals"
  - **A:** Document that! Mark CAB meeting as "⚠️ Partial" and note email approval process
- **Q:** "Emergency changes skip most steps"
  - **A:** Document standard process here, emergency variations in IMP-A.8.32.2


**Evidence to provide:**

- Process flowcharts or procedure documents
- Sample change requests showing workflow
- Approval email chains or system screenshots


### Sheet 3: Approval_Authority_Matrix

**What to document:**

- Who approves changes at different risk levels
- Approval authority by change type
- Delegation procedures
- Escalation paths


**Tips:**

- Be specific: "IT Operations Manager" not just "management"
- Document actual practice, not aspirational org chart
- If approval authority is unclear, this is a finding - document that
- Verify separation of duties (requester ≠ approver for high-risk changes)


**Common Questions:**

- **Q:** "What if we don't have documented approval authorities?"
  - **A:** Mark as "❌ Not Implemented" and document who actually approves in practice
- **Q:** "Does every single change need CISO approval?"
  - **A:** No - risk-based. Document thresholds (e.g., CISO only for critical-risk changes)


**Evidence to provide:**

- Approval matrix document
- Sample change requests with approvals
- Delegation of authority documents


### Sheet 4: CAB_Operations

**What to document:**

- CAB membership and roles
- Meeting frequency and attendance
- Review criteria and decision-making process
- Emergency CAB procedures


**Tips:**

- CAB can be standing committee or ad-hoc assembly
- Document actual attendance rates honestly
- If CAB meetings are ineffective, document that - it's a gap to remediate
- CAB review is not always required (e.g., standard changes skip CAB)


**Common Questions:**

- **Q:** "We don't have a formal CAB"
  - **A:** Mark as "❌ Not Implemented" - this is non-compliant with policy
- **Q:** "CAB meetings are poorly attended"
  - **A:** Document actual attendance - this identifies improvement opportunity


**Evidence to provide:**

- CAB charter or Terms of Reference
- Meeting minutes (last 3 months)
- Attendance records
- CAB decision log


### Sheet 5: Communication

**What to document:**

- Stakeholder notification procedures
- Communication templates
- Notification timing (advance notice requirements)
- Feedback mechanisms


**Tips:**

- Distinguish between user communication (service impact) and technical communication (implementation teams)
- Document communication failures if they occur - helps identify process improvements
- Automated notifications (e.g., from ITSM tool) are valid - document system capabilities


**Common Questions:**

- **Q:** "How much advance notice is enough?"
  - **A:** Policy says "appropriate to impact" - document YOUR standard (e.g., 48 hours for major changes)
- **Q:** "We forget to communicate sometimes"
  - **A:** Document current state honestly - mark as "⚠️ Partial" and note improvement needed


**Evidence to provide:**

- Communication templates (emails, portal notifications)
- Sample notifications sent to users
- Communication calendar or schedule


### Sheet 6: Documentation_Records

**What to document:**

- What gets documented in change records
- Record retention periods
- Audit trail capabilities
- Documentation update procedures (system docs, runbooks)


**Tips:**

- Distinguish between change request documentation (the change itself) and updated system documentation (post-change updates)
- If documentation updates lag behind changes, document that honestly
- Record retention should align with legal/regulatory requirements


**Common Questions:**

- **Q:** "We don't always update documentation after changes"
  - **A:** Common problem - mark as "⚠️ Partial" and document target improvement
- **Q:** "How long should we keep change records?"
  - **A:** Policy requires [Organization-defined] - document YOUR retention period


**Evidence to provide:**

- Sample change records showing completeness
- Documentation update procedures
- System documentation examples (showing recent updates)


### Sheet 7: Tool_Capabilities

**What to document:**

- Change management system/tools used
- Tool capabilities (workflow, approval, reporting, audit trail)
- Tool limitations or gaps
- Integration with other systems (CMDB, monitoring, etc.)


**Tips:**

- This is NOT a vendor evaluation - document capabilities objectively
- If you use multiple tools (e.g., Jira + spreadsheets), document all
- Tool limitations are common - document them, don't hide them
- N/A if you don't have automated tools - spreadsheets and email are valid (though less mature)


**Common Questions:**

- **Q:** "We use spreadsheets, not ITSM tools"
  - **A:** Document that - this may be compliant for small organizations, but identify capability gaps
- **Q:** "Our tool can't do X"
  - **A:** Document tool limitation - this informs future tool investment decisions


**Evidence to provide:**

- Tool screenshots (change request form, approval workflow, reports)
- Tool capabilities documentation
- Integration architecture diagrams


### Sheet 8: Metrics_KPIs

**What to document:**

- Change metrics tracked (volume, success rate, duration, emergency %)
- Reporting frequency and recipients
- Metric trends and analysis
- KPI targets and actual performance


**Tips:**

- If you don't track metrics systematically, mark as gap
- Even informal tracking (e.g., "we count emergency changes manually") is better than nothing
- Focus on metrics that drive improvement, not vanity metrics


**Common Questions:**

- **Q:** "What metrics should we track?"
  - **A:** Policy requires at minimum: change volume, success rate, emergency %, PIR completion. Document YOUR metrics.
- **Q:** "We don't track change metrics"
  - **A:** Mark as "❌ Not Implemented" - significant gap requiring remediation


**Evidence to provide:**

- Change metrics reports (last quarter)
- KPI dashboards or spreadsheets
- Trend analysis (if available)


### Sheet 9: Evidence_Register

**What to document:**

- Evidence location for each requirement
- Evidence type (document, system data, interview notes)
- Last verification date
- Evidence accessibility (who can access)


**Tips:**

- Be specific: "SharePoint > ISMS > Change Management > Process Docs > v2.3"
- Reference real documents/systems, not hypothetical evidence
- If evidence doesn't exist, mark requirement status accordingly in other sheets
- Evidence can be screenshots, documents, system exports, meeting minutes, etc.


**Common Questions:**

- **Q:** "What if evidence is scattered across multiple locations?"
  - **A:** Document all locations - this may identify need for centralized evidence repository
- **Q:** "Some evidence is in people's heads (undocumented)"
  - **A:** Not acceptable evidence - mark as gap


**Evidence to provide:**

- Links/paths to actual evidence locations


### Sheet 10: Summary_Dashboard

**Auto-calculated** - Review for accuracy:

- Overall compliance percentage
- Compliance by domain (process, approval, CAB, communication, etc.)
- Critical gaps requiring attention
- Audit readiness assessment


**What to check:**

- Do calculated percentages make sense?
- Are critical gaps accurately identified?
- Does overall assessment align with your subjective view?


**If discrepancies:** Review individual sheet entries for errors

### Sheet 11: Approval_Sign_Off

**What to complete:**

- Assessment completion date
- Change Manager sign-off
- CISO review and approval
- Next review date (typically +3 months)


**Tips:**

- Don't sign off until assessment is complete and accurate
- CISO may require remediation plans for critical gaps before approval
- Sign-off indicates "this assessment accurately reflects our current state" not "everything is perfect"


---

## Evidence Collection

### Types of Evidence

**Procedural Evidence:**

- Change management policy
- Process flowcharts and procedures
- Form templates (change request, PIR, etc.)
- Approval workflows
- Communication templates


**Operational Evidence:**

- Sample change requests (standard, normal, emergency)
- CAB meeting minutes
- Approval email chains or system records
- Stakeholder notifications
- PIRs for completed changes


**System Evidence:**

- ITSM tool screenshots (with sensitive data redacted)
- Change calendar exports
- Metrics reports
- Audit logs


**Interview Evidence:**

- Notes from conversations with Change Manager, CAB members
- Process walkthroughs
- Tool demonstrations


### Evidence Best Practices

**Do:**

- ✅ Reference specific documents with version numbers and dates
- ✅ Use system-generated evidence where available (better than manual documentation)
- ✅ Redact sensitive data (server names, IP addresses, personal data) but keep enough context
- ✅ Date all evidence
- ✅ Provide links or file paths to evidence locations


**Don't:**

- ❌ Create evidence just for the assessment (document what you actually do)
- ❌ Reference evidence that doesn't exist yet
- ❌ Provide incomplete or outdated evidence
- ❌ Rely solely on verbal confirmation without documentation


---

## Common Pitfalls

### Mistake #1: "We're doing everything, we just haven't documented it"

**Problem:** Undocumented processes are not auditable and not verifiable.

**Solution:** If processes are informal, mark status as "⚠️ Partial" and note documentation gap. Assessment identifies improvement opportunities.

### Mistake #2: "Let's document what we SHOULD do, not what we ACTUALLY do"

**Problem:** Assessment becomes fiction. Auditors will verify against actual practice.

**Solution:** Document current state honestly. Gaps are OK - that's the point of assessment!

### Mistake #3: "We use email for approvals, so we have no change management"

**Problem:** Confusing tool maturity with process compliance.

**Solution:** Email approvals CAN be compliant if properly documented, archived, and auditable. Document your email-based process, note tool limitation, plan tool improvement.

### Mistake #4: "Emergency changes happen too fast to document"

**Problem:** Emergency procedures still need control and retroactive documentation.

**Solution:** Document that emergency changes follow abbreviated process. Assess whether PIRs are conducted post-emergency (policy requires this).

### Mistake #5: "CAB meetings are rubber stamps, nobody pays attention"

**Problem:** CAB is performing security theater, not actual review.

**Solution:** Document low engagement honestly - this is process improvement opportunity, not something to hide.

### Mistake #6: "We skip documentation updates because we're too busy"

**Problem:** Out-of-date documentation causes operational incidents and audit findings.

**Solution:** Mark as "⚠️ Partial" or "❌ Not Implemented", document target improvement timeline.

### Mistake #7: "Standard changes don't need to be logged"

**Problem:** Even pre-approved changes need audit trail.

**Solution:** Verify standard changes are logged (even if abbreviated). If not logged, this is gap.

### Mistake #8: "We track metrics but never analyze them"

**Problem:** Metrics without analysis provide no value.

**Solution:** If metrics are tracked but not reviewed/acted upon, mark as "⚠️ Partial" - collection is good, analysis is missing.

### Mistake #9: "This assessment will take 6 months to complete"

**Problem:** Analysis paralysis and perfectionism.

**Solution:** Assessment should take 2-3 weeks. Document current state, identify gaps, move on. Perfection is not the goal.

### Mistake #10: "Nobody will review this anyway"

**Problem:** Low-quality assessment provides no value and fails audit.

**Solution:** Take it seriously - auditors WILL review this, and gaps identified here drive remediation priorities.

---

## Quality Checklist

### Before Submitting for Approval

**Assessment Completeness:**

- [ ] All sheets completed (no yellow cells remaining)
- [ ] Status indicators (✅/⚠️/❌/📋/N/A) used consistently
- [ ] All N/A entries have justification notes
- [ ] Free-text fields completed (not just "TBD" or "N/A")


**Evidence Quality:**

- [ ] Evidence location documented for all requirements
- [ ] Evidence is specific (document names, versions, dates)
- [ ] Evidence is accessible to auditors
- [ ] Sensitive data redacted appropriately
- [ ] Evidence Register sheet completed


**Accuracy & Honesty:**

- [ ] Assessment reflects ACTUAL current state, not aspirational state
- [ ] Gaps documented honestly
- [ ] Known issues not hidden
- [ ] Process improvements identified


**Policy Alignment:**

- [ ] All ISMS-POL-A.8.32 Section 2.1 requirements addressed
- [ ] Cross-references to policy sections accurate
- [ ] Compliance scoring methodology followed


**Stakeholder Input:**

- [ ] Change Manager reviewed and approved
- [ ] Key CAB members consulted
- [ ] IT Operations input obtained
- [ ] Process owners validated their sections


**Technical Accuracy:**

- [ ] Tool capabilities accurately described
- [ ] Approval workflows correct
- [ ] Metrics data current (last quarter)
- [ ] Process durations realistic


**Dashboard Validation:**

- [ ] Overall compliance percentage reasonable
- [ ] Critical gaps align with known issues
- [ ] Compliance by domain makes sense
- [ ] Audit readiness assessment matches subjective view


**Next Steps Defined:**

- [ ] Remediation priorities identified
- [ ] Target dates for gap closure
- [ ] Responsible parties assigned
- [ ] Next review date set (typically +3 months)


---

## Review & Approval

### Review Process

**Step 1: Self-Review (Change Manager)**

- Complete quality checklist above
- Validate all data entry
- Check formula calculations in Summary Dashboard
- Verify evidence completeness


**Step 2: Peer Review (CAB Members)**

- Distribute draft to key CAB members
- Request feedback on process documentation accuracy
- Incorporate feedback
- Typical turnaround: 3-5 days


**Step 3: Compliance Review (Compliance Officer)**

- Compliance Officer reviews:
  - Policy alignment
  - Evidence adequacy
  - Regulatory requirement coverage
  - Audit readiness
- Decision: Approved / Revisions Required
- Typical turnaround: 2-3 days


**Step 4: CISO Approval**

- CISO reviews:
  - Overall process maturity
  - Critical gap risk acceptance
  - Remediation plan adequacy
  - Audit readiness
- Decision: Approved / Approved with Conditions / Rejected
- Typical turnaround: 2-3 days


**Step 5: Documentation & Communication**

- Set assessment status to "Final"
- Set next review date (+3 months)
- File in document management
- Notify gap owners of assignments
- Create reminders for:
  - Gap remediation dates
  - Next quarterly assessment
  - Policy review triggers


**Approval Timeline:** 2-3 weeks from submission to final approval

**If Rejected:**

Common reasons for rejection:

- Incomplete process documentation
- Insufficient evidence
- Critical gaps without remediation plans
- Unrealistic gap closure timelines
- Missing stakeholder input


---

## Continuous Improvement

### Using Assessment Results

**Gap Remediation:**

- Prioritize critical gaps (red flags in dashboard)
- Assign owners and target dates
- Track progress monthly
- Re-assess quarterly


**Process Optimization:**

- Review change failure patterns - common failure modes?
- Analyze emergency change % - too high? Why?
- Review approval bottlenecks - delays in process?
- Assess communication effectiveness - users surprised by changes?


**Metric-Driven Decisions:**

- Success rate declining? → Process review needed
- Emergency changes increasing? → Planning issues or genuine emergencies?
- PIR completion rate low? → Enforcement or resource issue?
- Average change duration increasing? → Approval bottlenecks?


**Stakeholder Feedback:**

- Survey change requesters - is process clear?
- Survey CAB members - meetings effective?
- Survey implementers - adequate planning time?
- Survey users - communication adequate?


---

**END OF PART I: USER COMPLETION GUIDE**


---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.32.1  
**Assessment Area:** Change Process Workflow & Management Procedures  
**Related Policy:** ISMS-POL-A.8.32, Section 2.1 (Change Process Requirements)  
**Purpose:** Document change management processes, assess procedural capabilities against policy requirements, and identify gaps in a technology-agnostic manner

**Key Principle:** This assessment is **technology-independent**. Organizations document THEIR specific change management approach (tools, workflows, procedures) and verify capabilities against generic requirements.

---

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section

- **Title:** "ISMS-IMP-A.8.32.1 – Change Process Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.32: Change Management"
- **Styling:** Dark blue header (003366), white text, centered, 40px height


#### Document Information Block
```
Document ID:           ISMS-IMP-A.8.32.1
Assessment Area:       Change Process Workflow & Management
Related Policy:        ISMS-POL-A.8.32, Section 2.1
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [Organization]
Review Cycle:          Quarterly
```

#### How to Use This Workbook
1. Document YOUR organization's change management process in the Change_Process_Workflow sheet
2. Complete the Approval_Authority_Matrix with YOUR specific roles and thresholds
3. Fill in YOUR communication procedures and stakeholder notification methods
4. Document YOUR documentation requirements and record-keeping practices
5. Inventory YOUR change management tools (whatever platforms/systems you use)
6. Review the Summary_Dashboard for compliance metrics
7. Maintain the Evidence Register for audit traceability
8. Obtain final approval and sign-off

#### Status Legend
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Implemented | Process implemented and operational | Green (C6EFCE) |
| ⚠️ | Partial | Partial implementation or limited coverage | Yellow (FFEB9C) |
| ❌ | Not Implemented | Process not implemented | Red (FFC7CE) |
| 📋 | Planned | Implementation planned with target date | Blue (B4C7E7) |
| N/A | Not Applicable | Not applicable to this environment | Gray |

#### Compliance Levels
| Level | Percentage | Description |
|-------|------------|-------------|
| Fully Compliant | 90-100% | All requirements met, evidence documented |
| Substantially Compliant | 70-89% | Most requirements met, minor gaps |
| Partially Compliant | 50-69% | Significant gaps, remediation required |
| Non-Compliant | <50% | Major deficiencies, immediate action required |

#### Acceptable Evidence (Examples)

- ✓ Change management policy documents
- ✓ Process flowcharts/diagrams
- ✓ Change request form templates
- ✓ Change Advisory Board (CAB) meeting minutes
- ✓ Approval workflow documentation
- ✓ Communication templates (notification emails, status updates)
- ✓ Change management tool screenshots (redacted if needed)
- ✓ Change calendar/schedule examples
- ✓ Post-Implementation Review (PIR) templates
- ✓ Change failure metrics/reports
- ✓ Emergency change procedure documentation
- ✓ Training materials for change requesters/approvers


---

## Sheet 2: Change_Process_Workflow

### Purpose
Document the end-to-end change management process from request initiation through post-implementation review.

### Header Section
**Row 1:** "CHANGE MANAGEMENT PROCESS WORKFLOW"  
**Row 2:** "Document the complete change lifecycle in your organization"

### Process Stage Mapping Section (Rows 4-25)

| Stage | Stage Name | Description | Process Owner | Standard Duration | Tool/System Used | Status | Evidence Location |
|-------|------------|-------------|---------------|-------------------|------------------|--------|-------------------|
| 1 | Change Request Initiation | How changes are requested | Text | Text (e.g., "1 day") | Text | Dropdown: ✅/⚠️/❌/📋/N/A | Text |
| 2 | Initial Assessment & Screening | Validation and categorization | Text | Text | Text | Dropdown | Text |
| 3 | Risk & Impact Assessment | Evaluate change risks | Text | Text | Text | Dropdown | Text |
| 4 | Change Categorization | Standard/Normal/Emergency | Text | Text | Text | Dropdown | Text |
| 5 | CAB Scheduling (if required) | Schedule review meeting | Text | Text | Text | Dropdown | Text |
| 6 | CAB Review & Discussion | Formal review process | Text | Text | Text | Dropdown | Text |
| 7 | Approval Decision | Obtain required approvals | Text | Text | Text | Dropdown | Text |
| 8 | Implementation Planning | Detailed execution planning | Text | Text | Text | Dropdown | Text |
| 9 | Stakeholder Communication | Notify affected parties | Text | Text | Text | Dropdown | Text |
| 10 | Change Implementation | Execute change | Text | Text | Text | Dropdown | Text |
| 11 | Verification & Validation | Confirm success | Text | Text | Text | Dropdown | Text |
| 12 | Rollback (if needed) | Revert to previous state | Text | Text | Text | Dropdown | Text |
| 13 | Documentation Update | Update system docs | Text | Text | Text | Dropdown | Text |
| 14 | Continuity Plan Update | Update DR/BC plans if needed | Text | Text | Text | Dropdown | Text |
| 15 | Post-Implementation Review | Lessons learned | Text | Text | Text | Dropdown | Text |
| 16 | Change Closure | Close change record | Text | Text | Text | Dropdown | Text |

**Column Widths:**

- A: 8, B: 30, C: 35, D: 20, E: 18, F: 25, G: 12, H: 30


### Process Requirements Assessment (Rows 27-50)

**Section Header:** "CHANGE PROCESS REQUIREMENTS ASSESSMENT"

| Requirement ID | Requirement | Implemented | How Implemented | Tool/System | Status | Evidence |
|----------------|-------------|-------------|-----------------|-------------|--------|----------|
| REQ-PROCESS-001 | Change request procedures | Dropdown: Yes/No/Partial | Text (editable) | Text | Dropdown: ✅/⚠️/❌/📋 | Text |
| REQ-PROCESS-002 | Risk assessment | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-003 | Impact assessment | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-004 | Change classification | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-005 | Approval workflows | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-006 | CAB operation | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-007 | Emergency procedures | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-008 | Communication | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-009 | Implementation planning | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-010 | Testing requirements | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-011 | Rollback plans | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-012 | Documentation | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-013 | PIR mandatory | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-014 | Continuous improvement | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-015 | Record retention | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-016 | Tool capabilities | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-017 | Integration | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-018 | Metrics/KPIs | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-019 | Training | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-020 | Governance | Dropdown | Text | Text | Dropdown | Text |

### Critical Findings (Rows 52-57)

| Finding Type | Count | Description |
|--------------|-------|-------------|
| Critical Gaps | Formula (count ❌ from all sheets) | Text area (auto-populate key gaps) |
| High-Priority Items | Formula (count ⚠️) | Text area |
| Planned Improvements | Formula (count 📋) | Text area |

### Audit Readiness Assessment (Rows 59-65)

| Criterion | Status | Notes |
|-----------|--------|-------|
| All processes documented | Formula: ✅/⚠️/❌ | Text |
| Evidence available for key controls | Formula | Text |
| Roles and responsibilities defined | Formula | Text |
| Tool capabilities verified | Formula | Text |
| Compliance ≥70% | Formula | Text |
| **OVERALL AUDIT READINESS** | Formula | Text |

---

## Sheet 3: Approval_Authority_Matrix

### Purpose
Document approval authorities for different change types and risk levels.

### Header Section
**Row 1:** "APPROVAL AUTHORITY MATRIX"  
**Row 2:** "Define who approves changes at different risk levels"

### Approval Authority by Risk Level (Rows 4-12)

| Risk Level | Change Type | Primary Approver | Secondary Approver | Emergency Approver | Documented | Enforced | Evidence |
|------------|-------------|------------------|--------------------|--------------------|------------|----------|----------|
| Low | Standard Change | Text (role/title) | Text or N/A | Text | Dropdown: Yes/No | Dropdown: ✅/⚠️/❌ | Text |
| Medium | Normal Change | Text | Text | Text | Dropdown | Dropdown | Text |
| High | Normal Change | Text | Text | Text | Dropdown | Dropdown | Text |
| Critical | Normal Change | Text | Text | Text | Dropdown | Dropdown | Text |
| Emergency | Emergency Change | Text | Text | N/A | Dropdown | Dropdown | Text |

**Column Widths:**

- A: 15, B: 20, C: 25, D: 25, E: 25, F: 15, G: 12, H: 30


### Approval Requirements Assessment (Rows 14-30)

| Requirement | Implemented | Details | Status | Evidence |
|-------------|-------------|---------|--------|----------|
| Approval authority documented | Dropdown: Yes/No/Partial | Text | Dropdown: ✅/⚠️/❌ | Text |
| Risk-based approval levels | Dropdown | Text | Dropdown | Text |
| Separation of duties (requester ≠ approver) | Dropdown | Text | Dropdown | Text |
| Delegation procedures defined | Dropdown | Text | Dropdown | Text |
| Emergency approval procedures | Dropdown | Text | Dropdown | Text |
| Escalation paths documented | Dropdown | Text | Dropdown | Text |
| Approval timeframes defined | Dropdown | Text | Dropdown | Text |
| Approval tracked in system | Dropdown | Text | Dropdown | Text |
| Approval history auditable | Dropdown | Text | Dropdown | Text |
| Non-compliance consequences defined | Dropdown | Text | Dropdown | Text |

---

## Sheet 4: CAB_Operations

### Purpose
Assess Change Advisory Board (CAB) operations and effectiveness.

### Header Section
**Row 1:** "CHANGE ADVISORY BOARD (CAB) OPERATIONS"  
**Row 2:** "Document CAB composition, operation, and effectiveness"

### CAB Composition (Rows 4-15)

| Role | Name/Position | Attendance Rate | Decision Authority | Status | Notes |
|------|---------------|-----------------|--------------------| -------|-------|
| CAB Chair | Text | Text (e.g., "85%") | Text | Dropdown: ✅/⚠️/❌ | Text |
| Change Manager | Text | Text | Text | Dropdown | Text |
| Security Representative | Text | Text | Text | Dropdown | Text |
| IT Operations Rep | Text | Text | Text | Dropdown | Text |
| Application Owner Rep | Text | Text | Text | Dropdown | Text |
| Business Representative | Text | Text | Text | Dropdown | Text |
| [Additional Members] | Text | Text | Text | Dropdown | Text |

### CAB Operations Assessment (Rows 17-35)

| Requirement | Implemented | Details | Frequency/SLA | Status | Evidence |
|-------------|-------------|---------|---------------|--------|----------|
| CAB charter exists | Dropdown: Yes/No | Text | N/A | Dropdown: ✅/⚠️/❌ | Text |
| Regular meeting schedule | Dropdown | Text | Text (e.g., "Weekly") | Dropdown | Text |
| Meeting attendance tracked | Dropdown | Text | N/A | Dropdown | Text |
| Quorum requirements | Dropdown | Text | Text | Dropdown | Text |
| Meeting agenda distributed | Dropdown | Text | Text (e.g., "48h advance") | Dropdown | Text |
| Meeting minutes recorded | Dropdown | Text | N/A | Dropdown | Text |
| Decision criteria defined | Dropdown | Text | N/A | Dropdown | Text |
| Conflict resolution process | Dropdown | Text | N/A | Dropdown | Text |
| Emergency CAB procedures | Dropdown | Text | Text (e.g., "<4 hours") | Dropdown | Text |
| Virtual CAB option available | Dropdown | Text | N/A | Dropdown | Text |
| CAB effectiveness reviewed | Dropdown | Text | Text (e.g., "Annually") | Dropdown | Text |

### CAB Metrics (Rows 37-45)

| Metric | Last Quarter Value | Target | Status | Notes |
|--------|-------------------|--------|--------|-------|
| CAB meeting frequency | Text (e.g., "12 meetings") | Text | Formula: Green/Yellow/Red | Text |
| Average attendance rate | Text (e.g., "82%") | Text (e.g., ">80%") | Formula | Text |
| Changes reviewed by CAB | Text | Text | Formula | Text |
| CAB decisions overturned | Text | Text (e.g., "<5%") | Formula | Text |
| Average review duration | Text | Text | Formula | Text |

---

## Sheet 5: Communication_Stakeholder_Mgmt

### Purpose
Assess stakeholder communication procedures and effectiveness.

### Header Section
**Row 1:** "COMMUNICATION & STAKEHOLDER MANAGEMENT"  
**Row 2:** "Document how changes are communicated to affected stakeholders"

### Communication Procedures (Rows 4-20)

| Communication Type | Documented | Method | Timing | Template Exists | Status | Evidence |
|--------------------|------------|--------|--------|-----------------|--------|----------|
| Pre-change notification (users) | Dropdown: Yes/No | Text (e.g., "Email") | Text (e.g., "48h advance") | Dropdown: Yes/No | Dropdown: ✅/⚠️/❌ | Text |
| Pre-change notification (technical teams) | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Change approval notification | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Change schedule updates | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Implementation start notification | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Progress updates during change | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Change completion notification | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Rollback notification | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Post-implementation summary | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Incident/issue alerts | Dropdown | Text | Text | Dropdown | Dropdown | Text |

### Stakeholder Management Assessment (Rows 22-35)

| Requirement | Implemented | Details | Status | Evidence |
|-------------|-------------|---------|--------|----------|
| Stakeholder identification process | Dropdown: Yes/No/Partial | Text | Dropdown: ✅/⚠️/❌ | Text |
| Communication plan template | Dropdown | Text | Dropdown | Text |
| Communication channels defined | Dropdown | Text | Dropdown | Text |
| Advance notice requirements | Dropdown | Text | Dropdown | Text |
| Feedback mechanisms | Dropdown | Text | Dropdown | Text |
| Communication effectiveness measured | Dropdown | Text | Dropdown | Text |
| Communication failures tracked | Dropdown | Text | Dropdown | Text |

---

## Sheet 6: Documentation_Record_Keeping

### Purpose
Assess documentation and record-keeping practices for changes.

### Header Section
**Row 1:** "DOCUMENTATION & RECORD KEEPING"  
**Row 2:** "Document what information is captured and retained for changes"

### Change Record Documentation (Rows 4-30)

| Information Element | Captured | System/Location | Retention Period | Status | Evidence |
|---------------------|----------|-----------------|------------------|--------|----------|
| Change request ID | Dropdown: Yes/No | Text | Text | Dropdown: ✅/⚠️/❌ | Text |
| Requestor information | Dropdown | Text | Text | Dropdown | Text |
| Change description | Dropdown | Text | Text | Dropdown | Text |
| Business justification | Dropdown | Text | Text | Dropdown | Text |
| Systems affected | Dropdown | Text | Text | Dropdown | Text |
| Risk assessment | Dropdown | Text | Text | Dropdown | Text |
| Impact assessment | Dropdown | Text | Text | Dropdown | Text |
| Change classification | Dropdown | Text | Text | Dropdown | Text |
| Approval records | Dropdown | Text | Text | Dropdown | Text |
| CAB review notes | Dropdown | Text | Text | Dropdown | Text |
| Implementation plan | Dropdown | Text | Text | Dropdown | Text |
| Test results | Dropdown | Text | Text | Dropdown | Text |
| Rollback plan | Dropdown | Text | Text | Dropdown | Text |
| Communication records | Dropdown | Text | Text | Dropdown | Text |
| Implementation logs | Dropdown | Text | Text | Dropdown | Text |
| Verification results | Dropdown | Text | Text | Dropdown | Text |
| PIR results | Dropdown | Text | Text | Dropdown | Text |
| Lessons learned | Dropdown | Text | Text | Dropdown | Text |
| Change closure date | Dropdown | Text | Text | Dropdown | Text |

### Documentation Update Requirements (Rows 32-45)

| Documentation Type | Updated After Changes | Update Timeframe | Verified | Status | Evidence |
|--------------------|----------------------|------------------|----------|--------|----------|
| System configuration docs | Dropdown: Yes/No/Sometimes | Text (e.g., "5 days") | Dropdown: Yes/No | Dropdown: ✅/⚠️/❌ | Text |
| Network diagrams | Dropdown | Text | Dropdown | Dropdown | Text |
| Application architecture | Dropdown | Text | Dropdown | Dropdown | Text |
| Operational procedures | Dropdown | Text | Dropdown | Dropdown | Text |
| Runbooks | Dropdown | Text | Dropdown | Dropdown | Text |
| Troubleshooting guides | Dropdown | Text | Dropdown | Dropdown | Text |
| User documentation | Dropdown | Text | Dropdown | Dropdown | Text |
| Continuity/DR plans | Dropdown | Text | Dropdown | Dropdown | Text |

### Record Retention Assessment (Rows 47-55)

| Requirement | Implemented | Details | Status | Evidence |
|-------------|-------------|---------|--------|----------|
| Retention policy defined | Dropdown: Yes/No | Text (period) | Dropdown: ✅/⚠️/❌ | Text |
| Retention enforced | Dropdown | Text | Dropdown | Text |
| Records immutable | Dropdown | Text | Dropdown | Text |
| Audit trail complete | Dropdown | Text | Dropdown | Text |
| Records accessible for audit | Dropdown | Text | Dropdown | Text |

---

## Sheet 7: Tool_Capabilities

### Purpose
Inventory change management tools and assess capabilities.

### Header Section
**Row 1:** "CHANGE MANAGEMENT TOOL CAPABILITIES"  
**Row 2:** "Document tools used and their capabilities"

### Tool Inventory (Rows 4-15)

| Tool/System | Vendor/Type | Version | Purpose | User Count | License Status | Status | Notes |
|-------------|-------------|---------|---------|------------|----------------|--------|-------|
| Text (e.g., "ServiceNow") | Text | Text | Text | Text | Text (e.g., "Current") | Dropdown: ✅/⚠️/❌ | Text |
| [Additional tools] | Text | Text | Text | Text | Text | Dropdown | Text |

### Tool Capability Assessment (Rows 17-45)

| Capability | Required | Implemented | Tool/System | Effectiveness | Status | Gap/Notes |
|------------|----------|-------------|-------------|---------------|--------|-----------|
| Change request creation | Dropdown: Yes | Dropdown: Yes/No/Partial | Text | Dropdown: High/Medium/Low | Dropdown: ✅/⚠️/❌ | Text |
| Unique change ID generation | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Workflow automation | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Approval routing | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| CAB scheduling | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Change calendar | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Communication/notifications | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Documentation attachment | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Audit trail/logging | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Reporting/analytics | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Integration with CMDB | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Integration with incident mgmt | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Mobile access | Recommended | Dropdown | Text | Dropdown | Dropdown | Text |
| API availability | Recommended | Dropdown | Text | Dropdown | Dropdown | Text |

### Tool Gaps & Limitations (Rows 47-55)

| Gap/Limitation | Impact | Workaround | Remediation Plan | Target Date | Status |
|----------------|--------|------------|------------------|-------------|--------|
| Text | Dropdown: High/Medium/Low | Text | Text | Date DD.MM.YYYY | Dropdown: ✅/⚠️/❌/📋 |

---

## Sheet 8: Metrics_KPIs

### Purpose
Document change management metrics and performance indicators.

### Header Section
**Row 1:** "CHANGE MANAGEMENT METRICS & KPIs"  
**Row 2:** "Track change process performance and effectiveness"

### Tracked Metrics (Rows 4-25)

| Metric | Tracked | Frequency | Last Period Value | Target | Status | Tool/Method |
|--------|---------|-----------|-------------------|--------|--------|-------------|
| Total changes (all types) | Dropdown: Yes/No | Text (e.g., "Monthly") | Text | Text | Formula: Green/Yellow/Red | Text |
| Standard changes | Dropdown | Text | Text | Text | Formula | Text |
| Normal changes | Dropdown | Text | Text | Text | Formula | Text |
| Emergency changes | Dropdown | Text | Text | Text | Formula | Text |
| Emergency change % | Dropdown | Text | Text (e.g., "8%") | Text (e.g., "<5%") | Formula | Text |
| Change success rate | Dropdown | Text | Text (e.g., "94%") | Text (e.g., ">95%") | Formula | Text |
| Change failure rate | Dropdown | Text | Text | Text | Formula | Text |
| Failed changes causing incidents | Dropdown | Text | Text | Text | Formula | Text |
| Average change duration | Dropdown | Text | Text | Text | Formula | Text |
| Changes exceeding window | Dropdown | Text | Text | Text | Formula | Text |
| Rollback rate | Dropdown | Text | Text | Text | Formula | Text |
| PIR completion rate | Dropdown | Text | Text (e.g., "78%") | Text (e.g., ">90%") | Formula | Text |
| CAB attendance rate | Dropdown | Text | Text | Text | Formula | Text |
| Changes per system/app | Dropdown | Text | Text | Text | Formula | Text |
| Change backlog | Dropdown | Text | Text | Text | Formula | Text |
| Unauthorized changes detected | Dropdown | Text | Text | Text | Formula | Text |

### KPI Reporting (Rows 27-35)

| Report | Frequency | Recipients | Reviewed By | Action Taken | Status | Evidence |
|--------|-----------|------------|-------------|--------------|--------|----------|
| Change volume report | Text | Text | Text | Text | Dropdown: ✅/⚠️/❌ | Text |
| Change success/failure report | Text | Text | Text | Text | Dropdown | Text |
| Emergency change analysis | Text | Text | Text | Text | Dropdown | Text |
| Trend analysis | Text | Text | Text | Text | Dropdown | Text |
| Executive dashboard | Text | Text | Text | Text | Dropdown | Text |

---

## Sheet 9: Evidence_Register

### Purpose
Centralized evidence repository linking to all supporting documentation.

### Header Section
**Row 1:** "EVIDENCE REGISTER"  
**Row 2:** "Document evidence location for all assessed requirements"

### Evidence Inventory (Rows 4-100)

| Requirement ID | Requirement Description | Evidence Type | Evidence Location | Last Verified | Accessible To | Status | Notes |
|----------------|------------------------|---------------|-------------------|---------------|---------------|--------|-------|
| REQ-PROCESS-001 | Change request procedures | Text (e.g., "Policy Document") | Text (path/URL) | Date DD.MM.YYYY | Text (role) | Dropdown: ✅/⚠️/❌ | Text |
| REQ-PROCESS-002 | Risk assessment | Text | Text | Date | Text | Dropdown | Text |
| [Continue for all requirements] | Text | Text | Text | Date | Text | Dropdown | Text |

**Column Widths:**

- A: 18, B: 35, C: 20, D: 35, E: 15, F: 20, G: 12, H: 25


---

## Sheet 10: Summary_Dashboard

### Purpose
Executive summary with compliance scoring and audit readiness.

### Header Section
**Row 1:** "CHANGE PROCESS ASSESSMENT - SUMMARY DASHBOARD"  
**Row 2:** "Overall compliance status and key findings"  
**Row 3:** Date and organization info (formulas from Instructions sheet)

### Overall Compliance (Rows 5-12)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **Overall Compliance %** | Formula: AVG(all status columns) | 90% | Formula: Color-coded cell |
| Requirements Assessed | Formula: COUNT | N/A | Auto |
| Fully Compliant (✅) | Formula: COUNTIF | N/A | Auto |
| Partially Compliant (⚠️) | Formula: COUNTIF | N/A | Auto |
| Non-Compliant (❌) | Formula: COUNTIF | N/A | Auto |
| Planned (📋) | Formula: COUNTIF | N/A | Auto |

### Compliance by Domain (Rows 14-24)

| Domain | Requirements | Compliant | Partial | Non-Compliant | Compliance % | Status |
|--------|--------------|-----------|---------|---------------|--------------|--------|
| Change Process Workflow | Formula: COUNT | Formula | Formula | Formula | Formula | Color cell |
| Approval Authority | Formula | Formula | Formula | Formula | Formula | Color cell |
| CAB Operations | Formula | Formula | Formula | Formula | Formula | Color cell |
| Communication | Formula | Formula | Formula | Formula | Formula | Color cell |
| Documentation | Formula | Formula | Formula | Formula | Formula | Color cell |
| Tool Capabilities | Formula | Formula | Formula | Formula | Formula | Color cell |
| Metrics & KPIs | Formula | Formula | Formula | Formula | Formula | Color cell |

### Critical Findings (Rows 26-35)

**Section Header (RED):** "CRITICAL GAPS REQUIRING IMMEDIATE ATTENTION"

| Domain | Finding | Severity | Assigned To | Target Date | Status |
|--------|---------|----------|-------------|-------------|--------|
| Auto-populate from sheets | Text | Critical/High/Medium | Text | Date DD.MM.YYYY | Dropdown: ✅/⚠️/❌/📋 |

### Audit Readiness (Rows 37-45)

| Criterion | Status | Notes |
|-----------|--------|-------|
| All processes documented | Formula | Text |
| Evidence complete | Formula | Text |
| Roles defined | Formula | Text |
| Tools adequate | Formula | Text |
| Metrics tracked | Formula | Text |
| Compliance ≥70% | Formula | Text |
| **OVERALL AUDIT READY** | Formula: Yes/No/Conditional | Text |

**Column Widths:**

- A: 35, B: 15, C: 25


---

## Sheet 11: Approval_Sign_Off

### Purpose
Final approval and sign-off for assessment.

### Header Section
**Row 1:** "ASSESSMENT APPROVAL & SIGN-OFF"  
**Row 2:** "Formal approval of completed assessment"

### Assessment Metadata (Rows 4-12)

| Attribute | Value |
|-------|-------|
| Assessment Completion Date | Date picker (yellow cell) |
| Overall Compliance | Formula from Summary_Dashboard |
| Critical Gaps Count | Formula from Summary_Dashboard |
| Assessment Status | Dropdown: Draft / Under Review / Final / Rejected |
| Next Review Date | Date picker (yellow cell) |

### Approvals (Rows 14-25)

| Role | Name | Signature/Approval | Date | Comments |
|------|------|-------------------|------|----------|
| Assessment Owner (Change Manager) | Text | Dropdown: Approved/Rejected | Date picker | Text |
| CAB Chair | Text | Dropdown | Date picker | Text |
| Compliance Officer | Text | Dropdown | Date picker | Text |
| CISO | Text | Dropdown | Date picker | Text |

### Conditional Approval (if applicable) (Rows 27-30)

| Condition | Responsibility | Target Date | Status |
|-----------|---------------|-------------|--------|
| Text | Text | Date | Dropdown: ✅/⚠️/❌/📋 |

---

## Appendix: Technical Notes for Developers

### Formula Patterns

**Status Column Formulas:**
```excel
=IF(C5="Yes","✅",IF(C5="Partial","⚠️",IF(C5="No","❌","N/A")))
```

**Compliance Percentage:**
```excel
=COUNTIF(StatusRange,"✅")/(COUNTA(StatusRange)-COUNTIF(StatusRange,"N/A"))*100
```

**Conditional Formatting Rules:**

- Green (C6EFCE): Cell value = "✅"
- Yellow (FFEB9C): Cell value = "⚠️"  
- Red (FFC7CE): Cell value = "❌"
- Blue (B4C7E7): Cell value = "📋"
- Gray: Cell value = "N/A"


### Data Validation

**Status Dropdowns:**
```
List: ✅,⚠️,❌,📋,N/A
```

**Yes/No/Partial Dropdowns:**
```
List: Yes,No,Partial,N/A
```

**Severity Levels:**
```
List: Critical,High,Medium,Low
```

### Cell Protection

- **Protected:** All formula cells, headers, instructions
- **Unprotected:** Yellow input cells, text entry areas, status dropdowns
- **Sheet Protection Password:** [Organization-defined]


---

**END OF SPECIFICATION**

---

*"The enemy knows the system. Security through obscurity is not security at all."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-01-31 -->
