<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23:framework:GOV-POL:a.5.19-23 -->
**ISMS-POL-A.5.19-23 — Supplier & Cloud Services Security**
**Comprehensive Policy & Implementation Framework**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Supplier & Cloud Services Security |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.19-23 |
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
| 1.0 | [Date] | CISO/ISO | Initial policy framework for ISO 27001:2022 first certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- Compliance: Legal/Compliance Officer
- Procurement: Procurement Director
- Final Authority: Executive Management (GL)

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.19-23-S1 (Supplier Relationship Fundamentals)
- ISMS-POL-A.5.19-23-S2 (Supplier Agreement Requirements)
- ISMS-POL-A.5.19-23-S3 (ICT Supply Chain Security)
- ISMS-POL-A.5.19-23-S4 (Supplier Monitoring & Change Management)
- ISMS-POL-A.5.19-23-S5 (Cloud Services Security)
- ISMS-POL-A.5.19-23-S6 (Assessment Methodology & Automation)
- ISMS-IMP-A.5.23.S1-UG/TG (Cloud Service Inventory & Classification)
- ISMS-IMP-A.5.23.S2-UG/TG (Vendor Due Diligence & Contracts)
- ISMS-IMP-A.5.23.S3-UG/TG (Secure Configuration & Deployment)
- ISMS-IMP-A.5.23.S4-UG/TG (Ongoing Governance & Risk Management)
- ISMS-REF-A.5.23 (Cloud Service Provider Registry)
- ISO/IEC 27001:2022 Controls A.5.19-23
- ISO/IEC 27036 (Supplier Relationships)
- ISO/IEC 27017 (Cloud Security)
- ISO/IEC 27018 (Cloud Privacy)

**Distribution**: All employees, contractors, procurement staff, legal team, IT operations, cloud administrators

---

## Executive Summary

This document serves as the **master index** for [Organization]'s Supplier and Cloud Services Security framework, implementing ISO/IEC 27001:2022 Controls A.5.19 through A.5.23.

**Purpose**: Establish mandatory requirements for managing information security risks associated with external suppliers, contractual agreements, ICT supply chain dependencies, ongoing supplier relationship management, and cloud service lifecycle.

**Scope**: All supplier relationships involving access to organizational information or systems, all cloud services (IaaS, PaaS, SaaS, security services), all contractual agreements with external service providers, and all ICT products with supply chain dependencies.

**Critical Principle - "Supplier Trust Must Be Verified, Not Assumed"**: This framework requires evidence-based validation of supplier security posture through systematic due diligence, contractual commitments with enforceable terms, and continuous monitoring throughout the relationship lifecycle. Supplier claims without third-party attestation (SOC 2, ISO 27001, regulatory compliance certificates), contracts without enforceable security clauses and audit rights, and relationships without periodic review create unacceptable risks. Trust-but-verify through documented evidence is non-negotiable.

**Framework Components**:

- **Policy Layer:** Governance documents defining requirements (7 policy documents)
- **Assessment Layer:** Technical evaluation specifications (markdown documentation)
- **Implementation Layer:** Python-generated Excel workbooks (4 assessment workbooks)
- **Validation Layer:** Quality assurance and normalization scripts
- **Integration Layer:** Individual workbook Summary Dashboards

**Approach**: This framework employs a **documented, systematic process** where assessment tools are programmatically generated from controlled specifications rather than manually created. This ensures consistency, repeatability, and version control - if assessment requirements change, regenerating updated workbooks follows documented procedures rather than error-prone manual editing. The principle is straightforward: what can be created from documented specifications can be understood completely, maintained reliably, and audited objectively.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR Article 28 (processor agreements and security requirements), ISO/IEC 27001:2022, and conditional requirements for DORA (ICT third-party risk register, concentration risk assessment, exit strategies per Art. 28-31), NIS2 (supply chain security measures, 24-hour incident notification per Art. 21-23), EU AI Act (high-risk AI system provider requirements), and US CLOUD Act jurisdictional considerations where [Organization]'s business activities trigger applicability.

---

## Control Alignment

**ISO/IEC 27001:2022 Annex A.5.19-23 — Supplier and Cloud Services Security**

This policy framework provides organizational governance for five related controls covering the complete supplier and cloud service lifecycle:

### A.5.19 - Information Security in Supplier Relationships

> *Processes and procedures should be defined and agreed upon with suppliers to manage information security risks associated with the use of supplier's products or services.*

**Control Objective**: Ensure information security risks associated with supplier relationships are identified, assessed, and managed throughout the relationship lifecycle.

**ISO/IEC 27002:2022 Guidance Summary**:

- Supplier relationships shall be managed through defined processes covering entire lifecycle (selection, onboarding, operation, exit)
- Suppliers shall be identified and classified based on type of access, data sensitivity, and service criticality
- Due diligence shall be conducted before granting supplier access to organizational information or systems
- Supplier security requirements shall be defined based on risk classification and data classification
- Supplier performance and security posture shall be monitored throughout relationship duration
- Supplier exit procedures shall be established to ensure safe termination and data return
- Shadow IT and unauthorised supplier usage shall be actively identified and managed (see Shadow IT Detection below)
- Supplier dependency and concentration risk shall be assessed for critical services

**Policy Reference**: See ISMS-POL-A.5.19-23-S1 (Supplier Relationship Fundamentals) for detailed requirements.

### A.5.20 - Addressing Information Security in Supplier Agreements

> *Relevant information security requirements should be established and agreed upon with each supplier that may access, process, store, communicate or provide IT infrastructure components for the organization's information.*

**Control Objective**: Ensure information security requirements are contractually binding and enforceable throughout the supplier relationship.

**ISO/IEC 27002:2022 Guidance Summary**:

- Information security requirements shall be included in all supplier contracts and agreements
- Requirements shall address confidentiality, integrity, and availability of organizational information
- Contracts shall define access controls, authentication requirements, and authorization procedures
- Data protection and privacy obligations shall be specified per applicable regulations (GDPR Art. 28, nDSG)
- Incident notification and response requirements shall be documented with specific timelines
- Audit rights and compliance verification mechanisms shall be established
- Service level agreements shall include security metrics and performance indicators
- Termination procedures and data return/destruction obligations shall be contractually defined
- Right to audit (on-site or remote) and regulatory cooperation shall be enforceable

**Policy Reference**: See ISMS-POL-A.5.19-23-S2 (Supplier Agreement Requirements) for detailed contractual requirements.

### A.5.21 - Managing Information Security in the ICT Supply Chain

> *Processes and procedures should be defined and agreed upon with suppliers to manage information security risks associated with the information and communication technology (ICT) services and product supply chain.*

**Control Objective**: Manage information security risks within the ICT supply chain including sub-suppliers, components, and software dependencies.

**ISO/IEC 27002:2022 Guidance Summary**:

- ICT supply chain risks shall be identified and assessed systematically
- Security requirements for ICT products and services shall be specified in procurement
- Supplier sub-suppliers (supply chain transparency) shall be evaluated and disclosed
- Software supply chain security shall be addressed including dependencies, libraries, and open-source components
- Hardware supply chain security shall be considered including counterfeit detection and tampering protection
- Supply chain continuity and resilience shall be planned for critical ICT services
- Supplier changes and updates shall be managed through change control processes
- Supply chain risk assessment shall include geopolitical, concentration, and single-source dependencies

**Policy Reference**: See ISMS-POL-A.5.19-23-S3 (ICT Supply Chain Security) for detailed supply chain requirements.

### A.5.22 - Monitoring, Review and Change Management of Supplier Services

> *The organization should regularly monitor, review, evaluate and manage changes in supplier information security practices and service delivery.*

**Control Objective**: Ensure ongoing validation of supplier security posture and controlled management of changes to supplier services.

**ISO/IEC 27002:2022 Guidance Summary**:

- Supplier performance shall be monitored continuously against contractual commitments
- Periodic reviews of supplier security practices shall be conducted based on risk classification
- Changes to supplier services shall be managed through formal change control procedures
- Supplier compliance with agreements shall be verified through audits, attestations, or certifications
- Supplier incidents and security events shall be tracked, analyzed, and responded to appropriately
- Supplier audits or third-party attestations (SOC 2, ISO 27001) shall be obtained and reviewed
- Relationship with suppliers shall be maintained through regular communication and meetings
- Supplier service degradation or non-compliance shall trigger escalation and remediation procedures

**Policy Reference**: See ISMS-POL-A.5.19-23-S4 (Supplier Monitoring & Change Management) for detailed governance requirements.

