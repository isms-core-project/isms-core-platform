**ISMS-OP-POL-A.5.15-16-18 — Identity and Access Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Identity and Access Management |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.15-16-18 |
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

- ISO/IEC 27001:2022 Controls A.5.15, A.5.16, A.5.18 — Access control, identity management, access rights

**Related Annex A Controls**:

| Control | Relationship to IAM |
|---------|---------------------|
| A.5.3 Segregation of duties | SoD matrix enforced through access controls |
| A.5.10 Acceptable use of information | Acceptable use depends on access granted |
| A.5.12–13 Classification and labelling | Classification determines access level required |
| A.5.17 Authentication information | Credential management for authenticated identities |
| A.5.19–23 Supplier relationships | Third-party access governance |
| A.5.24–28 Incident management | Account compromise incident handling |
| A.8.2 Privileged access rights | Privileged access management |
| A.8.3 Information access restriction | Technical enforcement of access rules |
| A.8.5 Secure authentication | Authentication mechanisms for identity verification |
| A.8.11 Data masking | Masking controls aligned with access classification |

**Related Internal Policies**:

- Information Classification and Handling Policy
- Authentication and Privileged Access Policy
- Incident Management Policy
- Information Transfer Policy
- Secure Development Policy

---

# Access Control Policy

## Purpose

The purpose of this policy is to ensure the correct access to the correct information and resources by the correct people, and to manage the full lifecycle of user identities.

This policy supports Swiss nFADP (revDSG) by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data) through access controls. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

All employees and third-party users.
All systems and applications deemed in scope by the ISO 27001 scope statement.
Physical access is defined in the Physical and Environmental Policy.

## Principle

Access control is granted on the principle of least privilege. Users are only provided access to the information they require to perform their tasks and role.

Access is denied by default and granted only with documented approval. All access decisions shall be risk-based, considering the classification of information and the criticality of the system.

---

## Confidentiality Agreements

All employees and contractors who are given access to confidential information shall sign a confidentiality or non-disclosure agreement prior to being given access to information processing facilities.

## Role-Based Access

Access to systems is based on role. Access is granted by the business owner, system owner, or data owner and formally approved.

The organisation shall implement role-based access control (RBAC) as the preferred method for assigning access. Roles shall be documented and reviewed annually by business owners.

## Unique Identifier

Users are assigned a unique username or identifier on the principle of one user, one ID to ensure individual accountability. Usernames and identifiers shall not be shared between users.

Shared accounts are prohibited except where technically unavoidable (legacy systems, vendor-required accounts). Any exception requires written CISO approval with documented business justification, compensating controls (individual user logging, quarterly review), and formal risk acceptance. Shared accounts shall be included in the privileged account register.

## Access Authentication

Users are positively identified and authenticated before gaining access to systems, services, or information.

Multi-factor authentication (MFA) shall be required for:

- All remote access to organisation networks and cloud services.
- All privileged and administrator accounts.
- All externally-exposed applications.
- All systems processing confidential or personal data.

Systems unable to support MFA shall be documented in the risk register with technical justification, compensating controls (e.g., network segmentation, enhanced monitoring), and CISO-approved risk acceptance reviewed annually.

## Access Rights Review

User access to systems shall be reviewed periodically to ensure it is still appropriate and relevant:

| Account Type | Review Frequency |
|--------------|------------------|
| Privileged / administrator accounts | Quarterly |
| Third-party / contractor access | Quarterly |
| Service accounts | Quarterly |
| Standard user accounts | Annually |

Inactive and dormant accounts shall be investigated. An account is considered inactive if it has not successfully authenticated within the specified period. Accounts inactive for more than 45 days shall be disabled. Accounts inactive for more than 90 days shall be removed unless a documented business justification exists.

Service accounts are excluded from inactivity-based disablement but shall be reviewed quarterly to verify they remain in active use and are still required. Unused service accounts shall be disabled immediately upon discovery.

## Privileged Accounts / Administrator Accounts

Administrator accounts shall not be provided to users for standard tasks, including but not limited to laptops and mobile technology.

Where feasible, privileged and administrator users shall be assigned specific privileged accounts in addition to their normal account, for the specific use of completing privileged and administrator tasks.

Privileged and administrator accounts shall:

- Not be shared or generic accounts.
- Be clearly identifiable (naming convention).
- Be logged and monitored.
- Be time-bound where feasible (just-in-time access preferred).
- Be registered in a maintained inventory.

## Service Accounts

Service accounts (non-human accounts used by applications, scripts, or automated processes) shall be managed according to the following requirements:

- Service account creation shall be approved by the system owner and CISO.
- All service accounts shall be documented with purpose, system/application, owner, and review date.
- Service accounts shall be granted only the minimum permissions required for their function.
- Service accounts shall not be used for interactive login by personnel.
- Service account credentials shall be stored in an approved secrets management solution, not hard-coded or stored in plaintext.
- Service account activity shall be logged and monitored for anomalous behaviour.
- Service accounts shall be reviewed quarterly per the access review schedule.

## Passwords

Access to systems and information is authenticated by passwords. The organisation shall enforce the following password standards:

| Requirement | Standard |
|-------------|----------|
| Minimum length | 12 characters |
| Complexity | Length over complexity; no mandatory composition rules (per NIST SP 800-63B) |
| Screening | Passwords shall be validated against known compromised/breached credential databases |
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
| Session timeout | System sessions idle for 15 minutes shall require re-authentication (5 minutes for systems processing sensitive personal data or financial data) |
| Password managers | Use of organisation-approved password managers is recommended |

