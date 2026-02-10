<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.14.1-UG:framework:UG:a.5.14.1 -->
**ISMS-IMP-A.5.14.1-UG - Transfer Rules and Procedures**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.14

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.14.1-UG |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.14 (Information Transfer) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.14 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.14 (Information Transfer Policy)
- ISMS-IMP-A.5.14.2 (Channel Security Assessment)
- ISMS-IMP-A.5.14.3 (Transfer Agreements Register)
- ISMS-POL-A.5.12-13 (Information Classification and Labelling)
- ISMS-POL-A.8.24 (Use of Cryptography)

---

## Assessment Overview

### Purpose

The **Transfer Rules and Procedures Assessment Workbook** (ISMS-IMP-A.5.14.1) documents your organisation's information transfer policies, procedures, and acceptable methods for each classification level. This assessment ensures that appropriate transfer rules exist for electronic, physical, and verbal information exchanges.

### Scope

This assessment covers:
- **Transfer policy elements**: Overarching policy requirements for information transfer
- **Transfer method matrix**: Acceptable methods mapped to classification levels
- **Electronic transfer rules**: Email, cloud, messaging, and file sharing procedures
- **Physical transfer procedures**: Media, courier, and document handling
- **Verbal transfer protocols**: Meetings, calls, and discussion guidelines
- **Supporting evidence**: Documentation demonstrating rule implementation

### Business Value

Completing this assessment delivers:
- **Clear transfer guidelines** mapped to classification levels
- **Reduced data leakage risk** through defined procedures
- **Compliance evidence** for ISO 27001:2022 A.5.14
- **Consistent handling** across all transfer channels
- **Audit readiness** with documented rules and approvals

### Control Requirement

> *ISO/IEC 27001:2022 Annex A.5.14 — Information Transfer*
>
> "Information transfer rules, procedures, or agreements should be in place for all types of transfer facilities within the organization and between the organization and other parties."

---

## Prerequisites

Before starting this assessment, ensure you have:

### Required Documents
- [ ] ISMS-POL-A.5.14 (Information Transfer Policy) — approved and current
- [ ] ISMS-POL-A.5.12-13 (Classification Scheme) — defines classification levels
- [ ] ISMS-POL-A.8.24 (Cryptography Policy) — encryption requirements
- [ ] Existing transfer procedures (if any)
- [ ] IT architecture documentation showing transfer systems

### Required Access
- [ ] Access to email system administration (Exchange, M365)
- [ ] Cloud storage configuration (SharePoint, OneDrive)
- [ ] File transfer system documentation (SFTP, MFT)
- [ ] DLP system configuration
- [ ] Security policy repository

### Required Personnel
- [ ] IT Security Manager
- [ ] Email/Messaging Administrator
- [ ] Cloud Services Administrator
- [ ] Facilities/Physical Security Manager
- [ ] Legal/Compliance Representative (for external transfers)

---

## Completion Walkthrough

### Sheet 1: Instructions

**Purpose**: Provides overview and guidance for completing the workbook.

**Actions**:
1. Read the purpose statement thoroughly
2. Review the sheet descriptions
3. Note the classification colour coding:
   - **PUBLIC** (Blue): Information approved for public release
   - **INTERNAL** (Green): Internal business information
   - **CONFIDENTIAL** (Orange): Sensitive business information
   - **RESTRICTED** (Red): Highly sensitive, limited access
4. Proceed to Transfer_Policy sheet

### Sheet 2: Transfer_Policy

**Purpose**: Document the overarching policy elements governing information transfer.

**Pre-populated Elements**:
- Scope Definition
- Classification Alignment
- Encryption Standards
- Authentication Requirements
- Authorization Process
- Chain of Custody
- Third-Party Requirements
- Incident Reporting
- Retention of Transfer Records
- User Awareness

**For Each Policy Element, Complete**:

| Column | Action | Example |
|--------|--------|---------|
| Owner | Assign responsible role | "IT Security Manager" |
| Status | Select current state | "Approved" or "Draft" |

**Validation Checklist**:
- [ ] Every MANDATORY element has an assigned owner
- [ ] All elements have a status assigned
- [ ] Status reflects actual document state
- [ ] Review frequency is appropriate for the element

### Sheet 3: Transfer_Methods

**Purpose**: Define which transfer methods are permitted for each classification level.

**Matrix Structure**:
Rows contain transfer methods (e.g., Corporate Email, Cloud Storage, USB)
Columns contain classification levels (PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED)

**For Each Cell, Select**:
- **Allowed**: Method permitted without conditions
- **Conditional**: Method permitted with specific conditions
- **Not Allowed**: Method prohibited for this classification

**Key Columns to Complete**:

| Column | Purpose | Example |
|--------|---------|---------|
| Conditions | Specific requirements when "Conditional" | "TLS 1.2+ required, manager approval" |
| Approval Required | Who must approve use | "Manager", "CISO", "None" |
| Notes | Organisation-specific variations | "Legacy FTP to be retired by Q3" |

