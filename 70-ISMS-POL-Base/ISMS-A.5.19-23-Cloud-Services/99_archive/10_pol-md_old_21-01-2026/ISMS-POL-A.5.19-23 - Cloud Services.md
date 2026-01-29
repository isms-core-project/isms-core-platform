# ISMS-POL-A.5.19-23 – Supplier & Cloud Services Security
## Comprehensive Policy & Implementation Framework

---

## Document Control

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
- ISMS-IMP-A.5.23 (Implementation Guidance Suite)
- ISMS-REF-A.5.23 (Cloud Service Provider Registry)
- ISO/IEC 27001:2022 Controls A.5.19-23
- ISO/IEC 27036 (Supplier Relationships)
- ISO/IEC 27017 (Cloud Security)
- ISO/IEC 27018 (Cloud Privacy)

**Distribution**: All employees, contractors, procurement staff, legal team, IT operations, cloud administrators

---

## Executive Summary

This document serves as the **master index** for the organization's Supplier and Cloud Services Security framework, implementing ISO/IEC 27001:2022 Controls A.5.19 through A.5.23.

**Purpose**: Establish mandatory requirements for managing information security risks associated with external suppliers, contractual agreements, ICT supply chain dependencies, ongoing supplier relationship management, and cloud service lifecycle.

**Scope**: All supplier relationships involving access to organizational information or systems, all cloud services (IaaS, PaaS, SaaS, security services), all contractual agreements with external service providers, and all ICT products with supply chain dependencies.

**Framework Components**:
- **Policy Layer:** Governance documents defining requirements (7 documents: this index + 6 sections)
- **Assessment Layer:** Technical evaluation specifications (6 markdown specs including regulatory updates)
- **Implementation Layer:** Python-generated Excel workbooks (5 assessment workbooks)
- **Validation Layer:** Quality assurance scripts (reused from A.8.24)
- **Integration Layer:** Executive compliance dashboard

**Approach**: This framework uses a **vendor-neutral, system engineering methodology**. All assessments are generated via Python scripts to ensure consistency, repeatability, and maintainability across any cloud service provider configuration.

**Regulatory Context**: This framework addresses Swiss FADP, EU GDPR Article 28, and where applicable, DORA (financial sector), NIS2 (essential/important entities), EU AI Act, and US CLOUD Act jurisdictional considerations.

---

## Control Alignment

**ISO/IEC 27001:2022 Annex A.5.19-23 – Supplier and Cloud Services Security**

This policy framework provides organizational governance for five related controls covering the complete supplier and cloud service lifecycle:

### A.5.19 - Information Security in Supplier Relationships

> *Processes and procedures should be defined and agreed upon with suppliers to manage information security risks associated with the use of supplier's products or services.*

**Focus**: Foundational supplier security requirements, risk classification, due diligence processes.

### A.5.20 - Addressing Information Security in Supplier Agreements

> *Relevant information security requirements should be established and agreed upon with each supplier that may access, process, store, communicate or provide IT infrastructure components for the organization's information.*

**Focus**: Contractual security clauses, service level agreements, security terms and conditions.

### A.5.21 - Managing Information Security in the ICT Supply Chain

> *Processes and procedures should be defined and agreed upon with suppliers to manage information security risks associated with the information and communication technology (ICT) services and product supply chain.*

**Focus**: Sub-supplier requirements, component security, supply chain transparency.

### A.5.22 - Monitoring, Review and Change Management of Supplier Services

> *The organization should regularly monitor, review, evaluate and manage changes in supplier information security practices and service delivery.*

**Focus**: Review cycles, audit rights, change procedures, incident management, performance monitoring.

### A.5.23 - Information Security for Use of Cloud Services

> *Processes for acquisition, use, management and exit from cloud services should be established in accordance with the organization's information security requirements.*

**Focus**: Cloud-specific lifecycle (selection → implementation → operation → exit), shared responsibility model, data residency.

---

## 1. Framework Structure

### 1.1 Purpose

Establish mandatory requirements for managing information security risks associated with:

- External suppliers providing products or services
- Contractual agreements with suppliers
- ICT supply chain dependencies
- Ongoing supplier relationship management
- Cloud service acquisition, operation, and exit

### 1.2 Scope

This framework applies to:

- All supplier relationships involving access to organizational information or systems
- All cloud services (IaaS, PaaS, SaaS, XaaS models including security services, collaboration platforms, storage)
- All contractual agreements with external service providers
- All ICT products and services with supply chain dependencies
- All employees, contractors, and third parties managing supplier relationships

### 1.3 Exclusions

This framework does not cover:

- One-time purchases without ongoing service relationship or data access
- Suppliers with no access to organizational information assets
- Internal service providers (covered under separate HR/operational policies)

---

## 2. Policy Documents

### 2.1 Policy Structure

The supplier and cloud services security policy framework consists of the following modular documents:

| Document ID | Title | Lines | Primary Control(s) |
|-------------|-------|-------|--------------------|
| **ISMS-POL-A.5.19-23** | Master Index | ~800 | All (5.19-23) |
| **ISMS-POL-A.5.19-23-S1** | Supplier Relationship Fundamentals | ~250 | A.5.19 |
| **ISMS-POL-A.5.19-23-S2** | Supplier Agreement Requirements | ~300 | A.5.20 |
| **ISMS-POL-A.5.19-23-S3** | ICT Supply Chain Security | ~250 | A.5.21 |
| **ISMS-POL-A.5.19-23-S4** | Supplier Monitoring & Change Management | ~250 | A.5.22 |
| **ISMS-POL-A.5.19-23-S5** | Cloud Services Security | ~350 | A.5.23 |
| **ISMS-POL-A.5.19-23-S6** | Assessment Methodology & Automation | ~250 | All (5.19-23) |

**Total Policy Layer:** 7 documents, approximately 2,450 lines

**Design Philosophy**: Each document is independently versionable (maximum 250-400 lines) to enable granular change management, targeted stakeholder reviews, and clear audit trails.

