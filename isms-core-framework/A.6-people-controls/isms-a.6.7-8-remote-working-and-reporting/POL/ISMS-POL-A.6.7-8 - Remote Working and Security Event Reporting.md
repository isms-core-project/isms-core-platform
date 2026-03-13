<!-- ISMS-CORE:POLICY:ISMS-POL-A.6.7-8:framework:POL:a.6.7-8 -->
**ISMS-POL-A.6.7-8 – Remote Working and Security Event Reporting**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Remote Working and Security Event Reporting |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.6.7-8 |
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
| 1.0 | [Date] | CISO | Initial policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Human Resources Officer (CHRO)
- Technical: IT Director / CTO
- Final Authority: Executive Management

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.6.7-8.-UG/TGS1 through .S5 (Implementation & Assessment Guidance Suite)
- ISO/IEC 27001:2022 Controls A.6.7, A.6.8
- ISO/IEC 27002:2022 Sections 6.7, 6.8 (Implementation Guidance)
- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles)
- ISMS-POL-A.6.3 (Awareness and Training)
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle)
- ISMS-POL-A.8.1-7-18-19 (Endpoint Security)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for remote working security and information security event reporting in accordance with ISO/IEC 27001:2022 Controls A.6.7 and A.6.8.

**Scope**: This policy applies to all personnel who work remotely or outside [Organisation]'s premises, all devices used for remote work (corporate and personal), all information accessed or processed remotely, and all personnel responsible for reporting security events regardless of work location.

**Purpose**: Define organisational requirements for secure remote working and timely security event reporting. This policy establishes WHAT security measures are required for remote work, WHO may work remotely and under what conditions, WHAT constitutes a reportable security event, and WHO is responsible for reporting and responding. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.6.7-8 (UG/TG variants).S1 through .S5.

**Combined Control Framework**: These two controls are implemented as a unified framework because:

1. **Remote workers are the front line of event detection** - Personnel working remotely are often the first to observe security anomalies affecting their devices, connections, or data access
2. **Unique remote work threats require specialized reporting** - Remote workers face threats not present in office environments (unsecured networks, physical access by others, public space risks)
3. **ISO 27002:2022 explicitly links them** - Remote working guidance requires incident reporting procedures to be accessible from remote locations
4. **Same personnel population** - Both controls address the same people and their security responsibilities; combined training is more effective

**Statement of Applicability Independence**: Although implemented as a unified framework, A.6.7 and A.6.8 are assessed independently in the Statement of Applicability. Each control retains distinct requirements, evidence collection, and compliance scoring for audit purposes.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG (data protection), EU GDPR (where applicable), ISO/IEC 27001:2022, and industry-specific requirements where applicable.

**Why This Matters**: Remote work has become standard practice, expanding the organisational attack surface beyond traditional perimeter defenses. Industry research indicates that remote workers face 3x higher phishing exposure, and the average time to detect a breach increases significantly when personnel work outside monitored networks. This framework addresses these risks through systematic security requirements and robust event reporting mechanisms.

---

# Control Alignment & Scope

## ISO/IEC 27001:2022 Control A.6.7 - Remote Working

**ISO/IEC 27001:2022 Annex A.6.7 - Remote Working**

> *Security measures shall be implemented when personnel are working remotely to protect information accessed, processed, or stored outside the organisation's premises.*

**Control Objective**: Ensure that remote personnel have the necessary security controls in place to safeguard the confidentiality, integrity, and availability of organisational information, procedures, and systems from unauthorised access or disclosure when working outside [Organisation]'s premises.

**Control Type**: Preventive
**Control Category**: People Control
**Security Properties**: Confidentiality, Integrity, Availability

**ISO/IEC 27002:2022 Guidance Summary**:

- Remote working policy defines conditions and restrictions
- Physical security of remote working site addressed
- Risk of unauthorised access from persons sharing the space
- Secure communication channels required
- Multi-factor authentication for remote access
- Encryption of data in transit and at rest
- Hardware and software support provisions
- Backup and business continuity procedures
- Audit and security monitoring capabilities
- Revocation of access and equipment return upon termination

## ISO/IEC 27001:2022 Control A.6.8 - Information Security Event Reporting

**ISO/IEC 27001:2022 Annex A.6.8 - Information Security Event Reporting**

