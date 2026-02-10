<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.6.7-8:operational:OP-POL:a.6.7-8 -->
**ISMS-OP-POL-A.6.7-8 — Remote Working and Security Event Reporting**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Remote Working and Security Event Reporting |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.6.7-8 |
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

- ISO/IEC 27001:2022 Control A.6.7 — Remote working
- ISO/IEC 27001:2022 Control A.6.8 — Information security event reporting
- ISO/IEC 27002:2022 Sections 6.7, 6.8 — Implementation guidance

**Related Annex A Controls**:

| Control | Relationship to Remote Working and Event Reporting |
|---------|-----------------------------------------------------|
| A.5.10 Acceptable use of information and other associated assets | Defines acceptable use of devices and information in remote work contexts |
| A.5.11 Return of assets | Equipment return upon remote work termination or employment end |
| A.5.14 Information transfer | Secure transfer requirements for data sent from remote locations |
| A.5.24-28 Incident management lifecycle | Escalation path when reported events are confirmed as incidents |
| A.6.3 Information security awareness, education, and training | Training on remote work security and event reporting procedures |
| A.8.1 User endpoint devices | Device security baselines for remote and mobile endpoints |
| A.8.5 Secure authentication | MFA and authentication requirements for remote access |

**Related Internal Policies**:

- Access Control Policy
- Endpoint Security Policy
- Incident Management Policy
- Information Classification and Handling Policy
- Information Transfer Policy
- Acceptable Use and Return of Assets Policy

---

# Remote Working and Security Event Reporting Policy

## Purpose

This policy establishes the organisation's requirements for secure remote working and timely reporting of information security events. It defines the security measures required when personnel work outside the organisation's premises, and provides a structured mechanism for all personnel to report observed or suspected security events through appropriate channels.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data) in remote work environments. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

These two controls are combined because remote workers are the front line of event detection, remote workers face threats not present in office environments, and ISO 27002:2022 explicitly requires incident reporting procedures to be accessible from remote locations.

## Scope

All employees and third-party users.

All corporate and personal devices used to access, process, or store organisational information remotely.

All remote work arrangements including work from home, co-working spaces, client premises, and while travelling.

All personnel responsible for reporting security events, regardless of work location.

## Principle

Remote working shall be formally authorised and subject to security controls proportionate to the classification of information accessed. All personnel shall report observed or suspected information security events promptly and through designated channels. The organisation fosters a non-blame culture where good-faith reporting is protected and encouraged.

---

# Part 1 — Remote Working (A.6.7)

## Remote Work Authorisation

All regular remote work arrangements shall be formally approved before commencement.

- **Approval authority**: Line manager authorises the remote work arrangement; IT Security approves the technical access.
- **Risk assessment**: A risk assessment shall be performed for roles that handle Confidential or Restricted data remotely. The assessment shall evaluate at minimum: (a) classification level of data accessed remotely; (b) physical security capability of the remote location; (c) network security posture at the remote site; (d) device security baseline compliance; and (e) any regulatory or contractual restrictions.
- **Documented acknowledgment**: Remote workers shall sign an acknowledgment confirming they understand and accept the security requirements in this policy.
- **Annual review**: All remote work authorisations shall be reviewed at least annually. Reviews shall confirm that the authorisation remains appropriate, security requirements are maintained, and any changes to role, data access, or work location are reflected.

**Location approval**:
- **Standard remote locations** (home office in Switzerland, established remote workspace): Line manager approval sufficient.
- **International remote work** (working from outside Switzerland): Requires CISO approval + HR approval + legal review (tax, employment law, data residency implications).
- **Temporary remote work from high-risk locations** (public co-working spaces, cafes, travel): Requires line manager awareness; Confidential data access from public locations prohibited.

**Location changes**: Permanent changes to remote work location (e.g., move to new home, extended travel) shall be reported to line manager and IT Security within **14 days**.

**Revocation**: Remote work authorisation shall be revoked when employment or contract terminates, the role changes to one unsuitable for remote work, security requirements are not maintained, policy violations occur, or business needs require on-premises presence.

## Mobile Device Registration and Responsibilities

Mobile devices issued or approved for remote work shall be recorded in the asset register and assigned to a named individual.

**Device registration requirements**:

