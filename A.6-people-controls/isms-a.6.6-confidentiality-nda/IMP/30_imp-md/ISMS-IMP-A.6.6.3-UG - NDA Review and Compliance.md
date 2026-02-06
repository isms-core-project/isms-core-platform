**ISMS-IMP-A.6.6.3-UG - NDA Review and Compliance**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.6.6: Confidentiality or Non-Disclosure Agreements

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.6.3-UG |
| **Document Title** | NDA Review and Compliance Workbook Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.6.6: Confidentiality or Non-Disclosure Agreements |
| **Parent Policy** | ISMS-POL-A.6.6 (Confidentiality and Non-Disclosure Agreements) |
| **Version** | 1.0 |
| **Classification** | Internal |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial implementation specification for ISO 27001:2022 first certification |

---

This section provides step-by-step guidance for completing the NDA Review and Compliance workbook. Follow this guide to ensure NDAs remain current, appropriate, and properly executed as required by ISO 27001:2022.

---

## 1. Assessment Overview

### 1.1 Purpose

The NDA Review and Compliance workbook enables systematic periodic review of NDA adequacy and compliance. It ensures that confidentiality agreements remain fit for purpose, coverage is complete across all stakeholder categories, and gaps are identified and remediated in a timely manner.

ISO/IEC 27001:2022 Control A.6.6 states:

> *"Confidentiality or non-disclosure agreements reflecting the organisation's needs for the protection of information should be identified, documented, regularly reviewed and signed by personnel and other relevant interested parties."*

This workbook directly supports the "regularly reviewed" requirement by establishing a structured review process with documented evidence.

### 1.2 Scope and Applicability

**This workbook covers:**

| Review Area | Description |
|-------------|-------------|
| Periodic Review Scheduling | Planning and tracking of review activities |
| Template Adequacy Assessment | Evaluating NDA templates for legal and regulatory currency |
| Coverage Analysis | Verifying all required parties have executed NDAs |
| Compliance Verification | Checking individual NDA execution and storage compliance |
| Gap Identification | Documenting and tracking coverage and compliance gaps |
| Remediation Tracking | Managing gap closure to resolution |

**This workbook applies to NDAs for:**

| Stakeholder Category | Applicability |
|----------------------|---------------|
| Employees | All employees with information access |
| Contractors | All contractors regardless of duration |
| Vendors | Vendors with access to organisation data or systems |
| Partners | Business partners with information sharing |
| Consultants | External consultants engaged for projects |
| Visitors | Visitors to sensitive areas (if applicable) |
| Interns/Trainees | Temporary personnel with information access |
| Board Members | Non-executive directors and advisors |

### 1.3 Business Context

**Why NDA Review Matters:**

NDAs require ongoing review and maintenance:

1. **Legal Currency**: Laws and regulations change, requiring template updates
2. **Coverage Completeness**: Staff turnover creates gaps in NDA coverage
3. **Expiration Management**: Time-limited NDAs may lapse unnoticed
4. **Template Appropriateness**: New information types may not be covered
5. **Compliance Verification**: Execution errors reduce enforceability
6. **Audit Requirements**: Auditors expect documented review processes
7. **Risk Management**: Gaps in NDA coverage create information disclosure risk

**Regulatory Context:**

| Regulation | NDA Review Requirement |
|------------|------------------------|
| ISO 27001:2022 A.6.6 | Regular review requirement explicit |
| Swiss FADP/nDSG | Data protection requires binding confidentiality |
| GDPR | Processor agreements must include confidentiality |
| Employment Law | Employment NDAs may have specific requirements |

### 1.4 Assessment Outputs

Upon completion, this workbook provides:

| Output | Purpose | Audience |
|--------|---------|----------|
| Review Schedule | Planned review activities | Information Security Manager |
| Template Assessment | Template adequacy status | Legal, ISM |
| Coverage Report | NDA coverage by category | HR, Procurement, ISM |
| Compliance Status | Individual NDA compliance | ISM, Auditors |
| Gap Register | All identified gaps | Remediation owners |
| Audit Evidence | Review documentation | External Auditors |

---

## 2. Prerequisites

### 2.1 Required Inputs

Before beginning the review process, ensure you have:

| Input | Source | Required For |
|-------|--------|--------------|
| NDA Template Registry | ISMS-IMP-A.6.6.1 | Template adequacy assessment |
| NDA Execution Register | ISMS-IMP-A.6.6.2 | Compliance verification |
| Current HR headcount | Human Resources | Employee coverage analysis |
| Employee categories | Human Resources | Category-based analysis |
| Contractor roster | Procurement/HR | Contractor coverage analysis |
| Vendor list | Procurement | Vendor coverage analysis |
| Partner agreements | Business Development | Partner coverage analysis |
| Previous review findings | ISMS Evidence Library | Trend analysis |

### 2.2 Required Approvals

| Approval Type | Approver | Purpose |
|---------------|----------|---------|
| Review Plan | Information Security Manager | Authorise review scope |
| Template Changes | Legal Counsel | Approve template updates |
| Gap Remediation | Relevant Department Head | Resource allocation |
| Review Completion | CISO | Sign-off on review results |

### 2.3 Required Knowledge

Review personnel should understand:

- NDA legal concepts and enforceability requirements
- Organisation's information classification scheme
- Confidentiality requirements by information type
- Stakeholder categories and access patterns
- Regulatory requirements for confidentiality
- Gap remediation processes

### 2.4 Tool Requirements

| Tool | Purpose | Access Required |
|------|---------|-----------------|
| Excel or equivalent | Workbook completion | Standard user |
| Document management system | NDA storage verification | Read access |
| HR system | Headcount verification | Read access (or HR data extract) |
| Vendor management system | Vendor list | Read access |
| Calendar/scheduling | Review scheduling | Standard access |

---

## 3. Workbook Structure Overview

### 3.1 Sheet Summary

The workbook contains eight sheets for comprehensive review management:

| Sheet | Purpose | Primary Owner | Update Frequency |
|-------|---------|---------------|------------------|
| 1: Instructions | Usage guidance | N/A | Reference only |
| 2: Periodic_Review | Review scheduling | ISM | Per review cycle |
| 3: Template_Adequacy | Template assessment | Legal/ISM | Annual |
| 4: Coverage_Analysis | Coverage verification | ISM | Quarterly |
| 5: Compliance_Check | Individual NDA compliance | ISM | Annual |
| 6: Gap_Register | Gap tracking | Remediation Owners | As needed |
| 7: Evidence_Register | Evidence linking | ISM | Per activity |
| 8: Approval_SignOff | Formal approvals | CISO | Per review cycle |

### 3.2 Sheet Dependencies

```
Sheet 2: Periodic_Review (Schedule)
         ↓ (triggers)
Sheet 3: Template_Adequacy + Sheet 4: Coverage_Analysis + Sheet 5: Compliance_Check
         ↓ (feed gaps to)
Sheet 6: Gap_Register
         ↓ (evidence to)
Sheet 7: Evidence_Register
         ↓ (approval in)
Sheet 8: Approval_SignOff
```

### 3.3 Data Flow

1. **Review Scheduled**: Review planned in Sheet 2
2. **Assessments Conducted**: Sheets 3, 4, 5 completed
3. **Gaps Identified**: Documented in Sheet 6
4. **Evidence Linked**: Recorded in Sheet 7
5. **Approval Obtained**: Sign-off in Sheet 8
6. **Review Completed**: Status updated in Sheet 2

---

## 4. Completion Walkthrough

### 4.1 Sheet 2: Periodic_Review – Completion Guide

**Purpose**: Schedule, track, and document all NDA review activities.

**Step-by-Step Completion:**

**Step 1: Generate Review ID**

Create a unique identifier using the format `REV-YYYY-NNN`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | REV- | REV- |
| Year | YYYY | 2026 |
| Sequence | NNN | 001 |
| Full ID | REV-YYYY-NNN | REV-2026-001 |

**Step 2: Select Review Type**

| Review Type | Description | Frequency | Scope |
|-------------|-------------|-----------|-------|
| Annual Full Review | Comprehensive review of all aspects | Once per year | All templates, all coverage, all NDAs |
| Quarterly Check | Focused check on key metrics | Every 3 months | Coverage rates, expirations, gaps |
| Template Update Review | Review triggered by template changes | When templates updated | Affected templates and NDAs |
| Triggered Review | Review triggered by events | As needed | Affected areas |
| Ad-hoc Review | Unscheduled review | As requested | Specific scope |

**Triggers for Triggered Reviews:**

