<!-- ISMS-CORE:POLICY:ISMS-POL-00:framework:GOV-POL:00 -->
**ISMS-POL-00 — Regulatory Applicability Framework**
**Authoritative Reference for ISMS Compliance Obligations**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Regulatory Applicability Framework |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-00 |
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
| 0.1 | [Date - 8 weeks] | CISO | Initial draft - three-tier framework structure |
| 0.2 | [Date - 6 weeks] | CISO + Legal | Added DORA, NIS2, AI Act conditional regulations |
| 0.3 | [Date - 4 weeks] | DPO | Enhanced GDPR/FADP sections, added assessment methodology |
| 0.4 | [Date - 2 weeks] | CISO/Legal/DPO | Incorporated stakeholder feedback from policy review |
| 1.0 | [Date] | CISO/Legal/DPO | Initial approved release for Stage 1 audit |

**Review Cycle**: Annual (or upon significant regulatory changes)  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Legal/Compliance Officer
- Compliance: Data Protection Officer (DPO)
- Final Authority: Executive Management (GL)

**Related Documents**:

- All ISMS policy documents (mandatory reference)
- ISO/IEC 27001:2022 Clause 4.1 (Understanding the organisation and its context)
- ISO/IEC 27001:2022 Clause 4.2 (Understanding the needs and expectations of interested parties)

**Detailed Requirements References** (maintained for conditional regulations - see Section 8.3):

- ISMS-REF-DORA - Digital Operational Resilience Act Requirements Reference
- ISMS-REF-EU-AI-ACT - EU Artificial Intelligence Act Requirements Reference
- ISMS-REF-FINMA - FINMA Circular 2023/1 Requirements Reference
- ISMS-REF-NIS2 - Network and Information Security Directive 2 Requirements Reference
- ISMS-REF-PCI-DSS - Payment Card Industry Data Security Standard Requirements Reference

**Distribution**: All ISMS stakeholders, policy authors, system owners, auditors  
**Referenced By**: All ISMS policy documents

**Language Strategy**: Where technical or regulatory terms are internationally established (e.g., GDPR, ISO/IEC, NIST), English terminology is retained to preserve precision and facilitate cross-border regulatory reference.

---

## Executive Summary

This document provides the **authoritative reference** for interpreting regulatory and framework applicability across the entire Information Security Management System (ISMS).

**Purpose**: Eliminate ambiguity and inconsistency in how regulations and frameworks are referenced across ISMS policies, procedures, and controls.

**Scope**: All references to laws, regulations, standards, and frameworks within ISMS documentation.

**Key Principle**: **Regulatory applicability must be explicit, not assumed.** References to regulations and frameworks fall into three categories:

1. **Mandatory Compliance** - Legal obligations that apply to the organisation
2. **Conditional Applicability** - Requirements that apply only under specific circumstances
3. **Informational Reference** - Best practices and technical guidance

**Usage**: All ISMS policies SHALL include Section 1.3 referencing this framework, or include a "Regulatory Framework" section directly incorporating these categories.

---

## Policy Authority and Boundaries

### Purpose and Scope of This Policy

This policy defines the **identification and applicability** of legal, statutory, regulatory, and contractual requirements for the organisation's Information Security Management System.

**This policy establishes:**

- Which regulations and standards apply to the organisation
- Categorization of regulatory obligations (Mandatory, Conditional, Informational)
- Assessment methodology for determining applicability
- Review and update processes for regulatory landscape changes

**This policy does NOT establish:**

- Risk treatment decisions (addressed in Clause 6 - Risk Management)
- Control implementation requirements (addressed in Annex A controls)
- Compliance status or verification (addressed in compliance monitoring processes)

The outcome of the regulatory applicability assessment serves as **input** for:

- Control scoping decisions within Annex A
- Risk assessment and treatment prioritization
- Proportionality decisions for control implementation
- Audit planning and compliance verification

**Boundary Principle**: This policy establishes regulatory applicability. Implementation, enforcement, and verification are handled through separate ISMS processes.

---

**Regulatory Applicability Categories**

**Category Definitions**

**Mandatory Compliance**  
Legal or contractual obligations that the organisation MUST comply with. Non-compliance results in legal liability, regulatory fines, contract breach, or certification loss.

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

- Applicability depends on organisational context
- May become mandatory based on business activities
- Requires periodic re-assessment as business evolves
- Examples: PCI DSS v4.0.1 (only if processing card payments), HIPAA (only if handling US healthcare data)

**Clarification on Tier Classification**: Tier classification (Mandatory, Conditional, Informational) determines **regulatory binding force** and does not by itself imply implementation obligations. Implementation decisions are made through the risk assessment and treatment process, considering regulatory requirements alongside other factors such as risk appetite, business context, and technical feasibility.

## Compliance Hierarchy

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
│  • PCI DSS v4.0.1 (if processing payment cards)                        │
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

# Mandatory Compliance (Tier 1)

## Swiss Federal Data Protection Act (FADP/nDSG)

**Applicability**: All operations of organisation based in or serving Switzerland

**Key Requirements**:

- Article 6: Principles (lawfulness, proportionality, purpose limitation)
- Article 7: Data security (appropriate technical and organisational measures)
- Article 8: Data processing by processors
- Article 19: Right to information (data subject rights)
- Article 328b CO (Code of Obligations): Employee monitoring and personality protection

**ISMS Impact**:

- Data protection by design and by default
- Technical security measures (encryption, access control)
- Employee monitoring transparency and proportionality
- Data processing records (Art. 12)
- Data breach notification (Art. 24)

**Reference**: Federal Act on Data Protection (SR 235.1), effective September 1, 2023

## EU General Data Protection Regulation (GDPR)

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

