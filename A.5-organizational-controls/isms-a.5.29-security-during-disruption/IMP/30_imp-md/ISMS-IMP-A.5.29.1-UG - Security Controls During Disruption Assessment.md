**ISMS-IMP-A.5.29.1-UG - Security Controls During Disruption Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.29

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.29.1-UG |
| **Title** | Security Controls During Disruption Assessment |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.29.1-TG.

---

## Assessment Overview

### Purpose

This workbook enables systematic assessment and documentation of security controls that must be maintained during disruptive events. It serves as the authoritative registry for:

- **Security Control Inventory**: Complete catalogue of security controls and their disruption requirements
- **Minimum Security Baseline**: Non-negotiable controls that must be maintained regardless of operational status
- **Tiered Security Posture**: Defined security levels aligned with disruption severity
- **Compensating Controls**: Alternative measures when primary controls are unavailable
- **BC/DR Security Integration**: Security requirements embedded in continuity plans
- **Compliance Evidence**: Audit-ready documentation demonstrating Control A.5.29 compliance

The Security Controls During Disruption Assessment is foundational to ensuring that information security is not compromised during adverse situations. Without systematic planning, organisations risk security degradation during the very moments when they are most vulnerable to attack.

### Critical Principle — "Security Cannot Take a Holiday"

Disruptions create opportunities for threat actors. When organisations focus on recovery, adversaries exploit reduced vigilance. This assessment ensures security controls remain effective throughout all phases of disruption and recovery, preventing "security debt" accumulation that exposes the organisation to increased risk.

### Scope

This assessment covers the following components:

**In Scope:**
- All security controls relevant to information processing facilities
- Minimum security baseline definition and enforcement
- Security posture levels (Normal, Elevated, Degraded, Emergency, Recovery)
- Transition authority and approval requirements
- Compensating control identification
- BC/DR plan security review status
- Recovery site security requirements
- Integration with incident management during disruption

**Out of Scope:**
- Business continuity planning scope and methodology (covered in A.5.30)
- Redundancy of processing facilities architecture (covered in A.8.14)
- Incident response procedures for security events (covered in A.5.24-28)
- Backup procedures and data protection (covered in A.8.13)
- Degraded mode requirements (covered in ISMS-IMP-A.5.29.2)
- Recovery verification (covered in ISMS-IMP-A.5.29.3)

### Business Value

A well-maintained security control inventory during disruption delivers:

| Value Area | Benefit |
|------------|---------|
| **Risk Reduction** | Prevents security compromises during vulnerable periods |
| **Regulatory Compliance** | Demonstrates GDPR Article 32, NIS2, DORA security continuity |
| **Audit Readiness** | Clear evidence of security planning for disruption scenarios |
| **Incident Response** | Faster, more effective response with pre-planned security measures |
| **Operational Resilience** | Security integrated into business continuity |
| **Executive Confidence** | Clear visibility into security posture during crises |

### Assessment Frequency

| Activity | Frequency | Responsible Party |
|----------|-----------|-------------------|
| Security Control Inventory Review | Annual | CISO |
| BC/DR Plan Security Review | Annual + after updates | CISO |
| Security Posture Level Review | Annual | Security Team |
| Compensating Controls Review | Annual | Security Team |
| Full Assessment | Annual | CISO |

---

## Control Requirements

### ISO 27001:2022 Control A.5.29

> *"The organisation should plan how to maintain information security at an appropriate level during disruption."*

**Control Type:** Preventive, Detective, Corrective
**Security Properties:** Confidentiality, Integrity, Availability
**Cybersecurity Concepts:** Protect, Detect, Respond
**Operational Capabilities:** Continuity, Operations Security

### Implementation Requirements

Control A.5.29 requires organisations to establish a systematic approach to maintaining information security during disruption. The key requirements are:

**1. Planning**
- Security controls must be planned for disruption scenarios
- Minimum security baseline must be defined
- Compensating controls must be identified
- Security requirements must be integrated into BC/DR plans

