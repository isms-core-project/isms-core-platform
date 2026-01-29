# ISMS-IMP-A.8.31-S1
## Environment Architecture Implementation & Assessment

**Document ID**: ISMS-IMP-A.8.31-S1  
**Title**: Environment Architecture Implementation & Assessment  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | IT Operations / Information Security Manager | Initial implementation guide |

**Review Cycle**: Quarterly (or upon infrastructure changes)  
**Approvers**: CISO, IT Operations Manager, Cloud Architect  
**Related Policy**: ISMS-POL-A.8.31-S2.1 (Environment Architecture Requirements)

---

## 1. Purpose and Scope

### 1.1 Overview

This implementation guide provides **step-by-step procedures** for implementing and assessing environment separation architecture in compliance with ISO/IEC 27001:2022 Control A.8.31.

**Objectives**:
- Define environment architecture that separates dev, test, staging, and production
- Implement network, infrastructure, data, and credential separation
- Assess compliance with policy requirements
- Document evidence for audit purposes

**Technology Scope**: This guide is **technology-agnostic** and provides patterns for:
- On-premises infrastructure
- Cloud platforms (AWS, Azure, GCP)
- Container orchestration (Kubernetes)
- Hybrid/multi-cloud environments

### 1.2 Target Audience

- **IT Operations Teams**: Implementing environment separation
- **Cloud Architects**: Designing multi-environment infrastructure
- **DevOps Engineers**: Configuring deployment pipelines
- **Information Security Team**: Assessing compliance
- **Auditors**: Verifying implementation

---

## 2. Environment Architecture Design

### 2.1 Environment Tier Definition

**Step 1: Define Minimum Environment Tiers**

For each application/system in scope, define at minimum:

1. **Development Environment**
   - Purpose: Active code development
   - Users: Developers, DevOps engineers
   - Data: Synthetic/anonymized only
   - Availability: Best effort

2. **Testing/QA Environment**
   - Purpose: Quality assurance, UAT
   - Users: QA team, developers (limited), business users (UAT)
   - Data: Synthetic/anonymized only
   - Availability: 95% during business hours

3. **Production Environment**
   - Purpose: Live business operations
   - Users: Operations team ONLY
   - Data: Real production data
   - Availability: Per SLA (typically 99.5%+)

**Optional but Recommended**:

4. **Staging/Pre-Production Environment**
   - Purpose: Production-like final validation
   - Users: Operations team, senior developers (read-only)
   - Data: Synthetic/anonymized
   - Availability: Production-like

**Documentation Template**:

```markdown
# System: [Application Name]

## Environment Tier Definitions

| Environment | Purpose | Primary Users | Data Type | Availability Target |
|-------------|---------|---------------|-----------|---------------------|
| Development | Code development | Developers, DevOps | Synthetic | Best effort |
| Testing | QA, UAT | QA team, business users | Synthetic/Anonymized | 95% business hours |
| Staging | Pre-prod validation | Operations, Senior Devs | Anonymized | 99% |
| Production | Live operations | Operations ONLY | Production data | 99.9% |

## Business Justification
[Why these environments are necessary for this system]

## Separation Mechanisms
- Network: [VLAN/VPC separation details]
- Infrastructure: [Separate servers/cloud accounts]
- Data: [Separate databases, no prod data in dev/test]
- Credentials: [Separate credentials per environment]
```

**Step 2: Document Environment Naming Convention**

Establish consistent naming to prevent confusion:

**Examples**:
- Hostnames: `dev-app01.internal`, `test-app01.internal`, `prod-app01.internal`
- Cloud accounts: `myorg-dev`, `myorg-test`, `myorg-staging`, `myorg-prod`
- Databases: `dev_myapp`, `test_myapp`, `prod_myapp`
- URLs: `dev.myapp.example.com`, `test.myapp.example.com`, `myapp.example.com`

