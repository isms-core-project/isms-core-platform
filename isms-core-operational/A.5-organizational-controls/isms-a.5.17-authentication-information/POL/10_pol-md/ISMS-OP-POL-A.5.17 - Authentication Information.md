**ISMS-OP-POL-A.5.17 — Authentication Information**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Authentication Information |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.17 |
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

- ISO/IEC 27001:2022 Control A.5.17 — Authentication information
- NIST SP 800-63B-4 — Digital Identity Guidelines: Authentication and Authenticator Management

**Related Annex A Controls**:

| Control | Relationship to Authentication Information |
|---------|---------------------------------------------|
| A.5.15–18 Access control and identity management | Identity lifecycle feeds authentication; access rights determine credential scope |
| A.5.24–28 Incident management | Credential compromise triggers incident response and forced password change |
| A.8.2 Privileged access rights | Privileged accounts require stricter authentication (MFA, hardware keys) |
| A.8.3 Information access restriction | Authentication enforces access boundaries |
| A.8.5 Secure authentication | Technical authentication mechanism implementation |
| A.8.15 Logging | Authentication events feed centralised logging |
| A.8.16 Monitoring activities | Real-time monitoring of authentication failures and anomalies |
| A.8.24 Use of cryptography | Cryptographic protection of credentials, tokens, and password hashes |

**Related Internal Policies**:

- Identity and Access Management Policy
- Authentication and Privileged Access Policy
- Use of Cryptography Policy
- Logging and Monitoring Policy
- Incident Management Policy

---

# Authentication Information Policy

## Purpose

The purpose of this policy is to ensure that authentication information is securely allocated, managed, protected, and revoked through defined lifecycle processes, and that personnel are instructed on the secure handling of authentication credentials.

This policy establishes requirements for password standards, multi-factor authentication, credential distribution, and protection of authentication secrets to prevent unauthorised access to organisational systems and data.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data) through authentication controls. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

This policy applies to:

- All employees, contractors, and third-party users with access to organisational systems.
- All authentication information including passwords, passphrases, PINs, cryptographic keys, tokens, biometric templates, API keys, certificates, and other authentication secrets.
- All systems, applications, cloud services, network devices, and databases owned or operated by the organisation and deemed in scope by the ISO 27001 scope statement.
- All authentication lifecycle processes: allocation, distribution, usage, storage, reset, and revocation.

## Principle

Authentication information shall be managed on the principles of confidentiality, individual accountability, and defence in depth. Each user shall be positively identified and authenticated before accessing systems or data. Authentication mechanisms shall be commensurate with the sensitivity of the information and systems being accessed.

Passwords alone are not sufficient for high-risk access. Multi-factor authentication provides layered protection against credential compromise. Authentication controls shall be risk-based, considering the classification of information and the criticality of the system.

---

## Authentication Infrastructure

> **Systems specification**: The organisation uses the following systems to implement authentication controls. Placeholder references (e.g., [Identity Provider]) throughout this policy refer to the systems listed below.
>
> | Function | System/Tool | Owner |
> |----------|-------------|-------|
> | **Identity Provider (IdP)** | [e.g., Microsoft Entra ID, Okta, Google Workspace Identity] | IT Operations / IAM Team |
> | **Password Manager** | [e.g., 1Password Business, Bitwarden Enterprise, KeePass + centralised sync] | IT Security |
> | **MFA Platform** | [e.g., built-in IdP MFA, Duo Security, YubiKey management] | IT Operations |
> | **Privileged Access Management (PAM)** | [e.g., CyberArk, Delinea Secret Server, HashiCorp Vault] | IT Security |
> | **Breach Screening Service** | [e.g., Have I Been Pwned API (k-anonymity model), Enzoic, Microsoft Password Protection] | IT Operations |
> | **SIEM / Log Management** | [e.g., Microsoft Sentinel, Splunk, Elastic SIEM] | IT Security |

---

## Authentication Information Allocation

### Identity Verification

Before issuing new or replacement authentication credentials, the identity of the requesting person shall be verified through at least one of the following methods:

- Verification of a pre-registered secondary contact (email, mobile number).
- In-person verification with photo identification.
- Manager or HR confirmation of the user's identity.
- MFA-verified self-service process via the identity provider [Identity Provider].

