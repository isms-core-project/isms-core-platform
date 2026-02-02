**ISMS-IMP-A.8.27.1 — Security Architecture Review Process**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Security Architecture Review Process |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.1 |
| **Assessment Domain** | Domain 1 - Architecture Review Governance |
| **Related Policy** | ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Security Architect / Enterprise Architect |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect | Initial architecture review assessment specification |

**Review Cycle**: Annual (or after major architecture changes)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles)
- ISMS-IMP-A.8.27.2 (Threat Modelling Methodology)
- ISMS-IMP-A.8.27.3 (Secure Architecture Pattern Catalogue)
- ISMS-IMP-A.8.27.4 (Zero Trust Implementation Assessment)
- ISMS-POL-A.8.25-26-29 (Secure Development Framework)
- ISO/IEC 27002:2022 Control A.8.27
- NIST SP 800-160 Vol. 1 Rev. 1 (Engineering Trustworthy Secure Systems)
- INCOSE Systems Engineering Handbook, 5th Edition (2023)


---

# PART I: USER COMPLETION GUIDE

# Assessment Overview

## Purpose

This assessment evaluates [Organisation]'s **security architecture review process**, focusing on the governance, methodology, and effectiveness of architecture security reviews as mandated by ISMS-POL-A.8.27.

**What This Assessment Covers:**

- Architecture review governance framework
- Review triggers and applicability criteria
- Review methodology and process flow
- Documentation requirements and templates
- Approval workflows and RACI matrices
- Review quality and effectiveness metrics
- Integration with SDLC and project management


**What This Assessment Does NOT Cover:**

- Threat modelling methodology details (see ISMS-IMP-A.8.27.2)
- Secure architecture pattern definitions (see ISMS-IMP-A.8.27.3)
- Zero Trust implementation specifics (see ISMS-IMP-A.8.27.4)
- Secure coding standards (see ISMS-IMP-A.8.28)


**Assessment Output:**

- Excel workbook documenting architecture review process maturity
- Review governance framework assessment
- Process compliance evaluation
- Documentation completeness analysis
- Metrics and KPI tracking baseline


## Why This Matters

**ISO/IEC 27001:2022 Control A.8.27 Requirement:**
> *"Principles for engineering secure systems should be established, documented, maintained and applied to any information system development activities."*

**NIST SP 800-160 Vol. 1 Rev. 1 Guidance:**
> *"Security architecture review is a critical activity that ensures security requirements are addressed in system design and that security controls are appropriately positioned within the system architecture."*

**Business Impact of Missing Architecture Reviews:**

- **Security Gaps:** Design flaws discovered late are 6-10x more expensive to fix
- **Compliance Failures:** Missing evidence of "security by design" for audits
- **Technical Debt:** Insecure foundations require costly remediation
- **Breach Risk:** Architectural weaknesses create systemic vulnerabilities
- **Project Delays:** Late-stage security findings force redesign


**This Assessment Addresses:**

- Do we have a defined process for security architecture reviews?
- Are reviews triggered at the right points in the development lifecycle?
- Is the review methodology comprehensive and consistent?
- Are review findings documented and tracked to closure?
- Do we measure the effectiveness of our architecture reviews?


## Who Should Complete This Assessment

**Primary Responsibility:** Security Architect or Enterprise Security Architect

**Required Knowledge:**

- [Organisation]'s architecture review policies and procedures
- SDLC integration points and project governance
- Architecture documentation standards
- Threat modelling methodologies in use
- Security patterns and reference architectures


**Support Roles:**

- **CISO:** Governance framework, exception authority
- **Enterprise Architect:** Architecture standards, integration
- **Development Managers:** SDLC process, project coordination
- **Project Management Office:** Project lifecycle triggers
- **IT Operations:** Operational security requirements


**Collaboration Required:**

- Review process owners and stakeholders
- Sample review documentation
- Metrics and tracking data


## Time Estimate

**Total Assessment Time:** 6-10 hours

**Breakdown:**