### A.5.23 - Information Security for Use of Cloud Services

> *Processes for acquisition, use, management and exit from cloud services should be established in accordance with the organization's information security requirements.*

**Control Objective**: Manage cloud service lifecycle systematically from selection through secure exit.

**ISO/IEC 27002:2022 Guidance Summary**:

- Cloud service acquisition shall follow risk-based selection process with security evaluation
- Cloud service agreements shall address information security requirements and shared responsibility model
- Shared responsibility model shall be explicitly understood and documented (provider vs customer controls)
- Cloud service configuration shall be secured according to vendor baselines and organizational requirements
- Cloud data residency and sovereignty requirements shall be enforced per regulatory obligations
- Cloud service monitoring and logging shall be implemented with appropriate retention
- Cloud service exit strategy shall be planned and tested including data export and portability
- Cloud-specific risks (multi-tenancy, data commingling, jurisdiction) shall be assessed and mitigated
- Cloud provider certifications and compliance shall be verified (SOC 2, ISO 27017, CSA STAR)

**Policy Reference**: See ISMS-POL-A.5.19-23-S5 (Cloud Services Security) for detailed cloud-specific requirements.

---

# Framework Structure

## Purpose

Establish mandatory requirements for managing information security risks associated with:

- External suppliers providing products or services
- Contractual agreements with suppliers
- ICT supply chain dependencies
- Ongoing supplier relationship management
- Cloud service acquisition, operation, and exit

## Scope

This framework applies to:

- All supplier relationships involving access to organizational information or systems
- All cloud services (IaaS, PaaS, SaaS, XaaS models including security services, collaboration platforms, storage)
- All contractual agreements with external service providers
- All ICT products and services with supply chain dependencies
- All employees, contractors, and third parties managing supplier relationships

## Exclusions

This framework does not cover:

- One-time purchases without ongoing service relationship or data access
- Suppliers with no access to organizational information assets
- Internal service providers (covered under separate HR/operational policies)

---

# Policy Documents

## Policy Structure

The supplier and cloud services security policy framework consists of the following modular documents:

| Document ID | Title | Primary Control(s) | Purpose |
|-------------|-------|--------------------|---------| 
| **ISMS-POL-A.5.19-23** | Master Index | All (5.19-23) | Framework overview and navigation |
| **ISMS-POL-A.5.19-23-S1** | Supplier Relationship Fundamentals | A.5.19 | Risk classification and due diligence |
| **ISMS-POL-A.5.19-23-S2** | Supplier Agreement Requirements | A.5.20 | Contract clauses and SLA requirements |
| **ISMS-POL-A.5.19-23-S3** | ICT Supply Chain Security | A.5.21 | Sub-supplier and component security |
| **ISMS-POL-A.5.19-23-S4** | Supplier Monitoring & Change Management | A.5.22 | Review cycles and change procedures |
| **ISMS-POL-A.5.19-23-S5** | Cloud Services Security | A.5.23 | Cloud lifecycle management |
| **ISMS-POL-A.5.19-23-S6** | Assessment Methodology & Automation | All (5.19-23) | Programmatic documentation generation |

**Design Philosophy**: Each document is independently versionable to enable granular change management, targeted stakeholder reviews, and clear audit trails.

## Document Hierarchy

```
ISMS-POL-A.5.19-23 (Master Index) ← You are here
│
├── S1: Supplier Relationship Fundamentals (A.5.19)
│   └── Defines: Risk categories, classification, due diligence
│
├── S2: Supplier Agreement Requirements (A.5.20)
│   └── Defines: Contract clauses, SLA requirements, security terms
│
├── S3: ICT Supply Chain Security (A.5.21)
│   └── Defines: Sub-supplier requirements, component security
│
├── S4: Supplier Monitoring & Change Management (A.5.22)
│   └── Defines: Review cycles, audit rights, change procedures
│
├── S5: Cloud Services Security (A.5.23)
│   └── Defines: Cloud lifecycle (selection → implementation → exit)
│
└── S6: Assessment Methodology & Automation (All Controls)
    └── Defines: Excel workbooks, Python scripts, validation

Implementation Layer (Separate Documents):
├── ISMS-IMP-A.5.23.0 (Regulatory Update Specification - DORA/NIS2/AI Act/CLOUD Act)
├── ISMS-IMP-A.5.23.1 (Cloud Service Inventory & Classification)
├── ISMS-IMP-A.5.23.2 (Vendor Due Diligence & Contracts)
├── ISMS-IMP-A.5.23.3 (Secure Configuration & Deployment)
└── ISMS-IMP-A.5.23.4 (Ongoing Governance & Risk Management)

Reference Data:
└── ISMS-REF-A.5.23 (Cloud Service Provider Registry)
```

---

# Assessment & Implementation Documents

## Assessment Specifications (Markdown)

The framework includes comprehensive assessment specifications defining structure and requirements for Excel workbook generation:

| Document ID | Title | Purpose | Sheets |
|-------------|-------|---------|--------|
| **ISMS-IMP-A.5.23.0** | Regulatory Update Specification | DORA, NIS2, AI Act, CLOUD Act enhancements | N/A (spec) |
| **ISMS-IMP-A.5.23.1** | Cloud Service Inventory & Classification | Authoritative inventory with data classification and criticality | ~10 |
| **ISMS-IMP-A.5.23.2** | Vendor Due Diligence & Contracts | Due diligence criteria, contract security clauses | ~8 |
| **ISMS-IMP-A.5.23.3** | Secure Configuration & Deployment | Cloud service configuration baselines and deployment | ~8 |
| **ISMS-IMP-A.5.23.4** | Ongoing Governance & Risk Management | Monitoring, review cycles, incident management | ~8 |

**Note**: ISMS-IMP-A.5.23.0 is a specification document for updating workbooks 1-4 with regulatory enhancements, not a standalone workbook.

## Generated Excel Workbooks

When Python generators are executed, they produce:

| Workbook | Sheets | Primary Users | Purpose |
|----------|--------|---------------|---------|
| **ISMS_REG_A523_1_Inventory_YYYYMMDD.xlsx** | ~10 | Procurement, Security, IT Ops | Service inventory, data classification, exit feasibility |
| **ISMS_REG_A523_2_DueDiligence_YYYYMMDD.xlsx** | ~8 | Procurement, Legal, Security | Vendor evaluation, contract review, security clauses |
| **ISMS_REG_A523_3_Configuration_YYYYMMDD.xlsx** | ~8 | Cloud Architects, Security | Security configuration baselines, deployment compliance |
| **ISMS_REG_A523_4_Governance_YYYYMMDD.xlsx** | ~8 | IT Operations, Security | Ongoing monitoring, change management, incident tracking |

**Total Assessment Output:** ~34 sheets across 4 workbooks

## Assessment Domains Explained

**Domain 0 - Regulatory Updates (Specification)**:

- What regulatory frameworks apply? (DORA, NIS2, AI Act)
- What jurisdictional risks exist? (US CLOUD Act exposure)
- What additional fields are required? (concentration risk, data sovereignty)
- How do workbooks accommodate conditional compliance? (regulatory scope dropdowns)

**Domain 1 - Cloud Service Inventory & Classification**:

- What cloud services exist? (complete inventory: SaaS, IaaS, PaaS, security services)
- What data is processed? (classification: Public, Internal, Confidential, Restricted)
- What is service criticality? (business impact assessment)
- Where is data located? (residency: Switzerland, EU, USA, multi-region)
- What is exit feasibility? (portability, alternative vendors, transition cost)
- What regulatory scope applies? (DORA, NIS2, AI Act applicability per service)

**Domain 2 - Vendor Due Diligence & Contracts**:

- What due diligence was conducted? (certifications, audit reports, security questionnaires)
- What security clauses exist in contracts? (data protection, incident notification, audit rights)
- What are SLA commitments? (uptime, support response, breach notification timelines)
- What is provider jurisdiction? (headquarters, data centers, sub-processors)
- What is CLOUD Act exposure? (US-based providers, mitigation strategies)
- What exit provisions exist? (data export, transition assistance, termination clauses)

**Domain 3 - Secure Configuration & Deployment**:

- What configuration baselines apply? (CIS benchmarks, vendor hardening guides)
- What security controls are enabled? (encryption, MFA, network segmentation, logging)
- How is access managed? (least privilege, role-based access, privileged account monitoring)
- What monitoring is deployed? (security events, performance, compliance drift)
- What is shared responsibility division? (organization vs. provider controls)