The verification method used shall be documented for audit purposes.

### Secure Distribution

Authentication information shall be distributed through secure channels. Insecure methods such as unencrypted email or plain-text messaging shall not be used for credential distribution.

| Authentication Type | Distribution Method |
|--------------------|---------------------|
| **Initial passwords** | Secure channel (encrypted email, sealed envelope, or identity provider self-registration); separate from username; forced change on first use |
| **Tokens / hardware keys** | In-person handover with identity verification and signed receipt |
| **Certificates** | Secure certificate enrolment process; verified email or identity provider workflow |
| **API keys** | Encrypted channel; limited validity period; issuance logged; stored in secrets vault |

### Temporary Authentication

Temporary authentication credentials (initial passwords, reset tokens, one-time codes):

- Shall have a maximum validity of 24 hours.
- Shall require change on first use.
- Shall be generated with sufficient randomness and length to resist guessing.
- Shall be invalidated after successful use.

### Default Credential Management

Vendor-supplied and default passwords shall be changed immediately upon installation, before any system is connected to the production network.

Default accounts shall be disabled or renamed where technically feasible.

Where default credentials cannot be changed (vendor firmware dependency, system limitation), the following compensating controls shall be applied:

- Unique strong password set per device (not the vendor default).
- Network segmentation restricting access to the device.
- MFA applied where supported.
- Enhanced monitoring and alerting on the account.
- Credential stored in approved vault [Password Manager].
- Documented exception with CISO approval and annual review.

---

## Password Requirements

### Password Standards (NIST SP 800-63B Aligned)

The organisation shall enforce the following password standards, aligned with NIST SP 800-63B-4:

| Requirement | Standard |
|-------------|----------|
| **Minimum length** | 12 characters (15 characters where the password is the sole authenticator without MFA) |
| **Maximum length** | Systems shall accept at least 64 characters to support passphrases |
| **Character support** | All printable ASCII characters (including space) and Unicode shall be accepted |
| **Complexity rules** | No mandatory composition rules (no required mix of uppercase, lowercase, numbers, symbols); length is the primary strength factor |
| **Breach screening** | Passwords shall be validated against known compromised/breached credential databases (e.g., Have I Been Pwned API, or equivalent breach corpus integrated into [Identity Provider]) at creation and periodically. **Screening frequency**: At password creation (mandatory), at each authentication where technically feasible (real-time screening via IdP integration), and batch screening of all stored password hashes quarterly (offline screening against updated breach corpus). |
| **Rotation** | Event-based only — on suspected or confirmed compromise, shared credential discovery, or personnel role change affecting access scope; periodic forced rotation is not required |
| **Initial passwords** | Shall be changed on first use |
| **Default passwords** | Vendor-supplied and default passwords changed immediately upon installation |
| **Reuse** | A password history of at least 24 previous passwords shall be maintained to prevent reuse |
| **Sharing** | Passwords shall not be generic, shared, or set at a group level |
| **Lockout** | Systems shall lock out users after 6 failed access attempts; lockout duration minimum 15 minutes or until manual reset |
| **Password managers** | Use of organisation-approved password managers [Password Manager] is recommended and supported; systems shall permit paste into password fields |

**Privileged account password standards**:

Privileged accounts (administrator, Tier 0/1 accounts) shall enforce:

- Minimum 16 characters (or 24 characters for service accounts).
- Lockout after 3 failed attempts.
- Breach screening at creation and on each authentication where technically feasible.
- Storage in approved credential vault [Password Manager].

**Rationale for event-based rotation**: NIST SP 800-63B-4 establishes that mandatory periodic password rotation leads to weaker passwords (predictable patterns, minimal incremental changes) without measurable security benefit. Event-based rotation combined with breach screening and MFA provides stronger protection.

### Prohibited Password Practices

Personnel shall not:

- Share passwords with any other person, including IT support staff.
- Write passwords in unprotected locations (sticky notes, unencrypted files, notebooks).
- Store passwords in plaintext files, documents, spreadsheets, or browser auto-fill without an approved password manager.
- Use the same password across multiple systems or services.
- Include passwords in scripts, code, macros, or configuration files.
- Transmit passwords via unencrypted channels (email body, instant message, SMS).

