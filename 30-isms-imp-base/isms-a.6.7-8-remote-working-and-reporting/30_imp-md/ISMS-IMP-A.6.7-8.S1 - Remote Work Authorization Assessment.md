**ISMS-IMP-A.6.7-8.S1 - Remote Work Authorization Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S1 |
| **Version** | 1.0 |
| **Assessment Area** | Remote Work Authorization, Policy Framework, and Governance |
| **Related Policy** | ISMS-POL-A.6.7-8, Section 2.1 (Remote Work Authorization) |
| **Purpose** | Guide users through systematic assessment of remote work authorization processes |
| **Target Audience** | IT Security Team, HR Representatives, Line Managers, Auditors |
| **Assessment Type** | Policy & Operational |
| **Review Cycle** | Annual |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for remote work authorization assessment | ISMS Implementation Team |

---

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Sheet-by-Sheet Guidance
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formula Specifications
  - Styling Reference

**Target Audiences:**

- **Part I:** Assessment users (IT Security Team, HR Representatives, Line Managers)
- **Part II:** Workbook developers (Python/Excel script maintainers)

---

# PART I: USER COMPLETION GUIDE

**Audience:** IT Security Team, HR Representatives, Line Managers, Compliance Officers

---

## 1. Assessment Overview

#### 1.1 Purpose

This assessment workbook evaluates [Organization]'s remote work authorization framework, ensuring that:
- Formal authorization processes exist for remote work arrangements
- Authorization criteria are defined and consistently applied
- Risk assessments are performed for high-risk remote work scenarios
- Documentation requirements are met
- Periodic reviews maintain authorization currency

#### 1.2 Scope

This assessment covers:
- Remote work policy framework and governance
- Authorization request and approval workflows
- Risk assessment procedures for remote work
- Documentation and record-keeping
- Periodic review and re-authorization processes
- Integration with HR joiner/mover/leaver processes

#### 1.3 Target Audience

- **Primary Assessors**: IT Security Team, HR Representatives
- **Data Contributors**: Line Managers, IT Operations
- **Reviewers**: CISO, HR Director
- **Approvers**: CISO, Executive Management

#### 1.4 Assessment Frequency

| Trigger | Frequency |
|---------|-----------|
| Initial Assessment | Once (ISMS implementation) |
| Periodic Review | Annual |
| Triggered Review | After significant policy changes, security incidents, or organizational restructuring |

### 2. Prerequisites

Before starting this assessment, ensure:

| Prerequisite | Status | Notes |
|--------------|--------|-------|
| ISMS-POL-A.6.7-8 approved and published | ☐ | Policy must be finalized |
| Remote work authorization procedure documented | ☐ | Or gap identified |
| Access to HR records for remote work approvals | ☐ | Sample selection |
| Access to IT access provisioning records | ☐ | VPN/remote access grants |
| List of personnel currently working remotely | ☐ | From HR/IT systems |

