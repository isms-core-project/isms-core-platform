**ISMS-IMP-A.8.30.2-UG - Contract Compliance**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.30: Outsourced Development

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.2-UG |
| **Document Title** | Contract Compliance Workbook Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.30: Outsourced Development |
| **Parent Policy** | ISMS-POL-A.8.30 (Outsourced Development) |
| **Version** | 1.0 |
| **Classification** | Internal |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial implementation specification for ISO 27001:2022 first certification |

---

This section provides step-by-step guidance for completing the Contract Compliance workbook. Follow this guide to ensure comprehensive contract security management that satisfies ISO 27001:2022 audit requirements.

---

## Assessment Overview

### Purpose

The Contract Compliance workbook tracks security clause inclusion in outsourced development contracts, monitors ongoing compliance with contractual obligations, and manages subcontractor approvals. It provides the contractual foundation that converts security requirements into legally binding vendor commitments.

ISO/IEC 27001:2022 Control A.8.30 states:

> *"The organisation should direct, monitor and review the activities related to outsourced system development."*

Contracts are the primary mechanism for directing vendor security behaviour and establishing the legal framework for monitoring and review activities.

### Scope and Applicability

**This workbook applies to:**

| Contract Type | Applicability | Security Review Level |
|---------------|---------------|----------------------|
| Custom software development agreements | Mandatory | Full security clause review |
| System integration contracts | Mandatory | Full security clause review |
| Staff augmentation agreements | Required | Modified clause set |
| Managed service contracts with development | Required | Full security clause review |
| Maintenance and support contracts | Required | Subset of clauses |
| Professional services with code delivery | Required | Full security clause review |
| Freelance/contractor agreements | Required | Modified clause set |
| Open source commercial support | Conditional | Risk-based review |

**This workbook does NOT apply to:**

- Standard SaaS subscription agreements (use Supplier Management A.5.21-22)
- Hardware purchase agreements without development
- Consulting agreements without code delivery
- Internal development projects

### Business Context

**Why Contract Compliance Matters:**

Contracts establish the legal foundation for security requirements:

1. **Legal Enforceability**: Security policies without contractual backing cannot be enforced
2. **Liability Allocation**: Contracts define who bears responsibility for security failures
3. **SLA Binding**: Vulnerability remediation timeframes become binding obligations
4. **Audit Rights**: Contracts enable verification of vendor security practices
5. **Incident Response**: Notification obligations ensure timely incident awareness
6. **Termination Protection**: Security-related termination rights protect the organisation

**Regulatory Context:**

| Regulation | Contractual Requirements |
|------------|-------------------------|
| ISO 27001:2022 A.8.30 | Security requirements in contracts |
| Swiss FADP/nDSG Art. 10a | Data processing agreements, sub-processor controls |
| GDPR Article 28 | Processor contract requirements |
| FINMA | Third-party contract provisions |
| PCI DSS | Service provider contracts |

### Assessment Outputs

Upon completion, this workbook provides:

| Output | Purpose | Audience |
|--------|---------|----------|
| Contract Inventory | Complete list of development contracts | Procurement, Legal, IT Security |
| Clause Compliance Report | Security clause inclusion status | CISO, Legal |
| SLA Tracking Dashboard | Vulnerability remediation compliance | IT Security, Management |
| Subcontractor Register | Approved subcontractors | IT Security, Procurement |
| Termination Records | Contract closure verification | Legal, IT Security |
| Audit Evidence Package | ISO 27001 compliance documentation | External Auditors |

---

## Prerequisites

### Required Inputs

Before beginning contract compliance tracking, ensure you have:

| Input | Source | Required For |
|-------|--------|--------------|
| Executed contract copy | Legal/Procurement | Sheet 1, Sheet 2 |
| Vendor assessment record | ISMS-IMP-A.8.30.1 | Vendor_ID reference |
| Project classification | Project Manager | Risk-based clause requirements |
| Security schedule/annex | Legal | Clause verification |
| Subcontractor disclosure | Vendor | Sheet 4 |
| Security questionnaire | Vendor | Clause compliance verification |
| Statement of Work (SOW) | Project Manager | Scope verification |

### Required Approvals Before Contract Execution

