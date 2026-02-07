**ISMS-OP-POL-A.8.4 — Access to Source Code**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Access to Source Code |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.4 |
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
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.8.4 — Access to source code
- ISO/IEC 27002:2022 Section 8.4 — Implementation guidance for source code access control
- NIST SP 800-218 — Secure Software Development Framework (SSDF) v1.1
- CIS Controls v8 — Safeguard 16.1–16.14 (Application Software Security)

**Related Annex A Controls**:

| Control | Relationship to Source Code Access |
|---------|------------------------------------|
| A.5.9 Inventory of information and other associated assets | Source code repositories included in asset inventory |
| A.5.15–16–18 Identity and access management | Foundational IAM framework; authentication and authorisation for repositories |
| A.5.19–23 Supplier and cloud service security | Third-party developer access and cloud repository controls |
| A.8.2–3–5 Authentication and privileged access | MFA requirements; admin access treated as privileged |
| A.8.9 Configuration management | Repository platform configuration baselines |
| A.8.15 Logging | Audit logging for repository access and code changes |
| A.8.25–26–29 Secure development lifecycle | Secure coding, branch protection, code review integration |
| A.8.32 Change management | Change control for production code deployment |

**Related Internal Policies**:

- Identity and Access Management Policy
- Secure Development Lifecycle Policy
- Logging and Monitoring Policy
- Change Management Policy
- Information Classification and Handling Policy

---

# Access to Source Code Policy

## Purpose

The purpose of this policy is to ensure that read and write access to source code, development tools, and software libraries is appropriately managed in order to protect intellectual property, prevent the introduction of unauthorised functionality, avoid unintentional or malicious changes, and maintain the confidentiality of organisational software assets.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect personal data embedded in or processed by source code systems. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 requirements also apply. Source code access control is a key technical measure for demonstrating that systems processing personal data are subject to appropriate access restrictions.

## Scope

Source code repositories, development tools, and software libraries owned, managed, or controlled by the organisation and deemed in scope by the ISO 27001 scope statement. This includes:

- All source code repositories (production applications, internal tools, infrastructure-as-code, configuration management, open source contributions, archived code).
- All repository platforms ([Repository Platform] — e.g., GitHub Enterprise, GitLab, Bitbucket, Azure DevOps, or self-hosted Git server). The organisation shall document its primary repository platform(s) in the asset inventory, including: hosting model (cloud-hosted vs. self-hosted), data residency, backup arrangements, and administrative access controls. Where multiple platforms are used, this policy applies equally to all platforms.
- All development artifacts (source code, libraries, build scripts, test code, container definitions, CI/CD pipeline definitions).

All employees, contractors, and third-party users with source code access.

**Out of scope**: Compiled binaries and executables; production runtime configurations (covered under A.8.9); secure coding standards (covered under A.8.25-26-29); third-party commercial software to which the organisation has no source code access.

## Principle

Source code access shall follow the principle of least privilege. Access is granted only based on documented business need and approved by the repository owner.

The organisation shall centrally administer access to source code repositories using a source code management system. Default repository permissions shall be "no access" — explicit grant is required for any access level.

Source code is classified as a critical organisational asset. Unauthorised access, modification, or disclosure of source code may result in intellectual property loss, introduction of vulnerabilities, regulatory non-compliance, or reputational damage.

---

## Repository Classification

All source code repositories shall be classified to determine appropriate protection levels.

**Classification Categories**:

| Classification | Description | Examples |
|----------------|-------------|----------|
| **Production** | Code deployed to customer-facing or business-critical production systems | Customer web application, payment processing service, API gateway, mobile app backend |
| **Internal Tools** | Code for internal automation, utilities, and operational tools | CI/CD pipeline scripts, monitoring dashboards, internal admin tools, deployment automation |
| **Open Source** | Public or open source project code where the organisation contributes | Forked open-source libraries, community contributions, public documentation |
| **Archived** | Historical code no longer in active development | Legacy application code (sunset), previous product versions, completed proof-of-concepts |

Repository classification shall be assigned by the repository owner during creation and reviewed annually. Classification shall be updated when the repository purpose changes.

**Inherited and Dormant Repositories**: Repositories that are inherited (e.g., through acquisition, team restructuring, or developer departure) or dormant (no commits >12 months) shall be handled as follows:

- **Inherited repositories**: The receiving team lead shall be assigned as interim repository owner within 5 business days. The repository shall be reviewed for classification accuracy, access permissions, and secret scanning compliance within 30 days.
- **Dormant repositories**: Repositories with no commit activity for 12 months shall be flagged for review. The repository owner shall confirm: (a) the repository is still needed (retain with current classification), (b) the repository should be archived (move to Archived classification, restrict to read-only), or (c) the repository should be deleted (follow data retention policy). Non-response after 30 days shall result in automatic archival with notification to the Development Manager.

---

## Role-Based Access Control

Repository access shall be granted based on defined roles with the minimum permissions required.

**Access Roles**:

| Role | Permissions | Restrictions |
|------|-------------|--------------|
| **Developer** | Clone, pull, create branches, push to non-protected branches, submit pull requests | Cannot push to protected branches, approve own pull requests, or modify repository settings |
| **Security Reviewer** | Read access to all repositories for security reviews and audits | Cannot commit changes or modify settings unless specifically granted |
| **Auditor** | Time-bound, read-only access during audit period; access to audit logs and permission reports | Access automatically expires after audit completion |
| **External Contractor** | Time-bound, repository-specific write access limited to contracted work | Cannot access repositories outside project scope; all commits subject to enhanced review; access expires on contract end date |
| **Repository Administrator** | Manage repository settings, branch protection, and collaborator access | Admin access does not automatically grant code write access (separation of duties); admin actions are logged |
| **Repository Owner** | Approve access requests, conduct access reviews, set classification | May or may not have code write access depending on role |
| **Service Account** | Automated access for CI/CD, deployment, and security scanning tools | Descriptive naming; token-based authentication with expiration; access limited to specific repositories; documented owner and purpose. Token scopes shall be minimised — e.g., CI build: `repo:read`, `actions:write`; deployment: `repo:read`, `packages:write`; security scanner: `repo:read`, `security_events:write` |

Admin or owner access shall not be granted to external contractors except in documented exceptional cases with CISO approval.

---

## Access Request and Approval

All repository access requests shall include:

- Requestor name and role.
- Repository name and classification.
- Access level requested (read/write/admin).
- Business justification.
- Expected duration (if time-bound).

**Approval requirements**:

| Access Level | Required Approvers |
|--------------|--------------------|
| Read access | Repository Owner |
| Write access | Repository Owner + Development Team Lead |
| Admin access (any repository) | Repository Owner + Development Team Lead |
| Admin access (Production repository) | Repository Owner + CISO or delegate |

Access shall be provisioned within 24 hours of approval during business hours. Emergency access requests shall follow an expedited approval process with post-facto review within 48 hours.

All access requests and approvals shall be documented and retained for a minimum of 3 years.

---

## Access Review and Deprovisioning

Repository access shall be reviewed quarterly to confirm continued business justification.

**Quarterly Access Review Process**:

1. Repository owner reviews each user's access and confirms: access still required (yes/no), access level appropriate (yes/no), action (retain/modify/revoke).
2. Review documented with repository owner confirmation and date.
3. Non-response escalated to Development Manager after 10 business days; to CISO after 15 business days.

**Service Account Review** (quarterly):

- Is the automation or pipeline still active? (Flag for removal if inactive >90 days.)
- Is the documented owner still responsible?
- Is the access level still appropriate?
- Is the token expiration set appropriately? (Maximum 1 year; 90 days recommended for high-privilege accounts.)

**Deprovisioning**:

- Repository access shall be revoked within the same business day of employment termination, role change that removes the access need, or contract expiration.
- Automated deprovisioning via identity management system is preferred.
- Deprovisioning shall be verified within 24 hours of the trigger event.

---

## Branch Protection and Code Review

The main branch (main/master/trunk) of Production and Internal Tools repositories shall be protected.

**Branch Protection Requirements**:

| Requirement | Production | Internal Tools |
|-------------|------------|----------------|
| Direct commits blocked | Yes | Yes |
| Pull request required before merge | Yes | Yes |
| Minimum reviewers | 2 | 1 |
| Dismiss stale approvals on new commits | Yes | Recommended |
| Status checks must pass (CI/CD tests, linters, security scans) | Yes | Yes |
| Signed commits | Recommended | Optional |

