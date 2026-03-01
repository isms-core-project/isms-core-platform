<!-- ISMS-CORE:IMP:ISMS-IMP-A.6.6.2-UG:framework:UG:a.6.6.2 -->
**ISMS-IMP-A.6.6.2-UG - NDA Execution and Tracking**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.6.6

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | NDA Execution and Tracking |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.6.6.2-UG |
| **Related Policy** | ISMS-POL-A.6.6 (Confidentiality Nda) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.6) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.6.6 (Confidentiality Nda)
- ISMS-IMP-A.6.6.1 (NDA Template Registry and Inventory)
- ISMS-IMP-A.6.6.3 (NDA Review and Compliance)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.6.6.2-TG.

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Active NDAs | Inventory of all active signed NDAs and confidentiality agreements |
| 3 | Signatory Register | Track all parties who have signed NDAs |
| 4 | Expiration Monitor | Monitor NDA expiry dates and renewal requirements |
| 5 | Renewal Tracking | Manage NDA renewal and re-execution processes |
| 6 | Evidence Register | Store and reference copies of executed agreements |
| 7 | Summary Dashboard | Compliance status and key metrics overview |
| 8 | Approval Sign-Off | Management review sign-off and certification |

---

## Assessment Overview

### Purpose

This workbook provides comprehensive tracking of all executed (signed) Non-Disclosure Agreements (NDAs) and confidentiality agreements across the organisation. It serves as the authoritative record for:

- **Active NDA Inventory**: Complete catalogue of all signed, active NDAs
- **Signatory Tracking**: Individual-level tracking of every person bound by confidentiality obligations
- **Expiration Management**: Proactive monitoring of agreement lifecycles and renewal requirements
- **Renewal Workflow**: Systematic management of the renewal process for expiring agreements
- **Compliance Evidence**: Audit-ready documentation demonstrating Control A.6.6 compliance

The NDA Execution and Tracking workbook is the operational core of the organisation's confidentiality agreement programme. Without comprehensive tracking, the organisation cannot demonstrate that required NDAs are in place or monitor compliance with confidentiality obligations.

### Scope

This assessment covers the following components:

**In Scope:**
- All signed confidentiality and non-disclosure agreements
- Employee confidentiality agreements and clauses
- Contractor and consultant NDAs
- Vendor and supplier confidentiality agreements
- Partner and customer NDAs
- Board member and investor confidentiality agreements
- Individual signatory records and status
- Agreement expiration dates and renewal tracking
- Post-termination obligation monitoring
- Signature evidence and verification
- Renewal workflow management

**Out of Scope:**
- NDA template management (covered in ISMS-IMP-A.6.6.1)
- NDA compliance monitoring and auditing (covered in ISMS-IMP-A.6.6.3)
- Contract negotiation processes
- Legal dispute management

### Business Value

Effective NDA execution and tracking delivers:

| Value Area | Benefit |
|------------|---------|
| **Legal Protection** | Enforceable agreements with complete execution records |
| **Audit Readiness** | Immediate access to signed agreements and signatory records |
| **Risk Management** | No gaps in confidentiality coverage for any stakeholder |
| **Compliance Demonstration** | Evidence that NDAs are signed before information access |
| **Proactive Management** | Early warning of expiring agreements enables timely renewal |
| **Operational Efficiency** | Centralised tracking reduces administrative burden |

### Assessment Frequency

| Activity | Frequency | Responsible Party |
|----------|-----------|-------------------|
| New NDA Registration | Within 24 hours of execution | HR/Procurement/Legal |
| Signatory Status Update | Within 48 hours of change | HR/Contract Manager |
| Expiration Review | Weekly | ISMS Administrator |
| Renewal Initiation | 90 days before expiry | Contract Owner |
| Full Assessment | Quarterly | Information Security Manager |

---

## Control Requirements

### ISO 27001:2022 Control A.6.6

> *"Confidentiality or non-disclosure agreements reflecting the organisation's needs for the protection of information should be identified, documented, regularly reviewed and signed by personnel and other relevant interested parties."*

**Control Type:** Preventive
**Security Properties:** Confidentiality
**Cybersecurity Concepts:** Protect
**Operational Capabilities:** Legal and Compliance

### Execution Requirements

Control A.6.6 explicitly requires that NDAs be "signed by personnel and other relevant interested parties." This mandate requires:

**1. Signature Before Access**
- NDAs must be executed before individuals gain access to confidential information
- No exceptions permitted without documented risk acceptance
- Signature date must precede any system access provisioning date

**2. Complete Signatory Records**
- Every individual with access to confidential information must be tracked
- Signature evidence must be retained (wet signatures scanned, digital certificates retained)
- Signatory status must be kept current

