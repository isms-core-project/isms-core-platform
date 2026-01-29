# ISMS-POL-A.5.15-16-18-S1: Executive Summary & Control Alignment
## Identity & Access Management Foundation Framework

**Document ID**: ISMS-POL-A.5.15-16-18-S1  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Active

---

## Document Purpose

This section provides the executive summary and control alignment for [Organization]'s **Identity & Access Management (IAM) Foundation Framework**, implementing ISO/IEC 27001:2022 controls A.5.15, A.5.16, and A.5.18 as a unified governance framework.

---

## 1. Executive Summary

### 1.1 Business Context

Identity and access management forms the **cornerstone of information security governance**. Every security incident, data breach, and compliance violation ultimately traces back to a question: "Did the right person have the right access at the right time, for the right reason?"

**The IAM challenge organizations face**:
- **Orphaned accounts**: Former employees retain access months after termination
- **Privilege creep**: Users accumulate excessive rights over years, never removed
- **Access sprawl**: No one knows who has access to what, or why
- **Compliance gaps**: Access reviews overdue, no evidence of lifecycle management
- **Manual processes**: Provisioning takes weeks, deprovisioning forgotten entirely

**The cost of poor IAM governance**:
- **Security risk**: Unauthorized access, insider threats, credential compromise
- **Regulatory penalties**: GDPR violations for inadequate access controls
- **Operational inefficiency**: New employees wait days for system access
- **Audit findings**: Missing documentation, incomplete reviews, orphaned accounts
- **Reputational damage**: Data breaches attributed to excessive access

**This framework addresses**:
✅ Systematic identity lifecycle management (joiner/mover/leaver automation)  
✅ Strategic access control policy (who gets access, why, with what restrictions)  
✅ Effective access rights assignment and review (RBAC, periodic recertification)  
✅ Unified evidence collection (6 assessment workbooks + executive dashboard)  
✅ Regulatory compliance (FADP, GDPR, FINMA, DORA, NIS2)

---

### 1.2 Why Combined Implementation?

ISO/IEC 27001:2022 defines three separate but deeply interrelated controls:
- **A.5.15 - Access Control**: Strategic policy framework
- **A.5.16 - Identity Management**: Identity lifecycle management
- **A.5.18 - Access Rights**: Rights assignment and review

**Attempting separate implementation results in**:
- ❌ **Disconnected processes**: Access policy divorced from identity lifecycle
- ❌ **Redundant activities**: Three separate user inventories, three access reviews
- ❌ **Fragmented evidence**: Access data scattered across unrelated assessments
- ❌ **Organizational confusion**: "Is this A.5.15 or A.5.18? Who owns this?"
- ❌ **Audit inefficiency**: Auditors request same evidence three times

**Combined implementation provides**:
- ✅ **Unified governance**: Policy → Lifecycle → Rights as integrated framework
- ✅ **Single user inventory**: Serves all three controls simultaneously
- ✅ **Integrated assessment**: Six workbooks cover all control requirements
- ✅ **Consolidated evidence**: Dashboard summarizes compliance across all controls
- ✅ **~3x efficiency**: One implementation effort vs. three separate initiatives

**The relationship**:
```
A.5.15 (Access Control Policy)
    ↓ defines strategic requirements for
A.5.16 (Identity Management)
    ↓ creates identities with lifecycle management
A.5.18 (Access Rights)
    ↓ assigns and reviews access rights
```

**Integration with authentication/PAM stack**:
This IAM foundation (A.5.15/16/18) provides the **governance layer** that feeds into **ISMS-A.8.2-3-5-Authentication-Privileged-Access** (technical security layer):
- A.5.15/16/18 = WHO gets access, WHY, and lifecycle management
- A.8.2-3-5 = HOW access is authenticated, restricted, and privileged

---

### 1.3 Risk Mitigation

**Without effective IAM governance, organizations face**:

**Security Risks**:
- **Orphaned accounts**: 15-30% of accounts in typical organizations belong to former employees
- **Excessive privileges**: Average user has access to 10x more systems than job requires
- **Credential compromise**: Attackers target orphaned and over-privileged accounts
- **Insider threats**: Current employees with unnecessary access to sensitive data
- **Service account sprawl**: Non-human accounts with unknown owners and purposes

**Compliance Risks**:
- **GDPR Article 32**: Personal data access not restricted to authorized persons
- **FADP Article 8**: Inadequate technical/organizational access control measures
- **FINMA Circular 2023/1**: User administration deficiencies (banks)
- **Audit findings**: Missing access reviews, undocumented lifecycle processes
- **Regulatory penalties**: Fines for inadequate access governance

**Operational Risks**:
- **Business disruption**: New employees wait weeks for access, can't perform job
- **Productivity loss**: Manual provisioning consumes IT resources
- **Shadow IT**: Users create unauthorized accounts when official process too slow
- **Data loss**: Terminated employees retain access to email, files, applications
- **Fraud opportunity**: Segregation of duties violations enable unauthorized transactions

**This framework mitigates risks through**:
- Automated lifecycle management (timely provisioning/deprovisioning)
- Least privilege enforcement (access based on business need)
- Periodic access reviews (remove inappropriate access)
- Orphaned account detection (systematic cleanup)
- Segregation of duties monitoring (prevent fraud/error)
- Comprehensive audit trail (evidence for compliance)

---

## 2. ISO 27001:2022 Control Alignment

### 2.1 Control A.5.15 - Access Control (Zugangssteuerung)

**Official Control Text (German)**:
> Regeln zur Steuerung des physischen und logischen Zugriffs auf Informationen und andere damit verbundene Werte müssen auf der Grundlage von Geschäfts- und Informationssicherheitsanforderungen aufgestellt und umgesetzt werden.

**English Translation**:
> Rules to control physical and logical access to information and other associated assets shall be established and implemented based on business and information security requirements.

**Control Objective**:
Ensure access to information and systems is controlled based on business justification and security requirements, preventing unauthorized access while enabling legitimate business activities.

**Key Requirements**:
- Access control policy defining access principles (least privilege, need-to-know)
- Business justification framework for access requests
- Access classification (user types, system criticality, data sensitivity)
- Segregation of duties (SoD) requirements and monitoring
- Access control roles and responsibilities (approvers, provisioners, reviewers)
- Exception management (documented approvals, periodic review)
- Integration with HR processes (onboarding, offboarding, role changes)

