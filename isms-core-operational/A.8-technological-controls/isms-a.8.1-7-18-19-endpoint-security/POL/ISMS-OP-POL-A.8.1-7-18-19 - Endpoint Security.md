<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.1-7-18-19:operational:OP-POL:a.8.1-7-18-19 -->
**ISMS-OP-POL-A.8.1-7-18-19 — Endpoint Security**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Endpoint Security |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.1-7-18-19 |
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

- ISO/IEC 27001:2022 Controls A.8.1, A.8.7, A.8.18, A.8.19 — User endpoint devices, protection against malware, use of privileged utility programs, installation of software on operational systems

**Related Annex A Controls**:

| Control | Relationship to Endpoint Security |
|---------|-----------------------------------|
| A.5.9 Inventory of information and other associated assets | Endpoint device inventory and asset register |
| A.5.15–18 Access control and identity management | User authentication and access rights on endpoints |
| A.8.2 Privileged access rights | Privileged access management on endpoint devices |
| A.8.5 Secure authentication | Authentication mechanisms for endpoint access |
| A.8.8 Management of technical vulnerabilities | Patch management for endpoint operating systems and applications |
| A.8.9 Configuration management | Endpoint configuration baselines and hardening |
| A.8.20 Network security | Network admission requirements for endpoint devices |
| A.8.24 Use of cryptography | Full-disk encryption for endpoint devices |

**Related Internal Policies**:

- Access Control Policy
- Use of Cryptography Policy
- Network Security Policy
- Asset Management Policy
- Information Classification and Handling Policy
- Incident Management Policy

---

# Endpoint Security Policy

## Purpose

This policy is to manage and protect organisation endpoint devices and to mitigate the risk of malware, unauthorised software, and misuse of privileged utilities.

This policy supports Swiss nFADP (revDSG) and the Data Protection Ordinance (DSV) by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data) on endpoint devices. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

All employees and third-party users.

All organisation-owned devices (laptops, desktops, mobile phones, tablets).

All devices used to access, process, transmit, or store organisation information, including personally-owned devices where BYOD is permitted.

Virtual devices and cloud-hosted endpoints where applicable and feasible.

## Principle

Organisation devices shall have adequate protection of information from the risk of malware, unauthorised software, and loss or theft. Endpoints are managed on the principle of least privilege with security by design and default.

---

## User Endpoint Devices

### Device Registration and Inventory

All endpoint devices shall be registered in the asset register before being issued to users. The register shall record the device type, serial number, assigned user, operating system, encryption status, and issue date.

Devices that are lost, stolen, decommissioned, or reassigned shall be updated in the asset register promptly.

### Endpoint Configuration Baseline

All endpoint devices shall be configured to a documented security baseline before deployment. The baseline shall include:

- Operating system hardened per vendor and CIS Benchmark guidance (Level 1 minimum; Level 2 for systems handling confidential or sensitive personal data).
- Unnecessary services, ports, and default accounts disabled or removed.
- Full-disk encryption enabled (see Encryption section below).
- Malware protection installed and active (see Malware Protection section below).
- Screen lock and session timeout configured.
- Local firewall enabled.
- Automatic operating system and application updates enabled.

The configuration baseline shall be documented and version-controlled. Baseline standards shall reference vendor hardening guides and CIS Benchmarks. The baseline shall be reviewed at least annually or when significant changes occur to the operating system or threat landscape.

### Endpoint Management Tools

The following categories of management tools shall be deployed to support endpoint security:

| Category | Purpose | Examples |
|----------|---------|----------|
| **Endpoint Detection and Response (EDR)** | Threat detection, investigation, and response on endpoints | CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne, or equivalent |
| **Mobile Device Management (MDM)** | Device enrolment, configuration, compliance, remote wipe | Jamf Pro, Microsoft Intune, VMware Workspace ONE, or equivalent |
| **Patch Management** | Automated deployment and compliance reporting for OS and application patches | WSUS, Jamf Pro, ManageEngine, or equivalent |
| **Encryption Key Escrow** | Centralised recovery key storage for full-disk encryption | MDM-integrated or dedicated key management |
| **Software Approval** | Application allow-listing and installation control | AppLocker, Santa, MDM application catalogue, or equivalent |

