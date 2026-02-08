**ISMS-OP-POL-A.8.2-3-5 — Authentication and Privileged Access**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Authentication and Privileged Access |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.2-3-5 |
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

- ISO/IEC 27001:2022 Controls A.8.2, A.8.3, A.8.5 — Privileged access rights, information access restriction, secure authentication

**Related Annex A Controls**:

| Control | Relationship to Authentication and Privileged Access |
|---------|------------------------------------------------------|
| A.5.3 Segregation of duties | SoD enforced through access restrictions and tiered privileges |
| A.5.15–18 Access control and identity management | Identity lifecycle feeds authentication; access rights define restrictions |
| A.5.17 Authentication information | Credential management for passwords, tokens, and secrets |
| A.5.24–28 Incident management | Credential compromise triggers incident response |
| A.8.1 User endpoint devices | Endpoint security supports authentication (device trust, encryption) |
| A.8.9 Configuration management | System configurations enforce authentication and access baselines |
| A.8.15 Logging | Authentication events and privileged actions feed centralised logging |
| A.8.16 Monitoring activities | Real-time monitoring of authentication failures and privileged access |
| A.8.20–22 Network security | Network segmentation supports access zone enforcement |
| A.8.24 Use of cryptography | Cryptographic protection of credentials, tokens, and sessions |

**Related Internal Policies**:

- Identity and Access Management Policy
- Endpoint Security Policy
- Network Security Policy
- Use of Cryptography Policy
- Logging Policy
- Monitoring Activities Policy (A.8.16)
- Incident Management Policy

---

# Authentication and Privileged Access Policy

## Purpose

The purpose of this policy is to ensure that authentication mechanisms are implemented commensurate with the sensitivity of information and systems being accessed, that privileged access rights are restricted and managed according to the principle of least privilege, and that technical access controls enforce authorised access boundaries.

This policy supports Swiss nFADP (revDSG) and the Data Protection Ordinance (DSV) by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data) through authentication and access controls. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply. Strong authentication and privileged access management are key technical measures for demonstrating compliance with data protection obligations under both frameworks.

## Scope

All employees and third-party users.

All authentication mechanisms, privileged accounts, and technical access controls across systems, platforms, and environments owned or operated by the organisation and deemed in scope by the ISO 27001 scope statement.

This includes on-premises, cloud, hybrid, and SaaS environments.

## Principle

Authentication and access controls are implemented on the principle of defence in depth. Users are positively identified and authenticated before gaining access. Privileged access is granted only with documented approval and restricted to the minimum required for the task. Access is denied by default and granted only on explicit authorisation.

All authentication and access decisions shall be risk-based, considering the classification of information and the criticality of the system.

---

## Identity and Access Management Infrastructure

The following table documents the organisation's IAM technology stack. Actual tool selection is organisation-specific; examples are provided for guidance:

| Function | Solution | Owner | Primary Use |
|----------|----------|-------|-------------|
| **Identity Provider (IdP)** | [e.g., Azure Active Directory (Entra ID), Okta, Google Workspace, JumpCloud] | IT Operations | Centralised authentication, SSO, user lifecycle management |
| **Privileged Access Management (PAM)** | [e.g., CyberArk, Delinea (Thycotic), BeyondTrust, Azure AD PIM] | IT Security | Password vaulting, session recording, JIT access, credential rotation |
| **Multi-Factor Authentication (MFA)** | [e.g., Azure MFA, Okta Verify, Duo Security, YubiKey (FIDO2)] | IT Operations | Second-factor authentication for all users |
| **Corporate Password Manager** | [e.g., 1Password Business, Bitwarden Teams, LastPass Enterprise] | IT Security | Secure storage of shared credentials; interim until PAM for service accounts |
| **Single Sign-On (SSO)** | [Integrated with IdP via SAML 2.0 / OIDC] | IT Operations | Application authentication via centralised IdP |
| **Session Recording** | [e.g., PAM-native, CyberArk PSM, Teleport, Windows Defender for Identity] | IT Security | Record and audit Tier 0 privileged sessions |
| **Compromised Credential Screening** | [e.g., Azure AD Password Protection, Have I Been Pwned API, Enzoic] | IT Security | Prevent use of known-breached passwords |
| **Identity Governance** | [e.g., Azure AD Access Reviews, SailPoint, Saviynt, or manual spreadsheet workflow] | IT Security | Access certification campaigns, compliance reporting |

