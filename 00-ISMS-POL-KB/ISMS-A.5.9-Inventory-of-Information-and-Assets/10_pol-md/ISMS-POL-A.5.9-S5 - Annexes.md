# ISMS-POL-A.5.9-S5
## Inventory of Information and Assets - Annexes

**Document ID**: ISMS-POL-A.5.9-S5  
**Title**: Inventory of Information and Assets - Annexes  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial annexes collection |

**Review Cycle**: Annual (aligned with ISMS policy review cycle)  
**Next Review Date**: 10.01.2027  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Information Security Manager

**Distribution**: Asset owners, custodians, implementation teams, audit team  
**Related Documents**: ISMS-POL-A.5.9 (Master), All S1-S4 sections

---

## 5.1 Annex Overview

This section provides supporting materials, templates, and reference guides to facilitate implementation of Control A.5.9.

**Annexes Included**:
- **S5.A**: Asset Categorization Examples (industry-neutral examples)
- **S5.B**: Owner Acknowledgment Form Template
- **S5.C**: Asset Inventory Record Template
- **S5.D**: Asset Discovery Checklist
- **S5.E**: Quick Reference Guide (for owners and custodians)

**Purpose**: These annexes are **TEMPLATES** that [Organization] should customize for their specific context. They are provided as starting points, not prescriptive requirements.

---

# ANNEX S5.A
## Asset Categorization Examples

### Purpose
Provide concrete examples of how to categorize assets within the framework defined in S2 Section 2.2. These are **generic examples** that [Organization] adapts to their context.

---

### Information Asset Examples

#### Category 1: Structured Data

| Example Asset | Description | Typical Owner | Typical Classification |
|---------------|-------------|---------------|----------------------|
| Customer Database | Primary customer relationship data | Customer Service Director | Confidential |
| Product Catalog | Active product/service offerings | Product Management | Internal |
| Employee Directory | Staff contact information | Human Resources | Internal |
| Financial Ledger | Accounting transactions | Chief Financial Officer | Confidential |
| Inventory Management System | Stock levels and locations | Operations Director | Internal |

#### Category 2: Unstructured Documents

| Example Asset | Description | Typical Owner | Typical Classification |
|---------------|-------------|---------------|----------------------|
| Business Plan (Annual) | Strategic objectives and initiatives | Chief Executive Officer | Confidential |
| Marketing Materials | Brochures, presentations, content | Marketing Director | Public / Internal |
| Technical Specifications | Product design documentation | Engineering Director | Confidential |
| Meeting Minutes | Board/executive meeting records | Corporate Secretary | Confidential |
| Training Materials | Employee training content | Human Resources | Internal |

#### Category 3: Records and Archives

| Example Asset | Description | Typical Owner | Typical Classification |
|---------------|-------------|---------------|----------------------|
| Signed Contracts | Customer/vendor agreements | Legal Counsel | Confidential |
| Tax Returns | Annual tax filings | Chief Financial Officer | Confidential |
| Personnel Files | Employee records and performance | Human Resources | Confidential |
| Audit Reports | Internal/external audit results | Chief Audit Executive | Confidential |
| Compliance Records | Regulatory compliance evidence | Compliance Officer | Confidential |

#### Category 4: Intellectual Property

| Example Asset | Description | Typical Owner | Typical Classification |
|---------------|-------------|---------------|----------------------|
| Application Source Code | Software applications developed | CTO / Engineering Director | Confidential |
| Product Designs | Engineering drawings/CAD files | Engineering Director | Confidential |
| Proprietary Algorithms | Custom algorithms/formulas | Chief Technology Officer | Strictly Confidential |
| Patents | Filed patents and applications | Legal Counsel | Confidential |
| Trade Secrets | Competitive advantage information | Chief Executive Officer | Strictly Confidential |

#### Category 5: Configuration and Parameters

| Example Asset | Description | Typical Owner | Typical Classification |
|---------------|-------------|---------------|----------------------|
| Firewall Rules | Network security policies | Chief Information Officer | Confidential |
| Application Configurations | System parameter settings | Application Owner | Internal |
| Network Maps | Network topology diagrams | Network Manager | Confidential |
| Security Policies (Technical) | IAM policies, ACLs | Chief Information Security Officer | Confidential |
| Backup Configurations | Backup job definitions | IT Operations Manager | Internal |