**Domain 4 - Ongoing Governance & Risk Management**:

- What review schedule applies? (quarterly for high-risk, annual for low-risk)
- What performance metrics exist? (SLA compliance, incident frequency, support responsiveness)
- What incidents occurred? (security events, service disruptions, data breaches)
- What changes were approved? (configuration changes, contract amendments, migrations)
- What risks are tracked? (concentration risk, vendor lock-in, compliance gaps)

**Domain 5 - Compliance Monitoring Dashboard**:

- What is overall compliance status? (traffic light indicators per domain)
- What are key performance indicators? (service inventory completeness, contract coverage, configuration compliance)
- What gaps exist? (missing contracts, weak SLAs, configuration drift)
- What regulatory evidence exists? (DORA/NIS2 ICT register, AI Act documentation)
- What is the remediation roadmap? (prioritized action items, budget requirements)

## Assessment Workflow

```
┌──────────────────────────────────────────────────────────────┐
│ PHASE 1: GENERATION (Day 1)                                │
│ • Run 4 Python generator scripts                           │
│ • Output: 4 Excel workbooks with ~34 sheets total          │
│ • Validation: Automated structure and formula verification │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ PHASE 2: ASSESSMENT (Weeks 1-3)                            │
│ • Procurement/IT/Security teams complete workbooks         │
│ • Fill designated cells, use dropdown validations          │
│ • Document gaps, provide evidence (contracts, certs)       │
│ • Address regulatory fields if DORA/NIS2/AI Act applies    │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ PHASE 3: NORMALIZATION (Day 15)                            │
│ • Run normalization script                                 │
│ • Standardize filenames from review process                │
│ • Create audit trail manifest                              │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ PHASE 4: EXECUTIVE REVIEW (Week 4)                         │
│ • CISO reviews dashboard and risk register                 │
│ • Approve remediation roadmap and budget                   │
│ • Sign off on assessment package                           │
│ • Deliver to auditors (internal/external/regulatory)       │
└──────────────────────────────────────────────────────────────┘
```

---

# Automation Scripts

## Assessment Generator Scripts

| Script | Output Workbook | Purpose |
|--------|-----------------|---------|
| `generate_reg_a523_1_inventory.py` | ISMS-IMP-A.5.23.1_Inventory_{YYYYMMDD}.xlsx | Cloud service inventory and classification |
| `generate_reg_a523_2_vendor_dd.py` | ISMS-IMP-A.5.23.2_VendorDD_{YYYYMMDD}.xlsx | Vendor evaluation and contract review |
| `generate_reg_a523_3_secure_config.py` | ISMS-IMP-A.5.23.3_SecureConfig_{YYYYMMDD}.xlsx | Secure configuration and deployment |
| `generate_reg_a523_4_governance.py` | ISMS-IMP-A.5.23.4_Governance_{YYYYMMDD}.xlsx | Ongoing monitoring and risk management |

**Regulatory Enhancement**: All generators incorporate fields from ISMS-IMP-A.5.23.0 specification for DORA, NIS2, AI Act, and CLOUD Act compliance requirements.

## Supporting Scripts

| Script | Purpose |
|--------|---------|
**Script Quality Standards**:

- PEP 8 compliant Python code with consistent style
- Comprehensive error handling and input validation
- Detailed documentation explaining implementation rationale
- Modular functions enabling reusability across assessments
- Automated testing of critical functions
- Support for conditional regulatory logic (DORA/NIS2 fields shown only when applicable)

**Documentation Principle**: Scripts are designed to be readable, maintainable, and verifiable. What can be systematically created from documented specifications can be completely understood, reliably maintained, and objectively audited. Each function includes documentation explaining not just what it does, but why specific approaches were chosen - enabling future maintainers to understand design decisions and modify confidently without self-deception about implementation details.

---

# Roles & Responsibilities

## Executive Roles

| Role | Responsibilities |
|------|------------------|
| **CISO** | Overall accountability, policy approval, exception sign-off, risk acceptance, budget approval |
| **Executive Management** | Strategic supplier decisions, budget allocation, risk governance |
| **Procurement Director** | Vendor selection, contract negotiation, cost management |
| **Legal Counsel** | Contract review, regulatory compliance, agreement terms, dispute resolution |

## Operational Roles

| Role | Responsibilities |
|------|------------------|
| **Information Security Officer** | Policy ownership, enforcement, compliance monitoring, supplier risk assessment |
| **Procurement Team** | Supplier selection, RFP/RFQ management, vendor relationship management, contract administration |
| **IT Operations** | Technical implementation, configuration, monitoring, change management |
| **Cloud Architects** | Cloud service design, security configuration, architecture review |
| **System Owners** | Supplier relationships within their domains, business justification, budget approval |

## Supporting Roles

| Role | Responsibilities |
|------|------------------|
| **Compliance & Audit** | Regulatory interpretation (DORA, NIS2, AI Act), audit support, evidence collection |
| **Risk Management** | Supplier risk assessment, concentration risk analysis, risk register maintenance |
| **Data Protection Officer (DPO)** | GDPR Article 28 compliance, data processing agreements, privacy impact assessments |
| **Information Security** | Assessment tool development, generator scripts, validation automation |
| **Finance** | Budget tracking, cost analysis, ROI assessment |

## User Responsibilities

| Role | Responsibilities |
|------|------------------|
| **All Employees** | Adherence to approved cloud service list, prohibition on shadow IT, incident reporting |
| **Managers** | Budget approval for supplier services, business justification, user access management |

## Competence Requirements

Personnel performing supplier and cloud security assessment activities SHALL meet the following competence requirements, documented in [Organization ISMS Training and Competence Matrix]:

**Procurement Staff:**

- Supplier risk assessment training (internal or equivalent)
- Understanding of security requirements for cloud services
- Annual refresher on contract security clauses

**Cloud Architects / Technical Assessors:**

- Cloud security certification (CCSP, CCSK, or vendor-specific: AWS Security, Azure Security, GCP Security)
- Understanding of shared responsibility models
- Experience with cloud security configuration review

**Legal Counsel:**

- GDPR and data protection law training
- Understanding of processor agreements (GDPR Article 28)
- Familiarity with DORA/NIS2 requirements (where applicable)

**Information Security Officer:**

- ISO 27001 Lead Implementer or equivalent
- Risk assessment methodology training
- Cloud security frameworks (CSA CCM, ISO 27017/27018)

**Evidence:** Training records, certifications, and competence assessments maintained per ISO 27001 Clause 7.2 requirements.

---

# Assessment Methodology

## Programmatic Documentation Approach

This framework employs **quantitative, evidence-based assessment** rather than subjective evaluation:

**Core Principle**: What can be systematically created can be systematically maintained and objectively verified. Assessment tools are generated programmatically to ensure:

- **Consistency**: Identical structure across assessment cycles
- **Repeatability**: Same assessment methodology applied to all suppliers
- **Traceability**: Complete audit trail from policy to implementation to evidence
- **Maintainability**: Updates to requirements propagate systematically through regeneration
- **Objectivity**: Automated compliance calculation eliminates subjective scoring

**Implementation**:

- Generate assessment tools programmatically (Python → Excel)
- Enforce data validation and referential integrity through formula-driven cells
- Calculate compliance metrics automatically - no manual scoring
- Produce repeatable, auditable artifacts with version control
- Enable systematic updates when requirements change

**Evidence-Based Validation**:

- No "we're compliant because we said so" self-assessments
- Every "Compliant" status requires documented evidence (certificates, contracts, configurations)
- Every supplier requires third-party attestation (SOC 2, ISO 27001) or equivalent audit
- Every contract requires enforceable security clauses with audit rights
- Every exception requires CISO risk acceptance with documented mitigation

## Evidence Requirements

**For Each Supplier Service**:

| Evidence Type | Required Documentation | Minimum Standard |
|---------------|----------------------|------------------|
| **Certification** | SOC 2 Type II, ISO 27001, ISO 27017, CSA STAR | Current (see validity rules below) |
| **Contract** | Signed agreement with security clauses | GDPR Art. 28 compliant minimum |
| **Configuration** | Baseline security settings documentation | CIS benchmark or vendor hardening guide |
| **Monitoring** | SLA performance data, incident logs | Quarterly minimum |
| **Risk Assessment** | Documented due diligence and risk evaluation | Approved by CISO |

**Certification Validity Rules:**