- All mobile devices (corporate and approved BYOD) shall be registered in the asset register with the assigned owner, device type, serial number, and purpose.
- Assigned owners shall receive a copy of this policy and be informed of their responsibilities.
- Devices shall have appropriate encryption, anti-virus/endpoint protection, and access controls installed.

**Assigned owner responsibilities**:

- Ensure operating system and application patches are applied promptly.
- Ensure encryption and endpoint protection remain enabled and current.
- Not leave the device unattended; physically secure the device when not in use.
- Only access organisational information required for their role, in line with the Access Control Policy.
- Not install software or make changes that would breach the organisation's information security policies, regulations, or applicable legislation.
- Not allow others, including family members, to access or use the assigned device.
- Not store personal data or sensitive personal data (per nFADP) on the device unless authorised and recorded in the asset register.
- Return the mobile device when no longer required, when requested, or upon leaving the organisation's employment.

## Remote Wipe and Backup

- **Remote wipe**: All corporate mobile devices shall have remote wipe capability enabled before the device is issued to the user. Automatic lockout shall be enabled (maximum 5 failed authentication attempts).
- **Backup**: Mobile devices are not backed up by default to corporate backup solutions. Users shall store work files in approved cloud or network locations (e.g., SharePoint, OneDrive for Business, approved file server). Critical work data shall not reside solely on local device storage.

## Physical Security

Remote workers shall maintain physical security appropriate to the classification of information being handled:

- **Screen positioning**: Position screens to prevent unauthorised viewing by others in the workspace.
- **Privacy screens**: Use privacy screens when working in shared or public spaces (co-working areas, cafes, public transport).
- **Equipment security**: Secure work equipment when the workspace is unattended. Never leave devices unattended in public spaces. Lock devices when stepping away, even briefly.
- **Clear desk**: The clear desk policy (A.7.7 — see Physical and Environmental Security Policy) extends to remote work environments. Sensitive documents shall not be left visible when not actively in use. Work materials shall be secured at the end of each work session.

  **Remote clear desk requirements**:
  - Documents locked in drawer, filing cabinet, or secure home office when not in use.
  - Screens locked when stepping away (Windows+L, Ctrl+Cmd+Q).
  - No work materials left on kitchen tables, living room areas, or other shared family spaces.
- **Document disposal**: Sensitive documents shall be disposed of using approved methods (shredding). Where a shredder is not available at the remote location, sensitive documents shall be returned to the office for secure disposal.
- **Family and visitor access**: Prevent access to work devices and documents by family members, visitors, or other unauthorised persons.

## Technical Security

The following technical security controls shall apply to all remote access:

- **VPN or Zero Trust**: All connections to internal organisational resources shall use a VPN or equivalent Zero Trust architecture. Split tunnelling may be permitted only where a risk assessment demonstrates acceptable residual risk and all organisational resources are accessed via the encrypted tunnel.

  **Current implementation**: [Specify: e.g., "Cisco AnyConnect VPN", "Palo Alto GlobalProtect", "Zero Trust via Cloudflare Access / Zscaler", or "Selection in progress; interim: VPN required"]

  **VPN/Zero Trust requirements**:
  - Enforce MFA before establishing connection.
  - Enforce device compliance check (encryption, patching, endpoint protection) before access.
  - Terminate sessions after defined inactivity period (per session timeout requirements below).
  - Log all connection attempts (successful and failed).
- **Multi-factor authentication (MFA)**: MFA shall be required for all remote access to organisational systems. This includes VPN connections, cloud services, email, and any system containing Internal, Confidential, or Restricted data.
- **Encryption in transit**: All data transmitted between remote endpoints and organisational systems shall be encrypted using TLS 1.2 as a minimum (TLS 1.3 preferred).
- **Wi-Fi security**: Remote workers shall use only secure, encrypted wireless networks (WPA2 minimum, WPA3 preferred).

  **Public Wi-Fi usage**:
  - **Prohibited without VPN**: Public, unsecured Wi-Fi (airports, hotels, cafes) shall not be used for organisational work without VPN protection.
  - **With VPN**: Public Wi-Fi may be used with active VPN connection for Internal data access only.
  - **Confidential data**: Accessing Confidential data via public Wi-Fi is discouraged even with VPN; use cellular hotspot or trusted network where feasible.
  - **Prohibited activities on public Wi-Fi** (even with VPN): Financial transactions, password changes for critical accounts (use cellular data or trusted network).

  **Home network security**: Remote workers should secure their home networks (change default router password, enable WPA3/WPA2, disable WPS, apply router firmware updates).
