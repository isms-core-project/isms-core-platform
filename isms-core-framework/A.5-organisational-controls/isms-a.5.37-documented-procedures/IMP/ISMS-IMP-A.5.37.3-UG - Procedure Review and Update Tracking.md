<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.37.3-UG:framework:UG:a.5.37.3 -->
**ISMS-IMP-A.5.37.3-UG - Procedure Review and Update Tracking**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.37: Documented Operating Procedures

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.3-UG |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.37: Documented Operating Procedures |
| **Parent Policy** | ISMS-POL-A.5.37 Documented Operating Procedures Policy |
| **Related IMPs** | ISMS-IMP-A.5.37.1, ISMS-IMP-A.5.37.2, ISMS-IMP-A.5.37.4 |
| **Version** | 1.0 |
| **Classification** | Internal Use |
| **Owner** | Information Security Manager |
| **Last Review** | [Date to be set] |
| **Framework Version** | 1.0 |
| **Assessment Type** | Periodic Review and Change Management |

---

## Control Requirement

> "Operating procedures for information processing facilities should be documented and made available to personnel who need them."
>
> — ISO/IEC 27001:2022, Annex A Control 5.37

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.37.3-TG.

---

## Assessment Overview

### Purpose

The Procedure Review and Update Tracking workbook manages the complete lifecycle of procedure maintenance, from scheduled reviews through change implementation and communication. Procedures are living documents that require systematic review to remain accurate, relevant, and aligned with current systems and processes.

This assessment tracks:
- **Scheduled Reviews**: Periodic reviews based on procedure criticality
- **Triggered Reviews**: Event-driven reviews (incidents, system changes, regulatory updates)
- **Change Requests**: Formal requests to modify procedure content
- **Version Management**: Historical tracking of procedure evolution
- **Communication**: Distribution and acknowledgement of updates
- **Escalations**: Management of overdue reviews and blocked changes

### Scope

This workbook covers:
- All procedures documented in the Procedure Inventory (ISMS-IMP-A.5.37.1)
- Scheduled and ad-hoc review processes
- Change request lifecycle management
- Version control and history tracking
- Update communication and acknowledgement
- Escalation of overdue or blocked items

### Benefits

| Stakeholder | Benefit |
|-------------|---------|
| **ISM** | Complete visibility into procedure currency and change activity |
| **Procedure Owners** | Clear review schedules and change request workflow |
| **Management** | Assurance that procedures remain current and accurate |
| **Auditors** | Evidence of systematic review and change control |
| **Personnel** | Access to current, accurate operating procedures |

### Assessment Frequency

| Activity | Frequency |
|----------|-----------|
| Review schedule monitoring | Weekly |
| Change request processing | As submitted |
| Escalation review | Weekly |
| Dashboard refresh | Weekly |
| Trend analysis | Monthly |
| Full assessment cycle | Quarterly |

---

## Control Requirements

### ISO 27001:2022 A.5.37 Requirements for Review

The control requirement for documented operating procedures includes implicit requirements for maintaining procedure currency:

| Requirement Aspect | Assessment Focus |
|--------------------|------------------|
| **Documentation Currency** | Procedures reflect current systems and processes |
| **Accuracy** | Content matches actual operational practices |
| **Relevance** | Procedures address current threats and requirements |
| **Accessibility** | Updated versions available to personnel who need them |
| **Version Control** | Clear identification of current authoritative version |

### ISO 27002:2022 Implementation Guidance

ISO 27002 provides guidance on maintaining documented procedures:

| Guidance Element | Implementation Approach |
|------------------|------------------------|
| **Regular Review** | Scheduled review cycles based on criticality |
| **Change Triggers** | Event-driven reviews for system changes, incidents |
| **Approval Process** | Formal approval before changes become effective |
| **Communication** | Personnel informed of significant changes |
| **Version Management** | Clear version numbering and history |

### Review Trigger Matrix

