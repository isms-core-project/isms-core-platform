**ISMS-IMP-A.6.7-8.S2 - Technical Controls Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S2 |
| **Version** | 1.0 |
| **Assessment Area** | VPN, MFA, Encryption, Logging, and Session Management |
| **Related Policy** | ISMS-POL-A.6.7-8, Section 2.3 (Technical Security Requirements) |
| **Purpose** | Guide users through systematic assessment of technical security controls for remote access |
| **Target Audience** | IT Security Team, Network Engineers, Identity Management Team, Auditors |
| **Assessment Type** | Technical |
| **Review Cycle** | Semi-Annual |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for technical controls assessment | ISMS Implementation Team |

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

- **Part I:** Assessment users (IT Security Team, Network Engineers, Identity Management)
- **Part II:** Workbook developers (Python/Excel script maintainers)

---

# PART I: USER COMPLETION GUIDE

**Audience:** IT Security Team, Network Engineers, Identity Management Team

---

## 1. Assessment Overview

#### 1.1 Purpose

This assessment workbook evaluates [Organization]'s technical security controls for remote work, ensuring that:
- VPN or Zero Trust access solutions are properly deployed
- Multi-factor authentication (MFA) is enforced for all remote access
- Data encryption (in transit and at rest) meets requirements
- Remote access is properly logged and monitored
- Technical controls integrate with event reporting mechanisms

#### 1.2 Scope

This assessment covers:
- VPN infrastructure and configuration
- Zero Trust Network Access (ZTNA) solutions (if applicable)
- Multi-factor authentication deployment and enforcement
- Encryption for remote communications
- Remote access logging and monitoring
- DNS and network security for remote connections
- Session management and timeout controls

#### 1.3 Target Audience

- **Primary Assessors**: IT Security Team, Network Engineers
- **Data Contributors**: IT Operations, Identity Management Team
- **Reviewers**: IT Security Manager, CISO
- **Approvers**: CISO

#### 1.4 Assessment Frequency

| Trigger | Frequency |
|---------|-----------|
| Initial Assessment | Once (ISMS implementation) |
| Periodic Review | Semi-annual |
| Triggered Review | After security incidents, major changes to remote access infrastructure |

### 2. Prerequisites

Before starting this assessment, ensure:

| Prerequisite | Status | Notes |
|--------------|--------|-------|
| Access to VPN management console | ☐ | Admin or read-only access |
| Access to MFA administration portal | ☐ | Enrollment and compliance data |
| Access to identity management system | ☐ | User provisioning data |
| Network diagrams for remote access | ☐ | Current architecture |
| VPN/remote access logs | ☐ | Sample period for analysis |
| List of approved remote access methods | ☐ | From IT Security |

