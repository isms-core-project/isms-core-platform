# ISMS-POL-A.8.1-7-18-19-S2
## Endpoint Devices Requirements (A.8.1)

**Document ID**: ISMS-POL-A.8.1-7-18-19-S2  
**Title**: Endpoint Devices Requirements (ISO/IEC 27001:2022 Control A.8.1)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Endpoint Security Manager | Initial endpoint devices requirements (A.8.1) |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: IT Operations Manager / Endpoint Management Lead
- Implementation Review: Endpoint Administrators

**Distribution**: Endpoint team, security team, IT operations, auditors  
**Related Documents**: 
- ISMS-POL-A.8.1-7-18-19 (Master Framework)
- ISMS-POL-A.8.1-7-18-19-S1 (Executive Summary)
- ISMS-IMP-A.8.1-7-18-19-S1 (Endpoint Discovery Process)
- ISMS-IMP-A.8.1-7-18-19-S2 (Security Baseline Implementation)

---

## 1. Control Objective and Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.1

**Official Control Text**:

> *Information stored on, processed by or accessible via user endpoint devices shall be protected.*

**Control Purpose**: Ensure that information on user endpoint devices is protected against risks arising from endpoint usage, including loss, theft, unauthorized access, malware infection, and inadequate security configurations.

**Why This Matters**:

User endpoint devices are the primary interface between users and organizational information. These devices are vulnerable to:
- **Physical Loss/Theft**: Laptops left in vehicles, mobile devices misplaced in public
- **Unauthorized Access**: Unencrypted devices accessed by unauthorized parties
- **Malware Infection**: Endpoints as initial infection vector for ransomware, spyware
- **Data Leakage**: Sensitive data stored on unmanaged BYOD devices
- **Weak Configurations**: Default passwords, disabled firewalls, outdated operating systems
- **Insider Threats**: Authorized users misusing endpoint access

Comprehensive endpoint device security reduces these risks through inventory management, security baselines, encryption, and endpoint management controls.

### 1.2 Scope of A.8.1 Requirements

This section defines mandatory requirements for:

1. **Endpoint Inventory and Asset Management** - Knowing what endpoints exist
2. **Endpoint Classification** - Understanding endpoint types, ownership models, criticality
3. **Security Baseline Requirements** - Minimum security configurations per endpoint type
4. **Encryption Requirements** - Protecting data at rest on endpoints
5. **Endpoint Management Requirements** - Centralized management and control
6. **Physical Security and Lost/Stolen Device Procedures** - Responding to physical compromise
7. **Secure Disposal Requirements** - Data sanitization before decommissioning
8. **BYOD (Bring Your Own Device) Requirements** - Securing personal devices used for work

### 1.3 Integration with A.8.7, A.8.18, A.8.19

While A.8.1 focuses on endpoint devices and their security baselines:
- **A.8.7** addresses malware protection on these endpoints
- **A.8.18** addresses privileged utilities running on these endpoints
- **A.8.19** addresses software installation controls on these endpoints

All four controls share the same endpoint inventory and management infrastructure but have distinct requirements for audit purposes.

---

## 2. Endpoint Inventory and Asset Management

### 2.1 Requirement: Complete Endpoint Inventory

**REQ-A81-001**: [Organization] **MUST** maintain a complete and current inventory of all user endpoint devices that store, process, or access organizational information.

**Minimum Inventory Coverage**: ≥95% of network-connected endpoints (target: 100%)

**Inventory Attributes** (Mandatory):

| Attribute | Description | Examples |
|-----------|-------------|----------|
| **Device ID** | Unique identifier | Serial number, UUID, asset tag |
| **Hostname** | Computer/device name | DESKTOP-ABC123, iPhone-JohnSmith |
| **Device Type** | Category of endpoint | Laptop, Desktop, Smartphone, Tablet |
| **Operating System** | OS and version | Windows 11 23H2, macOS 14.2, iOS 17.1 |
| **Owner** | Assigned user or department | John Smith, IT Department, Visitor |
| **Ownership Model** | Who owns the device | Corporate-Owned, BYOD, Contractor, Guest |
| **Location** | Physical location | Office, Remote, Mobile, Data Center |
| **Network Connection** | How device connects | Wired, Wireless, VPN, Direct Internet |
| **Criticality** | Business importance | Critical, High, Medium, Low |
| **Last Seen** | Last network connection | Date/time of last successful connection |
| **Discovery Method** | How device was found | MDM, Network Scan, Manual Entry |
| **Discovery Date** | When added to inventory | Date device first inventoried |

**Inventory Update Frequency**:
- **Automated Discovery**: Weekly network scans minimum (daily preferred)
- **MDM Inventory Sync**: Daily synchronization from MDM platform
- **Manual Updates**: Within 24 hours of known device additions/removals
- **Reconciliation**: Monthly reconciliation (automated inventory vs. network discovery vs. manual records)

**Inventory Maintenance**:
- **Stale Endpoints**: Devices not seen >30 days flagged for investigation
- **Retired Endpoints**: Devices marked for disposal remain in inventory until disposal certified
- **Lost/Stolen**: Devices reported lost/stolen flagged immediately, remote wipe attempted