**2. Management Structure**
- Adequate management structure to prepare for, mitigate, and respond to disruptive events
- Personnel with authority, experience, and competence to manage security during incidents
- Clear transition authority for security posture changes

**3. Documentation**
- Documented plans for maintaining security during disruption
- Response and recovery procedures with security embedded
- Compensating control documentation

**4. Testing**
- Security controls validated through BC/DR testing
- Compensating controls tested for effectiveness
- Security personnel availability verified

### What Auditors Look For

ISO 27001 auditors examining Control A.5.29 will verify:

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Security Planning** | Documented security requirements for disruption scenarios |
| **BC/DR Integration** | Security sections in all BC/DR plans, CISO approval |
| **Minimum Baseline** | Non-negotiable security controls defined and justified |
| **Compensating Controls** | Alternative measures documented for each degradable control |
| **Testing** | Security scenarios in BC/DR tests, results documented |
| **Recovery Site Security** | Recovery environments meet security requirements |
| **Transition Authority** | Clear approval chain for security posture changes |

### Common Audit Questions

Auditors frequently ask:

1. *"What security controls are maintained during a disaster recovery scenario?"*
2. *"Show me the CISO's approval of security sections in your BC/DR plans."*
3. *"What compensating controls are used when MFA is unavailable?"*
4. *"How do you ensure security is not bypassed during emergency recovery?"*
5. *"What is your minimum security baseline that cannot be degraded?"*
6. *"How is security validated after recovery from disruption?"*

---

## Prerequisites

### Before Starting This Assessment

Complete the following prerequisites to ensure successful assessment completion:

#### Required Access

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| BC/DR Plans Repository | Read | Review security sections in continuity plans |
| Security Control Register | Read/Write | Document control disruption requirements |
| ISMS Evidence Library | Write | Upload evidence and completed workbook |
| Risk Register | Read | Understand security risks during disruption |
| IT Service Catalogue | Read | Identify services requiring security controls |

#### Required Information

| Information | Source | Why Needed |
|-------------|--------|------------|
| BC/DR Plan Inventory | BC Manager | Identify plans requiring security review |
| Security Control Register | Security Team | Baseline of controls to assess |
| Recovery Site Documentation | IT Operations | Verify recovery environment security |
| Incident History | Security Team | Understand past disruption security issues |
| Regulatory Requirements | Legal/Compliance | Identify mandatory security continuity |

#### Required Approvals

| Approval | Approver | When Needed |
|----------|----------|-------------|
| Access to BC/DR Plans | BC Manager | Before starting |
| Assessment Scope | CISO | Before starting |
| Minimum Baseline Definition | Executive Management | During assessment |
| Security Posture Levels | CISO + CIO | During assessment |

#### Prerequisite Checklist

Before proceeding, verify:

- [ ] Access to BC/DR plans confirmed
- [ ] Security control register available
- [ ] Recovery site documentation accessible
- [ ] Previous disruption incidents reviewed
- [ ] Regulatory requirements understood
- [ ] Assessment scope approved by CISO
- [ ] BC Manager engaged for coordination

---

## Disruption Categories

### Understanding Disruption Types

Disruptions affecting information security vary in nature, severity, and required response. The table below provides guidance on disruption categorisation:

#### Disruption Type Definitions

| Category | Description | Security Impact |
|----------|-------------|-----------------|
| **Natural Disasters** | Floods, earthquakes, storms, fire | Physical infrastructure unavailable, DR activation |
| **Infrastructure Failures** | Power outage, network failure, data centre issues | Systems unavailable, potential data integrity risk |
| **Cyber Incidents** | Ransomware, DDoS, data breach, APT | Active threat requiring containment and response |
| **Pandemics** | Extended remote work, reduced staffing | Access control changes, endpoint security criticality |
| **Supply Chain Disruptions** | Vendor failures, cloud outages | Third-party dependency exposure |
| **Civil Unrest** | Protests, strikes, access restrictions | Physical access limitations, personnel safety |
| **Key Personnel Unavailability** | Mass absence, key-person dependency | Knowledge gaps, authorisation delays |

