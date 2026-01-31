# ISMS-POL-A.8.9-S1
## Configuration Management - Purpose, Scope, Definitions

**Document ID**: ISMS-POL-A.8.9-S1  
**Title**: Configuration Management - Purpose, Scope, Definitions  
**Version**: 1.0  
**Date**: [Date] 
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]| Information Security Manager | Initial foundational document |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: 07.01.2027  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Information Security Manager / Configuration Manager
- Operations Review: Chief Technology Officer (CTO) / IT Director
- Compliance Review: Legal/Compliance Officer

**Distribution**: Security team, IT operations, system administrators, DevOps engineers, configuration management team  
**Related Documents**: ISMS-POL-A.8.9 (Master), ISO/IEC 27001:2023 A.8.9, ITIL 4 Service Configuration Management

---

## 1.1 Purpose

### 1.1.1 Policy Objective

This document establishes the purpose, scope, and key definitions for the organization's Configuration Management policy framework, implementing ISO/IEC 27001:2023 Annex A Control 8.9 (Configuration Management).

The policy framework aims to:

- **Establish** secure baseline configurations for all IT assets across the organization
- **Prevent** unauthorized or undocumented changes that could introduce security vulnerabilities
- **Detect** configuration drift from approved baselines through continuous monitoring
- **Enforce** security hardening standards aligned with industry best practices
- **Enable** rapid recovery and system restoration through documented configurations
- **Support** audit, compliance, and forensic investigations with configuration evidence
- **Balance** security requirements with operational flexibility and business needs

### 1.1.2 Control Alignment

This policy implements ISO/IEC 27001:2023 Annex A.8.9:

> **A.8.9 Configuration Management**  
> *"Configurations, including security configurations, of hardware, software, services and networks shall be established, documented, implemented, monitored and reviewed."*

**German (Original):**
> *"Konfigurationen, einschließlich Sicherheitskonfigurationen, von Hardware, Software, Diensten und Netzwerken müssen festgelegt, dokumentiert, umgesetzt, überwacht und überprüft werden."*

The control recognizes that poorly managed configurations expose organizations to significant risks including:
- Unauthorized changes introducing vulnerabilities or backdoors
- Configuration drift leading to inconsistent security postures
- Lack of baseline knowledge preventing effective incident response
- Inability to recover systems due to undocumented configurations
- Compliance failures due to missing hardening controls
- Shadow IT emerging when change processes are too cumbersome
- Operational instability from uncontrolled changes

### 1.1.3 Risk Management Context

Configuration management serves as a **foundational control** within the organization's layered security architecture. Proper configuration management:

**Reduces Attack Surface**:
- Hardened configurations eliminate unnecessary services and features
- Secure defaults prevent exploitation of known vulnerabilities
- Consistent configurations reduce complexity and attack vectors

**Enables Detection & Response**:
- Baseline knowledge allows identification of unauthorized changes
- Configuration logs support forensic investigations
- Known configurations enable rapid incident containment

**Supports Recovery**:
- Documented baselines enable system restoration
- Golden images accelerate redeployment
- Configuration backups reduce recovery time objectives (RTOs)

**Maintains Compliance**:
- Hardening standards align with regulatory requirements (PCI DSS, HIPAA, etc.)
- Configuration evidence satisfies audit requirements
- Change records demonstrate control effectiveness

**The Feynman Test**: *"If you can't explain your server's configuration in simple terms, you don't understand it well enough to secure it."*

The organization recognizes that configuration management must balance security rigor with operational agility. Overly bureaucratic change processes drive shadow IT, while insufficient controls create chaos. This framework seeks the optimal balance.

---

## 1.2 Scope

### 1.2.1 In Scope

This policy framework applies to:

#### Asset Types

**Compute & Infrastructure**:
- Physical servers (Windows Server, Linux/Unix, proprietary systems)
- Virtual machines (VMware, Hyper-V, KVM, Xen, etc.)
- Containers (Docker, Kubernetes pods, container images)
- Hypervisors and virtualization platforms
- Endpoints (workstations, laptops, thin clients, VDI desktops)
- Mobile devices (smartphones, tablets under MDM control)

