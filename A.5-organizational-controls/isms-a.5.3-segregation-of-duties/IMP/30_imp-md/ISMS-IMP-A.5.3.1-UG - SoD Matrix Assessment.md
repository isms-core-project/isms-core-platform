**ISMS-IMP-A.5.3.1-UG - SoD Matrix Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.3: Policies for Segregation of Duties

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.3.1-UG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.3 Segregation of Duties |
| **Parent Policy** | ISMS-POL-A.5.3 - Segregation of Duties |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.3.1-TG.

---

## Assessment Overview

### Purpose

This workbook provides a comprehensive Segregation of Duties (SoD) Matrix Assessment framework that identifies, documents, and tracks conflicting duties within your organisation. The SoD matrix is the foundational artifact that auditors expect to see during ISO 27001:2022 certification.

The assessment serves multiple purposes:
- **Identification**: Systematically identify all role combinations that create segregation conflicts
- **Documentation**: Create an audit-ready matrix showing which roles are incompatible
- **Gap Analysis**: Identify where current role assignments violate segregation principles
- **Risk Management**: Quantify and prioritise segregation risks for remediation
- **Evidence**: Provide Stage 2 audit evidence of operational segregation controls

### Scope

The SoD Matrix Assessment covers:

| Process Domain | Typical Conflicting Duties |
|----------------|---------------------------|
| **Financial** | Request/approve payments, create/modify vendor records, reconcile accounts |
| **IT Operations** | Develop/deploy code, administer/audit systems, create/approve access |
| **Human Resources** | Hire/verify candidates, set/approve compensation, terminate/confirm termination |
| **Procurement** | Select vendors, approve purchases, receive goods |
| **Security** | Configure controls, audit controls, respond to incidents |
| **Change Management** | Request/approve changes, implement/verify changes |

**Inclusions:**
- All business-critical processes identified in risk assessment
- All roles with access to sensitive systems or data
- All automated workflows requiring segregation checks
- Temporary and emergency access arrangements

**Exclusions:**
- Non-security-relevant administrative functions
- Roles without access to sensitive assets
- Contractor roles assessed separately (see A.5.19-23)

### Business Value

A well-maintained SoD matrix delivers:

| Value Area | Benefit |
|------------|---------|
| **Fraud Prevention** | Reduces opportunity for internal fraud by 60-80% |
| **Error Detection** | Independent verification catches mistakes before impact |
| **Regulatory Compliance** | Meets SOX, PCI DSS, FINMA, and other regulatory requirements |
| **Audit Efficiency** | Ready evidence reduces audit preparation time by 50% |
| **Insurance** | Strong controls may reduce cyber insurance premiums |
| **Due Diligence** | Supports M&A and investor due diligence requirements |

### Assessment Frequency

| Assessment Type | Frequency | Trigger Events |
|-----------------|-----------|----------------|
| Full Matrix Review | Annual | Major restructuring, new systems |
| Conflict Verification | Quarterly | Role changes, new business processes |
| Gap Status Update | Monthly | Remediation progress tracking |
| Exception Review | Quarterly | Compensating control effectiveness |
| Ad-hoc Review | As needed | Incident investigation, audit finding |

---

## Control Requirements

### ISO 27001:2022 Control A.5.3

Per ISO/IEC 27001:2022 Control A.5.3:

> *"Conflicting duties and conflicting areas of responsibility should be segregated."*

**Control Type:** Preventive
**Security Properties:** Confidentiality, Integrity, Availability
**Cybersecurity Concepts:** Protect
**Operational Capabilities:** Governance, Identity and Access Management

### Implementation Requirements

This control requires that:
1. Conflicting duties are identified and documented
2. Segregation is implemented where possible
3. Compensating controls are applied where segregation is not feasible
4. Regular review ensures continued compliance

### What Auditors Look For

