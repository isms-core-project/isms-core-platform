<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.37.2-UG:framework:UG:a.5.37.2 -->
**ISMS-IMP-A.5.37.2-UG - Procedure Quality Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.37

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.2-UG |
| **Title** | Procedure Quality Assessment |
| **Control Reference** | ISO/IEC 27001:2022 A.5.37 |
| **Control Name** | Documented Operating Procedures |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |
| **Framework Version** | 1.0 |

---

## Table of Contents

1. [USER COMPLETION GUIDE](#user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Quality Framework](#14-quality-framework)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 Quality Scoring Methodology](#17-quality-scoring-methodology)
   - [1.8 Quality Checklist Elements](#18-quality-checklist-elements)
   - [1.9 Evidence Collection](#19-evidence-collection)
   - [1.10 Common Pitfalls](#110-common-pitfalls)
   - [1.11 Quality Checklist](#111-quality-checklist)
   - [1.12 Review and Approval](#112-review-and-approval)
   - [1.13 Improvement Action Management](#113-improvement-action-management)
   - [1.14 Related Controls](#114-related-controls)
2. [TECHNICAL SPECIFICATION](#technical-specification) *(see companion TG document)*
   - [2.1 Workbook Architecture](#21-workbook-architecture)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Data Validations](#23-data-validations)
   - [2.4 Conditional Formatting](#24-conditional-formatting)
   - [2.5 Formula Specifications](#25-formula-specifications)
   - [2.6 Cell Styling Standards](#26-cell-styling-standards)
   - [2.7 Generator Script Reference](#27-generator-script-reference)

---

---

## Assessment Overview

### Purpose

This workbook assesses the quality and completeness of documented operating procedures. While ISMS-IMP-A.5.37.1 inventories procedures, this assessment evaluates whether each procedure meets quality standards for clarity, completeness, accuracy, usability, and maintainability.

The Procedure Quality Assessment serves as:

- **Quality Measurement**: Systematic evaluation of procedure quality against defined standards
- **Improvement Driver**: Identification of specific improvements needed for each procedure
- **Trend Tracking**: Monitoring quality improvements over time
- **Prioritisation Tool**: Focusing remediation efforts on highest-risk procedure gaps
- **Compliance Evidence**: Demonstrating ongoing procedure quality management to auditors

Having an inventory of procedures (A.5.37.1) is necessary but not sufficient. Procedures must be of sufficient quality to be usable in operations. A poorly written procedure that cannot be followed effectively is nearly as risky as having no procedure at all.

### Scope

This assessment covers the following components:

**In Scope:**
- Quality assessment of all documented operating procedures
- Clarity and readability evaluation
- Completeness verification against best practice checklists
- Accuracy verification against current systems and processes
- Usability assessment for target audience
- Maintainability evaluation for ongoing updates
- Quality scoring and rating
- Improvement action identification and tracking
- Quality trend analysis over time

**Out of Scope:**
- Procedure inventory management (covered in ISMS-IMP-A.5.37.1)
- Procedure review scheduling (covered in ISMS-IMP-A.5.37.3)
- Compliance dashboards and metrics aggregation (covered in ISMS-IMP-A.5.37.4)
- Actual procedure content creation or rewriting
- Technical validation of procedure steps (subject matter expert responsibility)

### Business Value

Effective procedure quality assessment delivers:

| Value Area | Benefit |
|------------|---------|
| **Operational Reliability** | High-quality procedures reduce errors and incidents |
| **Training Effectiveness** | Clear procedures accelerate staff competency |
| **Knowledge Transfer** | Well-documented procedures enable smooth handovers |
| **Audit Confidence** | Quality evidence demonstrates mature procedure management |
| **Risk Reduction** | Identifying and fixing poor procedures before they cause problems |
| **Continuous Improvement** | Systematic quality tracking drives ongoing enhancement |

### Assessment Frequency

| Activity | Frequency | Responsible Party |
|----------|-----------|-------------------|
| Critical Procedure Quality Review | Semi-annual | Information Security Manager |
| Full Quality Assessment | Annual | Information Security Manager |
| New Procedure Quality Check | Within 30 days of creation | Procedure Owner |
| Post-Incident Quality Review | After procedure-related incidents | ISM/Procedure Owner |
| Improvement Action Review | Monthly | ISMS Administrator |

---

## Control Requirements

### ISO 27001:2022 Control A.5.37

> *"Operating procedures for information processing facilities should be documented and made available to personnel who need them."*

**Control Type:** Preventive
**Security Properties:** Confidentiality, Integrity, Availability
**Cybersecurity Concepts:** Protect
**Operational Capabilities:** Asset Management, Operations Security

### Quality Implications

While Control A.5.37 requires procedures to be "documented and made available," effective implementation requires that procedures be of sufficient quality to serve their purpose. ISO 27002 guidance elaborates that procedures should be:

- **Understandable** by the intended audience
- **Complete** enough to perform the operation
- **Current** reflecting the actual system state
- **Actionable** providing practical guidance

### What Auditors Look For

ISO 27001 auditors examining procedure quality will verify:

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Procedure Clarity** | Procedures understandable by target audience |
| **Content Completeness** | All necessary steps documented |
| **Operational Accuracy** | Procedures match current systems |
| **Practical Usability** | Procedures can be followed in practice |
| **Regular Review** | Evidence of quality assessments and improvements |
| **Quality Standards** | Defined criteria for procedure quality |
| **Improvement Process** | Systematic approach to enhancing procedures |

### Common Audit Questions

Auditors frequently ask:

1. *"How do you ensure procedures are of sufficient quality?"*
2. *"Show me how you assess procedure quality."*
3. *"What criteria do you use for procedure quality?"*
4. *"How do you track and improve procedure quality over time?"*
5. *"What happens when a procedure is found to be inadequate?"*
6. *"How do you prioritise procedure improvement efforts?"*

---

## Prerequisites

### Before Starting This Assessment

Complete the following prerequisites to ensure successful assessment completion:

#### Required Access

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| Procedure Inventory (A.5.37.1) | Read | Reference procedure list |
| Procedure Documents | Read | Review procedure content |
| ISMS Evidence Library | Write | Upload evidence and completed workbook |
| Previous Quality Assessments | Read | Trend comparison |

#### Required Information

| Information | Source | Why Needed |
|-------------|--------|------------|
| Procedure Inventory | ISMS-IMP-A.5.37.1 | List of procedures to assess |
| Procedure Documents | Document Repository | Content to evaluate |
| Target Audience Definitions | HR/Department | Assess clarity for audience |
| Current System Documentation | IT Operations | Verify accuracy |
| Previous Quality Scores | Previous assessments | Trend analysis |
| Incident Reports | ITSM | Identify procedure-related issues |

#### Required Approvals

| Approval | Approver | When Needed |
|----------|----------|-------------|
| Assessment Scope | Information Security Manager | Before starting |
| Procedure Access | Procedure Owners | During assessment |
| Quality Standards | CISO | Before first assessment |

#### Prerequisite Checklist

Before proceeding, verify:

- [ ] Procedure inventory (A.5.37.1) is current and complete
- [ ] Access to all procedures confirmed
- [ ] Quality criteria understood and documented
- [ ] Assessment schedule agreed with stakeholders
- [ ] Previous assessment results available (if applicable)
- [ ] Assessor training completed (if new assessor)
- [ ] Subject matter experts available for accuracy verification

---

## Quality Framework

### Quality Dimensions

Procedure quality is assessed across five equally-weighted dimensions:

| Dimension | Weight | Description | Key Questions |
|-----------|:------:|-------------|---------------|
| **Clarity** | 20% | Can be understood by target audience | Is the language appropriate? Are steps clear? |
| **Completeness** | 20% | Covers all necessary steps and scenarios | Are all scenarios covered? Any gaps? |
| **Accuracy** | 20% | Reflects current systems and processes | Does it match reality? |
| **Usability** | 20% | Practical to follow in operations | Can it actually be followed? |
| **Maintainability** | 20% | Easy to update when changes occur | Is it structured for updates? |

### Dimension Definitions

#### Clarity (20%)

**Definition:** The procedure can be understood by its intended audience without requiring additional explanation.

**Assessment Criteria:**
- Language appropriate for audience technical level
- Instructions unambiguous and precise
- Technical terms defined or commonly understood
- Logical flow and structure
- Visual aids where beneficial

**Scoring Guidance:**
| Score | Description |
|:-----:|-------------|
| 5 | Crystal clear; any qualified person can follow without questions |
| 4 | Very clear; minor ambiguities that don't impede understanding |
| 3 | Reasonably clear; some sections require interpretation |
| 2 | Unclear in places; multiple interpretations possible |
| 1 | Confusing; significant clarification needed |
| 0 | Incomprehensible or missing |

#### Completeness (20%)

**Definition:** The procedure covers all necessary steps, decision points, error handling, and edge cases.

**Assessment Criteria:**
- All steps documented from start to finish
- Decision points and branches covered
- Error handling and escalation defined
- Prerequisites clearly stated
- Expected outcomes specified
- Rollback/recovery procedures included

**Scoring Guidance:**
| Score | Description |
|:-----:|-------------|
| 5 | Comprehensive; all scenarios covered including edge cases |
| 4 | Complete; main scenarios covered, minor gaps in edge cases |
| 3 | Adequate; covers normal operation but gaps in error handling |
| 2 | Incomplete; missing significant steps or scenarios |
| 1 | Seriously incomplete; major gaps in coverage |
| 0 | Missing or skeleton only |

#### Accuracy (20%)

**Definition:** The procedure accurately reflects current systems, processes, and requirements.

**Assessment Criteria:**
- System names and versions current
- Screenshots and diagrams accurate
- Commands and parameters valid
- Referenced documents exist and are current
- Contact information accurate
- Process reflects actual current practice

**Scoring Guidance:**
| Score | Description |
|:-----:|-------------|
| 5 | Fully accurate; reflects current state exactly |
| 4 | Mostly accurate; minor details outdated |
| 3 | Reasonably accurate; some updates needed |
| 2 | Partially inaccurate; significant updates required |
| 1 | Largely inaccurate; major rewrite needed |
| 0 | Completely outdated or missing |

#### Usability (20%)

**Definition:** The procedure is practical to follow during actual operations.

**Assessment Criteria:**
- Steps are actionable and specific
- Information organised for operational use
- Quick reference sections for common tasks
- Emergency procedures easily accessible
- Time estimates realistic
- Resource requirements specified

**Scoring Guidance:**
| Score | Description |
|:-----:|-------------|
| 5 | Highly usable; excellent operational utility |
| 4 | Very usable; practical with minor inconveniences |
| 3 | Usable; requires some interpretation or searching |
| 2 | Difficult to use; significant navigation or clarity issues |
| 1 | Very difficult; barely usable in practice |
| 0 | Unusable or missing |

#### Maintainability (20%)

**Definition:** The procedure is structured to facilitate easy updates when changes occur.

**Assessment Criteria:**
- Modular structure separating components
- Version control implemented
- Change history maintained
- References to external documents (not embedded copies)
- Clear ownership for updates
- Review cycle appropriate

**Scoring Guidance:**
| Score | Description |
|:-----:|-------------|
| 5 | Excellent structure; updates straightforward |
| 4 | Good structure; updates manageable |
| 3 | Adequate structure; updates require some effort |
| 2 | Poor structure; updates difficult |
| 1 | Very poor; updates require major restructuring |
| 0 | No structure; complete rewrite easier than update |

### Quality Rating Thresholds

| Overall Score | Rating | Interpretation | Action |
|:-------------:|--------|----------------|--------|
| ≥4.5 | Excellent | Best practice quality | Maintain; use as exemplar |
| 3.5-4.49 | Good | Meets quality standards | Minor improvements only |
| 2.5-3.49 | Adequate | Minimum acceptable | Schedule improvements |
| 1.5-2.49 | Needs Improvement | Below acceptable standards | Priority remediation |
| <1.5 | Poor | Unacceptable quality | Urgent rewrite required |

---

## Completion Walkthrough

### Step 1: Review Instructions Sheet

**Time allocation:** 10-15 minutes

1. Read the assessment methodology
2. Understand the quality dimensions and scoring
3. Note the checklist items to evaluate
4. Review assessment schedule and scope
5. Check workbook version matches this specification

### Step 2: Complete Quality_Assessment Sheet

**Time allocation:** 30-60 minutes per procedure

For each procedure being assessed, complete the following fields:

#### Column A: Procedure_ID

- **Format:** From ISMS-IMP-A.5.37.1 Procedure Inventory
- **Example:** SOP-IT-001
- **Rules:** Must match valid Procedure_ID from inventory
- **Guidance:** Use dropdown to select from inventory

#### Column B: Procedure_Name

- **Format:** Auto-populated from inventory lookup
- **Example:** Daily Backup Execution Procedure
- **Rules:** Read-only field
- **Guidance:** Verify correct procedure selected

#### Column C: Assessment_Date

- **Format:** DD.MM.YYYY (Swiss date format)
- **Example:** 15.01.2026
- **Rules:** Date assessment was conducted
- **Guidance:** Must be current assessment, not procedure date

#### Column D: Assessor

- **Format:** Full name
- **Example:** Maria Schmidt
- **Rules:** Person who conducted quality review
- **Guidance:** Assessor should have appropriate expertise

#### Column E: Clarity_Score

- **Format:** Number 0-5 (one decimal place)
- **Example:** 4.0
- **Rules:** Score per Clarity dimension criteria
- **Guidance:** Consider target audience understanding

#### Column F: Completeness_Score

- **Format:** Number 0-5 (one decimal place)
- **Example:** 3.5
- **Rules:** Score per Completeness dimension criteria
- **Guidance:** Check all steps, error handling, edge cases

#### Column G: Accuracy_Score

- **Format:** Number 0-5 (one decimal place)
- **Example:** 4.5
- **Rules:** Score per Accuracy dimension criteria
- **Guidance:** Verify against current systems; involve SME if needed

#### Column H: Usability_Score

- **Format:** Number 0-5 (one decimal place)
- **Example:** 3.0
- **Rules:** Score per Usability dimension criteria
- **Guidance:** Consider if you could actually follow this procedure

#### Column I: Maintainability_Score

- **Format:** Number 0-5 (one decimal place)
- **Example:** 4.0
- **Rules:** Score per Maintainability dimension criteria
- **Guidance:** Consider structure, modularity, version control

#### Column J: Overall_Score

- **Format:** Calculated (weighted average)
- **Example:** 3.8
- **Rules:** Formula: (E+F+G+H+I)/5
- **Guidance:** Auto-calculated field

#### Column K: Quality_Rating

- **Format:** Calculated (from thresholds)
- **Example:** Good
- **Rules:** Based on Overall_Score thresholds
- **Guidance:** Auto-calculated field

#### Column L: Priority_Improvements

- **Format:** Text (comma-separated)
- **Example:** Error handling, Screenshots
- **Rules:** Key areas needing improvement
- **Guidance:** Focus on lowest-scoring dimensions

#### Column M: Findings

- **Format:** Free text
- **Example:** Procedure lacks rollback steps for failed operations
- **Rules:** Maximum 500 characters
- **Guidance:** Specific, actionable findings

#### Column N: Next_Review

- **Format:** Calculated (based on rating)
- **Example:** 15.07.2026
- **Rules:** Excellent=365d, Good=180d, Adequate=90d, Poor=30d
- **Guidance:** Auto-calculated field

### Step 3: Complete Quality_Checklist Sheet

**Time allocation:** 20-40 minutes per procedure

For thorough quality assessment, apply the detailed checklist:

1. Select Procedure_ID from dropdown
2. For each checklist item, assess status (Pass/Partial/Fail/N/A)
3. Document specific findings
4. Provide improvement recommendations
5. Link findings to dimension scores in Quality_Assessment

### Step 4: Complete Improvement_Actions Sheet

**Time allocation:** 15-30 minutes per low-scoring procedure

For procedures rated Adequate or below, create improvement actions:

1. Generate Action_ID using format ACT-A.5.37.2-NNN
2. Link to Procedure_ID
3. Identify quality dimension affected
4. Describe the specific issue
5. Define required action
6. Assign owner
7. Set priority based on procedure criticality and quality gap
8. Set target date per priority SLA
9. Track status through to completion

### Step 5: Complete Trend_Analysis Sheet

**Time allocation:** 30-60 minutes (quarterly)

Update historical quality trends:

1. Add row for current assessment period
2. Calculate averages across all assessed procedures
3. Count procedures by rating
4. Calculate improvement percentage from previous period
5. Identify patterns and systematic issues

### Step 6: Complete Evidence_Register Sheet

**Time allocation:** 30-60 minutes

Document assessment evidence:

1. Generate Evidence_ID using format EVD-A.5.37.2-NNN
2. Describe evidence type (assessment form, procedure copy, etc.)
3. Link to Procedure_ID
4. Record storage location
5. Note collection date and collector

### Step 7: Complete Approval_SignOff Sheet

**Time allocation:** 15-30 minutes

Obtain required authorisations:

1. Complete assessor information
2. Enter assessment completion date
3. Route to ISM for sign-off
4. Obtain final approval

---

## Quality Scoring Methodology

### Scoring Process

#### Step 1: Read the Procedure

- Read the entire procedure before scoring
- Note initial impressions on each dimension
- Identify potential issues

#### Step 2: Apply Checklist

- Use Quality_Checklist sheet for detailed evaluation
- Mark each item as Pass/Partial/Fail/N/A
- Document specific findings

#### Step 3: Verify Accuracy

- Cross-reference with current systems
- Consult subject matter experts if needed
- Test procedure steps if possible

#### Step 4: Score Each Dimension

- Apply scoring guidance for each dimension
- Consider checklist results
- Be consistent across procedures

#### Step 5: Document Findings

- Specific, actionable findings
- Prioritise improvement areas
- Estimate effort for remediation

### Scoring Calibration

To ensure consistent scoring across assessors:

| Calibration Method | Frequency | Participants |
|-------------------|-----------|--------------|
| Sample procedure scoring | Before first assessment | All assessors |
| Score comparison | Monthly | Assessor group |
| Scoring guidance review | Annual | ISM + assessors |
| Inter-rater reliability | Quarterly | Randomly paired assessors |

### Score Adjustment Guidelines

| Situation | Adjustment |
|-----------|------------|
| N/A items | Exclude from dimension if >50% N/A |
| Mixed quality | Weight toward operational impact |
| New procedures | Consider as draft; note in findings |
| Legacy procedures | Note legacy status; focus on key improvements |

---

## Quality Checklist Elements

### Document Structure Checklist

| Check Item | Pass Criteria |
|------------|---------------|
| Document ID and title present | Clearly visible on first page |
| Version control information | Version number and date present |
| Owner and approver identified | Names/roles documented |
| Last review date documented | Date visible and current |
| Scope clearly defined | What the procedure covers/doesn't cover |
| Prerequisites listed | Pre-conditions for procedure execution |
| Related documents referenced | Links to related procedures/policies |

### Content Quality Checklist

| Check Item | Pass Criteria |
|------------|---------------|
| Purpose statement clear | Why the procedure exists |
| Step-by-step instructions | Numbered, sequential steps |
| Decision trees/flowcharts | Complex logic visualised |
| Screenshots/diagrams | Visual aids where helpful |
| Error handling documented | What to do when things go wrong |
| Escalation procedures defined | When and who to escalate to |
| Contact information current | Valid contacts for support |
| Glossary of terms | Technical terms defined (if needed) |

### Operational Elements Checklist

| Check Item | Pass Criteria |
|------------|---------------|
| Pre-execution checks defined | Verification before starting |
| Execution steps numbered | Clear sequence |
| Verification steps included | How to confirm success |
| Expected outcomes stated | What success looks like |
| Rollback procedures documented | How to undo if needed |
| Recovery steps included | How to recover from failure |
| Time estimates provided | How long procedure takes |
| Resource requirements listed | What's needed to execute |

---

## Evidence Collection

### Evidence Requirements

The following evidence must be collected and maintained:

| Evidence Type | Description | Retention Period | Storage Location |
|---------------|-------------|------------------|------------------|
| **Assessment Workbooks** | Completed quality assessments | 7 years | ISMS Evidence Library |
| **Procedure Copies** | Procedure versions assessed | Life of procedure + 7 years | ISMS Evidence Library |
| **Checklist Results** | Detailed checklist evaluations | 7 years | ISMS Evidence Library |
| **Improvement Records** | Action completion evidence | 7 years | ISMS Evidence Library |
| **Trend Reports** | Quality trend analyses | 7 years | ISMS Evidence Library |

### Evidence Collection Process

#### Step 1: Assessment Documentation

1. Complete all assessment fields
2. Save workbook with date suffix
3. Export PDF of Quality_Assessment sheet
4. Store in ISMS Evidence Library

#### Step 2: Procedure Copies

1. Save copy of assessed procedure version
2. Name with Procedure_ID and assessment date
3. Store with assessment evidence

#### Step 3: Improvement Evidence

1. Document improvement actions completed
2. Collect evidence of changes made
3. Link to original assessment

### Evidence Storage Standards

**Naming Convention:**
```
EVD-A.5.37.2_[EvidenceType]_[ProcedureID]_[YYYYMMDD].[ext]
```

**Examples:**
- `EVD-A.5.37.2_Assessment_SOP-IT-001_20260115.xlsx`
- `EVD-A.5.37.2_Checklist_SOP-SEC-003_20260115.pdf`
- `EVD-A.5.37.2_Improvement_ACT-001_20260215.pdf`

**Storage Structure:**
```
ISMS Evidence Library/
└── A.5.37-Documented-Procedures/
    ├── Quality-Assessments/
    │   └── [Assessment period]/
    ├── Checklists/
    ├── Improvements/
    └── Trends/
```

---

## Common Pitfalls

Avoid these common mistakes when assessing procedure quality:

### Assessment Process Pitfalls

❌ **MISTAKE**: Assessing procedures without reading them fully
✅ **CORRECT**: Read the entire procedure before scoring any dimension; initial impressions often change after full review; understanding the complete procedure is essential for accurate scoring

❌ **MISTAKE**: Scoring based on document appearance rather than content
✅ **CORRECT**: Focus on whether the procedure can be followed successfully, not on formatting aesthetics; a well-formatted procedure that can't be followed is still poor quality

❌ **MISTAKE**: Not involving subject matter experts for accuracy verification
✅ **CORRECT**: Accuracy scoring requires verification against current systems; involve SMEs who know the actual process; assessors cannot verify accuracy in areas outside their expertise

❌ **MISTAKE**: Assessing all procedures in one sitting, leading to fatigue errors
✅ **CORRECT**: Limit assessments to 3-5 procedures per session; maintain fresh perspective for each procedure; schedule breaks between assessments

### Scoring Pitfalls

❌ **MISTAKE**: Inconsistent scoring standards across assessors
✅ **CORRECT**: Conduct calibration exercises before assessments; use detailed scoring guidance; compare scores periodically; establish inter-rater reliability checks

❌ **MISTAKE**: Avoiding extreme scores (always scoring 3-4)
✅ **CORRECT**: Use the full scoring range; excellent procedures deserve 5s; poor procedures need 1s to drive improvement; central tendency bias masks real quality differences

❌ **MISTAKE**: Not documenting reasoning behind scores
✅ **CORRECT**: Record specific findings supporting each dimension score; findings enable remediation; documented reasoning allows score validation

❌ **MISTAKE**: Scoring accuracy without verifying against current systems
✅ **CORRECT**: Actually check that system names, screenshots, and commands are current; outdated accuracy reflects real risk; verification requires system access

### Improvement Pitfalls

❌ **MISTAKE**: Identifying issues without creating improvement actions
✅ **CORRECT**: Every procedure rated Adequate or below should have improvement actions; findings without actions don't drive improvement; track all issues to resolution

❌ **MISTAKE**: Generic improvement actions (e.g., "improve clarity")
✅ **CORRECT**: Specific, actionable improvements (e.g., "add error handling for database connection failure scenario"); vague actions cannot be implemented or verified

❌ **MISTAKE**: Not setting priorities based on procedure criticality
✅ **CORRECT**: Critical procedure with Poor quality is urgent; low-priority procedure with Adequate quality can wait; prioritise based on risk, not just quality score

❌ **MISTAKE**: Improvement actions assigned but not tracked
✅ **CORRECT**: Regular review of improvement action status; escalate overdue actions; verify completion before closing; track completion rates

### Quality Framework Pitfalls

❌ **MISTAKE**: Changing scoring criteria between assessments
✅ **CORRECT**: Maintain consistent criteria to enable trend analysis; document any changes; re-baseline if criteria change significantly

❌ **MISTAKE**: Not tracking trends over time
✅ **CORRECT**: Quality improvement should be measurable; trend analysis identifies systematic issues; historical data demonstrates improvement programme effectiveness

❌ **MISTAKE**: Quality assessment disconnected from procedure lifecycle
✅ **CORRECT**: Integrate quality assessment with procedure creation and review processes; new procedures should meet quality standards before approval; updates should maintain or improve quality

❌ **MISTAKE**: Treating quality assessment as a one-time exercise
✅ **CORRECT**: Quality is ongoing; procedures degrade over time as systems change; regular reassessment is essential; use rating-based review cycles

---

## Quality Checklist

Before submitting the completed assessment, verify all items:

### Assessment Completeness Checks

- [ ] All procedures in scope have been assessed
- [ ] Each procedure has scores for all five dimensions
- [ ] Overall scores and ratings calculated correctly
- [ ] Priority improvements identified for each procedure
- [ ] Findings documented for low-scoring procedures

### Checklist Completion Checks

- [ ] Quality_Checklist completed for assessed procedures
- [ ] All applicable items marked Pass/Partial/Fail
- [ ] N/A items documented with justification
- [ ] Findings linked to dimension scores
- [ ] Recommendations provided for Fail items

### Improvement Action Checks

- [ ] Actions created for Adequate or below procedures
- [ ] All actions have assigned owners
- [ ] Target dates set per priority SLA
- [ ] Actions are specific and actionable
- [ ] Critical procedure actions prioritised

### Trend Analysis Checks

- [ ] Current period data added to Trend_Analysis
- [ ] Averages calculated correctly
- [ ] Comparison to previous period documented
- [ ] Patterns and systematic issues noted

### Evidence Checks

- [ ] Evidence collected for all assessments
- [ ] Evidence stored in ISMS Evidence Library
- [ ] Evidence naming convention followed
- [ ] Evidence register updated

### Approval Checks

- [ ] Assessor information complete
- [ ] Assessment date documented
- [ ] ISM sign-off obtained
- [ ] Comments addressed

---

## Review and Approval

### Review Process

The completed Quality Assessment must follow this review process:

#### Step 1: Self-Review by Assessor

- Complete Quality Checklist (Section 1.11)
- Verify all procedures assessed
- Check score calculations
- Ensure evidence is linked

#### Step 2: Technical Review by ISMS Administrator

**Reviewer:** ISMS Administrator
**Timeframe:** Within 5 business days

**Review scope:**
- Assessment completeness
- Score consistency
- Improvement action validity
- Evidence adequacy

**Outcome:** Approve, Return for corrections, or Escalate

#### Step 3: Final Approval by Information Security Manager

**Approver:** Information Security Manager
**Timeframe:** Within 5 business days

**Approval scope:**
- Assessment methodology followed
- Scores appear reasonable
- Improvement priorities appropriate
- Resource implications acceptable

**Outcome:** Approve or Reject

### Approval Workflow

```
Assessor Completes
        │
        ▼
Self-Review (Checklist)
        │
        ▼
ISMS Administrator Review ──► Return for Corrections
        │                            │
        ▼                            │
ISM Final Approval ──────────────────┘
        │
        ▼
   Assessment Complete
        │
        ▼
   Upload to ISMS Evidence Library
```

### Sign-Off Requirements

| Role | Signature Required | Authority |
|------|-------------------|-----------|
| Assessor | Yes | Confirms accuracy of assessment |
| ISMS Administrator | Yes | Confirms completeness |
| Information Security Manager | Yes | Final approval |

---

## Improvement Action Management

### Action Priority Matrix

| Procedure Criticality | Quality Rating | Action Priority |
|-----------------------|----------------|-----------------|
| Critical | Poor | Critical (5 days) |
| Critical | Needs Improvement | High (30 days) |
| Critical | Adequate | Medium (60 days) |
| High | Poor | High (30 days) |
| High | Needs Improvement | Medium (60 days) |
| High | Adequate | Low (90 days) |
| Medium/Low | Poor | Medium (60 days) |
| Medium/Low | Needs Improvement | Low (90 days) |
| Medium/Low | Adequate | Low (90 days) |

### Action Lifecycle

```
Action Created
        │
        ▼
Status: Open
        │
        ▼ (Work begins)
Status: In Progress
        │
        ▼ (Work completed)
Status: Completed
        │
        ▼ (ISM verifies)
Verified Closed
```

### Escalation Triggers

| Trigger | Escalation Path | Timing |
|---------|-----------------|--------|
| Critical action open > 5 days | ISM → CISO | Immediate |
| High action open > 30 days | Assessor → ISM | Within 24 hours |
| Multiple actions overdue | ISM → CISO | Weekly report |
| Procedure Owner unresponsive | ISM → Department Head | After 7 days |

---

## Related Controls

### Primary Control Relationships

Control A.5.37 quality assessment relates to:

| Control | Relationship | Integration Point |
|---------|--------------|-------------------|
| **A.5.37.1** | Procedure Inventory | Procedures to assess |
| **A.5.37.3** | Review Tracking | Quality drives review priority |
| **A.5.37.4** | Compliance Dashboard | Quality metrics aggregation |
| **A.5.1** | Policies | Quality standards for policy procedures |
| **A.7.2** | Competence | Training on procedure quality |
| **A.5.24** | Incident Management | Quality of incident procedures |
| **A.5.29** | Business Continuity | Quality of BC/DR procedures |

### Quality Improvement Cycle

```
A.5.37.1 Inventory
        │
        ▼
A.5.37.2 Quality Assessment ◄──┐
        │                       │
        ▼                       │
Improvement Actions ────────────┤
        │                       │
        ▼                       │
Procedure Updates ──────────────┘
        │
        ▼
A.5.37.3 Review Tracking
        │
        ▼
A.5.37.4 Dashboard
```

### Reference to Related IMPs

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-IMP-A.5.37.1 | Procedure Inventory | Source of procedures to assess |
| ISMS-IMP-A.5.37.3 | Review and Update Tracking | Quality drives review scheduling |
| ISMS-IMP-A.5.37.4 | Compliance Dashboard | Quality metrics reported |

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
