# ISMS-POL-A.5.9-S1
## Inventory of Information and Assets - Purpose, Scope, Definitions

**Document ID**: ISMS-POL-A.5.9-S1  
**Title**: Inventory of Information and Assets - Purpose, Scope, Definitions  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial foundational document |

**Review Cycle**: Annual (aligned with ISMS policy review cycle)  
**Next Review Date**: 10.01.2027  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Information Security Manager
- Business Review: Business Unit Leaders
- Compliance Review: Legal/Compliance Officer

**Distribution**: ISMS stakeholders, asset owners, IT management, audit team  
**Related Documents**: ISMS-POL-A.5.9 (Master), ISO/IEC 27001:2022 A.5.9

---

## 1.1 Purpose and Control Alignment

### 1.1.1 ISO/IEC 27001:2022 Control Requirement

This policy implements ISO/IEC 27001:2022 Annex A Control 5.9:

> **A.5.9 Inventory of Information and Other Associated Assets**
>
> **Control**  
> *An inventory of information and other associated assets, including owners, should be created and maintained.*
>
> **Purpose**  
> *To identify the organization's information and other associated assets in order to maintain their information security and assign appropriate responsibilities.*

**Control Type**: Preventive  
**Information Security Properties**: Confidentiality, Integrity, Availability  
**Cybersecurity Concepts**: Identify, Protect  
**Operational Capabilities**: Asset Management  
**Security Domains**: Governance and Ecosystem

### 1.1.2 Policy Objective

This document establishes the foundational requirements for [Organization]'s information and asset inventory framework. The policy aims to:

**From an Implementer Perspective:**
- Provide systematic methodology for identifying and documenting all information and associated assets
- Enable [Organization] to know WHAT assets exist, WHERE they are located, and WHO is responsible
- Create foundation for risk-based security decisions and resource allocation
- Support operational processes including change management, incident response, and business continuity

**From an Auditor Perspective:**
- Enable objective verification that [Organization] knows what assets it must protect
- Provide evidence that accountability is assigned and accepted for each asset
- Demonstrate that inventory is maintained with defined accuracy and currency standards
- Support compliance verification for asset-related controls (A.5.10-5.18, A.8.x series)

### 1.1.3 Business Value and Security Rationale

**Why Asset Inventory Matters:**

An accurate, current inventory of information and associated assets is foundational to information security because:

1. **You Cannot Protect What You Don't Know Exists**: Security controls can only be applied to identified assets. Unknown assets create blind spots.

2. **Risk Management Requires Context**: Risk assessment depends on knowing what assets exist, their value, and their interdependencies.

3. **Accountability Requires Ownership**: Without assigned owners, no one is accountable for asset protection decisions.

4. **Incident Response Needs Scope**: When incidents occur, responders must quickly identify affected assets and their business impact.

5. **Compliance Demands Evidence**: Auditors and regulators require demonstration that [Organization] knows what it must protect.

6. **Change Management Requires Baseline**: You cannot assess change impact without knowing what exists today.

**Anti-Pattern: Cargo Cult Inventory**

This policy explicitly rejects "checkbox compliance" approaches where organizations create inventories solely to satisfy auditors without genuine operational use. A properly implemented asset inventory is a *living operational tool*, not a static compliance document.

### 1.1.4 Integration with ISMS Framework

This control integrates with [Organization]'s Information Security Management System as follows:

**ISMS Clause Integration:**
- **Clause 4 (Context)**: Asset inventory informs understanding of organizational context
- **Clause 6 (Risk Management)**: Inventory provides input to risk assessment process
- **Clause 8 (Operations)**: Inventory supports operational security processes
- **Clause 9 (Performance)**: Inventory completeness is measurable performance indicator

**Control Integration**: See Section 1.4.2 for detailed integration with related Annex A controls.

---

## 1.2 Scope

### 1.2.1 Assets In Scope

This policy applies to ALL information and associated assets owned, operated, custodied, or contractually responsible to [Organization], regardless of:

- Physical location (on-premises, cloud, remote, third-party facilities)
- Ownership model (owned, leased, licensed, managed service)
- Lifecycle stage (active, development, test, archive, end-of-life)
- Asset value (critical systems through commodity equipment)
- Management responsibility (internal, outsourced, co-managed)

**Information Assets:**

