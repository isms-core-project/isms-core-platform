# ISMS-IMP-A.5.10-11.S1 - Acceptable Use Policy Assessment

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.S1 |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.10: Acceptable Use of Information and Other Associated Assets |
| **Parent Policy** | ISMS-POL-A.5.10-11 Asset Usage Lifecycle Policy |
| **Related IMPs** | ISMS-IMP-A.5.10-11.S2, ISMS-IMP-A.5.10-11.S3, ISMS-IMP-A.5.10-11.S4 |
| **Version** | 1.0 |
| **Classification** | Internal Use |
| **Owner** | Information Security Manager |
| **Last Review** | [Date to be set] |
| **Framework Version** | 1.0 |
| **Assessment Type** | Policy Completeness and Effectiveness Assessment |

---

## Control Requirement

> "Rules for the acceptable use of information and other associated assets should be identified, documented and implemented."
>
> — ISO/IEC 27001:2022, Annex A Control 5.10

---

## Table of Contents

### PART I: USER COMPLETION GUIDE
1. [Assessment Overview](#1-assessment-overview)
2. [Control Requirements](#2-control-requirements)
3. [Prerequisites](#3-prerequisites)
4. [Policy Content Framework](#4-policy-content-framework)
5. [Asset Category Coverage](#5-asset-category-coverage)
6. [Workbook Structure](#6-workbook-structure)
7. [Completion Walkthrough](#7-completion-walkthrough)
8. [User Awareness and Acknowledgement](#8-user-awareness-and-acknowledgement)
9. [Communication Effectiveness](#9-communication-effectiveness)
10. [Evidence Collection](#10-evidence-collection)
11. [Common Pitfalls](#11-common-pitfalls)
12. [Quality Checklist](#12-quality-checklist)
13. [Review and Approval](#13-review-and-approval)
14. [Related Controls](#14-related-controls)

### PART II: TECHNICAL SPECIFICATION
15. [Workbook Architecture](#15-workbook-architecture)
16. [Sheet Specifications](#16-sheet-specifications)
17. [Data Validation Rules](#17-data-validation-rules)
18. [Conditional Formatting](#18-conditional-formatting)
19. [Formula Specifications](#19-formula-specifications)
20. [Cell Styling Standards](#20-cell-styling-standards)
21. [Generator Script Reference](#21-generator-script-reference)

---

# PART I: USER COMPLETION GUIDE

## 1. Assessment Overview

### 1.1 Purpose

The Acceptable Use Policy (AUP) Assessment workbook evaluates the completeness and effectiveness of your organisation's Acceptable Use Policy framework. It verifies that rules for acceptable use of information and other associated assets are:

- **Identified**: All asset categories have defined usage rules
- **Documented**: Rules are formally documented in an approved policy
- **Implemented**: Users are aware of and acknowledge the rules
- **Enforced**: Monitoring and consequences are in place

This assessment supports ISO 27001:2022 Control A.5.10 by providing a systematic evaluation of the AUP and its implementation.

### 1.2 Scope

This assessment covers:
- **Policy Content Completeness**: All required topics addressed in the AUP
- **Asset Category Coverage**: Rules defined for each asset type
- **User Awareness**: Acknowledgement tracking and compliance
- **Communication Effectiveness**: How well the policy is disseminated
- **Gap Identification**: Deficiencies requiring remediation

### 1.3 Benefits

| Stakeholder | Benefit |
|-------------|---------|
| **ISM** | Systematic verification of AUP completeness |
| **CISO** | Assurance that acceptable use is properly governed |
| **Legal/Compliance** | Evidence of policy implementation for regulatory compliance |
| **HR** | Clear framework for handling policy violations |
| **Auditors** | Documented assessment of control effectiveness |
| **Users** | Clear understanding of acceptable behaviour |

### 1.4 Assessment Frequency

| Activity | Frequency |
|----------|-----------|
| Full AUP completeness assessment | Annual |
| User acknowledgement monitoring | Monthly |
| New hire acknowledgement tracking | Per onboarding |
| Policy content review | Annual or after significant changes |
| Communication effectiveness review | Annual |

---

## 2. Control Requirements

### 2.1 ISO 27001:2022 A.5.10 Requirements

Control A.5.10 requires that acceptable use rules be identified, documented, and implemented. ISO 27002:2022 provides detailed implementation guidance:

| Requirement Element | Assessment Focus |
|---------------------|------------------|
| **Identification** | All asset categories have defined usage rules |
| **Documentation** | Rules are in a formal, approved policy |
| **Implementation** | Users are trained and acknowledge the rules |
| **Communication** | Policy is accessible and regularly reinforced |
| **Enforcement** | Monitoring and consequences are defined |

### 2.2 Policy Content Requirements

ISO 27002:2022 guidance specifies that the AUP should address:

| Topic Category | Required Content |
|----------------|------------------|
| **Scope** | Assets, users, and locations covered |
| **Acceptable Use** | Permitted business and personal use |
| **Prohibited Activities** | Explicitly forbidden actions |
| **Monitoring** | Disclosure of monitoring activities |
| **Consequences** | Disciplinary actions for violations |
| **Exceptions** | Process for requesting exceptions |
| **Responsibilities** | User obligations and accountabilities |
| **Asset Handling** | Requirements by classification level |

### 2.3 Compliance Indicators

| Indicator | Target | Measurement |
|-----------|:------:|-------------|
| Policy completeness | 100% | All required topics addressed |
| Asset category coverage | 100% | All categories have rules |
| User acknowledgement | 100% | All users have signed |
| Acknowledgement currency | 100% | Within 12 months |
| Communication channels | ≥3 | Multiple dissemination methods |

---

## 3. Prerequisites

### 3.1 Required Inputs

Before starting the assessment, gather:

| Prerequisite | Source | Purpose |
|--------------|--------|---------|
| **Current AUP Document** | Policy repository | Assess content completeness |
| **Asset Inventory** | ISMS-IMP-A.5.9 | Verify asset category coverage |
| **User Directory** | HR/Active Directory | Calculate acknowledgement rate |
| **Acknowledgement Records** | LMS or HR system | Verify user sign-offs |
| **Communication Records** | Email archives, intranet logs | Assess dissemination |
| **Previous Assessment** | ISMS Evidence Library | Compare improvements |

### 3.2 Access Requirements

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| **Policy Repository** | Read | Access current AUP |
| **LMS/Training System** | Read | Export acknowledgement data |
| **HR System** | Read | User counts and department data |
| **Email System** | Read | Communication distribution records |
| **ISMS Evidence Library** | Write | Store assessment evidence |

### 3.3 Stakeholder Contacts

Identify and confirm availability of:

| Role | Responsibility | Contact Required |
|------|----------------|------------------|
| **Policy Owner** | Confirm policy currency | Before assessment |
| **HR Manager** | Provide user counts | Before assessment |
| **LMS Administrator** | Export acknowledgement data | Before assessment |
| **Legal Counsel** | Confirm legal adequacy | For gaps identified |
| **IT Security** | Confirm monitoring implementation | For enforcement review |

---

## 4. Policy Content Framework

### 4.1 Required Policy Sections

The AUP should contain the following sections to be considered complete:

| Section | Required Content | Assessment Criteria |
|---------|------------------|---------------------|
| **1. Purpose and Scope** | Why the policy exists; who and what it covers | Clearly defines applicability |
| **2. Definitions** | Key terms used in the policy | Terms are unambiguous |
| **3. Policy Ownership** | Owner, approval, effective date | Governance clear |
| **4. Acceptable Business Use** | What users may do for work | Positive permissions stated |
| **5. Personal Use** | Rules for personal use of assets | Clear boundaries set |
| **6. Prohibited Activities** | Explicitly forbidden actions | Comprehensive list |
| **7. Monitoring and Privacy** | Disclosure of monitoring | Legal compliance |
| **8. Data Classification** | Handling by classification | Aligned with data classification policy |
| **9. Mobile and Remote Use** | BYOD, remote working rules | Modern work patterns addressed |
| **10. Cloud and Social Media** | Third-party service use | Current technologies covered |
| **11. Incident Reporting** | Obligation to report violations | Clear process |
| **12. Consequences** | Disciplinary framework | Proportionate sanctions |
| **13. Exceptions** | How to request exceptions | Process documented |
| **14. Acknowledgement** | User sign-off requirement | Enforcement mechanism |

### 4.2 Policy Quality Criteria

| Criterion | Definition | Assessment Method |
|-----------|------------|-------------------|
| **Clarity** | Language is unambiguous | Review for vague terms |
| **Completeness** | All required topics covered | Checklist comparison |
| **Currency** | Reflects current technology and practices | Date review, technology check |
| **Accessibility** | Easy to find and read | Location check, readability |
| **Actionability** | Users know what to do | Clear instructions present |
| **Enforceability** | Can be monitored and enforced | Enforcement mechanisms defined |

### 4.3 Common AUP Content Gaps

| Gap Type | Example | Remediation |
|----------|---------|-------------|
| **Scope Gap** | Contractors not explicitly included | Expand scope statement |
| **Technology Gap** | No cloud service rules | Add cloud usage section |
| **Monitoring Gap** | No monitoring disclosure | Add monitoring statement |
| **Consequence Gap** | Vague "disciplinary action" | Define specific consequences |
| **Exception Gap** | No exception process | Add exception request procedure |
| **Currency Gap** | Reference to obsolete systems | Update technology references |

---

## 5. Asset Category Coverage

### 5.1 Standard Asset Categories

Ensure the AUP addresses usage rules for each category:

| Category | Description | Example Assets | Key Rules Needed |
|----------|-------------|----------------|------------------|
| **Information Assets** | Data in all forms | Documents, databases, reports | Classification handling, sharing |
| **Software Assets** | Licensed and approved software | Applications, SaaS, tools | Installation, licensing, updates |
| **Hardware Assets** | Computing and peripheral devices | Laptops, mobiles, USB drives | Care, storage, loss reporting |
| **Network Assets** | Network infrastructure and access | WiFi, VPN, internet | Usage limits, security |
| **Cloud Services** | Third-party cloud platforms | M365, AWS, SaaS apps | Data storage, sharing, configuration |
| **Communication Tools** | Messaging and collaboration | Email, Teams, Slack | Appropriate use, retention |
| **Physical Media** | Removable storage | USB, CDs, external drives | Encryption, prohibited use |
| **Authentication Assets** | Credentials and tokens | Passwords, MFA, smart cards | Protection, sharing prohibition |
| **Development Assets** | Development tools and environments | IDEs, repositories, test data | Code handling, data protection |
| **Personal Devices** | BYOD equipment | Personal phones, laptops | Separation, security requirements |
| **IoT Devices** | Connected devices | Cameras, sensors, smart devices | Secure configuration, monitoring |
| **Intellectual Property** | Created or licensed IP | Code, designs, documentation | Protection, attribution |

### 5.2 Asset Coverage Matrix

For each asset category, verify:

| Verification Point | Question to Answer |
|--------------------|-------------------|
| **Mentioned** | Is the category explicitly addressed in the AUP? |
| **Usage Rules** | Are permitted uses defined? |
| **Prohibitions** | Are forbidden uses stated? |
| **Handling** | Are handling requirements documented? |
| **Monitoring** | Is monitoring disclosure included? |
| **Consequences** | Are violation consequences applicable? |

---

## 6. Workbook Structure

### 6.1 Sheet Overview

| Sheet # | Sheet Name | Purpose | Primary Users |
|:-------:|------------|---------|---------------|
| 1 | Instructions | Guidance and metadata | All assessors |
| 2 | Policy_Assessment | AUP content completeness | ISM, Assessors |
| 3 | Asset_Coverage | Coverage by asset category | ISM, Assessors |
| 4 | Awareness_Tracking | User acknowledgement status | ISM, HR |
| 5 | Communication_Matrix | Dissemination assessment | ISM, Comms |
| 6 | Evidence_Register | Audit evidence linking | ISM, Auditors |
| 7 | Approval_SignOff | Assessment approval | ISM, CISO |

### 6.2 Data Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    ASSESSMENT DATA FLOW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  INPUTS                                                         │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐    │
│  │ AUP Document   │  │ Asset Inventory│  │ User Directory │    │
│  └───────┬────────┘  └───────┬────────┘  └───────┬────────┘    │
│          │                   │                   │              │
│          ▼                   ▼                   ▼              │
│  ┌────────────────────────────────────────────────────────┐    │
│  │                    ASSESSMENT                           │    │
│  ├──────────────┬──────────────┬──────────────────────────┤    │
│  │ Policy_      │ Asset_       │ Awareness_               │    │
│  │ Assessment   │ Coverage     │ Tracking                 │    │
│  └──────────────┴──────────────┴──────────────────────────┘    │
│          │                   │                   │              │
│          ▼                   ▼                   ▼              │
│  ┌────────────────────────────────────────────────────────┐    │
│  │                    OUTPUTS                              │    │
│  │  • Compliance Score    • Gap Register                   │    │
│  │  • Evidence Package    • Remediation Plan               │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Completion Walkthrough

### Step 1: Document Information (Instructions Sheet)

**Objective:** Establish assessment context and metadata

**Actions:**
1. Enter assessment date
2. Record assessor name and role
3. Enter organisation name
4. Specify review period (e.g., "January-December 2026")
5. Note AUP version being assessed

**Fields to Complete:**

| Field | Example Entry |
|-------|---------------|
| Assessment Date | 03.02.2026 |
| Assessor Name | [Name] |
| Assessor Role | Information Security Analyst |
| Organisation | [Organisation Name] |
| Review Period | 2026 Annual Assessment |
| AUP Version Assessed | 1.3 (Effective: 01.01.2026) |

### Step 2: Policy Assessment (Policy_Assessment Sheet)

**Objective:** Evaluate AUP content completeness

**Actions:**
1. For each requirement row, review the AUP for coverage
2. Select "Addressed" status (Yes/Partial/No/N/A)
3. Document the AUP section reference where requirement is addressed
4. Rate clarity of the language used
5. Identify gaps and document remediation notes
6. Link to evidence (policy document, section number)

**Scoring Guidance:**

| Status | Criteria | Score |
|--------|----------|:-----:|
| **Yes** | Requirement fully addressed with clear, actionable language | 1.0 |
| **Partial** | Requirement mentioned but vague, incomplete, or unclear | 0.5 |
| **No** | Requirement not addressed in current policy | 0.0 |
| **N/A** | Requirement not applicable to organisation (with justification) | - |

**Verification for Each Requirement:**

1. Locate the content in the AUP document
2. Read the actual language used
3. Assess whether the language meets the requirement
4. Check for clarity and actionability
5. Document the section reference
6. Note any improvement needed

### Step 3: Asset Coverage (Asset_Coverage Sheet)

**Objective:** Verify all asset categories have defined usage rules

**Actions:**
1. For each asset category, verify mention in AUP
2. Check if usage rules are defined
3. Check if handling requirements are documented
4. Note any gaps requiring remediation
5. Mark whether remediation is required

**Coverage Verification:**

| Column | Action |
|--------|--------|
| Covered_In_AUP | Is the category explicitly mentioned? |
| Policy_Section | Where in the AUP is it addressed? |
| Usage_Rules_Defined | Are permitted/prohibited uses clear? |
| Handling_Rules_Defined | Are storage/transmission/disposal rules defined? |
| Gap_Notes | What is missing or inadequate? |
| Remediation_Required | Does this need fixing? |

### Step 4: Awareness Tracking (Awareness_Tracking Sheet)

**Objective:** Track user acknowledgement of the AUP

**Actions:**
1. For each department, enter total user count
2. Enter count of users who have acknowledged
3. Formula calculates pending and percentage
4. Document the acknowledgement campaign method
5. Record last campaign date
6. Track escalation status for non-compliance

**Data Sources:**
- Total users: HR system or Active Directory
- Acknowledgements: LMS, HR system, or signed forms
- Campaign records: Email archives, intranet logs

**Target:** 100% acknowledgement within 30 days of hire or policy update

**Escalation Levels:**

| Status | Timeframe | Action |
|--------|-----------|--------|
| Reminder Sent | 7 days overdue | Automated reminder |
| Manager Notified | 14 days overdue | Manager alerted |
| HR Escalation | 30 days overdue | HR intervention |
| Access Restriction | 45 days overdue | System access at risk |

### Step 5: Communication Matrix (Communication_Matrix Sheet)

**Objective:** Assess policy dissemination effectiveness

**Actions:**
1. For each communication channel, record last use date
2. Schedule next communication
3. Rate effectiveness based on feedback/metrics
4. Assign owner for each channel
5. Document improvement actions

**Communication Channels to Assess:**

| Channel | Purpose | Typical Frequency |
|---------|---------|-------------------|
| Onboarding | New hire introduction | Per hire |
| Intranet | Always-available reference | Permanent |
| Annual Training | Refresher and updates | Annual |
| Email Announcement | Policy changes | As needed |
| Team Meetings | Department reinforcement | Quarterly |
| Newsletter | Awareness articles | Monthly |
| Posters/Signage | Visual reminders | Quarterly rotation |

**Effectiveness Criteria:**

| Rating | Criteria |
|--------|----------|
| **Highly Effective** | High engagement, positive feedback, measurable impact |
| **Effective** | Good reach, adequate engagement |
| **Needs Improvement** | Low engagement, inconsistent delivery |
| **Ineffective** | Poor reach, no engagement, delivery issues |

### Step 6: Evidence Register (Evidence_Register Sheet)

**Objective:** Link supporting evidence for audit purposes

**Actions:**
1. For each evidence type, create a record
2. Describe the evidence
3. Link to requirement/assertion it supports
4. Record collection date
5. Specify storage location (with path or URL)
6. Note expiration date for time-sensitive evidence

**Required Evidence:**

| Evidence Type | Description | Example |
|---------------|-------------|---------|
| Policy Document | Current approved AUP | ISMS-POL-A.5.10-11_v1.3.pdf |
| Approval Record | Policy approval evidence | Approval email, meeting minutes |
| Acknowledgement Export | LMS/HR system export | AUP_Acknowledgements_20260203.xlsx |
| Communication Records | Distribution evidence | Email distribution report |
| Training Records | Completion certificates | LMS training report |
| Exception Register | Approved exceptions | AUP_Exceptions_Register.xlsx |

### Step 7: Approval Sign-Off (Approval_SignOff Sheet)

**Objective:** Obtain formal assessment approval

**Actions:**
1. Review auto-calculated summary metrics
2. Complete assessor information and signature
3. Submit for ISM review
4. Obtain CISO approval
5. Archive completed assessment

**Summary Metrics Displayed:**

| Metric | Formula Source |
|--------|----------------|
| Total Requirements Assessed | Count from Policy_Assessment |
| Requirements Addressed | Count where Addressed = "Yes" |
| Partial Coverage | Count where Addressed = "Partial" |
| Gaps Identified | Count where Addressed = "No" |
| Compliance Score | (Yes + 0.5×Partial) / Total × 100% |
| Asset Categories Covered | From Asset_Coverage sheet |
| Overall Acknowledgement % | From Awareness_Tracking sheet |

---

## 8. User Awareness and Acknowledgement

### 8.1 Acknowledgement Requirements

| User Type | Timing | Method | Renewal |
|-----------|--------|--------|---------|
| **New Hires** | Within 5 days of start | Onboarding LMS module | N/A |
| **Existing Employees** | Annual renewal | LMS or email acknowledgement | 12 months |
| **Contractors** | Before access granted | Contract terms + LMS | Per contract |
| **Temporary Staff** | Before access granted | Abbreviated acknowledgement | Per engagement |
| **Third-Party Users** | Before access granted | Contractual terms | Per agreement |

### 8.2 Acknowledgement Content

The acknowledgement should confirm the user:

1. Has read and understood the Acceptable Use Policy
2. Agrees to comply with its requirements
3. Understands the consequences of non-compliance
4. Acknowledges that usage may be monitored
5. Will report any policy violations observed

### 8.3 Tracking and Escalation

```
┌─────────────────────────────────────────────────────────────────┐
│                ACKNOWLEDGEMENT ESCALATION FLOW                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Day 0: User prompted to acknowledge                            │
│     │                                                           │
│     ▼                                                           │
│  Day 7: Automated reminder (if not completed)                   │
│     │                                                           │
│     ▼                                                           │
│  Day 14: Manager notification                                   │
│     │                                                           │
│     ▼                                                           │
│  Day 30: HR escalation                                          │
│     │                                                           │
│     ▼                                                           │
│  Day 45: Access restriction consideration                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 9. Communication Effectiveness

### 9.1 Multi-Channel Strategy

Effective AUP communication uses multiple channels:

| Channel | Strength | Limitation | Best Used For |
|---------|----------|------------|---------------|
| **Onboarding** | Structured, mandatory | One-time only | Initial education |
| **LMS Training** | Trackable, testable | Perceived as checkbox | Annual renewal |
| **Email** | Wide reach | Often ignored | Announcements |
| **Intranet** | Always available | Requires active search | Reference |
| **Team Meetings** | Interactive | Time-consuming | Clarifications |
| **Posters** | Constant visibility | Limited content | Reminders |
| **Security Newsletters** | Regular touchpoint | Low engagement | Ongoing awareness |

### 9.2 Measuring Effectiveness

| Metric | Measurement Method | Target |
|--------|-------------------|--------|
| **Reach** | Unique views/recipients | 100% of users |
| **Engagement** | Time on page, quiz scores | >70% engagement |
| **Retention** | Post-training assessments | >80% pass rate |
| **Compliance** | Violation incident rate | <2% annual |
| **Feedback** | Survey responses | >50% response rate |

---

## 10. Evidence Collection

### 10.1 Evidence Requirements

| Evidence Type | Description | Retention |
|---------------|-------------|-----------|
| **Policy Document** | Current approved version of AUP | Permanent (versions) |
| **Approval Record** | Evidence of policy approval | 3 years |
| **Acknowledgement Records** | User sign-off exports | 3 years |
| **Training Records** | LMS completion data | 3 years |
| **Communication Records** | Distribution logs, analytics | 3 years |
| **Exception Records** | Approved policy exceptions | 3 years |
| **Assessment Workbook** | This completed assessment | 3 years |

### 10.2 Evidence Storage

| Evidence Type | Storage Location | Naming Convention |
|---------------|------------------|-------------------|
| Policy documents | ISMS Evidence Library/A.5.10-11/Policies/ | ISMS-POL-A.5.10-11_v[X.Y].pdf |
| Acknowledgements | ISMS Evidence Library/A.5.10-11/Acknowledgements/ | AUP_Ack_[Department]_YYYYMMDD.xlsx |
| Training records | ISMS Evidence Library/A.5.10-11/Training/ | AUP_Training_YYYYMMDD.pdf |
| Communication | ISMS Evidence Library/A.5.10-11/Communication/ | AUP_Comm_[Type]_YYYYMMDD.pdf |
| Assessments | ISMS Evidence Library/A.5.10-11/Assessments/ | A.5.10-11.1_Assessment_YYYYMMDD.xlsx |

### 10.3 Evidence Quality Standards

| Standard | Requirement |
|----------|-------------|
| **Authenticity** | Clear source identification |
| **Completeness** | All relevant data included |
| **Currency** | Dated within assessment period |
| **Accessibility** | Retrievable within 24 hours |
| **Integrity** | Protected from modification |

---

## 11. Common Pitfalls

### Policy Content Pitfalls

❌ **MISTAKE:** Assessing against an outdated version of the AUP
✅ **CORRECT:** Always verify you have the current approved version before starting assessment

❌ **MISTAKE:** Accepting "implied" coverage without explicit policy language
✅ **CORRECT:** Requirements should be explicitly stated; don't assume implicit coverage

❌ **MISTAKE:** Marking coverage as "Yes" when content is vague or incomplete
✅ **CORRECT:** Use "Partial" for incomplete coverage; reserve "Yes" for fully addressed requirements

❌ **MISTAKE:** Not verifying policy alignment with current technology and practices
✅ **CORRECT:** Check that the AUP addresses current systems (cloud, mobile, remote work)

❌ **MISTAKE:** Skipping legal review for monitoring and consequence statements
✅ **CORRECT:** Ensure legal counsel has validated employment law compliance

### Acknowledgement Tracking Pitfalls

❌ **MISTAKE:** Counting unsigned or undated acknowledgements as complete
✅ **CORRECT:** Only count fully signed, dated acknowledgements with verification

❌ **MISTAKE:** Not verifying acknowledgement dates are within the required timeframe
✅ **CORRECT:** Check that acknowledgements are current (within 12 months)

❌ **MISTAKE:** Not tracking contractors and temporary staff separately
✅ **CORRECT:** Track all user types with appropriate acknowledgement requirements

❌ **MISTAKE:** No escalation process for non-compliant users
✅ **CORRECT:** Document and execute escalation for acknowledgement non-compliance

❌ **MISTAKE:** Relying on single acknowledgement method without verification
✅ **CORRECT:** Verify LMS data matches HR records; investigate discrepancies

### Asset Coverage Pitfalls

❌ **MISTAKE:** Skipping asset categories as "not applicable" without justification
✅ **CORRECT:** Document clear rationale for any N/A designations

❌ **MISTAKE:** Assuming general policy statements cover specific asset types
✅ **CORRECT:** Each significant asset category should have explicit rules

❌ **MISTAKE:** Not updating coverage when new asset types are introduced
✅ **CORRECT:** Trigger AUP review when new technologies are adopted

❌ **MISTAKE:** Inconsistent handling requirements across similar asset categories
✅ **CORRECT:** Ensure logical consistency in rules for related asset types

### Evidence and Documentation Pitfalls

❌ **MISTAKE:** Not documenting evidence locations for "Yes" ratings
✅ **CORRECT:** Every compliance claim should link to retrievable evidence

❌ **MISTAKE:** Accepting verbal confirmations without documentation
✅ **CORRECT:** All compliance evidence must be documented and stored

❌ **MISTAKE:** Not preserving point-in-time snapshots of acknowledgement data
✅ **CORRECT:** Export and archive acknowledgement data at assessment time

❌ **MISTAKE:** Failing to update evidence register when documents are moved
✅ **CORRECT:** Maintain accurate evidence locations; verify accessibility

---

## 12. Quality Checklist

### Pre-Submission Checklist

#### Document Completeness
- [ ] All Instructions sheet metadata fields completed
- [ ] Assessment date and period clearly documented
- [ ] AUP version being assessed is identified
- [ ] Assessor information complete

#### Policy Assessment
- [ ] Every policy requirement has a status assigned
- [ ] Policy section references provided for all "Yes" ratings
- [ ] Clarity ratings completed for addressed requirements
- [ ] Gap notes documented for all "Partial" or "No" ratings
- [ ] N/A designations have documented justification

#### Asset Coverage
- [ ] All standard asset categories evaluated
- [ ] Coverage status assigned for each category
- [ ] Policy section references provided
- [ ] Usage and handling rules verified
- [ ] Remediation requirements identified

#### Awareness Tracking
- [ ] User counts are current (within 30 days)
- [ ] Acknowledgement data exported from authoritative source
- [ ] Calculations verified for accuracy
- [ ] Escalation status documented for non-compliant users
- [ ] Campaign dates and methods recorded

#### Communication Assessment
- [ ] All communication channels evaluated
- [ ] Effectiveness ratings assigned
- [ ] Next scheduled communications planned
- [ ] Improvement actions documented

#### Evidence and Approval
- [ ] Evidence register complete with valid locations
- [ ] Evidence accessible and retrievable
- [ ] Summary metrics reviewed for accuracy
- [ ] Assessor signature obtained
- [ ] ISM review signature obtained
- [ ] CISO approval obtained

---

## 13. Review and Approval

### 13.1 Assessment Review Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                  ASSESSMENT APPROVAL WORKFLOW                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────────┐   │
│  │ Assessor     │      │ ISM Review   │      │ CISO         │   │
│  │ Completes    │─────▶│ Validates    │─────▶│ Approves     │   │
│  │ Assessment   │      │ Accuracy     │      │ Final        │   │
│  └──────────────┘      └──────────────┘      └──────────────┘   │
│        │                      │                      │          │
│        ▼                      ▼                      ▼          │
│  All sheets             Findings             Remediation        │
│  completed              reviewed             prioritised        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 13.2 Approval Authorities

| Assessment Component | Reviewer | Approver |
|---------------------|----------|----------|
| Policy Assessment | ISM | CISO |
| Asset Coverage | Asset Owners (consulted) | ISM |
| Awareness Tracking | HR Manager (validated) | ISM |
| Communication Matrix | Communications (consulted) | ISM |
| Overall Assessment | ISM | CISO |

### 13.3 Sign-off Record

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Assessor | | | |
| ISM Review | | | |
| CISO Approval | | | |

---

## 14. Related Controls

### 14.1 Primary Dependencies

| Control | Relationship | Integration |
|---------|--------------|-------------|
| **A.5.9** | Asset Inventory | Provides asset categories to cover |
| **A.5.10-11.2** | Usage Rules Inventory | Detailed rules supporting AUP |
| **A.5.10-11.3** | Asset Return | Offboarding extends AUP lifecycle |
| **A.5.10-11.4** | Compliance Dashboard | Aggregates assessment metrics |
| **A.6.3** | Awareness and Training | Training delivery mechanism |

### 14.2 Related Controls

| Control | Relevance |
|---------|-----------|
| **A.5.1** | Information Security Policy | Parent policy framework |
| **A.5.12** | Classification of Information | Data handling in AUP |
| **A.7.2** | Terms and Conditions | Employment terms reference AUP |
| **A.8.3** | Information Access Restriction | Access tied to AUP compliance |

---

# PART II: TECHNICAL SPECIFICATION

## 15. Workbook Architecture

### 15.1 Generator Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a510_11_1_acceptable_use_policy.py` |
| **Script Location** | `10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/10_generator-master/` |
| **Output Location** | `10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/90_workbooks/` |
| **Output Filename** | `ISMS-IMP-A.5.10-11.S1_Acceptable_Use_Policy_Assessment_YYYYMMDD.xlsx` |

### 15.2 Technical Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    WORKBOOK ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    HEADER STRUCTURE                       │   │
│  │  Row 1: Title Bar (merged A1:K1)                         │   │
│  │  Row 2: Control Reference                                 │   │
│  │  Row 3: Assessment Period                                 │   │
│  │  Row 4: Generated Date                                    │   │
│  │  Row 5: Empty (separator)                                 │   │
│  │  Row 6: Column Headers                                    │   │
│  │  Row 7+: Data Rows                                        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │Instruc-  │ │Policy_   │ │Asset_    │ │Awareness_│          │
│  │tions     │ │Assessment│ │Coverage  │ │Tracking  │          │
│  │ Sheet 1  │ │ Sheet 2  │ │ Sheet 3  │ │ Sheet 4  │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                        │
│  │Communic- │ │Evidence_ │ │Approval_ │                        │
│  │ation     │ │Register  │ │SignOff   │                        │
│  │ Sheet 5  │ │ Sheet 6  │ │ Sheet 7  │                        │
│  └──────────┘ └──────────┘ └──────────┘                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 16. Sheet Specifications

### Sheet 1: Instructions

**Purpose:** Assessment guidance and metadata

**Structure:**
- Merged header row with document title
- Metadata table (assessment date, assessor, organisation)
- Quick reference guide for completion
- Colour legend for status indicators

### Sheet 2: Policy_Assessment

**Purpose:** Evaluate AUP content completeness

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Requirement_ID | 15 | Text | Auto-generated (REQ-001) |
| B | Policy_Requirement | 45 | Text | Pre-populated requirement |
| C | Category | 20 | Text | Requirement category |
| D | Addressed | 14 | List | Yes/Partial/No/N/A |
| E | Policy_Section | 20 | Text | AUP section reference |
| F | Clarity_Rating | 16 | List | Clear/Needs Improvement/Unclear |
| G | Last_Updated | 16 | Date | When requirement was last reviewed |
| H | Owner | 22 | Text | Requirement owner |
| I | Gap_Status | 16 | List | Compliant/Gap Identified/Remediation In Progress |
| J | Remediation_Notes | 35 | Text | Required improvements |
| K | Evidence_Ref | 18 | Text | Evidence reference |

**Pre-populated Requirements (20 items):**
1. Policy scope defines applicable assets
2. Policy defines acceptable business use
3. Policy explicitly prohibits unauthorized activities
4. Personal use guidelines are documented
5. Monitoring and logging disclosure included
6. Consequences of violation are stated
7. Exception request process documented
8. Intellectual property rules defined
9. Data classification handling requirements
10. Mobile device acceptable use rules
11. Remote working asset use guidelines
12. Cloud service usage rules
13. Social media usage guidelines
14. Email and messaging acceptable use
15. Internet usage guidelines
16. Password and authentication requirements
17. Physical asset protection responsibilities
18. Incident reporting obligations
19. Third-party access provisions
20. Policy acknowledgement requirement

### Sheet 3: Asset_Coverage

**Purpose:** Verify all asset categories have defined usage rules

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Asset_Category | 25 | Text | Pre-populated categories |
| B | Asset_Examples | 40 | Text | Example assets in category |
| C | Covered_In_AUP | 16 | List | Yes/Partial/No |
| D | Policy_Section | 20 | Text | AUP section reference |
| E | Usage_Rules_Defined | 18 | List | Yes/No/N/A |
| F | Handling_Rules_Defined | 18 | List | Yes/No/N/A |
| G | Gap_Notes | 35 | Text | Coverage gaps identified |
| H | Remediation_Required | 18 | List | Yes/No |
| I | Evidence_Ref | 18 | Text | Evidence reference |

**Pre-populated Categories (12 items):**
- Information Assets, Software Assets, Hardware Assets
- Network Assets, Cloud Services, Communication Tools
- Physical Media, Authentication Assets, Development Environments
- Monitoring Systems, Personal Devices (BYOD), IoT Devices

### Sheet 4: Awareness_Tracking

**Purpose:** Track user AUP acknowledgement status

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Department | 22 | Text | Department name |
| B | Total_Users | 14 | Number | Total users in department |
| C | Acknowledged | 14 | Number | Users who acknowledged |
| D | Pending | 14 | Number | Formula: =B-C |
| E | Acknowledgment_% | 16 | Percent | Formula: =C/B*100 |
| F | Last_Campaign_Date | 18 | Date | Last acknowledgement campaign |
| G | Next_Due_Date | 16 | Date | Next renewal due |
| H | Campaign_Method | 22 | List | Email/LMS/Intranet/In-Person/Onboarding |
| I | Escalation_Status | 18 | List | None Required/Reminder Sent/Manager Notified/HR Escalation |
| J | Notes | 35 | Text | Additional notes |

**Summary Row:** TOTAL row with SUM formulas for columns B, C, D and AVERAGE for column E

### Sheet 5: Communication_Matrix

**Purpose:** Assess policy communication effectiveness

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Communication_Channel | 28 | Text | Pre-populated channels |
| B | Audience | 25 | Text | Target audience |
| C | Frequency | 18 | List | Daily/Weekly/Monthly/Quarterly/Annual/Per hire/As needed |
| D | Last_Communication | 18 | Date | Last use date |
| E | Next_Scheduled | 18 | Date | Next planned use |
| F | Effectiveness_Rating | 18 | List | Highly Effective/Effective/Needs Improvement/Ineffective |
| G | Owner | 22 | Text | Channel owner |
| H | Improvement_Actions | 35 | Text | Actions to improve effectiveness |
| I | Evidence_Ref | 18 | Text | Evidence reference |

**Pre-populated Channels:**
- Onboarding Process, Intranet/SharePoint, Annual Training
- Email Announcements, Team Meetings, Security Newsletter
- Posters/Digital Signage

### Sheet 6: Evidence_Register

**Purpose:** Link supporting audit evidence

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Evidence_ID | 15 | Text | Auto-generated (EV-001) |
| B | Evidence_Type | 22 | List | Policy Document/Acknowledgment Record/Training Record/etc. |
| C | Description | 45 | Text | Evidence description |
| D | Related_Requirement | 25 | Text | Requirement(s) supported |
| E | Collection_Date | 16 | Date | When collected |
| F | Location | 40 | Text | Storage location (URL or path) |
| G | Collected_By | 25 | Text | Person who collected |
| H | Valid_Until | 16 | Date | Expiration date |

### Sheet 7: Approval_SignOff

**Purpose:** Assessment approval and sign-off

**Structure:**
- Summary metrics section (auto-calculated)
- Assessor completion section
- ISM review section
- CISO approval section

**Summary Formulas:**
- Total Requirements Assessed: `=COUNTA(Policy_Assessment!A7:A26)`
- Requirements Addressed: `=COUNTIF(Policy_Assessment!D7:D26,"Yes")`
- Partial Coverage: `=COUNTIF(Policy_Assessment!D7:D26,"Partial")`
- Gaps Identified: `=COUNTIF(Policy_Assessment!D7:D26,"No")`
- Compliance Score: `=(COUNTIF(D7:D26,"Yes")+0.5*COUNTIF(D7:D26,"Partial"))/COUNTA(A7:A26)*100`
- Overall Acknowledgement: Reference to Awareness_Tracking total

---

## 17. Data Validation Rules

### 17.1 Dropdown Lists

| Field | Valid Values |
|-------|--------------|
| **Addressed** | Yes, Partial, No, N/A |
| **Clarity_Rating** | Clear, Needs Improvement, Unclear |
| **Gap_Status** | Compliant, Gap Identified, Remediation In Progress |
| **Covered_In_AUP** | Yes, Partial, No |
| **Usage/Handling Defined** | Yes, No, N/A |
| **Remediation_Required** | Yes, No |
| **Campaign_Method** | Email, LMS, Intranet, In-Person, Onboarding |
| **Escalation_Status** | None Required, Reminder Sent, Manager Notified, HR Escalation |
| **Frequency** | Daily, Weekly, Monthly, Quarterly, Annual, Per hire, As needed, Always available |
| **Effectiveness_Rating** | Highly Effective, Effective, Needs Improvement, Ineffective |
| **Evidence_Type** | Policy Document, Acknowledgment Record, Training Record, Screenshot, Export, Attestation, Email, Meeting Minutes |
| **Approval_Decision** | Approved, Approved with conditions, Rejected |

### 17.2 Numeric Constraints

| Field | Constraint |
|-------|------------|
| Total_Users | ≥0, whole number |
| Acknowledged | ≥0, ≤Total_Users |
| Dates | Valid date format (DD.MM.YYYY) |

---

## 18. Conditional Formatting

### 18.1 Policy_Assessment Sheet

| Range | Condition | Format |
|-------|-----------|--------|
| Column D (Addressed) | "Yes" | Green fill (#90EE90) |
| Column D (Addressed) | "Partial" | Yellow fill (#FFFF00) |
| Column D (Addressed) | "No" | Red fill (#FF6B6B) |
| Column D (Addressed) | "N/A" | Grey fill (#D3D3D3) |
| Column I (Gap_Status) | "Gap Identified" | Red fill (#FF6B6B) |

### 18.2 Asset_Coverage Sheet

| Range | Condition | Format |
|-------|-----------|--------|
| Column C (Covered) | "Yes" | Green fill |
| Column C (Covered) | "Partial" | Yellow fill |
| Column C (Covered) | "No" | Red fill |
| Column H (Remediation) | "Yes" | Red fill |

### 18.3 Awareness_Tracking Sheet

| Range | Condition | Format |
|-------|-----------|--------|
| Column E (%) | ≥95% | Green fill |
| Column E (%) | 80-94% | Yellow fill |
| Column E (%) | <80% | Red fill |
| Column I (Escalation) | "HR Escalation" | Red fill |

---

## 19. Formula Specifications

### 19.1 Awareness Tracking Formulas

**Pending Users (Column D):**
```excel
=B7-C7
```

**Acknowledgement Percentage (Column E):**
```excel
=IF(B7>0,C7/B7*100,0)
```

**Total Row:**
```excel
=SUM(B7:B20)  // Total Users
=SUM(C7:C20)  // Acknowledged
=SUM(D7:D20)  // Pending
=AVERAGE(E7:E20)  // Average %
```

### 19.2 Summary Metrics (Approval Sheet)

**Compliance Score:**
```excel
=(COUNTIF(Policy_Assessment!D7:D26,"Yes")+0.5*COUNTIF(Policy_Assessment!D7:D26,"Partial"))/COUNTA(Policy_Assessment!A7:A26)*100
```

**Asset Coverage Rate:**
```excel
=COUNTIF(Asset_Coverage!C7:C18,"Yes")/COUNTA(Asset_Coverage!A7:A18)*100
```

---

## 20. Cell Styling Standards

### 20.1 Colour Palette

| Element | Colour | Hex Code | Usage |
|---------|--------|----------|-------|
| Header Background | Navy Blue | #003366 | Title rows, headers |
| Header Text | White | #FFFFFF | Header text |
| Input Cells | Light Yellow | #FFFFCC | User input fields |
| Compliant/Yes | Green | #90EE90 | Positive status |
| Partial | Yellow | #FFFF00 | Partial compliance |
| Gap/No | Red | #FF6B6B | Non-compliance |
| N/A | Grey | #D3D3D3 | Not applicable |
| Border | Grey | #D0D0D0 | Cell borders |

### 20.2 Font Standards

| Element | Font | Size | Style |
|---------|------|:----:|-------|
| Title | Calibri | 14 | Bold |
| Column Headers | Calibri | 11 | Bold |
| Data Cells | Calibri | 10 | Regular |
| Notes | Calibri | 9 | Italic |

---

## 21. Generator Script Reference

### 21.1 Script Structure

```python
# =============================================================================
# ISMS-IMP-A.5.10-11.S1 - Acceptable Use Policy Assessment Generator
# =============================================================================
# ISO 27001:2022 Control A.5.10: Acceptable Use of Information and Assets
# Generates assessment workbook for AUP completeness and effectiveness
# =============================================================================

# Document Metadata
DOCUMENT_ID = "ISMS-IMP-A.5.10-11.S1"
WORKBOOK_NAME = "Acceptable Use Policy Assessment"
CONTROL_ID = "A.5.10"
CONTROL_NAME = "Acceptable Use of Information and Other Associated Assets"

# Output Configuration
OUTPUT_FILENAME = f"{DOCUMENT_ID}_Acceptable_Use_Policy_Assessment_{GENERATED_TIMESTAMP}.xlsx"
```

### 21.2 Key Functions

| Function | Purpose |
|----------|---------|
| `create_workbook()` | Initialise workbook with standard structure |
| `create_instructions_sheet()` | Generate Instructions sheet |
| `create_policy_assessment_sheet()` | Generate Policy_Assessment with requirements |
| `create_asset_coverage_sheet()` | Generate Asset_Coverage with categories |
| `create_awareness_tracking_sheet()` | Generate Awareness_Tracking with formulas |
| `create_communication_matrix_sheet()` | Generate Communication_Matrix |
| `create_evidence_register_sheet()` | Generate Evidence_Register |
| `create_approval_sheet()` | Generate Approval_SignOff with summaries |
| `apply_data_validation()` | Add dropdown lists |
| `apply_conditional_formatting()` | Apply status-based formatting |
| `style_workbook()` | Apply consistent styling |

### 21.3 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| openpyxl | ≥3.0.0 | Excel workbook generation |
| datetime | stdlib | Date handling |
| logging | stdlib | Execution logging |

### 21.4 Execution

```bash
cd 10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/10_generator-master/
python3 generate_a510_11_1_acceptable_use_policy.py
mv ISMS-IMP-A.5.10-11.S1_*.xlsx ../90_workbooks/
```

### 21.5 Output Verification

After generation, verify:
- [ ] All 7 sheets created
- [ ] Headers styled correctly
- [ ] Pre-populated requirements present
- [ ] Data validation dropdowns functional
- [ ] Conditional formatting applied
- [ ] Formulas calculate correctly
- [ ] Column widths appropriate

---

**END OF SPECIFICATION**

---

*"Security is not a product, but a process."*
— Bruce Schneier

<!-- QA_VERIFIED: 2026-02-03 -->