- **Information Gathering:** 2-3 hours
  - Review architecture review policy and procedures
  - Collect review templates and checklists
  - Gather sample completed reviews
  - Compile metrics and tracking data

- **Assessment Completion:** 2-3 hours
  - Document governance framework
  - Assess process maturity
  - Evaluate review quality
  - Analyse coverage and effectiveness

- **Evidence Collection:** 1-2 hours
  - Sample architecture review documents
  - Process flowcharts
  - Approval records
  - Metrics dashboards

- **Quality Review:** 1-2 hours
  - Gap analysis
  - Remediation planning
  - Stakeholder review


## Connection to Policy

This assessment implements **ISMS-POL-A.8.27, Section 2.2 (System Architecture Requirements)** which mandates:

**Review Triggers:**

- New system development or acquisition
- Major version upgrades or migrations
- Architecture changes affecting security boundaries
- Integration of new external services or data flows
- Changes to authentication or authorisation mechanisms


**Review Process Requirements:**

1. Threat modelling using structured methodology
2. Security requirements validation
3. Architecture pattern review against approved patterns
4. Control design review for defence in depth
5. Risk assessment and residual risk documentation
6. CISO or Security Architect approval


**Review Documentation Requirements:**

- Security Architecture Document (SAD)
- Threat Model Report
- Security Requirements Traceability Matrix
- Risk Assessment and Treatment Plan
- Architecture approval record


---

# Prerequisites

## Required Access

Before starting this assessment, ensure you have access to:

| System/Resource | Purpose | Who Can Provide |
|-----------------|---------|-----------------|
| Architecture review documentation | Review process definitions | Security Architect |
| Project management system | Review triggers and tracking | PMO |
| Architecture repository | Sample reviews and templates | Enterprise Architecture |
| SDLC tooling | Integration evidence | Development Manager |
| Metrics/reporting tools | Effectiveness data | Security Operations |


## Pre-Assessment Checklist

✅ Architecture review policy reviewed and understood
✅ Access to review templates and checklists confirmed
✅ Sample completed reviews identified (minimum 3)
✅ Review metrics and tracking data available
✅ Process stakeholders identified for consultation
✅ Assessment timeframe scheduled and communicated


## Information Gathering Requirements

**Collect the following before completing the assessment:**

| Category | Required Information | Source |
|----------|---------------------|--------|
| **Governance** | Review policy, procedures, RACI | Security Architect |
| **Process** | Workflow diagrams, trigger criteria | PMO/Architecture |
| **Templates** | SAD template, threat model template, checklists | Architecture team |
| **Samples** | 3+ completed reviews from past 12 months | Project files |
| **Metrics** | Review counts, timing, findings data | ISMS dashboard |
| **Training** | Reviewer training records | HR/Training |


---

# Workbook Structure

## Sheet Overview

The assessment workbook contains the following sheets:

| Sheet | Purpose | Completion Order |
|-------|---------|------------------|
| **Instructions** | Guide to completing the workbook | Read first |
| **Governance** | Review governance framework assessment | 1 |
| **Process** | Review process and methodology | 2 |
| **Templates** | Documentation templates assessment | 3 |
| **Integration** | SDLC and project integration | 4 |
| **Metrics** | Review effectiveness metrics | 5 |
| **Compliance** | Policy compliance scoring | 6 |
| **GapRegister** | Identified gaps and remediation | Last |
| **Dashboard** | Summary view and status | Auto-calculated |


## Sheet Descriptions

### Instructions Sheet

Read-only sheet containing:

- Assessment purpose and scope
- Completion instructions
- Rating scale definitions
- Evidence requirements
- Contact information for questions


### Governance Sheet

Documents the architecture review governance framework:

| Column | Description | Example |
|--------|-------------|---------|
| Gov-ID | Governance element identifier | GOV-001 |
| Category | Governance area | Policy |
| Requirement | Specific requirement | Documented review policy |
| Status | Current status | Implemented |
| Evidence | Supporting documentation | ISMS-POL-A.8.27 |
| Gap | If not implemented, describe gap | N/A |
| Owner | Responsible party | Security Architect |


