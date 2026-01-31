# ISMS-POL-A.5.15-16-18-S3: Identity Management (A.5.16)
## Identity Lifecycle Governance Framework

**Document ID**: ISMS-POL-A.5.15-16-18-S3  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Active

---

## Document Purpose

This section defines **identity management requirements** implementing ISO/IEC 27001:2022 Control A.5.16. It establishes the lifecycle framework governing HOW user identities are created, maintained, and removed throughout their entire existence.

---

## 1. Control Objective & Scope

### 1.1 ISO 27001:2022 Control A.5.16 - Identity Management

**Official Control Text (German)**:
> Der gesamte Lebenszyklus von Identitäten sollte verwaltet werden.

**English Translation**:
> The full life cycle of identities should be managed.

**Control Objective**:
Ensure user identities are systematically managed from creation through removal, preventing:
- Orphaned accounts (accounts without valid owners)
- Delayed provisioning (new users cannot work)
- Delayed deprovisioning (terminated users retain access)
- Identity data inaccuracies (wrong manager, department, etc.)
- Uncontrolled account proliferation (multiple accounts per person)

**Scope of A.5.16 Requirements**:
This section covers the **identity lifecycle management layer**:
- ✅ Joiner process (new user account creation and initial access)
- ✅ Mover process (role change, department transfer, access modification)
- ✅ Leaver process (termination, account disablement, access removal)
- ✅ Account type management (employees, contractors, vendors, service accounts)
- ✅ Identity repository management (authoritative source, synchronization)
- ✅ Orphaned account detection and remediation
- ✅ Contractor/vendor identity management (time-bound, sponsored)

**Out of Scope** (covered in other controls):
- ❌ Access control policy framework → A.5.15 (Access Control)
- ❌ Access rights assignment procedures → A.5.18 (Access Rights)
- ❌ Authentication mechanisms → A.8.5 (Secure Authentication)
- ❌ Privileged account management → A.8.2 (Privileged Access Rights)

---

### 1.2 Why Identity Lifecycle Management Matters

**The orphaned account problem**:
- Average organization: **15-30% of accounts belong to former employees or contractors**
- Typical scenario: Employee terminated on Friday → IT not notified → account active for months
- Security risk: Attackers target orphaned accounts (no one monitors, no one notices compromise)

**The provisioning delay problem**:
- New employee starts Monday → no access to systems → cannot perform job
- Frustration, productivity loss, manual workarounds (shared accounts, passwords emailed)
- Shadow IT: Users create unauthorized accounts when official process too slow

**The privilege creep problem**:
- Employee hired as "Junior Analyst" → promoted to "Senior Analyst" → then "Manager"
- Each role change: New access added, old access never removed
- Result: Manager has access accumulated from 3 previous roles (excessive privileges)

**This framework addresses**:
- **Timely provisioning**: Access ready by employee start date (no delays)
- **Timely deprovisioning**: Access removed within 24 hours of termination (no orphaned accounts)
- **Clean role changes**: Old role access removed when new role granted (no privilege creep)
- **Automated lifecycle**: HR system drives identity processes (not manual tickets)
- **Continuous cleanup**: Monthly orphaned account scans and remediation

---

## 2. Identity Lifecycle Framework

### REQ-A516-001: Joiner Process Defined

**Requirement**:
> Systematic process for creating identities and granting initial access when new users join.

**Joiner Process Triggers**:
- New employee hired (HR system creates employee record)
- New contractor engaged (sponsor submits contractor request)
- New vendor requires access (vendor access request approved)
- New partner collaboration (partnership agreement signed)

**Joiner Process Stages**:
1. **Identity Creation**: User account created in identity repository (AD, Azure AD, Okta)
2. **Attribute Population**: User attributes populated (name, email, department, manager, job title)
3. **Initial Access Assignment**: Standard access granted based on role (per RBAC framework)
4. **Account Activation**: Account enabled, welcome email sent
5. **Verification**: Provisioning timeliness measured (access ready by start date?)

**Success Criteria**:
- Access ready by employee start date (≥95% on-time provisioning)
- User attributes accurate (name, email, department correct)
- Standard role access granted (no manual access requests needed for day-1 systems)

---

### REQ-A516-002: Mover Process Defined

**Requirement**:
> Systematic process for modifying identities and access when users change roles or departments.

**Mover Process Triggers**:
- Employee promotion (job title change in HR system)
- Department transfer (department change in HR system)
- Role change (job function change requiring different access)
- Manager change (reporting structure change)

**Mover Process Stages**:
1. **Identity Update**: User attributes updated (department, manager, job title)
2. **Old Access Review**: Access review triggered → old role access evaluated
3. **Access Modification**: Old role access removed (if no longer needed), new role access granted
4. **Verification**: Access aligned with new role (no privilege creep)

**Success Criteria**:
- User attributes updated within 1 business day of HR system change
- Old role access removed (not accumulated with new role access)
- New role access granted within 1 business day
- Access review confirms access matches current role

**Common Pitfall**: Additive access (new access granted, old access retained) = privilege creep

---

### REQ-A516-003: Leaver Process Defined

**Requirement**:
> Systematic process for disabling identities and removing all access when users leave.