**What A.5.15 Controls**:
- **Strategic framework**: WHO gets access to WHAT, and WHY
- **Policy requirements**: Access principles, classification, justification
- **Governance**: Roles, responsibilities, exception handling
- **SoD enforcement**: Conflicting role detection and remediation

**Implementation in this Framework**:
- Section 2 (POL-S2) defines access control policy requirements
- Section 1 (IMP-S1) implements access control governance
- Assessment workbooks verify policy compliance and SoD adherence

---

### 2.2 Control A.5.16 - Identity Management (Identitätsmanagement)

**Official Control Text (German)**:
> Der gesamte Lebenszyklus von Identitäten sollte verwaltet werden.

**English Translation**:
> The full life cycle of identities should be managed.

**Control Objective**:
Ensure user identities are systematically created, maintained, and removed throughout their entire lifecycle, preventing orphaned accounts and ensuring timely provisioning/deprovisioning.

**Key Requirements**:
- Identity lifecycle framework (joiner, mover, leaver processes)
- User account provisioning procedures (timely access for new users)
- User account deprovisioning procedures (immediate removal for terminations)
- Account type management (employees, contractors, vendors, service accounts)
- Identity repository management (authoritative source, synchronization)
- Orphaned account detection and remediation
- Contractor/vendor identity management (time-bound, sponsored)

**What A.5.16 Controls**:
- **Lifecycle processes**: Joiner/mover/leaver automation
- **Timeliness**: Provisioning by start date, deprovisioning by termination date
- **Account hygiene**: Orphaned account cleanup, inactive account management
- **Special accounts**: Contractors (time-bound), service accounts (owned)

**Implementation in this Framework**:
- Section 3 (POL-S3) defines identity lifecycle requirements
- Section 2 (IMP-S2) implements lifecycle processes
- Assessment workbooks track provisioning/deprovisioning timeliness

---

### 2.3 Control A.5.18 - Access Rights (Zugangsrechte)

**Official Control Text (German)**:
> Zugangsrechte zu Informationen und anderen damit verbundenen Werten müssen in Übereinstimmung mit der themenspezifischen Richtlinie und den Regeln der Organisation für die Zugangssteuerung bereitgestellt, überprüft, geändert und entfernt werden.

**English Translation**:
> Access rights to information and other associated assets shall be provisioned, reviewed, modified and removed in accordance with the organization's topic-specific policy and rules for access control.

**Control Objective**:
Ensure access rights are appropriately assigned based on roles/business need, periodically reviewed for accuracy, and promptly removed when no longer required.

**Key Requirements**:
- Access rights assignment procedures (request, approval, provisioning)
- Role-based access control (RBAC) framework
- Group membership management
- Access review/recertification process (frequency, scope, accountability)
- Access removal procedures (timely removal when no longer needed)
- Privilege creep detection (accumulated excess rights over time)
- Emergency access procedures (break-glass accounts)
- Access rights documentation (who has what, why, approval evidence)

**What A.5.18 Controls**:
- **Rights assignment**: RBAC, group management, approval workflows
- **Access reviews**: Periodic recertification, manager accountability
- **Rights removal**: Timely removal when role changes or employment ends
- **Privilege management**: Detection and remediation of excess rights

**Implementation in this Framework**:
- Section 4 (POL-S4) defines access rights management requirements
- Sections 3-4 (IMP-S3/S4) implement RBAC and access review processes
- Assessment workbooks track access review completion and RBAC adoption

---

### 2.4 Control Interdependencies

**How the three controls work together**:

```
┌────────────────────────────────────────────────────────────────┐
│                    INTEGRATED IAM FRAMEWORK                     │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  A.5.15: Access Control Policy (Strategic Layer)               │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ • Define WHO can access WHAT (classification)            │  │
│  │ • Define WHY access is granted (business justification)  │  │
│  │ • Define HOW access is controlled (SoD, approvals)       │  │
│  └──────────────────────────────────────────────────────────┘  │
│                           ↓ Policy guides                       │
│                                                                 │
│  A.5.16: Identity Management (Lifecycle Layer)                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ • CREATE identities when users join                      │  │
│  │ • MODIFY identities when users move                      │  │
│  │ • REMOVE identities when users leave                     │  │
│  │ • DETECT orphaned accounts and remediate                 │  │
│  └──────────────────────────────────────────────────────────┘  │
│                           ↓ Identities enable                   │
│                                                                 │
│  A.5.18: Access Rights (Rights Management Layer)               │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ • ASSIGN rights based on roles (RBAC)                    │  │
│  │ • REVIEW rights periodically (recertification)           │  │
│  │ • MODIFY rights when roles change                        │  │
│  │ • REMOVE rights when no longer needed                    │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
                              ↓
        ┌─────────────────────────────────────────┐
        │  Shared Foundation:                     │
        │  • User Inventory (all account types)   │
        │  • Identity Repository (AD, Azure, etc) │
        │  • Access Rights Matrix (user→system)   │
        │  • Review Process (periodic validation) │
        └─────────────────────────────────────────┘
```

**Example integration scenario**:
1. **New employee hired** (A.5.16 Joiner):
   - HR system creates employee record
   - Identity provisioning triggered
   - Account created in AD/Azure AD
   - Initial access assigned based on role (per A.5.15 policy)
   
2. **Access rights assigned** (A.5.18):
   - Manager approves access request
   - RBAC role assigned (based on job function)
   - Access provisioned to systems
   - Documentation created (who, what, why, when)
   
3. **Quarterly access review** (A.5.18 + A.5.15):
   - Manager reviews all direct reports' access
   - Confirms access still appropriate OR removes
   - SoD violations detected and remediated
   
4. **Employee leaves** (A.5.16 Leaver):
   - HR system updates termination date
   - Account disabled immediately
   - All access rights removed (per A.5.18)
   - Verification logged for compliance

**Why this integration matters**:
- **Policy without lifecycle = orphaned accounts** (A.5.15 without A.5.16)
- **Lifecycle without rights management = privilege creep** (A.5.16 without A.5.18)
- **Rights without policy = uncontrolled access** (A.5.18 without A.5.15)
- **All three together = comprehensive IAM governance**

---

### 2.5 Integration with A.8.2-3-5 (Authentication & Privileged Access)

This IAM foundation framework (A.5.15/16/18) provides the **governance layer** that feeds into the **technical security layer** (A.8.2-3-5):

**Governance Layer (A.5.15/16/18)**:
- Defines WHO gets access (user identity management)
- Defines WHAT access they get (access rights assignment)
- Defines WHY they have access (business justification, policy)
- Defines LIFECYCLE (joiner/mover/leaver processes)