**3. Lifecycle Management**
- Agreement validity periods must be tracked
- Expired agreements must be renewed or relationships terminated
- Post-termination obligations must be monitored

**4. Evidence Retention**
- Original signed agreements must be securely stored
- Digital signature certificates must be retained
- Audit trail of signatory changes must be maintained

### What Auditors Look For

ISO 27001 auditors examining NDA execution will verify:

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Signature Trail** | Signed NDA for every individual with confidential access |
| **Timing Verification** | Proof that NDA was signed before access was granted |
| **Completeness** | Coverage of all stakeholder categories |
| **Currency** | No expired agreements for active relationships |
| **Signatory Records** | Ability to identify all individuals bound by each NDA |
| **Storage Security** | Signed agreements stored securely with backup |
| **Process Integration** | NDA execution integrated into onboarding workflows |

### Common Audit Questions

Auditors frequently ask:

1. *"Show me the signed NDA for this contractor who has system access."*
2. *"When was this employee's confidentiality agreement signed relative to their start date?"*
3. *"Which NDAs are due to expire in the next 90 days?"*
4. *"How many individuals are bound by this vendor NDA?"*
5. *"Show me the renewal process for this expired agreement."*

---

## Prerequisites

### Before Starting This Assessment

Complete the following prerequisites to ensure successful assessment completion:

#### Required Access

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| HR Information System | Read | Employee NDA records |
| Contract Management System | Read | Vendor/contractor NDAs |
| Document Management System | Read/Write | Signed NDA storage |
| ISMS Evidence Library | Write | Upload evidence |
| Identity Management System | Read | Access provisioning dates |

#### Required Information

| Information | Source | Why Needed |
|-------------|--------|------------|
| All signed NDAs (physical and digital) | HR, Legal, Procurement | NDA inventory |
| Employee roster with start dates | HR | Verify timing |
| Contractor and vendor list | Procurement | Completeness check |
| Access provisioning records | IT/IAM | Timing verification |
| Previous assessment (if any) | ISMS Evidence Library | Continuity |

#### Required Approvals

| Approval | Approver | When Needed |
|----------|----------|-------------|
| Access to HR records | HR Director | Before starting |
| Access to contract repository | Legal Counsel | Before starting |
| Permission to compile signatory data | CISO | Before starting |

#### Prerequisite Checklist

Before proceeding, verify:

- [ ] Access to signed NDA repository is confirmed
- [ ] HR contact is available for employee NDA queries
- [ ] Legal/Procurement contact is available for vendor NDA queries
- [ ] Identity management records are accessible
- [ ] Previous assessment has been reviewed
- [ ] Reporting structure for signatories is understood
- [ ] Renewal process owners are identified
- [ ] Evidence storage locations are identified

---

## NDA Execution Process

### Standard Execution Workflow

Understanding the NDA execution process ensures accurate tracking. The standard workflow is:

```
Template Selection (ISMS-IMP-A.6.6.1)
        │
        ▼
NDA Preparation
        │ (Populate template with party details)
        ▼
Internal Approval
        │ (Legal review if non-standard terms)
        ▼
Counterparty Delivery
        │ (Send for signature)
        ▼
Counterparty Signature
        │ (Wet signature, DocuSign, etc.)
        ▼
Organisation Signature
        │ (Authorised signatory)
        ▼
Execution Complete
        │ (Both parties signed)
        ▼
Registration in Tracker
        │ (This workbook)
        ▼
Secure Storage
        │ (Signed original archived)
        ▼
Access Provisioning
        │ (Can now grant access)
```

### Execution Timing Requirements

| Stakeholder Category | NDA Must Be Signed | Before |
|---------------------|--------------------|--------|
| Employees | Before start date | First day of work |
| Contractors | Before engagement | Contract start |
| Vendors | Before contract | Service commencement |
| Partners | Before discussions | Information sharing |
| Visitors | At arrival | Secure area access |
| Candidates | Before interview | Sensitive role interviews |

### Signature Methods

The organisation accepts the following signature methods:

| Method | Description | Evidence Required |
|--------|-------------|-------------------|
| **Wet Signature** | Physical pen-on-paper signature | Scanned original or PDF |
| **Digital Signature** | PKI-based cryptographic signature | Certificate and signed document |
| **Electronic Signature** | DocuSign, Adobe Sign, etc. | Certificate of completion |
| **Click-to-Accept** | Online acknowledgement (limited use) | System log with timestamp |

**Note:** Wet signatures and qualified digital signatures are preferred for commercial agreements. Click-to-accept may only be used for visitor acknowledgements and similar low-risk scenarios.

### Multi-Party NDAs

For NDAs with multiple signatories (e.g., mutual NDAs between companies with multiple authorised representatives):