| Trigger Category | Trigger Event | Review Type | Timeframe |
|------------------|---------------|-------------|-----------|
| **Scheduled** | Review cycle reached | Full review | Per cycle |
| **System** | Technology change | Targeted review | 30 days from change |
| **System** | Configuration change | Targeted review | 30 days from change |
| **System** | Tool replacement | Full review | 30 days from go-live |
| **Incident** | Procedure failure | Root cause review | 14 days from incident |
| **Incident** | Near-miss event | Gap review | 14 days from event |
| **Regulatory** | Law/regulation change | Compliance review | 60 days from effective |
| **Regulatory** | Standard update | Alignment review | 60 days from publication |
| **Audit** | Finding identified | Corrective review | Per CAR timeline |
| **Personnel** | Owner departure | Owner verification | 30 days from notice |
| **Personnel** | Responsibility transfer | Handover review | 30 days from transfer |
| **Organisational** | Restructure | Scope review | 60 days from change |

---

## Prerequisites

### Required Inputs

Before starting the Review and Update Tracking assessment, ensure you have:

| Prerequisite | Source | Purpose |
|--------------|--------|---------|
| **Procedure Inventory** | ISMS-IMP-A.5.37.1 | Complete list of procedures to track |
| **Quality Assessment** | ISMS-IMP-A.5.37.2 | Current quality scores and gaps |
| **Change Management Policy** | Organisational policy | Approval authority matrix |
| **Review Schedule** | Previous assessments | Historical review dates |
| **Incident Register** | Incident management system | Incident-triggered reviews |
| **Change Calendar** | IT change management | System changes requiring review |
| **Regulatory Updates** | Legal/compliance | Regulatory changes affecting procedures |

### Access Requirements

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| **Document Repository** | Read/Write | Access procedure documents |
| **Procedure Inventory Workbook** | Read | Reference procedure details |
| **Quality Assessment Workbook** | Read | Reference quality scores |
| **Change Management System** | Create/Update | Log change requests |
| **Communication System** | Send | Distribute update notifications |
| **Training System** | Read/Update | Track training requirements |

### Stakeholder Contacts

Identify and confirm availability of:

| Role | Responsibility | Contact Required |
|------|----------------|------------------|
| **Procedure Owners** | Review and approve changes | Before review deadlines |
| **Technical SMEs** | Validate technical accuracy | For system changes |
| **Compliance Officer** | Validate regulatory alignment | For regulatory changes |
| **Training Coordinator** | Coordinate training updates | For major changes |
| **IT Change Manager** | Coordinate with IT changes | For system-driven changes |

---

## Review Triggers and Cycles

### Review Cycle by Criticality

| Criticality | Review Cycle | Rationale | Example Procedures |
|-------------|:------------:|-----------|-------------------|
| **Critical** | 6 months | High-impact procedures with severe consequences if outdated | Incident response, disaster recovery, emergency shutdown |
| **High** | 12 months | Significant operational procedures | Backup operations, access provisioning, security monitoring |
| **Medium** | 12 months | Standard operational procedures | User onboarding, equipment maintenance, documentation updates |
| **Low** | 24 months | Stable procedures with infrequent changes | Office procedures, archive management |

### Mandatory Review Triggers

| Trigger | Review Scope | Timeframe | Escalation If Missed |
|---------|--------------|-----------|----------------------|
| **Scheduled Review** | Full procedure review | Per criticality cycle | L1 at due date, L2 at +14 days |
| **System Change** | Affected sections | Within 30 days of change | L1 immediately, L2 at +7 days |
| **Incident Related** | Root cause sections | Within 14 days of incident | L2 immediately (incident-related) |
| **Regulatory Change** | Compliance sections | Within 60 days of effective date | L1 at 30 days, L2 at 45 days |
| **Audit Finding** | Finding-related sections | Per CAR timeline | L2 if CAR at risk |
| **Personnel Change** | Owner verification | Within 30 days of notice | L1 at 14 days |

### Review Outcomes

| Outcome | Definition | Actions Required |
|---------|------------|------------------|
| **Current - No Changes** | Procedure accurately reflects current practice | Update review date, document confirmation |
| **Minor Updates** | Clarifications, corrections, formatting | Apply changes, increment minor version (X.Y+1) |
| **Major Updates** | Process changes, new steps, structural changes | Full rewrite, increment major version (X+1.0), re-approval required |
| **Obsolete** | Procedure no longer applicable | Archive procedure, remove from active use |
| **Superseded** | Replaced by new procedure | Link to replacement, archive old version |
| **Merge** | Combined with another procedure | Archive original, update combined procedure |

---

## Change Management Framework

### Change Categories

