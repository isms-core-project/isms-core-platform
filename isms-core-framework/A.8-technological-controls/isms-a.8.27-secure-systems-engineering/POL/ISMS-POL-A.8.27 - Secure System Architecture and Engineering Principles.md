<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.27:framework:POL:a.8.27 -->
**ISMS-POL-A.8.27 — Secure System Architecture and Engineering Principles**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Secure System Architecture and Engineering Principles |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.27 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Technology Officer (CTO)
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.8.25-26-29 (Secure Development Framework)
- ISMS-POL-A.8.28 (Secure Coding)
- ISMS-POL-A.8.9 (Configuration Management)
- ISMS-POL-A.5.8 (Information Security in Project Management)
- ISMS-IMP-A.8.27.1-UG/TG (Security Architecture Review Process)
- ISMS-IMP-A.8.27.2-UG/TG (Threat Modelling Methodology)
- ISMS-IMP-A.8.27.3-UG/TG (Secure Architecture Pattern Catalogue)
- ISMS-IMP-A.8.27.4-UG/TG (Zero Trust Implementation Assessment)
- ISMS-IMP-A.8.27.5-UG/TG (SSE Compliance Dashboard)
- ISO/IEC 27001:2022 Control A.8.27
- INCOSE Systems Engineering Handbook, 5th Edition (2023)
- NIST SP 800-160 Vol. 1 Rev. 1 - Engineering Trustworthy Secure Systems
- NIST SP 800-160 Vol. 2 Rev. 1 - Developing Cyber-Resilient Systems
- NIST SP 800-207 - Zero Trust Architecture

---

## Executive Summary

This policy establishes [Organisation]'s foundational requirements for Secure Systems Engineering (SSE) — the discipline of integrating security into every layer of system architecture throughout the entire system lifecycle.

**Purpose**: Define the principles, approaches, and requirements for engineering trustworthy secure systems. This policy establishes WHAT secure engineering principles apply and WHO is responsible for their implementation. Implementation procedures (HOW) are documented in ISMS-IMP-A.8.27.

**Scope**: This policy applies to ALL systems designed, developed, acquired, integrated, operated, and maintained by [Organisation], including information systems, operational technology, cloud services, and third-party developed systems.

**Foundational Principle**: Security SHALL be as foundational a perspective in system design as system performance and safety. Security is not an add-on but an inherent property of well-engineered systems.

**Key Concept**: This policy implements "Security by Design and Default" — the principle that security must be built into systems from inception, not retrofitted after deployment.

---

# Scope & Control Alignment

## ISO/IEC 27001:2022 Control A.8.27

**ISO/IEC 27001:2022 Annex A.8.27 - Secure System Architecture and Engineering Principles**

> *Principles for engineering secure systems should be established, documented, maintained and applied to any information system development activities.*

**Control Objective**: Ensure security is designed into all architecture layers throughout the system lifecycle, promoting "security by design," zero trust, and defence-in-depth strategies.

**Control Type**: Preventive
**Control Category**: Technological

## Policy Scope

**This policy applies to**:

| Category | Scope |
|----------|-------|
| **Systems** | All information systems, applications, infrastructure, cloud services, OT/ICS systems |
| **Lifecycle Phases** | Concept, development, production, utilisation, support, retirement |
| **Architecture Layers** | Business, data, application, technology, security |
| **Personnel** | System architects, engineers, developers, security professionals, third-party developers |
| **Processes** | System design, development, integration, deployment, operations, decommissioning |

**Relationship to Other Controls**:

| Control | Relationship |
|---------|--------------|
| **A.8.25** | Secure Development Lifecycle - process framework that implements SSE principles |
| **A.8.26** | Application Security Requirements - requirements derived from SSE principles |
| **A.8.28** | Secure Coding - coding standards implementing SSE principles |
| **A.8.29** | Security Testing - validation of SSE implementation |
| **A.5.8** | Project Management - SSE integration into project governance |

## Regulatory Applicability

**Tier 1 - Mandatory Compliance** (All operations):

| Regulation | Key SSE Requirements |
|------------|---------------------|
| **Swiss nDSG** | Article 8 - Technical measures appropriate to risk |
| **EU GDPR** | Article 25 - Data protection by design and by default |
| **ISO/IEC 27001:2022** | Control A.8.27 |

**Tier 2 - Conditional Applicability** (Triggered by business activities):

