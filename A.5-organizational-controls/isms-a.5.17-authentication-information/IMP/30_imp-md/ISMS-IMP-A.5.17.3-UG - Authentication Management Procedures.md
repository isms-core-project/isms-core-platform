**ISMS-IMP-A.5.17.3-UG - Authentication Management Procedures**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.17: Authentication Information

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.17.3-UG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.17 Authentication Information |
| **Parent Policy** | ISMS-POL-A.5.17 - Authentication Information |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.17.3-TG.

---

## Assessment Overview

### Purpose

This workbook provides a comprehensive Authentication Management Procedures assessment framework that evaluates the operational processes for managing authentication credentials throughout their lifecycle - from initial allocation through use, change, reset, and eventual revocation.

The assessment serves multiple purposes:
- **Process Verification**: Confirm credential lifecycle procedures exist and are followed
- **Security Assessment**: Evaluate credential handling against security requirements
- **Compliance Tracking**: Verify procedures meet policy requirements
- **Gap Identification**: Identify procedural weaknesses in credential management
- **Evidence**: Provide Stage 2 audit evidence of operational credential controls

### Scope

The Authentication Management Procedures Assessment covers:

| Lifecycle Phase | Procedures Assessed | Key Concerns |
|-----------------|---------------------|--------------|
| **Initial Allocation** | New user credential creation, initial password communication | Secure delivery, forced change |
| **Ongoing Use** | Day-to-day authentication, session management | Secure handling, timeout policies |
| **Password Changes** | Scheduled rotation, user-initiated changes | Change enforcement, history |
| **Password Reset** | Self-service reset, helpdesk reset | Identity verification, secure delivery |
| **Credential Recovery** | Lost MFA, locked accounts | Identity verification, audit trail |
| **Revocation** | Termination, role change | Timely revocation, verification |
| **Shared Credentials** | Service accounts, shared admin accounts | Vault storage, check-out logging |

**Account Types Covered:**

| Account Type | Lifecycle Considerations |
|--------------|-------------------------|
| Employee Accounts | Full lifecycle from hire to termination |
| Contractor Accounts | Time-limited, project-based lifecycle |
| Service Accounts | Rotation triggers, vault management |
| Privileged Accounts | Enhanced procedures per A.8.2-3-5 |
| External/Customer Accounts | Self-service, identity verification |
| Emergency/Break-Glass | Sealed credentials, audit requirements |

### Business Value

| Value Area | Benefit |
|------------|---------|
| **Security Posture** | Proper credential lifecycle reduces compromise window |
| **Operational Efficiency** | Documented procedures reduce errors and support time |
| **Compliance** | Meets ISO 27001, SOX, regulatory requirements |
| **Audit Readiness** | Procedures documentation accelerates certification |
| **Incident Response** | Clear procedures enable rapid credential revocation |
| **User Experience** | Consistent processes improve user satisfaction |

### Assessment Frequency

| Assessment Type | Frequency | Trigger Events |
|-----------------|-----------|----------------|
| Full Procedure Review | Annual | Policy changes, technology changes |
| Process Compliance Audit | Quarterly | Audit findings, incidents |
| Helpdesk Procedure Review | Semi-annual | Staff turnover, new systems |
| Emergency Procedure Test | Annual | Incident, DR test |
| Ad-hoc Review | As needed | Security incidents, audit requests |

---

## Control Requirements

### ISO 27001:2022 Control A.5.17

Per ISO/IEC 27001:2022 Control A.5.17:

> *"Allocation and management of authentication information should be controlled by a management process, including advising personnel on appropriate handling of authentication information."*

This control explicitly requires documented management processes for authentication information.

**Control Type:** Preventive
**Security Properties:** Confidentiality, Integrity
**Cybersecurity Concepts:** Protect, Identify
**Operational Capabilities:** Identity and Access Management

### Procedural Requirements (from ISMS-POL-A.5.17)