All information in any format that has value to [Organization], including but not limited to:
- **Structured data**: Databases, data warehouses, data lakes, registries
- **Unstructured data**: Documents, spreadsheets, presentations, reports
- **Records**: Legal documents, financial records, personnel files, contracts
- **Intellectual property**: Source code, designs, algorithms, trade secrets, patents
- **Configuration data**: System configurations, network parameters, security policies
- **Authentication data**: Passwords, certificates, keys, tokens, biometric templates
- **Communication records**: Email archives, chat logs, meeting recordings
- **Business intelligence**: Reports, analytics, dashboards, KPIs

**Associated Assets - Technical/IT Infrastructure:**

Physical and virtual technology assets that process, store, or transmit information:
- **Compute resources**: Physical servers, virtual machines, containers, serverless functions
- **Network infrastructure**: Routers, switches, firewalls, load balancers, wireless access points
- **Storage systems**: SAN/NAS, object storage, backup systems, removable media
- **Endpoints**: Workstations, laptops, tablets, smartphones, specialized terminals
- **Operational technology**: Industrial control systems, IoT devices, building systems
- **Supporting infrastructure**: Power systems (UPS, generators), cooling, physical security systems

**Associated Assets - Applications and Services:**

Software and services that process organizational information:
- **Business applications**: ERP, CRM, HRMS, financial systems, collaboration platforms
- **Infrastructure services**: Directory services, DNS, DHCP, time synchronization, monitoring
- **Development tools**: IDEs, CI/CD pipelines, code repositories, testing frameworks
- **Cloud services**: SaaS applications, PaaS platforms, managed services
- **APIs and integrations**: RESTful APIs, web services, microservices, data feeds

**Associated Assets - Physical:**

Physical assets beyond IT infrastructure:
- **Facilities**: Data centers, offices, storage rooms, secure areas
- **Physical media**: Backup tapes, external drives, optical media, paper documents
- **Equipment**: Printers, scanners, copiers, fax machines, specialized equipment
- **Physical security assets**: Locks, safes, access control systems, surveillance systems

**Associated Assets - Personnel and Organizational:**

Critical human assets and organizational capabilities:
- **Key personnel**: Individuals with specialized knowledge, critical roles, or privileged access
- **Competencies**: Specialized skills, certifications, domain expertise
- **Organizational knowledge**: Processes, procedures, institutional knowledge, relationships
- **Third-party dependencies**: Key vendors, service providers, partners

### 1.2.2 Special Considerations for Dynamic and Ephemeral Assets

**Challenge: Short-Lived Assets**

Modern IT environments include assets with lifecycles measured in minutes or hours (e.g., auto-scaling cloud instances, containers, serverless function executions, temporary development environments). Inventorying such assets at the instance level may be impractical or impossible.

**Approach:**

For assets with short lifecycles or high churn rates, [Organization] may inventory at a higher abstraction level, provided the inventory captures:

1. **Service/Template Definition**: What type of asset is being instantiated?
2. **Data Processed**: What information does the service handle?
3. **Security Controls**: What protections apply to the service?
4. **Owner Accountability**: Who is accountable for the service?
5. **Instance Tracking Mechanism**: How are active instances identified if needed?

**Examples:**
- **Auto-scaling Web Tier**: Inventory the "web application service" with its template, not individual VM instances
- **Container Platform**: Inventory the container orchestration platform and container images, not individual running containers
- **Serverless Functions**: Inventory the function definitions and their data access patterns
- **Development Environments**: Inventory the provisioning system and standard configurations

**Evidence Requirement**: [Organization] must demonstrate that the chosen abstraction level provides sufficient visibility for security management while remaining maintainable.

### 1.2.3 Inventory Granularity

**Principle**: Inventory granularity should balance completeness with maintainability.

[Organization] determines appropriate granularity for each asset category based on:
- **Asset criticality**: Higher criticality → more detailed inventory
- **Information classification**: Higher classification → more detailed inventory  
- **Risk assessment**: Higher risk → more detailed inventory
- **Operational needs**: What level of detail supports actual decision-making?
- **Maintenance burden**: Can this level of detail be realistically maintained?

**Examples of Granularity Decisions:**

| Asset Type | Could Inventory As... | Granularity Decision |
|------------|----------------------|---------------------|
| Database System | Single asset OR individual databases OR individual tables | Based on data classification and criticality |
| File Server | Single server OR shared folders OR individual files | Typically folder level for shared data |
| Application Suite | Single suite OR individual modules OR sub-components | Based on independent operation and data access |
| Network Infrastructure | Single network OR segments/VLANs OR individual devices | Typically segment + critical devices |

