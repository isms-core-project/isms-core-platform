<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S3:framework:GOV-POL:a.5.19-23-s3 -->
**ISMS-POL-A.5.19-23-S3 — ICT Supply Chain Security**
**Control A.5.21: Managing Information Security in the ICT Supply Chain**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | ICT Supply Chain Security |
| **Document Type** | Policy Section |
| **Document ID** | ISMS-POL-A.5.19-23-S3 |
| **Document Creator** | Information Security Officer (ISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISO | Initial section for ISO 27001:2022 Control A.5.21 |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Information Security Officer (ISO)
- Compliance: Legal/Compliance Officer
- Technical: Chief Information Officer (CIO)
- Final Authority: Executive Management (GL)

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.19-23 (Parent Policy - Supplier & Cloud Services Security)
- ISMS-POL-A.5.19-23-S1 (Supplier Relationship Fundamentals)
- ISMS-POL-A.5.19-23-S2 (Supplier Agreement Requirements)
- ISO/IEC 27001:2022 Control A.5.21
- ISO/IEC 27036-3 (ICT supply chain security)
- NIST SP 800-161 (Cybersecurity Supply Chain Risk Management)

---

# Purpose

This section defines requirements for managing information security risks within the ICT supply chain, including sub-suppliers, component providers, and software dependencies. It addresses the "supplier's supplier" problem and supply chain attack vectors.

**Critical Principle - "Trust Cascades Through the Chain"**: Your suppliers' security posture depends on their suppliers, who depend on their suppliers. SolarWinds, Log4Shell, and MOVEit breaches demonstrate supply chain compromise as a force multiplier - one backdoor in a widely-used component grants attackers access to thousands of downstream organizations. This policy requires systematic visibility, security requirement propagation, and continuous monitoring throughout multi-tier ICT supply chains.

**ISO/IEC 27001:2022 Control A.5.21 - Managing Information Security in the ICT Supply Chain**

> *Processes and procedures should be defined and agreed upon with suppliers to manage information security risks associated with the information and communication technology (ICT) services and product supply chain.*

**Control Objective**: Manage information security risks within the ICT supply chain including sub-suppliers, components, and software dependencies.

**ISO/IEC 27002:2022 Guidance Summary**:

- ICT supply chain risks shall be identified and assessed systematically
- Security requirements for ICT products and services shall be specified in procurement processes
- Supplier sub-suppliers (supply chain transparency) shall be evaluated and disclosed
- Software supply chain security shall be addressed including dependencies, libraries, and open-source components
- Hardware supply chain security shall be considered including counterfeit detection and tampering protection
- Supply chain continuity and resilience shall be planned for critical ICT services
- Supplier changes and updates shall be managed through formal change control processes
- Supply chain risk assessment shall include geopolitical, concentration, and single-source dependencies

---

# Scope

## Supply Chain Elements

| Element | Description | Examples |
|---------|-------------|----------|
| **Sub-suppliers** | Suppliers engaged by primary suppliers | Subcontractors, sub-processors, service providers to suppliers |
| **Fourth parties** | Suppliers to sub-suppliers | Infrastructure providers to SaaS vendors, data centers for cloud providers |
| **Software components** | Code dependencies and libraries | Open source packages, SDKs, APIs, frameworks |
| **Hardware components** | Physical components in ICT products | Processors, memory modules, network chips, firmware |
| **Service dependencies** | Services required by primary services | DNS providers, CDN networks, payment gateways, identity providers |
| **Development tools** | Tools used to build/deliver products | CI/CD platforms, code repositories, build systems |

## Supply Chain Risk Categories

| Risk Category | Description | Impact |
|---------------|-------------|--------|
| **Compromise risk** | Malicious code or backdoors inserted into supply chain | Data breach, system compromise, espionage |
| **Availability risk** | Supply chain disruption or single point of failure | Service outage, business disruption, delivery delays |
| **Integrity risk** | Unauthorized modifications to components or services | Data corruption, system instability, compliance violations |
| **Compliance risk** | Regulatory violations via supply chain (GDPR, DORA, NIS2) | Fines, sanctions, legal liability, reputational damage |
| **Concentration risk** | Over-reliance on single supplier/component/jurisdiction | Widespread impact from single failure, vendor lock-in |
| **Geopolitical risk** | Supply chain exposed to hostile jurisdictions or sanctions | Data access by foreign governments, service disruption |

---

# Sub-Supplier Management

## Sub-Supplier Visibility Requirements

| Supplier Level | Visibility Requirement |
|----------------|------------------------|
| Level 1 (Critical) | Full sub-supplier register for all data-processing and critical service activities |
| Level 2 (High) | Sub-supplier register for material services or data access |
| Level 3 (Medium) | Awareness of key sub-suppliers upon request |
| Level 4 (Low) | Not required |

**Regulatory Enhancement**:

- **DORA entities**: Full sub-outsourcing register required per Article 30, including fourth-party visibility
- **NIS2 entities**: Sub-supplier disclosure for critical services per Article 21 supply chain requirements

## Sub-Supplier Register

For Level 1 and Level 2 suppliers, maintain comprehensive visibility including:

| Field | Description | Update Trigger |
|-------|-------------|----------------|
| Sub-supplier name | Legal entity name and identifier | New engagement |
| Sub-supplier type | Category (infrastructure, development, support, processing) | Service change |
| Services provided | Specific services sub-supplier provides to primary supplier | Scope change |
| Data access | Whether sub-supplier accesses [Organization] data, classification level | Access change |
| Processing location | Geographic location(s) of data processing or service delivery | Location change |
| Certification status | Security certifications held (ISO 27001, SOC 2) | Cert expiry/renewal |
| Criticality | Impact if sub-supplier fails (Critical/High/Medium/Low) | Annual review |
| Approval status | [Organization] approval (Approved/Pending/Rejected) | Review decision |
| Contract terms | Key security obligations flowing to sub-supplier | Contract change |

**Register Maintenance**:

- Updated within 10 business days of sub-supplier changes
- Quarterly review for accuracy and completeness
- Annual reconciliation with supplier provided documentation

## Sub-Supplier Control Requirements

**Primary suppliers shall:**

| Requirement | Level 1 | Level 2 | Level 3-4 |
|-------------|---------|---------|-----------|
| Notify [Organization] of sub-supplier changes | ✓ 30 days prior | ✓ Before engagement | — |
| Obtain written approval for new sub-suppliers | ✓ Required | ✓ Notification sufficient | — |
| Flow security requirements to sub-suppliers | ✓ Verbatim | ✓ Equivalent | — |
| Remain fully liable for sub-supplier acts | ✓ Required | ✓ Required | ✓ Required |
| Provide sub-supplier audit reports on request | ✓ Within 30 days | ✓ Best effort | — |
| Allow [Organization] objection to specific sub-suppliers | ✓ 14-day objection window | ✓ Reasonable objection | — |
| Maintain sub-supplier register | ✓ Current, comprehensive | ✓ Key sub-suppliers | — |
| Perform sub-supplier due diligence | ✓ Equivalent to [Organization]'s | ✓ Risk-based | — |

## Sub-Supplier Change Process

```
┌─────────────────────────────────────────────────────────────┐
│ SUB-SUPPLIER CHANGE NOTIFICATION PROCESS                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Supplier notifies [Organization] of planned change      │
│     • Sub-supplier name and details                         │
│     • Services to be provided                               │
│     • Data access requirements                              │
│     • Geographic locations                                  │
│     • Security certifications                               │
│                         ↓                                   │
│  2. [Organization] Security reviews sub-supplier            │
│     • Certifications (ISO 27001, SOC 2)                     │
│     • Data access scope and classification                  │
│     • Geographic location and jurisdiction                  │
│     • Concentration risk impact                             │
│     • Regulatory implications (DORA, NIS2, GDPR)            │
│                         ↓                                   │
│  3. [Organization] responds (within 14 days)                │
│     • APPROVED: Proceed with engagement                     │
│     • REQUEST MORE INFO: Additional documentation needed    │
│     • OBJECT: Valid security/compliance reason provided     │
│                         ↓                                   │
│  4. If objection: Supplier proposes alternative or          │
│     mitigation controls                                     │
│                         ↓                                   │
│  5. Update sub-supplier register and contract amendments    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Objection Grounds**:

- Sub-supplier located in high-risk jurisdiction
- Sub-supplier lacks required certifications
- Sub-supplier has history of security incidents
- Concentration risk (same sub-supplier across multiple suppliers)
- Regulatory incompatibility (DORA, NIS2, GDPR)

---

# Fourth-Party Risk Management

## Fourth-Party Visibility

Fourth parties are suppliers to your suppliers' suppliers (e.g., the infrastructure provider hosting your SaaS vendor's cloud platform).

| Approach | Description | Applicability |
|----------|-------------|---------------|
| **Direct visibility** | Request fourth-party information from supplier with documentation | Level 1 suppliers for critical services |
| **Certification reliance** | Supplier's ISO 27001/SOC 2 certification covers fourth-party management | Level 2 suppliers, supplement direct visibility for Level 1 |
| **Contractual flow-down** | Require supplier to impose security requirements on all fourth parties | All suppliers with data access |

## Critical Fourth-Party Dependencies

Identify and document fourth-party dependencies for:

**Infrastructure Services**:

- Compute platforms (AWS, Azure, GCP underlying SaaS vendors)
- Storage providers (object storage, block storage, backup)
- Network providers (internet connectivity, private links, CDN)

**Security Services**:

- Identity providers (SSO, MFA, directory services)
- Encryption services (key management, HSM, certificate authorities)
- Monitoring services (SIEM, log aggregation, threat intelligence)

**Operational Services**:

- DNS providers (critical for availability)
- CDN networks (content delivery, DDoS protection)
- Payment processors (financial transaction handling)

## Fourth-Party Risk Indicators

| Indicator | Risk Signal | Mitigation |
|-----------|-------------|------------|
| Supplier uses single fourth-party for critical function | Concentration risk | Require supplier redundancy or contingency plan |
| Fourth-party located in high-risk jurisdiction (US CLOUD Act, sanctions) | Geopolitical risk | Assess data residency, encryption, contractual protections |
| Fourth-party has history of incidents or outages | Reliability risk | Request incident history, BC/DR evidence |
| No contractual controls over fourth-party | Compliance risk | Ensure flow-down requirements in supplier contract |
| Fourth-party lacks security certifications | Security risk | Require supplier due diligence documentation |

**Concentration Risk Assessment**: If multiple Level 1 suppliers depend on same fourth-party (e.g., all SaaS vendors use AWS), assess:

- Impact if fourth-party fails
- Alternative suppliers available
- Business continuity implications
- Mitigation strategies (multi-cloud, hybrid architecture)

---

# Software Supply Chain Security

## Software Component Risks

| Risk | Description | Mitigation |
|------|-------------|------------|
| Vulnerable dependencies | Known CVEs in libraries, frameworks, or open-source components | Continuous vulnerability scanning, Software Composition Analysis (SCA), timely patching |
| Malicious packages | Typosquatting attacks, compromised legitimate packages, backdoors | Package verification, checksum validation, trusted repository sources only |
| Abandoned software | Unmaintained components without security updates | Lifecycle monitoring, migration to maintained alternatives, vendor notification |
| License compliance | Incompatible licenses (GPL, AGPL) or unclear licensing | License scanning, legal review, open-source policy enforcement |
| Build compromise | Tampered build pipelines, compromised CI/CD, supply chain injection | Secure CI/CD hardening, code signing, reproducible builds, artifact verification |

## Requirements for Software Suppliers

**Level 1 & 2 suppliers providing software or software-as-a-service shall:**

| Requirement | Description |
|-------------|-------------|
| Software Bill of Materials (SBOM) | Maintain comprehensive SBOM for all deployed software including dependencies |
| Vulnerability management | Regular automated scanning and timely patching (critical: 14 days, high: 30 days) |
| Secure development lifecycle | Follow secure SDLC (OWASP SAMM, Microsoft SDL, or equivalent) |
| Code signing | Digitally sign all releases and updates to verify integrity and authenticity |
| Source code repository security | MFA, branch protection, audit logging, secrets scanning on repositories |
| Third-party library approval | Formal process for approving open-source and third-party components |
| Update notification | Notify [Organization] of security-relevant updates within 24 hours |
| Dependency update cadence | Regular dependency updates (quarterly minimum for non-security) |

## Software Bill of Materials (SBOM)

For Level 1 software suppliers, SBOM shall include:

| Field | Description |
|-------|-------------|
| Component name | Package/library identifier (e.g., org.apache.logging.log4j:log4j-core) |
| Version | Specific version in use (semantic versioning) |
| Source | Repository or vendor where component was obtained |
| License | SPDX license identifier (MIT, Apache-2.0, GPL-3.0) |
| Direct vs transitive | Whether [Organization] directly uses component or it's a dependency |
| Known vulnerabilities | Current CVE status with CVSS scores |
| Criticality | Impact if component were compromised (based on privileges, data access) |

**SBOM Standards**: Prefer SBOM in standard format:

- **CycloneDX**: OWASP standard for software bill of materials
- **SPDX**: Linux Foundation standard
- Both support JSON and XML formats for automated processing

**SBOM Update Frequency**: 

- Quarterly for routine updates
- Within 48 hours after new critical vulnerability discovered in component

## Open Source Security

| Consideration | Guidance |
|---------------|----------|
| Source verification | Download packages only from official repositories (npmjs.org, pypi.org, Maven Central) |
| Package integrity | Verify checksums/signatures before use, use lock files (package-lock.json, Pipfile.lock) |
| Maintenance status | Avoid abandoned projects (no commits >12 months) for critical functions |
| Community health | Active maintainers, responsive to security issues, established governance |
| Security track record | History of vulnerability disclosure and remediation speed |
| License compatibility | Verify license permits commercial use and derivative works (avoid AGPL in services) |
| Security tooling | Use Dependabot, Snyk, or equivalent for automated vulnerability detection |

**Prohibited Practices**:

- Installing packages from unofficial mirrors or modified repositories
- Using unmaintained packages for cryptography, authentication, or authorization
- Including packages with known critical vulnerabilities without remediation plan
- Copy-pasting code from Stack Overflow or GitHub without security review

---

# Hardware Supply Chain Security

## Hardware Supply Chain Risks

| Risk | Description | Examples |
|------|-------------|----------|
| Counterfeit components | Non-genuine parts substituted for authentic components | Fake Cisco switches, counterfeit memory chips, cloned batteries |
| Tampered hardware | Malicious modifications during manufacturing or transit | Implanted backdoors in servers, compromised network equipment |
| Compromised firmware | Pre-installed malicious firmware or BIOS modifications | Firmware rootkits, UEFI malware, BMC backdoors |
| Component failure | Substandard or refurbished components leading to early failure | Failed hard drives, unreliable power supplies |
| End-of-life hardware | Unsupported hardware without security patches | Legacy servers, EOL network devices with known vulnerabilities |

## Hardware Procurement Requirements

**For Level 1 & 2 hardware suppliers:**

| Requirement | Description |
|-------------|-------------|
| Authorized channels | Purchase through manufacturer-authorized distributors only |
| Chain of custody | Complete documentation of handling and transportation from factory |
| Integrity verification | Verify tamper-evident seals, packaging integrity, serial number authentication |
| Firmware verification | Validate firmware versions against manufacturer database, verify digital signatures |
| Component authenticity | Anti-counterfeit measures for critical components (processors, memory, storage) |
| Factory defaults | Hardware delivered in factory default state, not pre-configured |
| Documentation | Complete manufacturer documentation, certificates of authenticity |

**Verification Methods**:

- Serial number validation with manufacturer
- Packaging and hologram inspection
- Weight comparison (counterfeits often different weight)
- Visual inspection for modification evidence
- Firmware hash verification against known-good values

## Hardware Lifecycle Considerations

| Phase | Security Consideration |
|-------|------------------------|
| Procurement | Authorized source, integrity verification, authenticity checks |
| Receiving | Tamper inspection, documentation verification, quarantine period |
| Deployment | Secure configuration, firmware updates to current versions, asset registration |
| Operation | Patch management, firmware updates, environmental monitoring, physical security |
| Maintenance | Authorized service providers only, witness hardware service, verify post-service integrity |
| End-of-life | Secure decommissioning, data destruction (NIST SP 800-88 Rev. 2), certificate of destruction |

---

# Service Dependency Management

## Critical Service Dependencies

Identify services that suppliers depend on and assess impact:

| Dependency Type | Examples | Risk if Unavailable |
|-----------------|----------|---------------------|
| Infrastructure | Cloud platforms (AWS, Azure, GCP), data centers, colocation facilities | Complete service outage, data inaccessibility |
| Identity & Access | Authentication providers (Auth0, Okta), SSO, MFA services | Access disruption, authentication failures |
| Security Services | Certificate authorities, encryption key management (KMS), security monitoring | Security degradation, certificate expiry, compliance gaps |
| Communication | Email gateways, messaging platforms, notification services | Communication failure, incident notification delay |
| Operational Services | DNS providers, CDN networks, load balancers, DDoS protection | Performance degradation, availability impact, attack exposure |
| Payment Processing | Payment gateways, fraud detection, currency conversion | Transaction failures, revenue impact |

## Dependency Documentation

For Level 1 suppliers, document all critical service dependencies:

| Field | Description |
|-------|-------------|
| Service dependency | Specific service the supplier depends on (e.g., AWS RDS, Cloudflare CDN) |
| Provider | Fourth-party service provider name |
| Criticality | Impact if dependency fails (Critical/High/Medium/Low) |
| Alternatives | Backup or failover options (multi-cloud, redundant providers) |
| SLA | Service level commitment of the dependency provider |
| Geographic scope | Regions affected by dependency failure |
| Data residency | Where dependency processes or stores data |
| Concentration risk | Whether multiple suppliers share same dependency |

**Concentration Risk Example**:
If all your SaaS vendors use AWS us-east-1, an AWS regional outage affects all services simultaneously. Mitigation: Require multi-region or multi-cloud for Level 1 suppliers.

---

# Supply Chain Attack Mitigation

## Common Attack Vectors

| Vector | Description | Real-World Example | Mitigation |
|--------|-------------|-------------------|------------|
| Compromised updates | Malicious software updates pushed through legitimate channels | SolarWinds Orion, ASUS Live Update | Code signing verification, staged rollouts, update testing |
| Dependency confusion | Malicious packages with same name in public vs private repositories | npm dependency confusion attacks | Private registry configuration, namespace reservation |
| Credential theft | Supplier credentials stolen and used for access | Okta/LastPass breaches | MFA enforcement, credential monitoring, least privilege |
| Watering hole | Supplier developer tools or websites compromised to infect downstream | CCleaner, NotPetya via MeDoc | Network segmentation, endpoint detection, supply chain monitoring |
| Social engineering | Targeting supplier personnel with phishing or pretexting | LAPSUS$ attacks on suppliers | Supplier security awareness requirements, authentication hardening |
| Insider threat | Malicious supplier employee or contractor | Snowden-style exfiltration | Background checks, access controls, activity monitoring, segregation of duties |

## Supply Chain Security Controls

| Control | Description |
|---------|-------------|
| Supplier network segmentation | Isolate supplier access to dedicated segments, no lateral movement to production |
| Privileged access management | Require PAM for all supplier administrative access, session recording |
| Continuous monitoring | Log and alert on supplier activities, behavioral analysis, anomaly detection |
| Integrity verification | Verify checksums/signatures for updates, downloads, communications from suppliers |
| Incident response planning | Include supply chain compromise scenarios in incident response plans and tabletop exercises |
| Backup suppliers | Identify and pre-qualify alternatives for critical suppliers (multi-vendor strategy) |
| Supply chain threat intelligence | Monitor threat intelligence for supplier-related vulnerabilities and compromises |
| Software attestation | Require suppliers to attest to build integrity and security practices |

## Incident Detection Indicators

Monitor for signs of supply chain compromise:

- Unexpected supplier credential usage (time, location, volume)
- Unusual data access patterns by supplier accounts
- Software updates with unexpected code changes or missing signatures
- New sub-suppliers or service dependencies not previously disclosed
- Supplier communication from unusual channels or domains
- Abnormal network traffic to/from supplier-controlled systems

---

# Security Requirements Flow-Down

## Propagation Through Supply Chain

Primary suppliers shall propagate security requirements through the entire supply chain:

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ Organization │ ───► │   Supplier   │ ───► │ Sub-supplier │ ───► │ Fourth Party │
│              │      │  (Level 1)   │      │              │      │              │
│ Requirements │      │ MUST flow    │      │ MUST flow    │      │ MUST flow    │
│ defined in   │      │ requirements │      │ requirements │      │ requirements │
│ this policy  │      │ verbatim     │      │ equivalent   │      │ equivalent   │
└──────────────┘      └──────────────┘      └──────────────┘      └──────────────┘
```

## Minimum Flow-Down Requirements

| Requirement | Must Flow to Sub-suppliers | Verification Method |
|-------------|---------------------------|---------------------|
| Confidentiality obligations | ✓ Always, verbatim | Review sub-supplier contracts |
| Data protection (GDPR Art. 28) | ✓ If processing personal data | Review DPAs with sub-processors |
| Security controls baseline | ✓ If accessing [Organization] data or systems | Review sub-supplier certifications |
| Incident notification (24-hour) | ✓ Always | Verify incident escalation procedures |
| Audit cooperation | ✓ For critical sub-suppliers | Verify contract audit rights clause |
| Subcontractor approval | ✓ If sub-supplier uses fourth parties | Review sub-supplier's procurement process |
| Data residency | ✓ If geographic restrictions apply | Verify data processing locations |
| Secure development practices | ✓ If software development involved | Review SDLC documentation |

**Verification**: [Organization] may request evidence of flow-down including:

- Sub-supplier contract excerpts (redacted for non-security terms)
- Sub-supplier security questionnaires and certifications
- Supplier's vendor management procedures
- Audit reports covering sub-supplier management

---

# Monitoring & Review

## Supply Chain Monitoring Activities

| Activity | Frequency | Responsible | Documentation |
|----------|-----------|-------------|---------------|
| Sub-supplier register review | Quarterly | Procurement + Security | Updated register, review notes |
| Fourth-party risk assessment | Annual | Security Risk Management | Risk assessment report |
| Software dependency scan | Continuous (automated) | IT Operations + Development | Scan results, remediation tickets |
| Supply chain incident review | Upon occurrence | Security Incident Response | Incident report, lessons learned |
| Critical dependency validation | Semi-annual | IT Operations | Dependency mapping, SLA verification |
| Concentration risk assessment | Annual | CISO + Risk Management | Concentration analysis, mitigation plan |
| SBOM review (critical software) | Quarterly | Security + IT | SBOM validation, vulnerability assessment |

## Supply Chain Metrics and KPIs

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| Sub-supplier visibility (Level 1) | 100% documented | Register completeness audit |
| Critical dependencies identified | 100% documented | Dependency inventory completeness |
| SBOM coverage (critical software) | 100% available, <90 days old | SBOM collection and validation |
| Vulnerable dependencies | 0 critical, <5 high | SCA tool findings |
| Supply chain incidents | Track and trend, RCA for all | Incident management system |
| Sub-supplier certification rate (L1) | >90% ISO 27001 or SOC 2 | Certification tracking |
| Concentration risk score | Maintain below threshold | Concentration risk calculation |

## Supply Chain Reporting

**Quarterly Supply Chain Report** shall include:

- Sub-supplier changes (additions, removals, modifications)
- Fourth-party risk summary (critical dependencies, risks identified)
- Software vulnerability trends (new CVEs, remediation status)
- Supply chain incidents (summary, impact, remediation)
- Concentration risk assessment updates
- Non-compliance issues and remediation plans

**Audience**: CISO, CIO, Risk Management, Executive Management (annual summary)

---

# Regulatory Requirements

## DORA Sub-Outsourcing (Article 30)

For ICT services covered by DORA, maintain comprehensive sub-outsourcing register including:

- All sub-outsourcing arrangements by ICT third-party service providers
- Nature of sub-outsourced functions
- Jurisdictions where sub-outsourcing takes place
- Date of sub-outsourcing contracts
- Notification to [Organization] prior to sub-outsourcing

**Concentration Risk**: Assess and document concentration risk from sub-outsourcing arrangements per DORA Article 28.

## NIS2 Supply Chain Security (Article 21)

For entities covered by NIS2, supply chain security measures shall include:

- Policies on acquisition, development, and maintenance of ICT systems
- Security requirements for supplier and sub-supplier relationships
- Incident reporting from suppliers enabling 24-hour notification to authorities
- Supply chain risk assessment and mitigation strategies

---

# References

| Document | Relationship |
|----------|--------------|
| **ISMS-POL-A.5.19-23** | Parent policy framework |
| **ISMS-POL-A.5.19-23-S1** | Supplier classification and due diligence |
| **ISMS-POL-A.5.19-23-S2** | Subcontractor contract requirements and flow-down clauses |
| **ISMS-IMP-A.5.23-1-UG/TG** | Supplier inventory (includes sub-suppliers and dependencies) |
| **ISO/IEC 27036-3:2023** | Guidelines for ICT supply chain security |
| **NIST SP 800-161r1** | Cybersecurity Supply Chain Risk Management Practices |

---

**Next Document:** ISMS-POL-A.5.19-23-S4 — Supplier Monitoring & Change Management (Control A.5.22)

---

*"Your security is only as strong as your weakest supplier's weakest supplier."*
<!-- QA_VERIFIED: 2026-02-01 -->