#### Security Impact Matrix

| Disruption Type | Confidentiality Impact | Integrity Impact | Availability Impact |
|-----------------|----------------------|------------------|---------------------|
| Natural Disasters | Medium | Medium | Critical |
| Infrastructure Failures | Low | Medium | Critical |
| Cyber Incidents | Critical | Critical | High |
| Pandemics | Medium | Low | Medium |
| Supply Chain | Medium | Low | High |
| Civil Unrest | Low | Low | Medium |
| Personnel Unavailability | Low | Medium | Medium |

---

## Completion Walkthrough

### Step-by-Step Process

#### Step 1: Review Instructions (30 minutes)
1. Read the Instructions sheet completely
2. Understand the workbook structure and data flow
3. Identify required stakeholders for input
4. Confirm access to prerequisite information

#### Step 2: Complete Security Control Inventory (4-8 hours)
1. List all security controls relevant to information processing
2. For each control, assess:
   - Normal operation status
   - Whether control is mandatory (minimum baseline)
   - Degradation acceptability
   - Recovery priority
3. Reference ISMS-POL-A.5.29 for control classifications
4. Validate with Security Team members

#### Step 3: Define Minimum Baseline (2-4 hours)
1. Review Security Control Inventory
2. Identify non-negotiable controls that must always be maintained
3. Document rationale for each baseline control
4. Obtain CISO approval for baseline definition
5. Document "Never Acceptable" actions

#### Step 4: Document Security Posture Levels (2-4 hours)
1. Define each security posture level:
   - Normal (full controls)
   - Elevated (enhanced monitoring)
   - Degraded (core controls only)
   - Emergency (minimum baseline)
   - Recovery (gradual restoration)
2. Document transition criteria
3. Define transition authority for each level change
4. Obtain CISO and Executive Management approval

#### Step 5: Identify Compensating Controls (4-8 hours)
1. For each degradable control, identify compensating measures
2. Document when compensating control applies
3. Define effectiveness criteria
4. Validate with technical teams
5. Test compensating control feasibility

#### Step 6: Review BC/DR Plans (4-8 hours)
1. Obtain list of all BC/DR plans
2. For each plan, review security sections
3. Document CISO review status and date
4. Identify gaps requiring remediation
5. Track security section approval

#### Step 7: Complete Evidence Register (2-4 hours)
1. Link evidence for each assessment element
2. Document evidence storage locations
3. Verify evidence accessibility
4. Confirm evidence validity dates

#### Step 8: Obtain Approvals (1-2 hours)
1. Complete Assessment Completed By section
2. Route for Security Manager review
3. Obtain CISO approval
4. Document approval decisions and dates

---

## Security Control Classification

### Control Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Access Control** | Authentication and authorisation | MFA, RBAC, privileged access |
| **Data Encryption** | Protection of data confidentiality | TLS, disk encryption, key management |
| **Logging** | Audit trail and monitoring | SIEM, security logs, event correlation |
| **Network Security** | Network protection mechanisms | Firewalls, IDS/IPS, segmentation |
| **Backup Protection** | Backup security measures | Encrypted backups, offsite storage |
| **Endpoint Security** | Device protection | EDR, antimalware, patching |
| **Physical Security** | Physical access controls | CCTV, access badges, secure areas |

### Control Disruption Classification

| Classification | Definition | During Disruption |
|----------------|------------|-------------------|
| **Non-Negotiable** | Must be maintained at all times | No degradation permitted |
| **Degradable with Approval** | Can be reduced with compensating controls | Requires CISO approval |
| **Deferrable** | Can be postponed temporarily | Must be restored within defined timeframe |
| **Not Applicable** | Not relevant during disruption | Document rationale |

