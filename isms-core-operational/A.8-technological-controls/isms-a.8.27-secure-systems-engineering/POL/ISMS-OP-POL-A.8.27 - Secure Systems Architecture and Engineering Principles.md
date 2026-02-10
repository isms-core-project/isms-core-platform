<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.27:operational:OP-POL:a.8.27 -->
**ISMS-OP-POL-A.8.27 — Secure System Architecture and Engineering Principles**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Secure System Architecture and Engineering Principles |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.27 |
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

- ISO/IEC 27001:2022 Control A.8.27 — Secure system architecture and engineering principles
- ISO/IEC 27002:2022 Section 8.27 — Implementation guidance
- NIST SP 800-160 Vol. 1 Rev. 1 — Engineering Trustworthy Secure Systems
- NIST SP 800-207 — Zero Trust Architecture
- NIST SP 800-53 Rev 5 SA-8 — Security and Privacy Engineering Principles
- CIS Controls v8 — Safeguards 4.1, 16.1–16.14 (Application Software Security)

**Related Annex A Controls**:

| Control | Relationship to Secure System Architecture |
|---------|---------------------------------------------|
| A.5.8 Information security in project management | Security architecture requirements integrated into project governance |
| A.8.25 Secure development lifecycle | Architecture principles inform the development process framework |
| A.8.26 Application security requirements | Security requirements derived from architecture principles |
| A.8.28 Secure coding | Coding standards implement architecture principles at code level |
| A.8.29 Security testing in development and acceptance | Testing validates that architecture principles are correctly implemented |
| A.8.31 Separation of development, test, and production environments | Environment segregation is a core architecture principle |
| A.8.9 Configuration management | Configuration baselines enforce secure architecture standards |
| A.8.20–22 Network security | Network architecture implements segmentation and defence in depth |
| A.8.2–3–5 Authentication and privileged access | Authentication architecture implements zero trust principles |
| A.5.19–23 Supplier and cloud services | Third-party systems subject to architecture review |

**Related Internal Policies**:

- Secure Development Lifecycle Policy
- Network Security Policy
- Authentication and Privileged Access Policy
- Configuration Management Policy
- Information Security in Project Management Policy
- Use of Cryptography Policy

---

# Secure System Architecture and Engineering Principles Policy

## Purpose

The purpose of this policy is to establish the rules and principles for engineering secure information systems, ensuring that security is designed into system architecture from inception rather than added after deployment. This policy defines the foundational secure engineering principles that shall be applied to all system development, acquisition, integration, and modification activities.

This policy supports Swiss nFADP (revDSG) by implementing data protection by design and by default (Art. 7) and technical and organisational measures appropriate to risk (Art. 8). The nFADP requires that developers integrate the protection and respect of data subjects' privacy into the very structure of the products and services that process personal data, and that the highest level of security is activated by default without user intervention. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply (Art. 25 — data protection by design and by default; Art. 32 — security of processing).

## Scope

All information systems designed, developed, acquired, integrated, operated, and maintained by the organisation, including:

- Internally developed applications, APIs, and services.
- Infrastructure and platform architecture (on-premises and cloud).
- Third-party developed or acquired systems integrated into the organisation's environment.
- Cloud services, SaaS platforms, and managed services where the organisation defines or influences architecture.
- Operational technology (OT) and industrial control systems (ICS), where applicable.

All employees, contractors, and third-party users involved in system design, architecture, development, and engineering.

**Out of scope**: Standalone end-user devices managed under the Endpoint Security Policy (A.8.1-7-18-19), unless they form part of a system architecture under design review. Physical infrastructure is governed by the Physical Security Policy (A.7.x).

## Principle

Principles for engineering secure systems should be established, documented, maintained and applied to any information system development activities. Security shall be treated as a foundational property of system design — not an afterthought or a bolt-on addition.

All architecture and engineering decisions shall be risk-based, considering the value and classification of information processed, the threat landscape relevant to the system, regulatory requirements, and the organisation's risk appetite.

Where the organisation lacks dedicated security architecture resources — a common situation in small and medium-sized organisations — the CISO shall fulfil the Security Architect function, and external specialist review shall be engaged for High-Risk systems.

---

## Secure Engineering Principles

The organisation shall establish, document, and maintain a set of secure engineering principles that apply to all system development and acquisition activities. These principles shall be reviewed annually and updated to reflect changes in the threat landscape, technology standards, and regulatory requirements.

### Principle 1: Security by Design

Security shall be integrated from the earliest stages of system conception:

- Security requirements shall be identified during initial concept development, alongside functional requirements.
- Security architecture shall be defined before detailed design begins.
- Security controls shall be designed as integral system components, not additions after core functionality is built.
- Security trade-offs shall be explicitly documented, with risk acceptance approved by the CISO before proceeding.