### Process Sheet

Assesses the architecture review process:

| Column | Description | Example |
|--------|-------------|---------|
| Proc-ID | Process step identifier | PROC-001 |
| Phase | Review phase | Trigger |
| Activity | Specific activity | Project intake assessment |
| Documented | Is activity documented? | Yes |
| Implemented | Is activity performed? | Yes |
| Evidence | How is it evidenced? | JIRA workflow |
| Effectiveness | Rating (1-5) | 4 |


### Templates Sheet

Evaluates documentation templates:

| Column | Description | Example |
|--------|-------------|---------|
| Temp-ID | Template identifier | TEMP-001 |
| Template | Template name | Security Architecture Document |
| Version | Current version | 2.1 |
| Last Updated | Date of last update | 2025-06-15 |
| Completeness | Template coverage (1-5) | 4 |
| Usability | Ease of use (1-5) | 3 |
| Gaps | Missing elements | Cloud-specific sections |


### Integration Sheet

Assesses SDLC and project integration:

| Column | Description | Example |
|--------|-------------|---------|
| Int-ID | Integration point identifier | INT-001 |
| Integration | Integration type | Project initiation |
| Trigger | What triggers review? | New system >$50K |
| Automated | Is trigger automated? | Partial |
| Tracked | Is review tracked? | Yes, in JIRA |
| Enforced | Can projects bypass? | No, gate enforced |


### Metrics Sheet

Records review effectiveness metrics:

| Column | Description | Example |
|--------|-------------|---------|
| Met-ID | Metric identifier | MET-001 |
| Metric | Metric name | Reviews completed |
| Period | Measurement period | Q4 2025 |
| Target | Target value | 100% |
| Actual | Actual value | 95% |
| Trend | Up/Down/Stable | Up |
| Action | If below target | Additional reviewer training |


### Compliance Sheet

Calculates compliance with policy requirements:

| Column | Description | Example |
|--------|-------------|---------|
| Comp-ID | Compliance requirement ID | COMP-001 |
| Requirement | Policy requirement | All new systems reviewed |
| Source | Policy section reference | POL-A.8.27 §2.2.1 |
| Compliant | Yes/Partial/No | Yes |
| Evidence | Compliance evidence | Q4 review log |
| Score | Compliance score (0-100) | 100 |


### GapRegister Sheet

Documents identified gaps and remediation:

| Column | Description | Example |
|--------|-------------|---------|
| Gap-ID | Gap identifier | GAP-001 |
| Source | Which sheet identified gap | Process |
| Description | Gap description | No cloud architecture review template |
| Risk | Risk rating (H/M/L) | Medium |
| Remediation | Planned remediation | Develop cloud review template |
| Owner | Responsible party | Security Architect |
| Due Date | Target completion | 2026-03-31 |
| Status | Current status | In Progress |


### Dashboard Sheet

Auto-calculated summary view:

- Overall compliance score
- Compliance by category
- Gap summary by risk level
- Trend indicators
- Key metrics snapshot


---

# Completion Walkthrough

## Step 1: Review Instructions

1. Open the workbook and navigate to the **Instructions** sheet
2. Read the purpose, scope, and methodology
3. Understand the rating scales used throughout
4. Note the evidence requirements for each section


## Step 2: Complete Governance Assessment

**Navigate to the Governance sheet**

For each governance element:

1. **Identify Status:** Review whether each governance requirement is:
   - **Implemented:** Fully documented and operational
   - **Partial:** Documented but not fully operational, or operational but not documented
   - **Not Implemented:** Neither documented nor operational
   - **N/A:** Not applicable (with justification)

2. **Provide Evidence:** Reference specific documents, systems, or records that demonstrate compliance

3. **Document Gaps:** For any non-compliant items, describe what is missing

**Example Governance Elements:**

| Element | Question to Answer |
|---------|-------------------|
| Policy | Is there a documented architecture review policy? |
| Procedures | Are review procedures defined and maintained? |
| Roles | Are reviewer roles and responsibilities documented? |
| Authority | Is approval authority clearly defined? |
| Exceptions | Is there an exception process? |