---

## Evidence Collection

### Evidence Requirements

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| **BC/DR Plan Security Sections** | Approved security sections in continuity plans | ISMS Evidence Library |
| **CISO Approval Records** | Signed approvals for BC/DR security reviews | ISMS Evidence Library |
| **Minimum Baseline Documentation** | Approved baseline with rationale | ISMS Evidence Library |
| **Compensating Control Tests** | Test results validating alternatives | ISMS Evidence Library |
| **Security Posture Level Approvals** | Executive approval for posture definitions | ISMS Evidence Library |
| **BC/DR Test Security Scenarios** | Security-specific test plans and results | ISMS Evidence Library |

### Evidence Collection Timeline

| Phase | Evidence to Collect |
|-------|---------------------|
| **During Assessment** | Existing BC/DR plans, security control documentation |
| **During Review** | Approval signatures, test results |
| **Post-Assessment** | Updated plans, remediation evidence |

---

## Common Pitfalls

Avoid these common mistakes when completing this assessment:

❌ **MISTAKE: Treating BC/DR as separate from security**
- **Impact**: Security gaps in recovery procedures leave organisation vulnerable during disruption
- **Prevention**: Integrate CISO review into BC/DR lifecycle; make security approval mandatory before plan publication

❌ **MISTAKE: Not defining minimum baseline before disruption occurs**
- **Impact**: Arbitrary security decisions during crisis lead to inconsistent protection and audit findings
- **Prevention**: Pre-approve non-negotiable controls with executive sign-off during calm periods

❌ **MISTAKE: Missing compensating controls for degradable security measures**
- **Impact**: No alternatives when primary controls fail; security gaps during recovery
- **Prevention**: Document compensating control for each degradable control; validate technical feasibility

❌ **MISTAKE: Security as afterthought in BC/DR planning**
- **Impact**: Plans that bypass security controls create vulnerabilities precisely when most needed
- **Prevention**: Require CISO sign-off before any BC/DR plan approval; embed security review in plan template

❌ **MISTAKE: Not testing security scenarios during BC/DR exercises**
- **Impact**: Untested assumptions fail in real disruption; security controls may not function as expected
- **Prevention**: Include specific security scenarios in all BC/DR tests; measure security posture during drills

❌ **MISTAKE: Unclear transition authority for security posture changes**
- **Impact**: Confusion about who can authorise degradation; delays or inappropriate security decisions
- **Prevention**: Document approval chain for each posture level; provide offline contact details

❌ **MISTAKE: Ignoring recovery site security requirements**
- **Impact**: DR environment less secure than production; attackers target recovery infrastructure
- **Prevention**: Apply same security standards to recovery sites; include in regular security assessments

❌ **MISTAKE: Not updating security controls after incidents**
- **Impact**: Lessons not incorporated; same issues recur in future disruptions
- **Prevention**: Conduct mandatory security review after every disruption; track lessons learned actions

❌ **MISTAKE: Assuming compensating controls work without validation**
- **Impact**: Untested alternatives fail when needed; false sense of security
- **Prevention**: Test compensating controls annually; document test results and remediate failures

❌ **MISTAKE: Missing regulatory requirements in security planning**
- **Impact**: Non-compliance penalties; audit failures; reputational damage
- **Prevention**: Map GDPR, NIS2, DORA, Swiss nDSG requirements to controls; verify coverage

❌ **MISTAKE: Focusing only on IT security controls**
- **Impact**: Physical security, personnel security, and operational security overlooked
- **Prevention**: Include all control categories in inventory; coordinate with facilities and HR

❌ **MISTAKE: Failing to document "Never Acceptable" security bypasses**
- **Impact**: Pressure during crisis leads to inappropriate security relaxations
- **Prevention**: Explicitly document what can never be compromised regardless of situation