### Password Storage

Systems shall store passwords using approved one-way cryptographic hashing with unique per-password salt:

- **Approved algorithms**: bcrypt, Argon2id, scrypt, or PBKDF2 (with iteration count appropriate to current hardware capability).
- **Plaintext storage is prohibited** under all circumstances.
- **Reversible encryption of passwords is prohibited.**
- Password databases shall be protected with encryption at rest and access restricted to authorised service accounts.

---

## Multi-Factor Authentication

### MFA Requirements

Multi-factor authentication shall be required for the following access types:

| Access Type | MFA Requirement |
|-------------|-----------------|
| **Remote access** (VPN, cloud services, externally-accessible applications) | Mandatory |
| **Privileged / administrator accounts** | Mandatory |
| **Critical systems and infrastructure** | Mandatory |
| **Systems processing personal data** (nFADP / GDPR scope) | Mandatory |
| **Email** (external access) | Mandatory |
| **Cloud platform administrative consoles** | Mandatory |
| **Standard internal access** (on-premises, trusted network) | Risk-based; implementation determined by system classification and recorded in [Identity Provider] conditional access policy |

**MFA coverage targets**:

- Privileged users: 100% MFA enrolment from policy effective date.
- All users (remote access): 100% MFA enforcement.
- All users (all access): 95%+ MFA enrolment within 12 months of policy adoption.

### MFA Factor Types

Acceptable authentication factors shall be drawn from at least two different categories:

| Factor Category | Examples | Notes |
|-----------------|----------|-------|
| **Something you know** | Password, passphrase, PIN | Per password standards above |
| **Something you have** | Hardware security key (FIDO2/WebAuthn), authenticator app (TOTP), smart card | Registered to individual user; hardware keys preferred for privileged access |
| **Something you are** | Fingerprint, facial recognition, iris scan | Biometric template securely stored; used as local unlock factor |

### MFA Method Preference

MFA methods shall be selected with preference for phishing resistance:

| Method | Phishing Resistance | Recommended Use |
|--------|---------------------|-----------------|
| **Hardware security keys** (FIDO2/WebAuthn) | High — cryptographically bound to origin | Required for highest-privilege accounts; recommended for all users |
| **Passkeys** (device-bound, non-exportable) | High — origin-bound, user-verified | Acceptable for all access types; preferred over TOTP |
| **Authenticator apps** (TOTP) | Medium — codes can be phished in real-time | Acceptable for standard and moderate-privilege access |
| **Push notifications** (with number matching) | Medium — requires number matching to mitigate fatigue attacks | Acceptable where number matching is enforced |
| **SMS / Voice OTP** | Low — vulnerable to SIM swapping and interception | Only where no other method is technically feasible; documented exception required |

SMS-based OTP shall be documented in the risk register with a migration plan to a stronger method. New system deployments shall not implement SMS-based MFA as the sole second factor.

**Phishing-resistant authentication migration roadmap**:

The organisation shall plan and execute migration toward phishing-resistant authentication (FIDO2/WebAuthn passkeys) as the primary MFA method. FIDO2 uses public-key cryptography bound to the legitimate service origin, preventing credential phishing even if users are tricked by fraudulent sites.

| Phase | Timeline | Scope | Target |
|-------|----------|-------|--------|
| **Phase 1 — Pilot** | Months 1-3 | IT team, security team, CISO | 100% of pilot group using FIDO2 hardware keys |
| **Phase 2 — Privileged users** | Months 3-6 | All privileged/admin accounts, executives | 100% privileged accounts on FIDO2/passkeys |
| **Phase 3 — High-risk users** | Months 6-12 | Users with access to Confidential data, remote workers | 80%+ of high-risk users migrated |
| **Phase 4 — General rollout** | Months 12-24 | All users | 90%+ of all users using phishing-resistant MFA; SMS/voice OTP eliminated |

**Migration tracking**: Progress reported quarterly to CISO with: users migrated (count and %), remaining SMS/TOTP users, blockers (legacy systems, user resistance), hardware key inventory status.

