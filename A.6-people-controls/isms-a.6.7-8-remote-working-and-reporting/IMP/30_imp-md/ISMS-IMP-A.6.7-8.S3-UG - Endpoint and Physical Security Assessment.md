**ISMS-IMP-A.6.7-8.S3-UG - Endpoint and Physical Security Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S3-UG |
| **Version** | 1.0 |
| **Assessment Area** | Device Security, Encryption, Endpoint Protection, Physical Security |
| **Related Policy** | ISMS-POL-A.6.7-8, Sections 2.2 (Physical Security) & 2.5 (Device Security) |
| **Purpose** | Guide users through assessment of endpoint security controls and physical security for remote work |
| **Target Audience** | IT Security Team, Endpoint Management Team, Desktop Support, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly (technical), Annual (physical) |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for endpoint and physical security assessment | ISMS Implementation Team |

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.6.7-8.S3-TG.

---

**Audience:** IT Security Team, Endpoint Management Team, Desktop Support

---

## 1. Assessment Overview

#### 1.1 Purpose

This assessment workbook evaluates endpoint security controls and physical security requirements for remote work environments, ensuring that:
- Remote devices meet security baseline requirements
- Full-disk encryption is deployed on all remote devices
- Endpoint protection (EDR/antivirus) is active and current
- Patch management covers remote devices
- Physical security guidance is provided and acknowledged
- BYOD controls are appropriate where personal devices are permitted

#### 1.2 Scope

This assessment covers:
- Corporate device security baseline compliance
- Personal device (BYOD) security requirements
- Encryption status (full-disk, file-level)
- Endpoint protection deployment and currency
- Patch management for remote devices
- Physical security requirements for home offices
- Device inventory and tracking
- Lost/stolen device procedures

#### 1.3 Target Audience

- **Primary Assessors**: IT Security Team, Endpoint Management Team
- **Data Contributors**: IT Operations, Desktop Support
- **Reviewers**: IT Security Manager
- **Approvers**: CISO

#### 1.4 Assessment Frequency

| Trigger | Frequency |
|---------|-----------|
| Initial Assessment | Once (ISMS implementation) |
| Periodic Review | Quarterly for technical controls, Annual for physical security |
| Triggered Review | After device security incidents, major endpoint changes |

### 2. Prerequisites

Before starting this assessment, ensure:

| Prerequisite | Status | Notes |
|--------------|--------|-------|
| Access to endpoint management console | ☐ | MDM/UEM platform |
| Access to EDR/antivirus management | ☐ | Protection status |
| Access to patch management system | ☐ | Compliance reports |
| Device inventory data | ☐ | All remote devices |
| BYOD policy documentation | ☐ | If BYOD is permitted |
| Physical security guidelines | ☐ | Home office requirements |

