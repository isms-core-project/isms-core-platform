# ISMS-POL-A.5.15-16-18-S2: Access Control Policy (A.5.15)
## Strategic Access Control Framework

**Document ID**: ISMS-POL-A.5.15-16-18-S2  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Active

---

## Document Purpose

This section defines **access control policy requirements** implementing ISO/IEC 27001:2022 Control A.5.15. It establishes the strategic framework governing WHO gets access to WHAT information and systems, and WHY access is granted.

---

## 1. Control Objective & Scope

### 1.1 ISO 27001:2022 Control A.5.15 - Access Control

**Official Control Text (German)**:
> Regeln zur Steuerung des physischen und logischen Zugriffs auf Informationen und andere damit verbundene Werte müssen auf der Grundlage von Geschäfts- und Informationssicherheitsanforderungen aufgestellt und umgesetzt werden.

**English Translation**:
> Rules to control physical and logical access to information and other associated assets shall be established and implemented based on business and information security requirements.

**Control Objective**:
Ensure access to information, systems, and data is governed by strategic policies that:
- Prevent unauthorized access while enabling legitimate business activities
- Base access decisions on business justification and security requirements
- Separate conflicting roles to prevent fraud and error
- Document access control rules, responsibilities, and exceptions

**Scope of A.5.15 Requirements**:
This section covers the **strategic policy layer** for access control:
- ✅ Access control principles (least privilege, need-to-know, segregation of duties)
- ✅ Access classification framework (user types, system criticality, data sensitivity)
- ✅ Business justification requirements for access requests
- ✅ Access control roles and responsibilities (who approves, provisions, reviews)
- ✅ Segregation of duties (SoD) matrix and violation management
- ✅ Exception handling (documented approvals for policy deviations)
- ✅ Integration with HR processes (onboarding, offboarding, role changes)

**Out of Scope** (covered in other controls):
- ❌ Identity lifecycle implementation → A.5.16 (Identity Management)
- ❌ Access rights assignment procedures → A.5.18 (Access Rights)
- ❌ Technical authentication mechanisms → A.8.5 (Secure Authentication)
- ❌ Privileged access management (PAM) → A.8.2 (Privileged Access Rights)

---

### 1.2 Why Access Control Policy Matters

**Without strategic access control policy**:
- No clear criteria for WHO should have access to WHAT
- Access granted based on "whoever asks loudest"
- No segregation of duties = fraud opportunity
- Inconsistent access decisions across different managers/systems
- No business justification = access sprawl

**With strategic access control policy**:
- Clear principles guiding all access decisions
- Business justification required for all access
- Segregation of duties prevents fraud/error
- Consistent access governance across organization
- Documented accountability for access decisions

---

## 2. Access Control Principles

[Organization] implements the following **core access control principles** guiding all access decisions:

### REQ-A515-001: Least Privilege

**Requirement**:
> Users must be granted the **minimum access necessary** to perform their authorized job functions. No more, no less.

**Implementation**:
- Default: Users have NO access to any system/data
- Access granted ONLY when business justification provided
- Access level limited to minimum required (read-only preferred over write, write preferred over admin)
- Privileged access (admin, root) granted only when absolutely necessary

**Examples**:
- ✅ Financial analyst: Read-only access to finance reporting database
- ❌ Financial analyst: Admin access to finance reporting database (excessive)
- ✅ Developer: Write access to development environment, read-only to production
- ❌ Developer: Admin access to production (violates least privilege)

**Rationale**: Reduces blast radius of account compromise, limits insider threat risk.

---

### REQ-A515-002: Need-to-Know

**Requirement**:
> Users must access ONLY the information required to perform their specific duties, not all information in their department/system.

**Implementation**:
- Access limited by business function (not organizational hierarchy)
- Data access restricted to job-relevant information
- "All HR employees can access all HR data" = violation of need-to-know
- "Payroll specialists access payroll data, recruiters access candidate data" = compliant

**Examples**:
- ✅ Payroll specialist: Access to salary data for payroll processing
- ❌ Payroll specialist: Access to employee performance reviews (not needed)
- ✅ IT support: Access to logs for troubleshooting assigned incidents
- ❌ IT support: Unrestricted access to all system logs (excessive)

**Rationale**: Minimizes exposure of sensitive information, reduces risk of unauthorized disclosure.