ISO 27001 auditors examining Control A.5.3 will verify:

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Matrix Existence** | Formal SoD matrix document |
| **Completeness** | Coverage of all critical processes |
| **Currency** | Recent review dates, current role assignments |
| **Gap Tracking** | Documentation of known conflicts |
| **Compensating Controls** | Evidence for unavoidable conflicts |
| **Approval** | Management sign-off on matrix and exceptions |

### Why This Matters

**Audit Perspective:**
Stage 2 auditors specifically look for a formal SoD matrix. According to best practices, "auditors expect maps and artifacts - role matrices and digital logs that prove, for every critical action, at least one trusted 'segregator' is present." This workbook provides exactly that evidence.

**Business Perspective:**
Organisations without proper SoD:
- Experience 3x higher rates of internal fraud
- Face extended incident detection times
- Suffer more severe regulatory penalties
- Lack defensible positions during investigations

**Risk Perspective:**
The key principle is that **no single person should have enough authority to execute a sensitive process from start to finish without a second person's involvement**. This workbook systematically identifies where that principle is violated.

---

## Prerequisites

### Required Access

Before beginning this assessment, ensure access to:

| System | Purpose | Access Level Needed |
|--------|---------|---------------------|
| HR System | Organisation chart, role definitions | Read access to all roles |
| IAM/Directory | Current role assignments | Report access |
| ITSM | Change/incident records | Read access |
| Finance System | Transaction approval workflows | Workflow documentation |
| Access Management | RBAC configuration | Admin or audit access |

### Required Documents

- [ ] Current organisation chart with all roles
- [ ] Role-Based Access Control (RBAC) documentation
- [ ] Business process documentation for critical workflows
- [ ] Prior SoD assessments (if applicable)
- [ ] Risk assessment identifying critical processes
- [ ] List of privileged/administrator accounts
- [ ] Compliance requirements (SOX, PCI DSS, FINMA if applicable)

### Required Personnel

| Role | Responsibility | Time Commitment |
|------|----------------|-----------------|
| **SoD Assessment Lead** | Coordinate assessment, validate matrix | 8-16 hours |
| **Process Owners** | Define critical duties per process | 2-4 hours each |
| **IT Security** | Validate technical control capabilities | 4-8 hours |
| **Internal Audit** | Independent validation, gap assessment | 4-8 hours |
| **HR Representative** | Validate role definitions, org structure | 2-4 hours |

### Required Approvals

| Approval | Approver | When Needed |
|----------|----------|-------------|
| Access to HR/IAM systems | IT Security | Before starting |
| Authority to review role assignments | CISO | Before starting |
| Scope confirmation | Information Security Manager | Before starting |
| Final matrix approval | CISO/Executive Management | At completion |

### Time Allocation

| Organisation Size | Roles to Assess | Estimated Duration |
|-------------------|-----------------|-------------------|
| Small (<100 employees) | 20-50 roles | 1-2 weeks |
| Medium (100-500 employees) | 50-150 roles | 2-4 weeks |
| Large (500+ employees) | 150+ roles | 4-8 weeks |

### Prerequisite Checklist

Before proceeding, verify:

- [ ] Access to HR system confirmed
- [ ] IAM/Directory access confirmed
- [ ] Business process documentation available
- [ ] Process owner contacts identified
- [ ] Prior assessments reviewed (if any)
- [ ] Assessment scope approved
- [ ] Timeline agreed with stakeholders

---

## Completion Walkthrough

### Step 1: Populate Role Inventory

**Time allocation:** 2-4 hours

**Purpose:** Create a complete catalogue of all roles in scope for SoD assessment.

**Fields to Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| Role_ID | Unique identifier | ROLE-FIN-001 |
| Role_Name | Descriptive name | Accounts Payable Clerk |
| Department | Organisational unit | Finance |
| Process_Domain | Primary process area | Financial Processing |
| Risk_Level | Sensitivity rating | High / Medium / Low |
| Description | Brief role description | Processes vendor invoices and payment requests |
| Key_Duties | Primary responsibilities | Invoice entry, payment preparation |
| System_Access | Systems this role can access | SAP, Treasury System |
| Active | Currently in use | Yes / No |

