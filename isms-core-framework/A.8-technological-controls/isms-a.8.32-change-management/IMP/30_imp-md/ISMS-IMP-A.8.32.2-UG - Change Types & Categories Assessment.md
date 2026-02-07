**ISMS-IMP-A.8.32.2-UG - Change Types & Categories Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.32.2-UG |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.32.2-TG.

---



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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