| Certification | Validity Period | Currency Check |
|---------------|----------------|----------------|
| **ISO 27001** | 3 years (certificate cycle) | Annual surveillance audit confirmed within 12 months |
| **SOC 2 Type II** | 1 year (report period) | Report date within 12 months |
| **CSA STAR** | 2 years (Level 2) | Annual recertification or continuous monitoring |
| **ISO 27017/27018** | 3 years (aligned with ISO 27001) | Surveillance audit confirmed within 12 months |

**Rejection Criteria**:

- Supplier self-attestation without third-party validation
- Expired certifications (beyond validity period above)
- Contracts without security clauses or audit rights
- Missing data processing agreement (GDPR violation)
- No exit strategy or data portability mechanism

## Supplier Risk Classification

Suppliers are classified using **quantitative scoring** across six dimensions:

| Dimension | Weight | Scoring Criteria |
|-----------|--------|------------------|
| **Data Access** | 25% | Restricted=100, Confidential=75, Internal=50, Public=25, None=0 |
| **Service Criticality** | 25% | Critical (Tier 1)=100, High (Tier 2)=75, Medium (Tier 3)=50, Low (Tier 4)=25 |
| **Replaceability** | 15% | Single-source=100, Limited alternatives=75, Multiple alternatives=50, Commodity=25 |
| **Integration Depth** | 15% | Deep integration=100, Moderate=75, Light=50, None=25 |
| **Regulatory Impact** | 10% | DORA/NIS2 critical=100, GDPR processor=75, Compliance relevant=50, No impact=25 |
| **Concentration Risk** | 10% | >50% budget=100, 25-50%=75, 10-25%=50, <10%=25 |

> **Note:** Dimension weights may be adjusted based on organisational context. Financial institutions subject to FINMA, DORA, or equivalent supervisory frameworks may increase **Regulatory Impact** weight to 15-20% to reflect heightened supervisory expectations, reducing other dimensions proportionally.

**Concentration Risk Clarification:** Concentration risk is calculated as percentage of **total IT service budget** allocated to a single supplier. For example, if total IT budget is CHF 1M and AWS spend is CHF 400K, concentration risk is 40% (scores 75 points). Where a supplier provides services across multiple budget categories, aggregate spend across all categories.

**Total Score → Classification**:

- **Level 1 (Critical):** 75-100 points → Quarterly review, mandatory SOC 2 Type II or ISO 27001, on-site audit rights
- **Level 2 (High):** 50-74 points → Semi-annual review, third-party attestation required, remote audit rights
- **Level 3 (Medium):** 25-49 points → Annual review, self-assessment acceptable with sampling validation
- **Level 4 (Low):** 0-24 points → Biennial review, self-assessment acceptable

**Risk Methodology Integration:**

This supplier risk classification methodology operates within [Organization]'s enterprise risk assessment framework documented in [ISMS Risk Assessment Methodology]. Supplier risk scores feed into the organizational risk register per ISO 27001 Clause 6.1.2 requirements, enabling:

- Consistent risk evaluation across all ISMS domains  
- Integration with enterprise risk treatment plans
- Board-level risk reporting including supplier concentration risk (DORA Article 28.9)
- Risk acceptance workflow for exceptions

## Compliance Scoring

**Overall Compliance Status** (traffic light model):

| Status | Criteria | Action Required |
|--------|----------|-----------------|
| **Green (Compliant)** | All requirements met, evidence current (<12 months), no open findings | Routine monitoring |
| **Yellow (Partially Compliant)** | Minor gaps or evidence aging (12-18 months), non-critical findings | Remediation plan within 90 days |
| **Red (Non-Compliant)** | Major gaps, missing evidence, expired certifications (>18 months), critical findings | Immediate remediation or service suspension |

**Dashboard Metrics**:

- Compliance percentage by control (A.5.19-23)
- Supplier risk distribution (L1/L2/L3/L4)
- Contract coverage (% services with signed agreements)
- Certification status (% current vs. expired)
- Evidence completeness (% required documents available)

## Regulatory Conditional Logic

Assessment workbooks implement **conditional field display** based on regulatory applicability:

**DORA Fields** (displayed if: Financial sector entity in EU):

- ICT third-party risk register entry
- Concentration risk assessment
- Exit strategy documentation
- Sub-outsourcing approval status
- Competent authority cooperation clauses

**NIS2 Fields** (displayed if: Essential/important entity in EU):

- Supply chain security measures
- 24-hour incident reporting capability
- Management accountability documentation
- Annual cybersecurity risk report

**AI Act Fields** (displayed if: AI system provider/deployer):

- High-risk AI system classification
- Conformity assessment status
- Transparency obligations
- Human oversight mechanisms

**CLOUD Act Fields** (displayed if: US-headquartered provider):

- Jurisdictional risk assessment
- Legal challenge commitments
- Encryption and key management
- Supplementary measures (SCCs, TIA)

---

# Control Integration Matrix

## How Controls Work Together

This framework covers five related controls that work together across the supplier/cloud service lifecycle:

| Lifecycle Phase | Primary Control | Supporting Controls | Key Activities |
|-----------------|-----------------|---------------------|----------------|
| **Identification** | A.5.19 (Supplier relationships) | — | Supplier discovery, shadow IT identification, inventory creation |
| **Risk Assessment** | A.5.19 (Supplier relationships) | A.5.21 (Supply chain) | Risk classification, criticality assessment, due diligence scoping |
| **Selection** | A.5.19 + A.5.23 (Cloud specifics) | A.5.21 (Supply chain) | Vendor evaluation, security questionnaires, proof of concept |
| **Contracting** | A.5.20 (Agreements) | A.5.19, A.5.23 | Contract negotiation, security clauses, SLA definition, exit provisions |
| **Implementation** | A.5.23 (Cloud services) | A.5.20 | Service deployment, configuration, access provisioning, integration testing |
| **Operations** | A.5.22 (Monitoring) | A.5.19, A.5.23 | Performance monitoring, incident management, change control, compliance review |
| **Review** | A.5.22 (Monitoring) | A.5.19, A.5.20, A.5.21 | Periodic assessments, audit rights exercise, recertification, contract renewal |
| **Exit** | A.5.23 (Cloud exit) | A.5.20 | Data extraction, configuration backup, service migration, contract termination |

## Shared Responsibility Model

```
┌─────────────────────────────────────────────────────────────────┐
│                    SHARED RESPONSIBILITY                        │
├─────────────────────────────────────────────────────────────────┤
│  ORGANIZATION                    │  SUPPLIER/CSP                │
│  ─────────────────────────────── │  ─────────────────────────── │
│  • Define security requirements  │  • Meet contractual terms    │
│  • Conduct due diligence         │  • Provide certifications    │
│  • Review contracts              │  • Implement agreed controls │
│  • Monitor compliance            │  • Report incidents          │
│  • Manage access controls        │  • Support audits            │
│  • Document evidence             │  • Maintain SLAs             │
│  • Plan exit strategy            │  • Enable data portability   │
│  • Test exit procedures          │  • Provide transition support│
│  • Assess sub-suppliers          │  • Disclose supply chain     │
│  • Verify regulatory compliance  │  • Maintain certifications   │
└─────────────────────────────────────────────────────────────────┘
```

**Service Model Responsibility Breakdown:**

| Layer | IaaS (AWS EC2) | PaaS (Azure App Service) | SaaS (Microsoft 365) |
|-------|----------------|--------------------------|----------------------|
| **Data** | Organization | Organization | Organization |
| **Application** | Organization | Organization | Provider |
| **Runtime** | Organization | Provider | Provider |
| **OS** | Organization | Provider | Provider |
| **Virtualization** | Provider | Provider | Provider |
| **Servers** | Provider | Provider | Provider |
| **Storage** | Provider | Provider | Provider |
| **Networking** | Shared | Provider | Provider |

---

# Lifecycle Management

## Supplier Lifecycle Phases

**Phase 1: Selection & Due Diligence (A.5.19, A.5.21)**

- Business requirement definition
- Vendor identification and shortlisting
- Security questionnaire distribution
- Risk assessment and classification
- Technical evaluation (POC/pilot)
- Due diligence review (certifications, references, financial stability)

**Phase 2: Contracting (A.5.20)**

- Contract negotiation with security clauses
- Data processing agreement (GDPR Art. 28)
- Service level agreement (SLA) definition
- Audit rights establishment
- Exit strategy documentation
- Legal and procurement approval

**Phase 3: Onboarding & Configuration (A.5.23)**

- Security baseline configuration
- Access provisioning (least privilege)
- Monitoring and logging setup
- Integration with organizational systems
- User training and documentation
- Go-live approval

