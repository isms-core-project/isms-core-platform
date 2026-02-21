<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.29:framework:POL:a.5.29 -->
**ISMS-POL-A.5.29 — Information Security During Disruption**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Security During Disruption |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.29 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Business Continuity Manager
- Integration: Chief Information Officer (CIO)
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.30-8.13-14 (Business Continuity & Disaster Recovery Framework)
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle)
- ISMS-POL-A.8.14 (Redundancy of Information Processing Facilities)
- ISMS-IMP-A.5.29.1-UG/TG (Security Controls During Disruption Assessment)
- ISMS-IMP-A.5.29.2-UG/TG (Degraded Mode Security Requirements)
- ISMS-IMP-A.5.29.3-UG/TG (Recovery Security Verification)
- ISMS-IMP-A.5.29.4-UG/TG (Compliance Dashboard)
- ISO/IEC 27001:2022 Control A.5.29

---

## Executive Summary

This policy establishes [Organization]'s requirements for maintaining information security controls during disruptive events, ensuring that security is not compromised when normal operations are interrupted.

**Scope**: This policy applies to all disruptive events affecting [Organization]'s ability to operate normally, including natural disasters, infrastructure failures, cyber incidents, pandemics, supply chain disruptions, and civil unrest.

**Purpose**: Define organizational requirements for security during disruption. This policy establishes WHAT security controls must be maintained and WHO is responsible for security during adverse conditions. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.29 (UG/TG variants).

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (DORA, NIS2, FINMA) apply where [Organization]'s business activities trigger applicability.

**Critical Principle - "Security Cannot Take a Holiday"**: Disruptions create opportunities for threat actors. When organisations focus on recovery, adversaries exploit reduced vigilance. This policy ensures security controls remain effective throughout all phases of disruption and recovery.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Control A.5.29**

**ISO/IEC 27001:2022 Annex A.5.29 - Information Security During Disruption**

[Organisation] maintains defined security controls during disruptions through established baselines, tiered posture levels, and pre-planned recovery procedures that prevent security compromise during adverse conditions.

**Control Objectives**:

- Ensure information security controls remain effective during disruptive events
- Integrate security requirements into business continuity and disaster recovery planning
- Prevent security compromise in the interest of expediency during recovery operations
- Maintain compliance with regulatory obligations during disruption

**Control Type**: Preventive, Detective, Corrective
**Control Category**: Organisational

**This Policy Addresses**:

- Minimum security baseline during disruption
- Tiered security posture levels
- BC/DR plan security requirements
- Emergency access procedures
- Post-disruption security validation

## What This Policy Does

This policy:

- **Defines** minimum security controls that must be maintained during disruption
- **Establishes** tiered security posture levels aligned with disruption severity
- **Specifies** security requirements for BC/DR plans and recovery sites
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Define business continuity planning scope and methodology** (see ISMS-POL-A.5.30-8.13-14)
- **Specify redundancy architecture for processing facilities** (see ISMS-POL-A.8.14)
- **Detail incident response procedures for security events** (see ISMS-POL-A.5.24-28)
- **Provide backup procedures and data protection** (see ISMS-POL-A.8.13)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite operational procedure changes
- Flexibility for different recovery solutions
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- All disruptive events (natural disasters, infrastructure failures, cyber incidents, pandemics)
- All information systems, networks, applications, and data processing facilities
- All business continuity and disaster recovery processes
- All personnel during disruption and recovery phases

**Out of Scope**:

- Business continuity planning methodology (covered by A.5.30)
- Redundancy architecture decisions (covered by A.8.14)
- Security incident response procedures (covered by A.5.24-28)

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG Art. 8** | All personal data processing | Maintain appropriate security measures |
| **EU GDPR Art. 32** | Processing EU personal data | Security of processing including availability |
| **ISO/IEC 27001:2022** | Certification scope | Control A.5.29 - Security during disruption |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Security Requirements |
|-----------|-------------------|----------------------|
| **DORA** | EU financial services entity | Digital operational resilience including ICT incidents |
| **NIS2** | Essential/important entity (EU) | Business continuity including crisis management |
| **FINMA** | Swiss regulated financial institution | Operational resilience requirements (Circular 2023/1) |
| **Healthcare regulations** | Healthcare operations | Continuity of patient data protection |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- ISO 22301 (Business Continuity Management Systems)
- NIST SP 800-34 (Contingency Planning Guide)
- BCI Good Practice Guidelines
- ENISA Guidelines on ICT Service Continuity

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent security requirements apply where multiple regulations overlap. Regulatory obligations and specific timelines are governed by the Regulatory Requirements Register (output of ISMS-POL-00); this policy applies security principles irrespective of regulatory trigger.

---

# Policy Statements

## Security Level Requirements During Disruption

### Minimum Security Baseline

[Organisation] SHALL maintain the following minimum security controls regardless of operational status:

**Control Parameters / Sources of Truth**: For the purposes of this policy:
- **Critical systems**: Systems classified as Tier-1 or Tier-2 in the System Criticality Register derived from the BIA
- **Confidential+**: Information classified as CONFIDENTIAL or RESTRICTED per ISMS-POL-A.5.12-13 (Data Classification Policy)
- **Critical logging**: The minimum log set defined in the Logging Standard (ISMS-IMP-A.8.15), applying to all Tier-1/Tier-2 systems
- **Critical boundaries**: Network segmentation zones protecting Tier-1/Tier-2 systems as defined in the Network Architecture documentation

**Non-Negotiable Controls** (Must be maintained at all times):

| Control Category | Minimum Requirement | Rationale |
|------------------|---------------------|-----------|
| **Access Control** | Authentication required for all system access | Prevents unauthorised access during chaos |
| **Data Encryption** | Encryption at rest for confidential+ data | Data remains protected if media lost |
| **Logging** | Critical system logging continues | Audit trail for post-incident investigation |
| **Network Segmentation** | Critical network boundaries maintained | Prevents lateral movement during recovery |
| **Backup Protection** | Backups remain encrypted and access-controlled | Prevents backup compromise for data theft |

**Degraded Mode Acceptable** (With documented approval and compensating controls):

| Control Category | Acceptable Degradation | Required Compensating Control |
|------------------|----------------------|------------------------------|
| **MFA** | Single-factor if MFA infrastructure unavailable | Enhanced logging, session limits, IP restrictions |
| **Vulnerability Scanning** | Delayed scanning acceptable | Manual review of critical patches only |
| **Security Monitoring** | Reduced scope acceptable | Focus on critical systems, enhanced manual review |
| **Access Reviews** | Postponed reviews acceptable (max 30 days) | Stricter approval for new access requests |
| **Patch Management** | Delayed patching acceptable (max 30 days for non-critical) | Critical/high vulnerabilities still within 72h/7d |

**Mandatory Tracking**: Any approved control degradation SHALL immediately create a time-bound entry in the Security Debt Register or Exception Register (ISMS-REG-EXCEPTIONS), including: owner, compensating controls, start date, closure due date aligned to this policy, and evidence of closure.

**Never Acceptable** (Even during disruption):

- Disabled logging on critical systems
- Removal of authentication requirements
- Decryption of data at rest without re-encryption
- Disabling of network security controls (firewalls, IDS/IPS)
- Sharing of privileged credentials without individual accountability
- Bypassing change management for production systems (unless declared emergency per ISMS-IMP-A.8.32 Emergency Change Procedure, with post-implementation review within 5 business days)

### Tiered Security Posture

[Organisation] SHALL define security posture levels aligned with disruption severity:

| Level | Disruption State | Security Posture | Example |
|-------|-----------------|------------------|---------|
| **Normal** | No disruption | Full security controls operational | Day-to-day operations |
| **Elevated** | Minor disruption | Enhanced monitoring, accelerated patching | Single system failure, minor incident |
| **Degraded** | Moderate disruption | Core controls maintained, non-critical deferred | Data centre failover, regional outage |
| **Emergency** | Severe disruption | Minimum baseline only, survival mode | Multiple site disaster, major cyber attack |
| **Recovery** | Returning to normal | Gradual restoration with security validation | Post-disaster recovery phase |