### Principle 2: Security by Default

Systems shall be secure in their default configuration:

- Default configurations shall implement the most restrictive security settings appropriate for the system's intended purpose.
- Users shall not be required to take action to secure the system — security shall be active from first use.
- Optional security features shall be enabled by default unless a documented business justification exists for disabling them.
- Default-deny shall be applied to access controls, network communications, and system capabilities.
- Administrative interfaces shall be disabled or restricted by default.
- Application features requiring elevated privileges shall be explicitly enabled, not enabled by default (e.g., debug logging, remote administration).

**Privacy by Default (nFADP Art. 7)**:

- Default settings shall minimise personal data collection (data minimisation).
- Privacy-enhancing features shall be enabled by default (e.g., data anonymisation, purpose limitation enforcement).
- User consent mechanisms shall default to opt-in, not opt-out.
- Data retention shall default to shortest period unless business justification requires longer retention.

### Principle 3: Defence in Depth

Multiple layers of security controls shall be implemented so that no single point of failure results in total compromise:

- No single control shall be the sole protection for critical assets.
- Controls shall be implemented at multiple architecture layers: network, platform, application, and data.
- Failure of one control layer shall not result in complete compromise of the system.
- Layered controls shall be complementary — each layer addresses different attack vectors.

**Defence in Depth Layers**:

| Layer | Security Controls |
|-------|-------------------|
| **Perimeter** | Firewalls, web application firewalls (WAF), DDoS protection, secure gateways |
| **Network** | Segmentation, network access control, IDS/IPS, encrypted internal communications |
| **Platform** | Hardened configurations, patch management, endpoint protection, secure boot |
| **Application** | Input validation, output encoding, authentication, authorisation, session management |
| **Data** | Encryption at rest and in transit, access controls, data masking, data loss prevention |
| **Identity** | Multi-factor authentication, privileged access management, identity governance |
| **Monitoring** | Centralised logging, behavioural analytics, threat detection, incident response |

### Principle 4: Least Privilege

All users, processes, and systems shall operate with the minimum privileges necessary to perform their authorised function:

- Access rights shall be limited to what is required for the specific task.
- Elevated privileges shall be granted only when needed and revoked when no longer required.
- Service accounts shall have narrowly scoped permissions limited to specific resources and operations (not full database access, not domain administrator).
- Administrative access shall be separated from day-to-day operational access.

### Principle 5: Least Functionality

Systems shall provide only the capabilities required for their intended purpose:

- Unnecessary services, protocols, and features shall be disabled or removed.
- Attack surface shall be minimised through function reduction.
- Unused ports, interfaces, and capabilities shall be disabled.
- Default sample content, test pages, and unused modules shall be removed before deployment.

### Principle 6: Fail Secure

Systems shall fail in a secure state that does not expose sensitive data or functionality:

- System failures shall default to denying access rather than granting access.
- Error conditions shall not reveal security-sensitive information (stack traces, internal paths, database details, version numbers).
- Recovery from failure shall require re-authentication and re-authorisation.
- Graceful degradation shall maintain security controls even when performance is reduced.
- Failure events shall be logged for security monitoring and incident investigation.

**Fail Secure Examples**:

Correct (fail secure):

- Database connection failure: Application returns generic error, denies access.
- Authentication service unavailable: System denies login, does not bypass authentication.
- Firewall rule processing error: Default deny, block traffic.
- Encryption key unavailable: Data access denied until key restored.

Incorrect (fail insecure — avoid):

- Database connection failure: Application grants access assuming credentials are valid.
- Authentication service unavailable: System allows login with cached credentials without expiry check.
- Firewall rule processing error: Fail open, allow all traffic.
- Encryption key unavailable: Data served unencrypted.

### Principle 7: Reduced Complexity

System designs shall favour simplicity — complex systems are harder to secure, verify, and maintain:

- Components shall have well-defined interfaces with clear security boundaries.
- Systems shall be designed with independent, loosely coupled modules that can be secured, updated, and validated independently.
- Shared resources shall be minimised to reduce attack surface and prevent unauthorised information flows between components.
- Dependencies between components shall be well-defined and documented.

**Complexity Management**:

Complexity shall be managed through:

- **Modular design**: Components with single, well-defined purpose.
- **Interface limits**: External interfaces limited to minimum necessary (document and justify each external integration).
- **Dependency tracking**: Maintain dependency map for critical systems; target fewer than 10 external dependencies for Tier 1 systems.
- **Cyclomatic complexity**: Code complexity metrics tracked during development (target: fewer than 10 per function for security-critical code).

**Complexity Review Triggers**:

- System requires more than 5 different authentication mechanisms.
- More than 15 external system integrations.
- Shared resources between trust boundaries without isolation.
- Development team cannot explain data flow in fewer than 15 minutes.

---

## Zero Trust Architecture Principles

The organisation shall adopt Zero Trust principles for all new systems and progressively apply them to existing systems:

**Never Trust, Always Verify**:

- No implicit trust shall be granted based on network location, device ownership, or previous authentication.
- Every access request shall be authenticated and authorised regardless of source — internal or external.
- Trust shall be continuously evaluated, not assumed after initial verification.

**Assume Breach**:

- Systems shall be designed assuming that adversaries may already have access to internal networks.
- Internal network traffic shall be treated as potentially hostile.
- Lateral movement shall be restricted through segmentation and access controls.
- Detection capabilities shall assume perimeter controls may have failed.
- Endpoint Detection and Response (EDR) shall be deployed on all managed devices to detect post-compromise activity.

**Verify Explicitly**:

- Access decisions shall consider all available data points: user identity, device health, data sensitivity, access context (location, time, behaviour), and request anomaly indicators.
- Access decisions shall be logged for audit and investigation purposes.

**Least Privilege Access**:

- Just-in-time (JIT) access for elevated privileges — grant access only when needed, revoke automatically when the task is complete.
- Just-enough-access (JEA) for all access grants — no standing broad permissions.
- Risk-based conditional access policies enforced through the identity provider.

**Zero Trust Implementation Approach**:

| Phase | Activities | Target Timeline |
|-------|-----------|-----------------|
| **Phase 1: Foundation** | Identity-centric access control, MFA for all users, device health verification | Within 12 months of policy approval |
| **Phase 2: Network** | Micro-segmentation for critical systems, encrypted internal communications, network access control | Within 24 months |
| **Phase 3: Continuous** | Continuous access evaluation, behavioural analytics, automated response to anomalies | Within 36 months |

**Zero Trust Implementation Timelines**: The timelines shown assume a medium-sized organisation (50–200 employees) with moderate technical debt. Adjust based on:

- **Small organisations (<50 employees)**: Timelines may be 50% shorter with cloud-native infrastructure.
- **Large organisations (>200 employees)**: Timelines may be 50% longer due to legacy systems and organisational complexity.
- **Technical debt level**: Organisations with significant on-premises infrastructure require longer Phase 2 timelines.

Progress shall be assessed annually against the organisation-specific roadmap, not absolute calendar dates.

The organisation is not expected to achieve full Zero Trust maturity immediately. Each phase shall be planned, resourced, and reviewed. Progress shall be reported to Executive Management annually.

---

## Security Architecture Documentation

All systems classified as High-Risk or Medium-Risk shall have documented security architecture. Low-Risk systems shall have, at minimum, a completed security checklist.

### Documentation Requirements

**High-Risk Systems**:

| Document | Content | Owner |
|----------|---------|-------|
| **Security Architecture Document (SAD)** | System overview, trust boundaries, data flows, security controls per layer, integration points, threat context | CISO / Security Architect |
| **Threat Model** | Identified threats, attack vectors, risk ratings, mitigations, residual risks | CISO / Security Architect |
| **Security Requirements Traceability Matrix** | Security requirements mapped to design elements and test cases | System Owner |
| **Architecture Decision Records (ADRs)** | Security-relevant design decisions with rationale and alternatives considered | System Owner / Development Manager |

**Medium-Risk Systems**:

| Document | Content | Owner |
|----------|---------|-------|
| **Security Architecture Summary** | Abbreviated SAD covering trust boundaries, data flows, and key controls | System Owner |
| **Threat assessment** | Lightweight threat identification and mitigation planning | CISO |

**Low-Risk Systems**:

- Security design checklist (completed and signed off by CISO or delegate).

**Documentation Storage**: Security architecture documentation shall be stored in [Architecture Tool / Confluence / SharePoint] with access restricted to: CISO, Development Manager, System Owner, and personnel with documented need-to-know approved by the CISO. Documentation shall be version-controlled.

**Documentation Currency**: Security architecture documentation shall be reviewed and updated: when significant changes are made to the system, when new threats are identified that affect the system, and at least annually for High-Risk systems.

---

## Architecture Review Process

All new systems and significant changes to existing systems shall undergo security architecture review before implementation.

### Review Triggers

A security architecture review is required when:

- A new system is developed or acquired.
- A major version upgrade or platform migration occurs.
- Architecture changes affect security boundaries or trust zones.
- New external services or data flows are integrated.
- Authentication or authorisation mechanisms are changed.
- Data classification of processed information increases.
- A security incident reveals architectural weaknesses.

### Review Process