**Phase 4: Operation & Monitoring (A.5.22)**

- Continuous performance monitoring
- SLA compliance tracking
- Periodic security reviews
- Change management
- Incident response and resolution
- Relationship management

**Phase 5: Review & Optimization (A.5.22)**

- Annual contract review
- Cost-benefit analysis
- Service optimization
- Renegotiation or renewal
- Alternative evaluation

**Phase 6: Exit & Transition (A.5.23)**

- Exit trigger identification
- Data export and validation
- Service migration or replacement
- Contract termination
- Data destruction verification
- Lessons learned documentation

**Exit Plan Testing Requirements:**

- Exit plans for **Level 1 (Critical)** suppliers SHALL be tested annually (DORA Art. 28.6 where applicable)
- Exit plans for **Level 2 (High)** suppliers SHALL be tested biennially or upon major service change
- Exit plan testing includes: data export validation, service migration simulation, BC/DR integration verification
- Test results documented in ISMS-IMP-A.5.23.4 (Governance workbook) and reported to CISO

## Review Cycles

| Supplier Level | Review Frequency | Review Scope |
|----------------|-----------------|--------------|
| **Level 1 (Critical)** | Quarterly | Full compliance review, SLA performance, risk reassessment, certification status |
| **Level 2 (High)** | Semi-annually | Compliance spot-check, SLA performance, major changes review |
| **Level 3 (Medium)** | Annually | Compliance validation, contract renewal assessment |
| **Level 4 (Low)** | Biennially | Contract renewal decision, continued business need |

**Trigger Events for Ad-Hoc Review**:

- Security incident involving supplier
- Major service change or migration
- Contract amendment or renewal
- Merger/acquisition of supplier
- Regulatory change affecting supplier obligations
- Audit finding or compliance gap

## Exception Management

**Exception Request Process**:

1. **Request Submission**: Requestor documents exception with business justification
2. **Risk Assessment**: Security team evaluates risk level and potential impact
3. **Compensating Controls**: Identify mitigating measures if exception approved
4. **Approval Decision**:

   - Low risk: Information Security Officer
   - Medium risk: CISO
   - High risk: CISO + CIO
   - Critical risk: Executive Management

5. **Documentation**: Exception registered with approval, duration, and review date
6. **Monitoring**: Periodic review (quarterly for temporary, annual for permanent)
7. **Remediation**: Action plan for exception closure if temporary

**Common Exception Scenarios**:

- Supplier lacks SOC 2 but has alternative certification (ISO 27001)
- Legacy service without modern security features (exit plan required)
- Single-source critical supplier (concentration risk mitigation)
- Non-compliant contract inherited from acquisition (renegotiation timeline)

## Shadow IT Detection

Shadow IT (unauthorised cloud services or suppliers used without IT/Security approval) SHALL be actively detected through the following methods:

**Detection Methods:**

- **Firewall/proxy log analysis**: Identify connections to unregistered SaaS/cloud services
- **DNS query monitoring**: Detect resolution of domains associated with cloud services not in the approved supplier register
- **Cloud Access Security Broker (CASB)**: Automated discovery of cloud service usage (where deployed)
- **Expense report review**: Identify cloud service subscriptions in procurement/finance records
- **User self-reporting**: Encourage voluntary disclosure through awareness campaigns (no-blame policy for existing usage)

**Detection Cadence:**

- Quarterly shadow IT scans SHALL be conducted by IT Operations
- Results reported to CISO with remediation recommendations
- Discovered services assessed for risk and either onboarded to the approved register or decommissioned

---

# Incident Management

## Supplier Incident Categories

| Incident Type | Definition | Response |
|---------------|------------|----------|
| **Security Breach** | Unauthorized access, data breach, ransomware | Immediate containment, forensic investigation, notification (GDPR 72h, NIS2 24h) |
| **Service Outage** | Unplanned downtime exceeding SLA | Incident management, business continuity activation, supplier communication |
| **Contract Violation** | Supplier non-compliance with agreement | Escalation to legal, remediation demand, potential termination |
| **Performance Degradation** | SLA metric failures | Performance improvement plan, monitoring intensification |
| **Change Failure** | Unauthorized or failed change | Rollback procedures, change control review |

## Notification Requirements

**Internal Notification**:

- Immediate: CISO, System Owner, IT Operations
- Within 4 hours: Executive Management (for critical incidents)
- Within 24 hours: DPO (if personal data involved)

**External Notification**:

- **GDPR**: Data Protection Authority within 72 hours (Art. 33)
- **NIS2**: Competent authority within 24 hours (early warning), 72 hours (incident notification), 1 month (final report)
- **DORA**: Competent authority per regulatory timeline
- **Contractual**: Customer notification per contract terms

**Supplier Notification Requirements**:

| Incident Severity | Supplier Notification Timeline |
|-------------------|-------------------------------|
| **Critical** (data breach, ransomware) | Immediate (within 4 hours of awareness) |
| **High** (service outage, security event) | Within 24 hours |
| **Medium** (degraded performance, configuration change) | Within 72 hours |
| **Low** (maintenance, planned downtime) | 5 business days advance notice |

- Notification must include: incident description, affected systems, data impact, containment measures, estimated resolution
- Suppliers SHALL cooperate with incident investigation and forensics
- Suppliers SHALL provide post-incident report within agreed timeline
- These timelines SHALL be incorporated into supplier contracts (procurement/legal to use as contractual language)

## Post-Incident Actions

**Immediate Actions (0-24 hours)**:

- Incident containment and service restoration
- Impact assessment and evidence preservation
- Stakeholder communication
- Regulatory notification (if required)

**Short-Term Actions (1-7 days)**:

- Root cause analysis
- Remediation plan development
- Supplier performance review
- Contract compliance assessment

**Long-Term Actions (1-3 months)**:

- Lessons learned documentation
- Control enhancement implementation
- Supplier relationship reassessment
- Policy and procedure updates

---

# Compliance & Audit

## Mandatory Requirements

This policy framework demonstrates compliance with:

**Primary Standards:**

- ISO/IEC 27001:2022 Annex A Controls 5.19-5.23
- ISO/IEC 27002:2022 Controls 5.19-5.23 (implementation guidance)
- ISO/IEC 27036 (series) - Information security for supplier relationships

**Cloud-Specific Standards:**

- ISO/IEC 27017:2015 - Cloud security controls
- ISO/IEC 27018:2019 - Cloud privacy (PII protection)
- CSA CCM (Cloud Controls Matrix) - cloud control framework alignment

**Regulatory Alignment:**

- **Swiss Federal Data Protection Act (FADP)**: Data processing agreements, Art. 9 processor obligations
- **EU GDPR**: Article 28 processor agreements, sub-processor disclosure where applicable
- **DORA** (Digital Operational Resilience Act): ICT third-party risk management for EU financial entities
- **NIS2** (Network and Information Security Directive 2): Supply chain security for essential/important entities in EU
- **EU AI Act**: AI system provider/deployer obligations where applicable
- **US CLOUD Act**: Jurisdictional risk assessment and mitigation

## Audit Evidence

Auditors should expect the following evidence:

**Policy Documentation:**

- Complete policy framework (ISMS-POL-A.5.19-23 and subsections S1-S6)
- Approval records (CISO, Executive Management, Legal, Procurement Director)
- Distribution records (training acknowledgments, policy portal access logs)

**Implementation Evidence:**

- Completed assessment workbooks (4 Excel files)
- Supplier inventory with risk ratings
- Supplier contracts with security clauses highlighted
- Cloud service agreements with SLA and exit provisions
- Evidence artifacts:
  - Vendor certifications (ISO 27001, SOC 2, CSA STAR)
  - Third-party audit reports
  - Security questionnaire responses
  - Due diligence documentation
  - Contract addenda and amendments

**Operational Evidence:**

- Supplier review meeting minutes
- Incident notifications from suppliers (per contractual obligations)
- Change management records (service changes, migrations, configuration updates)
- Supplier audit reports and findings
- SLA performance reports (uptime, support response, incident resolution)
- Cloud configuration reviews (CIS benchmark compliance, security baselines)

**Regulatory Evidence (DORA/NIS2/AI Act):**

- ICT third-party risk register (DORA Article 28)
- Concentration risk assessment for critical providers
- Exit plan testing documentation
- Supply chain transparency documentation
- Incident notification logs to regulators (24h/72h/final reports)
- AI system risk classification documentation
- High-risk AI system conformity assessments