#### Category 6: Authentication and Cryptographic

| Example Asset | Description | Typical Owner | Typical Classification |
|---------------|-------------|---------------|----------------------|
| Root CA Certificates | Certificate authority keys | Chief Information Security Officer | Strictly Confidential |
| Database Credentials | Production database passwords | Database Administrator | Strictly Confidential |
| API Keys | Service authentication tokens | Application Owner | Confidential |
| SSL/TLS Certificates | Web server certificates | IT Operations Manager | Internal |
| Encryption Keys | Data encryption keys | Chief Information Security Officer | Strictly Confidential |

#### Category 7: Communication Records

| Example Asset | Description | Typical Owner | Typical Classification |
|---------------|-------------|---------------|----------------------|
| Email Archives | Corporate email retention | Chief Information Officer | Confidential |
| Chat Logs | Collaboration platform archives | Chief Information Officer | Internal |
| Call Recordings | Customer service calls | Customer Service Director | Confidential |
| Video Conferences | Recorded meetings | Meeting Organizer | Internal / Confidential |

#### Category 8: Business Intelligence

| Example Asset | Description | Typical Owner | Typical Classification |
|---------------|-------------|---------------|----------------------|
| Sales Dashboard | Real-time sales metrics | Chief Revenue Officer | Confidential |
| Financial Forecasts | Revenue/expense projections | Chief Financial Officer | Confidential |
| Customer Analytics | Usage patterns and insights | Product Management | Confidential |
| Operational Metrics | KPI dashboards | Chief Operating Officer | Internal |

---

### Associated Asset Examples - Technical

#### Category T1: Compute Resources

| Example Asset | Description | Typical Owner | Typical Custodian |
|---------------|-------------|---------------|-------------------|
| Production Database Server | Primary database host | Application Owner | Database Administrator |
| Web Application Server | Frontend web server | Application Owner | Systems Administrator |
| Virtual Machine Farm | VMware/Hyper-V cluster | Chief Information Officer | Virtualization Team |
| Container Platform | Kubernetes cluster | Chief Technology Officer | DevOps Team |
| Serverless Functions | AWS Lambda/Azure Functions | Application Owner | DevOps Team |

#### Category T2: Network Infrastructure

| Example Asset | Description | Typical Owner | Typical Custodian |
|---------------|-------------|---------------|-------------------|
| Core Router | Primary network router | Chief Information Officer | Network Engineer |
| Firewall | Perimeter security appliance | Chief Information Security Officer | Security Engineer |
| Load Balancer | Application load balancer | Chief Information Officer | Network Engineer |
| Wireless Access Points | Office Wi-Fi infrastructure | Chief Information Officer | Network Administrator |
| VPN Concentrator | Remote access gateway | Chief Information Security Officer | Network Engineer |

#### Category T3: Storage Systems

| Example Asset | Description | Typical Owner | Typical Custodian |
|---------------|-------------|---------------|-------------------|
| SAN Storage Array | Primary production storage | Chief Information Officer | Storage Administrator |
| NAS File Server | Shared file storage | Chief Information Officer | Systems Administrator |
| Backup System | Backup/recovery infrastructure | Chief Information Officer | Backup Administrator |
| Object Storage | Cloud object storage (S3-like) | Chief Information Officer | Cloud Administrator |

#### Category T4: Endpoints

| Example Asset | Description | Typical Owner | Typical Custodian |
|---------------|-------------|---------------|-------------------|
| Executive Workstations | C-level computers | User's Department Head | IT Support |
| Standard Laptops | Employee-issued laptops | User's Manager | IT Support |
| Mobile Devices | Smartphones/tablets | User's Manager | Mobile Device Management Team |
| Kiosk Terminals | Customer-facing terminals | Facility Manager | IT Support |

#### Category T5: Applications and Services

| Example Asset | Description | Typical Owner | Typical Custodian |
|---------------|-------------|---------------|-------------------|
| ERP System | Enterprise resource planning | Chief Operating Officer | Application Administrator |
| CRM Platform | Customer relationship management | Chief Revenue Officer | CRM Administrator |
| Email System | Corporate email service | Chief Information Officer | Email Administrator |
| Collaboration Platform | Teams/Slack/etc. | Chief Information Officer | Collaboration Admin |
| HR Management System | HRMS application | Human Resources Director | HRMS Administrator |