- **Session timeout**: Remote access sessions shall be configured to disconnect after a defined period of inactivity (maximum 15 minutes for systems handling Confidential or Restricted data; maximum 30 minutes for other systems).

## Data Handling

Remote workers shall handle data according to its classification level per the Information Classification and Handling Policy:

| Data Classification | Remote Storage Permitted | Conditions |
|--------------------|-------------------------|------------|
| **Public** | Yes | Standard device security |
| **Internal** | Yes | Encrypted device required |
| **Confidential** | Conditional | Encrypted device, approved storage location, line manager approval |
| **Restricted** | No (default) | Requires explicit CISO approval with documented compensating controls |

Remote workers shall follow the Information Transfer Policy when sending or receiving organisational data from remote locations. Organisational data shall not be transferred to personal cloud storage, personal email accounts, or unapproved file sharing services.

## Corporate and BYOD Device Requirements

### Corporate Devices

Corporate-issued devices used for remote work shall:

- Be configured per the organisational security baseline.
- Have full-disk encryption (FDE) enabled.
- Have current endpoint protection software installed and active.
- Be patched and updated per the organisational patching schedule.
- Have remote wipe capability enabled.
- Be registered in the device inventory.

### BYOD (Bring Your Own Device)

It is not the organisation's policy to allow use of personal mobile devices for work by default. Authorisation is required from the information security management team.

**BYOD approval criteria**:
- Business justification (temporary need, role requirement, cost reduction).
- Device meets minimum security requirements (current OS, MDM-compatible, no jailbreak/root).
- Data classification: BYOD permitted only for Internal and Public data; Confidential requires exception approval from CISO.
- User training completed and acknowledgment signed.
- MDM or containerisation solution deployed before access granted.

Where a personal device is authorised:

- The device shall be registered in the asset register.
- The user shall receive training and sign an acknowledgment of responsibility.
- All organisation policies, including this policy and the Access Control Policy, shall apply.
- An MDM (mobile device management) or containerisation solution shall be installed to separate personal and organisational data.
- The organisation retains the right to remotely wipe organisational data from the device upon termination of employment or access, or upon loss or theft.
- No personal data or sensitive personal data (per nFADP) shall be stored on the device outside the managed container.

### Prohibited Devices

The following shall not be used for organisational work:

- Jailbroken or rooted devices.
- Devices with disabled security features.
- Shared devices not under the user's sole control.
- Devices running end-of-life operating systems that no longer receive security updates.
- Devices that cannot meet the minimum security requirements defined by IT Security.

## Remote Work Termination

Upon termination of remote work authorisation or employment:

- Remote access credentials shall be revoked immediately (same day).
- VPN and remote access tokens shall be disabled.
- All organisational equipment shall be returned per the Return of Assets Policy (A.5.11).
- All organisational data shall be removed from personal devices. For BYOD devices, the MDM remote wipe of the organisational container shall be executed.
- Return and data removal shall be verified and documented.

---

# Part 2 — Security Event Reporting (A.6.8)

## Reporting Channels

The organisation shall provide accessible mechanisms for all personnel to report observed or suspected information security events.

**Channel requirements**:

- At least **two distinct reporting channels** shall be available.
- At least **one channel** shall be available outside business hours (24/7).
- All channels shall be accessible from remote locations without requiring access to internal systems (to allow reporting of access-related events).

**Standard reporting channels**:

| Channel | Purpose | Availability |
|---------|---------|--------------|
| **Security email** (e.g., security@[organisation].ch) | Non-urgent events, detailed reports with attachments | 24/7 (monitored during business hours) |
| **Phone / hotline** | Urgent events, active attacks, lost/stolen devices | 24/7 (on-call outside hours) |
| **Ticketing system** | Formal event submission, tracking, follow-up | Business hours |
| **Anonymous option** (web form or third-party hotline) | Reports where the reporter wishes to remain anonymous | 24/7 |

**Anonymous reporting**:
- **Purpose**: Allows reporting of suspected policy violations, insider threats, or sensitive concerns where the reporter fears retaliation.
- **Anonymity preservation**: Anonymous channel operated by third-party provider (if applicable) or via web form with no personally identifiable logging. Reporter identity not tracked or logged.
- **Follow-up limitation**: Since reporter identity is unknown, follow-up is limited. Anonymous reporters are encouraged to check the reporting portal/channel for responses if the system supports two-way anonymous communication.
- **Alternate approach**: Reporters may also report to HR or Legal with confidentiality (not full anonymity) if follow-up is needed.