**Leaver Process Triggers**:
- Employee termination (HR system updates termination date)
- Employee resignation (last working day in HR system)
- Contractor contract end (contract end date reached)
- Vendor contract termination (vendor access no longer needed)

**Leaver Process Stages**:
1. **Account Disablement**: User account disabled (login prevented)
2. **Access Removal**: All access rights revoked (group memberships removed)
3. **Data Handover**: Email/files transferred to manager (if applicable)
4. **Account Deletion**: Account deleted after retention period (typically 90 days)
5. **Verification**: Deprovisioning timeliness measured (disabled within 24 hours?)

**Success Criteria**:
- Account disabled within required timeframe (see REQ-A516-021)
- All access removed (verified via audit log)
- Manager notified of deprovisioning completion
- ≥98% on-time deprovisioning (critical security metric)

---

### REQ-A516-004: Lifecycle Stages Documented

**Requirement**:
> All identity lifecycle stages must be documented with clear ownership, timelines, and verification.

**Documentation Requirements**:
- Joiner process workflow diagram (trigger → stages → verification)
- Mover process workflow diagram
- Leaver process workflow diagram
- Role assignments (who performs each stage)
- Timeline requirements (SLAs for each stage)
- Verification procedures (how to confirm completion)

**Lifecycle Stage Ownership**:
| Stage | Owner | SLA | Verification |
|-------|-------|-----|--------------|
| **Joiner - Account Creation** | IT Operations | By start date | Account exists in identity system |
| **Joiner - Initial Access** | IT Operations | By start date | User can log in, access standard systems |
| **Mover - Access Review** | Manager | 1 business day | Access aligned with new role |
| **Mover - Access Modification** | IT Operations | 1 business day | Old access removed, new access granted |
| **Leaver - Account Disable** | IT Operations | Within 24 hours (termination) | Account disabled (login fails) |
| **Leaver - Access Removal** | IT Operations | Within 24 hours (termination) | All group memberships removed |

---

## 3. User Account Provisioning Requirements

### REQ-A516-010: HR System as Authoritative Source

**Requirement**:
> HR system is the **authoritative source of truth** for employee identity data. Identity provisioning triggered by HR system updates.

**HR System Contains**:
- Employee hire date, termination date
- Full name, email address (if assigned)
- Department, job title, manager
- Employment type (full-time, part-time, contractor)
- Employee status (active, on leave, terminated)

**Implementation**:
- Identity system (AD, Azure AD, Okta) synchronizes with HR system
- Sync frequency: Real-time (preferred) or daily batch
- Sync failures detected and escalated immediately
- Manual account creation discouraged (bypasses lifecycle controls)

**Example**:
- HR system: Employee "Alice Anderson" hired 2026-01-15, Department "Finance", Manager "Bob Brown"
- Identity sync: Creates "alice.anderson@example.com" in Azure AD, populates attributes
- Access provisioning: Grants "Finance Analyst" role access (per RBAC)
- Result: Alice can log in on 2026-01-15 (start date)

---

### REQ-A516-011: Provisioning Timeliness Requirements

**Requirement**:
> User accounts must be provisioned with appropriate access **by the employee start date**. Late provisioning = business disruption.

**Provisioning Timeliness Targets**:

| User Type | Provisioning Deadline | Rationale |
|-----------|----------------------|-----------|
| **Employee** | By hire date (Day 0) | Employee must be productive on Day 1 |
| **Contractor** | By contract start date (Day 0) | Contractor billable hours start immediately |
| **Vendor** | Within 2 business days of approval | Vendor access less time-critical |
| **Emergency** | Same day (within 4 hours) | Critical business need |

**Calculation**:
- Provisioning Delay = Provision Date - Hire Date (in days)
- **On-time**: Delay ≤ 0 days (access ready by start date or earlier)
- **Late**: Delay > 0 days (access not ready, employee cannot work)

**Compliance Target**: ≥95% on-time provisioning

**Example**:
- Employee: Hire Date = 2026-01-15, Account Created = 2026-01-14
- Provisioning Delay = 2026-01-14 minus 2026-01-15 = -1 day (1 day early)
- Status: **On-time** ✅ (access ready before start date)

**Example (Late)**:
- Employee: Hire Date = 2026-01-15, Account Created = 2026-01-17
- Provisioning Delay = 2026-01-17 minus 2026-01-15 = +2 days (2 days late)
- Status: **Late** ❌ (employee waited 2 days without access)

---

### REQ-A516-012: Account Creation Workflow

**Requirement**:
> Account creation workflow must be documented and automated where possible.

**Automated Workflow** (Preferred):
1. HR system updated (new employee record created, hire date set)
2. Identity provisioning system detects new employee (real-time or daily sync)
3. Account created automatically in identity repository (AD, Azure AD, Okta)
4. User attributes populated from HR data (name, email, department, manager)
5. Standard role access granted (per RBAC framework based on job title)
6. Welcome email sent to user (login credentials, instructions)
7. Manager notified (new employee account ready)