### 3. Assessment Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: VPN/Remote Access Infrastructure                     │
│  - Inventory VPN solutions                                      │
│  - Review architecture and configuration                        │
│  - Verify encryption standards                                  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 2: Multi-Factor Authentication                          │
│  - Assess MFA deployment coverage                               │
│  - Verify enforcement mechanisms                                │
│  - Check MFA method strength                                    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 3: Encryption Assessment                                 │
│  - Verify TLS/SSL configuration                                 │
│  - Check certificate management                                 │
│  - Assess data-at-rest encryption                               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 4: Logging and Monitoring                               │
│  - Verify remote access logging                                 │
│  - Check log retention and protection                          │
│  - Assess monitoring capabilities                               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 5: Gap Analysis & Evidence Collection                    │
│  - Document gaps identified                                     │
│  - Collect configuration evidence                               │
│  - Prepare remediation recommendations                          │
└─────────────────────────────────────────────────────────────────┘
```

### 4. Sheet-by-Sheet Completion Guide

#### 4.1 Instructions Sheet

**Purpose**: Provides guidance for workbook users.

**Actions**:
- Review the instructions before starting
- Note the version and assessment date
- Identify your role and access requirements

#### 4.2 VPN_Infrastructure Sheet

**Purpose**: Inventory and assess VPN/remote access solutions.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Solution ID | Unique identifier for VPN solution | Auto-generated |
| Solution Name | Name of VPN/remote access solution | Free text |
| Vendor | Solution vendor | Free text |
| Version | Current version deployed | Free text |
| Solution Type | VPN/ZTNA/RDP Gateway/Other | Dropdown |
| Deployment Scope | Who uses this solution | Free text |
| Users Covered | Approximate user count | Number |
| Protocol | VPN protocol (IKEv2, WireGuard, SSL, etc.) | Free text |
| Encryption | Encryption algorithm used | Free text |
| Compliant | Meets security requirements | Yes/No |
| Notes | Additional observations | Free text |

**Completion Steps**:
1. Inventory all VPN/remote access solutions
2. Document technical specifications
3. Verify encryption meets minimum standards (AES-256, TLS 1.2+)
4. Assess overall compliance

#### 4.3 VPN_Configuration Sheet

**Purpose**: Assess VPN configuration security settings.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Configuration Item | Security setting being assessed | Pre-populated |
| Requirement | Expected configuration | Pre-populated |
| Current Setting | Actual current setting | Free text |
| Compliant | Meets requirement | Yes/No |
| Evidence | Screenshot or config export reference | Free text |
| Gap Description | If non-compliant, describe gap | Free text |
| Remediation | Recommended fix | Free text |

**Key Configuration Items**:
- Encryption algorithm (AES-256 minimum)
- Key exchange protocol (IKEv2/DH Group 14+)
- Perfect Forward Secrecy enabled
- Split tunneling disabled (or controlled)
- Idle timeout configured
- Failed login lockout
- Certificate-based authentication
- Strong cipher suites only

#### 4.4 MFA_Deployment Sheet

**Purpose**: Assess multi-factor authentication deployment and coverage.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Application/System | System requiring MFA | Free text |
| MFA Required | Is MFA mandated for this system? | Yes/No |
| MFA Enforced | Is MFA technically enforced? | Yes/No |
| MFA Method | Primary MFA method used | Dropdown |
| Fallback Method | Backup MFA method | Dropdown |
| Enrollment % | Percentage of users enrolled | Percentage |
| Exceptions | Any users exempted | Free text |
| Compliant | Meets policy requirements | Formula |
| Notes | Additional observations | Free text |

**MFA Methods (Strength Order)**:
1. Hardware security keys (FIDO2/U2F) - Strongest
2. Authenticator apps (TOTP/Push)
3. SMS/Voice OTP - Acceptable
4. Email OTP - Minimum acceptable
5. Security questions - NOT acceptable for remote access

#### 4.5 MFA_Compliance Sheet

**Purpose**: Test MFA enforcement through user sampling.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Sample ID | Unique identifier | Auto-generated |
| User Type | Employee/Contractor/Admin/Service | Dropdown |
| Access Type | VPN/Web App/Email/All | Free text |
| MFA Enrolled | Is user enrolled in MFA? | Yes/No |
| MFA Active | Is MFA enforced on last login? | Yes/No |
| Last MFA Date | Date of last MFA authentication | Date |
| Method Used | Which MFA method was used | Free text |
| Compliant | User meets MFA requirements | Formula |
| Notes | Observations | Free text |

**Sample Selection**:
- Minimum 5% of remote users or 30 users (whichever is greater)
- Include: regular users, administrators, contractors, service accounts
- Include users from different departments

#### 4.6 Encryption_Assessment Sheet

**Purpose**: Assess encryption for data in transit and at rest.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Encryption Domain | What is being encrypted | Pre-populated |
| Requirement | Minimum encryption standard | Pre-populated |
| Current Implementation | What is currently in place | Free text |
| Protocol/Algorithm | Specific protocol or algorithm | Free text |
| Key Length | Encryption key length | Free text |
| Certificate Validity | Certificate expiration status | Date/Status |
| Compliant | Meets requirements | Yes/No |
| Evidence | Configuration or test evidence | Free text |
| Gap | If non-compliant, describe | Free text |

**Encryption Domains**:
- VPN tunnel encryption
- Web application TLS (public-facing)
- Internal web applications
- Email encryption (TLS)
- File transfer encryption
- API communications
- Database connections
- Storage/disk encryption

#### 4.7 Logging_Monitoring Sheet

**Purpose**: Assess remote access logging and monitoring capabilities.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Log Category | Type of log being assessed | Pre-populated |
| Log Source | System generating logs | Free text |
| Logging Enabled | Is logging active? | Yes/No |
| Log Content | What is captured | Free text |
| Retention Period | How long logs are kept | Free text |
| Centralized | Sent to SIEM/central logging? | Yes/No |
| Monitored | Active monitoring/alerting? | Yes/No |
| Alert Thresholds | Alerting configured | Yes/No |
| Compliant | Meets requirements | Formula |
| Notes | Observations | Free text |

**Log Categories**:
- VPN connection logs (connect/disconnect)
- Authentication logs (success/failure)
- MFA logs (enrollment, authentication, bypass)
- Failed login attempts
- Privileged access logs
- Session duration logs
- IP/geolocation logs
- Device compliance logs

#### 4.8 Session_Management Sheet

**Purpose**: Assess session timeout and management controls.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| System/Application | System being assessed | Free text |
| Idle Timeout | Configured idle timeout | Free text |
| Session Max | Maximum session duration | Free text |
| Re-auth Required | Re-authentication triggers | Free text |
| Concurrent Sessions | Concurrent session limits | Free text |
| Session Termination | Admin termination capability | Yes/No |
| Compliant | Meets policy requirements | Yes/No |
| Evidence | Configuration evidence | Free text |

#### 4.9 Gap_Analysis Sheet

**Purpose**: Consolidate all technical control gaps.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Gap ID | Unique identifier (GAP-TC-###) | Auto-generated |
| Source Sheet | Which sheet identified gap | Reference |
| Gap Description | Clear description of the gap | Free text |
| Control Reference | Related policy section | Free text |
| Technical Risk | Risk if gap not addressed | Dropdown |
| Remediation Action | Recommended fix | Free text |
| Effort Estimate | Implementation effort (H/M/L) | Dropdown |
| Owner | Who will remediate | Free text |
| Target Date | Remediation deadline | Date |
| Status | Current status | Dropdown |

#### 4.10 Evidence_Register Sheet

**Purpose**: Catalog all evidence collected during assessment.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Evidence ID | Unique identifier (EVD-TC-###) | Auto-generated |
| Evidence Type | Config Export/Screenshot/Report/Test Result | Dropdown |
| Description | What the evidence demonstrates | Free text |
| Source System | System evidence came from | Free text |
| Date Collected | When evidence was collected | Date |
| Collected By | Assessor name | Free text |
| File Reference | Filename or storage location | Free text |
| Sensitive | Contains sensitive data | Yes/No |

#### 4.11 Dashboard Sheet

**Purpose**: Provide executive summary of technical controls assessment.

**Metrics Displayed**:
- Overall technical compliance percentage
- VPN infrastructure compliance score
- MFA deployment coverage
- MFA enforcement rate
- Encryption compliance score
- Logging coverage percentage
- Gap count by severity and effort

#### 4.12 Approval_Sign_Off Sheet

**Purpose**: Document formal review and approval.

### 5. Evidence Collection Guidelines

#### 5.1 Required Evidence Types

| Evidence Category | Examples |
|-------------------|----------|
| Configuration Exports | VPN config, MFA policies, TLS settings |
| Screenshots | Admin console settings, compliance dashboards |
| Test Results | TLS scan results, penetration test excerpts |
| Reports | MFA enrollment reports, login statistics |
| Architecture Diagrams | Remote access architecture |
| Logs (Samples) | Sample authentication logs (sanitized) |

#### 5.2 Sensitive Data Handling

When collecting evidence:
- Redact usernames/passwords in screenshots
- Anonymize or mask personal identifiers
- Do not export full production logs with PII
- Store evidence in approved secure location
- Mark sensitive evidence appropriately

### 6. Common Pitfalls

| Pitfall | Avoidance Strategy |
|---------|-------------------|
| Testing only one VPN solution | Inventory ALL remote access methods |
| Ignoring legacy/exception access | Include legacy systems and exceptions |
| Checking enrollment, not enforcement | Verify MFA is enforced, not just enrolled |
| Missing mobile/BYOD access paths | Include all access methods (mobile, BYOD) |
| Not testing actual encryption | Use tools to verify TLS/encryption in practice |
| Ignoring service accounts | Include service accounts in MFA assessment |
| Accepting "enabled" without proof | Collect actual configuration evidence |
| Not checking certificate expiry | Verify certificate validity and monitoring |
| Missing cloud application access | Include SaaS/cloud apps accessed remotely |
| Overlooking split tunneling risks | Assess split tunneling configuration |

### 7. Quality Checklist

Before submitting assessment, verify:

**Completeness**:
- [ ] All VPN/remote access solutions inventoried
- [ ] MFA coverage assessed for all systems
- [ ] Encryption verified for all channels
- [ ] Logging assessed for all remote access
- [ ] All gaps documented with remediation

**Technical Accuracy**:
- [ ] Configuration settings verified (not assumed)
- [ ] Evidence supports compliance claims
- [ ] Encryption algorithms correctly identified
- [ ] MFA methods accurately categorized

**Evidence Quality**:
- [ ] Sensitive data redacted
- [ ] Evidence dated and attributed
- [ ] File references accurate
- [ ] Evidence stored securely

---

## PART II: Technical Specification

### 8. Workbook Architecture

#### 8.1 Sheet Structure

| Sheet Name | Purpose | Sheet Type |
|------------|---------|------------|
| Instructions | User guidance | Static |
| VPN_Infrastructure | VPN inventory | Assessment |
| VPN_Configuration | VPN security settings | Assessment |
| MFA_Deployment | MFA system coverage | Assessment |
| MFA_Compliance | MFA user compliance | Sample Testing |
| Encryption_Assessment | Encryption verification | Assessment |
| Logging_Monitoring | Log and monitor assessment | Assessment |
| Session_Management | Session controls | Assessment |
| Gap_Analysis | Consolidated gaps | Analysis |
| Evidence_Register | Evidence catalog | Register |
| Dashboard | Executive summary | Calculated |
| Approval_Sign_Off | Formal approvals | Governance |

### 9. Column Specifications

#### 9.1 VPN_Infrastructure Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Solution ID | 12 | Text | Auto (VPN-###) |
| B | Solution Name | 25 | Text | Free text |
| C | Vendor | 20 | Text | Free text |
| D | Version | 15 | Text | Free text |
| E | Solution Type | 15 | Dropdown | VPN/ZTNA/RDP Gateway/Other |
| F | Deployment Scope | 30 | Text | Free text |
| G | Users Covered | 12 | Number | Positive integer |
| H | Protocol | 20 | Text | Free text |
| I | Encryption | 20 | Text | Free text |
| J | Compliant | 10 | Dropdown | Yes/No |
| K | Notes | 40 | Text | Free text |

#### 9.2 MFA_Deployment Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Application/System | 30 | Text | Free text |
| B | MFA Required | 12 | Dropdown | Yes/No |
| C | MFA Enforced | 12 | Dropdown | Yes/No |
| D | MFA Method | 20 | Dropdown | See list below |
| E | Fallback Method | 20 | Dropdown | See list below |
| F | Enrollment % | 12 | Percentage | 0-100% |
| G | Exceptions | 30 | Text | Free text |
| H | Compliant | 12 | Formula | =AND(B="Yes",C="Yes",F>=95%) |
| I | Notes | 40 | Text | Free text |

**MFA Method Options**: Hardware Key, Authenticator App, Push Notification, SMS, Voice Call, Email, None

### 10. Formula Specifications

#### 10.1 Dashboard Calculations

**VPN Compliance Score**:
```
=COUNTIF(VPN_Infrastructure!J:J,"Yes")/COUNTA(VPN_Infrastructure!J2:J50)
```

**MFA Coverage**:
```
=AVERAGE(MFA_Deployment!F:F)
```

**MFA Enforcement Rate**:
```
=COUNTIF(MFA_Compliance!E:E,"Yes")/COUNTA(MFA_Compliance!E2:E100)
```

**Encryption Compliance**:
```
=COUNTIF(Encryption_Assessment!G:G,"Yes")/COUNTA(Encryption_Assessment!G2:G50)
```

### 11. Styling Specifications

#### 11.1 Compliance Status Colors

| Status | Fill Color | Use |
|--------|------------|-----|
| Compliant/Yes | #C6EFCE (Light Green) | Passing items |
| Non-Compliant/No | #FFC7CE (Light Red) | Failing items |
| Partial | #FFEB9C (Light Yellow) | Partial compliance |
| N/A | #D9D9D9 (Gray) | Not applicable |

#### 11.2 Risk/Priority Colors

| Level | Fill Color |
|-------|------------|
| High/Critical | #FF6B6B (Red) |
| Medium | #FFD93D (Yellow) |
| Low | #6BCB77 (Green) |

### 12. Data Validation Lists

#### 12.1 Dropdown Options

| Field | Options |
|-------|---------|
| Solution Type | VPN, ZTNA, RDP Gateway, SSH Gateway, Other |
| MFA Method | Hardware Key, Authenticator App, Push Notification, SMS, Voice Call, Email, None |
| User Type | Employee, Contractor, Administrator, Service Account |
| Effort Estimate | High, Medium, Low |
| Gap Status | Open, In Progress, Closed, Deferred, Accepted |
| Evidence Type | Config Export, Screenshot, Report, Test Result, Log Sample, Diagram |

### 13. Pre-Populated Content

#### 13.1 VPN Configuration Items

| Configuration Item | Requirement |
|--------------------|-------------|
| Encryption Algorithm | AES-256 or equivalent |
| Key Exchange | IKEv2 with DH Group 14+ or better |
| Perfect Forward Secrecy | Enabled |
| Split Tunneling | Disabled or controlled by policy |
| Idle Session Timeout | 30 minutes maximum |
| Failed Login Lockout | Lock after 5 failed attempts |
| Certificate Authentication | Enabled for machine auth |
| Weak Cipher Suites | Disabled (no DES, 3DES, RC4, MD5) |
| TLS Version | TLS 1.2 minimum, TLS 1.3 preferred |
| Logging | All connections and authentications logged |

#### 13.2 Encryption Domains

| Domain | Requirement |
|--------|-------------|
| VPN Tunnel | AES-256-GCM or AES-256-CBC |
| Web Applications (External) | TLS 1.2+ with strong cipher suites |
| Web Applications (Internal) | TLS 1.2+ recommended |
| Email (SMTP) | TLS 1.2+ with opportunistic encryption |
| File Transfer | SFTP or FTPS (not plain FTP) |
| API Communications | TLS 1.2+ |
| Database Connections | Encrypted connections or network segmentation |
| Disk Encryption | Full-disk encryption on remote devices |

#### 13.3 Log Categories

| Log Category | Minimum Content | Retention |
|--------------|-----------------|-----------|
| VPN Connections | User, timestamp, IP, duration | 90 days |
| Authentication Events | User, timestamp, result, source IP | 90 days |
| MFA Events | User, method, result, timestamp | 90 days |
| Failed Logins | User, timestamp, source IP, failure reason | 180 days |
| Privileged Access | User, action, target, timestamp | 1 year |
| Session Events | Session start/end, idle timeouts | 90 days |

---

## END OF SPECIFICATION

---

*"Complexity is the enemy of security."*
— Bruce Schneier


<!-- QA_VERIFIED: 2026-01-31 -->
