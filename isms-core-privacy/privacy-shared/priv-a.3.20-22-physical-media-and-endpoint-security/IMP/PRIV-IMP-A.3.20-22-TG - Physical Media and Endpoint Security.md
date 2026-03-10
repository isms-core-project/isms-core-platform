<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.20-22-TG:privacy:TG:a.3.20-22 -->
**PRIV-IMP-A.3.20-22-TG — Physical Media and Endpoint Security — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Physical Media and Endpoint Security — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.3.20-22-TG |
| **Related Policy** | PRIV-POL-A.3.20-22 (Physical Media and Endpoint Security) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant technical or regulatory change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.3.20-22 (Physical Media and Endpoint Security — the governing policy)
- PRIV-IMP-A.3.20-22-UG (Physical Media and Endpoint Security — User Guide)
- PRIV-IMP-A.3.23-31-TG (Technical Security Controls — encryption and key management standards)
- ISMS-POL-A.8.1 (User Endpoint Devices — ISMS parallel)

---

## Purpose of This Guide

This guide provides the **technical structures, register schemas, configuration standards, and templates** for physical media lifecycle management, equipment disposal, and endpoint device protection. It covers:

- Media Register schema
- Media Transportation Log schema
- Disposal Register schema
- Approved erasure method reference table
- Endpoint configuration minimum standards
- BYOD PII Agreement template
- Remote Wipe Test Record template

**Audience**: CISO, IT Security Team, DPO.

---

## 1. Media Register

The Media Register is maintained by IT Security Team with DPO oversight. It covers all removable storage media capable of containing PII.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Media ID | Text | Unique identifier (e.g., MED-2026-001) |
| Media Type | Enum | USB Drive / Portable HDD / Portable SSD / Optical Media / Backup Tape / SD Card / Other |
| Description | Text | Make, model, capacity (e.g., "SanDisk 128GB USB 3.0") |
| Serial Number | Text | Manufacturer serial number or asset tag |
| Owner | Text | Accountable individual or team |
| Department | Text | Business unit responsible |
| Acquisition Date | Date | Date acquired or first registered |
| Classification | Enum | Not Classified / INTERNAL / CONFIDENTIAL / RESTRICTED |
| Classification Date | Date | Date classification was assigned |
| PII Content Confirmed | Boolean | Yes / No / Unknown |
| PII Categories | Multi-select | Ordinary / Financial / Special Category / Sensitive / Unknown |
| Encryption Status | Enum | Hardware Encrypted / Software Encrypted / Not Encrypted / Not Applicable |
| Encryption Key Reference | Text | Key management system reference (where applicable) |
| Status | Enum | Active / In Transport / In Storage / Decommissioned / Disposed |
| Disposal Date | Date | If disposed: date of disposal |
| Disposal Method | Text | Erasure method or physical destruction method |
| Disposal Verification | Enum | Verified / Not Verified / Destruction Certificate Obtained |
| Disposal Reference | Text | Certificate of destruction reference or erasure tool log reference |
| Notes | Text | Outstanding actions, audit flags, transport entries |

---

## 2. Media Transportation Log

Maintained by IT Security Team. An entry is created whenever CONFIDENTIAL or RESTRICTED PII media is transported outside secure premises.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Transport ID | Text | Unique reference (e.g., TRANS-2026-001) |
| Media ID | Text | Reference to Media Register |
| Requester | Text | Name and role of person authorising/conducting transport |
| Departure Date | Date | Date medium left secure premises |
| Destination | Text | Organisation and location of destination |
| Purpose | Text | Reason for transport (e.g., offsite backup delivery, client data delivery) |
| Courier / Escort | Text | Courier service name or employee name escorting the medium |
| Expected Return Date | Date | Planned date of return (if applicable) |
| Actual Return Date | Date | Confirmed date of return |
| Return Condition | Enum | Intact / Damaged / Not Returned |
| Escalation Triggered | Boolean | Yes / No (Yes if not returned by expected date) |
| Notes | Text | Incident reference if loss reported; any deviations |

---

## 3. Disposal Register