**Audit Verification**:
- Evidence: Endpoint_Inventory.xlsx (Inventory worksheet)
- Verification Method: Spot-check random sample (20 endpoints) for accuracy
- Acceptance Criteria: Inventory accuracy ≥95% (manual verification vs. automated inventory)

### 2.2 Requirement: Endpoint Classification

**REQ-A81-002**: [Organization] **MUST** classify endpoints by device type, ownership model, and criticality to apply appropriate security controls.

**Device Type Classification**:
- **Laptop**: Portable computer (corporate laptop, BYOD laptop)
- **Desktop**: Fixed workstation (office desktop, kiosk)
- **Smartphone**: Mobile phone (iOS, Android, other mobile OS)
- **Tablet**: Tablet computer (iPad, Android tablet, Windows Surface)
- **Server** (if used as endpoint): Server accessed directly by users (not typical - flag for review)
- **IoT Device**: Connected device processing organizational data (flag for special handling)
- **Virtual Desktop**: VDI/DaaS client device

**Ownership Model Classification**:
- **Corporate-Owned**: Device purchased and owned by [Organization]
  - Full security baseline enforcement
  - Complete endpoint management
  - Comprehensive software restrictions
- **BYOD**: Personal device used for work
  - Limited security baseline (minimum requirements)
  - Containerized management (MAM)
  - User privacy protections
- **Contractor**: Device owned by contractor/consultant
  - Security baseline verification required
  - Time-limited access
  - Enhanced monitoring
- **Guest**: Temporary visitor device
  - Network isolation only (guest WiFi)
  - No access to corporate resources
- **Lab/Test**: Development and testing endpoints
  - Enhanced monitoring
  - No production data access

**Criticality Classification**:
- **Critical**: Endpoints accessing highly sensitive data (executive devices, finance, HR)
  - Enhanced security baseline
  - Mandatory encryption
  - Immediate remote wipe if lost/stolen
- **High**: Standard business endpoints (most corporate devices)
  - Standard security baseline
  - Mandatory encryption (laptops/desktops)
  - Remote wipe within 4 hours if lost/stolen
- **Medium**: Limited access endpoints (kiosks, guest devices with limited access)
  - Baseline security controls
  - Encryption recommended
- **Low**: Highly restricted endpoints (isolated lab devices, no data storage)
  - Minimal baseline
  - Network isolation primary control

**Audit Verification**:
- Evidence: Endpoint_Inventory.xlsx (Classification worksheet)
- Verification Method: Classification rules applied consistently
- Acceptance Criteria: 100% of endpoints classified

---

## 3. Security Baseline Requirements

### 3.1 Requirement: Security Baselines Per Endpoint Type

**REQ-A81-003**: [Organization] **MUST** define and enforce security baselines for each endpoint type (Windows, macOS, Linux, iOS, Android).

**Baseline Development Approach**:
- **Industry Standards**: CIS Benchmarks as baseline reference (customized for [Organization])
- **Vendor Guidance**: Microsoft security baselines, Apple platform security guides
- **Risk-Based**: Baselines adjusted based on endpoint criticality and data sensitivity
- **Technology-Agnostic**: Principles defined, implementation varies by platform

**Baseline Components** (All Endpoint Types):

1. **OS Hardening**:
   - Disable unnecessary services and features
   - Remove/disable default accounts (Guest account, etc.)
   - Enable secure boot (where supported)
   - Disable auto-run/auto-play for removable media

2. **Firewall Enabled**:
   - Host-based firewall enabled and configured
   - Default deny inbound, allow outbound
   - Exceptions documented and approved

3. **Automatic OS and Software Updates**:
   - Automatic updates enabled (or managed via centralized system)
   - Critical/security updates applied within SLA (see A.8.19 for patch SLAs)
   - Update verification monitoring

4. **Screen Lock**:
   - Maximum inactivity timeout: 15 minutes (corporate), 5 minutes (critical endpoints)
   - Password/PIN/biometric required to unlock
   - Lock on lid close (laptops)

5. **Strong Authentication**:
   - Password complexity: Minimum 12 characters (or passphrase >20 characters)
   - Password rotation: 90 days (or passwordless authentication with MFA)
   - Account lockout: 5 failed attempts → 15-minute lockout
   - MFA required for corporate account access (where technically feasible)

6. **Disk/Device Encryption** (see Section 4 for details):
   - Full disk encryption for laptops and desktops
   - Device encryption for mobile devices
   - Encryption verification and key escrow

7. **Anti-Malware Installed and Active** (see ISMS-POL-A.8.1-7-18-19-S3 for A.8.7 details):
   - Anti-malware/EDR solution installed
   - Real-time protection enabled
   - Regular scans configured

8. **Software Installation Restrictions** (see ISMS-POL-A.8.1-7-18-19-S5 for A.8.19 details):
   - Application control enabled (AppLocker, Gatekeeper, etc.)
   - Only approved software permitted
   - User installation restricted