| Step | Activity | Responsible |
|------|----------|-------------|
| 1. **Initiation** | System Owner submits architecture review request with system documentation | System Owner |
| 2. **Threat modelling** | Conduct threat modelling using STRIDE methodology (mandatory for High-Risk; recommended for Medium-Risk) | CISO / Security Architect |
| 3. **Requirements validation** | Verify security requirements are complete and aligned with business requirements | CISO |
| 4. **Pattern review** | Assess architecture against approved secure patterns; identify deviations | CISO / Security Architect |
| 5. **Defence in depth validation** | Verify controls are implemented across all relevant architecture layers | CISO |
| 6. **Risk assessment** | Document residual risks and treatment plans for identified gaps | CISO / System Owner |
| 7. **Approval** | CISO approves or returns with required changes | CISO |

**Approval Criteria**: Architecture shall not be approved if:

- Threat modelling has not been completed (High-Risk systems).
- Critical or high risks exist without treatment plans.
- Defence in depth is absent for systems processing Confidential or Restricted data.
- Deviations from approved architecture patterns lack compensating controls and CISO exception approval.

**Review SLA**:

- High-Risk systems (with full threat model): 15 business days from complete submission.
- Medium-Risk systems (summary review): 10 business days.
- Low-Risk systems (checklist review): 5 business days.

Incomplete submissions shall be returned within 3 business days with specific gaps identified. Clock resets upon resubmission of complete documentation.

### Architecture Review Checklist (Medium and High-Risk Systems)

**Identity and Access**:

- [ ] Authentication mechanism documented (SSO, MFA, API keys).
- [ ] Authorisation model defined (RBAC, ABAC).
- [ ] Privileged access separation implemented.
- [ ] Service account permissions minimised.

**Data Protection**:

- [ ] Data classification identified for all processed data.
- [ ] Encryption at rest implemented for Confidential/Restricted data.
- [ ] Encryption in transit (TLS 1.2+) for all network communications.
- [ ] Data retention and deletion mechanisms defined.

**Network Security**:

- [ ] Network segmentation appropriate to system tier.
- [ ] Inbound/outbound firewall rules documented and justified.
- [ ] API gateway or WAF for internet-facing applications.
- [ ] Internal communications encrypted where processing sensitive data.

**Defence in Depth**:

- [ ] At least 3 control layers verified (network, platform, application, data).
- [ ] Single point of failure analysis conducted.
- [ ] Complementary controls confirmed (different attack vectors addressed).

**Monitoring and Logging**:

- [ ] Security event logging configured.
- [ ] Log forwarding to central SIEM/logging platform.
- [ ] Alerting rules defined for critical events.
- [ ] Log retention meets policy requirements.

**Resilience**:

- [ ] Backup and recovery procedures documented.
- [ ] RPO/RTO defined and validated.
- [ ] Disaster recovery plan exists (Tier 1 systems).
- [ ] Redundancy implemented for critical components.

**Threat Modelling** (High-Risk only):

- [ ] STRIDE analysis completed.
- [ ] Attack vectors documented.
- [ ] Mitigations mapped to each threat.
- [ ] Residual risks accepted by CISO.

**Compliance**:

- [ ] nFADP/GDPR requirements assessed (if processing personal data).
- [ ] Industry-specific regulations addressed (if applicable).
- [ ] Data protection by design and by default demonstrated.

### External Security Architecture Review

Organisations shall engage external security architecture specialists when:

| Trigger | Rationale |
|---------|-----------|
| **New High-Risk system** developed in-house without prior secure architecture experience | Independent validation of threat model and design decisions |
| **Cryptographic system design** (custom implementations, key management) | Specialised cryptography expertise required |
| **Payment processing system** | PCI DSS compliance and specialised security requirements |
| **Zero Trust implementation** (initial design) | Complex architecture requiring specialised Zero Trust expertise |
| **Significant incident** revealed architectural weakness | Independent root cause analysis and remediation guidance |
| **Merger/acquisition integration** | Third-party assessment of combined architecture security posture |
| **Regulatory audit finding** related to architecture | Independent validation of remediation design |

External reviewers shall be selected based on: relevant industry certifications (CISSP, CCSP, or equivalent), demonstrated experience with similar architectures, and independence from implementation vendors.

### Threat Modelling

Where threat modelling is required, the STRIDE methodology shall be used as the primary approach:

| STRIDE Category | Threat Type | Example |
|-----------------|------------|---------|
| **Spoofing** | Identity impersonation | Credential theft, session hijacking |
| **Tampering** | Unauthorised modification | Data manipulation, configuration change |
| **Repudiation** | Denying actions | Absence of audit trails |
| **Information Disclosure** | Data exposure | Unencrypted data, verbose error messages |
| **Denial of Service** | Availability disruption | Resource exhaustion, flooding |
| **Elevation of Privilege** | Gaining unauthorised access | Privilege escalation, injection attacks |

