<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.3.3-UG:framework:UG:a.5.3.3 -->
**ISMS-IMP-A.5.3.3-UG - Role-Function Mapping**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.3: Policies for Segregation of Duties

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Role-Function Mapping |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.3.3-UG |
| **Related Policy** | ISMS-POL-A.5.3 (Segregation of Duties) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.3 (Policies for Segregation of Duties) |
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

- ISMS-POL-A.5.3 (Segregation of Duties)
- ISMS-IMP-A.5.3.1 (SoD Matrix Assessment)
- ISMS-IMP-A.5.3.2 (Conflict Analysis)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.3.3-TG.

---

## Assessment Overview

### Purpose

This workbook provides a comprehensive mapping between organisational roles and their associated functions/permissions. Role-Function Mapping is essential for implementing role-based segregation of duties because it documents exactly what each role can do across all systems.

The assessment serves multiple purposes:
- **Transparency**: Document all permissions associated with each role
- **Analysis**: Enable granular conflict detection at function level
- **RBAC Validation**: Verify role definitions match actual permissions
- **Access Review**: Support periodic access certification
- **Change Control**: Track permission changes over time

### Scope

The Role-Function Mapping covers:

| Layer | What's Mapped | Example |
|-------|---------------|---------|
| **Business Role** | Organisational position | Accounts Payable Manager |
| **Application Role** | System-specific role | SAP FI-Vendor-Admin |
| **Function** | Specific capability | Create Vendor Master Record |
| **Permission** | Technical access right | T-Code FK01 |
| **Data Scope** | Data boundaries | Company Code 1000 only |

**Mapping Levels:**

```
Business Role
    |
    +-- Application Role 1
    |       +-- Function A
    |       |       +-- Permission 1
    |       |       +-- Permission 2
    |       +-- Function B
    |               +-- Permission 3
    |
    +-- Application Role 2
            +-- Function C
                    +-- Permission 4
```

### Business Value

Detailed role-function mapping delivers:

| Value Area | Benefit |
|------------|---------|
| **Hidden Conflict Detection** | Identify conflicts invisible at role level |
| **Least Privilege Validation** | Verify users have only needed permissions |
| **Audit Evidence** | Provide detailed access documentation |
| **Compliance Demonstration** | Meet regulatory access control requirements |
| **Change Impact Analysis** | Understand effects of permission changes |
| **Access Certification** | Support periodic access reviews |

### Assessment Frequency

| Activity | Frequency | Trigger Events |
|----------|-----------|----------------|
| Full Role-Function Mapping | Annual | Major RBAC changes |
| Validation Against Systems | Quarterly | System upgrades |
| Function Conflict Review | Quarterly | New functions added |
| Change Log Update | Ongoing | Any permission change |
| Dormant Permission Analysis | Quarterly | Access review cycles |

### Workbook at a Glance

This workbook contains the following sheets:

| Sheet | Purpose |
|-------|---------|
| **Instructions & Legend** | Assessment guidance, CRUD+A classifications, and field descriptions |
| **Business Roles** | Catalogue of organisational roles in scope for mapping |
| **Application Roles** | Application-specific roles linked to each business role |
| **Functions** | Discrete capabilities available in each application |
| **Permissions** | Technical permissions (T-codes, API calls, etc.) enabling each function |
| **Role Function Map** | Complete mapping of business roles to functions |
| **Function Conflicts** | Function-level conflicts and their classifications |
| **Validation Status** | Results of RBAC validation against actual system configuration |
| **Change Log** | Ongoing record of all permission and mapping changes |
| **Summary Dashboard** | Compliance overview auto-populated from your input data |
| **Approval Sign-Off** | Stakeholder sign-off and approval workflow |

---

## Control Requirements

### ISO 27001:2022 Control A.5.3

Per ISO/IEC 27001:2022 Control A.5.3:

> *"Conflicting duties and conflicting areas of responsibility should be segregated."*

**Control Type:** Preventive
**Security Properties:** Confidentiality, Integrity, Availability
**Cybersecurity Concepts:** Protect
**Operational Capabilities:** Governance, Identity and Access Management