| Category | Description | Examples | Approval Authority |
|----------|-------------|----------|-------------------|
| **Administrative** | No content impact | Typos, formatting, contact updates, reference corrections | Procedure Owner (same day) |
| **Minor** | Clarification without process change | Step clarifications, additional notes, updated screenshots | Procedure Owner + Reviewer (within 5 days) |
| **Major** | Process or content change | New steps, changed sequence, tool changes, scope changes | Management Approval (within 14 days) |
| **Emergency** | Urgent operational necessity | Immediate safety/security requirements | Expedited approval + retrospective review (within 24 hours) |

### Change Request Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│                     CHANGE REQUEST WORKFLOW                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. INITIATE                 2. ASSESS                              │
│  ┌──────────────┐           ┌──────────────┐                        │
│  │ Submit CR    │ ───────── │ Categorise   │                        │
│  │ Document     │           │ Assess Impact│                        │
│  └──────────────┘           └──────────────┘                        │
│         │                          │                                │
│         ▼                          ▼                                │
│  3. DRAFT                   4. REVIEW                               │
│  ┌──────────────┐           ┌──────────────┐                        │
│  │ Prepare      │ ───────── │ Technical    │                        │
│  │ Changes      │           │ Peer Review  │                        │
│  └──────────────┘           └──────────────┘                        │
│         │                          │                                │
│         ▼                          ▼                                │
│  5. APPROVE                 6. PUBLISH                              │
│  ┌──────────────┐           ┌──────────────┐                        │
│  │ Per Matrix   │ ───────── │ Update Repo  │                        │
│  │ Sign-off     │           │ Version Ctrl │                        │
│  └──────────────┘           └──────────────┘                        │
│         │                          │                                │
│         ▼                          ▼                                │
│  7. COMMUNICATE             8. VERIFY                               │
│  ┌──────────────┐           ┌──────────────┐                        │
│  │ Notify Users │ ───────── │ Confirm      │                        │
│  │ Training     │           │ Accessibility│                        │
│  └──────────────┘           └──────────────┘                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Impact Assessment Checklist

For each change request, assess:

| Impact Area | Assessment Questions |
|-------------|---------------------|
| **Training** | Do personnel need training on the change? How many affected? |
| **Systems** | Does the change require system modifications? |
| **Compliance** | Does the change affect regulatory compliance? |
| **Dependencies** | Are other procedures affected by this change? |
| **Resources** | What resources are needed to implement the change? |
| **Risk** | What risks arise from making (or not making) the change? |
| **Timeline** | When must the change be effective? Any constraints? |

---

## Completion Walkthrough

### Step 1: Initialise Review Schedule (Sheet 1)

**Objective:** Establish the review schedule for all procedures

**Actions:**
1. Import procedure list from A.5.37.1 Inventory
2. Populate criticality from inventory
3. Set review cycle based on criticality matrix
4. Calculate next review date from last review
5. Assign reviewers for upcoming reviews

**Data to Capture:**

| Field | Source | Action |
|-------|--------|--------|
| Procedure_ID | Inventory | Import |
| Procedure_Name | Inventory | Lookup |
| Criticality | Inventory | Lookup |
| Review_Cycle_Days | Criticality matrix | Calculate |
| Last_Review_Date | Previous assessment | Enter/verify |
| Next_Review_Due | Formula | Automatic |
| Assigned_Reviewer | Assignment | Enter |

**Verification:**
- [ ] All procedures from inventory are listed
- [ ] Review cycles match criticality matrix
- [ ] Next review dates are calculated correctly
- [ ] Reviewers assigned for reviews due within 30 days

### Step 2: Process Change Requests (Sheet 2)

**Objective:** Log and track all procedure change requests

**Actions:**
1. Log incoming change requests with unique CR ID
2. Categorise change (Administrative/Minor/Major/Emergency)
3. Identify trigger (Scheduled/System/Incident/Regulatory/Audit/Personnel)
4. Complete impact assessment
5. Route for appropriate approval
6. Track through implementation

**Change Request ID Format:**
```
CR-YYYYMM-NNN
Example: CR-202602-001
```

**Required Information per CR:**

| Phase | Required Fields |
|-------|-----------------|
| **Submission** | Procedure_ID, Requestor, Description, Justification |
| **Assessment** | Category, Trigger, Impact_Assessment |
| **Approval** | Approver, Approval_Date (or Rejection reason) |
| **Implementation** | Implementation_Date, Verification |