| Procedure | Key Requirements |
|-----------|------------------|
| **Initial Allocation** | Unique credentials, secure communication, forced change |
| **Password Changes** | Self-service capability, enforcement mechanisms |
| **Password Reset** | Identity verification, secure delivery, audit logging |
| **Credential Recovery** | Multi-factor verification, supervisor approval for privileged |
| **Shared Credentials** | Vault storage, named custodians, check-out logging |
| **Revocation** | Same-day for terminations, immediate for security events |

### What Auditors Look For

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Documented Procedures** | Written procedures for each lifecycle phase |
| **Process Execution** | Evidence procedures are actually followed |
| **Identity Verification** | How users are verified during reset/recovery |
| **Secure Communication** | How temporary credentials are delivered |
| **Audit Trails** | Logging of credential changes and resets |
| **Timeliness** | Evidence of timely revocation |
| **Training** | Staff awareness of procedures |

---

## Prerequisites

### Required Access

| System | Purpose | Access Level Needed |
|--------|---------|---------------------|
| Identity Provider | Password reset procedures, logs | Admin access |
| Service Desk System | Ticket workflows, reset requests | Admin access |
| PAM Solution | Privileged credential procedures | Audit access |
| HR System | Termination/joiner notifications | Read access |
| Training Platform | Awareness completion records | Read access |

### Required Documents

- [ ] ISMS-POL-A.5.17 - Authentication Information (approved)
- [ ] Current helpdesk procedures/runbooks
- [ ] Self-service password reset documentation
- [ ] PAM operational procedures
- [ ] HR onboarding/offboarding checklists
- [ ] Prior procedure assessments (if applicable)

### Required Personnel

| Role | Responsibility | Time Commitment |
|------|----------------|-----------------|
| **Assessment Lead** | Coordinate assessment, document findings | 8-12 hours |
| **IAM Administrator** | Provide procedure documentation, demonstrate processes | 4-6 hours |
| **Service Desk Lead** | Explain reset/recovery procedures | 2-4 hours |
| **HR Representative** | Verify onboarding/offboarding integration | 2-3 hours |
| **PAM Administrator** | Demonstrate privileged credential procedures | 2-4 hours |

---

## Completion Walkthrough

### Step 1: Inventory Existing Procedures

**Time allocation:** 2-3 hours

**Purpose:** Create a complete inventory of all credential management procedures.

**Procedure Inventory Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Procedure_ID | Unique identifier | PROC-AUTH-001 |
| Procedure_Name | Descriptive title | New User Password Creation |
| Lifecycle_Phase | Which phase it covers | Initial Allocation |
| Account_Types | Applicable accounts | Employee, Contractor |
| Document_Location | Where procedure is stored | SharePoint/IT-Runbooks/ |
| Owner | Procedure owner | IAM Team Lead |
| Last_Updated | Document date | 01.01.2026 |
| Review_Status | Current/outdated | Current |

**Required Procedures per Lifecycle Phase:**

| Lifecycle Phase | Required Procedures |
|-----------------|---------------------|
| Initial Allocation | New user account creation, initial password generation, secure delivery |
| Ongoing Use | Password handling guidance, session timeout enforcement |
| Password Change | Self-service change, forced change on first login, expiry enforcement |
| Password Reset | Self-service reset, helpdesk reset, identity verification |
| Credential Recovery | MFA recovery, locked account recovery, escalation |
| Revocation | Termination processing, immediate revocation, verification |
| Shared Credentials | Service account creation, vault check-out, rotation |

**Worked Example - Procedure Inventory:**

| Procedure_ID | Procedure_Name | Lifecycle_Phase | Account_Types | Last_Updated |
|--------------|----------------|-----------------|---------------|--------------|
| PROC-AUTH-001 | New User Account Creation | Initial Allocation | Employee, Contractor | 01.01.2026 |
| PROC-AUTH-002 | Initial Password Delivery | Initial Allocation | All | 01.01.2026 |
| PROC-AUTH-003 | Self-Service Password Reset | Password Reset | Employee | 15.12.2025 |
| PROC-AUTH-004 | Helpdesk Password Reset | Password Reset | All | 01.01.2026 |
| PROC-AUTH-005 | MFA Recovery Procedure | Credential Recovery | Employee | 01.11.2025 |
| PROC-AUTH-006 | Employee Termination - Credential Revocation | Revocation | Employee | 01.01.2026 |
| PROC-AUTH-007 | Service Account Password Rotation | Shared Credentials | Service Account | 01.12.2025 |