**Baseline Enforcement**:
- **Windows**: Group Policy (GPO) or Intune configuration profiles
- **macOS**: Jamf configuration profiles or Intune profiles
- **Linux**: Configuration management (Ansible, Puppet, Chef) or manual enforcement
- **iOS**: MDM configuration profiles (Intune, Jamf Pro, etc.)
- **Android**: MDM managed configuration or Android Enterprise policies

**Baseline Compliance Monitoring**:
- **Automated Compliance Scanning**: Weekly minimum (daily preferred)
- **Compliance Reporting**: Monthly compliance dashboard
- **Non-Compliance Remediation**: Automatic remediation where possible, manual follow-up within 7 days for exceptions
- **Compliance Threshold**: Target ≥90% baseline compliance across all endpoints

**Audit Verification**:
- Evidence: Endpoint_Inventory.xlsx (Baseline_Compliance worksheet)
- Verification Method: Spot-check sample endpoints (10 per OS type)
- Acceptance Criteria: Sample endpoints meet baseline requirements ≥90%

### 3.2 Requirement: Windows Security Baseline

**REQ-A81-004**: Windows endpoints (Windows 10, Windows 11, Windows Server used as endpoints) **MUST** meet the Windows Security Baseline.

**Key Windows Baseline Requirements** (non-exhaustive - see implementation docs for full baseline):

1. **OS Hardening**:
   - Windows Defender Firewall enabled (all network profiles)
   - SMBv1 disabled
   - Windows Update automatic download and install configured
   - BitLocker enabled (see Section 4)
   - Local Administrator account disabled (domain-joined endpoints)
   - Remote Desktop (RDP) disabled or restricted to authorized users only

2. **Authentication**:
   - Domain authentication required (corporate endpoints)
   - Local account passwords meet complexity requirements
   - Windows Hello for Business enabled (where supported)
   - Credential Guard enabled (supported hardware)

3. **Application Control**:
   - AppLocker or Windows Defender Application Control (WDAC) enabled
   - Default deny for executables, scripts, libraries (whitelisting approach)

4. **Microsoft Defender Antivirus** (if using Microsoft solution):
   - Real-time protection enabled
   - Cloud-delivered protection enabled
   - Automatic sample submission enabled (or manual submission process)
   - Tamper protection enabled

5. **Audit Logging**:
   - Windows Event Log configured (Security, System, Application logs)
   - Key events logged: Account logon, privilege use, object access, policy changes
   - Logs forwarded to centralized SIEM (see A.8.15)

**Baseline Source**: Microsoft Security Baseline for Windows 10/11 + CIS Benchmark Level 1

**Audit Verification**:
- Evidence: GPO exports, Intune configuration profiles, compliance scan reports
- Verification Method: Automated compliance scanning via Microsoft Defender for Endpoint or third-party tools
- Acceptance Criteria: Windows baseline compliance ≥90%

### 3.3 Requirement: macOS Security Baseline

**REQ-A81-005**: macOS endpoints (macOS 12 Monterey and later) **MUST** meet the macOS Security Baseline.

**Key macOS Baseline Requirements** (non-exhaustive):

1. **OS Hardening**:
   - macOS Firewall enabled
   - Automatic software updates enabled
   - FileVault full disk encryption enabled (see Section 4)
   - Gatekeeper enabled (only allow apps from App Store and identified developers)
   - System Integrity Protection (SIP) enabled (default - do not disable)

2. **Authentication**:
   - Screen saver password required
   - Automatic login disabled
   - Touch ID or password required for wake/unlock
   - iCloud authentication with organization account (if using managed Apple IDs)

3. **Application Control**:
   - Gatekeeper enforced (do not allow "Anywhere" for app downloads)
   - Notarization requirements enforced
   - Third-party app installation restrictions (via MDM)

4. **Security Tools**:
   - XProtect (built-in macOS malware protection) enabled
   - MRT (Malware Removal Tool) enabled
   - Third-party EDR/antivirus (if organization requires beyond built-in)

5. **Audit Logging**:
   - Unified Logging enabled (default)
   - Security-relevant events forwarded to centralized SIEM

**Baseline Source**: Apple Platform Security Guide + CIS Benchmark for macOS

**Audit Verification**:
- Evidence: Jamf/Intune configuration profiles, compliance scan reports
- Verification Method: Automated compliance scanning via MDM or third-party tools
- Acceptance Criteria: macOS baseline compliance ≥90%

### 3.4 Requirement: Linux Security Baseline

**REQ-A81-006**: Linux endpoints (Ubuntu, Red Hat, CentOS, Debian, other distributions) **MUST** meet the Linux Security Baseline.

**Key Linux Baseline Requirements** (non-exhaustive):

1. **OS Hardening**:
   - Firewall enabled (iptables, firewalld, ufw)
   - Unnecessary services disabled
   - SELinux or AppArmor enabled (enforcing mode)
   - Full disk encryption (LUKS) enabled (see Section 4)
   - SSH hardening (key-based auth, disable root login, non-standard port optional)

2. **Authentication**:
   - Strong password policies enforced (/etc/login.defs, PAM)
   - Account lockout configured (faillock)
   - sudo usage restricted (only authorized users)
   - Screen lock configured (screensaver with password)