1. Track the NDA as a single record in Active_NDAs
2. Create individual records in Signatory_Register for each person
3. Link all signatories to the same NDA_ID
4. Record each person's signature date separately
5. NDA is only "Active" when all required signatures are obtained

---

## Completion Walkthrough

### Step 1: Review Instructions Sheet

**Time estimate:** 10-15 minutes

1. Read the document purpose and scope section
2. Note the contact information for queries
3. Review the sheet navigation sequence
4. Understand the data relationships between sheets
5. Check workbook version matches this specification

### Step 2: Complete Active_NDAs Sheet

**Time estimate:** 2-4 hours (depending on NDA count)

For each executed NDA, complete the following fields:

#### Column A: NDA_ID

- **Format:** NDA-EXE-YYYY-XXXX (where YYYY is year, XXXX is sequential)
- **Example:** NDA-EXE-2026-0042
- **Rules:** Must be unique, never reuse IDs
- **Guidance:** Reset sequence annually for easier date-based filtering

#### Column B: Template_Ref

- **Format:** Link to Template_ID from ISMS-IMP-A.6.6.1
- **Example:** NDA-TMP-001
- **Rules:** Must match a valid template in Template Registry
- **Guidance:** If custom/one-off NDA, enter "CUSTOM" and note in Comments

#### Column C: NDA_Title

- **Format:** Descriptive title
- **Example:** Mutual Non-Disclosure Agreement - Acme Corporation
- **Rules:** Include counterparty name for easy identification
- **Guidance:** Use consistent naming convention for searchability

#### Column D: Counterparty_Name

- **Format:** Legal entity name
- **Example:** Acme Corporation Ltd.
- **Rules:** Use full legal name as appears on agreement
- **Guidance:** For employees, enter "Employee" and record individual in Signatory_Register

#### Column E: Counterparty_Type

- **Format:** Select from dropdown validation list
- **Options:**
  - Employee
  - Contractor
  - Consultant
  - Vendor
  - Supplier
  - Partner
  - Customer
  - Board Member
  - Investor
  - Visitor
  - Candidate
  - Other
- **Guidance:** Select the primary relationship type

#### Column F: Execution_Date

- **Format:** DD.MM.YYYY (Swiss date format)
- **Example:** 15.01.2026
- **Rules:** Date when last required signature was obtained
- **Guidance:** This is when the agreement became fully executed

#### Column G: Effective_Date

- **Format:** DD.MM.YYYY (Swiss date format)
- **Example:** 15.01.2026
- **Rules:** Date when agreement obligations commence
- **Guidance:** Often same as Execution_Date; may be different if specified in agreement

#### Column H: Expiration_Date

- **Format:** DD.MM.YYYY or "Indefinite"
- **Example:** 14.01.2029 or Indefinite
- **Rules:** As specified in the agreement
- **Guidance:** Calculate from effective date plus term; use "Indefinite" if no expiry

#### Column I: Term_Years

- **Format:** Number or "Indefinite"
- **Example:** 3
- **Rules:** Agreement duration in years
- **Guidance:** Helps identify renewal patterns

#### Column J: Post_Term_Period

- **Format:** Number of years or "Indefinite"
- **Example:** 2
- **Rules:** How long confidentiality obligations survive after termination
- **Guidance:** Critical for tracking ongoing obligations after relationship ends

#### Column K: Post_Term_Expiry

- **Format:** DD.MM.YYYY or calculated
- **Example:** 14.01.2031
- **Rules:** Date when all obligations cease
- **Guidance:** Formula: Expiration_Date + Post_Term_Period (or "See Indefinite")

#### Column L: Signatories_Count

- **Format:** Number
- **Example:** 2
- **Rules:** Total number of individual signatories
- **Guidance:** Should match count of records in Signatory_Register for this NDA

#### Column M: Our_Signatory

- **Format:** Name and title
- **Example:** John Smith, CEO
- **Rules:** Who signed on behalf of our organisation
- **Guidance:** Must be an authorised signatory per delegation of authority

#### Column N: Storage_Location

- **Format:** System path or repository reference
- **Example:** SharePoint/Legal/Executed NDAs/2026/NDA-EXE-2026-0042.pdf
- **Rules:** Must be a secure, backed-up location
- **Guidance:** Original signed documents, not copies

#### Column O: Status

- **Format:** Select from dropdown validation list
- **Options:**
  - Active – Currently in effect
  - Expired – Term ended, within post-term period
  - Terminated – Ended early by agreement
  - Renewed – Replaced by new NDA
  - Superseded – Replaced by amended version
  - Post-Term – Agreement ended, post-term obligations active
  - Fully Expired – All obligations ended
- **Guidance:** Update status promptly as circumstances change