---

### REQ-A515-003: Segregation of Duties (SoD)

**Requirement**:
> Conflicting roles that could enable fraud or error must be separated. No single person should control an entire sensitive process.

**Implementation**:
- SoD matrix defines conflicting role pairs (see Section 6)
- Automated detection of SoD violations (users with both conflicting roles)
- Exceptions require senior management approval + compensating controls
- Financial and IT processes subject to mandatory SoD requirements

**Common SoD Conflicts**:
| Role A | Role B | Risk | Required Separation |
|--------|--------|------|---------------------|
| **Requestor** | **Approver** | Fraud (approve own requests) | Mandatory |
| **Developer** | **Production Admin** | Unauthorized changes to production | Mandatory |
| **Finance - Request Payment** | **Finance - Approve Payment** | Fraudulent payments | Mandatory |
| **User Admin** | **Security Auditor** | Cover up unauthorized access | Recommended |
| **Database Admin** | **Application Developer** | Data manipulation | Recommended |

**Examples**:
- ✅ Alice requests expense reimbursement → Manager Bob approves
- ❌ Alice requests expense reimbursement → Alice approves (SoD violation)
- ✅ Developer writes code → separate release manager deploys to production
- ❌ Developer writes code + deploys to production (SoD violation)

**Rationale**: Prevents fraud (requires collusion), reduces error (multiple people verify).

---

### REQ-A515-004: Default Deny

**Requirement**:
> Access is DENIED by default. Access granted ONLY upon explicit authorization.

**Implementation**:
- New users: Zero access until explicitly granted
- New systems: Zero users until access explicitly granted
- "Everyone can access unless blocked" = violation
- "No one can access unless granted" = compliant

**Examples**:
- ✅ New employee: No system access until manager approves access request
- ❌ New employee: Automatic access to all "standard" systems (violates default deny)
- ✅ New file share: No users have access until owner grants permissions
- ❌ New file share: "Everyone" group has read access by default (violates default deny)

**Rationale**: Prevents accidental over-provisioning, forces conscious access decisions.

---

### REQ-A515-005: Defense in Depth

**Requirement**:
> Multiple layers of access control provide redundancy. Single control failure does not result in unauthorized access.

**Implementation**:
- Network layer: Firewall, network segmentation
- System layer: Authentication (A.8.5), authorization (A.5.18)
- Application layer: Application-level access controls
- Data layer: Encryption, data masking
- Monitoring layer: Access logging (A.8.16), anomaly detection

**Examples**:
- ✅ VPN authentication → system authentication → application authorization → data encryption
- ❌ Only network firewall protecting sensitive data (single layer = fragile)
- ✅ Privileged access requires: MFA + jump host + session recording + approval
- ❌ Privileged access requires only password (single layer = weak)

**Rationale**: No single point of failure, compensates for individual control weaknesses.

---

## 3. Access Classification Requirements

[Organization] classifies access based on **three dimensions**: user type, system criticality, and data sensitivity.

### 3.1 User Type Classification

**REQ-A515-010: User Types Defined**

**Purpose**: Different user types have different access governance requirements.

| User Type | Definition | Access Governance | Lifecycle |
|-----------|------------|-------------------|-----------|
| **Employee** | Internal staff (full-time, part-time) | Standard approval | HR-driven (joiner/mover/leaver) |
| **Contractor** | Temporary workers | Sponsored + time-bound | Contract start/end dates |
| **Vendor** | Third-party service providers | Sponsored + enhanced monitoring | Vendor contract period |
| **Partner** | Business partners (joint ventures, etc.) | Formal agreement + reciprocal | Partnership agreement period |
| **Customer** | External users (customer portals) | Self-service + terms acceptance | Account lifecycle |
| **Service Account** | Non-human (application accounts) | Owner assigned + purpose documented | Service lifecycle |
| **Emergency Account** | Break-glass (disaster recovery) | Restricted storage + usage logged | Permanent (until revoked) |

**Implementation**:
- User type identified during account creation (documented in identity repository)
- Access approval workflow varies by user type (employees: manager approval, contractors: sponsor + manager)
- Review frequency varies by user type (contractors: quarterly, employees: annual)

---

### 3.2 System Criticality Classification

**REQ-A515-011: System Criticality Levels Defined**