3. **Application Control**:
   - Package manager restrictions (only install from trusted repositories)
   - AppArmor or SELinux policies for applications
   - Execution restrictions for /tmp, /var/tmp (noexec mount option)

4. **Security Tools**:
   - ClamAV or third-party antivirus installed
   - Host-based intrusion detection (AIDE, Tripwire, or similar)
   - Log forwarding to centralized SIEM

5. **Audit Logging**:
   - auditd enabled and configured
   - Security-relevant events logged
   - Logs forwarded to centralized SIEM

**Baseline Source**: CIS Benchmark for specific Linux distribution

**Audit Verification**:
- Evidence: Configuration management reports (Ansible/Puppet/Chef playbooks), compliance scan reports
- Verification Method: Automated compliance scanning via configuration management or third-party tools
- Acceptance Criteria: Linux baseline compliance ≥90%

### 3.5 Requirement: Mobile Device Security Baseline (iOS/Android)

**REQ-A81-007**: Mobile devices (iOS 15+, Android 11+) **MUST** meet the Mobile Device Security Baseline.

**Key Mobile Baseline Requirements** (iOS and Android):

1. **OS Hardening**:
   - Device encryption enabled (built-in iOS encryption, Android encryption)
   - Automatic OS updates enabled (or MDM-managed updates)
   - Jailbreak/root detection enabled (deny access if jailbroken/rooted)
   - Device passcode required (minimum 6-digit PIN or equivalent)

2. **Authentication**:
   - Biometric authentication enabled (Face ID, Touch ID, fingerprint)
   - Auto-lock timeout: 5 minutes maximum
   - Passcode complexity enforced

3. **Application Control** (Corporate-Owned Devices):
   - MDM app whitelisting/blacklisting
   - App installation restricted to approved apps (via MDM)
   - Unmanaged apps cannot access corporate data (data loss prevention)

4. **Data Protection**:
   - Managed apps only for corporate email, documents, etc.
   - Copy/paste restrictions between managed and unmanaged apps
   - Cloud backup restrictions for corporate data

5. **Security Tools**:
   - Mobile Threat Defense (MTD) solution (if organization requires)
   - Phishing protection (built-in or third-party)

**BYOD Mobile Devices** (Different Baseline):
- Containerized management (MAM) - corporate apps in separate container
- Corporate data encrypted within container
- No full device encryption requirement (privacy consideration)
- No device-level restrictions (user privacy)
- Container-level wipe capability (not full device wipe)

**Audit Verification**:
- Evidence: MDM compliance reports, device configuration profiles
- Verification Method: MDM compliance dashboard (Intune Compliance, Jamf Pro, etc.)
- Acceptance Criteria: Mobile baseline compliance ≥90% (corporate), ≥70% (BYOD - limited controls)

---

## 4. Encryption Requirements

### 4.1 Requirement: Full Disk Encryption (Laptops and Desktops)

**REQ-A81-008**: All corporate-owned laptops and desktops **MUST** have full disk encryption (FDE) enabled.

**Encryption Technologies**:
- **Windows**: BitLocker Drive Encryption (TPM-based preferred)
- **macOS**: FileVault 2
- **Linux**: LUKS (Linux Unified Key Setup) or dm-crypt
- **Third-Party Solutions**: Acceptable if meet encryption strength requirements

**Encryption Requirements**:
- **Algorithm**: AES-256 minimum
- **Pre-Boot Authentication**: Required (password, PIN, or TPM-based)
- **Key Management**: 
  - **Corporate Devices**: Encryption recovery keys escrowed centrally (MBAM, Intune, Jamf, or similar)
  - **BYOD Devices**: No key escrow (user privacy) - encryption required but recovery key not collected
- **Verification**: Monthly verification that encryption is enabled and active

**Exceptions**:
- **Desktop Computers in Secure Facilities**: Encryption optional if physical access highly restricted (data center servers, locked server rooms)
  - Exception requires CISO approval
  - Alternative controls: Physical security, access logging, no sensitive data storage
- **Legacy Hardware Incompatible with Encryption**: Exception allowed until hardware replacement
  - Alternative controls: No sensitive data storage, enhanced network controls, accelerated replacement schedule

**Encryption Deployment Timing**:
- **New Devices**: Encryption enabled before deployment to users (100% compliance)
- **Existing Devices**: Encryption deployed via phased rollout:
  - Critical endpoints (executives, finance, HR): Within 30 days
  - High-priority endpoints (standard corporate): Within 90 days
  - Medium-priority endpoints: Within 180 days

**Audit Verification**:
- Evidence: Endpoint_Inventory.xlsx (Encryption_Status worksheet), encryption management console reports
- Verification Method: Automated encryption status reporting from MDM/encryption management
- Acceptance Criteria: Encryption coverage ≥98% (corporate laptops/desktops)

### 4.2 Requirement: Mobile Device Encryption

**REQ-A81-009**: All corporate-owned mobile devices (smartphones, tablets) **MUST** have device encryption enabled.