**Manual Workflow** (If automation not available):
1. IT receives new hire notification from HR
2. IT creates account manually (using standard naming convention)
3. IT populates user attributes (from HR data)
4. IT grants standard access (per role definition)
5. IT sends welcome email
6. IT logs provisioning completion in ticketing system

**Automation Benefits**:
- Faster provisioning (real-time vs. manual delays)
- Fewer errors (no manual data entry)
- Auditability (automated logs)
- Scalability (handles high-volume hiring)

---

### REQ-A516-013: Initial Access Assignment

**Requirement**:
> New users must receive **standard access based on role** without requiring individual access requests.

**Standard Access Definition**:
- Access required for all users in a specific role (e.g., "Financial Analyst" role)
- Includes: Email, file shares, standard business applications, collaboration tools
- Excludes: Sensitive systems requiring additional approval (per A.5.15 access control policy)

**Implementation**:
- Role catalog defines standard access per role (per A.5.18 RBAC framework)
- Identity provisioning system grants standard access automatically
- Non-standard access requested separately (access request workflow per A.5.15)

**Example - Financial Analyst Role**:
- Standard access granted automatically:
  - Microsoft 365 (email, Teams, SharePoint)
  - Finance file share (department shared drive)
  - Finance reporting tool (read-only)
  - ERP system (finance module, standard user)
- Non-standard access (requires manager approval):
  - ERP admin access (elevated privilege)
  - Restricted finance data (merger/acquisition data)

---

### REQ-A516-014: Account Activation Procedures

**Requirement**:
> Account activation must be completed and verified before employee start date.

**Activation Checklist**:
- [ ] Account created in identity repository
- [ ] User attributes accurate (name, email, department, manager)
- [ ] Standard role access granted
- [ ] Account enabled (not disabled/locked)
- [ ] Password set (temporary password or self-service enrollment)
- [ ] Welcome email sent (login instructions)
- [ ] Verification: User can successfully log in

**Testing**:
- IT performs login test before start date (verify account works)
- If login fails: Troubleshoot and resolve before start date

---

### REQ-A516-015: Welcome Email Requirements

**Requirement**:
> New users must receive welcome email with access instructions.

**Welcome Email Contents**:
- Greeting and company welcome message
- Username (e.g., "alice.anderson@example.com")
- Password reset instructions (link to self-service password reset)
- Login URL (e.g., company portal, VPN portal)
- IT support contact information (help desk)
- Acceptable use policy acknowledgment (link to AUP)
- Multi-factor authentication (MFA) enrollment instructions (if required)

**Timing**: Welcome email sent 1-2 business days before start date (user can prepare)

---

## 4. User Account Deprovisioning Requirements

### REQ-A516-020: HR-Driven Deprovisioning

**Requirement**:
> Account deprovisioning triggered automatically by HR system termination date update.

**Deprovisioning Triggers**:
- HR system termination date reached (automated trigger)
- Manual termination notification (emergency termination, HR system lag)
- Contractor contract end date reached (automated expiration)
- Vendor access removal request (sponsor-initiated)

**Preferred**: Automated trigger from HR system (real-time or daily sync)

**Example**:
- HR system: Employee "Bob Brown" terminated 2026-01-15
- Identity sync: Detects termination date reached
- Automated workflow: Disable account on 2026-01-15 (termination date)
- Result: Bob's account disabled same day (cannot log in)

---

### REQ-A516-021: Deprovisioning Timeliness Requirements

**Requirement**:
> User accounts must be disabled **immediately upon termination**. Delayed deprovisioning = security risk.

**Deprovisioning Timeliness Targets**:

| Termination Type | Deprovisioning Deadline | Rationale |
|------------------|-------------------------|-----------|
| **Involuntary Termination** (fired) | Within 1 hour | High security risk (disgruntled employee) |
| **Voluntary Resignation** (last working day) | End of last working day | Lower risk (planned departure) |
| **Contractor Contract End** | Contract end date | Predictable (contract end date known) |
| **Leave of Absence** | Start of leave | Temporary (account disabled, not deleted) |

**Calculation**:
- Deprovisioning Delay = Disable Date - Termination Date (in days)
- **On-time**: Delay ≤ 1 day (disabled within 24 hours)
- **Late**: Delay > 1 day (security risk, account active too long)

**Compliance Target**: ≥98% on-time deprovisioning (higher than provisioning due to security criticality)

**Example**:
- Employee: Termination Date = 2026-01-15, Account Disabled = 2026-01-15 09:00
- Deprovisioning Delay = 0 days (same day)
- Status: **On-time** ✅

**Example (Late)**:
- Employee: Termination Date = 2026-01-15, Account Disabled = 2026-01-18
- Deprovisioning Delay = +3 days (3 days late)
- Status: **Late** ❌ (security risk, terminated employee had access for 3 days)

---

### REQ-A516-022: Account Disablement vs. Deletion

**Requirement**:
> Accounts must be **disabled immediately**, then **deleted after retention period**.

**Two-Stage Deprovisioning**:

**Stage 1: Immediate Disablement**
- Action: Account disabled (login prevented, authentication fails)
- Timing: Termination date (or within 1 hour for involuntary termination)
- Purpose: Prevent unauthorized access immediately
- Account status: Disabled (still exists, but inactive)