Role-Function Mapping enables this by providing the granular detail needed to identify function-level conflicts, not just role-level conflicts.

### What Auditors Look For

ISO 27001 auditors examining role-function mapping will verify:

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Completeness** | All roles and functions documented |
| **Accuracy** | Mapping matches actual system configuration |
| **Currency** | Recent validation dates |
| **Conflict Analysis** | Function-level conflicts identified |
| **Change Control** | Permission changes tracked |
| **Validation** | Regular reconciliation against systems |

### Why This Matters

**The Hidden Conflict Problem:**
Role-level analysis often misses conflicts that exist at the function level. For example:
- Two roles might appear non-conflicting at the role level
- But one role includes a "supervisor override" function
- That override function creates a conflict not visible at role level

**Role-Based Access Control (RBAC) Validation:**
Many organisations implement RBAC but don't validate that roles are correctly defined. This workbook:
- Documents intended permissions for each role
- Compares against actual system configuration
- Identifies role definition drift over time

**Audit Evidence:**
Auditors increasingly ask for function-level analysis. This workbook provides:
- Complete permission inventory by role
- Mapping to business processes
- Evidence of regular review and validation

---

## Prerequisites

### Required Access

| System | Purpose | Access Level Needed |
|--------|---------|---------------------|
| IAM/Directory | Role definitions, group memberships | Admin or audit access |
| Application Admin Panels | Application-specific role configs | Admin or audit access |
| HR System | Business role assignments | Read access |
| Security Documentation | Existing RBAC documentation | Read access |

### Required Documents

- [ ] RBAC design documentation
- [ ] Application security configuration guides
- [ ] Business process documentation
- [ ] Prior role-function mappings (if available)
- [ ] Audit reports on access management
- [ ] System-specific role documentation (SAP, Oracle, etc.)

### Required Personnel

| Role | Responsibility | Time Commitment |
|------|----------------|-----------------|
| **Mapping Lead** | Coordinate mapping effort | 8-16 hours |
| **Application Administrators** | Provide role/permission details | 2-4 hours per application |
| **Process Owners** | Validate function-to-process mapping | 2-4 hours per process |
| **IT Security** | Validate technical accuracy | 4-8 hours |
| **Internal Audit** | Independent validation | 4-8 hours |

### Prerequisite Checklist

Before proceeding, verify:

- [ ] Access to IAM system confirmed
- [ ] Application admin contacts identified
- [ ] RBAC documentation available
- [ ] Process owner availability confirmed
- [ ] Prior mappings reviewed (if any)
- [ ] System access for validation available

---

## Completion Walkthrough

### Step 1: Define Business Roles

**Time allocation:** 2-4 hours

**Purpose:** Create a catalogue of all organisational roles requiring mapping.

**Fields to Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| Business_Role_ID | Unique identifier | BROLE-FIN-001 |
| Role_Name | Descriptive name | Accounts Payable Manager |
| Department | Organisational unit | Finance |
| Process_Domain | Primary process area | Financial Processing |
| Role_Owner | Accountable person | CFO |
| Description | Brief description | Manages AP team and approves payments |
| Risk_Level | Role sensitivity | High / Medium / Low |
| Last_Reviewed | Review date | 01.01.2026 |

**Worked Example - Business Roles:**

| Business_Role_ID | Role_Name | Department | Process_Domain | Risk_Level | Role_Owner |
|------------------|-----------|------------|----------------|:----------:|------------|
| BROLE-FIN-001 | AP Manager | Finance | Financial Processing | High | CFO |
| BROLE-FIN-002 | AP Clerk | Finance | Financial Processing | Medium | Finance Director |
| BROLE-FIN-003 | GL Accountant | Finance | Financial Reporting | High | CFO |
| BROLE-IT-001 | System Administrator | IT | IT Operations | Critical | CIO |
| BROLE-IT-002 | DBA | IT | Database Operations | Critical | IT Director |
| BROLE-IT-003 | Developer | IT | Software Development | High | Dev Manager |
| BROLE-SEC-001 | Security Analyst | Security | Security Operations | High | CISO |