### 2.2 Document Hierarchy

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
├── ISMS-IMP-A.5.23.4 (Ongoing Governance & Risk Management)
└── ISMS-IMP-A.5.23.5 (Compliance Monitoring Dashboard)
```

---

## 3. Assessment & Implementation Documents

### 3.1 Assessment Specifications (Markdown)

The framework includes **6 comprehensive assessment specifications** defining structure and requirements for Excel workbook generation:

| Document ID | Title | Purpose | Sheets |
|-------------|-------|---------|--------|
| **ISMS-IMP-A.5.23.0** | Regulatory Update Specification | DORA, NIS2, AI Act, CLOUD Act enhancements | N/A (spec) |
| **ISMS-IMP-A.5.23.1** | Cloud Service Inventory & Classification | Authoritative inventory with data classification and criticality | ~10 |
| **ISMS-IMP-A.5.23.2** | Vendor Due Diligence & Contracts | Due diligence criteria, contract security clauses | ~8 |
| **ISMS-IMP-A.5.23.3** | Secure Configuration & Deployment | Cloud service configuration baselines and deployment | ~8 |
| **ISMS-IMP-A.5.23.4** | Ongoing Governance & Risk Management | Monitoring, review cycles, incident management | ~8 |
| **ISMS-IMP-A.5.23.5** | Compliance Monitoring Dashboard | Executive summary with KPIs and trends | ~8 |

**Note**: ISMS-IMP-A.5.23.0 is a specification document for updating workbooks 1-5 with regulatory enhancements, not a standalone workbook.

### 3.2 Generated Excel Workbooks

When Python generators are executed, they produce:

| Workbook | Sheets | Primary Users | Purpose |
|----------|--------|---------------|---------|
| **ISMS-IMP-A.5.23.1_Cloud_Inventory_YYYYMMDD.xlsx** | ~10 | Procurement, Security, IT Ops | Service inventory, data classification, exit feasibility |
| **ISMS-IMP-A.5.23.2_Due_Diligence_YYYYMMDD.xlsx** | ~8 | Procurement, Legal, Security | Vendor evaluation, contract review, security clauses |
| **ISMS-IMP-A.5.23.3_Configuration_YYYYMMDD.xlsx** | ~8 | Cloud Architects, Security | Security configuration baselines, deployment compliance |
| **ISMS-IMP-A.5.23.4_Governance_YYYYMMDD.xlsx** | ~8 | IT Operations, Security | Ongoing monitoring, change management, incident tracking |
| **ISMS-IMP-A.5.23.5_Dashboard_YYYYMMDD.xlsx** | ~8 | CISO, Management | Consolidated KPIs, risk register, compliance metrics |

**Total Assessment Output:** ~42 sheets across 5 workbooks

### 3.3 Assessment Domains Explained

**Domain 0 - Regulatory Updates (Specification):**
- What regulatory frameworks apply? (DORA, NIS2, AI Act)
- What jurisdictional risks exist? (US CLOUD Act exposure)
- What additional fields are required? (concentration risk, data sovereignty)
- How do workbooks accommodate conditional compliance? (regulatory scope dropdowns)

**Domain 1 - Cloud Service Inventory & Classification:**
- What cloud services exist? (complete inventory: SaaS, IaaS, PaaS, security services)
- What data is processed? (classification: Public, Internal, Confidential, Restricted)
- What is service criticality? (business impact assessment)
- Where is data located? (residency: Switzerland, EU, USA, multi-region)
- What is exit feasibility? (portability, alternative vendors, transition cost)
- What regulatory scope applies? (DORA, NIS2, AI Act applicability per service)

**Domain 2 - Vendor Due Diligence & Contracts:**
- What due diligence was conducted? (certifications, audit reports, security questionnaires)
- What security clauses exist in contracts? (data protection, incident notification, audit rights)
- What are SLA commitments? (uptime, support response, breach notification timelines)
- What is provider jurisdiction? (headquarters, data centers, sub-processors)
- What is CLOUD Act exposure? (US-based providers, mitigation strategies)
- What exit provisions exist? (data export, transition assistance, termination clauses)

**Domain 3 - Secure Configuration & Deployment:**
- What configuration baselines apply? (CIS benchmarks, vendor hardening guides)
- What security controls are enabled? (encryption, MFA, network segmentation, logging)
- How is access managed? (least privilege, role-based access, privileged account monitoring)
- What monitoring is deployed? (security events, performance, compliance drift)
- What is shared responsibility division? (organization vs. provider controls)

**Domain 4 - Ongoing Governance & Risk Management:**
- What review schedule applies? (quarterly for high-risk, annual for low-risk)
- What performance metrics exist? (SLA compliance, incident frequency, support responsiveness)
- What incidents occurred? (security events, service disruptions, data breaches)
- What changes were approved? (configuration changes, contract amendments, migrations)
- What risks are tracked? (concentration risk, vendor lock-in, compliance gaps)

**Domain 5 - Compliance Monitoring Dashboard:**
- What is overall compliance status? (traffic light indicators per domain)
- What are key performance indicators? (service inventory completeness, contract coverage, configuration compliance)
- What gaps exist? (missing contracts, weak SLAs, configuration drift)
- What regulatory evidence exists? (DORA/NIS2 ICT register, AI Act documentation)
- What is the remediation roadmap? (prioritized action items, budget requirements)

### 3.4 Assessment Workflow

```
┌────────────────────────────────────────────────────────────┐
│ PHASE 1: GENERATION (Day 1)                                │
│ • Run 5 Python generator scripts                           │
│ • Output: 5 Excel workbooks with ~42 sheets total          │
│ • Validation: Run excel_sanity_check.py on each            │
│ • Quality: Run style_object_checker.py on each             │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ PHASE 2: ASSESSMENT (Weeks 1-3)                            │
│ • Procurement/IT/Security teams complete workbooks         │
│ • Fill yellow cells, use dropdown validations              │
│ • Document gaps, provide evidence (contracts, certs)       │
│ • Address regulatory fields if DORA/NIS2/AI Act applies    │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ PHASE 3: NORMALIZATION (Day 15)                            │
│ • Run normalize_assessment_files.py                        │
│ • Clean up filename chaos from review process              │
│ • Create audit trail manifest                              │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ PHASE 4: DASHBOARD (Day 16)                                │
│ • Generate compliance dashboard (workbook 5)               │
│ • Link to normalized assessment files                      │
│ • Auto-populate KPIs and compliance metrics                │
│ • Complete risk register and remediation roadmap           │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ PHASE 5: EXECUTIVE REVIEW (Week 4)                         │
│ • CISO reviews dashboard and risk register                 │
│ • Approve remediation roadmap and budget                   │
│ • Sign off on assessment package                           │
│ • Deliver to auditors (internal/external/regulatory)       │
└────────────────────────────────────────────────────────────┘
```

---

## 4. Automation Scripts

### 4.1 Assessment Generator Scripts

| Script | Output | Purpose |
|--------|--------|---------|
| `generate_a519_23_1_cloud_inventory.py` | ISMS-IMP-A.5.23.1 | Cloud service inventory and classification workbook |
| `generate_a519_23_2_due_diligence.py` | ISMS-IMP-A.5.23.2 | Vendor evaluation and contract review workbook |
| `generate_a519_23_3_configuration.py` | ISMS-IMP-A.5.23.3 | Secure configuration and deployment workbook |
| `generate_a519_23_4_governance.py` | ISMS-IMP-A.5.23.4 | Ongoing monitoring and risk management workbook |
| `generate_a519_23_5_dashboard.py` | ISMS-IMP-A.5.23.5 | Compliance monitoring dashboard |

**Regulatory Enhancement**: All generators incorporate fields from ISMS-IMP-A.5.23.0 specification for DORA, NIS2, AI Act, and CLOUD Act compliance.

### 4.2 Validation Scripts (Reused from A.8.24)

| Script | Purpose |
|--------|---------|
| `excel_sanity_check.py` | Generic workbook validator (sheet structure, formulas, data validation) |
| `style_object_checker.py` | Detect shared style objects that cause Excel repair warnings |
| `style_object_patcher.py` | Auto-fix style issues in generated workbooks |
| `normalize_assessment_files.py` | Normalize filenames for audit readiness |

**Script Quality Standards:**
- PEP 8 compliant Python code
- Error handling and graceful failures
- Comprehensive commenting (explain WHY, not just WHAT)
- Modular functions for reusability
- Validation of inputs and outputs
- Support for regulatory conditional logic (DORA/NIS2 fields shown only when applicable)

---

## 5. Roles & Responsibilities

### 5.1 Executive Roles

| Role | Responsibilities |
|------|------------------|
| **CISO** | Overall accountability, policy approval, exception sign-off, risk acceptance, budget approval |
| **Executive Management** | Strategic supplier decisions, budget allocation, risk governance |
| **Procurement Director** | Vendor selection, contract negotiation, cost management |
| **Legal Counsel** | Contract review, regulatory compliance, agreement terms, dispute resolution |

### 5.2 Operational Roles

| Role | Responsibilities |
|------|------------------|
| **Information Security Officer** | Policy ownership, enforcement, compliance monitoring, supplier risk assessment |
| **Procurement Team** | Supplier selection, RFP/RFQ management, vendor relationship management, contract administration |
| **IT Operations** | Technical implementation, configuration, monitoring, change management |
| **Cloud Architects** | Cloud service design, security configuration, architecture review |
| **System Owners** | Supplier relationships within their domains, business justification, budget approval |

### 5.3 Supporting Roles

| Role | Responsibilities |
|------|------------------|
| **Compliance & Audit** | Regulatory interpretation (DORA, NIS2, AI Act), audit support, evidence collection |
| **Risk Management** | Supplier risk assessment, concentration risk analysis, risk register maintenance |
| **Data Protection Officer (DPO)** | GDPR Article 28 compliance, data processing agreements, privacy impact assessments |
| **Security Engineering** | Assessment tool development, generator scripts, validation automation |
| **Finance** | Budget tracking, cost analysis, ROI assessment |

### 5.4 User Responsibilities

| Role | Responsibilities |
|------|------------------|
| **All Employees** | Adherence to approved cloud service list, prohibition on shadow IT, incident reporting |
| **Managers** | Budget approval for supplier services, business justification, user access management |

---

## 6. Assessment Methodology

### 6.1 System Engineering Approach

This framework employs **quantitative, evidence-based assessment** rather than checkbox compliance:

**Traditional Approach (Avoided):**
```
Auditor: "Do you manage supplier risks?"
Organization: "Yes, we have a vendor management process"
Auditor: [checks box]
Reality: Unknown supplier inventory, risk ratings, or contract compliance
```

**System Engineering Approach (Implemented):**
```
1. Run Python generator → produces standardized Excel workbook
2. Procurement/Security teams complete assessment with evidence
3. Validation scripts check for errors/issues
4. Normalization creates audit-ready filenames
5. Dashboard auto-aggregates compliance metrics
6. Quantitative results: "87% suppliers risk-assessed, 12 contracts missing 
   security clauses, 5 cloud services without exit plan, 3 DORA-critical 
   providers identified"