**Purpose**: More critical systems require stricter access controls.

| Criticality | Definition | Access Approval | Review Frequency | Examples |
|-------------|------------|-----------------|------------------|----------|
| **Critical** | Business-critical systems; outage = severe business impact | Multi-person approval (manager + system owner + CISO) | Quarterly | Core banking system, payment processing, production ERP |
| **High** | Important systems; outage = moderate business impact | Dual approval (manager + system owner) | Semi-annual | Finance systems, HR systems, CRM |
| **Medium** | Standard business systems; outage = minor impact | Manager approval | Annual | Department file shares, standard office apps |
| **Low** | Non-critical systems; outage = negligible impact | Manager approval + self-service for read-only | Biennial | Public website (read-only), internal wikis |

**Implementation**:
- System owner classifies system criticality during system onboarding
- Classification reviewed annually (systems become more/less critical over time)
- Access approval workflow enforced based on criticality

**Example - Finance System Access Request**:
- System: "Finance ERP" = **High criticality**
- Requestor: Alice (Financial Analyst)
- Approval required: (1) Alice's manager + (2) Finance system owner
- Review frequency: Semi-annual access review

---

### 3.3 Data Sensitivity Classification

**REQ-A515-012: Data Sensitivity Levels Defined**

**Purpose**: More sensitive data requires stricter access controls and justification.

| Sensitivity | Definition | Access Requirements | Examples |
|-------------|------------|---------------------|----------|
| **Restricted** | Highly sensitive; unauthorized disclosure = severe harm | Business justification + CISO approval + enhanced monitoring | PII (SSN, health data), financial data (credit cards, bank accounts), intellectual property (trade secrets, M&A plans), authentication credentials (passwords, keys) |
| **Confidential** | Internal-only; unauthorized disclosure = moderate harm | Business justification + manager approval | Employee salaries, customer contracts, internal financial reports, product roadmaps |
| **Internal** | Internal use; unauthorized disclosure = minor harm | Manager approval (standard access) | Company policies, internal procedures, department org charts, meeting notes |
| **Public** | Public information; no harm from disclosure | No restrictions (publicly accessible) | Marketing materials, published financial results, public website content |

**Implementation**:
- Data owner classifies data sensitivity
- Access requests include data sensitivity level (auto-populated from system/data classification)
- Restricted data access requires enhanced justification + CISO approval

**Example - Salary Data Access Request**:
- Data: "Employee Salaries" = **Confidential**
- Requestor: Bob (HR Manager)
- Justification: "Manage compensation review process"
- Approval: Bob's manager (HR Director)
- Additional controls: Access logged, audit trail reviewed monthly

---

## 4. Business Justification Framework

**REQ-A515-020: Business Justification Required**

**Requirement**:
> All access requests must include business justification explaining WHY access is needed.

**What constitutes valid business justification**:
- ✅ Job function requires access (e.g., "Financial analyst needs read access to finance database for monthly reporting")
- ✅ Project assignment requires access (e.g., "Developer needs access to customer portal codebase for Project Phoenix")
- ✅ Support role requires access (e.g., "IT support needs admin access to troubleshoot email server issues")
- ❌ "Nice to have" (insufficient justification)
- ❌ "Everyone else has it" (not a business need)
- ❌ "Might need it someday" (speculative, not current need)

**Implementation**:
- Access request form includes mandatory "Business Justification" field
- Requestor enters justification in own words (free text, 50-500 characters)
- Approver evaluates justification adequacy before approving
- Insufficient justification = request rejected, requestor must re-submit with better justification

---

**REQ-A515-021: Justification Documented**

**Requirement**:
> Business justification must be documented in access request ticket/system for audit trail.

**Documentation Requirements**:
- Access request ticket includes:
  - Requestor name
  - System/data being requested
  - Access level requested (read/write/admin)
  - Business justification (free text)
  - Approver(s)
  - Approval date
  - Access grant date
- Retention: 3 years minimum (for audit purposes)

---

**REQ-A515-022: Approval Chain Based on Classification**

**Requirement**:
> Approval workflow varies based on system criticality and data sensitivity.

**Approval Matrix**:

| System Criticality | Data Sensitivity | Approval Required |
|-------------------|------------------|-------------------|
| **Critical** | Restricted | Manager + System Owner + CISO |
| **Critical** | Confidential | Manager + System Owner |
| **High** | Restricted | Manager + System Owner + Security Team |
| **High** | Confidential | Manager + System Owner |
| **Medium** | Restricted | Manager + Security Team |
| **Medium** | Confidential/Internal | Manager |
| **Low** | Internal/Public | Manager (or self-service for read-only) |

**Example**:
- Request: Access to **Critical** banking system containing **Restricted** customer PII
- Approval required: (1) Requestor's manager + (2) Banking system owner + (3) CISO
- Justification: "Customer support role requires access to resolve account issues"

---

**REQ-A515-023: Periodic Re-Validation**

**Requirement**:
> Business justification must be re-validated during periodic access reviews (quarterly/annual per criticality).

**Implementation**:
- Access reviews (per A.5.18) include business justification review
- Reviewer confirms: "Is this access still needed for business purposes?"
- If justification no longer valid → access removed
- If justification still valid → access retained + documented

---

## 5. Access Control Roles & Responsibilities

[Organization] defines clear roles and responsibilities for access control governance.

### REQ-A515-030: Access Requestor

**Who**: End user needing access

**Responsibilities**:
- Submit access request via approved ticketing system
- Provide valid business justification (why access is needed)
- Acknowledge acceptable use policy before access granted
- Notify manager when access no longer needed

**Accountability**: Responsible for proper use of granted access

---

### REQ-A515-031: Business Owner / Manager

**Who**: Direct manager of requestor, business unit leader

**Responsibilities**:
- Review access requests from direct reports
- Evaluate business justification (is access truly needed?)
- Approve or reject access request
- Participate in periodic access reviews (quarterly/annual)
- Remove access when employee changes roles or leaves

**Accountability**: Accountable for appropriateness of access granted to team members

**Decision Criteria**:
- ✅ Approve IF: Access needed for job function + justification valid
- ❌ Reject IF: Access not needed for job function OR justification insufficient

---

### REQ-A515-032: System Owner

**Who**: Business or IT leader responsible for system/application

**Responsibilities**:
- Define access requirements for system (roles, access levels)
- Approve access to owned system (especially sensitive/critical systems)
- Classify system criticality (Critical/High/Medium/Low)
- Participate in access reviews for owned system
- Define system-specific access control rules

**Accountability**: Accountable for who has access to their system and why

**Decision Criteria**:
- ✅ Approve IF: User's role requires system access + manager approved
- ❌ Reject IF: User's role doesn't require system access OR security concern

---

### REQ-A515-033: Security Team

**Who**: Information Security / Cybersecurity team

**Responsibilities**:
- Validate access requests comply with access control policy
- Approve access to **Restricted** data (enhanced security review)
- Monitor segregation of duties (SoD) violations
- Approve SoD exceptions (with compensating controls)
- Conduct periodic access audits (sample-based verification)
- Investigate access anomalies (unusual access patterns)

**Accountability**: Accountable for access control policy compliance

**When Security Team Involvement Required**:
- All requests for **Restricted** data access
- All requests for privileged/admin access
- SoD exception requests
- Access for vendors/contractors to critical systems

---

### REQ-A515-034: IT Operations

**Who**: IT infrastructure team, system administrators

**Responsibilities**:
- Provision access AFTER approvals received (no provisioning without approval)
- Implement access in accordance with approved access level
- Deprovision access upon termination/role change (per A.5.16)
- Document access provisioning in identity system
- Escalate provisioning issues (e.g., requested access level not available)

**Accountability**: Responsible for timely and accurate access provisioning

**SLA Requirements**:
- Standard access: Provisioned within 1 business day of final approval
- Sensitive access: Provisioned within 3 business days of final approval
- Emergency access: Same-day provisioning (with after-the-fact justification)

---

### REQ-A515-035: Access Reviewer

**Who**: Managers, system owners, security team (depending on review type)

**Responsibilities**:
- Review access for assigned users/systems (quarterly/annual per criticality)
- Confirm access is still appropriate OR flag for removal
- Document review completion (sign-off)
- Escalate access anomalies (users with excessive access)

**Accountability**: Accountable for accuracy of access review results

**Review Types**:
- **Manager Review**: Managers review all access for their direct reports
- **System Owner Review**: System owners review all access to their systems
- **Security Review**: Security team reviews all privileged access