**Worked Example - Finance Department Roles:**

| Role_ID | Role_Name | Department | Process_Domain | Risk_Level |
|---------|-----------|------------|----------------|------------|
| ROLE-FIN-001 | AP Clerk | Finance | Financial Processing | Medium |
| ROLE-FIN-002 | AP Manager | Finance | Financial Processing | High |
| ROLE-FIN-003 | AR Clerk | Finance | Financial Processing | Medium |
| ROLE-FIN-004 | AR Manager | Finance | Financial Processing | High |
| ROLE-FIN-005 | GL Accountant | Finance | Financial Processing | High |
| ROLE-FIN-006 | Treasurer | Finance | Financial Processing | Critical |
| ROLE-FIN-007 | Controller | Finance | Financial Processing | Critical |
| ROLE-FIN-008 | Payroll Specialist | Finance | Payroll Processing | High |
| ROLE-FIN-009 | Payroll Manager | Finance | Payroll Processing | Critical |

**Best Practices:**
- Use your RBAC documentation as the starting point
- Include both permanent and temporary roles
- Document shared/generic roles separately (these are high risk)
- Include automated/service accounts that perform duties
- Interview department heads to confirm completeness
- Cross-reference with HR system role definitions

### Step 2: Complete Conflict Matrix

**Time allocation:** 4-8 hours

**Purpose:** Define which role combinations create segregation conflicts.

The Conflict Matrix is a role-by-role comparison table where you mark whether combining two roles creates a conflict.

**Conflict Classifications:**

| Code | Meaning | Action Required |
|:----:|---------|-----------------|
| **X** | Hard Conflict | Must never be combined; no exceptions |
| **C** | Conditional Conflict | Requires compensating controls if combined |
| **M** | Monitoring Required | May be combined with enhanced monitoring |
| **-** | No Conflict | Roles may be combined |

**Standard Conflict Patterns:**

| Pattern | Example Conflict | Classification |
|---------|-----------------|----------------|
| Maker/Checker | Create payment / Approve payment | X |
| Requestor/Approver | Request access / Approve access | X |
| Developer/Deployer | Write code / Deploy to production | X |
| Admin/Auditor | Administer system / Audit system | X or C |
| Creator/Reconciler | Create records / Reconcile records | C |
| Custodian/Owner | Hold assets / Approve asset use | C |

**Worked Example - Financial Roles:**

|  | AP Clerk | AP Manager | AR Clerk | AR Manager | GL Accountant | Treasurer |
|--|:--------:|:----------:|:--------:|:----------:|:-------------:|:---------:|
| **AP Clerk** | - | - | M | M | C | X |
| **AP Manager** | - | - | M | C | C | X |
| **AR Clerk** | M | M | - | - | C | C |
| **AR Manager** | M | C | - | - | C | C |
| **GL Accountant** | C | C | C | C | - | C |
| **Treasurer** | X | X | C | C | C | - |

**Reading the Matrix:** An "X" at AP Clerk/Treasurer intersection means a person should NEVER hold both roles - this would allow someone to create and pay their own invoices.

**Detailed Conflict Analysis by Domain:**

**Financial Conflicts:**
| Role A | Role B | Conflict | Risk Description |
|--------|--------|:--------:|------------------|
| Vendor Creator | Payment Approver | X | Can create fake vendor and pay themselves |
| Invoice Entry | Invoice Approval | X | Can create and approve fraudulent invoices |
| Payroll Entry | Payroll Approval | X | Can manipulate payroll amounts |
| Bank Reconciliation | Cash Custody | X | Can hide theft through false reconciliation |
| Expense Submission | Expense Approval | X | Can submit and approve personal expenses |