### 3. Assessment Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: Policy Framework Review                              │
│  - Review remote work policy documentation                      │
│  - Verify approval and publication                              │
│  - Check communication to personnel                             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 2: Authorization Process Assessment                      │
│  - Document authorization workflow                              │
│  - Verify approval authorities                                  │
│  - Check criteria documentation                                 │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 3: Sample Testing                                        │
│  - Select sample of remote work authorizations                  │
│  - Verify proper approval obtained                              │
│  - Check documentation completeness                             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 4: Gap Analysis & Evidence Collection                    │
│  - Document gaps identified                                     │
│  - Collect supporting evidence                                  │
│  - Prepare remediation recommendations                          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 5: Review & Approval                                     │
│  - Technical review by IT Security                              │
│  - Management review by CISO                                    │
│  - Sign-off and next steps                                      │
└─────────────────────────────────────────────────────────────────┘
```

### 4. Sheet-by-Sheet Completion Guide

#### 4.1 Instructions Sheet

**Purpose**: Provides guidance for workbook users.

**Actions**:
- Review the instructions before starting
- Note the version and assessment date
- Identify your role (Assessor, Reviewer, Approver)

#### 4.2 Policy_Framework Sheet

**Purpose**: Assess the existence and quality of remote work policy documentation.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Policy Element | Specific policy component being assessed | Pre-populated |
| Requirement | What the element should contain | Pre-populated |
| Status | Current state (Exists/Partial/Missing) | Dropdown |
| Evidence Reference | Document ID or location | Free text |
| Gap Description | If not compliant, describe the gap | Free text |
| Remediation | Recommended action to address gap | Free text |
| Priority | Remediation priority (High/Medium/Low) | Dropdown |

**Completion Steps**:
1. Review each policy element listed
2. Locate the corresponding documentation
3. Assess whether the requirement is met
4. Record evidence reference
5. Document any gaps and remediation needs

#### 4.3 Authorization_Process Sheet

**Purpose**: Document and assess the remote work authorization workflow.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Process Step | Step in the authorization workflow | Pre-populated |
| Description | What should happen at this step | Pre-populated |
| Implemented | Is this step implemented? (Yes/No/Partial) | Dropdown |
| Owner | Role responsible for this step | Free text |
| Documentation | Where is this step documented? | Free text |
| Evidence | Evidence of implementation | Free text |
| Notes | Additional observations | Free text |

**Completion Steps**:
1. Walk through each process step
2. Interview process owners if needed
3. Verify implementation through evidence
4. Document the responsible owner
5. Note any deviations from expected process

#### 4.4 Authorization_Criteria Sheet

**Purpose**: Verify that authorization criteria are defined and appropriate.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Criterion Category | Type of authorization criterion | Pre-populated |
| Criterion | Specific criterion to evaluate | Pre-populated |
| Defined | Is this criterion formally defined? | Dropdown |
| Applied | Is it consistently applied? | Dropdown |
| Evidence | Evidence of definition/application | Free text |
| Gap | Any gaps identified | Free text |

**Key Criteria to Assess**:
- Role suitability for remote work
- Data classification considerations
- Technical capability requirements
- Physical environment requirements
- Regulatory/contractual restrictions
- Business continuity needs

#### 4.5 Sample_Testing Sheet

**Purpose**: Test a sample of actual remote work authorizations for compliance.

**Sample Selection**:
- Minimum 10% of remote workers or 20 personnel (whichever is greater)
- Include mix of: new authorizations, long-standing, different departments
- Include at least 2 high-risk roles (if applicable)

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Sample ID | Unique identifier for sample | Auto-generated |
| Employee ID | Personnel identifier (anonymized if needed) | Free text |
| Department | Department/team | Free text |
| Role | Job role/title | Free text |
| Authorization Date | When remote work was authorized | Date |
| Approval Obtained | Was formal approval obtained? | Yes/No |
| Approved By | Who approved (role) | Free text |
| Documentation Complete | All required docs present? | Yes/No/Partial |
| Risk Assessment Done | For high-risk roles | Yes/No/N/A |
| Acknowledgment Signed | Security acknowledgment obtained | Yes/No |
| Compliant | Overall compliance | Yes/No |
| Notes | Observations | Free text |

#### 4.6 Periodic_Review Sheet

**Purpose**: Assess whether remote work authorizations are periodically reviewed.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Review Requirement | What should be reviewed | Pre-populated |
| Frequency | Required review frequency | Pre-populated |
| Last Review Date | When was this last reviewed | Date |
| Next Review Due | When is next review due | Calculated |
| Overdue | Is review overdue? | Calculated |
| Evidence | Evidence of review | Free text |
| Notes | Observations | Free text |

#### 4.7 Gap_Analysis Sheet

**Purpose**: Consolidate all gaps identified across assessment areas.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Gap ID | Unique identifier (e.g., GAP-RWA-001) | Auto-generated |
| Source Sheet | Which sheet identified this gap | Reference |
| Gap Description | Clear description of the gap | Free text |
| Control Reference | Related policy section | Free text |
| Risk Level | Risk if gap not addressed (H/M/L) | Dropdown |
| Remediation Action | Recommended fix | Free text |
| Owner | Who will remediate | Free text |
| Target Date | When remediation should complete | Date |
| Status | Current status | Dropdown |

#### 4.8 Evidence_Register Sheet

**Purpose**: Catalog all evidence collected during assessment.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Evidence ID | Unique identifier (e.g., EVD-RWA-001) | Auto-generated |
| Evidence Type | Document/Screenshot/Interview/System Export | Dropdown |
| Description | What the evidence demonstrates | Free text |
| Source | Where evidence was obtained | Free text |
| Date Collected | When evidence was collected | Date |
| Collected By | Assessor name | Free text |
| File Reference | Filename or storage location | Free text |
| Related Gap | If evidence relates to a gap | Reference |

#### 4.9 Dashboard Sheet

**Purpose**: Provide executive summary of assessment results.

**Metrics Displayed**:
- Overall compliance percentage
- Gap count by severity
- Sample testing pass rate
- Policy framework completeness
- Authorization process maturity

**Note**: Dashboard is auto-calculated from other sheets. No manual input required.

#### 4.10 Approval_Sign_Off Sheet

**Purpose**: Document formal review and approval of assessment.

**Sections**:
1. **Assessor Certification**: Assessor confirms accuracy
2. **Technical Review**: IT Security review
3. **Management Approval**: CISO approval
4. **Next Steps**: Agreed actions and timeline

### 5. Evidence Collection Guidelines

#### 5.1 Required Evidence Types

| Evidence Category | Examples |
|-------------------|----------|
| Policy Documentation | Remote work policy, authorization procedure |
| Process Documentation | Workflow diagrams, approval forms |
| Authorization Records | Approved remote work requests |
| Acknowledgments | Signed security acknowledgments |
| Review Records | Periodic review documentation |
| System Exports | HR system reports, access logs |

#### 5.2 Evidence Quality Standards

Evidence must be:
- **Dated**: Clear date of creation/capture
- **Attributed**: Source system or document identified
- **Complete**: Shows full context, not excerpts
- **Current**: Reflects current state (within assessment period)
- **Authentic**: Original or verified copy

### 6. Common Pitfalls

#### ❌ MISTAKE #1: Assessing Policy Without Verifying Implementation

**The Problem:** Reviewing remote work policy documents but not checking whether the authorization process actually works as documented.

**Why It Matters:** Policy documentation may be aspirational or outdated. Actual practice often differs from documented procedures. Auditors will test implementation, not just documentation.

**The Fix:**
- Always include sample testing of actual authorizations
- Interview process participants (requesters, approvers, HR, IT)
- Verify that documented workflows match actual practice
- Check for workarounds or informal processes

#### ❌ MISTAKE #2: Missing Informal Remote Work Arrangements

**The Problem:** Only assessing formally documented remote workers, missing those with informal arrangements.

**Why It Matters:** Informal remote workers may lack security controls. They represent shadow IT risk. Organization may be unaware of full remote workforce scope.

**The Fix:**
- Survey managers about team members working remotely
- Cross-reference badge access data with VPN logs
- Check for employees who rarely badge into office
- Review pandemic-era temporary arrangements that became permanent

#### ❌ MISTAKE #3: Overlooking Contractor and Third-Party Remote Access

**The Problem:** Assessment scope limited to employees, excluding contractors, consultants, and third-party personnel.

**Why It Matters:** Third parties often have same or greater access than employees. Contractor remote access may have weaker controls. Third-party incidents can impact organization.

**The Fix:**
- Explicitly include non-employees in assessment scope
- Request contractor lists from procurement/vendor management
- Check third-party access provisioning records
- Verify contractor remote work agreements exist

#### ❌ MISTAKE #4: Not Checking Terminated Employee Access Revocation

**The Problem:** Assessing current authorizations without verifying that departed employees had access promptly revoked.

**Why It Matters:** Delayed revocation is a common audit finding. Former employees with active remote access pose security risk. Demonstrates control weakness in JML process.

**The Fix:**
- Sample recently terminated employees (last 90 days)
- Verify VPN/remote access revoked within SLA
- Check for orphaned accounts in remote access systems
- Cross-reference HR termination dates with IT access revocation dates

#### ❌ MISTAKE #5: Assuming HR Records Are Complete and Accurate

**The Problem:** Relying solely on HR system as source of truth for remote worker inventory.

**Why It Matters:** HR systems may not capture all remote work arrangements. IT may provision access without HR awareness. Temporary arrangements may not be recorded.

**The Fix:**
- Cross-reference HR data with IT access records
- Compare HR remote worker list with VPN user list
- Identify users with remote access but no HR designation
- Reconcile discrepancies before concluding assessment

#### ❌ MISTAKE #6: Skipping Risk Assessment Verification for High-Risk Roles

**The Problem:** Treating all remote work authorizations equally, not checking enhanced scrutiny for sensitive roles.

**Why It Matters:** High-risk roles (finance, IT admin, executives) require additional risk assessment per policy. Missing this verification is a compliance gap. These roles are primary targets for attacks.

**The Fix:**
- Identify high-risk roles per policy definition
- Verify enhanced risk assessment was performed
- Check for additional controls (MFA, privileged access management)
- Document any exceptions with compensating controls

#### ❌ MISTAKE #7: Not Documenting Absence of Evidence

**The Problem:** Failing to record when expected evidence doesn't exist, only documenting what was found.

**Why It Matters:** Absence of evidence is evidence of a gap. Auditors expect documentation of what was checked. Unrecorded gaps may be forgotten.

**The Fix:**
- Explicitly note when expected documentation is missing
- Record "Not Available" rather than leaving blank
- Document why evidence couldn't be obtained
- Include in gap analysis for remediation

#### ❌ MISTAKE #8: Rushing Sample Selection

**The Problem:** Selecting convenient samples rather than representative samples.

**Why It Matters:** Biased samples don't represent true compliance state. Cherry-picked examples may hide systemic issues. Auditors may question sampling methodology.

**The Fix:**
- Use structured sampling methodology (random or stratified)
- Document sample selection criteria and rationale
- Include variety: departments, tenure, employment types
- Ensure sample size is statistically meaningful

#### ❌ MISTAKE #9: Ignoring Policy Exceptions

**The Problem:** Assessing standard authorizations but not reviewing approved exceptions to policy.

**Why It Matters:** Exceptions may indicate policy gaps or implementation challenges. Unapproved exceptions are compliance violations. Exception patterns reveal systemic issues.

**The Fix:**
- Request list of approved policy exceptions
- Verify exception approval followed documented process
- Check that compensating controls are in place
- Assess whether exceptions should become policy changes

#### ❌ MISTAKE #10: Not Interviewing Process Owners

**The Problem:** Conducting document-only assessment without speaking to people who operate the process.

**Why It Matters:** Documents may not reflect current practice. Process owners know where problems exist. Interviews reveal practical challenges not in documentation.

**The Fix:**
- Schedule interviews with key process owners
- Prepare interview questions in advance
- Document interview findings
- Corroborate interview information with evidence

---

### 7. Quality Checklist

Before submitting assessment, verify:

#### Completeness Checks

**Sheet Completion:**
- [ ] All 10 sheets contain data or documented N/A justification
- [ ] All required fields populated (no blank mandatory cells)
- [ ] Instructions sheet reviewed and version confirmed

**Sample Testing:**
- [ ] Sample size meets minimum (≥10 authorizations or 10% of population)
- [ ] Sample includes variety: new, existing, high-risk, standard
- [ ] All sample items fully tested and documented
- [ ] Pass/fail status recorded for each sample

**Gap Documentation:**
- [ ] All identified gaps recorded in Gap_Analysis sheet
- [ ] Each gap has: description, severity, remediation, owner, target date
- [ ] No gaps left without remediation plan
- [ ] Critical gaps escalated appropriately

**Evidence:**
- [ ] All evidence cataloged in Evidence_Register
- [ ] Evidence references match actual file locations
- [ ] Evidence dated within assessment period
- [ ] Sensitive evidence appropriately protected

#### Accuracy Checks

- [ ] Status assessments justified with evidence
- [ ] Evidence references verified accessible
- [ ] Dates accurate (assessment period, evidence dates)
- [ ] Calculations spot-checked (dashboard metrics)
- [ ] Cross-references between sheets correct

#### Policy Alignment Checks

- [ ] Assessment criteria align with ISMS-POL-A.6.7-8
- [ ] Compliance thresholds match policy requirements
- [ ] Gap priorities reflect policy risk levels
- [ ] Remediation timelines within policy SLAs

#### Audit Readiness Checks

- [ ] Assessment could withstand external audit scrutiny
- [ ] Evidence trail complete and verifiable
- [ ] Methodology documented and defensible
- [ ] Findings clearly supported by evidence

#### Red Flags to Address Before Submission

| Red Flag | Resolution |
|----------|------------|
| >20% sample failure rate | Escalate to CISO before submitting |
| Missing critical evidence | Document gap and remediation plan |
| Conflicting data sources | Reconcile and document resolution |
| Unauthorized remote workers found | Initiate immediate security review |
| Policy exceptions without approval | Document as compliance violation |

---

### 8. Review and Approval Process

#### 8.1 Review Workflow

**Step 1: Self-Review** (Assessor)

Before submitting for review:
- Complete Quality Checklist above
- Verify all calculations are correct
- Ensure evidence is accessible
- Prepare summary of key findings

**Step 2: Peer Review** (Another Assessor)

**Reviewer:** Security team member not involved in assessment
**Focus:** Methodology and objectivity

**Review Points:**
- Sampling methodology appropriate
- Evidence supports conclusions
- Gaps accurately characterized
- No obvious oversights

**Duration:** 2-3 business days

**Step 3: Technical Review** (IT Security Lead)

**Reviewer:** IT Security Lead or designated technical reviewer
**Focus:** Technical accuracy

**Review Points:**
- Technical controls accurately assessed
- Access provisioning findings verified
- Integration points correctly evaluated
- Technical remediation feasible

**Duration:** 2-3 business days

**Step 4: Management Approval** (CISO)

**Reviewer:** Chief Information Security Officer
**Focus:** Strategic alignment and risk assessment

**Review Points:**
- Overall risk posture acceptable
- Gaps appropriately prioritized
- Remediation resources adequate
- Timeline realistic

**Duration:** 1-2 business days

**Outcomes:**
- **Approved:** Assessment complete, remediation authorized
- **Approved with Conditions:** Specific follow-up required
- **Rejected:** Material issues, reassessment required

#### 8.2 Approval Timeline

| Phase | Duration | Cumulative |
|-------|----------|------------|
| Assessment completion | 3-5 days | Day 5 |
| Self-review | 1 day | Day 6 |
| Peer review | 2-3 days | Day 9 |
| Technical review | 2-3 days | Day 12 |
| Management approval | 1-2 days | Day 14 |
| **Total** | **~2 weeks** | |

#### 8.3 After Approval

**Immediate Actions:**

1. **Store Assessment:**
   - Location: `ISMS/Controls/A.6.7-8_Remote_Working/Assessments/`
   - Filename: `ISMS-IMP-A.6.7-8.S1_Authorization_[DATE]_APPROVED.xlsx`

2. **Distribute Results:**
   - HR: For remote work policy enforcement
   - IT Operations: For access control remediation
   - Department Managers: For team compliance awareness
   - Compliance: For audit evidence

3. **Initiate Remediation:**
   - Create tickets for each gap
   - Assign to documented owners
   - Set due dates per remediation plan
   - Schedule progress check-ins

4. **Schedule Follow-Up:**
   - Annual reassessment (or per policy cycle)
   - Quarterly remediation progress review
   - Triggered reassessment if significant changes

---

## PART II: Technical Specification

### 9. Workbook Architecture

#### 9.1 Sheet Structure

| Sheet Name | Purpose | Sheet Type |
|------------|---------|------------|
| Instructions | User guidance | Static |
| Policy_Framework | Policy documentation assessment | Assessment |
| Authorization_Process | Workflow assessment | Assessment |
| Authorization_Criteria | Criteria definition assessment | Assessment |
| Sample_Testing | Sample authorization testing | Assessment |
| Periodic_Review | Review cycle assessment | Assessment |
| Gap_Analysis | Consolidated gaps | Analysis |
| Evidence_Register | Evidence catalog | Register |
| Dashboard | Executive summary | Calculated |
| Approval_Sign_Off | Formal approvals | Governance |

#### 9.2 Sheet Dependencies

```
Policy_Framework ─────┐
Authorization_Process ─┼──→ Gap_Analysis ──→ Dashboard
Authorization_Criteria ┤
Sample_Testing ────────┤
Periodic_Review ───────┘