#### Category T6: Development and Testing

| Example Asset | Description | Typical Owner | Typical Custodian |
|---------------|-------------|---------------|-------------------|
| Development Environment | Dev/test infrastructure | Chief Technology Officer | DevOps Team |
| CI/CD Pipeline | Build/deployment automation | Chief Technology Officer | DevOps Team |
| Code Repository | Git/source control | Chief Technology Officer | Development Manager |
| Test Data Management | Test data systems | Application Owner | QA Manager |

---

### Associated Asset Examples - Physical

#### Category P1: Facilities

| Example Asset | Description | Typical Owner | Typical Custodian |
|---------------|-------------|---------------|-------------------|
| Primary Data Center | Production datacenter facility | Chief Information Officer | Facilities Manager |
| Office Locations | Office buildings/spaces | Chief Operating Officer | Facilities Manager |
| Secure Storage Room | Media/backup storage | Chief Information Security Officer | Facilities Manager |
| Server Closets | Branch office IT rooms | Chief Information Officer | Local IT Contact |

#### Category P2: Physical Media

| Example Asset | Description | Typical Owner | Typical Custodian |
|---------------|-------------|---------------|-------------------|
| Backup Tapes | Monthly/yearly backup tapes | Data Owner | Backup Administrator |
| External Hard Drives | Portable storage devices | Data Owner | User / IT Support |
| Archive DVDs | Historical data archives | Records Manager | Records Retention Team |
| USB Flash Drives | Portable USB storage | User's Manager | User |

#### Category P3: Equipment

| Example Asset | Description | Typical Owner | Typical Custodian |
|---------------|-------------|---------------|-------------------|
| Network Printers | Office multifunction devices | Chief Information Officer | IT Support |
| Document Scanners | High-volume scanners | Department Manager | Department Staff |
| Shredders | Secure disposal equipment | Facilities Manager | Facilities Staff |

#### Category P4: Physical Security Assets

| Example Asset | Description | Typical Owner | Typical Custodian |
|---------------|-------------|---------------|-------------------|
| Access Control System | Badge/biometric access | Chief Security Officer | Security Operations |
| Surveillance Cameras | CCTV system | Chief Security Officer | Security Operations |
| Server Room Locks | Physical access controls | Chief Information Officer | Facilities Manager |
| Fire Suppression System | Datacenter fire protection | Facilities Manager | Facilities Maintenance |

---

### Associated Asset Examples - Personnel

#### Category H1: Key Personnel

| Example Asset | Description | Typical Owner | Typical Accountability |
|---------------|-------------|---------------|----------------------|
| Database Administrator (Critical Role) | Individual with root DB access | Chief Information Officer | Cannot afford to lose without succession |
| Network Architect (Specialized) | Only person who understands legacy routing | Chief Information Officer | Single point of failure |
| Application Owner (Business-Critical) | Owner of revenue-generating system | Application Owner | Business continuity dependency |

#### Category H2: Critical Competencies

| Example Competency | Description | Typical Owner | Personnel Count |
|-------------------|-------------|---------------|-----------------|
| CISSP Certification | Information security certification | Chief Information Security Officer | 3 staff members |
| Mainframe Programming | Legacy system maintenance | Chief Technology Officer | 1 staff member |
| Regulatory Expertise | Compliance domain knowledge | Compliance Officer | 2 staff members |

#### Category H3: Third-Party Dependencies

| Example Dependency | Description | Typical Owner | Relationship Type |
|-------------------|-------------|---------------|-------------------|
| Cloud Service Provider | Infrastructure hosting | Chief Information Officer | Critical vendor |
| Managed Security Provider | SOC/SIEM services | Chief Information Security Officer | Critical service |
| Specialized Consultant | Domain expert on retainer | Relevant Director | Knowledge dependency |

---

### Granularity Decision Examples

**Example 1: Database Server**

| Level | Description | When Appropriate |
|-------|-------------|------------------|
| **High Granularity** | Individual databases within server | High-value data with different owners/classifications |
| **Medium Granularity** | Database server as single asset | Standard operational database, single owner |
| **Low Granularity** | Database cluster/farm | Development/test databases, low criticality |

**[Organization] Decision**: Choose based on data classification and ownership diversity.

**Example 2: File Server**