Anonymous reports receive the same priority and investigation as identified reports.

**Publication**: Reporting channels shall be published on the intranet, included in employee onboarding materials, referenced in annual security awareness training, and displayed on login screens or desktop wallpapers.

## Reportable Events

**Event vs. incident distinction**:

| Term | Definition |
|------|------------|
| **Security event** | An identified occurrence indicating a *possible* breach of security policy or failure of controls |
| **Security incident** | A security event that has been assessed and confirmed as having an actual or potential adverse effect on the confidentiality, integrity, or availability of information |

**Personnel report EVENTS. The IT Security Team assesses whether events constitute INCIDENTS.** When in doubt, report it.

**Categories of reportable events**:

**Phishing and social engineering**:

- Suspicious emails requesting credentials, payment, or sensitive information.
- Suspicious phone calls or text messages impersonating colleagues or suppliers.
- Attempted manipulation to bypass security controls or gain access.

**Malware and system compromise**:

- Unexpected system behaviour, performance degradation, or crashes.
- Suspicious pop-ups, messages, or notifications.
- Suspected malware infection (including ransomware indicators).
- System alterations not processed via change control.

**Unauthorised access**:

- Unknown or unexpected login attempts to accounts.
- Unfamiliar devices logged into accounts.
- Unexpected account lockouts or password changes.
- Suspicious privilege changes or new administrator accounts.

**Data breach and leakage**:

- Misdirected emails containing sensitive or personal data.
- Unauthorised data access, exposure, or downloading.
- Lost or stolen documents or media containing organisational data.
- Suspected data exfiltration.

**Physical security**:

- Lost or stolen devices (laptops, phones, USB drives, access cards).
- Tailgating or unauthorised physical access to secure areas.
- Missing or damaged equipment.

**Policy violations**:

- Observed circumvention of security controls.
- Known security policy violations by others.
- Unapproved software installations or configuration changes.

**Remote work specific**:

- Suspected compromise of home network or router.
- Unauthorised access to work device by family members or others.
- VPN or remote access failures suggesting an attack or compromise.
- Suspicious activity while working from public locations.
- Device theft or loss while travelling or at a remote site.
- Suspicious IT support requests asking for remote access credentials.
- Home router configuration changes not initiated by the user.
- Physical observation of work materials by unauthorised persons.

### Lost or Stolen Device Procedure

If a device containing organisational data is lost or stolen:

1. **Report immediately** via phone/hotline (Critical severity — report immediately).
2. **Provide details**: Device type, serial number (if known), last known location, approximate time lost/stolen, data classification of data on device.
3. **IT Security actions**:
   - Initiate remote wipe (if device is powered on and connected).
   - Revoke VPN and remote access credentials.
   - Monitor for suspicious account activity.
   - Document incident for investigation.
4. **User actions**:
   - Change passwords for accounts accessed from the lost device (as directed by IT Security).
   - File police report (if stolen) and provide report number to IT Security.
   - Do not attempt to recover the device yourself (personal safety priority).
5. **Insurance / Replacement**: Contact HR for device replacement process.

**Evidence preservation**: If the device is later recovered, do not power it on or attempt to use it. Return it to IT Security for forensic analysis.

## Reporting Procedures

**What to include in a report** (where known):

- Date and time the event was observed or discovered.
- Description of what happened.
- Systems, applications, or data potentially affected.
- Actions already taken (if any).
- Contact information for follow-up (unless reporting anonymously).
- Any supporting evidence (screenshots, email headers, error messages).

**Reporting timeliness**:

| Event Severity | Examples | Reporting Timeframe |
|----------------|----------|---------------------|
| **Critical** | Active attack, confirmed data breach, ransomware, device with Restricted data stolen | Immediately |
| **High** | Lost/stolen device, credential compromise, suspected malware infection | Within 1 hour |
| **Medium** | Phishing attempt (not clicked), suspicious activity, policy violation observed | Within 4 hours |
| **Low** | General security concern, minor policy deviation, unusual but not threatening activity | Within 24 hours |

When uncertain about severity, report at the higher level. The IT Security Team will reassess during triage. Do not delay reporting to determine precise classification.