**Integration points**: IdP shall integrate with HR system for joiner/mover/leaver automation. PAM, IdP, and SIEM shall be integrated for centralised monitoring. MFA shall be enforced via IdP conditional access policies. Session recording logs shall forward to SIEM.

---

## Authentication Requirements

### Password Standards

Access to systems and information is authenticated by passwords or stronger mechanisms. The organisation shall enforce the following password standards, aligned with NIST SP 800-63B:

| Requirement | Standard |
|-------------|----------|
| Minimum length | 12 characters (14 for privileged accounts) |
| Complexity | Length over complexity; no mandatory composition rules |
| Maximum length | Systems shall accept at least 64 characters |
| Character support | All printable ASCII characters (including space) and Unicode shall be accepted |
| Screening | Passwords shall be validated against known compromised/breached credential databases at set/change and monthly thereafter |
| Rotation | Event-based only — on suspected or confirmed compromise; periodic forced rotation is not required |
| Initial passwords | Shall be changed on first use |
| Default passwords | Vendor-supplied and default passwords shall be changed immediately upon installation |
| Sharing | Passwords shall not be generic, shared, or set at a group level |
| Confidentiality | Passwords shall be kept confidential and not written down |
| Display | Passwords shall not be displayed when entered |
| Code | Passwords shall not be coded or included in scripts, code, or macros |
| Transmission | Passwords shall be encrypted when transmitted over networks |
| Storage | Passwords shall be stored using approved cryptographic hash functions (bcrypt, scrypt, Argon2, or PBKDF2) and never in plaintext or reversible encryption |
| Lockout | Systems shall lock out users after 6 failed access attempts |
| History | A password history of at least 24 previous passwords shall be maintained to prevent reuse |
| Password managers | Use of organisation-approved password managers is recommended |

**Compromised credential screening implementation options**:

| Option | Implementation | Notes |
|--------|---------------|-------|
| **Azure AD Password Protection** | Enable global banned password list + custom banned list; enforce in cloud and on-premises (via DC agents) | Recommended for Microsoft environments |
| **Have I Been Pwned (HIBP) API** | k-anonymity model (only first 5 chars of hash sent); check at password set/change and monthly scan | Open-source; requires integration effort |
| **Third-party solution** | Enzoic, Specops Password Policy, or equivalent | Commercial; typically includes additional password policy enforcement |

Passwords found in breach databases shall be rejected at set/change and force-changed if detected during monthly scans. Screening coverage metric: percentage of password set/change events validated against breach databases (target: 100%).

### Multi-Factor Authentication (MFA)

Multi-factor authentication shall be required for:

- All privileged and administrator accounts.
- All remote access to organisation networks and cloud services.
- All externally-exposed applications with authentication.
- All access to systems processing confidential or personal data.
- All cloud platform administrative consoles.

**Acceptable MFA methods** (in order of preference):

| Method | Phishing Resistance | Recommended Use |
|--------|---------------------|-----------------|
| Hardware security keys (FIDO2/WebAuthn) | High | Required for Tier 0; recommended for all privileged accounts |
| Authenticator apps (TOTP) | Medium | Acceptable for Tier 1/2 and standard users |
| Push notifications (with number matching) | Medium | Acceptable where number matching is enabled |
| SMS/Voice OTP | Low | Only where other methods are not technically feasible (legacy systems) |

SMS-based OTP should be phased out where possible due to known vulnerabilities (SIM swapping, interception). Systems relying solely on SMS-based MFA shall be documented in the risk register with a migration plan.

**MFA coverage targets**:

- Privileged users: 100% MFA enrolment.
- All users: 95%+ MFA enrolment within 12 months of policy adoption.
- Remote access: 100% MFA enforcement.

Systems unable to support MFA shall be documented in the risk register with technical justification, compensating controls (e.g., network segmentation, enhanced monitoring, IP restriction), and CISO-approved risk acceptance reviewed annually.

