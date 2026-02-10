<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.29.3-UG:framework:UG:a.5.29.3 -->
**ISMS-IMP-A.5.29.3-UG - Recovery Security Verification**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.29

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.29.3-UG |
| **Title** | Recovery Security Verification |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.29.3-TG.

---

## Assessment Overview

### Purpose

This workbook documents the security verification activities required before, during, and after recovery from disruption. It serves as the authoritative registry for:

- **Security Recovery Checklist**: Validation activities per recovery phase
- **Emergency Access Deactivation**: Verification that break-glass accounts are disabled
- **Security Control Validation**: Confirmation all controls are restored to normal
- **Anomaly Detection**: Log review for suspicious activity during disruption
- **Security Debt Resolution**: Tracking and closing security debt items
- **Lessons Learned**: Security-focused post-incident review

The Recovery Security Verification Assessment ensures that the organisation does not return to normal operations with compromised security posture, lingering emergency access, or unaddressed security debt.

### Critical Principle — "Trust But Verify"

After any disruption, assume that security controls may have been compromised, bypassed, or degraded. Verification is mandatory before declaring return to normal operations.

### Scope

This assessment covers the following components:

**In Scope:**
- Security recovery checklist by phase (Immediate, Short-term, Medium-term, Long-term)
- Emergency access deactivation verification
- Security control restoration validation
- Post-disruption log analysis and anomaly detection
- Security debt closure tracking
- Attack vector monitoring during disruption
- Lessons learned security review
- BC/DR plan security updates

**Out of Scope:**
- Security control inventory (covered in ISMS-IMP-A.5.29.1)
- Degraded mode procedures (covered in ISMS-IMP-A.5.29.2)
- Compliance dashboards (covered in ISMS-IMP-A.5.29.4)
- Operational recovery procedures (covered in A.5.30, A.8.13-14)

### Business Value

Systematic recovery verification delivers:

| Value Area | Benefit |
|------------|---------|
| **Security Assurance** | Confidence that security is fully restored |
| **Threat Detection** | Identification of attacks during vulnerable period |
| **Debt Resolution** | Systematic closure of security exceptions |
| **Continuous Improvement** | Lessons learned improve future resilience |
| **Audit Compliance** | Documented verification for auditors |
| **Executive Confidence** | Clear sign-off before return to normal |

### Assessment Frequency

| Activity | Frequency | Responsible Party |
|----------|-----------|-------------------|
| Post-Disruption Security Validation | After every disruption | Security Team |
| Security Debt Closure Review | Until all items closed | Security Manager |
| Lessons Learned Review | After every disruption | CISO |
| Verification Procedure Review | Annual | Security Team |

---

## Control Requirements

### ISO 27001:2022 Control A.5.29

> *"The organisation should plan how to maintain information security at an appropriate level during disruption."*

**Implementation Focus**: This assessment addresses the recovery phase, ensuring security is restored to required levels within defined timeframes.

### Key Requirements

**1. Phased Recovery**
- Security validation activities defined for each recovery phase
- Clear criteria for phase completion
- Security team involvement in recovery decisions

**2. Access Deactivation**
- All emergency access disabled
- Credentials rotated
- Audit review of emergency access usage

**3. Control Validation**
- All security controls verified operational
- Configuration baseline confirmed
- Vulnerability assessment completed

**4. Post-Incident Analysis**
- Log review for anomalies during disruption
- Threat actor activity detection
- Security compromise assessment

**5. Lessons Learned**
- Security-focused incident review
- Policy and procedure updates
- Training improvements

### What Auditors Look For

ISO 27001 auditors examining recovery verification will verify:

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Recovery Procedures** | Documented security validation checklists |
| **Access Deactivation** | Evidence emergency access disabled after incidents |
| **Control Restoration** | Verification that all controls operational |
| **Log Analysis** | Post-disruption log review reports |
| **Lessons Learned** | Security review findings and actions taken |
| **Security Debt** | Closure evidence for all deferred items |

---

## Prerequisites

### Before Starting This Assessment

#### Required Access

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| SIEM/Log Platform | Read | Post-disruption log analysis |
| Identity Management System | Admin | Verify emergency access disabled |
| Security Control Dashboards | Read | Verify control status |
| ISMS Evidence Library | Write | Upload verification evidence |
| Vulnerability Scanner | Execute | Post-recovery vulnerability assessment |

#### Required Information

| Information | Source | Why Needed |
|-------------|--------|------------|
| Disruption incident details | Incident Management | Understand what happened |
| Emergency access activation log | ISMS-IMP-A.5.29.2 | Verify deactivation required |
| Security debt register | ISMS-IMP-A.5.29.2 | Track items requiring closure |
| Security control baseline | ISMS-IMP-A.5.29.1 | Validate restoration |
| BC/DR test results | BC Manager | Compare to actual recovery |