- Technical and organisational measures (TOMs)
- Encryption and pseudonymization
- Access controls and authentication
- Data breach response procedures
- Vendor management (processor agreements)
- Privacy impact assessments

**Reference**: Regulation (EU) 2016/679, effective May 25, 2018

## ISO/IEC 27001:2022

**Applicability**: Where organisation seeks ISO 27001 certification

**Key Requirements**:

- Annex A Controls (93 controls across organisational, people, physical, technological)
- Clause 4: Context of the organisation
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

## Additional Mandatory Regulations

Organisations should document additional mandatory regulations based on their specific context:

| Regulation | Trigger | Examples |
|-----------|---------|----------|
| **Labor Law** | Employees in jurisdiction | Works council co-determination (Germany), employee monitoring laws |
| **Financial Regulations** | Financial services | FINMA (Switzerland), BaFin (Germany), MiFID II (EU) |
| **Telecommunications** | Telecom services | Lawful interception, data retention |
| **Export Control** | Cross-border operations | Dual-use goods, cryptography export |
| **Contract Law** | Customer agreements | Explicit security requirements in service contracts |

---

# Conditional Applicability (Tier 2)

These regulations apply **only when specific business conditions are met**:

## Swiss Financial Market Supervisory Authority (FINMA)

**Regulation**: Swiss Financial Market Supervisory Authority (Eidgenössische Finanzmarktaufsicht)  
**Primary Circulars**: 

- FINMA Circular 2023/1 (Operational risks and resilience - banks, effective January 1, 2024)
- FINMA Circular 2008/7 (Outsourcing - banks)
- FINMA Circular 2018/3 (Outsourcing - insurers)

**Applicability Triggers**:

- Organisation is a **Swiss financial institution** regulated by FINMA:
  - Banks (banking license from FINMA)
  - Securities dealers (securities dealer license)
  - Insurance companies (insurance license)
  - Financial infrastructure providers (stock exchanges, central securities depositories)
  - Collective investment schemes (fund management licenses)
  
**Key Requirements**:

- **Operational Resilience**: ICT risk management, business continuity planning, disaster recovery
- **Outsourcing**: Third-party risk management, due diligence, contracts, exit strategies
- **Data Protection**: Customer data security, confidentiality, availability
- **Incident Reporting**: Significant operational incidents to FINMA
- **Internal Controls**: Governance, risk management, internal audit

**ISMS Impact**:

- Enhanced business continuity and disaster recovery controls
- Comprehensive third-party risk management (A.5.19-23)
- Incident response and reporting procedures (A.5.24-28)
- Governance and oversight structures (A.5.1, 5.4)

**Assessment**: If organisation holds FINMA license or registration → **Mandatory Compliance**

## Digital Operational Resilience Act (DORA)

**Regulation**: Regulation (EU) 2022/2554 on digital operational resilience for the financial sector  
**Effective Date**: January 17, 2025

**Applicability Triggers**:

- Organisation is a **financial entity in the EU**:
  - Credit institutions (banks)
  - Payment institutions and e-money institutions
  - Investment firms
  - Crypto-asset service providers
  - Insurance and reinsurance undertakings
  - ICT third-party service providers to financial entities (critical/important designation)

**Key Requirements**:

- **ICT Risk Management**: Comprehensive framework covering identification, protection, detection, response, recovery
- **Incident Reporting**: Major ICT-related incidents to competent authorities
- **Digital Operational Resilience Testing**: Regular testing including threat-led penetration testing (TLPT)
- **Third-Party Risk**: ICT service provider oversight, contracts, exit strategies
- **Information Sharing**: Threat intelligence and cybersecurity information exchange

**ISMS Impact**:

- Advanced ICT risk management framework (beyond ISO 27001)
- Enhanced incident detection and response (A.5.24-28)
- Mandatory resilience testing programs
- Supplier risk management with regulatory oversight (A.5.19-23)
- Information sharing arrangements

**Assessment**: If organisation is EU financial entity or critical ICT service provider → **Mandatory Compliance**

## Network and Information Security Directive 2 (NIS2)

**Directive**: Directive (EU) 2022/2555 on measures for a high common level of cybersecurity  
**Transposition Deadline**: October 17, 2024 (EU member states must implement into national law)

**Applicability Triggers**:

- Organisation is an **essential or important entity** in the EU in covered sectors:
  
**Essential Entities** (stricter requirements):

- Energy (electricity, oil, gas)
- Transport (air, rail, water, road)
- Banking and financial market infrastructures
- Health (healthcare providers, EU reference laboratories, pharmaceutical manufacturers)
- Drinking water and wastewater
- Digital infrastructure (internet exchange points, DNS service providers, cloud computing, data centers, CDNs, trust service providers)
- ICT service management (managed service providers, managed security service providers)
- Public administration (central government entities)
- Space (ground-based infrastructure for space systems)

**Important Entities** (less strict):

- Postal and courier services
- Waste management
- Chemical production and distribution
- Food production and distribution
- Manufacturing (medical devices, electronics, machinery, motor vehicles, aerospace)
- Digital providers (online marketplaces, search engines, social networks)
- Research organisations

**Key Requirements**:

- **Risk Management**: Cybersecurity risk assessment and security policies
- **Incident Handling**: Detection, response, recovery capabilities
- **Business Continuity**: Backup management, disaster recovery
- **Supply Chain Security**: Third-party risk management
- **Network Security**: Access controls, encryption, multi-factor authentication
- **Incident Notification**: 24-hour early warning, 72-hour detailed incident report to national CSIRT/competent authority
- **Supervision**: Periodic audits, security assessments, ex-post monitoring

**ISMS Impact**:

