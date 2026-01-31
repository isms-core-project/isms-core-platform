# ISMS-POL-A.8.9-S2.1
## Configuration Management - Baseline Configuration Requirements

**Document ID**: ISMS-POL-A.8.9-S2.1  
**Title**: Baseline Configuration Requirements  
**Version**: 1.0  
**Date**: [Date] 
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]| Configuration Manager / Information Security Manager | Initial baseline requirements |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: 07.01.2027  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Configuration Manager / Chief Technology Officer
- Operations Review: IT Operations Manager / System Administrators Lead

**Distribution**: Configuration management team, system administrators, DevOps engineers, asset owners  
**Related Documents**: ISMS-POL-A.8.9-S1 (Definitions), ISMS-IMP-A.8.9.1 (Baseline Assessment)

---

## 2.1.1 Purpose

This document defines **mandatory and recommended requirements** for establishing, documenting, and maintaining configuration baselines. Baselines serve as the foundation for all other configuration management domains (change control, monitoring, hardening).

**The Anti-Pattern**: Organizations that create 500-page baseline documents that nobody reads, or worse, baseline documents that describe an ideal state that has never existed in production. Baselines must reflect **reality** and be **actionable**.

**The Feynman Standard**: *"If you can't use your baseline documentation to rebuild a server in under 2 hours, your documentation is useless."*

---

## 2.1.2 Baseline Definition Requirements

### 2.1.2.1 Asset Identification and Classification

**MUST Requirements**:
- All IT assets subject to configuration management MUST be uniquely identifiable in the Configuration Management Database (CMDB) or equivalent inventory system
- Each asset MUST be classified by:
  - **Asset Type** (server, network device, endpoint, cloud service, application, etc.)
  - **Criticality Level** (Critical, High, Medium, Low)
  - **Environment** (Production, Staging, Development, Test)
  - **Asset Owner** (responsible individual or team)
  - **Technical Owner** (hands-on management contact)
- Asset identifiers MUST be persistent across the asset lifecycle

**SHOULD Requirements**:
- Assets SHOULD be tagged with business service relationships (which applications/services depend on this asset)
- Assets SHOULD include location information (data center, region, availability zone, office location)
- Assets SHOULD track procurement and lifecycle dates (purchase, warranty, end-of-support, planned retirement)

**MAY Requirements**:
- Organizations MAY use additional classification schemes (e.g., data classification, compliance scope, cost center)
- Organizations MAY integrate with IT Asset Management (ITAM) systems for financial asset tracking

**Anti-Cargo-Cult Check**: Can you answer "What are all my Windows Servers?" in under 30 seconds? If not, your CMDB is decoration, not discovery.

### 2.1.2.2 Configuration Item (CI) Hierarchy

**MUST Requirements**:
- The organization MUST define a CI hierarchy establishing parent-child relationships between assets
- CIs MUST include at minimum:
  - Physical infrastructure (servers, storage, network devices)
  - Virtual infrastructure (hypervisors, VMs, containers)
  - Operating systems
  - Applications and middleware
  - Network services (DNS, DHCP, NTP, etc.)
  - Security services (firewalls, IDS/IPS, proxies)

**Example CI Hierarchy**:
```
Data Center A (Location)
└── Physical Server: SRV-DC-APP01 (Hardware)
    └── VMware ESXi 7.0 (Hypervisor)
        ├── VM: APP-PROD-WEB01 (Virtual Machine)
        │   └── Windows Server 2022 (Operating System)
        │       ├── IIS 10.0 (Web Server)
        │       └── Application: CustomerPortal v3.2 (Application)
        └── VM: APP-PROD-DB01 (Virtual Machine)
            └── Ubuntu 22.04 LTS (Operating System)
                └── PostgreSQL 15 (Database)
```

**SHOULD Requirements**:
- CI relationships SHOULD include dependencies (this application depends on these databases, network services, etc.)
- CIs SHOULD track configuration files and critical directories

**Rationale**: Hierarchy enables impact analysis ("if we change this firewall rule, what breaks?") and supports rollback planning.

### 2.1.2.3 Baseline Naming Conventions