### Step 2: Inventory Application Roles

**Time allocation:** 4-8 hours

**Purpose:** List all application-specific roles that business roles are assigned.

**Fields to Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| App_Role_ID | Unique identifier | AROLE-SAP-FI-001 |
| Application | System name | SAP ERP |
| Role_Name | Application role name | FI-AP-Manager |
| Role_Type | Classification | Composite / Single |
| Description | What the role provides | Full AP processing and approval |
| Business_Roles | Linked business roles | BROLE-FIN-001, BROLE-FIN-002 |
| Criticality | Risk classification | Critical / High / Medium / Low |
| Review_Frequency | How often reviewed | Quarterly |

**Worked Example - Application Roles:**

| App_Role_ID | Application | Role_Name | Role_Type | Business_Roles | Criticality |
|-------------|-------------|-----------|:---------:|----------------|:-----------:|
| AROLE-SAP-FI-001 | SAP ERP | FI-AP-Manager | Composite | BROLE-FIN-001 | High |
| AROLE-SAP-FI-002 | SAP ERP | FI-AP-Clerk | Single | BROLE-FIN-002 | Medium |
| AROLE-SAP-FI-003 | SAP ERP | FI-GL-Full | Composite | BROLE-FIN-003 | High |
| AROLE-AD-001 | Active Directory | Domain Admins | Single | BROLE-IT-001 | Critical |
| AROLE-SQL-001 | SQL Server | db_owner | Single | BROLE-IT-002 | Critical |
| AROLE-JIRA-001 | Jira | Developer | Single | BROLE-IT-003 | Medium |

**Role Type Definitions:**

| Type | Description | Example |
|------|-------------|---------|
| **Single** | Individual role with specific permissions | FI-AP-Clerk |
| **Composite** | Combines multiple single roles | FI-AP-Manager (includes Clerk + Approval) |
| **Derived** | Inherits from parent role | Child department role |

### Step 3: Define Functions

**Time allocation:** 4-8 hours

**Purpose:** Document discrete capabilities that roles can perform.

**Function Categorisation:**

| Category | Description | Examples |
|----------|-------------|----------|
| **Create** | Ability to create new records | Create vendor, Create PO |
| **Read** | Ability to view information | View accounts, Read reports |
| **Update** | Ability to modify records | Change vendor, Update PO |
| **Delete** | Ability to remove records | Delete vendor, Cancel PO |
| **Approve** | Ability to authorise actions | Approve payment, Approve access |
| **Execute** | Ability to perform transactions | Post journal, Run payroll |
| **Admin** | System administration capability | User management, Config change |

**Fields to Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| Function_ID | Unique identifier | FUNC-FIN-001 |
| Function_Name | Descriptive name | Approve Payment |
| Category | CRUD+A classification | Approve |
| Application | System providing function | SAP ERP |
| Process | Business process supported | Accounts Payable |
| Description | What the function does | Authorise payment execution |
| Risk_Level | Function sensitivity | Critical / High / Medium / Low |
| SoD_Sensitive | Conflicts with other functions | Yes / No |

**Worked Example - Functions:**

| Function_ID | Function_Name | Category | Application | Process | Risk_Level | SoD_Sensitive |
|-------------|---------------|:--------:|-------------|---------|:----------:|:-------------:|
| FUNC-FIN-001 | Create Vendor | Create | SAP ERP | Procurement | High | Yes |
| FUNC-FIN-002 | Approve Vendor | Approve | SAP ERP | Procurement | High | Yes |
| FUNC-FIN-003 | Create Invoice | Create | SAP ERP | Accounts Payable | Medium | Yes |
| FUNC-FIN-004 | Approve Invoice | Approve | SAP ERP | Accounts Payable | High | Yes |
| FUNC-FIN-005 | Execute Payment | Execute | SAP ERP | Accounts Payable | Critical | Yes |
| FUNC-FIN-006 | Create Journal Entry | Create | SAP ERP | General Ledger | High | Yes |
| FUNC-FIN-007 | Post Journal Entry | Execute | SAP ERP | General Ledger | High | Yes |
| FUNC-FIN-008 | Reconcile Accounts | Execute | SAP ERP | General Ledger | High | Yes |
| FUNC-IT-001 | Create User Account | Create | Active Directory | Identity Mgmt | High | Yes |
| FUNC-IT-002 | Approve Access Request | Approve | ServiceNow | Identity Mgmt | High | Yes |
| FUNC-IT-003 | Deploy to Production | Execute | Jenkins | DevOps | Critical | Yes |
| FUNC-IT-004 | Commit Code | Create | GitHub | DevOps | High | Yes |