**Visual Identification** (Production Warning):
- Production systems: Red banner "⚠️ PRODUCTION - Changes Affect Live Users"
- Staging: Yellow banner "STAGING - Production-Like Environment"
- Test: Blue banner "TEST - Quality Assurance Environment"
- Development: Green banner "DEV - Development Environment"

---

## 3. Network Separation Implementation

### 3.1 On-Premises / Data Center

**Step 1: VLAN Segmentation**

Create separate VLANs per environment:

```
VLAN 100 - Development (10.100.0.0/16)
VLAN 200 - Testing (10.200.0.0/16)
VLAN 300 - Staging (10.300.0.0/16)
VLAN 400 - Production (10.400.0.0/16)
```

**Step 2: Routing Policies**

Configure routing to prevent inter-environment traffic:

```
# Example firewall rules (generic syntax)

# Default deny between environments
deny ip 10.100.0.0/16 10.200.0.0/16
deny ip 10.100.0.0/16 10.300.0.0/16
deny ip 10.100.0.0/16 10.400.0.0/16
deny ip 10.200.0.0/16 10.400.0.0/16
deny ip 10.300.0.0/16 10.100.0.0/16

# Allow monitoring from centralized monitoring server
permit ip 10.250.10.5/32 10.0.0.0/8 port 9090  # Prometheus
permit ip 10.0.0.0/8 10.250.10.5/32 port 514   # Syslog

# Allow CI/CD pipeline to staging/production
permit ip 10.250.20.10/32 10.300.0.0/16 port 22  # Deploy to staging
permit ip 10.250.20.10/32 10.400.0.0/16 port 22  # Deploy to production

# All other inter-environment traffic DENIED
```

**Step 3: Verification**

Test network isolation:

```bash
# From development server, attempt to reach production
ping 10.400.10.5  # Should FAIL (timeout or unreachable)

# From test server, attempt to reach production database
telnet prod-db.internal 5432  # Should FAIL (connection refused)

# From monitoring server, verify allowed access
curl http://10.400.10.5:9090/metrics  # Should SUCCEED
```

### 3.2 AWS Cloud

**Step 1: Multi-Account Architecture**

Create separate AWS accounts per environment:

```
Organization: myorg-root
├── OU: Development
│   └── Account: myorg-dev (111111111111)
├── OU: Testing
│   └── Account: myorg-test (222222222222)
├── OU: Staging
│   └── Account: myorg-staging (333333333333)
└── OU: Production
    └── Account: myorg-prod (444444444444)
```

**Benefits**:
- Complete resource isolation
- Separate billing/cost tracking
- Account-level security boundaries
- IAM policy separation

**Step 2: VPC Configuration Per Account**

Each account has separate VPC:

```
Dev Account (111111111111):
  VPC: vpc-dev-main (10.100.0.0/16)
  
Test Account (222222222222):
  VPC: vpc-test-main (10.200.0.0/16)
  
Staging Account (333333333333):
  VPC: vpc-staging-main (10.300.0.0/16)
  
Production Account (444444444444):
  VPC: vpc-prod-main (10.400.0.0/16)
```

**Step 3: Security Groups - Default Deny**

Production account security group (example):

```json
{
  "GroupName": "prod-app-sg",
  "Description": "Production application security group",
  "VpcId": "vpc-prod-main",
  "IpPermissions": [
    {
      "IpProtocol": "tcp",
      "FromPort": 443,
      "ToPort": 443,
      "IpRanges": [{"CidrIp": "0.0.0.0/0", "Description": "HTTPS from internet"}]
    }
  ],
  "IpPermissionsEgress": [
    {
      "IpProtocol": "-1",
      "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
    }
  ]
}
```

**Step 4: Cross-Account Access Control**

NO VPC peering between dev/test and production.

Allowed cross-account access (via IAM roles):
- CI/CD pipeline (Jenkins/GitLab in shared account) → Staging/Production
- Monitoring (CloudWatch cross-account) → All environments
- Backup service → All environments

**Verification**:

```bash
# Verify VPC isolation
aws ec2 describe-vpc-peering-connections --profile prod
# Should show NO peering connections to dev/test accounts

# Verify security group rules
aws ec2 describe-security-groups --group-ids sg-prod-app --profile prod
# Review ingress/egress rules
```

### 3.3 Azure Cloud

**Step 1: Multi-Subscription Architecture**

Create separate Azure subscriptions per environment:

```
Management Group: myorg-root
├── Management Group: Development
│   └── Subscription: myorg-dev-sub
├── Management Group: Testing
│   └── Subscription: myorg-test-sub
├── Management Group: Staging
│   └── Subscription: myorg-staging-sub
└── Management Group: Production
    └── Subscription: myorg-prod-sub
```

**Step 2: Virtual Network Per Subscription**

Each subscription has separate VNet:

```
Dev Subscription:
  VNet: vnet-dev-main (10.100.0.0/16)
  
Test Subscription:
  VNet: vnet-test-main (10.200.0.0/16)
  
Staging Subscription:
  VNet: vnet-staging-main (10.300.0.0/16)
  
Production Subscription:
  VNet: vnet-prod-main (10.400.0.0/16)
```

**Step 3: Network Security Groups**

Configure NSGs to block inter-environment traffic:

```json
{
  "name": "nsg-prod-app",
  "properties": {
    "securityRules": [
      {
        "name": "Allow-HTTPS-Inbound",
        "properties": {
          "protocol": "Tcp",
          "sourcePortRange": "*",
          "destinationPortRange": "443",
          "sourceAddressPrefix": "Internet",
          "destinationAddressPrefix": "*",
          "access": "Allow",
          "priority": 100,
          "direction": "Inbound"
        }
      },
      {
        "name": "Deny-All-Inbound",
        "properties": {
          "protocol": "*",
          "sourcePortRange": "*",
          "destinationPortRange": "*",
          "sourceAddressPrefix": "*",
          "destinationAddressPrefix": "*",
          "access": "Deny",
          "priority": 4096,
          "direction": "Inbound"
        }
      }
    ]
  }
}
```

**Verification**:

```bash
# List VNet peerings (should be none to dev/test)
az network vnet peering list --resource-group rg-prod --vnet-name vnet-prod-main

# Review NSG rules
az network nsg show --resource-group rg-prod --name nsg-prod-app
```

### 3.4 GCP Cloud

**Step 1: Multi-Project Architecture**

Create separate GCP projects per environment:

```
Organization: myorg.com
├── Folder: Development
│   └── Project: myorg-dev (dev-project-123456)
├── Folder: Testing
│   └── Project: myorg-test (test-project-234567)
├── Folder: Staging
│   └── Project: myorg-staging (staging-project-345678)
└── Folder: Production
    └── Project: myorg-prod (prod-project-456789)
```

**Step 2: VPC Network Per Project**

Each project has separate VPC network:

```
Dev Project:
  VPC: vpc-dev-network (10.100.0.0/16)
  
Test Project:
  VPC: vpc-test-network (10.200.0.0/16)
  
Staging Project:
  VPC: vpc-staging-network (10.300.0.0/16)
  
Production Project:
  VPC: vpc-prod-network (10.400.0.0/16)
```

**Step 3: Firewall Rules**

Configure firewall rules (default deny):

```bash
# Production project firewall rules
gcloud compute firewall-rules create prod-allow-https \
    --project=prod-project-456789 \
    --network=vpc-prod-network \
    --allow=tcp:443 \
    --source-ranges=0.0.0.0/0 \
    --target-tags=prod-app

gcloud compute firewall-rules create prod-deny-all \
    --project=prod-project-456789 \
    --network=vpc-prod-network \
    --action=DENY \
    --rules=all \
    --source-ranges=0.0.0.0/0 \
    --priority=65534
```

**Verification**:

```bash
# List VPC peering connections (should be none to dev/test)
gcloud compute networks peerings list --project=prod-project-456789

# List firewall rules
gcloud compute firewall-rules list --project=prod-project-456789
```

### 3.5 Kubernetes

**Step 1: Separate Clusters Per Environment (Recommended)**