**Mobile Encryption**:
- **iOS Devices**: Built-in encryption (enabled by default when passcode set)
- **Android Devices**: Device encryption enabled (Android 10+ encrypted by default)

**BYOD Mobile Devices**:
- **Container Encryption**: Corporate container/apps encrypted (via MAM solution)
- **Full Device Encryption**: Recommended but not enforced (user privacy)

**Verification**: MDM reports device encryption status (monthly verification)

**Audit Verification**:
- Evidence: MDM compliance reports showing encryption status
- Verification Method: MDM compliance dashboard
- Acceptance Criteria: Mobile encryption coverage ≥95% (corporate), ≥60% (BYOD containers)

### 4.3 Requirement: Encryption Key Escrow and Recovery

**REQ-A81-010**: Encryption recovery keys for corporate-owned devices **MUST** be escrowed centrally to enable data recovery in case of forgotten passwords or device failures.

**Key Escrow Requirements**:
- **Windows BitLocker**: Recovery keys stored in Active Directory, Microsoft Intune, or MBAM
- **macOS FileVault**: Recovery keys stored in Jamf Pro, Intune, or institutional recovery key
- **Linux LUKS**: Recovery keys stored in centralized key management system or secure vault

**Key Escrow Restrictions**:
- **BYOD Devices**: No key escrow (user privacy protection)
- **Contractor Devices**: No key escrow (contractor owns device and data)

**Key Recovery Procedures**:
- User requests key recovery via IT service desk
- Identity verification required (multi-factor)
- Key provided after verification
- Key recovery events logged for audit

**Key Protection**:
- Encryption keys stored encrypted (key encryption key)
- Access restricted to authorized IT personnel only
- Key access logged and audited quarterly

**Audit Verification**:
- Evidence: Key escrow configuration, key recovery logs
- Verification Method: Verify keys escrowed for sample of encrypted devices (20 devices)
- Acceptance Criteria: 100% of corporate encrypted devices have keys escrowed

---

## 5. Endpoint Management Requirements

### 5.1 Requirement: Endpoint Management Enrollment

**REQ-A81-011**: All corporate-owned endpoints **MUST** be enrolled in an endpoint management system (MDM for mobile, agent-based for laptops/desktops).

**Endpoint Management Platforms** (technology-agnostic - examples):
- **Cross-Platform**: Microsoft Intune, VMware Workspace ONE, JAMF Pro (macOS/iOS)
- **Windows**: SCCM (System Center Configuration Manager), Intune
- **macOS/iOS**: Jamf Pro, Intune
- **Linux**: Configuration management (Ansible, Puppet, Chef) or agent-based solutions

**Enrollment Requirements**:
- **Timing**: Enrollment required before device given to user (pre-deployment)
- **Coverage**: 100% of corporate laptops, desktops, mobile devices
- **BYOD**: Containerized management (MAM) via MDM - limited scope (corporate apps/data only)
- **Contractor**: Not enrolled (but security baseline verification required via other means)

**Management Capabilities Required**:
- **Configuration Management**: Deploy and enforce security baselines (GPO, MDM profiles)
- **Software Deployment**: Centralized software deployment and updates
- **Compliance Monitoring**: Monitor baseline compliance, encryption status, software inventory
- **Remote Wipe**: Capability to remotely wipe device if lost/stolen
- **Inventory Sync**: Automatically update endpoint inventory
- **Policy Enforcement**: Enforce security policies (password, encryption, application control)

**Enrollment Verification**: Monthly MDM/management enrollment reports

**Audit Verification**:
- Evidence: Endpoint_Inventory.xlsx (Management_Enrollment worksheet), MDM enrollment reports
- Verification Method: MDM dashboard showing enrolled devices
- Acceptance Criteria: Enrollment coverage ≥98% (corporate devices)

### 5.2 Requirement: Endpoint Configuration Management

**REQ-A81-012**: Endpoint configurations **MUST** be managed centrally to ensure consistency and prevent configuration drift.

**Configuration Management Methods**:
- **Windows**: Group Policy (GPO), Intune configuration profiles
- **macOS**: Jamf configuration profiles, Intune profiles
- **Linux**: Configuration management tools (Ansible, Puppet, Chef)
- **Mobile**: MDM configuration profiles

**Configuration Management Scope**:
- Security baselines (see Section 3)
- Application settings (corporate apps)
- Network settings (WiFi, VPN, proxy)
- Certificate deployment (internal CA certificates)
- Compliance policies (password, encryption, etc.)

**Configuration Drift Detection**:
- **Automated Scanning**: Weekly configuration compliance scans
- **Drift Remediation**: Automatic re-application of configurations where possible
- **Drift Reporting**: Monthly drift report (number of drift incidents, root causes)
- **Drift SLA**: Configuration drift remediated within 7 days

**Audit Verification**:
- Evidence: Configuration policy exports (GPO, MDM profiles), compliance scan reports
- Verification Method: Spot-check sample endpoints for configuration compliance
- Acceptance Criteria: Configuration drift incidents <10 per quarter

---

## 6. Physical Security and Lost/Stolen Device Procedures

### 6.1 Requirement: User Physical Security Responsibilities