## Step 3: Complete Process Assessment

**Navigate to the Process sheet**

For each process phase (Trigger, Planning, Execution, Documentation, Approval, Follow-up):

1. **Document Activities:** List all activities performed in each phase
2. **Assess Documentation:** Is the activity documented in procedures?
3. **Verify Implementation:** Is the activity actually performed?
4. **Gather Evidence:** How can you prove the activity occurs?
5. **Rate Effectiveness:** On a 1-5 scale, how effective is the activity?

**Rating Scale:**

| Rating | Description |
|--------|-------------|
| 1 | Not performed or completely ineffective |
| 2 | Performed ad-hoc, minimal effectiveness |
| 3 | Defined process, moderate effectiveness |
| 4 | Managed process, good effectiveness |
| 5 | Optimised process, excellent effectiveness |


## Step 4: Complete Templates Assessment

**Navigate to the Templates sheet**

For each documentation template:

1. **Identify Templates:** List all architecture review templates in use
2. **Check Currency:** When were templates last updated?
3. **Rate Completeness:** Does the template cover all necessary elements? (1-5)
4. **Rate Usability:** Is the template easy to use? (1-5)
5. **Note Gaps:** What is missing from each template?

**Expected Templates:**

- Security Architecture Document (SAD)
- Threat Model Template
- Architecture Review Checklist
- Security Requirements Template
- Risk Assessment Template
- Architecture Decision Record (ADR)


## Step 5: Complete Integration Assessment

**Navigate to the Integration sheet**

For each SDLC integration point:

1. **Map Triggers:** What events trigger architecture review?
2. **Assess Automation:** Are triggers automated or manual?
3. **Verify Tracking:** How are reviews tracked through the lifecycle?
4. **Check Enforcement:** Can reviews be bypassed?

**Key Integration Points:**

- Project initiation/intake
- Architecture design phase
- Pre-development gate
- Pre-production release
- Major change requests
- Acquisitions/third-party integration


## Step 6: Complete Metrics Assessment

**Navigate to the Metrics sheet**

For each metric:

1. **Define Metrics:** What metrics are tracked?
2. **Set Targets:** What are the target values?
3. **Record Actuals:** What were actual values for the period?
4. **Analyse Trends:** Is performance improving or declining?
5. **Plan Actions:** What actions address underperformance?

**Recommended Metrics:**

| Metric | Description | Target |
|--------|-------------|--------|
| Review Coverage | % of applicable projects reviewed | 100% |
| Review Timeliness | Average days from trigger to completion | <10 days |
| Finding Closure | % of high findings remediated before release | 100% |
| Bypass Rate | % of projects bypassing review | 0% |
| Rework Rate | % of projects requiring re-review | <10% |


## Step 7: Complete Compliance Scoring

**Navigate to the Compliance sheet**

For each policy requirement:

1. **Map Requirements:** List each requirement from ISMS-POL-A.8.27
2. **Assess Compliance:** Is the organisation compliant? (Yes/Partial/No)
3. **Document Evidence:** What evidence demonstrates compliance?
4. **Calculate Score:** Apply scoring formula

**Scoring Formula:**

- Yes = 100%
- Partial = 50%
- No = 0%

**Overall Compliance = Average of all requirement scores**


## Step 8: Document Gaps and Remediation

**Navigate to the GapRegister sheet**

For each identified gap:

1. **Consolidate Gaps:** Gather all gaps identified in previous sheets
2. **Rate Risk:** Assess risk level (High/Medium/Low)
3. **Plan Remediation:** Define specific remediation actions
4. **Assign Ownership:** Identify responsible party
5. **Set Due Dates:** Establish realistic completion dates
6. **Track Status:** Monitor progress

**Risk Rating Criteria:**

| Rating | Criteria |
|--------|----------|
| High | Compliance failure, significant security risk, audit finding likely |
| Medium | Process gap, moderate security risk, improvement needed |
| Low | Minor gap, low security risk, enhancement opportunity |


