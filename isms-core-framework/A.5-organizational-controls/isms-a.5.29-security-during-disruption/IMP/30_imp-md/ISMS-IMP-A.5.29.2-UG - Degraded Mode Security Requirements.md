**ISMS-IMP-A.5.29.2-UG - Degraded Mode Security Requirements**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.29

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.29.2-UG |
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

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.29.2-TG.

---

## Assessment Overview

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

## Control Requirements

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

## Prerequisites

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

## Degradation Scenarios

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

## Completion Walkthrough

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

## Break-Glass Procedures

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

## Evidence Collection

### Evidence Requirements

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| **Break-Glass Test Results** | Annual activation test documentation | ISMS Evidence Library |
| **Personnel Drill Results** | Semi-annual availability drill results | ISMS Evidence Library |
| **Activation Logs** | Records of any actual break-glass usage | ISMS Evidence Library |
| **Security Debt Register** | Current register with aging data | ISMS Evidence Library |
| **Escalation Records** | Evidence of aged debt escalation | ISMS Evidence Library |

---

## Common Pitfalls

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

## Quality Checklist

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

## Review and Approval

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

## Integration with Other Controls

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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