**REQ-A81-013**: All users **MUST** be trained on endpoint physical security best practices.

**User Responsibilities** (from security awareness training):
- **Unattended Devices**: Lock screen when leaving device unattended (even briefly)
- **Screen Privacy**: Use privacy screen filters in public locations
- **Secure Storage**: Lock devices in secure location when not in use (not left on desk overnight)
- **Physical Protection**: Do not leave devices in vehicles (visible theft risk)
- **Awareness in Public**: Be aware of surroundings when using device in public (shoulder surfing, theft)
- **Travel Security**: Enhanced security when traveling (especially international)

**Physical Security Controls** (device-level):
- Screen lock enabled (see baseline requirements)
- Cable locks (Kensington locks) for desktop computers in open areas
- Device tracking (Find My Device, Find My Mac, mobile device tracking) enabled

**Audit Verification**:
- Evidence: Security awareness training completion records, training content
- Verification Method: Review training materials, verify user completion rates
- Acceptance Criteria: 100% user security awareness training completion annually

### 6.2 Requirement: Lost/Stolen Device Reporting and Response

**REQ-A81-014**: Users **MUST** report lost or stolen devices immediately, and [Organization] **MUST** execute remote wipe procedures promptly.

**Reporting Requirements**:
- **Immediate Reporting**: User reports lost/stolen device to IT Service Desk immediately upon awareness
- **Reporting Channels**: Phone, email, self-service portal (24/7 availability)
- **Information Captured**: Device details, when/where lost, data on device, circumstances

**Response Procedures**:
- **Immediate Actions** (within 1 hour of report):
  - Verify report authenticity (confirm user identity)
  - Locate device (if tracking enabled - Find My Device, MDM location tracking)
  - Disable user account access (prevent unauthorized access to cloud services via device)
  - Flag device in inventory as "Lost/Stolen"

- **Remote Wipe Execution** (within 4 hours of report):
  - Attempt remote wipe via MDM platform (Intune, Jamf, etc.)
  - Verify wipe successful (if device connects to network)
  - Document wipe attempt and outcome
  - If device offline: Wipe executed when device next connects

- **Corporate Devices**: Full device wipe (factory reset)
- **BYOD Devices**: Container/corporate data wipe only (preserve personal data)

- **Follow-Up Actions** (within 24 hours):
  - Incident report filed (security incident tracking)
  - User provided with replacement device (if applicable)
  - Post-incident review (root cause, user awareness issue?)

**SLA Requirements**:
- Report acknowledgment: <1 hour
- Remote wipe execution (if device online): <4 hours
- Incident documentation: <24 hours

**Audit Verification**:
- Evidence: Lost/stolen device incident reports, remote wipe logs, MDM wipe confirmations
- Verification Method: Review sample of lost/stolen incidents (last 12 months)
- Acceptance Criteria: 100% incidents have wipe attempted within 4 hours, 100% documented

### 6.3 Requirement: Device Recovery Procedures

**REQ-A81-015**: If lost devices are recovered, they **MUST** undergo security review before being returned to service.

**Recovery Procedures**:
1. **Security Review**: Determine if device potentially compromised
2. **Forensic Analysis** (if high-risk device): Forensic imaging and analysis before restore
3. **Re-image**: Factory reset and re-image device (do not trust existing OS)
4. **Re-enroll**: Re-enroll in endpoint management
5. **Re-deploy**: Deploy fresh configuration and return to service

**Return to User**:
- User training: Reinforce physical security best practices
- Data restoration: Restore user data from backup (if applicable)

**Audit Verification**:
- Evidence: Device recovery incident reports, re-imaging documentation
- Verification Method: Review recovery procedures in incident documentation
- Acceptance Criteria: 100% recovered devices re-imaged before return to service

---

## 7. Secure Disposal Requirements

### 7.1 Requirement: Data Sanitization Before Disposal

**REQ-A81-016**: Endpoints being decommissioned or disposed of **MUST** have data securely sanitized to prevent data recovery.

**Data Sanitization Methods**:
- **Software-Based Sanitization**: NIST SP 800-88 compliant tools (DBAN, Blancco, secure erase utilities)
  - Minimum: 3-pass overwrite (DoD 5220.22-M standard)
  - Preferred: 7-pass overwrite for highly sensitive endpoints
  - SSD-specific: Secure erase command (ATA Secure Erase) or cryptographic erase (if encrypted)

- **Physical Destruction** (for highly sensitive devices or damaged storage):
  - Hard drive shredding (data center-grade shredders)
  - Degaussing (magnetic media only - not SSDs)
  - Third-party certified destruction services (certificate of destruction required)

**Disposal Process**:
1. **Remove from Inventory**: Mark device for disposal in inventory
2. **Data Backup** (if needed): Backup any required data before sanitization
3. **Sanitization**: Execute sanitization method appropriate to device type and sensitivity
4. **Verification**: Verify sanitization successful (cannot recover data)
5. **Certificate of Destruction**: Document sanitization/destruction (certificate, logs)
6. **Asset Disposal**: Device physically disposed (recycling, destruction, donation)
7. **Inventory Update**: Mark device as "Disposed" in inventory with disposal date

