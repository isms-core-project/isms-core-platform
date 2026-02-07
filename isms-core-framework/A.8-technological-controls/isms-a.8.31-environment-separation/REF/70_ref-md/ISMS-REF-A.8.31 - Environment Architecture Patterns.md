**ISMS-REF-A.8.31 – Environment Architecture Patterns**
**Technical Reference for Infrastructure Implementation**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Environment Architecture Patterns |
| **Document Type** | Reference Document (Non-ISMS Technical Reference) |
| **Document ID** | ISMS-REF-A.8.31 |
| **Document Creator** | IT Operations Manager / Cloud Architecture |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | IT Operations Manager (Technical Reference - No Executive Approval Required) |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | IT Operations / Cloud Architecture | Initial technical reference for environment separation patterns |

**Review Cycle**: As needed (technology and platform evolution)  
**Next Review Date**: [Date + 12 months]  
**Approvers**: IT Operations Manager / Cloud Architect (technical reference, no ISMS approval required)

**Distribution**: IT Operations, Cloud Architecture, DevOps, System Owners (for technical implementation awareness)

---

⚠️ **IMPORTANT – NON-ISMS TECHNICAL SUPPORT DOCUMENT**

This document is provided for informational and awareness purposes only.

- This document is NOT part of the Information Security Management System (ISMS).
- This document does NOT define mandatory environment separation controls or requirements.
- This document does NOT establish binding requirements, deadlines, KPIs, or SLAs.
- This document does NOT mandate the use, prohibition, or configuration of specific cloud platforms, architectures, or tools.
- This document does NOT override or extend any ISMS policy.

All binding environment separation requirements, obligations, and governance decisions are defined exclusively in **ISMS-POL-A.8.31 (Environment Separation Policy)** and other approved ISMS documentation.

This document serves solely as a technical reference to:

- Describe commonly encountered environment architecture patterns
- Provide platform-specific implementation examples
- Support architecture decision-making during implementation
- Inform technical discussions and future implementation planning
- **This document must not be used as audit evidence of implementation**

Use of this document does not imply implementation, compliance, or operational maturity.

**Critical Positioning Statement**:
This document intentionally provides technical detail beyond what is required for ISO/IEC 27001 policy documentation. Its purpose is technical awareness only. No auditor conclusions shall be drawn from the presence, absence, or classification of any architecture pattern, platform, or configuration listed herein.

---

# Document Purpose and Scope

## Purpose

This document provides technical reference patterns for implementing environment separation across common infrastructure platforms. It is intended to support:

- Technical awareness of platform-specific separation approaches
- Understanding of cloud provider account/subscription models
- Context for infrastructure architecture decisions
- Future implementation planning discussions
- Tool and platform evaluation criteria

## What This Document Is NOT

This document does NOT:

- Define [Organization]'s required or prohibited architectures
- Establish mandatory implementation requirements
- Create compliance obligations or audit criteria
- Replace ISMS-POL-A.8.31 policy requirements
- Mandate specific cloud providers or platforms
- Replace vendor documentation or best practices

## Relationship to ISMS Policy

**Binding Requirements**: ISMS-POL-A.8.31 defines **WHAT** environment separation is required (network isolation, infrastructure separation, credential separation, etc.)

**This Document**: Provides **HOW** those requirements can be implemented on specific platforms (AWS multi-account, Azure subscriptions, Kubernetes namespaces, etc.)

Organizations choose platforms and architectures appropriate to their needs. The requirement is separation; the implementation varies.

---

# AWS (Amazon Web Services) Multi-Account Pattern

## Architecture Overview

**AWS Organizations Structure**:

Recommended structure using Organizational Units (OUs) to group accounts by environment:

```
Root Organization
├── Security OU (Organizational Unit)
│   ├── Audit Account (CloudTrail logs, compliance reporting)
│   └── Security Tooling Account (GuardDuty, SecurityHub, Inspector)
├── Development OU
│   ├── Dev Account 1 (Application Team A - Development)
│   ├── Dev Account 2 (Application Team B - Development)
│   └── Shared Dev Services Account (DevOps tools, artifact repositories)
├── Testing OU
│   ├── Test Account 1 (Application Team A - Testing)
│   ├── Test Account 2 (Application Team B - Testing)
│   └── Shared Test Services Account (QA automation tools)
├── Staging OU
│   ├── Staging Account 1 (Application Team A - Pre-Production)
│   └── Staging Account 2 (Application Team B - Pre-Production)
└── Production OU
    ├── Production Account 1 (Application Team A - Production)
    ├── Production Account 2 (Application Team B - Production)
    └── Production Shared Services (Monitoring, backup, disaster recovery)
```

**Why Multi-Account**:

- **IAM Boundary**: IAM policies cannot cross account boundaries (prevents dev → prod access)
- **Blast Radius**: Compromise of dev account does not affect production
- **Cost Attribution**: Separate billing per environment
- **Service Limits**: Separate service quotas per account
- **Audit Trail**: CloudTrail logs separate per account

## Network Separation

**VPC (Virtual Private Cloud) per Environment**:

Recommended CIDR blocks (RFC 1918 private address space):

- Development VPC: 10.1.0.0/16 (65,536 IPs)
- Testing VPC: 10.2.0.0/16 (65,536 IPs)
- Staging VPC: 10.3.0.0/16 (65,536 IPs)
- Production VPC: 10.4.0.0/16 (65,536 IPs)

**VPC Peering Configuration**:

Controlled peering between adjacent environments only:

- ✅ Dev ↔ Test peering: Allowed (deployment pipelines)
- ✅ Test ↔ Staging peering: Allowed (promotion workflows)
- ✅ Staging ↔ Production peering: Allowed (deployment automation)
- ❌ Dev ↔ Production peering: **PROHIBITED** (direct connection violates separation)

**Security Groups**:

- Default deny (no inbound traffic unless explicitly allowed)
- Separate security groups per environment
- Production security groups: managed via Terraform/CloudFormation only (prevent manual drift)
- Security group naming: `{environment}-{service}-{direction}` (e.g., `prod-web-inbound`)

**Route Tables**:

- Default route to Internet Gateway for public subnets
- NAT Gateway for private subnet outbound
- No routes between non-adjacent VPCs

## Access Control (IAM)

**Role-Based Access Model**:

**Developer IAM Roles** (in Dev Account only):
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["ec2:*", "s3:*", "rds:*"],
    "Resource": "*",
    "Condition": {
      "StringEquals": {"aws:RequestedRegion": "eu-central-1"}
    }
  }]
}
```

**Operations IAM Roles** (in Production Account):

- Require MFA for console access
- Session duration: 4 hours maximum
- Require approval workflow (ServiceNow, Jira) before AssumeRole

**Cross-Account AssumeRole** (Deployment Pipeline):
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam::DEV-ACCOUNT-ID:root"},
    "Action": "sts:AssumeRole",
    "Resource": "arn:aws:iam::TEST-ACCOUNT-ID:role/DeploymentRole",
    "Condition": {
      "StringEquals": {"sts:ExternalId": "unique-deployment-external-id"}
    }
  }]
}
```

**Break-Glass Emergency Role** (Production):
```json
{
  "RoleName": "EmergencyBreakGlassRole",
  "MFARequired": true,
  "ApprovalRequired": true,
  "SessionDuration": 14400,
  "Logging": "All actions logged to CloudTrail + SNS alert"
}
```

## Data Separation

**S3 Buckets** (per environment):

- Naming: `{environment}-{app}-{purpose}-{account-id}`
- Examples:
  - `dev-webapp-data-123456789012`
  - `test-webapp-data-234567890123`
  - `prod-webapp-data-345678901234`