#### Column P: Renewal_Required

- **Format:** Yes/No/TBD
- **Example:** Yes
- **Rules:** Whether this NDA should be renewed before expiry
- **Guidance:** Based on ongoing business relationship

#### Column Q: Renewal_Owner

- **Format:** Name or department
- **Example:** Procurement Department
- **Rules:** Who is responsible for initiating renewal
- **Guidance:** Must be assigned for all NDAs with expiration dates

#### Column R: Comments

- **Format:** Free text
- **Example:** Covers entire project team for Project Alpha
- **Rules:** Maximum 500 characters
- **Guidance:** Any relevant notes, special provisions, or context

### Step 3: Complete Signatory_Register Sheet

**Time estimate:** 1-3 hours (depending on signatory count)

For each individual signatory, complete the following fields:

#### Column A: Signatory_ID

- **Format:** SIG-YYYY-XXXXX
- **Example:** SIG-2026-00142
- **Rules:** Must be unique across all signatories

#### Column B: NDA_Ref

- **Format:** Link to NDA_ID from Active_NDAs
- **Example:** NDA-EXE-2026-0042
- **Rules:** Must match a valid NDA in Active_NDAs

#### Column C: Signatory_Name

- **Format:** Full legal name
- **Example:** Maria Schmidt
- **Rules:** As appears on signed document

#### Column D: Signatory_Type

- **Format:** Select from dropdown
- **Options:**
  - Employee
  - Contractor
  - Consultant
  - Vendor Representative
  - Partner Representative
  - Customer Representative
  - Board Member
  - Investor
  - Visitor
  - Witness
  - Authorised Signatory (Our Org)
  - Other

#### Column E: Organisation

- **Format:** Employer/company name
- **Example:** [Our Organisation] or Acme Corporation
- **Rules:** Their employer, not the NDA counterparty (if different)

#### Column F: Role_Title

- **Format:** Job title or role
- **Example:** Software Developer, Managing Director
- **Rules:** Title at time of signing

#### Column G: Department

- **Format:** Department name
- **Example:** Engineering, Legal
- **Rules:** Their department (for employees/contractors)

#### Column H: Email

- **Format:** Email address
- **Example:** maria.schmidt@example.com
- **Rules:** Primary contact email

#### Column I: Signature_Date

- **Format:** DD.MM.YYYY
- **Example:** 14.01.2026
- **Rules:** Exact date this individual signed
- **Guidance:** May differ from NDA Execution_Date if multi-party

#### Column J: Signature_Method

- **Format:** Select from dropdown
- **Options:**
  - Wet Signature
  - Digital Signature
  - DocuSign
  - Adobe Sign
  - Other E-Signature
  - Click-to-Accept

#### Column K: Relationship_Start

- **Format:** DD.MM.YYYY
- **Example:** 15.01.2026
- **Rules:** When their relationship with organisation began
- **Guidance:** Employment start date, contract start, etc.

#### Column L: Relationship_End

- **Format:** DD.MM.YYYY or blank
- **Example:** 31.12.2026 or (blank if ongoing)
- **Rules:** When their relationship ended
- **Guidance:** Leave blank if relationship is ongoing

#### Column M: Access_Granted_Date

- **Format:** DD.MM.YYYY
- **Example:** 15.01.2026
- **Rules:** When access to confidential information was granted
- **Guidance:** Must be on or after Signature_Date

#### Column N: Status

- **Format:** Select from dropdown
- **Options:**
  - Active – Currently has access
  - Terminated – Relationship ended, within post-term
  - Post-Term Expired – All obligations ended
  - Suspended – Temporarily restricted
- **Guidance:** Update when relationship changes

#### Column O: Notes

- **Format:** Free text
- **Example:** Project Alpha team lead, primary contact
- **Rules:** Maximum 300 characters

### Step 4: Complete Expiration_Monitor Sheet

**Time estimate:** 30-60 minutes (largely automated)

This sheet provides at-a-glance visibility of expiring NDAs:

#### Column A: NDA_ID

- **Formula:** Linked from Active_NDAs
- **Purpose:** Reference to full NDA record

#### Column B: Counterparty

- **Formula:** Linked from Active_NDAs
- **Purpose:** Quick identification

#### Column C: Expiration_Date

- **Formula:** Linked from Active_NDAs
- **Purpose:** When agreement expires

#### Column D: Days_Until_Expiry

- **Formula:** =Expiration_Date - TODAY()
- **Purpose:** Countdown to expiry

#### Column E: Alert_Status

- **Formula:** Conditional based on Days_Until_Expiry
- **Thresholds:**
  - Green: >90 days
  - Amber: 30-90 days
  - Red: <30 days
  - Expired: <0 days

