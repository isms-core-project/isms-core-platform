# ISMS-POL-A.8.2-3-5 – Authentication & Privileged Access Security

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Authentication & Privileged Access Security |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.2-3-5 |
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
- Security Operations: Security Operations Manager
- IT Operations: IT Operations Manager
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.15-16-18 (Identity & Access Management - IAM Foundation)
- ISMS-IMP-A.8.2-3-5 (Implementation Assessment Suite - 6 documents)
- ISMS-CTX-A.8.2-3-5 (Authentication & PAM Technology Landscape)
- ISMS-REF-A.5.23 (Third-Party Service Provider Registry - Identity & Authentication Providers)
- ISO/IEC 27001:2022 Controls A.8.2, A.8.3, A.8.5
- ISO/IEC 27002:2022 (Implementation Guidance for Controls 8.2, 8.3, 8.5)

---

## Executive Summary

This policy establishes [Organization]'s requirements for authentication security, privileged access management, and technical access enforcement in accordance with ISO/IEC 27001:2022 Controls A.8.5 (Secure Authentication), A.8.2 (Privileged Access Rights), and A.8.3 (Information Access Restriction).

**Scope**: This policy applies to all authentication mechanisms (passwords, MFA, SSO, certificates, biometrics), all privileged accounts (administrative, root, elevated rights), and all technical access controls (file systems, databases, applications, APIs, networks) regardless of deployment model, technology platform, or organizational size.

**Purpose**: Define organizational requirements for authentication security, privileged access management, and access enforcement. This policy establishes WHAT controls are required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8.2-3-5.

**Combined Control Approach**: These three controls are implemented as a unified framework because they form inseparable layers of the authentication and access security stack. Separate implementation would result in disconnected authentication strategies, fragmented privileged access management, and inconsistent access enforcement.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss FADP, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, DORA, NIS2, PCI DSS) apply where [Organization]'s business activities trigger applicability. Notably, NIS2 Article 21(2)(e) explicitly mandates multi-factor authentication for essential and important entities.

---


**Document ID**: ISMS-POL-A.8.2-3-5-S1  
**Title**: Authentication & Privileged Access Security Framework - Executive Summary and Control Alignment  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial authentication & privileged access framework (A.8.2/3/5) |

