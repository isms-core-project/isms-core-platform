# ISMS-IMP-A.5.14.2 — Channel Security Assessment

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.14.2 |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.14 (Information Transfer) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.14 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.14 (Information Transfer Policy)
- ISMS-IMP-A.5.14.1 (Transfer Rules and Procedures)
- ISMS-IMP-A.5.14.4 (Compliance Monitoring Dashboard)
- ISMS-POL-A.8.24 (Use of Cryptography)
- ISMS-POL-A.8.12 (Data Leakage Prevention)

---

# PART I: USER COMPLETION GUIDE

## 1. Assessment Overview

### 1.1 Purpose

The **Channel Security Assessment Workbook** (ISMS-IMP-A.5.14.2) provides a structured evaluation of security controls across all information transfer channels. This assessment verifies that email systems, cloud services, file transfer platforms, and physical transfer methods meet security requirements defined in ISMS-POL-A.5.14.

### 1.2 Scope

This assessment covers:
- **Email systems**: Corporate email security controls and configuration
- **Cloud services**: Cloud storage and sharing platform security
- **File transfer systems**: SFTP, MFT, API gateway security evaluation
- **Physical channels**: USB, courier, and physical media security
- **Risk assessment**: Channel-specific risk analysis and scoring

### 1.3 Business Value

Completing this assessment delivers:
- **Security gap identification** across transfer channels
- **Risk-based prioritisation** of remediation efforts
- **Compliance evidence** demonstrating control effectiveness
- **Baseline documentation** for continuous improvement
- **Audit preparation** with structured assessment data

### 1.4 Control Requirement

> *ISO/IEC 27001:2022 Annex A.5.14 — Information Transfer*
>
> "Information transfer rules, procedures, or agreements should be in place for all types of transfer facilities within the organization and between the organization and other parties."

The Channel Security Assessment verifies that transfer facilities meet the rules and procedures established in A.5.14.1.

---

## 2. Prerequisites

Before starting this assessment, ensure you have:

### 2.1 Required Documents
- [ ] ISMS-IMP-A.5.14.1 (Transfer Rules and Procedures) — defines expected configurations
- [ ] ISMS-POL-A.8.24 (Cryptography Policy) — encryption standards
- [ ] IT Asset Inventory — list of transfer systems
- [ ] Network diagrams showing transfer data flows
- [ ] Previous assessment results (if available)

### 2.2 Required Access
- [ ] Email administration console (Exchange, Google Workspace)
- [ ] Cloud service admin portals (Microsoft 365, AWS, Azure)
- [ ] File transfer system configuration
- [ ] Security tool dashboards (DLP, CASB, endpoint protection)
- [ ] Audit log access for all transfer systems

### 2.3 Required Personnel
- [ ] Email/Messaging Administrator
- [ ] Cloud Services Administrator
- [ ] Network Security Engineer
- [ ] Infrastructure/Platform Team Lead
- [ ] Physical Security Manager
- [ ] Risk Management Representative

---

## 3. Workbook Structure

The workbook contains **8 sheets** organised as follows:

| Sheet | Purpose | Input Required |
|-------|---------|----------------|
| Instructions | Guidance and rating legend | None (read-only) |
| Email_Assessment | Corporate email security evaluation | Configuration, Status, Gaps |
| Cloud_Services | Cloud storage and sharing assessment | Configuration, Status, Gaps |
| File_Transfer | SFTP, MFT, API systems assessment | Current State, Status |
| Physical_Channels | Physical media and courier evaluation | Current Practice, Status |
| Risk_Assessment | Channel-specific risk analysis | Likelihood, Impact, Treatment |
| Evidence_Register | Supporting documentation tracking | Location, Status |
| Approval_SignOff | Assessment approval workflow | Signatures, Dates |

---

## 4. Completion Walkthrough

### Sheet 1: Instructions

**Purpose**: Provides assessment methodology and rating definitions.

**Actions**:
1. Review the assessment purpose and scope
2. Understand the rating scale:
   - **Compliant**: Control fully implemented and effective
   - **Partial**: Control partially implemented, gaps exist
   - **Non-Compliant**: Control not implemented or ineffective
   - **N/A**: Control not applicable to this channel