**Stage 2: Delayed Deletion**
- Action: Account permanently deleted
- Timing: 90 days after disablement (retention period)
- Purpose: Allow data recovery if needed, comply with legal hold
- Account status: Deleted (no longer exists)

**Rationale for Two Stages**:
- Immediate disablement addresses security (no access)
- Delayed deletion addresses operational needs (data recovery, audit trail, legal hold)

**Example**:
- Employee terminated: 2026-01-15
- Account disabled: 2026-01-15 (immediate)
- Account deleted: 2026-04-15 (90 days later)

**Exception - Legal Hold**:
- If employee subject to legal investigation: Account NOT deleted until legal hold released
- Account remains disabled but not deleted indefinitely

---

### REQ-A516-023: Access Removal Verification

**Requirement**:
> Access removal must be verified via audit log to ensure complete deprovisioning.

**Verification Checklist**:
- [ ] Account disabled (login fails)
- [ ] All group memberships removed (no lingering access via groups)
- [ ] All application access removed (SaaS applications, databases)
- [ ] VPN access removed (remote access disabled)
- [ ] Email forwarding configured (if applicable, emails forwarded to manager)
- [ ] Verification logged in audit trail

**Automated Verification** (Preferred):
- Identity system logs account disablement event
- Automated script verifies all access removed (checks group memberships, application access)
- Verification report generated (confirms complete deprovisioning)

**Manual Verification** (If automation not available):
- IT manually checks account status
- IT confirms group memberships removed
- IT confirms application access removed
- IT documents verification in ticket

---

### REQ-A516-024: Data Handover Procedures

**Requirement**:
> Terminated employee data (email, files) must be transferred to manager before final account deletion.

**Data Handover Workflow**:
1. **Email**: Convert mailbox to shared mailbox OR export to PST file
2. **Files**: Transfer ownership of files to manager OR designated successor
3. **Applications**: Transfer application data ownership (CRM records, project files)
4. **Verification**: Manager confirms data handover complete

**Timing**:
- Data handover requested during deprovisioning workflow
- Completed within 5 business days of termination
- Account deletion delayed until data handover confirmed

**Example**:
- Employee terminated: 2026-01-15
- Email converted to shared mailbox: 2026-01-17 (manager can access)
- OneDrive files transferred to manager: 2026-01-18
- Data handover complete: 2026-01-20
- Account deletion scheduled: 2026-04-15 (90 days after disablement)

---

### REQ-A516-025: Manager Notification

**Requirement**:
> Manager must be notified when employee account deprovisioned.

**Notification Contents**:
- Employee name, termination date
- Account disablement confirmation
- Data handover status (complete or in progress)
- Reminder: Review employee's access (identify any shared accounts or exceptions)

**Purpose**: Ensure manager aware of deprovisioning, can plan for data handover and role coverage

---

## 5. Account Type Requirements

### REQ-A516-030: Employee Accounts

**Definition**: Standard user accounts for internal staff (full-time, part-time employees).

**Characteristics**:
- **Linked to HR system**: Employee record is authoritative source
- **Standard lifecycle**: Joiner/mover/leaver processes apply
- **Naming convention**: firstname.lastname@example.com (standard format)
- **Account type identifier**: "Employee" attribute in identity system
- **No expiration date**: Active until employee terminates

**Provisioning**:
- Triggered by HR system (new hire record)
- Standard access granted based on job title/role
- Manager approval required for non-standard access

**Deprovisioning**:
- Triggered by HR system (termination date)
- Disabled within 24 hours of termination
- Deleted after 90-day retention period

---

### REQ-A516-031: Contractor/Vendor Accounts

**Definition**: Time-bound accounts for temporary workers and third-party service providers.

**Characteristics**:
- **Sponsored**: Internal employee assigned as sponsor (accountable for contractor access)
- **Time-bound**: Contract start/end date documented, automatic expiration
- **External identifier**: Username prefixed with "EXT-" or "CTR-" (e.g., "EXT-vendor.name@example.com")
- **Account type identifier**: "Contractor" or "Vendor" attribute in identity system
- **Automatic expiration**: Account auto-disables on contract end date

**Provisioning**:
- Sponsor submits contractor access request
- Contract start/end dates documented
- Sponsor's manager approves request
- Security team approves (enhanced review for third-party access)
- Account created with expiration date

**Deprovisioning**:
- Automatic: Account disabled on contract end date
- Manual: Sponsor requests early termination
- Verification: Sponsor notified 30 days before expiration (opportunity to extend)

**Example**:
- Contractor: "Jane Doe", Company "ACME Consulting"
- Contract period: 2026-01-01 to 2026-06-30
- Sponsor: "Bob Brown" (internal employee)
- Account: "EXT-jane.doe@example.com"
- Expiration date: 2026-06-30 (auto-disable)
- Sponsor notification: 2026-05-30 (30 days before expiration)

---

### REQ-A516-032: Service Accounts

**Definition**: Non-human accounts used by applications, systems, or automated processes.

**Characteristics**:
- **Non-interactive**: Not used for human login (application/system use only)
- **Owner assigned**: Person designated as account owner (responsible for account)
- **Purpose documented**: Service account purpose clearly documented
- **No expiration date**: Active until service decommissioned
- **Privileged service accounts**: Special handling required (per A.8.2 privileged access)