## Step 9: Review Dashboard

**Navigate to the Dashboard sheet**

1. **Verify Calculations:** Ensure all scores calculated correctly
2. **Review Summary:** Check overall compliance posture
3. **Identify Focus Areas:** Note categories needing attention
4. **Prepare Report:** Extract key findings for stakeholders


---

# Evidence Collection

## Required Evidence

For a complete assessment, collect the following evidence:

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| **Policy Document** | Architecture review policy | ISMS Evidence Library |
| **Procedures** | Review procedures and workflow | ISMS Evidence Library |
| **Templates** | All review templates | Architecture Repository |
| **Sample Reviews** | 3+ completed reviews | Project Documentation |
| **Approval Records** | Signed approval documents | Architecture Repository |
| **Metrics Data** | Review tracking and metrics | ISMS Dashboard |
| **Training Records** | Reviewer training evidence | HR/Training System |
| **Exception Records** | Any review exceptions granted | Exception Register |


## Evidence Naming Convention

Use the following naming convention for evidence files:

```
ISMS-IMP-A.8.27.1_[EvidenceType]_[Description]_YYYYMMDD.[ext]
```

**Examples:**

- `ISMS-IMP-A.8.27.1_Policy_ArchitectureReviewPolicy_20260115.pdf`
- `ISMS-IMP-A.8.27.1_Sample_ProjectXReview_20260115.docx`
- `ISMS-IMP-A.8.27.1_Metrics_Q4ReviewData_20260115.xlsx`


## Evidence Storage

Store all evidence in the designated ISMS Evidence Library:

```
/ISMS Evidence Library/
  /A.8.27 - Secure Systems Engineering/
    /A.8.27.1 - Architecture Review/
      /Governance/
      /Process/
      /Templates/
      /Samples/
      /Metrics/
```


---

# Common Pitfalls

Avoid these common mistakes when completing this assessment:

❌ **MISTAKE:** Treating architecture review as optional for "small" projects
✅ **CORRECT:** Apply consistent criteria; small projects may still have significant risk

❌ **MISTAKE:** Documenting a process that exists only on paper
✅ **CORRECT:** Verify process is actually followed with sample evidence

❌ **MISTAKE:** Using outdated templates without periodic review
✅ **CORRECT:** Review and update templates at least annually

❌ **MISTAKE:** Allowing informal review bypasses without exception process
✅ **CORRECT:** All bypasses must follow formal exception process

❌ **MISTAKE:** Completing review but not tracking findings to closure
✅ **CORRECT:** Track all findings with clear ownership and due dates

❌ **MISTAKE:** Rating process as "5" without evidence of optimisation
✅ **CORRECT:** Reserve top ratings for processes with demonstrated continuous improvement

❌ **MISTAKE:** Assessing compliance without referencing specific policy sections
✅ **CORRECT:** Map each compliance item to specific policy requirements

❌ **MISTAKE:** Documenting gaps without risk assessment
✅ **CORRECT:** Rate all gaps by risk to prioritise remediation

❌ **MISTAKE:** Setting unrealistic remediation dates to show progress
✅ **CORRECT:** Set achievable dates with appropriate resource allocation

❌ **MISTAKE:** Completing assessment in isolation without stakeholder input
✅ **CORRECT:** Engage process owners, reviewers, and consumers


---

# Quality Checklist

Before submitting the assessment, verify:

**Completeness:**

- [ ] All governance elements assessed
- [ ] All process phases evaluated
- [ ] All templates reviewed
- [ ] All integration points assessed
- [ ] All metrics documented
- [ ] All compliance requirements scored
- [ ] All gaps documented in register
- [ ] Dashboard reflects current data


**Evidence:**

- [ ] Each compliance claim has supporting evidence
- [ ] Sample reviews collected (minimum 3)
- [ ] Evidence properly named and stored
- [ ] Evidence referenced in assessment


**Quality:**

- [ ] Ratings justified with evidence
- [ ] Gaps have remediation plans
- [ ] Remediation plans have owners
- [ ] Due dates are realistic
- [ ] No duplicate entries
- [ ] Formulas calculating correctly