> *The organisation shall provide a mechanism for personnel to report observed or suspected information security events through appropriate channels in a timely manner.*

**Control Objective**: Support timely, consistent, and effective reporting of information security events that can be identified by personnel, ensuring that events are documented accurately to support incident response activities and other security management responsibilities.

**Control Type**: Detective
**Control Category**: People Control
**Security Properties**: Confidentiality, Integrity, Availability

**ISO/IEC 27002:2022 Guidance Summary**:

- Simple, accessible, and well-publicized reporting channels
- Multiple reporting options available
- Clear definition of reportable events with examples
- Include reporting in security awareness training
- Non-punitive reporting environment
- System alterations not processed via change control (NEW in 2022)
- Suspected malware infection (NEW in 2022)
- Personnel SHALL NOT attempt to verify vulnerabilities themselves

## Combined Control Framework Rationale

[Organisation] implements these two controls as a unified framework because they represent complementary aspects of personnel security responsibilities:

**Operational Integration**:

- Remote work security (A.6.7) creates the protective environment
- Event reporting (A.6.8) enables detection when protection fails
- Remote workers need accessible reporting channels from any location
- Event categories include remote-specific scenarios (VPN issues, device theft, suspicious network activity)

**Implementation Synergy**:

- Shared training modules covering both remote security and event reporting
- Combined policy acknowledgment during onboarding
- Unified evidence collection (training records, acknowledgments, awareness materials)
- Single governance framework with consistent review cycles

**Why Separate Implementation Would Be Less Effective**:

- Remote workers without event reporting knowledge create detection gaps
- Event reporting channels inaccessible from remote locations delay response
- Fragmented training increases burden and reduces retention
- Separate policies create confusion about responsibilities

## What This Policy Does

This policy:

- **Defines** requirements for secure remote working arrangements
- **Establishes** authorisation requirements for remote work
- **Specifies** physical security requirements for remote work environments
- **Mandates** technical security controls for remote access
- **Defines** data handling requirements when working remotely
- **Establishes** security event reporting mechanisms and channels
- **Specifies** what constitutes a reportable security event
- **Mandates** timely reporting and non-blame culture
- **Assigns** accountability for remote work governance and event response
- **References** applicable regulatory requirements per ISMS-POL-00
- **Integrates** with related controls (endpoint security, incident management, access control)

## What This Policy Does NOT Do

This policy does NOT:

- **Specify technical VPN configuration procedures** (see ISMS-IMP-A.6.7-8.S2)
- **Define step-by-step MFA setup instructions** (vendor-specific, see IT procedures)
- **Provide remote work approval forms** (see Annex templates)
- **Detail incident response procedures** (see ISMS-POL-A.5.24-28)
- **Specify endpoint hardening procedures** (see ISMS-POL-A.8.1-7-18-19)
- **Define HR remote work policies** (eligibility, scheduling - HR domain)
- **Replace local employment law obligations** (complements existing HR framework)
- **Specify event triage procedures** (see ISMS-IMP-A.6.7-8.S4)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite evolving remote work technologies
- Technical flexibility for platform and tool updates
- Clear distinction between governance (policy) and execution (implementation)
- Organisation-agnostic approach applicable to any ISMS implementation

## Scope

**This policy applies to**:

**Personnel**:

- All employees working remotely (full-time, part-time, occasional)
- All contractors and consultants working from non-[Organisation] premises
- All third-party personnel with remote access to [Organisation]'s systems
- All personnel traveling for business who access organisational resources
- All personnel who may observe or report security events

**Remote Work Arrangements**:

- Work from home (regular or occasional)
- Work from co-working spaces or shared offices
- Work from client or partner premises
- Work while traveling (hotels, airports, public spaces)
- Any work performed outside [Organisation]'s controlled premises

**Devices and Equipment**:

- Corporate-issued laptops, tablets, and mobile devices
- Personal devices used for work (BYOD) where permitted
- Portable storage media containing organisational data
- Communication devices used for organisational purposes

**Information and Systems**:

- All organisational data accessed remotely
- All organisational systems accessed via remote connections
- All communications containing organisational information
- All documents and materials processed outside [Organisation]'s premises

**Out of Scope**:

- On-premises work performed at [Organisation]'s controlled facilities
- Personal activities on personal devices without organisational data
- HR aspects of remote work (eligibility, work-life balance, scheduling)
- Compensation and expense policies (separate HR domain)

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG** | All Swiss operations | Art. 8 - Appropriate technical and organisational measures for data protection in remote environments |
| **EU GDPR** | When processing EU personal data | Art. 32 - Security of processing must extend to remote work; Art. 33 - Breach notification within 72 hours requires timely event detection |
| **ISO/IEC 27001:2022** | Certification scope | Controls A.6.7 (Remote Working), A.6.8 (Event Reporting) |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Remote Work / Reporting Requirements |
|-----------|-------------------|--------------------------------------|
| **NIS2 Directive** | Essential/important entity (EU) | Art. 21 - Cybersecurity practices including remote access security; Art. 23 - Incident notification within 24 hours |
| **DORA** | EU financial services entity | Art. 9 - ICT security requirements extend to remote access; Art. 19 - Incident reporting to competent authorities |
| **FINMA Circular 2008/21** | Swiss regulated financial institution | Remote access controls, incident reporting to FINMA |
| **PCI DSS v4.0.1** | Processing payment card data | Req. 12.3.1 - Remote access security; Req. 12.10 - Incident response |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- NIST SP 800-46 Rev 2 - Guide to Enterprise Telework, Remote Access, and BYOD Security
- NIST SP 800-61 Rev 2 - Computer Security Incident Handling Guide
- CIS Controls v8.1 - Control 4 (Secure Configuration), Control 17 (Incident Response)
- ENISA - Teleworking Security Guidelines

**Compliance Determination**: [Organisation] determines applicable Tier 2 regulations through periodic business activity assessment per ISMS-POL-00. The most stringent requirements apply where multiple regulations overlap.

---

# Remote Working Requirements (Control A.6.7)

## Remote Work Authorisation

[Organisation] SHALL establish a formal authorisation process for remote working arrangements.

**2.1.1 Authorisation Requirements**

| Requirement | Description |
|-------------|-------------|
| **Formal Approval** | All regular remote work arrangements SHALL be formally approved before commencement |
| **Authorisation Authority** | Line managers authorise remote work; IT Security approves technical access |
| **Risk Assessment** | Risk assessment SHALL be performed for roles handling sensitive data remotely |
| **Risk Assessment Criteria** | Assessment SHALL evaluate at minimum: (a) Classification level of data accessed remotely (per A.5.12); (b) Physical security capability of remote location; (c) Network security posture; (d) Device security baseline compliance; (e) Regulatory or contractual restrictions |
| **Risk Assessment Verification** | Assessment adequacy is verified through documented criteria aligned with organisational risk methodology (per A.5.7). Detailed assessment procedures in ISMS-IMP-A.6.7-8.S1 |
| **Documented Agreement** | Remote workers SHALL acknowledge remote work security requirements |
| **Periodic Review** | Remote work authorisations SHALL be reviewed at least annually |

**2.1.2 Authorisation Criteria**

Remote work authorisation SHALL consider:

- Role suitability for remote work
- Data classification of information to be accessed
- Technical capability to establish secure remote connections
- Physical environment suitability (privacy, security)
- Regulatory or contractual restrictions
- Business continuity requirements

**2.1.3 Revocation**

Remote work authorisation SHALL be revoked when:

- Employment or contract terminates
- Role changes to one unsuitable for remote work
- Security requirements are not maintained
- Policy violations occur
- Business needs require on-premises presence

## Physical Security Requirements

[Organisation] SHALL define physical security requirements for remote work environments.

**2.2.1 Workspace Requirements**

Remote workers SHALL:

- Position screens to prevent unauthorised viewing by others
- Use privacy screens when working in shared or public spaces
- Secure work equipment when workspace is unattended
- Prevent access to work devices by family members, visitors, or other unauthorised persons
- Store sensitive documents securely when not in active use
- Dispose of sensitive documents using approved methods (shredding)

**Verification**: Physical security compliance is verified through annual self-assessment checklist completion, triggered reassessment following security events or significant workspace changes, or attestation during authorisation renewal.

**2.2.2 Equipment Security**

Remote workers SHALL:

- Physically secure portable equipment (cable locks, secure storage)
- Never leave devices unattended in public spaces
- Lock devices when stepping away, even briefly
- Report lost or stolen devices immediately (see Section 3)
- Transport devices securely between locations