```
Cluster: dev-cluster (GKE/EKS/AKS)
  Nodes: 3 (t3.medium or equivalent)
  Purpose: Development workloads

Cluster: test-cluster
  Nodes: 3 (t3.medium or equivalent)
  Purpose: Testing/QA workloads

Cluster: staging-cluster
  Nodes: 5 (t3.large or equivalent)
  Purpose: Pre-production validation

Cluster: prod-cluster
  Nodes: 10 (t3.xlarge or equivalent)
  Purpose: Production workloads
```

**Step 2: Namespace-Based Separation (If Multi-Tenant Cluster)**

If cost constraints require shared cluster (NOT recommended for production):

```yaml
# Namespace per environment
apiVersion: v1
kind: Namespace
metadata:
  name: dev
  labels:
    environment: development
---
apiVersion: v1
kind: Namespace
metadata:
  name: test
  labels:
    environment: testing
---
apiVersion: v1
kind: Namespace
metadata:
  name: prod
  labels:
    environment: production
```

**Step 3: NetworkPolicy Enforcement**

Enforce namespace isolation with NetworkPolicies:

```yaml
# Production namespace - deny all ingress except from prod namespace
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-cross-namespace
  namespace: prod
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

**Verification**:

```bash
# Test cross-namespace communication (should fail)
kubectl run -it --rm debug --image=busybox --restart=Never -n dev -- \
  wget -O- http://prod-service.prod.svc.cluster.local:8080
# Should timeout or be denied by NetworkPolicy

# Verify NetworkPolicies
kubectl get networkpolicies -n prod
```

---

## 4. Infrastructure Separation Implementation

### 4.1 Compute Resource Separation

**On-Premises / VMware**:

```
Development Cluster:
  - ESXi hosts: esxi-dev-01, esxi-dev-02, esxi-dev-03
  - Resource pool: dev-pool (256GB RAM, 100 vCPU)
  - Storage: dev-datastore (10TB)

Production Cluster:
  - ESXi hosts: esxi-prod-01 through esxi-prod-10
  - Resource pool: prod-pool (2TB RAM, 500 vCPU)
  - Storage: prod-datastore (100TB, enterprise SSD)
  
VMotion: DISABLED between dev and prod clusters
```

**Cloud Infrastructure**:

Already covered in network separation (separate accounts/subscriptions/projects).

### 4.2 Database Separation

**Step 1: Separate Database Instances Per Environment**

**On-Premises Example**:
```
dev-db-server (10.100.10.5):
  - PostgreSQL instance: dev_myapp database
  - MySQL instance: dev_analytics database
  
prod-db-server (10.400.10.5):
  - PostgreSQL instance: prod_myapp database
  - MySQL instance: prod_analytics database
```

**AWS RDS Example**:
```
Dev Account:
  - RDS instance: dev-myapp-db (db.t3.medium)
  - Endpoint: dev-myapp-db.abc123.us-east-1.rds.amazonaws.com
  
Prod Account:
  - RDS instance: prod-myapp-db (db.r5.2xlarge)
  - Endpoint: prod-myapp-db.xyz789.us-east-1.rds.amazonaws.com
```

**Step 2: Verify No Shared Database Servers**

```sql
-- Connect to production database
-- Verify NO development databases exist on same server
SHOW DATABASES;
-- Should show ONLY production databases

-- Check users (no dev users should exist)
SELECT User, Host FROM mysql.user;
-- Should show ONLY production users
```

### 4.3 Storage Separation

**File Storage / Object Storage**:

**AWS S3 Example**:
```
Dev Account:
  - Bucket: myorg-dev-app-data
  - Bucket policy: Deny access from other accounts
  
Prod Account:
  - Bucket: myorg-prod-app-data
  - Bucket policy: Deny access from other accounts
  - Encryption: AWS KMS (production key)
```

**Azure Blob Storage Example**:
```
Dev Subscription:
  - Storage Account: myorgdevdata
  - Container: app-uploads
  