- Regulatory changes affecting confidentiality requirements
- Security incidents involving information disclosure
- Significant organisational changes (M&A, restructure)
- New information types requiring protection
- Legal counsel advice on template updates
- Audit findings requiring remediation

**Step 3: Define Review Scope**

Document what the review covers:

| Scope Element | Description |
|---------------|-------------|
| Templates | Which templates are being reviewed |
| Stakeholder Categories | Which categories are being analysed |
| Time Period | NDAs from which period |
| Geographic Scope | Which locations/entities |
| Specific Focus | Any particular focus areas |

**Step 4: Record Review Details**

| Field | Guidance |
|-------|----------|
| Planned_Date | Target completion date |
| Actual_Date | When review was actually completed |
| Reviewer | Person(s) conducting review |
| Findings_Count | Total findings identified |
| Gaps_Identified | Number of gaps found |
| Status | Scheduled, In Progress, Completed, Overdue |
| Next_Review | Date of next scheduled review |

**Step 5: Track Review Status**

| Status | Definition | Action |
|--------|------------|--------|
| Scheduled | Review planned, not started | Monitor for start date |
| In Progress | Review underway | Track completion |
| Completed | All activities finished | Document results |
| Overdue | Past planned date, not complete | Escalate |
| Cancelled | Review not proceeding | Document reason |

**Review Frequency Requirements:**

| Review Type | Minimum Frequency | Recommended |
|-------------|------------------|-------------|
| Annual Full Review | Once per year | Q1 each year |
| Quarterly Check | Four per year | Month following quarter end |
| Template Update | When changes occur | Within 30 days of change |
| Triggered | When trigger occurs | Within 14 days of trigger |

### 4.2 Sheet 3: Template_Adequacy – Completion Guide

**Purpose**: Assess whether NDA templates remain legally and operationally adequate.

**Step-by-Step Completion:**

**Step 1: List All Templates**

Import templates from ISMS-IMP-A.6.6.1:

| Field | Source |
|-------|--------|
| Template_ID | From Template Registry |
| Template_Name | From Template Registry |
| Template_Version | Current version number |
| Template_Type | Employee, Contractor, Vendor, etc. |

**Step 2: Check Legal Review Currency**

| Field | Guidance |
|-------|----------|
| Last_Legal_Review | Date Legal Counsel last reviewed |
| Legal_Review_Due | When next review required |
| Legal_Review_Status | Current, Due, Overdue |

**Legal Review Requirements:**

| Review Trigger | Required Action |
|----------------|-----------------|
| Annual cycle | Legal review every 12 months |
| Regulatory change | Immediate legal review |
| New information types | Review coverage adequacy |
| Incident or litigation | Review enforceability |

**Step 3: Assess Regulatory Currency**

| Check Item | Assessment |
|------------|------------|
| Data protection compliance | Template covers GDPR/FADP requirements |
| Industry regulations | Template covers sector-specific requirements |
| Employment law | Employee NDAs comply with employment law |
| International scope | Template suitable for jurisdictions used |

| Regulatory_Current | Definition |
|--------------------|------------|
| Yes | All regulatory requirements met |
| Partial | Some requirements met, gaps identified |
| No | Template does not meet current requirements |

**Step 4: Evaluate Coverage Adequacy**

Assess whether template covers all necessary elements:

| Coverage Element | Check |
|------------------|-------|
| All information classifications | Confidential, Restricted, Internal |
| All information types | Data, documents, systems, processes |
| Physical and digital | Both formats covered |
| Derivative information | Created from confidential information |
| Employee knowledge | Learned during employment |

| Covers_All_Info_Types | Definition |
|-----------------------|------------|
| Yes | All relevant information types covered |
| Partial | Some types covered, gaps identified |
| No | Significant coverage gaps |

**Step 5: Review Post-Termination Provisions**

| Check Item | Assessment |
|------------|------------|
| Duration stated | Clear post-termination period defined |
| Duration adequate | Period appropriate for information type |
| Survival clause | Key clauses explicitly survive |
| Return/destruction | Data handling obligations clear |

| Post_Term_Adequate | Definition |
|--------------------|------------|
| Yes | Post-termination provisions appropriate |
| No | Provisions missing or inadequate |
| Partial | Some provisions adequate, some not |

**Step 6: Assess Breach Remedies**

