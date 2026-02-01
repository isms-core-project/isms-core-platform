**ISMS-IMP-A.5.31.5: Evidence Management Process**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.31: Legal, Statutory, Regulatory and Contractual Requirements

**Document ID**: ISMS-IMP-A.5.31.5  
**Title**: Evidence Management Process  
**Version**: 1.0  
**Related Policy**: ISMS-POL-A.5.31.4 (Change Management & Evidence Framework)  
**Purpose**: Operational guide for collecting, organizing, and maintaining evidence of regulatory compliance

---

# PART I: USER COMPLETION GUIDE
**Audience:** Security assessors, Control owners, Compliance officers

---

# Process Overview

## Purpose

This implementation guide operationalizes the evidence framework defined in ISMS-POL-A.5.31.4. It provides step-by-step instructions for compliance, security, and operational personnel to systematically collect, verify, organize, and maintain evidence that demonstrates [Organization]'s compliance with regulatory requirements.

**What This Guide Is**:

- Operational "how-to" for evidence lifecycle management
- Structured process from identification through audit presentation
- Practical guidance on evidence types, quality, and organization
- Audit readiness methodology


**What This Guide Is Not**:

- Control implementation guide (evidence demonstrates controls, doesn't implement them)
- Audit procedures (how auditors examine evidence)
- Legal advice on evidence sufficiency


## When to Use This Process

**Trigger Events**:

1. **Control Implementation**: New control implemented → Collect initial evidence
2. **Periodic Collection**: Scheduled evidence refresh (monthly, quarterly, annual)
3. **Regulatory Requirement**: Specific regulation mandates evidence retention
4. **Audit Preparation**: Pre-audit evidence gathering and organization
5. **Gap Remediation**: Gap closed, new control implemented → Collect evidence
6. **Regulatory Change**: Regulation amended, evidence requirements change
7. **Compliance Demonstration**: External stakeholder (customer, regulator) requests proof
8. **Control Effectiveness Testing**: Periodic validation that controls work as intended

## Who Performs This Process

**Primary Roles**:

- **Control Owners**: Collect evidence for their controls, verify evidence quality
- **Compliance Officer**: Coordinate evidence collection, validate completeness, maintain Evidence Register
- **ISMS Manager**: Oversee evidence framework, ensure audit readiness


**Supporting Roles**:

- System Administrators: Extract logs, configurations, system-generated evidence
- HR: Provide training records, background check confirmations
- Procurement: Provide vendor contracts, due diligence documentation
- Internal Audit: Validate evidence quality, conduct pre-audit reviews
- Legal Counsel: Confirm evidence meets legal/regulatory standards


## Process Flowchart

```
[Trigger: Control implemented, scheduled collection, audit prep]
         ↓
[STEP 1: Evidence Identification]

- Review Control Mapping Matrix (which controls mapped to requirements)
- Identify evidence needed per control
- Determine evidence types appropriate for control

         ↓
[STEP 2: Evidence Collection]

- Control Owners collect evidence
- System administrators export technical evidence
- Operational teams provide process evidence

         ↓
[STEP 3: Evidence Verification]

- Validate authenticity (is this what it claims to be?)
- Validate completeness (does it demonstrate control fully?)
- Validate timeliness (is it current, or expired?)

         ↓
[STEP 4: Evidence Organization]

- Store in structured repository
- Apply naming conventions
- Link to requirements and controls
- Update Evidence Register

         ↓
[STEP 5: Evidence Maintenance]

- Monitor for expiration (approaching Valid Until date)
- Refresh as needed (per Refresh Frequency)
- Version control (when evidence updated)

         ↓
[STEP 6: Audit Preparation]

- Assemble evidence packages per regulation
- Validate all requirements have supporting evidence
- Identify gaps (missing or inadequate evidence)
- Pre-audit review (internal validation)

         ↓
[STEP 7: Evidence Presentation]

- Provide evidence to auditors in organized manner
- Explain evidence context and relevance
- Address auditor questions

         ↓
[Complete - Evidence supports compliance demonstration]
```

## Timeline

**Initial Evidence Collection** (new control):

- Identification: 1-2 hours
- Collection: 2-8 hours (depending on control complexity)
- Verification: 1-2 hours
- Organization: 1 hour
- **Total**: 1-2 days per control


**Periodic Evidence Refresh**:

- Collection: 1-4 hours
- Verification: 30 min - 1 hour
- Organization: 30 min
- **Total**: Half-day per control


**Comprehensive Audit Preparation** (all regulations):

- Evidence gap analysis: 2-3 days
- Missing evidence collection: 1-2 weeks
- Organization and packaging: 2-3 days
- Pre-audit review: 1-2 days
- **Total**: 3-4 weeks before audit


## Prerequisites

**Before Beginning Evidence Management**:

✅ Control Mapping Matrix complete (know which controls map to which requirements)  
✅ Controls implemented (evidence demonstrates implementation, not plans)  
✅ Evidence Register template prepared (Workbook 5)  
✅ Evidence repository established (file system, SharePoint, DMS)  
✅ Control Owners identified and trained  
✅ Evidence retention requirements understood (from regulations)

---

# Detailed Process Steps

## Step 1: Evidence Identification

### Review Control Mappings

**Purpose**: Understand which controls need evidence based on regulatory requirements

**Actions**:
1. **Access Control Mapping Matrix** (Workbook 4)
2. **For each regulation**, identify all controls with Primary (P) mappings
3. **For each Primary-mapped control**, note:

   - Which requirement(s) the control satisfies
   - Control implementation status (implemented, planned, in progress)
   - Control Owner


**Output**: List of controls requiring evidence, organized by regulation

**Example**:
```
Regulation: GDPR

Controls Requiring Evidence:

- A.5.10 Acceptable Use of Information → REQ-GDPR-05 (Data minimization)
- A.8.24 Use of Cryptography → REQ-GDPR-32 (Encryption)
- A.5.26 Response to Information Security Incidents → REQ-GDPR-33 (Breach notification)
- A.5.34 Privacy and Protection of PII → REQ-GDPR-05, REQ-GDPR-25 (Data protection principles, privacy by design)
- CTRL-ORG-005 DPIA Process → REQ-GDPR-35 (DPIAs)

[... etc ...]
```

### Determine Evidence Types

**For each control**, identify what types of evidence would demonstrate implementation and effectiveness.

**Evidence Type Framework**:

**1. Policy Evidence** (Organizational controls)

- **What**: Approved policy documents, procedures, standards, guidelines
- **Demonstrates**: Governance, management intent, documented requirements
- **Example**: Information Security Policy v3.0 (approved by Executive, effective 2024-01-01)
- **Typical Controls**: A.5.1 Policies, A.5.10 Acceptable Use, A.5.15 Access Control Policy


**2. Procedure Evidence** (Operational controls)

- **What**: Documented procedures, work instructions, playbooks
- **Demonstrates**: How control is operationalized, step-by-step implementation
- **Example**: Incident Response Procedure v2.1 (breach notification workflow, escalation criteria)
- **Typical Controls**: A.5.26 Incident Response, A.5.24 Incident Planning, A.6.8 Disciplinary Process


**3. Configuration Evidence** (Technical controls)

- **What**: System configurations, settings exports, technical specifications
- **Demonstrates**: Technical implementation, control parameters
- **Example**: Firewall ruleset export (showing network segmentation), database encryption settings screenshot
- **Typical Controls**: A.8.24 Cryptography, A.8.20 Networks Security, A.8.22 Network Segregation


**4. Log Evidence** (Monitoring controls)

- **What**: Security logs, access logs, audit trails, event records
- **Demonstrates**: Control in operation, ongoing monitoring, historical activity
- **Example**: SIEM logs showing failed login attempts and account lockouts (access control enforcement)
- **Typical Controls**: A.8.15 Logging, A.8.16 Monitoring Activities, A.5.18 Access Rights


**5. Report Evidence** (Assessment controls)

- **What**: Assessment reports, audit reports, compliance reports, dashboards
- **Demonstrates**: Control effectiveness, compliance status, management oversight
- **Example**: Quarterly vulnerability scan report, annual penetration test report
- **Typical Controls**: A.8.8 Vulnerability Management, A.8.29 Security Testing


**6. Certificate/Attestation Evidence** (Certification controls)

- **What**: Third-party certifications, attestations, compliance certificates
- **Demonstrates**: External validation, industry standard compliance
- **Example**: ISO 27001 certification, SOC 2 Type II report, CSA STAR attestation
- **Typical Controls**: A.5.1 Policies (references certifications), supplier assessments (A.5.19-A.5.23)


**7. Training/Competence Evidence** (People controls)

- **What**: Training records, attendance sheets, competency assessments, certifications
- **Demonstrates**: Personnel awareness, skill development, regulatory training completion
- **Example**: Security awareness training completion records (95% staff completion), GDPR training certificates
- **Typical Controls**: A.6.3 Information Security Awareness, A.6.2 Terms and Conditions of Employment


**8. Test Result Evidence** (Validation controls)

- **What**: Test results, validation reports, effectiveness testing outcomes
- **Demonstrates**: Control works as intended, effectiveness validation
- **Example**: Backup restoration test results (successful recovery in <4 hours)
- **Typical Controls**: A.5.30 ICT Readiness for Business Continuity, A.5.29 Information Security During Disruption


**9. Contract/Agreement Evidence** (Third-party controls)

- **What**: Contracts, SLAs, NDAs, vendor agreements
- **Demonstrates**: Contractual obligations, third-party commitments
- **Example**: Cloud provider contract with data processing addendum (GDPR Article 28)
- **Typical Controls**: A.5.19-A.5.23 Supplier controls, A.5.31 Legal/Regulatory Requirements


**10. Photographic/Screenshot Evidence** (Physical and visual verification)

- **What**: Photos, screenshots, videos showing physical implementation or system state
- **Demonstrates**: Visual proof of implementation, physical security measures
- **Example**: Photo of server room access control (badge reader, camera), screenshot of dashboard
- **Typical Controls**: A.7.1-A.7.14 Physical controls, system configuration controls


**Evidence Selection Criteria**:

For each control, ask:
1. **What would convince an auditor** that this control is implemented and effective?
2. **What is SPECIFIC to this control** (not generic organizational documents)?
3. **What demonstrates CURRENT state** (not historical or planned)?
4. **What is VERIFIABLE** (auditor can independently check)?

**Decision Matrix**:

| Control Type | Primary Evidence Type(s) | Secondary Evidence Type(s) |
|--------------|--------------------------|---------------------------|
| **Policy/Governance** | Policy documents | Approval records, communication emails |
| **Procedural** | Procedure documents | Training records, execution logs |
| **Technical** | Configuration exports | Screenshots, architecture diagrams |
| **Monitoring** | Logs, SIEM reports | Dashboard screenshots, alert examples |
| **Testing** | Test reports | Test plans, remediation records |
| **Training** | Training records | Course materials, competency tests |
| **Physical** | Photos, access logs | Visitor logs, maintenance records |
| **Third-party** | Contracts, SLAs | Due diligence reports, audit rights letters |

**Example Evidence Identification**:
```
Control: A.8.24 Use of Cryptography
Mapped to: REQ-GDPR-32 (Encryption for personal data)

Evidence Needed:
1. Policy Evidence:

   - Cryptography Policy v2.0 (approved, in force)
   - Key Management Procedure v1.5
   

2. Configuration Evidence:

   - Database encryption settings (TDE enabled for all customer databases)
   - API TLS configuration (TLS 1.3 enforced, cipher suites documented)
   - Key management system configuration (HSM settings, key rotation policy)
   

3. Report Evidence:

   - Quarterly encryption compliance report (scan showing all databases encrypted)
   - Key rotation logs (keys rotated per policy schedule)
   

4. Test Evidence:

   - Encryption validation test results (attempted access to encrypted data without key → failed)


Primary Evidence: Configuration exports + Encryption compliance report
Secondary Evidence: Policy + Test results
```

---

## Step 2: Evidence Collection

### Assign Collection Responsibilities

**For each evidence item**, assign to appropriate role:

**Control Owner**: Responsible for overall evidence package for their control

- Coordinates collection
- Validates evidence quality
- Ensures evidence uploaded to repository


**Technical Roles** (System Admins, DevOps, Security Engineers):

- Extract technical configurations
- Generate log exports
- Create system screenshots
- Document technical specifications


**Operational Roles** (HR, Procurement, Legal, Business Units):

- Provide operational evidence (contracts, training records, policies)
- Execute manual processes to generate evidence (testing, reviews)


**Compliance Officer**:

- Coordinate evidence collection across all Control Owners
- Track progress (Evidence Register status updates)
- Identify missing evidence


**Example Assignment**:
```
Control: A.6.3 Information Security Awareness, Education and Training
Control Owner: CISO

Evidence Items:
1. Training Records (attendance, completion) → Assigned to: HR Training Coordinator
2. Training Materials (slides, videos) → Assigned to: Security Awareness Manager
3. Competency Assessment Results → Assigned to: HR Learning & Development
4. Training Plan/Schedule → Assigned to: CISO (Control Owner - develops plan)
5. Training Effectiveness Metrics → Assigned to: Compliance Officer (calculates from HR data)

Control Owner (CISO) coordinates, validates, and uploads all evidence.
```

### Collection Methods by Evidence Type

**Policy/Procedure Documents**:
1. Locate approved version (document management system)
2. Export as PDF (preserves formatting, prevents editing)
3. Include approval metadata (approver, approval date, version number)
4. **Quality Check**: Ensure document is current (not draft), approved, and in force

**Configuration Evidence**:
1. **For Cloud Systems**: Export configuration via API or admin console

   - AWS: Use AWS Config exports, CloudFormation templates
   - Azure: Use Azure Policy exports, ARM templates
   - Google Cloud: Use Cloud Asset Inventory exports

2. **For On-Premise Systems**: Export via CLI or GUI

   - Firewall: Export ruleset (`show running-config`)
   - Database: Export encryption settings (`SELECT * FROM sys.dm_database_encryption_keys`)
   - Active Directory: Export GPO settings (`Get-GPOReport`)

3. **Document Context**: Include README explaining what configuration shows and why it demonstrates compliance
4. **Quality Check**: Ensure export is complete, includes all relevant settings, timestamped

**Logs**:
1. **Identify Time Period**: What timeframe needed? (Last 30 days, last quarter, specific incident)
2. **Extract from SIEM/Log Management**: Export relevant log entries

   - Filter to relevant events (failed logins, access grants, security alerts)
   - Include sufficient context (timestamp, user, action, result)
   - Redact sensitive data if necessary (passwords, full credit card numbers)

3. **Aggregate if High-Volume**: If millions of log entries, provide summary/statistics + sample
4. **Quality Check**: Ensure logs are readable, timestamped, cover required period

**Reports** (Vulnerability Scans, Penetration Tests, Compliance Reports):
1. **Generate from Tool**: Run scan/assessment/report from security tool
2. **Include Metadata**: Tool name, version, scan date, coverage (what was scanned)
3. **Include Executive Summary**: High-level findings + detailed results
4. **Remediation Evidence** (if report shows issues): Include follow-up evidence showing issues resolved
5. **Quality Check**: Ensure report is complete (not truncated), includes all required sections

**Certificates/Attestations**:
1. **Obtain Copy**: Request from certifying body or download from portal
2. **Verify Authenticity**: Check certificate registry (for ISO 27001, check certifying body's registry)
3. **Include Scope Statement**: What is covered by certification (entire org, specific locations, specific processes)
4. **Quality Check**: Ensure certificate is current (not expired), scope matches claims

**Training Records**:
1. **Export from LMS/HRIS**: Learning Management System or HR Information System
2. **Include**: Employee name/ID, training course, completion date, score (if assessed)
3. **Aggregate Statistics**: Calculate completion rate (% employees completed)
4. **Privacy Consideration**: Redact personally identifiable info if evidence will be shared externally
5. **Quality Check**: Ensure records are current, cover all required personnel

**Test Results**:
1. **Execute Test**: Follow test procedure (backup restore test, failover test, penetration test)
2. **Document Methodology**: What was tested, how, by whom, when
3. **Document Results**: Pass/Fail, metrics (restore time, etc.), issues identified
4. **Document Remediation** (if test revealed issues): Evidence that issues fixed
5. **Quality Check**: Test results demonstrate control effectiveness (not just that test was performed)

**Contracts/Agreements**:
1. **Obtain Fully-Executed Version**: Signed by all parties, not draft
2. **Identify Relevant Clauses**: Highlight/annotate sections demonstrating compliance (data processing terms, security requirements)
3. **Redact if Necessary**: Commercial terms may be redacted if sensitive (keep compliance-relevant sections)
4. **Include Amendments**: If contract amended, include amendments
5. **Quality Check**: Contract is current (not expired), parties are correct

**Screenshots**:
1. **Capture Full Context**: Include URL/system name in screenshot, timestamp if possible
2. **Annotate if Needed**: Highlight/circle relevant settings in screenshot
3. **High Resolution**: Ensure text is readable
4. **Sequence if Multi-Step**: If demonstrating process, capture each step
5. **Quality Check**: Screenshot clearly shows what it claims to show

### Evidence Collection Checklist

For each evidence item:

- [ ] **Assigned**: Responsible party identified
- [ ] **Collected**: Evidence obtained from source system/process
- [ ] **Authenticated**: Verified this is genuine evidence (not placeholder, not fake)
- [ ] **Complete**: Evidence includes all necessary components (not truncated, not partial)
- [ ] **Current**: Evidence reflects current state (not outdated)
- [ ] **Relevant**: Evidence actually demonstrates the control it's meant to support
- [ ] **Formatted**: Evidence in appropriate format (PDF for documents, CSV/Excel for data, PNG/JPG for screenshots)
- [ ] **Named**: Evidence file named per naming convention (see 2.4.2)
- [ ] **Metadata**: Evidence includes context (what it is, when collected, by whom, why it demonstrates compliance)


---

## Step 3: Evidence Verification

**Before** evidence is stored in repository and registered, verify its quality.

### Authenticity Verification

**Question**: Is this evidence genuine and trustworthy?

**Checks**:
1. **Source Verification**: Evidence came from authoritative source (official system, not someone's laptop)
2. **Timestamp Verification**: Evidence timestamp aligns with collection date (not backdated)
3. **Signature Verification** (for documents): If document should be signed, verify signatures present
4. **System-Generated Verification**: For logs/reports, verify generated by legitimate system (not manually created Excel)

**Red Flags**:

- Evidence source unknown or unverifiable
- Timestamps don't make sense (future dates, suspiciously aligned)
- Document claims to be "approved" but no approval signature/metadata
- Manual document attempting to look like system report


**Example**:
```
Evidence: Vulnerability Scan Report

Authenticity Check:
✅ Generated by Qualys (official vulnerability scanner)
✅ Report header shows scan date: 2025-01-05
✅ Report metadata shows export date: 2025-01-06 (reasonable - exported day after scan)
✅ Digital signature from Qualys present (optional but preferred)

Verdict: AUTHENTIC
```

### Completeness Verification

**Question**: Does this evidence fully demonstrate what it's meant to demonstrate?

**Checks**:
1. **Scope Check**: Evidence covers full scope of control

   - If control applies to "all systems", evidence covers all systems (not just sample)
   - If control is "quarterly", evidence shows all 4 quarters

2. **Detail Check**: Evidence includes sufficient detail to be meaningful

   - Not just "encryption enabled" but which encryption algorithm, key length, scope
   - Not just "training completed" but when, by whom, pass/fail status

3. **Context Check**: Evidence includes enough context to be understood

   - Screenshots have captions explaining what they show
   - Logs include header explaining what log source, what filter applied


**Red Flags**:

- Evidence is partial (only some systems, only some users, only some time periods)
- Evidence is high-level summary without supporting detail
- Evidence lacks context (auditor wouldn't understand what it demonstrates)


**Example**:
```
Evidence: Encryption Configuration

Incomplete Version:

- Screenshot showing "Encryption: Enabled" checkbox ❌
- Problem: Doesn't show WHAT is encrypted, WHAT algorithm, WHAT key management


Complete Version:

- Database TDE configuration export showing:

  • Database names (all customer databases listed)
  • Encryption algorithm (AES-256)
  • Encryption status (Enabled for each database)
  • Key names and key vault location
  • Last key rotation date

- README file explaining: "This configuration export demonstrates all customer databases use AES-256 encryption (satisfying REQ-GDPR-32 encryption requirement)"


Verdict: COMPLETE ✅
```

### Timeliness Verification

**Question**: Is this evidence current and relevant?

**Checks**:
1. **Freshness Check**: Evidence date aligns with "current state"

   - For ongoing controls (access logs), evidence should be recent (last 30-90 days)
   - For annual controls (penetration test), evidence should be within last 12 months
   - For configuration (system settings), evidence should be current snapshot

2. **Validity Period Check**: If evidence has expiration date (certificates, attestations), verify not expired
3. **Refresh Frequency Check**: Evidence collected per expected refresh schedule

   - Monthly reports collected monthly
   - Quarterly scans conducted quarterly


**Red Flags**:

- Evidence is stale (2+ years old for ongoing control)
- Evidence is expired (certificate shows expiration date passed)
- Evidence collection frequency doesn't match control requirement (annual test only done once 3 years ago)


**Example**:
```
Evidence: ISO 27001 Certification

Timeliness Check:

- Certificate Issue Date: 2022-01-15
- Certificate Expiry Date: 2025-01-15
- Current Date: 2025-01-10
- Validity Period: 3 years
- Time Until Expiry: 5 days ⚠️


Verdict: CURRENT but EXPIRING SOON
Action: Schedule recertification audit, obtain renewed certificate by 2025-01-15
```

### Relevance Verification

**Question**: Does this evidence actually demonstrate the control/requirement it's meant to support?

**Checks**:
1. **Control Alignment Check**: Evidence aligns with control objective

   - If control is "access control", evidence shows access restrictions (not something else)
   - If requirement mandates "logging", evidence shows logs (not just logging policy)

2. **Requirement Alignment Check**: Evidence satisfies specific regulatory language

   - If GDPR requires "encryption", evidence shows encryption (not just "security measures")
   - If regulation requires "annual testing", evidence shows annual frequency (not one-time test)

3. **Sufficiency Check**: Evidence would satisfy auditor/regulator

   - Does evidence answer the question "How do you comply with Requirement X?"
   - Would auditor accept this as proof, or ask for more?


**Red Flags**:

- Evidence is tangentially related but doesn't directly demonstrate control
- Evidence shows PLAN to implement, not actual implementation
- Evidence is generic organizational document, not control-specific


**Example**:
```
Requirement: REQ-PCI-10.2 "Implement automated audit trails for all system components"

Submitted Evidence: Information Security Policy v3.0 (mentions logging requirement)

Relevance Check:
❌ Policy states logging SHALL be implemented (requirement/intent)
❌ Policy does NOT demonstrate logging IS implemented (actual state)
❌ Auditor would reject: "Policy is fine, but show me the actual logs"

Better Evidence:
✅ SIEM dashboard screenshot showing active log collection from all in-scope systems
✅ Sample audit trail export from critical system (showing user actions logged)
✅ Log retention report (showing logs retained per PCI requirement - 1 year online, 3 years total)

Verdict: ORIGINAL EVIDENCE NOT RELEVANT, BETTER EVIDENCE NEEDED
```

### Verification Approval

**Who Approves**:

- **Control Owner**: First-line verification (knows control best)
- **Compliance Officer**: Secondary verification (regulatory expertise)
- **Internal Audit** (optional): Independent verification for high-risk controls


**Verification Sign-Off**:
Document in Evidence Register:

- Verified By: [Name]
- Verification Date: [Date]
- Verification Status: Verified / Needs Improvement / Rejected


**If Evidence Rejected**:
1. Document reason for rejection (authenticity concern, incomplete, stale, not relevant)
2. Request corrected evidence from collector
3. Re-verify when corrected evidence provided

---

## Step 4: Evidence Organization

### Evidence Repository Structure

**Recommended Structure** (file system or SharePoint):

```
/Evidence_Repository/
├── By_Regulation/
│   ├── GDPR/
│   │   ├── REQ-GDPR-05_Data_Minimization/
│   │   │   ├── A.5.10_Acceptable_Use_Policy_v2.0.pdf
│   │   │   ├── A.5.34_Privacy_Policy_v1.5.pdf
│   │   │   └── README.md (explains what evidence demonstrates)
│   │   ├── REQ-GDPR-32_Encryption/
│   │   │   ├── A.8.24_Crypto_Policy_v2.0.pdf
│   │   │   ├── A.8.24_Database_TDE_Config_2025-01-05.json
│   │   │   ├── A.8.24_API_TLS_Config_Screenshot_2025-01-05.png
│   │   │   └── A.8.24_Encryption_Compliance_Report_Q4-2024.pdf
│   │   └── [...]
│   ├── PCI_DSS/
│   │   ├── REQ-PCI-10_Logging/
│   │   └── [...]
│   └── [Other Regulations]/
│
├── By_Control/
│   ├── A.5.10_Acceptable_Use/
│   │   ├── Policy_v2.0.pdf
│   │   ├── Training_Records_2024-Q4.xlsx
│   │   └── [...]
│   ├── A.8.24_Cryptography/
│   │   ├── [Evidence files as above]
│   │   └── [...]
│   └── [All 93 ISO Controls + Organizational Controls]/
│
├── By_Evidence_Type/
│   ├── Policies/
│   ├── Procedures/
│   ├── Configurations/
│   ├── Logs/
│   ├── Reports/
│   ├── Certificates/
│   ├── Training_Records/
│   └── Contracts/
│
└── Audit_Packages/
    ├── 2025-01_ISO27001_Recertification/
    │   ├── Controls_Evidence_Index.xlsx (mapping of evidence to controls)
    │   ├── [Evidence files or links]
    │   └── Auditor_Presentation_Deck.pptx
    ├── 2024-Q4_GDPR_Compliance_Review/
    └── [Future Audits]/
```

**Primary Organization: By_Regulation**

- Most useful for compliance demonstrations
- Organizes evidence by what it proves (regulatory requirement)
- Easy to answer "Show me your GDPR compliance evidence"


**Secondary Organization: By_Control and By_Evidence_Type**

- Symbolic links or duplicates (if file system allows)
- Alternative views for different use cases


### File Naming Conventions

**Format**: `[ControlID]_[EvidenceType]_[Description]_[Date].[Extension]`

**Components**:

- **ControlID**: ISO control (A.5.10) or organizational control (CTRL-ORG-005)
- **EvidenceType**: Policy, Procedure, Config, Log, Report, Certificate, Training, Contract, Screenshot
- **Description**: Brief descriptor (no spaces, use underscores)
- **Date**: ISO format YYYY-MM-DD (for time-sensitive evidence)
- **Extension**: Appropriate for file type (.pdf, .json, .csv, .png, .xlsx, .mp4)


**Examples**:
```
A.8.24_Config_Database_TDE_Settings_2025-01-05.json
A.8.24_Report_Encryption_Compliance_Q4-2024.pdf
A.6.3_Training_Security_Awareness_Records_2024-Q4.xlsx
A.5.26_Procedure_Incident_Response_v2.1.pdf
CTRL-ORG-005_Policy_DPIA_Process_v1.0.pdf
A.7.2_Screenshot_Server_Room_Access_Control_2025-01-10.png
```

**Benefits**:

- Alphabetical sort groups evidence by control
- Date suffix shows freshness
- Evidence type visible at glance
- Searchable and filterable


### Evidence Metadata

**For each evidence file**, maintain metadata (in Evidence Register or file properties):

**Required Metadata**:

- **Evidence ID**: Unique identifier (EV-2025-001, EV-2025-002, ...)
- **Control ID**: Which control this evidence supports
- **Requirement ID(s)**: Which regulatory requirement(s) this evidence satisfies
- **Evidence Type**: Policy, Config, Log, Report, etc.
- **Evidence Description**: Brief summary of what evidence shows
- **File Location**: Path in repository
- **Collection Date**: When evidence collected/generated
- **Valid Until**: Expiration date (if applicable - certificates, time-bound reports)
- **Collected By**: Who collected (name/role)
- **Verified By**: Who verified quality (name/date)
- **Refresh Frequency**: How often evidence should be refreshed (Annual, Quarterly, Monthly, One-time)
- **Next Refresh Date**: When evidence should be re-collected


**Optional Metadata**:

- **Audit History**: Which audits this evidence used in
- **Version**: If evidence updated multiple times (v1.0, v2.0)
- **Notes**: Additional context


**Example Metadata Entry**:
```
Evidence ID: EV-2025-042
Control ID: A.8.24
Requirement IDs: REQ-GDPR-32, REQ-PCI-4.1
Evidence Type: Configuration
Evidence Description: Database Transparent Data Encryption (TDE) configuration export showing AES-256 encryption enabled for all customer databases
File Location: /Evidence_Repository/By_Regulation/GDPR/REQ-GDPR-32_Encryption/A.8.24_Config_Database_TDE_Settings_2025-01-05.json
Collection Date: 2025-01-05
Valid Until: N/A (configuration, refresh periodically but no fixed expiration)
Collected By: Database Administrator (John Smith)
Verified By: CISO (Jane Doe) - 2025-01-06
Verification Status: Verified
Refresh Frequency: Quarterly
Next Refresh Date: 2025-04-05
Audit Ready: Yes
Notes: Configuration export includes all production databases. Dev/test databases excluded (not in scope for GDPR). Key rotation logs available separately (EV-2025-043).
```

### Evidence Register Population

**Actions**:
1. **Open Evidence Register** (Workbook 5)
2. **For each collected evidence item**, create entry with all metadata
3. **Link evidence to requirements and controls**: Populate Requirement ID and Control ID columns
4. **Update status**: Verification Status = Verified (after verification complete)
5. **Set refresh schedule**: Populate Refresh Frequency and Next Refresh Date

**Quality Check**:

- Every evidence item in repository has corresponding Evidence Register entry
- Every requirement has at least one evidence item (no requirements without evidence)
- All metadata fields populated (no blank Required fields)


---

## Step 5: Evidence Maintenance

Evidence is not "collect once and forget" - it requires ongoing maintenance.

### Periodic Refresh

**Why Refresh**:

- Evidence becomes stale (configurations change, policies update)
- Regulations require current evidence (not 2-year-old reports)
- Continuous compliance demonstration (not just "we were compliant 3 years ago")


**Refresh Triggers**:
1. **Scheduled Refresh**: Based on Refresh Frequency in Evidence Register

   - Annual evidence: Refresh every 12 months
   - Quarterly evidence: Refresh every 3 months
   - Monthly evidence: Refresh every month

2. **Control Change**: If control implementation changes, refresh evidence
3. **Regulatory Change**: If regulation updates, refresh evidence to reflect new requirements
4. **Approaching Expiration**: Certificate or attestation nearing expiry

**Refresh Process**:
1. **Identify evidence due for refresh** (Next Refresh Date approaching or passed)
2. **Re-collect evidence** using same method as initial collection
3. **Verify new evidence** (same quality checks as initial verification)
4. **Version control**:

   - **Option A (Versioning)**: Keep old evidence, add new version
     - Rename old: `A.8.24_Config_DB_TDE_2024-01-05_v1.json`
     - New file: `A.8.24_Config_DB_TDE_2025-01-05_v2.json`
   - **Option B (Replacement)**: Replace old evidence with new
     - Archive old evidence (move to `/Archive/`)
     - New evidence takes same filename

5. **Update Evidence Register**:

   - Collection Date → New date
   - Next Refresh Date → Calculate based on Refresh Frequency
   - Version → Increment if using versioning
   - Last Updated → Current date


**Automation Opportunities**:

- **Calendar Reminders**: Set reminders in Evidence Register for Next Refresh Date
- **Automated Collection**: For system-generated evidence (logs, configs), script collection
- **Dashboard Alerts**: Compliance Dashboard (Workbook 6) can flag evidence approaching refresh


### Expiration Monitoring

**For evidence with expiration dates** (certificates, attestations, time-bound reports):

**Actions**:
1. **Monitor Valid Until dates** in Evidence Register
2. **Alert on approaching expiration**:

   - 90 days before: Early warning
   - 30 days before: Urgent action required
   - 7 days before: Critical escalation

3. **Renew or replace**:

   - Certificates: Initiate renewal process (recertification audit, certificate reissuance)
   - Attestations: Request updated attestation from third party
   - Reports: Re-run assessment/scan


**Example**:
```
Evidence: ISO 27001 Certificate (EV-2025-001)
Valid Until: 2025-01-15
Current Date: 2024-10-10

Alert: 90 days until expiration
Action: Schedule recertification audit with certifying body (typically 3 months lead time)

---

Current Date: 2024-12-15
Alert: 30 days until expiration
Action: Confirm audit scheduled (Jan 5-7, 2025), prepare audit evidence package

---

Current Date: 2025-01-08
Alert: 7 days until expiration
Action: Audit complete (Jan 5-7), awaiting certification decision. If delayed, request interim letter from certifying body.

---

Current Date: 2025-01-14
Action: New certificate issued (EV-2025-100), Valid Until: 2028-01-14. Update Evidence Register.
```

### Change Management Integration

**When Controls Change**, evidence must be updated.

**Trigger**: Control implementation modified (new software, policy update, process change, scope expansion)

**Process**:
1. **Control Owner notifies Compliance Officer** of control change
2. **Assess Evidence Impact**:

   - Does existing evidence still accurately reflect control?
   - If yes → No action (but document that evidence was reviewed and remains valid)
   - If no → Evidence is now inaccurate, must refresh

3. **Collect Updated Evidence**: Re-collect to reflect new control state
4. **Update Evidence Register**: Mark old evidence as superseded, add new evidence

**Example**:
```
Control: A.8.24 Use of Cryptography
Change: Migrated from on-premise HSM to cloud-based KMS (AWS KMS)

Impact Assessment:

- Old Evidence (EV-2024-200): On-premise HSM configuration export
- Status: NO LONGER ACCURATE (HSM decommissioned)


Action:

- Collect New Evidence (EV-2025-110): AWS KMS configuration export, key policies, CloudTrail logs
- Update Evidence Register:
  - EV-2024-200: Status = Superseded, Superseded By = EV-2025-110
  - EV-2025-110: Status = Verified, Supersedes = EV-2024-200
- Archive old evidence (retain for historical record, not for current compliance demonstration)

```

### Evidence Retention

**Retention Requirements**:
1. **Regulatory Mandates**: Some regulations specify evidence retention periods

   - GDPR: 3 years (typical for demonstrating historical compliance)
   - PCI DSS: 1 year online, 3 years archived (for logs and audit trails)
   - SOX: 7 years (financial records and controls)

2. **Audit Trail**: Retain evidence for audit history (show compliance over time)
3. **Legal Hold**: If litigation/investigation, retain all evidence indefinitely until released

**Retention Policy**:

- **Current Evidence**: Retain indefinitely while control is in operation
- **Superseded Evidence**: Retain for:
  - Minimum: Regulatory retention requirement (e.g., 3 years)
  - Extended: Audit cycle + 1 year (to support historical audit inquiries)
- **Obsolete Evidence** (control decommissioned): Retain per regulatory/legal requirements


**Archive Process**:
1. When evidence superseded, move to `/Archive/[Year]/`
2. Maintain Evidence Register entry but mark Status = Archived
3. If retention period expires, delete (with approval from Legal Counsel and Compliance Officer)

---

## Step 6: Audit Preparation

### Evidence Gap Analysis

**Purpose**: Before audit, ensure all requirements have supporting evidence

**Process**:
1. **Generate Evidence Coverage Report**:

   - For each regulation being audited
   - List all requirements
   - For each requirement, list supporting evidence (from Evidence Register)
   - Flag requirements with NO evidence or INADEQUATE evidence


**Coverage Report Template**:
```
Regulation: GDPR
Audit Date: 2025-02-15

| Requirement ID | Requirement | Control(s) | Evidence Count | Evidence Status | Gap? |
|----------------|-------------|------------|----------------|-----------------|------|
| REQ-GDPR-05 | Data minimization | A.5.10, A.5.34 | 3 | ✅ Complete | No |
| REQ-GDPR-32 | Encryption | A.8.24 | 4 | ✅ Complete | No |
| REQ-GDPR-33 | Breach notification | A.5.26 | 2 | ⚠️ Partial | Yes - need test evidence |
| REQ-GDPR-35 | DPIA | CTRL-ORG-005 | 1 | ⚠️ Partial | Yes - only procedure, need completed DPIAs |

Gap Summary:

- Total Requirements: 42
- Requirements with Complete Evidence: 38 (90%)
- Requirements with Partial Evidence: 3 (7%)
- Requirements with No Evidence: 1 (3%)


Action Required:

- REQ-GDPR-33: Conduct breach notification drill, document test results
- REQ-GDPR-35: Locate 3 completed DPIAs (or conduct DPIAs if not done)
- REQ-GDPR-44: Implement international transfer safeguards (gap not yet remediated)

```

**Actions**:

- **For Complete Evidence**: No action, evidence ready
- **For Partial Evidence**: Collect missing evidence items before audit
- **For No Evidence**: 
  - If control implemented but evidence not collected → Urgent collection
  - If control NOT implemented → Escalate gap (cannot satisfy audit)


### Evidence Assembly

**Purpose**: Organize evidence for easy auditor access

**Audit Package Structure**:
```
/Audit_Packages/2025-02_GDPR_Compliance_Review/
├── 00_Index_and_Overview/
│   ├── Evidence_Index.xlsx (master list of all evidence with file locations)
│   ├── Control_Mapping_Matrix.xlsx (from Workbook 4)
│   ├── Executive_Summary.pdf (compliance status overview)
│   └── Audit_Scope_Statement.pdf (what's being audited, what's excluded)
│
├── 01_Policies_and_Procedures/
│   ├── Information_Security_Policy_v3.0.pdf
│   ├── Privacy_Policy_v1.5.pdf
│   ├── Incident_Response_Procedure_v2.1.pdf
│   └── [All policy/procedure evidence]
│
├── 02_Technical_Controls/
│   ├── A.8.24_Encryption/
│   │   ├── Database_TDE_Config_2025-01-05.json
│   │   ├── API_TLS_Config_Screenshot.png
│   │   ├── Encryption_Compliance_Report_Q4-2024.pdf
│   │   └── README.md (explains what each file demonstrates)
│   ├── A.8.15_Logging/
│   └── [Other technical controls]
│
├── 03_Organizational_Controls/
│   ├── A.6.3_Training/
│   ├── A.5.19_Vendor_Management/
│   └── [Other organizational controls]
│
├── 04_Assessment_Reports/
│   ├── Vulnerability_Scan_Q4-2024.pdf
│   ├── Penetration_Test_Annual_2024.pdf
│   └── Internal_Audit_Report_2024.pdf
│
├── 05_Certifications_and_Attestations/
│   ├── ISO_27001_Certificate_2022-2025.pdf
│   ├── SOC2_Type_II_Report_2024.pdf
│   └── Cloud_Provider_Certifications/
│
└── 06_Supplementary_Evidence/
    ├── Sample_Logs/ (if full logs too large, provide representative samples)
    ├── Additional_Context/ (supporting documents, explanations)
    └── Remediation_Evidence/ (for any gaps found during audit)
```

**Evidence Index**:

- Excel workbook listing ALL evidence in audit package
- Columns: Evidence ID, Requirement ID, Control ID, File Name, Location, Description
- Sortable and filterable for auditor convenience
- Hyperlinks to evidence files (if electronic audit)


### Pre-Audit Review

**Purpose**: Validate evidence quality before auditor sees it

**Internal Review Process**:
1. **Self-Review** (Control Owner): Review own control's evidence

   - Is evidence current?
   - Does evidence clearly demonstrate control?
   - Any gaps or weaknesses auditor will identify?

2. **Peer Review** (Compliance Officer): Review evidence for regulatory alignment

   - Does evidence satisfy regulatory requirement?
   - Is evidence format professional?
   - Any concerns about evidence authenticity or quality?

3. **Mock Audit** (Internal Audit): Simulate auditor review

   - Pretend to be external auditor
   - Ask questions auditor would ask
   - Identify weaknesses or gaps before real audit


**Mock Audit Sample Questions**:
```
Requirement: REQ-GDPR-32 (Encryption for personal data)

Mock Auditor Questions:
Q1: "Show me your encryption policy."
→ Check: Do we have approved encryption policy? Is it current?

Q2: "What encryption algorithm do you use?"
→ Check: Can we answer definitively? (AES-256, not just "strong encryption")

Q3: "Show me evidence that all personal data is encrypted."
→ Check: Do we have comprehensive evidence? (Not just sample, but all databases)

Q4: "How do you manage encryption keys?"
→ Check: Do we have key management evidence? (HSM/KMS configuration, key rotation logs)

Q5: "What happens if encryption key is compromised?"
→ Check: Do we have incident response plan for crypto incidents?

Q6: "Show me test results proving encryption works."
→ Check: Do we have encryption validation test evidence?

Mock Audit Findings:

- ✅ Q1-Q4: Evidence exists and is strong
- ⚠️ Q5: Incident response plan exists but doesn't specifically address crypto key compromise scenario
- ❌ Q6: No encryption validation test on record


Action Before Real Audit:

- Enhance incident response plan to include crypto key compromise scenario
- Conduct encryption validation test, document results (EV-2025-115)

```

**Pre-Audit Checklist**:

- [ ] All requirements have supporting evidence (no zero-evidence requirements)
- [ ] All evidence is current (no stale evidence >1 year old for ongoing controls)
- [ ] All evidence is verified (Verification Status = Verified in Evidence Register)
- [ ] Evidence is organized and indexed (Audit Package assembled)
- [ ] Evidence quality reviewed (internal review complete)
- [ ] Evidence locations documented (Evidence Index current)
- [ ] Gaps identified and remediated (or risk-accepted with management approval)


---

## Step 7: Evidence Presentation

### Auditor Evidence Request

**When Auditor Asks**: "Show me evidence for Requirement X" or "How do you satisfy Control Y?"

**Response Process**:
1. **Acknowledge Request**: "Let me pull the evidence for [Requirement/Control]"
2. **Consult Evidence Index**: Locate relevant evidence in audit package
3. **Provide Evidence**: Share file(s) with auditor (electronic or printed)
4. **Explain Context**: Brief explanation of what evidence shows
5. **Answer Questions**: Address auditor follow-up questions

**Example Response**:
```
Auditor: "Show me evidence that you encrypt personal data at rest."

Response:
"We satisfy the encryption requirement through Control A.8.24 - Use of Cryptography. Let me share the evidence package..."

[Open audit package: 02_Technical_Controls/A.8.24_Encryption/]

"Here are four evidence items:

1. Encryption Policy (A.8.24_Policy_Cryptography_v2.0.pdf):

   - Approved by CISO on 2024-01-01
   - Mandates AES-256 encryption for all personal data at rest
   - Specifies key management requirements


2. Database TDE Configuration (A.8.24_Config_Database_TDE_2025-01-05.json):

   - Configuration export from all production databases
   - Shows Transparent Data Encryption (TDE) enabled
   - AES-256 algorithm, keys managed in AWS KMS


3. Encryption Compliance Report (A.8.24_Report_Encryption_Compliance_Q4-2024.pdf):

   - Quarterly scan of all databases
   - Shows 100% of customer databases encrypted
   - Any exceptions flagged (none found in Q4 2024)


4. Encryption Validation Test (A.8.24_Test_Encryption_Validation_2024-12-15.pdf):

   - Test conducted December 2024
   - Attempted to read encrypted database without key → Failed (encryption confirmed working)
   - Test conducted by Security Engineer, reviewed by CISO


Does this satisfy your evidence request, or do you need additional information?"

Auditor: "This looks good. Can you show me key rotation logs?"

Response:
"Yes, key rotation is documented in our KMS logs. Let me pull that..."
[Retrieve supplementary evidence: A.8.24_Log_KMS_Key_Rotation_2024.csv]
```

### Handling Evidence Gaps During Audit

**If Auditor Identifies Gap**: "I need evidence for X, but I don't see it in your package."

**Response Options**:

**Option 1: Evidence Exists but Not Included**

- "We have that evidence - it's in our repository but wasn't included in the audit package. Let me retrieve it."
- Action: Locate evidence in repository, add to audit package, provide to auditor
- Lesson Learned: Improve evidence packaging process to avoid missing evidence


**Option 2: Evidence Exists but Not What Auditor Wants**

- "We have [Evidence A], but it sounds like you're looking for something different. Can you clarify what would satisfy this requirement?"
- Action: Understand auditor's expectation, provide alternative evidence or explain why current evidence is sufficient
- Negotiation: Sometimes auditor has different interpretation of requirement than organization - discuss and align


**Option 3: Evidence Doesn't Exist - Control Implemented but Not Documented**

- "The control is implemented, but we haven't collected this specific evidence. Can we provide it post-audit?"
- Action: Rapid evidence collection during audit (if possible), or commit to providing within X days post-audit
- Impact: May result in audit finding ("Control implemented but evidence inadequate") with remediation requirement


**Option 4: Evidence Doesn't Exist - Control Not Implemented (Gap)**

- "We acknowledge this is a gap. The control is not yet implemented."
- Action: Transparently acknowledge gap, explain remediation plan (if exists)
- Impact: Audit finding (non-conformance), must remediate before certification/attestation


**Example**:
```
Auditor: "I need evidence that you conduct Data Protection Impact Assessments (DPIAs) for high-risk processing. I see your DPIA procedure, but where are the completed DPIAs?"

Response (Option 3):
"You're correct - we have the DPIA procedure but haven't included completed DPIAs in the audit package. We have 3 DPIAs completed to date:

- DPIA #1: Customer Analytics Platform (completed Oct 2024)
- DPIA #2: Automated Decision System (completed Nov 2024)
- DPIA #3: Biometric Authentication Pilot (completed Dec 2024)


I can retrieve these from our repository and provide them this afternoon. Would that satisfy your requirement?"

Auditor: "Yes, please provide them. Also, how do you ensure DPIAs are conducted for all high-risk processing?"

Response:
"Our DPIA procedure integrates DPIAs into our product development lifecycle. Any new product or major feature must pass a DPIA threshold assessment. If threshold met (high risk), DPIA is mandatory before launch. We track DPIAs in our Privacy Compliance Register [show register]. This ensures no high-risk processing goes live without DPIA."

[Later that day: Provide 3 completed DPIAs to auditor]

Outcome: Evidence gap closed during audit, no finding.
```

### Evidence Presentation Best Practices

**Do**:

- ✅ Be organized (know where evidence is, provide quickly)
- ✅ Be transparent (if gap exists, acknowledge it)
- ✅ Provide context (explain what evidence shows, don't assume auditor will understand)
- ✅ Be concise (provide exactly what auditor asks for, not 50 pages of tangentially related documents)
- ✅ Anticipate questions (if evidence might raise questions, proactively address)


**Don't**:

- ❌ Provide unverified evidence (don't share evidence you haven't quality-checked)
- ❌ Overwhelm auditor (don't dump 1000 pages of logs when auditor asks for "logging evidence")
- ❌ Argue with auditor (if auditor says evidence is insufficient, listen and understand their concerns)
- ❌ Fabricate evidence (NEVER create fake evidence - this is fraud and grounds for certification revocation)
- ❌ Promise evidence you can't deliver ("We'll have that for you next week" when you know you won't)


---

# Evidence Types: Detailed Guidance

## Policy Evidence

**What**: Approved policy documents

**Quality Criteria**:

- [ ] Approved by appropriate authority (Executive, Board)
- [ ] Approval date and version number visible
- [ ] Policy is current (not draft, not expired)
- [ ] Policy scope matches control scope
- [ ] Policy content addresses requirement


**Collection Method**:
1. Retrieve from document management system (DMS)
2. Export as PDF (preserves approval metadata)
3. Verify approval signature/date

**Common Issues**:

- **Issue**: Policy is draft (not approved)
  - **Fix**: Obtain approved version or expedite approval process
- **Issue**: Policy is outdated (e.g., references old organizational structure)
  - **Fix**: Update policy, obtain re-approval


**Example**:
```
Control: A.5.1 Policies for Information Security
Evidence: Information Security Policy v3.0

Quality Check:
✅ Title page shows: "Version 3.0, Approved by CEO, Effective Date 2024-01-01"
✅ Content addresses information security governance, roles, compliance
✅ Policy scope: "All employees, contractors, and third parties with access to [Organization] systems"
✅ Current (approved Jan 2024, still in force)

Verdict: QUALITY EVIDENCE
```

## Configuration Evidence

**What**: System configuration exports, settings screenshots

**Quality Criteria**:

- [ ] Export/screenshot is recent (current state)
- [ ] Export includes all relevant settings (not partial)
- [ ] Context provided (what system, what settings shown, why relevant)
- [ ] Export is readable and parseable


**Collection Method**:

- **Cloud**: API export, admin console export
- **On-premise**: CLI export (`show config`), GUI screenshot
- **Database**: SQL query results showing settings


**Common Issues**:

- **Issue**: Screenshot doesn't show enough context (cropped too tightly)
  - **Fix**: Re-screenshot with URL/breadcrumbs visible
- **Issue**: Configuration export is massive (500 pages)
  - **Fix**: Extract relevant section, provide summary + full export as appendix


**Example**:
```
Control: A.8.20 Networks Security
Evidence: Firewall Ruleset Export

Quality Check:
✅ Export date: 2025-01-10 (current)
✅ Firewall: Palo Alto PA-5220 (production firewall)
✅ Ruleset includes: Source/Dest zones, allowed protocols, deny rules
✅ README included: "This ruleset shows network segmentation between Production, DMZ, and Management networks per A.8.20 requirement. Default deny rule at end (Rule 999)."

Verdict: QUALITY EVIDENCE
```

## Log Evidence

**What**: Security logs, access logs, audit trails

**Quality Criteria**:

- [ ] Logs cover required time period
- [ ] Logs include relevant events (not just all logs)
- [ ] Logs are authentic (from real system, not manually created)
- [ ] Logs are readable (formatted, not raw binary)
- [ ] Volume is appropriate (summary if millions of entries)


**Collection Method**:
1. Define time period and event types needed
2. Export from SIEM, log management system, or application
3. Filter to relevant events (reduce noise)
4. If large volume, provide summary + sample

**Common Issues**:

- **Issue**: Logs are too verbose (millions of entries, unreadable)
  - **Fix**: Provide summary statistics + representative sample (100-1000 entries)
- **Issue**: Logs don't include enough detail (just timestamps, no user/action)
  - **Fix**: Reconfigure logging to capture required fields, re-export


**Example**:
```
Control: A.8.15 Logging
Evidence: Failed Login Attempts Log

Quality Check:
✅ Time Period: Last 90 days (Oct 1 - Dec 31, 2024)
✅ Event Type: Failed login attempts (brute force detection)
✅ Fields: Timestamp, Username, Source IP, Failure Reason
✅ Volume: 1,247 failed attempts (manageable size)
✅ Summary: "Average 14 failed attempts/day. Top 3 usernames: admin (327), root (198), test (145). All IPs blocked after 5 attempts (per policy)."

Verdict: QUALITY EVIDENCE
```

## Report Evidence

**What**: Assessment reports, scan reports, compliance reports

**Quality Criteria**:

- [ ] Report is recent (within validity period)
- [ ] Report scope matches control scope
- [ ] Report includes executive summary + detailed findings
- [ ] Report includes remediation (if findings exist)
- [ ] Report is from reputable source/tool


**Collection Method**:
1. Generate report from tool (vulnerability scanner, compliance tool)
2. Export as PDF
3. If findings exist, include remediation evidence

**Common Issues**:

- **Issue**: Report shows vulnerabilities but no remediation
  - **Fix**: Include follow-up evidence showing vulnerabilities patched
- **Issue**: Report scope incomplete (didn't scan all systems)
  - **Fix**: Re-run scan with comprehensive scope


**Example**:
```
Control: A.8.8 Management of Technical Vulnerabilities
Evidence: Quarterly Vulnerability Scan Report Q4 2024

Quality Check:
✅ Scan Date: December 15, 2024
✅ Scan Scope: All production servers (42 systems)
✅ Tool: Qualys Vulnerability Management
✅ Findings: 3 Critical, 15 High, 47 Medium, 128 Low
✅ Remediation: Critical and High findings include patch plan + completion dates
✅ Follow-up: Re-scan on Jan 5, 2025 shows all Critical/High patched

Verdict: QUALITY EVIDENCE (includes remediation proof)
```

## Training Evidence

**What**: Training records, attendance, competency assessments

**Quality Criteria**:

- [ ] Records are current (recent training cycle)
- [ ] Records include: Employee name/ID, training course, completion date, pass/fail
- [ ] Completion rate calculated (% of required personnel completed)
- [ ] Training content is relevant to control


**Collection Method**:
1. Export from Learning Management System (LMS) or HRIS
2. Calculate completion statistics
3. Redact personal info if needed (for external sharing)

**Common Issues**:

- **Issue**: Low completion rate (<80%)
  - **Fix**: Follow up with non-completers, re-run report after follow-ups
- **Issue**: Training content outdated (2019 training for 2024 requirement)
  - **Fix**: Update training content, re-train personnel


**Example**:
```
Control: A.6.3 Information Security Awareness, Education and Training
Evidence: Security Awareness Training Records Q4 2024

Quality Check:
✅ Training Course: "Annual Information Security Awareness (2024 Edition)"
✅ Required Personnel: All employees and contractors (n=487)
✅ Completion: 472 completed (97%)
✅ Completion Period: Oct 1 - Dec 31, 2024
✅ Assessment: All completers passed quiz (80% passing score)
✅ Follow-up: 15 non-completers followed up, 12 completed by Jan 10, final completion 99%

Verdict: QUALITY EVIDENCE
```

---

# Special Scenarios

## Evidence for Third-Party Controls

**Challenge**: Control is implemented by third party (cloud provider, vendor), not directly by [Organization]

**Evidence Strategy**:
1. **Third-Party Attestation**: Obtain SOC 2, ISO 27001, or other certification from vendor
2. **Contract Clauses**: Evidence that contract requires vendor to implement control
3. **Audit Rights**: Evidence of audit rights in contract + results of vendor audits
4. **Vendor Self-Assessment**: Questionnaire responses from vendor

**Example**:
```
Control: A.8.9 Configuration Management (for cloud infrastructure)
Implementation: AWS manages infrastructure configuration

Evidence:
1. AWS SOC 2 Type II Report (covers configuration management controls)
2. [Organization]-AWS Contract, Section 8.3: "AWS shall maintain configuration management per SOC 2"
3. AWS Compliance Dashboard Screenshot (showing SOC 2 certification current)
4. AWS Artifact: ISO 27001 Certificate for AWS (covers A.8.9 equivalent controls)

Note: We inherit control from AWS. Our evidence demonstrates AWS implements control and we verified through attestations.
```

## Evidence for Compensating Controls

**Challenge**: Ideal control not implemented, compensating control used instead

**Evidence Strategy**:
1. **Document Rationale**: Why ideal control not feasible
2. **Document Compensating Control**: What compensating control does
3. **Demonstrate Effectiveness**: Evidence that compensating control achieves same objective
4. **Management Approval**: Evidence that compensating approach approved

**Example**:
```
Requirement: REQ-PCI-8.3 "Implement multi-factor authentication (MFA) for all remote access"
Ideal Control: Biometric MFA (fingerprint or facial recognition)
Issue: Biometric MFA cost-prohibitive (€500K for hardware tokens + biometric scanners)

Compensating Control: Hardware security keys (YubiKey) + behavioral analytics

- Hardware security keys (FIDO2 compliant): "Something you have"
- Behavioral analytics (Okta Adaptive MFA): Detects anomalous behavior (location, device, time)
- Combined: Provides equivalent security to biometric MFA


Evidence:
1. Cost-Benefit Analysis: Document showing biometric MFA cost (€500K) vs. YubiKey + Behavioral (€80K)
2. Executive Approval: CFO and CISO approval of compensating control approach
3. Technical Evidence:

   - YubiKey deployment records (all remote users issued hardware key)
   - Okta Adaptive MFA configuration (behavioral analytics enabled)
   - Test results: Simulated attack with stolen password → Blocked by behavioral analytics

4. Effectiveness Assessment: Independent review by penetration tester confirming compensating controls provide equivalent protection
```

## Evidence for Gaps

**Challenge**: Gap exists (control not implemented), but remediation in progress

**Evidence Strategy**:
1. **Acknowledge Gap**: Transparent documentation of gap
2. **Remediation Plan**: Evidence of plan to close gap
3. **Remediation Progress**: Evidence of progress (milestones achieved)
4. **Risk Acceptance** (if gap not yet closed): Management approval to operate with gap temporarily

**Example**:
```
Requirement: REQ-GDPR-35 "Conduct DPIAs for high-risk processing"
Current State: DPIA process defined (procedure exists) but not yet executed (no completed DPIAs)

Evidence (Interim):
1. Gap Acknowledgment: Gap Register entry GAP-2025-001 (DPIA process not operational)
2. Remediation Plan: Detailed plan to implement DPIA process (Feb-Mar 2025)
3. Progress Evidence:

   - DPIA Procedure v1.0 (approved Jan 2025)
   - DPIA Template (created, legal-reviewed)
   - Training scheduled (Privacy Team training on Feb 5, 2025)
   - 3 DPIAs planned: Customer Analytics, Automated Decisions, Biometric Auth

4. Risk Acceptance: Executive Management approval to proceed with product launches while DPIA process ramping up (time-limited to Q1 2025)

Timeline:

- Feb 5: Privacy Team trained
- Feb 15-28: Conduct 3 backlog DPIAs
- Mar 1: DPIA process operational, gap closed


Interim Compliance Status: PARTIAL (process defined but not yet fully operational)
```

---

# Tools & Automation

## Evidence Register (Workbook 5)

**Purpose**: Master inventory of all evidence

**Usage**:

- Central repository of evidence metadata
- Track evidence status (verified, pending, expired)
- Monitor refresh schedules
- Generate evidence coverage reports


**Key Features**:

- Evidence ID (unique identifier)
- Links to requirements and controls
- Valid Until dates (expiration tracking)
- Next Refresh Date (maintenance scheduling)
- Audit Ready status


## Evidence Repository

**Options**:
1. **File System**: Simple folder structure on network drive

   - Pros: Easy to set up, no cost
   - Cons: Limited search, no version control, no audit trail

2. **SharePoint/OneDrive**: Cloud-based document management

   - Pros: Version control, access control, collaboration, search
   - Cons: Requires Microsoft 365 license

3. **Document Management System** (M-Files, Laserfiche, OpenText): Enterprise DMS

   - Pros: Advanced features (workflow, retention, metadata), audit trail
   - Cons: Cost, complexity

4. **Compliance Platform** (OneTrust, LogicGate, ServiceNow GRC): Integrated GRC tool

   - Pros: Integrated with control management, automated workflows
   - Cons: Significant cost


**Recommendation**: Start with SharePoint (if available), migrate to GRC platform as compliance program matures

## Automation Opportunities

**Automated Evidence Collection**:

- **Logs**: Script to export security logs monthly (cron job)
- **Configurations**: Script to export cloud configs weekly (AWS Config, Azure Policy)
- **Reports**: Schedule vulnerability scans quarterly, auto-export reports


**Automated Evidence Verification**:

- **Hash Verification**: Calculate file hash on collection, recalculate on retrieval (detect tampering)
- **Timestamp Validation**: Check file creation date matches collection date
- **Format Validation**: Verify file is expected format (PDF, JSON, CSV)


**Automated Evidence Maintenance**:

- **Expiration Alerts**: Email when evidence approaching Valid Until date
- **Refresh Reminders**: Calendar reminders when Next Refresh Date approaches
- **Dashboard**: Compliance Dashboard (Workbook 6) shows evidence status at glance


---

# Roles & Responsibilities Summary

| Role | Responsibilities in Evidence Management |
|------|----------------------------------------|
| **Control Owners** | - Collect evidence for their controls<br>- Verify evidence quality<br>- Upload to repository<br>- Maintain evidence currency |
| **Compliance Officer** | - Coordinate evidence collection<br>- Maintain Evidence Register<br>- Monitor refresh schedules<br>- Validate evidence completeness<br>- Prepare audit packages |
| **ISMS Manager** | - Oversee evidence framework<br>- Ensure audit readiness<br>- Approve evidence management procedures |
| **System Administrators** | - Extract technical evidence (logs, configs)<br>- Automate evidence collection where possible |
| **Internal Audit** | - Validate evidence quality<br>- Conduct pre-audit reviews<br>- Independent verification |
| **Legal Counsel** | - Advise on evidence retention requirements<br>- Approve evidence destruction (when retention period expires) |

---

# Continuous Improvement

## Evidence Management Metrics

**Collection Metrics**:

- Time to collect evidence (target: <2 hours per evidence item)
- Evidence collection completion rate (% evidence collected on schedule)


**Quality Metrics**:

- Evidence verification pass rate (% evidence passing quality checks on first attempt)
- Evidence rejection rate (% evidence rejected during verification)


**Maintenance Metrics**:

- Evidence refresh compliance (% evidence refreshed per schedule)
- Evidence expiration rate (% evidence expired without renewal)


**Audit Readiness Metrics**:

- Evidence coverage (% requirements with supporting evidence)
- Audit-ready percentage (% evidence marked "Audit Ready: Yes")
- Evidence gaps (count of requirements without evidence)


## Lessons Learned

**After Each Audit**:
1. **Evidence Effectiveness**: Which evidence satisfied auditors easily? Which required extensive discussion?
2. **Evidence Gaps**: What evidence was missing that auditor requested?
3. **Process Improvements**: How can evidence collection be streamlined?

**Example**:
```
Post-Audit Lessons Learned: ISO 27001 Recertification (Jan 2025)

Evidence That Worked Well:

- Configuration exports (auditor appreciated technical detail)
- Completed test results (demonstrated control effectiveness)
- Training records with completion statistics (clear compliance demonstration)


Evidence That Needed Improvement:

- Some screenshots lacked context (had to re-explain what they showed)
- One policy was outdated (2022 version, should have been 2024)
- Log volume overwhelming (auditor asked for summary, not full export)


Process Improvements for Next Audit:

- Add README to all technical evidence explaining context
- Implement policy review calendar (ensure policies updated annually)
- Create log summary templates (provide stats + sample, not full logs)
- Pre-audit checklist: Verify all evidence current (<6 months old)

```

---

# Related Documents

**Policy Documents**:

- **ISMS-POL-A.5.31.4**: Change Management & Evidence Framework (evidence requirements policy)


**Implementation Guides**:

- **ISMS-IMP-A.5.31.3**: Requirements Extraction Process (creates requirements that need evidence)
- **ISMS-IMP-A.5.31.4**: Control Mapping Process (maps controls to requirements, informs evidence needs)
- **ISMS-IMP-A.5.31.6**: Compliance Dashboard & Regulatory Monitoring (evidence status tracking)


**Assessment Workbooks**:

- **Workbook 3**: Requirements Register (requirements context)
- **Workbook 4**: Control Mapping Matrix (control-to-requirement mappings)
- **Workbook 5**: Evidence Register (evidence inventory - this IMP guide's primary tool)
- **Workbook 6**: Compliance Dashboard (evidence status overview)


---

**Document Control**:

- **Last Updated**: 2025-01-11
- **Next Review**: [Date] (annual)
- **Change History**:
  - v1.0 (2025-01-11): Initial release


---

END OF DOCUMENT

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

# Detailed Process Steps

## Step 1: Evidence Identification

### Review Control Mappings

**Purpose**: Understand which controls need evidence based on regulatory requirements

**Actions**:
1. **Access Control Mapping Matrix** (Workbook 4)
2. **For each regulation**, identify all controls with Primary (P) mappings
3. **For each Primary-mapped control**, note:

   - Which requirement(s) the control satisfies
   - Control implementation status (implemented, planned, in progress)
   - Control Owner


**Output**: List of controls requiring evidence, organized by regulation

**Example**:
```
Regulation: GDPR

Controls Requiring Evidence:

- A.5.10 Acceptable Use of Information → REQ-GDPR-05 (Data minimization)
- A.8.24 Use of Cryptography → REQ-GDPR-32 (Encryption)
- A.5.26 Response to Information Security Incidents → REQ-GDPR-33 (Breach notification)
- A.5.34 Privacy and Protection of PII → REQ-GDPR-05, REQ-GDPR-25 (Data protection principles, privacy by design)
- CTRL-ORG-005 DPIA Process → REQ-GDPR-35 (DPIAs)

[... etc ...]
```

### Determine Evidence Types

**For each control**, identify what types of evidence would demonstrate implementation and effectiveness.

**Evidence Type Framework**:

**1. Policy Evidence** (Organizational controls)

- **What**: Approved policy documents, procedures, standards, guidelines
- **Demonstrates**: Governance, management intent, documented requirements
- **Example**: Information Security Policy v3.0 (approved by Executive, effective 2024-01-01)
- **Typical Controls**: A.5.1 Policies, A.5.10 Acceptable Use, A.5.15 Access Control Policy


**2. Procedure Evidence** (Operational controls)

- **What**: Documented procedures, work instructions, playbooks
- **Demonstrates**: How control is operationalized, step-by-step implementation
- **Example**: Incident Response Procedure v2.1 (breach notification workflow, escalation criteria)
- **Typical Controls**: A.5.26 Incident Response, A.5.24 Incident Planning, A.6.8 Disciplinary Process


**3. Configuration Evidence** (Technical controls)

- **What**: System configurations, settings exports, technical specifications
- **Demonstrates**: Technical implementation, control parameters
- **Example**: Firewall ruleset export (showing network segmentation), database encryption settings screenshot
- **Typical Controls**: A.8.24 Cryptography, A.8.20 Networks Security, A.8.22 Network Segregation


**4. Log Evidence** (Monitoring controls)

- **What**: Security logs, access logs, audit trails, event records
- **Demonstrates**: Control in operation, ongoing monitoring, historical activity
- **Example**: SIEM logs showing failed login attempts and account lockouts (access control enforcement)
- **Typical Controls**: A.8.15 Logging, A.8.16 Monitoring Activities, A.5.18 Access Rights


**5. Report Evidence** (Assessment controls)

- **What**: Assessment reports, audit reports, compliance reports, dashboards
- **Demonstrates**: Control effectiveness, compliance status, management oversight
- **Example**: Quarterly vulnerability scan report, annual penetration test report
- **Typical Controls**: A.8.8 Vulnerability Management, A.8.29 Security Testing


**6. Certificate/Attestation Evidence** (Certification controls)

- **What**: Third-party certifications, attestations, compliance certificates
- **Demonstrates**: External validation, industry standard compliance
- **Example**: ISO 27001 certification, SOC 2 Type II report, CSA STAR attestation
- **Typical Controls**: A.5.1 Policies (references certifications), supplier assessments (A.5.19-A.5.23)


**7. Training/Competence Evidence** (People controls)

- **What**: Training records, attendance sheets, competency assessments, certifications
- **Demonstrates**: Personnel awareness, skill development, regulatory training completion
- **Example**: Security awareness training completion records (95% staff completion), GDPR training certificates
- **Typical Controls**: A.6.3 Information Security Awareness, A.6.2 Terms and Conditions of Employment


**8. Test Result Evidence** (Validation controls)

- **What**: Test results, validation reports, effectiveness testing outcomes
- **Demonstrates**: Control works as intended, effectiveness validation
- **Example**: Backup restoration test results (successful recovery in <4 hours)
- **Typical Controls**: A.5.30 ICT Readiness for Business Continuity, A.5.29 Information Security During Disruption


**9. Contract/Agreement Evidence** (Third-party controls)

- **What**: Contracts, SLAs, NDAs, vendor agreements
- **Demonstrates**: Contractual obligations, third-party commitments
- **Example**: Cloud provider contract with data processing addendum (GDPR Article 28)
- **Typical Controls**: A.5.19-A.5.23 Supplier controls, A.5.31 Legal/Regulatory Requirements


**10. Photographic/Screenshot Evidence** (Physical and visual verification)

- **What**: Photos, screenshots, videos showing physical implementation or system state
- **Demonstrates**: Visual proof of implementation, physical security measures
- **Example**: Photo of server room access control (badge reader, camera), screenshot of dashboard
- **Typical Controls**: A.7.1-A.7.14 Physical controls, system configuration controls


**Evidence Selection Criteria**:

For each control, ask:
1. **What would convince an auditor** that this control is implemented and effective?
2. **What is SPECIFIC to this control** (not generic organizational documents)?
3. **What demonstrates CURRENT state** (not historical or planned)?
4. **What is VERIFIABLE** (auditor can independently check)?

**Decision Matrix**:

| Control Type | Primary Evidence Type(s) | Secondary Evidence Type(s) |
|--------------|--------------------------|---------------------------|
| **Policy/Governance** | Policy documents | Approval records, communication emails |
| **Procedural** | Procedure documents | Training records, execution logs |
| **Technical** | Configuration exports | Screenshots, architecture diagrams |
| **Monitoring** | Logs, SIEM reports | Dashboard screenshots, alert examples |
| **Testing** | Test reports | Test plans, remediation records |
| **Training** | Training records | Course materials, competency tests |
| **Physical** | Photos, access logs | Visitor logs, maintenance records |
| **Third-party** | Contracts, SLAs | Due diligence reports, audit rights letters |

**Example Evidence Identification**:
```
Control: A.8.24 Use of Cryptography
Mapped to: REQ-GDPR-32 (Encryption for personal data)

Evidence Needed:
1. Policy Evidence:

   - Cryptography Policy v2.0 (approved, in force)
   - Key Management Procedure v1.5
   

2. Configuration Evidence:

   - Database encryption settings (TDE enabled for all customer databases)
   - API TLS configuration (TLS 1.3 enforced, cipher suites documented)
   - Key management system configuration (HSM settings, key rotation policy)
   

3. Report Evidence:

   - Quarterly encryption compliance report (scan showing all databases encrypted)
   - Key rotation logs (keys rotated per policy schedule)
   

4. Test Evidence:

   - Encryption validation test results (attempted access to encrypted data without key → failed)


Primary Evidence: Configuration exports + Encryption compliance report
Secondary Evidence: Policy + Test results
```

---

## Step 2: Evidence Collection

### Assign Collection Responsibilities

**For each evidence item**, assign to appropriate role:

**Control Owner**: Responsible for overall evidence package for their control

- Coordinates collection
- Validates evidence quality
- Ensures evidence uploaded to repository


**Technical Roles** (System Admins, DevOps, Security Engineers):

- Extract technical configurations
- Generate log exports
- Create system screenshots
- Document technical specifications


**Operational Roles** (HR, Procurement, Legal, Business Units):

- Provide operational evidence (contracts, training records, policies)
- Execute manual processes to generate evidence (testing, reviews)


**Compliance Officer**:

- Coordinate evidence collection across all Control Owners
- Track progress (Evidence Register status updates)
- Identify missing evidence


**Example Assignment**:
```
Control: A.6.3 Information Security Awareness, Education and Training
Control Owner: CISO

Evidence Items:
1. Training Records (attendance, completion) → Assigned to: HR Training Coordinator
2. Training Materials (slides, videos) → Assigned to: Security Awareness Manager
3. Competency Assessment Results → Assigned to: HR Learning & Development
4. Training Plan/Schedule → Assigned to: CISO (Control Owner - develops plan)
5. Training Effectiveness Metrics → Assigned to: Compliance Officer (calculates from HR data)

Control Owner (CISO) coordinates, validates, and uploads all evidence.
```

### Collection Methods by Evidence Type

**Policy/Procedure Documents**:
1. Locate approved version (document management system)
2. Export as PDF (preserves formatting, prevents editing)
3. Include approval metadata (approver, approval date, version number)
4. **Quality Check**: Ensure document is current (not draft), approved, and in force

**Configuration Evidence**:
1. **For Cloud Systems**: Export configuration via API or admin console

   - AWS: Use AWS Config exports, CloudFormation templates
   - Azure: Use Azure Policy exports, ARM templates
   - Google Cloud: Use Cloud Asset Inventory exports

2. **For On-Premise Systems**: Export via CLI or GUI

   - Firewall: Export ruleset (`show running-config`)
   - Database: Export encryption settings (`SELECT * FROM sys.dm_database_encryption_keys`)
   - Active Directory: Export GPO settings (`Get-GPOReport`)

3. **Document Context**: Include README explaining what configuration shows and why it demonstrates compliance
4. **Quality Check**: Ensure export is complete, includes all relevant settings, timestamped

**Logs**:
1. **Identify Time Period**: What timeframe needed? (Last 30 days, last quarter, specific incident)
2. **Extract from SIEM/Log Management**: Export relevant log entries

   - Filter to relevant events (failed logins, access grants, security alerts)
   - Include sufficient context (timestamp, user, action, result)
   - Redact sensitive data if necessary (passwords, full credit card numbers)

3. **Aggregate if High-Volume**: If millions of log entries, provide summary/statistics + sample
4. **Quality Check**: Ensure logs are readable, timestamped, cover required period

**Reports** (Vulnerability Scans, Penetration Tests, Compliance Reports):
1. **Generate from Tool**: Run scan/assessment/report from security tool
2. **Include Metadata**: Tool name, version, scan date, coverage (what was scanned)
3. **Include Executive Summary**: High-level findings + detailed results
4. **Remediation Evidence** (if report shows issues): Include follow-up evidence showing issues resolved
5. **Quality Check**: Ensure report is complete (not truncated), includes all required sections

**Certificates/Attestations**:
1. **Obtain Copy**: Request from certifying body or download from portal
2. **Verify Authenticity**: Check certificate registry (for ISO 27001, check certifying body's registry)
3. **Include Scope Statement**: What is covered by certification (entire org, specific locations, specific processes)
4. **Quality Check**: Ensure certificate is current (not expired), scope matches claims

**Training Records**:
1. **Export from LMS/HRIS**: Learning Management System or HR Information System
2. **Include**: Employee name/ID, training course, completion date, score (if assessed)
3. **Aggregate Statistics**: Calculate completion rate (% employees completed)
4. **Privacy Consideration**: Redact personally identifiable info if evidence will be shared externally
5. **Quality Check**: Ensure records are current, cover all required personnel

**Test Results**:
1. **Execute Test**: Follow test procedure (backup restore test, failover test, penetration test)
2. **Document Methodology**: What was tested, how, by whom, when
3. **Document Results**: Pass/Fail, metrics (restore time, etc.), issues identified
4. **Document Remediation** (if test revealed issues): Evidence that issues fixed
5. **Quality Check**: Test results demonstrate control effectiveness (not just that test was performed)

**Contracts/Agreements**:
1. **Obtain Fully-Executed Version**: Signed by all parties, not draft
2. **Identify Relevant Clauses**: Highlight/annotate sections demonstrating compliance (data processing terms, security requirements)
3. **Redact if Necessary**: Commercial terms may be redacted if sensitive (keep compliance-relevant sections)
4. **Include Amendments**: If contract amended, include amendments
5. **Quality Check**: Contract is current (not expired), parties are correct

**Screenshots**:
1. **Capture Full Context**: Include URL/system name in screenshot, timestamp if possible
2. **Annotate if Needed**: Highlight/circle relevant settings in screenshot
3. **High Resolution**: Ensure text is readable
4. **Sequence if Multi-Step**: If demonstrating process, capture each step
5. **Quality Check**: Screenshot clearly shows what it claims to show

### Evidence Collection Checklist

For each evidence item:

- [ ] **Assigned**: Responsible party identified
- [ ] **Collected**: Evidence obtained from source system/process
- [ ] **Authenticated**: Verified this is genuine evidence (not placeholder, not fake)
- [ ] **Complete**: Evidence includes all necessary components (not truncated, not partial)
- [ ] **Current**: Evidence reflects current state (not outdated)
- [ ] **Relevant**: Evidence actually demonstrates the control it's meant to support
- [ ] **Formatted**: Evidence in appropriate format (PDF for documents, CSV/Excel for data, PNG/JPG for screenshots)
- [ ] **Named**: Evidence file named per naming convention (see 2.4.2)
- [ ] **Metadata**: Evidence includes context (what it is, when collected, by whom, why it demonstrates compliance)


---

## Step 3: Evidence Verification

**Before** evidence is stored in repository and registered, verify its quality.

### Authenticity Verification

**Question**: Is this evidence genuine and trustworthy?

**Checks**:
1. **Source Verification**: Evidence came from authoritative source (official system, not someone's laptop)
2. **Timestamp Verification**: Evidence timestamp aligns with collection date (not backdated)
3. **Signature Verification** (for documents): If document should be signed, verify signatures present
4. **System-Generated Verification**: For logs/reports, verify generated by legitimate system (not manually created Excel)

**Red Flags**:

- Evidence source unknown or unverifiable
- Timestamps don't make sense (future dates, suspiciously aligned)
- Document claims to be "approved" but no approval signature/metadata
- Manual document attempting to look like system report


**Example**:
```
Evidence: Vulnerability Scan Report

Authenticity Check:
✅ Generated by Qualys (official vulnerability scanner)
✅ Report header shows scan date: 2025-01-05
✅ Report metadata shows export date: 2025-01-06 (reasonable - exported day after scan)
✅ Digital signature from Qualys present (optional but preferred)

Verdict: AUTHENTIC
```

### Completeness Verification

**Question**: Does this evidence fully demonstrate what it's meant to demonstrate?

**Checks**:
1. **Scope Check**: Evidence covers full scope of control

   - If control applies to "all systems", evidence covers all systems (not just sample)
   - If control is "quarterly", evidence shows all 4 quarters

2. **Detail Check**: Evidence includes sufficient detail to be meaningful

   - Not just "encryption enabled" but which encryption algorithm, key length, scope
   - Not just "training completed" but when, by whom, pass/fail status

3. **Context Check**: Evidence includes enough context to be understood

   - Screenshots have captions explaining what they show
   - Logs include header explaining what log source, what filter applied


**Red Flags**:

- Evidence is partial (only some systems, only some users, only some time periods)
- Evidence is high-level summary without supporting detail
- Evidence lacks context (auditor wouldn't understand what it demonstrates)


**Example**:
```
Evidence: Encryption Configuration

Incomplete Version:

- Screenshot showing "Encryption: Enabled" checkbox ❌
- Problem: Doesn't show WHAT is encrypted, WHAT algorithm, WHAT key management


Complete Version:

- Database TDE configuration export showing:

  • Database names (all customer databases listed)
  • Encryption algorithm (AES-256)
  • Encryption status (Enabled for each database)
  • Key names and key vault location
  • Last key rotation date

- README file explaining: "This configuration export demonstrates all customer databases use AES-256 encryption (satisfying REQ-GDPR-32 encryption requirement)"


Verdict: COMPLETE ✅
```

### Timeliness Verification

**Question**: Is this evidence current and relevant?

**Checks**:
1. **Freshness Check**: Evidence date aligns with "current state"

   - For ongoing controls (access logs), evidence should be recent (last 30-90 days)
   - For annual controls (penetration test), evidence should be within last 12 months
   - For configuration (system settings), evidence should be current snapshot

2. **Validity Period Check**: If evidence has expiration date (certificates, attestations), verify not expired
3. **Refresh Frequency Check**: Evidence collected per expected refresh schedule

   - Monthly reports collected monthly
   - Quarterly scans conducted quarterly


**Red Flags**:

- Evidence is stale (2+ years old for ongoing control)
- Evidence is expired (certificate shows expiration date passed)
- Evidence collection frequency doesn't match control requirement (annual test only done once 3 years ago)


**Example**:
```
Evidence: ISO 27001 Certification

Timeliness Check:

- Certificate Issue Date: 2022-01-15
- Certificate Expiry Date: 2025-01-15
- Current Date: 2025-01-10
- Validity Period: 3 years
- Time Until Expiry: 5 days ⚠️


Verdict: CURRENT but EXPIRING SOON
Action: Schedule recertification audit, obtain renewed certificate by 2025-01-15
```

### Relevance Verification

**Question**: Does this evidence actually demonstrate the control/requirement it's meant to support?

**Checks**:
1. **Control Alignment Check**: Evidence aligns with control objective

   - If control is "access control", evidence shows access restrictions (not something else)
   - If requirement mandates "logging", evidence shows logs (not just logging policy)

2. **Requirement Alignment Check**: Evidence satisfies specific regulatory language

   - If GDPR requires "encryption", evidence shows encryption (not just "security measures")
   - If regulation requires "annual testing", evidence shows annual frequency (not one-time test)

3. **Sufficiency Check**: Evidence would satisfy auditor/regulator

   - Does evidence answer the question "How do you comply with Requirement X?"
   - Would auditor accept this as proof, or ask for more?


**Red Flags**:

- Evidence is tangentially related but doesn't directly demonstrate control
- Evidence shows PLAN to implement, not actual implementation
- Evidence is generic organizational document, not control-specific


**Example**:
```
Requirement: REQ-PCI-10.2 "Implement automated audit trails for all system components"

Submitted Evidence: Information Security Policy v3.0 (mentions logging requirement)

Relevance Check:
❌ Policy states logging SHALL be implemented (requirement/intent)
❌ Policy does NOT demonstrate logging IS implemented (actual state)
❌ Auditor would reject: "Policy is fine, but show me the actual logs"

Better Evidence:
✅ SIEM dashboard screenshot showing active log collection from all in-scope systems
✅ Sample audit trail export from critical system (showing user actions logged)
✅ Log retention report (showing logs retained per PCI requirement - 1 year online, 3 years total)

Verdict: ORIGINAL EVIDENCE NOT RELEVANT, BETTER EVIDENCE NEEDED
```

### Verification Approval

**Who Approves**:

- **Control Owner**: First-line verification (knows control best)
- **Compliance Officer**: Secondary verification (regulatory expertise)
- **Internal Audit** (optional): Independent verification for high-risk controls


**Verification Sign-Off**:
Document in Evidence Register:

- Verified By: [Name]
- Verification Date: [Date]
- Verification Status: Verified / Needs Improvement / Rejected


**If Evidence Rejected**:
1. Document reason for rejection (authenticity concern, incomplete, stale, not relevant)
2. Request corrected evidence from collector
3. Re-verify when corrected evidence provided

---

## Step 4: Evidence Organization

### Evidence Repository Structure

**Recommended Structure** (file system or SharePoint):

```
/Evidence_Repository/
├── By_Regulation/
│   ├── GDPR/
│   │   ├── REQ-GDPR-05_Data_Minimization/
│   │   │   ├── A.5.10_Acceptable_Use_Policy_v2.0.pdf
│   │   │   ├── A.5.34_Privacy_Policy_v1.5.pdf
│   │   │   └── README.md (explains what evidence demonstrates)
│   │   ├── REQ-GDPR-32_Encryption/
│   │   │   ├── A.8.24_Crypto_Policy_v2.0.pdf
│   │   │   ├── A.8.24_Database_TDE_Config_2025-01-05.json
│   │   │   ├── A.8.24_API_TLS_Config_Screenshot_2025-01-05.png
│   │   │   └── A.8.24_Encryption_Compliance_Report_Q4-2024.pdf
│   │   └── [...]
│   ├── PCI_DSS/
│   │   ├── REQ-PCI-10_Logging/
│   │   └── [...]
│   └── [Other Regulations]/
│
├── By_Control/
│   ├── A.5.10_Acceptable_Use/
│   │   ├── Policy_v2.0.pdf
│   │   ├── Training_Records_2024-Q4.xlsx
│   │   └── [...]
│   ├── A.8.24_Cryptography/
│   │   ├── [Evidence files as above]
│   │   └── [...]
│   └── [All 93 ISO Controls + Organizational Controls]/
│
├── By_Evidence_Type/
│   ├── Policies/
│   ├── Procedures/
│   ├── Configurations/
│   ├── Logs/
│   ├── Reports/
│   ├── Certificates/
│   ├── Training_Records/
│   └── Contracts/
│
└── Audit_Packages/
    ├── 2025-01_ISO27001_Recertification/
    │   ├── Controls_Evidence_Index.xlsx (mapping of evidence to controls)
    │   ├── [Evidence files or links]
    │   └── Auditor_Presentation_Deck.pptx
    ├── 2024-Q4_GDPR_Compliance_Review/
    └── [Future Audits]/
```

**Primary Organization: By_Regulation**

- Most useful for compliance demonstrations
- Organizes evidence by what it proves (regulatory requirement)
- Easy to answer "Show me your GDPR compliance evidence"


**Secondary Organization: By_Control and By_Evidence_Type**

- Symbolic links or duplicates (if file system allows)
- Alternative views for different use cases


### File Naming Conventions

**Format**: `[ControlID]_[EvidenceType]_[Description]_[Date].[Extension]`

**Components**:

- **ControlID**: ISO control (A.5.10) or organizational control (CTRL-ORG-005)
- **EvidenceType**: Policy, Procedure, Config, Log, Report, Certificate, Training, Contract, Screenshot
- **Description**: Brief descriptor (no spaces, use underscores)
- **Date**: ISO format YYYY-MM-DD (for time-sensitive evidence)
- **Extension**: Appropriate for file type (.pdf, .json, .csv, .png, .xlsx, .mp4)


**Examples**:
```
A.8.24_Config_Database_TDE_Settings_2025-01-05.json
A.8.24_Report_Encryption_Compliance_Q4-2024.pdf
A.6.3_Training_Security_Awareness_Records_2024-Q4.xlsx
A.5.26_Procedure_Incident_Response_v2.1.pdf
CTRL-ORG-005_Policy_DPIA_Process_v1.0.pdf
A.7.2_Screenshot_Server_Room_Access_Control_2025-01-10.png
```

**Benefits**:

- Alphabetical sort groups evidence by control
- Date suffix shows freshness
- Evidence type visible at glance
- Searchable and filterable


### Evidence Metadata

**For each evidence file**, maintain metadata (in Evidence Register or file properties):

**Required Metadata**:

- **Evidence ID**: Unique identifier (EV-2025-001, EV-2025-002, ...)
- **Control ID**: Which control this evidence supports
- **Requirement ID(s)**: Which regulatory requirement(s) this evidence satisfies
- **Evidence Type**: Policy, Config, Log, Report, etc.
- **Evidence Description**: Brief summary of what evidence shows
- **File Location**: Path in repository
- **Collection Date**: When evidence collected/generated
- **Valid Until**: Expiration date (if applicable - certificates, time-bound reports)
- **Collected By**: Who collected (name/role)
- **Verified By**: Who verified quality (name/date)
- **Refresh Frequency**: How often evidence should be refreshed (Annual, Quarterly, Monthly, One-time)
- **Next Refresh Date**: When evidence should be re-collected


**Optional Metadata**:

- **Audit History**: Which audits this evidence used in
- **Version**: If evidence updated multiple times (v1.0, v2.0)
- **Notes**: Additional context


**Example Metadata Entry**:
```
Evidence ID: EV-2025-042
Control ID: A.8.24
Requirement IDs: REQ-GDPR-32, REQ-PCI-4.1
Evidence Type: Configuration
Evidence Description: Database Transparent Data Encryption (TDE) configuration export showing AES-256 encryption enabled for all customer databases
File Location: /Evidence_Repository/By_Regulation/GDPR/REQ-GDPR-32_Encryption/A.8.24_Config_Database_TDE_Settings_2025-01-05.json
Collection Date: 2025-01-05
Valid Until: N/A (configuration, refresh periodically but no fixed expiration)
Collected By: Database Administrator (John Smith)
Verified By: CISO (Jane Doe) - 2025-01-06
Verification Status: Verified
Refresh Frequency: Quarterly
Next Refresh Date: 2025-04-05
Audit Ready: Yes
Notes: Configuration export includes all production databases. Dev/test databases excluded (not in scope for GDPR). Key rotation logs available separately (EV-2025-043).
```

### Evidence Register Population

**Actions**:
1. **Open Evidence Register** (Workbook 5)
2. **For each collected evidence item**, create entry with all metadata
3. **Link evidence to requirements and controls**: Populate Requirement ID and Control ID columns
4. **Update status**: Verification Status = Verified (after verification complete)
5. **Set refresh schedule**: Populate Refresh Frequency and Next Refresh Date

**Quality Check**:

- Every evidence item in repository has corresponding Evidence Register entry
- Every requirement has at least one evidence item (no requirements without evidence)
- All metadata fields populated (no blank Required fields)


---

## Step 5: Evidence Maintenance

Evidence is not "collect once and forget" - it requires ongoing maintenance.

### Periodic Refresh

**Why Refresh**:

- Evidence becomes stale (configurations change, policies update)
- Regulations require current evidence (not 2-year-old reports)
- Continuous compliance demonstration (not just "we were compliant 3 years ago")


**Refresh Triggers**:
1. **Scheduled Refresh**: Based on Refresh Frequency in Evidence Register

   - Annual evidence: Refresh every 12 months
   - Quarterly evidence: Refresh every 3 months
   - Monthly evidence: Refresh every month

2. **Control Change**: If control implementation changes, refresh evidence
3. **Regulatory Change**: If regulation updates, refresh evidence to reflect new requirements
4. **Approaching Expiration**: Certificate or attestation nearing expiry

**Refresh Process**:
1. **Identify evidence due for refresh** (Next Refresh Date approaching or passed)
2. **Re-collect evidence** using same method as initial collection
3. **Verify new evidence** (same quality checks as initial verification)
4. **Version control**:

   - **Option A (Versioning)**: Keep old evidence, add new version
     - Rename old: `A.8.24_Config_DB_TDE_2024-01-05_v1.json`
     - New file: `A.8.24_Config_DB_TDE_2025-01-05_v2.json`
   - **Option B (Replacement)**: Replace old evidence with new
     - Archive old evidence (move to `/Archive/`)
     - New evidence takes same filename

5. **Update Evidence Register**:

   - Collection Date → New date
   - Next Refresh Date → Calculate based on Refresh Frequency
   - Version → Increment if using versioning
   - Last Updated → Current date


**Automation Opportunities**:

- **Calendar Reminders**: Set reminders in Evidence Register for Next Refresh Date
- **Automated Collection**: For system-generated evidence (logs, configs), script collection
- **Dashboard Alerts**: Compliance Dashboard (Workbook 6) can flag evidence approaching refresh


### Expiration Monitoring

**For evidence with expiration dates** (certificates, attestations, time-bound reports):

**Actions**:
1. **Monitor Valid Until dates** in Evidence Register
2. **Alert on approaching expiration**:

   - 90 days before: Early warning
   - 30 days before: Urgent action required
   - 7 days before: Critical escalation

3. **Renew or replace**:

   - Certificates: Initiate renewal process (recertification audit, certificate reissuance)
   - Attestations: Request updated attestation from third party
   - Reports: Re-run assessment/scan


**Example**:
```
Evidence: ISO 27001 Certificate (EV-2025-001)
Valid Until: 2025-01-15
Current Date: 2024-10-10

Alert: 90 days until expiration
Action: Schedule recertification audit with certifying body (typically 3 months lead time)

---

Current Date: 2024-12-15
Alert: 30 days until expiration
Action: Confirm audit scheduled (Jan 5-7, 2025), prepare audit evidence package

---

Current Date: 2025-01-08
Alert: 7 days until expiration
Action: Audit complete (Jan 5-7), awaiting certification decision. If delayed, request interim letter from certifying body.

---

Current Date: 2025-01-14
Action: New certificate issued (EV-2025-100), Valid Until: 2028-01-14. Update Evidence Register.
```

### Change Management Integration

**When Controls Change**, evidence must be updated.

**Trigger**: Control implementation modified (new software, policy update, process change, scope expansion)

**Process**:
1. **Control Owner notifies Compliance Officer** of control change
2. **Assess Evidence Impact**:

   - Does existing evidence still accurately reflect control?
   - If yes → No action (but document that evidence was reviewed and remains valid)
   - If no → Evidence is now inaccurate, must refresh

3. **Collect Updated Evidence**: Re-collect to reflect new control state
4. **Update Evidence Register**: Mark old evidence as superseded, add new evidence

**Example**:
```
Control: A.8.24 Use of Cryptography
Change: Migrated from on-premise HSM to cloud-based KMS (AWS KMS)

Impact Assessment:

- Old Evidence (EV-2024-200): On-premise HSM configuration export
- Status: NO LONGER ACCURATE (HSM decommissioned)


Action:

- Collect New Evidence (EV-2025-110): AWS KMS configuration export, key policies, CloudTrail logs
- Update Evidence Register:
  - EV-2024-200: Status = Superseded, Superseded By = EV-2025-110
  - EV-2025-110: Status = Verified, Supersedes = EV-2024-200
- Archive old evidence (retain for historical record, not for current compliance demonstration)

```

### Evidence Retention

**Retention Requirements**:
1. **Regulatory Mandates**: Some regulations specify evidence retention periods

   - GDPR: 3 years (typical for demonstrating historical compliance)
   - PCI DSS: 1 year online, 3 years archived (for logs and audit trails)
   - SOX: 7 years (financial records and controls)

2. **Audit Trail**: Retain evidence for audit history (show compliance over time)
3. **Legal Hold**: If litigation/investigation, retain all evidence indefinitely until released

**Retention Policy**:

- **Current Evidence**: Retain indefinitely while control is in operation
- **Superseded Evidence**: Retain for:
  - Minimum: Regulatory retention requirement (e.g., 3 years)
  - Extended: Audit cycle + 1 year (to support historical audit inquiries)
- **Obsolete Evidence** (control decommissioned): Retain per regulatory/legal requirements


**Archive Process**:
1. When evidence superseded, move to `/Archive/[Year]/`
2. Maintain Evidence Register entry but mark Status = Archived
3. If retention period expires, delete (with approval from Legal Counsel and Compliance Officer)

---

## Step 6: Audit Preparation

### Evidence Gap Analysis

**Purpose**: Before audit, ensure all requirements have supporting evidence

**Process**:
1. **Generate Evidence Coverage Report**:

   - For each regulation being audited
   - List all requirements
   - For each requirement, list supporting evidence (from Evidence Register)
   - Flag requirements with NO evidence or INADEQUATE evidence


**Coverage Report Template**:
```
Regulation: GDPR
Audit Date: 2025-02-15

| Requirement ID | Requirement | Control(s) | Evidence Count | Evidence Status | Gap? |
|----------------|-------------|------------|----------------|-----------------|------|
| REQ-GDPR-05 | Data minimization | A.5.10, A.5.34 | 3 | ✅ Complete | No |
| REQ-GDPR-32 | Encryption | A.8.24 | 4 | ✅ Complete | No |
| REQ-GDPR-33 | Breach notification | A.5.26 | 2 | ⚠️ Partial | Yes - need test evidence |
| REQ-GDPR-35 | DPIA | CTRL-ORG-005 | 1 | ⚠️ Partial | Yes - only procedure, need completed DPIAs |

Gap Summary:

- Total Requirements: 42
- Requirements with Complete Evidence: 38 (90%)
- Requirements with Partial Evidence: 3 (7%)
- Requirements with No Evidence: 1 (3%)


Action Required:

- REQ-GDPR-33: Conduct breach notification drill, document test results
- REQ-GDPR-35: Locate 3 completed DPIAs (or conduct DPIAs if not done)
- REQ-GDPR-44: Implement international transfer safeguards (gap not yet remediated)

```

**Actions**:

- **For Complete Evidence**: No action, evidence ready
- **For Partial Evidence**: Collect missing evidence items before audit
- **For No Evidence**: 
  - If control implemented but evidence not collected → Urgent collection
  - If control NOT implemented → Escalate gap (cannot satisfy audit)


### Evidence Assembly

**Purpose**: Organize evidence for easy auditor access

**Audit Package Structure**:
```
/Audit_Packages/2025-02_GDPR_Compliance_Review/
├── 00_Index_and_Overview/
│   ├── Evidence_Index.xlsx (master list of all evidence with file locations)
│   ├── Control_Mapping_Matrix.xlsx (from Workbook 4)
│   ├── Executive_Summary.pdf (compliance status overview)
│   └── Audit_Scope_Statement.pdf (what's being audited, what's excluded)
│
├── 01_Policies_and_Procedures/
│   ├── Information_Security_Policy_v3.0.pdf
│   ├── Privacy_Policy_v1.5.pdf
│   ├── Incident_Response_Procedure_v2.1.pdf
│   └── [All policy/procedure evidence]
│
├── 02_Technical_Controls/
│   ├── A.8.24_Encryption/
│   │   ├── Database_TDE_Config_2025-01-05.json
│   │   ├── API_TLS_Config_Screenshot.png
│   │   ├── Encryption_Compliance_Report_Q4-2024.pdf
│   │   └── README.md (explains what each file demonstrates)
│   ├── A.8.15_Logging/
│   └── [Other technical controls]
│
├── 03_Organizational_Controls/
│   ├── A.6.3_Training/
│   ├── A.5.19_Vendor_Management/
│   └── [Other organizational controls]
│
├── 04_Assessment_Reports/
│   ├── Vulnerability_Scan_Q4-2024.pdf
│   ├── Penetration_Test_Annual_2024.pdf
│   └── Internal_Audit_Report_2024.pdf
│
├── 05_Certifications_and_Attestations/
│   ├── ISO_27001_Certificate_2022-2025.pdf
│   ├── SOC2_Type_II_Report_2024.pdf
│   └── Cloud_Provider_Certifications/
│
└── 06_Supplementary_Evidence/
    ├── Sample_Logs/ (if full logs too large, provide representative samples)
    ├── Additional_Context/ (supporting documents, explanations)
    └── Remediation_Evidence/ (for any gaps found during audit)
```

**Evidence Index**:

- Excel workbook listing ALL evidence in audit package
- Columns: Evidence ID, Requirement ID, Control ID, File Name, Location, Description
- Sortable and filterable for auditor convenience
- Hyperlinks to evidence files (if electronic audit)


### Pre-Audit Review

**Purpose**: Validate evidence quality before auditor sees it

**Internal Review Process**:
1. **Self-Review** (Control Owner): Review own control's evidence

   - Is evidence current?
   - Does evidence clearly demonstrate control?
   - Any gaps or weaknesses auditor will identify?

2. **Peer Review** (Compliance Officer): Review evidence for regulatory alignment

   - Does evidence satisfy regulatory requirement?
   - Is evidence format professional?
   - Any concerns about evidence authenticity or quality?

3. **Mock Audit** (Internal Audit): Simulate auditor review

   - Pretend to be external auditor
   - Ask questions auditor would ask
   - Identify weaknesses or gaps before real audit


**Mock Audit Sample Questions**:
```
Requirement: REQ-GDPR-32 (Encryption for personal data)

Mock Auditor Questions:
Q1: "Show me your encryption policy."
→ Check: Do we have approved encryption policy? Is it current?

Q2: "What encryption algorithm do you use?"
→ Check: Can we answer definitively? (AES-256, not just "strong encryption")

Q3: "Show me evidence that all personal data is encrypted."
→ Check: Do we have comprehensive evidence? (Not just sample, but all databases)

Q4: "How do you manage encryption keys?"
→ Check: Do we have key management evidence? (HSM/KMS configuration, key rotation logs)

Q5: "What happens if encryption key is compromised?"
→ Check: Do we have incident response plan for crypto incidents?

Q6: "Show me test results proving encryption works."
→ Check: Do we have encryption validation test evidence?

Mock Audit Findings:

- ✅ Q1-Q4: Evidence exists and is strong
- ⚠️ Q5: Incident response plan exists but doesn't specifically address crypto key compromise scenario
- ❌ Q6: No encryption validation test on record


Action Before Real Audit:

- Enhance incident response plan to include crypto key compromise scenario
- Conduct encryption validation test, document results (EV-2025-115)

```

**Pre-Audit Checklist**:

- [ ] All requirements have supporting evidence (no zero-evidence requirements)
- [ ] All evidence is current (no stale evidence >1 year old for ongoing controls)
- [ ] All evidence is verified (Verification Status = Verified in Evidence Register)
- [ ] Evidence is organized and indexed (Audit Package assembled)
- [ ] Evidence quality reviewed (internal review complete)
- [ ] Evidence locations documented (Evidence Index current)
- [ ] Gaps identified and remediated (or risk-accepted with management approval)


---

## Step 7: Evidence Presentation

### Auditor Evidence Request

**When Auditor Asks**: "Show me evidence for Requirement X" or "How do you satisfy Control Y?"

**Response Process**:
1. **Acknowledge Request**: "Let me pull the evidence for [Requirement/Control]"
2. **Consult Evidence Index**: Locate relevant evidence in audit package
3. **Provide Evidence**: Share file(s) with auditor (electronic or printed)
4. **Explain Context**: Brief explanation of what evidence shows
5. **Answer Questions**: Address auditor follow-up questions

**Example Response**:
```
Auditor: "Show me evidence that you encrypt personal data at rest."

Response:
"We satisfy the encryption requirement through Control A.8.24 - Use of Cryptography. Let me share the evidence package..."

[Open audit package: 02_Technical_Controls/A.8.24_Encryption/]

"Here are four evidence items:

1. Encryption Policy (A.8.24_Policy_Cryptography_v2.0.pdf):

   - Approved by CISO on 2024-01-01
   - Mandates AES-256 encryption for all personal data at rest
   - Specifies key management requirements


2. Database TDE Configuration (A.8.24_Config_Database_TDE_2025-01-05.json):

   - Configuration export from all production databases
   - Shows Transparent Data Encryption (TDE) enabled
   - AES-256 algorithm, keys managed in AWS KMS


3. Encryption Compliance Report (A.8.24_Report_Encryption_Compliance_Q4-2024.pdf):

   - Quarterly scan of all databases
   - Shows 100% of customer databases encrypted
   - Any exceptions flagged (none found in Q4 2024)


4. Encryption Validation Test (A.8.24_Test_Encryption_Validation_2024-12-15.pdf):

   - Test conducted December 2024
   - Attempted to read encrypted database without key → Failed (encryption confirmed working)
   - Test conducted by Security Engineer, reviewed by CISO


Does this satisfy your evidence request, or do you need additional information?"

Auditor: "This looks good. Can you show me key rotation logs?"

Response:
"Yes, key rotation is documented in our KMS logs. Let me pull that..."
[Retrieve supplementary evidence: A.8.24_Log_KMS_Key_Rotation_2024.csv]
```

### Handling Evidence Gaps During Audit

**If Auditor Identifies Gap**: "I need evidence for X, but I don't see it in your package."

**Response Options**:

**Option 1: Evidence Exists but Not Included**

- "We have that evidence - it's in our repository but wasn't included in the audit package. Let me retrieve it."
- Action: Locate evidence in repository, add to audit package, provide to auditor
- Lesson Learned: Improve evidence packaging process to avoid missing evidence


**Option 2: Evidence Exists but Not What Auditor Wants**

- "We have [Evidence A], but it sounds like you're looking for something different. Can you clarify what would satisfy this requirement?"
- Action: Understand auditor's expectation, provide alternative evidence or explain why current evidence is sufficient
- Negotiation: Sometimes auditor has different interpretation of requirement than organization - discuss and align


**Option 3: Evidence Doesn't Exist - Control Implemented but Not Documented**

- "The control is implemented, but we haven't collected this specific evidence. Can we provide it post-audit?"
- Action: Rapid evidence collection during audit (if possible), or commit to providing within X days post-audit
- Impact: May result in audit finding ("Control implemented but evidence inadequate") with remediation requirement


**Option 4: Evidence Doesn't Exist - Control Not Implemented (Gap)**

- "We acknowledge this is a gap. The control is not yet implemented."
- Action: Transparently acknowledge gap, explain remediation plan (if exists)
- Impact: Audit finding (non-conformance), must remediate before certification/attestation


**Example**:
```
Auditor: "I need evidence that you conduct Data Protection Impact Assessments (DPIAs) for high-risk processing. I see your DPIA procedure, but where are the completed DPIAs?"

Response (Option 3):
"You're correct - we have the DPIA procedure but haven't included completed DPIAs in the audit package. We have 3 DPIAs completed to date:

- DPIA #1: Customer Analytics Platform (completed Oct 2024)
- DPIA #2: Automated Decision System (completed Nov 2024)
- DPIA #3: Biometric Authentication Pilot (completed Dec 2024)


I can retrieve these from our repository and provide them this afternoon. Would that satisfy your requirement?"

Auditor: "Yes, please provide them. Also, how do you ensure DPIAs are conducted for all high-risk processing?"

Response:
"Our DPIA procedure integrates DPIAs into our product development lifecycle. Any new product or major feature must pass a DPIA threshold assessment. If threshold met (high risk), DPIA is mandatory before launch. We track DPIAs in our Privacy Compliance Register [show register]. This ensures no high-risk processing goes live without DPIA."

[Later that day: Provide 3 completed DPIAs to auditor]

Outcome: Evidence gap closed during audit, no finding.
```

### Evidence Presentation Best Practices

**Do**:

- ✅ Be organized (know where evidence is, provide quickly)
- ✅ Be transparent (if gap exists, acknowledge it)
- ✅ Provide context (explain what evidence shows, don't assume auditor will understand)
- ✅ Be concise (provide exactly what auditor asks for, not 50 pages of tangentially related documents)
- ✅ Anticipate questions (if evidence might raise questions, proactively address)


**Don't**:

- ❌ Provide unverified evidence (don't share evidence you haven't quality-checked)
- ❌ Overwhelm auditor (don't dump 1000 pages of logs when auditor asks for "logging evidence")
- ❌ Argue with auditor (if auditor says evidence is insufficient, listen and understand their concerns)
- ❌ Fabricate evidence (NEVER create fake evidence - this is fraud and grounds for certification revocation)
- ❌ Promise evidence you can't deliver ("We'll have that for you next week" when you know you won't)


---

# Evidence Types: Detailed Guidance

## Policy Evidence

**What**: Approved policy documents

**Quality Criteria**:

- [ ] Approved by appropriate authority (Executive, Board)
- [ ] Approval date and version number visible
- [ ] Policy is current (not draft, not expired)
- [ ] Policy scope matches control scope
- [ ] Policy content addresses requirement


**Collection Method**:
1. Retrieve from document management system (DMS)
2. Export as PDF (preserves approval metadata)
3. Verify approval signature/date

**Common Issues**:

- **Issue**: Policy is draft (not approved)
  - **Fix**: Obtain approved version or expedite approval process
- **Issue**: Policy is outdated (e.g., references old organizational structure)
  - **Fix**: Update policy, obtain re-approval


**Example**:
```
Control: A.5.1 Policies for Information Security
Evidence: Information Security Policy v3.0

Quality Check:
✅ Title page shows: "Version 3.0, Approved by CEO, Effective Date 2024-01-01"
✅ Content addresses information security governance, roles, compliance
✅ Policy scope: "All employees, contractors, and third parties with access to [Organization] systems"
✅ Current (approved Jan 2024, still in force)

Verdict: QUALITY EVIDENCE
```

## Configuration Evidence

**What**: System configuration exports, settings screenshots

**Quality Criteria**:

- [ ] Export/screenshot is recent (current state)
- [ ] Export includes all relevant settings (not partial)
- [ ] Context provided (what system, what settings shown, why relevant)
- [ ] Export is readable and parseable


**Collection Method**:

- **Cloud**: API export, admin console export
- **On-premise**: CLI export (`show config`), GUI screenshot
- **Database**: SQL query results showing settings


**Common Issues**:

- **Issue**: Screenshot doesn't show enough context (cropped too tightly)
  - **Fix**: Re-screenshot with URL/breadcrumbs visible
- **Issue**: Configuration export is massive (500 pages)
  - **Fix**: Extract relevant section, provide summary + full export as appendix


**Example**:
```
Control: A.8.20 Networks Security
Evidence: Firewall Ruleset Export

Quality Check:
✅ Export date: 2025-01-10 (current)
✅ Firewall: Palo Alto PA-5220 (production firewall)
✅ Ruleset includes: Source/Dest zones, allowed protocols, deny rules
✅ README included: "This ruleset shows network segmentation between Production, DMZ, and Management networks per A.8.20 requirement. Default deny rule at end (Rule 999)."

Verdict: QUALITY EVIDENCE
```

## Log Evidence

**What**: Security logs, access logs, audit trails

**Quality Criteria**:

- [ ] Logs cover required time period
- [ ] Logs include relevant events (not just all logs)
- [ ] Logs are authentic (from real system, not manually created)
- [ ] Logs are readable (formatted, not raw binary)
- [ ] Volume is appropriate (summary if millions of entries)


**Collection Method**:
1. Define time period and event types needed
2. Export from SIEM, log management system, or application
3. Filter to relevant events (reduce noise)
4. If large volume, provide summary + sample

**Common Issues**:

- **Issue**: Logs are too verbose (millions of entries, unreadable)
  - **Fix**: Provide summary statistics + representative sample (100-1000 entries)
- **Issue**: Logs don't include enough detail (just timestamps, no user/action)
  - **Fix**: Reconfigure logging to capture required fields, re-export


**Example**:
```
Control: A.8.15 Logging
Evidence: Failed Login Attempts Log

Quality Check:
✅ Time Period: Last 90 days (Oct 1 - Dec 31, 2024)
✅ Event Type: Failed login attempts (brute force detection)
✅ Fields: Timestamp, Username, Source IP, Failure Reason
✅ Volume: 1,247 failed attempts (manageable size)
✅ Summary: "Average 14 failed attempts/day. Top 3 usernames: admin (327), root (198), test (145). All IPs blocked after 5 attempts (per policy)."

Verdict: QUALITY EVIDENCE
```

## Report Evidence

**What**: Assessment reports, scan reports, compliance reports

**Quality Criteria**:

- [ ] Report is recent (within validity period)
- [ ] Report scope matches control scope
- [ ] Report includes executive summary + detailed findings
- [ ] Report includes remediation (if findings exist)
- [ ] Report is from reputable source/tool


**Collection Method**:
1. Generate report from tool (vulnerability scanner, compliance tool)
2. Export as PDF
3. If findings exist, include remediation evidence

**Common Issues**:

- **Issue**: Report shows vulnerabilities but no remediation
  - **Fix**: Include follow-up evidence showing vulnerabilities patched
- **Issue**: Report scope incomplete (didn't scan all systems)
  - **Fix**: Re-run scan with comprehensive scope


**Example**:
```
Control: A.8.8 Management of Technical Vulnerabilities
Evidence: Quarterly Vulnerability Scan Report Q4 2024

Quality Check:
✅ Scan Date: December 15, 2024
✅ Scan Scope: All production servers (42 systems)
✅ Tool: Qualys Vulnerability Management
✅ Findings: 3 Critical, 15 High, 47 Medium, 128 Low
✅ Remediation: Critical and High findings include patch plan + completion dates
✅ Follow-up: Re-scan on Jan 5, 2025 shows all Critical/High patched

Verdict: QUALITY EVIDENCE (includes remediation proof)
```

## Training Evidence

**What**: Training records, attendance, competency assessments

**Quality Criteria**:

- [ ] Records are current (recent training cycle)
- [ ] Records include: Employee name/ID, training course, completion date, pass/fail
- [ ] Completion rate calculated (% of required personnel completed)
- [ ] Training content is relevant to control


**Collection Method**:
1. Export from Learning Management System (LMS) or HRIS
2. Calculate completion statistics
3. Redact personal info if needed (for external sharing)

**Common Issues**:

- **Issue**: Low completion rate (<80%)
  - **Fix**: Follow up with non-completers, re-run report after follow-ups
- **Issue**: Training content outdated (2019 training for 2024 requirement)
  - **Fix**: Update training content, re-train personnel


**Example**:
```
Control: A.6.3 Information Security Awareness, Education and Training
Evidence: Security Awareness Training Records Q4 2024

Quality Check:
✅ Training Course: "Annual Information Security Awareness (2024 Edition)"
✅ Required Personnel: All employees and contractors (n=487)
✅ Completion: 472 completed (97%)
✅ Completion Period: Oct 1 - Dec 31, 2024
✅ Assessment: All completers passed quiz (80% passing score)
✅ Follow-up: 15 non-completers followed up, 12 completed by Jan 10, final completion 99%

Verdict: QUALITY EVIDENCE
```

---

# Special Scenarios

## Evidence for Third-Party Controls

**Challenge**: Control is implemented by third party (cloud provider, vendor), not directly by [Organization]

**Evidence Strategy**:
1. **Third-Party Attestation**: Obtain SOC 2, ISO 27001, or other certification from vendor
2. **Contract Clauses**: Evidence that contract requires vendor to implement control
3. **Audit Rights**: Evidence of audit rights in contract + results of vendor audits
4. **Vendor Self-Assessment**: Questionnaire responses from vendor

**Example**:
```
Control: A.8.9 Configuration Management (for cloud infrastructure)
Implementation: AWS manages infrastructure configuration

Evidence:
1. AWS SOC 2 Type II Report (covers configuration management controls)
2. [Organization]-AWS Contract, Section 8.3: "AWS shall maintain configuration management per SOC 2"
3. AWS Compliance Dashboard Screenshot (showing SOC 2 certification current)
4. AWS Artifact: ISO 27001 Certificate for AWS (covers A.8.9 equivalent controls)

Note: We inherit control from AWS. Our evidence demonstrates AWS implements control and we verified through attestations.
```

## Evidence for Compensating Controls

**Challenge**: Ideal control not implemented, compensating control used instead

**Evidence Strategy**:
1. **Document Rationale**: Why ideal control not feasible
2. **Document Compensating Control**: What compensating control does
3. **Demonstrate Effectiveness**: Evidence that compensating control achieves same objective
4. **Management Approval**: Evidence that compensating approach approved

**Example**:
```
Requirement: REQ-PCI-8.3 "Implement multi-factor authentication (MFA) for all remote access"
Ideal Control: Biometric MFA (fingerprint or facial recognition)
Issue: Biometric MFA cost-prohibitive (€500K for hardware tokens + biometric scanners)

Compensating Control: Hardware security keys (YubiKey) + behavioral analytics

- Hardware security keys (FIDO2 compliant): "Something you have"
- Behavioral analytics (Okta Adaptive MFA): Detects anomalous behavior (location, device, time)
- Combined: Provides equivalent security to biometric MFA


Evidence:
1. Cost-Benefit Analysis: Document showing biometric MFA cost (€500K) vs. YubiKey + Behavioral (€80K)
2. Executive Approval: CFO and CISO approval of compensating control approach
3. Technical Evidence:

   - YubiKey deployment records (all remote users issued hardware key)
   - Okta Adaptive MFA configuration (behavioral analytics enabled)
   - Test results: Simulated attack with stolen password → Blocked by behavioral analytics

4. Effectiveness Assessment: Independent review by penetration tester confirming compensating controls provide equivalent protection
```

## Evidence for Gaps

**Challenge**: Gap exists (control not implemented), but remediation in progress

**Evidence Strategy**:
1. **Acknowledge Gap**: Transparent documentation of gap
2. **Remediation Plan**: Evidence of plan to close gap
3. **Remediation Progress**: Evidence of progress (milestones achieved)
4. **Risk Acceptance** (if gap not yet closed): Management approval to operate with gap temporarily

**Example**:
```
Requirement: REQ-GDPR-35 "Conduct DPIAs for high-risk processing"
Current State: DPIA process defined (procedure exists) but not yet executed (no completed DPIAs)

Evidence (Interim):
1. Gap Acknowledgment: Gap Register entry GAP-2025-001 (DPIA process not operational)
2. Remediation Plan: Detailed plan to implement DPIA process (Feb-Mar 2025)
3. Progress Evidence:

   - DPIA Procedure v1.0 (approved Jan 2025)
   - DPIA Template (created, legal-reviewed)
   - Training scheduled (Privacy Team training on Feb 5, 2025)
   - 3 DPIAs planned: Customer Analytics, Automated Decisions, Biometric Auth

4. Risk Acceptance: Executive Management approval to proceed with product launches while DPIA process ramping up (time-limited to Q1 2025)

Timeline:

- Feb 5: Privacy Team trained
- Feb 15-28: Conduct 3 backlog DPIAs
- Mar 1: DPIA process operational, gap closed


Interim Compliance Status: PARTIAL (process defined but not yet fully operational)
```

---

# Tools & Automation

## Evidence Register (Workbook 5)

**Purpose**: Master inventory of all evidence

**Usage**:

- Central repository of evidence metadata
- Track evidence status (verified, pending, expired)
- Monitor refresh schedules
- Generate evidence coverage reports


**Key Features**:

- Evidence ID (unique identifier)
- Links to requirements and controls
- Valid Until dates (expiration tracking)
- Next Refresh Date (maintenance scheduling)
- Audit Ready status


## Evidence Repository

**Options**:
1. **File System**: Simple folder structure on network drive

   - Pros: Easy to set up, no cost
   - Cons: Limited search, no version control, no audit trail

2. **SharePoint/OneDrive**: Cloud-based document management

   - Pros: Version control, access control, collaboration, search
   - Cons: Requires Microsoft 365 license

3. **Document Management System** (M-Files, Laserfiche, OpenText): Enterprise DMS

   - Pros: Advanced features (workflow, retention, metadata), audit trail
   - Cons: Cost, complexity

4. **Compliance Platform** (OneTrust, LogicGate, ServiceNow GRC): Integrated GRC tool

   - Pros: Integrated with control management, automated workflows
   - Cons: Significant cost


**Recommendation**: Start with SharePoint (if available), migrate to GRC platform as compliance program matures

## Automation Opportunities

**Automated Evidence Collection**:

- **Logs**: Script to export security logs monthly (cron job)
- **Configurations**: Script to export cloud configs weekly (AWS Config, Azure Policy)
- **Reports**: Schedule vulnerability scans quarterly, auto-export reports


**Automated Evidence Verification**:

- **Hash Verification**: Calculate file hash on collection, recalculate on retrieval (detect tampering)
- **Timestamp Validation**: Check file creation date matches collection date
- **Format Validation**: Verify file is expected format (PDF, JSON, CSV)


**Automated Evidence Maintenance**:

- **Expiration Alerts**: Email when evidence approaching Valid Until date
- **Refresh Reminders**: Calendar reminders when Next Refresh Date approaches
- **Dashboard**: Compliance Dashboard (Workbook 6) shows evidence status at glance


---

# Roles & Responsibilities Summary

| Role | Responsibilities in Evidence Management |
|------|----------------------------------------|
| **Control Owners** | - Collect evidence for their controls<br>- Verify evidence quality<br>- Upload to repository<br>- Maintain evidence currency |
| **Compliance Officer** | - Coordinate evidence collection<br>- Maintain Evidence Register<br>- Monitor refresh schedules<br>- Validate evidence completeness<br>- Prepare audit packages |
| **ISMS Manager** | - Oversee evidence framework<br>- Ensure audit readiness<br>- Approve evidence management procedures |
| **System Administrators** | - Extract technical evidence (logs, configs)<br>- Automate evidence collection where possible |
| **Internal Audit** | - Validate evidence quality<br>- Conduct pre-audit reviews<br>- Independent verification |
| **Legal Counsel** | - Advise on evidence retention requirements<br>- Approve evidence destruction (when retention period expires) |

---

# Continuous Improvement

## Evidence Management Metrics

**Collection Metrics**:

- Time to collect evidence (target: <2 hours per evidence item)
- Evidence collection completion rate (% evidence collected on schedule)


**Quality Metrics**:

- Evidence verification pass rate (% evidence passing quality checks on first attempt)
- Evidence rejection rate (% evidence rejected during verification)


**Maintenance Metrics**:

- Evidence refresh compliance (% evidence refreshed per schedule)
- Evidence expiration rate (% evidence expired without renewal)


**Audit Readiness Metrics**:

- Evidence coverage (% requirements with supporting evidence)
- Audit-ready percentage (% evidence marked "Audit Ready: Yes")
- Evidence gaps (count of requirements without evidence)


## Lessons Learned

**After Each Audit**:
1. **Evidence Effectiveness**: Which evidence satisfied auditors easily? Which required extensive discussion?
2. **Evidence Gaps**: What evidence was missing that auditor requested?
3. **Process Improvements**: How can evidence collection be streamlined?

**Example**:
```
Post-Audit Lessons Learned: ISO 27001 Recertification (Jan 2025)

Evidence That Worked Well:

- Configuration exports (auditor appreciated technical detail)
- Completed test results (demonstrated control effectiveness)
- Training records with completion statistics (clear compliance demonstration)


Evidence That Needed Improvement:

- Some screenshots lacked context (had to re-explain what they showed)
- One policy was outdated (2022 version, should have been 2024)
- Log volume overwhelming (auditor asked for summary, not full export)


Process Improvements for Next Audit:

- Add README to all technical evidence explaining context
- Implement policy review calendar (ensure policies updated annually)
- Create log summary templates (provide stats + sample, not full logs)
- Pre-audit checklist: Verify all evidence current (<6 months old)

```

---

# Related Documents

**Policy Documents**:

- **ISMS-POL-A.5.31-S4**: Change Management & Evidence Framework (evidence requirements policy)


**Implementation Guides**:

- **ISMS-IMP-A.5.31-S3**: Requirements Extraction Process (creates requirements that need evidence)
- **ISMS-IMP-A.5.31-S4**: Control Mapping Process (maps controls to requirements, informs evidence needs)
- **ISMS-IMP-A.5.31-S6**: Compliance Dashboard & Regulatory Monitoring (evidence status tracking)


**Assessment Workbooks**:

- **Workbook 3**: Requirements Register (requirements context)
- **Workbook 4**: Control Mapping Matrix (control-to-requirement mappings)
- **Workbook 5**: Evidence Register (evidence inventory - this IMP guide's primary tool)
- **Workbook 6**: Compliance Dashboard (evidence status overview)


---

**Document Control**:

- **Last Updated**: 2025-01-11
- **Next Review**: [Date] (annual)
- **Change History**:
  - v1.0 (2025-01-11): Initial release


---

**END OF SPECIFICATION**

---

*"Every word or concept, clear as it may seem to be, has only a limited range of applicability."*
— Werner Heisenberg


*Where bamboo antennas actually work.* 🎋