### Step 4: Document Permissions

**Time allocation:** 4-8 hours

**Purpose:** Record technical permissions that enable functions.

**Fields to Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| Permission_ID | Unique identifier | PERM-SAP-001 |
| Function_ID | Parent function | FUNC-FIN-001 |
| Application | System | SAP ERP |
| Permission_Name | Technical name | T-Code FK01 |
| Permission_Type | Classification | Transaction / Report / API |
| Description | What it allows | Create vendor master record |
| Data_Scope | Data boundaries | Company Code 1000 |
| Special_Conditions | Constraints | Amount limit CHF 50,000 |

**Worked Example - Permissions:**

| Permission_ID | Function_ID | Application | Permission_Name | Permission_Type | Data_Scope |
|---------------|-------------|-------------|-----------------|:---------------:|------------|
| PERM-SAP-001 | FUNC-FIN-001 | SAP ERP | T-Code FK01 | Transaction | All Company Codes |
| PERM-SAP-002 | FUNC-FIN-002 | SAP ERP | T-Code FK09 | Transaction | All Company Codes |
| PERM-SAP-003 | FUNC-FIN-003 | SAP ERP | T-Code FB60 | Transaction | Company Code 1000 |
| PERM-SAP-004 | FUNC-FIN-004 | SAP ERP | T-Code FB65 | Transaction | Company Code 1000 |
| PERM-SAP-005 | FUNC-FIN-005 | SAP ERP | T-Code F110 | Transaction | All Company Codes |
| PERM-AD-001 | FUNC-IT-001 | Active Directory | Create User | API | All OUs |
| PERM-AD-002 | FUNC-IT-001 | Active Directory | Reset Password | API | All OUs |
| PERM-GH-001 | FUNC-IT-004 | GitHub | Push to main | Git | Repository X |
| PERM-JK-001 | FUNC-IT-003 | Jenkins | Deploy-Prod Job | Job | Production env |

**Permission Type Definitions:**

| Type | Description | Example |
|------|-------------|---------|
| **Transaction** | Interactive system transaction | SAP T-Code |
| **Report** | Ability to run reports | Crystal Reports |
| **API** | Programmatic access | REST API call |
| **Config** | Configuration change | System settings |
| **Data** | Direct data access | Database query |

### Step 5: Create Role-Function Map

**Time allocation:** 2-4 hours

**Purpose:** Document which roles have which functions.

**Mapping Table Structure:**

| Field | Description | Example |
|-------|-------------|---------|
| Mapping_ID | Unique identifier | MAP-001 |
| Business_Role_ID | Business role | BROLE-FIN-001 |
| App_Role_ID | Application role | AROLE-SAP-FI-001 |
| Function_ID | Function | FUNC-FIN-001 |
| Grant_Type | How granted | Direct / Inherited / Delegated / Emergency |
| Justification | Why needed | Core job duty |
| Effective_Date | When granted | 01.01.2026 |
| Expiry_Date | When expires | (blank = permanent) |

**Grant Types:**
- **Direct**: Explicitly assigned to role
- **Inherited**: Received through composite role
- **Delegated**: Temporarily assigned
- **Emergency**: Break-glass access

**Worked Example - Role-Function Map:**