**Network & Connectivity**:
- Network devices (routers, switches, wireless controllers)
- Security appliances (firewalls, IDS/IPS, web proxies, email gateways)
- Load balancers and application delivery controllers
- VPN concentrators and remote access gateways
- Network services (DNS, DHCP, NTP servers)

**Storage & Backup**:
- Storage systems (SAN, NAS, object storage)
- Storage arrays (block storage, file storage)
- Backup systems (backup servers, tape libraries, backup appliances)
- Replication systems and disaster recovery infrastructure

**Cloud & SaaS**:
- Cloud infrastructure (AWS EC2, Azure VMs, GCP Compute Engine, etc.)
- Cloud platform services (Azure App Services, AWS Lambda, GCP App Engine)
- Cloud storage (S3, Azure Blob, GCS buckets)
- SaaS application configurations (Office 365, Salesforce, ServiceNow settings)
- Cloud networking (security groups, VPCs, Azure NSGs)

**Applications & Middleware**:
- Web servers (Apache, Nginx, IIS, etc.)
- Application servers (Tomcat, JBoss, WebSphere, WebLogic, etc.)
- Databases (SQL Server, Oracle, PostgreSQL, MySQL, MongoDB, Redis, etc.)
- Middleware (message queues, ESB, integration platforms)
- Development tools (CI/CD pipelines, artifact repositories, source control servers)

**Security & Identity**:
- Identity systems (Active Directory, LDAP, Azure AD, Okta)
- Authentication systems (SSO, MFA platforms)
- Certificate services (PKI, CA servers, certificate management)
- SIEM and logging platforms
- DLP systems (Data Loss Prevention configurations)
- Vulnerability scanners (configuration, not scan results)

**IoT & Operational Technology**:
- Building management systems (HVAC, access control, surveillance)
- Industrial control systems (SCADA, PLC, industrial networks)
- IoT devices (sensors, smart devices, embedded systems)
- OT network infrastructure

**Business Services**:
- Business applications (ERP, CRM, financial systems)
- Collaboration platforms (email servers, SharePoint, Teams, Zoom)
- HR systems and payroll platforms
- Document management systems

#### Configuration Aspects

**System Configurations**:
- Operating system settings and parameters
- Security configurations (authentication, authorization, encryption)
- Network configurations (IP addressing, routing, VLANs)
- Service settings (enabled/disabled services, startup types)
- Patch levels and software versions
- Installed software and components

**Application Configurations**:
- Application settings and parameters
- Database configurations
- Integration and API settings
- Performance tuning parameters
- Logging and monitoring settings

**Security Hardening**:
- Security baselines (CIS Benchmarks, DISA STIGs, vendor guides)
- Access controls and permissions
- Encryption settings
- Audit configurations
- Account policies (password, lockout, etc.)

**Documentation References** (NOT storage of sensitive data):
- Service account references (accounts are stored in privileged access management systems, NOT in configuration documentation)
- Credential types and authentication methods (NOT actual credentials)
- Certificate purposes and expiration tracking (NOT private keys)
- Integration points and dependencies

#### Lifecycle Phases

This framework applies across the entire asset lifecycle:
- **Design**: Baseline definition, hardening standard selection
- **Deployment**: Golden image creation, initial provisioning
- **Operations**: Day-to-day configuration management, change control
- **Maintenance**: Patching, updates, configuration reviews
- **Decommissioning**: Configuration archival, secure disposal

#### Geographic & Organizational Scope

- **All organizational entities**: Headquarters, branch offices, remote sites, cloud regions
- **All geographic locations**: Switzerland, EU, international offices (where organization operates)
- **Third-party managed environments**: Where contractually obligated or risk-assessed as necessary

### 1.2.2 Out of Scope

The following are **explicitly excluded** from this policy:

**User Data & Content**:
- End-user documents, files, and personal data
- Application data and databases (content, not configuration)
- User-generated content in business systems