- Comprehensive cybersecurity risk management (Clause 6)
- Incident response with regulatory reporting timelines (A.5.24-28)
- Supply chain security requirements (A.5.19-23)
- Technical security controls (encryption, access control) (A.8.x series)
- Business continuity and disaster recovery (A.5.29-30)

**Penalties**: Up to €10 million or 2% of worldwide annual turnover (essential entities), €7 million or 1.4% (important entities)

**Assessment**: If organisation operates in covered sector in EU and meets size/criticality thresholds → **Mandatory Compliance**

## Payment Card Industry Data Security Standard (PCI DSS v4.0.1)

**Standard**: PCI DSS v4.0.1 (effective March 31, 2024)  
**Governing Body**: PCI Security Standards Council

**Applicability Triggers**:

- Organisation **stores, processes, or transmits** payment cardholder data:
  - Merchants accepting credit/debit cards
  - Payment processors and gateways
  - Service providers handling cardholder data
  - Any entity with access to cardholder data environment (CDE)

**Key Requirements**:

- **12 Requirements across 6 control objectives**:

  1. Install and maintain network security controls
  2. Apply secure configurations to all system components
  3. Protect stored account data
  4. Protect cardholder data with strong cryptography during transmission
  5. Protect systems and networks from malicious software
  6. Develop and maintain secure systems and software
  7. Restrict access to cardholder data by business need to know
  8. Identify users and authenticate access to system components
  9. Restrict physical access to cardholder data
  10. Log and monitor all access to system components and cardholder data
  11. Test security of systems and networks regularly
  12. Support information security with organisational policies and programs

**ISMS Impact**:

- Network segmentation and firewall controls (A.8.20-22)
- Encryption of cardholder data at rest and in transit (A.8.24)
- Strong access controls and authentication (A.5.15-18, A.8.2-5)
- Vulnerability management and patching (A.8.8)
- Logging, monitoring, and audit trails (A.8.15-16)
- Penetration testing and vulnerability scanning (A.8.8)

**Validation**: Annual on-site audit (Level 1), Self-Assessment Questionnaire (SAQ) for smaller merchants

**Assessment**: If organisation handles payment cards → **Mandatory Compliance**

## Health Insurance Portability and Accountability Act (HIPAA)

**Regulation**: US federal law protecting health information  
**Effective Date**: 1996 (with updates through HITECH Act 2009, Omnibus Rule 2013)

**Applicability Triggers**:

- Organisation is a **covered entity** or **business associate** handling US Protected Health Information (PHI):
  - Healthcare providers (doctors, hospitals, clinics)
  - Health plans (insurance companies, HMOs, Medicare/Medicaid)
  - Healthcare clearinghouses
  - Business associates (vendors, contractors handling PHI on behalf of covered entities)

**Key Requirements**:

- **HIPAA Security Rule** (45 CFR Part 164):
  - **Administrative Safeguards**: Security management process, workforce security, information access management, security awareness training, contingency planning
  - **Physical Safeguards**: Facility access controls, workstation security, device and media controls
  - **Technical Safeguards**: Access controls, audit controls, integrity controls, transmission security (encryption)
- **HIPAA Privacy Rule**: Patient rights, minimum necessary access, use and disclosure limitations
- **Breach Notification Rule**: Notification to individuals (60 days), HHS, media (if >500 affected)
- **Business Associate Agreements (BAAs)**: Required contracts with all vendors handling PHI

**ISMS Impact**:

- Risk assessment and risk management (required under Security Rule)
- Access controls and authentication (A.5.15-18, A.8.2-5)
- Encryption of PHI (A.8.24)
- Audit logging and monitoring (A.8.15-16)
- Incident response and breach notification (A.5.24-28)
- Workforce training and awareness (A.6.3)
- Business associate management (A.5.19-23)

**Penalties**: $100-$50,000 per violation (up to $1.5 million per year), criminal penalties for willful neglect

**Assessment**: If organisation handles US healthcare data (PHI) → **Mandatory Compliance**

## Federal Information Security Management Act (FISMA)

**Regulation**: US federal law requiring cybersecurity for government systems  
**Effective Date**: 2002 (updated by FISMA Reform Act 2014)

**Applicability Triggers**:

- Organisation operates **federal information systems** or provides **cloud services to US federal agencies**:
  - Federal agencies and departments
  - Federal contractors and cloud service providers (FedRAMP authorization)
  - Organisations processing federal information

**Key Requirements**:

- **Risk-based approach to cybersecurity**: Following NIST SP 800-53 controls
- **Categorization**: System categorization (Low, Moderate, High) per FIPS 199
- **Control Implementation**: NIST SP 800-53 security controls based on impact level
- **Continuous Monitoring**: Ongoing security assessment and authorization (A&A)
- **FedRAMP (for cloud)**: Federal Risk and Authorization Management Program
  - Third-party assessment by accredited assessors (3PAO)
  - Authorization by JAB (Joint Authorization Board) or agency ATO (Authority to Operate)

**ISMS Impact**:

- NIST SP 800-53 control implementation (comprehensive security controls)
- System categorization and impact analysis (A.5.9)
- Continuous monitoring and assessment (A.8.15-16)
- Supply chain risk management (A.5.19-23)
- Incident response aligned with NIST frameworks (A.5.24-28)

**Assessment**: If organisation has US federal contracts or FedRAMP authorization → **Mandatory Compliance**

## EU Artificial Intelligence Act (AI Act)

**Regulation**: Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence  
**Effective Date**: August 1, 2024 (phased implementation through August 2027)

**Applicability Triggers**:

- Organisation is a **provider** (develops or commissions AI systems placed on EU market)
- Organisation is a **deployer** (uses AI systems under own authority in the EU)
- Organisation is an **importer or distributor** of AI systems in the EU
- AI system outputs affect persons located in the EU (regardless of provider location)

