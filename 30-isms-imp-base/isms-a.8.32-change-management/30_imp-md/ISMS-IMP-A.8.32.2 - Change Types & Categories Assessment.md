**ISMS-IMP-A.8.32.2 - Change Types & Categories Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.32.2 |
| **Version** | 1.0 |
| **Assessment Area** | Change Types, Categories & Risk Classification |
| **Related Policy** | ISMS-POL-A.8.32, Section 2.2 (Change Classification Requirements) |
| **Purpose** | Document standard/normal/emergency change types, assess classification procedures, and evaluate risk-based categorization in a technology-agnostic manner |
| **Target Audience** | Change Manager, Risk Assessors, CAB Members, System Owners, Compliance Officers, Auditors, Workbook Developers |
| **Assessment Type** | Process & Risk Assessment |
| **Review Cycle** | Quarterly or After Classification Process Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial assessment specification for Change Types & Categories workbook | ISMS Implementation Team |

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

- **Part I:** Assessment users (Change Manager, Risk Assessors, CAB Members, System Owners)
- **Part II:** Workbook developers (Python/Excel script maintainers)


---

# PART I: USER COMPLETION GUIDE

**Audience:** Change Manager, Risk Assessors, CAB Members, System Owners

---

## Assessment Overview

### What This Assessment Evaluates

This assessment documents HOW your organization classifies changes into different types (Standard, Normal, Emergency) and HOW you assess change risk. It evaluates:

- **Standard Change Catalog:** What pre-approved, low-risk changes are documented
- **Normal Change Procedures:** How moderate/high-risk changes are assessed and categorized
- **Emergency Change Criteria:** What qualifies as emergency and how it's handled
- **Risk Assessment Methodology:** How you calculate change risk (Impact x Likelihood)
- **Change Calendar Management:** How you schedule changes and manage blackout windows


### Why This Matters

This assessment verifies [Organization]'s compliance with:

- ISO/IEC 27001:2022 Control A.8.32: Change Management
- ISMS-POL-A.8.32, Section 2.2 (Change Classification Requirements)
- ISO 27002:2022 element (f): Emergency and contingency procedures


Proper change classification ensures appropriate oversight - low-risk changes move quickly, high-risk changes get scrutiny. Risk assessment enables informed approval decisions.

### Key Principle

This assessment is **completely technology-agnostic**. You document YOUR specific classification approach and risk methodology, regardless of tools used.

---

## Prerequisites

### Before Starting This Assessment

**Required:**

- [ ] Read ISMS-POL-A.8.32, Section 2.2 (Change Classification Requirements)
- [ ] Identify Change Manager or Risk Assessment owner
- [ ] Gather Standard Change Catalog (if it exists)
- [ ] Access change management system
- [ ] Sample changes of each type (standard, normal, emergency)
- [ ] Risk assessment methodology documentation
- [ ] Change calendar or freeze period documentation


**Recommended:**

- [ ] Interview Change Manager about classification decisions
- [ ] Review last 3 months of changes by type
- [ ] Gather emergency change approvals
- [ ] Review change failure analysis by type
- [ ] Identify risk assessment training materials


### Who Should Complete This Assessment

**Primary:** Change Manager (classification procedures owner)

**Contributors:**

- Risk Assessors (risk methodology)
- CAB Members (approval thresholds)
- System Owners (standard change catalog entries)
- IT Operations (emergency change procedures)
- Compliance Officer (risk acceptance documentation)


**Reviewers:**

- CISO (risk assessment validation)
- Internal Audit (classification effectiveness)


---

## Assessment Workflow

### Step-by-Step Process

**Step 1: Initial Setup (Day 1)**

- Assign assessment owner (Change Manager)
- Gather existing classification documentation
- Review completion timeline (2-3 weeks)


**Step 2: Standard Change Catalog Documentation (Days 2-5)**

- Document all pre-approved standard changes (Sheet 2)
- Include procedure, risk assessment, success rate
- Verify catalog is actively used
- Document catalog review frequency


**Step 3: Normal Change Classification (Days 3-6)**

- Document normal change categorization criteria (Sheet 3)
- Assess classification consistency
- Review sample normal changes
- Verify risk assessment completion


**Step 4: Emergency Change Assessment (Days 4-7)**

- Document emergency change triggers (Sheet 4)
- Review emergency approval procedures
- Assess emergency change frequency
- Verify post-implementation reviews


**Step 5: Risk Assessment Methodology (Days 5-8)**

- Document risk classification approach (Sheet 5)
- Define Impact and Likelihood levels
- Document risk matrix (Impact x Likelihood)
- Verify approval authority alignment


**Step 6: Change Calendar Management (Days 6-9)**

- Document change scheduling approach (Sheet 6)
- Identify blackout windows and freeze periods
- Assess conflict management
- Review change calendar effectiveness


**Step 7: Classification Metrics (Days 7-10)**

- Document tracked metrics (Sheet 7)
- Review change type distribution
- Assess classification accuracy
- Analyze emergency change trends


**Step 8: Evidence Collection (Days 8-11)**

- Compile supporting evidence (Sheet 8)
- Link evidence to requirements
- Verify evidence accessibility


**Step 9: Summary Review (Days 9-12)**

- Review auto-calculated compliance (Sheet 9)
- Validate gap analysis
- Prioritize remediation


**Step 10: Quality Review (Days 10-13)**

- Self-review against checklist
- Peer review by CAB members


**Step 11: Final Approval (Days 11-15)**

- Change Manager approval
- CISO review and sign-off (Sheet 10)


**Total Duration:** 2-3 weeks

---

## Completing Each Sheet

### Sheet 1: Instructions & Legend

**Pre-filled** - Read to understand status symbols, compliance levels, and evidence expectations.

### Sheet 2: Standard_Changes_Catalog

**What to document:**

- Every standard change your organization has pre-approved
- Description, procedure, prerequisites, duration
- Risk level, success rate, last review date
- Owner and usage frequency


**Tips:**

- If you have NO standard change catalog, this is a gap - document as finding
- Common standard changes: password resets, certificate renewals, routine patches, standard software installs
- Each catalog entry should have documented procedure (not just "do the needful")
- If standard changes frequently fail, they shouldn't be standard - reclassify


**Common Questions:**

- **Q:** "How many standard changes should we have?"
  - **A:** Depends on your environment. Start with truly routine, low-risk activities. 10-30 is typical range.
- **Q:** "Can emergency activities be standard changes?"
  - **A:** No - emergency changes have different triggers. Standard changes are routine activities.
- **Q:** "Do standard changes need CAB approval?"
  - **A:** No - they're pre-approved. Log them, execute them, no CAB review needed.


**Evidence to provide:**

- Standard Change Catalog document
- Sample standard change tickets
- Procedures for each catalog entry
- Catalog review meeting minutes


### Sheet 3: Normal_Change_Classification

**What to document:**

- How you determine if a change is "normal" (needs CAB review)
- Classification criteria (complexity, risk, impact)
- Who performs initial classification
- Reclassification procedures


**Tips:**