**Service Account Naming Convention**:
- `svc-[purpose]` (e.g., "svc-backup", "svc-database", "svc-monitoring")
- Clearly identifies as service account (not human)

**Provisioning**:
- Service account request submitted by application owner
- Request includes: Purpose, owner, systems accessed, privilege level
- Security team approves (especially for privileged service accounts)
- Owner documented in identity system

**Password Management**:
- Service account passwords stored in password vault (not shared)
- Password rotation: Every 90 days (or per service requirements)
- Privileged service accounts: Password rotation enforced (automated)

**Deprovisioning**:
- Triggered when service decommissioned
- Owner confirms service account no longer needed
- Account disabled, then deleted after 30 days

**Example**:
- Service Account: "svc-backup"
- Purpose: "Automated backup service for file servers"
- Owner: "Alice Anderson" (Backup Administrator)
- Privilege: Domain Admin (high privilege)
- Password: Stored in CyberArk password vault
- Rotation: Every 90 days (automated)

---

### REQ-A516-033: Shared Accounts

**Definition**: Accounts used by multiple people (discouraged but sometimes necessary).

**Policy**: Shared accounts are **discouraged** due to accountability concerns. Use only when technically infeasible to use individual accounts.

**When Shared Accounts Allowed**:
- ✅ Generic application accounts (e.g., "admin" account for legacy system)
- ✅ Emergency break-glass accounts (disaster recovery)
- ✅ Equipment login (e.g., shared kiosk)
- ❌ Convenience (multiple users want same access) - NOT valid justification

**Requirements for Shared Accounts**:
- **Business justification required**: Why individual accounts not feasible?
- **Approval required**: CISO approval for all shared accounts
- **Users documented**: List of all people who use shared account
- **Enhanced monitoring**: All actions logged and reviewed
- **Password management**: Password stored in password vault, rotated frequently

**Example**:
- Shared Account: "admin" (legacy mainframe system)
- Justification: "Mainframe system does not support individual user accounts"
- Users: Alice Anderson, Bob Brown, Charlie Clark (IT Operations)
- Approval: CISO approved 2026-01-10
- Monitoring: All mainframe actions logged, reviewed weekly by Security team
- Password: Stored in password vault, rotated every 30 days

---

### REQ-A516-034: Emergency/Break-Glass Accounts

**Definition**: Accounts for disaster recovery scenarios when normal authentication systems unavailable.

**Characteristics**:
- **Emergency use only**: Used when primary authentication systems down
- **Restricted access**: Password stored in secure vault, accessible only to authorized personnel
- **Usage triggers investigation**: Any use of break-glass account triggers incident investigation
- **After-the-fact justification**: User must provide written justification within 24 hours

**Break-Glass Account Examples**:
- `EMERG-ADMIN` (emergency domain admin account)
- `BREAK-GLASS-ROOT` (emergency root access for critical systems)

**Provisioning**:
- Break-glass accounts created during system deployment
- Password stored in physical safe OR password vault with strict access controls
- Access restricted to: CISO, IT Director, designated emergency responders

**Usage Procedure**:
1. Emergency situation declared (e.g., authentication system outage)
2. Authorized person retrieves break-glass password from vault
3. Logs in using break-glass account
4. Performs emergency actions (restore authentication system)
5. Documents all actions taken
6. Submits written justification to CISO within 24 hours
7. Password rotated immediately after use

**Monitoring**:
- Break-glass account usage logged
- Security team receives real-time alert on break-glass usage
- Post-incident review conducted (was usage justified?)

---

## 6. Identity Repository Requirements

### REQ-A516-040: Authoritative Source of Truth

**Requirement**:
> HR system is the **authoritative source** for employee identity data. All identity systems synchronize from HR.

**HR System as Source of Truth**:
- Employee hire date, termination date
- Full name, employee ID
- Department, job title, manager
- Employment type (full-time, part-time, contractor)
- Work location

**Identity System Synchronization**:
- Active Directory (AD): Synchronizes from HR system
- Azure AD: Synchronizes from HR system OR from AD
- Okta: Synchronizes from HR system
- Google Workspace: Synchronizes from HR system

**Data Flow**:
```
HR System (Authoritative Source)
    ↓
Active Directory (On-Prem)
    ↓
Azure AD (Cloud) [via Azure AD Connect]
    ↓
Cloud Applications (via federation/SCIM)
```

---

### REQ-A516-041: Identity Synchronization

**Requirement**:
> Identity data must be synchronized from HR system to all identity repositories with minimal latency.

**Synchronization Frequency**:
| Sync Type | Frequency | Latency | Use Case |
|-----------|-----------|---------|----------|
| **Real-Time** | Immediate (event-driven) | <1 minute | Preferred for terminations (immediate access removal) |
| **Near Real-Time** | Every 15 minutes | <15 minutes | Acceptable for most use cases |
| **Daily Batch** | Once per day (overnight) | ~12 hours | Minimum acceptable (legacy systems) |

**Preferred**: Real-time or near real-time synchronization (event-driven)