**S3 Bucket Policies** (production - prevent cross-account access):
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Deny",
    "Principal": "*",
    "Action": "s3:*",
    "Resource": "arn:aws:s3:::prod-webapp-data-*/*",
    "Condition": {
      "StringNotEquals": {"aws:PrincipalAccount": "PROD-ACCOUNT-ID"}
    }
  }]
}
```

**RDS Databases**:

- Separate RDS instances per environment
- Production RDS: 
  - Encrypted at rest (AWS KMS customer-managed key)
  - Automated backups (7-35 day retention)
  - Multi-AZ deployment (high availability)
  - Enhanced monitoring enabled
- Dev/Test RDS:
  - May use smaller instance types
  - Single-AZ acceptable
  - Shorter backup retention (7 days)

**AWS Secrets Manager**:

- Separate secrets per environment
- Naming convention: `{environment}/{service}/{secret}` (e.g., `prod/webapp/db-password`)
- Production secrets: automatic rotation enabled (30-90 days)
- Cross-account secret access: **PROHIBITED** via resource policies

## Deployment Pipeline Integration

**CodePipeline Structure**:

```
Source (CodeCommit/GitHub)
  ↓
Build (CodeBuild in Dev Account)
  ↓
Deploy to Dev Account (Automatic)
  ↓
Test in Test Account (Automatic after build success)
  ↓
Deploy to Staging Account (Manual approval)
  ↓
Deploy to Production Account (Manual approval + CAB)
```

**Cross-Account Deployment Role**:

- Pipeline in Dev account assumes role in target accounts
- Time-limited credentials (1 hour session)
- Audit trail in CloudTrail for all deployments

---

# Azure Multi-Subscription Pattern

## Architecture Overview

**Azure Management Groups Hierarchy**:

```
Tenant Root Group
├── Security Management Group
│   ├── Audit Subscription (Azure Monitor logs, Log Analytics)
│   └── Security Tools Subscription (Microsoft Defender, Sentinel)
├── Development Management Group
│   ├── Dev Subscription - Team A
│   └── Dev Subscription - Team B
├── Testing Management Group
│   ├── Test Subscription - Team A
│   └── Test Subscription - Team B
├── Staging Management Group
│   ├── Staging Subscription - Team A
│   └── Staging Subscription - Team B
└── Production Management Group
    ├── Production Subscription - Team A
    └── Production Subscription - Team B
```

**Why Multi-Subscription**:

- **Azure Policy Enforcement**: Policies applied at Management Group level cascade to subscriptions
- **RBAC Boundary**: Azure RBAC does not cross subscription boundaries
- **Cost Management**: Separate billing and budgets per subscription
- **Service Limits**: Separate quota limits per subscription
- **Blast Radius Containment**: Dev subscription compromise isolated from production

## Network Separation

**Virtual Networks (VNets)** per subscription:

- Development VNet: 10.10.0.0/16
- Testing VNet: 10.20.0.0/16
- Staging VNet: 10.30.0.0/16
- Production VNet: 10.40.0.0/16

**Network Security Groups (NSGs)**:

- Default deny all inbound
- Explicit allow rules for required traffic
- Production NSG: managed via Azure Policy (prevent manual override)

**VNet Peering**:

- Hub-and-spoke topology (central hub VNet for shared services)
- Spoke VNets (Dev, Test, Staging, Prod) peer to Hub only
- Transitive routing disabled (Dev cannot reach Prod via Hub)
- User-Defined Routes (UDRs) control traffic flow

## Access Control (Azure RBAC)

**Role Assignments by Environment**:

**Developers** (Dev Subscription):

- Role: Contributor (can create/modify resources)
- Scope: Resource Groups in Dev Subscription
- Cannot access Test/Staging/Prod subscriptions

**QA Team** (Test Subscription):

- Role: Reader (view resources) + specific app access
- Scope: Test Subscription Resource Groups

**Operations** (Production Subscription):

- Role: Contributor (via Privileged Identity Management - PIM)
- Requires: JIT (Just-in-Time) activation + MFA + approval
- Session: 4-hour maximum
- Audit: All actions logged to Log Analytics

**Azure AD Conditional Access**:

- Production access requires:
  - Managed device (Intune compliance)
  - Multi-Factor Authentication (MFA)
  - Trusted network location
  - Risk-based policies (Azure AD Identity Protection)

## Data Separation

**Azure Storage Accounts**:

- Naming: `{env}{app}{purpose}{uniqueid}` (max 24 chars)
- Examples:
  - `devwebappdata001abc`
  - `testwebappdata002xyz`
  - `prodwebappdata003pqr`

**Azure SQL Database**:

- Separate Azure SQL Servers per environment
- Production SQL:
  - Transparent Data Encryption (TDE) enabled
  - Automated backups (7-35 days)
  - Geo-replication for DR
  - Advanced Threat Protection enabled
- Dev/Test SQL:
  - Lower performance tiers acceptable
  - No geo-replication required

**Azure Key Vault**:

- Separate Key Vaults per environment
- Naming: `{environment}-{app}-kv` (e.g., `prod-webapp-kv`)
- Production Key Vault:
  - Soft delete enabled (90-day retention)
  - Purge protection enabled (prevent permanent deletion)
  - Private endpoint (no public access)
  - Firewall rules (allow specific VNets only)

## Azure Policy Enforcement

**Management Group Policies**:

**Production Management Group** (enforced on all production subscriptions):
```json
{
  "policyRule": {
    "if": {
      "allOf": [
        {"field": "type", "equals": "Microsoft.Storage/storageAccounts"},
        {"field": "Microsoft.Storage/storageAccounts/encryption.keySource", "notEquals": "Microsoft.KeyVault"}
      ]
    },
    "then": {"effect": "deny"}
  }
}
```
Translation: Production storage accounts MUST use customer-managed encryption keys.

**Deployment Pipeline**:

- Azure DevOps Pipelines or GitHub Actions
- Service Principal per environment (limited to subscription)
- Pipeline: Dev → Test → Staging → Prod (manual gates between stages)

---

# GCP (Google Cloud Platform) Project Pattern

## Architecture Overview

**GCP Organization Hierarchy**:

```
Organization (example.com)
├── Security Folder
│   ├── Audit Project (Cloud Logging aggregation)
│   └── Security Tools Project (Security Command Center)
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