**Risk Classification** (determines obligation level):

| Risk Level | Examples | Key Obligations |
|-----------|----------|-----------------|
| **Unacceptable** | Social scoring, real-time biometric identification (with exceptions), manipulation techniques | **Prohibited** |
| **High-Risk** | Employment decisions, credit scoring, access to essential services, biometric categorisation, critical infrastructure | Conformity assessment, risk management, data governance, transparency, human oversight, documentation |
| **Limited Risk** | Chatbots, emotion recognition, deepfake generation | Transparency obligations (disclosure of AI interaction) |
| **Minimal Risk** | Spam filters, AI-assisted development tools, internal analytics | No specific obligations (voluntary codes of practice) |

**Key Requirements (High-Risk Systems)**:

- Article 9: Risk management system throughout AI system lifecycle
- Article 10: Data governance (training, validation, testing datasets)
- Article 11: Technical documentation
- Article 12: Record-keeping and logging
- Article 13: Transparency and information to deployers
- Article 14: Human oversight measures
- Article 15: Accuracy, robustness, and cybersecurity

**Key Requirements (All Providers/Deployers)**:

- Article 4: AI literacy for staff operating AI systems
- Article 50: Transparency for certain AI systems (chatbots, synthetic content)

**Implementation Timeline**:

- **February 2025**: Prohibitions on unacceptable risk AI
- **August 2025**: Obligations for general-purpose AI models
- **August 2026**: Full application for high-risk AI systems
- **August 2027**: High-risk AI in regulated products (medical devices, machinery)

**ISMS Impact**:

- AI system inventory and risk classification (A.5.9)
- Risk management for AI systems (Clause 6, A.5.7)
- Data governance and quality controls (A.5.12-14)
- Logging and monitoring of AI outputs (A.8.15-16)
- Human oversight procedures (A.5.37)
- Staff training on AI literacy (A.6.3)
- Supplier management for AI components (A.5.19-23)
- Documentation and transparency (A.5.37)

**Penalties**: Up to €35 million or 7% of worldwide annual turnover (prohibited practices), €15 million or 3% (other violations)

**Assessment**: If organisation develops, deploys, or distributes AI systems affecting EU persons → Evaluate risk classification and applicable obligations

## Additional Conditional Regulations

Organisations should assess applicability based on business context:

| Regulation | Applicability Trigger | Region/Scope |
|-----------|---------------------|--------------|
| **EU AI Act** | AI system development/deployment affecting EU persons | European Union |
| **Sarbanes-Oxley (SOX)** | US publicly traded company | United States |
| **GLBA (Gramm-Leach-Bliley)** | US financial institution | United States |
| **CCPA/CPRA** | Processing California resident data | California, US |
| **China PIPL** | Processing personal information of China residents | China |
| **Australia Privacy Act** | Processing Australian personal information | Australia |
| **Singapore PDPA** | Processing Singapore personal data | Singapore |
| **LGPD** | Processing Brazilian personal data | Brazil |
| **Sector-Specific** | Industry-dependent (telecom, energy, pharma) | Varies |

---

# Informational Reference / Best Practice (Tier 3)

These frameworks provide **technical guidance and best practices** but are not legally enforceable:

## NIST Special Publications (SP 800-series)

**Description**: National Institute of Standards and Technology cybersecurity guidance  
**Applicability**: Voluntary adoption for best practices (unless required by FISMA/FedRAMP contract)

**Key Publications**:

- **NIST SP 800-53**: Security and Privacy Controls (comprehensive control catalog)
- **NIST SP 800-171**: Protecting Controlled Unclassified Information (CUI) in non-federal systems
- **NIST Cybersecurity Framework (CSF)**: Identify, Protect, Detect, Respond, Recover
- **NIST SP 800-61**: Computer Security Incident Handling Guide
- **NIST SP 800-63**: Digital Identity Guidelines (authentication, federation)

**Use in ISMS**:

- Technical implementation guidance for ISO 27001 controls
- Incident response playbook development (800-61)
- Identity and access management (800-63)
- Risk assessment methodologies (800-30, 800-37)

## CIS Controls

**Description**: Center for Internet Security Critical Security Controls  
**Version**: CIS Controls v8.1 (18 controls)  
**Applicability**: Voluntary adoption for security benchmarking

**Key Controls**:
1. Inventory and Control of Enterprise Assets
2. Inventory and Control of Software Assets
3. Data Protection
4. Secure Configuration of Enterprise Assets
5. Account Management
6. Access Control Management
7. Continuous Vulnerability Management
8. Audit Log Management
9-18. Additional controls covering backup, incident response, penetration testing, training

**Use in ISMS**:

- Asset management practices (A.5.9)
- Configuration management (A.8.9)
- Vulnerability management (A.8.8)
- Benchmarking organisational security maturity

## OWASP (Open Web Application Security Project)

**Description**: Community-driven web application security standards  
**Applicability**: Voluntary adoption for secure software development

**Key Resources**:

- **OWASP Top 10**: Most critical web application security risks
- **OWASP ASVS**: Application Security Verification Standard
- **OWASP SAMM**: Software Assurance Maturity Model
- **OWASP Cheat Sheets**: Secure coding guidance

**Use in ISMS**:

- Secure software development lifecycle (A.8.25-28)
- Web application security testing
- Developer security training (A.6.3)
- Code review and vulnerability assessment

## ISO/IEC 27002:2022

**Description**: Code of practice for information security controls  
**Applicability**: Supporting guidance for ISO 27001 implementation (not separately certifiable)

**Use in ISMS**:

- Detailed implementation guidance for Annex A controls
- Control selection and tailoring
- Proportionality and scalability considerations

## Cloud Security Alliance (CSA)

