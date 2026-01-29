# ISMS-POL-00 — Regulatory Applicability Framework
## Authoritative Reference for ISMS Compliance Obligations

---

**Document ID**: ISMS-POL-00  
**Title**: Regulatory Applicability Framework  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Legal/Compliance / DPO | Initial framework |

**Review Cycle**: Annual (or upon significant regulatory changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Chief Information Security Officer (CISO)
- Legal/Compliance Officer
- Data Protection Officer (DPO)
- Executive Management

**Distribution**: All ISMS stakeholders, policy authors, system owners, auditors  
**Referenced By**: All ISMS policy documents (mandatory reference)

---

## Executive Summary

This document provides the **authoritative reference** for interpreting regulatory and framework applicability across the entire Information Security Management System (ISMS).

**Purpose**: Eliminate ambiguity and inconsistency in how regulations and frameworks are referenced across ISMS policies, procedures, and controls.

**Scope**: All references to laws, regulations, standards, and frameworks within ISMS documentation.

**Key Principle**: **Regulatory applicability must be explicit, not assumed.** References to regulations and frameworks fall into three categories:

1. **Mandatory Compliance** - Legal obligations that apply to the organization
2. **Informational Reference** - Best practices and technical guidance
3. **Conditional Applicability** - Requirements that apply only under specific circumstances

**Usage**: All ISMS policies SHALL include Section 1.3 referencing this framework, or include a "Regulatory Framework" section directly incorporating these categories.

---

## 1. Regulatory Applicability Categories

### 1.1 Category Definitions

**Mandatory Compliance**  
Legal or contractual obligations that the organization MUST comply with. Non-compliance results in legal liability, regulatory fines, contract breach, or certification loss.

**Characteristics**:
- Enforceable by law or contract
- Non-compliance has legal/financial consequences
- Requires documented evidence of compliance
- Subject to regulatory audits and inspections

**Informational Reference / Best Practice Alignment**  
Frameworks and standards used for technical guidance, benchmarking, or voluntary alignment. These inform security practices but do not constitute mandatory compliance requirements unless explicitly required by contract or regulation.

**Characteristics**:
- Voluntary adoption for best practices
- No legal enforcement mechanism
- Used for technical implementation guidance
- May become mandatory if referenced in contracts

**Conditional Applicability**  
Requirements that apply only when specific conditions are met (e.g., industry sector, geographic location, service type, customer contracts, regulatory scope).

**Characteristics**:
- Applicability depends on organizational context
- May become mandatory based on business activities
- Requires periodic re-assessment as business evolves
- Examples: PCI DSS (only if processing card payments), HIPAA (only if handling US healthcare data)

### 1.2 Compliance Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMPLIANCE HIERARCHY                         │
├─────────────────────────────────────────────────────────────────┤
│  TIER 1: MANDATORY (Legal/Contractual)                         │
│  • Swiss Federal Data Protection Act (FADP)                     │
│  • EU GDPR (where processing EU personal data)                  │
│  • ISO/IEC 27001:2022 (for certification)                       │
│  • Sector-specific regulations (as applicable)                  │
│  • Customer contracts (explicit security requirements)          │
│                                                                 │
│  TIER 2: CONDITIONAL (Context-Dependent)                        │
│  • DORA (if EU financial services entity)                       │
│  • NIS2 (if essential/important entity in EU)                   │
│  • PCI DSS (if processing payment cards)                        │
│  • HIPAA (if processing US healthcare data)                     │
│  • Industry regulations (sector-dependent)                      │
│                                                                 │
│  TIER 3: INFORMATIONAL (Best Practice)                          │
│  • NIST SP 800-series (technical guidance)                      │
│  • CIS Controls (security benchmarks)                           │
│  • OWASP (application security)                                 │
│  • Industry frameworks (reference only)                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Mandatory Compliance (Tier 1)

### 2.1 Swiss Federal Data Protection Act (FADP/nDSG)

**Applicability**: All operations of organization based in or serving Switzerland

**Key Requirements**:
- Article 8: Appropriate technical and organizational measures
- Article 19: Right to information (data subject rights)
- Article 26: Duties of the controller (security, privacy by design)
- Article 328b CO (Code of Obligations): Employee monitoring and personality protection

**ISMS Impact**:
- Data protection by design and by default
- Technical security measures (encryption, access control)
- Employee monitoring transparency and proportionality
- Data processing records (Art. 12)
- Data breach notification (Art. 24)

**Reference**: Federal Act on Data Protection (SR 235.1), effective September 1, 2023

### 2.2 EU General Data Protection Regulation (GDPR)

**Applicability**: When processing personal data of EU residents

**Key Requirements**:
- Article 5: Principles of processing (lawfulness, fairness, transparency, purpose limitation)
- Article 6: Lawful basis for processing
- Article 24: Controller responsibilities (accountability)
- Article 25: Data protection by design and by default
- Article 28: Processor obligations (contracts, security measures)
- Article 32: Security of processing (encryption, pseudonymization, resilience)
- Article 33: Breach notification (72 hours to supervisory authority)
- Article 35: Data Protection Impact Assessment (DPIA) for high-risk processing

**ISMS Impact**:
- Technical and organizational measures (TOMs)
- Encryption and pseudonymization
- Access controls and authentication
- Data breach response procedures
- Vendor management (processor agreements)
- Privacy impact assessments

**Reference**: Regulation (EU) 2016/679, effective May 25, 2018

### 2.3 ISO/IEC 27001:2022

**Applicability**: Where organization seeks ISO 27001 certification

**Key Requirements**:
- Annex A Controls (93 controls across organizational, people, physical, technological)
- Clause 4: Context of the organization
- Clause 5: Leadership and commitment
- Clause 6: Risk assessment and treatment
- Clause 7: Support (resources, competence, awareness, communication, documented information)
- Clause 8: Operation (risk treatment, assessment)
- Clause 9: Performance evaluation (monitoring, internal audit, management review)
- Clause 10: Improvement (nonconformity, corrective action, continual improvement)

**ISMS Impact**:
- Policy framework implementation
- Risk management methodology
- Control implementation and evidence
- Internal audit program
- Management review process
- Continual improvement

**Reference**: ISO/IEC 27001:2022 Information Security Management Systems

### 2.4 Additional Mandatory Regulations

Organizations should document additional mandatory regulations based on their specific context:

| Regulation | Trigger | Examples |
|-----------|---------|----------|
| **Labor Law** | Employees in jurisdiction | Works council co-determination (Germany), employee monitoring laws |
| **Financial Regulations** | Financial services | FINMA (Switzerland), BaFin (Germany), MiFID II (EU) |
| **Telecommunications** | Telecom services | Lawful interception, data retention |
| **Export Control** | Cross-border operations | Dual-use goods, cryptography export |
| **Contract Law** | Customer agreements | Explicit security requirements in service contracts |

---

## 3. Conditional Applicability (Tier 2)

These regulations apply **only when specific business conditions are met**:

### 3.1 Digital Operational Resilience Act (DORA)

**Regulation**: EU Regulation 2022/2554  
**Effective**: January 17, 2025

**Applicability Triggers**:
- Organization is a **financial entity** as defined by DORA:
  - Credit institutions, payment institutions, investment firms
  - Insurance/reinsurance undertakings
  - Crypto-asset service providers
  - ICT third-party service providers (TPPs) to financial entities
- Organization operates within the EU or serves EU financial entities

**Key Requirements** (if applicable):
- **ICT Risk Management Framework** (Article 6)
  - Comprehensive ICT risk management policies
  - Business continuity and disaster recovery
  - Backup policies and restoration procedures
  
- **ICT-Related Incident Management** (Articles 17-20)
  - Classification of incidents (major vs. significant)
  - Notification to authorities within strict timelines
  - Incident register maintenance
  
- **Digital Operational Resilience Testing** (Articles 24-27)
  - Regular vulnerability assessments
  - Threat-led penetration testing (TLPT) for critical entities
  - Advanced testing at least every 3 years
  
- **ICT Third-Party Risk Management** (Articles 28-30)
  - Contractual arrangements with TPPs
  - Due diligence, monitoring, exit strategies
  - Concentration risk management
  
- **Information Sharing** (Articles 45-46)
  - Participation in industry threat intelligence sharing

**ISMS Impact** (if applicable):
- Formalize ICT risk management aligned with Articles 5-16
- Implement incident classification and reporting per Articles 17-20
- Establish testing regime per Articles 24-27
- Vendor management per Articles 28-30
- Participate in threat intelligence sharing if applicable

**Determination Process**:
1. Is [Organization] a financial entity per DORA definitions?
2. Does [Organization] provide ICT services to financial entities?
3. If YES to either: DORA applies (becomes Tier 1 mandatory)
4. If NO: DORA remains informational reference

**Reference**: [Regulation (EU) 2022/2554](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554)

### 3.2 Network and Information Security Directive 2 (NIS2)

**Regulation**: EU Directive 2022/2555  
**Transposition Deadline**: October 17, 2024 (into national law)  
**Effective**: Varies by member state

**Applicability Triggers**:
- Organization operates in EU member states
- Organization is an **essential entity** or **important entity** per NIS2 definitions

**Essential Entities** (Annex I):
- Energy (electricity, oil, gas, hydrogen, district heating/cooling)
- Transport (air, rail, water, road)
- Banking, financial market infrastructures
- Health sector, drinking water, wastewater
- Digital infrastructure (internet exchange points, DNS, TLD registries, cloud, data centers, content delivery networks, trust service providers, public electronic communications)
- Public administration (central and regional levels)
- Space

**Important Entities** (Annex II):
- Postal and courier services
- Waste management
- Chemicals production, food production
- Manufacturing (medical devices, electronics, machinery, motor vehicles, etc.)
- Digital providers (online marketplaces, search engines, social networks)
- Research organizations

**Key Requirements** (if applicable):
- **Cybersecurity Risk Management** (Article 21)
  - Risk analysis and security policies
  - Incident handling, business continuity, crisis management
  - Supply chain security, secure development
  - Vulnerability disclosure, access controls
  
- **Incident Reporting** (Article 23)
  - **Early warning** within 24 hours of becoming aware
  - **Incident notification** within 72 hours with initial assessment
  - **Final report** within one month with detailed analysis
  
- **Supervision and Enforcement** (Article 32)
  - Periodic security audits
  - On-site inspections by national authorities
  - Administrative fines up to €10M or 2% of global turnover (essential), €7M or 1.4% (important)

**ISMS Impact** (if applicable):
- Align risk management with Article 21 measures
- Implement incident reporting timelines per Article 23
- Prepare for regulatory supervision per Article 32
- Document supply chain security per Article 21(2)(e)

**Determination Process**:
1. Does [Organization] operate in EU member states?
2. Is [Organization] in a sector listed in Annex I (essential) or Annex II (important)?
3. Does [Organization] meet size/significance thresholds per national law?
4. If YES: NIS2 applies (becomes Tier 1 mandatory)
5. If NO: NIS2 remains informational reference

**Reference**: [Directive (EU) 2022/2555](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555)

### 3.3 Payment Card Industry Data Security Standard (PCI DSS)

**Applicability Triggers**:
- Organization processes, stores, or transmits payment card data (cardholder data or sensitive authentication data)
- Organization is a merchant accepting card payments
- Organization is a service provider to merchants/financial institutions

**Key Requirements** (PCI DSS v4.0):
- **Build and Maintain Secure Network** (Req. 1-2)
  - Firewalls, secure configurations
  
- **Protect Cardholder Data** (Req. 3-4)
  - Encryption, tokenization, key management
  - Encryption in transit (TLS 1.2+)
  
- **Maintain Vulnerability Management** (Req. 5-6)
  - Anti-malware, secure development
  - Patch management, vulnerability scans
  
- **Implement Strong Access Controls** (Req. 7-8)
  - Need-to-know access, MFA
  - User management, authentication
  
- **Monitor and Test Networks** (Req. 9-11)
  - Physical security, logging, testing
  
- **Maintain Information Security Policy** (Req. 12)
  - Security policy, awareness training

**Compliance Validation**:
- **Merchants**: Annual Self-Assessment Questionnaire (SAQ) or Attestation of Compliance (AOC)
- **Service Providers**: Qualified Security Assessor (QSA) audit or self-assessment

**ISMS Impact** (if applicable):
- Cardholder data environment (CDE) scoping and segmentation
- Annual PCI DSS assessments (SAQ or AOC)
- Quarterly vulnerability scans by Approved Scanning Vendor (ASV)
- Remediation tracking for PCI gaps

**Determination Process**:
1. Does [Organization] process payment cards (credit/debit)?
2. If YES: PCI DSS applies (becomes Tier 1 mandatory)
3. If NO: PCI DSS is informational reference

**Reference**: [PCI Security Standards Council](https://www.pcisecuritystandards.org/)

### 3.4 Health Insurance Portability and Accountability Act (HIPAA)

**Regulation**: US Public Law 104-191 (1996), HITECH Act (2009)

**Applicability Triggers**:
- Organization is a **covered entity**:
  - Health care providers (if transmit health info electronically)
  - Health plans (insurance, HMOs)
  - Health care clearinghouses
- Organization is a **business associate** to a covered entity (provides services involving PHI access)

**Key Requirements**:
- **Privacy Rule** (45 CFR Part 160, 164 Subparts A, E)
  - Protected health information (PHI) use and disclosure limits
  - Patient rights (access, amendment, accounting)
  
- **Security Rule** (45 CFR Part 164 Subpart C)
  - Administrative safeguards (risk analysis, workforce security, training)
  - Physical safeguards (facility access, workstation security, device controls)
  - Technical safeguards (access controls, audit controls, encryption)
  
- **Breach Notification Rule** (45 CFR Part 164 Subpart D)
  - Notify affected individuals within 60 days
  - Notify HHS (immediately if >500 individuals)
  - Media notification for large breaches

**ISMS Impact** (if applicable):
- PHI risk assessment per Security Rule
- Business associate agreements (BAAs) with vendors
- Breach response procedures
- Technical safeguards (encryption, access logs)

**Determination Process**:
1. Does [Organization] handle US protected health information (PHI)?
2. Is [Organization] a covered entity or business associate?
3. If YES: HIPAA applies (becomes Tier 1 mandatory)
4. If NO: HIPAA is informational reference

**Reference**: [HHS HIPAA Portal](https://www.hhs.gov/hipaa/index.html)

### 3.5 Federal Information Security Management Act (FISMA)

**Regulation**: US Federal Law (44 U.S.C. § 3551 et seq.)

**Applicability Triggers**:
- Organization is a US federal agency
- Organization is a contractor/service provider to federal agencies processing federal information

**Key Requirements**:
- **NIST SP 800-53 Compliance** (Security and Privacy Controls)
  - Control baselines: Low, Moderate, High (based on FIPS 199 impact levels)
  - Continuous monitoring (ConMon)
  
- **FedRAMP Authorization** (for cloud service providers)
  - Third-party assessment organization (3PAO) audit
  - Low, Moderate, High authorization packages
  - Continuous monitoring requirements
  
- **Annual FISMA Reporting**
  - Federal agencies report to OMB
  - Contractors report to sponsoring agencies

**ISMS Impact** (if applicable):
- Implement NIST SP 800-53 controls
- FedRAMP authorization process (if cloud provider)
- Continuous monitoring program
- Annual compliance reporting

**Determination Process**:
1. Does [Organization] have US federal contracts?
2. Does [Organization] process federal information systems?
3. If YES: FISMA applies (becomes Tier 1 mandatory)
4. If NO: FISMA/NIST are informational references

**Reference**: [FISMA at CISA](https://www.cisa.gov/fisma)

---

## 4. Informational Reference (Tier 3)

These frameworks provide **best practice guidance** but are **not legally enforceable** unless explicitly required by contract or regulation:

### 4.1 NIST Special Publications (SP 800-series)

**Purpose**: Technical guidance for information security practices

**Key Publications**:
- **NIST SP 800-53** (Security and Privacy Controls)
  - Comprehensive catalog of security controls
  - Control baselines (Low, Moderate, High)
  - Referenced by FISMA, FedRAMP
  
- **NIST SP 800-171** (Protecting Controlled Unclassified Information)
  - 110 controls derived from SP 800-53
  - Required for defense contractors (DFARS 252.204-7012)
  
- **NIST Cybersecurity Framework (CSF)**
  - Identify, Protect, Detect, Respond, Recover
  - Voluntary for private sector (mandatory for some federal agencies)
  
- **NIST SP 800-61** (Incident Handling)
- **NIST SP 800-86** (Digital Forensics)
- **NIST SP 800-92** (Log Management)

**ISMS Usage**:
- Technical implementation guidance
- Mapping to ISO 27001 controls
- Benchmarking security practices
- **Status**: Informational unless contract requires NIST compliance

**Reference**: [NIST Computer Security Resource Center](https://csrc.nist.gov/)

### 4.2 Center for Internet Security (CIS) Controls

**Purpose**: Prioritized set of security best practices

**Structure**:
- **18 CIS Controls** (v8.0)
  - Implementation Groups (IG1, IG2, IG3) based on organization size/sophistication
  
**Key Controls**:
- Inventory and Control of Enterprise Assets (CIS 1)
- Data Protection (CIS 3)
- Secure Configuration (CIS 4)
- Account Management (CIS 5)
- Access Control (CIS 6)
- Continuous Vulnerability Management (CIS 7)
- Audit Log Management (CIS 8)
- Malware Defenses (CIS 10)

**ISMS Usage**:
- Prioritize control implementation
- Benchmarking against peer organizations
- Gap analysis vs. industry baselines
- **Status**: Informational unless contract requires CIS Controls

**Reference**: [CIS Controls](https://www.cisecurity.org/controls)

### 4.3 Open Web Application Security Project (OWASP)

**Purpose**: Application security guidance and tooling

**Key Resources**:
- **OWASP Top 10** (Web Application Security Risks)
  - A01 Broken Access Control
  - A02 Cryptographic Failures
  - A03 Injection
  - [etc.]
  
- **OWASP Application Security Verification Standard (ASVS)**
  - Security requirements for web apps (Levels 1-3)
  
- **OWASP SAMM** (Software Assurance Maturity Model)
  - Secure development lifecycle framework

**ISMS Usage**:
- Secure development standards
- Vulnerability assessment baselines
- Code review checklists
- **Status**: Informational unless contract requires OWASP compliance

**Reference**: [OWASP.org](https://owasp.org/)

### 4.4 Cloud Security Alliance (CSA)

**Purpose**: Cloud security best practices

**Key Frameworks**:
- **CSA Cloud Controls Matrix (CCM)**
  - 197 controls across 17 domains
  - Mapping to ISO 27001, NIST, PCI DSS
  
- **CSA Security Trust Assurance and Risk (STAR)**
  - Self-assessment, third-party certification, continuous monitoring

**ISMS Usage**:
- Cloud service provider assessments
- Cloud security architecture
- **Status**: Informational unless contract requires CSA compliance

**Reference**: [Cloud Security Alliance](https://cloudsecurityalliance.org/)

### 4.5 MITRE ATT&CK Framework

**Purpose**: Adversary tactics, techniques, and procedures (TTPs)

**Usage**:
- Threat modeling
- Detection engineering
- Red team/blue team exercises
- Security control validation

**ISMS Usage**:
- Threat intelligence integration
- Incident response playbooks
- **Status**: Informational (tactical threat intelligence)

**Reference**: [MITRE ATT&CK](https://attack.mitre.org/)

---

## 5. United States Federal Requirements

**Special Applicability Note**: References to US federal frameworks (FISMA, FIPS, FedRAMP, NIST cybersecurity requirements) apply **ONLY** where:

1. [Organization] has **explicit contractual obligations** with US federal agencies, OR
2. [Organization] processes **federal information systems** as defined by FISMA

**Without US federal contracts**, these frameworks are **Tier 3 Informational** and used for technical guidance only.

**With US federal contracts**, these become **Tier 1 Mandatory** and require:
- Compliance with specified NIST SP 800-53 control baselines
- FedRAMP authorization (if cloud service provider)
- FIPS 140-2/140-3 validated cryptography
- Annual FISMA reporting
- Continuous monitoring (ConMon)

Organizations SHALL document US federal applicability in the regulatory applicability matrix.

---

## 6. Determining Regulatory Applicability

### 6.1 Assessment Process

Organizations SHALL conduct annual regulatory applicability assessments:

**Step 1: Identify Business Activities**
- Geographic locations of operations
- Industries and sectors served
- Types of data processed (PII, healthcare, financial, etc.)
- Customer base (B2B, B2C, government)
- Services provided (cloud, consulting, software, etc.)

**Step 2: Map Regulations to Activities**

| Business Activity | Triggered Regulations |
|-------------------|----------------------|
| Processing EU resident data | GDPR (mandatory) |
| Operating in Switzerland | Swiss FADP (mandatory) |
| ISO 27001 certification goal | ISO 27001 (mandatory) |
| Processing payment cards | PCI DSS (conditional - if yes, mandatory) |
| EU financial services | DORA (conditional - if yes, mandatory) |
| US federal contracts | FISMA/FedRAMP (conditional - if yes, mandatory) |

**Step 3: Document Applicability**
- Create regulatory applicability matrix
- Assign ownership (Legal, Compliance, CISO, DPO)
- Update annually or when business changes

**Step 4: Implement Controls**
- Map regulations to ISMS controls
- Document compliance evidence
- Track via compliance dashboard

### 6.2 Regulatory Applicability Matrix Template

Organizations should maintain a regulatory applicability matrix:

| Regulation | Tier | Status | Triggers | Owner | Evidence |
|-----------|------|--------|----------|-------|----------|
| Swiss FADP | 1 - Mandatory | Applicable | Swiss operations | DPO | DPIA, processing records |
| EU GDPR | 1 - Mandatory | Applicable | EU customer data | DPO | TOMs, processor agreements |
| ISO 27001 | 1 - Mandatory | Applicable | Certification goal | CISO | Statement of Applicability |
| DORA | 2 - Conditional | Not Applicable | Not a financial entity | N/A | N/A |
| PCI DSS | 2 - Conditional | Applicable | Card processing | CISO | AOC, SAQ |
| NIST SP 800-53 | 3 - Informational | Reference Only | Technical guidance | CISO | Control mapping |

### 6.3 When to Re-Assess

**Trigger Events for Re-Assessment**:
- New business line or service offering
- Expansion to new geographic markets
- Acquisition or merger
- New customer contracts with regulatory requirements
- Regulatory changes (new laws, updated standards)
- Certification scope changes (ISO 27001 expansion)

**Frequency**: Annual minimum + triggered reassessments

---

## 7. Usage in ISMS Policies

### 7.1 Standard Reference Language

All ISMS policies SHALL include one of the following:

**Option A: Section 1.3 Reference** (Recommended for most policies):

```markdown
### 1.3 Applicability of Regulatory Frameworks

References to standards, frameworks, and regulations throughout this ISMS 
are categorized per ISMS-POL-00 (Regulatory Applicability Framework):

**Mandatory Compliance:**
- Swiss Federal Data Protection Act (FADP)
- EU GDPR (where processing EU personal data)
- ISO/IEC 27001:2022
- [Additional mandatory regulations per ISMS-POL-00]

**Informational Reference / Best Practice Alignment:**
- NIST Special Publications (SP 800-series)
- [Other frameworks per ISMS-POL-00]

**United States Federal Requirements:**
References to US federal frameworks (FISMA, FIPS, FedRAMP, NIST cybersecurity 
requirements) apply only where the organization has explicit US federal 
contractual obligations, as defined in ISMS-POL-00.

For complete regulatory categorization, refer to ISMS-POL-00.
```

**Option B: Dedicated Regulatory Framework Section** (For control-specific regulations):

```markdown
## 2. Regulatory Framework

This control implements requirements from regulations categorized per 
ISMS-POL-00 (Regulatory Applicability Framework).

### 2.1 Mandatory Compliance
[Control-specific mandatory requirements]

### 2.2 Conditional Applicability
[Control-specific conditional requirements]

### 2.3 Informational Reference
[Control-specific best practices]

For complete regulatory categorization, refer to ISMS-POL-00.
```

### 7.2 Audit References

**For Internal Audits**:
- Verify all ISMS policies reference ISMS-POL-00
- Confirm regulatory applicability matrix is current
- Validate triggered regulations have documented evidence

**For External Audits**:
- Provide ISMS-POL-00 as foundation document
- Reference regulatory applicability matrix
- Demonstrate annual reassessment process

---

## 8. Maintenance & Updates

### 8.1 Review Schedule

**Quarterly Review** (CISO + Legal + DPO):
- Monitor regulatory changes (GDPR guidance updates, new directives)
- Track organizational changes (new services, new markets)
- Update applicability matrix if triggers change

**Annual Review** (Executive Management approval):
- Comprehensive regulatory landscape assessment
- Update ISMS-POL-00 for new regulations
- Revise policy reference language if needed
- Executive sign-off on compliance obligations

**Triggered Review**:
- New regulation published (DORA effective, AI Act published)
- Business expansion (new country, new service)
- Merger/acquisition
- Major contract with new regulatory requirements

### 8.2 Communication

**Policy Updates Communicated Via**:
- Policy portal update
- Email to all policy owners
- Legal/Compliance briefing
- CISO briefing to Executive Management
- Training material updates

### 8.3 Version Control

**Major Version (X.0)**:
- New mandatory regulations added
- Tier changes (informational → mandatory)
- Structural changes to framework

**Minor Version (X.Y)**:
- Clarifications to existing regulations
- Additional informational frameworks
- Reference updates (NIST publication versions)

---

## 9. Related Documents

**Internal References**:
- All ISMS policies (ISMS-POL-A.X.XX series)
- ISMS Regulatory Compliance Register
- ISMS Risk Assessment Methodology
- ISMS Compliance Dashboard

**External References**:
- Swiss Federal Data Protection Act (SR 235.1)
- EU GDPR (Regulation 2016/679)
- ISO/IEC 27001:2022
- NIST Special Publications (nist.gov)
- PCI DSS (pcisecuritystandards.org)
- DORA (Regulation 2022/2554)
- NIS2 (Directive 2022/2555)

---

## 10. Glossary

| Term | Definition |
|------|------------|
| **Applicable** | Regulation applies to organization based on business activities, must comply |
| **Conditional** | Regulation applies only if specific triggers met (industry, geography, data type) |
| **Mandatory** | Legal obligation, enforceable by law or contract, non-compliance has consequences |
| **Informational** | Reference for best practices, not legally enforceable, voluntary adoption |
| **Tier 1** | Mandatory compliance (legal, contractual) |
| **Tier 2** | Conditional compliance (context-dependent) |
| **Tier 3** | Informational reference (best practice, voluntary) |

---

**END OF ISMS-POL-00**

*"Compliance is not a checkbox. It's a continuous commitment to understanding 
and meeting the obligations that apply to your organization."*