### Step 2: Assess Initial Allocation Procedures

**Time allocation:** 2-3 hours

**Purpose:** Verify procedures for creating and delivering initial credentials are secure.

**Assessment Criteria:**

| Criterion | Requirement | Evidence |
|-----------|-------------|----------|
| Unique credentials | Each user gets unique initial password | Procedure document |
| No shared initial passwords | Initial passwords not reused | Process verification |
| Secure generation | Passwords randomly generated | System configuration |
| Forced change | First login requires password change | IdP configuration |
| Secure delivery | Temporary password delivered securely | Procedure + sample |
| Audit logging | Creation and delivery logged | Log samples |

**Initial Password Delivery Methods Assessment:**

| Delivery Method | Acceptable | Conditions |
|-----------------|------------|------------|
| In-person to verified user | Yes | ID verification required |
| Encrypted email to verified address | Yes | Time-limited, forced change |
| SMS to verified mobile | Conditional | Time-limited, forced change |
| Manager delivery | Conditional | Manager verifies identity |
| Unencrypted email | No | Never acceptable |
| Shared document/portal | No | Never acceptable |
| Voice call | No | Never acceptable |

**Documentation Requirements:**

1. Document the procedure for creating new user accounts
2. Document how initial passwords are generated
3. Document how initial passwords are delivered
4. Capture evidence of forced password change configuration
5. Sample audit logs showing account creation events

### Step 3: Assess Password Reset Procedures

**Time allocation:** 2-3 hours

**Purpose:** Verify password reset procedures include adequate identity verification.

**Self-Service Reset Assessment:**

| Control | Requirement | Status |
|---------|-------------|--------|
| Identity verification | At least 2 factors before reset | ☐ |
| No knowledge-based questions | Security questions prohibited | ☐ |
| MFA challenge | Existing MFA factor required | ☐ |
| Temporary password expiry | Reset link expires (<1 hour) | ☐ |
| Forced change | Must set new password immediately | ☐ |
| Notification | User notified of reset attempt | ☐ |
| Audit logging | All reset attempts logged | ☐ |

**Prohibited Reset Methods (per ISMS-POL-A.5.17):**

| Method | Status | Risk |
|--------|--------|------|
| Security questions alone | Prohibited | Social engineering |
| Email link without MFA | Prohibited | Email compromise |
| Manager request without verification | Prohibited | Social engineering |
| Phone call reset | Prohibited (default) | Voice phishing |

**Helpdesk Reset Assessment:**

| Control | Requirement | Status |
|---------|-------------|--------|
| Caller verification | Multiple identity checks | ☐ |
| Verification documented | Checks recorded in ticket | ☐ |
| Ticket required | All resets via ticketing system | ☐ |
| Secure delivery | No verbal password delivery | ☐ |
| Forced change | Temporary password requires change | ☐ |
| Supervisor approval | Required for privileged accounts | ☐ |
| Audit trail | Full ticket history retained | ☐ |

**Identity Verification Requirements for Helpdesk:**

| Account Type | Minimum Verification |
|--------------|---------------------|
| Standard User | 2 identity factors (employee ID + callback to registered number) |
| Privileged User | 3 identity factors + manager approval |
| External User | Contract verification + registered contact callback |
| Service Account | Change ticket + application owner approval |

### Step 4: Assess Credential Recovery Procedures

**Time allocation:** 1-2 hours

**Purpose:** Verify procedures for recovering from lost MFA devices or locked accounts.

**MFA Recovery Assessment:**

| Scenario | Required Procedure | Verification |
|----------|-------------------|--------------|
| Lost phone (Authenticator) | Identity verification + supervisor approval | ☐ Documented |
| Lost hardware key | Identity verification + key deactivation + new key issue | ☐ Documented |
| Locked account (failed attempts) | Self-service after timeout OR helpdesk with verification | ☐ Documented |
| Forgotten password + lost MFA | In-person identity verification required | ☐ Documented |