### 3. Assessment Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: Device Inventory & Classification                    │
│  - Inventory all remote-capable devices                         │
│  - Classify by ownership (corporate/BYOD)                       │
│  - Identify high-risk device types                              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 2: Security Baseline Assessment                          │
│  - Assess encryption status                                     │
│  - Verify endpoint protection                                   │
│  - Check patch compliance                                       │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 3: BYOD Assessment (if applicable)                       │
│  - Review BYOD enrollment                                       │
│  - Verify security requirements met                             │
│  - Assess containerization/separation                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 4: Physical Security Assessment                          │
│  - Review physical security guidance                            │
│  - Sample acknowledgment verification                           │
│  - Assess lost/stolen device procedures                         │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 5: Gap Analysis & Evidence Collection                    │
│  - Document gaps identified                                     │
│  - Collect compliance evidence                                  │
│  - Prepare remediation recommendations                          │
└─────────────────────────────────────────────────────────────────┘
```

### 4. Sheet-by-Sheet Completion Guide

#### 4.1 Instructions Sheet

**Purpose**: Provides guidance for workbook users.

#### 4.2 Device_Inventory Sheet

**Purpose**: Catalog all devices used for remote work.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Device ID | Unique device identifier | Auto-generated |
| Device Type | Laptop/Desktop/Tablet/Mobile | Dropdown |
| Ownership | Corporate/BYOD/Contractor | Dropdown |
| OS | Operating system | Free text |
| OS Version | Current OS version | Free text |
| Assigned User | User the device is assigned to | Free text |
| Department | User's department | Free text |
| Remote Enabled | Used for remote work | Yes/No |
| MDM Enrolled | Enrolled in device management | Yes/No |
| Last Check-in | Last MDM check-in date | Date |
| Status | Active/Inactive/Lost/Retired | Dropdown |

#### 4.3 Encryption_Status Sheet

**Purpose**: Verify encryption deployment on remote devices.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Device ID | Reference to Device_Inventory | Reference |
| Encryption Type | BitLocker/FileVault/LUKS/Other | Dropdown |
| Full-Disk Encrypted | Entire disk encrypted | Yes/No |
| Encryption Status | Active/Suspended/Not Configured | Dropdown |
| Recovery Key Escrowed | Key stored centrally | Yes/No |
| Last Verified | When encryption was verified | Date |
| Compliant | Meets encryption requirements | Formula |
| Notes | Additional observations | Free text |

**Compliance Logic**:
- Corporate devices: Full-disk encryption required, key escrowed
- BYOD: Full-disk or containerized work data encrypted
- Mobile: Device encryption or container encryption

#### 4.4 Endpoint_Protection Sheet

**Purpose**: Assess endpoint protection (EDR/antivirus) deployment.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Device ID | Reference to Device_Inventory | Reference |
| Protection Solution | Name of EDR/AV solution | Free text |
| Agent Installed | Protection agent present | Yes/No |
| Agent Version | Current agent version | Free text |
| Agent Status | Active/Disabled/Outdated | Dropdown |
| Definitions Date | Last signature/definition update | Date |
| Last Scan | Last full scan date | Date |
| Threats Detected | Any threats in last 90 days | Number |
| Compliant | Meets protection requirements | Formula |
| Notes | Additional observations | Free text |

#### 4.5 Patch_Compliance Sheet

**Purpose**: Assess patch management compliance for remote devices.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Device ID | Reference to Device_Inventory | Reference |
| OS Patch Level | Current OS patch date | Date |
| Critical Patches Missing | Count of critical patches missing | Number |
| High Patches Missing | Count of high patches missing | Number |
| Medium Patches Missing | Count of medium patches missing | Number |
| Last Patch Scan | When device was last scanned | Date |
| Days Since Last Patch | Days since last patch installed | Calculated |
| Compliant | Within patch policy requirements | Formula |
| Notes | Specific missing patches or issues | Free text |

**Compliance Thresholds**:
- Critical patches: Must be applied within 14 days
- High patches: Must be applied within 30 days
- Medium patches: Must be applied within 90 days
- Zero critical/high patches missing = Compliant

#### 4.6 BYOD_Assessment Sheet

**Purpose**: Assess security of personal devices used for work (if BYOD permitted).

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Device ID | BYOD device identifier | Auto-generated |
| Device Type | Type of personal device | Dropdown |
| Owner | Device owner (user) | Free text |
| OS/Version | Operating system and version | Free text |
| Minimum OS Met | Meets minimum OS requirements | Yes/No |
| MDM Enrolled | Enrolled in MDM | Yes/No |
| Container Installed | Work container/profile active | Yes/No |
| Device Encrypted | Device-level encryption active | Yes/No |
| Remote Wipe Enabled | Can org data be wiped remotely | Yes/No |
| BYOD Agreement Signed | User signed BYOD agreement | Yes/No |
| Compliant | Meets BYOD requirements | Formula |
| Notes | Observations | Free text |

#### 4.7 Physical_Security Sheet

**Purpose**: Assess physical security requirements and acknowledgments.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Requirement Category | Category of physical security | Pre-populated |
| Requirement | Specific requirement | Pre-populated |
| Documented | Is requirement documented in policy/guidance | Yes/No |
| Communicated | Has it been communicated to remote workers | Yes/No |
| Acknowledgment Required | Is acknowledgment required | Yes/No |
| Acknowledgment Captured | Are acknowledgments on file | Yes/No/Partial |
| Verification Method | How is this verified | Free text |
| Compliant | Overall compliance | Formula |
| Notes | Observations | Free text |

**Physical Security Categories**:
- Screen privacy (positioning, privacy screens)
- Secure storage (lockable cabinet/drawer)
- Device security (cable locks, not left unattended)
- Document handling (shredding, secure disposal)
- Visitor/family access restrictions
- Clear desk requirements
- Equipment during travel

#### 4.8 Lost_Stolen_Procedures Sheet

**Purpose**: Assess procedures for lost or stolen devices.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Procedure Element | Component of lost/stolen process | Pre-populated |
| Requirement | What should be in place | Pre-populated |
| Implemented | Is this implemented | Yes/No/Partial |
| Documentation | Where is this documented | Free text |
| Last Tested | When was procedure last tested | Date |
| Responsible Party | Who executes this step | Free text |
| SLA | Expected timeframe | Free text |
| Evidence | Evidence of implementation | Free text |
| Compliant | Meets requirements | Formula |

**Procedure Elements**:
- Reporting channel (24/7 availability)
- Immediate account disable capability
- Remote lock capability
- Remote wipe capability
- Recovery key access
- Replacement device process
- Incident documentation
- Follow-up investigation

#### 4.9 Gap_Analysis Sheet

**Purpose**: Consolidate all endpoint and physical security gaps.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Gap ID | Unique identifier (GAP-EPS-###) | Auto-generated |
| Source Sheet | Which sheet identified gap | Reference |
| Gap Description | Clear description of the gap | Free text |
| Scope | Number of devices/users affected | Free text |
| Risk Level | Risk if gap not addressed | Dropdown |
| Remediation Action | Recommended fix | Free text |
| Owner | Who will remediate | Free text |
| Target Date | Remediation deadline | Date |
| Status | Current status | Dropdown |

#### 4.10 Evidence_Register Sheet

**Purpose**: Catalog all evidence collected.

#### 4.11 Dashboard Sheet

**Purpose**: Provide executive summary.

**Metrics Displayed**:
- Total devices in inventory
- Encryption compliance rate
- Endpoint protection coverage
- Patch compliance rate
- BYOD compliance rate (if applicable)
- Physical security acknowledgment rate
- Gap count by severity

#### 4.12 Approval_Sign_Off Sheet

**Purpose**: Document formal review and approval.

### 5. Evidence Collection Guidelines

#### 5.1 Required Evidence Types

| Evidence Category | Examples |
|-------------------|----------|
| MDM Reports | Device compliance reports, encryption status |
| EDR/AV Reports | Protection status, threat detection reports |
| Patch Reports | Patch compliance dashboards, missing patch lists |
| Inventory Exports | Device inventory from MDM |
| Policy Documents | BYOD policy, physical security guidelines |
| Acknowledgments | Sample signed acknowledgments |

### 6. Common Pitfalls

#### ❌ MISTAKE #1: Only Checking Managed Devices

**The Problem:** Assessing only MDM-enrolled devices, missing unmanaged endpoints.

**Why It Matters:** Unmanaged devices may lack security controls. BYOD and contractor devices often unmanaged. Incomplete picture of endpoint security.

**The Fix:**
- Request access lists from VPN/remote access systems
- Cross-reference MDM inventory with remote access users
- Survey managers for unmanaged devices in use

#### ❌ MISTAKE #2: Relying Solely on MDM Reports

**The Problem:** Accepting MDM compliance reports without physical verification.

**Why It Matters:** MDM data may be stale. Devices may be non-compliant since last check-in. Reports don't catch all issues.

**The Fix:**
- Spot-check sample of physical devices
- Verify encryption is active (not suspended)
- Check endpoint protection is running

#### ❌ MISTAKE #3: Missing Contractor and Third-Party Devices

**The Problem:** Assessment scope limited to employee devices.

**Why It Matters:** Contractors often use personal or contractor-owned devices. These may access sensitive systems. Weaker security baseline.

**The Fix:**
- Include contractor devices in scope
- Verify contractor device security requirements in contracts
- Assess third-party device compliance

#### ❌ MISTAKE #4: Not Testing Remote Wipe Capability

**The Problem:** Assuming remote wipe works without testing.

**Why It Matters:** Wipe may fail due to configuration issues. Critical for lost/stolen response. May not work for offline devices.

**The Fix:**
- Conduct periodic wipe tests on test devices
- Verify wipe procedures documented
- Check wipe audit logs for past incidents

#### ❌ MISTAKE #5: Ignoring Mobile Devices

**The Problem:** Focusing on laptops, missing phones and tablets.

**Why It Matters:** Mobile devices access email and corporate apps. Growing attack surface. Different security controls needed.

**The Fix:**
- Include mobile devices in inventory
- Assess mobile device management (MDM)
- Check mobile app security

#### ❌ MISTAKE #6: Not Verifying Encryption Key Recovery

**The Problem:** Confirming encryption enabled but not testing key recovery.

**Why It Matters:** Lost encryption keys mean lost data. Recovery must work for business continuity. Auditors may test this.

**The Fix:**
- Test recovery key retrieval process
- Verify key escrow is functioning
- Document recovery procedures

#### ❌ MISTAKE #7: Assuming Encryption Enabled = Compliant

**The Problem:** Checking encryption is enabled but not verifying it's active and complete.

**Why It Matters:** Encryption may be paused or suspended. May only cover system drive, not data drives. Configuration may be incomplete.

**The Fix:**
- Verify encryption status is "On" not "Paused"
- Check all drives are encrypted
- Verify encryption algorithm meets requirements

#### ❌ MISTAKE #8: Skipping Physical Security Assessment

**The Problem:** Focusing only on technical controls, ignoring physical security.

**Why It Matters:** Remote workers need physical security guidance. Unsecured home offices increase risk. Physical theft is a real threat.

**The Fix:**
- Include physical security requirements in assessment
- Check for guidance on secure workspace
- Verify clean desk/screen lock requirements

---

### 7. Quality Checklist

#### Completeness Checks

- [ ] ALL remote devices inventoried (laptops, desktops, mobile, tablets)
- [ ] Corporate, BYOD, and contractor devices included
- [ ] Encryption status verified for all devices
- [ ] Endpoint protection confirmed active
- [ ] Patch compliance within thresholds
- [ ] BYOD assessment complete (if applicable)
- [ ] Physical security requirements documented
- [ ] Lost/stolen procedures verified
- [ ] All gaps documented with remediation

#### Technical Accuracy Checks

- [ ] MDM data spot-checked against physical devices
- [ ] Encryption actually active (not suspended)
- [ ] Protection software running (not disabled)
- [ ] Patch dates within SLA

#### Evidence Quality Checks

- [ ] Device inventory exported with timestamp
- [ ] Compliance reports dated
- [ ] Sample testing documented
- [ ] Evidence stored securely

---

### 8. Review and Approval Process

#### 8.1 Review Workflow

**Step 1: Self-Review** (Assessor) - Complete Quality Checklist
**Step 2: Technical Review** (IT Operations/Endpoint Team) - 2-3 days
**Step 3: Management Approval** (CISO) - 1-2 days

#### 8.2 After Approval

1. **Store Assessment:** `ISMS/Controls/A.6.7-8/Endpoint_Security/`
2. **Distribute:** IT Operations, Endpoint Team
3. **Initiate Remediation:** Create tickets for non-compliant devices
4. **Schedule Follow-Up:** Quarterly device compliance review

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
