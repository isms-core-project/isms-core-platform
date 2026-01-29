# ISMS-POL-A.8.31-Annex-A
## Environment Separation - Environment Architecture Patterns

**Document ID**: ISMS-POL-A.8.31-Annex-A  
**Title**: Environment Architecture Patterns  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## A.1 Purpose

This annex provides **technology-specific implementation patterns** for environment separation across common infrastructure platforms. These patterns illustrate HOW to implement the technology-agnostic requirements from S2.1.

**Important**: These are EXAMPLES only. Organizations implement environment separation using their chosen platforms. The REQUIREMENT is environment separation; the IMPLEMENTATION varies by technology.

---

## A.2 AWS (Amazon Web Services) Multi-Account Pattern

### A.2.1 Architecture Overview

**AWS Organizations Structure**:
```
Root Organization
├── Security OU (Organizational Unit)
│   ├── Audit Account (logging, compliance)
│   └── Security Tooling Account (GuardDuty, SecurityHub)
├── Development OU
│   ├── Dev Account 1 (App Team A - Development)
│   ├── Dev Account 2 (App Team B - Development)
│   └── Shared Dev Services (DevOps tools)
├── Testing OU
│   ├── Test Account 1 (App Team A - Testing)
│   ├── Test Account 2 (App Team B - Testing)
│   └── Shared Test Services (QA tools)
├── Staging OU
│   ├── Staging Account 1 (App Team A - Pre-Prod)
│   └── Staging Account 2 (App Team B - Pre-Prod)
└── Production OU
    ├── Production Account 1 (App Team A - Production)
    ├── Production Account 2 (App Team B - Production)
    └── Production Shared Services (Monitoring, backup)
```

### A.2.2 Network Separation

**VPC (Virtual Private Cloud) per Environment**:
- Development VPC: 10.1.0.0/16
- Testing VPC: 10.2.0.0/16
- Staging VPC: 10.3.0.0/16
- Production VPC: 10.4.0.0/16

**VPC Peering**: DISABLED between non-adjacent environments
- Dev-Test peering: Allowed (code promotion)
- Test-Staging peering: Allowed (code promotion)
- Staging-Prod peering: Allowed (deployment pipeline only)
- **Dev-Prod peering**: PROHIBITED

**Security Groups**:
- Default deny (no inbound traffic unless explicitly allowed)
- Separate security groups per environment
- Production security groups managed via Infrastructure-as-Code only

### A.2.3 Access Control

**IAM (Identity and Access Management)**:
- **Developers**: IAM roles in Dev account only
- **QA**: IAM roles in Test account only
- **Operations**: IAM roles in Production account (cross-account assume role from staging)
- **Break-Glass**: Emergency IAM role in Production (requires MFA + approval)

**Cross-Account Access**:
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam::DEV-ACCOUNT:root"},
    "Action": "sts:AssumeRole",
    "Resource": "arn:aws:iam::TEST-ACCOUNT:role/DeploymentRole",
    "Condition": {"StringEquals": {"sts:ExternalId": "unique-external-id"}}
  }]
}
```

### A.2.4 Data Separation

**S3 Buckets**:
- dev-app-data-ACCOUNT_ID
- test-app-data-ACCOUNT_ID
- staging-app-data-ACCOUNT_ID
- prod-app-data-ACCOUNT_ID

**RDS Databases**:
- Separate RDS instances per environment
- Production RDS: encrypted at rest (KMS), automated backups, Multi-AZ
- Dev/Test RDS: may use smaller instances, less redundancy

**Secrets Manager**:
- Separate secrets per environment (dev/, test/, staging/, prod/ prefixes)
- Production secrets: automatic rotation enabled
- Cross-account secret access: PROHIBITED

---

## A.3 Azure Multi-Subscription Pattern

### A.3.1 Architecture Overview

**Azure Management Groups**:
```
Tenant Root Group
├── Security Management Group
│   ├── Audit Subscription
│   └── Security Tools Subscription
├── Development Management Group
│   ├── Dev Subscription (App Team A)
│   └── Dev Subscription (App Team B)
├── Testing Management Group
│   ├── Test Subscription (App Team A)
│   └── Test Subscription (App Team B)
├── Staging Management Group
│   ├── Staging Subscription (App Team A)
│   └── Staging Subscription (App Team B)
└── Production Management Group
    ├── Production Subscription (App Team A)
    └── Production Subscription (App Team B)