**Review Cycle**: Annual (aligned with IAM foundation review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Identity & Access Management Lead
- Security Architecture Review: Security Architect
- Implementation Review: Systems Administrators

**Distribution**: Security team, IAM team, systems administrators, IT operations, application owners, auditors  
**Related Documents**: 
- ISMS-POL-A.5.15-16-18 (Identity & Access Management Foundation)
- ISMS-POL-A.8.2-3-5-S2 through S5 (Detailed requirements)
- ISMS-POL-00 (Regulatory Applicability Framework)

---

## 1. Executive Summary

### 1.1 The Authentication & Privileged Access Challenge

Authentication and privileged access form the **most critical security boundary** in any organization. These controls determine WHO can access systems and WHAT they can do once inside.

**The Security Reality**:

Weak authentication and poor privileged access management are the #1 attack vector:
- **81% of breaches** involve compromised credentials (Verizon DBIR)
- **Privileged accounts** are the primary target - they're the "keys to the kingdom"
- **Credential stuffing, phishing, and privilege escalation** are standard attack methods
- **Lateral movement** after initial compromise depends on privileged access

Compromised authentication or privileged access enables attackers to:
- **Access ANY system** - privileged accounts can reach everything
- **Steal sensitive data** - authentication bypassed means access to confidential information
- **Modify critical systems** - admin access allows destructive changes
- **Cover their tracks** - privileged access includes log manipulation capabilities
- **Establish persistence** - create backdoor accounts for future access
- **Pivot laterally** - use one compromised account to access other systems

**Why These Three Controls Together?**

A.8.5 (Secure Authentication), A.8.2 (Privileged Access Rights), and A.8.3 (Information Access Restriction) form an **integrated security layer**:

1. **A.8.5 proves WHO you are** â†’ Authentication mechanisms (passwords, MFA, SSO, certificates)
2. **A.8.2 controls SPECIAL access** â†’ Privileged accounts with elevated rights require stronger controls
3. **A.8.3 enforces WHAT you can access** â†’ Technical restrictions based on authenticated identity

You cannot implement these controls separately:
- **Authentication without access enforcement** = identity without protection
- **Privileged access without authentication** = unaccountable admin actions
- **Access restrictions without authentication** = no way to verify identity

### 1.2 Business Impact

**Risk Reduction Through Unified Framework**:

- **Confidentiality**: Multi-factor authentication and privileged access controls prevent unauthorized data access
- **Integrity**: Admin tiering and session recording prevent unauthorized system modifications
- **Availability**: Proper authentication prevents denial-of-service through account lockout attacks
- **Accountability**: Authentication logging and privileged session recording enable forensic investigation
- **Compliance**: NIS2 MFA mandate, GDPR Article 32, FADP Article 8 requirements met

**Operational Benefits**:

- **Reduced credential compromise** through MFA deployment (99.9% effective per Microsoft)
- **Limited blast radius** through admin tiering (Tier 0 compromise doesn't expose all systems)
- **Faster incident response** through privileged session recordings and authentication logs
- **Improved user experience** through Single Sign-On (SSO)
- **Audit efficiency** through unified authentication and access assessment

**Regulatory Compliance**:

- **NIS2 Article 21(2)(e)**: Multi-factor authentication EXPLICITLY REQUIRED (not optional)
- **GDPR Article 32**: Security of processing requires authentication and access controls
- **Swiss FADP Article 8**: Technical measures for data security include authentication
- **FINMA Circular 2023/1**: MFA for critical systems, privileged access monitoring (if applicable)
- **ISO/IEC 27001:2022**: Controls A.8.2, A.8.3, A.8.5 implementation

### 1.3 Combined Control Approach

**Rationale for Unified Implementation**:

These three controls cannot be meaningfully implemented in isolation:

1. **Shared Identity Infrastructure**: All three controls use the same identity systems (Azure AD, Okta, Active Directory, PAM solutions)

2. **Technical Dependencies**:
   - A.8.5 authenticates users â†’ A.8.2 determines if they have privileged access â†’ A.8.3 enforces what they can access
   - Privileged access (A.8.2) REQUIRES stronger authentication (A.8.5) than normal access
   - Access enforcement (A.8.3) depends on authenticated identity (A.8.5)

3. **Evidence Consolidation**: 
   - MFA logs serve A.8.5 (authentication), A.8.2 (privileged MFA), and A.8.3 (access based on authentication)
   - Privileged access logs serve A.8.2 (admin monitoring) and A.8.3 (access enforcement)
   - Permission audits serve A.8.3 (access restrictions) and A.8.2 (privileged account rights)

4. **Assessment Synergy**: Unified assessment avoids duplicate data collection and provides holistic view

5. **Implementation Efficiency**: Combined framework is 3x more efficient than separate implementations

**Audit Clarity**:

Despite combined implementation, each control maintains:
- **Distinct requirements sections** (S2 for A.8.5, S3 for A.8.2, S4 for A.8.3)
- **Separate evidence collection** per control
- **Individual compliance scoring** for Statement of Applicability (SoA)
- **Clear control mapping** for auditors

### 1.4 Relationship to IAM Foundation (A.5.15-16-18)

This Authentication & Privileged Access Security Framework **builds on** the Identity & Access Management Foundation established in ISMS-POL-A.5.15-16-18:

**IAM Foundation (A.5.15-16-18) provides:**
- **A.5.16**: Identity lifecycle management (user provisioning, de-provisioning)
- **A.5.15**: Access control policy (who gets access, approval workflows)
- **A.5.18**: Access rights management (periodic reviews, recertification)

**This Framework (A.8.2-3-5) implements:**
- **A.8.5**: HOW users prove their identity (authentication mechanisms)
- **A.8.2**: Controls for privileged accounts created by A.5.16
- **A.8.3**: Technical enforcement of access rights defined by A.5.18

**Integration Points**:

| IAM Foundation (A.5.x) | Auth/PAM Framework (A.8.x) | Integration |
|------------------------|----------------------------|-------------|
| A.5.16 creates user accounts | A.8.5 authenticates those users | Same user directory (AD, Azure AD, Okta) |
| A.5.18 assigns access rights | A.8.3 enforces those restrictions | Access rights â†’ File permissions, DB grants, API scopes |
| A.5.18 defines privileged users | A.8.2 controls privileged access | Privileged user inventory â†’ PAM vault |
| A.5.18 reviews access rights | A.8.2 reviews privileged access | Quarterly reviews include admin accounts |

**Practical Example**:
- **A.5.16** creates "john.doe" account and "john.doe.admin" privileged account
- **A.8.5** requires John to authenticate with MFA (password + authenticator app)
- **A.8.2** requires John to use "john.doe.admin" (not "john.doe") for admin tasks, session recorded
- **A.8.3** enforces that "john.doe" can read files, "john.doe.admin" can write files
- **A.5.18** reviews quarterly: Does John still need admin access?

---

## 2. ISO/IEC 27001:2022 Control Alignment

### 2.1 A.8.5 - Secure Authentication

**Official Control Text (ISO/IEC 27001:2022 Annex A.8.5)**:

> *Secure authentication technologies and procedures should be implemented based on information access restrictions and the topic-specific policy on access control.*

**Control Objective**: Ensure users are authenticated using secure mechanisms appropriate to the sensitivity of the information and systems being accessed, with stronger authentication for privileged access.

**Key Requirements**:
- Multi-factor authentication (MFA) deployment - **NIS2 MANDATES this**
- Password policies aligned with modern best practices (length > complexity)
- Single Sign-On (SSO) for improved user experience and security
- Authentication protocols (SAML, OAuth, OpenID Connect, Kerberos, RADIUS)
- Certificate-based authentication for systems and services
- Biometric authentication where appropriate
- Authentication logging and monitoring
- Credential compromise detection and response

**Why This Matters**:

Authentication is the **gateway to all systems**. Weak authentication means:
- **Password-only access** is trivially compromised (phishing, credential stuffing, brute force)
- **No MFA** = single point of failure (one stolen password = full breach)
- **Shared credentials** = no accountability (who did what?)
- **Weak passwords** are cracked in seconds (password123, Summer2024!)

Strong authentication provides:
- **99.9% reduction in account compromise** with MFA (Microsoft data)
- **Phishing resistance** with FIDO2 hardware tokens
- **User convenience** with SSO (one login for multiple applications)
- **Audit trail** of who accessed what and when

**Detailed Requirements**: See ISMS-POL-A.8.2-3-5-S2

**Assessment Evidence**:
- MFA enrollment data and coverage metrics (Workbook 2)
- Authentication mechanism inventory (Workbook 1)
- Password policy configurations
- SSO integration status
- Authentication logs

### 2.2 A.8.2 - Privileged Access Rights

**Official Control Text (ISO/IEC 27001:2022 Annex A.8.2)**:

> *The allocation and use of privileged access rights should be restricted and managed.*

**Control Objective**: Ensure privileged accounts (administrators, root, system accounts) are tightly controlled, monitored, and audited to prevent misuse and detect compromise.

**Key Requirements**:
- Privileged account inventory and classification
- Separation of privileged accounts from user accounts (no daily email with admin account)
- Privileged Access Management (PAM) solutions (password vaulting, session recording)
- Just-in-time (JIT) privileged access (temporary elevation)
- **Admin Tiering Model** (Tier 0/1/2 isolation to prevent lateral movement)
- Multi-factor authentication MANDATORY for all privileged access
- Privileged session recording (keystroke logging or video)
- Privileged access monitoring and alerting
- Quarterly privileged access reviews

**Why This Matters**:

Privileged accounts are the **"keys to the kingdom"**:
- **Privileged account compromise** = complete organizational breach
- **Domain Admin** can access ANY system, modify ANY data, delete ANY log
- **Root/Administrator** accounts bypass all security controls
- **Shared admin passwords** = no accountability for destructive actions
- **Unmonitored privileged access** = attacker dwell time measured in MONTHS

Proper privileged access controls provide:
- **Blast radius limitation** through admin tiering (Tier 0 compromise doesn't reach Tier 1/2)
- **Accountability** through session recording (know exactly what admin did)
- **Credential rotation** through PAM solutions (passwords changed automatically)
- **Temporary access** through JIT (admin access only when needed, auto-revoked)

**Detailed Requirements**: See ISMS-POL-A.8.2-3-5-S3

**Assessment Evidence**:
- Privileged account inventory (Workbook 3)
- PAM solution deployment status
- Privileged access monitoring logs (Workbook 4)
- Session recordings
- Admin tier isolation compliance
- Privileged access review records

### 2.3 A.8.3 - Information Access Restriction

**Official Control Text (ISO/IEC 27001:2022 Annex A.8.3)**:

> *Access to information and other associated assets should be restricted in accordance with the established topic-specific policy on access control.*

**Control Objective**: Ensure technical access controls (file permissions, database grants, API scopes, encryption) enforce the access control policy, implementing principle of least privilege at technical layer.

**Key Requirements**:
- Operating system access controls (NTFS, file system ACLs)
- Database access controls (SQL grants, row-level security)
- Application access controls (RBAC within applications)
- API access controls (OAuth scopes, API keys, rate limiting)
- Cloud resource access controls (IAM policies)
- Data classification enforcement (encryption based on sensitivity)
- Network segmentation for access restriction (firewalls between zones)
- Default deny principle (explicit allow required)
- Access control effectiveness testing (penetration testing, configuration audits)

**Why This Matters**:

Technical access controls are the **last line of defense**:
- **Misconfigured permissions** = data exposed to unauthorized users
- **Overly permissive access** = violation of need-to-know principle
- **No default deny** = accidental access grants (everyone can access everything)
- **Encryption without access control** = key theft bypasses security

Proper access restriction provides:
- **Defense in depth** - multiple layers of access controls
- **Principle of least privilege** enforced at technical level (not just policy)
- **Audit trail** of access attempts (successful and denied)
- **Containment** - even if one system compromised, lateral movement blocked

**Detailed Requirements**: See ISMS-POL-A.8.2-3-5-S4

**Assessment Evidence**:
- Permission audit results (file systems, databases, applications) (Workbook 5)
- Configuration compliance scans
- Penetration test reports (access control bypass attempts)
- Data classification and encryption status
- Network segmentation documentation (A.8.22 integration)

---

## 3. Scope and Applicability

### 3.1 Scope

This Authentication & Privileged Access Security Framework applies to:

**Authentication Mechanisms (A.8.5)**:
- All user authentication to [Organization] systems
- Passwords, MFA, SSO, certificate-based, biometric authentication
- On-premises authentication (Active Directory, RADIUS)
- Cloud authentication (Azure AD, Okta, Google Workspace)
- Hybrid authentication (AD + cloud sync)

**Privileged Access (A.8.2)**:
- All privileged accounts (system administrators, DBAs, security admins, cloud admins)
- Privileged account types: Named accounts, shared accounts, service accounts, break-glass accounts
- All privileged access to systems: Windows, Linux, databases, network devices, cloud platforms
- Privileged Access Management (PAM) solutions

**Information Access Restriction (A.8.3)**:
- Operating system permissions (Windows, Linux, macOS)
- Database access controls
- Application-level access controls
- API access controls
- Cloud resource access controls (AWS, Azure, GCP)
- Encryption-based access restriction

### 3.2 Technology-Agnostic Approach

This framework is **completely generic** and applicable to ANY organization, regardless of:

**Authentication Infrastructure**:
- Microsoft Active Directory
- Azure Active Directory (Entra ID)
- Okta
- Google Workspace
- Auth0
- Custom identity solutions

**PAM Solutions**:
- CyberArk
- BeyondTrust
- Delinea (Thycotic)
- One Identity Safeguard
- Azure Privileged Identity Management (PIM)
- AWS Systems Manager Session Manager
- HashiCorp Vault
- Native OS controls (sudo, runas with logging)

**Platform Coverage**:
- On-premises systems (Windows servers, Linux servers, network devices, databases)
- Cloud platforms (AWS, Azure, GCP, other cloud providers)
- Hybrid environments
- SaaS applications

**Implementation Approach**:
- [Organization] selects authentication and PAM technologies based on requirements
- This framework defines WHAT to achieve (security objectives)
- Implementation guides (S1-S5) provide HOW to achieve it (platform-specific examples)

---

## 4. Regulatory and Compliance Framework

Per ISMS-POL-00 (Regulatory Applicability Framework), this control implements requirements from:

### 4.1 Mandatory Compliance (Tier 1)

**Swiss Federal Act on Data Protection (FADP) - Article 8**:
- Technical and organizational measures for data security
- Authentication and access controls are fundamental security measures
- Applies to: ALL organizations processing personal data in Switzerland

**EU General Data Protection Regulation (GDPR) - Article 32**:
- Security of processing requires appropriate technical measures
- Authentication, authorization, and access logging explicitly mentioned
- Applies to: Organizations processing EU personal data

**ISO/IEC 27001:2022**:
- Control A.8.5: Secure Authentication (mandatory)
- Control A.8.2: Privileged Access Rights (mandatory)
- Control A.8.3: Information Access Restriction (mandatory)
- Applies to: Organizations with ISO 27001 certification

### 4.2 Conditional Compliance (Tier 2)

**NIS2 Directive (EU Network and Information Security Directive 2)**:

**CRITICAL REQUIREMENT - Article 21(2)(e)**:
> "Policies and procedures to assess the effectiveness of cybersecurity risk-management measures, including **the use of multi-factor authentication**"

**NIS2 explicitly MANDATES multi-factor authentication** - this is NOT optional for essential/important entities.

**Other NIS2 Requirements**:
- Article 21(2)(d): Access control policies and implementation
- Article 21(2)(f): Identity and access management practices
- Privileged access monitoring and logging

**Determination**: Applies if organization is classified as essential or important entity under NIS2
- Critical infrastructure (energy, transport, banking, healthcare, digital infrastructure)
- Important entities in specific sectors

**FINMA (Swiss Financial Market Supervisory Authority)**:

If organization holds FINMA license:

**FINMA Circular 2023/1** (Operational risks and resilience - banks):
- Margin 56: Authentication mechanisms for critical systems
- Margin 63-72: Logging and monitoring requirements
- Multi-factor authentication for access to critical systems
- Privileged user management and monitoring
- Strong authentication mechanisms aligned with risk
- Privileged access logging and alerting
- Session recording for privileged access (where proportionate)

**Determination**: Applies if organization is:
- Bank
- Securities dealer
- Insurance company
- Fund management company
- Other FINMA-regulated entity

**DORA (Digital Operational Resilience Act)**:

If organization is EU financial entity:
- Article 6: ICT risk management includes access control and authentication
- Article 9(3): Strong authentication mechanisms required
- Article 10: Privileged access monitoring and logging

**Determination**: Applies to EU financial entities (banks, payment institutions, investment firms, insurers)

### 4.3 Informational Reference / Best Practice Alignment (Tier 3)

**NIST SP 800-63** (Digital Identity Guidelines):
- SP 800-63A: Enrollment and Identity Proofing
- SP 800-63B: Authentication and Lifecycle Management (AAL1, AAL2, AAL3)
- SP 800-63C: Federation and Assertions
- **Authoritative reference** for authentication best practices

**NIST SP 800-53** (Security and Privacy Controls):
- IA-2: Identification and Authentication (Organizational Users)
- IA-2(1): Multi-Factor Authentication (Privileged Accounts)
- IA-2(2): Multi-Factor Authentication (Non-Privileged Accounts)
- AC-6: Least Privilege
- AC-6(2): Privileged Access for Non-Security Functions

**CIS Controls**:
- CIS Control 6: Access Control Management
  - 6.3: Require MFA for Externally-Exposed Applications
  - 6.5: Require MFA for Administrative Access

**OWASP**:
- OWASP Top 10: A07:2021 - Identification and Authentication Failures
- Common authentication vulnerabilities and mitigations

**United States Federal Requirements**:

References to US federal frameworks (FISMA, NIST cybersecurity requirements) apply ONLY where the organization has explicit US federal contractual obligations, as defined in ISMS-POL-00.

### 4.4 Key Regulatory Takeaways

**For Most Organizations**:
- FADP + ISO 27001 = MFA strongly recommended, privileged access controls mandatory
- Best practice alignment (NIST, CIS) drives MFA deployment

**For NIS2-Covered Entities (Essential/Important)**:
- **MFA is MANDATORY per Article 21(2)(e)** - not optional, not recommended
- Privileged access monitoring required
- Non-compliance = penalties up to â‚¬10M or 2% of global turnover

**For FINMA-Regulated Entities**:
- MFA for critical systems required
- Privileged access management and monitoring mandatory
- Session recording expected for high-risk access

**For DORA-Covered Financial Entities**:
- Strong authentication mechanisms mandatory
- Privileged access monitoring and logging required

---

## 5. Framework Structure Overview

This Authentication & Privileged Access Security Framework consists of:

**Policy Layer (10_pol-md/)**:
- **S1** (this document): Executive summary, control alignment, scope
- **S2**: Secure Authentication Requirements (A.8.5) - MFA, passwords, SSO, protocols
- **S3**: Privileged Access Requirements (A.8.2) - PAM, admin tiering, monitoring
- **S4**: Information Access Restriction Requirements (A.8.3) - Technical access controls
- **S5**: Assessment Methodology and Evidence Framework (cross-cutting)

**Implementation Layer (30_imp-md/)**:
- **IMP-S1**: Authentication Implementation (SSO, MFA, password policies)
- **IMP-S2**: MFA Deployment (enrollment, rollout, monitoring)
- **IMP-S3**: PAM Implementation (vaulting, JIT, session recording, admin tiering)
- **IMP-S4**: Technical Access Enforcement (file/DB/app/API permissions)
- **IMP-S5**: Security Assessment and Monitoring

**Assessment Layer (50_scripts-excel/)**:
- **Workbook 1**: Authentication Inventory & Methods (A.8.5)
- **Workbook 2**: MFA Coverage Assessment (A.8.5)
- **Workbook 3**: Privileged Account Inventory (A.8.2)
- **Workbook 4**: Privileged Access Monitoring (A.8.2)
- **Workbook 5**: Access Restriction Compliance (A.8.3)
- **Dashboard**: Consolidated authentication & PAM security overview

---

## 6. Document Navigation Guide

**For Different Audiences**:

**Security Team**:
- Start: S1 (this document) â†’ S5 (Assessment Framework) â†’ Workbooks

**IAM Team**:
- Start: S1 â†’ S2 (Authentication) â†’ IMP-S1 (Auth Implementation) â†’ IMP-S2 (MFA Deployment)

**Systems Administrators**:
- Start: S1 â†’ S3 (Privileged Access) â†’ IMP-S3 (PAM Implementation)
- Critical: Admin Tiering Model (S3, IMP-S3) - prevents lateral movement

**Application Owners**:
- Start: S1 â†’ S4 (Access Restriction) â†’ IMP-S4 (Access Enforcement)

**Auditors**:
- Start: S1 â†’ S5 (Assessment Framework) â†’ Workbooks for evidence
- Statement of Applicability (SoA) mappings in each requirements section

**Management**:
- Start: S1 (Executive Summary) â†’ Dashboard â†’ S5 (Compliance Scoring)

---

## 7. Statement of Applicability (SoA) Mapping

For ISO 27001:2022 Statement of Applicability:

### A.8.5 - Secure Authentication
**Status**: âœ“ Applicable  
**Justification**: [Organization] operates authentication infrastructure for user access to systems and applications, requiring secure authentication mechanisms aligned with modern threats.  
**Implementation**: See ISMS-POL-A.8.2-3-5-S2 (Secure Authentication Requirements)  
**Evidence**: 
- MFA enrollment data (Workbook 2)
- Authentication mechanism inventory (Workbook 1)
- Password policy configurations
- Authentication logs
- SSO integration status

### A.8.2 - Privileged Access Rights
**Status**: âœ“ Applicable  
**Justification**: [Organization] has privileged accounts (administrators, DBAs, security admins) requiring restricted allocation, management, and monitoring to prevent misuse.  
**Implementation**: See ISMS-POL-A.8.2-3-5-S3 (Privileged Access Requirements)  
**Evidence**:
- Privileged account inventory (Workbook 3)
- PAM solution deployment status
- Privileged access monitoring logs (Workbook 4)
- Session recordings
- Admin tier isolation compliance assessment
- Privileged access review records

### A.8.3 - Information Access Restriction
**Status**: âœ“ Applicable  
**Justification**: [Organization] processes information with different sensitivity levels requiring technical access controls (file permissions, database grants, API scopes) to enforce access policy.  
**Implementation**: See ISMS-POL-A.8.2-3-5-S4 (Information Access Restriction Requirements)  
**Evidence**:
- Permission audit results (Workbook 5)
- Configuration compliance scans
- Penetration test reports
- Data classification and encryption status
- Access control effectiveness testing

---

**END OF SECTION 1 (EXECUTIVE SUMMARY & CONTROL ALIGNMENT)**

**Next Section**: ISMS-POL-A.8.2-3-5-S2 (Secure Authentication Requirements - A.8.5)

---

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial authentication & privileged access framework - executive summary |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**
---


**Document ID**: ISMS-POL-A.8.2-3-5-S2  
**Title**: Secure Authentication Requirements (ISO/IEC 27001:2022 Control A.8.5)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | IAM Security Lead | Initial secure authentication requirements (A.8.5) |

**Review Cycle**: Annual (aligned with authentication infrastructure changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Identity & Access Management Lead
- Operational Review: IT Operations Manager

**Distribution**: IAM team, security team, IT operations, application owners, auditors  
**Related Documents**: 
- ISMS-POL-A.8.2-3-5-S1 (Executive Summary)
- ISMS-IMP-A.8.2-3-5-S1 (Authentication Implementation)
- ISMS-IMP-A.8.2-3-5-S2 (MFA Deployment)

---

## 1. Control Objective and Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.5

**Official Control Text**:

> *Secure authentication technologies and procedures should be implemented based on information access restrictions and the topic-specific policy on access control.*

**Control Purpose**: Ensure users prove their identity using secure mechanisms appropriate to the sensitivity of information and systems being accessed, with stronger authentication for privileged access and sensitive data.

**Why This Matters**:

Authentication is the **gateway to all systems**. Every security control depends on knowing WHO is accessing systems. Weak authentication means:

- **81% of breaches involve stolen credentials** (Verizon DBIR)
- **Password-only authentication** is trivially compromised (phishing, credential stuffing, brute force)
- **Shared credentials** eliminate accountability (cannot determine who did what)
- **Weak passwords** are cracked instantly (password123, Summer2024!)

Strong authentication provides:
- **99.9% reduction in account compromise** with MFA (Microsoft Security)
- **Phishing resistance** with FIDO2 hardware tokens
- **User convenience** with Single Sign-On (SSO)
- **Audit trail** of authentication events

### 1.2 Scope of A.8.5 Requirements

This section defines mandatory requirements for:

1. **Authentication Mechanism Requirements** - Supported authentication methods
2. **Multi-Factor Authentication (MFA) Requirements** - MFA coverage and deployment
3. **Password Policy Requirements** - Password complexity, expiration, strength
4. **Single Sign-On (SSO) Requirements** - SSO deployment and integration
5. **Authentication Protocols** - SAML, OAuth, OpenID Connect, Kerberos, RADIUS
6. **Certificate-Based Authentication** - PKI for systems and services
7. **Biometric Authentication** - Fingerprint, facial recognition requirements
8. **Authentication Logging** - Authentication event logging and monitoring
9. **Credential Compromise Response** - Detection and response procedures

---

## 2. Authentication Mechanism Requirements

### 2.1 Requirement: Supported Authentication Methods

**REQ-A85-001**: [Organization] **MUST** support multiple authentication mechanisms appropriate to use cases.

**Supported Authentication Methods**:

| Method | Use Case | Security Level | Deployment Status |
|--------|----------|----------------|-------------------|
| **Password + MFA** | Standard user access | High | Mandatory for all users |
| **Single Sign-On (SSO)** | Application access | High (with MFA) | Deploy for all SaaS/web apps |
| **Certificate-based** | System-to-system, API | Very High | Deploy for APIs and services |
| **Biometric** | Mobile devices, physical access | High (with liveness detection) | Optional, user choice |
| **Hardware tokens** | High-security access | Very High | Deploy for Tier 0 admins |

**Authentication Method Selection Criteria**:

1. **User Type**:
   - **Standard users**: Password + MFA (authenticator app or push)
   - **Privileged users**: Password + MFA (hardware token preferred) + session recording
   - **Remote users**: VPN with MFA mandatory
   - **Contractors/vendors**: Time-limited access, MFA required

2. **System Criticality**:
   - **Critical systems** (Tier 0): Hardware MFA tokens (FIDO2) required
   - **High criticality** (Tier 1): MFA mandatory (authenticator app minimum)
   - **Medium criticality** (Tier 2): MFA recommended
   - **Low criticality**: Password acceptable (internal non-sensitive systems)

3. **Data Sensitivity**:
   - **Restricted data access**: MFA + certificate-based authentication
   - **Confidential data access**: MFA mandatory
   - **Internal data access**: MFA recommended
   - **Public data access**: Password acceptable

**Technology-Agnostic Approach**:

[Organization] may use any of the following authentication platforms:
- Microsoft Active Directory (on-premises)
- Azure Active Directory / Microsoft Entra ID (cloud)
- Okta
- Google Workspace
- Auth0
- Other enterprise identity providers

Requirements apply regardless of platform choice.

**Audit Evidence**: Authentication mechanism inventory, platform documentation

---

## 3. Multi-Factor Authentication (MFA) Requirements

### 3.1 Requirement: MFA Coverage Requirements

**REQ-A85-002**: [Organization] **MUST** deploy multi-factor authentication (MFA) according to coverage requirements.

**MFA Coverage Tiers**:

**Tier 1 - MANDATORY MFA (Non-negotiable)**:
- âœ… **ALL privileged users** (system admins, DBAs, security admins, cloud admins)
- âœ… **ALL remote access** (VPN, external access)
- âœ… **ALL access to restricted/confidential data**
- âœ… **ALL access to financial systems**
- âœ… **ALL access to production environments**
- âœ… **NIS2 compliance**: Essential/important entities MUST have MFA per Article 21(2)(e)

**Tier 2 - RECOMMENDED MFA (Strong recommendation)**:
- âš ï¸ **ALL standard users** (phishing protection for everyone)
- âš ï¸ **ALL SaaS application access** (Office 365, Salesforce, etc.)
- âš ï¸ **ALL cloud platform access** (AWS, Azure, GCP consoles)

**Tier 3 - OPTIONAL MFA**:
- â„¹ï¸ **Internal-only, non-sensitive systems** (MFA not required but available)
- â„¹ï¸ **Service accounts** (use certificate-based authentication instead)

**Target MFA Coverage Metrics**:
- **Privileged users with MFA**: 100% (mandatory)
- **Remote access users with MFA**: 100% (mandatory)
- **Standard users with MFA**: Target 95%+ within 12 months
- **Overall MFA coverage**: Target 90%+ within 24 months

**Audit Evidence**: MFA enrollment data (Workbook 2), coverage metrics by user type

### 3.2 Requirement: MFA Methods Supported

**REQ-A85-003**: [Organization] **MUST** support multiple MFA methods with varying security levels.

**Supported MFA Methods** (ranked by security level):

1. **Hardware Tokens (FIDO2, YubiKey)** - HIGHEST SECURITY
   - **Security**: Phishing-resistant, cryptographic authentication
   - **Use case**: Tier 0 administrators, high-value accounts, executives
   - **Platforms**: Works with Azure AD, Okta, Google Workspace, web applications
   - **Cost**: ~$50 per token, one-time expense
   - **User experience**: Excellent (tap token)

2. **Authenticator Apps (TOTP)** - HIGH SECURITY
   - **Security**: Time-based one-time passwords, offline capable
   - **Use case**: Standard users, privileged users (if hardware tokens unavailable)
   - **Platforms**: Microsoft Authenticator, Google Authenticator, Authy, Duo Mobile
   - **Cost**: Free
   - **User experience**: Good (type 6-digit code or approve push)

3. **Push Notifications** - HIGH SECURITY
   - **Security**: Real-time approval, user confirms authentication attempt
   - **Use case**: Standard users, convenient for frequent logins
   - **Platforms**: Microsoft Authenticator, Okta Verify, Duo Mobile
   - **Cost**: Free (requires internet connection)
   - **User experience**: Excellent (tap "Approve")
   - **Risk**: Vulnerable to MFA fatigue attacks (approve notification without checking)

4. **Biometric Authentication** - MEDIUM-HIGH SECURITY
   - **Security**: Fingerprint, facial recognition (with liveness detection)
   - **Use case**: Mobile devices, physical access
   - **Platforms**: Windows Hello, Face ID, Touch ID
   - **Cost**: Free (if device supports)
   - **User experience**: Excellent
   - **Risk**: Biometric data compromise is permanent (cannot change fingerprint)

5. **SMS/Voice** - LOW SECURITY (DISCOURAGED)
   - **Security**: Vulnerable to SIM swapping, interception
   - **Use case**: ONLY as last-resort backup method
   - **Status**: **Discouraged** - do not use as primary MFA
   - **Rationale**: NIST SP 800-63B discourages SMS due to vulnerabilities

**MFA Method Selection Guidelines**:
- **Tier 0 administrators**: Hardware tokens (FIDO2) required
- **Privileged users**: Authenticator app minimum, hardware token recommended
- **Standard users**: Authenticator app or push notifications
- **Mobile-only users**: Platform biometrics (Windows Hello, Face ID) acceptable
- **Backup MFA method**: Required for all users (in case primary method unavailable)

**Prohibited MFA Methods**:
- âŒ SMS as primary MFA method (only allowed as backup)
- âŒ Email-based OTP (email compromise = MFA bypass)
- âŒ Single-factor authentication for privileged access

**Audit Evidence**: MFA method inventory, user enrollment by method type

### 3.3 Requirement: MFA Enrollment Procedures

**REQ-A85-004**: MFA enrollment **MUST** be mandatory with defined timelines and verification.

**Mandatory Enrollment Requirements**:

1. **Privileged Users**:
   - **Enrollment deadline**: Within 7 days of privileged access grant
   - **Verification**: IT Security team verifies enrollment before activating privileged access
   - **Non-compliance**: Privileged access revoked if MFA not enrolled

2. **Remote Access Users**:
   - **Enrollment deadline**: Before VPN access granted
   - **Verification**: VPN access requires MFA enrollment first
   - **Non-compliance**: VPN access denied until MFA enrolled

3. **Standard Users**:
   - **Enrollment deadline**: Phased rollout over 12 months
   - **Verification**: Self-service enrollment, IT support available
   - **Non-compliance**: Escalation to management, eventual account restriction

**Enrollment Procedures**:

1. **User receives enrollment notification** (email with instructions)
2. **User installs authenticator app** (Microsoft Authenticator, Google Authenticator, etc.)
3. **User scans QR code** or enters setup key to register account
4. **User verifies MFA works** by authenticating once
5. **User registers backup MFA method** (second device or backup codes)
6. **System confirms enrollment** (user added to "MFA Enrolled" group)

**Backup MFA Method Registration**:
- **Required**: All users must register backup method
- **Options**: Second authenticator device, hardware token, backup codes
- **Purpose**: Prevent lockout if primary MFA device lost/stolen

**Audit Evidence**: MFA enrollment logs, enrollment completion rates, verification records

### 3.4 Requirement: MFA Recovery Procedures

**REQ-A85-005**: MFA recovery procedures **MUST** balance security with usability.

**MFA Recovery Scenarios**:

1. **Lost MFA Device** (phone lost/stolen):
   - User contacts IT support helpdesk
   - Identity verification required (employee ID, manager confirmation, security questions)
   - IT admin resets MFA registration
   - User re-enrolls MFA immediately (temporary access may be granted)

2. **Broken MFA Device** (phone damaged, app not working):
   - User uses backup MFA method (if registered)
   - If no backup: Same process as lost device

3. **MFA App Accidentally Deleted**:
   - User re-installs app
   - Uses backup codes or backup device to authenticate
   - Re-registers primary device if needed

**MFA Reset Verification Requirements**:
- **Identity proofing**: Multi-factor identity verification before MFA reset
  - Employee ID + manager email confirmation
  - OR in-person verification with ID badge
  - OR security questions + callback to registered phone number
- **Audit logging**: All MFA resets logged and reviewed monthly
- **Alert on suspicious resets**: Multiple reset attempts trigger security review

**Break-Glass MFA Bypass**:
- **Emergency accounts** (break-glass) may bypass MFA temporarily
- **Requires**: Executive approval (CISO or CIO)
- **Triggers**: Critical incident, all MFA methods unavailable
- **Audit**: Full investigation after use, re-enable MFA immediately

**Audit Evidence**: MFA reset logs, identity verification records, break-glass usage logs

---

## 4. Password Policy Requirements

### 4.1 Requirement: Password Complexity and Length

**REQ-A85-006**: Password policies **MUST** follow modern best practices emphasizing length over complexity.

**Modern Password Policy** (aligned with NIST SP 800-63B):

**Password Length** (MOST IMPORTANT):
- **Minimum length**: 12 characters (passwords)
- **Recommended length**: 15+ characters (passphrases)
- **Rationale**: Length provides far more entropy than complexity rules
  - 12-character password = 10^14 combinations (with basic complexity)
  - 15-character passphrase = 10^18 combinations

**Password Complexity** (LESS IMPORTANT):
- **Required**: At least 3 of 4 character types:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*)
- **Rationale**: Some complexity reduces dictionary attacks, but length matters more

**Passphrase Encouragement**:
- **Example**: "CoffeeTable!Morning92" (22 chars, easy to remember, very strong)
- **Better than**: "P@ssw0rd!" (9 chars, meets complexity, but weak)

**Password Strength Validation**:
- **Dictionary word detection**: Reject common passwords (password, 123456, qwerty, etc.)
- **Breach detection**: Check against known breached password lists (Have I Been Pwned API)
- **Sequential/repeated character detection**: Reject passwords like "aaaabbbb" or "12345678"

**Modern Best Practice Changes**:
- âœ… **Favor length over complexity** (15-char simple phrase beats 8-char complex password)
- âœ… **Allow spaces in passwords** (enables passphrases: "my dog has fleas 2024")
- âœ… **Allow copy-paste** (encourages password manager use)
- âŒ **No forced complexity** if password is 15+ characters
- âŒ **No character substitution requirements** (P@ssw0rd patterns are well-known to attackers)

**Audit Evidence**: Password policy configuration, password strength distribution analysis

### 4.2 Requirement: Password Expiration

**REQ-A85-007**: Password expiration **SHOULD** be disabled unless specific risk requires it.

**Modern Guidance on Password Expiration**:

**NIST SP 800-63B (2020)** recommends:
- **NO forced periodic password expiration** unless compromise suspected
- **Rationale**: Forced expiration leads to weaker passwords (Password1, Password2, Password3)
- **Better approach**: Continuous monitoring for compromised credentials

**[Organization] Password Expiration Policy**:

**Default: NO PASSWORD EXPIRATION**
- **Applies to**: Standard user accounts with MFA enabled
- **Rationale**: MFA provides strong security, forced expiration degrades password quality
- **Monitoring**: Passwords checked against breach databases continuously

**Exceptions Requiring Password Expiration**:

1. **Accounts WITHOUT MFA** (if any exist):
   - **Expiration**: 90 days
   - **Rationale**: Password-only access needs rotation as compensating control
   - **Goal**: Eliminate password-only access, then remove expiration

2. **Shared/Service Accounts**:
   - **Expiration**: 90 days (or automated rotation via PAM)
   - **Rationale**: Shared credentials have higher compromise risk

3. **Privileged Accounts in PAM Vault**:
   - **Rotation**: Automatic after each use (PAM-managed)
   - **Alternative**: JIT access with temporary passwords

4. **Suspected Compromise**:
   - **Immediate**: Force password reset if compromise suspected
   - **Notification**: User notified of security concern

**Audit Evidence**: Password expiration settings, accounts with/without MFA, password age distribution

### 4.3 Requirement: Password History and Reuse Prevention

**REQ-A85-008**: Password history **MUST** prevent reuse of recent passwords.

**Password History Requirements**:
- **History length**: Remember last 5 passwords
- **Reuse prevention**: Cannot reuse any of last 5 passwords
- **Rationale**: Prevents cycling through Password1, Password2, Password3
- **Exception**: Emergency password resets (if absolutely necessary, log and review)

**Audit Evidence**: Password history configuration, password reuse attempt logs

### 4.4 Requirement: Password Breach Detection

**REQ-A85-009**: Passwords **MUST** be checked against known breached password databases.

**Breach Detection Implementation**:

1. **At Password Creation/Change**:
   - Check password against Have I Been Pwned API (pwned passwords)
   - Reject password if found in breach database
   - User notification: "This password has been compromised in a data breach - please choose a different password"

2. **Continuous Monitoring**:
   - **Azure AD Password Protection**: Continuously monitors and alerts on compromised passwords
   - **Okta Compromised Credential Detection**: Automatically detects known breached credentials
   - **Force reset**: If user's password found in new breach, force immediate reset

**Breach Detection Platforms**:
- **Azure AD Password Protection**: Built-in for Azure AD
- **Okta Compromised Credential Detection**: Built-in for Okta
- **Have I Been Pwned API**: Can be integrated into custom authentication systems
- **Enzoic**: Commercial breach detection service

**Audit Evidence**: Breach detection configuration, compromised password detection logs, forced resets

---

## 5. Single Sign-On (SSO) Requirements

### 5.1 Requirement: SSO Deployment

**REQ-A85-010**: Single Sign-On (SSO) **MUST** be deployed for all supported applications.

**SSO Benefits**:
- **Reduced password fatigue**: Users remember one strong password instead of dozens
- **Improved security**: Centralized authentication with MFA
- **Better user experience**: Seamless access to applications
- **Centralized logging**: All authentication events in one place
- **Faster onboarding/offboarding**: Disable one account = disable all access

**SSO Coverage Requirements**:

**Tier 1 - Mandatory SSO**:
- âœ… All SaaS applications (Office 365, Salesforce, Slack, etc.)
- âœ… All web-based applications (internal portals, intranet)
- âœ… All cloud platform consoles (AWS, Azure, GCP management consoles)

**Tier 2 - Recommended SSO**:
- âš ï¸ Legacy applications (if technically feasible)
- âš ï¸ On-premises applications (if SAML/OAuth support available)

**Tier 3 - Excluded from SSO**:
- â„¹ï¸ Applications without SSO support (document exception)
- â„¹ï¸ Air-gapped systems (no network connection)
- â„¹ï¸ Infrastructure devices (use device-specific authentication)

**SSO Adoption Metrics**:
- **Applications with SSO**: Target 90%+ of SaaS applications
- **Users accessing apps via SSO**: Target 95%+ of authentication events

**Audit Evidence**: SSO integration status (Workbook 1), application inventory with SSO status

### 5.2 Requirement: SSO Platform Requirements

**REQ-A85-011**: SSO platform **MUST** support modern authentication protocols and MFA integration.

**Required SSO Capabilities**:

1. **Protocol Support**:
   - **SAML 2.0**: Enterprise SSO (preferred for SaaS applications)
   - **OAuth 2.0 / OpenID Connect (OIDC)**: Modern authentication (preferred for APIs)
   - **WS-Federation**: Legacy enterprise SSO (if needed for older apps)

2. **MFA Integration**:
   - Native MFA support (built into SSO platform)
   - MFA prompt during SSO authentication
   - Adaptive authentication (risk-based MFA prompts)

3. **Application Catalog**:
   - Pre-built integrations for common SaaS apps (Office 365, Salesforce, etc.)
   - Custom app integration support (SAML/OAuth configuration)
   - Application gallery with 1000+ pre-configured integrations

4. **User Provisioning (SCIM)**:
   - Automatic user account creation in applications (via SCIM protocol)
   - User attribute synchronization (email, name, department, etc.)
   - Automatic deprovisioning when user leaves organization

5. **Session Management**:
   - Configurable session timeout
   - Global logout capability (logout from SSO = logout from all apps)
   - Session monitoring and analytics

**SSO Platform Options** (technology-agnostic):
- Azure Active Directory (Microsoft Entra ID)
- Okta
- Google Workspace
- Auth0
- Ping Identity
- ForgeRock

**Audit Evidence**: SSO platform capabilities documentation, protocol support matrix

### 5.3 Requirement: SSO Session Management

**REQ-A85-012**: SSO sessions **MUST** have appropriate timeout and logout procedures.

**Session Timeout Requirements**:

| Access Type | Idle Timeout | Max Session Duration | Rationale |
|-------------|--------------|---------------------|-----------|
| **Standard users** | 8 hours | 12 hours | Balance security and usability |
| **Privileged users** | 1 hour | 4 hours | Higher risk requires shorter sessions |
| **Sensitive data access** | 30 minutes | 2 hours | Extra protection for confidential data |
| **Public workstations** | 15 minutes | 1 hour | Shared computer risk |

**Session Security**:
- **Session tokens**: Cryptographically secure, random
- **Token storage**: HTTP-only, secure cookies (no JavaScript access)
- **Token revocation**: Immediate logout revokes all application sessions
- **Session hijacking protection**: Bind session to IP address and user agent

**Global Logout**:
- **User-initiated logout**: Logout from SSO portal logs out from all applications
- **Admin-initiated logout**: IT can force logout for user (security incident response)
- **Automatic logout**: After max session duration reached

**Audit Evidence**: Session timeout configuration, global logout functionality, session logs

---

## 6. Authentication Protocols and Standards

### 6.1 Requirement: Supported Authentication Protocols

**REQ-A85-013**: [Organization] **MUST** support modern authentication protocols and deprecate insecure legacy protocols.

**Supported Authentication Protocols**:

1. **SAML 2.0** (Security Assertion Markup Language):
   - **Use case**: Enterprise SSO for web applications
   - **Common for**: SaaS applications (Salesforce, ServiceNow, etc.)
   - **Security**: Strong (XML signatures, assertions)
   - **Status**: âœ… Supported, widely deployed

2. **OAuth 2.0** (Authorization Framework):
   - **Use case**: API authorization (delegated access)
   - **Common for**: Mobile apps, APIs, third-party integrations
   - **Security**: Strong (token-based, scoped access)
   - **Status**: âœ… Supported, preferred for APIs

3. **OpenID Connect (OIDC)** (built on OAuth 2.0):
   - **Use case**: Modern authentication and SSO
   - **Common for**: Web applications, mobile apps
   - **Security**: Strong (JWT tokens, identity layer on OAuth)
   - **Status**: âœ… Supported, preferred for new applications

4. **Kerberos**:
   - **Use case**: On-premises Active Directory authentication
   - **Common for**: Windows domain environments
   - **Security**: Strong (encrypted tickets)
   - **Status**: âœ… Supported for on-premises AD

5. **RADIUS** (Remote Authentication Dial-In User Service):
   - **Use case**: Network device authentication (802.1X, VPN)
   - **Common for**: Wireless networks, network equipment
   - **Security**: Moderate (shared secret-based, can be strengthened with EAP-TLS)
   - **Status**: âœ… Supported for network authentication

6. **LDAP/LDAPS** (Lightweight Directory Access Protocol):
   - **Use case**: Directory authentication queries
   - **Common for**: Legacy applications, directory lookups
   - **Security**: LDAP weak (plaintext), LDAPS strong (TLS-encrypted)
   - **Status**: âš ï¸ LDAPS supported, plaintext LDAP deprecated

**Deprecated/Prohibited Protocols**:
- âŒ **Basic Authentication (HTTP Basic Auth)**: Credentials in Base64 (not encrypted)
- âŒ **NTLM** (NT LAN Manager): Legacy Windows authentication (Kerberos preferred)
- âŒ **Plaintext LDAP**: Credentials sent unencrypted

**Audit Evidence**: Protocol usage logs, legacy protocol deprecation status

### 6.2 Requirement: Secure Protocol Configuration

**REQ-A85-014**: Authentication protocols **MUST** be configured securely.

**SAML Configuration Requirements**:
- **Signature validation**: Always validate SAML assertions signatures
- **Certificate expiration monitoring**: Alert 30 days before certificate expires
- **Secure bindings**: Use HTTP-POST binding (avoid HTTP-Redirect for sensitive data)

**OAuth 2.0 / OIDC Configuration Requirements**:
- **PKCE required**: Use Proof Key for Code Exchange (PKCE) for public clients
- **State parameter**: Always use state parameter (CSRF protection)
- **Token encryption**: Store tokens securely (encrypted storage)
- **Scope limitation**: Grant minimum necessary OAuth scopes

**Kerberos Configuration Requirements**:
- **Encryption types**: Use AES256 or AES128 (disable DES, RC4)
- **Ticket lifetime**: Max 10 hours
- **Clock skew**: Max 5 minutes (time sync critical)

**RADIUS Configuration Requirements**:
- **Shared secret strength**: 32+ character random string
- **EAP methods**: Use EAP-TLS (certificate-based) or PEAP-MSCHAPv2
- **Avoid**: PAP, CHAP (weak authentication)

**Audit Evidence**: Protocol configuration audits, security settings documentation

---

## 7. Certificate-Based Authentication

### 7.1 Requirement: PKI for System-to-System Authentication

**REQ-A85-015**: Certificate-based authentication **MUST** be used for system-to-system and API authentication.

**Certificate Authentication Use Cases**:

1. **API Authentication**:
   - Client certificates for API access (mutual TLS)
   - Stronger than API keys (cryptographic authentication)
   - Use case: High-security APIs, financial transactions

2. **Service-to-Service Authentication**:
   - Certificates for service accounts (no passwords)
   - Automated certificate rotation
   - Use case: Microservices, cloud-native applications

3. **Device Authentication**:
   - Certificates for devices accessing network (802.1X with EAP-TLS)
   - Device identity tied to certificate (not password)
   - Use case: Corporate laptops, IoT devices

4. **VPN Authentication**:
   - Certificate-based VPN (in addition to username/password + MFA)
   - Device trust validation
   - Use case: Remote access VPN

**PKI Requirements**:
- **Certificate Authority (CA)**: Internal CA or trusted third-party CA
- **Certificate lifecycle**: Issuance, renewal (30 days before expiry), revocation (CRL/OCSP)
- **Key length**: RSA 2048-bit minimum, RSA 4096-bit or ECC P-256 recommended
- **Certificate validity**: Max 2 years (13 months for public trust)

**Audit Evidence**: Certificate inventory, certificate expiration monitoring, PKI documentation

### 7.2 Requirement: Certificate Management

**REQ-A85-016**: Certificates **MUST** be managed through defined lifecycle procedures.

**Certificate Lifecycle**:

1. **Issuance**:
   - Certificate requests approved by designated authority
   - Certificate subject matches intended use (CN, SAN fields)
   - Private key generated securely (on device, never transmitted)

2. **Renewal**:
   - Automated renewal 30 days before expiration
   - Alert if renewal fails
   - Monitor certificate inventory for approaching expiration

3. **Revocation**:
   - Revoke certificate immediately if:
     - Private key compromised
     - System decommissioned
     - Certificate misused
   - CRL (Certificate Revocation List) or OCSP (Online Certificate Status Protocol) published

4. **Storage**:
   - Private keys stored securely (hardware security module or encrypted storage)
   - Never store private keys in code repositories or configuration files
   - Access to private keys restricted to authorized systems/personnel

**Audit Evidence**: Certificate inventory with expiration dates, renewal logs, revocation logs

---

## 8. Biometric Authentication

### 8.1 Requirement: Biometric Authentication Standards

**REQ-A85-017**: Biometric authentication **MAY** be used with appropriate security controls.

**Supported Biometric Methods**:

1. **Fingerprint Recognition**:
   - **Devices**: Touch ID (Apple), Windows Hello (fingerprint)
   - **Use case**: Mobile device unlock, workstation login
   - **Security**: Liveness detection required (reject photos, molds)

2. **Facial Recognition**:
   - **Devices**: Face ID (Apple), Windows Hello (facial)
   - **Use case**: Mobile device unlock, workstation login
   - **Security**: 3D depth sensing required (reject photos)

3. **Iris/Retinal Scanning**:
   - **Devices**: Specialized readers
   - **Use case**: Physical access control
   - **Security**: Very high accuracy

**Biometric Security Requirements**:

1. **Liveness Detection**: MANDATORY
   - Detect and reject spoofing attempts (photos, videos, masks)
   - Active liveness (user performs action) or passive liveness (AI detection)

2. **Biometric Template Protection**:
   - **Never store raw biometric data** (fingerprint image, face image)
   - Store only biometric templates (mathematical representation)
   - Encrypt biometric templates at rest
   - Templates stored in secure enclave (iPhone Secure Enclave, TPM)

3. **Fallback Authentication**:
   - Always provide fallback to password/PIN
   - Biometric failure does not lock user out permanently
   - Max biometric attempts: 5, then require password

4. **Privacy Considerations**:
   - Biometric enrollment is user choice (not mandatory)
   - User can delete biometric templates anytime
   - Biometric data not shared with third parties

**Biometric Use Cases**:
- âœ… **Acceptable**: Device unlock (laptop, mobile), physical access
- âš ï¸ **Caution**: High-security systems (biometrics not phishing-resistant like FIDO2)
- âŒ **Prohibited**: Biometric-only for privileged access (combine with password/token)

**Audit Evidence**: Biometric enrollment status, biometric authentication logs

---

## 9. Authentication Logging and Monitoring

### 9.1 Requirement: Authentication Event Logging

**REQ-A85-018**: All authentication events **MUST** be logged for security monitoring and forensic investigation.

**Required Authentication Logs**:

1. **Successful Authentication**:
   - Username, timestamp, source IP, user agent
   - Authentication method (password, MFA, SSO, certificate)
   - Application/system accessed

2. **Failed Authentication**:
   - Username (attempted), timestamp, source IP, user agent
   - Failure reason (invalid password, invalid MFA, account locked, etc.)
   - Number of consecutive failures

3. **MFA Events**:
   - MFA enrollment (user, timestamp, method)
   - MFA authentication (success/failure, method used)
   - MFA reset requests (user, admin, timestamp)

4. **SSO Events**:
   - SSO login (user, timestamp, source IP)
   - Application accessed via SSO (application name, timestamp)
   - SSO logout (user, timestamp, applications logged out)

5. **Account Lockout Events**:
   - Account lockout (username, timestamp, reason)
   - Account unlock (username, timestamp, admin who unlocked)

**Log Retention**:
- **Minimum retention**: 90 days online, 1 year archived
- **Extended retention**: 7 years for financial systems (regulatory requirement)
- **Compliance**: GDPR Article 5(1)(e) limits data retention (review retention period)

**Log Protection**:
- **Centralized logging**: Forward authentication logs to SIEM (Security Information and Event Management)
- **Tamper-proof**: Logs write-once (cannot be modified after creation)
- **Access control**: Only security team can access authentication logs

**Audit Evidence**: Authentication log samples, log retention configuration, SIEM integration

### 9.2 Requirement: Authentication Monitoring and Alerting

**REQ-A85-019**: Authentication events **MUST** be monitored for anomalies and security incidents.

**Critical Authentication Alerts**:

| Alert | Threshold | Priority | Response Time |
|-------|-----------|----------|---------------|
| **Brute force attack** | 10 failed logins in 5 minutes | High | 15 minutes |
| **Impossible travel** | Login from 2 locations >500km apart in <1 hour | High | 30 minutes |
| **Privileged account login** | Admin login from unusual location/time | Medium | 1 hour |
| **MFA bypass attempt** | Multiple MFA failures followed by success | High | 15 minutes |
| **Account lockout spike** | >5 accounts locked in 10 minutes | High | 15 minutes |
| **New device/location** | User login from never-before-seen device/IP | Low | 24 hours |

**Automated Responses**:
- **Account lockout**: After 5 failed password attempts (30-minute lockout)
- **IP blocking**: Block source IP after 20 failed attempts from that IP (1-hour block)
- **MFA challenge**: Require MFA for logins from new locations/devices
- **Session termination**: Terminate active sessions if account compromised

**Integration with SIEM**:
- Forward authentication logs to SIEM (A.8.16)
- Correlation with other security events (malware, network anomalies, etc.)
- Automated incident ticket creation for critical alerts

**Audit Evidence**: Alert rules configuration, alert response logs, SIEM integration documentation

---

## 10. Credential Compromise Response

### 10.1 Requirement: Compromised Credential Detection

**REQ-A85-020**: [Organization] **MUST** detect and respond to compromised credentials.

**Compromise Detection Methods**:

1. **Password Breach Detection**:
   - Continuous monitoring against Have I Been Pwned database
   - Azure AD Password Protection / Okta Compromised Credential Detection
   - Alert and force reset if user password found in breach

2. **Impossible Travel Detection**:
   - User logs in from New York, then Tokyo 1 hour later = impossible
   - Automated MFA challenge or session termination
   - Alert security team for investigation

3. **Anomalous Behavior Detection**:
   - User logs in at 3 AM (normally 9 AM - 5 PM) = suspicious
   - User accesses systems never accessed before = suspicious
   - Machine learning-based anomaly detection (Azure AD Identity Protection, Okta ThreatInsight)

4. **Dark Web Monitoring**:
   - Monitor dark web forums for [Organization] credentials
   - Third-party services (SpyCloud, Flare, Have I Been Pwned Domain Search)
   - Alert if credentials posted for sale

**Compromise Indicators**:
- âš ï¸ Password found in public breach database
- âš ï¸ Impossible travel (geographically impossible logins)
- âš ï¸ Login from Tor exit node or known proxy
- âš ï¸ Unusual time of access (outside business hours)
- âš ï¸ Unusual systems accessed (never accessed before)
- âš ï¸ Suspicious activity after authentication (data exfiltration, privilege escalation)

**Audit Evidence**: Compromise detection alerts, dark web monitoring reports

### 10.2 Requirement: Compromised Credential Response

**REQ-A85-021**: Compromised credentials **MUST** trigger immediate response procedures.

**Response Procedures**:

**Severity Level 1 - Confirmed Compromise** (Password in breach, active attacker):
1. **Immediate actions** (within 15 minutes):
   - Force password reset for affected user(s)
   - Terminate all active sessions
   - Disable account temporarily (until investigation complete)
   - Alert security team and user

2. **Investigation** (within 1 hour):
   - Review authentication logs (what was accessed?)
   - Review audit logs (what actions were performed?)
   - Determine scope of compromise (one user or multiple?)
   - Identify any data accessed or exfiltrated

3. **Remediation** (within 24 hours):
   - User enrolls new password (in person or verified identity)
   - User re-enrolls MFA (new device if old device compromised)
   - Review and revoke unnecessary access rights
   - Monitor account for 30 days for suspicious activity

4. **Lessons learned** (within 1 week):
   - Incident report documenting timeline, impact, remediation
   - Identify root cause (how was credential compromised?)
   - Implement preventive measures (MFA enforcement, user training, etc.)

**Severity Level 2 - Suspected Compromise** (Suspicious activity, no confirmation):
1. **Immediate actions** (within 1 hour):
   - Challenge user with MFA (if not already required)
   - Alert security team for monitoring
   - Flag account for enhanced logging

2. **Investigation** (within 4 hours):
   - Contact user to verify activity was legitimate
   - Review recent authentication and activity logs
   - If suspicious confirmed, escalate to Level 1 response

**Severity Level 3 - Anomaly Detection** (Unusual but possibly legitimate):
1. **Automated response**:
   - Challenge with MFA
   - Email notification to user ("Did you just log in from X location?")
   - Log event for future correlation

2. **User self-service response**:
   - User confirms legitimate or reports suspicious
   - If suspicious, user initiates password reset

**Breach Notification**:
- **Internal**: Notify affected users immediately
- **Regulatory**: Notify regulators if personal data compromised (GDPR 72-hour rule)
- **Customer**: Notify customers if customer data compromised

**Audit Evidence**: Compromise response logs, incident reports, user notifications, remediation status

---

## 11. Measurable Requirements and Audit Verification

### 11.1 Authentication Security Metrics

**Measurable requirements for audit verification**:

| Requirement | Metric | Target | Verification Method |
|-------------|--------|--------|---------------------|
| **MFA coverage - privileged** | % privileged users with MFA | 100% | Workbook 2 |
| **MFA coverage - remote access** | % remote users with MFA | 100% | VPN logs + MFA data |
| **MFA coverage - overall** | % all users with MFA | 90%+ | Workbook 2 |
| **Password strength** | % passwords meeting minimum length | 95%+ | Password policy audit |
| **Password breaches** | Passwords in breach database | 0 | Breach detection logs |
| **SSO adoption** | % apps integrated with SSO | 90%+ | Workbook 1 |
| **Legacy protocol usage** | Authentications via insecure protocols | <5% | Protocol usage logs |
| **Authentication failures** | Failed auth rate | <1% | Authentication logs |
| **MFA enrollment time** | Days to enroll MFA (privileged) | <7 days | Enrollment logs |

### 11.2 Audit Evidence Requirements

**For ISO 27001:2022 A.8.5 audit**:

1. **Policy and procedures**: This document (ISMS-POL-A.8.2-3-5-S2)
2. **Authentication inventory**: Workbook 1 (authentication mechanisms by system)
3. **MFA coverage**: Workbook 2 (MFA enrollment by user type, coverage metrics)
4. **Password policy**: Configuration screenshots, policy documentation
5. **SSO integration**: Application catalog with SSO status
6. **Authentication logs**: Sample logs showing successful/failed authentication events
7. **Breach detection**: Compromised password detection logs, forced resets
8. **Incident response**: Compromise response logs, incident reports

---

**END OF SECTION 2 (SECURE AUTHENTICATION REQUIREMENTS - A.8.5)**

**Next Section**: ISMS-POL-A.8.2-3-5-S3 (Privileged Access Requirements - A.8.2)

---

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | IAM Security Lead | Initial secure authentication requirements (A.8.5) |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**

---


**Document ID**: ISMS-POL-A.8.2-3-5-S3  
**Title**: Privileged Access Requirements (ISO/IEC 27001:2022 Control A.8.2)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architecture Lead | Initial privileged access requirements (A.8.2) |

**Review Cycle**: Annual (aligned with privileged access review cycle)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Architect
- Operational Review: Systems Administration Manager
- PAM Review: Privileged Access Management Lead

**Distribution**: Security team, systems administrators, database administrators, security administrators, cloud administrators, auditors  
**Related Documents**: 
- ISMS-POL-A.8.2-3-5-S1 (Executive Summary)
- ISMS-POL-A.8.2-3-5-S2 (Authentication Requirements - A.8.5)
- ISMS-IMP-A.8.2-3-5-S3 (PAM Implementation)

---

## 1. Control Objective and Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.2

**Official Control Text**:

> *The allocation and use of privileged access rights should be restricted and managed.*

**Control Purpose**: Ensure privileged accounts (administrators, root, elevated access) are tightly controlled, monitored, and audited to prevent misuse, detect compromise, and limit blast radius of security incidents.

**Why This Matters**:

Privileged access is the **"keys to the kingdom"**. Privileged accounts can:
- Access ANY system in the environment
- Modify ANY data (including audit logs)
- Disable ANY security control
- Create backdoor accounts for persistence
- Delete evidence of compromise

**The Privileged Access Reality**:
- **80% of security breaches involve privileged access abuse** (CyberArk)
- **Domain Admin compromise = complete organizational breach**
- **Unmonitored privileged access = attacker dwell time measured in MONTHS**
- **Shared admin passwords = zero accountability** (who did what?)

Proper privileged access controls provide:
- **Blast radius limitation** through admin tiering (Tier 0 compromise doesn't reach everything)
- **Accountability** through session recording (know exactly what admin did)
- **Credential protection** through PAM vaulting (passwords never seen by humans)
- **Temporary access** through Just-in-Time (admin rights only when needed, auto-revoked)
- **Lateral movement prevention** through tier isolation (attacker cannot hop between tiers)

### 1.2 Scope of A.8.2 Requirements

This section defines mandatory requirements for:

1. **Privileged User Identification** - Who has admin access and why
2. **Privileged Account Types** - Named, shared, service, break-glass accounts
3. **Privileged Access Management (PAM)** - Vaulting, JIT, approval workflows, session recording
4. **Privileged Account Separation** - Separate admin accounts from user accounts
5. **Admin Tiering Model** - Tier 0/1/2 isolation to prevent lateral movement
6. **MFA for Privileged Access** - Multi-factor authentication MANDATORY
7. **Privileged Access Monitoring** - Real-time monitoring and alerting
8. **Privileged Credential Rotation** - Automated password changes
9. **Privileged Access Reviews** - Quarterly verification of need

---

## 2. Privileged User Identification Requirements

### 2.1 Requirement: Definition of Privileged Access

**REQ-A82-001**: [Organization] **MUST** clearly define what constitutes privileged access.

**Privileged Access Definition**:

Privileged access is any access that allows a user to:
- Perform administrative functions (install software, change configurations)
- Access systems or data beyond normal business need
- Modify security controls (disable firewall, change permissions)
- Bypass normal access controls
- Access audit logs or security monitoring systems

**Privileged Access Types**:

1. **System Administrators**:
   - Windows Server administrators (Domain Admin, Enterprise Admin, local Administrator)
   - Linux/Unix administrators (root, sudo access)
   - Network device administrators (network routers, switches, firewalls)
   - Virtual infrastructure administrators (VMware, Hyper-V admins)

2. **Database Administrators (DBAs)**:
   - Database server administrators (SQL Server sa, Oracle SYS/SYSTEM, PostgreSQL superuser)
   - Database backup/restore privileges
   - Schema modification privileges

3. **Security Administrators**:
   - Firewall administrators
   - SIEM administrators
   - Antivirus/EDR administrators
   - PAM administrators
   - IAM administrators

4. **Cloud Administrators**:
   - Cloud global administrators (Azure Global Admin, AWS root, GCP Owner)
   - Cloud subscription/account administrators
   - Cloud resource administrators (EC2, VM management)

5. **Application Administrators**:
   - ERP administrators (SAP, Oracle EBS)
   - CRM administrators (Salesforce admin)
   - Application-specific admin roles

6. **Backup/Recovery Administrators**:
   - Backup system administrators
   - Disaster recovery administrators

**Non-Privileged Access** (for clarity):
- Standard user access to email, productivity tools
- Application users with read/write access to business data (within their role)
- End-user device local user accounts (not local admin)

**Audit Evidence**: Privileged access definition documentation, role catalog

### 2.2 Requirement: Privileged User Inventory

**REQ-A82-002**: [Organization] **MUST** maintain a complete inventory of all privileged users and accounts.

**Privileged User Inventory Requirements**:

For EACH privileged user, document:
- **User identity** (name, employee ID)
- **Privileged accounts owned** (john.admin, john.tier0, john.dba, etc.)
- **Privileged role** (Windows admin, Linux admin, DBA, security admin, cloud admin)
- **Admin tier classification** (Tier 0, Tier 1, Tier 2 - see Section 5)
- **Systems/platforms** (Windows servers, Linux servers, network devices, AWS, Azure, databases)
- **Business justification** (why does this user need privileged access?)
- **Approval date and approver** (who approved this privileged access grant?)
- **Last access review date** (quarterly reviews required)
- **MFA status** (MFA MUST be enabled for all privileged users)

**Privileged User Discovery**:
- Query Active Directory for privileged groups (Domain Admins, Enterprise Admins, Administrators)
- Query Azure AD for privileged roles (Global Administrator, Security Administrator)
- Query AWS for privileged IAM users/roles
- Query database servers for DBA accounts (sa, SYSTEM, postgres)
- Query PAM solution for vaulted accounts
- Query network devices for admin accounts

**Inventory Maintenance**:
- **Update frequency**: Monthly (detect new privileged grants)
- **Verification**: Quarterly full inventory review
- **Automation**: Automated discovery where possible (AD queries, cloud APIs)

**Audit Evidence**: Privileged user inventory (Workbook 3), discovery automation

---

## 3. Privileged Account Types and Management

### 3.1 Requirement: Named Privileged Accounts

**REQ-A82-003**: Privileged access **MUST** use named privileged accounts separate from standard user accounts.

**Named Privileged Account Principle**:

Each user requiring privileged access has **two accounts**:
1. **Standard user account**: For daily work (email, documents, web browsing)
   - Example: `john.doe`
   - Rights: Standard user, no admin rights
   - Usage: 95% of the time

2. **Privileged account**: For administrative tasks ONLY
   - Example: `john.doe.admin` or `john.admin` or `adm-john.doe`
   - Rights: Administrative access
   - Usage: 5% of the time, only when performing admin tasks
   - Requires: MFA MANDATORY

**Why Separate Accounts?**
- **Reduces attack surface**: Standard account compromise doesn't grant admin access
- **Accountability**: Clear audit trail (admin account used = administrative action)
- **Least privilege**: Users operate with minimum necessary privileges most of the time
- **Malware protection**: Malware running under standard account cannot install itself system-wide

**Account Naming Conventions**:

Standardized naming helps identification and automation:
- **Windows**: `adm-firstname.lastname` or `firstname.lastname.admin`
- **Linux**: `firstname.lastname-admin` or `root-firstname.lastname`
- **Database**: `firstname.lastname.dba`
- **Cloud**: `firstname.lastname@admin.domain.com` or `admin-firstname.lastname`

[Organization] chooses naming convention and applies consistently.

**Prohibited Practices**:
- âŒ Using standard account for administrative tasks (elevate via UAC/sudo)
- âŒ Using privileged account for daily work (email, web browsing as admin)
- âŒ Shared privileged accounts without PAM vaulting (see Section 3.2)

**Audit Evidence**: Named privileged account inventory, account naming compliance

### 3.2 Requirement: Shared Privileged Accounts

**REQ-A82-004**: Shared privileged accounts **MUST** be secured in PAM vault with session recording.

**Shared Privileged Account Definition**:

Accounts used by multiple administrators or required for system functions:
- **Windows**: Local Administrator, Domain Administrator account
- **Linux**: root account
- **Network devices**: admin, enable
- **Databases**: sa (SQL Server), SYSTEM (Oracle), postgres (PostgreSQL)
- **Applications**: Application admin accounts

**Why Shared Accounts Are High Risk**:
- **No accountability**: Multiple people know password, cannot determine who acted
- **Password sharing**: Passwords shared via email, written down, never changed
- **No audit trail**: All actions logged under same account name (e.g., "root")
- **Permanent access**: Shared passwords don't expire when person leaves

**Shared Account Management Requirements**:

1. **PAM Vaulting** (MANDATORY):
   - All shared privileged passwords stored in PAM vault
   - Passwords never known to administrators (check-out/check-in)
   - Automated password rotation (passwords changed after each use or daily)

2. **Check-Out/Check-In Workflow**:
   - Administrator requests access via PAM solution
   - PAM provides temporary password (or launches session)
   - Administrator uses account for approved task
   - PAM rotates password after check-in (or after time limit)

3. **Session Recording** (MANDATORY):
   - All sessions using shared accounts recorded (keystroke or video)
   - Recordings retained for audit (90 days minimum, 1 year recommended)
   - Recordings reviewable by security team

4. **Approval Workflow** (for high-risk accounts):
   - Shared account access requires approval (manager or security team)
   - Approval includes justification (what task requires shared account?)
   - Emergency access: Approve after-the-fact (with review)

5. **Minimize Shared Account Usage**:
   - **Preferred**: Named privileged accounts with PAM
   - **Acceptable**: Shared accounts in PAM vault with recording
   - **Goal**: Eliminate shared accounts where possible (use named accounts + JIT)

**Shared Accounts by Platform**:

| Platform | Shared Account | PAM Requirement | Session Recording |
|----------|----------------|-----------------|-------------------|
| Windows | Local Administrator | Mandatory | Mandatory |
| Windows | Domain Administrator | Mandatory | Mandatory |
| Linux | root | Mandatory | Mandatory |
| Network | admin, enable | Mandatory | Mandatory |
| Database | sa, SYSTEM, postgres | Mandatory | Mandatory |
| Cloud | AWS root, Azure global admin | Mandatory | Mandatory |

**Audit Evidence**: Shared account inventory, PAM vault configuration, session recordings

### 3.3 Requirement: Service Accounts with Privileges

**REQ-A82-005**: Service accounts with privileged access **MUST** be managed and monitored.

**Service Account Definition**:

Non-human accounts used by applications, services, or automation:
- Windows services running as specific account
- Application service accounts (SharePoint farm account, SQL Server service account)
- Automation/scripting accounts (Ansible service account, scheduled task accounts)
- API service accounts (application-to-application authentication)

**Service Account Challenges**:
- **No interactive login**: Cannot use MFA (service cannot approve push notification)
- **Long-lived credentials**: Passwords rarely changed (breaks service if changed)
- **Broad access**: Often granted excessive privileges (easy shortcut)
- **Forgotten accounts**: Created for project, never removed

**Service Account Management Requirements**:

1. **Inventory and Ownership**:
   - Complete inventory of all service accounts with privileges
   - Owner assigned (who is responsible for this service account?)
   - Purpose documented (what service/application uses this account?)

2. **Credential Management**:
   - **Preferred**: Certificate-based authentication (no passwords)
   - **Acceptable**: Passwords in PAM vault with automated rotation
   - **Prohibited**: Hard-coded passwords in scripts or configuration files

3. **Least Privilege**:
   - Service accounts granted ONLY privileges required for function
   - No "Domain Admin" service accounts (unless absolutely necessary)
   - Regular privilege review (quarterly)

4. **Monitoring**:
   - Service account login monitoring (alert on interactive login - suspicious)
   - Service account privilege usage logging
   - Failed authentication monitoring (detect compromise attempts)

5. **Credential Rotation**:
   - Automated rotation where possible (PAM solution or Group Managed Service Accounts in AD)
   - Manual rotation if automated not possible (minimum: annually)
   - Immediate rotation if compromise suspected

6. **Alternatives to Service Accounts**:
   - **Managed identities** (Azure Managed Identity, AWS IAM Roles for EC2)
   - **Group Managed Service Accounts** (Windows gMSA - automatic password rotation)
   - **Certificate-based authentication** (no password needed)

**Audit Evidence**: Service account inventory, credential rotation logs, privilege reviews

### 3.4 Requirement: Break-Glass / Emergency Accounts

**REQ-A82-006**: Break-glass accounts **MUST** be secured with sealed credentials and monitored usage.

**Break-Glass Account Definition**:

Emergency privileged accounts for use when normal authentication systems fail:
- Primary identity provider down (Azure AD outage, Okta outage)
- MFA system unavailable
- PAM system down
- Critical incident requiring immediate access

**Break-Glass Account Requirements**:

1. **Account Creation**:
   - Minimum 2 break-glass accounts (redundancy)
   - Accounts excluded from normal policies (no password expiration, no MFA requirement)
   - Highest privilege level (Domain Admin, Global Admin, root)

2. **Credential Storage**:
   - **Physical security**: Passwords written down, sealed in envelope, stored in safe
   - **Dual custody**: Requires two authorized persons to open (CEO + CISO, or equivalent)
   - **Digital backup**: Encrypted password in secure offline storage (not in PAM - PAM might be down)

3. **Access Procedures**:
   - **Use triggers**: Only use when normal access methods unavailable
   - **Authorization**: Executive approval required (CISO or CIO)
   - **Documentation**: Reason for use, who used, what actions performed
   - **Immediate password change**: After use, change password and re-seal

4. **Monitoring and Alerting**:
   - **Alert on any use**: Critical alert to security team when break-glass account logs in
   - **Audit logging**: All actions performed with break-glass account logged
   - **Post-incident review**: Full investigation of why break-glass was needed

5. **Regular Verification**:
   - **Quarterly test**: Verify break-glass accounts work (in controlled test environment)
   - **Password verification**: Confirm sealed password matches actual password
   - **Envelope integrity**: Verify seals not broken

**Break-Glass Account Examples**:
- **Windows**: Emergency-Admin1, Emergency-Admin2 (local Administrator rights on all servers)
- **Azure AD**: breakglass1@domain.onmicrosoft.com, breakglass2@domain.onmicrosoft.com
- **AWS**: emergency-root-access-1, emergency-root-access-2

**Audit Evidence**: Break-glass account documentation, sealed credentials inventory, usage logs, test logs

---

## 4. Privileged Access Management (PAM) Requirements

### 4.1 Requirement: PAM Solution Deployment

**REQ-A82-007**: [Organization] **MUST** deploy Privileged Access Management (PAM) solution or equivalent controls.

**PAM Solution Purpose**:

Centralized system for managing, monitoring, and securing privileged access:
- **Password vaulting**: Secure storage of privileged credentials
- **Check-out/check-in**: Temporary access to privileged accounts
- **Session recording**: Record all privileged sessions for audit
- **Just-in-time (JIT) access**: Temporary privilege elevation
- **Automated credential rotation**: Change passwords automatically
- **Approval workflows**: Require approval for privileged access
- **Audit logging**: Complete audit trail of privileged access

**PAM Solution Options** (technology-agnostic):

**Enterprise PAM Solutions**:
- CyberArk Privileged Access Manager
- BeyondTrust Privilege Management
- Delinea Secret Server (formerly Thycotic)
- One Identity Safeguard

**Cloud-Native PAM**:
- Azure Privileged Identity Management (PIM)
- AWS Systems Manager Session Manager
- GCP Privileged Access Manager

**Open-Source / Alternative**:
- HashiCorp Vault
- Teleport (open-source PAM)

**Native OS Controls** (if no PAM solution):
- Windows: Local Admin Password Solution (LAPS) + sudo logging
- Linux: sudo with centralized logging (rsyslog to SIEM)
- Limitation: No session recording, limited workflow, manual password rotation

**PAM Deployment Requirements**:

1. **Coverage**: All shared privileged accounts in PAM vault
2. **High Availability**: PAM solution deployed redundantly (no single point of failure)
3. **Secure Storage**: PAM database encrypted at rest
4. **Access Control**: Only authorized admins can access PAM
5. **Backup**: PAM configuration and vault backed up securely (encrypted backups)
6. **Monitoring**: PAM solution logs forwarded to SIEM

**Audit Evidence**: PAM solution documentation, vaulted accounts inventory, PAM logs

### 4.2 Requirement: Password Vaulting

**REQ-A82-008**: Shared privileged passwords **MUST** be vaulted in PAM solution.

**Password Vaulting Requirements**:

1. **Credential Onboarding**:
   - Discover privileged accounts across all systems
   - Import credentials into PAM vault
   - Verify credentials work (test login)
   - Rotate credentials after import (previous password no longer valid)

2. **Secure Storage**:
   - Passwords encrypted at rest in PAM vault
   - Passwords encrypted in transit (TLS)
   - Passwords never displayed in plain text (copy-paste to application)

3. **Check-Out/Check-In Workflow**:
   - **Check-out**: Administrator requests access, PAM provides temporary credential
   - **Session**: Administrator uses credential for approved task
   - **Check-in**: Administrator returns credential or session expires
   - **Rotation**: PAM changes password after check-in (or after defined interval)

4. **Access Policies**:
   - Who can check out which credentials? (role-based access to vault)
   - Approval required for high-risk accounts? (Domain Admin, root, production DB)
   - Time limits on check-out? (automatic check-in after X hours)
   - Exclusive access? (only one person can check out account at a time)

5. **Credential Types in Vault**:
   - Shared administrative passwords (root, Administrator, sa)
   - Service account passwords
   - API keys and tokens
   - SSH private keys
   - Cloud access keys (AWS access keys, Azure service principal secrets)
   - Encryption keys (for specific use cases, not primary key management)

**Automated Password Rotation**:
- **Frequency**: After each check-in, or daily/weekly for inactive accounts
- **Rotation mechanism**: PAM connects to system and changes password programmatically
- **Verification**: PAM verifies new password works (test login)
- **Notification**: Alert if rotation fails

**Audit Evidence**: PAM vault inventory, check-out/check-in logs, rotation logs

### 4.3 Requirement: Just-in-Time (JIT) Privileged Access

**REQ-A82-009**: Just-in-time privileged access **SHOULD** be implemented to minimize standing privileges.

**JIT Privileged Access Concept**:

Instead of permanent admin rights, grant temporary privilege elevation:
- **Normal state**: User has NO admin rights
- **When needed**: User requests admin rights for specific task
- **Temporary grant**: Admin rights granted for limited time (e.g., 4 hours)
- **Automatic revocation**: Admin rights automatically removed after time expires
- **Audit**: Full audit trail of when admin rights granted and what was done

**JIT Benefits**:
- **Reduced attack surface**: Most of the time, accounts have no elevated privileges
- **Lateral movement prevention**: Attacker compromises account when NO admin rights
- **Accountability**: Clear justification required for each admin rights grant
- **Compliance**: Demonstrates least privilege principle

**JIT Implementation Options**:

1. **Azure Privileged Identity Management (PIM)**:
   - JIT for Azure AD admin roles (Global Admin, Security Admin, etc.)
   - Time-bound role activation (user activates role for 1-8 hours)
   - Approval workflow (require manager approval for role activation)
   - MFA on activation (require MFA to activate privileged role)

2. **AWS IAM Temporary Credentials**:
   - AssumeRole for temporary AWS access
   - Time-limited sessions (configurable duration)
   - Federated access with temporary tokens

3. **PAM Solution JIT**:
   - CyberArk Dual Control
   - BeyondTrust Temporary Privilege Elevation
   - Delinea Just-in-Time access

4. **Native OS JIT** (less sophisticated):
   - Windows: Admin Approval Mode (UAC prompts)
   - Linux: sudo with time limits (sudo timeout)
   - Limitation: No centralized management, limited workflow

**JIT Access Workflow**:

1. User requests privileged access (via PAM portal or PIM)
2. User provides justification ("Need to restart production DB server")
3. Approval (automatic for low-risk, manual for high-risk)
4. Privileged access granted for defined time (e.g., 4 hours)
5. User performs administrative task
6. Access automatically revoked after time expires
7. Session recorded and audited

**JIT vs. Standing Privileges**:

| Scenario | Standing Privileges | JIT Access |
|----------|---------------------|------------|
| **Daily state** | User always has admin rights | User has no admin rights |
| **When compromise occurs** | Attacker gets admin access | Attacker gets standard access only |
| **Audit complexity** | All admin actions always possible | Admin actions only during grant period |
| **User experience** | Seamless (always admin) | Request-and-approve (extra step) |
| **Security** | Higher risk | Lower risk (time-bounded) |

**JIT Adoption Strategy**:
- **Start**: High-risk privileged accounts (Domain Admin, Global Admin)
- **Expand**: Server administrators, database administrators
- **Goal**: 50%+ of privileged access via JIT within 24 months

**Audit Evidence**: JIT access requests, approval logs, time-bounded grants

### 4.4 Requirement: Approval Workflows for Privileged Access

**REQ-A82-010**: High-risk privileged access **MUST** require approval workflows.

**Approval Workflow Requirements**:

**Tier 0 Privileged Access** (Domain Admin, Global Admin, root on critical systems):
- **Approval required**: Yes, mandatory
- **Approver**: Security team lead or CISO
- **Approval timeframe**: 15 minutes for emergencies, 4 hours for planned work
- **Justification**: Business reason required ("Disaster recovery test", "Security incident response")

**Tier 1 Privileged Access** (Server admin, DBA):
- **Approval required**: For production systems
- **Approver**: Manager or senior admin
- **Approval timeframe**: 1 hour
- **Justification**: Change ticket number or incident number

**Tier 2 Privileged Access** (Workstation admin):
- **Approval required**: No (automatic)
- **Logging**: Yes (all access logged)
- **Justification**: Recorded for audit

**Emergency Access**:
- **Break-glass process**: Access granted immediately, approval after-the-fact
- **Review**: Within 24 hours of emergency access
- **Verification**: Was emergency legitimate? What was done?

**Approval Workflow Integration**:
- PAM solution approval workflows
- Azure PIM approval workflows
- Integration with ticketing system (ServiceNow, Jira) - link access to change ticket

**Audit Evidence**: Approval logs, justification records, emergency access reviews

### 4.5 Requirement: Privileged Session Recording

**REQ-A82-011**: Privileged sessions **MUST** be recorded for security audit and forensics.

**Session Recording Requirements**:

**What to Record**:
- All sessions using shared privileged accounts (root, Administrator, sa, admin)
- All Tier 0 privileged sessions (Domain Admin, Global Admin)
- Tier 1 sessions on production systems (server admin, DBA on production)

**Recording Methods**:

1. **Keystroke Logging** (text-based):
   - Record all commands typed and output displayed
   - Lower storage requirements (text-only)
   - Searchable (can search for specific commands)
   - Works well for: SSH sessions, database queries, command-line admin

2. **Video Recording** (graphical):
   - Record full video of session (screen capture)
   - Higher storage requirements (video files)
   - Shows GUI interactions
   - Works well for: RDP sessions, web-based admin consoles, GUI applications

3. **Hybrid Approach**:
   - Keystroke logging for SSH/CLI sessions
   - Video recording for RDP/GUI sessions

**Session Recording Platforms**:
- PAM solutions (CyberArk, BeyondTrust - built-in session recording)
- Dedicated session recording (Ekran System, ObserveIT)
- SSH session recording (tlog, asciinema)
- RDP session recording (Windows RDS session recording, third-party tools)

**Recording Retention**:
- **Minimum retention**: 90 days online (searchable)
- **Extended retention**: 1 year archived (compliance requirement)
- **High-risk sessions**: 7 years (financial systems, regulated environments)

**Recording Access Control**:
- **Who can view recordings**: Security team, audit team, authorized investigators
- **Recording search**: Searchable by user, timestamp, system, commands
- **Playback**: Ability to play back session at 1x, 2x, 4x speed
- **Export**: Export recordings for incident investigation

**Privacy Considerations**:
- Users notified that privileged sessions are recorded (login banner)
- Recordings used ONLY for security audit and incident investigation
- Access to recordings logged (who viewed which recording)

**Session Recording Benefits**:
- **Accountability**: Know exactly what admin did during session
- **Forensics**: Investigate what happened during security incident
- **Training**: Use recordings to train junior admins (with permission)
- **Compliance**: Demonstrate privileged access oversight to auditors

**Audit Evidence**: Session recording configuration, sample recordings, recording access logs

---

## 5. Admin Tiering / Tiered Administration Model

### 5.1 Requirement: Privileged Access Tier Classification

**REQ-A82-012**: [Organization] **MUST** implement Admin Tiering Model to prevent lateral movement and limit blast radius.

**Admin Tiering Concept**:

Segregate privileged access into **three tiers** to prevent credential theft and lateral movement:

**Problem without tiering**:
- Attacker compromises workstation â†’ steals Domain Admin credential cached on workstation â†’ compromises entire domain

**Solution with tiering**:
- Tier 0 accounts NEVER log into workstations â†’ attacker compromises workstation â†’ finds NO Tier 0 credentials â†’ cannot reach Tier 0 systems

**Admin Tiering Model Overview**:

```
Tier 0 (Domain/Enterprise Assets)    â† HIGHEST PRIVILEGE, HIGHEST PROTECTION
   â†‘ NO DOWNWARD ACCESS
   
Tier 1 (Server/Application Assets)    â† MEDIUM PRIVILEGE, MEDIUM PROTECTION
   â†‘ NO DOWNWARD ACCESS
   
Tier 2 (Workstation/Endpoint Assets)  â† LIMITED PRIVILEGE, STANDARD PROTECTION
```

**Tier 0 accounts NEVER access Tier 1 or Tier 2 systems**  
**Tier 1 accounts NEVER access Tier 2 systems**

### 5.2 Requirement: Tier 0 - Domain/Enterprise/Critical Infrastructure

**REQ-A82-013**: Tier 0 systems and accounts **MUST** have the strongest security controls.

**Tier 0 Definition**:

Systems and accounts that control the **entire environment** - compromise of Tier 0 = complete organizational breach.

**Tier 0 Systems** (can access ANY system in organization):

1. **Active Directory Domain Controllers**:
   - Domain controllers (Windows AD)
   - AD replication infrastructure
   - DNS servers (if integrated with AD)
   - Read-only domain controllers (RODCs)

2. **Cloud Identity Tenants**:
   - Azure AD tenant (entire tenant = Tier 0)
   - AWS root account and Organization root
   - GCP Organization node

3. **Security Infrastructure**:
   - SIEM systems (Splunk, Datadog, etc.)
   - PAM solution (CyberArk, BeyondTrust)
   - Backup infrastructure (can restore ANY system)
   - Certificate Authority (PKI root and issuing CAs)

4. **Critical Management Systems**:
   - ITSM admin (ServiceNow admins - control IT processes)
   - Identity governance platforms (SailPoint, One Identity)
   - Network management systems (with credentials to all network devices)

**Tier 0 Accounts**:
- Domain Admins, Enterprise Admins, Schema Admins (Windows AD)
- Azure Global Administrator, Security Administrator (Azure AD)
- AWS root user, Organization admin (AWS)
- GCP Organization Admin, Security Admin (GCP)
- Backup Administrators (Veeam admins, backup server admins)
- SIEM Administrators
- PAM Administrators
- PKI Administrators (Certificate Authority admins)

**Tier 0 Security Requirements** (STRONGEST controls):

1. **Separate Accounts per Tier**:
   - User has: `john.doe` (standard), `john.doe.tier1` (Tier 1 admin), `john.doe.tier0` (Tier 0 admin)
   - Tier 0 account used ONLY for Tier 0 administrative tasks
   - Tier 0 account NEVER used for email, web browsing, or non-Tier 0 tasks

2. **Dedicated Privileged Access Workstations (PAWs)**:
   - Tier 0 admins use **dedicated hardened workstations** (PAWs) for Tier 0 access
   - PAWs are clean, locked-down, monitored systems
   - PAWs cannot browse internet, cannot check email (air-gapped from user activity)
   - PAWs only RDP to Tier 0 systems

3. **Hardware MFA Tokens** (FIDO2):
   - Tier 0 accounts REQUIRE hardware MFA tokens (not authenticator apps)
   - Phishing-resistant authentication
   - YubiKey, Titan Security Key, or equivalent

4. **Session Recording MANDATORY**:
   - ALL Tier 0 sessions recorded (100% coverage)
   - Real-time monitoring of Tier 0 activities
   - Alerts on any Tier 0 account activity

5. **Just-in-Time Access** (where possible):
   - Tier 0 rights granted temporarily (not standing privileges)
   - Azure PIM for Azure AD Global Admin (activate role for 4 hours, then auto-revoke)

6. **Network Isolation**:
   - Tier 0 systems on separate VLAN/network segment
   - Firewall rules: ONLY PAWs can connect to Tier 0 systems
   - Jump servers for Tier 0 access (bastion hosts)

7. **No Internet Access**:
   - Tier 0 accounts cannot browse internet (no phishing risk)
   - Tier 0 accounts cannot check email

8. **Quarterly Access Reviews**:
   - Every quarter: Review who has Tier 0 access
   - Justification required for each Tier 0 account
   - Remove access if no longer needed

**Tier 0 Isolation Benefits**:
- Attacker compromises user workstation â†’ NO Tier 0 credentials found â†’ cannot escalate to Tier 0
- Limits blast radius: Even if Tier 1 or Tier 2 compromised, Tier 0 remains secure

**Audit Evidence**: Tier 0 system inventory, Tier 0 account inventory, PAW deployment, hardware token assignment

### 5.3 Requirement: Tier 1 - Server/Application Infrastructure

**REQ-A82-014**: Tier 1 systems and accounts **MUST** have strong security controls and NOT access Tier 0.

**Tier 1 Definition**:

Systems and accounts that manage **servers and applications** - compromise of Tier 1 affects production systems but not entire environment.

**Tier 1 Systems**:

1. **Server Infrastructure**:
   - Windows servers (not domain controllers)
   - Linux servers (web, app, database servers)
   - Virtualization hosts (VMware ESXi, Hyper-V hosts)

2. **Application Infrastructure**:
   - ERP systems (SAP, Oracle EBS)
   - CRM systems (Salesforce)
   - Database servers (SQL Server, Oracle, PostgreSQL, MySQL)
   - Web applications (production web apps)

3. **Cloud Infrastructure** (non-global):
   - AWS EC2 instances, RDS databases
   - Azure virtual machines, SQL databases
   - GCP Compute Engine instances

**Tier 1 Accounts**:
- Server administrators (Windows server admin, Linux admin)
- Application administrators (SAP admin, Salesforce admin)
- Database administrators (SQL Server DBA, Oracle DBA)
- Virtualization administrators (VMware admin, Hyper-V admin)
- Cloud infrastructure administrators (AWS EC2 admin, Azure VM admin - NOT Global Admin)

**Tier 1 Security Requirements**:

1. **Separate Admin Accounts**:
   - User has: `john.doe` (standard), `john.doe.tier1` (Tier 1 admin)
   - Tier 1 account used ONLY for server/application administration
   - Tier 1 account NEVER logs into Tier 0 systems (prevented via firewall/GPO)

2. **MFA MANDATORY**:
   - Tier 1 accounts REQUIRE MFA (authenticator app minimum, hardware token preferred)

3. **Separate Admin Workstations** (recommended but not mandatory like Tier 0):
   - Dedicated workstations for Tier 1 administration (separate from daily-use laptop)
   - Alternatively: Jump servers/bastion hosts for Tier 1 access

4. **Session Recording** (Tier 1 production systems):
   - Record sessions on production Tier 1 systems
   - Development/test Tier 1 systems: Recording recommended but not mandatory

5. **Quarterly Access Reviews**:
   - Review Tier 1 access quarterly
   - Remove access if no longer needed

6. **Tier Isolation Enforcement**:
   - Tier 1 accounts CANNOT log into Tier 0 systems (GPO, Azure conditional access)
   - Tier 1 accounts CANNOT log into Tier 2 systems (prevents credential theft if Tier 2 compromised)

**Tier 1 Isolation Benefits**:
- Attacker compromises Tier 1 server â†’ finds Tier 1 credentials â†’ can access other Tier 1 servers
- BUT: Cannot escalate to Tier 0 (no Tier 0 credentials on Tier 1 systems)
- AND: Cannot pivot to Tier 2 workstations (Tier 1 accounts restricted)

**Audit Evidence**: Tier 1 system inventory, Tier 1 account inventory, tier isolation policies

### 5.4 Requirement: Tier 2 - Workstation/Endpoint

**REQ-A82-015**: Tier 2 systems and accounts **MUST NOT** have access to Tier 0 or Tier 1 systems.

**Tier 2 Definition**:

Systems and accounts that manage **end-user workstations and devices** - lowest privilege tier.

**Tier 2 Systems**:
- End-user workstations (desktops, laptops)
- Mobile devices (smartphones, tablets)
- Printers, scanners, peripheral devices

**Tier 2 Accounts**:
- Desktop support / Help desk (local admin on workstations)
- MDM administrators (Intune admin, Jamf admin - device management only)
- Endpoint management (patch management for workstations)

**Tier 2 Security Requirements**:

1. **Limited Privilege**:
   - Tier 2 admins have local admin on workstations ONLY
   - Cannot access servers (Tier 1) or domain controllers (Tier 0)

2. **MFA MANDATORY**:
   - Tier 2 accounts REQUIRE MFA

3. **Tier Isolation Enforcement**:
   - Tier 2 accounts CANNOT log into Tier 0 or Tier 1 systems (firewall rules, access denied)

4. **Quarterly Access Reviews**:
   - Review Tier 2 access quarterly

**Tier 2 Why It Matters**:
- Workstations are MOST frequently compromised (phishing, malware, drive-by downloads)
- If Tier 0 or Tier 1 accounts log into workstations â†’ credentials cached â†’ attacker steals credentials
- Tier isolation prevents this: No Tier 0/1 credentials on workstations = attacker stuck at Tier 2

**Audit Evidence**: Tier 2 account inventory, tier isolation enforcement

### 5.5 Requirement: Tier Isolation Enforcement

**REQ-A82-016**: Tier isolation **MUST** be technically enforced to prevent cross-tier access.

**Tier Isolation Enforcement Methods**:

1. **Group Policy Objects (GPO)** - Windows AD:
   - Deny logon policies: Tier 0 accounts denied logon to Tier 1/2 systems
   - Logon restrictions configured via GPO applied to OUs (Organizational Units)

2. **Azure AD Conditional Access Policies**:
   - Tier 0 users can only access Tier 0 devices (PAWs)
   - Block Tier 0 users from accessing Tier 1/2 devices

3. **Firewall Rules**:
   - Network segmentation: Tier 0 network isolated from Tier 1/2 networks
   - Only PAWs can connect to Tier 0 systems (firewall rules)

4. **PAM Solution Tier Enforcement**:
   - CyberArk, BeyondTrust: Configure access policies based on tier
   - Tier 0 accounts can only check out Tier 0 credentials
   - Attempting to use Tier 0 account on Tier 1 system: DENIED

5. **Authentication Policies** (Windows AD):
   - Authentication Policies and Silos (Windows Server 2012 R2+)
   - Restrict which accounts can authenticate to which systems

**Tier Isolation Monitoring**:
- **Alert on tier violations**: Tier 0 account attempting to log into Tier 1/2 system = CRITICAL ALERT
- **Weekly tier violation reports**: Report showing any tier isolation violations
- **Investigation**: Any tier violation investigated immediately (legitimate need or attack?)

**Audit Evidence**: Tier isolation policies (GPOs, conditional access), tier violation logs, monitoring alerts

### 5.6 Requirement: Admin Tiering Implementation Roadmap

**REQ-A82-017**: Admin tiering implementation **MUST** follow phased approach.

**Admin Tiering Adoption Phases**:

**Phase 1 - Foundation** (Months 1-3):
- Classify all systems into Tier 0/1/2
- Identify all privileged accounts and classify by tier
- Create separate admin accounts per tier (john.doe.tier0, john.doe.tier1, john.doe.tier2)
- Document tier isolation requirements

**Phase 2 - Tier 0 Protection** (Months 4-6):
- Deploy Privileged Access Workstations (PAWs) for Tier 0 admins
- Enforce Tier 0 account restrictions (can only log into PAWs and Tier 0 systems)
- Deploy hardware MFA tokens for Tier 0 accounts
- Enable session recording for all Tier 0 access

**Phase 3 - Tier 1 Isolation** (Months 7-9):
- Enforce Tier 1 account restrictions (cannot log into Tier 0 or Tier 2 systems)
- Deploy jump servers / bastion hosts for Tier 1 access
- Enable session recording for Tier 1 production access

**Phase 4 - Monitoring and Compliance** (Months 10-12):
- Deploy tier violation monitoring and alerting
- Generate tier compliance reports
- Train administrators on tier model
- Quarterly tier compliance reviews

**Adoption Metrics**:
- Tier classification completion: 100% of systems classified
- Tier 0 PAW deployment: 100% of Tier 0 admins using PAWs
- Tier 0 hardware MFA: 100% of Tier 0 accounts using hardware tokens
- Tier isolation enforcement: 95%+ compliance (minimal tier violations)
- Tier violation response time: <15 minutes for critical alerts

**Audit Evidence**: Tiering implementation roadmap, phase completion status, adoption metrics

---

## 6. Multi-Factor Authentication for Privileged Access

### 6.1 Requirement: MFA Mandatory for All Privileged Access

**REQ-A82-018**: Multi-factor authentication **MUST** be enabled for ALL privileged accounts.

**MFA for Privileged Access Requirements**:

**Non-Negotiable**:
- **100% of privileged users MUST have MFA** - no exceptions
- **Password-only privileged access is PROHIBITED**

**MFA Methods by Tier**:

| Tier | MFA Requirement | Acceptable Methods |
|------|-----------------|-------------------|
| **Tier 0** | Hardware tokens REQUIRED | FIDO2, YubiKey, Titan Security Key |
| **Tier 1** | MFA REQUIRED | Hardware token (preferred), authenticator app (acceptable) |
| **Tier 2** | MFA REQUIRED | Authenticator app, push notifications |

**Privileged Account MFA Enrollment**:
- **Deadline**: Within 7 days of privileged access grant
- **Verification**: IT Security verifies MFA before activating privileged rights
- **Non-compliance**: Privileged access revoked if MFA not enrolled within deadline

**MFA Bypass Prohibited**:
- âŒ No privileged access without MFA (even temporarily)
- âŒ No "MFA bypass" exceptions for convenience
- âœ… Break-glass accounts only exception (sealed, monitored, executive approval)

**Audit Evidence**: Privileged user MFA enrollment status (100% target), MFA method by tier

---

## 7. Privileged Access Monitoring and Logging

### 7.1 Requirement: Privileged Command Logging

**REQ-A82-019**: All privileged commands **MUST** be logged for audit and forensics.

**Privileged Command Logging Requirements**:

**Windows**:
- PowerShell script block logging (capture all PowerShell commands)
- Windows Event Logs for privileged access (Event ID 4672 - Special Logon, 4688 - Process Creation)
- Sysmon for detailed process monitoring

**Linux**:
- sudo logging (all sudo commands logged to syslog)
- aureport / auditd for command auditing
- Centralized logging (rsyslog forwarding to SIEM)

**Network Devices**:
- Command logging on routers, switches, firewalls (syslog)
- Enable highest logging level (informational or debug)

**Databases**:
- Database audit logging (SQL Server Audit, Oracle Audit, PostgreSQL pgaudit)
- Log DDL (Data Definition Language) commands (CREATE, ALTER, DROP)
- Log privileged access (sa, SYSTEM, postgres usage)

**Cloud Platforms**:
- AWS CloudTrail (logs all API calls, including privileged actions)
- Azure Activity Log (logs Azure resource changes)
- GCP Cloud Audit Logs

**Log Centralization**:
- Forward all privileged access logs to SIEM (Security Information and Event Management)
- Real-time analysis and correlation
- Long-term retention (minimum 90 days online, 1 year archived)

**Audit Evidence**: Privileged command logs, SIEM integration, log retention configuration

### 7.2 Requirement: Privileged Access Monitoring and Alerting

**REQ-A82-020**: Privileged access **MUST** be monitored for anomalies and security incidents.

**Privileged Access Alerts**:

| Alert | Threshold | Priority | Response Time |
|-------|-----------|----------|---------------|
| **Privileged account login outside business hours** | 10 PM - 6 AM weekdays, weekends | Medium | 1 hour |
| **Privileged account from unusual location** | New country/city never seen before | High | 30 minutes |
| **Tier 0 account activity** | ANY Tier 0 account activity | High | 15 minutes |
| **Tier isolation violation** | Tier 0 account logging into Tier 1/2 system | Critical | 5 minutes |
| **Privileged account failed logins** | 3 failed attempts in 5 minutes | High | 15 minutes |
| **Privileged session > 4 hours** | Session exceeds maximum duration | Medium | 1 hour |
| **Privileged account accessing unusual systems** | System never accessed before | Medium | 1 hour |
| **Break-glass account usage** | ANY break-glass account login | Critical | Immediate |

**Automated Response Actions**:
- Alert security team (email, SMS, Slack notification)
- Create incident ticket automatically (ServiceNow, Jira)
- Require additional MFA challenge (risk-based MFA)
- Terminate session if critical violation detected

**Privileged Access Dashboards**:
- Real-time dashboard showing active privileged sessions
- Privileged account usage statistics (most active accounts, systems accessed)
- Tier isolation compliance status
- Alert summary (open alerts, resolved alerts, response times)

**Audit Evidence**: Privileged access alert logs, response actions, incident tickets

---

## 8. Privileged Credential Rotation

### 8.1 Requirement: Automated Credential Rotation

**REQ-A82-021**: Shared privileged credentials **MUST** be rotated automatically.

**Credential Rotation Requirements**:

**Rotation Frequency**:

| Account Type | Rotation Frequency | Trigger |
|--------------|-------------------|---------|
| **Shared admin accounts** (root, Administrator, sa) | After each check-in from PAM | After use |
| **Service accounts** (if in PAM) | Daily | Automated schedule |
| **Break-glass accounts** | After each use | Manual after use |
| **Tier 0 accounts** | After each session | After use |
| **API keys/tokens** | 90 days | Scheduled |

**Rotation Mechanism**:
- **PAM solution**: CyberArk, BeyondTrust automatically rotate passwords after check-in
- **Group Managed Service Accounts (gMSA)**: Windows automatically rotates passwords (30 days)
- **Native scripts**: PowerShell / Python scripts for systems without PAM

**Rotation Verification**:
- After rotation, PAM verifies new password works (test login)
- If rotation fails, alert security team immediately
- Retry rotation automatically (up to 3 attempts)

**Rotation Exceptions**:
- Service accounts with application dependencies (coordinate rotation with application team)
- Accounts requiring manual rotation (legacy systems without API support)
- Document exceptions and remediation plans

**Audit Evidence**: Credential rotation logs, rotation frequency compliance, failed rotation alerts

---

## 9. Privileged Access Reviews

### 9.1 Requirement: Quarterly Privileged Access Reviews

**REQ-A82-022**: Privileged access **MUST** be reviewed quarterly to verify continued need.

**Quarterly Review Requirements**:

**Review Scope**:
- ALL privileged users (every person with privileged accounts)
- ALL privileged accounts (named, shared, service, break-glass)
- ALL admin tier assignments (Tier 0/1/2 classification)

**Review Questions**:
1. Does this user still require privileged access? (Still in role requiring admin access?)
2. Is the level of privilege appropriate? (Should Tier 1 be downgraded to Tier 2?)
3. Has the user used privileged access in last 90 days? (Unused access = remove)
4. Is business justification still valid?
5. Is MFA enabled and functional?

**Review Workflow**:
1. **Generate review report**: List all privileged users and accounts (from Workbook 3)
2. **Send to managers**: Each manager reviews their team's privileged access
3. **Manager attestation**: Manager confirms each user still needs access (or marks for removal)
4. **Security review**: Security team verifies attestations and performs spot checks
5. **Access removal**: Remove privileged access for users no longer needing it
6. **Documentation**: Document review results, approvals, and removals

**Review Metrics**:
- **Review completion rate**: 100% (all privileged users reviewed quarterly)
- **Access removal rate**: 5-10% (continuous cleanup of unneeded access)
- **Review timeliness**: Completed within 30 days of quarter end

**Annual Deep Review** (in addition to quarterly):
- Review ALL service accounts (are they still needed?)
- Review ALL break-glass accounts (do they work? Seals intact?)
- Review admin tier classifications (are systems/accounts correctly classified?)
- Review PAM solution configuration (are policies still appropriate?)

**Audit Evidence**: Quarterly review reports, manager attestations, access removal logs

---

## 10. Measurable Requirements and Audit Verification

### 10.1 Privileged Access Security Metrics

**Measurable requirements for audit verification**:

| Requirement | Metric | Target | Verification Method |
|-------------|--------|--------|---------------------|
| **Privileged accounts - named** | % named accounts (vs. shared) | 70%+ | Workbook 3 |
| **Privileged accounts in PAM** | % shared accounts vaulted | 100% | Workbook 3 |
| **Privileged MFA coverage** | % privileged users with MFA | 100% | Workbook 2 + 3 |
| **Tier 0 hardware MFA** | % Tier 0 with hardware tokens | 100% | Workbook 3 |
| **Tier 0 PAW deployment** | % Tier 0 admins with PAWs | 100% | Workbook 3 |
| **Session recording coverage** | % privileged sessions recorded | 90%+ | Workbook 4 |
| **Credential rotation** | % accounts with recent rotation | 95%+ | Workbook 3 |
| **Tier isolation compliance** | Cross-tier violations per month | <5 | Workbook 4 |
| **Quarterly review completion** | % privileged users reviewed | 100% | Workbook 4 |
| **Privileged access response time** | Avg. alert response time | <30 min | Workbook 4 |

### 10.2 Audit Evidence Requirements

**For ISO 27001:2022 A.8.2 audit**:

1. **Policy and procedures**: This document (ISMS-POL-A.8.2-3-5-S3)
2. **Privileged account inventory**: Workbook 3 (complete inventory with tier classification)
3. **PAM deployment**: PAM solution documentation, vaulted accounts list
4. **Session recordings**: Sample session recordings, recording retention policy
5. **MFA for privileged**: Privileged user MFA enrollment status (target 100%)
6. **Admin tiering**: Tier classification documentation, PAW deployment, tier isolation policies
7. **Privileged access monitoring**: Workbook 4 (activity logs, alerts, reviews)
8. **Credential rotation**: Rotation logs, frequency compliance
9. **Quarterly reviews**: Review reports, attestations, access removal documentation

---

**END OF SECTION 3 (PRIVILEGED ACCESS REQUIREMENTS - A.8.2)**

**Next Section**: ISMS-POL-A.8.2-3-5-S4 (Information Access Restriction Requirements - A.8.3)

---

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architecture Lead | Initial privileged access requirements (A.8.2) |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**

---


**Document ID**: ISMS-POL-A.8.2-3-5-S4  
**Title**: Information Access Restriction Requirements (ISO/IEC 27001:2022 Control A.8.3)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect | Initial information access restriction requirements (A.8.3) |

**Review Cycle**: Annual  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Architect
- Systems Review: Systems Administration Manager
- Database Review: Database Administration Lead

**Distribution**: Security team, systems administrators, database administrators, application owners, developers, auditors  
**Related Documents**: 
- ISMS-POL-A.8.2-3-5-S1 (Executive Summary)
- ISMS-POL-A.8.2-3-5-S2 (Authentication - A.8.5)
- ISMS-IMP-A.8.2-3-5-S4 (Access Enforcement Implementation)

---

## 1. Control Objective and Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.3

**Official Control Text**:

> *Access to information and other associated assets should be restricted in accordance with the established topic-specific policy on access control.*

**Control Purpose**: Ensure technical access controls (file permissions, database grants, API scopes, encryption) enforce the access control policy defined in A.5.15, implementing principle of least privilege at the technical layer.

**Why This Matters**:

Access restriction is the **last line of defense**. Even with perfect authentication (A.8.5) and privileged access controls (A.8.2), misconfigured permissions allow unauthorized access:

- **Misconfigured file permissions** = data exposed to unauthorized users
- **Overly permissive database grants** = applications can read/write unintended data
- **Missing default deny** = accidental access (everyone can access everything)
- **No encryption** = data readable if access controls bypassed

Proper access restriction provides:
- **Defense in depth** - multiple layers of access controls
- **Principle of least privilege** enforced technically (not just policy)
- **Audit trail** of access attempts (successful and denied)
- **Containment** - lateral movement blocked even if one system compromised

### 1.2 Scope of A.8.3 Requirements

This section defines mandatory requirements for:

1. **Operating System Access Controls** - File permissions (NTFS, ACLs)
2. **Database Access Controls** - SQL grants, row/column-level security
3. **Application Access Controls** - RBAC, ABAC within applications
4. **API Access Controls** - OAuth scopes, API keys, rate limiting
5. **Cloud Resource Access Controls** - IAM policies (AWS, Azure, GCP)
6. **Data Classification Enforcement** - Encryption based on sensitivity
7. **Network Segmentation** - Firewalls between zones
8. **Default Deny Principle** - Explicit allow required
9. **Access Control Testing** - Penetration testing, configuration audits

---

## 2. Operating System Access Controls

### 2.1 Requirement: File System Permissions

**REQ-A83-001**: File system permissions **MUST** implement principle of least privilege with default deny.

**File System Permission Requirements**:

**Windows (NTFS)**:
- **Default permissions**: Deny all, explicit allow required
- **Permission types**: Read, Write, Modify, Full Control
- **Permission inheritance**: Properly configured (child folders inherit parent permissions)
- **Special permissions**: Limited use (require justification and approval)
- **Auditing**: Log access to sensitive directories

**Linux (ext4, XFS, ZFS)**:
- **Default permissions**: 644 files (rw-r--r--), 755 directories (rwxr-xr-x)
- **Sensitive data**: 600 files (rw-------), 700 directories (rwx------)
- **ACLs**: Use Access Control Lists for complex permission requirements
- **SELinux/AppArmor**: Mandatory Access Control for high-security systems
- **sudo**: Logged and monitored (see A.8.2 privileged access)

**Permission Assignment**:
- **User permissions**: Individual users only when necessary (prefer groups)
- **Group permissions**: Use AD groups (finance-team, hr-team, engineering-team)
- **Everyone/Authenticated Users**: NEVER grant write access to these groups
- **Service accounts**: Grant only permissions required for application function

**Prohibited Practices**:
- âŒ Full Control granted to Users or Everyone groups
- âŒ Write permissions to system directories (C:\Windows, /etc, /usr/bin)
- âŒ Executable permissions on data directories
- âŒ Permission inheritance disabled without justification

**Audit Evidence**: Sample file permissions from critical systems, permission audit logs (Workbook 5)

### 2.2 Requirement: Permission Management

**REQ-A83-002**: File system permissions **MUST** be documented, reviewed, and audited.

**Permission Documentation**:
- **Permission matrix**: Document which groups have access to which shares/directories
- **Business justification**: Why does this group need access?
- **Permission templates**: Standard permission sets for common scenarios (department share, project share, etc.)

**Regular Permission Audits**:
- **Frequency**: Quarterly for sensitive data, annually for standard data
- **Automated scanning**: PowerShell scripts (Get-Acl), Linux scripts (getfacl)
- **Manual review**: Review permissions on high-value directories
- **Cleanup**: Remove permissions for users no longer needing access

**Permission Change Control**:
- **Approval required**: Manager approval for adding permissions to sensitive directories
- **Change logging**: All permission changes logged (Windows Event ID 4670, Linux auditd)
- **Review**: Quarterly review of permission changes

**Audit Evidence**: Permission matrix, audit reports (Workbook 5), permission change logs

---

## 3. Database Access Controls

### 3.1 Requirement: Database Permissions and Grants

**REQ-A83-003**: Database access **MUST** use principle of least privilege with specific grants.

**Database Permission Requirements**:

**SQL Databases** (SQL Server, PostgreSQL, MySQL, Oracle):
- **Grant specific privileges only**: SELECT, INSERT, UPDATE, DELETE (not ALL PRIVILEGES)
- **Schema-level grants**: Grant on specific schemas/databases, not server-wide
- **Table-level grants**: For sensitive tables, grant specific access (not entire schema)
- **Row-level security**: Implement where users should only see subset of data (e.g., sales reps see only their accounts)
- **Column-level security**: Hide sensitive columns from standard users (e.g., salary, SSN)

**NoSQL Databases** (MongoDB, Cassandra, DynamoDB):
- **Database-specific roles**: Create custom roles with minimal privileges
- **Collection/table-level permissions**: Not database-wide admin access
- **Read-only users**: Applications that only need read access get read-only credentials

**Database Account Types**:

1. **Application Service Accounts**:
   - Grant ONLY privileges required for application function
   - Typical: SELECT, INSERT, UPDATE on specific tables (NOT DELETE, DROP)
   - Never grant: CREATE, ALTER, DROP (DDL privileges)
   - Never grant: GRANT OPTION (ability to grant privileges to others)

2. **Database Administrators (DBAs)**:
   - Full privileges on database servers (covered in A.8.2 privileged access)
   - Named DBA accounts (john.dba), not shared "sa" or "root"
   - MFA required, session recorded

3. **Data Analysts / Read-Only Users**:
   - SELECT privilege only
   - Access only to non-sensitive tables or anonymized views
   - Connection from specific IP addresses only (if possible)

**Prohibited Practices**:
- âŒ Granting "db_owner" or "ALL PRIVILEGES" to application accounts
- âŒ Using "sa" or "SYSTEM" accounts for applications
- âŒ Granting "GRANT OPTION" to non-DBAs
- âŒ Shared database credentials across multiple applications

**Audit Evidence**: Database grant reports (SQL queries showing grants), permission reviews (Workbook 5)

### 3.2 Requirement: Database Permission Auditing

**REQ-A83-004**: Database permissions **MUST** be audited regularly.

**Database Audit Procedures**:

**Monthly Audits**:
- Query database for all grants: `SELECT * FROM information_schema.table_privileges` (PostgreSQL)
- Review users with excessive privileges (db_owner, ALL PRIVILEGES)
- Review users with DDL privileges (CREATE, ALTER, DROP)
- Review users with GRANT OPTION
- Alert on new privileged users

**Quarterly Audits**:
- Full permission review for all application accounts
- Verify permissions match application requirements documentation
- Remove unused accounts (accounts with no connections in 90 days)
- Review service account permissions (still need this access?)

**Database Audit Logging**:
- Enable database audit logging (SQL Server Audit, Oracle Audit, PostgreSQL pgaudit)
- Log: Privileged access (sa, SYSTEM), DDL changes (DROP TABLE), sensitive data access
- Forward logs to SIEM for monitoring

**Audit Evidence**: Database permission audit reports, unused account cleanup logs (Workbook 5)

---

## 4. Application Access Controls

### 4.1 Requirement: Role-Based Access Control (RBAC)

**REQ-A83-005**: Applications **MUST** implement role-based access control aligned with business roles.

**RBAC Requirements**:

**Role Definition**:
- Define application roles based on business functions (not technical roles)
- Examples: "Sales Manager", "Customer Service Rep", "Finance Analyst", "HR Admin"
- Each role has specific permissions within application (read, write, approve, delete)

**Permission Assignment**:
- Users assigned to roles (user â†’ role â†’ permissions)
- Roles assigned based on job function (documented in access request)
- Regular review: Quarterly review of user-role assignments

**RBAC Best Practices**:
- **Separation of duties**: High-risk transactions require multiple roles (maker-checker)
- **Least privilege**: Roles have minimum permissions for job function
- **Role hierarchy**: Senior roles inherit junior role permissions (if appropriate)
- **Default deny**: New roles start with no permissions, add as needed

**Application-Specific RBAC Examples**:

**ERP Systems** (SAP, Oracle EBS):
- Complex role structure (hundreds of roles)
- Segregation of Duties (SoD) rules enforced (e.g., cannot create vendor AND approve payment)
- Regular SoD audits

**CRM Systems** (Salesforce):
- Profiles and permission sets
- Record-level access (user sees only their accounts)
- Field-level security (hide sensitive fields from standard users)

**Custom Applications**:
- Application-defined roles
- Permission checks at business logic layer (not just UI layer)
- API endpoints enforce same permissions as web UI

**Audit Evidence**: Application role matrix, user-role assignments, RBAC configuration (Workbook 5)

### 4.2 Requirement: Attribute-Based Access Control (ABAC)

**REQ-A83-006**: Applications **MAY** implement attribute-based access control for complex requirements.

**ABAC Concept**:

Access decisions based on attributes:
- **User attributes**: Department, job title, clearance level, location
- **Resource attributes**: Data classification, owner, project
- **Environmental attributes**: Time of day, network location, device type

**ABAC Examples**:

Example 1 - Data Classification:
- **Rule**: Users can access "Confidential" data only if: (user.clearance == "Confidential" OR "Restricted") AND (user.department == data.owner_department OR user.role == "Executive")

Example 2 - Time-Based Access:
- **Rule**: Contractors can access systems only during business hours (8 AM - 6 PM, Monday-Friday)

Example 3 - Location-Based Access:
- **Rule**: Access to financial systems allowed only from corporate network or VPN (not public Wi-Fi)

**ABAC vs. RBAC**:
- **RBAC**: Simpler, easier to manage, suitable for most applications
- **ABAC**: More flexible, handles complex rules, suitable for high-security environments

**Audit Evidence**: ABAC policy documentation, attribute definitions, access decision logs

---

## 5. API Access Controls

### 5.1 Requirement: API Authentication and Authorization

**REQ-A83-007**: APIs **MUST** implement authentication and authorization with scoped access.

**API Access Control Requirements**:

**API Authentication Methods**:
1. **OAuth 2.0** (preferred for user-facing APIs):
   - Client credentials flow (machine-to-machine)
   - Authorization code flow (user authorization)
   - Access tokens (JWT tokens)

2. **API Keys**:
   - Unique API key per application/client
   - API key rotation (every 90 days)
   - API key revocation capability

3. **Certificate-Based** (mTLS):
   - Client certificates for high-security APIs
   - Mutual TLS authentication

**API Authorization** (OAuth Scopes):
- **Scope-based access**: Define scopes for API endpoints (read:users, write:orders, delete:accounts)
- **Least privilege**: Grant only scopes required for client application function
- **Scope validation**: API endpoints verify client has required scope

**API Rate Limiting**:
- **Purpose**: Prevent abuse, DoS attacks, brute force attempts
- **Limits**: Per API key or per user (e.g., 1000 requests/hour)
- **Response**: HTTP 429 Too Many Requests when limit exceeded

**API Security Controls**:
- **Input validation**: Validate all API inputs (prevent SQL injection, XSS)
- **Output encoding**: Encode API responses (prevent XSS)
- **HTTPS only**: APIs accessible only via HTTPS (not HTTP)
- **CORS policy**: Restrict cross-origin requests to authorized domains

**Prohibited Practices**:
- âŒ APIs without authentication ("public" APIs for sensitive data)
- âŒ API keys in client-side code (JavaScript, mobile apps)
- âŒ Long-lived API keys (no rotation)
- âŒ Broad scopes ("admin" scope for standard users)

**Audit Evidence**: API authentication configuration, OAuth scope definitions, API rate limiting logs (Workbook 5)

### 5.2 Requirement: API Access Logging and Monitoring

**REQ-A83-008**: API access **MUST** be logged and monitored for security incidents.

**API Logging Requirements**:
- **Successful API calls**: User/client, endpoint, timestamp, response code
- **Failed API calls**: User/client, endpoint, timestamp, failure reason (401, 403)
- **Rate limit violations**: Client exceeding rate limits
- **Suspicious patterns**: Brute force attempts, data scraping, unusual access patterns

**API Monitoring Alerts**:
- Alert on: 100+ failed API calls in 5 minutes (brute force)
- Alert on: API access from unusual locations
- Alert on: Spike in API calls (potential DoS or data exfiltration)

**Audit Evidence**: API access logs, monitoring alerts, API security incidents

---

## 6. Cloud Resource Access Controls

### 6.1 Requirement: Cloud IAM Policies

**REQ-A83-009**: Cloud resource access **MUST** use Identity and Access Management (IAM) policies with least privilege.

**Cloud IAM Best Practices**:

**AWS IAM**:
- **Policy structure**: User â†’ Group â†’ IAM Policy â†’ AWS Resources
- **Least privilege**: Grant only actions required (ec2:DescribeInstances, not ec2:*)
- **Resource-level permissions**: Grant access to specific resources (specific S3 bucket, not all buckets)
- **Conditions**: Use conditions for additional security (MFA required, source IP restrictions)
- **Managed policies**: Use AWS Managed Policies where appropriate (reduces management overhead)
- **Service Control Policies (SCPs)**: Organization-level guardrails

**Azure RBAC**:
- **Role assignment**: User â†’ Azure AD Group â†’ Azure Role â†’ Subscription/Resource Group
- **Built-in roles**: Use built-in roles (Reader, Contributor, Owner) where possible
- **Custom roles**: Create custom roles for specific needs (principle of least privilege)
- **Management groups**: Organize subscriptions into hierarchy with inherited policies
- **Privileged Identity Management (PIM)**: Just-in-time access for privileged roles

**GCP IAM**:
- **Policy structure**: User â†’ Google Group â†’ IAM Role â†’ GCP Resources
- **Predefined roles**: Use predefined roles where possible
- **Custom roles**: Create custom roles with specific permissions
- **Resource hierarchy**: Organization â†’ Folder â†’ Project (permissions inherit down)
- **Service accounts**: Use service accounts for applications (not user accounts)

**Common Cloud IAM Principles** (all platforms):
- **No root/global admin usage**: Root/global admin accounts used only for account setup and break-glass
- **Service accounts for applications**: Applications use service accounts (AWS IAM roles, Azure Managed Identity, GCP service accounts)
- **Resource tagging**: Tag resources for access control (e.g., Environment=Production, Owner=FinanceTeam)
- **Cross-account access**: Use roles for cross-account access (not user keys)

**Audit Evidence**: Cloud IAM policy exports, role assignments, permission reviews (Workbook 5)

---

## 7. Data Classification and Access Enforcement

### 7.1 Requirement: Data Classification Alignment

**REQ-A83-010**: Access restrictions **MUST** align with data classification levels.

**Data Classification Levels** (typical):

| Classification | Access Restriction | Encryption | MFA | Example Data |
|----------------|-------------------|------------|-----|--------------|
| **Public** | No restriction | Optional | No | Marketing materials, public website content |
| **Internal** | Authenticated users only | Recommended | No | Internal memos, non-sensitive business documents |
| **Confidential** | Need-to-know, department access | Required (at rest) | Recommended | Customer data, financial reports, source code |
| **Restricted** | Need-to-know, executive approval | Required (at rest + in transit) | Required | PII, trade secrets, M&A documents, passwords |

**Access Enforcement by Classification**:

**Public Data**:
- Access: Anyone (may be published on public website)
- Encryption: Not required
- MFA: Not required

**Internal Data**:
- Access: Authenticated employees and contractors only
- Encryption: Recommended (encryption at rest)
- MFA: Not required (password sufficient)
- Storage: Corporate file shares, internal SharePoint sites

**Confidential Data**:
- Access: Need-to-know basis (specific departments or project teams)
- Encryption: Required (encryption at rest)
- MFA: Recommended (MFA for remote access to confidential data)
- Storage: Dedicated file shares with restricted access, encrypted databases
- Logging: Access logging enabled

**Restricted Data**:
- Access: Need-to-know basis with executive/security approval
- Encryption: Required (encryption at rest and in transit - TLS 1.2+)
- MFA: Required (mandatory MFA for access to restricted data)
- Storage: Dedicated secure storage with audit logging
- Logging: Full audit logging of all access
- DLP: Data Loss Prevention (DLP) policies prevent unauthorized exfiltration

**Audit Evidence**: Data classification policy, classification labels on files/systems, encryption status by classification (Workbook 5)

---

## 8. Network Segmentation for Access Restriction

### 8.1 Requirement: Firewall Rules for Access Enforcement

**REQ-A83-011**: Network segmentation **MUST** enforce access restrictions between security zones.

**Network Segmentation Integration** (see also A.8.22):

Access restriction (A.8.3) leverages network segmentation (A.8.22) for defense in depth:

**Security Zones** (typical):
- **Internet** (untrusted)
- **DMZ** (public-facing servers)
- **Internal Network** (employee workstations, internal servers)
- **Data Center** (production servers, databases)
- **Management Network** (network devices, infrastructure management)

**Inter-Zone Access Rules** (default deny, explicit allow):

| Source Zone | Destination Zone | Allowed Traffic | Rationale |
|-------------|------------------|-----------------|-----------|
| Internet | DMZ | HTTPS (443), HTTP (80) | Public access to web servers |
| Internet | Internal | DENY ALL | No direct access to internal network |
| DMZ | Internet | HTTPS (443) for updates | Web servers need to download updates |
| DMZ | Internal | DENY ALL | DMZ compromised should not reach internal |
| Internal | DMZ | HTTPS (443) | Employees access internal web apps in DMZ |
| Internal | Internet | HTTPS (443), DNS (53) | Employee internet access |
| Data Center | Internet | DENY ALL | Production servers no direct internet |
| Data Center | Internal | Application-specific | Servers serve internal applications |
| Management | All | SSH (22), RDP (3389), SNMP (161) | Infrastructure management |
| All | Management | DENY ALL | Nothing should connect TO management network |

**Firewall Rule Requirements**:
- **Default deny**: All traffic denied unless explicitly allowed
- **Rule documentation**: Each rule has business justification
- **Regular review**: Quarterly review of firewall rules (remove unused rules)
- **Change control**: Firewall rule changes require approval and documentation

**Audit Evidence**: Firewall rule exports, rule justification documentation, rule review logs (Workbook 5 can reference A.8.22 network segmentation assessment)

---

## 9. Encryption-Based Access Restriction

### 9.1 Requirement: Encryption for Access Control

**REQ-A83-012**: Encryption **MUST** be used to restrict access to sensitive data.

**Encryption as Access Control**:

Encryption provides access control: Only users with decryption keys can access data.

**Encryption at Rest**:

**Full Disk Encryption** (FDE):
- **Purpose**: Protect data if device lost/stolen
- **Technologies**: BitLocker (Windows), FileVault (macOS), LUKS (Linux)
- **Key management**: TPM-based or password-protected
- **Scope**: All laptops, mobile devices, removable media

**Database Encryption**:
- **Transparent Data Encryption (TDE)**: Encrypt entire database (SQL Server TDE, Oracle TDE)
- **Column encryption**: Encrypt specific sensitive columns (SSN, credit card numbers)
- **Application-layer encryption**: Application encrypts data before storing in database

**File Encryption**:
- **File system encryption**: Encrypted file systems (EFS on Windows, eCryptfs on Linux)
- **Application-level encryption**: Applications encrypt files before storage (S3 server-side encryption)

**Encryption in Transit**:

**TLS (Transport Layer Security)**:
- **Purpose**: Protect data transmitted over network
- **Requirements**: TLS 1.2 minimum (TLS 1.3 preferred)
- **Scope**: All data in transit (web traffic, API calls, database connections, file transfers)

**VPN (Virtual Private Network)**:
- **Purpose**: Encrypt remote access traffic
- **Technologies**: IPsec VPN, SSL VPN
- **Requirement**: All remote access via VPN

**Key Management**:
- **Key storage**: Keys stored in Hardware Security Module (HSM) or key management service (AWS KMS, Azure Key Vault)
- **Key rotation**: Keys rotated annually (or per policy)
- **Key access control**: Only authorized systems/users can access encryption keys
- **Key backup**: Encryption keys backed up securely (encrypted backup)

**Integration with A.8.24 (Use of Cryptography)**:
- Detailed cryptographic requirements defined in A.8.24
- A.8.3 focuses on access restriction aspect of encryption
- Both controls reference same key management system

**Audit Evidence**: Encryption status by system/data classification (Workbook 5), key management documentation

---

## 10. Default Deny Principle

### 10.1 Requirement: Explicit Allow Required

**REQ-A83-013**: Access controls **MUST** use default deny (whitelist approach).

**Default Deny Principle**:

**Access denied unless explicitly allowed**:
- File permissions: Deny all, grant specific read/write to specific users/groups
- Database permissions: No privileges by default, grant specific privileges
- Firewall rules: Deny all traffic, allow specific traffic flows
- API access: Deny all requests, allow authenticated requests with valid scopes

**Benefits of Default Deny**:
- **Security by default**: Misconfigurations result in denied access (safe failure)
- **Explicit permissions**: All access is intentional (not accidental)
- **Audit clarity**: All allowed access is documented and justified

**Default Deny Implementation**:

**File Systems**:
- Remove "Everyone" and "Authenticated Users" permissions
- Grant access only to specific users/groups who need it

**Databases**:
- Revoke "PUBLIC" permissions (PostgreSQL) or remove default grants
- Grant specific privileges to specific users/roles

**Firewalls**:
- Final rule in firewall ruleset: "DENY ALL"
- All allow rules above this (explicit allows)

**Applications**:
- Default user role: No permissions
- Permissions granted through role assignment

**Prohibited Practices**:
- âŒ "Allow all, deny specific" (blacklist approach) - always insecure
- âŒ Broad permissions first, then restrict (default allow)
- âœ… Deny all first, then grant specific (default deny)

**Audit Evidence**: Permission configurations showing default deny, firewall rule sets (Workbook 5)

---

## 11. Access Control Verification and Testing

### 11.1 Requirement: Configuration Audits

**REQ-A83-014**: Access control configurations **MUST** be audited regularly.

**Configuration Audit Procedures**:

**Quarterly Audits**:
- File system permissions audit (sample sensitive directories)
- Database permissions audit (review grants for all accounts)
- Application RBAC audit (user-role assignments)
- Firewall rule audit (review all rules, remove unused)
- Cloud IAM policy audit (review policies, identify overly permissive)

**Automated Scanning**:
- **CIS Benchmarks**: Automated scanning against CIS security benchmarks
- **Cloud Security Posture Management (CSPM)**: Automated scanning of cloud configurations (Prisma Cloud, Wiz, Orca Security)
- **Configuration management**: Ansible, PowerShell DSC, Terraform state validation

**Manual Reviews**:
- Review access to most sensitive systems (quarterly)
- Review recent permission changes (monthly)
- Spot check: Random sample of systems for permission compliance

**Audit Evidence**: Configuration audit reports, scanning results, remediation tracking (Workbook 5)

### 11.2 Requirement: Penetration Testing

**REQ-A83-015**: Access control effectiveness **MUST** be tested through penetration testing.

**Penetration Testing for Access Controls**:

**Testing Scope**:
- Attempt to bypass access controls (horizontal privilege escalation)
- Attempt to gain elevated privileges (vertical privilege escalation)
- Test API authorization (access data outside assigned scope)
- Test application RBAC (perform actions outside role)

**Testing Frequency**:
- **Annual**: External penetration test (third-party company)
- **Quarterly**: Internal testing (security team or authorized personnel)
- **Ad-hoc**: After major changes (new application, infrastructure changes)

**Test Scenarios**:
- **Horizontal escalation**: User A accesses User B's data
- **Vertical escalation**: Standard user gains admin privileges
- **API abuse**: Enumerate data by manipulating API parameters (IDOR - Insecure Direct Object Reference)
- **File traversal**: Access files outside permitted directories (../../../etc/passwd)
- **SQL injection**: Bypass database access controls via injection attacks

**Remediation**:
- High/critical findings: Remediate within 30 days
- Medium findings: Remediate within 90 days
- Low findings: Remediate within 180 days
- Re-test after remediation

**Audit Evidence**: Penetration test reports, finding remediation tracking (Workbook 5)

---

## 12. Measurable Requirements and Audit Verification

### 12.1 Access Control Security Metrics

**Measurable requirements for audit verification**:

| Requirement | Metric | Target | Verification Method |
|-------------|--------|--------|---------------------|
| **Systems with default deny** | % systems configured default deny | 95%+ | Workbook 5 |
| **Permission audit coverage** | % systems audited quarterly | 100% sensitive, 50% standard | Workbook 5 |
| **Encryption - restricted data** | % restricted data encrypted | 100% | Workbook 5 |
| **Encryption - confidential data** | % confidential data encrypted | 95%+ | Workbook 5 |
| **Access control testing** | Penetration tests per year | 1+ (external) | Pen test reports |
| **Database least privilege** | % DB accounts with specific grants (not ALL) | 90%+ | Workbook 5 |
| **API rate limiting** | % APIs with rate limiting | 95%+ | Workbook 5 |
| **Cloud IAM least privilege** | % cloud policies using specific actions | 85%+ | Workbook 5 |
| **Configuration compliance** | % systems compliant with baselines | 90%+ | Workbook 5 |
| **Access violation incidents** | Unauthorized access attempts per month | <10 | Security logs |

### 12.2 Audit Evidence Requirements

**For ISO 27001:2022 A.8.3 audit**:

1. **Policy and procedures**: This document (ISMS-POL-A.8.2-3-5-S4)
2. **Permission audits**: Workbook 5 (file system, database, application, API permissions)
3. **Configuration compliance**: Configuration scan results, CIS benchmark compliance
4. **Encryption status**: Encryption inventory aligned with data classification
5. **Penetration testing**: Penetration test reports, remediation evidence
6. **Network segmentation**: Firewall rules (reference A.8.22 assessment)
7. **Cloud IAM**: Cloud IAM policy exports, permission reviews
8. **Default deny evidence**: Sample configurations showing default deny implementation

---

**END OF SECTION 4 (INFORMATION ACCESS RESTRICTION REQUIREMENTS - A.8.3)**

**Next Section**: ISMS-POL-A.8.2-3-5-S5 (Assessment Methodology and Evidence Framework)

---

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect | Initial information access restriction requirements (A.8.3) |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**

---


**Document ID**: ISMS-POL-A.8.2-3-5-S5  
**Title**: Assessment Methodology and Evidence Framework (ISO/IEC 27001:2022 Controls A.8.2, A.8.3, A.8.5)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISMS Assessment Lead | Initial assessment methodology for A.8.2/3/5 |

**Review Cycle**: Annual  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Assessment Review: Internal Audit Lead
- Technical Review: Security Architect

**Distribution**: Security team, internal audit, external auditors, compliance team  
**Related Documents**: 
- ISMS-POL-A.8.2-3-5-S1 through S4 (Policy requirements)
- ISMS-IMP-A.8.2-3-5-S5 (Security Assessment Implementation)
- All assessment workbooks (Workbook 1-5, Dashboard)

---

## 1. Assessment Framework Overview

### 1.1 Purpose and Scope

**Purpose**: Define unified assessment methodology for evaluating compliance and effectiveness of Authentication & Privileged Access Security Framework across controls A.8.2, A.8.3, and A.8.5.

**Assessment Objectives**:
1. Verify technical implementation of authentication, privileged access, and access restriction controls
2. Measure control effectiveness (not just control existence)
3. Identify security gaps requiring remediation
4. Collect evidence for ISO 27001:2022 audits (internal and external)
5. Track compliance trends over time

**Scope**: This assessment methodology covers:
- **A.8.5** - Secure Authentication (authentication mechanisms, MFA, SSO, passwords)
- **A.8.2** - Privileged Access Rights (PAM, admin tiering, privileged monitoring)
- **A.8.3** - Information Access Restriction (permissions, access enforcement)

### 1.2 Combined Assessment Rationale

**Why Unified Assessment?**

1. **Shared Identity Infrastructure**: All three controls use same identity systems (AD, Azure AD, Okta, PAM)
2. **Evidence Consolidation**: Single data collection serves multiple controls
3. **Efficiency**: 3x faster than three separate assessments
4. **Holistic View**: Authentication â†’ Privileged Access â†’ Access Enforcement forms complete security layer

**Assessment Independence**:

Despite unified methodology, each control maintains:
- Separate requirements verification (S2 for A.8.5, S3 for A.8.2, S4 for A.8.3)
- Individual compliance scoring (separate scores per control)
- Distinct evidence collection (clear mapping: evidence â†’ control)
- Statement of Applicability (SoA) clarity (auditors can assess each control independently)

---

## 2. Assessment Structure and Workbooks

### 2.1 Assessment Workbook Architecture

**5 Specialized Assessment Workbooks + 1 Consolidated Dashboard**:

| Workbook | Primary Control | Purpose | Key Metrics |
|----------|----------------|---------|-------------|
| **WB1: Authentication Inventory** | A.8.5 | Document authentication mechanisms by system | Auth method coverage, SSO adoption |
| **WB2: MFA Coverage** | A.8.5 | Track MFA enrollment and coverage | MFA coverage by user type, gaps |
| **WB3: Privileged Accounts** | A.8.2 | Inventory privileged accounts and tier classification | PAM coverage, tier isolation |
| **WB4: Privileged Monitoring** | A.8.2 | Track privileged access activity and reviews | Session recording, alert response |
| **WB5: Access Restrictions** | A.8.3 | Assess technical access control effectiveness | Permission compliance, pen test results |
| **Dashboard** | A.8.2/3/5 | Executive compliance overview | Overall scores, gap prioritization |

### 2.2 Workbook Integration Flow

```
Data Collection â†’ Individual Workbooks â†’ Consolidated Dashboard â†’ Executive Reporting

Workbook 1 (Auth Inventory) â”
Workbook 2 (MFA Coverage)   â”œâ†’ Dashboard â†’ Executive Summary
Workbook 3 (Priv Accounts)  â”œâ†’ Compliance Scores per Control
Workbook 4 (Priv Monitoring)â”œâ†’ Gap Prioritization
Workbook 5 (Access Controls)â”˜  Trend Analysis
```

### 2.3 Assessment Frequency

**Continuous Monitoring** (automated where possible):
- MFA enrollment status (daily updates)
- Authentication logs (real-time SIEM)
- Privileged access activity (real-time PAM logs)
- Permission changes (daily configuration scans)

**Monthly Reviews**:
- Privileged account inventory updates
- Failed authentication analysis
- Privileged access anomaly review

**Quarterly Assessments** (formal):
- Complete all 5 workbooks
- Privileged access rights review (A.8.2 requirement)
- Permission audits (sample of critical systems)
- Generate dashboard and executive report

**Annual Assessments** (comprehensive):
- Full system coverage (not just samples)
- Penetration testing (access control bypass attempts)
- Deep review of service accounts, break-glass accounts
- Admin tier classification review
- ISO 27001:2022 annual audit preparation

---

## 3. Workbook 1: Authentication Inventory & Methods (A.8.5)

### 3.1 Assessment Objectives

**Purpose**: Document authentication mechanisms across all systems and evaluate security posture.

**Key Questions**:
- What authentication methods are used? (password, MFA, SSO, certificate, biometric)
- Which systems use modern authentication protocols? (SAML, OAuth vs. legacy NTLM, Basic Auth)
- What is SSO adoption rate?
- Are password policies compliant with requirements?

### 3.2 Data Collection

**Systems to Inventory**:
- All user-facing systems (applications, web portals, VPNs)
- Infrastructure systems (servers, network devices, databases)
- Cloud platforms (AWS, Azure, GCP consoles)
- SaaS applications

**Data Points per System**:
- System name and description
- Authentication method (password-only, password+MFA, SSO, certificate, biometric)
- Authentication protocol (SAML, OAuth, OIDC, Kerberos, LDAP, RADIUS, Basic Auth)
- Authentication provider (Azure AD, Okta, AD, local, other)
- SSO integration status (integrated, not integrated, in progress)
- Password policy enforced (yes/no, policy details)
- MFA available (yes/no, MFA methods)

**Data Sources**:
- Identity provider reports (Azure AD, Okta application catalogs)
- Application inventory (IT asset management)
- Network discovery scans
- Manual documentation review

### 3.3 Assessment Criteria

**Compliance Scoring**:

| Authentication Method | Security Score | Rationale |
|----------------------|----------------|-----------|
| Password-only (no MFA option) | ðŸ”´ 0% | Unacceptable - vulnerable to credential compromise |
| Password-only (MFA available but not enforced) | ðŸŸ¡ 25% | Poor - MFA should be mandatory |
| Password + MFA (optional) | ðŸŸ¡ 50% | Marginal - MFA not enforced |
| Password + MFA (mandatory) | ðŸŸ¢ 75% | Good - strong authentication |
| SSO + MFA (mandatory) | ðŸŸ¢ 90% | Very Good - centralized + strong |
| Certificate-based + MFA | ðŸŸ¢ 95% | Excellent - phishing-resistant |
| Hardware token (FIDO2) + MFA | ðŸŸ¢ 100% | Excellent - strongest authentication |

**SSO Adoption Metrics**:
- Target: 90%+ of SaaS applications integrated with SSO
- Current: Calculate (SSO-integrated apps / total apps) Ã— 100%
- Gap: Applications not yet integrated with SSO

**Password Policy Compliance**:
- Minimum length 12 characters: Yes/No
- Complexity enforced: Yes/No
- Breach detection enabled: Yes/No
- Password expiration: Acceptable (disabled or 90+ days)

### 3.4 Evidence Collection

**Evidence for A.8.5 (Authentication)**:
- Authentication inventory report (Workbook 1 export)
- SSO application catalog screenshots
- Password policy configurations (GPO, Azure AD, Okta)
- Sample authentication logs

**Audit Value**:
- Demonstrates comprehensive authentication mechanism documentation
- Shows technology-agnostic assessment (works for any identity provider)
- Provides baseline for measuring SSO adoption progress

---

## 4. Workbook 2: MFA Coverage Assessment (A.8.5)

### 4.1 Assessment Objectives

**Purpose**: Measure multi-factor authentication coverage across user population and identify gaps.

**Key Questions**:
- What % of users have MFA enrolled?
- What % of privileged users have MFA? (Target: 100%)
- What % of remote access users have MFA? (Target: 100%)
- What MFA methods are used? (Hardware token, authenticator app, SMS)
- What are high-priority gaps? (Privileged users without MFA)

### 4.2 Data Collection

**User Population Segmentation**:
1. **Privileged users** (system admins, DBAs, security admins, cloud admins)
2. **Remote access users** (VPN users, external access)
3. **Standard internal users** (office-based, internal access only)
4. **Contractors/vendors** (temporary accounts)

**Data Points per User**:
- User ID and name
- User type (privileged, remote, standard, contractor)
- MFA enrolled (yes/no)
- MFA method (hardware token, authenticator app, push notification, SMS, biometric, none)
- MFA enrollment date
- Backup MFA method registered (yes/no)
- Last successful MFA authentication

**Data Sources**:
- Identity provider MFA reports (Azure AD, Okta MFA enrollment reports)
- Active Directory privileged group memberships
- VPN access logs (who authenticated to VPN)
- PAM solution user lists (privileged users)

### 4.3 Assessment Criteria

**MFA Coverage Targets**:

| User Type | MFA Target | Current Status | Gap |
|-----------|------------|----------------|-----|
| **Privileged users** | 100% MANDATORY | Calculate from data | High priority gap |
| **Remote access users** | 100% MANDATORY | Calculate from data | High priority gap |
| **Standard users** | 90%+ target | Calculate from data | Medium priority gap |
| **Contractors/vendors** | 100% MANDATORY | Calculate from data | High priority gap |

**Compliance Scoring**:
- ðŸŸ¢ Green (Compliant): â‰¥95% MFA coverage for user type
- ðŸŸ¡ Yellow (Partial): 75-94% MFA coverage
- ðŸ”´ Red (Non-Compliant): <75% MFA coverage

**MFA Method Quality**:

| MFA Method | Security Rating | Suitable For |
|------------|-----------------|--------------|
| Hardware token (FIDO2) | ðŸŸ¢ Excellent | Tier 0 privileged users (required) |
| Authenticator app (TOTP) | ðŸŸ¢ Good | Privileged users, standard users |
| Push notification | ðŸŸ¢ Good | Standard users (convenient) |
| Biometric | ðŸŸ¡ Acceptable | Mobile devices, workstation login |
| SMS | ðŸ”´ Poor | Backup only (not primary MFA) |

### 4.4 Gap Analysis

**High-Priority Gaps** (immediate remediation required):
- Privileged users without MFA (critical security risk)
- Remote access users without MFA (exposure to external threats)
- Service accounts without certificate-based auth (password-only service accounts)

**Medium-Priority Gaps**:
- Standard users without MFA (phishing risk)
- Users with SMS as primary MFA (upgrade to authenticator app)

**Gap Remediation Tracking**:
- Gap identified date
- User notified date
- Deadline for MFA enrollment (7 days for privileged, 30 days for standard)
- Remediation status (in progress, complete, overdue)
- Escalation (if overdue: notify manager, restrict access)

### 4.5 Evidence Collection

**Evidence for A.8.5 (Authentication)**:
- MFA enrollment report by user type (Workbook 2 export)
- MFA coverage trend chart (quarterly comparison)
- Gap remediation tracking (high-priority gaps addressed)
- NIS2 compliance evidence (MFA mandatory per Article 21(2)(e))

**Audit Value**:
- Demonstrates MFA deployment progress toward targets
- Shows prioritization (privileged users first, then all users)
- Provides regulatory compliance evidence (NIS2, FINMA, DORA)

---

## 5. Workbook 3: Privileged Account Inventory (A.8.2)

### 5.1 Assessment Objectives

**Purpose**: Maintain complete inventory of privileged accounts with admin tier classification and PAM coverage tracking.

**Key Questions**:
- How many privileged accounts exist? (Named, shared, service, break-glass)
- What admin tier is each account? (Tier 0, Tier 1, Tier 2)
- Which privileged accounts are in PAM vault? (Target: 100% of shared accounts)
- Do all privileged users have MFA? (Target: 100%)
- Are Tier 0 accounts using PAWs and hardware tokens?

### 5.2 Data Collection

**Privileged Account Discovery**:

**Windows Active Directory**:
- Domain Admins, Enterprise Admins, Schema Admins (Tier 0)
- Server Administrators, Backup Operators (Tier 1)
- Workstation administrators (Tier 2)
- Local Administrator accounts on servers/workstations

**Azure AD / Entra ID**:
- Global Administrator (Tier 0)
- Security Administrator, Compliance Administrator (Tier 0)
- Application Administrator, Cloud Application Administrator (Tier 1)

**AWS IAM**:
- Root account (Tier 0 - should be break-glass only)
- AdministratorAccess policy users (Tier 0)
- PowerUser policy users (Tier 1)

**Databases**:
- sa (SQL Server), SYSTEM (Oracle), postgres (PostgreSQL) - Tier 1
- DBA accounts - Tier 1

**Data Points per Privileged Account**:
- Account name (john.doe.admin, root, sa, Administrator)
- Account type (named, shared, service, break-glass)
- Privileged role (Windows admin, Linux admin, DBA, security admin, cloud admin)
- **Admin tier** (Tier 0, Tier 1, Tier 2, N/A)
- Owner (for named accounts) or responsible party (for shared/service)
- Systems/platforms (Windows servers, Linux servers, AWS, Azure, databases)
- Last password change date
- PAM vaulted (yes/no - for shared accounts)
- MFA enabled (yes/no - for named accounts)
- **Tier isolation compliance**: Has this Tier 0 account logged into Tier 1/2 systems? (violation count)

### 5.3 Admin Tier Classification

**Critical Requirement**: Every privileged account must be classified into tier.

**Tier 0 Accounts** (Domain/Enterprise/Critical):
- Domain Admins, Enterprise Admins, Schema Admins
- Azure Global Administrator, AWS root account
- SIEM administrators, PAM administrators
- Backup administrators (can restore any system)
- Certificate Authority administrators

**Tier 1 Accounts** (Server/Application):
- Server administrators (Windows server admin, Linux admin)
- Database administrators (SQL Server DBA, Oracle DBA)
- Application administrators (SAP admin, Salesforce admin)
- Virtualization administrators (VMware admin, Hyper-V admin)
- Cloud infrastructure admins (AWS EC2 admin, Azure VM admin)

**Tier 2 Accounts** (Workstation/Endpoint):
- Desktop support / Help desk (local admin on workstations)
- MDM administrators (Intune, Jamf - device management)
- Endpoint management (patch management for workstations)

### 5.4 Assessment Criteria

**PAM Coverage**:
- ðŸŸ¢ Target: 100% of shared privileged accounts in PAM vault
- Calculate: (Shared accounts in PAM / Total shared accounts) Ã— 100%

**Privileged MFA Coverage**:
- ðŸŸ¢ Target: 100% of privileged users with MFA
- Calculate: (Privileged users with MFA / Total privileged users) Ã— 100%

**Tier 0 Security Requirements**:
- Hardware MFA tokens: 100% of Tier 0 users (yes/no per user)
- PAW deployment: 100% of Tier 0 admins (yes/no per user)
- Tier isolation: Zero cross-tier violations (Tier 0 logging into Tier 1/2)

**Credential Rotation Compliance**:
- Shared accounts: Password changed within last 30 days (yes/no)
- Service accounts: Password changed within last 90 days (yes/no)
- Break-glass accounts: Password changed after each use (yes/no)

### 5.5 Evidence Collection

**Evidence for A.8.2 (Privileged Access)**:
- Privileged account inventory with tier classification (Workbook 3 export)
- PAM vault coverage report (% of shared accounts vaulted)
- MFA enrollment for privileged users (100% target)
- Tier 0 PAW deployment status
- Hardware MFA token assignment records
- Tier isolation compliance (cross-tier violation count = 0)
- Quarterly privileged access review attestations

**Audit Value**:
- Demonstrates complete privileged account visibility
- Shows admin tiering implementation (critical for preventing lateral movement)
- Provides evidence of PAM deployment and coverage
- Documents privileged access oversight (quarterly reviews)

---

## 6. Workbook 4: Privileged Access Monitoring (A.8.2)

### 6.1 Assessment Objectives

**Purpose**: Track privileged access activity, detect anomalies, and verify monitoring controls effectiveness.

**Key Questions**:
- Is privileged access being monitored? (session recording, logging, alerting)
- Are privileged sessions recorded? (Target: 90%+ coverage)
- Are privileged access alerts responding quickly? (Target: <30 min response)
- Are quarterly privileged access reviews completed? (Target: 100%)
- Are there tier isolation violations? (Target: zero violations)

### 6.2 Data Collection

**Privileged Access Activity Monitoring**:

**Data Points**:
- Privileged account used
- System accessed
- Login date/time (timestamp)
- Session duration
- Session recorded (yes/no)
- Off-hours access (yes/no - outside 8 AM - 6 PM business hours)
- Unusual location (yes/no - new location/IP never seen before)
- Commands executed (if logged)
- Alert generated (yes/no)
- Alert response time (minutes)

**Data Sources**:
- PAM solution session logs
- Active Directory Security Event Logs (Event ID 4672 - Special Privileges)
- Linux sudo logs (centralized via rsyslog)
- Database audit logs (privileged account usage)
- Cloud platform audit logs (AWS CloudTrail, Azure Activity Log)
- SIEM alerts (privileged access anomalies)

### 6.3 Privileged Access Anomalies

**Anomaly Detection**:

| Anomaly Type | Detection Method | Priority | Response Time Target |
|--------------|------------------|----------|---------------------|
| Off-hours privileged access | Login 10 PM - 6 AM or weekends | Medium | 1 hour |
| Unusual location | New country/city | High | 30 minutes |
| Tier 0 activity | ANY Tier 0 account use | High | 15 minutes |
| Tier isolation violation | Tier 0 account on Tier 1/2 system | Critical | 5 minutes |
| Failed privileged login | 3+ failed attempts | High | 15 minutes |
| Long session | Session >4 hours | Medium | 1 hour |
| Break-glass usage | Break-glass account login | Critical | Immediate |

**Anomaly Response Tracking**:
- Anomaly detected date/time
- Alert sent to (security team, SOC, on-call admin)
- Response initiated date/time
- Investigation findings (legitimate access or security incident)
- Resolution (approved, password reset required, account suspended)

### 6.4 Session Recording Coverage

**Session Recording Assessment**:

**Recording Targets**:
- ðŸŸ¢ 100% of Tier 0 sessions (mandatory)
- ðŸŸ¢ 90%+ of Tier 1 production sessions (highly recommended)
- ðŸŸ¡ 50%+ of Tier 2 sessions (recommended)

**Recording Quality**:
- Video recording (for RDP/GUI sessions)
- Keystroke logging (for SSH/CLI sessions)
- Recording retention: 90 days online, 1 year archived
- Recordings searchable (by user, system, date, commands)

### 6.5 Quarterly Privileged Access Reviews

**Review Completion Tracking**:

**For each quarterly review period**:
- Review period (Q1, Q2, Q3, Q4)
- Privileged users reviewed (count and %)
- Privileged access confirmed appropriate (count)
- Privileged access removed as no longer needed (count)
- Privileged access justified as exception (count)
- Manager attestations collected (yes/no per manager)
- Review completion date (within 30 days of quarter end?)

**Review Metrics**:
- ðŸŸ¢ Target: 100% of privileged users reviewed quarterly
- Access removal rate: 5-10% typical (continuous cleanup)
- Overdue reviews: 0 (all reviews completed on time)

### 6.6 Evidence Collection

**Evidence for A.8.2 (Privileged Access)**:
- Privileged access activity logs (Workbook 4 export)
- Session recording samples (demonstrate recording capability)
- Anomaly detection alerts and response times
- Tier isolation violation report (target: zero violations)
- Quarterly review completion attestations
- Alert response metrics (average response time <30 minutes)

**Audit Value**:
- Demonstrates privileged access is monitored (not just controlled)
- Shows timely response to suspicious privileged activity
- Provides evidence of quarterly review process (A.8.2 requirement)
- Documents tier isolation enforcement and monitoring

---

## 7. Workbook 5: Access Restriction Compliance (A.8.3)

### 7.1 Assessment Objectives

**Purpose**: Assess technical access control effectiveness across operating systems, databases, applications, and APIs.

**Key Questions**:
- Are file permissions configured with default deny? (Target: 95%+)
- Are database permissions following least privilege? (Target: 90%+ with specific grants)
- Are access controls tested? (Penetration testing, configuration audits)
- Is encryption deployed per data classification? (Target: 100% for restricted data)
- Are there access control vulnerabilities? (Target: zero high/critical findings)

### 7.2 Data Collection

**Multi-Layer Assessment**:

**1. Operating System Permissions**:
- Systems assessed (Windows servers, Linux servers, workstations)
- Permission audit date
- Default deny configured (yes/no)
- Permission compliance score (% compliant with baseline)
- Findings (overly permissive permissions, Everyone group with write access, etc.)

**2. Database Access Controls**:
- Databases assessed (SQL Server, Oracle, PostgreSQL, MySQL, MongoDB, etc.)
- Database accounts reviewed
- Least privilege compliance (% accounts with specific grants vs. db_owner/ALL)
- Unused accounts identified (no connections in 90 days)
- Service accounts with excessive privileges (count)

**3. Application Access Controls**:
- Applications assessed
- RBAC implemented (yes/no)
- Role-permission matrix documented (yes/no)
- User-role assignments reviewed (date)
- SoD (Segregation of Duties) violations (count)

**4. API Access Controls**:
- APIs assessed
- Authentication method (OAuth, API keys, certificates, none)
- Rate limiting configured (yes/no)
- Scope-based authorization (yes/no)
- API vulnerabilities (OWASP API Top 10)

**5. Cloud IAM Policies**:
- Cloud platform (AWS, Azure, GCP)
- IAM policies reviewed (count)
- Overly permissive policies (wildcard actions like s3:*, ec2:*)
- Unused roles/policies (no activity in 90 days)

### 7.3 Data Classification and Encryption

**Encryption Compliance by Classification**:

| Data Classification | Encryption Required | Current Status | Gap |
|---------------------|---------------------|----------------|-----|
| **Restricted** | At rest + in transit | Calculate from data | High priority |
| **Confidential** | At rest | Calculate from data | Medium priority |
| **Internal** | Recommended | Calculate from data | Low priority |
| **Public** | Not required | N/A | N/A |

**Encryption Technologies**:
- Full disk encryption (BitLocker, FileVault, LUKS)
- Database TDE (Transparent Data Encryption)
- File encryption (EFS, encrypted shares)
- TLS for data in transit (TLS 1.2+ minimum)

### 7.4 Access Control Testing Results

**Penetration Testing Findings**:

**Test Scope**:
- Access control bypass attempts (horizontal/vertical privilege escalation)
- API authorization bypass (IDOR vulnerabilities)
- File traversal attacks (../../../etc/passwd)
- SQL injection (database access control bypass)

**Finding Severity**:
- ðŸ”´ Critical: Direct access to restricted data without authentication
- ðŸ”´ High: Privilege escalation (standard user â†’ admin)
- ðŸŸ¡ Medium: Information disclosure (access to data outside assigned scope)
- ðŸŸ¢ Low: Minor configuration issues

**Remediation Tracking**:
- Finding ID and description
- Severity (critical, high, medium, low)
- Identified date
- Remediation deadline (30 days for critical/high, 90 days for medium, 180 days for low)
- Remediation status (open, in progress, resolved, verified)
- Re-test date (verify fix works)

### 7.5 Assessment Criteria

**Access Control Compliance Scoring**:

| Metric | Target | Scoring |
|--------|--------|---------|
| Systems with default deny | 95%+ | ðŸŸ¢ â‰¥95%, ðŸŸ¡ 85-94%, ðŸ”´ <85% |
| Database least privilege | 90%+ | ðŸŸ¢ â‰¥90%, ðŸŸ¡ 75-89%, ðŸ”´ <75% |
| APIs with authentication | 100% | ðŸŸ¢ 100%, ðŸ”´ <100% (critical) |
| Encryption - restricted data | 100% | ðŸŸ¢ 100%, ðŸ”´ <100% (critical) |
| Pen test critical findings | 0 | ðŸŸ¢ 0, ðŸ”´ >0 (unacceptable) |
| Pen test high findings | <3 | ðŸŸ¢ 0-2, ðŸŸ¡ 3-5, ðŸ”´ >5 |

### 7.6 Evidence Collection

**Evidence for A.8.3 (Access Restriction)**:
- Permission audit reports (file system, database, application) - Workbook 5 export
- Configuration compliance scan results (CIS benchmarks)
- Penetration test reports (access control testing)
- Encryption inventory by data classification
- Finding remediation tracking (critical/high findings resolved)
- Network segmentation documentation (firewall rules - reference A.8.22)

**Audit Value**:
- Demonstrates technical access controls are assessed (not just documented)
- Shows access control effectiveness testing (penetration testing)
- Provides evidence of encryption deployment per data classification
- Documents remediation of access control vulnerabilities

---

## 8. Consolidated Dashboard

### 8.1 Dashboard Purpose

**Purpose**: Executive-level view of authentication and privileged access security compliance across all three controls (A.8.2, A.8.3, A.8.5).

**Dashboard Consumers**:
- CISO and security leadership (compliance status, risk prioritization)
- Internal audit (evidence for ISO 27001:2022 audit)
- External auditors (Statement of Applicability verification)
- Management (security investment justification)

### 8.2 Dashboard Structure

**Section 1: Overall Compliance Summary**

- **Overall Authentication & PAM Security Score**: Weighted average of three control scores
  - A.8.5 (Authentication) score: Weight 30%
  - A.8.2 (Privileged Access) score: Weight 40% (highest risk)
  - A.8.3 (Access Restriction) score: Weight 30%

- **Compliance Status**: ðŸŸ¢ Compliant (â‰¥90%), ðŸŸ¡ Partial (75-89%), ðŸ”´ Non-Compliant (<75%)

**Section 2: Control-Specific Scores**

**A.8.5 - Secure Authentication**:
- MFA coverage: Overall % and by user type (privileged, remote, standard)
- SSO adoption: % of applications integrated with SSO
- Password policy compliance: % systems with compliant password policies
- Authentication security score: 0-100%

**A.8.2 - Privileged Access Rights**:
- Privileged MFA coverage: % privileged users with MFA (target 100%)
- PAM vault coverage: % shared accounts in PAM vault (target 100%)
- Session recording coverage: % privileged sessions recorded
- Tier 0 security: % Tier 0 with PAWs and hardware MFA
- Tier isolation compliance: Cross-tier violation count (target 0)
- Quarterly review completion: % privileged users reviewed
- Privileged access score: 0-100%

**A.8.3 - Information Access Restriction**:
- Systems with default deny: % systems configured default deny
- Database least privilege: % DB accounts with specific grants
- Encryption compliance: % by data classification (restricted, confidential)
- Penetration test findings: Critical/high findings count
- Access restriction score: 0-100%

**Section 3: Critical Gaps Requiring Remediation**

**High-Priority Gaps** (top 10 most critical):
1. Privileged users without MFA (count) - CRITICAL RISK
2. Tier 0 accounts without PAWs (count) - CRITICAL RISK
3. Shared privileged accounts not in PAM vault (count) - HIGH RISK
4. Access control penetration test critical findings (count) - HIGH RISK
5. Restricted data not encrypted (count) - HIGH RISK
6. Tier isolation violations (count) - HIGH RISK
7. Standard users without MFA (count) - MEDIUM RISK
8. Applications not integrated with SSO (count) - MEDIUM RISK
9. Privileged sessions not recorded (count) - MEDIUM RISK
10. Database accounts with excessive privileges (count) - MEDIUM RISK

**Section 4: Compliance Trends**

- Quarterly trend charts:
  - MFA coverage trend (increasing over time)
  - PAM vault coverage trend
  - Tier isolation compliance trend
  - Overall security score trend

**Section 5: Evidence Summary**

- Total evidence items collected (count across all workbooks)
- Evidence completeness: % of required evidence collected
- Evidence freshness: Date of last assessment per workbook
- Next scheduled assessment: When is next quarterly assessment due?

### 8.3 Dashboard Generation

**Consolidation Logic**:

Dashboard script imports data from all 5 workbooks:
- Import Workbook 1 (Authentication Inventory) â†’ SSO adoption, auth method distribution
- Import Workbook 2 (MFA Coverage) â†’ MFA coverage by user type
- Import Workbook 3 (Privileged Accounts) â†’ PAM coverage, tier classification, MFA for privileged
- Import Workbook 4 (Privileged Monitoring) â†’ Session recording, alert response, reviews
- Import Workbook 5 (Access Restrictions) â†’ Permission compliance, encryption, pen test results

**Automated Calculations**:
- Calculate weighted scores per control
- Identify top 10 critical gaps (by risk priority)
- Generate trend charts (if historical data available)
- Flag overdue remediation items

### 8.4 Evidence Collection

**Evidence for Combined Assessment (A.8.2/3/5)**:
- Executive dashboard (consolidated view)
- All 5 workbooks (detailed evidence per control)
- Quarterly assessment reports
- Trend analysis (compliance improving over time)
- Gap remediation tracking

**Audit Value**:
- Provides executive summary for auditors (high-level view)
- Demonstrates unified assessment methodology
- Shows compliance trends (continuous improvement)
- Clear mapping: Dashboard â†’ Workbooks â†’ Individual Controls â†’ ISO Requirements

---

## 9. Assessment Execution Procedures

### 9.1 Quarterly Assessment Schedule

**Assessment Timeline** (30-day cycle per quarter):

**Week 1: Data Collection**
- Days 1-3: Export data from identity providers (Azure AD, Okta, AD)
- Days 4-5: Export data from PAM solutions (CyberArk, BeyondTrust)
- Days 6-7: Run configuration scans (CIS benchmarks, custom scripts)

**Week 2: Workbook Population**
- Days 8-10: Populate Workbooks 1-2 (Authentication, MFA)
- Days 11-13: Populate Workbooks 3-4 (Privileged Accounts, Monitoring)
- Day 14: Populate Workbook 5 (Access Restrictions)

**Week 3: Analysis and Review**
- Days 15-17: Analyze data, identify gaps, prioritize remediation
- Days 18-19: Generate dashboard, prepare executive report
- Days 20-21: Internal review (security team validates findings)

**Week 4: Reporting and Remediation Planning**
- Days 22-24: Present findings to CISO and security leadership
- Days 25-27: Develop remediation plans for critical gaps
- Days 28-30: Initiate remediation (assign owners, set deadlines)

### 9.2 Data Sources and Integration

**Identity Provider APIs**:
- **Azure AD Graph API**: MFA enrollment, authentication methods, privileged role assignments
- **Okta API**: MFA enrollment, authentication logs, application integrations
- **Active Directory PowerShell**: Privileged group memberships, account attributes

**PAM Solution APIs**:
- **CyberArk REST API**: Vaulted accounts, session recordings, check-out logs
- **BeyondTrust API**: Session recordings, privileged access activity

**SIEM Integration**:
- **Splunk/Datadog/Elastic**: Authentication logs, privileged access logs, security alerts
- **Query for**: Failed authentication attempts, privileged access anomalies, tier isolation violations

**Configuration Management**:
- **Ansible/PowerShell DSC**: Configuration compliance (file permissions, database grants)
- **Cloud APIs**: AWS IAM policies, Azure RBAC assignments, GCP IAM bindings

**Manual Data Collection** (where automation unavailable):
- Service account inventory (spreadsheet from application teams)
- Break-glass account documentation (sealed envelopes verification)
- Permission matrices (documented by system owners)

### 9.3 Assessment Roles and Responsibilities

| Role | Responsibilities |
|------|------------------|
| **CISO** | Approve assessment methodology, review findings, prioritize remediation |
| **Security Architect** | Design assessment procedures, interpret results, recommend controls |
| **IAM Lead** | Execute authentication/MFA assessments (WB1, WB2), provide identity data |
| **PAM Administrator** | Execute privileged access assessments (WB3, WB4), provide PAM data |
| **Systems Administrators** | Provide access control data (WB5), execute configuration audits |
| **Internal Audit** | Verify assessment methodology, validate evidence quality |
| **System Owners** | Attest to access control configurations, approve permission matrices |

---

## 10. Evidence Management

### 10.1 Evidence Collection Requirements

**Evidence Repository Structure**:

```
ISMS-A.8.2-3-5-Evidence/
â”œâ”€â”€ 2024-Q1/
â”‚   â”œâ”€â”€ Workbook-1-Authentication-Inventory.xlsx
â”‚   â”œâ”€â”€ Workbook-2-MFA-Coverage.xlsx
â”‚   â”œâ”€â”€ Workbook-3-Privileged-Accounts.xlsx
â”‚   â”œâ”€â”€ Workbook-4-Privileged-Monitoring.xlsx
â”‚   â”œâ”€â”€ Workbook-5-Access-Restrictions.xlsx
â”‚   â”œâ”€â”€ Dashboard-Authentication-PAM.xlsx
â”‚   â”œâ”€â”€ Executive-Report-Q1-2024.pdf
â”‚   â””â”€â”€ Raw-Data/
â”‚       â”œâ”€â”€ AzureAD-MFA-Export.csv
â”‚       â”œâ”€â”€ PAM-Session-Logs.csv
â”‚       â”œâ”€â”€ Privileged-Access-Review-Attestations.pdf
â”‚       â””â”€â”€ Penetration-Test-Report.pdf
â”œâ”€â”€ 2024-Q2/
â”‚   â””â”€â”€ [same structure]
â””â”€â”€ Annual-Reports/
    â””â”€â”€ ISO27001-Annual-Audit-2024.pdf
```

### 10.2 Evidence Retention

**Retention Requirements**:
- **Current year**: All workbooks and raw data (immediate access)
- **Previous 2 years**: Archived workbooks (compliance audits)
- **Older than 3 years**: Quarterly summaries only (historical trends)

**Evidence Access Control**:
- Evidence contains sensitive data (privileged account lists, security vulnerabilities)
- Access restricted to: Security team, internal audit, external auditors (with NDA)
- Evidence stored in secure location (encrypted file share)

### 10.3 Evidence Quality Assurance

**Quality Checks**:
1. **Completeness**: All required data fields populated (no blank cells for mandatory fields)
2. **Accuracy**: Data validated against source systems (spot checks)
3. **Timeliness**: Assessment data current (not older than 30 days at time of report)
4. **Consistency**: Data consistent across workbooks (e.g., privileged user count matches in WB2, WB3, WB4)

**Validation Procedures**:
- Automated validation script checks workbook data quality
- Manual review by second security team member
- Internal audit spot-checks (random sample of 10% of data verified against source)

---

## 11. Continuous Improvement

### 11.1 Assessment Methodology Updates

**Annual Review**:
- Review assessment methodology effectiveness (did assessments identify real security gaps?)
- Update workbook templates (add new data fields, improve calculations)
- Incorporate lessons learned (what worked well, what didn't)
- Align with updated regulatory requirements (new NIS2 guidance, FINMA circulars)

**Triggers for Interim Updates**:
- New technology deployment (new authentication method, new PAM solution)
- Regulatory changes (new compliance requirements)
- Security incidents (assessment should have detected the issue)
- Auditor feedback (external auditors recommend improvements)

### 11.2 Automation Opportunities

**Current Manual Processes** (candidates for automation):
- Data export from identity providers â†’ Automate with API scripts
- Workbook data entry â†’ Automate with Python scripts (direct data import)
- Configuration scanning â†’ Automate with Ansible/PowerShell scheduled tasks
- Dashboard generation â†’ Automate with Python script (reads all 5 workbooks, generates dashboard)

**Automation Benefits**:
- Reduce assessment time (30 days â†’ 7 days with full automation)
- Improve data accuracy (eliminate manual data entry errors)
- Enable more frequent assessments (monthly instead of quarterly)
- Real-time dashboards (dashboard updates daily instead of quarterly)

---

## 12. Integration with Broader ISMS

### 12.1 Integration with Other Controls

**Assessment Synergies**:

**A.5.15-16-18 (Identity & Access Management)**:
- User provisioning (A.5.16) â†’ Feeds authentication assessment (WB1, WB2)
- Access rights management (A.5.18) â†’ Quarterly reviews align with privileged access reviews (WB4)

**A.8.16 (Monitoring)**:
- SIEM alerts â†’ Feed privileged access monitoring (WB4)
- Authentication logs â†’ Feed authentication assessment (WB1)

**A.8.15 (Logging)**:
- Log retention â†’ Supports audit evidence requirements

**A.8.22 (Network Segmentation)**:
- Firewall rules â†’ Support access restriction assessment (WB5)

### 12.2 Integration with Risk Management

**Risk Assessment Integration**:
- Assessment findings â†’ Update risk register (privileged access risks)
- Critical gaps â†’ Escalate to risk management (risk acceptance or mitigation)
- Compliance scores â†’ Input to overall information security risk scoring

**Risk Mitigation Tracking**:
- Gap remediation plans â†’ Risk treatment plans
- Remediation completion â†’ Risk reduction evidence

---

## 13. Regulatory and Audit Considerations

### 13.1 ISO 27001:2022 Annual Audit Preparation

**Assessment Evidence for External Auditors**:

**For A.8.5 (Secure Authentication)**:
- Policy: ISMS-POL-A.8.2-3-5-S2
- Evidence: Workbook 1 (Authentication Inventory), Workbook 2 (MFA Coverage)
- Demonstrate: MFA deployment progress, SSO adoption, password policy compliance

**For A.8.2 (Privileged Access Rights)**:
- Policy: ISMS-POL-A.8.2-3-5-S3
- Evidence: Workbook 3 (Privileged Accounts), Workbook 4 (Privileged Monitoring)
- Demonstrate: PAM deployment, admin tiering, session recording, quarterly reviews

**For A.8.3 (Information Access Restriction)**:
- Policy: ISMS-POL-A.8.2-3-5-S4
- Evidence: Workbook 5 (Access Restrictions), penetration test reports
- Demonstrate: Permission audits, configuration compliance, encryption deployment, access control testing

**Audit Interview Preparation**:
- Security team can articulate assessment methodology
- Examples of gap identification and remediation
- Trend analysis showing continuous improvement

### 13.2 Regulatory Compliance Evidence

**NIS2 Compliance** (if applicable):
- **Article 21(2)(e)**: MFA deployment â†’ Workbook 2 shows MFA coverage (must be >0% and increasing)
- **Article 21(2)(d)**: Access control policies â†’ All policy sections S2, S3, S4

**FINMA Compliance** (if applicable):
- **Margin 56**: Authentication for critical systems â†’ Workbook 1 shows authentication mechanisms
- **Margin 63-72**: Logging and monitoring â†’ Workbook 4 shows privileged access monitoring

**GDPR Article 32** (if applicable):
- Security of processing â†’ Assessment demonstrates technical security measures (MFA, access controls, encryption)

---

**END OF SECTION 5 (ASSESSMENT METHODOLOGY AND EVIDENCE FRAMEWORK)**

**POLICY SUITE COMPLETE**

All 5 policy sections (S1-S5) now complete. Next deliverables: Implementation guides and assessment scripts.

---

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISMS Assessment Lead | Initial assessment methodology for A.8.2/3/5 |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**
---



---

## 3. Governance & Compliance

### 3.1 Roles & Responsibilities

[Organization] SHALL assign clear accountability for authentication and privileged access security:

**Executive Management**:
- Approve authentication and privileged access security policy
- Allocate budget for PAM solutions, MFA deployment, security tools
- Escalation point for major privileged access incidents
- Review privileged access security metrics (quarterly Board reporting)

**Chief Information Security Officer (CISO)**:
- Overall accountability for authentication and privileged access security
- Approve PAM solution selection
- Approve MFA deployment strategy
- Approve Admin Tiering Model implementation
- Approve privileged access exceptions
- Review privileged access metrics (monthly)
- Escalate privileged access security issues to Executive Management

**Security Team**:
- Implement MFA deployment (rollout, user enrollment, monitoring)
- Implement PAM solution (deployment, configuration, maintenance)
- Implement Admin Tiering Model (tier classification, enforcement, monitoring)
- Monitor authentication and privileged access logs (SIEM monitoring, alert response)
- Conduct privileged access reviews (quarterly reviews, gap remediation)
- Respond to credential compromise incidents
- Security awareness training (authentication security, privileged access risks)

**IT Operations**:
- Implement authentication systems (Azure AD, Okta, Active Directory)
- Configure authentication policies (password policies, MFA enrollment)
- Implement technical access controls (file permissions, database grants, firewall rules)
- Deploy dedicated admin workstations (PAWs, jump servers)
- Support PAM solution (operational support, break-fix)
- Support MFA deployment (user enrollment support, device replacement)

**System Owners**:
- Define access requirements for owned systems (who needs access, privilege level)
- Approve privileged access requests for owned systems
- Review privileged access for owned systems (quarterly access reviews)
- Verify access control configurations for owned systems (permission audits)

**Application Owners**:
- Define application access requirements (application roles, permissions)
- Approve application administrator access
- Review application access rights (quarterly reviews)

**Database Administrators (DBAs)**:
- Implement database access controls (grants, roles, row-level security)
- Review database permissions (quarterly audits)
- Monitor database access (privileged database access, unusual queries)

**Network Administrators**:
- Implement network segmentation (VLANs, firewall rules)
- Configure network access controls (inter-zone traffic, access restrictions)
- Review network access control configurations (quarterly audits)

**Managers**:
- Approve privileged access requests for direct reports
- Conduct privileged access reviews for direct reports (quarterly)
- Notify Security Team of personnel changes (leaver, role change)

**Users**:
- Protect authentication credentials (passwords, MFA devices)
- Use separate privileged accounts for admin tasks (not daily work)
- Report credential compromise immediately (suspected or confirmed)
- Comply with authentication and privileged access policies

**Detailed RACI matrix documented in ISMS-IMP-A.8.2-3-5 Implementation Assessment Suite.**

### 3.2 Assessment and Verification

[Organization] verifies authentication and privileged access control effectiveness through structured assessment framework:

**Assessment Framework Overview**:

- **Assessment Approach**: 6 assessment workbooks + 1 consolidated dashboard
- **Assessment Frequency**: 
  - Monthly: Authentication inventory updates, MFA enrollment tracking, privileged account inventory
  - Quarterly: Comprehensive assessments (all 6 workbooks), formal compliance reporting
  - Annual: Deep assessments, penetration testing, full compliance validation
- **Assessment Ownership**: Security Team leads, IT Operations provides data, Internal Audit verifies

**Assessment Workbooks**:

| Workbook | Primary Control | Purpose | Update Frequency |
|----------|----------------|---------|------------------|
| **IMP.1 - Authentication Inventory** | A.8.5 | Document authentication mechanisms by system | Monthly |
| **IMP.2 - MFA Coverage Assessment** | A.8.5 | Track MFA enrollment and coverage by user type | Monthly |
| **IMP.3 - Privileged Account Inventory** | A.8.2 | Inventory privileged accounts, tier classification, PAM coverage | Monthly |
| **IMP.4 - Privileged Monitoring Assessment** | A.8.2 | Track privileged access activity, session recording, reviews | Quarterly |
| **IMP.5 - Access Restrictions Assessment** | A.8.3 | Assess technical access control implementation and effectiveness | Quarterly |
| **IMP.6 - Compliance Dashboard** | A.8.2/3/5 | Executive compliance overview, consolidated metrics | Monthly |

**Evidence Requirements**:

Evidence SHALL be collected per control for audit purposes:

**Control A.8.5 (Secure Authentication)**:
- Authentication mechanism inventory (systems and authentication methods)
- MFA enrollment records (user MFA enrollment status, MFA methods)
- Password policy configurations (system password policy settings)
- SSO integration documentation (applications integrated with SSO)
- Authentication logs (successful/failed authentication events)
- Credential compromise response records (incident reports, remediation actions)

**Control A.8.2 (Privileged Access Rights)**:
- Privileged user inventory (privileged accounts, owners, justifications)
- Privileged account classifications (named, shared, service, break-glass, tier assignments)
- PAM solution documentation (PAM deployment, vaulting coverage, session recording)
- Admin Tiering Model documentation (tier classifications, tier isolation enforcement)
- Privileged access logs (privileged login events, privileged commands, session recordings)
- Privileged access review records (quarterly reviews, approval records, remediation actions)

**Control A.8.3 (Information Access Restriction)**:
- Technical access control configurations (file permissions, database grants, application roles, API policies)
- Data classification and access alignment (classification levels and corresponding access restrictions)
- Network segmentation documentation (network zones, firewall rules, VLANs)
- Encryption implementation records (encryption at rest, encryption in transit)
- Permission audit results (file system audits, database audits, configuration audits)
- Penetration testing reports (access control bypass testing, findings, remediation)

**Assessment Procedures**: Detailed assessment procedures, including data collection methods, compliance calculation methodologies, and evidence requirements, are documented in ISMS-IMP-A.8.2-3-5 (Implementation Assessment Suite).

### 3.3 Exception Management

[Organization] manages authentication and privileged access exceptions through formal approval and periodic review:

**Exception Request Process**:

1. **Exception Identification**: Situation where standard authentication/privileged access policy cannot be followed
2. **Business Justification**: Requester documents why exception necessary, business impact if denied
3. **Risk Assessment**: Security Team assesses risk of exception, proposes compensating controls
4. **Approval**: CISO approves exception with documented compensating controls
5. **Documentation**: Exception recorded in exception register (exception ID, justification, risk, compensating controls, approval date, expiry date)
6. **Implementation**: Compensating controls implemented and verified
7. **Review**: Exception reviewed quarterly (re-assess necessity, verify compensating controls effective)
8. **Expiration**: Exception expires on expiry date OR when technical limitation remediated

**Common Exception Scenarios**:

- **MFA Exemption**: Legacy system cannot support MFA (compensating control: network restriction, enhanced monitoring)
- **Shared Admin Account**: Application requires shared admin account (compensating control: PAM vaulting, session recording mandatory)
- **Password Policy Exception**: System cannot support modern password policy (compensating control: MFA required, enhanced monitoring)
- **Tier Isolation Exception**: Technical limitation prevents tier isolation (compensating control: enhanced monitoring, JIT access)
- **Service Account Non-Rotation**: Service account password cannot be rotated due to hardcoded password (compensating control: network restriction, migration plan documented)

**Exception Approval Authority**:

- Standard Exceptions: CISO approval
- High-Risk Exceptions: CISO + Executive Management approval
- Emergency Exceptions: Temporary CISO approval, formal approval within 5 business days

**Exception Monitoring**:

- Exceptions tracked in exception register (accessible to auditors)
- Exception expiry monitored (alerts before expiration, remediation tracking)
- Exception compliance monitored (compensating controls verified quarterly)

### 3.4 Incident Response

[Organization] responds to authentication and privileged access security incidents per ISMS incident management framework (A.5.24-27):

**Incident Classification**:

Authentication and privileged access incidents classified by severity:

**Severity 1 (Critical)**:
- Tier 0 credential compromise (domain admin, enterprise admin, cloud global admin)
- Break-glass account unauthorized usage
- PAM system compromise
- Authentication system outage (complete authentication failure)
- Widespread MFA bypass

**Severity 2 (High)**:
- Tier 1 credential compromise (server admin, DBA, application admin)
- Privileged account unauthorized usage
- MFA compromise (attacker bypassed MFA)
- Shared admin account credential leak
- Multiple failed privileged access attempts (brute-force attack)

**Severity 3 (Medium)**:
- Standard user credential compromise
- Single MFA bypass incident
- Unauthorized access to restricted data (successful access control bypass)
- Tier 2 credential compromise (workstation admin)

**Severity 4 (Low)**:
- Failed unauthorized access attempts (detected and blocked)
- Suspicious authentication patterns (investigated, no confirmed compromise)

**Incident Response Procedures**:

Authentication and privileged access incidents SHALL follow standard incident response:

1. **Detection**: Monitoring alerts, user reports, security tool alerts
2. **Containment**: 
   - Disable compromised credentials immediately
   - Isolate compromised systems
   - Revoke active sessions
3. **Investigation**: 
   - Review authentication logs (when/where/how)
   - Identify accessed systems/data
   - Assess blast radius
4. **Eradication**: 
   - Remove attacker access
   - Reset compromised credentials
   - Patch vulnerabilities exploited
5. **Recovery**: 
   - Restore systems to known-good state
   - Re-enable accounts with new credentials
   - Verify no persistent access
6. **Lessons Learned**: 
   - Post-incident review
   - Improve authentication/privileged access controls
   - Update monitoring rules

**Incident Escalation**:

- Severity 1: Immediate escalation to CISO, Executive Management notification within 1 hour
- Severity 2: Escalation to CISO within 4 hours
- Severity 3: Security Team handles, CISO notification within 24 hours
- Severity 4: Security Team handles, monthly reporting to CISO

**Incident Response Documentation**:

Authentication and privileged access incidents SHALL be documented:
- Incident timeline (detection, containment, resolution)
- Impact assessment (systems affected, data accessed, credential exposure)
- Response actions (credentials reset, systems isolated, monitoring enhanced)
- Lessons learned (what went wrong, how to prevent recurrence)

**Implementation Note**: Detailed incident response procedures documented in ISMS-IMP-A.8.2-3-5.4 (Privileged Monitoring Assessment).

### 3.5 Policy Governance

**Review Frequency**: Annual minimum OR triggered by significant changes

**Triggers for Policy Review**:
- New authentication technology adoption (passwordless, biometric, FIDO2)
- New PAM solution deployment
- Regulatory changes (new MFA mandates, new privileged access requirements)
- Significant security incidents (Tier 0 compromise, authentication bypass)
- Organizational changes (merger, acquisition, new service offerings)
- Technology changes (cloud migration, identity provider change)

**Approval Process**:
1. CISO drafts policy updates
2. Legal/Compliance review (regulatory compliance verification)
3. IT Operations review (technical feasibility verification)
4. Security Team review (implementation approach verification)
5. Executive Management approval (final authority)

**Version Control**:
- Major version (X.0): Substantial policy changes (new controls, significant requirement changes)
- Minor version (X.Y): Clarifications, technical updates, regulatory reference updates

**Communication**: Policy updates communicated via:
- Policy portal update
- Email to all stakeholders
- Security awareness training update
- Privileged user notification (for privileged access policy changes)

---

## 4. Implementation & References

### 4.1 Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):
- Authentication and privileged access controls selected based on [Organization]'s risk assessment
- Authentication risks (A.8.5), privileged access risks (A.8.2), and access restriction risks (A.8.3) identified and assessed
- Risk treatment decisions document which controls are implemented and at what level
- Residual risks from incomplete authentication/privileged access controls tracked in risk register

**Statement of Applicability** (ISO 27001 Clause 6.1.3):
- Controls A.8.2, A.8.3, A.8.5 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported
- Control effectiveness measured through compliance assessments

**This policy supports the following SoA entries**:

| Control | Status | Justification | Implementation |
|---------|--------|---------------|----------------|
| **A.8.5 - Secure Authentication** | ☑ Applicable | [Organization] requires reliable user authentication to prevent unauthorized access | Section 2.1, ISMS-IMP-A.8.2-3-5 |
| **A.8.2 - Privileged Access Rights** | ☑ Applicable | [Organization] requires privileged access management to prevent privilege abuse | Section 2.2, ISMS-IMP-A.8.2-3-5 |
| **A.8.3 - Information Access Restriction** | ☑ Applicable | [Organization] requires technical access controls to enforce access policies | Section 2.3, ISMS-IMP-A.8.2-3-5 |

**Related Controls** (Integration Points):

- **A.5.15-16-18 (Identity & Access Management)**: IAM foundation → Authentication/PAM implements technical security layer
- **A.8.16 (Monitoring Activities)**: Authentication and privileged access events monitored via SIEM
- **A.8.15 (Logging)**: Authentication, privileged access, access restriction events logged
- **A.8.24 (Use of Cryptography)**: Encryption used for authentication (certificates) and access restriction
- **A.5.7 (Threat Intelligence)**: Compromised credentials from threat intel feeds trigger immediate response
- **A.5.24-27 (Incident Management)**: Credential compromise and privileged access incidents managed per incident framework
- **A.8.8 (Technical Vulnerabilities Management)**: Authentication vulnerabilities (weak protocols, unpatched systems) managed per vulnerability framework
- **A.8.20 (Networks Security)**: Network device authentication integrated with overall authentication framework
- **A.8.22 (Segregation of Networks)**: Network segmentation supports access restriction (A.8.3)

### 4.2 Implementation Resources

**Implementation Assessment Suite** (ISMS-IMP-A.8.2-3-5):

| Document | Purpose | Target Audience | Review Frequency |
|----------|---------|----------------|------------------|
| **ISMS-IMP-A.8.2-3-5.1** | Authentication Inventory (A.8.5) | Security Team, IT Operations, System Owners | Monthly |
| **ISMS-IMP-A.8.2-3-5.2** | MFA Coverage Assessment (A.8.5) | Security Team, IT Operations, CISO | Monthly |
| **ISMS-IMP-A.8.2-3-5.3** | Privileged Account Inventory (A.8.2) | Security Team, IAM Team, Privileged Users | Monthly |
| **ISMS-IMP-A.8.2-3-5.4** | Privileged Monitoring Assessment (A.8.2) | Security Team, SOC, CISO | Quarterly |
| **ISMS-IMP-A.8.2-3-5.5** | Access Restrictions Assessment (A.8.3) | Security Team, System Owners, Network Team | Quarterly |
| **ISMS-IMP-A.8.2-3-5.6** | Compliance Dashboard (A.8.2/3/5) | CISO, Executive Management, Auditors | Monthly |

**Assessment Tools**:
- Python-generated Excel workbooks with automated compliance calculations
- Evidence registers and gap analysis templates embedded in workbooks
- Automated compliance scoring and trend analysis
- Remediation tracking and executive reporting

**Supporting Materials**:
- Exception request templates
- Privileged access request templates
- MFA enrollment guides (user-facing)
- Admin Tiering quick reference (Annex A)
- PAM solution comparison criteria (ISMS-CTX-A.8.2-3-5)
- Authentication/PAM technology landscape (ISMS-CTX-A.8.2-3-5)

**Reference Documents**:
- **ISMS-REF-A.5.23**: Cloud Service Provider Registry (identity and authentication provider assessment)
- **ISMS-CTX-A.8.2-3-5**: Authentication & PAM Technology Landscape (technology trends, solution comparisons)

### 4.3 Regulatory Mapping

This policy addresses authentication and privileged access requirements from multiple regulatory frameworks:

| Requirement Category | Swiss FADP | EU GDPR | ISO 27001 | FINMA* | DORA* | NIS2* | PCI DSS* |
|---------------------|-----------|---------|-----------|--------|-------|-------|----------|
| **Authentication Mechanisms** | Art. 8 | Art. 32 | A.8.5 | Margin 56 | Art. 9(3) | Art. 21(2)(d) | Req. 8 |
| **Multi-Factor Authentication** | Art. 8 | Art. 32 | A.8.5 | Margin 56 | Art. 9(3) | **Art. 21(2)(e)** | Req. 8.3 |
| **Privileged Access Management** | Art. 8 | Art. 32 | A.8.2 | Margin 56, 63 | Art. 10 | Art. 21(2)(f) | Req. 7 |
| **Privileged Access Monitoring** | Art. 8 | Art. 32 | A.8.2 | Margin 63-72 | Art. 10 | Art. 21(2)(f) | Req. 10 |
| **Technical Access Controls** | Art. 8 | Art. 32 | A.8.3 | Margin 56 | Art. 6 | Art. 21(2)(d) | Req. 7 |
| **Access Control Logging** | Art. 8 | Art. 32 | A.8.3 | Margin 63-72 | Art. 10 | Art. 21(2)(d) | Req. 10 |

*Conditional applicability per ISMS-POL-00

**Note**: Specific regulatory interpretation and compliance verification procedures are documented in ISMS-IMP-A.8.2-3-5 (Implementation Assessment Suite).

### 4.4 Training & Awareness

**Security Awareness** (all users):
- **Audience**: All employees, contractors, temporary personnel
- **Content**: 
  - Password security (strong passwords, password managers)
  - MFA importance (why MFA matters, how to use MFA)
  - Phishing awareness (credential theft via phishing)
  - Social engineering (pretexting for credentials)
  - Credential protection (don't share passwords, don't write passwords down)
  - Incident reporting (suspected credential compromise)
- **Frequency**: Annual security awareness training (mandatory)
- **Delivery**: E-learning modules, mandatory completion tracked
- **Verification**: Training completion tracked in HR system, attestation recorded

**Privileged User Training** (administrators):
- **Audience**: All users with privileged access (Tier 0, Tier 1, Tier 2 administrators)
- **Content**:
  - Privileged account usage (separate admin accounts, no daily work with admin accounts)
  - Admin Tiering Model (tier classifications, tier isolation requirements)
  - PAM solution usage (password vaulting, check-out/check-in procedures)
  - Session recording (privileged sessions are recorded, acceptable usage)
  - MFA for privileged access (hardware MFA for Tier 0, no SMS for privileged accounts)
  - Privileged access logging and monitoring (privileged actions are monitored)
  - Incident response (credential compromise response, break-glass usage)
- **Frequency**: Annual mandatory training + onboarding training (when privileged access granted)
- **Delivery**: Instructor-led training or advanced e-learning
- **Verification**: Training completion recorded, competency assessment

**Technical Training** (Security Team, IT Operations):
- **Content**:
  - Authentication system administration (Azure AD, Okta, Active Directory)
  - MFA deployment and support (enrollment, troubleshooting, device replacement)
  - PAM solution administration (CyberArk, BeyondTrust, Azure PIM)
  - Admin Tiering implementation (tier classification, GPO enforcement, conditional access)
  - Access control implementation (file permissions, database grants, firewall rules)
  - Security monitoring (SIEM, privileged access monitoring, anomaly detection)
- **Frequency**: Annual + ad-hoc (new technologies, new procedures)
- **Delivery**: Vendor training, hands-on workshops, internal knowledge transfer
- **Verification**: Competency assessment, certification programs (vendor certifications)

---

## 9. Related Documents

**Internal References**:
- All ISMS policies (ISMS-POL-A.X.XX series)
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.15-16-18 (Identity & Access Management - IAM Foundation)
- ISMS Risk Assessment Methodology (Clause 6)
- ISMS Statement of Applicability (Annex A scoping)
- ISMS Compliance Monitoring Processes
- ISMS Incident Management Framework (A.5.24-27)

**External References**:
- Swiss Federal Data Protection Act (SR 235.1)
- EU GDPR (Regulation 2016/679)
- ISO/IEC 27001:2022 (Controls A.8.2, A.8.3, A.8.5)
- ISO/IEC 27002:2022 (Implementation Guidance for Controls 8.2, 8.3, 8.5)
- NIST SP 800-63 (Digital Identity Guidelines)
- NIST SP 800-53 (Security and Privacy Controls)
- CIS Controls (Center for Internet Security)
- OWASP Top 10 (Open Web Application Security Project)
- FINMA Circular 2023/1 (if applicable)
- DORA (Regulation 2022/2554, if applicable)
- NIS2 (Directive 2022/2555, if applicable)
- PCI DSS (pcisecuritystandards.org, if applicable)

---

## 10. Glossary

| Term | Definition |
|------|------------|
| **Authentication** | Process of verifying the identity of a user, device, or system |
| **Multi-Factor Authentication (MFA)** | Authentication using two or more independent factors (something you know, something you have, something you are) |
| **Privileged Access** | Access rights that allow administrative control over systems, configuration of security controls, or access beyond normal business need |
| **Privileged Access Management (PAM)** | Solutions and practices for securing, managing, and monitoring privileged accounts and credentials |
| **Admin Tiering / Tiered Administration Model** | Security architecture separating privileged accounts into tiers (0/1/2) to prevent lateral movement and credential theft |
| **Tier 0** | Highest privilege level controlling enterprise infrastructure (domain admins, cloud global admins, PKI admins) |
| **Tier 1** | Server and application administration (server admins, DBAs, application admins) |
| **Tier 2** | Workstation and endpoint administration (desktop support, help desk with local admin) |
| **PAW (Privileged Access Workstation)** | Dedicated, hardened workstation for Tier 0 administration with restricted network access and no internet/email |
| **Break-Glass Account** | Emergency administrator account with sealed credentials for disaster recovery when normal authentication fails |
| **Just-in-Time (JIT) Access** | Temporary privilege elevation automatically revoked after time expires |
| **Session Recording** | Recording privileged sessions (video or keystroke logging) for security monitoring and incident investigation |
| **Single Sign-On (SSO)** | Authentication mechanism allowing single login for multiple applications |
| **FIDO2/WebAuthn** | Modern phishing-resistant authentication standard using hardware security keys |
| **TOTP** | Time-based One-Time Password (authenticator app-based MFA) |
| **Technical Access Control** | System-enforced mechanisms restricting information access (file permissions, database grants, firewall rules) |
| **Default Deny** | Security principle where access is denied by default, explicit allow required |

---

## 5. Closing Statement

This policy establishes authentication and privileged access security requirements for [Organization]'s Information Security Management System.

**What this policy establishes:**
- Authentication mechanism requirements (passwords, MFA, SSO, certificates, biometrics)
- Privileged access management requirements (PAM, Admin Tiering, monitoring, reviews)
- Technical access restriction requirements (OS, database, application, API, cloud, network, encryption)

**What this policy does NOT establish:**
- Technical implementation procedures (addressed in ISMS-IMP-A.8.2-3-5 Implementation Assessment Suite)
- Technology selection decisions (addressed through risk assessment and technology evaluation)
- Incident response playbooks (addressed in incident management framework A.5.24-27)

**Separation of Concerns:**
- **This Policy**: Defines WHAT controls are required (requirements, governance, accountability)
- **Implementation Assessments (IMP)**: Defines HOW to implement and assess controls (procedures, tools, evidence)
- **Risk Management (Clause 6)**: Determines control implementation priorities based on risk
- **Compliance Monitoring**: Verifies and tracks compliance status (assessment workbooks, dashboards)

**Critical Success Factors:**
- MFA deployment (especially for privileged access, NIS2 compliance if applicable)
- Admin Tiering Model implementation (prevent lateral movement, contain credential theft)
- PAM solution adoption (password vaulting, session recording, monitoring)
- Regular privileged access reviews (quarterly minimum)
- Continuous authentication and privileged access monitoring (SIEM integration)



## Annex A: Admin Tiering Quick Reference

**Purpose**: Quick reference guide for administrators to understand tier classifications and tier isolation requirements.

**Admin Tiering Model Summary**:

| Tier | Scope | Examples | MFA Requirement | Dedicated Workstation | Session Recording |
|------|-------|----------|-----------------|----------------------|-------------------|
| **Tier 0** | Domain/Enterprise/Critical | Domain Admins, Azure Global Admin, AWS root, PKI admins, Backup admins, SIEM admins | Hardware MFA (FIDO2, YubiKey) | **PAWs REQUIRED** (Privileged Access Workstations) | **MANDATORY** |
| **Tier 1** | Server/Application | Server admins, DBAs, Application admins, Cloud subscription admins, VMware admins | Authenticator app or hardware token | Recommended (dedicated admin workstations or VMs) | **Recommended** |
| **Tier 2** | Workstation/Endpoint | Desktop support, help desk with local admin, MDM admins, VDI user desktop admins | Authenticator app | Standard workstations | Optional |

**Tier Isolation Rules (CRITICAL)**:

❌ **NEVER:**
- Tier 0 accounts SHALL NEVER log into Tier 1 or Tier 2 systems
- Tier 1 accounts SHALL NEVER log into Tier 2 systems

✅ **ALWAYS:**
- Use separate accounts per tier (john.doe.tier0, john.doe.tier1, john.doe.tier2)
- Use different passwords per tier account
- Use dedicated PAWs for Tier 0 administration (no internet, no email, no daily work)

**Why Tier Isolation Matters:**

**Scenario WITHOUT Tier Isolation:**
1. Domain Admin (Tier 0) logs into workstation (Tier 2) to help user
2. Workstation infected with malware
3. Malware steals Domain Admin credentials (cached in memory)
4. Attacker uses Domain Admin credentials to compromise entire Active Directory domain

**Scenario WITH Tier Isolation:**
1. Domain Admin uses separate Tier 2 account (john.doe.tier2) to help user
2. Workstation infected with malware
3. Malware steals Tier 2 credentials
4. Attacker has Tier 2 access ONLY (cannot compromise Tier 0 domain controllers)
5. **Blast radius contained** - Domain controllers remain secure

**Tier Violation Examples (CRITICAL ALERTS):**

- ❌ Domain Admin account (Tier 0) used to RDP into file server (Tier 1) → **VIOLATION**
- ❌ SQL Server DBA account (Tier 1) used to help desk support on user workstation (Tier 2) → **VIOLATION**
- ❌ Administrator browses internet or checks email from PAW → **VIOLATION**

**Tier Compliance Monitoring:**

All tier violations generate CRITICAL alerts reviewed by Security Team. Repeated violations result in privileged access suspension pending retraining.

**For More Information:**

- Full Admin Tiering requirements: Section 2.2.5 (Admin Tiering Model)
- Admin Tiering implementation procedures: ISMS-IMP-A.8.2-3-5.3 (PAM Implementation)
- Technology landscape and vendor solutions: ISMS-CTX-A.8.2-3-5 (Authentication & PAM Technology Landscape)

---

**END OF ISMS-POL-A.8.2-3-5**

*"Authentication is the gateway. Privileged access is the keys to the kingdom. Access restrictions are the locks on the doors. Get these right, and you've secured the foundation."*

*Remember Feynman: The first principle is that you must not fool yourself — and you are the easiest person to fool. No security theater. Evidence over checkbox compliance.*