**Transition Authority**:

| Transition | Authority Required | Documentation |
|------------|-------------------|---------------|
| Normal → Elevated | CISO or Security Team Lead | Incident ticket |
| Elevated → Degraded | CISO + CIO | Formal notification to Executive Management |
| Degraded → Emergency | Executive Management (CEO or delegate) | Emergency declaration document |
| Recovery transitions | CISO approval for each phase | Phase completion checklist |

## Security Planning for BC/DR

### BC/DR Plan Security Requirements

All Business Continuity and Disaster Recovery plans SHALL include:

**Security Considerations in BC/DR Plans**:

1. **Access Control During Recovery**:
   - Who has access to recovery systems and data
   - How access is authenticated when normal systems unavailable
   - How access is revoked when recovery complete
   - Emergency access accounts and their controls

2. **Data Protection During Recovery**:
   - How data is protected during transfer to recovery site
   - Encryption requirements for recovery media
   - Chain of custody for physical data movement
   - Data classification enforcement in recovery environment

3. **Communication Security**:
   - Secure communication channels for crisis team
   - Alternative communication if primary channels compromised
   - Authentication of crisis communications (prevent social engineering)
   - Information sharing boundaries (what can be shared externally)

4. **Third-Party Security**:
   - Vendor access controls during recovery
   - Contractor security requirements during emergency operations
   - Cloud service security during failover
   - Supply chain security for emergency procurement

**BC/DR Plan Security Review**:

- CISO or delegate SHALL review and approve security sections of all BC/DR plans
- Security review SHALL occur before BC/DR plan approval and after each update
- Security-specific BC/DR test scenarios SHALL be included in annual testing
- Security deviations during testing SHALL be documented and addressed

### Recovery Site Security

Recovery sites (hot, warm, cold sites, cloud DR) SHALL maintain:

| Control | Requirement |
|---------|-------------|
| **Physical Security** | Equivalent to primary site for data criticality |
| **Network Security** | Same segmentation, firewall rules, monitoring |
| **Access Control** | Same authentication, authorisation model |
| **Data Protection** | Same encryption, classification controls |
| **Logging** | Equivalent logging capability |
| **Hardening** | Same configuration baselines |

## Emergency Access Procedures

### Break-Glass Access

[Organisation] SHALL maintain emergency access mechanisms for disruption scenarios:

**Break-Glass Account Requirements**:

| Requirement | Specification |
|-------------|---------------|
| **Account Status** | Dormant (disabled) until emergency declared |
| **Activation Authority** | CISO, CIO, or CEO (documented chain of authority) |
| **Authentication** | Strong authentication (stored securely, multiple factors) |
| **Scope** | Pre-defined, limited to recovery-essential systems |
| **Logging** | All actions logged with tamper protection |
| **Duration** | Time-limited (auto-disable after declared emergency ends) |
| **Deactivation** | Formal deactivation with password change/rotation |

**Emergency Access Log**: Each break-glass activation SHALL be recorded in the Emergency Access Log with: approver, activator, systems accessed, start/end time, actions performed, confirmation of log capture, and deactivation verification.

**Break-Glass Activation Process**:

1. Emergency declared by authorised authority
2. Break-glass activation request documented (even verbally, with written follow-up within 4 hours)
3. Activation by designated personnel (minimum two-person rule for critical systems)
4. Notification to CISO and Security Team
5. Enhanced monitoring enabled
6. Time-limited access (default: 24 hours, renewable with re-approval)
7. Post-emergency deactivation and full review

### Personnel Availability

[Organisation] SHALL ensure security personnel availability during disruption:

**Security Team Continuity**:

- Key security roles have designated backups (documented succession plan)
- Contact information for security personnel maintained offline (printed, encrypted USB)
- Geographic distribution of security team where possible
- Cross-training to ensure coverage for critical security functions
- On-call rotation for 24/7 coverage during elevated/degraded/emergency states