#### Column F: Renewal_Required

- **Formula:** Linked from Active_NDAs
- **Purpose:** Whether renewal is needed

#### Column G: Renewal_Owner

- **Formula:** Linked from Active_NDAs
- **Purpose:** Who manages renewal

#### Column H: Renewal_Status

- **Formula:** Linked from Renewal_Tracking (if exists)
- **Purpose:** Current renewal progress

#### Column I: Action_Required

- **Format:** Manual entry
- **Example:** Initiate renewal discussion with procurement
- **Purpose:** Next steps for this NDA

### Step 5: Complete Renewal_Tracking Sheet

**Time estimate:** Variable (as renewals arise)

For each NDA requiring renewal, track the workflow:

#### Column A: Renewal_ID

- **Format:** RNW-YYYY-XXXX
- **Example:** RNW-2026-0012

#### Column B: Original_NDA

- **Format:** Link to NDA_ID
- **Example:** NDA-EXE-2023-0089

#### Column C: Counterparty

- **Format:** Party name
- **Purpose:** Quick reference

#### Column D: Original_Expiry

- **Format:** DD.MM.YYYY
- **Purpose:** When original NDA expires

#### Column E: Renewal_Initiated

- **Format:** DD.MM.YYYY
- **Purpose:** When renewal process started
- **Guidance:** Should be 90+ days before expiry

#### Column F: Initiated_By

- **Format:** Name
- **Purpose:** Who started the renewal

#### Column G: New_Terms_Required

- **Format:** Yes/No
- **Purpose:** Whether terms need updating
- **Guidance:** May require legal review if yes

#### Column H: Legal_Review_Status

- **Format:** Select from dropdown
- **Options:** Not Required, Pending, In Progress, Completed, N/A

#### Column I: Counterparty_Agreed

- **Format:** Yes/No/Pending/Declined
- **Purpose:** Counterparty's response to renewal

#### Column J: New_NDA_ID

- **Format:** Link to NDA_ID (when created)
- **Purpose:** Reference to replacement NDA

#### Column K: New_Expiry

- **Format:** DD.MM.YYYY
- **Purpose:** New NDA expiration date

#### Column L: Renewal_Completed

- **Format:** DD.MM.YYYY
- **Purpose:** When renewal was executed

#### Column M: Status

- **Format:** Select from dropdown
- **Options:**
  - Not Started
  - In Progress
  - Legal Review
  - Awaiting Counterparty
  - Awaiting Signature
  - Completed
  - Cancelled - No Longer Required
  - Failed - Counterparty Declined

#### Column N: Notes

- **Format:** Free text
- **Purpose:** Progress notes and issues

### Step 6: Complete Evidence_Register Sheet

**Time estimate:** 30-60 minutes

Document all evidence supporting the assessment:

| Field | Description |
|-------|-------------|
| Evidence_ID | EVD-A.6.6.2-XXX |
| Evidence_Description | What the evidence demonstrates |
| Evidence_Type | Signed NDA, Signature Certificate, etc. |
| Storage_Location | Path to evidence |
| Collection_Date | When collected |
| Collected_By | Who collected |

### Step 7: Complete Approval_SignOff Sheet

**Time estimate:** 15-30 minutes

1. Complete assessor information
2. Enter assessment completion date
3. Route to reviewers for sign-off
4. Obtain final approval

---

## Signatory Management

### Individual Tracking Requirements

Every person with access to confidential information must be individually tracked:

**Why Individual Tracking?**
- Auditors may request NDA evidence for any specific individual
- Termination processing requires knowing who is bound by which NDA
- Post-termination obligations are personal, not just organisational
- Access reviews must verify NDA status for each person

### Employee NDAs

For employees, track confidentiality at the individual level:

| Scenario | Tracking Approach |
|----------|-------------------|
| **Individual Employment NDA** | One NDA record per employee |
| **Confidentiality Clause in Contract** | Track as "Employment Confidentiality"; link contract |
| **Team/Project NDA** | One NDA record; multiple signatory records |
| **Updated/Renewed NDA** | New NDA record; mark old as "Renewed" |

### Contractor and Vendor NDAs

For commercial relationships:

| Scenario | Tracking Approach |
|----------|-------------------|
| **Company-to-Company NDA** | NDA record for agreement; signatory records for each individual with access |
| **Individual Contractor** | Both NDA record and signatory record for same person |
| **Vendor Team Access** | Request list of individuals; create signatory record for each |

### Signatory Status Lifecycle

```
┌─────────────────┐
│   NDA Signed    │
│   (Active)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Access Granted │
│   (Active)      │
└────────┬────────┘
         │
         ▼ (Relationship ends)
┌─────────────────┐
│  Access Revoked │
│ (Terminated/    │
│  Post-Term)     │
└────────┬────────┘
         │
         ▼ (Post-term expires)
┌─────────────────┐
│ Post-Term Expired│
│(All obligations │
│     ended)      │
└─────────────────┘
```

