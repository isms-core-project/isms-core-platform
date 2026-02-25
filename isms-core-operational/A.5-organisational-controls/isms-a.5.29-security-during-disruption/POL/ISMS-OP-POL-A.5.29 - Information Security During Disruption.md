<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.29:operational:OP-POL:a.5.29 -->
**ISMS-OP-POL-A.5.29 — Information Security During Disruption**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Security During Disruption |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.29 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.5.29 — Information security during disruption
- ISO/IEC 22301 — Business continuity management systems (informational reference)
- NIST SP 800-34 Rev 1 — Contingency Planning Guide for Federal Information Systems (informational reference)
- NIST SP 800-61 Rev 2 — Computer Security Incident Handling Guide (informational reference)

**Related Annex A Controls**:

| Control | Relationship to Information Security During Disruption |
|---------|-------------------------------------------------------|
| A.5.24–28 Incident management lifecycle | Security incidents may trigger or coincide with business disruptions |
| A.5.30 ICT readiness for business continuity | BC/DR planning provides the operational framework; A.5.29 provides the security overlay |
| A.8.13 Information backup | Backup protection is a non-negotiable security control during disruption |
| A.8.14 Redundancy of information processing facilities | Recovery site security must be equivalent to primary site |
| A.5.15–16–18 Identity and access management | Emergency access procedures and access control during disruption |
| A.8.15 Logging | Logging continuity is mandatory even during degraded operations |
| A.8.16 Monitoring activities | Enhanced monitoring required during elevated and degraded states |

**Related Internal Policies**:

- Business Continuity and Disaster Recovery Policy
- Incident Management Policy
- Identity and Access Management Policy
- Logging Policy
- Monitoring Activities Policy (A.8.16)
- Change Management Policy

---

# Information Security During Disruption Policy

## Purpose

This policy establishes requirements for maintaining information security controls during disruptive events. Disruptions — whether natural disasters, infrastructure failures, cyber attacks, pandemics, or supply chain interruptions — create conditions where security controls are most likely to be weakened precisely when threat exposure is highest.

**"Security Cannot Take a Holiday."** When organisations focus on recovery, adversaries exploit reduced vigilance, distracted personnel, and degraded controls. This policy ensures the organisation maintains a defined minimum security posture throughout all phases of disruption and recovery, and validates that full security controls are restored before returning to normal operations.

This policy supports Swiss nFADP (revDSG) Art. 8 by maintaining appropriate technical and organisational security measures during adverse conditions. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 requirements for the ongoing security of processing also apply.

## Scope

This policy applies to:

- All disruptive events affecting the organisation's ability to operate normally, including natural disasters, infrastructure failures, cyber incidents, pandemics, supply chain disruptions, and civil unrest.
- All information systems, networks, applications, and data processing facilities within the ISO 27001 scope.
- All business continuity and disaster recovery processes.
- All personnel — employees, contractors, and third-party users — during disruption and recovery phases.

## Principle

**People's safety shall be our first priority. Always.**

Once the safety and welfare of personnel is assured, information security continuity becomes the immediate priority. The organisation shall plan, implement, and maintain processes to ensure the required level of information security during adverse situations, including compensating controls where standard security measures cannot be maintained.

No recovery action, however urgent, justifies permanently removing core security controls. Where temporary relaxation is necessary, it shall be documented, time-limited, compensated, and tracked to closure.

---

## Definitions

| Term | Definition |
|------|------------|
| **Disruption** | Any event that interrupts or threatens to interrupt normal business operations |
| **Security posture level** | Defined state of security control implementation (Normal, Elevated, Degraded, Emergency, Recovery) |
| **Minimum security baseline** | Non-negotiable security controls that must be maintained regardless of operational status |
| **Break-glass access** | Emergency privileged access mechanism activated when normal access is unavailable |
| **Security debt** | Security controls or activities deferred during disruption that require later remediation |
| **Recovery site** | Alternative location (physical or cloud) for resuming operations during disruption |
| **Compensating control** | Alternative security measure implemented when the primary control is unavailable |
| **Crisis management team** | Cross-functional team activated to manage the organisational response to a major disruption |

---

## Minimum Security Baseline

### Non-Negotiable Controls

The following security controls shall be maintained at all times, regardless of the disruption state. These controls are not subject to relaxation or exception:

| Control Category | Minimum Requirement | Rationale |
|------------------|---------------------|-----------|
| **Access control** | Authentication required for all system access | Prevents unauthorised access during chaotic conditions |
| **Data encryption** | Encryption at rest for confidential and restricted data | Data remains protected if media is lost, stolen, or exposed during recovery |
| **Logging** | Critical system logging continues on all Tier 1 and Tier 2 systems | Maintains audit trail for post-incident investigation and regulatory compliance |
| **Network segmentation** | Critical network boundaries maintained | Prevents lateral movement if an attacker exploits disruption |
| **Backup protection** | Backups remain encrypted and access-controlled | Prevents backup compromise as an alternative route to data theft |

### Degraded Mode Acceptable Controls

The following controls may be temporarily relaxed during disruption, subject to documented approval by the CISO (or designated backup), implementation of compensating controls, and entry into the Security Debt Register:

| Control Category | Acceptable Degradation | Required Compensating Control | Maximum Duration |
|------------------|----------------------|------------------------------|------------------|
| **Multi-factor authentication** | Single-factor if MFA infrastructure unavailable | Enhanced logging, session time limits, IP-based restrictions | Duration of disruption + 7 days |
| **Vulnerability scanning** | Delayed scheduled scanning | Manual review of critical patches; apply critical/high patches within 72h/7d | 30 days |
| **Security monitoring** | Reduced monitoring scope | Focus on Tier 1 and Tier 2 systems; enhanced manual review | Duration of disruption + 14 days |
| **Access reviews** | Postponed periodic reviews | Stricter approval for new access requests during disruption | 30 days |
| **Patch management** | Delayed patching for non-critical vulnerabilities | Critical and high vulnerabilities still patched within 72h/7d | 30 days for non-critical |

**Mandatory tracking**: Any approved control degradation shall immediately create a time-bound entry in the Security Debt Register, including: owner, compensating controls in effect, start date, target closure date, and evidence of closure upon remediation.

### Never Acceptable

The following actions are prohibited even during the most severe disruption. There are no exceptions:

- **Disabled logging** on critical systems — the audit trail must never be broken
- **Removal of authentication requirements** — no anonymous access to any system
- **Decryption of data at rest** without re-encryption — data must remain protected
- **Disabling of firewalls or IDS/IPS** on critical network boundaries
- **Sharing of privileged credentials** without individual accountability — each action must be attributable to a person
- **Bypassing change management** for production systems without following the emergency change procedure (with mandatory post-implementation review within 5 business days)

### Emergency Change Management During Disruption

**Standard rule**: All production changes require change management approval per the Change Management Policy.

**Emergency change exception**: During **Degraded** or **Emergency** security posture, emergency changes may be implemented with abbreviated approval, subject to the following requirements.

**Emergency change criteria** (all must be met):

1. Change is necessary to restore critical business operations or mitigate an active security incident.
2. Delay until standard change approval would cause significant harm.
3. Change is approved verbally by CIO or CISO (or designated backup).
4. Change is logged immediately in [Change Management System / Incident Ticket].

**Emergency change process**:

1. **Verbal approval**: Change requestor contacts CIO/CISO via crisis communication platform or phone; describes change, justification, and rollback plan.
2. **Approval**: CIO or CISO provides verbal approval; approval logged with timestamp and approver name.
3. **Implementation**: Change implemented with enhanced monitoring.
4. **Documentation**: Within 4 hours of implementation — change ticket created in [Change Management System] with details: what changed, why, who approved, rollback plan, actual outcome.
5. **Post-implementation review**: Within 5 business days — change review meeting (CIO, CISO, change implementer, affected system owner). Determine if change should remain, be rolled back, or be refined. Document lessons learned and any policy/procedure updates required.

**Emergency change restrictions**:

- Emergency changes shall not disable security controls from the "Never Acceptable" list (logging, authentication, encryption, firewalls, change management itself).
- Emergency changes bypassing security controls require CISO approval specifically (not just CIO).
- Emergency changes that increase risk (e.g., opening firewall rules, reducing authentication requirements) require compensating controls documented before implementation.

**Cross-reference**: Full emergency change procedure documented in Change Management Policy.

---

## Tiered Security Posture

The organisation shall operate at one of five defined security posture levels. The current posture level determines which controls are fully active, which may be degraded, and what additional measures are required.

### Posture Levels