| Mapping_ID | Business_Role_ID | App_Role_ID | Function_ID | Grant_Type | Justification |
|------------|------------------|-------------|-------------|:----------:|---------------|
| MAP-001 | BROLE-FIN-001 | AROLE-SAP-FI-001 | FUNC-FIN-001 | Direct | Manage vendors |
| MAP-002 | BROLE-FIN-001 | AROLE-SAP-FI-001 | FUNC-FIN-002 | Direct | Approve vendors |
| MAP-003 | BROLE-FIN-001 | AROLE-SAP-FI-001 | FUNC-FIN-004 | Direct | Approve invoices |
| MAP-004 | BROLE-FIN-001 | AROLE-SAP-FI-001 | FUNC-FIN-005 | Direct | Execute payments |
| MAP-005 | BROLE-FIN-002 | AROLE-SAP-FI-002 | FUNC-FIN-003 | Direct | Enter invoices |
| MAP-006 | BROLE-IT-001 | AROLE-AD-001 | FUNC-IT-001 | Direct | Manage users |
| MAP-007 | BROLE-IT-003 | AROLE-GH-001 | FUNC-IT-004 | Direct | Commit code |

### Step 6: Identify Function Conflicts

**Time allocation:** 2-4 hours

**Purpose:** Document which functions conflict with each other.

**Conflict Matrix at Function Level:**

| Field | Description | Example |
|-------|-------------|---------|
| Conflict_ID | Unique identifier | FCON-001 |
| Function_A | First function | FUNC-FIN-001 |
| Function_B | Second function | FUNC-FIN-005 |
| Conflict_Type | X, C, or M | X |
| Risk_Level | Criticality | Critical |
| Justification | Why conflict exists | Create vendor + Execute payment = fraud risk |
| Mitigation | Recommended control | Separate roles, dual approval |

**Conflict Types (consistent with ISMS-IMP-A.5.3.1):**
- **X**: Hard conflict - never combine
- **C**: Conditional - requires compensating controls
- **M**: Monitoring required

**Worked Example - Function Conflicts:**

| Conflict_ID | Function_A | Function_B | Conflict_Type | Risk_Level | Justification |
|-------------|------------|------------|:-------------:|:----------:|---------------|
| FCON-001 | FUNC-FIN-001 (Create Vendor) | FUNC-FIN-005 (Execute Payment) | X | Critical | Can create fake vendor and pay self |
| FCON-002 | FUNC-FIN-003 (Create Invoice) | FUNC-FIN-004 (Approve Invoice) | X | High | Self-approval of invoices |
| FCON-003 | FUNC-FIN-006 (Create JE) | FUNC-FIN-008 (Reconcile) | C | High | Can hide misstatements |
| FCON-004 | FUNC-IT-001 (Create User) | FUNC-IT-002 (Approve Access) | X | High | Self-approve elevated access |
| FCON-005 | FUNC-IT-004 (Commit Code) | FUNC-IT-003 (Deploy Prod) | X | Critical | Deploy unreviewed code |

### Step 7: Validate RBAC Configuration

**Time allocation:** 2-4 hours

**Purpose:** Compare documented mapping against actual system configuration.

**Validation Checklist:**

| Validation Point | Method | Expected Result |
|------------------|--------|-----------------|
| Role membership accurate | IAM export comparison | 100% match |
| Permission assignments correct | System audit | No undocumented permissions |
| Inherited permissions documented | Composite role analysis | All inheritances mapped |
| Data scope correctly applied | Access testing | No scope violations |
| Dormant permissions removed | Usage analysis | No unused permissions >90 days |

**Validation Status Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Validation_ID | Unique identifier | VAL-001 |
| Role_ID | Role being validated | AROLE-SAP-FI-001 |
| Validation_Date | When checked | 03.02.2026 |
| Validator | Who performed check | IT Security Analyst |
| Documented_Functions | Count from mapping | 15 |
| Actual_Functions | Count from system | 17 |
| Discrepancies | Issues found | 2 undocumented functions |
| Status | Validation result | Requires Investigation |
| Resolution | Action taken | Functions documented, approved |

**Worked Example - Validation Status:**