❌ **MISTAKE: Single point of approval for security decisions**
- **Impact**: Key person unavailability blocks critical decisions during disruption
- **Prevention**: Define succession for all approval authorities; test delegation procedures

❌ **MISTAKE: Not considering supply chain security during disruption**
- **Impact**: Third-party access controls relaxed inappropriately; vendor risks increase
- **Prevention**: Include vendor access in security control inventory; define vendor-specific procedures

❌ **MISTAKE: Inconsistent security control documentation across BC/DR plans**
- **Impact**: Different plans have different security requirements; gaps and confusion
- **Prevention**: Use standardised security section template; CISO reviews all plans against standard

❌ **MISTAKE: Not validating that security tools function during degraded operations**
- **Impact**: SIEM, EDR, or other security tools may not work during infrastructure disruption
- **Prevention**: Include security tool availability in BC/DR testing; document manual alternatives

---

## Quality Checklist

Before submitting this assessment, verify:

### Completeness Checks

- [ ] All security controls inventoried with disruption requirements
- [ ] Minimum baseline defined with rationale for each control
- [ ] All security posture levels documented with transition criteria
- [ ] Compensating controls identified for all degradable controls
- [ ] All BC/DR plans reviewed for security with CISO approval
- [ ] Recovery site security requirements documented
- [ ] Evidence linked for all assessment elements
- [ ] "Never Acceptable" actions documented for minimum baseline
- [ ] Transition authority chain documented for all posture levels
- [ ] Recovery priority assigned to each security control

### Accuracy Checks

- [ ] Security control classifications align with ISMS-POL-A.5.29
- [ ] Transition authority matches organisational structure
- [ ] Compensating controls are technically feasible
- [ ] BC/DR plan list is complete (no plans missing review)
- [ ] Evidence references are valid and accessible
- [ ] Control owners verified and current
- [ ] Last review dates within acceptable period (not >365 days)
- [ ] Regulatory mapping complete for applicable controls

### Validation Checks

- [ ] Compensating controls tested and results documented
- [ ] Recovery site security assessment completed
- [ ] Security scenarios included in latest BC/DR test
- [ ] Security personnel availability verified
- [ ] Break-glass procedures referenced correctly

### Approval Checks

- [ ] CISO approved minimum baseline
- [ ] Executive Management approved posture levels
- [ ] Security Manager reviewed assessment
- [ ] All BC/DR plans have current CISO security approval
- [ ] Approval signatures captured with dates
- [ ] Assessment version controlled and archived

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
Executive Management Informed
         │
         ▼
Assessment Published to ISMS Evidence Library
```

### Approval Criteria

| Reviewer | Approval Criteria |
|----------|-------------------|
| **Security Manager** | Technical accuracy, completeness, evidence quality |
| **CISO** | Strategic alignment, risk acceptance, regulatory compliance |

---

## Integration with Other Controls

### Related ISMS Controls

| Control | Relationship to A.5.29.1 |
|---------|--------------------------|
| **A.5.30** | BC/DR planning receives security requirements from this assessment |
| **A.5.24-28** | Incident management during disruption coordinates with security posture |
| **A.8.13** | Backup procedures include security controls from this assessment |
| **A.8.14** | Redundancy sites implement security requirements defined here |
| **A.8.15** | Logging requirements during disruption defined in minimum baseline |
| **A.5.15-18** | Access control during disruption including break-glass procedures |

### Related ISMS-IMP Documents

| Document | Relationship |
|----------|--------------|
| **ISMS-IMP-A.5.29.2** | Degraded Mode Security Requirements (detailed degradation scenarios) |
| **ISMS-IMP-A.5.29.3** | Recovery Security Verification (post-disruption validation) |
| **ISMS-IMP-A.5.29.4** | Compliance Dashboard (metrics and KPIs) |
| **ISMS-IMP-A.5.30-8.13-14** | BC/DR implementation with security integration |

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