**IT Operations Conflicts:**
| Role A | Role B | Conflict | Risk Description |
|--------|--------|:--------:|------------------|
| Code Developer | Production Deployer | X | Can deploy malicious code without review |
| DBA | Application Admin | C | Database and application control combination |
| System Admin | Security Admin | X | Can modify and audit own actions |
| Change Requester | Change Approver | X | Can approve own changes |
| User Admin | Audit Log Admin | X | Can create access and hide evidence |

### Step 3: Document Current Assignments

**Time allocation:** 2-4 hours

**Purpose:** Record which people currently hold which roles.

**Fields to Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| Person_ID | Employee identifier | EMP-12345 |
| Name | Full name | John Smith |
| Department | Current department | Finance |
| Primary_Role | Main role assignment | AP Clerk |
| Additional_Roles | Secondary roles (comma-separated) | Expense Reviewer |
| Assignment_Date | When roles were assigned | 15.03.2025 |
| Last_Review | Last access review date | 01.01.2026 |
| Manager | Reporting manager | Jane Doe |
| Notes | Special circumstances | Temporary backup for AP Manager |

**Worked Example - Current Assignments:**

| Person_ID | Name | Department | Primary_Role | Additional_Roles | Last_Review |
|-----------|------|------------|--------------|------------------|-------------|
| EMP-12345 | John Smith | Finance | AP Clerk | Expense Reviewer | 01.01.2026 |
| EMP-12346 | Jane Doe | Finance | AP Manager | - | 01.01.2026 |
| EMP-12347 | Bob Wilson | Finance | AR Clerk | AP Clerk (Backup) | 01.01.2026 |
| EMP-12348 | Alice Brown | Finance | GL Accountant | AP Manager (Backup) | 01.01.2026 |

**Data Sources:**
- Active Directory / IAM system export
- HR system role assignments
- Application-specific role reports
- Privileged access management system
- Manager attestation forms

### Step 4: Run Gap Analysis

**Time allocation:** 2-4 hours

**Purpose:** Compare current assignments against the conflict matrix to identify violations.

The Gap Analysis sheet auto-identifies conflicts by cross-referencing:
1. Each person's role assignments (from Step 3)
2. Conflict definitions (from Step 2)

**Gap Record Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Gap_ID | Unique identifier | GAP-2026-001 |
| Person_ID | Affected employee | EMP-12345 |
| Name | Employee name | John Smith |
| Conflicting_Roles | The roles in conflict | AP Clerk + Treasurer |
| Conflict_Type | X, C, or M | X |
| Risk_Level | Impact assessment | Critical |
| Identified_Date | When discovered | 03.02.2026 |
| Status | Current state | Open / Mitigated / Resolved |

**Worked Example - Gap Identification:**

| Gap_ID | Person_ID | Name | Conflicting_Roles | Conflict_Type | Risk_Level | Status |
|--------|-----------|------|-------------------|:-------------:|:----------:|--------|
| GAP-2026-001 | EMP-12347 | Bob Wilson | AR Clerk + AP Clerk | M | Medium | Open |
| GAP-2026-002 | EMP-12348 | Alice Brown | GL Accountant + AP Manager | C | High | Open |
| GAP-2026-003 | EMP-12350 | Tom Lee | Developer + Deployer | X | Critical | Open |

**Risk Level Determination:**

| Conflict Type | System Sensitivity | Risk Level |
|:-------------:|:------------------:|:----------:|
| X | Any | Critical |
| C | High | High |
| C | Medium/Low | Medium |
| M | High | Medium |
| M | Medium/Low | Low |

**Risk Level SLAs:**

| Risk Level | Remediation SLA | Escalation Point |
|:----------:|-----------------|------------------|
| Critical | 7 days | CISO, Executive Management |
| High | 30 days | CISO |
| Medium | 60 days | Information Security Manager |
| Low | 90 days | Security Team Lead |

### Step 5: Create Remediation Plans

**Time allocation:** 2-4 hours