**Mandatory Minimum**: At a minimum, [Organization] must inventory at a level that enables:
- Identification of asset owners
- Application of security controls based on information classification
- Impact assessment during incidents
- Risk identification and assessment

### 1.2.4 Assets Out of Scope

The following are explicitly excluded from inventory requirements:

**Temporary Test Data**: Purely synthetic test data with no production information content (however, test systems that store or process real data ARE in scope)

**Public Information**: Information explicitly designated for public release with no confidentiality requirements (however, the systems hosting public information ARE in scope as associated assets)

**Personal Employee-Owned Devices**: Employee-owned devices not used for organizational business (BYOD devices used for business ARE in scope)

### 1.2.5 Applicability

**Geographic Scope**: Worldwide - all locations where [Organization] operates

**Organizational Scope**: All business units, departments, subsidiaries, and controlled entities

**User Scope**: This policy applies to:
- All employees (permanent, temporary, contract)
- Asset owners and custodians
- IT personnel and system administrators
- Third-party service providers with asset management responsibilities
- Auditors and assessors (for verification purposes)

---

## 1.3 Key Definitions

### 1.3.1 Information Asset

**Definition**: Information in any format (digital, physical, oral) that has value to [Organization] and requires protection to maintain its confidentiality, integrity, or availability.

**Characteristics**:
- Represents knowledge, data, or intellectual property
- May exist in multiple locations or formats simultaneously
- Value may be intrinsic (e.g., customer data) or contextual (e.g., competitive advantage)
- Subject to classification based on sensitivity (see A.5.12)

**Examples**: Customer database, financial records, source code, employee personnel files, encryption keys, business plans

**Relationship to Other Definitions**: Information assets are carried by, processed by, stored in, or transmitted through *associated assets*.

### 1.3.2 Associated Asset

**Definition**: Physical, technical, or organizational asset that processes, stores, transmits, or protects information assets.

**Categories**:

**Technical Assets**: Servers, network devices, storage systems, endpoints, applications, cloud services

**Physical Assets**: Facilities, physical media, equipment, physical security systems

**Organizational Assets**: Personnel competencies, processes, third-party relationships

**Characteristics**:
- Enables creation, processing, storage, transmission, or protection of information
- May support multiple information assets simultaneously
- Has measurable attributes (location, configuration, capacity, etc.)
- May have dependencies on other associated assets

**Examples**: Database server (technical), backup tape (physical), network engineer with specialized BGP knowledge (organizational)

### 1.3.3 Asset Owner

**Definition**: Individual or group with approved accountability and authority for an asset throughout its lifecycle, including responsibility for:

- Ensuring asset is inventoried
- Determining asset classification
- Defining acceptable use requirements
- Approving access to the asset
- Ensuring appropriate security controls are applied
- Reviewing asset classification and controls periodically
- Participating in risk management for the asset
- Authorizing changes to the asset
- Authorizing asset disposal or retirement

**Key Principle: Accountability Cannot Be Delegated**

While asset owners may delegate *tasks* to custodians or administrators, they retain *accountability* for the asset. If something goes wrong, the owner is answerable.

**Characteristics**:
- Typically a business role, not IT role (for information assets)
- Must have authority to make decisions about the asset
- Must understand the business value and risk context
- Single owner per asset (no shared ownership to avoid diffusion of responsibility)
- Owner assignment is mandatory, not optional

**Examples**: 
- Customer database → Customer Service Director (owns the information)
- Financial reports → Chief Financial Officer
- HR information system → Human Resources Director

### 1.3.4 Asset Custodian

**Definition**: Individual or group with delegated day-to-day responsibility for implementing and maintaining security controls for an asset, acting under the authority and direction of the asset owner.

**Responsibilities** (typical, may vary):
- Implementing technical security controls
- Performing backups and recovery testing
- Applying patches and updates
- Monitoring asset health and security
- Responding to security events
- Maintaining asset documentation
- Executing owner-approved changes

**Characteristics**:
- Typically an IT or operations role
- Has day-to-day management responsibility
- Operates under owner's direction and approval
- May be custodian for many assets
- Custodian role does not eliminate owner accountability

**Examples**:
- Database Administrator (custodian) for customer database (owned by Customer Service Director)
- Network Engineer (custodian) for network infrastructure (owned by CIO)

**Owner vs. Custodian Analogy**: Owner is like property owner, custodian is like property manager.

### 1.3.5 Inventory

