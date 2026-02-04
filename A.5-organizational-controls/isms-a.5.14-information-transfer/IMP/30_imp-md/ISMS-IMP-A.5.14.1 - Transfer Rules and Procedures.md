# ISMS-IMP-A.5.14.1 — Transfer Rules and Procedures

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.14.1 |
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

# PART I: USER COMPLETION GUIDE

## 1. Assessment Overview

### 1.1 Purpose

The **Transfer Rules and Procedures Assessment Workbook** (ISMS-IMP-A.5.14.1) documents your organisation's information transfer policies, procedures, and acceptable methods for each classification level. This assessment ensures that appropriate transfer rules exist for electronic, physical, and verbal information exchanges.

### 1.2 Scope

This assessment covers:
- **Transfer policy elements**: Overarching policy requirements for information transfer
- **Transfer method matrix**: Acceptable methods mapped to classification levels
- **Electronic transfer rules**: Email, cloud, messaging, and file sharing procedures
- **Physical transfer procedures**: Media, courier, and document handling
- **Verbal transfer protocols**: Meetings, calls, and discussion guidelines
- **Supporting evidence**: Documentation demonstrating rule implementation

### 1.3 Business Value

Completing this assessment delivers:
- **Clear transfer guidelines** mapped to classification levels
- **Reduced data leakage risk** through defined procedures
- **Compliance evidence** for ISO 27001:2022 A.5.14
- **Consistent handling** across all transfer channels
- **Audit readiness** with documented rules and approvals

### 1.4 Control Requirement

> *ISO/IEC 27001:2022 Annex A.5.14 — Information Transfer*
>
> "Information transfer rules, procedures, or agreements should be in place for all types of transfer facilities within the organization and between the organization and other parties."

---

## 2. Prerequisites

Before starting this assessment, ensure you have:

### 2.1 Required Documents
- [ ] ISMS-POL-A.5.14 (Information Transfer Policy) — approved and current
- [ ] ISMS-POL-A.5.12-13 (Classification Scheme) — defines classification levels
- [ ] ISMS-POL-A.8.24 (Cryptography Policy) — encryption requirements
- [ ] Existing transfer procedures (if any)
- [ ] IT architecture documentation showing transfer systems

### 2.2 Required Access
- [ ] Access to email system administration (Exchange, M365)
- [ ] Cloud storage configuration (SharePoint, OneDrive)
- [ ] File transfer system documentation (SFTP, MFT)
- [ ] DLP system configuration
- [ ] Security policy repository

### 2.3 Required Personnel
- [ ] IT Security Manager
- [ ] Email/Messaging Administrator
- [ ] Cloud Services Administrator
- [ ] Facilities/Physical Security Manager
- [ ] Legal/Compliance Representative (for external transfers)

---

## 3. Workbook Structure

The workbook contains **8 sheets** organised as follows:

| Sheet | Purpose | Input Required |
|-------|---------|----------------|
| Instructions | Guidance and colour coding reference | None (read-only) |
| Transfer_Policy | Overarching policy element documentation | Owner, Status |
| Transfer_Methods | Acceptable methods by classification level | Approval flags, Notes |
| Electronic_Transfer | Email, cloud, messaging, and file sharing rules | Notes, Customisations |
| Physical_Transfer | Media, courier, document transfer procedures | Notes, Customisations |
| Verbal_Transfer | Meeting, call, and discussion protocols | Notes, Customisations |
| Evidence_Register | Supporting documentation references | Location, Status |
| Approval_SignOff | Formal sign-off and version history | Signatures, Dates |

---

## 4. Completion Walkthrough

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
| Authentication | How users/systems authenticate | "Azure AD + MFA" |
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

## 5. Evidence Collection

### 5.1 Evidence Requirements by Sheet

| Sheet | Required Evidence |
|-------|-------------------|
| Transfer_Policy | Approved policy document, communication records |
| Transfer_Methods | DLP configuration, system access control settings |
| Electronic_Transfer | Email gateway config, encryption settings, audit logs |
| Physical_Transfer | Courier contracts, packaging procedures, chain of custody forms |
| Verbal_Transfer | Meeting room booking system config, video platform settings |

### 5.2 Evidence Storage

Store all evidence in the ISMS Evidence Repository with the following structure:
```
/ISMS/Evidence/A.5.14-Information-Transfer/
├── A.5.14.1-Transfer-Rules/
│   ├── Policy-Documents/
│   ├── Configuration-Exports/
│   ├── Procedure-Documents/
│   └── Audit-Logs/
```

### 5.3 Evidence Naming Convention

Use format: `EV-514-[Type]-[Description]-[YYYYMMDD].[ext]`