**Development & Testing Code**:
- Application source code (covered by secure development lifecycle policies)
- Development environment sandboxes (unless promoted to production-equivalency)
- Proof-of-concept and experimental systems (unless containing production data)

**Temporary Systems**:
- Short-lived test environments (<7 days)
- Disposable containers that are never promoted beyond development
- Ephemeral compute instances used for batch processing only

**External Services** (except configuration integration points):
- Third-party SaaS platforms where organization has no configuration control
- Public internet services
- Vendor-managed platforms where configuration responsibility is contractually excluded

**Credentials & Secrets** (managed separately):
- Passwords, API keys, tokens (managed by privileged access management systems)
- Private keys and certificates (managed by PKI and secret management systems)
- Encryption keys (managed by key management systems)
  
**Note**: While credentials themselves are out of scope, the *references* to credential requirements and authentication methods ARE in scope for configuration documentation.

### 1.2.3 Technology Neutrality Statement

This policy framework is **vendor-agnostic and technology-neutral**. Requirements are defined as **capabilities**, not specific products or platforms.

**Vendor-Neutral Principle**:
- "Organizations SHALL maintain a Configuration Management Database (CMDB)" ✅
- "Organizations SHALL deploy ServiceNow CMDB" ❌

Organizations may use:
- Commercial platforms (ServiceNow, BMC, Jira, etc.)
- Open-source tools (Ansible, Terraform, OSSEC, etc.)
- Cloud-native services (AWS Config, Azure Policy, GCP Security Command Center)
- Custom or homegrown solutions
- Hybrid approaches combining multiple tools

**Rationale**: Technology landscapes evolve. Vendor lock-in at the policy level creates unnecessary rigidity. Policy defines "what" must be achieved (capability), not "how" it is achieved (specific tool).

### 1.2.4 Infrastructure as Code (IaC) Applicability

Organizations increasingly manage configurations using Infrastructure as Code approaches. This framework treats IaC as a **configuration documentation and deployment method**, fully in scope:

**IaC Platforms Supported** (examples, not prescriptive):
- Terraform, Ansible, Puppet, Chef, SaltStack
- CloudFormation, Azure Resource Manager, Google Cloud Deployment Manager
- Kubernetes manifests, Helm charts
- PowerShell DSC (Desired State Configuration)

**IaC Integration**:
- IaC code repositories serve as configuration baselines
- Version control systems (Git, etc.) provide change tracking
- CI/CD pipelines execute change management workflows
- IaC testing validates configurations before deployment

**Hybrid Environments**: Many organizations use both traditional and IaC approaches. The framework accommodates mixed environments.

---

## 1.3 Definitions

### 1.3.1 Core Configuration Management Terms

**Configuration Management (CM)**  
The process of establishing and maintaining the consistency of an asset's performance, functional, and physical attributes with its requirements, design, and operational information throughout its lifecycle.

**Configuration Item (CI)**  
A uniquely identifiable component of the IT infrastructure that is under configuration management control. CIs include hardware, software, services, documentation, and relationships.

**Configuration Baseline**  
An approved and documented configuration specification for a CI or set of CIs at a specific point in time. Baselines serve as the reference point for change control and compliance verification.

**Golden Image**  
A pre-configured, tested, and approved template for an operating system or application that serves as the standard for deploying new instances. Golden images embody baseline configurations.

**Configuration Management Database (CMDB)**  
A repository that stores information about CIs, their attributes, relationships, and lifecycle status. The CMDB is the authoritative source for configuration data.

**Configuration Management System (CMS)**  
The set of tools, processes, and databases used to manage configurations. Includes the CMDB plus supporting processes, workflows, and automation.

### 1.3.2 Change Management Terms

**Change Control**  
The process of controlling modifications to configurations through formal request, approval, implementation, and validation procedures.

**Change Advisory Board (CAB)**  
A group of stakeholders responsible for reviewing, assessing, and approving or rejecting proposed changes based on risk, impact, and business value.

**Standard Change**  
A pre-approved change that is low-risk, well-understood, and follows a documented procedure. Standard changes do not require CAB approval for each instance.