**Definition**: Structured, documented record of assets with defined attributes maintained to support asset management, security management, and compliance verification.

**Required Characteristics**:
- **Accurate**: Reflects actual asset state, not desired state
- **Current**: Updated within defined timeframes after asset changes
- **Consistent**: Aligned with other organizational inventories (CMDB, financial asset register, etc.)
- **Complete**: Captures all in-scope assets per section 1.2
- **Accessible**: Available to those with legitimate need (owners, custodians, auditors, incident responders)
- **Attributable**: Each entry identifies responsible parties

**Format Considerations**:
- May be single system or multiple coordinated systems
- May use dedicated CMDB/asset management tools or alternative appropriate systems
- May combine automated discovery with manual documentation
- Must support querying and reporting for management and audit purposes

**Not Required to Be**: A single spreadsheet or document (see ISO guidance - inventory "need not be a single list")

### 1.3.6 Asset Classification

**Definition**: Designation of an asset's sensitivity level based on the confidentiality, integrity, and availability requirements of the information it contains or processes.

**Relationship to A.5.12**: Asset classification follows [Organization]'s information classification scheme established under Control A.5.12 (Classification of Information). Associated assets inherit classification based on the highest classification of information they process.

**Purpose in Context of A.5.9**:
- Classification is a required inventory attribute
- Drives security control selection
- Influences risk assessment
- Determines access control requirements
- Informs incident response priorities

**Note**: Detailed classification scheme is defined in ISMS-POL-A.5.12. This policy requires that classification be assigned and documented in the inventory.

### 1.3.7 Asset Lifecycle

**Definition**: The sequential stages an asset progresses through from identification/acquisition to disposal/retirement.

**Typical Lifecycle Stages**:

1. **Identification/Acquisition**: Asset need identified, asset acquired or created
2. **Registration**: Asset added to inventory, owner assigned
3. **Active Use**: Asset in operational production or active development
4. **Maintenance**: Updates, modifications, configuration changes
5. **Review**: Periodic assessment of asset value, classification, controls
6. **Archive/Decommission**: Asset no longer in active use but retained
7. **Disposal/Retirement**: Asset permanently removed from organization
8. **Inventory Removal**: Asset record archived or removed from active inventory

**Lifecycle Variation**: Not all assets follow identical lifecycle stages. [Organization] defines appropriate lifecycle stages for different asset categories.

**Inventory Integration**: Asset lifecycle stage is a required inventory attribute, enabling [Organization] to:
- Identify assets approaching end-of-life
- Ensure appropriate controls for each lifecycle stage
- Plan for asset replacement or retirement
- Verify disposal procedures were followed

---

## 1.4 References

### 1.4.1 ISO/IEC Standards

**Primary Standards:**
- **ISO/IEC 27001:2022** - Information Security Management Systems - Requirements (Annex A.5.9)
- **ISO/IEC 27002:2022** - Information Security Controls (Section 5.9 - Inventory of Information and Other Associated Assets)

**Asset Management Standards:**
- **ISO/IEC 19770-1** - Information Technology - IT Asset Management - Part 1: IT Asset Management Systems - Requirements
- **ISO 55001** - Asset Management - Management Systems - Requirements

**Related Security Standards:**
- **ISO/IEC 27005** - Information Security Risk Management (asset identification in risk management)

### 1.4.2 Related Organizational Policies

This policy framework should be read in conjunction with:

**Directly Integrated Controls:**
- **ISMS-POL-A.5.10** - Acceptable Use of Information and Other Associated Assets (acceptable use rules apply to inventoried assets)
- **ISMS-POL-A.5.11** - Return of Assets (return verification against inventory)
- **ISMS-POL-A.5.12** - Classification of Information (classification scheme applied to inventory)
- **ISMS-POL-A.5.13** - Labeling of Information (labels reference inventory classification)
- **ISMS-POL-A.5.15** - Access Control (access rules based on inventoried assets)
- **ISMS-POL-A.5.18** - Access Rights (rights assigned per asset ownership)

**Supporting Technical Controls:**
- **ISMS-POL-A.8.8** - Management of Technical Vulnerabilities (vulnerabilities tracked per asset)
- **ISMS-POL-A.8.9** - Configuration Management (configuration items are inventoried assets)
- **ISMS-POL-A.8.10** - Information Deletion (deletion removes from inventory)
- **ISMS-POL-A.8.19** - Installation of Software on Operational Systems (software assets in inventory)