### Single Sign-On (SSO)

The organisation shall implement centralised SSO via the identity provider using SAML 2.0 or OIDC with the following targets:

- New SaaS applications: SSO integration required before procurement approval.
- Existing applications: SSO integration prioritised based on risk tier below.
- Target: 80%+ SaaS application integration within 12 months; 90%+ within 24 months.

**SSO integration priority tiers**:

| Priority | Criteria | Timeline |
|----------|----------|----------|
| **Priority 1** | Processes confidential data; >50 users; internet-facing; cloud infrastructure consoles | 30 days |
| **Priority 2** | Processes internal data; 20–50 users; privileged access applications | 90 days |
| **Priority 3** | <20 users; limited data exposure; infrequent use | 180 days |
| **Priority 4** | Legacy applications with SSO limitations; apps scheduled for decommission; vendors not supporting SSO | 12 months (or documented exception) |

An SSO integration inventory shall be maintained listing each application, its SSO status (integrated / in progress / exception), priority tier, and target date. The inventory shall be reviewed quarterly.

Applications without SSO capability require a documented exception with compensating controls (e.g., individual MFA, enhanced monitoring, password manager enforcement).

### Authentication Logging

All authentication events shall be logged and forwarded to the centralised logging system SIEM:

- Successful and failed authentication attempts.
- MFA enrolment and method changes.
- Password changes and resets.
- Account lockouts and unlocks.
- Session creation and termination.

Authentication logs shall be retained for a minimum of 12 months.

**Authentication monitoring alert rules**:

| Alert Rule | Threshold | Severity | Response SLA |
|------------|-----------|----------|--------------|
| Brute force attack | ≥10 failed logins from single IP in 5 minutes | High | 1 hour |
| Credential stuffing | ≥5 failed logins across multiple accounts from single IP in 10 minutes | High | 1 hour |
| Impossible travel | Successful login from locations >500 km apart within 1 hour | High | 1 hour |
| Privileged account — new device | Tier 0/1 login from device not seen in 30 days | Medium | 4 hours |
| Privileged account — unexpected location | Tier 0/1 login from country outside approved list | Critical | Immediate |
| Service account interactive login | Service account used for RDP/SSH/console login | High | 2 hours |
| MFA bypass attempt | Authentication without required MFA | High | 1 hour |
| Break-glass account usage | Emergency/break-glass account authenticates | Critical | Immediate; 24-hour review |
| Account lockout spike | ≥10 lockouts across the estate in 1 hour | Medium | Investigate same business day |

**Approved geographic locations**: Switzerland, [additional countries per business operations]. Logins from unapproved countries shall trigger alerts per table above.

Alert rules shall be reviewed and tuned quarterly to reduce false positive rates. Investigation workflow: receive alert → validate (true/false positive) → enrich with context → escalate if confirmed → document outcome.

### Authentication System Requirements

The main access authentication system shall:

- Not display system or application identifiers until the log-on process has been successfully completed.
- Display a general notice warning that the system should only be accessed by authorised users.
- Not provide help messages during the log-on procedure that would aid an unauthorised user.
- Validate the log-on information only on completion of all input data. If an error condition arises, the system shall not indicate which part of the data is correct or incorrect.
- Protect against brute force log-on attempts.
- Log unsuccessful and successful attempts.
- Raise a security event if a potential attempted or successful breach of log-on controls is detected.
- Not display a password being entered.
- Not transmit passwords in clear text over a network.
- Terminate inactive sessions after a defined period of inactivity.
- Restrict connection times to provide additional security for high-risk applications.

---

## Privileged Access Management

### Privileged Access Principles

Privileged access shall be restricted based on:

- **Least privilege**: Minimum access required to perform job functions.
- **Need-to-know**: Access only to information required for specific tasks.
- **Separation of duties**: Critical functions split across multiple individuals.
- **Time-limited access**: Just-in-time (JIT) provisioning where supported.

### Privileged Account Classification — Admin Tiering Model

The organisation shall implement tiered administration to limit the impact of compromised credentials:

| Tier | Scope | Examples | Requirements |
|------|-------|----------|--------------|
| **Tier 0** | Domain/Enterprise | Domain Admins, Azure/M365 Global Admin, PKI, SIEM | Hardware MFA (FIDO2); dedicated admin workstation; session recording mandatory |
| **Tier 1** | Server/Application | Server admins, DBAs, cloud subscription admins | MFA required; dedicated admin workstation recommended |
| **Tier 2** | Workstation/Endpoint | Desktop support, help desk with local admin | MFA required; standard workstation acceptable |

**Tier isolation requirements**:

- Tier 0 accounts shall never authenticate to Tier 1 or Tier 2 systems.
- Tier 1 accounts shall never authenticate to Tier 2 systems.
- Separate credentials shall be used per tier (e.g., j.smith.t0, j.smith.t1).
- Daily work activities (email, web browsing) shall not be performed on dedicated admin workstations.

**Tier isolation enforcement**:

Technical controls shall enforce tier boundaries. The following are implementation options depending on the organisation's identity platform:

*Conditional Access (Azure AD / Entra ID or equivalent):*

| Policy | Target | Enforcement |
|--------|--------|-------------|
| Require phishing-resistant MFA for Tier 0 | Tier 0 accounts, all cloud apps | FIDO2/WebAuthn only; block other MFA methods |
| Block Tier 0 from non-admin apps | Tier 0 accounts | Block access to Office 365, SharePoint, OneDrive, Teams |
| Require compliant device for admin access | Tier 0/1 accounts | Require compliant or hybrid-joined device |
| Block legacy authentication | All users | Block IMAP, POP3, SMTP AUTH |
| Block access from unapproved countries | All users (exclude break-glass) | Permit: CH + approved countries; block all others |
| Require MFA for all users | All users, all cloud apps | Sign-in frequency: 90 days |
| Block high-risk sign-ins | All users (requires Azure AD P2) | Block sign-ins flagged as high risk by Identity Protection |
| Session timeout for sensitive applications | Finance, HR, customer databases | Re-authentication every 4 hours |

*On-premises enforcement:*

- GPO logon restrictions: deny Tier 0 accounts from logging on locally to Tier 1/2 systems; deny Tier 1 accounts from Tier 2 workstations.
- Network segmentation: Tier 0 admin workstations on dedicated VLAN; Tier 1 on separate VLAN; standard users on corporate VLAN. Firewall rules restrict cross-tier access.

*SIEM alert rules for tier violations:*

| Alert | Severity | Notification |
|-------|----------|-------------|
| Tier 0 authentication on Tier 1/2 system | Critical | CISO immediate |
| Tier 1 authentication on Tier 2 system | High | IT Security Manager |
| Privileged account from unapproved location | High | IT Security Team |

**Privileged Access Workstations (PAW)**:

| Tier | PAW Requirement |
|------|----------------|
| **Tier 0** | PAW mandatory |
| **Tier 1** | PAW recommended; mandatory for Phase 2 |
| **Tier 2** | Standard workstation acceptable |

*PAW configuration baseline (Tier 0/1):*

- **Hardware**: Dedicated physical device; full-disk encryption; TPM 2.0; Secure Boot enabled.
- **Operating System**: Hardened per CIS Benchmark Level 2; automatic updates; no user-installed software (application allowlisting enforced).
- **Network**: Dedicated admin VLAN; firewall rules restrict connections to management targets only; no general internet browsing.
- **Applications**: RDP/SSH client, PAM client, and admin tools only. Email, web browser, Office suite, and collaboration tools (Teams/Slack) are prohibited.
- **Access Control**: Local admin disabled; PAM credentials required; MFA enforced; 10-minute screen lock.
- **Monitoring**: EDR agent installed; all activity forwarded to SIEM; alerts for unauthorised software, connections, or browsing attempts.

**Phased deployment**: Phase 1 (Year 1): Tier 0 PAWs deployed. Phase 2 (Year 2): Tier 1 PAWs deployed. Compensating controls shall be documented for any period where PAWs are not yet in place (e.g., enhanced monitoring, dedicated VMs, restricted admin accounts on standard workstations).