| Approval Type | Approver | Purpose |
|---------------|----------|---------|
| Vendor Assessment Complete | IT Security | Confirms vendor security suitability |
| Security Clause Review | IT Security/Legal | Confirms security clauses included |
| Data Protection Review | DPO (if applicable) | GDPR/FADP compliance |
| Legal Review | Legal Department | Contract terms acceptability |
| Commercial Approval | Procurement/Finance | Budget and terms |
| Final Execution | Authorised Signatory | Contract binding |

### Required Knowledge

Personnel completing this workbook should understand:

- Contract law fundamentals (or work with Legal)
- ISO 27001:2022 control requirements
- Organisation's security policy requirements
- Regulatory requirements (GDPR, FADP) for contracts
- Vulnerability classification and SLA structures
- Subcontractor risk implications

### Tool Requirements

| Tool | Purpose | Access Required |
|------|---------|-----------------|
| Excel or equivalent | Workbook completion | Standard user |
| Contract management system | Contract retrieval | Read access |
| Document management | Evidence storage | Write access |
| Vulnerability tracker | SLA monitoring | Read access |
| Calendar/tickler system | Expiry alerts | Standard access |

---

## Completion Walkthrough

### Sheet 1: Contract Inventory – Completion Guide

**Purpose**: Maintain the authoritative list of outsourced development contracts with key dates and status.

**Step-by-Step Completion:**

**Step 1: Generate Contract ID**

Create a unique identifier using the format `CTR-XXXX`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | CTR- | CTR- |
| Sequential Number | 4 digits | 0089 |
| Full ID | CTR-XXXX | CTR-0089 |

**Step 2: Link to Vendor**

Enter the Vendor_ID from ISMS-IMP-A.8.30.1 Vendor Registry. The vendor must be in "Approved" status before contract execution.

| Status | Allowed Contract Action |
|--------|------------------------|
| Approved | Contract may proceed |
| Pending | Cannot execute contract |
| Suspended | No new contracts, existing may continue or terminate |
| Removed | No contracts permitted |

**Step 3: Enter Contract Details**

| Field | Guidance |
|-------|----------|
| Contract_Name | Descriptive name (project/service name) |
| Contract_Type | Fixed-price, T&M, Staff Augmentation, Managed Service |
| Start_Date | Contract effective date |
| End_Date | Contract expiration or completion date |
| Project_Classification | Risk classification driving security requirements |
| Contract_Value | Total contract value in CHF |
| Primary_Contact | Internal project manager name |

**Step 4: Document Review Dates**

| Field | Description | Example |
|-------|-------------|---------|
| Legal_Review_Date | Date Legal approved contract | 15.01.2026 |
| Security_Review_Date | Date IT Security approved clauses | 12.01.2026 |

Security review must be complete BEFORE contract execution.

**Step 5: Set Contract Status**

| Status | When Used | Triggers |
|--------|-----------|----------|
| Active | Contract in effect | After execution |
| Completed | Deliverables accepted, obligations fulfilled | After termination checklist |
| Terminated | Contract ended early | For-cause or convenience termination |

### Sheet 2: Security Clause Checklist – Completion Guide

**Purpose**: Verify that all mandatory security clauses are included in the contract before execution.

**Step-by-Step Completion:**

**Step 1: Link to Contract**

Enter the Contract_ID from Sheet 1.

**Step 2: Work Through Each Clause Category**

Complete verification for all 14 mandatory security clause categories:

**Category 1: Secure Coding Standards Compliance**

| Check Item | Requirement | Standard Language |
|------------|-------------|-------------------|
| Coding standards reference | Vendor follows OWASP, SANS, or equivalent | "Vendor shall adhere to OWASP Secure Coding Practices" |
| Input validation | All inputs validated and sanitized | "All user inputs shall be validated server-side" |
| Output encoding | Proper encoding to prevent XSS | "All output shall be properly encoded" |
| Error handling | Secure error handling without information disclosure | "Error messages shall not reveal system internals" |

**Category 2: Security Policy Compliance**

| Check Item | Requirement |
|------------|-------------|
| Policy acknowledgment | Vendor acknowledges organisation security policies |
| Policy adherence | Vendor agrees to comply with security policies |
| Change notification | Vendor notifies of security-relevant changes |
| Training verification | Vendor confirms security training for personnel |

**Category 3: Vulnerability Remediation SLAs**