## User Account Provisioning

Account creation, modification, and deletion shall be performed by authorised personnel and fully documented.

The organisation shall implement a Joiner-Mover-Leaver (JML) process:

| HR Event | Access Action | Timeline |
|----------|---------------|----------|
| New hire | Account creation with role-based access | Access ready by start date |
| Role change | Access adjusted to new role; previous access removed | Within 2 business days |
| Termination (voluntary) | All access revoked | Same business day |
| Termination (for cause) | All access revoked | Immediate (within 1 hour) |
| Contract end | Contractor/vendor access removed | On contract end date |

Business, system, or information owners shall approve access to systems and information. A documented request shall clearly indicate the required access and an authorisation record shall be maintained.

**Access request workflow:**

1. User submits request via IT service desk or access management tool, specifying system, role, and business justification.
2. Line manager approves the business need.
3. System or data owner approves the access level.
4. IT provisions the access and records the authorisation.
5. Requestor confirms access is functional.

Emergency access (break-glass) may be granted by IT with CISO verbal approval and shall be formally documented within 1 business day.

All users requesting password resets or changes to authentication credentials shall have their identity verified using at least one of the following methods:

- Verification of a pre-registered secondary contact (email, phone).
- Challenge-response using pre-established security questions.
- In-person verification with photo identification.
- Manager or HR confirmation of the user's identity.

Self-service password reset via the identity provider (with verified MFA enrolment) is acceptable and does not require additional identity verification.

## Leavers

Line managers and HR shall inform the account provisioning team of a user's leave date.

When a user leaves the organisation, all access shall be revoked on the same business day, as a minimum to the main authentication technology, and to all systems and data recorded in the role-based access list.

User IDs, passwords, and authentication credentials of leavers shall not be reused.

## Authentication

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
- Terminate inactive sessions after a defined period of inactivity, especially in high-risk locations such as public or external areas outside the organisation's security management or on mobile devices.
- Restrict connection times to provide additional security for high-risk applications.

## Remote Access

Remote access to organisation networks, cloud-based services, and externally accessible applications follows the same rules covered by this policy with the additional requirement for multi-factor authentication.

Remote connections shall be set to disconnect after a defined period of inactivity.

A list of users with remote access to internal network systems shall be maintained and reviewed quarterly.

## Third-Party Remote Access

Access is only granted to third parties under current contract with an applicable non-disclosure agreement in place.

Access shall be granted for a specific time, to a specific system, to a specific individual, and provided on receipt of a formal, valid, authorised access request.

Access shall be removed immediately on completion of the requirement or contract end, whichever comes first.

A list of third parties and individuals with access shall be maintained and reviewed quarterly.

## Monitoring and Reporting

Access to systems shall be monitored and reported. Actions that directly or indirectly affect or could affect the confidentiality, integrity, or availability of data shall be managed via the Incident Management process.

## Data Masking

The organisation masks data in line with legal and regulatory obligations, including Swiss nFADP and GDPR requirements where applicable.

---

## Evidence

The following evidence demonstrates compliance with this policy:

- **User account inventory** (active accounts by type: employee, contractor, service, shared) — *maintained in identity provider or access management tool; exported quarterly*
- **JML process records** (joiner/mover/leaver workflow logs with timestamps) — *retained for 12 months after departure; audited semi-annually*
- **Access review completion records** (quarterly privileged, annual standard) — *signed off by system owners; retained for 3 years*
- **Orphaned/dormant account remediation logs** — *reviewed monthly; disabled accounts documented*
- **MFA enrolment records** across systems — *coverage report generated quarterly; target 100% for in-scope systems*
- **Privileged account register and usage logs** — *reviewed quarterly; anomalous usage investigated*
- **Service account register** (owner, purpose, system, review date) — *reviewed quarterly*
- **Third-party access register** with contract expiry dates — *reviewed quarterly; access revoked on contract end*
- **Password policy configuration evidence** (system screenshots or audit exports) — *captured annually or upon change*
- **Access request and approval records** — *retained for 12 months; sample audited during internal audits*

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, access review reports, JML audit trails, privileged access monitoring, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to identity and access management standards, emerging threats, regulatory changes, and lessons learned from incidents.

---

# Areas of the ISO 27001 Standard Addressed

Identity and Access Management Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.3 Segregation of duties |
| Clause 6.2 Information security objectives | 5.4 Management responsibilities |
| Clause 7.3 Awareness | **5.15 Access control** |
| Clause 7.5.3 Control of documented information | **5.16 Identity management** |
| | 5.17 Authentication information |
| | **5.18 Access rights** |
| | 5.36 Compliance with policies, rules, and standards |
| | 8.2 Privileged access rights |
| | 8.3 Information access restriction |
| | 8.5 Secure authentication |
| | 8.11 Data masking |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures including access controls |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 32 — Security of processing (access controls as appropriate measure) |
| ISO/IEC 27001:2022 | Annex A Controls 5.15, 5.16, 5.18 |
| ISO/IEC 27002:2022 | Sections 5.15, 5.16, 5.18 — Implementation guidance |
| NIST SP 800-63B | Digital identity and authentication guidelines |
| CIS Controls v8 | Controls 5 (Account Management) and 6 (Access Control Management) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