**Purpose:** Document actions to resolve identified gaps.

**Remediation Options:**

| Option | When to Use | Example |
|--------|-------------|---------|
| **Role Removal** | Clear conflict; role not essential | Remove Treasurer role from AP Clerk |
| **Role Reassignment** | Conflict exists; duties needed | Assign conflicting role to different person |
| **Process Redesign** | Workflow permits conflict | Add approval step before execution |
| **Compensating Control** | Small team; no separation possible | Enhanced monitoring + independent review |

**Remediation Record Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Remediation_ID | Unique identifier | REM-2026-001 |
| Gap_ID | Related gap | GAP-2026-001 |
| Action_Type | Remediation approach | Role Removal |
| Description | Specific action | Remove Treasurer role from John Smith |
| Owner | Responsible person | HR Manager |
| Target_Date | Deadline | 28.02.2026 |
| Status | Current state | In Progress |
| Completion_Date | When closed | - |
| Evidence_Ref | Proof of completion | EVD-2026-001 |

**Worked Example - Remediation Plan:**

| Remediation_ID | Gap_ID | Action_Type | Description | Owner | Target_Date | Status |
|----------------|--------|-------------|-------------|-------|-------------|--------|
| REM-2026-001 | GAP-2026-001 | Role Removal | Remove AP Clerk backup role from Bob Wilson | IT Security | 15.02.2026 | In Progress |
| REM-2026-002 | GAP-2026-002 | Compensating Control | Implement enhanced monitoring for Alice Brown | CISO | 28.02.2026 | Not Started |
| REM-2026-003 | GAP-2026-003 | Process Redesign | Separate deployment approval for Tom Lee's code | DevOps Lead | 10.02.2026 | In Progress |

### Step 6: Document Exceptions and Compensating Controls

**Time allocation:** 1-2 hours

**Purpose:** For conflicts that cannot be resolved through separation, document formal exceptions with compensating controls.

**When Exceptions Are Permitted:**
- Small teams where full segregation is impossible
- Emergency/break-glass scenarios
- Temporary situations pending remediation
- Business-critical operations requiring combined access

**Exception Record Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Exception_ID | Unique identifier | EXC-2026-001 |
| Gap_ID | Related gap | GAP-2026-001 |
| Justification | Business reason | Team of 2; cannot split duties |
| Compensating_Controls | Controls applied | Enhanced logging, weekly CEO review, quarterly audit |
| Risk_Acceptance | Approver | CFO, CISO |
| Approval_Date | When approved | 10.02.2026 |
| Expiry_Date | Review deadline | 10.05.2026 |
| Review_Frequency | How often re-evaluated | Quarterly |

**Required Compensating Controls:**

Per ISO 27001 guidance, when segregation is not possible:
1. **Activity Logging**: Every action logged and immutable
2. **Independent Review**: Logs reviewed by uninvolved party
3. **Management Oversight**: Regular management review of activities
4. **Audit Trail**: Full audit trail for all transactions
5. **Detective Controls**: Automated alerts for unusual patterns

**Compensating Control Examples by Risk Level:**

| Risk Level | Minimum Compensating Controls |
|:----------:|------------------------------|
| Critical | Real-time monitoring, daily management review, quarterly audit, dual approval for high-value transactions |
| High | Daily log review, weekly management review, quarterly audit |
| Medium | Weekly log review, monthly management review, annual audit |
| Low | Monthly log review, quarterly management review |

**Worked Example - Exception Register:**

| Exception_ID | Gap_ID | Justification | Compensating_Controls | Expiry_Date | Status |
|--------------|--------|---------------|----------------------|-------------|--------|
| EXC-2026-001 | GAP-2026-002 | Finance team of 3; cannot separate GL and AP | Enhanced logging, CFO weekly review, Internal Audit quarterly | 10.05.2026 | Active |
| EXC-2026-002 | GAP-2026-004 | Emergency access for on-call engineer | All access logged, reviewed within 24hrs, time-limited to incident | N/A (per incident) | Active |