**Recovery Procedure Requirements:**

| Requirement | Description | Evidence |
|-------------|-------------|----------|
| Alternative verification | Backup identity verification method defined | Procedure |
| Supervisor involvement | Required for privileged accounts | Procedure |
| Temporary access | Limited access until full recovery | Configuration |
| Device deactivation | Lost devices immediately deactivated | Process |
| New enrollment | Clean MFA enrollment after recovery | Process |
| Audit logging | Recovery events fully logged | Log samples |

### Step 5: Assess Revocation Procedures

**Time allocation:** 2-3 hours

**Purpose:** Verify credentials are revoked timely and completely.

**Revocation Trigger Assessment:**

| Trigger Event | SLA | Procedure Reference |
|---------------|-----|---------------------|
| Voluntary resignation | End of last working day | PROC-AUTH-006 |
| Termination for cause | Immediate | PROC-AUTH-006 |
| Security incident | Immediate | Incident response |
| Role change | Before new role starts | PROC-AUTH-008 |
| Contractor end date | End of contract | PROC-AUTH-009 |
| Leave of absence (>30 days) | Disable on start | PROC-AUTH-010 |

**Revocation Completeness Checklist:**

| System/Access | Revocation Action | Verification |
|---------------|-------------------|--------------|
| Primary directory (AD/Azure AD) | Account disabled/deleted | ☐ |
| Email/collaboration | Mailbox converted/deleted | ☐ |
| VPN access | Certificate/token revoked | ☐ |
| Application access | All app accounts disabled | ☐ |
| Physical access | Badge deactivated | ☐ |
| Mobile devices | MDM wipe initiated | ☐ |
| Shared credentials | Passwords rotated | ☐ |

**Revocation Verification Procedure:**

1. Revocation initiated by HR notification
2. IT executes revocation checklist
3. Verification performed within 24 hours
4. Manager confirms access removed
5. Audit trail retained

**Sample Testing:**

Select 5-10 recent terminations and verify:
- Time between HR notification and account disable
- All systems included in revocation
- Verification evidence exists
- Shared credential rotation (if applicable)

### Step 6: Assess Shared Credential Procedures

**Time allocation:** 2-3 hours

**Purpose:** Verify shared credentials (service accounts, shared admin accounts) are managed securely.

**Shared Credential Requirements (per ISMS-POL-A.5.17):**

| Requirement | Description | Verification |
|-------------|-------------|--------------|
| Vault storage | All shared credentials in approved vault | PAM inventory |
| Named custodians | Each credential has designated owner(s) | Ownership records |
| Check-out logging | All access logged with identity | Audit logs |
| Rotation triggers | Rotated on personnel change, suspected compromise, annually | Rotation history |
| No embedding | Credentials not hardcoded in scripts/configs | Code review/scan |

**Service Account Assessment:**

| Field | Description | Example |
|-------|-------------|---------|
| Account_ID | Service account identifier | svc-batch-finance |
| Purpose | What the account is used for | Finance batch processing |
| Custodian | Named owner(s) | John Smith, Jane Doe |
| Vault_Stored | In approved vault | Yes |
| Last_Rotation | Date of last password change | 01.12.2025 |
| Rotation_Reason | Why rotated | Scheduled (annual) |
| Next_Rotation | Scheduled rotation | 01.12.2026 |

**Rotation Trigger Events:**

| Event | Rotation Required | Timeline |
|-------|-------------------|----------|
| Custodian leaves organisation | Yes | Same day |
| Suspected compromise | Yes | Immediate |
| Annual scheduled | Yes | Per schedule |
| System change | Evaluate | Risk-based |

### Step 7: Review Audit Trails

**Time allocation:** 2-3 hours

**Purpose:** Verify credential management activities are properly logged and retained.

**Required Audit Events:**