**MUST Requirements**:
- Baseline names MUST follow a consistent naming convention
- Baseline names MUST include:
  - Asset type or category
  - Operating system or platform
  - Purpose or role
  - Version or revision number

**Recommended Naming Convention**:
```
[AssetType]-[OS/Platform]-[Role]-[Version]

Examples:
- Server-Windows2022-DomainController-v1.2
- Server-RHEL9-WebServer-v2.0
- Network-CiscoIOS-CoreRouter-v3.1
- Cloud-AWS-EC2-ApplicationTier-v1.0
- Database-PostgreSQL15-Production-v2.3
```

**SHOULD Requirements**:
- Baseline names SHOULD avoid vendor-specific product names where possible (use "Linux Web Server" not "Apache RHEL Server" unless vendor-specific settings apply)
- Version numbers SHOULD follow semantic versioning (Major.Minor.Patch)

**Anti-Pattern**: Baselines named "ServerConfig_Final_v2_FINAL_REALLY_FINAL.docx"

### 2.1.2.4 Version Control Requirements

**MUST Requirements**:
- All baseline definitions MUST be version-controlled
- Version increments MUST be documented with:
  - **Date of change**
  - **Author/responsible party**
  - **Reason for change** (security update, compliance requirement, operational improvement, etc.)
  - **Summary of changes** (what was added, modified, removed)
- Previous baseline versions MUST be retained for audit and rollback purposes

**SHOULD Requirements**:
- Baselines SHOULD be stored in version control systems (Git, SVN, etc.) or document management systems with versioning
- Baseline changes SHOULD trigger review by Configuration Manager and Asset Owner
- Major version changes (X.0) SHOULD require formal approval

**MAY Requirements**:
- Organizations MAY use automated version control for IaC-based baselines
- Organizations MAY integrate baseline version control with change management ticketing

---

## 2.1.3 Asset-Specific Baseline Requirements

### 2.1.3.1 Server Operating Systems

**MUST Requirements**:
- All production servers MUST have documented baseline configurations
- Server baselines MUST define at minimum:
  - Operating system version and patch level
  - Installed roles and features (or services/packages for Linux)
  - Security configurations (authentication, audit policy, firewall rules)
  - Network configurations (IP addressing if static, DNS settings)
  - Monitoring agents and management tools
  - Backup agent configurations
- Server baselines MUST reference applicable hardening standards (CIS Benchmark level, DISA STIG, vendor security guide)

**SHOULD Requirements**:
- Baselines SHOULD specify service account requirements (type, permissions, password policy)
- Baselines SHOULD document anti-malware and security agent requirements
- Baselines SHOULD define logging and auditing configurations
- Baselines SHOULD specify time synchronization (NTP) configurations

**MAY Requirements**:
- Baselines MAY include performance tuning parameters
- Baselines MAY specify organizational-specific software packages

**Baseline Granularity**:
- **Generic Baselines**: "Windows Server 2022" baseline applies to all Windows 2022 systems
- **Role-Specific Baselines**: "Windows Server 2022 - Domain Controller" inherits generic baseline plus adds role-specific configurations
- **Application-Specific**: "Windows Server 2022 - SQL Server" adds database-specific configurations

**Example Baseline Categories**:
- Windows Server - Domain Controller
- Windows Server - Member Server (Generic)
- Windows Server - File Server
- Windows Server - Web Server (IIS)
- Windows Server - Database Server (SQL Server)
- Linux Server - Web Server (Apache/Nginx)
- Linux Server - Application Server
- Linux Server - Database Server (PostgreSQL/MySQL)

### 2.1.3.2 Network Infrastructure Devices

**MUST Requirements**:
- All network devices (routers, switches, firewalls) MUST have documented baseline configurations
- Network device baselines MUST include:
  - Device model and firmware/OS version
  - Management interface configurations (SSH enabled, Telnet disabled, etc.)
  - Authentication and authorization (TACACS+, RADIUS, local accounts)
  - SNMP settings (v3 only, community strings if v2 legacy)
  - Logging configurations (syslog destinations, logging levels)
  - NTP configurations
  - Interface configurations (VLANs, trunking, access control)
  - Security features (port security, DHCP snooping, ARP inspection)