---

## Evidence Collection

### Evidence Requirements

| Evidence Type | Source | Retention |
|---------------|--------|-----------|
| SoD Matrix (this workbook) | Generated | 7 years |
| Access right reports | IAM system | 3 years |
| Role assignment logs | HR/Directory | 3 years |
| Exception approvals | Email/workflow | Duration + 2 years |
| Compensating control evidence | Various | Duration + 2 years |
| Management sign-offs | This workbook | 7 years |
| Log review records | SIEM/Review tool | 3 years |
| Audit reports | Internal Audit | 7 years |

### Evidence Storage

**Primary Location:** `[SharePoint/Evidence Library]/A.5.3/SoD-Matrix/[Year]/`

**Folder Structure:**
```
A.5.3/
|-- SoD-Matrix/
|   |-- 2026/
|   |   |-- Assessment-Workbooks/
|   |   |   |-- ISMS-IMP-A.5.3.1_SoD_Matrix_Assessment_20260203.xlsx
|   |   |-- Evidence/
|   |   |   |-- Role-Inventory/
|   |   |   |   |-- RBAC-Export-20260203.xlsx
|   |   |   |   |-- AD-Role-Report-20260203.pdf
|   |   |   |   |-- HR-Role-Definitions-20260203.xlsx
|   |   |   |-- Gap-Analysis/
|   |   |   |   |-- Access-Review-Q1-2026.xlsx
|   |   |   |   |-- Conflict-Identification-Notes.pdf
|   |   |   |   |-- Gap-Analysis-Working-Papers.xlsx
|   |   |   |-- Exceptions/
|   |   |   |   |-- EXC-2026-001-Approval.pdf
|   |   |   |   |-- EXC-2026-001-Compensating-Control-Evidence/
|   |   |   |   |   |-- Weekly-Review-Log-2026-01.pdf
|   |   |   |   |   |-- Audit-Report-Q1-2026.pdf
|   |   |   |-- Approvals/
|   |   |   |   |-- CISO-SignOff-20260203.pdf
|   |   |   |   |-- Management-Approval-20260203.pdf
```

**Naming Convention:**
```
EVD-A.5.3.1_[EvidenceType]_[Reference]_[YYYYMMDD].[ext]
```

**Examples:**
- `EVD-A.5.3.1_RoleInventory_Export_20260203.xlsx`
- `EVD-A.5.3.1_GapAnalysis_Summary_20260203.pdf`
- `EVD-A.5.3.1_Exception_EXC-2026-001_Approval_20260210.pdf`

### Evidence Collection Process

#### Step 1: Gather Role Information

1. Export role definitions from IAM system
2. Export organisation chart from HR system
3. Document all system-specific roles
4. Store exports with date stamps

#### Step 2: Document Current State

1. Export current role assignments per person
2. Capture screenshot/export of IAM configuration
3. Document any pending role changes
4. Store with assessment workbook

#### Step 3: Record Approvals

1. Obtain signed approval forms
2. Save email approvals as PDF
3. Link approvals to specific exceptions
4. Store in ISMS Evidence Library

---

## Common Pitfalls

Avoid these common mistakes when completing the SoD Matrix assessment:

### Inventory Completeness Pitfalls

❌ **MISTAKE**: Creating a SoD matrix once and never updating it
✅ **CORRECT**: Review quarterly and update after any role changes, reorganisations, or new systems; treat the matrix as a living document

❌ **MISTAKE**: Documenting conflicts but not checking actual role assignments
✅ **CORRECT**: Cross-reference conflict matrix against actual IAM system assignments monthly; automated checks are preferable

❌ **MISTAKE**: Only including IT roles in the assessment
✅ **CORRECT**: Include all business roles across Finance, HR, Operations, Procurement, and any department with access to sensitive data or systems