**Normal Change**  
A change that requires CAB review and approval before implementation due to risk, complexity, or organizational impact.

**Emergency Change**  
A change required urgently to resolve a critical incident or security vulnerability. Emergency changes follow expedited approval processes with retrospective CAB review.

**Change Window**  
A pre-scheduled time period during which changes may be implemented with minimal impact to business operations.

**Rollback**  
The process of reverting a system to its previous configuration if a change causes problems or does not achieve desired outcomes.

**Change Success Rate**  
The percentage of implemented changes that do not require rollback or cause unplanned incidents. Key performance indicator for change management effectiveness.

### 1.3.3 Monitoring & Compliance Terms

**Configuration Drift**  
Deviation of an actual configuration from its approved baseline. Drift may be authorized (pending change approval) or unauthorized (security incident).

**Drift Detection**  
The process of identifying configuration changes that differ from approved baselines through automated scanning or manual auditing.

**Compliance Scanning**  
Automated assessment of system configurations against security hardening standards (CIS Benchmarks, DISA STIGs, etc.) to identify non-compliant settings.

**Security Hardening**  
The process of reducing a system's attack surface by disabling unnecessary services, applying secure settings, and implementing defense-in-depth configurations.

**Security Baseline**  
A minimum set of security configurations required for an asset type. Often based on industry standards (CIS, STIG) or vendor security guides.

**File Integrity Monitoring (FIM)**  
Technology that detects unauthorized changes to critical files and configurations by monitoring file attributes (checksums, timestamps, permissions).

**Configuration Audit**  
Formal review of configurations to verify compliance with baselines, hardening standards, and organizational policies.

### 1.3.4 Infrastructure as Code Terms

**Infrastructure as Code (IaC)**  
The practice of managing and provisioning infrastructure through machine-readable definition files rather than manual processes or interactive configuration tools.

**Declarative Configuration**  
Configuration specification that describes the desired end state (what should exist) rather than the steps to achieve it (how to build it). Terraform and Ansible YAML are declarative.

**Imperative Configuration**  
Configuration specification that describes the sequence of steps to execute. Shell scripts and procedural code are imperative.

**Configuration as Code (CaC)**  
Similar to IaC but specifically refers to managing system and application configurations (not just infrastructure) through code.

**Desired State Configuration (DSC)**  
A management platform (particularly PowerShell DSC) that enables declarative configuration management for Windows systems.

**Idempotency**  
The property that applying the same configuration multiple times produces the same result as applying it once. Critical for reliable automation.

**Configuration Drift Remediation**  
Automated or manual process of restoring configurations to their desired state when drift is detected.

### 1.3.5 Hardening & Standards Terms

**CIS Benchmarks**  
Configuration hardening standards developed by the Center for Internet Security (CIS) covering 100+ technologies. Two levels: Level 1 (basic hardening) and Level 2 (advanced hardening).

**DISA STIG**  
Security Technical Implementation Guide published by the US Defense Information Systems Agency. Mandatory for US DoD systems, often adopted by defense contractors and federal agencies.

**STIG Viewer / SCAP Compliance Checker (SCC)**  
Tools for validating compliance with DISA STIGs through automated scanning.

**SCAP (Security Content Automation Protocol)**  
Suite of specifications for expressing and manipulating security data in standardized ways. Enables automated vulnerability assessment and configuration compliance checking.

**XCCDF (Extensible Configuration Checklist Description Format)**  
XML-based language for defining security checklists and benchmarks. Used by CIS, DISA, and NIST for machine-readable hardening standards.

**OVAL (Open Vulnerability and Assessment Language)**  
Language for encoding system details and assessing system state. Used within SCAP for compliance checking.

**CIS-CAT (Configuration Assessment Tool)**  
Automated tool for assessing compliance with CIS Benchmarks. Available in free and commercial (Pro) versions.

**Microsoft Security Baselines**  
Official security configuration recommendations from Microsoft for Windows, Office 365, Azure, and other Microsoft products.

**Vendor Security Hardening Guide**  
Official configuration security recommendations provided by technology vendors (Cisco, VMware, Oracle, etc.).