**Deployment status tracking**: The current deployment phase (planning, pilot, partial enforcement, full enforcement) shall be documented for each tier with compensating controls for non-enforced tiers and target completion dates.

### Privileged Account Management

All privileged accounts shall be:

- Not shared or generic (one user, one privileged account per tier).
- Clearly identifiable (naming convention documented and enforced).
- Logged and monitored for anomalous activity.
- Time-bound where feasible (JIT access preferred over standing privileges).
- Registered in a maintained privileged account inventory with owner, tier, purpose, and review date.

### Privileged Access Management (PAM) Solution

The organisation shall implement privileged access controls, which may include a dedicated PAM solution PAM solution (see IAM Infrastructure table) or equivalent manual controls:

| Capability | Requirement | Phased Approach for SMEs |
|------------|-------------|--------------------------|
| **Password vaulting** | Privileged passwords stored in approved vault, not in plaintext | Phase 1: Implement for Tier 0 accounts; expand to Tier 1/2 |
| **Session recording** | Tier 0 sessions recorded; Tier 1 recording recommended | Phase 1: Tier 0 mandatory; Tier 1 as PAM is extended |
| **Just-in-time access** | Temporary privilege elevation with automatic revocation | Phase 2: Implement where PAM supports JIT workflows |
| **Credential rotation** | Service account passwords rotated per schedule below | Phase 1: Manual rotation with documented evidence |

Where a dedicated PAM solution is not yet deployed, compensating controls shall be documented (e.g., manual credential rotation, shared password manager with audit trail, alternative session logging via SIEM).

**Credential rotation requirements**:

| Account Type | Rotation Frequency |
|--------------|--------------------|
| Service accounts (Tier 0) | 90 days maximum |
| Service accounts (Tier 1/2) | 180 days maximum |
| Break-glass accounts | After each use + 365 days maximum |
| Shared admin accounts (discouraged) | 90 days; migrate to individual accounts with CISO exception |

All credentials shall be rotated immediately upon suspected or confirmed compromise, regardless of schedule.

### Service Account Management

Service accounts shall be managed through a defined lifecycle:

1. **Request and approval**: Requester submits request via ticketing system. IT Security Manager approves within 3 business days. Approval criteria: documented business justification, minimum permissions defined, designated owner, designated tier.
2. **Creation**: Naming convention `svc-[system]-[purpose]` (e.g., `svc-erp-backup`). Minimum 20-character random password. Credentials delivered securely via PAM vault or equivalent (never via email or chat).
3. **Inventory**: All service accounts registered with: account name, purpose, owner, tier, permissions, credential location (vault reference), last rotation date, next rotation date.
4. **Access review**: Quarterly attestation by application owners. Unused accounts (no authentication in 90 days) disabled immediately and deleted after 90-day retention.
5. **Credential rotation**: Automated via PAM where supported; manual rotation documented in inventory where PAM is not available.
6. **Decommissioning**: When service is retired, service account disabled immediately, credentials rotated, and account deleted after 90-day retention.

**Service account monitoring**: SIEM alert rules shall detect interactive logon by service accounts, authentication from unexpected locations, and failed authentication attempts. A quarterly discovery scan shall identify undocumented service accounts.

### Just-In-Time (JIT) Privileged Access

JIT access is preferred over standing privileges. The following workflow applies based on available tooling:

**PAM-based JIT** (preferred):

1. User requests elevated privilege via PAM portal with justification.
2. Approval: automatic for pre-approved tasks; manager/IT Security approval for others.
3. PAM issues time-limited credentials (default: 4 hours; maximum: 8 hours).
4. Session recorded (Tier 0 mandatory; Tier 1 recommended).
5. Privileges automatically revoked at expiry.
6. All JIT sessions logged in PAM audit trail.

**Azure AD PIM** (for cloud roles):

1. Eligible role assigned (not active).
2. User activates role with justification and MFA.
3. Approval required for Global Admin and other Tier 0 roles.
4. Time-limited activation (default: 4 hours; maximum: 8 hours).
5. Auto-deactivation at expiry.
6. All activations logged in Azure AD audit log.

