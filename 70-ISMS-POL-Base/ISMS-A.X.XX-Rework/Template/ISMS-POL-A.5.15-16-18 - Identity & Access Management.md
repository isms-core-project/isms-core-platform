# ISMS-POL-A.5.15-16-18 – Identity & Access Management

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Identity & Access Management |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.15-16-18 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- HR Integration: Chief Human Resources Officer (CHRO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.5.15-16-18 (Implementation Guidance Suite)
- ISMS-POL-A.8.2-3-5 (Authentication & Privileged Access - Technical Security Layer)
- ISMS-REF-A.5.23 (Third-Party Service Provider Registry - Identity Providers)
- ISO/IEC 27001:2022 Controls A.5.15, A.5.16, A.5.18

---

## Executive Summary

This policy establishes [Organization]'s requirements for identity and access management controls to ensure appropriate access governance throughout the complete identity lifecycle in accordance with ISO/IEC 27001:2022 Controls A.5.15, A.5.16, and A.5.18.

**Scope**: This policy applies to all user identities (employees, contractors, vendors, service accounts), all identity systems (Active Directory, Azure AD, Okta, LDAP, custom), and all access types (application, system, data, network) regardless of deployment model or technology.

**Purpose**: Define organizational requirements for identity and access management governance. This policy establishes WHAT IAM controls are required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.15-16-18.

**Combined Control Approach**: These three controls are implemented as a unified framework because they address inseparable aspects of identity and access governance. Separate implementation would result in disconnected processes, redundant activities, and fragmented evidence collection.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, DORA, NIS2, PCI DSS) apply where [Organization]'s business activities trigger applicability.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Controls A.5.15, A.5.16, A.5.18

**ISO/IEC 27001:2022 Annex A.5.15 - Access Control**

> *Rules to control physical and logical access to information and other associated assets shall be established and implemented based on business and information security requirements.*

**Control Objective**: Ensure access to information and systems is controlled based on business justification and security requirements, preventing unauthorized access while enabling legitimate business activities.

**This Policy Addresses**: Access control policy requirements, business justification framework, access classification, segregation of duties requirements, access control roles and responsibilities, exception management, and integration with HR processes.

---

**ISO/IEC 27001:2022 Annex A.5.16 - Identity Management**

> *The full life cycle of identities should be managed.*

**Control Objective**: Ensure user identities are systematically created, maintained, and removed throughout their entire lifecycle, preventing orphaned accounts and ensuring timely provisioning/deprovisioning.

**This Policy Addresses**: Identity lifecycle framework (joiner/mover/leaver), user account provisioning and deprovisioning procedures, account type management, identity repository requirements, orphaned account detection and remediation, and contractor/vendor identity management.

---

**ISO/IEC 27001:2022 Annex A.5.18 - Access Rights**

> *Access rights to information and other associated assets shall be provisioned, reviewed, modified and removed in accordance with the organization's topic-specific policy and rules for access control.*

**Control Objective**: Ensure access rights are appropriately assigned based on roles/business need, periodically reviewed for accuracy, and promptly removed when no longer required.

**This Policy Addresses**: Access rights assignment procedures, role-based access control framework, group membership management, access review/recertification processes, access removal procedures, privilege creep detection, and access rights documentation.

---

**Statement of Applicability Independence**: Although implemented as a unified framework, A.5.15, A.5.16, and A.5.18 are assessed independently in the Statement of Applicability. Each control retains distinct requirements, evidence collection, and compliance scoring for audit purposes.

### 1.2 What This Policy Does

This policy:
- **Defines** requirements for access control governance aligned with organizational risk assessment
- **Establishes** identity lifecycle management framework (joiner/mover/leaver)
- **Specifies** access rights assignment and review procedures
- **Assigns** accountability for IAM control implementation
- **References** applicable regulatory requirements per ISMS-POL-00
- **Integrates** three related controls into unified framework for implementation efficiency

### 1.3 What This Policy Does NOT Do