### Encryption

All endpoint devices (laptops, desktops, mobile devices) shall have full-disk encryption enabled:

| Platform | Encryption Technology | Minimum Standard |
|----------|-----------------------|-----------------|
| Windows | BitLocker | AES-XTS 256-bit |
| macOS | FileVault | XTS-AES 128-bit |
| Mobile (iOS/Android) | Native device encryption | Enabled by default; verify active |
| Linux | LUKS / dm-crypt | AES-XTS 256-bit |

- Device encryption shall not be disabled by the end user.
- Recovery keys shall be escrowed centrally via MDM (e.g., Jamf Pro, Intune, or equivalent) or equivalent key escrow solution managed by IT. Recovery key access shall be logged and restricted to authorised IT personnel.
- Encryption status shall be verified before the device is approved for use with confidential data.

### Screen Lock and Session Timeout

- Devices shall lock automatically after **15 minutes** of inactivity. Devices with access to confidential or sensitive personal data shall lock after **5 minutes** of inactivity.
- Users shall lock their devices manually when leaving them unattended (Windows+L, Ctrl+Command+Q, or equivalent).
- Authentication (password, PIN, or biometric) shall be required to unlock.
- Lock on sleep and lid-close shall be enabled on all laptops.

### Physical Security

- Devices shall not be left unattended in public places or visible in unattended vehicles.
- Cable locks should be used for desktop devices in shared or public areas.
- Portable devices shall be stored securely when not in use (locked drawer or cabinet).
- Loss or theft of any device shall be reported immediately to the information security management team.

### Remote Wipe

The organisation shall maintain the capability to remotely wipe or lock lost or stolen devices via the MDM platform or equivalent management tool.

Remote wipe process:

1. Device reported lost or stolen — employee notifies IT and line manager immediately.
2. IT initiates **remote lock** within **1 hour** of notification during business hours (next business day start for after-hours reports).
3. If the device is not recovered within **24 hours**, IT initiates **remote wipe**.
4. Remote wipe confirmation shall be documented, including the date, device ID, wipe status (confirmed/pending), and authorising person.
5. Where a BYOD device is wiped, only the organisation container or work profile shall be erased (not personal data), unless the employee has consented to full wipe in the BYOD agreement.

### BYOD (Bring Your Own Device)

If the organisation permits personally-owned devices to access organisation information, the following requirements shall apply:

- The device shall be enrolled in the organisation's mobile device management (MDM) solution.
- Business data shall be separated from personal data using containerisation or a managed work profile.
- The device shall meet the same security baseline as organisation-owned devices (encryption, screen lock, current OS, malware protection).
- The organisation retains the right to remotely wipe organisation data (not personal data) from the device.
- Users shall acknowledge their responsibilities, including physical protection, software updates, and cooperation with security requirements.
- BYOD access shall be revoked on termination or contract end per the Access Control Policy.

### BYOD Enrolment Process

1. Employee submits BYOD access request to IT, specifying device type, operating system, and intended business use scope.
2. IT verifies the device meets minimum requirements (supported OS version, encryption capability, no jailbreak/root).
3. Employee signs the BYOD agreement acknowledging security requirements, remote wipe consent for organisation data, and cooperation obligations.
4. IT enrols the device in MDM and configures the managed work profile or container.
5. IT verifies security baseline compliance (encryption active, screen lock configured, current OS) before granting access.

If BYOD is not permitted, this shall be stated and enforced through technical controls.

---

## Malware and Antivirus Protection

### Approved Software

Only organisation-approved and licensed software shall be installed on organisation equipment.

Unauthorised software, downloaded software, freeware, or unapproved utilities shall not be installed.

### Malware Protection Requirements