**2.2.3 Clear Desk Requirements**

The clear desk policy (per A.7.7) SHALL extend to remote work environments:

- Sensitive documents SHALL NOT be left visible when not actively in use
- Work materials SHALL be secured at the end of each work session
- Printed materials SHALL be stored securely or disposed of appropriately

## Technical Security Requirements

[Organisation] SHALL mandate technical security controls for all remote access.

**2.3.1 Secure Connection Requirements**

| Requirement | Mandatory For |
|-------------|---------------|
| **VPN or Zero Trust Access** | All connections to internal resources |
| **Multi-Factor Authentication** | All remote access to organisational systems |
| **Encrypted Communications** | All data transmission (TLS 1.2+ minimum) |
| **Corporate DNS** | Resolution through organisational DNS when connected |

**2.3.2 Authentication Requirements**

Remote access authentication SHALL require:

- Multi-factor authentication (MFA) for all system access
- Strong passwords per organisational password policy (A.5.17)
- No credential sharing or storage in insecure locations
- Immediate password change if compromise is suspected
- Session timeout after period of inactivity

**2.3.3 Network Security Requirements**

Remote workers SHALL:

- Use only secure, encrypted wireless networks (WPA2/WPA3 minimum)
- Avoid public, unsecured Wi-Fi for organisational work without VPN protection
- Not disable or circumvent security controls
- Report network security concerns or anomalies

**Verification**: Network security compliance may be monitored through endpoint management telemetry (network SSID, encryption type, VPN connection status, certificate validity), VPN connection enforcement, or user attestation during periodic reviews. Where telemetry is not technically feasible, user attestation during authorisation renewal provides reasonable assurance.

## Data Handling Requirements

[Organisation] SHALL define data handling requirements for remote work contexts.

**2.4.1 Data Classification Compliance**

Remote workers SHALL:

- Handle data according to its classification level (per A.5.12-13)
- Not process Restricted data remotely unless specifically authorised
- Apply appropriate protection for Confidential data
- Follow secure information transfer procedures (per A.5.14)

**2.4.2 Data Storage Requirements**

| Data Classification | Remote Storage Permitted | Conditions |
|--------------------|-------------------------|------------|
| **Public** | Yes | Standard device security |
| **Internal** | Yes | Encrypted device, secure location |
| **Confidential** | Conditional | Encrypted, approved devices only, business justification |
| **Restricted** | No (default) | Requires explicit CISO approval, enhanced controls |

**Conditional Authorisation Process**: Confidential data remote storage requires: (a) Written business justification from Line Manager; (b) Technical controls verification (device encryption, secure storage location); (c) Approval by IT Security Manager. Restricted data requires written CISO approval with documented compensating controls. All approvals SHALL be logged in the exception register (Section 5.4).

**2.4.3 Data Backup**

Remote workers SHALL:

- Store work files in approved cloud or network locations
- Not rely solely on local device storage for critical data
- Follow organisational backup policies

## Device and Equipment Security

[Organisation] SHALL define security requirements for devices used in remote work.

**2.5.1 Corporate Device Requirements**

Corporate-issued devices used for remote work SHALL:

- Be configured per organisational security baseline (per A.8.9)
- Have full-disk encryption enabled
- Have current endpoint protection software (per A.8.7)
- Be patched and updated per organisational schedule (per A.8.8)
- Have remote wipe capability enabled
- Be registered in device inventory (per A.5.9)

**2.5.2 Personal Device (BYOD) Requirements**

Where personal devices are permitted for organisational work, they SHALL:

- Meet minimum security requirements defined by IT Security
- Have organisational MDM/EMM solution installed (if required)
- Maintain separation between personal and work data (containerization)
- Be subject to remote wipe of organisational data upon termination
- Not store organisational data after access is revoked

**2.5.3 Prohibited Devices**

The following SHALL NOT be used for organisational work:

- Jailbroken or rooted devices
- Devices with disabled security features
- Shared devices not under user's control
- Devices that cannot meet security requirements
- Devices running end-of-life operating systems without security updates
- Devices owned or controlled by third parties not subject to organisational security policies

## Remote Work Termination

[Organisation] SHALL define requirements for terminating remote work arrangements.

**2.6.1 Access Revocation**

Upon termination of remote work authorisation:

- Remote access credentials SHALL be revoked immediately
- VPN and remote access tokens SHALL be disabled
- Access to remote-accessible systems SHALL be reviewed and removed

**2.6.2 Equipment Return**

Upon termination of employment or contract:

- All organisational equipment SHALL be returned per A.5.11
- All organisational data SHALL be removed from personal devices
- Return SHALL be verified and documented

---

# Security Event Reporting Requirements (Control A.6.8)

## Reporting Mechanisms

[Organisation] SHALL provide accessible mechanisms for reporting security events.

**3.1.1 Reporting Channel Requirements**

| Requirement | Description |
|-------------|-------------|
| **Multiple Channels** | At least two distinct reporting channels SHALL be available |
| **24/7 Availability** | At least one channel SHALL be available outside business hours |
| **Remote Accessibility** | All channels SHALL be accessible from remote locations |
| **Clear Contact Information** | Reporting contacts SHALL be prominently published |
| **Acknowledgment** | All reports SHALL be acknowledged within defined timeframes |

**Verification**: Channel availability is verified through quarterly testing of reporting channels (email, phone, ticketing), annual incident response exercises verifying channel accessibility, or continuous automated monitoring where technically feasible.

**3.1.2 Standard Reporting Channels**

[Organisation] SHALL maintain the following reporting channels:

- **Security Email**: Dedicated email address for security event reports
- **Phone/Hotline**: Contact number for urgent security matters
- **Ticketing System**: Formal ticket submission for non-urgent events
- **Anonymous Option**: Mechanism for anonymous reporting where appropriate

**Anonymous Reporting**: Anonymous reporting SHALL be supported through: (a) Dedicated email alias not requiring authentication; (b) Web form accessible without login; or (c) Third-party hotline if implemented. **Limitations**: Anonymous reporting may preclude follow-up questions and detailed feedback. Reporters are encouraged to provide contact information where comfortable, with assurance of confidentiality per Section 3.4.1.

**3.1.3 Channel Accessibility**

Reporting channels SHALL be:

- Published on the intranet and included in security awareness materials
- Included in employee onboarding materials
- Displayed in common areas and on login screens
- Accessible without requiring system access (for reporting access issues)

## Reportable Events

[Organisation] SHALL define what constitutes a reportable security event.

**3.2.1 Event vs. Incident Distinction**

| Term | Definition |
|------|------------|
| **Security Event** | An identified occurrence indicating a *possible* breach of policy or failure of controls |
| **Security Incident** | An event that has been assessed as having a *significant probability* of compromising operations or threatening security |

**Personnel report EVENTS. The Security Team assesses whether events constitute INCIDENTS.**

**3.2.2 Categories of Reportable Events**

Personnel SHALL report the following event categories:

**Phishing and Social Engineering**:

- Suspicious emails requesting credentials or sensitive information
- Suspicious phone calls or text messages
- Attempted manipulation to bypass security controls

**Malware and System Compromise**:

- Unexpected system behavior or performance issues
- Suspicious pop-ups, messages, or notifications
- Suspected malware infection (NEW in ISO 27002:2022)
- Ransomware indicators

**Unauthorised Access**:

- Unknown or unexpected login attempts to your accounts
- Unfamiliar devices logged into your accounts
- Unexpected account lockouts or password changes
- Suspicious privilege changes

**Data Breach and Leakage**:

- Misdirected emails containing sensitive information
- Unauthorised data access or exposure
- Lost or stolen documents containing organisational data
- Suspected data exfiltration

**Physical Security**:

- Lost or stolen devices (laptops, phones, USB drives)
- Tailgating or unauthorised physical access
- Missing equipment
- Suspicious persons in secure areas

**Policy Violations**:

- Observed circumvention of security controls
- Known security policy violations by others
- System alterations not processed via change control (NEW in ISO 27002:2022)

**Remote Work Specific**:

- Suspected compromise of home network
- Unauthorised access to work device by others
- VPN or remote access issues suggesting attack
- Suspicious activity while working from public locations
- Attempts to access organisational systems from unapproved devices
- Suspicious IT support requests for remote access credentials
- Home router configuration changes not initiated by user
- Physical observation of work materials by unauthorised persons

## Reporting Procedures

[Organisation] SHALL define clear reporting procedures.