| Level | Description | When Appropriate |
|-------|-------------|------------------|
| **High Granularity** | Individual folders/shares | Different departments with different owners |
| **Medium Granularity** | Server as single asset | Single-purpose file server, one owner |
| **Low Granularity** | Storage infrastructure | Low-criticality shared storage |

**[Organization] Decision**: Typically folder/share level for shared data.

**Example 3: Cloud VMs (Ephemeral)**

| Level | Description | When Appropriate |
|-------|-------------|------------------|
| **Service Level** | Auto-scaling group template | VMs created/destroyed dynamically |
| **Instance Level** | Individual VM instances | Static VMs with long lifecycles |

**[Organization] Decision**: Service level for ephemeral, instance level for static.

---

# ANNEX S5.B
## Owner Acknowledgment Form Template

### Purpose
Template for asset owners to formally acknowledge their responsibilities per ISO 27002:2022 Section 5.9.

---

### ASSET OWNER ACKNOWLEDGMENT FORM

**Date**: _______________

**Asset Owner Information**:
- Name: _______________________________________
- Title/Role: ___________________________________
- Department: __________________________________
- Email: _______________________________________
- Phone: _______________________________________

**Assets Assigned**:
(List attached as separate document or reference inventory system)

☐ I have reviewed the list of assets for which I am designated owner

---

### OWNER RESPONSIBILITIES ACKNOWLEDGMENT

I understand and accept that as an Asset Owner, I am accountable for the following responsibilities throughout the asset lifecycle (per ISO 27002:2022 Section 5.9):

☐ **a) Inventorying**: I will ensure my assets are inventoried and inventory records are accurate

☐ **b) Classification and Protection**: I will determine appropriate classification and ensure proper protection

☐ **c) Periodic Review**: I will review asset classification and controls at required intervals

☐ **d) Component Tracking**: For technology assets, I will ensure components are listed and linked

☐ **e) Acceptable Use**: I will define acceptable use requirements for my assets

☐ **f) Access Control**: I will approve access requests and regularly review access rights

☐ **g) Secure Disposal**: I will ensure assets are securely handled during deletion/disposal

☐ **h) Risk Management**: I will participate in identifying and managing asset-related risks

☐ **i) User Support**: I will support personnel who manage my assets

---

### ADDITIONAL ACKNOWLEDGMENTS

☐ I understand that I may **delegate tasks** to custodians/administrators, but I retain **accountability**

☐ I understand that I am responsible for:
  - Approving access to my assets
  - Approving changes to my assets
  - Approving disposal of my assets
  - Defining acceptable use
  - Accepting risks (within my authority level)

☐ I understand I must complete required **asset owner training** within 30 days

☐ I understand I must **review my assets** at the following frequency:
  - Critical assets: Quarterly
  - High assets: Semi-annually
  - Standard/Low assets: Annually

☐ I understand that failure to fulfill owner responsibilities may result in:
  - Asset misclassification and inadequate protection
  - Compliance violations
  - Security incidents
  - Audit findings

---

### SUPPORT AND RESOURCES

I understand that support is available from:
- **Information Security Team**: [Contact]
- **IT Asset Management Team**: [Contact]
- **My Manager**: [Contact]
- **CISO Office**: [Contact]

Training materials and documentation available at: [Location/URL]

---

### ACKNOWLEDGMENT

**I acknowledge that I have read, understood, and accept the responsibilities of an Asset Owner as defined in ISMS-POL-A.5.9.**

**Signature**: _____________________________ **Date**: _______________

**Print Name**: _____________________________

---

### FOR OFFICIAL USE

**Approved By** (Manager/Director):

Signature: _____________________________ Date: _______________

Print Name: _____________________________

**Recorded By** (Information Security Team):

Name: _____________________________ Date: _______________

**Record Location**: [Inventory System / Document Repository]

---

**Note**: This acknowledgment should be renewed annually during access reviews, or when significant changes occur to assigned assets.

---

# ANNEX S5.C
## Asset Inventory Record Template

### Purpose
Template showing mandatory and recommended fields for inventory records. [Organization] adapts this to their inventory system.

---

### INFORMATION ASSET INVENTORY RECORD

#### Universal Attributes (Mandatory)