**Disposal SLA**:
- Devices retired → sanitized within 30 days
- Certificate of destruction provided within 7 days of disposal

**Audit Verification**:
- Evidence: Disposal records, certificates of destruction, sanitization logs
- Verification Method: Review disposal records for sample of disposed devices (last 12 months)
- Acceptance Criteria: 100% disposed devices have certificate of destruction/sanitization log

### 7.2 Requirement: Asset Decommissioning Workflow

**REQ-A81-017**: Endpoint decommissioning **MUST** follow a documented workflow to ensure complete asset lifecycle management.

**Decommissioning Workflow**:
1. **User Off-boarding**: User leaves organization → device collected
2. **Asset Recovery**: IT collects device from user or shipping
3. **Data Backup**: User data backed up if retention needed
4. **Device Assessment**: Determine if device reusable or disposal
   - **Reusable**: Re-image, re-deploy (see REQ-A81-015)
   - **Disposal**: Sanitization required (see REQ-A81-016)
5. **License Reclamation**: Software licenses de-activated and reclaimed
6. **Inventory Update**: Device status updated (Retired, Re-deployed, or Disposed)
7. **Documentation**: Decommissioning documented (date, reason, disposition)

**Audit Verification**:
- Evidence: Decommissioning records, inventory updates
- Verification Method: Review decommissioning workflow for sample of retired devices
- Acceptance Criteria: 100% decommissioned devices have documented workflow

---

## 8. BYOD (Bring Your Own Device) Requirements

### 8.1 Requirement: BYOD Minimum Security Standards

**REQ-A81-018**: Personal devices (BYOD) used to access organizational information **MUST** meet minimum security standards.

**BYOD Enrollment Requirements**:
- **Voluntary Program**: BYOD is voluntary (users may choose to use corporate device instead)
- **User Agreement**: User signs BYOD agreement acknowledging responsibilities
- **MDM Enrollment**: Device enrolled in MDM for containerized management (MAM)
- **Privacy Notice**: User informed of [Organization] access scope (corporate container only, not personal data)

**Minimum BYOD Security Standards**:

1. **Operating System**:
   - **Supported OS Versions**: Must run current or previous OS version (no outdated/unsupported OS)
   - **Security Updates**: Auto-updates enabled (OS and security patches)
   - **Jailbreak/Root**: No jailbroken/rooted devices (MDM detects and blocks)

2. **Device Security**:
   - **Screen Lock**: Passcode/PIN/biometric required (minimum 6-digit PIN)
   - **Auto-Lock**: 15-minute maximum inactivity timeout
   - **Device Encryption**: Recommended but not enforced (user privacy)

3. **Anti-Malware**:
   - **Corporate Endpoints (BYOD laptops)**: Anti-malware required
   - **Mobile Devices (BYOD smartphones/tablets)**: Built-in OS security sufficient (iOS/Android)

4. **Containerized Corporate Data**:
   - **Managed Apps**: Corporate email, documents, apps in managed container
   - **Data Separation**: Corporate data cannot be copied to personal apps (DLP controls)
   - **Container Encryption**: Corporate container encrypted
   - **Remote Wipe**: [Organization] can remotely wipe corporate container (not personal data)

5. **User Responsibilities**:
   - **Physical Security**: User responsible for physical device security
   - **Lost/Stolen Reporting**: Immediate reporting required
   - **Compliance**: Accept remote wipe of corporate container if device lost/stolen or employment terminates

**BYOD Restrictions**:
- **No Admin Rights**: Users cannot grant [Organization] administrative access to personal device
- **No Personal App Inventory**: [Organization] does not inventory or monitor personal apps
- **No Full Device Wipe**: Remote wipe limited to corporate container (user privacy protection)
- **Data Retention**: Corporate data deleted from device when user leaves [Organization] or exits BYOD program

**Audit Verification**:
- Evidence: BYOD user agreements, MDM enrollment reports (BYOD devices), compliance scan results
- Verification Method: Review BYOD program documentation, MDM compliance dashboard
- Acceptance Criteria: 100% BYOD devices enrolled in MAM, 100% user agreements signed

### 8.2 Requirement: BYOD Privacy Protections

**REQ-A81-019**: [Organization]'s BYOD program **MUST** respect user privacy and limit organizational access to corporate data only.

**Privacy Protections**:
- **No Personal Data Access**: [Organization] cannot access personal emails, photos, contacts, browsing history
- **No Personal App Inventory**: [Organization] does not inventory personal apps (only managed corporate apps)
- **No Full Device Control**: [Organization] cannot lock entire device, restrict personal app usage
- **Container-Only Management**: MDM management scope limited to corporate container
- **Transparent Privacy Notice**: Users informed exactly what [Organization] can and cannot access

**User Consent Required For**:
- MDM enrollment (containerized management)
- Corporate container remote wipe capability
- Corporate data access logging (within container)

**User Rights**:
- Exit BYOD program at any time (corporate data removed)
- Request removal of corporate container (employment termination or program exit)
- Retain full personal data ownership

