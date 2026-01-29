# ISMS-POL-A.8.31-S2.1
## Environment Separation - Environment Architecture Requirements

**Document ID**: ISMS-POL-A.8.31-S2.1  
**Title**: Environment Architecture Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / IT Architecture | Initial architecture requirements |

**Review Cycle**: Annual (or upon significant infrastructure changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: IT Operations Manager / Cloud Architect
- Development Review: DevOps Lead

**Distribution**: Security team, IT operations, cloud architects, system owners  
**Related Documents**: 
- ISMS-POL-A.8.31-S1 (Executive Summary & Control Alignment)
- ISMS-IMP-A.8.31-S1 (Architecture Implementation Guide)
- ISMS-POL-A.8.32 (Change Management)

---

## 2.1.1 Purpose and Scope

This section establishes **mandatory architecture requirements** for environment separation. These requirements define HOW environments must be separated technically to achieve the control objectives of A.8.31.

**In Scope**: Technical architecture mechanisms for environment isolation  
**Primary Stakeholder**: IT Operations, Cloud Architecture, DevOps  
**Implementation Evidence**: ISMS-IMP-A.8.31-S1 (Architecture Assessment)

---

## 2.1.2 Environment Definition Requirements

### 2.1.2.1 Minimum Environment Tiers

[Organization] **SHALL** maintain at minimum the following environment tiers for all systems in scope:

**Mandatory Environment Tiers**:

1. **Development Environment**
   - **Purpose**: Active code development, experimentation
   - **Minimum Separation**: Network isolation OR access control isolation
   - **Data Restriction**: Production data PROHIBITED (see S2.3)
   - **Availability Target**: Best effort (downtime acceptable for maintenance)

2. **Testing/QA Environment**
   - **Purpose**: Quality assurance, integration testing, UAT
   - **Minimum Separation**: Network isolation AND access control isolation
   - **Data Restriction**: Production data PROHIBITED unless anonymized (see S2.3)
   - **Availability Target**: 95% during business hours

3. **Production Environment**
   - **Purpose**: Live operations serving customers
   - **Minimum Separation**: Network isolation AND infrastructure isolation AND access control isolation
   - **Data Restriction**: Production data ONLY (no test data mixing)
   - **Availability Target**: Per SLA (typically 99.5%+)

**Optional but Recommended**:

4. **Staging/Pre-Production Environment**
   - **Purpose**: Production-equivalent final validation
   - **Separation**: Should mirror production isolation mechanisms
   - **Benefit**: Reduces production incidents from untested changes

**Audit Verification Criteria**:
- ✅ Documentation exists defining all environment tiers
- ✅ Each environment has documented purpose and separation mechanisms
- ✅ Environment inventory maintained and current

### 2.1.2.2 Environment Naming and Identification

[Organization] **SHALL** implement consistent environment naming to prevent confusion and misidentification:

**Naming Standards**:
- Environment names clearly distinguish environment type (e.g., "dev-", "test-", "prod-")
- Hostnames, DNS records, cloud account names include environment identifier
- Application URLs include environment subdomain (dev.app.example.com, test.app.example.com, app.example.com)
- Database names include environment prefix (dev_database, test_database, prod_database)

**Visual Identification** (STRONGLY RECOMMENDED):
- Different color schemes per environment in admin interfaces (e.g., production = red banner)
- Warning banners in production systems ("PRODUCTION ENVIRONMENT - Changes affect live users")
- Browser extensions or profiles for environment identification

**Audit Verification Criteria**:
- ✅ Environment naming standard documented
- ✅ Sample hostnames/URLs demonstrate environment identification
- ✅ Visual identification implemented for production

---

## 2.1.3 Network Separation Requirements

### 2.1.3.1 Network Segmentation

[Organization] **SHALL** implement network segmentation to isolate environments from each other:

**Network Isolation Mechanisms** (choose appropriate to infrastructure):

**On-Premises / Data Center**:
- Separate VLANs per environment tier
- Routing policies restrict inter-environment communication
- Firewall rules between environments (default deny)
- Physical network separation for highly sensitive systems (optional)

**Cloud Infrastructure**:
- Separate Virtual Private Clouds (VPCs) per environment (AWS)
- Separate Virtual Networks (VNets) per environment (Azure)
- Separate VPC networks per environment (GCP)
- VPC peering disabled between non-adjacent environments (dev CANNOT peer with prod)

**Hybrid/Multi-Cloud**:
- Each environment exists in separate network context
- Network connectivity between environments prohibited (except controlled promotion pipelines)
- VPN/ExpressRoute/Direct Connect separate per environment

**Audit Verification Criteria**:
- ✅ Network diagram shows environment segmentation
- ✅ VLAN/VPC/VNet configuration reviewed for separation
- ✅ Firewall rules prevent unauthorized inter-environment traffic
- ✅ Penetration test confirms network isolation

### 2.1.3.2 Firewall and Security Group Rules

[Organization] **SHALL** implement network access controls between environments:

**Default Deny Principle**:
- Default firewall/security group rule: **DENY ALL** between environments
- Explicit allow rules ONLY for authorized traffic (e.g., deployment pipelines)
- No direct developer access from workstation to production network

**Permitted Inter-Environment Traffic** (examples of allowed exceptions):
- Deployment pipeline from CI/CD server to staging/production (specific ports, specific source IPs)
- Monitoring system read-only access to all environments (port 9090/Prometheus, 514/syslog)
- Backup system access to all environments for data protection
- Centralized logging (log forwarding from all envs to SIEM)

**PROHIBITED Inter-Environment Traffic**:
- Development workstations → Production network (no direct access)
- Testing environment → Production database (no direct connection)
- Production → Development (no reverse traffic except monitoring)

**Audit Verification Criteria**:
- ✅ Firewall rule review shows default deny between environments
- ✅ Allowed traffic documented with business justification
- ✅ Quarterly firewall rule review conducted
- ✅ Unauthorized traffic attempts logged and alerted

---

## 2.1.4 Infrastructure Separation Requirements

### 2.1.4.1 Compute Resource Separation

[Organization] **SHALL** dedicate computing resources per environment to prevent resource sharing and unauthorized access:

**Physical Servers / Virtual Machines**:
- Separate physical servers per environment tier (where feasible)
- Separate VM clusters per environment (VMware resource pools, Hyper-V clusters)
- No VM migration between environment clusters
- Hypervisor-level isolation for high-security systems

**Cloud Infrastructure**:
- **AWS**: Separate AWS accounts per environment (using AWS Organizations)
  - Production account(s) in separate organizational unit
  - Consolidated billing acceptable, but resource isolation maintained
  - Cross-account access ONLY via IAM roles (no shared credentials)
- **Azure**: Separate Azure subscriptions per environment
  - Production subscription in separate management group
  - Resource sharing prohibited (no shared resource groups)
- **GCP**: Separate GCP projects per environment
  - Production projects in separate folder hierarchy
  - Service account sharing prohibited

**Container Orchestration**:
- **Kubernetes**: Separate clusters per environment (RECOMMENDED)
  - If shared cluster necessary (cost constraints), use separate namespaces with NetworkPolicies
  - Production namespace isolation enforced (no pod-to-pod traffic from non-prod namespaces)
  - Resource quotas per namespace to prevent resource exhaustion
- **Docker Swarm / ECS / AKS**: Separate orchestrator per environment

**Serverless / FaaS**:
- Separate function deployment per environment
- Environment variables differentiate environment
- Production function IAM roles separate from dev/test

**Audit Verification Criteria**:
- ✅ Infrastructure inventory shows resource separation per environment
- ✅ Cloud accounts/subscriptions/projects separate per environment
- ✅ Kubernetes namespaces (if used) enforce isolation via NetworkPolicies
- ✅ No shared compute resources between production and non-production

### 2.1.4.2 Storage and Data Separation

[Organization] **SHALL** separate data storage per environment (detailed data handling in S2.3):

**Database Separation**:
- Separate database instances per environment
- No shared database servers between production and non-production
- Database credentials unique per environment (no shared passwords)
- Production database backups stored separately from dev/test backups

**File Storage / Object Storage**:
- Separate file shares per environment (NFS, SMB/CIFS, object storage buckets)
- AWS S3: Separate buckets per environment (no cross-environment bucket access)
- Azure Blob Storage: Separate storage accounts per environment
- GCP Cloud Storage: Separate buckets per environment

**Backup and Recovery**:
- Production backups encrypted and stored with higher security controls
- Development/test backups (if taken) stored separately
- Production backup restoration tested in isolated recovery environment (not dev/test)

**Audit Verification Criteria**:
- ✅ Database inventory shows separate instances per environment
- ✅ Storage buckets/shares separate per environment
- ✅ Production data not accessible from dev/test environments (see S2.3 for data handling)
- ✅ Backup storage segregated by environment

---

## 2.1.5 Credential and Secrets Separation

### 2.1.5.1 Credential Isolation

[Organization] **SHALL** implement separate credentials per environment to prevent credential sharing:

**Password and Key Separation**:
- Production passwords/keys NEVER used in development or testing
- Database passwords unique per environment
- API keys separate per environment (dev keys, test keys, prod keys)
- SSH keys separate per environment (no shared private keys)
- Service account credentials unique per environment

**Secret Management Systems**:
- Production secrets stored in PAM vault or secret management system (Vault, AWS Secrets Manager, Azure Key Vault, CyberArk)
- Development/test secrets may use lighter-weight secret management (but never shared with production)
- Secrets rotation automated per environment

**Hardcoded Credential Prohibition**:
- No credentials hardcoded in source code (enforced via pre-commit hooks)
- No production credentials in configuration files committed to version control
- Environment variables or secret management for credential injection

**Audit Verification Criteria**:
- ✅ Credential inventory shows separate credentials per environment
- ✅ Production credentials stored in PAM/secret management system
- ✅ Code scans show no hardcoded credentials
- ✅ Credential rotation schedule documented and followed

---

## 2.1.6 Configuration Management

### 2.1.6.1 Environment-Specific Configuration

[Organization] **SHALL** maintain separate configurations per environment:

**Configuration Separation Mechanisms**:
- Environment-specific configuration files (application.dev.properties, application.prod.properties)
- Configuration management systems (Chef, Puppet, Ansible) with environment-specific cookbooks/playbooks
- Environment variables injected at runtime (12-factor app methodology)
- Configuration stored in version control with environment branching/tagging

**Configuration Validation**:
- Automated validation that production configuration not deployed to dev/test
- Configuration schema validation before deployment
- Configuration change approval required for production

**Sensitive Configuration**:
- Database connection strings environment-specific
- API endpoints environment-specific (no prod API calls from dev)
- Feature flags per environment (enable beta features in dev, disable in prod)

**Audit Verification Criteria**:
- ✅ Configuration management process documented
- ✅ Configuration files show environment separation
- ✅ Automated validation prevents config misdeployment
- ✅ Production configuration changes tracked and approved

---

## 2.1.7 Measurable Compliance Criteria

For audit and compliance verification, [Organization] must demonstrate:

**Architecture Compliance Metrics**:
- **100%** of in-scope systems have documented environment architecture
- **0** network connections from development to production (except authorized deployment pipelines)
- **0** shared credentials between production and non-production environments
- **100%** of production systems in separate cloud accounts/subscriptions (if cloud-based)
- **100%** of environments have separate databases/storage
- **≤ 5%** configuration drift between staging and production (measured monthly)
- **100%** of deployment pipelines enforce environment validation

**Verification Methods**:
- Quarterly infrastructure reviews
- Network penetration testing (annual)
- Cloud configuration scanning (automated, continuous)
- Credential audit (semi-annual)
- Deployment pipeline audit (quarterly)

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | [Name] | ________________ | [Date] |
| IT Operations Manager | [Name] | ________________ | [Date] |
| Cloud Architect | [Name] | ________________ | [Date] |
| Information Security Manager | [Name] | ________________ | [Date] |

---

*End of Document ISMS-POL-A.8.31-S2.1*