### MFA Recovery Process

Where a user loses access to their MFA device (lost phone, broken hardware key, factory reset):

1. **Helpdesk contact**: User contacts IT Helpdesk with identity verification (same procedure as helpdesk-assisted password reset).
2. **Temporary access**: Helpdesk issues a time-limited bypass code (maximum 24-hour validity, single-use) to allow immediate access while MFA is re-enrolled.
3. **MFA re-enrolment**: User re-enrols MFA within 24 hours via [Identity Provider] self-service portal. If re-enrolment not completed within 24 hours, access suspended until enrolment completed.
4. **Lost hardware key**: Reported as security incident (potential physical compromise). Previous key deregistered immediately. Replacement key issued via in-person handover with identity verification.
5. **Backup MFA method**: Users are encouraged to register a backup MFA method (e.g., second hardware key stored securely, backup authenticator app). Privileged users shall register at least two independent MFA methods.
6. **Logging**: All MFA recovery events logged in [SIEM] with user, timestamp, verification method, and recovery method used. Anomalous patterns (e.g., same user recovering MFA multiple times) investigated within 24 hours.

### Biometric Authentication Requirements

Where biometric authentication is used (fingerprint, facial recognition, iris scan):

- **Template storage**: Biometric templates shall be stored locally on the device (not centralised) where technically feasible. If centralised storage is required, templates shall be encrypted at rest with AES-256.
- **Liveness detection**: Biometric systems shall implement liveness detection to prevent replay attacks (e.g., photographs, silicone fingerprints).
- **Fallback**: A non-biometric fallback authentication method shall always be available (biometrics shall not be the sole authentication factor).
- **Consent**: Personnel shall provide informed consent before biometric enrolment, in compliance with Swiss nFADP requirements for sensitive personal data processing.
- **Revocation**: Biometric templates shall be deleted upon employment termination or when the individual withdraws consent.
- **Accuracy**: Biometric systems shall be configured with a false acceptance rate (FAR) appropriate to the risk level (recommended: FAR <= 1:50,000 for standard access, FAR <= 1:1,000,000 for privileged access).

### Systems Unable to Support MFA

Systems that cannot support MFA shall be documented in the risk register with:

- Technical justification for the limitation.
- Compensating controls (network segmentation, IP restriction, enhanced monitoring, reduced session timeout).
- CISO-approved risk acceptance.
- Annual review and migration plan where feasible.

---

## Authentication Information Protection

### User Responsibilities

All personnel shall:

- Keep authentication information confidential and not disclose it to any other person.
- Use strong, unique passwords or passphrases for each system.
- Use the organisation-approved password manager [Password Manager] for secure credential storage.
- Report suspected or confirmed credential compromise immediately to the IT service desk and security team.

### Credential Compromise Response

When credential compromise is suspected or confirmed:

1. **Immediate password reset**: Affected user resets password via [Identity Provider] self-service (MFA-verified) or helpdesk-assisted process. For privileged accounts: IT Security forces immediate password reset.
2. **MFA review**: Verify MFA factors have not been tampered with (no unauthorised devices registered). If suspicious MFA devices found, remove all MFA registrations and re-enrol from trusted device.
3. **Session termination**: All active sessions for the affected account terminated immediately via [Identity Provider] admin console.
4. **Breach scope assessment**: IT Security investigates: What was accessed using the compromised credential? Were other accounts affected (credential reuse)? Was data exfiltrated?
5. **Breach screening**: Check compromised password hash against breach corpus. If found in external breach database, assess scope of exposure.
6. **Notification**: If compromise involved personal data access, assess breach notification obligations per A.5.24-28 Incident Management and applicable data protection law.
7. **Root cause**: Determine how credentials were compromised (phishing, malware, social engineering, brute force, breach of external service). Implement targeted remediation (e.g., phishing awareness training if phishing was the vector).
8. **Documentation**: Incident recorded in [ITSM Tool] with: account affected, compromise vector, scope of access during compromise window, remediation actions, root cause, preventive measures.
- Not allow others to use their credentials or authenticate on their behalf.
- Complete MFA enrolment within the required timeframe.
- Not attempt to circumvent authentication controls.

### System Requirements