Examples:
- `EV-514-CFG-Email-TLS-Settings-20260115.pdf`
- `EV-514-POL-Transfer-Policy-Approved-20260110.pdf`
- `EV-514-LOG-Email-Audit-30day-20260115.xlsx`

---

## 6. Common Pitfalls

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

## 7. Quality Checklist

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

## 8. Review and Approval

### 8.1 Review Cycle
- **Frequency**: Annual, or upon significant change
- **Triggers**: New transfer systems, policy updates, security incidents

### 8.2 Approval Workflow
1. **Preparer** completes all sheets
2. **IT Security Manager** validates technical accuracy
3. **ISO** verifies policy alignment
4. **Department Heads** confirm operational feasibility
5. **CISO** provides final approval (if RESTRICTED content)

### 8.3 Post-Approval Actions
- Communicate rules to all personnel
- Update training materials
- Configure technical controls to enforce rules
- Schedule next review date

---

# PART II: TECHNICAL SPECIFICATION

## 9. Workbook Technical Details

### 9.1 File Information

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.14.1 |
| **Generated Filename** | `ISMS-IMP-A.5.14.1_Transfer_Rules_and_Procedures_YYYYMMDD.xlsx` |
| **Generator Script** | `generate_a514_1_transfer_rules_procedures.py` |
| **Sheet Count** | 8 |
| **Primary Control** | A.5.14 (Information Transfer) |

### 9.2 Sheet Specifications

#### Sheet 1: Instructions
- **Type**: Read-only guidance
- **Row 1**: Title banner (merged A1:H1)
- **Rows 3-7**: Document metadata
- **Rows 9+**: Sheet descriptions, colour legend
- **Column widths**: A=25, B=60, C-H=20

#### Sheet 2: Transfer_Policy
- **Type**: Data entry
- **Row 1**: Section title (merged A1:F1)
- **Row 3**: Column headers
- **Rows 4+**: Policy element entries
- **Data validation**: Status dropdown (Draft, Under Review, Approved, Needs Update)
- **Input columns**: D (Owner), F (Status) - yellow fill
- **Column widths**: A=30, B=50, C=15, D=25, E=18, F=15

#### Sheet 3: Transfer_Methods
- **Type**: Matrix entry
- **Row 1**: Section title (merged A1:H1)
- **Row 3**: Column headers with classification colours
- **Rows 4+**: Transfer method entries
- **Data validation**:
  - B4:E{n}: "Allowed, Conditional, Not Allowed"
  - G4:G{n}: "Yes, No, Varies, Technical Review"
- **Conditional formatting**: Allowed=green, Conditional=amber, Not Allowed=red
- **Column widths**: A=30, B-E=12, F=30, G=18, H=30

#### Sheet 4: Electronic_Transfer
- **Type**: Data entry
- **Row 1**: Section title (merged A1:H1)
- **Row 3**: Column headers
- **Rows 4+**: Channel entries with pre-populated examples
- **Data validation**:
  - F4:F{n}: "PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED"
  - G4:G{n}: "Yes, No, Manual, Custom, N/A"
- **Input column**: H (Notes) - yellow fill
- **Column widths**: A=28, B=30, C=25, D=22, E=20, F=18, G=15, H=30

#### Sheet 5: Physical_Transfer
- **Type**: Data entry
- **Row 1**: Section title (merged A1:H1)
- **Row 3**: Column headers
- **Rows 4+**: Transfer type entries
- **Data validation**: F4:F{n}: "PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED"
- **Input column**: H (Notes) - yellow fill
- **Column widths**: A=25, B=28, C=30, D=25, E=28, F=18, G=25, H=30

#### Sheet 6: Verbal_Transfer
- **Type**: Data entry
- **Row 1**: Section title (merged A1:G1)
- **Row 3**: Column headers
- **Rows 4+**: Communication type entries
- **Data validation**: E4:E{n}: "PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED"
- **Input column**: G (Notes) - yellow fill
- **Column widths**: A=30, B=35, C=28, D=28, E=18, F=28, G=30

#### Sheet 7: Evidence_Register
- **Type**: Data entry
- **Row 1**: Section title (merged A1:H1)
- **Row 3**: Column headers
- **Rows 4-8**: Pre-populated evidence entries
- **Rows 9+**: Empty rows for additional entries
- **Data validation**:
  - H4:H{n}: "Pending, Collected, Verified, Expired, N/A"
  - B4:B{n}: Evidence type dropdown
- **Input columns**: E, F, G, H - yellow fill
- **Column widths**: A=15, B=20, C=35, D=20, E=30, F=15, G=18, H=12