| Event Category | Events to Log | Retention |
|----------------|---------------|-----------|
| Account Creation | Create, initial password set | 3 years |
| Password Changes | User change, admin reset, expiry | 3 years |
| Authentication | Success, failure, lockout | 1 year |
| MFA | Enrollment, recovery, changes | 3 years |
| Access Revocation | Disable, delete, permission change | 7 years |
| Shared Credentials | Check-out, check-in, rotation | 7 years |

**Audit Trail Quality Checks:**

| Check | Requirement | Status |
|-------|-------------|--------|
| Completeness | All required events captured | ☐ |
| Timestamp accuracy | Synchronised time source | ☐ |
| User identification | Actor clearly identified | ☐ |
| Immutability | Logs protected from modification | ☐ |
| Retention | Meets retention requirements | ☐ |
| Accessibility | Available for audit/investigation | ☐ |

**Sample Audit Trail Review:**

1. Select 5 recent password resets - verify logs capture:
   - Who requested the reset
   - How identity was verified
   - Who performed the reset
   - Timestamp of reset
   - Delivery method used

2. Select 5 recent terminations - verify logs capture:
   - HR notification timestamp
   - Account disable timestamp
   - Who disabled the account
   - Systems affected

### Step 8: Document Gaps and Plan Remediation

**Time allocation:** 2-3 hours

**Purpose:** Consolidate findings and create remediation plans.

**Gap Categories:**

| Gap Type | Description | Example |
|----------|-------------|---------|
| Missing Procedure | No documented procedure exists | No MFA recovery procedure |
| Inadequate Procedure | Procedure exists but insufficient | Reset without verification |
| Non-Compliance | Procedure exists but not followed | Helpdesk bypassing verification |
| Outdated Procedure | Procedure doesn't reflect current process | Document references old system |
| Missing Audit Trail | Required events not logged | No reset attempt logging |

**Gap Record Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Gap_ID | Unique identifier | GAP-PROC-2026-001 |
| Gap_Type | Category | Inadequate Procedure |
| Lifecycle_Phase | Affected phase | Password Reset |
| Description | Gap details | Helpdesk reset lacks identity verification |
| Risk_Level | Impact assessment | High |
| Current_State | What exists now | Single factor verification |
| Required_State | What policy requires | Two-factor verification |
| Remediation_Action | Planned fix | Update procedure, retrain staff |

---

## Evidence Collection

### Evidence Requirements

| Evidence Type | Source | Retention |
|---------------|--------|-----------|
| This assessment workbook | Generated | 7 years |
| Procedure documents | Runbooks/SharePoint | 7 years |
| IdP configuration | Azure AD/Okta | 3 years |
| Sample tickets | Service desk | 3 years |
| Audit logs | SIEM/IdP | Per retention policy |
| Training records | LMS | 3 years |

### Evidence Storage

**Primary Location:** `[SharePoint/Evidence Library]/A.5.17/Auth-Procedures/[Year]/`

**Folder Structure:**
```
A.5.17/
|-- Auth-Procedures/
|   |-- 2026/
|   |   |-- Assessment-Workbooks/
|   |   |   |-- ISMS-IMP-A.5.17.3_Auth_Procedures_20260203.xlsx
|   |   |-- Evidence/
|   |   |   |-- Procedures/
|   |   |   |   |-- PROC-AUTH-001-New-User-Creation.pdf
|   |   |   |   |-- PROC-AUTH-003-Self-Service-Reset.pdf
|   |   |   |   |-- PROC-AUTH-006-Termination-Revocation.pdf
|   |   |   |-- Sample-Tickets/
|   |   |   |   |-- Reset-Ticket-Sample-20260203.pdf
|   |   |   |   |-- Termination-Ticket-Sample-20260203.pdf
|   |   |   |-- Audit-Logs/
|   |   |   |   |-- Reset-Audit-Log-Sample-20260203.xlsx
|   |   |   |   |-- Termination-Audit-Log-Sample-20260203.xlsx
|   |   |   |-- Training/
|   |   |   |   |-- Helpdesk-Training-Completion-20260203.pdf
|   |   |   |-- Approvals/
|   |   |   |   |-- CISO-SignOff-20260203.pdf
```

---

## Common Pitfalls

Avoid these common mistakes when completing the Authentication Management Procedures assessment:

### Procedure Documentation Pitfalls

❌ **MISTAKE**: Accepting verbal explanations as documented procedures
✅ **CORRECT**: Require written, approved procedure documents with version control

❌ **MISTAKE**: Assuming IdP default workflows constitute documented procedures
✅ **CORRECT**: Document organisation-specific procedures even when using platform defaults

❌ **MISTAKE**: Having procedures that reference outdated systems or roles
✅ **CORRECT**: Verify procedures reflect current technology and organisational structure

### Identity Verification Pitfalls

❌ **MISTAKE**: Allowing helpdesk to reset passwords based on manager email request alone
✅ **CORRECT**: Require callback verification or in-person identity confirmation

❌ **MISTAKE**: Using security questions as identity verification
✅ **CORRECT**: Security questions are prohibited per ISMS-POL-A.5.17

❌ **MISTAKE**: Same verification for standard and privileged accounts
✅ **CORRECT**: Enhanced verification (supervisor approval) required for privileged accounts

### Revocation Timing Pitfalls

❌ **MISTAKE**: Waiting for next business day to revoke terminated employee access
✅ **CORRECT**: Same-day revocation for standard, immediate for termination-for-cause

❌ **MISTAKE**: Disabling primary account but forgetting application-specific accounts
✅ **CORRECT**: Comprehensive revocation checklist covering all systems

❌ **MISTAKE**: Not rotating shared credentials when custodian leaves
✅ **CORRECT**: Immediate rotation of any shared credentials the departing user could access

### Audit Trail Pitfalls

❌ **MISTAKE**: Relying on IdP logs alone without verification they capture required events
✅ **CORRECT**: Verify specific events are logged with sample evidence

❌ **MISTAKE**: Logs exist but are not reviewed or monitored
✅ **CORRECT**: Document review procedures and alert configurations

---

## Quality Checklist

Before submitting the assessment, verify:

### Procedure Completeness Checks

- [ ] All lifecycle phases have documented procedures
- [ ] Procedures cover all account types (employee, contractor, service, privileged)
- [ ] Procedures are current (reviewed within 12 months)
- [ ] Procedures are approved and version-controlled
- [ ] Procedure locations documented and accessible

### Security Control Checks

- [ ] Identity verification meets policy requirements
- [ ] No prohibited methods (security questions, unverified email)
- [ ] Privileged accounts have enhanced procedures
- [ ] Shared credentials managed through vault
- [ ] Revocation SLAs meet policy requirements

### Evidence Quality Checks

- [ ] Sample tickets demonstrate procedure compliance
- [ ] Audit logs show required events captured
- [ ] Training records show staff awareness
- [ ] Configuration evidence supports technical controls
- [ ] Evidence dated within assessment period

### Gap Analysis Checks

- [ ] All gaps have clear descriptions
- [ ] Risk levels appropriately assigned
- [ ] Remediation actions are specific and actionable
- [ ] Owners and timelines assigned
- [ ] No critical gaps without remediation plans

---

## Review and Approval

### Review Workflow

```
Assessment Lead Completes
        │
        ▼
Self-Review (Quality Checklist)
        │
        ▼
Service Desk Lead Validates ──────► Return for Corrections
        │                                 │
        ▼                                 │
IAM Administrator Validates ──────► Return for Corrections
        │                                 │
        ▼                                 │
IT Security Review ───────────────► Return for Corrections
        │                                 │
        ▼                                 │
CISO Final Approval ──────────────────────┘
        │
        ▼
   Assessment Complete
```

### Approval Signatures

1. **Assessment Lead Certification:**
   - Confirms methodology was followed
   - Confirms evidence was verified
   - Date and signature

2. **Service Desk Lead Validation:**
   - Confirms reset/recovery procedures accurate
   - Confirms staff trained on procedures
   - Date and signature

3. **IAM Administrator Validation:**
   - Confirms technical controls accurate
   - Confirms audit logging verified
   - Date and signature

4. **CISO Approval:**
   - Approves overall procedure assessment
   - Accepts identified gaps and remediation plans
   - Date and signature

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