**Effectiveness Evidence:**

- Supplier risk scores (trend analysis over time)
- Contract compliance percentage (security clauses present in X% of contracts)
- Incident statistics from supplier services
- Cloud exit plan testing results
- Stakeholder feedback (business units, IT operations, security team)
- Cost-benefit analysis (cloud service optimization, vendor consolidation)

## Audit Approach

**Recommended Audit Methodology:**

1. **Document Review:** Verify policy completeness, approval, distribution
2. **Technical Assessment:** Review generated workbooks, validate evidence quality
3. **Sampling:** Select high-risk suppliers for detailed review (10-20% of inventory)
4. **Contract Review:** Verify security clauses in agreements (sample 5-10 contracts)
5. **Cloud Assessment:** Review cloud service selection, configuration, and exit planning
6. **Regulatory Verification:** Verify DORA/NIS2/AI Act compliance where applicable
7. **Interview:** Discuss with Procurement, Legal, IT Operations, Cloud Architects, Security
8. **Gap Analysis:** Compare actual vs. required capabilities
9. **Remediation Review:** Assess gap closure plans, timelines, and budget allocation

**Sampling Strategy:**

- **Critical Suppliers**: 100% review (audit all critical suppliers)
- **High-Risk Suppliers**: 50% sampling
- **Medium-Risk Suppliers**: 25% sampling
- **Low-Risk Suppliers**: 10% sampling or risk-based selection

**Audit Frequency:**

- **Internal Audit:** Annual (minimum), quarterly for DORA/NIS2 entities
- **External Audit:** As required by ISO 27001 certification body
- **Regulatory Audit:** As required (DORA, NIS2, financial regulators, data protection authorities)
- **Self-Assessment:** Quarterly (using assessment workbooks)

**Internal Audit Programme Integration:**

Supplier and cloud services security is included in the annual internal audit programme per ISO 27001 Clause 9.2. Audit frequency is risk-based:

- **Critical suppliers (L1)**: Audited annually with 100% coverage
- **High-risk suppliers (L2)**: Audited annually with 50% sampling
- **Medium-risk suppliers (L3)**: Audited biennially with 25% sampling
- **Low-risk suppliers (L4)**: Included in 3-year audit cycle with 10% sampling

Audit scope includes verification of: policy compliance, contract security clauses, supplier certifications currency, incident management effectiveness, and exit plan testing.

---

# Policy Maintenance

## Review Schedule

**Annual Review:** Comprehensive review of all policy sections (recommended Q4)

**Triggered Reviews:** Major events requiring immediate policy review:

- **Significant regulatory changes**: DORA technical standards, NIS2 implementing acts, AI Act delegated acts
- **Major supplier security incidents**: Data breaches, service disruptions >24h, supply chain compromises
- **Cloud service provider changes**: Mergers/acquisitions, major migrations, service discontinuation
- **Organizational M&A activity**: New subsidiaries, divestitures, business unit changes
- **New cloud service categories adopted**: Emerging technologies (AI/ML platforms, quantum-safe cryptography)
- **Audit findings requiring policy updates**: External audit, regulatory audit, internal audit critical findings

## Version Control

**Major Version (X.0):** Structural changes, new controls added, regulatory requirements, scope expansion  
**Minor Version (X.Y):** Content updates, clarifications, additions without structural change

**Master Framework Versioning:**

- This master document version reflects overall framework state
- Individual section versions (S1-S6) may increment independently
- Major framework changes require master document version update and re-approval

## Change Process

**Standard Changes:**
1. Change request submitted to Policy Owner (CISO)
2. Impact assessment (affected stakeholders, suppliers, contracts, regulatory obligations)
3. Stakeholder consultation (Procurement, Legal, IT Operations, Security, Compliance, DPO)
4. Draft revision prepared with tracked changes
5. Review and approval by CISO and required stakeholders (Legal, Procurement Director, Executive Management)
6. Communication plan executed:

   - Policy portal update
   - Training updates (procurement, cloud administrators, legal)
   - Supplier notifications where policy changes affect agreements

7. Contract amendment process initiated if required (standard clause updates, SLA revisions)
8. Implementation tracking (30/60/90 day checkpoints)

**Emergency Changes:**

- Critical supplier incidents or regulatory deadlines (e.g., DORA compliance deadline) may require expedited process
- Emergency approval by CISO with retrospective stakeholder review
- Documentation of justification for emergency process
- Post-implementation review within 30 days

## Communication

**Policy Updates Communicated Via:**

- Policy portal (central repository, version-controlled)
- Email notifications to:
  - All Procurement staff
  - Legal and Compliance teams
  - IT Operations and Cloud Administrators
  - Security team
  - Supplier relationship managers
- Training updates:
  - Procurement training (supplier risk assessment, contract review)
  - Cloud administrator training (security configuration, compliance monitoring)
  - Security awareness (shadow IT risks, approved service list)
- Quarterly CISO briefings to Executive Management
- Supplier notifications where policy changes affect agreements (contractual requirement changes, new security clauses)
- Regulatory notifications where required (NIS2 reporting, DORA ICT register updates)

---

# Integration with ISMS

## Related Controls

Supplier and cloud services security integrates with multiple ISO 27001 controls:

| Control | Integration Point |
|---------|-------------------|
| **A.5.1** | Policies - Supplier/cloud policy is part of ISMS policy suite |
| **A.5.9** | Inventory - Supplier/cloud services tracked in asset inventory |
| **A.5.12** | Classification - Data classification drives supplier security requirements |
| **A.5.24-5.28** | Incident Management - Supplier incident notification and response |
| **A.5.30** | **Business Continuity - Supplier disruption scenarios, alternative providers, BC/DR INTEGRATION FOR EXIT SCENARIOS** ⭐ |
| **A.5.31** | Legal & Regulatory - Contractual security obligations, regulatory compliance requirements |
| **A.8.8** | Vulnerability Management - Supplier patching commitments, vulnerability disclosure |
| **A.8.10** | Information Deletion - Supplier data deletion verification upon exit |
| **A.8.13-14** | **Backup & Redundancy - Independent backups for cloud exit, geographic redundancy for concentration risk** ⭐ |
| **A.8.24** | Cryptography - Encryption requirements for suppliers, key management |
| **Clause 6.1** | Risk Assessment - Supplier risks in organizational risk register |

## Bidirectional Data Flows

**Supplier/Cloud Management → Other Controls:**

- Supplier incidents → Incident management (A.5.24-28)
- Cloud service inventory → Asset inventory (A.5.9)
- Supplier vulnerabilities → Vulnerability management (A.8.8)
- Cloud data classification → Information classification (A.5.12)
- Supplier disruptions → Business continuity (A.5.30)
- **Exit requirements → BC/DR planning (A.8.13-14, A.5.30)** ⭐

**Other Controls → Supplier/Cloud Management:**

- Risk assessments → Supplier risk classification (A.5.19)
- Incident lessons learned → Contract amendments (A.5.20, A.5.22)
- Vulnerability findings → Supplier patch requirements (A.5.22)
- BCP testing → Alternative supplier identification (A.5.23)
- **BC/DR capabilities → Exit feasibility assessment (A.5.23)** ⭐

## Risk Management Integration

**Risk Treatment:**

- Supplier/cloud security controls as risk mitigation (access controls, encryption, monitoring)
- Residual risks from supplier dependencies tracked in risk register
- Risk assessment feeds supplier selection and contract requirements

**Risk Register:**

- Risk categories: Concentration risk, vendor lock-in, data sovereignty, regulatory exposure
- Risk scores drive remediation urgency and budget allocation
- Exception risks monitored quarterly and reported to CISO

**Concentration Risk Assessment (DORA Requirement):**

- Critical suppliers with >20% organizational dependency
- Alternative provider feasibility analysis
- Diversification strategy and timeline
- **Exit capability validation with BC/DR framework** ⭐
- Board-level reporting for critical dependencies

## BC/DR Integration for Exit Scenarios

**Critical Principle:** Exit scenarios require **BOTH** A.5.19-23 (contractual rights) AND BC/DR (technical capability)