| Field | Description | Example Value |
|-------|-------------|---------------|
| **Asset ID** | Unique identifier | INFO-2024-0123 |
| **Asset Name** | Human-readable name | Customer Relationship Database |
| **Asset Type** | Category | Structured Data |
| **Description** | Purpose and content | Primary CRM database containing customer contacts, interactions, and sales pipeline |
| **Owner** | Accountable person | Jane Smith, Customer Service Director |
| **Owner Email** | Contact | jane.smith@organization.example |
| **Custodian** | Day-to-day responsible | John Doe, Database Administrator |
| **Custodian Email** | Contact | john.doe@organization.example |
| **Classification** | Sensitivity level | Confidential |
| **Location** | Physical/logical location | Production Database Server PROD-DB-01 |
| **Status** | Lifecycle stage | Active |
| **Created Date** | When acquired/created | 15.03.2020 |
| **Last Updated** | Inventory record changed | 05.01.2026 |
| **Last Reviewed** | Owner last reviewed | 10.12.2025 |
| **Next Review Date** | Scheduled review | 10.03.2026 (Quarterly) |

#### Information Asset Specific (Mandatory)

| Field | Description | Example Value |
|-------|-------------|---------------|
| **Data Classification** | CIA requirements | Confidentiality: High, Integrity: High, Availability: Medium |
| **Data Format** | Format/schema | PostgreSQL database |
| **Storage Location(s)** | Where data resides | Primary: PROD-DB-01, Backup: BACKUP-SYS-02, DR: DR-DB-01 |
| **Retention Period** | How long kept | 7 years (regulatory requirement) |
| **Legal/Regulatory** | Applicable regulations | Data Protection Law, Customer Privacy Regulation |
| **Related Systems** | Accessing applications | CRM Application (APP-CRM-001), Reporting System (APP-RPT-003) |

#### Optional/Extended Attributes

| Field | Description | Example Value |
|-------|-------------|---------------|
| **Business Criticality** | Business impact if unavailable | High (Revenue impact within 4 hours) |
| **Data Volume** | Size/scale | 500 GB, 2.5 million customer records |
| **Update Frequency** | How often data changes | Real-time (continuous) |
| **Backup Frequency** | Backup schedule | Hourly incremental, daily full |
| **Dependencies** | Required assets | Network infrastructure, storage array, authentication system |
| **Compliance Certifications** | Applicable certs | ISO 27001, SOC 2 Type II |
| **Notes/Comments** | Additional information | Undergoing migration to cloud Q3 2026 |

---

### ASSOCIATED ASSET (TECHNICAL) INVENTORY RECORD

#### Universal Attributes (Mandatory)

| Field | Description | Example Value |
|-------|-------------|---------------|
| **Asset ID** | Unique identifier | IT-SVR-2024-0045 |
| **Asset Name** | Human-readable name | Production Database Server 01 |
| **Asset Type** | Category | Compute Resources - Physical Server |
| **Description** | Purpose | Primary database server for CRM application |
| **Owner** | Accountable person | Jane Smith, Customer Service Director |
| **Custodian** | Technical responsible | John Doe, Database Administrator |
| **Classification** | Inherited from data | Confidential (processes Confidential data) |
| **Location** | Physical location | Data Center A, Rack 12, Unit 15 |
| **Status** | Lifecycle stage | Active - Production |
| **Created Date** | When acquired | 20.05.2020 |
| **Last Updated** | Record changed | 08.01.2026 |
| **Last Reviewed** | Owner reviewed | 15.12.2025 |
| **Next Review Date** | Scheduled review | 15.06.2026 (Semi-annual) |

#### Technical Asset Specific (Mandatory)

| Field | Description | Example Value |
|-------|-------------|---------------|
| **Manufacturer/Vendor** | Producer | Dell EMC |
| **Model/Version** | Product model | PowerEdge R740 |
| **Serial Number** | Physical identifier | SN: ABCD1234567890 |
| **Asset Tag** | Organization tag | ORG-IT-0045 |
| **IP Address** | Network identifier | 10.20.30.45 |
| **Hostname** | DNS name | prod-db-01.internal.organization.example |
| **Operating System** | OS version | Ubuntu 22.04 LTS |
| **Configuration Baseline** | Standard config | DB-Server-Standard-v3.2 |
| **Dependencies** | Required assets | Network switch SW-CORE-02, Storage array SAN-01, Power UPS-A-12 |
| **Supported Information** | What information processed | Customer Relationship Database (INFO-2024-0123) |