| Validation_ID | Role_ID | Validation_Date | Documented | Actual | Discrepancies | Status |
|---------------|---------|-----------------|:----------:|:------:|:-------------:|--------|
| VAL-001 | AROLE-SAP-FI-001 | 03.02.2026 | 15 | 15 | 0 | Validated |
| VAL-002 | AROLE-SAP-FI-002 | 03.02.2026 | 8 | 10 | 2 | Requires Investigation |
| VAL-003 | AROLE-AD-001 | 03.02.2026 | 12 | 12 | 0 | Validated |
| VAL-004 | AROLE-SQL-001 | 03.02.2026 | 20 | 18 | 2 | Remediated |

### After Completing the Mapping Sheets

Once Steps 1–7 are complete:

- **Change Log** — This sheet is an ongoing responsibility, not a one-time activity. Record every permission or mapping change as it occurs: the date, the role or function affected, the nature of the change, who approved it, and who implemented it. An up-to-date Change Log demonstrates active access governance and is key audit evidence. Start populating it from Day 1 of your mapping effort and continue throughout the year.
- **Summary Dashboard** — Review the dashboard for an executive summary of mapping completeness, validation status, and function-level conflict counts. It aggregates data from your completed sheets automatically. Review it before initiating the approval workflow to confirm the metrics reflect your current state.

---

## Function-Level Conflict Analysis

### Identifying Hidden Conflicts

Function-level analysis reveals conflicts invisible at role level:

**Example: The Override Problem**

| Role | Functions |
|------|-----------|
| Buyer | Create PO, Submit PO |
| Buyer Manager | Approve PO, Override Approval Limit |

At role level: No apparent conflict (different roles)
At function level: "Override Approval Limit" allows buyer manager to approve without limit, potentially creating self-dealing opportunity if same person is temporarily assigned Buyer role.

**Example: The Composite Role Problem**

| Composite Role | Contains |
|----------------|----------|
| Finance Power User | AP Clerk Role + AR Clerk Role + GL Role |

Individual roles may be non-conflicting, but composite role creates conflicts because one person now has create + approve + reconcile functions.

**Example: The Inherited Permission Problem**

| Role | Direct Functions | Inherited Functions |
|------|-----------------|---------------------|
| Senior Developer | Code Review | Code Commit (from Developer role) |

If Senior Developer role is built on Developer role, they inherit code commit permissions plus have review authority - can review and commit their own code.

### Transaction-Level Analysis (SAP Example)

For SAP environments, analyse transaction code combinations:

| T-Code 1 | T-Code 2 | Conflict | Risk |
|----------|----------|:--------:|------|
| FK01 (Create Vendor) | F110 (Payment Run) | X | Fake vendor payment |
| ME21N (Create PO) | MIGO (Goods Receipt) | C | Inventory theft |
| SU01 (User Admin) | SM21 (Log Display) | X | Admin + audit |
| FB01 (Post Document) | FBL3N (GL Line Items) | M | Post and view |
| PA40 (Personnel Actions) | PC00_M99_CALC (Payroll) | X | Change pay and process |

### Critical Function Combinations

**Financial Systems:**

| Function 1 | Function 2 | Risk | Control |
|------------|------------|------|---------|
| Create vendor master | Approve vendor payments | Fictitious vendor fraud | Separate roles |
| Enter invoices | Approve invoices | Inflated payments | Dual approval |
| Create journal entries | Post to GL | Financial misstatement | Second reviewer |
| Bank reconciliation | Cash handling | Embezzlement | Independent reconciliation |

**IT Systems:**

| Function 1 | Function 2 | Risk | Control |
|------------|------------|------|---------|
| Write code | Deploy to production | Malicious code | CI/CD with approvals |
| Create user accounts | Assign permissions | Privilege escalation | Separate admins |
| Administer systems | Review audit logs | Evidence destruction | Log forwarding |
| Change configurations | Approve changes | Unauthorised changes | CAB process |

---

## Evidence Collection

### Evidence Requirements

| Evidence Type | Source | Retention |
|---------------|--------|-----------|
| Role-Function Mapping Workbook | Generated | 7 years |
| System role exports | IAM/Applications | 3 years |
| Validation test results | Testing process | 3 years |
| Permission change logs | Applications | 3 years |
| Composite role analysis | Security team | 3 years |
| Dormant permission reports | IAM/Usage analytics | 3 years |

### Evidence Storage