**Review:**

- [ ] Self-review completed
- [ ] Peer review completed
- [ ] Stakeholder validation obtained
- [ ] Ready for management approval


---

# Review & Approval

## Review Process

1. **Self-Review:** Assessor reviews completed workbook for completeness
2. **Peer Review:** Another Security Architect or analyst reviews
3. **Stakeholder Review:** Process owners validate accuracy
4. **Management Approval:** CISO or designate approves final assessment

## Approval Workflow

| Step | Reviewer | Focus | Timeline |
|------|----------|-------|----------|
| 1 | Assessor | Completeness, evidence | Before submission |
| 2 | Peer | Technical accuracy | 2 business days |
| 3 | Stakeholders | Process accuracy | 3 business days |
| 4 | CISO | Final approval | 2 business days |


## Sign-Off Record

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Assessor | | | |
| Peer Reviewer | | | |
| Security Architect | | | |
| CISO | | | |


---

# PART II: TECHNICAL SPECIFICATION

# Excel Workbook Specification

## Workbook Overview

| Property | Value |
|----------|-------|
| **Filename** | ISMS-IMP-A.8.27.1_Security_Architecture_Review_Process_YYYYMMDD.xlsx |
| **Sheets** | 9 |
| **Purpose** | Security architecture review process assessment |
| **Generator** | generate_a827_1_architecture_review.py |


## Sheet Specifications

### Sheet 1: Instructions

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Instructions |
| **Purpose** | User guidance and reference |
| **Protection** | Read-only (protected) |

**Content Sections:**

1. Document header with ISMS branding
2. Assessment purpose and scope
3. Completion instructions
4. Rating scale definitions
5. Evidence requirements
6. Contact information
7. Version and date information


### Sheet 2: Governance

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Governance |
| **Purpose** | Architecture review governance assessment |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gov-ID | 10 | Auto | GOV-001 format |
| B | Category | 20 | Dropdown | Policy/Procedures/Roles/Authority/Exceptions |
| C | Requirement | 40 | Text | Required |
| D | Status | 15 | Dropdown | Implemented/Partial/Not Implemented/N/A |
| E | Evidence | 40 | Text | Required if Implemented |
| F | Gap | 40 | Text | Required if Not Implemented |
| G | Owner | 20 | Text | Required |
| H | Notes | 30 | Text | Optional |

**Pre-populated Rows:** 15 governance requirements from ISMS-POL-A.8.27


### Sheet 3: Process

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Process |
| **Purpose** | Review process assessment |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Proc-ID | 10 | Auto | PROC-001 format |
| B | Phase | 15 | Dropdown | Trigger/Planning/Execution/Documentation/Approval/Follow-up |
| C | Activity | 40 | Text | Required |
| D | Documented | 12 | Dropdown | Yes/Partial/No |
| E | Implemented | 12 | Dropdown | Yes/Partial/No |
| F | Evidence | 30 | Text | Required |
| G | Effectiveness | 12 | Dropdown | 1/2/3/4/5 |
| H | Notes | 30 | Text | Optional |

**Pre-populated Rows:** 25 process activities


### Sheet 4: Templates

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Templates |
| **Purpose** | Documentation templates assessment |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Temp-ID | 10 | Auto | TEMP-001 format |
| B | Template | 35 | Text | Required |
| C | Version | 10 | Text | Version format |
| D | Last Updated | 12 | Date | Date validation |
| E | Completeness | 12 | Dropdown | 1/2/3/4/5 |
| F | Usability | 12 | Dropdown | 1/2/3/4/5 |
| G | Gaps | 35 | Text | Optional |
| H | Notes | 25 | Text | Optional |

**Pre-populated Rows:** 8 expected templates


### Sheet 5: Integration

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Integration |
| **Purpose** | SDLC integration assessment |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Int-ID | 10 | Auto | INT-001 format |
| B | Integration | 30 | Text | Required |
| C | Trigger | 35 | Text | Required |
| D | Automated | 12 | Dropdown | Yes/Partial/No |
| E | Tracked | 12 | Dropdown | Yes/Partial/No |
| F | Enforced | 12 | Dropdown | Yes/Partial/No |
| G | Evidence | 30 | Text | Required |
| H | Notes | 25 | Text | Optional |