Prod Subscription:
  - Storage Account: myorgproddata
  - Container: app-uploads
  - Encryption: Customer-managed key (production key vault)
```

**Verification**:

```bash
# AWS - verify bucket access from dev account to prod bucket (should fail)
aws s3 ls s3://myorg-prod-app-data --profile dev
# Error: Access Denied

# Azure - verify storage account access from dev to prod (should fail)
az storage blob list --account-name myorgproddata --container-name app-uploads
# Error: AuthorizationPermissionMismatch
```

---

## 5. Credential and Secrets Separation

### 5.1 Password Separation

**Implementation**:

1. Generate unique passwords per environment
2. Store production passwords in PAM vault (CyberArk, BeyondTrust, HashiCorp Vault)
3. Never reuse passwords across environments

**Example Credential Matrix**:

| Service | Development | Testing | Production |
|---------|-------------|---------|------------|
| Database Admin | dev_admin / [unique-pwd-1] | test_admin / [unique-pwd-2] | prod_admin / [stored-in-PAM] |
| Application DB User | dev_app / [unique-pwd-3] | test_app / [unique-pwd-4] | prod_app / [stored-in-PAM] |
| SSH Root | dev_root / [unique-pwd-5] | test_root / [unique-pwd-6] | prod_root / [stored-in-PAM] |

### 5.2 API Key Separation

**AWS IAM Example**:

```
Dev Account:
  IAM User: dev-api-user
  Access Key: AKIA...DEV (for development API calls)
  
Prod Account:
  IAM User: prod-api-user
  Access Key: AKIA...PROD (for production API calls)
```

**Secret Management**:

```bash
# Development - store in environment variables
export DB_PASSWORD="dev_password_123"
export API_KEY="dev_api_key_xyz"

# Production - retrieve from secret manager
AWS_SECRET=$(aws secretsmanager get-secret-value --secret-id prod/db/password)
DB_PASSWORD=$(echo $AWS_SECRET | jq -r '.SecretString')
```

### 5.3 TLS Certificate Separation

**Implementation**:

```
Development:
  - Certificate: dev.myapp.example.com
  - Issuer: Internal CA (self-signed)
  - Private Key: /etc/ssl/private/dev-myapp.key
  
Production:
  - Certificate: myapp.example.com
  - Issuer: Let's Encrypt / DigiCert (publicly trusted CA)
  - Private Key: Stored in PAM vault (never on filesystem)
```

---

## 6. Configuration Management

### 6.1 Environment-Specific Configuration Files

**Application Configuration Example** (Spring Boot):

```
src/main/resources/
├── application.properties (common)
├── application-dev.properties (development)
├── application-test.properties (testing)
├── application-staging.properties (staging)
└── application-prod.properties (production)
```

**application-dev.properties**:
```properties
spring.datasource.url=jdbc:postgresql://dev-db:5432/dev_myapp
spring.datasource.username=dev_app
spring.datasource.password=${DEV_DB_PASSWORD}
logging.level.root=DEBUG
feature.beta.enabled=true
```

**application-prod.properties**:
```properties
spring.datasource.url=jdbc:postgresql://prod-db:5432/prod_myapp
spring.datasource.username=prod_app
spring.datasource.password=${PROD_DB_PASSWORD}
logging.level.root=WARN
feature.beta.enabled=false
```

### 6.2 Infrastructure as Code (IaC) Separation

**Terraform Example**:

```
terraform/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── dev.tfvars
│   ├── test/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── test.tfvars
│   └── prod/
│       ├── main.tf
│       ├── variables.tf
│       └── prod.tfvars
└── modules/
    └── app-infrastructure/