#### Optional/Extended Attributes

| Field | Description | Example Value |
|-------|-------------|---------------|
| **Purchase Date** | When bought | 01.05.2020 |
| **Purchase Cost** | Acquisition cost | €15,000 |
| **Warranty Expiration** | Support end date | 01.05.2025 (expired - renewal needed) |
| **Support Contract** | Support details | Dell ProSupport Plus - Contract #12345 |
| **CPU** | Processor | Dual Intel Xeon Silver 4214, 12-core |
| **Memory** | RAM | 128 GB DDR4 |
| **Storage** | Local storage | 2 × 1 TB SSD (RAID 1) |
| **Power Consumption** | Watts | 450W average |
| **Patch Level** | Current patch | All patches current as of 08.01.2026 |
| **Vulnerabilities** | Known issues | None critical (last scan 05.01.2026) |
| **Change History** | Recent changes | RAM upgrade 64GB→128GB on 10.11.2025 |

---

### USAGE NOTES

**For [Organization]**:
1. **Mandatory fields** must be populated (no exceptions)
2. **Optional fields** populate if relevant and maintainable
3. **Adapt field names** to match your inventory system
4. **Add custom fields** as needed for your context
5. **Automate** field population where possible (discovery, integration)

**Field Population Sources**:
- **Owner/Custodian**: Manual assignment + acknowledgment
- **Classification**: Owner determination (per A.5.12)
- **Location**: Discovery tools / manual documentation
- **Technical attributes**: Discovery tools / CMDB
- **Dates**: Automated timestamps + manual reviews
- **Dependencies**: Manual documentation + automated discovery

---

# ANNEX S5.D
## Asset Discovery Checklist

### Purpose
Systematic checklist to help identify assets during initial inventory creation or periodic reviews.

---

### INFORMATION ASSET DISCOVERY

#### Structured Data

☐ **Databases**
  - Production databases (identify all)
  - Data warehouses
  - Data marts
  - Data lakes
  - Reporting databases
  - Archive databases

☐ **Registries and Directories**
  - Customer databases/CRM data
  - Employee directories
  - Product catalogs
  - Vendor/supplier databases
  - Asset registers (non-IT)
  - Contact lists

**Discovery Method**: Interview database administrators, query CMDB, review application dependencies

---

#### Unstructured Documents

☐ **Office Documents**
  - Financial reports
  - Business plans and strategies
  - Marketing materials
  - Technical specifications
  - Presentations
  - Spreadsheets

☐ **Collaboration Spaces**
  - SharePoint sites
  - Wiki pages
  - Shared network drives
  - Cloud storage (OneDrive, Google Drive, etc.)

**Discovery Method**: Review file servers, collaboration platforms, interview department heads

---

#### Records and Archives

☐ **Legal Documents**
  - Contracts (customer, vendor, partner)
  - Legal agreements
  - Patents and trademarks
  - Corporate governance documents

☐ **Compliance Records**
  - Audit reports
  - Compliance certifications
  - Regulatory filings
  - Retention schedules

☐ **Personnel Records**
  - Employee files
  - Performance reviews
  - Training records

**Discovery Method**: Interview legal, compliance, HR; review document management systems

---

#### Intellectual Property

☐ **Source Code**
  - Application source code
  - Scripts and automation
  - Configuration-as-code

☐ **Designs**
  - Product designs
  - Engineering drawings
  - CAD files

☐ **Proprietary Information**
  - Trade secrets
  - Algorithms and formulas
  - Processes and procedures

**Discovery Method**: Review code repositories, CAD systems, interview engineering/development teams

---

#### Configuration and Credentials

☐ **System Configurations**
  - Firewall rules
  - Router configurations
  - Application settings
  - Security policies

☐ **Authentication Data**
  - Certificate stores
  - Password vaults
  - API keys
  - Encryption keys

**Discovery Method**: Interview IT security, network teams; review configuration management systems

---

#### Communications

☐ **Email Archives**
☐ **Chat Logs**
☐ **Meeting Recordings**
☐ **Call Records**

**Discovery Method**: Review email retention systems, collaboration platforms

---

#### Business Intelligence

☐ **Dashboards**
☐ **Reports**
☐ **Analytics**
☐ **Forecasts**