3. Note the priority ratings for remediation (Critical, High, Medium, Low)
4. Proceed to Email_Assessment sheet

### Sheet 2: Email_Assessment

**Purpose**: Evaluate security controls for corporate email systems.

**Assessment Areas**:
- Transport Encryption (TLS, DANE/MTA-STS)
- Message Encryption (S/MIME, PGP)
- Authentication (SPF, DKIM, DMARC)
- Anti-Malware (attachment scanning, URL sandboxing)
- Data Loss Prevention (DLP policies)
- Logging and Monitoring (audit logs, message tracking)
- Access Control (MFA, Conditional Access)

**For Each Control, Complete**:

| Column | Action | Example |
|--------|--------|---------|
| Actual Configuration | Document current setting | "TLS 1.3 enforced, DANE configured" |
| Status | Select assessment rating | "Compliant" |
| Evidence | Reference supporting evidence | "EV-514-CSA-001" |
| Gap Description | Describe any deficiency | "DKIM key is 1024-bit, should be 2048" |
| Remediation | Proposed fix if not compliant | "Rotate to 2048-bit DKIM key" |
| Priority | Remediation urgency | "Medium" |

**Email Security Checklist**:
- [ ] TLS 1.2+ enforcement verified
- [ ] DMARC policy at p=reject
- [ ] S/MIME certificates available for CONFIDENTIAL+
- [ ] DLP policies detect sensitive data patterns
- [ ] External forwarding blocked or monitored
- [ ] MFA enforced for all email access

### Sheet 3: Cloud_Services

**Purpose**: Assess security of cloud storage and sharing platforms.

**Services to Assess**:
- SharePoint/OneDrive
- Microsoft Teams
- Box/Dropbox (if used)
- AWS S3 (if applicable)
- Azure Blob Storage (if applicable)
- Google Drive (if applicable)

**For Each Service Control, Document**:

| Column | Description | Example |
|--------|-------------|---------|
| Service | Platform being assessed | "SharePoint/OneDrive" |
| Control Area | Security domain | "External Sharing" |
| Requirement | Expected configuration | "Restricted to approved domains" |
| Configuration | Actual setting | "External sharing enabled for all" |
| Status | Assessment rating | "Non-Compliant" |
| Gap | Description of deficiency | "No domain restrictions configured" |
| Remediation | Recommended action | "Configure sharing domain allowlist" |
| Priority | Urgency level | "High" |

**Cloud Security Checklist**:
- [ ] Encryption at rest verified (AES-256)
- [ ] Encryption in transit verified (TLS 1.2+)
- [ ] External sharing restrictions configured
- [ ] Sensitivity labels applied to content
- [ ] Audit logging enabled
- [ ] DLP or CASB integration active

### Sheet 4: File_Transfer

**Purpose**: Evaluate security of file transfer systems and APIs.

**Systems to Assess**:
- SFTP Server
- Managed File Transfer (MFT) Platform
- API Gateway
- Legacy FTP (document deprecation plan)

**For Each System, Assess**:

| Column | Description | Example |
|--------|-------------|---------|
| System Type | Transfer platform | "SFTP Server" |
| Control | Security requirement | "Authentication" |
| Requirement | Expected configuration | "Key-based auth required, password disabled" |
| Current State | Actual configuration | "Password auth still enabled for 3 accounts" |
| Status | Assessment rating | "Partial" |
| Evidence | Reference to proof | "EV-514-CSA-004" |
| Gap | Description of issue | "Legacy accounts still use passwords" |
| Remediation | Fix action | "Migrate to SSH keys, disable password auth" |
| Priority | Urgency | "High" |

**File Transfer Security Checklist**:
- [ ] SSH 2.0 only (deprecated algorithms disabled)
- [ ] Key-based authentication enforced where possible
- [ ] Chroot jails configured for user isolation
- [ ] All transfers logged with user/file/timestamp
- [ ] AES-256 encryption for data at rest (MFT)
- [ ] API authentication uses OAuth 2.0 or mTLS

### Sheet 5: Physical_Channels

**Purpose**: Assess security of physical media and courier transfers.

**Channels to Assess**:
- USB/Removable Media
- Courier Services
- Internal Mail
- Backup Media
- Print/Fax

**For Each Channel, Document**:

| Column | Description | Example |
|--------|-------------|---------|
| Channel | Physical transfer method | "USB/Removable Media" |
| Control Area | Security domain | "Device Encryption" |
| Requirement | Expected control | "Hardware encrypted USB only (FIPS 140-2)" |
| Current Practice | What actually happens | "Mix of encrypted and unencrypted USB in use" |
| Status | Assessment rating | "Partial" |
| Evidence | Supporting proof | "Device inventory report" |
| Gap | Issue description | "20% of USB devices are not encrypted" |
| Remediation | Fix action | "Replace unencrypted USB with approved devices" |
| Priority | Urgency | "High" |

**Physical Channel Checklist**:
- [ ] Approved USB device list maintained
- [ ] DLP enforces USB device policies
- [ ] Courier vendor list vetted and documented
- [ ] Tamper-evident packaging used for CONFIDENTIAL+
- [ ] Backup media encrypted before transport
- [ ] Secure print (PIN release) configured

### Sheet 6: Risk_Assessment

**Purpose**: Perform risk analysis for each transfer channel.

**Risk Assessment Methodology**:

| Likelihood | Description |
|------------|-------------|
| Rare | May occur in exceptional circumstances |
| Unlikely | Could occur but not expected |
| Possible | Might occur at some time |
| Likely | Will probably occur |
| Almost Certain | Expected to occur regularly |

| Impact | Description |
|--------|-------------|
| Negligible | Minimal or no effect |
| Minor | Limited effect, easily recoverable |
| Moderate | Significant effect, recovery needed |
| Major | Serious effect, prolonged recovery |
| Severe | Catastrophic, potentially unrecoverable |

**For Each Channel Risk, Complete**:

| Column | Description | Example |
|--------|-------------|---------|
| Channel | Transfer method | "Corporate Email" |
| Threat Scenario | What could go wrong | "Data interception in transit" |
| Likelihood | Probability rating | "Unlikely" |
| Impact | Consequence rating | "Major" |
| Inherent Risk | Risk before controls | "High" |
| Current Controls | Mitigations in place | "TLS, S/MIME available" |
| Control Effectiveness | How well controls work | "Effective" |
| Residual Risk | Risk after controls | "Medium" |
| Treatment | Risk response | "Mitigate" |
| Owner | Accountable person | "Email Administrator" |

**Common Transfer Risks**:
- Data interception in transit
- Malware distribution via attachment
- Accidental disclosure to wrong recipient
- Unauthorised external sharing
- Data breach at cloud provider
- Brute force attack on credentials
- Loss or theft of physical media
- Package interception

### Sheet 7: Evidence_Register

**Purpose**: Track all supporting evidence for the assessment.

**For Each Evidence Item**:

| Column | Action | Example |
|--------|--------|---------|
| Evidence ID | Unique identifier | "EV-514-CSA-001" |
| Evidence Type | Document category | "Configuration Export" |
| Description | What it demonstrates | "Email transport rules export" |
| Related Assessment | Which sheet it supports | "Email_Assessment" |
| Location/Link | Where stored | "SharePoint/ISMS/Evidence/A.5.14.2" |
| Date Collected | When gathered | "15.01.2026" |
| Collected By | Who gathered it | "Email Administrator" |
| Status | Current status | "Verified" |

**Evidence Types**:
- Configuration Export
- Screenshot
- Audit Report
- Policy Document
- Log Sample
- Vendor Certification
- Assessment Report

### Sheet 8: Approval_SignOff

**Purpose**: Formal sign-off for the assessment.

**Complete**:
1. **Document Information**: Verify pre-filled data
2. **Assessment Summary**: Count of items by status per assessment area
3. **Approval Signatures**: Obtain required sign-offs

| Role | Responsibility |
|------|----------------|
| Assessment Lead | Primary assessor, data accuracy |
| IT Security Manager | Technical validation |
| Information Security Officer | Overall assessment approval |

---

## 5. Evidence Collection

### 5.1 Evidence by Assessment Area

| Area | Required Evidence |
|------|-------------------|
| Email_Assessment | TLS reports, DMARC records, DLP configuration, audit log samples |
| Cloud_Services | Sharing settings export, encryption verification, CASB reports |
| File_Transfer | SFTP config, cipher suites, access logs, authentication settings |
| Physical_Channels | USB inventory, courier contracts, encryption verification |
| Risk_Assessment | Risk register extract, control effectiveness testing results |