---

### REQ-A515-036: Internal Audit

**Who**: Internal Audit function (independent of IT/Security)

**Responsibilities**:
- Verify access control effectiveness (sample-based testing)
- Review access provisioning timeliness
- Verify access reviews completed on schedule
- Test segregation of duties controls
- Report access control deficiencies to senior management

**Accountability**: Independent verification of access control governance

**Audit Frequency**: Annual (minimum), more frequently for high-risk areas

---

## 6. Segregation of Duties (SoD) Requirements

### REQ-A515-040: SoD Matrix Defined

**Requirement**:
> [Organization] must maintain a **Segregation of Duties (SoD) Matrix** defining all conflicting role pairs.

**SoD Matrix Structure**:

| Conflict ID | Role A | Role B | Conflict Type | Risk if Not Separated | Separation Level |
|-------------|--------|--------|---------------|----------------------|------------------|
| **SoD-FIN-001** | Request Payment | Approve Payment | Financial | Fraudulent payments | **Mandatory** |
| **SoD-FIN-002** | Enter Journal Entry | Approve Journal Entry | Financial | Fraudulent accounting entries | **Mandatory** |
| **SoD-IT-001** | Developer | Production Admin | IT | Unauthorized production changes | **Mandatory** |
| **SoD-IT-002** | User Administrator | Security Auditor | IT | Cover up unauthorized access | **Recommended** |
| **SoD-IT-003** | Backup Operator | Restore Operator | IT | Unauthorized data restoration | **Recommended** |
| **SoD-HR-001** | Hire Employee | Approve Salary | HR | Fraudulent salary assignments | **Mandatory** |
| **SoD-PROC-001** | Request Purchase | Approve Purchase | Procurement | Fraudulent purchases | **Mandatory** |

**Separation Levels**:
- **Mandatory**: MUST be separated (no exceptions without CISO approval + compensating controls)
- **Recommended**: SHOULD be separated (exceptions allowed with management approval)

**Example**:
- ❌ Alice has both "Request Payment" + "Approve Payment" roles = **SoD-FIN-001 violation** (Mandatory)
- Remediation: Remove one role OR document exception with compensating controls

---

### REQ-A515-041: Automated SoD Violation Detection

**Requirement**:
> SoD violations must be detected automatically through system monitoring.

**Implementation**:
- Access Rights Matrix (per A.5.18) cross-referenced with SoD Matrix
- Monthly automated scan: Identify users with both conflicting roles
- Violation report generated listing:
  - User ID
  - Conflicting roles
  - SoD conflict ID
  - Risk level (mandatory vs. recommended)
  - Exception status (approved exception vs. unresolved violation)

**Example Detection**:
```
User: bob@example.com
Conflicting Roles: "Developer" + "Production Admin"
SoD Conflict: SoD-IT-001 (Mandatory separation)
Status: VIOLATION (no approved exception)
Action Required: Remove one role OR submit exception request
```

---

### REQ-A515-042: SoD Exceptions Require Approval

**Requirement**:
> Exceptions to mandatory SoD requirements require **CISO approval** + documented **compensating controls**.

**Exception Request Process**:
1. User's manager submits SoD exception request
2. Request includes:
   - Business justification (why separation not feasible)
   - Compensating controls (how risk is mitigated)
   - Exception duration (temporary vs. permanent)
3. Security team reviews compensating controls adequacy
4. CISO approves or rejects exception
5. If approved: Exception documented in access rights system

**Compensating Controls Examples**:
- Enhanced monitoring: All actions logged and reviewed by independent party
- Dual authorization: Sensitive actions require second approval
- Restricted access: Access limited to read-only (cannot execute conflicting functions)
- Time-limited: Exception expires after project completion

**Example**:
- Request: Developer needs production admin access for critical system migration
- Justification: "Migration requires both development expertise + production deployment"
- Compensating controls:
  - Duration: 2 weeks (migration project only)
  - Monitoring: All production actions logged + reviewed daily by Security team
  - Approval: Each production change requires Security team approval
- CISO Decision: **Approved** (adequate compensating controls, time-limited)

---

### REQ-A515-043: Compensating Controls Documentation

**Requirement**:
> Compensating controls for SoD exceptions must be documented and verified.

