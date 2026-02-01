**ISMS-IMP-A.6.7-8.S3 - Endpoint and Physical Security Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S3 |
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

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Sheet-by-Sheet Guidance
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formula Specifications
  - Styling Reference

**Target Audiences:**

- **Part I:** Assessment users (IT Security Team, Endpoint Management, Desktop Support)
- **Part II:** Workbook developers (Python/Excel script maintainers)

---

# PART I: USER COMPLETION GUIDE

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

| Pitfall | Avoidance Strategy |
|---------|-------------------|
| Only checking managed devices | Include unmanaged/BYOD devices |
| Relying on MDM data without verification | Spot-check physical devices |
| Missing contractor devices | Include all third-party devices |
| Not testing remote wipe capability | Conduct periodic wipe tests |
| Ignoring mobile devices | Include phones and tablets |
| Not verifying key escrow | Test recovery key retrieval |
| Assuming encryption = compliant | Verify encryption is active, not suspended |
| Missing physical security assessment | Don't skip non-technical controls |

### 7. Quality Checklist

Before submitting assessment, verify:

- [ ] All remote devices inventoried
- [ ] Encryption status verified for all devices
- [ ] Endpoint protection confirmed active
- [ ] Patch compliance within thresholds
- [ ] BYOD assessment complete (if applicable)
- [ ] Physical security requirements documented
- [ ] Lost/stolen procedures verified
- [ ] All gaps documented with remediation

---

## PART II: Technical Specification

### 8. Workbook Architecture

#### 8.1 Sheet Structure

| Sheet Name | Purpose | Sheet Type |
|------------|---------|------------|
| Instructions | User guidance | Static |
| Device_Inventory | Device catalog | Inventory |
| Encryption_Status | Encryption assessment | Assessment |
| Endpoint_Protection | EDR/AV assessment | Assessment |
| Patch_Compliance | Patch status | Assessment |
| BYOD_Assessment | Personal device assessment | Assessment |
| Physical_Security | Physical security | Assessment |
| Lost_Stolen_Procedures | Incident procedures | Assessment |
| Gap_Analysis | Consolidated gaps | Analysis |
| Evidence_Register | Evidence catalog | Register |
| Dashboard | Executive summary | Calculated |
| Approval_Sign_Off | Formal approvals | Governance |

### 9. Column Specifications

#### 9.1 Device_Inventory Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Device ID | 15 | Text | Auto (DEV-####) |
| B | Device Type | 12 | Dropdown | Laptop/Desktop/Tablet/Mobile |
| C | Ownership | 12 | Dropdown | Corporate/BYOD/Contractor |
| D | OS | 15 | Text | Free text |
| E | OS Version | 12 | Text | Free text |
| F | Assigned User | 25 | Text | Free text |
| G | Department | 20 | Text | Free text |
| H | Remote Enabled | 12 | Dropdown | Yes/No |
| I | MDM Enrolled | 12 | Dropdown | Yes/No |
| J | Last Check-in | 12 | Date | Date format |
| K | Status | 12 | Dropdown | Active/Inactive/Lost/Retired |

### 10. Formula Specifications

#### 10.1 Dashboard Calculations

**Encryption Compliance Rate**:
```
=COUNTIF(Encryption_Status!G:G,"Yes")/COUNTA(Encryption_Status!G2:G500)
```

**Endpoint Protection Coverage**:
```
=COUNTIF(Endpoint_Protection!I:I,"Yes")/COUNTA(Endpoint_Protection!I2:I500)
```

**Patch Compliance Rate**:
```
=COUNTIF(Patch_Compliance!H:H,"Yes")/COUNTA(Patch_Compliance!H2:H500)
```

### 11. Pre-Populated Content

#### 11.1 Physical Security Requirements

| Requirement Category | Requirement |
|---------------------|-------------|
| Screen Privacy | Position screen away from windows and common areas |
| Screen Privacy | Use privacy screen filter in public spaces |
| Secure Storage | Lockable cabinet or drawer for sensitive documents |
| Device Security | Cable lock or secure storage for portable devices |
| Device Security | Never leave devices unattended in public |
| Document Handling | Shred sensitive documents (cross-cut shredder) |
| Document Handling | Clear desk when leaving workspace |
| Access Control | Prevent family/visitor access to work devices |
| Travel Security | Carry devices in hand luggage |
| Travel Security | Never leave devices in vehicles |

#### 11.2 Lost/Stolen Procedure Elements

| Element | Requirement |
|---------|-------------|
| Reporting Channel | 24/7 hotline or email for reporting |
| Account Disable | Ability to disable account within 1 hour |
| Remote Lock | Ability to lock device remotely within 1 hour |
| Remote Wipe | Ability to wipe device remotely within 4 hours |
| Recovery Key Access | Access to recovery keys for encrypted devices |
| Replacement Process | Process to issue replacement device |
| Incident Documentation | Record of incident details |
| Investigation | Follow-up investigation procedure |
| Insurance | Device covered by insurance (if applicable) |

---

## END OF SPECIFICATION

---

*"Physical security is the foundation upon which all other security measures are built."*
— ASIS International


*Where bamboo antennas actually work.* 🎋