| Severity | Required SLA | Maximum SLA |
|----------|--------------|-------------|
| Critical | 7 days | 14 days |
| High | 30 days | 45 days |
| Medium | 90 days | 120 days |
| Low | 180 days | Best effort |

Include escalation procedures for SLA breaches.

**Category 4: Security Testing Rights**

| Check Item | Requirement |
|------------|-------------|
| Right to test | Organisation may conduct security testing |
| Test notification | Testing notification requirements (if any) |
| Access provision | Vendor provides necessary access for testing |
| Finding acceptance | Vendor accepts findings as valid |

**Category 5: Audit Rights**

| Check Item | Requirement |
|------------|-------------|
| Right to audit | Organisation may audit vendor security practices |
| Audit notice | Reasonable notice period (typically 5-10 business days) |
| Audit scope | Security controls, code, processes |
| Finding remediation | Vendor addresses audit findings within agreed timeframe |
| Third-party audit | Organisation may use third-party auditors |

**Category 6: Incident Notification (24-hour)**

| Check Item | Requirement |
|------------|-------------|
| Notification timeline | 24 hours for security incidents |
| Notification method | Defined contact method (email, phone) |
| Notification content | Required information in notification |
| Cooperation | Vendor cooperates with investigation |

**Category 7: Data Protection/Confidentiality**

| Check Item | Requirement |
|------------|-------------|
| Confidentiality obligations | Vendor maintains confidentiality |
| Data handling | Defined data handling procedures |
| Data location | Data processing locations specified |
| Return/destruction | Data return or destruction at termination |
| Personnel confidentiality | Vendor staff bound by confidentiality |

**Category 8: Subcontractor Restrictions**

| Check Item | Requirement |
|------------|-------------|
| Prior approval | Subcontractors require written approval |
| Flow-down | Security requirements flow to subcontractors |
| Liability | Vendor liable for subcontractor compliance |
| Disclosure | Vendor discloses all subcontractors |

**Category 9: IP/Code Ownership**

| Check Item | Requirement |
|------------|-------------|
| Ownership transfer | Code ownership transfers to organisation |
| Background IP | Pre-existing IP clearly identified |
| License grants | Clear license terms for any retained IP |
| Escrow | Source code escrow for critical systems |

**Category 10: Source Code Escrow (if applicable)**

| Check Item | Requirement |
|------------|-------------|
| Escrow agent | Identified third-party escrow provider |
| Deposit schedule | Regular code deposits (e.g., quarterly) |
| Release conditions | Defined release triggers (bankruptcy, breach) |
| Verification | Periodic escrow verification rights |

**Category 11: Personnel Security Requirements**

| Check Item | Requirement |
|------------|-------------|
| Background checks | Vendor screens personnel |
| Security training | Vendor ensures security awareness |
| Identification | Vendor identifies personnel working on project |
| Removal right | Organisation may request personnel removal |

**Category 12: Termination/Transition Security**

| Check Item | Requirement |
|------------|-------------|
| Access revocation | Immediate access termination |
| Data return | Complete data return within defined period |
| Destruction certificate | Certification of data destruction |
| Transition assistance | Vendor provides reasonable transition support |

**Category 13: Insurance Requirements**

| Check Item | Requirement |
|------------|-------------|
| Cyber liability | Minimum coverage amount (e.g., CHF 5M) |
| Professional indemnity | Minimum coverage amount |
| Certificate requirement | Annual certificate provision |
| Notice of change | Notification of coverage changes |

**Category 14: Liability Provisions**

| Check Item | Requirement |
|------------|-------------|
| Security breach liability | Vendor liability for security breaches |
| Limitation carve-outs | Security breaches excluded from liability caps |
| Indemnification | Vendor indemnifies for security failures |
| Insurance coverage | Liability backed by insurance |

**Step 3: Document Clause Status**

For each clause, record:

| Status | Meaning | Action Required |
|--------|---------|-----------------|
| Yes | Clause included as required | None |
| No | Clause missing | Negotiate inclusion or risk acceptance |
| N/A | Clause not applicable | Document rationale |
| Modified | Clause modified from standard | Document modification and approval |

**Step 4: Record Evidence**

For each clause, document:
- Contract section/paragraph reference
- Any modifications and approval
- Reviewer name and date

### Sheet 3: SLA Compliance Tracking – Completion Guide