**Why Multi-Project**:

- **IAM Boundary**: IAM policies scoped to projects
- **Billing**: Separate billing accounts per project
- **Quotas**: Separate resource quotas per project
- **Audit**: Separate Cloud Audit Logs per project

## Network Separation

**VPC Networks** (per project):

- Shared VPC architecture (host project shares VPC with service projects)
- Development VPC: 10.100.0.0/16
- Testing VPC: 10.110.0.0/16
- Staging VPC: 10.120.0.0/16
- Production VPC: 10.130.0.0/16

**VPC Peering**:

- Controlled peering between adjacent environments
- Private Google Access enabled (access GCP services without public IPs)
- No transitive peering (Dev cannot reach Prod)

**Firewall Rules**:

- Default deny all ingress
- Explicit allow rules required
- Production firewall rules: managed via Terraform (prevent manual changes)
- Priority: 1000 (deny all) → 100-500 (explicit allows)

## Access Control (Cloud IAM)

**IAM Roles by Environment**:

**Developers** (Dev Project):

- Role: `roles/editor` (can create/modify resources)
- Scope: Dev project only
- Cannot access other projects

**Operations** (Production Project):

- Role: `roles/compute.admin` + `roles/storage.admin` (limited scope)
- Requires: Context-Aware Access + MFA
- Session: Time-bound (4 hours via temporary credentials)

**Service Accounts** (for applications):

- Separate service accounts per environment
- Naming: `{env}-{app}-sa@{project-id}.iam.gserviceaccount.com`
- Production service accounts: key rotation enforced (90 days)

**Deployment Service Account** (CI/CD):

- Service account in Dev project
- Can impersonate service accounts in Test/Staging/Prod (cross-project deployment)
- Workload Identity Federation (no JSON keys stored in pipeline)

## Data Separation

**Cloud Storage Buckets**:

- Naming: `{project-id}-{app}-{purpose}` (e.g., `prod-team-a-webapp-data`)
- Production buckets:
  - Versioning enabled
  - Retention policy (30-day minimum)
  - Customer-managed encryption keys (Cloud KMS)

**Cloud SQL**:

- Separate Cloud SQL instances per project
- Production SQL:
  - Automated backups (7-365 days)
  - High availability (regional)
  - Private IP only (no public IP)
  - Database encryption with Cloud KMS