#### Prerequisite Checklist

Before proceeding, verify:

- [ ] Disruption incident documented
- [ ] Access to all security monitoring platforms
- [ ] Security control baseline documentation available
- [ ] Emergency access records accessible
- [ ] Security debt register current
- [ ] Incident timeline available

---

## Recovery Phases

### Phase Definitions

| Phase | Timeframe | Focus | Security Objectives |
|-------|-----------|-------|---------------------|
| **Immediate** | 0-24 hours post-disruption | Critical stabilisation | Verify critical controls, disable emergency access, initial log review |
| **Short-term** | 1-7 days | Full control restoration | Complete validation, vulnerability scan, access review |
| **Medium-term** | 1-4 weeks | Security debt resolution | Clear all deferred items, apply patches, full recertification |
| **Long-term** | 1-3 months | Improvement implementation | Lessons learned, policy updates, training updates |

### Phase Transition Criteria

| Transition | Criteria |
|------------|----------|
| **Immediate → Short-term** | Critical systems operational, emergency access disabled, no active incidents |
| **Short-term → Medium-term** | All security controls verified, vulnerability scan complete, no critical findings |
| **Medium-term → Long-term** | Security debt cleared, all deferred patches applied, access recertification complete |
| **Long-term → Normal** | Lessons learned implemented, policies updated, training completed |

### Security Sign-Off Requirements

| Phase Completion | Sign-Off Required |
|------------------|-------------------|
| Immediate Phase | Security Team Lead |
| Short-term Phase | Security Manager |
| Medium-term Phase | CISO |
| Long-term Phase | CISO + Executive Management notification |

---

## Completion Walkthrough

### Step-by-Step Process

#### Step 1: Immediate Phase (0-24 hours)

**Objective**: Stabilise security posture

1. **Verify Critical Controls Operational**
   - Authentication systems functioning
   - Network segmentation intact
   - Logging active on critical systems
   - Data encryption verified

2. **Disable Emergency Access**
   - Identify all break-glass activations during disruption
   - Deactivate each account
   - Rotate credentials
   - Notify CISO

3. **Initial Log Review**
   - Review logs from disruption period
   - Identify anomalies requiring investigation
   - Document findings

4. **Security Team Handover**
   - Brief incoming shift on status
   - Document outstanding actions

#### Step 2: Short-term Phase (1-7 days)

**Objective**: Full security control restoration

1. **Complete Security Control Validation**
   - Walk through all controls from ISMS-IMP-A.5.29.1
   - Verify each control operational
   - Document any gaps

2. **Vulnerability Assessment**
   - Run vulnerability scan on recovered systems
   - Prioritise critical/high findings
   - Create remediation plan

3. **Access Review**
   - Review access changes during disruption
   - Verify no unauthorised access remains
   - Document any access anomalies

4. **Detailed Log Analysis**
   - Complete review of logs from disruption period
   - Correlate with incident timeline
   - Document any suspicious activity

#### Step 3: Medium-term Phase (1-4 weeks)

**Objective**: Security debt resolution

1. **Close Security Debt Items**
   - Review all items in Security_Debt_Register
   - Complete deferred patches
   - Apply deferred configuration changes
   - Conduct postponed access reviews

2. **Full Access Recertification**
   - Verify all access appropriate
   - Remove temporary access
   - Confirm privileged access justified

3. **Control Testing**
   - Test security controls for effectiveness
   - Verify monitoring and alerting
   - Confirm backup procedures

4. **Security Manager Sign-Off**
   - Review all validation activities
   - Confirm security debt cleared
   - Approve transition to Long-term phase

#### Step 4: Long-term Phase (1-3 months)

**Objective**: Continuous improvement

1. **Lessons Learned Review**
   - Conduct security-focused post-incident review
   - Document findings and recommendations
   - Assign improvement actions

2. **Policy and Procedure Updates**
   - Update BC/DR plans with security lessons
   - Revise emergency procedures if needed
   - Update security baselines if required

3. **Training Updates**
   - Incorporate lessons into awareness training
   - Update technical training as needed
   - Brief security team on changes

4. **CISO Sign-Off**
   - Review lessons learned implementation
   - Confirm all updates completed
   - Approve return to normal operations

---

## Security Validation Activities

### Control Validation Checklist