**Sync Failure Detection**:
- Synchronization errors logged
- IT receives alert when sync fails
- Failed syncs retried automatically
- Manual intervention if persistent failure

**Example**:
- HR system: Employee "Alice Anderson" hired 2026-01-15
- Sync frequency: Real-time (event-driven)
- Active Directory: User created within 1 minute
- Azure AD: User synchronized within 2 minutes (via Azure AD Connect)
- Result: Alice can log in on 2026-01-15 (start date)

---

### REQ-A516-042: Identity Data Accuracy

**Requirement**:
> User attributes (name, email, department, manager) must be accurate and up-to-date.

**User Attributes Maintained**:
- Full name (first name, last name)
- Email address (primary contact)
- Department (organizational unit)
- Manager (reporting relationship)
- Job title (role/position)
- Work location (office, city, country)
- Employee type (employee, contractor, vendor)
- Status (active, on leave, terminated)

**Data Quality Monitoring**:
- Monthly data quality report (% users with complete attributes)
- Missing attributes flagged (e.g., users without manager)
- Inaccurate attributes corrected (e.g., wrong department)

**Data Update Process**:
- HR system updated (authoritative source)
- Changes synchronized to identity systems automatically
- Verification: User attributes match HR system (monthly audit sample)

---

### REQ-A516-043: Multiple Identity Systems Consistency

**Requirement**:
> When multiple identity systems exist (AD, Azure AD, Okta), identity data must be consistent across systems.

**Common Hybrid Architecture**:
- Active Directory (on-premises) ← Synchronizes from HR
- Azure Active Directory (cloud) ← Synchronizes from AD (via Azure AD Connect)
- Cloud Applications (Okta, Google) ← Synchronizes from Azure AD OR directly from HR

**Consistency Requirements**:
- User exists in AD → must exist in Azure AD (synchronized)
- User disabled in AD → must be disabled in Azure AD (synchronized)
- User attributes match across systems (same name, email, department)

**Conflict Resolution**:
- HR system is authoritative (HR data wins in conflicts)
- Identity system updates NOT written back to HR (one-way sync)
- Manual changes to identity systems overwritten by next sync (discouraged)

**Example**:
- HR system: Employee "Bob Brown", Department "Sales"
- Active Directory: User "bob.brown@example.com", Department "Sales"
- Azure AD: User "bob.brown@example.com", Department "Sales"
- Consistency verified: ✅ All systems agree

---

## 7. Orphaned Account Detection & Remediation

### REQ-A516-050: Orphaned Account Definition

**Requirement**:
> Orphaned accounts must be clearly defined to enable systematic detection.

**Orphaned Account Criteria**:
An account is "orphaned" if ANY of the following conditions met:

1. **User not in HR system**:
   - Account exists in identity system (AD, Azure AD, Okta)
   - No corresponding employee record in HR system
   - Example: Employee terminated but account not disabled

2. **No valid business owner**:
   - Service account exists
   - Owner attribute empty OR owner no longer with company
   - Example: Service account created for decommissioned application

3. **Inactive for extended period**:
   - Account exists and enabled
   - No login in 90+ days (no activity)
   - Example: Contractor account not disabled after contract end

**Example Orphaned Accounts**:
- Employee "Charlie Clark" terminated 2025-11-01 → account still active [Date] (70 days late)
- Service account "svc-old-backup" → owner "David Davis" left company 2025-06-15
- Contractor "EXT-jane.doe" → last login 2025-08-20 (144 days ago), contract ended 2025-09-01

---

### REQ-A516-051: Detection Frequency

**Requirement**:
> Orphaned account detection must run **monthly** (automated scan).

**Detection Frequency**: Monthly (first week of each month)

**Detection Report Contents**:
- Total orphaned accounts detected
- Breakdown by orphaned criteria (not in HR, no owner, inactive)
- Account details (username, last login, creation date, owner if applicable)
- Recommended action (disable immediately, investigate, identify owner)

---

### REQ-A516-052: Detection Methodology

**Requirement**:
> Orphaned account detection methodology must be systematic and automated.

**Detection Process**:

**Step 1: Export Identity Data**
- Export all user accounts from identity systems (AD, Azure AD, Okta)
- Include attributes: Username, display name, creation date, last login, status (enabled/disabled), manager, owner (for service accounts)

**Step 2: Export HR Data**
- Export all active employees from HR system
- Include attributes: Employee ID, full name, email, status (active/terminated), termination date

**Step 3: Cross-Reference**
- Match identity accounts to HR employees (by email or employee ID)
- Identify accounts NOT in HR system (potential orphans)

