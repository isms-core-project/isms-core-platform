<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.4:framework:POL:a.8.4 -->
**ISMS-POL-A.8.4 – Access to Source Code**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Access to Source Code |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.4 |
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
| 1.0 | [Date] | CISO | Initial consolidated policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Technology Officer (CTO) or VP Engineering
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.4.1-UG/TG (Repository Access Control Implementation)
- ISMS-IMP-A.8.4.2-UG/TG (Branch Protection Configuration)
- ISMS-IMP-A.8.4.3-UG/TG (Source Code Access Assessment)
- ISO/IEC 27001:2022 Control A.8.4
- ISMS-POL-A.8.25-26-29 (Secure Development Lifecycle)
- ISMS-POL-A.5.15-16-18 (Access Control / Identity and Access Management)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for source code access control to protect intellectual property and maintain secure software development practices in accordance with ISO/IEC 27001:2022 Control A.8.4.

**Scope**: This policy applies to all source code repositories (production, internal tools, infrastructure-as-code, open source contributions, archived); all development artifacts (libraries, build scripts, test code); all repository platforms (GitHub, GitLab, Bitbucket, Azure DevOps, self-hosted); and all organisational personnel, contractors, and third parties with source code access.

**Purpose**: Define organisational requirements for source code access control implementation and governance. This policy establishes WHAT access controls are required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8 (UG/TG variants).4 suite.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, DORA, NIS2) apply where [Organisation]'s business activities trigger applicability.

---

# Control Alignment & Scope

## ISO/IEC 27001:2022 Control A.8.4

**ISO/IEC 27001:2022 Annex A.8.4 - Access to Source Code**

> *Access to source code, development tools and software libraries shall be appropriately managed.*

**Control Objective**: Establish organisational policy for source code access controls protecting intellectual property and ensuring secure software development through appropriate access management to source code repositories and related development artifacts.

**This Policy Addresses**:

- Source code access control requirements based on repository classification and organisational risk appetite
- Role-based access control for repositories and development artifacts
- Branch protection and code review requirements
- Secret management and prevention requirements
- Backup, recovery, and audit logging requirements
- Third-party access management
- Organisational roles and responsibilities for source code access governance
- Exception and incident management frameworks
- Integration with [Organisation]'s risk assessment and treatment processes

## What This Policy Does

This policy:

- **Defines** source code access control requirements aligned with data classification and regulatory obligations
- **Establishes** governance framework for repository access decision-making and accountability
- **Specifies** mandatory access controls for source code repositories and development artifacts
- **References** applicable regulatory requirements per ISMS-POL-00
- **Identifies** organisational roles and responsibilities for source code access controls

## What This Policy Does NOT Do

This policy does NOT:

- **Specify technical implementation details** (see ISMS-IMP-A.8.4 Implementation Guides)
- **Define platform-specific configuration procedures** (see ISMS-IMP-A.8.4.1 and ISMS-IMP-A.8.4.2 for GitHub, GitLab, Bitbucket, Azure DevOps procedures)
- **Provide assessment methodologies or evidence collection procedures** (see ISMS-IMP-A.8.4.3 Assessment Procedures)
- **Select repository platforms or technologies** (technology selection based on [Organisation]'s risk assessment)
- **Replace risk assessment** (source code access controls selected based on [Organisation]'s risk treatment)
- **Define detailed incident response procedures** (integrated with organisational incident response per A.5.24-27)
- **Establish secure coding standards** (covered by ISMS-POL-A.8.25-26-29 Secure Development Framework)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite evolving repository technologies and platform capabilities
- Technical agility for platform migrations and technology changes without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Focused audit scope (auditors audit policy compliance, not technical platform configurations)

**Document Structure**:

- **ISMS-POL-A.8.4** (THIS DOCUMENT): Policy requirements (WHAT and WHO)
- **ISMS-IMP-A.8.4.1**: Repository access control implementation procedures (HOW)
- **ISMS-IMP-A.8.4.2**: Branch protection configuration guidance (HOW)
- **ISMS-IMP-A.8.4.3**: Source code access assessment procedures (HOW)

## Scope

**This policy applies to**:

- All source code repositories containing production application code, internal tools, infrastructure-as-code, configuration management, or development artifacts
- All repository platforms (cloud-hosted Git platforms, self-hosted Git platforms, alternative version control systems)
- All development artifacts (source code, libraries, build scripts, test code, documentation, container definitions, CI/CD pipelines)
- All organisational personnel (employees, contractors, temporary staff) with source code access requirements
- All third-party development partners, offshore development teams, and security auditors
- All deployment models (on-premises infrastructure, hybrid environments, cloud-hosted repositories)

**Out of Scope**:

- Compiled binaries and executables (covered under A.8.1 - User Endpoint Devices)
- Production runtime configurations (covered under A.8.9 - Configuration Management)
- Secure coding standards and practices (covered under ISMS-POL-A.8.25-26-29 Secure Development Framework)
- Change management for production deployments (covered under A.8.32 - Change Management)
- Third-party commercial software without source code access
- Open source software used but not modified by [Organisation]

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

### Tier 1: Mandatory Compliance

[Organisation] MUST comply with these regulations based on jurisdiction and business operations:

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **ISO/IEC 27001:2022** | All operations | A.8.4 - Access to source code shall be appropriately managed |
| **Swiss nDSG** | All Swiss operations | Art. 8 - Technical and organisational measures to protect personal data include source code access control |
| **EU GDPR** | EU data processing | Art. 32 - Appropriate technical measures include access control to systems processing personal data |

### Tier 2: Conditional Applicability

Applicable only if [Organisation]'s business activities trigger specific regulatory scope:

| Regulation | Trigger Condition | Key Requirements |
|------------|-------------------|------------------|
| **FINMA** | Swiss financial institution | Circular 2023/1 Margin 50-62 - Information security includes source code protection |
| **DORA** | EU financial entity | Art. 9 - ICT asset management includes source code; Art. 15 - Incident reporting includes source code compromise |
| **NIS2** | Essential/important entity | Art. 21(2) - Asset management includes source code; Art. 23 - Incident reporting includes source code security incidents |

### Tier 3: Informational Reference

Non-mandatory guidance and best practices:

- NIST SP 800-218: Secure Software Development Framework (source code security)
- CIS Control 16: Application Software Security
- OWASP Code Repository Security Guide

**For complete regulatory categorization, refer to ISMS-POL-00 (Regulatory Applicability Framework).**

## Related Controls Integration

This policy integrates with and depends upon the following related ISMS controls:

**A.5.15-16-18 (Access Control / Identity and Access Management)**:

- Provides foundational IAM framework and user lifecycle management
- Source code access control inherits authentication, authorisation, and identity management requirements
- Multi-factor authentication (MFA) and access review requirements apply to source code repositories

**A.8.2-3-5 (Authentication and Privileged Access)**:

- Defines authentication mechanisms and privileged account management
- Repository administrator access is treated as privileged access

**A.8.25-26-29 (Secure Development Lifecycle)**:

- Defines secure coding standards and development practices
- A.8.4 enables secure development controls by ensuring only authorised personnel can modify code

**A.8.32 (Change Management)**:

- Addresses how changes are managed through environments (dev, test, production)
- A.8.4 focuses on controlling access to source code before deployment

**A.5.24-27 (Incident Management)**:

- Defines how to respond to security incidents
- A.8.4 helps detect source code access incidents through monitoring

**Integration Principle**: A.8.4 provides the access control foundation that enables other controls. Secure development practices are only effective if unauthorised individuals cannot bypass them by directly modifying code in repositories.

---

# Access Control Requirements

## Repository Access Management

[Organisation] implements role-based access control for all source code repositories with the principle of least privilege.

**Access Control Principles**:

All source code repositories SHALL implement role-based access control (RBAC). Default repository permissions SHALL be "no access" - explicit grant required for any access level. Access to source code repositories SHALL be granted only based on documented business need and approved by the repository owner. Repository access SHALL be reviewed quarterly for continued business justification. Repository access SHALL be automatically revoked upon employment termination, role change, or contract expiration.

**Quarterly Access Review Process**:

- Reviews conducted using standardized access review form (template in ISMS-IMP-A.8.4.3)
- Repository owner reviews each user's access and confirms: access still required (yes/no), access level appropriate (yes/no), action (retain/modify/revoke)
- Review completion documented with repository owner signature and date
- Review records retained in evidence repository (SharePoint/Confluence ISMS Evidence Library or equivalent)
- Non-response escalated to Development Manager after 10 business days; to CISO after 15 business days

**Access Request and Approval**:

All repository access requests SHALL include requestor name and role, repository name and classification, access level requested (read/write/admin), business justification, and expected duration if time-bound. Repository access requests SHALL be approved by the repository owner (mandatory), development team lead for write access or higher, and CISO or delegate for admin access to production repositories. Access SHALL be provisioned within 24 hours of approval during business hours. All access requests and approvals SHALL be documented and retained for audit purposes (minimum 3 years). Emergency access requests SHALL follow expedited approval process with post-facto review within 48 hours.

**Access Provisioning and Deprovisioning**:

Repository access SHALL be provisioned through centralized identity management systems where technically feasible. Access SHALL be granted to specific repositories, not blanket access to all repositories (unless explicitly justified and approved). HR system SHALL trigger automated deprovisioning workflow within 1 hour of termination processing. Deprovisioning SHALL be verified within 24 hours of trigger event through automated reporting.

**Deprovisioning Verification Process**:

- Automated daily report generated showing terminations processed in last 48 hours with repository access revocation status
- IT Security reviews report daily and confirms: access revoked (timestamp), repositories affected, verification complete (checkbox)
- Verification failures escalated immediately to IT Operations for manual remediation
- Monthly deprovisioning compliance report to CISO (target: 100% verified within 24 hours)

**Implementation Note**: Access request workflows, provisioning procedures, and deprovisioning automation are documented in ISMS-IMP-A.8.4.1 (Repository Access Control Implementation).

**Audit Evidence**:

- Repository access logs showing RBAC implementation
- Access request approval records
- Quarterly access review completion records
- Automated deprovisioning logs and verification

## Repository Classification and Controls

[Organisation] classifies all source code repositories to determine appropriate protection levels.

**Classification Framework**:

All source code repositories SHALL be classified according to the following categories:

- **Production Code Repositories**: Code directly deployed to customer-facing or business-critical production systems (highest protection)
  - *Examples*: Customer web application, payment processing service, API gateway, mobile app backend
- **Internal Tools Repositories**: Code for internal automation, utilities, and operational tools (high protection)
  - *Examples*: CI/CD pipeline scripts, monitoring dashboards, internal admin tools, deployment automation
- **Open Source Contribution Repositories**: Public or open source project code where organisation contributes (medium protection - controlled public access)
  - *Examples*: Forked open-source libraries, community contributions, public documentation
- **Archived/Deprecated Repositories**: Historical code no longer in active development (read-only)
  - *Examples*: Legacy application code (sunset), previous product versions, completed proof-of-concepts

Repository classification SHALL be assigned by the repository owner during repository creation. Repository classification SHALL be reviewed annually and updated when repository purpose changes.

**Classification-Based Controls**:

Production code repositories SHALL require minimum two-person review for all code merges, branch protection on main and release branches, signed commits where technically feasible, daily secret scanning, and quarterly access reviews. Internal tools repositories SHALL require minimum one-person review for code merges to main branch, branch protection on main branch, weekly secret scanning, and quarterly access reviews. Open source contribution repositories SHALL require access control (not publicly writable), review process for contributions, secret scanning before public push, and no internal secrets or credentials in public repositories. Archived/deprecated repositories SHALL be set to read-only mode, have write access removed from all users, retain access logs, and be documented as archived with deprecation date.

**Implementation Note**: Repository classification assignment procedures and classification review processes are documented in ISMS-IMP-A.8.4.1 (Repository Access Control Implementation).

**Audit Evidence**:

- Repository inventory with classification
- Repository metadata showing classification
- Annual classification review records
- Branch protection configuration per classification

## Role-Based Access Control

[Organisation] grants repository access based on defined roles with appropriate permissions.

**Access Roles and Permissions**:

Repository access SHALL be granted based on the following roles:

**Developers** have write access to clone/pull repositories, create branches/commits, push to non-protected branches, submit pull requests, and assign reviewers. Developers cannot push to protected branches, approve own pull requests, or modify repository settings.

**Security Team** has read access to all repositories for security reviews and audits, can clone/pull, read source code and commit history. Security team cannot commit changes or modify repository settings unless specifically granted.

**Auditors** have time-bound read-only access during audit period, access to audit logs and permission reports. Access automatically expires after audit completion.

**External Contractors** have time-bound, repository-specific write access limited to contracted work. Access expires on contract end date, cannot access repositories outside project scope, and all commits subject to enhanced review.

**Repository Administrators** manage repository settings, configure branch protection, manage collaborator access. Admin access does not automatically grant code write access (separation of duties), and admin actions are logged.

**Repository Owners** have ultimate responsibility for repository, approve access requests, conduct access reviews, and set repository classification. May or may not have write access to code depending on role.

**Service Accounts** (CI/CD, deployment automation, security scanners) SHALL be created with descriptive names indicating purpose, have access limited to specific repositories required for automation, use token-based authentication with expiration, be reviewed quarterly for continued need, and be documented with owner and purpose.

**Service Account Quarterly Review Criteria**:

- Is the automation/pipeline still active? (Check last activity date; inactive >90 days flagged for removal)
- Is the documented owner still responsible? (Confirm owner still with organisation and still managing the automation)
- Is access level still appropriate? (Review permissions; reduce if broader than required)
- Is token expiration set appropriately? (Maximum 1 year; recommend 90 days for high-privilege accounts)
- Action: Retain (with confirmation), Modify (reduce access), or Revoke (no longer needed)

**Least Privilege Enforcement**:

Users SHALL be granted the minimum access level required for their role: read access for code reviews or reference only, write access only if contributing code, admin access only for repository management responsibilities. Users with write access to multiple repositories SHALL have access justified individually per repository. Admin access SHALL be granted sparingly and limited to personnel with repository management responsibilities. "Admin" or "owner" access SHALL NOT be granted to external contractors except in documented exceptional cases with CISO approval.

**Implementation Note**: Role assignment procedures, permission matrices, and access justification templates are documented in ISMS-IMP-A.8.4.1 (Repository Access Control Implementation).

**Audit Evidence**:

- Repository permission reports showing role-based access
- Service account inventory with purpose documentation
- Quarterly service account reviews
- Access justification documentation per user per repository

## Branch Protection and Code Review

[Organisation] implements branch protection to prevent unauthorised code changes and enforce code review.

**Main Branch Protection**:

The main branch (master/main/trunk) of production and internal tools repositories SHALL be protected with direct commits blocked, pull request required before merging, minimum reviewers (2 for production, 1 for internal tools), dismiss stale pull request approvals when new commits pushed, require review from code owners where code owners defined, status checks must pass before merge (CI/CD tests, linters, security scans), signed commits required where technically feasible, and linear history enforced where technically feasible. Only repository administrators SHALL be able to modify branch protection rules. Temporary branch protection rule removal SHALL require documented justification, CISO approval, and automatic re-enablement after specified time period.

**Release Branch Protection**:

Release branches (release/*, hotfix/*) SHALL have the same protection requirements as main branch. Creation of release branches SHALL follow documented branching strategy and be traceable to release planning.

**Pull Request Requirements**:

All code changes to protected branches SHALL be submitted via pull requests. Pull requests SHALL NOT be approved by the code author (separation of duties). Pull requests SHALL include clear description of changes and purpose, link to related issue/ticket where applicable, evidence of testing (test results, test coverage), and security impact assessment for security-relevant changes. Reviewers SHALL verify code quality and adherence to coding standards, security implications of changes, adequate test coverage, and documentation updates where needed. Pull requests SHALL remain open for minimum review period: 4 hours for production code changes (to allow distributed team review), 1 hour for internal tools changes, with exception for emergency fixes with post-facto review.

**Fast-Track Review** (reduced review period): Low-risk changes (documentation updates, typo fixes, configuration-only changes with no code logic) may use 1-hour review period for production repos if: labeled as "low-risk" or "docs-only", limited to documentation/configuration files, no executable code changes, and approved by code owner.

**Implementation Note**: Branch protection configuration procedures, pull request workflows, and code review standards are documented in ISMS-IMP-A.8.4.2 (Branch Protection Configuration).

**Audit Evidence**:

- Branch protection configuration exports from repository platforms
- Pull request logs showing enforcement
- Code review completion confirmations
- Emergency fix post-facto review records
- Temporary exception records with approvals

## Secret Management

[Organisation] prohibits secrets in source code repositories and implements automated secret scanning.

**Secret Prohibition**:

Source code repositories SHALL NOT contain passwords/passphrases/credentials, API keys/tokens/access keys, private cryptographic keys/certificates, database connection strings with embedded credentials, SSH private keys/OAuth secrets, encryption keys/initialization vectors, or any other sensitive authentication material. Configuration files requiring secrets SHALL use environment variables, secrets management systems, encrypted configuration with external key management, or configuration templates with placeholder values. Developers SHALL be trained on secret management best practices including use of environment variables, secrets management systems, pre-commit hooks, and Git history remediation.

**Secret Scanning**:

All repositories SHALL have automated secret scanning enabled with pre-commit scanning (prevents secrets from entering repository), server-side scanning (detects secrets already in repository), and scan frequency of real-time for new commits and daily for full repository scan. Secret scanning SHALL detect generic secrets (regex-based patterns), provider-specific secrets (AWS keys, GitHub tokens, Azure credentials), and custom patterns defined by security team. Secret scanning findings SHALL trigger immediate notification to repository owner and security team, automatic creation of remediation ticket, and block of commit if pre-commit scanning enabled. Production repositories SHALL have pre-commit secret scanning enabled.

**Secret Remediation**:

Discovered secrets SHALL be remediated within 1 hour for production repository secrets and 24 hours for internal tools repository secrets, with immediate rotation if secret is confirmed exposed or used. Secret remediation SHALL include immediate rotation of exposed secret, removal from repository (including Git history if necessary), impact assessment (was secret accessed by unauthorised parties?), and incident reporting if required by A.5.24-27.

**Remediation Timeline Exception Handling**:

- After-hours discovery (outside business hours): On-call engineer contacted via PagerDuty/equivalent; 1-hour clock starts from engineer acknowledgment; if no acknowledgment within 30 minutes, escalate to secondary on-call
- If 1-hour remediation not achievable: Immediate compensating control required (disable secret at provider, revoke API key, block affected service); full remediation completed within 4 hours; exception documented with justification
- All timeline exceptions logged and reviewed weekly by Security Team; repeat exceptions trigger process improvement review

**Implementation Note**: Secret scanning tool configuration, remediation procedures, and developer training materials are documented in ISMS-IMP-A.8.4.1 (Repository Access Control Implementation) and ISMS-IMP-A.8.4.2 (Branch Protection Configuration).

**Audit Evidence**:

- Developer training completion records
- Secrets management system configuration
- Pre-commit hook deployment verification
- Secret scanning tool configuration and logs
- Secret finding remediation records showing completion times

## Authentication and Multi-Factor Authentication

[Organisation] requires strong authentication for repository access with multi-factor authentication for production repositories.

**Authentication Methods**:

Access to source code repositories SHALL be authenticated using username/password (with MFA required), SSH public key authentication, personal access tokens (with expiration), certificate-based authentication, or single sign-on (SSO) via organisational identity provider. Passwords SHALL comply with organisational password policy (minimum length, complexity, rotation). SSH keys and personal access tokens SHALL be unique per user and device, protected with passphrase or secure storage, rotated annually or upon suspicion of compromise, and revoked upon device loss or decommissioning.

**Multi-Factor Authentication**:

Multi-factor authentication SHALL be required for all human user accounts with write or admin access to production repositories, all human user accounts with admin access to any repository, and web-based repository access for all users. Accepted MFA methods include authenticator applications (Google Authenticator, Authy, Microsoft Authenticator), hardware security keys (YubiKey), push notification to registered mobile device, and SMS-based codes (least preferred, only if other methods unavailable). MFA SHALL NOT be bypassable through alternative authentication methods. Service accounts and automation tools SHALL use token-based authentication with restricted scopes instead of MFA.

**Service Account MFA Exception Justification**: Service accounts cannot perform interactive MFA; compensating controls applied:

- Tokens issued with minimum required scopes (least privilege)
- Token expiration enforced (maximum 1 year; 90 days recommended)
- Service account activity logged and monitored for anomalies
- Quarterly review ensures continued need and appropriate access
- High-privilege service accounts require CISO approval and enhanced monitoring

**Implementation Note**: Authentication configuration, MFA enrollment procedures, and SSH key management are documented in ISMS-IMP-A.8.4.1 (Repository Access Control Implementation).

**Audit Evidence**:

- Repository platform authentication configuration
- MFA enrollment reports showing 100% coverage
- MFA enforcement configuration
- Failed MFA attempts logs
- SSH key/token inventory and rotation records

## Audit Logging and Monitoring

[Organisation] implements comprehensive logging and monitoring of repository access and activities.

**Logging Requirements**:

Repository platforms SHALL log access events (login attempts, logout events, session duration), repository access (clone, pull, browsing operations), code changes (commits with author/timestamp/message/files, pushes, force pushes), branch operations (creation, deletion, protection changes), pull request activities (creation, review, approval, merge, rejection), permission changes (access granted, revoked, role changes), administrative actions (repository settings changes, collaborator management), and security events (secret scanning alerts, failed authentication, suspicious access patterns). Logs SHALL include minimum metadata: timestamp (UTC), user identity (username or service account), source IP address, action performed, repository affected, and success or failure status. Logs SHALL be tamper-evident and protected from unauthorised modification or deletion.

**Log Retention**:

Repository access logs SHALL be retained for minimum periods: access events 1 year, code change events 3 years (or life of repository if shorter), permission changes 3 years, security events 3 years, and administrative actions 3 years. Logs for production repositories SHALL be retained for longer periods based on regulatory requirements. Archived repositories SHALL retain logs even after repository archival.

**Log Monitoring and Alerting**:

Repository access logs SHALL be monitored for multiple failed authentication attempts (brute force), access from unusual geographic locations, access outside normal business hours (for role-based anomalies), bulk download operations, permission elevation attempts, force pushes to protected branches, secret scanning alerts, and large-scale access pattern changes. Security alerts SHALL be generated and sent to security operations team within 15 minutes of detection. Critical security events (confirmed unauthorised access, mass permission changes) SHALL trigger immediate incident response.

**Implementation Note**: Logging configuration, monitoring rules, and alerting procedures are documented in ISMS-IMP-A.8.4.3 (Source Code Access Assessment).

**Audit Evidence**:

- Log configuration showing required events
- Sample logs demonstrating metadata completeness
- Log integrity controls
- Log retention configuration and archive storage
- Log monitoring rules configuration
- Alert delivery testing results
- Security event response records

## Backup and Recovery

[Organisation] implements regular backups of source code repositories with tested recovery procedures.

**Backup Requirements**:

All source code repositories SHALL be backed up with frequency of daily incremental backups and weekly full backups, retention minimum of 90 days for active repositories and 7 years for production repositories, and geographic redundancy with backups stored in different geographic location than primary repository. Backups SHALL include source code (all branches, all commits, full history), repository metadata (permissions, settings, configurations), pull request history and discussions, issue tracking data if integrated, and wikis and documentation. Backups SHALL be encrypted at rest using organisationally-approved encryption standards. Backup access SHALL be restricted to authorised backup administrators and require MFA.

**Recovery Testing**:

Repository recovery procedures SHALL be tested quarterly for production repositories, annually for internal tools repositories, and after major platform upgrades or configuration changes. Recovery testing SHALL verify repository restoration within Recovery Time Objective (RTO: 4 hours for production, 24 hours for non-production), data integrity (all commits, branches, history intact), permission restoration, and functionality of restored repository. Recovery test results SHALL be documented including success/failure, time to recover, and issues identified.

**Recovery Testing Methodology**:

- Testing performed in isolated test environment (not production) to avoid operational disruption
- Representative sample testing acceptable: minimum 3 production repositories per quarter (rotating selection to cover all production repos annually)
- Simulated recovery (restore to test environment, verify integrity, measure RTO) is acceptable; full production failover not required for routine testing
- Annual full-scope test includes at least one complete production repository restoration with permission validation
- Test schedule published quarterly; results documented in standard test report template (ISMS-IMP-A.8.4.3)

**Implementation Note**: Backup configuration procedures, recovery testing methodology, and RTO targets are documented in ISMS-IMP-A.8.4.1 (Repository Access Control Implementation).

**Audit Evidence**:

- Backup schedule and execution logs
- Backup retention records
- Backup encryption configuration
- Backup access control lists
- Recovery testing schedule and completion records
- Recovery test reports
- RTO compliance measurements

## Third-Party Access Management

[Organisation] implements additional controls for third-party developer access to source code repositories.

**Third-Party Access Requirements**:

Third-party developers, contractors, and offshore development teams SHALL sign non-disclosure agreements (NDAs) before repository access is granted, have access limited to specific repositories required for contracted work, have time-bound access tied to contract duration, have access automatically revoked upon contract expiration, and be subject to enhanced code review requirements. Third-party access requests SHALL include contracting company name and contact information, individual developer names requiring access, repositories requiring access with justification, contract start and end dates, and project manager accountability. Third-party access SHALL be approved by repository owner (mandatory), procurement or legal (for NDA verification), and CISO or delegate (for production repository access).

**Third-Party Monitoring**:

Third-party repository access SHALL be monitored for unusual patterns or behaviors, reviewed monthly for continued need, and documented in third-party access registry. All code contributions from third-parties SHALL require code review by internal developer (minimum one reviewer), security review for security-relevant changes, and documentation review. Third-party access SHALL be immediately revoked upon contract expiration, contract termination, security incident involving third-party, or repository owner request.

**Implementation Note**: Third-party access procedures, monitoring requirements, and code review standards are documented in ISMS-IMP-A.8.4.1 (Repository Access Control Implementation) and ISMS-IMP-A.8.4.2 (Branch Protection Configuration).

**Audit Evidence**:

- NDA signature records
- Third-party access request approvals
- Contract-tied access expiration records
- Third-party access registry
- Monthly access review records
- Third-party code review records

## Exception Management

[Organisation] implements formal exception management for source code access policy requirements.

**Exception Request Process**:

Exceptions to this policy SHALL be requested in writing including specific requirement(s) requiring exception, business justification for exception, compensating controls (if applicable), requested exception duration, and risk assessment and acceptance. Exceptions SHALL be approved by repository owner (mandatory), Information Security Manager (mandatory), and CISO (for production repository exceptions). Exceptions SHALL be granted for limited time periods (maximum 12 months) and require renewal. All active exceptions SHALL be reviewed quarterly for continued validity.

**Compensating Controls**:

Where technically infeasible to meet a requirement, compensating controls SHALL be implemented to achieve equivalent risk reduction. Compensating controls SHALL be documented in exception request, verified by Information Security Manager, monitored for effectiveness, and reviewed annually.

**Implementation Note**: Exception request procedures, approval workflows, and compensating control assessment methodology are documented in ISMS-IMP-A.8.4.3 (Source Code Access Assessment).

**Audit Evidence**:

- Exception request documentation
- Exception approval records
- Quarterly exception review records
- Compensating control documentation
- Effectiveness verification records
- Annual compensating control reviews

---

# Roles, Governance & Compliance

## Roles and Responsibilities

**Chief Information Security Officer (CISO)**:

- Overall accountability for source code access control policy and implementation
- Approval of exceptions to policy requirements
- Approval of admin access to production repositories
- Oversight of security incidents involving source code access
- Annual policy review and updates
- Reporting to Executive Management on source code security posture

**Chief Technology Officer (CTO) / VP Engineering**:

- Accountability for development platform selection and configuration
- Approval of repository classifications
- Escalation point for access disputes
- Development team compliance with policy requirements
- Resource allocation for policy implementation
- Collaboration with CISO on policy updates

**Information Security Manager**:

- Policy maintenance and update coordination
- Exception review and approval (non-production repositories)
- Security monitoring and incident investigation
- Audit coordination and evidence provision
- Training coordination for developers
- Quarterly compliance reporting to CISO

**Repository Owners**:

- Repository classification assignment
- Access request approval
- Quarterly access reviews
- Repository security configuration maintenance
- Incident reporting to security team
- Collaboration with security team on security reviews

**Development Team Leads**:

- Access request review for team members
- Code review process enforcement
- Developer training on secure repository practices
- Team compliance with branch protection requirements
- Secret management enforcement within team
- Collaboration with repository owners on access management

**Security Team**:

- Security monitoring and alerting configuration
- Secret scanning tool management
- Security audits and assessments
- Incident response for source code security events
- Vulnerability assessment of repository configurations
- Security training development and delivery

**IT Operations**:

- Repository platform maintenance and availability
- Backup and recovery implementation
- Access provisioning/deprovisioning automation
- Log collection and retention
- Integration with identity management systems
- Disaster recovery testing

**Individual Developers and Contractors**:

- Compliance with access control and authentication requirements
- Protection of credentials (passwords, SSH keys, tokens)
- No storage of secrets in repositories
- Code review participation
- Incident reporting to repository owner and security team
- Completion of required security training

## Policy Review and Updates

This policy SHALL be reviewed annually by the CISO and Information Security Manager. Policy updates SHALL be triggered by annual scheduled review, significant security incidents involving source code access, changes to regulatory requirements, major repository platform changes, internal audit findings or external audit recommendations, and changes to organisational risk appetite. Policy updates SHALL be approved by CISO (mandatory), CTO or VP Engineering (mandatory), Legal/Compliance Officer (mandatory), and Executive Management (final authority). Policy effective date SHALL be 30 days after approval to allow implementation preparation.

**Audit Evidence**:

- Annual policy review records
- Policy update approval records
- Stakeholder consultation records

## Compliance Monitoring and Reporting

Information Security Manager SHALL monitor policy compliance through quarterly access control assessments, continuous secret scanning monitoring, log analysis and anomaly detection, and audit of branch protection configurations. Compliance status SHALL be reported monthly to CISO (summary dashboard), quarterly to Executive Management (detailed report), and annually to Board of Directors (strategic overview). Compliance reports SHALL include overall compliance score and trends, identified gaps and remediation status, security incidents and lessons learned, exception status and validity, and recommendations for improvement.

**Audit Evidence**:

- Monthly compliance reports to CISO
- Quarterly reports to Executive Management
- Annual reports to Board

## Audit and Certification

Source code access controls SHALL be audited annually by internal audit team, annually by external ISO 27001 certification auditors, and ad-hoc based on security incidents or management request. Audit scope SHALL include policy compliance verification, access control effectiveness, branch protection implementation, secret management practices, backup and recovery capabilities, log integrity and retention, and third-party access management. Audit findings SHALL be documented in audit reports, tracked in audit finding management system, remediated within agreed timelines, and verified by follow-up audits.

**Gap Remediation Process**:

- **Identification**: Gaps identified via quarterly assessments, continuous monitoring alerts, audit findings, or incident investigations
- **Assignment**: Information Security Manager assigns remediation owner within 5 business days; owner acknowledged in tracking system
- **Tracking**: Gaps tracked in central gap register (Jira, ServiceNow, or equivalent) with severity, owner, due date, status
- **Escalation**: Overdue gaps (>30 days past due) escalated to CISO; >60 days to Executive Management
- **Closure**: Remediation verified by Information Security Manager; evidence of closure documented; gap status updated to "Closed-Verified"
- **Reporting**: Open gap summary included in monthly CISO compliance report

**Audit Evidence**:

- Internal audit reports
- External audit reports
- Audit finding remediation tracking
- Follow-up audit verification

## Non-Compliance Consequences

Policy violations SHALL result in minor violations (written warning, mandatory retraining), moderate violations (access suspension, formal disciplinary action), or severe violations (access revocation, termination consideration, legal action). All policy violations SHALL be documented in incident management system, investigated by Information Security Manager, reported to CISO, and tracked to resolution. Repeat violations SHALL result in escalated consequences regardless of severity.

**Audit Evidence**:

- Policy violation records
- Disciplinary action documentation
- Violation trend analysis

---

# Assessment and Evidence Framework

## Assessment Methodology

[Organisation] assesses compliance with source code access control requirements through repository inventory and classification verification, access control compliance assessment, branch protection configuration review, secret scanning effectiveness measurement, backup and recovery testing, and log monitoring and analysis.

**Implementation Note**: Detailed assessment methodology, evidence collection procedures, and compliance scoring framework are documented in ISMS-IMP-A.8.4.3 (Source Code Access Assessment).

## Assessment Frequency

**Continuous Monitoring**: Secret scanning (real-time), access anomaly detection (real-time), permission change monitoring (real-time)

**Quarterly Assessments**: Repository access compliance review, branch protection verification, service account validation, contractor access review, exception review

**Annual Comprehensive Audit**: Full compliance assessment across all repositories, evidence collection for ISO 27001 certification, policy effectiveness review, control improvement recommendations

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:

- ✅ This policy document (ISMS-POL-A.8.4 v1.0)
- ✅ Approval signatures from CISO, CTO, Executive Management
- ✅ Repository access control requirements defined
- ✅ Branch protection requirements documented
- ✅ Secret management requirements specified
- ✅ Authentication requirements documented
- ✅ Roles and responsibilities assigned

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

**Evidence Repository**: All audit evidence stored in centralized ISMS Evidence Library (SharePoint, Confluence, or equivalent document management system) with folder structure by control and assessment period.

**Repository Inventory Evidence**: Repository inventory with classification/owner/metadata, repository platform exports, quarterly inventory review records

**Access Control Evidence**: User-to-repository access matrix, access request approval records, quarterly access review completion records, NDA signature records, deprovisioning logs and verification

**Branch Protection Evidence**: Branch protection configuration exports, pull request enforcement logs, code review completion records, temporary exception records with approvals

**Secret Management Evidence**: Secret scanning configuration and logs, secret finding remediation records, developer training completion records

**Authentication Evidence**: MFA enrollment reports, authentication configuration, SSH key/token inventory and rotation records

**Logging and Monitoring Evidence**: Log configuration showing required events, log retention configuration, security alert configuration and testing results

**Backup and Recovery Evidence**: Backup execution logs, recovery testing results, RTO compliance measurements

## Compliance Scoring

**Overall Source Code Security Score** (0-100%): Repository Access Compliance 35%, Branch Protection Compliance 35%, Secret Management Compliance 20%, Third-Party Access Compliance 10%

**Compliance Scoring Methodology**:

| Component | Calculation | Data Source |
|-----------|-------------|-------------|
| Repository Access (35%) | (Repos with compliant RBAC + completed quarterly reviews) / Total repos × 100 | Repository platform reports, access review records |
| Branch Protection (35%) | (Repos with required branch protection enabled) / Applicable repos × 100 | Branch protection configuration exports |
| Secret Management (20%) | (Repos with secret scanning enabled + secrets remediated within SLA) / Total × 100 | Secret scanning tool reports |
| Third-Party Access (10%) | (Third-party accounts with valid NDA + current contract) / Total third-party accounts × 100 | Third-party access registry |

**Score Calculation**: Information Security Manager calculates monthly; score tracked in Summary Dashboards; historical scores retained for trend analysis.

**Compliance Targets**: Mature ISMS ≥90% overall compliance, New ISMS ≥70% compliance within 180 days

**Non-Compliance Handling**: <70% (immediate CISO escalation, remediation plan required), 70-89% (Information Security Manager oversight, monthly reviews), ≥90% (standard quarterly monitoring)

---

# Effective Date and Transition

## Effective Date

**Effective Date**: [30 days after Executive Management approval]

This policy becomes effective 30 days after Executive Management approval to allow communication to all affected personnel, implementation of required technical controls, training delivery for developers and administrators, and transition planning for non-compliant repositories.

## Transition Timeline

**Immediate (0-30 days)** - Critical controls: Access reviews for production repositories, secret scanning activation, emergency access revocation process, MFA enforcement for production repositories

**Short-term (30-90 days)** - Core implementations: Branch protection implementation, access documentation and inventory, repository classification completion, quarterly access review process

**Medium-term (90-180 days)** - Full compliance: Complete compliance across all repositories, automated monitoring deployment, backup and recovery testing, training completion for all personnel

**Long-term (180-365 days)** - Optimization: Automation enhancement, process optimization, advanced monitoring and analytics, continuous improvement initiatives

**Transition Period Evidence**: During transition, collect evidence of progress for audits occurring before full compliance:

- Transition plan document with milestones and target dates
- Monthly progress reports showing percentage of repositories compliant per control area
- Documented exceptions/compensating controls for repositories not yet compliant
- Risk acceptance for deferred compliance items (signed by CISO)

## Implementation Priorities

Repositories SHALL be brought into compliance in the following priority order:

1. Production code repositories (customer-facing applications)
2. Production infrastructure-as-code repositories
3. Internal tools repositories
4. Open source contribution repositories
5. Archived/deprecated repositories

## Grandfathering and Exceptions

No permanent exceptions SHALL be granted based solely on "existing state" or "legacy repository." Temporary exceptions MAY be granted during transition period for technical limitations requiring platform upgrades, third-party dependencies requiring vendor coordination, or resource constraints requiring phased implementation. All temporary exceptions SHALL be documented with justification and remediation plan, approved by CISO, expire no later than 12 months after policy effective date, and be tracked in exception management system.

**Audit Evidence**:

- Transition plan documentation
- Temporary exception records with approvals
- Remediation completion tracking

---

# Document Control and Approval

## Document Approval

**Policy Approved By**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Chief Information Security Officer (CISO) | [Name] | _________________ | [Date] |
| Chief Technology Officer (CTO) | [Name] | _________________ | [Date] |
| Legal/Compliance Officer | [Name] | _________________ | [Date] |
| Chief Executive Officer (CEO) | [Name] | _________________ | [Date] |

## Document Distribution

This policy SHALL be distributed to all personnel with source code repository access, all development team leads and managers, Information Security team, IT Operations team, Internal Audit team, Executive Management, and Board of Directors (upon request). Distribution methods include publication in organisational policy repository, email notification to affected personnel, inclusion in onboarding materials for developers, and reference in employment agreements (where applicable).

## Next Review Date

**Next Scheduled Review**: [Approval Date + 12 months]

**Responsible**: Chief Information Security Officer (CISO)

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for source code access control. Implementation procedures are documented in ISMS-IMP-A.8.4 (UG/TG).1 (Repository Access Control), ISMS-IMP-A.8.4.2 (Branch Protection), and ISMS-IMP-A.8.4.3 (Source Code Access Assessment).*

<!-- QA_VERIFIED: 2026-03-01 -->