| Regulation | Trigger | Requirement |
|-----------|---------|-------------|
| **DORA** | EU financial services | ICT risk management framework, secure architecture |
| **NIS2** | Essential/important entity | Security by design requirements |
| **PCI DSS v4.0.1** | Payment card processing | Secure systems development requirements |
| **FINMA** | Swiss financial institution | IT architecture security requirements |

Compliance determination per ISMS-POL-00 (Regulatory Applicability Framework).

---

# Policy Statements

## Foundational Security Engineering Principles

### Core Principles

[Organisation] SHALL apply the following foundational secure systems engineering principles to ALL system development and acquisition activities:

**Principle 1: Security by Design**

Security SHALL be integrated from the earliest stages of system conception:

- Security requirements SHALL be identified during initial concept development
- Security architecture SHALL be defined before detailed design begins
- Security controls SHALL be designed as integral system components, not bolt-on additions
- Security trade-offs SHALL be explicitly documented and approved

**Principle 2: Security by Default**

Systems SHALL be secure in their default configuration:

- Default configurations SHALL implement the most restrictive security settings appropriate for the system's purpose
- Users SHALL not be required to take action to secure the system
- Optional security features SHALL be enabled by default unless business justification exists for disabling
- Default deny SHALL be applied to access controls, network communications, and system capabilities

**Principle 3: Defence in Depth**

Multiple layers of security controls SHALL be implemented:

- No single control SHALL be the sole protection for critical assets
- Controls SHALL be implemented at multiple architecture layers (network, platform, application, data)
- Control failure at one layer SHALL not result in complete compromise
- Layered controls SHALL be complementary, not redundant

**Principle 4: Least Privilege**

All users, processes, and systems SHALL operate with minimum necessary privileges:

- Access rights SHALL be limited to those required to perform authorised functions
- Elevated privileges SHALL be granted only when needed and revoked when no longer required
- Service accounts SHALL have narrowly scoped permissions
- Administrative access SHALL be separated from operational access

**Principle 5: Least Functionality**

Systems SHALL provide only the capabilities required for their intended purpose:

- Unnecessary services, protocols, and features SHALL be disabled or removed
- System functionality SHALL be limited to documented business requirements
- Attack surface SHALL be minimised through function reduction
- Unused ports, interfaces, and capabilities SHALL be disabled

**Principle 6: Fail Secure**

Systems SHALL fail in a secure state:

- System failures SHALL not expose sensitive data or functionality
- Authentication failures SHALL default to deny access
- Error conditions SHALL not reveal security-sensitive information
- Recovery from failure SHALL require re-authentication and re-authorisation

### Zero Trust Architecture Principles

[Organisation] SHALL implement Zero Trust principles for all systems:

**Never Trust, Always Verify**:

- No implicit trust based on network location, device ownership, or previous authentication
- Every access request SHALL be authenticated and authorised regardless of source
- Trust SHALL be continuously evaluated, not granted once and assumed thereafter

**Assume Breach**:

- Design systems assuming adversaries may already have network access
- Internal network traffic SHALL be treated as potentially hostile
- Lateral movement SHALL be restricted through segmentation and access controls
- Detection capabilities SHALL assume perimeter controls may have failed

**Verify Explicitly**:

- Access decisions SHALL be based on all available data points:
  - User identity and authentication strength
  - Device health and compliance status
  - Data sensitivity and classification
  - Access context (location, time, behaviour patterns)
  - Request anomaly detection

**Least Privilege Access**:

- Just-in-time (JIT) access for elevated privileges
- Just-enough-access (JEA) for all access grants
- Risk-based conditional access policies
- Continuous access evaluation and revocation

**Encryption by Default**:

- All data in transit SHALL be encrypted (TLS 1.2+ minimum)
- All data at rest SHALL be encrypted for CONFIDENTIAL+ classification
- Internal service-to-service communication SHALL use encrypted channels
- Encryption keys SHALL be managed per ISMS-POL-A.8.24

### Defence in Depth Implementation

[Organisation] SHALL implement layered security controls across all architecture layers:

| Layer | Security Controls | ISO 27001 Control Mapping |
|-------|------------------|---------------------------|
| **Perimeter** | Firewalls, WAF, DDoS protection, secure gateways | A.8.20, A.8.21, A.8.22 |
| **Network** | Segmentation, micro-segmentation, network access control, IDS/IPS | A.8.20, A.8.22 |
| **Platform** | Hardened configurations, patch management, endpoint protection | A.8.1, A.8.8, A.8.9 |
| **Application** | Input validation, output encoding, authentication, authorisation | A.8.25, A.8.26, A.8.28 |
| **Data** | Encryption, masking, access controls, DLP | A.8.10, A.8.11, A.8.12, A.8.24 |
| **Identity** | MFA, privileged access management, identity governance | A.5.15, A.5.16, A.5.18, A.8.2, A.8.5 |
| **Monitoring** | SIEM, behavioural analytics, threat detection, incident response | A.8.15, A.8.16, A.5.24, A.5.25 |

## System Architecture Requirements

### Architecture Security Review

All new systems and significant changes to existing systems SHALL undergo security architecture review:

**Review Triggers**:

- New system development or acquisition
- Major version upgrades or migrations
- Architecture changes affecting security boundaries
- Integration of new external services or data flows
- Changes to authentication or authorisation mechanisms

**Review Process**:

1. Threat modelling using structured methodology:
   - **STRIDE** as primary methodology for all systems (mandatory)
   - **PASTA** for complex systems requiring attack simulation (optional enhancement)
   - Methodology selection rationale documented in ISMS-IMP-A.8.27.2
2. Security requirements validation against business requirements
3. Architecture pattern review against approved patterns
4. Control design review for defence in depth
5. Risk assessment and residual risk documentation
6. CISO or Security Architect approval before implementation

**Architecture Review Approval Criteria**:

Systems SHALL meet the following criteria before architecture approval:

- ✅ Threat model completed using approved methodology
- ✅ All HIGH and CRITICAL risks have approved treatment plans
- ✅ Architecture implements approved patterns OR deviations have CISO exception approval
- ✅ Defence in depth validated across all architecture layers
- ✅ Zero Trust principles addressed for authentication, authorisation, and data flows
- ✅ Security requirements traceable to business requirements
- ✅ Third-party integrations comply with ISMS-POL-A.5.19-23

**Architecture review SHALL NOT be approved if**:
- Critical risks without treatment plan
- Unapproved pattern deviations without compensating controls
- Missing defence in depth layers for CONFIDENTIAL+ data

**Review Documentation**:

- Security Architecture Document (SAD)
- Threat Model Report
- Security Requirements Traceability Matrix
- Risk Assessment and Treatment Plan
- Architecture approval record

### Secure Architecture Patterns

[Organisation] SHALL maintain a catalogue of approved secure architecture patterns:

**Pattern Categories**:

| Category | Examples |
|----------|----------|
| **Authentication** | SSO integration, MFA implementation, federated identity |
| **Authorisation** | RBAC implementation, attribute-based access, API authorisation |
| **Data Protection** | Encryption at rest, encryption in transit, tokenisation |
| **Network Security** | DMZ architecture, micro-segmentation, API gateway |
| **Integration** | Secure API patterns, message queue security, service mesh |
| **Cloud** | Landing zone architecture, workload isolation, cloud-native security |

**Pattern Catalogue Minimum Content**:

The pattern catalogue SHALL include at minimum:

- **Authentication Patterns**: SSO integration (SAML/OIDC), MFA implementation, API key management
- **Authorisation Patterns**: RBAC with least privilege, attribute-based access for sensitive data
- **Data Protection Patterns**: Encryption at rest (AES-256), encryption in transit (TLS 1.3), tokenisation for PII
- **Network Security Patterns**: DMZ architecture, micro-segmentation, API gateway with WAF
- **Cloud Patterns**: Landing zone architecture (per cloud provider), workload isolation, CSPM integration

**Pattern Documentation Requirements**:
Each pattern SHALL document:
- Security rationale and threat mitigation
- Implementation steps and configuration examples
- Testing and validation procedures
- Common pitfalls and anti-patterns to avoid

**Pattern Catalogue Location**: [SharePoint/Confluence] - Security Architecture Space

**Pattern Governance**:

- Patterns SHALL be documented with security rationale
- Patterns SHALL be reviewed annually for continued appropriateness
- Deviations from approved patterns require Security Architect approval
- New patterns SHALL be validated through threat modelling before approval

### Third-Party and Acquired Systems