**Step 4: Check Inactive Accounts**
- Identify accounts with no login in 90+ days
- Exclude service accounts (service accounts don't have interactive logins)

**Step 5: Check Service Account Owners**
- Identify service accounts without owner attribute
- Identify service accounts where owner no longer in HR system

**Step 6: Generate Report**
- List all orphaned accounts
- Categorize by orphaned type
- Prioritize by risk (highly privileged orphaned accounts = highest risk)

**Automation**:
- Python script performs cross-reference monthly
- Report generated automatically
- Report emailed to IT Operations and Security team

---

### REQ-A516-053: Remediation Procedures

**Requirement**:
> Orphaned accounts must be remediated systematically (disable → investigate → delete).

**Remediation Workflow**:

**Step 1: Identify Owner (if possible)**
- Contact former manager (if employee account)
- Contact application owner (if service account)
- Question: "Is this account still needed? If so, for what purpose?"

**Step 2: Decision**
- **If still needed**: Assign owner, document business justification, set expiration date
- **If no longer needed**: Proceed to Step 3 (disable)

**Step 3: Disable Account**
- Immediately disable orphaned account (prevent further access)
- Document disablement in audit log

**Step 4: Monitor (30 days)**
- Monitor for any access attempts or complaints
- If someone reports needing account: Re-evaluate, possibly re-enable with proper owner

**Step 5: Delete Account**
- After 30 days disabled with no activity: Permanently delete account
- Document deletion in audit log

**Example**:
- Orphaned account detected: "svc-old-backup"
- Investigation: Application decommissioned 2025-12-01, service account no longer needed
- Action: Disable account immediately (2026-01-10)
- Monitor: 30 days (no access attempts)
- Delete: 2026-02-10 (30 days after disablement)

---

### REQ-A516-054: Orphaned Account Reporting

**Requirement**:
> Monthly orphaned account detection report must be reviewed by Security team and IT Operations.

**Report Distribution**:
- Recipients: IT Operations Manager, CISO, Security Analyst
- Frequency: Monthly (first week of each month)

**Report Metrics**:
- Total orphaned accounts detected (current month)
- Orphaned accounts remediated (previous month)
- Orphaned accounts still open (aging report)
- Trend analysis (orphaned account count over time)

**Review Meeting**:
- Monthly review meeting (IT Operations + Security team)
- Review orphaned account report
- Assign remediation owners (who will investigate each orphaned account)
- Track remediation progress (target: 100% remediated within 30 days of detection)

---

## 8. Contractor/Vendor Identity Management

### REQ-A516-060: Sponsorship Requirements

**Requirement**:
> All contractor and vendor accounts require **internal sponsor** (employee responsible for contractor access).

**Sponsor Responsibilities**:
- Justify business need for contractor access
- Approve contractor access request
- Monitor contractor access (ensure appropriate use)
- Extend access if contract extended (re-approval)
- Request access removal when contractor engagement ends
- Notify Security team when contractor contract ends

**Sponsor Assignment**:
- Sponsor identified during contractor onboarding
- Sponsor documented in identity system (contractor account attributes)
- Sponsor must be active employee (if sponsor leaves, new sponsor assigned)

**Example**:
- Contractor: "Jane Doe", ACME Consulting
- Sponsor: "Bob Brown" (Project Manager)
- Sponsor responsibility: Justify Jane's access, monitor usage, request removal when project ends

---

### REQ-A516-061: Time-Bound Access

**Requirement**:
> Contractor and vendor access must be **time-bound** to contract period with automatic expiration.

**Implementation**:
- Contractor account created with contract end date attribute
- Automatic expiration: Account auto-disables on contract end date
- Sponsor notification: 30 days before expiration (opportunity to extend if contract continues)
- Access extension requires sponsor re-approval

**Example**:
- Contractor: "Jane Doe"
- Contract period: 2026-01-01 to 2026-06-30
- Account created: 2026-01-01 with expiration date 2026-06-30
- Automatic expiration: Account auto-disables 2026-06-30
- Sponsor notification: 2026-05-30 (30 days before expiration)
- If contract extended to 2026-12-31: Sponsor submits access extension request, new expiration date 2026-12-31

---

### REQ-A516-062: Vendor Lifecycle

**Requirement**:
> Vendor identity lifecycle must address onboarding, active management, and offboarding.

**Vendor Onboarding**:
- Vendor access request submitted by internal sponsor
- Vendor company name, individual name, business justification documented
- Background check performed (if required per vendor risk assessment)
- Security team approves vendor access (enhanced review)
- Vendor account created with external identifier (EXT- prefix)
- Vendor receives access instructions (may require NDA signature)

**Active Management**:
- Quarterly access review (sponsor confirms access still needed)
- Vendor activity monitored (enhanced logging for third-party access)
- Vendor access restricted to minimum necessary (least privilege)

**Vendor Offboarding**:
- Vendor contract ends → sponsor notified
- Sponsor confirms access no longer needed
- Account disabled immediately (contract end date)
- Access removal verified (all systems, all applications)
- Vendor access termination logged for audit

---

## 9. Identity for Non-Human Entities

### REQ-A516-070: Service Accounts Managed

**Requirement**:
> Service accounts (non-human) must be managed with same rigor as user accounts.

**Service Account Lifecycle**:
- **Provisioning**: Service account request → approval → creation → owner assignment
- **Active Management**: Password rotation, access review, owner verification
- **Deprovisioning**: Service decommissioned → owner confirms → account disabled → deleted

**Service Account Documentation**:
- Service account inventory (all service accounts documented)
- Owner assigned (person responsible)
- Purpose documented (what service does this account support)
- Systems accessed (where does service account have access)
- Privilege level (standard user vs. privileged access)

---

### REQ-A516-071: IoT Devices (if applicable)

**Requirement**:
> IoT devices (if applicable) must have identities managed in identity system.

**IoT Device Identity** (if organization has IoT devices):
- Device registered in identity system (unique device ID)
- Device certificate issued (for authentication)
- Device ownership assigned (person or department responsible)
- Device access controlled (device can only access authorized systems)

**Note**: Many organizations do not have IoT devices. This requirement applies only if IoT devices present.

---

### REQ-A516-072: API Keys/Tokens Managed

**Requirement**:
> API keys and tokens must be managed as identities with lifecycle controls.

**API Key Lifecycle**:
- **Provisioning**: API key request → approval → key generated → owner assigned
- **Active Management**: Key rotation (every 90 days or per API requirements), access review
- **Deprovisioning**: API no longer used → key revoked → deletion

**API Key Documentation**:
- API key inventory (all active keys documented)
- Owner assigned (person or application responsible)
- Purpose documented (what does this key access)
- Expiration date (if time-bound)

---

### REQ-A516-073: Ownership and Lifecycle Defined

**Requirement**:
> All non-human identities (service accounts, devices, API keys) must have defined ownership and lifecycle.

**Ownership Requirements**:
- Owner attribute mandatory (service account without owner = orphaned)
- Owner must be active employee (if owner leaves, new owner assigned)
- Owner receives notifications (password rotation reminders, access reviews)

**Lifecycle Requirements**:
- Creation: Approval required, owner assigned, purpose documented
- Active: Periodic review (annual), password rotation, access verification
- Decommissioning: Owner confirms no longer needed, account disabled, deleted after 30 days

---

## 10. Audit & Evidence Requirements

### 10.1 Evidence Required for A.5.16 Compliance

**User Inventory** (Complete list of all identities):
- All user accounts (employees, contractors, vendors, service accounts)
- Account attributes (name, email, user type, status, creation date, last login)
- Source: Identity systems (AD, Azure AD, Okta) + HR system

**Provisioning Timeliness Reports**:
- New hires (hire date vs. account creation date)
- Provisioning delay calculation (days)
- On-time provisioning rate (%)
- Source: Workbook 1 (User Inventory), Workbook 5 (Lifecycle Compliance)

**Deprovisioning Timeliness Reports**:
- Terminations (termination date vs. account disable date)
- Deprovisioning delay calculation (days)
- On-time deprovisioning rate (%)
- Source: Workbook 1 (User Inventory), Workbook 5 (Lifecycle Compliance)

**Orphaned Account Detection Reports**:
- Monthly orphaned account scan results
- Orphaned account count (trend over time)
- Remediation status (accounts disabled, investigated, deleted)
- Source: Workbook 1 (Orphaned Accounts sheet)

**Contractor/Vendor Access Register**:
- All contractor and vendor accounts
- Sponsor identification, contract period, expiration date
- Source: Workbook 1 (Contractor Lifecycle sheet)

---

### 10.2 Assessment Workbooks (A.5.16 Evidence)

**Workbook 1: User Inventory & Lifecycle Compliance**
- Complete user inventory (all account types)
- Employee lifecycle metrics (provisioning/deprovisioning timeliness)
- Contractor lifecycle metrics (time-bound access, sponsor identification)
- Service accounts (owner assignment, purpose documentation)
- Orphaned account detection results

**Workbook 5: Lifecycle Compliance Detailed Assessment**
- Joiner compliance (new hire provisioning timeliness)
- Mover compliance (role change access modification timeliness)
- Leaver compliance (termination deprovisioning timeliness)
- Contractor lifecycle compliance (auto-expiration verification)
- Orphaned account remediation tracking

---

### 10.3 Audit Testing Approach

**Provisioning Audit**:
1. Select sample of 20 new hires (random selection)
2. Verify account created by hire date (on-time provisioning)
3. Verify user attributes accurate (name, email, department, manager)
4. Verify standard access granted (per role definition)

**Deprovisioning Audit**:
1. Select sample of 20 terminations (random selection)
2. Verify account disabled within 24 hours of termination
3. Verify all access removed (group memberships, application access)
4. Verify deprovisioning logged in audit trail

**Orphaned Account Audit**:
1. Request most recent orphaned account detection report
2. Verify monthly scan occurred (frequency compliance)
3. Select 5 orphaned accounts → verify remediation (disabled or deleted)
4. Verify unresolved orphaned accounts escalated

**Contractor Lifecycle Audit**:
1. Select sample of 10 contractor accounts
2. Verify sponsor assigned (documented)
3. Verify contract end date documented (time-bound access)
4. Verify accounts auto-disabled on contract end (or extended with approval)

---

## 11. Document Approval

**Prepared By**: [Name], [Title] - [Date]  
**Reviewed By**: [Name], [Title] - [Date]  
**Approved By**: [Name], CISO - [Date]

**Next Review Date**: [Date + 12 months]

**Version History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial policy release |

---

**END OF SECTION 3 (POL-S3 - A.5.16 Identity Management)**

**Next Document**: ISMS-POL-A.5.15-16-18-S4_Access_Rights_Management_A518.md