**Discovery Method**: Review BI platforms, interview business analysts

---

### ASSOCIATED ASSET DISCOVERY - TECHNICAL

#### Compute Resources

☐ **Physical Servers**
  - Production servers
  - Development/test servers
  - Infrastructure servers

☐ **Virtual Machines**
  - VM inventories from hypervisor

☐ **Containers**
  - Container registries
  - Running containers

☐ **Cloud Resources**
  - Cloud VMs
  - Serverless functions

**Discovery Method**: Network scans, hypervisor inventory, cloud API queries, CMDB

---

#### Network Infrastructure

☐ **Routers**
☐ **Switches**
☐ **Firewalls**
☐ **Load Balancers**
☐ **Wireless Access Points**
☐ **VPN Concentrators**

**Discovery Method**: Network discovery scans, SNMP queries, network diagrams

---

#### Storage Systems

☐ **SAN/NAS**
☐ **Object Storage**
☐ **Backup Systems**
☐ **Removable Media**

**Discovery Method**: Storage management systems, backup catalogs, physical inventory

---

#### Endpoints

☐ **Workstations/Desktops**
☐ **Laptops**
☐ **Mobile Devices** (smartphones, tablets)
☐ **Specialized Terminals**

**Discovery Method**: Endpoint management systems (SCCM, Intune, MDM), network scans

---

#### Applications

☐ **Business Applications** (ERP, CRM, HRMS, etc.)
☐ **Infrastructure Services** (DNS, DHCP, NTP, etc.)
☐ **SaaS Applications**
☐ **Custom Applications**

**Discovery Method**: License inventories, user surveys, network traffic analysis, SaaS management platforms

---

### ASSOCIATED ASSET DISCOVERY - PHYSICAL

#### Facilities

☐ **Data Centers**
☐ **Office Locations**
☐ **Secure Storage Rooms**
☐ **Remote Sites**

**Discovery Method**: Facilities management records, physical inspection

---

#### Physical Media

☐ **Backup Tapes**
  - On-site storage
  - Off-site storage
  - Iron Mountain or similar

☐ **External Drives**
☐ **Optical Media** (CD/DVD)
☐ **USB Drives**

**Discovery Method**: Backup catalogs, physical counts, media tracking systems

---

#### Equipment

☐ **Printers/MFDs**
☐ **Scanners**
☐ **Copiers**
☐ **Fax Machines**
☐ **Specialized Equipment**

**Discovery Method**: Network scans (for networked devices), purchase records, physical inventory

---

#### Physical Security

☐ **Access Control Systems**
☐ **Surveillance Cameras**
☐ **Locks and Safes**
☐ **Environmental Controls** (HVAC, fire suppression)

**Discovery Method**: Security team inventory, facilities management

---

### ASSOCIATED ASSET DISCOVERY - PERSONNEL

#### Key Personnel

☐ **Individuals with Privileged Access**
  - Domain admins
  - Database admins
  - Security admins
  - Application admins

☐ **Specialized Knowledge**
  - Legacy system experts
  - Rare skill holders
  - Single points of failure

☐ **Critical Business Roles**
  - Key customer relationships
  - Unique business expertise

**Discovery Method**: HR records, access reviews, manager interviews

---

#### Competencies

☐ **Certifications**
  - Security certifications (CISSP, etc.)
  - Technical certifications
  - Professional licenses

☐ **Specialized Skills**
  - Programming languages (especially rare ones)
  - Domain expertise
  - Language skills

**Discovery Method**: HR system, training records, competency databases

---

#### Third-Party Dependencies

☐ **Critical Vendors**
☐ **Managed Service Providers**
☐ **Key Consultants**
☐ **Partners**

**Discovery Method**: Procurement records, contract management, vendor management

---

### DISCOVERY VERIFICATION

After completing discovery, verify completeness:

☐ **Cross-Check with**:
  - Network discovery scans
  - CMDB
  - Procurement records
  - License inventories
  - Financial asset register
  - HR system
  - Facilities inventory

☐ **Validate with**:
  - Department managers (attestation)
  - IT teams
  - Security team
  - Facilities team

☐ **Document**:
  - Discovery method used
  - Date of discovery
  - Who performed discovery
  - Coverage percentage

---

# ANNEX S5.E
## Quick Reference Guide

### Purpose
One-page quick reference for asset owners and custodians.