- Network baselines MUST reference hardening guides (CIS, DISA STIG, vendor security guides)

**SHOULD Requirements**:
- Baselines SHOULD document routing protocol configurations (OSPF, BGP, static routes)
  - Network baselines SHOULD specify ACL (Access Control List) strategies and examples
- Baselines SHOULD document Quality of Service (QoS) policies if applicable
- Baselines SHOULD include high-availability configurations (HSRP, VRRP, stacking)

**MAY Requirements**:
- Baselines MAY include traffic monitoring configurations (NetFlow, sFlow)
- Baselines MAY document integration with network management platforms

**Cargo Cult Warning**: Don't just copy-paste the running-config. Document the REQUIRED settings and WHY they matter. A 5000-line firewall config where only 50 lines are security-critical is noise, not knowledge.

### 2.1.3.3 Endpoint Devices

**MUST Requirements**:
- Endpoint baselines (workstations, laptops) MUST be defined for each supported operating system
- Endpoint baselines MUST include:
  - Operating system version and edition
  - Security configurations (BitLocker/encryption, firewall, Windows Defender/AV)
  - Management agent (SCCM, Intune, Jamf, etc.)
  - Required business applications
  - Update and patching policy
  - User access controls (local admin restrictions)

**SHOULD Requirements**:
- Endpoint baselines SHOULD specify browser configurations and security extensions
- Baselines SHOULD document VPN client requirements
- Baselines SHOULD define acceptable software installation policies

**MAY Requirements**:
- Organizations MAY use golden images for rapid endpoint provisioning
- Organizations MAY differentiate baselines by user role (executive, standard user, developer, etc.)

**Mobile Devices**:
- Mobile device baselines SHOULD leverage Mobile Device Management (MDM) policies
- Baselines SHOULD specify encryption, screen lock, remote wipe capabilities
- Baselines SHOULD define application whitelisting/blacklisting policies

### 2.1.3.4 Cloud Service Configurations

**MUST Requirements**:
- Cloud infrastructure (IaaS) baselines MUST be defined per service type:
  - Compute instances (EC2, Azure VMs, GCP Compute Engine)
  - Storage services (S3 buckets, Azure Blob, GCS buckets)
  - Network configurations (Security Groups, Network Security Groups, VPC Firewalls)
  - Identity and access management (IAM roles, policies, service principals)
- Cloud baselines MUST reference cloud security benchmarks (CIS AWS/Azure/GCP Benchmark, cloud provider security guides)

**SHOULD Requirements**:
- Cloud baselines SHOULD leverage Infrastructure as Code (Terraform, CloudFormation, ARM templates)
- Cloud baselines SHOULD include tagging standards for cost allocation and governance
- Cloud baselines SHOULD document backup and disaster recovery configurations
- Cloud baselines SHOULD specify logging and monitoring (CloudTrail, Azure Monitor, GCP Cloud Logging)

**Platform as a Service (PaaS)**:
- PaaS baselines (Azure App Services, AWS Lambda, etc.) SHOULD document:
  - Runtime versions
  - Environment variables
  - Scaling configurations
  - Integration points

**Software as a Service (SaaS)**:
- SaaS configuration baselines (Office 365, Salesforce, etc.) SHOULD document:
  - User and group configurations
  - Permission models
  - Security settings (MFA requirements, conditional access)
  - Data retention and compliance settings

### 2.1.3.5 Application Configurations

**MUST Requirements**:
- Business-critical applications MUST have documented configuration baselines
- Application baselines MUST include:
  - Application version and patch level
  - Installation parameters
  - Database connection strings (not credentials - see note below)
  - Integration endpoints and APIs
  - Security settings (authentication method, encryption, session management)
  - Performance settings (connection pools, timeouts, caching)

**SHOULD Requirements**:
- Application baselines SHOULD document environment-specific differences (prod vs. staging vs. dev)
- Baselines SHOULD specify backup and recovery procedures
- Baselines SHOULD document dependencies on other services

**Credentials Management Note**:
- Baselines MUST NOT contain actual credentials (passwords, API keys, tokens, certificates)
- Baselines SHOULD reference WHERE credentials are stored (key vault, secrets manager, privileged access management system)
- Baselines MAY document credential rotation policies