### 5.2 Evidence Storage

Store all evidence in:
```
/ISMS/Evidence/A.5.14-Information-Transfer/
├── A.5.14.2-Channel-Assessment/
│   ├── Email/
│   ├── Cloud/
│   ├── File-Transfer/
│   ├── Physical/
│   └── Risk/
```

### 5.3 Evidence Naming

Format: `EV-514-CSA-[Area]-[Description]-[YYYYMMDD].[ext]`

Examples:
- `EV-514-CSA-EMAIL-TLS-Report-20260115.pdf`
- `EV-514-CSA-CLOUD-SharePoint-Sharing-20260115.xlsx`
- `EV-514-CSA-SFTP-CipherConfig-20260115.txt`

---

## 6. Common Pitfalls

### ❌ MISTAKE: Assessing only production systems, ignoring dev/test environments
✅ CORRECT: Include all environments that handle real data or connect to production

### ❌ MISTAKE: Accepting vendor claims without verification
✅ CORRECT: Request configuration exports, run verification tests, check audit logs

### ❌ MISTAKE: Rating "Partial" without documenting specific gaps
✅ CORRECT: Always document exactly what is missing and what remediation is needed

### ❌ MISTAKE: Skipping risk assessment because technical controls are "good"
✅ CORRECT: Complete risk assessment to identify threats controls may not address

### ❌ MISTAKE: Not testing email encryption end-to-end
✅ CORRECT: Send test messages externally to verify TLS enforcement

### ❌ MISTAKE: Assuming cloud provider handles all security
✅ CORRECT: Verify customer-managed controls (sharing, DLP, access) are configured

### ❌ MISTAKE: Documenting deprecated systems as "N/A"
✅ CORRECT: Document with "Non-Compliant" status and deprecation timeline

### ❌ MISTAKE: Not validating DLP rule effectiveness
✅ CORRECT: Test DLP with sample sensitive data to verify detection

### ❌ MISTAKE: Ignoring physical channels in "digital-first" assessments
✅ CORRECT: USB, backup media, and printed documents remain significant risks

### ❌ MISTAKE: Missing evidence for "Compliant" ratings
✅ CORRECT: Every "Compliant" rating requires supporting evidence reference

---

## 7. Quality Checklist

Before submitting the assessment, verify:

### Assessment Completeness
- [ ] All pre-populated control areas have been assessed
- [ ] Every control has a Status rating assigned
- [ ] All gaps have specific descriptions
- [ ] Remediation actions are actionable and assigned
- [ ] Priority ratings reflect business impact

### Email Assessment
- [ ] Transport encryption (TLS) verified with evidence
- [ ] DMARC policy documented with actual setting
- [ ] DLP configuration assessed
- [ ] MFA enforcement confirmed

### Cloud Services
- [ ] All cloud storage platforms assessed
- [ ] External sharing settings documented
- [ ] Encryption (rest and transit) verified
- [ ] Audit logging status confirmed

### File Transfer
- [ ] All file transfer systems included
- [ ] Legacy systems documented with deprecation plans
- [ ] Authentication methods assessed
- [ ] Encryption ciphers verified

### Physical Channels
- [ ] USB device policy enforcement verified
- [ ] Courier security assessed
- [ ] Backup media encryption confirmed
- [ ] Secure print configuration checked

### Risk and Evidence
- [ ] Risk assessment complete for all channels
- [ ] All evidence items have location references
- [ ] Evidence status is current
- [ ] All approvals obtained

---

## 8. Review and Approval

### 8.1 Assessment Frequency
- **Full assessment**: Annual
- **High-risk channels**: Quarterly review
- **Ad-hoc**: After security incidents or major changes

### 8.2 Approval Workflow
1. **Assessment Lead** completes technical evaluation
2. **IT Security Manager** validates findings
3. **ISO** approves final assessment
4. **Remediation tracking** initiated for gaps

### 8.3 Post-Assessment Actions
- Generate remediation action items
- Update risk register with residual risks
- Schedule follow-up assessment for critical gaps
- Report executive summary to management

---

# PART II: TECHNICAL SPECIFICATION