### 1.3.6 Asset Classification Terms

**Asset Criticality**  
Classification of an asset's importance to business operations. Typical levels: Critical, High, Medium, Low. Determines configuration management rigor.

**Asset Type**  
Category of asset (server, network device, database, application, etc.). Determines applicable baseline and hardening standards.

**Asset Owner**  
Individual or team accountable for an asset's security, compliance, and operational requirements. Responsible for approving configuration changes.

**System Owner**  
Individual responsible for a logical system or application consisting of multiple assets. Coordinates configuration management across related CIs.

**Technical Owner**  
Individual or team responsible for day-to-day technical management of an asset. Implements configuration changes per approved procedures.

### 1.3.7 Compliance & Audit Terms

**Configuration Evidence**  
Documented proof of configuration state, typically including:
- Baseline documentation
- Change records
- Scan results (hardening compliance, drift detection)
- Approval records
- Audit logs

**Evidence Register**  
Structured log of evidence collected during configuration assessments. Each assessment workbook includes a 100-row evidence register.

**Configuration Assessment**  
Formal evaluation of configuration management implementation effectiveness. This framework includes 5 domain-specific assessments.

**Configuration Compliance**  
Measure of alignment between actual configurations and required baselines/standards. Expressed as percentage (e.g., "87% compliant with CIS Level 1").

**Gap Analysis**  
Identification of differences between current state (actual configurations) and target state (required baselines). Includes risk assessment and remediation planning.

**Compensating Control**  
Alternative control implemented when standard configuration cannot be applied due to technical or business constraints. Must provide equivalent risk mitigation.

### 1.3.8 Technology-Specific Terms

**Cloud Service Configuration**  
Settings and parameters for cloud services (AWS, Azure, GCP) including compute, storage, networking, identity, and security controls.

**Container Image**  
Package containing application code, runtime, libraries, and configurations. Container images are CIs requiring baseline management and hardening.

**Kubernetes Manifest**  
YAML or JSON file defining desired state for Kubernetes resources (pods, services, deployments). Treated as IaC for configuration management purposes.

**Network Device Configuration**  
Settings and parameters for routers, switches, firewalls, and other network infrastructure. Often managed via CLI, SNMP, or network management platforms.

**Database Configuration**  
Database server settings (not data) including security, performance, backup, and operational parameters.

---

## 1.4 Control Principles

### 1.4.1 Defense in Depth

Configuration management is ONE layer in a defense-in-depth strategy. It works alongside:
- Vulnerability management (patching systems)
- Access management (controlling who can change configurations)
- Network security (limiting attack paths)
- Monitoring & logging (detecting anomalies)
- Incident response (reacting to configuration-related incidents)

**Anti-Pattern**: Assuming hardened configurations alone prevent all attacks. They reduce attack surface but do not eliminate risk.

### 1.4.2 Least Privilege Principle

Apply least privilege to configuration management:
- Limit who can modify configurations
- Separate read vs. write access to CMDB
- Require approval for high-risk changes
- Use service accounts with minimal necessary permissions
- Audit privileged configuration changes

### 1.4.3 Separation of Duties

Prevent single points of failure and fraud:
- Change requesters should not approve their own changes
- Configuration implementers should not be sole approvers
- Auditors should be independent from implementation teams
- CAB membership should include diverse stakeholders

### 1.4.4 Auditability & Traceability

Every configuration change must be traceable:
- **What** changed (configuration parameters modified)
- **Who** made the change (identity and authorization)
- **When** the change occurred (timestamp)
- **Why** the change was made (change request, approval, justification)
- **How** the change was implemented (procedure, rollback plan)

**The Feynman Audit**: *"If you can't explain exactly when and why your firewall ruleset changed, you have a problem."*

### 1.4.5 Business Continuity Alignment

Configuration management supports business continuity:
- Baselines enable rapid system recovery
- Golden images reduce RTO (Recovery Time Objectives)
- Configuration backups support disaster recovery
- Documented dependencies support impact analysis
- Change windows minimize business disruption