❌ **MISTAKE**: Missing roles that exist only in specific applications
✅ **CORRECT**: Inventory application-specific roles in addition to directory/IAM roles; SAP roles, database roles, and application admin roles often create conflicts

### Role Assignment Pitfalls

❌ **MISTAKE**: Using a shared "Admin" account for multiple people
✅ **CORRECT**: Every user must have unique credentials; shared accounts destroy accountability and make SoD verification impossible

❌ **MISTAKE**: Granting temporary access that becomes permanent
✅ **CORRECT**: Set expiry dates on all temporary role assignments; enforce automatic revocation and require re-approval for extensions

❌ **MISTAKE**: Not documenting emergency/break-glass access
✅ **CORRECT**: Include emergency access procedures in the assessment; all break-glass access must be logged, reviewed, and time-limited

❌ **MISTAKE**: Forgetting about service accounts and automated processes
✅ **CORRECT**: Include all accounts that perform security-relevant actions, including service accounts, batch users, and API credentials

### Conflict Identification Pitfalls

❌ **MISTAKE**: Defining conflicts only at the role level, missing system-specific permissions
✅ **CORRECT**: Include granular permissions (e.g., "approve own requests" at application level); some conflicts exist within roles, not just between them

❌ **MISTAKE**: Treating all conflicts the same regardless of data sensitivity
✅ **CORRECT**: Apply risk-based conflict classification; conflicts involving financial data or PII require stricter controls than those involving internal operations data

❌ **MISTAKE**: Not considering cross-system conflicts
✅ **CORRECT**: Analyse conflicts that span multiple systems; a developer with read access to production database and deploy rights creates a conflict even if roles are in different systems

❌ **MISTAKE**: Assuming inherited or nested group memberships don't create conflicts
✅ **CORRECT**: Analyse effective permissions including all group memberships; nested groups often create unexpected conflict situations

### Documentation and Process Pitfalls

❌ **MISTAKE**: Not documenting compensating controls for small team exceptions
✅ **CORRECT**: Every exception requires formal documentation of compensating controls and risk acceptance; "we're too small" is not sufficient justification without controls

❌ **MISTAKE**: Treating the matrix as a one-time documentation exercise
✅ **CORRECT**: SoD matrix must be integrated into access management processes; new role assignments should check the matrix before approval

❌ **MISTAKE**: Not involving process owners in conflict identification
✅ **CORRECT**: Process owners understand where fraud/error opportunities exist; their input is essential for accurate conflict classification

❌ **MISTAKE**: Accepting verbal approvals for exceptions
✅ **CORRECT**: All exceptions require documented approval from authorised personnel; verbal approvals are not audit evidence

### Exception Management Pitfalls

❌ **MISTAKE**: Approving exceptions without compensating controls
✅ **CORRECT**: No exception should be approved without documented compensating controls; the control must be specific, measurable, and verifiable

❌ **MISTAKE**: Allowing exceptions to continue indefinitely
✅ **CORRECT**: All exceptions must have expiry dates and be formally re-reviewed; maximum exception period should be 12 months

❌ **MISTAKE**: Exception register not reviewed regularly
✅ **CORRECT**: Review all active exceptions quarterly; verify compensating controls are functioning and still necessary

❌ **MISTAKE**: Compensating control evidence not collected
✅ **CORRECT**: Maintain evidence that compensating controls are operating effectively; log reviews, audit reports, and management sign-offs must be documented

---

## Quality Checklist

Before submitting the completed workbook, verify all items:

### Completeness Checks

- [ ] All roles in scope are listed in Role_Inventory
- [ ] Conflict_Matrix covers all role combinations
- [ ] Current_Assignments includes all personnel with roles in scope
- [ ] All identified gaps have records in Gap_Analysis
- [ ] Each gap has either a remediation plan or documented exception
- [ ] All sheets are populated with no blank required fields
- [ ] Instructions sheet reviewed and understood

### Coverage Checks