| Check Item | Assessment |
|------------|------------|
| Remedies specified | What happens on breach |
| Injunctive relief | Right to seek injunction |
| Damages | Liquidated damages or actual damages |
| Reporting obligations | Obligation to report breaches |

**Step 7: Verify Jurisdiction**

| Check Item | Assessment |
|------------|------------|
| Governing law | Appropriate governing law specified |
| Dispute resolution | Clear dispute resolution mechanism |
| Jurisdiction | Courts with jurisdiction identified |
| International applicability | Suitable for cross-border use |

**Step 8: Determine Overall Adequacy**

| Overall_Adequacy | Definition | Action |
|------------------|------------|--------|
| Adequate | Template meets all requirements | No action needed |
| Partially Adequate | Minor gaps or updates needed | Schedule updates |
| Inadequate | Significant deficiencies | Immediate update required |
| Not Assessed | Assessment not completed | Complete assessment |

### 4.3 Sheet 4: Coverage_Analysis – Completion Guide

**Purpose**: Verify that all required parties have current, executed NDAs.

**Step-by-Step Completion:**

**Step 1: Identify Stakeholder Categories**

| Category | Definition | NDA Requirement |
|----------|------------|-----------------|
| Permanent Employees | Full-time/part-time employees | 100% required |
| Temporary Employees | Fixed-term employees | 100% required |
| Contractors | Individual contractors | 100% required |
| Agency Staff | Staff from agencies | 100% required |
| Vendors | Companies providing services | 100% where data access |
| Partners | Business partners | 100% where data sharing |
| Consultants | External consultants | 100% required |
| Interns | Interns and trainees | 100% required |
| Board Members | Non-executive directors | 100% required |
| Visitors | Visitors to sensitive areas | Risk-based |

**Step 2: Gather Population Data**

For each category, obtain current counts:

| Data Source | Stakeholder Category | Data Required |
|-------------|----------------------|---------------|
| HR System | Employees (all types) | Current headcount by category |
| HR/Procurement | Contractors | Active contractor roster |
| Procurement | Vendors | Vendors with data access |
| Business Development | Partners | Active partner agreements |
| HR | Interns/Trainees | Current intern roster |
| Corporate Secretary | Board Members | Current board composition |

**Step 3: Count NDAs per Category**

From ISMS-IMP-A.6.6.2, count NDAs by category:

| Field | Calculation |
|-------|-------------|
| Total_Count | Total persons in category |
| NDA_Required | How many require NDA (may equal total) |
| NDA_Signed | Count with signed, valid NDA |
| Expired_NDAs | Count with expired NDA |
| Missing_NDAs | NDA_Required - NDA_Signed |

**Step 4: Calculate Coverage Rate**

```
Coverage_Rate = (NDA_Signed / NDA_Required) × 100%
```

**Coverage Targets:**

| Category | Target | Acceptable | Critical |
|----------|--------|------------|----------|
| Employees | 100% | ≥99% | <95% |
| Contractors | 100% | ≥98% | <90% |
| Vendors | 100% | ≥95% | <85% |
| Partners | 100% | ≥95% | <85% |
| All Others | 100% | ≥95% | <90% |

**Step 5: Identify Gap Status**

| Gap_Status | Definition | Action |
|------------|------------|--------|
| No Gap | Coverage at target | Monitor |
| Gap Identified | Coverage below target | Remediation required |
| Remediation In Progress | Gap being addressed | Track progress |
| Gap Closed | Remediation complete | Verify and close |

**Step 6: Assign Remediation Owners**

| Category | Default Owner |
|----------|---------------|
| Employees | HR Manager |
| Contractors | Procurement Manager |
| Vendors | Vendor Manager |
| Partners | Business Development |
| Board | Corporate Secretary |

### 4.4 Sheet 5: Compliance_Check – Completion Guide

**Purpose**: Verify individual NDA execution and storage compliance.

**Step-by-Step Completion:**

**Step 1: Identify NDAs to Check**

For annual full review, check all NDAs. For quarterly checks, sample or focus on:
- New NDAs since last check
- NDAs expiring soon
- NDAs flagged in previous review
- Random sample (10-20%)

**Step 2: Verify Correct Execution**

For each NDA, verify:

| Check Item | Verification Method |
|------------|---------------------|
| Correct parties | Names match contract parties |
| Authorised signatories | Signers have authority |
| All pages initialled | If required by template |
| All blanks completed | No missing information |
| Date completed | Execution date present |
| Witness (if required) | Witness signature present |