**Primary Location:** `[SharePoint/Evidence Library]/A.5.3/Role-Function-Mapping/[Year]/`

**Folder Structure:**
```
A.5.3/
|-- Role-Function-Mapping/
|   |-- 2026/
|   |   |-- Assessment-Workbooks/
|   |   |   |-- ISMS-IMP-A.5.3.3_Role_Function_Mapping_20260203.xlsx
|   |   |-- System-Exports/
|   |   |   |-- SAP-Role-Export-20260203.xlsx
|   |   |   |-- AD-Group-Membership-20260203.csv
|   |   |   |-- ServiceNow-Roles-20260203.pdf
|   |   |-- Validation/
|   |   |   |-- Validation-Test-Results-Q1-2026.xlsx
|   |   |   |-- Discrepancy-Resolution-Log.xlsx
|   |   |-- Change-History/
|   |   |   |-- Permission-Changes-2026.xlsx
|   |   |   |-- Change-Approval-Records/
```

**Naming Convention:**
```
EVD-A.5.3.3_[EvidenceType]_[Reference]_[YYYYMMDD].[ext]
```

---

## Common Pitfalls

Avoid these common mistakes when completing the Role-Function Mapping:

### Mapping Completeness Pitfalls

❌ **MISTAKE**: Mapping only at the business role level
✅ **CORRECT**: Map down to application role, function, and permission level for complete visibility; surface-level mapping misses critical details

❌ **MISTAKE**: Not documenting inherited permissions from composite roles
✅ **CORRECT**: Explode composite roles to show all inherited functions; composite roles often contain hidden conflicts

❌ **MISTAKE**: Missing application-specific roles not in central IAM
✅ **CORRECT**: Inventory roles in all applications, including those with local role management (databases, legacy systems, cloud applications)

❌ **MISTAKE**: Only mapping production systems
✅ **CORRECT**: Include test/dev systems if they contain sensitive data or can promote to production; dev access often leads to prod access

### Validation Pitfalls

❌ **MISTAKE**: Assuming documented RBAC matches actual configuration
✅ **CORRECT**: Validate mapping against actual system configuration periodically; role definitions drift over time

❌ **MISTAKE**: Validating only once during initial mapping
✅ **CORRECT**: Re-validate quarterly or after significant system changes; permissions change more often than expected

❌ **MISTAKE**: Not investigating discrepancies
✅ **CORRECT**: Every discrepancy between documentation and system configuration must be investigated and resolved; discrepancies indicate control failures

❌ **MISTAKE**: Accepting "it's always been that way" for unexplained permissions
✅ **CORRECT**: Challenge all permissions without documented business justification; legacy permissions often violate current security requirements

### Function Analysis Pitfalls

❌ **MISTAKE**: Not identifying function-level conflicts
✅ **CORRECT**: Analyse conflicts at function level, not just role level; many significant conflicts exist within composite roles

❌ **MISTAKE**: Treating all permissions equally regardless of data scope
✅ **CORRECT**: Document data scope limitations - a permission limited to test data is lower risk than production data access

❌ **MISTAKE**: Not considering indirect function access
✅ **CORRECT**: Include API access, reporting permissions, and export capabilities that provide equivalent function access through different paths

❌ **MISTAKE**: Ignoring "read-only" permissions in conflict analysis
✅ **CORRECT**: Read access to sensitive data combined with other permissions can create conflicts (e.g., view salary + modify own record)

### Change Management Pitfalls

❌ **MISTAKE**: Not updating mapping when roles change
✅ **CORRECT**: Integrate mapping updates into role change process; mapping must be updated within 24 hours of permission changes

❌ **MISTAKE**: No change log maintenance
✅ **CORRECT**: Maintain change log for audit trail and trend analysis; undocumented changes indicate control failures

❌ **MISTAKE**: Using outdated application documentation
✅ **CORRECT**: Verify function definitions against current system version; application upgrades often change permission behaviours

❌ **MISTAKE**: Not tracking permission removal
✅ **CORRECT**: Log permission removals as well as additions; removal patterns reveal access review effectiveness

### Documentation Pitfalls