- Normal changes = everything that isn't standard or emergency
- Most changes should be normal (60-80% typical)
- Classification should happen early (at request submission)
- Misclassification should trigger process review


**Common Questions:**

- **Q:** "What if we're not sure if something is normal or standard?"
  - **A:** Default to normal (more oversight). Add to standard catalog after proven track record.
- **Q:** "Can normal changes become standard over time?"
  - **A:** Yes! That's continuous improvement. Document promotion criteria.


**Evidence to provide:**

- Classification criteria documentation
- Sample normal change requests
- CAB review records
- Reclassification examples


### Sheet 4: Emergency_Change_Procedures

**What to document:**

- What qualifies as emergency change
- Emergency approval procedures (E-CAB)
- Fast-track process vs standard process
- Post-implementation review requirements
- Emergency change frequency and trends


**Tips:**

- Emergency changes should be RARE (<5% of all changes is target)
- High emergency % indicates planning problems
- "Urgent because we forgot" is NOT emergency - it's poor planning
- Document actual emergency criteria honestly


**Common Questions:**

- **Q:** "Can we skip testing for emergencies?"
  - **A:** Policy allows risk-based testing shortcuts WITH documented risk acceptance. Never skip entirely.
- **Q:** "Who can declare something emergency?"
  - **A:** Document YOUR criteria and approval authority (typically IT Ops Manager + CISO).
- **Q:** "Do emergencies need PIR?"
  - **A:** YES - mandatory per policy. This is how you learn and prevent future emergencies.


**Evidence to provide:**

- Emergency change procedure document
- E-CAB approval examples
- Emergency PIR reports
- Emergency change trend analysis


### Sheet 5: Risk_Assessment_Matrix

**What to document:**

- Impact level definitions (Low/Medium/High/Critical)
- Likelihood level definitions (Low/Medium/High)
- Risk matrix (Impact x Likelihood = Risk Level)
- Approval authority by risk level
- Risk mitigation strategies


**Tips:**

- Be specific in definitions - "High Impact" needs concrete criteria
- Document YOUR organization's risk tolerance
- Risk matrix should align with approval authority (ISMS-POL-A.8.32, Section 2.1)
- Consistency matters - same risk assessment regardless of who performs it


**Common Questions:**

- **Q:** "Should we use our enterprise risk methodology?"
  - **A:** If you have one, yes - align change risk with enterprise risk approach.
- **Q:** "What if impact is High but likelihood is Low?"
  - **A:** Follow the matrix - that's typically Medium risk. Document if you deviate.
- **Q:** "Can we reassess risk during the change process?"
  - **A:** Yes - if scope changes, risk changes. Document reassessment triggers.


**Evidence to provide:**

- Risk assessment methodology document
- Risk matrix (can reference ISMS-REF-A.8.32)
- Sample risk assessments
- Training materials for risk assessors


### Sheet 6: Change_Calendar_Management

**What to document:**

- How changes are scheduled
- Change freeze periods (e.g., financial year-end, peak business)
- Blackout windows (no non-emergency changes)
- Conflict management (overlapping changes)
- Change calendar tool/system


**Tips:**

- If you don't have change calendar, mark as gap
- Freeze periods protect critical business periods
- Too many freeze periods = changes back up
- Document exceptions process (emergency changes during freeze)


**Common Questions:**

- **Q:** "We don't have formal freeze periods"
  - **A:** Document actual practice - do you avoid changes during certain times? That's informal freeze.
- **Q:** "What if two changes conflict?"
  - **A:** Document YOUR conflict resolution process (defer one, coordinate timing, etc.).


**Evidence to provide:**

- Change calendar (screenshot or export)
- Freeze period documentation
- Conflict resolution examples
- Change scheduling policy


### Sheet 7: Classification_Metrics

**What to document:**

- Change volume by type (standard/normal/emergency)
- Change type distribution (% of each)
- Classification accuracy (misclassifications caught)
- Emergency change trend
- Success rate by change type


**Tips:**

- If you don't track this, mark as gap - these are key metrics
- Emergency % is KEY indicator - rising trend means problems
- Low standard change utilization = catalog not valuable
- Success rate should be HIGHEST for standard, lowest acceptable for emergency


**Common Questions:**

- **Q:** "What's acceptable emergency change percentage?"
  - **A:** Policy target is <5%. Above 10% indicates systemic issues.
- **Q:** "Should standard changes have 100% success rate?"
  - **A:** Near 100% - if standard changes fail regularly, they shouldn't be standard.


**Evidence to provide:**

- Change metrics reports
- Trend analysis charts
- Classification audit results


### Sheet 8: Evidence_Register

**What to document:**

- Evidence location for all requirements
- Evidence type and last verification date
- Accessibility for auditors


**Tips:**

- Be specific with evidence locations
- Reference actual documents, not hypothetical ones


### Sheet 9: Summary_Dashboard

**Auto-calculated** - Review for accuracy:

- Overall compliance percentage
- Compliance by domain
- Critical gaps
- Audit readiness


### Sheet 10: Approval_Sign_Off

**What to complete:**

- Assessment completion date
- Change Manager sign-off
- CISO approval
- Next review date


---

## Evidence Collection

### Types of Evidence

**Catalog Evidence:**

- Standard Change Catalog document
- Procedures for each catalog entry
- Success rate data
- Catalog review minutes


**Classification Evidence:**

- Classification criteria documentation
- Risk assessment methodology
- Sample changes (all types)
- CAB review notes showing classifications


**Emergency Evidence:**

- Emergency change procedures
- E-CAB approval records
- Emergency PIR reports
- Emergency change log


**Risk Assessment Evidence:**

- Risk matrix documentation
- Approval authority matrix
- Sample risk assessments
- Risk assessor training materials


**Calendar Evidence:**

- Change calendar screenshots
- Freeze period announcements
- Conflict resolution examples


### Evidence Best Practices

**Do:**

- ? Document actual practice, not aspirational
- ? Include metrics showing trends
- ? Reference risk assessments with actual change examples
- ? Show catalog is actively maintained (review dates)


**Don't:**

- ? Create "catalog" just for audit with entries never used
- ? Classify everything as emergency to skip process
- ? Hide high emergency change percentage
- ? Reference non-existent risk methodology


---

## Common Pitfalls

### Mistake #1: "We don't need a standard change catalog"

**Problem:** Missing efficiency opportunity and not fully policy-compliant.

**Solution:** Start small - identify 5-10 truly routine activities and catalog them properly.

### Mistake #2: "Everything is emergency because we're fast-paced"

**Problem:** Process erosion. If everything is emergency, nothing is.

**Solution:** Document true emergency criteria. High percentage is finding, not excuse.

### Mistake #3: "Risk assessment is too subjective"

**Problem:** Inconsistent classification leads to wrong approval levels.

**Solution:** Define concrete impact/likelihood criteria. Train assessors. Audit consistency.

### Mistake #4: "Standard changes never get reviewed"

**Problem:** Catalog becomes stale, includes activities that are no longer low-risk.

