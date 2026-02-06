# ISMS-IMP-A.6.4-5.S1 - Disciplinary Process Assessment

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.4-5.S1 |
| **Title** | Disciplinary Process Assessment |
| **Control Reference** | ISO/IEC 27001:2022 A.6.4, A.6.5 |
| **Control Name** | Disciplinary Process / Responsibilities After Termination |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Chief Human Resources Officer (CHRO) |
| **Classification** | Internal |
| **Framework Version** | 1.0 |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Violation Categories](#14-violation-categories)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 Investigation Framework](#17-investigation-framework)
   - [1.8 Due Process Requirements](#18-due-process-requirements)
   - [1.9 Evidence Collection](#19-evidence-collection)
   - [1.10 Common Pitfalls](#110-common-pitfalls)
   - [1.11 Quality Checklist](#111-quality-checklist)
   - [1.12 Review and Approval](#112-review-and-approval)
   - [1.13 Regulatory Compliance](#113-regulatory-compliance)
   - [1.14 Related Controls](#114-related-controls)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Architecture](#21-workbook-architecture)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Data Validations](#23-data-validations)
   - [2.4 Conditional Formatting](#24-conditional-formatting)
   - [2.5 Formula Specifications](#25-formula-specifications)
   - [2.6 Cell Styling Standards](#26-cell-styling-standards)
   - [2.7 Generator Script Reference](#27-generator-script-reference)

---

# PART I: USER COMPLETION GUIDE

---

## 1.1 Assessment Overview

### Purpose

This workbook establishes and maintains the organisation's disciplinary process framework for addressing information security policy violations. It serves as the operational tool for:

- **Violation Classification**: Standardised categorisation of security violations by severity
- **Investigation Tracking**: Documented investigation procedures and evidence collection
- **Response Framework**: Graduated disciplinary responses aligned with violation severity
- **Due Process Compliance**: Ensuring fair treatment consistent with employment law
- **Escalation Management**: Clear escalation paths for serious violations
- **Trend Analysis**: Pattern identification for preventive measures

The disciplinary process is fundamental to an effective ISMS. Without formal, documented procedures for handling security violations, organisations cannot demonstrate the deterrent effect required by ISO 27001:2022 Control A.6.4.

### Scope

This assessment covers the following components:

**In Scope:**
- Information security policy violation categories
- Disciplinary investigation procedures
- Response matrix linking violations to consequences
- Due process requirements and employee rights
- Escalation and notification procedures
- Documentation and evidence requirements
- Appeal processes
- Integration with HR disciplinary frameworks
- Security team involvement criteria
- External notification requirements (regulators, law enforcement)

**Out of Scope:**
- Employment exit procedures (covered in ISMS-IMP-A.6.4-5.S2)
- Post-employment obligations (covered in ISMS-IMP-A.6.4-5.S3)
- General HR misconduct not related to information security
- Third-party/vendor disciplinary matters (covered in A.5.19-23)

### Business Value

A well-defined disciplinary process delivers:

| Value Area | Benefit |
|------------|---------|
| **Deterrence** | Clear consequences discourage policy violations |
| **Consistency** | Fair, uniform treatment across all personnel |
| **Legal Protection** | Defensible actions if challenged |
| **Audit Compliance** | Documented processes for ISO 27001 certification |
| **Culture Building** | Reinforces security-aware organisational culture |
| **Risk Reduction** | Identifies patterns enabling preventive action |

### Assessment Frequency

| Activity | Frequency | Responsible Party |
|----------|-----------|-------------------|
| Disciplinary Process Review | Annual | HR Director with CISO |
| Violation Category Review | Annual | Information Security Manager |
| Case Documentation Audit | Quarterly | Internal Audit |
| Response Matrix Validation | Annual | Legal Counsel |
| Trend Analysis | Quarterly | Information Security Manager |

---

## 1.2 Control Requirements

### ISO 27001:2022 Control A.6.4 - Disciplinary Process

> *"A disciplinary process should be formalized and communicated to take actions against personnel and other relevant interested parties who have committed an information security policy violation."*

**Control Type:** Corrective, Preventive
**Security Properties:** Confidentiality, Integrity, Availability
**Cybersecurity Concepts:** Protect, Respond
**Operational Capabilities:** Human Resource Security

### Implementation Requirements

Control A.6.4 requires organisations to establish:

**1. Formalisation**
- Documented disciplinary procedures specific to security violations
- Clear categorisation of violation types and severity levels
- Defined investigation processes
- Documented response options for each violation category

**2. Communication**
- Employees informed of disciplinary procedures during onboarding
- Procedures accessible to all personnel
- Regular reminders of policies and consequences
- Clear reporting channels for violations

**3. Graduated Response**
- Response proportionate to violation severity
- Consideration of intentionality (malicious vs. accidental)
- Review of prior violations and training history
- Escalation procedures for repeated or serious violations

**4. Legal Compliance**
- Alignment with employment law requirements
- Due process provisions
- Appeal mechanisms
- Privacy protection for individuals under investigation

### What Auditors Look For

ISO 27001 auditors examining Control A.6.4 will verify:

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Documented Procedures** | Formal disciplinary policy with security-specific provisions |
| **Violation Categories** | Defined categories with severity levels |
| **Response Matrix** | Clear linkage between violations and consequences |
| **Investigation Process** | Documented investigation procedures |
| **Due Process** | Employee rights and appeal mechanisms |
| **Case Records** | Anonymised records demonstrating process compliance |
| **Communication Evidence** | Training records, policy acknowledgements |
| **Integration** | Links to HR disciplinary framework |

---

## 1.3 Prerequisites

### Before Starting This Assessment

Complete the following prerequisites to ensure successful assessment completion:

#### Required Access

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| HR Information System | Read/Write | Access to personnel records |
| Security Incident System | Read | Review of security violations |
| Policy Repository | Read | Access to current policies |
| Legal/Compliance Repository | Read | Employment law references |
| ISMS Evidence Library | Write | Upload evidence |

#### Required Information

| Information | Source | Why Needed |
|-------------|--------|------------|
| Current disciplinary policy | HR Department | Baseline review |
| Employment contracts (template) | HR/Legal | Terms and conditions review |
| Security policies | ISMS Documentation | Violation definition source |
| Historical violation records | Security/HR | Trend analysis |
| Employment law requirements | Legal Counsel | Compliance verification |
| Union/works council agreements | HR/Legal | Procedural requirements |

#### Required Approvals

| Approval | Approver | When Needed |
|----------|----------|-------------|
| Access to disciplinary records | HR Director | Before starting |
| Review of legal requirements | Legal Counsel | Before starting |
| Security policy interpretation | CISO | During assessment |

#### Prerequisite Checklist

Before proceeding, verify:

- [ ] Current disciplinary policy obtained from HR
- [ ] Employment law requirements understood (Swiss OR, nDSG)
- [ ] Security policy suite accessible
- [ ] Historical violation data available (anonymised)
- [ ] Legal Counsel available for consultation
- [ ] HR Director briefed on assessment purpose
- [ ] Works council/union requirements understood (if applicable)

---

## 1.4 Violation Categories

### Understanding Violation Severity

Effective disciplinary processes require consistent violation categorisation. The following framework provides guidance:

#### Category 1: Minor/Inadvertent Violations

| Characteristic | Description |
|----------------|-------------|
| **Nature** | Accidental or unintentional policy breach |
| **Intent** | No malicious intent evident |
| **Impact** | Minimal or no actual harm |
| **Examples** | Leaving screen unlocked, minor password sharing, accidental email misdirection |
| **Typical Response** | Verbal warning, additional training |
| **Escalation Trigger** | Third occurrence within 12 months |

#### Category 2: Moderate Violations

| Characteristic | Description |
|----------------|-------------|
| **Nature** | Repeated minor violations or negligent behaviour |
| **Intent** | Carelessness or disregard for policy |
| **Impact** | Potential for harm, no actual breach |
| **Examples** | Repeated acceptable use violations, sharing credentials, bypassing controls |
| **Typical Response** | Written warning, mandatory retraining |
| **Escalation Trigger** | Second occurrence or actual data exposure |

#### Category 3: Serious Violations

| Characteristic | Description |
|----------------|-------------|
| **Nature** | Deliberate policy violation or significant negligence |
| **Intent** | Intentional or reckless disregard |
| **Impact** | Actual or significant potential harm |
| **Examples** | Deliberate data exfiltration attempt, access abuse, security control circumvention |
| **Typical Response** | Final written warning, suspension, termination |
| **Escalation Trigger** | Any occurrence of gross misconduct |

#### Category 4: Gross Misconduct

| Characteristic | Description |
|----------------|-------------|
| **Nature** | Severe violation warranting immediate action |
| **Intent** | Malicious or criminal intent |
| **Impact** | Significant harm or criminal activity |
| **Examples** | Data theft, sabotage, fraud, selling access credentials |
| **Typical Response** | Immediate dismissal, legal action |
| **Reporting** | Law enforcement, regulators as required |

### Categorisation Decision Tree

```
Is information security policy implicated?
├── NO → Refer to general HR disciplinary
└── YES → Continue...
    │
    └── Was the action intentional/malicious?
        ├── YES → Category 3 or 4 (based on impact)
        └── NO → Continue...
            │
            └── Did actual harm occur?
                ├── YES → Category 2 or 3 (based on severity)
                └── NO → Continue...
                    │
                    └── Is this a repeat violation?
                        ├── YES → Category 2
                        └── NO → Category 1
```

---

## 1.5 Workbook Structure

### Sheet Overview

The workbook consists of seven sheets, each serving a specific purpose in the disciplinary process framework:

| Sheet | Purpose | Primary User | Update Frequency |
|-------|---------|--------------|------------------|
| **Instructions** | Guidance and orientation | All users | As needed |
| **Violation_Categories** | Standardised violation classification | ISM, HR | Annual |
| **Response_Matrix** | Violation-to-consequence mapping | HR, Legal | Annual |
| **Investigation_Process** | Investigation procedure documentation | HR, Security | Annual |
| **Case_Tracker** | Active and historical case tracking | HR | Ongoing |
| **Evidence_Register** | Evidence tracking and links | HR, ISM | Ongoing |
| **Approval_SignOff** | Assessment authorisation | Approvers | At completion |

### Sheet Relationships

```
┌─────────────────┐
│  Instructions   │ ◄── Start here
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│Violation_       │────►│ Response_Matrix │
│Categories       │     │                 │
└────────┬────────┘     └─────────────────┘
         │                      │
         │                      │ (links by Category)
         ▼                      │
┌─────────────────┐     ┌───────┴─────────┐
│Investigation_   │◄────┤  Case_Tracker   │
│Process          │     │                 │
└────────┬────────┘     └─────────────────┘
         │
         ▼
┌─────────────────┐
│Evidence_Register│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Approval_SignOff│ ◄── Complete here
└─────────────────┘
```

---

## 1.6 Completion Walkthrough

### Step 1: Review Instructions Sheet

**Time estimate:** 10-15 minutes

1. Read the document purpose and scope section
2. Note the contact information for queries
3. Understand the relationship to ISMS-POL-A.6.4-5
4. Review regulatory compliance requirements
5. Identify key stakeholders for completion

### Step 2: Complete Violation_Categories Sheet

**Time estimate:** 2-3 hours

Document all information security violation categories:

#### Column A: Category_ID

- **Format:** VIOL-XXX
- **Example:** VIOL-001
- **Rules:** Sequential numbering within severity level

#### Column B: Category_Name

- **Format:** Descriptive name
- **Example:** Unauthorized Data Sharing
- **Rules:** Clear, unambiguous terminology

#### Column C: Severity_Level

- **Format:** Select from dropdown
- **Options:** Minor, Moderate, Serious, Gross Misconduct
- **Rules:** Align with response matrix

#### Column D: Description

- **Format:** Detailed description of the violation type
- **Example:** Sharing confidential data with unauthorised parties via email, file transfer, or verbal disclosure
- **Rules:** Sufficient detail for consistent classification

#### Column E: Examples

- **Format:** Specific examples of this violation type
- **Example:** Forwarding confidential emails to personal accounts, sharing credentials
- **Rules:** Include both obvious and edge cases

#### Column F: Investigation_Required

- **Format:** Yes/No
- **Rules:** Generally "Yes" for Moderate and above

#### Column G: Security_Team_Involvement

- **Format:** Yes/No/Conditional
- **Rules:** Define when security team must be involved

#### Column H: Related_Policy

- **Format:** Policy document reference
- **Example:** ISMS-POL-A.5.10 Acceptable Use
- **Rules:** Link to specific policy section violated

### Step 3: Complete Response_Matrix Sheet

**Time estimate:** 2-3 hours

Map violations to appropriate responses:

#### Column A: Severity_Level

- Link to Violation_Categories severity levels

#### Column B: First_Occurrence

- **Format:** Standard response for first violation
- **Example:** Verbal warning with documented counselling

#### Column C: Second_Occurrence

- **Format:** Escalated response
- **Example:** Written warning with mandatory retraining

#### Column D: Third_Occurrence

- **Format:** Further escalated response
- **Example:** Final written warning with performance improvement plan

#### Column E: Immediate_Actions

- **Format:** Actions required immediately upon discovery
- **Example:** Preserve logs, suspend access (if serious)

#### Column F: Mitigating_Factors

- **Format:** Factors that may reduce response severity
- **Example:** Prompt self-reporting, no prior violations, inadequate training

#### Column G: Aggravating_Factors

- **Format:** Factors that may increase response severity
- **Example:** Attempted concealment, abuse of privileged access, harm to third parties

### Step 4: Complete Investigation_Process Sheet

**Time estimate:** 2-3 hours

Document investigation procedures:

#### Column A: Phase

- **Format:** Investigation phase name
- **Options:** Discovery, Assessment, Investigation, Decision, Action, Follow-up

#### Column B: Activities

- **Format:** Activities performed in this phase
- Detailed step-by-step activities

#### Column C: Timeline

- **Format:** Expected duration
- **Example:** Within 2 business days

#### Column D: Responsible_Party

- **Format:** Role(s) responsible
- **Example:** HR Manager, Security Team

#### Column E: Outputs

- **Format:** Required outputs from this phase
- **Example:** Investigation report, evidence log

#### Column F: Documentation_Required

- **Format:** Specific documentation to produce
- **Example:** Interview notes, forensic report

### Step 5: Complete Case_Tracker Sheet

**Time estimate:** Ongoing

Track active and historical disciplinary cases:

#### Column A: Case_ID

- **Format:** DISC-YYYY-XXX
- **Example:** DISC-2026-001

#### Column B: Date_Reported

- **Format:** DD.MM.YYYY

#### Column C: Violation_Category

- Link to Violation_Categories

#### Column D: Status

- **Options:** Under Investigation, Pending Decision, Action Taken, Closed, Appealed

#### Column E: Investigation_Lead

- **Format:** Name of investigator

#### Column F: Date_Closed

- **Format:** DD.MM.YYYY (when closed)

#### Column G: Outcome

- **Format:** Summary of disciplinary action taken

#### Column H: Notes

- **Format:** Additional relevant information

**Important:** Case records should be anonymised for audit purposes. Link detailed records securely.

### Step 6: Complete Evidence_Register Sheet

**Time estimate:** 30-60 minutes

Document evidence supporting the disciplinary framework:

#### Column A: Evidence_ID

- **Format:** EVD-A.6.4.1-XXX

#### Column B: Evidence_Description

- What the evidence demonstrates

#### Column C: Evidence_Type

- **Options:** Policy Document, Procedure, Training Record, Case Record, Communication

#### Column D: Storage_Location

- ISMS Evidence Library path

#### Column E: Collection_Date

- **Format:** DD.MM.YYYY

#### Column F: Collected_By

- Name of collector

### Step 7: Complete Approval_SignOff Sheet

**Time estimate:** 15-30 minutes

Obtain required authorisations:

1. Complete assessor information
2. Enter assessment completion date
3. Route to HR Director for review
4. Obtain Legal Counsel sign-off
5. Secure CISO final approval

---

## 1.7 Investigation Framework

### Investigation Principles

All investigations must adhere to these principles:

| Principle | Description |
|-----------|-------------|
| **Impartiality** | Investigator independent from the matter |
| **Confidentiality** | Information shared only on need-to-know basis |
| **Documentation** | All steps and findings documented |
| **Timeliness** | Investigations completed within defined timeframes |
| **Proportionality** | Investigation depth matched to violation severity |
| **Evidence Preservation** | Digital evidence preserved per forensic standards |

### Investigation Phases

#### Phase 1: Discovery and Initial Assessment (1-2 business days)

- Receive violation report
- Conduct preliminary assessment
- Determine if investigation warranted
- Identify investigation lead
- Implement immediate protective measures if needed

#### Phase 2: Investigation Planning (1 business day)

- Define investigation scope
- Identify evidence sources
- Plan interviews
- Coordinate with Security Team (if required)
- Notify Legal if serious violation

#### Phase 3: Evidence Collection (2-5 business days)

- Collect and preserve digital evidence
- Conduct interviews
- Review relevant documentation
- Analyse logs and access records
- Document chain of custody

#### Phase 4: Analysis and Findings (2-3 business days)

- Analyse collected evidence
- Determine facts and timeline
- Assess violation severity
- Identify mitigating/aggravating factors
- Prepare investigation report

#### Phase 5: Decision and Action (1-2 business days)

- Review investigation findings with decision-makers
- Determine appropriate disciplinary action
- Document decision rationale
- Communicate decision to individual
- Implement disciplinary action

#### Phase 6: Follow-up and Closure (Ongoing)

- Monitor compliance with disciplinary requirements
- Process any appeals
- Update case records
- Conduct trend analysis
- Implement preventive measures

---

## 1.8 Due Process Requirements

### Employee Rights

All individuals subject to disciplinary investigation have the following rights:

| Right | Description |
|-------|-------------|
| **Notification** | Informed of allegations in writing |
| **Response Opportunity** | Chance to respond before decision |
| **Representation** | Right to be accompanied in meetings |
| **Evidence Access** | Ability to view evidence (where appropriate) |
| **Appeal** | Right to appeal disciplinary decisions |
| **Confidentiality** | Identity protected where possible |
| **Timely Resolution** | Investigation completed within reasonable timeframe |

### Appeal Process

#### Grounds for Appeal

- Procedural unfairness
- New evidence available
- Disproportionate sanction
- Factual errors in findings

#### Appeal Timeline

| Stage | Timeline |
|-------|----------|
| Submit appeal | Within 5 business days of decision |
| Acknowledge receipt | Within 2 business days |
| Appeal hearing | Within 10 business days |
| Appeal decision | Within 5 business days of hearing |

#### Appeal Decision-Makers

| Original Decision By | Appeal Heard By |
|---------------------|-----------------|
| Line Manager | HR Director |
| HR Director | Executive Management |
| Executive Management | External independent panel |

---

## 1.9 Evidence Collection

### Evidence Requirements

| Evidence Type | Description | Retention Period | Storage Location |
|---------------|-------------|------------------|------------------|
| **Disciplinary Policy** | Current policy document | Life of policy + 7 years | ISMS Evidence Library |
| **Violation Categories** | Category definitions | Current version | ISMS Evidence Library |
| **Response Matrix** | Response mapping | Current version | ISMS Evidence Library |
| **Investigation Procedures** | Documented procedures | Current version | ISMS Evidence Library |
| **Case Records (anonymised)** | Sample completed cases | 7 years from closure | HR Confidential |
| **Training Records** | Policy acknowledgements | Employment + 7 years | HR System |
| **Completed Workbook** | This assessment | 3 assessment cycles | ISMS Evidence Library |

### Evidence Collection Process

#### Step 1: Gather Framework Documents

1. Collect current disciplinary policy
2. Verify version currency
3. Check approval dates
4. Store in ISMS Evidence Library

#### Step 2: Document Process Evidence

1. Investigation procedure documentation
2. Due process provisions
3. Appeal process documentation
4. Template forms and checklists

#### Step 3: Compile Case Evidence

1. Request anonymised case samples from HR
2. Verify cases demonstrate process compliance
3. Redact personal identifiers
4. Store securely with access controls

### Evidence Storage Standards

**Naming Convention:**
```
EVD-A.6.4.1_[EvidenceType]_[YYYYMMDD].[ext]
```

**Examples:**
- `EVD-A.6.4.1_DisciplinaryPolicy_20260203.pdf`
- `EVD-A.6.4.1_ResponseMatrix_20260203.xlsx`
- `EVD-A.6.4.1_CaseSample_Anonymised_20260203.pdf`

---

## 1.10 Common Pitfalls

Avoid these common mistakes when implementing the disciplinary process:

### Process Design Pitfalls

**MISTAKE**: No security-specific disciplinary provisions
**CORRECT**: Develop information security-specific violation categories and responses integrated with general HR disciplinary policy; ensure security team involvement criteria are defined; document when technical investigation is required

**MISTAKE**: One-size-fits-all response approach
**CORRECT**: Implement graduated response matrix with escalation based on severity, intentionality, and repetition; document mitigating and aggravating factors; allow flexibility within defined parameters

**MISTAKE**: Unclear violation categories
**CORRECT**: Define specific, unambiguous violation categories with clear examples; avoid overlap between categories; include edge case guidance; train managers on categorisation

**MISTAKE**: No consideration of intent
**CORRECT**: Explicitly assess whether violation was intentional (malicious), negligent, or accidental; adjust response accordingly; document intent assessment in investigation findings

### Investigation Pitfalls

**MISTAKE**: Investigation by involved parties
**CORRECT**: Ensure investigator independence; escalate to HR or external party if line manager potentially involved; document investigator selection rationale

**MISTAKE**: Poor evidence preservation
**CORRECT**: Implement digital evidence preservation procedures; involve Security Team for technical evidence; maintain chain of custody documentation; follow forensic standards for serious violations

**MISTAKE**: Delayed investigations
**CORRECT**: Define and enforce investigation timelines; escalate delays to senior management; communicate timeline to individual under investigation; document any extensions with justification

**MISTAKE**: Inconsistent documentation
**CORRECT**: Use standardised templates for investigation reports; document all interviews and findings; maintain comprehensive case files; enable audit trail of investigation steps

### Legal Compliance Pitfalls

**MISTAKE**: Ignoring employment law requirements
**CORRECT**: Consult Legal Counsel when developing procedures; ensure compliance with Swiss OR requirements; respect notice periods and due process; consider works council obligations

**MISTAKE**: No appeal mechanism
**CORRECT**: Establish clear appeal process with defined grounds, timelines, and decision-makers; document appeal procedures; communicate appeal rights in all disciplinary decisions

**MISTAKE**: Inadequate confidentiality protection
**CORRECT**: Protect identity of individuals under investigation; limit information to need-to-know basis; secure storage of case files; anonymise records for trend analysis

**MISTAKE**: Missing external notification requirements
**CORRECT**: Define criteria for regulatory notification (FDPIC for data breaches); establish law enforcement referral process; document notification decisions and rationale

### Communication Pitfalls

**MISTAKE**: Policies not communicated to staff
**CORRECT**: Include disciplinary procedures in onboarding; require policy acknowledgement; conduct regular awareness reminders; ensure accessibility of policy documents

**MISTAKE**: Unclear escalation paths
**CORRECT**: Document escalation criteria and contacts; define when Security Team, Legal, and Executive Management must be involved; communicate escalation procedures to relevant parties

---

## 1.11 Quality Checklist

Before submitting the completed assessment, verify all items:

### Process Framework Checks

- [ ] Violation categories comprehensive and unambiguous
- [ ] All severity levels defined with clear criteria
- [ ] Response matrix complete for all severity levels
- [ ] Escalation triggers documented for each category
- [ ] Investigation procedures documented by phase
- [ ] Timeline targets defined for each phase

### Legal Compliance Checks

- [ ] Due process requirements documented
- [ ] Employee rights clearly stated
- [ ] Appeal process defined with grounds and timelines
- [ ] Confidentiality provisions included
- [ ] External notification criteria defined
- [ ] Legal Counsel has reviewed response matrix

### Integration Checks

- [ ] Security Team involvement criteria defined
- [ ] Links to relevant security policies documented
- [ ] Integration with HR disciplinary process confirmed
- [ ] Incident management interface documented
- [ ] Access revocation triggers defined

### Evidence Checks

- [ ] All framework documents stored in Evidence Library
- [ ] Sample case records available (anonymised)
- [ ] Policy acknowledgement process documented
- [ ] Evidence naming convention followed
- [ ] Storage locations verified accessible

### Approval Checks

- [ ] Assessor information complete
- [ ] HR Director review obtained
- [ ] Legal Counsel sign-off obtained
- [ ] CISO final approval obtained

---

## 1.12 Review and Approval

### Review Process

The completed Disciplinary Process Assessment must follow this review process:

#### Step 1: Self-Review by Assessor

- Complete Quality Checklist (Section 1.11)
- Verify all sheets are complete
- Check for obvious errors
- Ensure evidence is properly linked

#### Step 2: HR Director Review

**Reviewer:** HR Director
**Timeframe:** Within 5 business days

**Review scope:**
- Process alignment with HR practices
- Employment law compliance
- Practical implementability
- Resource requirements

**Outcome:** Approve, Return for corrections, or Escalate

#### Step 3: Legal Counsel Review

**Reviewer:** Legal Counsel
**Timeframe:** Within 10 business days

**Review scope:**
- Employment law compliance (Swiss OR, nDSG)
- Due process adequacy
- Appeal process validity
- External notification requirements

**Outcome:** Approve or Return for corrections

#### Step 4: CISO Final Approval

**Approver:** CISO
**Timeframe:** Within 5 business days

**Approval scope:**
- Security control effectiveness
- Integration with ISMS
- Audit readiness
- Risk acceptance

**Outcome:** Approve or Reject

### Post-Approval Actions

Upon approval:

1. Upload completed workbook to ISMS Evidence Library
2. Update ISMS control status
3. Communicate changes to relevant parties
4. Schedule next assessment
5. Update training materials if needed

---

## 1.13 Regulatory Compliance

### Employment Law Requirements

#### Swiss Code of Obligations (OR)

| Requirement | Disciplinary Implication |
|-------------|--------------------------|
| **Art. 328 Employee Protection** | Fair treatment, protection of personality |
| **Art. 337 Summary Dismissal** | Only for gross misconduct; burden of proof on employer |
| **Art. 336 Unfair Dismissal** | Avoid retaliatory or discriminatory dismissal |
| **Notice Periods** | Must be respected unless gross misconduct |

#### Swiss Data Protection (nDSG)

| Requirement | Disciplinary Implication |
|-------------|--------------------------|
| **Proportionality** | Investigation scope proportionate to violation |
| **Transparency** | Individual informed of data processing |
| **Purpose Limitation** | Data used only for investigation |
| **Data Minimisation** | Collect only necessary information |

### Regulatory Notification Requirements

| Trigger | Notification Required | Timeline |
|---------|----------------------|----------|
| **Data Breach (personal data)** | FDPIC notification | Without delay |
| **Criminal Activity** | Law enforcement referral | As appropriate |
| **FINMA-regulated activities** | FINMA notification | Per FINMA requirements |
| **Serious security incident** | Per incident response plan | Per plan |

---

## 1.14 Related Controls

### Primary Control Relationships

| Control | Relationship | Integration Point |
|---------|--------------|-------------------|
| **A.5.24-28** Incident Management | Upstream | Security incidents may trigger disciplinary |
| **A.6.5** Post-Employment | Downstream | Termination may result from disciplinary |
| **A.5.1** Information Security Policy | Reference | Policies define violation criteria |
| **A.6.3** Awareness and Training | Preventive | Training reduces violations |
| **A.5.15-18** IAM | Operational | Access suspension during investigation |

### Reference to Related IMPs

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-IMP-A.6.4-5.S2 | Employment Exit Assessment | Exit process post-termination |
| ISMS-IMP-A.6.4-5.S3 | Post-Employment Obligations | Continuing obligations tracking |
| ISMS-IMP-A.6.4-5.S4 | Employment Exit Dashboard | Metrics and reporting |
| ISMS-IMP-A.5.24-28.x | Incident Management | Incident-disciplinary interface |

---

# PART II: TECHNICAL SPECIFICATION

---

## 2.1 Workbook Architecture

### File Details

| Attribute | Value |
|-----------|-------|
| **Filename** | `ISMS-IMP-A.6.4-5.S1_Disciplinary_Process_Assessment_YYYYMMDD.xlsx` |
| **Format** | Microsoft Excel Open XML (.xlsx) |
| **Sheets** | 7 |
| **Protected** | Yes (structure and formatting) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 2 |
| 2 | Violation_Categories | Violation classification | 50+ | 8 |
| 3 | Response_Matrix | Response mapping | 20 | 7 |
| 4 | Investigation_Process | Procedure documentation | 30 | 6 |
| 5 | Case_Tracker | Case tracking | 100+ | 8 |
| 6 | Evidence_Register | Evidence tracking | 50+ | 6 |
| 7 | Approval_SignOff | Authorisation | 15 | 3 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

#### Layout

| Row | Column A | Column B |
|-----|----------|----------|
| 1 | **ISMS-IMP-A.6.4-5.S1** | |
| 2 | **Disciplinary Process Assessment** | |
| 3 | | |
| 4 | **Document Information** | |
| 5 | Control Reference | ISO/IEC 27001:2022 A.6.4, A.6.5 |
| 6 | Document ID | ISMS-IMP-A.6.4-5.S1 |
| 7 | Generated Date | [Date] |
| 8 | Version | 1.0 |

#### Column Widths

| Column | Width (characters) |
|--------|-------------------|
| A | 28 |
| B | 70 |

### Sheet 2: Violation_Categories

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Category_ID | 15 | Text | VIOL-### |
| B | Category_Name | 35 | Text | Required |
| C | Severity_Level | 18 | List | Dropdown |
| D | Description | 50 | Text | Required |
| E | Examples | 45 | Text | Required |
| F | Investigation_Required | 12 | List | Yes/No |
| G | Security_Team_Involvement | 15 | List | Yes/No/Conditional |
| H | Related_Policy | 30 | Text | Policy reference |

### Sheet 3: Response_Matrix

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Severity_Level | 18 | List | From categories |
| B | First_Occurrence | 35 | Text | Response description |
| C | Second_Occurrence | 35 | Text | Response description |
| D | Third_Occurrence | 35 | Text | Response description |
| E | Immediate_Actions | 35 | Text | Immediate response |
| F | Mitigating_Factors | 40 | Text | Factors reducing response |
| G | Aggravating_Factors | 40 | Text | Factors increasing response |

### Sheet 4: Investigation_Process

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Phase | 20 | List | Investigation phases |
| B | Activities | 50 | Text | Detailed activities |
| C | Timeline | 20 | Text | Expected duration |
| D | Responsible_Party | 25 | Text | Role(s) responsible |
| E | Outputs | 35 | Text | Required outputs |
| F | Documentation_Required | 35 | Text | Required documentation |

### Sheet 5: Case_Tracker

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Case_ID | 18 | Text | DISC-YYYY-### |
| B | Date_Reported | 14 | Date | DD.MM.YYYY |
| C | Violation_Category | 20 | List | From categories |
| D | Status | 18 | List | Status options |
| E | Investigation_Lead | 25 | Text | Name |
| F | Date_Closed | 14 | Date | DD.MM.YYYY |
| G | Outcome | 40 | Text | Summary |
| H | Notes | 35 | Text | Additional info |

### Sheet 6: Evidence_Register

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Evidence_ID | 20 | Text | EVD-A.6.4.1-### |
| B | Evidence_Description | 50 | Text | Description |
| C | Evidence_Type | 20 | List | Type dropdown |
| D | Storage_Location | 50 | Text | Path/URL |
| E | Collection_Date | 14 | Date | DD.MM.YYYY |
| F | Collected_By | 25 | Text | Name |

### Sheet 7: Approval_SignOff

#### Layout

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 1 | **Assessment Sign-Off** | | |
| 3 | **Assessor Details** | | |
| 4 | Assessor Name | [Input] | |
| 5 | Role | [Input] | |
| 6 | Assessment Date | [Input] | |
| 8 | **Reviewer Sign-Off** | **Signature** | **Date** |
| 9 | HR Director | | |
| 10 | Legal Counsel | | |
| 11 | CISO | | |

---

## 2.3 Data Validations

### Severity_Level Dropdown

```python
SEVERITY_LEVEL_LIST = [
    "Minor",
    "Moderate",
    "Serious",
    "Gross Misconduct"
]
```

### Investigation_Required Dropdown

```python
INVESTIGATION_REQUIRED_LIST = [
    "Yes",
    "No"
]
```

### Security_Team_Involvement Dropdown

```python
SECURITY_INVOLVEMENT_LIST = [
    "Yes",
    "No",
    "Conditional"
]
```

### Case_Status Dropdown

```python
CASE_STATUS_LIST = [
    "Reported",
    "Under Investigation",
    "Pending Decision",
    "Action Taken",
    "Closed",
    "Appealed",
    "Appeal Resolved"
]
```

### Investigation_Phase Dropdown

```python
INVESTIGATION_PHASE_LIST = [
    "Discovery",
    "Assessment",
    "Planning",
    "Evidence Collection",
    "Analysis",
    "Decision",
    "Action",
    "Follow-up",
    "Closure"
]
```

### Evidence_Type Dropdown

```python
EVIDENCE_TYPE_LIST = [
    "Policy Document",
    "Procedure",
    "Case Record",
    "Training Record",
    "Communication",
    "Form/Template",
    "Other"
]
```

---

## 2.4 Conditional Formatting

### Violation_Categories Sheet

#### Severity Level Formatting

| Value | Fill Colour | Font Colour |
|-------|-------------|-------------|
| Minor | Light Blue (#BDD7EE) | Dark Blue (#1F4E79) |
| Moderate | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Serious | Light Orange (#FCE4D6) | Dark Red (#9C0006) |
| Gross Misconduct | Light Red (#FFC7CE) | Dark Red (#9C0006) |

### Case_Tracker Sheet

#### Status Formatting

| Value | Fill Colour | Font Colour |
|-------|-------------|-------------|
| Reported | Light Blue (#BDD7EE) | Dark Blue (#1F4E79) |
| Under Investigation | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Pending Decision | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Action Taken | Light Green (#C6EFCE) | Dark Green (#006100) |
| Closed | Light Grey (#D9D9D9) | Dark Grey (#595959) |
| Appealed | Light Orange (#FCE4D6) | Dark Red (#9C0006) |
| Appeal Resolved | Light Green (#C6EFCE) | Dark Green (#006100) |

---

## 2.5 Formula Specifications

### Case_Tracker Calculated Fields

#### Days Open

```excel
=IF(F2="", TODAY()-B2, F2-B2)
```
*Calculates days between report date and closure (or today if open)*

#### Overdue Flag

```excel
=IF(AND(D2<>"Closed", TODAY()-B2>30), "OVERDUE", "")
```
*Flags cases open more than 30 days*

### Approval_SignOff Summary Formulas

#### Total Categories Defined

```excel
=COUNTA(Violation_Categories!A4:A53)-COUNTBLANK(Violation_Categories!B4:B53)
```

#### Active Cases Count

```excel
=COUNTIF(Case_Tracker!D4:D103,"<>Closed")-COUNTIF(Case_Tracker!D4:D103,"")
```

---

## 2.6 Cell Styling Standards

### Colour Palette

| Purpose | Colour Name | Hex Code |
|---------|-------------|----------|
| Header Background | Navy Blue | #003366 |
| Header Text | White | #FFFFFF |
| Subheader Background | Medium Blue | #4472C4 |
| Column Header | Light Grey | #D9D9D9 |
| Input Field | Light Yellow | #FFFFCC |
| Success/Complete | Light Green | #C6EFCE |
| Warning | Light Yellow | #FFEB9C |
| Alert/Error | Light Red | #FFC7CE |

### Font Standards

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Sheet Title | Calibri | 14 | Bold |
| Section Header | Calibri | 12 | Bold |
| Column Header | Calibri | 10 | Bold |
| Data Cell | Calibri | 10 | Normal |

### Border Standards

| Element | Style |
|---------|-------|
| Header Row | Thin all sides |
| Data Rows | Thin all sides |
| Section Divider | Medium bottom |

---

## 2.7 Generator Script Reference

### Script Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a645_1_disciplinary_process.py` |
| **Location** | `10-isms-scr-base/isms-a.6.4-5-employment-exit/10_generator-master/` |
| **Language** | Python 3.8+ |
| **Dependencies** | openpyxl, logging, datetime |

### Key Functions

| Function | Purpose |
|----------|---------|
| `create_instructions_sheet()` | Generates Instructions sheet |
| `create_violation_categories_sheet()` | Generates Violation_Categories sheet |
| `create_response_matrix_sheet()` | Generates Response_Matrix sheet |
| `create_investigation_process_sheet()` | Generates Investigation_Process sheet |
| `create_case_tracker_sheet()` | Generates Case_Tracker sheet |
| `create_evidence_register_sheet()` | Generates Evidence_Register sheet |
| `create_approval_signoff_sheet()` | Generates Approval_SignOff sheet |

### Output Location

```
10-isms-scr-base/
└── isms-a.6.4-5-employment-exit/
    └── 90_workbooks/
        └── ISMS-IMP-A.6.4-5.S1_Disciplinary_Process_Assessment_YYYYMMDD.xlsx
```

### Execution

```bash
cd 10-isms-scr-base/isms-a.6.4-5-employment-exit/10_generator-master
python3 generate_a645_1_disciplinary_process.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"The art of leadership is saying no, not yes. It is very easy to say yes."*
— Tony Blair

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-02-03 -->