### Termination Processing

When a signatory's relationship ends:

1. **Update Signatory_Register:**
   - Set Relationship_End date
   - Update Status to "Terminated"

2. **Verify Access Revocation:**
   - Confirm system access has been removed
   - Record date of access revocation

3. **Calculate Post-Term Period:**
   - Determine when obligations end
   - Set reminder for post-term expiry

4. **Retain Records:**
   - Do not delete signatory records
   - Maintain for post-term period plus retention requirements

---

## Expiration and Renewal Management

### Expiration Alert Thresholds

The Expiration_Monitor sheet uses colour-coded alerts:

| Alert Level | Days to Expiry | Colour | Action Required |
|-------------|----------------|--------|-----------------|
| **Green** | >90 days | Light Green | No immediate action |
| **Amber** | 30-90 days | Light Yellow | Initiate renewal assessment |
| **Red** | <30 days | Light Red | Urgent renewal action |
| **Expired** | Past expiry | Dark Red | Immediate attention - gap! |

### Renewal Decision Process

When an NDA approaches expiration:

```
NDA Expiring (<90 days)
        │
        ▼
Is relationship continuing?
├── NO → Allow to expire; update status
└── YES → Continue...
    │
    └── Are current terms acceptable?
        ├── YES → Execute renewal with same template
        └── NO → Continue...
            │
            └── What changes needed?
                ├── Minor updates → Legal review; amend
                └── Major changes → Negotiate new agreement
```

### Renewal Workflow

**Standard Renewal Process:**

| Phase | Activities | Duration |
|-------|------------|----------|
| **1. Assessment** | Review relationship, terms, changes needed | 90-60 days prior |
| **2. Preparation** | Update template if needed; legal review | 60-45 days prior |
| **3. Negotiation** | Send to counterparty; negotiate if needed | 45-30 days prior |
| **4. Execution** | Obtain signatures | 30-15 days prior |
| **5. Registration** | Register new NDA; update old NDA status | Within 7 days of execution |

### Gap Management

If an NDA expires before renewal is complete:

1. **Assess Risk:**
   - Is confidential information still being shared?
   - What is the exposure during the gap?

2. **Interim Measures:**
   - Restrict information sharing to minimum necessary
   - Obtain written acknowledgement of continuing obligations
   - Escalate to Legal and CISO

3. **Documentation:**
   - Document the gap period
   - Record interim measures taken
   - Note in NDA comments field

4. **Expedited Renewal:**
   - Prioritise completion of new agreement
   - Consider shorter negotiation cycle

---

## Evidence Collection

### Evidence Requirements

The following evidence must be collected and maintained:

| Evidence Type | Description | Retention Period | Storage |
|---------------|-------------|------------------|---------|
| **Signed NDAs** | Original executed agreements | Life of agreement + 10 years | Secure document repository |
| **Signature Certificates** | DocuSign/Adobe Sign completion certificates | Life of agreement + 10 years | ISMS Evidence Library |
| **Signatory List** | Current list with signature dates | Current | This workbook |
| **Renewal Records** | Renewal correspondence and approvals | 7 years | ISMS Evidence Library |
| **Termination Records** | Evidence of post-term notification | 7 years | ISMS Evidence Library |

### Evidence Collection Process

#### For New NDAs:

1. Obtain signed original (scan if wet signature)
2. Export signature certificate (if e-signature)
3. Create NDA record in Active_NDAs
4. Create signatory records in Signatory_Register
5. Store evidence with standard naming convention
6. Link in Evidence_Register

#### For Renewals:

1. Complete renewal workflow documentation
2. Obtain new signed agreement
3. Create new NDA record (link to original)
4. Update original NDA status to "Renewed"
5. Update signatory records if needed
6. Store evidence

### Evidence Storage Standards

**Naming Convention:**
```
NDA-EXE-YYYY-XXXX_[Counterparty]_[Type]_[YYYYMMDD].[ext]
```

**Examples:**
- `NDA-EXE-2026-0042_Acme_Corp_Mutual_NDA_20260115.pdf`
- `NDA-EXE-2026-0042_Signature_Certificate_20260115.pdf`
- `NDA-EXE-2026-0042_Renewal_Email_20260115.msg`

**Storage Structure:**
```
Document Repository/
└── Legal/
    └── Executed NDAs/
        ├── 2026/
        │   ├── Employees/
        │   ├── Contractors/
        │   ├── Vendors/
        │   └── Partners/
        └── Archive/
            └── [Prior years]
```

---