**Audit Verification**:
- Evidence: BYOD privacy notice, user consent forms
- Verification Method: Review privacy notice for BYOD users
- Acceptance Criteria: 100% BYOD users provided privacy notice, 100% consent documented

---

## 9. Audit Verification Criteria

### 9.1 Evidence Requirements for A.8.1 Compliance

**Mandatory Evidence**:
1. **Endpoint Inventory**: Endpoint_Inventory.xlsx (Inventory worksheet)
   - Complete inventory with all mandatory attributes
   - ≥95% coverage (all network-connected endpoints)
   - Updated weekly minimum

2. **Classification**: Endpoint_Inventory.xlsx (Classification worksheet)
   - All endpoints classified by type, ownership, criticality
   - 100% classification coverage

3. **Baseline Compliance**: Endpoint_Inventory.xlsx (Baseline_Compliance worksheet)
   - Baseline compliance assessment per endpoint
   - ≥90% baseline compliance target
   - Updated monthly minimum

4. **Encryption Status**: Endpoint_Inventory.xlsx (Encryption_Status worksheet)
   - Encryption verification for all corporate laptops/desktops
   - ≥98% encryption coverage target (corporate devices)
   - Encryption key escrow verification

5. **Management Enrollment**: Endpoint_Inventory.xlsx (Management_Enrollment worksheet)
   - MDM enrollment status for all corporate devices
   - ≥98% enrollment coverage target

6. **Lost/Stolen Procedures**: Incident reports, remote wipe logs
   - Documentation of lost/stolen incidents (last 12 months)
   - Remote wipe attempts within 4 hours (100% compliance)

7. **Disposal Procedures**: Certificates of destruction, sanitization logs
   - Documentation of disposed endpoints (last 12 months)
   - 100% have certificate of destruction

8. **BYOD Program**: BYOD user agreements, privacy notices, MDM enrollment
   - User agreement signed (100% BYOD users)
   - Privacy notice provided (100% BYOD users)
   - MAM enrollment (100% BYOD devices)

### 9.2 Assessment Methodology

**Compliance Scoring**:
- **Inventory Completeness**: (Endpoints in inventory / Network-connected endpoints) × 100
- **Classification Coverage**: (Classified endpoints / Total endpoints) × 100
- **Baseline Compliance**: Average baseline compliance score across all endpoints
- **Encryption Coverage**: (Encrypted corporate laptops/desktops / Total corporate laptops/desktops requiring encryption) × 100
- **Management Enrollment**: (Enrolled corporate devices / Total corporate devices) × 100

**Overall A.8.1 Compliance Score**: Weighted average
- Inventory Completeness: 20%
- Baseline Compliance: 30%
- Encryption Coverage: 30%
- Management Enrollment: 20%

**Compliance Thresholds**:
- **Green (Compliant)**: ≥90%
- **Yellow (Partial Compliance)**: 70-89%
- **Red (Non-Compliant)**: <70%

**Assessment Frequency**:
- **Continuous**: Automated compliance monitoring via MDM (daily)
- **Weekly**: Baseline compliance scans, inventory updates
- **Monthly**: Comprehensive compliance reporting (all metrics)
- **Quarterly**: Executive dashboard and trend analysis
- **Annual**: Full assessment, auditor review, policy review

### 9.3 Auditor Verification Steps

**For ISO 27001 Certification Audits**:

1. **Review Policy Documentation**:
   - ISMS-POL-A.8.1-7-18-19-S2 (this document)
   - Implementation procedures (ISMS-IMP-A.8.1-7-18-19-S1, S2)

2. **Review Evidence**:
   - Endpoint_Inventory.xlsx (all worksheets)
   - MDM console screenshots
   - Baseline compliance reports
   - Encryption management console reports
   - Lost/stolen incident reports
   - Disposal certificates

3. **Sample Testing** (recommended sample size):
   - Select random sample of 20 endpoints
   - Verify inventory accuracy (device exists, attributes correct)
   - Verify baseline compliance (manual check or automated scan)
   - Verify encryption status (manual verification)
   - Verify management enrollment (MDM console verification)

4. **Interview Personnel**:
   - Endpoint administrators: Understanding of baseline requirements
   - Help desk: Knowledge of lost/stolen reporting procedures
   - Users: Awareness of physical security responsibilities (sample 5 users)

5. **Verify Incident Response**:
   - Review sample of lost/stolen incidents (last 12 months)
   - Verify remote wipe attempts, timing compliance (within 4 hours)

6. **Assess BYOD Program** (if applicable):
   - Review BYOD user agreements and privacy notices
   - Verify MAM enrollment for sample of BYOD devices
   - Confirm containerization and data separation

**Acceptance Criteria for Audit**:
- All evidence available and complete
- Compliance scores meet thresholds (≥90% target)
- Sample testing confirms automated reporting accuracy
- Personnel demonstrate understanding of procedures
- Incidents handled per documented procedures

---

**END OF SECTION 2**

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Endpoint Security Manager | Initial endpoint devices requirements (A.8.1) |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**

**Next Document**: ISMS-POL-A.8.1-7-18-19-S3 (Malware Protection Requirements - A.8.7)