| Control Category | Validation Activities |
|------------------|----------------------|
| **Access Control** | Verify authentication working, MFA operational, privileged access correct |
| **Data Encryption** | Confirm encryption at rest enabled, TLS certificates valid |
| **Logging** | Verify logs flowing to SIEM, log integrity intact |
| **Network Security** | Confirm firewall rules correct, IDS/IPS operational |
| **Endpoint Security** | Verify EDR active, antimalware updated |
| **Backup Protection** | Confirm backups encrypted, access controlled |
| **Physical Security** | Verify access controls operational, CCTV functioning |

### Anomaly Detection Focus Areas

| Area | What to Look For |
|------|------------------|
| **Authentication Logs** | Failed attempts, unusual locations, off-hours access |
| **Privileged Access** | Unusual admin activity, break-glass usage, elevation |
| **Network Traffic** | Unusual destinations, data exfiltration patterns, C2 indicators |
| **File Access** | Mass file access, unusual access patterns, encryption activity |
| **Security Tools** | Disabled controls, configuration changes, agent stops |
| **Email/Comms** | Phishing during disruption, social engineering attempts |

---

## Evidence Collection

### Evidence Requirements

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| **Emergency Access Deactivation** | Records of account disable and rotation | ISMS Evidence Library |
| **Control Validation Checklist** | Completed validation with timestamps | ISMS Evidence Library |
| **Vulnerability Scan Results** | Post-recovery scan report | ISMS Evidence Library |
| **Log Analysis Report** | Anomaly findings from disruption period | ISMS Evidence Library |
| **Security Debt Closure** | Remediation evidence for each item | ISMS Evidence Library |
| **Lessons Learned Report** | Findings and action items | ISMS Evidence Library |
| **Phase Sign-Off Records** | Approval signatures for each phase | ISMS Evidence Library |

---

## Common Pitfalls

Avoid these common mistakes:

| Mistake | Impact | Prevention |
|---------|--------|------------|
| **Rush to declare "normal"** | Unresolved security issues | Enforce phase completion criteria |
| **Emergency access left active** | Standing privileged access | Mandatory deactivation checklist |
| **Skip log review** | Attacks during disruption missed | Required anomaly analysis |
| **Security debt forgotten** | Permanent security gaps | Track to closure |
| **No lessons learned** | Same problems recur | Mandatory post-incident review |
| **Skip vulnerability scan** | Recovery introduces vulnerabilities | Required before medium-term |
| **Access review skipped** | Unauthorised access persists | Mandatory access recertification |
| **Control validation assumed** | Controls may not be restored | Explicit verification required |
| **CISO not informed** | Lack of oversight | Mandatory phase sign-offs |
| **Evidence not collected** | No audit trail | Collect evidence during recovery |

---

## Quality Checklist

Before declaring return to normal operations, verify:

### Immediate Phase Checklist
- [ ] All emergency access accounts deactivated
- [ ] Credentials rotated for activated accounts
- [ ] Critical security controls verified operational
- [ ] Initial log review completed
- [ ] No active security incidents

### Short-term Phase Checklist
- [ ] All security controls validated
- [ ] Vulnerability scan completed
- [ ] Access review completed
- [ ] Detailed log analysis completed
- [ ] Security Manager sign-off obtained

### Medium-term Phase Checklist
- [ ] All security debt items closed
- [ ] Full access recertification completed
- [ ] Deferred patches applied
- [ ] Control testing completed
- [ ] CISO sign-off obtained

### Long-term Phase Checklist
- [ ] Lessons learned review completed
- [ ] Policy/procedure updates implemented
- [ ] Training updates completed
- [ ] BC/DR plans updated with security lessons
- [ ] Final CISO sign-off obtained

---

## Review and Approval

### Approval Workflow

```
Immediate Phase Complete
         │
         ▼
Security Team Lead Sign-Off
         │
         ▼
Short-term Phase Complete
         │
         ▼
Security Manager Sign-Off
         │
         ▼
Medium-term Phase Complete
         │
         ▼
CISO Sign-Off
         │
         ▼
Long-term Phase Complete
         │
         ▼
Final CISO Sign-Off + Executive Notification
         │
         ▼
Return to Normal Operations Declared
```

---

## Integration with Other Controls

### Related ISMS Controls

| Control | Relationship |
|---------|--------------|
| **A.5.24-28** | Incident management provides disruption details |
| **A.8.8** | Vulnerability management for post-recovery scan |
| **A.5.15-18** | Access control for recertification |
| **A.8.15-16** | Logging and monitoring for anomaly detection |
| **A.5.30** | BC/DR plan updates from lessons learned |

### Related ISMS-IMP Documents

| Document | Relationship |
|----------|--------------|
| **ISMS-IMP-A.5.29.1** | Security control baseline for validation |
| **ISMS-IMP-A.5.29.2** | Emergency access records, security debt register |
| **ISMS-IMP-A.5.29.4** | Compliance dashboard for recovery metrics |

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