**Technical Security Layer (A.8.2-3-5)**:
- Defines HOW users authenticate (passwords, MFA, biometrics)
- Defines HOW privileged access is controlled (PAM, JIT, elevation)
- Defines HOW access is restricted (authentication strength, session limits)

**Data flow**:
```
A.5.16 creates user identity
    ↓
A.5.18 assigns access rights
    ↓
A.8.5 authenticates user (password + MFA)
    ↓
A.8.3 restricts access based on role
    ↓
A.8.2 controls privileged access (if admin)
```

**Example**:
- A.5.16: User "alice@example.com" created in Azure AD (joiner process)
- A.5.18: Alice assigned "Financial Analyst" role (RBAC)
- A.5.15: Policy requires approval for finance system access
- A.8.5: Alice authenticates with password + MFA
- A.8.3: Alice restricted to read-only finance data (role-based restriction)
- A.8.2: Alice's admin request requires additional approval (PAM)

**Both frameworks required**:
- Without A.5.15/16/18: No governance, identity chaos, orphaned accounts
- Without A.8.2-3-5: Weak authentication, uncontrolled privileged access
- Together: Strong IAM foundation + robust technical security

---

## 3. Scope & Applicability

### 3.1 Framework Scope

**This IAM framework applies to**:

**User Types**:
- ✅ Employees (internal staff, full-time, part-time)
- ✅ Contractors (temporary workers, time-bound access)
- ✅ Vendors (third-party service providers with system access)
- ✅ Partners (business partners requiring access to shared systems)
- ✅ Customers (external users for customer-facing applications)
- ✅ Service accounts (non-human accounts for applications/systems)
- ✅ Emergency accounts (break-glass accounts for disaster recovery)
- ✅ Shared accounts (discouraged but documented if required)

**Identity Systems**:
- ✅ Active Directory (on-premises)
- ✅ Azure Active Directory / Microsoft Entra ID (cloud)
- ✅ Okta (cloud identity platform)
- ✅ Google Workspace (cloud identity)
- ✅ LDAP directories (OpenLDAP, FreeIPA)
- ✅ Custom identity systems (proprietary)
- ✅ Hybrid environments (AD + Azure AD sync)
- ✅ Federated identity (SAML, OAuth, OpenID Connect)

**Access Types**:
- ✅ Application access (SaaS, on-prem applications)
- ✅ System access (servers, workstations, network devices)
- ✅ Data access (databases, file shares, cloud storage)
- ✅ Network access (VPN, Wi-Fi, remote access)
- ✅ Administrative access (privileged accounts)
- ✅ Physical access (building badges, server rooms) - governance only

**Environments**:
- ✅ On-premises infrastructure
- ✅ Cloud services (SaaS, IaaS, PaaS)
- ✅ Hybrid environments (on-prem + cloud)
- ✅ Multi-cloud (AWS, Azure, GCP)

**Organizational Applicability**:
- ✅ Small organizations (10-100 users)
- ✅ Medium organizations (100-1,000 users)
- ✅ Large organizations (1,000-10,000+ users)
- ✅ Any industry (finance, healthcare, technology, manufacturing)
- ✅ Any geography (Switzerland, EU, global)

---

### 3.2 Out of Scope

**This framework does NOT cover** (addressed in other ISMS controls):

- ❌ **Physical access control systems** (card readers, biometric scanners)
  - Covered in: A.7.2 Physical Entry Controls
  - Note: IAM framework governs WHO gets physical access badges, not HOW locks work

- ❌ **Detailed authentication mechanisms** (password policies, MFA configuration)
  - Covered in: A.8.5 Secure Authentication
  - Note: IAM framework creates identities, A.8.5 defines how they authenticate

- ❌ **Privileged access management (PAM) implementation** (JIT, session recording)
  - Covered in: A.8.2 Privileged Access Rights
  - Note: IAM framework identifies privileged users, A.8.2 controls their access

- ❌ **User awareness training** (security awareness, acceptable use)
  - Covered in: A.6.3 Information Security Awareness
  - Note: IAM framework provisions accounts, A.6.3 trains users

- ❌ **Monitoring and logging** (user activity monitoring, SIEM)
  - Covered in: A.8.16 Monitoring Activities
  - Note: IAM framework assigns access, A.8.16 monitors usage

- ❌ **Incident response** (account compromise handling)
  - Covered in: A.5.24-27 Incident Management
  - Note: IAM framework provides evidence for investigations

**Interfaces with other controls**:
While not implementing these areas, the IAM framework provides the **foundation** that other controls build upon:
- A.5.9 (Asset Inventory) - users are assigned to assets
- A.5.10 (Acceptable Use) - users acknowledge AUP
- A.5.7 (Threat Intelligence) - compromised credentials detected
- A.8.16 (Monitoring) - user activity logged
- A.5.24-27 (Incident Management) - account compromise response

---

### 3.3 Technology Neutrality

**Critical principle**: This framework is **completely generic and technology-agnostic**.

**What this means**:
- Framework describes **principles and objectives** (what must be achieved)
- Implementation guidance provides **examples across technologies** (how to achieve it)
- Assessment tools are **adaptable to different environments** (measure any implementation)

**Example: Identity Lifecycle (A.5.16)**:

**Generic requirement**:
> User accounts must be provisioned within 1 business day of hire date.

**Technology-specific implementation examples**:
- **Active Directory**: PowerShell script triggered by HR system update
- **Azure AD**: Azure AD provisioning service with HR connector
- **Okta**: Okta Workflows automation from HR feed
- **Google Workspace**: Google Cloud Directory Sync from HR system
- **Custom LDAP**: Shell script parsing HR CSV export

**All implementations achieve same objective**: Timely provisioning.

**Assessment approach**:
- Measure: % users provisioned on-time (regardless of technology)
- Evidence: Provisioning date vs. hire date (from any identity system)
- Compliance: ≥95% on-time provisioning (technology-neutral metric)

**Why technology neutrality matters**:
- Organizations use different identity platforms (AD, Azure AD, Okta, custom)
- Identity landscapes evolve (migrate from AD to Azure AD)
- Framework remains valid regardless of technology choices
- Auditors assess governance effectiveness, not specific tools

**Framework usage**:
1. Read framework requirements (what to achieve)
2. Consult implementation examples (how others achieve it)
3. Adapt to your specific technology environment
4. Use assessment tools to measure compliance
5. Provide evidence regardless of technology