Release branches (release/*, hotfix/*) shall have the same protection as the main branch.

Only repository administrators shall be able to modify branch protection rules. Temporary branch protection removal shall require documented justification, CISO approval, and automatic re-enablement after the specified period.

**Pull Request Requirements**:

- All code changes to protected branches shall be submitted via pull requests.
- Pull requests shall not be approved by the code author (separation of duties).
- Pull requests shall include a clear description of changes, link to related issue or ticket where applicable, and evidence of testing.
- Security-relevant changes shall include a security impact assessment.

**Fast-Track Review**: Low-risk changes (documentation updates, typo fixes, configuration-only changes with no code logic) may use a 1-hour review period for Production repositories if labelled as "low-risk" or "docs-only", limited to documentation or configuration files, and approved by a code owner. Standard review period for Production code changes: 4 hours.

---

## Secret Management

Source code repositories shall not contain passwords, API keys, tokens, private keys, database connection strings with embedded credentials, SSH private keys, encryption keys, or any other sensitive authentication material.

**Secret Scanning**:

All repositories shall have automated secret scanning enabled using [Secret Scanning Tool] (e.g., GitLeaks, TruffleHog, GitHub Secret Scanning, or equivalent).

| Scanning Type | Scope | Frequency |
|---------------|-------|-----------|
| Pre-commit scanning | Prevents secrets from entering repository | Real-time (every commit) |
| Server-side scanning | Detects secrets already in repository | Daily full scan |

Production repositories shall have pre-commit secret scanning enabled (blocking mode).

Secret scanning shall detect generic secrets (regex-based patterns), provider-specific secrets (AWS keys, GitHub tokens, Azure credentials), and custom patterns defined by the security team.

**Secret Remediation**:

| Repository Classification | Remediation SLA |
|---------------------------|-----------------|
| Production | 1 hour (immediate rotation if confirmed exposed) |
| Internal Tools | 24 hours |

Remediation shall include: (1) immediate rotation of exposed secret, (2) removal from repository history if committed, (3) impact assessment (was the secret accessed by unauthorised parties?), and (4) incident reporting if required.

**Approved Secrets Management**:

| Environment | Approved Method |
|-------------|-----------------|
| Development | Environment variables; `.env` files excluded from version control via `.gitignore` |
| CI/CD Pipelines | Pipeline secrets store ([CI/CD Platform] Secrets or equivalent); no hardcoded secrets in pipeline definitions |
| Production | Dedicated secrets manager (e.g., HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, or equivalent) |

Developers shall be trained on secret management best practices, including use of environment variables, secrets management systems, and pre-commit hooks.

---

## Authentication and Multi-Factor Authentication

Access to source code repositories shall be authenticated using approved methods: username/password (with MFA), SSH public key authentication, personal access tokens (with expiration), certificate-based authentication, or single sign-on (SSO) via the organisational identity provider.

**MFA Requirements**:

Multi-factor authentication shall be required for:

- All human user accounts with write or admin access to Production repositories.
- All human user accounts with admin access to any repository.
- Web-based repository access for all users.

Accepted MFA methods: authenticator applications (e.g., Google Authenticator, Microsoft Authenticator, Authy), hardware security keys (e.g., YubiKey), or push notification to registered device. SMS-based codes are the least preferred method and shall only be used if other methods are unavailable.

**SSH Keys and Personal Access Tokens**:

- Unique per user and device.
- Protected with passphrase or secure storage.
- Rotated annually or immediately upon suspicion of compromise.
- Revoked upon device loss or decommissioning.

**Service Accounts**: Service accounts cannot perform interactive MFA. Compensating controls shall include: tokens issued with minimum required scopes, token expiration enforced (maximum 1 year; 90 days recommended for high-privilege accounts), activity logged and monitored for anomalies, and quarterly review for continued need.

---

## Audit Logging and Monitoring

Repository platforms shall log the following events:

| Event Category | Events Logged |
|----------------|---------------|
| **Access** | Login attempts, logout events, session duration |
| **Repository access** | Clone, pull, browsing operations |
| **Code changes** | Commits (author, timestamp, message, files), pushes, force pushes |
| **Branch operations** | Creation, deletion, protection changes |
| **Pull requests** | Creation, review, approval, merge, rejection |
| **Permission changes** | Access granted, revoked, role changes |
| **Administrative actions** | Repository settings changes, collaborator management |
| **Security events** | Secret scanning alerts, failed authentication, suspicious access patterns |

Logs shall include: timestamp (UTC), user identity, source IP address, action performed, repository affected, and success or failure status.

**Log Retention**:

| Event Type | Minimum Retention |
|------------|-------------------|
| Access events | 1 year |
| Code change events | 3 years |
| Permission changes | 3 years |
| Security events | 3 years |
| Administrative actions | 3 years |

Logs shall be tamper-evident and protected from unauthorised modification or deletion.

**Monitoring and Alerting**:

Repository access logs shall be monitored for: multiple failed authentication attempts, access from unusual geographic locations, access outside normal business hours, bulk download operations, permission elevation attempts, force pushes to protected branches, and secret scanning alerts.

Security alerts shall be generated and delivered to the security operations team within 15 minutes of detection. Critical events (confirmed unauthorised access, mass permission changes) shall trigger immediate incident response per the organisation's incident management process. Confirmed security incidents involving source code (unauthorised access, code tampering, intellectual property theft) shall be escalated to the CISO within 1 hour of confirmation. Where the incident involves customer data or production systems, the incident management process (A.5.24-28) shall be activated immediately.

---

## Backup and Recovery

All source code repositories shall be backed up to enable recovery from data loss, corruption, or platform failure.

**Backup Requirements**:

| Requirement | Standard |
|-------------|----------|
| Frequency | Daily incremental; weekly full |
| Retention | 90 days (active repositories); 7 years (Production repositories) |
| Geographic redundancy | Backups stored in a different geographic location from primary repository |
| Encryption | Encrypted at rest using organisation-approved encryption |
| Access control | Restricted to authorised backup administrators; MFA required |

Backups shall include source code (all branches, commits, full history), repository metadata (permissions, settings, configurations), pull request history, and issue tracking data if integrated.

**Recovery Testing**:

| Repository Classification | Testing Frequency | Recovery Time Objective (RTO) |
|---------------------------|-------------------|-------------------------------|
| Production | Quarterly | 4 hours |
| Internal Tools | Annually | 24 hours |

Recovery testing shall verify: repository restoration within RTO, data integrity (all commits, branches, history intact), permission restoration, and functionality of restored repository. Testing shall use a representative sample of repositories (minimum 3 Production repositories per quarter, rotating to cover all annually). Results shall be documented.

---

## Third-Party Access Management

Third-party developers, contractors, and offshore development teams shall meet the following requirements before receiving repository access:

- Signed non-disclosure agreement (NDA) verified by procurement or legal.
- Access limited to specific repositories required for contracted work.
- Time-bound access tied to contract duration with automatic expiration.
- Access approved by repository owner (mandatory) and CISO or delegate (for Production repositories).

**Third-Party Monitoring**:

- Third-party access reviewed monthly for continued need.
- All code contributions from third parties shall require review by an internal developer (minimum one reviewer) and security review for security-relevant changes.
- Third-party access shall be immediately revoked upon contract expiration, contract termination, security incident involving the third party, or repository owner request.

Third-party access shall be documented in a third-party access register with: contracting company, individual names, repositories accessed, contract dates, and project manager accountability.

---

## Exception Management

Exceptions to this policy shall be requested in writing and shall include:

- Specific requirement(s) requiring exception.
- Business justification.
- Compensating controls.
- Requested exception duration (maximum 12 months).
- Risk assessment and acceptance.

Exceptions shall be approved by the repository owner and Information Security Manager (mandatory), plus the CISO for Production repository exceptions. All active exceptions shall be reviewed quarterly.

Where technically infeasible to meet a requirement, compensating controls shall be implemented to achieve equivalent risk reduction, documented, verified by the Information Security Manager, and reviewed annually.

---

## Definitions

| Term | Definition |
|------|------------|
| **Branch protection** | Configuration rules that prevent direct commits to specified branches, requiring pull requests, reviews, and passing status checks |
| **Code owner** | Individual or team designated as responsible for reviewing changes to specific parts of the codebase |
| **Force push** | A Git operation that overwrites remote branch history; restricted on protected branches |
| **MFA** | Multi-factor authentication — requiring two or more verification factors to gain access |
| **Pre-commit hook** | A script that runs before a commit is created, used to prevent secrets or policy violations from entering the repository |
| **Pull request (merge request)** | A request to merge code changes from one branch to another, enabling review before integration |
| **RBAC** | Role-based access control — assigning permissions based on defined organisational roles |
| **Repository** | A storage location for source code, managed by a version control system (e.g., Git) |
| **Secret** | Any credential, API key, token, private key, or authentication material that must not be stored in source code |
| **Service account** | A non-human account used for automation, CI/CD, and system-to-system integration |
| **SSO** | Single sign-on — authentication that allows users to access multiple systems with one set of credentials |

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; approval of admin access to Production repositories; exception approval; oversight of security incidents involving source code; annual policy review; reporting to Executive Management |
| **CTO / Development Manager** | Development platform selection and configuration; repository classification approval; development team compliance; resource allocation for policy implementation |
| **Information Security Manager** | Policy maintenance; exception review (non-Production repositories); security monitoring and incident investigation; audit coordination; quarterly compliance reporting to CISO |
| **Repository Owners** | Repository classification assignment; access request approval; quarterly access reviews; repository security configuration; incident reporting to security team |
| **Development Team Leads** | Access request review for team members; code review process enforcement; developer training on secure repository practices; secret management enforcement within team |
| **Security Team** | Security monitoring and alerting configuration; secret scanning tool management; security audits and assessments; incident response for source code security events |
| **IT Operations** | Repository platform maintenance and availability; backup and recovery implementation; access provisioning and deprovisioning automation; log collection and retention |
| **Individual Developers and Contractors** | Compliance with access control and authentication requirements; protection of credentials; no storage of secrets in repositories; code review participation; incident reporting; completion of required security training |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | **Repository inventory** with classification, owner, and platform metadata | CTO / Development Manager | Maintained continuously; reviewed annually | Life of repository + 3 years |
| 2 | **Access request and approval records** (requests, justifications, approvals) | Repository Owners | Per request | 3 years |
| 3 | **Quarterly access review records** (user-by-user confirmation, actions taken) | Repository Owners | Quarterly | 3 years |
| 4 | **Service account inventory** with owner, purpose, and quarterly review records | IT Operations / Development Manager | Maintained continuously; reviewed quarterly | Life of account + 1 year |
| 5 | **Branch protection configuration exports** from repository platform | Development Manager / DevOps | Quarterly | 2 years |
| 6 | **Pull request and code review records** (review comments, approvals, merge history) | Development Manager | Per code change | 3 years |
| 7 | **Secret scanning configuration and findings log** (tool settings, alerts, remediation records) | Security Team / DevOps | Continuous; findings reviewed weekly | 3 years |
| 8 | **MFA enrolment reports** showing coverage across repository users | IT Operations / Security Team | Quarterly | 1 year |
| 9 | **Authentication and access logs** from repository platform | IT Operations | Continuous | Per retention table (1–3 years by event type) |
| 10 | **Backup execution and recovery test records** (backup logs, test reports, RTO measurements) | IT Operations | Backup: daily; Recovery tests: quarterly (Production) / annually (other) | 3 years |
| 11 | **Third-party access register** (contractor details, NDA records, contract dates, access expiry) | Repository Owners / Procurement | Maintained continuously; reviewed monthly | Contract duration + 3 years |
| 12 | **Exception register** (requests, approvals, compensating controls, quarterly reviews) | Information Security Manager | Maintained continuously; reviewed quarterly | Exception duration + 3 years |
| 13 | **Developer security training records** (secret management, repository security practices) | CISO / HR | Annually | Employment duration + 3 years |
| 14 | **Deprovisioning verification records** (termination-triggered revocation confirmations) | IT Operations / HR | Per termination event | 3 years |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, repository platform access reports, branch protection configuration audits, secret scanning tool reports, access review completion records, internal and external audits, and feedback to the policy owner.

**Compliance Metrics**:

| Metric | Target | Measurement Frequency |
|--------|--------|-----------------------|
| Repositories with compliant RBAC and completed quarterly reviews | >= 90% | Quarterly |
| Repositories with required branch protection enabled | >= 95% | Quarterly |
| Repositories with secret scanning enabled and secrets remediated within SLA | >= 90% | Monthly |
| Third-party accounts with valid NDA and current contract | 100% | Monthly |
| MFA enrolment for users with write or admin access | 100% | Quarterly |
| Access deprovisioned within same business day of termination | 100% | Per event |

**Compliance Scoring**:

| Component | Weight | Calculation |
|-----------|--------|-------------|
| Repository Access Compliance | 35% | (Repos with compliant RBAC + completed quarterly reviews) / Total repos x 100 |
| Branch Protection Compliance | 35% | (Repos with required branch protection enabled) / Applicable repos x 100 |
| Secret Management Compliance | 20% | (Repos with scanning enabled + secrets remediated within SLA) / Total x 100 |
| Third-Party Access Compliance | 10% | (Third-party accounts with valid NDA + current contract) / Total third-party accounts x 100 |

**Non-Compliance Handling**: Below 70% requires immediate CISO escalation and remediation plan. 70–89% requires Information Security Manager oversight with monthly reviews. 90% and above follows standard quarterly monitoring.

**Remediation Ownership by Score Component**:

| Component | Below Target | Remediation Owner | Escalation |
|-----------|-------------|-------------------|------------|
| Repository Access Compliance | <90% | Repository Owners + Development Manager | CISO at 30 days overdue |
| Branch Protection Compliance | <95% | DevOps / Development Manager | CISO at 15 days overdue |
| Secret Management Compliance | <90% | Security Team + DevOps | CISO immediately if active secrets exposed |
| Third-Party Access Compliance | <100% | Procurement + Repository Owners | CISO at 5 days overdue (legal/contractual risk) |

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date (maximum 12 months). Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Policy violations shall be documented, investigated by the Information Security Manager, and reported to the CISO.

## SOC 2 Implementation Stages

For organisations pursuing SOC 2 Type II certification, the following phased implementation is recommended:

| Stage | Focus | Key Actions |
|-------|-------|-------------|
| 1 | **Asset inventory** | Complete repository inventory with classification and owner |
| 2 | **RBAC implementation** | Role-based access control with least privilege |
| 3 | **MFA enforcement** | MFA for all write/admin access |
| 4 | **Branch protection** | Protected branches with required reviews |
| 5 | **Secret scanning** | Automated pre-commit and server-side scanning |
| 6 | **Logging and monitoring** | Comprehensive audit logging forwarded to SIEM |
| 7 | **Access reviews** | Quarterly reviews with documented evidence |
| 8 | **Backup and recovery** | Backup strategy with tested recovery |
| 9 | **Third-party controls** | NDA, time-bound access, enhanced review |
| 10 | **Continuous improvement** | Metrics, compliance scoring, quarterly reporting |

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to repository platform capabilities, emerging threats to source code security (supply chain attacks, dependency confusion, CI/CD pipeline compromise), regulatory changes, audit findings, and lessons learned from security incidents.

---

# Areas of the ISO 27001 Standard Addressed

Access to Source Code Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | **8.4 Access to source code** |
| | 8.5 Secure authentication |
| | 8.25 Secure development lifecycle |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures for data protection; source code access control as a technical measure |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 32 — Security of processing (access control as appropriate technical measure) |
| ISO/IEC 27001:2022 | Annex A Control 8.4 — Access to source code |
| ISO/IEC 27002:2022 | Section 8.4 — Implementation guidance for source code access control |
| NIST SP 800-218 (SSDF) | PS.1 — Protect all forms of code from unauthorised access and tampering |
| NIST SP 800-53 Rev 5 | AC-3 (Access Enforcement), AC-6 (Least Privilege), CM-5 (Access Restrictions for Change), AU-2 (Audit Events) |
| CIS Controls v8 | 6.1–6.2 (Access Granting/Revoking), 6.7 (Centralised Access Control), 6.8 (Role-Based Access), 16.1–16.4 (Application Software Security) |
| FINMA (if applicable) | Circular 2023/1 Margin 50–62 — Information security includes source code protection |
| DORA (if applicable) | Art. 9 — ICT asset management includes source code; Art. 15 — Incident reporting includes source code compromise |
| NIS2 (if applicable) | Art. 21(2) — Asset management includes source code; Art. 23 — Incident reporting for source code security incidents |

---

<!-- QA_VERIFIED: 2026-02-07 -->