| Correctly_Executed | Definition |
|--------------------|------------|
| Yes | All execution requirements met |
| No | Execution deficiencies identified |

**Step 3: Verify Validity Period**

| Check Item | Verification |
|------------|--------------|
| Within validity period | Not expired |
| Expiry date known | Expiry date documented |
| Renewal tracking | Renewal process in place |

| Within_Validity | Definition |
|-----------------|------------|
| Yes | NDA currently valid |
| No | NDA expired |
| Perpetual | No expiry (perpetual NDA) |

**Step 4: Verify Appropriate Template**

| Check Item | Verification |
|------------|--------------|
| Correct template type | Employee NDA for employee, etc. |
| Current version | Not outdated template |
| Appropriate scope | Template scope matches relationship |

| Appropriate_Template | Definition |
|----------------------|------------|
| Yes | Correct, current template |
| No | Wrong or outdated template |

**Step 5: Verify All Signatures**

| Check Item | Verification |
|------------|--------------|
| Counterparty signature | Other party has signed |
| Organisation signature | Authorised representative signed |
| All required signatures | Multi-party NDAs fully signed |

| All_Parties_Signed | Definition |
|--------------------|------------|
| Yes | All required signatures present |
| No | Missing signatures |

**Step 6: Verify Secure Storage**

| Check Item | Verification |
|------------|--------------|
| Located in repository | NDA in designated storage |
| Access controlled | Appropriate access restrictions |
| Backup exists | Document backed up |
| Findable | Document can be located when needed |

| Securely_Stored | Definition |
|-----------------|------------|
| Yes | Meets storage requirements |
| No | Storage deficiencies |

**Step 7: Determine Overall Compliance**

| Overall_Compliance | Definition |
|--------------------|------------|
| Compliant | Meets all requirements |
| Partially Compliant | Minor issues, still enforceable |
| Non-Compliant | Significant issues affecting validity |

**Step 8: Document Actions Required**

For each non-compliant NDA:
- Document specific issues
- Identify action required
- Assign owner
- Set target date
- Add to Gap Register

### 4.5 Sheet 6: Gap_Register – Completion Guide

**Purpose**: Track all identified gaps from coverage analysis and compliance checks to resolution.

**Step-by-Step Completion:**

**Step 1: Generate Gap ID**

Create unique identifier using format `GAP-YYYY-NNN`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | GAP- | GAP- |
| Year | YYYY | 2026 |
| Sequence | NNN | 023 |
| Full ID | GAP-YYYY-NNN | GAP-2026-023 |

**Step 2: Classify Gap Type**

| Gap Type | Definition | Example |
|----------|------------|---------|
| Missing NDA | No NDA exists | New employee without NDA |
| Expired NDA | NDA past validity | NDA expired, not renewed |
| Inadequate Template | Wrong or outdated template | Old version used |
| Unsigned | NDA exists but not signed | Draft not executed |
| Wrong Template | Incorrect template type | Vendor NDA for employee |
| Storage Issue | NDA not properly stored | Original missing |
| Execution Error | Improperly executed | Missing signatures |
| Coverage Gap | Category has systematic gap | Contractor category at 85% |
| Other | Other gap type | Document specific |

**Step 3: Document Gap Details**

| Field | Guidance |
|-------|----------|
| Description | Clear description of the gap |
| Affected_Area | Who or what is affected |
| Source_Review | Which review identified this gap |
| NDA_Reference | If specific NDA, reference it |

**Step 4: Assign Severity**

| Severity | Definition | Target Resolution |
|----------|------------|-------------------|
| Critical | Person with active access has no NDA | 5 business days |
| High | NDA expired, relationship ongoing | 30 days |
| Medium | Wrong template used, NDA exists | 60 days |
| Low | Minor clause missing, NDA valid | 90 days |

**Severity Assessment Matrix:**

| Access Level | No NDA | Expired NDA | Wrong Template |
|--------------|--------|-------------|----------------|
| Active system access | Critical | Critical | High |
| Data access only | Critical | High | Medium |
| Limited access | High | Medium | Low |
| No current access | Medium | Low | Low |

**Step 5: Assign Owner and Remediation**