The main access authentication system shall:

- Not display system or application identifiers until the log-on process has been successfully completed.
- Display a general notice warning that the system should only be accessed by authorised users.
- Not provide help messages during the log-on procedure that would aid an unauthorised user.
- Validate the log-on information only on completion of all input data; if an error condition arises, the system shall not indicate which part of the data is correct or incorrect.
- Protect against brute force log-on attempts (rate limiting, progressive delay, CAPTCHA, or account lockout).
- Log all successful and failed authentication attempts.
- Raise a security event if a potential attempted or successful breach of log-on controls is detected.
- Not display a password being entered (mask input).
- Not transmit passwords in clear text over a network.
- Terminate inactive sessions after a defined period of inactivity.
- Restrict connection times to provide additional security for high-risk applications.

**Session timeout requirements**:

| System Classification | Idle Timeout | Absolute Timeout |
|----------------------|--------------|------------------|
| Confidential / critical systems | 15 minutes | 8 hours |
| Systems processing sensitive personal data | 5 minutes | 4 hours |
| Privileged admin consoles | 10 minutes | 4 hours |
| Standard business systems | 30 minutes | 12 hours |

Absolute timeout requires re-authentication regardless of activity.

### Shared Authentication Information

Shared authentication information is discouraged and shall be avoided wherever possible. Where shared credentials are required (legacy systems, vendor-mandated accounts):

- CISO approval is mandatory with documented business justification.
- Credentials shall be stored in the approved credential vault [Password Manager], not in plaintext documents, email, or chat.
- A named custodian shall be assigned for each shared credential.
- Check-out logging with user identification and timestamp shall be maintained.
- Session recording is recommended for privileged shared accounts where technically feasible.
- Individual accountability shall be maintained through audit logging.
- Access and usage shall be reviewed quarterly; annual reauthorisation required.
- Shared accounts shall be included in the privileged account register and access review process.

---

## Password Reset and Recovery

### Self-Service Password Reset

Where self-service password reset is implemented via [Identity Provider]:

- MFA-based verification (authenticator push, FIDO2, or hardware token) shall be required before a password reset is permitted.
- Knowledge-based security questions shall not be used as the sole verification method due to their susceptibility to social engineering.
- Reset tokens shall be time-limited (maximum 1 hour validity) and single-use.
- All reset activities shall be logged, including the verification method used.
- The user shall be notified of the password change via a registered secondary contact (email or mobile).
- The reset process shall not reveal whether an account exists (prevent account enumeration).

### Helpdesk-Assisted Password Reset

Helpdesk-assisted password resets shall follow this procedure:

1. **Verify identity**: The helpdesk shall verify the caller's identity using at least one pre-registered verification method (secondary email, registered mobile number, manager confirmation, or in-person with photo ID).
2. **Generate temporary password**: A random temporary password shall be generated meeting minimum length requirements.
3. **Communicate securely**: The temporary password shall be communicated via a secure channel (not unencrypted email); where possible, use the identity provider's secure reset link.
4. **Force change**: The temporary password shall expire on first use, requiring the user to set a new password immediately.
5. **Document**: The reset request, verification method used, and timestamp shall be recorded in the IT service management system.

