# ISMS-POL-A.5.9 – Inventory of Information and Assets

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Inventory of Information and Assets |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.9 |
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
| 1.0 | [Date] | CISO | Initial consolidated policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.10 through A.5.18 (Asset Management Controls)
- ISMS-POL-A.8.x (Technical Controls)
- ISMS-IMP-A.5.9 (Implementation Guidance Suite)
- ISO/IEC 27001:2022 Control A.5.9

---

## Executive Summary

This policy establishes [Organization]'s requirements for maintaining an inventory of information and associated assets in accordance with ISO/IEC 27001:2022 Control A.5.9.

**The Fundamental Principle**: You cannot protect what you do not know you have. Asset inventory is the foundation upon which all other security controls depend - risk assessment, access control, classification, vulnerability management, incident response, and business continuity planning.

**Scope**: This policy applies to all information assets (data, content, intellectual property) and associated assets (IT infrastructure, applications, physical facilities, personnel competencies) within [Organization]'s information security management scope. The policy establishes WHAT must be inventoried, WHO is accountable, and HOW compliance is verified.

**Purpose**: Define organizational requirements for asset inventory creation, maintenance, and governance. This policy establishes the governance framework (WHAT and WHY). Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.9 suite, and assessment tools provide objective verification mechanisms.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS, FINMA, DORA, NIS2, HIPAA) apply where [Organization]'s business activities trigger applicability.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control A.5.9

**ISO/IEC 27001:2022 Annex A.5.9 - Inventory of Information and Other Associated Assets**

> *An inventory of information and other associated assets, including owners, should be created and maintained.*

**Control Objective (ISO/IEC 27002:2022)**: To identify the organization's information and other associated assets in order to maintain their information security and assign appropriate responsibilities.

**Control Type**: Organizational  
**Information Security Properties**: Confidentiality, Integrity, Availability  
**Cybersecurity Concepts**: Identify  
**Operational Capabilities**: Asset Management  
**Security Domains**: Governance and Ecosystem

**This Policy Addresses**:
- Information asset identification and classification requirements
- Associated asset inventory requirements (IT, physical, personnel)
- Asset ownership assignment and accountability framework
- Inventory accuracy, completeness, and currency standards
- Organizational roles and responsibilities for asset management
- Integration with other ISMS controls and organizational systems
- Assessment methodology and compliance verification

### 1.2 What This Policy Does

This policy:
- **Defines** what constitutes an information asset and associated asset requiring inventory
- **Establishes** mandatory attributes for inventory records (owner, classification, location, etc.)
- **Specifies** ownership assignment requirements and owner accountability
- **Sets** accuracy, completeness, and currency standards for inventory maintenance
- **Identifies** organizational roles and responsibilities for asset inventory
- **References** applicable regulatory requirements per ISMS-POL-00

### 1.3 What This Policy Does NOT Do