**Secret Manager**:

- Separate secrets per project
- Naming: `{environment}_{service}_{secret}` (e.g., `prod_webapp_db_password`)
- Production secrets: automatic rotation (Secret Manager Rotation)

---

# Kubernetes Environment Separation

## Architecture Options

**Option 1: Namespace-Based Separation** (Single Cluster):
```
Kubernetes Cluster (shared)
├── dev namespace
├── test namespace
├── staging namespace
└── production namespace
```

**Pros**: Resource efficiency, simpler management  
**Cons**: Weaker isolation (production shares control plane with dev)  
**Use Case**: Small organizations, low-risk applications

**Option 2: Cluster-Based Separation** (Separate Clusters):
```
Development Cluster
Test Cluster
Staging Cluster
Production Cluster (separate)
```

**Pros**: Strong isolation (production control plane separate)  
**Cons**: Higher operational overhead, higher cost  
**Use Case**: Large organizations, high-risk applications, regulatory requirements

**Recommended**: Cluster-based separation for production, namespace-based for dev/test/staging.

## Namespace-Based Separation

**Namespace Configuration**:

```yaml
# Production namespace with resource quotas
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    environment: production
---
apiVersion: v1
kind: ResourceQuota
metadata:
  name: prod-quota
  namespace: production
spec:
  hard:
    requests.cpu: "100"
    requests.memory: 200Gi
    persistentvolumeclaims: "10"
```

**Network Policies** (isolate namespaces):

```yaml
# Deny all traffic to production namespace except from ingress
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
    - namespaceSelector:

        matchLabels:
          environment: production
```

**RBAC** (Role-Based Access Control):

```yaml
# Developers can only access dev namespace
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: developers
  namespace: dev
subjects:

- kind: Group

  name: developers
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: edit
  apiGroup: rbac.authorization.k8s.io
```

## Cluster-Based Separation

**Separate EKS/AKS/GKE Clusters**:

**Development Cluster**:

- Node count: Auto-scaling 2-10 nodes
- Node size: Smaller instance types (cost optimization)
- Monitoring: Basic (Prometheus)

**Production Cluster**:

- Node count: Auto-scaling 5-50 nodes
- Node size: Performance-optimized instances
- Monitoring: Full observability (Prometheus, Grafana, Jaeger tracing)
- High Availability: Multi-AZ node pools

**Pod Security Standards**:

- Production: `restricted` (highest security)
- Staging: `restricted`
- Test: `baseline`
- Dev: `privileged` (developers need flexibility)

**Service Mesh** (Istio/Linkerd):

- mTLS between services (automatic encryption)
- Traffic policies (rate limiting, circuit breakers)
- Observability (distributed tracing)

---

# On-Premises / Traditional Infrastructure

## VLAN-Based Separation

**Network Segmentation**:

```
Core Network (192.168.0.0/16)
├── VLAN 10: Development (192.168.10.0/24)
├── VLAN 20: Testing (192.168.20.0/24)
├── VLAN 30: Staging (192.168.30.0/24)
└── VLAN 40: Production (192.168.40.0/24)
```

**Firewall Rules Between VLANs**:

- Default deny all traffic
- ACLs (Access Control Lists) permit deployment traffic (dev → test → staging → prod)
- Production VLAN: no inbound from dev/test VLANs

**Physical Switches**:

- VLAN tagging (IEEE 802.1Q)
- Private VLANs (PVLAN) for additional isolation
- Spanning Tree Protocol (STP) for loop prevention

## Physical Separation (High Security)

**Separate Infrastructure Per Environment**:

**Development Data Center / Server Room**:

- Dedicated servers for development workloads
- Separate network switch
- Separate internet connection (optional)

**Production Data Center** (separate physical location):

- Dedicated production servers
- Separate network infrastructure
- Physical access controls (badge readers, biometric)
- 24/7 monitoring

**Use Case**: Financial institutions, government, healthcare (high compliance requirements)

## DMZ and Staging Zones

**Multi-Tier Network Architecture**:

```
Internet
  ↓
Firewall (DMZ)
  ↓
Web Tier VLAN (public-facing)
  ↓
Firewall
  ↓
Application Tier VLAN
  ↓
Firewall
  ↓
Database Tier VLAN (most restricted)
```

**Staging Zone** (mirrors production):

- Separate staging VLAN
- Mirrors production architecture (same tiers, same firewall rules)
- Validates production deployment before actual production

---

# Hybrid Cloud Patterns

## Cloud + On-Premises Hybrid

**Architecture**:

- Development/Test: Cloud-based (AWS/Azure/GCP)
- Production: On-premises data center (regulatory requirement)

**Connectivity**:

- VPN or Direct Connect / ExpressRoute / Cloud Interconnect
- Deployment pipeline deploys to cloud dev/test, then to on-premises prod

**Use Case**: Organizations migrating to cloud (keep production on-prem during transition)

## Multi-Cloud Hybrid

**Architecture**:

- Development: AWS (cost-effective)
- Testing: Azure (PaaS services)
- Production: GCP (high-performance compute)

**Challenges**:

- Complex IAM (separate identity systems)
- Network connectivity (VPN between clouds)
- Cost management (multi-cloud billing)

**Use Case**: Vendor diversification, best-of-breed services

---

# Reference Architecture Diagrams

## AWS Multi-Account Separation

```
┌─────────────────────────────────────────────────────────────┐
│ AWS Organizations Root                                       │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Dev Account  │  │ Test Account │  │ Prod Account │     │
│  │              │  │              │  │              │     │
│  │ VPC 10.1.0.0 │  │ VPC 10.2.0.0 │  │ VPC 10.4.0.0 │     │
│  │              │  │              │  │              │     │
│  │ IAM: Dev     │  │ IAM: QA      │  │ IAM: Ops     │     │
│  │ Roles        │  │ Roles        │  │ Roles (PAM)  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│         │                  │                  │             │
│         └──────────────────┴──────────────────┘             │
│          Deployment Pipeline (CodePipeline)                 │
└─────────────────────────────────────────────────────────────┘
```

## Kubernetes Namespace Separation

```
┌──────────────────────────────────────────────────┐
│ Kubernetes Cluster                                │
│                                                   │
│ ┌────────────┐ ┌────────────┐ ┌────────────┐   │
│ │ dev        │ │ test       │ │ production │   │
│ │ namespace  │ │ namespace  │ │ namespace  │   │
│ │            │ │            │ │            │   │
│ │ Pods       │ │ Pods       │ │ Pods       │   │
│ │ Services   │ │ Services   │ │ Services   │   │
│ │            │ │            │ │            │   │
│ │ Network    │ │ Network    │ │ Network    │   │
│ │ Policy:    │ │ Policy:    │ │ Policy:    │   │
│ │ Allow      │ │ Restricted │ │ Isolated   │   │
│ └────────────┘ └────────────┘ └────────────┘   │
└──────────────────────────────────────────────────┘
```

---

# Decision Framework

## Choosing Separation Approach

| Factor | Namespace-Based | Account/Subscription-Based | Physical Separation |
|--------|----------------|---------------------------|---------------------|
| **Cost** | Low (shared resources) | Medium (separate accounts) | High (duplicate infrastructure) |
| **Isolation** | Medium (logical only) | High (account boundaries) | Maximum (physical) |
| **Compliance** | Low-Medium risk | High risk acceptable | Maximum (financial, healthcare) |
| **Complexity** | Low (single cluster/account) | Medium (multi-account management) | High (separate data centers) |
| **Recommended For** | Small orgs, low risk | Most organizations | Regulated industries |

## Migration Path

**Phase 1**: Start with namespace-based separation (quick to implement)  
**Phase 2**: Migrate to account/subscription-based (stronger isolation)  
**Phase 3**: Consider physical separation for production only (if regulatory requirement)

---

**END OF REFERENCE DOCUMENT**

---

*This technical reference supports ISMS-POL-A.8.31. Implementation decisions should be based on organizational risk assessment and approved by CISO.*

<!-- QA_VERIFIED: 2026-02-01 -->