**Solution:** Policy requires quarterly catalog review. Document review dates and decisions.

### Mistake #5: "We classify changes after implementation"

**Problem:** Defeats purpose of classification (proper oversight).

**Solution:** Classification happens at REQUEST TIME, before approval.

### Mistake #6: "Emergency changes don't need post-review"

**Problem:** Policy violation. You don't learn from emergencies.

**Solution:** Mandatory PIR for ALL emergency changes within policy timeframe.

### Mistake #7: "Risk matrix is just for show"

**Problem:** If risk assessment doesn't drive decisions, it's theater.

**Solution:** Verify approval authorities align with risk levels. High-risk = high approval.

### Mistake #8: "Change calendar is too much overhead"

**Problem:** Results in overlapping changes, conflicts, unexpected downtime.

**Solution:** Even simple calendar (shared calendar, spreadsheet) better than none.

### Mistake #9: "We use ServiceNow's default classification"

**Problem:** Vendor defaults may not match YOUR risk tolerance.

**Solution:** Customize to YOUR organization. Document YOUR criteria.

### Mistake #10: "Classification is the requester's job"

**Problem:** Requesters often lack perspective for accurate classification.

**Solution:** Change Manager validates/corrects classification. Document who has final say.

---

## Quality Checklist

### Assessment Completeness

**Standard Change Catalog:**

- [ ] All standard changes documented
- [ ] Each entry has procedure
- [ ] Risk assessment completed for each
- [ ] Success rates documented
- [ ] Last review date recorded
- [ ] Catalog is actively used (evidence)


**Normal Changes:**

- [ ] Classification criteria documented
- [ ] Sample normal changes provided
- [ ] CAB review process verified
- [ ] Reclassification procedures defined


**Emergency Changes:**

- [ ] Emergency criteria defined
- [ ] E-CAB procedures documented
- [ ] Emergency % tracked
- [ ] PIR completion verified
- [ ] Emergency trend analyzed


**Risk Assessment:**

- [ ] Impact levels defined with criteria
- [ ] Likelihood levels defined with criteria
- [ ] Risk matrix complete
- [ ] Approval authorities aligned with risk
- [ ] Assessor training documented


**Change Calendar:**

- [ ] Calendar system/method documented
- [ ] Freeze periods identified
- [ ] Conflict resolution process defined
- [ ] Calendar effectiveness assessed


**Metrics:**

- [ ] Change type distribution tracked
- [ ] Emergency % monitored
- [ ] Success rates by type tracked
- [ ] Trends analyzed


**Evidence:**

- [ ] Evidence Register complete
- [ ] All evidence accessible
- [ ] Evidence current (<6 months)


**Dashboard:**

- [ ] Compliance percentage validated
- [ ] Critical gaps identified
- [ ] Remediation priorities set


---

## Review & Approval

### Review Process

**Step 1: Self-Review (Change Manager)**

- Complete quality checklist
- Validate all data
- Check formula calculations


**Step 2: Peer Review (CAB Members)**

- Distribute to CAB members
- Request feedback on classification approach
- Typical turnaround: 3-5 days


**Step 3: Compliance Review (Compliance Officer)**

- Policy alignment check
- Risk methodology validation
- Regulatory requirement coverage
- Typical turnaround: 2-3 days


**Step 4: CISO Approval**

- Risk assessment methodology review
- Emergency change % review
- Critical gap risk acceptance
- Typical turnaround: 2-3 days


**Step 5: Documentation & Communication**

- Set status to "Final"
- Set next review date (+3 months)
- File in document management
- Notify gap owners


**Approval Timeline:** 2-3 weeks

**Rejection Reasons:**

- Incomplete standard change catalog
- Undefined risk methodology
- High emergency % without remediation plan
- Missing emergency PIR evidence
- Classification criteria too vague


---

## Continuous Improvement

### Using Assessment Results

**Catalog Optimization:**

- Low utilization -> Remove unused entries
- High utilization -> Promote successful normal changes to standard
- Failures -> Demote to normal change


**Risk Assessment Refinement:**

- Assess risk assessment accuracy - do assessed-low-risk changes succeed?
- If high-risk changes succeed without issues, criteria may be too conservative
- If low-risk changes fail, criteria too lenient


**Emergency Change Reduction:**

- Analyze root causes - planning issues? Pressure from business?
- Implement preventive measures
- Track emergency % trend - should decrease over time


**Classification Training:**

- If misclassifications common -> Training needed
- If risk assessments inconsistent -> Assessor calibration needed


---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

# ISMS-IMP-A.8.32.2 - Change Types & Categories Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.32.2  
**Assessment Area:** Change Types, Categories & Risk Classification  
**Related Policy:** ISMS-POL-A.8.32-S2.2 (Change Classification Requirements)  
**Purpose:** Document standard/normal/emergency change types, assess classification procedures, and evaluate risk-based categorization in a technology-agnostic manner

**Key Principle:** This assessment is **technology-independent**. Organizations document THEIR specific change classification approach and verify procedures against generic requirements.

---

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section

- **Title:** "ISMS-IMP-A.8.32.2 – Change Types & Categories Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.32: Change Management"
- **Styling:** Dark blue header (003366), white text, centered, 40px height


#### Document Information Block
```
Document ID:           ISMS-IMP-A.8.32.2
Assessment Area:       Change Types & Categories
Related Policy:        ISMS-POL-A.8.32-S2.2
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [Organization]
Review Cycle:          Quarterly
```

#### How to Use This Workbook
1. Complete the Standard_Changes_Catalog with YOUR pre-approved changes
2. Document YOUR normal change assessment criteria
3. Define YOUR emergency change triggers and procedures
4. Configure YOUR change risk classification matrix
5. Document YOUR change calendar management approach
6. Review the Summary_Dashboard for compliance metrics
7. Maintain the Evidence Register for audit traceability
8. Obtain final approval and sign-off

#### Status Legend
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| [YES] | Defined | Criteria/process clearly defined and documented | Green (C6EFCE) |
| [PARTIAL] | Partial | Partially defined or inconsistent application | Yellow (FFEB9C) |
| [NO] | Not Defined | Not defined or not documented | Red (FFC7CE) |
| [PLANNED] | Planned | Definition planned with target date | Blue (B4C7E7) |
| N/A | Not Applicable | Not applicable to this environment | Gray |


#### Change Type Decision Tree
```
Is this change:
|- Pre-approved, low-risk, well-documented? -> STANDARD CHANGE
|- Requires assessment and approval? -> NORMAL CHANGE
|   |- Low Risk + Low Impact -> Expedited Normal Change
|   |- Medium Risk/Impact -> Standard Normal Change
|   `- High/Critical Risk/Impact -> High-Priority Normal Change
`- Urgent, meets emergency criteria? -> EMERGENCY CHANGE
    |- Critical system outage?
    |- Security incident?
    |- Data loss prevention?
    `- Regulatory deadline?
