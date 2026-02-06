**ISMS-IMP-A.6.7-8.S2-UG - Technical Controls Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S2-UG |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.6.7-8.S2-TG.

---

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

#### ❌ MISTAKE #1: Testing Only Primary VPN Solution

**The Problem:** Focusing assessment only on the main corporate VPN, missing other remote access paths.

**Why It Matters:** Organizations often have multiple remote access methods (vendor VPN, legacy systems, cloud gateways). Unassessed paths may have weaker security.

**The Fix:**
- Inventory ALL remote access methods before starting
- Include: VPN, RDP gateways, ZTNA, cloud proxies, vendor access
- Check with IT operations for any additional access paths

#### ❌ MISTAKE #2: Checking MFA Enrollment, Not Enforcement

**The Problem:** Confirming MFA is enrolled/available but not verifying it's actually enforced.

**Why It Matters:** Users may have MFA enrolled but configured with bypass options. "Enrolled" doesn't mean "protected."

**The Fix:**
- Test actual login flow to verify MFA prompt
- Check for bypass conditions (trusted networks, remembered devices)
- Verify MFA is required, not optional

#### ❌ MISTAKE #3: Missing Mobile and BYOD Access

**The Problem:** Assessing laptop VPN but not mobile device access or BYOD scenarios.

**Why It Matters:** Mobile access may use different authentication paths. BYOD devices may have weaker controls. Growing attack surface.

**The Fix:**
- Include mobile email, apps, and browser access
- Assess BYOD enrollment and security requirements
- Check mobile device management (MDM) integration

#### ❌ MISTAKE #4: Not Testing Actual Encryption

**The Problem:** Accepting documented encryption standards without technical verification.

**Why It Matters:** Configuration may differ from documentation. Weak ciphers may be negotiated. Certificate issues may exist.

**The Fix:**
- Use tools to verify actual encryption (testssl.sh, nmap)
- Check negotiated cipher suites
- Verify certificate validity and chain

#### ❌ MISTAKE #5: Ignoring Service Account Remote Access

**The Problem:** Focusing on user accounts, missing service accounts that access systems remotely.

**Why It Matters:** Service accounts often have elevated privileges. They may bypass MFA requirements. Compromise is harder to detect.

**The Fix:**
- Inventory service accounts with remote access
- Assess service account authentication methods
- Check for use of secrets management

#### ❌ MISTAKE #6: Accepting "Enabled" Without Configuration Evidence

**The Problem:** Trusting that controls are "enabled" without seeing actual configuration.

**Why It Matters:** Settings may be misconfigured. "Enabled" doesn't mean "correctly configured." Evidence needed for audit.

**The Fix:**
- Collect configuration screenshots or exports
- Verify specific settings against policy requirements
- Document actual configuration state

#### ❌ MISTAKE #7: Not Checking Certificate Validity and Monitoring

**The Problem:** Verifying current certificate is valid but not checking expiration monitoring.

**Why It Matters:** Expired certificates cause outages and security issues. Lack of monitoring means surprise failures.

**The Fix:**
- Check certificate expiration dates
- Verify certificate monitoring is in place
- Check renewal process documentation

#### ❌ MISTAKE #8: Missing Cloud Application Remote Access

**The Problem:** Assessing on-premises VPN but not cloud/SaaS application access.

**Why It Matters:** Cloud apps may be primary remote access path. Different authentication requirements. Shadow IT risk.

**The Fix:**
- Include SaaS applications in scope
- Check SSO/federation configuration
- Assess cloud access security broker (CASB) if used

#### ❌ MISTAKE #9: Overlooking Split Tunneling Risks

**The Problem:** Not assessing whether split tunneling is enabled and its security implications.

**Why It Matters:** Split tunneling may expose corporate traffic. Different security posture for tunneled vs. local traffic.

**The Fix:**
- Document split tunneling configuration
- Assess what traffic is tunneled vs. local
- Check DNS leak protection

#### ❌ MISTAKE #10: Not Correlating VPN Access with HR Data

**The Problem:** Assessing VPN technically but not verifying users are authorized personnel.

**Why It Matters:** May find active VPN accounts for terminated employees. Orphaned accounts represent security risk.

**The Fix:**
- Cross-reference VPN user list with HR active employees
- Check for orphaned or unknown accounts
- Verify contractor accounts match active contracts

---

### 7. Quality Checklist

#### Completeness Checks

**Infrastructure Coverage:**
- [ ] ALL VPN/remote access solutions inventoried
- [ ] ALL remote access methods documented (VPN, ZTNA, RDP, cloud)
- [ ] Service accounts with remote access included
- [ ] Mobile and BYOD access assessed

**MFA Assessment:**
- [ ] MFA coverage assessed for all systems
- [ ] MFA enforcement verified (not just enrollment)
- [ ] Fallback methods documented
- [ ] Exceptions documented with justification

**Encryption Assessment:**
- [ ] Encryption verified for all channels
- [ ] Protocol versions documented (TLS 1.2/1.3)
- [ ] Cipher suites verified
- [ ] Certificate validity checked

**Logging:**
- [ ] Logging assessed for all remote access
- [ ] Log retention verified
- [ ] Monitoring alerts assessed

**Gaps:**
- [ ] All gaps documented with remediation
- [ ] Gap priorities assigned
- [ ] Owners and target dates set

#### Technical Accuracy Checks

- [ ] Configuration settings verified (not assumed)
- [ ] Evidence supports compliance claims
- [ ] Encryption algorithms correctly identified
- [ ] MFA methods accurately categorized
- [ ] Version numbers verified

#### Evidence Quality Checks

- [ ] Sensitive data redacted (passwords, keys)
- [ ] Evidence dated and attributed
- [ ] File references accurate and accessible
- [ ] Evidence stored securely
- [ ] No production credentials in evidence

---

### 8. Review and Approval Process

#### 8.1 Review Workflow

**Step 1: Self-Review** (Assessor)
- Complete Quality Checklist
- Verify technical accuracy
- Ensure evidence accessibility

**Step 2: Technical Review** (IT Security/Network Team)
- Verify technical findings accuracy
- Validate configuration assessments
- Confirm remediation feasibility
- Duration: 3-5 business days

**Step 3: Management Approval** (CISO)
- Review overall security posture
- Approve remediation priorities
- Authorize resources
- Duration: 1-2 business days

#### 8.2 After Approval

1. **Store Assessment:** `ISMS/Controls/A.6.7-8/Technical_Controls/`
2. **Distribute:** IT Operations, Security Team, Compliance
3. **Initiate Remediation:** Create tickets for gaps
4. **Schedule Follow-Up:** Annual reassessment

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