| Field | Guidance |
|-------|----------|
| Owner | Person responsible for remediation |
| Remediation_Action | Specific action to resolve gap |
| Target_Date | Resolution deadline per severity |
| Dependencies | Any dependencies on other actions |

**Step 6: Track Status**

| Status | Definition | Action |
|--------|------------|--------|
| Open | Gap identified, not started | Begin remediation |
| In Progress | Remediation underway | Track progress |
| Remediated | Action completed | Verify closure |
| Verified Closed | Closure verified | Archive |
| Risk Accepted | Gap accepted with risk | Document risk acceptance |

**Step 7: Verify Closure**

Before marking verified closed:
- Confirm action completed
- Verify gap resolved
- Collect evidence
- Update source workbooks

### 4.6 Sheet 7: Evidence_Register – Completion Guide

**Purpose**: Link review activities to supporting evidence for audit purposes.

**Step-by-Step Completion:**

**Step 1: Generate Evidence ID**

Create unique identifier using format `EVD-YYYY-NNN`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | EVD- | EVD- |
| Year | YYYY | 2026 |
| Sequence | NNN | 045 |
| Full ID | EVD-YYYY-NNN | EVD-2026-045 |

**Step 2: Classify Evidence Type**

| Evidence Type | Description |
|---------------|-------------|
| Review Report | Completed review documentation |
| Coverage Analysis | Coverage analysis export |
| Template Assessment | Template adequacy documentation |
| Gap Remediation | Evidence of gap closure |
| Approval Record | Signed approval |
| Legal Review | Legal Counsel review documentation |
| Data Extract | Source data used for analysis |

**Step 3: Document Evidence Details**

| Field | Guidance |
|-------|----------|
| Evidence_Description | Clear description of evidence |
| Related_Review | Link to review ID |
| Related_Gap | Link to gap ID (if applicable) |
| Evidence_Date | Date evidence created |
| Author | Who created evidence |
| Storage_Location | Where evidence is stored |
| Retention_Period | How long to retain |

**Step 4: Verify Evidence Quality**

Before linking evidence, verify:
- Evidence is complete
- Evidence is legible
- Evidence supports finding/action
- Evidence is properly dated
- Evidence is securely stored

### 4.7 Sheet 8: Approval_SignOff – Completion Guide

**Purpose**: Obtain formal approval of review completion and findings.

**Step-by-Step Completion:**

**Step 1: Document Review Summary**

Summarise review results:
- Review type and scope
- Key findings
- Gap count and severity
- Remediation status
- Recommendations

**Step 2: Obtain Approvals**

| Approver | Approval Scope | Documentation |
|----------|----------------|---------------|
| Reviewer | Review findings accurate | Reviewer sign-off |
| ISM | Review complete, gaps tracked | ISM sign-off |
| CISO | Overall review results | CISO sign-off |

**Step 3: Record Approval Details**

| Field | Guidance |
|-------|----------|
| Approver_Name | Full name |
| Approver_Role | Position/title |
| Approval_Date | Date approved |
| Approval_Scope | What is being approved |
| Comments | Any approver comments |
| Signature | Digital or physical signature |

---

## 5. Evidence Collection

### 5.1 Evidence Requirements

Evidence must be collected for all review activities:

| Evidence Category | Retention Period | Storage Location |
|-------------------|------------------|------------------|
| Review reports | 7 years | ISMS Evidence Library |
| Coverage analyses | 7 years | ISMS Evidence Library |
| Template assessments | 7 years | ISMS Evidence Library |
| Gap records | 7 years | ISMS Evidence Library |
| Approval records | 7 years | ISMS Evidence Library |
| Source data | 3 years | ISMS Evidence Library |

### 5.2 Evidence Folder Structure

```
ISMS-Evidence-Library/
└── NDA-Management/
    └── A.6.6-Confidentiality-NDAs/
        └── Reviews/
            └── [REV-ID]/
                ├── Review-Report.pdf
                ├── Template-Assessment.xlsx
                ├── Coverage-Analysis.xlsx
                ├── Compliance-Checks.xlsx
                ├── Gap-Register.xlsx
                └── Approval-SignOff.pdf
```

### 5.3 Evidence for Audit

During ISO 27001 audit, be prepared to demonstrate:

| Auditor Request | Evidence to Provide |
|-----------------|---------------------|
| "How do you review NDAs?" | Review procedure + recent review report |
| "Show me NDA coverage" | Coverage analysis with current data |
| "How do you track NDA gaps?" | Gap register with resolution evidence |
| "When was last review?" | Sheet 2 review schedule |
| "Who approves reviews?" | Sheet 8 approval records |
| "How current are templates?" | Sheet 3 template assessment |

---

## 6. Common Pitfalls

### 6.1 Review Process Errors

❌ **MISTAKE: Reviews not conducted regularly**
NDAs must be reviewed at least annually with quarterly checks. Missing reviews creates compliance gaps.

❌ **MISTAKE: Coverage analysis against outdated headcount**
Use current HR/vendor data. Outdated data produces inaccurate coverage metrics.

❌ **MISTAKE: Template review without legal involvement**
Legal Counsel must review template adequacy. ISM cannot assess legal sufficiency.

❌ **MISTAKE: Reviews not documented**
Undocumented reviews have no audit value. Formal records with findings required.

### 6.2 Gap Management Errors

❌ **MISTAKE: Gaps identified but not remediated**
Every gap must be tracked to verified closure. Unfixed gaps remain as risks.

❌ **MISTAKE: No ownership of gaps**
Every gap must have an assigned owner. Unowned gaps don't get fixed.

❌ **MISTAKE: Severity not assigned to gaps**
Gaps without severity are prioritised incorrectly. Critical gaps may not be addressed first.

❌ **MISTAKE: No trend analysis of gaps**
Track gap trends over time to identify systemic issues. Recurring gaps indicate process failures.

### 6.3 Coverage Analysis Errors

❌ **MISTAKE: Compliance check only on sample**
Annual review should check all NDAs. Sampling may miss compliance issues.

❌ **MISTAKE: Not verifying NDA existence, just counting**
Coverage analysis must verify NDAs actually exist and are valid, not just count records.

❌ **MISTAKE: Excluding categories from coverage analysis**
All categories requiring NDAs must be included. Exclusions create blind spots.

### 6.4 Template Assessment Errors

❌ **MISTAKE: Assuming templates are adequate without assessment**
Templates require periodic legal review. Laws change, templates may become inadequate.

❌ **MISTAKE: Not checking post-termination provisions**
Post-termination obligations are critical. Inadequate provisions reduce protection.

❌ **MISTAKE: Not verifying jurisdiction appropriateness**
Templates must be appropriate for all jurisdictions used. Multi-jurisdiction use requires verification.

---

## 7. Quality Checklist

### 7.1 Pre-Review Checklist

Before starting review:

- [ ] Review type and scope defined
- [ ] Source data obtained (HR, vendor lists)
- [ ] Previous review findings available
- [ ] Template registry current
- [ ] NDA execution register current
- [ ] Reviewers identified and available

### 7.2 Review Completion Checklist

Before marking review complete:

- [ ] All templates assessed for adequacy
- [ ] Coverage analysis complete for all categories
- [ ] Compliance check performed (all or sample per review type)
- [ ] All gaps documented with owners and targets
- [ ] Evidence register updated
- [ ] Approval sign-offs obtained

### 7.3 Gap Closure Checklist

Before marking gap verified closed:

- [ ] Remediation action completed
- [ ] Gap actually resolved
- [ ] Evidence collected
- [ ] Source workbook updated
- [ ] Verifier confirmed closure

---

## 8. Review and Approval

### 8.1 Review Authority

| Review Activity | Authority |
|-----------------|-----------|
| Conduct review | Information Security Manager |
| Template adequacy assessment | Legal Counsel |
| Gap remediation assignment | Relevant Department Head |
| Review sign-off | CISO |

### 8.2 Escalation Process

| Trigger | Escalation Path |
|---------|-----------------|
| Critical gap not remediated in 5 days | ISM → CISO |
| High gap not remediated in 30 days | ISM → Department Head → CISO |
| Coverage below 90% | ISM → CISO → Executive |
| Review overdue by 30 days | ISM → CISO |

### 8.3 Review Workflow

```
Review Scheduled
         ↓
Data Collection (HR, Vendors, Templates)
         ↓
Assessment Execution (Templates, Coverage, Compliance)
         ↓
Gap Identification and Documentation
         ↓
Remediation Assignment
         ↓
Review Report Preparation
         ↓
ISM Review and Sign-off
         ↓
CISO Approval
         ↓
Evidence Filing
         ↓
Next Review Scheduling
```

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