Threat models shall be retained for:

- **Active systems**: Lifecycle of the system plus 3 years after decommissioning.
- **Major incidents**: Threat models for systems involved in security incidents shall be retained permanently (minimum 7 years).

Threat models shall be reviewed and updated: at each major release, when the system architecture changes significantly, when new threat intelligence relevant to the system is identified, and at least annually for High-Risk systems.

---

## Technology Selection Security Criteria

When selecting new technologies, platforms, frameworks, or third-party components, security shall be a selection criterion with equal weight to functional requirements.

### Selection Criteria

| Criterion | Requirement |
|-----------|-------------|
| **Vendor security posture** | Vendor provides evidence of secure development practices (e.g., SOC 2, ISO 27001 certification, or equivalent) |
| **Vulnerability history** | No pattern of unresolved critical vulnerabilities; timely patch release track record |
| **Secure defaults** | Technology ships with secure default configuration; does not require extensive hardening to reach acceptable state |
| **Encryption support** | Supports current encryption standards (TLS 1.2 minimum, TLS 1.3 preferred; AES-256 for data at rest) |
| **Authentication integration** | Supports integration with the organisation's identity provider (SAML, OIDC, or equivalent) |
| **Logging and auditability** | Provides security event logging compatible with the organisation's logging infrastructure |
| **Update and patch mechanism** | Vendor provides regular security updates with clear advisory process |
| **End-of-life roadmap** | Clear support lifecycle; no technology at end-of-life or within 12 months of end-of-life shall be selected |
| **Regulatory compliance** | Technology supports compliance with nFADP, GDPR (where applicable), and ISO 27001 requirements |

Technology selection decisions for High-Risk systems shall be documented with security assessment evidence and approved by the CISO before procurement.

---

## Security Baselines

The organisation shall maintain security baselines for each system tier, defining the minimum security controls required.

### System Tier Classification

| Tier | Description | Example Systems |
|------|-------------|-----------------|
| **Tier 1 — Critical** | Systems processing Confidential or Restricted data; internet-facing; core business function | ERP, CRM with customer PII, payment systems, public-facing web applications |
| **Tier 2 — Important** | Systems processing Internal data; limited external exposure; supporting business function | Internal collaboration tools, project management, internal reporting |
| **Tier 3 — Standard** | Systems processing Public data only; no PII; non-critical function | Marketing website (static content), internal wikis (non-sensitive) |

**System Tier Re-Classification**:

System tier shall be reviewed and potentially reclassified when:

- **Data classification increases**: System begins processing Confidential or Restricted data (e.g., Tier 3 reclassified to Tier 1).
- **Internet exposure changes**: Internal system becomes internet-facing (e.g., Tier 2 reclassified to Tier 1).
- **Business criticality increases**: System becomes revenue-critical or a core operational function (e.g., Tier 2 reclassified to Tier 1).
- **Security incident occurs**: Incident reveals system is higher risk than originally assessed.
- **Regulatory scope expands**: System begins processing data subject to regulation (PCI DSS, GDPR).

Re-classification triggers updated security baseline requirements and architecture review. The System Owner shall request a re-classification review from the CISO when any trigger occurs.

### Baseline Requirements by Tier

| Control Area | Tier 1 (Critical) | Tier 2 (Important) | Tier 3 (Standard) |
|-------------|-------------------|--------------------|--------------------|
| **Authentication** | MFA mandatory; SSO integration; session timeouts | MFA mandatory; SSO integration | Password policy compliance |
| **Encryption in transit** | TLS 1.3 required (TLS 1.2 exception with CISO approval) | TLS 1.2 minimum | TLS 1.2 minimum |
| **Encryption at rest** | AES-256 mandatory | AES-256 for PII/sensitive data | Required for systems processing personal data (names, email addresses) even if non-sensitive; not required for truly public data (marketing content, published documentation) |
| **Network segmentation** | Dedicated segment; micro-segmentation where feasible | Segmented from untrusted networks | Standard network controls |
| **Logging** | All security events to centralised [SIEM]; real-time alerting | Security events to centralised logging | Basic access logging |
| **Vulnerability scanning** | Continuous or weekly | Monthly | Quarterly |
| **Penetration testing** | Annually + before initial release + after significant change | Every 2 years | Risk-based decision |
| **Architecture review** | Mandatory (full review with threat model) | Mandatory (summary review) | Security checklist |
| **Backup and recovery** | RPO and RTO defined per BIA; tested annually | Regular backups; recovery tested | Standard backup policy |
| **Access review** | Quarterly | Semi-annually | Annually |