```

**dev.tfvars**:
```hcl
environment = "dev"
instance_type = "t3.micro"
db_instance_class = "db.t3.micro"
enable_monitoring = false
```

**prod.tfvars**:
```hcl
environment = "prod"
instance_type = "t3.xlarge"
db_instance_class = "db.r5.2xlarge"
enable_monitoring = true
multi_az = true
```

---

## 7. Assessment Methodology

### 7.1 Architecture Compliance Assessment

Use the provided Excel assessment workbook: **ISMS-IMP-A.8.31.1.xlsx**

**Assessment Process**:

1. **Inventory All Environments**
   - Document each environment tier (dev, test, staging, prod)
   - Record infrastructure details (servers, cloud accounts, databases)

2. **Assess Network Separation**
   - Review VLAN/VPC configuration
   - Verify firewall rules (default deny between environments)
   - Test network isolation (penetration testing)

3. **Assess Infrastructure Separation**
   - Verify separate compute resources
   - Check database separation
   - Review storage/backup separation

4. **Assess Data Separation**
   - Confirm NO production data in dev/test
   - Review data anonymization procedures
   - Check synthetic data generation

5. **Assess Credential Separation**
   - Verify unique credentials per environment
   - Check production credentials in PAM vault
   - Review secret management

6. **Document Gaps**
   - Identify non-compliance areas
   - Assess risk severity
   - Propose remediation plan

### 7.2 Evidence Collection

Required evidence for audit:

- **Network diagrams** showing environment segmentation
- **Firewall rule exports** demonstrating default deny
- **Cloud account/subscription inventory** (separate per environment)
- **Database instance inventory** (separate per environment)
- **Credential inventory** (demonstrating separation)
- **Penetration test results** validating network isolation
- **Access logs** showing no unauthorized cross-environment access

---

## 8. Common Implementation Patterns

### 8.1 Small Organization (Single Application)

**Pattern**: Namespace-based separation on shared infrastructure

```
Physical Servers: 3 servers (small VMs)
  
Logical Separation:
  - VLANs: dev (VLAN 100), test (VLAN 200), prod (VLAN 300)
  - Databases: Separate PostgreSQL instances per environment
  - Credentials: Unique per environment (prod in basic vault)
  - Deployment: Manual promotion with approval
```

**Cost**: Low  
**Complexity**: Low  
**Compliance**: Adequate with compensating controls

### 8.2 Medium Organization (Multiple Applications)

**Pattern**: Separate cloud accounts per environment

```
AWS Multi-Account:
  - Dev Account: All development workloads
  - Test Account: All testing workloads
  - Prod Account: All production workloads
  
Per Account:
  - VPC per application (app1-vpc, app2-vpc)
  - RDS instances per application
  - S3 buckets per application
  - IAM roles per application
```

**Cost**: Medium  
**Complexity**: Medium  
**Compliance**: Strong separation

### 8.3 Large Organization (Many Applications, Multi-Cloud)

**Pattern**: Separate cloud accounts/subscriptions per application AND environment

```
AWS:
  - app1-dev, app1-test, app1-prod accounts
  - app2-dev, app2-test, app2-prod accounts
  
Azure:
  - app3-dev, app3-test, app3-prod subscriptions
  
GCP:
  - app4-dev, app4-test, app4-prod projects
  
Governance:
  - Centralized IAM (AWS Organizations, Azure AD, GCP Cloud Identity)
  - Centralized monitoring (multi-cloud SIEM)
  - Centralized deployment (Jenkins/GitLab multi-cloud pipelines)
```

**Cost**: High  
**Complexity**: High  
**Compliance**: Maximum separation

---

## 9. Troubleshooting Common Issues

### 9.1 Network Isolation Failures

**Problem**: Developer can access production database from dev workstation

**Root Cause**: Firewall rule allowing 0.0.0.0/0 → production network

**Solution**:
```bash
# Review firewall rules
iptables -L -n | grep 10.400.0.0

# Remove overly permissive rule
iptables -D INPUT -s 0.0.0.0/0 -d 10.400.0.0/16 -j ACCEPT

# Add specific allow rule for authorized sources only
iptables -A INPUT -s 10.250.20.10/32 -d 10.400.0.0/16 -p tcp --dport 22 -j ACCEPT
```

### 9.2 Credential Sharing

**Problem**: Same database password used in dev and production

**Root Cause**: Copy-paste configuration during setup

**Solution**:
```bash
# Generate unique password for production
PROD_PASSWORD=$(openssl rand -base64 32)