### Step 3: Maintain Version History (Sheet 3)

**Objective:** Track all procedure versions

**Actions:**
1. Record each new version when changes are implemented
2. Link to change request that drove the change
3. Document change summary
4. Record approval and effective date
5. Update status of superseded versions

**Version Numbering Convention:**

| Change Type | Version Change | Example |
|-------------|----------------|---------|
| Major update | X.0 → (X+1).0 | 1.0 → 2.0 |
| Minor update | X.Y → X.(Y+1) | 1.2 → 1.3 |
| Administrative | No change | 1.2 → 1.2 (note in log) |

### Step 4: Log Communications (Sheet 4)

**Objective:** Track procedure update communications

**Actions:**
1. Record each communication about procedure updates
2. Track communication method and audience
3. Monitor acknowledgement rates where required
4. Track training completion for major changes

**Communication Methods:**

| Method | Use Case | Acknowledgement |
|--------|----------|-----------------|
| Email | General notifications | Optional |
| Intranet | Broad awareness | No |
| Meeting | Team-specific updates | Attendance record |
| Training | Major changes | Completion required |
| Alert/Banner | Critical updates | Confirmation click |

### Step 5: Manage Escalations (Sheet 5)

**Objective:** Handle overdue reviews and blocked changes

**Actions:**
1. Identify overdue items automatically
2. Apply escalation matrix
3. Track escalation communications
4. Document resolution

### Step 6: Link Evidence (Sheet 6)

**Objective:** Maintain evidence trail for audit

**Actions:**
1. Link review records to evidence
2. Link approval emails/documents
3. Link communication records
4. Link training records where applicable

### Step 7: Calculate Metrics (Sheet 7)

**Objective:** Generate KPIs for dashboard

**Actions:**
1. Calculate review on-time rate
2. Calculate CR cycle times
3. Calculate acknowledgement rates
4. Populate trend data

---

## Escalation Management

### Escalation Matrix

| Condition | Level | Escalate To | Timeframe | Required Action |
|-----------|:-----:|-------------|-----------|-----------------|
| Review 1-14 days overdue | L1 | Procedure Owner + Line Manager | Immediately | Schedule review within 7 days |
| Review 15-30 days overdue | L2 | Department Head + ISM | At day 15 | Mandatory review within 14 days |
| Review >30 days overdue | L3 | CISO + Executive Management | At day 31 | Executive intervention, risk acceptance or immediate action |
| CR blocked >14 days | L1 | Approver + ISM | At day 14 | Identify blocker, resolve or escalate |
| CR blocked >30 days | L2 | Management | At day 30 | Management decision required |
| Emergency CR pending >24h | L2 | CISO | At 24 hours | Emergency approval process |

### Escalation Response Requirements

| Level | Response SLA | Resolution SLA |
|:-----:|--------------|----------------|
| L1 | Acknowledge within 2 business days | Resolve within 7 business days |
| L2 | Acknowledge within 1 business day | Resolve within 5 business days |
| L3 | Acknowledge same business day | Executive decision within 2 business days |

### Risk Acceptance for Overdue Reviews

When a procedure review cannot be completed within the extended escalation timeframe:

1. **Document the Risk**: Formally record why the review is delayed
2. **Compensating Controls**: Identify temporary measures in place
3. **Risk Acceptance**: Obtain signed risk acceptance from appropriate authority
4. **Remediation Plan**: Define specific date for review completion
5. **Monitoring**: Increased monitoring of procedure usage until reviewed

---

## Communication Requirements

### Notification Matrix

| Change Type | Notification Scope | Method | Timing | Acknowledgement |
|-------------|-------------------|--------|--------|-----------------|
| Administrative | None required | - | - | No |
| Minor | Direct users | Email | Within 5 days of publication | Optional |
| Major | All users | Email + Intranet | Before effective date | Required |
| Emergency | Affected users | Alert/Immediate | Immediately | Confirmation required |

### Communication Content Requirements

| Change Type | Required Content |
|-------------|------------------|
| **Minor** | Procedure name, version, summary of changes, effective date, link to procedure |
| **Major** | Procedure name, version, detailed changes, rationale, effective date, training requirements, link to procedure |
| **Emergency** | URGENT flag, immediate actions required, procedure link, escalation contact |

### Training Requirements