❌ **MISTAKE**: Skipping dormant permission analysis
✅ **CORRECT**: Identify and investigate permissions not used in 90+ days; unused permissions increase attack surface without business value

❌ **MISTAKE**: Not documenting data scope restrictions
✅ **CORRECT**: Data scope is critical for risk assessment; a permission limited to specific data sets is lower risk

❌ **MISTAKE**: Generic function descriptions
✅ **CORRECT**: Function descriptions must be specific enough to enable conflict analysis; "access to finance system" is not sufficient

❌ **MISTAKE**: Not linking to source RBAC documentation
✅ **CORRECT**: Reference authoritative RBAC documentation; mapping should trace back to official role definitions

---

## Quality Checklist

Before submitting the completed workbook, verify all items:

### Completeness Checks

- [ ] All business roles in scope documented
- [ ] All application roles mapped to business roles
- [ ] All functions documented with categories
- [ ] All permissions linked to functions
- [ ] Role-Function map complete for all roles
- [ ] Function conflicts identified and documented
- [ ] Composite roles exploded to show inherited functions

### Coverage Checks

- [ ] All critical applications included
- [ ] SAP/ERP roles fully mapped
- [ ] Active Directory groups included
- [ ] Database roles included
- [ ] Cloud application roles included
- [ ] Service accounts documented
- [ ] Emergency access roles included

### Accuracy Checks

- [ ] Mapping validated against system exports
- [ ] Discrepancies investigated and resolved
- [ ] Composite roles exploded correctly
- [ ] Data scopes accurately documented
- [ ] Function categories consistently applied
- [ ] Conflict classifications reviewed by process owners

### Documentation Checks

- [ ] All fields populated (no blank required fields)
- [ ] Change log maintained
- [ ] Evidence of validation stored
- [ ] Function conflicts reference ISMS-IMP-A.5.3.1 classifications
- [ ] All required attachments present
- [ ] Naming conventions followed

### Process Checks

- [ ] Application administrators validated their systems
- [ ] Process owners confirmed function-to-process mapping
- [ ] IT Security reviewed technical accuracy
- [ ] Internal Audit validated independently
- [ ] CISO approved final mapping
- [ ] Workbook saved with correct naming convention

### Validation Checks

- [ ] All application roles validated against systems
- [ ] Zero discrepancies or all discrepancies resolved
- [ ] Validation dates within acceptable period
- [ ] Validation evidence stored

---

## Review and Approval

### Review Workflow

| Step | Role | Responsibility | Timeline |
|------|------|----------------|----------|
| 1 | Mapping Lead | Complete all sheets | By deadline |
| 2 | Application Admins | Validate technical accuracy | 5 business days |
| 3 | Process Owners | Validate business context | 5 business days |
| 4 | IT Security | Security review | 3 business days |
| 5 | Internal Audit | Independent validation | 5 business days |
| 6 | CISO | Final approval | 3 business days |

### Approval Workflow

```
Mapping Lead Completes
        │
        ▼
Self-Review (Quality Checklist)
        │
        ▼
Application Admins Validate ─────► Return for Corrections
        │                                │
        ▼                                │
Process Owners Confirm ──────────► Return for Corrections
        │                                │
        ▼                                │
IT Security Review ──────────────► Return for Corrections
        │                                │
        ▼                                │
Internal Audit Validation ───────► Return for Corrections
        │                                │
        ▼                                │
CISO Final Approval ─────────────────────┘
        │
        ▼
   Mapping Complete
        │
        ▼
   Upload to ISMS Evidence Library
```

### Post-Approval Actions

Upon approval:

1. Upload completed workbook to ISMS Evidence Library
2. Update ISMS control status
3. Communicate function conflicts to A.5.3.1 assessment
4. Schedule next validation cycle
5. Communicate function conflict data to related assessments (ISMS-IMP-A.5.3.1 and A.5.3.2) as required
6. Integrate Change Log updates into the ongoing permission change process

---

**END OF USER GUIDE**

---

*"Form ever follows function."*
— Louis Sullivan

<!-- QA_VERIFIED: 2026-03-01 -->