```


#### Acceptable Evidence (Examples)

- ✓ Standard changes catalog/library
- ✓ Change classification decision trees
- ✓ Risk assessment matrices
- ✓ Emergency change criteria documentation
- ✓ Change calendar procedures
- ✓ CAB meeting records (classification decisions)
- ✓ Change metrics (by type and category)
- ✓ Training materials on change classification
- ✓ Audit reports on classification accuracy
- ✓ Exception/deviation records
- ✓ Change type definitions document
- ✓ Historical change data (by type)


---

## Sheet 2: Standard_Changes_Catalog

### Purpose
Document all pre-approved standard changes that can be executed without CAB approval.

### Header Section
**Row 1:** "STANDARD CHANGES CATALOG"  
**Row 2:** "Pre-approved, low-risk changes with documented procedures"

### Standard Change Register (Rows 4-53, 50 entries)

| Change ID | Change Title | Description | Category | Frequency | Pre-requisites | Procedure Location | Owner | Approval Date | Review Date | Risk Level | Status | Evidence |
|-----------|--------------|-------------|----------|-----------|----------------|-------------------|-------|---------------|-------------|------------|--------|----------|
| STD-001 | [User defines] | Text | Dropdown: Infrastructure/Application/Security/Data/Network/Other | Dropdown: Daily/Weekly/Monthly/Quarterly/On-Demand | Text | Text (URL/path) | Text | Date | Date | Dropdown: Low/Medium | Dropdown: ✅ Active/⚠️ Under Review/❌ Retired/📋 Proposed | Text |

**Column Specifications:**

#### Column: Change ID

- **Data Type:** Text (auto-suggest STD-NNN format)
- **Required:** Yes
- **Width:** 12
- **Description:** Unique identifier for standard change
- **Example:** STD-001, STD-002, etc.


#### Column: Change Title

- **Data Type:** Text
- **Required:** Yes
- **Width:** 30
- **Description:** Short, descriptive title
- **Example:** "Password Reset - End User", "Patch Deployment - Workstations"


#### Column: Description

- **Data Type:** Text (long)
- **Required:** Yes
- **Width:** 40
- **Description:** Full description of the change
- **Example:** "Reset end user password in Active Directory following identity verification"


#### Column: Category

- **Data Type:** Dropdown
- **Required:** Yes
- **Width:** 18
- **Validation:** Infrastructure, Application, Security, Data, Network, Cloud, User Access, Configuration, Other
- **Description:** Type of change for classification purposes


#### Column: Frequency

- **Data Type:** Dropdown
- **Required:** Yes
- **Width:** 15
- **Validation:** Daily, Weekly, Monthly, Quarterly, Annual, On-Demand, Rare
- **Description:** How often this change typically occurs


#### Column: Pre-requisites

- **Data Type:** Text
- **Required:** No
- **Width:** 30
- **Description:** Conditions that must be met before executing
- **Example:** "User identity verified via two-factor authentication"


#### Column: Procedure Location

- **Data Type:** Text
- **Required:** Yes
- **Width:** 30
- **Description:** Where detailed procedure is documented
- **Example:** "Wiki: /IT/Procedures/Password-Reset", "ServiceNow KB12345"


#### Column: Owner

- **Data Type:** Text
- **Required:** Yes
- **Width:** 20
- **Description:** Role or person responsible for this standard change
- **Example:** "Service Desk Team", "Network Operations"


#### Column: Approval Date

- **Data Type:** Date (DD.MM.YYYY)
- **Required:** Yes
- **Width:** 15
- **Description:** When this change was approved as standard


#### Column: Review Date

- **Data Type:** Date (DD.MM.YYYY)
- **Required:** Yes
- **Width:** 15
- **Description:** Next scheduled review (typically annually)


#### Column: Risk Level

- **Data Type:** Dropdown
- **Required:** Yes
- **Width:** 15
- **Validation:** Low, Medium (requires justification)
- **Description:** Only Low and Medium risk changes qualify as Standard
- **Note:** High/Critical changes CANNOT be Standard Changes per policy


#### Column: Status

- **Data Type:** Dropdown
- **Required:** Yes
- **Width:** 18
- **Validation:** ✅ Active, ⚠️ Under Review, ❌ Retired, 📋 Proposed
- **Description:** Current status of this standard change


#### Column: Evidence

- **Data Type:** Text
- **Required:** No
- **Width:** 25
- **Description:** Reference to evidence (procedure docs, approvals, etc.)


### Standard Change Summary Metrics (Rows 55-62)

| Metric | Value | Notes |
|--------|-------|-------|
| Total Standard Changes Defined | [Formula: COUNT] | [Text - editable] |
| Active Standard Changes | [Formula: COUNTIF Status=Active] | [Text] |
| Standard Changes Under Review | [Formula: COUNTIF Status=Review] | [Text] |
| Standard Changes Requiring Annual Review | [Formula: COUNT where Review Date < TODAY] | [Text] |
| Most Common Category | [Formula: MODE of Category] | [Text] |
| Average Age of Standard Changes | [Formula: Average of (TODAY - Approval Date)] | [Text] |

---

## Sheet 3: Normal_Changes_Assessment

### Purpose
Document criteria and procedures for normal (non-standard, non-emergency) changes.

### Header Section
**Row 1:** "NORMAL CHANGES ASSESSMENT"  
**Row 2:** "Changes requiring risk assessment, approval, and CAB review"

### Normal Change Criteria (Rows 4-20)

| Criterion | Defined | Documentation Reference | Assessment Method | Responsible Role | Compliance | Evidence |
|-----------|---------|------------------------|-------------------|------------------|------------|----------|
| Change does not meet Standard criteria | Dropdown: ✅/⚠️/❌/📋 | Text | Text | Text | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text |
| Change is not an emergency | Dropdown | Text | Text | Text | Dropdown | Text |
| Risk assessment required | Dropdown | Text | Text | Text | Dropdown | Text |
| Impact assessment required | Dropdown | Text | Text | Text | Dropdown | Text |
| CAB review required (based on risk) | Dropdown | Text | Text | Text | Dropdown | Text |
| Business justification required | Dropdown | Text | Text | Text | Dropdown | Text |
| Implementation plan required | Dropdown | Text | Text | Text | Dropdown | Text |
| Test plan required | Dropdown | Text | Text | Text | Dropdown | Text |
| Rollback plan required | Dropdown | Text | Text | Text | Dropdown | Text |
| Communication plan required | Dropdown | Text | Text | Text | Dropdown | Text |
| PIR (Post-Implementation Review) required | Dropdown | Text | Text | Text | Dropdown | Text |
| Change window scheduling required | Dropdown | Text | Text | Text | Dropdown | Text |

[15 rows total for normal change criteria]

### Risk-Based Approval Paths (Rows 22-35)

| Risk Category | Impact Category | Approval Authority | CAB Review | Typical Timeline | Success Rate | Documented | Evidence |
|---------------|----------------|-------------------|------------|------------------|-------------|------------|----------|
| Low | Low | Dropdown: Change Manager/CAB/Service Owner/CISO/Other | Dropdown: Mandatory/Recommended/Optional/Not Required | Text (e.g., "2-3 days") | Text (e.g., "95%") | Dropdown: ✅/⚠️/❌/📋 | Text |
| Low | Medium | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| Low | High | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| Medium | Low | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| Medium | Medium | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| Medium | High | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| High | Low | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| High | Medium | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| High | High | Dropdown | Dropdown: Mandatory (always) | Text | Text | Dropdown | Text |
| Critical | Any | Dropdown: Multiple approvers required | Dropdown: Mandatory | Text | Text | Dropdown | Text |

### Normal Change Workflow Stages (Rows 37-50)

| Stage | Stage Name | Required for All Normal Changes | Exceptions Allowed | Exception Approval | Documented | Evidence |
|-------|------------|-------------------------------|-------------------|-------------------|------------|----------|
| 1 | Change Request Submission | Dropdown: ✅ Yes/❌ No | Dropdown: ✅ Yes/❌ No | Text (who can approve exception) | Dropdown: ✅/⚠️/❌/📋 | Text |
| 2 | Risk Assessment | Dropdown | Dropdown | Text | Dropdown | Text |
| 3 | Impact Assessment | Dropdown | Dropdown | Text | Dropdown | Text |
| 4 | Change Classification | Dropdown | Dropdown | Text | Dropdown | Text |
| 5 | CAB Scheduling | Dropdown | Dropdown | Text | Dropdown | Text |
| 6 | CAB Review | Dropdown | Dropdown | Text | Dropdown | Text |
| 7 | Formal Approval | Dropdown | Dropdown | Text | Dropdown | Text |
| 8 | Implementation Planning | Dropdown | Dropdown | Text | Dropdown | Text |
| 9 | Testing (pre-implementation) | Dropdown | Dropdown | Text | Dropdown | Text |
| 10 | Stakeholder Notification | Dropdown | Dropdown | Text | Dropdown | Text |
| 11 | Implementation | Dropdown | Dropdown | Text | Dropdown | Text |
| 12 | Verification | Dropdown | Dropdown | Text | Dropdown | Text |
| 13 | Post-Implementation Review | Dropdown | Dropdown | Text | Dropdown | Text |

---

## Sheet 4: Emergency_Changes

### Purpose
Document emergency change criteria, procedures, and governance.

### Header Section
**Row 1:** "EMERGENCY CHANGES"  
**Row 2:** "Urgent changes meeting specific emergency criteria with E-CAB approval"

### Emergency Criteria Definition (Rows 4-15)

| Emergency Criterion | Defined | Specific Triggers | Escalation Path | Response Time SLA | Documented | Evidence |
|--------------------|---------|-------------------|-----------------|-------------------|------------|----------|
| System Outage (Critical Services) | Dropdown: ✅ Clearly Defined/⚠️ Partially/❌ Not Defined | Text (e.g., "Complete loss of email service >1000 users") | Text (e.g., "NOC → IT Ops Manager → CIO") | Text (e.g., "E-CAB within 30 min") | Dropdown: ✅/⚠️/❌/📋 | Text |
| Security Incident Response | Dropdown | Text | Text | Text | Dropdown | Text |
| Data Loss Prevention | Dropdown | Text | Text | Text | Dropdown | Text |
| Regulatory Compliance Deadline | Dropdown | Text | Text | Text | Dropdown | Text |
| Health & Safety Risk | Dropdown | Text | Text | Text | Dropdown | Text |
| Business Continuity Threat | Dropdown | Text | Text | Text | Dropdown | Text |
| [Custom Criterion 1] | Dropdown | Text | Text | Text | Dropdown | Text |
| [Custom Criterion 2] | Dropdown | Text | Text | Text | Dropdown | Text |

### Emergency Change Process Requirements (Rows 17-30)

| Requirement | Implemented | Process Description | Responsible Role | Exceptions Allowed | Compliance | Evidence |
|-------------|-------------|---------------------|------------------|-------------------|------------|----------|
| Emergency criteria must be met | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Text | Dropdown: ✅ Yes/❌ No/N/A | Dropdown: ✅/⚠️/❌ | Text |
| E-CAB convened | Dropdown | Text (how E-CAB is convened) | Text | Dropdown | Dropdown | Text |
| Minimum E-CAB members defined | Dropdown | Text (who must participate) | Text | Dropdown | Dropdown | Text |
| Emergency approval documented | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Risk acceptance explicit | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Communication immediate | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Implementation window immediate | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Rollback plan prepared (where feasible) | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Incident ticket linked | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Mandatory PIR within 2 business days | Dropdown | Text | Text | Dropdown: ❌ No Exceptions | Dropdown | Text |
| Retrospective CAB review | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Emergency change metrics tracked | Dropdown | Text | Text | Dropdown | Dropdown | Text |

### Emergency Change Metrics (Rows 32-42)

| Metric | Target | Current (Last Quarter) | Status | Notes |
|--------|--------|----------------------|--------|-------|
| Emergency changes as % of total changes | Text (e.g., "<5%") | Text (formula: [emergency count / total changes]) | Formula: Green/Yellow/Red based on target | Text (editable) |
| Average E-CAB response time | Text (e.g., "<30 minutes") | Text | Formula | Text |
| Emergency changes with PIR completed | Text (e.g., "100%") | Text (formula) | Formula | Text |
| Emergency changes leading to incidents | Text (e.g., "<10%") | Text | Formula | Text |
| Retrospective CAB review completion | Text (e.g., "100%") | Text | Formula | Text |
| False emergency declarations | Text (e.g., "<5%") | Text | Formula | Text |
| Emergency change success rate | Text (e.g., ">90%") | Text | Formula | Text |

### E-CAB (Emergency Change Advisory Board) (Rows 44-55)

| E-CAB Aspect | Configuration | Details | Documented | Evidence |
|-------------|--------------|---------|------------|----------|
| E-CAB Member Roles | Text (list of roles) | Text (names if applicable, or "per on-call rotation") | Dropdown: ✅/⚠️/❌/📋 | Text |
| Minimum quorum | Number | Text (e.g., "3 of 5 members") | Dropdown | Text |
| Convening method | Dropdown: Conference Call/Video/IM Group/Emergency Hotline/Other | Text | Dropdown | Text |
| Availability requirement | Text (e.g., "24/7 on-call rotation") | Text | Dropdown | Text |
| Decision authority | Text (e.g., "IT Ops Manager has final say") | Text | Dropdown | Text |
| Documentation requirements | Text | Text | Dropdown | Text |
| Escalation if E-CAB unavailable | Text | Text | Dropdown | Text |

---

## Sheet 5: Change_Risk_Classification

### Purpose
Document the risk classification matrix and assessment methodology.

### Header Section
**Row 1:** "CHANGE RISK CLASSIFICATION MATRIX"  
**Row 2:** "Risk = Impact Ã- Likelihood methodology"

### Impact Level Definitions (Rows 4-12)

| Impact Level | User Count Affected | Service Downtime Potential | Recovery Time | Data Loss Risk | Financial Impact | Documented | Evidence |
|--------------|-------------------|-------------------------|---------------|----------------|------------------|------------|----------|
| Low | Dropdown: <10 users/10-50/50-100/Other | Dropdown: <15 min/15-60 min/1-2 hours/Other | Text (e.g., "<15 min") | Dropdown: None/Minimal/Moderate/High | Text (e.g., "<€1,000") | Dropdown: ✅/⚠️/❌/📋 | Text |
| Medium | Dropdown | Dropdown | Text | Dropdown | Text | Dropdown | Text |
| High | Dropdown | Dropdown | Text | Dropdown | Text | Dropdown | Text |
| Critical | Dropdown: >1000 users/All users/Business-critical/Other | Dropdown: >8 hours/Irreversible/Business-critical/Other | Text (e.g., ">8 hours or permanent") | Dropdown | Text (e.g., ">€100,000") | Dropdown | Text |

### Likelihood Level Definitions (Rows 14-20)

| Likelihood Level | Failure Probability | Complexity | Dependencies | Testing Maturity | Historical Success Rate | Documented | Evidence |
|-----------------|-------------------|------------|--------------|-----------------|----------------------|------------|----------|
| Low | Text (e.g., "<10%") | Dropdown: Simple/Moderate/Complex/Very Complex | Text (e.g., "Single system, no external dependencies") | Dropdown: Extensively Tested/Well Tested/Limited Testing/Untested | Text (e.g., ">95%") | Dropdown: ✅/⚠️/❌/📋 | Text |
| Medium | Text (e.g., "10-30%") | Dropdown | Text | Dropdown | Text | Dropdown | Text |
| High | Text (e.g., ">30%") | Dropdown | Text | Dropdown | Text | Dropdown | Text |

### Risk Matrix (Impact Ã- Likelihood) (Rows 22-28)

|  | **Low Impact** | **Medium Impact** | **High Impact** | **Critical Impact** |
|--|----------------|-------------------|----------------|-------------------|
| **Low Likelihood** | LOW RISK (Green) | LOW RISK (Green) | MEDIUM RISK (Yellow) | HIGH RISK (Orange) |
| **Medium Likelihood** | LOW RISK (Green) | MEDIUM RISK (Yellow) | HIGH RISK (Orange) | CRITICAL RISK (Red) |
| **High Likelihood** | MEDIUM RISK (Yellow) | HIGH RISK (Orange) | CRITICAL RISK (Red) | CRITICAL RISK (Red) |

**Color Coding:**

- Green (C6EFCE): LOW RISK - Expedited approval possible
- Yellow (FFEB9C): MEDIUM RISK - Standard CAB review
- Orange (FFD966): HIGH RISK - Enhanced scrutiny, senior approval
- Red (FFC7CE): CRITICAL RISK - CISO/CIO approval required


### Risk Assessment Process (Rows 30-42)

| Process Step | Implemented | Process Description | Tool/Method | Responsible Role | Compliance | Evidence |
|-------------|-------------|---------------------|------------|------------------|------------|----------|
| Impact assessment performed | Dropdown: ✅ Always/⚠️ Sometimes/❌ Never | Text | Text (e.g., "Change request form, section 3") | Text | Dropdown: ✅/⚠️/❌ | Text |
| Likelihood assessment performed | Dropdown | Text | Text | Text | Dropdown | Text |
| Risk score calculated | Dropdown | Text (formula/method) | Text | Text | Dropdown | Text |
| Risk score documented | Dropdown | Text | Text | Text | Dropdown | Text |
| Risk mitigation identified | Dropdown | Text | Text | Text | Dropdown | Text |
| Residual risk assessed | Dropdown | Text | Text | Text | Dropdown | Text |
| Risk acceptance documented | Dropdown | Text | Text | Text | Dropdown | Text |
| Risk review at PIR | Dropdown | Text | Text | Text | Dropdown | Text |

### Risk Trends (Rows 44-52)

| Metric | Last Quarter | Current Quarter | Trend | Target | Status |
|--------|--------------|----------------|-------|--------|--------|
| % Low Risk Changes | Text (editable) | Text (editable) | Formula (↑/↓/→) | Text | Formula (Green/Yellow/Red) |
| % Medium Risk Changes | Text | Text | Formula | Text | Formula |
| % High Risk Changes | Text | Text | Formula | Text | Formula |
| % Critical Risk Changes | Text | Text | Formula | Text | Formula |
| Risk Assessment Accuracy | Text (e.g., "85%") | Text | Formula | Text (e.g., ">90%") | Formula |
| Changes failing due to risk | Text | Text | Formula | Text (e.g., "<5%") | Formula |

---

## Sheet 6: Change_Calendar_Management

### Purpose
Document change calendar management, blackout windows, and scheduling procedures.

### Header Section
**Row 1:** "CHANGE CALENDAR MANAGEMENT"  
**Row 2:** "Scheduling, blackout windows, and conflict detection"

### Change Window Definitions (Rows 4-15)

| Change Window | Days/Times | Applicable Change Types | Approval Required | Advance Notice | Documented | Evidence |
|--------------|------------|------------------------|-------------------|----------------|------------|----------|
| Standard Maintenance Window | Text (e.g., "Saturday 02:00-06:00 CET") | Dropdown: All/Standard Only/Normal Only/Emergency Only/Custom | Dropdown: Yes/No | Text (e.g., "5 business days") | Dropdown: ✅/⚠️/❌/📋 | Text |
| Business Hours (Restricted) | Text (e.g., "Monday-Friday 08:00-18:00 CET") | Dropdown | Dropdown | Text | Dropdown | Text |
| After-Hours Window | Text | Dropdown | Dropdown | Text | Dropdown | Text |
| Emergency Window | Text (e.g., "Anytime - as needed") | Dropdown: Emergency Only | Dropdown | Text (e.g., "Immediate") | Dropdown | Text |
| [Custom Window 1] | Text | Dropdown | Dropdown | Text | Dropdown | Text |
| [Custom Window 2] | Text | Dropdown | Dropdown | Text | Dropdown | Text |

### Blackout Periods (Rows 17-30)

| Blackout Period | Start Date | End Date | Reason | Affected Systems/Services | Exceptions Allowed | Exception Approver | Documented | Evidence |
|----------------|-----------|----------|--------|--------------------------|-------------------|-------------------|------------|----------|
| Year-End Freeze | Date (DD.MM.YYYY) | Date (DD.MM.YYYY) | Dropdown: Financial Close/Holiday Period/Peak Business/Audit/Other | Text | Dropdown: Yes/No/Emergency Only | Text (role) | Dropdown: ✅/⚠️/❌/📋 | Text |
| [Recurring - specify] | Date | Date | Dropdown | Text | Dropdown | Text | Dropdown | Text |

[12 rows for blackout periods - covering annual cycle]

### Change Calendar Procedures (Rows 32-45)

| Procedure | Implemented | Process Description | Tool/System | Responsible Role | Compliance | Evidence |
|-----------|-------------|---------------------|------------|------------------|------------|----------|
| Change calendar maintained | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Text (tool name) | Text | Dropdown: ✅/⚠️/❌ | Text |
| Changes scheduled in calendar | Dropdown | Text | Text | Text | Dropdown | Text |
| Conflict detection automated | Dropdown | Text | Text | Text | Dropdown | Text |
| Blackout periods enforced | Dropdown | Text | Text | Text | Dropdown | Text |
| Calendar visible to stakeholders | Dropdown | Text | Text | Text | Dropdown | Text |
| Calendar synchronization (if multiple systems) | Dropdown | Text | Text | Text | Dropdown | Text |
| Change window utilization tracked | Dropdown | Text | Text | Text | Dropdown | Text |
| Scheduling conflicts escalated | Dropdown | Text | Text | Text | Dropdown | Text |

### Conflict Detection & Resolution (Rows 47-58)

| Conflict Type | Detection Method | Resolution Process | Escalation Path | Documented | Evidence |
|--------------|------------------|-------------------|-----------------|------------|----------|
| Overlapping change windows | Dropdown: Automated/Manual/None | Text | Text | Dropdown: ✅/⚠️/❌/📋 | Text |
| Resource conflicts (same team) | Dropdown | Text | Text | Dropdown | Text |
| Dependency conflicts | Dropdown | Text | Text | Dropdown | Text |
| Blackout period violations | Dropdown | Text | Text | Dropdown | Text |
| Same system multiple changes | Dropdown | Text | Text | Dropdown | Text |

### Change Calendar Metrics (Rows 60-68)

| Metric | Target | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| Changes scheduled in advance (>5 days) | Text (e.g., ">80%") | Text | Formula | Text |
| Blackout period violations | Text (e.g., "<2%") | Text | Formula | Text |
| Emergency changes bypassing schedule | Text (e.g., "<5%") | Text | Formula | Text |
| Change window utilization | Text (e.g., "60-80%") | Text | Formula | Text |
| Conflicts detected and resolved | Text (e.g., "100%") | Text | Formula | Text |

---

## Sheet 7: Summary_Dashboard

### Purpose
Aggregate compliance metrics and identify gaps across all change type assessments.

### Header Section
**Row 1:** "CHANGE TYPES & CATEGORIES - SUMMARY DASHBOARD"  
**Row 2:** "Overall compliance status and key findings"

### Overall Compliance Summary (Rows 4-12)

| Assessment Area | Total Criteria | Defined | Partial | Not Defined | Compliance % | Status |
|-----------------|---------------|---------|---------|-------------|--------------|--------|
| Standard Changes Catalog | Formula | Formula | Formula | Formula | Formula | Formula: Green/Yellow/Red |
| Normal Changes Criteria | Formula | Formula | Formula | Formula | Formula | Formula |
| Emergency Change Procedures | Formula | Formula | Formula | Formula | Formula | Formula |
| Risk Classification Matrix | Formula | Formula | Formula | Formula | Formula | Formula |
| Change Calendar Management | Formula | Formula | Formula | Formula | Formula | Formula |
| **OVERALL TOTAL** | Formula | Formula | Formula | Formula | Formula | Formula |

### Policy Requirement Mapping (Rows 14-28)

| Policy Req ID | Requirement Summary | Status | Evidence Sheet | Evidence Row | Auditor Notes |
|--------------|---------------------|--------|----------------|--------------|---------------|
| REQ-CLASSIFY-001 | Standard changes catalog maintained | Formula: ✅/⚠️/❌ | Text | Text | Text (editable) |
| REQ-CLASSIFY-002 | Standard change pre-approval | Formula | Text | Text | Text |
| REQ-CLASSIFY-003 | Normal change assessment criteria | Formula | Text | Text | Text |
| REQ-CLASSIFY-004 | Emergency criteria defined | Formula | Text | Text | Text |
| REQ-CLASSIFY-005 | Risk-based categorization | Formula | Text | Text | Text |
| REQ-CLASSIFY-006 | Impact assessment methodology | Formula | Text | Text | Text |
| REQ-CLASSIFY-007 | Likelihood assessment methodology | Formula | Text | Text | Text |
| REQ-CLASSIFY-008 | Risk matrix documented | Formula | Text | Text | Text |
| REQ-CLASSIFY-009 | Change calendar management | Formula | Text | Text | Text |
| REQ-CLASSIFY-010 | Blackout periods defined | Formula | Text | Text | Text |
| REQ-CLASSIFY-011 | E-CAB procedures | Formula | Text | Text | Text |
| REQ-CLASSIFY-012 | Classification metrics tracked | Formula | Text | Text | Text |

### Change Distribution Analysis (Rows 30-38)

| Metric | Current | Target | Status | Notes |
|--------|---------|--------|--------|-------|
| Standard Changes (%) | Formula from Sheet 2 | Text (e.g., "40-60%") | Formula | Text |
| Normal Changes (%) | Formula | Text (e.g., "35-55%") | Formula | Text |
| Emergency Changes (%) | Formula | Text (e.g., "<5%") | Formula | Text |
| Total Active Standard Changes | Formula | Text | Formula | Text |
| Standard Changes Requiring Review | Formula | Text | Formula | Text |
| Classification Accuracy | Text (e.g., "Current: 92%") | Text (e.g., ">90%") | Formula | Text |

### Critical Findings (Rows 40-45)

| Finding Type | Count | Description |
|--------------|-------|-------------|
| Critical Gaps | Formula (count ❌) | Text area (auto-populate key gaps) |
| High-Priority Items | Formula (count ⚠️) | Text area |
| Planned Improvements | Formula (count 📋) | Text area |

### Audit Readiness Assessment (Rows 47-54)

| Criterion | Status | Notes |
|-----------|--------|-------|
| All change types clearly defined | Formula: ✅/⚠️/❌ | Text |
| Standard changes catalog complete | Formula | Text |
| Risk classification methodology documented | Formula | Text |
| Emergency procedures documented | Formula | Text |
| Evidence available for all criteria | Formula | Text |
| Compliance ≥70% | Formula | Text |
| **OVERALL AUDIT READINESS** | Formula | Text |

---

## Sheet 8: Evidence_Register

### Purpose
Centralized evidence repository linking to all supporting documentation.

### Header Section
**Row 1:** "EVIDENCE REGISTER"  
**Row 2:** "Document all evidence supporting this assessment"

### Evidence Inventory (Rows 4-103, 100 rows)

| Evidence ID | Evidence Type | Description | Related Sheet/Requirement | Location/Path | Date Collected | Collected By | Verification Status | Auditor Notes |
|-------------|---------------|-------------|--------------------------|---------------|----------------|--------------|-------------------|---------------|
| EV-001 | Dropdown: Catalog/Procedure/Criteria Doc/Risk Matrix/Calendar/Meeting Minutes/Metrics Report/Approval Record/Training Material/Other | Text | Dropdown: (all sheets + REQ-IDs) | Text | Date (DD.MM.YYYY) | Text | Dropdown: ✅ Verified/⚠️ Pending/❌ Not Verified | Text |

[100 rows for evidence tracking with alternating row colors for readability]

**Column Widths:**

- Evidence ID: 12
- Evidence Type: 18
- Description: 40
- Related Sheet/Requirement: 25
- Location/Path: 30
- Date Collected: 15
- Collected By: 20
- Verification Status: 18
- Auditor Notes: 30


---

## Sheet 9: Approval_Sign_Off

### Purpose
Formal approval workflow for completed assessment.

### Assessment Summary Section (Rows 3-10)
```
Assessment Document:        ISMS-IMP-A.8.32.2 - Change Types & Categories Assessment
Assessment Period:          [USER INPUT - date range]
Assessment Scope:           [USER INPUT - text]
Overall Compliance Rate:    [Formula from Summary_Dashboard]
Critical Gaps:              [Formula from Summary_Dashboard]
Audit Readiness:            [Formula from Summary_Dashboard]
Assessment Status:          [Dropdown: ✅ Final/⚠️ Requires Remediation/📋 Draft/❌ Re-assessment Required]
```

### Assessment Completed By (Rows 12-20)
```
Name:               [USER INPUT]
Role/Title:         [USER INPUT]
Department:         [USER INPUT]
Email:              [USER INPUT]
Phone:              [USER INPUT]
Date Completed:     [USER INPUT - date picker, format DD.MM.YYYY]
Signature:          [USER INPUT]
```

### Reviewed By - Change Manager (Rows 22-30)
```
Name:                   [USER INPUT]
Role/Title:             [USER INPUT]
Review Date:            [USER INPUT - date picker, format DD.MM.YYYY]
Review Notes:           [Text area - merged cells]
Recommendation:         [Dropdown: ✅ Approve/⚠️ Approve with Conditions/❌ Reject/📋 Require Rework]
Conditions (if any):    [Text area]
Signature:              [USER INPUT]
```

### Approved By - CISO or IT Operations Manager (Rows 32-40)
```
Name:                   [USER INPUT]
Role/Title:             [USER INPUT]
Approval Date:          [USER INPUT - date picker, format DD.MM.YYYY]
Approval Decision:      [Dropdown: ✅ Approved/⚠️ Approved with Conditions/❌ Rejected]
Conditions/Notes:       [Text area]
Signature:              [USER INPUT]
```

### Next Review Details (Rows 42-48)
```
Next Review Date:               [Date - auto-calculate +3 months from Approval Date]
Review Responsible:             [USER INPUT]
Special Considerations:         [Text area]
Regulatory Review Required:     [Dropdown: Yes/No/To Be Determined]
External Audit Scheduled:       [Date]
```

---

## Cell Styling Reference

### Header Styles

- **Main Header (Row 1):** Font: Calibri 14pt bold white, Fill: 003366 (dark blue), Alignment: centered/wrapped, Height: 40px
- **Subheader (Row 2):** Font: Calibri 11pt bold white, Fill: 4472C4 (medium blue), Alignment: centered/wrapped, Height: 25px
- **Section Header:** Font: Calibri 11pt bold white, Fill: 4472C4 (light blue), Alignment: center, Height: 20px
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (light gray), Alignment: centered/wrapped, Border: thin all sides


### Input Cell Styles

- **Editable (User Input):** Fill: FFFFCC (light yellow), Border: thin black, Alignment: left/wrap
- **Calculated/Formula:** Fill: E0E0E0 (light gray), Border: thin black, Protection: locked
- **Dropdown:** Fill: FFFFCC (light yellow), Border: thin black, Data validation applied


### Status Color Coding

- **✅ Defined/Compliant:** C6EFCE (light green)
- **⚠️ Partial/Requires Attention:** FFEB9C (light yellow)
- **❌ Not Defined/Non-Compliant:** FFC7CE (light red)
- **📋 Planned:** B4C7E7 (light blue)
- **N/A:** F2F2F2 (light gray)


### Risk Level Colors

- **LOW RISK:** C6EFCE (green)
- **MEDIUM RISK:** FFEB9C (yellow)
- **HIGH RISK:** FFD966 (orange)
- **CRITICAL RISK:** FFC7CE (red)


---

## Freeze Panes

- **All assessment sheets:** Freeze at row 4 (headers remain visible during scrolling)
- **Standard Changes Catalog:** Freeze at row 5 (includes column headers)
- **Evidence Register:** Freeze at row 5
- **Approval Sign-Off:** Freeze at row 3


---

## File Naming Convention

**Format:** `ISMS_A_8_32_2_Change_Types_Categories_Assessment_YYYYMMDD.xlsx`

**Examples:**

- `ISMS_A_8_32_2_Change_Types_Categories_Assessment_20260115.xlsx`
- `ISMS_A_8_32_2_Change_Types_Categories_Assessment_20260401_FINAL.xlsx`


---

## Quarterly Review Cycle

### Review Checklist
1. ☐ Review standard changes catalog (additions/retirements)
2. ☐ Verify normal change criteria remain appropriate
3. ☐ Review emergency change metrics (<5% target)
4. ☐ Validate risk classification methodology
5. ☐ Update change calendar and blackout periods
6. ☐ Recalculate compliance metrics
7. ☐ Add new evidence entries
8. ☐ Address any identified gaps
9. ☐ Update approval sign-off with quarterly review notes
10. ☐ Distribute updated assessment to stakeholders

### Triggers for Ad-Hoc Review

- Addition/retirement of standard changes
- Emergency change threshold exceeded (>5%)
- Change failure rate increase
- Risk assessment methodology changes
- Organizational restructuring affecting approvals
- Internal/external audit findings
- Regulatory requirement changes


---

## Integration Points

### Related ISMS Documents

- **ISMS-POL-A.8.32-S2.2:** Change Classification Requirements (12 requirements)
- **ISMS-POL-A.8.32-S5.C:** Risk Assessment Matrix
- **ISMS-IMP-A.8.32.1:** Change Process Assessment
- **ISMS-IMP-A.8.32.3:** Environment Separation Assessment
- **ISMS-IMP-A.8.32.4:** Testing & Validation Assessment
- **ISMS-IMP-A.8.32.5:** Compliance Dashboard (consolidates this data)


### Related ISO 27001:2022 Controls

- **Control 5.7:** Threat intelligence (risk assessment inputs)
- **Control 8.29:** Configuration management (change classification consistency)
- **Control 8.31:** Separation of environments (standard vs. normal change criteria)


### External Integrations

- **Risk Register:** Link change risk classifications to organizational risk register
- **Incident Management:** Track emergency changes triggered by incidents
- **Change Management System:** Standard changes catalog synchronized
- **Metrics Dashboard:** Change distribution and classification accuracy metrics
- **Training Register:** Track training on change classification


### Audit Trail Requirements

- All change types documented with approval dates
- Standard changes catalog with annual review dates
- Risk classification methodology documented and versioned
- Emergency change metrics tracked quarterly
- Classification accuracy measured and trended
- Evidence maintained for all classification decisions


---

**END OF SPECIFICATION**

---

*"Cryptography is a mix of math, computer science, and paranoia."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-01-31 -->