All Sheets ──→ Evidence_Register
```

### 10. Column Specifications

#### 10.1 Policy_Framework Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Policy Element | 30 | Text | Pre-populated |
| B | Requirement | 50 | Text | Pre-populated |
| C | Status | 15 | Dropdown | Exists/Partial/Missing |
| D | Evidence Reference | 30 | Text | Free text |
| E | Gap Description | 40 | Text | Free text |
| F | Remediation | 40 | Text | Free text |
| G | Priority | 12 | Dropdown | High/Medium/Low |

#### 10.2 Sample_Testing Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Sample ID | 12 | Text | Auto-generated (RWA-###) |
| B | Employee ID | 15 | Text | Free text |
| C | Department | 20 | Text | Free text |
| D | Role | 25 | Text | Free text |
| E | Authorization Date | 15 | Date | Date format |
| F | Approval Obtained | 12 | Dropdown | Yes/No |
| G | Approved By | 20 | Text | Free text |
| H | Documentation Complete | 15 | Dropdown | Yes/No/Partial |
| I | Risk Assessment Done | 15 | Dropdown | Yes/No/N/A |
| J | Acknowledgment Signed | 15 | Dropdown | Yes/No |
| K | Compliant | 12 | Formula | =AND(F="Yes",H="Yes",J="Yes") |
| L | Notes | 40 | Text | Free text |

#### 10.3 Gap_Analysis Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap ID | 15 | Text | GAP-RWA-### format |
| B | Source Sheet | 20 | Text | Sheet name |
| C | Gap Description | 50 | Text | Free text |
| D | Control Reference | 25 | Text | Policy section |
| E | Risk Level | 12 | Dropdown | High/Medium/Low |
| F | Remediation Action | 50 | Text | Free text |
| G | Owner | 20 | Text | Free text |
| H | Target Date | 15 | Date | Date format |
| I | Status | 15 | Dropdown | Open/In Progress/Closed |

### 11. Formula Specifications

#### 11.1 Dashboard Calculations

**Overall Compliance %**:
```
=COUNTIF(Sample_Testing!K:K,"TRUE")/COUNTA(Sample_Testing!K2:K100)
```

**Gaps by Severity**:
```
High: =COUNTIF(Gap_Analysis!E:E,"High")
Medium: =COUNTIF(Gap_Analysis!E:E,"Medium")
Low: =COUNTIF(Gap_Analysis!E:E,"Low")
```

**Policy Framework Score**:
```
=COUNTIF(Policy_Framework!C:C,"Exists")/(COUNTIF(Policy_Framework!C:C,"Exists")+COUNTIF(Policy_Framework!C:C,"Partial")+COUNTIF(Policy_Framework!C:C,"Missing"))
```

### 12. Styling Specifications

#### 12.1 Color Coding

| Element | Fill Color | Font Color | Use |
|---------|------------|------------|-----|
| Header Row | #003366 (Navy) | #FFFFFF (White) | Column headers |
| Input Cell | #FFFF00 (Yellow) | #000000 (Black) | User input |
| Calculated Cell | #DCE6F1 (Light Blue) | #000000 (Black) | Formulas |
| Label Cell | #D9D9D9 (Gray) | #000000 (Black) | Row labels |
| Compliant | #C6EFCE (Light Green) | #006100 (Dark Green) | Pass status |
| Non-Compliant | #FFC7CE (Light Red) | #9C0006 (Dark Red) | Fail status |
| Partial | #FFEB9C (Light Yellow) | #9C5700 (Dark Yellow) | Partial status |

#### 12.2 Conditional Formatting

**Status Column (Policy_Framework)**:
- "Exists" → Green fill
- "Partial" → Yellow fill
- "Missing" → Red fill

**Compliant Column (Sample_Testing)**:
- TRUE → Green fill
- FALSE → Red fill

**Risk Level (Gap_Analysis)**:
- "High" → Red fill
- "Medium" → Yellow fill
- "Low" → Green fill

### 13. Data Validation Lists

#### 13.1 Dropdown Options

| Field | Options |
|-------|---------|
| Status (Policy) | Exists, Partial, Missing |
| Implemented | Yes, No, Partial |
| Priority | High, Medium, Low |
| Risk Level | High, Medium, Low |
| Gap Status | Open, In Progress, Closed, Deferred |
| Evidence Type | Document, Screenshot, Interview, System Export, Email |
| Yes/No | Yes, No |
| Yes/No/Partial | Yes, No, Partial |
| Yes/No/N/A | Yes, No, N/A |

### 14. Pre-Populated Content

#### 14.1 Policy Framework Elements

| Policy Element | Requirement |
|----------------|-------------|
| Remote Work Policy | Formal policy document approved and published |
| Authorization Procedure | Documented process for requesting/approving remote work |
| Security Requirements | Technical and physical security requirements defined |
| Eligibility Criteria | Criteria for remote work eligibility documented |
| Data Handling Rules | Data classification handling for remote work |
| Device Requirements | Corporate and BYOD device requirements |
| Termination Procedure | Process for revoking remote work authorization |
| Review Cycle | Periodic review requirements defined |

#### 14.2 Authorization Process Steps

| Step | Description |
|------|-------------|
| Request Initiation | Employee/manager initiates remote work request |
| Eligibility Check | HR/Manager verifies role eligibility |
| Risk Assessment | Security assesses risk for sensitive roles |
| Technical Approval | IT confirms technical capability |
| Manager Approval | Line manager approves arrangement |
| Security Acknowledgment | Employee signs security requirements |
| Access Provisioning | IT provisions remote access |
| Documentation | Records filed in HR system |
| Periodic Review | Authorization reviewed per schedule |

---

## END OF SPECIFICATION

---

*"The only truly secure system is one that is powered off, cast in a block of concrete, and sealed in a lead-lined room with armed guards."*
— Gene Spafford

<!-- QA_VERIFIED: 2026-01-31 -->