#### Sheet 8: Approval_SignOff
- **Type**: Sign-off form
- **Row 1**: Section title (merged A1:F1)
- **Rows 3-6**: Document information
- **Rows 8+**: Approval signature table
- **Rows {n}+**: Version history table
- **Data validation**: Status column: "Pending, Approved, Rejected, Deferred"
- **Input columns**: B-F in approval rows - yellow fill
- **Column widths**: A=25, B=25, C=20, D=15, E=15, F=30

### 9.3 Styling Specifications

| Style Element | Specification |
|--------------|---------------|
| Header Fill | Navy (#003366) |
| Subheader Fill | Blue (#4472C4) |
| Input Fill | Light Yellow (#FFFFCC) |
| Locked Fill | Light Grey (#F2F2F2) |
| PUBLIC colour | Light Blue (#74C0FC) |
| INTERNAL colour | Light Green (#69DB7C) |
| CONFIDENTIAL colour | Orange (#FFA94D) |
| RESTRICTED colour | Red (#FF6B6B) |
| Allowed colour | Green (#C6EFCE) |
| Conditional colour | Amber (#FFEB9C) |
| Not Allowed colour | Red (#FFC7CE) |
| Header Font | Calibri 14pt Bold White |
| Body Font | Calibri 11pt |
| Border | Thin black all sides |

### 9.4 Data Validation Rules

| Field | Type | Values |
|-------|------|--------|
| Policy Status | List | Draft, Under Review, Approved, Needs Update |
| Transfer Permission | List | Allowed, Conditional, Not Allowed |
| Approval Required | List | Yes, No, Varies, Technical Review |
| Max Classification | List | PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED |
| DLP Integration | List | Yes, No, Manual, Custom, N/A |
| Evidence Status | List | Pending, Collected, Verified, Expired, N/A |
| Approval Status | List | Pending, Approved, Rejected, Deferred |

---

## 10. Integration Points

### 10.1 Stacked Control Dependencies

| Control | Integration |
|---------|-------------|
| A.5.12-13 | Classification levels from this control determine transfer method permissions |
| A.8.24 | Encryption requirements referenced in Electronic_Transfer sheet |
| A.8.12 | DLP integration status aligns with Data Leakage Prevention control |
| A.8.15 | Logging requirements support this control's audit trail needs |

### 10.2 Data Flow to Other A.5.14 Workbooks

```
A.5.14.1 (Transfer Rules) ──► A.5.14.2 (Channel Assessment)
    │                              │
    │  Rules define what          │  Assessment verifies
    │  channels must support      │  channels meet rules
    │                              │
    └──────────────────────────────┼──► A.5.14.5 (Consolidation)
                                   │
A.5.14.3 (Agreements) ─────────────┘
    │
    │  Agreements reference
    │  transfer rules for
    │  third parties
    │
A.5.14.4 (Monitoring) ─────────────────► A.5.14.5
    │
    │  Incidents tracked against
    │  rule violations
```

---

## 11. Audit Considerations

### 11.1 Stage 1 Evidence (Documentation Review)
- Completed Transfer_Policy sheet showing all mandatory elements
- Transfer_Methods matrix with clear permissions per classification
- Evidence_Register with policy document references

### 11.2 Stage 2 Evidence (Operational Effectiveness)
- Sample transfer audit logs (30-day period)
- DLP incident reports showing policy enforcement
- User awareness training completion records
- Chain of custody documentation samples

### 11.3 Common Auditor Questions
1. "How do you ensure CONFIDENTIAL data isn't sent via unauthorised channels?"
2. "What happens if someone needs to transfer RESTRICTED information urgently?"
3. "How are third-party transfer requirements communicated to external partners?"
4. "Show me evidence that users are trained on these transfer rules."

---

## 12. Generator Script Reference

**Script**: `generate_a514_1_transfer_rules_procedures.py`

**Location**: `10-isms-scr-base/isms-a.5.14-information-transfer/10_generator-master/`

**Key Functions**:
- `create_instructions_sheet()`: Instructions and colour legend
- `create_transfer_policy_sheet()`: Policy element documentation
- `create_transfer_methods_sheet()`: Classification-method matrix
- `create_electronic_transfer_sheet()`: Electronic channel rules
- `create_physical_transfer_sheet()`: Physical transfer procedures
- `create_verbal_transfer_sheet()`: Verbal communication protocols
- `create_evidence_register_sheet()`: Evidence tracking
- `create_approval_signoff_sheet()`: Sign-off and version history

**Execution**:
```bash
cd 10-isms-scr-base/isms-a.5.14-information-transfer/10_generator-master
python3 generate_a514_1_transfer_rules_procedures.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"The single biggest problem in communication is the illusion that it has taken place."*
— George Bernard Shaw

<!-- QA_VERIFIED: 2026-02-04 -->