- [ ] Finance department roles included and assessed
- [ ] IT department roles included and assessed
- [ ] HR department roles included and assessed
- [ ] Procurement roles included and assessed
- [ ] Security roles included and assessed
- [ ] All application-specific admin roles included
- [ ] Service accounts and automated processes included
- [ ] Temporary and emergency access arrangements documented

### Accuracy Checks

- [ ] Role definitions match actual RBAC configuration
- [ ] Current assignments verified against IAM system export
- [ ] Conflict classifications reviewed by process owners
- [ ] Gap risk levels consistent with methodology
- [ ] Remediation target dates realistic and achievable
- [ ] Exception expiry dates appropriate (max 12 months)
- [ ] Compensating controls specific and measurable

### Documentation Checks

- [ ] Evidence files stored in correct location
- [ ] Evidence naming convention followed
- [ ] Exception approvals signed and dated
- [ ] Compensating controls specified for all exceptions
- [ ] Remediation target dates tracked and realistic
- [ ] All required attachments present

### Process Checks

- [ ] Internal Audit reviewed gap analysis
- [ ] Process owners validated conflict matrix
- [ ] HR verified role definitions
- [ ] IT Security verified technical accuracy
- [ ] CISO approved final assessment
- [ ] Workbook saved with correct naming convention
- [ ] All reviewers have signed off

### Evidence Checks

- [ ] IAM system export attached
- [ ] Organisation chart attached
- [ ] Prior assessment reviewed (if applicable)
- [ ] Exception approval documentation attached
- [ ] Compensating control evidence attached
- [ ] Management approval documentation attached

---

## Review and Approval

### Review Workflow

| Step | Role | Responsibility | Timeline |
|------|------|----------------|----------|
| 1 | Assessment Lead | Complete all sheets with evidence | By deadline |
| 2 | Process Owners | Validate conflicts for their domains | 5 business days |
| 3 | IT Security | Verify technical accuracy | 5 business days |
| 4 | Internal Audit | Independent validation of gaps | 5 business days |
| 5 | CISO | Approve final assessment | 3 business days |
| 6 | Executive Management | Accept residual risk (exceptions) | As needed |

### Approval Workflow

```
Assessment Lead Completes
        │
        ▼
Self-Review (Quality Checklist)
        │
        ▼
Process Owners Validate ──────► Return for Corrections
        │                              │
        ▼                              │
IT Security Verify ───────────► Return for Corrections
        │                              │
        ▼                              │
Internal Audit Review ────────► Return for Corrections
        │                              │
        ▼                              │
CISO Final Approval ──────────────────┘
        │
        ▼
   Assessment Complete
        │
        ▼
   Upload to ISMS Evidence Library
```

### Approval Signatures

The Approval_SignOff sheet requires:

1. **Assessment Lead Certification:**
   - Confirms methodology was followed
   - Confirms evidence was verified
   - Date and signature

2. **Internal Audit Review:**
   - Confirms independent validation
   - Documents any concerns
   - Date and signature

3. **CISO Approval:**
   - Approves final matrix
   - Authorises exception register
   - Date and signature

### Sign-Off Requirements

| Role | Signature Required | Authority |
|------|-------------------|-----------|
| Assessment Lead | Yes | Confirms accuracy of information |
| Process Owners | Yes (relevant areas) | Confirms conflict accuracy |
| IT Security | Yes | Confirms technical accuracy |
| Internal Audit | Yes | Confirms independent validation |
| CISO | Yes | Final approval authority |

### Post-Approval Actions

Upon approval:

1. Upload completed workbook to ISMS Evidence Library
2. Update ISMS control status to reflect assessment completion
3. Schedule next assessment (quarterly for gap status, annual for full)
4. Communicate any identified gaps to relevant parties
5. Initiate remediation tracking for all open gaps
6. Set calendar reminders for exception reviews
7. Update related controls (A.5.3.2, A.5.3.4) as needed

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