| Change Impact | Training Requirement |
|---------------|---------------------|
| Cosmetic/formatting | None |
| Step clarification | Awareness (read procedure) |
| New step added | Awareness + demonstration |
| Process change | Formal training session |
| Tool/system change | Hands-on training |

---

## Evidence Collection

### Evidence Requirements by Activity

| Activity | Required Evidence | Retention |
|----------|-------------------|-----------|
| **Scheduled Review** | Review record, reviewer sign-off, outcome documentation | 3 years |
| **Change Request** | CR form, impact assessment, approvals, implementation record | 3 years |
| **Version Change** | Before/after versions, change log, approval | Permanent |
| **Communication** | Notification copy, distribution list, acknowledgement records | 3 years |
| **Training** | Attendance/completion records, materials | 3 years |
| **Escalation** | Escalation notices, responses, resolution records | 3 years |

### Evidence Storage

| Evidence Type | Storage Location | Naming Convention |
|---------------|------------------|-------------------|
| Review records | ISMS Evidence Library/A.5.37/Reviews/ | PROC-ID_Review_YYYYMMDD |
| Change requests | ISMS Evidence Library/A.5.37/Changes/ | CR-YYYYMM-NNN_[Description] |
| Approvals | ISMS Evidence Library/A.5.37/Approvals/ | PROC-ID_v[X.Y]_Approval |
| Communications | ISMS Evidence Library/A.5.37/Communications/ | PROC-ID_Comm_YYYYMMDD |
| Training records | Training System + backup copy | PROC-ID_Training_YYYYMMDD |

### Evidence Quality Standards

| Standard | Requirement |
|----------|-------------|
| **Completeness** | All required fields populated |
| **Authenticity** | Clear identification of author/approver |
| **Integrity** | Protected from unauthorised modification |
| **Accessibility** | Retrievable within 24 hours for audit |
| **Readability** | Clear, legible, properly formatted |

---

## Common Pitfalls

### Procedure Review Pitfalls

❌ **MISTAKE:** Treating reviews as a rubber-stamp exercise without actually reading the procedure
✅ **CORRECT:** Conduct thorough reviews comparing procedure content to actual current practice

❌ **MISTAKE:** Skipping reviews because "nothing has changed"
✅ **CORRECT:** Document formal review confirmation even when no changes are needed—this is evidence of currency validation

❌ **MISTAKE:** Only reviewing the procedure document without consulting practitioners
✅ **CORRECT:** Involve personnel who execute the procedure to validate accuracy

❌ **MISTAKE:** Allowing review backlogs to accumulate without escalation
✅ **CORRECT:** Apply escalation matrix promptly when reviews become overdue

❌ **MISTAKE:** Updating procedures without formal change request
✅ **CORRECT:** All changes, even minor ones, should be logged for audit trail

### Change Management Pitfalls

❌ **MISTAKE:** Categorising all changes as "Administrative" to avoid approval
✅ **CORRECT:** Honestly assess change impact; minor process changes are "Minor" not "Administrative"

❌ **MISTAKE:** Implementing changes before approval is complete
✅ **CORRECT:** Wait for formal approval except for documented emergency procedures

❌ **MISTAKE:** Emergency changes bypassing retrospective review
✅ **CORRECT:** Emergency changes require expedited approval AND retrospective formal review within 7 days

❌ **MISTAKE:** Not assessing impact on related procedures
✅ **CORRECT:** Check dependencies—a change to one procedure may require updates to others

❌ **MISTAKE:** Incomplete impact assessments that miss training requirements
✅ **CORRECT:** Explicitly assess training needs for every change request

### Version Control Pitfalls

❌ **MISTAKE:** Inconsistent version numbering across procedures
✅ **CORRECT:** Apply standard version numbering convention consistently

❌ **MISTAKE:** Not updating version in all document locations (header, footer, metadata)
✅ **CORRECT:** Version number should appear in document header, footer, properties, and repository

❌ **MISTAKE:** Overwriting previous versions without archiving
✅ **CORRECT:** Maintain complete version history; archive superseded versions, don't delete

❌ **MISTAKE:** Version history that doesn't explain what changed
✅ **CORRECT:** Change summaries should clearly describe what changed and why

### Communication Pitfalls

❌ **MISTAKE:** Publishing updates without notification to users
✅ **CORRECT:** All significant updates require communication per the notification matrix