**ISMS Process Integration:**
- **Risk Management Process** - Asset inventory provides risk assessment input
- **Change Management Process** - Changes trigger inventory updates
- **Incident Management Process** - Incidents reference affected inventory assets
- **Business Continuity Management** - Critical assets identified from inventory

### 1.4.3 External Frameworks and Guidance

**NIST (National Institute of Standards and Technology):**
- **NIST SP 800-53** - Security and Privacy Controls:
  - CM-8: System Component Inventory
  - PM-5: System Inventory
- **NIST Cybersecurity Framework**: ID.AM (Asset Management) category

**CIS (Center for Internet Security):**
- **CIS Controls v8**:
  - Control 1: Inventory and Control of Enterprise Assets
  - Control 2: Inventory and Control of Software Assets

**COBIT 2019:**
- **BAI09** - Managed Assets
- **DSS05** - Managed Security Services (asset inventory for security)

**ITIL (IT Infrastructure Library):**
- **Service Asset and Configuration Management (SACM)**: CMDB integration guidance

### 1.4.4 Regulatory and Compliance Considerations

[Organization] should consider applicable regulations that mandate asset inventories or related requirements:

**Examples** (applicability varies by organization):
- **GDPR (EU)**: Processing activity records require identification of data processing systems
- **Swiss Federal Data Protection Act (FADP)**: Similar requirements for data processing transparency
- **PCI-DSS** (if applicable): Requirement 2.4 - Maintain inventory of system components in scope
- **HIPAA** (if applicable): Administrative safeguards require hardware and software inventory
- **SOX** (if applicable): IT general controls include asset management

**Note**: Specific regulatory applicability depends on [Organization]'s industry, geography, and operations. Compliance team should assess applicable requirements.

---

## 1.5 Document Structure and Navigation

This document (S1) is part of a comprehensive policy framework for Control A.5.9:

**Policy Framework Components:**

- **ISMS-POL-A.5.9** - Master policy index and executive summary
- **ISMS-POL-A.5.9-S1** - Purpose, Scope, Definitions [THIS DOCUMENT]
- **ISMS-POL-A.5.9-S2** - Requirements Framework (what must be inventoried and how)
- **ISMS-POL-A.5.9-S3** - Implementation and Assessment (how to implement and verify)
- **ISMS-POL-A.5.9-S4** - Roles, Responsibilities, and Governance (who does what)

**Implementation Guidance:**

- **ISMS-IMP-A.5.9-1** - Asset Identification and Discovery Procedures
- **ISMS-IMP-A.5.9-2** - Inventory Structure and Maintenance
- **ISMS-IMP-A.5.9-3** - Assessment Specifications

**Assessment Tools:**

- Excel workbook generators for systematic assessment (50_scripts-excel/)
- Compliance dashboard for executive oversight

**Reading Sequence**:

1. Start with **ISMS-POL-A.5.9** (master index) for overview
2. Read **S1** (this document) for foundational understanding
3. Review **S2** for specific requirements
4. Consult **S3** for implementation approach
5. Reference **S4** for roles and governance
6. Use **IMP documents** for practical implementation guidance

---

## 1.6 Key Principles Summary

**Principle 1: Know Your Assets**
You cannot protect what you don't know exists. Systematic identification and documentation is foundational to security.

**Principle 2: Ownership is Mandatory**
Every asset must have an identified, accountable owner. No exceptions.

**Principle 3: Inventory is a Living System**
Inventory is not a one-time compliance exercise. It must be maintained as assets change.

**Principle 4: Balance Detail with Maintainability**
Inventory granularity should support decision-making without creating unsustainable maintenance burden.

**Principle 5: Integration Over Duplication**
Leverage existing systems (CMDB, financial asset registers) rather than creating redundant inventories.

**Principle 6: Evidence-Based Compliance**
Inventory completeness and accuracy must be objectively verifiable, not assumed.

**Principle 7: Don't Fool Yourself**
Following Feynman's principle, [Organization] must honestly assess whether inventory is complete and current, not just claim it is.

---

**END OF SECTION 1 (S1)**

**Next Document**: ISMS-POL-A.5.9-S2 - Requirements Framework

---

*"The first principle is that you must not fool yourself — and you are the easiest person to fool."*  
— Richard Feynman

**Document Status**: Ready for review and approval  
**Estimated Reading Time**: 15-20 minutes  
**Target Audience**: Asset owners, ISMS stakeholders, audit team, management