```

### A.3.2 Network Separation

**Virtual Networks (VNets)** per subscription:
- Development VNet: 10.10.0.0/16
- Testing VNet: 10.20.0.0/16
- Staging VNet: 10.30.0.0/16
- Production VNet: 10.40.0.0/16

**Network Security Groups (NSGs)**:
- Deny all traffic between environments (default)
- Explicit allow rules for deployment pipelines
- Production NSG: managed via Azure Policy (prevent manual changes)

**VNet Peering**: Controlled
- Hub-and-spoke topology (central hub for shared services)
- Production VNet does NOT peer with Dev VNet

### A.3.3 Access Control

**Azure RBAC (Role-Based Access Control)**:
- **Developers**: Contributor role in Dev subscription only
- **QA**: Contributor role in Test subscription only
- **Operations**: Owner role in Production subscription
- **Security Team**: Security Reader role in all subscriptions

**Azure AD Privileged Identity Management (PIM)**:
- Production access: Just-in-Time (JIT) activation required
- Activation requires approval + MFA
- Maximum activation time: 4 hours

**Managed Identity**:
- System-assigned managed identities per environment
- Production managed identity cannot access dev/test resources

### A.3.4 Data Separation

**Azure Storage Accounts**:
- devstorageaccount{uniqueid}
- teststorageaccount{uniqueid}
- stagingstorageaccount{uniqueid}
- prodstorageaccount{uniqueid}

**Azure SQL Database**:
- Separate Azure SQL Server per environment
- Production: Transparent Data Encryption (TDE) enabled, geo-replication
- Dev/Test: Basic tier acceptable, no geo-replication

**Azure Key Vault**:
- Separate Key Vault per environment
- Production secrets: soft delete enabled, purge protection
- Access policies: environment-specific

---

## A.4 GCP (Google Cloud Platform) Multi-Project Pattern

### A.4.1 Architecture Overview

**GCP Folder Hierarchy**:
```
Organization
├── Security Folder
│   ├── Audit Project
│   └── Security Tools Project
├── Development Folder
│   ├── Dev Project - Team A
│   └── Dev Project - Team B
├── Testing Folder
│   ├── Test Project - Team A
│   └── Test Project - Team B
├── Staging Folder
│   ├── Staging Project - Team A
│   └── Staging Project - Team B
└── Production Folder
    ├── Production Project - Team A
    └── Production Project - Team B
```

### A.4.2 Network Separation

**VPC Networks** per project:
- Development VPC: 10.100.0.0/16
- Testing VPC: 10.200.0.0/16
- Staging VPC: 10.300.0.0/16
- Production VPC: 10.400.0.0/16

**Firewall Rules**:
- Default deny ingress, allow egress
- Separate firewall rules per environment
- Production firewall rules: version controlled, change-managed

**VPC Peering**: Restricted
- Shared VPC for organization-wide services
- Production VPC isolated (no peering with dev/test)

### A.4.3 Access Control

**IAM (Identity and Access Management)**:
- **Developers**: Project Editor role in Dev project only
- **QA**: Project Editor role in Test project only
- **Operations**: Project Owner role in Production project
- **Service Accounts**: Separate per environment (dev-sa@, test-sa@, prod-sa@)

**Organization Policy Constraints**:
```yaml
constraints:
  - name: iam.allowedPolicyMemberDomains
    list_policy:
      allowed_values: ["organization-domain.com"]
  - name: compute.vmExternalIpAccess
    list_policy:
      denied_values: ["all"] # Production VMs: no external IPs