**Purpose**: Track vendor compliance with vulnerability remediation SLAs established in contracts.

**Step-by-Step Completion:**

**Step 1: Generate SLA Record**

Create unique identifier using format `SLA-XXXX` when a vulnerability is reported against outsourced code:

| Field | Source | Example |
|-------|--------|---------|
| SLA_ID | Auto-generated | SLA-0234 |
| Contract_ID | From Sheet 1 | CTR-0089 |
| Vulnerability_ID | From security testing | VULN-2026-0156 |

**Step 2: Classify Vulnerability**

| Severity | Definition | Contractual SLA |
|----------|------------|-----------------|
| Critical | Remote code execution, auth bypass, data exposure | 7 days |
| High | Privilege escalation, significant security impact | 30 days |
| Medium | Information disclosure, limited impact | 90 days |
| Low | Minor issues, best practice recommendations | 180 days |

**Step 3: Calculate SLA Due Date**

```
SLA_Due_Date = Discovery_Date + SLA_Days
```

Exclude weekends and holidays if contract specifies business days.

**Step 4: Track Remediation**

| Status | Definition | Action |
|--------|------------|--------|
| Pending | Within SLA period, not yet fixed | Monitor |
| Met | Remediated before SLA expiry | Record completion date |
| Missed | SLA expired without remediation | Escalate, document |
| Exception | SLA extended with approval | Document approval |

**Step 5: Manage Exceptions**

When SLA cannot be met:

1. Vendor requests extension with justification
2. IT Security evaluates risk and compensating controls
3. Appropriate authority approves exception
4. Document in Exception Register (ISMS-IMP-A.8.30.4)

| Exception Approver | Severity | Maximum Extension |
|--------------------|----------|-------------------|
| IT Security Manager | Medium/Low | 30 days |
| CISO | High | 30 days |
| CISO + Executive | Critical | 14 days |

### Sheet 4: Subcontractor Approvals – Completion Guide

**Purpose**: Track approval of subcontractors used by primary vendors.

**Step-by-Step Completion:**

**Step 1: Generate Approval Record**

When vendor requests subcontractor approval:

| Field | Source | Example |
|-------|--------|---------|
| Approval_ID | Auto-generated | SUB-0045 |
| Contract_ID | Primary contract | CTR-0089 |
| Primary_Vendor_ID | From Vendor Registry | VND-0042 |

**Step 2: Capture Subcontractor Details**

| Field | Guidance |
|-------|----------|
| Subcontractor_Name | Legal entity name |
| Subcontractor_Scope | Specific work to be performed |
| Access_Level | Direct (to org systems), Via Vendor, or None |

**Step 3: Determine Assessment Level**

| Access Level | Risk | Assessment Required |
|--------------|------|---------------------|
| Direct | High | Full assessment (as primary vendor) |
| Via Vendor | Medium | Abbreviated assessment |
| None | Low | Vendor attestation sufficient |

**Step 4: Verify Flow-Down**

Confirm that:
- Primary vendor's contract with subcontractor includes security requirements
- Subcontractor bound by same confidentiality obligations
- Audit rights extend to subcontractor
- Incident notification obligations flow down

**Step 5: Record Approval**

| Field | Guidance |
|-------|----------|
| Risk_Classification | Based on access and scope |
| Approval_Status | Approved, Pending, Rejected |
| Approved_By | Based on risk classification |
| Approval_Date | Date approval granted |
| Expiry_Date | Typically annual renewal |
| Flow_Down_Verified | Confirmation security requirements flow down |

**Approval Authority:**

| Subcontractor Risk | Approver |
|--------------------|----------|
| High (Direct access to critical systems) | CISO |
| Medium (Direct access to standard systems) | IT Security Manager |
| Low (Via Vendor or No access) | IT Security Lead |

### Sheet 5: Termination Checklist – Completion Guide

**Purpose**: Verify all security requirements are met when contracts terminate.

**Step-by-Step Completion:**

**Step 1: Initiate Termination Checklist**

When contract is ending (completion, early termination, or breach):

| Field | Guidance |
|-------|----------|
| Contract_ID | Contract being terminated |
| Termination_Type | Completion, Early, or Breach |
| Termination_Date | Effective termination date |

**Step 2: Work Through Each Checklist Item**

Complete all 10 standard termination items:

**Item 1: All Access Credentials Revoked (within 24 hours)**

| Verification | Evidence |
|--------------|----------|
| System access removed | Access termination confirmation |
| Repository access removed | Git/VCS access audit |
| VPN/remote access removed | VPN admin confirmation |
| Shared credentials rotated | Credential rotation log |

**Item 2: Organisation Data Returned or Destroyed**

| Verification | Evidence |
|--------------|----------|
| Data inventory confirmed | Data register |
| Data returned (if applicable) | Transfer confirmation |
| Destruction ordered | Destruction request |
| Destruction confirmed | Destruction certificate |

**Item 3: Destruction Certificate Received**

| Requirements | Standard |
|--------------|----------|
| Signed by authorised vendor representative | Officer-level |
| Lists data types destroyed | Specific enumeration |
| Specifies destruction method | NIST 800-88 compliant |
| Dated within termination period | Within 30 days |

**Item 4: Source Code Transferred (if applicable)**

| Verification | Evidence |
|--------------|----------|
| Code repository access provided | Repository URL |
| Complete code history | Full git history |
| Build instructions | README/build docs |
| Test suites included | Test coverage report |

**Item 5: Documentation Transferred**

| Documentation | Status |
|---------------|--------|
| Design documents | Received |
| API documentation | Received |
| User guides | Received |
| Administrator guides | Received |
| Architecture diagrams | Received |

**Item 6: Escrow Arrangements Verified**

| Verification | Evidence |
|--------------|----------|
| Final code deposit made | Escrow receipt |
| Deposit verified | Verification report |
| Release procedures confirmed | Escrow agreement |

**Item 7: Outstanding Vulnerabilities Addressed or Risk Accepted**

| Status | Action |
|--------|--------|
| All Critical/High resolved | Sign-off |
| Outstanding items | Formal risk acceptance |
| Risk accepted | Exception documented |

**Item 8: Final Security Review Completed**

| Review Item | Status |
|-------------|--------|
| Final code scan | Complete |
| Open findings triaged | Complete |
| Security debt documented | Complete |

**Item 9: Lessons Learned Documented**

| Topic | Documentation |
|-------|---------------|
| What went well | Success factors |
| What could improve | Improvement areas |
| Security observations | Security-specific lessons |
| Process improvements | Recommendations |

**Item 10: Vendor Removed from Active Registry**

| Action | Verification |
|--------|--------------|
| Vendor Registry updated | Status changed to Removed (if applicable) |
| Contract marked Completed | Sheet 1 status updated |
| Final documentation filed | Evidence folder complete |

---

## Evidence Collection

### Evidence Requirements

Evidence must be collected and stored for all contract compliance activities:

| Evidence Category | Retention Period | Storage Location |
|-------------------|------------------|------------------|
| Contract copies | 10 years after termination | Contract Management System |
| Clause checklists | Duration of contract + 7 years | ISMS Evidence Library |
| SLA records | 7 years | ISMS Evidence Library |
| Subcontractor approvals | Duration of approval + 3 years | ISMS Evidence Library |
| Termination records | 10 years | ISMS Evidence Library |
| Destruction certificates | 10 years | ISMS Evidence Library |

### Evidence Folder Structure

```
ISMS-Evidence-Library/
└── Contract-Compliance/
    └── A.8.30-Outsourced-Development/
        └── [Contract_ID]-[Vendor_Name]/
            ├── Contract/
            │   ├── Executed-Contract.pdf
            │   ├── Security-Schedule.pdf
            │   └── Amendments/
            ├── Clause-Review/
            │   ├── Security-Clause-Checklist.xlsx
            │   └── Approval-Email.pdf
            ├── SLA-Compliance/
            │   ├── Monthly-Reports/
            │   └── Exception-Records/
            ├── Subcontractors/
            │   └── [SUB-ID]-[Name]/
            └── Termination/
                ├── Checklist.xlsx
                └── Destruction-Certificate.pdf
```

### Evidence for Audit

During ISO 27001 audit, be prepared to demonstrate:

| Auditor Request | Evidence to Provide |
|-----------------|---------------------|
| "Show me how security requirements are included in contracts" | Sheet 2 examples + contract extracts |
| "How do you track vulnerability remediation SLAs?" | Sheet 3 + SLA compliance report |
| "How are subcontractors managed?" | Sheet 4 + approval workflow evidence |
| "What happens when a contract ends?" | Sheet 5 + sample termination package |
| "Show me a non-compliant scenario and how it was handled" | Exception records, escalation evidence |