### 2.1.3.6 Database Configurations

**MUST Requirements**:
- Database server baselines MUST be defined separately from database instance configurations
- Database baselines MUST include:
  - Database version and edition
  - Security configurations (authentication methods, encryption in transit, encryption at rest)
  - Backup configurations (frequency, retention, location)
  - High-availability configurations (replication, clustering, failover)
  - Performance settings (memory allocation, connection limits, indexing strategy)
- Database baselines MUST reference database hardening guides (CIS, DISA STIG, vendor security guides)

**SHOULD Requirements**:
- Database baselines SHOULD document audit logging configurations
- Baselines SHOULD specify maintenance window settings
- Baselines SHOULD document data retention and archival policies

**MAY Requirements**:
- Organizations MAY use database-as-code approaches for schema and configuration management

---

## 2.1.4 Golden Image Requirements

### 2.1.4.1 Golden Image Purpose

**Definition**: A golden image is a pre-configured, tested, and approved template (virtual machine image, container image, or installation media) that embodies a baseline configuration and serves as the standard for deploying new instances.

**MUST Requirements**:
- Golden images MUST exist for all standard server and endpoint builds
- Golden images MUST be based on approved baseline configurations
- Golden images MUST be tested before approval for production use
- Golden images MUST be stored in secure, access-controlled repositories
- Golden images MUST be version-controlled with documented change history

**SHOULD Requirements**:
- Golden images SHOULD be updated quarterly (minimum) or when significant security updates occur
- Organizations SHOULD automate golden image creation and testing
- Golden images SHOULD include organizational management agents (monitoring, backup, etc.)

**MAY Requirements**:
- Organizations MAY use image factories or pipelines for automated golden image generation
- Organizations MAY differentiate golden images by workload type (web server, database, application server)

### 2.1.4.2 Image Creation Process

**MUST Requirements**:
- Golden image creation MUST follow documented procedures
- Images MUST be validated through:
  - Security scanning (vulnerability assessment, hardening compliance)
  - Functional testing (applications/services start correctly)
  - Integration testing (connectivity to network services)
  - Deployment testing (image can be deployed and boots successfully)
- Images MUST be approved by Configuration Manager and Security Operations before production use

**SHOULD Requirements**:
- Image creation SHOULD be automated where possible (Packer, image builder pipelines)
- Images SHOULD include only necessary software (minimal attack surface)
- Images SHOULD be built from trusted base images (official OS vendors, verified container registries)

**The Build vs. Buy Dilemma**:
- **Build**: Create images from scratch, full control, higher maintenance
- **Buy/Reuse**: Use vendor images with customization, faster deployment, dependency on vendor
- **Recommendation**: Start with vendor base images, apply organizational hardening, document customizations

### 2.1.4.3 Image Storage and Management

**MUST Requirements**:
- Golden images MUST be stored in repositories with:
  - Access controls (only authorized personnel can modify)
  - Version control (previous versions retained)
  - Integrity protection (checksums, digital signatures)
- Image repositories MUST be backed up

**SHOULD Requirements**:
- Image repositories SHOULD integrate with automated deployment tools
- Organizations SHOULD track image deployment statistics (how many instances deployed from each image)

**Recommended Repository Types**:
- **Virtual Machine Images**: VMware Content Library, Hyper-V Library, KVM image repository
- **Container Images**: Private Docker Registry, Harbor, Azure Container Registry, AWS ECR, GCP Artifact Registry
- **Cloud Images**: AWS AMI, Azure Managed Images, GCP Machine Images
- **Physical Server Images**: PXE boot servers, Windows Deployment Services (WDS), Cobbler

### 2.1.4.4 Image Update and Refresh

**MUST Requirements**:
- Golden images MUST be refreshed when:
  - Critical security vulnerabilities are patched
  - Baseline configurations are significantly updated
  - New versions of operating systems or applications are approved
- Image refresh frequency MUST NOT exceed 180 days (6 months)

**SHOULD Requirements**:
- Images SHOULD be refreshed quarterly
- Image refresh SHOULD be automated where possible
- Organizations SHOULD maintain 2-3 versions of each golden image (current, previous, emergency rollback)

