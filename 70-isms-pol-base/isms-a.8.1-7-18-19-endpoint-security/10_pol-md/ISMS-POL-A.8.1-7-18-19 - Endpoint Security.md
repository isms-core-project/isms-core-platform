**ISMS-POL-A.8.1-7-18-19 – Endpoint Security**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Endpoint Security |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.1-7-18-19 |
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
| 1.0 | [Date] | CISO / Endpoint Security Manager | Initial framework - Combined controls A.8.1, A.8.7, A.8.18, A.8.19 |

**Review Cycle**: Annual (or upon significant organizational/regulatory/technology changes)  
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO) or IT Director
- Technical Review: IT Operations Manager / Endpoint Management Lead
- Compliance: Legal/Compliance Officer (for regulatory alignment)
- Final Authority: Executive Management (CEO)


**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.1-7-18-19 (Implementation Guidance Suite)
- ISMS-POL-A.5.9 (Asset Inventory)
- ISMS-POL-A.8.2 (Privileged Access Rights)
- ISMS-POL-A.8.8 (Vulnerability Management)
- ISMS-POL-A.8.15 (Logging)
- ISMS-POL-A.8.16 (Monitoring Activities)
- ISMS-POL-A.8.20-22 (Network Security)
- ISO/IEC 27001:2022 Controls A.8.1, A.8.7, A.8.18, A.8.19


---

## Executive Summary

This policy establishes [Organization]'s requirements for endpoint security, implementing ISO/IEC 27001:2022 Controls A.8.1 (User Endpoint Devices), A.8.7 (Protection Against Malware), A.8.18 (Use of Privileged Utility Programs), and A.8.19 (Installation of Software on Operational Systems) as a unified security framework.

**Scope**: This policy applies to all user endpoint devices regardless of type (laptops, desktops, mobile devices, tablets, IoT devices), operating system (Windows, macOS, Linux, iOS, Android, ChromeOS), or ownership model (corporate-owned, BYOD, contractor, guest).

**Purpose**: Define organizational requirements for endpoint security control implementation and governance. This policy establishes WHAT endpoint security protection is required, WHEN it must be implemented, and WHO is accountable. Implementation procedures (HOW controls are implemented) are documented separately in ISMS-IMP-A.8.1-7-18-19 Implementation Guides.

**Combined Control Rationale**: A.8.1 (endpoint devices), A.8.7 (malware protection), A.8.18 (privileged utilities), and A.8.19 (software installation) are implemented as a unified framework because:

- They operate on the same endpoint infrastructure
- Endpoint discovery activities serve all four controls
- Assessment evidence overlaps significantly (endpoint inventory, software inventory, security tool telemetry)
- Endpoint security requires holistic implementation (cannot secure endpoints in silos)
- Combined approach is 4x more efficient than separate implementations


**Statement of Applicability Independence**: Despite unified implementation and documentation, Controls A.8.1, A.8.7, A.8.18, and A.8.19 are assessed independently in the Statement of Applicability. Each control maintains distinct requirements, evidence collection, and compliance scoring for audit purposes.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss Federal Data Protection Act (nDSG/FADP), EU GDPR where applicable, and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS, HIPAA, FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

---

# Control Alignment & Scope

## ISO/IEC 27001:2022 Control Alignment

**ISO/IEC 27001:2022 Annex A.8.1, A.8.7, A.8.18, A.8.19 – Endpoint Security**

This policy framework provides organizational governance for four related controls covering the complete endpoint security ecosystem:

### A.8.1 - User Endpoint Devices

> *Information stored on, processed by or accessible via user endpoint devices shall be protected.*

**Control Objective**: Ensure that information on user endpoint devices is protected against risks arising from endpoint usage, including loss, theft, unauthorized access, malware infection, and inadequate security configurations.

**This Policy Addresses** (A.8.1):

- Endpoint inventory and asset management requirements
- Endpoint classification and criticality determination
- Security baseline requirements per endpoint type and ownership model
- Encryption requirements for data at rest
- Endpoint management and enrollment requirements (MDM, agent-based)
- Physical security and lost/stolen device response requirements
- Secure disposal requirements
- BYOD program security requirements and privacy protections


### A.8.7 - Protection Against Malware

> *Protection against malware shall be implemented and supported by appropriate user awareness.*

**Control Objective**: Ensure detection, prevention, and recovery from malware attacks through technical controls and user awareness.

**This Policy Addresses** (A.8.7):

- Anti-malware/EDR solution requirements and detection capabilities
- Protection coverage requirements across endpoint landscape
- Real-time protection and scanning requirements
- Signature/definition update requirements
- Quarantine and remediation requirements
- Malware incident response requirements
- User awareness requirements


### A.8.18 - Use of Privileged Utility Programs

> *Use of utility programs that might be capable of overriding system and application controls shall be restricted and tightly controlled.*

**Control Objective**: Ensure that privileged utilities that can bypass or override security controls are identified, restricted to authorized users only, used appropriately, and their usage is monitored and logged.

**This Policy Addresses** (A.8.18):

- Privileged utility identification and inventory requirements
- Access control requirements for privileged utilities
- Approval workflow requirements for privileged access
- Usage monitoring and logging requirements
- Security bypass tool management requirements


### A.8.19 - Installation of Software on Operational Systems

> *Procedures and measures shall be implemented to securely manage the installation of software on operational systems.*

**Control Objective**: Ensure that software installations on operational systems are controlled, authorized, and do not introduce security vulnerabilities or malware.

**This Policy Addresses** (A.8.19):

- Approved software list requirements
- Software approval process requirements
- Change control integration requirements
- Unauthorized software detection and removal requirements
- Application control technology requirements
- Software vulnerability management requirements
- BYOD software control requirements


## What This Policy Does

This policy:

- **Defines** endpoint security control requirements aligned with data classification, organizational risk appetite, and regulatory obligations
- **Establishes** governance framework for endpoint security decision-making and accountability
- **Specifies** mandatory control implementation requirements (WHAT must be implemented)
- **References** applicable regulatory requirements per ISMS-POL-00
- **Identifies** organizational roles and responsibilities for endpoint security governance
- **Provides** framework for managing exceptions and incidents


## What This Policy Does NOT Do

This policy does NOT:

- **Specify technical implementation procedures** (see ISMS-IMP-A.8.1-7-18-19 Implementation Guides)
- **Define specific endpoint discovery methods** (see ISMS-IMP-A.8.1-7-18-19-S1 Endpoint Discovery Process)
- **List security baseline configurations** (see ISMS-IMP-A.8.1-7-18-19-S2 Security Baseline Implementation)
- **Provide anti-malware deployment procedures** (see ISMS-IMP-A.8.1-7-18-19-S3 Malware Protection Deployment)
- **Detail software approval workflows** (see ISMS-IMP-A.8.1-7-18-19-S4 Software Control Process)
- **Specify privileged utility access controls** (see ISMS-IMP-A.8.1-7-18-19-S5 Privileged Utility Management)
- **Define assessment methodologies** (see ISMS-IMP-A.8.1-7-18-19-S6 Endpoint Security Assessment)
- **Select specific technologies or vendors** (technology selection based on [Organization]'s risk assessment, technical environment, and budget)
- **Replace risk assessment** (endpoint security controls selected based on [Organization]'s risk treatment decisions)


**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite evolving technology landscape
- Technical agility for technology updates without policy revision
- Clear distinction between governance (policy) and execution (implementation)


## Scope

**This policy applies to**:

**Endpoint Device Types**:

- Laptops and desktops (corporate-owned and BYOD, all operating systems)
- Mobile devices (smartphones and tablets - iOS, Android, other mobile OS)
- Specialized endpoints (thin clients, chromebooks, kiosks, point-of-sale terminals)
- IoT devices that store, process, or access organizational information
- Virtual desktop infrastructure (VDI/DaaS client-side security components)


**Operating Systems**:

- Windows (Windows 10, Windows 11, Windows Server endpoint use cases)
- macOS (macOS 12 Monterey and later versions)
- Linux (Ubuntu, Red Hat, CentOS, Debian, and other distributions)
- iOS (iOS 15 and later versions)
- Android (Android 11 and later versions)
- ChromeOS and other operating systems used on user endpoint devices


**Ownership Models**:

- Corporate-Owned: Devices purchased and managed by [Organization]
- BYOD (Bring Your Own Device): Personal devices used for work purposes
- Contractor Devices: Devices owned by contractors, consultants, temporary staff
- Guest Devices: Temporary visitor devices with limited network access
- Lab/Test Devices: Development, testing, and quality assurance endpoints


**Personnel**:

- Employees (full-time, part-time, temporary)
- Contractors and consultants
- Third-party vendors with endpoint access
- Guests and visitors (limited access scenarios)


**Network Locations**:

- On-premises (offices, data centers, conference rooms)
- Remote/home office (work-from-home endpoints)
- Mobile (traveling employees, field workers)
- Branch offices and satellite locations
- Customer sites and third-party locations


## Out of Scope

This policy does **NOT** cover the following areas (covered by separate ISMS policies):

- **Server Infrastructure**: Covered by server security controls and hardening policies
- **Network Infrastructure**: Covered by ISMS-POL-A.8.20-22 (Network Security)
- **Cloud Infrastructure**: Covered by ISMS-POL-A.5.23 (Cloud Services Security)
- **Physical Security**: Covered by ISMS-POL-A.7.x (Physical and Environmental Security)
- **Identity and Access Management**: Covered by ISMS-POL-A.5.15-16-18 (Identity & Access Management)
- **Data Classification and Handling**: Covered by ISMS-POL-A.5.12-13 (Information Classification and Handling)


However, this policy **integrates** with these control areas where endpoint security intersects with other controls (see Section 4).

## Technology Neutrality

This policy is **completely technology-agnostic**:

- Works with any endpoint management platform (Intune, Jamf, SCCM, Google Workspace MDM, VMware Workspace ONE, etc.)
- Supports any anti-malware/EDR vendor (CrowdStrike, Microsoft Defender, SentinelOne, Carbon Black, etc.)
- Compatible with any application control technology (AppLocker, Gatekeeper, whitelisting solutions)
- Adaptable to any privileged access management (PAM) solution
- Vendor selection decisions are separate from policy framework
- Principles and requirements remain constant regardless of technology choices


Implementation guidance (ISMS-IMP-A.8.1-7-18-19 suite) provides technology-specific examples while maintaining policy-level technology neutrality.

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG** | All Swiss operations | Art. 8 - Appropriate technical and organizational measures for data protection |
| **EU GDPR** | When processing EU personal data | Art. 32 - Security measures including encryption, access controls, malware protection |
| **ISO/IEC 27001:2022** | Certification scope | Controls A.8.1, A.8.7, A.8.18, A.8.19 - Documented policy and implementation |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Endpoint Security Requirements |
|-----------|-------------------|-------------------------------|
| **PCI DSS v4.0** | Processing payment card data | Endpoint security for systems accessing cardholder data (Requirements 2, 5, 6, 10, 11) |
| **HIPAA** | Processing protected health information (ePHI) | Technical safeguards including encryption, access controls, audit logging (45 CFR § 164.312) |
| **FINMA** | Swiss regulated financial institution | Technical and organizational measures per risk assessment, operational risk management |
| **DORA** | EU financial services entity | ICT risk management including endpoint security controls |
| **NIS2** | Essential/important entity (EU) | Security measures for network and information systems including endpoints |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- NIST Cybersecurity Framework 2.0
- NIST SP 800-53 Rev. 5
- CIS Controls v8 (Controls 1, 2, 4, 5, 7, 10, 16)
- MITRE ATT&CK Framework


**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment documented in ISMS-POL-00. The most stringent requirements apply where multiple regulations overlap.

---

# Endpoint Security Requirements Framework

## Endpoint Device Security (A.8.1)

**Objective**: Protect information stored on, processed by, or accessible via user endpoint devices.

### Endpoint Inventory (Mandatory)

[Organization] SHALL maintain a complete and current inventory of all user endpoint devices that store, process, or access organizational information.

**Minimum Inventory Coverage**: ≥95% of network-connected endpoints (target: 100%)

**Inventory Update Frequency**: Weekly automated discovery minimum (daily preferred), monthly reconciliation

**Implementation Note**: Endpoint discovery procedures, inventory attributes, and reconciliation methods are defined in ISMS-IMP-A.8.1-7-18-19-S1 (Endpoint Discovery Process).

### Endpoint Classification (Mandatory)

[Organization] SHALL classify endpoints by device type, ownership model, and criticality to apply appropriate security controls.

**Classification Dimensions**:

- Device Type (laptop, desktop, mobile, tablet, IoT, VDI client)
- Ownership Model (corporate-owned, BYOD, contractor, guest, lab/test)
- Criticality (critical, high, medium, low - based on data accessed and business impact)


**Implementation Note**: Classification criteria, procedures, and security control mapping are defined in ISMS-IMP-A.8.1-7-18-19-S1 (Endpoint Discovery Process).

### Security Baselines (Mandatory)

[Organization] SHALL implement security baselines appropriate to endpoint type and ownership model.

**Universal Baseline Requirements** (all endpoints):

- Operating system hardening (latest security updates, firewall enabled, unnecessary services disabled)
- Authentication controls (strong passwords, screen lock, MFA where applicable)
- Network security (secure WiFi, Bluetooth restrictions)
- Logging and monitoring (security event logging, SIEM integration where applicable)


**Platform-Specific Baselines**: Windows, macOS, Linux, iOS/Android baselines SHALL be defined based on vendor security guidance (Microsoft Security Baselines, Apple Platform Security Guide) and industry standards (CIS Benchmarks).

**Baseline Compliance Monitoring**: Weekly automated compliance scanning minimum (daily preferred), monthly compliance reporting, ≥90% compliance target across all endpoints.

**Implementation Note**: Detailed baseline specifications, enforcement mechanisms, and compliance monitoring procedures are defined in ISMS-IMP-A.8.1-7-18-19-S2 (Security Baseline Implementation).

### Encryption (Mandatory)

[Organization] SHALL implement encryption to protect data at rest on endpoints.

**Full Disk Encryption Requirements**:

- All corporate-owned laptops and desktops: Full disk encryption (FDE) required (≥98% coverage target)
- Encryption algorithm: AES-256 minimum
- Pre-boot authentication: Required
- Encryption key escrow: Required for corporate-owned devices (recovery keys stored centrally)


**Mobile Device Encryption Requirements**:

- All corporate-owned mobile devices: Device encryption enabled (≥95% coverage target)
- BYOD mobile devices: Container encryption required (corporate apps/data only)


**Encryption Deployment Timing**:

- New devices: Encryption enabled before deployment (100% compliance)
- Existing devices: Critical endpoints within 30 days, high-priority within 90 days, medium-priority within 180 days


**Exceptions**: Desktop computers in secure facilities MAY be exempted with CISO approval and compensating controls. Secure facilities are defined as: (a) Physically access-controlled areas with badge/biometric entry; (b) 24/7 monitoring or staffed reception; (c) No public access; (d) Documented in physical security register per A.7.1-4.

**Implementation Note**: Encryption deployment procedures, key management, and verification methods are defined in ISMS-IMP-A.8.1-7-18-19-S2 (Security Baseline Implementation).

### Endpoint Management (Mandatory)

[Organization] SHALL enroll all corporate-owned endpoints in an endpoint management system (MDM for mobile, agent-based for laptops/desktops).

**Required Management Capabilities**:

- Configuration management (deploy and enforce security baselines)
- Software deployment (centralized software distribution and updates)
- Compliance monitoring (monitor baseline compliance, encryption status, software inventory)
- Remote wipe capability (for lost/stolen devices)
- Inventory synchronization (automatically update endpoint inventory)


**Enrollment Requirements**:

- Timing: Enrollment required before device given to user (pre-deployment)
- Coverage: 100% target for corporate laptops, desktops, mobile devices
- BYOD: Containerized management (MAM) via MDM - limited scope (corporate apps/data only)


**Configuration Drift Management**: Weekly configuration compliance scans, automatic remediation where possible, drift remediated within 7 days.

**Implementation Note**: Management platform selection, enrollment procedures, and configuration drift detection are defined in ISMS-IMP-A.8.1-7-18-19-S2 (Security Baseline Implementation).

### Lost/Stolen Device Response (Mandatory)

[Organization] SHALL implement procedures for responding to lost or stolen endpoint devices.

**Reporting Requirements**: Users SHALL report lost/stolen devices immediately (target: within 1 hour of discovery).

**Remote Wipe Requirements**: Remote wipe capability SHALL be available for all corporate-owned endpoints, initiated within 4 hours of report (1 hour for critical devices).

**Implementation Note**: Lost/stolen device reporting procedures, remote wipe workflows, and incident response are defined in ISMS-IMP-A.8.1-7-18-19-S2 (Security Baseline Implementation).

### Secure Disposal (Mandatory)

[Organization] SHALL securely dispose of endpoints when decommissioned to prevent data leakage.

**Disposal Requirements**:

- Data sanitization: Secure erase (NIST SP 800-88 compliant) or physical destruction
- Certificate of destruction: Required for all disposed endpoints
- Inventory update: Endpoint marked "Disposed" in inventory with certificate attached


**Disposal Methods**:

- Secure Erase: DoD 5220.22-M or NIST SP 800-88 Clear/Purge
- Degaussing: For magnetic hard drives
- Physical Destruction: Shredding, crushing, or incineration (certified vendor)


**Implementation Note**: Disposal procedures, sanitization methods, and vendor selection are defined in ISMS-IMP-A.8.1-7-18-19-S2 (Security Baseline Implementation) and ISMS-REF-A.8.10 (Deletion Methods Reference).

### BYOD Program (Conditional)

[Organization] MAY implement a BYOD program allowing personal devices for work purposes, subject to security requirements and user privacy protections.

**BYOD Security Requirements**:

- BYOD user agreement: Required (user acknowledges security requirements and remote container wipe)
- Minimum device security: Device passcode, encryption (or container encryption), auto-lock, supported OS
- Containerized management (MAM): Corporate apps in managed container, separated from personal data
- Remote wipe scope: Container-only wipe (not full device wipe)


**BYOD Privacy Protections**: No personal data access, no personal app inventory, no full device control, container-only management, transparent privacy notice.

**Implementation Note**: BYOD program design, user agreement templates, MAM configuration, and privacy protections are defined in ISMS-IMP-A.8.1-7-18-19-S2 (Security Baseline Implementation).

## Malware Protection (A.8.7)

**Objective**: Protect endpoints from malware through detection, prevention, and recovery controls, supported by user awareness.

### Anti-Malware/EDR Solution (Mandatory)

[Organization] SHALL deploy anti-malware or EDR solutions with multi-layered detection capabilities.

**Required Detection Mechanisms**:

- Signature-based detection: Traditional antivirus signatures for known malware
- Behavioral detection (heuristics): Monitors program behavior for suspicious activities
- Machine learning-based detection: AI/ML models for unknown threat identification (strongly recommended)
- Exploit prevention: Blocks exploit techniques
- Ransomware-specific protection: Behavioral analysis, controlled folder access, rollback capability


**Cloud-Delivered Protection**: Anti-malware/EDR solutions SHOULD leverage cloud-delivered protection for real-time threat intelligence.

**Tamper Protection**: Anti-malware/EDR agents SHALL have tamper protection enabled to prevent malware from disabling protection.

**Implementation Note**: Solution selection, deployment architecture, and feature configuration are defined in ISMS-IMP-A.8.1-7-18-19-S3 (Malware Protection Deployment).

### Protection Coverage (Mandatory)

[Organization] SHALL achieve malware protection coverage across endpoint landscape.

**Coverage Requirements**:

- Corporate endpoints: ≥98% protection coverage (target: 100%)
- BYOD endpoints: ≥80% protection coverage (lower due to voluntary nature and limited management)


**Coverage Monitoring**: Daily coverage reports from anti-malware management console, immediate alerting if coverage drops below 95%.

**Gap Remediation**: Unprotected endpoint identified → protection deployed within 24 hours.

**Implementation Note**: Coverage monitoring procedures, gap identification, and remediation workflows are defined in ISMS-IMP-A.8.1-7-18-19-S3 (Malware Protection Deployment).

### Real-Time Protection and Scanning (Mandatory)

[Organization] SHALL implement real-time protection and periodic scanning.

**Real-Time Protection**: On-access scanning SHALL be enabled on all protected endpoints (files scanned when opened, executed, or copied).

**Full System Scans**: Full system scans SHALL be performed weekly on all protected endpoints.

**Quick Scans**: Quick scans SHOULD be performed daily on all protected endpoints.

**Implementation Note**: Scan configuration, scheduling, and result monitoring are defined in ISMS-IMP-A.8.1-7-18-19-S3 (Malware Protection Deployment).

### Signature Updates (Mandatory)

[Organization] SHALL keep anti-malware signatures/definitions current.

**Update Frequency**: Daily minimum (real-time updates strongly preferred for cloud-delivered protection).

**Update Verification**: Outdated signatures flagged (Yellow: >24 hours outdated, Red: >48 hours outdated), remediation within 24 hours.

**Agent Currency**: Anti-malware/EDR agent software SHALL be kept current (latest version or N-1), ≥90% of endpoints on latest or N-1 version.

**Implementation Note**: Update deployment, verification procedures, and agent version management are defined in ISMS-IMP-A.8.1-7-18-19-S3 (Malware Protection Deployment).

### Quarantine and Remediation (Mandatory)

[Organization] SHALL implement automatic malware quarantine and remediation procedures.

**Automatic Quarantine**: Detected malware SHALL be automatically quarantined without user interaction.

**Remediation Requirements**: Malware remediation SHALL include cleanup, verification, and recovery (restore files from backup, reset compromised credentials, re-image if necessary for severe infections).

**Implementation Note**: Quarantine configuration, remediation workflows, and recovery procedures are defined in ISMS-IMP-A.8.1-7-18-19-S3 (Malware Protection Deployment).

### Malware Incident Response (Mandatory)

[Organization] SHALL implement incident response procedures for malware infections.

**Detection Triggers**: Malware detected by anti-malware/EDR (automatic alerting), behavioral anomalies detected, user reports suspicious behavior.

**Response Timeline**: Triage within 1 hour, containment immediate for critical (active ransomware, data exfiltration), within 4 hours for high-severity.

**Incident Logging**: All malware detections logged centrally (SIEM per ISMS-POL-A.8.15), incident tickets created, 12-month retention minimum.

**Implementation Note**: Incident classification, response workflows, and escalation procedures are defined in ISMS-IMP-A.8.1-7-18-19-S3 (Malware Protection Deployment).

### User Awareness (Mandatory)

[Organization] SHALL provide user security awareness training on malware threats.

**Training Requirements**:

- Topics: Phishing recognition, safe email/browsing practices, USB/removable media risks, reporting suspicious activity
- Frequency: Initial training during onboarding, annual refresher minimum (quarterly recommended)
- Phishing simulations: Quarterly simulated phishing campaigns
- Effectiveness measurement: ≥95% training completion annually, ≤10% phishing simulation click rate target
- Repeat failure remediation: Personnel failing two consecutive phishing simulations SHALL receive targeted remediation training within 14 days; three or more consecutive failures triggers manager notification and enhanced monitoring per HR policy


**Implementation Note**: Training content, delivery methods, and effectiveness measurement are defined in ISMS-IMP-A.8.1-7-18-19-S3 (Malware Protection Deployment).

## Privileged Utility Management (A.8.18)

**Objective**: Restrict and tightly control privileged utilities capable of overriding system and application controls.

### Privileged Utility Inventory (Mandatory)

[Organization] SHALL maintain an inventory of privileged utility programs capable of overriding system and application controls.

**Privileged Utilities Include**:

- System administration tools (Task Manager, Registry Editor, Services Manager, MMC)
- Remote access tools (Remote Desktop, VNC, TeamViewer, SSH clients)
- Debugging and development tools (debuggers, decompilers, hex editors)
- Disk and file utilities (disk formatters, partition managers, secure delete tools)
- Password and security tools (password recovery, encryption bypass tools)
- Network utilities (packet sniffers, port scanners, network analyzers)
- Virtualization tools (hypervisors, VM management tools)
- Any tools that can bypass security controls (disable antivirus, modify audit logs)


**Inventory Maintenance**: Quarterly review of privileged utility inventory, new utilities assessed before deployment.

**Implementation Note**: Privileged utility identification, inventory procedures, and classification are defined in ISMS-IMP-A.8.1-7-18-19-S5 (Privileged Utility Management).

### Access Control (Mandatory)

[Organization] SHALL restrict access to privileged utilities to authorized personnel only.

**Role-Based Access Control (RBAC)**: Access to privileged utilities SHALL be restricted based on job role and business need.

**Access Control Mechanisms**:

- Application whitelisting: Privileged utilities blocked for standard users (see REQ-A819-005)
- Privileged Access Management (PAM): Just-in-time access, session recording for highly privileged utilities
- Group Policy (Windows): Disable Task Manager, Registry Editor for standard users
- MDM restrictions (macOS/mobile): Restrict access to developer tools, system settings
- sudo restrictions (Linux): Limit sudo access to authorized users only


**Multi-Factor Authentication**: Access to critical privileged utilities SHALL require multi-factor authentication.

**Implementation Note**: Access control implementation, RBAC configuration, and MFA enforcement are defined in ISMS-IMP-A.8.1-7-18-19-S5 (Privileged Utility Management).

### Approval Workflows (Mandatory)

[Organization] SHALL implement approval workflows for privileged utility access requests.

**Access Request Types**:

- Standing access (permanent assignment): Manager approval + CISO approval (critical utilities), annual recertification
- Temporary access (time-limited): Manager approval, auto-revocation after duration, 1-90 days maximum
- Emergency access (break-glass): Post-approval (access granted immediately, manager notified), reviewed within 24 hours


**Approval Documentation**: Request ticket, business justification, approval authority, approval date, access duration (if temporary).

**Implementation Note**: Approval workflow design, request forms, and recertification procedures are defined in ISMS-IMP-A.8.1-7-18-19-S5 (Privileged Utility Management).

### Usage Monitoring and Logging (Mandatory)

[Organization] SHALL log and monitor privileged utility usage.

**Logging Requirements**: User identity, utility name, timestamp, duration, endpoint identifier, actions performed (if available - session recording).

**Log Retention**: 12 months minimum.

**Monitoring Requirements**: Real-time alerting for unauthorized privileged utility usage attempts, daily review of privileged utility usage logs (automated anomaly detection), quarterly usage audit.

**SIEM Integration**: Privileged utility usage logs forwarded to centralized SIEM (per ISMS-POL-A.8.15).

**Implementation Note**: Logging configuration, monitoring procedures, and SIEM integration are defined in ISMS-IMP-A.8.1-7-18-19-S5 (Privileged Utility Management).

### Security Bypass Tool Management (Mandatory)

[Organization] SHALL identify and tightly restrict tools capable of bypassing security controls.

**Security Bypass Tools Include**: Anti-malware disablers, audit log editing tools, encryption bypass tools (password crackers), rootkit tools, tools that disable Windows Defender or tamper protection, tools that modify system integrity protection (macOS SIP).

**Control Approach**:

- Prohibited: Security bypass tools prohibited on production endpoints (unless authorized for security testing)
- Detection: Application control detects unauthorized security bypass tools (see Section 2.4)
- Automatic remediation: Detected tools automatically quarantined/removed
- Authorized use: Security team only, isolated security lab environment, approval required


**Implementation Note**: Security bypass tool identification, detection rules, and authorized usage procedures are defined in ISMS-IMP-A.8.1-7-18-19-S5 (Privileged Utility Management).

## Software Installation Controls (A.8.19)

**Objective**: Securely manage software installation on operational systems through controls, authorization, and vulnerability management.

### Approved Software List (Mandatory)

[Organization] SHALL maintain an approved software list.

**Approved Software List Contents**: Software name and vendor, approved version(s), purpose/business justification, security review status, installation method, approval authority, license compliance status.

**Software Categories**:

- Mandatory corporate software: Required for all users (OS, anti-malware, productivity suite)
- Role-specific software: Required for specific roles (development tools for developers)
- Optional approved software: Available for user installation (approved browsers, utilities)
- Prohibited software: Explicitly prohibited (security risks, licensing issues)


**List Maintenance**: Annual review of approved software list, quarterly additions/removals as needed, security review required before approval.

**Implementation Note**: Approved software list management, category definitions, and review procedures are defined in ISMS-IMP-A.8.1-7-18-19-S4 (Software Control Process).

### Software Approval Process (Mandatory)

[Organization] SHALL implement software approval process before deployment.

**Approval Process Components**:

- Software request with business justification
- Security review (vulnerability assessment, vendor reputation, privacy review, license compliance)
- Approval decision (approved, approved with conditions, denied)
- Deployment (centralized deployment preferred, user self-installation if approved)


**Approval SLA**: Standard request 5 business days, urgent request 2 business days (manager approval), emergency request 1 business day (CISO approval). When CISO is unavailable, emergency approval authority delegates to: (1) Deputy CISO, (2) IT Director, or (3) designated Security Manager, with retrospective CISO review within 5 business days.

**Implementation Note**: Approval workflow design, security review procedures, and deployment methods are defined in ISMS-IMP-A.8.1-7-18-19-S4 (Software Control Process).

### Change Control Integration (Mandatory)

[Organization] SHALL subject software installations on production systems to change control procedures.

**Change Control Requirements**: Software deployment classified as change, change request submitted, impact assessment required, approval required (Change Advisory Board for significant changes), testing required (pilot deployment), rollback plan documented.

**Exceptions**: Emergency security patches (expedited change), pre-approved standard changes (OS updates, anti-malware updates), user-installed approved software (already approved, low impact).

**Implementation Note**: Change control integration, change classification, and approval workflows are defined in ISMS-IMP-A.8.1-7-18-19-S4 (Software Control Process).

### Unauthorized Software Detection (Mandatory)

[Organization] SHALL detect and remove unauthorized software.

**Detection Methods**: Software inventory scans (daily via endpoint management platform), application control alerts (unauthorized execution attempts), network traffic analysis, user reports.

**Unauthorized Software Includes**: Software not on approved list, prohibited software (explicitly forbidden), malware, unapproved versions of approved software, shadow IT (unapproved cloud services).

**Remediation Timeline**: Prohibited/malicious software removed within 24 hours, unapproved software removed within 7 days (or approved if legitimate business need).

**Implementation Note**: Detection procedures, remediation workflows, and root cause analysis are defined in ISMS-IMP-A.8.1-7-18-19-S4 (Software Control Process).

### Application Control Technology (Mandatory)

[Organization] SHALL implement application control technologies to restrict software execution.

**Application Control Approaches**:

- Whitelisting (preferred): Only approved software allowed to execute, default deny for all other executables
- Blacklisting (supplemental): Known malicious/prohibited software blocked, default allow for everything else


**Application Control Scope**: Executables (.exe, .com, .bat, .ps1), scripts (PowerShell, VBScript, JavaScript), libraries (DLLs, dylibs, .so files), installer packages (MSI, PKG, DEB, RPM), browser extensions and add-ons.

**Enforcement**:

- Corporate laptops/desktops: Whitelisting enforced (mandatory)
- BYOD devices: Containerized apps only (corporate container whitelisting)
- Servers: Strict whitelisting (change control required for new software)


**Implementation Note**: Application control technology selection, whitelisting rule configuration, and enforcement mechanisms are defined in ISMS-IMP-A.8.1-7-18-19-S4 (Software Control Process).

### Software Vulnerability Management (Mandatory)

[Organization] SHALL keep installed software current with security patches and updates.

**Patching Requirements**:

- Critical security patches: Installed within 7 days of release
- High-severity patches: Installed within 30 days of release
- Medium/low-severity patches: Installed within 90 days of release
- Zero-day exploits: Emergency patching (within 24-48 hours)


**Software Lifecycle Management**: End-of-life software identified and replaced before vendor support ends, unsupported software flagged as high risk with compensating controls required.

**Integration**: Software vulnerability management integrates with ISMS-POL-A.8.8 (Vulnerability Management).

**Implementation Note**: Patch management procedures, testing requirements, and lifecycle tracking are defined in ISMS-IMP-A.8.1-7-18-19-S4 (Software Control Process) and ISMS-POL-A.8.8.

### BYOD Software Control (Conditional)

[Organization] SHALL implement software controls for corporate data access on BYOD devices (if BYOD program implemented).

**BYOD Software Approach**:

- Containerized apps: Corporate apps installed in managed container (MAM solution)
- No personal app inventory: [Organization] does not inventory or control personal apps (privacy)
- Container-only controls: Application control applied to corporate container only
- Personal app restrictions: No restrictions on personal app installation (user privacy), corporate data cannot be copied to personal apps (DLP controls)


**Implementation Note**: BYOD software control design, MAM configuration, and DLP integration are defined in ISMS-IMP-A.8.1-7-18-19-S4 (Software Control Process).

---

# Roles & Responsibilities

## Accountability Matrix (RACI)

| Role | A.8.1 Endpoints | A.8.7 Malware | A.8.18 Utilities | A.8.19 Software | Overall Framework |
|------|----------------|---------------|------------------|-----------------|-------------------|
| **CISO** | Accountable | Accountable | Accountable | Accountable | Accountable |
| **IT Security Manager** | Responsible | Responsible | Responsible | Responsible | Responsible |
| **Endpoint Administrators** | Responsible | Responsible | Consulted | Consulted | Responsible |
| **Security Operations (SOC)** | Consulted | Responsible | Responsible | Consulted | Consulted |
| **IT Service Desk** | Informed | Informed | Informed | Informed | Informed |
| **End Users** | Responsible (compliance) | Informed | Informed | Informed | Responsible (compliance) |
| **Asset Management** | Consulted | Informed | Informed | Informed | Consulted |
| **Change Management** | Consulted | Informed | Consulted | Responsible (approvals) | Consulted |

**RACI Legend**: R = Responsible (executes), A = Accountable (decision authority), C = Consulted (input sought), I = Informed (kept updated)

## Key Roles

**Chief Information Security Officer (CISO)**:

- Overall accountability for endpoint security framework
- Approve endpoint security policy and major exceptions
- Allocate resources for endpoint security implementation
- Executive reporting on endpoint security posture
- Risk acceptance for endpoint security gaps


**IT Security Manager**:

- Day-to-day management of endpoint security controls
- Implement and maintain endpoint security framework
- Coordinate endpoint security assessments
- Manage endpoint security incidents
- Report compliance status to CISO
- Recommend policy updates and control improvements


**Endpoint Administrators**:

- Deploy and configure endpoint management platforms
- Enforce security baselines and configurations
- Manage endpoint encryption deployment
- Perform endpoint inventory management
- Troubleshoot endpoint security issues
- Implement endpoint security patches and updates


**Security Operations Center (SOC)**:

- Monitor anti-malware/EDR alerts
- Triage and respond to malware incidents
- Investigate security events on endpoints
- Coordinate incident response for endpoint compromises
- Monitor privileged utility usage for anomalies
- Escalate critical endpoint security events


**End Users**:

- Comply with endpoint security requirements
- Report lost/stolen devices immediately
- Report suspected malware or security incidents
- Attend security awareness training
- Maintain physical security of assigned endpoints
- Do not attempt to bypass security controls


**Detailed RACI Matrix**: Complete roles and responsibilities matrix documented in ISMS-IMP-A.8.1-7-18-19 Implementation Guides.

---

# Integration & Implementation

## Integration with Other ISMS Controls

**Critical Integration Points**:

| Related Control | Integration Point | Dependency |
|----------------|-------------------|------------|
| **A.5.9 - Asset Inventory** | Endpoint inventory feeds asset inventory | Endpoint devices = information assets |
| **A.8.2 - Privileged Access Rights** | Privileged utility access is subset of privileged access management | Privileged utility users require governance |
| **A.8.3 - Information Access Restriction** | Endpoint authentication enforces access restrictions | BYOD containerization separates data |
| **A.8.5 - Secure Authentication** | Endpoint authentication implements secure authentication | MFA for endpoints and privileged utilities |
| **A.8.8 - Vulnerability Management** | Software patching remediates endpoint vulnerabilities | Vulnerability scanning identifies unpatched software |
| **A.8.9 - Configuration Management** | Endpoint baselines are managed configurations | Baseline drift = configuration deviation |
| **A.8.15 - Logging** | Endpoint security events logged centrally | Privileged utility usage logs feed SIEM |
| **A.8.16 - Monitoring** | Endpoint security monitoring implements monitoring activities | SOC monitors endpoint security events |
| **A.8.20-22 - Network Security** | Endpoint network security complements network infrastructure security | NAC verifies endpoint compliance |
| **A.6.7 - Remote Working** | Remote endpoints have additional security requirements | VPN enforcement, stronger encryption |
| **A.5.23 - Cloud Services** | Cloud-delivered anti-malware/EDR are cloud services | Cloud security policy defines approval process |

**Implementation Note**: Detailed integration mapping, evidence overlap, and coordination procedures are defined in ISMS-IMP-A.8.1-7-18-19-S6 (Endpoint Security Assessment).

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.8.1-7-18-19 Suite):

- **ISMS-IMP-A.8.1-7-18-19-S1**: Endpoint Discovery Process
- **ISMS-IMP-A.8.1-7-18-19-S2**: Security Baseline Implementation
- **ISMS-IMP-A.8.1-7-18-19-S3**: Malware Protection Deployment
- **ISMS-IMP-A.8.1-7-18-19-S4**: Software Control Process
- **ISMS-IMP-A.8.1-7-18-19-S5**: Privileged Utility Management
- **ISMS-IMP-A.8.1-7-18-19-S6**: Endpoint Security Assessment


**Assessment Workbooks** (Generated by Python scripts):

- Endpoint_Inventory.xlsx (via generate_a817_1_endpoint_inventory.py)
- Protection_Coverage.xlsx (via generate_a817_2_protection_coverage.py)
- Software_Controls.xlsx (via generate_a817_3_software_controls.py)
- Privileged_Utilities.xlsx (via generate_a817_4_privileged_utilities.py)
- Endpoint_Security_Compliance_Matrix.xlsx (via generate_a817_5_compliance_matrix.py)
- Endpoint_Security_Dashboard.xlsx (via generate_a817_6_compliance_dashboard.py)


**Note**: Implementation resource updates (ISMS-IMP suite, assessment scripts) do not require policy revision.

**Script Accuracy Verification Controls**:

- **Version Control**: All generator scripts maintained in version control with change history and approval tracking
- **Sanity Check Scripts**: Each workbook type has corresponding sanity check script (50_sanity/) that validates structure, required sheets, and data integrity
- **Normalization Scripts**: Normalization scripts (11_normalize/) ensure consistent formatting and styling across generated workbooks
- **Test Execution**: Scripts tested against known baselines before deployment; output compared to expected results
- **Peer Review**: Script modifications require peer review before merge to production branch
- **Output Validation**: Generated workbooks validated against expected sheet structures, data validation rules, and formula integrity
- **Change Documentation**: Script changes documented with QA verification tags (QA_VERIFIED date, QA_STATUS, CHANGES log)


## Assessment & Verification

**Assessment Frequency**:

- Continuous: Automated compliance monitoring via MDM (daily)
- Weekly: Baseline compliance scans, inventory updates, signature verification
- Monthly: Comprehensive compliance reporting (all metrics)
- Quarterly: Executive dashboard and trend analysis
- Annual: Full assessment, auditor review, policy review


**Compliance Scoring**: Per-control scoring for A.8.1, A.8.7, A.8.18, A.8.19 enables independent SoA assessment. Overall endpoint security score provides consolidated view for executive reporting.

**Compliance Thresholds**:

- ✅ Compliant (Green): ≥90%
- ⚠️ Partial Compliance (Yellow): 70-89%
- ❌ Non-Compliant (Red): <70%


**Evidence Requirements**: Mandatory evidence artifacts documented in ISMS-IMP-A.8.1-7-18-19-S6 (Endpoint Security Assessment).

**Implementation Note**: Assessment methodology, scoring formulas, evidence collection procedures, and gap management are defined in ISMS-IMP-A.8.1-7-18-19-S6 (Endpoint Security Assessment).

## Exception Management

**When Exceptions Required**: Technical limitation prevents compliance, business requirement conflicts with security control, cost-benefit analysis favors alternative control, temporary exception during migration/upgrade.

**Exception Approval Authority**:

- Low Risk: IT Security Manager
- Medium Risk: CISO (risk assessment required)
- High Risk: CISO + Risk Committee (compensating controls mandatory, executive notification)
- Permanent Exceptions: CISO + Risk Committee (annual recertification required)


**Compensating Controls**: Required for all exceptions. Compensating controls reduce risk when primary control cannot be implemented.

**Exception Tracking and Review**: All approved exceptions documented in centralized exception register, temporary exceptions reviewed monthly, permanent exceptions reviewed annually, high-risk exceptions reviewed quarterly.

**Implementation Note**: Exception request procedures, approval workflows, compensating control requirements, and exception tracking are defined in ISMS-IMP-A.8.1-7-18-19-S6 (Endpoint Security Assessment).

## Regulatory Mapping

This policy addresses endpoint security requirements from multiple regulatory frameworks:

| Requirement Category | Swiss nDSG | EU GDPR | ISO 27001 | PCI DSS* | HIPAA* | FINMA* | DORA/NIS2* |
|---------------------|-----------|---------|-----------|---------|--------|--------|------------|
| **Endpoint Inventory** | Art. 8 | Art. 32 | A.8.1 | Req. 2, 11 | §164.310(d)(1) | Risk-Based | Asset Management |
| **Encryption** | Art. 8 | Art. 32 | A.8.1 | Req. 3 | §164.312(a)(2)(iv) | Risk-Based | Data Protection |
| **Malware Protection** | Art. 8 | Art. 32 | A.8.7 | Req. 5 | §164.308(a)(5)(ii)(B) | Risk-Based | Cyber Resilience |
| **Access Controls** | Art. 8 | Art. 32 | A.8.18 | Req. 7, 8 | §164.312(a)(1) | Risk-Based | Access Management |
| **Software Controls** | Art. 8 | Art. 32 | A.8.19 | Req. 6 | §164.308(a)(5)(ii)(B) | Risk-Based | Change Management |
| **Logging & Monitoring** | Art. 8 | Art. 32 | A.8.15, A.8.16 | Req. 10 | §164.308(a)(1)(ii)(D) | Risk-Based | Security Monitoring |

*Conditional applicability per ISMS-POL-00

**Note**: Specific regulatory interpretation and compliance verification procedures are documented in ISMS-IMP-A.8.1-7-18-19-S6 (Endpoint Security Assessment).

## Training & Awareness

**Security Awareness** (All Personnel):

- Annual training module on endpoint security and user responsibilities
- User responsibilities for physical security, reporting lost/stolen devices, malware recognition
- Training completion: ≥95% annually


**Technical Training** (IT Operations, Endpoint Administrators):

- Endpoint management platform configuration and operation
- Security baseline deployment and enforcement
- Anti-malware/EDR configuration and monitoring
- Incident response procedures
- Exception request evaluation


**Privacy Training** (DPO Office, Legal/Compliance):

- BYOD program privacy protections
- User privacy rights and organizational limitations
- Data subject erasure request handling (endpoint data removal)


**Management Training** (Data Owners, System Owners, Management):

- Endpoint security governance and risk assessment
- Exception approval decision-making
- Compliance reporting interpretation


**Implementation Note**: Training content, delivery methods, and effectiveness measurement are defined in ISMS-IMP-A.8.1-7-18-19 Implementation Guides.

---

# Definitions

**Endpoint Device**: Any user-facing device that stores, processes, or accesses organizational information (laptops, desktops, mobile devices, tablets, IoT devices).

**EDR (Endpoint Detection and Response)**: Advanced endpoint security solution providing real-time monitoring, threat detection, investigation, and automated response capabilities beyond traditional antivirus.

**MAM (Mobile Application Management)**: Management of corporate applications on mobile devices, especially BYOD scenarios, allowing corporate app/data control while preserving user privacy.

**MDM (Mobile Device Management)**: Centralized management of mobile devices, enforcing security policies, deploying configurations, and enabling remote wipe capabilities.

**Privileged Utility Program**: Software tool capable of overriding or bypassing system and application security controls (e.g., registry editors, debuggers, administrative tools).

**BYOD (Bring Your Own Device)**: Program allowing employees to use personal devices for work purposes, subject to security and privacy controls.

**Security Baseline**: Minimum security configuration requirements for endpoints, typically aligned with vendor security guides (Microsoft, Apple) and CIS Benchmarks.

**Application Control (Whitelisting)**: Security control that allows only explicitly approved software to execute, blocking all other executables by default.

**Full Disk Encryption (FDE)**: Encryption of entire disk volume(s), protecting data at rest from unauthorized physical access.

**Tamper Protection**: Anti-malware feature preventing malware or unauthorized users from disabling, modifying, or uninstalling security software.

**Zero-Day Threat**: Previously unknown malware or exploit, not yet detected by signature-based antivirus, requiring behavioral or ML-based detection.

**Configuration Drift**: Deviation from approved security baseline configuration, typically caused by manual changes, software updates, or policy inconsistencies.

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **IT Operations Manager** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (CEO)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements. Implementation procedures are documented in ISMS-IMP-A.8.1-7-18-19.*
<!-- QA_VERIFIED: 2026-02-01 -->