```

### 6.2 Vendor-Agnostic Design

**Policy Layer** (ISMS-POL-A.5.19-23): Defines *what* must be accomplished using generic capability requirements. No specific cloud providers mentioned.

**Implementation Layer** (ISMS-IMP-A.5.23): Defines *how* requirements are met in organizational context. Cloud-specific guidance provided as examples (AWS, Azure, GCP, Salesforce, etc.), not mandates.

**Benefits:**
- Policy remains stable across provider changes
- Organizations can use any cloud services that meet security requirements
- Audit focuses on capability outcomes, not vendor selection
- Implementation flexibility without policy revision
- Reduces vendor lock-in risk

**Example**:
- **Generic Requirement** (Policy): "Organizations SHALL conduct due diligence on cloud service providers including review of certifications, audit reports, and security questionnaires"
- **Vendor-Specific Implementation** (Examples): AWS Artifact for compliance reports, Azure Trust Center for certifications, Google Cloud Security & Privacy documentation

### 6.3 Response Values

Assessment checklists use standardized response values:

| Value | Meaning | Action Required |
|-------|---------|-----------------|
| `Yes` (✅ Compliant) | Fully implemented and documented | Maintain, provide evidence |
| `No` (❌ Non-Compliant) | Not implemented | Remediate or document exception |
| `Partial` (⚠️ Partial) | Partially implemented | Improvement plan required |
| `Planned` | Scheduled for implementation | Provide target date |
| `N/A` | Not applicable | Justify why (e.g., service not used, regulation not applicable) |

**Note:** "Maybe" is not a valid response. Uncertainty must be resolved before assessment completion.

### 6.4 Assessment Cycle

**Frequency:**
- **High-Risk Suppliers/Cloud Services**: Quarterly assessment
- **Medium-Risk**: Semi-annual assessment
- **Low-Risk**: Annual assessment
- **Triggered Reviews**: Upon contract renewal, major incident, regulatory change, or technology migration

**Quarterly Cycle:**
1. **Week 1:** Generate assessment workbooks, distribute to Procurement/IT Operations/Security
2. **Weeks 2-3:** Teams complete assessments, provide evidence (contracts, certifications, audit reports, SLA metrics)
3. **Week 4:** Security team reviews, validates, identifies gaps (missing contracts, expired certifications, weak SLAs)
4. **Week 5:** Dashboard generation, executive briefing, remediation planning
5. **Week 6:** Remediation initiation (contract amendments, provider audits, service migration), tracking

### 6.5 Regulatory Conditional Logic

**DORA (Financial Sector) Applicability:**
- If organization is EU financial entity → Complete DORA-specific fields:
  - ICT third-party risk register
  - Concentration risk assessment for critical providers
  - Exit plan testing documentation
  - Sub-contracting chain transparency

**NIS2 (Essential/Important Entities) Applicability:**
- If organization is NIS2 essential/important entity → Complete NIS2-specific fields:
  - Supply chain security measures
  - Incident notification procedures (24h, 72h, final report)
  - Management body accountability documentation

**EU AI Act Applicability:**
- If organization provides/deploys AI systems → Complete AI Act-specific fields:
  - AI risk classification (minimal, limited, high, unacceptable)
  - Transparency requirements (user disclosure)
  - High-risk system documentation (data governance, accuracy, human oversight)

**US CLOUD Act Considerations:**
- For all cloud services → Assess CLOUD Act exposure:
  - Provider headquarters jurisdiction
  - Data processing locations
  - Mitigation strategies (EU data boundary, encryption, contractual protections)
  - Risk acceptance documentation

---

## 7. Control Integration Matrix

### 7.1 How Controls Work Together

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

### 7.2 Shared Responsibility Model

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

## 8. Integration with ISMS

### 8.1 Related Controls

Supplier and cloud services security integrates with multiple ISO 27001 controls:

| Control | Integration Point |
|---------|-------------------|
| **A.5.1** | Policies - Supplier/cloud policy is part of ISMS policy suite |
| **A.5.9** | Inventory - Supplier/cloud services tracked in asset inventory |
| **A.5.12** | Classification - Data classification drives supplier security requirements |
| **A.5.24-5.28** | Incident Management - Supplier incident notification and response |
| **A.5.30** | Business Continuity - Supplier disruption scenarios, alternative providers |
| **A.8.8** | Vulnerability Management - Supplier patching commitments, vulnerability disclosure |
| **A.8.10** | Information Deletion - Supplier data deletion verification upon exit |
| **A.8.24** | Cryptography - Encryption requirements for suppliers, key management |
| **Clause 6.1** | Risk Assessment - Supplier risks in organizational risk register |

### 8.2 Bidirectional Data Flows

**Supplier/Cloud Management → Other Controls:**
- Supplier incidents → Incident management (A.5.24-28)
- Cloud service inventory → Asset inventory (A.5.9)
- Supplier vulnerabilities → Vulnerability management (A.8.8)
- Cloud data classification → Information classification (A.5.12)
- Supplier disruptions → Business continuity (A.5.30)

**Other Controls → Supplier/Cloud Management:**
- Risk assessments → Supplier risk classification (A.5.19)
- Incident lessons learned → Contract amendments (A.5.20, A.5.22)
- Vulnerability findings → Supplier patch requirements (A.5.22)
- BCP testing → Alternative supplier identification (A.5.23)

### 8.3 Risk Management Integration

**Risk Treatment:**
- Supplier/cloud security controls as risk mitigation (access controls, encryption, monitoring)
- Residual risks from supplier dependencies tracked in risk register
- Risk assessment feeds supplier selection and contract requirements

**Risk Register:**
- Supplier/cloud risks documented in compliance dashboard (Domain 5)
- Risk categories: Concentration risk, vendor lock-in, data sovereignty, regulatory exposure
- Risk scores drive remediation urgency and budget allocation
- Exception risks monitored quarterly and reported to CISO

**Concentration Risk Assessment (DORA Requirement):**
- Critical suppliers with >20% organizational dependency
- Alternative provider feasibility analysis
- Diversification strategy and timeline
- Board-level reporting for critical dependencies

---

## 9. Compliance & Audit

### 9.1 Mandatory Requirements

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

### 9.2 Audit Evidence

Auditors should expect the following evidence:

**Policy Documentation:**
- Complete policy framework (ISMS-POL-A.5.19-23 and subsections S1-S6)
- Approval records (CISO, Executive Management, Legal, Procurement Director)
- Distribution records (training acknowledgments, policy portal access logs)

**Implementation Evidence:**
- Completed assessment workbooks (5 Excel files)
- Normalized filenames with audit manifest
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

### 9.3 Audit Approach

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

---

## 10. Policy Maintenance

### 10.1 Review Schedule

**Annual Review:** Comprehensive review of all policy sections (recommended Q4)

**Triggered Reviews:** Major events requiring immediate policy review:
- **Significant regulatory changes**: DORA technical standards, NIS2 implementing acts, AI Act delegated acts
- **Major supplier security incidents**: Data breaches, service disruptions >24h, supply chain compromises
- **Cloud service provider changes**: Mergers/acquisitions, major migrations, service discontinuation
- **Organizational M&A activity**: New subsidiaries, divestitures, business unit changes
- **New cloud service categories adopted**: Emerging technologies (AI/ML platforms, quantum-safe cryptography)
- **Audit findings requiring policy updates**: External audit, regulatory audit, internal audit critical findings

### 10.2 Version Control

**Major Version (X.0):** Structural changes, new controls added, regulatory requirements, scope expansion  
**Minor Version (X.Y):** Content updates, clarifications, additions without structural change

**Master Framework Versioning:**
- This master document version reflects overall framework state
- Individual section versions (S1-S6) may increment independently
- Major framework changes require master document version update and re-approval

### 10.3 Change Process

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

### 10.4 Communication

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

## 11. Reference Documents

### 11.1 Internal Documents

**Policy Layer:**
- ISMS-POL-A.5.19-23 (this document) + Sections S1 through S6

**Assessment Layer:**
- ISMS-IMP-A.5.23.0 – Regulatory Update Specification (DORA/NIS2/AI Act/CLOUD Act) (Markdown)
- ISMS-IMP-A.5.23.1 – Cloud Service Inventory & Classification (Markdown + Excel)
- ISMS-IMP-A.5.23.2 – Vendor Due Diligence & Contracts (Markdown + Excel)
- ISMS-IMP-A.5.23.3 – Secure Configuration & Deployment (Markdown + Excel)
- ISMS-IMP-A.5.23.4 – Ongoing Governance & Risk Management (Markdown + Excel)
- ISMS-IMP-A.5.23.5 – Compliance Monitoring Dashboard (Markdown + Excel)

**Automation Layer:**
- Generator Scripts (5 Python files)
- Validation Scripts (4 Python files, reused from A.8.24)

**Related ISMS Policies:**
- ISMS Information Security Policy (parent policy)
- ISMS Risk Assessment Methodology
- ISMS Asset Management Policy
- ISMS-POL-A.5.12 - Classification of Information
- ISMS-POL-A.8.24 - Use of Cryptography
- ISMS-POL-A.5.24-28 - Information Security Incident Management
- ISMS Incident Management Procedure
- ISMS Business Continuity Plan
- ISMS-POL-A.5.30 - ICT Readiness for Business Continuity

### 11.2 External Standards & Regulations

**International Standards:**
- ISO/IEC 27001:2022 – Information Security Management Systems
- ISO/IEC 27002:2022 – Information Security Controls (Controls 5.19-5.23 guidance)
- ISO/IEC 27005:2022 – Information Security Risk Management
- ISO/IEC 27036-1:2021 – Information security for supplier relationships (Overview and concepts)
- ISO/IEC 27036-2:2022 – Requirements
- ISO/IEC 27036-3:2023 – ICT supply chain security
- ISO/IEC 27036-4:2016 – Cloud services
- ISO/IEC 27017:2015 – Cloud security controls
- ISO/IEC 27018:2019 – Cloud privacy (PII protection)

**Cloud Frameworks:**
- CSA CCM (Cloud Controls Matrix) v4.0
- CSA STAR (Security, Trust, Assurance, and Risk)
- NIST SP 800-144 – Guidelines on Security and Privacy in Public Cloud Computing
- NIST SP 800-146 – Cloud Computing Synopsis and Recommendations
- NIST SP 800-171 – Protecting CUI in Non-Federal Systems (for US government contracts)
- Shared Responsibility Model (CSP-specific: AWS, Azure, GCP documentation)

**Regulatory:**
- **Swiss Federal Act on Data Protection (FADP/nDSG)**: Art. 9 (Processor obligations)
- **EU GDPR**: Article 28 (Processor agreements), Article 44-50 (International transfers)
- **DORA** (Regulation EU 2022/2554): Digital Operational Resilience Act
  - Chapter V - ICT Third-Party Risk (Articles 28-31)
  - EBA/ESMA/EIOPA Guidelines and Technical Standards
- **NIS2 Directive** (Directive EU 2022/2555): Network and Information Security
  - Article 21 - Cybersecurity risk management
  - Annex - Supply chain security measures
- **EU AI Act** (Regulation EU 2024/1689): Artificial Intelligence Act
  - Title III - High-Risk AI Systems
  - Article 16 - Obligations of providers of high-risk AI systems
- **US CLOUD Act**: Clarifying Lawful Overseas Use of Data Act
  - 18 U.S.C. § 2713 - Required preservation and disclosure of communications
- **Schrems II** (CJEU C-311/18): Data protection for EU-US transfers

**Industry Guidelines:**
- Cloud Security Alliance – Cloud Controls Matrix
- Cloud Security Alliance – Security Guidance v5.0
- ENISA – Cloud Computing Risk Assessment
- NIST Cybersecurity Framework (CSF) v2.0
- CIS Controls v8 - Cloud Security Controls

### 11.3 Applicability of Regulatory Frameworks

References to standards, frameworks, and regulations throughout this policy are categorized as follows:

#### Mandatory Compliance (All Organizations)

| Framework | Applicability |
|-----------|---------------|
| **Swiss Federal Act on Data Protection (nFADP)** | All processing of personal data |
| **EU GDPR** | Where processing EU resident data |
| **ISO/IEC 27001:2022** | Full ISMS scope |

#### Sector-Specific Regulations (Conditional)

| Framework | Applicability | Relevance to Suppliers/Cloud |
|-----------|---------------|------------------------------|
| **DORA** (Digital Operational Resilience Act) | Financial sector entities in EU (credit institutions, payment institutions, investment firms, etc.) | ICT third-party risk management (Art. 28-31), exit strategies, concentration risk, mandatory ICT register |
| **NIS2** (Network and Information Security Directive 2) | Essential/important entities in EU (energy, transport, health, digital infrastructure, etc.) | Supply chain security, incident reporting (24h/72h/final), management accountability, security measures |
| **EU AI Act** | Organizations deploying/providing AI systems in EU | AI service providers (high-risk systems), deployers (transparency, human oversight), prohibited practices |

**Enhanced Requirements for DORA/NIS2 Entities:**

Organizations subject to DORA or NIS2 have **mandatory additional requirements**:

**DORA-Specific:**
- Maintain ICT third-party risk register (Article 28.2)
- Contractual provisions for:
  - Full cooperation with competent authorities (access, inspection)
  - Audit rights (on-site and remote)
  - Exit strategies (data portability, transition assistance)
- Concentration risk assessment for critical ICT third-party providers
- Sub-outsourcing register and approval process
- Key contractual provisions pre-approval by competent authority (critical providers)

**NIS2-Specific:**
- Supply chain security measures (Article 21.2(e))
- Policies on acquisition, development, and maintenance of ICT systems
- Incident notification to authorities:
  - Early warning (24 hours after becoming aware)
  - Incident notification (72 hours)
  - Final report (1 month, or upon authority request)
- Management body accountability and training
- Annual cybersecurity risk management report

#### Data Sovereignty & Cross-Border Considerations

| Framework | Impact on Cloud Services |
|-----------|--------------------------|
| **US CLOUD Act** | US-headquartered providers may be compelled to disclose data regardless of storage location. Assess provider HQ jurisdiction. |
| **EU Data Boundary Initiatives** | Some providers offer EU-only data processing guarantees (e.g., AWS European Sovereign Cloud, Azure EU Data Boundary). Verify contractual commitments. |
| **Swiss-US Data Privacy Framework** | Adequacy mechanism for US transfers (replaced Privacy Shield). Verify provider participation at https://www.dataprivacyframework.gov/list |
| **Schrems II Implications** | Additional safeguards required for non-adequate country transfers: Transfer Impact Assessment (TIA), supplementary measures (encryption, contractual clauses). |

**Guidance for Cloud Provider Selection - Jurisdictional Risk Assessment:**

When selecting cloud providers, organizations must document assessment of:

| Risk Factor | Assessment Criteria |
|-------------|---------------------|
| **Provider headquarters jurisdiction** | US CLOUD Act exposure assessment. US-based providers subject to CLOUD Act data disclosure orders. |
| **Data processing locations** | Regulatory alignment with data residency requirements (FADP, GDPR Art. 44-50, NIS2, DORA). |
| **Sub-processor locations** | Downstream jurisdictional exposure. Review sub-processor list for non-adequate countries. |
| **Contractual commitments** | Provider's legal challenge commitments (resist unlawful disclosure orders, notify customer). |
| **Technical measures** | Encryption (data-at-rest, data-in-transit), customer-controlled key management, access controls (geo-fencing, IP restrictions). |

Organizations handling **Confidential** or **Restricted** data should:
1. Document jurisdictional risk assessment for each cloud service
2. Implement compensating controls (encryption, key management, access restrictions)
3. Obtain risk acceptance from CISO for residual risks
4. Review annually or upon regulatory/geopolitical changes

#### Informational Reference / Best Practice Alignment

| Framework | Usage |
|-----------|-------|
| **NIST SP 800-series** | Technical guidance and control selection (informational) |
| **CIS Controls** | Benchmark for security configurations (best practice) |
| **CSA CCM** | Cloud-specific control mapping (framework alignment) |
| **OWASP** | Application security guidance (development practices) |

These frameworks inform security practices but do not constitute mandatory compliance requirements unless explicitly required by contract or regulation.

#### United States Federal Requirements

References to United States federal frameworks and regulations (including, but not limited to, FISMA, FIPS, FedRAMP, NIST cybersecurity requirements, CMMC) apply **only** where the organization:

- Acts as contractor, subcontractor, or service provider to US federal agencies
- Provides services to customers subject to such regulations
- Has explicit contractual obligations requiring such compliance

In all other cases, these references are provided for informational or technical alignment purposes only and do not constitute mandatory compliance requirements.

#### Supplier Compliance Evaluation Matrix

When evaluating supplier compliance, use this framework:

| Supplier Location | Primary Framework | Additional Considerations |
|-------------------|-------------------|---------------------------|
| **Switzerland** | nFADP, ISO 27001 | Verify ISO 27001 certification, Art. 9 processor agreement |
| **EU/EEA** | GDPR, ISO 27001 | Article 28 processor agreement, sub-processor disclosure, DORA/NIS2 if financial/essential entity |
| **United States** | Contractual requirements, SOC 2 Type II | CLOUD Act assessment, adequacy mechanisms (Swiss-US DPF, EU-US DPF), supplementary measures |
| **Other** | Risk-based assessment | Transfer Impact Assessment (TIA), adequacy decision, Standard Contractual Clauses (SCCs), supplementary measures |

---

## Appendix A: Philosophy & Methodology

### A.1 Trust, But Verify — And Document the Verification

> "Trust, but verify — and document the verification."

This framework prevents **cargo cult supplier management** — the practice of:
- Accepting supplier self-attestations without independent verification
- Signing contracts without reading security clauses (or understanding their enforceability)
- Selecting cloud services based on marketing materials instead of security assessment
- Assuming "ISO 27001 certified" automatically means "secure for our specific use case"
- Treating vendor questionnaires as compliance proof rather than starting points for due diligence

**The assessment workbooks force specificity and evidence:**

- **What** suppliers exist? (Complete inventory with risk ratings: Critical, High, Medium, Low)
- **What** security clauses are in contracts? (Clause-by-clause verification with evidence location)
- **What** cloud services are used? (Service classification, data types, criticality, exit feasibility)
- **How** are suppliers monitored? (Review schedules, incident tracking, performance metrics, change management)
- **Where** is data processed? (Jurisdictional assessment, CLOUD Act exposure, adequacy mechanisms)
- **Proof** of compliance? (Certifications with expiry tracking, audit reports, SLA metrics, incident statistics)

If these questions cannot be answered with quantitative evidence and audit trails, the organization does not have supplier risk management — it has supplier risk management **theater**.

### A.2 Cloud Is Still Someone Else's Computer

> "There is no cloud — it's just someone else's computer."

Cloud services don't eliminate security responsibilities — they **shift and redistribute** them according to the shared responsibility model. Organizations that treat cloud adoption as "outsourcing security" fundamentally misunderstand the model.

**Shared Responsibility Reality Check:**

- **IaaS (Infrastructure as a Service)**: Organization responsible for OS patching, application security, data protection, network configuration, identity management, encryption.
- **PaaS (Platform as a Service)**: Organization responsible for application code security, data protection, access controls, identity management.
- **SaaS (Software as a Service)**: Organization responsible for user access management, data classification, configuration security, integration security.

**Shared responsibility is NOT equal responsibility.** Cloud providers secure the infrastructure; organizations secure what they put on that infrastructure.

**Critical Organizational Responsibilities That Cannot Be Outsourced:**

1. **Data Classification**: Provider doesn't know which data is Confidential vs. Public — organization must classify
2. **Access Control**: Provider provides IAM tools — organization must configure least privilege
3. **Incident Response**: Provider may notify of infrastructure issues — organization must respond to data/application incidents
4. **Compliance**: Provider may offer compliance certifications — organization must map to their regulatory requirements
5. **Exit Planning**: Provider may offer data export — organization must test export completeness and format compatibility

### A.3 Exit Planning Is Security Planning

> "If you can't exit, you don't control your security posture — your vendor does."

The ability to exit a cloud service is a **security control**, not just a business continuity consideration. Vendor lock-in creates:
- **Security debt**: Cannot migrate away from provider even if security deteriorates
- **Compliance risk**: Cannot meet regulatory requirements if provider changes terms
- **Negotiation weakness**: Provider knows switching cost is prohibitive
- **Concentration risk**: Critical dependency on single provider (DORA Article 28 concern)

**Every cloud service must have documented and tested exit strategy appropriate to its criticality and risk profile.**

---

#### A.3.1 Three Exit Strategy Options

Exit strategies must consider three primary transition paths, selected based on service criticality, regulatory requirements, workload characteristics, and total cost of ownership:

**1. Cloud-to-Cloud Migration (Default Strategy - 90%+ of Services)**

Migration to alternative cloud provider is the **primary exit strategy** for most services.

**When Optimal:**
- Service is cloud-native (containers, serverless, managed services)
- Workload has variable/unpredictable demand
- No regulatory mandate for physical on-premises hosting
- Organization lacks on-premises infrastructure capacity
- Cloud TCO remains favorable over 3-5 year horizon

**Key Requirements:**
- Alternative providers identified and evaluated (2+ options)
- Data export format compatibility verified
- Migration timeline estimated (typically 3-6 months)
- Annual proof-of-concept testing (DORA Article 28.6)

**Cost Profile**: CAPEX: None | OPEX: Ongoing cloud fees | 5-Year TCO: CHF 250K-2.5M+

---

**2. Hybrid Cloud Transition (Selective Strategy - 5-10% of Services)**

Partial repatriation maintaining some workloads in cloud while moving selected components to on-premises infrastructure.

**When Optimal:**
- Regulatory requirements mandate some on-premises data storage (data sovereignty)
- Specific workloads have extreme latency sensitivity (<10ms requirements)
- Workload characteristics support segmentation (stateless app vs. stateful database)
- Gradual transition strategy preferred (spread cost/risk over 12-24 months)
- Organization has existing on-premises capacity with available headroom

**Key Requirements:**
- Workload placement decision framework (which components cloud vs. on-prem)
- Hybrid connectivity architecture (VPN, Direct Connect, ExpressRoute)
- Data synchronization requirements documented
- Cross-platform management and security controls

**Cost Profile**: CAPEX: CHF 95K-700K | OPEX: CHF 80K-300K/year | 5-Year TCO: CHF 335K-1.6M

---

**3. On-Premises Repatriation (Reserved Strategy - <5% of Services)**

Complete migration from cloud to organization-owned infrastructure. This is the **highest-risk, highest-cost** exit strategy.

**When Justified (ONLY):**
- **Regulatory mandate**: Legal requirement for physically controlled, air-gapped infrastructure
- **Cost inversion**: Cloud costs >CHF 500K/year AND stable workload (no burst) AND 5-year on-prem TCO <70% of cloud
- **Strategic independence**: Critical infrastructure requiring zero external dependencies (defense, critical infrastructure)
- **Concentration risk**: DORA Article 28.9 diversification from critical ICT third-party provider

**Key Requirements:**
- Comprehensive TCO analysis (3-5 year horizon)
- Infrastructure capacity planning (compute, storage, network, facilities)
- Staffing requirements (3-10 FTEs for infrastructure operations)
- Technology refresh budget (3-5 year hardware lifecycle)
- Timeline assessment (typically 9-18 months)

**Cost Profile**: CAPEX: CHF 390K-990K | OPEX: CHF 470K-1.11M/year | 5-Year TCO: CHF 2.94M-7.04M

**⚠️ CRITICAL**: On-premises repatriation is economically justified in <5% of cloud exit scenarios. For most workloads, cloud-to-cloud or hybrid models offer superior TCO, faster timelines, and maintained elasticity.

---

#### A.3.2 Exit Strategy Decision Framework

**Quick Decision Tree:**
```
Regulatory mandate for on-prem?
├─ YES → On-Premises or Hybrid
└─ NO → Annual cloud cost >CHF 500K AND stable workload?
    ├─ YES → Run TCO analysis → On-prem TCO <70% of cloud?
    │   ├─ YES → On-Premises or Hybrid
    │   └─ NO → Cloud-to-Cloud (Default)
    └─ NO → Cloud-to-Cloud (Default)