**3.3.1 What to Report**

Reports SHALL include (where known):

- Date and time of observation
- Description of the event
- Systems or assets potentially affected
- Actions already taken (if any)
- Contact information for follow-up (unless anonymous)
- Any supporting evidence (screenshots, email headers)

**3.3.2 Reporting Timeliness**

| Event Severity | Reporting Timeframe |
|----------------|---------------------|
| **Critical** (active attack, data breach, ransomware) | Immediately |
| **High** (lost device, credential compromise) | Within 1 hour |
| **Medium** (phishing attempt, suspicious activity) | Within 4 hours |
| **Low** (policy concern, general observation) | Within 24 hours |

**Severity Determination**: Reporters SHALL report based on their best judgment of severity. When uncertain between severity levels, report at the higher severity level to ensure timely response. The IT Security Team will reassess severity during initial triage. Reporters SHALL NOT delay reporting to determine precise classification.

**3.3.3 Reporter Responsibilities**

Personnel reporting events SHALL:

- Report promptly per the timeframes above
- Provide accurate information to the best of their knowledge
- Preserve potential evidence: for phishing emails, forward as attachment to preserve headers (do not forward in body or click links); for system anomalies, screenshot error messages and note exact time and affected systems; for physical security events, photograph if safe to do so. Never compromise personal safety to gather evidence
- NOT attempt to investigate or verify the event themselves
- NOT attempt to test or exploit suspected vulnerabilities
- Cooperate with any follow-up investigation

## Non-Blame Culture

[Organisation] SHALL foster a non-punitive environment for security event reporting.

**3.4.1 Non-Blame Principles**

| Principle | Commitment |
|-----------|------------|
| **Good Faith Protection** | Personnel who report events in good faith SHALL NOT face negative consequences for the act of reporting |
| **Honest Mistake Handling** | Honest mistakes reported promptly SHALL be handled constructively, focusing on learning and improvement |
| **No Retaliation** | Retaliation against good-faith reporters is prohibited and subject to disciplinary action |
| **Confidentiality** | Reporter identity SHALL be protected to the extent possible |

**3.4.2 Encouraging Reporting**

[Organisation] SHALL:

- Recognize personnel who demonstrate exemplary reporting behavior
- Use reported events as learning opportunities, not punishment triggers
- Communicate the value of reporting through awareness programs
- Provide feedback on reported events to demonstrate action is taken

**Verification**: Non-blame culture effectiveness may be assessed through reporting volume trends (declining volumes may indicate fear of consequences and trigger culture review), anonymous personnel surveys on reporting comfort, or analysis of time-to-report metrics. Peer organisation benchmarking or industry averages may inform adequacy assessment.

**3.4.3 Exceptions**

Non-blame principles do NOT protect:

- Deliberate policy violations reported only after discovery
- Malicious activity disguised as accidental
- Repeated negligence after training and warnings
- False reports made in bad faith

## Response and Feedback

[Organisation] SHALL respond to security event reports.

**3.5.1 Response Timeframes**

| Response Type | Timeframe |
|---------------|-----------|
| **Acknowledgment** | Within 4 business hours |
| **Initial Assessment** | Within 24 hours |
| **Status Update to Reporter** | Within 72 hours |
| **Closure Notification** | Upon resolution |

**Verification**: Response timeframe compliance is measured through ticketing system metrics, reporting dashboards, or periodic compliance audits.

**3.5.2 Feedback to Reporters**

[Organisation] SHALL:

- Acknowledge receipt of all reports
- Provide status updates on reported events
- Communicate outcomes where appropriate and permitted
- Use lessons learned to improve the reporting process
- Thank reporters for their contribution to organisational security

**3.5.3 Escalation**

Events SHALL be escalated per ISMS-POL-A.5.24-28 (Incident Management Lifecycle) when:

- Event is assessed as a confirmed security incident
- Event requires resources beyond initial response team
- Event has regulatory notification implications
- Event affects multiple systems or business units

---

# Roles and Responsibilities

## Responsibility Matrix