**Documentation Requirements**:
- Exception request ticket
- Business justification
- Compensating controls detailed description
- CISO approval sign-off
- Monitoring evidence (logs, review records)
- Exception expiration date (if temporary)

**Verification**:
- Internal Audit samples SoD exceptions annually
- Verifies compensating controls are actually implemented
- Reports exceptions without adequate compensating controls

---

### REQ-A515-044: SoD Monitoring and Reporting

**Requirement**:
> SoD compliance must be monitored continuously and reported to senior management.

**Reporting Frequency**:
- **Monthly**: SoD violation report to CISO
- **Quarterly**: SoD compliance dashboard to senior management
- **Annually**: SoD control effectiveness to Audit Committee

**Metrics**:
- Total SoD violations detected
- Mandatory violations (must be zero or approved exceptions)
- Recommended violations (trend over time)
- Exceptions granted (count, adequacy of compensating controls)
- Exceptions expired/remediated (closure rate)

---

## 7. Access Control Exception Management

### REQ-A515-050: Exceptions Require Approval

**Requirement**:
> Deviations from access control policy (exceptions) require documented approval.

**What constitutes an exception**:
- Access granted without standard business justification (emergency access)
- Access granted without standard approval workflow (emergency bypass)
- Segregation of duties violation (approved exception per REQ-A515-042)
- Access level higher than role requires (temporary elevation)
- Access duration longer than standard (extended contractor access)

**Exception Categories**:
| Category | Approval Required | Duration | Examples |
|----------|-------------------|----------|----------|
| **Emergency Access** | CISO (after-the-fact) | 24-48 hours | System outage recovery, security incident response |
| **Project-Based** | Manager + System Owner | Project duration | Contractor needs access for 6-month project |
| **SoD Exception** | CISO + compensating controls | As documented | Developer needs production access (with monitoring) |
| **Elevated Privilege** | CISO | Time-limited (days/weeks) | Standard user needs temporary admin for specific task |

---

### REQ-A515-051: Exception Approval Workflow

**Requirement**:
> Exception approval workflow must be documented and enforced.

**Standard Exception Workflow**:
1. **Requestor** submits exception request with:
   - Access details (who, what, what level)
   - Exception type (emergency, project-based, SoD, elevated)
   - Business justification (why exception needed)
   - Duration (how long exception needed)
2. **Manager** reviews and forwards to Security team
3. **Security team** evaluates risk and recommends compensating controls
4. **CISO** approves or rejects exception
5. **IT Operations** provisions access with exception flag
6. **Security team** monitors exception usage

---

### REQ-A515-052: Exception Justification Documented

**Requirement**:
> All exceptions must be documented with clear justification for audit trail.

**Documentation Requirements**:
- Exception request ticket
- Business justification (why exception needed)
- Approval sign-offs (manager, CISO)
- Compensating controls (if applicable)
- Exception start/end date
- Usage monitoring records (access logs)

---

### REQ-A515-053: Periodic Exception Review

**Requirement**:
> Active exceptions must be reviewed quarterly to determine if still needed.

**Review Process**:
- Security team generates list of all active exceptions
- Exception owner confirms exception still needed OR requests closure
- Exceptions no longer needed → access revoked
- Long-running exceptions → escalated to CISO for re-approval

**Escalation Criteria**:
- Exception > 6 months old (should temporary exceptions still be active?)
- Exception without recent usage (is access still needed?)
- Exception without compensating control verification (controls still in place?)

---

### REQ-A515-054: Exception Removal

**Requirement**:
> Exceptions must be removed immediately when no longer needed.

**Automatic Removal Triggers**:
- Exception expiration date reached
- Project completion (for project-based exceptions)
- User role change (exception was role-specific)
- User termination (all access including exceptions removed)

**Manual Removal**:
- Exception owner requests closure
- Quarterly exception review identifies no longer needed
- Internal Audit identifies unnecessary exception

---

## 8. Remote Access Policy Considerations

### REQ-A515-060: Remote Access Subject to Policy

**Requirement**:
> Remote access (VPN, remote desktop, cloud applications) must comply with access control policy.

**Remote Access Requirements**:
- Same business justification required (working remotely ≠ automatic VPN access)
- Same approval workflow (manager approval for VPN access)
- Same least privilege principle (VPN access = only to systems needed for job)
- Enhanced authentication (MFA required for remote access per A.8.5)