## Common Pitfalls

Avoid these common mistakes when tracking NDA execution:

### Timing Pitfalls

❌ **MISTAKE**: Granting access before NDA is fully executed
✅ **CORRECT**: Verify NDA execution before any access provisioning; implement workflow integration with identity management; require NDA confirmation in access request process

❌ **MISTAKE**: Recording NDA execution date as when sent, not when signed
✅ **CORRECT**: Execution date is when last required signature is obtained; track each party's signature date separately in Signatory_Register

❌ **MISTAKE**: Starting work while NDA is "in progress"
✅ **CORRECT**: No access to confidential information until NDA status is "Active"; document exceptions with CISO approval and compensating controls

### Tracking Pitfalls

❌ **MISTAKE**: NDAs stored in personal folders or email
✅ **CORRECT**: Centralised, secure, backed-up storage with controlled access; consistent naming convention; storage location recorded in Active_NDAs

❌ **MISTAKE**: No tracking of individual signatories, only company NDAs
✅ **CORRECT**: Track every individual bound by confidentiality; create Signatory_Register record for each person; update when individuals join or leave

❌ **MISTAKE**: Not tracking post-termination obligations
✅ **CORRECT**: Calculate and record Post_Term_Expiry date; maintain records until all obligations expire; include in offboarding process

❌ **MISTAKE**: Terminated signatories deleted from tracking
✅ **CORRECT**: Never delete signatory records; update status to "Terminated"; maintain for post-term period; archive after full expiry

### Expiration Pitfalls

❌ **MISTAKE**: Expiration dates not monitored
✅ **CORRECT**: Weekly review of Expiration_Monitor; automated alerts at 90, 60, 30 days; assign renewal owners for all expiring NDAs

❌ **MISTAKE**: Renewal started too late (inside 30 days)
✅ **CORRECT**: Initiate renewal assessment at 90 days; allow time for legal review and negotiation; escalate if not progressing

❌ **MISTAKE**: Allowing NDAs to expire without action
✅ **CORRECT**: Every expiring NDA must have a decision (renew, terminate, or documented acceptance of gap); no silent expiration

❌ **MISTAKE**: Renewed NDAs not linked to originals
✅ **CORRECT**: Record Original_NDA reference in Renewal_Tracking; update original NDA status to "Renewed"; maintain audit trail

### Process Integration Pitfalls

❌ **MISTAKE**: NDA tracking disconnected from HR onboarding
✅ **CORRECT**: Integrate NDA execution into employee onboarding checklist; block system access provisioning until NDA confirmed; HR verifies before day one

❌ **MISTAKE**: Vendor onboarding bypasses NDA requirements
✅ **CORRECT**: Procurement process includes NDA verification step; no purchase order without NDA confirmation; vendor portal requires NDA status

❌ **MISTAKE**: Project teams create their own ad-hoc NDAs
✅ **CORRECT**: All NDAs must use approved templates; custom agreements require legal approval; register all NDAs centrally regardless of origin

❌ **MISTAKE**: No integration with access management
✅ **CORRECT**: Access provisioning requires NDA verification; periodic access reviews check NDA status; terminated signatory triggers access review

### Evidence Pitfalls

❌ **MISTAKE**: Only storing scanned signature page, not full agreement
✅ **CORRECT**: Store complete signed agreement; signature page alone may not be enforceable; include all pages, schedules, and attachments

❌ **MISTAKE**: E-signature certificates not retained
✅ **CORRECT**: Export and store completion certificates; certificate proves who signed, when, and with what verification; required for enforcement

❌ **MISTAKE**: Evidence scattered across multiple systems
✅ **CORRECT**: Consolidated evidence repository; consistent naming and structure; cross-reference in Evidence_Register

---

## Quality Checklist

Before submitting the completed assessment, verify all items:

### Active_NDAs Completeness

- [ ] All known executed NDAs registered
- [ ] Every NDA has unique NDA_ID
- [ ] Template reference verified or marked "CUSTOM"
- [ ] Execution dates verified against signed documents
- [ ] Expiration dates calculated correctly
- [ ] Post-term periods documented
- [ ] Storage locations verified accessible
- [ ] Status is current for all NDAs
- [ ] Renewal owners assigned for expiring NDAs

### Signatory_Register Completeness

- [ ] Every person with confidential access has signatory record
- [ ] All signatories linked to valid NDA
- [ ] Signature dates verified against evidence
- [ ] Relationship dates accurate (start and end)
- [ ] Status is current for all signatories
- [ ] Terminated signatories have end date recorded

### Expiration Management

- [ ] Expiration_Monitor current (no stale data)
- [ ] Alert statuses displaying correctly
- [ ] All Red/Amber NDAs have assigned actions
- [ ] Renewal tracking initiated for expiring NDAs
- [ ] No unexplained gaps in NDA coverage