**Manual JIT** (interim where PAM/PIM not deployed):

1. User requests access via ticketing system with justification.
2. IT Security approves and adds temporary group membership.
3. Calendar reminder set for revocation time.
4. IT Operations manually revokes access at expiry.
5. Ticket closed with revocation confirmation.

**JIT targets**: Year 1: 50% of Tier 1 access via JIT. Year 2: 80% of Tier 1 access via JIT. Tier 0: standing access for on-call roles; JIT for all others.

### Privileged Access Reviews

| Account Type | Review Frequency |
|--------------|------------------|
| Tier 0 privileged accounts | Quarterly (CISO or IT Security Manager reviews) |
| Tier 1/2 privileged accounts | Quarterly (system owners review) |
| Service accounts | Quarterly (system owners verify continued need) |

**Review process**:

- Access review campaigns initiated via identity governance tool or manual process.
- Reviewers: Direct managers for Tier 1/2; CISO or IT Security Manager for Tier 0.
- Review period: 10 business days to complete.
- Non-response: Reminder at day 5; escalation to reviewer's manager at day 8; access suspended at day 15 if no response.
- Removal requests processed within 48 hours.

### Access Certification Campaign Process

Quarterly access reviews shall follow a structured campaign:

**Week 1 — Campaign preparation**:
- Generate privileged accounts report, service accounts report, and group memberships report from identity provider and PAM.
- Distribute to reviewers: Tier 0 accounts to CISO; Tier 1/2 accounts to system owners; service accounts to application owners.