## Post-Disruption Security Validation

### Security Posture Recovery

Before returning to normal operations, [Organisation] SHALL validate security posture:

**Security Recovery Checklist**:

| Phase | Validation Activities |
|-------|----------------------|
| **Immediate (0-24h post-disruption)** | Verify critical security controls operational, disable emergency access, review logs for anomalies |
| **Short-term (1-7 days)** | Full security control validation, vulnerability scan, access review, incident analysis |
| **Medium-term (1-4 weeks)** | Security debt remediation, deferred patches applied, full access recertification, control testing |
| **Long-term (1-3 months)** | Lessons learned implementation, BC/DR plan updates, policy updates, training updates |

**Security Debt Tracking**:

- All security relaxations during disruption SHALL be logged in security debt register
- Each debt item SHALL have owner, remediation plan, and target date
- Security debt older than 30 days SHALL be escalated to CISO
- Security debt older than 90 days SHALL be escalated to Executive Management or accepted as permanent risk

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Security During Disruption Responsibilities |
|------|---------------------------------------------|
| **Executive Management** | Approve security posture levels, authorise emergency mode, resource allocation |
| **CISO** | Security requirements for BC/DR, approve security posture transitions, post-disruption validation |
| **Business Continuity Manager** | Integrate security requirements into BC/DR plans, coordinate with CISO |
| **CIO** | IT recovery aligned with security requirements, emergency access authorisation |
| **Security Team** | Monitor security during disruption, activate emergency procedures, validate recovery |
| **Crisis Management Team** | Include security considerations in crisis decisions, communicate with CISO |
| **IT Operations** | Implement security controls in recovery environments, report security issues |
| **All Personnel** | Follow security procedures during disruption, report security concerns |

## Escalation Path

- Security concerns during active disruption: Security Team → CISO → Crisis Management Team
- Security incidents during disruption: Per ISMS-POL-A.5.24-28 with heightened priority
- Security posture transition requests: Requestor → CISO → Executive Management (as needed)

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| BC/DR Plan Security Review | Annual + after updates | CISO | Review report, approval signature |
| Emergency Access Testing | Annual | Security Team | Test results, procedure validation |
| Security Component of BC/DR Tests | With BC/DR tests (annual minimum) | Security Team + BC Manager | Test scenarios, findings, remediation |
| Recovery Site Security Assessment | Annual | Security Team | Configuration review, gap analysis |
| Security Personnel Availability Drill | Semi-annual | CISO | Contact test results, succession validation |

**Governance Metrics**:

- BC/DR plans with CISO security approval (target: 100%)
- Emergency access procedure tests completed (target: 100% annually)
- Security incidents during disruption events (trend tracking)
- Security debt items post-disruption (target: 0 items >90 days)
- Recovery site security assessment findings (target: 0 critical/high findings)

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Major disruption event, BC/DR plan changes, regulatory updates, audit findings
- **Reviewers**: CISO, Business Continuity Manager, CIO, Crisis Management Team
- **Approval**: Executive Management

## Exception Management

**Permitted Exceptions**:

- Security control degradation during active disruption (with documented compensating controls)
- Standing pre-approved relaxations for specific scenarios (risk-assessed and time-limited)
- Post-disruption security debt for documented remediation plans

**Exception Process**:

1. Document business justification and disruption context
2. Risk assessment of security impact
3. CISO approval (or designated backup if CISO unavailable)
4. Compensating controls documented
5. Time-limited approval (duration of disruption + 7 days for recovery)

**Not Permissible**:

- Permanent exceptions to minimum security baseline
- Exceptions eliminating audit trail capability
- Exceptions without compensating controls

All exceptions SHALL be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

## Corrective Action Linkage

Nonconformities related to this policy (e.g., inadequate BC/DR security review, untested emergency access, security debt accumulation, recovery site gaps) SHALL be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Disruption scenarios included in risk assessment
- Security requirements during disruption informed by impact analysis
- Risk treatment plans document security controls for BC/DR

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Control A.5.29 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported

**Related Controls**:

| Control | Relationship |
|---------|--------------|
| **A.5.30** | Business Continuity - BC/DR planning; A.5.29 provides security requirements |
| **A.8.13** | Backup - Data protection during disruption |
| **A.8.14** | Redundancy - Recovery site security requirements |
| **A.5.24-28** | Incident Management - Security incidents during disruption |
| **A.8.15** | Logging - Logging requirements during disruption |
| **A.5.15-16-18** | Access Control - Emergency access, access during disruption |

**Stacked Control Integration**:

A.5.29 (Information Security During Disruption) stacks with related controls:

| Stacked Control | Integration Point | A.5.29 Contribution |
|-----------------|-------------------|---------------------|
| **A.5.30** (Business Continuity) | BC/DR planning | A.5.29 defines security requirements; A.5.30 defines continuity procedures |
| **A.5.24-28** (Incident Management) | Incident response | A.5.29 addresses security during any disruption; A.5.24-28 for security incidents |
| **A.8.14** (Redundancy) | Recovery sites | A.5.29 specifies security requirements for recovery environments |

Assessment of A.5.29 should reference stacked control assessments for complete coverage.

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.5.29 Suite):

| Document ID | Title | Purpose |
|-------------|-------|---------|
| **ISMS-IMP-A.5.29.1-UG/TG** | Security Requirements for BC/DR Plans | BC/DR security integration procedures |
| **ISMS-IMP-A.5.29.2-UG/TG** | Emergency Access Procedures | Break-glass activation and deactivation |
| **ISMS-IMP-A.5.29.3-UG/TG** | Post-Disruption Security Validation Checklist | Recovery validation procedures |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Required Stage 1 evidence includes:

- ✅ This policy document (ISMS-POL-A.5.29 v1.0)
- ✅ Recorded approval by CISO, Business Continuity Manager, CIO, Executive Management
- ✅ Evidence of communication to relevant roles
- ✅ Minimum security baseline defined (Security Level Requirements During Disruption)
- ✅ Tiered security posture levels defined with transition authority (Tiered Security Posture)
- ✅ BC/DR plan security requirements specified (Security Planning for BC/DR)
- ✅ Emergency access procedures defined (Emergency Access Procedures)
- ✅ Post-disruption validation requirements defined (Post-Disruption Security Validation)
- ✅ Roles and responsibilities assigned (Roles and Responsibilities)

Evidence status is tracked in the ISMS Evidence Register.

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- BC/DR plans with CISO security approval signatures
- Emergency access (break-glass) test results and procedure validation
- BC/DR test results showing security-specific scenarios
- Recovery site security assessment reports
- Security personnel availability drill results
- Security posture transition records (if any disruptions occurred)
- Security debt register with remediation tracking
- Post-disruption security review reports (if any disruptions occurred)
- Training records for crisis management team security procedures

---

# Definitions

| Term | Definition |
|------|------------|
| **Disruption** | Any event that interrupts or threatens to interrupt normal business operations |
| **Security Posture Level** | Defined state of security control implementation (Normal, Elevated, Degraded, Emergency, Recovery) |
| **Break-Glass Access** | Emergency privileged access mechanism activated when normal access is unavailable |
| **Security Debt** | Security controls or activities deferred during disruption requiring later remediation |
| **Recovery Site** | Alternative location (physical or cloud) for resuming operations during disruption |
| **Crisis Management Team** | Cross-functional team activated to manage organisational response to major disruptions |
| **Compensating Control** | Alternative security measure implemented when primary control is unavailable |
| **Minimum Security Baseline** | Non-negotiable security controls that must be maintained regardless of operational status |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Business Continuity Manager** | [Name] | [Date to be set] |
| **Chief Information Officer (CIO)** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for maintaining information security during disruption. Implementation procedures are documented in ISMS-IMP-A.5.29 (UG/TG).*

<!-- QA_VERIFIED: 2026-02-04 -->