| Scenario | A.5.19-23 Requirement | BC/DR Capability | Integration Required |
|----------|----------------------|------------------|---------------------|
| **Cloud provider bankruptcy** | Termination rights (A.5.20) | Independent backups (A.8.13) | ✅ BOTH |
| **Service quality degradation** | SLA enforcement (A.5.20) | Failover capability (A.8.14) | ✅ BOTH |
| **Regulatory data sovereignty** | Geographic constraints (A.5.23) | Alternative site (A.8.14) | ✅ BOTH |
| **Strategic cloud exit** | Exit procedures (A.5.23) | Migration capability (A.5.30) | ✅ BOTH |
| **Cost reduction initiative** | Contract negotiation (A.5.22) | On-prem capacity (A.8.6) | ✅ BOTH |
| **Vendor lock-in concern** | Portability rights (A.5.23) | Format independence (A.8.13) | ✅ BOTH |

**Integration Requirements:**

1. **Contractual Rights Need Technical Capability:**

   - Contract says "30-day exit" but BC/DR requires 6 months → Gap (must align)
   - Contract says "API-based export" and BC/DR can execute in 20 days → Ready ✅

2. **Technical Capability Needs Contractual Permission:**

   - BC/DR can migrate in 1 week but contract requires 90 days notice → Blocked (must negotiate)
   - BC/DR capability matches contract terms → Executable ✅

3. **Untested Integration = Unknown Risk:**

   - Both frameworks exist but never tested together → Don't know if they work
   - Exit plans tested annually (DORA Art. 28.6) with BC/DR validation → Proven capability ✅

**Documentation:** Exit planning integration documented in:

- ISMS-IMP-A.5.23.4 (Governance workbook - Exit Strategy sheet)
- ISMS-POL-A.5.30-8.13-14 (BC/DR Policy - Supplier exit scenarios)

**Reference:** See "A.5.19-23 ↔ BC/DR Integration - Critical for Exit Scenarios" alignment document for detailed integration requirements.

---

# Regulatory Applicability

This policy implements supplier and cloud service security requirements to comply with regulations per **ISMS-POL-00 (Regulatory Applicability Framework)**:

## Tier 1: Mandatory Compliance

| Regulation | Requirement | Applicability |
|------------|-------------|---------------|
| **Swiss nDSG (Federal Data Protection Act)** | Processor security measures (Art. 9), sub-processor disclosure | All [Organization] processing of personal data |
| **EU GDPR** | Processor agreements (Art. 28), security measures (Art. 32), data breach notification (Art. 33) | When processing EU personal data |
| **ISO/IEC 27001:2022** | Controls A.5.19-23 | Certification scope |

## Tier 2: Conditional Applicability

| Regulation | Requirement | Trigger Condition |
|------------|-------------|-------------------|
| **FINMA Circular 2023/1** | Operational resilience, outsourcing governance, sub-outsourcing register, incident reporting | Swiss FINMA-regulated financial institution |
| **DORA (Digital Operational Resilience Act)** | ICT third-party risk management (Art. 28-31): risk register, concentration assessment, exit strategies, contractual provisions | EU financial services operations |
| **NIS2 Directive** | Supply chain security measures (Art. 21), incident reporting (Art. 23): 24h early warning, 72h notification, final report | Essential/important entity designation |
| **EU AI Act** | High-risk AI system requirements (Art. 9-15): conformity assessment, transparency, human oversight | Providing/deploying AI systems in EU |
| **US CLOUD Act** | Jurisdictional data access considerations, legal process transparency | Using US-headquartered cloud providers |

> **Multiple Conditional Regulations:** Organisations subject to multiple conditional regulations (e.g., FINMA + DORA, or DORA + NIS2) SHALL implement the most stringent requirement where overlap exists. Assessment workbooks enable parallel tracking of FINMA, DORA, and NIS2 fields to ensure all applicable requirements are met simultaneously.

## Tier 3: Informational Guidance

Best practice frameworks referenced but not mandatory compliance requirements:

- ISO/IEC 27036 (Information security for supplier relationships)
- ISO/IEC 27017 (Cloud security controls)
- ISO/IEC 27018 (Cloud privacy)
- NIST SP 800-161 (Cybersecurity Supply Chain Risk Management)
- CSA Cloud Controls Matrix (CCM)

## DORA-Specific Requirements

For EU financial entities subject to DORA, the following additional requirements apply:

**Article 28 - ICT Third-Party Risk**:

- Maintain comprehensive ICT third-party risk register
- Document risk assessment for each ICT third-party service provider
- Identify concentration risk and critical ICT third-party service providers
- Implement monitoring and risk management strategy

**Article 29 - Key Contractual Provisions**:

- Full cooperation with competent authorities (access, inspection, audit rights)
- Subcontracting requirements and approval process
- Exit strategies including data portability and transition assistance
- Service level agreements with security metrics
- Audit rights (on-site and remote)
- Termination rights in case of non-compliance

**Article 30 - Sub-Outsourcing**:

- Maintain register of sub-outsourcing arrangements
- Assess risks from sub-outsourcing
- Ensure contractual provisions flow down to sub-contractors
- Obtain authorization for critical sub-outsourcing

**Article 31 - ICT Concentration Risk**:

- Assess concentration risk from individual ICT third-party providers
- Document dependencies on critical providers
- Implement mitigation strategies for concentration risk
- Report concentration risk to competent authorities

**Implementation Notes**:

- DORA-specific fields in assessment workbook 2 (Due Diligence)
- Concentration risk analysis in workbook 4 (Governance)

## NIS2-Specific Requirements

For essential/important entities subject to NIS2, the following apply:

**Article 21 - Cybersecurity Risk Management**:

- Supply chain security measures including vendor security assessment
- Policies on acquisition, development, and maintenance of ICT systems
- Asset management and configuration management
- Incident handling including supply chain incidents

**Article 23 - Incident Notification**:

- Early warning to CSIRT/competent authority (24 hours after becoming aware)
- Incident notification (72 hours): preliminary assessment, impact, indicators of compromise
- Final report (1 month or upon authority request): detailed description, root cause, impact assessment, remediation measures

**Article 24 - Governance**:

- Management body accountability for cybersecurity risk management
- Regular cybersecurity training for management
- Annual cybersecurity risk assessment report

**Implementation Notes**:

- NIS2-specific incident notification workflows in workbook 4 (Governance)
- Supply chain security measures checklist in workbook 2 (Due Diligence)

## FINMA Sub-Outsourcing Requirements (Circular 2023/1)

For Swiss banks subject to FINMA Circular 2023/1, the following sub-outsourcing requirements apply:

**Sub-Outsourcing Definition:**
Material services outsourced by a bank to a service provider, where the service provider further delegates those services to a sub-outsourcer (sub-supplier).

**Register Requirements:**
- Maintain comprehensive register of all sub-outsourcing arrangements
- Update register when sub-outsourcing occurs or changes
- Include in register:
  - Sub-outsourcer name and jurisdiction
  - Services provided (description and criticality)
  - Data access and processing activities
  - Geographic location of service delivery
  - Risk assessment and mitigation measures
  - FINMA approval status (where required)

**Approval Requirements:**
- Material sub-outsourcing requires bank approval before implementation
- Bank must assess sub-outsourcing risks (operational, concentration, data protection, jurisdiction)
- Contractual flow-down of bank requirements to sub-outsourcers
- Right to audit sub-outsourcers (direct or via service provider)

**Implementation:**
- Sub-outsourcing register maintained in ISMS-IMP-A.5.23.2 (Due Diligence workbook - Sub-Supplier Sheet)
- Sub-outsourcer risk assessment documented in ISMS-IMP-A.5.23.4 (Governance workbook)
- Approval workflow integrated with supplier onboarding process (Section 8: Lifecycle Management)

## Data Sovereignty & Cross-Border Considerations

| Framework | Impact on Cloud Services |
|-----------|--------------------------|
| **US CLOUD Act** | US-headquartered providers may be compelled to disclose data regardless of storage location. Assess provider HQ jurisdiction, evaluate legal challenge commitments, implement technical safeguards (encryption, customer-controlled keys). |
| **EU Data Boundary Initiatives** | Some providers offer EU-only data processing guarantees (AWS European Sovereign Cloud, Azure EU Data Boundary, Google Cloud EU regions). Verify contractual commitments and technical implementation. |
| **Swiss-US Data Privacy Framework** | Adequacy mechanism for US transfers (replaced Privacy Shield). Verify provider self-certification at https://www.dataprivacyframework.gov/list |
| **Schrems II Implications** | Additional safeguards required for non-adequate country transfers: Transfer Impact Assessment (TIA), Standard Contractual Clauses (SCCs), supplementary technical measures (encryption, access controls). |

**Jurisdictional Risk Assessment Matrix**:

| Risk Factor | Assessment Criteria |
|-------------|---------------------|
| **Provider headquarters jurisdiction** | US CLOUD Act exposure assessment. US-based providers subject to data disclosure orders. |
| **Data processing locations** | Regulatory alignment with data residency requirements (nDSG, GDPR Art. 44-50, NIS2, DORA). |
| **Sub-processor locations** | Downstream jurisdictional exposure. Review sub-processor list for non-adequate countries. |
| **Contractual commitments** | Provider's legal challenge commitments (resist unlawful disclosure orders, notify customer). |
| **Technical measures** | Encryption (data-at-rest, data-in-transit, in-use), customer-controlled key management, access controls (geo-fencing, IP allowlisting). |

**Organizations handling Confidential or Restricted data SHALL**:
1. Document jurisdictional risk assessment for each cloud service
2. Implement compensating controls (end-to-end encryption, customer-managed encryption keys, access restrictions)
3. Obtain risk acceptance from CISO for residual jurisdictional risks
4. Review annually or upon regulatory/geopolitical changes

## United States Federal Requirements

References to US federal frameworks (FISMA, FIPS, FedRAMP, NIST cybersecurity requirements, CMMC) apply **only** where [Organization]:

- Acts as contractor, subcontractor, or service provider to US federal agencies
- Provides services to customers subject to such regulations
- Has explicit contractual obligations requiring such compliance

In all other cases, these references are informational only and do not constitute mandatory compliance requirements.

---

# Definitions

**Supplier**: External organization providing products or services to [Organization] that may access, process, store, or transmit organizational information.

**Cloud Service Provider (CSP)**: Supplier providing cloud computing services (IaaS, PaaS, SaaS) over network.

**ICT Third-Party Service Provider**: Supplier providing ICT products or services critical to organizational operations (DORA terminology).

**Sub-Processor**: Supplier's own suppliers (sub-suppliers) that may access organizational data.

**Shared Responsibility Model**: Division of security responsibilities between cloud service provider and customer.

**Due Diligence**: Systematic evaluation of supplier security posture before engagement.

**Concentration Risk**: Risk arising from dependency on single supplier or limited number of suppliers for critical services.

**Vendor Lock-In**: Dependence on supplier's proprietary technology making migration costly or difficult.

**Exit Strategy**: Plan for orderly termination of supplier relationship including data export and service migration.

**Data Residency**: Geographic location where data is physically stored and processed.

**Data Sovereignty**: Legal requirement that data be subject to laws of country where located.

**Transfer Impact Assessment (TIA)**: Assessment of adequacy of data protection in destination country (GDPR Schrems II requirement).

**Standard Contractual Clauses (SCCs)**: EU Commission-approved contractual terms for international data transfers.

**US CLOUD Act**: Clarifying Lawful Overseas Use of Data Act - US law requiring US companies to provide data to US law enforcement regardless of storage location.

**DORA**: Digital Operational Resilience Act - EU regulation for financial sector ICT risk management.

**NIS2**: Network and Information Security Directive 2 - EU directive for cybersecurity of essential/important entities.

**Shadow IT**: Unauthorized cloud services or suppliers used without IT/Security approval.

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Procurement Director** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

# Evidence for This Policy

## Stage 1 (Documentation Review) Evidence

Evidence required to demonstrate this policy framework is adequately documented and approved:

- ✅ This master policy document (ISMS-POL-A.5.19-23 v1.0)
- ✅ Approval signatures from CISO, CIO, Procurement Director, Legal/Compliance Officer, Executive Management (Approval Record)
- ✅ Sub-policy documents complete (S1-S6):
  - S1: Supplier Relationship Fundamentals (A.5.19)
  - S2: Supplier Agreement Requirements (A.5.20)
  - S3: ICT Supply Chain Security (A.5.21)
  - S4: Supplier Monitoring & Change Management (A.5.22)
  - S5: Cloud Services Security (A.5.23)
  - S6: Assessment Methodology & Automation
- ✅ Control alignment with ISO/IEC 27001:2022 A.5.19-23 documented (Section 2: Control Alignment)
- ✅ Supplier risk classification methodology defined (Section 6: Supplier Risk Classification)
- ✅ Compliance scoring thresholds established (Section 6: Compliance Scoring)
- ✅ Lifecycle management phases documented (Section 8: Lifecycle Management)
- ✅ Incident management categories and notification requirements defined (Section 9: Incident Management)
- ✅ Roles and responsibilities assigned with competence requirements (Section 5)
- ✅ Regulatory applicability framework documented (Section 12: Regulatory Applicability)
- ✅ Integration with related ISMS controls documented (Section 11: Integration with ISMS)
- ✅ BC/DR integration for exit scenarios defined (Section 11: BC/DR Integration)

## Stage 2 (Operational Effectiveness) Evidence

Evidence required to demonstrate this policy framework is operationally effective:

- **Cloud Service Inventory**: ISMS-IMP-A.5.23.1 workbook showing complete inventory with data classification, criticality ratings, residency, and exit feasibility
- **Vendor Due Diligence Records**: ISMS-IMP-A.5.23.2 workbook documenting due diligence evaluations, certifications reviewed, security questionnaire responses
- **Signed Contracts with Security Clauses**: Supplier agreements containing required security provisions (GDPR Art. 28, audit rights, incident notification, exit provisions)
- **Configuration Baselines**: ISMS-IMP-A.5.23.3 workbook showing security configuration compliance against CIS benchmarks or vendor hardening guides
- **Supplier Review Meeting Minutes**: Quarterly/semi-annual/annual review documentation showing SLA performance, compliance status, remediation tracking
- **Ongoing Governance Records**: ISMS-IMP-A.5.23.4 workbook tracking monitoring results, change management, incident history, risk assessments
- **Supplier Certification Evidence**: Current SOC 2 Type II, ISO 27001, CSA STAR certificates for critical/high-risk suppliers (within 12 months)
- **SLA Performance Reports**: Monthly/quarterly reports showing uptime, support response times, incident resolution metrics
- **Incident Notifications from Suppliers**: Documented security incidents per contractual notification requirements with response evidence
- **Change Management Records**: Approved service changes, configuration updates, migrations, and contract amendments
- **Exit Plan Test Results**: Annual exit strategy validation demonstrating data export capability and transition readiness (DORA Art. 28.6)
- **Concentration Risk Assessments**: Documented analysis of critical supplier dependencies with mitigation strategies
- **Exception Register**: Approved exceptions with business justification, compensating controls, and CISO sign-off
- **Regulatory Evidence (where applicable)**:
  - DORA: ICT third-party risk register, concentration risk reports, competent authority cooperation records
  - NIS2: 24h/72h/final incident reports to CSIRT, annual cybersecurity risk assessment
  - AI Act: High-risk AI system conformity assessments, transparency documentation

## Clarification on Compliance Evidence

This policy framework establishes **supplier and cloud services security governance requirements** covering the complete lifecycle from supplier selection through secure exit, including risk classification, contractual requirements, supplier incident notification, ongoing monitoring, access requirements for supplier personnel, and cloud-specific considerations.

It does **NOT** establish:
- **Internal IT operations** (addressed in ISMS-POL-A.8.1-7-18-19 - Endpoint Security, ISMS-POL-A.8.20-22 - Network Security)
- **Data classification methodology** (addressed in ISMS-POL-A.5.12 - Information Classification; supplier access requirements reference this classification)
- **Organisational incident response procedures** (addressed in ISMS-POL-A.5.24-28 - Incident Management; this policy defines supplier incident notification requirements that feed into that framework)
- **Business continuity procedures** (addressed in ISMS-POL-A.5.30 and ISMS-POL-A.8.13-14 - Backup & Redundancy; this policy defines exit requirements that integrate with BC/DR capabilities)
- **Employee authentication controls** (addressed in ISMS-POL-A.5.15-16-18 - Identity Access Management, ISMS-POL-A.8.2-3-5 - Privileged Access & Authentication; this policy requires suppliers to implement equivalent controls)

The boundary is: **This policy governs EXTERNAL supplier/cloud relationships** (what suppliers must do, what contracts must contain, how to monitor suppliers) → Internal technical policies govern INTERNAL systems and employees → This policy's requirements REFERENCE internal policies but do not duplicate them.

---

**END OF POLICY DOCUMENT**

---

*This master index provides comprehensive governance for supplier and cloud services security. Detailed requirements for each control are documented in sections S1-S6. Assessment tools and implementation guidance are provided in the ISMS-IMP-A.5.23 document suite.*
<!-- QA_VERIFIED: 2026-02-02 -->