### Evidence Quality

- [ ] Signed NDA evidence available for all Active NDAs
- [ ] E-signature certificates retained where applicable
- [ ] Evidence naming convention followed
- [ ] Storage locations documented and verified
- [ ] Evidence is readable and complete

### Process Integration

- [ ] HR confirmed employee NDA coverage
- [ ] Procurement confirmed vendor NDA coverage
- [ ] Partnership team confirmed partner NDA coverage
- [ ] No access without NDA verification

---

## Review and Approval

### Review Process

The completed NDA Execution and Tracking assessment must follow this review process:

#### Step 1: Self-Review by Assessor

- Complete Quality Checklist (Section 1.11)
- Verify all sheets are complete
- Spot-check signature dates against evidence
- Confirm no obvious gaps in coverage

#### Step 2: Technical Review by ISMS Administrator

**Reviewer:** ISMS Administrator
**Timeframe:** Within 5 business days

**Review scope:**
- Data completeness and accuracy
- Cross-references between sheets
- Evidence availability verification
- Calculation validation

#### Step 3: Stakeholder Review

**Reviewers:** HR Manager, Procurement Manager (as applicable)
**Timeframe:** Within 5 business days

**Review scope:**
- Completeness of their stakeholder categories
- Accuracy of signatory information
- Confirmation of relationship dates

#### Step 4: Final Approval by Information Security Manager

**Approver:** Information Security Manager
**Timeframe:** Within 5 business days

**Approval scope:**
- Overall assessment quality
- Gap identification and remediation plans
- Risk acceptance for any identified issues

### Approval Workflow

```
Assessor Completes
        │
        ▼
Self-Review (Checklist)
        │
        ▼
ISMS Administrator Review ──► Return for Corrections
        │                            │
        ▼                            │
HR/Procurement Review ───────► Return for Corrections
        │                            │
        ▼                            │
ISM Final Approval ──────────────────┘
        │
        ▼
   Assessment Complete
```

---

## Integration with HR and Procurement

### HR Integration

NDA execution must be integrated with HR processes:

#### Employee Onboarding

| Stage | NDA Action | Responsible |
|-------|------------|-------------|
| Offer Acceptance | Include NDA with offer letter | HR |
| Pre-Start | Verify NDA returned signed | HR |
| Day One | Confirm NDA in Active_NDAs | ISMS Admin |
| Access Request | Verify NDA before provisioning | IAM Team |

#### Employee Offboarding

| Stage | NDA Action | Responsible |
|-------|------------|-------------|
| Resignation/Termination | Update Signatory_Register | HR |
| Exit Interview | Remind of ongoing confidentiality | HR |
| System Access Removal | Verify access revoked | IAM Team |
| Post-Term | Track obligation period | ISMS Admin |

### Procurement Integration

NDA execution must be integrated with procurement processes:

#### Vendor Onboarding

| Stage | NDA Action | Responsible |
|-------|------------|-------------|
| Vendor Selection | Initiate NDA process | Procurement |
| NDA Negotiation | Legal review if needed | Legal |
| NDA Execution | Register in Active_NDAs | Procurement |
| Contract Award | Verify NDA status | Procurement |
| Individual Access | Create Signatory records | Contract Mgr |

#### Vendor Offboarding

| Stage | NDA Action | Responsible |
|-------|------------|-------------|
| Contract End | Update NDA status | Procurement |
| Access Removal | Verify all vendor personnel removed | IAM Team |
| Post-Term | Track obligation period | ISMS Admin |

---

## Related Controls

### Primary Control Relationships

| Control | Relationship | Integration Point |
|---------|--------------|-------------------|
| **A.6.6.1** | Template Registry | Templates used for execution |
| **A.6.6.3** | NDA Compliance | Compliance monitoring of executed NDAs |
| **A.6.1** | Screening | Background checks precede NDA |
| **A.6.2** | Terms of Employment | Employment NDAs in onboarding |
| **A.6.5** | Termination | Offboarding includes NDA reminder |
| **A.5.15** | Access Control | NDA verification before access |
| **A.5.18** | Access Rights | Periodic review includes NDA status |

### Control Integration Flow

```
Hiring Process:
A.6.1 Screening → A.6.6.2 NDA Execution → A.6.2 Employment → A.5.15 Access

Termination Process:
A.6.5 Termination → A.6.6.2 Update Status → A.5.18 Revoke Access

Vendor Process:
Procurement → A.6.6.2 NDA Execution → A.5.15 Vendor Access → Contract
```

---

**END OF USER GUIDE**

---

*"Words have weight; a signed agreement has the weight of law."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