| Role | Remote Work (A.6.7) | Event Reporting (A.6.8) |
|------|---------------------|------------------------|
| **Executive Management** | Approve remote work policy; Provide resources | Champion non-blame culture; Receive critical incident briefings |
| **CISO** | Define security requirements; Authorise exceptions; Review compliance | Define reporting mechanisms; Oversee response; Report to management |
| **IT Security Team** | Implement technical controls; Monitor compliance; Assess risks | Receive reports; Assess events; Coordinate response; Provide feedback |
| **IT Operations** | Provision remote access; Maintain VPN/MFA; Support devices | Support reporting channels; Implement containment actions |
| **HR** | Manage remote work agreements; Coordinate terminations | Include reporting in onboarding; Address personnel-related incidents |
| **Line Managers** | Authorise remote work; Ensure team compliance | Encourage reporting; Escalate team concerns |
| **All Personnel** | Comply with remote work requirements; Secure devices and data | Report events promptly; Preserve evidence; Cooperate with investigations |

## Key Role Definitions

**4.2.1 CISO (Chief Information Security Officer)**

Responsibilities:

- Overall accountability for remote work security policy
- Approve high-risk remote work arrangements
- Define event reporting mechanisms and procedures
- Ensure reporting channels are accessible and effective
- Report significant events to Executive Management
- Review and improve remote work and reporting programs

**4.2.2 IT Security Team**

Responsibilities:

- Implement and maintain remote access security controls
- Monitor remote access for anomalies
- Receive and assess security event reports
- Coordinate incident response per A.5.24-28
- Provide feedback to reporters
- Maintain security event documentation
- Conduct periodic reviews of remote work security

**4.2.3 Line Managers**

Responsibilities:

- Authorise remote work for team members
- Ensure team members understand remote work requirements
- Foster a culture of security awareness and reporting
- Escalate security concerns to IT Security
- Address non-compliance within their teams
- Support investigations when required

**4.2.4 All Personnel**

Responsibilities:

- Obtain authorisation before working remotely
- Comply with all remote work security requirements
- Maintain physical and technical security of work environment
- Report security events promptly through designated channels
- Preserve evidence and cooperate with investigations
- Complete required security awareness training
- Acknowledge and adhere to this policy

---

# Governance and Compliance

## Policy Review

| Aspect | Requirement |
|--------|-------------|
| **Review Frequency** | Annual, or upon significant change |
| **Review Authority** | CISO with Executive Management approval |
| **Triggered Reviews** | Major security incident, regulatory change, technology change, organisational restructuring |
| **Review Scope** | Policy effectiveness, compliance metrics, incident trends, regulatory alignment |

## Compliance Monitoring

[Organisation] SHALL monitor compliance with this policy through:

**Remote Work Compliance**:

- Periodic review of remote work authorisations
- Technical compliance checks (VPN usage, MFA status, device encryption)
- Security baseline assessments for remote devices
- Audit of remote access logs

**Event Reporting Compliance**:

- Tracking of reporting channel availability
- Analysis of event reporting metrics
- Review of response timeframes
- Assessment of reporter feedback

## Non-Compliance

**5.3.1 Non-Compliance Consequences**

Violations of this policy may result in:

- Revocation of remote work privileges
- Mandatory additional security training
- Disciplinary action per HR policies
- Termination of employment or contract for serious violations
- Legal action where criminal activity is involved

**5.3.2 Non-Compliance Reporting**

Observed non-compliance SHALL be reported to:

- Line Manager (for team member issues)
- IT Security (for technical violations)
- HR (for personnel matters)
- CISO (for significant or repeated violations)

## Exception Management

**5.4.1 Exception Process**

Exceptions to this policy require:

- Documented business justification
- Risk assessment of the exception
- Compensating controls where applicable
- Approval by CISO (or delegate)
- Time-limited duration with review date
- Documentation in exception register

**5.4.2 Exception Authority**

| Exception Type | Approval Authority |
|----------------|-------------------|
| Standard exceptions (minor deviations) | IT Security Manager |
| High-risk exceptions (sensitive data, extended duration) | CISO |
| Policy waivers (fundamental requirements) | Executive Management |

---

# Integration with Other Controls

## ISMS Integration

This policy integrates with [Organisation]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Remote work risks assessed as part of organisational risk assessment
- Event reporting effectiveness evaluated in risk treatment
- Risk treatment plans document control implementation

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Controls A.6.7 and A.6.8 applicability justified in [Organisation]'s SoA
- Implementation status tracked and reported separately for each control

## Related Controls