This policy does NOT:
- **Specify technical implementation details** (see ISMS-IMP-A.5.9 Implementation Guides)
- **Define inventory tool selection** (technology decisions based on [Organization]'s needs)
- **Provide detailed discovery procedures** (see ISMS-IMP-A.5.9-1 Asset Identification)
- **Describe maintenance workflows** (see ISMS-IMP-A.5.9-2 Inventory Maintenance)
- **Replace risk assessment** (inventory provides input to risk assessment process)

**Rationale**: Separating policy requirements from implementation guidance enables:
- Policy stability despite organizational changes
- Technical agility for tool and process updates without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Adaptability to different organizational contexts and risk profiles

### 1.4 Scope

**This policy applies to**:
- All information assets within [Organization]'s ISMS scope (databases, documents, records, IP, configuration data)
- All IT infrastructure supporting information processing (servers, storage, networking, endpoints)
- All applications and software (business applications, SaaS services, development tools)
- All physical assets supporting information security (facilities, media, equipment)
- All personnel assets critical to operations (key roles, specialized competencies)
- All third-party services processing [Organization]'s information

**In Scope Asset Categories**:

1. **Information Assets**: Any data, content, or knowledge with value to [Organization]
   - Structured data (databases, data warehouses)
   - Unstructured documents (files, emails, reports)
   - Records and archives (regulatory retention)
   - Intellectual property (trade secrets, patents, designs)
   - Configuration and parameters (system configurations)
   - Authentication and cryptographic materials (keys, certificates, credentials)

2. **Associated Assets - IT Infrastructure**: Systems that process, store, or transmit information
   - Physical servers and virtual machines
   - Storage systems and backup infrastructure
   - Network infrastructure (routers, switches, firewalls, load balancers)
   - Endpoints (workstations, laptops, mobile devices)
   - Cloud infrastructure and services

3. **Associated Assets - Applications**: Software that processes information
   - Business applications (ERP, CRM, financial systems)
   - SaaS and cloud services
   - Custom developed applications
   - Development tools and CI/CD pipelines
   - APIs and integration platforms

4. **Associated Assets - Physical**: Tangible resources supporting operations
   - Facilities and data centers
   - Removable media (USB drives, backup tapes, portable drives)
   - Physical security equipment (access control, surveillance)
   - Paper documents and printed materials

5. **Associated Assets - Personnel**: Human resources and competencies
   - Key personnel roles (critical to operations)
   - Specialized competencies (unique skills, certifications)
   - NOT individual person records (privacy compliance)

**Out of Scope**:
- Assets owned by third parties (unless processing [Organization]'s information)
- Personal devices not used for [Organization] work (unless BYOD policy applies)
- Public information with no confidentiality, integrity, or availability requirements
- Commodity office supplies with no security impact

### 1.5 Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance** (applies to all [Organization] operations):
- **Swiss nDSG (Art. 8)**: Personal data security requires knowing what data exists and where
- **EU GDPR (Art. 5, 32)**: Data protection by design requires documented data inventory
- **ISO/IEC 27001:2022 (Control A.5.9)**: Explicit control requirement for certification

**Tier 2: Conditional Applicability** (triggered by specific business activities):
- **PCI DSS (Req. 2.4, 12.5)**: Inventory of system components in cardholder data environment
- **HIPAA (164.310(d)(1))**: Inventory and asset controls for healthcare information systems
- **FINMA**: Risk-based asset inventory requirements for Swiss financial institutions
- **DORA/NIS2**: ICT asset inventory for critical infrastructure and financial entities
- **SOX**: IT general controls require documented system inventory for financial reporting
- **Industry-specific regulations**: May require specialized asset categorization

**Tier 3: Informational Reference** (best practices, not legally binding):
- **ISO/IEC 19770-1**: IT Asset Management systems requirements
- **ISO 55001**: Asset Management - Management systems requirements
- **NIST SP 800-53 (CM-8, PM-5)**: System component and inventory controls
- **CIS Controls (1, 2)**: Inventory and Control of Enterprise Assets and Software
- **COBIT 2019 (BAI09)**: Managed Assets framework

**United States Federal Requirements**: References to US federal frameworks (FISMA, FIPS, FedRAMP, NIST cybersecurity requirements) apply only where [Organization] has explicit US federal contractual obligations, as defined in ISMS-POL-00.

For complete regulatory categorization and applicability determination methodology, refer to ISMS-POL-00.

---

## 2. Requirements Framework

### 2.1 Asset Inventory Creation

**Requirement A.5.9-R1**: [Organization] SHALL maintain an inventory of information and associated assets.

**Mandatory Coverage**:
- All information assets within ISMS scope (databases, documents, IP, configurations)
- All IT infrastructure processing information (servers, storage, networking, endpoints)
- All applications and services (business apps, SaaS, APIs, development tools)
- All physical assets supporting security (facilities, media, equipment)
- All personnel assets critical to operations (key roles, competencies)

**Implementation Approach**: [Organization] determines appropriate inventory structure based on risk assessment. Inventory may consist of multiple specialized inventories (CMDB for IT, HRIS for personnel, document repositories) provided they collectively satisfy control requirements.

**Verification Method**: Completeness assessment per ISMS-IMP-A.5.9-3 (Quality & Compliance Assessment).

### 2.2 Asset Categorization

**Requirement A.5.9-R2**: [Organization] SHALL categorize assets to enable appropriate security control application.

**Categorization Dimensions**:

1. **By Asset Type** (primary categorization):
   - Information Assets (what needs protection)
   - IT Infrastructure (systems processing information)
   - Applications (software processing information)
   - Physical Assets (tangible resources)
   - Personnel Assets (competencies and roles)

2. **By Criticality** (for risk-based treatment):
   - Critical: Loss would cause severe business impact (operational disruption, regulatory breach)
   - High: Loss would cause significant business impact (financial loss, reputational damage)
   - Medium: Loss would cause moderate business impact (efficiency reduction, customer inconvenience)
   - Low: Loss would cause minimal business impact (minor inconvenience, easily replaceable)

3. **By Lifecycle State** (for maintenance planning):
   - Active: In production use
   - Development: Being developed or tested
   - Maintenance: Scheduled for updates or patches
   - Retired: Scheduled for decommissioning
   - Archived: Retained for compliance but not actively used

**Decision Support**: Annex A provides categorization decision framework and examples.

**Verification Method**: Category assignments reviewed during asset owner acknowledgment process per ISMS-IMP-A.5.9-4 (Owner Accountability Assessment).

### 2.3 Mandatory Inventory Attributes

**Requirement A.5.9-R3**: [Organization] SHALL document mandatory attributes for each inventoried asset.

**Core Attributes** (required for all assets):

| Attribute | Description | Purpose | Verification |
|-----------|-------------|---------|--------------|
| **Asset ID** | Unique identifier | Traceability across systems | Automatic (system-generated) |
| **Asset Name** | Human-readable name | Communication and reporting | Owner verification |
| **Asset Type** | Category per 2.2 | Control applicability | Category validation |
| **Owner** | Accountable individual | Responsibility assignment | Owner acknowledgment |
| **Custodian** | Day-to-day manager (may differ from owner) | Operational responsibility | Custodian acknowledgment |
| **Description** | Purpose and function | Understanding and context | Owner verification |
| **Location** | Physical or logical location | Asset tracking, data residency | Physical verification |
| **Status** | Lifecycle state per 2.2 | Maintenance planning | Status workflow |
| **Criticality** | Business impact per 2.2 | Risk prioritization | Risk assessment alignment |
| **Created Date** | Acquisition/creation date | Asset age tracking | Documentation verification |
| **Last Updated** | Record last modified | Currency tracking | Automatic timestamp |
| **Last Reviewed** | Owner last reviewed record | Accuracy assurance | Owner attestation |
| **Next Review Date** | Scheduled review | Proactive maintenance | Review schedule |

**Information Asset Specific Attributes**:

| Attribute | Description | Purpose |
|-----------|-------------|---------|
| **Data Classification** | Confidentiality/integrity/availability level per A.5.12 | Security control selection |
| **Data Format** | File format, schema, structure | Technical compatibility |
| **Storage Location(s)** | Where data physically resides | Data residency compliance |
| **Retention Period** | Legal/business retention requirement | Compliance, storage planning |
| **Legal/Regulatory Requirements** | Applicable regulations | Compliance tracking |
| **Related Systems** | Systems accessing this information | Dependency analysis |
| **Encryption Status** | At rest, in transit, or both | Cryptographic protection verification |

**IT Infrastructure Specific Attributes**:

| Attribute | Description | Purpose |
|-----------|-------------|---------|
| **Manufacturer/Vendor** | Producer of asset | Support contracts, compatibility |
| **Model/Version** | Specific product version | Patch management, EOL tracking |
| **Serial Number/Asset Tag** | Physical identifier | Physical asset verification |
| **IP Address/Hostname** | Network identifier | Network management |
| **Configuration Baseline** | Standard configuration reference | Configuration management (A.8.9) |
| **Dependencies** | Required assets for operation | Impact assessment |
| **Supported Information** | Information assets it processes | Classification inheritance |

**Optional Attributes**: [Organization] may extend inventory with additional attributes based on operational needs (purchase cost, warranty dates, energy consumption, compliance certifications) provided they do not create excessive maintenance burden.

**Verification Method**: Attribute completeness checked per ISMS-IMP-A.5.9-3 (Quality & Compliance Assessment).

### 2.4 Asset Ownership

**Requirement A.5.9-R4**: [Organization] SHALL assign an owner to every inventoried asset.

**Ownership Principles**:
- **Universal Assignment**: Every asset MUST have an assigned owner (no exceptions)
- **Accountability**: Owner is accountable for asset throughout its lifecycle
- **Delegation Permitted**: Owner may delegate custodian responsibilities but retains accountability
- **Acknowledgment Required**: Owners must acknowledge ownership and responsibilities
- **Change Management**: Ownership changes trigger inventory update

**Owner Responsibilities**:
- Classify asset according to business value and risk
- Ensure appropriate security controls are applied
- Review inventory record accuracy at least annually
- Approve access requests to owned assets
- Report security incidents affecting owned assets
- Participate in asset lifecycle decisions (decommissioning, archival)
- Maintain awareness of regulatory requirements affecting owned assets

**When Ownership is Unclear**:
1. Escalate to appropriate management level
2. Document temporary ownership assignment
3. Set deadline for permanent owner determination (maximum 30 days)
4. No asset remains "unowned" beyond 30-day threshold

**Verification Method**: Owner assignment completeness (100% target) verified per ISMS-IMP-A.5.9-4 (Owner Accountability Assessment).

### 2.5 Inventory Quality Standards

**Requirement A.5.9-R5**: [Organization] SHALL maintain inventory quality through accuracy, completeness, and currency standards.

#### 2.5.1 Completeness

**Standard**: Inventory must include all assets within scope.

**Verification Approach**:
- Periodic discovery scans and reconciliation
- Cross-validation with other systems (CMDB, procurement, HR)
- Sample testing for missing assets
- Management attestation

**Acceptable Granularity**: Determined by asset criticality and risk. High-value/high-risk assets require detailed individual records. Low-risk commodity assets may be grouped (e.g., "standard employee laptops - quantity 50" vs. individual serial numbers).

**Target**: 95% completeness minimum for critical assets, 90% for standard assets.

#### 2.5.2 Accuracy

**Standard**: Inventory data must correctly reflect actual asset state.

**Verification Approach**:
- Regular reviews by asset owners (at least annually)
- Statistical sampling for data accuracy validation
- Automated validation where technically feasible
- Incident-based verification (inventory checked when incidents occur)

**Accuracy Targets**:
- Information Assets: 95% accuracy minimum
- IT Infrastructure: 98% accuracy minimum (more stable than information)
- Physical Assets: 90% accuracy minimum
- Personnel Assets: 100% accuracy (critical roles/competencies must be current)

#### 2.5.3 Currency

**Standard**: Inventory must reflect current state, not historical state.

**Update Triggers**:
- Asset creation (new acquisition, development)
- Asset modification (configuration change, relocation)
- Asset disposal (decommissioning, deletion)
- Ownership change
- Classification change
- Scheduled periodic review

**Maximum Staleness**:
- Critical assets: Real-time or daily updates
- High-risk assets: Updates within 3 business days
- Standard assets: Updates within 1 week
- Low-risk assets: Updates within 1 month
- All assets: Reviewed annually minimum

**Integration Requirement**: Asset inventory SHALL integrate with change management processes (changes trigger inventory updates automatically where technically feasible).

#### 2.5.4 Verification Schedule

| Asset Category | Review Frequency | Responsible Role | Verification Method |
|----------------|------------------|------------------|---------------------|
| Critical Information | Quarterly | Information Owner | Owner attestation + sampling |
| High-Risk IT Infrastructure | Quarterly | System Owner | Automated scan + manual verification |
| Standard Assets | Semi-annually | Asset Owner | Owner review + spot checks |
| Low-Risk Assets | Annually | Asset Owner | Owner attestation |
| All Personnel Assets | Quarterly | HR + Department Heads | HR system reconciliation |

**Verification Method**: Currency and accuracy metrics tracked per ISMS-IMP-A.5.9-3 (Quality & Compliance Assessment).

### 2.6 Integration Requirements

**Requirement A.5.9-R6**: [Organization] SHALL integrate asset inventory with other ISMS processes and organizational systems.

**Mandatory Integration Points**:

| ISMS Control/Process | Integration Requirement | Purpose |
|---------------------|------------------------|---------|
| **A.5.12 (Information Classification)** | Classification assigned to information assets | Security control selection |
| **A.5.13 (Labeling)** | Labels reference inventory classification | Visible security marking |
| **A.5.15 (Access Control)** | Access rules based on asset ownership and classification | Authorization decisions |
| **A.5.18 (Access Rights)** | Access rights approved by asset owners | Accountability enforcement |
| **A.8.x (Technical Controls)** | Technical controls protect inventoried assets | Control-asset mapping |
| **Risk Management (Clause 6)** | Inventory provides risk assessment input | Threat-asset-vulnerability identification |
| **Change Management** | Changes trigger inventory updates | Currency maintenance |
| **Incident Management** | Incidents reference affected assets | Impact assessment |
| **Business Continuity** | Critical asset identification for BCP/DRP | Prioritization |

**Organizational System Integration**:

| System | Integration Purpose | Synchronization |
|--------|-------------------|----------------|
| **CMDB (Configuration Management Database)** | IT asset inventory source | Bi-directional (where technically feasible) |
| **Procurement/Finance** | Asset acquisition tracking | Inbound (procurement → inventory) |
| **HR System** | Personnel asset validation | Inbound (HR → inventory for roles/competencies) |
| **Asset Management System** | Physical asset tracking | Bi-directional |
| **Document Management** | Information asset repository | Inbound (DMS → inventory metadata) |

**Verification Method**: Integration effectiveness assessed per ISMS-IMP-A.5.9-2 (Inventory Maintenance) and ISMS-IMP-A.5.9-3 (Quality & Compliance Assessment).

---

## 3. Governance & Compliance

### 3.1 Roles & Responsibilities

**3.1.1 Executive Management**

**Strategic Accountability**:
- Approve asset inventory policy and major changes
- Allocate resources for inventory implementation and maintenance
- Receive annual inventory compliance reports
- Ensure organizational culture supports asset accountability

**Specific Responsibilities**:
- Approve RACI matrix for asset inventory governance
- Resolve ownership disputes escalated from business unit level
- Approve exceptions to inventory requirements (rare, documented)

**3.1.2 Chief Information Security Officer (CISO)**

**Operational Accountability**:
- Own asset inventory policy and framework
- Define inventory requirements and quality standards
- Monitor compliance with inventory requirements
- Report inventory compliance status to Executive Management
- Coordinate with other control owners (Classification A.5.12, Access Control A.5.15)

**Specific Responsibilities**:
- Approve inventory categorization framework
- Define accuracy, completeness, currency targets
- Review and approve assessment findings
- Escalate significant gaps to Executive Management
- Maintain awareness of regulatory changes affecting inventory

**3.1.3 Information Security Manager**

**Tactical Implementation**:
- Implement asset inventory framework
- Conduct periodic inventory assessments
- Provide guidance to asset owners and custodians
- Track and report metrics (completeness, accuracy, owner assignment)
- Coordinate periodic reviews and validation activities

**Specific Responsibilities**:
- Generate assessment workbooks
- Facilitate owner acknowledgment process
- Conduct sampling and validation activities
- Maintain assessment evidence
- Prepare compliance reports for CISO

**3.1.4 IT Operations / Infrastructure Teams**

**IT Asset Management**:
- Maintain IT infrastructure inventory (servers, storage, networking, endpoints)
- Integrate inventory with CMDB
- Conduct automated discovery scans
- Update inventory for IT asset lifecycle events
- Support inventory validation and reconciliation

**Specific Responsibilities**:
- Configure and maintain discovery tools
- Update IT asset records within defined timeframes
- Provide technical accuracy verification
- Support incident investigations requiring asset information
- Coordinate with procurement for new asset onboarding

**3.1.5 Application Owners / System Owners**

**Application Asset Management**:
- Maintain application and system inventory
- Document application dependencies and information flows
- Classify applications per criticality framework
- Update inventory for application changes (versions, configurations, decommissions)
- Ensure application-to-information asset relationships documented

**Specific Responsibilities**:
- Review and validate application inventory accuracy
- Update application records within defined timeframes
- Participate in application risk assessments
- Document application-to-infrastructure dependencies
- Notify Security Team of application lifecycle changes

**3.1.6 Information Owners / Data Owners**

**Information Asset Ownership**:
- Own assigned information assets throughout lifecycle
- Classify information per A.5.12 (Information Classification)
- Review information asset inventory records at least annually
- Approve access to owned information
- Participate in information risk assessments
- Make retention and disposal decisions per A.8.10 (Information Deletion)

**Specific Responsibilities**:
- Acknowledge ownership formally
- Ensure information assets are accurately inventoried
- Report changes affecting owned information (location, classification, storage)
- Approve exceptions for owned information
- Participate in incident investigations

**3.1.7 Asset Custodians**

**Day-to-Day Asset Management**:
- Perform operational tasks delegated by asset owner
- Maintain asset availability and integrity
- Update inventory records for routine changes
- Report issues to asset owner
- Implement security controls as directed by owner

**Distinction**: Custodians have operational responsibility but accountability remains with owner.

**3.1.8 All Personnel**

**User Responsibilities**:
- Report lost, stolen, or damaged assets immediately
- Comply with acceptable use policies for assigned assets
- Notify IT Operations of asset changes (hardware, software)
- Return assets upon departure or role change
- Participate in periodic asset verification when requested

**3.1.9 Internal Audit / Compliance**

**Independent Verification**:
- Conduct independent inventory audits
- Verify compliance with policy requirements
- Test control effectiveness (accuracy, completeness, owner assignment)
- Report findings to Executive Management and CISO
- Recommend improvements to inventory framework

### 3.2 RACI Matrix

**Asset Inventory Governance**:

| Activity | Executive Mgmt | CISO | Info Security Mgr | IT Ops | App Owners | Info Owners | Custodians | All Users | Audit |
|----------|---------------|------|------------------|--------|------------|-------------|------------|-----------|-------|
| **Policy Approval** | A | R | C | I | I | I | I | I | C |
| **Framework Design** | I | A | R | C | C | C | I | I | C |
| **Asset Identification** | I | I | C | R | R | R | C | I | I |
| **Owner Assignment** | I | A | C | C | C | R | I | I | I |
| **Record Creation** | I | I | C | R | R | C | C | I | I |
| **Record Maintenance** | I | I | C | R | R | R | R | I | I |
| **Accuracy Review** | I | I | C | C | R | R | C | I | I |
| **Compliance Assessment** | I | A | R | C | C | C | I | I | C |
| **Gap Remediation** | C | A | R | R | R | R | C | I | I |
| **Reporting** | I | A | R | C | C | I | I | I | C |
| **Independent Audit** | I | I | C | I | I | I | I | I | A/R |
| **Exception Approval** | A | R | C | I | C | C | I | I | C |

**Legend**: R = Responsible (does the work), A = Accountable (final authority), C = Consulted (input sought), I = Informed (kept updated)

### 3.3 Assessment and Verification

**Requirement A.5.9-R7**: [Organization] SHALL conduct periodic assessments to verify inventory compliance.

**Assessment Framework** (5 domains):

| Assessment Domain | Document ID | Assessment Focus | Frequency |
|------------------|-------------|------------------|-----------|
| **Asset Identification & Discovery** | ISMS-IMP-A.5.9-1 | Discovery procedures, completeness | Quarterly |
| **Inventory Maintenance** | ISMS-IMP-A.5.9-2 | Structure, update procedures, integration | Quarterly |
| **Quality & Compliance** | ISMS-IMP-A.5.9-3 | Accuracy, completeness, currency verification | Quarterly |
| **Owner Accountability** | ISMS-IMP-A.5.9-4 | Owner assignment, acknowledgment, training | Quarterly |
| **Compliance Dashboard** | ISMS-IMP-A.5.9-5 | Executive summary, consolidated metrics | Quarterly |

**Assessment Tools**: Excel-based workbooks generated from Python scripts provide:
- Structured data collection
- Automated compliance calculations
- Gap identification
- Evidence registers
- Trend tracking

**Implementation Note**: Detailed assessment specifications, user guides, and Python script generators are documented in ISMS-IMP-A.5.9 series.

**Compliance Metrics**:

| Metric | Target | Measurement Method | Reporting Frequency |
|--------|--------|-------------------|-------------------|
| **Completeness** | ≥95% for critical, ≥90% for standard | Discovery reconciliation | Quarterly |
| **Accuracy** | ≥95% information, ≥98% IT infrastructure | Statistical sampling | Quarterly |
| **Currency** | ≥98% within staleness thresholds | Review date analysis | Monthly |
| **Owner Assignment** | 100% | Null owner field check | Monthly |
| **Owner Acknowledgment** | ≥95% within 30 days | Acknowledgment tracking | Monthly |
| **Review Schedule Compliance** | ≥90% reviews on time | Schedule adherence | Quarterly |

### 3.4 Exception Management

**Requirement A.5.9-R8**: [Organization] SHALL establish formal exception process for deviations from inventory requirements.

**Exception Categories**:

1. **Granularity Exception**: Asset requires different level of detail than standard
2. **Review Frequency Exception**: Asset requires different review schedule
3. **Ownership Exception**: Asset has unclear ownership requiring extended resolution time
4. **Technical Exception**: Technical constraints prevent standard inventory approach

**Exception Request Process**:
1. Requestor submits exception request with business justification
2. Information Security Manager performs risk assessment
3. CISO approves/denies exception
4. Approved exceptions documented with:
   - Justification and risk assessment
   - Compensating controls (if applicable)
   - Exception expiration date (maximum 12 months)
   - Re-evaluation criteria
5. Exceptions reviewed during periodic assessments
6. Exception register maintained as evidence

**Exception Authority**:
- **Information Security Manager**: Approve temporary exceptions ≤30 days (tactical)
- **CISO**: Approve exceptions ≤12 months (strategic)
- **Executive Management**: Approve exceptions >12 months (rare, documented at board level)

**Maximum Exception Duration**: 12 months (must be renewed or remediated)

**Verification Method**: Exception register reviewed per ISMS-IMP-A.5.9-5 (Compliance Dashboard).

### 3.5 Incident Response

**Requirement A.5.9-R9**: [Organization] SHALL use asset inventory to support incident response processes.

**Inventory in Incident Response**:
- **Asset Identification**: Quickly identify affected assets and dependencies
- **Owner Notification**: Contact asset owners for business impact assessment
- **Impact Assessment**: Determine criticality and business impact using inventory metadata
- **Containment**: Use dependency information to isolate affected systems
- **Recovery**: Prioritize recovery based on asset criticality classification
- **Root Cause Analysis**: Cross-reference asset configurations and relationships

**Incident-Triggered Inventory Actions**:
- Verify affected asset inventory records are current
- Update asset status if damaged or compromised
- Document incident in asset history
- Review and update risk classification if warranted
- Conduct post-incident inventory validation

**Integration**: Incident management system SHALL reference asset inventory for affected assets.

### 3.6 Policy Governance

**Review Frequency**: Annual minimum, or triggered by:
- Significant organizational changes (mergers, acquisitions, restructuring)
- Major regulatory changes affecting asset management
- Audit findings requiring policy updates
- Risk assessment identifying policy gaps
- Technology changes affecting inventory approach

**Review Process**:
1. Information Security Manager proposes policy updates
2. CISO reviews and approves changes
3. Legal/Compliance reviews regulatory alignment
4. Stakeholder consultation (IT Operations, Application Owners, Information Owners)
5. Executive Management final approval
6. Communication and training on changes
7. Version control and change history maintained

**Triggers for Immediate Review**:
- New regulatory requirements (GDPR-equivalent, sector-specific)
- Significant security incident exposing inventory gaps
- External audit findings
- Material business model changes

**Approval Authority**: Executive Management (CEO or designated authority)

**Version Control**: All policy versions retained for audit trail (minimum 7 years retention)

---

## 4. Implementation & References

### 4.1 Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):
- Asset inventory provides foundation for risk identification
- Asset criticality influences risk rating and treatment prioritization
- Threat-asset-vulnerability analysis requires complete asset inventory
- Risk treatment plans reference inventoried assets

**Statement of Applicability** (ISO 27001 Clause 6.1.3):
- Control A.5.9 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported
- Asset inventory enables other Annex A control implementation

**Related Controls**:

| Control | Relationship | Integration Point |
|---------|-------------|------------------|
| **A.5.10 (Acceptable Use)** | Defines acceptable use of inventoried assets | Asset records reference acceptable use policy |
| **A.5.11 (Return of Assets)** | Asset return tracked in inventory | Status updated upon return/disposal |
| **A.5.12 (Classification)** | Classification applied to information assets | Classification field in inventory |
| **A.5.13 (Labeling)** | Labels applied per inventory classification | Label generation uses inventory data |
| **A.5.14 (Information Transfer)** | Transfer controls based on asset classification | Transfer logs reference asset inventory |
| **A.5.15 (Access Control)** | Access rules protect inventoried assets | Asset-based access control policies |
| **A.5.16 (Identity Management)** | Identities linked to personnel assets | Personnel inventory validates identities |
| **A.5.17 (Authentication)** | Authentication protects asset access | Systems requiring authentication inventoried |
| **A.5.18 (Access Rights)** | Asset owners approve access rights | Ownership in inventory enables approval workflow |
| **A.8.9 (Configuration Management)** | Configuration baselines for IT infrastructure | Baseline referenced in inventory |
| **A.8.10 (Information Deletion)** | Disposal updates inventory status | Disposal triggers inventory update |
| **A.8.19 (Installation of Software)** | Software installation creates inventory record | Application inventory maintained |

### 4.2 Implementation Resources

**Implementation Guidance Suite** (ISMS-IMP-A.5.9):

| Document ID | Title | Purpose | Target Audience |
|-------------|-------|---------|----------------|
| **ISMS-IMP-A.5.9-1** | Asset Identification & Discovery | Procedures for identifying assets, discovery methods, completeness verification | Security Team, IT Operations |
| **ISMS-IMP-A.5.9-2** | Inventory Maintenance | Inventory structure design, update procedures, integration methods | Security Team, IT Operations, System Owners |
| **ISMS-IMP-A.5.9-3** | Quality & Compliance Assessment | Accuracy sampling, currency verification, gap analysis | Security Team, Audit, Compliance |
| **ISMS-IMP-A.5.9-4** | Owner Accountability Assessment | Owner assignment, acknowledgment tracking, responsibility verification | Security Team, Management, Asset Owners |
| **ISMS-IMP-A.5.9-5** | Compliance Dashboard | Executive summary, consolidated metrics, compliance reporting | CISO, Executive Management, Audit |

**Assessment Tools**:
- Excel-based assessment workbooks (generated from Python scripts)
- Automated compliance calculations
- Gap registers
- Evidence tracking
- Trend analysis

**Supporting Materials**:
- Asset categorization decision framework (Annex A)
- Owner acknowledgment form template
- Asset discovery checklist
- Quick reference guide for asset owners (Annex B)

### 4.3 Regulatory Mapping

This policy addresses asset inventory requirements from multiple regulatory frameworks:

| Requirement Category | Swiss nDSG | EU GDPR | ISO 27001 | PCI DSS* | FINMA* | DORA/NIS2* | HIPAA* |
|---------------------|-----------|---------|-----------|---------|--------|------------|--------|
| Asset identification | Art. 8 (data inventory) | Art. 5, 30 (records) | A.5.9 | Req. 2.4 | Risk-based | Asset management | 164.310(d)(1) |
| Owner assignment | Art. 8 (accountability) | Art. 5 (accountability) | A.5.9 | Req. 12.5 | Risk-based | ICT asset register | 164.308(a)(2) |
| Accuracy & currency | Art. 8 (accuracy) | Art. 5 (accuracy) | A.5.9 | Req. 12.5.2 | Risk-based | Current inventory | 164.310(d)(1) |
| Classification | Art. 8 (protection level) | Art. 32 (risk-based) | A.5.9, A.5.12 | Req. 2.2 | Risk-based | Criticality | 164.308(a)(1) |

*Conditional applicability per ISMS-POL-00

**Compliance Verification**: Regulatory compliance demonstration procedures documented in ISMS-IMP-A.5.9-5 (Compliance Dashboard), including evidence registers and audit trail requirements.

### 4.4 Training & Awareness

**Security Awareness** (All Personnel):
- Annual training module on asset responsibilities
- Reporting procedures for lost/damaged assets
- Acceptable use and asset handling
- Privacy considerations (especially for personnel assets)

**Asset Owner Training**:
- Ownership responsibilities and accountability
- Inventory review procedures
- Access approval workflow
- Classification guidance per A.5.12
- Exception request process

**Technical Training** (IT/Security Staff):
- Discovery tool configuration and operation
- Inventory system administration
- Assessment workbook completion
- Integration with CMDB and other systems
- Evidence collection for audits

**Custodian Training**:
- Operational responsibilities
- Inventory update procedures
- Incident reporting
- Delegation boundaries

---

## 5. Definitions

**Asset**: Anything that has value to [Organization] and requires protection. Assets include information, IT infrastructure, applications, physical resources, and personnel competencies.

**Information Asset**: Data, content, or knowledge in any form (structured databases, unstructured documents, intellectual property, configurations, credentials) with confidentiality, integrity, or availability requirements.

**Associated Asset**: Infrastructure, applications, facilities, or personnel that process, store, transmit, or protect information assets. These assets derive their security requirements from the information they support.

**Asset Owner**: Individual accountable for an asset throughout its lifecycle. Owner is responsible for classification, access approval, protection decisions, and compliance with security requirements. Ownership is assigned based on business accountability, not technical custody.

**Asset Custodian**: Individual or team with day-to-day operational responsibility for an asset. Custodian implements security controls as directed by owner but accountability remains with owner.

**Asset Inventory**: Structured register of information and associated assets, documenting mandatory attributes including owner, classification, location, and lifecycle status.

**Inventory Completeness**: Degree to which inventory includes all assets within scope. Measured as percentage of discoverable assets present in inventory.

**Inventory Accuracy**: Degree to which inventory data correctly reflects actual asset state. Measured through sampling and validation against authoritative sources.

**Inventory Currency**: Degree to which inventory reflects current state rather than historical state. Measured by review dates and update timeliness.

**Criticality**: Assessment of business impact should asset be unavailable, compromised, or destroyed. Used to prioritize risk treatment and incident response.

**Lifecycle State**: Current stage in asset lifecycle (active, development, maintenance, retired, archived). Determines applicable controls and maintenance requirements.

**Discovery**: Automated or manual process to identify assets within organizational environment. Discovery compares findings against inventory to identify gaps.

**CMDB (Configuration Management Database)**: Organizational system documenting IT infrastructure configurations. Primary source for IT asset inventory where implemented.

**Personnel Asset**: Key organizational roles and specialized competencies (not individual person records). Documented generically to protect privacy while enabling business continuity planning.

**Granularity**: Level of detail at which assets are inventoried. High-risk assets require individual records; low-risk assets may be grouped (e.g., "standard laptops - quantity 50").

## 6. Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:
- ✅ This policy document (ISMS-POL-A.5.9 v1.0)
- ✅ Approval signatures from CISO, Executive Management, Legal/Compliance Officer
- ✅ Asset inventory creation requirements defined (Section 2.1)
- ✅ Asset categorization framework documented (Section 2.2, Annex A)
- ✅ Mandatory inventory attributes specified (Section 2.3)
- ✅ Asset ownership requirements defined (Section 2.4)
- ✅ Inventory quality standards established (Section 2.5 - completeness, accuracy, currency)
- ✅ Integration requirements with other ISMS controls documented (Section 2.6)
- ✅ Roles and responsibilities assigned (Section 3)
- ✅ Governance and review procedures defined (Section 3.3)
- ✅ Integration with related controls documented (Section 4.1)

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:
- Asset identification and discovery assessments per ISMS-IMP-A.5.9-1 (completeness verification, discovery methods)
- Inventory maintenance assessments per ISMS-IMP-A.5.9-2 (update procedures, integration methods, currency tracking)
- Quality and compliance assessments per ISMS-IMP-A.5.9-3 (accuracy sampling, gap analysis, completeness metrics)
- Owner accountability assessments per ISMS-IMP-A.5.9-4 (ownership assignment, acknowledgment tracking, responsibility verification)
- Asset inventory records (all asset types: information, IT infrastructure, applications, physical, personnel)
- Asset categorization determinations (type, criticality, lifecycle state)
- Asset ownership assignments with owner acknowledgments (100% target)
- Inventory completeness metrics (percentage of assets discovered vs. inventoried)
- Inventory accuracy metrics (percentage of records verified as accurate)
- Inventory currency metrics (percentage of records updated within required timeframes)
- Asset owner review records (annual attestations)
- Integration evidence with other controls (access control, classification, change management, incident management)
- CMDB/HR/procurement system synchronization records
- Asset lifecycle documentation (acquisition, change, retirement records)
- Unowned asset escalation records (if any - with <30 day resolution)
- Compliance dashboard (ISMS-IMP-A.5.9-5) showing consolidated metrics
- Audit findings and remediation evidence for inventory gaps

**Clarification on Compliance Evidence:**

This policy establishes asset inventory requirements (identification, categorization, ownership, maintenance). It does NOT establish:
- **Asset classification requirements** (addressed in A.5.12 Information Classification - inventory provides foundation for classification)
- **Access control to assets** (addressed in A.5.15 Access Control - inventory identifies what to protect)
- **Asset protection controls** (addressed in A.8.x Technical Controls - inventory identifies scope of control application)
- **Risk assessment methodology** (addressed in Clause 6.1 Risk Assessment - inventory provides asset input to risk assessment)
- **Configuration management procedures** (addressed in A.8.9 Configuration Management - inventory tracks configuration items)

The boundary is: POL-A.5.9 defines what must be inventoried and ownership accountability → Other controls define how to protect, classify, and control access to inventoried assets → Inventory is the foundation, controls build upon it.

---

## Annex A: Asset Categorization Decision Matrix

### Purpose

This annex provides practical decision framework for categorizing assets within the inventory. These are **generic examples** that [Organization] adapts to their specific context during risk assessment.

### Primary Categorization: Information vs. Associated Asset

**Decision Question**: Is this INFORMATION or SOMETHING THAT PROCESSES/STORES INFORMATION?

```
┌─ INFORMATION (data, content, knowledge)
│  └─ Information Asset Categories:
│     ├─ Structured Data (databases, tables, data warehouses)
│     ├─ Unstructured Documents (files, emails, reports)
│     ├─ Records & Archives (retained for compliance)
│     ├─ Intellectual Property (trade secrets, patents, designs)
│     ├─ Configuration & Parameters (system configs, settings)
│     ├─ Authentication & Cryptographic (keys, certificates, credentials)
│     ├─ Communication Records (emails, chats, call logs)
│     └─ Business Intelligence (reports, analytics, dashboards)
│
└─ SOMETHING ELSE (system, device, facility, person)
   └─ Associated Asset Categories:
      ├─ IT Infrastructure (servers, storage, networking, endpoints)
      ├─ Applications (software, SaaS, services, APIs)
      ├─ Physical Assets (facilities, media, equipment)
      └─ Personnel Assets (competencies, key roles)
```

### Criticality Assessment Framework

**Business Impact Questions** (determines criticality):

| Impact Area | Critical | High | Medium | Low |
|-------------|----------|------|--------|-----|
| **Operational** | Complete business disruption | Major process failure | Process degradation | Minor inconvenience |
| **Financial** | >5% annual revenue | 1-5% annual revenue | <1% annual revenue | Negligible |
| **Regulatory** | Mandatory reporting, fines | Compliance breach | Minor violation | No impact |
| **Reputational** | National media, customer exodus | Industry press, customer loss | Local press, complaints | No visibility |
| **Recovery Time** | Cannot be replaced | >1 month to replace | 1 week to 1 month | <1 week |

**Criticality Assignment**: Use highest impact area for overall criticality classification.

### Granularity Decision Framework

**Question**: At what level should we inventory this asset?

**High Granularity** (individual records) when:
- Asset is critical to operations
- Asset processes sensitive information (High/Very High classification per A.5.12)
- Regulatory requirements demand individual tracking (PCI cardholder systems, HIPAA PHI systems)
- Asset is unique or specialized
- Asset value justifies tracking overhead

**Low Granularity** (grouped records) when:
- Assets are commodity/standardized
- Assets are low-risk and easily replaceable
- Individual tracking creates excessive maintenance burden
- Assets are homogeneous (identical model, configuration, purpose)

**Examples**:

| Asset Type | Granularity | Rationale |
|------------|-------------|-----------|
| Production database server | Individual | Critical, unique, processes sensitive data |
| CEO laptop | Individual | High-risk user, potential for sensitive information |
| Standard employee laptops (identical model) | Grouped (quantity: 100) | Commodity, standardized, low individual risk |
| Customer PII database | Individual | Regulatory requirement, high sensitivity |
| Office WiFi access points | Grouped by building | Standardized, low individual significance |
| Source code repositories | Individual | Intellectual property, version control needed |
| Marketing brochure PDFs | Grouped by campaign | Public information, low individual value |
| Domain administrator accounts | Individual | High privilege, must track precisely |
| Backup tapes | Grouped by rotation set | Tracked by set, not individual tape |

### Information Asset Categorization Examples

**Structured Data**:
- Customer database (CRM)
- Financial transaction records
- Employee records (HRIS)
- Product inventory database
- Web analytics data warehouse
- Email archives
- Audit logs

**Unstructured Documents**:
- Contracts and agreements
- Project documentation
- Policies and procedures
- Employee handbooks
- Marketing materials
- Meeting recordings
- Design specifications

**Intellectual Property**:
- Source code repositories
- Patent applications and granted patents
- Trade secrets (formulas, algorithms, business methods)
- Product designs and blueprints
- Brand assets (logos, trademarks)
- Proprietary research data

**Configuration & Parameters**:
- System configuration files
- Application settings
- Network device configurations (router, firewall rules)
- Infrastructure-as-Code templates
- Database schemas and stored procedures

### IT Infrastructure Categorization Examples

**Compute**:
- Physical servers (production, development, test)
- Virtual machines
- Containers and orchestration platforms
- Desktop workstations
- Laptops and mobile devices

**Storage**:
- SAN/NAS systems
- Backup infrastructure
- Archive storage
- Cloud storage buckets
- File servers

**Networking**:
- Routers and switches
- Firewalls and security appliances
- Load balancers
- VPN concentrators
- Wireless access points
- DNS/DHCP servers

### Application Categorization Examples

**Business Applications**:
- ERP system
- CRM platform
- Financial management system
- HR management system (HRIS)
- Project management tools
- Collaboration platforms

**SaaS and Cloud Services**:
- Email service (Microsoft 365, Google Workspace)
- Cloud storage (Dropbox, OneDrive)
- Communication tools (Slack, Teams, Zoom)
- Development platforms (GitHub, GitLab, Jira)

**Custom Developed Applications**:
- Customer portal
- Internal management applications
- Mobile applications
- APIs and integration services

### Personnel Asset Categorization

**Critical Roles** (not individuals, but role capabilities):
- C-Level executives (CEO, CFO, CTO, CISO)
- Key technical roles (lead architect, senior DBA)
- Regulatory compliance roles (DPO, compliance officer)
- Security operations roles (SOC lead, incident response)

**Specialized Competencies**:
- Deep technical expertise (specific technologies, legacy systems)
- Regulatory expertise (industry-specific compliance knowledge)
- Vendor relationships (key vendor contacts, negotiation history)
- Certifications (specialized certifications required for operations)
- Language skills (critical for international operations)

**Privacy Note**: Personnel assets document ROLES and COMPETENCIES, never individual person records. "Database Administrator competency (3 qualified staff)" NOT "John Smith - DBA".

---

## Annex B: Quick Reference Guide for Asset Owners

### Your Role as Asset Owner

**You are accountable** for information or associated assets assigned to your ownership. This quick reference summarizes your responsibilities.

### Core Responsibilities

**1. Classify Your Assets** (per ISMS-POL-A.5.12 if implemented)
- Determine confidentiality, integrity, availability requirements
- Consider business impact if asset compromised
- Document classification in inventory

**2. Review Inventory Records**
- **Frequency**: At least annually, or after significant changes
- **Verify**: Asset description, location, classification, dependencies accurate
- **Update**: Submit updates if information changes
- **Attest**: Confirm accuracy by signing review record

**3. Approve Access Requests**
- Review access requests for assets you own
- Verify business need and appropriate privileges
- Approve/deny based on least privilege principle
- Document approval rationale

**4. Report Security Incidents**
- Immediately report incidents affecting owned assets
- Participate in incident investigation
- Approve recovery and restoration procedures
- Review and update asset classification if incident reveals new risks

**5. Manage Asset Lifecycle**
- Participate in decisions: retention, archival, disposal
- Ensure proper disposal per ISMS-POL-A.8.10 (Information Deletion)
- Update inventory when assets retired or archived
- Transfer ownership when changing roles

### When You Need Help

**Inventory Questions**: Contact Information Security Manager
**Technical Issues**: Contact IT Operations or System Custodian
**Classification Guidance**: Contact CISO or Information Security Manager
**Access Approval Workflow**: Contact Identity & Access Management team
**Incident Reporting**: Contact Security Operations Center (SOC) or Help Desk

### Common Scenarios

**Scenario 1: Asset Location Changed**
- **Action**: Submit inventory update request within 3 business days
- **How**: [Organization-specific procedure]

**Scenario 2: Asset No Longer Needed**
- **Action**: Request decommissioning through change management
- **Remember**: Ensure data properly disposed per A.8.10

**Scenario 3: Not Sure Who Should Own Asset**
- **Action**: Contact CISO for ownership determination
- **Timeline**: Resolved within 30 days maximum

**Scenario 4: Asset Criticality Changed**
- **Action**: Update criticality classification in inventory
- **Trigger**: Update risk assessment for this asset

**Scenario 5: Received Access Request**
- **Action**: Verify requestor business need, approve/deny within defined SLA
- **Document**: Rationale for decision

### Annual Review Checklist

When conducting annual inventory review:

- [ ] Verify asset description accurate
- [ ] Confirm physical/logical location correct
- [ ] Validate criticality classification still appropriate
- [ ] Check dependencies documented
- [ ] Ensure custodian assignment current
- [ ] Review access list (if available)
- [ ] Confirm classification appropriate (per A.5.12)
- [ ] Sign attestation form
- [ ] Submit to Information Security Manager

### Owner Acknowledgment

When assigned as asset owner:

- [ ] Receive formal owner assignment notification
- [ ] Review asset inventory record
- [ ] Review this Quick Reference Guide
- [ ] Complete owner training (if required)
- [ ] Sign owner acknowledgment form
- [ ] Add asset to your review schedule

### Owner Transition (Changing Roles)

When leaving role or changing positions:

- [ ] Generate list of owned assets
- [ ] Identify successor owners (with manager approval)
- [ ] Document transition in change management
- [ ] Conduct handover meeting with new owner
- [ ] Update inventory with new owner
- [ ] Confirm new owner acknowledgment received

### Key Policy References

- **Full Policy**: ISMS-POL-A.5.9 (this document)
- **Implementation Guides**: ISMS-IMP-A.5.9-1 through A.5.9-5
- **Classification Policy**: ISMS-POL-A.5.12 (if implemented)
- **Deletion Policy**: ISMS-POL-A.8.10 (if implemented)
- **Access Control Policy**: ISMS-POL-A.5.15 (if implemented)

### Questions or Exceptions?

**For Questions**: Contact Information Security Manager  
**For Exceptions**: Submit exception request per Section 3.4 of full policy  
**For Emergencies**: Contact Security Operations Center (SOC) immediately

---

**END OF ISMS-POL-A.5.9**

*"You cannot protect what you do not know you have. Asset inventory is the foundation of information security."*