❌ **MISTAKE:** Assuming email delivery equals user awareness
✅ **CORRECT:** For major changes, require acknowledgement and verify understanding

❌ **MISTAKE:** Not tracking training completion for major changes
✅ **CORRECT:** Training completion should be tracked and verified before personnel resume duties

❌ **MISTAKE:** Communicating changes in technical jargon users don't understand
✅ **CORRECT:** Communications should be clear and accessible to the target audience

---

## Quality Checklist

### Pre-Submission Checklist

#### Review Schedule Management
- [ ] All procedures from inventory are included in review schedule
- [ ] Review cycles correctly calculated based on criticality
- [ ] Next review dates are accurate
- [ ] Reviewers assigned for upcoming reviews (within 30 days)
- [ ] Overdue reviews identified and escalated

#### Change Request Management
- [ ] All change requests have unique CR IDs
- [ ] Category (Administrative/Minor/Major/Emergency) correctly assigned
- [ ] Trigger type documented
- [ ] Impact assessment completed for all non-Administrative changes
- [ ] Approval workflow followed per change category
- [ ] Implementation verified and documented

#### Version Control
- [ ] Version numbers follow standard convention
- [ ] All versions linked to originating change request
- [ ] Change summaries are clear and complete
- [ ] Superseded versions marked and archived
- [ ] Current version clearly identifiable

#### Communication
- [ ] Notifications sent per communication matrix
- [ ] Acknowledgements tracked where required
- [ ] Training requirements identified and tracked
- [ ] Communication records preserved

#### Evidence
- [ ] All review records captured
- [ ] Approval evidence preserved
- [ ] Communication records filed
- [ ] Training records available
- [ ] Evidence accessible for audit

### Quality Metrics Targets

| Metric | Target | Measurement |
|--------|--------|-------------|
| Reviews completed on time | ≥95% | Reviews completed by due date / Total reviews due |
| CR cycle time (Minor) | ≤5 business days | Average days from submission to implementation |
| CR cycle time (Major) | ≤14 business days | Average days from submission to implementation |
| Communication acknowledgement | ≥90% | Acknowledgements received / Required acknowledgements |
| Training completion | 100% | Personnel trained / Personnel requiring training |
| Zero overdue reviews >30 days | 0 | Count of L3 escalations |

---

## Review and Approval

### Assessment Review Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                  ASSESSMENT APPROVAL WORKFLOW                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────────┐   │
│  │ Assessor     │      │ ISM Review   │      │ Management   │   │
│  │ Completes    │─────▶│ Validation   │─────▶│ Approval     │   │
│  │ Workbook     │      │ & QA Check   │      │ (if required)│   │
│  └──────────────┘      └──────────────┘      └──────────────┘   │
│        │                      │                      │          │
│        ▼                      ▼                      ▼          │
│  Evidence              Findings             Final Sign-off      │
│  Collected             Documented           Recorded            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Approval Authorities

| Assessment Component | Reviewer | Approver |
|---------------------|----------|----------|
| Review Schedule | Procedure Owners | ISM |
| Change Requests (Admin) | Procedure Owner | Procedure Owner |
| Change Requests (Minor) | Peer Reviewer | Procedure Owner |
| Change Requests (Major) | ISM | Department Head / CISO |
| Emergency Changes | CISO | CISO + Retrospective |
| Escalation Resolution | Department Head | CISO |
| Quarterly Assessment | Compliance Officer | ISM |

### Sign-off Record

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Assessor | | | |
| ISM Review | | | |
| Management Approval | | | |

---

## Related Controls

### Primary Dependencies

| Control | Relationship | Integration |
|---------|--------------|-------------|
| **A.5.37.1** | Procedure Inventory | Source of procedures to track |
| **A.5.37.2** | Quality Assessment | Quality triggers review |
| **A.5.37.4** | Compliance Dashboard | Consumes metrics |
| **A.5.1** | Information Security Policy | Policy framework for procedures |
| **A.8.32** | Change Management | Aligns with IT change processes |

### Related Controls

| Control | Relevance |
|---------|-----------|
| **A.5.24-28** | Incident Management | Incidents trigger procedure reviews |
| **A.5.35** | Independent Review | Audit findings trigger reviews |
| **A.7.2** | Information Classification | Procedure classification affects handling |
| **A.6.3** | Information Security Awareness | Training on procedure changes |

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