**Critical Transfer Methods to Document**:
1. Corporate Email (encrypted and unencrypted)
2. Personal Email (emergency use only)
3. Approved Cloud Storage (SharePoint, OneDrive)
4. Public Cloud Storage (Dropbox, Google Drive)
5. SFTP/SCP for system integrations
6. USB/Removable Media
7. Physical Courier
8. Video Conference platforms
9. Instant Messaging (corporate and public)
10. API/Web Services

### Sheet 4: Electronic_Transfer

**Purpose**: Document security controls for each electronic transfer channel.

**For Each Channel, Document**:

| Column | Description | Example |
|--------|-------------|---------|
| Channel | Transfer system name | "Corporate Email - External" |
| Security Controls | Technical controls in place | "Exchange Online + S/MIME" |
| Encryption Requirement | Minimum encryption standard | "TLS 1.2+ or S/MIME" |
| Authentication | How users/systems authenticate | "Microsoft Entra ID (formerly Azure AD) + MFA" |
| Logging | Audit trail mechanism | "Exchange Audit Logs" |
| Max Classification | Highest permitted classification | "CONFIDENTIAL" |
| DLP Integration | Whether DLP monitors this channel | "Yes", "Manual", "N/A" |
| Notes | Additional context | "External gateway filters attachments" |

**Standard Electronic Channels**:
- Corporate Email (Internal)
- Corporate Email (External)
- SharePoint/OneDrive
- Teams File Sharing
- SFTP Server
- API Gateway
- Managed File Transfer (MFT)
- VPN Site-to-Site

### Sheet 5: Physical_Transfer

**Purpose**: Document procedures for physical media and document transfers.

**For Each Transfer Type, Document**:

| Column | Description | Example |
|--------|-------------|---------|
| Transfer Type | Physical transfer method | "Encrypted USB Drive" |
| Packaging Requirements | How items must be packaged | "Tamper-evident bag" |
| Courier/Transport | Approved delivery methods | "Hand delivery or approved courier" |
| Chain of Custody | Tracking requirements | "Transfer log required" |
| Recipient Verification | How to verify recipient | "ID verification + signature" |
| Max Classification | Highest permitted classification | "CONFIDENTIAL" |
| Environmental Protection | Physical safeguards | "Static protection" |
| Notes | Organisation-specific procedures | "USB inventory logged" |

**Standard Physical Transfer Types**:
- Encrypted USB Drive
- External Hard Drive
- Printed Documents
- Classified Documents (double-sealed)
- Backup Tapes
- Mobile Devices
- Hardware for Disposal

### Sheet 6: Verbal_Transfer

**Purpose**: Document protocols for verbal information exchange.

**For Each Communication Type, Document**:

| Column | Description | Example |
|--------|-------------|---------|
| Communication Type | Verbal transfer method | "In-Person Meeting (internal)" |
| Security Precautions | Safeguards required | "Secure meeting room, no unauthorised persons" |
| Participant Verification | How to verify attendees | "Badge/employee verification" |
| Recording Policy | Rules for recording | "No recording without consent" |
| Max Classification | Highest permitted classification | "CONFIDENTIAL" |
| Follow-up Documentation | Required documentation | "Meeting minutes if needed" |
| Notes | Additional context | "Clean desk policy applies" |

**Standard Verbal Transfer Types**:
- In-Person Meeting (internal and external)
- Video Conference (internal and external)
- Phone Call (internal and external)
- Voicemail
- Presentation/Training

### Sheet 7: Evidence_Register

**Purpose**: Track supporting evidence for transfer rules.

**For Each Evidence Item**:

| Column | Action | Example |
|--------|--------|---------|
| Evidence ID | Unique identifier | "EV-514-001" |
| Evidence Type | Document category | "Policy Document", "Configuration Export" |
| Description | What the evidence demonstrates | "Information Transfer Policy v1.0" |
| Related Control | Which sheet it supports | "Transfer_Policy" |
| Location/Link | Where evidence is stored | "SharePoint/ISMS/Evidence/A.5.14" |
| Date Collected | When evidence was gathered | "15.01.2026" |
| Collected By | Person who collected it | "IT Security Analyst" |
| Status | Current evidence status | "Verified" |

**Required Evidence Types**:
- Approved Information Transfer Policy
- Email encryption configuration
- Secure courier procedures
- Transfer security training records
- 30-day transfer audit log sample

### Sheet 8: Approval_SignOff

**Purpose**: Formal authorisation and version tracking.

**Complete the Following**:

| Section | Fields | Action |
|---------|--------|--------|
| Document Information | Pre-filled | Verify accuracy |
| Approval Signatures | Name, Signature, Date, Status | Obtain all approvals |
| Version History | Author, Changes, Approved By | Document any changes |