---

### QUICK REFERENCE: ASSET OWNER

**Your Role**: You are **accountable** for protecting your asset throughout its lifecycle.

**Key Responsibilities**:
1. ✅ Ensure asset is in inventory with accurate information
2. ✅ Classify asset appropriately (Confidential, Internal, Public, etc.)
3. ✅ Define who can use the asset and how
4. ✅ Approve access requests
5. ✅ Review asset quarterly/semi-annually/annually (based on criticality)
6. ✅ Approve changes and disposal
7. ✅ Participate in risk assessments
8. ✅ Support custodians/users with business context

**You CAN Delegate**:
- Technical implementation → Custodian
- Day-to-day operations → Custodian
- Monitoring and alerts → Operations

**You CANNOT Delegate**:
- Accountability (you remain answerable)
- Classification decisions
- Access approval authority
- Risk acceptance

**Review Schedule**:
- Critical assets: **Every 3 months**
- High assets: **Every 6 months**
- Standard/Low assets: **Every 12 months**

**When to Update Inventory**:
- Asset acquired/created
- Asset changes significantly
- Asset ownership changes
- Asset classification changes
- Asset disposed

**Need Help?**
- Training: [URL/Location]
- Security Team: [Contact]
- Asset Management: [Contact]
- Your Manager: [Contact]

---

### QUICK REFERENCE: ASSET CUSTODIAN

**Your Role**: You implement and maintain security controls **under the owner's direction**.

**Key Responsibilities**:
1. ✅ Implement technical security controls
2. ✅ Perform backups and monitor health
3. ✅ Apply patches and updates
4. ✅ Respond to security alerts
5. ✅ Execute owner-approved changes
6. ✅ Maintain technical documentation
7. ✅ Keep inventory technically accurate
8. ✅ Notify owner of significant issues

**You Work With**:
- **Owner**: Provides direction, approves decisions
- **Security Team**: Provides security guidance
- **Users**: Provide support and access

**You Report To**: Asset Owner (for asset matters)

**When to Contact Owner**:
- Access request received (owner approves)
- Major incident or issue
- Change request requiring approval
- Classification question
- Risk decision needed

**Update Inventory When**:
- Technical details change (IP, location, config)
- Patches applied
- Incidents occur
- Maintenance performed

**Need Help?**
- Asset Owner: [See inventory]
- Security Team: [Contact]
- Asset Management: [Contact]
- IT Support: [Contact]

---

### QUICK REFERENCE: COMMON QUESTIONS

**Q: Who owns this asset?**
A: Check inventory system. If unclear, ask your manager or Security Team.

**Q: How do I request an exception?**
A: Submit exception request form to Security Team with business justification.

**Q: Asset not in inventory. What do I do?**
A: Report to Asset Management or Security Team immediately. Add within 5 business days.

**Q: I'm leaving my role. What about my assets?**
A: Work with your manager to reassign ownership before departure. Maximum 30-day gap.

**Q: How detailed should inventory be?**
A: Detailed enough to support risk management and security decisions. See granularity guidance in S2.

**Q: Can I skip reviews if nothing changed?**
A: No. Reviews verify accuracy even if no changes. Quick review better than skipped review.

**Q: What if I disagree with classification?**
A: Discuss with Security Team. Owner makes final decision with CISO approval if high-risk.

---

### QUICK REFERENCE: COMPLIANCE TARGETS

| Metric | Target | What It Means |
|--------|--------|---------------|
| **Completeness** | ≥95% | 95%+ of discovered assets are inventoried |
| **Owner Assignment** | 100% | Every asset has an owner (no exceptions) |
| **Owner Acknowledgment** | 100% | All owners have acknowledged responsibilities |
| **Review Currency** | ≥90% | 90%+ of assets reviewed on time |
| **Accuracy** | ≥95% | 95%+ of sampled records are accurate |

**Overall Goal**: ≥95% compliance = **Green** status ✅

---

**END OF ANNEXES (S5)**

**Previous Document**: ISMS-POL-A.5.9-S4 - Roles, Responsibilities, and Governance

---

*"The first principle is that you must not fool yourself — and you are the easiest person to fool."*  
— Richard Feynman

**These annexes provide practical templates and reference materials to support implementation of Control A.5.9, helping [Organization] move from policy to practice.** 🎯