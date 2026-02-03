# ISMS-IMP-A.5.29.2 — Degraded Mode Security Requirements

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.29.2 |
| **Title** | Degraded Mode Security Requirements |
| **Control Reference** | ISO/IEC 27001:2022 A.5.29 |
| **Control Name** | Information Security During Disruption |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Chief Information Security Officer (CISO) |
| **Classification** | Internal |
| **Framework Version** | 1.0 |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Degradation Scenarios](#14-degradation-scenarios)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 Break-Glass Procedures](#17-break-glass-procedures)
   - [1.8 Evidence Collection](#18-evidence-collection)
   - [1.9 Common Pitfalls](#19-common-pitfalls)
   - [1.10 Quality Checklist](#110-quality-checklist)
   - [1.11 Review and Approval](#111-review-and-approval)
   - [1.12 Integration with Other Controls](#112-integration-with-other-controls)
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

This workbook documents detailed requirements for operating in degraded security modes during disruption. It serves as the authoritative registry for:

- **Degradation Scenarios**: Specific situations requiring security control relaxation
- **Break-Glass Procedures**: Emergency access mechanisms and activation protocols
- **Time-Limited Exceptions**: Duration and renewal requirements for security relaxations
- **Elevated Monitoring**: Enhanced surveillance requirements during degraded operations
- **Personnel Availability**: Security team continuity and succession planning
- **Security Debt Tracking**: Deferred security activities requiring post-disruption remediation

The Degraded Mode Security Requirements Assessment ensures that security relaxations during disruption are controlled, documented, time-limited, and subject to post-incident review.

### Scope

This assessment covers the following components:

**In Scope:**
- Degraded security mode definitions and criteria
- Break-glass account inventory and activation procedures
- Emergency access authorisation chain
- Time limits for security relaxations
- Elevated monitoring requirements per security posture level
- Security personnel availability and succession
- Security debt register structure
- Post-disruption review requirements

**Out of Scope:**
- Security control inventory (covered in ISMS-IMP-A.5.29.1)
- Recovery verification procedures (covered in ISMS-IMP-A.5.29.3)
- Compliance dashboards (covered in ISMS-IMP-A.5.29.4)
- Incident response procedures (covered in A.5.24-28)

### Business Value

Well-documented degraded mode requirements deliver:

| Value Area | Benefit |
|------------|---------|
| **Controlled Flexibility** | Pre-approved relaxations prevent ad-hoc security bypasses |
| **Accountability** | Clear records of who authorised what relaxations |
| **Time Limits** | Prevents indefinite security degradation |
| **Recovery Tracking** | Security debt captured for remediation |
| **Audit Evidence** | Documented decisions support compliance |
| **Personnel Continuity** | Security functions survive key person unavailability |

### Assessment Frequency

| Activity | Frequency | Responsible Party |
|----------|-----------|-------------------|
| Break-Glass Account Testing | Annual | Security Team |
| Personnel Availability Drill | Semi-annual | CISO |
| Degradation Scenario Review | Annual | Security Team |
| Security Debt Review | Monthly | CISO |
| Full Assessment | Annual | Security Team |

---

## 1.2 Control Requirements

### ISO 27001:2022 Control A.5.29

> *"The organisation should plan how to maintain information security at an appropriate level during disruption."*

**Implementation Focus**: This assessment addresses the "appropriate level" aspect by defining what degradation is acceptable and what compensating measures must be implemented.

### Key Requirements

**1. Emergency Access Procedures**
- Break-glass accounts for emergency scenarios
- Activation authority defined
- Time-limited access with mandatory review
- Enhanced logging during emergency access

**2. Acceptable Degradation**
- Pre-approved degradation scenarios
- Compensating controls for each relaxation
- Time limits for each degradation type
- Escalation requirements

**3. Security Personnel Continuity**
- Succession plan for security roles
- Contact information maintained offline
- Cross-training for critical functions
- Geographic distribution where possible

**4. Security Debt Management**
- All relaxations logged as security debt
- Remediation plans required
- Escalation for aged debt items
- Executive visibility for extended relaxations

### What Auditors Look For

ISO 27001 auditors examining degraded mode requirements will verify:

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Break-Glass Controls** | Documented accounts, activation procedures, test results |
| **Time Limits** | Defined durations, renewal process, enforcement |
| **Enhanced Monitoring** | Monitoring requirements per posture level, implementation evidence |
| **Personnel Availability** | Succession documentation, contact test results |
| **Security Debt** | Register maintained, aging reports, escalation evidence |

---

## 1.3 Prerequisites

### Before Starting This Assessment

#### Required Access

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| Identity Management System | Admin | Inventory break-glass accounts |
| Security Monitoring Platform | Read | Verify monitoring capabilities |
| ISMS Evidence Library | Write | Upload evidence |
| HR System | Read | Verify personnel information |

#### Required Information

| Information | Source | Why Needed |
|-------------|--------|------------|
| Break-glass account inventory | IAM Team | Document emergency access |
| Security team roster | HR/Security | Verify personnel availability |
| Monitoring platform capabilities | SOC | Document enhancement options |
| Previous disruption incidents | Security Team | Learn from past experience |

#### Prerequisite Checklist

Before proceeding, verify:

- [ ] Access to identity management system confirmed
- [ ] Security monitoring platform documentation available
- [ ] Security team roster current
- [ ] Previous incident reports reviewed
- [ ] Assessment scope approved by CISO

---

## 1.4 Degradation Scenarios

### Scenario Categories

| Scenario | Description | Typical Duration | Authority |
|----------|-------------|------------------|-----------|
| **MFA Unavailable** | Multi-factor authentication infrastructure failure | Hours to days | CISO |
| **Network Segmentation Bypass** | Emergency connectivity requirements | Hours | CIO + CISO |
| **Delayed Patching** | Patch deployment postponed for stability | Days to weeks | CISO |
| **Reduced Monitoring** | SOC capacity constraints | Hours to days | CISO |
| **Access Review Postponed** | Periodic reviews delayed | Days (max 30) | Security Manager |
| **Vulnerability Scan Delayed** | Scan schedule interrupted | Days to weeks | Security Manager |

### Scenario Impact Assessment

| Scenario | Confidentiality Impact | Integrity Impact | Availability Impact | Compensating Control |
|----------|----------------------|------------------|---------------------|---------------------|
| MFA Unavailable | High | Low | Medium | Enhanced logging, IP restrictions, session limits |
| Network Bypass | High | Medium | Low | Enhanced monitoring, time-limited access |
| Delayed Patching | Medium | High | Low | IDS/IPS signatures, compensating controls |
| Reduced Monitoring | High | High | Low | Manual log review, critical system focus |
| Access Review Delay | Medium | Low | Low | Stricter new access approval |
| Delayed Scans | Medium | Medium | Low | Manual patch review |

---

## 1.5 Workbook Structure

### Sheet Overview

The workbook consists of eight sheets:

| Sheet | Purpose | Primary User | Update Frequency |
|-------|---------|--------------|------------------|
| **Instructions** | Guidance and orientation | All users | As needed |
| **Degradation_Scenarios** | Acceptable degradation documentation | Security Team | Annual |
| **BreakGlass_Accounts** | Emergency account inventory | IAM Team | Upon change |
| **BreakGlass_Activation** | Activation log and procedures | Security Team | Per activation |
| **Elevated_Monitoring** | Enhanced monitoring requirements | SOC | Annual |
| **Personnel_Availability** | Security team succession | CISO | Quarterly |
| **Security_Debt_Register** | Deferred security tracking | Security Team | Ongoing |
| **Evidence_Register** | Evidence tracking | Security Team | Ongoing |
| **Approval_SignOff** | Assessment authorisation | Approvers | At completion |

### Sheet Relationships

```
┌─────────────────────┐
│    Instructions     │ ◄── Start here
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐     ┌─────────────────────┐
│Degradation_Scenarios│────►│Elevated_Monitoring  │
└──────────┬──────────┘     └─────────────────────┘
           │
           ▼
┌─────────────────────┐     ┌─────────────────────┐
│BreakGlass_Accounts  │────►│BreakGlass_Activation│
└──────────┬──────────┘     └─────────────────────┘
           │
           ▼
┌─────────────────────┐
│Personnel_Availability│
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│Security_Debt_Register│
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Evidence_Register  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Approval_SignOff   │ ◄── Complete here
└─────────────────────┘
```

---

## 1.6 Completion Walkthrough

### Step-by-Step Process

#### Step 1: Review Instructions (30 minutes)
1. Read the Instructions sheet completely
2. Understand the relationship to ISMS-IMP-A.5.29.1 (Security Control Inventory)
3. Identify stakeholders required for input:
   - IAM Team (break-glass accounts)
   - SOC/Security Operations (monitoring capabilities)
   - HR (personnel roster)
   - Security Team (procedures and scenarios)
4. Confirm access to prerequisite systems and information
5. Schedule time with stakeholders for information gathering

#### Step 2: Document Degradation Scenarios (4-6 hours)
1. List all acceptable degradation scenarios from organisational experience
2. For each scenario, define:
   - Trigger conditions (what initiates this degradation)
   - Control affected (link to Security Control Inventory)
   - Compensating controls required (specific measures)
   - Maximum duration (hours, days, or weeks)
   - Renewal process (who approves extension, documentation)
   - Authorisation required (role and alternate)
   - Posture level (Elevated, Degraded, Emergency)
3. Document "never acceptable" degradations explicitly:
   - Security controls that cannot be bypassed
   - Rationale for non-negotiable status
4. Validate scenarios with CISO for approval
5. Cross-reference with regulatory requirements (GDPR, NIS2, DORA)

#### Step 3: Inventory Break-Glass Accounts (2-4 hours)
1. Work with IAM team to list all break-glass accounts
2. For each account, document comprehensively:
   - Account identifier (unique ID)
   - Account name (descriptive)
   - Account type (Domain Admin, System Admin, etc.)
   - Target systems (scope of access)
   - Scope/permissions (specific privileges granted)
   - Credential storage location (safe, vault, split knowledge)
   - Activation authority (who can authorise)
   - Two-person requirement (Yes/No)
   - Default duration (hours)
   - Logging status (Enabled, Verified)
3. Verify accounts are disabled in normal operations
4. Document credential rotation schedule
5. Record last test date and results

#### Step 4: Document Activation Procedures (2-4 hours)
1. Define detailed activation workflow:
   - Emergency declaration (who can declare, how documented)
   - Request documentation (verbal OK, written within 4 hours)
   - Two-person rule (which accounts, how enforced)
   - Notification requirements (CISO, Security Team, Management)
   - Enhanced monitoring activation (what, when, how verified)
   - Time limit enforcement (default 24 hours, how extended)
   - Deactivation procedure (mandatory steps, verification)
2. Create activation log template with all required fields
3. Document post-emergency review requirements
4. Define credential rotation requirement after each use

#### Step 5: Define Elevated Monitoring (2-4 hours)
1. For each security posture level (Elevated, Degraded, Emergency):
   - Define monitoring enhancements (additional log sources, increased frequency)
   - Specify alert threshold changes (lower thresholds, additional rules)
   - Document manual review requirements (what, how often, by whom)
   - Identify responsible party for implementation
2. Map monitoring to SOC capabilities:
   - Verify technical feasibility
   - Document implementation steps
   - Identify dependencies
3. Test monitoring changes in non-production if possible

#### Step 6: Document Personnel Availability (2-4 hours)
1. List key security roles requiring coverage during disruption
2. For each role, document:
   - Primary holder (name, contact details)
   - Backup 1 (name, contact details)
   - Backup 2 (name, contact details)
   - Contact methods (mobile, personal email, messaging app)
   - Geographic location (for time zone and travel considerations)
3. Define on-call rotation for disruption periods
4. Document cross-training status for each backup
5. Record last contact test date and results
6. Record last drill participation date

#### Step 7: Establish Security Debt Register (1-2 hours)
1. Define debt categories:
   - Deferred Patch
   - Skipped Review
   - Delayed Scan
   - Config Exception
   - Access Exception
   - Other
2. Establish aging thresholds:
   - 0-30 days: Normal
   - 31-60 days: Warning
   - 61-90 days: Escalation to Security Manager
   - >90 days: Executive escalation
3. Define escalation rules and notification process
4. Create remediation tracking structure
5. Define closure verification requirements

#### Step 8: Complete Evidence Register (1-2 hours)
1. Link test results (break-glass activation tests)
2. Document personnel drill results
3. Link procedure documentation
4. Verify all evidence is accessible and current
5. Document evidence retention requirements

#### Step 9: Obtain Approvals (1-2 hours)
1. Security Manager review (technical accuracy, completeness)
2. CISO approval (strategic alignment, risk acceptance)
3. Executive Management notification (awareness, escalation path)
4. Archive approved assessment in ISMS Evidence Library

---

## 1.7 Break-Glass Procedures

### Break-Glass Account Requirements

| Requirement | Specification |
|-------------|---------------|
| **Account Status** | Disabled in normal operations |
| **Activation Authority** | CISO, CIO, or CEO (documented chain) |
| **Authentication** | Strong credentials stored securely (hardware token, safe, split knowledge) |
| **Scope** | Pre-defined, limited to recovery-essential systems |
| **Logging** | All actions logged with tamper protection |
| **Duration** | Default 24 hours, renewable with re-approval |
| **Deactivation** | Mandatory formal deactivation with password rotation |

### Activation Process

```
1. Emergency declared by authorised authority
         │
         ▼
2. Break-glass request documented (verbal OK, written within 4 hours)
         │
         ▼
3. Two-person rule for critical systems (if required)
         │
         ▼
4. Credentials retrieved and account enabled
         │
         ▼
5. CISO and Security Team notified
         │
         ▼
6. Enhanced monitoring activated
         │
         ▼
7. Time limit set (default: 24 hours)
         │
         ▼
8. Post-emergency: Deactivation and full review
```

### Testing Requirements

| Test Type | Frequency | Participants | Evidence |
|-----------|-----------|--------------|----------|
| **Activation Test** | Annual | Security Team, IAM | Test plan, results, issues found |
| **Credential Access Test** | Semi-annual | Designated personnel | Verification that credentials accessible |
| **Notification Test** | Quarterly | All stakeholders | Reachability confirmation |
| **Logging Verification** | Annual | Security Team | Log completeness check |

---

## 1.8 Evidence Collection

### Evidence Requirements

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| **Break-Glass Test Results** | Annual activation test documentation | ISMS Evidence Library |
| **Personnel Drill Results** | Semi-annual availability drill results | ISMS Evidence Library |
| **Activation Logs** | Records of any actual break-glass usage | ISMS Evidence Library |
| **Security Debt Register** | Current register with aging data | ISMS Evidence Library |
| **Escalation Records** | Evidence of aged debt escalation | ISMS Evidence Library |

---

## 1.9 Common Pitfalls

Avoid these common mistakes when completing this assessment:

❌ **MISTAKE: Break-glass accounts always enabled in normal operations**
- **Impact**: Standing privileged access creates persistent security risk; accounts may be compromised
- **Prevention**: Verify disabled status monthly; implement automated alerting for enabled state

❌ **MISTAKE: No two-person rule for critical system emergency access**
- **Impact**: Single point of compromise; no accountability or oversight during emergency
- **Prevention**: Require dual authorisation for domain admin and critical infrastructure access

❌ **MISTAKE: Break-glass credentials not tested regularly**
- **Impact**: Credentials may not work when urgently needed; delays in emergency response
- **Prevention**: Test credential accessibility and validity semi-annually; document test results

❌ **MISTAKE: No time limits defined on security degradation**
- **Impact**: Indefinite security reduction; "temporary" becomes permanent
- **Prevention**: Enforce maximum durations with mandatory renewal; auto-escalate overdue items

❌ **MISTAKE: Security debt not tracked in centralised register**
- **Impact**: Forgotten remediation items; accumulating security vulnerabilities
- **Prevention**: Maintain register; review monthly; report to CISO on aging items

❌ **MISTAKE: Security personnel contact information outdated**
- **Impact**: Cannot reach key people during emergency; delays in response
- **Prevention**: Quarterly contact verification; multiple contact methods per person

❌ **MISTAKE: No enhanced monitoring during degraded operations**
- **Impact**: Reduced visibility when threat exposure is highest
- **Prevention**: Pre-define monitoring enhancements per posture level; test SOC capability

❌ **MISTAKE: Break-glass activity not logged to tamper-proof location**
- **Impact**: No audit trail; cannot verify actions taken during emergency
- **Prevention**: Verify logging configuration before account activation; use immutable logs

❌ **MISTAKE: Single backup person for key security roles**
- **Impact**: Still vulnerable to unavailability; single point of failure
- **Prevention**: Minimum two backups per critical role; geographic distribution where possible

❌ **MISTAKE: Not testing succession procedures in drills**
- **Impact**: Backup personnel not prepared; delays and errors during real emergency
- **Prevention**: Include succession scenarios in all drills; rotate primary and backup roles

❌ **MISTAKE: Degradation scenarios not pre-approved by CISO**
- **Impact**: Ad-hoc decisions during crisis; inconsistent security posture
- **Prevention**: Pre-approve all degradation scenarios; document "never acceptable" items

❌ **MISTAKE: Compensating controls not defined for each degradation**
- **Impact**: Security gaps during degraded mode; no mitigation for relaxed controls
- **Prevention**: Require compensating control for every degradable control; test effectiveness

❌ **MISTAKE: Break-glass credential rotation neglected**
- **Impact**: Stale credentials may be compromised; known passwords in circulation
- **Prevention**: Mandatory rotation after each use; annual rotation minimum if unused

❌ **MISTAKE: No notification chain defined for emergency access**
- **Impact**: Key stakeholders unaware of emergency access; delayed oversight
- **Prevention**: Define notification requirements; automate where possible; verify delivery

❌ **MISTAKE: Security debt closure not verified with evidence**
- **Impact**: Items marked closed without actual remediation; false sense of resolution
- **Prevention**: Require closure evidence; independent verification for critical items

❌ **MISTAKE: Personnel cross-training incomplete or undocumented**
- **Impact**: Backup personnel lack skills; knowledge gaps during succession
- **Prevention**: Track cross-training status; include in annual review; schedule training

---

## 1.10 Quality Checklist

Before submitting this assessment, verify:

### Completeness Checks

- [ ] All degradation scenarios documented with compensating controls
- [ ] All break-glass accounts inventoried with full metadata
- [ ] Activation procedure documented and approved
- [ ] Elevated monitoring defined for each posture level
- [ ] All key security roles have minimum two backups
- [ ] Security debt register structure established
- [ ] Evidence linked for tests and drills
- [ ] "Never Acceptable" degradations explicitly documented
- [ ] Time limits defined for each degradation type
- [ ] Renewal process documented for extended degradations

### Accuracy Checks

- [ ] Break-glass accounts verified as disabled in IAM system
- [ ] Contact information tested and current (within 90 days)
- [ ] Credentials accessible (tested within 180 days)
- [ ] Monitoring enhancements technically feasible with SOC
- [ ] Time limits aligned with business requirements
- [ ] Two-person requirements documented for critical accounts
- [ ] Logging verification completed for all break-glass accounts
- [ ] Credential storage locations documented and secure

### Validation Checks

- [ ] Break-glass activation test completed within last 12 months
- [ ] Personnel contact test completed within last 90 days
- [ ] Succession drill completed within last 6 months
- [ ] Cross-training status verified for all backup personnel
- [ ] Security debt aging thresholds correctly configured
- [ ] Escalation rules tested and verified

### Approval Checks

- [ ] Degradation scenarios approved by CISO
- [ ] Break-glass procedures approved by CISO
- [ ] Security Manager reviewed assessment
- [ ] Executive Management informed
- [ ] Approval signatures captured with dates
- [ ] Assessment archived in ISMS Evidence Library

---

## 1.11 Review and Approval

### Approval Workflow

```
Assessor Completes Assessment
         │
         ▼
Security Manager Reviews
         │
         ▼
CISO Approves
         │
         ▼
Executive Management Notified
         │
         ▼
Assessment Published to ISMS Evidence Library
```

---

## 1.12 Integration with Other Controls

### Related ISMS Controls

| Control | Relationship |
|---------|--------------|
| **A.5.15-18** | Access control policies apply to break-glass with modifications |
| **A.8.15** | Logging requirements especially important during degraded mode |
| **A.8.16** | Monitoring enhancements during disruption |
| **A.5.24-28** | Incident management may trigger degraded mode |
| **A.5.30** | BC/DR plans may invoke degradation scenarios |

### Related ISMS-IMP Documents

| Document | Relationship |
|----------|--------------|
| **ISMS-IMP-A.5.29.1** | Security control inventory (what can be degraded) |
| **ISMS-IMP-A.5.29.3** | Recovery verification (resolving security debt) |
| **ISMS-IMP-A.5.29.4** | Compliance dashboard (tracking degradation metrics) |

---

# PART II: TECHNICAL SPECIFICATION

---

## 2.1 Workbook Architecture

### File Naming Convention

```
ISMS-IMP-A.5.29.2_Degraded_Mode_Security_Requirements_YYYYMMDD.xlsx
```

### Sheet Tab Order

1. Instructions
2. Degradation_Scenarios
3. BreakGlass_Accounts
4. BreakGlass_Activation
5. Elevated_Monitoring
6. Personnel_Availability
7. Security_Debt_Register
8. Evidence_Register
9. Approval_SignOff

---

## 2.2 Sheet Specifications

### Sheet 2: Degradation_Scenarios

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Scenario_ID | 15 | Text | Required |
| B | Scenario_Name | 30 | Text | Required |
| C | Trigger_Condition | 40 | Text | Required |
| D | Control_Affected | 25 | Text | Required |
| E | Degradation_Type | 20 | List | Temporary Bypass, Reduced Capability, Postponed, Alternative Method |
| F | Compensating_Control | 40 | Text | Required |
| G | Max_Duration | 20 | Text | Required |
| H | Renewal_Process | 30 | Text | Required |
| I | Authorisation_Required | 25 | Text | Required |
| J | Posture_Level | 15 | List | Elevated, Degraded, Emergency |
| K | Never_Acceptable | 40 | Text | Required |

### Sheet 3: BreakGlass_Accounts

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Account_ID | 15 | Text | Required |
| B | Account_Name | 25 | Text | Required |
| C | Account_Type | 20 | List | Domain Admin, System Admin, Database Admin, Network Admin, Application Admin, Other |
| D | Target_Systems | 35 | Text | Required |
| E | Scope_Permissions | 35 | Text | Required |
| F | Credential_Location | 30 | Text | Required |
| G | Activation_Authority | 25 | Text | Required |
| H | Two_Person_Required | 10 | List | Yes, No |
| I | Default_Duration | 15 | Text | Required |
| J | Logging_Enabled | 10 | List | Yes, No, Verified |
| K | Last_Rotation_Date | 15 | Date | Required |
| L | Last_Test_Date | 15 | Date | Required |
| M | Status | 12 | List | Disabled, Enabled, Unknown |

### Sheet 4: BreakGlass_Activation

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Activation_ID | 15 | Text | Required |
| B | Account_ID | 15 | Text | From BreakGlass_Accounts |
| C | Emergency_Type | 25 | Text | Required |
| D | Activation_DateTime | 20 | DateTime | Required |
| E | Authorised_By | 25 | Text | Required |
| F | Activated_By | 25 | Text | Required |
| G | Second_Person | 25 | Text | If two-person required |
| H | CISO_Notified | 10 | List | Yes, No |
| I | Expiry_DateTime | 20 | DateTime | Required |
| J | Renewed | 10 | List | Yes, No |
| K | Deactivation_DateTime | 20 | DateTime | Required |
| L | Post_Review_Completed | 10 | List | Yes, No |
| M | Issues_Found | 40 | Text | Optional |

### Sheet 5: Elevated_Monitoring

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Posture_Level | 15 | List | Elevated, Degraded, Emergency |
| B | Monitoring_Area | 25 | Text | Required |
| C | Normal_Frequency | 20 | Text | Required |
| D | Enhanced_Frequency | 20 | Text | Required |
| E | Alert_Threshold_Change | 30 | Text | Required |
| F | Manual_Review_Required | 10 | List | Yes, No |
| G | Review_Frequency | 20 | Text | If manual review |
| H | Responsible_Party | 25 | Text | Required |
| I | Implementation_Notes | 40 | Text | Optional |

### Sheet 6: Personnel_Availability

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Role_ID | 15 | Text | Required |
| B | Role_Name | 30 | Text | Required |
| C | Primary_Name | 25 | Text | Required |
| D | Primary_Phone | 20 | Text | Required |
| E | Primary_Email | 30 | Text | Required |
| F | Backup1_Name | 25 | Text | Required |
| G | Backup1_Phone | 20 | Text | Required |
| H | Backup1_Email | 30 | Text | Required |
| I | Backup2_Name | 25 | Text | Required |
| J | Backup2_Phone | 20 | Text | Required |
| K | Backup2_Email | 30 | Text | Required |
| L | Cross_Training_Status | 15 | List | Complete, Partial, None |
| M | Last_Contact_Test | 15 | Date | Required |
| N | Last_Drill_Date | 15 | Date | Required |

### Sheet 7: Security_Debt_Register

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Debt_ID | 15 | Text | Required |
| B | Debt_Type | 20 | List | Deferred Patch, Skipped Review, Delayed Scan, Config Exception, Access Exception, Other |
| C | Description | 40 | Text | Required |
| D | Disruption_Reference | 20 | Text | Optional |
| E | Created_Date | 15 | Date | Required |
| F | Owner | 25 | Text | Required |
| G | Remediation_Plan | 40 | Text | Required |
| H | Target_Date | 15 | Date | Required |
| I | Status | 15 | List | Open, In Progress, Closed |
| J | Age_Days | 10 | Formula | =TODAY()-E |
| K | Escalation_Required | 10 | Formula | =IF(J>30,"Yes","No") |
| L | Escalated_To | 25 | Text | If escalation required |
| M | Escalation_Date | 15 | Date | If escalated |
| N | Closure_Date | 15 | Date | If closed |
| O | Closure_Evidence | 30 | Text | If closed |

---

## 2.3 Data Validations

### Degradation Type Validation
```
Temporary Bypass, Reduced Capability, Postponed, Alternative Method
```

### Account Type Validation
```
Domain Admin, System Admin, Database Admin, Network Admin, Application Admin, Other
```

### Debt Type Validation
```
Deferred Patch, Skipped Review, Delayed Scan, Config Exception, Access Exception, Other
```

### Cross-Training Status Validation
```
Complete, Partial, None
```

---

## 2.4 Conditional Formatting

### BreakGlass_Accounts Sheet

| Condition | Formatting |
|-----------|------------|
| Status = "Enabled" | Red fill (should normally be disabled) |
| Last_Test_Date > 365 days ago | Yellow fill |
| Logging_Enabled != "Verified" | Orange text |

### Security_Debt_Register Sheet

| Condition | Formatting |
|-----------|------------|
| Age_Days > 90 | Red fill |
| Age_Days > 30 | Yellow fill |
| Status = "Closed" | Green fill |
| Escalation_Required = "Yes" | Bold red text |

---

## 2.5 Formula Specifications

### Security_Debt_Register Formulas

```excel
# Age Days
=IF(E4<>"",TODAY()-E4,"")

# Escalation Required
=IF(J4>30,"Yes","No")

# Executive Escalation Required (>90 days)
=IF(J4>90,"Executive","")
```

### Approval_SignOff Summary Formulas

```excel
# Total Break-Glass Accounts
=COUNTA(BreakGlass_Accounts!A4:A103)-COUNTBLANK(BreakGlass_Accounts!B4:B103)

# Accounts Tested This Year
=COUNTIF(BreakGlass_Accounts!L4:L103,">=" & DATE(YEAR(TODAY()),1,1))

# Open Security Debt Items
=COUNTIF(Security_Debt_Register!I4:I103,"Open")

# Overdue Security Debt (>30 days)
=COUNTIF(Security_Debt_Register!K4:K103,"Yes")
```

---

## 2.6 Cell Styling Standards

### Header Styling
- **Font**: Calibri 14pt Bold White
- **Fill**: Navy Blue (#003366)
- **Alignment**: Centre, Middle, Wrap Text
- **Row Height**: 30-40

### Column Header Styling
- **Font**: Calibri 10pt Bold
- **Fill**: Light Grey (#D9D9D9)
- **Alignment**: Centre, Middle, Wrap Text
- **Border**: Thin black all sides

### Input Cell Styling
- **Fill**: Light Yellow (#FFFFCC)
- **Border**: Thin black all sides
- **Alignment**: Left, Middle, Wrap Text

### Warning Cell Styling
- **Fill**: Light Red (#FFC7CE)
- **Font**: Bold

---

## 2.7 Generator Script Reference

**Script Name**: `generate_a529_2_degraded_mode.py`

**Location**: `10-isms-scr-base/isms-a.5.29-security-during-disruption/10_generator-master/`

**Output**: `ISMS-IMP-A.5.29.2_Degraded_Mode_Security_Requirements_YYYYMMDD.xlsx`

**Dependencies**:
- openpyxl
- logging
- datetime

---

**END OF SPECIFICATION**

---

*"In preparing for battle I have always found that plans are useless, but planning is indispensable."*
— Dwight D. Eisenhower

<!-- QA_VERIFIED: 2026-02-03 -->