| Level | Disruption State | Security Posture | Example Triggers |
|-------|-----------------|------------------|------------------|
| **Normal** | No disruption | Full security controls operational | Day-to-day operations |
| **Elevated** | Minor disruption | Enhanced monitoring, accelerated patching | Single system failure, minor security event, weather warning |
| **Degraded** | Moderate disruption | Core controls maintained, non-critical controls deferred per degraded mode table | Data centre failover, regional outage, significant cyber incident |
| **Emergency** | Severe disruption | Minimum baseline only, survival mode | Multi-site disaster, major ransomware attack, pandemic lockdown |
| **Recovery** | Returning to normal | Gradual restoration with security validation at each phase | Post-disaster recovery, system rebuild |

### Transition Authority

Transitions between posture levels shall be formally authorised. Verbal authorisation is permitted in urgent situations, followed by written confirmation within 4 hours.

| Transition | Authority Required | Documentation |
|------------|-------------------|---------------|
| Normal to Elevated | CISO or IT Security Manager | Incident ticket or notification email |
| Elevated to Degraded | CISO + CIO (jointly) | Formal notification to Executive Management |
| Degraded to Emergency | Executive Management (CEO or delegate) | Emergency declaration document |
| Any level to Recovery | CISO | Phase transition record |
| Recovery to Normal | CISO (confirmed by Executive Management) | Phase completion checklist and security validation sign-off |

Each transition shall be recorded with: date/time, authorising person, justification, current state, target state, and any controls affected.

### Security Posture Level Communication

All personnel shall be informed of the current security posture level and associated requirements.

**Communication channels**:

| Channel | Message Format | Audience |
|---------|----------------|----------|
| **Email** | Formal posture level announcement from CISO or CEO | All employees |
| **Intranet banner** | Visible banner at top of intranet homepage: "CURRENT SECURITY POSTURE: [LEVEL] — [Brief description]" | All employees (whenever accessing intranet) |
| **Collaboration platform** (e.g., Slack/Teams) | Pinned message in #general or #security channel | All employees |
| **Crisis management team** | Direct notification via crisis communication platform | Crisis team, security team, management |

**Intranet banner convention**:

| Posture | Banner Colour | Text |
|---------|---------------|------|
| **Normal** | Green | "SECURITY POSTURE: NORMAL — All systems operational" |
| **Elevated** | Yellow | "SECURITY POSTURE: ELEVATED — Minor disruption; enhanced monitoring in effect" |
| **Degraded** | Orange | "SECURITY POSTURE: DEGRADED — Moderate disruption; core controls active; follow updated procedures" |
| **Emergency** | Red | "SECURITY POSTURE: EMERGENCY — Severe disruption; minimum baseline only; await further instructions" |
| **Recovery** | Blue | "SECURITY POSTURE: RECOVERY — Returning to normal; validate security controls before resuming standard operations" |

**Communication timing**:

- Posture level transitions: Immediate communication (within 1 hour of authorisation).
- Status updates during prolonged disruption: Daily (minimum) or more frequently as situation evolves.
- Return to Normal: Formal "all clear" announcement after post-disruption validation sign-off.

Communication delivery shall be verified (email sent, intranet banner live, collaboration platform message posted). Non-receipt triggers escalation to alternative communication methods.

---

## BC/DR Plan Security Requirements

All business continuity and disaster recovery plans shall include security requirements reviewed and approved by the CISO. Security is not an afterthought in continuity planning — it is a design requirement.

### Security Considerations in BC/DR Plans

BC/DR plans shall address the following four areas:

**1. Access Control During Recovery**

- Who has access to recovery systems and data (named roles, not blanket access).
- How access is authenticated when normal identity systems are unavailable.
- How temporary access is revoked when recovery is complete.
- Emergency access account controls (see Break-Glass Access below).

**2. Data Protection During Recovery**

- Encryption requirements for data in transit to the recovery site.
- Encryption requirements for recovery media (physical and digital).
- Chain of custody procedures for physical data movement.
- Data classification enforcement in the recovery environment.

**3. Communication Security**

- Secure communication channels for the crisis management team (see Crisis Communication Platform below).
- Alternative communication channels if primary systems are compromised (e.g., out-of-band phone, pre-arranged messaging groups).
- Authentication of crisis communications to prevent social engineering during confusion.
- Information sharing boundaries — what may be shared externally and who approves external communications.

### Crisis Communication Platform

**Primary platform**: [Specify tool — e.g., Microsoft Teams (with E2EE), Signal, Wickr, encrypted Zoom, WhatsApp Business]

**Configuration**:

- End-to-end encryption enabled (verify E2EE is active).
- Pre-configured crisis management group chat with all authorised personnel.
- Group chat name: **"Crisis Management Team — Secure"**.
- Access restricted to pre-approved personnel (no ad-hoc additions without CISO approval during crisis).

**Backup platform** (if primary is unavailable): [Specify alternative — e.g., encrypted email (PGP/S/MIME), pre-arranged phone bridge, out-of-band SMS group]

**Authentication during crisis**:

- All crisis communication participants shall authenticate using their organisational credentials.
- During Emergency posture, if MFA infrastructure is unavailable, participants shall use pre-shared authentication phrases to verify identity (rotated monthly, distributed via offline contact list).

**Out-of-band verification**: For critical decisions (e.g., authorising Emergency posture, approving break-glass activation), verbal confirmation via phone call required to prevent impersonation attacks. Phone numbers verified and updated quarterly in offline contact list.

**Testing**: Crisis communication platform tested quarterly. Tests include connectivity verification, encryption status check, participant authentication, and message delivery confirmation. Test documentation retained for 3 years.

**4. Third-Party Security**

- Vendor access controls during recovery operations.
- Contractor security requirements during emergency operations.
- Cloud service security verification during failover.
- Supply chain security for emergency procurement.

### BC/DR Plan Security Review

- The CISO or designated backup shall review and approve the security sections of all BC/DR plans before the plans are approved.
- Security review shall occur after each update to a BC/DR plan.
- At least one security-specific test scenario shall be included in annual BC/DR testing.
- Security deviations observed during testing shall be documented and addressed within 30 days.

---

## Recovery Site Security

Recovery sites — whether hot, warm, cold standby, or cloud-based disaster recovery environments — shall maintain security controls equivalent to the primary site. A recovery environment with weaker security than the primary site creates an exploitable gap.

| Control | Requirement |
|---------|-------------|
| **Physical security** | Equivalent to primary site for the data criticality level handled |
| **Network security** | Same segmentation rules, firewall policies, and monitoring |
| **Access control** | Same authentication and authorisation model; no weaker access paths |
| **Data protection** | Same encryption standards (at rest and in transit) and classification enforcement |
| **Logging** | Equivalent logging capability; logs shall feed the same [SIEM] or monitoring system |
| **Hardening** | Same configuration baselines applied to recovery infrastructure |

### Recovery Site Definition and Configuration

**Primary recovery site**: [Specify type and location]

| Option | Description | Configuration |
|--------|-------------|---------------|
| **Cloud disaster recovery** (most common for SMEs) | [e.g., AWS, Azure, Google Cloud] in [e.g., eu-central-1 (Frankfurt), West Europe (Netherlands)] | Hot standby (always available), warm standby (spin-up within X hours), or cold standby (manual deployment). Failover trigger: automatic (health check failure) or manual (declared by CIO + CISO) |
| **Colocation / secondary data centre** | [Facility name, city] | Dedicated WAN link or encrypted VPN to primary site |
| **Work-from-anywhere** (pandemic/office unavailability) | VPN access, MFA, endpoint encryption, secure home network guidance | Administrative/knowledge worker functions only; dependent on cloud/colo for infrastructure recovery |

**Current configuration**: [Specify which option(s) deployed]

**Security equivalence verification**:

| Security Control | Verification Method |
|------------------|---------------------|
| **Physical security** | Annual review of provider audit reports (SOC 2 Type II or ISO 27001); on-site inspection if physical facility |
| **Network segmentation** | Recovery site config compared to primary site baseline |
| **Access control** | Test authentication (including MFA) to recovery systems |
| **Encryption** | Config scan; certificate verification |
| **Logging** | Verify log forwarding to [SIEM] during DR test |
| **Backup protection** | Restore test from recovery site backups |

**Failover testing**: Annual failover test to recovery site. Security validation during test shall confirm authentication works (including MFA), network segmentation is enforced, logging is active and forwarding to [SIEM], encryption is verified, and access controls match primary site. Security findings documented and remediated within 30 days.

Recovery site security shall be verified:

- At initial provisioning, before the site is declared operational.
- Annually, as part of the BC/DR testing programme.
- After any significant change to recovery infrastructure.

---

## Emergency Access Procedures

### Break-Glass Access

The organisation shall maintain pre-configured emergency access accounts ("break-glass accounts") for scenarios where normal authentication or access systems are unavailable.

**Break-Glass Account Requirements**:

| Requirement | Specification |
|-------------|---------------|
| **Account status** | Dormant (disabled) until emergency is declared |
| **Activation authority** | CISO, CIO, or CEO (documented chain of authority with designated backups) |
| **Authentication** | Strong authentication — credentials stored securely per the Break-Glass Credential Storage specification below |
| **Scope** | Pre-defined, limited to recovery-essential systems only |
| **Logging** | All actions logged with tamper-protected audit trail |
| **Duration** | Time-limited — default 24 hours, renewable with re-approval |
| **Deactivation** | Formal deactivation with credential rotation and full activity review |

### Break-Glass Activation Process

1. **Emergency declared** by an authorised authority (see Transition Authority table).
2. **Activation request documented** — even if initially verbal, written record within 4 hours.
3. **Two-person activation** — for critical systems, break-glass requires a minimum of two authorised personnel (dual control).
4. **CISO and Security Team notified** immediately upon activation.
5. **Enhanced monitoring enabled** — all break-glass account activity monitored in real time where possible.
6. **Time limit applied** — 24 hours default; renewal requires explicit re-approval with justification.
7. **Deactivation and review** — upon emergency resolution: disable account, rotate credentials, review all actions performed, document findings.

### Break-Glass Credential Storage and Access

**Storage method**: [Specify organisation's chosen method from below]

**Option 1 — Physical safe** (primary method for high-security environments):

- **Location**: [Building name], [Floor], [Room number] — physically secured room with restricted access.
- **Access authorisation**: CEO, CISO, CIO (each has safe combination or key; two required for access).
- **Contents**: Sealed tamper-evident envelopes containing break-glass account usernames and initial passwords, recovery site VPN credentials, root passwords for critical systems (Tier 0), and encryption recovery keys.
- **Envelope integrity**: Tamper-evident seals; envelope opening triggers mandatory credential rotation.
- **Verification**: Quarterly verification that safe is accessible and envelopes are intact (external inspection only; no opening).

**Option 2 — Password manager emergency vault**:

- **Tool**: [e.g., 1Password Emergency Kit, Bitwarden Emergency Access, LastPass Emergency Access].
- **Configuration**: Emergency vault separate from standard corporate vault.
- **Access**: Emergency access granted to designated personnel (CEO, CISO, CIO) with time-delayed access (e.g., 12-hour wait period before access granted).
- **MFA bypass**: Emergency vault accessible with recovery codes stored offline (printed cards in sealed envelopes, stored per Option 1).
- **Testing**: Quarterly test of emergency access workflow (time-delay verification, access confirmation, credential retrieval).

**Option 3 — Split-knowledge / secret sharing** (advanced):

- **Method**: Shamir's Secret Sharing or similar cryptographic split.
- **Configuration**: Break-glass password split into 3 shares; any 2 of 3 required to reconstruct.
- **Share holders**: CEO (Share 1), CISO (Share 2), CIO (Share 3).
- **Storage**: Each share holder stores their share in a personal safe or sealed envelope (home safe, bank safety deposit box).
- **Testing**: Annual test of reconstruction process.

**Current method**: [Specify which option(s) the organisation uses]

**Backup access** (if primary method fails): If safe is inaccessible (building destroyed) → Password Manager Emergency Vault (cloud-accessible). If Password Manager is inaccessible (service outage) → Physical safe or split-knowledge.

### Break-Glass Testing

Break-glass accounts and procedures shall be tested at least annually to verify:

- Credentials are accessible and functional.
- Activation process is understood by all authorised personnel.
- Logging captures all actions performed.
- Deactivation process works correctly.

Test results shall be documented. Failed tests shall trigger immediate remediation.

---

## Personnel Availability

The organisation shall ensure that personnel with security responsibilities are available during disruption events. Disruptions frequently occur outside business hours and may prevent normal access to the workplace.

**Security team continuity requirements**:

- Key security roles shall have designated backups documented in a succession plan.
- Contact information for security personnel shall be maintained offline — printed contact lists and/or encrypted USB — accessible when email, intranet, and other digital systems are unavailable.
- Where possible, security personnel should be geographically distributed to avoid a single-site failure disabling the entire security team.
- Cross-training shall ensure that at least two individuals can perform each critical security function (break-glass activation, log review, emergency access revocation, security posture assessment).
- On-call rotation shall be established for 24/7 coverage when the organisation operates at Elevated, Degraded, or Emergency posture levels.

### Offline-Accessible Contact List

**Multi-layered approach for resilience**:

**Layer 1 — Printed laminated cards**:

- Wallet-sized laminated cards provided to all crisis management team members and security personnel.
- Contains: Names, mobile phone numbers, personal email addresses (for out-of-band contact), role.
- Updated quarterly; old cards destroyed (shredded). Distribution: Hand-delivered; personnel sign acknowledgment of receipt.

**Layer 2 — Encrypted USB drive**:

- USB drive stored in break-glass safe alongside credentials.
- Contains: Full contact list (all security personnel, extended crisis team, vendor emergency contacts).
- File encrypted (e.g., VeraCrypt, BitLocker To Go) with password known to CEO/CISO/CIO.
- Updated quarterly.

**Layer 3 — Secure cloud storage** (accessible if Internet available):

- Contact list stored in [secure document repository] with access restricted to crisis management team.
- Regularly updated (real-time when personnel changes occur).

**Testing**: Quarterly verification — 3 random personnel contacted using information from laminated cards (verify phone numbers work), USB drive tested (encryption password verified, file opened), cloud storage access verified. Test results documented; failures trigger immediate update.

### Security Team On-Call Coverage

**Activation trigger**: Automatically activated when security posture transitions to **Elevated**, **Degraded**, or **Emergency**.

**Coverage model**:

| Posture | Coverage |
|---------|----------|
| **Normal** | No dedicated on-call (business hours support only) |
| **Elevated** | 16x7 coverage (07:00–23:00 CET, 7 days/week) |
| **Degraded / Emergency** | 24x7 coverage |

**Rotation schedule**:

| Role | Coverage Responsibility |
|------|-------------------------|
| **Primary on-call** | IT Security Analyst or IT Security Manager (rotates weekly) |
| **Backup on-call** | CISO or designated Security Team member |
| **Escalation** | CISO (24x7 reachable during Degraded/Emergency) |

**Response SLAs**:

| Severity | Elevated | Degraded / Emergency |
|----------|----------|----------------------|
| **Critical** (break-glass activation, confirmed breach) | 30 minutes | 15 minutes |
| **High** (security control failure, suspicious activity) | 2 hours | 1 hour |
| **Medium** (non-critical alert, advisory) | 4 hours | 2 hours |

**Escalation path**: Primary on-call → Backup on-call (if primary unreachable after 30 min for Critical, 1 hour for High) → CISO → Executive Management.

**Testing**: Monthly on-call test page during normal business hours (verify contact info and response time). Quarterly after-hours test (random time; verify escalation path works).

---

## Post-Disruption Security Validation

Before returning to Normal posture level, the organisation shall validate that full security controls have been restored. The recovery-to-normal transition is not complete until security validation is signed off by the CISO.

### Four-Phase Validation

| Phase | Timeframe | Validation Activities |
|-------|-----------|----------------------|
| **Immediate** | 0–24 hours post-disruption | Verify non-negotiable controls are operational; disable all break-glass accounts; review logs for anomalies during disruption; confirm no unauthorised access occurred |
| **Short-term** | 1–7 days | Full security control validation; vulnerability scan of all Tier 1 and Tier 2 systems; access review (verify no residual emergency permissions); initial incident analysis |
| **Medium-term** | 1–4 weeks | Security debt remediation (apply deferred patches, restore deferred controls); full access recertification; control testing to verify effectiveness; BC/DR plan update with lessons learned |
| **Long-term** | 1–3 months | Lessons learned implementation; policy and procedure updates; training updates; trend analysis of security posture during disruption |

### Security Debt Tracking

All security relaxations approved during a disruption shall be tracked in the Security Debt Register until fully remediated.

**System**: [Specify tool — e.g., GRC platform (Vanta, Drata, ServiceNow GRC), Jira, Asana, Excel register stored in secure location]

**Ownership**: CISO maintains register; assigned owners remediate individual debt items.

**Security Debt Register format**:

| Field | Description |
|-------|-------------|
| **Debt ID** | Unique identifier (e.g., DEBT-2025-001) |
| **Control relaxed** | Which security control was degraded or deferred |
| **Business justification** | Why was relaxation necessary? (tied to specific disruption event) |
| **Compensating control** | Alternative security measure implemented |
| **Date opened** | When the relaxation was approved |
| **Security posture at opening** | Elevated / Degraded / Emergency |
| **Approver** | CISO or authorised delegate |
| **Owner** | Person responsible for remediation |
| **Target closure date** | When full control must be restored |
| **Current status** | Open / In Progress / Closed |
| **Progress notes** | Updates on remediation actions |
| **Closure date** | When control was fully restored |
| **Closure verification** | CISO or Security Team verification of control restoration |

**Debt lifecycle**:

1. **Opening**: Control relaxation approved during disruption → immediate entry into register.
2. **Tracking**: Weekly review during active disruption; bi-weekly during Recovery posture.
3. **Escalation**: Per thresholds below.
4. **Closure**: Control fully restored → Security Team verifies → Debt marked Closed.

**Integration with security posture**: Recovery → Normal transition requires Security Debt Register to be empty or have documented Executive Management approval for remaining items.

**Reporting**: Security Debt status reported in every ISMS Management Review during and after disruption. Metrics: total open debts, average age, overdue debts, closure rate.

**Escalation thresholds**:

- Security debt older than **30 days** shall be escalated to the CISO with a remediation plan and revised target date.
- Security debt older than **90 days** shall be escalated to Executive Management for a decision: either approve accelerated remediation with additional resources, or formally accept the residual risk with documented risk acceptance.
- Security debt that cannot be remediated shall be converted to a permanent risk entry in the Risk Register with compensating controls and annual review.

---

## Roles and Responsibilities

| Role | Information Security During Disruption Responsibilities |
|------|---------------------------------------------------------|
| **CEO / Executive Management** | Approve security posture levels; authorise Emergency mode; allocate resources for security during recovery; make risk acceptance decisions for security debt exceeding 90 days |
| **CISO** | Policy owner; define security requirements for BC/DR plans; approve security posture transitions; authorise break-glass activation; own post-disruption security validation; escalation point for security debt |
| **BC/DR Coordinator** | Integrate security requirements into BC/DR plans; coordinate with CISO on plan security review; include security scenarios in BC/DR testing |
| **CIO** | Ensure IT recovery aligns with security requirements; co-authorise Elevated-to-Degraded transition; authorise break-glass activation |
| **Security Team / IT Security** | Monitor security during disruption; activate and deactivate emergency procedures; validate recovery site security; conduct post-disruption vulnerability scans and access reviews |
| **Crisis Management Team** | Include security considerations in all crisis decisions; maintain communication with CISO throughout disruption (see composition below) |
| **IT Operations** | Implement security controls in recovery environments; maintain logging during recovery; report security anomalies during recovery |
| **All Personnel** | Follow security procedures during disruption; report security concerns through established channels; do not bypass security controls without authorisation |

### Crisis Management Team Composition

**Purpose**: Coordinate organisational response to major disruptions affecting business operations and information security.

**Activation trigger**: Security posture transition to **Degraded** or **Emergency**; incident severity P0 (Critical) or P1 (High) with business-wide impact; or declaration by CEO, CIO, or CISO that crisis management is required.

**Core team members**:

| Role | Responsibilities During Crisis |
|------|-------------------------------|
| **CEO** (Team Leader) | Overall crisis leadership; external communication; strategic decisions; authorise Emergency posture |
| **CIO** | IT recovery coordination; resource allocation; technology decision authority |
| **CISO** | Information security continuity; security posture management; break-glass authorisation; post-disruption validation |
| **CFO** | Financial impact assessment; budget authorisation for recovery; insurance coordination |
| **HR Director** | Personnel safety; communication to employees; workforce continuity |
| **Legal Counsel** | Regulatory notification; liability management; contract issues; data breach legal obligations |
| **Communications / PR** (if applicable) | External communications; media management; customer notification |

**Extended team** (activated as needed): BC/DR Coordinator, IT Operations Manager, Security Team Lead, Facilities Manager, key vendors.

**Decision authority**:

| Decision Type | Authority |
|---------------|-----------|
| Security posture level transitions | CEO + CIO + CISO agreement required |
| Risk acceptance decisions, external communication, resource allocation beyond budget | CEO final authority |
| Security control relaxations, break-glass activation, security debt approval | CISO final authority |
| Technology recovery priorities, system restoration sequencing | CIO final authority |

**Meeting cadence during crisis**:

| Posture | Frequency |
|---------|-----------|
| **Degraded** | Daily crisis management team call (30 minutes) until recovery begins |
| **Emergency** | Twice-daily (morning and evening) plus ad-hoc as needed |
| **Recovery** | Every 2–3 days until return to Normal |

Meeting minutes documented (even if brief) for post-incident review. Action items tracked with owner and target date.

**Post-crisis**: Formal lessons learned session within 30 days of return to Normal posture. Lessons learned inform policy updates, BC/DR plan updates, and training.

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **BC/DR plans with CISO security approval** (signed review confirming security sections are adequate) | BC/DR Coordinator / CISO | *Annual review; updated after tests and incidents; retained current + 2 prior versions* |
| 2 | **Minimum security baseline documentation** (defining non-negotiable controls and degraded mode thresholds) | CISO | *Annual review; updated upon policy change; retained 3 years* |
| 3 | **Break-glass account inventory** (account list, scope, credential storage location, activation authority) | Security Team | *Maintained continuously; reviewed quarterly; retained 3 years* |
| 4 | **Break-glass test results** (annual test documenting credential accessibility, activation process, logging, deactivation) | Security Team | *Annual minimum; retained 3 years* |
| 5 | **Security posture transition records** (date, authority, justification, controls affected) — if any disruptions occurred | CISO | *Per event; retained 5 years* |
| 6 | **Security Debt Register** (all relaxations during disruption with owner, compensating controls, target date, closure) | CISO | *Per event; reviewed monthly during active debt; retained 3 years* |
| 7 | **Post-disruption security validation reports** (four-phase checklist completion with sign-off) — if any disruptions occurred | CISO / Security Team | *Per disruption event; retained 5 years* |
| 8 | **Recovery site security assessment** (annual verification of security equivalence with primary site) | Security Team | *Annual; retained 3 years* |
| 9 | **Security personnel contact list and succession plan** (offline-accessible, tested quarterly) | CISO | *Reviewed quarterly; updated upon any change* |
| 10 | **BC/DR test records showing security-specific scenarios** (test scope, security findings, remediation actions) | BC/DR Coordinator / Security Team | *Annual minimum; retained 3 years* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, BC/DR plan security reviews, break-glass account testing, security posture transition records, Security Debt Register status, recovery site assessments, internal and external audits, and feedback to the policy owner.

**Governance metrics** (reported to Executive Management at least annually):

| Metric | Target |
|--------|--------|
| BC/DR plans with current CISO security approval | 100% |
| Break-glass account tests completed on schedule | 100% |
| Security incidents during disruption events | Trend tracking (target: decreasing) |
| Security debt items open beyond 90 days | 0 |
| Recovery site security assessments with zero critical/high findings | 100% |

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO in advance, with documented risk acceptance, compensating controls, and a defined review date (maximum duration of disruption + 7 days for recovery exceptions; maximum 12 months for standing exceptions). Exceptions shall be reported to the Management Review Team.

Exceptions are not permitted for non-negotiable controls (access control, data encryption, logging, network segmentation, backup protection). Exceptions that eliminate audit trail capability are not permitted.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider lessons learned from actual disruptions, BC/DR test results, changes to the threat landscape, regulatory updates, audit findings, and emerging best practices for security during adverse conditions.

---

# Areas of the ISO 27001 Standard Addressed

Information Security During Disruption Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | **5.29 Information security during disruption** |
| Clause 7.3 Awareness | 5.30 ICT readiness for business continuity |
| Clause 8.1 Operational planning and control | 5.36 Compliance with policies, rules, and standards |
| | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | 8.13 Information backup |
| | 8.14 Redundancy of information processing facilities |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Maintain appropriate technical and organisational security measures, including during disruption |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 32 — Security of processing, including the ability to ensure ongoing confidentiality, integrity, availability, and resilience of processing systems and services |
| ISO/IEC 27001:2022 | Annex A Control 5.29 — Information security during disruption |
| ISO/IEC 27002:2022 | Section 5.29 — Implementation guidance |
| ISO/IEC 22301 | Business continuity management systems (informational reference) |
| NIST SP 800-34 Rev 1 | Contingency Planning Guide — three-phase approach (notification/activation, recovery, reconstitution) (informational reference) |
| CIS Controls v8 | Control 17 (Incident Response Management), Control 11 (Data Recovery) |
| DORA (conditional) | Art. 11 — ICT business continuity management including security requirements during disruption |
| NIS2 (conditional) | Art. 21 — Business continuity and crisis management measures |
| FINMA (conditional) | Circular 2023/1 — Operational resilience for Swiss regulated financial institutions |

---

<!-- QA_VERIFIED: 2026-02-07 -->