**Week 2–3 — Review period (10 business days)**:
- Reviewers attest each account: Approve / Revoke / Transfer / Unable to Determine.
- Reminders: Day 5 (automated), Day 8 (escalation to reviewer's manager), Day 10 (final warning — non-response treated as implicit denial, access suspended).

**Week 4 — Remediation**:
- IT Operations processes revocations within 48 hours.
- Summary report generated with actions taken.

**Post-campaign**: Results presented to CISO at next quarterly review. Certification records retained for 3 years.

**Campaign metrics**: Review completion rate (target: 100%); average review time (target: ≤5 business days); revocation rate (healthy range: 5–15%; rates outside this range warrant investigation).

### Break-Glass / Emergency Access

The organisation shall maintain emergency access procedures for situations where normal authentication channels are unavailable:

- Break-glass accounts secured with sealed credentials (physical safe or PAM solution (see IAM Infrastructure table) sealed envelope).
- Multi-person authorisation required for break-glass use (dual control — two individuals required to access credentials).
- All break-glass usage logged, alerted, and reviewed within 24 hours.
- Credentials rotated immediately after use.
- Break-glass accounts tested semi-annually (e.g., January and July) to confirm credentials work and procedures are current.
- Test records shall document the date, tester, successful authentication confirmation, and post-test credential rotation.

---

## Access Restriction

### Enforcement Principles

Access to information and other associated assets shall be restricted in accordance with this policy and the Identity and Access Management Policy:

- **Default deny**: Access denied by default; explicit authorisation required.
- **Role-based access control (RBAC)**: Access based on documented job roles.
- **Attribute-based access control (ABAC)**: Context-aware access (location, device compliance, risk score) where supported by the identity provider (see IAM Infrastructure table).
- **Data classification alignment**: Access restrictions match the classification level of information.

### Technical Access Controls

**Operating system access**:

- File system permissions enforced per data classification.
- Privileged commands restricted to authorised administrators.
- Local administrator rights removed from standard users (managed privilege escalation for exceptions).

**Database access**:

- Direct database access restricted to authorised DBAs.
- Application access via service accounts with minimum privileges.
- Sensitive columns encrypted or masked for non-privileged access.

**Application access**:

- Role-based access within applications.
- Sensitive functions require additional authentication (step-up MFA) where supported.

**API access**:

- API authentication required (OAuth 2.0 or API keys with rotation per the credential rotation schedule).
- Rate limiting enforced on all APIs.
- Sensitive APIs require additional authorisation.

**Cloud resource access**:

- Cloud IAM policies follow least privilege.
- Cross-account access restricted, logged, and reviewed quarterly.
- Resource-level permissions enforced.

### Session Timeouts

System sessions shall enforce the following timeout periods:

| Classification | Idle Timeout | Absolute Timeout |
|---------------|--------------|------------------|
| Confidential / Critical systems | 15 minutes | 8 hours |
| Systems processing sensitive personal data | 5 minutes | 4 hours |
| Privileged admin consoles | 10 minutes | 4 hours |
| Standard business systems | 30 minutes | 12 hours |

Absolute timeout requires re-authentication regardless of activity.

### Network-Based Access Restrictions

- Network segmentation shall separate trust zones to support access restriction (detailed in the Network Security Policy).
- Firewall rules shall enforce access boundaries between network segments.
- Network access control (NAC) or equivalent shall verify endpoint compliance before granting access where feasible.

### Data Masking

The organisation masks data in line with legal and regulatory obligations, including Swiss nFADP and GDPR requirements where applicable. Data masking shall be applied to:

- Personal data displayed in non-production environments.
- Sensitive data fields visible to users without a legitimate need for full access.
- Data presented in reports, dashboards, or logs where full values are not required.

### Access Control Verification

The organisation shall verify access controls through:

- Annual penetration testing that includes access control bypass attempts.
- Quarterly permission audits for critical systems and privileged accounts.
- Automated compliance scanning for configuration drift where feasible.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Executive Management** | Approve policy; allocate budget for authentication infrastructure, MFA deployment, and PAM; review security metrics quarterly |
| **CISO** | Overall accountability for authentication and access security; approve PAM strategy and Admin Tiering Model; approve exceptions (medium/high risk); review quarterly reports |
| **IT Security Manager** | Day-to-day management of authentication infrastructure; monitor authentication and privileged access alerts; conduct quarterly access certification campaigns; approve service account requests; approve low-risk exceptions |
| **IT Operations / IAM Team** | Manage identity provider and SSO infrastructure; process privileged access and JIT requests; maintain MFA enrolment; execute provisioning and deprovisioning; generate access certification reports; maintain service account inventory; manage PAW deployment |
| **System Administrators** | Implement access controls on managed systems; comply with Admin Tiering requirements; use dedicated privileged accounts; report access control anomalies |
| **All Users** | Protect authentication credentials; report suspected credential compromise immediately; complete MFA enrolment within required timeframe; not share accounts or credentials; not attempt to bypass access controls |

---

## Key Performance Indicators

The following metrics shall be tracked to measure the effectiveness of authentication and privileged access controls:

| Metric | Target | Frequency |
|--------|--------|-----------|
| MFA enrolment (all users) | ≥95% | Monthly |
| MFA enrolment (privileged users) | 100% | Monthly |
| Privileged access review completion | 100% | Quarterly |
| Password policy compliance | ≥98% | Monthly |
| SSO application integration | ≥80% (Year 1); ≥90% (Year 2) | Quarterly |
| Privileged session recording (Tier 0) | 100% | Monthly |
| Credential rotation compliance (service accounts) | 100% within schedule | Quarterly |
| Break-glass account test completion | 100% | Semi-annually |
| JIT access adoption (Tier 1) | ≥50% (Year 1); ≥80% (Year 2) | Quarterly |
| Service account inventory completeness | 100% | Quarterly |
| Access certification completion rate | 100% | Quarterly |
| Conditional access policy coverage | 100% of defined policies enforced | Quarterly |
| Compromised credential screening | 100% of set/change events validated | Monthly |

Metrics shall be reported to the CISO quarterly. Metrics falling below target shall include a remediation plan with owner and target date.

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Password policy configuration** evidence (identity provider settings, breach screening configuration) | IT Operations | *Captured annually or upon change* |
| 2 | **MFA enrolment reports** (coverage percentage by user type: privileged, standard, remote) | IT Security | *Monthly for privileged; quarterly for all users* |
| 3 | **SSO application integration inventory** (integrated vs. non-integrated, exception records) | IT Operations | *Reviewed quarterly* |
| 4 | **Privileged account inventory** (account, owner, tier, purpose, last review date) | IT Security | *Reviewed quarterly* |
| 5 | **Privileged access review completion records** (attestation, reviewer, date, actions taken) | IT Security | *Quarterly; retained 3 years* |
| 6 | **Session recording samples** (Tier 0 sessions; random sample reviewed for anomalies) | IT Security | *Reviewed quarterly* |
| 7 | **Break-glass account test records** (date, tester, result, post-test rotation confirmation) | IT Security | *Semi-annually* |
| 8 | **Credential rotation logs** (service accounts, break-glass accounts, shared accounts) | IT Operations | *Per rotation event; audited semi-annually* |
| 9 | **Authentication event logs** (successful/failed logins, lockouts, anomaly investigations) | IT Security | *Retained 12 months; anomalies investigated within 24 hours* |
| 10 | **Penetration test and permission audit reports** (access control findings and remediation status) | IT Security | *Penetration test annually; permission audits quarterly* |
| 11 | **Service account inventory** (account name, owner, tier, purpose, credential location, last/next rotation) | IT Security | *Maintained continuously; reviewed quarterly; retained 3 years* |
| 12 | **JIT access logs** (requests, approvals, duration, auto-revocation confirmation) | IT Security | *Per event; audited quarterly; retained 12 months* |
| 13 | **Access certification campaign records** (campaign results, reviewer attestations, revocations processed) | IT Security | *Quarterly; retained 3 years* |
| 14 | **Conditional access policy documentation** (policy definitions, deployment status, exceptions) | IT Operations | *Reviewed quarterly; updated upon policy changes* |
| 15 | **PAW deployment status** (inventory of PAWs, configuration compliance, deployment phase tracking) | IT Security | *Reviewed quarterly; retained 3 years* |
| 16 | **SSO integration inventory** (applications, SSO status, priority tier, exception records) | IT Operations | *Reviewed quarterly; retained 3 years* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, identity provider configuration audits, MFA coverage reports, privileged access reviews, penetration testing, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team. Maximum exception duration: 12 months, renewable with re-approval.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

**Progressive response** (within rolling 12-month period):

| Occurrence | Response | Timeline | Owner |
|------------|----------|----------|-------|
| First | Awareness reminder and targeted training | Within 5 business days | IT Security |
| Second (within 90 days) | Manager notification + documented warning | Within 3 business days | IT Security + HR |
| Third (within 12 months) | Access restriction pending remediation | Immediate | IT Security + Manager |
| Wilful / critical violation | Disciplinary action per HR policies | Immediate escalation | HR + CISO |

**Critical violations** warranting immediate escalation regardless of prior history:

- Sharing privileged credentials.
- Deliberately bypassing security controls.
- Tier isolation violations.
- Unauthorised use of break-glass accounts.

**Phishing simulation failures** (within rolling 12-month period):

- 1 failure: Targeted awareness training (within 7 days).
- 2 failures: Manager notification + additional training (within 5 days).
- 3+ failures: Privileged access suspended; standard access restricted pending demonstrated improvement.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to authentication standards (including NIST SP 800-63B revisions), emerging threats (credential stuffing, phishing, MFA bypass techniques), regulatory changes, and lessons learned from incidents.

---

# Areas of the ISO 27001 Standard Addressed

Authentication and Privileged Access Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.15 Access control |
| Clause 7.3 Awareness | 5.17 Authentication information |
| Clause 7.5.3 Control of documented information | 5.36 Compliance with policies, rules, and standards |
| | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | **8.2 Privileged access rights** |
| | **8.3 Information access restriction** |
| | **8.5 Secure authentication** |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures including authentication and access controls |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 32 — Security of processing (authentication controls as appropriate measure) |
| ISO/IEC 27001:2022 | Annex A Controls 8.2, 8.3, 8.5 |
| ISO/IEC 27002:2022 | Sections 8.2, 8.3, 8.5 — Implementation guidance |
| NIST SP 800-63B | Digital identity and authentication guidelines (memorised secrets, MFA) |
| NIST CSF 2.0 | PR.AA (Identity Management, Authentication, and Access Control) |
| CIS Controls v8 | Control 5 (Account Management), Control 6 (Access Control Management) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