**Description**: Cloud computing security best practices  
**Applicability**: Voluntary adoption for cloud security

**Key Frameworks**:

- **CSA Cloud Controls Matrix (CCM)**: Cloud security control framework
- **CSA Security Trust Assurance and Risk (STAR)**: Cloud provider certification
- **CSA Consensus Assessments Initiative Questionnaire (CAIQ)**: Cloud security assessment

**Use in ISMS**:

- Cloud service provider evaluation (A.5.23)
- Cloud security architecture
- Vendor security assessments

## Additional Best Practice Frameworks

Organisations may reference additional frameworks based on industry context:

| Framework | Description | Use Case |
|----------|-------------|----------|
| **COBIT** | IT governance and management | IT governance alignment |
| **ITIL** | IT service management | Service delivery processes |
| **ISO 22301** | Business continuity management | BCM program structure |
| **ISO 27017/27018** | Cloud security and privacy | Cloud-specific controls |
| **ENISA Guidelines** | EU cybersecurity agency guidance | EU regulatory context |

---

# United States Federal Requirements (Special Category)

**Principle**: US federal cybersecurity requirements (FISMA, FIPS, FedRAMP, NIST CSF 2.0) apply **only where the organisation has explicit US federal contractual obligations**.

**Cloud Infrastructure Note:** If organisation uses US-based cloud service providers (AWS, Azure, GCP), this does NOT automatically trigger US federal compliance obligations. FedRAMP/FISMA apply only if:

- Organisation provides services directly to US federal agencies (prime contractor or subcontractor), OR
- Organisation's customer contract explicitly requires FedRAMP authorization or FISMA compliance

Using FedRAMP-authorized cloud providers (e.g., AWS GovCloud) is a **vendor risk management decision** (A.5.19-23), not evidence that FedRAMP applies to the organisation.

**Default Status**: **Not Applicable** unless:

- Organisation holds US federal contracts
- Organisation provides services to US federal agencies
- Contract explicitly requires NIST controls or FedRAMP authorization

**Rationale**: US federal requirements are not extraterritorial and do not apply to non-US organisations unless contractually required.

**ISMS Treatment**:

- NIST frameworks may be used as **informational reference** (Tier 3)
- FISMA/FedRAMP become **mandatory** (Tier 1) only with federal contracts
- NIST SP 800-series used for technical guidance without mandatory compliance

---

# Determining Regulatory Applicability

## Assessment Process

Organisations SHALL conduct annual regulatory applicability assessments:

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
| Processing payment cards | PCI DSS v4.0.1 (conditional - if yes, mandatory) |
| EU financial services | DORA (conditional - if yes, mandatory) |
| Developing/deploying AI systems affecting EU | EU AI Act (conditional - if yes, mandatory) |
| US federal contracts | FISMA/FedRAMP (conditional - if yes, mandatory) |

**Step 3: Document Applicability Determination**

- Create regulatory applicability matrix
- Document rationale for applicability determination
- Assign ownership (Legal, Compliance, CISO, DPO)
- Update annually or when business changes

**Note**: This assessment process identifies **which regulations apply**, not how compliance is implemented or verified. Implementation and verification are addressed through separate ISMS processes (risk assessment, control implementation, compliance monitoring).

## Regulatory Applicability Matrix Template

Organisations should maintain a regulatory applicability matrix:

| Regulation | Tier | Status | Triggers | Owner | Last Reviewed |
|-----------|------|--------|----------|-------|---------------|
| Swiss FADP | 1 - Mandatory | Applicable | Swiss operations | DPO | [Date] |
| EU GDPR | 1 - Mandatory | Applicable | EU customer data | DPO | [Date] |
| ISO 27001 | 1 - Mandatory | Applicable | Certification goal | CISO | [Date] |
| DORA | 2 - Conditional | Not Applicable | Not a financial entity | N/A | [Date] |
| PCI DSS v4.0.1 | 2 - Conditional | Applicable | Card processing | CISO | [Date] |
| EU AI Act | 2 - Conditional | [To Assess] | AI system development/deployment affecting EU | CISO | [Date] |
| NIST SP 800-53 | 3 - Informational | Reference Only | Technical guidance | CISO | [Date] |

## When to Re-Assess

**Trigger Events for Re-Assessment**:

- New business line or service offering
- Expansion to new geographic markets
- Acquisition or merger
- New customer contracts with regulatory requirements
- Regulatory changes (new laws, updated standards)
- Certification scope changes (ISO 27001 expansion)

**Frequency**: Annual minimum + triggered reassessments

**Responsibility**: CISO + Legal/Compliance + DPO (quarterly monitoring), Executive Management approval (annual comprehensive review)

---

# Usage in ISMS Policies

## Standard Reference Language

All ISMS policies SHALL include one of the following:

**Option A: Section 1.3 Reference** (Recommended for most policies):

```markdown
## Applicability of Regulatory Frameworks

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
requirements) apply only where the organisation has explicit US federal 
contractual obligations, as defined in ISMS-POL-00.

For complete regulatory categorization, refer to ISMS-POL-00.
```

**Option B: Dedicated Regulatory Framework Section** (For control-specific regulations):

```markdown
# Regulatory Framework

This control implements requirements from regulations categorized per 
ISMS-POL-00 (Regulatory Applicability Framework).

## Mandatory Compliance
[Control-specific mandatory requirements]

## Conditional Applicability
[Control-specific conditional requirements]

## Informational Reference
[Control-specific best practices]

For complete regulatory categorization, refer to ISMS-POL-00.
```

## Audit References

**For Internal Audits**:

- Verify all ISMS policies reference ISMS-POL-00
- Confirm regulatory applicability matrix is current (reviewed annually)
- Validate applicability determinations have documented rationale