## 9. Workbook Technical Details

### 9.1 File Information

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.14.2 |
| **Generated Filename** | `ISMS-IMP-A.5.14.2_Channel_Security_Assessment_YYYYMMDD.xlsx` |
| **Generator Script** | `generate_a514_2_channel_security_assessment.py` |
| **Sheet Count** | 8 |
| **Primary Control** | A.5.14 (Information Transfer) |

### 9.2 Sheet Specifications

#### Sheet 1: Instructions
- **Type**: Read-only guidance
- **Row 1**: Title banner (merged A1:H1)
- **Rows 3-7**: Document metadata
- **Rows 9+**: Sheet descriptions, rating legend
- **Column widths**: A=25, B=60, C-H=20

#### Sheet 2: Email_Assessment
- **Type**: Assessment entry
- **Row 1**: Section title (merged A1:I1)
- **Row 3**: Column headers (9 columns)
- **Rows 4+**: Assessment items (15 pre-populated)
- **Data validation**:
  - E4:E{n}: "Compliant, Partial, Non-Compliant, N/A"
  - I4:I{n}: "Critical, High, Medium, Low"
- **Input columns**: D, E, F, G, H, I - yellow fill
- **Column widths**: A=20, B=28, C=35, D=30, E=15, F=20, G=30, H=30, I=12

#### Sheet 3: Cloud_Services
- **Type**: Assessment entry
- **Row 1**: Section title (merged A1:I1)
- **Row 3**: Column headers (9 columns)
- **Rows 4+**: Service assessment items (18 pre-populated)
- **Data validation**:
  - E4:E{n}: "Compliant, Partial, Non-Compliant, N/A"
  - I4:I{n}: "Critical, High, Medium, Low"
- **Input columns**: D, E, F, G, H, I - yellow fill
- **Column widths**: A=20, B=20, C=30, D=30, E=15, F=18, G=25, H=25, I=12

#### Sheet 4: File_Transfer
- **Type**: Assessment entry
- **Row 1**: Section title (merged A1:I1)
- **Row 3**: Column headers (9 columns)
- **Rows 4+**: System assessment items (17 pre-populated)
- **Data validation**:
  - E4:E{n}: "Compliant, Partial, Non-Compliant, N/A"
  - I4:I{n}: "Critical, High, Medium, Low"
- **Input columns**: D, E, F, G, H, I - yellow fill
- **Column widths**: A=18, B=20, C=35, D=30, E=15, F=18, G=25, H=25, I=12

#### Sheet 5: Physical_Channels
- **Type**: Assessment entry
- **Row 1**: Section title (merged A1:I1)
- **Row 3**: Column headers (9 columns)
- **Rows 4+**: Channel assessment items (17 pre-populated)
- **Data validation**:
  - E4:E{n}: "Compliant, Partial, Non-Compliant, N/A"
  - I4:I{n}: "Critical, High, Medium, Low"
- **Input columns**: D, E, F, G, H, I - yellow fill
- **Column widths**: A=20, B=20, C=35, D=30, E=15, F=18, G=25, H=25, I=12

#### Sheet 6: Risk_Assessment
- **Type**: Risk analysis entry
- **Row 1**: Section title (merged A1:J1)
- **Row 3**: Column headers (10 columns)
- **Rows 4+**: Risk scenarios (14 pre-populated)
- **Data validation**:
  - C4:C{n}: "Rare, Unlikely, Possible, Likely, Almost Certain"
  - D4:D{n}: "Negligible, Minor, Moderate, Major, Severe"
  - E4:E{n}, H4:H{n}: "Low, Medium, High, Critical"
  - G4:G{n}: "Effective, Partially Effective, Ineffective, Not Assessed"
  - I4:I{n}: "Accept, Mitigate, Transfer, Avoid"
- **Input columns**: C, D, E, G, H, I, J - yellow fill
- **Column widths**: A=18, B=35, C=15, D=12, E=14, F=25, G=18, H=14, I=12, J=18

#### Sheet 7: Evidence_Register
- **Type**: Evidence tracking
- **Row 1**: Section title (merged A1:H1)
- **Row 3**: Column headers
- **Rows 4-8**: Pre-populated entries
- **Rows 9+**: Empty rows for additional evidence
- **Data validation**: H4:H{n}: "Pending, Collected, Verified, Expired, N/A"
- **Input columns**: E, F, G, H - yellow fill
- **Column widths**: A=18, B=20, C=35, D=20, E=30, F=15, G=18, H=12