```

**Recommendation Priority (90-5-5 Rule):**
- **Cloud-to-Cloud**: 90%+ of services (cost, speed, elasticity, innovation)
- **Hybrid**: 5-10% of services (regulatory compliance, latency, cost optimization)
- **On-Premises**: <5% of services (regulatory mandate, extreme cost inversion, strategic independence)

**Detailed guidance on exit strategy selection, cost comparisons, and implementation requirements: See ISMS-POL-A.5.19-23-S5 Section 8.1.1**

---

#### A.3.3 Common Exit Planning Elements (All Strategies)

Regardless of exit strategy chosen, all cloud services must document:

**1. Data Export Procedures**:
   - Export format (structured? proprietary? open standard?)
   - Completeness (all data? historical data? metadata? audit logs?)
   - Timeline (hours? days? weeks?)
   - Automation (API-based? manual? bulk export tools?)
   - Validation (integrity checks, completeness verification)

**2. Configuration Backup and Portability**:
   - Infrastructure-as-Code (Terraform, CloudFormation, ARM templates)
   - Configuration backups (security policies, network rules, IAM policies)
   - Portability assessment (vendor-neutral vs. proprietary constructs)
   - Documentation (architecture diagrams, dependency maps)

**3. Transition Plan to Alternative**:
   - Alternative provider/architecture identified and evaluated
   - Cost estimation (migration effort, new contracts, training)
   - Timeline estimation (realistic migration duration)
   - Risk assessment (data loss, downtime, functionality gaps)
   - Rollback procedures (if migration fails)

**4. Contract Termination Clauses**:
   - Termination for convenience (notice period, penalties)
   - Termination for cause (security breach, SLA violations)
   - Data deletion verification (certification of deletion, timeline)
   - Transition assistance (provider support during migration, documentation access)

**5. Exit Plan Testing**:
   - **Annual testing requirement** (DORA Article 28.6): Export subset of data, verify format and completeness
   - **Alternative provider proof-of-concept**: Deploy critical workload on alternative provider annually (cloud-to-cloud strategy)
   - **Hybrid connectivity testing**: Validate data synchronization, failover procedures (hybrid strategy)
   - **Cost updates**: Re-assess migration cost annually (provider pricing changes, new alternatives)

**Testing exit plans annually isn't paranoia — it's due diligence and regulatory compliance (DORA Article 28.6).**

---

#### A.3.4 Integration with Business Continuity & Disaster Recovery

**Distinction:**

| Scenario Type | Planning Framework | Timeline | Example |
|---------------|-------------------|----------|---------|
| **Planned Exit** (Voluntary) | This policy (A.5.23) | 3-18 months | Contract renegotiation failure, cost optimization, strategic change |
| **Emergency Failover** (Involuntary) | BC/DR (A.8.13-14-5.30) | Hours-Days | Provider outage, security breach, geopolitical access loss, bankruptcy |

For emergency scenarios involving cloud provider total failure (bankruptcy, catastrophic breach, geopolitical access loss), refer to Business Continuity and Disaster Recovery planning (ISMS-POL-A.8.13-14-5.30) for:
- Provider failure response procedures
- Emergency on-premises recovery capabilities
- Alternative provider hot-standby configurations
- Data recovery from backup/DR sites

**DORA Article 28.6**: Exit strategies shall consider both planned transitions and emergency scenarios requiring immediate service continuity.

---

#### A.3.5 Exit Strategy Myths vs. Reality

**Myth 1: "We'll exit to on-prem if cloud gets too expensive"**

**Reality**: On-prem repatriation typically costs 2-3x more than cloud over 5 years for most workloads due to:
- Capital expenditure (CHF 390K-990K initial investment)
- Staffing (3-10 FTEs @ CHF 300K-600K/year)
- Technology refresh cycles (every 3-5 years)
- Lost elasticity (fixed capacity = over-provisioning waste)

Cloud-to-cloud migration to cheaper provider is almost always more economical.

---

**Myth 2: "Exit planning is only needed for critical services"**

**Reality**: **All** cloud services need exit plans. The depth varies by criticality:
- **Critical**: Full exit simulation, annual testing, hot standby alternative
- **High**: Significant sample testing, documented migration plan
- **Medium**: Representative sample testing, cost/timeline estimates
- **Low**: Export capability verification, documentation only

ISO 27001:2022 Control A.5.23 mandates exit planning for **all** cloud services, not just critical ones.

---

**Myth 3: "ISO 27001 certification means the provider is secure"**

**Reality**: ISO 27001 certification means the provider has a documented ISMS, not that their service is appropriate for your risk profile or that exit will be painless.

Exit planning forces you to understand:
- What data can you extract, in what format, how long does it take?
- Can you migrate to alternative provider without functionality loss?
- What's the true cost of switching (not just cloud bill, but migration effort)?

If you can't answer these questions, you don't have exit planning — you have exit planning **theater**.

---

**Myth 4: "Multi-cloud eliminates exit risk"**

**Reality**: Multi-cloud reduces **concentration risk** but introduces **complexity cost**:
- Multiple skill sets required
- Integration between clouds (networking, IAM, monitoring)
- Inconsistent security controls across platforms
- Higher operational overhead

Multi-cloud is justified for:
- ✅ Critical services requiring provider-level redundancy
- ✅ Geographically distributed workloads (latency optimization)
- ✅ Regulatory diversification (DORA concentration risk)

Multi-cloud is **not** justified for:
- ❌ Speculative "what if we need to exit someday" without specific exit triggers
- ❌ Resume-driven engineering ("everyone's doing multi-cloud")
- ❌ Simple workloads with clear single-provider optimal solution

**Proper exit planning with provider-neutral architecture matters more than multi-cloud deployment.**

---

#### A.3.6 Exit Planning Checklist

For each cloud service, confirm:

- [ ] Exit strategy selected (Cloud-to-Cloud / Hybrid / On-Premises) with documented justification
- [ ] Alternative providers identified (minimum 2 for critical services)
- [ ] Data export capability verified (format, completeness, timeline)
- [ ] Configuration backup strategy documented (IaC, API configs)
- [ ] Migration cost estimated (effort, timeline, risk)
- [ ] Contract termination clauses reviewed (notice period, data deletion, transition assistance)
- [ ] Exit plan tested annually (data export, alternative PoC, cost update)
- [ ] Evidence retained (test results, cost quotes, timeline estimates)
- [ ] Integration with BC/DR documented (emergency failover procedures)
- [ ] Risk acceptance obtained for residual exit risks

**Documentation**: Record exit planning details in:
- **ISMS-IMP-A.5.23.4** (Governance & Risk Management workbook) - "Exit Strategy" sheet
- **ISMS-IMP-A.5.23.5** (Compliance Monitoring Dashboard workbook) - "Exit Planning" sheet

**The cheapest insurance is the insurance you buy before you need it. Exit planning is that insurance.**

---

### A.4 Concentration Risk Is Underestimated Risk

> "Diversification is the only free lunch in investing — and in cloud services."

Organizations tend to consolidate cloud services with single providers for:
- Volume discounts (enterprise agreements)
- Integration convenience (single pane of glass)
- Skill consolidation (one platform to train on)

**But concentration risk creates systemic vulnerabilities:**

- **Provider Outage**: AWS US-EAST-1 outage affects multiple services simultaneously
- **Security Breach**: Provider compromise affects all services at once
- **Price Increases**: Monopolistic pricing when switching is prohibitive
- **Regulatory Changes**: Provider changes terms to comply with foreign jurisdiction (e.g., CLOUD Act disclosure)
- **Acquisition**: Provider acquired by competitor or foreign entity

**DORA Article 28.9 explicitly requires concentration risk assessment for critical ICT third-party providers.**

**Mitigation Strategies:**

1. **Multi-Cloud Architecture** (where feasible):
   - Critical workloads: Primary cloud + standby alternative
   - Non-critical workloads: Distributed across providers
   - Data replication: Cross-provider backup

2. **Provider Criticality Assessment**:
   - If provider failure causes >20% business impact → **Critical dependency**
   - Document alternative providers and migration feasibility
   - Test failover to alternative provider annually

3. **Exit Plan Investment**:
   - Budget for exit testing (time, resources, alternative provider costs)
   - Treat exit planning as continuous process, not one-time assessment
   - Update exit plans when provider changes services/terms/pricing

**The cheapest insurance is the insurance you buy before you need it.**

---

**END OF MASTER DOCUMENT**