# ISMS-IMP-A.5.37.1 — Procedure Inventory Assessment

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.1 |
| **Title** | Procedure Inventory Assessment |
| **Control Reference** | ISO/IEC 27001:2022 A.5.37 |
| **Control Name** | Documented Operating Procedures |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |
| **Framework Version** | 1.0 |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Procedure Categories](#14-procedure-categories)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 Procedure Identification Methods](#17-procedure-identification-methods)
   - [1.8 Accessibility Requirements](#18-accessibility-requirements)
   - [1.9 Evidence Collection](#19-evidence-collection)
   - [1.10 Common Pitfalls](#110-common-pitfalls)
   - [1.11 Quality Checklist](#111-quality-checklist)
   - [1.12 Review and Approval](#112-review-and-approval)
   - [1.13 Integration with Other Controls](#113-integration-with-other-controls)
   - [1.14 Related Controls](#114-related-controls)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Architecture](#21-workbook-architecture)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Data Validations](#23-data-validations)
   - [2.4 Conditional Formatting](#24-conditional-formatting)
   - [2.5 Formula Specifications](#25-formula-specifications)
   - [2.6 Cell Styling Standards](#26-cell-styling-standards)
   - [2.7 Generator Script Reference](#27-generator-script-reference)

---

# PART I: USER COMPLETION GUIDE

---

## 1.1 Assessment Overview

### Purpose

This workbook enables systematic inventory and assessment of all documented operating procedures across the organisation's information processing facilities. It serves as the authoritative registry for:

- **Procedure Catalogue**: Complete inventory of all documented operating procedures
- **Ownership Tracking**: Clear accountability for procedure maintenance and currency
- **Accessibility Verification**: Evidence that procedures are available to personnel who need them
- **Currency Monitoring**: Tracking of review dates and approval status
- **Gap Identification**: Systematic identification of missing or inadequate procedures
- **Compliance Evidence**: Audit-ready documentation demonstrating Control A.5.37 compliance

The Procedure Inventory Assessment is foundational to the organisation's operational documentation programme. Without a controlled, centrally-managed procedure inventory, the organisation cannot demonstrate that operating procedures are documented, accessible, and current as required by ISO 27001:2022.

### Scope

This assessment covers the following components:

**In Scope:**
- All documented operating procedures for information processing facilities
- IT system operational procedures (backup, recovery, monitoring, maintenance)
- Security-specific operational procedures (incident response, access review)
- Physical facility operational procedures (HVAC, access controls, alarms)
- Change management procedures (CAB process, emergency change)
- Recovery operations procedures (DR activation, failover, restoration)
- User management procedures (onboarding, offboarding, access provisioning)
- Supplier and third-party operational procedures
- Procedure ownership and accountability documentation
- Accessibility and distribution mechanisms
- Review cycles and approval records
- Version control and change history

**Out of Scope:**
- Policy documents (covered by A.5.1 Information Security Policies)
- Standards and guidelines (separate documentation type)
- Procedure quality assessment (covered in ISMS-IMP-A.5.37.2)
- Review and update tracking (covered in ISMS-IMP-A.5.37.3)
- Compliance dashboards and metrics (covered in ISMS-IMP-A.5.37.4)
- Project-specific documentation
- End-user application guides (unless security-relevant)

### Business Value

A well-maintained procedure inventory delivers:

| Value Area | Benefit |
|------------|---------|
| **Operational Consistency** | Standardised execution of critical operations |
| **Knowledge Retention** | Documented procedures survive personnel changes |
| **Training Efficiency** | Clear procedures accelerate staff onboarding |
| **Audit Readiness** | Immediate access to procedure documentation for auditors |
| **Risk Reduction** | Eliminates reliance on undocumented tribal knowledge |
| **Regulatory Compliance** | Demonstrates systematic approach to operations |
| **Incident Response** | Clear procedures enable faster, more effective response |

### Assessment Frequency

| Activity | Frequency | Responsible Party |
|----------|-----------|-------------------|
| Inventory Review | Quarterly | ISMS Administrator |
| New Procedure Registration | Within 24 hours of creation | Procedure Owner |
| Currency Status Check | Monthly | ISMS Administrator |
| Full Inventory Assessment | Annual | Information Security Manager |
| Gap Analysis | Semi-annual | Information Security Manager |

---

## 1.2 Control Requirements

### ISO 27001:2022 Control A.5.37

> *"Operating procedures for information processing facilities should be documented and made available to personnel who need them."*

**Control Type:** Preventive
**Security Properties:** Confidentiality, Integrity, Availability
**Cybersecurity Concepts:** Protect
**Operational Capabilities:** Asset Management, Operations Security

### Implementation Requirements

Control A.5.37 requires organisations to establish a systematic approach to documenting operating procedures. The key requirements are:

**1. Documentation**
- Operating procedures must be documented in writing
- Documentation must be sufficient for personnel to execute procedures correctly
- Procedures must be version-controlled
- Changes must be formally approved before implementation

**2. Availability**
- Procedures must be accessible to personnel who need them
- Access mechanisms must be defined and verified
- Procedures must be findable when needed
- Availability must not be dependent on specific individuals

**3. Currency**
- Procedures must be regularly reviewed for accuracy
- Updates must be made when systems or processes change
- Review cycles must be defined and adhered to
- Outdated procedures must be updated or retired

**4. Completeness**
- All information processing facilities must have documented procedures
- Critical operations must not rely on undocumented processes
- Gaps must be identified and remediated

### What Auditors Look For

ISO 27001 auditors examining Control A.5.37 will verify:

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Procedure Existence** | Documented procedures for all information processing facilities |
| **Inventory Completeness** | Comprehensive catalogue of all operating procedures |
| **Accessibility** | Evidence that personnel can access required procedures |
| **Currency** | Review dates within defined cycles, approval records |
| **Version Control** | Version history and change documentation |
| **Ownership** | Clear accountability for each procedure |
| **Coverage** | No gaps in critical operational areas |

### Common Audit Questions

Auditors frequently ask:

1. *"Show me the procedure for [specific operation, e.g., backup, incident response]."*
2. *"How do personnel access operating procedures?"*
3. *"When was this procedure last reviewed and by whom?"*
4. *"How do you ensure procedures are updated when systems change?"*
5. *"What is your inventory of all operating procedures?"*
6. *"How do you identify gaps in procedure documentation?"*

---

## 1.3 Prerequisites

### Before Starting This Assessment

Complete the following prerequisites to ensure successful assessment completion:

#### Required Access

| System/Resource | Access Level | Purpose |
|-----------------|--------------|---------|
| Document Management System | Read/Write | Access to procedure documents |
| ISMS Evidence Library | Write | Upload evidence and completed workbook |
| SharePoint/Confluence | Read | Verify procedure storage locations |
| IT Service Management System | Read | Identify operational procedures |
| HR Information System | Read | Verify department and role information |

#### Required Information

| Information | Source | Why Needed |
|-------------|--------|------------|
| Organisational structure | HR | Map procedures to departments |
| IT system inventory | IT Operations | Identify systems requiring procedures |
| Previous procedure audits | ISMS Evidence Library | Understand existing state |
| Department contacts | HR/Department Heads | Coordinate procedure discovery |
| Document repository structure | IT/DMS Admin | Understand storage locations |
| Role definitions | HR | Map accessibility requirements |

#### Required Approvals

| Approval | Approver | When Needed |
|----------|----------|-------------|
| Access to procedure repositories | Document Owner/IT | Before starting |
| Permission to interview process owners | Department Heads | During discovery |
| Authority to register procedures | CISO | Before populating inventory |
| Assessment scope confirmation | Information Security Manager | Before starting |

#### Prerequisite Checklist

Before proceeding, verify:

- [ ] Access to document management system confirmed
- [ ] Department contacts identified and available
- [ ] Organisational structure documentation available
- [ ] IT system inventory accessible
- [ ] Previous assessments reviewed (if any)
- [ ] Document storage locations identified
- [ ] Role definitions and access groups available
- [ ] Assessment scope approved by ISM

---

## 1.4 Procedure Categories

### Understanding Procedure Categories

Operating procedures must be categorised for effective management and gap analysis. The table below provides guidance on procedure categorisation:

#### Category Definitions

| Category | Description | Example Procedures |
|----------|-------------|-------------------|
| **System Operations** | Day-to-day IT system operations | Backup execution, system restart, monitoring response |
| **Security Operations** | Security-specific operational procedures | Incident response, access review, vulnerability scanning |
| **Facility Operations** | Physical facility procedures | HVAC management, physical access, fire suppression |
| **Change Management** | Change control procedures | CAB process, emergency change, release management |
| **Recovery Operations** | Business continuity and DR procedures | DR activation, failover, restoration, BCP testing |
| **User Management** | Identity lifecycle procedures | Onboarding, offboarding, access provisioning |
| **Network Operations** | Network infrastructure procedures | Firewall management, router configuration, network monitoring |
| **Database Operations** | Database management procedures | Database backup, replication, maintenance windows |
| **Application Operations** | Application-specific procedures | Application restart, batch job management, log rotation |

#### Procedure Category Matrix

| Category | Examples | Typical Owner | Criticality |
|----------|----------|---------------|-------------|
| System Operations | System start/stop, monitoring alerts | IT Operations | High |
| Security Operations | Incident handling, log review | Security Team | Critical |
| Facility Operations | Access control, environmental | Facilities | Medium-High |
| Change Management | RFC process, rollback | IT Service Management | High |
| Recovery Operations | DR runbooks, restoration | IT Operations/DR Team | Critical |
| User Management | Joiner/Mover/Leaver | IT/HR | High |
| Network Operations | Firewall rules, VPN | Network Team | High |
| Database Operations | Backup verification, failover | DBA Team | Critical |
| Application Operations | Release deployment, healthchecks | Application Teams | Medium-High |

#### Procedure Criticality Assessment

| Criticality Level | Definition | Review Cycle | Approval Level |
|-------------------|------------|--------------|----------------|
| **Critical** | Failure impacts business continuity or security | 6 months | Management |
| **High** | Significant operational impact if missing | 12 months | Team Lead |
| **Medium** | Moderate impact, workarounds available | 12 months | Team Lead |
| **Low** | Minor operational procedures | 24 months | Team Lead |

---

## 1.5 Workbook Structure

### Sheet Overview

The workbook consists of seven sheets, each serving a specific purpose in procedure inventory management:

| Sheet | Purpose | Primary User | Update Frequency |
|-------|---------|--------------|------------------|
| **Instructions** | Guidance and orientation | All users | As needed |
| **Procedure_Inventory** | Master catalogue of procedures | ISM/Procedure Owners | Upon change |
| **Required_Procedures** | Reference list for compliance | ISM | Annual |
| **Accessibility_Matrix** | Role-based access mapping | ISM | Upon change |
| **Gap_Analysis** | Gap tracking and remediation | ISM | Ongoing |
| **Evidence_Register** | Evidence tracking and links | ISM | Ongoing |
| **Approval_SignOff** | Assessment authorisation | Approvers | At completion |

### Sheet Relationships

```
┌─────────────────┐
│  Instructions   │ ◄── Start here
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│Procedure_       │────►│Required_        │
│Inventory        │     │Procedures       │
└────────┬────────┘     └─────────────────┘
         │                      ▲
         │                      │ (gap comparison)
         ▼                      │
┌─────────────────┐     ┌─────────────────┐
│Accessibility_   │     │  Gap_Analysis   │
│Matrix           │     │                 │
└────────┬────────┘     └─────────────────┘
         │
         ▼
┌─────────────────┐
│Evidence_Register│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Approval_SignOff│ ◄── Complete here
└─────────────────┘
```

### Sheet-by-Sheet Summary

#### 1. Instructions Sheet

Provides orientation including:
- Document purpose and scope
- Sheet navigation guide
- Completion timeline
- Contact information for queries
- Version history of the workbook

#### 2. Procedure_Inventory Sheet

The master registry containing:
- Unique procedure identifiers
- Procedure names and descriptions
- Category classifications
- Ownership information
- Document locations
- Review dates and cycles
- Approval status and history
- Related ISO 27001 controls
- Criticality ratings

#### 3. Required_Procedures Sheet

Reference list containing:
- ISO 27001-required procedures
- Industry best practice procedures
- Regulatory-required procedures
- Mapping to Procedure_Inventory
- Gap status indicators

#### 4. Accessibility_Matrix Sheet

Access mapping containing:
- Procedure to role mappings
- Access method documentation
- Verification dates
- Distribution channels

#### 5. Gap_Analysis Sheet

Gap tracking containing:
- Gap identifiers
- Gap types and descriptions
- Severity ratings
- Remediation assignments
- Target dates and status
- Evidence of closure

#### 6. Evidence_Register Sheet

Evidence tracking:
- Evidence identifiers
- Evidence descriptions
- Evidence types
- Storage locations
- Collection dates
- Validity periods

#### 7. Approval_SignOff Sheet

Assessment authorisation:
- Assessor information
- Assessment dates
- Reviewer sign-offs
- Approval status
- Comments and notes

---

## 1.6 Completion Walkthrough

### Step 1: Review Instructions Sheet

**Time allocation:** 10-15 minutes

1. Read the document purpose and scope section
2. Note the contact information for queries
3. Review the completion timeline
4. Understand the sheet navigation sequence
5. Check workbook version matches this specification

### Step 2: Complete Procedure_Inventory Sheet

**Time allocation:** 4-8 hours (depending on organisation size)

For each operating procedure, complete the following fields:

#### Column A: Procedure_ID

- **Format:** SOP-[DEPT]-NNN (where DEPT is department code, NNN is sequential)
- **Example:** SOP-IT-001, SOP-SEC-015, SOP-FAC-003
- **Rules:** Must be unique, do not reuse IDs for retired procedures
- **Guidance:** Use consistent department codes across organisation

#### Column B: Procedure_Name

- **Format:** Descriptive name reflecting purpose
- **Example:** Daily Backup Execution Procedure
- **Rules:** Maximum 100 characters, use title case
- **Guidance:** Name should clearly indicate what the procedure covers

#### Column C: Category

- **Format:** Select from dropdown validation list
- **Options:**
  - System Operations
  - Security Operations
  - Facility Operations
  - Change Management
  - Recovery Operations
  - User Management
  - Network Operations
  - Database Operations
  - Application Operations
  - Other
- **Guidance:** Select the category that best describes the procedure's purpose

#### Column D: Process_Owner

- **Format:** Full name or role title
- **Example:** IT Operations Manager, John Smith
- **Rules:** Must be an identifiable person or role
- **Guidance:** Owner is accountable for procedure currency and accuracy

#### Column E: Department

- **Format:** Department name
- **Example:** IT Operations, Information Security, Facilities
- **Rules:** Use standard organisational department names
- **Guidance:** Should match HR organisational structure

#### Column F: Document_Location

- **Format:** Full path or URL
- **Example:** SharePoint/IT/Procedures/SOP-IT-001.docx
- **Rules:** Must be a verifiable, accessible location
- **Guidance:** Use persistent URLs or document IDs where possible

#### Column G: Last_Review_Date

- **Format:** DD.MM.YYYY (Swiss date format)
- **Example:** 15.01.2026
- **Rules:** Must be a valid date, not future-dated
- **Guidance:** Date of most recent formal review

#### Column H: Next_Review_Due

- **Format:** DD.MM.YYYY (Swiss date format)
- **Example:** 15.01.2027
- **Rules:** Calculated from Last_Review_Date + Review_Cycle_Days
- **Guidance:** Auto-calculated field

#### Column I: Review_Cycle_Days

- **Format:** Number (days)
- **Example:** 365 (annual), 180 (semi-annual)
- **Rules:** Must be positive integer
- **Guidance:** Critical procedures should have shorter cycles (180 days)

#### Column J: Version

- **Format:** X.Y (major.minor)
- **Example:** 2.1
- **Rules:** Increment minor for small changes, major for significant revisions
- **Guidance:** Version 1.0 is the initial approved version

#### Column K: Approval_Status

- **Format:** Select from dropdown validation list
- **Options:**
  - Draft – Under development
  - Pending Approval – Submitted for approval
  - Approved – Formally approved and current
  - Expired – Past review date, needs update
  - Under Review – Being revised
  - Retired – No longer in use
- **Guidance:** Only "Approved" procedures should be used for operations

#### Column L: Approver

- **Format:** Full name and role
- **Example:** Jane Doe, IT Director
- **Rules:** Required when Approval_Status is "Approved"
- **Guidance:** Must be appropriate authority level for procedure criticality

#### Column M: Approval_Date

- **Format:** DD.MM.YYYY (Swiss date format)
- **Example:** 10.01.2026
- **Rules:** Required when Approval_Status is "Approved"
- **Guidance:** Must be on or before Last_Review_Date

#### Column N: Related_Controls

- **Format:** Comma-separated control references
- **Example:** A.8.13, A.8.16, A.5.37
- **Rules:** Must be valid ISO 27001:2022 control references
- **Guidance:** Link to all controls this procedure supports

#### Column O: Criticality

- **Format:** Select from dropdown validation list
- **Options:**
  - Critical – Business continuity/security impact
  - High – Significant operational impact
  - Medium – Moderate impact, workarounds exist
  - Low – Minor operational impact
- **Guidance:** Base on business impact if procedure is unavailable

#### Column P: Notes

- **Format:** Free text
- **Example:** Revised for new backup system in January 2026
- **Rules:** Maximum 500 characters
- **Guidance:** Include any special considerations or context

### Step 3: Complete Required_Procedures Sheet

**Time allocation:** 2-3 hours

Cross-reference against ISO 27001 requirements and best practices:

1. Review the pre-populated list of required procedures
2. For each required procedure, check if it exists in Procedure_Inventory
3. Update the Current_Status field (Exists/Partial/Missing)
4. Link to Procedure_Inventory via Mapped_Procedure_ID
5. Document gaps in Gap_Notes field

### Step 4: Complete Accessibility_Matrix Sheet

**Time allocation:** 1-2 hours

For each procedure, verify accessibility:

1. List all roles that should have access
2. Verify each role can actually access the procedure
3. Document the access method (SharePoint, intranet, etc.)
4. Record verification date
5. Flag any access issues as gaps

### Step 5: Complete Gap_Analysis Sheet

**Time allocation:** 1-2 hours

Document all identified gaps:

1. Generate Gap_ID using format GAP-A.5.37.1-NNN
2. Classify gap type (Missing/Incomplete/Outdated/Unapproved/Inaccessible)
3. Assign severity based on criticality
4. Identify remediation owner
5. Set target date per severity SLA
6. Track status through to closure

### Step 6: Complete Evidence_Register Sheet

**Time allocation:** 30-60 minutes

Document all supporting evidence:

1. Generate Evidence_ID using format EVD-A.5.37.1-NNN
2. Describe what evidence demonstrates
3. Record storage location
4. Note collection date and collector
5. Set validity period

### Step 7: Complete Approval_SignOff Sheet

**Time allocation:** 15-30 minutes

Obtain required authorisations:

1. Complete assessor information
2. Enter assessment completion date
3. Route to reviewers for sign-off
4. Obtain final approval from ISM

---

## 1.7 Procedure Identification Methods

### Discovery Approaches

#### Interview-Based Discovery

Conduct structured interviews with:

| Stakeholder | Focus Areas | Questions to Ask |
|-------------|-------------|------------------|
| IT Operations Manager | System procedures | What procedures do your team follow daily? |
| Security Team Lead | Security procedures | What runbooks exist for incident response? |
| Facilities Manager | Physical procedures | What operational procedures exist for the data centre? |
| HR Manager | User management | What procedures govern employee onboarding/offboarding? |
| IT Service Manager | Change management | What ITIL procedures are documented? |

#### Document Repository Mining

Search document management systems for:

- Files containing "procedure", "SOP", "runbook", "work instruction"
- Documents in /Procedures/, /Operations/, /Runbooks/ folders
- Documents with naming patterns like SOP-*, PROC-*, WI-*
- Recent modifications in operational folders

#### System-Based Discovery

Identify procedures from:

- IT Service Management tickets referencing procedures
- Automated job schedules requiring manual fallback
- Monitoring alerts with escalation procedures
- Change management records
- Incident post-mortems referencing procedures

### Validation Checklist

For each discovered procedure, verify:

- [ ] Document exists and is accessible
- [ ] Document is clearly a procedure (not policy, guideline, or template)
- [ ] Procedure is relevant to information processing facilities
- [ ] Procedure has identifiable ownership
- [ ] Procedure has version information
- [ ] Procedure has been reviewed within its cycle

---

## 1.8 Accessibility Requirements

### Accessibility Verification

Personnel must be able to access procedures they need. Verify accessibility through:

#### Access Method Documentation

| Access Method | Verification Approach | Evidence Required |
|---------------|----------------------|-------------------|
| SharePoint | Confirm user permissions | Permission report, user test |
| Confluence | Verify space access | Space permissions, user test |
| Network Share | Check folder permissions | ACL report, user test |
| Printed Manual | Confirm physical availability | Location verification |
| ITSM Knowledge Base | Verify role-based access | KB permissions |

#### Role-Based Access Requirements

| Role | Typical Procedure Access | Verification |
|------|-------------------------|--------------|
| IT Operations | System, Network, Database procedures | Permission check |
| Security Team | Security procedures, Incident response | Permission check |
| Help Desk | User management, Basic troubleshooting | Permission check |
| Facilities | Facility operations procedures | Physical + system check |
| Management | All procedures (read access) | Permission check |

### Accessibility Issues

Common accessibility problems:

| Issue | Impact | Resolution |
|-------|--------|------------|
| Broken links | Procedure unavailable | Update document location |
| Permission denied | User cannot access | Grant appropriate permissions |
| Outdated version | Wrong procedure followed | Implement version control |
| Offline unavailable | Procedure unavailable during outage | Provide offline copies |
| Language barrier | Procedure misunderstood | Translate or simplify |

---

## 1.9 Evidence Collection

### Evidence Requirements

The following evidence must be collected and maintained to demonstrate compliance with Control A.5.37:

| Evidence Type | Description | Retention Period | Storage Location |
|---------------|-------------|------------------|------------------|
| **Procedure Documents** | All documented procedures | Life of procedure + 7 years | ISMS Evidence Library |
| **Inventory Workbook** | Completed assessment workbook | 3 assessment cycles | ISMS Evidence Library |
| **Access Verification** | Permission reports, test results | 3 years | ISMS Evidence Library |
| **Approval Records** | Signed approval evidence | 7 years | ISMS Evidence Library |
| **Gap Remediation** | Evidence of gap closure | 7 years | ISMS Evidence Library |
| **Review Records** | Procedure review documentation | 7 years | ISMS Evidence Library |

### Evidence Collection Process

#### Step 1: Gather Procedure Documents

1. Export list of all procedures from document management
2. Verify each document is accessible
3. Capture version information
4. Store copies in ISMS Evidence Library with date stamp

#### Step 2: Collect Access Verification

1. Export permission reports from document repositories
2. Document user access tests performed
3. Record any access issues identified
4. Store evidence with assessment

#### Step 3: Document Approval Records

1. Collect approval emails or signed forms
2. Link approvals to specific procedure versions
3. Store in ISMS Evidence Library

### Evidence Storage Standards

**Naming Convention:**
```
EVD-A.5.37.1_[EvidenceType]_[Reference]_[YYYYMMDD].[ext]
```

**Examples:**
- `EVD-A.5.37.1_Inventory_Complete_20260115.xlsx`
- `EVD-A.5.37.1_AccessVerification_IT-Ops_20260115.pdf`
- `EVD-A.5.37.1_Approval_SOP-IT-001_20260115.pdf`

**Storage Structure:**
```
ISMS Evidence Library/
└── A.5.37-Documented-Procedures/
    ├── Inventories/
    │   └── [Assessment period]/
    ├── Procedures/
    │   ├── System-Operations/
    │   ├── Security-Operations/
    │   └── [Other categories]/
    ├── Access-Verification/
    ├── Approvals/
    └── Gap-Remediation/
```

---

## 1.10 Common Pitfalls

Avoid these common mistakes when completing the Procedure Inventory assessment:

### Inventory Completeness Pitfalls

❌ **MISTAKE**: Only inventorying IT procedures, ignoring security and facilities
✅ **CORRECT**: Include ALL operating procedures for information processing facilities including physical security, access control, environmental controls, and emergency procedures

❌ **MISTAKE**: Treating policies as procedures and including them in inventory
✅ **CORRECT**: Distinguish between policies (what to do) and procedures (how to do it); only inventory procedures in this workbook; policies belong in A.5.1 documentation

❌ **MISTAKE**: Missing informal or tribal knowledge procedures
✅ **CORRECT**: Interview operational staff to identify undocumented processes that should be procedures; capture even informal "how we do things" as potential gaps

❌ **MISTAKE**: Not including third-party/supplier operational procedures
✅ **CORRECT**: Inventory procedures for managed services, outsourced operations, and cloud services that affect your information processing; request procedure documentation from suppliers

### Ownership and Accountability Pitfalls

❌ **MISTAKE**: Assigning procedure ownership to generic groups (e.g., "IT")
✅ **CORRECT**: Assign ownership to specific individuals or defined roles; ownership requires accountability for currency and accuracy

❌ **MISTAKE**: No ownership for procedures inherited from predecessor organisations
✅ **CORRECT**: Assign ownership to all procedures regardless of origin; inherited procedures without owners must have ownership assigned before inventory completion

❌ **MISTAKE**: Procedure owner is person who created it, not person responsible for it
✅ **CORRECT**: Owner should be the person with ongoing accountability for the procedure's accuracy and relevance, not necessarily the original author

### Currency and Review Pitfalls

❌ **MISTAKE**: Recording creation date as review date
✅ **CORRECT**: Review date is when procedure was formally reviewed for accuracy and currency, not when it was created; procedures may have been created years ago but recently reviewed

❌ **MISTAKE**: Not setting review cycles based on criticality
✅ **CORRECT**: Critical procedures should have shorter review cycles (6 months); standard procedures can be annual; low-criticality can be 24 months; document rationale for cycle selection

❌ **MISTAKE**: Approving procedures without actual review
✅ **CORRECT**: Approval must follow genuine review of procedure content; rubber-stamp approvals create compliance risk and audit findings

❌ **MISTAKE**: Not updating review date when systems change
✅ **CORRECT**: Procedures must be reviewed when underlying systems or processes change, regardless of scheduled review date; maintain change-triggered review process

### Accessibility Pitfalls

❌ **MISTAKE**: Assuming SharePoint access equals procedure access
✅ **CORRECT**: Verify actual accessibility by testing that relevant roles can open and read the specific documents; permission inheritance issues often block access

❌ **MISTAKE**: No offline access to critical procedures
✅ **CORRECT**: Ensure critical procedures (incident response, DR) are accessible during system outages; maintain printed copies or offline documentation where needed

❌ **MISTAKE**: Not verifying accessibility after repository migrations
✅ **CORRECT**: After any document system migration, verify all procedure links are valid and permissions are correct; broken links are common post-migration

### Documentation Quality Pitfalls

❌ **MISTAKE**: Procedures that only exist in individual inboxes or local drives
✅ **CORRECT**: All procedures must be in centrally managed, backed-up, access-controlled locations; personal storage is not acceptable for operational procedures

❌ **MISTAKE**: Multiple versions of the same procedure in different locations
✅ **CORRECT**: Establish single authoritative location for each procedure; delete or clearly mark any copies as "reference only"; implement document management controls

❌ **MISTAKE**: Not capturing version history
✅ **CORRECT**: Maintain version history for all procedures showing what changed, when, and who approved; enables rollback and provides audit trail

❌ **MISTAKE**: Inventory workbook not kept current
✅ **CORRECT**: Update inventory within 24 hours of procedure creation, modification, or retirement; stale inventory creates compliance gaps and operational risk

---

## 1.11 Quality Checklist

Before submitting the completed assessment, verify all items:

### Completeness Checks

- [ ] All known procedures registered in Procedure_Inventory
- [ ] Every procedure has a unique Procedure_ID
- [ ] All categories represented (System, Security, Facility, etc.)
- [ ] Procedure ownership assigned for each entry
- [ ] Document locations verified accessible
- [ ] Review dates and cycles documented
- [ ] Approval status current for all procedures

### Coverage Checks

- [ ] Required_Procedures sheet cross-referenced
- [ ] All required procedures mapped or flagged as gaps
- [ ] No critical operational areas without procedures
- [ ] Third-party/supplier procedures included

### Accessibility Checks

- [ ] Accessibility_Matrix completed for all procedures
- [ ] All relevant roles have verified access
- [ ] Access methods documented
- [ ] Accessibility issues logged as gaps

### Currency Checks

- [ ] All review dates verified against documents
- [ ] Expired procedures flagged appropriately
- [ ] Review cycles appropriate for criticality
- [ ] Approvals verified for current status

### Gap Management Checks

- [ ] All identified gaps documented in Gap_Analysis
- [ ] Gaps assigned severity ratings
- [ ] Remediation owners assigned
- [ ] Target dates set per SLA
- [ ] No overdue gaps without escalation

### Evidence Checks

- [ ] Evidence collected for all key findings
- [ ] Evidence stored in ISMS Evidence Library
- [ ] Evidence naming convention followed
- [ ] Evidence is retrievable and readable

### Approval Checks

- [ ] Assessor information complete
- [ ] Assessment date documented
- [ ] All required sign-offs obtained
- [ ] Comments addressed

---

## 1.12 Review and Approval

### Review Process

The completed Procedure Inventory assessment must follow this review process:

#### Step 1: Self-Review by Assessor

- Complete Quality Checklist (Section 1.11)
- Verify all sheets are complete
- Check for obvious errors or omissions
- Ensure evidence is properly linked

#### Step 2: Technical Review by ISMS Administrator

**Reviewer:** ISMS Administrator
**Timeframe:** Within 5 business days

**Review scope:**
- Workbook completeness and formatting
- Evidence register accuracy
- Gap analysis validation
- Cross-reference verification

**Outcome:** Approve, Return for corrections, or Escalate

#### Step 3: Department Owner Review

**Reviewers:** Department heads for relevant procedures
**Timeframe:** Within 5 business days

**Review scope:**
- Verify procedure accuracy for their department
- Confirm ownership assignments
- Validate accessibility
- Agree with gap priorities

**Outcome:** Approve or Return for corrections

#### Step 4: Final Approval by Information Security Manager

**Approver:** Information Security Manager
**Timeframe:** Within 5 business days

**Approval scope:**
- Overall assessment quality
- Gap remediation plan adequacy
- Resource allocation for gaps
- Risk acceptance

**Outcome:** Approve or Reject

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
Department Owner Review ─────► Return for Corrections
        │                            │
        ▼                            │
ISM Final Approval ──────────────────┘
        │
        ▼
   Assessment Complete
        │
        ▼
   Upload to ISMS Evidence Library
```

### Sign-Off Requirements

| Role | Signature Required | Authority |
|------|-------------------|-----------|
| Assessor | Yes | Confirms accuracy of information |
| ISMS Administrator | Yes | Confirms completeness |
| Department Owners | Yes (relevant departments) | Confirms procedure accuracy |
| Information Security Manager | Yes | Final approval |

### Post-Approval Actions

Upon approval:

1. Upload completed workbook to ISMS Evidence Library
2. Update ISMS control status to reflect assessment completion
3. Schedule next assessment (typically quarterly for inventory review)
4. Communicate any identified gaps to relevant parties
5. Initiate remediation tracking for all open gaps
6. Update related controls as needed

---

## 1.13 Integration with Other Controls

### Document Management Integration

Procedure inventory must integrate with document management systems:

| Integration Point | Purpose | Mechanism |
|-------------------|---------|-----------|
| Version Control | Track procedure versions | DMS version history |
| Access Control | Manage who can edit procedures | DMS permissions |
| Approval Workflow | Route procedures for approval | DMS workflow |
| Change Notification | Alert stakeholders to changes | DMS notifications |
| Search and Discovery | Enable procedure findability | DMS search indexing |

### ITIL/ITSM Integration

Operating procedures should align with ITIL processes:

| ITIL Process | Procedure Integration |
|--------------|----------------------|
| Change Management | Procedures for CAB, emergency changes |
| Incident Management | Incident response procedures |
| Problem Management | Root cause analysis procedures |
| Service Request | Standard operating procedures |
| Knowledge Management | Procedure repository management |

### Training Integration

Procedures must connect to training programmes:

| Training Aspect | Procedure Link |
|-----------------|----------------|
| New hire training | Relevant procedure familiarisation |
| Role-based training | Job-specific procedure training |
| Procedure changes | Update training when procedures change |
| Competency assessment | Verify procedure understanding |

---

## 1.14 Related Controls

### Primary Control Relationships

Control A.5.37 works in conjunction with these ISO 27001:2022 controls:

| Control | Relationship | Integration Point |
|---------|--------------|-------------------|
| **A.5.1** | Policies | Policies define requirements; procedures implement them |
| **A.5.2** | Roles and Responsibilities | Procedures define role-specific actions |
| **A.5.23** | Cloud Services | Cloud operational procedures required |
| **A.5.24** | Incident Management | Incident response procedures essential |
| **A.5.26** | Incident Response | Detailed response procedures |
| **A.5.29** | Business Continuity | BC/DR procedures critical |
| **A.8.6** | Capacity Management | Capacity monitoring procedures |
| **A.8.13** | Backup | Backup execution procedures |
| **A.8.14** | Redundancy | Failover procedures |
| **A.8.31** | Separation of Environments | Environment management procedures |
| **A.8.32** | Change Management | Change control procedures |

### Control Integration Flow

```
A.5.1 Policies (What to do)
        │
        ▼
A.5.37 Procedures (How to do it)
        │
        ├──► A.5.24/26 Incident Response Procedures
        ├──► A.5.29 BC/DR Procedures
        ├──► A.8.13 Backup Procedures
        ├──► A.8.32 Change Management Procedures
        └──► All operational controls
```

### Reference to Related IMPs

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-IMP-A.5.37.2 | Procedure Quality Assessment | Assesses quality of inventoried procedures |
| ISMS-IMP-A.5.37.3 | Procedure Review and Update Tracking | Tracks procedure review cycles |
| ISMS-IMP-A.5.37.4 | Compliance Dashboard | Aggregates compliance metrics |
| ISMS-IMP-A.5.1.x | Policy Management | Policies that procedures implement |
| ISMS-IMP-A.5.24.x | Incident Management | Incident response procedures |

---

# PART II: TECHNICAL SPECIFICATION

---

## 2.1 Workbook Architecture

### File Details

| Attribute | Value |
|-----------|-------|
| **Filename** | `ISMS-IMP-A.5.37.1_Procedure_Inventory_Assessment_YYYYMMDD.xlsx` |
| **Format** | Microsoft Excel Open XML (.xlsx) |
| **Sheets** | 7 |
| **Protected** | Yes (structure and formatting) |
| **Password** | [Organisation standard] |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 2 |
| 2 | Procedure_Inventory | Master catalogue | 200+ | 16 |
| 3 | Required_Procedures | Compliance reference | 50+ | 8 |
| 4 | Accessibility_Matrix | Access mapping | 200+ | 10 |
| 5 | Gap_Analysis | Gap tracking | 50+ | 10 |
| 6 | Evidence_Register | Evidence links | 50+ | 8 |
| 7 | Approval_SignOff | Authorisation | 15 | 3 |

### Workbook Properties

```python
WORKBOOK_PROPERTIES = {
    "title": "ISMS-IMP-A.5.37.1 Procedure Inventory Assessment",
    "subject": "Operating Procedure Inventory Management",
    "creator": "ISMS Generator",
    "keywords": "ISO27001, A.5.37, Procedures, Operating, Inventory",
    "category": "ISMS Assessment Workbook",
    "company": "[Organisation Name]"
}
```

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

#### Layout

| Row | Column A | Column B |
|-----|----------|----------|
| 1 | **ISMS-IMP-A.5.37.1** | |
| 2 | **Procedure Inventory Assessment** | |
| 3 | | |
| 4 | **Document Information** | |
| 5 | Control Reference | ISO/IEC 27001:2022 A.5.37 |
| 6 | Document ID | ISMS-IMP-A.5.37.1 |
| 7 | Generated Date | [Date] |
| 8 | Version | 1.0 |
| 9 | | |
| 10 | **Purpose** | |
| 11 | [Purpose text spanning both columns] | |
| ... | ... | ... |

#### Column Widths

| Column | Width (characters) |
|--------|-------------------|
| A | 25 |
| B | 80 |

### Sheet 2: Procedure_Inventory

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Procedure_ID | 15 | Text | SOP-XXX-NNN pattern |
| B | Procedure_Name | 40 | Text | Max 100 chars |
| C | Category | 20 | List | See dropdown |
| D | Process_Owner | 25 | Text | Required |
| E | Department | 20 | Text | Required |
| F | Document_Location | 50 | Text | Path/URL |
| G | Last_Review_Date | 15 | Date | DD.MM.YYYY |
| H | Next_Review_Due | 15 | Date | Calculated |
| I | Review_Cycle_Days | 12 | Number | Default 365 |
| J | Version | 10 | Text | X.Y format |
| K | Approval_Status | 15 | List | See dropdown |
| L | Approver | 25 | Text | Conditional |
| M | Approval_Date | 15 | Date | Conditional |
| N | Related_Controls | 25 | Text | Multi-value |
| O | Criticality | 12 | List | See dropdown |
| P | Notes | 50 | Text | Optional |

#### Header Row Format

```python
HEADER_FORMAT = {
    "font": Font(name='Calibri', size=11, bold=True, color='FFFFFF'),
    "fill": PatternFill(start_color='2E75B6', end_color='2E75B6', fill_type='solid'),
    "alignment": Alignment(horizontal='center', vertical='center', wrap_text=True),
    "border": Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
}
```

### Sheet 3: Required_Procedures

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Reference_ID | 15 | Text | Standard reference |
| B | Required_Procedure | 40 | Text | Procedure name |
| C | ISO_Control | 15 | Text | Control reference |
| D | Category | 20 | List | Category dropdown |
| E | Priority | 12 | List | High/Medium/Low |
| F | Current_Status | 15 | List | Exists/Partial/Missing |
| G | Mapped_Procedure_ID | 15 | Text | Link to inventory |
| H | Gap_Notes | 50 | Text | Gap description |

### Sheet 4: Accessibility_Matrix

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Procedure_ID | 15 | List | From Procedure_Inventory |
| B | IT_Operations | 10 | Boolean | Y/N |
| C | Security_Team | 10 | Boolean | Y/N |
| D | Facilities | 10 | Boolean | Y/N |
| E | Help_Desk | 10 | Boolean | Y/N |
| F | Management | 10 | Boolean | Y/N |
| G | Other_Roles | 20 | Text | Additional roles |
| H | Access_Method | 25 | Text | How accessed |
| I | Verified_Date | 15 | Date | Last verification |
| J | Issues | 30 | Text | Access issues |

### Sheet 5: Gap_Analysis

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap_ID | 20 | Text | GAP-A.5.37.1-NNN |
| B | Gap_Type | 15 | List | See dropdown |
| C | Procedure_Reference | 25 | Text | Procedure or description |
| D | Severity | 12 | List | Critical/High/Medium/Low |
| E | Identified_Date | 15 | Date | DD.MM.YYYY |
| F | Remediation_Owner | 20 | Text | Responsible party |
| G | Target_Date | 15 | Date | Deadline |
| H | Status | 15 | List | Open/In Progress/Closed |
| I | Completion_Date | 15 | Date | When resolved |
| J | Evidence | 30 | Text | Evidence reference |

### Sheet 6: Evidence_Register

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Evidence_ID | 20 | Text | EVD-A.5.37.1-NNN |
| B | Evidence_Type | 20 | List | See dropdown |
| C | Description | 40 | Text | What it demonstrates |
| D | Related_Procedure | 15 | Text | Procedure ID |
| E | Collection_Date | 15 | Date | DD.MM.YYYY |
| F | Location | 40 | Text | Storage path |
| G | Collected_By | 20 | Text | Name |
| H | Valid_Until | 15 | Date | Expiry date |

### Sheet 7: Approval_SignOff

#### Layout

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 1 | **Assessment Sign-Off** | | |
| 2 | | | |
| 3 | **Assessor Details** | | |
| 4 | Assessor Name | [Input field] | |
| 5 | Role | [Input field] | |
| 6 | Assessment Date | [Input field] | |
| 7 | | | |
| 8 | **Reviewer Sign-Off** | **Signature** | **Date** |
| 9 | ISMS Administrator | | |
| 10 | Department Owner | | |
| 11 | Information Security Manager | | |
| 12 | | | |
| 13 | **Approval Status** | | |
| 14 | Status | [Approved/Pending/Rejected] | |
| 15 | Comments | [Input field spanning columns] | |

---

## 2.3 Data Validations

### Category Dropdown

```python
CATEGORY_LIST = [
    "System Operations",
    "Security Operations",
    "Facility Operations",
    "Change Management",
    "Recovery Operations",
    "User Management",
    "Network Operations",
    "Database Operations",
    "Application Operations",
    "Other"
]
```

### Approval_Status Dropdown

```python
APPROVAL_STATUS_LIST = [
    "Draft",
    "Pending Approval",
    "Approved",
    "Expired",
    "Under Review",
    "Retired"
]
```

### Criticality Dropdown

```python
CRITICALITY_LIST = [
    "Critical",
    "High",
    "Medium",
    "Low"
]
```

### Gap_Type Dropdown

```python
GAP_TYPE_LIST = [
    "Missing",
    "Incomplete",
    "Outdated",
    "Unapproved",
    "Inaccessible",
    "Other"
]
```

### Evidence_Type Dropdown

```python
EVIDENCE_TYPE_LIST = [
    "Document",
    "Screenshot",
    "Export",
    "Attestation",
    "Meeting Minutes",
    "Other"
]
```

### Current_Status Dropdown

```python
CURRENT_STATUS_LIST = [
    "Exists",
    "Partial",
    "Missing"
]
```

---

## 2.4 Conditional Formatting

### Procedure_Inventory Sheet

#### Review Status Formatting

| Condition | Fill Colour | Font Colour |
|-----------|-------------|-------------|
| Next_Review_Due < TODAY() | Light Red (#FFC7CE) | Dark Red (#9C0006) |
| Next_Review_Due < TODAY()+30 | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Within review cycle | No fill | Default |

#### Approval Status Formatting

| Status | Fill Colour | Font Colour |
|--------|-------------|-------------|
| Approved | Light Green (#C6EFCE) | Dark Green (#006100) |
| Draft | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Pending Approval | Light Blue (#BDD7EE) | Dark Blue (#1F4E79) |
| Expired | Light Red (#FFC7CE) | Dark Red (#9C0006) |
| Under Review | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Retired | Light Grey (#D9D9D9) | Dark Grey (#595959) |

### Gap_Analysis Sheet

#### Severity Formatting

| Severity | Fill Colour | Font Colour |
|----------|-------------|-------------|
| Critical + Open | Light Red (#FFC7CE) | Dark Red (#9C0006), Bold |
| High + Open | Light Orange (#FABF8F) | Dark Orange (#9C5700) |
| Medium + Open | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Low + Open | Light Grey (#D9D9D9) | Dark Grey (#595959) |
| Closed | Light Green (#C6EFCE) | Dark Green (#006100) |

### Required_Procedures Sheet

#### Status Formatting

| Status | Fill Colour | Font Colour |
|--------|-------------|-------------|
| Exists | Light Green (#C6EFCE) | Dark Green (#006100) |
| Partial | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Missing | Light Red (#FFC7CE) | Dark Red (#9C0006) |

---

## 2.5 Formula Specifications

### Procedure_Inventory Calculated Fields

#### Next Review Due Date

```excel
=G2+I2
```
*Calculates next review date from last review plus cycle days*

#### Review Status

```excel
=IF(H2<TODAY(),"OVERDUE",IF(H2<TODAY()+30,"DUE SOON","CURRENT"))
```
*Determines review status based on next review date*

### Dashboard Formulas (if implemented)

#### Total Procedures Count

```excel
=COUNTA(Procedure_Inventory!A:A)-1
```

#### Approved Percentage

```excel
=COUNTIF(Procedure_Inventory!K:K,"Approved")/COUNTA(Procedure_Inventory!A:A)-1)*100
```

#### Overdue Review Count

```excel
=COUNTIF(Procedure_Inventory!H:H,"<"&TODAY())
```

#### Critical Open Gaps

```excel
=COUNTIFS(Gap_Analysis!D:D,"Critical",Gap_Analysis!H:H,"Open")
```

---

## 2.6 Cell Styling Standards

### Colour Palette

| Purpose | Colour Name | Hex Code | RGB |
|---------|-------------|----------|-----|
| Header Background | Theme Blue | #2E75B6 | 46, 117, 182 |
| Header Text | White | #FFFFFF | 255, 255, 255 |
| Alternate Row | Light Grey | #F2F2F2 | 242, 242, 242 |
| Input Field | Light Yellow | #FFFFCC | 255, 255, 204 |
| Success/Approved | Light Green | #C6EFCE | 198, 239, 206 |
| Warning | Light Yellow | #FFEB9C | 255, 235, 156 |
| Error/Alert | Light Red | #FFC7CE | 255, 199, 206 |
| Neutral | Light Grey | #D9D9D9 | 217, 217, 217 |

### Font Standards

| Element | Font | Size | Weight | Colour |
|---------|------|------|--------|--------|
| Sheet Title | Calibri | 16 | Bold | Theme Blue |
| Section Header | Calibri | 12 | Bold | Black |
| Column Header | Calibri | 11 | Bold | White |
| Data Cell | Calibri | 10 | Normal | Black |
| Notes/Comments | Calibri | 9 | Italic | Grey |

### Border Standards

| Element | Style | Colour |
|---------|-------|--------|
| Header Row | Thin all sides | Black |
| Data Rows | Thin all sides | Grey |
| Section Divider | Medium bottom | Black |
| Outer Border | Medium | Black |

### Row Heights

| Row Type | Height (points) |
|----------|-----------------|
| Title | 25 |
| Header | 30 |
| Data | 20 |
| Notes | 15 |

---

## 2.7 Generator Script Reference

### Script Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a537_1_procedure_inventory.py` |
| **Location** | `10-isms-scr-base/isms-a.5.37-documented-procedures/10_generator-master/` |
| **Language** | Python 3.8+ |
| **Dependencies** | openpyxl, logging, datetime |

### Script Structure

```python
# =============================================================================
# ISMS-IMP-A.5.37.1 Procedure Inventory Assessment
# Excel Workbook Generator
# =============================================================================

# Section 1: Imports and Configuration
# Section 2: Constants and Metadata
# Section 3: Style Definitions
# Section 4: Data Validation Lists
# Section 5: Sheet Creation Functions
# Section 6: Formatting Functions
# Section 7: Main Generation Function
# Section 8: Entry Point

# =============================================================================
# QA_VERIFIED: [Date]
# QA_STATUS: PASSED - STANDARDIZATION COMPLETE
# =============================================================================
```

### Key Functions

| Function | Purpose |
|----------|---------|
| `create_instructions_sheet()` | Generates Instructions sheet |
| `create_procedure_inventory_sheet()` | Generates Procedure_Inventory sheet |
| `create_required_procedures_sheet()` | Generates Required_Procedures sheet |
| `create_accessibility_matrix_sheet()` | Generates Accessibility_Matrix sheet |
| `create_gap_analysis_sheet()` | Generates Gap_Analysis sheet |
| `create_evidence_register_sheet()` | Generates Evidence_Register sheet |
| `create_approval_signoff_sheet()` | Generates Approval_SignOff sheet |
| `apply_conditional_formatting()` | Applies conditional formatting rules |
| `apply_data_validations()` | Applies dropdown validations |
| `generate_workbook()` | Main orchestration function |

### Output Location

```
10-isms-scr-base/
└── isms-a.5.37-documented-procedures/
    └── 90_workbooks/
        └── ISMS-IMP-A.5.37.1_Procedure_Inventory_Assessment_YYYYMMDD.xlsx
```

### Execution

```bash
cd 10-isms-scr-base/isms-a.5.37-documented-procedures/10_generator-master
python3 generate_a537_1_procedure_inventory.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"The beginning of wisdom is the definition of terms."*
— Socrates

<!-- QA_VERIFIED: 2026-02-03 -->