**MAY Requirements**:
- Organizations MAY implement continuous image updates with automated testing pipelines

**Deprecation Process**:
- Outdated images MUST be marked as deprecated
- Deprecated images MUST NOT be used for new deployments
- Deprecated images MAY be retained for forensic or compliance purposes

---

## 2.1.5 Documentation Requirements

### 2.1.5.1 Configuration Parameters to Document

**MUST Requirements**:
- Baselines MUST document configuration parameters that affect:
  - **Security posture** (authentication, encryption, access controls)
  - **Compliance requirements** (audit logging, data retention, hardening controls)
  - **System functionality** (services, features, roles)
  - **Network connectivity** (IP addressing, routing, firewall rules)
  - **Monitoring and management** (agents, logging, SNMP)

**SHOULD Requirements**:
- Baselines SHOULD document:
  - **Performance settings** (memory allocation, connection limits, tuning parameters)
  - **High-availability configurations** (clustering, replication, failover)
  - **Backup and recovery settings**

**MAY Requirements**:
- Baselines MAY document application-specific configurations
- Baselines MAY include operational procedures (startup, shutdown, common maintenance tasks)

**Documentation Format**:
- Baselines MAY be documented as:
  - Structured documents (Word, Markdown, Wiki pages)
  - IaC code (Terraform, Ansible playbooks, CloudFormation templates)
  - Configuration management tool definitions (Puppet manifests, Chef recipes)
  - Spreadsheets (for simple inventories)
  - CMDB entries with configuration parameters

**The "Rebuild Test"**: Can someone use your baseline documentation to rebuild a system from scratch without asking you questions? If not, your documentation is incomplete.

### 2.1.5.2 Baseline Storage and Accessibility

**MUST Requirements**:
- Baseline documentation MUST be stored in centralized, accessible location(s)
- Access to baselines MUST be controlled (read access for operations, write access for authorized configuration managers)
- Baselines MUST be searchable (by asset type, operating system, role, etc.)
- Baselines MUST be backed up

**SHOULD Requirements**:
- Baselines SHOULD be integrated with the CMDB
- Baseline documentation SHOULD be in version-controlled repositories
- Organizations SHOULD maintain both human-readable documentation and machine-readable formats

**Recommended Storage Options**:
- CMDB/ITSM platforms (ServiceNow, BMC, Device42)
- Documentation wikis (Confluence, SharePoint, GitLab Wiki)
- Version control systems (Git, with Markdown documentation)
- IaC repositories (Git, with Terraform/Ansible code)
- Configuration management platforms (Puppet, Chef, Ansible Tower)

### 2.1.5.3 Baseline Review Frequency

**MUST Requirements**:
- All baselines MUST be reviewed at least annually
- Baselines for critical assets MUST be reviewed semi-annually (every 6 months)
- Baselines MUST be reviewed when:
  - Major security vulnerabilities are discovered affecting the baseline
  - Compliance requirements change (new regulations, updated standards)
  - Technology changes (OS upgrades, new versions)
  - Security incidents reveal baseline inadequacies

**SHOULD Requirements**:
- Baseline reviews SHOULD include:
  - Verification that baselines match production reality
  - Assessment of hardening compliance
  - Comparison to updated industry standards (new CIS Benchmark versions)
  - Stakeholder feedback (are baselines practical and usable?)
- Review outcomes SHOULD be documented

**Review Process**:
1. Configuration Manager schedules baseline review
2. Asset Owner and Technical Owner review baseline for accuracy
3. Security Operations reviews security configurations
4. Compliance Officer reviews regulatory alignment
5. Updates are proposed, reviewed, and approved
6. Baseline version incremented
7. Changes communicated to stakeholders

---

## 2.1.6 Infrastructure as Code (IaC) Integration

### 2.1.6.1 IaC as Configuration Documentation

**Philosophy**: Infrastructure as Code is not a separate domain - it's a METHOD of documenting and deploying configurations.

**MUST Requirements**:
- Organizations using IaC MUST treat IaC code as baseline documentation
- IaC repositories MUST be version-controlled (Git, etc.)
- IaC code MUST be reviewed before deployment (code review process)
- IaC deployments MUST be tested in non-production environments before production