**For External Audits**:

- Provide ISMS-POL-00 as foundation document
- Reference regulatory applicability matrix
- Demonstrate annual reassessment process and ownership

## Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**
Evidence required to demonstrate this policy is adequately documented and approved:

- ✅ This policy document (ISMS-POL-00 v1.0)
- ✅ Approval signatures from CISO, Legal/Compliance, DPO, Executive Management
- ✅ Regulatory applicability framework structure (Tier 1/2/3 taxonomy defined)
- ✅ Assessment methodology documented (Section 5)
- ✅ Standard reference language for ISMS policies (Section 6)

**Stage 2 (Operational Effectiveness) Evidence:**
Evidence required to demonstrate this policy is operationally effective:

- Regulatory applicability matrix populated with current organisational status (Section 8)
- Review records: Quarterly monitoring logs, annual comprehensive review meeting minutes
- Applicability determination documents: Rationale for Tier assignments (especially Tier 2 decisions)
- Triggered assessment records: Business expansion, regulatory change impact assessments
- Historical versions: Previous POL-00 versions showing framework evolution

**Clarification on Compliance Evidence:**
This policy establishes regulatory applicability (WHICH regulations apply). It does NOT establish:

- **Control implementation evidence** (addressed per Annex A control documentation)
- **Compliance KPIs/dashboards** (addressed in ISMS-POL-A.5.31-S4 §6)
- **Regulatory audit findings** (addressed in compliance monitoring processes)

The boundary is: POL-00 identifies obligations → Risk assessment prioritizes → Controls implement → Separate processes verify compliance.

---

# Maintenance & Updates

## Review Schedule

**Quarterly Review** (CISO + Legal + DPO):

- Monitor regulatory changes (GDPR guidance updates, new directives)
- Track organisational changes (new services, new markets)
- Update applicability matrix if triggers change
- Document review in quarterly ISMS review meeting

**Annual Review** (Executive Management approval):

- Comprehensive regulatory landscape assessment
- Update ISMS-POL-00 for new regulations
- Revise policy reference language if needed
- Executive sign-off on compliance obligations
- Update version control and distribution

**Triggered Review**:

- New regulation published (DORA effective, AI Act published)
- Business expansion (new country, new service)
- Merger/acquisition
- Major contract with new regulatory requirements

**Responsibility**:

- **Regulatory Monitoring**: Legal/Compliance Officer (primary), CISO (supporting)
- **Applicability Assessment**: CISO + Legal/Compliance + DPO (joint responsibility)
- **Matrix Updates**: CISO (owner), DPO (data protection regulations)
- **Policy Updates**: CISO (author), Executive Management (approval)

## Communication

**Policy Updates Communicated Via**:

- Policy portal update
- Email to all policy owners
- Legal/Compliance briefing
- CISO briefing to Executive Management
- Training material updates (if significant changes)

**Stakeholders Notified**:

- All ISMS policy authors (immediate impact)
- System owners (control scoping impact)
- Internal audit (audit planning)
- External auditors (certification scope)

## Version Control

**Major Version (X.0)**:

- New mandatory regulations added (Tier 1 changes)
- Tier changes (informational → mandatory)
- Structural changes to framework
- Removal of regulations (no longer applicable)

**Minor Version (X.Y)**:

- Clarifications to existing regulations
- Additional informational frameworks (Tier 3)
- Reference updates (NIST publication versions, GDPR guidance)
- Non-structural improvements

---

# Related Documents

**Internal References**:

- All ISMS policies (ISMS-POL-A.X.XX series)
- ISMS Risk Assessment Methodology (Clause 6)
- ISMS Statement of Applicability (Annex A scoping)
- ISMS Compliance Monitoring Processes

**External References**:

- Swiss Federal Data Protection Act (SR 235.1)
- EU GDPR (Regulation 2016/679)
- ISO/IEC 27001:2022
- NIST Special Publications (nist.gov)
- PCI DSS v4.0.1 (pcisecuritystandards.org)
- DORA (Regulation 2022/2554)
- NIS2 (Directive 2022/2555)

---

# Current Regulatory Status

**Applicability Assessment Status (as of [Date]):**

This section documents the organisation's current regulatory compliance obligations as determined through the assessment methodology defined in Section 5.

## Tier 1: Mandatory Compliance (Active)

| Regulation | Applicability Rationale | Implementation Status | Next Review |
|-----------|------------------------|----------------------|-------------|
| **Swiss FADP (nDSG)** | ✅ Applicable - Swiss-based organisation with Swiss operations and employees | Controls implemented per Annex A (A.5.12-14 Data Protection, A.5.34 Privacy Protection) | [Date + 12 months] |
| **EU GDPR** | ✅ Applicable - Processing personal data of EU residents through customer relationships | Controls implemented per Annex A (A.5.34, A.8.11 Data Masking, A.8.10 Information Deletion) | [Date + 12 months] |
| **ISO/IEC 27001:2022** | ✅ Applicable - Pursuing certification (certification goal documented in ISMS scope) | 48/93 controls implemented (52%), Stage 1 readiness achieved, Stage 2 preparation in progress | Continuous (certification maintenance) |

## Tier 2: Conditional Applicability

### Not Currently Applicable (Under Monitoring)