Security baselines shall be reviewed annually by the CISO and updated to reflect current threats, technology changes, and regulatory requirements.

---

## Secure Architecture Patterns

The organisation shall maintain a catalogue of approved secure architecture patterns that system designers shall reference when building new systems or modifying existing ones.

**Pattern Categories**:

| Category | Examples |
|----------|----------|
| **Authentication** | SSO integration (SAML/OIDC), MFA implementation, API key management, certificate-based authentication |
| **Authorisation** | Role-based access control (RBAC), attribute-based access control (ABAC), API authorisation (OAuth 2.0) |
| **Data protection** | Encryption at rest (AES-256), encryption in transit (TLS 1.3), tokenisation for PII, data masking |
| **Network security** | DMZ architecture, micro-segmentation, API gateway with WAF, VPN/ZTNA for remote access |
| **Integration** | Secure API patterns (REST with OAuth 2.0), message queue security, service mesh with mTLS |
| **Cloud** | Landing zone architecture, workload isolation, cloud-native security controls, CSPM integration |

Each approved pattern shall document:

- Security rationale and threat mitigation.
- Implementation guidance.
- Common pitfalls and anti-patterns to avoid.
- Testing and validation criteria.

**Pattern Governance**:

- Approved patterns shall be reviewed annually for continued appropriateness.
- Deviations from approved patterns require CISO approval with documented justification and compensating controls.
- New patterns shall be validated through threat modelling before addition to the catalogue.

**Example Approved Pattern: SSO Integration with SAML 2.0**

**Security Rationale**:

- Centralises authentication, reducing credential sprawl.
- Enables MFA enforcement at identity provider.
- Provides audit trail of application access.
- Supports just-in-time provisioning.

**Implementation Guidance**:

1. Register application with identity provider (Azure AD, Okta, Google Workspace).
2. Configure SAML assertions to include required attributes (email, groups, MFA status).
3. Validate SAML response signatures and certificates.
4. Implement logout propagation (SLO — Single Logout).
5. Set session timeout aligned with organisational policy (4 hours maximum).

**Common Pitfalls**:

- Accepting unsigned SAML assertions.
- Not validating certificate expiration.
- Trusting assertion content without signature verification.
- Not implementing logout propagation (user remains logged into application after IdP logout).

**Testing Criteria**:

- Login redirects to identity provider.
- MFA enforcement visible in authentication flow.
- Invalid SAML response rejected.
- Session expires after timeout period.
- Logout from identity provider logs user out of application.

**Reference Implementation**: [Link to code repository / wiki]

**Pattern Catalogue Location**: [Architecture Tool / Confluence / SharePoint] — accessible to all system architects and developers.

### Common Architecture Anti-Patterns to Avoid

| Anti-Pattern | Risk | Alternative |
|--------------|------|-------------|
| **Shared database across trust boundaries** | Lateral movement; privilege escalation via SQL injection | Database per service or strong schema-level isolation with separate credentials |
| **Hardcoded secrets in configuration** | Credential exposure in version control | Secrets management system (Vault, Key Vault, Secrets Manager) |
| **Authentication bypass for "internal" services** | Assumption that internal network is trusted | Mutual TLS or OAuth 2.0 for service-to-service communication |
| **Logging sensitive data (passwords, tokens, PII)** | Compliance violation; insider threat | Log redaction or tokenisation before logging |
| **Single admin account shared across services** | No accountability; credential sprawl | Service-specific admin accounts with least privilege |
| **Unauthenticated health check endpoints exposing system details** | Information disclosure | Authenticated health checks or minimal response (HTTP 200 only) |
| **Direct database access from web tier** | SQL injection amplification; no defence in depth | API/service layer between web and database |
| **Trusting client-side validation** | Trivial bypass | Server-side validation; client-side as UX enhancement only |

---

## Third-Party and Acquired Systems

Secure engineering principles shall apply to third-party developed and acquired systems that are integrated into the organisation's environment.

**Pre-Acquisition**:

- Security architecture documentation shall be reviewed before procurement approval.
- Vendor security assessment shall be conducted per the Supplier and Cloud Services Policy (A.5.19-23).
- Architecture compatibility with the organisation's security standards shall be verified.

**Contractual Requirements**:

- Third-party developers shall be contractually required to follow the organisation's secure engineering principles.
- Security architecture review shall be required at design milestone.
- Evidence of secure development practices shall be provided.
- Security testing results shall be provided before acceptance.

**Post-Acquisition**:

- Integration security review before deployment into the organisation's environment.
- Annual architecture re-assessment for SaaS and managed services.
- Vendor non-compliance shall trigger issue escalation per contract terms.

**Ongoing Review Triggers for Third-Party Systems**:

- Major version upgrades (e.g., v2.x to v3.x).
- Changes to the third-party system's data processing scope.
- Security incidents affecting the third-party system.
- Annual review for Tier 1 integrations.
- Every 2 years for Tier 2 integrations.
- When vendor SOC 2 or ISO 27001 certification lapses.

---

## Definitions

| Term | Definition |
|------|------------|
| **Secure Systems Engineering (SSE)** | The discipline of integrating security considerations into all phases of the system lifecycle to produce trustworthy systems |
| **Security by Design** | Principle that security is built into systems from inception rather than added after development |
| **Security by Default** | Principle that systems are configured securely out-of-the-box without requiring user action to enable security |
| **Defence in Depth** | Layered security approach where multiple controls protect assets so that compromise of one layer does not result in total compromise |
| **Zero Trust** | Security model based on "never trust, always verify" — no implicit trust is granted based on network location or previous authentication |
| **Threat Model** | Structured analysis of potential threats, attack vectors, and countermeasures for a system |
| **Security Architecture** | Design artifacts describing how security controls are positioned and how they relate to the overall system architecture |
| **Attack Surface** | The sum of all points where an attacker could potentially enter or extract data from a system |
| **STRIDE** | Threat modelling methodology categorising threats as Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege |
| **Security Baseline** | The minimum set of security controls required for a given system tier or classification |

---

## Roles and Responsibilities

| Role | Secure Architecture Responsibilities |
|------|--------------------------------------|
| **Executive Management** | Approve secure engineering policy; allocate resources for architecture reviews; accept residual architectural risks |
| **CISO** | Policy ownership; define and maintain secure engineering principles; conduct or commission architecture reviews; approve architecture exceptions; threat modelling oversight |
| **Development Manager** | Ensure development teams apply secure engineering principles; participate in architecture reviews; maintain technology standards alignment |
| **System Owners** | Submit systems for architecture review; maintain security architecture documentation; own system-specific risks |
| **Developers / Engineers** | Apply secure engineering principles in system design and implementation; participate in threat modelling; use approved architecture patterns |
| **IT Operations** | Implement and maintain security baselines; enforce configuration standards; support architecture review with infrastructure information |
| **Third-Party Vendors** | Comply with contractual secure engineering requirements; provide architecture documentation and security testing evidence |

### Escalation Path

- Architecture security concerns: Developer/Engineer notifies CISO. CISO escalates to Executive Management if resource or organisational change is required.
- Pattern deviations: Requestor submits deviation request to CISO. CISO approves or rejects with documented rationale.
- Architecture risk acceptance: System Owner submits risk assessment to CISO. Risks exceeding the CISO's acceptance threshold are escalated to Executive Management.

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Documented secure engineering principles** (this policy and any supporting standards documents) | CISO | *Reviewed annually; updated upon threat landscape or regulatory change* |
| 2 | **Security architecture documentation** (SAD, threat models, security requirements traceability) for High and Medium-Risk systems | CISO / System Owner | *Per system; updated upon significant change; reviewed annually for High-Risk* |
| 3 | **Architecture review records** (review requests, findings, approval or rejection with rationale) | CISO | *Per review; retained 3 years* |
| 4 | **Threat model reports** (STRIDE analysis, risk ratings, mitigations, residual risks) | CISO | *Per system; retained for lifecycle of system + 3 years; permanently for systems involved in major incidents (minimum 7 years)* |
| 5 | **Approved architecture pattern catalogue** (documented patterns with security rationale) | CISO / Development Manager | *Maintained continuously; reviewed annually* |
| 6 | **Security baseline configurations** (per system tier, with documented minimum controls) | CISO / IT Operations | *Reviewed annually; updated upon technology or threat change* |
| 7 | **Technology selection security assessments** (security evaluation records for new technology procurements) | CISO | *Per procurement; retained 3 years* |
| 8 | **Architecture exception register** (deviations from patterns or principles with CISO approval, compensating controls, and expiry dates) | CISO | *Reviewed quarterly; retained 3 years post-closure* |
| 9 | **Third-party architecture assessments** (vendor security architecture reviews, integration security reviews) | CISO | *Per engagement; retained for contract duration + 2 years* |
| 10 | **Zero Trust implementation progress** (maturity assessment, roadmap, phase completion evidence) | CISO | *Assessed annually; reported to Executive Management* |
| 11 | **Defence in depth validation records** (control layer analysis confirming layered controls across architecture) | CISO / IT Operations | *Semi-annually for Tier 1 systems; annually for Tier 2* |
| 12 | **Training records** (secure architecture and engineering training completion for relevant personnel) | CISO / HR | *Tracked per individual; reviewed annually; target: 100% completion* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, architecture review completion tracking, pattern adoption analysis, security baseline compliance audits, threat model coverage assessments, internal and external audits, and feedback to the policy owner.