**Common Remote Access Types**:
- **VPN Access**: Access to internal network from outside office
- **Remote Desktop**: Access to internal workstations from home
- **Cloud SaaS**: Access to cloud applications (Office 365, Salesforce)

---

### REQ-A515-061: VPN Access Requires Justification

**Requirement**:
> VPN access is not automatic for all employees. Business justification required.

**Valid VPN Justifications**:
- ✅ Remote worker (works from home regularly)
- ✅ On-call support (needs after-hours access for incident response)
- ✅ Travel frequently (needs access while traveling)
- ❌ "Everyone else has VPN" (not a business need)
- ❌ "Might need it someday" (speculative, not current need)

**Implementation**:
- VPN access request submitted via ticketing system
- Manager approves based on business justification
- IT provisions VPN access with appropriate network segmentation
- Quarterly review of VPN access (remove inactive VPN accounts)

---

### REQ-A515-062: Cloud Access Governance

**Requirement**:
> Access to cloud applications (SaaS, IaaS, PaaS) follows same access control policy as on-premises systems.

**Cloud-Specific Considerations**:
- Cloud application access requests require business justification
- Cloud admin access subject to privileged access controls (A.8.2)
- Cloud access reviews conducted same frequency as on-prem systems
- Cloud identity federation (SSO) does NOT bypass access approval requirements

**Example**:
- User requests access to Salesforce (cloud CRM)
- Business justification: "Sales role requires CRM access"
- Approval: Manager approves
- Provisioning: IT assigns Salesforce license + appropriate role
- Review: Annual access review includes Salesforce access

---

## 9. Third-Party Access Governance

### REQ-A515-070: Vendor/Partner Access Requires Sponsorship

**Requirement**:
> Vendor and partner access requires internal sponsor (employee responsible).

**Sponsor Responsibilities**:
- Justify business need for vendor access
- Approve vendor access request
- Monitor vendor access usage
- Request vendor access removal when no longer needed
- Notify Security team of vendor contract end

**Vendor Access Request Workflow**:
1. Internal sponsor submits vendor access request
2. Request includes vendor company, individual name, business justification, contract period
3. Manager approves sponsor's request
4. Security team approves vendor access (enhanced security review)
5. IT provisions vendor account with external identifier (e.g., "EXT-vendorname")

---

### REQ-A515-071: Third-Party Access Time-Bound

**Requirement**:
> Vendor and partner access must be time-bound to contract period with automatic expiration.

**Implementation**:
- Vendor account created with contract end date
- System automatically disables account on contract end date
- Sponsor receives notification 30 days before expiration
- Access extension requires sponsor re-approval

**Example**:
- Vendor: "ACME Consulting" providing IT support services
- Contract period: 2026-01-01 to 2026-06-30
- Vendor account: Created 2026-01-01, auto-expires 2026-06-30
- Sponsor notification: 2026-05-30 (30 days before expiration)
- If contract extended: Sponsor submits access extension request

---

### REQ-A515-072: Third-Party Access Reviewed Quarterly

**Requirement**:
> Vendor and partner access must be reviewed quarterly (more frequently than employee access).

**Quarterly Review Process**:
- Security team generates vendor access report
- Sponsor confirms access still needed OR requests removal
- Sponsor verifies vendor personnel (same individuals or new personnel?)
- Contract end date verified (still accurate or contract extended?)

**Rationale**: Vendor relationships change frequently, quarterly reviews ensure access remains appropriate.

---

### REQ-A515-073: Immediate Revocation on Contract End

**Requirement**:
> Vendor access must be revoked immediately upon contract termination.

**Implementation**:
- Sponsor notifies Security team when vendor contract ends
- IT disables vendor account immediately (within 24 hours)
- All vendor access rights removed
- Verification: Security team confirms vendor access disabled

---

## 10. Integration with HR Processes

### REQ-A515-080: Onboarding Integration

**Requirement**:
> Access control integrated with employee onboarding process.

**Onboarding Workflow** (A.5.16 Joiner Process + A.5.15 Access Control):
1. HR system creates new employee record (hire date, department, manager, job title)
2. Manager receives access request workflow (approve access for new employee)
3. Standard access granted based on role (per RBAC framework A.5.18)
4. Additional access requests submitted as needed (with business justification)
5. New employee receives access by start date