| Regulation | Assessment Status | Current Decision | Monitoring Trigger | Owner | Last Assessed |
|-----------|------------------|------------------|-------------------|-------|---------------|
| **DORA** | ✅ Assessed | **Not Applicable** - Organisation is not an EU financial entity nor designated critical ICT service provider to financial entities | Business model change (financial services entry), customer contracts requiring DORA compliance | CISO + Legal | [Date] |
| **NIS2** | ✅ Assessed | **Not Applicable** - Organisation does not operate as essential/important entity in covered sectors (energy, transport, banking, health, digital infrastructure) | Expansion into NIS2-covered sectors, designation as essential/important entity | CISO + Legal | [Date] |
| **PCI DSS v4.0.1** | ✅ Assessed | **Not Applicable** - Organisation does not currently store, process, or transmit payment cardholder data | Business decision to accept payment cards, merchant account establishment | CISO | [Date] |
| **FINMA** | ✅ Assessed | **Not Applicable** - Organisation does not hold FINMA license (not a Swiss bank, securities dealer, insurance company, or regulated financial infrastructure provider) | Acquisition of financial services license, provision of services to FINMA-regulated entities | Legal + CISO | [Date] |

### Under Assessment (Decision Pending)

| Regulation | Assessment Status | Expected Completion | Preliminary Findings | Owner |
|-----------|------------------|---------------------|---------------------|-------|
| **EU AI Act** | 🔄 In Progress | [Date] | Organisation uses AI tools (GitHub Copilot for development assistance, potential future AI-assisted security tools). Assessment focus: Are these systems "AI systems" under Article 3 definition? If yes, risk classification per Annex III. Preliminary: Likely **minimal risk** (Tier 3) or **limited risk** (transparency obligations only). **Recommendation:** Complete detailed assessment by [Date], document in ISMS-REF-AI-ACT if applicable. | CISO + Legal |

**Assessment Approach for EU AI Act:**
1. **Inventory AI Usage** (Due: [Date + 2 weeks])

   - GitHub Copilot (code generation assistant)
   - [List other AI tools if any]

2. **Risk Classification per AI Act Annex III** (Due: [Date + 4 weeks])

   - Assess against high-risk categories (employment, credit scoring, biometrics, critical infrastructure, law enforcement)
   - Preliminary determination: None of current AI usage falls under high-risk categories

3. **Document Decision** (Due: [Date + 6 weeks])

   - If minimal/limited risk → Tier 3 (Informational) with transparency obligations
   - If high-risk → Tier 2 (Conditional → Mandatory if confirmed)
   - Create ISMS-REF-AI-ACT if obligations identified

## Tier 3: Informational Reference (Active Use)

| Framework | Usage | Referenced In | Rationale |
|----------|-------|--------------|-----------|
| **NIST SP 800-series** | Technical implementation guidance | Multiple Annex A controls (A.8.8 Vulnerability Management references NIST SP 800-40, A.5.24-28 Incident Response references NIST SP 800-61) | Industry-standard technical guidance for control implementation |
| **CIS Controls v8.1** | Security benchmarking | Internal security posture assessment, control gap analysis | Widely recognized security baseline for comparison |
| **OWASP** | Secure development practices | A.8.25-28 Secure Development Lifecycle | Web application security best practices |
| **ISO/IEC 27002:2022** | Control implementation guidance | All Annex A controls | Official implementation guidance for ISO 27001 controls |

## Assessment Methodology Execution

**Annual Comprehensive Review:**

- **Scheduled:** Q4 annually (December)
- **Participants:** CISO (lead), Legal Counsel, DPO, Compliance Officer
- **Deliverable:** Updated Section 8 + Executive Management briefing
- **Approval:** Executive Management (GL)

**Quarterly Monitoring Review:**

- **Scheduled:** End of each quarter (March, June, September, December)
- **Participants:** CISO, Legal, DPO
- **Focus:** Regulatory changes detected, business trigger events, conditional regulation status updates
- **Deliverable:** Regulatory monitoring log, trigger event assessments

**Triggered Assessments:**

- Business expansion (new markets, services)
- Customer contract requirements (explicit regulatory obligations)
- Regulatory publications (new laws, enforcement guidance)
- **Recent Example:** EU AI Act entered into force August 1, 2024 → Triggered assessment (currently in progress per Section 8.2.2)

**Next Scheduled Activities:**

- **[Date + 2 weeks]:** Complete EU AI Act assessment (Step 1: AI usage inventory)
- **Q4 [Year]:** Annual comprehensive regulatory review
- **[Date + 12 months]:** FADP/GDPR applicability reconfirmation

## Detailed Requirements References

For conditional regulations with complex requirements (regardless of current applicability status), the organisation maintains detailed requirements reference documents for future applicability scenarios and preparedness.

| Regulation | Reference Document | Purpose | Maintenance Status |
|-----------|-------------------|---------|-------------------|
| **DORA** | ISMS-REF-DORA - Digital Operational Resilience Act Requirements Reference | Detailed ICT risk management, incident reporting, resilience testing, and third-party risk requirements per DORA Articles 3-49. Maintained for future applicability assessment if organisation enters EU financial services. | Maintained (updated when DORA regulatory technical standards published) |
| **FINMA** | ISMS-REF-FINMA - FINMA Circular 2023/1 Requirements Reference | Operational resilience and outsourcing requirements for Swiss financial institutions. Maintained for future applicability if organisation obtains FINMA license or serves FINMA-regulated clients. | Maintained (updated per FINMA circular revisions) |
| **NIS2** | ISMS-REF-NIS2 - Network and Information Security Directive 2 Requirements Reference | Cybersecurity risk management, incident notification, supply chain security, and governance requirements per NIS2 Articles 20-23. Maintained for future applicability if organisation designated as essential/important entity. | Maintained (updated as EU member states transpose NIS2 into national law) |
| **PCI DSS v4.0.1** | ISMS-REF-PCI-DSS - Payment Card Industry Data Security Standard Requirements Reference | 12 PCI DSS v4.0.1 requirements covering network security, data protection, vulnerability management, access control, monitoring, and testing. Maintained for future applicability if organisation begins processing payment cards. | Maintained (updated per PCI SSC publications, currently v4.0 effective March 2024) |
| **EU AI Act** | ISMS-REF-EU-AI-ACT - EU Artificial Intelligence Act Requirements Reference | Risk-based AI governance framework covering prohibited practices (Article 5), high-risk AI systems (Articles 9-72), limited risk transparency obligations (Article 50), and general-purpose AI model requirements (Articles 53-54). Maintained for future applicability if organisation develops or deploys AI systems affecting EU persons. | Maintained (updated as EU AI Act delegated acts and implementing acts published, phased implementation 2025-2027) |