---

## 1.5 Policy Interpretation

### 1.5.1 Requirement Levels

This framework uses **RFC 2119** terminology for requirement levels:

**MUST / SHALL / REQUIRED**: Absolute requirement. Non-compliance is a policy violation.  
**SHOULD / RECOMMENDED**: Strong recommendation. Deviations require documented justification and risk acceptance.  
**MAY / OPTIONAL**: Permitted but not required. Organization decides based on risk appetite.

**Example**:
- "All production servers MUST have documented baseline configurations" (mandatory)
- "Organizations SHOULD implement automated drift detection" (recommended but exceptions allowed)
- "Organizations MAY use Infrastructure as Code for configuration management" (optional approach)

### 1.5.2 Exception Handling Philosophy

Not all baseline requirements can be met immediately or universally. The framework includes exception management:

**Valid Exception Scenarios**:
- Technical incompatibility (legacy systems that cannot meet current hardening standards)
- Business constraints (third-party application requiring non-standard configuration)
- Risk-based decisions (accepting residual risk with compensating controls)
- Transition periods (migrating to new baseline over defined timeframe)

**Invalid Exception Scenarios**:
- "Too much work" (resource constraints are implementation challenges, not exceptions)
- "We've always done it this way" (inertia is not justification)
- Convenience or personal preference
- Lack of understanding (training need, not exception)

**Exception Process**: See ISMS-POL-A.8.9-S5.C (Configuration Deviation Procedures)

### 1.5.3 Progressive Implementation

Organizations may implement this framework progressively:

**Phase 1 (Foundational)**: Critical assets, high-risk systems, internet-facing infrastructure  
**Phase 2 (Expansion)**: Internal servers, databases, network core  
**Phase 3 (Comprehensive)**: Endpoints, branch offices, cloud services  
**Phase 4 (Optimization)**: IoT/OT, development environments, automation

**Rationale**: Attempting to baseline 1000 servers on day one creates burnout and cargo cult compliance. Start with crown jewels, prove value, expand systematically.

---

## 1.6 Framework Adoption

### 1.6.1 For New Organizations

Organizations implementing configuration management for the first time:

1. **Asset Inventory**: Identify what exists (CMDB or discovery tools)
2. **Prioritization**: Classify by criticality and risk
3. **Baseline Definition**: Start with CIS Level 1 or vendor guides
4. **Pilot Phase**: Implement for 5-10 representative systems
5. **Lessons Learned**: Refine baselines based on pilot
6. **Phased Rollout**: Expand per progressive implementation approach
7. **Continuous Improvement**: Quarterly reviews, metric-driven optimization

### 1.6.2 For Existing Configuration Management

Organizations with existing configuration management processes:

1. **Gap Assessment**: Compare current state to framework requirements
2. **Evidence Collection**: Document what already exists
3. **Process Alignment**: Map existing processes to framework domains
4. **Tool Integration**: Integrate existing tools into assessment workbooks
5. **Standardization**: Harmonize inconsistent baseline approaches
6. **Optimization**: Leverage automation, eliminate redundancy
7. **Documentation**: Formalize tribal knowledge into baselines

**Avoid**: Throwing away working processes to conform to framework. Adapt framework to organizational context while meeting control objectives.

---

## 1.7 Relationship to Other ISMS Controls

Configuration management intersects with multiple ISO 27001 controls:

**A.8.1 (User Endpoint Devices)**: Endpoint configurations managed per baselines  
**A.8.2 (Privileged Access Rights)**: Access to configuration management systems restricted  
**A.8.3 (Information Access Restriction)**: CMDB access controls align with data classification  
**A.8.8 (Management of Technical Vulnerabilities)**: Patching updates configurations  
**A.8.10 (Information Deletion)**: Asset decommissioning includes configuration archival  
**A.8.16 (Monitoring Activities)**: Configuration changes logged and monitored  
**A.8.20 (Networks Security)**: Network device configurations managed per baselines  
**A.8.23 (Web Filtering)**: Web proxy configurations managed per baselines  

---

**END OF DOCUMENT**