**Reporter responsibilities**:

- Report promptly per the timeframes above.
- Provide accurate information to the best of your knowledge.
- **Preserve evidence**: Forward phishing emails as attachments (do not forward inline or click links). Screenshot anomalies and note exact time and affected systems. Photograph physical security events if safe to do so.
- **Do NOT** attempt to investigate, verify, or resolve the event yourself.
- **Do NOT** attempt to test or exploit suspected vulnerabilities.
- Cooperate with any follow-up investigation by the IT Security Team.

## Non-Blame Culture

The organisation fosters a non-punitive environment for security event reporting.

| Principle | Commitment |
|-----------|------------|
| **Good faith protection** | Personnel who report events in good faith shall not face negative consequences for the act of reporting |
| **Honest mistake handling** | Honest mistakes (e.g., clicking a phishing link) reported promptly shall be handled constructively, focusing on learning and prevention |
| **No retaliation** | Retaliation against good-faith reporters is prohibited and shall itself be subject to disciplinary action |
| **Reporter confidentiality** | Reporter identity shall be protected to the extent possible and shared only on a need-to-know basis |

The organisation shall recognise and encourage exemplary reporting behaviour. Reported events shall be used as learning opportunities, not as triggers for punishment.

**Exceptions to non-blame protection**:

- Deliberate policy violations reported only after discovery by others.
- Malicious activity disguised as accidental.
- Repeated negligence after training and formal warnings.
- False reports made in bad faith.

## Response and Feedback

The organisation shall respond to all security event reports within defined timeframes:

| Response Type | Timeframe |
|---------------|-----------|
| **Acknowledgment** (confirming report received) | Within 4 business hours |
| **Initial assessment** (event classified, priority assigned) | Within 24 hours |
| **Status update to reporter** | Within 72 hours |
| **Closure notification** | Upon resolution |

The organisation shall:

- Acknowledge receipt of all reports (including anonymous reports where a channel for reply exists).
- Provide status updates to reporters on the progress and outcome of their reports.
- Communicate lessons learned from events through awareness updates (without identifying reporters).
- Escalate events to the incident management process (per A.5.24-28) when the event is assessed as a confirmed security incident, requires resources beyond initial response, has regulatory notification implications, or affects multiple systems or business units.

## Reporting Metrics

The organisation shall track the following security event reporting metrics:

| Metric | Target | Review Frequency |
|--------|--------|------------------|
| **Report acknowledgment within 4 business hours** | 100% | Monthly |
| **Initial assessment within 24 hours** | 100% | Monthly |
| **Event volume trend** (increasing awareness or increasing threat) | Tracked | Quarterly |
| **Reporting channel usage** (email, phone, ticketing, anonymous) | Balanced usage across channels | Quarterly |
| **Reporter feedback** (satisfaction with response and communication) | >80% satisfied | Annually (survey) |
| **False positive rate** (events vs. confirmed incidents) | Tracked | Quarterly |

Metrics shall be reported to the CISO monthly and to the Management Review Team quarterly.

**Event reporting KPIs integrated into awareness training**: Annual training shall include reporting volume and success stories to reinforce the non-blame culture.

---

## Reporting Training and Awareness

All personnel shall receive training on security event reporting:

**Initial training** (within 30 days of hire or role change):
- What constitutes a security event vs. incident.
- Reportable event categories with examples.
- Reporting channels and when to use each.
- Reporting timeframes by severity.
- Non-blame culture and good-faith protection.

**Annual refresher training**:
- Updated threat landscape (recent phishing campaigns, social engineering tactics).
- Success stories (events reported that prevented incidents).
- Reporting metrics (reinforcing that reporting is valued).

**Phishing simulation**: Quarterly phishing simulations with immediate training for users who click; simulations treated as learning opportunities, not punitive measures.

Training completion tracked; target: **100% of personnel** complete annual training.

---

## Remote Work Compliance Verification

Remote work security compliance shall be verified through:

**Quarterly compliance checks**:
- VPN/MFA usage logs (100% of remote workers accessing via VPN with MFA).
- Device encryption status (100% of registered devices encrypted).
- Endpoint protection current (100% of devices with current antivirus/EDR).
- Patching compliance (≥95% of devices current on OS and critical patches).