**Required Approvers**:
1. Document Owner (Primary author)
2. IT Security Manager
3. Information Security Officer
4. Department Head
5. CISO (if RESTRICTED information included)

---

## Evidence Collection

### Evidence Requirements by Sheet

| Sheet | Required Evidence |
|-------|-------------------|
| Transfer_Policy | Approved policy document, communication records |
| Transfer_Methods | DLP configuration, system access control settings |
| Electronic_Transfer | Email gateway config, encryption settings, audit logs |
| Physical_Transfer | Courier contracts, packaging procedures, chain of custody forms |
| Verbal_Transfer | Meeting room booking system config, video platform settings |

### Evidence Storage

Store all evidence in the ISMS Evidence Repository with the following structure:
```
/ISMS/Evidence/A.5.14-Information-Transfer/
├── A.5.14.1-Transfer-Rules/
│   ├── Policy-Documents/
│   ├── Configuration-Exports/
│   ├── Procedure-Documents/
│   └── Audit-Logs/
```

### Evidence Naming Convention

Use format: `EV-514-[Type]-[Description]-[YYYYMMDD].[ext]`

Examples:
- `EV-514-CFG-Email-TLS-Settings-20260115.pdf`
- `EV-514-POL-Transfer-Policy-Approved-20260110.pdf`
- `EV-514-LOG-Email-Audit-30day-20260115.xlsx`

---

## Common Pitfalls

### ❌ MISTAKE: Allowing personal email for "emergency" transfers without controls
✅ CORRECT: Define specific conditions, require post-facto documentation within 24 hours, and manager notification

### ❌ MISTAKE: Marking all methods as "Not Allowed" for RESTRICTED
✅ CORRECT: Ensure at least one secure path exists for legitimate RESTRICTED transfers (e.g., encrypted MFT)

### ❌ MISTAKE: Using generic "Approved" status without documenting conditions
✅ CORRECT: Always specify conditions in the Conditions column for "Conditional" methods

### ❌ MISTAKE: Omitting legacy systems from the transfer method matrix
✅ CORRECT: Document all current systems, including legacy FTP, with deprecation plans noted

### ❌ MISTAKE: Not aligning encryption requirements with A.8.24 policy
✅ CORRECT: Reference specific encryption standards from the Cryptography Policy

### ❌ MISTAKE: Missing DLP integration for key transfer channels
✅ CORRECT: Document DLP coverage for all channels handling INTERNAL+ information

### ❌ MISTAKE: Not documenting verbal transfer protocols
✅ CORRECT: Verbal transfers are common attack vectors; document security precautions for each type

### ❌ MISTAKE: Skipping physical transfer procedures for "digital-first" organisations
✅ CORRECT: Document even minimal physical procedures (printed documents, visitor handling)

### ❌ MISTAKE: Not obtaining CISO sign-off when RESTRICTED methods are defined
✅ CORRECT: CISO approval required if any rules govern RESTRICTED information transfer

### ❌ MISTAKE: Storing evidence without version control
✅ CORRECT: Use dated filenames and maintain version history in Evidence_Register

---

## Quality Checklist

Before submitting the completed workbook, verify:

### Policy Completeness
- [ ] All MANDATORY policy elements have assigned owners
- [ ] All elements have appropriate review frequency set
- [ ] Status reflects actual documentation state

### Transfer Methods
- [ ] Every classification level has at least one allowed method
- [ ] "Conditional" entries have conditions documented
- [ ] Approval requirements are clear and assigned
- [ ] Legacy/deprecated methods are identified with plans

### Electronic Transfer
- [ ] All corporate transfer channels are documented
- [ ] Encryption requirements are specific (algorithms, versions)
- [ ] DLP integration status is accurate
- [ ] Max classification aligns with technical controls

### Physical Transfer
- [ ] Packaging requirements are specific and testable
- [ ] Courier/transport options are approved and documented
- [ ] Chain of custody requirements are clear
- [ ] Environmental protection is appropriate for media type

### Verbal Transfer
- [ ] All common communication types are covered
- [ ] Recording policies are clear and compliant
- [ ] Participant verification methods are practical
- [ ] Max classification is appropriate for each type

### Evidence and Approval
- [ ] All required evidence types are listed
- [ ] Evidence locations are accurate and accessible
- [ ] All required approvers have signed
- [ ] Version history is current

---

## Review and Approval

### Review Cycle
- **Frequency**: Annual, or upon significant change
- **Triggers**: New transfer systems, policy updates, security incidents

### Approval Workflow
1. **Preparer** completes all sheets
2. **IT Security Manager** validates technical accuracy
3. **ISO** verifies policy alignment
4. **Department Heads** confirm operational feasibility
5. **CISO** provides final approval (if RESTRICTED content)

### Post-Approval Actions
- Communicate rules to all personnel
- Update training materials
- Configure technical controls to enforce rules
- Schedule next review date

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