#### Sheet 8: Approval_SignOff
- **Type**: Sign-off form
- **Row 1**: Section title (merged A1:F1)
- **Rows 3-6**: Document information
- **Rows 8-13**: Assessment summary table
- **Rows 15+**: Approval signatures
- **Data validation**: E column: "Pending, Approved, Rejected, Deferred"
- **Column widths**: A=25, B=20, C=20, D=15, E=15, F=30

### 9.3 Styling Specifications

| Style Element | Specification |
|--------------|---------------|
| Header Fill | Navy (#003366) |
| Subheader Fill | Blue (#4472C4) |
| Input Fill | Light Yellow (#FFFFCC) |
| Compliant/Pass Fill | Green (#C6EFCE) |
| Partial Fill | Amber (#FFEB9C) |
| Non-Compliant/Fail Fill | Red (#FFC7CE) |
| Header Font | Calibri 14pt Bold White |
| Body Font | Calibri 11pt |
| Border | Thin black all sides |

### 9.4 Data Validation Rules

| Field | Type | Values |
|-------|------|--------|
| Assessment Status | List | Compliant, Partial, Non-Compliant, N/A |
| Priority | List | Critical, High, Medium, Low |
| Likelihood | List | Rare, Unlikely, Possible, Likely, Almost Certain |
| Impact | List | Negligible, Minor, Moderate, Major, Severe |
| Risk Level | List | Low, Medium, High, Critical |
| Control Effectiveness | List | Effective, Partially Effective, Ineffective, Not Assessed |
| Risk Treatment | List | Accept, Mitigate, Transfer, Avoid |
| Evidence Status | List | Pending, Collected, Verified, Expired, N/A |

---

## 10. Integration Points

### 10.1 Dependencies

| Workbook | Integration |
|----------|-------------|
| A.5.14.1 | Rules define expected configurations assessed here |
| A.5.14.4 | Monitoring dashboard tracks issues found in this assessment |
| A.5.14.5 | Consolidation aggregates assessment results |
| A.8.24 | Cryptography requirements inform encryption assessments |

### 10.2 Data Flow

```
A.5.14.1 (Rules) ────► A.5.14.2 (This Assessment)
    │                       │
    │  Expected configs     │  Actual findings
    │  inform assessment    │  feed monitoring
    │                       ▼
    │               A.5.14.4 (Monitoring)
    │                       │
    └───────────────────────┼──► A.5.14.5 (Consolidation)
```

---

## 11. Audit Considerations

### 11.1 Stage 1 Evidence
- Assessment methodology documented
- All transfer channels identified
- Assessment schedule established

### 11.2 Stage 2 Evidence
- Completed assessment with all areas rated
- Evidence supporting "Compliant" ratings
- Remediation plans for gaps
- Risk assessment completed

### 11.3 Common Auditor Questions
1. "Show me evidence that email encryption is enforced."
2. "How did you verify cloud sharing restrictions are working?"
3. "What is your risk assessment methodology?"
4. "How are assessment findings tracked to closure?"

---

## 12. Generator Script Reference

**Script**: `generate_a514_2_channel_security_assessment.py`

**Location**: `10-isms-scr-base/isms-a.5.14-information-transfer/10_generator-master/`

**Key Functions**:
- `create_instructions_sheet()`: Methodology guidance
- `create_email_assessment_sheet()`: Email security evaluation
- `create_cloud_services_sheet()`: Cloud platform assessment
- `create_file_transfer_sheet()`: File transfer systems
- `create_physical_channels_sheet()`: Physical media assessment
- `create_risk_assessment_sheet()`: Channel risk analysis
- `create_evidence_register_sheet()`: Evidence tracking
- `create_approval_signoff_sheet()`: Assessment approval

**Execution**:
```bash
cd 10-isms-scr-base/isms-a.5.14-information-transfer/10_generator-master
python3 generate_a514_2_channel_security_assessment.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"Security is always excessive until it's not enough."*
— Robbie Sinclair

<!-- QA_VERIFIED: 2026-02-04 -->