```

### A.4.4 Data Separation

**Cloud Storage Buckets**:
- dev-app-bucket-PROJECT_ID
- test-app-bucket-PROJECT_ID
- staging-app-bucket-PROJECT_ID
- prod-app-bucket-PROJECT_ID

**Cloud SQL**:
- Separate Cloud SQL instances per environment
- Production: high availability, automated backups, point-in-time recovery
- Dev/Test: standard configuration

**Secret Manager**:
- Separate secrets per project
- Production secrets: versioning enabled, automatic replication

---

## A.5 Kubernetes Namespace-Based Separation

### A.5.1 Namespace Structure

**Namespaces per Environment** (if shared cluster - NOT RECOMMENDED for production):
```
kubectl get namespaces
- development (dev workloads)
- testing (test workloads)
- staging (staging workloads - if on shared cluster)
- production (RECOMMENDED: separate cluster entirely)
```

**RECOMMENDED: Separate Clusters**:
- Development Cluster (all dev namespaces)
- Testing Cluster (all test namespaces)
- Production Cluster (all production namespaces, highly isolated)

### A.5.2 Network Policies

**NetworkPolicy Enforcement**:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-from-other-namespaces
  namespace: production
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector: {} # Allow only from same namespace
```

**Deny All Cross-Namespace Traffic** (default):
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
```

### A.5.3 RBAC and Access Control

**Role Bindings per Namespace**:
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: developers-binding
  namespace: development
subjects:
- kind: Group
  name: developers
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: developer-role
  apiGroup: rbac.authorization.k8s.io
```

**Production Namespace**: Operations team ONLY
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: operations-binding
  namespace: production
subjects:
- kind: Group
  name: operations-team
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: admin
  apiGroup: rbac.authorization.k8s.io
```

### A.5.4 Resource Quotas and Limits

**Prevent Resource Exhaustion**:
```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: namespace-quota
  namespace: development
spec:
  hard:
    requests.cpu: "10"
    requests.memory: 20Gi
    persistentvolumeclaims: "10"
```

---

## A.6 On-Premises / Traditional Infrastructure

### A.6.1 Physical/Virtual Server Separation

**Server Allocation**:
- Development Servers: dev-app-01, dev-app-02, dev-db-01
- Testing Servers: test-app-01, test-app-02, test-db-01
- Staging Servers: stage-app-01, stage-app-02, stage-db-01
- Production Servers: prod-app-01, prod-app-02, prod-db-01

**VMware vSphere**:
- Separate clusters per environment tier (Dev Cluster, Test Cluster, Prod Cluster)
- DRS (Distributed Resource Scheduler) rules: prevent VM migration between clusters
- Resource pools: isolate environment workloads

### A.6.2 Network Segmentation (VLANs)

**VLAN Structure**:
- VLAN 10: Development (10.10.0.0/24)
- VLAN 20: Testing (10.20.0.0/24)
- VLAN 30: Staging (10.30.0.0/24)
- VLAN 40: Production (10.40.0.0/24)

**Firewall Rules** (between VLANs):
```
Default: DENY ALL
Allow: VLAN 10 → VLAN 20 (Dev to Test deployment)
Allow: VLAN 20 → VLAN 30 (Test to Staging deployment)
Allow: VLAN 30 → VLAN 40 (Staging to Prod deployment - specific ports only)
Deny: VLAN 10 → VLAN 40 (Dev to Prod - absolutely prohibited)
```

### A.6.3 Active Directory Separation

**AD Organizational Units (OUs)**:
```
root.local
├── Development OU
│   ├── Dev Users
│   ├── Dev Computers
│   └── Dev Service Accounts
├── Testing OU
│   ├── Test Users
│   ├── Test Computers
│   └── Test Service Accounts
└── Production OU
    ├── Prod Users (Operations only)
    ├── Prod Computers
    └── Prod Service Accounts
```

**Group Policy Objects (GPOs)**:
- Separate GPOs per environment
- Production GPO: Strictest security settings
- Development GPO: Developer-friendly settings

---

## A.7 Hybrid Cloud Architecture

### A.7.1 Multi-Cloud Environment Separation

**Architecture**:
- On-Premises: Production database (compliance requirement - data residency)
- AWS: Development and Testing (cloud scalability)
- Azure: Staging and Production applications (Azure PaaS services)

**Network Connectivity**:
- AWS Direct Connect: Dev/Test to on-premises (low latency testing)
- Azure ExpressRoute: Staging/Prod to on-premises (production data access)
- **NO direct connection**: Dev (AWS) to Prod (Azure) - prevents cross-environment access

### A.7.2 Identity Federation

**Single Sign-On (SSO) Integration**:
- On-Premises Active Directory (identity source)
- Azure AD Connect (sync to Azure AD)
- AWS IAM federated to Azure AD (SAML)

**Environment-Specific Access**:
- Azure AD Conditional Access policies control access per environment
- Developers: Can authenticate to AWS Dev only
- Operations: Can authenticate to Azure Prod only

---

## A.8 Deployment Pipeline Integration

### A.8.1 CI/CD Pipeline Architecture

**Pipeline Stages per Environment**:
```
GitHub (Source Control)
   ↓