Maintained by IT Security Team. An entry is created for every item of equipment disposed of or reassigned.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Disposal ID | Text | Unique reference (e.g., DISP-2026-001) |
| Asset ID | Text | IT asset management reference for the equipment |
| Equipment Type | Enum | Laptop / Desktop / Server / Printer / Mobile Device / External Drive / Tape Drive / Other |
| Make / Model | Text | Equipment description |
| PII Status | Enum | PII Confirmed Present / PII Possibly Present / No PII Confirmed / Unknown |
| PII Classification | Enum | RESTRICTED / CONFIDENTIAL / INTERNAL / Not Applicable |
| Previous User(s) | Text | User(s) who had PII access on this device |
| Erasure Method | Enum | Software Overwrite (NIST Clear) / Software Overwrite (Purge) / Cryptographic Erasure / Physical Destruction / Factory Reset (for printers/network) / No PII — No Erasure Required |
| Erasure Tool / Standard | Text | Tool name and version, or destruction service name |
| Erasure Date | Date | Date erasure was performed |
| Verification Outcome | Enum | Pass / Fail / Not Verified |
| Verification Tool | Text | Post-erasure verification tool name (if used) |
| Disposal Type | Enum | Internal Reassignment / Sale / Donation / Recycling / Physical Destruction / Return to Vendor |
| Disposal Date | Date | Date device was disposed of or reassigned |
| Third-Party Disposal Agent | Text | Name of recycler, reseller, or charity (if applicable) |
| Certificate of Destruction | Boolean | Yes / No / Not Required |
| Certificate Reference | Text | Destruction certificate document reference |
| Responsible Person | Text | IT Security Team member executing the disposal |
| DPO Notified | Boolean | Yes / No (required for RESTRICTED PII equipment) |
| Notes | Text | Exceptional circumstances, escalations |

---

## 4. Approved Erasure Methods

Reference table for selecting the appropriate erasure method:

| Media Type | PII Classification | Approved Methods (in order of preference) |
|------------|-------------------|-------------------------------------------|
| HDD (traditional hard drive) | RESTRICTED | Physical destruction (shredding / degaussing) |
| HDD | CONFIDENTIAL / INTERNAL | NIST SP 800-88 Purge (7-pass overwrite) OR Physical destruction |
| SSD / NVMe / Flash | RESTRICTED | Physical destruction |
| SSD / NVMe / Flash | CONFIDENTIAL / INTERNAL | Cryptographic erasure (if FDE confirmed throughout life) OR Physical destruction — do NOT use standard software overwrite |
| USB Drive / SD Card | RESTRICTED | Physical destruction |
| USB Drive / SD Card | CONFIDENTIAL / INTERNAL | Cryptographic erasure (if hardware encrypted) OR Physical destruction |
| Backup Tape | Any | Physical destruction (degaussing confirmed effective + shredding) |
| Optical Media (CD/DVD) | Any | Physical destruction (cross-cut shredding or specialist media destroyer) |
| Printer Internal Storage | Any | Manufacturer-specified factory reset + security wipe mode; verify with manufacturer documentation |
| Mobile Device (iOS/Android) | Any | Cryptographic erase (factory reset via MDM remote wipe) — confirm encryption was active throughout device life |

**NIST SP 800-88 summary**:
- **Clear**: Software overwrite; suitable for media remaining in the same security domain
- **Purge**: More thorough overwrite or degaussing; suitable for media leaving the organisation's control
- **Destroy**: Physical destruction; required for RESTRICTED PII and media where other methods are uncertain

---

## 5. Endpoint Configuration Minimum Standards

CISO configures and maintains these standards for all corporate endpoints accessing PII systems. Reviewed annually.

### Encryption

| Device Type | Required Standard | Acceptable Implementation |
|-------------|-----------------|--------------------------|
| Laptop (Windows) | Full-disk encryption | BitLocker (TPM 2.0) with AES-256 |
| Laptop (macOS) | Full-disk encryption | FileVault 2 |
| Desktop with PII access | Full-disk encryption | BitLocker (Windows) / FileVault (macOS) |
| Mobile device (iOS) | Device encryption (built-in) | Enable hardware encryption + 6+ digit passcode |
| Mobile device (Android) | Full-disk encryption | Android built-in encryption enabled |
| BYOD managed workspace | Container encryption | MDM-enforced container with AES-256 |