# Update production database
psql -h prod-db -U postgres -c "ALTER USER prod_app WITH PASSWORD '$PROD_PASSWORD';"

# Store in PAM vault (example with HashiCorp Vault)
vault kv put secret/prod/db password=$PROD_PASSWORD

# Update application to retrieve from vault (NOT environment variable)
```

### 9.3 Configuration Drift

**Problem**: Staging and production configurations diverge

**Root Cause**: Manual changes to production not reflected in IaC

**Solution**:
```bash
# Detect drift with Terraform
terraform plan -var-file=prod.tfvars

# Output shows differences between IaC and actual state
# Either:
# (a) Update IaC to match production (if change was intentional)
# (b) Apply IaC to revert production change (if change was unauthorized)

terraform apply -var-file=prod.tfvars
```

---

## 10. Continuous Compliance Monitoring

### 10.1 Automated Scanning

Implement continuous compliance scanning:

**Cloud Config Rules (AWS)**:
```bash
# AWS Config rule - check for VPC peering between prod and dev
aws configservice put-config-rule --config-rule \
  '{
    "ConfigRuleName": "no-prod-dev-vpc-peering",
    "Source": {
      "Owner": "AWS",
      "SourceIdentifier": "VPC_PEERING_CONNECTION_CHECK"
    },
    "Scope": {
      "ComplianceResourceTypes": ["AWS::EC2::VPCPeeringConnection"]
    }
  }'
```

**Azure Policy**:
```json
{
  "properties": {
    "displayName": "Audit VNet peering to production",
    "policyType": "Custom",
    "mode": "All",
    "description": "Deny VNet peering from dev/test to production subscription",
    "policyRule": {
      "if": {
        "allOf": [
          {
            "field": "type",
            "equals": "Microsoft.Network/virtualNetworks/virtualNetworkPeerings"
          },
          {
            "field": "Microsoft.Network/virtualNetworks/virtualNetworkPeerings/remoteVirtualNetwork.id",
            "contains": "/subscriptions/prod-subscription-id/"
          }
        ]
      },
      "then": {
        "effect": "deny"
      }
    }
  }
}
```

### 10.2 Compliance Dashboard

Monitor key metrics:
- Environments with proper network separation: **100%** (target)
- Cross-environment VPC peering connections: **0** (target)
- Shared credentials between environments: **0** (target)
- Production data in dev/test: **0 incidents** (target)
- Configuration drift (staging vs prod): **≤ 5%** (target)

---

## 11. Audit Preparation

### 11.1 Evidence Package

Prepare the following for auditors:

1. **Environment Architecture Documentation**
   - Network diagrams per environment
   - Infrastructure inventory (completed assessment workbook)

2. **Separation Evidence**
   - Firewall rule exports
   - Cloud account/subscription list
   - VPC/VNet configuration exports
   - Database instance inventory

3. **Access Control Evidence**
   - User → environment access matrix
   - Production access logs (last 90 days)
   - PAM vault credential list (production)

4. **Testing Evidence**
   - Penetration test report (network isolation)
   - Configuration drift reports
   - Automated scanning results

5. **Exception Documentation**
   - List of systems with exceptions
   - Compensating controls per exception
   - Remediation plans with timelines

### 11.2 Interview Preparation

Be prepared to answer:

- How do you prevent developers from accessing production?
- How do you ensure production data never reaches dev/test?
- How do you detect unauthorized cross-environment access?
- What happens if someone accidentally deploys dev code to production?
- How do you maintain consistency between staging and production?

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Implementation Lead | [Name] | ________________ | [Date] |
| CISO | [Name] | ________________ | [Date] |
| IT Operations Manager | [Name] | ________________ | [Date] |
| Cloud Architect | [Name] | ________________ | [Date] |

---

*End of Document ISMS-IMP-A.8.31-S1*