This policy does NOT:
- **Specify technical implementation details** (see ISMS-IMP-A.5.15-16-18 Implementation Guides)
- **Define identity system technology** (AD, Azure AD, Okta selection based on risk assessment)
- **Provide step-by-step provisioning procedures** (see ISMS-IMP-A.5.15-16-18.2 Identity Lifecycle Process)
- **Define RBAC role catalog** (see ISMS-IMP-A.5.15-16-18.3 Role Definition and Assignment)
- **Specify access review tool selection** (technology selection based on [Organization]'s assessment)
- **Replace risk assessment** (IAM controls are selected based on [Organization]'s risk treatment)
- **Define detailed incident response procedures** (see ISMS-IMP-A.5.15-16-18.4 for incident handling)

**Rationale**: Separating policy requirements from implementation guidance enables:
- Policy stability despite evolving IAM technologies (cloud identity, zero trust)
- Technical agility for technology updates without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Focused audit scope (auditors audit policy compliance, not specific tool configurations)
- Technology-agnostic approach applicable to any identity architecture

### 1.4 Scope

**This policy applies to**:

**User Types**:
- Employees (internal staff, full-time, part-time)
- Contractors (temporary workers, time-bound access)
- Vendors (third-party service providers with system access)
- Service accounts (non-human accounts for applications/systems)
- Shared accounts (discouraged but documented if required with CISO approval)
- Emergency accounts (break-glass accounts for disaster recovery)

**Identity Systems**:
- Active Directory (on-premises)
- Azure Active Directory / Microsoft Entra ID (cloud)
- Okta (cloud identity platform)
- Google Workspace (cloud identity)
- LDAP directories (OpenLDAP, FreeIPA, custom)
- Hybrid environments (AD + Azure AD synchronization)
- Any identity system used by [Organization]

**Access Types**:
- Application access (SaaS, on-premises applications)
- System access (servers, workstations, network devices)
- Data access (databases, file shares, cloud storage)
- Network access (VPN, wireless, remote access)
- Administrative/privileged access

**Personnel**:
- IAM Team, Security Team, HR Team, IT Operations
- Managers (access approvers and reviewers)
- System Owners (application/data custodians)
- All employees (subject to access control policies)

**This policy does NOT apply to**:
- Physical access control systems (covered in A.7.2 Physical Entry Controls)
  - Note: IAM policy governs WHO gets physical access badges, not HOW locks work
- Detailed authentication mechanisms (covered in A.8.5 Secure Authentication)
  - Note: IAM creates identities, A.8.5 defines how they authenticate
- Privileged access management implementation (covered in A.8.2 Privileged Access Rights)
  - Note: IAM defines privileged users, A.8.2 implements PAM controls
- Application-layer authorization (covered in application security controls)

### 1.5 Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**:

**Tier 1: Mandatory Compliance** (Applies to ALL [Organization] operations):

| Regulation | Applicability | Key IAM Requirements |
|------------|---------------|----------------------|
| **Swiss nDSG** | All Swiss operations | Article 8 - Technical and organizational measures for access control; Access to personal data limited to authorized persons; Logging of access to personal data |
| **EU GDPR** | When processing EU personal data | Article 32 - Security of processing (access controls as security measure); Access controls must be appropriate to risk; Access limited to those needing to process personal data; User authentication and authorization required |
| **ISO/IEC 27001:2022** | Certification scope | A.5.15 - Access Control; A.5.16 - Identity Management; A.5.18 - Access Rights |

---

**Tier 2: Conditional Applicability** (Triggered by specific business activities):

**FINMA (Swiss Financial Market Supervisory Authority)**:

**Applicability Determination**: Applies if [Organization] holds FINMA license (bank, securities dealer, insurance company, fund management company)

**Requirements**:
- **FINMA Circular 2023/1** (Operational risks and resilience - banks):
  - Margin 50-62: Information security including access control requirements
  - Margin 56: User administration and authorization
  - Margin 58: Segregation of duties requirements
  - Access control framework aligned with operational risk management
  - User authorization processes (joiner/mover/leaver compliance)
  - Segregation of duties implementation and monitoring
  - Access review and recertification procedures
  - Identity management for all user types (employees, contractors, external)
- **FINMA Circular 2008/7** (Outsourcing - banks): Third-party identity provider management

---

**DORA (Digital Operational Resilience Act)**:

**Applicability Determination**: Applies if [Organization] is EU financial entity

**Requirements**:
- Article 6: ICT risk management framework includes access control governance
- Article 6(5): Identification and documentation of all ICT-supported functions and assets (relates to access mapping)
- Article 28-30: Third-party service provider management (identity provider risk assessment)

---

**NIS2 (Network and Information Security Directive)**:

**Applicability Determination**: Applies if [Organization] is essential or important entity in EU

**Requirements**:
- Article 21(2)(a): Policies on risk analysis and information security (includes access control)
- Article 21(2)(d): Policies on access control and asset management
- Article 21(2)(f): Practices for identity and access management

---

**PCI DSS (Payment Card Industry Data Security Standard)**:

**Applicability Determination**: Applies if [Organization] stores, processes, or transmits payment card data

**Requirements**:
- Requirement 7: Restrict access to cardholder data by business need-to-know
- Requirement 8: Identify and authenticate access to system components
  - 8.2: User identification and authentication management
  - 8.3: Multi-factor authentication for remote access
  - 8.6: Use of application and system accounts

---

**Compliance Determination**: Legal/Compliance Officer determines applicability of Tier 2 regulations based on [Organization]'s business activities and regulatory status.

---

**Tier 3: Informational Reference / Best Practice Alignment**:

**NIST SP 800-53** (Access Control & Identity Management):
- AC-2: Account Management (aligns with A.5.16)
- AC-3: Access Enforcement (aligns with A.5.15)
- AC-5: Separation of Duties (aligns with A.5.15)
- AC-6: Least Privilege (aligns with A.5.15)
- IA-4: Identifier Management (aligns with A.5.16)

**CIS Controls**:
- CIS Control 5: Account Management
- CIS Control 6: Access Control Management

**ISO/IEC 27002:2022**: Detailed guidance for controls A.5.15, A.5.16, A.5.18

**United States Federal Requirements**: References to US federal frameworks (FISMA, NIST cybersecurity requirements) apply only where [Organization] has explicit US federal contractual obligations, as defined in ISMS-POL-00.

---

## 2. Requirements Framework

### 2.1 Access Control Policy Requirements (A.5.15)

[Organization] SHALL implement the following access control governance requirements:

**2.1.1 Access Control Principles**

[Organization]'s access control framework is based on the following principles:

| Principle | Requirement | Implementation |
|-----------|-------------|----------------|
| **Least Privilege** | Users granted minimum access required for job function | Role-based access, periodic review removes excess rights |
| **Need-to-Know** | Access restricted to business need | Business justification required for all access requests |
| **Segregation of Duties (SoD)** | Conflicting responsibilities separated to prevent fraud/error | SoD matrix defines incompatible roles, violations detected and remediated |
| **Defense in Depth** | Multiple layers of access control | Network segmentation, application-level authorization, data-level encryption |
| **Deny by Default** | Access denied unless explicitly granted | Whitelist approach, all access requires approval |

**2.1.2 Access Classification Framework**

[Organization] classifies access based on multiple dimensions to determine appropriate controls:

**User Type Classification**:
- **Employee** (Standard): Full-time and part-time staff with employment contract
- **Contractor** (Time-Bound): Temporary workers with defined contract end date
- **Vendor** (External): Third-party service providers requiring system access
- **Service Account** (Non-Human): Application/system accounts for automated processes
- **Shared Account** (Exceptional): Accounts used by multiple individuals (requires CISO approval)
- **Emergency** (Break-Glass): Emergency access accounts for disaster scenarios

**System Criticality Classification**:
- **Critical**: Systems whose unavailability causes immediate business disruption (revenue-generating, customer-facing production systems)
- **High**: Systems supporting critical business functions (HR systems, financial systems, core infrastructure)
- **Medium**: Systems supporting normal business operations (collaboration tools, internal applications)
- **Low**: Systems with minimal business impact (test systems, development tools)

**Data Sensitivity Classification** (per [Organization]'s data classification scheme):
- **Restricted**: Highest sensitivity (personal data under GDPR/nDSG, payment card data, trade secrets)
- **Confidential**: High sensitivity (business contracts, employee data, intellectual property)
- **Internal**: Moderate sensitivity (internal communications, operational data)
- **Public**: No sensitivity (published information, marketing materials)

**Access Level Classification**:
- **Read**: View information without modification
- **Write**: Create or modify information
- **Admin**: System administration, configuration changes
- **Privileged**: Elevated access (root, domain admin, database admin)

**Implementation Note**: Specific classification criteria (which systems are "critical", which data is "restricted") are defined by [Organization] based on business context and risk assessment. See ISMS-IMP-A.5.15-16-18.1 for classification methodology.

**2.1.3 Business Justification Requirements**

All access requests SHALL include documented business justification:

| Access Type | Justification Required | Approval Authority |
|-------------|------------------------|-------------------|
| **Standard User Access** | Job role and business need | Direct manager |
| **Sensitive System Access** | Specific business requirement | System owner + Manager |
| **Confidential/Restricted Data** | Data processing purpose and legal basis | Data owner + CISO |
| **Privileged/Admin Access** | Technical justification and necessity | CISO + CIO |
| **Third-Party Vendor Access** | Contract reference and scope of work | Business sponsor + CISO |
| **Shared Account** (exceptional) | Technical impossibility of individual accounts | CISO (with compensating controls) |

**Approval Workflow**:
1. Requester submits access request via ticketing system
2. Request includes: User identity, system/data requested, access level, business justification, duration (if temporary)
3. Automated workflow routes to appropriate approver(s) based on access type
4. Approver verifies business need and legitimacy
5. Upon approval, IT Operations provisions access within SLA
6. Audit trail maintained (requester, approver, timestamp, justification)

**Implementation Note**: Specific approval workflows and ticketing system integration are documented in ISMS-IMP-A.5.15-16-18.1 (Access Control Governance).

**2.1.4 Segregation of Duties (SoD)**

[Organization] implements segregation of duties to prevent fraud, error, and conflicts of interest:

**SoD Matrix**:
[Organization] maintains a Segregation of Duties matrix identifying incompatible role combinations. Examples of conflicting roles:

| Role A | Role B | Risk if Combined | Mitigation |
|--------|--------|------------------|------------|
| Expense Submitter | Expense Approver | Approve own expenses (fraud) | Manager review required |
| Purchase Requisitioner | Purchase Approver | Approve own purchases (fraud) | Separate approval authority |
| Developer | Production Deployer | Deploy unauthorized code (error/malicious) | Change approval board + segregated environments |
| Database Admin | Application Owner | Manipulate data without detection | Audit logging + periodic review |
| User Administrator | Security Auditor | Create accounts and audit self (fraud) | Independent audit function |

**SoD Violation Detection**:
- Automated scanning identifies users with conflicting roles (monthly)
- SoD violations reported to Security Team
- Each violation requires: CISO review, documented exception approval OR immediate remediation

**SoD Exception Approval**:
When separation is technically infeasible (small organization, specialized skills):
- CISO approval required with documented business justification
- Compensating controls implemented (enhanced logging, manager review, periodic audits)
- Exception reviewed annually for continued necessity

**Implementation Note**: Complete SoD matrix and detection procedures are documented in ISMS-IMP-A.5.15-16-18.1 (Access Control Governance).

**2.1.5 Access Control Roles and Responsibilities**

[Organization] assigns clear accountability for access control activities:

| Role | Responsibility |
|------|----------------|
| **Access Requesters** | Submit access requests with valid business justification; Use access appropriately per Acceptable Use Policy |
| **Access Approvers** (Managers) | Approve/deny access requests for direct reports; Verify business need and appropriateness; Accountability for team members' access |
| **Access Approvers** (System Owners) | Approve/deny access to systems they own; Define access requirements for their systems; Participate in access reviews |
| **Access Provisioners** (IT Operations) | Provision access upon proper approval; Verify approver authority; Meet provisioning SLAs; Maintain audit trail |
| **Access Reviewers** (Managers) | Review direct reports' access quarterly/annually; Certify access is appropriate or request removal; Accountability for review completion |
| **Access Reviewers** (System Owners) | Review access to systems they own; Verify access aligns with business need; Remove inappropriate access |
| **Security Team** | Monitor access patterns and anomalies; Investigate access violations; Enforce access control policies; Conduct periodic assessments |
| **IAM Team** | Maintain identity systems; Automate joiner/mover/leaver processes; Detect orphaned accounts; Generate access reports |

**Detailed RACI Matrix**: Comprehensive RACI (Responsible, Accountable, Consulted, Informed) matrix for all IAM processes is documented in ISMS-IMP-A.5.15-16-18.1.

**2.1.6 Exception Management**

Access control exceptions require formal approval and periodic review:

**Exception Scenarios**:
- Shared accounts (where individual accounts technically infeasible)
- Extended provisioning timelines (complex system integration)
- Delayed access reviews (business constraints, resource limitations)
- SoD violations (small organization, cannot separate duties)
- Privileged access for non-IT personnel (business requirement)

**Exception Request Process**:
1. Requester documents exception need and business justification
2. Security Team assesses risk and proposes compensating controls
3. CISO approves exception with compensating controls
4. Exception documented in exception register (exception ID, justification, risk, compensating controls, expiry date)
5. Exceptions reviewed annually for continued necessity

**Compensating Controls Examples**:
- Shared account → Enhanced logging, manager approval for each use, quarterly access review
- Extended provisioning → Manual interim access, expedited processing for critical users
- Delayed review → Increased review depth when completed, interim spot checks
- SoD violation → Manager review of all conflicting transactions, quarterly audits

**Implementation Note**: Exception request templates and approval workflows are documented in ISMS-IMP-A.5.15-16-18.1.

**2.1.7 Integration with HR Processes**

Access control integrates with HR lifecycle events:

| HR Event | Access Control Action | Timeline | Responsibility |
|----------|----------------------|----------|----------------|
| **New Hire** | Trigger joiner process, provision access | Access ready by start date | HR triggers, IT provisions |
| **Role Change** | Trigger mover process, adjust access | Within 2 business days | HR triggers, Manager approves, IT provisions |
| **Promotion** | Review and update access rights | Within 5 business days | Manager reviews, IT updates |
| **Termination** | Trigger leaver process, disable all access | Immediate (within 1 hour for termination for cause) | HR triggers, IT deprovisions |
| **Leave of Absence** | Suspend access (if extended leave >30 days) | By leave start date | Manager requests, IT suspends |
| **Contract End** | Remove contractor access | On contract end date | HR triggers, IT deprovisions |

**HR System Integration**: HR system is designated as authoritative source for identity lifecycle events. Integration methods include API integration, automated file feeds, or manual notifications depending on technical capabilities.

---

### 2.2 Identity Management Requirements (A.5.16)

[Organization] SHALL implement the following identity lifecycle management requirements:

**2.2.1 Identity Lifecycle Framework**

[Organization] manages the complete identity lifecycle through standardized processes:

**Joiner Process** (New User Onboarding):
- **Trigger**: HR system notification of new hire/contractor
- **Actions**: Create user account, assign initial access based on role, provide credentials
- **Timeline**: Access ready by employee start date (target: ≤0 days delay)
- **Responsibilities**: HR triggers → IAM Team creates account → IT Operations provisions access → Manager verifies

**Mover Process** (Role Change, Transfer):
- **Trigger**: HR system notification of role change, department transfer, promotion
- **Actions**: Review current access, adjust to align with new role, remove access from previous role
- **Timeline**: Access updated within 2 business days of role change
- **Responsibilities**: HR triggers → Manager reviews access → IAM Team updates identity → IT Operations adjusts rights

**Leaver Process** (Termination, Resignation, Contract End):
- **Trigger**: HR system notification of termination, resignation, contract expiration
- **Actions**: Disable all accounts, remove all access, archive mailbox/files per retention policy
- **Timeline**: 
  - Termination for cause: Immediate (within 1 hour)
  - Voluntary resignation: Same business day
  - Contractor end date: Scheduled on contract end date
- **Responsibilities**: HR triggers → IAM Team disables accounts → IT Operations verifies removal → Manager confirms

**Implementation Note**: Detailed joiner/mover/leaver procedures, including automation workflows and manual fallback procedures, are documented in ISMS-IMP-A.5.15-16-18.2 (Identity Lifecycle Process).

**2.2.2 User Account Provisioning**

[Organization] provisions user accounts systematically:

**Provisioning Workflow**:
1. HR system triggers joiner event (API integration or file feed)
2. IAM Team receives notification and validates employee data
3. User account created in primary identity system (AD, Azure AD, Okta)
4. Initial access assigned based on role template or manager specification
5. Account activation procedures completed (initial password, MFA enrollment)
6. User notified of account creation and onboarding instructions

**Provisioning Timeliness**:
- **Target**: Access ready by employee start date (≤0 days delay)
- **Measurement**: Days between hire date and account creation
- **Reporting**: Monthly provisioning timeliness metrics in IAM assessment workbooks

**Account Creation Standards**:
- **Naming Convention**: Standardized format (firstname.lastname or employee_id)
- **Attributes**: Name, email, department, manager, hire date, account type
- **Initial Access**: Based on job role template or manager request with approval
- **Security Settings**: MFA enrollment required, password complexity enforced, account expiration for contractors

**Implementation Note**: Specific provisioning procedures, including technology-specific steps for AD, Azure AD, Okta, and other identity systems, are documented in ISMS-IMP-A.5.15-16-18.2.

**2.2.3 User Account Deprovisioning**

[Organization] deprovisions user accounts promptly to prevent unauthorized access:

**Deprovisioning Workflow**:
1. HR system triggers leaver event (termination, resignation, contract end)
2. IAM Team receives notification and initiates deprovisioning
3. User account disabled immediately (authentication prevented)
4. Access removed from all systems (applications, network, data)
5. Mailbox archived or forwarded per manager request
6. Account deletion scheduled (typically 90 days after disable for recovery purposes)
7. Verification completed (IT Operations confirms all access removed)

**Deprovisioning Timeliness**:

| Scenario | Timeline | Rationale |
|----------|----------|-----------|
| **Termination for Cause** | Immediate (within 1 hour) | Security risk, prevent data exfiltration |
| **Voluntary Resignation** | Same business day | Employee goodwill, minimal risk during notice period |
| **Contractor End Date** | On contract end date (scheduled) | Time-bound access, automated expiration |
| **Role Change** (mover) | Within 2 business days | Access adjustment, not full removal |

**Account Disablement vs. Deletion**:
- **Disable**: Immediate action preventing authentication while preserving account data
- **Delete**: Permanent removal after retention period (typically 90 days)
- **Rationale**: Disablement allows recovery if termination reversed; deletion prevents account sprawl

**Data Handover Procedures**:
- Manager specifies data handover requirements (mailbox access, file ownership transfer)
- IT Operations executes handover before account deletion
- Handover completion required before final account deletion

**Implementation Note**: Detailed deprovisioning procedures, including emergency deprovisioning for security incidents, are documented in ISMS-IMP-A.5.15-16-18.2.

**2.2.4 Account Type Management**

[Organization] manages different account types with appropriate controls:

**Employee Accounts** (Standard user accounts):
- **Characteristics**: Tied to employment, permanent until termination
- **Lifecycle**: Joiner → Mover (as needed) → Leaver
- **Ownership**: Individual employee
- **Expiration**: None (active until termination)

**Contractor/Vendor Accounts** (Time-bound external access):
- **Characteristics**: Tied to contract, time-limited, requires internal sponsor
- **Lifecycle**: Joiner (contract start) → Mover (if needed) → Leaver (contract end)
- **Ownership**: Individual contractor, sponsored by internal employee
- **Expiration**: Mandatory (contract end date)
- **Access Extension**: Requires sponsor approval + contract extension verification
- **Special Requirements**: NDA verification, sponsor accountability

**Service Accounts** (Application/system accounts for automated processes):
- **Characteristics**: Non-human, no interactive login, used by applications/scripts
- **Lifecycle**: Created upon application deployment → Updated as needed → Deleted upon decommissioning
- **Ownership**: Application owner or technical lead (documented)
- **Expiration**: No expiration (runs until service decommissioned)
- **Special Requirements**: Password rotation (quarterly minimum), privileged access controls, usage logging

**Shared Accounts** (Multiple users, strongly discouraged):
- **Characteristics**: Single account used by multiple individuals
- **Usage**: ONLY when technical constraints prevent individual accounts
- **Approval**: CISO approval required with documented justification
- **Compensating Controls**: Enhanced logging, manager approval for each use, quarterly access review
- **Alternatives Preferred**: Individual accounts with shared resource access

**Emergency/Break-Glass Accounts** (Disaster recovery privileged access):
- **Characteristics**: Dormant privileged accounts for emergency scenarios
- **Usage**: ONLY during disaster scenarios when normal access unavailable
- **Storage**: Credentials stored in secure vault, access requires dual authorization
- **Monitoring**: Usage triggers immediate alert and investigation
- **Review**: Quarterly verification that accounts remain dormant

**Implementation Note**: Account type-specific procedures, including service account password rotation and break-glass account management, are documented in ISMS-IMP-A.5.15-16-18.2.

**2.2.5 Identity Repository Requirements**

[Organization] maintains identity data with appropriate governance:

**Authoritative Source**:
- HR system designated as authoritative source of employee identity data
- Contractor management system or procurement system for contractor/vendor identities
- Identity data flows from authoritative source to identity systems (AD, Azure AD, Okta)

**Identity Synchronization** (if multiple identity systems):
- Automated synchronization between identity repositories (AD → Azure AD, AD → Okta)
- Synchronization frequency: Real-time or near-real-time (≤15 minutes)
- Synchronization failures detected and alerted
- Manual synchronization fallback for failures

**Identity Data Accuracy**:
- Identity attributes maintained current (name, email, department, manager)
- Manager updates trigger identity system updates
- Data quality monitored (missing attributes, stale data flagged)
- Annual identity data validation (HR verifies identity system accuracy)

**Implementation Note**: Identity repository integration methods and synchronization technologies are documented in ISMS-IMP-A.5.15-16-18.2.

**2.2.6 Orphaned Account Detection and Remediation**

[Organization] systematically detects and remediates orphaned accounts:

**Orphaned Account Definition**:
- Account without valid business owner (employee no longer with organization)
- Account not linked to active employee in HR system
- Contractor account beyond contract end date
- Service account without documented owner

**Detection Methodology**:
- Cross-reference identity systems (AD, Azure AD, Okta) with HR system (monthly)
- Identify accounts not matching active employees or contractors
- Flag accounts inactive >90 days (no successful authentication)
- Report orphaned accounts to IAM Team and Security Team

**Detection Frequency**: Monthly scans

**Remediation Procedures**:
1. **Investigation** (Week 1): IAM Team attempts to identify owner or determine legitimate need
2. **Notification** (Week 2): If owner identified, owner verifies account necessity
3. **Disable** (Week 3): If no response or no legitimate need, account disabled
4. **Delete** (Week 4+): After 30 days disabled, account deleted

**Exceptions**: Orphaned accounts with documented business justification (e.g., former employee mailbox retained for litigation hold) require CISO approval and periodic review.

**Implementation Note**: Orphaned account detection tools and automated remediation workflows are documented in ISMS-IMP-A.5.15-16-18.2.

**2.2.7 Contractor/Vendor Identity Management**

[Organization] manages contractor and vendor identities with appropriate controls:

**Sponsorship Model**:
- Every contractor/vendor account requires internal sponsor (permanent employee)
- Sponsor accountability: Verify business need, approve access, review quarterly
- Sponsor change process: If sponsor leaves, new sponsor assigned or access removed

**Time-Bound Access**:
- All contractor/vendor accounts have mandatory expiration date (contract end date)
- Account automatically disabled on expiration date (prevents forgotten access)
- Access extension requires: Sponsor approval + HR verification of contract extension

**Access Extension Approval**:
1. Contractor requests access extension 2 weeks before expiration
2. Sponsor approves with business justification
3. HR verifies contract extended
4. IAM Team extends account expiration date
5. Extension documented in audit trail

**Vendor Identity Lifecycle**:
- Vendor onboarding: NDA signature verification + sponsor assignment
- Vendor access: Limited to systems necessary for service delivery
- Vendor monitoring: Enhanced logging, quarterly access review
- Vendor offboarding: Contract termination triggers immediate access removal

**Implementation Note**: Contractor/vendor lifecycle procedures and vendor risk management are documented in ISMS-IMP-A.5.15-16-18.2.

---

### 2.3 Access Rights Management Requirements (A.5.18)

[Organization] SHALL implement the following access rights assignment and review requirements:

**2.3.1 Access Rights Assignment**

[Organization] assigns access rights systematically through standardized processes:

**Access Request and Approval Workflow**:
1. **Request Submission**: User or manager submits access request via ticketing system
2. **Business Justification**: Request includes business need, role requirement, system/data scope
3. **Approval Routing**: Automated workflow routes to appropriate approver (manager, system owner, CISO)
4. **Approval Decision**: Approver verifies business need and grants/denies access
5. **Provisioning**: IT Operations provisions access upon approval
6. **Notification**: User notified when access granted
7. **Documentation**: Request logged with requester, approver, timestamp, justification

**Role-Based Access Control (RBAC) Framework**:
- Preferred method: Assign users to predefined roles rather than direct access assignments
- Role templates: Standardized role definitions with associated access rights
- Role catalog: Published repository of available roles with descriptions and access included
- RBAC adoption target: ≥80% users assigned to roles (vs. direct access assignments)

**Access Provisioning Timeliness**:

| Request Type | SLA | Measurement |
|--------------|-----|-------------|
| **Standard Access** | Within 2 business days | Time from approval to provisioning |
| **Sensitive Access** | Within 5 business days | Time from approval to provisioning (additional verification) |
| **Emergency Access** | Within 4 hours | Time from approval to provisioning (business-critical) |

**Access Grant Documentation**:
- Every access grant documented with: User identity, system/data accessed, access level, business justification, approver, approval date
- Documentation retained for audit period (minimum 3 years)
- Access history queryable for user access reports and audits

**Implementation Note**: Access request workflows, RBAC role templates, and provisioning procedures are documented in ISMS-IMP-A.5.15-16-18.3 (Role Definition and Assignment).

**2.3.2 Role Definition and RBAC**

[Organization] implements role-based access control to standardize and streamline access management:

**Role Catalog Maintenance**:
- **Role Definition**: Each role documented with name, description, business owner, access rights included
- **Role-to-Access Mapping**: Roles mapped to specific systems, applications, data, and access levels
- **Role Catalog Publication**: Role catalog published and accessible to managers for access requests
- **Role Updates**: Role definitions updated when business needs or access requirements change
- **Role Owner**: Each role has designated business owner accountable for role accuracy

**Role Definition Standards**:

| Role Attribute | Requirement | Example |
|----------------|-------------|---------|
| **Role Name** | Clear, descriptive name | "Finance Analyst", "HR Manager", "IT Operations Engineer" |
| **Description** | Business purpose and scope | "Access to financial systems for monthly reporting and analysis" |
| **Business Owner** | Department or function | Finance Department, HR Department, IT Operations |
| **Access Included** | Systems, applications, data, access level | ERP (Read), BI Tool (Write), Financial Database (Read-only) |
| **Approval Requirements** | Who can assign this role | Department manager, CISO (for privileged roles) |
| **Review Frequency** | How often role reviewed | Annually or when business needs change |

**Role Assignment Criteria**:
- Job function alignment: Role matches user's job responsibilities
- Business need verification: Manager confirms role necessary for job performance
- Least privilege: Role provides minimum access required
- Role hierarchy: Roles may inherit from other roles (if applicable)

**Role Review and Maintenance**:
- Annual role review: Business owner verifies role definition still accurate and necessary
- Usage analysis: Review which users assigned to role, verify appropriate
- Access creep detection: Identify users accumulating multiple roles unnecessarily
- Role consolidation: Merge duplicate or overlapping roles

**Implementation Note**: Complete role catalog, role definition templates, and role assignment procedures are documented in ISMS-IMP-A.5.15-16-18.3.

**2.3.3 Group Membership Management**

[Organization] manages group memberships with appropriate governance:

**Group Purpose Documentation**:
- Every group documented with: Purpose (what access does this group grant), owner, members, creation date
- Group naming convention: Descriptive names indicating purpose (e.g., "Finance-ERP-Users", "IT-Server-Admins")
- Group types: Security groups (access control), distribution groups (email), dynamic groups (auto-membership based on attributes)

**Group Ownership Assignment**:
- Every group has designated owner (individual accountable for membership accuracy)
- Owner responsibilities: Approve membership requests, review membership quarterly, remove inappropriate members
- Owner change process: If owner leaves organization, new owner assigned or group deleted

**Group Membership Approval**:
- Membership changes require group owner approval
- Approval process: User or manager requests → Group owner approves → IT Operations adds member
- Self-service options: Users can request membership via self-service portal, routed to group owner for approval

**Nested Group Management** (if applicable):
- Nested groups: Groups that are members of other groups (group A is member of group B)
- Documentation: Nested relationships documented to understand effective permissions
- Complexity management: Limit nesting depth to avoid unintended access grants (typically ≤3 levels)

**Implementation Note**: Group management procedures, including nested group strategies and dynamic group automation, are documented in ISMS-IMP-A.5.15-16-18.3.

**2.3.4 Access Review and Recertification**

[Organization] reviews access rights periodically to ensure appropriateness:

**Access Review Frequency**:

| System/Data Classification | Review Frequency | Reviewer | Scope |
|----------------------------|------------------|----------|-------|
| **Critical Systems / Privileged Access** | Quarterly | CISO + Security Team | All privileged accounts and critical system access |
| **High-Risk Systems / Confidential Data** | Semi-Annual | System owners + Managers | Access to confidential data and high-risk systems |
| **Standard Systems / Internal Data** | Annual | Managers | All direct reports' access to standard systems |

**Review Scope**:
- All users: Every user account reviewed
- All systems: Access to all systems and applications
- All groups: Membership in all security groups
- Privileged access: Special focus on administrative and elevated access

**Reviewer Accountability**:
- **Managers**: Review direct reports' access, certify appropriate or request removal
- **System Owners**: Review access to systems they own, verify business need
- **Security Team**: Review privileged access, verify technical necessity
- **Accountability**: Reviewers digitally sign off on access review, accepting accountability

**Review Process**:
1. **Preparation**: IAM Team generates access review workbooks (users, systems, groups, access levels)
2. **Distribution**: Workbooks distributed to reviewers (managers, system owners)
3. **Review Execution**: Reviewers verify each user's access is appropriate
4. **Decision Options**: Approve (access appropriate), Remove (access no longer needed), Justify (exception with documentation)
5. **Remediation**: Access removal requests executed within 5 business days
6. **Documentation**: Review results documented (who reviewed, what was certified/removed, timestamp)
7. **Evidence Retention**: Review results retained for audit period (3 years minimum)

**Review Evidence Retention**: All access review results retained for minimum 3 years, including: Review period, reviewer identity, users reviewed, access approved/removed, justifications for exceptions

**Remediation of Review Findings**:
- **Access Removal**: Inappropriate access removed within 5 business days of review decision
- **Access Justification**: If access retained despite appearing inappropriate, business justification documented
- **Escalation**: Unresponsive reviewers escalated to their manager, CISO, and executive management

**Implementation Note**: Access review procedures, including automated review tool configuration and manual review templates, are documented in ISMS-IMP-A.5.15-16-18.4 (Access Review Process).

**2.3.5 Access Removal**

[Organization] removes access promptly when no longer required:

**Access Removal Timelines**:

| Trigger | Timeline | Process |
|---------|----------|---------|
| **Termination** (for cause) | Immediate (within 1 hour) | Emergency deprovisioning procedure |
| **Termination** (voluntary) | Same business day | Standard leaver process |
| **Role Change** | Within 2 business days | Remove access from previous role, add access for new role |
| **Project Completion** | Within 5 business days | Project owner requests removal, IT Operations executes |
| **Access Review Finding** | Within 5 business days | Review decision documented, IT Operations removes access |
| **Security Incident** | Immediate | Emergency access removal, investigation |

**Access Removal Verification**:
- IT Operations confirms access removed from all systems
- Verification checklist: AD account disabled, application access removed, VPN access removed, building badge deactivated (if applicable)
- Verification documented in ticketing system
- Periodic spot checks: Security team verifies access actually disabled (not just documented)

**Audit Trail of Removals**:
- All access removals logged with: User, system, access level, removal date, removal reason, requestor, executor
- Logs retained for audit period (3 years minimum)
- Logs queryable for compliance reporting

**Implementation Note**: Access removal procedures, including emergency removal for security incidents, are documented in ISMS-IMP-A.5.15-16-18.4.

**2.3.6 Privilege Creep Detection**

[Organization] detects and remediates privilege creep systematically:

**Privilege Creep Definition**: Accumulation of excess access rights over time as users change roles but retain access from previous roles.

**Detection Methodology**:
1. **Current Access Inventory**: Generate current access for each user (systems, groups, roles)
2. **Required Access Baseline**: Determine required access based on current job role
3. **Comparison**: Compare current access vs. required access
4. **Excess Access Identification**: Flag access not aligned with current role (privilege creep)
5. **Reporting**: Report privilege creep cases to managers and Security Team

**Remediation Procedures**:
1. **Manager Review**: Manager verifies whether excess access is legitimate (project work, cross-functional role)
2. **Business Justification**: If excess access is legitimate, document justification
3. **Access Removal**: If excess access is not justified, remove within 5 business days
4. **Prevention**: Future role changes trigger automatic access review and cleanup

**Prevention Strategies**:
- Role-based provisioning (users assigned to roles, not individual access grants)
- Automated access reviews (quarterly/annual removal of unnecessary access)
- Leaver process improvements (ensure all access removed, not just primary systems)

**Implementation Note**: Privilege creep detection tools and automated remediation workflows are documented in ISMS-IMP-A.5.15-16-18.4.

**2.3.7 Emergency Access Procedures**

[Organization] manages emergency access with appropriate controls:

**Break-Glass Account Management**:
- Dormant privileged accounts for emergency scenarios when normal access unavailable
- Credentials stored in secure vault with dual-authorization access
- Usage triggers immediate alert to CISO and Security Team
- All actions logged for post-incident review
- Accounts reviewed quarterly to verify they remain dormant and functional

**Emergency Access Approval**:
- Emergency access granted when business-critical need and normal approval process too slow
- Approval required within 24 hours of access grant (after-the-fact justification)
- CISO approval required for emergency privileged access
- Emergency access logged and reviewed in security team meeting

**Emergency Access Logging**:
- All emergency access usage logged in detail (user, system, actions performed, duration)
- Logs reviewed immediately by Security Team
- Incident report generated for any emergency access usage

**Emergency Access Review**:
- Quarterly review of break-glass accounts (verify functionality, credential rotation)
- Review of all emergency access grants in past quarter
- Lessons learned: Identify why normal process failed, improve processes

**Implementation Note**: Break-glass account procedures and emergency access approval workflows are documented in ISMS-IMP-A.5.15-16-18.3.

**2.3.8 Access Rights Documentation**

[Organization] maintains comprehensive access rights documentation:

**Access Matrix**:
- User-to-system mapping: Which users have access to which systems
- Access level documentation: Read, Write, Admin, Privileged for each user-system pair
- Group membership: Users assigned to groups, groups granting access to systems
- Role assignments: Users assigned to roles, roles including specific access rights

**Business Justification Documentation**:
- All access grants include documented business justification
- Justification includes: Why access needed, what business function requires access, approval date and approver

**Access Rights Inventory**:
- Current and accurate access inventory maintained (updated within 30 days)
- Inventory queryable for: User access reports, system access reports, privilege escalation analysis
- Inventory feeds into access review processes (baseline for reviewing appropriateness)

**Implementation Note**: Access matrix generation tools and access reporting procedures are documented in ISMS-IMP-A.5.15-16-18.5 (IAM Assessment Procedures).

---

## 3. Governance & Compliance

### 3.1 Roles and Responsibilities

**Executive Management** (CEO, Board):
- **Accountability**: Overall IAM program effectiveness and risk acceptance
- **Responsibilities**: Approve IAM policy; Allocate budget and resources; Accept residual risks; Support security program; Escalation point for critical IAM failures

**Chief Information Security Officer (CISO)**:
- **Accountability**: IAM policy implementation and compliance
- **Responsibilities**: Approve IAM policy updates; Approve high-risk exceptions; Approve privileged access grants; Review quarterly IAM metrics; Escalate critical issues to Executive Management; Annual policy review

**Chief Information Officer (CIO)**:
- **Accountability**: IAM technical infrastructure and operations
- **Responsibilities**: Implement IAM technologies; Allocate IT resources for IAM automation; Support identity system operations; Technology selection (identity platforms, provisioning tools)

**Chief Human Resources Officer (CHRO)**:
- **Accountability**: HR system as authoritative source for identity data
- **Responsibilities**: Maintain accurate employee data; Trigger joiner/mover/leaver events; Coordinate terminations with IT; Ensure manager accountability for access reviews

**Security Team**:
- **Responsibilities**: Develop and maintain IAM policy; Monitor IAM compliance; Conduct periodic IAM assessments; Investigate access-related incidents; Generate IAM metrics; Report to CISO; Incident response for access violations

**IAM Team** (or IT Operations if no dedicated IAM team):
- **Responsibilities**: Implement identity lifecycle processes; Maintain identity systems (AD, Azure AD, Okta); Execute provisioning/deprovisioning; Maintain role catalog; Generate assessment workbooks; Detect orphaned accounts; Technical support for access requests

**HR Team**:
- **Responsibilities**: Trigger joiner events (new hire notifications); Trigger leaver events (termination notifications); Trigger mover events (role change notifications); Maintain accurate employee data in HR system; Coordinate with IT on terminations

**IT Operations**:
- **Responsibilities**: Provision access per IAM team instructions; Maintain application-specific access controls; Support access request workflow; Technical implementation of deprovisioning

**Managers** (People Managers):
- **Accountability**: Direct reports' access appropriateness
- **Responsibilities**: Approve access requests for direct reports; Review direct reports' access (quarterly/annual); Notify HR/IT immediately upon termination; Complete data handover for departing employees

**System Owners** (Application/Data Custodians):
- **Accountability**: Access control for systems/data they own
- **Responsibilities**: Define access requirements; Approve access to sensitive systems; Review access to their systems (quarterly/annual); Maintain system-specific access documentation; Participate in access classification

**Internal Audit**:
- **Responsibilities**: Verify IAM control effectiveness; Test compliance with IAM policy; Review assessment workbooks; Report audit findings to CISO and Executive Management

**External Auditors**:
- **Responsibilities**: Verify IAM controls for ISO 27001 certification; Test evidence from assessment workbooks; Report certification findings

**All Employees, Contractors, Vendors**:
- **Responsibilities**: Request access only when business need exists; Use access appropriately (comply with Acceptable Use Policy); Report suspicious access activity; Acknowledge termination of access upon departure

**Detailed RACI Matrix**: Complete RACI (Responsible, Accountable, Consulted, Informed) matrix for all IAM processes is documented in ISMS-IMP-A.5.15-16-18.1 (Access Control Governance).

### 3.2 Assessment and Verification

[Organization] verifies IAM control effectiveness through structured assessment framework:

**Assessment Framework Overview**:
- **Assessment Approach**: 5 workbooks + 1 dashboard
- **Assessment Frequency**: Monthly (user inventory updates), Quarterly (access reviews for critical systems), Annual (comprehensive assessment)
- **Assessment Ownership**: Security Team leads, IAM Team provides data, Internal Audit verifies

**Assessment Workbooks**:

| Workbook | Purpose | Update Frequency | Owner |
|----------|---------|------------------|-------|
| **Workbook 1** | User Inventory & Lifecycle Compliance (A.5.16) | Monthly | IAM Team |
| **Workbook 2** | Access Rights Matrix (A.5.18) | Monthly | IAM Team |
| **Workbook 3** | Access Review Results (A.5.15 + A.5.18) | Quarterly | Security Team |
| **Workbook 4** | Role Compliance & SoD (A.5.15 + A.5.18) | Quarterly | IAM Team |
| **Workbook 5** | Lifecycle Compliance Detailed (A.5.16) | Quarterly | IAM Team |
| **Dashboard** | IAM Governance Overview (All controls) | Monthly | Security Team |

**Workbook Content Summary**:

**Workbook 1 - User Inventory & Lifecycle Compliance**:
- Complete user inventory (all users, all identity systems)
- User attributes (name, email, department, manager, hire date, account status)
- Provisioning timeliness metrics (days from hire date to account creation)
- Deprovisioning timeliness metrics (days from termination to account disable)
- Orphaned account count and remediation status
- Inactive account count (no login in 90+ days)
- Compliance status per user (lifecycle compliant/non-compliant)

**Workbook 2 - Access Rights Matrix**:
- User-to-system access mapping (User → System → Access Level)
- Group memberships per user
- Role assignments per user
- Access grant documentation (business justification, approval date, approver)
- Access expiration dates (for time-bound access)
- Privileged access flag (identify admin, root, elevated access)
- Data sensitivity classification (confidential, restricted access highlighted)

**Workbook 3 - Access Review Results**:
- Access review tracking (review period, system reviewed, reviewer, completion status)
- Review findings (access confirmed, access removed, access justified)
- Overdue reviews (reviews not completed by deadline)
- Remediation tracking (access removal requests and completion)
- Reviewer accountability (completion rates by manager/system owner)
- Review compliance by system (% completion)

**Workbook 4 - Role Compliance & SoD**:
- Role catalog (role definitions, owners, users assigned)
- RBAC adoption metrics (% users in roles vs. direct access)
- Role-to-user alignment (verify users have appropriate roles)
- Segregation of duties violations (users with conflicting roles)
- SoD exception tracking (approved exceptions with compensating controls)
- Role accuracy (role definitions match actual access granted)

**Workbook 5 - Lifecycle Compliance Detailed**:
- Joiner compliance (provision by start date, account creation timeline)
- Mover compliance (access updates within SLA, role change tracking)
- Leaver compliance (deprovision timeliness, verification of complete removal)
- Contractor lifecycle (time-bound access, sponsor verification, contract end compliance)
- Service account management (owner documentation, password rotation compliance)

**Dashboard - IAM Governance Overview**:
- Overall IAM maturity score (0-100, combining all metrics)
- Compliance per control (A.5.15, A.5.16, A.5.18 individual scores)
- User inventory metrics (total users, orphaned accounts, inactive accounts)
- Access review metrics (completion rate, overdue reviews, access removal rate)
- Lifecycle metrics (provisioning timeliness, deprovisioning timeliness)
- Role compliance metrics (RBAC adoption %, SoD violations)
- Trend analysis (if historical data available)
- Gap identification (high/medium/low priority gaps)
- Evidence summary (assessment evidence collected and verified)

**Evidence Requirements**:
- Assessment workbooks retained for audit cycle + 1 year minimum
- Evidence linked to specific control requirements (A.5.15, A.5.16, A.5.18)
- Evidence accessible to internal and external auditors
- Evidence verification (spot checks to validate accuracy)

**Assessment Procedures**: Detailed assessment procedures, including data collection methods, compliance calculation methodologies, and evidence requirements, are documented in ISMS-IMP-A.5.15-16-18.5 (IAM Assessment Procedures).

### 3.3 Exception Management

[Organization] manages IAM exceptions through formal approval and periodic review:

**Exception Request Process**:

1. **Exception Identification**: Situation where standard IAM policy cannot be followed
2. **Business Justification**: Requester documents why exception necessary, business impact if denied
3. **Risk Assessment**: Security Team assesses risk of exception, proposes compensating controls
4. **Approval**: CISO approves exception with documented compensating controls
5. **Documentation**: Exception recorded in exception register (exception ID, justification, risk, compensating controls, approval date, expiry date)
6. **Implementation**: Compensating controls implemented and verified
7. **Review**: Exceptions reviewed annually, renewed or remediated

**Approval Authority**:
- **CISO**: Required for all IAM policy exceptions
- **Executive Management**: Required for exceptions involving significant risk (e.g., SoD violations enabling fraud)

**Common Exception Scenarios**:
- **Shared accounts**: When technical constraints prevent individual accounts (legacy system, embedded device)
- **Extended provisioning timelines**: Complex system integration, vendor delays
- **Delayed access reviews**: Business constraints, resource limitations, organizational change
- **SoD violations**: Small organization, specialized skills, cannot separate duties
- **Orphaned account retention**: Legal hold, litigation preservation, business continuity

**Compensating Controls Examples**:

| Exception Type | Compensating Control | Verification |
|----------------|---------------------|--------------|
| **Shared account** | Enhanced logging, manager approval for each use, quarterly access review | Audit logs reviewed monthly |
| **Extended provisioning** | Manual interim access, expedited processing for critical users | Backlog tracked weekly |
| **Delayed review** | Increased review depth when completed, interim spot checks | Spot checks documented |
| **SoD violation** | Manager review of all conflicting transactions, quarterly audits | Manager sign-off on reviews |
| **Orphaned account** | Account monitoring, restricted access, periodic verification of continued need | Monthly verification |

**Exception Tracking**:
- All exceptions documented in exception register
- Exception register reviewed quarterly by CISO
- Exceptions reported in IAM compliance dashboard
- Expired exceptions automatically flagged for renewal or remediation

**Exception Renewal**:
- Exceptions typically approved for 12 months maximum
- Renewal requires re-justification and risk re-assessment
- CISO may revoke exceptions if risk changes or compensating controls fail

**Implementation Note**: Exception request templates and approval workflows are documented in ISMS-IMP-A.5.15-16-18.1 (Access Control Governance).

### 3.4 Incident Response

[Organization] handles IAM-related incidents through systematic response procedures:

**IAM-Related Incident Types**:
- Account compromise (credential theft, unauthorized access)
- Orphaned account exploitation (attacker uses former employee account)
- Privilege escalation (user gains unauthorized elevated access)
- Access policy violation (user accesses data without authorization)
- Failure to deprovision (terminated employee retains access beyond policy)
- SoD violation enabling fraud (conflicting roles used to commit fraud)
- Identity system compromise (AD, Azure AD, Okta breach)

**Incident Classification** (per ISMS-POL-A.5.24-27 Incident Management):

| Severity | Description | Example | Response Time |
|----------|-------------|---------|---------------|
| **Critical** | Privileged account compromise, active exploitation | Admin account compromised, attacker active | Immediate (within 1 hour) |
| **High** | Standard account compromise, SoD violation enabling fraud | User account compromised, data exfiltration | Within 4 hours |
| **Medium** | Policy violation without data breach, delayed deprovisioning | Unauthorized access attempt, access not removed within SLA | Within 1 business day |
| **Low** | Failed access attempt, procedural non-compliance | Failed login, access review delayed | Within 3 business days |

**Response Procedures** (IAM-specific actions):

**Account Compromise Response**:
1. **Immediate Actions**: Disable compromised account, revoke all active sessions, reset credentials
2. **Investigation**: Review access logs (what did attacker access?), Determine compromise vector
3. **Notification**: Notify affected system owners, security team, CISO, potentially users/customers
4. **Forensic Analysis**: Preserve logs, analyze attacker actions, identify data accessed
5. **Remediation**: Implement additional controls (MFA, access restrictions), address root cause
6. **Recovery**: Re-enable account with enhanced security, monitor for re-compromise

**Orphaned Account Exploitation Response**:
1. **Immediate Actions**: Disable orphaned account, all other orphaned accounts (comprehensive scan)
2. **Investigation**: Determine how account was exploited, review all orphaned account activity
3. **Accelerated Cleanup**: Remediate all orphaned accounts within 7 days (not 30 days)
4. **Process Review**: Identify why account was not removed, improve deprovisioning process
5. **Prevention**: Implement automated orphaned account detection and remediation

**Emergency Deprovisioning**:
- **Trigger**: Security incident, suspected compromise, immediate termination for cause
- **Timeline**: Access disabled within 1 hour
- **Procedure**: HR/Security notifies IAM Team → IAM Team disables all accounts → IT Operations verifies removal → Security Team confirms
- **Verification**: Complete access removal verified across all systems
- **Documentation**: Incident ticket with timestamp, approver, reason, verification evidence

**Incident Response Integration**: IAM incidents are managed per ISMS-POL-A.5.24-27 (Incident Management). IAM Team participates in incident response as subject matter experts for identity and access-related incidents.

**Implementation Note**: Detailed IAM incident response playbooks, including account compromise procedures and emergency deprovisioning workflows, are documented in ISMS-IMP-A.5.15-16-18.1.

### 3.5 Policy Governance

[Organization] maintains this IAM policy through systematic governance:

**Review Frequency**:
- **Annual review minimum** (mandatory, scheduled at policy anniversary)
- **Triggered reviews** (as needed when conditions change)

**Triggers for Policy Review**:
- **Regulatory changes**: New compliance requirements (GDPR updates, new industry regulations)
- **Organizational changes**: Merger, acquisition, significant restructuring
- **Technology changes**: New identity systems, significant architecture changes (cloud migration)
- **Audit findings**: Deficiencies requiring policy update, certification audit recommendations
- **Risk assessment changes**: New threats (credential stuffing, identity attacks), changed risk tolerance
- **Incident lessons learned**: Serious IAM-related incidents revealing policy gaps

**Policy Review Process**:
1. **Security Team** proposes policy updates based on review triggers
2. **Stakeholder Review**: HR, IT, Legal, Business representatives review and provide feedback
3. **CISO Approval**: CISO approves policy changes
4. **Executive Management Approval** (if significant changes affecting business operations)
5. **Communication**: Policy updates announced organization-wide, training provided if needed
6. **Version Control**: Version history maintained, previous versions archived

**Policy Approval Authority**:
- **CISO**: Required for all policy changes
- **Executive Management**: Required for major policy revisions affecting business operations

**Policy Communication**:
- Policy published in centralized policy repository (intranet)
- All employees notified of policy updates (email, intranet announcement)
- Training provided for significant changes (new processes, new technologies)
- Policy accessible to all stakeholders (employees, contractors, vendors)

**Version Control**:
- Version history maintained in Document Control section
- Change log documents who changed what, when, and why
- Previous versions archived for reference and audit
- Current version clearly marked as active

**Training on Policy Updates**:
- Security awareness training updated to reflect policy changes
- Technical training for IAM Team and IT Operations on new procedures
- Manager training on new approval or review responsibilities
- Communication includes effective date and transition period if applicable

**Implementation Note**: Policy governance procedures and stakeholder communication templates are documented in ISMS-IMP-A.5.15-16-18.1.

---

## 4. Implementation & References

### 4.1 Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):
- IAM controls selected based on [Organization]'s risk assessment
- Identity lifecycle risks (A.5.16), access control risks (A.5.15), and access rights risks (A.5.18) identified and assessed
- Risk treatment decisions document which controls are implemented and at what level
- Residual risks from incomplete IAM controls tracked in risk register

**Statement of Applicability** (ISO 27001 Clause 6.1.3):
- Controls A.5.15, A.5.16, A.5.18 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported
- Control effectiveness measured through compliance assessments

**This policy supports the following SoA entries**:

| Control | Status | Justification | Implementation |
|---------|--------|---------------|----------------|
| **A.5.15 - Access Control** | ☑ Applicable | [Organization] requires strategic access control policy to prevent unauthorized access | Section 2.1, ISMS-IMP-A.5.15-16-18.1 |
| **A.5.16 - Identity Management** | ☑ Applicable | [Organization] requires systematic identity lifecycle management to prevent orphaned accounts | Section 2.2, ISMS-IMP-A.5.15-16-18.2 |
| **A.5.18 - Access Rights** | ☑ Applicable | [Organization] requires access rights assignment and review to prevent privilege creep | Section 2.3, ISMS-IMP-A.5.15-16-18.3/4 |

**Related Controls** (Integration Points):

- **A.8.2** (Privileged Access Rights): IAM defines privileged users, A.8.2 implements PAM controls
- **A.8.3** (Information Access Restriction): IAM assigns access rights, A.8.3 enforces restrictions technically
- **A.8.5** (Secure Authentication): IAM creates identities, A.8.5 authenticates them
- **A.5.9** (Inventory of Information and Assets): Users access assets, asset owners are users
- **A.5.10** (Acceptable Use): Users acknowledge AUP during onboarding (part of joiner process)
- **A.8.16** (Monitoring Activities): User activity monitored, suspicious access detected
- **A.5.7** (Threat Intelligence): Compromised credentials trigger emergency deprovisioning
- **A.5.24-27** (Incident Management): Account compromise incidents managed per incident framework

### 4.2 Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.5.15-16-18 Suite):

| Document | Purpose | Target Audience | Review Frequency |
|----------|---------|----------------|------------------|
| **ISMS-IMP-A.5.15-16-18.1** | Access Control Governance | Security Team, CISO, Policy Owners | Annual |
| **ISMS-IMP-A.5.15-16-18.2** | Identity Lifecycle Process | IAM Team, HR Team, IT Operations | Quarterly |
| **ISMS-IMP-A.5.15-16-18.3** | Role Definition and Assignment | IAM Team, Managers, System Owners | Quarterly |
| **ISMS-IMP-A.5.15-16-18.4** | Access Review Process | Managers, System Owners, Security Team | Quarterly |
| **ISMS-IMP-A.5.15-16-18.5** | IAM Assessment Procedures | Security Team, IAM Team, Internal Audit | Quarterly |

**Assessment Tools**:
- Excel-based assessment workbooks generated via Python automation (5 workbooks + 1 dashboard)
- Evidence registers and gap analysis templates embedded in workbooks
- Automated compliance calculations and reporting
- Remediation tracking and trend analysis

**Supporting Materials**:
- Access request form templates
- Access review templates (quarterly, annual)
- SoD matrix template
- Role definition template
- Exception request template
- Identity provider selection criteria (ISMS-REF-A.5.23 Cloud Service Provider Registry)

**Reference Documents**:
- **ISMS-REF-A.5.23**: Cloud Service Provider Registry (identity provider assessment)

### 4.3 Regulatory Mapping

This policy addresses IAM requirements from multiple regulatory frameworks:

| Requirement Category | Swiss nDSG | EU GDPR | ISO 27001 | FINMA* | DORA/NIS2* | PCI DSS* |
|---------------------|-----------|---------|-----------|--------|------------|----------|
| **Access Control Policy** | Art. 8 | Art. 32 | A.5.15 | Margin 56 | Art. 21(2)(d) | Req. 7 |
| **Identity Lifecycle** | Art. 8 | Art. 32 | A.5.16 | Margin 56 | Art. 21(2)(f) | Req. 8.2 |
| **Access Reviews** | Art. 8 | Art. 32 | A.5.18 | Margin 56 | Art. 21(2)(f) | Req. 7 |
| **Segregation of Duties** | Art. 8 | Art. 32 | A.5.15 | Margin 58 | Risk-Based | Req. 7 |
| **Privileged Access** | Art. 8 | Art. 32 | A.5.18 | Margin 56 | Risk-Based | Req. 7, 8 |

*Conditional applicability per ISMS-POL-00

**Note**: Specific regulatory interpretation and compliance verification procedures are documented in ISMS-IMP-A.5.15-16-18.5 (IAM Assessment Procedures).

### 4.4 Training & Awareness

**Security Awareness** (All Personnel):
- Annual training module on access control policies and responsibilities
- User responsibilities: Access requests, appropriate use, reporting suspicious activity
- Access control awareness: Least privilege, business justification, access reviews

**Technical Training** (IAM Team, IT Operations):
- Identity system administration (AD, Azure AD, Okta)
- Provisioning/deprovisioning procedures
- Access review tools and processes
- Orphaned account detection and remediation
- Assessment workbook generation and compliance measurement

**Manager Training** (Access Approvers, Reviewers):
- Access approval responsibilities and accountability
- Access review procedures and expectations
- Recognizing inappropriate access patterns
- SoD awareness and conflict identification

**Specialized Training**:
- **HR Team**: IAM integration (joiner/mover/leaver triggers, termination coordination)
- **System Owners**: Access classification, requirement definition, review participation
- **Security Team**: IAM assessment, evidence collection, incident response

---

## 5. Definitions

**Identity**: Digital representation of user (person, service, device) with unique identifier and attributes. Identities enable authentication and access control.

**Access Control**: Security technique regulating who or what can view or use resources. Combines authentication (proving identity), authorization (granting permissions), and accountability (logging activity).

**Role-Based Access Control (RBAC)**: Access control model where permissions assigned to roles rather than individual users. Users assigned to roles based on job function, inheriting role permissions.

**Least Privilege**: Security principle requiring users be granted minimum access necessary to perform job functions. Prevents excessive rights accumulation and limits damage from compromised accounts.

**Need-to-Know**: Access restriction principle limiting information access to those with legitimate business requirement. Prevents unnecessary data exposure.

**Segregation of Duties (SoD)**: Practice of dividing critical tasks among multiple people to prevent fraud and error. No single person should control entire high-risk process.

**Joiner Process**: Systematic onboarding of new users including account creation, initial access provisioning, and credential delivery. Triggered by HR notification of new hire or contractor.

**Mover Process**: Systematic handling of user role changes including access review, access adjustment to new role, and removal of access from previous role. Triggered by HR notification of transfer or promotion.

**Leaver Process**: Systematic offboarding of departing users including account disablement, access removal, and data handover. Triggered by HR notification of termination or contract end.

**Orphaned Account**: User account without valid business owner, typically belonging to former employee whose access was not removed during leaver process. Security risk requiring systematic detection and remediation.

**Provisioning**: Process of creating user accounts and granting access to systems, applications, and data based on business justification and approval.

**Deprovisioning**: Process of removing user access and disabling/deleting accounts when no longer required (termination, role change, contract end).

**Access Review** (Recertification): Periodic verification that users' access remains appropriate for current job function. Reviewers (managers, system owners) certify access or request removal.

**Privilege Creep**: Gradual accumulation of excess access rights as users change roles over time but retain access from previous positions. Detected through comparison of current vs. required access.

**Service Account**: Non-human account used by applications, scripts, or services for automated processes. Requires documented owner, password rotation, and privileged access controls.

**Shared Account**: Account used by multiple individuals (discouraged). Requires CISO approval with business justification and compensating controls (enhanced logging, manager approval).

**Break-Glass Account** (Emergency Account): Dormant privileged account for disaster scenarios when normal access unavailable. Credentials stored in secure vault, usage triggers immediate alert and investigation.

**Access Matrix**: Mapping of users to systems/applications to access levels. Documents who has access to what, providing baseline for access reviews and compliance reporting.

**Business Justification**: Documented explanation of why access is required, what business function needs it, and why user cannot perform job without it. Required for all access requests.

**Compensating Control**: Alternative security measure implemented when primary control cannot be applied. Used for IAM exceptions to mitigate risk when policy cannot be followed.

---

## Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Chief Human Resources Officer (CHRO)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements. Implementation procedures are documented in ISMS-IMP-A.5.15-16-18.*