---

## Common Pitfalls

### Contract Review Errors

❌ **MISTAKE: Executing contracts before security review**
Security clause review must be complete BEFORE contract execution. Post-execution amendments are difficult and costly.

❌ **MISTAKE: Accepting "we'll negotiate security separately"**
Security requirements must be in the main contract or executed security schedule. Verbal agreements are unenforceable.

❌ **MISTAKE: Using outdated security clause templates**
Contract templates must be reviewed annually. Regulatory changes (GDPR, FADP) require contract updates.

❌ **MISTAKE: Not involving Legal in clause modifications**
Modified security clauses have legal implications. All modifications require Legal approval.

### SLA Management Errors

❌ **MISTAKE: Not tracking SLA start dates accurately**
The SLA clock starts when the vulnerability is reported to the vendor. Document notification date with evidence.

❌ **MISTAKE: Informal SLA extensions without documentation**
All SLA extensions must be formally documented with approver and new due date. Verbal extensions are not valid.

❌ **MISTAKE: Not escalating repeated SLA misses**
Pattern of SLA non-compliance should trigger contract review. Track vendor performance over time.

### Subcontractor Management Errors

❌ **MISTAKE: Discovering subcontractors after engagement**
Require upfront disclosure of all subcontractors. Undisclosed subcontractors are a contract breach.

❌ **MISTAKE: Approving subcontractors without flow-down verification**
Security requirements must flow down to subcontractors. Verify before approval.

❌ **MISTAKE: Not tracking subcontractor approval expiry**
Approvals have expiration dates. Lapsed approvals require re-evaluation.

### Termination Errors

❌ **MISTAKE: Not revoking access immediately**
Access revocation must occur within 24 hours of termination. Delays create security exposure.

❌ **MISTAKE: Accepting verbal destruction confirmations**
Destruction must be certified in writing. Certificates must specify data types and destruction method.

❌ **MISTAKE: Not verifying code completeness before termination**
Verify all code, documentation, and build artifacts are received before final payment.

---

## Quality Checklist

### Pre-Contract Execution Checklist

Before executing any outsourced development contract:

**Clause Verification**
- [ ] All 14 mandatory clause categories reviewed
- [ ] Missing clauses escalated for risk acceptance
- [ ] Modified clauses approved by Legal and IT Security
- [ ] Contract section references documented
- [ ] Security review sign-off obtained

**Vendor Verification**
- [ ] Vendor in Approved status in registry
- [ ] Vendor risk tier appropriate for project
- [ ] Vendor assessment current (within 12 months)

**Documentation**
- [ ] Contract copy filed
- [ ] Clause checklist completed
- [ ] Approval emails archived

### Ongoing Compliance Checklist

Monthly verification:

- [ ] SLA tracking current
- [ ] Overdue SLAs escalated
- [ ] Subcontractor approvals current
- [ ] Contract expiry alerts configured

### Termination Checklist

Before marking contract complete:

- [ ] All 10 termination items verified
- [ ] Evidence collected for each item
- [ ] Destruction certificate received
- [ ] Registry updated
- [ ] Contract status updated to Completed

---

## Review and Approval

### Contract Approval Authority

| Contract Value | Clause Compliance | Final Approval |
|----------------|-------------------|----------------|
| Any value | IT Security + Legal | Per financial delegation |
| > CHF 500K | CISO review | Executive approval |
| Critical systems | CISO mandatory | Executive approval |

### Exception Approval Authority

| Exception Type | Approver |
|----------------|----------|
| Missing mandatory clause (Standard) | CISO |
| Missing mandatory clause (Critical) | CISO + Executive |
| SLA extension (Medium/Low) | IT Security Manager |
| SLA extension (High/Critical) | CISO |

### Review Workflow

```
Contract Drafted (Procurement/Legal)
         ↓
Security Clause Review (IT Security)
         ↓
Gap Analysis and Negotiation
         ↓
Final Clause Checklist Completion
         ↓
Security Sign-off
         ↓
Legal Sign-off
         ↓
Commercial Sign-off
         ↓
Contract Execution
```

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
