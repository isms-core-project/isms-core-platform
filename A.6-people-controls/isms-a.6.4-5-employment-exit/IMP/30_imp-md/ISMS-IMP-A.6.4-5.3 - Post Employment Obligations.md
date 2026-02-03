# ISMS-IMP-A.6.4-5.3 - Post-Employment Obligations

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.4-5.3 |
| **Title** | Post-Employment Obligations |
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
   - [1.4 Obligation Types](#14-obligation-types)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 NDA Tracking Framework](#17-nda-tracking-framework)
   - [1.8 Enforcement Procedures](#18-enforcement-procedures)
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

This workbook tracks and manages post-employment obligations for former personnel, ensuring that continuing confidentiality and security responsibilities are documented, communicated, and enforced. It serves as the operational tool for:

- **Obligation Registry**: Comprehensive tracking of post-employment obligations
- **NDA Status Monitoring**: Active monitoring of confidentiality agreement terms
- **Expiration Tracking**: Alerts for approaching and expired obligation periods
- **Enforcement Documentation**: Records of enforcement actions if required
- **Acknowledgement Tracking**: Evidence that obligations were communicated at exit
- **Compliance Reporting**: Management visibility into obligation compliance

ISO 27001:2022 Control A.6.5 requires that information security responsibilities that remain valid after termination be defined, enforced, and communicated. This workbook provides the operational implementation for that requirement.

### Scope

This assessment covers the following components:

**In Scope:**
- Post-employment confidentiality obligations (NDAs)
- Intellectual property restrictions
- Non-compete obligations (where applicable and enforceable)
- Non-solicitation obligations
- Trade secret protection requirements
- Data return/destruction confirmations
- Continuing security responsibilities
- Obligation expiration tracking
- Exit acknowledgement documentation
- Enforcement action records

**Out of Scope:**
- Initial NDA execution (covered in ISMS-IMP-A.6.6)
- Disciplinary processes (covered in ISMS-IMP-A.6.4-5.1)
- Exit procedures (covered in ISMS-IMP-A.6.4-5.2)
- Active employee obligations (covered in employment agreements)

### Business Value

Effective post-employment obligation management delivers:

| Value Area | Benefit |
|------------|---------|
| **Information Protection** | Confidentiality maintained beyond employment |
| **Legal Enforceability** | Documented evidence supports enforcement |
| **Deterrence** | Clear obligations deter violations |
| **Compliance** | Demonstrates ISO 27001 control effectiveness |
| **Risk Visibility** | Management awareness of obligation status |
| **IP Protection** | Trade secrets and IP rights preserved |

### Assessment Frequency

| Activity | Frequency | Responsible Party |
|----------|-----------|-------------------|
| Obligation Registry Review | Quarterly | Legal Counsel |
| Expiration Report Review | Monthly | Information Security Manager |
| Enforcement Review | As needed | Legal Counsel |
| Exit Acknowledgement Audit | Quarterly | HR |
| Full Assessment | Annual | ISM with Legal |

---

## 1.2 Control Requirements

### ISO 27001:2022 Control A.6.5

> *"Information security responsibilities and duties that remain valid after termination or change of employment should be defined, enforced and communicated to relevant personnel and other interested parties."*

**Control Type:** Preventive
**Security Properties:** Confidentiality
**Cybersecurity Concepts:** Protect
**Operational Capabilities:** Legal and Compliance

### Implementation Requirements

Control A.6.5 requires organisations to:

**1. Definition of Continuing Obligations**
- Identify which responsibilities continue post-employment
- Document obligation duration and scope
- Specify information and activities covered
- Define consequences of violation

**2. Enforcement Mechanisms**
- Establish monitoring procedures (where appropriate)
- Define enforcement triggers
- Document enforcement procedures
- Maintain enforcement records

**3. Communication**
- Inform personnel of continuing obligations during exit
- Provide written summary of obligations
- Obtain signed acknowledgement
- Retain communication evidence

### What Auditors Look For

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Obligation Documentation** | Clear definition of post-employment duties |
| **Communication Evidence** | Exit interview records, signed acknowledgements |
| **Tracking System** | Registry of former personnel with active obligations |
| **Expiration Management** | Process for tracking obligation expiration |
| **Enforcement Capability** | Documented enforcement procedures |

---

## 1.3 Prerequisites

### Required Access

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| NDA Repository | Read | Access to signed agreements |
| HR Information System | Read | Leaver records |
| Legal Case System | Read/Write | Enforcement tracking |
| ISMS Evidence Library | Write | Evidence storage |

### Required Information

| Information | Source | Why Needed |
|-------------|--------|------------|
| Standard NDA templates | Legal | Obligation terms |
| Leaver records | HR | Former personnel list |
| Exit interview records | HR | Acknowledgement evidence |
| Enforcement history | Legal | Historical cases |

### Prerequisite Checklist

- [ ] NDA templates and terms understood
- [ ] Leaver records accessible
- [ ] Exit interview process includes obligation communication
- [ ] Legal Counsel available for enforcement queries
- [ ] Obligation duration periods confirmed

---

## 1.4 Obligation Types

### Understanding Post-Employment Obligations

#### Confidentiality Obligations

| Aspect | Description |
|--------|-------------|
| **Scope** | All non-public information accessed during employment |
| **Duration** | Typically 2-5 years, or indefinite for trade secrets |
| **Source** | Employment contract, NDA, company policies |
| **Enforceability** | Generally enforceable in all jurisdictions |

**Covered Information:**
- Business strategies and plans
- Customer and client information
- Technical specifications and designs
- Financial data
- Personnel information
- Vendor and partner information
- Trade secrets

#### Intellectual Property Obligations

| Aspect | Description |
|--------|-------------|
| **Scope** | Work product created during employment |
| **Duration** | Perpetual (ownership remains with organisation) |
| **Source** | Employment contract, IP assignment agreement |
| **Enforceability** | Strong legal protections available |

**Covered Items:**
- Software code and algorithms
- Inventions and patents
- Documentation and processes
- Creative works
- Customer solutions

#### Non-Compete Obligations

| Aspect | Description |
|--------|-------------|
| **Scope** | Restriction on working for competitors |
| **Duration** | Typically 6-24 months |
| **Source** | Employment contract (separate clause) |
| **Enforceability** | Varies by jurisdiction; limited in Switzerland |

**Note:** Non-compete clauses have limited enforceability in Switzerland and require specific conditions (compensation, reasonable scope).

#### Non-Solicitation Obligations

| Aspect | Description |
|--------|-------------|
| **Scope** | Restriction on soliciting employees or customers |
| **Duration** | Typically 12-24 months |
| **Source** | Employment contract, NDA |
| **Enforceability** | Generally more enforceable than non-compete |

**Types:**
- Employee non-solicitation
- Customer non-solicitation
- Vendor non-solicitation

#### Data Return/Destruction Obligations

| Aspect | Description |
|--------|-------------|
| **Scope** | Return or certified destruction of company data |
| **Duration** | Must be completed by termination |
| **Source** | NDA, acceptable use policy |
| **Enforceability** | Enforceable with documentation |

**Requirements:**
- Return all physical materials
- Delete electronic copies
- Remove from personal devices
- Certify destruction in writing

---

## 1.5 Workbook Structure

### Sheet Overview

| Sheet | Purpose | Primary User | Update Frequency |
|-------|---------|--------------|------------------|
| **Instructions** | Guidance | All users | As needed |
| **Obligation_Types** | Obligation definitions | Legal, ISM | Annual |
| **Former_Personnel** | Registry of former staff with obligations | HR | Ongoing |
| **Active_Obligations** | Current active obligations | ISM | Ongoing |
| **Expiration_Tracker** | Approaching and expired obligations | ISM | Monthly |
| **Acknowledgement_Log** | Exit acknowledgement records | HR | Ongoing |
| **Enforcement_Register** | Enforcement actions | Legal | As needed |
| **Evidence_Register** | Evidence tracking | ISM | Ongoing |
| **Approval_SignOff** | Assessment authorisation | Approvers | At completion |

---

## 1.6 Completion Walkthrough

### Step 1: Complete Obligation_Types Sheet

**Time estimate:** 1-2 hours

Document all obligation types and their terms:

#### Column A: Obligation_ID

- **Format:** OBL-XXX
- **Example:** OBL-001

#### Column B: Obligation_Type

- **Options:** Confidentiality, IP Assignment, Non-Compete, Non-Solicitation, Data Return

#### Column C: Description

- **Format:** Detailed description of the obligation
- **Example:** Protection of confidential information accessed during employment

#### Column D: Standard_Duration

- **Format:** Period or "Indefinite"
- **Example:** 3 years, Indefinite (trade secrets)

#### Column E: Source_Document

- **Format:** Document reference
- **Example:** Employment Contract Section 12, NDA Clause 5

#### Column F: Applicable_To

- **Format:** Who this applies to
- **Options:** All Employees, Executives, Technical Staff, Contractors

#### Column G: Enforceability_Notes

- **Format:** Jurisdiction-specific notes
- **Example:** Fully enforceable under Swiss law

### Step 2: Complete Former_Personnel Sheet

**Time estimate:** Ongoing

Track all former personnel with active obligations:

#### Column A: Person_ID

- **Format:** FP-YYYY-XXX
- **Example:** FP-2025-047

#### Column B: Name

- **Format:** Full name
- Note: May be pseudonymised for privacy

#### Column C: Exit_Date

- **Format:** DD.MM.YYYY

#### Column D: Exit_Type

- **Options:** Voluntary, Involuntary, Contract End, Retirement

#### Column E: Position_Held

- **Format:** Last position

#### Column F: Access_Level

- **Options:** Standard, Elevated, Privileged, Executive
- Indicates sensitivity of information accessed

#### Column G: NDA_Reference

- **Format:** NDA document reference
- **Example:** NDA-2023-0156

#### Column H: Obligations_End_Date

- **Format:** DD.MM.YYYY (latest obligation expiry)

#### Column I: Status

- **Options:** Active Obligations, Expired, Under Enforcement

### Step 3: Complete Active_Obligations Sheet

**Time estimate:** Ongoing

Track individual active obligations:

#### Column A: Obligation_Ref

- **Format:** ACT-YYYY-XXXX
- **Example:** ACT-2025-0012

#### Column B: Person_ID

- Link to Former_Personnel

#### Column C: Obligation_Type

- Link to Obligation_Types

#### Column D: Start_Date

- **Format:** DD.MM.YYYY (typically exit date)

#### Column E: End_Date

- **Format:** DD.MM.YYYY or "Indefinite"

#### Column F: Specific_Terms

- **Format:** Any specific terms for this individual
- **Example:** Extended to 5 years due to executive role

#### Column G: Monitoring_Required

- **Options:** Yes, No, Periodic
- Whether active monitoring is appropriate

#### Column H: Status

- **Options:** Active, Expired, Waived, Under Enforcement

### Step 4: Complete Expiration_Tracker Sheet

**Time estimate:** Monthly review

Track obligations approaching or past expiration:

#### Column A: Obligation_Ref

- Link to Active_Obligations

#### Column B: Person_Name

- From Former_Personnel

#### Column C: Obligation_Type

- Type of obligation

#### Column D: Expiration_Date

- **Format:** DD.MM.YYYY

#### Column E: Days_Until_Expiry

- **Formula:** =D2-TODAY()

#### Column F: Status

- **Options:** Expiring Soon (<90 days), Expired, Acknowledged

#### Column G: Action_Required

- **Format:** Required action
- **Example:** Send reminder letter, Update status

#### Column H: Action_Taken

- **Format:** Action completed
- **Example:** Reminder sent 01.01.2026

### Step 5: Complete Acknowledgement_Log Sheet

**Time estimate:** Ongoing

Track exit acknowledgements:

#### Column A: Ack_ID

- **Format:** ACK-YYYY-XXX
- **Example:** ACK-2025-089

#### Column B: Person_ID

- Link to Former_Personnel

#### Column C: Exit_Date

- **Format:** DD.MM.YYYY

#### Column D: Acknowledgement_Type

- **Options:** Exit Interview, Written Acknowledgement, Email Confirmation

#### Column E: Acknowledgement_Date

- **Format:** DD.MM.YYYY

#### Column F: Obligations_Summarised

- **Options:** Yes, No
- Whether obligations were summarised to individual

#### Column G: Signed_Document

- **Options:** Yes, No
- Whether signed acknowledgement obtained

#### Column H: Document_Location

- **Format:** Evidence location
- **Example:** ISMS Evidence Library/A.6.5/Acknowledgements/

### Step 6: Complete Enforcement_Register Sheet

**Time estimate:** As needed

Document any enforcement actions:

#### Column A: Enforcement_ID

- **Format:** ENF-YYYY-XXX
- **Example:** ENF-2026-001

#### Column B: Person_ID

- Link to Former_Personnel

#### Column C: Obligation_Violated

- Link to Obligation_Types

#### Column D: Violation_Date

- **Format:** DD.MM.YYYY (when discovered)

#### Column E: Violation_Description

- **Format:** Description of alleged violation
- **Example:** Shared confidential pricing information with competitor

#### Column F: Detection_Method

- **Format:** How violation was detected
- **Example:** Customer report, Social media, Third-party notification

#### Column G: Enforcement_Action

- **Format:** Action taken
- **Example:** Cease and desist letter, Legal proceedings initiated

#### Column H: Status

- **Options:** Under Investigation, Cease and Desist Sent, Legal Action, Resolved

#### Column I: Outcome

- **Format:** Resolution
- **Example:** Individual acknowledged and ceased activity

### Step 7: Complete Evidence_Register and Approval Sheets

Complete per standard processes.

---

## 1.7 NDA Tracking Framework

### NDA Lifecycle Post-Employment

```
Employment Ends
       │
       ▼
Exit Interview
(Obligations communicated)
       │
       ▼
Written Acknowledgement
(Signed confirmation)
       │
       ▼
Active Monitoring Period
(If required)
       │
       ▼
Expiration Tracking
(Monthly review)
       │
       ├──► Expiration ──► Archive Record
       │
       └──► Violation Detected ──► Enforcement
```

### Obligation Duration Guidelines

| Obligation Type | Typical Duration | Maximum Duration |
|-----------------|------------------|------------------|
| General Confidentiality | 2-3 years | 5 years |
| Trade Secrets | Indefinite | Indefinite |
| IP Assignment | Perpetual | Perpetual |
| Non-Compete | 6-12 months | 24 months |
| Non-Solicitation | 12-24 months | 36 months |
| Data Return | Immediate | At exit |

### Risk-Based Monitoring

| Former Role | Access Level | Monitoring Approach |
|-------------|--------------|---------------------|
| Executive/C-Suite | Full strategic access | Enhanced monitoring (public announcements, competitor moves) |
| Technical Lead | Source code, architecture | Moderate monitoring (industry publications, patents) |
| Sales/Account Manager | Customer relationships | Customer feedback monitoring |
| Standard Employee | Limited access | Minimal monitoring (incident-triggered) |

---

## 1.8 Enforcement Procedures

### Enforcement Triggers

| Trigger | Source | Response |
|---------|--------|----------|
| Customer complaint | Customer relationship | Investigate, involve Legal |
| Competitor intelligence | Market monitoring | Assess, involve Legal |
| Social media disclosure | PR/Marketing monitoring | Investigate, cease and desist |
| Patent filing | IP watch service | Assess, involve Legal/IP |
| Employee report | Internal hotline | Investigate, document |

### Enforcement Escalation

**Level 1: Informal Resolution**
- Contact former employee directly
- Remind of obligations
- Request cessation of activity
- Document interaction

**Level 2: Formal Notice**
- Cease and desist letter
- Sent via Legal Counsel
- Documented delivery
- Deadline for response

**Level 3: Legal Action**
- Injunction application
- Damages claim
- Criminal referral (if theft)
- Full legal proceedings

### Evidence Preservation for Enforcement

| Evidence Type | How to Preserve |
|---------------|-----------------|
| Original NDA | Certified copy from records |
| Employment Contract | HR records |
| Exit Acknowledgement | ISMS Evidence Library |
| Violation Evidence | Screenshots, correspondence, third-party statements |
| Communication Records | Email, letter copies with proof of delivery |

---

## 1.9 Evidence Collection

### Evidence Requirements

| Evidence Type | Description | Retention |
|---------------|-------------|-----------|
| **Obligation Definitions** | Documented obligation types | Current version |
| **Former Personnel Registry** | List with obligation status | 7 years post-expiry |
| **Signed Acknowledgements** | Exit acknowledgement documents | 7 years post-expiry |
| **Expiration Reports** | Monthly tracking reports | 3 years |
| **Enforcement Records** | Any enforcement actions | 10 years |
| **Completed Workbook** | This assessment | 3 cycles |

### Evidence Storage

**Naming Convention:**
```
EVD-A.6.4-5.3_[EvidenceType]_[YYYYMMDD].[ext]
```

---

## 1.10 Common Pitfalls

### Obligation Definition Pitfalls

**MISTAKE**: Vague or undefined post-employment obligations
**CORRECT**: Clearly document all obligation types with specific duration, scope, and enforceability; ensure obligations are defined in employment contracts and NDAs before exit; avoid ambiguous terms

**MISTAKE**: No distinction between obligation types
**CORRECT**: Distinguish between confidentiality (broad), trade secrets (indefinite), IP (perpetual), and restrictive covenants (time-limited); apply appropriate tracking and enforcement to each

**MISTAKE**: Unenforceable non-compete clauses
**CORRECT**: Consult Legal on jurisdiction-specific enforceability; in Switzerland, non-competes require compensation and reasonable scope; focus on enforceable confidentiality instead

**MISTAKE**: No consideration of role-based risk
**CORRECT**: Apply risk-based approach to obligation duration and monitoring; executives and technical staff with strategic access may require extended obligations

### Tracking Pitfalls

**MISTAKE**: No systematic tracking of former personnel
**CORRECT**: Maintain comprehensive registry of all former personnel with active obligations; update status as obligations expire; integrate with HR leaver process

**MISTAKE**: Missing expiration tracking
**CORRECT**: Implement monthly review of approaching expirations; automate alerts where possible; archive expired obligations appropriately

**MISTAKE**: Incomplete acknowledgement records
**CORRECT**: Obtain signed acknowledgement at exit for all personnel; document obligations communicated during exit interview; store evidence in ISMS Evidence Library

**MISTAKE**: No link to original NDA
**CORRECT**: Maintain clear reference to signed NDA for each former employee; ensure NDA is retrievable if enforcement needed; verify NDA exists before tracking obligations

### Communication Pitfalls

**MISTAKE**: Obligations not communicated at exit
**CORRECT**: Include obligation summary in exit interview; provide written reminder of continuing duties; obtain signed acknowledgement; send reminder letter post-exit

**MISTAKE**: No written acknowledgement obtained
**CORRECT**: Require signed acknowledgement as part of exit clearance; escalate if refused; document refusal and witness

**MISTAKE**: Unclear obligation terms in communication
**CORRECT**: Use clear, plain language in exit communication; specify what is covered, duration, and consequences; avoid legal jargon that may be misunderstood

**MISTAKE**: No reminder before expiration
**CORRECT**: Send courtesy reminder as obligations approach expiration (for long-duration obligations); reinforces importance; maintains relationship

### Enforcement Pitfalls

**MISTAKE**: No enforcement capability
**CORRECT**: Define enforcement procedures in advance; ensure Legal Counsel availability; maintain evidence for potential enforcement; act promptly on violations

**MISTAKE**: Delayed response to violations
**CORRECT**: Respond quickly to suspected violations; delays weaken legal position; preserve evidence immediately; involve Legal early

**MISTAKE**: No evidence preservation
**CORRECT**: Maintain all original documents (NDA, acknowledgements); preserve violation evidence immediately; maintain chain of custody; use forensic preservation for digital evidence

**MISTAKE**: Enforcement without Legal involvement
**CORRECT**: Always involve Legal Counsel before enforcement action; ensure actions are legally defensible; avoid harassment claims; document all communications

---

## 1.11 Quality Checklist

### Obligation Framework Checks

- [ ] All obligation types documented with clear terms
- [ ] Duration and scope defined for each type
- [ ] Source documents (NDA templates) referenced
- [ ] Enforceability notes included
- [ ] Risk-based approach documented

### Tracking Checks

- [ ] Former personnel registry complete
- [ ] All active obligations documented
- [ ] Expiration tracking current
- [ ] Monthly review process established
- [ ] Archive process for expired obligations defined

### Communication Checks

- [ ] Exit interview includes obligation communication
- [ ] Written acknowledgement template available
- [ ] Acknowledgement log maintained
- [ ] Process for refused acknowledgement documented

### Evidence Checks

- [ ] All framework documents stored
- [ ] Sample acknowledgements available
- [ ] Evidence naming convention followed
- [ ] Storage locations verified

### Enforcement Checks

- [ ] Enforcement procedures documented
- [ ] Legal Counsel involvement defined
- [ ] Evidence preservation procedures established
- [ ] Escalation path clear

---

## 1.12 Review and Approval

### Review Process

#### Step 1: Self-Review

- Complete Quality Checklist
- Verify all sheets complete
- Check evidence links

#### Step 2: Legal Counsel Review

**Reviewer:** Legal Counsel
**Timeframe:** 10 business days
**Scope:** Obligation definitions, enforceability, procedures

#### Step 3: HR Director Review

**Reviewer:** HR Director
**Timeframe:** 5 business days
**Scope:** Exit process integration, acknowledgement procedures

#### Step 4: CISO Approval

**Approver:** CISO
**Timeframe:** 5 business days
**Scope:** Overall security effectiveness

---

## 1.13 Regulatory Compliance

### Swiss Employment Law

| Requirement | Implication |
|-------------|-------------|
| **OR Art. 321a** | Employee duty of loyalty extends post-employment for confidential information |
| **OR Art. 340** | Non-compete requires compensation and reasonable scope |
| **Unfair Competition Act** | Protection of trade secrets |
| **nDSG** | Personal data handling in obligation tracking |

### Data Protection Considerations

| Aspect | Requirement |
|--------|-------------|
| **Retention Period** | Track obligations only while active + reasonable buffer |
| **Minimisation** | Collect only necessary data |
| **Access Control** | Restrict access to obligation records |
| **Deletion** | Archive/delete after retention period |

---

## 1.14 Related Controls

| Control | Relationship |
|---------|--------------|
| **A.6.6** | NDAs provide source of obligations |
| **A.6.4** | Disciplinary process may lead to enhanced obligations |
| **A.5.32-33** | IP and information protection framework |
| **A.5.31** | Legal and regulatory requirements |

---

# PART II: TECHNICAL SPECIFICATION

---

## 2.1 Workbook Architecture

### File Details

| Attribute | Value |
|-----------|-------|
| **Filename** | `ISMS-IMP-A.6.4-5.3_Post_Employment_Obligations_YYYYMMDD.xlsx` |
| **Format** | Microsoft Excel Open XML (.xlsx) |
| **Sheets** | 9 |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows | Columns |
|-------------|------------|---------|------|---------|
| 1 | Instructions | Guidance | 50 | 2 |
| 2 | Obligation_Types | Obligation definitions | 20 | 7 |
| 3 | Former_Personnel | Personnel registry | 500+ | 9 |
| 4 | Active_Obligations | Active tracking | 1000+ | 8 |
| 5 | Expiration_Tracker | Expiration monitoring | 100+ | 8 |
| 6 | Acknowledgement_Log | Exit acknowledgements | 500+ | 8 |
| 7 | Enforcement_Register | Enforcement records | 50+ | 9 |
| 8 | Evidence_Register | Evidence tracking | 50+ | 6 |
| 9 | Approval_SignOff | Authorisation | 15 | 3 |

---

## 2.2 Sheet Specifications

### Sheet 2: Obligation_Types

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Obligation_ID | 14 | Text |
| B | Obligation_Type | 20 | List |
| C | Description | 50 | Text |
| D | Standard_Duration | 20 | Text |
| E | Source_Document | 30 | Text |
| F | Applicable_To | 25 | List |
| G | Enforceability_Notes | 45 | Text |

### Sheet 3: Former_Personnel

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Person_ID | 16 | Text |
| B | Name | 30 | Text |
| C | Exit_Date | 14 | Date |
| D | Exit_Type | 20 | List |
| E | Position_Held | 30 | Text |
| F | Access_Level | 16 | List |
| G | NDA_Reference | 20 | Text |
| H | Obligations_End_Date | 14 | Date |
| I | Status | 18 | List |

### Sheet 4: Active_Obligations

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Obligation_Ref | 18 | Text |
| B | Person_ID | 16 | List |
| C | Obligation_Type | 20 | List |
| D | Start_Date | 14 | Date |
| E | End_Date | 14 | Date/Text |
| F | Specific_Terms | 40 | Text |
| G | Monitoring_Required | 18 | List |
| H | Status | 18 | List |

### Sheet 5: Expiration_Tracker

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Obligation_Ref | 18 | List |
| B | Person_Name | 30 | Text |
| C | Obligation_Type | 20 | Text |
| D | Expiration_Date | 14 | Date |
| E | Days_Until_Expiry | 16 | Formula |
| F | Status | 20 | List |
| G | Action_Required | 35 | Text |
| H | Action_Taken | 35 | Text |

---

## 2.3 Data Validations

### Obligation_Type Dropdown

```python
OBLIGATION_TYPE_LIST = [
    "Confidentiality",
    "Trade Secrets",
    "IP Assignment",
    "Non-Compete",
    "Non-Solicitation (Employee)",
    "Non-Solicitation (Customer)",
    "Data Return"
]
```

### Exit_Type Dropdown

```python
EXIT_TYPE_LIST = [
    "Voluntary Resignation",
    "Involuntary Termination",
    "Contract End",
    "Retirement",
    "Role Change"
]
```

### Access_Level Dropdown

```python
ACCESS_LEVEL_LIST = [
    "Standard",
    "Elevated",
    "Privileged",
    "Executive"
]
```

### Obligation_Status Dropdown

```python
OBLIGATION_STATUS_LIST = [
    "Active",
    "Expired",
    "Waived",
    "Under Enforcement"
]
```

### Personnel_Status Dropdown

```python
PERSONNEL_STATUS_LIST = [
    "Active Obligations",
    "All Expired",
    "Under Enforcement"
]
```

### Expiration_Status Dropdown

```python
EXPIRATION_STATUS_LIST = [
    "Expiring Soon",
    "Expired",
    "Acknowledged",
    "Extended"
]
```

### Enforcement_Status Dropdown

```python
ENFORCEMENT_STATUS_LIST = [
    "Under Investigation",
    "Cease and Desist Sent",
    "Legal Action Initiated",
    "Resolved",
    "No Action Required"
]
```

### Monitoring_Required Dropdown

```python
MONITORING_REQUIRED_LIST = [
    "Yes",
    "No",
    "Periodic"
]
```

### Acknowledgement_Type Dropdown

```python
ACKNOWLEDGEMENT_TYPE_LIST = [
    "Exit Interview",
    "Written Acknowledgement",
    "Email Confirmation",
    "Refused"
]
```

---

## 2.4 Conditional Formatting

### Active_Obligations Sheet

#### Status Formatting

| Value | Fill Colour |
|-------|-------------|
| Active | Light Green (#C6EFCE) |
| Expired | Light Grey (#D9D9D9) |
| Under Enforcement | Light Red (#FFC7CE) |
| Waived | Light Blue (#BDD7EE) |

### Expiration_Tracker Sheet

#### Days Until Expiry Formatting

| Condition | Fill Colour |
|-----------|-------------|
| < 0 (Expired) | Light Red (#FFC7CE) |
| 0-30 days | Light Orange (#FCE4D6) |
| 31-90 days | Light Yellow (#FFEB9C) |
| > 90 days | Light Green (#C6EFCE) |

### Enforcement_Register Sheet

#### Status Formatting

| Value | Fill Colour |
|-------|-------------|
| Under Investigation | Light Yellow (#FFEB9C) |
| Cease and Desist Sent | Light Orange (#FCE4D6) |
| Legal Action Initiated | Light Red (#FFC7CE) |
| Resolved | Light Green (#C6EFCE) |

---

## 2.5 Formula Specifications

### Expiration_Tracker Calculated Fields

#### Days Until Expiry

```excel
=IF(D2="Indefinite", "N/A", D2-TODAY())
```

#### Status Auto-Calculate

```excel
=IF(E2="N/A", "Indefinite", IF(E2<0, "Expired", IF(E2<=90, "Expiring Soon", "Active")))
```

### Former_Personnel Summary

#### Count Active Obligations

```excel
=COUNTIF(Former_Personnel!I:I, "Active Obligations")
```

#### Count Under Enforcement

```excel
=COUNTIF(Former_Personnel!I:I, "Under Enforcement")
```

---

## 2.6 Cell Styling Standards

Standard styling as per ISMS framework.

---

## 2.7 Generator Script Reference

### Script Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a645_3_post_employment.py` |
| **Location** | `10-isms-scr-base/isms-a.6.4-5-employment-exit/10_generator-master/` |
| **Language** | Python 3.8+ |
| **Dependencies** | openpyxl, logging, datetime |

### Execution

```bash
cd 10-isms-scr-base/isms-a.6.4-5-employment-exit/10_generator-master
python3 generate_a645_3_post_employment.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Russian Proverb

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-02-03 -->