**Annual remote work reviews**:
- Remote work authorisation review (confirm authorisations current and appropriate).
- BYOD device inventory audit (verify all personal devices registered and compliant).
- High-risk remote workers (Confidential data access) — risk assessment refresh.

**Spot checks** (random or triggered):
- IT Security may conduct remote compliance checks (request screenshots showing encryption, endpoint protection, VPN connection).
- Non-compliance triggers remediation plan or revocation of remote work privileges.

Compliance metrics reported to CISO quarterly.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|------------------|
| **Executive Management** | Approve remote work policy; provide resources; champion non-blame reporting culture; receive briefings on critical security events |
| **CISO** | Define remote work security requirements and event reporting mechanisms; authorise high-risk exceptions; oversee compliance; report to management |
| **IT Security Team** | Implement and maintain remote access controls; receive and assess event reports; coordinate response; provide feedback to reporters; maintain reporting channels |
| **IT Operations** | Provision remote access (VPN, MFA, devices); support reporting channel infrastructure; implement containment actions when directed |
| **HR** | Manage remote work agreements and terminations; include event reporting in onboarding; coordinate personnel-related matters |
| **Line Managers** | Authorise remote work for team members; ensure team compliance; encourage event reporting; escalate security concerns |
| **All Personnel** | Comply with remote work requirements; secure devices and data; report events promptly; preserve evidence; cooperate with investigations |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Remote work authorisation records** (approved arrangements with risk assessment where applicable) | HR / Line Managers | *Per arrangement; reviewed annually; retained duration + 2 years* |
| 2 | **Policy acknowledgment records** from remote workers | HR | *Per onboarding / annual renewal; target: 100% coverage* |
| 3 | **Device inventory** (corporate and approved BYOD devices assigned to remote workers) | IT Operations | *Updated within 5 business days of change; audited annually* |
| 4 | **Technical compliance reports** (VPN usage, MFA enrolment, device encryption, patching status) | IT Security | *Reviewed monthly; dashboard updated continuously* |
| 5 | **Security event reports** received through designated channels | IT Security | *Maintained continuously; retained for 3 years minimum* |
| 6 | **Event response records** (acknowledgment, assessment, status updates, closure) with response time metrics | IT Security | *Per event; response timeframe compliance reviewed quarterly* |
| 7 | **Security awareness training records** covering remote work security and event reporting | HR / IT Security | *Annual; completion tracked; target: 100% of remote workers* |
| 8 | **Reporting channel availability records** (testing and uptime of email, phone, ticketing, anonymous channels) | IT Operations | *Tested quarterly; results documented* |
| 9 | **Equipment return and data removal records** upon remote work termination | IT Operations / HR | *Per termination; verified and signed off* |
| 10 | **Exception register** (authorised exceptions to this policy with justification and compensating controls) | CISO | *Updated per exception; reviewed quarterly; time-limited entries re-assessed at expiry* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, remote access log analysis, device compliance reports, event reporting metrics (volume, timeliness, response times), internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Non-compliance with remote work requirements may also result in revocation of remote work privileges. Failure to report security events does not carry non-blame protection and may be treated as a policy violation.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to remote working patterns, emerging threats targeting remote workers, regulatory changes (particularly nFADP and GDPR), technology developments, event reporting trends, and lessons learned from incidents.

---

# Areas of the ISO 27001 Standard Addressed

Remote Working and Security Event Reporting Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 6.3 Information security awareness, education, and training |
| Clause 8.1 Operational planning and control | 6.4 Disciplinary process |
| | **6.7 Remote working** |
| | **6.8 Information security event reporting** |
| | 7.9 Security of assets off premises |
| | 8.1 User endpoint devices |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures for data protection in remote environments |
| Swiss CO Art. 328b | Employee data processing limited to data necessary for employment relationship |
| Swiss DSV (Data Protection Ordinance) | Art. 1-3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 32 — Security of processing must extend to remote work; Art. 33 — Breach notification within 72 hours requires timely event detection |
| ISO/IEC 27001:2022 | Annex A Controls 6.7, 6.8 |
| ISO/IEC 27002:2022 | Sections 6.7, 6.8 — Implementation guidance |
| NIST SP 800-46 Rev 2 | Guide to Enterprise Telework, Remote Access, and BYOD Security |
| CIS Controls v8 | Control 4 (Secure Configuration of Enterprise Assets), Control 6 (Access Control Management), Control 17 (Incident Response Management) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