**Rationale for Maintaining "Not Applicable" Requirements References:**

1. **Preparedness:** If business context changes (e.g., obtaining financial services license, entering NIS2-covered sectors, accepting payment cards), organisation can rapidly assess gap and implementation effort.

2. **Customer Due Diligence:** Customers may request evidence of preparedness for conditional regulations even if not currently applicable (e.g., "If we require PCI DSS v4.0.1 compliance in future, can you achieve it?").

3. **Regulatory Monitoring:** Maintaining requirements references enables proactive monitoring of regulatory changes that might affect future applicability (e.g., DORA technical standards, NIS2 national implementations, PCI DSS v4.0.1 version updates).

4. **Control Mapping Efficiency:** Requirements references facilitate mapping conditional regulations to existing ISO 27001 Annex A controls, showing overlap and potential reuse (e.g., "If DORA applies, we estimate 70% of requirements already satisfied by existing controls").

5. **Strategic Planning:** Executive Management can make informed decisions on entering regulated markets by understanding compliance effort required.

**Access and Usage:**

- **ISMS-REF-XXX documents are NOT mandatory compliance materials** (regulations are Tier 2 - Not Applicable).
- **Purpose:** Strategic preparedness, customer inquiries, business development due diligence.
- **Review Cycle:** Annual review aligned with POL-00 review (verify regulation hasn't changed making assessment outdated).
- **Ownership:** CISO (maintains technical requirements), Legal (maintains legal interpretation and applicability triggers).

**Auditor Note:** 
Maintaining requirements references for non-applicable regulations is a **maturity indicator** demonstrating proactive compliance management, not evidence of scope creep. ISO 27001 Clause 4.1 (Understanding the organisation and its context) encourages understanding both current and potential future compliance obligations.

---

# Glossary

| Term | Definition |
|------|------------|
| **Applicable** | Regulation applies to organisation based on business activities, must comply |
| **Conditional** | Regulation applies only if specific triggers met (industry, geography, data type) |
| **Mandatory** | Legal obligation, enforceable by law or contract, non-compliance has consequences |
| **Informational** | Reference for best practices, not legally enforceable, voluntary adoption |
| **Tier 1** | Mandatory compliance (legal, contractual) |
| **Tier 2** | Conditional compliance (context-dependent) |
| **Tier 3** | Informational reference (best practice, voluntary) |
| **Binding Force** | Legal or contractual enforceability of a regulation |
| **Implementation Obligation** | Requirement to implement specific controls (determined through risk assessment) |

---

# Appendix A: Regulatory Implementation Timelines

**Regulations with Phased Implementation (for Monitoring):**

| Regulation | Key Implementation Dates | Organisational Relevance |
|-----------|-------------------------|-------------------------|
| **DORA** | **January 17, 2025:** Full application for financial entities | Monitor: If organisation becomes EU financial entity or critical ICT service provider before 2025-01-17, DORA becomes Tier 1 immediately |
| **EU AI Act** | **February 2, 2025:** Prohibitions (unacceptable risk AI)<br>**August 2, 2025:** General-purpose AI obligations<br>**August 2, 2026:** High-risk AI systems<br>**August 2, 2027:** High-risk AI in regulated products<br>**August 2, 2030:** Grace period ends for existing systems | Monitor: If organisation develops or deploys AI systems affecting EU persons → Compliance required by applicable phase deadline. Existing systems (pre-August 2026) have grace period until 2030 unless substantially modified |
| **PCI DSS v4.0.1** | **March 31, 2024:** v4.0 effective (v3.2.1 retired)<br>**March 31, 2025:** New requirements (marked "future-dated" in v4.0) become mandatory | Not currently applicable. If payment card processing begins → v4.0 requirements apply immediately (v3.2.1 retired). Future-dated requirements (MFA expansion, cryptographic enhancements, anti-phishing) mandatory March 2025 |
| **NIS2** | **October 17, 2024:** EU member states must transpose into national law<br>**2024-2025:** National implementations vary by member state<br>**Varies by member state:** Application dates depend on national transposition law | Monitor: National implementations may affect applicability determination if organisation operates in multiple EU member states. Check national cybersecurity authority for specific effective dates |

---

# Closing Statement

This policy establishes regulatory applicability for the organisation's Information Security Management System.

**What this policy establishes:**

- Identification of applicable regulations (mandatory, conditional, informational)
- Assessment methodology for determining regulatory applicability
- Review and update processes for regulatory landscape changes

**What this policy does NOT establish:**

- Risk treatment decisions (addressed in Clause 6 - Risk Management)
- Control implementation requirements (addressed in Annex A controls)
- Compliance status or verification (addressed in compliance monitoring processes)

**Separation of Concerns:**

- **This Policy (POL-00)**: Defines WHICH regulations apply
- **Risk Management (Clause 6)**: Determines HOW to respond to regulatory requirements
- **Control Implementation (Annex A)**: Implements SPECIFIC controls
- **Compliance Monitoring**: Verifies and tracks COMPLIANCE status

---

**END OF ISMS-POL-00**

*"Regulatory applicability is the foundation. Implementation and compliance are the structure built upon it."*

<!-- QA_VERIFIED: 2026-02-01 -->