The following metrics shall be tracked and reported to the CISO quarterly:

| Metric | Target | Red Threshold |
|--------|--------|---------------|
| New High-Risk systems with completed architecture review | 100% | <100% |
| New Medium-Risk systems with completed architecture review | 100% | <80% |
| Architecture review completion within SLA (risk-based: 5/10/15 business days) | 90% | <70% |
| Approved architecture pattern adoption rate for new systems | 80% | <60% |
| Active architecture exceptions | Minimised; trending downward | >5 concurrent or any >12 months |
| Security baseline compliance (Tier 1 systems) | 100% | <90% |
| Threat models current for High-Risk systems | 100% | <80% |

**Reporting requirements**:
- **Quarterly CISO report**: Architecture review status, pattern adoption, exception register status, baseline compliance.
- **Annual Executive Management report**: Zero Trust maturity progress, architecture programme effectiveness, key risks, and resource requirements.
- **Annual Management Review**: Full secure engineering programme assessment including metrics trends, significant findings, and improvement recommendations.

Metrics breaching red thresholds shall be escalated to the CISO for immediate attention and reported at the next Management Review.

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO in advance, with documented risk acceptance, compensating controls, and a defined review date. Architecture exceptions shall be time-limited (maximum 12 months) and reviewed quarterly. Exceptions shall be reported to the Management Review Team. Permanent exceptions to core secure engineering principles and exceptions that eliminate defence in depth are not permitted.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Systems deployed without required architecture review may be suspended from production pending review and remediation.

## SOC 2 Alignment

This policy supports SOC 2 Trust Services Criteria compliance:

| SOC 2 Criterion | Coverage |
|-----------------|----------|
| **CC3.1** (Specification of objectives) | Security objectives in system design |
| **CC5.2** (General controls over technology) | Architecture controls; architecture changes require change control approval per Configuration Management Policy (A.8.9) |
| **CC6.1** (Logical access security) | Authentication architecture, least privilege, Zero Trust |
| **CC6.6** (External threat protection) | Defence in depth, perimeter controls |
| **CC7.1** (Vulnerability detection) | Vulnerability scanning in baseline requirements |
| **CC7.2** (Anomaly detection) | Monitoring layer in defence in depth; cross-reference Monitoring Activities Policy (A.8.16) |
| **CC9.2** (Vendor risk management) | Third-party architecture review; cross-reference Supplier and Cloud Services Policy (A.5.19-23) |

**SOC 2 Evidence Requirements**:

- Architecture review records (Evidence #3).
- Threat models (Evidence #4).
- Approved pattern catalogue (Evidence #5).
- Security baselines (Evidence #6).
- Security requirements traceability matrix for High-Risk systems.
- Evidence of CISO approval for architecture exceptions (Evidence #8).

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to secure engineering standards (NIST SP 800-160, NIST SP 800-207), evolution of the threat landscape and attack techniques, new architecture patterns and technology standards, regulatory changes (nFADP, GDPR), lessons learned from security incidents and architecture reviews, and audit findings. Nonconformities related to this policy shall be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Areas of the ISO 27001 Standard Addressed

Secure System Architecture and Engineering Principles Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.1 Actions to address risks and opportunities | 5.8 Information security in project management |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 8.25 Secure development lifecycle |
| Clause 8.1 Operational planning and control | 8.26 Application security requirements |
| Clause 9.1 Monitoring, measurement, analysis and evaluation | **8.27 Secure system architecture and engineering principles** |
| Clause 10.2 Nonconformity and corrective action | 8.28 Secure coding |
| | 8.29 Security testing in development and acceptance |
| | 8.31 Separation of development, test, and production environments |
| | 8.9 Configuration management |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 7 — Data protection by design and by default; Art. 8 — Technical and organisational measures appropriate to risk |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 25 — Data protection by design and by default; Art. 32 — Security of processing |
| ISO/IEC 27001:2022 | Annex A Control 8.27 — Secure system architecture and engineering principles |
| ISO/IEC 27002:2022 | Section 8.27 — Implementation guidance for secure system architecture |
| NIST SP 800-160 Vol. 1 Rev. 1 | Engineering Trustworthy Secure Systems — foundational systems security engineering principles |
| NIST SP 800-207 | Zero Trust Architecture — reference architecture for zero trust implementation |
| NIST SP 800-53 Rev 5 | SA-8 (Security and Privacy Engineering Principles) — 28 security engineering principles including clear abstractions, modularity, reduced complexity |
| CIS Controls v8 | Control 4 (Secure Configuration), Control 16 (Application Software Security) — safeguards supporting secure architecture |

---

<!-- QA_VERIFIED: 2026-02-08 -->