Jenkins / GitLab CI / GitHub Actions (CI/CD)
   ↓
┌─────────────────────────────────────────────┐
│  Build Stage (artifact creation)            │
└─────────────────────────────────────────────┘
   ↓
┌─────────────────────────────────────────────┐
│  Dev Deployment (automatic)                 │
│  → AWS Dev Account or Azure Dev Subscription│
└─────────────────────────────────────────────┘
   ↓ (automated tests pass)
┌─────────────────────────────────────────────┐
│  Test Deployment (automatic or manual)      │
│  → AWS Test Account or Azure Test Sub      │
└─────────────────────────────────────────────┘
   ↓ (QA approval)
┌─────────────────────────────────────────────┐
│  Staging Deployment (manual trigger)        │
│  → AWS Staging Account or Azure Staging Sub│
└─────────────────────────────────────────────┘
   ↓ (CAB approval)
┌─────────────────────────────────────────────┐
│  Production Deployment (manual + approval)  │
│  → AWS Prod Account or Azure Prod Sub      │
└─────────────────────────────────────────────┘
```

**Environment-Specific Credentials**:
- CI/CD system has separate credentials per environment (stored in secret manager)
- Production deployment credentials: highest privilege, tightly controlled
- Deployment logs: complete audit trail

---

## A.9 Comparison Matrix

| Architecture Aspect | AWS | Azure | GCP | Kubernetes | On-Premises |
|---------------------|-----|-------|-----|------------|-------------|
| Environment Isolation | Separate Accounts | Separate Subscriptions | Separate Projects | Separate Clusters (recommended) or Namespaces | VLANs + Separate Servers |
| Network Separation | VPCs + Security Groups | VNets + NSGs | VPC Networks + Firewall Rules | NetworkPolicies | VLANs + Firewall |
| Access Control | IAM Roles | Azure RBAC + PIM | IAM + Org Policies | RBAC | Active Directory + GPOs |
| Data Storage | S3 (buckets per env) | Storage Accounts (per env) | Cloud Storage (buckets per env) | PersistentVolumes (per namespace) | File shares (per env) |
| Secrets Management | Secrets Manager / Parameter Store | Key Vault | Secret Manager | Secrets (K8s) + External Secrets | CyberArk / Vault |
| Deployment Method | CodePipeline / Jenkins | Azure DevOps / GitHub Actions | Cloud Build / Jenkins | Helm / Kustomize / ArgoCD | Jenkins / Ansible |
| Cost Model | Pay-per-use (can be expensive for many accounts) | Pay-per-subscription | Pay-per-project | Cluster costs | Fixed infrastructure costs |

---

## A.10 Selection Criteria

**Choose AWS Multi-Account** if:
- Already on AWS
- Need fine-grained isolation (separate billing, governance)
- Compliance requires account-level separation

**Choose Azure Multi-Subscription** if:
- Already on Azure
- Microsoft ecosystem (Azure AD, Office 365 integration)
- Need Azure PaaS services

**Choose GCP Multi-Project** if:
- Already on GCP
- Data analytics focus (BigQuery, Dataflow)
- Google Kubernetes Engine (GKE) preferred

**Choose Kubernetes Namespaces** if:
- Container-native applications
- Multi-cloud portability required
- Development/testing only (NOT RECOMMENDED for production isolation)

**Choose On-Premises** if:
- Data residency requirements (cannot use cloud)
- Existing infrastructure investment
- Security/compliance mandates on-premises

**Choose Hybrid** if:
- Transition to cloud (some workloads on-prem, some cloud)
- Data residency + cloud scalability
- Best-of-breed (use best cloud service for each workload)

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | [Name] | ________________ | [Date] |
| Cloud Architect | [Name] | ________________ | [Date] |
| IT Operations Manager | [Name] | ________________ | [Date] |

---

*End of Annex A - Environment Architecture Patterns*