| Control | Relationship |
|---------|--------------|
| **A.5.1-2-6.1-2** (Secure Employment & Roles) | Personnel responsibilities, screening, employment terms |
| **A.5.10** (Acceptable Use) | Defines acceptable use of assets including remote work scenarios |
| **A.5.11** (Return of Assets) | Equipment return upon remote work termination |
| **A.5.17** (Authentication Information) | Password and authentication requirements |
| **A.5.24-28** (Incident Management) | Escalation path for security events becoming incidents |
| **A.6.3** (Awareness & Training) | Training on remote work security and event reporting |
| **A.7.7** (Clear Desk) | Clear desk requirements extend to remote environments |
| **A.8.1-7-18-19** (Endpoint Security) | Device security, malware protection for remote devices |
| **A.8.5** (Secure Authentication) | MFA and authentication requirements |
| **A.8.20-22** (Network Security) | VPN and network security for remote connections |

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.6.7-8 Suite):

- ISMS-IMP-A.6.7-8.S1: Remote Work Authorisation & Policy Assessment
- ISMS-IMP-A.6.7-8.S2: Technical Controls Assessment (VPN, MFA, Encryption)
- ISMS-IMP-A.6.7-8.S3: Endpoint & Physical Security Assessment
- ISMS-IMP-A.6.7-8.S4: Event Reporting Mechanisms Assessment

**Assessment Tools**:

- Excel-based assessment workbooks with automated compliance calculations
- Evidence registers for audit documentation
- Gap analysis templates for remediation planning
- Remediation tracking for improvement actions

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:

- ✅ This policy document (ISMS-POL-A.6.7-8 v1.0)
- ✅ Approval signatures from CISO, HR Director, Executive Management
- ✅ Remote work authorisation procedure documented
- ✅ Reporting channel documentation published
- ✅ Training materials for remote work and event reporting
- ✅ Exception register with documented approvals
- ✅ Roles and responsibilities assigned

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Remote work authorisation samples (approved arrangements)
- Policy acknowledgment records from personnel
- Training completion records for remote work/reporting training
- Technical compliance reports (VPN usage, MFA enrollment, device encryption status)
- Sample security event reports demonstrating mechanism use
- Response records showing timely response to reported events
- Compliance metrics dashboard showing policy compliance levels

**Evidence Retention:**

- Policy versions: Life of ISMS + 3 years
- Authorisation records: Duration of arrangement + 2 years
- Training records: Duration of employment + 2 years
- Event reports: 3 years minimum (or per regulatory requirement)
- Compliance assessments: 3 years minimum

---

# Annex A: Supporting Documentation Requirements

This policy requires the following supporting documentation to be developed and maintained by [Organisation]. These are operational documents owned by the respective process owners, not part of the core ISMS policy framework.

## A.1 Remote Work Documentation

| Document Type | Purpose | Owner |
|---------------|---------|-------|
| **Remote Work Authorisation Form** | Formal request and approval for remote work arrangements | HR |
| **Remote Work Security Acknowledgment** | Personnel acknowledgment of security requirements | HR/IT Security |
| **Remote Work Agreement** | Terms and conditions for remote work arrangements | HR/Legal |
| **Home Office Security Self-Assessment** | Checklist for personnel to assess workspace security | IT Security |

## A.2 Event Reporting Documentation

| Document Type | Purpose | Owner |
|---------------|---------|-------|
| **Security Event Report Form** | Standardized form for reporting security events | IT Security |
| **Event Classification Guide** | Guidance on event categories and severity levels | IT Security |
| **Reporting Channel Quick Reference** | Contact information and reporting procedures | IT Security |
| **Event Response Acknowledgment** | Template for acknowledging received reports | IT Security |

## A.3 Reference Materials

Optional reference templates and examples may be provided in:

- ISMS-REF-A.6.7-8 (Reference Materials - if created)
- Organisational intranet or document management system
- HR onboarding materials

**Note**: The specific format and content of operational forms and templates are determined by [Organisation] based on its operational requirements, technology platforms, and organisational culture. This policy defines WHAT documentation is required, not the specific format.

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Human Resources Director** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for remote working and information security event reporting. Implementation procedures, assessment templates, and detailed guidance are documented in ISMS-IMP-A.6.7-8 (UG/TG).*

<!-- QA_VERIFIED: 2026-03-01 -->