Malware protection software (endpoint detection and response — EDR, or next-generation antivirus — NGAV, as appropriate to the organisation's risk profile) shall be installed on every device that can run it.

Malware protection software shall:

- Automatically update detection definitions and engines as they are released by the vendor.
- Not be modified, disabled, or uninstalled by the end user.
- Produce an alert when an infection or suspected infection occurs.
- Be set to auto-repair or quarantine suspect files.
- Automatically scan local storage and attached storage devices.
- Automatically scan any file that is accessed, modified, or executed.
- Retain audit logs which are forwarded to the centralised logging system.

Suspected infections shall be managed via the Incident Management process. The following events shall trigger an incident report:

- EDR/antivirus alert indicating confirmed malware detection (not false positive).
- Ransomware indicators (file encryption activity, ransom note files).
- Unauthorised outbound connections to known command-and-control infrastructure.
- User-reported suspicious behaviour (unexpected pop-ups, performance degradation, unknown processes).
- Detection of unauthorised software or tools on the device.

### Email Protection

Email servers and gateways shall have malware scanning that inspects all inbound and outbound email, including attachments.

### Web Gateway Protection

Internet proxies or secure web gateways shall be configured to:

- Block sites with known malicious reputations.
- Scan content for threats on sites with intermediate reputations.
- Log all detections.
- Automatically check for definition updates.

Allow-listing and deny-listing shall be deployed to control access to approved and prohibited web resources.

### File Integrity Monitoring

File integrity monitoring shall be implemented for system-critical files and files that contain or provide access to personal or confidential data, based on risk and business need.

### Removable Media Controls

- Autorun and autoplay shall be disabled for all removable media.
- Removable media shall be automatically scanned for malware when connected.
- Only organisation-owned, encrypted removable media shall be approved for use with confidential data, in line with the Information Transfer Policy.

---

## Education

Users shall be educated periodically as part of the security awareness programme on:

- Recognising phishing emails and social engineering attacks.
- Safe use of the Internet and email.
- Approved software usage and the prohibition on unapproved software.
- What to do in the event of a suspected malware infection.
- Physical security of devices (locking, storage, reporting loss/theft).

---

## Privileged Utility Programs

### Scope

Privileged utility programs are tools that can override system or application controls. These include but are not limited to:

- System administration tools (user/group management, service management).
- Registry editors, PowerShell (unrestricted execution policy), and command-line tools with elevated privileges.
- Diagnostics, debuggers, and disk utilities.
- Backup and recovery utilities with access to raw data.
- Network management and scanning tools.

### Controls

- Access to privileged utility programs shall be restricted to authorised personnel only, based on the principle of least privilege.
- Multi-factor authentication shall be required for accessing privileged utility programs on critical systems.
- All execution of privileged utility programs shall be logged, including the user, timestamp, utility name, and target system.
- Privileged utility programs that are not required for operational purposes shall be removed or disabled.
- The use of privileged utility programs shall be subject to periodic review (at least quarterly) to verify continued business justification.
- The organisation shall maintain a documented list of approved privileged utility programs by role.

---

## Installation of Software on Operational Systems

### Software Installation Controls

- Software installation on operational systems shall be performed only by authorised personnel (IT administrators or designated support staff).
- Standard users shall not have local administrator rights. Where elevation is required, a managed privilege escalation mechanism shall be used:
  - **Just-in-time (JIT) access**: Temporary elevation granted for a defined period (maximum 4 hours), automatically revoked on expiry.
  - **Approval workflow**: User submits request with business justification; IT or line manager approves; elevation granted and logged.
  - All privilege escalations shall be logged (user, timestamp, justification, duration, approver).
- All software installations shall follow the organisation's change management process, including testing, approval, and documentation.
- Only approved software from the organisation's software catalogue shall be installed. New software requests shall be submitted through a formal approval process.

### Patch Management

Operating systems, applications, and browser software on endpoint devices shall be kept up to date. Security patches shall be applied according to the following timelines:

| Severity | Timeframe |
|----------|-----------|
| Critical vulnerabilities (CVSS 9.0+, active exploitation) | Within 14 days |
| High vulnerabilities (CVSS 7.0–8.9) | Within 30 days |
| Medium vulnerabilities (CVSS 4.0–6.9) | Within 90 days |
| Low vulnerabilities (CVSS 0.1–3.9) | Next scheduled maintenance window |

Patches shall be tested before deployment using the following approach:

| System Type | Testing Requirement |
|-------------|-------------------|
| Standard endpoints (laptops, desktops) | Deploy to a **pilot group** (5–10% of devices) for **48 hours** before full rollout |
| Mobile devices | Deploy to a pilot group via MDM for 48 hours before full rollout |
| Specialised endpoints (kiosks, lab systems) | Test in non-production environment before deployment |

- **P0 emergency patches** (active exploitation confirmed) may bypass pilot testing with CISO approval. Enhanced monitoring for 48 hours post-deployment and a documented rollback plan are required.
- **Patch failure handling**: If a patch causes operational issues in the pilot group, deployment shall be halted, the issue documented, and the vendor contacted. A workaround or compensating control shall be applied until a stable patch is available.

Automatic updates shall be enabled for operating systems and supported applications. Devices that have not applied critical patches within the defined timeframe shall be flagged for remediation or restricted from network access.

### Rollback

A rollback strategy shall be agreed upon before applying updates or installations to operational systems to ensure business continuity if a patch causes issues.

### Audit Trail

A record of all software changes on operational systems shall be maintained, including the software name, version, date of installation, and the individual who performed the change.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; approval of exceptions and emergency patch bypasses; escalation point for non-compliance |
| **IT Operations / Endpoint Team** | Device provisioning, baseline configuration, MDM management, patch deployment, remote wipe execution |
| **Information Security Management Team** | EDR monitoring, malware incident triage, privileged utility reviews, compliance reporting |
| **Asset Owner / Line Manager** | Approval of device allocation, BYOD requests, and software requests for their team |
| **All Users** | Physical security of devices, reporting loss/theft immediately, cooperating with security requirements, not disabling security controls |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Endpoint device inventory** (asset register with encryption status, OS version, assigned user) | IT Operations | *Updated per event; full audit annually* |
| 2 | **Endpoint configuration baseline** documentation and compliance scan reports | IT Operations | *Baseline reviewed annually; compliance scans monthly* |
| 3 | **Malware protection deployment** and update status reports (coverage percentage, definition currency) | Information Security | *Monthly reports; target: 100% coverage* |
| 4 | **Malware detection and incident logs** (detections, quarantine actions, incident escalations) | Information Security | *Reviewed monthly; retained 12 months* |
| 5 | **Software installation records** and change management approvals | IT Operations | *Per event; audited quarterly* |
| 6 | **Privileged utility program** approved list and usage logs | Information Security | *List reviewed quarterly; logs retained 12 months* |
| 7 | **Patch compliance reports** (percentage of devices current, overdue patches by severity) | IT Operations | *Monthly; target: ≥95% current within SLA* |
| 8 | **BYOD enrolment records** and MDM compliance status (if applicable) | IT Operations | *Updated per event; reviewed semi-annually* |
| 9 | **Remote wipe execution records** (device ID, date, wipe status, authorising person) | IT Operations | *Per event; retained 3 years* |
| 10 | **Pilot group patch testing records** (test results, issues identified, rollout decisions) | IT Operations | *Per patch cycle* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, endpoint compliance scanning, malware detection reports, patch status reports, software inventory audits, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to endpoint security standards, emerging threats (including new malware techniques and attack vectors), regulatory changes, and lessons learned from incidents.

---

# Areas of the ISO 27001 Standard Addressed

Endpoint Security Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | **8.1 User endpoint devices** |
| | **8.7 Protection against malware** |
| | **8.18 Use of privileged utility programs** |
| | **8.19 Installation of software on operational systems** |
| | 8.23 Web filtering |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures for data protection |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 32 — Security of processing (endpoint controls as appropriate measure) |
| ISO/IEC 27001:2022 | Annex A Controls 8.1, 8.7, 8.18, 8.19 |
| ISO/IEC 27002:2022 | Sections 8.1, 8.7, 8.18, 8.19 — Implementation guidance |
| NIST SP 800-53 Rev 5 | SC-28 (Protection of Information at Rest), SI-3 (Malicious Code Protection), CM-11 (User-Installed Software) |
| CIS Controls v8 | Control 2 (Inventory and Control of Software Assets), Control 4 (Secure Configuration), Control 10 (Malware Defenses) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