**Pre-populated Rows:** 8 integration points


### Sheet 6: Metrics

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Metrics |
| **Purpose** | Review effectiveness metrics |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Met-ID | 10 | Auto | MET-001 format |
| B | Metric | 35 | Text | Required |
| C | Period | 15 | Text | Required |
| D | Target | 12 | Percentage | 0-100% |
| E | Actual | 12 | Percentage | 0-100% |
| F | Trend | 10 | Dropdown | Up/Down/Stable |
| G | Action | 35 | Text | Required if Actual < Target |
| H | Notes | 25 | Text | Optional |

**Pre-populated Rows:** 10 recommended metrics


### Sheet 7: Compliance

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Compliance |
| **Purpose** | Policy compliance scoring |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Comp-ID | 10 | Auto | COMP-001 format |
| B | Requirement | 40 | Text | Required |
| C | Source | 20 | Text | Policy reference |
| D | Compliant | 12 | Dropdown | Yes/Partial/No |
| E | Evidence | 35 | Text | Required |
| F | Score | 10 | Formula | =IF(D="Yes",100,IF(D="Partial",50,0)) |
| G | Notes | 25 | Text | Optional |

**Pre-populated Rows:** 20 compliance requirements from ISMS-POL-A.8.27


### Sheet 8: GapRegister

| Property | Specification |
|----------|---------------|
| **Sheet Name** | GapRegister |
| **Purpose** | Gap tracking and remediation |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap-ID | 10 | Auto | GAP-001 format |
| B | Source | 15 | Dropdown | Sheet names |
| C | Description | 40 | Text | Required |
| D | Risk | 10 | Dropdown | High/Medium/Low |
| E | Remediation | 40 | Text | Required |
| F | Owner | 20 | Text | Required |
| G | Due Date | 12 | Date | Future date |
| H | Status | 12 | Dropdown | Open/In Progress/Closed |
| I | Closure Date | 12 | Date | Date validation |
| J | Notes | 25 | Text | Optional |


### Sheet 9: Dashboard

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Dashboard |
| **Purpose** | Summary and status view |
| **Protection** | Read-only (formulas only) |

**Dashboard Elements:**

1. **Overall Compliance Score:** Average of Compliance sheet scores
2. **Category Scores:** Governance, Process, Templates, Integration, Metrics
3. **Gap Summary:** Count by risk level (High/Medium/Low)
4. **Status Summary:** Open/In Progress/Closed gaps
5. **Trend Chart:** Placeholder for compliance trend
6. **Key Metrics:** Top 5 metrics with status indicators


## Styling Specifications

### Colour Palette

| Element | Colour Code | Usage |
|---------|-------------|-------|
| Header Background | #1F4E79 | Sheet headers |
| Header Text | #FFFFFF | Header text |
| Subheader Background | #2E75B6 | Section subheaders |
| Input Cell | #E2EFDA | User input cells |
| Formula Cell | #FFF2CC | Calculated cells |
| Compliant | #C6EFCE | Yes/Implemented status |
| Partial | #FFEB9C | Partial status |
| Non-Compliant | #FFC7CE | No/Not Implemented status |
| High Risk | #FF0000 | High risk gaps |
| Medium Risk | #FFA500 | Medium risk gaps |
| Low Risk | #FFFF00 | Low risk gaps |


### Font Standards

| Element | Font | Size | Style |
|---------|------|------|-------|
| Headers | Calibri | 14 | Bold |
| Subheaders | Calibri | 12 | Bold |
| Body Text | Calibri | 11 | Regular |
| Notes | Calibri | 10 | Italic |


### Cell Formatting

- All cells with borders (thin, black)
- Headers with bottom border (medium)
- Alternating row shading for readability (optional)
- Frozen panes for headers on all data sheets
- Column auto-filter enabled on data sheets