**SHOULD Requirements**:
- IaC code SHOULD be modular and reusable (Terraform modules, Ansible roles, etc.)
- IaC SHOULD include automated testing (linting, syntax checking, security scanning)
- Organizations SHOULD document IaC code with inline comments and README files

**MAY Requirements**:
- Organizations MAY use CI/CD pipelines for automated IaC deployment
- Organizations MAY implement policy-as-code (Sentinel, Open Policy Agent) to enforce standards

### 2.1.6.2 Supported IaC Platforms

**Platform-Agnostic Principle**: This policy does not mandate specific IaC tools.

**Common IaC Tools** (examples, not requirements):
- **Terraform**: Multi-cloud infrastructure provisioning (declarative)
- **Ansible**: Configuration management and orchestration (declarative YAML)
- **Puppet**: Configuration management with agents (declarative DSL)
- **Chef**: Configuration management with agents (imperative Ruby DSL)
- **SaltStack**: Configuration management and orchestration (declarative YAML)
- **PowerShell DSC**: Windows configuration management (declarative)
- **CloudFormation**: AWS infrastructure (declarative JSON/YAML)
- **Azure Resource Manager (ARM)**: Azure infrastructure (declarative JSON)
- **Google Cloud Deployment Manager**: GCP infrastructure (declarative YAML)
- **Kubernetes**: Container orchestration with declarative manifests (YAML)

**Selection Criteria**: Choose tools based on organizational skill sets, technology stack, and operational requirements.

### 2.1.6.3 IaC Version Control

**MUST Requirements**:
- All IaC code MUST be stored in version control systems (Git, SVN, etc.)
- IaC commits MUST include meaningful commit messages describing changes
- IaC repositories MUST have access controls (who can commit, who can approve)
- IaC MUST have branching strategy (e.g., GitFlow: main/production, development, feature branches)

**SHOULD Requirements**:
- IaC changes SHOULD require peer review via pull requests / merge requests
- IaC SHOULD be tagged for releases (v1.0, v2.0, etc.)
- Organizations SHOULD maintain separate branches for environments (dev, staging, production)

**Integration with Change Management**:
- IaC deployments MUST follow change management procedures (see ISMS-POL-A.8.9-S2.2)
- IaC pull requests MAY serve as change requests for standard changes
- Production IaC deployments SHOULD be approved by CAB or delegated authority

---

## 2.1.7 Baseline Coverage Requirements

### 2.1.7.1 Coverage Targets

**MUST Requirements**:
- Organizations MUST achieve at least **80% baseline coverage** for critical and high-priority assets within 12 months of policy adoption
- Coverage MUST be tracked and reported quarterly

**SHOULD Requirements**:
- Organizations SHOULD target **100% baseline coverage** for critical assets
- Organizations SHOULD achieve **60% baseline coverage** for medium-priority assets within 18 months

**MAY Requirements**:
- Organizations MAY define baseline coverage targets for low-priority assets (development, test environments)

**Coverage Calculation**:
```
Baseline Coverage % = (Assets with Baselines / Total Assets in Scope) × 100
```

**Per-Category Tracking**: Calculate coverage separately for servers, network devices, endpoints, cloud services, etc.

### 2.1.7.2 Gap Analysis and Remediation

**MUST Requirements**:
- Organizations MUST conduct baseline coverage gap analysis at least quarterly
- Gaps MUST be documented with:
  - Asset identification (what's missing)
  - Risk assessment (why it matters)
  - Remediation plan (how to close the gap)
  - Target completion date
  - Responsible owner
- Critical asset gaps MUST be remediated within 90 days
- High-priority asset gaps MUST be remediated within 180 days

**SHOULD Requirements**:
- Gap analysis SHOULD prioritize assets by criticality and risk
- Remediation plans SHOULD be tracked in change management or project management systems
- Organizations SHOULD report gap closure progress monthly

**Acceptable Justifications for Gaps**:
- Asset scheduled for decommissioning within 90 days
- Temporary/short-lived asset (<30 days lifecycle)
- Exception approved per deviation procedures (ISMS-POL-A.8.9-S5.C)

---

**END OF DOCUMENT**