Security architecture principles SHALL apply to third-party developed and acquired systems:

**Acquisition Requirements**:

- Security architecture documentation required before procurement approval
- Vendor security assessment per ISMS-POL-A.5.19-23
- Architecture compatibility with [Organisation]'s security standards
- Integration security review before deployment

**Third-Party Development Requirements**:

- Contractual obligation to follow [Organisation]'s SSE principles
- Security architecture review at design milestone
- Evidence of secure development practices
- Security testing before acceptance

**Third-Party Compliance Verification**:

- **Pre-Procurement**: Vendor security assessment per ISMS-POL-A.5.19-23 (architecture documentation reviewed)
- **Contractual Requirements**: SSE principles SHALL be incorporated into development contracts (reference ISMS-IMP-A.5.20)
- **Design Milestone Review**: Security Architect SHALL review architecture documentation at design phase
- **Pre-Acceptance Testing**: Security testing results required before system acceptance (reference ISMS-POL-A.8.29)
- **Ongoing Monitoring**: Annual architecture re-assessment for SaaS/managed services

**Non-Compliance Remediation**: Vendor non-compliance with SSE requirements triggers issue escalation per contract terms and ISMS-POL-A.5.22.

## Engineering Process Integration

### System Lifecycle Integration

SSE principles SHALL be integrated into every phase of the system lifecycle:

| Phase | SSE Activities | Responsible Role | Gate/Milestone |
|-------|---------------|------------------|----------------|
| **Concept** | Security objectives, threat context, risk tolerance, compliance requirements | System Owner + Security Architect | Concept approval |
| **Development** | Security architecture, threat modelling, secure design, security testing | Security Architect + Dev Team | Design freeze |
| **Production** | Security configuration, hardening, penetration testing, security approval | Security Team + Operations | Pre-production approval |
| **Utilisation** | Security monitoring, vulnerability management, incident response | System Owner + Security Operations | Quarterly review |
| **Support** | Security patching, configuration management, access reviews | System Owner + Operations | Monthly/quarterly |
| **Retirement** | Data sanitisation, secure decommissioning, access revocation | System Owner + Security Team | Decommissioning approval |

### Design Principles for Trustworthy Secure Systems

[Organisation] adopts the following design principles aligned with NIST SP 800-160:

**Clear Abstractions**: System components SHALL have well-defined interfaces with clear security boundaries and minimal complexity.

**Modularity and Layering**: Systems SHALL be designed with independent, loosely coupled modules that can be secured, updated, and validated independently.

**Partially Ordered Dependencies**: System components SHALL have well-defined, acyclic dependencies to prevent circular trust relationships and enable systematic security analysis.

**Minimised Sharing**: Shared resources SHALL be minimised to reduce attack surface and prevent unauthorised information flows between components.

**Reduced Complexity**: System designs SHALL favour simplicity; complex systems are harder to secure, verify, and maintain.

**Secure Evolvability**: Systems SHALL be designed to accommodate security updates and improvements without requiring complete redesign.

**Self-Reliant Trustworthiness**: Systems SHALL not depend solely on external entities for security; security mechanisms SHALL be built into the system itself.

---

# Roles & Responsibilities

| Role | Accountability |
|------|----------------|
| **Executive Management** | Approve SSE policy, allocate resources, accept residual architectural risks |
| **CISO** | Policy ownership, SSE standards, architecture risk acceptance, exception approval |
| **Chief Technology Officer (CTO)** | Technical architecture governance, pattern approval, technology standards |
| **Security Architect** | SSE standards development, architecture reviews, pattern catalogue, threat modelling |
| **Enterprise Architect** | Integration of security into enterprise architecture, pattern alignment |
| **System Owners** | SSE compliance for owned systems, architecture documentation, risk ownership |
| **Development Teams** | Implementation of SSE principles, secure design, threat model participation |
| **Third-Party Vendors** | Compliance with contractual SSE requirements |

**Escalation Path**:

- Architecture security concerns: Development Team → Security Architect → CISO
- Pattern deviations: Requestor → Security Architect → CISO
- Architecture risk acceptance: System Owner → Security Architect → CISO → Executive Management

**SSE Training Requirements**:

| Role | Training | Frequency | Evidence |
|------|----------|-----------|----------|
| Security Architects | Threat modelling certification (e.g., STRIDE practitioner) | Initial + refresher every 3 years | Certificate + annual threat model work product |
| System Architects | SSE principles overview, pattern catalogue training | Initial + annual refresh | Training completion record |
| Developers | Secure design fundamentals (aligned with ISMS-POL-A.8.28) | Initial + annual refresh | Training completion + secure coding assessments |

---

# Governance & Compliance

## Assessment Framework

[Organisation] SHALL verify SSE implementation through:

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| Architecture security reviews | Per project milestone | Security Architect | Review reports, threat models |
| Pattern compliance audit | Annual | Security Team | Pattern usage analysis |
| Zero Trust maturity assessment | Annual | CISO | Maturity scorecard |
| Defence in depth validation | Semi-annual | Security Team | Control layer analysis |
| Third-party architecture review | Per acquisition/engagement | Security Architect | Vendor assessments |

**Zero Trust Maturity Assessment Methodology**:

[Organisation] SHALL use **CISA Zero Trust Maturity Model v2.0** (or equivalent framework approved by CISO) to assess Zero Trust implementation maturity.

**Assessment Scope**: Five pillars assessed annually:
1. Identity
2. Devices
3. Networks
4. Applications and Workloads
5. Data

**Maturity Levels** (per CISA model):
- **Traditional** (Level 0): Perimeter-based security
- **Initial** (Level 1): Zero Trust principles acknowledged
- **Advanced** (Level 2): Zero Trust partially implemented
- **Optimal** (Level 3): Zero Trust fully implemented and optimised

**Target Maturity**: [Organisation] targets **Advanced (Level 2)** maturity across all pillars within 24 months of policy approval.

**Assessment Output**: Annual scorecard with pillar-specific maturity levels and improvement roadmap.

**Governance Metrics (Quarterly Dashboard)**:

| Metric | Target | Measurement |
|--------|--------|-------------|
| % of new systems with completed architecture review | 100% | Count of systems with approved review / Total new systems |
| Average time from design to architecture approval | ≤ 15 business days | Mean time from review request to CISO approval |
| Number of active architecture exceptions | ≤ 5 at any time | Count of open exceptions in register |
| Zero Trust implementation maturity score | ≥ Level 2 (Advanced) across all pillars | Annual CISA ZT Maturity Model assessment |
| Pattern adoption rate for new systems | ≥ 80% | Systems using approved patterns / Total systems reviewed |
| Critical/high security findings from architecture reviews | < 10% of reviews | Reviews with critical/high findings / Total reviews |

## Exception Management

Architecture policy exceptions require:

- Documented business justification
- Risk assessment of deviation impact
- Compensating controls specification
- Security Architect recommendation
- CISO approval
- Time-limited approval (maximum 12 months for architecture exceptions)
- Quarterly review for continued necessity

**Not Permissible**:

- Permanent exceptions to core SSE principles
- Exceptions that eliminate defence in depth
- Systems without any architecture security review

---

# ISMS Integration

## Statement of Applicability

| Control | Status | Implementation Reference |
|---------|--------|-------------------------|
| **A.8.27 - Secure System Architecture and Engineering Principles** | Applicable | This policy, ISMS-IMP-A.8.27-UG/TG |

## Related Controls

| Control | Relationship |
|---------|--------------|
| **A.8.25-26-29** | SSE principles inform secure development lifecycle requirements |
| **A.8.28** | Secure coding implements SSE principles at code level |
| **A.8.9** | Configuration management enforces secure baseline configurations |
| **A.5.8** | Project management integrates SSE into project governance |
| **A.8.31** | Environment separation implements SSE architecture patterns |
| **A.8.2-3-5** | Authentication/access implements Zero Trust principles |

## Implementation Resources

| Document | Purpose |
|----------|---------|
| **ISMS-IMP-A.8.27.1-UG/TG** | Security Architecture Review Process |
| **ISMS-IMP-A.8.27.2-UG/TG** | Threat Modelling Methodology |
| **ISMS-IMP-A.8.27.3-UG/TG** | Secure Architecture Pattern Catalogue |
| **ISMS-IMP-A.8.27.4-UG/TG** | Zero Trust Implementation Assessment |
| **ISMS-IMP-A.8.27.5-UG/TG** | SSE Compliance Dashboard |

## External References