**A.5.15 Role in Onboarding**:
- Define what "standard access" means for each role
- Ensure manager approves all access (even standard)
- Verify business justification for non-standard access

---

### REQ-A515-081: Offboarding Integration

**Requirement**:
> Access control integrated with employee offboarding process.

**Offboarding Workflow** (A.5.16 Leaver Process + A.5.15 Access Control):
1. HR system updates employee termination date
2. IT receives automated notification (disable access on termination date)
3. All access removed immediately (within 1 hour for involuntary termination, end of day for voluntary)
4. Verification: Access removal logged and verified
5. Manager confirms data handover complete before final access removal

**A.5.15 Role in Offboarding**:
- Define deprovisioning timeliness requirements (immediate for termination)
- Ensure all access removed (no orphaned accounts)
- Verify access removal effectiveness

---

### REQ-A515-082: Role Change Integration

**Requirement**:
> Access control integrated with employee role change process.

**Role Change Workflow** (A.5.16 Mover Process + A.5.15 Access Control):
1. HR system updates employee role/department
2. Manager receives access modification workflow
3. Old role access reviewed → removed if no longer needed
4. New role access granted based on new job function
5. Access review triggered by role change (verify all access still appropriate)

**A.5.15 Role in Role Change**:
- Ensure access modified to match new role (not just additive)
- Prevent privilege creep (accumulating access from all previous roles)
- Verify segregation of duties not violated by new role assignment

---

## 11. Audit & Evidence Requirements

### 11.1 Evidence Required for A.5.15 Compliance

**Access Control Policy Document**:
- This document (ISMS-POL-A.5.15-16-18-S2) = formal access control policy
- Evidence of policy approval (CISO signature)
- Evidence of policy distribution (employees acknowledged policy)

**Access Request Approval Records**:
- Access request tickets (showing requestor, justification, approver, approval date)
- Sample size: Minimum 20 access requests per quarter
- Verification: Business justification documented, appropriate approver signed off

**Segregation of Duties Matrix**:
- SoD Matrix document (Section 6 requirements)
- SoD violation reports (monthly scans)
- SoD exception approvals (CISO-approved exceptions with compensating controls)

**Exception Approval Records**:
- Exception request tickets
- CISO approval sign-offs
- Compensating controls documentation
- Exception monitoring records (usage logs)

**Third-Party Access Register**:
- List of all vendor/partner accounts
- Sponsor identification (who sponsored each vendor)
- Contract period (start/end dates)
- Quarterly review records (sponsor confirmation access still needed)

---

### 11.2 Assessment Workbooks (A.5.15 Evidence)

**Workbook 3: Access Review Results**
- Review schedule (quarterly for critical, annual for standard)
- Review completion status (% reviews completed on time)
- SoD violations identified during reviews
- Exception reviews (active exceptions validated)

**Workbook 4: Role Compliance**
- SoD Matrix
- SoD violation report (users with conflicting roles)
- SoD exceptions (approved exceptions with compensating controls)
- RBAC adoption (% users assigned to roles vs. direct access)

---

### 11.3 Audit Testing Approach

**Access Request Audit**:
1. Select sample of 20 access requests (random selection)
2. Verify business justification documented
3. Verify appropriate approver signed off
4. Verify access level matches approved access level
5. Verify provisioning timeliness (within SLA)

**SoD Audit**:
1. Request current SoD violation report
2. Verify all violations are approved exceptions OR remediated
3. Review exception approvals (CISO signature present?)
4. Verify compensating controls implemented (sample 5 exceptions)

**Third-Party Access Audit**:
1. Request vendor access register
2. Verify all vendors have internal sponsor
3. Verify quarterly review completed (last quarter)
4. Select 5 expired contracts → verify access removed

---

## 12. Document Approval

**Prepared By**: [Name], [Title] - [Date]  
**Reviewed By**: [Name], [Title] - [Date]  
**Approved By**: [Name], CISO - [Date]

**Next Review Date**: [Date + 12 months]

**Version History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial policy release |

---

**END OF SECTION 2 (POL-S2 - A.5.15 Access Control)**

**Next Document**: ISMS-POL-A.5.15-16-18-S3_Identity_Management_A516.md