---

## 4. Framework Users

### 4.1 Primary Stakeholders

**IAM Team** (Framework Implementers):
- **Role**: Implement identity lifecycle processes, maintain identity systems
- **Uses Framework For**: Technical implementation guidance, process design
- **Key Sections**: IMP-S2 (Identity Lifecycle), IMP-S3 (Role Definition)

**Security Team** (Governance):
- **Role**: Define access control policies, monitor compliance, conduct assessments
- **Uses Framework For**: Policy development, compliance monitoring, audit preparation
- **Key Sections**: POL-S2 (Access Control Policy), POL-S5 (Assessment), all assessment workbooks

**HR Team** (Authoritative Source):
- **Role**: Trigger joiner/mover/leaver events, provide employee data
- **Uses Framework For**: Understanding IAM integration points, process handoffs
- **Key Sections**: IMP-S2 (Identity Lifecycle), integration with HR systems

**IT Operations** (Provisioning):
- **Role**: Provision/deprovision accounts, grant/remove access
- **Uses Framework For**: Operational procedures, SLA requirements
- **Key Sections**: IMP-S2 (Lifecycle Process), IMP-S3 (Role Assignment)

**Managers** (Access Approvers & Reviewers):
- **Role**: Approve access requests, review direct reports' access quarterly/annually
- **Uses Framework For**: Approval responsibilities, review procedures
- **Key Sections**: IMP-S1 (Access Control Governance), IMP-S4 (Access Review Process)

**System Owners** (Application/Data Custodians):
- **Role**: Define access requirements for their systems, approve sensitive access
- **Uses Framework For**: Access control responsibilities, review participation
- **Key Sections**: POL-S2 (Access Control Policy), IMP-S4 (Access Review)

**Internal Audit** (Verification):
- **Role**: Verify IAM control effectiveness, assess compliance
- **Uses Framework For**: Audit planning, evidence requirements, control testing
- **Key Sections**: POL-S5 (Assessment Evidence), all assessment workbooks

**External Auditors** (Compliance Verification):
- **Role**: ISO 27001 certification audits, regulatory audits
- **Uses Framework For**: Understanding control implementation, evidence review
- **Key Sections**: All POL sections (control requirements), assessment dashboard

---

### 4.2 RACI Matrix

**Responsibility Assignment** (for key IAM processes):

| Activity | IAM Team | Security | HR | IT Ops | Managers | System Owners | Audit |
|----------|----------|----------|-----|---------|----------|---------------|-------|
| **Access Control Policy Development** | C | R/A | C | C | I | C | I |
| **Identity Provisioning (Joiner)** | R | I | A | R | C | I | I |
| **Identity Deprovisioning (Leaver)** | R | I | A | R | I | I | I |
| **Access Request Approval** | I | C | I | I | A | A | I |
| **Access Provisioning** | R | I | I | R | I | C | I |
| **Access Review Execution** | C | C | I | I | R/A | R/A | I |
| **RBAC Role Definition** | C | C | C | C | C | A | I |
| **SoD Violation Remediation** | C | R | I | C | A | C | I |
| **Orphaned Account Detection** | R | A | C | I | I | I | I |
| **IAM Assessment** | C | R/A | C | I | I | I | C |
| **Audit Evidence Provision** | C | R | C | C | C | C | A |

**Key**:
- **R** = Responsible (does the work)
- **A** = Accountable (final approval/authority)
- **C** = Consulted (provides input)
- **I** = Informed (kept updated)

---

## 5. Regulatory Framework

### 5.1 Regulatory Categorization (per ISMS-POL-00)

[Organization] applies the **three-tier regulatory framework** defined in ISMS-POL-00 (Regulatory Applicability Framework).

---

### 5.2 Tier 1: Mandatory Compliance

**These regulations apply to ALL organizations and MUST be complied with**:

#### 5.2.1 Swiss Federal Act on Data Protection (FADP)

**Applicability**: All Swiss organizations, all organizations processing Swiss residents' personal data

**Relevant Provision**: **Article 8 - Data Security**

**Requirements**:
- Technical and organizational measures appropriate to risk
- Access to personal data restricted to authorized persons only
- Access controls must prevent unauthorized access to personal data

**IAM Framework Compliance**:
- A.5.15: Access control policy defines who accesses personal data
- A.5.16: Identity lifecycle ensures only active employees have access
- A.5.18: Access reviews verify personal data access is appropriate