| Reference | Purpose |
|-----------|---------|
| **INCOSE SE Handbook 5th Ed. (2023)** | Systems engineering process framework |
| **NIST SP 800-160 Vol. 1 Rev. 1** | Engineering Trustworthy Secure Systems |
| **NIST SP 800-160 Vol. 2 Rev. 1** | Developing Cyber-Resilient Systems |
| **NIST SP 800-207** | Zero Trust Architecture |
| **NIST SP 800-207A** | Zero Trust for Cloud-Native Applications |
| **OWASP SAMM** | Software Assurance Maturity Model |
| **MITRE ATT&CK** | Threat-informed architecture design |

---

# Definitions

| Term | Definition |
|------|------------|
| **Secure Systems Engineering (SSE)** | The discipline of integrating security considerations into all phases of the system lifecycle to produce trustworthy secure systems |
| **Security by Design** | Principle that security is built into systems from inception rather than added after development |
| **Security by Default** | Principle that systems are configured securely out-of-the-box without requiring user action |
| **Defence in Depth** | Layered security approach where multiple controls protect assets so that compromise of one layer does not result in total compromise |
| **Zero Trust** | Security model based on "never trust, always verify" where no implicit trust is granted based on network location or previous authentication |
| **Threat Model** | Structured analysis of potential threats, attack vectors, and countermeasures for a system |
| **Security Architecture** | The design artifacts that describe how security controls are positioned and how they relate to the overall system architecture |
| **Trustworthy Secure System** | A system that can be trusted to operate securely within defined threat context and risk tolerance |
| **Attack Surface** | The sum of all points where an attacker could potentially enter or extract data from a system |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:

- ✅ This policy document (ISMS-POL-A.8.27 v1.0)
- ✅ Approval signatures from CISO, CTO, Executive Management
- ✅ Foundational SSE principles documented (Section 2.1)
- ✅ Zero Trust principles defined (Section 2.1)
- ✅ Defence in depth requirements specified (Section 2.1)
- ✅ Architecture review requirements documented (Section 2.2)
- ✅ Secure architecture patterns referenced (Section 2.2)
- ✅ Lifecycle integration requirements defined (Section 2.3)
- ✅ Roles and responsibilities assigned (Section 3)
- ✅ External framework references documented (Section 5.3)

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

**Evidence Repository and Generation**:

| Evidence Type | Repository Location | Generation Method | Owner | Retention |
|---------------|-------------------|-------------------|-------|-----------|
| **Architecture Review Records** | [GRC Platform] - Architecture Review Module | Generated by Security Architect using review template ISMS-IMP-A.8.27.1-UG/TG | Security Architect | 3 years |
| **Threat Models** | [GRC Platform] - Threat Model Repository | Created during architecture review using STRIDE template ISMS-IMP-A.8.27.2-UG/TG | Security Architect + System Owner | Life of system + 1 year |
| **Pattern Catalogue** | [Confluence/SharePoint] - Security Architecture Space | Maintained by Security Architect, quarterly updates | Security Architect | Indefinite (living document) |
| **Zero Trust Assessment** | [GRC Platform] - Compliance Assessments | Annual self-assessment using CISA ZT Maturity Model v2.0 | CISO | 3 years |
| **Defence in Depth Validation** | [GRC Platform] - Control Validation Module | Semi-annual control layer analysis per ISMS-IMP-A.8.27.4-UG/TG | Security Team | 3 years |
| **Training Records** | [LMS] - Learning Management System | SSE training completion tracked per role requirements | HR + CISO | 3 years post-employment |
| **Third-Party Assessments** | [GRC Platform] - Vendor Risk Module | Vendor architecture security evaluations per ISMS-POL-A.5.19-23 | Security Architect | Active + 2 years post-contract |
| **Exception Register** | [GRC Platform] - Risk & Exception Register | Exception requests approved per Section 4.2 process | CISO | Active + 2 years post-closure |
| **Metrics Dashboard** | [GRC Platform] - Metrics Module | Automated quarterly from architecture review data | Security Team | 3 years |

**Evidence Accessibility**: All evidence SHALL be accessible to internal audit and external certification auditors upon request within 2 business days.

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Chief Technology Officer (CTO)** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes [Organisation]'s foundational requirements for Secure Systems Engineering — the cornerstone of ISMS CORE. Implementation procedures are documented in ISMS-IMP-A.8.27 (UG/TG).*

<!-- QA_VERIFIED: 2026-02-06 -->