Helpdesk personnel shall not have access to view user passwords after issuance.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Executive Management** | Approve policy; allocate budget for authentication infrastructure (MFA, password manager, identity provider); review security metrics quarterly |
| **CISO** | Policy ownership and accountability; approve MFA strategy and phishing-resistant authentication roadmap; approve exceptions (medium/high risk); review quarterly compliance reports |
| **IT Security Manager** | Day-to-day management of authentication security; monitor authentication alerts and anomalies; conduct quarterly MFA coverage reviews; approve low-risk exceptions |
| **IT Operations / IAM Team** | Manage [Identity Provider] and authentication infrastructure; process credential issuance and resets; maintain MFA enrolment; configure password policy settings; integrate breach screening |
| **Helpdesk** | Execute helpdesk-assisted password resets per documented procedure; verify user identity before credential changes; escalate suspicious reset requests to IT Security |
| **System Owners** | Ensure systems under their ownership comply with authentication requirements; implement MFA where mandated; report authentication control gaps |
| **All Personnel** | Protect authentication credentials; complete MFA enrolment within required timeframe; report suspected credential compromise immediately; not share accounts or credentials; comply with password standards |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Password policy configuration** evidence ([Identity Provider] settings: minimum length, breach screening, lockout, history) | IT Operations | Captured annually and upon change |
| 2 | **MFA enrolment reports** (coverage percentage by user type: privileged, standard, remote) | IT Security | Monthly for privileged; quarterly for all users |
| 3 | **MFA method distribution** (FIDO2, TOTP, push, SMS — migration progress toward phishing-resistant methods) | IT Security | Quarterly |
| 4 | **Breach screening configuration** evidence (integration with compromised credential database, screening frequency) | IT Operations | Annually and upon change |
| 5 | **Default credential scan results** (no default or vendor-supplied credentials in production) | IT Security | Quarterly |
| 6 | **Authentication event logs** (successful/failed logins, lockouts, anomaly investigations, impossible travel alerts) | IT Security | Retained 12 months; anomalies investigated within 24 hours |

**Authentication anomaly examples** (indicators triggering investigation):

| Anomaly Type | Detection Method | Response |
|-------------|-----------------|----------|
| **Impossible travel** | Login from two geographically distant locations within impossible travel time | Block second session; notify user; investigate |
| **Brute force** | > 10 failed login attempts within 5 minutes from single source | Block source IP; notify IT Security |
| **Credential stuffing** | Multiple accounts targeted with failed logins from same IP range | Block IP range; review affected accounts; notify IT Security |
| **MFA fatigue** | > 3 MFA push notifications declined within 10 minutes | Block account; contact user via secondary channel to verify |
| **Unusual hours** | Login outside normal working hours for non-shift workers | Log and review; alert if combined with other anomalies |
| **New device/location** | First-time login from unrecognised device or location | Step-up authentication (additional MFA challenge); notify user |
| **Privilege escalation** | User granted elevated privileges without approved change request | Immediate investigation; revert if unauthorised |
| 7 | **Password reset records** (self-service and helpdesk-assisted; identity verification method documented) | IT Operations | Per event; audited semi-annually |
| 8 | **Shared credential register** (account, custodian, vault location, last review, reauthorisation date) | IT Security | Reviewed quarterly |
| 9 | **Exception register** (systems without MFA, legacy password limitations, SMS-only MFA — with compensating controls and CISO approval) | IT Security | Reviewed quarterly; each exception max 12 months |
| 10 | **Authentication awareness training** completion records | HR / IT Security | Annually |

### Authentication Training Requirements

All personnel shall complete authentication awareness training as follows:

| Training Module | Audience | Frequency | Content |
|----------------|----------|-----------|---------|
| **Security awareness — authentication basics** | All personnel | Annual (part of mandatory security awareness) | Password hygiene, MFA enrolment, phishing recognition, credential reporting |
| **Password manager onboarding** | All personnel | At onboarding + when tool changes | [Password Manager] setup, vault creation, browser extension, mobile app, emergency access |
| **Privileged access training** | Privileged users (admins, DBAs, security team) | Annual + at role assignment | PAM tool usage, credential vault check-out/check-in, session recording awareness, MFA hardware key management |
| **Phishing simulation** | All personnel | Quarterly | Simulated phishing campaigns testing credential harvesting awareness; results reported to CISO; targeted retraining for personnel who fail |
| **Service account management** | System owners, DevOps, IT Operations | Annual | Service account lifecycle, credential storage (no hardcoding), rotation procedures, decommissioning |

**Training effectiveness measurement**: Phishing simulation click rate tracked quarterly (target: < 5%). Personnel failing phishing simulations twice within 12 months receive mandatory 1:1 security coaching.

---

# Policy Compliance

## Compliance Measurement

The information security management team shall verify compliance with this policy through various methods, including but not limited to, identity provider configuration audits, MFA coverage reports, breach screening verification, authentication log analysis, penetration testing, internal and external audits, and feedback to the policy owner.

**Key performance indicators**:

| Metric | Target | Frequency |
|--------|--------|-----------|
| MFA enrolment (all users) | >=95% | Monthly |
| MFA enrolment (privileged users) | 100% | Monthly |
| Password policy compliance | >=98% | Monthly |
| Default credential findings in production | 0 | Quarterly |
| Breach-screened password coverage | 100% of new passwords | Monthly |
| Authentication anomaly investigation (within 24 hours) | 100% | Ongoing |
| SMS-based MFA reduction (year-over-year) | Decreasing trend | Annually |
| Password manager adoption (organisation-wide) | >=80% of users with active vault | Quarterly |
| Password manager unique password ratio | >=90% unique passwords across vaults | Quarterly |
| Service account credential rotation compliance | 100% within defined rotation period | Quarterly |

Metrics shall be reported to the CISO quarterly. Metrics falling below target shall include a remediation plan with owner and target date.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team. Maximum exception duration: 12 months, renewable with re-approval.

**Permitted exceptions** (with compensating controls):

- Legacy systems unable to meet password length requirements (compensating control: network segmentation, enhanced monitoring, restricted access).
- Systems incompatible with MFA (compensating control: IP restriction, enhanced logging, reduced session timeout, VPN-only access).
- Service accounts requiring different authentication policies (compensating control: credential vaulting, automated rotation, enhanced monitoring).

### Service Account Authentication

Service accounts (non-interactive accounts used for application-to-application communication, scheduled tasks, and automation) shall comply with the following requirements:

| Requirement | Standard |
|-------------|----------|
| **Naming convention** | Prefix `svc-` followed by application/function name (e.g., `svc-backup-agent`, `svc-crm-integration`) |
| **Password length** | Minimum 24 characters, randomly generated |
| **Credential storage** | Approved secrets vault [PAM / Password Manager] — not in scripts, config files, or source code |
| **Rotation** | Automated rotation every 90 days where technically feasible; manual rotation every 180 days with documented justification |
| **Interactive logon** | Prohibited — service accounts shall not be used for interactive login. Technical controls (GPO/IdP policy) shall prevent interactive logon where supported. |
| **Ownership** | Named human owner (system owner or application manager) responsible for lifecycle management |
| **Review** | Quarterly review of all service accounts: still required? owner still valid? credentials rotated? permissions still appropriate? |
| **Decommissioning** | Disabled within 5 business days of application decommissioning; credentials rotated immediately |

**Service account inventory**: Maintained in [PAM / Asset Management System] with: account name, purpose, owner, creation date, last rotation date, next rotation date, associated application, permissions scope.
- Systems where SMS is the only available MFA method (compensating control: IP restriction, anomaly monitoring, migration plan documented).

**Not permissible as exceptions**:

- Eliminating MFA for privileged access.
- Permitting password sharing without accountability.
- Allowing default credentials in production environments.
- Disabling authentication logging.

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
- Deliberately bypassing authentication controls.
- Storing credentials in plaintext in shared locations.
- Using default or vendor-supplied credentials in production after notification.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to authentication standards (including NIST SP 800-63B revisions), emerging threats (credential stuffing, phishing, MFA bypass techniques such as adversary-in-the-middle and MFA fatigue attacks), advances in phishing-resistant authentication (FIDO2/WebAuthn, passkeys), regulatory changes, and lessons learned from incidents.

---

# Areas of the ISO 27001 Standard Addressed

Authentication Information Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | **5.17 Authentication information** |
| Clause 7.3 Awareness | 5.15 Access control |
| Clause 7.5.3 Control of documented information | 5.16 Identity management |
| | 5.18 Access rights |
| | 5.36 Compliance with policies, rules, and standards |
| | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | 8.2 Privileged access rights |
| | 8.5 Secure authentication |
| | 8.24 Use of cryptography |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures including authentication controls for data protection |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 32 — Security of processing (authentication controls as appropriate technical measure) |
| ISO/IEC 27001:2022 | Annex A Control 5.17 — Authentication information |
| ISO/IEC 27002:2022 | Section 5.17 — Implementation guidance for authentication information |
| NIST SP 800-63B-4 | Digital identity guidelines — memorised secrets, multi-factor authentication, verifier requirements |
| CIS Controls v8 | Control 5 (Account Management), Control 6 (Access Control Management) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