**Evidence Required**:
- Access control policy document
- User inventory (who has access)
- Access rights matrix (who accesses personal data)
- Access review results (periodic verification)
- Deprovisioning logs (terminated employees' access removed)

---

#### 5.2.2 EU General Data Protection Regulation (GDPR)

**Applicability**: Organizations processing EU residents' personal data

**Relevant Provision**: **Article 32 - Security of Processing**

**Requirements**:
> Taking into account the state of the art, the costs of implementation and the nature, scope, context and purposes of processing as well as the risk of varying likelihood and severity for the rights and freedoms of natural persons, the controller and the processor shall implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk, including inter alia as appropriate:
> (a) the pseudonymisation and encryption of personal data;
> (b) the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services;
> (c) the ability to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident;
> (d) a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing.

**Access Control Specific Requirements** (GDPR Recital 39):
> Personal data should be processed in a manner that ensures appropriate security and confidentiality of the personal data, including for preventing unauthorised access to or use of personal data and the equipment used for the processing.

**IAM Framework Compliance**:
- **Article 32(1)**: Access controls are "appropriate technical measures"
- **Article 32(1)(b)**: Confidentiality ensured by restricting access
- **Article 32(1)(d)**: Regular assessment via access reviews and IAM audits

**Specific GDPR-IAM Alignment**:
- **Need-to-know principle**: Access limited to those requiring personal data for legitimate purposes
- **User authentication**: Verify identity before granting access (A.8.5 integration)
- **Access logging**: Maintain audit trail of personal data access (A.8.16 integration)
- **Timely deprovisioning**: Remove access immediately upon termination
- **Periodic review**: Quarterly/annual recertification of personal data access

**Evidence Required**:
- Access control policy (demonstrating "appropriate measures")
- Access rights matrix (showing restricted access to personal data)
- Access review results (demonstrating regular assessment per Article 32(1)(d))
- Provisioning/deprovisioning timeliness reports
- Audit logs (who accessed personal data, when)

---

#### 5.2.3 ISO/IEC 27001:2022

**Applicability**: Organizations implementing ISO 27001 ISMS

**Relevant Controls**:
- **A.5.15 - Access Control**
- **A.5.16 - Identity Management**
- **A.5.18 - Access Rights**

**Requirements**: See Section 2 (ISO 27001:2022 Control Alignment)

**Evidence Required**:
- Statement of Applicability (SoA) with controls marked "Applicable"
- Implementation evidence per control (this framework provides)
- Assessment results (6 workbooks + dashboard)

---

### 5.3 Tier 2: Conditional Compliance

**These regulations apply IF specific conditions are met**:

#### 5.3.1 FINMA Regulations (Swiss Financial Institutions)

**Applicability Trigger**: Organization holds a FINMA license (bank, securities dealer, insurance company, fund management company)

**Determination**: Check with Legal/Compliance team whether FINMA-regulated

**Relevant Regulations**:

**FINMA Circular 2023/1 - Operational Risks and Resilience (Banks)**

**Relevant Provisions**:
- **Margin 50-62**: Information security requirements
- **Margin 56**: User administration and authorization
- **Margin 58**: Segregation of duties

**Margin 56 - User Administration and Authorization**:
> Banks must establish processes for user administration that ensure access rights are granted, modified, and revoked in a timely and controlled manner. User accounts must be assigned based on the principle of least privilege and need-to-know. Authorization processes must be documented and subject to periodic review.

**Margin 58 - Segregation of Duties**:
> To prevent fraud and error, banks must implement segregation of duties for critical processes. Conflicting roles and functions must be identified and separated. Where full separation is not feasible, compensating controls must be documented and approved by senior management.

**IAM Framework Compliance**:
- A.5.15: Access control policy aligned with operational risk management
- A.5.15: Segregation of duties matrix and monitoring
- A.5.16: User authorization processes (joiner/mover/leaver compliance)
- A.5.18: Access review and recertification procedures
- A.5.18: Identity management for all user types (employees, contractors, external)

**Evidence Required**:
- Access control policy approved by CISO/CRO
- Segregation of duties matrix
- SoD violation reports (should be zero or documented exceptions)
- User authorization procedures (documented workflows)
- Access review completion reports (quarterly for critical systems)
- Provisioning/deprovisioning timeliness (≥95% on-time)

**FINMA Circular 2008/7 - Outsourcing (Banks)**:
- Third-party identity provider management
- Vendor access governance
- Cloud identity service risk assessment

---

#### 5.3.2 DORA (Digital Operational Resilience Act)

**Applicability Trigger**: Organization is a financial entity operating in the EU (banks, payment institutions, investment firms, insurance companies, crypto-asset service providers)

**Determination**: Check with Legal/Compliance team whether DORA-regulated

**Relevant Provisions**:

**Article 6 - ICT Risk Management Framework**:
> Financial entities shall have in place an internal governance and control framework that ensures an effective and prudent management of ICT risk...

**Article 6(5) - Asset Management**:
> Financial entities shall identify and document all ICT-supported functions and the information assets supporting those functions. This includes... access controls and authentication mechanisms.

**Article 28-30 - Third-Party Service Provider Management**:
> Financial entities shall... identify and assess all relevant risks with regard to contractual arrangements on the use of ICT services provided by ICT third-party service providers.

**IAM Framework Compliance**:
- Article 6: ICT risk management framework includes access control governance
- Article 6(5): Identification of ICT-supported functions and assets (relates to access mapping in access rights matrix)
- Article 28-30: Third-party service provider management (identity provider risk assessment per ISMS-REF-A.5.23)

**Identity Provider Risk Assessment** (if using cloud identity services):
- Assess Okta, Auth0, Azure AD as "ICT third-party service providers"
- Document data residency (US CLOUD Act implications)
- Evaluate operational resilience (SLA, availability, incident response)
- Contractual arrangements (data processing agreement, exit strategy)

**Evidence Required**:
- Access control policy as part of ICT risk management framework
- Access rights matrix (mapping users to ICT-supported functions)
- Identity provider risk assessment (if using Okta, Azure AD, etc.)
- Third-party vendor access governance procedures

---

#### 5.3.3 NIS2 (Network and Information Security Directive)

**Applicability Trigger**: Organization is classified as "essential entity" or "important entity" under NIS2 (energy, transport, banking, health, digital infrastructure, etc.)

**Determination**: Check with Legal/Compliance team whether NIS2-regulated

**Relevant Provisions**:

**Article 21(2) - Cybersecurity Risk Management Measures**:

**(a) Policies on risk analysis and information security**:
> Essential and important entities shall adopt policies on risk analysis and information security policies.

**(d) Policies on access control and asset management**:
> Measures shall include policies for access control and asset management.

**(f) Practices for identity and access management**:
> Measures shall include practices for the use of multi-factor authentication or continuous authentication solutions, secured voice, video and text communications and secured emergency communication systems.

**IAM Framework Compliance**:
- Article 21(2)(a): Access control policy as part of information security
- Article 21(2)(d): Access control and asset management policies (access rights matrix ties access to assets per A.5.9)
- Article 21(2)(f): Identity and access management practices (IAM governance framework)

**Evidence Required**:
- Access control policy document
- Identity and access management procedures
- Access rights matrix (linking users to assets)
- Integration with A.8.5 (multi-factor authentication for identity management)

---

### 5.4 Risk Considerations

#### 5.4.1 US CLOUD Act (Data Sovereignty)

**Not a direct compliance requirement**, but **risk consideration** when selecting identity providers.

**US CLOUD Act** (Clarifying Lawful Overseas Use of Data Act):
- US law enforcement can compel US companies to provide data, even if stored outside US
- Applies to: Microsoft (Azure AD), Okta, Auth0, Google (Workspace)

**Identity Data at Risk**:
- User identities (names, email addresses)
- User attributes (department, manager, location)
- Group memberships
- Access rights mappings

**Risk Assessment**:
- **High sensitivity organizations** (government, defense, critical infrastructure):
  - Consider EU-based identity providers OR on-premises solutions
  - Document CLOUD Act risk in identity provider selection
  
- **Standard organizations**:
  - US CLOUD Act risk acceptable (user identity data is lower sensitivity than business data)
  - Ensure data processing agreements address data access requests

**Framework Guidance**:
- See **ISMS-REF-A.5.23** (Third-Party Service Provider Registry) for identity provider jurisdictions
- Document identity provider selection rationale
- Include CLOUD Act assessment in vendor risk assessment (DORA Article 28-30)

---

### 5.5 Tier 3: Informational Reference / Best Practice Alignment

**These frameworks are NOT mandatory but provide best practice guidance**:

#### 5.5.1 NIST SP 800-53 (Access Control & Identity Management)

**Applicability**: Informational reference (mandatory only for US federal contractors per FISMA)

**Relevant Control Families**:

**AC (Access Control)**:
- **AC-2**: Account Management (aligns with A.5.16 Identity Management)
- **AC-3**: Access Enforcement (aligns with A.5.15 Access Control)
- **AC-5**: Separation of Duties (aligns with A.5.15 SoD requirements)
- **AC-6**: Least Privilege (aligns with A.5.15 access principles)

**IA (Identification and Authentication)**:
- **IA-2**: Identification and Authentication (Organizational Users) - integrates with A.8.5
- **IA-4**: Identifier Management (aligns with A.5.16 identity lifecycle)
- **IA-5**: Authenticator Management (integrates with A.8.5)

**Use in Framework**:
- NIST provides detailed implementation guidance
- AC-2 control enhancement examples inform identity lifecycle processes
- AC-5 SoD guidance informs segregation of duties matrix

---

#### 5.5.2 CIS Controls

**CIS Control 5: Account Management**:
- Use unique passwords
- Disable dormant accounts
- Restrict administrator privileges
- Establish and maintain an inventory of service accounts
- Centralize account management

**CIS Control 6: Access Control Management**:
- Establish an access granting process
- Establish an access revoking process
- Require MFA for externally-exposed applications
- Require MFA for remote network access

**Use in Framework**:
- CIS Controls provide tactical implementation checklist
- Account Management (CIS 5) aligns with A.5.16 lifecycle
- Access Control Management (CIS 6) aligns with A.5.18 rights management

---

#### 5.5.3 ISO/IEC 27002:2022 (Implementation Guidance)

**Purpose**: Provides detailed implementation guidance for ISO 27001 controls

**Relevant Sections**:
- **5.15**: Access control (expanded guidance beyond control text)
- **5.16**: Identity management (implementation examples)
- **5.18**: Access rights (review process examples)

**Use in Framework**:
- ISO 27002 provides implementation examples across different organizational contexts
- Guidance on contractor identity management
- Examples of access review frequency based on criticality

---

### 5.6 United States Federal Requirements

**Note**: References to US federal frameworks (FISMA, NIST cybersecurity requirements) apply **ONLY** where [Organization] has explicit US federal contractual obligations, as defined in ISMS-POL-00.

**Determination**:
- Check with Legal/Compliance: Do we have US federal contracts?
- If YES: NIST SP 800-53 becomes **Tier 2 (Conditional)** instead of Tier 3
- If NO: NIST remains informational reference only

---

## 6. Identity Provider Considerations

### 6.1 Cloud Identity Providers

When selecting identity providers for [Organization], consider the following **Tier 8** providers (per ISMS-REF-A.5.23 - Security & Identity category):

**Major Cloud Identity Platforms**:
- **Okta** (Identity-as-a-Service)
  - HQ: USA (San Francisco)
  - Data residency: EU regions available
  - Compliance: ISO 27001, SOC 2, GDPR
  
- **Auth0** (Identity-as-a-Service)
  - HQ: USA (owned by Okta)
  - Data residency: EU regions available
  - Compliance: ISO 27001, SOC 2, GDPR
  
- **Microsoft Azure Active Directory / Entra ID**
  - HQ: USA
  - Data residency: EU regions available (data residency commitments)
  - Compliance: ISO 27001, SOC 2, GDPR
  
- **Google Workspace** (Google Cloud Identity)
  - HQ: USA
  - Data residency: EU regions available
  - Compliance: ISO 27001, SOC 2, GDPR

**Assessment Criteria** (per ISMS-REF-A.5.23):
1. **Data Residency**:
   - US CLOUD Act implications (US law enforcement access)
   - EU data residency options (GDPR compliance)
   - Swiss data residency (if required for FADP)

2. **Compliance Certifications**:
   - ISO 27001 (information security)
   - SOC 2 Type II (operational security)
   - GDPR compliance (if processing EU personal data)

3. **Identity Lifecycle Capabilities**:
   - Automated provisioning/deprovisioning (API-driven)
   - HR system integration (Workday, SAP SuccessFactors, custom)
   - Group management and RBAC support

4. **Access Review Capabilities**:
   - Built-in access recertification
   - Access review workflows
   - Integration with GRC platforms (Saviynt, SailPoint)

5. **Multi-Factor Authentication (MFA) Support**:
   - Integrates with A.8.5 (Secure Authentication)
   - MFA methods supported (TOTP, push, WebAuthn, biometrics)

6. **Privileged Access Features**:
   - Integrates with A.8.2 (Privileged Access Rights)
   - Conditional access policies
   - Just-in-time (JIT) access

7. **API Capabilities**:
   - REST APIs for automation
   - Webhook support (real-time event notifications)
   - SCIM protocol (System for Cross-domain Identity Management)

---

### 6.2 On-Premises Identity Systems

**Traditional Identity Platforms**:
- **Active Directory** (Microsoft)
  - Most common on-premises identity system
  - Full control over data residency
  - Requires infrastructure management
  
- **OpenLDAP**
  - Open-source LDAP directory
  - Full control, customizable
  - Requires technical expertise
  
- **FreeIPA**
  - Open-source identity management (Red Hat)
  - Integrated solution (LDAP + Kerberos + DNS)
  
- **Custom Identity Solutions**
  - Organization-built identity systems
  - Legacy systems (mainframe, proprietary)

**Considerations**:
- Full data sovereignty (no US CLOUD Act risk)
- Infrastructure cost (servers, management, patches)
- Technical expertise required
- Integration complexity (cloud applications require federation)

---

### 6.3 Hybrid Identity Models

**Common Hybrid Approaches**:
- **Azure AD Connect** (AD → Azure AD synchronization)
- **Okta AD Agent** (AD → Okta synchronization)
- **Google Cloud Directory Sync** (AD → Google Workspace)

**Benefits**:
- Single source of truth (on-prem AD)
- Cloud application access (synchronized cloud identities)
- Gradual cloud migration path

**Considerations**:
- Synchronization latency (real-time vs. scheduled)
- Conflict resolution (changes in both systems)
- Password synchronization (security implications)

---

### 6.4 Framework Neutrality

**Critical Principle**: This IAM framework is **vendor-neutral**.

**What this means**:
- Framework requirements apply **regardless of identity provider**
- Implementation examples span **multiple technologies**
- Assessment tools measure **compliance, not specific tools**

**Example**:
> **Requirement**: User accounts must be deprovisioned within 24 hours of termination.

**Implementation varies by technology**:
- **Active Directory**: PowerShell script disables account, moves to disabled OU
- **Azure AD**: Azure Automation runbook disables account
- **Okta**: Okta Workflows disables account, removes group memberships
- **Custom system**: API call to identity service with termination date

**Assessment is technology-neutral**:
- Measure: Termination date vs. account disable date
- Data source: Any identity system (AD, Azure AD, Okta, custom)
- Compliance: ≥98% within 24 hours

**Organizations must**:
1. Select identity provider based on requirements
2. Document configuration in assessment workbooks
3. Demonstrate compliance regardless of technology choice

---

## 7. Definitions & Terminology

### 7.1 Identity & Access Concepts

**Identity**:
- Representation of a user, person, or entity in an identity system
- Example: User "alice@example.com" in Azure AD

**User Account**:
- Digital account associated with an identity
- Enables authentication and access to systems
- Example: Active Directory account "DOMAIN\alice"

**User ID / Username**:
- Unique identifier for a user account
- Example: "alice", "alice@example.com", "EXT-vendor123"

**Access Control**:
- Process of granting or denying requests to access information or systems
- Combination of authentication (who you are) + authorization (what you can do)

**Access Rights**:
- Permissions granted to a user for specific resources
- Example: "Read" access to Finance folder, "Admin" access to HR system

**Authorization**:
- Determination of what an authenticated user is allowed to do
- Example: Alice is authenticated (verified identity) → authorized to read finance data

---

### 7.2 IAM Processes

**Joiner** (Onboarding):
- Process of creating identity and granting access for new user
- Triggered by: New hire, contractor start, vendor engagement
- Result: User account created, initial access assigned

**Mover** (Transfer):
- Process of modifying identity and access when user changes roles
- Triggered by: Promotion, department transfer, role change
- Result: Old role access removed, new role access granted

**Leaver** (Offboarding):
- Process of disabling/deleting identity and removing all access
- Triggered by: Termination, resignation, contract end
- Result: User account disabled, all access revoked

**Provisioning**:
- Granting access to a user (creating account, assigning rights)
- Example: "Provision Alice with access to Finance system"

**Deprovisioning**:
- Removing access from a user (disabling account, revoking rights)
- Example: "Deprovision Bob's account after termination"

**Access Review / Access Recertification**:
- Periodic verification that users have appropriate access
- Managers/system owners confirm or remove access
- Example: "Quarterly review of admin access"

---

### 7.3 Access Control Models

**Role**:
- Collection of access rights associated with a job function
- Example: "Financial Analyst" role includes read access to finance systems

**Group**:
- Collection of users with similar access needs
- Example: "Finance_Team" group has access to Finance folder

**RBAC (Role-Based Access Control)**:
- Access model where rights are assigned via roles, not directly to users
- Example: Assign "Financial Analyst" role to user → user inherits all role permissions

**Privilege**:
- Elevated access right beyond standard user
- Example: Administrator privilege, root access, domain admin

---

### 7.4 Access Control Principles

**Least Privilege**:
- Users have minimum access necessary to perform job functions
- Reduces risk of accidental or intentional misuse

**Need-to-Know**:
- Users only access information required for their specific duties
- Subset of least privilege (data-focused)

**Segregation of Duties (SoD)**:
- Separation of conflicting roles to prevent fraud/error
- Example: Same person cannot both request payment AND approve payment

**Default Deny**:
- No access granted unless explicitly authorized
- Opposite of "default allow"

**Defense in Depth**:
- Multiple layers of access control
- Example: VPN + authentication + authorization + audit logging

---

### 7.5 Account Types

**Employee Account**:
- Standard user account for internal staff
- Linked to HR system (authoritative source)
- Standard lifecycle (joiner/mover/leaver)

**Contractor Account**:
- Time-bound account for temporary workers
- Sponsored by internal employee
- Automatic expiration at contract end
- Identifier: Often prefixed (e.g., "EXT-" or "CTR-")

**Vendor Account**:
- Third-party service provider account
- Sponsored by internal employee
- Time-bound (contract period)
- Enhanced monitoring

**Service Account**:
- Non-human account used by applications/systems
- No expiration date (until service decommissioned)
- Owner assigned (person responsible)
- Example: "svc-backup", "app-webserver"

**Shared Account**:
- Account used by multiple people (discouraged)
- Requires business justification
- Enhanced monitoring (accountability concern)
- Example: "admin", "root" (if not using individual admin accounts)

**Emergency Account / Break-Glass Account**:
- Account for disaster recovery scenarios
- Stored securely (password vault)
- Use triggers incident investigation
- Example: "EMERG-ADMIN"

---

### 7.6 Compliance & Audit Terms

**Orphaned Account**:
- Account without valid owner or business justification
- Examples: Ex-employee account not disabled, contractor account past contract end
- Security risk (no accountability)

**Inactive Account**:
- Account that hasn't been used recently (no login in 90+ days)
- May indicate orphaned account or no longer needed

**Privilege Creep**:
- Accumulation of excess access rights over time
- Example: User changes roles but retains access from all previous roles

**Access Matrix**:
- Mapping of users to systems/applications to access levels
- Example: User Alice → Finance System → Read access

**SoD Violation**:
- User has conflicting roles that violate segregation of duties
- Example: User can both submit expense report AND approve it

**Provisioning Timeliness**:
- Measure of how quickly new users receive access
- Target: Access ready by start date (≤0 days delay)

**Deprovisioning Timeliness**:
- Measure of how quickly terminated users' access is removed
- Target: Access disabled within 24 hours (≤1 day delay)

---

### 7.7 Identity System Terms

**Authoritative Source**:
- System of record for identity data
- Typically HR system (employee hire/termination dates, job titles)

**Identity Repository**:
- System storing user identities and attributes
- Examples: Active Directory, Azure AD, LDAP directory

**Identity Synchronization**:
- Process of keeping identity data consistent across multiple systems
- Example: HR system → Active Directory → Azure AD

**Federation**:
- Trust relationship between identity providers
- Enables single sign-on (SSO) across organizations
- Protocols: SAML, OAuth, OpenID Connect

**Single Sign-On (SSO)**:
- Authenticate once, access multiple systems
- Example: Log in to Okta → access all connected applications

---

## 8. Framework Navigation

### 8.1 Document Hierarchy

This IAM framework consists of **11 policy documents** and **5 implementation guides**:

**Master Framework**:
- `ISMS-POL-A.5.15-16-18_Master_Framework.md` - Overview and navigation

**Policy Layer** (POL):
1. `ISMS-POL-A.5.15-16-18-S1_Executive_Control_Alignment.md` (this document)
2. `ISMS-POL-A.5.15-16-18-S2_Access_Control_Policy_A515.md`
3. `ISMS-POL-A.5.15-16-18-S3_Identity_Management_A516.md`
4. `ISMS-POL-A.5.15-16-18-S4_Access_Rights_Management_A518.md`
5. `ISMS-POL-A.5.15-16-18-S5_Assessment_Evidence_Framework.md`

**Implementation Layer** (IMP):
1. `ISMS-IMP-A.5.15-16-18-S1_Access_Control_Governance.md`
2. `ISMS-IMP-A.5.15-16-18-S2_Identity_Lifecycle_Process.md`
3. `ISMS-IMP-A.5.15-16-18-S3_Role_Definition_Assignment.md`
4. `ISMS-IMP-A.5.15-16-18-S4_Access_Review_Process.md`
5. `ISMS-IMP-A.5.15-16-18-S5_IAM_Assessment_Procedures.md`

**Assessment Tools**:
- 6 Python scripts generating Excel workbooks
- 1 consolidated dashboard script
- 2 utility scripts (normalization, sanity check)

---

### 8.2 How to Use This Framework

**For Implementers** (IAM Team, IT Operations):
1. Start with: **IMP-S2** (Identity Lifecycle Process)
2. Implement: Joiner/mover/leaver automation
3. Then: **IMP-S3** (Role Definition) - build RBAC framework
4. Then: **IMP-S4** (Access Review Process) - establish periodic reviews
5. Finally: **IMP-S5** (IAM Assessment) - measure compliance

**For Security/Governance** (CISO, Security Team):
1. Start with: **POL-S1** (this document) - understand scope
2. Define: **POL-S2** (Access Control Policy) - strategic requirements
3. Document: **POL-S3/S4** (Identity & Access Rights) - process requirements
4. Assess: **POL-S5** (Assessment Framework) - evidence collection
5. Review: **Dashboard** - executive compliance summary

**For Managers** (Access Approvers/Reviewers):
1. Read: **IMP-S1** (Access Control Governance) - your approval responsibilities
2. Execute: **IMP-S4** (Access Review Process) - how to review access
3. Use: **Access Review Workbook** - review tool

**For Auditors** (Internal/External):
1. Review: **POL-S1** (this document) - control alignment
2. Review: **POL-S5** (Assessment Framework) - evidence requirements
3. Request: **6 assessment workbooks + dashboard** - compliance evidence
4. Verify: Implementation per POL-S2/S3/S4 requirements

---

## 9. Next Steps

### 9.1 For Organizations Implementing This Framework

**Phase 1: Foundation** (Weeks 1-4)
- [ ] Read POL-S1 (this document) - understand scope and requirements
- [ ] Identify current identity systems (AD, Azure AD, Okta, custom)
- [ ] Inventory user types (employees, contractors, vendors, service accounts)
- [ ] Assess current state (joiner/mover/leaver processes, access reviews)

**Phase 2: Policy Development** (Weeks 5-8)
- [ ] Develop access control policy (POL-S2)
- [ ] Define identity lifecycle requirements (POL-S3)
- [ ] Define access rights management requirements (POL-S4)
- [ ] Document assessment methodology (POL-S5)

**Phase 3: Implementation** (Weeks 9-16)
- [ ] Implement access control governance (IMP-S1)
- [ ] Automate identity lifecycle processes (IMP-S2)
- [ ] Develop RBAC framework (IMP-S3)
- [ ] Establish access review process (IMP-S4)

**Phase 4: Assessment** (Weeks 17-20)
- [ ] Generate user inventory workbook
- [ ] Generate access rights matrix workbook
- [ ] Execute access reviews (generate review results workbook)
- [ ] Assess RBAC adoption (generate role compliance workbook)
- [ ] Measure lifecycle compliance (generate lifecycle workbook)
- [ ] Consolidate dashboard

**Phase 5: Continuous Improvement** (Ongoing)
- [ ] Monthly: User inventory updates, orphaned account scans
- [ ] Quarterly: Access reviews (critical systems), role compliance checks
- [ ] Annual: Comprehensive IAM assessment (all six workbooks)

---

### 9.2 For Auditors Reviewing This Framework

**Pre-Audit Preparation**:
1. Review this document (POL-S1) - understand control integration approach
2. Review POL-S2/S3/S4 - understand specific control requirements
3. Review POL-S5 - understand assessment methodology and evidence

**Audit Evidence Requests**:
- **For A.5.15 (Access Control)**:
  - Access control policy document
  - Segregation of duties matrix
  - SoD violation reports
  - Exception approval records
  
- **For A.5.16 (Identity Management)**:
  - User inventory (Workbook 1)
  - Provisioning/deprovisioning timeliness reports (Workbook 1 & 5)
  - Orphaned account detection reports (Workbook 1)
  
- **For A.5.18 (Access Rights)**:
  - Access rights matrix (Workbook 2)
  - Access review results (Workbook 3)
  - Role compliance assessment (Workbook 4)

**Audit Testing**:
- Sample user accounts → verify provisioning timeliness
- Sample terminated employees → verify access removed within 24h
- Sample access reviews → verify completion and remediation
- Sample SoD violations → verify documented exceptions or remediated

**Expected Maturity**:
- **Initial (Ad-hoc)**: Manual processes, inconsistent enforcement, limited evidence
- **Managed (Repeatable)**: Documented processes, some automation, periodic reviews
- **Defined (Standardized)**: Automated lifecycle, RBAC framework, regular assessments
- **Optimizing (Continuous)**: Real-time monitoring, predictive analytics, proactive remediation

---

## 10. Document Approval

**Prepared By**: [Name], [Title] - [Date]  
**Reviewed By**: [Name], [Title] - [Date]  
**Approved By**: [Name], CISO - [Date]

**Next Review Date**: [Date + 12 months]

**Version History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial framework release |

---

**END OF SECTION 1 (POL-S1)**

**Next Document**: ISMS-POL-A.5.15-16-18-S2_Access_Control_Policy_A515.md
