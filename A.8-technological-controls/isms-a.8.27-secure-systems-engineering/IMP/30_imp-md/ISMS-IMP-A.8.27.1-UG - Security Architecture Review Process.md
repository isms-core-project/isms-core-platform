**ISMS-IMP-A.8.27.1-UG - Security Architecture Review Process**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Security Architecture Review Process |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.1-UG |
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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