## Data Validation

### Dropdown Lists

Create named ranges for dropdown validation:

| Name | Values |
|------|--------|
| StatusList | Implemented, Partial, Not Implemented, N/A |
| YesNoPartial | Yes, Partial, No |
| RatingScale | 1, 2, 3, 4, 5 |
| RiskLevel | High, Medium, Low |
| GapStatus | Open, In Progress, Closed |
| TrendList | Up, Down, Stable |
| ProcessPhase | Trigger, Planning, Execution, Documentation, Approval, Follow-up |
| GovCategory | Policy, Procedures, Roles, Authority, Exceptions |


### Input Validation Rules

- Date fields: Valid date format, not in past for due dates
- Percentage fields: 0-100%
- Required fields: Cannot be blank
- Conditional: Evidence required when status is "Implemented"


## Formulas

### Compliance Score Calculation

```excel
# Individual requirement score
=IF(D2="Yes",100,IF(D2="Partial",50,0))

# Overall compliance score
=AVERAGE(F:F)
```

### Gap Summary Counts

```excel
# High risk gaps
=COUNTIF(GapRegister!D:D,"High")

# Open gaps
=COUNTIF(GapRegister!H:H,"Open")
```

### Category Scores

```excel
# Governance compliance
=AVERAGEIF(Compliance!C:C,"*GOV*",Compliance!F:F)
```


---

# Generator Script Reference

## Script Information

| Property | Value |
|----------|-------|
| **Script Name** | generate_a827_1_architecture_review.py |
| **Location** | 10-isms-scr-base/isms-a.8.27-secure-systems-engineering/10_generator-master/ |
| **Output** | ISMS-IMP-A.8.27.1_Security_Architecture_Review_Process_YYYYMMDD.xlsx |


## Script Structure

```python
# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.8.27.1"
WORKBOOK_NAME = "Security Architecture Review Process"
CONTROL_ID = "A.8.27"
CONTROL_NAME = "Secure System Architecture and Engineering Principles"
```


## Pre-populated Data

The generator should pre-populate the following:

**Governance Requirements (15 rows):**

1. Architecture review policy documented
2. Review procedures defined
3. Reviewer roles and responsibilities defined
4. Approval authority documented
5. Exception process established
6. Review scope criteria defined
7. Mandatory review triggers documented
8. Review timeline requirements specified
9. Documentation standards defined
10. Quality review process established
11. Training requirements specified
12. Escalation procedures documented
13. Integration with SDLC defined
14. Metrics and reporting requirements
15. Continuous improvement process


**Process Activities (25 rows):**

Organised by phase: Trigger (5), Planning (4), Execution (6), Documentation (4), Approval (3), Follow-up (3)


**Templates (8 rows):**

1. Security Architecture Document (SAD)
2. Threat Model Template
3. Architecture Review Checklist
4. Security Requirements Template
5. Risk Assessment Template
6. Architecture Decision Record (ADR)
7. Exception Request Form
8. Review Completion Report


**Integration Points (8 rows):**

1. Project initiation
2. Architecture design phase
3. Pre-development gate
4. Pre-production release
5. Major change requests
6. Third-party integration
7. Cloud service adoption
8. Post-incident architecture review


**Metrics (10 rows):**

1. Review coverage (% applicable projects reviewed)
2. Review timeliness (days from trigger to completion)
3. Finding closure rate (% high findings closed before release)
4. Bypass rate (% projects bypassing review)
5. Rework rate (% requiring re-review)
6. Template compliance (% using approved templates)
7. Documentation completeness (average documentation score)
8. Stakeholder satisfaction (survey score)
9. Time to approval (days from submission to approval)
10. Finding recurrence (% findings repeating)


**Compliance Requirements (20 rows):**

Mapped from ISMS-POL-A.8.27 Sections 2.2 and 4


---

**END OF SPECIFICATION**

---

*"Architecture is the foundation; security architecture is the foundation's foundation."*
— Gene Kim

<!-- QA_VERIFIED: [Date] -->