### Screen Lock

| Setting | Minimum Value | Configured Standard |
|---------|--------------|---------------------|
| Automatic lock timeout (laptops/desktops) | 5 minutes | [Organisation to set] |
| Automatic lock timeout (mobile devices) | 2 minutes | [Organisation to set] |
| Screen lock authentication (laptops) | Password or biometric | [Organisation to set] |
| Failed attempts before device wipe (mobile) | ≤ 10 | [Organisation to set] |

### Endpoint Management (MDM/UEM)

All endpoints with PII access must be enrolled in [Organisation]'s MDM/UEM solution. Minimum capabilities enforced through MDM:

| Capability | Required |
|-----------|---------|
| Remote wipe (full device or managed workspace) | Mandatory |
| Remote lock | Mandatory |
| Encryption compliance enforcement | Mandatory |
| OS patch compliance monitoring | Mandatory |
| Application policy enforcement | Mandatory |
| Jailbreak/root detection | Required for mobile devices |

### Remote Wipe Test Record

Complete this record each time a remote wipe capability test is conducted:

```
REMOTE WIPE CAPABILITY TEST RECORD

Test Reference: RWTEST-[YYYY]-[NNN]
Test Date: [Date]
Conducted By (IT Security Team): [Name]
Approved By (CISO): [Name]

Test Device: [Make / Model / Asset ID] — designated test device (NOT production device)
MDM/UEM Platform: [Platform name and version]

TEST PROCEDURE
1. Device enrolled in MDM and encryption confirmed active: [ ] Yes
2. Remote wipe command issued from MDM console at [Time]: [ ] Confirmed
3. Device confirmed wiped / reset to factory state at [Time]: [ ] Confirmed
4. Post-wipe verification: [ ] No previous data recoverable / [ ] Partial wipe — see notes
5. Time from command to confirmed wipe: [Number] minutes

OUTCOME
[ ] Pass — remote wipe capability confirmed functional
[ ] Fail — see notes; escalate to CISO immediately

CISO Sign-off: _________________________ Date: _____________
Next test due: [Date + 12 months]
```

---

## 6. BYOD PII Agreement Template

```
BYOD PERSONAL DEVICE — PII ACCESS AGREEMENT

Personnel Name: _____________________________________________
Role: _____________________________________________
Personal Device: Make [_____] Model [_____] OS [_____]
Device ID (MDM): [To be assigned on enrolment]
Date: _____________________________________________

I agree to the following conditions as a prerequisite for accessing
[Organisation]'s PII systems from my personal device:

1. MANAGED WORKSPACE
My personal device will be enrolled in [Organisation]'s MDM/containerisation
solution. A managed workspace will be created on my device, segregated from
my personal data. PII will only be accessed within this managed workspace.

2. MINIMUM SECURITY REQUIREMENTS
I confirm my device meets the following minimum requirements:
- [ ] Device encryption is enabled
- [ ] Screen lock with PIN/password/biometric is enabled
- [ ] Operating system is current (within [X] months of latest release)
- [ ] I will not jailbreak or root the device while enrolled

3. REMOTE WIPE AUTHORITY
I acknowledge and agree that [Organisation] has the right to remotely wipe
the managed workspace on my device if:
- The device is reported lost or stolen
- My employment or engagement is terminated
- A security incident requires immediate containment
I understand that remote wipe applies to the managed workspace only and will
not affect my personal data outside the managed container.

4. PII HANDLING
I will access and handle PII only within the managed workspace. I will not
copy, store, or share PII outside the managed workspace on this device.

5. INCIDENT REPORTING
I will report loss or suspected compromise of this device to IT Security Team
and my manager immediately upon discovery.

Personnel Signature: _________________________ Date: _____________
IT Security Team (MDM Enrolment Confirmed): __________ Date: _____________
DPO Awareness: [ ] Notified
```

---

<!-- QA_VERIFIED: [Date] -->
